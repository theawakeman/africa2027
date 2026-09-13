# -*- coding: utf-8 -*-
"""Evalúa las coordenadas de un país contra las referencias de Photon/Wikidata.

Lee audit/geo/<slug>_queries.json y audit/geo/<slug>_ref.json (respuesta del
navegador) y escribe audit/geo/<slug>_eval.json + una tabla markdown.

Veredictos:
  OK          referencia con el mismo nombre a menos del umbral
  DESPLAZADO  referencia clara (nombre coincide) a más del umbral → propuesta de corrección
  AREA        área extensa (parque, reserva, delta…): la referencia es un centroide;
              el punto de la app está dentro/cerca (< umbral_area) → aceptable
  DUDOSO      hay candidatos pero el nombre no coincide bien: revisar a mano
  SIN_REF     ninguna fuente encuentra el lugar: revisar a mano (¿existe?)

Umbrales (km): punto concreto 1.5 · ciudad 4 · área extensa 15.

Uso:  python3 audit_geo_eval.py <slug>
"""
import json
import math
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEO = ROOT / "audit" / "geo"

AREA_PAT = re.compile(r"\b(parque|parc|park|reserva|réserve|reserve|delta|desierto|desert|lago|lac|lake|"
                      r"bosque|forêt|forest|cordillera|macizo|montes|meseta|plateau|valle|valley|"
                      r"salinas|pan|ruta|pista|corredor|costa|coast|archipiélago|islas|bahía|bay|"
                      r"cuenca|región|region|zona|área|area|santuario|sanctuary|conservancy|"
                      r"transfronterizo|transfrontier|game|wildlife|nacional|national)\b", re.I)
CIUDAD_CATS = ("ciudad", "base", "servicios")


def km(a, b, c, d):
    r = math.pi / 180
    x, y = (c - a) * r, (d - b) * r
    h = math.sin(x / 2) ** 2 + math.cos(a * r) * math.cos(c * r) * math.sin(y / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]+", " ", s)


STOP = set("de del la el los las du des le les of the national park parc parque nacional reserve reserva reserve "
           "hospital hopital centre center regional general embassy embajada consulado consulate cascade cascada "
           "falls lake lac lago isla ile island mount mont monte museo musee museum".split())


def tokens(s):
    return {t for t in norm(s).split() if t and t not in STOP and len(t) > 2}


def coincide(nombre, candidato):
    """¿El nombre del candidato comparte el núcleo del nombre del punto?"""
    a, b = tokens(nombre), tokens(candidato)
    if not a or not b:
        return False
    inter = a & b
    return len(inter) >= max(1, math.ceil(min(len(a), len(b)) * 0.6))


def clase(item):
    if item["type"] == "log":
        return "ciudad" if item["cat"].lower() in ("combustible", "agua potable", "servicio") else "punto"
    if any(c in item["cat"].lower() for c in CIUDAD_CATS):
        return "ciudad"
    if AREA_PAT.search(item["name"]) or AREA_PAT.search(item["cat"]):
        return "area"
    return "punto"


UMBRAL = {"punto": 1.5, "ciudad": 4.0, "area": 15.0}


def evalua(item, ref):
    cands = []
    for c in ref.get("ph", []):
        if "err" in c:
            continue
        cands.append({"src": "osm", "name": c["n"], "kind": f"{c['k']}={c['v']}", "lat": c["lat"], "lon": c["lon"],
                      "d": c["d"], "match": coincide(item["q"][0], c["n"]) or any(coincide(q, c["n"]) for q in item["q"])})
    for c in ref.get("wd", []):
        if "err" in c:
            continue
        cands.append({"src": "wd", "name": c.get("l") or c["id"], "kind": c.get("t") or "", "lat": c["lat"], "lon": c["lon"],
                      "d": c["d"], "match": coincide(item["q"][0], c.get("l") or "") or any(coincide(q, c.get("l") or "") for q in item["q"]), "id": c["id"]})
    cl = clase(item)
    um = UMBRAL[cl]
    buenos = [c for c in cands if c["match"]]
    if not cands:
        return "SIN_REF", cl, None, cands
    if not buenos:
        # candidatos sin coincidencia de nombre: si alguno está muy cerca, lo damos por OK-débil
        cerca = min(cands, key=lambda c: c["d"])
        return ("OK?" if cerca["d"] <= um else "DUDOSO"), cl, cerca, cands
    mejor = min(buenos, key=lambda c: c["d"])
    if mejor["d"] <= um:
        return "OK", cl, mejor, cands
    if cl == "area" and mejor["d"] <= 40:
        return "AREA", cl, mejor, cands
    return "DESPLAZADO", cl, mejor, cands


def main(slug):
    q = json.loads((GEO / f"{slug}_queries.json").read_text(encoding="utf-8"))
    refs = {r["id"]: r for r in json.loads((GEO / f"{slug}_ref.json").read_text(encoding="utf-8"))}
    out, filas = [], []
    for it in q["items"]:
        ref = refs.get(it["id"], {})
        ver, cl, mejor, cands = evalua(it, ref)
        out.append({"id": it["id"], "type": it["type"], "name": it["name"], "cat": it["cat"], "clase": cl,
                    "lat": it["lat"], "lon": it["lon"], "veredicto": ver,
                    "ref": mejor, "cands": cands[:4]})
        refs_txt = "; ".join(f"{c['src']}:{c['name']} [{c['kind']}] {c['d']} km" for c in cands[:3]) or "—"
        filas.append(f"| {it['id']} | {it['name'][:48]} | {cl} | **{ver}** | {refs_txt} |")
    (GEO / f"{slug}_eval.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    resumen = {}
    for o in out:
        resumen[o["veredicto"]] = resumen.get(o["veredicto"], 0) + 1
    md = (f"# Evaluación GPS · {slug}\n\nResumen: {resumen}\n\n| id | nombre | clase | veredicto | referencias (fuente:nombre [tipo] distancia) |\n|---|---|---|---|---|\n"
          + "\n".join(filas) + "\n")
    (GEO / f"{slug}_eval.md").write_text(md, encoding="utf-8")
    print(slug, resumen)


if __name__ == "__main__":
    main(sys.argv[1])

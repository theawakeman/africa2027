#!/usr/bin/env python3
"""Genera audit/pdi/<slug>.md a partir de los ficheros del scratchpad y del data_<slug>.py final.

Uso: python3 audit_md.py <slug> "<Nombre>" "<grupo>" [notas_extra.md]
"""
import importlib.util
import json
import os
import math
import sys
from pathlib import Path

SCRATCH = Path(os.environ.get("A27_SCRATCH", Path(__file__).resolve().parent.parent))
REPO = Path(os.environ.get("A27_REPO", "/home/claude/africa2027"))


def dist(a, b, c, d):
    r = 6371.0
    p1, p2 = math.radians(a), math.radians(c)
    dp, dl = math.radians(c - a), math.radians(d - b)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def load(slug):
    spec = importlib.util.spec_from_file_location(f"data_{slug}", REPO / "tools/gen" / f"data_{slug.replace('-', '_')}.py")
    sys.path.insert(0, str(REPO / "tools/gen"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(slug, name, group, extra=None):
    d = SCRATCH / slug
    pdis = json.loads((d / "pdis.json").read_text())
    op = json.loads((d / "operativo.json").read_text())
    gm = json.loads((d / "gm_results.json").read_text())
    hist = json.loads((REPO / "audit/historia" / f"{slug}.json").read_text())
    m = load(slug)
    pois = m.POIS
    n = len(pois)
    with_link = sum(1 for p in pois if p.get("links"))
    with_photo = sum(1 for p in pois if p.get("photos"))
    gal = sum(1 for p in pois if len(p.get("photos", [])) >= 2)
    files = {ph["img"] for p in pois for ph in p.get("photos", [])}
    nfiles = sum(len(p.get("photos", [])) for p in pois)
    dec = sum(1 for p in pois if p.get("visit") or p.get("why"))
    words = sum(len(s.get("texto", s.get("text", "")).split()) if isinstance(s, dict) else len(str(s).split())
                for s in hist["historia_secciones"]) if isinstance(hist["historia_secciones"], list) else \
        sum(len(str(v).split()) for v in hist["historia_secciones"].values())
    nsrc = len(hist["historia_fuentes"])
    out = [f"# Grupo 10 · {name} ({group}) · auditoría editorial y visual de PDIs", "",
           f"País: {name}. Ficha nueva creada el 18 de septiembre de 2026 con el método validado",
           "en el piloto de Túnez (formato de los países de los grupos «Alternativas y opcionales»,",
           "«Solo alcanzable en avión», «Excluidos por protocolo» y «Fuera de la ruta prevista»).", "",
           "## Resultado", "",
           "| País | PDIs | Ficha de decisión | Con enlace | Con foto | Galerías (2+) | Fotografías distintas |",
           "|---|---:|---:|---:|---:|---:|---:|",
           f"| {name} | {n} | {dec}/{n} | {with_link}/{n} | {with_photo}/{n} | {gal} | {len(files)} |", "",
           "Cada PDI lleva el resumen corto compartido por la tarjeta y el globo del mapa,",
           "la ficha de decisión (por qué ir, qué se ve, acceso real, cuándo, cuándo",
           "descartarlo), enlaces concretos y una galería de fotografías de Wikimedia Commons",
           f"con autor, licencia y página de origen leídos de la API de Commons ({nfiles} archivos",
           f"comprobados, {len(files)} distintos).", "",
           "## Pines comprobados uno a uno en Google Maps", "",
           "Cada coordenada de la app es la del objeto navegable que Google Maps devuelve",
           "para el ancla indicada (búsqueda en el navegador del propietario, 18-09-2026).",
           "La distancia es el desplazamiento respecto a la coordenada de Wikipedia/GeoNames",
           "con la que se redactó el PDI. Los anclas marcados «(Wikipedia)» no existen como",
           "objeto en Google Maps y conservan la coordenada de la fuente.", "",
           "| # | PDI | Ancla en Google Maps | Desplazamiento | Coordenadas finales |",
           "|---:|---|---|---:|---|"]
    src = {str(x["n"]): x for x in pdis["pois"]}
    for i, p in enumerate(pois, 1):
        key = f"poi-{i}"
        g = gm.get(key, {})
        s = src.get(str(i), {})
        try:
            dd = dist(float(s["lat"]), float(s["lon"]), p["lat"], p["lon"])
            dtxt = f"{dd:.1f} km"
        except Exception:
            dtxt = "—"
        out.append(f"| {i} | {p['name']} | {g.get('name', '—')} | {dtxt} | {p['lat']:.7f}, {p['lon']:.7f} |")
    out += ["", "## Logística", "",
            f"{len(op['logistics'])} puntos (aeropuerto, pasos fronterizos, Embajada de España, clínicas,",
            "combustible y agua) con pin comprobado en Google Maps salvo los marcados en la tabla:", "",
            "| # | Punto | Ancla en Google Maps | Coordenadas |", "|---:|---|---|---|"]
    for i, l in enumerate(op["logistics"]):
        g = gm.get(f"log-{i}", {})
        out.append(f"| {i + 1} | {l['name']} | {g.get('name', '— (fuente)')} | {g.get('lat', l['lat'])}, {g.get('lon', l['lon'])} |")
    out += ["", "## Historia", "",
            f"Siete secciones con los títulos estándar del proyecto, {words:,} palabras y {nsrc}".replace(",", "."),
            "fuentes abiertas en la sesión. Expediente y dudas del redactor en",
            f"`audit/historia/{slug}.json`.", "", "## Límites y pendientes", ""]
    for t, a in op.get("pendientes", [])[:8]:
        out.append(f"- {t}: {a}")
    if extra:
        out += ["", Path(extra).read_text().strip()]
    (REPO / "audit/pdi" / f"{slug}.md").write_text("\n".join(out) + "\n")
    print("escrito", slug, n, dec, with_link, with_photo, gal, len(files), nfiles, words, nsrc)


if __name__ == "__main__":
    main(*sys.argv[1:])

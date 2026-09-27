# -*- coding: utf-8 -*-
"""Datos del Planificador por puntos (fase 1): assets/js/planificador-puntos.json.

Convierte en datos lo que en las fichas es texto, sin tocar las fichas:

  · Cada punto de interés, con el tiempo de visita en DÍAS (a partir de
    «1 noche», «medio día», «1–2 noches»…) y el perro en cuatro estados.
  · Cada puesto fronterizo de las fichas, con los DOS países que une, el estado
    de esa frontera en el grafo del planificador y si parece un puesto oficial.

Solo biblioteca estándar: se ejecuta en el Mac, en GitHub Actions y aquí.
Los casos dudosos se listan en audit/planificador-puntos-datos.md.
"""
import json
import math
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
GEO = RAIZ / "assets" / "js" / "africa.geo.json"

# ------------------------------------------------------------------ tiempo
_UNIDAD = [
    (re.compile(r"semanas?"), 7.0),
    (re.compile(r"noches?"), 1.0),
    (re.compile(r"d[ií]as?"), 1.0),
    (re.compile(r"(?:h|horas?)\b"), None),   # horas: se convierte aparte
]
_NUM = r"(\d+(?:[.,]\d+)?)"
_TOKEN = re.compile(_NUM + r"(?:\s*–\s*" + _NUM + r")?\s*(semanas?|noches?|d[ií]as?|horas?|h)\b")
_CERO = ("no se visita", "no visitable", "cerrado", "incluido arriba")
_PASO = ("parada técnica", "paso, sin parada", "tránsito")


def _horas_a_dias(h):
    return 0.25 if h <= 3 else 0.5


def dias(texto):
    """(días, nota). Días redondeados a 0,25; nota = '' si la lectura es directa."""
    t = (texto or "").strip().lower()
    if not t or t in ("—", "-"):
        return 0.5, "sin tiempo en la ficha: medio día por defecto"
    if any(k in t for k in _CERO):
        return 0.0, "la ficha dice que no se visita o está cerrado"
    base = re.sub(r"\([^)]*\)", " ", t)            # lo que va entre paréntesis es una variante
    base = re.split(r"\bsi\b", base)[0]              # «6–9 días si se sube» → 6–9 días
    base = base.replace("medio día", "0.5 día").replace("½", "0.5").replace("-", "–")
    valores = []
    for a, b, unidad in _TOKEN.findall(base):
        a = float(a.replace(",", "."))
        b = float(b.replace(",", ".")) if b else a
        v = (a + b) / 2
        if unidad.startswith("h"):
            v = _horas_a_dias(v)
        elif unidad.startswith("semana"):
            v *= 7
        valores.append(v)
    if valores:
        v = max(valores)
        return round(v * 4) / 4, ""
    if any(k in t for k in _PASO):
        return 0.25, "parada breve"
    if "sin pernocta" in t:
        return 0.5, "sin pernocta: medio día"
    return 0.5, f"texto no reconocido («{texto}»): medio día por defecto"


# ------------------------------------------------------------------ perro
def perro(texto):
    s = (texto or "").lower()
    if not s or "pendiente" in s or "por confirmar" in s:
        return "sin_dato"
    if "tratar como prohibido" in s or "prohibido" in s or "no recomendado" in s:
        return "no"
    if "condiciones" in s or "correa" in s or "precaución" in s or "confirmar" in s or "autorización" in s:
        return "condiciones"
    if "permitido" in s or s.startswith("sí") or s == "si":
        return "si"
    return "sin_dato"


# ------------------------------------------------------------------ geometría
def _km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371 * math.asin(min(1, math.sqrt(h)))


def _anillos(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"]]
    return geom["coordinates"]


def _dentro(pt, poligono):
    lat, lon = pt
    dentro = False
    for anillo in poligono:
        for i in range(len(anillo) - 1):
            (x1, y1), (x2, y2) = anillo[i], anillo[i + 1]
            if (y1 > lat) != (y2 > lat):
                x = x1 + (lat - y1) * (x2 - x1) / (y2 - y1)
                if x > lon:
                    dentro = not dentro
    return dentro


def _dist_segmento(pt, a, b):
    """Distancia en km de pt a un segmento (proyección equirectangular local)."""
    k = math.cos(math.radians(pt[0]))
    px, py = pt[1] * k, pt[0]
    ax, ay, bx, by = a[0] * k, a[1], b[0] * k, b[1]
    dx, dy = bx - ax, by - ay
    t = 0 if dx == dy == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy)) * 111.2


def distancia_pais(pt, geom):
    """0 si el punto está dentro del país; si no, km hasta su borde."""
    polys = _anillos(geom)
    if any(_dentro(pt, p) for p in polys):
        return 0.0
    return min(_dist_segmento(pt, anillo[i], anillo[i + 1])
               for p in polys for anillo in p for i in range(len(anillo) - 1))


# ------------------------------------------------------------------ construir
def construir(FULL, C, FRONTERAS, ISLAS):
    nombres = {c[0]: c[1].split(" (")[0] for c in C}
    geo = {f["properties"]["slug"]: f["geometry"]
           for f in json.loads(GEO.read_text(encoding="utf-8"))["features"]}
    vecinos = {}
    for a, b, tipo, nota in FRONTERAS:
        a, b = ("angola" if a == "cabinda" else a), ("angola" if b == "cabinda" else b)
        if a == b:
            continue
        vecinos.setdefault(a, {})[b] = (tipo, nota)
        vecinos.setdefault(b, {})[a] = (tipo, nota)

    puntos, fronteras, dudas = [], [], {"tiempo": [], "frontera": []}
    for slug, d in sorted(FULL.items()):
        for p in d.get("pois", []):
            dd, nota = dias(p.get("time", ""))
            if nota:
                dudas["tiempo"].append((slug, p["name"], p.get("time", ""), dd, nota))
            puntos.append({
                "id": f"{slug}-{p['n']}", "pais": slug, "n": p["n"], "nombre": p["name"],
                "cat": p.get("cat", ""), "prio": p.get("prio", ""),
                "lat": round(p["lat"], 5), "lon": round(p["lon"], 5),
                "tiempo": p.get("time", ""), "dias": dd,
                "perro": perro(p.get("dog", "")), "perro_txt": p.get("dog", ""),
                "ficha": f"paises/{slug}/#poi-{p['n']}",
            })
        for i, lg in enumerate(d.get("logistics", [])):
            if "frontera" not in (lg.get("cat", "").lower()):
                continue
            pt = (lg["lat"], lg["lon"])
            texto = (lg["name"] + " " + lg.get("info", "")).lower()
            nombre_l = lg["name"].lower()
            sub = ("aeropuerto" if "aeropuerto" in nombre_l
                   else "puerto" if nombre_l.startswith("puerto") or "ferry" in nombre_l
                   else "terrestre")
            if sub != "terrestre":
                fronteras.append({"id": f"{slug}-f{i + 1}", "pais": slug, "otro": None, "nombre": lg["name"],
                                  "tipo": sub, "lat": round(lg["lat"], 5), "lon": round(lg["lon"], 5),
                                  "estado": "abierta", "oficial": True, "fiable": True,
                                  "km_otro": None, "km_propio": None, "ficha": f"paises/{slug}/#logistica"})
                continue
            cand = vecinos.get(slug, {})
            # 1) un vecino nombrado en el texto; 2) el vecino más cercano
            nombrados = [v for v in cand if nombres.get(v, v).lower() in texto]
            dist = {v: distancia_pais(pt, geo[v]) for v in cand if v in geo}
            otro = (min(nombrados, key=lambda v: dist.get(v, 9e9)) if nombrados
                    else (min(dist, key=dist.get) if dist else None))
            if otro and not nombrados and dist[otro] > 60:
                otro = None      # frontera con un país fuera del grafo (Israel…) o punto de interior
            km_otro = round(dist.get(otro, 9e9), 1) if otro else None
            km_propio = round(distancia_pais(pt, geo[slug]), 1) if slug in geo else None
            tipo = cand.get(otro, ("", ""))[0] if otro else ""
            oficial = not re.search(r"no (es )?un puesto|no contar con él", texto)
            estado = {"": "abierta", "cerrada": "cerrada", "evitar": "evitar", "ferry": "ferry"}.get(tipo, tipo)
            if estado == "abierta" and (re.search(r"cerrad[ao]", nombre_l) or re.search(
                    r"(frontera|paso|puesto) cerrad[ao]|cerrad[ao] (desde|hasta|al tráfico|a extranjeros)|sigue cerrad|permanece cerrad", texto)):
                estado = "revisar"
            fiable = bool(otro) and km_otro is not None and km_otro <= 25 and (km_propio or 0) <= 25
            f = {"id": f"{slug}-f{i + 1}", "pais": slug, "otro": otro, "nombre": lg["name"], "tipo": sub,
                 "lat": round(lg["lat"], 5), "lon": round(lg["lon"], 5), "estado": estado,
                 "oficial": oficial, "fiable": fiable, "km_otro": km_otro, "km_propio": km_propio,
                 "ficha": f"paises/{slug}/#logistica"}
            fronteras.append(f)
            if not fiable or not oficial or estado == "revisar":
                dudas["frontera"].append(f)
    datos = {"version": 1, "puntos": puntos, "fronteras": fronteras,
             "islas": sorted(ISLAS)}
    return datos, dudas


def informe(datos, dudas):
    fr = [f for f in datos["fronteras"] if f["tipo"] == "terrestre"]
    lineas = [
        "# Datos del Planificador por puntos (fase 1)",
        "",
        "Generado por `tools/gen/planificador_puntos.py` en cada reconstrucción. No se edita a mano:",
        "si algo está mal, se corrige en la ficha del país (tiempo, perro o punto de frontera).",
        "",
        f"- Puntos de interés: {len(datos['puntos'])}; tiempo leído directamente en "
        f"{len(datos['puntos']) - len(dudas['tiempo'])}, con criterio en {len(dudas['tiempo'])}.",
        f"- Puestos fronterizos terrestres: {len(fr)}; emparejados con seguridad {sum(1 for f in fr if f['fiable'])}, "
        f"a revisar {len(dudas['frontera'])}. Puertos y aeropuertos: "
        f"{len(datos['fronteras']) - len(fr)} (no unen dos países por carretera).",
        "- Perro: " + ", ".join(f"{k} {sum(1 for p in datos['puntos'] if p['perro'] == k)}"
                                for k in ("si", "condiciones", "no", "sin_dato")) + ".",
        "",
        "## Tiempos leídos con criterio",
        "",
        "| País | Punto | Texto de la ficha | Días | Criterio |",
        "| --- | --- | --- | --- | --- |",
    ]
    lineas += [f"| {s} | {n} | {t or '—'} | {d:g} | {nota} |" for s, n, t, d, nota in dudas["tiempo"]]
    lineas += ["", "## Puestos fronterizos a revisar", "",
               "`fiable` = a menos de 25 km de los dos países; `oficial` = la ficha no dice que no es un puesto.", "",
               "| País | Punto | Une con | km al otro país | km al propio | Estado | Oficial |",
               "| --- | --- | --- | --- | --- | --- | --- |"]
    lineas += [f"| {f['pais']} | {f['nombre']} | {f['otro'] or '—'} | {f['km_otro']} | {f['km_propio']} | "
               f"{f['estado']} | {'sí' if f['oficial'] else 'no'} |" for f in dudas["frontera"]]
    return "\n".join(lineas) + "\n"

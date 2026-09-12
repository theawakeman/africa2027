# -*- coding: utf-8 -*-
"""Genera assets/js/africa.geo.json: contornos simplificados de África.

Se ejecuta A MANO, no en cada build: el resultado se versiona en el repo para
que la app siga funcionando sin red (es una PWA offline-first).

    python3 gen_geo.py ruta/al/ne_110m_admin_0_countries.geojson

Origen de los datos: Natural Earth 110m (dominio público).
"""
import json
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parents[2]

# Nombre en Natural Earth -> slug nuestro
NOMBRES = {
    "Morocco": "marruecos", "W. Sahara": "sahara-occidental", "Mauritania": "mauritania",
    "Senegal": "senegal", "Gambia": "gambia", "Guinea": "guinea", "Guinea-Bissau": "guinea-bisau",
    "Sierra Leone": "sierra-leona", "Liberia": "liberia", "Côte d'Ivoire": "costa-de-marfil",
    "Ghana": "ghana", "Togo": "togo", "Benin": "benin", "Nigeria": "nigeria",
    "Cameroon": "camerun", "Gabon": "gabon", "Eq. Guinea": "guinea-ecuatorial",
    "Congo": "congo", "Dem. Rep. Congo": "rd-congo", "Angola": "angola",
    "Zambia": "zambia", "Malawi": "malaui", "Tanzania": "tanzania", "Kenya": "kenia",
    "Uganda": "uganda", "Rwanda": "ruanda", "Burundi": "burundi",
    "Mozambique": "mozambique", "Zimbabwe": "zimbabue", "Botswana": "botsuana",
    "South Africa": "sudafrica", "Namibia": "namibia", "Lesotho": "lesoto",
    "eSwatini": "esuatini", "Madagascar": "madagascar",
    "Mali": "mali", "Burkina Faso": "burkina-faso", "Niger": "niger", "Chad": "chad",
    "Central African Rep.": "rca", "Sudan": "sudan", "S. Sudan": "sudan-del-sur",
    "Ethiopia": "etiopia", "Eritrea": "eritrea", "Djibouti": "yibuti", "Somalia": "somalia",
    "Egypt": "egipto", "Libya": "libia", "Tunisia": "tunez", "Algeria": "argelia",
}

DECIMALES = 2          # ~1,1 km: de sobra para un mapa de países
AREA_MINIMA = 0.02     # grados²: descarta islotes que no se verían


def _area(anillo):
    s = 0.0
    for i in range(len(anillo) - 1):
        x1, y1 = anillo[i]
        x2, y2 = anillo[i + 1]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2


def _redondea(anillo):
    out, ant = [], None
    for x, y in anillo:
        p = [round(x, DECIMALES), round(y, DECIMALES)]
        if p != ant:
            out.append(p)
            ant = p
    if len(out) >= 3 and out[0] != out[-1]:
        out.append(out[0])
    return out if len(out) >= 4 else None


def _limpia(geom):
    """Simplifica el polígono y tira los trozos irrelevantes."""
    poligonos = [geom["coordinates"]] if geom["type"] == "Polygon" else geom["coordinates"]
    salida = []
    for poli in poligonos:
        exterior = _redondea(poli[0])
        if not exterior or _area(exterior) < AREA_MINIMA:
            continue
        salida.append([exterior])          # sin agujeros: no aportan nada al mapa
    if not salida:
        return None
    if len(salida) == 1:
        return {"type": "Polygon", "coordinates": salida[0]}
    return {"type": "MultiPolygon", "coordinates": salida}


def main():
    origen = Path(sys.argv[1])
    datos = json.loads(origen.read_text(encoding="utf-8"))
    feats = []
    vistos = set()
    for f in datos["features"]:
        p = f["properties"]
        slug = NOMBRES.get(p.get("NAME")) or NOMBRES.get(p.get("NAME_LONG"))
        if not slug or slug in vistos:
            continue
        geom = _limpia(f["geometry"])
        if not geom:
            continue
        vistos.add(slug)
        feats.append({"type": "Feature", "properties": {"slug": slug}, "geometry": geom})

    faltan = set(NOMBRES.values()) - vistos
    if faltan:
        print("AVISO, sin geometría:", sorted(faltan))

    destino = SITE / "assets/js/africa.geo.json"
    destino.write_text(
        json.dumps({"type": "FeatureCollection", "features": feats},
                   ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8")
    print(f"{len(feats)} países · {destino.stat().st_size/1024:.0f} KB · {destino}")


if __name__ == "__main__":
    main()

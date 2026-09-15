#!/usr/bin/env python3
"""Bloquea regresiones del diseño aprobado de fichas y mapa."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def require(condition, message):
    if not condition:
        raise SystemExit(f"ERROR UI: {message}")


css = (ROOT / "assets/css/site.css").read_text(encoding="utf-8")
map_js = (ROOT / "assets/js/map.js").read_text(encoding="utf-8")
map_html = (ROOT / "mapa/index.html").read_text(encoding="utf-8")
sw = (ROOT / "sw.js").read_text(encoding="utf-8")
visa_html = (ROOT / "visados/index.html").read_text(encoding="utf-8")
visa_js = (ROOT / "assets/js/visamap.js").read_text(encoding="utf-8")

# Contrato visual aprobado: tarjetas compactas, una sola vista del carrusel,
# detalle oculto hasta abrir el modal y una única familia tipográfica de UI.
require('.poi-card { background:' in css and 'font-family:"Archivo"' in css,
        "las fichas deben conservar la tipografía Archivo")
require('.poi-carousel-track { display:flex;' in css,
        "las fotografías del carrusel no pueden apilarse")
require('.poi-carousel figcaption { display:none; }' in css,
        "los pies de foto solo se muestran en la ficha ampliada")
require('.poi-grid > .poi-card .poi-details { display:none; }' in css,
        "el detalle largo debe permanecer oculto en la ficha compacta")
require("translateX(-' + (index * 100) + '%)" in map_js or
        "translateX(-' + (index * 100) + '%)" in (ROOT / "tools/gen/build.py").read_text(encoding="utf-8"),
        "el carrusel debe desplazar una fotografía cada vez")

# Contrato del mapa: control plegado y solo los dos corredores y los PDI activos.
require("{collapsed: true}" in map_js, "la leyenda debe arrancar plegada")
match = re.search(r'<script>var A27_GEN = (\{.*?\});</script>', map_html, re.S)
require(match, "no se encuentra la configuración generada del mapa")
config = json.loads(match.group(1))
require(config.get("defaultOn") == [
    "Corredor de bajada (ida)",
    "Corredor de subida (vuelta)",
    "Puntos de interés",
], "las capas visibles por defecto han cambiado")

# Evita mezclar HTML nuevo con CSS/JS antiguos en una pestaña controlada por PWA.
require("assets/css/site.css?v=" in map_html, "falta versionar el CSS")
require("assets/js/map.js?v=" in map_html, "falta versionar el JavaScript del mapa")
require("self.skipWaiting()" in sw, "el PWA no activa automáticamente la versión coherente")
require("req.destination === 'style' || req.destination === 'script'" in sw,
        "CSS y JavaScript deben usar red primero")
for forbidden in ("./.DS_Store", "./tmp/", "./_to_delete/", "./_incoming/"):
    require(forbidden not in sw, f"la precaché no debe incluir {forbidden}")

country_pages = list((ROOT / "paises").glob("*/index.html"))
carousel_pages = [p for p in country_pages if 'class="poi-carousel"' in p.read_text(encoding="utf-8")]
require(carousel_pages, "no se han encontrado fichas con carrusel")
for page in carousel_pages:
    html = page.read_text(encoding="utf-8")
    require("assets/css/site.css?v=" in html, f"CSS sin versión en {page.relative_to(ROOT)}")
    require('class="poi-carousel-track"' in html, f"carrusel incompleto en {page.relative_to(ROOT)}")

# La pestaña de visados reutiliza el lenguaje visual de CPD y conserva una
# fuente única de fechas en todas las fichas.
require('class="hero small"' in visa_html and 'class="cpdleg"' in visa_html,
        "Visados debe conservar los componentes visuales de CPD")
require("assets/css/site.css?v=" in visa_html, "falta versionar el CSS de Visados")
require("assets/js/visamap.js?v=" in visa_html, "falta versionar el mapa de Visados")
require("function a27VisaMap" in visa_js, "falta el mapa interactivo de Visados")
visa_match = re.search(r'<script>var A27_VISAS = (\{.*?\});</script>', visa_html, re.S)
require(visa_match, "no se encuentra la configuración del mapa de Visados")
visa_config = json.loads(visa_match.group(1))
require(visa_config["data"]["namibia"]["pasos"] == "5 jun",
        "Namibia debe conservar la corrección a junio")
require(visa_config["data"]["angola"]["pasos"] == "7 mar · 20 jun",
        "la segunda entrada de Angola debe estar en junio")
require(visa_config["data"]["tanzania"]["pasos"] == "16 abr" and
        visa_config["data"]["mozambique"]["pasos"] == "24 abr",
        "se han perdido las correcciones manuscritas del bucle oriental")
for page in country_pages:
    html = page.read_text(encoding="utf-8")
    require('<div class="callout-title">Calendario aproximado</div>' in html,
            f"falta el calendario común en {page.relative_to(ROOT)}")

print(f"UI OK: {len(carousel_pages)} países con fichas compactas; leyenda plegada; "
      f"visados y {len(country_pages)} calendarios coherentes; caché coherente")

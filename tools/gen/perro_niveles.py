# -*- coding: utf-8 -*-
"""Clasificación del perro por país, leída del propio dosier.

El dosier (docs/DOSSIER_PERRO.md) es la fuente única de la sección del perro, y
sus tablas del capítulo 2 ya traen una columna de dificultad con un semáforo.
Este módulo la lee en vez de duplicarla en otro sitio: así el mapa de la página
no puede contradecir a la tabla que tiene debajo.

Orden de preferencia cuando un país sale en más de una tabla: la entrada de ida
(2.1) manda, porque es la que decide si el perro puede empezar el viaje; si el
segundo cruce (2.2) es más duro, se anota aparte en vez de pisar el color.
"""
import re
from pathlib import Path

from actualiza_dosier import FILA

DOSIER = Path(__file__).parent / "docs" / "DOSSIER_PERRO.md"

# clave -> (color, etiqueta corta, descripción de la leyenda)
NIVELES = {
    "verde":   ("#2e7d32", "Trámite simple",
                "entrada documentada y sin permiso previo: basta el certificado sanitario."),
    "ambar":   ("#f9a825", "Con permiso o condiciones",
                "hace falta permiso previo, plazos cortos de certificado o requisitos añadidos."),
    "naranja": ("#ef6c00", "Mal documentado",
                "ninguna fuente oficial del país: solo webs comerciales, embajadas o silencio."),
    "rojo":    ("#c62828", "No viable o muy duro",
                "cuarentena, prohibición o país al que el perro directamente no va."),
}

_EMOJI = {"🟢": "verde", "🟡": "ambar", "🟠": "naranja", "🔴": "rojo"}
_SECCION = {"2.1": "ida", "2.2": "vuelta", "2.3": "alternativa", "2.4": "fuera"}
_ORDEN = ["verde", "ambar", "naranja", "rojo"]


def _limpio(s):
    """Texto plano a partir de una celda de la tabla: fuera enlaces, negritas y marcas."""
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = s.replace("**", "").replace("*", "")
    s = re.sub(r"\s*[⚠️❓✅❌]\s*", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _filas(md):
    """Devuelve (seccion, nombre, nivel, celdas) por cada fila de país del capítulo 2."""
    sec = None
    for ln in md.split("\n"):
        m = re.match(r"^## (2\.\d)", ln)
        if m:
            sec = m.group(1)
            continue
        if ln.startswith("## ") and not ln.startswith("## 2."):
            sec = None
        if not sec or not ln.startswith("|") or "**" not in ln:
            continue
        celdas = [c.strip() for c in ln.strip("|").split("|")]
        nombre = None
        for c in celdas[:2]:
            mm = re.match(r"^\*\*(.+?)\*\*$", c)
            if mm:
                nombre = mm.group(1)
                break
        nivel = idx = None
        for i, c in enumerate(celdas):
            if c in _EMOJI:
                nivel, idx = _EMOJI[c], i
                break
        # La celda que sigue al semáforo es la «nota clave» en las cuatro tablas.
        nota = celdas[idx + 1] if idx is not None and idx + 1 < len(celdas) else ""
        if nombre and nivel:
            yield sec, nombre, nivel, nota


def niveles(md=None):
    """slug -> dict(nivel, etapas, nombre, peor) leyendo el dosier."""
    md = md if md is not None else DOSIER.read_text(encoding="utf-8")
    out = {}
    for sec, nombre, nivel, nota in _filas(md):
        slug = FILA.get(nombre)
        if not slug:
            continue
        d = out.setdefault(slug, {"nombre": nombre, "etapas": {}, "nivel": None, "nota": ""})
        d["etapas"][_SECCION[sec]] = nivel
        # La ida manda; si el país no está en la ida, vale la primera tabla que lo cite.
        if sec == "2.1" or d["nivel"] is None:
            d["nivel"] = nivel
            d["nota"] = _limpio(nota)
    for d in out.values():
        d["peor"] = max(d["etapas"].values(), key=_ORDEN.index)
    return out

# -*- coding: utf-8 -*-
"""Calendario aproximado común a todas las fichas de país.

Fuente: ``Planificació Viatge.jpeg`` de la carpeta compartida ``04_Visats``.
Son fechas de entrada manuscritas, no reservas ni duraciones cerradas. La imagen
es la fuente para las fechas; la hoja de cálculo se usa para los visados.

Transcripción: 15-09-2026.
"""

SOURCE_FOLDER = "https://drive.google.com/drive/folders/19hD98XEZwjXq9Tj7hs4-zurDns7QD6Pz"
SOURCE_NAME = "Planificació Viatge.jpeg"

# (sentido, fecha de entrada aproximada). Se mantiene el orden escrito cuando
# un país aparece varias veces. No se calculan estancias que la imagen no da.
FECHAS_PAIS = {
    "marruecos": [("bajada", "12 ene 2027"), ("subida", "20 jul 2027")],
    "mauritania": [("bajada", "18 ene 2027"), ("subida", "15 jul 2027")],
    "senegal": [("bajada", "27 ene 2027"), ("subida", "3 jul 2027"),
                ("subida", "8 jul 2027")],
    "guinea": [("bajada", "2 feb 2027"), ("subida", "28 jun 2027")],
    "costa-de-marfil": [("bajada", "9 feb 2027"), ("subida", "23 jun 2027")],
    "ghana": [("bajada", "14 feb 2027"), ("subida", "19 jun 2027")],
    "togo": [("bajada", "17 feb 2027"), ("subida", "18 jun 2027")],
    "benin": [("bajada", "18 feb 2027"), ("subida", "16 jun 2027")],
    "nigeria": [("bajada", "19 feb 2027"), ("subida", "11 jun 2027")],
    "camerun": [("bajada", "24 feb 2027"), ("subida", "7 jun 2027")],
    "congo": [("bajada", "28 feb 2027"), ("subida", "2 jun 2027")],
    "rd-congo": [("bajada", "6 mar 2027"), ("subida", "1 jun 2027")],
    "angola": [("bajada", "7 mar 2027"), ("subida", "20 jun 2027")],
    "zambia": [("bucle", "17 mar 2027")],
    # Correcciones manuscritas: Tanzania fue sustituida por Malaui el 1/04 y
    # Mozambique por Tanzania el 16/04; Mozambique pasa al 24/04.
    "malaui": [("bucle", "1 abr 2027")],
    "tanzania": [("bucle", "16 abr 2027")],
    "mozambique": [("bucle", "24 abr 2027")],
    "zimbabue": [("bucle", "1 may 2027")],
    "namibia": [("bucle", "5 jun 2027")],
    "botsuana": [("bucle", "10 may 2027")],
    "sudafrica": [("bucle", "20 may 2027")],
    "gambia": [("subida", "7 jul 2027")],
}

NOTAS = {
    "sahara-occidental": "Sin fecha propia: tránsito incluido en las dos entradas de Marruecos.",
    "kenia": "Sin fecha en la planificación manuscrita; falta encajarlo en el bucle oriental.",
}


def resumen(slug, group=""):
    """Texto corto para el chip de cualquier ficha de país."""
    pasos = FECHAS_PAIS.get(slug, [])
    if pasos:
        return " · ".join(fecha.replace(" 2027", "") for _, fecha in pasos) + " (aprox.)"
    if slug in NOTAS:
        return NOTAS[slug]
    if group in ("bajada", "bucle", "subida"):
        return "Sin fecha en la planificación"
    if group in ("alternativa", "vuelo"):
        return "Opcional · sin fecha"
    return "No prevista"


def pasos_visado(slug):
    """Formato compacto para tablas y popups de visados."""
    pasos = FECHAS_PAIS.get(slug, [])
    return " · ".join(fecha.replace(" 2027", "") for _, fecha in pasos)


def detalle(slug):
    """Fechas con sentido de marcha para el contenido ampliado."""
    etiquetas = {"bajada": "bajada", "subida": "subida", "bucle": "bucle"}
    return " · ".join(f'{fecha} ({etiquetas.get(sentido, sentido)})'
                           for sentido, fecha in FECHAS_PAIS.get(slug, []))

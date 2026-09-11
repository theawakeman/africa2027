# -*- coding: utf-8 -*-
"""Gambia — ficha completa (9 sep 2026): alternativa/opcional, solo si obliga la logística."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Isla Kunta Kinteh (antigua James Island)", cat="Cultura", prio="Media", dog="no aplicable (isla, acceso en barco)", time="medio día (excursión)",
         lat=13.5772, lon=-16.5719,
         desc="Isla fluvial en el río Gambia, antiguo fuerte y factoría negrera británica, Patrimonio de la Humanidad por su papel central en la memoria de la trata atlántica de esclavos; se visita en barco desde Juffureh.",
         credit="Leonora (Ellie) Enking · CC BY-SA 2.0", source=W + "James%20Island%20near%20Juffureh%20(4129325186).jpg?width=900"),
    dict(n=2, name="Kotu Beach / Serrekunda (costa turística)", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=13.4526, lon=-16.7069,
         desc="Franja costera atlántica de la Gambia turística, con buena oferta hotelera y observación de aves; Serrekunda, la mayor ciudad del país, concentra los mercados y servicios más completos.",
         credit="Mark Hodson Photos · CC BY 2.0", source=W + "Kotu%20Beach%2C%20The%20Gambia%20(16197149546).jpg?width=900"),
]

_CAT_COLOR = {"cultura": "morado", "naturaleza": "verde"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Karang/Amdalai (con Senegal, oeste)", "Frontera", 13.2167, -16.7000,
     "Cruce más usado desde la Petite Côte senegalesa; protocolo binacional específico para no perder el corredor base del proyecto por Senegal."),
    ("Frontera · Keur Ayib/Farafenni (con Senegal, este)", "Frontera", 13.5667, -15.6000,
     "Alternativa oriental si el desvío a Gambia se hace desde el interior de Senegal en lugar de la costa."),
    ("Embajada de España en Banjul", "Consular", 13.4549, -16.5790,
     "Oficina de la embajada de España en Banjul (dependiente de Dakar para trámites mayores); confirmar dirección y teléfono exactos 30-60 días antes — información pendiente de verificación directa."),
    ("Royal Victoria Teaching Hospital, Banjul", "Hospital", 13.4540, -16.5776,
     "Principal hospital de referencia del país; capacidad limitada — seguro con evacuación médica real recomendable."),
    ("Combustible · Banjul / Serrekunda", "Combustible", 13.4549, -16.5790,
     "Estaciones formales en la conurbación de Banjul-Serrekunda-Kotu; sin gap relevante dado lo compacto del país."),
    ("Agua potable y de uso general · Serrekunda / Kotu", "Agua potable", 13.4526, -16.7069,
     "Agua embotellada sin problema en la zona turística; hoteles de Kotu permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa recomendada",
                  "Gambia no tiene una normativa de drones tan desarrollada como sus vecinos, lo que en la práctica genera incertidumbre: recomendable solicitar información y, si procede, autorización a la autoridad de aviación civil (Gambia Civil Aviation Authority) antes de volar, y evitar cualquier vuelo cerca del aeropuerto de Banjul o de instalaciones oficiales.")

STARLINK_CALLOUT = ("warn", "Estado sin confirmar a mediados de 2026",
                     "No hay confirmación clara del estado de licencia de Starlink en Gambia a la fecha de esta revisión. Tratar como no garantizado y llevar SIM local (Africell, Qcell) como conectividad principal.")

DOG_MATRIX = [
    ("Isla Kunta Kinteh", "no aplicable", "Visita en barco de corta duración; no aplica llevar mascota en la excursión."),
    ("Banjul, Serrekunda, Kotu", "permitido con condiciones", "Correa y sombra; calor húmedo costero todo el año."),
]

SOURCES = [
    ("thingstodoingambia.com · requisitos de entrada 2026", "https://thingstodoingambia.com/entry-requirements/"),
    ("Lost In A 4x4 · guía del cruce Senegal-Gambia (Karang/Amdalai)", "https://lostina4x4.com/senegal-to-the-gambia-border-crossing-guide-overland-step-by-step/"),
    ("Feathery Travels · cruce fronterizo Gambia/Senegal (Amdallai-Karang)", "https://www.featherytravels.com/gambiasenegalborderkarang/"),
    ("UNESCO · Isla Kunta Kinteh y sitios relacionados, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/761/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
]

CORRIDOR = [(13.2167, -16.7000), (13.4549, -16.5790), (13.4526, -16.7069), (13.5772, -16.5719)]

HISTORIA_RESUMEN = ("Gambia es una franja de apenas unos kilómetros a cada lado de su río, enclavada dentro de Senegal, y debe su forma a la rivalidad colonial anglo-francesa; su isla de Kunta Kinteh (la antigua James Island) "
                     "fue uno de los puntos de embarque de la trata atlántica de esclavos y hoy es Patrimonio de la Humanidad, mientras el país vive del turismo costero y de una recuperación democrática tras años de dictadura.")

HISTORIA_SECCIONES = [
    ("El río como frontera y ruta de esclavos",
     "El río Gambia fue durante siglos una vía de comercio hacia el interior africano, y desde el siglo XVII se convirtió en un punto clave de la trata atlántica de esclavos: la isla hoy llamada Kunta Kinteh (entonces James Island) "
     "albergó un fuerte británico desde el que se embarcaba a personas esclavizadas hacia América, un episodio que la novela y serie «Raíces» de Alex Haley popularizó mundialmente al situar en Juffureh el origen de su protagonista."),
    ("Colonia británica dentro de Senegal francés",
     "La forma alargada y estrecha de Gambia —apenas la anchura navegable de su río— es resultado directo de un acuerdo anglo-francés de 1889 que fijó la frontera a pocos kilómetros de cada orilla, dejando un enclave británico completamente rodeado por el Senegal francés. "
     "Gambia se independizó del Reino Unido en 1965 y se convirtió en república en 1970."),
    ("De la dictadura de Jammeh a la transición democrática",
     "Tras un golpe de Estado en 1994, Yahya Jammeh gobernó el país durante 22 años con un régimen represivo, hasta que perdió las elecciones de 2016 y, tras semanas de resistencia a abandonar el poder, se exilió en enero de 2017 gracias a la presión de la CEDEAO. "
     "Desde entonces Gambia vive un proceso de transición democrática con comisión de la verdad sobre los abusos de la era Jammeh."),
    ("Situación actual",
     "Gambia es hoy un país estable, cuya economía depende sobre todo del turismo costero (Kotu, Kololi) y de la agricultura; para este proyecto queda fuera del corredor base de Senegal y solo se contempla como desvío opcional si la logística del viaje lo justifica."),
]

HISTORIA_FUENTES = [
    ("BBC News · The Gambia country profile", "https://www.bbc.com/news/world-africa-13376517"),
    ("UNESCO · Isla Kunta Kinteh y sitios relacionados", "https://whc.unesco.org/en/list/761/"),
    ("Encyclopaedia Britannica · The Gambia, History", "https://www.britannica.com/place/The-Gambia/History"),
]

SPEC = dict(
    slug="gambia", name="Gambia", revision="9 sep 2026",
    sub="Alternativa/opcional · fuera del corredor base de Senegal",
    chips=[
        ("ROL EN LA RUTA", "opcional — solo si obliga la logística"),
        ("ENTRADA/SALIDA", "Karang/Amdalai (oeste) o Keur Ayib/Farafenni (este)"),
        ("SEGURIDAD", "estable"),
        ("VEHÍCULO", "permiso temporal en frontera"),
    ],
    center=[13.45, -16.2], zoom=8,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, si finalmente se incluye este desvío.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    facts=[
        ("Rol en la ruta", "Alternativa/opcional: Gambia queda fuera del corredor base de Senegal y solo se visita si lo justifica la logística."),
        ("Entrada/salida", "Karang/Amdalai (oeste, desde la Petite Côte) o Keur Ayib/Farafenni (este, desde el interior de Senegal)."),
        ("Seguridad", "País estable; sin alertas relevantes para este proyecto."),
        ("Vehículo", "Permiso temporal en frontera; verificar si se exige o recomienda CPD para el desvío puntual."),
    ],
    alerts=[
        "Este desvío añade dos cruces fronterizos extra (entrada y salida) al corredor base de Senegal: valorar el tiempo y trámite adicional antes de incluirlo.",
        "Confirmar 30-60 días antes los detalles exactos del CPD/permiso temporal para una entrada y salida tan cortas.",
    ],
    ruta_intro="Desvío corto desde el corredor base de Senegal: entrada por un lado del río, visita a Kunta Kinteh y la costa turística, y salida por el otro cruce fronterizo para reincorporarse a la ruta principal.",
    route_rows=[
        ("Entrada", "Karang/Amdalai → Banjul/Serrekunda", "Base turística y de servicios"),
        ("Cultura", "Serrekunda → Isla Kunta Kinteh (Juffureh)", "Excursión en barco de medio día"),
        ("Salida", "Banjul → Keur Ayib/Farafenni", "Reincorporación al corredor base de Senegal"),
    ],
    offroad=[],
    acampada=[
        "Kotu y Kololi: hoteles y campings de la zona turística, con buena oferta de aparcamiento.",
    ],
    visado=[
        "Exención de visado para españoles — verificar vigencia y duración exacta 30-60 días antes.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica.",
    ],
    fronteras_rows=[
        ("Entrada/salida (oeste)", "Karang/Amdalai (Senegal)", "Cruce más usado desde la Petite Côte senegalesa."),
        ("Entrada/salida (este)", "Keur Ayib/Farafenni (Senegal)", "Alternativa desde el interior de Senegal."),
    ],
    vehiculos=[
        "Permiso temporal en frontera para el vehículo; confirmar si se exige o recomienda CPD para esta entrada y salida cortas.",
        "Seguro de terceros (Carte Brune CEDEAO) válido en Gambia como miembro de la CEDEAO.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Consultar con la Gambia Civil Aviation Authority antes de volar; normativa menos desarrollada que en países vecinos.",
        "No volar cerca del aeropuerto de Banjul ni de instalaciones oficiales.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado sin confirmar a mediados de 2026: tratar como no garantizado.",
        "SIM local (Africell, Qcell) como conectividad principal.",
    ],
    perro_intro=[
        "Certificado veterinario internacional y vacuna antirrábica en vigor, exigibles en frontera.",
        "Sin restricciones específicas relevantes para el itinerario corto previsto en este desvío.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en todo el país: profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Royal Victoria Teaching Hospital (Banjul) como referencia sanitaria del país, con capacidad limitada.",
    ],
    seguridad_intro="Gambia es un país pequeño y estable; el principal factor a valorar es si el desvío compensa el tiempo y los trámites fronterizos adicionales frente al corredor base de Senegal.",
    seguridad=[
        "Precaución normal de viaje; sin alertas de seguridad activas relevantes.",
        "Aparcamiento vigilado en la zona turística de Kotu/Kololi por prudencia estándar.",
    ],
    agua=[
        "Serrekunda y Kotu: agua embotellada sin problema en la zona turística.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): hoteles de Kotu permiten llenar el depósito con manguera.",
    ],
    combustible=[
        "Sin riesgo de gap relevante dado lo compacto del país: la conurbación Banjul-Serrekunda-Kotu concentra estaciones formales a poca distancia entre sí.",
    ],
    pendientes=[
        ("Decisión de incluir el desvío", "Confirmar si compensa frente al corredor base de Senegal antes de cerrar el itinerario"),
        ("Embajada de Banjul", "Verificar dirección y teléfono exactos — información pendiente de confirmación directa"),
        ("Vehículo", "Confirmar si se exige CPD para esta entrada y salida cortas"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Gambia es un desvío opcional: confirmar si se incluye antes de revalidar el resto de trámites.",
    emergency="Sin línea de emergencia consular propia confirmada en Banjul — en caso de necesidad, contactar con la Embajada de España en Dakar (Senegal) como referencia regional más cercana.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

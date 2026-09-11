# -*- coding: utf-8 -*-
"""Esuatini — ficha completa (9 sep 2026): alternativa/opcional en el enlace Sudáfrica→Mozambique."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Santuario de Vida Silvestre de Mlilwane", cat="Naturaleza", prio="Alta", dog="prohibido", time="1 noche",
         lat=-26.4667, lon=31.1667,
         desc="Primera reserva protegida del país, sin grandes depredadores, lo que permite paseos y rutas en bicicleta entre cebras, antílopes e hipopótamos; una introducción cómoda a la fauna del sur de África.",
         credit="Bernard Gagnon · CC BY-SA 4.0", source=W + "Plains%20zebra%20in%20Mlilwane%20Wildlife%20Sanctuary%2001.jpg?width=900"),
    dict(n=2, name="Reserva Natural de Malolotja", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-26.1500, lon=31.1000,
         desc="Montañas del noroeste del país con senderos de trekking, la segunda cascada más alta de África austral (Malolotja Falls) y buena observación de aves; alternativa de naturaleza más agreste que Mlilwane.",
         credit="Bernard DUPONT · CC BY-SA 2.0", source=W + "Malolotja%20Scenery%20(31722500693).jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Ngwenya/Oshoek (con Sudáfrica)", "Frontera", -26.1667, 31.0000,
     "Cruce principal y más transitado desde Sudáfrica (Mpumalanga); asfaltado y bien equipado."),
    ("Frontera · Lomahasha/Namaacha (con Mozambique)", "Frontera", -25.9500, 31.9333,
     "Cruce hacia Mozambique en el extremo noreste del país; permite enlazar directamente Esuatini con el corredor de Maputo."),
    ("Embajada de España en Maputo (competente para Esuatini)", "Consular", -25.9700, 32.5850,
     "Rua Damião de Góis, 347, Maputo (Mozambique). Tel. (+258) 21 49 20 25/27/30 · Emergencia consular 24h: (+258) 84 32 82 900. Gestionar trámites mayores a través de esta embajada."),
    ("Mbabane Government Hospital", "Hospital", -26.3167, 31.1333,
     "Principal hospital de referencia del país; para necesidades serias, evacuación hacia Sudáfrica es la opción más fiable."),
    ("Combustible · Mbabane / Ezulwini / Manzini", "Combustible", -26.3054, 31.1367,
     "Estaciones formales en el eje urbano central del país; sin gap relevante dado el tamaño compacto de Esuatini."),
    ("Agua potable y de uso general · Ezulwini", "Agua potable", -26.4500, 31.2000,
     "Agua embotellada sin problema en la zona turística del valle de Ezulwini; hoteles y lodges permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa recomendada",
                  "Esuatini exige en la práctica coordinación previa con la autoridad de aviación civil (Eswatini Civil Aviation Authority) para el uso de drones; recomendable solicitar información con antelación y evitar volar cerca de residencias reales o instalaciones oficiales, dado que el país es una monarquía absoluta con alta sensibilidad hacia estos asuntos.")

STARLINK_CALLOUT = ("warn", "Estado sin confirmar a mediados de 2026",
                     "No hay confirmación clara del estado de licencia de Starlink en Esuatini a la fecha de esta revisión. Tratar como no garantizado y llevar SIM local (MTN Eswatini, Eswatini Mobile) como conectividad principal.")

DOG_MATRIX = [
    ("Mlilwane", "prohibido", "No se permite el acceso de mascotas al santuario; dejar en el vehículo con sombra o con el alojamiento."),
    ("Malolotja, Mbabane, Ezulwini", "permitido con condiciones", "Correa y sombra; clima templado de altiplano en Mbabane, más cálido en el valle de Ezulwini."),
]

SOURCES = [
    ("thingstodoineswatini.com · requisitos de entrada 2026", "https://thingstodoineswatini.com/entry-requirements/"),
    ("Embajada de España en Maputo · también embajada en Esuatini", "https://www.exteriores.gob.es/Embajadas/maputo/es/Embajada/Paginas/Tambien-somos-tu-embajada-en.aspx"),
    ("Drive South Africa · guía de cruces fronterizos con Sudáfrica", "https://www.drivesouthafrica.com/blog/south-africa-border-crossing-guide/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
]

CORRIDOR = [(-26.1667, 31.0000), (-26.3054, 31.1367), (-26.4667, 31.1667), (-26.1500, 31.1000), (-25.9500, 31.9333)]

HISTORIA_RESUMEN = ("Esuatini es la última monarquía absoluta de África, fundada por el pueblo swazi bajo el rey Sobhuza I en el siglo XIX como refugio frente a la expansión zulú y bóer; protectorado británico hasta 1968, "
                     "mantiene hoy un sistema de doble gobierno (rey y parlamento) muy cuestionado por su falta de partidos políticos legales, mientras vive del turismo y de su estrecha integración económica con Sudáfrica.")

HISTORIA_SECCIONES = [
    ("El reino swazi entre zulúes y bóers",
     "En el siglo XIX, el pueblo swazi (ngwane) consolidó un reino en las montañas del actual Esuatini bajo el liderazgo del rey Sobhuza I, buscando protección frente a la expansión militar del reino zulú de Shaka y, más tarde, frente a la presión de los colonos bóers que avanzaban desde el Transvaal."),
    ("Protectorado británico",
     "Ante las presiones tanto bóers como británicas por el control del territorio, Suazilandia (nombre colonial del país) se convirtió en protectorado británico en 1903, tras la guerra anglo-bóer, quedando administrada por separado de Sudáfrica —de forma similar a Lesoto y Botsuana— "
     "lo que la mantuvo fuera del sistema del apartheid sudafricano."),
    ("Independencia y monarquía absoluta",
     "El país alcanzó la independencia en 1968 como monarquía constitucional bajo el rey Sobhuza II, pero en 1973 el propio rey suspendió la constitución y prohibió los partidos políticos, instaurando un sistema de monarquía absoluta (Tinkhundla) que se ha mantenido, con reformas parciales, hasta hoy bajo el rey Mswati III."),
    ("Situación actual: cambio de nombre y protestas por la democracia",
     "En 2018 el rey Mswati III cambió el nombre oficial del país de Suazilandia a Esuatini (\"tierra de los swazis\"), y desde 2021 el país ha vivido protestas prodemocráticas recurrentes, reprimidas con dureza por las fuerzas de seguridad. "
     "Pese a esta tensión política, el turismo (Mlilwane, Malolotja, el valle de Ezulwini) y la fuerte integración económica con Sudáfrica mantienen a Esuatini como un desvío manejable y de corta duración en el enlace hacia Mozambique."),
]

HISTORIA_FUENTES = [
    ("BBC News · Eswatini country profile", "https://www.bbc.com/news/world-africa-14650437"),
    ("Encyclopaedia Britannica · Eswatini, History", "https://www.britannica.com/place/Eswatini/History"),
]

SPEC = dict(
    slug="esuatini", name="Esuatini", revision="9 sep 2026",
    sub="Alternativa/opcional · enlace Sudáfrica→Mozambique",
    chips=[
        ("ROL EN LA RUTA", "opcional — enlace Sudáfrica→Mozambique"),
        ("ENTRADA", "Ngwenya/Oshoek (desde Sudáfrica)"),
        ("SALIDA", "Lomahasha/Namaacha (hacia Mozambique)"),
        ("SEGURIDAD", "estable"),
    ],
    center=[-26.3, 31.3], zoom=8,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, si finalmente se incluye este desvío.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    facts=[
        ("Rol en la ruta", "Alternativa/opcional en el enlace Sudáfrica→Mozambique, atravesando el país de suroeste a noreste."),
        ("Entrada", "Ngwenya/Oshoek desde Sudáfrica (Mpumalanga)."),
        ("Salida", "Lomahasha/Namaacha hacia Mozambique, enlazando directamente con el corredor de Maputo."),
        ("Seguridad", "País estable en el eje turístico; protestas prodemocráticas ocasionales en centros urbanos — evitar concentraciones."),
    ],
    alerts=[
        "Protestas prodemocráticas: pueden producirse de forma puntual en Mbabane u otros centros urbanos; evitar cualquier concentración y seguir indicaciones locales.",
        "Este desvío atraviesa el país de extremo a extremo (Ngwenya-Lomahasha): confirmar que el tiempo disponible permite las dos noches recomendadas en Mlilwane y Malolotja.",
    ],
    ruta_intro="Travesía de Esuatini de suroeste a noreste: entrada desde Sudáfrica, dos paradas de naturaleza (Mlilwane, Malolotja) y salida directa hacia el corredor de Maputo en Mozambique.",
    route_rows=[
        ("Entrada y fauna", "Ngwenya/Oshoek → Mlilwane", "Primera reserva del país; paseos entre fauna sin grandes depredadores"),
        ("Montaña", "Mlilwane → Malolotja", "Trekking y cascadas en el noroeste"),
        ("Salida", "Malolotja → Lomahasha/Namaacha", "Enlace directo con el corredor de Maputo (Mozambique)"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: los accesos a Mlilwane y Malolotja son pistas de tierra en buen estado, transitables sin dificultad técnica.",
    ],
    acampada=[
        "Mlilwane: campamento propio de la reserva, con opción de cabañas tradicionales o zona de acampada.",
        "Malolotja: campamento de la reserva, más rústico y orientado a senderistas.",
    ],
    visado=[
        "Exención de visado para españoles — verificar vigencia exacta 30-60 días antes.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica.",
    ],
    fronteras_rows=[
        ("Entrada", "Ngwenya/Oshoek (Sudáfrica)", "Cruce principal y más transitado desde Mpumalanga."),
        ("Salida", "Lomahasha/Namaacha (Mozambique)", "Enlace directo con el corredor de Maputo."),
    ],
    vehiculos=[
        "Permiso temporal sencillo en frontera para el vehículo.",
        "Seguro de terceros SADC válido en Esuatini como miembro de la región.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Consultar con la Eswatini Civil Aviation Authority antes de volar.",
        "No volar cerca de residencias reales ni instalaciones oficiales, dada la alta sensibilidad de la monarquía hacia estos asuntos.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado sin confirmar a mediados de 2026: tratar como no garantizado.",
        "SIM local (MTN Eswatini, Eswatini Mobile) como conectividad principal.",
    ],
    perro_intro=[
        "Certificado veterinario internacional y vacuna antirrábica en vigor, exigibles en frontera.",
        "Perro prohibido en Mlilwane; dejar con el alojamiento o en el vehículo con sombra durante esa visita.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en zonas bajas del este del país (hacia la frontera con Mozambique); menor riesgo en el altiplano central.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Mbabane Government Hospital como referencia local; para casos serios, evacuación hacia Sudáfrica es la opción real.",
    ],
    seguridad_intro="Esuatini es en general un tramo tranquilo del enlace hacia Mozambique; la única precaución específica es evitar protestas prodemocráticas ocasionales en centros urbanos.",
    seguridad=[
        "Evitar concentraciones o manifestaciones en Mbabane u otros centros urbanos.",
        "Precaución normal de viaje en el resto del itinerario (Mlilwane, Malolotja).",
    ],
    agua=[
        "Ezulwini: agua embotellada sin problema en la zona turística.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): hoteles y lodges de Ezulwini y los campamentos de Mlilwane/Malolotja permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap relevante: el eje central (Mbabane-Ezulwini-Manzini) concentra estaciones formales a poca distancia entre sí, y el país es pequeño en su totalidad.",
    ],
    pendientes=[
        ("Decisión de incluir el desvío", "Confirmar si compensa frente a un enlace directo Sudáfrica-Mozambique"),
        ("Situación política", "Revisar 30-60 días antes si hay protestas programadas o alertas específicas"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Esuatini es un desvío opcional: confirmar si se incluye antes de revalidar el resto de trámites.",
    emergency="Emergencia consular española (vía Embajada en Maputo, Mozambique, 24h): (+258) 84 32 82 900.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

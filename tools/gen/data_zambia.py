# -*- coding: utf-8 -*-
"""Zambia — ficha completa (9 sep 2026): alternativa Victoria Falls/South Luangwa."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Cataratas Victoria (lado zambiano, Livingstone)", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=-17.8419, lon=25.8543,
         desc="La vista zambiana de las cataratas más célebres de África, con acceso desde la ciudad de Livingstone; menos concurrida que el lado zimbabuense y con actividades adicionales como rafting en el cañón del Zambeze y el histórico puente de Victoria Falls.",
         credit="Matti Blume · CC BY-SA 4.0", source=W + "Mosi-oa-Tunya%2C%20Livingstone%20%2820260519-P1075699%29.jpg?width=900"),
    dict(n=2, name="Parque Nacional South Luangwa (Mfuwe)", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=-13.0833, lon=31.9500,
         desc="Considerado la cuna del safari a pie, con una de las mayores densidades de leopardos de África y el valle del río Luangwa como escenario; Mfuwe es la puerta logística con aeródromo y campamentos de referencia.",
         credit="Timothy A. Gonsalves · CC BY-SA 4.0", source=W + "Giraffe%20Standing%20Lupande%20Zambia%20Jul23%20A7C%2006176.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Kazungula (con Botsuana/Zimbabue)", "Frontera", -17.7833, 25.2667,
     "Punto cuádruple con puente nuevo sobre el Zambeze; cruce ágil, base para enlazar con Botsuana o continuar hacia Zimbabue por Victoria Falls."),
    ("Frontera · Chirundu (con Zimbabue)", "Frontera", -16.0333, 28.8500,
     "Uno de los pasos más transitados de la región (corredor Norte-Sur); puesto fronterizo de ventanilla única (one-stop border post), relativamente ágil para lo que es la media regional."),
    ("Embajada de España en Harare (competente para Zambia)", "Consular", -17.8216, 31.0492,
     "16 Phillips Ave., Belgravia, Harare (Zimbabue). Tel. +263 (0)242 250740/1; emergencias +263 (0)772 436 620. Gestionar trámites mayores a través de esta embajada."),
    ("University Teaching Hospital, Lusaka", "Hospital", -15.4067, 28.3050,
     "Principal hospital de referencia del país en la capital; para necesidades serias, evacuación hacia Sudáfrica es la práctica habitual en la región."),
    ("Combustible · Livingstone / Lusaka / Mfuwe", "Combustible", -17.8419, 25.8543,
     "Estaciones formales en las tres localidades; repostar a fondo en cada una, especialmente antes del tramo hacia South Luangwa, con menos oferta fiable en el camino."),
    ("Agua potable y de uso general · Livingstone y Lusaka", "Agua potable", -17.8419, 25.8543,
     "Agua embotellada sin problema en ambas ciudades; lodges y campings permiten llenar el depósito de uso general con manguera, confirmar potabilidad en zonas rurales del valle del Luangwa."),
]

DRONE_CALLOUT = ("danger", "Prohibido en la práctica en parques nacionales y muy restringido en general",
                  "Zambia exige registro y permiso previo de la Zambia Civil Aviation Authority para cualquier uso de drones, y su uso dentro de parques nacionales (incluidos Victoria Falls/Mosi-oa-Tunya y South Luangwa) está prohibido salvo autorización expresa y muy excepcional. Norma del proyecto: no volar el dron en ningún parque o reserva sin autorización expresa ya concedida.")

STARLINK_CALLOUT = ("ok", "Disponible y operativo en 2026",
                     "Starlink está activo comercialmente en Zambia desde 2023, con cobertura razonable incluso en zonas de safari como South Luangwa; kit y suscripción configurables antes de entrar al país.")

DOG_MATRIX = [
    ("Victoria Falls/Mosi-oa-Tunya, South Luangwa", "prohibido", "No se permite el acceso de mascotas a los parques nacionales; dejar en Livingstone o Mfuwe con cuidador o en el alojamiento."),
    ("Livingstone, Lusaka", "permitido con condiciones", "Correa y sombra; clima cálido, especialmente en la estación seca-cálida (septiembre-noviembre)."),
]

SOURCES = [
    ("Gobierno de Zambia · Zambia Immigration Department, requisitos de visado", "https://www.zambiaimmigration.gov.zm/"),
    ("Zambia Wildlife Authority (DNPW) · normativa de parques nacionales", "https://www.dnpw.gov.zm/"),
    ("Zambia Civil Aviation Authority · normativa de drones", "https://www.zcaa.co.zm/"),
    ("KAZA Univisa · información oficial de la visa conjunta Zambia-Zimbabue", "https://www.kazatransfrontier.org/"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
]

CORRIDOR = [(-17.7833, 25.2667), (-17.8419, 25.8543), (-15.4067, 28.3050), (-13.0833, 31.9500), (-16.0333, 28.8500)]

HISTORIA_RESUMEN = ("Zambia, antigua Rodesia del Norte, alcanzó la independencia en 1964 bajo el liderazgo de Kenneth Kaunda sin el conflicto armado que marcó a su vecina Rodesia del Sur (actual Zimbabue), y ha mantenido desde entonces "
                     "una trayectoria política relativamente estable, sostenida sobre todo por el cobre y, cada vez más, por el turismo de naturaleza en torno a las Cataratas Victoria y los grandes parques del valle del Luangwa y el Zambeze.")

HISTORIA_SECCIONES = [
    ("Reinos e imperios previos a la colonización",
     "El territorio de la actual Zambia estuvo habitado por pueblos bantúes organizados en reinos como el Lozi (en la llanura de Barotseland, sobre el alto Zambeze) y el Bemba (en el noreste), con sistemas políticos centralizados y redes comerciales "
     "que conectaban el interior con la costa índica mucho antes de la llegada europea."),
    ("Rodesia del Norte y el peso del cobre",
     "El territorio fue administrado por la British South Africa Company de Cecil Rhodes desde finales del siglo XIX y pasó a ser colonia británica directa como Rodesia del Norte en 1924. El descubrimiento de enormes yacimientos de cobre en el Copperbelt "
     "convirtió a la colonia en un motor económico regional, con mano de obra africana en condiciones duras y una minoría blanca que dominaba la explotación minera y la vida política."),
    ("Independencia sin guerra, bajo Kenneth Kaunda",
     "A diferencia de Rodesia del Sur, Rodesia del Norte alcanzó la independencia por vía pacífica en 1964 como Zambia, bajo el liderazgo de Kenneth Kaunda, quien gobernaría durante 27 años con un proyecto de «humanismo zambiano» y un papel activo "
     "como refugio y base de apoyo para movimientos de liberación de países vecinos (incluida la lucha contra el apartheid y contra el régimen de Ian Smith en Rodesia)."),
    ("Situación actual: transición democrática y economía del cobre y el turismo",
     "Zambia transitó al multipartidismo en 1991 y ha vivido desde entonces alternancias pacíficas en el poder, incluida la derrota electoral del presidente saliente en 2021, un hecho valorado como signo de salud democrática en la región. "
     "La economía sigue muy dependiente del cobre, con episodios de deuda y renegociación en los últimos años, mientras el turismo de naturaleza en torno a Victoria Falls, South Luangwa y el bajo Zambeze crece como fuente complementaria de ingresos."),
]

HISTORIA_FUENTES = [
    ("BBC News · Zambia country profile", "https://www.bbc.com/news/world-africa-14113019"),
    ("Encyclopaedia Britannica · Zambia, History", "https://www.britannica.com/place/Zambia/History"),
    ("UNESCO · Mosi-oa-Tunya / Victoria Falls, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/509/"),
]

SPEC = dict(
    slug="zambia", name="Zambia", revision="9 sep 2026",
    sub="Alternativa · Victoria Falls/South Luangwa",
    chips=[
        ("ROL EN LA RUTA", "opcional — Cataratas Victoria y South Luangwa"),
        ("ENTRADA/SALIDA", "Kazungula o Chirundu (Zimbabue)"),
        ("SEGURIDAD", "estable"),
        ("COMUNICACIONES", "Starlink activo (ok)"),
    ],
    center=[-15.5, 28.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, si finalmente se incluye este desvío.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    facts=[
        ("Rol en la ruta", "Alternativa de naturaleza de alto nivel (Cataratas Victoria, South Luangwa) si el itinerario lo permite."),
        ("Entrada/salida", "Kazungula desde Botsuana/Zimbabue, o Chirundu desde Zimbabue."),
        ("Seguridad", "País estable, con alternancias democráticas pacíficas; sin alertas relevantes para este proyecto."),
        ("Perro", "Prohibido en Victoria Falls/Mosi-oa-Tunya y South Luangwa; planificar cuidado en Livingstone o Mfuwe."),
    ],
    alerts=[
        "Perro prohibido en los parques nacionales del itinerario: prever cuidador o alojamiento con guardería en Livingstone o Mfuwe.",
        "KAZA Univisa (50 USD, 30 días, uso múltiple dentro de ese periodo) cubre Zambia y Zimbabue conjuntamente y permite excursiones de un día a Botsuana vía Kazungula: valorar frente al visado individual según el itinerario final.",
    ],
    ruta_intro="Entrada por Kazungula o Chirundu, visita a Livingstone y las Cataratas Victoria, travesía hacia Lusaka y desvío al valle del Luangwa (South Luangwa) antes de retomar el eje principal o cruzar a Zimbabue/Malaui.",
    route_rows=[
        ("Entrada y cataratas", "Kazungula/Chirundu → Livingstone", "Cataratas Victoria, rafting en el Zambeze"),
        ("Capital", "Livingstone → Lusaka", "Escala logística, repostaje y gestiones"),
        ("Safari a pie", "Lusaka → South Luangwa (Mfuwe)", "Cuna del safari a pie; alta densidad de leopardos"),
        ("Salida", "South Luangwa → Chipata → Malaui", "Enlace hacia el eje principal por Malaui"),
    ],
    offroad=[
        "Pistas de tierra en el acceso final a algunos campamentos de South Luangwa (recomendable 4x4 en temporada de lluvias, nov-abr); el eje Livingstone-Lusaka-Chipata es carretera asfaltada.",
    ],
    acampada=[
        "Livingstone: amplia oferta de campings orientados a overlanders junto al Zambeze.",
        "Mfuwe: campamentos y lodges de South Luangwa con parcelas para vehículo propio en varios de ellos.",
    ],
    visado=[
        "Visado de turista disponible a la llegada para españoles, o KAZA Univisa (50 USD) si se combina con Zimbabue.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica.",
    ],
    fronteras_rows=[
        ("Entrada/salida (sur)", "Kazungula (Botsuana/Zimbabue)", "Punto cuádruple; puente nuevo sobre el Zambeze."),
        ("Entrada/salida (sureste)", "Chirundu (Zimbabue)", "Puesto de ventanilla única, corredor Norte-Sur, tráfico pesado de camiones."),
    ],
    vehiculos=[
        "Permiso temporal en frontera para el vehículo; confirmar despacho aduanero según el punto de entrada.",
        "Seguro de terceros COMESA/SADC válido en Zambia como miembro de ambas regiones.",
        "Peajes de carretera (road toll) de pago obligatorio en varios tramos del eje principal.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No volar en ningún caso dentro de Mosi-oa-Tunya/Victoria Falls o South Luangwa sin autorización expresa ya concedida.",
        "Registrar el dron ante la Zambia Civil Aviation Authority antes de cualquier uso fuera de parques.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo desde 2023, con cobertura razonable incluso en zonas de safari como South Luangwa.",
        "SIM local (MTN, Airtel Zambia) como respaldo en zonas más remotas.",
    ],
    perro_intro=[
        "Certificado veterinario internacional y permiso de importación previo, exigibles en frontera.",
        "Perro prohibido en Mosi-oa-Tunya/Victoria Falls y South Luangwa; prever cuidador o alojamiento con guardería en Livingstone o Mfuwe.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en todo el país, incluido el valle del Luangwa: profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "University Teaching Hospital (Lusaka) como referencia nacional; evacuación hacia Sudáfrica para casos serios.",
    ],
    seguridad_intro="Zambia es uno de los países más estables políticamente de la región, con alternancia democrática pacífica; la principal atención en este tramo debe ir a la fauna salvaje y a la carretera, no a la seguridad ciudadana.",
    seguridad=[
        "Respetar siempre las distancias de seguridad con la fauna en South Luangwa y las indicaciones del guía o ranger en los safaris a pie.",
        "Precaución normal de viaje en Livingstone y Lusaka.",
        "Tráfico pesado de camiones en el corredor Chirundu-Lusaka: extremar precaución, especialmente de noche.",
    ],
    agua=[
        "Livingstone y Lusaka: agua embotellada sin problema.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): lodges y campings de ambas localidades permiten llenar el depósito con manguera; confirmar potabilidad en zonas rurales del valle del Luangwa.",
    ],
    combustible=[
        "Livingstone, Lusaka y Mfuwe concentran la oferta fiable; repostar a fondo en cada una, con menor oferta garantizada en el tramo hacia South Luangwa.",
        "Sin gap relevante de 500 km en el eje asfaltado Livingstone-Lusaka-Chipata.",
    ],
    pendientes=[
        ("KAZA Univisa", "Confirmar si conviene frente al visado individual, según si se visita también Zimbabue"),
        ("Perro", "Confirmar guardería o cuidador en Livingstone/Mfuwe durante las visitas a los parques"),
        ("Dron", "Registrar ante la Zambia Civil Aviation Authority si se quiere volar fuera de los parques"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Zambia es un desvío opcional: confirmar si se incluye antes de revalidar el resto de trámites.",
    emergency="Sin representación española propia en Zambia — gestionar emergencias a través de la Embajada de España en Harare (Zimbabue), competente para el país: +263 (0)242 250740/1; emergencias +263 (0)772 436 620.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

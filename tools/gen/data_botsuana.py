# -*- coding: utf-8 -*-
"""Botsuana — ficha completa (9 sep 2026): alternativa Kalahari/Chobe."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Parque Nacional de Chobe", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=-17.8167, lon=25.1500,
         desc="Una de las mayores concentraciones de elefantes de África a orillas del río Chobe; safaris fluviales en barco además de en vehículo, con Kasane como base logística junto al punto cuádruple de Kazungula.",
         credit="Bernard Gagnon · CC BY-SA 4.0", source=W + "Elephants%20in%20Chobe%20National%20Park%2001.jpg?width=900"),
    dict(n=2, name="Delta del Okavango (Maun)", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=-19.9833, lon=23.4167,
         desc="El mayor delta interior del mundo, Patrimonio de la Humanidad: un laberinto de canales, islas y lagunas donde el agua del interior se pierde en el desierto del Kalahari; Maun es la puerta de entrada logística para excursiones en mokoro o avioneta.",
         credit="Joachim Huber · CC BY-SA 2.0", source=W + "Okavango%20Delta%2C%20Botswana.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Kazungula (con Zambia/Zimbabue)", "Frontera", -17.7833, 25.2667,
     "Punto cuádruple con puente nuevo sobre el Zambeze; cruce ágil y bien equipado, base para entrar directamente en el Parque de Chobe desde Kasane."),
    ("Frontera · Mamuno/Trans-Kalahari (con Namibia)", "Frontera", -22.0333, 20.0167,
     "Cruce occidental por el corredor Trans-Kalahari, asfaltado y de baja congestión; alternativa si se enlaza con Namibia en lugar de Zambia/Zimbabue."),
    ("Embajada de España en Windhoek (competente para Botsuana)", "Consular", -22.5700, 17.0836,
     "58 Simeon Shixungileni Street, Windhoek (Namibia). Tel. +264 (0)61 22 30 66. Gestionar trámites mayores a través de esta embajada — ver ficha de Namibia para el contacto completo."),
    ("Letsholathebe II Memorial Hospital, Maun", "Hospital", -19.9950, 23.4200,
     "Principal hospital de referencia en la zona del Okavango; para necesidades serias, evacuación aérea hacia Gaborone o Sudáfrica es la práctica habitual en la región."),
    ("Combustible · Kasane / Maun", "Combustible", -17.8167, 25.1500,
     "Estaciones formales en ambas localidades de safari; repostar a fondo en cada una antes de tramos de pista hacia los parques."),
    ("Agua potable y de uso general · Kasane y Maun", "Agua potable", -17.8167, 25.1500,
     "Agua embotellada sin problema en ambas localidades; lodges y campings permiten llenar el depósito de uso general con manguera, confirmar en recepción dado el entorno semidesértico."),
]

DRONE_CALLOUT = ("danger", "Prohibido en la práctica en parques nacionales y reservas",
                  "Botsuana prohíbe el uso de drones dentro de sus parques nacionales y reservas de fauna (incluidos Chobe y el Delta del Okavango) sin un permiso específico, muy restrictivo en la práctica; fuera de estas áreas se exige registro ante la Civil Aviation Authority of Botswana. Norma del proyecto: no volar el dron en ningún parque o reserva sin autorización expresa ya concedida.")

STARLINK_CALLOUT = ("ok", "Disponible y operativo en 2026",
                     "Starlink está activo comercialmente en Botsuana, con buena cobertura incluso en zonas remotas como Maun y el entorno del Delta del Okavango; kit y suscripción configurables antes de entrar al país.")

DOG_MATRIX = [
    ("Chobe y Delta del Okavango", "prohibido", "No se permite el acceso de mascotas a los parques nacionales; dejar en Kasane o Maun con cuidador o en el alojamiento."),
    ("Kasane, Maun", "permitido con condiciones", "Correa y sombra; calor seco intenso, especialmente en la estación cálida (septiembre-noviembre)."),
]

SOURCES = [
    ("thingstodoinbotswana.com · requisitos de entrada 2026", "https://thingstodoinbotswana.com/entry-requirements/"),
    ("Gobierno de Botsuana · normativa de importación/exportación de vehículos", "https://www.gov.bw/policing/vehicle-importexport-clearance"),
    ("Botswana Tourism Organisation · formalidades de entrada", "https://www.botswanatourism.co.bw/travel-info/entry-formalities"),
    ("UNESCO · Delta del Okavango, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/1432/"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
]

CORRIDOR = [(-17.7833, 25.2667), (-17.8167, 25.1500), (-19.9833, 23.4167), (-22.0333, 20.0167)]

HISTORIA_RESUMEN = ("Botsuana es, a diferencia de casi todos sus vecinos, una de las democracias más estables y menos convulsas de África: el pueblo tswana llegó a un acuerdo con Gran Bretaña para protegerse de la expansión bóer, "
                     "logró la independencia en 1966 siendo entonces uno de los países más pobres del mundo, y transformó el hallazgo de diamantes en una de las historias de desarrollo más sólidas del continente.")

HISTORIA_SECCIONES = [
    ("Los reinos tswana del Kalahari",
     "Desde el siglo XVIII, distintos grupos tswana (bangwato, bakwena, bangwaketse) se establecieron en torno al desierto del Kalahari, desarrollando estructuras políticas centralizadas (los «morafe») bajo jefes hereditarios que gestionaban el ganado y el acceso al agua, un recurso crítico en esta región semidesértica."),
    ("El protectorado de Bechuanalandia",
     "Ante la amenaza de anexión por parte de la Compañía Británica de Sudáfrica de Cecil Rhodes, tres jefes tswana viajaron a Londres en 1895 y negociaron directamente con la Corona británica la protección de sus tierras, "
     "logrando que el territorio se convirtiera en el protectorado de Bechuanalandia en lugar de una colonia de explotación plena — una decisión que preservó buena parte de la autoridad tradicional tswana hasta la independencia."),
    ("Independencia y el descubrimiento de diamantes",
     "Botsuana se independizó en 1966 como una de las naciones más pobres del mundo, sin apenas infraestructura. Apenas un año después se descubrieron yacimientos de diamantes de primer nivel mundial, y el país, bajo un liderazgo que priorizó la gestión prudente de esos ingresos "
     "(a través de la empresa conjunta Debswana con De Beers), los convirtió en inversión en educación, sanidad e infraestructura en lugar de derrocharlos, evitando la llamada «maldición de los recursos» que ha afectado a otros países africanos."),
    ("Situación actual: modelo de estabilidad y conservación",
     "Botsuana se mantiene hoy como una de las democracias multipartidistas más estables de África, con alternancia pacífica en el poder, y ha apostado por un modelo de turismo de safari de alto valor y bajo volumen para proteger ecosistemas como el Delta del Okavango y el Parque de Chobe, "
     "que alberga una de las mayores poblaciones de elefantes del continente — el gran atractivo de este desvío opcional del proyecto."),
]

HISTORIA_FUENTES = [
    ("BBC News · Botswana country profile", "https://www.bbc.com/news/world-africa-13040376"),
    ("Encyclopaedia Britannica · Botswana, History", "https://www.britannica.com/place/Botswana/History"),
    ("UNESCO · Delta del Okavango", "https://whc.unesco.org/en/list/1432/"),
]

SPEC = dict(
    slug="botsuana", name="Botsuana", revision="9 sep 2026",
    sub="Alternativa · Kalahari/Chobe/Okavango",
    chips=[
        ("ROL EN LA RUTA", "opcional — Kalahari, Chobe y Delta del Okavango"),
        ("ENTRADA/SALIDA", "Kazungula (Zambia/Zimbabue) o Mamuno (Namibia)"),
        ("SEGURIDAD", "estable"),
        ("COMUNICACIONES", "Starlink activo (ok)"),
    ],
    center=[-19.5, 24.0], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, si finalmente se incluye este desvío.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    facts=[
        ("Rol en la ruta", "Alternativa de naturaleza de alto nivel (Chobe, Delta del Okavango) si el itinerario lo permite."),
        ("Entrada/salida", "Kazungula desde Zambia/Zimbabue, o Mamuno desde Namibia por el corredor Trans-Kalahari."),
        ("Seguridad", "País muy estable; una de las democracias más consolidadas de África, sin alertas relevantes para este proyecto."),
        ("Perro", "Prohibido en los parques nacionales del itinerario (Chobe, Okavango); planificar cuidado en Kasane o Maun."),
    ],
    alerts=[
        "Perro prohibido en Chobe y el Delta del Okavango: prever cuidador o alojamiento con guardería en Kasane o Maun.",
        "El acceso a zonas profundas del Delta del Okavango normalmente requiere avioneta o mokoro desde Maun, no vehículo propio: planificar esta logística con antelación.",
    ],
    ruta_intro="Entrada por Kazungula directamente al Parque de Chobe, travesía hacia Maun como base del Delta del Okavango, y salida hacia Namibia por el corredor Trans-Kalahari o vuelta al eje principal.",
    route_rows=[
        ("Entrada y fauna", "Kazungula → Chobe (Kasane)", "Safaris fluviales y en vehículo; alta densidad de elefantes"),
        ("Travesía del Kalahari", "Kasane → Maun", "Base logística del Delta del Okavango"),
        ("Delta", "Maun → Delta del Okavango", "Excursión en mokoro o avioneta; no accesible en vehículo propio"),
        ("Salida", "Maun → Mamuno (Namibia)", "Corredor Trans-Kalahari, asfaltado y de baja congestión"),
    ],
    offroad=[
        "Pistas de arena dentro de Chobe (recomendable 4x4 con buena tracción y presión de neumáticos reducida); el eje Kasane-Maun-Mamuno es carretera asfaltada.",
    ],
    acampada=[
        "Kasane: campings y lodges junto al río Chobe, con buena oferta orientada a overlanders.",
        "Maun: base logística con campings, agencias de excursión y aeródromo para vuelos al Delta.",
    ],
    visado=[
        "Exención de visado para españoles — verificar vigencia exacta 30-60 días antes.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica.",
    ],
    fronteras_rows=[
        ("Entrada/salida (este)", "Kazungula (Zambia/Zimbabue)", "Punto cuádruple; puente nuevo sobre el Zambeze."),
        ("Entrada/salida (oeste)", "Mamuno (Namibia)", "Corredor Trans-Kalahari, asfaltado y de baja congestión."),
    ],
    vehiculos=[
        "Permiso temporal en frontera para el vehículo; confirmar despacho aduanero en el Departamento de Policía de Tránsito según el punto de entrada.",
        "Seguro de terceros SADC válido en Botsuana como miembro de la región.",
        "Presión de neumáticos reducida recomendable para las pistas de arena de Chobe.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No volar en ningún caso dentro de Chobe o el Delta del Okavango sin autorización expresa ya concedida.",
        "Registrar el dron ante la Civil Aviation Authority of Botswana para su uso fuera de parques y reservas.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo y operativo en 2026, con buena cobertura incluso en Maun y el entorno del Delta.",
        "SIM local (Mascom, Orange Botswana) como respaldo en zonas más remotas.",
    ],
    perro_intro=[
        "Certificado veterinario internacional y permiso de importación previo, exigibles en frontera.",
        "Perro prohibido en Chobe y el Delta del Okavango; prever cuidador o alojamiento con guardería en Kasane o Maun.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en el norte del país (Chobe, Okavango): profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Letsholathebe II Memorial Hospital (Maun) como referencia regional; evacuación aérea hacia Gaborone o Sudáfrica para casos serios.",
    ],
    seguridad_intro="Botsuana es una de las democracias más estables de África y uno de los tramos más tranquilos de todo el proyecto; la principal atención debe ir a la fauna salvaje, no a la seguridad ciudadana.",
    seguridad=[
        "Respetar siempre las distancias de seguridad con la fauna en Chobe y el Delta, y las indicaciones del guía o ranger.",
        "Precaución normal de viaje en Kasane y Maun.",
        "Llevar reserva de agua y combustible en los tramos de pista dentro de Chobe, por si se prolonga el safari.",
    ],
    agua=[
        "Kasane y Maun: agua embotellada sin problema.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): lodges y campings de ambas localidades permiten llenar el depósito con manguera; confirmar en recepción dado el entorno semidesértico.",
    ],
    combustible=[
        "Kasane y Maun concentran la oferta fiable de la región; repostar a fondo en cada una antes de las pistas de arena de Chobe o el tramo Trans-Kalahari.",
        "Sin gap relevante de 500 km en el eje asfaltado Kasane-Maun-Mamuno.",
    ],
    pendientes=[
        ("Delta del Okavango", "Reservar con antelación la excursión en mokoro o avioneta desde Maun"),
        ("Perro", "Confirmar guardería o cuidador en Kasane/Maun durante las visitas a los parques"),
        ("Dron", "Registrar ante la Civil Aviation Authority of Botswana si se quiere volar fuera de los parques"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Botsuana es un desvío opcional: confirmar si se incluye antes de revalidar el resto de trámites.",
    emergency="Sin representación española propia en Botsuana — gestionar emergencias a través de la Embajada de España en Windhoek (Namibia), competente para el país: +264 (0)61 22 30 66.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

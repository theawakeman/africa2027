# -*- coding: utf-8 -*-
"""Uganda — ficha completa (9 sep 2026): alternativa Kampala/Bwindi (gorilas)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Kampala", cat="Ciudad", prio="Media", dog="permitido con condiciones", time="1-2 noches",
         lat=0.3476, lon=32.5825,
         desc="Capital vibrante repartida sobre siete colinas, con mercados, templos de distintas religiones y el cercano origen del Nilo en Jinja como excursión clásica; base logística y de gestiones para la ruta hacia Bwindi.",
         credit="Todd Huffman · CC BY 2.0", source=W + "Kampala%20skyline.jpg?width=900"),
    dict(n=2, name="Bosque Impenetrable de Bwindi (Buhoma)", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=-1.0500, lon=29.6167,
         desc="Patrimonio de la Humanidad y uno de los últimos refugios del gorila de montaña; el trekking guiado para verlos (con permiso previo, cupo muy limitado) es una de las experiencias de naturaleza más singulares de toda la ruta.",
         credit="Giles Laurent · CC BY-SA 4.0", source=W + "068%20Mountain%20gorilla%20close-up%20at%20Bwindi%20Impenetrable%20Forest%20National%20Park%20Photo%20by%20Giles%20Laurent.jpg?width=900"),
]

_CAT_COLOR = {"ciudad": "azul", "naturaleza": "verde"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Malaba (con Kenia)", "Frontera", 0.6333, 34.2667,
     "Principal paso del corredor Norte hacia/desde Kenia; puesto de ventanilla única, con tráfico pesado de camiones y tiempos de espera variables."),
    ("Frontera · Busia (con Kenia)", "Frontera", 0.4667, 34.0833,
     "Alternativa a Malaba, algo menos congestionada, también con formato de ventanilla única."),
    ("Embajada de España en Nairobi (competente para Uganda)", "Consular", -1.2921, 36.8219,
     "CBA Building, 3ª planta, Mara & Ragati Roads, Upper Hill, Nairobi (Kenia). Tel. +254 20 272 02 22/3/4/5; emergencias +254 733 63 11 44. Gestionar trámites mayores a través de esta embajada."),
    ("Mulago National Referral Hospital, Kampala", "Hospital", 0.3419, 32.5764,
     "Principal hospital de referencia del país; para necesidades serias, evacuación hacia Nairobi es la práctica habitual en la región."),
    ("Combustible · Kampala / Kabale (acceso a Bwindi)", "Combustible", 0.3476, 32.5825,
     "Estaciones formales en ambas localidades; repostar a fondo en Kabale antes del tramo final de pista hacia Buhoma."),
    ("Agua potable y de uso general · Kampala y Kabale", "Agua potable", 0.3476, 32.5825,
     "Agua embotellada sin problema en ambas localidades; lodges de Buhoma permiten llenar el depósito de uso general con manguera, confirmar en recepción."),
]

DRONE_CALLOUT = ("danger", "Prohibido en la práctica: permiso previo obligatorio y muy restrictivo",
                  "Uganda exige un permiso previo de la Uganda Civil Aviation Authority para cualquier uso de drones, con un proceso largo y poco predecible; su uso dentro de parques nacionales y zonas de trekking de gorilas (Bwindi) está prácticamente excluido en la práctica. Norma del proyecto: no volar el dron en ningún parque o zona de trekking sin autorización expresa ya concedida.")

STARLINK_CALLOUT = ("ok", "Disponible y operativo en 2026",
                     "Starlink está activo comercialmente en Uganda desde 2023, con cobertura razonable en Kampala y aceptable en zonas rurales del suroeste como Kabale/Bwindi; kit y suscripción configurables antes de entrar al país.")

DOG_MATRIX = [
    ("Bosque Impenetrable de Bwindi", "prohibido", "No se permite el acceso de mascotas al parque ni al trekking de gorilas; dejar en Buhoma o Kabale con cuidador o en el alojamiento."),
    ("Kampala, Kabale", "permitido con condiciones", "Correa y control en zonas urbanas; tráfico denso en Kampala requiere atención extra."),
]

SOURCES = [
    ("Uganda Immigration · portal oficial de visados electrónicos", "https://visas.immigration.go.ug/"),
    ("Uganda Wildlife Authority · permisos de trekking de gorilas", "https://www.ugandawildlife.org/"),
    ("Uganda Civil Aviation Authority · normativa de drones", "https://www.caa.co.ug/"),
    ("UNESCO · Bosque Impenetrable de Bwindi, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/682/"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
]

CORRIDOR = [(0.6333, 34.2667), (0.3476, 32.5825), (-1.0500, 29.6167), (0.4667, 34.0833)]

HISTORIA_RESUMEN = ("Uganda combina varios reinos tradicionales de gran profundidad histórica —sobre todo Buganda, en torno a Kampala— con un colonialismo británico que dejó fronteras que agruparon a decenas de pueblos distintos, una independencia en 1962 pronto ensombrecida "
                     "por la dictadura de Idi Amín en los años setenta, y una recuperación posterior que ha convertido al país en uno de los últimos refugios del gorila de montaña y en un destino de naturaleza de primer nivel.")

HISTORIA_SECCIONES = [
    ("El reino de Buganda y otros reinos tradicionales",
     "El territorio de la actual Uganda albergaba varios reinos centralizados de gran antigüedad y sofisticación política, en particular el reino de Buganda (en torno al lago Victoria y la actual Kampala), junto con Bunyoro, Toro y Busoga, "
     "con monarquías (el kabaka de Buganda) que conservan hoy un papel ceremonial y cultural reconocido dentro del estado moderno."),
    ("El protectorado británico",
     "Gran Bretaña estableció un protectorado sobre Uganda en 1894, gobernando en gran medida a través de una alianza con la aristocracia de Buganda, a la que otorgó privilegios frente a otros reinos y pueblos del territorio — una dinámica de favoritismo colonial "
     "que sembró tensiones interregionales que se prolongarían mucho después de la independencia."),
    ("Independencia, Idi Amín y el terror de los años setenta",
     "Uganda se independizó en 1962. Tras un periodo de inestabilidad política que incluyó la abolición de los reinos tradicionales, el general Idi Amín tomó el poder en 1971 y gobernó hasta 1979 mediante una de las dictaduras más brutales de la historia africana reciente, "
     "con cientos de miles de muertos y la expulsión de la minoría asiática del país, hasta ser derrocado tras la guerra con la Tanzania de Julius Nyerere."),
    ("Situación actual: estabilidad bajo Museveni y naturaleza como motor turístico",
     "Yoweri Museveni gobierna el país desde 1986, en un periodo de relativa estabilidad y crecimiento económico marcado también por sucesivas reformas constitucionales para prolongar su mandato y por restricciones a la oposición y la prensa, "
     "un asunto con debate internacional activo. Uganda se ha consolidado entretanto como destino de naturaleza de referencia, con el trekking de gorilas de montaña en Bwindi como su gran atractivo, motivo de esta parada opcional del proyecto."),
]

HISTORIA_FUENTES = [
    ("BBC News · Uganda country profile", "https://www.bbc.com/news/world-africa-14107906"),
    ("Encyclopaedia Britannica · Uganda, History", "https://www.britannica.com/place/Uganda/History"),
    ("UNESCO · Bosque Impenetrable de Bwindi", "https://whc.unesco.org/en/list/682/"),
]

SPEC = dict(
    slug="uganda", name="Uganda", revision="9 sep 2026",
    sub="Alternativa · Kampala/Bwindi (gorilas)",
    chips=[
        ("ROL EN LA RUTA", "opcional — trekking de gorilas en Bwindi"),
        ("ENTRADA/SALIDA", "Malaba o Busia (Kenia)"),
        ("SEGURIDAD", "moderada — precaución normal"),
        ("COMUNICACIONES", "Starlink activo (ok)"),
    ],
    center=[0.0, 31.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, si finalmente se incluye este desvío.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    facts=[
        ("Rol en la ruta", "Alternativa de naturaleza de alto nivel: trekking de gorilas de montaña en Bwindi, permiso previo obligatorio y muy limitado en cupo."),
        ("Entrada/salida", "Malaba o Busia desde Kenia; enlaza con Ruanda hacia el sur si se combina con el trekking de Volcanoes NP."),
        ("Seguridad", "Precaución normal de viaje; estabilidad interna con debate político activo sobre el largo mandato de Museveni, sin afectar en la práctica a la ruta turística."),
        ("Perro", "Prohibido en Bwindi; planificar cuidado en Buhoma o Kabale."),
    ],
    alerts=[
        "El permiso de trekking de gorilas en Bwindi (Uganda Wildlife Authority) tiene cupo diario muy limitado y conviene reservarlo con varios meses de antelación.",
        "Perro prohibido en Bwindi: prever cuidador o alojamiento con guardería en Buhoma o Kabale.",
    ],
    ruta_intro="Entrada por Malaba o Busia desde Kenia, escala en Kampala para gestiones y descanso, travesía hacia el suroeste vía Kabale hasta Buhoma (Bwindi) para el trekking de gorilas, con posible enlace hacia Ruanda.",
    route_rows=[
        ("Entrada", "Malaba/Busia → Kampala", "Gestiones, descanso, excursión opcional a las fuentes del Nilo en Jinja"),
        ("Travesía suroeste", "Kampala → Kabale", "Escala logística antes del tramo final de pista"),
        ("Trekking de gorilas", "Kabale → Buhoma (Bwindi)", "Permiso previo obligatorio; cupo diario muy limitado"),
        ("Salida", "Buhoma → frontera con Ruanda", "Enlace opcional hacia Volcanoes NP (Ruanda) para más trekking"),
    ],
    offroad=[
        "Pista de tierra y curvas cerradas en el tramo final Kabale-Buhoma (recomendable 4x4, especialmente en temporada de lluvias, mar-may y sep-nov); el resto del eje es carretera asfaltada.",
    ],
    acampada=[
        "Kampala: opciones limitadas orientadas a overlanders; considerar alojamiento urbano convencional.",
        "Buhoma: campamentos y lodges junto al parque, con parcelas para vehículo propio en varios de ellos.",
    ],
    visado=[
        "Visado electrónico (e-visa) obligatorio para españoles, tramitar con antelación online.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
    ],
    fronteras_rows=[
        ("Entrada/salida (este)", "Malaba (Kenia)", "Corredor Norte principal; ventanilla única, tráfico pesado de camiones."),
        ("Entrada/salida (este, alt.)", "Busia (Kenia)", "Alternativa a Malaba, algo menos congestionada."),
    ],
    vehiculos=[
        "Permiso temporal en frontera para el vehículo; confirmar despacho aduanero según el punto de entrada.",
        "Seguro de terceros COMESA válido en Uganda como miembro de la región.",
        "Carné de conducir internacional recomendable junto con el nacional.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No volar en ningún caso dentro de Bwindi o durante el trekking de gorilas sin autorización expresa ya concedida.",
        "Solicitar el permiso de la Uganda Civil Aviation Authority con mucha antelación si se quiere volar fuera de zonas protegidas; proceso lento y poco predecible.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo desde 2023, con cobertura razonable en Kampala y aceptable en el suroeste (Kabale/Bwindi).",
        "SIM local (MTN Uganda, Airtel) como respaldo en zonas más remotas.",
    ],
    perro_intro=[
        "Certificado veterinario internacional y permiso de importación previo, exigibles en frontera.",
        "Perro prohibido en Bwindi y durante el trekking de gorilas; prever cuidador o alojamiento con guardería en Buhoma o Kabale.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en todo el país, incluida la zona de Bwindi: profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido en frontera.",
        "Mulago National Referral Hospital (Kampala) como referencia nacional; evacuación hacia Nairobi para casos serios.",
    ],
    seguridad_intro="Precaución normal de viaje en el eje turístico Kampala-Kabale-Bwindi; el debate político interno sobre la larga presidencia de Museveni no suele afectar en la práctica al recorrido, pero conviene evitar concentraciones y manifestaciones.",
    seguridad=[
        "Evitar manifestaciones políticas y concentraciones, especialmente en periodos electorales.",
        "Respetar siempre las indicaciones del guía durante el trekking de gorilas: distancia mínima y normas de comportamiento ante los animales.",
        "Tráfico denso e indisciplinado en Kampala: extremar precaución al circular por la capital.",
    ],
    agua=[
        "Kampala y Kabale: agua embotellada sin problema.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): lodges de Buhoma permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Kampala y Kabale concentran la oferta fiable; repostar a fondo en Kabale antes del tramo final de pista hacia Buhoma.",
        "Sin gap relevante de 500 km en el eje Malaba-Kampala-Kabale, mayoritariamente asfaltado.",
    ],
    pendientes=[
        ("Trekking de gorilas", "Reservar permiso con la Uganda Wildlife Authority con varios meses de antelación (cupo muy limitado)"),
        ("Perro", "Confirmar guardería o cuidador en Buhoma/Kabale durante el trekking"),
        ("Dron", "Evaluar si compensa solicitar permiso a la Uganda Civil Aviation Authority dado el proceso largo"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Uganda es un desvío opcional: confirmar si se incluye antes de revalidar el resto de trámites.",
    emergency="Sin representación española propia en Uganda — gestionar emergencias a través de la Embajada de España en Nairobi (Kenia), competente para el país: +254 20 272 02 22/3/4/5; emergencias +254 733 63 11 44.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

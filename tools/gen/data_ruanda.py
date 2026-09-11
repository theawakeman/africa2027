# -*- coding: utf-8 -*-
"""Ruanda — ficha completa (9 sep 2026): alternativa Kigali/Volcanoes NP (gorilas)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Kigali", cat="Ciudad", prio="Media", dog="permitido con condiciones", time="1-2 noches",
         lat=-1.9441, lon=30.0619,
         desc="Una de las capitales más limpias y ordenadas de África, reconstruida tras el genocidio de 1994; el Kigali Genocide Memorial es visita obligada para entender el país, y la ciudad sirve de base logística y de gestiones antes de subir a Volcanoes NP.",
         credit="Baraka29 · CC BY-SA 4.0", source=W + "Kigali%20city%20view.jpg?width=900"),
    dict(n=2, name="Parque Nacional de los Volcanes (Kinigi)", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=-1.4667, lon=29.4833,
         desc="Cadena de volcanes de los Virunga y uno de los últimos refugios del gorila de montaña; el trekking guiado (permiso previo, cupo muy limitado y de coste elevado) es la gran experiencia de naturaleza de este desvío, junto a rutas al lago del cráter del Bisoke.",
         credit="Happy Gentille · CC0", source=W + "Bisoke%20Crater%20Lake%20in%20Volcanoes%20National%20Park%2C%20Rwanda.jpg?width=900"),
]

_CAT_COLOR = {"ciudad": "azul", "naturaleza": "verde"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Rusumo (con Tanzania)", "Frontera", -2.3833, 30.7833,
     "Principal paso hacia/desde Tanzania, puesto de ventanilla única sobre el río Kagera; cruce relativamente ágil."),
    ("Frontera · Gatuna/Katuna (con Uganda)", "Frontera", -1.3000, 30.0500,
     "Paso habitual hacia/desde Uganda, útil para enlazar con el trekking de gorilas de Bwindi; sujeto a cierres o restricciones puntuales según el estado de las relaciones bilaterales, verificar antes de viajar."),
    ("Embajada de España en Dar es Salaam (competente para Ruanda)", "Consular", -6.7924, 39.2083,
     "99 B Kinondoni Road, Dar es Salaam (Tanzania). Tel. +255 022 266 60 18/19; emergencias +255 754 04 21 23. Gestionar trámites mayores a través de esta embajada."),
    ("King Faisal Hospital, Kigali", "Hospital", -1.9548, 30.0930,
     "Principal hospital de referencia privado-público de la capital; para necesidades serias, evacuación hacia Nairobi es la práctica habitual en la región."),
    ("Combustible · Kigali / Musanze (acceso a Volcanoes NP)", "Combustible", -1.9441, 30.0619,
     "Estaciones formales en ambas localidades; repostar a fondo en Musanze antes del tramo final hacia Kinigi."),
    ("Agua potable y de uso general · Kigali y Musanze", "Agua potable", -1.9441, 30.0619,
     "Agua embotellada sin problema en ambas localidades; lodges de Kinigi permiten llenar el depósito de uso general con manguera, confirmar en recepción."),
]

DRONE_CALLOUT = ("danger", "Prohibido sin permiso previo, y prácticamente excluido en Volcanoes NP",
                  "Ruanda exige un permiso previo de la Rwanda Utilities Regulatory Authority (RURA) para cualquier uso de drones, con proceso restrictivo; su uso dentro de Volcanoes National Park y durante el trekking de gorilas está prohibido en la práctica. Norma del proyecto: no volar el dron en ningún parque o zona de trekking sin autorización expresa ya concedida.")

STARLINK_CALLOUT = ("ok", "Disponible y operativo en 2026",
                     "Starlink está activo comercialmente en Ruanda, uno de los primeros países africanos en autorizarlo, con buena cobertura incluso en Kigali y zonas rurales del norte; kit y suscripción configurables antes de entrar al país.")

DOG_MATRIX = [
    ("Parque Nacional de los Volcanes", "prohibido", "No se permite el acceso de mascotas al parque ni al trekking de gorilas; dejar en Musanze o Kinigi con cuidador o en el alojamiento."),
    ("Kigali, Musanze", "permitido con condiciones", "Correa y control en zonas urbanas; normativa municipal de limpieza especialmente estricta en Kigali."),
]

SOURCES = [
    ("Irembo · portal oficial de trámites del gobierno de Ruanda (visados)", "https://irembo.gov.rw/"),
    ("Rwanda Development Board · permisos de trekking de gorilas", "https://www.rdb.rw/"),
    ("Rwanda Utilities Regulatory Authority (RURA) · normativa de drones", "https://www.rura.rw/"),
    ("UNESCO · Parque Nacional de los Volcanes (lista indicativa)", "https://whc.unesco.org/en/tentativelists/5439/"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
]

CORRIDOR = [(-2.3833, 30.7833), (-1.9441, 30.0619), (-1.4667, 29.4833), (-1.3000, 30.0500)]

HISTORIA_RESUMEN = ("Ruanda es un país pequeño y densamente poblado con una identidad precolonial fuertemente centralizada en torno a la monarquía tutsi, cuyas divisiones étnicas fueron rigidificadas y explotadas por el colonialismo belga hasta desembocar en el genocidio de 1994 contra los tutsis, "
                     "uno de los episodios más brutales del siglo XX; desde entonces el país ha construido una reconstrucción notable bajo un gobierno fuertemente centralizado, con Kigali como modelo regional de orden y desarrollo, aunque con muy poco espacio para la disidencia política.")

HISTORIA_SECCIONES = [
    ("El reino de Ruanda precolonial",
     "Antes de la colonización, el territorio estaba organizado en torno a un reino centralizado dominado por la monarquía tutsi (el mwami), con una estructura social jerárquica entre tutsis, hutus y twa que originalmente tenía más de casta socioeconómica y ocupacional "
     "(ganaderos frente a agricultores) que de origen étnico o racial diferenciado, con importante movilidad entre grupos."),
    ("El colonialismo alemán y belga: la fabricación de la división étnica",
     "Alemania y después Bélgica (tras la Primera Guerra Mundial) gobernaron a través de la aristocracia tutsi, a la que favorecieron sistemáticamente, y introdujeron carnés de identidad étnica obligatorios que fijaron de forma rígida y pseudocientífica una distinción entre hutus y tutsis "
     "que hasta entonces había sido mucho más fluida, sentando las bases del enfrentamiento posterior."),
    ("El genocidio de 1994",
     "Tras décadas de tensión poselecciones y varios episodios de violencia previa, el asesinato del presidente en abril de 1994 desencadenó un genocidio planificado contra la población tutsi (y hutus moderados) que se cobró alrededor de 800.000 vidas en apenas cien días, "
     "uno de los genocidios más rápidos y brutales de la historia moderna, hasta que el Frente Patriótico Ruandés puso fin a la matanza y tomó el poder."),
    ("Situación actual: reconstrucción, centralización del poder y crecimiento",
     "Desde 1994, el gobierno liderado por Paul Kagame ha impulsado una notable reconstrucción económica e institucional —Kigali es hoy una de las ciudades más limpias y seguras de África y un centro de innovación tecnológica regional—, "
     "combinada con un control político muy estricto, restricciones severas a la oposición y a la prensa, y una prohibición legal de mencionar la etnia en la vida pública como parte de una política oficial de reconciliación nacional; el país también ha estado implicado en tensiones "
     "y conflictos armados en la vecina RD Congo, un asunto de atención internacional continuada."),
]

HISTORIA_FUENTES = [
    ("BBC News · Rwanda country profile", "https://www.bbc.com/news/world-africa-14093238"),
    ("Encyclopaedia Britannica · Rwanda, History", "https://www.britannica.com/place/Rwanda/History"),
    ("United Nations · Outreach Programme on the Rwanda Genocide", "https://www.un.org/en/preventgenocide/rwanda/"),
]

SPEC = dict(
    slug="ruanda", name="Ruanda", revision="9 sep 2026",
    sub="Alternativa · Kigali/Volcanoes NP (gorilas)",
    chips=[
        ("ROL EN LA RUTA", "opcional — trekking de gorilas en Volcanoes NP"),
        ("ENTRADA/SALIDA", "Rusumo (Tanzania) o Gatuna (Uganda)"),
        ("SEGURIDAD", "estable — orden y control fuertes"),
        ("COMUNICACIONES", "Starlink activo (ok)"),
    ],
    center=[-1.9, 29.9], zoom=7,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, si finalmente se incluye este desvío.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    facts=[
        ("Rol en la ruta", "Alternativa de naturaleza de alto nivel: trekking de gorilas de montaña en Volcanoes NP, permiso previo obligatorio y de coste elevado."),
        ("Entrada/salida", "Rusumo desde Tanzania, o Gatuna/Katuna desde Uganda si se combina con Bwindi."),
        ("Seguridad", "País muy ordenado y seguro para el visitante, con control político interno estricto; sin alertas relevantes para el turista en la ruta prevista."),
        ("Perro", "Prohibido en Volcanoes NP; planificar cuidado en Musanze o Kinigi."),
    ],
    alerts=[
        "El permiso de trekking de gorilas en Volcanoes NP (Rwanda Development Board) tiene cupo diario muy limitado, coste elevado y conviene reservarlo con varios meses de antelación.",
        "Verificar el estado de la frontera de Gatuna/Katuna con Uganda antes de viajar, ya que ha sufrido cierres o restricciones puntuales en el pasado por tensiones bilaterales.",
        "Perro prohibido en Volcanoes NP: prever cuidador o alojamiento con guardería en Musanze o Kinigi.",
    ],
    ruta_intro="Entrada por Rusumo desde Tanzania o Gatuna desde Uganda, escala en Kigali para gestiones y memoria histórica, travesía hacia el norte vía Musanze hasta Kinigi para el trekking de gorilas en Volcanoes NP.",
    route_rows=[
        ("Entrada", "Rusumo/Gatuna → Kigali", "Gestiones, Kigali Genocide Memorial"),
        ("Travesía norte", "Kigali → Musanze", "Escala logística antes del acceso al parque"),
        ("Trekking de gorilas", "Musanze → Kinigi (Volcanoes NP)", "Permiso previo obligatorio; cupo diario muy limitado"),
        ("Salida", "Kinigi → frontera con Uganda", "Enlace opcional hacia Bwindi (Uganda) para más trekking"),
    ],
    offroad=[
        "Pista de tierra en el tramo final Musanze-Kinigi (practicable con turismo la mayor parte del año, algo más exigente en temporada de lluvias); el resto del eje es carretera asfaltada en muy buen estado.",
    ],
    acampada=[
        "Kigali: opciones limitadas orientadas a overlanders; considerar alojamiento urbano convencional.",
        "Kinigi: campamentos y lodges junto al parque, con parcelas para vehículo propio en varios de ellos.",
    ],
    visado=[
        "Visado a la llegada o e-visa disponible para españoles, tramitar con antelación vía Irembo si se prefiere.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica.",
    ],
    fronteras_rows=[
        ("Entrada/salida (este)", "Rusumo (Tanzania)", "Ventanilla única sobre el río Kagera; cruce ágil."),
        ("Entrada/salida (norte)", "Gatuna/Katuna (Uganda)", "Verificar estado antes de viajar por posibles restricciones bilaterales."),
    ],
    vehiculos=[
        "Permiso temporal en frontera para el vehículo; confirmar despacho aduanero según el punto de entrada.",
        "Seguro de terceros COMESA válido en Ruanda como miembro de la región.",
        "Normativa de tráfico y limpieza urbana muy estricta en Kigali (bolsas de plástico prohibidas en todo el país): evitar llevarlas al cruzar la frontera.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No volar en ningún caso dentro de Volcanoes NP o durante el trekking de gorilas sin autorización expresa ya concedida.",
        "Solicitar el permiso de la RURA con antelación si se quiere volar fuera de zonas protegidas; proceso restrictivo.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo y de los primeros autorizados en África, con buena cobertura incluso en Musanze y Kinigi.",
        "SIM local (MTN Rwanda, Airtel) como respaldo en zonas más remotas.",
    ],
    perro_intro=[
        "Certificado veterinario internacional y permiso de importación previo, exigibles en frontera.",
        "Perro prohibido en Volcanoes NP y durante el trekking de gorilas; prever cuidador o alojamiento con guardería en Musanze o Kinigi.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en zonas bajas del país, riesgo menor en las zonas altas de Volcanoes NP: profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "King Faisal Hospital (Kigali) como referencia nacional; evacuación hacia Nairobi para casos serios.",
    ],
    seguridad_intro="Ruanda es percibido como uno de los países más seguros y ordenados de África para el visitante, con un control estatal muy fuerte; conviene evitar cualquier comentario público sobre etnia o política interna, tema legalmente sensible en el país.",
    seguridad=[
        "Evitar comentarios o publicaciones sobre etnia, genocidio o política interna que puedan malinterpretarse; el tema está regulado legalmente.",
        "Respetar siempre las indicaciones del guía durante el trekking de gorilas: distancia mínima y normas de comportamiento ante los animales.",
        "Normativa muy estricta contra bolsas de plástico de un solo uso en todo el país: no introducirlas.",
    ],
    agua=[
        "Kigali y Musanze: agua embotellada sin problema.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): lodges de Kinigi permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Kigali y Musanze concentran la oferta fiable; repostar a fondo en Musanze antes del tramo final hacia Kinigi.",
        "Sin gap relevante de 500 km en el eje asfaltado Rusumo-Kigali-Musanze.",
    ],
    pendientes=[
        ("Trekking de gorilas", "Reservar permiso con el Rwanda Development Board con varios meses de antelación (cupo muy limitado, coste elevado)"),
        ("Frontera con Uganda", "Verificar el estado de Gatuna/Katuna antes de viajar por posibles restricciones bilaterales"),
        ("Perro", "Confirmar guardería o cuidador en Musanze/Kinigi durante el trekking"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Ruanda es un desvío opcional: confirmar si se incluye antes de revalidar el resto de trámites.",
    emergency="Sin representación española propia en Ruanda — gestionar emergencias a través de la Embajada de España en Dar es Salaam (Tanzania), competente para el país: +255 022 266 60 18/19; emergencias +255 754 04 21 23.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

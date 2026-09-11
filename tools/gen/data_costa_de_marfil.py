# -*- coding: utf-8 -*-
"""Costa de Marfil — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Man y las Dents de Man", cat="Naturaleza · montaña", prio="Media", dog="permitido", time="1–2 días",
         lat=7.4125, lon=-7.5539,
         desc="Ciudad de montaña rodeada de picos escarpados (Dents de Man), cascadas y puentes colgantes tradicionales de liana. Base de aclimatación tras la entrada desde Liberia, con clima más fresco que la costa.",
         credit="Zenman/Letsgoforward · CC BY-SA 3.0", source=W + "Dent%20de%20Man%20montagne.jpg?width=900"),
    dict(n=2, name="Yamoussoukro — Basílica de Nuestra Señora de la Paz", cat="Patrimonio", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=6.8167, lon=-5.2833,
         desc="Capital política del país y mayor basílica católica del mundo por superficie, réplica ampliada de San Pedro del Vaticano. Visita guiada obligatoria en el interior; el perro puede quedarse en el vehículo o esperar en el exterior del recinto.",
         credit="Didierwiki · CC0", source=W + "Basilique%20notre%20Dame%20de%20la%20Paix%20de%20Yamoussoukro%20(2).jpg?width=900"),
    dict(n=3, name="Grand-Bassam", cat="Patrimonio UNESCO", prio="Media", dog="permitido", time="1 día",
         lat=5.2000, lon=-3.7333,
         desc="Antigua capital colonial francesa, ciudad UNESCO de arquitectura colonial en decadencia elegante junto a playas de arena; museo del traje y ambiente artesanal. Parada obligada cerca de Abidjan.",
         credit="Adoscam · CC BY-SA 4.0", source=W + "WikiConvFr23%20Visite%20B%C3%A2timents%20sites%20historiques%20de%20Grand-Bassam%20(boblioth%C3%A8que%20municicpale%20de%20Grand-Bassam%20)%2002.jpg?width=900"),
    dict(n=4, name="Abidjan (Plateau y puerto)", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=5.3097, lon=-4.0122,
         desc="Capital económica y mayor base logística del golfo de Guinea occidental: puerto, aeropuerto internacional, embajada de España, talleres y recambios 4x4 de referencia regional.",
         credit="Adoscam · CC BY-SA 4.0", source=W + "WikiConvFr23%20Visite%20B%C3%A2timents%20sites%20historiques%20de%20Grand-Bassam%20(boblioth%C3%A8que%20municicpale%20de%20Grand-Bassam%20)%2003.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza · montaña": "verde", "patrimonio": "marron", "patrimonio unesco": "marron", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Danané/Loguatuo (desde Liberia)", "Frontera", 7.2500, -8.1500,
     "Continuación de la ruta desde Ganta (Liberia); control de inmigración y aduanas. Confirmar estado de la vía en temporada de lluvias."),
    ("Frontera · Salida — Noé/Elubo (hacia Ghana)", "Frontera", 5.1667, -2.7667,
     "Paso principal y más transitado hacia Ghana; carretera pavimentada en buen estado en el lado ghanés, puente sobre el río fronterizo. Horario 06:00-18:00."),
    ("Embajada de España en Abidjan", "Consular", 5.3600, -3.9700,
     "Impasse Ablaha Pokou, Cocody Danga Nord, Abiyán. +225 22 44 48 50 · fax +225 22 44 71 22 · emb.abidjan@maec.es."),
    ("CHU de Cocody — Abidjan", "Hospital", 5.3550, -3.9850,
     "Centro Hospitalario Universitario de referencia en la capital económica; mejor capacidad de la región para urgencias graves. Coordenada urbana aproximada."),
    ("Combustible · Man", "Combustible", 7.4125, -7.5539,
     "Estaciones formales (Total, Ola Energy) en la ciudad de montaña; primer repostaje serio tras la frontera de Liberia."),
    ("Combustible · Yamoussoukro", "Combustible", 6.8167, -5.2833,
     "Buena oferta en la capital política, a medio camino hacia la costa."),
    ("Combustible · Abidjan", "Combustible", 5.3097, -4.0122,
     "Mejor oferta y calidad del país; repostar aquí antes de Grand-Bassam y del tramo final a Ghana."),
    ("Agua potable · Abidjan y Yamoussoukro (supermercados y garrafas)", "Agua potable", 5.3097, -4.0122,
     "Agua embotellada ampliamente disponible en las ciudades del itinerario; sin problema de suministro en este tramo."),
]

DRONE_CALLOUT = ("warn", "Autorización previa recomendable; sin procedimiento turístico simplificado",
                  "No se ha localizado un trámite turístico simplificado para drones en Costa de Marfil. Solicitar autorización previa por escrito a la ANAC (Agence Nationale de l'Aviation Civile) antes de introducir o volar el equipo, especialmente cerca de Abidjan, Yamoussoukro y zonas gubernamentales.")

STARLINK_CALLOUT = ("warn", "Servicio recién autorizado (2026): confirmar activación real antes de contar con él",
                     "Costa de Marfil autorizó a Starlink a lanzar servicio en julio de 2026, pero la cobertura y el marco de itinerancia pueden seguir en despliegue en el momento del viaje. Revisar el mapa oficial 30-60 días antes de entrar y mantener SIM local (Orange, MTN, Moov) como respaldo principal.")

DOG_MATRIX = [
    ("Interior de la Basílica de Yamoussoukro", "requiere autorización escrita", "El perro espera fuera o en el vehículo durante la visita guiada."),
    ("Resto del país (Man, Grand-Bassam, Abidjan)", "permitido con condiciones", "Correa y sombra; tráfico denso en Abidjan."),
]

SOURCES = [
    ("Bradt Guides · visados y viaje a Costa de Marfil", "https://www.bradtguides.com/destinations/africa/ivory-coast/travel-and-visas/"),
    ("Digital Logistics Capacity Assessment · frontera de Elubo", "https://lca.logcluster.org/ghana-232-border-crossing-elubo"),
    ("Embajada de España en Abidjan · consulados y demarcación", "https://www.exteriores.gob.es/Embajadas/abidjan/es/Embajada/Paginas/Consulados.aspx"),
    ("Financial Afrik · autorización de Starlink en Costa de Marfil (jul. 2026)", "https://www.financialafrik.com/en/2026/07/21/ivory-coast-allows-starlink-to-launch-its-satellite-internet-service/"),
    ("UNESCO · Grand-Bassam", "https://whc.unesco.org/en/list/1322/"),
    ("Comisión Europea · animales de compañía", "https://europa.eu/youreurope/citizens/travel/carry/pets-and-other-animals/index_es.htm"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(7.2500, -8.1500), (7.4125, -7.5539), (6.8167, -5.2833), (5.3097, -4.0122), (5.2000, -3.7333), (5.1667, -2.7667)]

HISTORIA_RESUMEN = ("Costa de Marfil fue durante décadas el «milagro económico» del África Occidental francófona bajo su primer presidente, Félix Houphouët-Boigny, gracias al cacao y al café; tras su muerte en 1993 el país cayó en una crisis de identidad nacional "
                     "en torno al concepto de «ivoirité» que desembocó en dos guerras civiles (2002-2007 y 2010-2011), superadas con una recuperación económica notable en la última década bajo el presidente Alassane Ouattara.")

HISTORIA_SECCIONES = [
    ("Reinos akan y colonización francesa",
     "El territorio fue hogar de reinos y jefaturas akan (como el Baulé) y otros pueblos como los senufo y dioula en el norte, con intensas redes comerciales transaharianas; Francia estableció su colonia a finales del siglo XIX, integrándola en el África Occidental Francesa como colonia agrícola de plantación (café, cacao, madera)."),
    ("El «milagro» de Houphouët-Boigny",
     "Félix Houphouët-Boigny, líder independentista convertido en primer presidente en 1960, gobernó hasta su muerte en 1993 con un modelo de estabilidad política, apertura a la inversión francesa y desarrollo agrícola exportador (cacao, del que Costa de Marfil es hoy el mayor productor mundial) que convirtió al país en uno de los más prósperos de la región, atrayendo a millones de trabajadores migrantes de países vecinos."),
    ("La crisis de la «ivoirité» y las guerras civiles",
     "Tras la muerte de Houphouët-Boigny, la disputa por su sucesión reavivó tensiones entre el sur cristiano-animista y el norte musulmán, agravadas por el concepto político de «ivoirité» que cuestionaba la nacionalidad de ciudadanos de origen extranjero (muchos del norte); el país se dividió de facto tras un intento de golpe en 2002, y vivió una segunda guerra civil en 2010-2011 tras una disputada elección presidencial, resuelta con la intervención de fuerzas francesas y de la ONU."),
    ("Situación actual: recuperación económica y estabilidad bajo Ouattara",
     "Desde 2011, bajo la presidencia de Alassane Ouattara, Costa de Marfil ha experimentado una notable recuperación económica, con Abiyán consolidada como uno de los grandes centros financieros y logísticos del África Occidental francófona, aunque persisten tensiones políticas en torno a la duración de los mandatos presidenciales y la reconciliación nacional tras el conflicto."),
]

HISTORIA_FUENTES = [
    ("BBC News · Ivory Coast country profile", "https://www.bbc.com/news/world-africa-13287585"),
    ("Encyclopaedia Britannica · Côte d'Ivoire, History", "https://www.britannica.com/place/Ivory-Coast/History"),
    ("International Crisis Group · Côte d'Ivoire", "https://www.crisisgroup.org/africa/west-africa/cote-divoire"),
]

SPEC = dict(
    slug="costa-de-marfil", name="Costa de Marfil", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Danané/Loguatuo (desde Liberia)"),
        ("SALIDA", "Noé/Elubo (hacia Ghana)"),
        ("SEGURIDAD", "estable en el sur · precaución en el norte"),
        ("FRONTERA TERRESTRE", "operativa en ambos extremos"),
        ("VISADO", "visado previo obligatorio (~140 €)"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[6.3, -5.5], zoom=7,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Costa de Marfil se recorre de oeste a este: entrada montañosa por Man, capital política en Yamoussoukro, "
                   "patrimonio colonial en Grand-Bassam y Abidjan como gran base logística antes de cruzar a Ghana por Noé/Elubo, el paso más transitado de la subregión."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Liberia."),
        ("Entrada", "Danané/Loguatuo desde Ganta (Liberia)."),
        ("Salida", "Noé → Elubo (Ghana): paso principal, carretera en buen estado."),
        ("Visado", "Visado previo obligatorio para pasaporte español (~140 €, multientrada hasta 3 meses); certificado de fiebre amarilla exigido."),
        ("Seguridad", "Estable en el sur; precaución reforzada en el extremo norte, fuera de la ruta prevista."),
        ("Comunicaciones", "Starlink recién autorizado (jul. 2026): confirmar activación real; SIM local como base."),
    ],
    alerts=[
        "Visado previo obligatorio y de trámite relativamente costoso (~140 €): iniciar el proceso con margen suficiente antes del viaje.",
        "Extremo norte del país: mantener precaución reforzada y no desviarse de la ruta prevista por el sur/centro.",
        "Certificado de fiebre amarilla exigido y verificado habitualmente en frontera.",
    ],
    ruta_intro="Tramo de oeste a este por el centro y sur del país.",
    route_rows=[
        ("Entrada y montaña", "Danané → Man", "Aclimatación tras Liberia; clima más fresco"),
        ("Capital política", "Man → Yamoussoukro", "Basílica y provisiones en ruta hacia la costa"),
        ("Costa y capital económica", "Yamoussoukro → Abidjan → Grand-Bassam", "Base logística mayor y patrimonio colonial"),
        ("Hacia Ghana", "Abidjan → Noé/Elubo", "Paso fronterizo más transitado de la subregión"),
    ],
    offroad=[
        "Entorno de Man (Dents de Man, cascadas): pistas secundarias de montaña, transitables en 4x4 fuera de la temporada de lluvias más intensa.",
    ],
    acampada=[
        "Grand-Bassam: alojamientos con parking junto a la playa, opción más práctica que la acampada libre por la afluencia turística de la zona.",
        "Abidjan: aparcamiento vigilado recomendado por la densidad urbana y el tráfico.",
    ],
    visado=[
        "Visado previo obligatorio para pasaporte español: solicitud online con copia de pasaporte, itinerario y alojamiento; coste aproximado 140 €, resolución en ~2 días laborables.",
        "Certificado internacional de fiebre amarilla obligatorio, habitualmente verificado en frontera.",
    ],
    fronteras_rows=[
        ("Entrada", "Danané/Loguatuo (Liberia)", "Continuación desde Ganta; confirmar estado de la vía en lluvias."),
        ("Salida", "Noé → Elubo (Ghana)", "Paso principal y más transitado; carretera pavimentada en buen estado, horario 06:00-18:00."),
    ],
    vehiculos=[
        "CPD o laissez-passer temporal en frontera; Carte Brune (CEDEAO) válida como seguro regional.",
        "Llevar copias impresas de toda la documentación de ambos vehículos para los controles internos.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa a la ANAC antes de introducir o volar el dron.",
        "Evitar sobrevolar Abidjan, Yamoussoukro y edificios gubernamentales sin permiso expreso.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Revisar el mapa oficial 30-60 días antes de entrar: el servicio se autorizó en julio de 2026 y puede seguir en despliegue.",
        "SIM local (Orange, MTN, Moov) como conectividad principal mientras se confirma la cobertura Starlink real.",
    ],
    perro_intro=[
        "Sin normativa pública detallada localizada para Costa de Marfil: aplicar pasaporte UE de mascota, microchip y certificado antirrábico vigente, y confirmar por escrito antes de viajar.",
        "Llevar certificado sanitario reciente para el control fronterizo de Danané.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado obligatorio para entrar, habitualmente verificado.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "Seguro con evacuación médica: Abidjan concentra la mejor capacidad hospitalaria de la subregión.",
    ],
    seguridad_intro="El sur y el centro del país son estables; el extremo norte requiere precaución reforzada y queda fuera de la ruta prevista.",
    seguridad=[
        "No desviarse hacia el extremo norte del país.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
        "Revisar el aviso de Exteriores 72 h antes de entrar.",
    ],
    agua=[
        "Agua embotellada ampliamente disponible en Man, Yamoussoukro, Abidjan y Grand-Bassam; sin problema de suministro en este tramo.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): hoteles y estaciones de servicio Total/Shell de Man, Yamoussoukro y Abidjan aceptan llenar bidones/depósito con manguera sin problema; confirmar precio o donativo en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km: Danané → Man (~100 km) → Yamoussoukro (~300 km) → Abidjan (~240 km) → Elubo (~120 km vía Grand-Bassam), todos con estaciones formales de buena calidad.",
        "Red Total/Ola Energy/Vivo densa en todo el eje; es el tramo con mejor infraestructura de combustible desde Marruecos.",
    ],
    pendientes=[
        ("Visado", "Iniciar la solicitud previa con margen suficiente por su coste y trámite"),
        ("Starlink", "Confirmar activación real de cobertura 30-60 días antes"),
        ("Dron", "Resolver autorización con la ANAC o excluirlo del país"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Policía 111 · Bomberos 180 · Ambulancia 185 (verificar localmente). Emergencia consular española (Abidjan): +225 22 44 48 50.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

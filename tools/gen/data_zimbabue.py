# -*- coding: utf-8 -*-
"""Zimbabue — ficha completa (9 sep 2026): alternativa interior con las Cataratas Victoria."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Cataratas Victoria (Mosi-oa-Tunya)", cat="Naturaleza", prio="Alta", dog="no recomendado", time="2 noches",
         lat=-17.9243, lon=25.8572,
         desc="Una de las Siete Maravillas Naturales del Mundo y Patrimonio de la Humanidad compartido con Zambia: 1,7 km de frente de agua cayendo hasta 108 m, con el mejor mirador del lado zimbabuense (Parque Nacional de las Cataratas Victoria).",
         credit="Bernard Gagnon · CC BY-SA 4.0", source=W + "Victoria%20Falls%2C%20Zimbabwe%2001.jpg?width=900"),
    dict(n=2, name="Gran Zimbabue (ruinas)", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-20.2667, lon=30.9333,
         desc="La mayor construcción de piedra prehispánica del África subsahariana, capital de un reino comercial medieval que dio nombre al país moderno; Patrimonio de la Humanidad y referencia arqueológica de primer orden.",
         credit="Trinapee · CC BY-SA 4.0", source=W + "Great%20Zimbabwe%20Ruins.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "cultura": "morado"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Kazungula (con Botsuana/Zambia)", "Frontera", -17.7833, 25.2667,
     "Punto cuádruple donde convergen Zimbabue, Zambia, Botsuana y (a poca distancia) Namibia; puente nuevo sobre el Zambeze que agiliza el tránsito de vehículos."),
    ("Frontera · Beitbridge (con Sudáfrica)", "Frontera", -22.2167, 30.0000,
     "Cruce terrestre más transitado del país, a menudo congestionado por tráfico comercial; prever tiempo de espera adicional."),
    ("Embajada de España en Harare", "Consular", -17.8100, 31.0500,
     "16 Phillips Ave., Belgravia, P.O. Box 3300, Harare. Tel. +263 (0)242 250740/1 · Emergencia consular: +263 (0)772 436 620 · emb.harare@maec.es. También competente para Malaui y Zambia."),
    ("Victoria Falls Hospital / Mater Dei Hospital (Bulawayo)", "Hospital", -17.9300, 25.8300,
     "Clínicas privadas de referencia en la zona turística de Cataratas Victoria; para necesidades serias, evacuación hacia Sudáfrica es la opción más fiable."),
    ("Combustible · Victoria Falls / Bulawayo / Masvingo", "Combustible", -17.9243, 25.8572,
     "Estaciones formales en las ciudades del eje turístico; la disponibilidad de combustible en Zimbabue ha sido históricamente irregular — llevar reserva y pagar preferentemente en USD."),
    ("Agua potable y de uso general · Victoria Falls", "Agua potable", -17.9243, 25.8572,
     "Agua embotellada sin problema en la zona turística; hoteles y lodges permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria de la CAAZ",
                  "Zimbabue exige registro y autorización previa de la Civil Aviation Authority of Zimbabwe (CAAZ) para el uso de drones, con un trámite que conviene iniciar con antelación; el entorno de las Cataratas Victoria tiene además restricciones específicas por tráfico aéreo turístico (helicópteros, avionetas).")

STARLINK_CALLOUT = ("warn", "Coming en 2026, no plenamente activo",
                     "Starlink ha avanzado en su proceso de licencia en Zimbabue pero no está confirmado como plenamente activo y estable a la fecha de esta revisión. Tratar con precaución y llevar SIM local (Econet, NetOne) como respaldo garantizado.")

DOG_MATRIX = [
    ("Cataratas Victoria (parque nacional)", "no recomendado", "Normativa del parque y afluencia turística desaconsejan llevar mascota; dejar en el hotel durante la visita."),
    ("Gran Zimbabue, Bulawayo", "permitido con condiciones", "Correa y sombra; clima templado de altiplano."),
]

SOURCES = [
    ("thingstodoinzimbabwe.com · requisitos de entrada 2026", "https://thingstodoinzimbabwe.com/entry-requirements/"),
    ("Embajada de España en Harare · contacto", "https://www.exteriores.gob.es/Embajadas/harare/es/Embajada/Paginas/Horario.aspx"),
    ("UNESCO · Cataratas Victoria (Mosi-oa-Tunya), Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/509/"),
    ("UNESCO · Gran Zimbabue, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/364/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
]

CORRIDOR = [(-17.7833, 25.2667), (-17.9243, 25.8572), (-20.2667, 30.9333), (-22.2167, 30.0000)]

HISTORIA_RESUMEN = ("Zimbabue toma su nombre del Gran Zimbabue, capital de piedra de un poderoso reino comercial medieval; la colonización británica bajo Cecil Rhodes dio paso a la minoría blanca de Rodesia, "
                     "a una guerra de independencia que trajo el país moderno en 1980 bajo Robert Mugabe, y a décadas de crisis económica y política que aún condicionan al país, aunque el eje turístico de las Cataratas Victoria se mantiene estable.")

HISTORIA_SECCIONES = [
    ("El Gran Zimbabue y los reinos de piedra",
     "Entre los siglos XI y XV, el reino de Zimbabue (y sus sucesores, como el imperio de Mutapa) construyó Gran Zimbabue, una ciudad de piedra sin argamasa con muros de hasta 11 metros, capital de una red comercial que llegaba hasta la costa swahili e incluso China, "
     "intercambiando oro y marfil por porcelana y cuentas de vidrio. Su nombre —«casas de piedra» en shona— dio origen al del país moderno."),
    ("Colonización y Rodesia",
     "La Compañía Británica de Sudáfrica de Cecil Rhodes ocupó el territorio en la década de 1890, dando lugar a la colonia de Rodesia del Sur, con una minoría blanca que acaparó las mejores tierras agrícolas. "
     "En 1965, el gobierno blanco minoritario declaró unilateralmente la independencia de Rodesia para evitar el traspaso de poder a la mayoría negra, lo que provocó sanciones internacionales y una guerra de guerrillas de casi 15 años."),
    ("Independencia y la era de Mugabe",
     "La guerra de independencia terminó con los acuerdos de Lancaster House de 1979, y en 1980 nació Zimbabue como república bajo Robert Mugabe, inicialmente celebrado como líder de la liberación. "
     "Mugabe gobernó durante 37 años, con una controvertida reforma agraria en los años 2000 que expropió tierras de granjeros blancos y contribuyó a un colapso económico con una de las hiperinflaciones más extremas de la historia moderna."),
    ("Situación actual: crisis económica persistente",
     "Un golpe militar depuso a Mugabe en 2017, pero la crisis económica y la escasez de divisas y combustible han persistido bajo sus sucesores, con el dólar estadounidense circulando de facto junto a la moneda local. "
     "Pese a ello, el eje turístico de las Cataratas Victoria y Gran Zimbabue se mantiene como una de las alternativas más atractivas y manejables del corredor de regreso para este proyecto."),
]

HISTORIA_FUENTES = [
    ("BBC News · Zimbabwe country profile", "https://www.bbc.com/news/world-africa-14113618"),
    ("Encyclopaedia Britannica · Zimbabwe, History", "https://www.britannica.com/place/Zimbabwe/History"),
    ("UNESCO · Gran Zimbabue", "https://whc.unesco.org/en/list/364/"),
]

SPEC = dict(
    slug="zimbabue", name="Zimbabue", revision="9 sep 2026",
    sub="Alternativa interior · Cataratas Victoria si se ajusta el regreso",
    chips=[
        ("ROL EN LA RUTA", "opcional — alternativa interior con Cataratas Victoria"),
        ("ENTRADA/SALIDA", "Kazungula (Botsuana/Zambia) o Beitbridge (Sudáfrica)"),
        ("SEGURIDAD", "estable · precaución económica"),
        ("COMUNICACIONES", "Starlink llegando, no plenamente activo"),
    ],
    center=[-19.0, 29.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, si finalmente se incluye este desvío.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    facts=[
        ("Rol en la ruta", "Alternativa interior con las Cataratas Victoria, si se ajusta el itinerario del corredor de regreso."),
        ("Entrada/salida", "Kazungula desde Botsuana/Zambia, o Beitbridge desde Sudáfrica."),
        ("Seguridad", "País estable en el eje turístico; precaución económica por la irregularidad del suministro de combustible y divisas."),
        ("Visado", "Visa on arrival disponible — verificar tarifas y validez 30-60 días antes."),
    ],
    alerts=[
        "Combustible: suministro históricamente irregular fuera de las grandes ciudades; llevar reserva y pagar preferentemente en USD en efectivo.",
        "Beitbridge: frontera con congestión habitual por tráfico comercial pesado; prever tiempo de espera adicional.",
        "Confirmar 30-60 días antes la tarifa exacta de la visa on arrival, que ha variado en los últimos años.",
    ],
    ruta_intro="Entrada por Kazungula o Beitbridge, con las Cataratas Victoria como eje principal del desvío y una parada cultural en Gran Zimbabue de camino hacia el resto del itinerario.",
    route_rows=[
        ("Entrada y cataratas", "Kazungula → Cataratas Victoria", "2 noches; mejor mirador del lado zimbabuense"),
        ("Cultura", "Cataratas Victoria → Gran Zimbabue", "Ruinas de piedra, Patrimonio de la Humanidad"),
        ("Salida", "Gran Zimbabue → Beitbridge", "Reincorporación hacia Sudáfrica o Mozambique"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: el eje Kazungula-Cataratas Victoria-Gran Zimbabue-Beitbridge es carretera asfaltada, con baches ocasionales fuera de las rutas principales.",
    ],
    acampada=[
        "Victoria Falls (ciudad): amplia oferta de campings y lodges orientados a overlanders, con aparcamiento vigilado.",
        "Gran Zimbabue: campamento junto al yacimiento arqueológico, sencillo pero funcional.",
    ],
    visado=[
        "Visa on arrival disponible para españoles; confirmar tarifa exacta 30-60 días antes (ha variado en los últimos años).",
        "KAZA Univisa como alternativa si se combina con Zambia: un único visado válido para movimientos entre ambos países durante 30 días.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica.",
    ],
    fronteras_rows=[
        ("Entrada/salida (norte)", "Kazungula (Botsuana/Zambia)", "Punto cuádruple; puente nuevo sobre el Zambeze."),
        ("Entrada/salida (sur)", "Beitbridge (Sudáfrica)", "Cruce más transitado del país; congestión habitual."),
    ],
    vehiculos=[
        "CPD recomendado — verificar si se exige o si basta un permiso temporal según el punto de entrada.",
        "KAZA Univisa no cubre el vehículo, solo a las personas: gestionar el papeleo del vehículo por separado en cada frontera.",
        "Seguro de terceros SADC/COMESA válido en Zimbabue como miembro de ambas organizaciones.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Registrar el dron y tramitar autorización ante la CAAZ con antelación.",
        "Restricciones específicas de tráfico aéreo turístico en el entorno de las Cataratas Victoria (helicópteros, avionetas) — confirmar zona de exclusión antes de volar.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "En proceso de licencia, no plenamente activo y estable a la fecha de esta revisión: tratar con precaución.",
        "SIM local (Econet, NetOne) como respaldo garantizado en todo el itinerario.",
    ],
    perro_intro=[
        "Certificado veterinario internacional y vacuna antirrábica en vigor, exigibles en frontera.",
        "No recomendado en el Parque Nacional de las Cataratas Victoria; dejar en el hotel durante la visita.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en la zona de las Cataratas Victoria y el valle del Zambeze: profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Clínicas privadas de Victoria Falls y Bulawayo como referencia; para casos serios, evacuación hacia Sudáfrica es la opción real.",
    ],
    seguridad_intro="El eje turístico de las Cataratas Victoria y Gran Zimbabue es manejable y estable; el principal factor a gestionar es la irregularidad económica (combustible, divisas), no la seguridad ciudadana.",
    seguridad=[
        "Llevar efectivo en USD para imprevistos, dada la inestabilidad de la moneda local.",
        "Repostar siempre que se vea oferta fiable, sin esperar a necesitarlo con urgencia.",
        "Precaución normal de viaje en el resto del itinerario.",
    ],
    agua=[
        "Victoria Falls (ciudad): agua embotellada sin problema en la zona turística.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): hoteles y lodges de Victoria Falls y el campamento de Gran Zimbabue permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Suministro históricamente irregular fuera de Victoria Falls, Bulawayo y Masvingo: llevar reserva en jerricán y repostar siempre que se vea oferta fiable.",
        "Pago preferente en USD en efectivo; tarjetas y moneda local pueden no ser aceptadas o generar recargos.",
    ],
    pendientes=[
        ("Decisión de incluir el desvío", "Confirmar si se ajusta el calendario del corredor de regreso para incluir Zimbabue"),
        ("Visado", "Confirmar tarifa exacta de la visa on arrival o valorar el KAZA Univisa combinado con Zambia"),
        ("Combustible", "Prever reserva adicional dada la irregularidad histórica del suministro"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Zimbabue es un desvío opcional: confirmar si se incluye antes de revalidar el resto de trámites.",
    emergency="Emergencia consular española (Harare): +263 (0)772 436 620 · Embajada de España en Harare: +263 (0)242 250740/1.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

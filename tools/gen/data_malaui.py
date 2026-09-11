# -*- coding: utf-8 -*-
"""Malaui — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Zomba y su meseta", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-15.3833, lon=35.3167,
         desc="Antigua capital colonial a los pies de una meseta boscosa de más de 1.800 m, con miradores, cascadas y aire fresco tras el calor del corredor de Tete; buena base de descanso nada más entrar desde Mozambique.",
         credit="Dr. Ferdinand Groeger · CC BY-SA 3.0", source=W + "Zomba%20Plateau.jpg?width=900"),
    dict(n=2, name="Parque Nacional de Liwonde", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 noches",
         lat=-14.8333, lon=35.3167,
         desc="Uno de los grandes proyectos de recuperación de fauna del país junto al río Shire: elefantes, rinocerontes negros reintroducidos y una de las mejores densidades de aves de la región; safaris en vehículo o barco.",
         credit="Brian Dell · dominio público", source=W + "Elephants%20in%20Liwonde%20National%20Park.JPG?width=900"),
    dict(n=3, name="Lago Malaui — Cabo Maclear", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-14.0206, lon=34.8306,
         desc="El gran eje del país: tercer lago más grande de África, con playas de agua dulce, cientos de especies endémicas de cíclidos y el Parque Nacional del Lago Malaui (UNESCO) frente a la costa de Cabo Maclear.",
         credit="Hans Hillewaert · CC BY-SA 4.0", source=W + "Otter%20Point%2C%20Cape%20Maclear%20(Malawi).jpg?width=900"),
    dict(n=4, name="Lilongwe", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-13.9626, lon=33.7741,
         desc="Capital administrativa del país, con la mayor oferta de talleres, recambios y supermercados del tramo; base logística antes de continuar hacia el norte y la frontera de Songwe con Tanzania.",
         credit="NASA Astronauts · dominio público", source=W + "Lilongwe%2C%20Malawi.JPG?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Zóbuè/Mwanza (desde Mozambique)", "Frontera", -16.1167, 33.0500,
     "Cruce del corredor de Tete; carretera asfaltada, controles rutinarios sin incidencias reportadas."),
    ("Frontera · Salida — Songwe (hacia Tanzania)", "Frontera", -9.3833, 33.7167,
     "Puente sobre el río Songwe, al norte de Karonga; cruce estándar hacia Mbeya (Tanzania), con puesto integrado a ambos lados."),
    ("Consulado Honorario de España en Lilongwe", "Consular", -13.9626, 33.7741,
     "María Ángeles Soriano, Blantyre Street 279, Area 10, Lilongüe. Tel./WhatsApp (+265) 999 846 081. Depende de la Embajada de España en Harare (Zimbabue), que también cubre Zambia."),
    ("Embajada de España en Harare (competente para Malaui)", "Consular", -17.8292, 31.0522,
     "16 Phillips Ave., Belgravia, P.O. Box 3300, Harare (Zimbabue). Tel. +263 (0)242 250740/1 · Emergencia consular: +263 (0)772 436 620. Referencia diplomática de Malaui y Zambia; contactar directamente el consulado honorario de Lilongüe para gestiones ordinarias y solo Harare para trámites mayores."),
    ("Hospital Kamuzu Central, Lilongwe", "Hospital", -13.9553, 33.7614,
     "Principal hospital de referencia de la capital; mejor opción sanitaria del tramo junto con clínicas privadas de Blantyre."),
    ("Combustible · Zomba / Blantyre / Lilongwe", "Combustible", -15.3833, 35.3333,
     "Estaciones formales (Puma, Total, OilCom) en las principales ciudades del corredor sur-norte; sin gap relevante de 500 km en el eje previsto."),
    ("Agua potable y de uso general · Lilongwe y Cabo Maclear", "Agua potable", -13.9626, 33.7741,
     "Agua embotellada en supermercados de Lilongwe y Blantyre; lodges y campings de Cabo Maclear y Liwonde permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria ante la Autoridad de Aviación Civil de Malaui",
                  "Malaui exige registro y autorización previa del Departamento de Aviación Civil para el uso de drones, incluido el uso recreativo con cámara; el trámite puede llevar varias semanas. Norma prudente del proyecto: solicitar el permiso con antelación suficiente y no volar sobre los parques nacionales (Liwonde, Lago Malaui) sin autorización específica del área protegida.")

STARLINK_CALLOUT = ("ok", "Disponible y operativo en 2026",
                     "Starlink está activo comercialmente en Malaui, con cobertura confirmada en el corredor Zomba-Blantyre-Lilongwe y en la costa del Lago Malaui; kit y suscripción configurables antes de entrar al país.")

DOG_MATRIX = [
    ("Parque Nacional de Liwonde", "prohibido", "No se permite el acceso de mascotas a las zonas de fauna del parque; dejar con cuidador en la entrada."),
    ("Zomba, Cabo Maclear, Lilongwe", "permitido con condiciones", "Correa y sombra; buen clima en la meseta de Zomba, más calor en la costa del lago."),
]

SOURCES = [
    ("Embajada de España en Harare · Malaui (consulado honorario de Lilongüe)", "https://www.exteriores.gob.es/Embajadas/harare/es/Embajada/tambien-somos-tu-embajada-en/Paginas/Malawi.aspx"),
    ("thingstodoinmalawi.com · requisitos de visado/eVisa para Malaui", "https://thingstodoinmalawi.com/entry-requirements/"),
    ("Bordercrossinghub.com · cruce de Mwanza/Zóbuè", "https://bordercrossinghub.com/mwanza-zobue-border-crossing/"),
    ("Tracks4Africa Blog · Carnet de Passage en el sur de África", "https://blog.tracks4africa.co.za/2888-2/"),
    ("PetTravel.com · requisitos de importación de mascotas a Malaui", "https://www.pettravel.com/information/pet-passports/malawi-pet-import-requirements/"),
    ("connectingafrica.com · lanzamiento de Starlink en Malaui", "https://www.connectingafrica.com/broadband/spacex-s-starlink-launches-in-malawi"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(-16.1167, 33.0500), (-15.3833, 35.3167), (-14.8333, 35.3167), (-14.0206, 34.8306), (-13.9626, 33.7741), (-9.3833, 33.7167)]

HISTORIA_RESUMEN = ("Malaui creció alrededor del gran lago que le da nombre, cruce de rutas de comercio y de la trata de esclavos árabe-swahili hasta que el misionero David Livingstone impulsó su freno; "
                     "convertido en el protectorado británico de Niasalandia, alcanzó la independencia en 1964 bajo Hastings Banda, cuyo régimen autoritario de partido único duró tres décadas, y hoy es uno de los países más estables y tranquilos del corredor de regreso.")

HISTORIA_SECCIONES = [
    ("El lago y las rutas de comercio",
     "El lago Malaui, tercero más grande de África, ha sido durante siglos el eje de la vida de los pueblos chewa, yao y ngoni que se asentaron en sus orillas. "
     "En el siglo XIX, mercaderes árabe-swahilis remontaron el lago desde la costa mozambiqueña y tanzana para comerciar con marfil y personas esclavizadas, convirtiendo la región en uno de los últimos grandes escenarios de la trata de esclavos en el interior de África oriental."),
    ("Livingstone y el protectorado británico",
     "El misionero y explorador escocés David Livingstone llegó al lago en 1859 y dedicó buena parte de su carrera a denunciar la trata de esclavos en la región, lo que impulsó la presencia misionera y comercial británica posterior. "
     "En 1891 el territorio se convirtió en el protectorado británico de Niasalandia (British Central Africa, luego Nyasaland), integrado entre 1953 y 1963 en la Federación de Rodesia y Niasalandia junto a las actuales Zimbabue y Zambia, una unión impuesta y resistida por la población africana."),
    ("Independencia y la era de Hastings Banda",
     "Malaui alcanzó la independencia en 1964 bajo el liderazgo de Hastings Kamuzu Banda, quien gobernó como presidente vitalicio de partido único hasta 1994, con un régimen autoritario de censura estricta y culto a la personalidad, "
     "pero también de relativa estabilidad y ausencia de los conflictos armados que sacudieron a varios de sus vecinos en esas décadas. La transición a un sistema multipartidista llegó en 1994 tras un referéndum."),
    ("Situación actual: uno de los tramos más tranquilos de la ruta",
     "Desde los años 90, Malaui ha mantenido un sistema democrático con alternancia de poder, sin conflictos armados ni insurgencias activas en su territorio, aunque continúa siendo uno de los países más pobres del mundo. "
     "Para este viaje, ese contexto se traduce en un tramo sin zonas excluidas: el itinerario Zóbuè-Zomba-Liwonde-Cabo Maclear-Lilongwe-Songwe se recorre con precaución normal de viaje, sin las alertas de seguridad que condicionan a varios de sus vecinos."),
]

HISTORIA_FUENTES = [
    ("BBC News · Malawi country profile", "https://www.bbc.com/news/world-africa-13864367"),
    ("Encyclopaedia Britannica · Malawi, History", "https://www.britannica.com/place/Malawi/History"),
    ("UNESCO · Lago Malaui, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/289/"),
]

SPEC = dict(
    slug="malaui", name="Malaui", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Zóbuè/Mwanza (desde Mozambique)"),
        ("SALIDA", "Songwe (hacia Tanzania)"),
        ("SEGURIDAD", "estable — sin exclusiones de ruta"),
        ("VISADO", "eVisa — verificar exención antes de viajar"),
        ("COMUNICACIONES", "Starlink activo (ok)"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[-14.0, 34.3], zoom=7,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    facts=[
        ("Ventana prevista", "Segundo país del corredor de regreso, tras Mozambique."),
        ("Entrada", "Zóbuè/Mwanza desde Mozambique, por el corredor de Tete."),
        ("Salida", "Songwe hacia Tanzania, al norte de Karonga."),
        ("Seguridad", "País estable, sin zonas excluidas del itinerario; el Lago Malaui es el eje del tramo."),
        ("Visado", "eVisa (evisa.gov.mw) obligatoria para españoles — no exentos; tramitar con 5-10 días laborables de antelación."),
        ("Vehículo", "CPD recomendado; verificar si se admite permiso temporal alternativo en frontera."),
    ],
    alerts=[
        "Visado: España NO está exenta — tramitar el eVisa en evisa.gov.mw antes de llegar a la frontera, no confiar en visado a la llegada.",
        "Perro prohibido en el Parque Nacional de Liwonde: prever cuidador en la entrada o rotación del itinerario.",
        "Sin alertas de seguridad activas en el corredor previsto a fecha de esta revisión; reconfirmar igualmente 30-60 días antes.",
    ],
    ruta_intro="Entrada por el corredor de Tete hacia la meseta de Zomba, descenso al Parque de Liwonde, ascenso a la costa del Lago Malaui en Cabo Maclear y paso por Lilongwe antes de salir hacia Tanzania por Songwe.",
    route_rows=[
        ("Entrada y meseta", "Zóbuè/Mwanza → Zomba", "Aire fresco de meseta tras el calor de Tete; descanso"),
        ("Fauna", "Zomba → Liwonde NP", "Safaris en vehículo o barco por el río Shire"),
        ("Lago", "Liwonde → Cabo Maclear", "Playas de agua dulce del Lago Malaui; 2 noches recomendadas"),
        ("Capital y salida", "Cabo Maclear → Lilongwe → Songwe", "Base logística final antes de Tanzania"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: el eje Zóbuè-Zomba-Liwonde-Cabo Maclear-Lilongwe-Songwe es carretera asfaltada en su mayor parte, con pistas de tierra en buen estado dentro de Liwonde.",
    ],
    acampada=[
        "Cabo Maclear: campings y lodges de playa con aparcamiento, muy orientados a overlanders y mochileros.",
        "Liwonde: campamentos dentro y en la entrada del parque, con opción de safari nocturno.",
        "Zomba y Lilongwe: hoteles y campings urbanos sin incidencias reportadas.",
    ],
    visado=[
        "eVisa obligatoria para ciudadanos españoles (evisa.gov.mw), aproximadamente 75 USD, 5-10 días laborables de tramitación, válida 30 días de entrada única.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica.",
        "Confirmar 30-60 días antes si existe alguna vía de exención o visado a la llegada que haya cambiado desde esta revisión.",
    ],
    fronteras_rows=[
        ("Entrada", "Zóbuè/Mwanza (Mozambique)", "Corredor de Tete; carretera asfaltada, controles rutinarios."),
        ("Salida", "Songwe (Tanzania)", "Puente sobre el río Songwe, al norte de Karonga; puesto integrado."),
    ],
    vehiculos=[
        "CPD recomendado — verificar si Malaui admite alternativa de permiso temporal en frontera para vehículos de turismo.",
        "Seguro de terceros (COMESA) obligatorio, comprado en la frontera de entrada.",
        "Carnet de conducir internacional recomendado en todos los controles.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa ante el Departamento de Aviación Civil de Malaui, con margen de varias semanas.",
        "No volar sobre Liwonde ni la costa del Lago Malaui sin autorización específica del área protegida.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo y operativo en 2026 en el corredor Zomba-Blantyre-Lilongwe y en la costa del Lago Malaui.",
        "SIM local (TNM, Airtel Malawi) como respaldo en zonas rurales sin cobertura satelital directa.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente y vacuna antirrábica en vigor, exigibles en frontera.",
        "Perro prohibido en el Parque Nacional de Liwonde; prever cuidador en la entrada o dejarlo en Zomba/Cabo Maclear durante la visita.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en todo el territorio, especialmente en la costa del lago: profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Hospital Kamuzu Central (Lilongwe) como mejor referencia sanitaria; seguro con evacuación médica real imprescindible fuera de la capital.",
    ],
    seguridad_intro="Malaui es uno de los tramos más tranquilos del corredor de regreso: sin zonas excluidas ni alertas activas, con precaución normal de viaje suficiente en todo el itinerario.",
    seguridad=[
        "Precaución normal de viaje; sin zonas del itinerario que requieran exclusión o revalidación especial.",
        "Aparcamiento vigilado en Lilongwe y Blantyre por prudencia estándar, sin incidencia reportada relevante.",
        "Carreteras secundarias de la meseta de Zomba pueden tener baches tras las lluvias: circular con luz de día.",
    ],
    agua=[
        "Lilongwe y Blantyre: agua embotellada sin problema en supermercados.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): lodges y campings de Cabo Maclear, Liwonde, Zomba y Lilongwe permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje previsto: Zóbuè → Zomba (~90 km) → Liwonde (~50 km) → Cabo Maclear (~110 km) → Lilongwe (~250 km) → Songwe (~470 km), todos con estaciones formales.",
        "Zomba, Blantyre y Lilongwe concentran la mejor oferta y calidad del país (Puma, Total, OilCom); repostar a fondo antes del tramo final hacia Songwe.",
    ],
    pendientes=[
        ("Visado", "Tramitar el eVisa en evisa.gov.mw con margen suficiente"),
        ("Vehículo", "Confirmar si se admite permiso temporal alternativo al CPD en frontera"),
        ("Perro", "Confirmar cuidador en Liwonde durante la visita al parque"),
        ("Dron", "Iniciar trámite de autorización ante el Departamento de Aviación Civil con semanas de antelación"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Consulado Honorario de España en Lilongüe: (+265) 999 846 081 · Embajada de España en Harare (competente para Malaui), emergencia consular: +263 (0)772 436 620.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

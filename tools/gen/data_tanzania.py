# -*- coding: utf-8 -*-
"""Tanzania — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Cráter del Ngorongoro", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 noches",
         lat=-3.2000, lon=35.5000,
         desc="Caldera volcánica de 20 km de diámetro convertida en el mayor recinto natural de fauna cerrado de África: los «Big Five» conviven en un espacio de densidad excepcional. Área de Conservación gestionada junto a comunidades masái.",
         credit="Arnold Tibaijuka · CC BY-SA 4.0", source=W + "Wide%20aerial%20landscape%20of%20the%20Ngorongoro%20ecosystem.jpg?width=900"),
    dict(n=2, name="Arusha y el monte Meru", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-3.3869, lon=36.6830,
         desc="Capital logística del norte de safaris (Serengeti, Ngorongoro, Kilimanjaro, Manyara); mejor oferta de talleres, recambios y supermercados del tramo, y puerta de salida hacia Kenia por Namanga.",
         credit="Khalidsalewa · CC BY-SA 4.0", source=W + "Mount%20meru%20with%20snow%2C%20Arusha%20Region%2C%20Tanzania.jpg?width=900"),
    dict(n=3, name="Dar es Salaam", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-6.7924, lon=39.2083,
         desc="Antigua capital y mayor ciudad y puerto del país; desvío costero opcional desde el eje Mbeya-Arusha, con mejor infraestructura urbana y punto de embarque del ferry hacia Zanzíbar.",
         credit="Muhammad Mahdi Karim · GFDL", source=W + "Dar%20es%20Salaam%20City%20Skyline.jpg?width=900"),
    dict(n=4, name="Zanzíbar (Stone Town)", cat="Naturaleza", prio="Media", dog="no recomendado", time="2 noches",
         lat=-6.1659, lon=39.1917,
         desc="Ciudad histórica swahili-omaní (UNESCO) en la isla de Unguja, accesible en ferry desde Dar es Salaam; casco antiguo, mercados de especias y playas del archipiélago como desvío costero opcional del corredor.",
         credit="Kgbo · CC BY-SA 4.0", source=W + "Stone%20Town%2C%20Zanzibar%2C%202021%2C%2036.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Songwe (desde Malaui)", "Frontera", -9.3833, 33.7167,
     "Puente sobre el río Songwe, al norte de Karonga; cruce estándar hacia Mbeya, con puesto integrado a ambos lados."),
    ("Frontera · Salida — Namanga (hacia Kenia)", "Frontera", -2.5450, 36.7867,
     "Paso principal del corredor norte, junto al Parque de Amboseli; puesto de alto tránsito turístico bien equipado."),
    ("Embajada de España en Dar es Salaam", "Consular", -6.7900, 39.2600,
     "99 B Kinondoni Road, P.O. Box 842, Dar es Salaam. Tel. (+255) 022 266 60 18/19 · Emergencia consular 24h: (+255) 754 04 21 23 · emb.daressalaam@maec.es."),
    ("Muhimbili National Hospital, Dar es Salaam", "Hospital", -6.8083, 39.2764,
     "Principal hospital de referencia del país; mejor opción sanitaria del tramo costero junto con clínicas privadas de Arusha."),
    ("Combustible · Mbeya / Iringa / Arusha", "Combustible", -3.3869, 36.6830,
     "Estaciones formales (TotalEnergies, Puma, Oryx) en las ciudades principales del corredor Mbeya-Iringa-Arusha; sin gap relevante de 500 km en el eje previsto."),
    ("Agua potable y de uso general · Arusha y Dar es Salaam", "Agua potable", -3.3869, 36.6830,
     "Agua embotellada sin problema en supermercados de ambas ciudades; lodges de safari y campings del corredor Mbeya-Iringa-Arusha permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria de la TCAA, muy restrictiva en parques nacionales",
                  "Tanzania exige permiso previo de la Tanzania Civil Aviation Authority (TCAA) para cualquier vuelo de dron, y TANAPA (Parques Nacionales de Tanzania) añade un permiso adicional y de pago para volar dentro de sus áreas — incluidos el Ngorongoro y el Serengeti, donde en la práctica rara vez se autoriza a particulares. Norma prudente del proyecto: no volar dentro de áreas protegidas sin el permiso de TANAPA en mano, y tramitar el permiso TCAA con semanas de antelación para el resto del país.")

STARLINK_CALLOUT = ("warn", "Licencia solicitada, servicio aún no plenamente activo — tratar como en transición durante 2026",
                     "Starlink solicitó licencia en Tanzania a finales de 2024 y ha sido preseleccionada por la TCRA, con cobertura parcial ya operativa vía un acuerdo directo-a-dispositivo con Airtel Africa, pero sin servicio residencial pleno confirmado a la fecha de esta revisión. Tratar como no garantizado y llevar SIM local (Vodacom, Airtel Tanzania, Tigo) como conectividad principal; reconfirmar el estado 30-60 días antes del viaje.")

DOG_MATRIX = [
    ("Cráter del Ngorongoro y Serengeti", "prohibido", "No se permite el acceso de mascotas a las áreas de conservación y parques nacionales; dejar con cuidador en Arusha o Karatu."),
    ("Zanzíbar", "no recomendado", "Trayecto en ferry y calor húmedo intenso; sin infraestructura práctica para mascotas en la isla."),
    ("Arusha, Dar es Salaam, corredor Mbeya-Iringa", "permitido con condiciones", "Correa y sombra; calor elevado en la costa."),
]

SOURCES = [
    ("Embajada de España en Dar es Salaam · contacto", "https://www.exteriores.gob.es/Embajadas/daressalaam/en/Embajada/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx"),
    ("safarimasters.com · requisitos de visado/e-visa para Tanzania", "https://safarimasters.com/tanzania-entry-requirements/"),
    ("tech.africa · Starlink en África, estado por país 2026 (Tanzania: licencia en trámite, servicio parcial vía Airtel)", "https://tech.africa/starlink-africa/"),
    ("Space in Africa · solicitud de licencia de Starlink en Tanzania", "https://spaceinafrica.com/2024/11/16/starlink-applies-for-licenses-to-operate-in-tanzania/"),
    ("Overlanding Association · Carnet de Passage y permisos de vehículo por país", "https://overlandingassociation.org/carnet-de-passage/"),
    ("PetTravel.com · requisitos de importación de mascotas a Tanzania", "https://www.pettravel.com/information/pet-passports/tanzania-pet-import-requirements/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(-9.3833, 33.7167), (-3.3869, 36.6830), (-3.2000, 35.5000), (-6.7924, 39.2083), (-2.5450, 36.7867)]

HISTORIA_RESUMEN = ("Tanzania nace de la unión en 1964 de Tanganica y el sultanato de Zanzíbar, dos historias muy distintas — el interior bantú de la Ruta de la Seda del marfil y el emporio comercial swahili-omaní de la costa — "
                     "fusionadas bajo el liderazgo de Julius Nyerere y su particular experimento socialista africano (ujamaa); hoy es uno de los países más estables políticamente del continente, con la meseta del Serengeti y el Ngorongoro como epicentro mundial de la conservación de fauna.")

HISTORIA_SECCIONES = [
    ("La costa swahili y el sultanato de Zanzíbar",
     "Durante más de un milenio, la costa tanzana formó parte del mundo swahili, una civilización mestiza de comerciantes bantúes, árabes y persas que edificó ciudades-estado prósperas con el comercio de oro, marfil y esclavos hacia Oriente Medio e India. "
     "En el siglo XIX, el sultanato omaní trasladó su capital a Zanzíbar, convirtiendo la isla en el mayor mercado de esclavos y de clavo del Índico occidental, con Stone Town como su corazón administrativo y comercial — hoy Patrimonio de la Humanidad."),
    ("Colonización alemana y británica del interior",
     "El interior, poblado por más de cien grupos étnicos bantúes, nilóticos y cusitas, fue colonizado por Alemania a finales del siglo XIX como el África Oriental Alemana, con una represión especialmente dura durante la rebelión Maji Maji (1905-1907). "
     "Tras la Primera Guerra Mundial, el territorio pasó a administración británica como Tanganica, mientras Zanzíbar seguía siendo un protectorado británico aparte, con el sultanato local nominalmente en el trono."),
    ("Independencia, unión y el socialismo de Nyerere",
     "Tanganica se independizó en 1961 y Zanzíbar en 1963, pero una revolución popular derrocó al sultán de Zanzíbar apenas un mes después de su independencia. En 1964 ambos territorios se unieron para formar Tanzania, bajo el liderazgo de Julius Nyerere. "
     "Nyerere impulsó el ujamaa, un modelo de socialismo africano basado en aldeas comunales autosuficientes y en el suajili como lengua nacional unificadora — una política que, pese a sus fracasos económicos, dejó a Tanzania con una cohesión nacional y una estabilidad política poco comunes en la región."),
    ("Situación actual: estabilidad y capital mundial de los safaris",
     "Tanzania es hoy uno de los países más estables de África, sin conflictos armados internos activos, aunque mantiene tensiones políticas ocasionales en torno a procesos electorales en Zanzíbar. "
     "El país alberga algunos de los ecosistemas de fauna más importantes del planeta —el Serengeti, el cráter del Ngorongoro y el Kilimanjaro— convertidos en el eje económico y turístico del norte, y en el gran atractivo natural de este tramo del corredor de regreso."),
]

HISTORIA_FUENTES = [
    ("BBC News · Tanzania country profile", "https://www.bbc.com/news/world-africa-14095868"),
    ("Encyclopaedia Britannica · Tanzania, History", "https://www.britannica.com/place/Tanzania/History"),
    ("UNESCO · Stone Town de Zanzíbar, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/173/"),
    ("UNESCO · Área de Conservación de Ngorongoro, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/39/"),
]

SPEC = dict(
    slug="tanzania", name="Tanzania", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Songwe (desde Malaui)"),
        ("SALIDA", "Namanga (hacia Kenia)"),
        ("SEGURIDAD", "estable · precaución normal — sin exclusiones de ruta"),
        ("VEHÍCULO", "CPD exigido en la práctica en frontera terrestre — imprescindible"),
        ("COMUNICACIONES", "Starlink en transición — tratar como no garantizado"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[-4.8, 36.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    facts=[
        ("Ventana prevista", "Tercer país del corredor de regreso, tras Malaui."),
        ("Entrada", "Songwe desde Malaui, al norte de Karonga."),
        ("Salida", "Namanga hacia Kenia, junto al Parque de Amboseli."),
        ("Seguridad", "País estable, sin zonas excluidas del itinerario; precaución normal reforzada en zonas turísticas de alta afluencia."),
        ("Visado", "e-Visa disponible (Spain no exenta): tramitar online, 5-10 días laborables, o visado a la llegada como respaldo."),
        ("Vehículo", "CPD exigido en la práctica en la frontera terrestre — imprescindible, no opcional como en países vecinos."),
    ],
    alerts=[
        "CPD imprescindible: a diferencia de Mozambique o Malaui, la frontera terrestre de Tanzania exige en la práctica el Carnet de Passage — no confiar en un permiso temporal alternativo.",
        "Dron: no intentar volar dentro de Ngorongoro o Serengeti sin el permiso de pago de TANAPA tramitado con antelación; en la práctica rara vez se concede a particulares.",
        "Starlink: no garantizar el servicio antes de confirmarlo 30-60 días antes del viaje; llevar SIM local como respaldo principal.",
        "Perro prohibido en el Ngorongoro y el Serengeti: prever cuidador en Arusha o Karatu antes de los safaris.",
    ],
    ruta_intro="Entrada por Songwe y ascenso por el corredor central (Mbeya-Iringa) hasta Arusha, con el cráter del Ngorongoro como eje de safari y un desvío costero opcional a Dar es Salaam/Zanzíbar antes de salir hacia Kenia por Namanga.",
    route_rows=[
        ("Entrada y corredor central", "Songwe → Mbeya → Iringa", "Carretera asfaltada principal (Great North Road / TAZARA)"),
        ("Desvío costero opcional", "Iringa → Dar es Salaam → Zanzíbar (ferry)", "2-3 noches; regreso al eje principal por la misma vía o vía Dodoma"),
        ("Safari y logística", "Iringa/Dodoma → Arusha", "Base de safaris del norte; mejor oferta de talleres y recambios"),
        ("Cráter y salida", "Arusha → Ngorongoro → Namanga", "1-2 noches en el cráter; salida hacia Kenia junto a Amboseli"),
    ],
    offroad=[
        "Pistas de safari dentro del Área de Conservación del Ngorongoro y el Serengeti, solo con guía/vehículo homologado del parque cuando así se exija.",
        "El eje principal Songwe-Mbeya-Iringa-Arusha-Namanga es carretera asfaltada; el desvío a Zanzíbar requiere ferry de vehículos desde Dar es Salaam (reserva previa recomendada).",
    ],
    acampada=[
        "Arusha y Karatu (puerta del Ngorongoro): campings orientados a overlanders y operadores de safari, buena oferta de aparcamiento vigilado.",
        "Dentro del Área de Conservación del Ngorongoro: campamentos designados únicamente, sin acampada libre.",
        "Dar es Salaam y Zanzíbar: hoteles y campings urbanos/costeros sin incidencias reportadas.",
    ],
    visado=[
        "e-Visa obligatoria para ciudadanos españoles (no exentos), 50 USD, 5-10 días laborables de tramitación; visado a la llegada disponible como respaldo en los principales puestos.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica (aplica viniendo de Malaui/Mozambique).",
        "Confirmar 30-60 días antes la vigencia exacta y si se exige el CPD también para tránsito exclusivamente por carretera.",
    ],
    fronteras_rows=[
        ("Entrada", "Songwe (Malaui)", "Puente sobre el río Songwe, al norte de Karonga; puesto integrado."),
        ("Salida", "Namanga (Kenia)", "Paso de alto tránsito turístico junto al Parque de Amboseli; puesto bien equipado."),
    ],
    vehiculos=[
        "CPD exigido en la práctica en la frontera terrestre de Songwe — imprescindible, con todos los pares de sellos en regla.",
        "Permiso de importación temporal (TIP) de 90 días complementario al CPD, más seguro de terceros e inspección aduanera en frontera.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Tramitar el permiso TCAA con semanas de antelación para volar fuera de áreas protegidas.",
        "No intentar volar dentro del Ngorongoro o el Serengeti sin el permiso de pago de TANAPA ya concedido.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio en transición: licencia solicitada y preseleccionada por la TCRA, cobertura parcial vía acuerdo directo-a-dispositivo con Airtel, sin servicio residencial pleno confirmado a la fecha de esta revisión.",
        "SIM local (Vodacom, Airtel Tanzania, Tigo) como conectividad principal mientras se confirma el estado de Starlink.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente y vacuna antirrábica en vigor, exigibles en frontera.",
        "Perro prohibido en el Ngorongoro y el Serengeti; prever cuidador en Arusha o Karatu durante los días de safari.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en todo el territorio, incluida la costa y Zanzíbar: profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Muhimbili National Hospital (Dar es Salaam) como mejor referencia sanitaria; clínicas privadas de Arusha para el tramo de safaris. Seguro con evacuación médica real imprescindible en el Ngorongoro/Serengeti.",
    ],
    seguridad_intro="Tanzania es un tramo estable del corredor de regreso: sin zonas excluidas, con precaución normal reforzada en el ambiente de alta afluencia turística de las zonas de safari.",
    seguridad=[
        "Precaución normal reforzada en zonas de alta afluencia turística (robos oportunistas de bolsos/cámaras en Arusha y Zanzíbar).",
        "En safari, seguir siempre las indicaciones del guía/ranger respecto a distancia con la fauna y horarios de circulación dentro de los parques.",
        "Aparcamiento vigilado en Dar es Salaam y Arusha por prudencia estándar.",
    ],
    agua=[
        "Arusha y Dar es Salaam: agua embotellada sin problema en supermercados.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): lodges de safari y campings del corredor Mbeya-Iringa-Arusha, así como hoteles de Dar es Salaam y Zanzíbar, permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje previsto: Songwe → Mbeya (~120 km) → Iringa (~300 km) → Arusha (~470 km vía Dodoma) → Namanga (~110 km), todos con estaciones formales.",
        "Mbeya, Iringa y Arusha concentran la mejor oferta y calidad del país (TotalEnergies, Puma, Oryx); repostar a fondo en Arusha antes del tramo final hacia Kenia.",
    ],
    pendientes=[
        ("CPD", "Confirmar todos los pares de sellos antes de Songwe — exigencia estricta en esta frontera"),
        ("Starlink", "Reconfirmar estado de licencia y cobertura 30-60 días antes del viaje"),
        ("Dron", "Tramitar TCAA con semanas de antelación; descartar vuelo dentro de Ngorongoro/Serengeti salvo permiso TANAPA concedido"),
        ("Perro", "Confirmar cuidador en Arusha/Karatu para los días de safari"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Dar es Salaam, 24h): (+255) 754 04 21 23 · Embajada de España en Dar es Salaam: (+255) 022 266 60 18/19.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

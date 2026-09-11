# -*- coding: utf-8 -*-
"""República del Congo (Congo-Brazzaville) — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Dolisie", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-4.2000, lon=12.6667,
         desc="Tercera ciudad del país y primera gran plaza tras cruzar desde Gabón; nudo de comunicaciones entre Pointe-Noire, Brazzaville y la frontera gabonesa, con oferta de talleres y combustible antes de continuar en cualquier dirección.",
         credit="Jomako · CC BY-SA 3.0", source=W + "Dolisie.jpg?width=900"),
    dict(n=2, name="Pointe-Noire", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-4.7975, lon=11.8481,
         desc="Capital económica y mayor puerto del país, con playas urbanas y la mejor oferta de talleres y recambios del tramo congoleño; punto de referencia si se valora un desvío hacia Cabinda (enclave angoleño) en vez de continuar por Brazzaville.",
         credit="David Stanley · CC BY 2.0", source=W + "Pointe-Noire%20downtown.jpg?width=900"),
    dict(n=3, name="Brazzaville (Basílica de Santa Ana)", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-4.2634, lon=15.2429,
         desc="Capital política, con la Basílica de Santa Ana del Congo (art déco, 1949) como hito arquitectónico y el malecón sobre el río Congo frente a Kinshasa —las dos capitales nacionales más próximas entre sí del mundo. Cruce a la República Democrática del Congo por barco/ferry sobre el río.",
         credit="Henri van der Noot · CC BY-SA 4.0", source=W + "Brazzaville%20-%20Basilique%20Sainte-Anne-du-Congo.jpg?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "cultura": "marron"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Ndendé/Doussala (desde Gabón)", "Frontera", -2.8333, 10.9167,
     "Paso principal desde Gabón hacia Dolisie; confirmar el estado de la pista en temporada de lluvias."),
    ("Frontera · Salida — Brazzaville–Kinshasa (ferry sobre el río Congo, hacia RD Congo)", "Frontera", -4.2800, 15.2800,
     "Cruce en barco/ferry entre las dos capitales; trámite de aduana y pasaportes en ambos lados del río, vehículo embarcado aparte — confirmar tarifas y horarios con antelación, el servicio de carga puede tener menos frecuencia que el de pasajeros."),
    ("Embajada de España en Kinshasa (también acreditada en Congo-Brazzaville)", "Consular", -4.3050, 15.3050,
     "Bd. Colonel Tshatshi nº 37, Kinshasa (Gombe), RD Congo. Tel. +243 813 300 061 / 817 008 770 · Emergencia consular: +243 819 500 289. Sin embajada española propia en Congo-Brazzaville."),
    ("Hôpital Général de Brazzaville", "Hospital", -4.2694, 15.2761,
     "Principal hospital de referencia de la capital congoleña. Coordenada urbana aproximada."),
    ("Combustible · Pointe-Noire / Brazzaville", "Combustible", -4.7975, 11.8481,
     "Mejor oferta y calidad del país (Total, Congo Oil) en las dos grandes ciudades; repostar a fondo en ambas antes de cualquier tramo más largo."),
    ("Combustible · Dolisie", "Combustible", -4.2000, 12.6667,
     "Estaciones formales en el nudo de comunicaciones entre Gabón, Pointe-Noire y Brazzaville."),
    ("Agua potable y de uso general · Pointe-Noire y Brazzaville", "Agua potable", -4.7975, 11.8481,
     "Agua embotellada sin problema en supermercados de las dos grandes ciudades; estaciones de servicio y hoteles permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria: tratar como restringido",
                  "Congo-Brazzaville exige autorización previa de la autoridad de aviación civil (ANAC-Congo) para cualquier vuelo de dron. Norma prudente del proyecto: no volar sin permiso escrito, y no intentar el vuelo cerca de las dos capitales, del río Congo (frontera con RD Congo) ni de instalaciones petroleras de Pointe-Noire.")

STARLINK_CALLOUT = ("warn", "Anunciado para 2026, aún no activo a mediados de año: tratar como no disponible",
                     "Congo-Brazzaville figura entre los mercados africanos con Starlink previsto («coming in 2026») pero sin confirmación de servicio activo a mediados de 2026. Tratarlo como no disponible hasta confirmación oficial y mantener SIM local (MTN Congo, Airtel) como conectividad principal.")

DOG_MATRIX = [
    ("Dolisie, Pointe-Noire, Brazzaville", "permitido con condiciones", "Correa y sombra; calor húmedo intenso en la costa."),
    ("Ferry Brazzaville-Kinshasa", "permitido con condiciones", "Confirmar con la naviera si el perro puede embarcar junto al vehículo o necesita gestión aparte."),
]

SOURCES = [
    ("Saiga Tours · cruce de Cabinda a Pointe-Noire (referencia de frontera sur)", "https://www.saigatours.com/article/A-guide-to-crossing-from-Cabinda-to-Pointe-Noire"),
    ("Roam Facts · guía de viaje de la República del Congo (2026)", "https://roamfacts.com/country/republic-of-the-congo"),
    ("Expedition Conservation · notas de viaje overland por Congo-Brazzaville", "https://expeditionconservation.substack.com/p/congo-brazzaville-first-a-new-master"),
    ("Embajada de España en Kinshasa (también RD Congo y Congo-Brazzaville)", "https://www.exteriores.gob.es/Embajadas/kinshasa/es/Paginas/index.aspx"),
    ("BNCR · Carte Rose CEMAC, portal oficial", "https://bncr.cm/en/"),
    ("tech.africa · disponibilidad de Starlink en África (2026)", "https://tech.africa/starlink-africa/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(-2.8333, 10.9167), (-4.2000, 12.6667), (-4.7975, 11.8481), (-4.2634, 15.2429), (-4.2800, 15.2800)]

HISTORIA_RESUMEN = ("La República del Congo, con capital en Brazzaville, fue el centro administrativo de todo el África Ecuatorial Francesa y heredó de ese pasado una identidad urbana y política distinta a la de su vecina, mucho más grande, la República Democrática del Congo; "
                     "tras la independencia en 1960 adoptó brevemente el marxismo-leninismo, y desde el fin de la Guerra Fría ha vivido guerras civiles recurrentes en torno a la figura del presidente Denis Sassou Nguesso, en el poder durante la mayor parte de las últimas cinco décadas.")

HISTORIA_SECCIONES = [
    ("El reino de Kongo y los pueblos del norte",
     "El sur del territorio formó parte de la periferia del gran reino de Kongo, una de las civilizaciones más sofisticadas de África central antes de la colonización, mientras que los pueblos del norte y del interior forestal (teke, mbochi, entre otros) mantenían estructuras políticas más descentralizadas basadas en el comercio del marfil y los productos forestales."),
    ("Brazzaville, capital del África Ecuatorial Francesa",
     "El explorador franco-italiano Pierre Savorgnan de Brazza fundó Brazzaville en 1880, que se convertiría en la capital administrativa de todo el África Ecuatorial Francesa (que agrupaba los actuales Congo, Gabón, República Centroafricana y Chad); durante la Segunda Guerra Mundial, Brazzaville fue además la capital simbólica de la Francia Libre del general De Gaulle tras la ocupación de París."),
    ("Independencia, el experimento marxista y las guerras civiles",
     "El Congo se independizó en 1960 y en 1969 adoptó oficialmente el marxismo-leninismo bajo el Partido Congoleño del Trabajo, siendo el primer país africano en declararse formalmente marxista; tras la apertura al multipartidismo en 1992, el país vivió sucesivas guerras civiles en los años noventa (1993-94, 1997 y 1998-99) centradas en la disputa por el poder entre facciones armadas leales a distintos líderes, entre ellos el propio Denis Sassou Nguesso."),
    ("Situación actual: petróleo y la larga presidencia de Sassou Nguesso",
     "Denis Sassou Nguesso, que ya había gobernado el país entre 1979 y 1992, recuperó el poder por la fuerza en 1997 y lo mantiene desde entonces mediante sucesivas reformas constitucionales, siendo hoy uno de los jefes de Estado con más años acumulados en el poder de toda África; la economía depende en gran medida del petróleo extraído en la costa atlántica, con una deuda pública elevada pese a esa riqueza y una selva del Congo apenas explorada como potencial de turismo de naturaleza."),
]

HISTORIA_FUENTES = [
    ("BBC News · Republic of Congo country profile", "https://www.bbc.com/news/world-africa-13284240"),
    ("Encyclopaedia Britannica · Republic of the Congo, History", "https://www.britannica.com/place/Republic-of-the-Congo/History"),
    ("International Crisis Group · Republic of Congo", "https://www.crisisgroup.org/africa/central-africa/republic-congo"),
]

SPEC = dict(
    slug="congo", name="Congo (Brazzaville)", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Ndendé/Doussala (desde Gabón)"),
        ("SALIDA", "Ferry Brazzaville–Kinshasa (hacia RD Congo)"),
        ("SEGURIDAD", "estable en el corredor sur · precaución normal"),
        ("SEGURO", "última frontera con Carte Rose CEMAC; RD Congo exige seguro local aparte"),
        ("DECISIÓN DE RUTA", "vía Kinshasa (recomendada) o vía Cabinda — ver ficha de RD Congo"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[-4.4, 13.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("Desde Congo-Brazzaville hay dos vías hacia el sur: (1) cruzar el río Congo en ferry hasta Kinshasa (RD Congo) y bajar por el corredor occidental del Bajo Congo hasta Angola — la vía elegida por este proyecto, más directa y con mejor infraestructura overland documentada; "
              "o (2) desviarse hacia el enclave angoleño de Cabinda desde Pointe-Noire (paso de Massabi/Nzassi) y desde allí buscar transporte marítimo o aéreo a Angola continental, evitando el tránsito por RD Congo. "
              "La vía (1) es la de referencia de esta ficha; revisar la ficha de RD Congo para el detalle del corredor Kinshasa-Matadi-Boma."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Gabón y antes de RD Congo."),
        ("Entrada", "Ndendé/Doussala desde Gabón, hacia Dolisie."),
        ("Salida", "Ferry Brazzaville-Kinshasa sobre el río Congo hacia RD Congo."),
        ("Seguridad", "Estable en el corredor sur (Dolisie-Pointe-Noire-Brazzaville); norte del país (Cuvette, Sangha, fronteras con Camerún/RCA) fuera del itinerario por remoto y sin infraestructura relevante para esta ruta."),
        ("Seguro", "Última frontera del tramo con Carte Rose CEMAC válida — RD Congo no pertenece a esta zona y exige gestionar un seguro local aparte."),
        ("Comunicaciones", "Starlink anunciado para 2026, no confirmado activo; SIM local (MTN Congo, Airtel) como base."),
    ],
    alerts=[
        "Decisión de ruta hacia RD Congo: confirmar con antelación el servicio de ferry de vehículos Brazzaville-Kinshasa (frecuencia, tarifa, documentación) — es un cuello de botella logístico real, no un simple paso fronterizo por carretera.",
        "Norte del país (Cuvette, Sangha, fronteras con Camerún y RCA): fuera del itinerario, sin relevancia para el corredor de bajada previsto.",
        "Dron: sin procedimiento civil turístico claro — tratar como restringido y no volar sin autorización previa por escrito.",
    ],
    ruta_intro="Tramo corto entre la frontera gabonesa y el cruce del río Congo hacia Kinshasa, con Pointe-Noire como base logística alternativa.",
    route_rows=[
        ("Entrada y nudo de comunicaciones", "Ndendé/Doussala → Dolisie", "Primera gran plaza tras Gabón"),
        ("Costa y puerto", "Dolisie → Pointe-Noire", "Mejor oferta de talleres y recambios; opción de desvío a Cabinda"),
        ("Capital y cruce fluvial", "Dolisie → Brazzaville → ferry a Kinshasa", "Basílica de Santa Ana; cruce del río Congo hacia RD Congo"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: el eje Ndendé-Dolisie-Pointe-Noire/Brazzaville es carretera asfaltada en buen estado.",
    ],
    acampada=[
        "Pointe-Noire y Brazzaville: alojamientos con parking vigilado, opción más práctica que la acampada libre en ambas ciudades.",
        "Dolisie: hoteles sencillos con aparcamiento, suficiente para una noche de tránsito.",
    ],
    visado=[
        "Visado electrónico (e-Visa) congoleño previo obligatorio para ciudadanos españoles; tramitar con antelación.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
    ],
    fronteras_rows=[
        ("Entrada", "Ndendé/Doussala (Gabón)", "Carretera asfaltada en el lado gabonés; confirmar estado de la pista congoleña en temporada de lluvias."),
        ("Salida", "Ferry Brazzaville–Kinshasa (RD Congo)", "Cruce fluvial con trámite aduanero en ambos lados; confirmar frecuencia y tarifa del servicio de carga con antelación."),
    ],
    vehiculos=[
        "CPD con todos los pares de sellos en regla.",
        "Carte Rose CEMAC como seguro de responsabilidad civil regional, última frontera donde es válida en este sentido de la marcha.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
        "Confirmar el procedimiento de embarque del vehículo en el ferry de Brazzaville con la naviera antes de llegar a la capital.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa por escrito a la ANAC-Congo antes de intentar introducir el dron en el país.",
        "No volar cerca de las dos capitales, del río Congo (frontera con RD Congo) ni de instalaciones petroleras de Pointe-Noire.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado no confirmado a mediados de 2026 pese al anuncio de llegada dentro del año: revisar el mapa oficial 30-60 días antes.",
        "SIM local (MTN Congo, Airtel) como conectividad principal en Pointe-Noire y Brazzaville.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
        "Confirmar con la naviera del ferry Brazzaville-Kinshasa si el perro puede viajar junto al vehículo o necesita gestión aparte.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "Hôpital Général de Brazzaville como referencia hospitalaria del tramo; seguro con evacuación médica imprescindible.",
    ],
    seguridad_intro="Corredor sur (Dolisie-Pointe-Noire-Brazzaville) estable con precaución normal; el norte del país queda fuera del itinerario por ser remoto y sin infraestructura relevante para esta ruta.",
    seguridad=[
        "No desviarse hacia el norte del país (Cuvette, Sangha, fronteras con Camerún y RCA): fuera del itinerario previsto.",
        "Planificar el cruce del ferry de Brazzaville con margen de tiempo suficiente, evitando llegar el mismo día que se necesita cruzar.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
    ],
    agua=[
        "Pointe-Noire y Brazzaville: agua embotellada en supermercados sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio y hoteles de Dolisie, Pointe-Noire y Brazzaville permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km: Ndendé/Doussala → Dolisie (~120 km) → Pointe-Noire (~150 km) o Brazzaville (~380 km), todos con estaciones formales (Total, Congo Oil).",
        "Repostar a fondo en Brazzaville antes del ferry: en Kinshasa, del otro lado, la oferta y calidad pueden variar más.",
    ],
    pendientes=[
        ("Ferry Brazzaville-Kinshasa", "Confirmar frecuencia, tarifa y procedimiento de embarque del vehículo con semanas de antelación"),
        ("Visado", "Tramitar el e-Visa congoleño con margen suficiente"),
        ("Seguro RD Congo", "Confirmar qué seguro local hace falta al cruzar, dado que Carte Rose CEMAC deja de ser válida"),
        ("Dron", "Contactar con la ANAC-Congo o descartar el vuelo en el país"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Kinshasa, competente también para Congo-Brazzaville): +243 819 500 289.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

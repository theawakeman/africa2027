# -*- coding: utf-8 -*-
"""Camerún — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Limbe (Centro de Fauna y Down Beach)", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1 noche",
         lat=4.0186, lon=9.2054,
         desc="Ciudad costera a los pies del monte Camerún, con el Limbe Wildlife Centre (santuario de primates rescatados del tráfico de carne de animales silvestres) y playas volcánicas de arena negra; primera gran base de servicios tras cruzar desde Nigeria.",
         credit="Ndiptambe · CC0", source=W + "Limbe%20wildlife%20center.jpg?width=900"),
    dict(n=2, name="Kribi (Chutes de la Lobé)", cat="Naturaleza", prio="Alta", dog="permitido", time="1–2 noches",
         lat=2.9098, lon=9.8973,
         desc="Una de las pocas cascadas del mundo que cae directamente al mar; playas de arena blanca y aguas tranquilas, con Kribi como referencia de descanso y de la mejor oferta de pescado fresco de la costa camerunesa.",
         credit="Blaizo 237 · CC BY-SA 4.0", source=W + "Les%20chutes%20de%20la%20lobé%20kribi%20cameroon1.jpg?width=900"),
    dict(n=3, name="Yaundé", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=3.8480, lon=11.5021,
         desc="Capital política, sede de la embajada de España y mayor base administrativa y logística del interior del país, asentada sobre siete colinas; punto de paso obligado antes de continuar hacia Gabón o la República del Congo.",
         credit="Eavebe · CC BY-SA 3.0", source=W + "Yaoundé%201.jpg?width=900"),
    dict(n=4, name="Duala", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=4.0483, lon=9.7043,
         desc="Capital económica y mayor puerto del país; talleres, recambios y aeropuerto internacional, aunque con más tráfico, calor húmedo y menor tranquilidad que Limbe o Kribi para pernoctar.",
         credit="Mboupda Talla Roger · CC BY-SA 3.0", source=W + "Port%20autonome%20de%20Douala%201.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Ekok/Mfum (desde Nigeria)", "Frontera", 5.9400, 9.0650,
     "Cruce del río Cross hacia Mamfe, en plena región Suroeste (zona de crisis anglófona). Ver alerta detallada de seguridad antes de decidir esta entrada; posibles cierres súbitos y escoltas militares."),
    ("Frontera · Salida — hacia Gabón (Kyé-Ossi / Ambam)", "Frontera", 2.3167, 11.2833,
     "Puesto en la llamada «zona de las tres fronteras» (Camerún-Gabón-Guinea Ecuatorial), fuera de la zona de conflicto; carretera asfaltada desde Yaundé."),
    ("Embajada de España en Yaundé", "Consular", 3.8944, 11.5139,
     "Bld. de l'U.R.S.S., Quartier Bastos, B.P. 877, Yaundé. Tel. +237 222 20 35 43 · Emergencia consular 24h: +237 698 44 79 00 · emb.yaunde@maec.es."),
    ("Hôpital Central de Yaundé", "Hospital", 3.8720, 11.5180,
     "Principal hospital de referencia de la capital y del país. Coordenada urbana aproximada."),
    ("Combustible · Duala / Yaundé", "Combustible", 4.0483, 9.7043,
     "Mejor oferta y calidad del país (Tradex, Total, Oryx) en las dos grandes ciudades; repostar a fondo en ambas antes de cualquier tramo más largo."),
    ("Combustible · Limbe / Kribi", "Combustible", 4.0186, 9.2054,
     "Estaciones formales en el eje costero Limbe-Duala-Kribi, sin problema de suministro en el itinerario previsto."),
    ("Agua potable y de uso general · Duala y Yaundé", "Agua potable", 4.0483, 9.7043,
     "Agua embotellada sin problema en supermercados de las grandes ciudades; estaciones de servicio y hoteles de Limbe, Kribi, Duala y Yaundé permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria y muy restrictiva",
                  "Camerún trata los drones como material sensible: la autorización debe solicitarse con antelación ante las autoridades de aviación civil y, en la práctica, también ante el Ministerio de Defensa por razones de seguridad interna (crisis anglófona, Boko Haram). Norma prudente del proyecto: no volar en ningún caso en las regiones Noroeste, Suroeste y Extremo Norte, y no intentar introducir el dron sin autorización escrita previa en el resto del país.")

STARLINK_CALLOUT = ("warn", "Estado legal no resuelto a mediados de 2026: tratar como no disponible",
                     "Camerún ha mantenido una postura restrictiva hacia Starlink, sin autorización comercial plena confirmada a mediados de 2026 pese a la expansión del servicio en países vecinos. Tratarlo como no disponible hasta confirmación oficial explícita y mantener SIM local (MTN Cameroon, Orange) como conectividad principal.")

DOG_MATRIX = [
    ("Región Suroeste (Mamfe y alrededores)", "no recomendado", "Evitar pernocta y paradas innecesarias con el perro en la zona de conflicto; cruzar directo hacia Limbe el mismo día si es posible."),
    ("Limbe, Kribi, Duala, Yaundé", "permitido con condiciones", "Correa y sombra; calor húmedo intenso en la costa."),
]

SOURCES = [
    ("U.S. Embassy Cameroon · Travel Advisory (mayo 2026)", "https://cm.usembassy.gov/travel-advisory-cameroon-may-2026/"),
    ("RegionAlert · mapa de zonas de guerra anglófonas y Boko Haram en Camerún (2026)", "https://regionalert.com/blog/cameroon-travel-safety-2026.html"),
    ("A Little Off Track · cruce de Mfum/Ekok y ruta por Mamfe-Limbe-Kribi-Yaundé", "https://www.alittleofftrack.com/overlanding-cameroon/"),
    ("Fundación Mapfre iO · información para viajeros en Camerún", "https://fundacionio.com/viajarseguro/paises/camerun/informacion-para-viajeros-camerun/"),
    ("Embajada de España en Camerún · contacto", "https://www.exteriores.gob.es/Embajadas/yaunde/es/Paginas/index.aspx"),
    ("Business in Cameroon · Carte Rose CEMAC", "https://www.businessincameroon.com/finance/1207-6371-in-2013-2015-the-carte-rose-enabled-cemac-insurers-to-pay-cross-border-damages-worth-fcfa-382-million"),
    ("BNCR · Carte Rose CEMAC, portal oficial", "https://bncr.cm/en/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(5.9400, 9.0650), (4.0186, 9.2054), (4.0483, 9.7043), (2.9098, 9.8973), (3.8480, 11.5021), (2.3167, 11.2833)]

HISTORIA_RESUMEN = ("Camerún es a menudo llamado «África en miniatura» por su extraordinaria diversidad geográfica y étnica, resultado también de una historia colonial poco común: colonia alemana hasta 1916, fue después repartida entre Francia y Gran Bretaña, y las dos mitades "
                     "se reunificaron en una única nación en 1961, una fusión franco-británica que sigue generando tensión hoy en la región angloparlante del noroeste y suroeste del país.")

HISTORIA_SECCIONES = [
    ("Reinos bamún y sultanatos del norte",
     "El territorio albergó reinos organizados como el de los bamún (con capital en Foumban, célebre por su palacio real y su propia escritura inventada a comienzos del siglo XX) y sultanatos islámicos fulani en el norte, junto con una gran diversidad de pequeños reinos y jefaturas en las regiones costeras y forestales."),
    ("Kamerun alemán y su reparto tras la Primera Guerra Mundial",
     "Alemania estableció el protectorado de Kamerun en 1884, desarrollando plantaciones e infraestructura; tras su derrota en la Primera Guerra Mundial, el territorio fue repartido en 1922 como mandato de la Sociedad de Naciones entre Francia (la mayor parte, al este) y Gran Bretaña (dos franjas al oeste, administradas junto a Nigeria), un reparto que crearía dos tradiciones administrativas y lingüísticas distintas dentro de un mismo futuro país."),
    ("Independencia y la reunificación de 1961",
     "El Camerún francés se independizó en 1960; en 1961, tras un referéndum, la parte sur del Camerún británico votó unirse a la nueva república (mientras la parte norte optó por integrarse en Nigeria), dando lugar a un Camerún reunificado con dos idiomas oficiales, francés e inglés, bajo el presidente Ahmadou Ahidjo y, desde 1982, Paul Biya, uno de los jefes de Estado con más años en el poder de toda África."),
    ("Situación actual: la crisis anglófona y la longevidad de Paul Biya",
     "Desde 2016-2017, las regiones angloparlantes del noroeste y suroeste viven un conflicto armado de baja intensidad (la «crisis anglófona») entre el Estado camerunés y grupos separatistas que reclaman la independencia de una «Ambazonia», un foco de inestabilidad ajeno al eje costero y central de este itinerario; Paul Biya, en el poder desde 1982, sigue gobernando el país en 2026, en uno de los mandatos presidenciales más largos del mundo."),
]

HISTORIA_FUENTES = [
    ("BBC News · Cameroon country profile", "https://www.bbc.com/news/world-africa-13146029"),
    ("Encyclopaedia Britannica · Cameroon, History", "https://www.britannica.com/place/Cameroon/History"),
    ("International Crisis Group · Cameroon's Anglophone Crisis", "https://www.crisisgroup.org/africa/central-africa/cameroon"),
]

SPEC = dict(
    slug="camerun", name="Camerún", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Ekok/Mfum (desde Nigeria) — ver alerta de ruta"),
        ("SALIDA", "Kyé-Ossi/Ambam (hacia Gabón)"),
        ("SEGURIDAD", "Noroeste/Suroeste y Extremo Norte EXCLUIDOS — conflicto activo"),
        ("SEGURO", "cambio de zona CEDEAO (Brown Card) a CEMAC (Carte Rose) en esta frontera"),
        ("DRONES", "prácticamente inviable — no volar en zonas de conflicto"),
        ("REVALIDACIÓN", "30–60 días antes, y de nuevo 72 h antes de Ekok"),
    ],
    center=[4.5, 10.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y de nuevo 72 h antes de cruzar por Ekok/Mfum.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("La única entrada terrestre práctica desde Nigeria (Ekok/Mfum) atraviesa Mamfe, en la región Suroeste, clasificada como zona de conflicto activo por la crisis separatista anglófona: "
              "kidnapping, IEDs, «ciudades fantasma» semanales impuestas por los separatistas y operaciones militares que pueden activar la zona sin previo aviso. "
              "Un convoy humanitario fue detenido y uno de sus vehículos destruido en un control cerca de Kumba en diciembre de 2025. "
              "Decisión del proyecto: cruzar Ekok/Mfum → Mamfe → Limbe en un único día, sin pernocta ni paradas innecesarias en la región Suroeste, evitando por completo la carretera Kumba-Mamfe si hay alternativa, "
              "y con información local verificada las 72 h previas (no solo fuentes internacionales). Si la situación empeora antes del viaje, la alternativa es NO entrar por aquí y estudiar una ruta más al este (Nigeria-Camerún vía Adamawa/Garoua, más larga y con menos infraestructura overland, o replantear el corredor de Camerún por completo) — decisión que debe cerrarse con antelación suficiente, igual que la del corredor de Sudán en el tramo de regreso."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Nigeria y antes de Gabón."),
        ("Entrada", "Ekok/Mfum desde Nigeria: cruza directamente la región Suroeste, en conflicto activo — ver decisión de ruta."),
        ("Salida", "Kyé-Ossi/Ambam hacia Gabón: zona de las tres fronteras, fuera de las áreas de conflicto."),
        ("Seguridad", "Noroeste, Suroeste (crisis anglófona) y Extremo Norte (Boko Haram/ISWAP): EXCLUIDOS del itinerario salvo el tránsito imprescindible Ekok-Mamfe-Limbe."),
        ("Seguro", "Cambio de zona regional en esta frontera: de Brown Card (CEDEAO) a Carte Rose (CEMAC) — comprar la Carte Rose nada más entrar."),
        ("Comunicaciones", "Starlink sin autorización comercial confirmada; SIM local (MTN Cameroon, Orange) como base."),
    ],
    alerts=[
        "Ruta de entrada (Ekok/Mfum → Mamfe): zona de conflicto activo de la crisis anglófona — cruzar en un único día sin pernocta, con información local verificada 72 h antes, y estar preparado para un cierre súbito de frontera o un desvío impuesto por control militar.",
        "Ruta excluida — Extremo Norte: actividad activa de Boko Haram e ISWAP (Mayo-Sava, Mayo-Tsanaga, Logone-et-Chari); fuera del itinerario sin excepción.",
        "Seguro regional: el Brown Card de Nigeria/CEDEAO no cubre Camerún — comprar la Carte Rose CEMAC en la primera oportunidad tras cruzar Ekok.",
        "Dron: no volar en ningún caso en Noroeste, Suroeste o Extremo Norte; en el resto del país, solo con autorización previa por escrito.",
    ],
    ruta_intro="Cruce de un día por la zona de conflicto (Ekok-Mamfe-Limbe) y descenso por la costa hasta Yaundé, evitando el interior anglófono y el Extremo Norte.",
    route_rows=[
        ("Entrada — cruce sin pernocta", "Ekok/Mfum → Mamfe → Limbe", "Zona de conflicto activo; un único día, sin paradas innecesarias"),
        ("Costa y descanso", "Limbe → Duala → Kribi", "Chutes de la Lobé; mejor descanso costero del tramo"),
        ("Capital e interior", "Kribi → Yaundé", "Embajada española; base administrativa antes de Gabón"),
        ("Hacia Gabón", "Yaundé → Kyé-Ossi/Ambam", "Zona de las tres fronteras, fuera de áreas de conflicto"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: el eje Ekok-Mamfe-Limbe-Duala-Kribi-Yaundé es carretera asfaltada, con el riesgo estando en la seguridad y no en la dificultad técnica.",
    ],
    acampada=[
        "Mamfe: sin acampada libre — si hiciera falta parar, misión católica o recinto vigilado, nunca acampada al raso (riesgo de confusión con posiciones militares o separatistas).",
        "Limbe y Kribi: hoteles y campings costeros con aparcamiento, opción de descanso real tras el cruce.",
    ],
    visado=[
        "Visado camerunés previo obligatorio para ciudadanos españoles, tramitado con antelación (embajada de Camerún en Madrid: 91 571 11 60).",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
        "Confirmar la vigencia exacta del visado 30-60 días antes; revisar también si se exige registro adicional en Mamfe dado el contexto de seguridad.",
    ],
    fronteras_rows=[
        ("Entrada", "Ekok/Mfum (Nigeria)", "Cruce del río Cross hacia Mamfe; zona de conflicto activo — cruzar en un día, sin pernocta, con información local de 72 h."),
        ("Salida", "Kyé-Ossi/Ambam (Gabón)", "Zona de las tres fronteras (Camerún-Gabón-Guinea Ecuatorial); fuera de áreas de conflicto, carretera asfaltada desde Yaundé."),
    ],
    vehiculos=[
        "CPD con todos los pares de sellos en regla.",
        "Carte Rose CEMAC obligatoria desde la entrada por Ekok: el Brown Card de Nigeria no tiene validez en Camerún — comprarla en la primera plaza con oferta (Mamfe o Limbe).",
        "Carnet de conducir internacional obligatorio en todos los controles, especialmente numerosos en la región Suroeste.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No volar en ningún caso en las regiones Noroeste, Suroeste o Extremo Norte, por razones de seguridad y de sensibilidad militar del espacio aéreo.",
        "En el resto del país, solicitar autorización previa por escrito ante las autoridades de aviación civil camerunesas antes de intentar introducir el dron.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Sin autorización comercial confirmada a mediados de 2026: tratar como no disponible y revisar el mapa oficial 30-60 días antes.",
        "SIM local (MTN Cameroon, Orange) como conectividad principal en Limbe, Duala, Kribi y Yaundé.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
        "Evitar pernocta y paradas innecesarias con el perro en la región Suroeste (Mamfe); cruzar directo hacia Limbe.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "La atención sanitaria general está por debajo de los estándares europeos (Fundación Mapfre iO); Hôpital Central de Yaundé como mejor referencia del tramo. Seguro con evacuación médica real imprescindible.",
    ],
    seguridad_intro="Camerún es, junto con Nigeria, el tramo de mayor exigencia de seguridad del proyecto: el cruce de entrada obliga a atravesar en un día una zona de conflicto activo antes de llegar a la costa, tranquila y manejable.",
    seguridad=[
        "Cruzar Ekok-Mamfe-Limbe en un único día, sin pernocta ni paradas innecesarias; evitar la carretera Kumba-Mamfe si existe alternativa verificada el mismo día.",
        "Informarse con fuentes locales (no solo internacionales) 72 h antes del cruce: los «ghost town» semanales y los controles militares pueden cambiar la situación de un día para otro.",
        "No fotografiar controles militares ni instalaciones de seguridad en ningún punto del país, especialmente en la región Suroeste.",
        "Fuera de la región de conflicto, el resto del itinerario (Limbe-Duala-Kribi-Yaundé-frontera de Gabón) es manejable con precaución normal.",
    ],
    agua=[
        "Duala y Yaundé: agua embotellada en supermercados sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio y hoteles/campings de Limbe, Kribi, Duala y Yaundé permiten llenar el depósito con manguera; confirmar en recepción. En Mamfe, no dar por hecho ningún punto — cruzar con el depósito ya cargado desde Nigeria.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje previsto: Ekok → Limbe (~90 km) → Duala (~70 km) → Kribi (~150 km) → Yaundé (~180 km) → Kyé-Ossi (~280 km), todos con estaciones formales salvo el tramo inicial en zona de conflicto.",
        "Repostar a fondo en Nigeria (Obudu/Calabar) antes de Ekok: en Mamfe la oferta puede estar interrumpida por la situación de seguridad — no depender de encontrar combustible en la propia zona de conflicto.",
        "Duala y Yaundé concentran la mejor oferta y calidad del país (Tradex, Total, Oryx); repostar a fondo en ambas antes de tramos más largos.",
    ],
    pendientes=[
        ("Ruta de entrada", "Revalidar 72 h antes si Ekok/Mfum-Mamfe es viable con información local, o replantear el corredor completo de Camerún"),
        ("Visado", "Tramitar con margen en la embajada de Camerún en Madrid"),
        ("Seguro CEMAC", "Comprar la Carte Rose nada más cruzar a Camerún"),
        ("Dron", "Descartar el vuelo salvo autorización escrita expresa fuera de las zonas de conflicto"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. La decisión de ruta de entrada debe revalidarse activamente antes del viaje, igual que el corredor de Sudán en el tramo de regreso.",
    emergency="Emergencia consular española (Yaundé, 24h): +237 698 44 79 00 · Embajada de España en Yaundé: +237 222 20 35 43.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

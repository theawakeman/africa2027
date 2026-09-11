# -*- coding: utf-8 -*-
"""Benín — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Cotonou (Mercado de Dantokpa)", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=6.3703, lon=2.3912,
         desc="Capital económica y mayor base logística del país: puerto, aeropuerto internacional, embajada de España acreditada desde Abuja, talleres y recambios. El mercado de Dantokpa, uno de los más grandes de África Occidental, ocupa la orilla del lago Nokoué.",
         credit="Alacoolwiki · CC BY 4.0", source=W + "Marché%20Dantokpa%201.jpg?width=900"),
    dict(n=2, name="Uidá — Puerta del No Retorno", cat="Patrimonio", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=6.3597, lon=2.0870,
         desc="Cuna histórica del vudú y uno de los mayores puntos de embarque de la trata atlántica; el monumento de la Puerta del No Retorno cierra la Route des Esclaves, con el Templo de las Pitones y la Basílica de la Inmaculada Concepción en el centro de la ciudad.",
         credit="Borisghost · CC0", source=W + "Porte%20du%20non-retour%20au%20Benin.jpg?width=900"),
    dict(n=3, name="Ganvié — poblado lacustre", cat="Cultura", prio="Alta", dog="prohibido", time="½ día",
         lat=6.4667, lon=2.4167,
         desc="Aldea sobre pilotes en el lago Nokoué, fundada por el pueblo tofinu para escapar de los cazadores de esclavos fon; se visita exclusivamente en piragua con guía local. El perro no tiene cabida en las piraguas ni en las viviendas palafíticas.",
         credit="jbdodane · CC BY 2.0", source=W + "Ganvié%20fishing%20village%20on%20stilts%20in%20Benin%20(10282059623)%20(2).jpg?width=900"),
    dict(n=4, name="Palacios Reales de Abomey", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=7.1833, lon=1.9833,
         desc="Recinto de doce palacios sucesivos de los reyes del antiguo Reino de Dahomey (s. XVII-XIX), Patrimonio Mundial UNESCO; bajorrelieves de barro y el Museo Histórico de Abomey narran la historia militar y ritual del reino.",
         credit="Willem Heerbaart · CC BY 2.0", source=W + "Royal%20Palaces%2C%20Abomey%20(Benin)%20banner.jpg?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "patrimonio": "marron", "cultura": "morado", "patrimonio unesco": "marron"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Hillacondji/Sanvee-Condji (desde Togo)", "Frontera", 6.1667, 1.6333,
     "Puesto conjunto (yuxtapuesto) entre Togo y Benín; cruzar por la mañana, el tráfico comercial se satura al mediodía."),
    ("Frontera · Salida — Kraké/Seme (hacia Nigeria)", "Frontera", 6.3697, 2.7275,
     "Paso más transitado de África Occidental hacia Lagos; alta congestión y controles múltiples. Tramitar el visado nigeriano ANTES de llegar — no existe visado en frontera para turismo."),
    ("Embajada de España en Abuja (acreditada también en Benín)", "Consular", 9.0579, 7.4951,
     "Nigeria y Benín comparten demarcación consular española desde Abuja. Contacto y cita previa por la embajada de Abuja; Cotonou dispone solo de gestión honoraria puntual — confirmar canal exacto antes del viaje."),
    ("CNHU-HKM (Centre National Hospitalier Universitaire) — Cotonou", "Hospital", 6.3667, 2.4333,
     "Principal hospital universitario y de referencia del país. Coordenada urbana aproximada."),
    ("Combustible · Cotonou", "Combustible", 6.3703, 2.3912,
     "Mejor oferta y calidad del país (Total, Oryx, Petro Ivoire); repostar aquí antes del tramo final hacia Kraké/Nigeria."),
    ("Combustible · Uidá / Abomey", "Combustible", 6.3667, 2.0333,
     "Estaciones formales en el eje Cotonou-Uidá-Abomey, sin problema de suministro en el itinerario previsto."),
    ("Agua potable y de uso general · Cotonou", "Agua potable", 6.3703, 2.3912,
     "Agua embotellada sin problema en supermercados; estaciones de servicio y hoteles de Cotonou y Uidá permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria: tratar como restringido",
                  "Benín no publica un procedimiento civil turístico simple y estable para drones; la Autorité Nationale de l'Aviation Civile (ANAC-Bénin) exige autorización previa para cualquier vuelo. Norma prudente del proyecto: no volar sin permiso escrito, mantener el equipo declarable, y evitar zonas cercanas a fronteras, instalaciones militares y áreas protegidas (Pendjari, W).")

STARLINK_CALLOUT = ("warn", "No disponible / estado no confirmado a mediados de 2026",
                     "Benín no figura de forma consistente entre los mercados africanos con Starlink activo en las listas de expansión revisadas a mediados de 2026. Tratarlo como no disponible hasta confirmación oficial y mantener SIM local (MTN Bénin, Moov) como conectividad principal.")

DOG_MATRIX = [
    ("Ganvié (piraguas y viviendas palafíticas)", "prohibido", "Dejar el perro en Cotonou con cuidador o rotación entre los viajeros durante la visita."),
    ("Cotonou, Uidá, Abomey", "permitido con condiciones", "Correa y sombra; tráfico denso en Cotonou."),
]

SOURCES = [
    ("Scoot West Africa · guía de visados de África Occidental", "https://scootwestafrica.com/guide-visas/"),
    ("Scoot West Africa · cruce de Seme/Kraké con e-visa nigeriano", "https://scootwestafrica.com/crossing-at-seme-krake-with-an-e-visa-for-nigeria/"),
    ("ECOWAS Brown Card · esquema regional de seguro (CEDEAO)", "https://www.browncard.org/"),
    ("Embajada de España en Nigeria, Benín y CEDEAO (Abuja)", "https://www.exteriores.gob.es/Embajadas/abuja/es/Paginas/index.aspx"),
    ("UNESCO · Palacios Reales de Abomey", "https://whc.unesco.org/en/list/323/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(6.1667, 1.6333), (6.3703, 2.3912), (6.3597, 2.0870), (7.1833, 1.9833), (6.4667, 2.4167), (6.3697, 2.7275)]

HISTORIA_RESUMEN = ("Benín fue el corazón del poderoso reino de Dahomey, temido por su ejército y tristemente célebre por su papel en la trata negrera atlántica desde el «Puerto de No Retorno» de Ouidah; hoy es reconocido como uno de los grandes bastiones democráticos de África "
                     "Occidental desde su pionera transición pacífica del socialismo al multipartidismo en 1990, y sigue siendo cuna del vudú, religión que aquí tiene su origen histórico y su reconocimiento oficial.")

HISTORIA_SECCIONES = [
    ("El reino de Dahomey y su ejército de amazonas",
     "El reino de Dahomey, con capital en Abomey, se consolidó desde el siglo XVII como una de las potencias militares más organizadas de África Occidental, célebre por su cuerpo de guerreras (las «amazonas» de Dahomey) y por un Estado centralizado que sostenía su economía en gran medida sobre la captura y venta de esclavos a comerciantes europeos en la costa."),
    ("Ouidah y el «Puerto de No Retorno»",
     "La ciudad costera de Ouidah fue uno de los mayores puertos de embarque de esclavos hacia América durante los siglos XVII a XIX, un pasado hoy conmemorado en la «Ruta de los Esclavos» y su monumento del Puerto de No Retorno; Ouidah es también, junto con Abomey, uno de los grandes centros espirituales del vudú, religión reconocida oficialmente en Benín y con festival nacional propio."),
    ("Colonia francesa y la efímera «República Popular de Benín»",
     "Francia colonizó el territorio como Dahomey a finales del siglo XIX, integrándolo en el África Occidental Francesa; tras la independencia en 1960, el país vivió una notable inestabilidad con varios golpes de Estado hasta que el militar Mathieu Kérékou instauró en 1972 un régimen marxista-leninista de partido único, renombrando el país República Popular de Benín en 1975."),
    ("Situación actual: pionero de la transición democrática africana",
     "En 1990, Benín fue pionero al organizar una «Conferencia Nacional» que condujo pacíficamente del marxismo al multipartidismo, un modelo que después inspiraría transiciones similares en otros países africanos; el propio Kérékou aceptó la derrota electoral en 1991, un hecho poco común en la época, y desde entonces el país mantiene una de las democracias más estables de la región, aunque con tensiones recientes en torno a reformas constitucionales."),
]

HISTORIA_FUENTES = [
    ("BBC News · Benin country profile", "https://www.bbc.com/news/world-africa-13037572"),
    ("UNESCO · Palacios reales de Abomey", "https://whc.unesco.org/en/list/323/"),
    ("Encyclopaedia Britannica · Benin, History", "https://www.britannica.com/place/Benin"),
]

SPEC = dict(
    slug="benin", name="Benín", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Hillacondji/Sanvee-Condji (desde Togo)"),
        ("SALIDA", "Kraké/Seme (hacia Nigeria)"),
        ("SEGURIDAD", "estable en el sur · precaución en el norte (Pendjari/W)"),
        ("FRONTERA TERRESTRE", "Kraké/Seme, la más transitada de la subregión"),
        ("VISADO NIGERIA", "tramitar ANTES de llegar a Kraké — sin visado en frontera"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[6.7, 2.2], zoom=8,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Benín concentra en poco espacio algunos de los puntos históricos más importantes del golfo de Guinea: Uidá y la Puerta del No Retorno (memoria de la trata atlántica y cuna del vudú), "
                   "el poblado lacustre de Ganvié y los Palacios Reales de Abomey (UNESCO), con Cotonou como base logística antes de cruzar a Nigeria por Kraké/Seme, "
                   "el paso más transitado — y el que exige más planificación previa de todo el tramo."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Togo y antes de Nigeria."),
        ("Entrada", "Hillacondji/Sanvee-Condji desde Togo: puesto conjunto, cruzar por la mañana."),
        ("Salida", "Kraké/Seme hacia Nigeria: paso más transitado de la subregión; visado nigeriano imprescindible ANTES de llegar."),
        ("Visado Nigeria", "No existe visado de turismo en frontera — tramitar el e-Visa o visado consular con semanas de antelación."),
        ("Seguridad", "Estable en el sur (Cotonou-Uidá-Abomey-Ganvié); el norte (parques de Pendjari y W, frontera con Burkina Faso/Níger) fuera del itinerario por riesgo yihadista transfronterizo del Sahel."),
        ("Comunicaciones", "Starlink sin confirmar en el país; SIM local (MTN Bénin, Moov) como base."),
    ],
    alerts=[
        "Visado de Nigeria: NO se emite en la frontera de Kraké/Seme para turismo — tramitarlo por e-Visa o consulado antes de salir de España o desde Cotonou, con margen de varias semanas.",
        "Norte de Benín (parques de Pendjari y W, frontera con Burkina Faso y Níger): fuera del itinerario previsto por el riesgo de incursiones yihadistas transfronterizas del Sahel, extendido a esta zona en los últimos años.",
        "Ganvié: perro prohibido en piraguas y viviendas — planificar cuidado en Cotonou antes de la visita.",
    ],
    ruta_intro="Tramo del sur de Benín, entre las dos fronteras de Togo y Nigeria, con desvío a Abomey.",
    route_rows=[
        ("Entrada y costa histórica", "Hillacondji → Uidá → Cotonou", "Puerta del No Retorno; base logística en Cotonou"),
        ("Desvío histórico", "Cotonou → Abomey (Palacios Reales)", "UNESCO; ida y vuelta desde Cotonou o de paso hacia el norte corto"),
        ("Poblado lacustre", "Cotonou → Ganvié", "Piragua con guía local; perro prohibido a bordo"),
        ("Hacia Nigeria", "Cotonou → Kraké/Seme", "Paso más transitado de la subregión; visado nigeriano ya tramitado"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: el eje Hillacondji-Cotonou-Abomey-Kraké es carretera asfaltada en buen estado.",
    ],
    acampada=[
        "Cotonou: alojamientos con parking vigilado, opción más práctica que la acampada libre en la capital económica.",
        "Uidá/Abomey: pequeños hoteles con aparcamiento cerca de los sitios históricos.",
    ],
    visado=[
        "Visado electrónico (e-Visa) beninés previo obligatorio para ciudadanos españoles; tramitar con antelación.",
        "Visado nigeriano: imprescindible antes de llegar a Kraké/Seme — no hay visado de turismo en frontera; el visado de llegada (visa on arrival) en Nigeria está limitado a negocios con invitación y no aplica a la mayoría de overlanders.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
    ],
    fronteras_rows=[
        ("Entrada", "Hillacondji/Sanvee-Condji (Togo)", "Puesto conjunto (yuxtapuesto); cruzar por la mañana, tráfico comercial satura el mediodía."),
        ("Salida", "Kraké/Seme (Nigeria)", "Paso más transitado de la subregión hacia Lagos; alta congestión y controles múltiples; visado nigeriano ya tramitado es obligatorio."),
    ],
    vehiculos=[
        "CPD con todos los pares de sellos en regla; Carte Brune CEDEAO como seguro de responsabilidad civil regional.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
        "Documentación del vehículo en copias adicionales para el paso de Kraké/Seme, el más exigente en revisión documental del tramo.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa por escrito a la ANAC-Bénin antes de intentar introducir el dron en el país.",
        "No volar en Pendjari, W ni cerca de fronteras o instalaciones militares, tampoco con autorización genérica.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado no confirmado a mediados de 2026: revisar el mapa oficial 30-60 días antes de la entrada.",
        "SIM local (MTN Bénin, Moov) como conectividad principal en Cotonou y el eje sur.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE).",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "CNHU-HKM (Cotonou) como referencia hospitalaria del tramo; seguro con evacuación médica imprescindible.",
    ],
    seguridad_intro="Sur de Benín (Cotonou-Uidá-Abomey-Ganvié) estable con precaución normal; el norte del país queda fuera del itinerario por el riesgo yihadista transfronterizo del Sahel.",
    seguridad=[
        "No desviarse hacia el norte del país (Pendjari, W, fronteras con Burkina Faso y Níger) por la situación de seguridad regional.",
        "Preparar toda la documentación (vehículo, visados, CPD) antes de llegar a Kraké/Seme: es el control más exhaustivo del tramo.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
    ],
    agua=[
        "Cotonou y Uidá: agua embotellada en supermercados y tiendas sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio de Cotonou y los hoteles de Uidá y Abomey permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km: Hillacondji → Cotonou (~85 km) → Abomey (~140 km, desvío) → Ganvié (~20 km) → Kraké/Seme (~35 km), todos con estaciones formales.",
        "Repostar en Cotonou antes del desvío a Abomey y antes del tramo final hacia Kraké: mejor oferta y calidad del país.",
    ],
    pendientes=[
        ("Visado Nigeria", "Tramitar con semanas de antelación — condiciona toda la salida por Kraké/Seme"),
        ("Visado Benín", "Tramitar el e-Visa beninés con margen suficiente"),
        ("Dron", "Contactar con la ANAC-Bénin o descartar el vuelo en el país"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Policía 117 · Bomberos/Ambulancia 118 · Emergencia consular española (Embajada Abuja): consultar teléfono vigente en exteriores.gob.es antes de viajar.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

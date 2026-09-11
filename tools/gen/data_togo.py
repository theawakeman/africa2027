# -*- coding: utf-8 -*-
"""Togo — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Lomé (Grand Marché y Catedral del Sagrado Corazón)", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=6.1319, lon=1.2228,
         desc="Capital y única gran base logística del país: puerto, aeropuerto internacional, mercado central (Grand Marché, dominado por las «Nana Benz» del comercio textil) junto a la Catedral del Sagrado Corazón. Última plaza con oferta completa antes de Ghana o de Benín según el sentido de la marcha.",
         credit="Dan Sloan · CC BY-SA 2.0", source=W + "Lomé%20Grand%20Marché%20with%20the%20Cathédrale%20du%20Sacré%20Coeur%20(33592985581).jpg?width=900"),
    dict(n=2, name="Lac Togo y Togoville", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=6.2667, lon=1.5333,
         desc="Laguna costera a 30 km de Lomé; Togoville es cuna del vudú togolés y del tratado colonial de 1884 con Alemania, con una catedral católica sincrética (Notre-Dame du Lac Togo) junto a los santuarios vudú. Travesía en piragua desde Agbodrafo.",
         credit="Rayman3640 · CC BY-SA 3.0", source=W + "Cathédrale%20Notre-Dame%20du%20Lac%20Togo.jpg?width=900"),
    dict(n=3, name="Cascada de Kpimé (Kpalimé)", cat="Naturaleza", prio="Media", dog="permitido", time="1 día",
         lat=6.9667, lon=0.6333,
         desc="Cascada de unos 50 m en las montañas de Kpalimé (macizo del Togo, región cafetera y cacaotera), con senderos entre plantaciones y buena climatología por altitud. Desvío hacia el interior desde el eje costero.",
         credit="Ak9visuelmind · CC BY-SA 4.0", source=W + "Cascade%20de%20Kpimé%201.jpg?width=900"),
    dict(n=4, name="Aného", cat="Cultura", prio="Baja", dog="permitido", time="medio día",
         lat=6.2333, lon=1.6000,
         desc="Antigua capital colonial alemana (Klein Popo) sobre el litoral, con arquitectura afro-brasileña y afro-portuguesa de los antiguos comerciantes de esclavos retornados; playa amplia y tranquila junto a la frontera con Benín.",
         credit="Francois Jake Green (Fanfan) · CC BY 3.0", source=W + "Aného%20Beach%2C%20DSC01117%20-%20by%20Fanfan.JPG?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "cultura": "marron", "naturaleza": "verde"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Aflao/Kodjoviakopé (desde Ghana)", "Frontera", 6.1167, 1.2000,
     "Paso urbano integrado en la conurbación Aflao-Lomé, el más transitado del tramo; caminar menos de 1 km entre ambos puestos. Reputación conocida de estafadores de cambio de moneda — usar solo casas de cambio autorizadas."),
    ("Frontera · Salida — Hillacondji/Sanvee-Condji (hacia Benín)", "Frontera", 6.1667, 1.6333,
     "Puesto conjunto (yuxtapuesto) entre Togo y Benín a unos 21 km de Lomé; cruzar por la mañana, el tráfico comercial se satura al mediodía."),
    ("Embajada de España en Accra (acreditada también en Togo)", "Consular", 5.6050, -0.1700,
     "Drake Av. Extension, Airport Residential Area, P.M.B. KA 44, Accra (Ghana). +233 302 77 40 04/05. Togo no tiene embajada española propia; gestionar trámites con margen desde Accra o Lomé."),
    ("CHU Sylvanus Olympio — Lomé", "Hospital", 6.1256, 1.2283,
     "Principal hospital universitario y de referencia del país. Coordenada urbana aproximada."),
    ("Combustible · Lomé", "Combustible", 6.1319, 1.2228,
     "Mejor oferta y calidad del país (Togo Oil, Total, CM Oil); repostar aquí antes o después de cualquiera de las dos fronteras."),
    ("Combustible · Aného / Hillacondji", "Combustible", 6.2333, 1.6000,
     "Estaciones formales en Aného, última plaza con oferta amplia antes de cruzar a Benín."),
    ("Agua potable y de uso general · Lomé", "Agua potable", 6.1319, 1.2228,
     "Agua embotellada sin problema en supermercados; estaciones de servicio y hoteles de Lomé permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Sin marco claro publicado: tratar como prohibido salvo autorización expresa",
                  "Togo no publica un procedimiento civil claro y estable para drones de uso turístico; la Agence Nationale de l'Aviation Civile (ANAC-Togo) es la autoridad de referencia. Norma prudente del proyecto: no volar sin autorización previa por escrito, mantener el equipo declarable y no volar cerca de fronteras, instalaciones militares o del aeropuerto de Lomé.")

STARLINK_CALLOUT = ("warn", "No disponible / estado no confirmado a mediados de 2026",
                     "Togo no figura de forma consistente entre los mercados africanos con Starlink activo en las listas de expansión revisadas a mediados de 2026. Tratarlo como no disponible hasta confirmación oficial y mantener SIM local (Togocom, Moov) como conectividad principal.")

DOG_MATRIX = [
    ("Lomé, Lac Togo, Kpalimé, Aného", "permitido con condiciones", "Correa y sombra; sin restricciones específicas conocidas en estos puntos del itinerario."),
]

SOURCES = [
    ("Saiga Tours · guía de fronteras terrestres de Togo", "https://www.saigatours.com/article/a-guide-to-togos-land-borders"),
    ("Carnet de Passage.org · Togo (sin organización emisora de CPD)", "https://carnetdepassage.org/country/togo/"),
    ("ECOWAS Brown Card · esquema regional de seguro (CEDEAO)", "https://www.browncard.org/"),
    ("Embajada de España en Accra · contacto", "https://www.ayuntamiento-espana.es/embajada-de-espana-en-ghana-accra.html"),
    ("Casa África · Embajada de España en Ghana (Togo)", "https://www.casafrica.es/en/network/embajada-de-espana-en-ghana-togo"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(6.1167, 1.2000), (6.1319, 1.2228), (6.2667, 1.5333), (6.9667, 0.6333), (6.2333, 1.6000), (6.1667, 1.6333)]

HISTORIA_RESUMEN = ("Togo es un país estrecho y alargado que pasó de colonia alemana a mandato repartido entre Francia y Gran Bretaña tras la Primera Guerra Mundial, y que desde 1967 ha estado gobernado casi ininterrumpidamente por la familia Gnassingbé —primero Gnassingbé Eyadéma, "
                     "después su hijo Faure— en uno de los regímenes más longevos y personalistas de África, pese a protestas democráticas recurrentes.")

HISTORIA_SECCIONES = [
    ("El reino de Tado y los pueblos ewe",
     "El territorio fue hogar histórico de los pueblos ewe, organizados en pequeñas jefaturas y reinos como Tado, con una fuerte tradición de vudú (vodun) que tiene aquí uno de sus centros espirituales más importantes de África Occidental, visible hoy en mercados de fetiches como el de Lomé."),
    ("El Togoland alemán y su reparto anglo-francés",
     "Alemania estableció el protectorado de Togoland en 1884, desarrollándolo como colonia modelo con infraestructura ferroviaria y portuaria; tras la derrota alemana en la Primera Guerra Mundial, el territorio fue repartido en 1922 como mandato de la Sociedad de Naciones entre Gran Bretaña (que integró su parte en la Costa de Oro, hoy Ghana) y Francia (que administró el actual Togo), una partición que dividió a comunidades ewe entre dos países distintos."),
    ("Independencia y el ascenso de Eyadéma",
     "Togo se independizó en 1960, pero en 1963 y de nuevo en 1967 vivió golpes de Estado que llevaron al poder al militar Gnassingbé Eyadéma, quien gobernaría durante 38 años, uno de los mandatos más largos de la historia africana, con un sistema de partido dominante y represión de la oposición."),
    ("Situación actual: la dinastía Gnassingbé y protestas recurrentes",
     "Tras la muerte de Eyadéma en 2005, su hijo Faure Gnassingbé asumió el poder en circunstancias controvertidas y ha sido reelegido en sucesivas ocasiones, manteniendo a la familia Gnassingbé al frente del país durante más de cinco décadas en total; el país ha vivido oleadas periódicas de protestas prodemocráticas, la más intensa entre 2017 y 2018, sin lograr hasta ahora una alternancia política."),
]

HISTORIA_FUENTES = [
    ("BBC News · Togo country profile", "https://www.bbc.com/news/world-africa-14106781"),
    ("Encyclopaedia Britannica · Togo, History", "https://www.britannica.com/place/Togo/History"),
    ("International Crisis Group · Togo", "https://www.crisisgroup.org/africa/west-africa/togo"),
]

SPEC = dict(
    slug="togo", name="Togo", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Aflao/Kodjoviakopé (desde Ghana)"),
        ("SALIDA", "Hillacondji/Sanvee-Condji (hacia Benín)"),
        ("SEGURIDAD", "estable en el eje costero · precaución en el norte"),
        ("FRONTERA TERRESTRE", "Aflao muy transitada; Hillacondji puesto conjunto"),
        ("CPD", "Togo no emite CPD propio — tramitarlo en país vecino"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[6.4, 1.2], zoom=8,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Togo se cruza por un tramo costero corto y muy manejable: Lomé como única gran base logística, un desvío cultural a Togoville en el Lac Togo, "
                   "otro de naturaleza a la cascada de Kpimé en las montañas cafeteras de Kpalimé, y la ciudad colonial de Aného antes de cruzar a Benín por Hillacondji. "
                   "El país no exige CPD (no tiene organización emisora propia) pero sí participa del seguro regional CEDEAO."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Ghana y antes de Benín."),
        ("Entrada", "Aflao/Kodjoviakopé desde Ghana: paso urbano más transitado del tramo."),
        ("Salida", "Hillacondji/Sanvee-Condji hacia Benín: puesto conjunto, cruzar por la mañana."),
        ("CPD", "Togo no tiene organización emisora de CPD (AIT/FIA); si el vehículo lo necesita, tramitarlo en Ghana o Benín antes de entrar."),
        ("Seguridad", "Estable en el eje costero (Lomé-Kpalimé-Aného); el paso de Cinkassé hacia Burkina Faso, en el extremo norte, no recomendado por seguridad — fuera del itinerario previsto."),
        ("Comunicaciones", "Starlink sin confirmar en el país; SIM local (Togocom, Moov) como base."),
    ],
    alerts=[
        "CPD: Togo no tiene organización emisora propia — el vehículo debe llevar el CPD tramitado en España (RACE) o, si hiciera falta un documento adicional, gestionarlo en un país vecino con organización AIT/FIA.",
        "Cambio de moneda en Aflao: reputación conocida de estafadores — cambiar solo en casas de cambio autorizadas, nunca con particulares en el paso fronterizo.",
        "Norte del país (Cinkassé, frontera con Burkina Faso): no recomendado por seguridad — completamente fuera del itinerario previsto de este proyecto.",
    ],
    ruta_intro="Tramo costero corto (Lomé y un desvío a Kpalimé) entre las dos fronteras de Ghana y Benín.",
    route_rows=[
        ("Entrada y capital", "Aflao → Lomé", "Base logística única; embajada española acreditada en Accra"),
        ("Desvío cultural", "Lomé → Togoville (Lac Togo)", "Piragua desde Agbodrafo; cuna del vudú togolés"),
        ("Desvío de montaña", "Lomé → Kpalimé → Cascada de Kpimé", "Región cafetera; clima más fresco por altitud"),
        ("Hacia Benín", "Lomé → Aného → Hillacondji", "Ciudad colonial; puesto fronterizo conjunto"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: el eje costero y el desvío a Kpalimé son carretera asfaltada o pista en buen estado.",
    ],
    acampada=[
        "Lomé: alojamientos con parking vigilado, opción más práctica que la acampada libre en la capital.",
        "Kpalimé: pequeños hoteles y auberges de montaña con aparcamiento.",
    ],
    visado=[
        "Visado electrónico (e-Visa) togolés previo obligatorio para ciudadanos españoles; tramitar con antelación y llevar la aprobación impresa y en digital.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
        "Confirmar validez y categoría exacta del e-Visa 30-60 días antes, ya que los requisitos de la subregión cambian con frecuencia.",
    ],
    fronteras_rows=[
        ("Entrada", "Aflao/Kodjoviakopé (Ghana)", "Paso urbano más transitado del tramo; caminar menos de 1 km entre puestos; cuidado con estafadores de cambio."),
        ("Salida", "Hillacondji/Sanvee-Condji (Benín)", "Puesto conjunto (yuxtapuesto); cruzar por la mañana, tráfico comercial satura el mediodía."),
    ],
    vehiculos=[
        "Togo no emite CPD propio: llevar el CPD tramitado en España (RACE) con todos los pares de sellos en regla.",
        "Carte Brune CEDEAO como seguro de responsabilidad civil regional — confirmar que cubre Togo explícitamente.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Sin procedimiento civil turístico claro y estable publicado por la ANAC-Togo: tratar como prohibido sin autorización previa por escrito.",
        "No volar cerca del aeropuerto de Lomé, fronteras (Aflao, Hillacondji) ni instalaciones militares.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado no confirmado a mediados de 2026: revisar el mapa oficial 30-60 días antes de la entrada.",
        "SIM local (Togocom, Moov) como conectividad principal en Lomé y el eje costero.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE).",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "CHU Sylvanus Olympio (Lomé) como referencia hospitalaria del tramo; seguro con evacuación médica imprescindible.",
    ],
    seguridad_intro="Eje costero (Lomé-Kpalimé-Aného) estable con precaución normal; el extremo norte del país, cerca de Burkina Faso, queda fuera del itinerario por la situación de seguridad regional del Sahel.",
    seguridad=[
        "Evitar cualquier desvío hacia el norte del país (Cinkassé, frontera con Burkina Faso) por la situación de seguridad regional.",
        "Cuidado con estafadores de cambio de moneda en el paso de Aflao; usar solo casas de cambio autorizadas.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
    ],
    agua=[
        "Lomé y Aného: agua embotellada en supermercados y tiendas sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio de Lomé y los hoteles de Kpalimé permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km: Aflao → Lomé (~10 km) → Kpalimé (~120 km, desvío) → Aného (~45 km) → Hillacondji (~20 km), todos con estaciones formales.",
        "Repostar en Lomé antes del desvío a Kpalimé: oferta más limitada en el interior montañoso.",
    ],
    pendientes=[
        ("CPD", "Confirmar que el CPD tramitado en España cubre el tránsito por Togo sin trámite adicional"),
        ("Visado", "Tramitar el e-Visa togolés con margen suficiente antes de la entrada"),
        ("Dron", "Contactar con la ANAC-Togo o descartar el vuelo en el país"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Policía 117 · Bomberos 118 · Emergencia consular española (Accra): +233 302 77 40 04.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

# -*- coding: utf-8 -*-
"""RD Congo — tránsito occidental Kinshasa–Matadi–Lufu (ficha completa, 9 sep 2026).
El este del país (Kivu, conflicto M23) queda a ~2.000 km de esta ruta y fuera del itinerario."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Kinshasa (orilla del río Congo)", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-4.4419, lon=15.2663,
         desc="Capital y megaciudad del país, frente a Brazzaville al otro lado del río Congo; embajada de España, aeropuerto internacional y mejor oferta de talleres del tramo, aunque con tráfico denso y logística exigente.",
         credit="EdwinAlden.1995 · CC BY-SA 4.0", source=W + "A%20view%20of%20Congo%20River%20from%20Kinshasa%2C%20Democratic%20Republic%20of%20the%20Congo%20(DRC).jpg?width=900"),
    dict(n=2, name="Boma", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=-5.8500, lon=13.0500,
         desc="Antigua capital colonial del Congo Belga (hasta 1926), con arquitectura de la época y el gran baobab histórico junto al río; parada intermedia en el descenso hacia la costa.",
         credit="Χρίστος Ιμμανοελ · CC BY-SA 4.0", source=W + "Boma%20DR%20Congo.jpg?width=900"),
    dict(n=3, name="Matadi (puente Maréchal Mobutu)", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-5.8167, lon=13.4500,
         desc="Principal puerto fluvial del país sobre el río Congo, con el mayor puente colgante de África central; última gran plaza de servicios antes del breve tramo costero hacia la frontera de Angola.",
         credit="Χρίστος Ιμμανοελ · CC BY-SA 4.0", source=W + "Matadi%20Bridge%20DR%20Congo.jpg?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "cultura": "marron"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Ferry Brazzaville–Kinshasa (desde Congo-Brazzaville)", "Frontera", -4.2800, 15.2800,
     "Cruce fluvial con trámite aduanero en ambos lados; confirmar frecuencia y tarifa del servicio de carga con antelación."),
    ("Frontera · Salida — Lufu/Luvo (hacia Angola)", "Frontera", -5.9167, 13.9667,
     "Cruce a pie/vehículo hacia Luvo (Angola); registro en inmigración de RD Congo, paso de un puente y trámite de entrada angoleño unos 500 m después. Proceso descrito como ágil y sin solicitudes de soborno por overlanders recientes."),
    ("Embajada de España en Kinshasa (también RD Congo y Congo-Brazzaville)", "Consular", -4.3050, 15.3050,
     "Bd. Colonel Tshatshi nº 37, Kinshasa (Gombe). Tel. +243 813 300 061 / 817 008 770 / 818 843 195 · Emergencia consular: +243 819 500 289."),
    ("Hôpital Général de Référence de Kinshasa", "Hospital", -4.3250, 15.3139,
     "Principal hospital de referencia de la capital. Coordenada urbana aproximada."),
    ("Combustible · Kinshasa", "Combustible", -4.4419, 15.2663,
     "Mejor oferta y calidad del país (Total, Engen); repostar a fondo antes del tramo hacia Matadi y la frontera de Angola."),
    ("Combustible · Matadi", "Combustible", -5.8167, 13.4500,
     "Última plaza con oferta formal amplia antes de Lufu/Luvo; repostar a fondo aquí."),
    ("Agua potable y de uso general · Kinshasa", "Agua potable", -4.4419, 15.2663,
     "Agua embotellada sin problema en supermercados de la capital; estaciones de servicio y hoteles de Kinshasa y Matadi permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Sin marco civil turístico claro: tratar como prohibido",
                  "RD Congo no publica un procedimiento civil turístico simple y estable para drones, y el contexto de seguridad del país (aunque no en el corredor occidental) hace que cualquier equipo aéreo sea tratado con máxima sensibilidad por las autoridades. Norma prudente del proyecto: no volar en ningún caso sin autorización previa por escrito, y nunca cerca de fronteras, del río Congo o de instalaciones oficiales.")

STARLINK_CALLOUT = ("ok", "Starlink activo en el país (verificar cobertura exacta antes de entrar)",
                     "RD Congo es uno de los mercados africanos con Starlink activo confirmado a mediados de 2026, con acuerdos recientes de integración satélite-móvil (Airtel). Puede usarse como respaldo de comunicaciones fiable en un país con infraestructura terrestre limitada; revisar el mapa oficial 30-60 días antes por si cambia la cobertura o el marco regulatorio.")

DOG_MATRIX = [
    ("Kinshasa, Boma, Matadi", "permitido con condiciones", "Correa siempre puesta; tráfico muy denso en Kinshasa."),
]

SOURCES = [
    ("WhirledAway · cruce de frontera Lufu (RD Congo) / Luvo (Angola)", "https://whirled-away.com/border-crossing-drc-angola/"),
    ("Kwafrika Travel · guía de visado de RD Congo (2026)", "https://www.kwafrikatravel.com/dr-congo-visa-guide/"),
    ("Critical Threats · Congo War Security Review (agosto 2026)", "https://www.criticalthreats.org/briefs/congo-war-security-review"),
    ("The Ops Con · nivel de amenaza M23 en el este de RD Congo (2026)", "https://theopscon.com/intelligence/eastern-drc-m23-threat-level-june-2026"),
    ("Embajada de España en Kinshasa (RD Congo y Congo-Brazzaville)", "https://www.exteriores.gob.es/Embajadas/kinshasa/es/Paginas/index.aspx"),
    ("Businessday NG · Starlink activo en RD Congo (integración Airtel)", "https://businessday.ng/technology/article/airtel-starlink-launch-direct-to-phone-satellite-service-in-dr-congo/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(-4.2800, 15.2800), (-4.4419, 15.2663), (-5.8500, 13.0500), (-5.8167, 13.4500), (-5.9167, 13.9667)]

HISTORIA_RESUMEN = ("La República Democrática del Congo es el escenario de una de las mayores tragedias coloniales de la historia —el Estado Libre del Congo del rey belga Leopoldo II, un régimen de explotación del caucho que causó millones de muertos— y, tras la independencia en 1960, "
                     "de décadas de dictadura bajo Mobutu Sese Seko y de las llamadas «guerras mundiales africanas» (1996-2003), el conflicto con más víctimas mortales desde la Segunda Guerra Mundial; este proyecto solo transita brevemente por el corredor de Matadi, lejos de las zonas de conflicto activo del este.")

HISTORIA_SECCIONES = [
    ("El reino de Kongo y la cuenca del río Congo",
     "El poderoso reino de Kongo, con el que Portugal mantuvo relaciones diplomáticas desde el siglo XV (incluida la conversión al cristianismo de su rey Nzinga a Nkuwu), dominó la desembocadura del río Congo, la zona que hoy recorre este corredor de tránsito por Matadi, antes de decaer por la presión de la trata de esclavos portuguesa."),
    ("El Estado Libre del Congo de Leopoldo II",
     "En 1885, el rey Leopoldo II de Bélgica obtuvo el territorio como posesión personal —no como colonia del Estado belga— bajo el nombre de Estado Libre del Congo, y lo explotó mediante un régimen de trabajo forzado para la extracción de caucho de una brutalidad extrema, documentada internacionalmente y responsable de la muerte de varios millones de congoleños; la presión internacional forzó a Bélgica a asumir el territorio como colonia oficial en 1908."),
    ("Independencia, Mobutu y el Zaire",
     "El Congo se independizó en 1960 en medio de un caos político que incluyó el asesinato del primer ministro Patrice Lumumba, y tras una crisis de varios años el militar Mobutu Sese Seko tomó el poder en 1965, gobernando durante 32 años bajo un régimen cleptocrático de partido único que renombró el país Zaire, hasta ser derrocado en 1997."),
    ("Las «guerras mundiales africanas» y el conflicto persistente en el este",
     "La caída de Mobutu desencadenó dos guerras sucesivas (1996-97 y 1998-2003) que llegaron a involucrar a nueve países africanos, con un saldo estimado de varios millones de muertos, en su mayoría por hambre y enfermedad, el conflicto más letal desde la Segunda Guerra Mundial; aunque la guerra formal terminó en 2003, el este del país (Kivu) sigue sufriendo un conflicto armado activo entre el ejército, grupos armados locales y fuerzas regionales, un foco de inestabilidad grave completamente ajeno al breve corredor de tránsito de Matadi que contempla este proyecto."),
]

HISTORIA_FUENTES = [
    ("BBC News · DR Congo country profile", "https://www.bbc.com/news/world-africa-13286306"),
    ("Encyclopaedia Britannica · Democratic Republic of the Congo, History", "https://www.britannica.com/place/Democratic-Republic-of-the-Congo/History"),
    ("Council on Foreign Relations · Conflict in the Democratic Republic of Congo", "https://www.cfr.org/global-conflict-tracker/conflict/violence-democratic-republic-congo"),
]

SPEC = dict(
    slug="rd-congo", name="RD Congo (tránsito Matadi)", revision="9 sep 2026",
    sub="Tránsito occidental Kinshasa–Matadi–Lufu · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Ferry Brazzaville–Kinshasa (desde Congo-Brazzaville)"),
        ("SALIDA", "Lufu/Luvo (hacia Angola)"),
        ("SEGURIDAD", "conflicto activo en el ESTE — a ~2.000 km, fuera de esta ruta"),
        ("RUTA", "solo tránsito occidental Kinshasa–Matadi–Boma"),
        ("SEGURO", "seguro local propio — fuera de las zonas CEDEAO/CEMAC"),
        ("REVALIDACIÓN", "30–60 días antes, y de nuevo 72 h antes de cada frontera"),
    ],
    center=[-5.0, 14.3], zoom=7,
    notice="Documento de planificación. Esta ficha cubre EXCLUSIVAMENTE el tránsito occidental Kinshasa-Matadi-Lufu; el este del país (Kivu, conflicto M23) está a unos 2.000 km de esta ruta y queda completamente fuera del itinerario. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("RD Congo se atraviesa exclusivamente por su estrecho corredor occidental —Kinshasa, Matadi, Boma— hasta la frontera de Lufu/Luvo con Angola, un tránsito de pocos días por carretera principal. "
              "El conflicto activo del este del país (M23, Kivu, Goma) está a más de 2.000 km de este corredor y no afecta al itinerario en absoluto; se menciona aquí solo para que quede explícito que esta ficha NO cubre esa región y que no forma parte de la ruta del proyecto bajo ninguna circunstancia."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Congo-Brazzaville y antes de Angola."),
        ("Entrada", "Ferry Brazzaville-Kinshasa sobre el río Congo."),
        ("Salida", "Lufu/Luvo hacia Angola: cruce ágil, sin incidencias reportadas por overlanders recientes."),
        ("Seguridad", "Corredor occidental (Kinshasa-Matadi-Boma) manejable con precaución alta; ESTE del país (M23/Kivu) completamente excluido, a ~2.000 km de esta ruta."),
        ("Seguro", "RD Congo no pertenece a CEDEAO ni a CEMAC: confirmar y contratar el seguro local de responsabilidad civil al entrar."),
        ("Comunicaciones", "Starlink activo; SIM local (Vodacom, Airtel, Orange) como base en Kinshasa."),
    ],
    alerts=[
        "El itinerario cubre EXCLUSIVAMENTE el corredor occidental Kinshasa-Matadi-Lufu; el este del país (Kivu, M23, Goma) está fuera de la ruta bajo cualquier circunstancia — no es una alerta de proximidad, es una región distinta a miles de kilómetros.",
        "Visado: trámite descrito como exigente y con requisitos que cambian con frecuencia — iniciar el proceso con más antelación que en el resto de países del tramo.",
        "Seguro del vehículo: RD Congo queda fuera de las zonas regionales CEDEAO (Brown Card) y CEMAC (Carte Rose) — no dar por hecho ninguna cobertura previa, contratar el seguro local al entrar.",
    ],
    ruta_intro="Tránsito corto y directo por el estrecho corredor occidental del país, entre el río Congo y la frontera de Angola.",
    route_rows=[
        ("Entrada y capital", "Ferry Kinshasa → Kinshasa", "Base logística mayor; embajada española"),
        ("Descenso hacia la costa", "Kinshasa → Boma → Matadi", "Antigua capital colonial; puente sobre el río Congo"),
        ("Hacia Angola", "Matadi → Lufu/Luvo", "Cruce descrito como ágil por overlanders recientes"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: el corredor Kinshasa-Boma-Matadi-Lufu es carretera principal asfaltada.",
    ],
    acampada=[
        "Kinshasa: alojamientos con parking vigilado, opción única frente a la acampada libre en la megaciudad.",
        "Matadi: hoteles con aparcamiento, suficiente para una noche antes de la frontera.",
    ],
    visado=[
        "Visado congoleño (RD Congo) previo obligatorio para ciudadanos españoles, con trámite descrito como exigente — iniciar el proceso con semanas de margen adicional respecto a otros países del tramo.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
        "Llevar copias adicionales de toda la documentación: los controles en el corredor occidental son frecuentes.",
    ],
    fronteras_rows=[
        ("Entrada", "Ferry Brazzaville–Kinshasa (Congo-Brazzaville)", "Cruce fluvial con trámite aduanero en ambos lados; confirmar frecuencia y tarifa de carga con antelación."),
        ("Salida", "Lufu/Luvo (Angola)", "Registro en inmigración de RD Congo, cruce del puente y trámite de entrada angoleño ~500 m después; proceso ágil según overlanders recientes."),
    ],
    vehiculos=[
        "CPD con todos los pares de sellos en regla.",
        "RD Congo no pertenece a CEDEAO ni CEMAC: contratar seguro local de responsabilidad civil al entrar, no dar por válida ninguna Carte Brune o Carte Rose previa.",
        "Carnet de conducir internacional obligatorio; controles frecuentes en todo el corredor occidental.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No volar en ningún caso sin autorización previa por escrito; el contexto de seguridad nacional hace que cualquier equipo aéreo sea tratado con máxima sensibilidad.",
        "Nunca cerca de fronteras, del río Congo o de instalaciones oficiales en Kinshasa, Boma o Matadi.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo confirmado a mediados de 2026, con integración satélite-móvil reciente (Airtel): revisar el mapa oficial 30-60 días antes por posibles cambios.",
        "SIM local (Vodacom, Airtel, Orange) como conectividad complementaria en Kinshasa.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE).",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "Hôpital Général de Référence de Kinshasa como mejor referencia hospitalaria del tramo; seguro con evacuación médica real imprescindible.",
    ],
    seguridad_intro="El corredor occidental (Kinshasa-Matadi-Boma-Lufu) es manejable con precaución alta y sin relación alguna con el conflicto del este del país, a unos 2.000 km de distancia.",
    seguridad=[
        "No hay ninguna razón operativa para acercarse al este del país (Kivu, Goma): queda completamente fuera de cualquier variante razonable de esta ruta.",
        "Extremar la seguridad de convoy y check-in diario en Kinshasa por la densidad de tráfico y el tamaño de la ciudad.",
        "Llevar siempre el certificado de fiebre amarilla y copias completas de la documentación del vehículo, dado el número de controles en el corredor.",
    ],
    agua=[
        "Kinshasa: agua embotellada en supermercados sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio y hoteles de Kinshasa y Matadi permiten llenar el depósito con manguera; confirmar en recepción. Entre Boma y Lufu no dar por hecho ningún punto adicional.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el corredor previsto: Kinshasa → Boma (~350 km) → Matadi (~50 km) → Lufu/Luvo (~90 km), con estaciones formales en cada núcleo urbano.",
        "Repostar a fondo en Kinshasa y de nuevo en Matadi: última plaza con oferta amplia antes de cruzar a Angola.",
    ],
    pendientes=[
        ("Visado", "Iniciar el trámite de RD Congo con semanas de margen adicional por su complejidad"),
        ("Seguro local", "Confirmar dónde y cómo contratarlo al entrar por el ferry de Kinshasa"),
        ("Ferry Brazzaville-Kinshasa", "Coordinar con la ficha de Congo-Brazzaville: frecuencia, tarifa y embarque del vehículo"),
        ("Dron", "Descartar el vuelo en el país salvo autorización escrita expresa"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Cubre exclusivamente el corredor occidental de tránsito; no aplica en absoluto al este del país.",
    emergency="Emergencia consular española (Kinshasa): +243 819 500 289.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

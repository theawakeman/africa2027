# -*- coding: utf-8 -*-
"""Sudán — ficha de decisión (9 sep 2026): país NO viable para tránsito mientras dure la guerra civil."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Jartum (referencia — NO visitar)", cat="Referencia · conflicto", prio="No planificable", dog="no aplicable", time="—",
         lat=15.5007, lon=32.5599,
         desc="Capital y escenario principal de los combates entre el Ejército sudanés (SAF) y las Fuerzas de Apoyo Rápido (RSF) desde abril de 2023; incluida aquí únicamente como referencia geográfica del conflicto, sin ninguna intención de visita mientras dure la guerra.",
         credit="NASA (ISS-64) · dominio público", source=W + "ISS-64%20Khartoum%2C%20Sudan.jpg?width=900"),
    dict(n=2, name="Wadi Halfa (referencia — cruce histórico a Egipto)", cat="Referencia · conflicto", prio="No planificable", dog="no aplicable", time="—",
         lat=21.8000, lon=31.3500,
         desc="Localidad junto al lago Nasser que históricamente conectaba Sudán con Egipto por ferry; en teoría fuera de las zonas de combate más intensas, pero la fiabilidad general del país durante el conflicto hace que el proyecto no la considere una opción de tránsito real a día de hoy.",
         credit="David Stanley from Nanaimo, Canada · CC BY 2.0", source=W + "Traditional%20House%20in%20Wadi%20Halfa%2C%20Sudan.jpg?width=900"),
]

_CAT_COLOR = {"referencia · conflicto": "gris"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "gris")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Metema/Gallabat (con Etiopía) — NO USAR", "Frontera", 12.9667, 36.2000,
     "Sin fiabilidad operativa mientras dure el conflicto; no forma parte de ninguna variante de la ruta del proyecto."),
    ("Frontera · Qustul/Wadi Halfa (con Egipto) — NO USAR", "Frontera", 21.9333, 31.3333,
     "Cruce histórico hacia Egipto por el lago Nasser; descartado como opción de tránsito mientras persista la guerra civil."),
    ("Embajada de España en Jartum (sin actividad operativa recomendada)", "Consular", 15.5900, 32.5300,
     "La representación diplomática española en Sudán queda fuera de cualquier plan de contingencia de este proyecto mientras dure el conflicto; en caso de necesidad, contactar con el Ministerio de Asuntos Exteriores en España (+34 91 379 17 00, línea de emergencia consular)."),
]

DRONE_CALLOUT = ("danger", "No aplicable — país excluido de la ruta",
                  "Cualquier consideración sobre drones en Sudán queda anulada por el estado de guerra civil activa: no se contempla ningún vuelo, tránsito ni presencia del equipo de expedición en el país mientras dure el conflicto.")

STARLINK_CALLOUT = ("danger", "No aplicable — país excluido de la ruta",
                     "Sudán figura entre los países africanos sin fecha prevista de licencia para Starlink, pero esto es irrelevante para el proyecto: no se planifica ninguna presencia en el país mientras dure la guerra civil.")

DOG_MATRIX = [
    ("Todo el país", "no aplicable", "Sudán queda excluido de cualquier variante de la ruta; no aplica matriz canina real."),
]

SOURCES = [
    ("Wikipedia · Sudanese civil war (2023–present), estado actualizado 2026", "https://en.wikipedia.org/wiki/Sudanese_civil_war_(2023%E2%80%93present)"),
    ("Sudans Post · mapa de control territorial del conflicto (junio 2026)", "https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-june-21-2026/"),
    ("armedconflicts.org · Sudan Civil War, seguimiento en vivo 2026", "https://armedconflicts.org/sudan-civil-war.html"),
    ("Overlanding Association · Shipping around Ethiopia (alternativas marítimas al corredor de Sudán)", "https://overlandingassociation.org/overland-wiki/shipping-around-ethiopia/"),
    ("Ministerio de Asuntos Exteriores de España · recomendaciones de viaje Sudán", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/DetalleRecomendacion.aspx?pais=SUDAN"),
]

CORRIDOR = []

HISTORIA_RESUMEN = ("Sudán fue cuna de reinos nubios milenarios con más pirámides que Egipto y cruce de caminos entre el mundo árabe y el África subsahariana; su independencia en 1956 abrió décadas de golpes militares y guerras civiles "
                     "que culminaron en la partición de 2011 (nace Sudán del Sur) y, desde abril de 2023, en una nueva guerra civil entre el Ejército y las Fuerzas de Apoyo Rápido que hace inviable cualquier tránsito por el país.")

HISTORIA_SECCIONES = [
    ("Nubia: más pirámides que Egipto",
     "Mucho antes de la llegada del islam, el valle del Nilo sudanés albergó los reinos nubios de Kerma, Napata y Meroe, que llegaron a gobernar el propio Egipto como la XXV dinastía faraónica (siglo VIII-VII a.C.). "
     "Meroe, cerca de la actual Jartum, reúne hoy más de 200 pirámides —más que todo Egipto—, un patrimonio arqueológico de primer orden que la guerra actual mantiene fuera del alcance de cualquier visitante."),
    ("Islamización, dominio turco-egipcio y el Mahdi",
     "El islam se extendió por el norte de Sudán desde el siglo VII, y el país pasó a integrarse en la órbita otomano-egipcia en el siglo XIX. En 1881, el líder religioso Muhammad Ahmad se proclamó Mahdi (\"el guiado\") "
     "y lideró una revuelta que expulsó temporalmente a egipcios y británicos, estableciendo un Estado islámico independiente hasta que una expedición angloegipcia lo reconquistó en 1898, inaugurando el condominio anglo-egipcio de Sudán."),
    ("Independencia, guerras civiles y la partición de 2011",
     "Sudán se independizó en 1956, pero desde el mismo momento de la independencia el sur, de mayoría cristiana y animista, se sintió marginado por el norte árabe-musulmán, desencadenando dos guerras civiles sucesivas (1955-1972 y 1983-2005) "
     "entre las más largas y mortíferas de África. Un referéndum pactado en el acuerdo de paz de 2005 llevó a la independencia de Sudán del Sur en 2011, aunque el propio Sudán siguió sufriendo el conflicto de Darfur, "
     "activo desde 2003 y marcado por acusaciones de genocidio contra las milicias yanyauid, antecesoras directas de las actuales Fuerzas de Apoyo Rápido."),
    ("Situación actual: la guerra civil de 2023",
     "Tras la caída del dictador Omar al-Bashir en 2019 y una frágil transición hacia un gobierno civil, la rivalidad entre el Ejército sudanés y las Fuerzas de Apoyo Rápido (la milicia paramilitar heredera de los yanyauid) estalló en una guerra abierta en abril de 2023. "
     "El conflicto ha provocado la mayor crisis de desplazamiento del mundo, con hambruna declarada en varias zonas, y sigue sin resolución a mediados de 2026 — el motivo por el que este proyecto excluye Sudán por completo y busca una alternativa marítima vía Yibuti para conectar Etiopía con Egipto."),
]

HISTORIA_FUENTES = [
    ("BBC News · Sudan country profile", "https://www.bbc.com/news/world-africa-14094995"),
    ("Encyclopaedia Britannica · Sudan, History", "https://www.britannica.com/place/Sudan/History"),
    ("UNESCO · Sitios arqueológicos de la isla de Meroe, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/1336/"),
    ("Wikipedia · Sudanese civil war (2023–present)", "https://en.wikipedia.org/wiki/Sudanese_civil_war_(2023%E2%80%93present)"),
]

SPEC = dict(
    slug="sudan", name="Sudán", revision="9 sep 2026",
    sub="PUNTO CRÍTICO DEL CORREDOR DE REGRESO · país excluido mientras dure la guerra civil",
    chips=[
        ("ESTADO", "GUERRA CIVIL ACTIVA desde abril de 2023 — sin alto el fuego"),
        ("RUTA", "país EXCLUIDO de toda variante mientras dure el conflicto"),
        ("ALTERNATIVA ADOPTADA", "Etiopía → Yibuti → envío marítimo (RoRo/contenedor) → Egipto o Europa"),
        ("REVISIÓN", "revalidar el estado del conflicto 30–60 días antes del tramo final"),
    ],
    center=[15.5, 32.5], zoom=5,
    notice="Esta ficha documenta una DECISIÓN DE RUTA, no un itinerario: Sudán queda excluido de cualquier variante del viaje mientras persista la guerra civil. Revisar el estado del conflicto antes de cualquier replanteamiento.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("Sudán vive desde abril de 2023 una guerra civil entre el Ejército sudanés (SAF) y las Fuerzas de Apoyo Rápido (RSF) que, a mediados de 2026, sigue sin alto el fuego: ambos bandos han descartado oficialmente una salida negociada. "
              "El SAF recuperó el control de Jartum en 2025, pero las RSF mantienen el dominio de gran parte de Darfur y Kordofán, con combates activos en curso (por ejemplo, en torno a El Fasher). El resultado humanitario es catastrófico: "
              "unos 14 millones de personas desplazadas, 4,5 millones de ellas como refugiadas fuera del país, inseguridad alimentaria severa y hambruna en amplias zonas. Ninguna frontera de Sudán es fiable ni planificable en este contexto. "
              "Decisión del proyecto: Sudán queda completamente excluido de cualquier variante de la ruta —ni tránsito, ni pernocta, ni frontera— mientras dure el conflicto. La alternativa adoptada para conectar Etiopía con Egipto es "
              "desviar la ruta por el este: salir de Etiopía hacia Yibuti por Galafi y, desde el puerto de Yibuti, contratar un envío marítimo (RoRo o contenedor) del vehículo hacia Egipto —vía Arabia Saudí en tránsito— o directamente hacia Europa, "
              "con la tripulación viajando por separado en avión. Esta decisión debe revisarse activamente 30-60 días antes del tramo final del viaje: solo si el conflicto se resolviera con garantías sólidas y sostenidas en el tiempo cabría "
              "reevaluar el corredor terrestre clásico Etiopía-Sudán-Egipto; mientras tanto, la ruta de referencia del proyecto es la marítima vía Yibuti — ver las fichas de Etiopía, Yibuti y Egipto."),
    facts=[
        ("Estado", "Guerra civil activa desde abril de 2023, sin alto el fuego a la fecha de esta revisión (sep. 2026)."),
        ("Ruta", "País EXCLUIDO por completo de cualquier variante de la ruta mientras dure el conflicto."),
        ("Fronteras", "Ninguna frontera de Sudán se considera fiable ni planificable en este contexto."),
        ("Alternativa adoptada", "Etiopía → Galafi → Yibuti → envío marítimo RoRo/contenedor → Egipto o Europa."),
        ("Revisión", "Revalidar el estado del conflicto 30-60 días antes del tramo final; solo una resolución sólida y sostenida justificaría reconsiderar el corredor terrestre."),
    ],
    alerts=[
        "Guerra civil activa en todo el país: no planificar ningún tránsito, pernocta ni cruce fronterizo por Sudán bajo ninguna circunstancia mientras dure el conflicto.",
        "Ninguna de las dos fronteras relevantes para este proyecto (Metema/Gallabat con Etiopía, Qustul/Wadi Halfa con Egipto) se considera operativa ni fiable.",
        "La alternativa marítima vía Yibuti implica separar temporalmente vehículo y tripulación: el vehículo viaja por barco y las personas por avión — planificar esta logística con antelación suficiente.",
    ],
    ruta_intro="No existe ruta terrestre planificada por Sudán. Esta ficha documenta la decisión de excluir el país y la alternativa marítima adoptada para seguir conectando el corredor de regreso.",
    route_rows=[
        ("Decisión", "Sudán completo", "EXCLUIDO — ver decisión de ruta"),
        ("Alternativa", "Adís Abeba/Etiopía → Galafi → Yibuti", "Salida terrestre hacia el puerto de embarque"),
        ("Alternativa", "Puerto de Yibuti → mar → Egipto/Europa", "RoRo o contenedor; tripulación por avión"),
    ],
    offroad=[],
    acampada=[],
    visado=[
        "No aplicable: no se planifica ninguna entrada a Sudán mientras dure el conflicto.",
    ],
    fronteras_rows=[
        ("Entrada (no usar)", "Metema/Gallabat (Etiopía)", "Sin fiabilidad operativa — excluida de la ruta."),
        ("Salida (no usar)", "Qustul/Wadi Halfa (Egipto)", "Cruce histórico por el lago Nasser — descartado mientras dure el conflicto."),
    ],
    vehiculos=[
        "No aplicable dentro de Sudán: ningún trámite de CPD, seguro o importación temporal se gestiona para este país mientras dure la exclusión de ruta.",
        "La logística de vehículo relevante es la del envío marítimo desde Yibuti — ver la ficha de Yibuti y de Egipto para los trámites de origen y destino.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=["No aplicable — país excluido de la ruta."],
    starlink_callout=STARLINK_CALLOUT,
    starlink=["No aplicable — país excluido de la ruta."],
    perro_intro=["No aplicable — país excluido de la ruta."],
    dog_matrix=DOG_MATRIX,
    salud=["No aplicable — país excluido de la ruta; ver la ficha de Etiopía y de Egipto para la cobertura sanitaria del tramo real del proyecto."],
    seguridad_intro="Sudán es, junto con Mali, Libia y Somalia, uno de los países que este proyecto excluye por completo del itinerario por conflicto armado activo.",
    seguridad=[
        "No planificar ningún tránsito, pernocta ni cruce fronterizo por Sudán mientras dure la guerra civil.",
        "Monitorizar la evolución del conflicto de forma periódica durante toda la planificación del viaje, no solo en la revisión final de 30-60 días.",
        "Ante cualquier duda sobre si el conflicto se ha resuelto lo suficiente como para reconsiderar el corredor terrestre, tratar la pregunta como abierta y mantener por defecto la alternativa marítima vía Yibuti.",
    ],
    agua=["No aplicable — país excluido de la ruta."],
    combustible=["No aplicable — país excluido de la ruta."],
    pendientes=[
        ("Estado del conflicto", "Revisar 30-60 días antes del tramo final si hay alto el fuego sólido y sostenido"),
        ("Envío marítimo", "Confirmar la decisión definitiva (Egipto directo vía Arabia Saudí, o directamente a Europa) según la ficha de Yibuti"),
        ("Contingencia", "Mantener siempre la alternativa marítima como plan por defecto salvo resolución clara y verificada del conflicto"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha documenta una decisión de exclusión de ruta, no un itinerario de viaje; revisar el estado del conflicto antes de cualquier replanteamiento.",
    emergency="Sin representación operativa recomendada en el país durante el conflicto. Ministerio de Asuntos Exteriores de España, línea de emergencia consular: +34 91 379 17 00.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

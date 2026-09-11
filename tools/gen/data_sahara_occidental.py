# -*- coding: utf-8 -*-
"""Sáhara Occidental (tránsito) — ficha completa (9 sep 2026)."""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Laayoune (El Aaiún)", cat="Ciudad · servicios", prio="Media", dog="permitido", time="1 noche",
         lat=27.1418, lon=-13.1873,
         desc="Mayor ciudad del Sáhara Occidental bajo administración marroquí; última base con hospital de referencia, talleres, bancos y combustible antes del tramo semidesértico hacia Dakhla. Catedral de estilo colonial español como referencia urbana.",
         credit="Bjørn Christian Tørrissen · CC BY-SA 3.0", source=W + "Laayoune%20Cathedral%202011.jpg?width=900"),
    dict(n=2, name="Laguna de Dakhla", cat="Naturaleza · deporte", prio="Media", dog="permitido", time="1–2 días",
         lat=23.6900, lon=-15.9500,
         desc="Península y laguna de aguas planas, referencia mundial de kitesurf y windsurf; ambiente de viajeros y overlanders con explanadas para pernoctar. Punto de descanso recomendado antes del tramo final a Guerguerat.",
         credit="Trincerone · CC BY-SA 4.0", source=W + "FortecolorWestsaharaIII-36.jpg?width=900"),
    dict(n=3, name="Guerguerat — paso fronterizo", cat="Frontera", prio="Alta", dog="permitido con condiciones", time="4–6 h",
         lat=21.3400, lon=-16.9500,
         desc="Único paso terrestre hacia Mauritania: control marroquí, franja de tierra de nadie sin asfaltar (con cambistas informales) y control mauritano con varios edificios y controles por nacionalidad. Calcular 4–6 horas y no cruzar después de mediodía para evitar el cierre nocturno del lado mauritano.",
         credit="Wikimedia Commons · CC BY-SA 2.0", source=W + "Guerguerat%20border%20crossing.jpg?width=900"),
]

_CAT_COLOR = {
    "ciudad · servicios": "azul", "naturaleza · deporte": "turquesa", "frontera": "gris",
}
import re as _re
for _p in POIS:
    _url = _p.pop("source")
    _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower()
    _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Salida — Guerguerat / Punto Kilométrico 55", "Frontera", 21.3400, -16.9500,
     "Corredor único hacia Nuadibú (Mauritania). Llevar dírhams o euros en efectivo (no dólares), agua y paciencia; contratar eVisa mauritana con antelación (no hay visado a la llegada). No fotografiar en el paso."),
    ("Delegación de Aguas y Bosques — Laayoune", "Servicio", 27.1500, -13.2000,
     "Punto de referencia para confirmar accesos a zonas protegidas costeras del tramo Tarfaya-Dakhla. Coordenada urbana aproximada; confirmar por teléfono antes de desplazarse."),
    ("Hospital Regional Hassan II — Laayoune", "Hospital", 27.1450, -13.1950,
     "Hospital de referencia de la región; capacidad limitada para politraumatismos graves — el seguro de evacuación es imprescindible en este tramo. Coordenada urbana aproximada."),
    ("Centro de salud — Dakhla", "Hospital", 23.6845, -15.9350,
     "Recurso sanitario urbano de Dakhla; para urgencias graves, evacuación hacia Laayoune o Agadir. Coordenada urbana aproximada."),
    ("Consulado de España más próximo — Agadir (referencia)", "Consular", 30.4202, -9.5982,
     "Sin representación consular española en Laayoune ni Dakhla: el consulado de Agadir y la embajada en Rabat son las referencias operativas para todo el tramo del Sáhara Occidental."),
    ("Combustible · Laayoune Plage", "Combustible", 27.1100, -13.4200,
     "Primera estación tras salir de Laayoune, ~20 km al sur. Diésel estándar marroquí."),
    ("Combustible · Lemsid", "Combustible", 26.7200, -13.6300,
     "~80 km al sur de Laayoune Plage; punto de repostaje intermedio confirmado por overlanders (Horizons Unlimited, iOverlander)."),
    ("Combustible · Boujdour", "Combustible", 26.1258, -14.4900,
     "~80 km al sur de Lemsid; última localidad con oferta amplia antes del tramo largo hacia Dakhla. Repostar aquí siempre, aunque el depósito no esté a la mitad."),
    ("Combustible · cruce de Dakhla (Dakhla Junction)", "Combustible", 23.7350, -15.8700,
     "~290 km al sur de Boujdour; dos estaciones en la rotonda de acceso a la península de Dakhla, confirmadas y activas en iOverlander. Tramo previo sin nada intermedio salvo viento."),
    ("Combustible · Bir Gandouz", "Combustible", 21.0170, -16.3170,
     "Última localidad con estación fiable antes de Guerguerat (~80 km); el tramo Dakhla-Bir Gandouz (~250 km) es el más largo sin repostaje garantizado de todo Marruecos/Sáhara — llegar con depósito lleno desde Dakhla."),
    ("Agua potable · Dakhla y Laayoune (supermercados y garrafas)", "Agua potable", 23.6845, -15.9350,
     "Agua embotellada disponible en Laayoune y Dakhla; fuera de estas dos ciudades, prácticamente inexistente en el tramo costero. Cargar reserva completa en cada una antes de continuar."),
]

DRONE_CALLOUT = ("danger", "Mismo régimen restrictivo que Marruecos, con sensibilidad añadida",
                  "El Sáhara Occidental está bajo administración marroquí y es zona de disputa territorial con el Frente Polisario: además de la práctica habitual de confiscación de drones en aduana, volar aquí sin autorización expresa tiene una sensibilidad política añadida (infraestructura del muro/berma, zonas próximas a la franja este). No introducir el dron en este tramo sin autorización previa por escrito de la DGAC.")

STARLINK_CALLOUT = ("danger", "Mismo estado que Marruecos: sin licencia activa",
                     "El Sáhara Occidental comparte el régimen regulatorio marroquí de telecomunicaciones. A fecha de esta revisión no hay servicio Starlink activo; la cobertura móvil (Maroc Telecom/Orange/inwi) es buena en Laayoune y Dakhla, pero se degrada notablemente en el tramo Dakhla-Guerguerat. Llevar mensajería satelital independiente para ese tramo.")

DOG_MATRIX = [
    ("Paso de Guerguerat", "permitido con condiciones", "Llevar cartilla/pasaporte del perro visible; el control mauritano puede pedir certificado sanitario al otro lado."),
    ("Laayoune, Dakhla, corredor costero", "permitido", "Sin restricción específica publicada."),
]

SOURCES = [
    ("Wikivoyage · Guerguerat", "https://en.wikivoyage.org/wiki/Guerguerat"),
    ("Wikipedia · Guerguerat", "https://en.wikipedia.org/wiki/Guerguerat"),
    ("Mind of a Hitchhiker · cruce Dakhla–Nuadibú a través de la berma", "https://mindofahitchhiker.com/through-the-berm-mauritania-border-crossing-with-western-sahara-morocco/"),
    ("Away with the Steiners · cruce Dakhla–Nuadibú en vehículo propio", "https://awaywiththesteiners.com/morocco-mauritania-border-crossing/"),
    ("Spirit Travelers · cómo cruzar la frontera Marruecos–Mauritania", "https://spirit-travelers.com/en/how-to-cross-the-border-morocco-mauritania/"),
    ("MAEC España · recomendaciones de viaje (Marruecos, aplicable al tránsito)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Marruecos"),
    ("Starlink · mapa de disponibilidad", "https://starlink.com/map"),
    ("Sahara Overland · combustible en la Atlantic Highway (Laayoune-Dakhla-Guerguerat)", "https://sahara-overland.com/2020/04/03/a-if-for-atlantic-highway/"),
    ("Horizons Unlimited · gasolineras en el Sáhara Occidental (foro overlander)", "https://www.horizonsunlimited.com/hubb/morocco/fuel-stations-in-western-sahara-89474"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [
    (27.9394, -12.9231),  # enlace con Tarfaya (Marruecos)
    (27.1418, -13.1873),  # Laayoune
    (23.6900, -15.9500),  # Dakhla laguna
    (21.3400, -16.9500),  # Guerguerat
]

HISTORIA_RESUMEN = ("El Sáhara Occidental es el último gran contencioso de descolonización pendiente en África: territorio nómada saharaui bajo dominio español hasta 1975, fue ocupado por Marruecos tras la retirada de España en plena Marcha Verde, "
                     "lo que desencadenó una guerra con el Frente Polisario y un exilio saharaui a Argelia que se prolonga hasta hoy, con un referéndum de autodeterminación prometido por la ONU en 1991 y jamás celebrado.")

HISTORIA_SECCIONES = [
    ("Pueblo nómada saharaui y el Sáhara español",
     "El territorio estuvo habitado tradicionalmente por tribus nómadas saharauis de origen árabe-bereber, organizadas en torno al pastoreo de camellos y rutas comerciales transaharianas. España estableció su colonia del Sáhara Español en 1884, gestionándolo durante casi un siglo como una posesión marginal hasta el descubrimiento de grandes yacimientos de fosfatos en Bu Craa en los años sesenta."),
    ("La retirada española y la Marcha Verde de 1975",
     "Ante la presión internacional por la descolonización y la debilidad del régimen franquista en sus últimos meses, España acordó en los Acuerdos de Madrid de 1975 ceder la administración del territorio a Marruecos y Mauritania, tras la masiva Marcha Verde marroquí; España se retiró sin celebrar el referéndum de autodeterminación que había prometido, dejando al pueblo saharaui sin ser consultado."),
    ("La guerra con el Frente Polisario y la partición",
     "El Frente Polisario, movimiento independentista saharaui, proclamó la República Árabe Saharaui Democrática y libró una guerra contra Marruecos y Mauritania; esta última se retiró del conflicto en 1979, y Marruecos ocupó también su parte, construyendo un extenso muro de arena (el «berm») que separa hoy el territorio bajo control marroquí (donde transcurre el corredor turístico) de la franja oriental bajo control del Polisario, sembrada de minas."),
    ("Situación actual: alto el fuego frágil y estatus sin resolver",
     "Desde 1991 rige un alto el fuego supervisado por la misión de la ONU (MINURSO), pero el referéndum de autodeterminación prometido nunca se celebró por el desacuerdo sobre el censo de votantes, y en 2020 se reanudaron esporádicamente las hostilidades de baja intensidad en la zona de Guerguerat. Decenas de miles de refugiados saharauis siguen viviendo en campamentos en Tinduf (Argelia) mientras la comunidad internacional permanece dividida sobre el reconocimiento del territorio."),
]

HISTORIA_FUENTES = [
    ("BBC News · Western Sahara profile", "https://www.bbc.com/news/world-africa-14115273"),
    ("United Nations · MINURSO", "https://minurso.unmissions.org/"),
    ("Encyclopaedia Britannica · Western Sahara", "https://www.britannica.com/place/Western-Sahara"),
]

SPEC = dict(
    slug="sahara-occidental", name="Sáhara Occidental (tránsito)", revision="9 sep 2026",
    sub="Corredor costero · frontera de Guerguerat · logística",
    chips=[
        ("ENTRADA", "Tarfaya → Laayoune"),
        ("SALIDA", "Guerguerat → Nuadibú (Mauritania)"),
        ("SEGURIDAD", "precaución · no abandonar el corredor costero"),
        ("FRONTERA TERRESTRE", "Guerguerat: único paso, 4–6 h"),
        ("VISADO", "cubierto por la entrada marroquí"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[24.5, -14.5], zoom=6,
    notice="Territorio no autónomo bajo administración marroquí de facto en el corredor costero. Este documento cubre exclusivamente el tránsito por la carretera N1 Tarfaya–Laayoune–Dakhla–Guerguerat; no se contempla salir del corredor asfaltado.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("El Sáhara Occidental se recorre íntegramente por el corredor costero asfaltado (N1) entre Tarfaya y el paso de Guerguerat, límite con Mauritania. "
                   "No es territorio de exploración off-road para este proyecto: la franja este del territorio, más allá de la carretera y su entorno inmediato, "
                   "está afectada por minas terrestres desde el conflicto con el Frente Polisario y queda excluida sin excepción."),
    facts=[
        ("Ventana prevista", "Enero de 2027, tramo de 2-3 días dentro del corredor de bajada."),
        ("Entrada", "Continuidad terrestre desde Tarfaya (Marruecos); sin control internacional adicional."),
        ("Salida", "Paso de Guerguerat hacia Nuadibú (Mauritania): 4-6 horas, dos controles + tierra de nadie."),
        ("Visado", "Cubierto por la exención de entrada marroquí; para Mauritania se necesita eVisa previa, no hay visado a la llegada."),
        ("Seguridad", "Precaución general; nunca abandonar la carretera asfaltada ni las pistas balizadas del corredor por riesgo de minas en la franja este."),
        ("Comunicaciones", "Buena cobertura móvil en Laayoune y Dakhla; se degrada en el tramo final hacia Guerguerat."),
    ],
    alerts=[
        "Minas terrestres: la franja este del territorio (más allá del corredor costero y su entorno inmediato) está señalada como zona minada — bajo ninguna circunstancia salir de la carretera o pista oficial.",
        "Guerguerat: llevar dírhams/euros en efectivo, no dólares; la eVisa mauritana debe estar tramitada ANTES de llegar, ya no existe visado a la llegada.",
        "No fotografiar en el entorno del paso fronterizo ni de instalaciones del muro/berma.",
        "Planificar el cruce de Guerguerat por la mañana: el lado mauritano cierra hacia las 17:00 y los trámites pueden alargarse varias horas.",
    ],
    ruta_intro="Tramo lineal de norte a sur por la N1; no hay bifurcaciones relevantes para el proyecto.",
    route_rows=[
        ("Entrada y Laayoune", "Tarfaya → Laayoune", "Repostaje, provisiones y revisión de vehículos antes del tramo largo"),
        ("Corredor Laayoune–Dakhla", "~550 km de carretera asfaltada", "Tramo largo sin apenas núcleos intermedios; salir con depósitos llenos"),
        ("Dakhla y península", "Laguna, kitesurf, descanso", "Buena base para un día de pausa antes de la frontera"),
        ("Tramo final y frontera", "Dakhla → Guerguerat", "Reservar la mañana completa; no intentar el cruce por la tarde"),
    ],
    offroad=[
        "No se contemplan pistas off-road propias en este tramo: el objetivo es el corredor asfaltado seguro. Cualquier desvío hacia el interior queda descartado por el riesgo de minas.",
    ],
    acampada=[
        "Explanadas junto a la laguna de Dakhla: uso habitual entre overlanders y kitesurfistas; confirmar tranquilidad y presencia de otros viajeros antes de pernoctar.",
        "Evitar pernoctar en el tramo Laayoune–Dakhla fuera de núcleos urbanos; distancias largas sin servicios ni vigilancia.",
    ],
    visado=[
        "Sin trámite adicional respecto a la entrada marroquí para el tránsito por el corredor.",
        "Para Mauritania: eVisa obligatoria tramitada con antelación (desde 2025 no hay visado a la llegada en Guerguerat); llevar copia impresa y digital.",
    ],
    fronteras_rows=[
        ("Salida del bloque Marruecos/Sáhara", "Guerguerat (Punto Kilométrico 55)", "Control marroquí de salida + ~3-5 km de tierra de nadie sin asfaltar + control mauritano por nacionalidades; 4-6 h en total."),
    ],
    vehiculos=[
        "El vehículo mantiene la TVIP obtenida en Tánger Med hasta la salida por Guerguerat; comprobar que quede registrada la salida.",
        "En el lado mauritano se emite un nuevo permiso de importación temporal (mínimo 10 días) y se debe contratar seguro local en el propio paso.",
        "Llevar combustible con margen: pocas estaciones fiables entre Dakhla y la frontera.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Aplican las mismas restricciones que en Marruecos, agravadas por la sensibilidad territorial: no volar cerca del paso fronterizo, del muro/berma ni de instalaciones militares.",
        "Mantener el dron declarado en depósito aduanero o fuera del país durante todo este tramo si no hay autorización escrita previa.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Sin servicio activo a fecha de esta revisión; usar SIM local marroquí como conectividad principal en Laayoune y Dakhla.",
        "Llevar mensajería satelital independiente para el tramo Dakhla-Guerguerat, donde la cobertura móvil se degrada.",
    ],
    perro_intro=[
        "Sin requisitos adicionales al tránsito marroquí para entrar en este tramo.",
        "Para la salida hacia Mauritania: llevar pasaporte/cartilla del perro visible; el control mauritano en Guerguerat puede solicitar certificado sanitario.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Golpe de calor como riesgo principal en el tramo Laayoune-Dakhla-Guerguerat: agua abundante, sombra y horarios de conducción que eviten las horas centrales.",
        "Seguro con evacuación médica: la capacidad hospitalaria del territorio es limitada: Laayoune y Dakhla cubren urgencias básicas, no politraumatismos graves.",
    ],
    seguridad_intro="El corredor costero es la única zona recomendada; el resto del territorio queda fuera del itinerario por la combinación de disputa territorial y riesgo de minas.",
    seguridad=[
        "Nunca abandonar la carretera asfaltada ni las pistas balizadas del corredor.",
        "No fotografiar infraestructura militar, el muro/berma ni el entorno inmediato del paso fronterizo.",
        "Compartir plan diario y hora prevista de cruce de Guerguerat con la base en España antes de iniciar el tramo final.",
    ],
    agua_combustible_alerta="El tramo Dakhla → Bir Gandouz → Guerguerat (~330 km en total) es el más largo de todo el corredor Marruecos/Sáhara Occidental sin combustible garantizado: salir de Dakhla con el depósito lleno y, si es posible, un bidón de reserva. Agua potable prácticamente inexistente fuera de Laayoune y Dakhla: cargar toda la reserva en esas dos ciudades.",
    agua=[
        "Laayoune y Dakhla: agua embotellada en supermercados; sin garantía fiable fuera de esas dos ciudades en todo el corredor costero.",
        "Cargar la reserva completa de los vehículos (mínimo 20-30 l) en cada una de las dos ciudades antes de continuar.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio Afriquia/Shell de Laayoune y Dakhla y algún camping de Dakhla (Point Dakhla, La Sarga) aceptan llenar el depósito; entre Boujdour y Bir Gandouz no dar por hecho ningún punto — llenar a tope en cada una de las dos ciudades antes de salir.",
    ],
    combustible=[
        "Laayoune → Laayoune Plage (20 km) → Lemsid (80 km) → Boujdour (80 km): tramo bien cubierto, repostar en cada parada aunque no haga falta.",
        "Boujdour → cruce de Dakhla (290 km): el tramo intermedio más largo del corredor; no hay nada fiable entre medias salvo viento — salir de Boujdour con el depósito lleno.",
        "Dakhla → Bir Gandouz (~250 km) → Guerguerat (~80 km): tramo crítico final; estaciones antiguas cerca de El Argoub/Tchika pueden estar vacías — no confiar en ellas como plan principal.",
        "Calidad del gasóleo: estándar marroquí en todas las estaciones de la red (Afriquia, Ziz, etc.); sin alternativa de mejor calidad en este tramo.",
    ],
    pendientes=[
        ("eVisa mauritana", "Tramitar con antelación suficiente antes de llegar a Guerguerat"),
        ("Horario de cruce", "Confirmar apertura/cierre actualizados de ambos lados 72 h antes"),
        ("Combustible", "Confirmar disponibilidad en Dakhla antes de salir hacia la frontera"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Mismos números que Marruecos: Policía 19 · Gendarmería Real 177 · Protección Civil/Ambulancia 15. Sin consulado español en el territorio: referencia en Agadir (+212 528 84 56 81) o embajada en Rabat.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

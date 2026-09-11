# -*- coding: utf-8 -*-
"""Etiopía — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Valle del Omo (Turmi y mercados del sur)", cat="Cultura", prio="Alta", dog="no recomendado", time="2 noches",
         lat=4.9500, lon=36.4833,
         desc="Mosaico de pueblos (hamer, mursi, karo, dassanech) con mercados semanales tradicionales; visitar siempre con guía local, con respeto y consentimiento explícito antes de fotografiar a las personas, evitando cualquier trato del encuentro como espectáculo.",
         credit="Josep M. Gracia · CC BY-SA 4.0", source=W + "Market%20scene%20in%20Turmi%2C%20Ethiopia%2C%202011.jpg?width=900"),
    dict(n=2, name="Addis Abeba", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=9.0250, lon=38.7469,
         desc="Capital y mayor base de servicios, talleres y recambios del tramo; sede de la embajada de España (que también cubre Yibuti y Seychelles) y punto de decisión sobre cómo continuar el viaje dado el bloqueo del corredor de Sudán.",
         credit="ምቅ37382 · CC BY-SA 4.0", source=W + "Addis%20abeba%20meskele%20square.jpg?width=900"),
    dict(n=3, name="Lago Langano", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=7.5833, lon=38.7500,
         desc="Lago del Valle del Rift apto para el baño (a diferencia de la mayoría de lagos etíopes), con lodges y campings de descanso a un día de Addis Abeba; buena parada de transición hacia el sur o el este.",
         credit="Nina R from Africa · CC BY 2.0", source=W + "Lake%20Langano%2C%20Ethiopia%20(51101653388).jpg?width=900"),
    dict(n=4, name="Harar (ciudad amurallada, Jugol)", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=9.3125, lon=42.1258,
         desc="Cuarta ciudad santa del islam y casco histórico amurallado (Jugol, UNESCO), con más de 80 mezquitas en un laberinto de callejones; última gran referencia cultural antes de virar hacia la frontera de Galafi con Yibuti.",
         credit="Bikoadem · CC BY-SA 4.0", source=W + "Old%20City%20(Jugal)%20Jamia%20Mosque%20inside%20Jugol%201.jpg?width=900"),
]

_CAT_COLOR = {"cultura": "morado", "naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Moyale (desde Kenia)", "Frontera", 3.5300, 39.0500,
     "Carretera A2 asfaltada; el vehículo NO se admite con CPD (ver alerta de vehículos) — gestionar el patrocinio de un operador turístico etíope con antelación."),
    ("Frontera · Salida — Galafi (hacia Yibuti)", "Frontera", 11.4667, 41.9333,
     "Puesto principal del corredor comercial Adís Abeba-Yibuti (el mismo que usa el ferrocarril de mercancías); bien transitado y equipado."),
    ("Embajada de España en Adís Abeba", "Consular", 9.0280, 38.7600,
     "Haile Melekot Street, Gullele Subcity, Woreda 01, House Nº 036, P.O. Box 2312, Addis Abeba. Tel. +251 111222542 · Emergencia consular 24h: +251 911 219 403 · emb.addisabeba.consu@maec.es. También acreditada en Yibuti y Seychelles."),
    ("Black Lion Hospital, Adís Abeba", "Hospital", 9.0350, 38.7500,
     "Principal hospital de referencia del país; mejor opción sanitaria del tramo junto con clínicas privadas de la capital."),
    ("Combustible · Adís Abeba / eje Moyale-Harar", "Combustible", 9.0250, 38.7469,
     "Estaciones formales (NOC, Total) en las ciudades principales del eje sur-Adís Abeba-Harar; repostar a fondo en cada ciudad antes de tramos rurales largos."),
    ("Agua potable y de uso general · Adís Abeba", "Agua potable", 9.0250, 38.7469,
     "Agua embotellada sin problema en supermercados de la capital; hoteles y lodges de Langano y Harar permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Prohibición de facto y muy alta sensibilidad militar",
                  "Etiopía mantiene un contexto de conflicto interno activo en varias regiones y una notable sensibilidad hacia cualquier aeronave no tripulada; en la práctica no se conceden autorizaciones a particulares y el riesgo de confiscación o problemas legales es alto. Norma del proyecto: no volar el dron en ningún punto del país sin una autorización oficial explícita y verificada por escrito.")

STARLINK_CALLOUT = ("warn", "Sin fecha prevista de licencia a mediados de 2026",
                     "Etiopía figura entre los países africanos sin fecha prevista de aprobación de licencia para Starlink a mediados de 2026. Tratar como no disponible y llevar SIM local (Ethio Telecom, Safaricom Ethiopia) como conectividad principal en todo el país.")

DOG_MATRIX = [
    ("Valle del Omo", "no recomendado", "Desplazamientos largos por pista, calor y logística de visitas culturales incompatibles con llevar mascota; valorar dejarla en Adís Abeba con cuidador."),
    ("Adís Abeba, Langano, Harar", "permitido con condiciones", "Correa y sombra; clima templado en la capital y Langano, más caluroso en Harar."),
]

SOURCES = [
    ("U.S. Embassy Ethiopia · avisos de viaje 2026", "https://et.usembassy.gov/travel-advisory-ethiopia-august-27-2026/"),
    ("travelwarningcheck.com · situación de seguridad por región en Etiopía 2026", "https://www.travelwarningcheck.com/travel-advisory/ethiopia"),
    ("Great Ethiopian Tours · entrada con vehículo propio por Moyale (patrocinio de operador, sin CPD)", "https://www.greatethiopiantours.com/enter-ethiopia-with-a-foreign-vehicle-via-moyale-border-crossing/"),
    ("Embajada de España en Adís Abeba · contacto", "https://www.exteriores.gob.es/Embajadas/addisabeba/es/Embajada/Paginas/Contacto.aspx"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("UNESCO · Ciudad histórica fortificada de Harar Jugol", "https://whc.unesco.org/en/list/1189/"),
    ("Overlanding Association · Shipping around Ethiopia (alternativas marítimas al corredor de Sudán)", "https://overlandingassociation.org/overland-wiki/shipping-around-ethiopia/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
]

CORRIDOR = [(3.5300, 39.0500), (4.9500, 36.4833), (9.0250, 38.7469), (7.5833, 38.7500), (9.3125, 42.1258), (11.4667, 41.9333)]

HISTORIA_RESUMEN = ("Etiopía es el único país africano que nunca fue colonizado de forma duradera, heredero del antiguo reino de Aksum y de una monarquía milenaria derrocada por una revolución marxista en 1974; "
                     "tres décadas de guerra civil y de independencia de Eritrea dieron paso a una relativa estabilidad que se ha visto sacudida de nuevo desde 2020 por la guerra de Tigray y tensiones en Amhara y Oromía, "
                     "el motivo directo por el que este viaje traza un eje sur-este muy concreto y evita el resto del país.")

HISTORIA_SECCIONES = [
    ("Aksum y la cristiandad más antigua de África",
     "El reino de Aksum, en el norte del actual Tigray, fue una de las grandes potencias comerciales del mundo antiguo, con moneda propia y rutas hacia el mar Rojo y el Mediterráneo. "
     "En el siglo IV adoptó el cristianismo como religión oficial —entre las primerísimas conversiones estatales del mundo—, dando origen a la Iglesia ortodoxa etíope, que conserva hoy tradiciones litúrgicas y arquitectónicas únicas, como las iglesias excavadas en roca de Lalibela."),
    ("La monarquía salomónica y la resistencia a la colonización",
     "Durante siglos, una sucesión de emperadores reclamó descender del rey Salomón y la reina de Saba, dando a Etiopía una legitimidad dinástica poco común en el continente. "
     "En 1896, el emperador Menelik II infligió a Italia una derrota decisiva en la batalla de Adwa, la única victoria africana que frenó de forma duradera un intento de conquista colonial europea y convirtió a Etiopía en símbolo panafricano de resistencia. "
     "Italia ocupó el país brevemente entre 1936 y 1941 bajo Mussolini, pero esa ocupación nunca se consolidó como colonia plena y el emperador Haile Selassie fue restaurado con apoyo aliado."),
    ("Revolución, guerra civil e independencia de Eritrea",
     "La monarquía de Haile Selassie fue derrocada en 1974 por una junta militar marxista (el Derg), que instauró un régimen represivo marcado por el «Terror Rojo» y una economía centralizada que agravó hambrunas devastadoras en los años 80. "
     "Una coalición de guerrillas regionales derrocó al Derg en 1991, y en 1993 Eritrea —que había luchado por su independencia durante tres décadas— se separó formalmente de Etiopía, dejando al país sin salida directa al mar."),
    ("Situación actual: la guerra de Tigray y la fragmentación regional",
     "Etiopía vivió dos décadas de crecimiento económico notable bajo un sistema federal étnico, hasta que en 2020 estalló la guerra de Tigray entre el gobierno federal y el Frente Popular de Liberación de Tigray, uno de los conflictos más mortíferos del mundo en ese periodo. "
     "Pese a un acuerdo de paz en 2022, la inestabilidad se ha extendido a las regiones de Amhara (milicias Fano) y Oromía (insurgencia del Frente de Liberación Oromo), con actividad armada activa reportada todavía en 2026. "
     "Por eso el itinerario de este viaje se ciñe a un eje muy concreto —Moyale, Valle del Omo, Adís Abeba, Langano y Harar— y evita por completo el norte y el interior del país; ver la decisión de ruta de esta ficha."),
]

HISTORIA_FUENTES = [
    ("BBC News · Ethiopia country profile", "https://www.bbc.com/news/world-africa-13349398"),
    ("Encyclopaedia Britannica · Ethiopia, History", "https://www.britannica.com/place/Ethiopia/History"),
    ("UNESCO · Aksum, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/15/"),
    ("UNESCO · Iglesias excavadas en roca de Lalibela, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/18/"),
]

SPEC = dict(
    slug="etiopia", name="Etiopía", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Moyale (desde Kenia)"),
        ("SALIDA", "Galafi (hacia Yibuti) — corredor de Sudán BLOQUEADO"),
        ("SEGURIDAD", "Tigray, Amhara y Oromía: evaluación fina obligatoria"),
        ("VEHÍCULO", "CPD NO aceptado — requiere patrocinio de operador etíope"),
        ("COMUNICACIONES", "Starlink sin fecha prevista"),
        ("DECISIÓN", "ruta hacia Egipto por Yibuti (RoRo), no por Sudán"),
    ],
    center=[7.5, 40.0], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y de nuevo 72 h antes de cada frontera.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("La guerra civil de Sudán (activa desde 2023, sin alto el fuego a mediados de 2026) bloquea por completo el corredor terrestre histórico Etiopía→Sudán→Egipto: las fronteras no son fiables ni planificables mientras dure el conflicto. "
              "Decisión del proyecto: NO intentar el corredor de Sudán bajo ninguna circunstancia mientras persista la guerra civil. La alternativa adoptada es desviar la ruta hacia el este, saliendo de Etiopía por Galafi hacia Yibuti, "
              "y desde el puerto de Yibuti (o, en su defecto, desde Adís Abeba con transporte a puerto) contratar un envío marítimo RoRo o en contenedor del vehículo hacia Egipto (vía Arabia Saudí en tránsito) o directamente hacia Europa, "
              "mientras la tripulación vuela por separado. Esta decisión debe revisarse activamente 30-60 días antes del tramo final: si el conflicto de Sudán se resolviera con garantías suficientes, se podría reevaluar el corredor terrestre clásico; "
              "en caso contrario, Yibuti-mar es la ruta de referencia del proyecto — ver también la ficha de Yibuti y la de Egipto."),
    facts=[
        ("Ventana prevista", "Último país de tránito terrestre pleno del corredor de regreso antes de la decisión marítima."),
        ("Entrada", "Moyale desde Kenia, carretera A2 asfaltada."),
        ("Salida", "Galafi hacia Yibuti — NO se intenta el corredor de Sudán (ver decisión de ruta)."),
        ("Seguridad", "Tigray, Amhara y Oromía: conflicto/inestabilidad activos — evitar por completo salvo el eje sur-Adís Abeba-Harar validado."),
        ("Vehículo", "CPD no aceptado en la práctica: se exige patrocinio de un operador turístico etíope licenciado y un Temporary Import Permit tramitado por él."),
        ("Comunicaciones", "Starlink sin fecha prevista de licencia; SIM local imprescindible."),
    ],
    alerts=[
        "Tigray, Amhara y Oromía: conflicto armado y actividad insurgente activos a mediados de 2026 — excluidos del itinerario; el eje del proyecto (Moyale-Valle del Omo-Adís Abeba-Langano-Harar-Galafi) los evita, pero revalidar 30-60 días antes.",
        "Corredor de Sudán: BLOQUEADO por la guerra civil — no planificar ninguna variante que lo atraviese mientras dure el conflicto.",
        "Vehículo: gestionar el patrocinio del operador etíope y el permiso de Aduanas de Adís Abeba con semanas de antelación; no presentarse en Moyale sin esta documentación resuelta.",
        "Valle del Omo: fotografiar personas solo con consentimiento explícito y, cuando así se acostumbre, la contribución acordada; ir siempre con guía local.",
    ],
    ruta_intro="Entrada por Moyale y el Valle del Omo, base logística y de decisión en Adís Abeba, descanso en el lago Langano y cierre cultural en Harar antes de salir hacia Yibuti por Galafi — evitando por completo el corredor de Sudán.",
    route_rows=[
        ("Entrada y cultura", "Moyale → Valle del Omo (Turmi)", "Mercados tradicionales; guía local obligatorio"),
        ("Capital y decisión", "Turmi → Adís Abeba", "Embajada española; gestión del envío marítimo hacia Egipto/Europa"),
        ("Descanso", "Adís Abeba → Lago Langano", "Transición hacia el este; apto para el baño"),
        ("Cultura y salida", "Langano → Harar → Galafi", "Ciudad amurallada UNESCO; salida hacia Yibuti"),
    ],
    offroad=[
        "Pistas de tierra en el tramo Moyale-Turmi del Valle del Omo, transitables con 4x4 en estación seca; el resto del eje previsto (Adís Abeba-Langano-Harar-Galafi) es carretera asfaltada.",
    ],
    acampada=[
        "Turmi: campings y lodges orientados a visitantes del Valle del Omo, con guías locales disponibles in situ.",
        "Langano: lodges y campings de playa lacustre, opción de descanso real tras el tramo sur.",
        "Harar: hoteles dentro y fuera de la muralla; sin acampada libre recomendada en el casco histórico.",
    ],
    visado=[
        "e-Visa obligatoria para ciudadanos españoles, tramitada online con antelación.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica (aplica viniendo de Kenia).",
        "Confirmar 30-60 días antes la situación de seguridad exacta por región antes de fijar el itinerario definitivo.",
    ],
    fronteras_rows=[
        ("Entrada", "Moyale (Kenia)", "Carretera A2 asfaltada; gestionar patrocinio de operador etíope antes de llegar."),
        ("Salida", "Galafi (Yibuti)", "Corredor comercial principal Adís Abeba-Yibuti; puesto bien equipado."),
    ],
    vehiculos=[
        "El CPD NO se acepta en la práctica en Etiopía: es imprescindible contratar a un operador turístico etíope licenciado que actúe como patrocinador, obtenga el permiso del Ministerio de Turismo y tramite el Temporary Import Permit ante la Aduana de Adís Abeba.",
        "Solicitar también una carta de la Embajada de Etiopía en Nairobi dirigida a aduanas, antes de presentarse en Moyale.",
        "Seguro de terceros local obligatorio, gestionado normalmente por el propio operador patrocinador.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No volar el dron en ningún punto del país sin autorización oficial explícita y verificada por escrito.",
        "Máxima discreción cerca de cualquier instalación gubernamental o militar, especialmente en Adís Abeba.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Sin fecha prevista de licencia a mediados de 2026: tratar como no disponible en todo el país.",
        "SIM local (Ethio Telecom, Safaricom Ethiopia) como conectividad principal.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente y vacuna antirrábica en vigor, exigibles en frontera.",
        "No recomendado en el Valle del Omo por la logística de las visitas culturales y el calor; valorar dejarlo con cuidador en Adís Abeba durante ese tramo.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en tierras bajas (incluido el Valle del Omo y el corredor hacia Yibuti); menor riesgo en Adís Abeba por altitud. Profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Black Lion Hospital (Adís Abeba) como mejor referencia sanitaria del tramo; seguro con evacuación médica real imprescindible fuera de la capital.",
    ],
    seguridad_intro="Etiopía combina un eje sur-este manejable (Moyale-Valle del Omo-Adís Abeba-Langano-Harar) con varias regiones en conflicto activo (Tigray, Amhara, Oromía) que quedan fuera de cualquier variante de esta ruta.",
    seguridad=[
        "No desviarse hacia Tigray, Amhara ni el interior de Oromía bajo ninguna circunstancia mientras persista la inestabilidad reportada.",
        "Revalidar la situación de seguridad de todo el eje previsto 30-60 días antes del viaje, con fuentes oficiales y locales.",
        "En Adís Abeba, evitar zonas de concentración de protestas y seguir indicaciones de la embajada ante cualquier incidente.",
        "En el Valle del Omo, moverse siempre con guía local y evitar desplazamientos nocturnos por pista.",
    ],
    agua=[
        "Adís Abeba: agua embotellada sin problema en supermercados.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): hoteles y lodges de Langano y Harar permiten llenar el depósito con manguera; en el Valle del Omo, confirmar con el guía/lodge local antes de dar por hecho un punto.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje previsto: Moyale → Turmi (~90 km) → Adís Abeba (~600 km) → Langano (~200 km) → Harar (~370 km) → Galafi (~330 km), todos con estaciones formales salvo el tramo final más rural hacia Galafi.",
        "Repostar a fondo en Harar antes de Galafi: la oferta en el tramo final hacia la frontera de Yibuti es más escasa.",
    ],
    pendientes=[
        ("Vehículo", "Cerrar el patrocinio del operador etíope y el TIP antes de llegar a Moyale"),
        ("Corredor de Sudán", "Confirmar que sigue bloqueado 30-60 días antes; si no, reevaluar con el proyecto"),
        ("Envío marítimo", "Reservar el RoRo/contenedor desde Yibuti hacia Egipto o Europa con antelación suficiente"),
        ("Seguridad regional", "Revalidar Tigray/Amhara/Oromía justo antes del viaje"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. La decisión sobre el corredor de Sudán debe revalidarse activamente antes del viaje.",
    emergency="Emergencia consular española (Adís Abeba, 24h): +251 911 219 403 · Embajada de España en Adís Abeba: +251 111222542.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

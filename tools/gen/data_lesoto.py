# -*- coding: utf-8 -*-
"""Lesoto — ficha completa (9 sep 2026): alternativa/opcional (Sani Pass) si el calendario lo permite."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Sani Pass (Techo de África)", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1 noche",
         lat=-29.5833, lon=29.2833,
         desc="Uno de los puertos de montaña 4x4 más icónicos del sur de África, con curvas de herradura que suben desde KwaZulu-Natal hasta los 2.876 m del altiplano lesotense; imprescindible vehículo con tracción total y frenos en buen estado.",
         credit="Amada44 · dominio público", source=W + "Sani%20Pass%20Lesotho%202.jpg?width=900"),
    dict(n=2, name="Maseru", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-29.3167, lon=27.4833,
         desc="Capital y único centro urbano relevante del país, enclavada en el altiplano y completamente rodeada por Sudáfrica; base de servicios básicos si el itinerario incluye una vuelta completa por Lesoto en lugar de una simple excursión a Sani Pass.",
         credit="Axelspace Corporation · CC BY-SA 4.0", source=W + "Maseru%2C%20Lesotho.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Puesto de Sani Pass (con Sudáfrica)", "Frontera", -29.5900, 29.2800,
     "Puesto fronterizo en lo alto del puerto; pista de montaña de tierra y roca en el lado lesotense, exigente en mal tiempo o con nieve."),
    ("Frontera · Maseru Bridge (con Sudáfrica)", "Frontera", -29.3200, 27.5200,
     "Cruce principal y más transitado, asfaltado, si se opta por una vuelta completa por carretera en lugar de solo Sani Pass."),
    ("Embajada de España en Pretoria (competente para Lesoto)", "Consular", -25.7461, 28.1871,
     "Referencia diplomática de Lesoto, Madagascar, Mauricio y Comores; gestionar trámites mayores a través de Pretoria (Sudáfrica) — ver ficha de Sudáfrica para el contacto completo."),
    ("Queen Mamohato Memorial Hospital, Maseru", "Hospital", -29.3200, 27.5000,
     "Principal hospital de referencia del país; para necesidades serias, evacuación hacia Sudáfrica (Bloemfontein o Durban) es la opción real."),
    ("Combustible · Maseru", "Combustible", -29.3167, 27.4833,
     "Única concentración fiable de estaciones formales si se hace la vuelta completa por el país; repostar a fondo antes de cualquier tramo de montaña."),
    ("Agua potable y de uso general · Maseru", "Agua potable", -29.3167, 27.4833,
     "Agua embotellada sin problema en la capital; lodges de montaña cerca de Sani Pass permiten llenar el depósito de uso general con manguera, confirmar en recepción."),
]

DRONE_CALLOUT = ("warn", "Autorización previa recomendada",
                  "Lesoto no tiene una normativa de drones muy desarrollada ni ampliamente publicada; recomendable consultar con la autoridad de aviación civil antes de volar y evitar cualquier vuelo cerca de instalaciones oficiales en Maseru.")

STARLINK_CALLOUT = ("warn", "Estado sin confirmar a mediados de 2026",
                     "No hay confirmación clara del estado de licencia de Starlink en Lesoto a la fecha de esta revisión. Tratar como no garantizado, especialmente en el altiplano de Sani Pass, y llevar SIM local (Vodacom Lesotho, Econet) como respaldo.")

DOG_MATRIX = [
    ("Sani Pass", "permitido con condiciones", "Correa siempre; frío intenso en altitud incluso en verano — llevar abrigo para la mascota."),
    ("Maseru", "permitido con condiciones", "Correa y sombra; clima templado de altiplano."),
]

SOURCES = [
    ("The Travelling Sloth · guía overland de Lesoto", "https://www.thetravellingsloth.com/lesotho-overlanding-travel-guide/"),
    ("Toone's Travels · guía de conducción de Sani Pass 2025", "https://www.chris-toone.com/blog/self-driving-sani-pass-guide"),
    ("Embajada de España en Pretoria · consulados y competencias", "https://www.exteriores.gob.es/Embajadas/pretoria/es/Embajada/Paginas/Consulados.aspx"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
]

CORRIDOR = [(-29.5900, 29.2800), (-29.5833, 29.2833), (-29.3167, 27.4833), (-29.3200, 27.5200)]

HISTORIA_RESUMEN = ("Lesoto es el único país del mundo situado íntegramente por encima de los 1.000 m de altitud y uno de los tres enclavados por completo dentro de otro país; nació de la resistencia del pueblo basoto bajo el rey Moshoeshoe I "
                     "frente a la expansión bóer en el siglo XIX, sobrevivió como protectorado británico separado de Sudáfrica y hoy es una monarquía constitucional que vive del turismo de montaña y de la exportación de agua hacia su vecino.")

HISTORIA_SECCIONES = [
    ("Moshoeshoe I y la fundación del reino basoto",
     "A principios del siglo XIX, en pleno periodo de disturbios y guerras conocido como el Difaqane, el jefe Moshoeshoe I unificó a distintos clanes sotho en las montañas del Drakensberg, estableciendo su fortaleza en la meseta inexpugnable de Thaba Bosiu. "
     "Su liderazgo diplomático —y la protección natural del terreno montañoso— permitió al reino basoto resistir sucesivas presiones de los bóers que se expandían desde el Estado Libre de Orange."),
    ("Protectorado británico separado de Sudáfrica",
     "En 1868, ante la presión bóer, Moshoeshoe solicitó la protección británica, y el territorio se convirtió en el protectorado de Basutolandia. Esta decisión resultó crucial: cuando en 1910 se formó la Unión Sudafricana, Basutolandia permaneció fuera de ella como territorio británico aparte, "
     "evitando así quedar sometida directamente al sistema que después derivaría en el apartheid."),
    ("Independencia como Reino de Lesoto",
     "Lesoto alcanzó la independencia en 1966 como monarquía constitucional bajo el rey Moshoeshoe II, descendiente del fundador del reino. El país vivió golpes de Estado y periodos de gobierno militar en las décadas siguientes, "
     "pero mantuvo su identidad basoto y su sistema de doble monarquía (jefaturas tradicionales y Corona) hasta la actualidad."),
    ("Situación actual: agua, montaña y dependencia de Sudáfrica",
     "La economía de Lesoto depende en gran medida de las remesas de trabajadores en Sudáfrica y de la exportación de agua a través del Proyecto de las Tierras Altas de Lesoto, que embalsa los ríos de sus montañas para abastecer a Johannesburgo. "
     "El país es hoy un destino de turismo de montaña y aventura —Sani Pass y el trekking en poni son sus grandes atractivos— y, para este proyecto, queda como un desvío opcional que corona el viaje con una de las carreteras de montaña más espectaculares del continente."),
]

HISTORIA_FUENTES = [
    ("BBC News · Lesotho country profile", "https://www.bbc.com/news/world-africa-13031816"),
    ("Encyclopaedia Britannica · Lesotho, History", "https://www.britannica.com/place/Lesotho/History"),
    ("UNESCO · Maloti-Drakensberg Park (comparte límite con Lesoto)", "https://whc.unesco.org/en/list/985/"),
]

SPEC = dict(
    slug="lesoto", name="Lesoto", revision="9 sep 2026",
    sub="Alternativa/opcional · Sani Pass como coronación de montaña si el calendario lo permite",
    chips=[
        ("ROL EN LA RUTA", "opcional — enlace Sudáfrica→Mozambique"),
        ("ENTRADA/SALIDA", "Sani Pass (montaña, 4x4) o Maseru Bridge (asfaltado)"),
        ("SEGURIDAD", "estable"),
        ("VEHÍCULO", "permiso temporal sencillo"),
    ],
    center=[-29.5, 28.2], zoom=8,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, si finalmente se incluye este desvío.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    facts=[
        ("Rol en la ruta", "Alternativa/opcional en el enlace Sudáfrica→Mozambique, si el calendario permite el desvío de montaña."),
        ("Entrada/salida", "Sani Pass (pista de montaña, imprescindible 4x4) o Maseru Bridge (cruce asfaltado más directo)."),
        ("Seguridad", "País estable; sin alertas relevantes para este proyecto."),
        ("Vehículo", "Permiso temporal sencillo en frontera; confirmar condiciones específicas del vehículo para subir Sani Pass."),
    ],
    alerts=[
        "Sani Pass: pista de tierra y roca con tramos de zigzag pronunciado; puede cerrarse por nieve o hielo en invierno austral (junio-agosto) — confirmar el estado de la pista antes de subir.",
        "Confirmar que el vehículo de expedición (Grenadier/Delica) cumple los requisitos de tracción y despeje necesarios para Sani Pass antes de decidir esta variante.",
    ],
    ruta_intro="Desvío de montaña desde Sudáfrica: subida por Sani Pass hasta el altiplano lesotense, con opción de bajar por Maseru Bridge para completar una vuelta más amplia por el país antes de reincorporarse a la ruta hacia Mozambique.",
    route_rows=[
        ("Subida", "KwaZulu-Natal (Sudáfrica) → Sani Pass", "Pista de montaña 4x4; imprescindible buen tiempo"),
        ("Altiplano", "Sani Pass → Maseru (opcional)", "Vuelta completa por el país si el calendario lo permite"),
        ("Reincorporación", "Maseru Bridge → Sudáfrica", "Cruce asfaltado hacia el corredor principal"),
    ],
    offroad=[
        "Sani Pass es la pista de montaña más exigente de todo el proyecto en el corredor de regreso: zigzag pronunciado, superficie de tierra y roca suelta, y posible nieve/hielo en invierno austral.",
    ],
    acampada=[
        "Sani Mountain Lodge (en lo alto del puerto): referencia clásica de descanso para overlanders tras la subida.",
        "Maseru: hoteles urbanos si se opta por la vuelta completa por el país.",
    ],
    visado=[
        "Exención de visado para españoles — verificar vigencia exacta 30-60 días antes.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica.",
    ],
    fronteras_rows=[
        ("Entrada/salida (montaña)", "Sani Pass (Sudáfrica)", "Pista de tierra y roca; imprescindible 4x4 y buen tiempo."),
        ("Entrada/salida (asfaltada)", "Maseru Bridge (Sudáfrica)", "Cruce principal y más directo del país."),
    ],
    vehiculos=[
        "Permiso temporal sencillo en frontera para el vehículo.",
        "Confirmar despeje y tracción del vehículo antes de subir Sani Pass; en condiciones adversas, valorar la variante asfaltada por Maseru Bridge.",
        "Seguro de terceros SADC válido en Lesoto como miembro de la región.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Consultar con la autoridad de aviación civil de Lesoto antes de volar.",
        "No volar cerca de instalaciones oficiales en Maseru.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado sin confirmar a mediados de 2026: tratar como no garantizado, especialmente en el altiplano de Sani Pass.",
        "SIM local (Vodacom Lesotho, Econet) como respaldo.",
    ],
    perro_intro=[
        "Certificado veterinario internacional y vacuna antirrábica en vigor, exigibles en frontera.",
        "Llevar abrigo para la mascota en Sani Pass: temperaturas bajas incluso en verano austral por la altitud.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Altitud considerable en todo el país (Maseru ya está a ~1.600 m, Sani Pass a casi 2.900 m): posible mal de altura leve en personas sensibles.",
        "Frío intenso en invierno austral (junio-agosto), con nieve frecuente en el altiplano: equipación de abrigo imprescindible.",
        "Queen Mamohato Memorial Hospital (Maseru) como referencia local; para casos serios, evacuación hacia Sudáfrica es la opción real.",
    ],
    seguridad_intro="Lesoto es un país estable; el principal factor de riesgo del desvío es la propia dificultad técnica y meteorológica de Sani Pass, no la seguridad ciudadana.",
    seguridad=[
        "Confirmar el estado de la pista de Sani Pass y la previsión meteorológica antes de subir; no intentarlo con nieve o hielo sin experiencia específica.",
        "Precaución normal de viaje en Maseru y el resto del país.",
    ],
    agua=[
        "Maseru: agua embotellada sin problema en la capital.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): lodges de montaña cerca de Sani Pass permiten llenar el depósito con manguera; confirmar en recepción dado lo remoto de la zona.",
    ],
    combustible=[
        "Repostar a fondo en Sudáfrica (Underberg u otra localidad de KwaZulu-Natal) antes de subir Sani Pass: la oferta en el lado lesotense del puerto es limitada.",
        "Maseru concentra la única oferta fiable si se hace la vuelta completa por el país.",
    ],
    pendientes=[
        ("Decisión de ruta", "Confirmar si se sube por Sani Pass o se opta por Maseru Bridge según vehículo y meteorología"),
        ("Vehículo", "Verificar despeje y tracción del Grenadier/Delica para la pista de Sani Pass"),
        ("Meteorología", "Revisar previsión antes de subir, especialmente fuera de la temporada seca"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Lesoto es un desvío opcional: confirmar si se incluye antes de revalidar el resto de trámites.",
    emergency="Sin representación española propia en Lesoto — gestionar emergencias a través de la Embajada de España en Pretoria (Sudáfrica), competente para el país.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

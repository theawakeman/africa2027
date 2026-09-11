# -*- coding: utf-8 -*-
"""Angola — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Luanda", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-8.8383, lon=13.2344,
         desc="Capital y mayor base logística del país: puerto, aeropuerto internacional, embajada de España, talleres y recambios de todo tipo. Marginal (paseo marítimo), Fortaleza de San Miguel e Ilha de Luanda como referencia urbana e histórica.",
         credit="Chimpanz APe · CC BY 2.0", source=W + "2009%20Luanda%20Angola%203818325721.jpg?width=900"),
    dict(n=2, name="Miradouro da Lua", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=-9.1667, lon=13.0333,
         desc="Paisaje erosionado de cañones y formaciones lunares sobre el Atlántico, a 40 km al sur de Luanda; mirador espectacular al atardecer y parada obligada nada más salir de la capital hacia el sur.",
         credit="Paulo César Santos · CC0", source=W + "Miradouro%20da%20Lua%20(Angola).jpg?width=900"),
    dict(n=3, name="Lobito", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-12.3644, lon=13.5456,
         desc="Ciudad portuaria sobre una restinga arenosa entre el océano y la bahía, con arquitectura colonial portuguesa bien conservada (Igreja da Arrábida) y ambiente más tranquilo que Luanda; punto de descanso en el descenso hacia el sur.",
         credit="Robertoago · CC BY-SA 3.0", source=W + "Lobito%20restinga2.jpg?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "naturaleza": "verde", "cultura": "marron"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Lufu/Luvo (desde RD Congo)", "Frontera", -5.9167, 13.9667,
     "Cruce del puente fronterizo con RD Congo; registro y sellado ~500 m dentro de Angola. Desvío opcional a M'banza-Kongo (Patrimonio Mundial UNESCO, antigua capital del Reino del Kongo) a poca distancia de la frontera."),
    ("Frontera · Salida — Santa Clara/Oshikango (hacia Namibia)", "Frontera", -17.3500, 15.7500,
     "Paso principal y más transitado hacia Namibia; carretera asfaltada en ambos lados, infraestructura de control moderna."),
    ("Embajada de España en Luanda", "Consular", -8.8167, 13.2333,
     "Rua Frederico Welwitsch 84, Torre Maculusso, 12º andar C, Postal 3061, Luanda. Tel. +244 222 391 166/187/188 · Emergencia consular: +244 929 900 900."),
    ("Hospital Américo Boavida — Luanda", "Hospital", -8.8147, 13.2302,
     "Principal hospital de referencia de la capital. Coordenada urbana aproximada."),
    ("Combustible · Luanda / Lobito", "Combustible", -8.8383, 13.2344,
     "Mejor oferta y calidad del país (Sonangol, Pumangol) en las dos grandes ciudades costeras; repostar a fondo en ambas antes de tramos más largos hacia el sur."),
    ("Combustible · M'banza-Kongo / Uíge (eje norte)", "Combustible", -6.2667, 14.2500,
     "Estaciones formales en el desvío norte antes de bajar a Luanda; confirmar disponibilidad, oferta más limitada que en la costa."),
    ("Agua potable y de uso general · Luanda", "Agua potable", -8.8383, 13.2344,
     "Agua embotellada sin problema en supermercados de la capital; estaciones de servicio y hoteles de Luanda y Lobito permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria: tratar como restringido",
                  "Angola exige autorización previa del Instituto Nacional de Aviação Civil (INAVIC) para cualquier vuelo de dron, con especial sensibilidad cerca de instalaciones petroleras y portuarias (Luanda, Lobito, Cabinda). Norma prudente del proyecto: no volar sin permiso escrito, y evitar cualquier vuelo cerca de infraestructura energética o militar.")

STARLINK_CALLOUT = ("warn", "Anunciado para 2026, aún no activo a mediados de año: tratar como no disponible",
                     "Angola figura entre los mercados africanos con Starlink previsto («coming in 2026») pero sin confirmación de servicio activo a mediados de 2026. Tratarlo como no disponible hasta confirmación oficial y mantener SIM local (Unitel, Africell) como conectividad principal.")

DOG_MATRIX = [
    ("Luanda, Miradouro da Lua, Lobito", "permitido con condiciones", "Correa y sombra; calor seco en el sur, más húmedo en la franja costera norte."),
]

SOURCES = [
    ("Angola-Visa.com · proceso de e-visa para viajeros overland", "https://www.angola-visa.com/overland/"),
    ("Hinterland Travel · requisitos de visado de Angola para ciudadanos españoles", "https://www.hinterlandtravel.com/spain/destinations/angola"),
    ("WhirledAway · cruce de frontera Lufu (RD Congo) / Luvo (Angola)", "https://whirled-away.com/border-crossing-drc-angola/"),
    ("Africa Tour Visa · frontera Angola-República del Congo (referencia Cabinda)", "https://www.africatourvisa.com/angola/border-crossing/republicof-the-congo-border/"),
    ("Embajada de España en Angola · contacto", "https://www.exteriores.gob.es/Embajadas/luanda/es/Paginas/index.aspx"),
    ("tech.africa · disponibilidad de Starlink en África (2026)", "https://tech.africa/starlink-africa/"),
    ("UNESCO · Mbanza Kongo, vestigios de la capital del antiguo Reino del Kongo", "https://whc.unesco.org/en/list/1473/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(-5.9167, 13.9667), (-8.8383, 13.2344), (-9.1667, 13.0333), (-12.3644, 13.5456), (-17.3500, 15.7500)]

HISTORIA_RESUMEN = ("Angola, heredera del gran reino de Ndongo y del reino de Kongo, sufrió casi cinco siglos de presencia colonial portuguesa centrada en la trata de esclavos hacia Brasil, y tras una independencia tardía en 1975 se sumió de inmediato en una guerra civil de 27 años "
                     "(1975-2002) que fue uno de los grandes escenarios de la Guerra Fría en África, con Cuba y la URSS apoyando al gobierno marxista y Sudáfrica y Estados Unidos a la guerrilla de UNITA; la paz de 2002 dio paso a un boom petrolero que ha transformado Luanda en una de las ciudades más caras del mundo.")

HISTORIA_SECCIONES = [
    ("Los reinos de Kongo y Ndongo",
     "El norte del actual territorio formó parte del reino de Kongo, mientras que el reino de Ndongo, gobernado en el siglo XVII por la célebre reina Nzinga Mbandi —hoy símbolo nacional de resistencia—, libró una larga lucha contra el avance portugués antes de sucumbir a la ocupación colonial."),
    ("Cinco siglos de colonización portuguesa y la trata de esclavos",
     "Portugal estableció su presencia en la costa angoleña ya en el siglo XV, y Angola se convirtió en uno de los mayores puntos de origen de la trata negrera atlántica, con millones de personas embarcadas hacia Brasil a lo largo de tres siglos; el dominio colonial portugués, uno de los más prolongados y tardíos en abandonar África, se mantuvo hasta 1975."),
    ("Independencia y la guerra civil de la Guerra Fría (1975-2002)",
     "Angola alcanzó la independencia en 1975 tras una guerra de liberación, pero la rivalidad entre los movimientos independentistas MPLA, UNITA y FNLA derivó de inmediato en una guerra civil que se convirtió en uno de los grandes conflictos por delegación de la Guerra Fría: Cuba y la Unión Soviética respaldaron al gobierno marxista del MPLA, mientras Sudáfrica del apartheid y Estados Unidos apoyaron a la guerrilla anticomunista de UNITA liderada por Jonas Savimbi; el conflicto se prolongó, con altibajos, hasta la muerte de Savimbi en 2002."),
    ("Situación actual: boom petrolero y desigualdad",
     "Desde el fin de la guerra, Angola ha vivido un notable boom económico basado en sus enormes reservas petroleras (una de las mayores de África) y, en menor medida, en diamantes, que ha convertido a Luanda en una de las capitales más caras del mundo para expatriados, conviviendo con una desigualdad social muy marcada; el partido MPLA, en el poder desde la independencia, mantiene el control político del país bajo el presidente João Lourenço desde 2017."),
]

HISTORIA_FUENTES = [
    ("BBC News · Angola country profile", "https://www.bbc.com/news/world-africa-13036732"),
    ("Encyclopaedia Britannica · Angola, History", "https://www.britannica.com/place/Angola/History"),
    ("Council on Foreign Relations · Angola's civil war", "https://www.cfr.org/timeline/angolas-civil-war"),
]

SPEC = dict(
    slug="angola", name="Angola", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Lufu/Luvo (desde RD Congo)"),
        ("SALIDA", "Santa Clara/Oshikango (hacia Namibia)"),
        ("SEGURIDAD", "estable · precaución normal"),
        ("VISADO", "exención de 30 días para españoles — verificar vigencia antes de viajar"),
        ("DESVÍO UNESCO", "M'banza-Kongo, cerca de la frontera de entrada"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[-11.0, 14.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Angola marca el regreso a un país con infraestructura sólida y buenas carreteras tras el tramo más exigente de Centroáfrica: Luanda como gran base logística, "
                   "el paisaje lunar del Miradouro da Lua a las puertas de la capital, la ciudad colonial de Lobito y un desvío histórico opcional a M'banza-Kongo (UNESCO) cerca de la frontera de entrada, "
                   "antes del largo descenso hacia Namibia."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras RD Congo y antes de Namibia."),
        ("Entrada", "Lufu/Luvo desde RD Congo; desvío opcional a M'banza-Kongo (UNESCO) a poca distancia."),
        ("Salida", "Santa Clara/Oshikango hacia Namibia: paso más transitado, infraestructura moderna."),
        ("Visado", "Exención de visado de turismo de 30 días para pasaportes españoles a fecha de esta revisión — confirmar vigencia 30-60 días antes, la política ha cambiado varias veces en los últimos años."),
        ("Seguridad", "Estable en todo el país, precaución normal; sin zonas excluidas en el corredor previsto."),
        ("Comunicaciones", "Starlink anunciado para 2026, no confirmado activo; SIM local (Unitel, Africell) como base."),
    ],
    alerts=[
        "Visado: la exención de 30 días para españoles debe reconfirmarse 30-60 días antes de viajar — Angola ha ajustado su política de visados varias veces en los últimos años; si hay cualquier duda, tramitar el e-Visa como respaldo.",
        "Reentradas: si el itinerario contempla salir de Angola y volver a entrar (por ejemplo, por un desvío a Cabinda), verificar que el régimen de entrada aplicable permite múltiples entradas — la exención de 30 días se trata como de entrada única salvo confirmación expresa.",
        "M'banza-Kongo: desvío que añade tiempo y pista adicional cerca de la frontera — valorar según el calendario general del tramo centroafricano, que ya acumula varias fronteras complejas seguidas.",
    ],
    ruta_intro="Descenso por la costa atlántica angoleña, desde la frontera de RD Congo hasta el paso hacia Namibia.",
    route_rows=[
        ("Entrada y desvío histórico", "Lufu/Luvo → (M'banza-Kongo opcional) → Luanda", "UNESCO cerca de la frontera; capital como base logística"),
        ("Paisaje y costa", "Luanda → Miradouro da Lua → Lobito", "Mirador lunar; ciudad colonial portuaria"),
        ("Hacia Namibia", "Lobito → Namibe → Santa Clara/Oshikango", "Descenso largo por buena infraestructura hasta la frontera namibia"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto en este primer tramo angoleño: la costa Luanda-Lobito es carretera asfaltada en buen estado; el desierto del Namibe (más al sur) se trata en el tramo siguiente.",
    ],
    acampada=[
        "Luanda: alojamientos con parking vigilado, opción más práctica que la acampada libre en la capital.",
        "Lobito: hoteles y alguna opción de camping costero con aparcamiento.",
    ],
    visado=[
        "Exención de visado de turismo (30 días) para pasaportes españoles a fecha de esta revisión; confirmar vigencia 30-60 días antes de viajar.",
        "Si la exención cambiara, tramitar el e-Visa angoleño con antelación suficiente, prestando atención a si se necesita entrada múltiple.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
    ],
    fronteras_rows=[
        ("Entrada", "Lufu/Luvo (RD Congo)", "Cruce del puente fronterizo; registro y sellado ~500 m dentro de Angola; desvío opcional a M'banza-Kongo cerca de aquí."),
        ("Salida", "Santa Clara/Oshikango (Namibia)", "Paso más transitado hacia Namibia; carretera asfaltada e infraestructura de control moderna en ambos lados."),
    ],
    vehiculos=[
        "CPD recomendado; confirmar si Angola exige también una importación temporal adicional del vehículo, dado que el país no pertenece a CEDEAO ni a CEMAC.",
        "Seguro de responsabilidad civil local obligatorio: contratarlo al entrar por Lufu/Luvo si no se dispone de cobertura previa válida.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa por escrito al INAVIC antes de intentar introducir el dron en el país.",
        "No volar cerca de instalaciones petroleras o portuarias (Luanda, Lobito) ni de zonas militares.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado no confirmado a mediados de 2026 pese al anuncio de llegada dentro del año: revisar el mapa oficial 30-60 días antes.",
        "SIM local (Unitel, Africell) como conectividad principal en Luanda y el eje costero.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE).",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio, con mayor intensidad en el norte: profilaxis a valorar con Sanidad Exterior.",
        "Hospital Américo Boavida (Luanda) como referencia hospitalaria del tramo; seguro con evacuación médica imprescindible.",
    ],
    seguridad_intro="País estable con precaución normal en todo el corredor previsto; buena infraestructura de carreteras tras el tramo más exigente de Centroáfrica.",
    seguridad=[
        "Sin zonas excluidas por seguridad en el tramo previsto entre Lufu/Luvo y la frontera namibia.",
        "Extremar la precaución documental en el cruce de Lufu/Luvo: primer país fuera de las zonas de seguro regional CEDEAO/CEMAC del tramo.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
    ],
    agua=[
        "Luanda: agua embotellada en supermercados sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio y hoteles de Luanda y Lobito permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje costero: Lufu/Luvo → Luanda (~350 km) → Miradouro da Lua (~40 km) → Lobito (~500 km), con estaciones formales (Sonangol, Pumangol) en cada núcleo urbano intermedio.",
        "Repostar a fondo en Luanda y de nuevo en Lobito antes de continuar hacia Namibe y el sur, donde la oferta se espacía más.",
    ],
    pendientes=[
        ("Visado", "Reconfirmar la vigencia de la exención de 30 días para españoles 30-60 días antes de viajar"),
        ("M'banza-Kongo", "Decidir si el desvío UNESCO entra en el calendario del tramo centroafricano"),
        ("Seguro e importación del vehículo", "Confirmar el procedimiento exacto al entrar por Lufu/Luvo, fuera de CEDEAO/CEMAC"),
        ("Dron", "Contactar con el INAVIC o descartar el vuelo en el país"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Luanda): +244 929 900 900 · Embajada: +244 222 391 166.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

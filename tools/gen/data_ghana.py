# -*- coding: utf-8 -*-
"""Ghana — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Castillo de Elmina", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=5.0836, lon=-1.3508,
         desc="El fuerte europeo más antiguo del África subsahariana (portugués, 1482), punto central de la memoria de la trata atlántica; museo y visita guiada obligatoria en el interior. El perro espera fuera durante la visita.",
         credit="Damien Halleux Radermecker · CC BY-SA 2.0", source=W + "Elmina%20Castle%20-%20Ghana.jpg?width=900"),
    dict(n=2, name="Castillo de Cape Coast", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=5.1053, lon=-1.2466,
         desc="Fuerte y museo gemelo de Elmina, con la «puerta sin retorno» hacia los barcos negreros; una de las visitas históricas más intensas de la ruta. Reservar tiempo para la explicación guiada, obligatoria y recomendable.",
         credit="Matti Blume · CC BY-SA 4.0", source=W + "Castle%2C%20Cape%20Coast%20(P1100221).jpg?width=900"),
    dict(n=3, name="Parque Nacional de Kakum (pasarela de dosel)", cat="Naturaleza", prio="Alta", dog="prohibido", time="½ día",
         lat=5.3500, lon=-1.3833,
         desc="Selva tropical primaria con la pasarela colgante de dosel más conocida de África Occidental, a 30-40 m de altura entre siete plataformas. El perro no puede acceder al parque ni a la pasarela.",
         credit="daSupremo · CC BY-SA 4.0", source=W + "Canopy%20walkway%20in%20Kakum%20National%20Park%204.jpg?width=900"),
    dict(n=4, name="Accra (Independence Square y Jamestown)", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=5.5471, lon=-0.1942,
         desc="Capital y mayor base logística del golfo de Guinea oriental: puerto (Tema), aeropuerto internacional, embajada de España, talleres y recambios. Independence Square y el barrio pesquero de Jamestown como referencia urbana.",
         credit="Flowizm · CC BY 2.0", source=W + "Independence%20Arch%20Accra%20Ghana.jpg?width=900"),
    dict(n=5, name="Cascadas de Wli", cat="Naturaleza", prio="Media", dog="permitido", time="1 día",
         lat=7.1167, lon=0.5833,
         desc="La cascada más alta de Ghana (~80 m), en la región del Volta cerca de la frontera con Togo; caminata corta hasta la caída baja, más exigente hasta la alta. Buen último punto antes de cruzar a Togo por Aflao/Kpalimé.",
         credit="Stig Nygaard · CC BY 2.0", source=W + "Wli%20Lower%20Fall-4.jpg?width=900"),
]

_CAT_COLOR = {"patrimonio unesco": "marron", "naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Elubo (desde Costa de Marfil)", "Frontera", 5.0333, -2.8667,
     "Paso principal y más transitado de la subregión; carretera pavimentada en buen estado, puente sobre el río fronterizo, horario 06:00-18:00. Laissez-passer/C59 temporal para vehículos extranjeros."),
    ("Frontera · Salida — Aflao (hacia Togo)", "Frontera", 6.1167, 1.2000,
     "Paso urbano integrado en la conurbación Aflao-Lomé; alto volumen de tráfico peatonal y comercial, prever demoras."),
    ("Embajada de España en Accra (también acreditada en Togo)", "Consular", 5.6050, -0.1700,
     "Drake Av. Extension, Airport Residential Area, P.M.B. KA 44, Accra. +233 302 77 40 04/05. Coordenada urbana aproximada."),
    ("Korle Bu Teaching Hospital — Accra", "Hospital", 5.5364, -0.2270,
     "Principal hospital universitario y de referencia del país; mejor capacidad de la subregión para urgencias graves. Coordenada urbana aproximada."),
    ("Combustible · Elubo", "Combustible", 5.0333, -2.8667,
     "Estaciones en el propio puesto fronterizo (GOIL, Total); repostar al entrar si el depósito no está lleno."),
    ("Combustible · Cape Coast / Elmina", "Combustible", 5.1053, -1.2466,
     "Buena oferta en el eje costero histórico, entre Elubo y Accra."),
    ("Combustible · Accra", "Combustible", 5.5471, -0.1942,
     "Mejor oferta y calidad del país (GOIL, Total, Shell); repostar aquí antes del tramo final hacia Aflao/Togo."),
    ("Agua potable · Accra y Cape Coast (supermercados y garrafas)", "Agua potable", 5.5471, -0.1942,
     "Agua embotellada ampliamente disponible en todo el eje costero del itinerario; sin problema de suministro en este tramo."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria por escrito (GCAA)",
                  "Ghana exige aprobación previa de la Ghana Civil Aviation Authority (formulario R28-AF-001) antes de importar cualquier dron, con despacho de aduanas condicionado a esa autorización. Sin ella, el equipo puede ser retenido en frontera o aeropuerto. Restricciones adicionales: 10 km de aeropuertos/helipuertos, techo de 120 m (400 ft), línea de vista visual, sin vuelo nocturno sin permiso expreso.")

STARLINK_CALLOUT = ("ok", "Starlink activo en el país (verificar cobertura exacta antes de entrar)",
                     "Ghana figura entre los mercados africanos con servicio Starlink activo a mediados de 2026. Puede usarse como respaldo de comunicaciones, sin sustituir la SIM local (MTN, Telecel, AirtelTigo) en zonas urbanas. Revisar el mapa oficial 30-60 días antes por si cambia la cobertura o el marco regulatorio.")

DOG_MATRIX = [
    ("Parque Nacional de Kakum (pasarela y senderos)", "prohibido", "Dejar el perro en Cape Coast/Elmina con cuidador o rotación entre los viajeros."),
    ("Castillos de Elmina y Cape Coast (interior)", "permitido con condiciones", "El perro espera fuera durante la visita guiada obligatoria."),
    ("Accra, costa, Wli", "permitido con condiciones", "Correa y sombra; tráfico denso en Accra."),
]

SOURCES = [
    ("Digital Logistics Capacity Assessment · frontera de Elubo", "https://lca.logcluster.org/ghana-232-border-crossing-elubo"),
    ("Fragomen · nuevo sistema ETA/eVisa de Ghana (mayo 2026)", "https://www.fragomen.com/insights/ghana-new-electronic-travel-authorization-eta-and-evisa-requirements-visa-on-arrival-discontinued.html"),
    ("PetTravel · requisitos de importación de mascotas en Ghana", "https://www.pettravel.com/information/pet-passports/ghana-pet-import-requirements/"),
    ("Drone-Laws.com · normativa de drones en Ghana", "https://drone-laws.com/drone-laws-in-ghana/"),
    ("GCAA · preguntas frecuentes sobre RPAS/drones (PDF)", "https://www.gcaa.com.gh/web/wp-content/uploads/2023/RPAS/RPAS%20FAQs.pdf"),
    ("Embajada de España en Accra · contacto", "https://www.ayuntamiento-espana.es/embajada-de-espana-en-ghana-accra.html"),
    ("tech.africa · disponibilidad de Starlink en África (2026)", "https://tech.africa/starlink-africa/"),
    ("UNESCO · fortalezas y castillos de Ghana", "https://whc.unesco.org/en/list/34/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(5.0333, -2.8667), (5.0836, -1.3508), (5.1053, -1.2466), (5.3500, -1.3833), (5.5471, -0.1942), (7.1167, 0.5833), (6.1167, 1.2000)]

HISTORIA_RESUMEN = ("Ghana fue la Costa del Oro, uno de los grandes centros del comercio de oro y esclavos de África Occidental, y en 1957 se convirtió en el primer país subsahariano en independizarse del colonialismo europeo, bajo el liderazgo carismático de Kwame Nkrumah "
                     "y su visión panafricanista; tras un periodo de golpes militares, el país se ha consolidado desde los años noventa como una de las democracias más estables y admiradas de todo el continente.")

HISTORIA_SECCIONES = [
    ("El imperio ashanti y la Costa del Oro",
     "El poderoso imperio ashanti, con capital en Kumasi, dominó buena parte del territorio desde el siglo XVII, construyendo su riqueza sobre el comercio del oro y, trágicamente, también de esclavos hacia la costa; los castillos de Elmina y Cape Coast, construidos primero por los portugueses y luego disputados por holandeses y británicos, fueron puntos clave de embarque de esclavos hacia América, hoy Patrimonio de la Humanidad y lugares de memoria histórica visitables."),
    ("Colonia británica de la Costa del Oro",
     "Gran Bretaña estableció su colonia de la Costa del Oro a lo largo del siglo XIX, tras varias guerras contra el imperio ashanti, que finalmente fue anexionado en 1902; la colonia se convirtió en una de las más prósperas de África Occidental gracias a la exportación de cacao, mineral de oro y madera."),
    ("Independencia bajo Nkrumah y el panafricanismo",
     "Ghana se independizó en 1957, la primera colonia subsahariana en hacerlo, bajo el liderazgo de Kwame Nkrumah, una figura clave del panafricanismo que impulsó la creación de la Organización para la Unidad Africana; su gobierno, cada vez más autoritario y con una economía en dificultades, fue derrocado por un golpe militar en 1966, abriendo un periodo de casi dos décadas de inestabilidad política y golpes de Estado."),
    ("Situación actual: modelo de estabilidad democrática",
     "Desde el retorno al gobierno civil en 1992 bajo Jerry Rawlings, Ghana ha celebrado sucesivas elecciones competitivas con alternancia pacífica de poder, consolidándose como una de las democracias más estables de África y un destino habitual de memoria histórica afroamericana («Year of Return»); el descubrimiento de petróleo en 2007 y una economía diversificada (cacao, oro, servicios) sostienen hoy uno de los crecimientos más sólidos de la región."),
]

HISTORIA_FUENTES = [
    ("BBC News · Ghana country profile", "https://www.bbc.com/news/world-africa-13433790"),
    ("UNESCO · Castillos y fortalezas de Ghana", "https://whc.unesco.org/en/list/34/"),
    ("Encyclopaedia Britannica · Ghana, History", "https://www.britannica.com/place/Ghana/History"),
]

SPEC = dict(
    slug="ghana", name="Ghana", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Elubo (desde Costa de Marfil)"),
        ("SALIDA", "Aflao (hacia Togo)"),
        ("SEGURIDAD", "estable · precaución normal"),
        ("FRONTERA TERRESTRE", "Elubo muy transitada; Aflao urbana"),
        ("VISADO", "eVisa/ETA previa obligatoria (España no exenta)"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[5.7, -1.0], zoom=7,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Ghana se recorre por el eje costero histórico: los castillos de Elmina y Cape Coast (memoria de la trata atlántica, UNESCO), "
                   "la selva de Kakum con su pasarela de dosel, Accra como gran base logística y un desvío final a las cascadas de Wli antes de cruzar a Togo por Aflao, "
                   "el paso urbano más transitado de todo el tramo."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Costa de Marfil."),
        ("Entrada", "Elubo desde Costa de Marfil: paso más transitado de la subregión, carretera en buen estado."),
        ("Salida", "Aflao hacia Togo/Lomé: paso urbano, alto volumen de tráfico."),
        ("Visado", "Desde mayo de 2026, Ghana exige ETA o eVisa previa según nacionalidad; España no está exenta — tramitar eVisa antes de viajar."),
        ("Seguridad", "Estable, precaución normal en todo el país."),
        ("Comunicaciones", "Starlink activo; SIM local (MTN, Telecel, AirtelTigo) como base en ciudades."),
    ],
    alerts=[
        "Visado: sistema ETA/eVisa nuevo desde mayo de 2026 — verificar la categoría exacta para pasaporte español antes de viajar, ya que la exención antigua para varias nacionalidades ha cambiado.",
        "Dron: aprobación previa obligatoria de la GCAA (formulario R28-AF-001) antes de intentar introducirlo en el país.",
        "Kakum: perro prohibido en el parque y la pasarela — planificar cuidado o rotación.",
    ],
    ruta_intro="Tramo por el eje costero histórico, con desvío final al Volta antes de Togo.",
    route_rows=[
        ("Entrada y costa histórica", "Elubo → Elmina → Cape Coast", "Castillos UNESCO; visitas guiadas obligatorias en el interior"),
        ("Selva de Kakum", "Cape Coast → Kakum NP", "Pasarela de dosel; perro prohibido en el parque"),
        ("Accra", "Capital y servicios", "Base logística mayor antes del tramo final"),
        ("Hacia Togo", "Accra → Wli → Aflao", "Desvío al Volta opcional antes del paso urbano de Aflao"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto en este tramo: la red principal pavimentada cubre todo el itinerario previsto.",
    ],
    acampada=[
        "Cape Coast/Elmina: alojamientos con parking cerca de los castillos, opción más práctica que la acampada libre.",
        "Accra: aparcamiento vigilado recomendado por la densidad urbana y el tráfico.",
    ],
    visado=[
        "Desde el 25 de mayo de 2026, Ghana exige ETA (gratuita, para exentos previos de la Unión Africana/CEDEAO) o eVisa (de pago) según nacionalidad; España no está en la lista de exentos — tramitar eVisa con antelación.",
        "Procesamiento de eVisa: 72-96 h; llevar la aprobación impresa y en digital para el control fronterizo de Elubo.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
    ],
    fronteras_rows=[
        ("Entrada", "Elubo (Costa de Marfil)", "Paso más transitado de la subregión; carretera pavimentada, laissez-passer/C59 temporal para el vehículo."),
        ("Salida", "Aflao (Togo)", "Paso urbano integrado en la conurbación con Lomé; alto tráfico peatonal, prever demoras."),
    ],
    vehiculos=[
        "Laissez-passer/C59 temporal en Elubo, válido 30 días (renovable hasta 90); llevar carnet de conducir internacional y Carte Brune (CEDEAO).",
        "Peso y dimensiones controlados en básculas de carretera del eje Elubo-Accra: circular con la carga bien distribuida.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar aprobación previa a la GCAA (formulario R28-AF-001) antes de intentar introducir el dron en el país; sin ella, riesgo de retención en aduana.",
        "Tras la aprobación: mantener 10 km de separación de aeropuertos/helipuertos, techo de 120 m, línea de vista visual, sin vuelo nocturno sin permiso expreso, 30 m de edificios/vehículos sin autorización.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo confirmado a mediados de 2026: revisar el mapa oficial 30-60 días antes por posibles cambios.",
        "SIM local (MTN, Telecel, AirtelTigo) como conectividad principal en ciudades.",
    ],
    perro_intro=[
        "Permiso de importación obligatorio (válido 8 semanas desde su emisión), solicitado tras las pruebas de sangre correspondientes.",
        "Vacuna antirrábica administrada entre 30 días y 6 meses antes de la entrada; certificado veterinario oficial (Pet Health Certificate) del país de origen.",
        "Vacunas adicionales exigidas: moquillo, hepatitis, parvovirus y leptospirosis; tratamiento antiparasitario antes de la llegada.",
        "Sin cuarentena si se cumplen los requisitos; el incumplimiento puede derivar en cuarentena, devolución al país de origen o sacrificio, con costes a cargo del propietario — tramitar todo con margen suficiente.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "Seguro con evacuación médica: Accra concentra la mejor capacidad hospitalaria del tramo (Korle Bu).",
    ],
    seguridad_intro="País estable con precaución normal en todo el itinerario previsto; el paso de Aflao concentra el mayor volumen de tráfico y requiere paciencia, no alarma.",
    seguridad=[
        "Prever demoras en Aflao por el alto tráfico peatonal y comercial fronterizo con Togo.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
        "Revisar el aviso de Exteriores 72 h antes de entrar.",
    ],
    agua=[
        "Agua embotellada ampliamente disponible en todo el eje costero (Elubo, Cape Coast, Elmina, Accra); sin problema de suministro en este tramo.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones Shell/Total/GOIL de Cape Coast y Accra y los campings/guesthouses de la costa (Elmina, Busua) permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km: Elubo → Cape Coast/Elmina (~80 km) → Accra (~150 km) → Wli (~180 km) → Aflao (~170 km), todos con estaciones formales (GOIL, Total, Shell) de buena calidad.",
        "Repostar en Accra antes del desvío a Wli: oferta más limitada en la región del Volta.",
    ],
    pendientes=[
        ("Visado", "Confirmar categoría exacta (ETA/eVisa) para pasaporte español y tramitar con margen"),
        ("Dron", "Iniciar el trámite con la GCAA con antelación suficiente (formulario R28-AF-001)"),
        ("Kakum", "Planificar cuidado del perro durante la visita al parque"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Policía 191 · Bomberos 192 · Ambulancia 193 · Emergencia única 112. Emergencia consular española (Accra): +233 302 77 40 04.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

# -*- coding: utf-8 -*-
"""Nigeria — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Lagos (Lekki Conservation Centre)", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=6.4432, lon=3.6011,
         desc="Megaciudad y mayor base logística del golfo de Guinea: puerto, aeropuerto internacional, embajada de España, talleres y recambios de todo tipo. El Lekki Conservation Centre ofrece la pasarela colgante más larga de África sobre bosque de manglar, una pausa verde dentro de la ciudad.",
         credit="Ashinze · CC BY-SA 4.0", source=W + "LEKKI%20CONSERVATION%20CENTRE%20LAGOS%2C%20NIGERIA%20(LCC)%2006.jpg?width=900"),
    dict(n=2, name="Bosque Sagrado de Osun-Osogbo", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=7.7581, lon=4.5586,
         desc="Bosque sagrado a orillas del río Osun, Patrimonio Mundial UNESCO y santuario viviente del pueblo yoruba dedicado a la diosa Osun; esculturas y santuarios integrados en la vegetación, con el festival anual Osun-Osogbo como su expresión más conocida.",
         credit="Auskid1215 · CC BY-SA 4.0", source=W + "Osun-Osogbo%20Sacred%20Grove%2C%20Osun%20State.jpg?width=900"),
    dict(n=3, name="Benin City (Palacio del Oba)", cat="Cultura", prio="Media", dog="permitido con condiciones", time="medio día",
         lat=6.3350, lon=5.6037,
         desc="Antigua capital del Reino de Benín, cuna de los célebres bronces de Benín; el palacio del Oba sigue siendo sede activa de la monarquía tradicional edo, con guías locales que explican la historia del reino y de las piezas.",
         credit="Kelechukwu Ajoku · CC BY-SA 4.0", source=W + "Royal%20Palace%20of%20the%20Oba%20of%20Benin%20cropped.jpg?width=900"),
    dict(n=4, name="Calabar", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=4.9589, lon=8.3269,
         desc="Ciudad más ordenada y tranquila del itinerario nigeriano, antiguo puerto de la trata atlántica reconvertido en referencia de memoria histórica (Slave History Museum); última gran base de servicios antes del desvío a Obudu o del paso a Camerún por Mfum/Ekok.",
         credit="Otomeonoge · CC BY-SA 4.0", source=W + "Calabar%20carnival%209.jpg?width=900"),
    dict(n=5, name="Obudu Mountain Resort", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=6.6167, lon=9.4000,
         desc="Antiguo rancho ganadero colonial reconvertido en resort de montaña a 1.500 m de altitud, con teleférico, clima fresco y vistas sobre la meseta de Obudu; último punto de aclimatación antes del descenso hacia la frontera con Camerún.",
         credit="Bassnificient · CC BY-SA 4.0", source=W + "Obudu%20Mountain%20Resort%2002.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "patrimonio unesco": "marron", "cultura": "morado", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Kraké/Seme (desde Benín)", "Frontera", 6.3697, 2.7275,
     "Paso más transitado de África Occidental hacia Lagos; visado nigeriano ya tramitado, CPD y seguro Brown Card en regla. Alta congestión, varios filtros de control sucesivos."),
    ("Frontera · Salida — Mfum/Ekok (hacia Camerún)", "Frontera", 5.9450, 9.0600,
     "Cruce del río Cross State hacia Mamfe (región Suroeste de Camerún, zona de crisis anglófona). Ver alerta de seguridad específica antes de decidir esta salida."),
    ("Embajada de España en Abuja (también acreditada en Benín)", "Consular", 9.0579, 7.4951,
     "Consulado General de España en Lagos: 21C Kofo Abayomi St, Victoria Island, Lagos. Tel. +234 (0)1 2094603499 · Emergencia consular: +234 803 360 1658. Embajada en Abuja para trámites de visado y asuntos oficiales."),
    ("Lagos University Teaching Hospital (LUTH) — Lagos", "Hospital", 6.5194, 3.3486,
     "Principal hospital universitario y de referencia de Lagos; mejor capacidad del tramo para urgencias graves. Coordenada urbana aproximada."),
    ("Combustible · Lagos", "Combustible", 6.4432, 3.6011,
     "Mejor oferta del país (NNPC, Total, Oando); repostar aquí y comprobar precio, sujeto a variaciones frecuentes por política de subsidios."),
    ("Combustible · Benin City / Calabar", "Combustible", 6.3350, 5.6037,
     "Estaciones formales en el eje Lagos-Benin City-Calabar; confirmar disponibilidad real, con roturas de suministro puntuales fuera de las grandes ciudades."),
    ("Agua potable y de uso general · Lagos y Calabar", "Agua potable", 6.4432, 3.6011,
     "Agua embotellada («pure water» en bolsa o botella) ampliamente disponible; estaciones de servicio y hoteles de Lagos y Calabar permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Registro obligatorio al llegar + licencia de piloto (NCAA)",
                  "La Nigeria Civil Aviation Authority (NCAA) exige registro del dron a la llegada (documento «Recognition of Ownership» que debe acompañar cada vuelo) y licencia de piloto válida, con traducción al inglés recomendada. Techo 120 m (400 ft), línea de vista visual, solo de día, sin sobrevolar aglomeraciones, estadios ni agua sin autorización de control aéreo, y ninguna operación cerca de aeropuertos. El incumplimiento del registro puede acarrear multas o hasta 3 años de prisión.")

STARLINK_CALLOUT = ("ok", "Starlink activo en el país (verificar cobertura exacta antes de entrar)",
                     "Nigeria es uno de los mercados africanos con Starlink activo desde hace tiempo, con acuerdos recientes de expansión (incluida integración satélite-móvil con operadores locales). Puede usarse como respaldo de comunicaciones, sin sustituir la SIM local (MTN, Airtel, Glo) en zonas urbanas. Revisar el mapa oficial 30-60 días antes por si cambia la cobertura o el marco regulatorio.")

DOG_MATRIX = [
    ("Lagos, Benin City, Calabar, Obudu", "permitido con condiciones", "Correa siempre puesta; tráfico muy denso en Lagos, extremar precaución en cruces y mercados."),
]

SOURCES = [
    ("Destinali · viajar a Nigeria en vehículo propio", "https://destinali.com/nigeria-overland/"),
    ("Scoot West Africa · cruce de Seme/Kraké con e-visa nigeriano", "https://scootwestafrica.com/crossing-at-seme-krake-with-an-e-visa-for-nigeria/"),
    ("Nigeria Immigration Service · e-Visa oficial", "https://evisa.immigration.gov.ng/"),
    ("Federal Ministry of Information · nueva política de admisión temporal de vehículos (Nigeria Customs Service)", "https://fmino.gov.ng/nigeria-customs-service-commences-implementation-of-safe-passage-for-personal-vehicles-under-temporary-admission/"),
    ("Drone-Laws.com · normativa de drones en Nigeria", "https://drone-laws.com/drone-laws-in-nigeria/"),
    ("NCAA · portal de regulación de drones", "https://ncaa.gov.ng/media/news/ncaa-launches-new-digital-drone-regulation-portal/"),
    ("Consulado General de España en Lagos · contacto", "https://www.exteriores.gob.es/Consulados/lagos/es/Consulado/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx"),
    ("A Little Off Track · cruce de Mfum/Ekok hacia Camerún", "https://www.alittleofftrack.com/overlanding-cameroon/"),
    ("UNESCO · Bosque Sagrado de Osun-Osogbo", "https://whc.unesco.org/en/list/1118/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(6.3697, 2.7275), (6.4432, 3.6011), (7.7581, 4.5586), (6.3350, 5.6037), (4.9589, 8.3269), (6.6167, 9.4000), (5.9450, 9.0600)]

HISTORIA_RESUMEN = ("Nigeria es el país más poblado de África, un mosaico de más de 250 grupos étnicos forjado por fronteras coloniales británicas que unieron un norte musulmán haussa-fulani, un suroeste yoruba y un sureste igbo bajo un mismo Estado, cuyas fracturas desembocaron "
                     "en la guerra de Biafra (1967-1970); hoy es la mayor economía de África gracias al petróleo, aunque enfrenta desafíos de seguridad severos, en particular la insurgencia yihadista de Boko Haram en el noreste.")

HISTORIA_SECCIONES = [
    ("Reinos e imperios previos: Benín, los emiratos haussa y el califato de Sokoto",
     "El territorio albergó civilizaciones de gran sofisticación, entre ellas el reino de Benín (con su célebre arte en bronce, hoy objeto de disputas de restitución con museos europeos), la ciudad-estado yoruba de Ife, los emiratos haussa del norte y el califato de Sokoto, un poderoso Estado islámico fundado en 1804 tras la yihad de Usman dan Fodio."),
    ("El «Nigeria» de Lord Lugard y la amalgama colonial",
     "Gran Bretaña colonizó el territorio a finales del siglo XIX y, en 1914, el gobernador Frederick Lugard fusionó administrativamente los protectorados del norte y del sur en la colonia unificada de Nigeria, una «amalgama» puramente administrativa que unió bajo un mismo Estado a pueblos con religiones, lenguas y sistemas políticos muy distintos, sentando las bases de futuras tensiones interétnicas."),
    ("Independencia y la guerra civil de Biafra",
     "Nigeria se independizó en 1960. Tensiones étnicas y políticas entre el norte y el sureste igbo desembocaron en 1967 en la secesión de la autoproclamada República de Biafra y una guerra civil devastadora que se prolongó hasta 1970, con cientos de miles de muertos, muchos por hambruna, y que dejó una huella profunda en la memoria colectiva del país."),
    ("Situación actual: petróleo, Boko Haram y la mayor economía de África",
     "Tras décadas de gobiernos militares alternados con periodos civiles, Nigeria vive desde 1999 su periodo democrático más largo. El petróleo del delta del Níger sostiene la mayor economía de África, aunque con enormes desigualdades y contaminación ambiental severa en la región productora; desde 2009, la insurgencia yihadista de Boko Haram —y su escisión afín al Estado Islámico— mantiene un conflicto activo en el noreste, con episodios como el secuestro masivo de niñas de Chibok en 2014, un foco de inseguridad ajeno al eje sur/suroeste de este itinerario."),
]

HISTORIA_FUENTES = [
    ("BBC News · Nigeria country profile", "https://www.bbc.com/news/world-africa-13949550"),
    ("Encyclopaedia Britannica · Nigeria, History", "https://www.britannica.com/place/Nigeria/History"),
    ("Council on Foreign Relations · Boko Haram in Nigeria", "https://www.cfr.org/global-conflict-tracker/conflict/boko-haram-nigeria"),
]

SPEC = dict(
    slug="nigeria", name="Nigeria", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Kraké/Seme (desde Benín)"),
        ("SALIDA", "Mfum/Ekok (hacia Camerún) — ver alerta de ruta"),
        ("SEGURIDAD", "corredor sur estrecho; norte y sureste EXCLUIDOS"),
        ("VISADO", "tramitar semanas antes — sin visado de turismo en frontera"),
        ("CPD", "exigido; nueva admisión temporal complementaria (Nigeria Customs)"),
        ("REVALIDACIÓN", "30–60 días antes, y de nuevo 72 h antes de Mfum/Ekok"),
    ],
    center=[6.2, 6.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y de nuevo 72 h antes de la frontera con Camerún.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("Corredor sur estricto: Kraké/Seme → Lagos → Osun-Osogbo → Benin City → Calabar → Obudu → Mfum/Ekok. "
              "El norte de Nigeria (Boko Haram/ISWAP) y el sureste del delta del Níger (secuestros, criminalidad petrolera) quedan expresamente excluidos del itinerario. "
              "La salida hacia Camerún por Mfum/Ekok entra directamente en la región Suroeste, zona de conflicto activo de la crisis anglófona (ver alerta): revalidar esta decisión de ruta 72 h antes y no proceder sin información local actualizada."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Benín y antes de Camerún."),
        ("Entrada", "Kraké/Seme desde Benín: paso más transitado de la subregión hacia Lagos."),
        ("Salida", "Mfum/Ekok hacia Camerún: cruza el río Cross hacia Mamfe, en plena zona de crisis anglófona camerunesa."),
        ("Visado", "Nigeria no ofrece visado de turismo en frontera — e-Visa o visado consular imprescindible, tramitado semanas antes."),
        ("Seguridad", "Corredor sur (Lagos-Benin City-Calabar-Obudu) manejable con precaución alta; norte (Boko Haram/ISWAP) y sureste del delta del Níger, EXCLUIDOS del itinerario."),
        ("Comunicaciones", "Starlink activo; SIM local (MTN, Airtel, Glo) como base en ciudades."),
    ],
    alerts=[
        "Visado: NO existe visado de turismo en la frontera — tramitar el e-Visa o el visado consular con semanas de antelación; el visado de llegada está limitado a negocios con invitación de empresa nigeriana.",
        "Ruta excluida — norte de Nigeria: Boko Haram e ISWAP mantienen actividad armada activa en el noreste; fuera del itinerario sin excepción.",
        "Ruta excluida — sureste/delta del Níger: riesgo de secuestro y criminalidad ligada a la industria petrolera; el itinerario evita esta región por completo.",
        "Frontera de Mfum/Ekok hacia Camerún: entra directamente en la región Suroeste camerunesa, en conflicto activo (crisis anglófona) — revisar la alerta detallada en la ficha de Camerún antes de decidir esta salida; puede ser necesario replantear el paso a Camerún por una vía distinta o esperar una ventana de mayor calma.",
    ],
    ruta_intro="Corredor sur estricto entre las dos fronteras de Benín y Camerún, evitando por completo el norte y el delta del Níger.",
    route_rows=[
        ("Entrada y megaciudad", "Kraké/Seme → Lagos", "Base logística mayor; embajada y consulado español"),
        ("Patrimonio yoruba", "Lagos → Osun-Osogbo", "Bosque sagrado UNESCO; desvío corto desde el eje principal"),
        ("Antiguo reino", "Osun-Osogbo → Benin City", "Palacio del Oba, cuna de los bronces de Benín"),
        ("Hacia la frontera camerunesa", "Benin City → Calabar → Obudu", "Última gran base de servicios (Calabar) y aclimatación de montaña (Obudu)"),
        ("Salida — decisión de ruta", "Obudu → Mfum/Ekok", "Entra en zona de conflicto anglófono camerunés; revalidar 72 h antes"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: el corredor sur previsto es carretera asfaltada, con tráfico denso más que dificultad técnica.",
    ],
    acampada=[
        "Lagos: alojamientos con parking vigilado en Victoria Island/Lekki, opción única frente a la acampada libre en la megaciudad.",
        "Calabar y Obudu: hoteles y el propio resort de Obudu con aparcamiento seguro.",
    ],
    visado=[
        "e-Visa nigeriano obligatorio, tramitado con semanas de antelación desde un país de residencia; llevar la aprobación impresa y en digital.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
        "Verificar la vigencia y el tipo exacto de e-Visa 30-60 días antes: el sistema y los requisitos han cambiado varias veces en los últimos años.",
    ],
    fronteras_rows=[
        ("Entrada", "Kraké/Seme (Benín)", "Paso más transitado de la subregión; visado, CPD y seguro Brown Card ya en regla, varios filtros de control sucesivos."),
        ("Salida", "Mfum/Ekok (Camerún)", "Cruce del río Cross hacia Mamfe, región Suroeste en conflicto anglófono; revalidar la decisión de ruta 72 h antes."),
    ],
    vehiculos=[
        "CPD obligatorio, complementado desde 2026 por el nuevo «Temporary Vehicle Admission Permit» de la Nigeria Customs Service (hasta 90 días, prorrogable 30 más), que exige pasaporte, carnet de conducir internacional, ficha técnica, seguro y CPD.",
        "Carte Brune CEDEAO como seguro de responsabilidad civil regional — confirmar cobertura explícita de Nigeria.",
        "El vehículo no puede venderse, alquilarse, transferirse ni modificarse durante la admisión temporal; debe presentarse a la salida con la declaración aduanera aprobada.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Registrar el dron a la llegada ante la NCAA («Recognition of Ownership») y llevar licencia de piloto, con traducción al inglés si es necesario.",
        "Techo 120 m, línea de vista visual, solo de día, sin sobrevolar aglomeraciones ni agua sin autorización; nunca cerca de aeropuertos ni instalaciones militares.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo confirmado a mediados de 2026, con expansión reciente de acuerdos satélite-móvil: revisar el mapa oficial 30-60 días antes por posibles cambios.",
        "SIM local (MTN, Airtel, Glo) como conectividad principal en ciudades.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE).",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "LUTH (Lagos) como referencia hospitalaria del tramo; seguro con evacuación médica imprescindible dada la variabilidad de la atención sanitaria fuera de las grandes ciudades.",
    ],
    seguridad_intro="El corredor sur previsto (Lagos-Osun-Osogbo-Benin City-Calabar-Obudu) es manejable con precaución alta y sin desvíos; Nigeria es, junto con Camerún, el tramo de mayor exigencia de seguridad de todo el proyecto por el contraste entre zonas.",
    seguridad=[
        "No desviarse en ningún caso hacia el norte (Boko Haram/ISWAP) ni hacia el sureste del delta del Níger (secuestro, criminalidad petrolera): ambos quedan fuera del itinerario.",
        "Extremar la seguridad de convoy y check-in diario en todo el tramo nigeriano, con especial atención en la aproximación a Mfum/Ekok.",
        "Consultar MAEC España + fuentes locales (no solo internacionales) 72 h antes de cada frontera, dada la volatilidad de la información sobre el suroeste camerunés fronterizo.",
        "Llevar siempre el certificado de fiebre amarilla y copias completas de la documentación del vehículo, incluida la nueva admisión temporal de Aduanas.",
    ],
    agua=[
        "Lagos y Calabar: agua embotellada o en bolsa («pure water») ampliamente disponible; sin problema de suministro en las ciudades del itinerario.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio de Lagos, Benin City y Calabar y el resort de Obudu permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje principal: Kraké/Seme → Lagos (~90 km) → Osun-Osogbo (~250 km) → Benin City (~200 km) → Calabar (~350 km) → Obudu (~180 km), todos con estaciones formales (NNPC, Total, Oando).",
        "El precio y la disponibilidad de combustible en Nigeria están sujetos a variaciones frecuentes por la política de subsidios — llevar margen de reserva adicional y verificar el precio vigente al repostar.",
        "Repostar a fondo en Calabar antes de Obudu y de la aproximación final a Mfum/Ekok: última plaza con oferta amplia y garantizada.",
    ],
    pendientes=[
        ("Visado", "Tramitar el e-Visa nigeriano con semanas de antelación — condiciona toda la entrada por Kraké/Seme"),
        ("Admisión temporal del vehículo", "Confirmar el procedimiento exacto del nuevo permiso de Aduanas de Nigeria (2026) junto con el CPD"),
        ("Ruta de salida a Camerún", "Revalidar 72 h antes si Mfum/Ekok es viable o si hace falta replantear el paso por la crisis anglófona"),
        ("Dron", "Registrar ante la NCAA a la llegada o descartar el vuelo en el país"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Nigeria y la salida hacia Camerún son el tramo de mayor exigencia de revalidación de todo el proyecto.",
    emergency="Policía/Emergencia única 112 · Consulado General de España en Lagos: +234 (0)1 2094603499 · Emergencia consular: +234 803 360 1658.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

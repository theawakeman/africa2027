# -*- coding: utf-8 -*-
"""Egipto — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Alejandría", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=31.2001, lon=29.9187,
         desc="Puerto mediterráneo y punto de llegada previsto por mar (RoRo/contenedor desde Yibuti) o de salida hacia Europa; ciudad helenística de Alejandro Magno y la Biblioteca, hoy con buena oferta de talleres y agentes de aduanas para vehículos de expedición.",
         credit="Mmelouk · CC BY-SA 4.0", source=W + "Alexandria%20eastern%20harbor.jpg?width=900"),
    dict(n=2, name="Giza (pirámides y la Esfinge)", cat="Cultura", prio="Alta", dog="no recomendado", time="1–2 noches",
         lat=29.9792, lon=31.1342,
         desc="El conjunto monumental más famoso del planeta, a las puertas de El Cairo; visita imprescindible y muy transitada, con aparcamiento vigilado para vehículos grandes en el propio recinto.",
         credit="Kallerna · CC BY-SA 3.0", source=W + "Sphinx%20and%20the%20Great%20Pyramid%20of%20Giza%20panorama.jpg?width=900"),
    dict(n=3, name="Luxor (Valle de los Reyes y Karnak)", cat="Cultura", prio="Alta", dog="no recomendado", time="2 noches",
         lat=25.6872, lon=32.6396,
         desc="El mayor museo al aire libre del mundo: el templo de Karnak, el Valle de los Reyes y los Colosos de Memnón, en la orilla del Nilo a medio camino entre El Cairo y Asuán.",
         credit="Wouter Hagens · CC BY-SA 3.0", source=W + "Luxor%20Valley%20of%20the%20Kings%20D.jpg?width=900"),
    dict(n=4, name="Asuán y el lago Nasser", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=24.0889, lon=32.8998,
         desc="Ciudad más al sur del eje turístico del Nilo, con feluccas tradicionales y la Presa Alta; referencia histórica del cruce hacia Sudán por Wadi Halfa, hoy sin uso mientras dure el conflicto sudanés.",
         credit="Przemyslaw \"Blueshade\" Idzkiewicz · CC BY-SA 2.0", source=W + "Aswan%2C%20Elephantine%2C%20felucca%2C%20Egypt%2C%20Oct%202004.jpg?width=900"),
]

_CAT_COLOR = {"cultura": "morado", "naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Puerto · Entrada — Alejandría (RoRo/contenedor desde Yibuti vía Arabia Saudí)", "Frontera", 31.2001, 29.9187,
     "Punto de entrada previsto del proyecto dado el bloqueo del corredor de Sudán; gestionar el desembarco con un agente de aduanas egipcio (Automobile and Touring Club Egypt / EGA) antes de la llegada del barco."),
    ("Frontera · Qustul/Wadi Halfa (con Sudán) — sin uso mientras dure el conflicto", "Frontera", 22.2000, 31.6000,
     "Cruce histórico por el lago Nasser; descartado como vía de entrada real mientras persista la guerra civil de Sudán."),
    ("Puerto · Salida hacia Europa — Alejandría (Grimaldi, Neptune Lines)", "Frontera", 31.2001, 29.9187,
     "RoRo hacia Grecia/Chipre/Italia; la tripulación vuela por separado, el vehículo no puede viajar con personas a bordo del ferry de carga."),
    ("Embajada de España en El Cairo", "Consular", 30.0596, 31.2233,
     "41, Ismail Mohamed St., Zamalek, El Cairo. Tel. (0020) 227356437 · Emergencia consular 24h: (0020) 1223183783."),
    ("Kasr Al Ainy Hospital, El Cairo", "Hospital", 30.0300, 31.2300,
     "Principal hospital universitario de referencia de la capital; buena red de clínicas privadas también en El Cairo y Alejandría."),
    ("Combustible · El Cairo / Luxor / Asuán", "Combustible", 30.0444, 31.2357,
     "Estaciones formales (TotalEnergies, Mobil, estatales) en todo el eje turístico del Nilo; sin gap relevante de 500 km en el itinerario previsto."),
    ("Agua potable y de uso general · El Cairo y Luxor", "Agua potable", 30.0444, 31.2357,
     "Agua embotellada obligatoria para beber en todo el país (no beber del grifo); hoteles y campings de El Cairo, Luxor y Asuán permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("danger", "Prohibido en la práctica sin permiso militar previo — riesgo de confiscación",
                  "Egipto trata el uso de drones como asunto de seguridad nacional: se exige un permiso previo de las autoridades militares y de seguridad del Estado, un trámite lento y que en la práctica rara vez se concede a turistas. Volar sin autorización puede acarrear la confiscación del equipo e incluso problemas legales serios. Norma del proyecto: no introducir ni volar el dron en Egipto sin un permiso oficial ya concedido por escrito.")

STARLINK_CALLOUT = ("warn", "Sin fecha prevista de licencia a mediados de 2026",
                     "Egipto figura entre los países africanos sin fecha prevista de aprobación de licencia para Starlink a mediados de 2026. Tratar como no disponible y llevar SIM local (Vodafone Egypt, Orange, Etisalat) como conectividad principal.")

DOG_MATRIX = [
    ("Recintos arqueológicos (Giza, Karnak, Valle de los Reyes)", "no recomendado", "Normativa de los sitios y calor extremo desaconsejan llevar mascota; dejar en el vehículo con sombra y ventilación o con cuidador en el hotel."),
    ("El Cairo, Alejandría, Asuán", "permitido con condiciones", "Correa y sombra; calor muy intenso en verano, especialmente en Luxor y Asuán."),
]

SOURCES = [
    ("Overlanding Association · Egypt Overland (CPD, aduanas, RoRo hacia Europa)", "https://overlandingassociation.org/overland-wiki/egypt-overland/"),
    ("Overlanding Association · Shipping around Ethiopia (envío marítimo Yibuti-Egipto/Europa)", "https://overlandingassociation.org/overland-wiki/shipping-around-ethiopia/"),
    ("Embajada de España en El Cairo · contacto", "https://www.exteriores.gob.es/Embajadas/elcairo/es/Paginas/index.aspx"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("PetTravel.com · requisitos de importación de mascotas a Egipto", "https://www.pettravel.com/information/pet-passports/egypt-pet-import-requirements/"),
    ("UNESCO · Menfis y su necrópolis (pirámides de Giza a Dahshur), Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/86/"),
    ("UNESCO · Antigua Tebas y su necrópolis (Luxor), Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/87/"),
]

CORRIDOR = [(31.2001, 29.9187), (30.0444, 31.2357), (25.6872, 32.6396), (24.0889, 32.8998)]

HISTORIA_RESUMEN = ("Egipto reúne una de las civilizaciones continuas más largas de la historia, más de tres milenios de faraones seguidos por griegos, romanos, árabes y otomanos hasta la independencia de 1922 (plena desde 1952); "
                     "hoy cierra el itinerario africano de este viaje como el país de trámites aduaneros más exigentes de toda la ruta, precisamente por proteger su industria nacional del automóvil.")

HISTORIA_SECCIONES = [
    ("Tres milenios de faraones",
     "Unificado hacia el 3100 a.C., el antiguo Egipto se mantuvo como civilización continua durante más de tres mil años, con las pirámides de Giza (hacia 2560 a.C.) como su legado más célebre y Luxor —la antigua Tebas— como capital religiosa del Imperio Nuevo, "
     "sede de Karnak y del Valle de los Reyes, donde se enterró a Tutankamón y a decenas de faraones más."),
    ("Helenismo, Roma y la llegada del islam",
     "Alejandro Magno fundó Alejandría en 331 a.C. y, tras su muerte, la dinastía griega de los Ptolomeos gobernó Egipto hasta que Roma lo anexionó en el 30 a.C. tras la derrota de Cleopatra. "
     "El país permaneció bajo dominio romano y luego bizantino hasta la conquista árabe-musulmana del siglo VII, que introdujo el islam y transformó gradualmente la lengua y la cultura egipcias, sin borrar del todo la herencia copta cristiana que sobrevive hasta hoy."),
    ("Otomanos, protectorado británico e independencia",
     "Egipto pasó a manos otomanas en 1517 y, en el siglo XIX, vivió bajo la dinastía de Mehmet Ali una modernización acelerada que incluyó la construcción del canal de Suez (1869), obra que atrajo un fuerte endeudamiento y la posterior ocupación británica de facto desde 1882. "
     "La independencia formal llegó en 1922, aunque la presencia militar británica se mantuvo hasta la revolución de los Oficiales Libres de 1952, liderada por Gamal Abdel Nasser, que abolió la monarquía y nacionalizó el canal de Suez en 1956."),
    ("Situación actual: estabilidad en el Nilo, cierre del itinerario",
     "Tras décadas de gobiernos de partido único, la Primavera Árabe de 2011 derrocó a Hosni Mubarak, en un proceso convulso que desembocó en el gobierno actual. El eje turístico del Nilo (Alejandría-El Cairo-Luxor-Asuán) se mantiene estable y es uno de los circuitos "
     "más visitados y protegidos del país, mientras el norte del Sinaí concentra la actividad de seguridad más delicada. Para este proyecto, Egipto cierra el itinerario africano: el vehículo llega y sale por mar desde Alejandría, dado el bloqueo del corredor de Sudán — ver la decisión de ruta de esta ficha."),
]

HISTORIA_FUENTES = [
    ("BBC News · Egypt country profile", "https://www.bbc.com/news/world-africa-13315719"),
    ("Encyclopaedia Britannica · Egypt, History", "https://www.britannica.com/place/Egypt/History"),
    ("UNESCO · Menfis y su necrópolis (pirámides de Giza a Dahshur)", "https://whc.unesco.org/en/list/86/"),
    ("UNESCO · Antigua Tebas y su necrópolis (Luxor)", "https://whc.unesco.org/en/list/87/"),
]

SPEC = dict(
    slug="egipto", name="Egipto", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Alejandría por mar (RoRo/contenedor desde Yibuti) — acceso terrestre desde el sur BLOQUEADO"),
        ("SALIDA", "Alejandría, RoRo hacia Europa (Grecia/Chipre/Italia)"),
        ("SEGURIDAD", "estable · precaución normal (evitar Sinaí norte)"),
        ("VEHÍCULO", "CPD OBLIGATORIO con aval alto — el trámite más exigente del viaje"),
        ("COMUNICACIONES", "Starlink sin fecha prevista"),
        ("CIERRE", "último país del itinerario africano"),
    ],
    center=[27.5, 31.0], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y de nuevo 72 h antes de embarcar hacia Europa.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("El acceso terrestre a Egipto desde el sur está bloqueado por la guerra civil de Sudán (ver la ficha de Sudán): el cruce histórico de Wadi Halfa por el lago Nasser no es una opción viable mientras dure el conflicto. "
              "Decisión del proyecto: el vehículo llega a Egipto por mar, en un envío RoRo o en contenedor desde el puerto de Yibuti (en tránsito por Arabia Saudí) hasta Alejandría, mientras la tripulación vuela por separado y se reencuentra con el vehículo en el puerto. "
              "Una vez en Egipto, el itinerario recorre el eje clásico del Nilo (Alejandría-El Cairo/Giza-Luxor-Asuán) y cierra el viaje africano con un segundo envío RoRo desde Alejandría hacia Europa (Grecia, Chipre o Italia), de nuevo con la tripulación volando por separado. "
              "Egipto es, en términos aduaneros, el país más exigente de todo el proyecto: el Carnet de Passage es obligatorio y el aval bancario exigido puede alcanzar el 200% del valor declarado del vehículo, por lo que este trámite debe cerrarse con RACE con varios meses de antelación."),
    facts=[
        ("Ventana prevista", "Último país del itinerario africano, tras la decisión marítima de Sudán/Yibuti."),
        ("Entrada", "Por mar en Alejandría (RoRo/contenedor desde Yibuti); el acceso terrestre desde el sur está bloqueado."),
        ("Salida", "Por mar en Alejandría, RoRo hacia Grecia/Chipre/Italia; cierre del itinerario africano."),
        ("Seguridad", "País estable en el eje turístico del Nilo; evitar el norte del Sinaí, fuera de cualquier variante de esta ruta."),
        ("Vehículo", "CPD obligatorio con aval elevado (hasta el 200% del valor declarado); alternativa local vía ATCE/EGA con depósito negociable."),
        ("Comunicaciones", "Starlink sin fecha prevista de licencia; SIM local imprescindible."),
    ],
    alerts=[
        "Acceso terrestre desde el sur BLOQUEADO por la guerra de Sudán: no planificar ningún cruce por Wadi Halfa mientras dure el conflicto — ver la decisión de ruta de esta ficha y la ficha de Sudán.",
        "CPD: gestionar el aval con RACE con varios meses de antelación; declarar con cuidado el valor del vehículo, ya que el depósito exigido es proporcional a esa cifra.",
        "Dron: no introducirlo en el país sin permiso militar/de seguridad ya concedido por escrito — riesgo real de confiscación.",
        "Norte del Sinaí: fuera de cualquier variante de la ruta; el itinerario se limita al eje Alejandría-El Cairo-Luxor-Asuán.",
    ],
    ruta_intro="Llegada por mar a Alejandría, recorrido clásico del eje del Nilo (El Cairo/Giza, Luxor, Asuán) y cierre del viaje africano con un segundo envío marítimo hacia Europa desde el mismo puerto.",
    route_rows=[
        ("Llegada", "Puerto de Yibuti → mar → Alejandría", "RoRo/contenedor vía Arabia Saudí; tripulación por avión"),
        ("Capital y pirámides", "Alejandría → El Cairo/Giza", "Gestión de aduanas y agente local; visita a las pirámides"),
        ("Nilo alto", "El Cairo → Luxor → Asuán", "Karnak, Valle de los Reyes, feluccas del Nilo"),
        ("Cierre del viaje", "Asuán → Alejandría → mar → Europa", "RoRo hacia Grecia/Chipre/Italia; fin del itinerario africano"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: el eje Alejandría-El Cairo-Luxor-Asuán es carretera asfaltada de buen nivel en todo el recorrido.",
    ],
    acampada=[
        "El Cairo y Alejandría: hoteles y aparcamientos vigilados; sin acampada libre recomendada en zonas urbanas.",
        "Luxor y Asuán: campings orientados a overlanders junto al Nilo, con buena oferta de servicios.",
    ],
    visado=[
        "e-Visa o visado a la llegada disponible para ciudadanos españoles; tramitar con antelación para evitar colas en el puerto de desembarco.",
        "Confirmar 30-60 días antes cualquier requisito adicional derivado de la entrada por mar en lugar de por una frontera terrestre habitual.",
    ],
    fronteras_rows=[
        ("Entrada (por mar)", "Alejandría", "RoRo/contenedor desde Yibuti vía Arabia Saudí; gestionar agente de aduanas antes de la llegada."),
        ("Salida (por mar)", "Alejandría", "RoRo hacia Grecia/Chipre/Italia; la tripulación vuela por separado."),
    ],
    vehiculos=[
        "CPD obligatorio con aval elevado (hasta el 200% del valor declarado del vehículo); gestionar con RACE con varios meses de antelación dado el volumen del trámite.",
        "Alternativa local: Carnet a través de ATCE (Automobile and Touring Club Egypt) o EGA en el propio país, con depósitos negociables (referencia: aval de unos 8.000 USD para un vehículo de 25.000 USD).",
        "Matrícula temporal egipcia (\"ruchsa\") expedida en el puerto de entrada; verificar que VIN, número de motor y matrícula queden correctamente registrados antes de salir del recinto portuario.",
        "El seguro COMESA (yellow card) NO es válido en Egipto pese a parecerlo: comprar seguro de terceros local en el propio puerto de entrada.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No introducir el dron en el país sin autorización militar/de seguridad del Estado ya concedida por escrito.",
        "Valorar seriamente dejar el dron fuera de Egipto (enviado con el resto del envío marítimo a Europa) si no se dispone de tiempo para tramitar el permiso.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Sin fecha prevista de licencia a mediados de 2026: tratar como no disponible en todo el país.",
        "SIM local (Vodafone Egypt, Orange, Etisalat) como conectividad principal en todo el eje del Nilo.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente, vacuna antirrábica en vigor y microchip, exigibles en el puerto de entrada.",
        "No recomendado en los recintos arqueológicos (Giza, Karnak, Valle de los Reyes); dejar en el vehículo con sombra y ventilación o con cuidador en el hotel durante esas visitas.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Calor extremo en Luxor y Asuán, especialmente entre mayo y septiembre: hidratación reforzada y evitar exposición al mediodía.",
        "Agua del grifo no potable en todo el país: agua embotellada obligatoria para beber.",
        "Kasr Al Ainy Hospital (El Cairo) como mejor referencia sanitaria del tramo; buena red de clínicas privadas también en Alejandría y Luxor.",
    ],
    seguridad_intro="El eje turístico del Nilo (Alejandría-El Cairo-Luxor-Asuán) es un tramo estable y muy transitado; el norte del Sinaí queda fuera de cualquier variante de esta ruta.",
    seguridad=[
        "Ceñirse al eje clásico del Nilo; no desviarse hacia el norte del Sinaí bajo ninguna circunstancia.",
        "Precaución estándar frente a la venta agresiva y las estafas de guías no oficiales en Giza y Luxor.",
        "Aparcamiento vigilado en El Cairo y Alejandría por prudencia estándar frente a la delincuencia oportunista habitual de grandes ciudades.",
    ],
    agua=[
        "Agua embotellada obligatoria para beber en todo el país; no confiar en el agua del grifo en ningún punto del itinerario.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): hoteles y campings de El Cairo, Luxor y Asuán permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje previsto: Alejandría → El Cairo (~220 km) → Luxor (~670 km) → Asuán (~215 km), todos con estaciones formales.",
        "El Cairo, Luxor y Asuán concentran la mejor oferta del país (TotalEnergies, Mobil, estatales); repostar a fondo en cada ciudad antes de tramos de desierto.",
    ],
    pendientes=[
        ("CPD", "Cerrar el aval con RACE con varios meses de antelación dado el volumen exigido"),
        ("Envío marítimo de entrada", "Reservar el RoRo/contenedor desde Yibuti con antelación suficiente — ver ficha de Yibuti"),
        ("Envío marítimo de salida", "Reservar el RoRo de cierre desde Alejandría hacia Europa (Grimaldi, Neptune Lines)"),
        ("Dron", "Decidir si se tramita el permiso militar o se envía el dron directamente a Europa con el vehículo"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. La logística de entrada por mar debe cerrarse con antelación suficiente con un agente de envíos especializado en vehículos.",
    emergency="Emergencia consular española (El Cairo, 24h): (0020) 1223183783 · Embajada de España en El Cairo: (0020) 227356437.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

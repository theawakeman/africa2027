# -*- coding: utf-8 -*-
"""Madagascar — ficha aparte (revisión 11 sep 2026).

A diferencia del resto de fichas, Madagascar NO forma parte de la ruta 4x4
overland: es una isla sin conexión terrestre ni ferry de pasajero+vehículo
viable. Esta ficha existe para planificar una POSIBLE escapada en avión
durante el bloque sur/este del viaje, dejando los vehículos en el
continente. Por eso no hay corredor 4x4, CPD ni fronteras terrestres: se
adapta la misma plantilla de ficha a un viaje en avión + coche de alquiler o
conductor-guía local (habitual en Madagascar por el estado de las pistas).
"""
from data_common import make_ficha

POIS = [
    {"n": 1, "name": "Parque Nacional de Andasibe-Mantadia", "cat": "Selva y lémures", "prio": "Imprescindible",
     "dog": "no aplica (viaje en avión sin el perro)", "color": "verde", "time": "1 día",
     "lat": -18.9333, "lon": 48.4167,
     "desc": "El parque más visitado de Madagascar, a un par de horas de Antananarivo. Selva primaria y el canto inconfundible del indri, el lémur más grande, oíble a varios kilómetros.",
     "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Indri_indri_by_Frank_Vassen.jpg?width=900",
     "credit": "Frank Vassen · Wikimedia Commons (CC BY 2.0)",
     "source": "https://commons.wikimedia.org/wiki/File:Indri_indri_by_Frank_Vassen.jpg",
     "icon": "lémur / selva"},
    {"n": 2, "name": "Antsirabe", "cat": "Ciudad colonial de altura", "prio": "Recomendable",
     "dog": "no aplica", "color": "marron", "time": "1 día",
     "lat": -19.8667, "lon": 47.0333,
     "desc": "Ciudad colonial de tierras altas, talleres artesanos y el lago-cráter de Tritriva cerca. Punto de paso natural entre Antananarivo y el oeste.",
     "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Isalo_National_Park_01.jpg?width=900",
     "credit": "foto genérica de referencia — sustituir por una específica de Antsirabe cuando se verifique",
     "source": "https://commons.wikimedia.org/wiki/Category:Antsirabe",
     "icon": "ciudad / altura"},
    {"n": 3, "name": "Avenida de los Baobabs (Morondava)", "cat": "Paisaje icónico", "prio": "Imprescindible",
     "dog": "no aplica", "color": "naranja", "time": "media tarde (atardecer)",
     "lat": -20.2500, "lon": 44.4167,
     "desc": "Fila de baobabs Adansonia grandidieri de varios siglos, la imagen más reconocible de Madagascar. Se visita al atardecer; cerca, la Reserva de Kirindy para fauna nocturna.",
     "img": "https://commons.wikimedia.org/wiki/Special:FilePath/All%C3%A9e_des_Baobabs_near_Morondava,_Madagascar.jpg?width=900",
     "credit": "Wikimedia Commons",
     "source": "https://commons.wikimedia.org/wiki/File:All%C3%A9e_des_Baobabs_near_Morondava,_Madagascar.jpg",
     "icon": "árbol / paisaje"},
    {"n": 4, "name": "Parque Nacional Tsingy de Bemaraha", "cat": "Patrimonio UNESCO", "prio": "Imprescindible",
     "dog": "no aplica", "color": "gris", "time": "2 días",
     "lat": -18.9000, "lon": 44.7667,
     "desc": "Patrimonio de la Humanidad UNESCO: formaciones kársticas afiladas ('tsingy') recorridas con vía ferrata, puentes colgantes y escaleras. Pista dura desde Morondava, con vados y transbordador; requiere guía local obligatorio.",
     "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tsingy_de_Bemaraha_National_Park,_Madagascar.jpg?width=900",
     "credit": "Wikimedia Commons",
     "source": "https://commons.wikimedia.org/wiki/File:Tsingy_de_Bemaraha_National_Park,_Madagascar.jpg",
     "icon": "roca / patrimonio"},
    {"n": 5, "name": "Parque Nacional de Ranomafana", "cat": "Selva tropical y lémures", "prio": "Muy recomendable",
     "dog": "no aplica", "color": "verde", "time": "1 día",
     "lat": -21.2500, "lon": 47.4167,
     "desc": "Selva tropical de montaña en las tierras altas del centro-sur, con el lémur de bambú dorado (especie muy amenazada) y varias especies de sifaka. Buena combinación con Isalo si se sigue hacia el sur.",
     "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Milne-Edwards%27_sifaka_(Propithecus_edwardsi)_in_the_Ranomafana_National_Park,_Madagascar_(15881806706).jpg?width=900",
     "credit": "Wikimedia Commons",
     "source": "https://commons.wikimedia.org/wiki/File:Milne-Edwards%27_sifaka_(Propithecus_edwardsi)_in_the_Ranomafana_National_Park,_Madagascar_(15881806706).jpg",
     "icon": "lémur / selva"},
    {"n": 6, "name": "Parque Nacional de Isalo", "cat": "Cañones y formaciones rocosas", "prio": "Muy recomendable",
     "dog": "no aplica", "color": "naranja", "time": "1-2 días",
     "lat": -22.5667, "lon": 45.3667,
     "desc": "Paisaje de cañones, piscinas naturales y formaciones rocosas de aire jurásico. Senderismo con guía obligatorio desde la oficina del parque en Ranohira; hábitat de fosas y aves endémicas.",
     "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Isalo_National_Park_01.jpg?width=900",
     "credit": "Wikimedia Commons",
     "source": "https://commons.wikimedia.org/wiki/File:Isalo_National_Park_01.jpg",
     "icon": "cañón / senderismo"},
    {"n": 7, "name": "Nosy Be", "cat": "Playa y buceo", "prio": "Recomendable",
     "dog": "no aplica", "color": "turquesa", "time": "2-3 días",
     "lat": -13.3167, "lon": 48.2667,
     "desc": "La isla-balneario más conocida del norte: playas de arena blanca, buceo y snorkel, y salidas a islotes cercanos. Se llega en vuelo doméstico desde Antananarivo.",
     "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Nosy_Be_beach_(3186856441).jpg?width=900",
     "credit": "Wikimedia Commons",
     "source": "https://commons.wikimedia.org/wiki/File:Nosy_Be_beach_(3186856441).jpg",
     "icon": "playa / buceo"},
    {"n": 8, "name": "Nosy Boraha / Île Sainte-Marie", "cat": "Isla histórica y ballenas", "prio": "Opcional",
     "dog": "no aplica", "color": "morado", "time": "2 días",
     "lat": -16.9333, "lon": 49.8500,
     "desc": "Antiguo refugio de piratas del Índico, con un cementerio pirata histórico; playas tranquilas y, de junio a septiembre, paso de ballenas jorobadas frente a la costa.",
     "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sainte_marie_Madagascar_pirate_cemetery_2.JPG?width=900",
     "credit": "Wikimedia Commons",
     "source": "https://commons.wikimedia.org/wiki/File:Sainte_marie_Madagascar_pirate_cemetery_2.JPG",
     "icon": "isla / historia"},
]

LOGISTICS = [
    ("Aeropuerto Internacional Ivato (Antananarivo)", "Consular", -18.7969, 47.4788,
     "Único aeropuerto internacional relevante para esta escapada; vuelos domésticos de Air Madagascar/Tsaradia hacia Morondava, Nosy Be y otros puntos."),
    ("Hôpital Joseph Ravoahangy Andrianavalona (HJRA), Antananarivo", "Hospital", -18.9100, 47.5250,
     "Principal hospital de referencia del país, en la capital; fuera de Antananarivo la atención médica es muy limitada — seguro de evacuación fuertemente recomendado."),
    ("Centre ValBio, cerca de Ranomafana", "Servicio", -21.2550, 47.4200,
     "Centro de investigación con presencia médica básica ligada al parque; no sustituye una evacuación a Antananarivo en caso serio."),
]

FACTS = [
    ("Duración", "Escapada aparte de la ruta 4x4: 8-12 días si se combinan baobabs/Tsingy con Andasibe y/o el sur (Ranomafana-Isalo); menos si solo se hace un circuito"),
    ("Vehículo", "Los 4x4 de expedición se quedan en el continente; en Madagascar se alquila coche con conductor-guía o 4x4 de alquiler local — las pistas son duras y la señalización escasa"),
    ("Perro", "Se recomienda dejarlo con un cuidador de confianza en el continente durante esta escapada; llevarlo en avión exigiría permiso de importación y jaula homologada IATA, un trámite aparte que no compensa para un viaje corto"),
    ("Vuelos internos", "Varios destinos (Morondava, Nosy Be) se conectan mejor en vuelo doméstico que por carretera — las distancias por pista son largas y lentas"),
    ("Salud", "Malaria en todo el país salvo Antananarivo, con resistencia a cloroquina; fiebre amarilla si se llega desde país con riesgo; peste transmitida por pulgas presente en algunas zonas — profilaxis y repelente imprescindibles"),
    ("Drones", "Registro obligatorio ante la autoridad de aviación civil (ACM) antes de volar uno, salvo modelos muy pequeños sin sensores"),
]

ALERTS = [
    "Es una escapada EN AVIÓN, separada de la ruta 4x4 — no lleva los vehículos de expedición.",
    "Las pistas hacia Tsingy de Bemaraha y Morondava son duras y lentas incluso en 4x4 de alquiler; mejor con conductor-guía local que las conoce.",
    "Malaria en todo el país excepto la capital: profilaxis, repelente y mosquitera son obligatorios, no opcionales.",
    "El perro se queda en el continente con un cuidador — no está pensado para venir en esta escapada.",
]

ROUTE = [
    ("1", "Vuelo a Antananarivo (Ivato)", "Llegada, cambio de moneda, organizar coche/guía", "Confirmar eVisa impreso o en el móvil"),
    ("2", "Antananarivo → Andasibe-Mantadia", "Selva y el canto del indri", "Reservar guía del parque con antelación"),
    ("3", "Andasibe → Antananarivo → vuelo o carretera a Morondava", "Traslado hacia el oeste", "Valorar vuelo doméstico para ahorrar 1-2 días de pista"),
    ("4", "Morondava · Avenida de los Baobabs", "Atardecer entre baobabs; Kirindy si hay tiempo", "Repostar a fondo antes de continuar"),
    ("5-6", "Tsingy de Bemaraha", "Vía ferrata y formaciones kársticas con guía obligatorio", "Pista con vados y transbordador; salir con margen"),
    ("7", "Regreso a Morondava / Antananarivo", "Cierre del bloque oeste", "Vuelo doméstico recomendado de vuelta"),
    ("8-9", "Ranomafana", "Selva de montaña, lémur de bambú dorado", "Combinar con Isalo si el calendario lo permite"),
    ("10-11", "Isalo", "Cañones, piscinas naturales, senderismo con guía", "Oficina del parque en Ranohira"),
    ("12", "Vuelo de regreso al continente", "Cierre de la escapada", "Recoger al perro y retomar la ruta 4x4"),
]

VISADO = [
    "eVisa de turista obligatorio, trámite online en evisamada.gov.mg antes de volar (también existe visa on arrival como alternativa, más lenta); válido hasta 60 días de estancia única.",
    "Llevar el eVisa impreso o guardado en el móvil para el control policial a la llegada a Ivato.",
]

FRONTERAS_ROWS = [
    ("Entrada única", "Aeropuerto Internacional Ivato (Antananarivo)", "eVisa tramitado con antelación; sin conexión terrestre ni ferry de pasajero+vehículo con el continente"),
]

VEHICULOS = [
    "No aplica CPD ni matrícula temporal: los 4x4 de expedición no viajan a Madagascar.",
    "In situ: alquiler de 4x4 con o sin conductor-guía — muy recomendable con conductor por el estado de las pistas y la señalización.",
]

DRONES_CALLOUT = ("warn", "Registro obligatorio", "Todo dron debe registrarse ante la Autoridad de Aviación Civil (ACM) antes de volar, salvo modelos muy pequeños sin sensores; el procedimiento actual es por email a drone@acm.mg mientras se implanta una plataforma online.")
DRONES = [
    "Iniciar el registro con semanas de antelación: pasaporte, factura de compra, manual, fotos de los números de serie del dron y del mando.",
    "Sin restricciones publicadas por parque de forma centralizada — confirmar en cada oficina de parque (Isalo, Tsingy, Andasibe) antes de volar.",
]

STARLINK_CALLOUT = ("", "Estado por confirmar", "No se ha verificado la disponibilidad ni cobertura real de Starlink Roam en Madagascar para esta ficha — comprobar antes del viaje si es imprescindible mantener conexión en zonas remotas como Tsingy.")
STARLINK = [
    "Cobertura móvil razonable en ciudades y parques principales; débil o nula en pistas remotas hacia Tsingy de Bemaraha.",
]

PERRO_INTRO = [
    "Esta escapada está pensada SIN el perro: se queda con un cuidador de confianza en el continente durante los días que dure Madagascar.",
    "Si en algún momento se quisiera llevarlo, haría falta permiso de importación de animales, certificado veterinario internacional y jaula homologada IATA para el vuelo — un trámite propio que no compensa para una escapada corta.",
]

SALUD = [
    "Malaria en todo el país excepto Antananarivo, con resistencia a cloroquina — profilaxis específica indicada por Sanidad Exterior.",
    "Fiebre amarilla: certificado exigible si se llega desde país con riesgo de transmisión.",
    "Peste transmitida por pulgas presente en algunas zonas rurales; dengue, chikungunya y fiebre del Valle del Rift también descritos — repelente y ropa larga, sobre todo en temporada de lluvias (noviembre-abril).",
    "Vacunas recomendadas: fiebre tifoidea, hepatitis A, rabia (riesgo moderado) y las de calendario habituales.",
]

SEGURIDAD_INTRO = "Madagascar es en general un destino turístico estable, con precaución normal en ciudades grandes (carteristas, robos oportunistas) y atención al estado de las pistas más que a la seguridad personal."
SEGURIDAD = [
    "Antananarivo: cuidado habitual con carteristas y robos oportunistas, sobre todo de noche.",
    "Pistas remotas (Tsingy, sur): salir con margen de luz, agua y combustible; la asistencia en carretera es escasa.",
    "Contratar guía local obligatorio en los parques (Isalo, Tsingy, Andasibe) — no es solo recomendable, es la norma del país.",
]

PENDIENTES = [
    ("Duración real", "Decidir si esta escapada compensa dentro del calendario del bloque sur/este, y cuántos días dedicarle"),
    ("Cuidado del perro", "Cerrar con quién se queda el perro en el continente durante estos días"),
    ("Starlink/cobertura", "Confirmar si hace falta conexión garantizada en las pistas remotas"),
    ("Circuito definitivo", "Elegir entre el bloque oeste (baobabs + Tsingy), el bloque centro-sur (Ranomafana + Isalo) o ambos si el tiempo lo permite"),
]

SOURCES = [
    ("Road Trip Africa · Madagascar self-drive itineraries", "https://www.roadtripafrica.com/madagascar/itinerary/"),
    ("Road Trip Africa · The Baobab Route (14 días)", "https://www.roadtripafrica.com/madagascar/itinerary/the-baobab-route/"),
    ("Adventure Life · Madagascar Highlights", "https://www.adventure-life.com/africa/articles/madagascar-highlights"),
    ("SafariFind · Madagascar Visa for Spanish Citizens 2026", "https://www.safarifind.uk/blog/madagascar-visa-for-spanish-citizens-in-2026-requirements"),
    ("Portal oficial eVisa Madagascar", "https://evisamada.gov.mg"),
    ("Passport Health · Madagascar health risks & vaccines", "https://www.passporthealthusa.com/destination-advice/madagascar/"),
    ("CDC · Madagascar Traveler View", "https://wwwnc.cdc.gov/travel/destinations/traveler/none/madagascar"),
    ("WAU Madagascar · New Drone Regulations", "https://waumadagascar.com/blog/new-drone-regulations-in-madagascar-what-travelers-and-operators-need-to-know"),
    ("Wikivoyage · Ranomafana / Isalo / Tsingy de Bemaraha", "https://en.wikivoyage.org/wiki/Madagascar"),
    ("MAEC España · Embajada en Pretoria, también competente en Madagascar", "https://www.exteriores.gob.es/Embajadas/pretoria/es/Embajada/tambien-somos-tu-embajada-en/Paginas/Madagascar.aspx"),
]

SPEC = dict(
    slug="madagascar", name="Madagascar", revision="11 sep 2026",
    sub="Escapada en avión (fuera de la ruta 4x4) · sin vehículos · sin perro",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/All%C3%A9e_des_Baobabs_near_Morondava,_Madagascar.jpg?width=1200",
    hero_credit="Avenida de los Baobabs, Morondava · Wikimedia Commons",
    chips=[
        ("MODALIDAD", "Vuelo, sin los 4x4"),
        ("RITMO", "8-12 días si se hace"),
        ("PERRO", "se queda en el continente"),
        ("VISADO", "eVisa obligatorio"),
        ("ESTADO", "Ficha exploratoria — por confirmar si se hace"),
    ],
    center=[-19.5, 46.5], zoom=6,
    notice="Ficha de una posible escapada EN AVIÓN durante el bloque sur/este del viaje — no forma parte de la ruta 4x4 ni lleva los vehículos de expedición.",
    verificado=False,
    pois=POIS,
    logistics=LOGISTICS,
    corridor=[],
    facts=FACTS,
    alerts=ALERTS,
    decision="Escapada opcional, a decidir según el calendario del bloque sur/este. Si se hace, deja los dos 4x4 aparcados en el continente (por ejemplo en Tanzania o Kenia) y se vuela desde ahí o desde Sudáfrica.",
    ruta_intro="Itinerario modular: el bloque oeste (baobabs + Tsingy) es el más icónico y compacto; el bloque centro-sur (Ranomafana + Isalo) añade selva y cañones si hay más días.",
    route_rows=ROUTE, route_headers=("Día", "Tramo", "Objetivo", "Condición"),
    visado=VISADO,
    fronteras_rows=FRONTERAS_ROWS,
    vehiculos=VEHICULOS,
    drones_callout=DRONES_CALLOUT, drones=DRONES,
    starlink_callout=STARLINK_CALLOUT, starlink=STARLINK,
    perro_intro=PERRO_INTRO,
    salud=SALUD,
    seguridad_intro=SEGURIDAD_INTRO, seguridad=SEGURIDAD,
    pendientes=PENDIENTES,
    sources=SOURCES,
    sources_note="Ficha exploratoria de una escapada opcional en avión — consulta realizada el 11 de septiembre de 2026; verificar visado, salud y estado de pistas antes de decidir si se hace.",
    emergency="Policía 117 · Bomberos 118 · Gendarmería 119 (cobertura y respuesta muy variables fuera de Antananarivo). España no tiene embajada en Madagascar: hay un Consulado Honorario en Antananarivo (+261 20 22 222 31 · ch.espagne@consulat.mg), bajo la Embajada de España en Pretoria (Sudáfrica), que es quien tiene la competencia plena.",
    matrix_note="Coordenadas de referencia general (parques y ciudades), no verificadas punto a punto como en las fichas de la ruta 4x4 — esta es una ficha exploratoria.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

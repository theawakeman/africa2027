#!/usr/bin/env python3
"""Aplica la auditoría explícita del grupo 6: Uganda, Ruanda y Malaui.

Los pines se contrastaron uno a uno con el objeto o acceso visible de Google
Maps. Las fotografías se escogieron tras leer título, descripción, autor y
licencia en la API de Wikimedia Commons; no hay relleno automático.
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]


FICHA_REPLACEMENTS: dict[str, tuple[tuple[str, str], ...]] = {
    "uganda": (
        (
            "En esta revisión NO se pudo acceder a commons.wikimedia.org desde la sesión (bloqueo de red), así que solo dos PDIs llevan foto verificada. Pendiente: completar los nombres de archivo de Wikimedia Commons de los 18 PDIs restantes, verificándolos uno a uno. No inventarlos",
            "Auditoría cerrada el 15 de septiembre de 2026: los 20 PDIs tienen fotografías exactas y trazables. Se contrastaron 60 archivos de Wikimedia Commons y los 20 puntos disponen de galería; autor, licencia, pie y página de origen se conservan en cada ficha ampliada.",
        ),
        (
            "Última revisión de esta versión: 12 de septiembre de 2026.",
            "Última revisión de esta versión: 15 de septiembre de 2026.",
        ),
    ),
    "ruanda": (
        (
            "En esta revisión NO se pudo acceder a commons.wikimedia.org desde la sesión (bloqueo de red), así que solo dos PDIs llevan foto verificada. Pendiente: completar los nombres de archivo de Wikimedia Commons de los 16 PDIs restantes, verificándolos uno a uno. No inventarlos",
            "Auditoría cerrada el 15 de septiembre de 2026: los 18 PDIs tienen fotografías exactas y trazables. Se contrastaron 54 archivos de Wikimedia Commons y los 18 puntos disponen de galería; autor, licencia, pie y página de origen se conservan en cada ficha ampliada.",
        ),
        (
            "Última revisión de esta versión: 12 de septiembre de 2026.",
            "Última revisión de esta versión: 15 de septiembre de 2026.",
        ),
    ),
    "malaui": (
        (
            "Los 22 PDIs usan solo las cinco imágenes de Malaui ya verificadas en el proyecto, porque en esta revisión commons.wikimedia.org no era accesible desde el entorno de trabajo. Los 17 PDIs que llevan foto prestada lo dicen en su descripción: sustituir una a una cuando se puedan verificar nombres de archivo",
            "Auditoría cerrada el 15 de septiembre de 2026: los 22 PDIs tienen fotografías exactas y trazables. Se contrastaron 59 archivos de Wikimedia Commons y 20 puntos disponen de galería; Manchewe Falls y Livingstone Tree mantienen una única imagen exacta en vez de rellenarse con fotografías ajenas.",
        ),
        (
            "Última revisión de esta versión: 12 de septiembre de 2026.",
            "Última revisión de esta versión: 15 de septiembre de 2026.",
        ),
    ),
}


def commons(filename: str, credit: str, caption: str) -> dict[str, str]:
    encoded = quote(filename.replace(" ", "_"), safe="(),-._~")
    return {
        "img": f"https://commons.wikimedia.org/wiki/Special:FilePath/{encoded}?width=1200",
        "source": f"https://commons.wikimedia.org/wiki/File:{encoded}",
        "credit": credit,
        "caption": caption,
    }


COORDS: dict[str, dict[int, tuple[float, float]]] = {
    "uganda": {
        1: (1.3380390, 34.3797112), 2: (1.1184119, 34.5260918),
        3: (0.4219667, 33.1939700), 4: (0.3361437, 32.5825700),
        5: (0.0620109, 32.4792744), 6: (-0.3095222, 32.2914626),
        7: (1.4483053, 32.0776534), 8: (2.2784825, 31.6854957),
        9: (3.7399407, 33.7308169), 10: (3.0157765, 32.3177336),
        11: (0.4972007, 30.3284158), 12: (0.4368086, 30.3951215),
        13: (0.3423867, 30.0441325), 14: (-0.1276134, 29.8670563),
        15: (-0.1869974, 29.9006375), 16: (-0.5858030, 29.7175670),
        17: (-0.9877780, 29.6163890), 18: (-1.3547836, 29.6190763),
        19: (-1.2711134, 29.9391462), 20: (-0.5314967, 31.0164031),
    },
    "ruanda": {
        1: (-1.5036800, 29.6132300), 2: (-1.4445561, 29.4967457),
        3: (-1.4619444, 29.4858333), 4: (-1.4732680, 29.4846160),
        5: (-1.4801217, 29.7390696), 6: (-1.7033608, 29.2587778),
        7: (-2.0616008, 29.3483403), 8: (-2.0600136, 29.3477473),
        9: (-2.4911606, 28.8930143), 10: (-2.4786176, 29.2002976),
        11: (-2.5887351, 29.7452954), 12: (-2.3601536, 29.7406071),
        13: (-1.9466888, 30.0532142), 14: (-1.9307690, 30.0605135),
        15: (-2.1490625, 30.0936760), 16: (-1.8416233, 30.2279998),
        17: (-1.8787340, 30.7035770), 18: (-1.8164718, 29.3509978),
    },
    "malaui": {
        1: (-9.9417840, 33.9225836), 2: (-10.6117056, 34.1130061),
        3: (-10.5862618, 34.1201458), 4: (-10.5880293, 33.8115589),
        5: (-12.0115721, 33.8644002), 6: (-11.6069181, 34.3012235),
        7: (-11.9211028, 34.1718230), 8: (-12.0642185, 34.7381655),
        9: (-12.8502645, 34.1711193), 10: (-12.9314917, 34.2980250),
        11: (-13.7519505, 34.6165033), 12: (-12.9092303, 33.1688883),
        13: (-13.9720199, 33.7835383), 14: (-14.3173823, 34.2698215),
        15: (-14.2813689, 34.5094255), 16: (-14.0647224, 34.8844867),
        17: (-15.0385611, 35.2542643), 18: (-15.3500070, 35.3292954),
        19: (-15.7933029, 35.0134321), 20: (-15.9396270, 35.4976271),
        21: (-16.0536289, 35.1124764), 22: (-15.9092875, 34.7422031),
    },
}


LINKS: dict[str, dict[int, list[dict[str, str]]]] = {
    "uganda": {
        1: [{"label": "UWA · Sipi y guía de Mount Elgon", "url": "https://ugandawildlife.org/national-parks/mount-elgon-national-park/"}],
        2: [{"label": "UWA · Mount Elgon National Park", "url": "https://ugandawildlife.org/national-parks/mount-elgon-national-park/"}],
        3: [{"label": "Jinja District · Source of the Nile", "url": "https://www.jinja.go.ug/opportunities/tourism"}],
        4: [{"label": "Uganda Museums · aviso y visitas", "url": "https://museums.tourism.go.ug/"}],
        5: [{"label": "NARO · Entebbe Botanical Gardens", "url": "https://naro.go.ug/naris/narl/"}],
        6: [{"label": "Uganda Tourism Board · islas Ssese", "url": "https://utb.go.ug/why-you-need-to-visit-the-84-ssese-islands-2/"}],
        7: [{"label": "Ziwa Rhino & Wildlife Ranch · visita", "url": "https://ziwarhino.com/index/"}],
        8: [{"label": "UWA · Murchison Falls National Park", "url": "https://ugandawildlife.org/national-parks/murchison-falls-national-park/"}],
        9: [{"label": "UWA · Kidepo Valley National Park", "url": "https://ugandawildlife.org/national-parks/kidepo-valley-national-park/"}],
        10: [{"label": "Fort Patiko · contexto y visita", "url": "https://en.wikipedia.org/wiki/Fort_Patiko"}],
        11: [{"label": "Fort Portal · lagos de cráter", "url": "https://en.wikipedia.org/wiki/Fort_Portal"}],
        12: [{"label": "UWA · Kibale National Park", "url": "https://ugandawildlife.org/national-parks/kibale-national-park/"}],
        13: [{"label": "UNESCO · Rwenzori Mountains National Park", "url": "https://whc.unesco.org/en/list/684/"}],
        14: [{"label": "UWA · Queen Elizabeth National Park", "url": "https://ugandawildlife.org/national-parks/queen-elizabeth-national-park/"}],
        15: [{"label": "UWA · Queen Elizabeth National Park", "url": "https://ugandawildlife.org/national-parks/queen-elizabeth-national-park/"}],
        16: [{"label": "UWA · Queen Elizabeth e Ishasha", "url": "https://ugandawildlife.org/national-parks/queen-elizabeth-national-park/"}],
        17: [{"label": "UNESCO · Bwindi Impenetrable National Park", "url": "https://whc.unesco.org/en/list/682/"}],
        18: [{"label": "UWA · Mgahinga Gorilla National Park", "url": "https://ugandawildlife.org/national-parks/mgahinga-gorilla-national-park/"}],
        19: [{"label": "Uganda Tourism Board · alojamientos autorizados en Bunyonyi", "url": "https://utb.go.ug/licensed-facilities/"}],
        20: [{"label": "UWA · Lake Mburo National Park", "url": "https://ugandawildlife.org/national_parks/lake-mburo/"}],
    },
    "ruanda": {
        1: [{"label": "Visit Rwanda · cuevas de Musanze", "url": "https://visitrwanda.com/interests/caving/"}],
        2: [{"label": "Visit Rwanda · Volcanoes National Park", "url": "https://visitrwanda.com/destinations/volcanoes-national-park/"}],
        3: [{"label": "Visit Rwanda · senderos volcánicos", "url": "https://visitrwanda.com/interests/hiking/"}],
        4: [{"label": "Dian Fossey Gorilla Fund · campus y legado", "url": "https://gorillafund.org/ellen-campus/"}],
        5: [{"label": "Visit Rwanda · Musanze y lagos gemelos", "url": "https://visitrwanda.com/destinations/musanze/"}],
        6: [{"label": "Visit Rwanda · Rubavu", "url": "https://visitrwanda.com/destinations/rubavu/"}],
        7: [{"label": "Visit Rwanda · Congo Nile Trail", "url": "https://visitrwanda.com/interests/cycling/"}],
        8: [{"label": "Visit Rwanda · lago Kivu y Karongi", "url": "https://visitrwanda.com/destinations/lake-kivu/"}],
        9: [{"label": "MAEC · recomendación de viaje para Ruanda", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Ruanda"}],
        10: [{"label": "Visit Rwanda · pasarela del dosel de Nyungwe", "url": "https://visitrwanda.com/interests/canopy-walkway/"}],
        11: [{"label": "Rwanda Cultural Heritage Academy · Museo Etnográfico", "url": "https://www.rwandaheritage.gov.rw/en/museum-and-heritages-sites-management-division-1"}],
        12: [{"label": "Rwanda Cultural Heritage Academy · King’s Palace", "url": "https://www.rwandaheritage.gov.rw/en/museum-and-heritages-sites-management-division-1"}],
        13: [{"label": "Rwanda Cultural Heritage Academy · Kandt House", "url": "https://www.rwandaheritage.gov.rw/en/museum-and-heritages-sites-management-division-1"}],
        14: [{"label": "Kigali Genocide Memorial · preparar la visita", "url": "https://kgm.rw/visit/know-before-you-go/"}],
        15: [{"label": "UNESCO · memoriales de Nyamata, Murambi, Gisozi y Bisesero", "url": "https://whc.unesco.org/en/list/1586/"}],
        16: [{"label": "Lago Muhazi · localización y contexto", "url": "https://en.wikipedia.org/wiki/Lake_Muhazi"}],
        17: [{"label": "Akagera · acceso, actividades y autoconducción", "url": "https://visitakagera.org/"}],
        18: [{"label": "Gishwati-Mukura · guía práctica del parque", "url": "https://www.cepf.net/resources/documents/guidebook-gishwati-mukura-national-park"}],
    },
    "malaui": {
        1: [{"label": "Visit Malawi · Karonga y su museo", "url": "https://visitmalawi.mw/karonga/"}],
        2: [{"label": "Visit Malawi · museos y Stone House", "url": "https://visitmalawi.mw/museums-and-monuments/"}],
        3: [{"label": "Malawi Tourism · Livingstonia y Manchewe", "url": "https://www.malawitourism.com/regions/north-malawi/livingstonia-mission/"}],
        4: [{"label": "Visit Malawi · región norte y Nyika", "url": "https://visitmalawi.mw/northern-region/"}],
        5: [{"label": "Visit Malawi · región norte y Mzuzu", "url": "https://visitmalawi.mw/northern-region/"}],
        6: [{"label": "Visit Malawi · región norte y Nkhata Bay", "url": "https://visitmalawi.mw/northern-region/"}],
        7: [{"label": "Visit Malawi · Bandawe Mission", "url": "https://visitmalawi.mw/northern-region/"}],
        8: [{"label": "Malawi Tourism · Likoma Island", "url": "https://www.malawitourism.com/regions/north-malawi/likoma-island/"}],
        9: [{"label": "African Parks · Nkhotakota", "url": "https://www.africanparks.org/the-parks/nkhotakota"}],
        10: [{"label": "Visit Malawi · museos y monumentos", "url": "https://visitmalawi.mw/museums-and-monuments/"}],
        11: [{"label": "Visit Malawi · región central y Senga Bay", "url": "https://visitmalawi.mw/central-region/"}],
        12: [{"label": "Visit Malawi · región central y Kasungu", "url": "https://visitmalawi.mw/central-region/"}],
        13: [{"label": "Lilongwe Wildlife Centre · guía oficial de visita", "url": "https://lilongwewildlife.org/wp-content/uploads/2024/04/LWC-Visitor-Guide-1.pdf"}],
        14: [{"label": "UNESCO · Chongoni Rock-Art Area", "url": "https://whc.unesco.org/en/list/476/"}],
        15: [{"label": "Kungoni Centre · museo y talleres de Mua", "url": "http://www.kungoni.org/"}],
        16: [{"label": "UNESCO · Lake Malawi National Park", "url": "https://whc.unesco.org/en/list/289/"}],
        17: [{"label": "African Parks · visita a Liwonde", "url": "https://www.africanparks.org/the-parks/liwonde/park-revenue-generation"}],
        18: [{"label": "Visit Malawi · región sur y meseta de Zomba", "url": "https://visitmalawi.mw/southern-region/"}],
        19: [{"label": "Society of Malawi · biblioteca y archivo en Mandala House", "url": "https://societyofmalawi.wordpress.com/about/"}],
        20: [{"label": "UNESCO · paisaje cultural de Mount Mulanje", "url": "https://whc.unesco.org/en/list/1201/"}],
        21: [{"label": "Satemwa Tea Estate · visitas y finca", "url": "https://www.satemwa.com/"}],
        22: [{"label": "African Parks · Majete", "url": "https://www.africanparks.org/the-parks/majete"}],
    },
}


NAMES = {
    "uganda": {4: "Kampala · Museo de Uganda y base logística", 10: "Fort Patiko · historia del norte", 11: "Lago Nyabikere y cráteres de Fort Portal", 13: "Rwenzori · acceso por Nyakalengija", 15: "Canal de Kazinga · embarcadero de Mweya", 19: "Lago Bunyonyi · base de Rutinda"},
    "ruanda": {1: "Cuevas de Musanze", 2: "Volcanoes National Park · acceso de Kinigi", 7: "Congo Nile Trail · tramo de Karongi", 13: "Kigali · Kandt House y base logística", 15: "Memorial de Nyamata"},
    "malaui": {4: "Nyika National Park · Chelinda", 5: "Mzuzu · base logística del norte", 7: "Bandawe Mission y costa de Chintheche", 9: "Nkhotakota Wildlife Reserve", 10: "Nkhotakota histórico · Livingstone Tree", 13: "Lilongüe · Wildlife Centre y base logística", 14: "Chongoni · arte rupestre en Chentcherere", 15: "Mua · Kungoni Centre", 16: "Cabo Maclear · Lake Malawi National Park", 17: "Liwonde National Park", 18: "Zomba Plateau · Queen’s View", 19: "Blantyre · Mandala House y base logística", 20: "Mount Mulanje · acceso por Likhubula", 21: "Satemwa · plantaciones de té de Thyolo", 22: "Majete Wildlife Reserve"},
}


CONTENT: dict[str, dict[int, dict[str, object]]] = {
    "uganda": {
        1: {"desc": "Tres saltos sobre los acantilados de Mount Elgon, con el principal cayendo frente a una amplia llanura. La visita exige guía local para enlazar miradores y comprobar barro, niebla y bordes.", "visit": {"why": "Es la cascada más escénica del este de Uganda y una parada clara antes de subir a Elgon.", "see": "Salto principal, otros dos niveles y paisaje cafetero; no todas las rutas incluyen los tres.", "access": "El pin coincide con Sipi Falls en Google Maps. Contratar guía acreditado y dejar el coche en estacionamiento acordado.", "when": "Primera hora y tiempo estable; tras lluvias hay más caudal pero también senderos resbaladizos.", "skip": "Descartarlo con tormenta, niebla cerrada o si no hay tiempo para una ruta guiada segura."}},
        2: {"desc": "Antiguo volcán transfronterizo cuya cumbre ugandesa, Wagagai, alcanza 4.321 m junto a una enorme caldera. Es una travesía de varios días, no una excursión añadida a Sipi.", "visit": {"why": "Ofrece alta montaña menos concurrida, páramo afroalpino y una caldera de escala excepcional.", "see": "Bosque, bambú, lobelias, brezos, caldera y pico Wagagai según el itinerario contratado.", "access": "El pin marca el pico Wagagai real; la entrada y ruta deben fijarse con UWA y guía antes de salir.", "when": "Ventanas relativamente secas y con varios días reservados; llevar abrigo y equipo impermeable.", "skip": "No intentarlo sin permiso, guía, previsión meteorológica y margen suficiente para aclimatar y regresar."}},
        3: {"desc": "El monumento de Speke junto al nacimiento del Nilo Blanco convierte Jinja en una visita concreta, complementada por paseos en barca y rápidos río abajo. El punto histórico es interpretativo: el lago Victoria alimenta el río a través de una zona amplia.", "visit": {"why": "Une geografía, historia de la exploración europea y vida actual del Nilo en una parada fácil.", "see": "Monumento de Speke, salida del lago, aves y, con operador, perspectiva desde el agua.", "access": "El pin coincide con Speke Memorial Monument en Google Maps; aparcar dentro del recinto autorizado.", "when": "Por la mañana, con mejor luz y antes del calor; reservar aparte cualquier actividad acuática.", "skip": "No confundir el monumento con una coordenada hidrológica única ni contratar barca sin chalecos."}},
        4: {"desc": "Kampala es el nodo principal para talleres, recambios, hospitales y trámites. La ficha se ancla en el Museo de Uganda; su web oficial advierte de cierre temporal por obras, por lo que hay que comprobar la reapertura.", "visit": {"why": "Es la escala logística imprescindible y, si reabre, el museo ofrece la mejor introducción general al país.", "see": "Colecciones arqueológicas, etnográficas y musicales; Kasubi es una visita separada y exige confirmar acceso.", "access": "El pin coincide con Uganda Museum en Google Maps. Evitar horas punta y usar estacionamiento vigilado.", "when": "Día laborable para resolver gestiones; consultar el aviso oficial del museo antes de desplazarse.", "skip": "No dedicar jornada turística al museo mientras conste cerrado ni mover el vehículo de noche sin necesidad."}},
        5: {"desc": "Jardín botánico histórico junto al lago Victoria, con grandes árboles, aves y senderos sombreados cerca del aeropuerto. Es una parada suave, distinta de una reserva de fauna.", "visit": {"why": "Permite caminar y observar vegetación tropical sin alejarse de la base logística de Entebbe.", "see": "Arboledas, plantas cultivadas, monos y orilla; los avistamientos nunca están garantizados.", "access": "El pin coincide con Entebbe Botanical Garden en Google Maps; confirmar horario y entrada en la puerta.", "when": "Mañana fresca y sin lluvia fuerte, evitando terminar al anochecer junto al lago.", "skip": "Omitirlo si está cerrado, el suelo está anegado o la escala aeroportuaria deja poco margen."}},
        6: {"desc": "Archipiélago de 84 islas en el lago Victoria; Kalangala, en Bugala, es la base más práctica para playas, bosque y descanso. El vehículo depende del ferry y de un horario que debe reconfirmarse.", "visit": {"why": "Aporta dos noches tranquilas junto al lago y rompe la intensidad de parques y carreteras.", "see": "Orilla de Bugala, pueblos, bosque y puestas de sol; otras islas requieren transporte aparte.", "access": "El pin marca Lutoboka/Kalangala ferry terminal, punto real de llegada. Confirmar ferry, plaza de vehículo y alojamiento.", "when": "Con dos noches y regreso flexible; evitar travesías ajustadas a una frontera o vuelo.", "skip": "No embarcar sin horario vigente, capacidad confirmada y alojamiento que acepte expresamente al perro."}},
        7: {"desc": "Rancho de conservación donde se realiza rastreo a pie de rinoceronte blanco con guía. El pin se fija en la entrada operativa de Ziwa Rhino and Wildlife Ranch, no en el centro del santuario.", "visit": {"why": "Es la oportunidad más directa de observar rinocerontes a pie en Uganda dentro de un programa de conservación.", "see": "Rinocerontes blancos, sabana y otra fauna del rancho; la distancia de observación la decide el guía.", "access": "El pin coincide con Ziwa Rhino and Wildlife Ranch en Google Maps. Reservar actividad y seguir siempre al ranger.", "when": "Primera hora o final de la tarde, con menor calor y actividad previamente confirmada.", "skip": "No entrar con el perro, no separarse del grupo y no prometer proximidad ni número de animales."}},
        8: {"desc": "El Nilo Victoria se comprime entre roca antes de caer en Murchison Falls, dentro del mayor parque nacional ugandés. La ficha se ancla en el mirador superior exacto; crucero y safari son actividades separadas.", "visit": {"why": "Combina una cascada de enorme fuerza, río y safari en una de las grandes etapas del país.", "see": "Top of the Falls, paisaje del Nilo y, con reserva, crucero al pie o circuito de fauna.", "access": "El pin coincide con Murchison Falls en Google Maps. Pagar tasas y confirmar puentes, ferry, puertas y pistas con UWA.", "when": "Dos o tres noches; mirador con luz y crucero reservado según caudal y operación.", "skip": "No acercarse a bordes fuera de sendero ni improvisar una travesía del parque con poco combustible."}},
        9: {"desc": "Sabana remota entre montañas en el extremo nordeste, con Apoka como base operativa. La distancia y el aislamiento son parte de su atractivo y también su principal coste logístico.", "visit": {"why": "Es el safari más remoto de Uganda y ofrece paisajes abiertos muy distintos al circuito occidental.", "see": "Valle de Narus, montañas, fauna de sabana y cultura karimojong solo mediante actividades responsables.", "access": "El pin coincide con Apoka en Google Maps. Llegar con combustible, reserva, repuestos y estado de carretera comprobados.", "when": "Mínimo dos noches y preferencia por estación seca; calcular una jornada completa de aproximación.", "skip": "Descartarlo si seguridad, combustible, alojamiento o pistas no están confirmados antes de salir."}},
        10: {"desc": "Fort Patiko conserva murallas y afloramientos de la antigua base vinculada primero al tráfico de personas esclavizadas y después a Samuel Baker. Sustituye al centro genérico de Gulu por una visita histórica concreta.", "visit": {"why": "Explica de forma material la violencia del comercio esclavista y la ocupación colonial del norte.", "see": "Muros, patios, marcas en la roca y paisaje de Patiko con interpretación local.", "access": "El pin coincide con Fort Patiko en Google Maps, a unos 30 km de Gulu; llegar de día y contratar guía local.", "when": "Mañana o media tarde con tiempo seco y regreso a Gulu antes de anochecer.", "skip": "No recorrer ruinas sin guía ni convertir relatos locales no documentados en hechos cerrados."}},
        11: {"desc": "Lake Nyabikere es uno de los lagos de cráter más accesibles del campo volcánico al sur de Fort Portal. Representa un paisaje concreto sin fingir que un solo pin cubre decenas de lagos.", "visit": {"why": "Añade un paseo lacustre y agrícola fácil entre Kibale, Fort Portal y Queen Elizabeth.", "see": "Lago Nyabikere, laderas cultivadas y otros cráteres solo si se acuerda una ruta más larga.", "access": "El pin coincide con Lake Nyabikere en Google Maps. Preguntar por acceso, guía y estacionamiento en propiedad local.", "when": "Mañana despejada y suelo seco; combinar con Kibale sin comprimir el rastreo de chimpancés.", "skip": "No entrar en fincas ni acercarse a orillas empinadas sin permiso local."}},
        12: {"desc": "Bosque húmedo del Rift Albertino famoso por el rastreo guiado de chimpancés y otros primates. El pin conduce al Kanyanchu Visitor Center, salida real de las actividades principales.", "visit": {"why": "Es una de las experiencias de primates más sólidas de la ruta y contrasta con la sabana.", "see": "Bosque maduro, chimpancés si se localizan, aves y primates; Bigodi es una actividad comunitaria separada.", "access": "El pin coincide con Kanyanchu Visitor Center en Google Maps. Permiso, hora y briefing son obligatorios.", "when": "Reservar con antelación; llevar botas y protección de lluvia incluso en meses relativamente secos.", "skip": "No llevar al perro, no abandonar al grupo y no presentar el avistamiento como garantizado."}},
        13: {"desc": "Cordillera ecuatorial de glaciares menguantes, lagos y vegetación afroalpina, Patrimonio Mundial. La ficha se ancla en Rwenzori Mountaineering Services de Nyakalengija, no en la cumbre ni en el centro del parque.", "visit": {"why": "Es uno de los paisajes de alta montaña más singulares de África y admite desde paseos a expediciones.", "see": "Bosque, valles de brezos y lobelias; Margherita Peak requiere una expedición técnica de varios días.", "access": "El pin coincide con la base de Nyakalengija en Google Maps. Acordar ruta, guía, porteadores y equipo antes.", "when": "Con ventana meteorológica y días de margen; incluso una ruta corta puede ser húmeda y fangosa.", "skip": "No confundir una visita al acceso con la ascensión ni salir sin guía, registro y equipo adecuado."}},
        14: {"desc": "Salinas artesanales en el lago de cráter Katwe, donde la extracción organiza el paisaje en balsas y canales. Es una visita cultural y laboral que requiere respeto, no un baño ni un mirador libre.", "visit": {"why": "Muestra una economía salinera histórica y un paisaje volcánico muy distinto al safari cercano.", "see": "Balsas de evaporación, trabajos de extracción y borde del cráter con explicación local.", "access": "El pin coincide con Lake Katwe en Google Maps. Pedir guía y permiso antes de fotografiar personas o faenas.", "when": "Con luz suave y terreno seco, evitando las horas de mayor calor.", "skip": "No caminar por balsas sin indicación, no bañarse y no usar imágenes de trabajadores sin consentimiento."}},
        15: {"desc": "El canal de Kazinga une los lagos George y Edward y concentra aves, hipopótamos y fauna que baja a beber. El pin se ha corregido al Launch Jetty de Mweya, punto real de embarque.", "visit": {"why": "El crucero ofrece una perspectiva de fauna y humedales difícil de obtener desde el coche.", "see": "Orillas, aves acuáticas, hipopótamos y posibles elefantes o búfalos sin garantía de especie.", "access": "El pin coincide con Launch Jetty en Google Maps. Reservar barco autorizado y confirmar acceso al parque.", "when": "Salida de mañana o tarde, enlazada con una noche dentro o junto a Queen Elizabeth.", "skip": "No acercarse por libre al agua ni dejar el perro en el vehículo durante el crucero."}},
        16: {"desc": "Sector meridional de Queen Elizabeth conocido por leones que a veces descansan en higueras. El pin está en Ishasha Sector Entrance Gate: el comportamiento es posible, nunca garantizado.", "visit": {"why": "Permite enlazar Queen Elizabeth con Bwindi atravesando una sabana menos concurrida.", "see": "Higueras, llanura, kob y otros mamíferos; los leones pueden estar ocultos o en el suelo.", "access": "El pin coincide con la entrada de Ishasha en Google Maps. Confirmar pista, guía y salida antes del cierre.", "when": "Primera o última franja de luz, con tiempo suficiente para continuar o dormir en zona autorizada.", "skip": "No salirse de pista, no conducir de noche y no planificar la etapa en torno a un avistamiento incierto."}},
        17: {"desc": "Bosque antiguo del Rift Albertino y Patrimonio Mundial, célebre por el rastreo de gorila de montaña. El pin conduce al Buhoma Visitor Centre, uno de varios sectores que no son intercambiables.", "visit": {"why": "Es una experiencia de conservación excepcional y Buhoma combina bosque, comunidad y rutas guiadas.", "see": "Gorilas solo con permiso y grupo asignado; también senderos forestales y aves con guía.", "access": "El pin coincide con Buhoma Visitor Centre en Google Maps. El permiso debe corresponder a Buhoma y la llegada exige margen.", "when": "Dormir cerca la víspera y presentarse al briefing temprano con ropa de lluvia y botas.", "skip": "No llevar al perro, no cambiar de sector a última hora y no acercarse a gorilas fuera del protocolo."}},
        18: {"desc": "Pequeño parque volcánico en la frontera con Ruanda y Congo, con gorilas, monos dorados y ascensiones a los Virunga. El pin marca el Ntebeko Visitor Centre, acceso operativo.", "visit": {"why": "Concentra bosque de bambú y volcanes en una alternativa compacta a Bwindi.", "see": "Rastreo de gorila o mono dorado, sendero Batwa y ascensiones; cada actividad necesita permiso propio.", "access": "El pin coincide con Mgahinga/Ntebeko Visitor Centre en Google Maps. Confirmar actividad y estado fronterizo con UWA.", "when": "Llegar la víspera a Kisoro o Ntebeko y reservar antes; niebla y lluvia son frecuentes.", "skip": "No combinar actividades incompatibles en un día ni entrar con el perro o sin permiso."}},
        19: {"desc": "Lago de laderas cultivadas e islas cerca de Kabale, adecuado para descansar y navegar con operador local. El pin lleva a Bunyonyi Overland Resort, base concreta con acceso por carretera en Rutinda.", "visit": {"why": "Es una pausa paisajística muy cómoda entre los parques de gorilas y la frontera de Ruanda.", "see": "Bahías, islas, terrazas y pueblos desde la orilla o en canoa con chaleco.", "access": "El pin coincide con Bunyonyi Overland Resort en Google Maps. Confirmar pista final, camping y aceptación del perro.", "when": "Una o dos noches, con salida en barca solo si el tiempo y el operador son seguros.", "skip": "No nadar ni embarcar sin evaluación local del agua, del viento y del equipo de seguridad."}},
        20: {"desc": "Parque de sabana, colinas y humedales cercano al eje Kampala–Mbarara, conocido por cebras y safaris a pie autorizados. El pin conduce a Nshara Gate, entrada real.", "visit": {"why": "Es el parque de fauna más fácil de encajar al final del circuito occidental y permite actividades a pie.", "see": "Cebras, impalas, elands, aves y lago; ningún avistamiento está garantizado.", "access": "El pin coincide con Nshara Gate en Google Maps. Pagar tasas y reservar guía para caminar.", "when": "Una noche o jornada completa; las primeras y últimas horas son mejores para fauna.", "skip": "No caminar sin ranger, no entrar con mascota y no subestimar tiempos de pista dentro del parque."}},
    },
}

CONTENT["ruanda"] = {
    1: {"desc": "Túneles de lava visitables en las afueras de Musanze, formados por antiguas coladas de los Virunga. Es una actividad guiada con casco y luz, y una buena introducción geológica antes de los volcanes.", "visit": {"why": "Añade una experiencia subterránea concreta a la base logística de Musanze.", "see": "Galerías de lava, claraboyas naturales y paredes modeladas por las coladas; la fauna no debe molestarse.", "access": "El pin marca la entrada real de Musanze Caves contrastada con cartografía abierta; Google Maps no devuelve un objeto nominal fiable en ese punto. Reservar con operador autorizado.", "when": "Con plaza confirmada y calzado adherente; la lluvia puede volver húmedo el acceso.", "skip": "No entrar por libre, sin casco o si el operador no confirma que la visita está abierta."}},
    2: {"desc": "Bosque montano sobre los volcanes Virunga, principal base ruandesa para rastreos reglados de gorila de montaña y mono dorado. Cada actividad requiere reserva y permiso propios.", "visit": {"why": "Es uno de los grandes paisajes de conservación de primates del viaje.", "see": "Bambú, bosque de montaña, volcanes y primates si el grupo asignado los localiza; nada se garantiza.", "access": "El pin coincide con el objeto Volcanoes National Park de Google Maps. La oficina y hora de presentación exactas deben constar en la reserva.", "when": "Dormir en Musanze o Kinigi la víspera y llegar con ropa de lluvia, polainas y botas.", "skip": "No entrar sin permiso, no llevar al perro y no confundir el pin del parque con el punto de briefing."}},
    3: {"desc": "Ascensión guiada al volcán Bisoke y a su lago de cráter, por bosque, bambú y terreno frecuentemente embarrado. La altitud y el desnivel la convierten en una jornada exigente.", "visit": {"why": "Ofrece una cumbre volcánica muy visual sin depender de un avistamiento de fauna.", "see": "Lago del cráter, bosque de los Virunga y, si se abre la niebla, vistas transfronterizas.", "access": "El pin coincide con Mount Bisoke en Google Maps; el inicio operativo y el ranger se asignan al registrarse en el parque.", "when": "Salir temprano con tiempo estable, agua, comida y protección de lluvia.", "skip": "Descartarlo con tormenta, mala forma física, equipo insuficiente o sin ranger autorizado."}},
    4: {"desc": "Cementerio de montaña donde descansan Dian Fossey y varios gorilas, junto al emplazamiento histórico de Karisoke. Se llega en una caminata guiada dentro del parque.", "visit": {"why": "Permite entender el coste humano y animal de la historia de conservación de los gorilas.", "see": "Tumbas, restos del antiguo campamento y bosque entre Karisimbi y Bisoke, con interpretación del ranger.", "access": "El pin coincide con el objeto Dian Fossey Cemetery en Google Maps. Permiso, guía y punto de inicio se confirman con el parque.", "when": "Por la mañana y con equipo para barro y lluvia; reservar una jornada flexible.", "skip": "No acceder por libre, no llevar mascota y no tratar el lugar como una simple localización fotográfica."}},
    5: {"desc": "Lago Ruhondo, uno de los lagos gemelos al este de Musanze, ofrece agua, colinas cultivadas y los Virunga al fondo. La ficha se ancla en un punto real de embarque, no en el centro del lago.", "visit": {"why": "Es una pausa paisajística accesible después de las actividades de montaña.", "see": "Orilla de Ruhondo, islas y terrazas agrícolas; Burera requiere otro acceso.", "access": "El pin coincide con Lake Ruhondo Boat Point en Google Maps. Confirmar barca, chaleco, estacionamiento y política del perro.", "when": "Mañana despejada o final de la tarde, sin viento fuerte.", "skip": "No embarcar sin chaleco ni asumir que cualquier pista de la orilla es pública."}},
    6: {"desc": "Rubavu es la principal escala del lago Kivu al norte, con paseo costero, playa pública y servicios junto a la frontera congoleña. El pin lleva a la playa real, no a una vista de Karongi.", "visit": {"why": "Combina descanso junto al agua, aprovisionamiento y salida del Congo Nile Trail.", "see": "Bahía de Rubavu, paseo y horizonte de Goma; la situación fronteriza se evalúa aparte.", "access": "El pin coincide con Rubavu Public Beach en Google Maps. Usar estacionamiento vigilado y comprobar avisos locales.", "when": "Una o dos noches, preferiblemente sin desplazamientos nocturnos cerca de la frontera.", "skip": "No cruzar a RD Congo ni nadar o navegar sin comprobación local de seguridad y condiciones del agua."}},
    7: {"desc": "Ruta de senderismo y bicicleta que recorre las colinas de la orilla oriental del Kivu entre Rubavu y Rusizi. El pin representa el tramo de Gisovu–Karongi y no toda la travesía.", "visit": {"why": "Es la mejor forma de leer el paisaje rural del Kivu a ritmo lento.", "see": "Crestas, plantaciones, aldeas y bahías; el firme y los servicios cambian por etapas.", "access": "El pin coincide con Congo-Nile Trail Gisovu–Karongi en Google Maps. Elegir previamente un tramo y confirmar guía, alojamiento y traslado.", "when": "En días relativamente secos y con horas de luz suficientes para terminar la etapa.", "skip": "No asumir que todo el recorrido es transitable en coche ni improvisar atajos por propiedades privadas."}},
    8: {"desc": "Karongi, antigua Kibuye, ocupa una sucesión de penínsulas y bahías del lago Kivu. Es una base cómoda para navegar, descansar y dividir el corredor occidental.", "visit": {"why": "Ofrece el paisaje lacustre más recortado de Ruanda y una escala manejable.", "see": "Bahías, islas y colinas desde la orilla o en barca autorizada; cada desembarco se acuerda aparte.", "access": "El pin coincide con el objeto Kibuye de Google Maps junto al frente de agua. Confirmar embarcadero y aparcamiento con el alojamiento.", "when": "Una o dos noches, con navegación de mañana si el tiempo lo permite.", "skip": "No subir a una barca sin chalecos ni dejar al perro solo en el coche durante la excursión."}},
    9: {"desc": "Rusizi cierra el eje del lago Kivu junto al puente hacia Bukavu y sirve de base para el acceso meridional a Nyungwe. La frontera congoleña no forma parte de la ruta prevista.", "visit": {"why": "Es una escala logística útil entre el Kivu, Nyungwe y el sur de Ruanda.", "see": "Salida del río Rusizi, puente fronterizo y frente urbano; no es una excursión a Bukavu.", "access": "El pin coincide con el puente Ruzizi I en Google Maps. Mantenerse en el lado ruandés y comprobar el aviso vigente del MAEC.", "when": "De día, para repostar y continuar con alojamiento confirmado.", "skip": "No acercarse a pasos secundarios ni cruzar la frontera por curiosidad o con documentación incompleta."}},
    10: {"desc": "El sendero de Igishigishigi alcanza una pasarela suspendida sobre el bosque montano de Nyungwe. El pin se ha corregido al Uwinka Visitor Center, salida operativa de esta actividad.", "visit": {"why": "Permite contemplar el dosel desde arriba en una ruta relativamente corta y bien definida.", "see": "Bosque montano, helechos, aves y pasarela; primates y vistas despejadas no están garantizados.", "access": "El pin coincide con Uwinka Visitor Center en Google Maps. Reservar guía y actividad; el parque asigna horario y sendero.", "when": "Con lluvia moderada asumible y calzado de agarre; salir temprano.", "skip": "No entrar con el perro, sin reserva o con tormenta y cierre comunicado por el parque."}},
    11: {"desc": "Museo Etnográfico de Huye con colecciones sobre tecnología, vivienda, música y formas de vida de Ruanda. Es la parada cultural más completa del corredor sur.", "visit": {"why": "Aporta contexto social y material que el itinerario de parques no ofrece.", "see": "Objetos, arquitectura, artesanía y exposición interpretativa; comprobar qué salas están abiertas.", "access": "El pin coincide con Ethnographic Museum en Google Maps. Consultar horario y normas fotográficas en la entrada.", "when": "Una mañana o tarde laborable, reservando al menos dos horas.", "skip": "No ir sin verificar apertura ni contar con que el perro pueda entrar al edificio."}},
    12: {"desc": "Reconstrucción del recinto real en Nyanza, con vivienda tradicional y exposición sobre la monarquía ruandesa. La visita debe separar patrimonio documentado de escenificación contemporánea.", "visit": {"why": "Explica la organización política y ceremonial previa al periodo colonial.", "see": "Palacio tradicional reconstruido, residencia posterior y ganado inyambo cuando la gestión lo programa.", "access": "El pin coincide con King’s Palace Museum en Google Maps. Confirmar horario y visita guiada.", "when": "Combinarlo con Huye sin comprimir ambos museos en una visita superficial.", "skip": "No entrar con mascota ni presentar la reconstrucción como un edificio original intacto."}},
    13: {"desc": "Antigua residencia de Richard Kandt convertida en museo sobre historia natural y la formación de Kigali. Funciona además como ancla concreta para la base logística de la capital.", "visit": {"why": "Une el origen urbano colonial de Kigali con una visita breve y localizada.", "see": "Casa, exposiciones históricas y sección de fauna; el contenido puede variar por salas.", "access": "El pin coincide con Kandt House Museum en Google Maps. Aparcar dentro o usar transporte local en horas punta.", "when": "Día laborable para combinar museo, talleres, bancos y trámites.", "skip": "No ir sin confirmar apertura ni dedicar tiempo urbano innecesario de noche."}},
    14: {"desc": "Lugar de memoria y centro de documentación donde descansan víctimas del genocidio contra los tutsi de 1994. Exige tiempo, silencio y una visita respetuosa.", "visit": {"why": "Es esencial para comprender la historia contemporánea de Ruanda y sus consecuencias humanas.", "see": "Jardines conmemorativos, exposición histórica y espacios de duelo; algunos contenidos son emocionalmente duros.", "access": "El pin coincide con Kigali Genocide Memorial en Google Maps. Revisar las indicaciones oficiales y la reserva antes de acudir.", "when": "Con al menos dos horas y sin encadenarlo a una agenda turística acelerada.", "skip": "No entrar con mascota, no fotografiar donde esté restringido y no forzar la visita a quien no esté preparado."}},
    15: {"desc": "Iglesia y recinto conmemorativo de Nyamata, parte del conjunto de memoriales del genocidio inscrito por UNESCO. Conserva el lugar como prueba y espacio de duelo.", "visit": {"why": "Aporta una escala local y material a una historia que no debe reducirse a cifras abstractas.", "see": "Iglesia, objetos conservados y espacios funerarios según el recorrido autorizado.", "access": "El pin coincide con Nyamata Genocide Memorial en Google Maps. Seguir al personal y respetar todas las restricciones.", "when": "Con tiempo para la explicación y recuperación emocional posterior.", "skip": "No acudir para obtener fotografías impactantes, no llevar mascota y no usar un tono frívolo."}},
    16: {"desc": "Lago alargado al este de Kigali, rodeado de colinas agrícolas y pequeños alojamientos. El pin se fija en Muhazi Marina Beach como acceso real y no en el centro del agua.", "visit": {"why": "Es una escapada lacustre sencilla antes de Akagera o después de la capital.", "see": "Orilla, aves, barcas y colinas; el nivel de servicios depende del establecimiento.", "access": "El pin coincide con Muhazi Marina Beach en Google Maps. Confirmar entrada, estacionamiento, comida y admisión del perro.", "when": "Una tarde y una noche, evitando navegar con viento o tormenta.", "skip": "No asumir acceso público a cualquier orilla ni embarcar sin chaleco y operador responsable."}},
    17: {"desc": "Parque de sabana, lagos y humedales en el este de Ruanda, gestionado con un sistema de puertas y reservas. La autoconducción es posible solo dentro de las rutas y horarios autorizados.", "visit": {"why": "Añade un safari de sabana compacto a un país dominado por montañas y bosques.", "see": "Lagos, llanuras, aves y grandes mamíferos; ninguna especie concreta está garantizada.", "access": "El pin coincide con Akagera Reception en Google Maps. Registrar el vehículo y confirmar entrada, salida, guía y estado de pistas.", "when": "Dos noches y salidas de primera hora; revisar la operación vigente en la web oficial.", "skip": "No entrar con el perro, no salir de pista ni intentar cruzar el parque sin combustible y hora de salida confirmados."}},
    18: {"desc": "Bosque montano restaurado dentro de Gishwati–Mukura, con senderos guiados y primates en un paisaje que también muestra los efectos históricos de la deforestación. La visita se prepara con la gestión del parque.", "visit": {"why": "Permite entender restauración ecológica y conectividad forestal, no solo buscar fauna.", "see": "Bosque, aves, primates si aparecen y bordes en regeneración.", "access": "El pin coincide con el objeto Gishwati Forest de Google Maps. Confirmar acceso, guía y alojamiento antes de desviarse.", "when": "Con tiempo seco relativo y una jornada reservada; el barro ralentiza mucho los senderos.", "skip": "No entrar con mascota, sin autorización o esperando infraestructura equivalente a los parques más visitados."}},
}

CONTENT["malaui"] = {
    1: {"desc": "Museo de Karonga dedicado a los hallazgos paleontológicos y a la historia cultural del extremo norte de Malaui. Es una primera parada concreta tras la frontera de Songwe.", "visit": {"why": "Da contexto al paisaje y a la larga ocupación humana de la región antes de bajar por el lago.", "see": "Fósiles, reconstrucciones y exposiciones de historia local; comprobar qué salas están abiertas.", "access": "El pin coincide con Karonga Museum en Google Maps. Confirmar horario en la entrada y aparcar dentro del recinto.", "when": "En horario diurno, combinado con combustible, efectivo y compras en Karonga.", "skip": "No ir sin verificar apertura ni contar con acceso del perro al interior."}},
    2: {"desc": "Casa de piedra vinculada a la misión de Livingstonia, hoy museo sobre la comunidad, el asentamiento y su historia. El edificio es una visita distinta de la iglesia cercana.", "visit": {"why": "Permite leer de forma tangible la historia misionera y educativa del altiplano.", "see": "Stone House, objetos y documentación local; la iglesia y los miradores se visitan aparte.", "access": "El pin coincide con Stone House Museum en Google Maps. Confirmar apertura, guía y estacionamiento local.", "when": "Mañana fresca y con pista de subida comprobada.", "skip": "No subir con lluvia fuerte o sin saber el estado de la carretera del escarpe."}},
    3: {"desc": "Manchewe Falls cae desde el escarpe junto a Livingstonia y se alcanza mediante un sendero local. El terreno húmedo y los bordes exigen guía y prudencia.", "visit": {"why": "Combina una cascada alta, bosque y vistas del lago en una excursión corta.", "see": "Salto, garganta y miradores naturales; el caudal cambia con la estación.", "access": "El pin coincide con Manchewe Falls en Google Maps. Contratar guía local y acordar aparcamiento antes de caminar.", "when": "Por la mañana y con suelo razonablemente seco.", "skip": "No acercarse al borde con niebla o lluvia ni seguir atajos no autorizados."}},
    4: {"desc": "Meseta de pastizales y manchas de bosque montano, con Chelinda como base de acceso a Nyika. La lejanía, el frío nocturno y las pistas requieren planificación real.", "visit": {"why": "Es uno de los paisajes de altura más singulares del África austral y muy diferente del lago.", "see": "Colinas onduladas, pastizales, orquídeas en temporada y fauna dispersa sin garantía.", "access": "El pin coincide con Chelinda Camp en Google Maps. Confirmar reserva, puerta, combustible y estado de la pista.", "when": "Dos o tres noches y ropa de abrigo; la estación seca facilita el acceso.", "skip": "No entrar con perro, sin autonomía o cuando la gestión no confirma que la pista es practicable."}},
    5: {"desc": "Mzuzu es la base de servicios del norte para combustible, talleres, compras y atención sanitaria. El pin se ancla en Mzuzu Central Hospital para evitar un punto urbano genérico.", "visit": {"why": "Permite resolver logística antes de Nyika, Nkhata Bay o el corredor central.", "see": "Mercados y ciudad solo como complemento; el valor principal es operativo.", "access": "El pin coincide con Mzuzu Central Hospital en Google Maps. Separar el estacionamiento de gestiones del acceso de urgencias.", "when": "Día laborable y con lista de compras y reparaciones agrupada.", "skip": "No prolongar la estancia urbana ni circular de noche sin necesidad."}},
    6: {"desc": "Bahía portuaria rodeada de laderas verdes, principal base del lago en el norte. El pin marca el embarcadero de Nkhata Bay, referencia real para entender transportes y costa.", "visit": {"why": "Ofrece vida portuaria, descanso y conexión con Likoma sin inventar una playa genérica.", "see": "Embarcadero, bahía y actividad local; horarios de barcos y servicios cambian.", "access": "El pin coincide con Nkhata Bay Jetty en Google Maps. Confirmar billetes, carga, estacionamiento y alojamiento por separado.", "when": "Una o dos noches con margen respecto al transporte lacustre.", "skip": "No dejar el vehículo o al perro sin custodia ni confiar en horarios antiguos del ferry."}},
    7: {"desc": "Antigua misión de Bandawe junto a Chintheche, con iglesia, cementerio y memoria del traslado de Livingstonia. Es una visita histórica breve en la costa norte.", "visit": {"why": "Explica la primera implantación misionera junto al lago y las razones de su traslado.", "see": "Iglesia, tumbas y entorno costero con interpretación local.", "access": "El pin coincide con Old Bandawe Mission en Google Maps. Pedir permiso y guía antes de recorrer el recinto.", "when": "De día, combinado con la etapa Nkhata Bay–Nkhotakota.", "skip": "No entrar durante ceremonias ni fotografiar personas o tumbas sin consentimiento."}},
    8: {"desc": "Catedral anglicana de gran escala construida en Likoma, isla malauí rodeada por aguas mozambiqueñas. Llegar exige coordinar barco o vuelo y alojamiento.", "visit": {"why": "Es el edificio religioso más singular del lago y justifica la compleja desviación a Likoma.", "see": "Nave, vidrieras, piedra y vida insular; respetar los oficios.", "access": "El pin coincide con St Peter’s Cathedral en Google Maps. Confirmar transporte, equipaje, alojamiento y custodia del vehículo continental.", "when": "Con al menos dos noches y margen por cambios de navegación o vuelo.", "skip": "No ir con calendario ajustado ni asumir que el perro o el coche pueden viajar en cualquier servicio."}},
    9: {"desc": "Gran reserva de miombo restaurada por African Parks, con ríos, senderos y fauna reintroducida. La ficha se ancla en la puerta principal, no en el centro del área protegida.", "visit": {"why": "Permite conocer una recuperación ecológica importante con menos tráfico que los parques del sur.", "see": "Bosque de miombo, ríos, aves y mamíferos si aparecen; la densidad varía por sector.", "access": "El pin coincide con Nkhotakota Main Gate en Google Maps. Confirmar actividades, alojamiento y estado de pista con African Parks.", "when": "Dos noches y salidas guiadas de primera o última hora.", "skip": "No entrar con mascota, sin reserva, combustible o instrucciones claras de salida."}},
    10: {"desc": "Monumento bajo un gran árbol asociado al encuentro de David Livingstone con Jumbe en Nkhotakota. Es una parada histórica breve cuyo relato debe leerse de forma crítica.", "visit": {"why": "Introduce las redes comerciales, el poder local y la presencia europea del siglo XIX.", "see": "Árbol y placa conmemorativa; la interpretación disponible puede ser limitada.", "access": "El pin coincide con Livingstone Tree en Google Maps, no con el objeto similar situado unos cientos de metros al norte.", "when": "De día, dentro de una parada logística en Nkhotakota.", "skip": "No convertir una tradición conmemorativa en prueba exacta sin explicar sus límites."}},
    11: {"desc": "Bahía de arena junto al lago Malaui y base de descanso cerca de Salima. El pin coincide con Senga Bay y no con una playa genérica de otra parte del lago.", "visit": {"why": "Ofrece una pausa sencilla junto al agua en el corredor central.", "see": "Playa, barcas de pesca y amanecer; las condiciones del agua cambian.", "access": "El pin coincide con Senga Bay en Google Maps. Elegir alojamiento con estacionamiento y admisión del perro confirmados.", "when": "Una noche, evitando baño o navegación con oleaje y tormenta.", "skip": "No beber agua del lago ni asumir que todas las playas son públicas o seguras para nadar."}},
    12: {"desc": "Parque nacional de miombo y llanuras en torno al lago Lifupa, alejado de los grandes circuitos. La infraestructura y la presencia de fauna deben confirmarse antes de desviarse.", "visit": {"why": "Aporta un safari tranquilo y paisaje de bosque abierto en el centro del país.", "see": "Lago Lifupa, miombo, aves y mamíferos dispersos; ningún avistamiento está garantizado.", "access": "El pin coincide con Kasungu National Park en Google Maps, cerca de Lifupa. Confirmar puerta, alojamiento, guía y pistas.", "when": "Con dos noches y durante una fase relativamente seca.", "skip": "No entrar con perro, sin comunicación previa o si el estado de acceso no está claro."}},
    13: {"desc": "Bosque urbano protegido con senderos, pasarela, observatorio de aves y educación ambiental dentro de Lilongüe. El santuario de animales rescatados no está abierto a visitas: no es un zoológico.", "visit": {"why": "Permite caminar por el último gran espacio verde del centro y apoyar el trabajo de conservación.", "see": "Senderos forestales, río, aves y monos salvajes; los recintos de rehabilitación no forman parte de la visita.", "access": "El pin coincide con Lilongwe Wildlife Centre en Google Maps. La guía oficial prohíbe perros y detalla las normas del recinto.", "when": "En horario diurno, combinado con talleres, compras y gestiones en la capital.", "skip": "No entrar con mascota ni esperar contacto o una visita guiada a los animales rescatados."}},
    14: {"desc": "Abrigos rocosos de Chentcherere dentro del área UNESCO de Chongoni, con pinturas de tradiciones cazadoras y agrícolas. La lectura correcta requiere guía y respeto absoluto de los paneles.", "visit": {"why": "Es el conjunto de arte rupestre más importante de Malaui y conserva tradiciones de larga duración.", "see": "Paneles pintados, abrigos y paisaje granítico; la visibilidad depende de luz y conservación.", "access": "El pin coincide con Chentcherere Rock Art en Google Maps. Acordar guía local y estado de la pista.", "when": "Con luz oblicua, tiempo seco y varias horas sin prisa.", "skip": "No tocar, mojar, calcar ni usar flash sobre las pinturas; no entrar con mascota."}},
    15: {"desc": "Kungoni Centre, en Mua Mission, reúne museo, tallas y conocimiento sobre culturas de Malaui. Es una visita cultural viva y no solo una tienda de artesanía.", "visit": {"why": "Ofrece contexto profundo sobre máscaras, rituales, lengua y cambios sociales.", "see": "Chamare Museum, talleres de talla y edificios de la misión según disponibilidad.", "access": "El pin coincide con Kungoni Centre en Google Maps. Reservar museo o guía y confirmar la pista final.", "when": "Con media jornada y preferiblemente cita previa.", "skip": "No fotografiar ceremonias, objetos sensibles o personas sin autorización expresa."}},
    16: {"desc": "Cabo Maclear es la base continental del Lake Malawi National Park, Patrimonio Mundial por su diversidad de peces y paisaje lacustre. El pin corresponde al objeto real del parque junto al pueblo.", "visit": {"why": "Combina vida local, islas, senderos y ecosistema acuático en una parada central del viaje.", "see": "Bahía, islas, aves y peces con operador responsable; la visibilidad y la fauna varían.", "access": "El pin coincide con Lake Malawi National Park en Google Maps. Confirmar entrada, barca, chalecos y estacionamiento.", "when": "Dos o tres noches con mañanas tranquilas y margen por viento.", "skip": "No entrar en el parque con perro ni nadar o bucear sin evaluar riesgos sanitarios y meteorológicos locales."}},
    17: {"desc": "Liwonde protege el río Shire, llanuras inundables y bosque, con safaris terrestres y navegación autorizada. El pin se ha corregido a la puerta principal de acceso.", "visit": {"why": "Es el parque de fauna más fácil de integrar en el sur de Malaui y el río cambia la experiencia.", "see": "Shire, aves, hipopótamos, elefantes y otros mamíferos si aparecen.", "access": "El pin coincide con Liwonde National Park Main Entrance Gate en Google Maps. Reservar actividad y confirmar pistas con African Parks.", "when": "Dos noches, con salida de madrugada y paseo fluvial si opera con seguridad.", "skip": "No entrar con mascota, acercarse por libre al río ni dejarla en el coche durante un safari."}},
    18: {"desc": "La meseta de Zomba se eleva sobre la antigua capital entre bosques, miradores y carreteras de montaña. El pin marca Queen’s View, un mirador real y accesible.", "visit": {"why": "Ofrece un cambio de temperatura y amplias vistas sin exigir una expedición.", "see": "Escarpe, llanura y bosque desde Queen’s View; otros senderos requieren tiempo adicional.", "access": "El pin coincide con Queen’s View en Google Maps. Comprobar carretera, niebla y estacionamiento antes de subir.", "when": "Primera hora o final de la tarde con cielo despejado.", "skip": "No conducir con niebla cerrada ni acercarse a bordes o senderos mojados."}},
    19: {"desc": "Mandala House, uno de los edificios coloniales conservados más antiguos de Malaui, alberga espacios culturales en Blantyre. Sirve como visita concreta y ancla de la principal base comercial del sur.", "visit": {"why": "Permite combinar historia urbana con talleres, repuestos, bancos y gestiones.", "see": "Casa, jardines y exposiciones o actividades vigentes; confirmar el uso actual antes de acudir.", "access": "El pin coincide con Mandala House/Abrar Vanara en Google Maps. Usar estacionamiento vigilado y evitar horas punta.", "when": "Día laborable, agrupando todas las necesidades logísticas.", "skip": "No ir sin comprobar acceso actual ni moverse innecesariamente de noche."}},
    20: {"desc": "Macizo granítico de gran relieve y paisaje cultural, con Likhubula como una de las puertas habituales para senderos y refugios. Las rutas cambian mucho en dificultad y duración.", "visit": {"why": "Es la gran etapa de montaña del sur y combina geología, bosque y cultura local.", "see": "Paredes de granito, valles, cursos de agua y cumbres solo en itinerarios acordes al tiempo disponible.", "access": "El pin coincide con Likhubula Forest Gate en Google Maps. Registrar ruta y contratar guía local competente.", "when": "Con tiempo seco, salida temprana y plan de retorno o refugio definido.", "skip": "No entrar con mascota, sin guía o con incendio, tormenta, crecida o niebla fuerte."}},
    21: {"desc": "Finca histórica de té y café en las colinas de Thyolo, con visitas organizadas sujetas a reserva. La fotografía de portada muestra plantaciones malauíes, no un paisaje de otro país.", "visit": {"why": "Permite entender una actividad agrícola central del sur en una parada agradable entre Blantyre y Mulanje.", "see": "Campos de té, proceso y degustación según el programa contratado.", "access": "El pin coincide con Satemwa Tea & Coffee Estate en Google Maps. Reservar antes y seguir las zonas autorizadas.", "when": "Mañana de día laborable, comprobando cosecha y disponibilidad de visita.", "skip": "No entrar en áreas de trabajo, volar dron ni llevar al perro sin permiso escrito de la finca."}},
    22: {"desc": "Reserva restaurada en el bajo Shire, referente de recuperación de fauna y financiación mediante turismo. La visita se organiza por puertas, alojamientos y actividades autorizadas.", "visit": {"why": "Cierra el circuito malauí con un proyecto de conservación consolidado y safari de paisaje seco.", "see": "Bosque, río y grandes mamíferos si aparecen; los avistamientos nunca son seguros.", "access": "El pin coincide con el objeto Majete Wildlife Reserve de Google Maps. Confirmar puerta de entrada, pista y reserva con African Parks.", "when": "Dos noches y salidas de primera o última hora.", "skip": "No entrar con mascota, sin combustible o sin saber qué puerta usar y a qué hora cierra."}},
}


DOGS: dict[str, dict[int, str]] = {
    "uganda": {
        1: "confirmar con guía y alojamiento", 2: "prohibido en el parque", 3: "confirmar con recinto y operador",
        4: "prohibido en el museo", 5: "confirmar con el jardín", 6: "confirmar con alojamiento y ferry",
        7: "prohibido en la reserva", 8: "prohibido en el parque", 9: "prohibido en el parque",
        10: "confirmar con custodios locales", 11: "confirmar con guía y alojamiento",
        12: "prohibido en el parque", 13: "prohibido en el parque", 14: "confirmar con guía local",
        15: "prohibido en el parque", 16: "prohibido en el parque", 17: "prohibido en el parque",
        18: "prohibido en el parque", 19: "confirmar con alojamiento y barca", 20: "prohibido en el parque",
    },
    "ruanda": {
        1: "prohibido en la cueva", 2: "prohibido en el parque", 3: "prohibido en el parque",
        4: "prohibido en el parque", 5: "confirmar con alojamiento y barca", 6: "confirmar con alojamiento",
        7: "confirmar con guía y alojamiento", 8: "confirmar con alojamiento y barca", 9: "permitido con condiciones",
        10: "prohibido en el parque", 11: "prohibido en el museo", 12: "prohibido en el museo",
        13: "prohibido en el museo", 14: "prohibido en el memorial", 15: "prohibido en el memorial",
        16: "confirmar con alojamiento y barca", 17: "prohibido en el parque", 18: "prohibido en el parque",
    },
    "malaui": {
        1: "prohibido en el museo", 2: "confirmar con museo y alojamiento", 3: "confirmar con guía local",
        4: "prohibido en el parque", 5: "confirmar con alojamiento", 6: "confirmar con alojamiento y ferry",
        7: "confirmar con custodios locales", 8: "confirmar con iglesia y transporte",
        9: "prohibido en la reserva", 10: "confirmar con custodios locales", 11: "confirmar con alojamiento",
        12: "prohibido en el parque", 13: "prohibido en el centro", 14: "prohibido en el sitio protegido",
        15: "confirmar con el centro", 16: "prohibido en el parque", 17: "prohibido en el parque",
        18: "permitido con condiciones", 19: "confirmar con recinto y alojamiento",
        20: "prohibido en la reserva", 21: "requiere autorización escrita", 22: "prohibido en la reserva",
    },
}


PHOTOS: dict[str, dict[int, list[dict[str, str]]]] = {
    "uganda": {
        1: [
            commons("Sipi falls uganda.jpg", "Mumdantie · CC BY-SA 4.0", "Salto principal de Sipi y su anfiteatro verde."),
            commons("Sipi Falls Main Drop.jpg", "Quack3142 · CC BY-SA 3.0", "Vista frontal del salto principal de Sipi."),
            commons("The stunning beauty of Sipi Falls in Uganda's Mount Elgon National Park 11.jpg", "Sandra Aceng · CC BY-SA 4.0", "Sendero y paisaje real de las cataratas de Sipi."),
        ],
        2: [
            commons("Mount Elgon-1.jpg", "Kristina Just · CC BY-SA 2.0", "Paisaje de altura de Mount Elgon."),
            commons("Sacred lake.jpg", "Ronaldcameron · CC BY-SA 4.0", "Lago de montaña dentro del macizo de Elgon."),
            commons("Monte Elgon, Uganda - Quênia, Africa.jpg", "INPE · CC BY-SA 2.0", "Vista satelital del gran macizo transfronterizo de Mount Elgon."),
        ],
        3: [
            commons("Jinja source of Nile.jpg", "Dror Feitelson · CC BY-SA 3.0", "Monumento y aguas del nacimiento del Nilo en Jinja."),
            commons("Source of the Nile - Jinja, Uganda (181090963).jpg", "Daniel Aufgang · CC BY 3.0", "Señalización del nacimiento del Nilo en Jinja."),
            commons("Source of the Nile, Jinja Uganda.jpg", "Christopher Liberty · CC BY-SA 4.0", "Perspectiva desde el agua en el nacimiento del Nilo."),
        ],
        4: [
            commons("Uganda Museum, kampala.jpg", "Sandra Aceng · CC BY-SA 4.0", "Fachada real del Uganda Museum en Kampala."),
            commons("Museum Entrance 2.JPG", "Lneruba · CC BY-SA 4.0", "Entrada del Uganda Museum."),
            commons("Uganda Society Library At Uganda Museum.jpg", "Jambujack · CC BY-SA 4.0", "Biblioteca de la Uganda Society dentro del recinto del museo."),
        ],
        5: [
            commons("Entebbe Botanical Gardens UGANDA.jpg", "Nicholas Kisaakye Nsobya · CC BY-SA 4.0", "Arboleda del Jardín Botánico de Entebbe."),
            commons("Entebbe Botanical Gardens 5.jpg", "zeroexposure · CC BY 2.0", "Vegetación tropical del jardín de Entebbe."),
            commons("Beach within Botanical Garden, Entebbe, Uganda.jpg", "Rcdwealth · CC BY 4.0", "Orilla del lago dentro del Jardín Botánico de Entebbe."),
        ],
        6: [
            commons("The Shore at Ssese Islands, on Lake Victoria.jpg", "Jiame Josh · CC BY-SA 4.0", "Orilla real de las islas Ssese en el lago Victoria."),
            commons("Beautiful Scenery of Ssese Islands In Uganda.jpg", "Jiame Josh · CC BY-SA 4.0", "Paisaje de las islas Ssese."),
            commons("Sunset at Ssese Island Uganda.jpg", "AlindaRS · CC BY-SA 4.0", "Puesta de sol en una de las islas Ssese."),
        ],
        7: [
            commons("White Rhinos at Ziwa Rhino Sanctuary in Uganda, August 2025.jpg", "Abdushariff Muhumuza · CC BY 4.0", "Rinocerontes blancos fotografiados en Ziwa en agosto de 2025."),
            commons("Rhino in ziwa sanctuary uganda.jpg", "Moongateclimber · CC BY-SA 3.0", "Rinoceronte dentro del santuario de Ziwa."),
            commons("Ziwa rhino sanctuary.jpg", "Alvinategyeka · CC BY-SA 4.0", "Sabana y rinoceronte en Ziwa Rhino Sanctuary."),
        ],
        8: [
            commons("Murchison Falls, Uganda (23475021234).jpg", "Rod Waddington · CC BY-SA 2.0", "El Nilo comprimido en la garganta de Murchison Falls."),
            commons("Top of Murchison falls.jpg", "Jingo Faizal · CC BY-SA 4.0", "Vista desde la parte superior de Murchison Falls."),
            commons("Vegetation in Murchison Falls National Park Uganda 01.jpg", "Kateregga1 · CC BY-SA 4.0", "Vegetación dentro de Murchison Falls National Park."),
        ],
        9: [
            commons("Kidepo savanna plain.jpg", "Vincent Mugaba · CC BY-SA 4.0", "Llanura de sabana de Kidepo Valley."),
            commons("Kidepo Valley National Park evening.jpg", "Rod Waddington · CC BY-SA 2.0", "Kidepo Valley National Park al final de la tarde."),
            commons("Graceful Giants of Kidepo Valley.png", "Chapelle Musa 2 · CC BY-SA 4.0", "Elefantes en Kidepo Valley; el avistamiento no se garantiza."),
        ],
        10: [
            commons("Fort Patiko walls.jpg", "Keitsist · CC BY-SA 3.0", "Muros conservados de Fort Patiko."),
            commons("Baker s Fort Patiko , Gulu.jpg", "Micheal Kaluba · CC BY-SA 4.0", "Afloramientos y restos de Baker's Fort en Patiko."),
            commons("Fort Patiko, also known as Baker's Fort, was a military fort built by Samuel Baker in Patiko, in Northern Uganda.Uganda.jpg", "Jim Joel · CC BY-SA 4.0", "Recinto histórico de Fort Patiko en el norte de Uganda."),
        ],
        11: [
            commons("Crater Lakes of Fort Portal 01.jpg", "Fiktube · CC BY-SA 4.0", "Lagos de cráter del entorno de Fort Portal."),
            commons("Crater Lake nestled in Fort Portal 01.jpg", "Fiktube · CC BY-SA 4.0", "Uno de los lagos de cráter entre laderas cultivadas."),
            commons("Crater Lake nestled in Fort Portal 02.jpg", "Fiktube · CC BY-SA 4.0", "Otra perspectiva del campo de cráteres de Fort Portal."),
        ],
        12: [
            commons("Entrance of Kibale NP (7863696254).jpg", "Bernard DUPONT · CC BY-SA 2.0", "Entrada señalizada de Kibale National Park."),
            commons("Kibale Forest in Kibale National Park in Fort Portal in 2025 02.jpg", "B722N · CC BY-SA 4.0", "Bosque real de Kibale fotografiado en 2025."),
            commons("Tree House (17937964155).jpg", "Bernard DUPONT · CC BY-SA 2.0", "Estructura de observación en el bosque de Kibale."),
        ],
        13: [
            commons("Rwenzori night Kitasamba.jpg", "Rafał Kozubek · CC BY-SA 4.0", "Campamento y montañas del Rwenzori al anochecer."),
            commons("Alexandra Peak Margherita Peak Rwenzori.jpg", "Rafał Kozubek · CC BY-SA 4.0", "Picos Alexandra y Margherita en el Rwenzori."),
            commons("Ruwenpflanzen.jpg", "Manuel Werner · CC BY-SA 2.5", "Vegetación afroalpina característica de los Rwenzori."),
        ],
        14: [
            commons("Salt mining in Lake Katwe, Uganda 16.jpg", "Sandra Aceng · CC BY-SA 4.0", "Balsas y trabajo salinero en Lake Katwe."),
            commons("Salt mining in Lake Katwe, Uganda 09.jpg", "Sandra Aceng · CC BY-SA 4.0", "Detalle de la extracción artesanal de sal en Lake Katwe."),
            commons("Salt mining in Lake Katwe, Uganda 15.jpg", "Sandra Aceng · CC BY-SA 4.0", "Paisaje productivo de las salinas de Lake Katwe."),
        ],
        15: [
            commons("Passenger boats at Kazinga Channel in Kasese district in western Uganda 03.jpg", "B722N · CC BY-SA 4.0", "Barcas de pasajeros en el canal de Kazinga."),
            commons("Passenger boats at Kazinga Channel in Kasese district in western Uganda 02.jpg", "B722N · CC BY-SA 4.0", "Embarcaciones en el canal de Kazinga, cerca de Mweya."),
            commons("Passenger boats at Kazinga Channel in Kasese district in western Uganda 06.jpg", "B722N · CC BY-SA 4.0", "Actividad real en el canal de Kazinga."),
        ],
        16: [
            commons("Tree-climbing lions (Panthera leo).jpg", "Charles J Sharp · CC BY-SA 4.0", "Leones descansando en un árbol; el comportamiento no se garantiza en Ishasha."),
            commons("Tree-climbing lions (Panthera leo) in sycamore fig (Ficus sycomorus).jpg", "Charles J Sharp · CC BY-SA 4.0", "Leones en una higuera sicómoro dentro del paisaje de Ishasha."),
            commons("Tree lion 2.jpg", "Cody Pope · CC BY-SA 3.0", "Otro ejemplo documentado de león trepador en Uganda."),
        ],
        17: [
            commons("Gorila de montaña (Gorilla beringei beringei), parque nacional de la Selva Impenetrable de Bwindi, Uganda, 2024-02-02, DD 80.jpg", "Diego Delso · CC BY-SA 4.0", "Gorila de montaña fotografiado en Bwindi en febrero de 2024."),
            commons("Mountain gorilla (Gorilla beringei beringei) female eating root.jpg", "Charles J Sharp · CC BY-SA 4.0", "Hembra de gorila de montaña en Bwindi; el encuentro depende del rastreo."),
            commons("Bwindi Impenetrable National Park desde el Broadbill Forest Camp 20190925 085152.jpg", "Josefito123 · CC BY-SA 4.0", "Bosque Impenetrable de Bwindi visto desde su entorno occidental."),
        ],
        18: [
            commons("Mgahinga Gorilla National Park.jpg", "Byekwaso Blasio · CC BY-SA 4.0", "Bosque y volcanes de Mgahinga Gorilla National Park."),
            commons("Volcanoes in Western Uganda.jpg", "Sjoerdug · CC BY-SA 4.0", "Conos volcánicos del extremo suroeste de Uganda."),
            commons("Mgahinga Banner.JPG", "Jgdb500 · CC BY-SA 4.0", "Paisaje de bambú y montaña de Mgahinga."),
        ],
        19: [
            commons("Impressions of Lake Bunyonyi by Zenith4237 (04).jpg", "Zenith4237 · CC BY-SA 4.0", "Islas y laderas cultivadas de Lake Bunyonyi."),
            commons("A view of Lake Bunyonyi.jpg", "PatriciaUganda · CC BY 4.0", "Vista abierta de Lake Bunyonyi."),
            commons("View over Lake Bunyonyi from Lakeside Road - Southwestern Uganda - 03.jpg", "Adam Jones · CC BY-SA 3.0", "Lago Bunyonyi visto desde la carretera de la orilla."),
        ],
        20: [
            commons("Lake Mburo National Park.JPG", "Vebjorl · CC BY-SA 4.0", "Sabana de Lake Mburo National Park."),
            commons("Vast Grasslands of Lake Mburo National Park.jpg", "Sally Ruth · CC BY-SA 4.0", "Grandes pastizales dentro de Lake Mburo."),
            commons("Lake Mburo National Park - Uganda 20190927 084252.jpg", "Josefito123 · CC BY-SA 4.0", "Paisaje real de Lake Mburo National Park en 2019."),
        ],
    },
}

PHOTOS["ruanda"] = {
    1: [
        commons("Musanze Cave.jpg", "Joseph Lionceau · CC BY-SA 4.0", "Galería real de lava en Musanze Caves."),
        commons("Musanze cave.jpg", "Zamda12 · CC BY-SA 4.0", "Interior de las cuevas de Musanze durante una visita."),
        commons("Musanze-Caves.jpg", "Chretie17 · CC BY-SA 4.0", "Boca y paredes de lava de Musanze Caves."),
    ],
    2: [
        commons("Mountain gorilla (Gorilla beringei beringei) female with baby.jpg", "Charles J Sharp · CC BY-SA 4.0", "Hembra y cría de gorila de montaña en Volcanoes National Park."),
        commons("Mountain gorilla (Gorilla beringei beringei) female 2.jpg", "Charles J Sharp · CC BY-SA 4.0", "Gorila de montaña fotografiado dentro del parque."),
        commons("Mountain gorilla from Susa Group in Karisimbi thicket of Volcanoes National Park in Rwanda. Emmanuel Kwizera.jpg", "Emmanuel Kwizera · CC BY-SA 4.0", "Gorila del grupo Susa en la vegetación de Karisimbi."),
    ],
    3: [
        commons("Bisoke Crater Lake in Volcanoes National Park, Rwanda.jpg", "Happy Gentille · CC0", "Lago del cráter de Bisoke en Volcanoes National Park."),
        commons("Bisoke Crater View.jpg", "Joseph Lionceau · CC BY-SA 4.0", "Vista del borde y lago del cráter de Bisoke."),
        commons("On the top of Mount Bisoke, Rwanda.jpg", "Alex Niragira · CC BY-SA 4.0", "Excursionistas en la cumbre de Mount Bisoke."),
    ],
    4: [
        commons("Digit's and Dian Fossey's graves.jpg", "Fanny Schertzer · CC BY 3.0", "Tumbas de Dian Fossey y Digit en el antiguo Karisoke."),
        commons("Tombe Dian Fossey.jpg", "Zinkiol · CC BY-SA 4.0", "Tumba de Dian Fossey dentro del cementerio de montaña."),
        commons("Gorilla and Dian Fossey's graveyard.jpg", "Fanny Schertzer · CC BY 3.0", "Cementerio de gorilas y de Dian Fossey."),
    ],
    5: [
        commons("Twin lakes burera and ruhondo Rwanda.jpg", "Rogerirakoze · CC BY-SA 4.0", "Lagos gemelos Burera y Ruhondo con los Virunga al fondo."),
        commons("Lake Ruhondo.jpg", "Joseph Lionceau · CC BY-SA 4.0", "Orilla y colinas de Lake Ruhondo."),
        commons("Burera lake.jpg", "Ntwali Jay · CC BY-SA 4.0", "Lake Burera, el otro lago gemelo del conjunto."),
    ],
    6: [
        commons("Scene along Shore of Lake Kivu - Looking toward DR Congo Border - Rubavu-Gisenyi - Rwanda - 01.jpg", "Adam Jones · CC BY-SA 3.0", "Orilla del lago Kivu en Rubavu mirando hacia la frontera congoleña."),
        commons("Shore of Lake Kivu en route to Rubona - Near Rubavu-Gisenyi - Rwanda.jpg", "Adam Jones · CC BY-SA 3.0", "Costa del lago Kivu cerca de Rubavu."),
        commons("Harbor Scene - Rubona - Near Rubavu-Gisenyi - Rwanda.jpg", "Adam Jones · CC BY-SA 3.0", "Escena portuaria en Rubona, cerca de Rubavu."),
    ],
    7: [
        commons("Congo-Nile trail - 6956319035.jpg", "François Terrier · CC BY 2.0", "Pista y paisaje rural del Congo Nile Trail."),
        commons("Batwa people in Rwanda in the village of Kiguri on the Congo Nile Trail (3).jpg", "Hanay · CC BY-SA 3.0", "Aldea de Kiguri en el Congo Nile Trail; fotografía documental acreditada."),
        commons("Batwa people in Rwanda in the village of Kiguri on the Congo Nile Trail (2).jpg", "Hanay · CC BY-SA 3.0", "Entorno de Kiguri en el recorrido del Congo Nile Trail."),
    ],
    8: [
        commons("Shore of Lake Kivu - Karongi-Kibuye - Western Rwanda - 01.jpg", "Adam Jones · CC BY-SA 3.0", "Bahía y orilla de Karongi-Kibuye."),
        commons("Shore of Lake Kivu - Karongi-Kibuye - Western Rwanda - 02.jpg", "Adam Jones · CC BY-SA 3.0", "Otra vista exacta del frente de agua de Karongi."),
        commons("View over Lake Kivu - Outside Kibuye (Karongi) - Rwanda (8970076941).jpg", "Adam Jones · CC BY-SA 2.0", "Lago Kivu visto desde las colinas de Karongi."),
    ],
    9: [
        commons("View over Rwandan Shore of Lake Kivu - With DR Congo-Bukavu at Rear - Cyangugu (Rusizi) - Rwanda (9008089727).jpg", "Adam Jones · CC BY-SA 2.0", "Orilla ruandesa en Rusizi con Bukavu al fondo."),
        commons("View over Lake Kivu with Overturned Boats - Cyangugu (Rusizi) - Rwanda (9009284768).jpg", "Adam Jones · CC BY-SA 2.0", "Lago Kivu y barcas en Cyangugu-Rusizi."),
        commons("Panorama of Rwandan Shore of Lake Kivu - With DR Congo at Rear - Cyangugu (Rusizi) - Rwanda (9008173737).jpg", "Adam Jones · CC BY-SA 2.0", "Panorama del extremo sur del lago desde Rusizi."),
    ],
    10: [
        commons("Nyungwe Canopy Walk.jpg", "Alex Niragira · CC BY-SA 4.0", "Pasarela suspendida sobre el bosque de Nyungwe."),
        commons("Nyungwe Inside Canopy Walk.jpg", "Alex Niragira · CC BY-SA 4.0", "Visitantes dentro del recorrido del dosel de Nyungwe."),
        commons("Nyungwe canopy sun set.jpg", "BENAYOBI · CC BY-SA 4.0", "Dosel del bosque de Nyungwe al final del día."),
    ],
    11: [
        commons("National Museum of Rwanda - Butare - Flickr - Dave Proffer (3).jpg", "Dave Proffer · CC BY 2.0", "Edificio del Museo Etnográfico de Huye, antigua Butare."),
        commons("RwandaNationalMuseum.jpg", "Amakuru · CC BY-SA 3.0", "Fachada del museo nacional en Huye."),
        commons("Hutte royale reconstituée au musee national de Butare.JPG", "Antoinetorrens · CC BY-SA 3.0", "Vivienda tradicional reconstruida en el recinto del museo."),
    ],
    12: [
        commons("King's palace in Nyanza.jpg", "Guswen · CC BY 3.0", "Palacio tradicional reconstruido en Nyanza."),
        commons("Rwanda Nyanza Mwami Palace.jpg", "Amakuru · CC BY-SA 3.0", "Exterior del Mwami Palace en Nyanza."),
        commons("King's Palace Museum 2022-1.jpg", "Yakov Fedorov · CC BY-SA 4.0", "King's Palace Museum fotografiado en 2022."),
    ],
    13: [
        commons("Front side in Richard Kandt museum.jpg", "Inezac · CC BY-SA 4.0", "Fachada principal de Kandt House Museum."),
        commons("Front side in Richard Kandt museum perspective whole view.jpg", "Inezac · CC BY-SA 4.0", "Vista completa de la antigua residencia de Richard Kandt."),
        commons("Reptiles House at Kandt House Museum in Rwanda (2).jpg", "Adygrafix250 · CC BY-SA 4.0", "Sección de reptiles del Kandt House Museum."),
    ],
    14: [
        commons("Kigali Genocide Memorial site.jpg", "Brenney Nickson · CC BY-SA 4.0", "Jardines y edificio del Kigali Genocide Memorial."),
        commons("Grounds of Kigali Genocide Memorial with City in the Distance - Kigali - Rwanda.jpg", "Adam Jones · CC BY-SA 3.0", "Recinto del memorial con Kigali al fondo."),
        commons("Kigali Memorial Centre 4.jpg", "Fanny Schertzer · CC BY-SA 3.0", "Espacio conmemorativo exterior en Gisozi."),
    ],
    15: [
        commons("Nyamata Genocide Memorial Church - Flickr - Dave Proffer (11).jpg", "Dave Proffer · CC BY 2.0", "Exterior de la iglesia memorial de Nyamata."),
        commons("Nyamata Genocide Herdenkingssite.jpg", "Ziqo · CC BY-SA 4.0", "Recinto conmemorativo de Nyamata."),
        commons("Delegates Arrive with Genocide Commemoration Bouquets - Catholic Church Memorial - Nyamata - Rwanda.jpg", "Adam Jones · CC BY-SA 3.0", "Ofrendas conmemorativas a la entrada del memorial de Nyamata."),
    ],
    16: [
        commons("Canoe on Lake Muhazi, Rwanda, Africa.jpg", "Kchorst · CC BY-SA 4.0", "Canoa en Lake Muhazi."),
        commons("Passenger tour boat on Lake Muhazi, Rwanda, Africa.jpg", "Kchorst · CC BY-SA 4.0", "Barca de paseo en Lake Muhazi."),
        commons("Lake Muhazi.jpg", "Gilbert Sibomana · CC BY-SA 4.0", "Orilla y colinas de Lake Muhazi."),
    ],
    17: [
        commons("Parc National d'Akagera.jpg", "Louis Dewame · CC BY 3.0", "Lago y sabana dentro de Akagera National Park."),
        commons("Paths roads in Akagera national park.jpg", "Rodrigue250 · CC BY-SA 4.0", "Pistas de autoconducción en Akagera."),
        commons("Akagera Night Sky.jpg", "Dpiskho · CC BY-SA 4.0", "Cielo nocturno sobre el paisaje de Akagera."),
    ],
    18: [
        commons("Gishwati Natural Forest 01.jpg", "Andr96 · CC BY-SA 4.0", "Bosque natural de Gishwati."),
        commons("Gishwati Natural Forest 02.jpg", "Andr96 · CC BY-SA 4.0", "Interior y vegetación de Gishwati."),
        commons("Gishwati Forest 1986.jpg", "NASA/Jesse Allen · dominio público", "Imagen satelital histórica de Gishwati en 1986, útil para entender la deforestación y restauración."),
    ],
}

PHOTOS["malaui"] = {
    1: [
        commons("Karonga Museum, Karonga, northern Malawi.jpg", "Michael Phoya · CC BY-SA 4.0", "Edificio real del Karonga Museum."),
        commons("Malawisaurus 04.jpg", "Alexander Leisser · CC BY-SA 4.0", "Reconstrucción de Malawisaurus en el museo de Karonga."),
        commons("Malawisaurus 01.jpg", "Alexander Leisser · CC BY-SA 4.0", "Detalle de la exposición de Malawisaurus."),
    ],
    2: [
        commons("Stone House, Livingstonia.jpg", "Michael Phoya · CC BY-SA 3.0", "Stone House Museum en Livingstonia."),
        commons("Livingstonia Mission Church, Malawi 01.jpg", "Paul Shaffner · CC BY 2.0", "Iglesia de la misión de Livingstonia, visita separada de Stone House."),
        commons("Livingstonia Mission Church, Malawi 02.jpg", "Mara 1 · CC BY 2.0", "Otra vista del conjunto misionero de Livingstonia."),
    ],
    3: [
        commons("Manchewe Falls, Livingstonia. 1998.jpg", "Society of Malawi · CC BY 3.0", "Manchewe Falls junto a Livingstonia en una imagen de 1998."),
    ],
    4: [
        commons("Nyika typical.jpg", "Thomas Wagner · CC BY-SA 3.0", "Pastizales ondulados característicos de Nyika Plateau."),
        commons("Altopiano nyika-malawi.jpg", "Ludger Heide · CC BY-SA 2.0", "Paisaje abierto de la meseta de Nyika."),
        commons("Nyika grassland.jpg", "Thomas Wagner · CC BY-SA 3.0", "Pastizal de altura dentro de Nyika National Park."),
    ],
    5: [
        commons("MzuzuMalawi.JPG", "Malawiana · dominio público", "Vista urbana de Mzuzu."),
        commons("Mzuzu, Malawi.jpg", "Le Grand Portage · CC BY 2.0", "Calle y actividad diaria en Mzuzu."),
        commons("Mzuzu Market 5.jpg", "Mike W · CC BY-SA 2.0", "Mercado de Mzuzu, referencia de la escala de servicios."),
    ],
    6: [
        commons("Nkhata Bay Lake Malawi.jpg", "Avi Alpert · CC BY-SA 2.0", "Bahía y relieve costero de Nkhata Bay."),
        commons("Nkhata Bay, Malawi.jpg", "JackyR · CC BY-SA 3.0", "Frente de agua real de Nkhata Bay."),
    ],
    7: [
        commons("\"Old Mission Station, Bandawe, Livingstonia\", Malawi, ca.1910 (imp-cswc-GB-237-CSWC47-LS4-1-003).jpg", "Autor desconocido · dominio público", "Documento histórico de la antigua misión de Bandawe hacia 1910."),
        commons("Bandawe Shore, Malawi, (s.d.) (imp-cswc-GB-237-CSWC47-LS5-1-023).jpg", "Autor desconocido · dominio público", "Documento histórico de la costa de Bandawe."),
    ],
    8: [
        commons("Likoma Island Cathedral - Malawi.jpg", "TravelingOtter · CC BY-SA 2.0", "Fachada de St Peter's Cathedral en Likoma."),
        commons("St Peters Cathedral Likoma Island 2026.jpg", "GJU Malawi · CC BY 4.0", "Catedral de Likoma fotografiada en 2026."),
        commons("St peters church likoma island malawi.jpg", "Moongateclimber · CC BY-SA 3.0", "Interior y escala de St Peter's Cathedral."),
    ],
    9: [
        commons("Flickr - ggallice - Nkhotakota Game Reserve.jpg", "Geoff Gallice · CC BY 2.0", "Paisaje de miombo en Nkhotakota Wildlife Reserve."),
        commons("Nkhotakota Wildlife Reserve, Malawi (2498415131).jpg", "Joachim Huber · CC BY-SA 2.0", "Pista y vegetación dentro de la reserva de Nkhotakota."),
        commons("Nkhotakota Wildlife Reserve, Malawi (2499242426).jpg", "Joachim Huber · CC BY-SA 2.0", "Río y bosque en Nkhotakota Wildlife Reserve."),
    ],
    10: [
        commons("Nkhotakota, Malawi1.jpg", "JackyR · CC BY-SA 3.0", "Livingstone Tree y su monumento en Nkhotakota."),
    ],
    11: [
        commons("Senga Bay Fischerdorf.jpg", "Corenetic · CC BY-SA 4.0", "Aldea de pescadores en Senga Bay."),
        commons("Senga Bay Strand.JPG", "Brian Dell · dominio público", "Playa real de Senga Bay."),
        commons("Senga Bay sunrise.JPG", "Brian Dell · dominio público", "Amanecer sobre el lago en Senga Bay."),
    ],
    12: [
        commons("Kasungu lifupa2.jpg", "Thomas Wagner · CC BY-SA 3.0", "Lago Lifupa dentro de Kasungu National Park."),
        commons("Yawning Hippo in Kasungu National Park.jpg", "Salix Oculus · CC BY-SA 4.0", "Hipopótamo fotografiado en Kasungu; el avistamiento no se garantiza."),
        commons("Kasungu miombo1.jpg", "Thomas Wagner · CC BY-SA 3.0", "Bosque de miombo característico de Kasungu."),
    ],
    13: [
        commons("Lilongwe Wildlife Centre - entrance - Jan 2018.jpg", "Nesnad · CC BY 3.0", "Entrada del Lilongwe Wildlife Centre."),
        commons("Lilongwe Wildlife Centre - inside - Jan 2018.jpg", "Nesnad · CC BY 3.0", "Sendero dentro del Lilongwe Wildlife Centre."),
    ],
    14: [
        commons("Chongoni rock art.jpg", "Malawi · dominio público", "Panel de arte rupestre de Chongoni."),
        commons("Chongoni Rock-Art Area-110132.jpg", "Lazare Eloundou Assomo · CC BY-SA 3.0 IGO", "Abrigo y pinturas del área UNESCO de Chongoni."),
        commons("Chongoni Rock-Art Area-110134.jpg", "Lazare Eloundou Assomo · CC BY-SA 3.0 IGO", "Detalle documentado de otro panel de Chongoni."),
    ],
    15: [
        commons("Museum rand.jpg", "Snickers-rocks · CC BY-SA 3.0", "Museo Chamare dentro del Kungoni Centre."),
        commons("Carving center rand.jpg", "Snickers-rocks · CC BY-SA 3.0", "Taller de talla del Kungoni Centre en Mua."),
        commons("Pavillions bearbeitet rand.jpg", "Snickers-rocks · CC BY-SA 3.0", "Pabellones del conjunto cultural de Kungoni."),
    ],
    16: [
        commons("Otter Point, Cape Maclear (Malawi).jpg", "Hans Hillewaert · CC BY-SA 4.0", "Otter Point en Cape Maclear, dentro de Lake Malawi National Park."),
        commons("Dugouts on Lake Malawi.jpg", "Hans Hillewaert · CC BY-SA 4.0", "Canoas en el lago Malaui junto a Cape Maclear."),
        commons("Dugout canoe.jpg", "Hans Hillewaert · CC BY-SA 4.0", "Canoa tradicional en el agua del parque nacional."),
    ],
    17: [
        commons("Liwonde Park - view of Shire River.jpg", "Brian Dell · dominio público", "Río Shire dentro de Liwonde National Park."),
        commons("Elephants in Liwonde National Park (cropped).JPG", "Brian Dell · dominio público", "Elefantes fotografiados en Liwonde; el encuentro no se garantiza."),
        commons("Impala's in Liwonde National Park Malawi.jpg", "Arnoldus9 · CC BY-SA 4.0", "Impalas en el paisaje real de Liwonde."),
    ],
    18: [
        commons("Zomba Plateau banner.jpg", "Rockwurm/Jjtkk · CC BY-SA 3.0", "Bosque y relieve de Zomba Plateau."),
        commons("View of Zomba plateau from north.JPG", "Brian Dell · dominio público", "Meseta de Zomba vista desde el norte."),
        commons("Zomba Plateau seen from south.jpg", "Felefuchs · CC BY-SA 3.0", "Perfil de Zomba Plateau visto desde el sur."),
    ],
    19: [
        commons("Old Mandala house, Malawi oldest standing building, Blantyre.jpg", "Society of Malawi · CC BY-SA 4.0", "Mandala House en Blantyre."),
        commons("Mandala, from Old Mandala House, Blantyre..jpg", "Society of Malawi · CC BY-SA 4.0", "Vista desde el recinto de Old Mandala House."),
        commons("Mandala Manager's House, Blantyre.jpg", "Wandumi · CC BY-SA 3.0", "Casa del gerente dentro del conjunto histórico de Mandala."),
    ],
    20: [
        commons("Mount Mulanje (15669855526).jpg", "David Davies · CC BY-SA 2.0", "Paredes y vegetación de Mount Mulanje."),
        commons("Mount Mulanje (15073633334).jpg", "David Davies · CC BY-SA 2.0", "Macizo de Mulanje visto desde sus faldas."),
        commons("Mount Mulanje (15695175852).jpg", "David Davies · CC BY-SA 2.0", "Sendero y relieve granítico en Mount Mulanje."),
    ],
    21: [
        commons("Teeplantage bei Thyolo.jpg", "Ferdinand Groeger · CC BY-SA 3.0", "Plantación de té en Thyolo, el distrito de Satemwa."),
        commons("Malawi Tea Estate.jpg", "Steve Evans · CC BY 2.0", "Campos de té en una finca de Malaui."),
        commons("Tea plantation near Mulanje.JPG", "Papphase · dominio público", "Plantación de té cerca de Mulanje y Thyolo."),
    ],
    22: [
        commons("Majete Wildlife Reserve Entrance.jpg", "Stonyyy · CC BY-SA 3.0", "Entrada señalizada de Majete Wildlife Reserve."),
        commons("Majete wildlife reserve.jpg", "David Davies · CC BY-SA 2.0", "Paisaje dentro de Majete Wildlife Reserve."),
        commons("Elephant at Majete wildlife reserve (15073475793).jpg", "David Davies · CC BY-SA 2.0", "Elefante fotografiado en Majete; el avistamiento no se garantiza."),
    ],
}


def apply_country(country: str) -> None:
    path = ROOT / "content" / "pois" / f"{country}.json"
    pois = json.loads(path.read_text(encoding="utf-8"))
    by_number = {poi["n"]: poi for poi in pois}

    expected = set(by_number)
    for label, values in (
        ("coordenadas", COORDS[country]),
        ("contenido", CONTENT[country]),
        ("enlaces", LINKS[country]),
        ("fotografías", PHOTOS[country]),
    ):
        if set(values) != expected:
            missing = sorted(expected - set(values))
            extra = sorted(set(values) - expected)
            raise ValueError(f"{country}: {label} incompletos; faltan={missing}, sobran={extra}")

    for number, poi in by_number.items():
        poi["lat"], poi["lon"] = COORDS[country][number]
        if number in NAMES.get(country, {}):
            poi["name"] = NAMES[country][number]
        poi["dog"] = DOGS[country][number]
        poi["desc"] = CONTENT[country][number]["desc"]
        poi["visit"] = CONTENT[country][number]["visit"]
        poi["links"] = LINKS[country][number]
        poi["photos"] = PHOTOS[country][number]
        primary = poi["photos"][0]
        poi["img"] = primary["img"]
        poi["source"] = primary["source"]
        poi["credit"] = primary["credit"]

    path.write_text(json.dumps(pois, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace_strings(value: object, replacements: tuple[tuple[str, str], ...]) -> object:
    if isinstance(value, str):
        for old, new in replacements:
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [replace_strings(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: replace_strings(item, replacements) for key, item in value.items()}
    return value


def update_ficha(country: str) -> None:
    path = ROOT / "content" / "ficha" / f"{country}.json"
    ficha = json.loads(path.read_text(encoding="utf-8"))
    updated = replace_strings(ficha, FICHA_REPLACEMENTS[country])
    path.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    for country_name in ("uganda", "ruanda", "malaui"):
        apply_country(country_name)
        update_ficha(country_name)

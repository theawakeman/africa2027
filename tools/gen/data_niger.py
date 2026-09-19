# -*- coding: utf-8 -*-
"""Níger — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Níger está EXCLUIDO POR PROTOCOLO: golpe militar de julio de 2023, junta del CNSP, salida de la CEDEAO junto a Mali y Burkina Faso, ruptura con Francia y con la misión militar estadounidense, y yihadismo activo en Tillabéri (frontera de las tres fronteras), Diffa (Boko Haram/ISWAP) y el norte. El MAEC desaconseja viajar bajo cualquier circunstancia. La app solo tiene una ficha stub: créala entera con el formato del piloto de Túnez. La ficha es INFORMATIVA. Ojo a dos datos que hay que verificar bien: el estado del visado tras la ruptura diplomática (dónde se pide ahora para un español) y si el Aïr y el Ténéré, que fueron el gran destino sahariano de los años noventa, tienen hoy alguna vía legal de acceso. El Árbol del Ténéré original fue derribado en 1973 y está en el Museo Nacional de Niamey: dilo, no lo pongas como si siguiera en pie.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/niger.json y audit/pdi/niger.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Niamey · Museo Nacional Boubou Hama y la orilla del Níger", cat="Cultura", prio="Alta",
        dog="prohibido", time="medio día",
        lat=13.5109553, lon=2.1071253,  # Google Maps: Museo Nacional de Níger «Boubou Hama»
        desc="El museo nacional de Níger, abierto el 18 de diciembre de 1959, es el mejor resumen del país en un solo recinto: pabellones etnográficos con cinco casas tradicionales (fulani, hausa, songhai, tuareg y zarma), arqueología, artesanía y un zoo. Aquí se guarda, EN SU PROPIO MAUSOLEO DESDE 1979, el Árbol del Ténéré original, derribado por un camión en 1973. El río queda a un paso, con los puentes Kennedy y de la Amistad Chino-Nigerina. Advertencia: el MAEC desaconseja absolutamente viajar, y Niamey elevó su nivel de riesgo tras un secuestro en el centro en octubre de 2025.",
        dog_note="Museo con zoo de cincuenta especies: los perros no entran en recintos museísticos ni en zoológicos.",
        visit={
            "why": "Es la única parada donde se entiende Níger entero sin salir de la capital, y donde está físicamente el Árbol del Ténéré. Con 170.000 visitantes anuales en 2013 era el museo más visitado del país.",
            "see": "Las cinco casas tradicionales por etnia, las salas de arqueología y paleontología, el pabellón artesanal y el mausoleo del Árbol del Ténéré. El zoo, con cincuenta especies, es la parte más discutible del conjunto.",
            "access": "Región de Niamey (distrito capital). Asfalto urbano hasta la puerta; aparcamiento para dos 4x4 en la calle, mejor con vigilante. Horario y tarifa no confirmados en fuente abierta: POR CONFIRMAR. El pin marca la entrada principal del museo, no el recinto del zoo. Seguridad: MAEC 9-02-2026 desaconseja absolutamente viajar a todo el país y señala riesgo muy elevado en Niamey tras el secuestro de octubre de 2025, recomendando evitar desplazamientos nocturnos y a pie por la ciudad.",
            "when": "Primera hora de la mañana, en estación seca (noviembre a febrero), cuando el calor aún permite recorrer los pabellones al aire libre.",
            "skip": "Descártalo mientras el MAEC mantenga el nivel de desaconsejar absolutamente viajar, que es la situación a fecha de esta ficha.",
        },
        links=[
            {"label": "Musée National Boubou Hama (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Niger_National_Museum"},
            {"label": "Niamey (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Niamey"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niamey_from_grand_mosque_theatre_2006.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niamey_from_grand_mosque_theatre_2006.jpg",
                "credit": "Roland Huziaker · CC BY-SA 2.0",
                "caption": "Niamey desde el alminar de la gran mezquita.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niamey,_Niger_1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niamey,_Niger_1.jpg",
                "credit": "Lars Rosendahl Appelquist · CC BY-SA 4.0",
                "caption": "Una avenida de Niamey.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niamey,_Niger_11.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niamey,_Niger_11.jpg",
                "credit": "Lars Rosendahl Appelquist · CC BY-SA 4.0",
                "caption": "Vendedores callejeros en Niamey.",
            },
        ],
    ),
    dict(
        n=2, name="Parque nacional de la W · leones y elefantes del río (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=12.3500368, lon=2.3549858,  # Google Maps: Parque Nacional de la W (Níger)
        desc="Creado por decreto el 4 de agosto de 1954 y declarado Patrimonio de la Humanidad en 1996, el W nigerino es la pieza original de un conjunto de 10.000 km² repartido entre Níger, Burkina Faso y Benín; en 2017 la UNESCO lo amplió como Complejo W-Arly-Pendjari. Guarda leones de África Occidental, elefantes de sabana, hipopótamos, leopardos y MÁS DE 350 ESPECIES DE AVES. Advertencia: el parque está en plena zona de las tres fronteras y ha sufrido ataques recientes, con un episodio en 2025 que dejó 54 víctimas.",
        dog_note="Parque nacional con leones, leopardos y elefantes: los perros no entran, ni en el vehículo.",
        visit={
            "why": "Es la mejor fauna de sabana de Níger y el único punto del país donde todavía quedan leones de África Occidental en libertad.",
            "see": "Elefantes y hipopótamos en los meandros del río Níger y del Tapoa, antílopes, babuinos y una avifauna de más de 350 especies; guepardos, muy escasos, con unos 25 individuos estimados en todo el complejo W-Arli-Pendjari.",
            "access": "Región de Tillabéri, departamento de Say, unos 150 km al sur de Niamey. Pista y asfalto hasta La Tapoa, la puerta nigerina del parque; a partir de ahí, pistas de tierra solo aptas en estación seca y con vehículo alto. Hay espacio de sobra para dos 4x4 en el recinto de La Tapoa. Tarifas, horarios y obligatoriedad de guía: POR CONFIRMAR, no hay web oficial nigerina operativa localizada. El pin marca la puerta de La Tapoa, no el centroide del parque. Seguridad: región de Tillabéri, señalada por el MAEC (9-02-2026) como zona de amenaza terrorista permanente dentro de un país al que se desaconseja absolutamente viajar. El FCDO británico (29-08-2026) desaconseja todo viaje a Níger sin excepción, y Canadá (9-09-2026) pide evitar todo viaje y cita expresamente las zonas fronterizas con Malí y Burkina Faso.",
            "when": "Estación seca, de diciembre a mayo; la fauna se concentra en el agua y las pistas son transitables. En la estación de lluvias el sector nigerino suele cerrar.",
            "skip": "Descártalo mientras la zona de las tres fronteras siga activa: aquí el riesgo no es teórico, ha habido ataques mortales dentro del complejo.",
        },
        links=[
            {"label": "UNESCO · Complexe W-Arly-Pendjari (ficha 749)", "url": "https://whc.unesco.org/en/list/749"},
            {"label": "W National Park (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/W_National_Park"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bends_in_the_River_Niger_which_give_W_National_Park_its_distinctive_name.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bends_in_the_River_Niger_which_give_W_National_Park_its_distinctive_name.jpg",
                "credit": "Júlio Reis · Public domain",
                "caption": "Los meandros del Níger que dan nombre al parque de la W.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Elephants_bath_park_w_wide_2006.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Elephants_bath_park_w_wide_2006.jpg",
                "credit": "Roland Hunziker · CC BY-SA 2.0",
                "caption": "Elefantes en el sector nigerino del parque.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Landsacpe_dry_stream_park_w_niger_2006.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Landsacpe_dry_stream_park_w_niger_2006.jpg",
                "credit": "Roland Hunziker · CC BY-SA 2.0",
                "caption": "Un cauce seco del parque de la W.",
            },
        ],
    ),
    dict(
        n=3, name="Reserva de jirafas de Kouré · las últimas jirafas de África Occidental", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="medio día",
        lat=13.3253586, lon=2.5916443,  # Google Maps: Kouré
        desc="A 60 km al este de Niamey, en la carretera de Dallol Bosso, sobrevive la ÚLTIMA POBLACIÓN SILVESTRE de jirafa de África Occidental (Giraffa camelopardalis peralta). De 49 animales a mediados de los noventa se ha pasado a unos 600, uno de los grandes éxitos de conservación del Sahel. No hay vallas: las jirafas comparten la brousse tigrée con los campos y se buscan a pie con guía local. Advertencia: el 9 de agosto de 2020 un atentado en la reserva mató a varios turistas franceses y a sus acompañantes nigerinos.",
        dog_note="Zona de fauna protegida con guía obligatorio y aproximación a pie: el perro se queda en el vehículo o, mejor, en Niamey.",
        visit={
            "why": "Es el único sitio del mundo donde se ve la subespecie peralta en libertad, y a una hora escasa de la capital.",
            "see": "Manadas de jirafas claras, de hasta 5,80 m, moviéndose entre la brousse tigrée y los campos de mijo; aves y pastores fulani alrededor.",
            "access": "Región de Tillabéri, departamento de Kollo. Asfalto desde Niamey por la RN1 hasta Kouré, unos 60 km; luego pistas de arena blanda hacia la zona de pastoreo, donde el 4x4 es necesario. Se contrata guía en el punto de acogida del pueblo; tarifa y horario POR CONFIRMAR. El pin marca el punto de acogida de guías a pie de carretera, no la zona de avistamiento, que cambia con la estación. Seguridad: Tillabéri, amenaza terrorista permanente según el MAEC (9-02-2026).",
            "when": "Primera hora de la mañana o última de la tarde; entre junio y septiembre las jirafas suben desde el valle del Níger hacia las tierras altas de Kouré.",
            "skip": "Descártalo mientras Tillabéri siga en amenaza terrorista permanente: el atentado de 2020 ocurrió exactamente en este recorrido.",
        },
        links=[
            {"label": "Kouré, Niger (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Kour%C3%A9,_Niger"},
            {"label": "Jirafa de África Occidental (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/West_African_giraffe"},
            {"label": "Kouré (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Kour%C3%A9"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Giraffe_koure_niger_2006.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Giraffe_koure_niger_2006.jpg",
                "credit": "Roland Hunziker · CC BY-SA 2.0",
                "caption": "Jirafa de África Occidental en Kouré.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Girafes_d'Afrique_de_l'Ouest_au_Niger.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Girafes_d'Afrique_de_l'Ouest_au_Niger.jpg",
                "credit": "Barke11 · CC BY-SA 4.0",
                "caption": "El último grupo salvaje de jirafas peralta.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Girafe_du_Niger_07.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Girafe_du_Niger_07.jpg",
                "credit": "Barke11 · CC BY-SA 4.0",
                "caption": "Jirafa en la meseta de Kouré.",
            },
        ],
    ),
    dict(
        n=4, name="Ayorou · el mercado del domingo y los hipopótamos del Níger", cat="Cultura", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=14.7328144, lon=0.9104334,  # Google Maps: Ayorou
        desc="Ayorou, a unos 200 km al noroeste de Niamey y cerca de la frontera con Malí, tiene el casco viejo en una isla del río Níger. Su MERCADO DEL DOMINGO ocupa media ciudad, de la orilla a la calle principal, y atrae a comerciantes de Malí, Burkina Faso y Nigeria; el mercado de ganado, con camellos y cebúes, es el más fotografiado del país. En las islas de aguas abajo hay hipopótamos y una avifauna notable. Advertencia: en 2023 los enfrentamientos intercomunitarios desplazaron a unas 13.400 personas hacia la localidad.",
        dog_note="Mercado de ganado muy concurrido y paseo en piragua: mala combinación para un perro.",
        visit={
            "why": "Es el mercado semanal más vivo del río y el punto de partida clásico para ver hipopótamos en piragua.",
            "see": "El mercado de ganado del domingo, las islas del Níger con hipopótamos y aves, y el casco viejo insular.",
            "access": "Región de Tillabéri, en la RN1 hacia Gao (Malí). Asfalto en mal estado desde Tillabéri; aparcamiento informal junto al mercado, suficiente para dos 4x4 pero sin vigilancia. Las salidas en piragua se negocian en el embarcadero; precio POR CONFIRMAR. El pin marca la explanada del mercado junto a la orilla. Seguridad: Tillabéri, zona de amenaza terrorista permanente para el MAEC (9-02-2026) y corredor de paso hacia Malí.",
            "when": "Domingo por la mañana para el mercado; el río va más alto y los hipopótamos se ven mejor entre diciembre y marzo.",
            "skip": "Descártalo siempre que la frontera maliense esté activa; es de los puntos más expuestos de la lista.",
        },
        links=[
            {"label": "Ayorou (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ayourou"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fleuve_Niger_%C3%A0_Ayorou_en_2023.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fleuve_Niger_%C3%A0_Ayorou_en_2023.jpg",
                "credit": "Faride.boureima · CC BY-SA 4.0",
                "caption": "Piragua en el Níger, en Ayorou.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Setting_up_at_the_Ayorou_Market_(2348830036).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Setting_up_at_the_Ayorou_Market_(2348830036).jpg",
                "credit": "ACEI Cheung · CC BY-SA 2.0",
                "caption": "Montando el mercado de Ayorou.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ASC_Leiden_-_F._van_der_Kraaij_Collection_-_04_-_045_-_Une_procession_de_quinze_dromadaires_avec_trois_escortes_-_Ayourou,_Niger,_1972.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ASC_Leiden_-_F._van_der_Kraaij_Collection_-_04_-_045_-_Une_procession_de_quinze_dromadaires_avec_trois_escortes_-_Ayourou,_Niger,_1972.jpg",
                "credit": "Fred van der Kraaij · CC BY-SA 4.0",
                "caption": "Caravana de dromedarios en Ayorou, 1972.",
            },
        ],
    ),
    dict(
        n=5, name="Agadez · la gran mezquita de adobe y el centro histórico (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=16.9741689, lon=7.986535,  # Google Maps: Agadez (la gran mezquita no figura como objeto)
        desc="Capital del sultanato desde 1449 y bisagra del comercio transahariano, Agadez conserva un centro histórico de barro inscrito por la UNESCO en 2013 (criterios ii y iii, 77,6 ha más 98,1 ha de zona tampón). Su gran mezquita, levantada en 1515 y reconstruida en 1844 respetando la forma original, remata en un MINARETE DE ADOBE DE 27 METROS, el más alto del mundo en este material. Advertencia: Agadez es hoy la puerta de las rutas migratorias hacia Libia y Argelia, con fuerte presencia de seguridad y control de movimientos de extranjeros.",
        dog_note="La mezquita es recinto religioso en uso y no admite perros; el casco viejo se recorre a pie entre mucha gente.",
        visit={
            "why": "Es la ciudad de barro mejor conservada del Sáhara central y el único casco urbano nigerino con sello UNESCO.",
            "see": "La gran mezquita y su minarete de 27 m, el palacio del sultán, el viejo barrio de Katanga, los talleres de plateros tuareg y un trazado urbano que todavía respeta los límites del campamento original.",
            "access": "Región de Agadez, a 520 m de altitud. Asfalto desde Tahoua y desde Zinder, en estado irregular. Aparcamiento en la plaza de la mezquita, amplio para dos 4x4. La subida al minarete se hace con guardián y propina; horario y tarifa POR CONFIRMAR. El pin marca la puerta de la gran mezquita, el punto al que se conduce. Seguridad: el MAEC (9-02-2026) desaconseja absolutamente viajar a todo Níger y advierte específicamente sobre los desplazamientos fuera de Niamey; la región de Agadez no aparece nombrada una por una en el aviso, pero queda cubierta por la recomendación general. Sahara Overland, referencia clásica de las rutas transaharianas, afirma que NINGÚN TURISTA HA CRUZADO A NÍGER DESDE 2011 y que el noreste del país exigía escolta militar en convoy; no hay constancia reciente de viajeros admitidos en esos convoyes. Canadá (9-09-2026) desaconseja expresamente viajar a Agadez, Arlit, Tahoua y Tillabéri.",
            "when": "De noviembre a febrero, y a última hora de la tarde, cuando el adobe toma color y la temperatura baja.",
            "skip": "Descártalo mientras el MAEC mantenga la recomendación de no viajar; sin ella, sigue exigiendo autorización de circulación para el norte.",
        },
        links=[
            {"label": "UNESCO · Historic Centre of Agadez (ficha 1268)", "url": "https://whc.unesco.org/en/list/1268"},
            {"label": "Agadez (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Agadez"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
            {"label": "Sahara Overland · rutas transaharianas", "url": "https://sahara-overland.com/routes/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/1997_277-9A_Agadez_mosque_cropped.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:1997_277-9A_Agadez_mosque_cropped.jpg",
                "credit": "Dan Lundberg · CC BY-SA 2.0",
                "caption": "La gran mezquita de adobe de Agadez.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/1997_277-16A_Agadez_hotel.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:1997_277-16A_Agadez_hotel.jpg",
                "credit": "Dan Lundberg · CC BY-SA 2.0",
                "caption": "Agadez desde el alminar de la mezquita.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_Agadez_(09),_Sidi_K%C3%A2_bakery.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_Agadez_(09),_Sidi_K%C3%A2_bakery.jpg",
                "credit": "Vincent van Zeijst · CC BY-SA 4.0",
                "caption": "Panadería tradicional en Agadez.",
            },
        ],
    ),
    dict(
        n=6, name="Macizo del Aïr · Timia, los guelta y los oasis tuareg (UNESCO en peligro)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=18.0557589, lon=8.656116,  # Google Maps: Timia
        desc="El Aïr es un macizo volcánico sahelino incrustado en pleno Sáhara y forma, con el Ténéré, las Reservas Naturales del Aïr y del Ténéré: 7.736.000 hectáreas, LA MAYOR ÁREA PROTEGIDA DE ÁFRICA, inscritas por la UNESCO en 1991 (criterios vii, ix y x) y en la Lista del Patrimonio en Peligro DESDE 1992. Timia es su oasis emblemático, con una guelta de roca que retiene agua todo el año a unos 3 km del pueblo y huertos de frutales insólitos en el Sáhara. Advertencia: acceso sujeto a autorización militar y, hoy, sin vía legal verificada.",
        dog_note="Reserva natural con fauna sahelo-sahariana amenazada y aldeas tuareg; un perro suelto es un problema en los guelta.",
        visit={
            "why": "Es el paisaje sahariano por excelencia de Níger y la razón por la que el Aïr fue un destino mayor en los años noventa.",
            "see": "La guelta permanente de Timia y su cascada estacional, los huertos de cítricos y granados, las aldeas tuareg, el grabado rupestre del Aïr y fauna relicta: gacela dorcas, gacela dama y addax.",
            "access": "Región de Agadez, al norte de la ciudad y al sur de Iferouane. Pista de arena y roca desde Agadez, sin asfalto, con tramos de fech-fech: obligatorio ir en convoy de al menos dos vehículos, con navegación autónoma y reserva de combustible. Escolta o autorización de las autoridades nigerinas exigida históricamente; VÍA LEGAL DE ACCESO ACTUAL SIN CONFIRMAR. El pin marca el pueblo de Timia, del que parte la pista a la guelta. Seguridad: MAEC 9-02-2026, se desaconseja absolutamente viajar a Níger; el norte está además bajo control militar. Sahara Overland, referencia clásica de las rutas transaharianas, afirma que NINGÚN TURISTA HA CRUZADO A NÍGER DESDE 2011 y que el noreste del país exigía escolta militar en convoy; no hay constancia reciente de viajeros admitidos en esos convoyes. Canadá (9-09-2026) desaconseja expresamente viajar a Agadez, Arlit, Tahoua y Tillabéri.",
            "when": "De noviembre a febrero; la cascada de Timia solo corre tras las lluvias de agosto y septiembre.",
            "skip": "Descártalo: no consta ninguna vía legal de acceso verificada para turistas extranjeros al Aïr, y el sitio sigue en la Lista del Patrimonio Mundial en Peligro desde 1992.",
        },
        links=[
            {"label": "UNESCO · Air and Ténéré Natural Reserves (ficha 573)", "url": "https://whc.unesco.org/en/list/573"},
            {"label": "Timia (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Timia"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
            {"label": "Sahara Overland · rutas transaharianas", "url": "https://sahara-overland.com/routes/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Montagnes_Bleus1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Montagnes_Bleus1.jpg",
                "credit": "Jacques Taberlet · CC BY 3.0",
                "caption": "Las Montañas Azules, en el macizo del Aïr.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bivouac_%C3%A0_Arakao,_Massif_de_l'A%C3%AFr,_Niger.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bivouac_%C3%A0_Arakao,_Massif_de_l'A%C3%AFr,_Niger.jpg",
                "credit": "Jacques Taberlet · CC BY 3.0",
                "caption": "Vivac en el Arakao, en el Aïr.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Un_puit_pastorale_dans_les_massifs_de_l'A%C3%AFr_(cropped).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Un_puit_pastorale_dans_les_massifs_de_l'A%C3%AFr_(cropped).jpg",
                "credit": "Faride.boureima · CC BY-SA 4.0",
                "caption": "Pozo pastoral en el Aïr.",
            },
        ],
    ),
    dict(
        n=7, name="Desierto del Ténéré · el mar de arena y el lugar del Arbre du Ténéré (UNESCO en peligro)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=17.75, lon=10.06667,  # Google Maps: (sin objeto en Google Maps; coordenada de la fuente)
        desc="El Ténéré es la mitad llana de las Reservas Naturales del Aïr y del Ténéré, Patrimonio de la Humanidad desde 1991 y EN PELIGRO DESDE 1992. En este punto crecía el Arbre du Ténéré, la acacia solitaria considerada el árbol más aislado de la Tierra, con raíces a 33-36 m de profundidad. OJO: EL ÁRBOL YA NO ESTÁ AQUÍ. Un camionero lo derribó en 1973 y el 8 de noviembre de ese año el ejemplar muerto se llevó al Museo Nacional de Niamey; en el sitio original solo queda una sencilla escultura metálica que reproduce su silueta.",
        dog_note="Travesía de desierto absoluto sin agua ni sombra durante cientos de kilómetros: inviable con perro.",
        visit={
            "why": "Es el hito simbólico del Sáhara nigerino y el punto de navegación clásico de la ruta Agadez-Bilma.",
            "see": "La escultura metálica que sustituye al árbol, el erg del Ténéré y el horizonte plano hasta el Aïr al oeste. El árbol auténtico se ve en el Museo Nacional Boubou Hama de Niamey, no aquí.",
            "access": "Región de Agadez. Sin carretera: navegación sobre arena y reg desde Agadez, varios cientos de kilómetros, con GPS, dos vehículos mínimo, autonomía completa de agua y combustible y guía local. Nunca hubo taquilla ni aparcamiento. El pin marca la escultura metálica en el emplazamiento del árbol. Seguridad: MAEC 9-02-2026, se desaconseja absolutamente viajar a Níger; el Ténéré está además dentro de un sitio UNESCO en peligro desde 1992 y bajo control militar. Sahara Overland, referencia clásica de las rutas transaharianas, afirma que NINGÚN TURISTA HA CRUZADO A NÍGER DESDE 2011 y que el noreste del país exigía escolta militar en convoy; no hay constancia reciente de viajeros admitidos en esos convoyes. Canadá (9-09-2026) desaconseja expresamente viajar a Agadez, Arlit, Tahoua y Tillabéri.",
            "when": "De diciembre a febrero, y solo con el harmattan calmado; entre marzo y mayo las tormentas de arena anulan la visibilidad.",
            "skip": "Descártalo: no hay vía legal de acceso confirmada al Ténéré y, según Sahara Overland, ningún turista ha cruzado a Níger desde 2011.",
        },
        links=[
            {"label": "UNESCO · Air and Ténéré Natural Reserves (ficha 573)", "url": "https://whc.unesco.org/en/list/573"},
            {"label": "Arbre du Ténéré (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Arbre_du_T%C3%A9n%C3%A9r%C3%A9"},
            {"label": "Museo Nacional de Níger, donde está el árbol original", "url": "https://en.wikipedia.org/wiki/Niger_National_Museum"},
            {"label": "Sahara Overland · rutas transaharianas", "url": "https://sahara-overland.com/routes/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tenere_NASA.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tenere_NASA.jpg",
                "credit": "NASA · Public domain",
                "caption": "El Ténéré desde satélite (NASA).",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Le_reste_de_l'arbre_du_T%C3%A9n%C3%A9r%C3%A9_au_mus%C3%A9e_national_du_Niger.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Le_reste_de_l'arbre_du_T%C3%A9n%C3%A9r%C3%A9_au_mus%C3%A9e_national_du_Niger.jpg",
                "credit": "Amadouibrahim2 · CC BY-SA 4.0",
                "caption": "Lo que queda del Árbol del Ténéré, en el Museo Nacional de Niamey.",
            },
        ],
    ),
    dict(
        n=8, name="Bilma y el Kaouar · las salinas y las caravanas de sal", cat="Cultura", prio="Media",
        dog="no recomendado", time="1–2 noches",
        lat=18.68667, lon=12.91917,  # Google Maps: (sin objeto en Google Maps; coordenada de la fuente)
        desc="Bilma, 4.016 habitantes en el censo de 2012, se apoya en los acantilados del Kaouar y es el destino de la azalai, la caravana de sal que sale de Agadez A UNOS 560 KM AL OESTE. Sus balsas de evaporación producen sal y natrón en moldes cónicos que todavía viajan a lomos de camello. Es uno de los lugares más calurosos habitados del planeta: 44,1 °C de máxima media en junio y un récord de 48,2 °C el 23 de junio de 2010, con apenas 12,7 mm de lluvia al año. Advertencia: zona militarizada y sin acceso legal confirmado.",
        dog_note="Oasis aislado a 560 km de pista de Agadez, con calor extremo: no es sitio para un perro.",
        visit={
            "why": "Es la última caravana de sal viva del Sáhara y un oasis kanuri intacto al pie del Kaouar.",
            "see": "Las balsas de evaporación y los panes cónicos de sal, los palmerales de dátiles, el Fort Dromard colonial y las dunas del erg de Bilma al oeste.",
            "access": "Región de Agadez, departamento de Bilma. Sin asfalto: unos 560 km de pista de arena y reg desde Agadez por el Ténéré, itinerario de varios días con autonomía total. Aparcamiento no aplicable; se acampa junto al oasis. Escolta militar exigida históricamente; SITUACIÓN ACTUAL POR CONFIRMAR. El pin marca las salinas al borde del palmeral. Seguridad: MAEC 9-02-2026, se desaconseja absolutamente viajar a Níger; ruta de tránsito migratorio y contrabando hacia Libia. Sahara Overland, referencia clásica de las rutas transaharianas, afirma que NINGÚN TURISTA HA CRUZADO A NÍGER DESDE 2011 y que el noreste del país exigía escolta militar en convoy; no hay constancia reciente de viajeros admitidos en esos convoyes. Canadá (9-09-2026) desaconseja expresamente viajar a Agadez, Arlit, Tahoua y Tillabéri.",
            "when": "De diciembre a febrero; la azalai se organiza tradicionalmente en otoño e invierno, fechas exactas POR CONFIRMAR.",
            "skip": "Descártalo si no hay convoy autorizado: es el punto más remoto de toda la ficha y no hay rescate posible.",
        },
        links=[
            {"label": "Bilma (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bilma"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
            {"label": "Sahara Overland · rutas transaharianas", "url": "https://sahara-overland.com/routes/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bilma-Saline-85.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bilma-Saline-85.jpg",
                "credit": "Holger Reineccius · CC BY-SA 3.0",
                "caption": "Las salinas de Kalala, junto a Bilma.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bilma-Salzkarawane1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bilma-Salzkarawane1.jpg",
                "credit": "Holger Reineccius · CC BY-SA 3.0",
                "caption": "Caravana de sal camino de Agadez.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/33GL9PL-highres-1685863509.webp?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:33GL9PL-highres-1685863509.webp",
                "credit": "4deefing · CC BY-SA 4.0",
                "caption": "Fachi, el otro oasis del Kaouar, desde el aire.",
            },
        ],
    ),
    dict(
        n=9, name="Gadoufaoua · el cementerio de dinosaurios del Ténéré", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=16.8333333, lon=9.4166667,  # Google Maps: Gadoufaoua
        desc="En el borde occidental del Ténéré, la Formación Elrhaz aflora en Gadoufaoua como uno de los yacimientos de vertebrados del Cretácico Inferior más ricos del mundo, de hace 125 a 112 millones de años (Aptiense-Albiense). De aquí salieron Ouranosaurus, Nigersaurus y SARCOSUCHUS IMPERATOR, el cocodrilo gigante cuyo cráneo de 1,8 m desenterró Paul Sereno en 1997; Philippe Taquet lo había estudiado ya en 1970. Advertencia: los fósiles están protegidos, no se recoge nada, y la zona carece de vía de acceso legal confirmada.",
        dog_note="Yacimiento en pleno desierto, sin agua ni sombra ni servicio alguno.",
        visit={
            "why": "Es el yacimiento que dio el SuperCroc y el paisaje donde el Sáhara enseña que fue río y bosque.",
            "see": "Campos de huesos y placas óseas erosionando en superficie sobre arenisca, y el reg desnudo del Ténéré occidental. Todo hallazgo es propiedad del Estado nigerino.",
            "access": "Región de Agadez. Sin carretera ni pista señalizada: navegación GPS desde Agadez a través del reg, varios centenares de kilómetros, con guía y dos vehículos mínimo. No hay instalaciones de ningún tipo. El pin marca el área principal del yacimiento, que es extenso y difuso: el punto es orientativo. Seguridad: MAEC 9-02-2026, se desaconseja absolutamente viajar a Níger; zona norte bajo control militar. Sahara Overland, referencia clásica de las rutas transaharianas, afirma que NINGÚN TURISTA HA CRUZADO A NÍGER DESDE 2011 y que el noreste del país exigía escolta militar en convoy; no hay constancia reciente de viajeros admitidos en esos convoyes. Canadá (9-09-2026) desaconseja expresamente viajar a Agadez, Arlit, Tahoua y Tillabéri.",
            "when": "De diciembre a febrero, y siempre con luz rasante de mañana para distinguir los restos del sustrato.",
            "skip": "Descártalo sin autorización y sin acompañamiento científico o guía acreditado: además del riesgo, recolectar fósiles es delito.",
        },
        links=[
            {"label": "Elrhaz Formation / Gadoufaoua (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Gadoufaoua"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
            {"label": "Sahara Overland · rutas transaharianas", "url": "https://sahara-overland.com/routes/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Suchomimus_tenerensis_theropod_dinosaur_(Elrhaz_Formation,_Lower_Cretaceous%3B_Gadoufaoua,_Tenere_Desert,_central_Niger,_northwest-central_Africa)_2_(15414433522).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Suchomimus_tenerensis_theropod_dinosaur_(Elrhaz_Formation,_Lower_Cretaceous%3B_Gadoufaoua,_Tenere_Desert,_central_Niger,_northwest-central_Africa)_2_(15414433522).jpg",
                "credit": "James St. John · CC BY 2.0",
                "caption": "Suchomimus tenerensis, hallado en Gadoufaoua.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Suchomimus_tenerensis_(2).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Suchomimus_tenerensis_(2).jpg",
                "credit": "James St. John · CC BY 2.0",
                "caption": "Cráneo de Suchomimus del yacimiento de Gadoufaoua.",
            },
        ],
    ),
    dict(
        n=10, name="Ingall · la Cure Salée y el encuentro de nómadas", cat="Cultura", prio="Media",
        dog="no recomendado", time="1–2 noches",
        lat=16.7867314, lon=6.934332,  # Google Maps: In-Gall
        desc="In-Gall es un oasis de menos de 500 habitantes fijos que CADA SEPTIEMBRE se convierte en la capital nómada del Sáhel: la Cure Salée reúne a pastores tuareg y wodaabe al final de la estación de lluvias, cuando el ganado sube a los pastos salinos. La comuna entera censó 51.903 personas en 2012, pero es el festival el que llena el lugar de miles de nómadas, autoridades y curiosos. Advertencia: las fechas se fijan cada año y han llegado a suspenderse; conviene confirmarlas antes de moverse.",
        dog_note="Concentración masiva de ganado y de gente durante el festival: el perro estorba y corre riesgo.",
        visit={
            "why": "Es el gran encuentro pastoral del Sáhel y la ocasión de ver juntos a tuareg y wodaabe.",
            "see": "Desfiles de camellos, carreras, mercados de ganado y los rituales de cortejo wodaabe asociados al gerewol (vínculo con el gerewol no detallado en la fuente consultada: POR CONFIRMAR).",
            "access": "Región de Agadez, unos 100 km al oeste de Agadez. Pista y tramos de asfalto desde Agadez y desde Tahoua. Explanada amplia, sin problema para dos 4x4. No hay entrada formal al festival. El pin marca el núcleo de In-Gall; el campamento de la Cure Salée se monta en las afueras y cambia de sitio cada año. Seguridad: MAEC 9-02-2026, se desaconseja absolutamente viajar a Níger; además In-Gall queda entre Agadez y Tahoua, esta última señalada como zona de amenaza terrorista permanente. Sahara Overland, referencia clásica de las rutas transaharianas, afirma que NINGÚN TURISTA HA CRUZADO A NÍGER DESDE 2011 y que el noreste del país exigía escolta militar en convoy; no hay constancia reciente de viajeros admitidos en esos convoyes. Canadá (9-09-2026) desaconseja expresamente viajar a Agadez, Arlit, Tahoua y Tillabéri.",
            "when": "Septiembre, al terminar las lluvias; fuera de esas fechas In-Gall es un oasis pequeño y tranquilo.",
            "skip": "Descártalo si el festival no está confirmado ese año: sin Cure Salée el sitio no justifica el desvío.",
        },
        links=[
            {"label": "In-Gall (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/In-Gall"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
            {"label": "Sahara Overland · rutas transaharianas", "url": "https://sahara-overland.com/routes/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_In-Gall_(7).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_In-Gall_(7).jpg",
                "credit": "NigerTZai · CC BY-SA 4.0",
                "caption": "La calle principal de In-Gall.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Wodaabe_during_Gerewol,_Cure_Salee,_In-Gall,_Niger_(15380276990).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Wodaabe_during_Gerewol,_Cure_Salee,_In-Gall,_Niger_(15380276990).jpg",
                "credit": "Alfred Weidinger · CC BY 2.0",
                "caption": "Wodaabe en el gerewol de la Cure Salée.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_In-Gall_(11).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_In-Gall_(11).jpg",
                "credit": "NigerTZai · CC BY-SA 4.0",
                "caption": "Saliendo del recinto de la Cure Salée.",
            },
        ],
    ),
    dict(
        n=11, name="Zinder · el palacio del sultán y el barrio Birni", cat="Cultura", prio="Alta",
        dog="no recomendado", time="1 noche",
        lat=13.7941834, lon=9.0012665,  # Google Maps: Gran Mezquita de Zinder (junto al palacio del sultán)
        desc="A 861 km al este de Niamey, Zinder fue la capital colonial del territorio hasta 1926 y sigue siendo la ciudad hausa por excelencia. El barrio de BIRNI, fundado en 1736 por aristócratas kanuri como recinto fortificado, concentra el palacio del sultán del Damagaram, la mezquita y el Fort Cazemajou francés de 1899. La ciudad ha cuadruplicado su población desde 1977, con 235.605 habitantes en el censo de 2012. Advertencia: la carretera Niamey-Zinder es larga y los controles militares son constantes.",
        dog_note="Palacio en uso, mezquita y callejeo por un barrio densamente habitado.",
        visit={
            "why": "Es la arquitectura hausa de barro decorado mejor conservada de Níger y el sultanato más vivo del país.",
            "see": "El palacio del sultán del Damagaram en Birni, la mezquita vieja, el Fort Cazemajou, el barrio tuareg de Zengou al norte y el Grand Marché de Sabon Gari.",
            "access": "Región de Zinder. Asfalto por la RN1 desde Maradi; aparcamiento en la explanada frente al palacio, suficiente para dos 4x4. La visita al palacio se hace con permiso del chambelán y propina; horario y tarifa POR CONFIRMAR. El pin marca la puerta del palacio del sultán, en Birni. Seguridad: la región de Zinder no aparece nombrada individualmente en el aviso del MAEC de 9-02-2026, que sí desaconseja absolutamente viajar a todo el país y advierte de los desplazamientos fuera de Niamey. Canadá (9-09-2026) sí cita expresamente la región de Zinder entre las que hay que evitar.",
            "when": "Mañana temprano, de noviembre a febrero; el viernes hay más actividad alrededor de la mezquita.",
            "skip": "Descártalo si no se puede garantizar el trayecto por la RN1 en horario diurno y sin pernocta en ruta.",
        },
        links=[
            {"label": "Zinder (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Zinder"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Zinder_Old_Town_Niger_2007.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Zinder_Old_Town_Niger_2007.jpg",
                "credit": "diasUndKompott · CC BY-SA 2.0",
                "caption": "El barrio viejo de Zinder (Birni).",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Zinder-du_ciel.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Zinder-du_ciel.jpg",
                "credit": "Mab.black · CC BY-SA 4.0",
                "caption": "Zinder desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Montagne_de_Zinder_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Montagne_de_Zinder_02.jpg",
                "credit": "AbdoulHamidAmani · CC BY-SA 4.0",
                "caption": "Los bloques graníticos dentro de la ciudad.",
            },
        ],
    ),
    dict(
        n=12, name="Maradi · la capital económica y el país hausa", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=13.5009779, lon=7.1036396,  # Google Maps: Maradi
        desc="Segunda ciudad de Níger con 267.249 habitantes en 2012, Maradi es el nudo comercial y agrícola del sur hausa y la puerta natural hacia Kano, en Nigeria. Nació como parte del estado hausa de Katsina y se independizó de él en el siglo XIX; los franceses la arrasaron en 1899 y tras la INUNDACIÓN DE 1945 la ciudad se rehízo en cuadrícula, abandonando el trazado tradicional. Como PDI turístico es flojo: vale sobre todo como parada de servicios, cambio y combustible camino de Zinder.",
        dog_note="Parada logística urbana: el perro puede quedarse en el alojamiento, no en el Grand-marché.",
        visit={
            "why": "Es el mejor punto de avituallamiento entre Niamey y Zinder, y el escaparate del comercio transfronterizo con Nigeria.",
            "see": "El Grand-marché y su trasiego de cacahuete y mercancía nigeriana, la trama en cuadrícula de posguerra y el palacio del sarki. Sin monumento de primer orden.",
            "access": "Región de Maradi. Asfalto por la RN1; talleres, combustible y hoteles con patio cerrado donde caben dos 4x4. Sin entradas ni horarios que gestionar. El pin marca el Grand-marché, el punto de referencia urbano. Seguridad: la región de Maradi no aparece nombrada individualmente en el aviso del MAEC de 9-02-2026, que desaconseja absolutamente viajar a todo Níger; la proximidad de la frontera nigeriana añade riesgo de secuestro con fines económicos.",
            "when": "Cualquier día laborable, mejor por la mañana; el calor de abril y mayo es duro.",
            "skip": "Descártalo como visita si vas justo de días: es una parada logística, no un destino.",
        },
        links=[
            {"label": "Maradi (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Maradi,_Niger"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Maradi.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Maradi.JPG",
                "credit": "Mab.black · CC BY-SA 3.0",
                "caption": "Una calle de Maradi.",
            },
        ],
    ),
    dict(
        n=13, name="Tahoua y el Ader · la meseta y los mercados", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=14.8904575, lon=5.2579968,  # Google Maps: Región de Tahoua
        desc="Cuarta ciudad del país con 117.826 habitantes en 2012, Tahoua es la bisagra entre el Níger agrícola del sur y el Sáhara del norte: aquí se cruzan comerciantes hausa, fulani y tuareg desde el siglo XVII. Nació de dos aldeas, Bilbis y Fakoua, y es conocida por su TCHOUKOU, el queso seco en discos que se vende en todo el Sáhel. Advertencia: el MAEC nombra expresamente la región de Tahoua como zona de amenaza terrorista permanente en su actualización de 9 de febrero de 2026.",
        dog_note="Ciudad de paso; en el mercado, atado y controlado.",
        visit={
            "why": "Es la parada obligada camino de Agadez y el mercado donde se mezclan las tres economías del país.",
            "see": "El gran mercado semanal, los puestos de tchoukou y la meseta del Ader alrededor, árida y cortada por valles fósiles.",
            "access": "Región de Tahoua. Asfalto por la RN25 desde Niamey y hacia Agadez, con tramos degradados. Aparcamiento en hoteles con patio, válido para dos 4x4. Sin entradas. El pin marca el Grand Marché. Seguridad: región expresamente citada por el MAEC (9-02-2026) entre las de amenaza terrorista permanente, dentro de un país al que se desaconseja absolutamente viajar. Canadá (9-09-2026) también cita expresamente Tahoua.",
            "when": "Día de mercado por la mañana; evita abril y mayo, con medias máximas cercanas a 44 °C.",
            "skip": "Descártalo mientras Tahoua siga citada por nombre en el aviso del MAEC.",
        },
        links=[
            {"label": "Tahoua (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Tahoua"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Universit%C3%A9_Djibo_Hamani_de_Tahoua_04.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Universit%C3%A9_Djibo_Hamani_de_Tahoua_04.jpg",
                "credit": "Barke11 · CC BY-SA 4.0",
                "caption": "La universidad Djibo Hamani de Tahoua.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tahoua_Niger_Kids1_2006.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tahoua_Niger_Kids1_2006.jpg",
                "credit": "Cpl. Enrique Saenz (USMC) · Public domain",
                "caption": "Niños en Tahoua.",
            },
        ],
    ),
    dict(
        n=14, name="Dogondoutchi y los Dallols · las mesetas rojas y los animismos", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=13.6441828, lon=4.0337846,  # Google Maps: Dogondoutchi
        desc="A unos 300 km al este de Niamey y a 40 km de la frontera nigeriana, Dogondoutchi se apoya en un cerro que le da nombre, «colina alta», entre depósitos de arena y arcilla del Terciario y el Cuaternario que dibujan mesetas y cornisas rojizas. Su interés no es solo el paisaje: LOS MAOURI DE ESTA ZONA SON LOS ÚLTIMOS ANIMISTAS HAUSA, y la ciudad es un centro del ritual de posesión bori, muy estudiado por antropólogos. Advertencia: fotografiar ceremonias exige permiso explícito.",
        dog_note="Lugares de culto tradicional y aldeas: el perro no debe entrar en los recintos rituales.",
        visit={
            "why": "Es la ventana a la religión tradicional hausa que sobrevive en un país musulmán al 95 %, con un marco geológico llamativo.",
            "see": "La colina y las cornisas de arenisca sobre la ciudad, los pueblos maouri del entorno y, con suerte y permiso, una sesión de bori.",
            "access": "Región de Dosso, departamento de Dogondoutchi. Asfalto por la RN1 Niamey-Birnin Konni; aparcamiento fácil en el centro para dos 4x4. Sin entradas ni horarios. El pin marca el centro de Dogondoutchi, base para los desvíos por el Dallol Maouri. Seguridad: la región de Dosso no aparece citada individualmente en el aviso del MAEC de 9-02-2026, que desaconseja absolutamente viajar a todo el país; la cercanía de la frontera nigeriana aconseja no moverse de noche.",
            "when": "De noviembre a febrero; las ceremonias bori se concentran en fechas del calendario local, POR CONFIRMAR sobre el terreno.",
            "skip": "Descártalo si vas de paso hacia Zinder con etapa larga: da para media jornada, no más.",
        },
        links=[
            {"label": "Dogondoutchi (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Dogondoutchi"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_Dogondoutchi_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_Dogondoutchi_(1).jpg",
                "credit": "NigerTZai · CC BY-SA 4.0",
                "caption": "El centro de Dogondoutchi, bajo las mesetas rojas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_Dogondoutchi_(5).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_Dogondoutchi_(5).jpg",
                "credit": "NigerTZai · CC BY-SA 4.0",
                "caption": "Calle de Dogondoutchi.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_Dogondoutchi_(3).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_Dogondoutchi_(3).jpg",
                "credit": "NigerTZai · CC BY-SA 4.0",
                "caption": "Escena urbana de Dogondoutchi.",
            },
        ],
    ),
    dict(
        n=15, name="Reserva de Termit y Tin Toumma · el último addax salvaje", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=16.0419444, lon=11.345,  # Google Maps: Macizo de Termit
        desc="El macizo de Termit es una cresta de arenisca negra muy erosionada, con picos volcánicos al norte, que se extiende 180 km de largo por 40 de ancho, unos 3.500 km². Desde 2012 forma parte de la Reserva Natural de Termit y Tin Toumma, UNA DE LAS MAYORES RESERVAS TERRESTRES DEL PLANETA, y en ella sobrevive el último núcleo silvestre de addax, junto a gacela dama, gacela dorcas, guepardo y arrui. Llueve menos de 100 mm al año. Advertencia: la reserva toca la región de Diffa, señalada por el MAEC como zona de amenaza terrorista permanente.",
        dog_note="Reserva natural con fauna sahariana crítica: guepardo sahariano, addax y gacela dama no admiten presencia de perros.",
        visit={
            "why": "Es el último refugio del addax en libertad y uno de los desiertos menos transitados del mundo.",
            "see": "La cresta negra de Termit sobre el erg de Tin Toumma, acacias paraguas y cepillos de dientes, y campamentos nómadas tubu, tuareg y árabes de Diffa. La fauna es escasa y esquiva: los avistamientos no están garantizados.",
            "access": "Regiones de Zinder y Diffa. Sin carretera: pista y navegación desde Zinder o Gouré, con guía obligatorio en la práctica y autonomía completa. No hay puerta, taquilla ni aparcamiento. El pin marca el macizo de Termit, referencia orientativa de un área enorme. Seguridad: el MAEC (9-02-2026) cita expresamente Diffa entre las regiones de amenaza terrorista permanente, por actividad de Boko Haram e ISWAP, dentro de un país al que se desaconseja absolutamente viajar.",
            "when": "De diciembre a febrero; fuera de esas fechas el calor hace inviable la travesía.",
            "skip": "Descártalo mientras Diffa siga citada por el MAEC: no hay forma segura de llegar.",
        },
        links=[
            {"label": "Macizo de Termit (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Termit_Massif"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Termit1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Termit1.jpg",
                "credit": "Jacques Taberlet · CC BY 3.0",
                "caption": "El macizo de Termit.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Maci%C3%A7o_de_Termit_no_N%C3%ADger.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Maci%C3%A7o_de_Termit_no_N%C3%ADger.jpg",
                "credit": "INPE (Brasil) · CC BY-SA 2.0",
                "caption": "Termit desde satélite.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Addax_(Addax_nasomaculatus)_female.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Addax_(Addax_nasomaculatus)_female.jpg",
                "credit": "Charles J. Sharp · CC BY-SA 4.0",
                "caption": "Addax hembra (foto de la especie, no tomada en Termit).",
            },
        ],
    ),
    dict(
        n=16, name="Tillabéri · el río, las dunas y la zona de las tres fronteras", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=14.2061141, lon=1.4579696,  # Google Maps: Tillabéri
        desc="Capital de departamento y región, Tillabéri se asoma al Níger unos 115 km al noroeste de Niamey, en el tramo donde el río se ensancha entre dunas y arrozales. Con 47.678 habitantes en 2012, es una ciudad-mercado tranquila cuyo atractivo son las orillas al atardecer. Pero su nombre se ha vuelto sinónimo de otra cosa: TILLABÉRI ES LA ZONA DE LAS TRES FRONTERAS, entre Níger, Malí y Burkina Faso, y el MAEC la cita expresamente como región de amenaza terrorista permanente.",
        dog_note="Orillas con hipopótamos y cocodrilos aguas abajo; el perro no debe bajar al agua.",
        visit={
            "why": "Es el paisaje fluvial más abierto del Níger nigerino, con dunas cayendo directamente al agua.",
            "see": "El río al atardecer, las piraguas de pescadores sorko, los arrozales de ribera y el mercado local.",
            "access": "Región de Tillabéri. Asfalto por la RN1 desde Niamey, unos 115 km; aparcamiento junto a la orilla, amplio para dos 4x4. Sin entradas ni horarios. El pin marca el acceso a la ribera del río en la ciudad. Seguridad: el MAEC (9-02-2026) cita Tillabéri entre las tres regiones de amenaza terrorista permanente y desaconseja absolutamente viajar a Níger. El FCDO (29-08-2026) y Canadá (9-09-2026) desaconsejan igualmente todo viaje, y Canadá cita Tillabéri y las fronteras con Malí y Burkina Faso.",
            "when": "Última hora de la tarde, de diciembre a febrero, cuando la luz sobre el río compensa la parada.",
            "skip": "Descártalo mientras la zona de las tres fronteras siga activa; es, de toda la lista, la etiqueta de riesgo más repetida.",
        },
        links=[
            {"label": "Tillabéri (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Tillab%C3%A9ri"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_Tillab%C3%A9ri,_2008_43.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_Tillab%C3%A9ri,_2008_43.jpg",
                "credit": "Lars Rosendahl Appelquist · CC BY-SA 4.0",
                "caption": "El norte de la región de Tillabéri.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_Tillab%C3%A9ri,_2008_50.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_Tillab%C3%A9ri,_2008_50.jpg",
                "credit": "Lars Rosendahl Appelquist · CC BY-SA 4.0",
                "caption": "Dunas y río en Tillabéri.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_Tillab%C3%A9ri,_2008_28.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_Tillab%C3%A9ri,_2008_28.jpg",
                "credit": "Lars Rosendahl Appelquist · CC BY-SA 4.0",
                "caption": "Paisaje de Tillabéri.",
            },
        ],
    ),
    dict(
        n=17, name="Dosso · el sultanato zarma y la ruta a Benín", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=13.0504833, lon=3.2080991,  # Google Maps: Dosso
        desc="A 130-140 km al sureste de Niamey, Dosso es el cruce donde se separan la carretera de Zinder y la de Benín. Es la sede del reino zarma que acabó dominando toda la región antes de la colonización, y su soberano, el ZARMAKOY, sigue siendo la autoridad tradicional: su palacio y museo fueron propuestos a la Lista Indicativa de la UNESCO en 2006. Curiosidad: la línea férrea Niamey-Dosso, construida entre 2014 y 2016, nunca llegó a explotarse por un litigio comercial y sigue huérfana.",
        dog_note="Palacio y museo en uso protocolario; el perro se queda fuera.",
        visit={
            "why": "Es el sultanato zarma mejor conservado y una parada natural en la salida hacia Benín por Gaya.",
            "see": "El palacio del Zarmakoy y su pequeño museo, el mercado y la estación ferroviaria sin trenes.",
            "access": "Región de Dosso. Asfalto por la RN1 desde Niamey, unos 135 km; aparcamiento en la explanada del palacio, suficiente para dos 4x4. Visita con permiso del secretariado del Zarmakoy; horario y tarifa POR CONFIRMAR. El pin marca la puerta del palacio del Zarmakoy. Seguridad: la región de Dosso no aparece citada individualmente en el aviso del MAEC de 9-02-2026, que sí desaconseja absolutamente viajar a todo Níger.",
            "when": "Mañana de día laborable; la ciudad se anima con las fiestas del sultanato, fechas POR CONFIRMAR.",
            "skip": "Descártalo si no vas a salir por Benín: el palacio se ve en una hora.",
        },
        links=[
            {"label": "Dosso (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Dosso,_Niger"},
            {"label": "Reserva Parcial de Fauna de Dosso (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Dosso_Reserve"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_Dosso_(5),_busy_street.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_Dosso_(5),_busy_street.jpg",
                "credit": "NigerTZai · CC BY-SA 4.0",
                "caption": "Calle de mercado en Dosso.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_Dosso_(24),_Place_Dosso_Soga.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_Dosso_(24),_Place_Dosso_Soga.jpg",
                "credit": "NigerTZai · CC BY-SA 4.0",
                "caption": "La plaza Dosso Soga.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger,_Dosso_(59),_Palais_de_Justice.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger,_Dosso_(59),_Palais_de_Justice.jpg",
                "credit": "NigerTZai · CC BY-SA 4.0",
                "caption": "El palacio de justicia de Dosso.",
            },
        ],
    ),
    dict(
        n=18, name="Koutoukalé y los rápidos del Níger · el río antes de Niamey", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="medio día",
        lat=13.67138, lon=1.815749,  # Google Maps: Karma
        desc="Aguas arriba de Niamey, en la comuna de Karma, el Níger baja entre bancos de arena y umbrales rocosos que forman rápidos en aguas bajas, con pueblos de pescadores sorko y arrozales en la orilla. Hay varios caseríos llamados Koutoukalé: Koutoukalé Kourtey, Koutoukalé Zéno y Koutoukalé Kado. Advertencia importante: KARMA ALBERGA LA ÚNICA PRISIÓN DE MÁXIMA SEGURIDAD DE NÍGER, la de Koutoukalé, escenario de una fuga en julio de 2024; es zona militarizada donde no se fotografía ni se merodea.",
        dog_note="Ribera con hipopótamos y zona sensible por la prisión: nada de perro suelto.",
        visit={
            "why": "Es el tramo fluvial más bonito cerca de la capital y el más fácil de encajar en media jornada.",
            "see": "Los umbrales y bancos de arena del río en aguas bajas, las piraguas sorko, los arrozales y aves acuáticas.",
            "access": "Región de Tillabéri, comuna rural de Karma, a unos 40-50 km al noroeste de Niamey por la RN1 y desvío de tierra. Aparcamiento informal en la orilla, cabe un par de 4x4. Sin entradas ni horarios. El pin marca el núcleo de Karma; los rápidos y el embarcadero quedan en la ribera, POR CONFIRMAR sobre el terreno. Seguridad: región de Tillabéri, citada por el MAEC (9-02-2026) como zona de amenaza terrorista permanente; además hay presencia militar permanente por la prisión.",
            "when": "De febrero a mayo, con el río bajo y los umbrales al descubierto; al amanecer para las aves.",
            "skip": "Descártalo siempre: es un PDI menor en una comuna militarizada y en la región más peligrosa del país.",
        },
        links=[
            {"label": "Karma, Niger (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Karma,_Niger"},
            {"label": "MAEC · Recomendaciones de viaje a Níger", "url": "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niger_river_in_Niamey.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niger_river_in_Niamey.jpg",
                "credit": "diasUndKompott · CC BY-SA 2.0",
                "caption": "El Níger a su paso por Niamey.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Vue_de_loin_du_village_de_Karma_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Vue_de_loin_du_village_de_Karma_02.jpg",
                "credit": "Barke11 · CC BY-SA 4.0",
                "caption": "El pueblo de Karma, aguas arriba de Niamey.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Niamey,_Niger_River_bank.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Niamey,_Niger_River_bank.jpg",
                "credit": "Roland Hunziker · CC BY-SA 2.0",
                "caption": "Las orillas del Níger.",
            },
        ],
    ),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul", "cultura": "morado",
              "patrimonio unesco": "marron", "costa": "turquesa"}
for _p in POIS:
    # La portada de la tarjeta, el globo del mapa y el modal es siempre la primera foto de la galería.
    _p["img"] = _p["photos"][0]["img"]
    _p["source"] = _p["photos"][0]["source"]
    _p["credit"] = _p["photos"][0]["credit"]
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")

LOGISTICS = [
    ("Aeropuerto Internacional Diori Hamani (NIM/DRRN)", "Frontera", 13.4765568, 2.176969,  # Google Maps: Aeropuerto Internacional Diori Hamani
     "Única puerta de entrada realista al país, a 9 km al sureste de Niamey. Operativo, con controles reforzados a extranjeros. Atacado el 29/01/2026 (Estado Islámico) y el 18/06/2026 (JNIM), y objetivo del intento de golpe del 29/08/2026. Pin comprobado en Google Maps («Aeropuerto Internacional Diori Hamani»)."),
    ("Puesto fronterizo de Assamakka (Argelia)", "Frontera", 19.3339813, 5.7727791,  # Google Maps: Assamakka
     "Único paso oficial Níger-Argelia, 10 km al sur de In Guezzam, en la Transahariana. 400 km a Tamanrasset y 200 km a Arlit por pista. Punto de deportación de migrantes; sin cruces de viajeros registrados en más de una década (Sahara Overland, 07/2026). Pin comprobado en Google Maps («Assamakka»)."),
    ("Paso de Gaya - Malanville (Benín)", "Frontera", 11.8864375, 3.453512,  # Google Maps: Gaya
     "Puente sobre el río Níger entre Gaya (Níger) y Malanville (Benín), a 733 km de Cotonú. CERRADO desde 2023; comunicado conjunto de reapertura el 18/06/2026 y comité de expertos, sin apertura efectiva. Pin comprobado en Google Maps («Gaya»)."),
    ("Embajada de España en Niamey", "Consular", 13.526027, 2.0700927,  # Google Maps: Embajada de España en Niamey
     "Rue AM-5, enfrente de la Embajada de Turquía, Koira Kano (barrio de las Embajadas), Niamey. Tel. +227 20 75 59 61/62/64. EMERGENCIA CONSULAR +227 96 83 83 94. emb.niamey@maec.es · consular emb.niamey.vis@maec.es · citas emb.niamey.cita@maec.es. Abierta desde 2007 y operativa en 2026. Pin comprobado en Google Maps («Embajada de España en Niamey»)."),
    ("Embajada de Níger en Bruselas (visados para España)", "Consular", 50.8098948, 4.383583,  # Google Maps: Embajada de Níger en Bruselas
     "Avenue Fr. Roosevelt 78, B-1050 Bruselas. Tel. +32 2 648 61 40 / +32 2 648 59 60. Es donde el MAEC dice que los españoles deben solicitar el visado. Pin comprobado en Google Maps («Embajada de Níger en Bruselas»)."),
    ("Hôpital National de Niamey", "Hospital", 13.5128832, 2.1011553,  # Google Maps: National Hospital of Niamey
     "Mayor hospital de referencia del país según Wikipedia («the country's largest referral hospital»). POR CONFIRMAR capacidad actual y si la Embajada de España lo recomienda. Pin comprobado en Google Maps («National Hospital of Niamey»)."),
    ("Hôpital Central et maternité de Niamey", "Hospital", 13.5861305, 2.0918857,  # Google Maps: Hôpital Général de Référence de Niamey
     "Hospital central y maternidad construidos en los años cuarenta (Wikipedia). POR CONFIRMAR ubicación exacta y servicios. El MAEC advierte de que las condiciones sanitarias son muy precarias fuera de Niamey y todo caso grave exige evacuación internacional. Pin comprobado en Google Maps («Hôpital Général de Référence de Niamey»)."),
    ("Eje de repostaje Niamey - Dosso - Birni N'Konni", "Combustible", 13.0504833, 3.2080991,  # Google Maps: Dosso
     "Dosso, nudo comercial entre Niamey y el este del país y hacia Benín, a 130-140 km al sureste de la capital (Wikipedia). Gasolina 499 FCFA/l (GlobalPetrolPrices, 08/12/2025); precios de calle de 600 FCFA el gasóleo y 636 la gasolina (Sahara Overland, 07/2026). Pin comprobado en Google Maps («Dosso»)."),
    ("Agadez, última base logística hacia el norte", "Agua potable", 16.9741689, 7.986535,  # Google Maps: Agadez
     "Última base logística antes del Aïr y el Ténéré y sede de los operadores que gestionan permisos y escolta. Quinta ciudad del país (110.497 hab., censo de 2012). El norte de Agadez está señalado por EEUU como zona de máximo riesgo. Acceso vetado sin escolta militar. Pin comprobado en Google Maps («Agadez»)."),
    ("Niamey, punto de carga de agua", "Agua potable", 13.5115963, 2.1253854,  # Google Maps: Niamey
     "Única red urbana con garantías relativas. Toda el agua de boca debe filtrarse y potabilizarse: el MAEC prohíbe beber agua no embotellada. No vadear ni bañarse en el río Níger por esquistosomiasis (TravelHealthPro). Pin comprobado en Google Maps («Niamey»)."),
]

DRONE_CALLOUT = ("danger", "NO METAS UN DRON EN NÍGER",
                 "Sobre el papel el dron es legal: la ANAC lo regula, exige identificación y número asignado, y limita a 90 metros, vuelo diurno y contacto visual. En la práctica gobierna una junta en guerra: el 8 de marzo de 2026 el ejército repelió un ataque contra la base de drones del aeropuerto de Tahoua y el de Niamey fue atacado dos veces ese año. Llegar con un dron a un control reforzado, donde el FCDO documenta pasaportes retenidos durante días, es pedir una incautación en el mejor caso y una detención por espionaje en el peor.")

STARLINK_CALLOUT = ("warn", "STARLINK FUNCIONA, PERO NO ES UN SALVOCONDUCTO",
                    "Starlink se activó en Níger el 13 de marzo de 2025 con una licencia de cinco años otorgada por el Gobierno militar y tramitada ante la ARCEP nigerina; fue el país africano número 18 en tener servicio. Que exista cobertura legal no cambia nada del fondo: sigue habiendo escolta militar obligatoria fuera de Niamey, riesgo de secuestro en todo el país y controles reforzados en frontera. Un terminal Starlink en el equipaje de un extranjero es, además, material de comunicaciones que puede dar pie a preguntas incómodas en un control militar.")

DOG_MATRIX = [
    ("Niamey (capital)", "no recomendado", "Si el viaje fuese aparte y en avión, el perro se queda en España con cuidador. No hay clínica veterinaria verificada en esta sesión."),
    ("Tillabéri y frontera con Mali/Burkina", "prohibido", "Zona de operaciones yihadistas y de las tres fronteras. Ni con perro ni sin él. Sin plan B."),
    ("Diffa y cuenca del lago Chad", "prohibido", "Amenaza permanente de Boko Haram/ISWAP según el MAEC. Sin plan B."),
    ("Agadez, Aïr y Ténéré", "prohibido", "Acceso solo con permiso, guía y escolta militar de pago; los convoyes no admiten animales y el calor supera los 45 °C de media en junio. Sin plan B."),
    ("Pasos fronterizos terrestres", "por confirmar", "Ningún puesto nigerino verificado publica procedimiento para animales de compañía. Asumir que no está resuelto y no presentarse con el perro."),
    ("Regreso a la UE desde Níger", "permitido con condiciones", "Solo con la titulación de anticuerpos antirrábicos hecha y anotada en el pasaporte ANTES de salir de la UE: Níger no está en los anexos del Reglamento de Ejecución (UE) 2026/636, así que no hay vía simplificada."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Níger (Ministerio de Asuntos Exteriores, UE y Cooperación, consultado 18/09/2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=N%C3%ADger"),
    ("Embajada de España en Niamey · datos de contacto y emergencia consular (MAEC, consultado 18/09/2026)", "https://www.exteriores.gob.es/Embajadas/niamey/es/Paginas/index.aspx"),
    ("Foreign travel advice: Niger (FCDO, Reino Unido, consultado 18/09/2026)", "https://www.gov.uk/foreign-travel-advice/niger"),
    ("Foreign travel advice: Niger — Entry requirements (FCDO, consultado 18/09/2026)", "https://www.gov.uk/foreign-travel-advice/niger/entry-requirements"),
    ("Foreign travel advice: Niger — Regional risks (FCDO, consultado 18/09/2026)", "https://www.gov.uk/foreign-travel-advice/niger/regional-risks"),
    ("Niger — country health information (TravelHealthPro / NaTHNaC, actualizado agosto de 2026)", "https://travelhealthpro.org.uk/country/164/niger"),
    ("Niger (Sahara Overland, Chris Scott, revisión de julio de 2026)", "https://sahara-overland.com/niger-2/"),
    ("Travel in Niger. Security Situation and Updates (Niger Travel and Tours, Agadez, noviembre de 2018)", "https://nigertravelandtours.com/travel-niger/"),
    ("2026 in Niger (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/2026_in_Niger"),
    ("Benin–Niger crisis (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/Benin%E2%80%93Niger_crisis"),
    ("Benin and Niger formalise commitment to reopening shared border (Africanews, 18 de junio de 2026)", "https://www.africanews.com/2026/06/18/benin-and-niger-formalise-commitment-to-reopening-shared-border/"),
    ("Nigeria Re-Opens Border with Neighboring Niger (VOA Africa, marzo de 2024)", "https://www.voaafrica.com/a/nigeria-re-opens-border-with-neighboring-niger/7527572.html"),
    ("Assamakka (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/Assamakka"),
    ("Diori Hamani International Airport (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/Diori_Hamani_International_Airport"),
    ("Gaya, Niger (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/Gaya,_Niger"),
    ("Tree of Ténéré (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/Tree_of_T%C3%A9n%C3%A9r%C3%A9"),
    ("Niger Drone Laws 2026 (Drone-Laws.com, actualizado 2026)", "https://drone-laws.com/drone-laws-in-niger/"),
    ("Starlink Goes Live in Niger, Expanding African Footprint (Space in Africa, 13 de marzo de 2025)", "https://spaceinafrica.com/2025/03/13/starlink-goes-live-in-niger-expanding-african-footprint/"),
    ("Niger gasoline prices (GlobalPetrolPrices.com, dato de 8 de diciembre de 2025)", "https://www.globalpetrolprices.com/Niger/gasoline_prices/"),
    ("Niger — formalités d'entrée pour les animaux de compagnie (AniVetVoyage, consultado 18/09/2026)", "https://anivetvoyage.com/pays/niger/"),
    ("More than 34,000 deportations consolidate the Algeria–Niger border as one of Africa's deadliest migration routes (Atalayar, 27 de enero de 2026)", "https://www.atalayar.com/en/articulo/politics/more-than-34000-deportations-consolidate-the-algeria-niger-border-one-of-africas-deadliest-migration-routes/20260127155611222860.html"),
    ("Niger Travel Advisory — Level 4: Do Not Travel (Departamento de Estado de EEUU, 9 de julio de 2026)", "https://travel.state.gov/en/international-travel/travel-advisories/niger.html"),
    ("MAEC · Ficha País Níger (Oficina de Información Diplomática, septiembre de 2025, PDF)", "https://www.exteriores.gob.es/Documents/FichasPais/NIGER_FICHA%20PAIS.pdf"),
    ("Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026, listas de terceros países para desplazamientos sin ánimo comercial de animales de compañía (BOE/DOUE)", "https://www.boe.es/buscar/doc.php?id=DOUE-L-2026-80458"),
    ("Reglamento Delegado (UE) 2026/131 de la Comisión, de 20 de enero de 2026 (EUR-Lex, PDF)", "https://eur-lex.europa.eu/legal-content/ES/TXT/PDF/?uri=OJ%3AL_202600131"),
    ("List of emergency telephone numbers — Niger (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/List_of_emergency_telephone_numbers"),
    ("Air and Ténéré Natural Reserves — World Heritage in Danger (UNESCO World Heritage Centre, consultado 18/09/2026)", "https://whc.unesco.org/en/list/573/"),
    ("Buying a SIM Card in Niger Guide (Phone Travel Wiz, guía 2025)", "https://www.phonetravelwiz.com/buying-a-sim-card-in-niger-guide/"),
    ("Exteriores reorganiza la Embajada en Níger en plena investigación sobre una presunta trama de visados (The Objective, 14 de julio de 2026)", "https://theobjective.com/espana/2026-07-14/exteriores-embajada-niger-investigacion-visados/"),
    ("Agadez (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/Agadez"),
    ("Dosso, Niger (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/Dosso,_Niger"),
    ("Niamey (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/Niamey"),
    ("Malanville (Wikipedia, consultado 18/09/2026)", "https://en.wikipedia.org/wiki/Malanville"),
    ("Musée National Boubou Hama (Wikipedia EN)", "https://en.wikipedia.org/wiki/Niger_National_Museum"),
    ("MAEC · Recomendaciones de viaje a Níger", "https://www.exteriores.gob.es/Embajadas/niamey/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"),
    ("UNESCO · Complexe W-Arly-Pendjari (ficha 749)", "https://whc.unesco.org/en/list/749"),
    ("W National Park (Wikipedia EN)", "https://en.wikipedia.org/wiki/W_National_Park"),
    ("Kouré, Niger (Wikipedia EN)", "https://en.wikipedia.org/wiki/Kour%C3%A9,_Niger"),
    ("Jirafa de África Occidental (Wikipedia EN)", "https://en.wikipedia.org/wiki/West_African_giraffe"),
    ("Kouré (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Kour%C3%A9"),
    ("Ayorou (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ayourou"),
    ("UNESCO · Historic Centre of Agadez (ficha 1268)", "https://whc.unesco.org/en/list/1268"),
    ("Sahara Overland · rutas transaharianas", "https://sahara-overland.com/routes/"),
    ("UNESCO · Air and Ténéré Natural Reserves (ficha 573)", "https://whc.unesco.org/en/list/573"),
    ("Timia (Wikipedia EN)", "https://en.wikipedia.org/wiki/Timia"),
    ("Arbre du Ténéré (Wikipedia EN)", "https://en.wikipedia.org/wiki/Arbre_du_T%C3%A9n%C3%A9r%C3%A9"),
    ("Bilma (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bilma"),
    ("Elrhaz Formation / Gadoufaoua (Wikipedia EN)", "https://en.wikipedia.org/wiki/Gadoufaoua"),
    ("In-Gall (Wikipedia EN)", "https://en.wikipedia.org/wiki/In-Gall"),
    ("Zinder (Wikipedia EN)", "https://en.wikipedia.org/wiki/Zinder"),
    ("Maradi (Wikipedia EN)", "https://en.wikipedia.org/wiki/Maradi,_Niger"),
    ("Tahoua (Wikipedia EN)", "https://en.wikipedia.org/wiki/Tahoua"),
    ("Dogondoutchi (Wikipedia EN)", "https://en.wikipedia.org/wiki/Dogondoutchi"),
    ("Macizo de Termit (Wikipedia EN)", "https://en.wikipedia.org/wiki/Termit_Massif"),
    ("Tillabéri (Wikipedia EN)", "https://en.wikipedia.org/wiki/Tillab%C3%A9ri"),
    ("Reserva Parcial de Fauna de Dosso (Wikipedia EN)", "https://en.wikipedia.org/wiki/Dosso_Reserve"),
    ("Karma, Niger (Wikipedia EN)", "https://en.wikipedia.org/wiki/Karma,_Niger"),
]

# Bucle oeste-este: Niamey · Dosso · Dogondoutchi · Maradi · Zinder (hipotético)
CORRIDOR = [
    (13.51096, 2.10713),
    (13.32536, 2.59164),
    (13.05048, 3.2081),
    (13.64418, 4.03378),
    (13.50098, 7.10364),
    (13.79418, 9.00127),
    (16.04194, 11.345),
    (13.79418, 9.00127),
    (14.89046, 5.258),
    (16.97417, 7.98653),
    (16.78673, 6.93433),
    (18.05576, 8.65612),
    (17.75, 10.06667),
    (18.68667, 12.91917),
    (16.83333, 9.41667),
    (16.97417, 7.98653),
    (14.89046, 5.258),
    (13.51096, 2.10713),
]

# Ramal fluvial noroeste: Niamey · Karma · Tillabéri · Ayorou y bajada al Parque W (hipotético)
CORRIDOR_ALT = [
    (13.51096, 2.10713),
    (13.67138, 1.81575),
    (14.20611, 1.45797),
    (14.73281, 0.91043),
    (14.20611, 1.45797),
    (13.51096, 2.10713),
    (12.52528, 2.66333),
    (13.05048, 3.2081),
]

HISTORIA_RESUMEN = "Níger es un país sin salida al mar, dos tercios de desierto, tendido sobre el corredor donde el Sáhara se encuentra con el Sahel. Por su territorio pasaron el imperio songhai, Kanem-Bornu, las ciudades hausa y el sultanato de Agadez antes de que Francia lo convirtiera en territorio militar en 1900 y en colonia en 1922. Independiente el 3 de agosto de 1960, alternó regímenes militares y civiles, vivió dos rebeliones tuareg y alcanzó una democracia electoral entre 2011 y 2023. El golpe del 26 de julio de 2023 la interrumpió: gobierna la junta del CNSP, el país abandonó la CEDEAO y rompió con Francia y con Estados Unidos. El uranio de Arlit sigue siendo su mayor baza y su mayor disputa."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>El territorio del actual Níger nunca fue una unidad política antes de la colonización, sino un corredor de paso entre el Sáhara y el Sahel recorrido por caravanas, pastores y ejércitos. Según la historia de Níger recogida en Wikipedia, el <strong>imperio songhai</strong>, expandido desde comienzos del siglo XIV con centro en Gao, controló el oeste del país hasta su hundimiento en 1591, mientras el <strong>imperio de Kanem-Bornu</strong> dominó la cuenca del lago Chad entre los siglos X y XVII por el este.</p><p>En el centro y el sur florecieron desde el siglo X las <strong>ciudades-estado hausa</strong>, independientes entre sí, comerciantes y densamente pobladas; de ellas viene el peso demográfico y lingüístico que el hausa conserva hoy. En el norte, las federaciones tuareg del Aïr se organizaron a partir del siglo XII alrededor de <strong>Agadez</strong>, cuyo sultanato fue la bisagra entre las rutas transaharianas de la sal, el oro y los esclavos y los mercados del Sahel. La UNESCO inscribió en 2013 el centro histórico de Agadez en la Lista del Patrimonio Mundial precisamente por ese papel de encrucijada comercial y religiosa, con su mezquita de adobe y su minarete de tierra. El desierto del Ténéré, al este, quedó siempre al margen de cualquier administración: territorio de nómadas y de pozos contados.</p>"),
    ("Colonización",
     "<p>Francia llegó tarde y por la fuerza. La <strong>expedición Voulet-Chanoine</strong>, que atravesó el sur del país entre 1898 y 1899 camino del lago Chad, dejó un rastro de aldeas arrasadas que sigue siendo el episodio más recordado de la conquista. En <strong>1900</strong> el territorio quedó convertido en zona militar y sólo en <strong>1922</strong> se formalizó como colonia integrada en el África Occidental Francesa, con Niamey como capital administrativa.</p><p>La resistencia no fue menor. Entre 1916 y 1917 la revuelta tuareg encabezada por Kaocen puso Agadez bajo asedio, y su aplastamiento sirvió a Francia para consolidar el control del norte. La administración colonial gobernó con pocos funcionarios y menos inversión: trazó fronteras rectas sobre el desierto, impuso cultivos comerciales y trabajo forzado en el sur agrícola y dejó el Aïr y el Ténéré como una periferia militar sin escuelas ni caminos. Entre 1944 y 1958 las reformas de posguerra abrieron paso a una autonomía gradual dentro de la Comunidad Francesa. Lo que Níger heredó al independizarse fue un Estado enorme y vacío, con el <em>francés</em> instalado como lengua de la administración —así lo sigue describiendo la ficha país del Ministerio de Asuntos Exteriores español— y una economía de subsistencia que no había cambiado.</p>"),
    ("Independencia y construcción del Estado",
     "<p>Níger accedió a la independencia el <strong>3 de agosto de 1960</strong> con Hamani Diori como primer presidente. Su gobierno, de partido único y muy apoyado en París, cayó el <strong>15 de abril de 1974</strong> en un golpe militar dirigido por Seyni Kountché, en plena sequía saheliana. El régimen militar duró quince años y coincidió con el auge del uranio: la mina de <strong>Arlit</strong>, en producción comercial desde 1971 según la World Nuclear Association, pagó carreteras, funcionarios y ciudades nuevas mientras el precio se mantuvo alto, y arrastró al país cuando se hundió.</p><p>A Kountché le sucedió Ali Saibou, que abrió una transición pactada. Una conferencia nacional dio paso a elecciones y <strong>Mahamane Ousmane</strong> inauguró en 1993 el primer gobierno civil elegido. La experiencia duró poco: el <strong>26 de enero de 1996</strong> el coronel Ibrahim Baré Maïnassara tomó el poder y fue asesinado en <strong>1999</strong>, tras lo cual Mamadou Tandja abrió un nuevo ciclo civil. En paralelo, entre <strong>1990 y 1995</strong> el norte vivió la <em>primera rebelión tuareg</em>, alimentada por el agravio de que el uranio saliera del Aïr sin dejar nada en él; se cerró con acuerdos de paz, integración de combatientes y promesas de descentralización que se cumplieron a medias.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>Tandja gobernó una década y cayó en 2010 tras forzar un referéndum para prolongar su mandato. Entremedias, entre <strong>2007 y 2009</strong> estalló la <em>segunda rebelión tuareg</em>, liderada por el Movimiento de los Nigerinos por la Justicia, que volvió a cerrar el acceso al Aïr y al Ténéré y acabó con el turismo sahariano que había sido la gran fuente de divisas de Agadez.</p><p>La década siguiente fue la más estable de su historia. Mahamadou Issoufou ganó las elecciones de <strong>2011</strong> y repitió en <strong>2016</strong>; Mohamed Bazoum le sucedió tras las presidenciales de <strong>2020-2021</strong>, que Freedom House describe como el primer traspaso de poder entre presidentes elegidos democráticamente del país. Fue también la década en que el yihadismo se instaló: el Estado Islámico en el Gran Sáhara en la zona de las tres fronteras de <strong>Tillabéri</strong> y Boko Haram con su escisión ISWAP en <strong>Diffa</strong>.</p><p>El <strong>26 de julio de 2023</strong> la guardia presidencial detuvo a Bazoum y el general <strong>Abdourahamane Tiani</strong> se proclamó el 28 de julio jefe del Consejo Nacional para la Salvaguarda de la Patria (CNSP). La CEDEAO dio un ultimátum el 30 de julio, impuso cierre de fronteras, zona de exclusión aérea y congelación de activos, y llegó a amenazar con intervenir. Níger respondió alineándose con Mali y Burkina Faso.</p>"),
    ("Política y gobierno en 2026",
     "<p>A fecha de septiembre de 2026, Níger es en la práctica una <strong>dictadura militar</strong>. El general <strong>Abdourahamane Tiani</strong>, que mandaba la guardia presidencial desde 2011, encabeza el CNSP desde el 28 de julio de 2023 y juró como presidente de la República el <strong>26 de marzo de 2025</strong>, al amparo de una Carta de la Refundación que fija una transición de <em>cinco años prorrogables</em>; el primer ministro es Ali Lamine Zeine. No hay elecciones convocadas. La ficha país del Ministerio de Asuntos Exteriores español, de septiembre de 2025, resume que el sistema concentra los poderes legislativo, ejecutivo y judicial en el general Tiani.</p><p>Freedom House clasifica al país como «Not Free» con <strong>30 puntos sobre 100</strong> en su informe de 2025 —5 sobre 40 en derechos políticos y 25 sobre 60 en libertades civiles— Reporteros Sin Fronteras lo sitúa en el puesto 120 de 180 en 2026. Human Rights Watch documenta que Bazoum sigue detenido desde julio de 2023 y que en 2025 hubo matanzas yihadistas en mezquitas de Tillabéri.</p><p>Níger expulsó a las tropas francesas en 2023, recuperó la base estadounidense de drones de <strong>Agadez</strong> el 6 de agosto de 2024 y salió de la <strong>CEDEAO</strong> el 29 de enero de 2025, tras unas sanciones impuestas en 2023 y levantadas el 24 de febrero de 2024. El MAEC desaconseja absolutamente viajar a todo el país.</p>"),
    ("Economía y recursos",
     "<p>Níger es uno de los países más pobres del mundo. Según la ficha del Ministerio de Asuntos Exteriores español de septiembre de 2025, con datos del FMI para 2025, el PIB ronda los <strong>21.900 millones de dólares</strong> y el PIB per cápita los <strong>750 dólares</strong>, con un crecimiento del 6,6 % y una deuda pública del 43,4 %. La moneda es el <strong>franco CFA</strong>. La agricultura de subsistencia y la ganadería ocupan al 87 % de la población activa; la ayuda internacional sigue siendo estructural.</p><p>El uranio es la seña de identidad económica del país. La mina de <strong>Arlit</strong> produce desde 1971 y sitúa a Níger como noveno productor histórico mundial con 158.889 toneladas acumuladas hasta 2024, aunque su producción ha caído a 962 toneladas en 2024 frente a las 2.020 de 2022, según la World Nuclear Association; la mina subterránea de Akouta cerró en marzo de 2021. El <strong>19 de junio de 2025</strong> el gobierno <em>nacionalizó SOMAÏR</em>, la sociedad de Arlit en la que el francés Orano tenía el 63 %, acusándole de haberse quedado el 86,3 % de la producción desde 1971: es el símbolo económico de la ruptura con París. El otro pilar es el petróleo de <strong>Agadem</strong>, explotado por la china CNPC, con refinería en Zinder y un oleoducto de unos 2.000 kilómetros hasta la costa de Benín.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Níger tiene unos <strong>27 millones de habitantes</strong> según el MAEC (2024), sobre 1.266.491 kilómetros cuadrados, dos tercios desierto. La fecundidad es de 6,7 hijos por mujer y el analfabetismo, del 69 %. Los grupos de población, según el censo de 2001: hausa (55,4 %), zarma y songhay (21 %), tuareg (9,3 %), peul (8,5 %) y kanuri (4,7 %). El 99,3 % era musulmán en el censo de 2012, frente a un 0,3 % de cristianos.</p><p>El <strong>francés</strong> sigue siendo la lengua de la administración y la que abre puertas por carretera; la Carta de la Refundación de 2025 elevó el <strong>hausa</strong> a lengua oficial. Hay diez lenguas nacionales reconocidas, entre ellas fulfuldé, kanuri, tamasheq y zarma. Tiene tres bienes del Patrimonio Mundial: las reservas del Aïr y el Ténéré (1991), en la Lista de Patrimonio en Peligro desde 1992, el complejo W-Arly-Pendjari y el centro histórico de Agadez (2013). El <em>árbol del Ténéré</em>, símbolo del desierto, fue derribado en 1973 y sus restos se conservan en el Museo Nacional de Niamey.</p><p>Conviene vestir discreto, con hombros y rodillas cubiertos también ellos, y pedir permiso antes de fotografiar; fotografiar militares o edificios oficiales está prohibido. En <strong>ramadán</strong>, que en 2027 empieza en torno al 8 de febrero, no se come, bebe ni fuma en público durante el día. El alcohol es marginal fuera de los hoteles de Niamey.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Níger (MAEC España · PDF · septiembre de 2025)", "https://www.exteriores.gob.es/Documents/FichasPais/NIGER_FICHA%20PAIS.pdf"),
    ("Recomendaciones de viaje: Níger (MAEC España · actualizado 9 de febrero de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=N%C3%ADger"),
    ("Niger: Freedom in the World 2025 (Freedom House · 2025)", "https://freedomhouse.org/country/niger/freedom-world/2025"),
    ("Niger — History (Encyclopædia Britannica · consultada en septiembre de 2026)", "https://www.britannica.com/place/Niger/History"),
    ("Niger — States Parties (UNESCO Centro del Patrimonio Mundial · 2026)", "https://whc.unesco.org/en/statesparties/ne"),
    ("Air and Ténéré Natural Reserves (UNESCO Centro del Patrimonio Mundial · ficha 573)", "https://whc.unesco.org/en/list/573"),
    ("Historia de Níger (Wikipedia en español · consultada en septiembre de 2026)", "https://es.wikipedia.org/wiki/Historia_de_N%C3%ADger"),
    ("Níger (Wikipedia en español · consultada en septiembre de 2026)", "https://es.wikipedia.org/wiki/N%C3%ADger"),
    ("Niger (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/Niger"),
    ("Economy of Niger (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/Economy_of_Niger"),
    ("2023 Nigerien coup d'état (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/2023_Nigerien_coup_d%27%C3%A9tat"),
    ("Alliance of Sahel States (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/Alliance_of_Sahel_States"),
    ("Abdourahamane Tiani (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/Abdourahamane_Tiani"),
    ("Nigerien Air Base 201, Agadez (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/Nigerien_Air_Base_201"),
    ("Tree of Ténéré (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/Tree_of_T%C3%A9n%C3%A9r%C3%A9"),
    ("Niger (Reporteros Sin Fronteras · índice de libertad de prensa 2026)", "https://rsf.org/en/country/niger"),
    ("Niger — World Report 2026 (Human Rights Watch · 2026)", "https://www.hrw.org/world-report/2026/country-chapters/niger"),
    ("Uranium in Niger (World Nuclear Association · actualizado 2026)", "https://world-nuclear.org/information-library/country-profiles/countries-g-n/niger"),
    ("Niger nationalises uranium mine as spat with French nuclear giant worsens (Al Jazeera · 20 de junio de 2025)", "https://www.aljazeera.com/amp/news/2025/6/20/niger-nationalises-uranium-mine-as-spat-with-french-nuclear-giant-worsens"),
    ("ECOWAS Lifts Some Sanctions on Niger Imposed After 2023 Military Coup (VOA Africa · 24 de febrero de 2024)", "https://www.voaafrica.com/a/ecowas-lifts-sanctions-on-niger-imposed-after-2023-military-coup/7501207.html"),
]

SPEC = dict(
    slug="niger", name="Níger", revision="18 sep 2026",
    sub="EXCLUIDO POR PROTOCOLO — junta militar, yihadismo activo y escolta militar obligatoria fuera de Niamey · ficha informativa",
    chips=[
        ("ESTATUS", "EXCLUIDO POR PROTOCOLO. MAEC: «SE DESACONSEJA ABSOLUTAMENTE VIAJAR A NÍGER»…"),
        ("CÓMO LLEGAR", "Solo en avión, al Aeropuerto Internacional Diori Hamani de Niamey (NIM/DRRN)…"),
        ("VISADO", "OBLIGATORIO Y PRESENCIAL. Níger no tiene embajada en Madrid: el MAEC remite a la Embajada…"),
        ("VEHÍCULO", "Históricamente laissez-passer local en lugar de CPD (Sahara Overland)…"),
        ("SEGURIDAD", "MAEC y EEUU nivel máximo · secuestro de extranjeros"),
        ("SEGURO", "Carta Verde no cubre · sin cobertura con aviso MAEC"),
        ("SALUD", "Fiebre amarilla OBLIGATORIA · malaria alto riesgo"),
        ("DRONES", "Legal con ANAC, suicida en la práctica: no llevar"),
        ("STARLINK", "Operativo desde el 13/03/2025 · licencia 5 años"),
        ("4x4", "Inviable: escolta militar obligatoria fuera de Niamey"),
        ("A PIE", "No: el MAEC desaconseja caminar por Niamey"),
        ("PERRO", "Entrada con microchip, rabia de más de 1 mes y menos de 1 año y certificado sanitario internacional de menos…"),
        ("MONEDA", "Franco CFA de África Occidental (XOF), paridad fija 1 EUR = 655,957 FCFA (MAEC)…"),
        ("VENTANA", "Desértico y saheliano. En Assamakka, en la frontera argelina…"),
    ],
    center=[15.52, 6.91], zoom=5,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle oeste-este: Niamey · Dosso · Dogondoutchi · Maradi · Zinder (hipotético)",
    corridor_alt_label="Ramal fluvial noroeste: Niamey · Karma · Tillabéri · Ayorou y bajada al Parque W (hipotético)",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/1997_277-9A_Agadez_mosque_cropped.jpg?width=1200",
    hero_credit="Agadez · Dan Lundberg · CC BY-SA 2.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Níger queda fuera de la ruta de 2027 y no se plantea ni como tramo alternativo ni como desvío corto. El MAEC desaconseja absolutamente viajar a todo el país y el FCDO británico mantiene «advise against all travel»; ese doble aviso, por sí solo, deja el viaje sin cobertura de seguro y convierte cualquier incidente en un problema sin red. Sobre eso se acumula lo operativo: fuera de Niamey la escolta de las fuerzas de seguridad nigerinas es obligatoria según el FCDO, los convoyes privados de seguridad que citaba Niger Travel and Tours ya en 2018 partían de 4.000 dólares por cinco a siete días alrededor de Agadez, y en 2026 el aeropuerto de Niamey fue atacado en enero y en junio y fue escenario del intento de golpe del 29 de agosto. La frontera con Benín, la puerta natural desde Cotonú, sigue cerrada desde 2023 pese al compromiso de reapertura firmado en junio de 2026. Si algún día fuera viable, no sería una etapa de la vuelta sino un viaje aparte: vuelo a Niamey, operador local, permisos y escolta contratados con antelación, y un presupuesto que con escolta militar y guía se va con facilidad por encima de 5.000–8.000 euros por persona para diez días, sin contar el seguro de riesgo de guerra. Lo que habría que decidir entonces es sencillo: si el objetivo es el Aïr y el Ténéré, se va en avión y con operador; los vehículos propios no entran en esa ecuación.",
    facts=[
        ("Estatus", "EXCLUIDO POR PROTOCOLO. MAEC: «SE DESACONSEJA ABSOLUTAMENTE VIAJAR A NÍGER». FCDO: «advises against all travel to Niger» (todo el país)."),
        ("Cómo llegar", "Solo en avión, al Aeropuerto Internacional Diori Hamani de Niamey (NIM/DRRN). Operan Air Algérie, Ethiopian, Turkish, Royal Air Maroc, ASKY, Air France y otras."),
        ("Visado", "OBLIGATORIO Y PRESENCIAL. Níger no tiene embajada en Madrid: el MAEC remite a la Embajada de Níger en BRUSELAS. No se expide visado en aeropuerto ni en frontera terrestre."),
        ("Vehículo/aduana", "Históricamente laissez-passer local en lugar de CPD (Sahara Overland). Con el país excluido y la escolta obligatoria, la entrada con vehículo propio matriculado en España es inviable en la práctica."),
        ("Seguro", "Carta Verde NO cubre Níger. El seguro regional es la Carte Brune de la CEDEAO, pero Níger salió de la CEDEAO junto a Mali y Burkina Faso: su validez futura está POR CONFIRMAR."),
        ("Moneda", "Franco CFA de África Occidental (XOF), paridad fija 1 EUR = 655,957 FCFA (MAEC). País de efectivo: cajeros escasos y tarjetas de aceptación muy limitada (FCDO)."),
        ("Perro", "Entrada con microchip, rabia de más de 1 mes y menos de 1 año y certificado sanitario internacional de menos de 10 días (AniVetVoyage). Sin web oficial nigerina localizable: POR CONFIRMAR."),
        ("Drones", "Permitidos sobre el papel bajo reglamento de la ANAC (registro e identificación previos), pero con junta militar, ataques a bases de drones y controles reforzados el riesgo real de confiscación y detención es máximo."),
        ("Starlink", "OPERATIVO. Licencia de cinco años del Gobierno nigerino y activación el 13 de marzo de 2025 (ARCEP Níger). Níger fue el país africano número 18 con servicio."),
        ("Seguridad", "Terrorismo y secuestro en todo el país, Niamey incluida. EEUU: Nivel 4 «Do not travel» (09/07/2026) y «foreigners traveling beyond Niamey must request a military escort from the Nigerien police». Estado de emergencia vigente en varias regiones."),
        ("Clima", "Desértico y saheliano. En Assamakka, en la frontera argelina, las máximas superan los 40 °C de finales de abril a octubre y la media de junio pasa de 45 °C a la sombra (Wikipedia)."),
        ("Sanidad", "Fiebre amarilla OBLIGATORIA desde los 9 meses (TravelHealthPro). Malaria de alto riesgo en todo el país. Brote de poliovirus derivado de vacuna cVDPV3 activo en agosto de 2026. Sanidad muy precaria fuera de Niamey."),
        ("Conectividad móvil", "Airtel es el único operador con 4G/LTE y la mejor cobertura; también Orange, Moov y SahelCom (residual). Registro de SIM OBLIGATORIO al comprarla (Phone Travel Wiz)."),
        ("Aïr y Ténéré", "Reservas Naturales inscritas por la UNESCO en 1991 y en la Lista del Patrimonio Mundial EN PELIGRO desde 1992, sin interrupción. 7.736.000 ha. No hay vía legal de acceso practicable hoy."),
    ],
    alerts=[
        "El MAEC desaconseja absolutamente viajar a Níger: no hay lectura amable de esa frase, es el nivel máximo de su escala y anula de hecho cualquier seguro de viaje convencional.",
        "Tras el secuestro de un ciudadano estadounidense en octubre de 2025, el MAEC elevó a MUY ELEVADO el riesgo en la propia capital y recomienda no caminar por Niamey ni moverse tras la puesta de sol.",
        "El FCDO es explícito: fuera de Niamey hay que ir escoltado por las fuerzas de seguridad y el ejército nigerinos. No es una recomendación, es la condición de movimiento.",
        "Estados Unidos mantiene Níger en Nivel 4 «Do not travel» desde el 9 de julio de 2026 por terrorismo, secuestro, crimen, disturbios y sanidad, y obliga a su personal a moverse en vehículos blindados y respetar un toque de queda.",
        "El aeropuerto Diori Hamani de Niamey fue atacado por el Estado Islámico el 29 de enero de 2026 y por el JNIM el 18 de junio de 2026, y el 29 de agosto de 2026 fue uno de los objetivos de un intento de golpe.",
        "La frontera con Benín —la vía natural desde el puerto de Cotonú, por donde pasaba el 80 % de las importaciones de Níger— sigue cerrada desde 2023 pese al comunicado conjunto de reapertura de junio de 2026.",
        "Níger salió de la CEDEAO junto a Mali y Burkina Faso: el paraguas del seguro regional Carte Brune y los acuerdos de libre circulación de la CEDEAO quedan en el aire.",
        "El MAEC prohíbe de hecho los desplazamientos antes de las 06:00 y después de las 17:00 y desaconseja taxis colectivos, autobuses y conducción nocturna.",
        "Las autoridades nigerinas han reforzado los controles a extranjeros a la llegada y, según el FCDO, «in some cases, passports have been withheld for several days».",
        "El turismo del Aïr y el Ténéré colapsó hace años: Sahara Overland, en su revisión de julio de 2026, no tiene constancia de ningún cruce desde Argelia «for well over a decade».",
        "El Árbol del Ténéré, el hito que justificaba medio viaje en los años noventa, fue derribado por un camionero libio en 1973: lo que queda allí es una escultura metálica, y el árbol muerto está en el Museo Nacional de Niamey desde el 8 de noviembre de 1973.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Niamey", "Llegada, Museo Nacional Boubou Hama y orilla del Níger", "~0 km · 2 días"),
        ("2 · Niamey → Kouré → Dosso", "RN1 este y sur, jirafas de Kouré y palacio del Zarmakoy", "~200 km · 1 día"),
        ("3 · Dosso → Dogondoutchi", "RN1 hacia el este, Dallol Maouri", "~170 km · 1 día"),
        ("4 · Dogondoutchi → Maradi", "RN1 por Birnin Konni y Madaoua", "~430 km · 2 días"),
        ("5 · Maradi → Zinder", "RN1, país hausa, Birni y palacio del sultán", "~240 km · 1 día"),
        ("6 · Zinder → Gouré → Termit (ida y vuelta)", "Pista al macizo de Termit y Tin Toumma", "~800 km · 4 días"),
        ("7 · Zinder → Tanout → Agadez", "RN11 hacia el norte, entrada en el Sáhara", "~440 km · 2 días"),
        ("8 · Agadez → Timia (Aïr)", "Pista de arena y roca por el macizo del Aïr", "~250 km · 2 días"),
        ("9 · Timia → Arbre du Ténéré", "Navegación GPS por el Ténéré", "~300 km · 2 días"),
        ("10 · Arbre du Ténéré → Bilma", "Pista de la azalai hasta el Kaouar", "~350 km · 2 días"),
        ("11 · Bilma → Gadoufaoua → Agadez", "Regreso por el Ténéré occidental y el yacimiento", "~700 km · 4 días"),
        ("12 · Agadez → In-Gall → Tahoua", "RN25 hacia el suroeste, meseta del Ader", "~500 km · 2 días"),
        ("13 · Tahoua → Niamey", "RN25 y RN1 de vuelta a la capital", "~550 km · 2 días"),
        ("14 · Niamey → Karma → Tillabéri → Ayorou y regreso", "Ramal fluvial del Níger, mercado del domingo", "~420 km · 2 días"),
    ],
    offroad=[
        "La pista Agadez–Bilma, la ruta histórica de la azalai, cruza unos 560 km de Ténéré sin asfalto ni señalización: exige navegación GPS, dos vehículos mínimo y autonomía completa de agua y combustible (fuente: Bilma, Wikipedia EN).",
        "El acceso al macizo del Aïr desde Agadez hacia Timia e Iferouane se hace por pistas de arena y roca dentro de las Reservas Naturales del Aïr y del Ténéré, sitio UNESCO en peligro desde 1992, donde históricamente se ha exigido autorización administrativa y guía local; no hay vía legal de acceso verificada hoy (fuente: UNESCO ficha 573).",
        "Gadoufaoua no tiene pista marcada: se llega navegando sobre reg desde Agadez y el yacimiento se extiende de forma difusa, por lo que el punto GPS es orientativo (fuente: Elrhaz Formation, Wikipedia EN).",
        "Dentro del Parque Nacional de la W, las pistas del sector nigerino que parten de La Tapoa son de tierra y solo practicables en estación seca; el parque tiene 10.000 km² repartidos entre tres países y su uso es de circulación reglada, no de campo a través (fuente: W National Park, Wikipedia EN).",
        "La aproximación al macizo de Termit y al erg de Tin Toumma se hace por pista desde Zinder o Gouré sin puerta ni control formal, dentro de una de las mayores reservas naturales terrestres del mundo, creada en 2012 (fuente: Termit Massif, Wikipedia EN).",
        "ZONAS VETADAS DE FACTO: todo el eje Tillabéri–frontera de Malí y Burkina Faso, la región de Diffa y el norte de Agadez quedan cubiertos por la recomendación del MAEC de 9 de febrero de 2026 de no viajar a Níger bajo ninguna circunstancia, con amenaza terrorista permanente citada en Tillabéri, Tahoua y Diffa.",
        "ACCESO AL NORTE: Sahara Overland documenta que el noreste de Níger exigía escolta militar en convoy y que los convoyes comerciales escoltados salen de Tamanrasset hacia Agadez cada 15 días, pero afirma que NINGÚN TURISTA HA CRUZADO A NÍGER DESDE 2011 y no hay constancia de viajeros admitidos en ellos (fuente: https://sahara-overland.com/routes/).",
        "No se han podido abrir iOverlander ni Tracks4Africa para Níger en esta investigación, de modo que no hay waypoints de pista ni estado de firme verificados; la única referencia overland consultable ha sido Sahara Overland, que remite a su foro para el estado actual (fuente: https://sahara-overland.com/routes/).",
        "AVISOS CRUZADOS: FCDO británico (29-08-2026) desaconseja todo viaje a Níger sin excepción; Canadá (9-09-2026) pide evitar todo viaje y cita Agadez, Arlit, Tahoua, Tillabéri, Zinder, las fronteras con Malí y Burkina Faso y las zonas remotas; MAEC (9-02-2026) desaconseja absolutamente viajar. Los tres coinciden en riesgo alto de secuestro de extranjeros.",
    ],
    senderismo=[
        "Guelta de Timia: caminata corta desde el pueblo hasta la poza de roca que retiene agua todo el año, a unos 3 km, y hasta la cascada estacional que solo corre tras las lluvias de agosto y septiembre (fuente: Timia, Wikipedia EN).",
        "Rastreo de jirafas en Kouré: recorrido a pie de una a dos horas con guía local por la brousse tigrée, sin vallas ni recorrido fijo; el trazado cambia según dónde estén los animales (fuente: Kouré, Wikipedia EN y FR).",
        "Casco histórico de Agadez: paseo urbano por las 77,6 hectáreas inscritas por la UNESCO, del palacio del sultán a la gran mezquita y al barrio de plateros, con subida al minarete de 27 m si el guardián lo autoriza (fuente: UNESCO ficha 1268).",
        "Barrio de Birni en Zinder: circuito a pie por el recinto fortificado de 1736, el palacio del sultán del Damagaram, la mezquita vieja y el Fort Cazemajou (fuente: Zinder, Wikipedia EN).",
        "Cornisas de Dogondoutchi: subida a la colina que da nombre a la ciudad y recorrido por las cornisas de arenisca sobre el Dallol Maouri (fuente: Dogondoutchi, Wikipedia EN).",
        "Palmeral y salinas de Bilma: vuelta a pie por las balsas de evaporación bajo los acantilados del Kaouar, siempre a primera hora por el calor extremo (fuente: Bilma, Wikipedia EN).",
        "Ribera del Níger en Tillabéri y Karma: paseos cortos por la orilla entre arrozales y bancos de arena, con precaución por los hipopótamos (fuente: Tillabéri y Karma, Wikipedia EN).",
        "Cresta de Termit: ascensiones cortas a la cresta de arenisca negra, 180 km de largo, para ver el erg de Tin Toumma; sin sendero marcado y solo con guía (fuente: Termit Massif, Wikipedia EN).",
    ],
    acampada=[
        "No se ha localizado ninguna fuente abierta y verificable sobre campings en funcionamiento en Níger en 2026: toda la información de acampada de esta ficha es ORIENTATIVA y está SIN CONFIRMAR.",
        "iOverlander y Tracks4Africa no se han podido consultar en esta investigación. La única referencia overland abierta, Sahara Overland, sostiene que ningún turista ha cruzado a Níger desde 2011, por lo que no existen reportes recientes de acampada (fuente: https://sahara-overland.com/routes/).",
        "Niamey: la práctica habitual de los viajeros por carretera ha sido dormir en hoteles con patio cerrado y vigilancia en lugar de acampar, dado el nivel de riesgo urbano que señala el MAEC tras el secuestro de octubre de 2025 (POR CONFIRMAR si sigue habiendo campamentos abiertos).",
        "Parque Nacional de la W: el alojamiento clásico del sector nigerino ha sido el campamento de La Tapoa, junto a la puerta del parque; su estado operativo actual está POR CONFIRMAR.",
        "Agadez: la ciudad ha contado con campamentos y hoteles con patio para vehículos, pero no se ha podido verificar ninguno abierto ni su nombre en fuente fiable.",
        "Aïr y Ténéré: la acampada libre en el desierto ha sido siempre la norma en estas rutas, pero se realiza dentro de un sitio UNESCO en peligro y bajo control militar, por lo que hoy no puede considerarse una opción legal verificada (fuente: UNESCO ficha 573).",
        "Bilma: el alojamiento tradicional era la acampada junto al oasis y el palmeral, con permiso de la comunidad; POR CONFIRMAR.",
        "Regla general para esta ficha: mientras el MAEC mantenga la recomendación de no viajar a Níger (actualización de 9 de febrero de 2026), la acampada libre fuera de núcleos urbanos debe darse por descartada en todo el país.",
    ],
    visado=[
        "VISADO OBLIGATORIO para españoles. No hay exención ni visado a la llegada: el MAEC avisa de que NO se expiden visados en aeropuertos ni en fronteras terrestres.",
        "DÓNDE: Níger no tiene embajada en España. El MAEC remite a la EMBAJADA DE NÍGER EN BRUSELAS, Avenue Fr. Roosevelt 78, B-1050 Bruselas, tel. +32 2 648 61 40 / +32 2 648 59 60.",
        "El FCDO remite a los británicos a la embajada nigerina en GINEBRA, y Sahara Overland cita además consulados en Ámsterdam y Bonn: la demarcación varía según el país de residencia, conviene confirmarla antes de enviar nada.",
        "PASAPORTE con validez mínima de SEIS MESES (MAEC) y certificado de vacunación de fiebre amarilla, que se exige en el propio control de entrada.",
        "Plazos y coste vigentes en 2026: POR CONFIRMAR. No se ha podido abrir en esta sesión una tarifa oficial publicada por la embajada de Bruselas; tramitar por correo desde España añade semanas y no hay atajo consular en Madrid.",
        "Aunque se obtenga el visado, no habilita a moverse libremente: fuera de Niamey el FCDO da por obligatoria la escolta militar, y las zonas desérticas exigieron históricamente permiso y guía.",
        "AVISO DE CONTEXTO: en 2026 las autoridades nigerinas investigaban una presunta red de comercialización de visados Schengen y permisos de residencia que salpicó al entorno del Ministro del Interior nigerino (The Objective, 14/07/2026). El clima administrativo alrededor de los visados es, como mínimo, turbio.",
    ],
    fronteras_rows=[
        ("Entrada principal (aérea)", "Aeropuerto Internacional Diori Hamani, Niamey (NIM/DRRN)", "OPERATIVO pero atacado tres veces en 2026 (29 enero, 18 junio, 29 agosto). Controles reforzados a extranjeros; pasaportes retenidos varios días en algunos casos (FCDO, 2026). Única vía realista de entrada."),
        ("Paso terrestre · Benín", "Gaya — Malanville (puente sobre el río Níger)", "CERRADO desde 2023. La CEDEAO levantó las sanciones en febrero de 2024 pero Niamey mantuvo el cierre acusando a Benín de albergar bases francesas. Comunicado conjunto de reapertura en junio de 2026, comité de expertos en marcha, sin apertura efectiva (Africanews, 18/06/2026)."),
        ("Paso terrestre · Nigeria", "Birni N'Konni — Illela y Magaria — Jibiya", "REABIERTOS. Nigeria cerró los 1.600 km de frontera en agosto de 2023 y ordenó reabrir «with effect immediate» tras el levantamiento de sanciones de la CEDEAO, por directiva del presidente Tinubu (VOA Africa, marzo de 2024). Zona de Maradi/Zinder con amenaza terrorista."),
        ("Paso terrestre · Burkina Faso", "Makalondi y Torodi (eje Niamey — Uagadugú)", "Abiertos en teoría entre aliados de la Alianza de Estados del Sahel, pero es la zona más peligrosa del país: el 4 de enero de 2026 fue asesinado el prefecto de Torodi con su familia. POR CONFIRMAR el estado operativo diario."),
        ("Paso terrestre · Mali", "Labbezanga (río Níger, región de Tillabéri)", "Zona de las tres fronteras, epicentro yihadista. El 18 de enero de 2026 murieron al menos 31 personas en Gorouol (Tillabéri). El FCDO sitúa a los terroristas operando en toda la franja fronteriza con Mali. NO TRANSITABLE en la práctica."),
        ("Paso terrestre · Argelia", "Assamakka — In Guezzam (Transahariana)", "Único paso oficial con Argelia, a 10 km al sur de In Guezzam. Funciona como punto de deportación de migrantes desde Argelia, no como frontera turística: Sahara Overland (julio de 2026) no registra ningún cruce de viajeros «for well over a decade»."),
        ("Paso terrestre · Libia", "Toummo (Ténéré del Tafassasset)", "Frontera con Libia en zona de tráfico y grupos armados. El FCDO sitúa a los terroristas operando en las áreas fronterizas con Libia. Sin control estatal fiable; CERRADO a efectos de viaje legal. POR CONFIRMAR estado formal."),
        ("Paso terrestre · Chad", "Bosso (región de Diffa, cuenca del lago Chad)", "Región de Diffa bajo amenaza permanente de Boko Haram/ISWAP según el MAEC. Zona de operaciones militares; NO TRANSITABLE para viajeros. POR CONFIRMAR estado formal del puesto."),
        ("Salida de Niamey por carretera", "Cualquier eje fuera del perímetro urbano", "ESCOLTA MILITAR OBLIGATORIA: «Outside of Niamey you must be escorted by Nigerien security and military forces» (FCDO, 2026). El MAEC añade prohibición práctica de moverse antes de las 06:00 y después de las 17:00."),
    ],
    vehiculos=[
        "Se conduce POR LA DERECHA. Permiso de conducción internacional recomendado junto al español; en Níger no se ha podido confirmar en esta sesión una exigencia formal publicada.",
        "CPD/carnet de passages: la referencia histórica de Sahara Overland es que en Níger el vehículo se movía con un LAISSEZ-PASSER local, no con carnet. No hay confirmación de la práctica aduanera vigente en 2026.",
        "La Carta Verde europea NO cubre Níger: hay que contratar seguro local a la entrada. El instrumento regional es la Carte Brune de la CEDEAO, pero Níger abandonó la CEDEAO con Mali y Burkina Faso y su vigencia para el país está por confirmar.",
        "Los permisos para circular por las zonas desérticas costaban históricamente desde 50 euros diarios con guía obligatorio (Sahara Overland), a lo que hoy se sumaría la escolta.",
        "La escolta militar fuera de Niamey no es opcional (FCDO). Los convoyes privados de seguridad que ofrecía Niger Travel and Tours partían de 4.000 dólares por cinco a siete días alrededor de Agadez, y se pagaban por adelantado.",
        "Dos 4x4 europeos con matrícula española y tres extranjeros son un objetivo de secuestro de manual en un país donde el MAEC señala riesgo muy elevado incluso en la capital: el problema no es el papeleo del vehículo, es el vehículo.",
        "Entrar por tierra desde el sur exigiría cruzar Benín (frontera cerrada) o Nigeria (reabierta, pero por Maradi/Zinder con amenaza terrorista); desde el norte, la Transahariana por Assamakka, sin cruces registrados en más de una década.",
        "Las aduanas nigerinas aplican controles estrictos y exigen declarar toda mercancía gravable o potencialmente prohibida (FCDO): un vehículo de expedición con repuestos, comunicaciones y dron entra de lleno en esa categoría.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autoridad competente: Agence Nationale de l'Aviation Civile (ANAC) de Níger, anac.ne. Ningún dron puede operar sin que la Autoridad lo haya identificado y le haya asignado un número de identificación.",
        "Límites del reglamento ANAC recogidos por drone-laws.com: altura máxima 90 metros, solo vuelo diurno salvo autorización especial, contacto visual permanente y distancias mínimas a aeródromos y zonas sensibles.",
        "El aparato debe llevar visibles el nombre, la dirección y el teléfono del operador. No se exige seguro de responsabilidad civil ni Remote ID para operaciones básicas.",
        "Uso comercial: autorización previa de la ANAC. Uso recreativo: registro, sin licencia de piloto específica.",
        "La norma escrita no describe la realidad: con el país en conflicto, bases de drones militares atacadas y controles reforzados a extranjeros, el riesgo operativo real de llevar un dron es la incautación y la imputación. POR CONFIRMAR si existe alguna prohibición de importación publicada en el BO nigerino.",
        "El aviso de viaje de EEUU (Nivel 4, 09/07/2026) no menciona drones, y tampoco lo hacen el MAEC ni el FCDO: no hay prohibición expresa publicada en fuente consular, pero tampoco respaldo alguno para llevarlo.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "DISPONIBLE. Starlink entró en servicio en Níger el 13 de marzo de 2025 tras una negociación abierta en el cuarto trimestre de 2024 (Space in Africa).",
        "La licencia es de cinco años y la otorgó el Gobierno nigerino; el regulador es la ARCEP (Autorité de Régulation des Communications Électroniques et de la Poste) de Níger.",
        "La penetración de internet en Níger era del 32 % según la propia ARCEP en el momento del lanzamiento: fuera de Niamey la alternativa terrestre es pobre.",
        "Disponibilidad concreta de planes Roam/regional y precios en 2026: POR CONFIRMAR, no se ha podido abrir el mapa de disponibilidad de starlink.com en esta sesión.",
        "Operadores móviles: Airtel Níger es el mayor (en torno al 50 % de cuota) y el ÚNICO con red 4G/LTE; le siguen Orange (licencia 4G en 2020), Moov y SahelCom, esta última de cobertura testimonial (Phone Travel Wiz).",
        "SIM turística: el REGISTRO DE LA SIM ES OBLIGATORIO al comprarla, con documento de identidad. Precios de tarjeta: Airtel 1.000 XOF, Orange 300 XOF, Moov 200 XOF, con saldo inicial incluido. Cobertura sólida solo en el sur y el oeste.",
    ],
    perro_intro=[
        "NO LLEVES AL PERRO. Es un país con escolta militar obligatoria fuera de la capital, restricción de movimientos nocturnos y riesgo de secuestro: no hay escenario en el que el animal esté a salvo ni atendido.",
        "Requisitos de entrada según AniVetVoyage (recopilador francés que cita IATA y PetTravel, no fuente oficial nigerina): identificación electrónica (microchip), vacuna antirrábica de MÁS DE 1 MES Y MENOS DE 1 AÑO y certificado sanitario internacional expedido MENOS DE 10 DÍAS antes de la llegada.",
        "No se ha localizado en esta sesión ninguna página oficial del Ministerio de Agricultura y Ganadería de Níger ni de sus servicios veterinarios que publique estas condiciones: el dato queda como POR CONFIRMAR con la autoridad nigerina o vía la embajada de Bruselas.",
        "Razas prohibidas: POR CONFIRMAR. No se ha encontrado lista publicada de razas vetadas en Níger.",
        "VUELTA A LA UE: es aquí donde está el problema real. El Reglamento de Ejecución (UE) 2026/636, de 20 de marzo de 2026, adopta las listas de terceros países y NÍGER NO FIGURA EN NINGUNO DE SUS ANEXOS; los únicos territorios africanos listados son insulares (Ascensión, Mauricio y Santa Elena). Por tanto rige el régimen del Reglamento Delegado (UE) 2026/131: prueba de valoración de anticuerpos antirrábicos, en laboratorio autorizado y ANOTADA EN EL PASAPORTE ANTES DE SALIR de la UE (vía A).",
        "Rabia: TravelHealthPro incluye la rabia entre los riesgos de Níger por contacto con animales. Un perro que viaja es, además, un vector de mordedura y de incidente con perros locales.",
        "Atención veterinaria: no se ha podido verificar en esta sesión ninguna clínica veterinaria de referencia en Niamey. Fuera de la capital no existe infraestructura veterinaria utilizable.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "FIEBRE AMARILLA OBLIGATORIA. TravelHealthPro: «a yellow fever vaccination certificate is required from all travellers aged 9 months or over». El MAEC la da igualmente por obligatoria y se comprueba en el control de entrada.",
        "Vacunas recomendadas para la mayoría: hepatitis A, tétanos y fiebre tifoidea (TravelHealthPro). El MAEC añade hepatitis, tétanos-difteria y MENINGITIS, coherente con el cinturón meningítico saheliano.",
        "Según perfil: cólera, dengue, hepatitis B, sarampión, meningococo, polio, rabia y tuberculosis (BCG).",
        "MALARIA DE ALTO RIESGO EN TODO EL PAÍS Y TODO EL AÑO. Quimioprofilaxis recomendada: atovacuona/proguanil, doxiciclina o mefloquina, más prevención de picaduras de anochecer a amanecer.",
        "Brote activo: poliovirus circulante derivado de vacuna tipo 3 (cVDPV3) reportado en agosto de 2026 (TravelHealthPro). Revisar el refuerzo de polio.",
        "Agua y comida: el MAEC es tajante — evitar agua no embotellada, alimentos crudos y puestos callejeros. Añadir esquistosomiasis: no bañarse ni vadear agua dulce (río Níger incluido).",
        "Asistencia sanitaria muy precaria fuera de Niamey según el MAEC. Cualquier problema serio implica evacuación médica internacional, que ningún seguro convencional cubrirá con el país en «desaconsejado absolutamente».",
    ],
    seguridad_intro="Níger es un país en guerra interna, con JNIM en el oeste, Estado Islámico en el Sahel y Boko Haram/ISWAP en Diffa. El MAEC desaconseja absolutamente viajar y, tras el secuestro de un estadounidense en octubre de 2025, eleva a muy elevado el riesgo en la propia Niamey: recomienda no caminar por la ciudad y prohíbe moverse entre las 17:00 y las 06:00. EEUU mantiene el Nivel 4 desde julio de 2026 y exige escolta militar para cualquier extranjero que salga de la capital. En 2026 el aeropuerto fue atacado dos veces y hubo un intento de golpe.",
    seguridad=[
        "SECUESTRO DE EXTRANJEROS: el FCDO habla de un «rise of reported terrorist and criminal kidnappings of foreign nationals» y de riesgo en todo el país, capital incluida. Un grupo de tres españoles con dos 4x4 es exactamente el perfil.",
        "ESCOLTA OBLIGATORIA: «Outside of Niamey you must be escorted by Nigerien security and military forces» (FCDO). El FCDO recomienda a los británicos no salir del perímetro urbano de Niamey.",
        "ESTADOS UNIDOS, NIVEL 4 (09/07/2026): zonas señaladas Niamey, franja fronteriza con Mali (Tillabéri, zona de las tres fronteras), Diffa/cuenca del lago Chad, norte de Agadez y el corredor del oleoducto Níger-Benín. Estado de emergencia con restricciones de movimiento.",
        "«Foreigners traveling beyond Niamey must request a military escort from the Nigerien police» (Departamento de Estado, 2026). Su personal se mueve en vehículos blindados, con toque de queda obligatorio, y tiene vetados restaurantes y mercados al aire libre.",
        "HORARIOS: el MAEC fija que se prohíben los desplazamientos antes de las 06:00 y después de las 17:00, y desaconseja taxis colectivos, autobuses y conducción nocturna.",
        "TILLABÉRI (frontera Mali/Burkina, zona de las tres fronteras): amenaza terrorista permanente según el MAEC. El 18 de enero de 2026 murieron al menos 31 personas en Gorouol. El 14 de mayo de 2026, emboscada del JNIM en Garbougna con 67 muertos.",
        "DIFFA (lago Chad): amenaza permanente de Boko Haram/ISWAP. TAHOUA: igualmente señalada por el MAEC.",
        "NIAMEY: el 29 de enero de 2026 el Estado Islámico atacó el aeropuerto internacional (20 atacantes muertos, 4 soldados heridos); el 18 de junio de 2026 el JNIM repitió con 11 soldados y 2 civiles muertos.",
        "INESTABILIDAD POLÍTICA: el 29 de agosto de 2026 la junta reprimió un intento de golpe con combates en el palacio presidencial, el aeropuerto y la radiotelevisión estatal RTN. El FCDO avisa de «further instability».",
        "APOYO CONSULAR LIMITADO: el FCDO reconoce que «support for British nationals is severely limited in Niger» y lo presta en remoto desde Lagos. España sí mantiene embajada abierta en Niamey, pero con capacidad de reacción muy condicionada.",
        "APOYO CONSULAR LIMITADO: el FCDO reconoce que «support for British nationals is severely limited in Niger» y lo presta en remoto desde Lagos; la embajada estadounidense «cannot offer routine or emergency services outside of Niamey». España mantiene embajada abierta en Niamey desde 2007, reorganizada en abril de 2026, pero su alcance fuera de la capital es igual de limitado.",
    ],
    agua=[
        "Agua de boca: NO beber agua no embotellada (MAEC). Para la expedición eso significa filtro más potabilización química o UV en el 100 % de lo que entre en los depósitos.",
        "Agua de uso general (ducha, lavado): las fuentes utilizables son los pozos y las redes urbanas de Niamey, Dosso, Maradi y Zinder; fuera de eje urbano, el Sahel y el Ténéré no ofrecen puntos fiables. POR CONFIRMAR sin relatos recientes de overlanders.",
        "NO vadear ni bañarse en agua dulce: esquistosomiasis confirmada por TravelHealthPro. El río Níger a su paso por Niamey entra en esa categoría.",
        "En el desierto, la autonomía de agua es el límite duro: Assamakka está a 200 km de Arlit por pista y a 400 km de Tamanrasset, sin puntos intermedios garantizados.",
        "Con las temperaturas de junio por encima de 45 °C de media a la sombra en la frontera argelina, el consumo por persona y día se dispara y multiplica el problema de carga.",
    ],
    combustible=[
        "GASOLINA: 499 FCFA/litro (0,762 EUR; 0,886 USD) según GlobalPetrolPrices, dato de 8 de diciembre de 2025. Muy por debajo de la media mundial (727 FCFA en ese momento).",
        "Sahara Overland, en su revisión de julio de 2026, cita gasóleo a 600 FCFA/litro y gasolina a 636 FCFA/litro: precios de calle superiores a la referencia estadística, señal de tensión de suministro.",
        "Níger es productor y refinador (refinería de Zinder), pero el combustible es también una palanca política: el 12 de enero de 2026 el Gobierno revocó las licencias de 33 transportistas que se negaron a llevar combustible a Mali.",
        "Red de estaciones fiable solo en el eje Niamey — Dosso — Birni N'Konni — Maradi — Zinder y en Agadez/Arlit. Fuera de ahí, bidones y mercado informal, con la calidad que eso implica.",
        "Racionamiento y disponibilidad real en 2026: POR CONFIRMAR. No se ha localizado en esta sesión una fuente fechada que documente cortes de suministro a surtidor.",
        "Para un Grenadier y una Delica con 250 km/día, la autonomía crítica está en los tramos desérticos del norte, donde además el acceso está vetado sin escolta.",
        "La paridad fija del franco CFA (1 EUR = 655,957 FCFA) hace que los precios no fluctúen por tipo de cambio: 499 FCFA son 0,76 EUR y 636 FCFA, 0,97 EUR.",
    ],
    experiencias_intro="No hay relatos recientes de overlanders en Níger: el turismo desértico se hundió hace más de una década y el país lleva desde 2023 bajo junta militar. Lo que sigue son las últimas referencias utilizables, con su fecha, y lo que cada una aporta a la decisión.",
    experiencias=[
        "Sahara Overland, el archivo de referencia, da el Ténéré por perdido: en su revisión de julio de 2026 Chris Scott escribe que «desert tourism collapsed in the Aïr-Tenere years ago with no reports of anyone crossing from Algeria for well over a decade». Esa frase es el dato más importante de toda la ficha: no es que sea peligroso, es que nadie lo hace. La misma página conserva la mecánica histórica —laissez-passer en vez de carnet, seguro de zona CFA, permisos de desierto desde 50 euros al día con guía— como arqueología de lo que fue.",
        "El precio de la escolta, según el operador local: Niger Travel and Tours, con sede en Agadez, mantiene publicado desde noviembre de 2018 que «private military security convoys, which can sometimes be mandatory for travel, cost $4000 and up for 5-7 days around Agadez in the north», y recomienda contratar un operador en vez de gestionarlo por cuenta propia porque los militares cobran por adelantado. Es la única cifra concreta localizada del coste real de moverse por el norte.",
        "El Ténéré más allá de Madam, vetado desde antes del golpe: la misma fuente de Agadez señalaba ya en 2018 restricciones severas al norte de Madam por minas terrestres y presencia militar multilateral. Es decir, el tramo mítico hacia Bilma, Dirkou y Toummo estaba cerrado por munición sin explotar y despliegue militar años antes de que la junta y el yihadismo actual lo hicieran irrelevante.",
        "La ruta Agadez-Dirkou, atacada: Sahara Overland documenta incidentes en 2022 en el eje Agadez-Dirkou y ataques a campamentos mineros artesanales, en un momento en el que el país todavía tenía gobierno electo y presencia militar francesa. El deterioro es anterior al golpe de julio de 2023, no una consecuencia de él.",
        "Assamakka no es una frontera de viajeros, es una frontera de deportados: la Wikipedia en inglés describe el puesto como el único cruce oficial con Argelia y como punto donde Argelia devuelve regularmente a migrantes subsaharianos. Atalayar cifraba en enero de 2026 más de 34.000 deportaciones que consolidan el corredor Argelia-Níger como una de las rutas migratorias más letales de África. Presentarse ahí con dos 4x4 europeos es entrar en un escenario que no está pensado para turistas.",
        "El aeropuerto como línea del frente: Wikipedia recoge que las fuerzas francesas dejaron la base aérea de Diori Hamani en diciembre de 2023, que Estados Unidos completó su retirada el 7 de julio de 2024 y que personal militar ruso ocupó después las instalaciones; el propio aeropuerto fue atacado el 29 de enero y el 18 de junio de 2026 y fue objetivo del intento de golpe del 29 de agosto. La única puerta de entrada al país es también un objetivo militar recurrente.",
        "La frontera de Benín, cerrada por política y no por seguridad: Africanews informaba el 18 de junio de 2026 de que Cotonú y Niamey firmaban un comunicado conjunto comprometiéndose a reabrir y creaban un comité de expertos, sin apertura efectiva. El origen del cierre, según la Wikipedia, fue la acusación nigerina de que Benín albergaba bases francesas, pese a que el 80 % de las importaciones de Níger pasaban por ahí. Para un overlander, la puerta lógica desde el golfo de Guinea sigue tapiada.",
        "Nigeria sí reabrió: VOA Africa informó en marzo de 2024 de que los servicios de inmigración nigerianos recibieron la orden de reabrir «with immediate effect» por directiva del presidente Tinubu, tras el levantamiento de sanciones de la CEDEAO, citando expresamente el puesto de Jibiya en el estado de Katsina. Es el único paso terrestre con reapertura documentada y fechada en esta sesión.",
        "El Árbol del Ténéré, el relato que hay que corregir: la Wikipedia detalla que el acacia solitaria, referencia de las caravanas de sal durante unos 300 años, fue derribada en 1973 por un camionero libio presuntamente ebrio, tras haber sobrevivido a un golpe anterior en 1959, y que el 8 de noviembre de 1973 el árbol muerto se instaló en un santuario del Museo Nacional de Níger, en Niamey. En el desierto solo queda una escultura metálica, y en el centro histórico de Agadez una réplica más fiel.",
        "El Aïr y el Ténéré llevan 34 años en la lista roja: las Reservas Naturales del Aïr y Ténéré, 7.736.000 hectáreas inscritas por la UNESCO en 1991, entraron en la Lista del Patrimonio Mundial en Peligro en 1992 y siguen ahí. La UNESCO cita la caza furtiva y el pastoreo ilegal como amenazas principales y pide reforzar la presencia física de las autoridades de gestión sobre el terreno. Traducido: el Estado nigerino no controla el territorio que el catálogo turístico vende, y no lo controla desde antes de que existiera el yihadismo saheliano.",
        "El silencio como dato: entre 2019 y 2026 no se ha localizado en esta sesión ni un solo relato de overlander independiente cruzando Níger con vehículo propio. En un país que en los años noventa era la etapa estrella de la travesía sahariana, esa ausencia de literatura es la conclusión operativa: no hay ruta que planificar, hay un país al que no se va.",
    ],
    pendientes=[
        ("Tarifa y plazo oficial del visado en Bruselas", "Abrir la web o el escrito oficial de la Embajada de Níger en Bruselas con tasas y plazos vigentes, o confirmación por correo/teléfono al +32 2 648 61 40."),
        ("Demarcación consular exacta para residentes en España", "Confirmar con el MAEC o con la propia embajada nigerina que Bruselas es la competente para España en 2026 y no Ginebra, Ámsterdam o Bonn."),
        ("Régimen aduanero del vehículo (CPD vs laissez-passer)", "Documento de la aduana nigerina o relato fechado 2024-2026 que confirme si se admite carnet de passages o solo laissez-passer, y su coste."),
        ("Validez de la Carte Brune CEDEAO tras la salida de Níger", "Nota de la CEDEAO, de la aseguradora emisora o de OFESAUTO que aclare si la Carte Brune sigue amparando a Níger tras su retirada del bloque."),
        ("Estado formal de los pasos de Bosso (Chad), Toummo (Libia) y Labbezanga (Mali)", "Fuente oficial nigerina o aviso consular fechado en 2025-2026 que declare abierto o cerrado cada puesto."),
        ("Reapertura efectiva de Gaya-Malanville", "Comunicado oficial de Níger o de Benín, o noticia fechada, que confirme la apertura física del puente y no solo el compromiso de junio de 2026."),
        ("Prohibición o autorización real de drones en la práctica", "Texto publicado por la ANAC (anac.ne) o aviso consular que confirme si la importación está prohibida o requiere autorización previa concreta."),
        ("Web oficial de los servicios veterinarios de Níger", "Localizar y abrir la página del Ministère de l'Agriculture et de l'Élevage o del servicio veterinario nacional con las condiciones de importación de animales de compañía."),
        ("Razas de perro prohibidas en Níger", "Lista publicada por la autoridad nigerina o confirmación expresa de que no existe."),
        ("Planes y precios de Starlink en Níger en 2026", "Abrir el mapa de disponibilidad de starlink.com o una fuente fechada con los planes Roam/residencial y sus tarifas."),
        ("Operadores móviles y requisitos de SIM para extranjeros", "Fuente de la ARCEP nigerina o relato fechado con el procedimiento de registro de SIM prepago."),
        ("Racionamiento y disponibilidad de combustible en 2026", "Noticia o informe fechado que documente si hay colas, cupos o cortes de suministro en surtidor."),
        ("Hospitales y clínicas de referencia en Niamey", "Listado de médicos y centros recomendados publicado por la Embajada de España en Niamey o por otra embajada europea."),
        ("Vía legal de acceso al Aïr y al Ténéré", "Confirmación escrita del Ministerio de Turismo nigerino o de la ANAC/autoridad de la reserva de si existe algún permiso expedible a extranjeros en 2026 y en qué condiciones."),
        ("Aviso oficial sobre drones", "Localizar y abrir anac.ne o el Journal Officiel nigerino con el reglamento de aeronaves no tripuladas y su régimen de importación."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026. Todos los datos proceden de páginas abiertas en esa revisión y llevan la fecha de su fuente; lo que no se pudo confirmar aparece como «por confirmar» y está recogido en pendientes. Esta ficha es una herramienta de planificación, no una autorización de viaje: Níger está excluido por protocolo y nada de lo aquí escrito sustituye a la recomendación del MAEC ni a la decisión de una aseguradora.",
    emergency="EMERGENCIA CONSULAR ESPAÑOLA EN NÍGER: +227 96 83 83 94 (Embajada de España en Niamey, Rue AM-5, Koira Kano; centralita +227 20 75 59 61/62/64, emb.niamey@maec.es). Números nacionales de Níger: POLICÍA 17, AMBULANCIA 15, BOMBEROS 18 (Wikipedia, lista de números de emergencia). No confundir con Nigeria, que usa el 112. La respuesta real de ambulancia y bomberos es muy limitada: el canal principal es el teléfono consular, y fuera de Niamey la embajada no puede garantizar asistencia.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

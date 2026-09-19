# -*- coding: utf-8 -*-
"""Somalia — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Somalia está FUERA DE LA RUTA PREVISTA y es el país con la recomendación más dura del MAEC de toda África: desaconsejado viajar bajo cualquier circunstancia. La app solo tiene un stub: créala entera con el formato del piloto de Túnez. La ficha es INFORMATIVA y debe dejar claro por qué NO se va. Claves que DECIDEN la ficha y hay que documentar con fuente fechada: Al Shabab sigue activo con atentados regulares en Mogadiscio y control de zonas rurales del centro y el sur; el riesgo de secuestro de extranjeros es alto; la piratería en la costa nordeste ha repuntado desde 2023-2024. DISTINGUE CON CLARIDAD TRES REALIDADES: (1) Somalia federal (Mogadiscio, Baidoa, Kismayo), donde se viaja con escolta armada privada y alojamiento fortificado; (2) SOMALILANDIA (Hargeisa, Berbera, Las Geel), autoproclamada independiente desde 1991, no reconocida, con su propio visado y su propia moneda, de facto estable y visitable con Special Protection Unit obligatoria fuera de la capital; y (3) PUNTLANDIA (Garowe, Bosaso), autónoma dentro de Somalia. Los visados y los permisos son distintos en cada una y NO son intercambiables. El conflicto de Las Anod (2023) entre Somalilandia y las milicias de Dhulbahante y el acuerdo de acceso al mar con Etiopía (enero de 2024) son los dos hechos que más han movido la situación.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/somalia.json y audit/pdi/somalia.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Mogadiscio · ciudad vieja de Hamar Weyne y el puerto", cat="Cultura", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=2.0317269, lon=45.3426366,  # Google Maps: Xamar-Weyne Fish Market
        desc="Hamar Weyne y Shangani son el Mogadiscio anterior a 1938: hasta esa fecha la ciudad se reducía a esos dos barrios. En sus callejuelas se concentran más de 25 mezquitas, entre ellas la de Fakr ad-Din, fechada por inscripción en 1269 y con mihrab de mármol traído del norte de la India. Al lado está el puerto, creado como instalación moderna por Italia en los años veinte y gestionado desde 2014 por la turca Albayrak. VISITA SOLO CON ESCOLTA ARMADA PRIVADA: el MAEC desaconseja viajar a Somalia bajo cualquier circunstancia.",
        dog_note="Barrio de mezquitas y mercados, recorrido obligatoriamente con escolta armada; el perro estorba el dispositivo y no es bien recibido en recintos religiosos.",
        visit={
            "why": "Es el núcleo histórico de una de las ciudades comerciales más antiguas del Índico occidental y el único lugar de Mogadiscio donde queda tejido urbano antiguo. La mezquita de Fakr ad-Din, de 1269, es el monumento fechado más antiguo de la ciudad.",
            "see": "Callejuelas de casas benadiríes, las Twin Mosques (Aw Mukhtar y Aw Sheikh Omar), la Jama'a Xamar Weyne y la mezquita de Fakr ad-Din con sus dos cúpulas cónicas. Desde el paseo del puerto se ven los muelles de Albayrak.",
            "access": "Asfalto urbano en mal estado; no hay aparcamiento turístico y dos 4x4 extranjeros aparcados llaman mucho la atención. El movimiento se hace en convoy con escolta privada contratada desde el aeropuerto Aden Adde, con recogida en pista. No hay horarios ni entradas: es barrio vivo. El pin marca el mercado de Xamar Weyne, punto navegable dentro del casco viejo.",
            "when": "Mañana temprano, entre semana; noviembre-marzo evita las lluvias de abril-mayo y junio-agosto.",
            "skip": "Descártalo en bloque: el MAEC (28/05/2026) desaconseja viajar a Somalia bajo cualquier circunstancia y el FCDO (04/06/2026) desaconseja todo viaje al país.",
        },
        links=[
            {"label": "Hamar Weyne (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Hamar_Weyne,_Mogadishu"},
            {"label": "Puerto de Mogadiscio (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Port_of_Mogadishu"},
            {"label": "Mezquita de Fakr ad-Din (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Fakr_ad-Din_Mosque"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Aerial_view_of_the_port_of_Mogadishu.JPEG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Aerial_view_of_the_port_of_Mogadishu.JPEG",
                "credit": "TSGT PERRY HEIMER · Public domain",
                "caption": "El puerto de Mogadiscio desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/2013_04_15_Port_B.jpg_(8654746348).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:2013_04_15_Port_B.jpg_(8654746348).jpg",
                "credit": "AMISOM Public Information · CC0",
                "caption": "Faena en el puerto de Mogadiscio.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mogadishu_Daily_Life_one_year_after_Al_Shabaab_02_(7731055824).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mogadishu_Daily_Life_one_year_after_Al_Shabaab_02_(7731055824).jpg",
                "credit": "AMISOM Public Information · CC0",
                "caption": "Vida diaria en Mogadiscio.",
            },
        ],
    ),
    dict(
        n=2, name="Playa del Lido · la costa de Mogadiscio", cat="Costa", prio="Media",
        dog="no recomendado", time="medio día",
        lat=2.0403466, lon=45.3629556,  # Google Maps: Playa de Lido
        desc="La playa del Lido abre el frente norte de Mogadiscio sobre el mar de Somalia y conserva el nombre que le pusieron los italianos, que la urbanizaron a finales de los años treinta y la remataron en los cincuenta. Hoy es el escaparate de la reconstrucción: restaurantes de pescado, hoteles y paseo lleno los fines de semana. También es objetivo recurrente de Al Shabab: atentados en 2016 (una veintena de muertos), en 2020 y el del 2 de agosto de 2024, con al menos 56 fallecidos. El faro de Secondo-Lido, en este mismo frente, entró en 2025 en la lista indicativa de Somalia ante la UNESCO. NO ES UNA PLAYA PARA BAÑARSE SIN ESCOLTA.",
        dog_note="Playa urbana muy concurrida y de sensibilidad religiosa alta; además es objetivo repetido de atentados, sin margen para gestionar un animal.",
        visit={
            "why": "Es el termómetro social de Mogadiscio y el sitio donde se mide de un vistazo cuánto ha cambiado la ciudad y cuánto no.",
            "see": "Arena clara, arrecife coralino, marisquerías y hoteles nuevos levantados con dinero de la diáspora, y el faro de Secondo-Lido, propuesto por Somalia para la lista indicativa de la UNESCO en 2025; atardecer con la ciudad al fondo.",
            "access": "Se llega por la avenida costera desde el eje del aeropuerto, siempre en convoy; los restaurantes de la playa tienen recinto vallado con control de acceso donde caben dos 4x4. No hay entrada. Corrientes fuertes y ninguna vigilancia acuática. El pin marca la playa del Lido; para comer hay que fijar el hotel o restaurante concreto.",
            "when": "Viernes por la tarde es cuando está viva, pero también cuando más expuesta queda; diciembre-febrero para el clima.",
            "skip": "Descártalo: acumula el peor historial de atentados contra objetivos blandos de la ciudad, con el ataque del 2 de agosto de 2024 como referencia.",
        },
        links=[
            {"label": "Lido Beach (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Lido_Beach,_Mogadishu"},
            {"label": "Mogadiscio (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Mogadishu"},
            {"label": "Recomendaciones de viaje MAEC · Somalia", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Somalia"},
            {"label": "UNESCO · Somalia, Estado Parte y lista indicativa", "url": "https://whc.unesco.org/en/statesparties/so"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mogadishu_Liido_beach.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mogadishu_Liido_beach.JPG",
                "credit": "Khadija Isse · CC BY-SA 4.0",
                "caption": "La playa del Lido.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lido_beach_from_the_sea_in_Mogadishu.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lido_beach_from_the_sea_in_Mogadishu.jpg",
                "credit": "AMISOM · CC0",
                "caption": "El Lido visto desde el mar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/People_play_in_the_ocean_on_Lido_beach_in_Mogadishu,_Somalia,_during_Eid_al-Fitr_on_July_28._AMISOM_Photo_-_Tobin_Jones_(14581419187).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:People_play_in_the_ocean_on_Lido_beach_in_Mogadishu,_Somalia,_during_Eid_al-Fitr_on_July_28._AMISOM_Photo_-_Tobin_Jones_(14581419187).jpg",
                "credit": "AMISOM Public Information · CC0",
                "caption": "Baño en el Lido durante el Eid.",
            },
        ],
    ),
    dict(
        n=3, name="Catedral de Mogadiscio · el barrio italiano en ruinas", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=2.0358777, lon=45.3416169,  # Google Maps: Catedral de Mogadiscio
        desc="Levantada entre 1923 y 1928 por la administración italiana con proyecto de Antonio Vandone, copiaba el románico normando de la catedral de Cefalù: planta de cruz latina, tres naves con arcos apuntados y dos torres de 37,5 metros. Fue sede episcopal hasta 1991 y quedó arrasada por Al Shabab en 2008, sin cubierta pero con muros y arcos en pie. En 2013 la diócesis anunció su reconstrucción; en 2023 seguía en ruinas y sin obras. Se fotografía desde fuera y en cuestión de minutos.",
        dog_note="Recinto religioso en ruinas, con escombros y hierros sueltos; parada de minutos con escolta, sin sitio para bajar al animal.",
        visit={
            "why": "Es la ruina que mejor resume el siglo XX somalí: colonia italiana, independencia, guerra civil y yihadismo en un solo edificio.",
            "see": "El esqueleto de las tres naves, los arcos apuntados de piedra y los muñones de las dos torres de la fachada; alrededor, el trazado del barrio italiano con edificios administrativos reventados.",
            "access": "Está en pleno centro, a pocos minutos de Hamar Weyne, con asfalto degradado; no hay recinto ni taquilla y el solar está sin acondicionar. Parada breve en convoy, sin bajar de los vehículos más de lo imprescindible. El pin marca la ruina de la catedral.",
            "when": "Primera hora de la mañana, con luz rasante y poca gente; estación seca (diciembre-marzo).",
            "skip": "Descártalo mientras siga la recomendación del MAEC; y aunque se levantara, el entorno inmediato es de los más vigilados de la ciudad.",
        },
        links=[
            {"label": "Catedral de Mogadiscio (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Mogadishu_Cathedral"},
            {"label": "Mogadiscio (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Mogadishu"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cattedrale_di_Mogadiscio_2023.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cattedrale_di_Mogadiscio_2023.jpg",
                "credit": "Dan Sloan · CC BY-SA 2.0",
                "caption": "La catedral de Mogadiscio en 2023.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/2012_11_18_AMISOM_Mogadishu_Cathedral_F_(8199816654).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:2012_11_18_AMISOM_Mogadishu_Cathedral_F_(8199816654).jpg",
                "credit": "AMISOM Public Information · CC0",
                "caption": "El interior arruinado de la catedral.",
            },
        ],
    ),
    dict(
        n=4, name="Mercado de Bakaara · el corazón económico y su leyenda negra", cat="Ciudad · servicios", prio="Media",
        dog="prohibido", time="medio día",
        lat=2.0471218, lon=45.3188406,  # Google Maps: Mercado de Bakaara
        desc="Creado a finales de 1972 bajo Siad Barre, Bakaara es el mayor mercado al aire libre de Somalia: maíz, sorgo, alubias, cacahuete, sésamo, trigo, arroz, gasolina y medicinas, más una sección negra llamada Cabdalle Shideeye especializada en documentación falsa. Aquí cayeron dos Black Hawk el 3 de octubre de 1993 y aquí empezó la batalla de Mogadiscio. Su historial de incendios y atentados es largo, del mortero de 2009 (20 muertos) al cuádruple atentado de febrero de 2024. NO ES UN SITIO PARA EXTRANJEROS.",
        dog_note="Mercado alimentario masivo, con presencia yihadista y el mayor riesgo de secuestro de la ciudad; entrar con un perro es impensable.",
        visit={
            "why": "Es el pulso económico real del país y el escenario del episodio que marcó la relación de Occidente con Somalia durante treinta años.",
            "see": "Pasillos de sacos de grano y sorgo, cambistas, puestos de piezas y combustible; nada monumental, todo comercio.",
            "access": "Calles sin asfaltar en buena parte, sin posibilidad de aparcar dos 4x4 sin bloquear el mercado. No hay horarios ni entrada. Las empresas de seguridad de Mogadiscio no suelen aceptar llevar clientes aquí. El pin marca el distrito de Howlwadaag, donde Wikipedia sitúa el mercado; el punto exacto de la entrada está POR CONFIRMAR.",
            "when": "Irrelevante: no hay ventana recomendable.",
            "skip": "Descártalo siempre, incluso en un escenario futuro de mejora: es el punto de la capital con más historial de atentados y secuestros.",
        },
        links=[
            {"label": "Bakaara Market (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bakaara_Market"},
            {"label": "Mercado de Bakaara (Wikipedia en español)", "url": "https://es.wikipedia.org/wiki/Mercado_de_Bakaara"},
            {"label": "Howlwadaag, Mogadiscio (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Howlwadaag,_Mogadishu"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bakaara_Market_(6152938113).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bakaara_Market_(6152938113).jpg",
                "credit": "AMISOM Public Information · CC0",
                "caption": "Un puesto del mercado de Bakaara.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Street_life_in_Bukara_Market_(6242875971).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Street_life_in_Bukara_Market_(6242875971).jpg",
                "credit": "AMISOM Public Information · CC0",
                "caption": "Calle del mercado de Bakaara.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Daily_life_in_Bukara_Market_(6243386144).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Daily_life_in_Bukara_Market_(6243386144).jpg",
                "credit": "AMISOM Public Information · CC0",
                "caption": "Vida diaria en Bakaara.",
            },
        ],
    ),
    dict(
        n=5, name="Afgooye y el bajo Shabelle · el corredor agrícola", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="medio día",
        lat=2.1426226, lon=45.1167167,  # Google Maps: Afgooye
        desc="Treinta kilómetros al noroeste de Mogadiscio, Afgooye es la puerta del bajo Shabelle: el río cruza el pueblo y riega el corredor agrícola que abastece la capital. Fue capital del sultanato Geledi y a principios del siglo XIX llegó a superar los 80.000 habitantes, con edificios de varias plantas, cañerías y muralla de cinco puertas. Conserva el Istunka, torneo anual de lucha con palos heredado del periodo ajurán que marca el año nuevo. El corredor concentra además uno de los mayores asentamientos de desplazados del país.",
        dog_note="Zona rural con Al Shabab activo y campos de desplazados; ningún alojamiento apto y control de paso constante.",
        visit={
            "why": "Es el granero de Mogadiscio y el único sitio donde se ve el Shabelle en un entorno agrícola trabajado, además de la sede del Istunka.",
            "see": "El puente sobre el Shabelle, bananeras y huertas, mercado de producto y, si se acierta con la fecha, el torneo de Istunka con su parte de poesía y música.",
            "access": "Carretera asfaltada desde Mogadiscio, la más transitada del país, con puestos de control militares constantes; 30 km. No hay aparcamiento formal. Las salidas de la capital hacia el oeste solo se hacen con escolta y coordinación previa. El pin marca el núcleo de Afgooye, junto al río.",
            "when": "Istunka cae en el año nuevo somalí (julio-agosto, fecha por confirmar); clima mejor entre diciembre y marzo.",
            "skip": "Descártalo: el Gobierno recuperó el pueblo en 2012, pero Al Shabab sigue operando en el campo del bajo Shabelle y emboscando esa carretera.",
        },
        links=[
            {"label": "Afgooye (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Afgooye"},
            {"label": "Al Shabab (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Al-Shabaab_(militant_group)"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Afgoi_River,.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Afgoi_River,.jpg",
                "credit": "Amal Aweis · CC BY-SA 4.0",
                "caption": "El Shabelle a su paso por Afgooye.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Afgoi_Farms,_Lower_Shabelle_Somalia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Afgoi_Farms,_Lower_Shabelle_Somalia.jpg",
                "credit": "Amal Aweis · CC BY-SA 4.0",
                "caption": "Huertas del bajo Shabelle.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Istunka_Afgoye.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Istunka_Afgoye.jpg",
                "credit": "E. H. M. Clifford · CC BY-SA 4.0",
                "caption": "El istunka, el torneo tradicional de Afgooye.",
            },
        ],
    ),
    dict(
        n=6, name="Merca (Marka) · la ciudad benadirí de la costa", cat="Costa", prio="Alta",
        dog="no recomendado", time="1 noche",
        lat=1.7174656, lon=44.7686135,  # Google Maps: Merca
        desc="Merca aparece ya en el Periplo del mar Eritreo, en el siglo I, y fue centro administrativo del sultanato ajurán antes de convertirse, con los colonos italianos de los años treinta, en el gran puerto bananero del Benadir. De aquella época quedan almacenes, arquitectura benadirí de coral y un embarcadero. Está a 109 kilómetros al suroeste de Mogadiscio por la costera. Cambió de manos varias veces: Al Shabab la tomó en febrero de 2016 y el 27 de julio de 2022 un suicida mató al alcalde y a otras veinte personas.",
        dog_note="Casco histórico con mezquitas y presencia yihadista intermitente; sin alojamiento que admita animales ni margen de maniobra.",
        visit={
            "why": "Es el conjunto benadirí más completo de la costa después de Mogadiscio y el mejor testimonio de la economía bananera colonial.",
            "see": "Casas de coral encaladas, mezquitas antiguas, el viejo muelle y los almacenes del puerto bananero; playa larga sin urbanizar al sur.",
            "access": "Carretera costera desde Mogadiscio, 109 km, con tramos deteriorados y control militar; también hay aeródromo K50 a medio camino. El casco viejo es de calles estrechas: dos 4x4 se dejan en el descampado del puerto. Sin horarios ni entradas. Estado de seguridad muy volátil: la ciudad ha caído y ha sido recuperada varias veces desde 2016.",
            "when": "Diciembre-marzo, fuera de las lluvias gu; primera hora por el calor y la humedad.",
            "skip": "Descártalo mientras Al Shabab opere en el bajo Shabelle; el atentado que mató al alcalde en julio de 2022 marca el nivel de amenaza.",
        },
        links=[
            {"label": "Merca (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Merca"},
            {"label": "FCDO · Somalia travel advice", "url": "https://www.gov.uk/foreign-travel-advice/somalia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Merca,_Somalia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Merca,_Somalia.jpg",
                "credit": "Bacciy (talk) · Public domain",
                "caption": "Merca desde lo alto.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Merca_streets.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Merca_streets.JPG",
                "credit": "New Ways Merka · CC BY-SA 2.0",
                "caption": "Calle del casco antiguo de Merca.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Merca_streets2.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Merca_streets2.JPG",
                "credit": "New Ways Merka · CC BY-SA 2.0",
                "caption": "Arquitectura benadirí en Merca.",
            },
        ],
    ),
    dict(
        n=7, name="Barawa (Brava) · la lengua chimwiini y la costa suroeste", cat="Costa", prio="Alta",
        dog="no recomendado", time="1 noche",
        lat=1.115007, lon=44.0314325,  # Google Maps: Barāwe
        desc="Barawa, la Brava de los italianos, es una de las ciudades suajilis más antiguas de la costa somalí y la única donde se habla chimwiini, el dialecto suajili propio de los bravaneses. Resistió el ataque portugués de Tristão da Cunha en 1506, Zanzíbar la cedió a Italia en 1889 y quedó casi destruida en 1991. Al Shabab la controló de 2009 a octubre de 2014, cuando el Ejército somalí y AMISOM la recuperaron. Playas largas, casas de coral encaladas y una lengua que apenas sobrevive fuera de la diáspora.",
        dog_note="Ciudad conservadora, sin infraestructura turística y con acceso terrestre cortado; nada preparado para un animal.",
        visit={
            "why": "Por el patrimonio inmaterial: el chimwiini es una isla lingüística suajili dentro del mundo somalí, y la tradición de escuela islámica y tejido de Barawa fue célebre en todo el Índico.",
            "see": "Casco de coral encalado, mezquitas, el frente marítimo y las dunas; la costa entre Barawa y Merca es de las más vacías del país.",
            "access": "Carretera costera desde Merca en mal estado y bajo amenaza constante; en la práctica solo se llega por aire o por mar con operación militar. No hay hoteles homologados ni aparcamiento. El pin marca el núcleo urbano de Barawa; el punto navegable real sería el frente del puerto.",
            "when": "Diciembre-marzo; el monzón de junio-agosto levanta mucho mar.",
            "skip": "Descártalo: está dentro de la zona donde Al Shabab conserva capacidad territorial, con Jilib como cuartel general a menos de 200 km.",
        },
        links=[
            {"label": "Barawa (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Baraawe"},
            {"label": "Brava, Somalia (Wikipedia en italiano)", "url": "https://it.wikipedia.org/wiki/Brava_(Somalia)"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/2015_05_23_CDF_Barawe-1-2_(17821842600).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:2015_05_23_CDF_Barawe-1-2_(17821842600).jpg",
                "credit": "AMISOM Public Information · CC0",
                "caption": "Barawa, en la costa suroeste.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/2015_05_23_CDF_Barawe-11_(17819144728).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:2015_05_23_CDF_Barawe-11_(17819144728).jpg",
                "credit": "AMISOM Public Information · CC0",
                "caption": "Calles de Barawa.",
            },
        ],
    ),
    dict(
        n=8, name="Kismayo y el bajo Juba · el puerto del sur", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=-0.3881066, lon=42.5426788,  # Google Maps: Kismayo port
        desc="Capital de facto de Jubalandia y tercer puerto del país, Kismayo está 528 kilómetros al suroeste de Mogadiscio, donde el Juba desemboca en el Índico. El puerto es de 1964 y el aeropuerto queda a unos diez kilómetros. La fundaron los bajuni; pasó por el imperio ajurán, el sultanato Geledi y la Italia colonial desde 1925-26. Al Shabab la controló de 2006 a septiembre de 2012, cuando la desalojaron las fuerzas somalíes y de AMISOM. SE LLEGA EN AVIÓN, NO POR CARRETERA.",
        dog_note="Plaza militarizada a la que se llega en avión; los vuelos regionales y los recintos de la AU no admiten animales de compañía.",
        visit={
            "why": "Es la llave del sur y el único gran puerto entre Mogadiscio y Mombasa; su control decide quién manda en el valle del Juba. En su hinterland está el parque nacional de Bushbushle, uno de los tres sitios que Somalia propuso en 2024-2025 para su lista indicativa ante la UNESCO.",
            "see": "El puerto de 1964, el frente marítimo, playas largas al norte y la desembocadura del Juba; la ciudad es funcional, no monumental.",
            "access": "Tres carreteras principales conectan la ciudad, pero ninguna es transitable para extranjeros: el trayecto habitual es vuelo desde Mogadiscio o Nairobi al aeropuerto Ahmed Gurey, a unos 10 km. Alojamiento en recintos fortificados. Escolta obligatoria para cualquier desplazamiento. El pin marca el puerto.",
            "when": "Estación seca xagaa, tras las lluvias gu de abril a julio.",
            "skip": "Descártalo: el bajo Juba es el corazón del territorio de Al Shabab y la carretera de acceso está cortada de hecho.",
        },
        links=[
            {"label": "Kismayo (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Kismayo"},
            {"label": "Kismaayo (Wikipedia en español)", "url": "https://es.wikipedia.org/wiki/Kismayo"},
            {"label": "UNESCO · Somalia, Estado Parte y lista indicativa", "url": "https://whc.unesco.org/en/statesparties/so"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Kismayo_Dalxiiska_2016.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Kismayo_Dalxiiska_2016.jpg",
                "credit": "Mr.matija.kovac · CC BY-SA 4.0",
                "caption": "La playa de Dalxiiska, en Kismayo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Kismayo_1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Kismayo_1.jpg",
                "credit": "Zahra Qorane · CC BY-SA 4.0",
                "caption": "Kismayo desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Kismayo_Gobweyn.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Kismayo_Gobweyn.jpg",
                "credit": "Zahra Qorane · CC BY-SA 4.0",
                "caption": "El bajo Juba en Gobweyn.",
            },
        ],
    ),
    dict(
        n=9, name="Baidoa y el Bay · el interior agrícola", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=3.1043845, lon=43.6327611,  # Google Maps: Shaati Gaduud International Airport - Baydhabo
        desc="Baidoa, la «Baydhabo Janaay» o paradisíaca, manda sobre la zona interfluvial del Bay, comarca del sorgo, las cabras y los camellos. Fue escala de caravanas bajo el sultanato Geledi y, en 1992, el epicentro de la hambruna que la prensa internacional bautizó como la ciudad de la muerte. Hoy ronda el 1,2 millón de habitantes contando desplazados, tiene la Universidad del Sur de Somalia (2007) y un aeropuerto con pista asfaltada de 3.000 metros. Las fuerzas etíopes y somalíes la recuperaron de Al Shabab en febrero de 2012.",
        dog_note="Ciudad sitiada de hecho, con enorme población desplazada; no hay alojamiento ni logística que contemple un perro.",
        visit={
            "why": "Es la capital del mundo rahanweyn y el observatorio más claro de la relación entre sequía, hambruna y desplazamiento en Somalia.",
            "see": "Mercado de sorgo y ganado, manantiales del borde de la meseta, campus universitario y la extensión de los campos de desplazados alrededor.",
            "access": "Asfalto parcial desde Mogadiscio (unos 250 km) pero la carretera atraviesa terreno controlado por Al Shabab; la vía normal es el vuelo al aeropuerto de Baidoa, con pista de 3.000 m a 1.520 pies de altitud. Alojamiento en recintos protegidos. El pin marca el aeropuerto, que es el punto de entrada real.",
            "when": "Lluvias en abril-mayo y octubre-noviembre (585 mm al año); mejor enero-marzo.",
            "skip": "Descártalo: la ciudad está en la práctica cercada y los accesos por carretera son la principal zona de emboscadas del centro-sur.",
        },
        links=[
            {"label": "Baidoa (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Baidoa"},
            {"label": "FCDO · Somalia travel advice", "url": "https://www.gov.uk/foreign-travel-advice/somalia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Baidoa_Market.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Baidoa_Market.jpg",
                "credit": "Zahra Qorane · CC BY-SA 4.0",
                "caption": "El mercado de Baidoa.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Baidoa_Somalia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Baidoa_Somalia.jpg",
                "credit": "Zahra Qorane · CC BY-SA 4.0",
                "caption": "Baidoa, capital del Bay.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Xoolaha_Baydhabo_.v.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Xoolaha_Baydhabo_.v.jpg",
                "credit": "Mayow2020 · CC0",
                "caption": "Ganado en los alrededores de Baidoa.",
            },
        ],
    ),
    dict(
        n=10, name="Hargeisa · capital de Somalilandia y su mercado", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=9.5612168, lon=44.0669251,  # Google Maps: Hargeisa
        desc="Capital de Somalilandia, 1.334 metros de altitud y en torno a 1,2 millones de habitantes: es la base logística obligada de todo el norte. El monumento central es un MiG derribado, recuerdo de los bombardeos de finales de los ochenta que destruyeron cerca del 90 % de la ciudad. El mercado de cambistas, con pilas de chelines de Somalilandia sobre la acera, es la estampa clásica. Aquí se tramitan el permiso de turismo y la escolta SPU. EL VISADO Y LA MONEDA DE SOMALILANDIA NO SIRVEN EN SOMALIA FEDERAL.",
        dog_note="En el hotel y en el coche sí; en mercados, mezquitas y oficinas públicas no. El perro se considera impuro y conviene no exhibirlo.",
        visit={
            "why": "Es el único sitio del área somalí donde se puede caminar por la calle con relativa normalidad, y el centro administrativo donde se consiguen permisos y escoltas.",
            "see": "El MiG-17 sobre su pedestal, el mercado central y la calle de los cambistas, el mercado de camellos a las afueras y los talleres de talla de piedras.",
            "access": "Asfalto en buen estado desde Wajaale (frontera etíope, 60 km) y desde Berbera (unos 160 km). Los hoteles del centro (Oriental, Damal) tienen patio cerrado donde caben dos 4x4. El permiso de turismo se pide en el Ministerio de Turismo; la exención de escolta SPU se solicita en la jefatura de policía. El pin marca el monumento del MiG, en pleno centro.",
            "when": "Diciembre-febrero, la ventana fresca; entre mayo y septiembre hace calor y llueve de abril a septiembre (unos 400 mm al año).",
            "skip": "Si el FCDO endurece el aviso sobre Maroodi Jeex (hoy «todo viaje salvo esencial») o si hay tensión electoral, no entres.",
        },
        links=[
            {"label": "Hargeisa (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Hargeisa"},
            {"label": "Turismo en Somalilandia (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Tourism_in_Somaliland"},
            {"label": "FCDO · Somalia travel advice", "url": "https://www.gov.uk/foreign-travel-advice/somalia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Aerial_view_of_Hargeisa_DJI_0226.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Aerial_view_of_Hargeisa_DJI_0226.jpg",
                "credit": "Ridwan Bukhari · CC BY-SA 4.0",
                "caption": "Hargeisa desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Street_Market_Hargeisa,_Somaliland_(29322262370).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Street_Market_Hargeisa,_Somaliland_(29322262370).jpg",
                "credit": "Clay Gilliland from Chandler, U.S.A. · CC BY-SA 2.0",
                "caption": "Mercado callejero de Hargeisa.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Hargeisa_at_night.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Hargeisa_at_night.jpg",
                "credit": "Future brothers · CC BY-SA 4.0",
                "caption": "Hargeisa de noche.",
            },
        ],
    ),
    dict(
        n=11, name="Las Geel · las pinturas rupestres neolíticas", cat="Cultura", prio="Alta",
        dog="prohibido", time="medio día",
        lat=9.78091, lon=44.44364,  # Google Maps: Laas Geel (sin objeto en Google Maps; coordenada de la fuente)
        desc="Diez abrigos bajo una escarpadura, en las afueras rurales de Hargeisa, con la pintura rupestre mejor conservada del Cuerno de África: vacas de cuernos larguísimos con gualdrapas ceremoniales, figuras humanas, jirafas y cánidos. Un equipo arqueológico francés las documentó entre noviembre y diciembre de 2002 y se fechan entre 5.500 y 4.500 años de antigüedad, es decir, entre mediados del IV y mediados del III milenio a. C. NO ES PATRIMONIO DE LA HUMANIDAD: Somalia no tiene ningún bien inscrito y Las Geel tampoco figura en su lista indicativa, donde solo hay Bushbushle, Hobyo y el faro del Lido.",
        dog_note="Yacimiento con abrigos pintados y guía obligatorio; ningún sitio arqueológico de este tipo admite animales sueltos.",
        visit={
            "why": "Es el gran monumento del norte y una de las series de pintura neolítica mejor conservadas de África, con el pigmento casi intacto por el saliente de roca.",
            "see": "Diez alcobas con vacas policromas de cuernos en lira, figuras humanas con los brazos alzados, jirafas y perros; vistas del uadi desde la plataforma superior.",
            "access": "Desvío de la carretera asfaltada Hargeisa-Berbera y unos kilómetros de pista hasta el pie del cerro; a partir del control hay que subir a pie con guía. Relatos de viajeros citan unos 35 USD por persona con guía incluido, y guía obligatorio desde el control. El aparcamiento es un descampado al pie del cerro, suficiente para dos 4x4. El pin marca el yacimiento.",
            "when": "Primera hora de la mañana o última de la tarde: el abrigo se ve mejor con luz indirecta y a mediodía el calor es duro. Noviembre-marzo.",
            "skip": "Si no llevas permiso del Ministerio de Turismo de Hargeisa te darán la vuelta en el control; y si el aviso del FCDO sobre Maroodi Jeex sube de nivel, cancela.",
        },
        links=[
            {"label": "Laas Geel (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Laas_Geel"},
            {"label": "Turismo en Somalilandia (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Tourism_in_Somaliland"},
            {"label": "Guía práctica de Somalilandia (Against the Compass)", "url": "https://againstthecompass.com/en/travel-somaliland/"},
            {"label": "UNESCO · Somalia, Estado Parte y lista indicativa", "url": "https://whc.unesco.org/en/statesparties/so"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Laas_Geel,_2024.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Laas_Geel,_2024.jpg",
                "credit": "Mheidegger · CC BY 4.0",
                "caption": "Los abrigos pintados de Las Geel.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Laas_Geel_single_cow.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Laas_Geel_single_cow.jpg",
                "credit": "najeeb · CC BY-SA 2.0",
                "caption": "Una de las vacas pintadas de Las Geel.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Laas_Geel_Cave_with_Rock_Art,_September_2022.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Laas_Geel_Cave_with_Rock_Art,_September_2022.jpg",
                "credit": "Tinasimonrowe · CC BY-SA 4.0",
                "caption": "Interior de uno de los abrigos.",
            },
        ],
    ),
    dict(
        n=12, name="Berbera · el puerto del golfo de Adén y su casco otomano", cat="Costa", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=10.4347941, lon=45.0139904,  # Google Maps: Berbera
        desc="Único fondeadero abrigado de la orilla sur del golfo de Adén, Berbera fue capital de la Somalilandia británica hasta 1941 y conserva un casco antiguo muy deteriorado con huellas otomanas y coloniales. Desde 2016 DP World gestiona el puerto con una inversión de 442 millones de dólares y reparto 51 % para la compañía, 30 % para Somalilandia y 19 % para Etiopía. Exporta ganado, goma arábiga, incienso y mirra a Arabia Saudí y Yemen. EL CLIMA ES EL FILTRO: más de 40 °C durante unos cuatro meses de verano.",
        dog_note="En la playa y en el coche sí, pero el calor extremo lo hace inviable medio año; en el casco antiguo y las mezquitas, no.",
        visit={
            "why": "Es el puerto que explica la geopolítica actual del Cuerno: el corredor a Etiopía y el memorando de acceso al mar de enero de 2024 pasan por aquí.",
            "see": "El casco viejo con casas otomanas y coloniales arruinadas, el frente portuario de DP World, el mercado de ganado y playas largas de arena blanca al este de la ciudad.",
            "access": "Asfalto bueno desde Hargeisa (unos 160 km) por la carretera que pasa junto a Las Geel; la ruta Hargeisa-Berbera es una de las que suelen cubrirse con exención de escolta SPU. Hay espacio de sobra para aparcar dos 4x4 en el frente de playa. El pin marca el puerto; para la playa conviene fijar el establecimiento concreto.",
            "when": "Diciembre-febrero. De mayo a septiembre el calor pasa de 40 °C con humedad alta y la ciudad es inhabitable de día.",
            "skip": "Descártalo en verano sin más discusión, y en cualquier época si se reactiva la tensión por el memorando etíope-somalilandés.",
        },
        links=[
            {"label": "Berbera (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Berbera"},
            {"label": "Memorando Etiopía-Somalilandia de 2024 (Wikipedia)", "url": "https://en.wikipedia.org/wiki/2024_Ethiopia%E2%80%93Somaliland_memorandum_of_understanding"},
            {"label": "Guía práctica de Somalilandia (The Travel Camel)", "url": "https://www.thetravelcamel.com/somaliland-travel-guide/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Berbera,_Somaliland.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Berbera,_Somaliland.jpg",
                "credit": "Siirski · Public domain",
                "caption": "Berbera, en el golfo de Adén.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Berbera_city,_Somaliland.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Berbera_city,_Somaliland.jpg",
                "credit": "Siirski · Public domain",
                "caption": "El casco urbano de Berbera.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Berbera_shore.png?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Berbera_shore.png",
                "credit": "James Grant · CC BY-SA 4.0",
                "caption": "La orilla de Berbera.",
            },
        ],
    ),
    dict(
        n=13, name="Sheikh y el paso de la escarpa · el viejo camino a Berbera", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=9.9591667, lon=45.1841667,  # Google Maps: Shiikh (puerto de montaña)
        desc="Sheikh cuelga a 1.430 metros en los montes Golis, 71 kilómetros tierra adentro de Berbera y 60 de Burao: es el viejo camino de la escarpa que une el puerto con la meseta interior. Junto al pueblo están las ruinas medievales de Fardowsa, nodo comercial del siglo XV que decayó a comienzos del XVI con el veto chino a la exportación de 1521 y las incursiones portuguesas contra Zeila (1517) y Berbera (1518). El pueblo actual lo refundó en el siglo XIX Sayyid Adan Ahmad. Con 19 °C de media es el respiro térmico del norte.",
        dog_note="Tramo de montaña con paradas en mirador; el perro puede bajar atado, pero no entra en el pueblo ni en el recinto escolar.",
        visit={
            "why": "Es la carretera de montaña más espectacular de Somalilandia y, de paso, el yacimiento medieval de Fardowsa, que documenta la red comercial que unía el interior con el Índico.",
            "see": "Curvas de la escarpa con caída al mar, bosque abierto de acacias, el pueblo de Sheikh con su famosa escuela secundaria (dos presidentes de Somalilandia salieron de ella) y las ruinas de Fardowsa.",
            "access": "Carretera asfaltada pero estrecha y muy revirada entre Berbera y Sheikh, 71 km de subida continua; de Sheikh a Burao otros 60 km. Hay apartaderos donde caben dos 4x4. La exención de escolta SPU suele cubrir el eje Berbera-Sheikh-Burao, pero conviene confirmarlo en Hargeisa. El pin marca el pueblo de Sheikh.",
            "when": "Todo el año por la altitud; en verano es el refugio obligado frente a los 40 °C de Berbera. 466 mm de lluvia anual.",
            "skip": "Con lluvia fuerte la escarpa da desprendimientos; y de noche no se conduce ese tramo.",
        },
        links=[
            {"label": "Sheikh, Somalilandia (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Sheikh,_Somaliland"},
            {"label": "Guía práctica de Somalilandia (The Travel Camel)", "url": "https://www.thetravelcamel.com/somaliland-travel-guide/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Somaliland,_Sheikh,_aerial_view_(01).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Somaliland,_Sheikh,_aerial_view_(01).jpg",
                "credit": "Mubarik Mario · Public domain",
                "caption": "Sheikh, en lo alto de la escarpa.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sheikh_mountains,_Togdheer,_Sheikh,_Somaliland.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sheikh_mountains,_Togdheer,_Sheikh,_Somaliland.jpg",
                "credit": "Siirski · Public domain",
                "caption": "Los montes de Sheikh.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Somaliland,_Golis_mountains,_road.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Somaliland,_Golis_mountains,_road.jpg",
                "credit": "Abdillahi M. Ali · Public domain",
                "caption": "La carretera por los montes Golis.",
            },
        ],
    ),
    dict(
        n=14, name="Zeila · la ciudad histórica del golfo de Tadjoura", cat="Costa", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=11.3536874, lon=43.4753136,  # Google Maps: Zeila
        desc="Zeila es con casi total seguridad el Avalites de los textos grecorromanos: puerto desde el siglo I, capital del reino de Adal en el IX y sede del sultanato de Ifat en el XIII, con la mezquita de al-Qiblatayn como la más antigua de la ciudad. Se asienta en una lengua de arena con arrecifes, manglares y el archipiélago de Saad ad-Din enfrente. El Imperio otomano la controló nominalmente del XVI al XIX y acabó en la Somalilandia británica tras el acuerdo anglofrancés de 1888. Quedó destrozada en la guerra civil y se ha rehecho a medias con remesas.",
        dog_note="Pueblo costero muy conservador; el perro puede ir en el vehículo y en la playa desierta, nunca en el casco ni en las mezquitas.",
        visit={
            "why": "Es la ciudad histórica más antigua del área somalí y el punto donde el islam entró en el Cuerno de África; el conjunto de ruinas y mezquitas no tiene equivalente.",
            "see": "Minaretes y mezquitas en ruinas, la de al-Qiblatayn, restos otomanos y coloniales, manglares, arrecife y las islas de Saad ad-Din frente a la costa.",
            "access": "Está en Awdal, junto a la frontera de Yibuti en Loyada; los relatos de viajeros describen unos 300 km de desierto y arena desde el paso de Loyada hasta Borama, con 4x4 obligatorio y carreteras en mal estado. Hay alojamiento muy básico (en torno a 20 USD la noche). Aparcamiento improvisado en la arena. El pin marca el núcleo de Zeila.",
            "when": "Diciembre-febrero; de mayo a septiembre el calor costero es extremo.",
            "skip": "Sin 4x4 alto y sin combustible de sobra no se entra; y si el aviso del FCDO sobre Awdal empeora, se cancela.",
        },
        links=[
            {"label": "Zeila (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Zeila"},
            {"label": "Turismo en Somalilandia (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Tourism_in_Somaliland"},
            {"label": "Guía práctica de Somalilandia (Against the Compass)", "url": "https://againstthecompass.com/en/travel-somaliland/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Zeila_city.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Zeila_city.jpg",
                "credit": "Seepsimon · CC BY-SA 4.0",
                "caption": "Zeila, en el golfo de Tadjoura.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Zeila_Mosque.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Zeila_Mosque.jpg",
                "credit": "Walter Callens · CC BY 2.0",
                "caption": "Una de las mezquitas de Zeila.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Zeila_awdal.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Zeila_awdal.jpg",
                "credit": "Abdihakimper · CC BY-SA 4.0",
                "caption": "La costa de Zeila.",
            },
        ],
    ),
    dict(
        n=15, name="Montes Cal Madow y Daallo · el bosque de niebla del norte", cat="Naturaleza", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=10.6149654, lon=47.3657603,  # Google Maps: Daallo Park
        desc="La cadena de Cal Madow levanta una muralla sobre el golfo de Adén y culmina en el Shimbiris, 2.460 metros, techo de Somalilandia. En la escarpadura de caliza y yeso de Daallo sobrevive un bosque de niebla con enebros (Juniperus procera) y Buxus hildebrandtii: unas 1.000 especies vegetales, de las que 200 solo existen en estas montañas, más el antílope beira y el pardillo de Warsangli. BirdLife lo considera Área Importante para las Aves. NO HAY PISTA HASTA LA CUMBRE: el Shimbiris se sube a pie y se puede acampar.",
        dog_note="Reserva con fauna endémica frágil (beira, pardillo de Warsangli) y ascensiones a pie de varias horas sin agua garantizada.",
        visit={
            "why": "Es el ecosistema más singular del Cuerno de África y, con diferencia, el mejor paisaje de toda la ficha: bosque de niebla a 2.000 metros sobre un desierto costero.",
            "see": "Enebros milenarios (hay árboles de más de mil años en el parque), la caída de la escarpa hacia el mar desde el borde de Daallo, incienso silvestre y aves endémicas.",
            "access": "Erigavo (1.786 m) es la base; desde Burao son unos 400 km de pista larga y dura, y desde ahí unas decenas de kilómetros hasta el borde de Daallo. Esta zona está fuera de las rutas cubiertas por la exención de escolta: exige SPU armada. Acampada posible en la montaña. El pin marca el bosque de Daallo, junto a Erigavo.",
            "when": "La cumbre recibe unos 650-850 mm al año con niebla y lluvias de invierno; octubre-marzo es lo más practicable.",
            "skip": "Descártalo si no consigues la escolta SPU o si hay tensión clánica en el Sanaag, disputado entre Somalilandia y Puntlandia.",
        },
        links=[
            {"label": "Cal Madow (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Cal_Madow"},
            {"label": "Monte Daallo (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Daallo_Mountain"},
            {"label": "Shimbiris (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Shimbiris"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Daallo_Mountain_-_Erigavo,_Sanaag_Region,_Somaliland_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Daallo_Mountain_-_Erigavo,_Sanaag_Region,_Somaliland_01.jpg",
                "credit": "Abukar Musa · CC BY-SA 4.0",
                "caption": "El escarpe de Daallo, sobre el golfo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Daallo_Mountain_-_Erigavo,_Sanaag_Region,_Somaliland_03.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Daallo_Mountain_-_Erigavo,_Sanaag_Region,_Somaliland_03.jpg",
                "credit": "Abukar Musa · CC BY-SA 4.0",
                "caption": "Bosque de niebla en Daallo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Daallo_Mountain_-_Erigavo,_Sanaag_Region,_Somaliland_06.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Daallo_Mountain_-_Erigavo,_Sanaag_Region,_Somaliland_06.jpg",
                "credit": "Abukar Musa · CC BY-SA 4.0",
                "caption": "El Cal Madow desde Daallo.",
            },
        ],
    ),
    dict(
        n=16, name="Bosaso y Puntlandia · el puerto del nordeste", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=11.2892378, lon=49.181378,  # Google Maps: bosaso seaport
        desc="Bosaso es el gran puerto del nordeste y el motor comercial de Puntlandia: ganado, pescado, incienso, oro y materiales de construcción, en la misma costa que abastecía el antiguo comercio del país de Punt. Tiene aeropuerto internacional, el Bender Qassim, y aquí arranca la carretera de 750 kilómetros que baja hacia el sur. Desierto cálido con veranos por encima de 40 °C. Es también el embarcadero del tráfico de migrantes hacia Yemen y la retaguardia del repunte pirata del golfo de Adén desde 2023. LOS PERMISOS DE PUNTLANDIA NO VALEN EN SOMALILANDIA.",
        dog_note="Ciudad portuaria con calor extremo, riesgo de secuestro y hoteles bajo control de seguridad; no hay alojamiento que lo contemple.",
        visit={
            "why": "Es la puerta del Cuerno hacia Arabia y el mejor sitio para entender la economía del incienso y del ganado de Puntlandia.",
            "see": "El puerto y sus dhows, el mercado de incienso y la lonja de pescado; nada monumental, la ciudad es funcional.",
            "access": "Carretera norte-sur asfaltada a trechos hasta Garowe (unos 205 km) y un tramo pavimentado de 5,9 km hasta el puerto; entrada normal por el aeropuerto Bender Qassim. Alojamiento en hoteles con seguridad privada. Los permisos y escoltas se gestionan con la administración de Puntlandia, no con Hargeisa. El pin marca el puerto.",
            "when": "Noviembre-febrero. En verano es inviable por el calor.",
            "skip": "Descártalo: riesgo alto de secuestro de extranjeros y base de retaguardia del repunte pirata desde 2023-2024.",
        },
        links=[
            {"label": "Bosaso (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bosaso"},
            {"label": "ISS · El regreso de los piratas somalíes", "url": "https://issafrica.org/iss-today/as-somali-pirates-make-a-comeback-collaboration-is-key"},
            {"label": "FCDO · Somalia travel advice", "url": "https://www.gov.uk/foreign-travel-advice/somalia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bosaso_Seaport.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bosaso_Seaport.jpg",
                "credit": "Omar Dr Abdulkadir · CC BY-SA 4.0",
                "caption": "El puerto de Bosaso.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bosaso,_Somalia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bosaso,_Somalia.jpg",
                "credit": "Omar Dr Abdulkadir · CC BY-SA 4.0",
                "caption": "Bosaso, en el nordeste.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Karin,_Bosaso,_Somalia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Karin,_Bosaso,_Somalia.jpg",
                "credit": "Omar Abdulkadir · CC BY-SA 2.0",
                "caption": "La costa de Karin, junto a Bosaso.",
            },
        ],
    ),
    dict(
        n=17, name="Garowe · la capital administrativa de Puntlandia", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=8.4070782, lon=48.4875873,  # Google Maps: Garowe
        desc="Capital administrativa de Puntlandia, Garowe se asienta a 467 metros en el valle del Nugal, rodeada de altiplanos que suben hasta 500-1.000 metros. Concentra el parlamento regional, el palacio presidencial, los ministerios y la Puntland State University. El aeropuerto internacional, abierto en 2010, queda a unos 12 kilómetros del centro. Por la carretera norte-sur son 205 kilómetros hasta Bosaso y 216 hasta Galkayo. Clima de desierto cálido: 41 °C en verano y solo 133 mm de lluvia al año. ES DONDE SE TRAMITAN PERMISOS Y ESCOLTAS DE PUNTLANDIA.",
        dog_note="Capital administrativa sin infraestructura turística; los hoteles con seguridad no admiten animales.",
        visit={
            "why": "Es el centro de decisión de Puntlandia y la parada logística obligada de cualquier movimiento por el nordeste.",
            "see": "El conjunto institucional, el campus universitario y el paisaje del valle del Nugal con los altiplanos al fondo; es una ciudad joven, sin casco histórico.",
            "access": "Está sobre la carretera norte-sur, asfaltada a trechos; 205 km a Bosaso y 216 a Galkayo. Aeropuerto internacional a 12 km. Hoteles con recinto vallado donde caben dos vehículos. Cualquier salida de la ciudad requiere escolta autorizada por la administración de Puntlandia. El pin marca el centro de Garowe.",
            "when": "Noviembre-febrero; los picos de 41 °C del verano desaconsejan cualquier otra fecha.",
            "skip": "Descártalo mientras el MAEC mantenga el nivel actual; y en concreto si hay tensión con Mogadiscio o con las milicias del Sool.",
        },
        links=[
            {"label": "Garowe (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Garoowe"},
            {"label": "Recomendaciones de viaje MAEC · Somalia", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Somalia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Garowe.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Garowe.jpg",
                "credit": "Omar Dr Abdulkadir · CC BY-SA 4.0",
                "caption": "Garowe, capital administrativa de Puntlandia.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Puntland_Presidential_House,_2019.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Puntland_Presidential_House,_2019.jpg",
                "credit": "Abdullahi Mohamoud Ali · CC BY 4.0",
                "caption": "La casa presidencial de Puntlandia.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Garowe_Overview.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Garowe_Overview.jpg",
                "credit": "Omar Abdulkadir · Public domain",
                "caption": "Vista general de Garowe.",
            },
        ],
    ),
    dict(
        n=18, name="Las Anod y el Sool · la frontera disputada", cat="Ciudad · servicios", prio="Media",
        dog="prohibido", time="medio día",
        lat=8.476057, lon=47.3567199,  # Google Maps: Las Anod
        desc="Las Anod, capital del Sool, es el nudo del conflicto que más ha movido el mapa del norte. Está a 691 metros en el valle del Nugal, sobre las rutas comerciales entre Somalilandia y Puntlandia, y es el centro político del clan Dhulbahante. Somalilandia la ocupó en 2007 y la perdió en agosto de 2023 frente a las fuerzas de SSC-Khatumo; el Consejo de Derechos Humanos de la ONU contabilizó más de 185.000 desplazados, el 89 % mujeres y niños. Ni Hargeisa la controla ni está plenamente integrada en la federación: ZONA VETADA.",
        dog_note="Zona de conflicto abierto desde 2023, con desplazamiento masivo; no es un lugar al que se lleve a nadie, menos aún a un animal.",
        visit={
            "why": "Documentalmente importa porque explica por qué el mapa de Somalilandia que circula ya no corresponde a lo que controla: sin entender Las Anod no se entiende el norte.",
            "see": "Ciudad de mercado del valle del Nugal, sin patrimonio destacable; lo relevante es el contexto político, no lo visitable.",
            "access": "Está sobre el eje que une Burao con Garowe, asfaltado a trechos. No es una ruta cubierta por ninguna exención de escolta y las líneas de control cambian. Ni el permiso de Somalilandia ni el de Puntlandia sirven aquí. Sin alojamiento ni servicios utilizables. El pin marca el centro de Laascaanood.",
            "when": "Ninguno: no hay ventana recomendable.",
            "skip": "Descártalo siempre mientras no haya un acuerdo político estable sobre el Sool.",
        },
        links=[
            {"label": "Las Anod (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Las_Anod"},
            {"label": "FCDO · Somalia travel advice", "url": "https://www.gov.uk/foreign-travel-advice/somalia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Las_anod_aerial_panorama_east.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Las_anod_aerial_panorama_east.jpg",
                "credit": "Danesrmithpl8 · Public domain",
                "caption": "Las Anod desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Las_Anod,_night_view.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Las_Anod,_night_view.jpg",
                "credit": "Siirski · CC BY-SA 4.0",
                "caption": "Las Anod de noche.",
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
    ("Aeropuerto Internacional Aden Adde (Mogadiscio)", "Frontera", 2.0176418, 45.3038042,  # Google Maps: Aeropuerto Internacional Aden Adde
     "Única vía practicable a Somalia federal. eTAS previa obligatoria (etas.gov.so). Recinto fortificado MIA/Halane; salir a la ciudad exige convoy con escolta armada. Morteros disparados hacia el aeropuerto en febrero de 2025. Pin comprobado en Google Maps («Aeropuerto Internacional Aden Adde»)."),
    ("Aeropuerto Internacional Egal (Hargeisa, Somalilandia)", "Frontera", 9.5180099, 44.0836786,  # Google Maps: Aeropuerto Internacional de Hargeisa
     "Entrada aérea a Somalilandia. Visado somalilandés a la llegada; los visados emitidos por Somalia no son válidos desde el 10 de noviembre de 2025. Pin comprobado en Google Maps («Aeropuerto Internacional de Hargeisa»)."),
    ("Paso fronterizo de Tog Wajaale (Etiopía–Somalilandia)", "Frontera", 9.6030127, 43.3415357,  # Google Maps: Wajale
     "Entrada real a Somalilandia por tierra y principal puerta de mercancías del país. Abierto de 06:00 a 18:00. Visado somalilandés previo obligatorio; no hay visado a la llegada. Trámites de 30 a 90 minutos. Pin comprobado en Google Maps («Wajale»)."),
    ("Paso fronterizo de Loyada (Yibuti–Somalilandia)", "Frontera", 11.4615657, 43.2500923,  # Google Maps: Loyada (lado yibutiano)
     "Único paso oficial entre Yibuti y Somalilandia, a 25 km de la capital yibutiana. Usado por circuitos comerciales en 2026. Cierres políticos repetidos desde 1999; estado actual por confirmar. Pin comprobado en Google Maps («Loyada (lado yibutiano)»)."),
    ("Puerto de Berbera (Somalilandia)", "Frontera", 10.4388783, 44.9995722,  # Google Maps: Berbera Port
     "Puerto ampliado por DP World (442 M USD; DP World 51 %, Somalilandia 30 %, Etiopía 19 %), muelle de 1.000 m y hasta 2 M TEU. Tráfico de carga, no de pasajeros: no es vía de entrada para un vehículo particular. Pin comprobado en Google Maps («Berbera Port»)."),
    ("Embajada de España en Nairobi (competente para Somalia)", "Consular", -1.2976459, 36.8131933,  # Google Maps: Embajada de España en Kenia
     "NCBA Building, 3.er piso, Nairobi (Kenia). Embajador Jaime Moreno Bau. Tel. (+254) 20 272 02 22/3/4/5. Emergencia consular (+254) 733 631 144. emb.nairobi@maec.es. España NO tiene embajada residente en Somalia. Pin comprobado en Google Maps («Embajada de España en Kenia»)."),
    ("Hargeisa Group Hospital (Somalilandia)", "Hospital", 9.5616576, 44.0558192,  # Google Maps: Hargeisa Group Hospital
     "Mayor hospital público de Somalilandia, 400 camas, fundado en 1953. Maternidad, urgencias, cirugía, pediatría y nefrología. Pin comprobado en Google Maps («Hargeisa Group Hospital»)."),
    ("Hospital Erdoğan (Digfer), Mogadiscio", "Hospital", 2.042835, 45.3044508,  # Google Maps: Hospital Recep Tayyip Erdoğan (Mogadiscio)
     "200 camas, 4 quirófanos, 12 camas de UCI, rehabilitado por la agencia turca TIKA. Referencia habitual para extranjeros en Mogadiscio. El MAEC describe la sanidad del país como muy escasa y deplorable. Pin comprobado en Google Maps («Hospital Recep Tayyip Erdoğan (Mogadiscio)»)."),
    ("Combustible en Hargeisa", "Combustible", 9.5675269, 44.1299513,  # Google Maps: Somaliland fuel station (Hargeisa)
     "Estaciones operativas en la capital. Referencia nacional a 5 de marzo de 2026: gasolina y gasóleo a 750 SoSh/litro (1,31 USD). Pago en chelines, dólares o dinero móvil (Zaad). Fuera de la ciudad, suministro con bidones. Pin comprobado en Google Maps («Somaliland fuel station (Hargeisa)»)."),
    ("Agua en Hargeisa", "Agua potable", 9.5602517, 44.0515209,  # Google Maps: Water Agency (Hargeisa)
     "Agua de red no potable. Solo agua embotellada o suministro de hoteles y compounds, con cobro. País en emergencia de sequía 2025-2026: hasta 1 USD por bidón de 20 litros. No hay puntos de agua documentados para overlanders. Pin comprobado en Google Maps («Water Agency (Hargeisa)»)."),
]

DRONE_CALLOUT = ("danger", "DRONES: NO LLEVARLOS",
                 "Los drones no están permitidos a los visitantes extranjeros. La Somali Civil Aviation Authority declara que las operaciones con dron no están reguladas en Somalia y remite a las recomendaciones de la OACI, lo que en la práctica deja el asunto en manos de la policía y del ejército. En un país donde en enero de 2025 se derribaron dos drones sobre Villa Somalia, volar un aparato cerca de instalaciones oficiales, aeropuertos o convoyes se interpreta como reconocimiento hostil. El resultado esperable es confiscación, detención y un problema consular que España no puede resolver desde Nairobi.")

STARLINK_CALLOUT = ("warn", "STARLINK: ACTIVO EN SOMALIA, INCIERTO EN SOMALILANDIA",
                    "La National Communications Authority somalí licenció a Starlink el 14 de abril de 2025 y el servicio arrancó comercialmente el 5 de agosto de 2025, con un kit de unos 390 USD y una cuota residencial de unos 70 USD al mes. Lo que no está verificado es su cobertura efectiva en Somalilandia y Puntlandia, que tienen autoridades de telecomunicaciones propias y, en el caso de Hargeisa, un pulso abierto con Mogadiscio sobre soberanía del espacio aéreo. Añádase que una antena de satélite en un vehículo llama la atención en cualquier control armado.")

DOG_MATRIX = [
    ("Somalia federal (Mogadiscio, Baidoa, Kismayo)", "no recomendado", "El perro no viaja. Zona de escolta armada y alojamiento fortificado; ningún recinto de seguridad admite animales."),
    ("Somalilandia (Hargeisa, Berbera, Las Geel)", "por confirmar", "Sin requisitos oficiales publicados por su Ministry of Livestock and Rural Development. Si algún día se fuera, se iría sin perro y con residencia canina en España."),
    ("Puntlandia (Garowe, Bosaso)", "no recomendado", "Permisos propios, ruptura con el gobierno federal desde 2024, presencia del Estado Islámico y piratería. Descartado sin matices."),
    ("Pasos terrestres (Tog Wajaale, Loyada)", "por confirmar", "No hay constancia de control veterinario ni de procedimiento para mascotas. Riesgo real de bloqueo, retención indefinida o sacrificio en frontera."),
    ("Vuelta a la UE desde Somalia", "permitido con condiciones", "Vía A del Reg. (UE) 2026/131: microchip, vacuna, titulación ≥0,5 UI/ml y 90 días de espera. Sin la analítica hecha ANTES de salir de la UE, no hay retorno."),
    ("Alojamiento fortificado / compounds", "prohibido", "Los recintos de seguridad de Mogadiscio y del aeropuerto (MIA/Halane) no admiten animales. Sin alternativa posible."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Somalia (Ministerio de Asuntos Exteriores, consultado en septiembre de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Somalia"),
    ("MAEC · Ficha País Somalia (Oficina de Información Diplomática, julio de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/SOMALIA_FICHA%20PAIS.pdf"),
    ("FCDO · Somalia travel advice: safety and security (Gobierno del Reino Unido, 4 de junio de 2026)", "https://www.gov.uk/foreign-travel-advice/somalia/safety-and-security"),
    ("FCDO · Somalia travel advice: entry requirements (Gobierno del Reino Unido, 2026)", "https://www.gov.uk/foreign-travel-advice/somalia/entry-requirements"),
    ("Government of Canada · Somalia travel advice and advisories (9 de septiembre de 2026)", "https://travel.gc.ca/destinations/somalia"),
    ("NaTHNaC TravelHealthPro · Somalia (actualizado en enero de 2026)", "https://travelhealthpro.org.uk/countries/somalia"),
    ("carnetdepassage.org · Somalia (AIT/FIA, consultado en septiembre de 2026)", "https://www.carnetdepassage.org/country/somalia"),
    ("Drone Laws · Drone Laws in Somalia (21 de enero de 2026)", "https://drone-laws.com/drone-laws-in-somalia/"),
    ("EUR-Lex · Reglamento de Ejecución (UE) 2026/636, de 20 de marzo de 2026, listas de terceros países (aplicable desde el 22 de abril de 2026)", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600636"),
    ("EUR-Lex · Reglamento Delegado (UE) 2026/131, de 20 de enero de 2026, desplazamientos sin ánimo comercial de animales de compañía", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600131"),
    ("MAPA · Viajar con la mascota: perros, gatos y hurones (Ministerio de Agricultura, Pesca y Alimentación, consultado en 2026)", "https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones"),
    ("OFESAUTO · Carta Verde y sistema de corresponsales (consultado en septiembre de 2026)", "https://www.ofesauto.es/carta-verde/"),
    ("Ministry of Livestock, Forestry and Range (Gobierno Federal de Somalia) · Contact us", "https://molfr.gov.so/contact-us/"),
    ("Wikipedia · Ministry of Livestock (Somaliland) (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Ministry_of_Livestock_(Somaliland)"),
    ("Wikipedia · Somaliland (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Somaliland"),
    ("Wikipedia · Puntland (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Puntland"),
    ("Wikipedia · Tourism in Somaliland (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Tourism_in_Somaliland"),
    ("Wikipedia · Las Anod conflict (2023) (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Las_Anod_conflict_(2023)"),
    ("Wikipedia · 2024 Ethiopia–Somaliland memorandum of understanding (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2024_Ethiopia%E2%80%93Somaliland_memorandum_of_understanding"),
    ("Wikipedia · 2025 Shabelle offensive (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2025_Shabelle_offensive"),
    ("Wikipedia · 2025 timeline of the Somali Civil War (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2025_timeline_of_the_Somali_Civil_War"),
    ("Wikipedia · 2025 in Somaliland (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2025_in_Somaliland"),
    ("Wikipedia · 2025 in piracy (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2025_in_piracy"),
    ("Wikipedia · Tog Wajaale (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Tog_Wajaale"),
    ("Wikipedia · Loyada (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Loyada"),
    ("Wikipedia · Berbera (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Berbera"),
    ("Wikipedia · Hargeisa (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Hargeisa"),
    ("Wikipedia · Hargeisa International Airport (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Hargeisa_International_Airport"),
    ("Wikipedia · Hargeisa Group Hospital (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Hargeisa_Group_Hospital"),
    ("Wikipedia · Mogadishu (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Mogadishu"),
    ("Wikipedia · Aden Adde International Airport (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Aden_Adde_International_Airport"),
    ("Wikipedia · Erdoğan Hospital, Mogadiscio (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Erdo%C4%9Fan_Hospital"),
    ("Wikipedia · Aamin Ambulance (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Aamin_Ambulance"),
    ("Wikipedia · Garowe (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Garowe"),
    ("ReliefWeb / CICR · Somalia: Somali Red Crescent launches toll-free number (446) for emergency services", "https://reliefweb.int/report/somalia/somalia-somali-red-crescent-launches-toll-free-number-446-emergency-services"),
    ("Africanews · Somaliland rejects visas issued by Somalia and tightens control over its airspace (11 de noviembre de 2025)", "https://www.africanews.com/2025/11/11/somaliland-rejects-visas-issued-by-somalia-and-tightens-control-over-its-airpsace/"),
    ("Visa Mundi · In Somalia, a leak in the visa system precipitates the switch to eTAS (migración a eTAS el 27 de noviembre de 2025)", "https://www.visamundi.co/en/blog/in-somalia-a-leak-in-the-visa-system-precipitates-the-passage-to-letas/"),
    ("Things to do in Somalia · Somalia visa and entry requirements (2026)", "https://thingstodoinsomalia.com/entry-requirements/"),
    ("Connecting Africa · Starlink gets green light in Somalia (licencia de la NCA, 14 de abril de 2025)", "https://www.connectingafrica.com/connectivity/starlink-gets-greenlight-in-somalia"),
    ("Space in Africa · Starlink's high-speed internet goes live in Somalia (5 de agosto de 2025)", "https://spaceinafrica.com/2025/08/05/starlinks-high-speed-internet-goes-live-in-somalia/"),
    ("AfroFuel · Fuel prices in Somalia: petrol, diesel and LPG (datos de 5 de marzo de 2026)", "https://afrotools.com/tools/fuel-tracker/somalia/"),
    ("OCHA · Somalia: severe water crisis unravels as sources dry up (Naciones Unidas, diciembre de 2024)", "https://www.unocha.org/news/somalia-severe-water-crisis-unravels-sources-dry"),
    ("Gard · Piracy: a persistent threat to seafarers (12 de febrero de 2025)", "https://gard.no/en/insights/piracy-a-persistent-threat-to-seafarers/"),
    ("Skuld · Somali piracy resurgence: a new era of risk in the Indian Ocean (7 de noviembre de 2025)", "https://www.skuld.com/topics/port/piracy/somali-piracy-resurgence-a-new-era-of-risk-in-the-indian-ocean/"),
    ("Against the Compass · Tips and how to travel to Somaliland (actualizado el 30 de agosto de 2026)", "https://againstthecompass.com/en/travel-somaliland/"),
    ("Border Crossing Hub · Tog Wajaale (Somaliland) / Togo Wuchale (Ethiopia) border crossing", "https://bordercrossinghub.com/tog-wajaale-somaliland-togo-wuchale-ethiopia-side-border-crossing/"),
    ("The Candy Trail · Laas Geel: the colorful prehistoric cave art of Somaliland (viaje de 2013, publicado en 2018)", "https://www.thecandytrail.com/laas-geel-cave-paintings-somaliland/"),
    ("The Travel Camel · Somaliland travel guide", "https://www.thetravelcamel.com/somaliland-travel-guide/"),
    ("Bradt Somaliland Travel News · Police escorts (entradas de 2013 y 2017)", "https://bradtsomaliland.wordpress.com/category/police-escorts/"),
    ("Kumakonda · Trip to Djibouti, Somaliland and Somalia (Mogadishu), salida de octubre de 2026, 3.600 € por persona", "https://kumakonda.com/trip/trip-to-djibouti-somaliland-somalia/"),
    ("Untamed Borders · Somaliland destinations (circuitos por carretera desde Yibuti, salidas de 2025)", "https://untamedborders.com/destinations/somaliland/"),
    ("Visit Horn Africa · Travel with the SPU (Somaliland Special Police)", "https://visithornafrica.com/travel-with-the-spu/"),
    ("Hamar Weyne (Wikipedia)", "https://en.wikipedia.org/wiki/Hamar_Weyne,_Mogadishu"),
    ("Puerto de Mogadiscio (Wikipedia)", "https://en.wikipedia.org/wiki/Port_of_Mogadishu"),
    ("Mezquita de Fakr ad-Din (Wikipedia)", "https://en.wikipedia.org/wiki/Fakr_ad-Din_Mosque"),
    ("Lido Beach (Wikipedia)", "https://en.wikipedia.org/wiki/Lido_Beach,_Mogadishu"),
    ("UNESCO · Somalia, Estado Parte y lista indicativa", "https://whc.unesco.org/en/statesparties/so"),
    ("Catedral de Mogadiscio (Wikipedia)", "https://en.wikipedia.org/wiki/Mogadishu_Cathedral"),
    ("Bakaara Market (Wikipedia)", "https://en.wikipedia.org/wiki/Bakaara_Market"),
    ("Mercado de Bakaara (Wikipedia en español)", "https://es.wikipedia.org/wiki/Mercado_de_Bakaara"),
    ("Howlwadaag, Mogadiscio (Wikipedia)", "https://en.wikipedia.org/wiki/Howlwadaag,_Mogadishu"),
    ("Afgooye (Wikipedia)", "https://en.wikipedia.org/wiki/Afgooye"),
    ("Al Shabab (Wikipedia)", "https://en.wikipedia.org/wiki/Al-Shabaab_(militant_group)"),
    ("Merca (Wikipedia)", "https://en.wikipedia.org/wiki/Merca"),
    ("FCDO · Somalia travel advice", "https://www.gov.uk/foreign-travel-advice/somalia"),
    ("Barawa (Wikipedia)", "https://en.wikipedia.org/wiki/Baraawe"),
    ("Brava, Somalia (Wikipedia en italiano)", "https://it.wikipedia.org/wiki/Brava_(Somalia)"),
    ("Kismayo (Wikipedia)", "https://en.wikipedia.org/wiki/Kismayo"),
    ("Kismaayo (Wikipedia en español)", "https://es.wikipedia.org/wiki/Kismayo"),
    ("Baidoa (Wikipedia)", "https://en.wikipedia.org/wiki/Baidoa"),
    ("Laas Geel (Wikipedia)", "https://en.wikipedia.org/wiki/Laas_Geel"),
    ("Sheikh, Somalilandia (Wikipedia)", "https://en.wikipedia.org/wiki/Sheikh,_Somaliland"),
    ("Zeila (Wikipedia)", "https://en.wikipedia.org/wiki/Zeila"),
    ("Cal Madow (Wikipedia)", "https://en.wikipedia.org/wiki/Cal_Madow"),
    ("Monte Daallo (Wikipedia)", "https://en.wikipedia.org/wiki/Daallo_Mountain"),
    ("Shimbiris (Wikipedia)", "https://en.wikipedia.org/wiki/Shimbiris"),
    ("Bosaso (Wikipedia)", "https://en.wikipedia.org/wiki/Bosaso"),
    ("ISS · El regreso de los piratas somalíes", "https://issafrica.org/iss-today/as-somali-pirates-make-a-comeback-collaboration-is-key"),
    ("Garowe (Wikipedia)", "https://en.wikipedia.org/wiki/Garoowe"),
    ("Las Anod (Wikipedia)", "https://en.wikipedia.org/wiki/Las_Anod"),
]

# Norte · Zeila–Hargeisa–Berbera–Sheikh–Erigavo–Bosaso (Somalilandia y Puntlandia)
CORRIDOR = [
    (11.35369, 43.47531),
    (9.93583, 43.18417),
    (9.60139, 43.33611),
    (9.56122, 44.06693),
    (9.78091, 44.44364),
    (10.43479, 45.01399),
    (9.95917, 45.18417),
    (9.52789, 45.5345),
    (10.61497, 47.36576),
    (10.73583, 47.245),
    (11.28924, 49.18138),
    (8.40708, 48.48759),
    (8.47606, 47.35672),
]

# Sur federal · Mogadiscio–Afgooye–Baidoa–Merca–Barawa–Kismayo (VETADO)
CORRIDOR_ALT = [
    (2.03588, 45.34162),
    (2.14262, 45.11672),
    (3.10438, 43.63276),
    (2.14262, 45.11672),
    (1.71747, 44.76861),
    (1.11501, 44.03143),
    (-0.38811, 42.54268),
]

HISTORIA_RESUMEN = "Somalia es el país africano con la advertencia más dura del Ministerio de Asuntos Exteriores español, que desaconseja el viaje bajo cualquier circunstancia. Heredera de los sultanatos de Adal, Ajuran y Geledi y de dos colonizaciones distintas, la británica en el norte y la italiana en el sur, se unificó en 1960 y se desintegró en 1991 con la caída de Siad Barre. Desde entonces conviven tres realidades: el Estado federal de Mogadiscio, acosado por Al Shabab; Somalilandia, independiente de hecho desde 1991 y estable; y Puntlandia, autónoma en el nordeste. Los visados y los permisos de cada una son distintos y no se aceptan entre sí. La ficha es informativa: la ruta de 2027 no entra en el país."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>La costa somalí figura entre los espacios comerciales más antiguos del océano Índico. La mayoría de los especialistas sitúan aquí el <em>País de Punt</em> que prosperó en la Edad del Bronce, y en época clásica la franja litoral estaba jalonada de ciudades-Estado mercantiles —Opone, Malao, Mosylon, Mundus, Sarapion, Essina y Tabae— que comerciaban con Egipto, Arabia y el Mediterráneo. Tierra adentro, el conjunto rupestre de Laas Geel, cerca de Hargeisa, conserva pinturas de vacuno doméstico de hace entre 5.500 y 4.500 años.</p><p>El islam llegó pronto por el mar Rojo y dio forma a una sucesión de sultanatos. El de <strong>Adal</strong> alcanzó su cénit con el imán Ahmad ibn Ibrahim al-Ghazi, llamado <em>Gurey</em>, «el zurdo», que hacia 1527 invadió Abisinia; una fuerza conjunta portuguesa y etíope lo derrotó y lo mató en la batalla de Wayna Daga, el 21 de febrero de 1543. Después vino la «era de los Ajuran», con los puertos de Mogadiscio, Merca, Barawa y Hobyo volcados en el comercio exterior. En el sur, el sultanato de <strong>Geledi</strong> vivió su edad de oro con Yusuf Mahamud Ibrahim, tercer sultán de la casa Gobroon, cuyo ejército venció en 1843. En el nordeste dominaban los sultanatos majeerteen y de Hobyo.</p>"),
    ("Colonización",
     "<p>El reparto europeo de finales del siglo XIX troceó el territorio somalí en cuatro. Gran Bretaña estableció el <strong>protectorado de la Somalilandia británica</strong> en el norte, Italia organizó la <strong>Somalia italiana</strong> en el sur y el centro, Francia se quedó con la Somalilandia francesa —el actual Yibuti— y Etiopía incorporó el Ogadén. Esa fractura explica casi todo lo que vino después: dos administraciones, dos lenguas europeas y dos culturas jurídicas en un mismo pueblo.</p><p>La resistencia más larga fue el movimiento derviche de Sayyid Mohammed Abdullah Hassan, que combatió entre 1899 y 1920 y solo se desmoronó cuando los británicos recurrieron al bombardeo aéreo intensivo. Italia tardó todavía más en someter el nordeste: la campaña contra el sultanato de Hobyo arrancó en octubre de 1925 y se topó en noviembre con la rebelión de Omar Samatar, mientras la resistencia majeerteen de Hersi Boqor se prolongó hasta finales de 1927. Tras la Segunda Guerra Mundial, el sur pasó a ser en 1950 un territorio en fideicomiso de Naciones Unidas bajo administración italiana, con la promesa explícita de independencia en diez años. De aquella etapa quedan el italiano residual, el inglés del norte y la pasta en la mesa somalí.</p>"),
    ("Independencia y construcción del Estado",
     "<p>La Somalilandia británica se independizó el 26 de junio de 1960 y cinco días después, el 1 de julio, se unió al antiguo territorio italiano para formar la <strong>República Somalí</strong>. Aden Abdullah Osman Daar fue el primer presidente y Abdirashid Ali Shermarke el primer jefe de Gobierno. La joven república abrazó el pansomalismo, representado en las cinco puntas de la estrella de su bandera.</p><p>Shermarke, ya presidente, fue asesinado el 15 de octubre de 1969 en la ciudad norteña de Las Anod. El 21 de octubre el ejército tomó el poder sin encontrar resistencia armada en un golpe incruento encabezado por el general <strong>Mohamed Siad Barre</strong>, que implantó un «socialismo científico» y oficializó en 1972 la escritura del somalí en alfabeto latino. En julio de 1977 estalló la guerra del Ogadén, cuando Barre trató de anexionarse la región etíope de mayoría somalí; la derrota frente a una Etiopía respaldada por la Unión Soviética y Cuba descabezó al régimen. La represión y la guerra civil hicieron el resto. Según el Ministerio de Asuntos Exteriores español, «tras el colapso del régimen de Siad Barre, en 1991, se inició en Somalia una etapa marcada por la guerra y la anarquía». El 18 de mayo de 1991 Somalilandia declaró su independencia, y el 1 de agosto de 1998 Puntlandia se proclamó autónoma.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>Tras varios gobiernos de transición, la Unión de Tribunales Islámicos controló Mogadiscio en 2006 hasta que una intervención etíope la desalojó; de aquella derrota nació <strong>Al Shabab</strong>. En 2012 una constitución provisional dio forma al Gobierno Federal y a sus Estados miembros: Galmudug, Hirshabelle, Jubalandia, Puntlandia y Somalia del Sudoeste, además de la Somalilandia autoproclamada. Hassan Sheikh Mohamud presidió el país entre 2012 y 2017, le siguió Mohamed Abdullahi Farmaajo y desde 2022 gobierna de nuevo Mohamud.</p><p>Dos hechos han movido el tablero. El primero es el <strong>conflicto de Las Anod</strong>, entre el 6 de febrero y el 28 de agosto de 2023: las milicias dhulbahante de SSC-Khatumo expulsaron de la ciudad al ejército de Somalilandia, con entre 1.000 y 2.000 muertos y entre 154.000 y 203.000 desplazados; Mogadiscio reconoció a SSC-Khatumo como Estado federal en octubre de 2023. El segundo es el <strong>memorando de entendimiento entre Etiopía y Somalilandia</strong> de enero de 2024, que arrendaba a Adís Abeba el puerto de Berbera durante veinte años a cambio de un posible reconocimiento; la crisis con Somalia se rebajó con la Declaración de Ankara de diciembre de 2024. En marzo de 2024 Puntlandia dejó de reconocer la autoridad federal, en enero de 2025 la misión AUSSOM relevó a ATMIS y el 26 de diciembre de 2025 Israel fue el primer Estado miembro de la ONU en reconocer a Somalilandia.</p>"),
    ("Política y gobierno en 2026",
     "<p>Somalia es una república federal; a fecha de septiembre de 2026, según el MAEC (julio de 2026), el jefe del Estado es <strong>Hassan Sheikh Mohamud</strong>, elegido por el Parlamento en 2022, ya presidente entre 2012 y 2017, y el primer ministro es <strong>Hamza Abdi Barre</strong>. El Parlamento, bicameral, se reparte indirectamente entre clanes. En marzo de 2026 se aprobó una constitución que «refuerza los poderes del Presidente de la República y establece un sistema electoral directo»; la oposición la rechaza y las presidenciales se prevén para 2027.</p><p>No es una democracia. Freedom House la clasifica en 2025 como <em>Not Free</em> con 8 puntos sobre 100 —2 sobre 40 en derechos políticos y 6 sobre 60 en libertades civiles—, un 0 sobre 4 en salvaguardas contra la corrupción y ninguna elección nacional directa; la puntuación excluye a Somalilandia, evaluada aparte. Reporteros Sin Fronteras la sitúa en el puesto 126 de 180 en 2026. Al Shabab controla comarcas del centro y el sur y lanzó más de 160 ataques contra civiles en Mogadiscio entre 2023 y 2025, según la Agencia europea de Asilo. La UE es, según el MAEC, el mayor contribuyente financiero, con más de 2.600 millones de euros desde 2007, y mantiene EUCAP, EUTM y Atalanta, con participación española. El MAEC desaconseja el viaje bajo cualquier circunstancia, con amenaza terrorista «muy alta» y «alto riesgo de secuestro».</p>"),
    ("Economía y recursos",
     "<p>Somalia es uno de los países más pobres del mundo. Según el MAEC (julio de 2026), con datos del FMI para 2026, el PIB ronda los 14.170 millones de dólares y el PIB por habitante, los 813, con un crecimiento del 2,6 por ciento y una inflación del 5,9. El Banco Mundial rebaja el crecimiento de 2025 al 3 por ciento, frente al 4 de 2023 y 2024, por el recorte de la ayuda y la sequía. La moneda es el <strong>chelín somalí</strong>, a unos 652 por euro en julio de 2026, aunque el dólar circula de forma generalizada.</p><p>El sector primario aporta el 60 por ciento del PIB, repartido entre ganadería, un 40 por ciento, y pesca, un 20. Las exportaciones de 2024 son casi solo animales vivos: 294 millones de dólares en ovino y caprino, 81 en otros animales y 19 en vacuno, frente a unas importaciones dominadas por el azúcar, 431 millones, el arroz, 293, los tejidos y la pasta. El verdadero sostén son las <strong>remesas</strong> de la diáspora, el 17,5 por ciento del PIB en 2024, entre 1.300 y 2.000 millones de dólares anuales. El 55 por ciento de la población vive bajo el umbral de pobreza y el país ocupa el puesto 192 de 193 en el índice de desarrollo humano del PNUD de 2025. En Somalilandia el motor es el puerto de Berbera.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Viven en Somalia unos 19,7 millones de personas según Naciones Unidas (2025), con tres millones de desplazados internos y dos millones en la diáspora. Los idiomas oficiales son el <strong>somalí</strong>, escrito en alfabeto latino desde 1972, y el <strong>árabe</strong>; por carretera uno se entiende en somalí; el inglés funciona en Somalilandia. La población es musulmana suní de escuela shafi'í, con tradición sufí, en torno al 99,8 por ciento; la Constitución define el islam como religión del Estado. El MAEC cifra en un 85 por ciento la etnia somalí, con minorías bantúes y árabes en el sur, y cita los clanes darod, dir, hawiye, isaq y rahanweyn.</p><p>Somalia se llama «nación de poetas»: la poesía oral y la música pentatónica vertebran su vida social. En la mesa mandan el <em>canjeero</em>, el arroz especiado <em>bariis iskukaris</em> y el té con cardamomo; todo es halal y no hay cerdo. Es Estado parte de la Convención del Patrimonio Mundial desde 2020, sin bienes inscritos y solo tres candidatos; Laas Geel tampoco figura.</p><p>Conviene ropa holgada que cubra brazos y piernas, con pañuelo para las mujeres, también en Somalilandia. Hay que pedir permiso antes de fotografiar personas y nunca fotografiar edificios oficiales ni controles militares. El ramadán empieza en 2027 en torno al 8 de febrero: no se come ni bebe en público de día, y el alcohol está prohibido.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Somalia (Ministerio de Asuntos Exteriores de España · PDF · julio de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/SOMALIA_FICHA%20PAIS.pdf"),
    ("Recomendaciones de viaje: Somalia (Ministerio de Asuntos Exteriores de España · consultado en septiembre de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Somalia"),
    ("Somalia: Freedom in the World 2025 (Freedom House · 2025)", "https://freedomhouse.org/country/somalia/freedom-world/2025"),
    ("Somalia (Encyclopaedia Britannica · ficha de país · consultado en septiembre de 2026)", "https://www.britannica.com/place/Somalia"),
    ("History of Somalia (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/History_of_Somalia"),
    ("Somalia (Wikipedia en español · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Somalia"),
    ("Somalia · State Party (UNESCO, Centro del Patrimonio Mundial · consultado en septiembre de 2026)", "https://whc.unesco.org/en/statesparties/so"),
    ("Somaliland (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Somaliland"),
    ("International recognition of Somaliland (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/International_recognition_of_Somaliland"),
    ("2023 Las Anod conflict (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2023_Las_Anod_conflict"),
    ("Puntland (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Puntland"),
    ("Laas Geel (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Laas_Geel"),
    ("Visa policy of Somaliland (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Visa_policy_of_Somaliland"),
    ("Somalis: lengua, religión y clanes (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Somalis"),
    ("Somali cuisine (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Somali_cuisine"),
    ("Al-Shabaab control areas, presence and influence (Agencia de la UE para el Asilo, EUAA · informe de seguridad 2025)", "https://www.euaa.europa.eu/coi/somalia/2025/security-situation/12-armed-actors-and-relevant-developments/122-al-shabaab-control-areas-presence-and-influence"),
    ("Somalia · World Report 2026 (Human Rights Watch · 2026)", "https://www.hrw.org/world-report/2026/country-chapters/somalia"),
    ("Somalia (Reporteros Sin Fronteras · Clasificación Mundial de la Libertad de Prensa 2026)", "https://rsf.org/en/country/somalia"),
    ("Somalia (International Crisis Group · seguimiento de crisis · consultado en septiembre de 2026)", "https://www.crisisgroup.org/africa/horn-africa/somalia"),
    ("Somalia Overview (Banco Mundial · consultado en septiembre de 2026)", "https://www.worldbank.org/en/country/somalia/overview"),
    ("El IMB advierte de un repunte de la piratería en Somalia, el océano Índico y el golfo de Adén (Puente de Mando · 17 de abril de 2024)", "https://www.puentedemando.com/imb-advierte-de-un-repunte-de-la-pirateria-en-somalia-oceano-indico-y-golfo-de-aden/"),
    ("Somalia travel advice · Safety and security (Foreign, Commonwealth and Development Office del Reino Unido · 4 de junio de 2026)", "https://www.gov.uk/foreign-travel-advice/somalia/safety-and-security"),
]

SPEC = dict(
    slug="somalia", name="Somalia", revision="18 sep 2026",
    sub="EXCLUIDO POR PROTOCOLO — MAEC: desaconsejado bajo cualquier circunstancia · ficha informativa",
    chips=[
        ("ESTATUS", "FUERA DE RUTA. MAEC: se desaconseja el viaje bajo cualquier circunstancia…"),
        ("CÓMO LLEGAR", "En la práctica solo en avión: Aden Adde (Mogadiscio) o Egal (Hargeisa)…"),
        ("VISADO", "Obligatorio y DISTINTO en cada realidad. Somalia: eTAS previa en etas.gov.so…"),
        ("VEHÍCULO", "AIT/FIA no tiene organización emisora de CPD en Somalia. Admisión temporal sin norma localizable…"),
        ("SEGURIDAD", "MAEC: desaconsejado bajo cualquier circunstancia"),
        ("SEGURO", "Carta Verde no vale · evacuación obligatoria"),
        ("SALUD", "Malaria alta · cólera activo · fiebre amarilla"),
        ("DRONES", "No permitidos a extranjeros · confiscación"),
        ("STARLINK", "Activo desde agosto de 2025 · 70 USD/mes"),
        ("4x4", "Solo con escolta armada privada"),
        ("A PIE", "Descartado fuera de recinto fortificado"),
        ("PERRO", "Sin trámite oficial publicado. Vuelta a la UE: Somalia NO figura en el Reglamento (UE) 2026/636 → titulación…"),
        ("MONEDA", "Chelín somalí (~652 SoSh/EUR, Ficha País julio 2026)…"),
        ("VENTANA", "Semiárido y caluroso. Lluvias gu de abril a junio con inundaciones…"),
    ],
    center=[5.48, 45.86], zoom=5,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Norte · Zeila–Hargeisa–Berbera–Sheikh–Erigavo–Bosaso (Somalilandia y Puntlandia)",
    corridor_alt_label="Sur federal · Mogadiscio–Afgooye–Baidoa–Merca–Barawa–Kismayo (VETADO)",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Laas_Geel,_2024.jpg?width=1200",
    hero_credit="Las Geel · Mheidegger · CC BY 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Somalia queda fuera de la ruta de 2027 y no es negociable. Es el único país de África al que el MAEC aplica su fórmula más dura —se desaconseja el viaje bajo cualquier circunstancia— y añade que todo el país y sus aguas aledañas son zona de riesgo alto que debe evitarse. Al Shabab lanzó en febrero de 2025 la ofensiva del Shabelle, llegó a tomar Adan Yabaal a 70 km de Mogadiscio y Balad a 30 km, y mantiene atentados regulares en la capital; el FCDO sitúa la amenaza de secuestro de occidentales como ALTA en todo el país, incluida Somalilandia; y la piratería ha vuelto al Índico, con el secuestro del Hellas Aphrodite el 6 de noviembre de 2025 a 560 millas náuticas de Eyl. Con dos 4x4 matriculados en España, tres viajeros y un perro, la única forma de estar allí sería con escolta armada privada y alojamiento fortificado: un modelo incompatible con una expedición overland autónoma. Si algún día se hiciera algo, sería un viaje aparte y sin coches propios: vuelo a Hargeisa, 4x4 con conductor y escolta SPU, entre siete y diez días. Como referencia real, un circuito comercial Yibuti–Somalilandia–Mogadiscio de nueve días cuesta 3.600 € por persona, sin seguro de evacuación, que es el gasto que de verdad decide. Para replantearlo harían falta tres cosas: que el MAEC rebaje la recomendación sobre Somalilandia, que exista un seguro que cubra la zona y que el perro se quede en España.",
    facts=[
        ("Estatus", "FUERA DE RUTA. MAEC: se desaconseja el viaje bajo cualquier circunstancia. Todo el país y sus aguas son zona de riesgo alto."),
        ("Cómo llegar", "En la práctica solo en avión: Aden Adde (Mogadiscio) o Egal (Hargeisa). Por tierra, únicamente Tog Wajaale desde Etiopía."),
        ("Visado", "Obligatorio y DISTINTO en cada realidad. Somalia: eTAS previa en etas.gov.so. Somalilandia: visado propio; desde el 10-11-2025 NO reconoce los visados somalíes."),
        ("Vehículo/aduana", "AIT/FIA no tiene organización emisora de CPD en Somalia. Admisión temporal sin norma localizable. Se conduce por la DERECHA."),
        ("Seguro", "La Carta Verde NO cubre Somalia. No consta tarjeta regional obligatoria verificable. Seguro con evacuación médica imprescindible."),
        ("Moneda", "Chelín somalí (~652 SoSh/EUR, Ficha País julio 2026). Somalilandia: chelín somalilandés (~8.500/USD). Dólares en efectivo y dinero móvil; tarjetas no."),
        ("Perro", "Sin trámite oficial publicado. Vuelta a la UE: Somalia NO figura en el Reglamento (UE) 2026/636 → titulación antirrábica previa obligatoria."),
        ("Drones", "No permitidos a visitantes extranjeros. La SCAA declara que las operaciones con dron no están reguladas en Somalia."),
        ("Starlink", "Activo desde el 5 de agosto de 2025: 390 USD el kit y 70 USD/mes. Licencia de la NCA somalí; validez en Somalilandia por confirmar."),
        ("Seguridad", "Amenaza terrorista muy alta, secuestro alto en todo el país, piratería en el mar. Escolta armada obligatoria por carretera."),
        ("Clima", "Semiárido y caluroso. Lluvias gu de abril a junio con inundaciones. Hargeisa a 1.334 m, más templada. Mejor ventana: de noviembre a marzo."),
        ("Sanidad", "MAEC: instalaciones hospitalarias muy escasas y en estado deplorable. Malaria de alto riesgo en todo el país y cólera activo."),
    ],
    alerts=[
        "MAEC: se desaconseja el viaje bajo cualquier circunstancia. Es la recomendación más dura que Exteriores aplica en toda África.",
        "Al Shabab lanzó en febrero de 2025 la ofensiva del Shabelle y llegó a tomar Balad (30 km de Mogadiscio) y Adan Yabaal (70 km). El cerco no se ha cerrado, pero tampoco se ha revertido.",
        "Amenaza de SECUESTRO alta en todo el país, incluida Somalilandia, según el FCDO (actualizado el 4 de junio de 2026). Los occidentales son objetivo declarado.",
        "España no tiene embajada residente: la competencia es de la Embajada en Nairobi y la asistencia consular sobre el terreno es extremadamente difícil.",
        "El visado de Somalia NO sirve para Somalilandia. Desde el 10 de noviembre de 2025 Hargeisa declara nulos los visados y autorizaciones emitidos por Mogadiscio.",
        "El sistema de visado electrónico somalí sufrió una filtración masiva de datos (más de 35.000 registros) antes de migrar al eTAS el 27 de noviembre de 2025.",
        "PIRATERÍA en resurgencia: el Hellas Aphrodite fue secuestrado el 6 de noviembre de 2025 a 560 millas náuticas al sureste de Eyl. El riesgo llega a más de 1.000 millas de la costa.",
        "Frontera terrestre con Kenia CERRADA (MAEC). El único paso practicable para extranjeros es Tog Wajaale desde Etiopía.",
        "Conflicto de Las Anod: desde febrero de 2023 Somalilandia perdió el control de Sool ante SSC-Khatumo, con 153.000-203.000 desplazados. Sool y Sanaag siguen vetados.",
        "Drones no permitidos a extranjeros y riesgo real de confiscación y detención. No llevarlos ni en el equipaje.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Loyada–Zeila", "Frontera de Yibuti a Zeila por la costa de Awdal", "~60 km · 1 día"),
        ("2 · Zeila–Borama", "Arena y desierto tierra adentro hasta el altiplano de Awdal", "~190 km · 1 día"),
        ("3 · Borama–Hargeisa", "Por Tog Wajaale, asfalto, control fronterizo etíope al lado", "~120 km · 1 día"),
        ("4 · Hargeisa (base)", "Permiso del Ministerio de Turismo, trámite SPU, mercado y monumento del MiG", "0 km · 1 día"),
        ("5 · Hargeisa–Las Geel", "Carretera de Berbera, desvío y aproximación a pie al yacimiento", "~55 km · 1 día"),
        ("6 · Las Geel–Berbera", "Bajada de la escarpa al golfo de Adén, puerto y playa", "~100 km · 1 día"),
        ("7 · Berbera–Sheikh", "Subida del paso de Sheikh, 71 km de curvas y ruinas de Fardowsa", "~71 km · 1 día"),
        ("8 · Sheikh–Burao", "Meseta del Togdheer, 60 km, mercado de ganado", "~60 km · 1 día"),
        ("9 · Burao–Erigavo", "La etapa dura: pista larga del Sanaag, escolta SPU obligatoria", "~400 km · 2 días"),
        ("10 · Erigavo–Daallo", "Borde de la escarpa, bosque de niebla y ascensión al Shimbiris", "~35 km · 1 día"),
        ("11 · Erigavo–Bosaso", "Bajada a Puntlandia por Badhan; cambio de administración y de permisos", "~450 km · 2 días"),
        ("12 · Bosaso–Garowe", "Carretera norte-sur por el valle del Nugal", "~205 km · 1 día"),
        ("13 · Garowe–Las Anod", "Regreso hacia el Sool · ZONA VETADA, etapa solo teórica", "~180 km · 1 día"),
    ],
    offroad=[
        "El único acceso rodado realista al conjunto es Somalilandia, y el tramo más 4x4 es el de la frontera de Yibuti: relatos de viajeros describen unos 300 km de desierto y arena entre el paso de Loyada y Borama, con firme muy malo y vehículo alto obligatorio (againstthecompass.com/en/travel-somaliland).",
        "El eje Hargeisa–Berbera (unos 160 km) es asfalto en buen estado y es, junto con las carreteras a la frontera etíope y a la de Yibuti, una de las pocas rutas que la policía de Hargeisa cubre con exención de escolta SPU (thetravelcamel.com/somaliland-travel-guide).",
        "La subida Berbera–Sheikh son 71 km de asfalto estrecho y muy revirado sobre la escarpa de los montes Golis, con 1.430 m de desnivel ganado de golpe; es el tramo más vistoso y el que más sufre desprendimientos con lluvia (en.wikipedia.org/wiki/Sheikh,_Somaliland).",
        "Burao–Erigavo son unos 400 km de pista del Sanaag: queda fuera de las rutas consideradas seguras y exige escolta armada SPU, igual que todo lo que se acerque a las fronteras con Puntlandia y Somalia (thetravelcamel.com/somaliland-travel-guide).",
        "No hay acceso rodado a la cumbre del Shimbiris (2.460 m): se deja el coche en el borde de Daallo y se continúa a pie, con posibilidad de acampar (en.wikipedia.org/wiki/Shimbiris).",
        "Bradt resume la norma general del país: taxis compartidos en las carreteras principales y 4x4 con conductor local para cualquier zona remota, con noviembre-marzo como única ventana practicable fuera del asfalto (bradtguides.com).",
        "Las guías de overlanding clasifican Somalia como destino de dificultad 5/5, con firme que va de autopista asfaltada a pista de tierra dura y visados distintos por región (overlandtraveltips.com).",
        "ZONAS VETADAS PARA CUALQUIER PISTA: todo el centro-sur federal por Al Shabab, que conserva control rural y cuartel general en Jilib; el Sool en torno a Las Anod por el conflicto abierto desde 2023; y la franja costera del nordeste por el repunte pirata desde diciembre de 2023.",
    ],
    senderismo=[
        "Ascensión al Shimbiris (2.460 m), techo de Somalilandia, desde el borde de Daallo: no hay pista hasta arriba, se sube a pie y se puede vivaquear (en.wikipedia.org/wiki/Shimbiris).",
        "Recorrido del borde de la escarpa de Daallo, con caídas de más de 2.000 m sobre el golfo de Adén y observación de aves endémicas como el pardillo de Warsangli (bradtguides.com).",
        "Paseo por el bosque de niebla de Daallo entre enebros (Juniperus procera) y Buxus hildebrandtii, con ejemplares de más de mil años (en.wikipedia.org/wiki/Daallo_Mountain).",
        "Aproximación a los abrigos de Las Geel: desde el control hay unos kilómetros de subida a pie con guía obligatorio, una hora larga ida y vuelta con las paradas (againstthecompass.com/en/travel-somaliland).",
        "Vuelta a las ruinas medievales de Fardowsa, junto al pueblo de Sheikh, sobre el yacimiento del siglo XIV-XV que controlaba el camino del puerto a la meseta (en.wikipedia.org/wiki/Sheikh,_Somaliland).",
        "Costa de Berbera: caminata de playa y arrecife, con acceso a corales bien conservados; es más snorkel que senderismo, pero el frente de playa se recorre a pie durante kilómetros (bradtguides.com).",
        "Lengua de arena, manglares y frente de arrecife de Zeila, con las islas de Saad ad-Din a la vista; recorrido llano y expuesto, solo viable en invierno (en.wikipedia.org/wiki/Zeila).",
        "Hargeisa National Park, en las afueras de la capital: figura como parque nacional en Wikipedia pero sin datos de superficie, fauna ni servicios; su interés real está POR CONFIRMAR (en.wikipedia.org/wiki/Hargeisa_National_Park).",
    ],
    acampada=[
        "NO HE ENCONTRADO NINGÚN CAMPING HOMOLOGADO en Somalia ni en Somalilandia a través de fuentes abiertas verificables; doy este punto por confirmar.",
        "En la montaña sí hay acampada documentada: Wikipedia señala que el Shimbiris se sube a pie y que es posible acampar en la zona, que es la única mención explícita de vivac que he podido verificar.",
        "Operadores de gama alta anuncian campamentos móviles privados en Hargeisa, Las Geel y Berbera (Journeys by Design / Wild Expeditions), pero solo he visto los títulos en el buscador: contenido NO VERIFICADO con fetch, tratar como pista, no como dato.",
        "La alternativa real es hotel barato con patio cerrado: precios citados por viajeros de unos 20 USD en Zeila, 15 en Borama, 20-25 en Hargeisa y 10 en Berbera, con Oriental y Damal como referencias en la capital (againstthecompass.com, thetravelcamel.com).",
        "iOverlander y Tracks4Africa no los he podido consultar en esta sesión; cualquier punto de acampada libre que aparezca ahí debe cruzarse con la exención de escolta SPU antes de plantearlo.",
        "La acampada libre choca de frente con el sistema de escoltas: fuera de Hargeisa, Berbera y los corredores a las fronteras, la SPU es obligatoria y el escolta debe pernoctar contigo, lo que en la práctica empuja a dormir en pueblo.",
        "En Somalia federal (Mogadiscio, Baidoa, Kismayo, Merca, Barawa) la acampada es sencillamente inviable: el estándar es alojamiento fortificado con seguridad privada y traslados en convoy.",
        "En Puntlandia (Bosaso, Garowe) tampoco hay acampada documentada; los hoteles con recinto vallado y permiso de la administración de Puntlandia son la única fórmula descrita.",
    ],
    visado=[
        "SOMALIA FEDERAL: visado obligatorio. Desde el 27 de noviembre de 2025 el sistema es el eTAS (etas.gov.so), autorización electrónica PREVIA y sin ella la aerolínea no emite tarjeta de embarque.",
        "MAEC: una entrada, validez de UN MES, 60 USD EN EFECTIVO, pasaporte con seis meses de validez. Se recomienda llevar carta de invitación con motivo y duración del viaje.",
        "SOMALILANDIA: visado PROPIO. Desde el 10 de noviembre de 2025 declara NO válidos los visados y autorizaciones emitidos por Somalia; hay que sacar visado a la llegada o en sus representaciones.",
        "Somalilandia emite visado en Adís Abeba (100 USD), Yibuti (60 USD) y Londres (30 GBP), y a la llegada en Hargeisa por unos 40-60 USD (Against the Compass, agosto de 2026; FCDO, 2026).",
        "POR VÍA TERRESTRE en Tog Wajaale el visado somalilandés debe llevarse YA EMITIDO: en ese paso no se expide a la llegada.",
        "PUNTLANDIA aplica sus propios permisos. Ninguno de los tres sistemas es intercambiable con los otros dos.",
    ],
    fronteras_rows=[
        ("Aeropuerto internacional", "Aden Adde (Mogadiscio) · 2,0136 N / 45,3047 E", "Única vía practicable a Somalia federal. eTAS obligatoria. Recinto fortificado MIA/Halane; salir a la ciudad solo en convoy con escolta. Morteros contra el aeropuerto en febrero de 2025 (Wikipedia, timeline 2025)."),
        ("Aeropuerto internacional", "Egal (Hargeisa, Somalilandia) · 9,56 N / 44,07 E", "Visado somalilandés a la llegada, entrada única, un mes. El visado somalí NO sirve aquí desde noviembre de 2025 (Africanews, 11-11-2025)."),
        ("Paso terrestre", "Tog Wajaale (Etiopía–Somalilandia) · 9,6014 N / 43,3361 E", "ABIERTO, de 06:00 a 18:00. Entrada real a Somalilandia. Visado previo obligatorio. Trámites de 30 a 90 minutos (Border Crossing Hub, 2026)."),
        ("Paso terrestre", "Loyada (Yibuti–Somalilandia) · 11,4667 N / 43,2458 E", "Único paso oficial desde Yibuti, a 25 km de la capital yibutiana. Usado por circuitos comerciales en 2025-2026. Cierres políticos repetidos desde 1999; estado en 2026 POR CONFIRMAR."),
        ("Paso terrestre", "Liboi / Dhobley (Kenia–Somalia)", "CERRADO. El MAEC indica expresamente que la frontera terrestre con Kenia está cerrada."),
        ("Puerto", "Berbera (Somalilandia) · 10,4356 N / 45,0164 E", "Ampliado por DP World (442 M USD; DP World 51%, Somalilandia 30%, Etiopía 19%). Muelle de 1.000 m y hasta 2 M TEU. Tráfico de carga, no de pasajeros: no es vía de entrada para un 4x4 particular."),
        ("Puerto / aeropuerto", "Bosaso (Puntlandia)", "Acceso a Puntlandia con permisos propios. Puntlandia dejó de reconocer la autoridad federal en 2024. Zona de piratería y presencia del Estado Islámico. Desaconsejado."),
        ("Frontera interna", "Sool y Sanaag (Las Anod / Erigavo)", "Zona de conflicto Somalilandia / SSC-Khatumo desde febrero de 2023, con estancamiento militar a 100 km de Las Anod. Vetada por FCDO y por Canadá (9-09-2026)."),
    ],
    vehiculos=[
        "Se conduce por la DERECHA. El permiso internacional de conducción es recomendable, pero su aceptación real en controles no está documentada.",
        "carnetdepassage.org indica textualmente que AIT/FIA no tiene ninguna organización emisora de CPD en Somalia; no hay vía local para tramitarlo ni constancia de que la aduana lo exija.",
        "No existe norma localizable de admisión temporal de vehículos extranjeros de turismo. POR CONFIRMAR: es el agujero documental más serio de esta ficha.",
        "La Carta Verde de OFESAUTO no cubre Somalia: para países fuera del sistema hace falta seguro de frontera, y no consta que se emita aquí.",
        "El FCDO exige consultar a una empresa de seguridad antes de cualquier desplazamiento por carretera; los controles armados son constantes y la circulación nocturna está prohibida de facto.",
        "En Somalilandia la Special Protection Unit (SPU) acompaña a los extranjeros fuera de Hargeisa. Hay exenciones teóricas del Ministerio del Interior, pero los relatos coinciden en que sin escolta hay problemas en cada control.",
        "Coste histórico de referencia en Somalilandia: unos 100 USD por taxi con escolta SPU de Hargeisa a Las Geel y 20 USD por la escolta en el regreso desde Berbera (The Candy Trail; Bradt Somaliland).",
        "No hay ningún relato verificado de overlanders europeos entrando en Somalia o Somalilandia con vehículo propio matriculado en la UE en los últimos años. Repuestos y talleres solo en Hargeisa y Mogadiscio.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autoridad: Somali Civil Aviation Authority (SCAA). Según drone-laws.com (21 de enero de 2026), no hay normativa específica de drones en Somalia.",
        "La misma fuente afirma que los drones NO están permitidos a los visitantes extranjeros. Ausencia de norma no significa permiso, significa discrecionalidad total.",
        "Contexto: el 31 de enero de 2025 las fuerzas de seguridad derribaron uno de los dos drones que sobrevolaban Villa Somalia, con el presidente y el primer ministro dentro. Los drones son un arma aquí, no un juguete.",
        "Somalilandia gestiona su propio espacio aéreo y desde noviembre de 2025 exige autorización formal para cualquier aeronave que entre o salga. No hay texto publicado sobre drones. POR CONFIRMAR.",
        "Regla de la expedición: el dron no entra en Somalia, ni en Somalilandia, ni en Puntlandia, bajo ningún supuesto.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Licencia de operador concedida por la National Communications Authority de Somalia el 14 de abril de 2025 (Connecting Africa).",
        "Servicio comercial en marcha desde el 5 de agosto de 2025: hardware unos 220.000 SoSh (390 USD) y plan residencial unos 40.000 SoSh (70 USD) al mes (Space in Africa).",
        "Validez de esa licencia en Somalilandia y Puntlandia: POR CONFIRMAR. Hargeisa reivindica control regulatorio propio y en noviembre de 2025 endureció el control de su espacio aéreo.",
        "Red móvil: Hormuud en Somalia y Telesom en Somalilandia. SIM prepago barata, unos 3 USD con 1 GB (Against the Compass, 2026).",
        "El dinero móvil (EVC Plus, Zaad) es el medio de pago habitual, por delante del efectivo y muy por delante de la tarjeta: no hay aceptación de tarjetas de crédito (MAEC).",
    ],
    perro_intro=[
        "NO EXISTE una página oficial somalí de requisitos de importación de animales de compañía localizable en esta sesión. Todo lo referido a la entrada del perro está POR CONFIRMAR.",
        "El organismo nacional competente es el Ministry of Livestock, Forestry and Range (molfr.gov.so), con un Department of Animal Health and Public Veterinary Services en el distrito de Warta Nabada de Mogadiscio, pero no publica trámites para mascotas.",
        "Somalilandia tiene su propio Ministry of Livestock and Rural Development (molfd.govsomaliland.org) y sus certificados no serían válidos en Somalia federal, igual que ocurre con los visados.",
        "VUELTA A LA UE: Somalia NO figura en las listas del Reglamento de Ejecución (UE) 2026/636, aplicable desde el 22 de abril de 2026. Ningún país africano continental está en ellas; solo aparecen Ascensión y Santa Elena.",
        "Por tanto se aplica la vía A del Reglamento Delegado (UE) 2026/131: microchip, primovacunación antirrábica al menos 21 días antes y TITULACIÓN DE ANTICUERPOS (≥0,5 UI/ml) en laboratorio autorizado, con extracción al menos 30 días después de la vacuna y 90 días de espera antes de entrar en la UE.",
        "Esa titulación debe estar anotada en el pasaporte ANTES de salir de España; hacerla desde Somalia sería materialmente imposible. Entrada en España solo por un Punto de Entrada de Viajeros (PEV), con declaración a Aduanas o Guardia Civil.",
        "La rabia es endémica en Somalia (TravelHealthPro, enero de 2026) y no hay atención veterinaria fiable fuera de Hargeisa y Mogadiscio. DECISIÓN DEL PROYECTO: el perro no entra en Somalia ni en Somalilandia.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "MAEC: las instalaciones hospitalarias son muy escasas y su estado es deplorable, y las farmacias tienen inventario limitado. Seguro médico completo con evacuación incluida: imprescindible.",
        "MALARIA: riesgo ALTO en todo el país. TravelHealthPro (enero de 2026) recomienda atovacuona/proguanil, doxiciclina o mefloquina, iniciando 1-2 días antes de llegar.",
        "FIEBRE AMARILLA: TravelHealthPro indica que NO hay requisito de certificado bajo el Reglamento Sanitario Internacional y sitúa el riesgo como bajo en Bakool, Banaadir y Bay. El MAEC la recomienda y varias fuentes de viaje afirman que se exige en frontera. Llevarla puesta y con certificado.",
        "CÓLERA: brote activo, con 8.763 casos notificados entre enero y diciembre de 2025 (TravelHealthPro). Agua no potable en todo el país.",
        "POLIO: circulación de poliovirus derivado de vacuna tipo 2. Refuerzo recomendado antes de viajar.",
        "Otras vacunas recomendadas por el MAEC y NaTHNaC: hepatitis A y B, fiebre tifoidea, tétanos-difteria, meningococo, sarampión y dengue presente. Rabia endémica: profilaxis preexposición en estancias largas.",
        "Referencias hospitalarias: Hargeisa Group Hospital (400 camas, el mayor hospital público de Somalilandia) y el Hospital Erdoğan de Mogadiscio (200 camas, rehabilitado por la agencia turca TIKA). La evacuación real se hace a Nairobi o a Yibuti.",
    ],
    seguridad_intro="Somalia es el peor escenario de seguridad de África para un viajero europeo. El MAEC desaconseja el viaje bajo cualquier circunstancia y califica todo el país y sus aguas como zona de riesgo alto. Al Shabab ataca con alta frecuencia en todas las regiones, controla territorio rural en el centro y el sur y en 2025 llegó a 30 km de Mogadiscio; la amenaza de secuestro de occidentales es alta incluso en Somalilandia; y la piratería ha vuelto al Índico. Cualquier desplazamiento por carretera exige escolta armada privada y alojamiento fortificado.",
    seguridad=[
        "MAEC: amenaza terrorista muy alta, con ataques de alta frecuencia en todas las regiones del país y enfrentamientos armados diarios. Todo el territorio y sus aguas son zona de riesgo alto.",
        "FCDO (4 de junio de 2026): es muy probable que los terroristas intenten atentar en Somalia, incluida Somalilandia. Cita ataques con cohetes contra el aeropuerto de Mogadiscio en abril de 2025 y un artefacto contra el convoy presidencial en marzo de 2025.",
        "SECUESTRO: amenaza alta en todo el país. Los occidentales son objetivo legítimo tanto para grupos terroristas como para bandas criminales que revenden rehenes.",
        "Ofensiva del Shabelle (desde el 20 de febrero de 2025): Al Shabab tomó Balad a 30 km de Mogadiscio, Adan Yabaal a 70 km, Awdheegle, Sabiid y Moqokori, y llegó a los suburbios de Elasha Biyaha. Las contraofensivas de AUSSOM no han cerrado la situación.",
        "Canadá (9 de septiembre de 2026): evitar todo viaje. Señala conflictos violentos en las zonas fronterizas de Sool y Sanaag y que no existe oficina canadiense en el país para asistencia de emergencia.",
        "PIRATERÍA: repunte claro. Nueve incidentes y cuatro secuestros entre diciembre de 2023 y mayo de 2024 (Gard), y una nueva oleada en octubre-noviembre de 2025 que culminó con el secuestro del Hellas Aphrodite a 560 millas náuticas de Eyl el 6 de noviembre (Skuld).",
        "SOMALILANDIA es de facto estable en Hargeisa, Berbera y el corredor a Las Geel, pero mantiene la Special Protection Unit para extranjeros fuera de la capital y su este, Sool y Sanaag, está en conflicto abierto con SSC-Khatumo desde febrero de 2023.",
        "PUNTLANDIA dejó de reconocer la autoridad del gobierno federal en 2024 y tiene presencia del Estado Islámico en las montañas de Bari, además de las bases históricas de la piratería.",
        "Sin embajada española en el país no hay rescate consular posible sobre el terreno: todo depende de Nairobi, a 1.000 km, y el propio MAEC califica la asistencia consular de extremadamente difícil.",
    ],
    agua=[
        "El agua de red no es potable en ningún punto del país. Para beber, solo agua embotellada o tratada; el cólera está activo desde 2025.",
        "Somalia atraviesa una emergencia de sequía 2025-2026: OCHA cifró en más de 570.000 las personas con escasez aguda de agua en Gedo y los dos Juba, y en 156.000 los desplazados en Sanaag, Sool y Togdheer.",
        "El agua es un recurso disputado y se compra: los proveedores llegan a cobrar 1 USD por un bidón de 20 litros, unos 50 USD por cada 1.000 litros en camión cisterna (OCHA).",
        "Llenar depósitos grandes de ducha y lavado en una zona en sequía es socialmente conflictivo además de caro. La única opción razonable serían hoteles y compounds de Hargeisa, con cobro.",
        "No hay red de puntos de agua documentada en iOverlander ni en Tracks4Africa para Somalia ni para Somalilandia. POR CONFIRMAR.",
        "Regla de la expedición: si algún día se entrara, se entraría con autonomía total de agua y sin repostar fuera de recintos seguros.",
    ],
    combustible=[
        "Precio de referencia a 5 de marzo de 2026 (AfroFuel): gasolina 750 SoSh/litro (1,31 USD) y gasóleo 750 SoSh/litro (1,31 USD). GLP 950 SoSh/kg. Un 6 % por debajo de la media de África oriental.",
        "La misma fuente advierte de que el precio varía mucho entre Mogadiscio, Hargeisa y las estaciones rurales, y de que son estimaciones de planificación, no precios garantizados.",
        "El mercado del carburante somalí es de importación privada y se paga en dólares o por dinero móvil. La calidad del gasóleo es irregular y su trazabilidad, nula.",
        "Fuera de Hargeisa, Berbera y Mogadiscio la red de estaciones es escasa y el suministro se hace con bidones: filtrado y decantación obligatorios para no destrozar los inyectores del Grenadier y de la Delica.",
        "Somalilandia fija sus propios precios por decisión administrativa; el anuncio de marzo de 2026 no se pudo abrir (error 403). POR CONFIRMAR.",
        "Autonomía recomendada para cualquier tramo: de 800 a 1.000 km, muy por encima de los 250 km/día de media de la expedición.",
    ],
    experiencias_intro="No existen relatos recientes y verificables de overlanders europeos cruzando Somalia federal con vehículo propio: el conflicto lo impide desde hace más de treinta años. Lo que sí hay son relatos de viajeros independientes y de agencias en Somalilandia, que es otra realidad, y de circuitos con escolta a Mogadiscio.",
    experiencias=[
        "Somalilandia se visita, Somalia no: Against the Compass mantiene una guía actualizada el 30 de agosto de 2026 en la que describe un país visitable con 30 a 50 USD al día, alojamiento de 10 a 15 USD, entrada a Las Geel por 35 USD con guía y 4x4 por 50 USD. Hay cajeros en Hargeisa (Premier Bank, Dahabshil) y el cambio ronda los 8.500 chelines por dólar. Su conclusión es tajante: Somalilandia es segura, Somalia no lo es.",
        "El visado no es intercambiable: la misma guía insiste en que un visado turístico de Somalilandia no permite viajar a Somalia y que uno de Somalia no permite viajar a Somalilandia. Es el error clásico del viajero que compra la autorización somalí pensando que le sirve para aterrizar en Hargeisa, y el FCDO lo confirma: en el aeropuerto de Egal el documento somalí no es válido y hay que comprar visado a la llegada.",
        "La SPU depende del humor del policía: Against the Compass relata en 2026 que su experiencia con la escolta policial obligatoria fuera de Hargeisa fue distinta de la de otros viajeros, y lo resume diciendo que puede depender del humor y la percepción del agente. En la práctica eso significa que no se puede planificar un itinerario en Somalilandia dando por hecho que se viajará sin escolta.",
        "Exención sobre el papel, control en la carretera: el blog Bradt Somaliland Travel News recoge que un mando policial les aseguró que no hacía falta escolta para Las Geel pero admitió que ya no emitían cartas de exención, y que después hubo problemas en cada puesto de control. Cifra 25 USD por persona en permisos del Ministerio de Turismo y 20 USD por la escolta de vuelta desde Berbera (entradas de 2013 y 2017).",
        "Las Geel, con AK-47 en el asiento de al lado: The Candy Trail describe el trayecto de 50 km desde Hargeisa en taxi contratado con un soldado armado incluido por 100 USD, más 25 USD de permiso del Ministerio de Turismo. Recomienda seguir hacia Berbera en lugar de volver a Hargeisa para no pagar dos veces taxi y escolta. Relato de 2013 publicado en 2018: es lo más detallado que hay.",
        "Tog Wajaale, el paso real: Border Crossing Hub describe el cruce desde Togo Wuchale en Etiopía como un proceso de tres fases con una franja neutral de mercado caótico, horario de 06:00 a 18:00 y entre 30 y 90 minutos de trámites. Advierte de que el visado de Somalilandia hay que llevarlo ya emitido porque en ese paso no se expide a la llegada, y de que se admiten todo tipo de vehículos.",
        "Yibuti-Hargeisa-Mogadiscio, 3.600 € por persona: la agencia Kumakonda vende para octubre de 2026 un circuito de nueve días que entra por carretera desde Yibuti a Somalilandia por Loyada, sigue por Borama y Hargeisa y vuela a Mogadiscio, con unos 80 USD en visados y escolta militar cuando hace falta para pasar los controles de la capital. Es la referencia de coste más honesta que hemos encontrado.",
        "Mogadiscio se vive dentro del aeropuerto: la ficha del aeropuerto Aden Adde recoge que la terminal turca de 2015 duplicó los vuelos diarios hasta 60 y que la OACI lo sacó de su lista de zonas de riesgo en 2013. Pero la cronología de 2025 registra morteros disparados hacia el aeropuerto el 27 de febrero durante la visita del primer ministro etíope: el perímetro más protegido del país tampoco es seguro.",
        "El este de Somalilandia se cayó del mapa: el conflicto de Las Anod, abierto el 6 de febrero de 2023, terminó el 28 de agosto con la derrota de Somalilandia en Goojacade y la pérdida de Sool ante SSC-Khatumo, con entre 153.000 y 203.000 desplazados y un estancamiento militar a 100 km de Las Anod. Canadá sitúa en septiembre de 2026 los conflictos violentos precisamente ahí. Cualquier itinerario al este de Burao queda descartado.",
        "Piratería de vuelta: Skuld documenta en noviembre de 2025 cuatro episodios en diez días, entre ellos el secuestro del Hellas Aphrodite a 560 millas náuticas al sureste de Eyl el 6 de noviembre. Wikipedia añade que el pesquero chino Liao Dong Yu 57, liberado en enero de 2025 por un rescate de 2 millones de dólares, fue vuelto a secuestrar el 1 de enero de 2026. El fenómeno no se ha cerrado.",
    ],
    pendientes=[
        ("Admisión temporal de vehículos extranjeros", "Localizar la norma aduanera somalí o somalilandesa, o un relato verificado de entrada con vehículo matriculado en la UE."),
        ("Precio del combustible en Somalilandia", "Abrir el anuncio oficial de precios de Hargeisa (el de marzo de 2026 devolvió 403) y fijar precio por litro con fecha."),
        ("Estado del paso de Loyada en 2026", "Confirmación en FCDO, autoridades de Yibuti o relato de viajero de 2026, más allá del folleto de una agencia."),
        ("Cobertura de Starlink en Somalilandia", "Comprobar el mapa oficial de starlink.com y la posición de la autoridad de telecomunicaciones de Hargeisa."),
        ("Requisitos de entrada del perro", "Respuesta por escrito del Ministry of Livestock, Forestry and Range (Info@molfr.gov.so) o publicación de un trámite oficial."),
        ("Fiebre amarilla: obligatoria o no", "Contraste entre el Reglamento Sanitario Internacional (NaTHNaC dice que no) y la exigencia real en frontera (MAEC y guías dicen que sí)."),
        ("Consulado honorario de España", "Confirmar en exteriores.gob.es si existe alguno en Mogadiscio o Hargeisa, o descartarlo expresamente."),
        ("Teléfonos locales de emergencia", "Verificar policía, ambulancia y bomberos en fuente oficial somalí; de momento solo consta el 446 de la Media Luna Roja en Mogadiscio."),
        ("Coordenadas exactas de los hospitales", "Fijar latitud y longitud del Hargeisa Group Hospital y del Hospital Erdoğan en GeoNames o fuente equivalente."),
        ("Normativa de drones en Somalilandia", "Texto de la autoridad de aviación civil somalilandesa o confirmación escrita de una embajada."),
        ("Seguro de vehículo válido", "Comprobar con OFESAUTO y con aseguradoras especializadas si existe alguna cobertura para Somalia o Somalilandia, o certificar que no la hay."),
        ("Tarifa oficial de la SPU", "Tarifa diaria publicada por el Gobierno de Somalilandia o por una agencia local en 2025-2026; las cifras que manejamos son de 2013 y 2017."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las páginas citadas arriba, todas abiertas durante la elaboración de este documento. Es una herramienta de planificación, no una autorización de viaje ni un sustituto de la recomendación oficial del MAEC, que desaconseja viajar a Somalia bajo cualquier circunstancia. Los datos de visados, permisos y fronteras cambian sin aviso —el caso del visado somalí anulado por Hargeisa en noviembre de 2025 lo demuestra— y hay que reconfirmarlos antes de cualquier decisión.",
    emergency="Emergencia consular española (Embajada en Nairobi, competente para Somalia): (+254) 733 631 144; centralita (+254) 20 272 02 22/3/4/5; emb.nairobi@maec.es. No hay embajada ni consulado de España en territorio somalí y el MAEC califica la asistencia consular de extremadamente difícil. En Mogadiscio existe el 446 gratuito de la Media Luna Roja Somalí (primeros auxilios y ambulancia, 24 horas) y el servicio voluntario Aamin Ambulance. Los números de policía y bomberos NO están verificados en fuente oficial. El contacto real en una crisis es la empresa de seguridad privada y el seguro de evacuación.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

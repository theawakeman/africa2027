# -*- coding: utf-8 -*-
"""Mauricio — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Mauricio está FUERA DE LA RUTA PREVISTA por ser insular, a 900 km al este de Madagascar. La app solo tiene un stub: créala entera con el formato del piloto de Túnez. ATENCIÓN, ESTO ES ÚNICO EN TODA LA GUÍA: **Mauricio SÍ figura en la lista del Reglamento de Ejecución (UE) 2026/636**, junto a Santa Elena y Ascensión, y es el ÚNICO país africano que aparece. Eso significa que el perro NO necesita la titulación antirrábica previa hecha en la UE (la «vía A» que exigen todos los demás países de esta guía): documenta con fuente cuál es el procedimiento real de vuelta a la UE desde un país listado, porque la ficha del perro de Mauricio es distinta de las otras cuarenta y tantas. Claves que DECIDEN la ficha y hay que documentar con fuente fechada: es la democracia más estable y con mejor gobernanza de África según Freedom House y el Índice Mo Ibrahim; las elecciones de noviembre de 2024 dieron un vuelco de gobierno; hay dos bienes del Patrimonio Mundial, Aapravasi Ghat y el Paisaje Cultural de Le Morne Brabant; y la isla de Rodrigues, a 560 km, es una dependencia autónoma con su propio carácter. Para el perro, Mauricio impone además una cuarentena de entrada muy estricta: compruébalo.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/mauricio.json y audit/pdi/mauricio.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Port Louis · el Caudan Waterfront y el mercado central", cat="Ciudad · servicios", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=-20.160863, lon=57.498089,  # Google Maps: Caudan Waterfront
        desc="Port Louis, fundada en 1638 y desarrollada por el gobernador francés Mahé de La Bourdonnais, concentra los 140.000 habitantes del casco y medio millón en su área metropolitana. El Caudan Waterfront, abierto en 1996 sobre una península portuaria que trabajó el azúcar durante 250 años, reúne tiendas, restaurantes, marina y el Blue Penny Museum, que guarda DOS DE LOS SELLOS MÁS RAROS DEL MUNDO. A pocas calles quedan el mercado central, el Champ de Mars —segundo hipódromo más antiguo del planeta— y la puerta del barrio chino. Aparcar en el centro es difícil y caro: usar el parking del Caudan y moverse a pie.",
        dog_note="El paseo del Caudan es zona comercial y el mercado central es alimentación: con perro, ni dentro del mercado ni en las tiendas; mejor dejarlo en el vehículo a la sombra o en el alojamiento.",
        visit={
            "why": "Es la base logística obvia de la isla: puerto, aduana, bancos, talleres y repuestos, y en la misma mañana se ven el frente marítimo colonial y el mercado que explica la mezcla india, criolla, china y europea del país.",
            "see": "El Caudan Waterfront y su marina, el Blue Penny Museum con los sellos Post Office de 1847, el mercado central, Place d'Armes, el Champ de Mars y la Citadelle (Fort Adelaide) sobre la ciudad.",
            "access": "Llegada por la autopista M1/M2; el Caudan tiene aparcamiento cubierto de varias plantas, con gálibo limitado para un 4x4 con baca o tienda de techo: comprobar altura antes de entrar y, si no cabe, dejar los coches en los aparcamientos de superficie del frente portuario. El pin marca el conjunto del Caudan Waterfront, no el mercado, que queda unos 400 m al noreste. Delincuencia común de poca entidad (hurtos y carteristas) señalada por el FCDO para Port Louis y Grand Baie: no dejar nada a la vista.",
            "when": "De lunes a sábado por la mañana, cuando el mercado está lleno; los domingos el centro se vacía. Evitar la hora punta de entrada y salida por la M1.",
            "skip": "Si solo hay un día en la isla y el interés es paisaje, se puede pasar de largo: Port Louis es trámite y ciudad, no postal.",
        },
        links=[
            {"label": "Wikipedia · Le Caudan Waterfront", "url": "https://en.wikipedia.org/wiki/Caudan_Waterfront"},
            {"label": "Wikipedia · Port Louis", "url": "https://en.wikipedia.org/wiki/Port_Louis"},
            {"label": "FCDO · Mauritius safety and security", "url": "https://www.gov.uk/foreign-travel-advice/mauritius/safety-and-security"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mauritius_Port-Louis_CaudanWaterfront.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mauritius_Port-Louis_CaudanWaterfront.JPG",
                "credit": "B.navez · CC BY-SA 3.0",
                "caption": "El Caudan Waterfront de Port Louis.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Port_Louis_Waterfront._(6719488523).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Port_Louis_Waterfront._(6719488523).jpg",
                "credit": "carrotmadman6 · CC BY 2.0",
                "caption": "El frente marítimo de Port Louis.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Port_Louis_Waterfront_-_Bank_of_Mauritius_(4716828179).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Port_Louis_Waterfront_-_Bank_of_Mauritius_(4716828179).jpg",
                "credit": "carrotmadman6 · CC BY 2.0",
                "caption": "El Banco de Mauricio, en el Caudan.",
            },
        ],
    ),
    dict(
        n=2, name="Aapravasi Ghat · el desembarcadero de los trabajadores contratados (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="medio día",
        lat=-20.158554, lon=57.5029509,  # Google Maps: Aapravasi Ghat World Heritage Site
        desc="Inscrito por la UNESCO en 2006 con el criterio (vi), Aapravasi Ghat es el depósito de inmigración de Trou Fanfaron por el que pasaron CERCA DE MEDIO MILLÓN de trabajadores contratados indios entre 1834 y 1920, el arranque de la diáspora moderna del trabajo por contrata que el Imperio británico ensayó tras abolir la esclavitud. De las instalaciones originales —alojamientos, cocinas, letrinas, hospital— quedan restos parciales de tres edificios de piedra y los catorce escalones de entrada. Es monumento nacional desde 1987. El sitio ocupa 1.640 m² y ha quedado tierra adentro por los rellenos del puerto.",
        dog_note="Recinto histórico cerrado con centro de interpretación y visita guiada: no entran animales; queda a diez minutos a pie del aparcamiento del Caudan, donde puede esperar uno de los viajeros con el perro.",
        visit={
            "why": "Es uno de los dos bienes mauricianos de la Lista del Patrimonio Mundial y la clave para entender por qué dos tercios de la población de Mauricio son de origen indio.",
            "see": "Los catorce escalones de piedra que subían los recién llegados, los restos del hospital y de los barracones, y el centro de interpretación del Aapravasi Ghat Trust Fund con los registros de inmigración.",
            "access": "En pleno Port Louis, junto a la carretera del puerto y a unos 800 m del Caudan Waterfront. No tiene aparcamiento propio utilizable por dos 4x4: dejar los vehículos en el Caudan y llegar andando. Entrada y horario no publicados en la ficha de la UNESCO: POR CONFIRMAR en el Trust Fund. El pin marca la puerta del recinto, en la Beach Street.",
            "when": "Primera hora de la mañana entre semana, antes del calor y del tráfico del puerto. Todo el año.",
            "skip": "Si el grupo va con prisa y ya ha visto Le Morne, este es el que se puede dejar: la carga es histórica, no visual.",
        },
        links=[
            {"label": "UNESCO · Aapravasi Ghat (ref. 1227)", "url": "https://whc.unesco.org/en/list/1227/"},
            {"label": "Wikipedia · Aapravasi Ghat", "url": "https://en.wikipedia.org/wiki/Aapravasi_Ghat"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Apravasi_Ghat_Mauritius_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Apravasi_Ghat_Mauritius_02.jpg",
                "credit": "Suyash Dwivedi · CC BY-SA 4.0",
                "caption": "El Aapravasi Ghat, el desembarcadero de los trabajadores contratados.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Aapravasi_ghat_museum,_Port_Louis,_Mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Aapravasi_ghat_museum,_Port_Louis,_Mauritius.jpg",
                "credit": "Ashish Bhatnagar · CC BY-SA 3.0",
                "caption": "El museo del Aapravasi Ghat.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Old_monument_at_Aapravasi_ghat_museum,_Port_Louis,_Mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Old_monument_at_Aapravasi_ghat_museum,_Port_Louis,_Mauritius.jpg",
                "credit": "Ashish Bhatnagar · CC BY-SA 3.0",
                "caption": "Restos del antiguo depósito de inmigración.",
            },
        ],
    ),
    dict(
        n=3, name="Le Morne Brabant · la montaña de los cimarrones (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=-20.45194, lon=57.32833,  # Google Maps: Le Morne Brabant (coordenada de la fuente; Google solo da un centroide redondeado)
        desc="Monolito basáltico de 556 m que cierra la punta suroeste de la isla, inscrito por la UNESCO en 2008 con los criterios (iii) y (vi) como Paisaje Cultural de Le Morne: 349,6 ha de bien y 2.405 de zona tampón. Sus cuevas y cornisas sirvieron de refugio a los esclavos fugados —los cimarrones— durante los siglos XVIII y XIX, y la tradición oral cuenta que, al llegar en 1835 una expedición policial a anunciar la abolición, los de la cima se arrojaron al vacío creyendo que venían a recapturarlos. ES EL SÍMBOLO NACIONAL DE LA RESISTENCIA A LA ESCLAVITUD.",
        dog_note="La pista de aproximación y la primera mitad del sendero son terreno abierto y se pueden hacer con el perro atado; la trepada final es roca con manos y exposición, y ahí no sube el animal.",
        visit={
            "why": "Une en un solo sitio la mejor caminata de Mauricio, la playa más fotografiada del país y la memoria del cimarronaje, que la UNESCO considera de valor universal por su eco en África, Madagascar, India y el Sudeste Asiático.",
            "see": "La subida por la ladera este con vistas a la laguna, la meseta intermedia con la cruz y el mirador, la cima a 556 m y, abajo, las playas de Le Morne y la barra de arrecife.",
            "access": "Asfalto bueno por la B9 hasta el pie de la montaña; el acceso al sendero termina en un aparcamiento de tierra donde caben sin problema dos 4x4. La marcha es de 5 a 8 km y de 3,5 a 4,5 horas ida y vuelta; el tramo superior tiene roca donde hay que usar las manos y exposición, y las fuentes locales recomiendan guía para llegar a la cima. Horario de la barrera: POR CONFIRMAR. El pin marca el aparcamiento del sendero, no la cumbre.",
            "when": "Salir antes de las 7:00 para evitar el calor y llegar con la roca seca; no subir con lluvia ni con roca mojada.",
            "skip": "Si llueve o el viento sopla fuerte en la meseta, quedarse abajo: la parte alta es resbaladiza y expuesta.",
        },
        links=[
            {"label": "UNESCO · Le Morne Cultural Landscape (ref. 1259)", "url": "https://whc.unesco.org/en/list/1259/"},
            {"label": "Wikipedia · Le Morne Brabant", "url": "https://en.wikipedia.org/wiki/Le_Morne_Brabant"},
            {"label": "Trekking Mauritius · guía de la subida a Le Morne", "url": "https://www.trekkingmauritius.com/guide-to-le-morne-hike/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Le_Morne_Brabant.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Le_Morne_Brabant.jpg",
                "credit": "LisanneD · CC BY-SA 4.0",
                "caption": "Le Morne Brabant.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Le_Morne,_Mauritius.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Le_Morne,_Mauritius.JPG",
                "credit": "Dávid Máth · CC0",
                "caption": "La montaña de los cimarrones.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Le_Morne_Mauritius_tunliweb_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Le_Morne_Mauritius_tunliweb_01.jpg",
                "credit": "Svein-Magne Tunli · CC BY-SA 4.0",
                "caption": "La península de Le Morne.",
            },
        ],
    ),
    dict(
        n=4, name="Parque nacional de Black River Gorges · el último bosque nativo", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=-20.4085255, lon=57.4717554,  # Google Maps: Le Pétrin Information Centre
        desc="Proclamado el 15 de junio de 1994 y con 67,54 km², es el mayor parque nacional del país y guarda EL ÚLTIMO BOSQUE NATIVO DE MAURICIO, lo poco que sobrevivió a tres siglos de caña de azúcar. En sus 60 km de senderos viven la paloma rosada, el cernícalo de Mauricio, la cotorra de Mauricio, el bulbul, el zosterops verde oliva y el zorro volador mauriciano. Tiene dos centros de información, Pétrin al este, a 2 km de Grand Bassin, y Black River al oeste. El acceso no tenía tarifa según las fuentes consultadas, pero el parque cierra a una hora que cambia con la estación: no quedarse dentro.",
        dog_note="Parque nacional con fauna endémica en recuperación —paloma rosada, cernícalo de Mauricio, cotorra de Mauricio—: los perros no entran en los senderos por riesgo de depredación y molestia a la avifauna.",
        visit={
            "why": "Es la única manera de ver cómo era Mauricio antes de la caña, y el único sitio de la isla donde se cruzan de golpe tres especies que estuvieron al borde de la extinción.",
            "see": "Los miradores de las gargantas y de las cataratas de Alexandra desde la carretera de Plaine Champagne, el sendero de Macchabée —unos 10 km y cuatro horas—, la cascada de Mare aux Joncs con unos 100 m de caída y, con suerte, la paloma rosada en los comederos.",
            "access": "Se entra por la B103 de Plaine Champagne, asfaltada y con miradores señalizados; el centro de Pétrin está 2 km al oeste de Grand Bassin y el de Black River a unos 8 km del cruce de Trois Bras. Aparcamientos de tierra amplios en ambos centros, de sobra para dos 4x4. Sin tarifa de entrada según la fuente consultada (donativo voluntario), horario variable por estación: preguntar en el centro antes de meterse en un sendero largo. El pin marca el centro de información de Pétrin.",
            "when": "De mayo a noviembre, la estación seca; salir temprano porque la meseta se nubla y llueve por la tarde casi a diario.",
            "skip": "Con lluvia fuerte el barro de los senderos y las nubes en los miradores lo dejan en nada: ese día, al sur costero.",
        },
        links=[
            {"label": "Wikipedia · Black River Gorges National Park", "url": "https://en.wikipedia.org/wiki/Black_River_Gorges_National_Park"},
            {"label": "Guía práctica con mapa de senderos del parque", "url": "https://mel365.com/black-river-gorges-national-park/"},
            {"label": "Wikipedia · Piton de la Petite Rivière Noire", "url": "https://en.wikipedia.org/wiki/Piton_de_la_Petite_Rivi%C3%A8re_Noire"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Black_River_Gorges_National_Park,_Mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Black_River_Gorges_National_Park,_Mauritius.jpg",
                "credit": "Adamina · CC BY 2.0",
                "caption": "Las gargantas del Black River.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/BlackRiverGorges.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:BlackRiverGorges.jpg",
                "credit": "Mauritiustrip · Public domain",
                "caption": "El bosque nativo del parque.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Black_river_gorges_national_park_2019-09-28.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Black_river_gorges_national_park_2019-09-28.jpg",
                "credit": "Z thomas · CC BY-SA 4.0",
                "caption": "Mirador sobre las gargantas.",
            },
        ],
    ),
    dict(
        n=5, name="Tierras de Siete Colores de Chamarel y su cascada", cat="Naturaleza", prio="Alta",
        dog="por confirmar", time="medio día",
        lat=-20.4400767, lon=57.3731676,  # Google Maps: Chamarel Seven Colored Earth Geopark
        desc="Dunas de arena en las que el basalto descompuesto se convirtió en arcilla y luego, por hidrólisis total, en suelo ferralítico: el hierro tiñe de rojo y antracita y el aluminio de azul y violeta, y el resultado son SIETE COLORES que no se mezclan aunque se remuevan. Se ven desde miradores de madera —ya no se puede pisarlas— y son atracción turística desde los años sesenta. En el mismo recinto, 1,5 km antes, cae la cascada de Chamarel, de unos 95 m, la más alta de la isla. Es visita de pago y cerrada: horario y tarifa, comprobar en taquilla.",
        dog_note="Recinto privado de pago con pasarelas y tortugas gigantes en cercado: la política de mascotas no aparece publicada; dar por hecho que no y preguntar en taquilla.",
        visit={
            "why": "Es la imagen geológica más reconocible de Mauricio y se resuelve en una hora larga, con la cascada más alta del país incluida en el mismo billete.",
            "see": "Las dunas de siete colores desde las plataformas de madera, el mirador de la cascada de Chamarel y los corrales de tortugas gigantes del recinto.",
            "access": "Carretera de montaña estrecha y con curvas desde Case Noyale o desde Plaine Champagne, asfaltada y sin dificultad para los dos vehículos; dentro del recinto se circula por pista de tierra hasta los aparcamientos de cada mirador, amplios. Entrada de pago; horario y tarifa POR CONFIRMAR en la taquilla. El pin marca la entrada y taquilla del geoparque, no las dunas.",
            "when": "A primera hora de la mañana, cuando la luz rasante y la humedad realzan los colores; de mayo a noviembre en seco.",
            "skip": "A mediodía y con sol alto los colores se aplanan y la parada pierde sentido; si el día está cubierto, mejor otro.",
        },
        links=[
            {"label": "Wikipedia · Seven Coloured Earths", "url": "https://en.wikipedia.org/wiki/Seven_Coloured_Earths"},
            {"label": "Wikipedia · Chamarel", "url": "https://en.wikipedia.org/wiki/Chamarel"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Seven_coloured_earths_mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Seven_coloured_earths_mauritius.jpg",
                "credit": "Moongateclimber · CC BY-SA 3.0",
                "caption": "Las tierras de siete colores de Chamarel.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mauritius_Seven_Colored_Earths_1.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mauritius_Seven_Colored_Earths_1.JPG",
                "credit": "Martin Falbisoner · CC BY-SA 4.0",
                "caption": "Las dunas teñidas de Chamarel.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Seven_Coloured_Earths,_Chamarel,_March_2020_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Seven_Coloured_Earths,_Chamarel,_March_2020_(1).jpg",
                "credit": "Benoît Prieur · CC0",
                "caption": "Detalle de las tierras de colores.",
            },
        ],
    ),
    dict(
        n=6, name="Grand Bassin (Ganga Talao) · el lago sagrado hindú", cat="Cultura", prio="Alta",
        dog="prohibido", time="medio día",
        lat=-20.4180203, lon=57.4917217,  # Google Maps: Ganga Talao
        desc="Lago de cráter a 550 m de altitud en la meseta central, el lugar más sagrado del hinduismo mauriciano. La tradición arranca en 1887, cuando el pandit Jhummun Giri dijo haber visto en sueños que sus aguas conectaban con el Ganges; en 1972 se vertió en él agua traída del río indio y en 1998 fue declarado lago sagrado. En Maha Shivaratri, MEDIO MILLÓN DE PEREGRINOS llegan a pie desde toda la isla cargando kanvars de madera y papel. A la entrada, el Mangal Mahadev, un Shiva de 33 m inaugurado en 2007, es la estatua más alta del país.",
        dog_note="Recinto religioso hindú en activo con templos y agua sagrada: los animales no entran; el perro se queda en el vehículo, en el aparcamiento con sombra.",
        visit={
            "why": "Es el corazón religioso del Mauricio indio y, fuera de la peregrinación, un cráter tranquilo con templos y monos a 550 m, a diez minutos del parque nacional.",
            "see": "El lago, los templos de la orilla, la estatua de 33 m de Mangal Mahadev y la de Durga frente a ella, y los peregrinos dejando ofrendas.",
            "access": "Asfalto en buen estado desde la B88 y desde Plaine Champagne; hay aparcamiento amplio junto a las estatuas, sin problema para dos 4x4. Acceso libre y gratuito. Descalzarse en los templos y vestir con hombros y rodillas cubiertos. El pin marca el aparcamiento de la explanada de las estatuas, no la orilla del lago.",
            "when": "Al amanecer, con niebla en el cráter y sin autocares. En Maha Shivaratri (febrero o marzo) la isla entera se mueve hacia aquí: espectacular, pero con carreteras cortadas y aparcamiento imposible.",
            "skip": "Los días de Maha Shivaratri, si se va con vehículos grandes y perro: no hay manera de aparcar ni de circular.",
        },
        links=[
            {"label": "Wikipedia · Ganga Talao", "url": "https://en.wikipedia.org/wiki/Ganga_Talao"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ganga_Talao_(5489050038).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ganga_Talao_(5489050038).jpg",
                "credit": "carrotmadman6 · CC BY 2.0",
                "caption": "Ganga Talao, el lago sagrado.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Monkeys_near_Grand_Bassin_(3041169662).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Monkeys_near_Grand_Bassin_(3041169662).jpg",
                "credit": "mwanasimba · CC BY-SA 2.0",
                "caption": "Macacos junto al Grand Bassin.",
            },
        ],
    ),
    dict(
        n=7, name="Trou aux Cerfs · el cráter de Curepipe", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=-20.315, lon=57.505,  # Google Maps: Trou aux Cerfs
        desc="Cráter de un volcán dormido en pleno Curepipe, a 605 m, con entre 300 y 350 m de diámetro y 80 m de profundidad, hoy cubierto de vegetación y con una laguna en el fondo. La última erupción se calcula HACE UNOS 700.000 AÑOS, aunque la ficha lo describe como dormido y capaz de despertar en los próximos mil años. Desde el borde se abarca la meseta central y, con el aire limpio, las montañas del oeste. El pueblo es el punto más alto y lluvioso de las ciudades del país: la niebla tapa el cráter con frecuencia.",
        dog_note="Mirador y paseo perimetral al aire libre, sin taquilla: el perro puede acompañar atado; no hay sombra en la vuelta al cráter.",
        visit={
            "why": "Es una parada de veinte minutos en el camino entre Port Louis y el sur que explica de un vistazo el origen volcánico de la isla.",
            "see": "El cráter con su laguna, la pista asfaltada de 1 km que da la vuelta al borde y la panorámica de la meseta central.",
            "access": "Se llega por calle asfaltada desde el centro de Curepipe; hay una pequeña explanada y aparcamiento en línea junto al mirador, justo para dos 4x4 si no está lleno. Acceso libre y gratuito. El pin marca el mirador y su aparcamiento, no el fondo del cráter.",
            "when": "Por la mañana temprano, antes de que suba la nube: Curepipe es la ciudad más lluviosa del país.",
            "skip": "Con niebla no se ve nada del cráter; en ese caso, seguir hacia Grand Bassin.",
        },
        links=[
            {"label": "Wikipedia · Trou aux Cerfs", "url": "https://en.wikipedia.org/wiki/Trou_aux_Cerfs"},
            {"label": "Wikipedia · Curepipe", "url": "https://en.wikipedia.org/wiki/Curepipe"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Trou-aux-cerfs.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Trou-aux-cerfs.jpg",
                "credit": "sharri (Flickr) · CC BY 2.0",
                "caption": "El cráter del Trou aux Cerfs.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_view_from_Trou_aux_Cerfs_(3006424405).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_view_from_Trou_aux_Cerfs_(3006424405).jpg",
                "credit": "mwanasimba · CC BY-SA 2.0",
                "caption": "Curepipe desde el Trou aux Cerfs.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Trou_aux_Cerfs_(3007262274).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Trou_aux_Cerfs_(3007262274).jpg",
                "credit": "mwanasimba · CC BY-SA 2.0",
                "caption": "El interior del cráter.",
            },
        ],
    ),
    dict(
        n=8, name="Pamplemousses · el Jardín Botánico Sir Seewoosagur Ramgoolam", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="medio día",
        lat=-20.1116867, lon=57.5726965,  # Google Maps: Jardín Botánico de Pamplemousses
        desc="Fundado en 1770 por Pierre Poivre, el intendente que quiso romper el monopolio holandés de las especias, es EL JARDÍN BOTÁNICO MÁS ANTIGUO DEL HEMISFERIO SUR y ocupa unas 37 ha. Su estanque de nenúfares gigantes Victoria amazonica, con hojas de más de un metro, es la postal del país; hay además no menos de ochenta especies de palmeras, varias endémicas de las Mascareñas, y la talipot, que florece una sola vez entre los treinta y los ochenta años y muere después. Se recorre en dos horas por caminos llanos y con sombra; horario y tarifa, comprobar en la puerta.",
        dog_note="Jardín botánico cerrado y de pago, con estanques y colecciones vegetales protegidas: no admite animales; el aparcamiento exterior tiene sombra de árboles grandes.",
        visit={
            "why": "Reúne en un paseo llano la historia colonial del comercio de especias, los nenúfares gigantes y la mayor colección de palmeras del Índico occidental.",
            "see": "El estanque de Victoria amazonica, la avenida de palmeras reales, la talipot, los ébanos, las tortugas gigantes del recinto y la puerta de hierro forjado de 1868.",
            "access": "A 11 km de Port Louis por la M2, asfalto bueno y señalización clara; hay aparcamiento de tierra frente a la puerta principal, amplio y con sombra, sin problema para dos 4x4. Entrada de pago y horario: POR CONFIRMAR en taquilla. El pin marca la puerta principal del jardín, en Pamplemousses.",
            "when": "De 9:00 a 11:00, antes del calor y de los grupos. Todo el año; los nenúfares están mejor en verano austral.",
            "skip": "Si el grupo ya ha visto jardines tropicales y va justo de días, es el más prescindible de los PDIs de prioridad alta.",
        },
        links=[
            {"label": "Wikipedia · Sir Seewoosagur Ramgoolam Botanical Garden", "url": "https://en.wikipedia.org/wiki/Sir_Seewoosagur_Ramgoolam_Botanical_Garden"},
            {"label": "Wikipedia · Pamplemousses District", "url": "https://en.wikipedia.org/wiki/Pamplemousses_District"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mon_Plaisir_im_Sir_Seewoosagur_Ramgoolam_Botanical_Garden.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mon_Plaisir_im_Sir_Seewoosagur_Ramgoolam_Botanical_Garden.jpg",
                "credit": "Lonelyplanet · CC BY-SA 3.0 de",
                "caption": "La casa de Mon Plaisir, en Pamplemousses.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Victoria_cruziana_pond_at_Sir_Seewoosagur_Ramgoolam_Botanical_Garden,_March_2020_(5).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Victoria_cruziana_pond_at_Sir_Seewoosagur_Ramgoolam_Botanical_Garden,_March_2020_(5).jpg",
                "credit": "Benoît Prieur · CC0",
                "caption": "El estanque de nenúfares gigantes.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pamplemousses,_Sir_Seewoosagur_Ramgoolam_Botanical_Garden,_Samadhi_Seewoosagur_Ramgoolam.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pamplemousses,_Sir_Seewoosagur_Ramgoolam_Botanical_Garden,_Samadhi_Seewoosagur_Ramgoolam.jpg",
                "credit": "Karsten Ratzke · CC0",
                "caption": "El samadhi de Seewoosagur Ramgoolam.",
            },
        ],
    ),
    dict(
        n=9, name="Île aux Cerfs y la costa este", cat="Costa", prio="Media",
        dog="no recomendado", time="medio día",
        lat=-20.2433824, lon=57.7836139,  # Google Maps: Trou d'Eau Douce
        desc="Isla privada frente a la costa este, en el distrito de Flacq, con playas de arena blanca, laguna somera en la que se puede caminar más de cien metros y un campo de golf de dieciocho hoyos. Se llega en lancha desde el embarcadero de Trou d'Eau Douce, el pueblo pesquero de unos 5.600 habitantes que vive de este tráfico. Es el sitio más masificado del país: a partir de las diez de la mañana los catamaranes descargan cientos de personas. NO ES UNA RESERVA: todo el suelo está concesionado y la playa pública es una franja.",
        dog_note="Isla privada a la que solo se llega en lancha compartida y con concesiones de playa y campo de golf: los operadores no suelen aceptar animales a bordo.",
        visit={
            "why": "Es la laguna turquesa de postal y, si se madruga, se disfruta una hora larga antes de que lleguen las excursiones organizadas.",
            "see": "La laguna somera y las playas del norte de la isla, la barra de arrecife y, de camino, la cascada del Grand River South East desde el barco.",
            "access": "Carretera costera B28 hasta Trou d'Eau Douce, asfalto bueno; aparcamiento junto al embarcadero, en tierra y limitado en temporada alta: llegar pronto con dos vehículos grandes. Lanchas de varias compañías desde primera hora; precio y horario, POR CONFIRMAR en el muelle. El pin marca el embarcadero de Trou d'Eau Douce, que es a donde se conduce, no la isla.",
            "when": "Primer barco de la mañana, sobre las 9:00. De mayo a noviembre el este está más ventoso pero con menos calor.",
            "skip": "En temporada alta y a mediodía, descartarlo: la masificación arruina la visita y Belle Mare da la misma playa sin barco.",
        },
        links=[
            {"label": "Wikipedia · Île aux Cerfs", "url": "https://en.wikipedia.org/wiki/%C3%8Ele_aux_Cerfs"},
            {"label": "Wikipédia · Trou d'Eau Douce", "url": "https://fr.wikipedia.org/wiki/Trou_d%27Eau_Douce"},
            {"label": "Wikipedia · Flacq District", "url": "https://en.wikipedia.org/wiki/Flacq_District"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/%C3%8Ele_aux_Cerfs.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:%C3%8Ele_aux_Cerfs.JPG",
                "credit": "MapiVanPelt · CC BY-SA 3.0",
                "caption": "La Île aux Cerfs.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ile_aux_Cerfs_(2994854930).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ile_aux_Cerfs_(2994854930).jpg",
                "credit": "mwanasimba · CC BY-SA 2.0",
                "caption": "La laguna de la Île aux Cerfs.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/%C3%8Ele_aux_Cerfs,_Mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:%C3%8Ele_aux_Cerfs,_Mauritius.jpg",
                "credit": "Adamina · CC BY 2.0",
                "caption": "Arena y turquesa en la isla.",
            },
        ],
    ),
    dict(
        n=10, name="Belle Mare y Trou d'Eau Douce · las playas del este", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=-20.1948426, lon=57.7767335,  # Google Maps: Belle Mare Beach
        desc="El este de Mauricio es la costa de arena blanca y casuarinas, con la laguna más ancha de la isla protegida por el arrecife. Belle Mare y Palmar forman el tramo de playa pública más largo del país y Trou d'Eau Douce, al sur, es el pueblo pesquero con el embarcadero a la Île aux Cerfs. Aquí sopla el alisio del sureste casi todo el año: menos calor que en el oeste y más viento. LA LEY MAURICIANA PROHÍBE LAS PLAYAS PRIVADAS —el Pas Géométriques deja la franja litoral en dominio público—, aunque los hoteles ocupan la parte de atrás.",
        dog_note="Playas públicas del dominio estatal: el perro puede ir atado fuera de las concesiones hoteleras, recogiendo siempre; en los tramos de hotel, no.",
        visit={
            "why": "Es el mejor sitio de la isla para un día sin plan: playa pública larga, sombra de filaos, agua somera y aparcamiento a pie de arena.",
            "see": "La playa pública de Belle Mare con sus casuarinas, la laguna turquesa hasta la barra de arrecife, los pescadores de Trou d'Eau Douce y la caleta de Palmar.",
            "access": "Carretera costera B28/A4, asfalto bueno y llano; hay varios aparcamientos públicos de tierra a pie de playa con sitio de sobra para dos 4x4. Acceso libre y gratuito a las 126 playas públicas identificadas por la Beach Authority. El pin marca el aparcamiento de la playa pública de Belle Mare. Coordenadas del distrito: el lugar no tiene artículo propio en Wikipedia, POR CONFIRMAR con precisión.",
            "when": "De mayo a noviembre, con alisio fresco; en enero y febrero, vigilar los avisos de ciclón.",
            "skip": "Con aviso de ciclón o mar de fondo, salir de la costa este: es la más expuesta al alisio.",
        },
        links=[
            {"label": "Wikipedia · Flacq District", "url": "https://en.wikipedia.org/wiki/Flacq_District"},
            {"label": "Wikipédia · Trou d'Eau Douce", "url": "https://fr.wikipedia.org/wiki/Trou_d%27Eau_Douce"},
            {"label": "Expat.com · lo que permite la ley en las playas de Mauricio", "url": "https://www.expat.com/en/expat-mag/11660-mauritius-beaches-what-the-law-allows.html"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mauritius_belle_mare_beach.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mauritius_belle_mare_beach.jpg",
                "credit": "Arne Müseler · CC BY-SA 3.0 de",
                "caption": "La playa de Belle Mare.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Flacq,_Belle_Mare.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Flacq,_Belle_Mare.jpg",
                "credit": "Guillaume · CC BY 2.0",
                "caption": "La costa este en Belle Mare.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/2011-06-26_12-03-32_Mauritius_Flacq_Belle_Mare_3hl.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:2011-06-26_12-03-32_Mauritius_Flacq_Belle_Mare_3hl.JPG",
                "credit": "Autor desconocido (panorama) · CC BY-SA 3.0",
                "caption": "Belle Mare, en el distrito de Flacq.",
            },
        ],
    ),
    dict(
        n=11, name="Grand Baie y la costa norte", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=-20.0089204, lon=57.5816352,  # Google Maps: Grand Baie
        desc="Con unos 11.900 habitantes en 2011, Grand Baie es la capital turística del norte: bahía cerrada llena de barcos, restaurantes, buceo y el centro comercial La Croisette, el tercero construido en el país. Es la base logística del norte —bancos, supermercados, talleres, gasolineras— y el puerto natural de salida hacia los islotes de Coin de Mire, Île Plate e Îlot Gabriel. La playa urbana de La Cuvette es pequeña pero pública. EL FCDO SEÑALA GRAND BAIE Y PORT LOUIS como los puntos donde más se dan los hurtos a turistas.",
        dog_note="La playa pública de La Cuvette y el paseo admiten perro atado; en los restaurantes, el centro comercial La Croisette y las lanchas de excursión, no.",
        visit={
            "why": "Es el sitio donde reabastecerse, arreglar papeles y contratar la salida a los islotes del norte, con playa pública a cien metros.",
            "see": "La bahía y su flota de catamaranes, la playa de La Cuvette, el paseo de Royal Road y, a quince minutos, Cap Malheureux y la iglesia del techo rojo.",
            "access": "Carretera B13 y A5 desde Port Louis, asfalto bueno; aparcamiento en calle y en las explanadas de la bahía, con sitio para dos 4x4 fuera de las horas punta. Acceso libre. El pin marca la playa pública de La Cuvette, que tiene aparcamiento propio. Cuidado con los hurtos de bolsos y con lo que se deja a la vista en el coche.",
            "when": "Entre semana y fuera de las vacaciones escolares mauricianas; de mayo a noviembre el mar está más tranquilo en el norte.",
            "skip": "Si se busca tranquilidad, Grand Baie no es el sitio: dormir en Cap Malheureux o en Pereybère y venir solo a comprar.",
        },
        links=[
            {"label": "Wikipedia · Grand Baie", "url": "https://en.wikipedia.org/wiki/Grand_Baie"},
            {"label": "FCDO · Mauritius safety and security", "url": "https://www.gov.uk/foreign-travel-advice/mauritius/safety-and-security"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Grand-Baie-banner.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Grand-Baie-banner.jpg",
                "credit": "Nicolas1981 · CC BY-SA 4.0",
                "caption": "Grand Baie, en la costa norte.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Grand_Baie,_National_Coast_Guard.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Grand_Baie,_National_Coast_Guard.JPG",
                "credit": "Karsten Ratzke · CC0",
                "caption": "El puesto de guardacostas de Grand Baie.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Grand_Baie,_Bazar.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Grand_Baie,_Bazar.JPG",
                "credit": "Karsten Ratzke · CC0",
                "caption": "El bazar de Grand Baie.",
            },
        ],
    ),
    dict(
        n=12, name="Île aux Aigrettes · la reserva de la flora endémica", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="medio día",
        lat=-20.4205232, lon=57.7324845,  # Google Maps: Île aux Aigrettes
        desc="Islote de coral de 27 ha a 850 m de la costa sureste, declarado reserva natural en 1965 y gestionado por la Mauritian Wildlife Foundation como estación científica. Conserva EL ÚNICO FRAGMENTO QUE QUEDA EN EL MUNDO del bosque seco costero de Mauricio, con el ébano Diospyros egrettarum que le da nombre. Ahí viven palomas rosadas, fodis de Mauricio, escincos de Telfair, gecos diurnos y tortugas gigantes de Aldabra, introducidas para cumplir el papel ecológico de las tortugas mauricianas extinguidas. Se visita solo con guía, en barco desde Pointe Jérôme, y hay que reservar.",
        dog_note="Reserva natural con especies en peligro y visita guiada obligatoria en barco: ningún animal doméstico puede desembarcar, por riesgo de introducción de depredadores y patógenos.",
        visit={
            "why": "Es la mejor lección de conservación del Índico: un ecosistema reconstruido planta a planta y la posibilidad real de ver paloma rosada y escinco de Telfair en una hora y media.",
            "see": "El bosque de ébanos, las tortugas gigantes de Aldabra sueltas, la paloma rosada, el fody de Mauricio y el geco ornamentado diurno.",
            "access": "Embarque en Pointe Jérôme, junto a Mahébourg, al que se llega por asfalto bueno; aparcamiento de tierra en el embarcadero, suficiente para dos 4x4. Visita guiada obligatoria, con reserva previa en la Mauritian Wildlife Foundation; precio y horarios POR CONFIRMAR. El pin marca el embarcadero de Pointe Jérôme, no la isla.",
            "when": "Primera salida de la mañana, cuando los animales están activos y el sol aún no aprieta; todo el año.",
            "skip": "Sin reserva previa es probable quedarse fuera; si el mar está agitado, la travesía se cancela.",
        },
        links=[
            {"label": "Wikipedia · Île aux Aigrettes", "url": "https://en.wikipedia.org/wiki/%C3%8Ele_aux_Aigrettes"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ile_aux_Aigrettes_-_Mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ile_aux_Aigrettes_-_Mauritius.jpg",
                "credit": "Abu Shawka · CC0",
                "caption": "La Île aux Aigrettes.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Aldabra_tortoise_Ile_aux_Aigrettes_-_Mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Aldabra_tortoise_Ile_aux_Aigrettes_-_Mauritius.jpg",
                "credit": "Abu Shawka · CC0",
                "caption": "Tortuga gigante de Aldabra en la reserva.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Leiolopisma_telfairii_-_skink_on_Ile_aux_Aigrettes_-_Mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Leiolopisma_telfairii_-_skink_on_Ile_aux_Aigrettes_-_Mauritius.jpg",
                "credit": "Abu Shawka · CC0",
                "caption": "Escinco de Telfair, endémico de la isla.",
            },
        ],
    ),
    dict(
        n=13, name="Mahébourg y el museo naval · la bahía histórica", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=-20.4163245, lon=57.7033301,  # Google Maps: Mahebourg Museum
        desc="Población de unos 15.500 habitantes en el sureste, con nombre del gobernador francés Mahé de La Bourdonnais y trazado documentado desde el plano de Richemont de 1804. Su museo naval, instalado en una gran casa colonial rodeada de parque, cuenta LAS BATALLAS NAVALES ENTRE LA MARINA FRANCESA Y LA ROYAL NAVY que se libraron en esta misma bahía de Grand Port. Es el pueblo más auténtico del sur, con mercado y frente marítimo, y queda a diez minutos del aeropuerto y del embarcadero de la Île aux Aigrettes. Aparcar es fácil salvo en día de mercado.",
        dog_note="El museo no admite animales y el mercado del lunes es alimentación; el paseo de Pointe Canon y el frente de la bahía sí se pueden hacer con el perro atado.",
        visit={
            "why": "Es la ciudad histórica del sureste y el mejor sitio para entender la rivalidad franco-británica que decidió el destino de la isla, con el embarcadero a Île aux Aigrettes al lado.",
            "see": "El museo naval en su casa colonial, el frente de la bahía de Grand Port, el mercado del pueblo y la vista a la Île aux Aigrettes y al Lion Mountain.",
            "access": "Asfalto bueno por la A10 desde el aeropuerto y por la costa desde Blue Bay; aparcamiento en calle amplio y gratuito salvo en día de mercado. Horario y entrada del museo: POR CONFIRMAR. El pin marca la puerta del museo naval. Las coordenadas de Wikipedia están redondeadas a tres decimales: POR CONFIRMAR con precisión.",
            "when": "Por la mañana, y si se puede el día de mercado; todo el año, con cuidado en temporada de ciclones.",
            "skip": "Si el museo está cerrado por obras —ha tenido cierres prolongados—, el pueblo solo da un paseo corto.",
        },
        links=[
            {"label": "Wikipedia · Mahébourg", "url": "https://en.wikipedia.org/wiki/Mah%C3%A9bourg"},
            {"label": "Wikipédia · Mahébourg (fr)", "url": "https://fr.wikipedia.org/wiki/Mah%C3%A9bourg"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Maheburg02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Maheburg02.jpg",
                "credit": "Anne97432 · CC BY-SA 1.0",
                "caption": "Mahébourg y su bahía.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mahebourg_Street_(16205715731).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mahebourg_Street_(16205715731).jpg",
                "credit": "Mark Fischer · CC BY-SA 2.0",
                "caption": "Una calle de Mahébourg.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Grand_Port_Battle_Memorial_in_Mah%C3%A9bourg,_Mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Grand_Port_Battle_Memorial_in_Mah%C3%A9bourg,_Mauritius.jpg",
                "credit": "ZoschH · CC BY-SA 4.0",
                "caption": "Memorial de la batalla de Grand Port.",
            },
        ],
    ),
    dict(
        n=14, name="Cap Malheureux y la iglesia del techo rojo", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=-19.9866358, lon=57.6222496,  # Google Maps: Notre-Dame Auxiliatrice de Cap Malheureux
        desc="La punta más septentrional de Mauricio, con la capilla de Notre-Dame Auxiliatrice y su tejado rojo recortado sobre la laguna, una de las postales más repetidas del país. El nombre —«cabo desdichado»— recuerda que POR AQUÍ DESEMBARCARON LOS BRITÁNICOS EN 1810, sorprendiendo a los franceses en el punto más débil de sus defensas del norte después de haber fracasado en el sur, en Grand Port. Enfrente, a ocho kilómetros, se levanta el perfil de Coin de Mire. Es parada corta: diez minutos de fotos y un café en el pueblo.",
        dog_note="El césped frente a la iglesia y la orilla son abiertos y se recorren con el perro atado; dentro de la capilla, no.",
        visit={
            "why": "Es el mejor mirador del norte hacia los islotes y un recordatorio de que aquí se decidió el cambio de bandera de la isla en 1810.",
            "see": "La capilla de techo rojo, la laguna, el perfil de Coin de Mire a ocho kilómetros y, con buena visibilidad, Île Plate más al norte.",
            "access": "Carretera costera B13, asfalto bueno; explanada de tierra y aparcamiento en línea junto a la iglesia, suficiente para dos 4x4 fuera de las horas punta. Acceso libre y gratuito. El pin marca la capilla de Notre-Dame Auxiliatrice, que es el objeto navegable.",
            "when": "Al final de la tarde, con la luz de poniente sobre el tejado rojo y la laguna; todo el año.",
            "skip": "A mediodía y con autocares, la parada no da mucho más que una foto: se puede encadenar con Grand Baie.",
        },
        links=[
            {"label": "Wikipedia · Cap Malheureux", "url": "https://en.wikipedia.org/wiki/Cap_Malheureux"},
            {"label": "Wikipedia · Islets of Mauritius", "url": "https://en.wikipedia.org/wiki/Islets_of_Mauritius"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Coin_de_Mire,_from_Cape_Malheureux,_Mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Coin_de_Mire,_from_Cape_Malheureux,_Mauritius.jpg",
                "credit": "Stefan Ivanovich · CC BY-SA 3.0",
                "caption": "El Coin de Mire desde Cap Malheureux.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cap_Malheureux_(2994852778).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cap_Malheureux_(2994852778).jpg",
                "credit": "mwanasimba · CC BY-SA 2.0",
                "caption": "La iglesia del techo rojo de Cap Malheureux.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/2011-06-26_09-17-37_Mauritius_Rivi%C3%A8re_du_Rempart_Cap_Malheureux_10hl.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:2011-06-26_09-17-37_Mauritius_Rivi%C3%A8re_du_Rempart_Cap_Malheureux_10hl.JPG",
                "credit": "Autor desconocido (panorama) · CC BY-SA 3.0",
                "caption": "La punta norte de la isla.",
            },
        ],
    ),
    dict(
        n=15, name="Eureka y las casas criollas de Moka", cat="Cultura", prio="Media",
        dog="prohibido", time="medio día",
        lat=-20.2179386, lon=57.4974066,  # Google Maps: Eureka - La Maison Créole
        desc="Casa criolla de madera construida en 1830 por un escocés apellidado Carr y comprada en 1863 por la familia Leclézio, que la conservó hasta 1985; es museo desde 1986. Tiene UNAS 109 PUERTAS Y VENTANAS, pensadas para ventilar el trópico sin aire acondicionado, y conserva mobiliario, mapas y vajilla de la época. Jean-Marie Le Clézio, premio Nobel de Literatura, la describió como el lugar más importante de su familia. En la finca bajan cascadas del río Moka. Hay restaurante y alojamiento; horario y tarifas, comprobar en la web oficial.",
        dog_note="Casa museo con mobiliario de época y visita guiada por el interior: no entran animales; el jardín y el camino a las cascadas, por confirmar en recepción.",
        visit={
            "why": "Es la mejor casa criolla abierta al público del país y explica de un vistazo cómo vivía la oligarquía azucarera francomauriciana del XIX.",
            "see": "Los salones con mobiliario de época y mapas antiguos, la cocina separada del cuerpo principal, la veranda perimetral y el sendero a las cascadas del río Moka.",
            "access": "A pocos minutos de la M1 por Moka, asfalto bueno y ramal corto de tierra hasta la casa; aparcamiento propio en el jardín, con sitio de sobra para dos 4x4. Entrada de pago; horario y tarifa POR CONFIRMAR en eureka-house.com. El pin marca la casa; las coordenadas son las del pueblo de Moka en Wikipedia, POR CONFIRMAR con precisión.",
            "when": "Por la mañana, antes de que suba la nube del interior; todo el año.",
            "skip": "Si ya se ha visitado una casa criolla en Reunión o en las Antillas, aporta poco nuevo.",
        },
        links=[
            {"label": "Eureka House · web oficial", "url": "https://www.eureka-house.com/"},
            {"label": "Wikipedia · Eureka House", "url": "https://en.wikipedia.org/wiki/Eureka_House"},
            {"label": "Wikipédia · Moka (Maurice)", "url": "https://fr.wikipedia.org/wiki/Moka_(Maurice)"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Moka_(6021581442).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Moka_(6021581442).jpg",
                "credit": "carrotmadman6 · CC BY 2.0",
                "caption": "Moka, el distrito de las casas criollas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mauritius_Moka-Range-from-Balaclava-Fort-01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mauritius_Moka-Range-from-Balaclava-Fort-01.jpg",
                "credit": "CEphoto, Uwe Aranas · CC BY-SA 3.0",
                "caption": "La sierra de Moka.",
            },
        ],
    ),
    dict(
        n=16, name="La Vanille y los criaderos de tortugas gigantes", cat="Naturaleza", prio="Media",
        dog="prohibido", time="medio día",
        lat=-20.4992338, lon=57.563272,  # Google Maps: La Vanille Nature Park
        desc="Creado en 1985 en Rivière des Anguilles, en el distrito de Savanne, reúne MÁS DE MIL TORTUGAS GIGANTES DE ALDABRA en semilibertad —la mayor manada en cautividad del mundo— y más de dos mil cocodrilos del Nilo, además de museos y un jardín de helechos junto al río. Abre todos los días de 9:00 a 17:00, incluidos festivos, y la entrada arranca en 450 rupias; las comidas de los cocodrilos son a las 11:30 y a las 14:30. Se recorre en dos horas por caminos llanos. La carretera de acceso desde el sur es estrecha y con curvas.",
        dog_note="Parque zoológico con más de dos mil cocodrilos del Nilo y tortugas en semilibertad: no admite perros, y el estrés para los animales del recinto sería evidente.",
        visit={
            "why": "Es el sitio donde el grupo puede tocar el papel de las tortugas gigantes en el ecosistema mauriciano, después de haberlas visto sueltas en Île aux Aigrettes.",
            "see": "La manada de tortugas gigantes de Aldabra, los estanques de cocodrilos del Nilo, el insectario y el jardín de helechos del cauce.",
            "access": "Asfalto estrecho y con curvas por la B9 y la A9 desde Souillac o desde Curepipe; aparcamiento propio de tierra con sitio para dos 4x4. Abierto de lunes a domingo, de 9:00 a 17:00, festivos incluidos; entrada desde 450 MUR. El pin marca la entrada del parque. Las coordenadas son las del distrito de Savanne en Wikipedia: Rivière des Anguilles no tiene coordenadas publicadas, POR CONFIRMAR.",
            "when": "Llegar hacia las 11:00 para coincidir con la comida de los cocodrilos de las 11:30; todo el año.",
            "skip": "Si el grupo no quiere ver animales en recinto, descartarlo: Île aux Aigrettes cubre la parte de conservación real.",
        },
        links=[
            {"label": "La Vanille Nature Park · web oficial", "url": "https://www.lavanillenaturepark.com/"},
            {"label": "Wikipédia · Rivière-des-Anguilles", "url": "https://fr.wikipedia.org/wiki/Rivi%C3%A8re-des-Anguilles"},
            {"label": "Wikipedia · Savanne District", "url": "https://en.wikipedia.org/wiki/Savanne_District"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/R%C3%A9serve_Fran%C3%A7ois_Leguat_1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:R%C3%A9serve_Fran%C3%A7ois_Leguat_1.jpg",
                "credit": "Gulnara Bektemirovna · CC BY 4.0",
                "caption": "Tortugas gigantes en criadero.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/R%C3%A9serve_Fran%C3%A7ois_Leguat_3.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:R%C3%A9serve_Fran%C3%A7ois_Leguat_3.jpg",
                "credit": "Gulnara Bektemirovna · CC BY 4.0",
                "caption": "Criadero de tortugas.",
            },
        ],
    ),
    dict(
        n=17, name="Rodrigues · Port Mathurin y la isla autónoma", cat="Costa", prio="Alta",
        dog="por confirmar", time="1–2 noches",
        lat=-19.6822952, lon=63.4205674,  # Google Maps: Port Mathurin
        desc="A 560 km al este de Mauricio, Rodrigues son 108 km² y unos 43.650 habitantes que desde el 12 de octubre de 2002 se gobiernan con su propia Asamblea Regional: ES LA ÚNICA DEPENDENCIA AUTÓNOMA DEL PAÍS y tiene otro carácter, criollo, rural y sin grandes hoteles. La descubrió el portugués Diogo Rodrigues en 1528 y en 1691 la colonizó el hugonote François Leguat; allí vivió el solitario de Rodrigues, palomo gigante no volador pariente del dodo, hoy extinguido. Port Mathurin, la capital, tiene unos 6.000 habitantes y el único puerto.",
        dog_note="El traslado desde Mauricio es en avión o en el barco de línea; el transporte de un perro en cualquiera de los dos y las reglas de la isla no están publicadas: consultar con la naviera y con los servicios veterinarios.",
        visit={
            "why": "Es el Mauricio que ya no existe en la isla grande: lagunas enormes, pueblos de pescadores y montes desnudos, con autonomía política propia desde 2002.",
            "see": "El mercado y el puerto de Port Mathurin, el Mont Limon de 398 m —el punto más alto—, la reserva de tortugas gigantes y cuevas François Leguat, y la reserva natural de la Île aux Cocos.",
            "access": "No hay conexión rodada: se llega en avión desde el aeropuerto de Plaisance, unos 90 minutos, o en el barco de línea desde Port Louis, con dos cargueros que fondean en Port Mathurin cinco veces al mes. LOS VEHÍCULOS DEL PROYECTO NO PASAN: hay que alquilar en la isla. Horarios y tarifas de barco y avión, POR CONFIRMAR. El pin marca el mercado de Port Mathurin, en el centro.",
            "when": "De mayo a noviembre, con el alisio. Evitar enero y febrero por los ciclones.",
            "skip": "Si no se dispone de tres días completos, no compensa: los traslados se comen el tiempo.",
        },
        links=[
            {"label": "Wikipedia · Rodrigues", "url": "https://en.wikipedia.org/wiki/Rodrigues"},
            {"label": "Wikipedia · Port Mathurin", "url": "https://en.wikipedia.org/wiki/Port_Mathurin"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Rodrigues_PortMathurinHarbour.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Rodrigues_PortMathurinHarbour.jpg",
                "credit": "B.navez · CC BY-SA 3.0",
                "caption": "El puerto de Port Mathurin, en Rodrigues.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Post_Office_in_Port_Mathurin.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Post_Office_in_Port_Mathurin.jpg",
                "credit": "Giorgio Minguzzi · CC BY-SA 2.0",
                "caption": "La oficina de correos de Port Mathurin.",
            },
        ],
    ),
    dict(
        n=18, name="Islote Gabriel y la Île Plate · los islotes del norte", cat="Naturaleza", prio="Media",
        dog="prohibido", time="medio día",
        lat=-19.886269, lon=57.6715337,  # Google Maps: Gabriel Island
        desc="Île Plate mide 2,53 km² y está 11 km al norte de Cap Malheureux, el extremo septentrional de la isla. En su lado suroeste sigue en servicio UN FARO DE 1855, uno de los pocos que quedan activos en Mauricio, y entre mediados del siglo XIX y los años treinta funcionó aquí la estación de cuarentena por la que pasaban los trabajadores contratados enfermos de cólera; quedan barracones, hospital y cementerio. Junto a ella, el Îlot Gabriel y Pigeon Rock forman con ella un área nacional protegida. Se visitan en catamarán desde Grand Baie, en excursión de día completo.",
        dog_note="Áreas nacionales protegidas a las que solo se llega en catamarán compartido: los operadores no llevan animales y la fauna de los islotes es especialmente vulnerable.",
        visit={
            "why": "Es la laguna más limpia del norte y una lección de historia desagradable y poco contada: la cuarentena que remataba el viaje de los trabajadores contratados.",
            "see": "La laguna del Îlot Gabriel, el faro de 1855, las ruinas del hospital y los barracones de cuarentena y el cementerio del siglo XIX.",
            "access": "No se conduce hasta aquí: el embarque es en Grand Baie o en Cap Malheureux, en catamarán de excursión, con salidas por la mañana y regreso a media tarde. Aparcamiento en las explanadas de Grand Baie, suficiente para dos 4x4. Precios y horarios de los operadores, POR CONFIRMAR. El pin marca la playa pública de Grand Baie, punto de embarque más habitual.",
            "when": "De mayo a noviembre, con el mar del norte más tranquilo; salida de la mañana.",
            "skip": "Con viento fuerte o mar de fondo las salidas se cancelan; y si ya se ha hecho Île aux Aigrettes, la parte naturalista se repite.",
        },
        links=[
            {"label": "Wikipedia · Île Plate", "url": "https://en.wikipedia.org/wiki/%C3%8Ele_Plate"},
            {"label": "Wikipedia · Islets of Mauritius", "url": "https://en.wikipedia.org/wiki/Islets_of_Mauritius"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Gabriel_Island_Mauritius.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Gabriel_Island_Mauritius.jpg",
                "credit": "dany13 · CC BY 2.0",
                "caption": "El islote Gabriel.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ilot_Gabriel_Mauritius_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ilot_Gabriel_Mauritius_01.jpg",
                "credit": "Algonkins · Public domain",
                "caption": "La laguna del islote Gabriel.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Gabriel_Island_as_seen_from_Flat_Island_in_Mauritius_(53698124019).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Gabriel_Island_as_seen_from_Flat_Island_in_Mauritius_(53698124019).jpg",
                "credit": "dronepicr · CC BY 2.0",
                "caption": "Gabriel visto desde la Île Plate.",
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
    ("Aeropuerto Internacional Sir Seewoosagur Ramgoolam (MRU)", "Frontera", -20.4334615, 57.6787266,  # Google Maps: Aeropuerto Internacional Sir Seewoosagur Ramgoolam
     "Plaine Magnien, a 48 km al sureste de Port Louis. Única puerta de entrada realista. Exención de visado de 90 días para españoles y «All in One travel form» previo obligatorio. Es también el punto de llegada del perro, que debe venir como carga manifestada. Pin comprobado en Google Maps («Aeropuerto Internacional Sir Seewoosagur Ramgoolam»)."),
    ("Puerto de Port Louis (único puerto de entrada del país)", "Frontera", -20.16444, 57.50417,  # Google Maps: Puerto de Port Louis (único puerto de entrada del país) (sin objeto en Google Maps; coordenada de la fuente)
     "Único Port of Entry oficial de Mauricio (Noonsite). Punto de despacho si algún día se enviaran los vehículos en contenedor o ro-ro, y terminal del ferry a Rodrigues. Pin comprobado en Google Maps («Puerto de Port Louis (único puerto de entrada del país) (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Consulado Honorario de España en Port Louis", "Consular", -20.1610549, 57.4989277,  # Google Maps: IBL House (Caudan)
     "Cónsul honorario D. Patrice Robert. Ground Floor, IBL House, Le Caudan Waterfront, Port Louis. Lunes a viernes de 9:00 a 12:00. Teléfonos +230 208 7289 y +230 208 2879; EMERGENCIAS fuera de horario +230 5729 3313; ch.portlouis@maec.es, con copia a consulates@iblgroup.com. Depende del Consulado General de España en Ciudad del Cabo. Pin comprobado en Google Maps («IBL House (Caudan)»)."),
    ("C-Care Wellkin Hospital, Moka", "Hospital", -20.2330351, 57.5039966,  # Google Maps: C-Care Wellkin
     "Royal Road, Moka. Hospital privado de referencia, abierto 24/7. Centralita +230 605 1000, urgencias 132. Es el centro privado más completo de la isla y está en la meseta central, a media hora de casi cualquier punto. Pin comprobado en Google Maps («C-Care Wellkin»)."),
    ("C-Care Darné, Floréal", "Hospital", -20.3128705, 57.5169105,  # Google Maps: C-Care Darné
     "Georges Guibert Street, Floréal (barrio de Curepipe). Clínica privada histórica del grupo C-Care. Centralita +230 601 2300, urgencias 118. Verificar la ubicación exacta en Floréal. Pin comprobado en Google Maps («C-Care Darné»)."),
    ("Quarantine Facility, Réduit (estación oficial de cuarentena animal)", "Hospital", -20.2313659, 57.4895998,  # Google Maps: Réduit
     "Instalación de la Livestock and Veterinary Division donde el perro cumple la cuarentena obligatoria de un mínimo de 5 días a Rs 15 por día. Visitas de lunes a sábado 9:00-11:00 y 13:00-14:30; domingos y festivos 9:00-12:00. COORDENADAS POR CONFIRMAR: Réduit está junto a Moka, y aquí se usan las de Moka como referencia provisional. Pin comprobado en Google Maps («Réduit»)."),
    ("Estaciones de servicio de la autopista M1, Port Louis", "Combustible", -20.16444, 57.50417,  # Google Maps: Estaciones de servicio de la autopista M1, Port Louis (sin objeto en Google Maps; coordenada de la fuente)
     "Red densa y moderna con pago con tarjeta y calidad europea. Precios oficiales desde el 15 de agosto de 2026: gasolina Rs 70,65/l y diésel Rs 71,25/l (State Trading Corporation). No hay racionamiento. Pin comprobado en Google Maps («Estaciones de servicio de la autopista M1, Port Louis (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Red de agua de la Central Water Authority, Port Louis", "Agua potable", -20.2891738, 57.5107777,  # Google Maps: Central Water Authority
     "Agua de red tratada y analizada en unos 160 puntos de muestreo con laboratorio ISO/IEC 17025. Vale para llenar depósitos de ducha y lavado en toda la isla; para beber, botella o filtro. Atención al cliente +230 601 5000 y línea directa 170. Pin comprobado en Google Maps («Central Water Authority»)."),
]

DRONE_CALLOUT = ("warn", "AUTORIZACIÓN PREVIA PARA CADA VUELO",
                 "Mauricio no prohíbe los drones, pero los somete a permiso del Department of Civil Aviation antes de cada vuelo, y a los visitantes los evalúa caso por caso, con licencia de piloto y registro del aparato. Los límites son 120 metros de altura, 50 metros de separación de personas, estructuras y vehículos, contacto visual permanente y prohibición de sobrevolar zonas densamente pobladas o concentraciones de más de 500 personas. En los foros de viajeros de 2025 y 2026 hay quejas de que el DCA no contesta a los correos de registro: hay que empezar el trámite con semanas de margen.")

STARLINK_CALLOUT = ("danger", "STARLINK NO ESTÁ AUTORIZADO EN MAURICIO",
                    "La Information and Communication Technologies Authority no ha licenciado el servicio. En agosto de 2023 la prensa local recogió que la ICTA lo había denegado alegando seguridad nacional y falta de control sobre el tráfico de internet; a finales de 2024 los residentes seguían informando de que la web de Starlink mostraba Mauricio «en espera», y en el recuento de cobertura mundial de mayo de 2026 el país no aparecía ni como disponible ni como próximo. No merece la pena cargar con el kit: la isla tiene fibra, 4G en todas partes y 5G en las zonas urbanas.")

DOG_MATRIX = [
    ("Entrada al país por MRU (como carga)", "permitido con condiciones", "Permiso previo con 3 meses de antelación, titulación antirrábica ≥0,5 UI/ml con 3 meses de espera, Ehrlichia y Brucella negativos en los 45 días previos, y 5 días de cuarentena en Réduit a Rs 15/día. Plan B: dejar al perro en España. Es el único país de la guía donde la cuarentena hace inviable una visita corta."),
    ("Vuelta a la UE desde Mauricio", "permitido con condiciones", "SIN titulación antirrábica previa hecha en la UE: Mauricio está en el Anexo II del Reg. de Ejecución (UE) 2026/636 y el art. 17.1.b) del Reg. Delegado (UE) 2026/131 exime de la prueba. Basta microchip, vacuna en vigor y pasaporte europeo, o certificado del Reg. 2026/705 firmado por veterinario oficial mauriciano, más declaración de no comercialidad y entrada por PEV autorizado. Plan B: ninguno necesario; es el regreso más sencillo de toda la guía."),
    ("Hoteles y resorts de playa", "no recomendado", "La gran mayoría de los resorts no admiten perros. Plan B: alquiler de villa o casa particular con autorización expresa y por escrito del propietario antes de reservar."),
    ("Playas públicas y lagunas", "por confirmar", "No hemos localizado ninguna norma nacional publicada sobre perros en playas públicas; la competencia está repartida entre la Beach Authority y las municipalidades. Plan B: preguntar a la Beach Authority y mantener al perro atado y fuera del agua."),
    ("Parques nacionales y reservas (Black River Gorges, Île aux Aigrettes, Le Morne)", "prohibido", "Las reservas gestionadas por el National Parks and Conservation Service protegen fauna endémica muy vulnerable y no admiten perros. Plan B: residencia canina en Quatre Bornes o Curepipe durante las excursiones."),
    ("Rodrigues (vuelo desde MRU o ferry desde Port Louis)", "por confirmar", "No hemos encontrado norma publicada sobre el traslado interior de animales a Rodrigues ni confirmación de que el MS Mauritius Trochetia los admita. Plan B: consultar por escrito a Air Mauritius y a la Mauritius Shipping Corporation (+230 217 2285) antes de comprar billete."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Mauricio (Ministerio de Asuntos Exteriores, UE y Cooperación, España; consultado en 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Mauricio"),
    ("MAEC · Ficha País Mauricio, PDF (Oficina de Información Diplomática, mayo de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/MAURICIO_FICHA%20PAIS.pdf"),
    ("Consulado General de España en Ciudad del Cabo · Demarcación y consulados honorarios (MAEC, consultado en 2026)", "https://www.exteriores.gob.es/Consulados/ciudaddelcabo/es/Consulado/Paginas/Demarcacion.aspx"),
    ("Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026, listas de terceros países para desplazamientos sin ánimo comercial de animales de compañía · texto consolidado en español (EUR-Lex, 2026)", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600636"),
    ("Reglamento de Ejecución (UE) 2026/636 · PDF del Diario Oficial (BOE, DOUE-L-2026-80458, 2026)", "https://www.boe.es/doue/2026/636/L00001-00007.pdf"),
    ("Reglamento de Ejecución (UE) 2026/636 · ficha del acto (EUR-Lex, CELEX 32026R0636, 2026)", "https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=CELEX%3A32026R0636"),
    ("MAPA · Viajar con la mascota: perros, gatos y hurones (Ministerio de Agricultura, Pesca y Alimentación, España, 2026)", "https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones"),
    ("MAPA · Viajar con perros, gatos y hurones: preguntas frecuentes (Ministerio de Agricultura, Pesca y Alimentación, España, 2026)", "https://www.mapa.gob.es/es/ganaderia/preguntas-frecuentes/preguntas-mascotas"),
    ("Sanitary and Phytosanitary Portal · Livestock and Veterinary Division: Imports (Gobierno de Mauricio, consultado en 2026)", "https://sps.govmu.org/lvd-imports/"),
    ("Guidelines to bring dogs to Mauritius, PDF (Ministry of Agro-Industry and Food Security, Mauricio, 2022)", "https://sps.govmu.org/wp-content/uploads/2022/12/2022-GUIDELINES-TO-BRING-DOGS-TO-MAURITIUS.pdf"),
    ("Health Certificate for Dogs and Cats to Mauritius, PDF (USDA APHIS, Estados Unidos)", "https://www.aphis.usda.gov/sites/default/files/mauritius-dogs-cats.pdf"),
    ("Pet Travel from the United States to Mauritius (USDA APHIS, actualizado el 19 de septiembre de 2025)", "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-mauritius"),
    ("Freedom in the World 2025: Mauritius (Freedom House, 2025)", "https://freedomhouse.org/country/mauritius/freedom-world/2025"),
    ("Foreign travel advice: Mauritius (FCDO, Reino Unido, actualizado el 4 de septiembre de 2026)", "https://www.gov.uk/foreign-travel-advice/mauritius"),
    ("Foreign travel advice: Mauritius · Safety and security (FCDO, Reino Unido, actualizado el 4 de septiembre de 2026)", "https://www.gov.uk/foreign-travel-advice/mauritius/safety-and-security"),
    ("Mauritius (Wikipedia en inglés, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Mauritius"),
    ("Port Louis (Wikipedia en inglés, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Port_Louis"),
    ("Curepipe (Wikipedia en inglés, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Curepipe"),
    ("Rodrigues (Wikipedia en inglés, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Rodrigues"),
    ("Sir Seewoosagur Ramgoolam International Airport (Wikipedia en inglés, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Sir_Seewoosagur_Ramgoolam_International_Airport"),
    ("Mauritius Shipping Corporation (Wikipedia en inglés, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Mauritius_Shipping_Corporation"),
    ("Visa policy of Mauritius (Wikipedia en inglés, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Visa_policy_of_Mauritius"),
    ("2025 in Mauritius (Wikipedia en inglés, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2025_in_Mauritius"),
    ("Mauritius Drone Laws 2026 (Drone Laws, actualizado el 21 de enero de 2026)", "https://drone-laws.com/drone-laws-in-mauritius/"),
    ("New Drone Laws · foro de Mauricio (Tripadvisor, hilo abierto en 2025, último mensaje en diciembre de 2025)", "https://www.tripadvisor.com/ShowTopic-g293816-i9265-k15025517-New_Drone_Laws-Mauritius.html"),
    ("Mapped: Where Starlink Is Available Around the World (Mappr, 10 de mayo de 2026)", "https://www.mappr.co/starlink-availability-by-country/"),
    ("Starlink Internet via Satellite: ICTA fears Lack of Control Over Internet Traffic (News Moris, 21 de agosto de 2023)", "https://newsmoris.com/starlink-internet-via-satellite-icta-fears-lack-of-control-over-internet-traffic/"),
    ("SpaceX Starlink · foro de Mauricio (Expat.com, mensajes hasta finales de 2024)", "https://www.expat.com/en/forum/africa/mauritius/1011895-spacex-starlink.html"),
    ("Relocating from U.K. 1 dog · air transport agents, foro de Mauricio (Expat.com)", "https://www.expat.com/forum/viewtopic.php?id=921582"),
    ("Cyclone Warning Class 3 Issued in Mauritius as Severe Tropical Storm Garance Intensifies (News Moris, 26 de febrero de 2025)", "https://newsmoris.com/cyclone-warning-class-3-issued-in-mauritius-as-severe-tropical-storm-garance-intensifies/"),
    ("State Trading Corporation · Press Release sobre precios del petróleo (STC Mauricio, comunicado de 15 de agosto de 2026)", "https://www.stcmu.com/ppm/press-release"),
    ("Mauritius diesel prices (GlobalPetrolPrices, dato de 9 de febrero de 2026)", "https://www.globalpetrolprices.com/Mauritius/diesel_prices/"),
    ("Private Importers · Customs (Mauritius Revenue Authority, consultado en 2026)", "https://www.mra.mu/customs1/import/private-importers"),
    ("Carnet de Passages en Douane · Mauritius (carnetdepassage.org, consultado en 2026)", "https://carnetdepassage.org/country/mauritius"),
    ("Mauritius · country information (TravelHealthPro / NaTHNaC, Reino Unido, consultado en 2026)", "https://travelhealthpro.org.uk/countries/mauritius"),
    ("C-Care Mauritius · hospitales y clínicas del grupo (C-Care, consultado en 2026)", "https://c-care.com/mu/"),
    ("C-Care Wellkin Hospital · ficha y coordenadas (Mapcarta, consultado en 2026)", "https://mapcarta.com/W389013882"),
    ("Water Quality (Central Water Authority, Gobierno de Mauricio, consultado en 2026)", "https://cwa.govmu.org/cwa/?page_id=813"),
    ("Drinking Tap Water in Mauritius: Safe or Not? (Tap Water Worldwide, publicado el 9 de febrero de 2026 y actualizado el 7 de agosto de 2026)", "https://tapwaterworldwide.com/mauritius/"),
    ("Mauritius · formalidades para navegantes (Noonsite, consultado en 2026)", "https://www.noonsite.com/place/mauritius/"),
    ("Marine Services · MS Mauritius Trochetia y ruta a Rodrigues (Mauritius Shipping Corporation, consultado en 2026)", "https://www.mauritiusshipping.net/coraline-services/"),
    ("Mauritius · States Parties, bienes del Patrimonio Mundial (UNESCO World Heritage Centre, consultado en 2026)", "https://whc.unesco.org/en/statesparties/mu"),
    ("Mauritius · perfil de país del Ibrahim Index of African Governance 2024 (Mo Ibrahim Foundation, IIAG Data Portal, 2024)", "https://iiag.online/locations/mu.html"),
    ("Arrival Travel Tips (Airport Terminal Operations Ltd, aeropuerto MRU, consultado en 2026)", "https://mru.airport.aero/passengers/travel-tips/arrival"),
    ("Rodrigues Island: Mauritius's Off-the-Beaten-Path Gem (HIDMC, blog de viajes)", "https://www.hidmc.com/blog-posts/rodrigues-island-mauritiuss-off-the-beaten-path-gem"),
    ("Driving in Mauritius: Expert Guide to Getting Around the Island (Our Soulful Travels, 2024)", "https://oursoulfultravels.com/driving-in-mauritius/"),
    ("Imports · Sanitary and Phytosanitary Portal, formulario de solicitud para animales de compañía, PDF (Gobierno de Mauricio, 2025)", "https://sps.govmu.org/wp-content/uploads/2025/05/APPLICATION-FORM-Pet-animals-Dog-Cat-others.pdf"),
    ("Wikipedia · Le Caudan Waterfront", "https://en.wikipedia.org/wiki/Caudan_Waterfront"),
    ("UNESCO · Aapravasi Ghat (ref. 1227)", "https://whc.unesco.org/en/list/1227/"),
    ("Wikipedia · Aapravasi Ghat", "https://en.wikipedia.org/wiki/Aapravasi_Ghat"),
    ("UNESCO · Le Morne Cultural Landscape (ref. 1259)", "https://whc.unesco.org/en/list/1259/"),
    ("Wikipedia · Le Morne Brabant", "https://en.wikipedia.org/wiki/Le_Morne_Brabant"),
    ("Trekking Mauritius · guía de la subida a Le Morne", "https://www.trekkingmauritius.com/guide-to-le-morne-hike/"),
    ("Wikipedia · Black River Gorges National Park", "https://en.wikipedia.org/wiki/Black_River_Gorges_National_Park"),
    ("Guía práctica con mapa de senderos del parque", "https://mel365.com/black-river-gorges-national-park/"),
    ("Wikipedia · Piton de la Petite Rivière Noire", "https://en.wikipedia.org/wiki/Piton_de_la_Petite_Rivi%C3%A8re_Noire"),
    ("Wikipedia · Seven Coloured Earths", "https://en.wikipedia.org/wiki/Seven_Coloured_Earths"),
    ("Wikipedia · Chamarel", "https://en.wikipedia.org/wiki/Chamarel"),
    ("Wikipedia · Ganga Talao", "https://en.wikipedia.org/wiki/Ganga_Talao"),
    ("Wikipedia · Trou aux Cerfs", "https://en.wikipedia.org/wiki/Trou_aux_Cerfs"),
    ("Wikipedia · Sir Seewoosagur Ramgoolam Botanical Garden", "https://en.wikipedia.org/wiki/Sir_Seewoosagur_Ramgoolam_Botanical_Garden"),
    ("Wikipedia · Pamplemousses District", "https://en.wikipedia.org/wiki/Pamplemousses_District"),
    ("Wikipedia · Île aux Cerfs", "https://en.wikipedia.org/wiki/%C3%8Ele_aux_Cerfs"),
    ("Wikipédia · Trou d'Eau Douce", "https://fr.wikipedia.org/wiki/Trou_d%27Eau_Douce"),
    ("Wikipedia · Flacq District", "https://en.wikipedia.org/wiki/Flacq_District"),
    ("Expat.com · lo que permite la ley en las playas de Mauricio", "https://www.expat.com/en/expat-mag/11660-mauritius-beaches-what-the-law-allows.html"),
    ("Wikipedia · Grand Baie", "https://en.wikipedia.org/wiki/Grand_Baie"),
    ("Wikipedia · Île aux Aigrettes", "https://en.wikipedia.org/wiki/%C3%8Ele_aux_Aigrettes"),
    ("Wikipedia · Mahébourg", "https://en.wikipedia.org/wiki/Mah%C3%A9bourg"),
    ("Wikipédia · Mahébourg (fr)", "https://fr.wikipedia.org/wiki/Mah%C3%A9bourg"),
    ("Wikipedia · Cap Malheureux", "https://en.wikipedia.org/wiki/Cap_Malheureux"),
    ("Wikipedia · Islets of Mauritius", "https://en.wikipedia.org/wiki/Islets_of_Mauritius"),
    ("Eureka House · web oficial", "https://www.eureka-house.com/"),
    ("Wikipedia · Eureka House", "https://en.wikipedia.org/wiki/Eureka_House"),
    ("Wikipédia · Moka (Maurice)", "https://fr.wikipedia.org/wiki/Moka_(Maurice)"),
    ("La Vanille Nature Park · web oficial", "https://www.lavanillenaturepark.com/"),
    ("Wikipédia · Rivière-des-Anguilles", "https://fr.wikipedia.org/wiki/Rivi%C3%A8re-des-Anguilles"),
    ("Wikipedia · Savanne District", "https://en.wikipedia.org/wiki/Savanne_District"),
    ("Wikipedia · Port Mathurin", "https://en.wikipedia.org/wiki/Port_Mathurin"),
    ("Wikipedia · Île Plate", "https://en.wikipedia.org/wiki/%C3%8Ele_Plate"),
]

# Bucle completo de la isla · Port Louis, norte, este, sureste, sur, oeste y meseta central (unos 400 km de asfalto)
CORRIDOR = [
    (-20.15855, 57.50295),
    (-20.11169, 57.5727),
    (-20.00892, 57.58164),
    (-19.98664, 57.62225),
    (-20.19484, 57.77673),
    (-20.24338, 57.78361),
    (-20.41632, 57.70333),
    (-20.42052, 57.73248),
    (-20.49923, 57.56327),
    (-20.41802, 57.49172),
    (-20.44008, 57.37317),
    (-20.45194, 57.32833),
    (-20.44008, 57.37317),
    (-20.41802, 57.49172),
    (-20.315, 57.505),
    (-20.21794, 57.49741),
    (-20.16086, 57.49809),
]

# Variante marítima · islotes del norte desde Grand Baie y salto a Rodrigues en barco o avión (sin vehículos propios)
CORRIDOR_ALT = [
    (-20.15855, 57.50295),
    (-20.00892, 57.58164),
    (-19.98664, 57.62225),
    (-19.88627, 57.67153),
    (-20.00892, 57.58164),
    (-20.15855, 57.50295),
    (-19.6823, 63.42057),
]

HISTORIA_RESUMEN = "Mauricio es una isla volcánica del océano Índico situada a unos 900 kilómetros al este de Madagascar que nunca tuvo población autóctona: todo lo que hay en ella llegó en barco. Neerlandeses, franceses y británicos la ocuparon sucesivamente entre 1598 y 1968, y sobre la caña de azúcar levantaron primero un sistema esclavista y después el mayor experimento mundial de trabajo por contrato, que trajo a cerca de medio millón de indios. De esa acumulación nació una sociedad hindú, criolla, musulmana y china que habla criollo, francés e inglés. Independiente desde 1968 y república desde 1992, es hoy la democracia mejor puntuada del continente según Freedom House 2025, con alternancia real de gobierno y una economía de servicios muy por encima de la media africana."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>Mauricio no tiene prehistoria humana. La isla, de origen volcánico y rodeada por un cinturón de arrecife coralino, formaba parte del archipiélago deshabitado de las Mascareñas y permaneció sin población permanente hasta finales del siglo XVI. No hubo, por tanto, reinos, jefaturas ni pueblos originarios: la referencia obligada en otros países africanos aquí simplemente no existe, y conviene saberlo antes de pisar la isla.</p><p>Lo que sí hubo fueron avistamientos. Navegantes árabes la conocían probablemente desde el siglo X y la habrían llamado <em>Dina Arobi</em>; los portugueses la visitaron a comienzos del siglo XVI —en 1505 según la versión española de Wikipedia, en 1507 según la inglesa— y la bautizaron <em>Ilha do Cisne</em>, pero no se establecieron en ella. Durante siglos fue una escala de aguada y de caza en la ruta hacia las Indias.</p><p>El único «pueblo» anterior a la llegada humana era una fauna endémica sin depredadores, cuyo emblema es el dodo, un ave no voladora extinguida pocas décadas después del primer asentamiento europeo y convertida desde entonces en el caso de manual de extinción provocada por el hombre.</p>"),
    ("Colonización",
     "<p>La colonización efectiva empieza en 1598, cuando el almirante neerlandés Wybrand van Warwyck toma posesión de la isla y la llama Mauricio en honor del príncipe Mauricio de Nassau. Los neerlandeses introdujeron la caña de azúcar y trajeron esclavos malgaches, pero el asentamiento nunca prosperó y fue abandonado en 1710.</p><p>Francia ocupó el vacío en 1715 y rebautizó el territorio como <em>Isle de France</em>. Bajo el gobernador Mahé de La Bourdonnais, Port Louis se convirtió en base naval y capital, y la economía azucarera despegó sobre el trabajo de esclavos africanos y malgaches. Los cimarrones que lograban huir se refugiaban en la montaña de Le Morne Brabant; esa historia oral es la que la UNESCO inscribió en 2008 como paisaje cultural y símbolo de la resistencia a la esclavitud.</p><p>Los británicos conquistaron la isla en 1810 y el Tratado de París de 1814 formalizó el traspaso, devolviéndole el nombre de Mauricio pero conservando el derecho civil francés, el idioma y los grandes propietarios. Abolida la esclavitud a partir de 1833 y de forma efectiva en 1835, Londres puso en marcha en 1834 su «gran experimento»: sustituir a los esclavos por trabajadores contratados. Entre 1834 y 1920 llegaron por el muelle de Aapravasi Ghat, en Port Louis, cerca de medio millón de indios. Ese recinto, Patrimonio Mundial desde 2006, marca el arranque de la diáspora moderna del trabajo por contrato.</p>"),
    ("Independencia y construcción del Estado",
     "<p>Mauricio accedió a la independencia dentro de la Commonwealth el 12 de marzo de 1968, bajo el liderazgo de Sir Seewoosagur Ramgoolam, considerado el padre de la patria y jefe del Partido Laborista. El país mantuvo a la reina británica como jefa de Estado representada por un gobernador general, un Parlamento unicameral heredado de Westminster y un sistema electoral con escaños adicionales de «mejor perdedor» pensado para garantizar la representación de las minorías —una pieza clave para que la convivencia entre comunidades no descarrilara.</p><p>Antes de marcharse, el Reino Unido había separado en 1965 el archipiélago de Chagos del territorio mauriciano para crear el Territorio Británico del Océano Índico e instalar con Estados Unidos la base de Diego García. Entre 1967 y 1973 unos dos mil chagosianos fueron expulsados o impedidos de regresar, la mayoría hacia Mauricio. El contencioso ha marcado la política exterior del país desde entonces.</p><p>La economía de la independencia era un monocultivo azucarero con fuerte desempleo. A partir de los años setenta y ochenta, con la zona franca de exportación, el textil y el turismo, el país empezó a diversificarse. El 12 de marzo de 1992 Mauricio se proclamó república dentro de la Commonwealth, con un presidente elegido por la Asamblea Nacional y un primer ministro como jefe efectivo del Gobierno.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>El siglo XXI mauriciano ha sido el de la consolidación de un modelo de servicios —banca <em>offshore</em>, seguros, tecnologías de la información y turismo de gama alta— y el de una alternancia política casi mecánica entre coaliciones encabezadas por dos dinastías: los Ramgoolam del Partido Laborista y los Jugnauth del Movimiento Socialista Militante. Navin Ramgoolam gobernó entre 1995 y 2000 y de nuevo entre 2005 y 2014; después el MSM encadenó una década en el poder.</p><p>En 2002 Rodrigues, la isla hermana situada 560 kilómetros al este, obtuvo autonomía regional con asamblea y consejo ejecutivo propios, un gesto de descentralización poco frecuente en la región.</p><p>En el plano internacional, el pulso por Chagos dio un vuelco: en 2015 la Corte Permanente de Arbitraje falló contra el Reino Unido en el asunto del área marina protegida y en febrero de 2019 la Corte Internacional de Justicia dictaminó, por trece votos contra uno, que Londres debía poner fin a su administración del archipiélago «lo antes posible». El 22 de mayo de 2025 ambos países firmaron un acuerdo por el que el Reino Unido cede la soberanía y arrienda Diego García durante 99 años. A fecha de septiembre de 2026 el acuerdo sigue sin ratificar: según la ficha del MAEC (mayo de 2026), Londres pausó la validación legislativa tras las objeciones de la administración estadounidense.</p>"),
    ("Política y gobierno en 2026",
     "<p>Mauricio es una república parlamentaria unitaria, con Parlamento unicameral de setenta escaños y un presidente elegido por la Asamblea Nacional para cinco años, según la Ficha País del MAEC de mayo de 2026. El jefe del Estado es <strong>Dharam Gokhool</strong>, desde el 6 de diciembre de 2024; el jefe del Gobierno es el primer ministro <strong>Navinchandra Ramgoolam</strong>, del Partido Laborista, hijo del padre de la independencia.</p><p>Llegó al poder por las urnas. En las legislativas de noviembre de 2024 la coalición Alianza por el Cambio arrasó: Freedom House habla de «victoria abrumadora, capturando 60 de los 62 escaños directamente elegidos». Las municipales de mayo de 2025 lo confirmaron con 117 de 120 concejalías. Las próximas generales corresponden al ciclo de 2029.</p><p>Es una democracia real, no una democracia limitada. Freedom House 2025 la clasifica como <strong>«Free»</strong> con <strong>86 sobre 100</strong> —35 de 40 en derechos políticos y 51 de 60 en libertades civiles—, la mejor nota del continente. La misma fuente señala como debilidades la corrupción persistente, agravada por el escándalo de las escuchas filtradas de 2024, y el acoso ocasional a periodistas. Reporteros Sin Fronteras lo sitúa en 2026 en el puesto 42 de 180. No hay conflicto armado ni problema de seguridad reseñable.</p><p>La Unión Europea es su primer socio comercial, con el 23,8 % del intercambio total. Con España las relaciones diplomáticas datan de 1979 y España es su cuarto socio europeo.</p>"),
    ("Economía y recursos",
     "<p>Mauricio no tiene minerales ni hidrocarburos: su riqueza son la gente, la posición y la reputación regulatoria. Según la Ficha País del MAEC de mayo de 2026, el PIB fue de unos 15.000 millones de dólares en 2024 y el PIB per cápita de unos <strong>12.000 dólares</strong>, con un crecimiento del 3,2 % y una inflación del 3,7 % en 2025 y un paro del 5,4 %, alto entre los jóvenes. La moneda es la rupia mauriciana; a primeros de enero de 2026 un euro equivalía a unas 54 rupias.</p><p>Los servicios superan el 70 % del PIB. Los servicios financieros y de seguros pesan un 13,4 %, el comercio un 11,2 % y el turismo un 8,5 %: en 2024 llegaron 1.382.177 visitantes, un 6,7 % más que el año anterior, dos tercios de ellos desde la Unión Europea. La manufactura, sobre todo textil y procesado de alimentos, aporta un 12,9 %, y el sector primario apenas un 4,9 %, con la caña de azúcar en declive relativo.</p><p>La balanza de bienes es muy deficitaria —1.720 millones de dólares exportados frente a 6.650 importados en 2024—, compensada por el superávit de servicios. Francia, Sudáfrica, Estados Unidos y el Reino Unido son los principales clientes; China, Emiratos, India y Sudáfrica, los proveedores. En Rodrigues la economía es otra: pesca, cebolla, ajo, guindilla, ganadería y artesanía.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>La población ronda los 1,25 millones de habitantes según el MAEC (2024) y es uno de los países más densamente poblados de África. Los idiomas oficiales son el francés y el inglés, pero cerca del 90 % de la gente habla criollo mauriciano, y es en criollo y en francés como uno se entiende por carretera; el inglés domina en la administración, y también se oyen bhojpuri, hindi y urdu. La población es mayoritariamente indomauriciana, con comunidades criolla, sinomauriciana y franco-mauriciana.</p><p>El censo de 2011 da un 48,5 % de hinduistas, un 32,7 % de cristianos y un 17,2 % de musulmanes. Es el único país africano donde el hinduismo es mayoritario, y eso se nota en el calendario: Maha Shivaratri, Thaipoosam Cavadee y Diwali conviven con la Navidad, el Eid al-Fitr, el Año Nuevo chino y el 1 de febrero —abolición de la esclavitud— y el 12 de marzo. La música identitaria es el <em>sega</em>, cantado en criollo al ritmo del tambor <em>ravanne</em>. La cocina mezcla India, África, China y Francia. El patrimonio UNESCO son Aapravasi Ghat y Le Morne Brabant.</p><p>Para el viajero: el bañador es normal en la playa, no fuera de ella, y en templos y mezquitas hay que cubrirse hombros y rodillas y descalzarse. Conviene pedir permiso antes de fotografiar a personas. Durante el ramadán, que en 2027 empieza en torno al 8 de febrero, es cortés no comer ni beber ante quien ayuna. El alcohol se vende sin restricciones.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Mauricio (MAEC España · Oficina de Información Diplomática · mayo de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/MAURICIO_FICHA%20PAIS.pdf"),
    ("Mauritius: Freedom in the World 2025 (Freedom House · informe de país · 2025)", "https://freedomhouse.org/country/mauritius/freedom-world/2025"),
    ("Mauritius — States Parties (UNESCO · Centro del Patrimonio Mundial · consultado en 2026)", "https://whc.unesco.org/en/statesparties/mu"),
    ("Aapravasi Ghat (UNESCO · Lista del Patrimonio Mundial · inscrito en 2006)", "https://whc.unesco.org/en/list/1227"),
    ("Le Morne Cultural Landscape (UNESCO · Lista del Patrimonio Mundial · inscrito en 2008)", "https://whc.unesco.org/en/list/1259"),
    ("Mauritius (Wikipedia en inglés · artículo de país · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Mauritius"),
    ("Historia de Mauricio (Wikipedia en español · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Historia_de_Mauricio"),
    ("Mauricio (Wikipedia en español · artículo de país · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Mauricio"),
    ("Rodrigues (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Rodrigues"),
    ("Chagos Archipelago sovereignty dispute (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Chagos_Archipelago_sovereignty_dispute"),
    ("Mauritius — Press Freedom Index (Reporteros Sin Fronteras · índice 2026)", "https://rsf.org/en/country/mauritius"),
    ("Mauritius — Ibrahim Index of African Governance Data Portal (Mo Ibrahim Foundation · edición 2024)", "https://iiag.online/locations/mu.html"),
    ("Reglamento de Ejecución (UE) 2026/636, de 20 de marzo de 2026, listas de terceros países para desplazamientos de animales de compañía (DOUE · BOE)", "https://www.boe.es/doue/2026/636/L00001-00007.pdf"),
    ("Guidelines to bring dogs to Mauritius (Ministry of Agro-Industry and Food Security · portal SPS · 2022)", "https://sps.govmu.org/wp-content/uploads/2022/12/2022-GUIDELINES-TO-BRING-DOGS-TO-MAURITIUS.pdf"),
    ("Mauritius (Encyclopaedia Britannica · página de país · consultado en septiembre de 2026)", "https://www.britannica.com/place/Mauritius"),
    ("International rankings of Mauritius (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/International_rankings_of_Mauritius"),
]

SPEC = dict(
    slug="mauricio", name="Mauricio", revision="18 sep 2026",
    sub="FUERA DE RUTA — isla a 900 km al este de Madagascar, sin travesía de vehículos desde el continente · ÚNICO país africano en la lista UE del perro · se conduce por la izquierda",
    chips=[
        ("ESTATUS", "FUERA DE RUTA. Insular, a unos 900 km al este de Madagascar…"),
        ("CÓMO LLEGAR", "Solo en avión: Aeropuerto Internacional Sir Seewoosagur Ramgoolam (MRU), en Plaine Magnien…"),
        ("VISADO", "SIN VISADO para españoles: 90 días por visita y hasta 180 días de turismo por año natural…"),
        ("VEHÍCULO", "Sin procedimiento publicado de admisión temporal para vehículo de turista…"),
        ("SEGURIDAD", "Viajar con precaución · sin zonas desaconsejadas"),
        ("SEGURO", "Fuera del sistema de Carta Verde · seguro local"),
        ("SALUD", "Sin vacunas obligatorias desde España · chikungunya"),
        ("DRONES", "Permiso del DCA antes de cada vuelo · caso por caso"),
        ("STARLINK", "No autorizado por la ICTA · fibra y 4G/5G"),
        ("4x4", "Innecesario · asfalto y conducción por la izquierda"),
        ("A PIE", "Sí · Black River Gorges, Le Morne y Le Pouce"),
        ("PERRO", "ENTRADA DURA: permiso previo con 3 meses de antelación, titulación antirrábica ≥0,5 UI/ml con 3 meses de…"),
        ("MONEDA", "Rupia mauriciana (MUR). 1 € = 54,36 MUR según la Ficha País del MAEC de mayo de 2026…"),
        ("VENTANA", "Tropical. Temporada de ciclones de mediados de noviembre a mediados de abril según el…"),
    ],
    center=[-20.09, 60.37], zoom=6,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle completo de la isla · Port Louis, norte, este, sureste, sur, oeste y meseta central (unos 400 km de asfalto)",
    corridor_alt_label="Variante marítima · islotes del norte desde Grand Baie y salto a Rodrigues en barco o avión (sin vehículos propios)",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Le_Morne_Brabant.jpg?width=1200",
    hero_credit="Le Morne Brabant · LisanneD · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Mauricio queda fuera de la ruta de 2027 por geografía, no por riesgo: es una isla de 2.045 km² en pleno Índico, a unos 900 km al este de Madagascar, y NO existe travesía regular de vehículos entre el continente africano y Port Louis. Meter el Grenadier y la Delica exigiría flete marítimo en contenedor o ro-ro desde Durban, Mombasa o Europa, con despacho en el único puerto de entrada del país. La Mauritius Revenue Authority solo publica el régimen general de admisión temporal de mercancías —reexportación en seis meses, validez máxima de doce, depósito de garantía— sin procedimiento específico para vehículo de turista, y AIT/FIA no tiene organización emisora de carnet de passages en la isla. Encima se conduce por la IZQUIERDA y hay asfalto en todas partes: el 4x4 no aporta nada. Si algún día se hace, se hace aparte y sin coches: vuelo desde Barcelona con escala en Estambul, Dubái, París o Johannesburgo, una o dos semanas, coche de alquiler y, si se quiere el contraste, el salto a Rodrigues en avión (90 minutos) o en el Mauritius Trochetia (36 horas). Lo que habría que decidir de verdad es el perro: Mauricio exige permiso previo con tres meses de antelación, titulación antirrábica, serologías de Ehrlichia y Brucella, viaje como CARGA manifestada y CUARENTENA de cinco días en Réduit. Es el país de la guía donde el perro entra peor y sale mejor.",
    facts=[
        ("Estatus", "FUERA DE RUTA. Insular, a unos 900 km al este de Madagascar. No hay travesía regular de vehículos desde el continente africano."),
        ("Cómo llegar", "Solo en avión: Aeropuerto Internacional Sir Seewoosagur Ramgoolam (MRU), en Plaine Magnien, a 48 km al sureste de Port Louis. Port Louis es el ÚNICO puerto de entrada oficial del país."),
        ("Visado", "SIN VISADO para españoles: 90 días por visita y hasta 180 días de turismo por año natural. Pasaporte con más de 6 meses de vigencia y «All in One travel form» en safemauritius.govmu.org antes de volar."),
        ("Vehículo/aduana", "Sin procedimiento publicado de admisión temporal para vehículo de turista. Régimen general de la MRA: reexportación en 6 meses, validez máxima 12 meses, depósito de garantía. SE CONDUCE POR LA IZQUIERDA."),
        ("Seguro", "Mauricio NO está en el sistema de Carta Verde y no le aplican Carte Brune CEDEAO, Carte Rose CEMAC ni Yellow Card COMESA para un vehículo español. Seguro local obligatorio; en la práctica, el del coche de alquiler."),
        ("Moneda", "Rupia mauriciana (MUR). 1 € = 54,36 MUR según la Ficha País del MAEC de mayo de 2026. Tarjeta aceptada con normalidad; cajeros en toda la isla."),
        ("Perro", "ENTRADA DURA: permiso previo con 3 meses de antelación, titulación antirrábica ≥0,5 UI/ml con 3 meses de espera, Ehrlichia y Brucella negativos, viaje como carga y CUARENTENA MÍNIMA DE 5 DÍAS en Réduit. VUELTA A LA UE FÁCIL: Mauricio está en el Anexo II del Reglamento de Ejecución (UE) 2026/636 y NO exige la titulación previa hecha en la UE."),
        ("Drones", "Autorización previa del Department of Civil Aviation para CADA vuelo. Máximo 120 m de altura, 50 m de personas y estructuras, siempre a la vista. A los visitantes se los evalúa caso por caso, con licencia y registro."),
        ("Starlink", "NO DISPONIBLE. La ICTA no ha licenciado el servicio y en 2023 alegó seguridad nacional; a finales de 2024 los residentes seguían viéndolo «en espera» y en mayo de 2026 Mauricio no figuraba ni como disponible ni como próximo. Fibra y 4G/5G excelentes."),
        ("Seguridad", "«SE RECOMIENDA VIAJAR CON PRECAUCIÓN» (MAEC), sin ninguna zona desaconsejada. Freedom House le da 86/100 en 2025 y la condición de país libre. Sin terrorismo ni conflicto."),
        ("Clima", "Tropical. Temporada de ciclones de mediados de noviembre a mediados de abril según el MAEC, de noviembre a mayo según el FCDO. En alerta de clase 3 el país se para y el aeropuerto cierra."),
        ("Sanidad", "SIN MALARIA y SIN RABIA declarada. Chikungunya en brote: 6.675 casos confirmados en 2026 frente a 1.395 en 2025. Sanidad privada de buen nivel; seguro médico internacional imprescindible."),
    ],
    alerts=[
        "NO HAY FORMA DE LLEVAR LOS COCHES. No existe travesía regular de vehículos entre el continente africano y Mauricio: solo flete en contenedor o ro-ro, con coste muy superior al del propio viaje.",
        "SE CONDUCE POR LA IZQUIERDA. Dos 4x4 españoles con el volante a la izquierda serían un problema permanente en adelantamientos y rotondas, en una isla pequeña y con tráfico denso.",
        "EL PERRO ENTRA CON CUARENTENA. Mínimo CINCO DÍAS en la estación oficial de Réduit, más permiso de importación solicitado con TRES MESES de antelación. Inviable para una visita corta.",
        "EL PERRO VIAJA COMO CARGA. Las directrices oficiales exigen que llegue «as manifest CARGO ONLY»: ni en cabina ni en la bodega de equipaje. Nada de ir con él en el mismo vuelo de forma normal.",
        "RAZAS PROHIBIDAS. Pit Bull en todas sus variantes, American Staffordshire, Staffordshire Terrier, Tosa japonés, Dogo argentino, Fila brasileiro y Boerboel no pueden entrar en el país.",
        "CICLONES. De mediados de noviembre a mediados de abril. Con Garance, en febrero de 2025, se declaró alerta de clase 3 y se cerró el aeropuerto MRU. El teléfono de información ciclónica es el 95.",
        "CHIKUNGUNYA EN BROTE. 6.675 casos confirmados en 2026 frente a 1.395 en 2025 (TravelHealthPro). El mosquito pica de día: repelente desde el amanecer.",
        "STARLINK NO FUNCIONA. La ICTA no lo ha autorizado. Llevar el kit es cargar con un trasto inútil; una eSIM local resuelve el viaje.",
        "DROGAS. El tráfico se castiga con hasta 30 años de prisión y los controles aeroportuarios son muy estrictos (MAEC).",
        "TABACO Y VAPEO. Está PROHIBIDA la importación de papel de fumar y de cigarrillos electrónicos (MAEC). Es una confiscación segura en aduana.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Llegada y trámites", "Aeropuerto SSR (Plaine Magnien) → M1 → Port Louis; despacho de los vehículos (embarcados o alquilados) y recogida del perro en la cuarentena de Réduit", "~50 km · 1–2 días"),
        ("2 · Port Louis", "Caudan Waterfront, Aapravasi Ghat (UNESCO), mercado central, Champ de Mars y la Citadelle", "~15 km · 1 día"),
        ("3 · Pamplemousses y el norte", "Port Louis → Jardín Botánico SSR (Pamplemousses) → Grand Baie → Cap Malheureux", "~45 km · 1 día"),
        ("4 · Islotes del norte", "Grand Baie → catamarán a Îlot Gabriel e Île Plate → Grand Baie", "~10 km + travesía · 1 día"),
        ("5 · Bajada a la costa este", "Cap Malheureux → Poste Lafayette → Belle Mare → Trou d'Eau Douce", "~60 km · 1 día"),
        ("6 · Île aux Cerfs", "Trou d'Eau Douce → lancha a la Île aux Cerfs y cascada del Grand River South East → regreso", "~10 km + travesía · 1 día"),
        ("7 · Sureste histórico", "Trou d'Eau Douce → Grande Rivière Sud-Est → Mahébourg y museo naval → Blue Bay", "~45 km · 1 día"),
        ("8 · Île aux Aigrettes", "Mahébourg → embarcadero de Pointe Jérôme → reserva de la Île aux Aigrettes (visita guiada MWF) → Mahébourg", "~10 km + travesía · medio día"),
        ("9 · Sur y tortugas", "Mahébourg → Souillac (Gris-Gris) → Rivière des Anguilles (La Vanille) → Bel Ombre", "~60 km · 1 día"),
        ("10 · Le Morne Brabant", "Bel Ombre → Baie du Cap → Le Morne (UNESCO); subida al amanecer, 3,5–4,5 h", "~35 km · 1–2 días"),
        ("11 · Chamarel y las gargantas", "Le Morne → Chamarel (Tierras de Siete Colores y cascada) → Plaine Champagne → Black River Gorges (Pétrin)", "~45 km · 1–2 días"),
        ("12 · Meseta central", "Pétrin → Grand Bassin (Ganga Talao) → Curepipe (Trou aux Cerfs) → Moka (Eureka)", "~50 km · 1 día"),
        ("13 · Cierre en Port Louis", "Moka → M1 → Port Louis; embarque o devolución de los vehículos y papeleo de salida del perro", "~20 km · 1 día"),
        ("14 · Extensión a Rodrigues (opcional)", "Vuelo desde Plaisance o carguero de línea desde Port Louis; Port Mathurin, Mont Limon, Île aux Cocos. SIN vehículos propios", "~560 km de travesía · 3–4 días"),
    ],
    offroad=[
        "AVISO DE PARTIDA: Mauricio es insular y está a unos 2.000 km de la costa sureste de África, al este de Madagascar, sin ferri de vehículos desde el continente; los dos 4x4 del proyecto no pueden llegar rodando y cualquier conducción aquí implica embarque marítimo desde Europa o alquiler local (tramitación y coste, POR CONFIRMAR).",
        "La isla tiene 2.772 km de carreteras, un 98 % asfaltadas, con 104 km de autopista —la M1 de Port Louis al aeropuerto (47 km), la M2 de Port Louis a Grand Baie (23 km) y la M3 de circunvalación—, de modo que el bucle completo de los PDIs se hace por asfalto: aquí el 4x4 es comodidad, no necesidad.",
        "NO HAY PISTAS PÚBLICAS 4x4 DE LARGO RECORRIDO: el suelo rural no urbanizado es caña de azúcar en manos privadas y los caminos de finca pertenecen a los ingenios; meterse por ellos sin permiso es allanamiento y no aparece en ninguna guía como ruta abierta.",
        "El parque nacional de Black River Gorges se recorre a pie y no en coche: sus 60 km de senderos están cerrados a vehículos privados y el acceso rodado se limita a la B103 asfaltada de Plaine Champagne y a los aparcamientos de los centros de Pétrin y de Black River; el parque cierra a una hora que cambia con la estación.",
        "Los circuitos 4x4 reales del país son concesiones privadas y guiadas. La Bel Ombre Nature Reserve (antigua Frédérica), en el sur, abre de 8:30 a 16:30 y ofrece safari 4x4 de dos horas, quad y buggy, pero PROHÍBE EXPRESAMENTE conducir vehículo propio: «you are not authorized to do so. Our tours are performed on our private lands, and we are not insured for persons seeking to drive their own quad». La Étoile Reserve, en el este, funciona igual con quads.",
        "Se conduce por la izquierda y el FCDO avisa de accidentes frecuentes por carreteras estrechas, mala visibilidad de motos sin luces y peatones en la calzada; con dos vehículos anchos y volante a la izquierda, extremar la precaución en las carreteras B de montaña (Chamarel, Plaine Champagne, La Vanille), estrechas y con curvas cerradas.",
        "Conducir por la playa está descartado: la franja entre la línea de pleamar y el mar es dominio público del Estado por el Pas Géométriques Act y la Beach Authority gestiona 126 playas públicas de uso peatonal.",
        "ZONAS VETADAS A CUALQUIER VEHÍCULO: los islotes del norte (Île Plate, Îlot Gabriel y Pigeon Rock son áreas nacionales protegidas), la Île aux Aigrettes (reserva de visita guiada en barco) y la Île Ronde, reserva natural con reptiles endémicos. A Rodrigues no llegan los vehículos propios: el enlace es aéreo o en carguero, con dos barcos fondeando cinco veces al mes en Port Mathurin.",
    ],
    senderismo=[
        "Le Morne Brabant (556 m), suroeste: de 5 a 8 km y de 3,5 a 4,5 horas ida y vuelta —otras fuentes hablan de 7 km y de 3 a 5 horas—, con una primera mitad ancha y cómoda y un tramo superior de roca donde hay que usar las manos, con exposición; las guías locales recomiendan ir con guía a la cima y no subir con la roca mojada. Salida antes de las 7:00 y 1,5-2 litros de agua por persona.",
        "Sendero de Macchabée, Black River Gorges: unos 10 km y cuatro horas contando las paradas en los miradores, desde el centro de información de Pétrin; es la caminata clásica por el último bosque nativo de la isla, dentro de los 60 km de senderos del parque.",
        "Piton de la Petite Rivière Noire (828 m), el techo de Mauricio: se sube desde el centro de visitantes de Black River, en el lado oeste del parque; media jornada larga y sin sombra en la parte alta.",
        "Le Pouce (812 m), sobre Port Louis y Moka: 4,5 km ida y vuelta, de 2 a 3 horas, dificultad fácil-moderada; es la mejor panorámica de la capital y del norte y se encadena bien con la visita a Eureka.",
        "Corps de Garde (720 m), sobre Quatre Bornes: 4,5 km ida y vuelta, de 3 a 4 horas, fácil-moderada; montaña urbana con vistas a la meseta central.",
        "Siete Cascadas (Tamarind Falls), Henrietta: unos 5 km y de 4 a 6 horas, moderada, con pasos por el cauce y bañeras naturales; las guías recomiendan guía para quien no tenga experiencia, porque el itinerario no está balizado y hay tramos resbaladizos.",
        "Cascada de Mare aux Joncs, dentro de Black River Gorges: salto de unos 100 m en la variante de bosque lluvioso del parque, buena alternativa corta cuando el sendero de Macchabée está embarrado.",
        "Paseo guiado de la Île aux Aigrettes (Mauritian Wildlife Foundation): recorrido a pie por el único resto del bosque seco costero de Mauricio, con tortugas de Aldabra, paloma rosada y escinco de Telfair; obligatorio con guía y con reserva. En Rodrigues, la reserva de la Île aux Cocos y las cuevas y tortugas de François Leguat dan otras dos caminatas cortas.",
    ],
    acampada=[
        "NO EXISTE UNA RED DE CAMPINGS PÚBLICOS en Mauricio: las fuentes consultadas solo identifican tres opciones comerciales, The Outpost en Grand Port (montañas de Bambous Virieux, acceso empinado que exige 4x4), Otentic Eco Tent en Deux Frères y Explorers, que monta campamentos en Black River Gorges, Chamarel y Le Morne.",
        "Otentic Eco Tent (otentic.mu) es la opción más sólida y verificable: tiendas fijas entre la Grande Rivière Sud-Est y el océano, cerca de Trou d'Eau Douce y de Blue Bay, con cocina mauriciana, kayak y paddle. Tarifas y política de mascotas, POR CONFIRMAR directamente con el establecimiento.",
        "La acampada libre no está amparada por ningún derecho general: las fuentes consultadas la describen como no posible fuera de las opciones designadas, con control estricto del litoral y de las áreas protegidas y con necesidad de permiso expreso en terreno privado.",
        "Las playas son dominio público del Estado por el Pas Géométriques Act y la Beach Authority gestiona 126 playas públicas; el camping en ellas se ha tratado en la prensa local como actividad sujeta a autorización y pago. Antes de montar nada en una playa, pedir permiso a la Beach Authority: los tramos con concesión hotelera quedan fuera en cualquier caso.",
        "NO SE HAN LOCALIZADO FICHAS ÚTILES DE iOVERLANDER NI DE TRACKS4AFRICA para Mauricio: las búsquedas devuelven la app genérica y agregadores comerciales, sin ningún punto de pernocta verificable en la isla. Tratar la ausencia de datos como lo que es, ausencia, y no como permiso.",
        "Dentro del parque nacional de Black River Gorges no hay zona de acampada anunciada por el gestor y el recinto cierra a una hora que cambia con la estación: la pernocta por libre ahí hay que descartarla.",
        "Los islotes del norte (Île Plate, Îlot Gabriel, Pigeon Rock) y la Île aux Aigrettes son áreas protegidas de visita diurna y guiada: no se pernocta en ninguno.",
        "PLAN REALISTA PARA EL PROYECTO: dormir en pensiones y bungalós, abundantes y baratos fuera de temporada alta, y tratar la acampada como excepción concertada con un establecimiento; con el perro, además, conviene alojamiento cerrado, porque la isla tiene mucho perro suelto.",
    ],
    visado=[
        "Los españoles NO necesitan visado: 90 días por visita y hasta 180 días de turismo por año natural, según la política de visados de Mauricio.",
        "Pasaporte con vigencia superior a seis meses sobre la fecha de entrada (MAEC, 2026).",
        "Hay que cumplimentar el «Mauritius All in One travel form» en safemauritius.govmu.org ANTES de volar; el QR se enseña en inmigración. Es el único sitio legítimo (Airport Terminal Operations Ltd).",
        "En inmigración pueden pedir billete de vuelta, reserva de alojamiento confirmada y fondos por un mínimo de 100 dólares al día. Algunas aerolíneas exigen ya el alojamiento para dejar embarcar (MAEC).",
        "Coste: cero. No hay tasa de entrada, eVisa ni eTA para españoles.",
        "No aplica la casilla de «validez en frontera terrestre»: Mauricio no tiene fronteras terrestres. Todo el control se hace en MRU o en el puerto de Port Louis.",
    ],
    fronteras_rows=[
        ("Aeropuerto principal", "Sir Seewoosagur Ramgoolam International (MRU), Plaine Magnien", "ABIERTO. Única puerta de entrada realista. Exención de visado de 90 días para españoles y «All in One travel form» previo obligatorio. También es el punto de llegada del perro, que debe venir como carga manifestada. Fuente: MAEC 2026 y mru.airport.aero."),
        ("Puerto de entrada", "Port Louis Harbour", "ABIERTO. «Port Louis is the only official Port of Entry on Mauritius» (Noonsite). Los documentos de barco y tripulación deben llegar a la autoridad portuaria con 24 horas de antelación; no hay tasas de entrada ni salida. Sería el punto de despacho de los vehículos si se enviaran por mar."),
        ("Puerto secundario", "Port Mathurin, Rodrigues", "Se puede despachar primero en Port Mathurin, pero hay que completar el despacho después en Port Louis (Noonsite). No sirve como entrada definitiva al país."),
        ("Enlace interior (aire)", "Sir Gaëtan Duval Airport (RRG), Rodrigues", "ABIERTO. Vuelos diarios de Air Mauritius desde MRU, unos 90 minutos. Rodrigues está a 560 km al este y es dependencia autónoma con Asamblea Regional propia desde 2002."),
        ("Enlace interior (mar)", "MS Mauritius Trochetia, Port Louis – Port Mathurin", "OPERATIVO. De tres a cuatro travesías al mes, unas 36 horas, 112 plazas de pasaje y carga rodada (transporta «vehicles & containers»). Reservas de pasaje en +230 217 2285 / 217 2284 / 217 2291. POR CONFIRMAR si admite vehículos de turista y animales."),
        ("Paso terrestre", "No existe", "Mauricio es insular: no hay ningún paso fronterizo terrestre. La ficha de pasos terrestres de la guía no aplica a este país."),
        ("Aduana de vehículos", "Mauritius Revenue Authority – Customs, Port Louis", "Admisión temporal general de mercancías con reexportación en 6 meses y validez máxima de 12, con depósito de garantía en efectivo o aval. NO publica procedimiento específico para vehículo de turista ni menciona el carnet de passages. Fuente: mra.mu, Private Importers."),
    ],
    vehiculos=[
        "SE CONDUCE POR LA IZQUIERDA, herencia británica. Es el argumento que más pesa: dos vehículos españoles con el volante a la izquierda serían inseguros aquí.",
        "No hay travesía regular de vehículos desde el continente africano. La única vía sería flete en contenedor de 40 pies o ro-ro desde Durban, Mombasa o Europa, y despacho en Port Louis, único puerto de entrada del país.",
        "La Mauritius Revenue Authority contempla la admisión temporal de mercancías con reexportación en seis meses, hasta doce meses de validez y depósito de garantía; no publica un procedimiento específico para vehículo de turista.",
        "AIT/FIA no tiene organización emisora de carnet de passages en Mauricio (carnetdepassage.org). Eso se refiere a EMITIRLO, no a si Mauricio lo ACEPTA: sigue siendo un dato por confirmar con la MRA.",
        "El carné europeo sirve para conducir, pero las empresas de alquiler exigen en la práctica el permiso internacional, además de edad y antigüedad mínimas (FCDO, 4 de septiembre de 2026).",
        "Obligación local curiosa: hay que llevar TIZA AMARILLA en el coche para marcar la posición de las ruedas en caso de accidente o avería (FCDO).",
        "La tasa de alcoholemia es aproximadamente la cuarta parte de la inglesa y las sanciones son severas. Los accidentes son frecuentes y muchas motos circulan de noche sin luces (FCDO).",
        "La red asfaltada cubre toda la isla, con autopista M1/M2 entre el aeropuerto, Port Louis y el norte. Un 4x4 no aporta ninguna ventaja: un utilitario de alquiler resuelve el viaje entero.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autoridad competente: Department of Civil Aviation (DCA) de Mauricio, civil-aviation.govmu.org.",
        "Permiso obligatorio del DCA antes de CADA vuelo. A los turistas se los evalúa caso por caso, con licencia de piloto y registro del dron; el seguro se recomienda pero no es obligatorio para ellos.",
        "Límites operativos: 120 metros de altura máxima, 50 metros de separación de personas, estructuras y vehículos, y vuelo siempre dentro del alcance visual. Prohibido sobrevolar zonas densamente pobladas y concentraciones de más de 500 personas.",
        "Uso comercial: tasa de Rs 10.000, seguro obligatorio, edad mínima 18 años y validez de 36 meses.",
        "POR CONFIRMAR el régimen sancionador y si la aduana de MRU confisca a la llegada: no hemos encontrado ningún testimonio de confiscación ni de multa, solo viajeros que no consiguen respuesta del DCA (foro de Tripadvisor, diciembre de 2025).",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "NO DISPONIBLE. La ICTA (icta.mu) es el regulador y no ha concedido licencia; en 2023 se justificó por seguridad nacional y falta de control sobre el tráfico (newsmoris.com, 21 de agosto de 2023).",
        "A finales de 2024 los residentes confirmaban en foros de expatriados que el servicio seguía en estado «awaiting» y que la ICTA no se había pronunciado con el nuevo gobierno (expat.com).",
        "En el recuento de cobertura mundial de mayo de 2026, Mauricio no figuraba ni entre los 27 países africanos activos ni entre los anunciados para 2026 (Mappr). Seychelles y Reunión sí tienen servicio.",
        "Alternativa real: Mauritius Telecom (marca my.t), Emtel y Chili, con 4G en toda la isla y 5G en Port Louis y la costa norte. SIM o eSIM turística en el aeropuerto o en cualquier tienda, presentando el pasaporte.",
        "POR CONFIRMAR la cobertura móvil en Rodrigues fuera de Port Mathurin: no hemos encontrado fuente fiable.",
    ],
    perro_intro=[
        "ENTRADA · PERMISO PREVIO. Mauricio exige un Import Permit solicitado con AL MENOS TRES MESES de antelación a la Livestock and Veterinary Division del Ministry of Agro-Industry and Food Security, por petimport@govmu.org. Tasa de Rs 500 por animal más Rs 500 de inspección veterinaria. Fuente: guía oficial «Guidelines to bring dogs to Mauritius», publicada en el portal sanitario del Gobierno de Mauricio (sps.govmu.org).",
        "ENTRADA · REQUISITOS SANITARIOS. Microchip leído en el momento de la extracción de sangre; vacuna antirrábica aplicada no menos de dos semanas antes del envío; TITULACIÓN DE ANTICUERPOS ANTIRRÁBICOS por FAVN o RFFIT con resultado igual o superior a 0,5 UI/ml, con la muestra tomada al menos cuatro semanas después de la vacuna y al menos TRES MESES antes del viaje; vacunas de moquillo, hepatitis infecciosa, leptospirosis y parvovirus; serología NEGATIVA de Ehrlichia canis (IFAT, dilución 1:40) y de Brucella canis en los 45 días previos; y certificado veterinario internacional firmado por la autoridad competente del país exportador.",
        "ENTRADA · CUARENTENA Y TRANSPORTE. Cuarentena obligatoria de un MÍNIMO DE CINCO DÍAS en la Quarantine Facility de Réduit, a Rs 15 por día y animal según la guía oficial. No es domiciliaria. Visitas de lunes a sábado de 9:00 a 11:00 y de 13:00 a 14:30, y domingos y festivos de 9:00 a 12:00. El animal debe llegar «as manifest CARGO ONLY»: ni en cabina ni en la bodega de equipaje.",
        "ENTRADA · RAZAS PROHIBIDAS. El Fourth Schedule veta American Pit Bull Terrier, American Staffordshire Terrier, Staffordshire Terrier, Blue Nose Pit Bull, Red Nose Pit Bull, Tosa japonés, Dogo argentino, Fila brasileiro y Boerboel. Otras razas consideradas peligrosas (Rottweiler, Dobermann, Cane Corso, Bullmastiff, Mastino napolitano, Presa canario, Rhodesian Ridgeback, Kangal, Alaskan Malamute) solo se admiten si son de pura raza acreditada.",
        "VUELTA A LA UE · AQUÍ MAURICIO ES LA EXCEPCIÓN DE TODA LA GUÍA. Mauricio (código MU) figura en el ANEXO II del Reglamento de Ejecución (UE) 2026/636, aplicable desde el 22 de abril de 2026, junto con Santa Elena (SH) y Ascensión (AC): son los ÚNICOS territorios africanos de la lista y Mauricio es el único Estado africano. Por eso, a diferencia de los otros cuarenta y tantos países de esta guía, el perro NO necesita la titulación antirrábica hecha en la UE antes de salir, la llamada vía A. El considerando 3 del Reglamento y el artículo 17, apartado 1, letra b), del Reglamento Delegado (UE) 2026/131 lo dicen expresamente: los animales que se desplacen desde un tercer país listado «no están obligados a someterse a una prueba de valoración de anticuerpos de la rabia».",
        "VUELTA A LA UE · QUÉ HAY QUE LLEVAR. Microchip legible, vacuna antirrábica en vigor y, o bien el pasaporte europeo con el que el perro salió de España —sigue siendo válido mientras la vacuna esté vigente, según el MAPA—, o bien el certificado sanitario del modelo del Reglamento de Ejecución (UE) 2026/705 expedido por un veterinario oficial mauriciano. Además, declaración escrita de desplazamiento sin ánimo comercial y entrada por un Punto de Entrada de Viajeros (PEV) autorizado, declarando el animal al Resguardo Fiscal de la Guardia Civil o a la aduana para el control documental y la lectura del chip.",
        "LA PARADOJA QUE HAY QUE ENTENDER. La titulación antirrábica NO la pide la Unión Europea: la pide MAURICIO para dejar entrar al perro, y además con tres meses de espera desde la toma de muestra. Es decir, el análisis hay que hacerlo igual, pero por exigencia mauriciana y con calendario mauriciano, no por el trámite europeo de regreso. Mauricio no tiene rabia declarada (TravelHealthPro, 2026), y de ahí viene tanto su inclusión en el Anexo II como su celo en la frontera.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "NO HAY MALARIA en Mauricio: «There is no risk of malaria in Mauritius» (TravelHealthPro/NaTHNaC, 2026). El MAEC menciona casos esporádicos, pero no hay transmisión local establecida.",
        "FIEBRE AMARILLA: no se exige a quien llega de España, pero SÍ se exige certificado a partir de UN año de edad a quien llegue de un país que Mauricio considere de riesgo de transmisión, y su lista difiere de la de la OMS. Crítico si se encadena con otro país africano.",
        "CHIKUNGUNYA EN BROTE: 6.675 casos confirmados en 2026 frente a 1.395 casos autóctonos en 2025. También hay dengue. El mosquito pica de día: repelente y manga larga desde el amanecer.",
        "RABIA: «Rabies has not been reported in this country». El único riesgo residual es el lisavirus de murciélago; no tocar murciélagos. Esto explica que Mauricio esté en la lista europea del Anexo II.",
        "AGUA: la Central Water Authority trata y analiza el agua en unos 160 puntos de muestreo con laboratorio acreditado ISO/IEC 17025, pero la práctica generalizada entre residentes y viajeros es no beberla del grifo por el estado de la red de distribución. Botella o filtro.",
        "Evitar el contacto con agua dulce estancada por riesgo de esquistosomiasis (TravelHealthPro).",
        "SANIDAD: pública gratuita pero saturada; privada de buen nivel, con el grupo C-Care (Wellkin en Moka, Darné en Floréal, Grand Baie y Tamarin). SEGURO MÉDICO INTERNACIONAL IMPRESCINDIBLE, con repatriación. Algunos medicamentos habituales en España están prohibidos: el MAEC cita Coproxamal y Di-antalvic.",
    ],
    seguridad_intro="Mauricio es el país más seguro y mejor gobernado de esta guía. El MAEC lo clasifica como «SE RECOMIENDA VIAJAR CON PRECAUCIÓN», sin ninguna zona desaconsejada, sin terrorismo y sin conflicto. Freedom House le da 86 sobre 100 en 2025, con la condición de país libre, y el Índice Mo Ibrahim de 2024 lo sitúa segundo de África con 72,8 sobre 100, muy por encima de la media continental de 49,3. Los problemas reales aquí son el hurto en zonas turísticas, el tráfico y los ciclones, no la violencia.",
    seguridad=[
        "El MAEC recomienda «viajar con precaución» y no desaconseja ninguna zona del territorio.",
        "Delincuencia común baja, pero con aumento de robos y asaltos. Zonas de riesgo medio: Port Louis, Grand Baie, Flic en Flac y los mercados locales (MAEC y FCDO, 2026).",
        "El FCDO documenta agresiones sexuales contra turistas y desaconseja caminar solo o sola de noche por zonas mal iluminadas. El MAEC añade no pasear de noche por zonas solitarias ni ostentar objetos de valor.",
        "Tráfico: accidentes frecuentes, motos sin luces de noche, conducción por la izquierda y tasa de alcoholemia en torno a la cuarta parte de la inglesa, con sanciones severas.",
        "Accidentes con lanchas deportivas y motos de agua en las playas: el MAEC los señala expresamente. Comprobar que el operador tenga permiso del Ministerio de Turismo (FCDO).",
        "Ciclones: alerta de clase 1 a 4 entre mediados de noviembre y mediados de abril. Con Garance, el 26 de febrero de 2025, se declaró clase 3 y se cerró el aeropuerto MRU. Información ciclónica en el 95.",
        "Drogas: hasta 30 años de prisión por tráfico y controles aeroportuarios muy estrictos (MAEC).",
        "Estabilidad política: las elecciones del 10 de noviembre de 2024 dieron un vuelco total, con la Alliance du Changement de Navin Ramgoolam llevándose los 60 escaños en disputa, tras un escándalo de escuchas telefónicas filtradas y un intento fallido de bloquear las redes sociales. El relevo fue pacífico (Freedom House 2025 y Ficha País del MAEC de mayo de 2026).",
        "Ruido de fondo institucional en 2025: detención del ex primer ministro Pravind Jugnauth por blanqueo en febrero y dimisión del gobernador del Banco de Mauricio en septiembre. No afecta a la seguridad del viajero, pero explica titulares alarmantes.",
    ],
    agua=[
        "La Central Water Authority (cwa.govmu.org) trata el agua y la analiza en unos 160 puntos de muestreo con laboratorio acreditado ISO/IEC 17025 conforme a las Drinking Water Standards nacionales. Teléfono 601 5000 y línea directa 170.",
        "Aun así, la recomendación práctica para el viajero es NO beber del grifo: el problema no es el tratamiento sino el estado de la red de distribución, que puede aportar sedimento o bacterias (tapwaterworldwide.com, actualizado el 7 de agosto de 2026).",
        "Para llenar depósitos de ducha y lavado, cualquier toma de red municipal sirve sin problema. La ducha con agua del grifo se considera segura.",
        "POR CONFIRMAR la existencia de puntos públicos de llenado para autocaravanas: no hay cultura de camper en Mauricio y no hemos localizado ninguna red de áreas de servicio.",
        "Los cortes y las restricciones de suministro son un problema crónico y recurrente en la isla; muchos alojamientos tienen cisterna y bomba propias. Conviene preguntar si el agua del grifo es de red o de cisterna.",
        "Evitar el contacto con agua dulce estancada, ríos y charcas, por riesgo de esquistosomiasis (TravelHealthPro).",
    ],
    combustible=[
        "PRECIOS OFICIALES vigentes desde el 15 de agosto de 2026, fijados por la State Trading Corporation: GASOLINA (Mogas) Rs 70,65 por litro y DIÉSEL (Gas Oil) Rs 71,25 por litro.",
        "Al cambio de la Ficha País del MAEC de mayo de 2026 (1 € = 54,36 MUR), eso son aproximadamente 1,30 €/litro de gasolina y 1,31 €/litro de diésel: caro para África, parecido a España.",
        "El precio lo fija el Petroleum Pricing Committee y está topado. En agosto de 2026 la subida calculada de la gasolina era del 14,75 % y se limitó al 10 % permitido, con un déficit de Rs 3.500 millones en la cuenta de estabilización de precios: cabe esperar nuevas subidas.",
        "GlobalPetrolPrices daba MUR 58,95 por litro de diésel el 9 de febrero de 2026. La diferencia con el dato de agosto muestra lo rápido que se mueve el precio regulado: usar siempre el último comunicado de la STC (stcmu.com).",
        "Red de estaciones densa y moderna en toda la isla, con pago con tarjeta y calidad de combustible europea. No hay racionamiento ni desabastecimiento.",
        "POR CONFIRMAR la red de estaciones en Rodrigues, mucho más escasa; el propio Mauritius Trochetia transporta combustible y gas a la isla en ocasiones especiales, lo que da idea de la dependencia logística.",
    ],
    experiencias_intro="No existe ni un solo relato de overlander que haya llevado su propio vehículo a Mauricio, sencillamente porque no hay forma de hacerlo. Lo que sigue son testimonios de viajeros aéreos, expatriados que trasladaron a sus animales, navegantes y residentes, recogidos por lo que aportan al caso real de esta expedición.",
    experiencias=[
        "Conducir por la izquierda sin drama, pero con ojo: Our Soulful Travels publicó en 2024 una guía detallada de conducción en Mauricio. Confirma que se circula a la izquierda al estilo británico, que las autopistas están bien mantenidas pero las carreteras rurales son estrechas, y que hay baches, animales sueltos y atascos en las zonas turísticas. Pide carné en inglés o francés, o permiso internacional, y edad mínima de 21 años para alquilar.",
        "Llevar un perro desde Europa cuesta lo que un viaje: en el foro de Expat.com sobre Mauricio, viajeros que trasladaron a su perro desde el Reino Unido citan agencias como Animal Couriers y PetAir UK y presupuestos de entre 50.000 y 100.000 rupias mauricianas. Detallan que el permiso de importación vale 45 días, que el animal solo viaja como carga y que la cuarentena estatal de Réduit fue de cinco días.",
        "La cuarentena de Réduit no es un hotel: en ese mismo hilo de Expat.com, un usuario advierte de las deficiencias de las instalaciones estatales y recomienda visitar al animal a diario y pagar extras para que lo cuiden mejor. Cita una tarifa de unas 75 rupias diarias, cinco veces la que publica la guía oficial del Gobierno. Es la discrepancia que hay que aclarar por escrito antes de embarcar al perro.",
        "Starlink sigue sin llegar: el hilo «SpaceX Starlink» del foro de Expat.com recoge que a finales de 2024 el servicio seguía sin estar disponible y que la web mostraba Mauricio «en espera». Una moderadora responde que la ICTA no ha confirmado si llegará y sugiere esperar al pronunciamiento del nuevo gobierno. Sigue igual en 2026: es el único país de esta guía con buena conectividad y sin Starlink.",
        "Los drones son un limbo administrativo: en el hilo «New Drone Laws» del foro de Tripadvisor sobre Mauricio, abierto tras las normas de enero de 2025, varios viajeros dicen que la web del Gobierno no explica nada para turistas y uno cuenta que no consigue respuesta por correo para registrar su aparato. La última pregunta, de diciembre de 2025, se quedó sin contestar. Nadie relata confiscaciones ni multas.",
        "Para los navegantes, Port Louis y solo Port Louis: Noonsite, la referencia mundial de formalidades náuticas, es tajante: «Port Louis is the only official Port of Entry on Mauritius». Se puede despachar primero en Port Mathurin, en Rodrigues, pero hay que completarlo después en la capital. Los documentos deben llegar a la autoridad portuaria 24 horas antes y no hay tasas de entrada ni de salida.",
        "Rodrigues es otro país: el reportaje de HIDMC sobre Rodrigues la describe como el tesoro escondido de Mauricio, a 560 km al este, mucho más tranquila y menos turística. Se llega en 90 minutos de vuelo con Air Mauritius desde MRU o en unas 36 horas a bordo del MV Trochetia. El transporte público es limitado y recomiendan coche o scooter de alquiler.",
        "Un ciclón para la isla entera: newsmoris.com informó el 26 de febrero de 2025 de la alerta de clase 3 por la tormenta tropical severa Garance, entonces a 440 km al noroeste. La Wikipedia recoge que el aeropuerto internacional Sir Seewoosagur Ramgoolam se cerró por precaución. Planificar un viaje entre noviembre y abril es aceptar que puedes perder dos o tres días encerrado.",
        "El agua del grifo, mejor no: tapwaterworldwide.com, en su ficha de Mauricio actualizada el 7 de agosto de 2026, concluye que el agua pública no alcanza los estándares internacionales de potabilidad por el estado de la red, aunque ducharse sea seguro. Recomienda botella o filtro portátil. La Central Water Authority, por su parte, sostiene que el agua cumple las normas nacionales.",
        "Mauricio, segunda de África en gobernanza: el portal de datos del Ibrahim Index of African Governance da a Mauricio 72,8 sobre 100 en la edición de 2024, segunda de 54 países africanos, frente a una media continental de 49,3 y regional de 46,8. Conviene precisarlo: durante años fue la primera, y en 2024 ya no lo es, aunque sigue siendo la única democracia plena del continente.",
    ],
    pendientes=[
        ("Admisión temporal de vehículo de turista", "Respuesta escrita de la Mauritius Revenue Authority (Customs) que diga si acepta un CPD extranjero o qué régimen aplica a un vehículo español matriculado, con importe de la garantía."),
        ("Coste real del flete de un 4x4", "Presupuesto en firme de una naviera para contenedor de 40 pies Barcelona o Durban – Port Louis, ida y vuelta, con despacho incluido."),
        ("Validez del certificado veterinario de entrada", "Confirmación por escrito de petimport@govmu.org sobre el plazo en días del International Veterinary Certificate y los países de origen aceptados."),
        ("Tarifa real de la cuarentena de Réduit", "Aclaración oficial de la contradicción entre las Rs 15 por día de la guía del Gobierno y las Rs 75 por día que citan los expatriados en Expat.com."),
        ("Perros en playas públicas", "Norma o comunicado de la Beach Authority o de una municipalidad que regule expresamente la presencia de perros en playas públicas."),
        ("Traslado del perro a Rodrigues", "Respuesta de Air Mauritius y de la Mauritius Shipping Corporation (+230 217 2285) sobre transporte de animales entre Mauricio y Rodrigues."),
        ("Vehículos y animales en el ferry a Rodrigues", "Tarifa oficial vigente del MS Mauritius Trochetia con frecuencia, precio de pasaje, admisión de vehículos de turista y de animales."),
        ("Régimen sancionador de drones", "Texto vigente de las Mauritius Civil Aviation Regulations o comunicado del DCA con las multas y los supuestos de confiscación, y un procedimiento de registro para visitantes que funcione."),
        ("Starlink", "Consulta del mapa oficial de starlink.com y, en su caso, decisión publicada de la ICTA sobre la licencia. Cerrar si sigue sin figurar a la fecha del viaje."),
        ("Dirección del Consulado Honorario", "Resolver la contradicción entre la demarcación consular (IBL House, Le Caudan Waterfront, cónsul Patrice Robert) y la Ficha País de mayo de 2026 (DML Building, Almadina Road, cónsul Peter Goldsmith)."),
        ("Coordenadas de los puntos logísticos", "Verificación en Google Maps de la estación de cuarentena de Réduit, el consulado honorario, C-Care Darné y los puntos de combustible y agua, marcados aquí como aproximados."),
        ("Seguro del vehículo", "Confirmación de OFESAUTO o del Consejo de Oficinas de que Mauricio queda fuera del sistema de Carta Verde y de qué póliza local sería exigible."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las páginas efectivamente abiertas y citadas en esta lista; cuando un dato no se ha podido confirmar, se dice y se traslada a «pendientes». Es una herramienta de planificación, no una autorización: los requisitos de entrada de personas, vehículos y animales cambian sin aviso y solo valen los que confirme por escrito la autoridad competente. Antes de cualquier gestión con el perro, escribir a petimport@govmu.org y contrastar el regreso con el MAPA español.",
    emergency="EMERGENCIA CONSULAR, Consulado Honorario de España en Port Louis, fuera de horario: +230 5729 3313; en horario, +230 208 7289 o +230 208 2879, ch.portlouis@maec.es. La oficina competente es el Consulado General de España en Ciudad del Cabo. AMBULANCIA y urgencias médicas: 114. POLICÍA: 999 o +230 208 1212. BOMBEROS: 115. INFORMACIÓN CICLÓNICA: 95. Urgencias privadas: C-Care Wellkin 132, C-Care Darné 118. Números verificados en las recomendaciones de viaje del MAEC y en la demarcación consular, 2026.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

# -*- coding: utf-8 -*-
"""Etiopía — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Etiopía está FUERA DE LA RUTA PREVISTA: la vuelta de 2027 termina en Kenia y no sube al Cuerno de África. La ficha es INFORMATIVA, para un viaje aparte. La app ya tiene una ficha corta (4 PDIs: Omo, Adís Abeba, lago Langano y Harar, sin fotos, sin enlaces y sin ficha de decisión) que hay que SUSTITUIR por la ficha completa con el formato del piloto de Túnez. Clave: el país sigue con conflictos abiertos y desiguales por región (Tigray tras el acuerdo de Pretoria de 2022, Amhara con el Fano, Oromía con el OLA) y con estados de emergencia intermitentes; cada PDI tiene que decir en qué región está y qué dice el MAEC de esa región con fecha. Etiopía es de los pocos países africanos donde el CPD y la entrada con vehículo propio tienen relatos overland recientes: concreta aduana, seguro, permiso de conducir y el estado de los pasos con Kenia (Moyale), Sudán (Metema), Yibuti (Galafi/Dewele) y Somalilandia (Togochale).

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/etiopia.json y audit/pdi/etiopia.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Adís Abeba · Museo Nacional (Lucy), Merkato y catedral de la Trinidad", cat="Ciudad · servicios", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=9.0382429, lon=38.7617736,  # Google Maps: Museo nacional de Etiopía
        desc="Capital a 2.355 m y sede de la Unión Africana, es el punto de entrada logístico del país: talleres, repuestos, embajadas y cambio. El Museo Nacional guarda a Lucy (Dinkinesh), el Australopithecus afarensis de 3,2 millones de años, y a Selam, de 3,3 millones. La catedral de la Trinidad es el templo ortodoxo de mayor rango de la ciudad y alberga las tumbas de Haile Selassie y de Sylvia Pankhurst. El Merkato, enorme mercado abierto, exige vigilancia extrema con carteristas y NO es sitio para dejar los coches cargados.",
        dog_note="El Museo Nacional y la catedral de la Trinidad son recinto cerrado y religioso; el Merkato es una aglomeración inviable con perro. Sirve como base logística, no como visita canina.",
        visit={
            "why": "Es la única ciudad del país con servicios de verdad para dos 4x4 y el mejor museo para entender por qué Etiopía es la cuna de los homínidos.",
            "see": "Lucy y Selam en el Museo Nacional, la cripta imperial de la catedral de la Trinidad, el Merkato y el mirador de Entoto sobre la ciudad.",
            "access": "Asfalto y ring road en buen estado; el tráfico y los minibuses son el verdadero peligro. Aparcamiento vigilado solo en hoteles y en el propio recinto del museo: reserva alojamiento con patio cerrado para los dos vehículos. Entrada al museo simbólica (pocos birr, importe POR CONFIRMAR en taquilla). El pin marca la entrada del Museo Nacional, en la zona universitaria.",
            "when": "Todo el año; el clima de altura es templado. Museo por la mañana, Merkato entre semana y nunca al caer la tarde.",
            "skip": "Descártalo como visita si viajas con el perro sin poder dejarlo alojado, o durante estados de emergencia con restricciones de circulación.",
        },
        links=[
            {"label": "Museo Nacional de Etiopía (Wikipedia)", "url": "https://en.wikipedia.org/wiki/National_Museum_of_Ethiopia"},
            {"label": "Catedral de la Trinidad (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Holy_Trinity_Cathedral,_Addis_Ababa"},
            {"label": "MAEC · Recomendaciones de viaje Etiopía", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Etiop%C3%ADa"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ethiopian_National_Museum_in_Addis_Ababa.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ethiopian_National_Museum_in_Addis_Ababa.jpg",
                "credit": "Ninaras · CC BY 4.0",
                "caption": "El Museo Nacional de Etiopía, donde se expone Lucy.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/National_museum_of_Ethiopia_New_facility.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:National_museum_of_Ethiopia_New_facility.JPG",
                "credit": "Richard van Alphen · Public domain",
                "caption": "El edificio nuevo del museo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Addis_Ababa_City_view.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Addis_Ababa_City_view.jpg",
                "credit": "Ninaras · CC BY-SA 4.0",
                "caption": "Adís Abeba desde las alturas.",
            },
        ],
    ),
    dict(
        n=2, name="Lalibela · las once iglesias excavadas en la roca (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=12.0331956, lon=39.0433851,  # Google Maps: Iglesias excavadas en la roca de Lalibela
        desc="Once iglesias medievales talladas hacia abajo en la toba volcánica, no construidas: el rey Lalibela quiso levantar en el siglo XII una «nueva Jerusalén» cuando las conquistas musulmanas cortaron la peregrinación a Tierra Santa. Biete Medhani Alem está considerada la MAYOR IGLESIA MONOLÍTICA DEL MUNDO y Bete Giyorgis, en cruz griega, es la imagen del país. Siguen en culto: hay que descalzarse y respetar oficios. Advertencia seria: el MAEC desaconseja los desplazamientos a Amhara y cita Lalibela por su nombre.",
        dog_note="Recinto religioso ortodoxo en uso y lugar de peregrinación; los perros no entran en los patios ni en las iglesias.",
        visit={
            "why": "Es el monumento más extraordinario de África oriental y el único sitio del país que justifica por sí solo un viaje.",
            "see": "Los cuatro grupos de iglesias (norte, este, oeste y las exteriores como Asheton Maryam y Yemrehana Krestos), túneles, trincheras y sacerdotes con cruces procesionales.",
            "access": "Asfalto desde Woldiya y desde Gashena, con tramos de montaña y baches; el pueblo está a ~2.500 m. Aparcamiento amplio junto a la taquilla y en los hoteles del alto. Entrada única válida varios días (importe POR CONFIRMAR: ha subido repetidamente). SEGURIDAD: Amhara es zona de la insurgencia Fano, con estados de emergencia intermitentes y cortes de carretera; el MAEC (26-05-2026) y el FCDO (29-05-2026) desaconsejan viajar a la región. El pin marca la taquilla del conjunto rupestre.",
            "when": "Octubre a marzo, seco. Genna (Navidad ortodoxa, 7 de enero) llena el pueblo de peregrinos: espectacular e imposible de alojar.",
            "skip": "Descártalo mientras Amhara siga desaconsejada o haya estado de emergencia: no hay forma de garantizar el acceso por carretera.",
        },
        links=[
            {"label": "UNESCO · Rock-Hewn Churches, Lalibela (nº 18)", "url": "https://whc.unesco.org/en/list/18/"},
            {"label": "Lalibela (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Lalibela"},
            {"label": "MAEC · Recomendaciones de viaje Etiopía", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Etiop%C3%ADa"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bete_Giyorgis_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bete_Giyorgis_01.jpg",
                "credit": "Bernard Gagnon · CC BY-SA 3.0",
                "caption": "Bete Giyorgis, la iglesia de San Jorge, excavada en cruz.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ethiopia_-_sunset_at_Church_of_Saint_George,_Lalibela_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ethiopia_-_sunset_at_Church_of_Saint_George,_Lalibela_01.jpg",
                "credit": "Thomas Fuhrmann · CC BY-SA 4.0",
                "caption": "Atardecer sobre Bete Giyorgis.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lalibela,_san_giorgio,_esterno_24.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lalibela,_san_giorgio,_esterno_24.jpg",
                "credit": "Sailko · CC BY 3.0",
                "caption": "El foso excavado alrededor de la iglesia.",
            },
        ],
    ),
    dict(
        n=3, name="Axum · las estelas y Santa María de Sion (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="1 noche",
        lat=14.1320767, lon=38.7193644,  # Google Maps: Obelisco de Aksum (campo de estelas norte)
        desc="Capital del reino de Aksum, «el estado más poderoso entre el Imperio Romano de Oriente y Persia» según la UNESCO. Quedan obeliscos monolíticos, tumbas reales y ruinas de palacios de los siglos I a XIII. La GRAN ESTELA, de 33 m, se partió al levantarla y sigue tumbada; la mayor en pie supera los 23 m y está tallada como un edificio de nueve plantas. En Santa María de Sion, reconstruida por Fasilides en 1665, la tradición sitúa el Arca de la Alianza. Está en Tigray: región desaconsejada.",
        dog_note="Campo de estelas y recinto eclesiástico en culto; la capilla del Arca tiene prohibido el acceso incluso a las mujeres, con más razón a los animales.",
        visit={
            "why": "Es el yacimiento fundacional de la identidad etíope y el mayor conjunto de estelas monolíticas del continente.",
            "see": "El campo de estelas norte, la tumba del rey Kaleb, la piscina de la reina de Saba, el museo y el recinto de Santa María de Sion con la capilla del Arca.",
            "access": "Asfalto desde Shire y desde Adwa; la carretera Debark–Limalimo–Shire es de montaña y estuvo muy dañada durante la guerra (ESTADO POR CONFIRMAR). Aparcamiento junto al campo de estelas y en los hoteles del centro. SEGURIDAD: Tigray tras el acuerdo de Pretoria (noviembre de 2022) sigue con tensión política interna —en marzo de 2025 una facción del TPLF tomó oficinas en Mekelle— y el MAEC (26-05-2026) desaconseja los desplazamientos a la región. El pin marca el campo de estelas norte, junto a la taquilla.",
            "when": "Octubre a marzo. Las fiestas marianas de noviembre llenan la ciudad.",
            "skip": "Descártalo mientras Tigray siga desaconsejada, la frontera con Eritrea cerrada y sin confirmar el estado de los accesos por carretera.",
        },
        links=[
            {"label": "UNESCO · Aksum (nº 15)", "url": "https://whc.unesco.org/en/list/15/"},
            {"label": "Axum (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Axum"},
            {"label": "MAEC · Recomendaciones de viaje Etiopía", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Etiop%C3%ADa"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ET_Axum_asv2018-01_img40_Stelae_Park.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ET_Axum_asv2018-01_img40_Stelae_Park.jpg",
                "credit": "A.Savin · FAL",
                "caption": "El parque de estelas norte de Axum.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Stelae,_Aksum,_Ethiopia_(7158408756).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Stelae,_Aksum,_Ethiopia_(7158408756).jpg",
                "credit": "Rod Waddington · CC BY-SA 2.0",
                "caption": "La Gran Estela caída, el mayor monolito jamás tallado.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Facade_of_Axumite_House_-_Main_Stelae_Field_-_Axum_(Aksum)_-_Ethiopia_(8701131121).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Facade_of_Axumite_House_-_Main_Stelae_Field_-_Axum_(Aksum)_-_Ethiopia_(8701131121).jpg",
                "credit": "Adam Jones · CC BY-SA 2.0",
                "caption": "Fachada axumita tallada en una estela.",
            },
        ],
    ),
    dict(
        n=4, name="Gondar · Fasil Ghebbi y los baños de Fasilides (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="1 noche",
        lat=12.6080067, lon=37.4696345,  # Google Maps: Fasil Ghebi (Gondar)
        desc="Fasilides rompió en 1645 la tradición de la corte itinerante y fijó capital en Gondar. El recinto real reúne palacios, tres iglesias, biblioteca, sala de banquetes y baños dentro de una muralla de 900 m con doce puertas, sobre 70.000 m². La mezcla es insólita: influencias hindúes y árabes transformadas por el barroco que trajeron los jesuitas. Los baños de Fasilides, a las afueras, se llenan una vez al año para el TIMKAT (Epifanía, 19 de enero) y se convierten en una piscina bautismal multitudinaria. Amhara está desaconsejada por el MAEC.",
        dog_note="Recinto monumental cerrado con taquilla y con iglesias en uso; no admite animales.",
        visit={
            "why": "Es el único conjunto palaciego «de castillos» de África subsahariana y explica dos siglos de arquitectura etíope.",
            "see": "El castillo de Fasilides, el palacio de Iyasu, la muralla de doce puertas, la iglesia de Debre Berhan Selassie con su techo de ángeles y los baños.",
            "access": "Asfalto desde Bahir Dar (~180 km) y desde Debark. Aparcamiento delante de la puerta principal del recinto, suficiente para dos 4x4; los baños tienen su propio acceso a ~2 km. Entrada conjunta recinto + baños (importe POR CONFIRMAR). SEGURIDAD: región Amhara, escenario del conflicto con las milicias Fano desde agosto de 2023; MAEC (26-05-2026) y FCDO (29-05-2026) desaconsejan viajar allí. El pin marca la puerta de entrada al recinto real.",
            "when": "Octubre a marzo. El 19 de enero (Timkat) es el día grande de los baños.",
            "skip": "Descártalo mientras Amhara siga desaconsejada o haya estado de emergencia regional.",
        },
        links=[
            {"label": "UNESCO · Fasil Ghebbi, Gondar Region (nº 19)", "url": "https://whc.unesco.org/en/list/19/"},
            {"label": "Fasil Ghebbi (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Fasil_Ghebbi"},
            {"label": "MAEC · Recomendaciones de viaje Etiopía", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Etiop%C3%ADa"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ET_Gondar_asv2018-02_img18_Fasil_Ghebbi.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ET_Gondar_asv2018-02_img18_Fasil_Ghebbi.jpg",
                "credit": "A.Savin · FAL",
                "caption": "El recinto real de Fasil Ghebbi, en Gondar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fasil_Ghebbi_(6821473537).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fasil_Ghebbi_(6821473537).jpg",
                "credit": "Martijn Munneke · CC BY 2.0",
                "caption": "El castillo de Fasilides.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_Ruins_at_Gondar,_Ethiopia_-_Mentewabs_Castle_(2414832141).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_Ruins_at_Gondar,_Ethiopia_-_Mentewabs_Castle_(2414832141).jpg",
                "credit": "A. Davey · CC BY 2.0",
                "caption": "El castillo de Mentewab.",
            },
        ],
    ),
    dict(
        n=5, name="Lago Tana · monasterios de las islas y salida del Nilo Azul", cat="Cultura", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=11.6039306, lon=37.3946262,  # Google Maps: Tana Hotel (Bahir Dar, embarcadero del lago Tana)
        desc="El mayor lago de Etiopía, 3.200 km² a 1.788 m, y una de las fuentes del Nilo Azul, que sale por Bahir Dar. En sus islas y penínsulas sobreviven monasterios ortodoxos de los siglos XIV-XVII —Ura Kidane Mehret, Azwa Maryam, Narga Selassie, Kebran Gabriel, Tana Qirqos, Daga Estifanos— con murales y tesoros de manuscritos. Se visitan en barca desde Bahir Dar en medio día o una jornada. Ojo: ALGUNOS MONASTERIOS NO ADMITEN MUJERES, conviene decidir el itinerario con eso delante. Región Amhara, desaconsejada por el MAEC.",
        dog_note="Los monasterios son recintos religiosos en clausura parcial (algunos vetados a mujeres) y se llega en barca compartida: el perro se queda en Bahir Dar.",
        visit={
            "why": "Reúne pintura mural etíope viva, hipopótamos y la salida del Nilo Azul en una misma jornada de barca.",
            "see": "Murales de Ura Kidane Mehret en la península de Zege, Narga Selassie en Dek, hipopótamos en la desembocadura y las barcas de papiro (tankwa).",
            "access": "Bahir Dar está en asfalto desde Adís Abeba (~578 km) y desde Gondar. Los embarcaderos están en el paseo del lago y en los hoteles de la orilla; aparcamiento en el recinto del hotel, aceptable para dos 4x4. Precio de la lancha por grupo, se negocia en el muelle (importe POR CONFIRMAR). SEGURIDAD: Amhara desaconsejada por MAEC (26-05-2026) y FCDO (29-05-2026). El pin marca el embarcadero del Tana Hotel, en Bahir Dar.",
            "when": "Octubre a marzo. Salida a primera hora: el lago se encrespa por la tarde.",
            "skip": "Descártalo si solo dispones de medio día o si Amhara sigue cerrada de hecho por el conflicto.",
        },
        links=[
            {"label": "Lago Tana (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Lake_Tana"},
            {"label": "Bahir Dar (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bahir_Dar"},
            {"label": "MAEC · Recomendaciones de viaje Etiopía", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Etiop%C3%ADa"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Debre_Mariam_Monastery_on_Lake_Tana_Ethiopia_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Debre_Mariam_Monastery_on_Lake_Tana_Ethiopia_(1).jpg",
                "credit": "Radosław Botev · CC BY 3.0 pl",
                "caption": "El monasterio de Debre Mariam, en el lago Tana.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ET_Amhara_asv2018-02_img068_Lake_Tana_at_Bahir_Dar.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ET_Amhara_asv2018-02_img068_Lake_Tana_at_Bahir_Dar.jpg",
                "credit": "A.Savin · FAL",
                "caption": "Hipopótamos en el Tana, cerca de Bahir Dar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/16_lago_Tana_Etiopia.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:16_lago_Tana_Etiopia.JPG",
                "credit": "Cooperazione · CC BY-SA 4.0",
                "caption": "El lago Tana, nacimiento del Nilo Azul.",
            },
        ],
    ),
    dict(
        n=6, name="Cataratas del Nilo Azul · Tis Issat", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="medio día",
        lat=11.4905589, lon=37.588051,  # Google Maps: Cataratas del Nilo Azul
        desc="Tis Abay, «el gran humo» en amárico, cae 42 m sobre el Nilo Azul a unos 30 km aguas abajo de Bahir Dar. Fue el salto más célebre de Etiopía, pero desde 2003 UNA CENTRAL HIDROELÉCTRICA DESVÍA BUENA PARTE DEL CAUDAL y fuera de la estación de lluvias el espectáculo queda muy rebajado. La visita es un circuito a pie de dos a tres horas con puente portugués del siglo XVII y puente colgante. Merece la parada solo entre julio y septiembre, o si ya estás en Bahir Dar.",
        dog_note="Sendero largo con puente colgante, mucha gente y guías locales; no hay prohibición documentada, pero el manejo con perro es incómodo.",
        visit={
            "why": "Es la caída histórica del Nilo Azul y un paseo agradable por campos y aldeas si coincides con aguas altas.",
            "see": "El salto de 42 m, la garganta, el puente portugués sobre el Abbay y el mirador de la orilla opuesta.",
            "access": "~30 km de Bahir Dar por carretera asfaltada hasta el pueblo de Tis Abay y luego pista corta; aparcamiento de tierra junto a la taquilla, holgado para dos 4x4. Entrada y guía local obligatorios (importes POR CONFIRMAR). Región Amhara: MAEC (26-05-2026) desaconseja los desplazamientos a la región. El pin marca la taquilla del pueblo de Tis Abay.",
            "when": "Julio a septiembre, con las lluvias y el caudal alto. Primera hora de la mañana por la luz.",
            "skip": "Descártalo en estación seca: con la central en marcha el salto se queda en un hilo.",
        },
        links=[
            {"label": "Cataratas del Nilo Azul (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Blue_Nile_Falls"},
            {"label": "Lago Tana (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Lake_Tana"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ET_Bahir_Dar_asv2018-02_img17_Tis_Issat.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ET_Bahir_Dar_asv2018-02_img17_Tis_Issat.jpg",
                "credit": "A.Savin · FAL",
                "caption": "Las cataratas del Nilo Azul en Tis Issat.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Blue_Nile_Falls-03,_by_CT_Snow.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Blue_Nile_Falls-03,_by_CT_Snow.jpg",
                "credit": "CT Snow · CC BY 2.0",
                "caption": "El salto visto desde el mirador.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Blue_Nile_Falls,_Ethiopia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Blue_Nile_Falls,_Ethiopia.jpg",
                "credit": "Barrowbob · CC BY-SA 4.0",
                "caption": "El Nilo Azul tras la caída.",
            },
        ],
    ),
    dict(
        n=7, name="Montes Simien · parque nacional, gelada e ibex walia (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="2–3 noches",
        lat=13.2027138, lon=37.8876477,  # Google Maps: Parque nacional de Simien
        desc="Uno de los paisajes de montaña más espectaculares de África: 412 km² de picos, valles y precipicios que caen unos 1.500 m, con el RAS DASHEN (~4.550 m), techo de Etiopía. Aquí viven el ibex walia, que no existe en ningún otro sitio, tropas enormes de gelada y el rarísimo lobo etíope. Fue Patrimonio en Peligro entre 1996 y 2017. Se entra por Debark, a 2.850 m, donde están la sede del parque y los guías y scouts obligatorios. Región Amhara: desaconsejada por el MAEC.",
        dog_note="Parque nacional con lobo etíope, leopardo y fauna endémica muy sensible; los perros domésticos son además vector de rabia y moquillo para el lobo etíope.",
        visit={
            "why": "Es el mejor trekking de altura del continente y la única opción de ver ibex walia en libertad.",
            "see": "Escarpe de Geech, cascada de Jinbar, tropas de gelada a pocos metros, ibex en Chennek y el Bwahit.",
            "access": "Asfalto hasta Debark; dentro del parque, pista de tierra apta para 4x4 hasta Sankaber y Chennek, con tramos expuestos y barro en lluvias. Aparcamiento en los campamentos y en la sede del parque. Entrada por persona y día, más scout armado obligatorio y guía (importes POR CONFIRMAR en la oficina de Debark). SEGURIDAD: Amhara desaconsejada por MAEC (26-05-2026) y FCDO (29-05-2026). El pin marca la sede del parque en Debark, donde se pagan permisos.",
            "when": "Octubre a marzo, seco y despejado; las noches bajan de cero por encima de 3.500 m.",
            "skip": "Descártalo si no puedes dedicarle al menos dos noches dentro del parque o si la región está cerrada por el conflicto.",
        },
        links=[
            {"label": "UNESCO · Simien National Park (nº 9)", "url": "https://whc.unesco.org/en/list/9/"},
            {"label": "Simien Mountains National Park (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Simien_Mountains_National_Park"},
            {"label": "Debark (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Debarq"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Simien_Mountains_National_Park_in_Ethiopia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Simien_Mountains_National_Park_in_Ethiopia.jpg",
                "credit": "Barrowbob · CC BY-SA 4.0",
                "caption": "El escarpe del parque nacional de Simien.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Southern_gelada_(Theropithecus_gelada_obscura)_female_with_baby.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Southern_gelada_(Theropithecus_gelada_obscura)_female_with_baby.jpg",
                "credit": "Charles J. Sharp · CC BY-SA 4.0",
                "caption": "Gelada hembra con cría, endémica de estas montañas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Simien_Mountains,_Ethiopia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Simien_Mountains,_Ethiopia.jpg",
                "credit": "Barrowbob · CC BY-SA 4.0",
                "caption": "Las cumbres del Simien.",
            },
        ],
    ),
    dict(
        n=8, name="Gheralta · iglesias rupestres de Tigray y Abuna Yemata Guh", cat="Cultura", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=13.9152875, lon=39.3452969,  # Google Maps: Iglesia Abuna Yemata Guh (Gheralta)
        desc="El macizo de Gheralta, en Tigray, concentra la mayor agrupación de iglesias excavadas en la roca de Etiopía: unas 35. La más famosa, Abuna Yemata Guh, está a 2.580 m, unos 200 m sobre el llano, y se alcanza TREPANDO SIN CUERDA por agarres tallados en la arenisca, cruzando un puente natural con caída de unos 250 m a ambos lados y una pasarela de madera. Dentro, frescos del siglo XV en muy buen estado. No es apta para quien tenga vértigo. Tigray está desaconsejada por el MAEC.",
        dog_note="Se accede trepando por roca con pasos expuestos y se entra en iglesia en culto: imposible e improcedente con perro.",
        visit={
            "why": "Ninguna otra iglesia del mundo se gana así, y los frescos del XV están casi intactos por el aislamiento.",
            "see": "Frescos y dípticos con texto en ge'ez, la cornisa de acceso, y desde arriba toda la llanura de Hawzen con las agujas de arenisca.",
            "access": "Asfalto hasta Hawzen y Megab; el último tramo hasta el pie de la pared es pista de tierra, bien para 4x4, con aparcamiento informal en el pueblo de Megab. Guía y «escaladores» locales obligatorios, más entrada de la iglesia (importes POR CONFIRMAR). Subida de ~45 min a pie más la trepada. SEGURIDAD: Tigray desaconsejada por MAEC (26-05-2026) y FCDO (29-05-2026); muchas iglesias sufrieron saqueos durante la guerra de 2020-2022 (ESTADO POR CONFIRMAR). El pin marca la iglesia; se conduce hasta Megab.",
            "when": "Octubre a marzo, y a primera hora: la roca se pone al rojo al mediodía.",
            "skip": "Descártalo con vértigo, con lluvia (la arenisca resbala) o mientras Tigray siga desaconsejada.",
        },
        links=[
            {"label": "Abuna Yemata Guh (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Abuna_Yemata_Guh"},
            {"label": "Mekelle, capital de Tigray (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Mekelle"},
            {"label": "MAEC · Recomendaciones de viaje Etiopía", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Etiop%C3%ADa"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Abuna_Yemata_Guh_Mural_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Abuna_Yemata_Guh_Mural_2.jpg",
                "credit": "Mark Fischer · CC BY-SA 2.0",
                "caption": "Murales del siglo XV en Abuna Yemata Guh.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Gheralta_Mountains,_Tigray,_Ethiopia_2013_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Gheralta_Mountains,_Tigray,_Ethiopia_2013_-_panoramio.jpg",
                "credit": "MarcD. · CC BY-SA 3.0",
                "caption": "Los pitones de arenisca del Gheralta.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Houses_in_Gheralta_Massif.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Houses_in_Gheralta_Massif.jpg",
                "credit": "Bernard Gagnon · CC BY-SA 3.0",
                "caption": "Casas al pie del macizo.",
            },
        ],
    ),
    dict(
        n=9, name="Harar · Jugol, la ciudad amurallada y el hombre de las hienas (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=9.3124367, lon=42.121843,  # Google Maps: Harar Jugol
        desc="Ciudad santa del islam —para muchos la cuarta— amurallada entre los siglos XIII y XVI, con cinco puertas históricas y, según la UNESCO, 82 MEZQUITAS, TRES DE ELLAS DEL SIGLO X, y 102 santuarios en apenas 48 hectáreas. Las casas harari, de interiores policromados, son lo más singular del conjunto. Cada noche, desde los años sesenta, los «hombres de las hienas» dan de comer carne cruda a hienas salvajes junto a las murallas. Está en la región Harari, no citada por el MAEC, pero se llega cruzando Oromía, sí desaconsejada.",
        dog_note="Ciudad santa musulmana con mezquitas y santuarios vetados a los perros, callejones densos y, de noche, HIENAS MANCHADAS SUELTAS en las puertas: peligro real para el animal.",
        visit={
            "why": "Es el laberinto urbano más vivo de África oriental y el único sitio donde el hombre convive de forma ritual con las hienas.",
            "see": "Jugol y sus cinco puertas, el mercado, la casa de Arthur Rimbaud, las casas harari tradicionales y el ritual nocturno de las hienas.",
            "access": "Asfalto desde Dire Dawa (~50 km, puerto de montaña) y desde Adís Abeba por Awash. Los coches NO entran en Jugol: se aparca extramuros, junto a la puerta de Shoa/Duke's Memorial. Entrada a museos y casas por separado; propina fija al hombre de las hienas (importes POR CONFIRMAR). SEGURIDAD: región Harari, no nombrada por el MAEC (26-05-2026), pero rodeada por Oromía —desaconsejada— y cerca de la región Somali, también desaconsejada. El pin marca la puerta de Shoa, donde se aparca.",
            "when": "Todo el año; a 1.885 m el clima es benigno. El ritual de las hienas es al anochecer.",
            "skip": "Descártalo si vas con el perro y no tienes alojamiento con patio cerrado: las hienas entran a la ciudad.",
        },
        links=[
            {"label": "UNESCO · Harar Jugol (nº 1189)", "url": "https://whc.unesco.org/en/list/1189/"},
            {"label": "Harar (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Harar"},
            {"label": "MAEC · Recomendaciones de viaje Etiopía", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Etiop%C3%ADa"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Harar,_Ethiopia_-_52016435319.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Harar,_Ethiopia_-_52016435319.jpg",
                "credit": "Ninara31 · CC BY 2.0",
                "caption": "Casa tradicional de Jugol, la ciudad amurallada de Harar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_Hyena_Man_of_Harar.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_Hyena_Man_of_Harar.jpg",
                "credit": "Gusjer · CC BY 2.0",
                "caption": "El hombre de las hienas de Harar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Harar,_Ethiopia_1956.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Harar,_Ethiopia_1956.JPG",
                "credit": "Bair175 · CC BY-SA 3.0",
                "caption": "Harar en 1956.",
            },
        ],
    ),
    dict(
        n=10, name="Depresión del Danakil · Dallol y el volcán Erta Ale", cat="Naturaleza", prio="Media",
        dog="prohibido", time="3–4 noches",
        lat=13.6069149, lon=40.6616942,  # Google Maps: Erta Ale
        desc="El sitio habitado MÁS CALUROSO DE LA TIERRA: en Dallol, a 130 m bajo el nivel del mar, se midió una media anual de 35 °C entre 1960 y 1966. Sus campos hidrotermales de sales amarillas, verdes y naranjas no se parecen a nada. A un día de pista al sur, el Erta Ale (613 m) mantiene el lago de lava más antiguo conocido, activo al menos desde 1906. Es zona de riesgo alto: cinco turistas murieron en un ataque en enero de 2012 y otro fue tiroteado en diciembre de 2017. Solo con escolta.",
        dog_note="Calor extremo, sal, ácido y gases sulfurosos; además exige escolta militar y noches al raso. Inviable para un animal.",
        visit={
            "why": "Es el paisaje geotérmico más extremo del planeta y uno de los pocos lagos de lava permanentes que existen.",
            "see": "Las terrazas y fumarolas de Dallol, el lago salado de Afdera/Karum con las caravanas de sal, y el cráter del Erta Ale de noche.",
            "access": "Asfalto hasta Berahile o Abala y después pistas de sal, lava y arena que exigen 4x4 alto y convoy; el último tramo al Erta Ale se remata a pie de noche. Acceso SOLO en excursión organizada desde Mekelle con permisos, guía afar y ESCOLTA MILITAR OBLIGATORIA. El MAEC (26-05-2026) exige desplazarse en Afar «acompañado de fuerzas de seguridad y de expertos locales», y el FCDO (29-05-2026) desaconseja todo viaje a la región. El pin marca el volcán; se accede por Berahile.",
            "when": "Noviembre a enero, cuando el calor es menos brutal. Nunca de abril a septiembre.",
            "skip": "Descártalo si viajas con vehículo propio sin convoy, con el perro, o mientras Afar siga en nivel de todo viaje desaconsejado.",
        },
        links=[
            {"label": "Erta Ale (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Erta_Ale"},
            {"label": "Dallol (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Dallol,_Ethiopia"},
            {"label": "FCDO · Ethiopia safety and security", "url": "https://www.gov.uk/foreign-travel-advice/ethiopia/safety-and-security"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Erta_Ale.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Erta_Ale.jpg",
                "credit": "filippo_jean · CC BY-SA 2.0",
                "caption": "El volcán Erta Ale, en el Danakil.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Erta-ale_lac-de-lave_2001.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Erta-ale_lac-de-lave_2001.jpg",
                "credit": "Hervé Sthioul · CC BY 2.5",
                "caption": "El lago de lava del Erta Ale.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ET_Afar_asv2018-01_img48_Dallol.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ET_Afar_asv2018-01_img48_Dallol.jpg",
                "credit": "A.Savin · FAL",
                "caption": "Las sales de colores de Dallol.",
            },
        ],
    ),
    dict(
        n=11, name="Valle del Omo · Jinka, Turmi y los mercados del sur (UNESCO)", cat="Cultura", prio="Alta",
        dog="no recomendado", time="3–4 noches",
        lat=5.7959219, lon=36.5733318,  # Google Maps: South Omo Research Center (Jinka)
        desc="El bajo valle del Omo está inscrito por la UNESCO desde 1980 por sus yacimientos de homínidos junto al lago Turkana, pero lo que trae a los viajeros son los pueblos: hamer, mursi, karo, dassanech, bana. Jinka, a 1.490 m, es la base y tiene el museo de investigación del sur del Omo; Turmi, a 925 m, es el pueblo hamer principal, con mercado los lunes y el SALTO DEL TORO como rito de paso. Cuidado con el turismo de fotografía de pago: acuerda el precio antes y respeta las negativas.",
        dog_note="Poblados habitados, ganado por todas partes y visitas con guía: el perro estorba y genera conflicto con los perros locales.",
        visit={
            "why": "Es la región de diversidad cultural más densa de África y un yacimiento clave de la evolución humana.",
            "see": "El museo de Jinka, el mercado de Turmi los lunes, el mercado de Dimeka, los poblados mursi de Mago y las aldeas karo sobre el Omo.",
            "access": "Asfalto hasta Jinka y hasta Turmi; a partir de ahí, pistas de tierra y arena hacia Omorate, Kangaten y los poblados, con vados que se cortan en lluvias. Aparcamiento en los lodges y campings de Turmi y Jinka, amplio. Entrada al parque de Mago y guía/scout obligatorios (importes POR CONFIRMAR). SEGURIDAD: región de Etiopía del Sur; el MAEC (26-05-2026) desaconseja los estados centrales y meridionales y todo punto fronterizo con Kenia y Sudán del Sur. El pin marca el museo de Jinka, base de la zona.",
            "when": "Junio a septiembre y diciembre a febrero (evita las lluvias largas de marzo a mayo). Mercados a primera hora.",
            "skip": "Descártalo si vas con prisa: menos de tres días convierte la visita en un safari fotográfico incómodo.",
        },
        links=[
            {"label": "UNESCO · Lower Valley of the Omo (nº 17)", "url": "https://whc.unesco.org/en/list/17/"},
            {"label": "Jinka (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Jinka"},
            {"label": "Turmi (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Turmi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sunrise,_Omo_Valley,_Ethiopia_(21413550896).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sunrise,_Omo_Valley,_Ethiopia_(21413550896).jpg",
                "credit": "Rod Waddington · CC BY-SA 2.0",
                "caption": "Amanecer en el valle del Omo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Hamar_community_gathering,_Ethiopia,_2011.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Hamar_community_gathering,_Ethiopia,_2011.jpg",
                "credit": "Josep M. Gracia · CC BY-SA 4.0",
                "caption": "Reunión de una comunidad hamer.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Etiopia_-_omo_river_valley_DSC_2835_(43).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Etiopia_-_omo_river_valley_DSC_2835_(43).jpg",
                "credit": "Gianfranco Gori · CC BY-SA 3.0",
                "caption": "Gente y paisaje del bajo Omo.",
            },
        ],
    ),
    dict(
        n=12, name="Montes Bale · lobo etíope y la meseta de Sanetti (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="2–3 noches",
        lat=6.8858193, lon=39.734338,  # Google Maps: Bale Mountains National Park
        desc="215.000 hectáreas inscritas por la UNESCO en 2023 con «las mayores tasas de endemismo animal de cualquier hábitat terrestre del mundo». La meseta de Sanetti, por encima de 3.000 m, es el mayor afroalpino de África y la cruza LA CARRETERA MÁS ALTA DEL CONTINENTE, que pasa junto al Tullu Dimtu (4.385 m). Es el mejor sitio del planeta para ver el lobo etíope, y al sur baja al bosque húmedo de Harenna. Cinco ríos nacen aquí y abastecen a millones de personas. Sede en Dinsho.",
        dog_note="El lobo etíope está en peligro crítico y la rabia y el moquillo transmitidos por perros domésticos son su principal amenaza: entrar con perro es directamente irresponsable.",
        visit={
            "why": "Se conduce de los 2.400 m a los 4.000 m en una mañana y es la mayor probabilidad del mundo de ver lobo etíope.",
            "see": "Lobos etíopes y nyalas de montaña en Sanetti y en el valle del Web, lagos glaciares, lobelias gigantes y el bosque de Harenna con sus colmenas.",
            "access": "Asfalto hasta Dinsho y Goba; la travesía Goba–Sanetti–Rira–Dolo Mena está asfaltada a tramos y con baches severos, apta para los dos 4x4 pero lenta. Aparcamiento en la sede de Dinsho y en los campamentos. Entrada por persona y vehículo, más scout (importes POR CONFIRMAR). SEGURIDAD: región de Oromía, desaconsejada por el MAEC (26-05-2026) y por el FCDO (29-05-2026) por la actividad del OLA. El pin marca la sede del parque en Dinsho.",
            "when": "Octubre a marzo. Cruza Sanetti a primera hora: la niebla y el granizo llegan por la tarde.",
            "skip": "Descártalo si no puedes subir a Sanetti (el lobo apenas se ve por debajo de 3.000 m) o si Oromía está cerrada por operaciones.",
        },
        links=[
            {"label": "UNESCO · Bale Mountains National Park (nº 111)", "url": "https://whc.unesco.org/en/list/111/"},
            {"label": "Bale Mountains National Park (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bale_Mountains_National_Park"},
            {"label": "MAEC · Recomendaciones de viaje Etiopía", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Etiop%C3%ADa"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bale_mountains.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bale_mountains.jpg",
                "credit": "AGoetzke · CC BY-SA 2.0",
                "caption": "La meseta de Sanetti, en los montes Bale.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ethiopian_wolf_(Canis_simensis_citernii)_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ethiopian_wolf_(Canis_simensis_citernii)_2.jpg",
                "credit": "Charles J. Sharp · CC BY-SA 4.0",
                "caption": "Lobo etíope, el cánido más amenazado del mundo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bale_Mtns,_Ethiopia_(16810718520).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bale_Mtns,_Ethiopia_(16810718520).jpg",
                "credit": "Rod Waddington · CC BY-SA 2.0",
                "caption": "Páramo afroalpino del Bale.",
            },
        ],
    ),
    dict(
        n=13, name="Lagos del Rift · Langano, Abiata-Shala y Ziway", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="1–2 noches",
        lat=7.5931358, lon=38.6907762,  # Google Maps: Sabana Beach Resort (lago Langano)
        desc="Tres lagos a un par de horas de la capital por la carretera de Moyale. Langano, 230 km² a 1.585 m, es marrón por su carga mineral y es el ÚNICO LAGO DEL RIFT ETÍOPE LIBRE DE BILHARZIA, así que se puede nadar; su orilla oeste concentra los resorts y campings. Abiata-Shala protege 887 km² con dos lagos alcalinos separados por tres kilómetros de cerros, flamencos comunes y enanos y fuentes termales, aunque el parque está muy degradado por el carboneo y el pastoreo. Ziway (Batu) tiene islas con monasterios e hipopótamos.",
        dog_note="En los resorts de la orilla de Langano suele admitirse con correa; dentro del parque de Abiata-Shala, NO (fauna y aves). Hay cocodrilos e hipopótamos en Ziway: nunca suelto en la orilla.",
        visit={
            "why": "Es la parada de descanso natural del corredor sur, con baño seguro y una avifauna excepcional.",
            "see": "Flamencos y pelícanos en Abiata, las fuentes termales de Shala, el baño en Langano y el monasterio de Tullu Gudo en Ziway.",
            "access": "Todo sobre la carretera asfaltada Adís Abeba–Hawassa; los desvíos a las orillas son pistas de tierra cortas aptas para cualquier 4x4. Aparcamiento amplio en los resorts de Langano, con acampada. Entrada de parque en Abiata-Shala (importe POR CONFIRMAR). SEGURIDAD: región de Oromía, desaconsejada por el MAEC (26-05-2026); la carretera principal es transitada pero ha sufrido cortes por el OLA. El pin marca un resort de la orilla oeste de Langano (ANCLA POR CONFIRMAR sobre el terreno).",
            "when": "Todo el año; mejor entre octubre y marzo. Los flamencos dependen del nivel del agua.",
            "skip": "Descártalo si buscas fauna grande: aquí ya casi no queda, es un sitio de agua y aves.",
        },
        links=[
            {"label": "Lago Langano (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Lake_Langano"},
            {"label": "Parque nacional de Abijatta-Shalla (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Abijatta-Shalla_National_Park"},
            {"label": "Lago Ziway / Batu (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Lake_Ziway"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_Southwestern_shore_of_Lake_Langano,_Ethiopia,_2004-10-29.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_Southwestern_shore_of_Lake_Langano,_Ethiopia,_2004-10-29.jpg",
                "credit": "Sakari A. Maaranen · CC BY 3.0",
                "caption": "La orilla suroeste del lago Langano.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lakes_Shalla,_Abijatta_and_Langano,_January_2017.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lakes_Shalla,_Abijatta_and_Langano,_January_2017.jpg",
                "credit": "Mjr74 · CC BY 4.0",
                "caption": "Shalla, Abiata y Langano desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Flamingoes_on_Lake_Abiyatta.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Flamingoes_on_Lake_Abiyatta.jpg",
                "credit": "Seifu Kidane · CC BY 3.0",
                "caption": "Flamencos enanos en el lago Abiata.",
            },
        ],
    ),
    dict(
        n=14, name="Parque nacional de Awash · el valle y las fuentes termales de Filwoha", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1 noche",
        lat=9.0833333, lon=40.0,  # Google Maps: Parque nacional de Awash
        desc="850 km² de sabana de acacias a unos 900 m, a 225 km de Adís Abeba y partido en dos por LA CARRETERA A DIRE DAWA, que separa las llanuras de Illala Saha de la garganta del Kudu. Tiene las cataratas del Awash, el volcán dormido Fentale (2.007 m) y, en el alto valle del Kudu, las fuentes termales de Filwoha entre palmerales. Se cuentan más de 81 mamíferos, 43 reptiles y 453 aves, pero elefantes, rinocerontes, cebras y búfalos FUERON EXTIRPADOS por la caza y la presión humana.",
        dog_note="Parque nacional con leones, leopardos, guepardos e hipopótamos; los perros no entran.",
        visit={
            "why": "Es el único parque de sabana que se cruza sin desviarse camino de Harar, y las termas de Filwoha son un baño memorable.",
            "see": "Las cataratas del Awash, órix, kudú y babuinos en Illala Saha, el cráter del Fentale y las pozas azules de Filwoha.",
            "access": "Se entra desde la carretera asfaltada Adís Abeba–Dire Dawa; dentro, pistas de tierra y grava aptas para 4x4, con el ramal a Filwoha (~30 km) exigente y arenoso. Aparcamiento en la puerta y en el lodge de las cataratas. Entrada por persona y vehículo, más scout para Fentale (importes POR CONFIRMAR). SEGURIDAD: el parque queda entre Oromía y Afar, ambas desaconsejadas por el MAEC (26-05-2026); la carretera es un corredor de camiones a Yibuti, con accidentes frecuentes. El pin marca la puerta principal, sobre la carretera.",
            "when": "Octubre a febrero. Fauna a primera hora y al atardecer; a mediodía hace un calor brutal.",
            "skip": "Descártalo si vienes de parques de África austral u oriental: la densidad de fauna es baja.",
        },
        links=[
            {"label": "Parque nacional de Awash (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Awash_National_Park"},
            {"label": "UNESCO · Lower Valley of the Awash (nº 10)", "url": "https://whc.unesco.org/en/list/10/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Awash_National_Park,_Ethiopia_(50778515198).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Awash_National_Park,_Ethiopia_(50778515198).jpg",
                "credit": "Nina R · CC BY 2.0",
                "caption": "Sabana del parque nacional de Awash.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Parc_national_d'Awash-Ethiopie-Chutes_d'eau_(2).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Parc_national_d'Awash-Ethiopie-Chutes_d'eau_(2).jpg",
                "credit": "Ji-Elle · CC BY-SA 3.0",
                "caption": "Las cataratas del río Awash.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Awash_National_Park,_Ethiopia_(50072291633).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Awash_National_Park,_Ethiopia_(50072291633).jpg",
                "credit": "Nina R · CC BY 2.0",
                "caption": "El valle del Awash.",
            },
        ],
    ),
    dict(
        n=15, name="Konso · paisaje cultural de terrazas y waga (UNESCO)", cat="Patrimonio UNESCO", prio="Media",
        dog="no recomendado", time="medio día",
        lat=5.3309278, lon=37.426805,  # Google Maps: Konso Cultural Landscape
        desc="23.000 hectáreas de bancales de piedra seca levantados durante más de cuatrocientos años sobre laderas áridas: algunos muros alcanzan los 8 m. Los poblados, encaramados a los cerros, se rodean de UNO A SEIS ANILLOS CONCÉNTRICOS DE MURALLA de bloques de basalto, con plazas comunales (mora) dentro. La firma de Konso son las waga, estatuas de madera que recuerdan a un difunto que mató a un enemigo o a una fiera, y las daga-hela, piedras generacionales. Fue el primer «paisaje cultural» reconocido en Etiopía, en 2011.",
        dog_note="Poblados habitados con recintos amurallados, ganado y bosques sagrados; sin prohibición formal, pero no es lugar para un perro suelto.",
        visit={
            "why": "Es una lección viva de ingeniería agrícola en secano y el único paisaje cultural inscrito del país.",
            "see": "Los bancales de piedra, los poblados amurallados de Mecheke o Gamole, las plazas mora, las waga y el museo de Konso.",
            "access": "Sobre la carretera asfaltada Arba Minch–Jinka/Yabelo; los accesos a los poblados son pistas cortas de tierra, correctas para 4x4 en seco. Aparcamiento en la entrada de cada poblado y en el museo. Guía local prácticamente obligatorio, más entrada al poblado (importes POR CONFIRMAR). SEGURIDAD: Región de Etiopía del Sur, dentro de los estados meridionales que el MAEC (26-05-2026) desaconseja. El pin marca la zona de Karat-Konso, base del paisaje cultural.",
            "when": "Todo el año; mejor de octubre a febrero. Media mañana, con los bancales de lado.",
            "skip": "Descártalo si vas justo de tiempo camino del Omo: es una parada corta y muy dependiente de tener buen guía.",
        },
        links=[
            {"label": "UNESCO · Konso Cultural Landscape (nº 1333)", "url": "https://whc.unesco.org/en/list/1333/"},
            {"label": "Paisaje cultural de Konso (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Konso_Cultural_Landscape"},
            {"label": "Pueblo konso (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Konso_people"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Wagas_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Wagas_01.jpg",
                "credit": "Bernard Gagnon · CC BY-SA 3.0",
                "caption": "Waga, los postes funerarios tallados de Konso.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Street_in_a_Konso_village,_Ethiopia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Street_in_a_Konso_village,_Ethiopia.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Calle de una aldea tradicional konso.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Marketplace_in_the_Ethiopian_town_of_Konso.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Marketplace_in_the_Ethiopian_town_of_Konso.jpg",
                "credit": "Ondřej Havelka · CC BY 4.0",
                "caption": "El mercado de Konso.",
            },
        ],
    ),
    dict(
        n=16, name="Arba Minch · lagos Chamo y Abaya y el parque de Nechisar", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=5.9335499, lon=37.681228,  # Google Maps: Nech Sar National Park (Arba Minch)
        desc="Arba Minch significa «cuarenta manantiales» y debe el nombre a las más de cuarenta fuentes que alimentan un bosque freático al pie del Rift. Entre el lago Abaya, rojizo por el hierro, y el Chamo se extiende el istmo llamado EL PUENTE DE DIOS, dentro del parque nacional de Nechisar: 1.030 km² de llanura de hierba blanca con cebras, hipopótamos y leopardos. En la orilla noroeste del Chamo está el «mercado de cocodrilos», con cientos de cocodrilos del Nilo. El parque nunca llegó a declararse formalmente desde 1974.",
        dog_note="Parque nacional con leopardo e hiena manchada y orillas con cientos de cocodrilos del Nilo; los perros no entran y en la orilla serían presa.",
        visit={
            "why": "Es el mejor mirador del Rift etíope y una salida en barca con cocodrilos enormes a metros del casco.",
            "see": "El Puente de Dios desde el mirador de Arba Minch, cebras en la llanura de Nechisar, el mercado de cocodrilos e hipopótamos en el Chamo.",
            "access": "Asfalto hasta Arba Minch desde Hawassa y desde Konso. Dentro de Nechisar, pistas duras de tierra y roca: la bajada al istmo es exigente y se pasa mejor con dos vehículos por seguridad. Puerta del parque en el lado este de Sikela, el barrio bajo. Entrada por persona y vehículo, más scout y barca aparte (importes POR CONFIRMAR). SEGURIDAD: Región de Etiopía del Sur, dentro de los estados meridionales desaconsejados por el MAEC (26-05-2026). El pin marca la puerta principal del parque.",
            "when": "Octubre a febrero. La barca al mercado de cocodrilos, a media mañana.",
            "skip": "Descártalo en plena estación de lluvias: las pistas de Nechisar se vuelven intransitables.",
        },
        links=[
            {"label": "Parque nacional de Nechisar (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Nechisar_National_Park"},
            {"label": "Arba Minch (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Arba_Minch"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lake_Chamo_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lake_Chamo_01.jpg",
                "credit": "Bernard Gagnon · CC BY-SA 3.0",
                "caption": "El lago Chamo desde Arba Minch.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Crocodylus_niloticus_in_Lake_Chamo_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Crocodylus_niloticus_in_Lake_Chamo_02.jpg",
                "credit": "Bernard Gagnon · CC BY-SA 3.0",
                "caption": "Cocodrilo del Nilo en la orilla del Chamo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Hillside_neighbourhood_in_Arba_Minch,_Ethiopia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Hillside_neighbourhood_in_Arba_Minch,_Ethiopia.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Arba Minch, en la ladera sobre los dos lagos.",
            },
        ],
    ),
    dict(
        n=17, name="Jimma y Kaffa · la cuna del café y los bosques de arábica", cat="Cultura", prio="Media",
        dog="no recomendado", time="1–2 noches",
        lat=7.6976219, lon=36.8684596,  # Google Maps: Palacio de Abba Jifar (Jimma)
        desc="Jimma, a 1.780 m, es la mayor ciudad del suroeste de Oromía y conserva el palacio del rey Abba Jifar I, superviviente del reino de Jimma. Al oeste queda Kaffa, cuyos antepasados kafficho fueron, según la tradición, los primeros en cultivar el cafeto; de ahí viene la palabra «café». La Reserva de Biosfera de Kafa, designada por la UNESCO en 2010, protege 760.144 hectáreas en torno a Bonga y es LA CUNA DEL ARÁBICA SILVESTRE, con cerca de 5.000 variedades salvajes. Es la Etiopía verde y húmeda, muy distinta del norte: barro en lluvias y etapas lentas.",
        dog_note="El palacio de Abba Jifar es recinto con taquilla; en los bosques y fincas cafeteras, con correa y previa consulta.",
        visit={
            "why": "Cierra el círculo del café: el bosque de arábica silvestre está aquí, no en una plantación.",
            "see": "El palacio de Abba Jifar, el mercado de Jimma, los bosques de la Reserva de Biosfera de Kafa en torno a Bonga, el Museo Nacional del Café y las ceremonias de café en cualquier casa.",
            "access": "Asfalto desde Adís Abeba (Bonga está a ~460 km de la capital) y de Jimma a Bonga; el ramal a los bosques de Kaffa es pista de tierra roja, muy resbaladiza con lluvia y con vados. Aparcamiento en el recinto del palacio, en los hoteles y en el centro de información de la reserva, junto al museo del café. SEGURIDAD: Jimma está en Oromía, desaconsejada por el MAEC (26-05-2026); Bonga y la reserva están en la Región de los Pueblos del Suroeste de Etiopía, dentro de los estados que el mismo aviso desaconseja. El pin marca el palacio de Abba Jifar, a las afueras de Jimma.",
            "when": "Octubre a febrero. La cosecha de café va de octubre a diciembre.",
            "skip": "Descártalo si vas justo de días: es un desvío de dos jornadas largas fuera del circuito clásico.",
        },
        links=[
            {"label": "UNESCO MAB · Reserva de Biosfera de Kafa", "url": "https://www.unesco.org/en/mab/kafa"},
            {"label": "Jimma (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Jimma"},
            {"label": "Bonga (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bonga"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Jimma,_Ethiopia_(16842619942).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Jimma,_Ethiopia_(16842619942).jpg",
                "credit": "Rod Waddington · CC BY-SA 2.0",
                "caption": "Jimma, capital del país del café.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_start_of_your_morning_coffee_(5984450578).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_start_of_your_morning_coffee_(5984450578).jpg",
                "credit": "DFID (Reino Unido) · CC BY 2.0",
                "caption": "Recolección de café arábica en Etiopía.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Farmers_farming,Jimma_,Ethiopia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Farmers_farming,Jimma_,Ethiopia.jpg",
                "credit": "Mintsnot · CC BY-SA 4.0",
                "caption": "Campos de labor en la región de Jimma.",
            },
        ],
    ),
    dict(
        n=18, name="Cuevas de Sof Omar · el río Web bajo la caliza", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="medio día",
        lat=6.9050116, lon=40.8374849,  # Google Maps: Sof Umer
        desc="El río Web, que baja de los montes Bale (4.300 m), se mete bajo la caliza y excava 15,1 KM DE GALERÍAS, el mayor sistema de cuevas de Etiopía. El recorrido turístico atraviesa salas con columnas y arcadas naturales y obliga a vadear el río en varios puntos. Es lugar sagrado: debe el nombre a Sof Omar, santo musulmán que vivió en la zona, y lleva siglos siendo centro religioso tanto para el islam como para la fe tradicional oromo. Está en la lista indicativa de la UNESCO desde 2011.",
        dog_note="Cueva sagrada para el islam y para la religión tradicional oromo, con vadeo del río en el interior; no es sitio para un perro.",
        visit={
            "why": "Es la gran cueva fluvial de África oriental y un lugar de culto compartido por dos religiones.",
            "see": "La cámara de las Columnas, los arcos de caliza esculpidos por el agua y la salida del Web al otro lado del macizo.",
            "access": "Desde Robe/Goba, ~120 km de carretera y pista de tierra hacia el este (ESTADO DE LA PISTA POR CONFIRMAR); zona baja y calurosa. Aparcamiento de tierra junto al pueblo, suficiente para dos 4x4. Guía local obligatorio, linterna frontal propia y calzado que se pueda mojar. SEGURIDAD: zona Bale Este, región de Oromía, desaconsejada por el MAEC (26-05-2026). El pin marca la entrada de las cuevas.",
            "when": "Estación seca, de noviembre a febrero: con el río crecido el recorrido interior se cierra.",
            "skip": "Descártalo con lluvias recientes o si no llevas al menos una jornada de margen: es un desvío largo desde Bale.",
        },
        links=[
            {"label": "Cuevas de Sof Omar (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Sof_Omar_Caves"},
            {"label": "Bale Mountains National Park (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bale_Mountains_National_Park"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Underground_River,_Sof_Omer_Cave,_Ethiopia_(11562528124).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Underground_River,_Sof_Omer_Cave,_Ethiopia_(11562528124).jpg",
                "credit": "Rod Waddington · CC BY-SA 2.0",
                "caption": "El río Web bajo la caliza, en Sof Omar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Holuca,_Sof_Omar_Caves.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Holuca,_Sof_Omar_Caves.jpg",
                "credit": "Dave Catlin · CC BY-SA 2.5",
                "caption": "La surgencia de Holuca, en las cuevas de Sof Omar.",
            },
        ],
    ),
    dict(
        n=19, name="Tiya · el campo de estelas grabadas (UNESCO)", cat="Patrimonio UNESCO", prio="Media",
        dog="no recomendado", time="medio día",
        lat=8.4312668, lon=38.6105738,  # Google Maps: Tiya World Heritage Site
        desc="Un prado vallado con 36 monumentos, de los que 32 SON ESTELAS TALLADAS con espadas, discos y signos vegetales que nadie sabe leer. Es el más importante de los cerca de 160 yacimientos de este tipo catalogados en la región de Soddo, al sur de Adís Abeba, y pertenece a una civilización etíope cuya cronología sigue sin fijarse. Visita de treinta o cuarenta minutos, perfecta como parada camino del sur. Está en la zona Gurage, en los estados centrales que el MAEC desaconseja.",
        dog_note="Recinto vallado y pequeño con guarda; sin prohibición documentada, pero mejor dejarlo en el coche a la sombra: la visita dura media hora.",
        visit={
            "why": "Es el testimonio megalítico mejor conservado del país y queda justo sobre la carretera del sur.",
            "see": "Las 32 estelas grabadas en fila, el pequeño centro de interpretación y la explicación del guarda sobre los símbolos de espadas.",
            "access": "A unos 85 km de Adís Abeba por la carretera asfaltada de Butajira; el último kilómetro es pista de tierra. Aparcamiento de tierra junto a la valla, de sobra para dos 4x4. Entrada simbólica cobrada por el guarda (importe POR CONFIRMAR). SEGURIDAD: zona Gurage, en los estados centrales desaconsejados por el MAEC (26-05-2026). El pin marca el recinto vallado del campo de estelas.",
            "when": "Todo el año; la luz rasante de la mañana o la tarde marca mejor los relieves.",
            "skip": "Descártalo si vas a ver Axum: allí las estelas son de otra escala y esto se queda pequeño.",
        },
        links=[
            {"label": "UNESCO · Tiya (nº 12)", "url": "https://whc.unesco.org/en/list/12/"},
            {"label": "Tiya (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Tiya"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tiya_Stelae_Field,_ca._1300_(8)_(28842370870).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tiya_Stelae_Field,_ca._1300_(8)_(28842370870).jpg",
                "credit": "Richard Mortel · CC BY 2.0",
                "caption": "El campo de estelas grabadas de Tiya.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tiya_vue_d'ensemble.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tiya_vue_d'ensemble.JPG",
                "credit": "Julien Demade · CC BY-SA 3.0",
                "caption": "Vista de conjunto de las estelas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tiya_archaeological_site.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tiya_archaeological_site.jpg",
                "credit": "AsfawSeyoum · CC BY-SA 4.0",
                "caption": "Detalle de los grabados de espadas.",
            },
        ],
    ),
    dict(
        n=20, name="Dire Dawa y el ferrocarril a Yibuti · la estación y el mercado de Kefira", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=9.6048717, lon=41.8585081,  # Google Maps: Dire Dawa
        desc="Dire Dawa nació como estación del ferrocarril franco-etíope a Yibuti y sigue siendo, con Adís Abeba, UNA DE LAS DOS ÚNICAS CIUDADES AUTÓNOMAS del país, condición que tiene desde 2004. El río Dechatu la parte en dos: al noroeste, la trama ortogonal que trazaron los ingenieros del ferrocarril; al sureste, Kezira, el barrio del mercado donde se instalaron comerciantes somalíes y árabes. La vieja estación está a unos 10 km del centro; la terminal del nuevo ferrocarril chino, en la ciudad. Buena parada técnica antes de Harar.",
        dog_note="Mercado muy concurrido y calor fuerte; ninguna prohibición formal, pero es una parada urbana y logística, no una visita con perro.",
        visit={
            "why": "Es la única ciudad ferroviaria colonial del Cuerno y la mejor base de servicios antes de subir a Harar.",
            "see": "La estación histórica, la trama europea de Kezira/Megala, el mercado de Kefira y los acantilados que cierran la ciudad.",
            "access": "Asfalto desde Adís Abeba por Awash (corredor de camiones hacia Yibuti) y desde Harar (~50 km de puerto). Hoteles con patio cerrado para dos 4x4. SEGURIDAD: ciudad autónoma, no citada nominalmente por el MAEC (26-05-2026), pero rodeada por Oromía y muy cerca de la región Somali, ambas desaconsejadas; además la ruta hacia el este roza la frontera con Somalia, desaconsejada expresamente. El pin marca la estación histórica del ferrocarril.",
            "when": "Noviembre a febrero: a 1.276 m y en una hondonada, el resto del año hace mucho calor.",
            "skip": "Descártalo como visita cultural: es parada logística, y si vas escaso de tiempo se cambia por una noche más en Harar.",
        },
        links=[
            {"label": "Dire Dawa (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Dire_Dawa"},
            {"label": "Harar (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Harar"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Landing_at_Dire_Dawa.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Landing_at_Dire_Dawa.jpg",
                "credit": "Qchasserieau · CC BY-SA 4.0",
                "caption": "Dire Dawa desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/MosqueDireDawa.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:MosqueDireDawa.JPG",
                "credit": "Arne Hückelheim · CC BY-SA 3.0",
                "caption": "La gran mezquita Jumaa de Dire Dawa.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Djibouti_-_Ethiopia_Railway_Station,_Dire_Dawa,_Ethiopia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Djibouti_-_Ethiopia_Railway_Station,_Dire_Dawa,_Ethiopia.jpg",
                "credit": "A. Davey · CC BY 2.0",
                "caption": "La estación del ferrocarril franco-etíope en Dire Dawa.",
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
    ("Aeropuerto Internacional de Adís Abeba–Bole (ADD)", "Frontera", 8.9837879, 38.7963064,  # Google Maps: Aeropuerto internacional de Bole Adís Abeba (ADD)
     "Entrada aérea principal y único punto donde el eVisa es indiscutiblemente válido. Hub de Ethiopian Airlines, dos terminales y unos 69 puestos de estacionamiento; 2.334 m de altitud. Aquí se exige el certificado de fiebre amarilla y aquí se producen las confiscaciones de drones. Pin comprobado en Google Maps («Aeropuerto internacional de Bole Adís Abeba (ADD)»)."),
    ("Paso fronterizo de Moyale (Kenia–Etiopía)", "Frontera", 3.5359699, 39.0515247,  # Google Maps: Moyale
     "Puesto principal de la carretera Nairobi–Adís Abeba y primer puesto fronterizo de ventanilla única (OSBP) de Etiopía, en servicio desde junio de 2021. Altitud 1.090 m. El MAEC desaconseja la zona fronteriza con Kenia y no garantiza la emisión de visado aquí. Pin comprobado en Google Maps («Moyale»)."),
    ("Paso fronterizo de Omorate (ruta del lago Turkana)", "Frontera", 4.8025849, 36.0540012,  # Google Maps: Omorate
     "Población del bajo Omo a 395 m, alternativa a Moyale por la orilla este del lago Turkana. Dan Grec entró por aquí con vehículo propio en 2020 y recibió un permiso de importación temporal de 60 días. Ruta mucho más dura, aislada y sin servicios; el MAEC desaconseja absolutamente los estados del sur. Pin comprobado en Google Maps («Omorate»)."),
    ("Paso fronterizo de Metema–Gallabat (Sudán)", "Frontera", 12.954462, 36.1572559,  # Google Maps: Metema
     "Cruce comercial con Sudán, a 685 m. Cerrado por Sudán el 1 de septiembre de 2024 tras la toma de Metema por Fano y reabierto tras la recaptura del 21 de octubre de 2024. El MAEC da la frontera sudanesa por cerrada y Metema está en Amhara, región desaconsejada absolutamente. Pin comprobado en Google Maps («Metema»)."),
    ("Paso fronterizo de Galafi (Yibuti)", "Frontera", 11.7168693, 41.8376077,  # Google Maps: Galafi
     "Paso oficial de entrada desde Yibuti por la Carretera Nacional 1, con carretera asfaltada hasta Yibuti ciudad desde 1975. Clima árido, hasta 41 °C en junio. Está en la zona de Afar, parcialmente desaconsejada por el MAEC. Estado para turistas con vehículo propio POR CONFIRMAR. Pin comprobado en Google Maps («Galafi»)."),
    ("Paso fronterizo de Togochale / Tog Wajaale (Somalilandia)", "Frontera", 9.6030127, 43.3415357,  # Google Maps: Wajale (Tog Wajaale / Togochale)
     "Principal paso de mercancías entre Somalilandia y Etiopía por el corredor del puerto de Berbera, con aduana e inmigración somalilandesas. Está en la región Somali, desaconsejada absolutamente por el MAEC; el FCDO veta además de 30 a 100 km de frontera. NO utilizable. Pin comprobado en Google Maps («Wajale (Tog Wajaale / Togochale)»)."),
    ("Humera (frontera con Eritrea y Sudán)", "Frontera", 14.2866615, 36.6096306,  # Google Maps: Humera
     "Última población etíope al sur de la frontera con Eritrea y Sudán, puerta estratégica hacia Sudán. Bombardeada y vaciada durante la guerra de Tigray desde noviembre de 2020, con violencia étnica documentada y control administrativo en disputa. NO utilizable. Pin comprobado en Google Maps («Humera»)."),
    ("Embajada de España en Adís Abeba", "Consular", 9.0620982, 38.7603164,  # Google Maps: Embassy of Spain (Adís Abeba)
     "Haile Melekot Street, Gullele Subcity, Woreda 01, House Nº 036, P.O. Box 2312. Tel. +251 929 136 159; consular +251 929 136 161; fax +251 11 122 25 42; emb.addisabeba@maec.es. Horario de lunes a viernes de 8:30 a 12:30. Emergencia consular 24 h: +251 911 219 403. COORDENADAS APROXIMADAS (Gullele): verificar con la dirección postal. Pin comprobado en Google Maps («Embassy of Spain (Adís Abeba)»)."),
    ("Nordic Medical Centre (Adís Abeba)", "Hospital", 8.9844077, 38.7780562,  # Google Maps: Nordic Medical Centre (Bole)
     "Clínica privada de referencia para extranjeros: Bole Sub City, Kebele 01, House No. 1244. Urgencias 24 horas; consulta de lunes a viernes de 8:30 a 17:30 y sábados de 8:30 a 12:30. Tel. 8901 y +251 929 105 653; reception@nordicmedicalcentre.com. COORDENADAS APROXIMADAS (Bole): verificar con la dirección postal. Pin comprobado en Google Maps («Nordic Medical Centre (Bole)»)."),
    ("Black Lion (Tikur Anbessa) Specialized Hospital", "Hospital", 9.0200753, 38.7502491,  # Google Maps: Tikur Anbessa Specialised Hospital (Black Lion)
     "Hospital universitario público de tercer nivel de la Universidad de Adís Abeba, 700 camas y 15 hectáreas, fundado en 1964. Es el mayor centro especializado del país, pero el MAEC advierte de que los servicios hospitalarios etíopes son muy insuficientes: para cualquier cosa grave, repatriación medicalizada. Pin comprobado en Google Maps («Tikur Anbessa Specialised Hospital (Black Lion)»)."),
    ("Repostaje y depósitos en Adís Abeba (centro)", "Combustible", 9.010573, 38.7611014,  # Google Maps: Meskel Square (Adís Abeba; sin gasolinera concreta como objeto)
     "Adís Abeba, 2.355 m, es donde hay más estaciones y donde primero llega el suministro, pero también donde se han visto colas de dos kilómetros y esperas de ocho horas en abril de 2026. Gasolina 132,18 ETB/l (9-3-2026) y diésel 116,49 ETB/l (9-2-2026), al alza. Estación concreta POR CONFIRMAR. Pin comprobado en Google Maps («Meskel Square (Adís Abeba; sin gasolinera concreta como objeto)»)."),
    ("Repostaje en Moyale (entrada desde Kenia)", "Combustible", 3.5359699, 39.0515247,  # Google Maps: Moyale
     "Primera opción de repostaje al entrar desde Kenia, en la carretera Nairobi–Adís. En marzo de 2018 Goanna Tracks pagaba 18 birr/litro aquí y 16 más al norte, y avisaba de que sin electricidad en el lado etíope no había ni banco ni surtidor. Disponibilidad 2026 POR CONFIRMAR. Pin comprobado en Google Maps («Moyale»)."),
    ("Llenado de depósitos en Adís Abeba", "Agua potable", 9.0098104, 38.7553098,  # Google Maps: Wim's Holland House (Adís Abeba)
     "La red urbana de la capital es la más fiable del país (98,64 % de viviendas con acceso a agua potable según el censo de 2007). Es el punto lógico para llenar depósitos de ducha y lavado en hoteles con jardín o campings. Agua de boca solo embotellada o tratada; filtrar y clorar siempre por los brotes de cólera. Pin comprobado en Google Maps («Wim's Holland House (Adís Abeba)»)."),
    ("Llenado de depósitos en Hawassa (valle del Rift)", "Agua potable", 7.0477329, 38.4957849,  # Google Maps: Awasa (Hawassa)
     "Hawassa, 1.708 m y 273 km al sur de Adís por la carretera de Moyale, es la parada natural del corredor del Rift y capital regional de Sidama. NO llenar del lago Hawassa: hay esquistosomiasis en las aguas dulces del Rift. Punto concreto y potabilidad POR CONFIRMAR sobre el terreno. Pin comprobado en Google Maps («Awasa (Hawassa)»)."),
]

DRONE_CALLOUT = ("danger", "DRONES PROHIBIDOS: se confiscan en aduana",
                 "El MAEC lo dice sin matices: los drones están prohibidos en Etiopía. La Ethiopian Civil Aviation Authority exige licencia de piloto y registro del aparato, y mantiene una lista amplia de zonas vetadas: bases militares y aeropuertos de forma permanente, 500 m de puentes, de 300 m a 1 km de edificios gubernamentales y 2 km de instalaciones petroleras. Los testimonios recogidos por drone-laws.com describen confiscaciones en la aduana de Bole e incluso en vuelos internos, sin devolución posterior. Con un conflicto armado en curso y ataques con drones militares documentados por HRW, volar uno es buscarse un problema grave.")

STARLINK_CALLOUT = ("warn", "STARLINK NO ESTÁ AUTORIZADO EN ETIOPÍA",
                    "Etiopía es uno de los pocos países de África Oriental que sigue cerrado a Starlink. La Ethiopian Communications Authority desmintió en julio de 2025 haber concedido ninguna licencia, con estas palabras: la información que sugiere que Starlink ha recibido la aprobación para lanzar servicios en Etiopía es «entirely false and misleading». En junio de 2026 el país seguía catalogado como «planned, no date». Traducción práctica: no hay itinerancia, no hay activación y meter una antena por la aduana puede acabar en incautación. La conectividad depende del monopolio de Ethio Telecom.")

DOG_MATRIX = [
    ("Entrada por Bole (avión) con permiso previo", "permitido con condiciones", "Tramitar el permiso del Ministerio de Agricultura con semanas de antelación mediante agente o la propia aerolínea; sin permiso, cuarentena a cargo del importador, devolución o eutanasia (PetTravel)."),
    ("Entrada por Moyale u otra frontera terrestre", "por confirmar", "No hay procedimiento documentado para perro que entra por carretera. Plan B: dejar al perro en Kenia con residencia de confianza y entrar en Etiopía sin él."),
    ("Adís Abeba y valle del Rift hasta Hawassa", "permitido con condiciones", "Alojamiento con jardín o camping; perro siempre atado por los callejeros y por el tráfico. Veterinaria privada solo en la capital."),
    ("Parques nacionales (Simien, Bale, Awash, Omo)", "no recomendado", "Presencia de fauna, babuinos y depredadores, y personal armado obligatorio en varios parques. Plan B: dejar al perro con un miembro del grupo en el campamento base fuera del parque."),
    ("Recintos religiosos: Lalibela, Aksum, monasterios del Tana, ciudad amurallada de Harar", "prohibido", "El perro no entra en iglesias ni monasterios ortodoxos ni en mezquitas. Plan B: turnos entre viajeros y sombra en el vehículo; además Lalibela y Aksum están en regiones desaconsejadas por el MAEC."),
    ("Regiones desaconsejadas por el MAEC (Tigray, Amhara, Oromía, Somali, Gambela)", "no recomendado", "No es cuestión del perro sino de la recomendación oficial: no se entra. Plan B: limitar el itinerario a Adís y al corredor del Rift."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Etiopía (actualizado 26 de mayo de 2026, vigencia 13 de septiembre de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Etiop%C3%ADa"),
    ("MAEC · Ficha País Etiopía, PDF (julio de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/ETIOPIA_FICHA%20PAIS.pdf"),
    ("FCDO (gov.uk) · Ethiopia travel advice (actualizado 29 de mayo de 2026)", "https://www.gov.uk/foreign-travel-advice/ethiopia"),
    ("Gobierno de Canadá · Ethiopia travel advice and advisories (consultado en septiembre de 2026)", "https://travel.gc.ca/destinations/ethiopia"),
    ("NaTHNaC TravelHealthPro · Ethiopia country information (revisiones hasta junio de 2026)", "https://travelhealthpro.org.uk/country/76/ethiopia"),
    ("Carnet de Passages en Douane (AIT/FIA) · Ethiopia (consultado en septiembre de 2026)", "https://www.carnetdepassage.org/country/ethiopia"),
    ("Overland Bound Community · «Entering Ethiopia with a car» (hilo de agosto de 2023)", "https://www.overlandbound.com/forums/threads/entering-ethiopia-with-a-car.47191/"),
    ("Goanna Tracks · «Overland Ethiopia. The Border Crossing from and to Kenya» (viaje de marzo de 2018)", "https://www.goannatracks.com/ethiopia-overland.html"),
    ("Bosman's Big Adventure · «Marsabit to Moyale» (relato de cruce a Etiopía)", "https://www.bosmansbigadventure.com/Countries_Visited/Marsabit_to_Moyale.htm"),
    ("Kingsmill Overland · «Africa Overland #10 – Kenya and Ethiopia» (viaje de febrero de 1999)", "https://kingsmilloverland.com/africa/Africa-10.html"),
    ("PikiPiki Overland · Archivo de Etiopía (relatos de 2011, 2012, 2018 y diciembre de 2021)", "https://www.pikipikioverland.com/category/follow-us/ethiopia/"),
    ("Against the Compass · «Travel to Ethiopia: Everything you need to know» (actualizado 31 de agosto de 2026)", "https://againstthecompass.com/en/travel-ethiopia/"),
    ("Ethiopia Observer · «Ethiopia hit hard by the fuel crisis» (9 de abril de 2026)", "https://www.ethiopiaobserver.com/2026/04/09/ethiopia-hit-hard-by-the-fuel-crisis/"),
    ("GlobalPetrolPrices · Precio de la gasolina en Etiopía (dato de 9 de marzo de 2026)", "https://www.globalpetrolprices.com/Ethiopia/gasoline_prices/"),
    ("GlobalPetrolPrices · Precio del diésel en Etiopía (dato de 9 de febrero de 2026)", "https://www.globalpetrolprices.com/Ethiopia/diesel_prices/"),
    ("Birr Metrics · «Ethiopia Denies Granting Starlink License» (4 de julio de 2025)", "https://birrmetrics.com/ethiopia-denies-granting-starlink-license-as-satellite-internet-expansion-faces-regulatory-pushback/"),
    ("tech.africa · «Starlink in Africa: countries, prices and speeds» (actualizado 16 de junio de 2026)", "https://tech.africa/starlink-africa/"),
    ("Drone Laws · «Ethiopia Drone Laws» (actualizado 14 de enero de 2026)", "https://drone-laws.com/drone-laws-in-ethiopia/"),
    ("PetTravel · «Ethiopia Pet Import Requirements» (consultado en septiembre de 2026)", "https://www.pettravel.com/information/pet-passports/ethiopia-pet-import-requirements/"),
    ("FDRE Ministry of Agriculture · Portada oficial (consultado en septiembre de 2026)", "https://www.moa.gov.et/"),
    ("EUR-Lex · Reglamento de Ejecución (UE) 2026/636, de 20 de marzo de 2026, listas de terceros países para desplazamientos sin ánimo comercial de animales de compañía", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600636"),
    ("MAPA · «Viajar con la mascota. Perros, gatos, hurones» (consultado en septiembre de 2026)", "https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones"),
    ("Human Rights Watch · World Report 2026, capítulo Etiopía", "https://www.hrw.org/world-report/2026/country-chapters/ethiopia"),
    ("Wikipedia · Fano insurgency (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Fano_insurgency"),
    ("Wikipedia · Moyale", "https://en.wikipedia.org/wiki/Moyale"),
    ("Wikipedia · Metema", "https://en.wikipedia.org/wiki/Metema"),
    ("Wikipedia · Galafi", "https://en.wikipedia.org/wiki/Galafi"),
    ("Wikipedia · Tog Wajaale", "https://en.wikipedia.org/wiki/Tog_Wajaale"),
    ("Wikipedia · Humera", "https://en.wikipedia.org/wiki/Humera"),
    ("Wikipedia · Borders of Ethiopia", "https://en.wikipedia.org/wiki/Borders_of_Ethiopia"),
    ("Wikipedia · Addis Ababa Bole International Airport", "https://en.wikipedia.org/wiki/Addis_Ababa_Bole_International_Airport"),
    ("Wikipedia · Addis Ababa", "https://en.wikipedia.org/wiki/Addis_Ababa"),
    ("Wikipedia · Hawassa", "https://en.wikipedia.org/wiki/Hawassa"),
    ("Wikipedia · Black Lion Hospital (Tikur Anbessa)", "https://en.wikipedia.org/wiki/Black_Lion_Hospital"),
    ("Nordic Medical Centre · Contacto, Adís Abeba", "https://www.nordicmedicalcentre.com/contact"),
    ("COMESA Yellow Card · Yellow Card overview: cobertura y países emisores y aceptantes (consultado en septiembre de 2026)", "https://comesayellowcard.com/yellow-card-overview"),
    ("COMESA Yellow Card Management Information System · Background del esquema (protocolo firmado en Adís Abeba, 1986)", "http://ycmis.comesa.int/index.php?page=background"),
    ("Wikipedia · International Motor Insurance Card System (Carta Verde y sistemas regionales africanos)", "https://en.wikipedia.org/wiki/International_Motor_Insurance_Card_System"),
    ("Wikipedia · Omorate", "https://en.wikipedia.org/wiki/Omorate"),
    ("Tread Magazine · Dan Grec, «Exploring Ethiopia» (23 de octubre de 2020)", "https://www.treadmagazine.com/features/exploring-ethiopia/"),
    ("East of Elveden · Archivo de diciembre de 2024, trayecto Adís Abeba–Dire Dawa", "https://eastofelveden.com/2024/12/"),
    ("Museo Nacional de Etiopía (Wikipedia)", "https://en.wikipedia.org/wiki/National_Museum_of_Ethiopia"),
    ("Catedral de la Trinidad (Wikipedia)", "https://en.wikipedia.org/wiki/Holy_Trinity_Cathedral,_Addis_Ababa"),
    ("UNESCO · Rock-Hewn Churches, Lalibela (nº 18)", "https://whc.unesco.org/en/list/18/"),
    ("Lalibela (Wikipedia)", "https://en.wikipedia.org/wiki/Lalibela"),
    ("UNESCO · Aksum (nº 15)", "https://whc.unesco.org/en/list/15/"),
    ("Axum (Wikipedia)", "https://en.wikipedia.org/wiki/Axum"),
    ("UNESCO · Fasil Ghebbi, Gondar Region (nº 19)", "https://whc.unesco.org/en/list/19/"),
    ("Fasil Ghebbi (Wikipedia)", "https://en.wikipedia.org/wiki/Fasil_Ghebbi"),
    ("Lago Tana (Wikipedia)", "https://en.wikipedia.org/wiki/Lake_Tana"),
    ("Bahir Dar (Wikipedia)", "https://en.wikipedia.org/wiki/Bahir_Dar"),
    ("Cataratas del Nilo Azul (Wikipedia)", "https://en.wikipedia.org/wiki/Blue_Nile_Falls"),
    ("UNESCO · Simien National Park (nº 9)", "https://whc.unesco.org/en/list/9/"),
    ("Simien Mountains National Park (Wikipedia)", "https://en.wikipedia.org/wiki/Simien_Mountains_National_Park"),
    ("Debark (Wikipedia)", "https://en.wikipedia.org/wiki/Debarq"),
    ("Abuna Yemata Guh (Wikipedia)", "https://en.wikipedia.org/wiki/Abuna_Yemata_Guh"),
    ("Mekelle, capital de Tigray (Wikipedia)", "https://en.wikipedia.org/wiki/Mekelle"),
    ("UNESCO · Harar Jugol (nº 1189)", "https://whc.unesco.org/en/list/1189/"),
    ("Harar (Wikipedia)", "https://en.wikipedia.org/wiki/Harar"),
    ("Erta Ale (Wikipedia)", "https://en.wikipedia.org/wiki/Erta_Ale"),
    ("Dallol (Wikipedia)", "https://en.wikipedia.org/wiki/Dallol,_Ethiopia"),
    ("FCDO · Ethiopia safety and security", "https://www.gov.uk/foreign-travel-advice/ethiopia/safety-and-security"),
    ("UNESCO · Lower Valley of the Omo (nº 17)", "https://whc.unesco.org/en/list/17/"),
    ("Jinka (Wikipedia)", "https://en.wikipedia.org/wiki/Jinka"),
    ("Turmi (Wikipedia)", "https://en.wikipedia.org/wiki/Turmi"),
    ("UNESCO · Bale Mountains National Park (nº 111)", "https://whc.unesco.org/en/list/111/"),
    ("Bale Mountains National Park (Wikipedia)", "https://en.wikipedia.org/wiki/Bale_Mountains_National_Park"),
    ("Lago Langano (Wikipedia)", "https://en.wikipedia.org/wiki/Lake_Langano"),
    ("Parque nacional de Abijatta-Shalla (Wikipedia)", "https://en.wikipedia.org/wiki/Abijatta-Shalla_National_Park"),
    ("Lago Ziway / Batu (Wikipedia)", "https://en.wikipedia.org/wiki/Lake_Ziway"),
    ("Parque nacional de Awash (Wikipedia)", "https://en.wikipedia.org/wiki/Awash_National_Park"),
    ("UNESCO · Lower Valley of the Awash (nº 10)", "https://whc.unesco.org/en/list/10/"),
    ("UNESCO · Konso Cultural Landscape (nº 1333)", "https://whc.unesco.org/en/list/1333/"),
    ("Paisaje cultural de Konso (Wikipedia)", "https://en.wikipedia.org/wiki/Konso_Cultural_Landscape"),
    ("Pueblo konso (Wikipedia)", "https://en.wikipedia.org/wiki/Konso_people"),
    ("Parque nacional de Nechisar (Wikipedia)", "https://en.wikipedia.org/wiki/Nechisar_National_Park"),
    ("Arba Minch (Wikipedia)", "https://en.wikipedia.org/wiki/Arba_Minch"),
    ("UNESCO MAB · Reserva de Biosfera de Kafa", "https://www.unesco.org/en/mab/kafa"),
    ("Jimma (Wikipedia)", "https://en.wikipedia.org/wiki/Jimma"),
    ("Bonga (Wikipedia)", "https://en.wikipedia.org/wiki/Bonga"),
    ("Cuevas de Sof Omar (Wikipedia)", "https://en.wikipedia.org/wiki/Sof_Omar_Caves"),
    ("UNESCO · Tiya (nº 12)", "https://whc.unesco.org/en/list/12/"),
    ("Tiya (Wikipedia)", "https://en.wikipedia.org/wiki/Tiya"),
    ("Dire Dawa (Wikipedia)", "https://en.wikipedia.org/wiki/Dire_Dawa"),
]

# Bucle histórico del norte y ramal este · Adís Abeba – Bahir Dar – Gondar – Simien – Axum – Tigray – Danakil – Lalibela – Awash – Harar
CORRIDOR = [
    (9.03824, 38.76177),
    (11.60393, 37.39463),
    (11.49056, 37.58805),
    (12.60801, 37.46963),
    (13.20271, 37.88765),
    (13.183, 38.067),
    (14.13208, 38.71936),
    (13.91529, 39.3453),
    (13.49694, 39.47694),
    (14.23861, 40.29389),
    (13.60691, 40.66169),
    (12.0332, 39.04339),
    (11.133, 39.633),
    (9.08333, 40.0),
    (9.60487, 41.85851),
    (9.31244, 42.12184),
    (9.03824, 38.76177),
]

# Bucle sur · lagos del Rift, Bale, Sof Omar, Arba Minch, Konso y el Omo
CORRIDOR_ALT = [
    (9.03824, 38.76177),
    (8.43127, 38.61057),
    (8.0, 38.833),
    (7.59314, 38.69078),
    (6.667, 39.667),
    (6.90501, 40.83748),
    (7.05, 38.467),
    (6.033, 37.55),
    (5.33093, 37.42681),
    (5.79592, 36.57333),
]

HISTORIA_RESUMEN = "Etiopía es la gran excepción del continente: un Estado con más de dos mil años de continuidad política que nunca llegó a ser colonizado, salvo los cinco años de ocupación italiana entre 1936 y 1941. Del reino de Aksum heredó una escritura propia, un cristianismo adoptado en el siglo IV y un calendario distinto del occidental. La monarquía salomónica cayó en 1974 ante el Derg marxista; la dictadura de Mengistu se hundió en 1991 y dio paso a una federación de base étnica que perdió su salida al mar con la independencia de Eritrea en 1993. Desde 2018 gobierna Abiy Ahmed, Nobel de la Paz en 2019 y, a la vez, primer ministro de la guerra de Tigray. En 2026 el país crece deprisa y sigue en conflicto abierto."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>El altiplano etíope es uno de los focos más antiguos de estatalidad de África. La Wikipedia en español sitúa el origen del reino de Aksum en la llegada de colonos hacia el año 400 antes de nuestra era; aquel reino llegó a controlar el comercio del mar Rojo con moneda y escritura propias. En el siglo IV, durante el reinado de Ezana, el monje sirio Frumencio introdujo el cristianismo, que cristalizó en la Iglesia ortodoxa etíope Tewahedo. Britannica subraya que esa adopción del siglo IV convierte a Etiopía en una de las naciones cristianas más antiguas del continente.</p><p>Tras el declive de Aksum, la dinastía Zagüe gobernó hasta 1270 y dejó su obra más conocida: las iglesias excavadas en la roca de Lalibela, atribuidas al soberano del mismo nombre, que reinó hacia 1185-1225. En 1270 Yekuno Amlak derrocó al último rey Zagüe y restauró la llamada dinastía salomónica, que reivindicaba descender de Salomón y la reina de Saba. El imperio resistió la invasión de Ahmad ibn Ibrahim al-Ghazi, desarrollada entre 1528 y 1540 y cerrada con la derrota del invasor en la batalla de Wayna Daga el 21 de febrero de 1543. A la muerte del emperador Iyasus II, en 1755, se abrió el <em>Zemene Mesafint</em> o «era de los príncipes», casi un siglo de poder fragmentado entre señores regionales.</p>"),
    ("Colonización",
     "<p>Etiopía es el gran caso atípico del reparto colonial africano. Britannica la describe como el único país africano que resistió con éxito la colonización europea, y presenta la ocupación italiana de 1936 a 1941 como una invasión temporal más que como un dominio colonial asentado. La clave está en el siglo XIX: según la Wikipedia en español, Menelik II modernizó el reino, fundó la nueva capital, Adís Abeba, y abolió la esclavitud.</p><p>El choque llegó por el tratado de Uchalli, firmado con Italia en 1889, cuyas versiones en amárico e italiano no decían lo mismo: Roma sostenía que convertía al país en protectorado. Menelik lo denunció y en 1896 derrotó a los italianos en la batalla de Adua, victoria que garantizó la independencia etíope y que se convirtió en símbolo para todo el continente. Italia conservó Eritrea, la franja costera que resultaría decisiva un siglo después.</p><p>La revancha llegó con Mussolini: Italia se anexionó formalmente Etiopía el 9 de mayo de 1936 y el emperador Haile Selassie marchó al exilio. Los británicos expulsaron a los italianos en 1941 y lo restauraron en el trono. A diferencia de sus vecinos, el país no salió de aquel paréntesis con una administración colonial consolidada ni con una lengua europea impuesta: el amárico siguió siendo la lengua oficial del Estado, como lo es hoy según la ficha país del Ministerio de Asuntos Exteriores español.</p>"),
    ("Independencia y construcción del Estado",
     "<p>Restaurado en 1941, Haile Selassie gobernó hasta 1974 —Britannica fecha su etapa en el poder entre 1916 y 1974— y levantó un Estado centralizado con Adís Abeba como capital diplomática del continente, donde el Ministerio de Asuntos Exteriores español sitúa todavía hoy la sede de la Unión Africana. La federación con Eritrea y su posterior absorción abrieron una guerra independentista de tres décadas.</p><p>El emperador fue depuesto en septiembre de 1974 por un comité de militares, el Derg. En 1975 se proclamó una república popular y en febrero de 1977 Mengistu Haile Mariam tomó el poder y alineó el país con la Unión Soviética. Britannica llama a esa etapa «Etiopía socialista» (1974-1991) y la asocia a la reforma agraria y a la hambruna; la de 1984 dio la vuelta al mundo. La represión, las colectivizaciones y las guerras simultáneas contra los frentes eritreo y tigriño agotaron al régimen.</p><p>En 1991 Mengistu fue derrocado y se exilió en Zimbabue, y el Frente Democrático Revolucionario del Pueblo Etíope tomó el control. La constitución, aprobada el 8 de diciembre de 1994 y en vigor desde el 21 de agosto de 1995, creó una república federal parlamentaria organizada en regiones de base étnica. Eritrea se separó en 1993 y Etiopía quedó sin salida al mar. Entre 1998 y 2000 ambos países libraron una guerra fronteriza cerrada con un acuerdo favorable a Adís Abeba.</p>"),
    ("Historia reciente (2000-2026)",
     "<p>El Frente Democrático Revolucionario del Pueblo Etíope, dominado por el Frente Popular de Liberación de Tigray, gobernó sin alternancia durante dos décadas. Las protestas oromo y amhara de mediados de la década de 2010 acabaron con esa hegemonía: el primer ministro Hailemariam Desalegn dimitió el 15 de febrero de 2018 y Abiy Ahmed juró el cargo el 2 de abril de 2018.</p><p>El primer año fue de apertura. El 9 de julio de 2018 Abiy firmó en Asmara con Isaias Afwerki una declaración de paz y amistad que cerró el contencioso con Eritrea, y el 11 de octubre de 2019 recibió el Premio Nobel de la Paz por esa iniciativa. El 21 de noviembre de 2019 disolvió la vieja coalición en un partido único, el Partido de la Prosperidad.</p><p>El giro llegó el 3 de noviembre de 2020 con la guerra de Tigray, que enfrentó al ejército federal, fuerzas amharas y tropas eritreas con el frente tigriño. Las estimaciones de muertos van de los 162.000-378.000 de la Universidad de Gante a los 600.000 que citó el mediador de la Unión Africana Olusegun Obasanjo. El acuerdo de cese de hostilidades de Pretoria, del 2 de noviembre de 2022, detuvo los combates sin incluir a Eritrea. Desde agosto de 2023 la violencia se trasladó a Amhara, con las milicias Fano, y continúa en Oromía con el Ejército de Liberación Oromo.</p>"),
    ("Política y gobierno en 2026",
     "<p>Según la ficha país del Ministerio de Asuntos Exteriores español actualizada en julio de 2026, Etiopía es una república federal parlamentaria con doce regiones y dos ciudades de estatuto especial, Adís Abeba y Dire Daua. El jefe del Estado es el presidente Taye Atske-Selassie, desde el 7 de octubre de 2024, con funciones puramente protocolarias; el poder lo ejerce el primer ministro Abiy Ahmed, en el cargo desde el 2 de abril de 2018. En las elecciones generales del 1 de junio de 2026 el Partido de la Prosperidad obtuvo 438 de los 486 escaños en juego, para un mandato de cinco años.</p><p>Freedom House clasifica al país como <strong>«no libre»</strong> en su informe de 2025, con 18 puntos sobre 100: 8 sobre 40 en derechos políticos y 10 sobre 60 en libertades civiles. Recuerda que Abiy prometió reformar un Estado autoritario, pero que el país sigue sacudido por conflictos internos y violencia intercomunitaria, con abusos habituales de las fuerzas de seguridad. A la vista de esas fuentes, se trata de un régimen autoritario con elecciones no competitivas, no de una democracia. Reporteros Sin Fronteras lo sitúa en el puesto 148 de 180 en 2026, con 34,66 puntos y cinco periodistas presos. Human Rights Watch cifra en 3,3 millones los desplazados internos a mediados de 2025. España mantiene embajada residente desde 1960 y un Marco de Asociación País 2023-2027.</p>"),
    ("Economía y recursos",
     "<p>La ficha del Ministerio de Asuntos Exteriores español de julio de 2026 describe una economía que crece deprisa y desde muy abajo: un 9,2 % en 2025 según el Fondo Monetario Internacional, con una renta por habitante de 1.910 dólares en 2024 y una inflación del 13,2 %. El Banco Mundial es más severo y sitúa el producto interior bruto por habitante en 979 dólares, con la pobreza al alza del 27 % al 32 % entre 2016 y 2021 y quince millones de personas dependientes de la ayuda alimentaria. La moneda es el bir etíope; en julio de 2026 el cambio rondaba los 183 bir por euro.</p><p>La agricultura aporta cerca de un tercio del producto y emplea al 70 % de la población activa. El café es el principal generador de divisas, seguido del oro, el sésamo, el khat, la horticultura y el ganado. Las exportaciones sumaron 3.300 millones de dólares en 2024 frente a 8.000 millones de importaciones, desequilibrio que explica la fragilidad externa. En diciembre de 2023 el país incurrió en impago de deuda y en julio de 2024 acordó un programa con el Fondo Monetario Internacional que llevó a liberalizar el tipo de cambio. El gran proyecto nacional es la Gran Presa del Renacimiento sobre el Nilo Azul, la mayor de África y fuente permanente de tensión con Egipto.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Etiopía es el segundo país más poblado de África: 128,7 millones de habitantes en 2023 según el Ministerio de Asuntos Exteriores español y 135,9 millones en 2025 según el Banco Mundial. El amárico es la lengua oficial entre cerca de setenta lenguas; desde febrero de 2020 el oromo, el somalí, el tigriña y el afar son lenguas de trabajo federales. El inglés, sin rango oficial, es lo que se encuentra en la carretera; el amárico abre puertas en cualquier región.</p><p>Wikipedia da para 2020 un 61,9 % de cristianos y un 35,9 % de musulmanes (67,3 % y 31,3 % para 2016), con la Iglesia ortodoxa Tewahedo en el 43,8 %. El censo de 2007 daba un 34,5 % de oromo, un 26,9 % de amhara y cerca de un 6 % de somalíes y de tigriños. Hay doce sitios del Patrimonio Mundial, entre ellos Lalibela, Gondar, Harar Jugol y el bajo valle del Omo. La mesa gira en torno a la <em>injera</em> de tef, y aquí nació el café.</p><p>Conviene vestir con discreción y descalzarse y cubrirse hombros y rodillas en los templos. Pedir permiso antes de fotografiar, sobre todo en el Omo. El ramadán de 2027 empieza hacia el 8 de febrero: en zonas musulmanas como Harar no se come ni bebe en público de día. El alcohol es legal y corriente, pero conviene moderarlo en barrios musulmanes.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Etiopía (MAEC España · PDF · julio 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/ETIOPIA_FICHA%20PAIS.pdf"),
    ("Recomendaciones de viaje: Etiopía (MAEC España · act. 26 mayo 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Etiop%C3%ADa"),
    ("Ethiopia (Freedom House · Freedom in the World 2025)", "https://freedomhouse.org/country/ethiopia/freedom-world/2025"),
    ("Ethiopia (Britannica · página principal · consultada 19-09-2026)", "https://www.britannica.com/place/Ethiopia"),
    ("Ethiopia: History (Britannica · consultada 19-09-2026)", "https://www.britannica.com/place/Ethiopia/History"),
    ("Historia de Etiopía (Wikipedia ES · consultada 19-09-2026)", "https://es.wikipedia.org/wiki/Historia_de_Etiop%C3%ADa"),
    ("Etiopía (Wikipedia ES · consultada 19-09-2026)", "https://es.wikipedia.org/wiki/Etiop%C3%ADa"),
    ("Ethiopia (Wikipedia EN · consultada 19-09-2026)", "https://en.wikipedia.org/wiki/Ethiopia"),
    ("Tigray war (Wikipedia EN · consultada 19-09-2026)", "https://en.wikipedia.org/wiki/Tigray_war"),
    ("Abiy Ahmed (Wikipedia EN · consultada 19-09-2026)", "https://en.wikipedia.org/wiki/Abiy_Ahmed"),
    ("Ethiopia · States Parties (UNESCO Patrimonio Mundial · consultada 19-09-2026)", "https://whc.unesco.org/en/statesparties/et"),
    ("Ethiopia (Reporteros Sin Fronteras · Clasificación Mundial 2026)", "https://rsf.org/en/country/ethiopia"),
    ("Ethiopia: Events of 2025 (Human Rights Watch · World Report 2026)", "https://www.hrw.org/world-report/2026/country-chapters/ethiopia"),
    ("Ethiopia Overview (Banco Mundial · datos a marzo de 2026)", "https://www.worldbank.org/en/country/ethiopia/overview"),
]

SPEC = dict(
    slug="etiopia", name="Etiopía", revision="18 sep 2026",
    sub="FUERA DE RUTA — la vuelta de 2027 acaba en Kenia y no sube al Cuerno · ficha informativa: conflicto abierto y desigual por región",
    chips=[
        ("ESTATUS", "FUERA DE RUTA. La vuelta de 2027 acaba en Kenia; ficha informativa para un viaje aparte."),
        ("CÓMO LLEGAR", "Avión a Adís Abeba–Bole (ADD, 8,978 N / 38,799 E) o por tierra desde Kenia por Moyale…"),
        ("VISADO", "OBLIGATORIO y previo. eVisa en evisa.gov.et: 82 USD / 30 días y 102 USD / 90 días (Against…"),
        ("VEHÍCULO", "Sin organización emisora de CPD en el país (AIT/FIA). Relatos de overlanders (Overland Bound…"),
        ("SEGURIDAD", "MAEC desaconseja Tigray, Amhara, Oromía, Somali y Gambela"),
        ("SEGURO", "Sin Carta Verde · Yellow Card COMESA (Etiopía la acepta)"),
        ("SALUD", "Fiebre amarilla OBLIGATORIA · malaria bajo 2.000 m"),
        ("DRONES", "PROHIBIDOS (MAEC) · confiscación en aduana"),
        ("STARLINK", "Sin licencia en Etiopía: no disponible (junio 2026)"),
        ("4x4", "Imprescindible fuera del asfalto · 250 km/día, irreal"),
        ("A PIE", "Solo de día y en la capital; nunca solo de noche"),
        ("PERRO", "Permiso previo de importación del Ministerio de Agricultura…"),
        ("MONEDA", "Birr etíope (ETB). 1 EUR = 183 ETB (Ficha País MAEC, julio 2026). Inflación 13,2 %…"),
        ("VENTANA", "Altiplano a 2.000–2.500 m con clima templado: lluvias largas de junio a mediados de…"),
    ],
    center=[9.73, 39.35], zoom=5,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle histórico del norte y ramal este · Adís Abeba – Bahir Dar – Gondar – Simien – Axum – Tigray – Danakil – Lalibela – Awash – Harar",
    corridor_alt_label="Bucle sur · lagos del Rift, Bale, Sof Omar, Arba Minch, Konso y el Omo",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Bete_Giyorgis_01.jpg?width=1200",
    hero_credit="Lalibela · Bernard Gagnon · CC BY-SA 3.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Etiopía queda fuera del trazado de 2027 por dos motivos que se refuerzan. El primero es de geografía: la vuelta termina en Kenia y no sube al Cuerno de África, de modo que meter Etiopía obligaría a añadir ida y vuelta por Moyale y unos 4.000–5.000 km extra sobre un país del tamaño de Francia y España juntas. El segundo es de riesgo: el MAEC (actualizado el 26 de mayo de 2026) desaconseja ABSOLUTAMENTE viajar a Tigray, Amhara —con Lalibela y Gondar dentro—, Oromía, Somali/Ogadén, Gambela, Benishangul-Gumuz y los estados Central, Sudoccidental y Meridional, es decir, casi todo lo que un overlander querría ver; y desaconseja además las fronteras terrestres con Eritrea, Sudán, Sudán del Sur, Somalia y Kenia. Con ese mapa, la ruta legítima se reduce a Adís Abeba, el valle del Rift hasta Hawassa y poco más. Como viaje aparte sí es concebible: vuelo a Bole, 4x4 alquilado con conductor y guía, dos o tres semanas, orientativamente 3.500–5.000 € por persona con vuelos. Para hacerlo con vehículo propio habría que decidir tres cosas: si el eVisa sirve en frontera terrestre (hoy solo está garantizado en Bole), qué régimen aduanero sustituye al CPD —hay relatos de que Etiopía dejó de aceptarlo a finales de 2022— y si el perro entra o se queda. Nada de eso está cerrado hoy.",
    facts=[
        ("Estatus", "FUERA DE RUTA. La vuelta de 2027 acaba en Kenia; ficha informativa para un viaje aparte."),
        ("Cómo llegar", "Avión a Adís Abeba–Bole (ADD, 8,978 N / 38,799 E) o por tierra desde Kenia por Moyale. MAEC desaconseja todas las fronteras terrestres."),
        ("Visado", "OBLIGATORIO y previo. eVisa en evisa.gov.et: 82 USD / 30 días y 102 USD / 90 días (Against the Compass, ago-2026). MAEC: NO se conceden visados en frontera terrestre."),
        ("Vehículo/aduana", "Sin organización emisora de CPD en el país (AIT/FIA). Relatos de overlanders (Overland Bound, ago-2023) dicen que Etiopía dejó de aceptar CPD y TIP a finales de 2022 y pide depósito aduanero o agente. POR CONFIRMAR."),
        ("Seguro", "Etiopía NO está en el sistema de Carta Verde (solo Marruecos, Túnez e Irán en África y su entorno). SÍ emite y acepta la YELLOW CARD de COMESA, seguro obligatorio de responsabilidad civil a terceros, igual que Kenia, Yibuti y Sudán."),
        ("Moneda", "Birr etíope (ETB). 1 EUR = 183 ETB (Ficha País MAEC, julio 2026). Inflación 13,2 %. Salida limitada a 10.000 USD y 4.000 ETB."),
        ("Perro", "Permiso previo de importación del Ministerio de Agricultura, microchip ISO y rabia entre 30 días y 12 meses antes (PetTravel). Vuelta a la UE: Etiopía NO está en el Anexo II del Reg. (UE) 2026/636 → titulación antirrábica obligatoria."),
        ("Drones", "PROHIBIDOS según el MAEC. La ECAA exige registro y licencia; hay confiscaciones documentadas en aduana y en vuelos internos."),
        ("Starlink", "NO disponible. La Ethiopian Communications Authority negó haber concedido licencia (julio 2025) y el país sigue como «planned, no date» (tech.africa, junio 2026)."),
        ("Seguridad", "Conflicto abierto en Amhara (Fano), Oromía (OLA) y tensión en Tigray tras Pretoria. 3,3 millones de desplazados internos (HRW, informe 2026). Elecciones el 1 de junio de 2026."),
        ("Clima", "Altiplano a 2.000–2.500 m con clima templado: lluvias largas de junio a mediados de septiembre y lluvias cortas de febrero a mayo. Adís Abeba a 2.355 m; Danakil y tierras bajas, extremos de calor."),
        ("Sanidad", "Fiebre amarilla: certificado internacional OBLIGATORIO (MAEC). Malaria por debajo de 2.000 m, no en Adís. El MAEC califica los servicios médicos de «muy insuficientes» y exige seguro con repatriación medicalizada."),
    ],
    alerts=[
        "El MAEC desaconseja ABSOLUTAMENTE viajar a Tigray, Amhara (incluidas Lalibela y Gondar), Oromía, Somali/Ogadén, Gambela, Benishangul-Gumuz y los estados Central, Sudoccidental y Meridional (actualización de 26 de mayo de 2026).",
        "El MAEC también desaconseja las zonas fronterizas: Eritrea (cerrada a extranjeros), Sudán (cerrada), Sudán del Sur (mínimo 100 km), Somalia y Kenia. Entrar por tierra choca de frente con la recomendación oficial.",
        "El eVisa etíope está pensado para el aeropuerto de Bole. El MAEC es tajante: NO se conceden visados en fronteras terrestres. Llegar a Moyale sin visado emitido es exponerse a que no te dejen entrar.",
        "Etiopía ya no tiene organización emisora de CPD y hay relatos de que dejó de aceptarlo a finales de 2022; el régimen alternativo (depósito o agente aduanero) no está confirmado por fuente oficial abierta en esta sesión.",
        "Los DRONES están prohibidos según el MAEC y se confiscan en aduana. Con dos vehículos y material de vídeo, es el punto que más problemas puede dar en la entrada.",
        "Crisis de combustible activa: el suministro diario de diésel se recortó a la mitad (de 9,2 a 4,5 millones de litros) y el precio subió de 129 a 163 birr entre febrero y el 1 de abril de 2026; colas de dos kilómetros en Adís Abeba (Ethiopia Observer, abril de 2026).",
        "La milicia Fano unificó sus dos facciones en el Amhara Fano National Movement el 22 de enero de 2026: el conflicto de Amhara sigue abierto y corta las carreteras del norte, que es justo donde está el patrimonio histórico.",
        "Se han documentado ataques con drones armados del Ejército con víctimas civiles en Amhara (Human Rights Watch, informe mundial 2026). No es un conflicto de baja intensidad.",
        "El MAEC recuerda que la homosexualidad es delito en Etiopía, con penas de uno a cinco años de prisión.",
        "Etiopía es uno de los países con mayor mortalidad por accidentes de tráfico del mundo según el MAEC; ganado suelto, peatones y camiones sin luces hacen inviable conducir de noche.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 20 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada por Moyale", "Moyale (frontera con Kenia) – Yabelo – Hawassa", "~565 km · 2–3 días"),
        ("2 · Lagos del Rift", "Hawassa – Langano – Abiata-Shala – Ziway – Tiya – Adís Abeba", "~300 km · 2 días"),
        ("3 · Subida al noroeste", "Adís Abeba – Debre Markos – Bahir Dar", "~578 km · 2–3 días"),
        ("4 · Lago Tana y el Nilo Azul", "Bahir Dar – Tis Abay – monasterios del Tana – Gondar", "~240 km · 2 días"),
        ("5 · Montes Simien", "Gondar – Debark – Sankaber – Chennek – Debark", "~180 km i/v · 2–3 días"),
        ("6 · Hacia Axum", "Debark – Limalimo – Shire – Axum", "~260 km · 1–2 días"),
        ("7 · Gheralta", "Axum – Adwa – Hawzen (Abuna Yemata Guh) – Mekelle", "~250 km · 2 días"),
        ("8 · Danakil (con escolta)", "Mekelle – Berahile – Dallol – Erta Ale – Mekelle", "~500 km i/v · 3–4 días"),
        ("9 · Lalibela", "Mekelle – Woldiya – Gashena – Lalibela", "~430 km · 2 días"),
        ("10 · Regreso a la capital", "Lalibela – Dessie – Debre Birhan – Adís Abeba", "~640 km · 3 días"),
        ("11 · Ramal este", "Adís Abeba – Awash NP – Dire Dawa – Harar", "~520 km · 2–3 días"),
        ("12 · Suroeste cafetero", "Harar – Adís Abeba – Jimma – Bonga (Kaffa)", "~880 km · 4 días"),
        ("13 · Montes Bale", "Jimma – Shashamane – Dinsho – Goba – Sanetti – Sof Omar", "~600 km · 3 días"),
        ("14 · Omo y salida", "Goba – Arba Minch – Konso – Jinka – Turmi – Yabelo – Moyale", "~900 km · 4–5 días"),
    ],
    offroad=[
        "La travesía de la MESETA DE SANETTI, en el parque nacional de los montes Bale, es la pista de altura clásica del país: la UNESCO y Wikipedia documentan que por el macizo pasa «la carretera más alta de África», con el Tullu Dimtu a 4.385 m, y desciende después al bosque de Harenna hacia Dolo Mena; está asfaltada a tramos pero con baches severos y exige 4x4 y salida temprana.",
        "Dentro del parque nacional de los montes Simien, la pista de tierra Debark – Sankaber – Geech – Chennek es la única ruta rodada y exige scout armado y guía contratados en la sede del parque de Debark, a 2.850 m; con las lluvias de julio a septiembre se embarra y se vuelve muy expuesta.",
        "La bajada a la DEPRESIÓN DEL DANAKIL (Berahile – Hamed Ela – Dallol – Erta Ale) es la pista más dura y la única formalmente vetada al viajero independiente: las visitas a Erta Ale requieren escolta militar, y el MAEC exige ir «acompañado de fuerzas de seguridad y de expertos locales»; el historial de ataques a turistas (2012, 2017) hace que ninguna agencia la abra a vehículos particulares sin convoy.",
        "En el parque nacional de Awash, el ramal de tierra y arena hasta las fuentes termales de FILWOHA, en el alto valle del Kudu, es el tramo más técnico: el resto del parque son pistas de grava, y la carretera asfaltada Adís Abeba – Dire Dawa lo parte en dos, separando las llanuras de Illala Saha de la garganta del Kudu.",
        "En Nechisar, la bajada al istmo del PUENTE DE DIOS entre los lagos Abaya y Chamo es roca suelta y fuerte pendiente: es el tramo donde más compensa llevar los dos vehículos juntos, porque el parque apenas tiene tráfico y no está siquiera declarado legalmente desde 1974.",
        "En el sur del Omo, el asfalto llega a Jinka y a Turmi y a partir de ahí todo es tierra y arena hacia Omorate, Kangaten y las aldeas karo; los vados se cortan con las lluvias largas de marzo a mayo, y el parque nacional de Mago exige scout.",
        "El acceso a las CUEVAS DE SOF OMAR, desde Robe o Goba hacia el este, combina asfalto y pista de tierra en una zona baja y calurosa; el estado concreto del último tramo NO SE HA PODIDO CONFIRMAR con fuente reciente en esta sesión.",
        "ZONAS VETADAS de facto: todo Tigray y Amhara mientras el MAEC mantenga la recomendación de no desplazarse (act. 26-05-2026), la franja fronteriza con Sudán, Sudán del Sur, Kenia y Somalia, y la frontera con Eritrea, cerrada para extranjeros.",
    ],
    senderismo=[
        "Travesía de los Simien, de Sankaber a Geech y Chennek, con noches en campamento a 3.200-3.600 m, guía y scout obligatorios; es el trekking de referencia de Etiopía y el único sitio donde ver ibex walia.",
        "Ascensión al Ras Dashen (~4.550 m), techo de Etiopía, desde Chennek por Ambiko: dos o tres jornadas adicionales dentro del mismo parque.",
        "Subida a Abuna Yemata Guh, en Gheralta: unos 45 minutos de aproximación y luego trepada sin cuerda por agarres tallados en la arenisca, con un puente natural de 250 m de caída a ambos lados y una pasarela de madera final. NO APTA CON VÉRTIGO.",
        "Paseo de Lalibela al monasterio de Asheton Maryam, y excursión más larga a Yemrehana Krestos: ambas iglesias quedan fuera del núcleo excavado y se hacen a pie o en mula.",
        "Circuito a pie de las cataratas del Nilo Azul: dos o tres horas desde el pueblo de Tis Abay, con el puente portugués del siglo XVII y el mirador de la orilla opuesta.",
        "Recorrido interior de las cuevas de Sof Omar siguiendo el río Web bajo la caliza, con vadeos y la cámara de las Columnas; solo en estación seca y con guía local.",
        "Caminatas por la meseta de Sanetti y el bosque de Harenna, en los montes Bale, en busca del lobo etíope y del nyala de montaña; el parque tiene además campamentos de trekking en el valle del Web y en Rafu.",
        "Travesía del Puente de Dios, el istmo entre Abaya y Chamo en Nechisar, y subida al mirador sobre los dos lagos desde Arba Minch.",
    ],
    acampada=[
        "Montes Simien: los campamentos oficiales del parque son Sankaber (~3.200 m, al borde del escarpe entre brezos gigantes), Geech (junto al abismo de Geech y las cataratas de Jinbar) y Chennek (con vistas al Bwahit y al Innatiye); acampar es «la forma más económica de vivir el parque» según Brilliant Ethiopia.",
        "Montes Bale: campamentos de Dinsho (el más básico, junto a la sede), valle del Web (llanuras donde se ve el lobo etíope), monte Waaswma y Rafu (entre formaciones volcánicas).",
        "Danakil: no hay camping, se duerme al raso sobre colchonetas finas o camastros de madera en las aldeas del desierto (Hamed Ela, Abaala) y en el borde del cráter del Erta Ale, siempre dentro de una excursión organizada con escolta.",
        "Valle del Omo: Lale's Camp es el campamento de gama alta para las zonas más remotas; en Turmi y Jinka hay campings y lodges con terreno para plantar tienda y espacio para dos 4x4 (nombres y precios POR CONFIRMAR).",
        "Lagos del Rift: la orilla oeste del lago Langano concentra los resorts con acampada, y es el único lago del país libre de bilharzia donde bañarse; es la parada de descanso natural del corredor sur.",
        "Adís Abeba: la referencia histórica de los overlanders es Wim's Holland House, con aparcamiento y acampada en el patio; aparece fichado en iOverlander, pero la ficha concreta NO SE HA PODIDO ABRIR en esta sesión (robots.txt) y su estado actual queda POR CONFIRMAR.",
        "Awash y Nechisar tienen zonas de acampada dentro del parque junto a las cataratas y a la puerta respectivamente, pero NO HE ENCONTRADO fuente reciente que confirme servicios ni precios.",
        "Acampada libre: en Etiopía es poco realista fuera de los parques y de los recintos privados, por la densidad de población rural y por la situación de seguridad; con el MAEC desaconsejando tantas regiones, dormir fuera de recinto cerrado NO ES RECOMENDABLE.",
    ],
    visado=[
        "VISADO OBLIGATORIO Y PREVIO para españoles. Se tramita en línea en evisa.gov.et o en la Embajada de Etiopía en París, que es la acreditada ante España (MAEC).",
        "Modalidades de turismo: 30 días por 82 USD y 90 días por 102 USD, con tramitación de hasta 3 días (Against the Compass, actualizado el 31 de agosto de 2026). Precio y plazo a reconfirmar en la web oficial antes de pagar.",
        "El eVisa es de ENTRADA ÚNICA. Para varias entradas hay que pedir varios visados; el MAEC lo dice expresamente.",
        "El eVisa es oficialmente válido solo en el aeropuerto internacional de Bole; hay viajeros que declaran haberlo usado por tierra, pero el MAEC afirma que NO se otorgan visados en fronteras terrestres. POR CONFIRMAR para Moyale.",
        "Pasaporte con validez mínima de SEIS MESES y sellado obligatorio a la llegada; la estancia fuera de plazo se sanciona con multas elevadas (MAEC y Gobierno de Canadá).",
        "Entrar con un visado inadecuado (turismo cuando se hace trabajo, voluntariado o rodaje) puede acarrear multas elevadas, expulsión e incluso prisión, según el MAEC.",
    ],
    fronteras_rows=[
        ("Entrada aérea principal", "Aeropuerto Internacional de Adís Abeba–Bole (ADD/HAAB), 8,97778 N / 38,79944 E", "Único punto donde el eVisa es indiscutiblemente válido. Dos terminales, hub de Ethiopian Airlines; 12 millones de pasajeros en 2024 (Wikipedia). Certificado de fiebre amarilla en mano."),
        ("Frontera con Kenia", "Moyale, 3,527 N / 39,056 E", "Puesto fronterizo principal de la carretera Nairobi–Adís y primer OSBP de Etiopía desde junio de 2021. ABIERTO al tráfico, pero el MAEC desaconseja la zona fronteriza con Kenia y el eVisa no está garantizado aquí."),
        ("Frontera con Kenia (ruta del Turkana)", "Omorate, 4,800 N / 35,967 E", "Puesto del bajo Omo a 395 m, alternativa a Moyale por la orilla este del lago Turkana. Dan Grec entró por aquí en 2020 y obtuvo un permiso de importación temporal de 60 días (Tread Magazine). Ruta mucho más dura y solitaria; está en el sur, hoy dentro de los estados que el MAEC desaconseja absolutamente."),
        ("Frontera con Sudán", "Metema–Gallabat, 12,967 N / 36,200 E", "Cerrado por Sudán el 1 de septiembre de 2024 cuando Fano tomó Metema y reabierto tras la recaptura del 21 de octubre de 2024 (Wikipedia). El MAEC da la frontera con Sudán por CERRADA; además está en Amhara, región desaconsejada absolutamente."),
        ("Frontera con Yibuti", "Galafi, 11,71694 N / 41,83667 E", "Paso oficial de la carretera Yibuti-Adís y corredor logístico del puerto de Yibuti. Está en Afar, región parcialmente desaconsejada por el MAEC. Estado para extranjeros con vehículo propio POR CONFIRMAR."),
        ("Frontera con Yibuti (2)", "Dewele, en la línea del ferrocarril Adís–Yibuti", "Paso secundario, sobre todo ferroviario. No se han localizado coordenadas verificadas ni estado 2026 en fuente abierta. POR CONFIRMAR."),
        ("Frontera con Somalilandia", "Togochale / Tog Wajaale, 9,60139 N / 43,33611 E", "Principal entrada de mercancías de Somalilandia por el corredor de Berbera. Está en la región Somali, que el MAEC desaconseja absolutamente; el FCDO veta además una franja de 30–100 km de frontera. NO utilizable."),
        ("Frontera con Eritrea", "Zalambessa, Bure y Rama", "El MAEC la da por CERRADA para extranjeros. El FCDO y Canadá vetan 10 km a cada lado. Ha habido aperturas informales sin confirmar. NO utilizable."),
        ("Frontera con Sudán / Eritrea (oeste)", "Humera, 14,28611 N / 36,60972 E", "Población fronteriza del oeste de Tigray, arrasada en la guerra de 2020-2022 y con disputa administrativa abierta. Región desaconsejada absolutamente por el MAEC. NO utilizable."),
        ("Frontera con Sudán del Sur", "Pasos de Gambela", "Gambela está desaconsejada absolutamente por el MAEC, con toque de queda de 19:00 a 06:00. El MAEC pide mantenerse a 100 km de la frontera. NO utilizable."),
        ("Salida del vehículo", "Reexportación por el mismo régimen aduanero de entrada", "Sin CPD hay que recuperar el depósito o cerrar el expediente con el agente. Sin confirmación oficial del procedimiento; contar con días y con un despachante local. POR CONFIRMAR."),
    ],
    vehiculos=[
        "Se conduce POR LA DERECHA. Matrícula española y documentación del vehículo en regla; Etiopía no forma parte del sistema de Carta Verde —en el que de África solo están Marruecos y Túnez—, así que el seguro europeo no cubre nada aquí.",
        "SEGURO: Etiopía emite y acepta la YELLOW CARD de COMESA, el esquema obligatorio de responsabilidad civil a terceros firmado precisamente en Adís Abeba en 1986. Cubre lesiones y muerte de terceros, daños materiales y, opcionalmente, tratamiento médico de urgencia. Como Kenia también la emite, una Yellow Card contratada allí debería servir; el precio depende de duración y tamaño del vehículo y se pide a la oficina nacional de seguros.",
        "Dato de referencia sobre admisión temporal: Dan Grec, que entró por Omorate en 2020, obtuvo un PERMISO DE IMPORTACIÓN TEMPORAL VÁLIDO 60 DÍAS (Tread Magazine, octubre de 2020). Es el único plazo concreto localizado y hay que darlo por orientativo.",
        "CPD: la AIT/FIA no tiene organización emisora en Etiopía y, según el foro Overland Bound (agosto de 2023), el país dejó de aceptar carnet de passages y TIP a finales de 2022, exigiendo depósito en aduana o la intervención de una agencia. Es el punto más incierto de toda la ficha.",
        "Relatos anteriores a ese cambio (Goanna Tracks, marzo de 2018; Bosman's Big Adventure) describían el procedimiento clásico: sellado del carnet en aduana de Moyale, documento de importación temporal y cotejo de los números de chasis y motor, con más de dos horas de trámite y registro completo del equipaje.",
        "PERMISO DE CONDUCIR: contradicción entre fuentes. El MAEC afirma que Etiopía NO reconoce el permiso internacional y exige permiso etíope; el Gobierno de Canadá dice que el permiso extranjero con IDP vale 45 días y luego hay que sacar el etíope. Llevar ambos y contar con el trámite local.",
        "Dos vehículos de 2,0–2,3 t con depósitos auxiliares son la única forma sensata de moverse con la crisis de combustible de 2026: autonomía mínima de 800 km y bidones homologados.",
        "La media de 250 km/día del proyecto no es realista fuera del corredor asfaltado Adís–Hawassa–Moyale: pistas corrugadas, ganado, altitud de 2.000–3.000 m y controles militares. El MAEC desaconseja conducir de noche fuera de zonas urbanas y sitúa a Etiopía entre los países con mayor mortalidad por accidente del mundo; East of Elveden contó ocho camiones accidentados en un solo trayecto Adís–Dire Dawa en 2024.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "MAEC: los drones están PROHIBIDOS. Es el dato de partida y el que hay que asumir al preparar el equipaje.",
        "La autoridad competente es la Ethiopian Civil Aviation Authority (ECAA, ecaa.gov.et). Exige registro del aparato y licencia de piloto, y publica la lista de zonas prohibidas. No se ha podido abrir su normativa completa en esta sesión.",
        "Distancias mínimas recogidas por drone-laws.com: aeropuertos y bases militares vetados de forma permanente, 500 m de puentes, 300 m a 1 km de edificios gubernamentales y 2 km del centro de instalaciones petroleras.",
        "Riesgo real en frontera: hay testimonios de confiscación en aduana sin acta ni devolución, también en los controles de vuelos domésticos. Si se viaja con dron, declararlo y contar con perderlo.",
        "El contexto agrava el asunto: Human Rights Watch documenta ataques con drones armados del Ejército en Amhara con víctimas civiles en 2025. Un aparato civil volando cerca de una carretera puede leerse como reconocimiento hostil.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "NO DISPONIBLE. La Ethiopian Communications Authority negó en julio de 2025 toda conversación de licencia con Starlink y calificó de falsa la noticia de su aprobación (Birr Metrics).",
        "En la revisión de tech.africa del 16 de junio de 2026 Etiopía aparece como «planned, no date», junto a Yibuti; Kenia y Somalia sí están operativos, y Tanzania y Uganda previstos para 2026.",
        "Sin licencia local, el modo itinerancia de un kit contratado en Europa no funciona sobre territorio etíope; y la importación del terminal puede considerarse equipo de telecomunicaciones no autorizado. No se ha localizado norma aduanera concreta: POR CONFIRMAR.",
        "La alternativa es Ethio Telecom, operador con monopolio de facto. Se venden SIM turísticas y el datos móvil da para hacer hotspot, aunque el wifi de hoteles es malo en todo el país (Against the Compass, agosto de 2026).",
        "Hay historial de cortes de internet y de redes sociales ligados a los conflictos y a procesos electorales: no se puede planificar una expedición contando con conectividad continua.",
    ],
    perro_intro=[
        "ENTRADA: se exige permiso previo de importación del Ministerio de Agricultura, microchip ISO 11784/11785 de 15 dígitos y vacuna antirrábica administrada entre 30 días y 12 meses antes de la llegada, más certificado veterinario del país de origen (PetTravel). No se ha podido abrir una página oficial etíope que lo confirme.",
        "PetTravel añade que desde países considerados de alto riesgo se pide además titulación de anticuerpos antirrábicos, realizada al menos 30 días después de la vacunación. El plazo de validez en días del certificado veterinario no está publicado: POR CONFIRMAR.",
        "RAZAS PROHIBIDAS: Etiopía no publica lista de razas vetadas, según PetTravel; la responsabilidad por la conducta del animal recae en el propietario. Sin lista oficial localizada, se da por confirmado solo a nivel de fuente secundaria.",
        "VUELTA A LA UE: Etiopía NO figura en el Anexo II del Reglamento de Ejecución (UE) 2026/636 —ningún país africano continental está en esa lista; la única excepción africana es Mauricio, insular—. Eso obliga a la vía larga.",
        "Vía A en la práctica: titulación de anticuerpos antirrábicos ≥ 0,5 UI/ml en laboratorio autorizado por la UE, con muestra tomada al menos 30 días después de la vacunación, y entrada en España solo 90 DÍAS DESPUÉS de la extracción, más certificado zoosanitario firmado por veterinario oficial etíope y entrada por un Punto de Entrada de Viajeros autorizado (MAPA).",
        "Lo sensato es hacer la titulación EN ESPAÑA antes de salir y anotarla en el pasaporte europeo: mientras la vacuna no caduque, esa titulación sigue siendo válida y evita depender de un laboratorio etíope.",
        "RIESGOS SOBRE EL TERRENO: rabia endémica, perros callejeros en todas las ciudades, garrapatas y leishmania en tierras bajas, altitudes de más de 2.500 m y temperaturas extremas en Danakil. El MAEC califica la sanidad humana de muy insuficiente; la veterinaria de calidad se limita a Adís Abeba.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "FIEBRE AMARILLA: el MAEC exige certificado internacional de vacunación para entrar. TravelHealthPro confirma que hay riesgo de transmisión en partes del país y que la vacuna no se recomienda solo para Afar y la región Somali.",
        "MALARIA: riesgo alto por debajo de 2.000 m en casi todo el país; no hay riesgo en Adís Abeba ni por encima de esa cota. Profilaxis con atovacuona/proguanil, doxiciclina o mefloquina según pauta (TravelHealthPro, revisión de junio de 2026).",
        "Vacunas recomendadas a casi todo el mundo: hepatitis A, tétanos y fiebre tifoidea; y según perfil, RABIA, meningocócica ACWY, cólera, hepatitis B, polio de recuerdo y sarampión, que es endémico. Con perro a bordo y estancia larga, la preexposición de rabia deja de ser opcional.",
        "Otros riesgos: dengue, chikunguña y zika; esquistosomiasis en agua dulce —no bañarse en los lagos del Rift—; y mal de altura por encima de 2.500 m, cota que se cruza a diario en el altiplano.",
        "El MAEC califica los servicios médicos y hospitalarios de «muy insuficientes» y hace OBLIGATORIO un seguro de viaje que cubra todos los gastos médicos e incluya repatriación aérea medicalizada.",
        "Brotes recientes citados por el MAEC: cólera en las regiones Somali, Oromía y Amhara; virus de Marburgo con brote declarado extinto en enero de 2026; y riesgo de ébola por el papel de Bole como hub aeroportuario continental.",
        "Referencia sanitaria para extranjeros en Adís Abeba: Nordic Medical Centre (Bole Sub City, urgencias 24 h, tel. +251 929 105 653) y, como hospital público de tercer nivel, el Black Lion / Tikur Anbessa de la Universidad de Adís Abeba, con 700 camas.",
    ],
    seguridad_intro="Etiopía no es un país «peligroso» de manera uniforme: es un país con varias guerras a la vez y con una capital razonablemente tranquila. El MAEC desaconseja absolutamente siete regiones enteras, entre ellas Amhara con Lalibela y Gondar dentro, y Oromía, que rodea Adís Abeba por todos lados. Fuera del corredor Adís–Hawassa y de la propia capital, el mapa oficial se cierra casi por completo. A eso se suman terrorismo, delincuencia en aumento contra extranjeros, cortes de carretera y una siniestralidad vial de las peores del mundo.",
    seguridad=[
        "El MAEC (26 de mayo de 2026) desaconseja ABSOLUTAMENTE: Tigray, Amhara —incluidas Lalibela y Gondar—, Oromía, Somali/Ogadén, Gambela con toque de queda de 19:00 a 06:00, Benishangul-Gumuz y los estados Central, Sudoccidental y Meridional, más determinadas zonas de Afar.",
        "El FCDO británico (29 de mayo de 2026) coincide en Tigray, Amhara, Gambela y Afar fronterizo, y añade franjas de exclusión: 20 km con Sudán, 10 km con Sudán del Sur y Eritrea, 100 km con Somalia y Kenia en la región Somali y 10 km con Kenia salvo carreteras y ciudades principales.",
        "El Gobierno de Canadá recomienda evitar todo viaje no esencial al país por disturbios, violencia, ESCASEZ DE COMBUSTIBLE, conflicto armado y delincuencia, con excepción de Adís Abeba, donde pide alto grado de precaución.",
        "Amhara: el conflicto con la milicia Fano sigue abierto. Las dos facciones mayores se unificaron el 22 de enero de 2026 en el Amhara Fano National Movement, con mando conjunto por primera vez; en 2025 hubo ofensivas en Wollo Norte y un ataque aéreo en Gojjam Este con más de cien muertos.",
        "Oromía: combates entre las fuerzas federales y el Ejército de Liberación Oromo (OLA), además de choques entre grupos armados. Rodea Adís Abeba, así que cualquier salida por carretera de la capital atraviesa territorio desaconsejado.",
        "Tigray: el acuerdo de Pretoria de noviembre de 2022 detuvo la guerra abierta, pero persisten desplazamientos forzados desde el Tigray occidental y enfrentamientos entre facciones tigrayanas (HRW, informe mundial 2026).",
        "Human Rights Watch documenta ataques con drones armados con víctimas civiles, detenciones arbitrarias de periodistas, suspensión de organizaciones de derechos humanos y 3,3 millones de desplazados internos.",
        "Elecciones generales el 1 de junio de 2026, con refuerzo de controles de seguridad y disrupciones atribuidas a Fano; históricamente estos periodos traen cortes de internet y estados de emergencia intermitentes.",
        "Delincuencia y tráfico: el MAEC señala aumento de robos con y sin violencia contra extranjeros, desaconseja los deportes de aventura y sitúa a Etiopía entre los países con mayor mortalidad por accidente de tráfico. Añádase que la homosexualidad es delito con penas de uno a cinco años.",
    ],
    agua=[
        "AGUA DE BOCA: solo embotellada o tratada. La recomendación estándar para Etiopía es no beber agua del grifo en ningún punto del país (Against the Compass, agosto de 2026; TravelHealthPro).",
        "AGUA DE USO GENERAL para ducha y lavado: en Adís Abeba la red urbana es la más fiable del país —el censo de 2007 daba un 98,64 % de viviendas con acceso a agua potable— y es donde tiene sentido llenar depósitos, en hoteles con jardín y campings de la capital.",
        "Fuera de la capital, conviene llenar en Hawassa (1.708 m, 273 km al sur de Adís por la carretera de Moyale) y en Adama/Bishoftu, las paradas de camiones del corredor del Rift. Puntos concretos y potabilidad: POR CONFIRMAR sobre el terreno.",
        "Filtrar y clorar siempre el agua que entre en el depósito: hay brotes de cólera activos en las regiones Somali, Oromía y Amhara según el MAEC.",
        "NO bañarse ni llenar en lagos ni ríos del valle del Rift: esquistosomiasis confirmada por TravelHealthPro. Los lagos Langano, Awasa y Chamo quedan descartados como fuente.",
        "Estacionalidad: las lluvias largas van de junio a mediados de septiembre y las cortas de febrero a mayo. En la estación seca de noviembre a enero, la disponibilidad en el sur y en Afar cae mucho.",
    ],
    combustible=[
        "CRISIS ACTIVA. El cierre del estrecho de Ormuz a partir del 28 de febrero de 2026 dejó sin llegar 180.000 toneladas de combustible y obligó a recortar el suministro diario de diésel de 9,2 a 4,5 millones de litros (Ethiopia Observer, 9 de abril de 2026).",
        "Precio del diésel: 116,49 ETB/l el 9 de febrero de 2026 según GlobalPetrolPrices (0,75 USD/l), pero el Ethiopia Observer sitúa la subida de 129 a 163 birr entre febrero y el 1 de abril de 2026, un 26 % en dos meses. El precio real de 2026 hay que darlo por volátil.",
        "Precio de la gasolina: 132,18 ETB/l el 9 de marzo de 2026 (0,844 USD/l, 0,727 EUR/l), muy por debajo de la media mundial porque el mercado está fuertemente subvencionado y regulado (GlobalPetrolPrices).",
        "Colas reales: en Adís Abeba se han visto filas de al menos dos kilómetros con los motores apagados y esperas de ocho horas o de un día entero según los testimonios recogidos por Ethiopia Observer en abril de 2026.",
        "El mercado paralelo es masivo, con el riesgo de calidad que eso implica: filtros de gasóleo de repuesto y decantador de agua son imprescindibles para un Grenadier y una Delica.",
        "Referencia histórica de contraste: en marzo de 2018 el combustible costaba 16–18 birr/litro en Moyale y era mucho más barato que en Kenia (Goanna Tracks). En 2026 esa ventaja se ha evaporado y lo que manda es la disponibilidad, no el precio.",
    ],
    experiencias_intro="Etiopía tuvo mucha literatura overland hasta 2019 y casi nada desde la guerra de Tigray: los relatos recientes con vehículo propio son escasos y los que hay se centran en el corredor de Moyale. Se recogen los más útiles, con su fecha, avisando de cuáles han quedado obsoletos por el cambio aduanero de finales de 2022.",
    experiencias=[
        "Moyale con carnet, cuando el carnet aún valía: Goanna Tracks documenta el cruce de Kenia a Etiopía por Moyale en marzo de 2018. Inmigración en la planta alta y aduana en la baja, sellado del carnet de passages y cumplimentación de un documento de importación temporal. Sin electricidad en el lado etíope, lo que dejaba sin banco ni gasolinera. El combustible costaba 18 birr/litro en Moyale y 16 más al norte, bastante más barato que en Kenia.",
        "El aviso que lo cambia todo: en el hilo «Entering Ethiopia with a car» de Overland Bound, en agosto de 2023, se afirma que Etiopía dejó de aceptar carnet de passages y TIP a finales de 2022, y que el tránsito pasó a exigir depósitos altos en aduana o contratar una agencia. El mismo hilo recomienda contrastar en el foro alemán Wuestenschiff y en HUBB, y cuenta que muchos viajeros optaron por embarcar el vehículo desde Kenia o desviarse por Tanzania y Zambia.",
        "Dos horas de aduana y cotejo de números: Bosman's Big Adventure describe la subida de Marsabit a Moyale y el paso a Etiopía. Los agentes etíopes comprobaron TODOS los números de chasis y motor contra el carnet e inspeccionaron el equipaje al completo, más de dos horas frente al trámite rápido del lado keniano. Insisten en llenar depósitos en Isiolo porque entre Isiolo y Marsabit no hay nada garantizado.",
        "Escasez de combustible, versión 1999: Kingsmill Overland cruzó por Moyale en febrero de 1999 con trámites «straightforward and cordial». La guerra con Eritrea había vaciado las gasolineras y tuvieron que hacer 600 km sin repostar. También cuentan que al pedir el visado etíope les hicieron firmar formularios del vehículo que luego la aduana no siempre exigía. Útil como recordatorio de que la escasez de carburante es recurrente, no nueva.",
        "El Turkana como alternativa a Moyale: PikiPiki Overland publicó en diciembre de 2021 «This is Turkana – Africa's Jade Desert Lake», describiendo la ruta Kenia-Etiopía con dos opciones, la principal por Marsabit y una alternativa mucho menos transitada por el lago Turkana. Es la referencia para quien quiera evitar el eje principal, aunque la ruta del Turkana es más dura y más solitaria.",
        "El relato más completo y más incómodo: Dan Grec cuenta en Tread Magazine (octubre de 2020) su travesía en Jeep desde Omorate hasta la frontera sudanesa, pasando por Jinka, Adís, las montañas Simien y el lago Tana. Le dieron un permiso de importación temporal de 60 días; compró combustible en el mercado negro al doble del precio oficial; pagó guías y guardias armados obligatorios en los parques; y escribe que fue «the only place I have felt unsafe and, in fact, unwelcome», con intentos de forzar las puertas del vehículo.",
        "Ocho horas que fueron doce: East of Elveden describe en diciembre de 2024 el trayecto por carretera de Adís Abeba a Dire Dawa, de amanecer a anochecer. Cotejó el mapa de zonas del FCDO británico y comprobó que la ruta atravesaba zona ámbar y verde rozando una franja roja entre Welenchiti y Metehara. Contó ocho camiones accidentados por el camino. Es la referencia más reciente sobre cómo se conduce realmente en el corredor este.",
        "El diagnóstico de 2026 sobre el terreno: la guía de país de Against the Compass, actualizada el 31 de agosto de 2026, confirma que se puede entrar por tierra desde Sudán, Yibuti, Kenia y Somalilandia, que el eVisa es oficialmente solo para Bole aunque algunos viajeros digan haberlo usado por carretera, que el wifi es «really, really bad» en todo el país y que conviene VPN por la censura. Presupuesto mochilero de 35–40 USD/día.",
        "Colas de dos kilómetros en la capital: Ethiopia Observer, el 9 de abril de 2026, recoge testimonios de conductores de Adís Abeba esperando de la 1:30 a las 9:30 de la mañana por un depósito, y de otro que esperó un día y una noche enteros. Con dos vehículos y perro a bordo, ese es el escenario que hay que dimensionar antes de plantearse la entrada.",
        "Lo que dicen los foros sobre drones: los comentarios recogidos por drone-laws.com describen confiscaciones de drones en la aduana de llegada e incluso en controles de vuelos internos, sin que los propietarios pudieran recuperarlos ni reexportarlos. Coincide con la prohibición tajante que publica el MAEC y desaconseja por completo llevar material aéreo.",
    ],
    pendientes=[
        ("Validez del eVisa en frontera terrestre (Moyale)", "Respuesta por escrito de la Embajada de Etiopía en París o de la Dirección de Inmigración etíope confirmando si el eVisa admite entrada por Moyale; cerrar solo con fuente oficial."),
        ("Régimen aduanero del vehículo tras la retirada del CPD", "Confirmación oficial de la Ethiopian Customs Commission sobre qué documento sustituye al carnet, importe del depósito y plazo de devolución."),
        ("Precio y punto de venta de la Yellow Card COMESA", "Presupuesto por escrito de una oficina nacional de seguros de Kenia o Etiopía para dos vehículos de 2-3 t y 60 días; confirmar si se puede comprar en el propio puesto de Moyale."),
        ("Permiso de conducir válido", "Resolver la contradicción entre el MAEC (no reconoce el permiso internacional) y Canadá (45 días con IDP): confirmación de la autoridad de transporte etíope."),
        ("Permiso previo de importación del perro", "Obtener del Ministerio de Agricultura etíope el formulario, coste, plazo y validez en días del certificado veterinario; cerrar con documento oficial, no con PetTravel."),
        ("Entrada del perro por frontera terrestre", "Confirmar si existe puesto de inspección veterinaria en Moyale o si el permiso solo es operativo en Bole."),
        ("Estado real de los pasos de Galafi y Dewele para extranjeros con vehículo propio", "Testimonio de overlander de 2025-2026 o confirmación de la embajada; hoy solo hay fuente geográfica."),
        ("Normativa completa de drones de la ECAA", "Descargar el reglamento UAS de ecaa.gov.et y verificar si existe algún régimen de permiso para extranjeros o si la prohibición es absoluta."),
        ("Importación del terminal Starlink", "Norma aduanera o de la Ethiopian Communications Authority sobre equipos satelitales no licenciados; hoy solo se sabe que no hay licencia de servicio."),
        ("Coordenadas exactas de la Embajada de España y del Nordic Medical Centre", "Verificación en Google Maps por la persona encargada, a partir de las direcciones postales completas que sí están confirmadas."),
        ("Precio y disponibilidad real de combustible en 2027", "Revisión de GlobalPetrolPrices y de la prensa etíope tres meses antes de cualquier viaje; la crisis de 2026 puede haberse resuelto o agravado."),
        ("Puntos concretos de agua de uso general en el corredor Adís–Hawassa–Moyale", "Entradas de iOverlander o Tracks4Africa posteriores a 2024 con coordenadas y valoración; no se han localizado en esta sesión."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las páginas efectivamente abiertas en esa fecha: MAEC (recomendaciones de viaje actualizadas el 26 de mayo de 2026 y Ficha País de julio de 2026), FCDO, Gobierno de Canadá, TravelHealthPro, EUR-Lex, MAPA y fuentes overland fechadas. Es una herramienta de planificación, no una autorización: ni sustituye la consulta al MAEC antes de salir ni garantiza la entrada del vehículo, del dron o del perro. Todo lo marcado como POR CONFIRMAR debe cerrarse con fuente oficial antes de tomar ninguna decisión.",
    emergency="Emergencia consular española 24 h: +251 911 219 403, solo para situaciones graves y urgentes. Embajada de España en Adís Abeba: +251 929 136 159 y +251 929 136 161, emb.addisabeba@maec.es, de lunes a viernes de 8:30 a 12:30. Número general de emergencias en Etiopía: 991 (Gobierno de Canadá). Los números diferenciados de policía, ambulancia y bomberos NO han podido verificarse en el MAEC: por confirmar. Nordic Medical Centre, urgencias 24 h: +251 929 105 653.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

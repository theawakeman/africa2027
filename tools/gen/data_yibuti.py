# -*- coding: utf-8 -*-
"""Yibuti — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Yibuti está FUERA DE LA RUTA PREVISTA: la vuelta de 2027 termina en Kenia y no sube al Cuerno de África. La ficha es INFORMATIVA, para un viaje aparte. La app ya tiene una ficha corta (3 PDIs: la ciudad, el Lac Assal y el Lac Abbé, sin fotos, sin enlaces y sin ficha de decisión) que hay que SUSTITUIR por la ficha completa con el formato del piloto de Túnez. Es un país pequeño (23.200 km²) y caro, con calor extremo de junio a septiembre (más de 45 °C): la ventana de viaje y el aviso de calor tienen que estar en cada PDI de interior. Peculiaridades a documentar con fuente: el eVisa oficial y si sirve para entrada terrestre, la presencia de bases militares extranjeras (francesa, estadounidense en Lemonnier, china, japonesa) y qué está prohibido fotografiar, el ferrocarril a Adís Abeba y la temporada de tiburón ballena en el golfo de Tadjoura.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/yibuti.json y audit/pdi/yibuti.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Yibuti ciudad · plaza Mahmoud Harbi, mercado central y barrio europeo", cat="Ciudad · servicios", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=11.5922966, lon=43.1460261,  # Google Maps: Mosquée Hamoudi (Yibuti ciudad)
        desc="La capital concentra 776.966 habitantes, el 73 % del país según el censo de 2024. El corazón es la plaza Mahmoud Harbi, presidida por la mezquita Hamoudi (hacia 1906, estilo abasí, unos 1.000 fieles), con el mercado central al lado y, al norte, el trazado colonial francés del barrio europeo fundado en 1888. El conjunto urbano histórico figura en la lista indicativa de la UNESCO desde 2015. PROHIBIDO FOTOGRAFIAR edificios públicos, puerto y personal militar.",
        dog_note="Mercado abarrotado, calor de asfalto y perros callejeros; el recinto de la mezquita Hamoudi está vetado a los animales.",
        visit={
            "why": "Es el único sitio del país con bancos, talleres, repuestos y gasolina fiable, y el contraste entre el damero colonial y el barrio africano se recorre a pie en una mañana.",
            "see": "Mezquita Hamoudi y plaza Mahmoud Harbi, mercado central (Marché Central) con especias y khat, arcadas del barrio europeo y el frente portuario.",
            "access": "Todas las carreteras nacionales convergen aquí; asfalto en buen estado en el casco. El pin marca la mezquita Hamoudi, junto a la plaza; aparcar dos 4x4 en el centro es difícil, es mejor dejarlos en el hotel y caminar. El MAEC clasifica la capital como riesgo medio por amenaza terrorista y desaconseja las playas de Doraleh y Khor Ambado al atardecer por robos.",
            "when": "Noviembre–marzo. De junio a septiembre el calor es extremo (más de 45 °C en el interior, por encima de 40 °C habituales en la ciudad); a diario, primera hora de la mañana.",
            "skip": "Si solo se busca paisaje: la ciudad es cara y la parte monumental se agota en medio día.",
        },
        links=[
            {"label": "Djibouti City (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Djibouti_City"},
            {"label": "Mezquita Hamoudi (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Hamoudi_Mosque"},
            {"label": "Guía oficial · Agence Nationale du Tourisme de Djibouti", "url": "https://guide.visitdjibouti.dj/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Djibouti,_Djibouti_ville.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Djibouti,_Djibouti_ville.jpg",
                "credit": "Clovis conchou · CC BY-SA 4.0",
                "caption": "Yibuti ciudad.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Place_Menelik_in_Djibouti_city_(25058480721).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Place_Menelik_in_Djibouti_city_(25058480721).jpg",
                "credit": "Francisco Anzola · CC BY 2.0",
                "caption": "La plaza Menelik, en el barrio europeo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Hamoudi_mosque_(24856003400).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Hamoudi_mosque_(24856003400).jpg",
                "credit": "Francisco Anzola · CC BY 2.0",
                "caption": "La mezquita Hamoudi, junto al mercado central.",
            },
        ],
    ),
    dict(
        n=2, name="Lac Assal · el punto más bajo de África y sus salinas", cat="Naturaleza", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=11.6611633, lon=42.4135036,  # Google Maps: Lago Assal
        desc="Lago de cráter a 155 metros BAJO EL NIVEL DEL MAR: el punto más bajo de África y el tercero más bajo del planeta. Ocupa unos 54 km² de salmuera con 300 g/L de sal, la segunda masa de agua más salina de la Tierra tras el Don Juan Pond, muy por encima del mar Muerto. La orilla es una costra blanca deslumbrante donde todavía se carga sal para las caravanas hacia Etiopía. Llevar calzado cerrado: la costra corta y el agua abrasa cualquier rozadura.",
        dog_note="Sal cáustica y costras cortantes en las almohadillas, sin sombra y agua imbebible; el perro se queda en el vehículo con aire o no se baja.",
        visit={
            "why": "Es el gran icono geológico del país y uno de los paisajes más extremos accesibles en coche del continente.",
            "see": "Banda de sal blanca, aguas turquesa sobre fondo negro de basalto, montones de sal y vendedores de geodas de sal en el mirador de la orilla sur.",
            "access": "Carretera asfaltada desde la capital, unos 120 km al oeste por la RN-9; el descenso final al lago es una pista corta apta para 4x4 y hay explanada de sobra para dos vehículos. Sin taquilla ni horario conocidos; suele haber vendedores y, a veces, un gesto de propina. El pin marca la cubeta del lago; el acceso rodado habitual es el mirador de la orilla sureste.",
            "when": "Noviembre–marzo, y dentro del día antes de las 10:00. De junio a septiembre el calor es extremo (más de 45 °C) y el lago, sin una sombra, resulta peligroso.",
            "skip": "Si se viaja en verano o a mediodía de cualquier época: el golpe de calor es un riesgo real.",
        },
        links=[
            {"label": "Lake Assal (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Lake_Assal_(Djibouti)"},
            {"label": "Lago Assal (Wikipedia ES)", "url": "https://es.wikipedia.org/wiki/Lago_Assal"},
            {"label": "Lista indicativa UNESCO · Yibuti", "url": "https://whc.unesco.org/en/statesparties/dj"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lake_Assal_1-Djibouti.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lake_Assal_1-Djibouti.jpg",
                "credit": "Fishercd · Public domain",
                "caption": "El lago Assal, a 155 m bajo el nivel del mar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Assal_Lake,_2024.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Assal_Lake,_2024.jpg",
                "credit": "Mheidegger · CC BY 4.0",
                "caption": "Las salinas del Assal.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lake_Assal_NASA.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lake_Assal_NASA.jpg",
                "credit": "NASA · Public domain",
                "caption": "El Assal desde satélite (NASA).",
            },
        ],
    ),
    dict(
        n=3, name="Lac Abbé · las chimeneas de caliza y los flamencos", cat="Naturaleza", prio="Alta",
        dog="no recomendado", time="1 noche",
        lat=11.1986833, lon=41.7805477,  # Google Maps: Lago Abbe
        desc="Lago salado en la frontera con Etiopía, a 243 m de altitud, con un bosque de CHIMENEAS DE CALIZA DE HASTA 50 METROS por las que sale vapor al amanecer. El paisaje, formado por la actividad geotérmica del triángulo de Afar, sirvió de decorado a «El planeta de los simios». Acoge flamencos comunes en sus orillas. Es una de las zonas más inaccesibles del planeta: solo se llega en 4x4 por pista desde Dikhil, y conviene guía y depósito lleno.",
        dog_note="Fumarolas, suelo con costra caliente y fuentes termales; además hay hienas por la noche en el campamento.",
        visit={
            "why": "Amanecer entre chimeneas humeantes, sin infraestructura ni vallas: la imagen más reconocible de Yibuti.",
            "see": "Campo de chimeneas, fuentes termales, salinas y bandadas de flamencos; por la noche, cielo limpio y hienas alrededor del campamento.",
            "access": "Asfalto por la RN-1 hasta Dikhil (122 km desde la capital, unas 3 h) y después pista de arena y grava hacia el suroeste; el lago está a unos 140 km de la capital en línea recta y solo es practicable en 4x4. No hay taquilla ni horario: se duerme en campamentos afar básicos tipo Asboley, con tarifa a negociar. Hay puestos de control; llevar pasaporte y eVisa impresos por la cercanía de la frontera etíope.",
            "when": "Noviembre–enero, llegando la tarde anterior para ver el amanecer. De junio a septiembre el calor es extremo (más de 45 °C) y la zona es inviable; el propio Wikipedia da 30–40 °C de media estival.",
            "skip": "Si no se puede pernoctar: ir y volver en el día se come 8–10 horas de pista y se pierde la luz buena.",
        },
        links=[
            {"label": "Lake Abbe (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Lake_Abbe"},
            {"label": "Lista indicativa UNESCO · Yibuti (Lac Abbeh)", "url": "https://whc.unesco.org/en/statesparties/dj"},
            {"label": "Crónica de viaje · Atlas & Boots", "url": "https://www.atlasandboots.com/travel-blog/lac-abbe-in-djibouti/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Abbe-4-wiki.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Abbe-4-wiki.jpg",
                "credit": "jbcombes · CC BY-SA 3.0",
                "caption": "Las chimeneas de caliza del lago Abbé al amanecer.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Abbe-8.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Abbe-8.jpg",
                "credit": "Jbcombes · CC BY-SA 3.0",
                "caption": "Orillas del lago Abbé.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fumerolle_(Lac_Abbe).JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fumerolle_(Lac_Abbe).JPG",
                "credit": "Cjulien21 · CC BY-SA 3.0",
                "caption": "Fumarola en el Abbé.",
            },
        ],
    ),
    dict(
        n=4, name="Golfo de Tadjoura · tiburón ballena en Arta y el Ghoubbet", cat="Costa", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=11.5838023, lon=42.8232643,  # Google Maps: Arta Plage (golfo de Tadjoura)
        desc="Brazo de mar de unos 1.920 km² que parte el país en dos y recibe el 40 % de los turistas extranjeros. Entre NOVIEMBRE Y ENERO se concentran juveniles de tiburón ballena frente a la playa de Arta y Ras Eiro, y hay salidas regulares de snorkel de 45–60 minutos. En su fondo de saco, el Ghoubbet-el-Kharab (21 km por 11 km, 205 m de profundidad media) marca la unión de las placas africana y arábiga. Corrientes fuertes en el estrecho: nunca nadar por libre allí.",
        dog_note="Las salidas de snorkel con tiburón ballena van en barca pequeña y los operadores no admiten animales.",
        visit={
            "why": "Nadar con tiburón ballena a 40 km de la capital y ver de cerca el punto donde se separan dos continentes.",
            "see": "Juveniles de tiburón ballena, delfines, el arrecife de Ras Eiro y «The Crack»; acantilados negros sobre el Ghoubbet.",
            "access": "Arta está a 41 km de la capital por asfalto; el embarque para el snorkel es en la playa, bajo el pueblo, por pista corta con espacio para aparcar. Los operadores de la capital programan salidas viernes y sábados en temporada, en torno a 110 USD el snorkel y 160 USD la inmersión. El pin marca el centro del golfo; el punto navegable es la plage d'Arta. Aguas de Bab el-Mandeb y golfo de Adén: el MAEC las desaconseja por piratería.",
            "when": "Noviembre–enero para el tiburón ballena; salidas a primera hora. De junio a septiembre, calor extremo (más de 45 °C en el interior) y sin avistamientos.",
            "skip": "Fuera de la ventana de noviembre a enero la excursión pierde su motivo principal.",
        },
        links=[
            {"label": "Gulf of Tadjoura (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Gulf_of_Tadjoura"},
            {"label": "Dolphin Excursions Djibouti · temporada de tiburón ballena", "url": "https://www.divedjibouti.com/whalesharks"},
            {"label": "Ghoubbet-el-Kharab (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ghoubbet-el-Kharab"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Gulf_of_Tadjoura_NASA.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Gulf_of_Tadjoura_NASA.jpg",
                "credit": "NASA · Public domain",
                "caption": "El golfo de Tadjoura visto desde satélite (NASA); imagen de contexto, no del tiburón ballena.",
            },
        ],
    ),
    dict(
        n=5, name="Tadjoura · la ciudad blanca de las siete mezquitas", cat="Cultura", prio="Alta",
        dog="no recomendado", time="1 noche",
        lat=11.7873808, lon=42.8810929,  # Google Maps: Tadjoura
        desc="Uno de los asentamientos más antiguos del país y tercera ciudad de Yibuti con 18.808 habitantes (censo de 2024). Se la conoce como la ciudad blanca de las SIETE MEZQUITAS por sus casas encaladas sobre la orilla norte del golfo. Fue puerto alternativo a Zeila en el siglo XIX y punto de salida de las caravanas hacia Etiopía; Arthur Rimbaud vivió aquí en los años 1880 traficando con armas. El distrito tiene minas sin desactivar confirmadas: no salir de pistas marcadas.",
        dog_note="Ciudad muy religiosa con siete mezquitas activas: el perro no entra en ningún recinto y llama la atención en las calles.",
        visit={
            "why": "La estampa encalada frente al golfo y el peso histórico de un puerto caravanero que aún funciona.",
            "see": "Mezquitas blancas del casco antiguo, el puerto nuevo (90 millones de dólares), el mercado y la playa de arena al este.",
            "access": "Asfalto: RN-9 desde la capital, 123 km, segunda carretera más larga del país; también ferry desde Yibuti ciudad, unas 2,5 h para 130 km. La RN-14 sigue 61 km hacia Obock. Aparcamiento fácil junto al puerto. El pin marca el centro urbano; el objeto navegable es el puerto.",
            "when": "Noviembre–marzo; al atardecer, con el encalado a contraluz. Junio–septiembre, calor extremo (más de 45 °C en el interior del macizo vecino).",
            "skip": "Si el tiempo es corto y ya se va a subir a Randa y la Forêt du Day, Tadjoura puede quedarse en parada de paso.",
        },
        links=[
            {"label": "Tadjoura (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Tadjoura"},
            {"label": "RN-9 (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/National_Highway_9_(Djibouti)"},
            {"label": "Tadjoura · Wikitravel", "url": "https://wikitravel.org/en/Tadjoura"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tagore.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tagore.jpg",
                "credit": "Driss · CC BY-SA 2.0 de",
                "caption": "Tadjoura, la ciudad blanca, desde el mar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tadjoura_in_1887.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tadjoura_in_1887.jpg",
                "credit": "Skilla1st · Public domain",
                "caption": "Tadjoura en 1887.",
            },
        ],
    ),
    dict(
        n=6, name="Obock · el primer establecimiento francés del Cuerno", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=11.9647465, lon=43.2884071,  # Google Maps: Obock
        desc="Puerto en la orilla norte, donde el golfo de Tadjoura se abre al de Adén. Aquí nació la colonia francesa: el TRATADO CON LOS SULTANES AFAR SE FIRMÓ EL 11 DE MARZO DE 1862 y en 1884 Léonce Lagarde la convirtió en asentamiento real, antes de que la capital se trasladara a Yibuti en 1894. Quedan 20.152 habitantes, ruinas coloniales, un faro y playas desiertas. Es distrito con minas confirmadas y a menos de 20 km de la franja fronteriza con Eritrea que EE. UU. recomienda evitar.",
        dog_note="Pueblo abierto y playas vacías, pero con calor tremendo: solo con sombra, agua y paseos de amanecer o noche.",
        visit={
            "why": "El origen de la presencia francesa en el Cuerno, con un abandono fotogénico y playas sin nadie.",
            "see": "Restos del puesto colonial y del cementerio, el faro, el mercado afar y los manglares de Godoria y Khor Angar al norte.",
            "access": "RN-14 asfaltada desde Tadjoura, 61 km; también ferry desde la capital, unos 237 km por mar en torno a 3 h. Aparcar es libre. El pin marca el núcleo urbano. AVISO: MAEC sitúa el distrito en riesgo medio por minas y Estados Unidos desaconseja acercarse a menos de 16 km de la frontera eritrea.",
            "when": "Noviembre–marzo. De junio a septiembre el calor es extremo (más de 45 °C tierra adentro) y no hay refugio.",
            "skip": "Si no se va a subir a los manglares del norte ni a las Sept Frères, Obock no justifica por sí sola el rodeo.",
        },
        links=[
            {"label": "Obock (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Obock"},
            {"label": "Recomendaciones de viaje MAEC · Yibuti", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Yibuti"},
            {"label": "US Travel Advisory · Djibouti", "url": "https://travel.state.gov/en/international-travel/travel-advisories/djibouti.html"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Obock_ferry.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Obock_ferry.jpg",
                "credit": "Charles Roffey · CC BY-SA 3.0",
                "caption": "El ferry de Yibuti llegando a Obock.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Obock(r%C3%A9s_Lagarde).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Obock(r%C3%A9s_Lagarde).jpg",
                "credit": "Postal, Yibuti h. 1920-1930 · Public domain",
                "caption": "Obock hacia 1920-1930.",
            },
        ],
    ),
    dict(
        n=7, name="Forêt du Day · el bosque de enebros del macizo de Goda (Parque Nacional)", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1 noche",
        lat=11.7541978, lon=42.6880552,  # Google Maps: Parque nacional del Bosque de Day
        desc="Parque nacional creado en 1939 en el macizo de Goda, el mayor bosque de Yibuti: unas 900 hectáreas de enebro africano (Juniperus procera) por encima de los 950 metros, con ejemplares de hasta 20 m. Aquí viven tres aves que no existen en ningún otro sitio, entre ellas el francolín de Yibuti. Es también la zona más lluviosa del país, con unos 500 mm anuales. Aviso: SE HA PERDIDO EL 88 % DEL BOSQUE EN DOS SIGLOS y el enebro está muriendo en pie.",
        dog_note="Parque nacional con aves endémicas amenazadas: el perro queda fuera del recinto forestal.",
        visit={
            "why": "Es la única mancha de bosque del país y 20 grados menos de sensación térmica que la costa.",
            "see": "Enebros secos y vivos, acebuches y bojes, terrazas agrícolas, francolín de Yibuti y buitres sobre el macizo.",
            "access": "Asfalto RN-9 hasta Tadjoura y luego RN-11 a Randa (32 km al sur de Randa queda Tadjoura); desde Randa, a unos 16 km, pista de montaña con rampas fuertes que exige 4x4 y reductora. Explanadas para aparcar cerca del mirador. No consta taquilla ni horario oficial; los operadores locales ponen guía. El pin marca el corazón del parque.",
            "when": "Noviembre–marzo, con mañana temprana para las aves. De junio a septiembre el interior pasa de 45 °C, aunque la altura suaviza algo (Randa: 34,7 °C de media de tarde en junio).",
            "skip": "Con lluvia fuerte o barro: la pista de subida se vuelve resbaladiza y sin escapatoria.",
        },
        links=[
            {"label": "Day Forest National Park (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Day_Forest_National_Park"},
            {"label": "Randa (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Randa,_Djibouti"},
            {"label": "Lista indicativa UNESCO · Yibuti (Parc National de la forêt du Day)", "url": "https://whc.unesco.org/en/statesparties/dj"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Day_Forest_National_Park_banner.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Day_Forest_National_Park_banner.jpg",
                "credit": "Singlab · CC BY-SA 3.0",
                "caption": "El bosque de Day, en el macizo del Goda.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Juniperus_procera_Djibouti.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Juniperus_procera_Djibouti.jpg",
                "credit": "Plantsman · CC BY 4.0",
                "caption": "Juniperus procera, el enebro africano del Day.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Airolaf_near_the_Day_Forest_National_Park.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Airolaf_near_the_Day_Forest_National_Park.jpg",
                "credit": "Skilla1st · CC BY-SA 4.0",
                "caption": "Airolaf, junto al parque.",
            },
        ],
    ),
    dict(
        n=8, name="Bankoualé y los oasis del Goda · palmeras y senderismo", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=11.8333333, lon=42.6666667,  # Google Maps: Bankouwale (pin aproximado del pueblo en el macizo del Goda)
        desc="Aldea a 640 metros en la vertiente del macizo de Goda, con huertos en terrazas regados por manantiales y el palmeral que da nombre a la palmera de Bankoualé (Livistona carinensis), una de las palmeras más raras del mundo. Es la base natural para caminar por los oasis y subir a la Forêt du Day. Aviso: los alojamientos son campamentos muy básicos y no hay ni gasolina ni cobertura fiable; se sube con todo resuelto desde Tadjoura.",
        dog_note="Aldea agrícola con huertos y ganado: el perro debe ir atado y no entrar en las parcelas ni en las balsas de riego.",
        visit={
            "why": "Es el único paisaje verde y habitado del país, y el punto de partida de las mejores caminatas de Yibuti.",
            "see": "Terrazas de hortalizas, acequias, palmeras Livistona, gargantas de la vertiente sur del Goda y aldeas afar de piedra.",
            "access": "Desde Randa por pista de montaña de tierra y piedra suelta, estrecha, con tramos de un solo vehículo: 4x4 obligatorio y mejor no cruzarse en horas punta. Aparcamiento improvisado a la entrada de la aldea. No hay entrada ni horario; se paga guía local de palabra. El pin marca el núcleo de Bankoualé.",
            "when": "Noviembre–marzo, caminando de amanecer. De junio a septiembre el interior supera los 45 °C; Bankoualé llega a 37 °C de media estival y no compensa.",
            "skip": "Si el grupo no piensa caminar: el interés está en los senderos, no en el pueblo.",
        },
        links=[
            {"label": "Bankouale (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bankouale"},
            {"label": "Goda Mountains · Walkopedia", "url": "https://www.walkopedia.net/best-world-walks/Djibouti/Goda-Mountains"},
            {"label": "Randa (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Randa,_Djibouti"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bankouale_2015_Village_Entrance.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bankouale_2015_Village_Entrance.jpg",
                "credit": "Albert Backer · CC BY-SA 4.0",
                "caption": "Entrada del pueblo de Bankoualé.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bankouale_2015_Mango_Trees.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bankouale_2015_Mango_Trees.jpg",
                "credit": "Albert Backer · CC BY-SA 4.0",
                "caption": "Huertos de mango regados por acequias.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Valley_in_the_Goda_Mountains.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Valley_in_the_Goda_Mountains.jpg",
                "credit": "Skilla1st · CC BY-SA 4.0",
                "caption": "Un valle del macizo del Goda.",
            },
        ],
    ),
    dict(
        n=9, name="Islas Musha y Maskali · el arrecife frente a la capital", cat="Costa", prio="Media",
        dog="prohibido", time="medio día",
        lat=11.7222978, lon=43.1904547,  # Google Maps: Isla Moucha
        desc="Isla coralina de unos 4 km² a 15 km de la capital, rodeada de los islotes Maskali y de un arrecife continuo: es la salida de snorkel más sencilla del país y se hace en medio día desde el puerto pesquero. Apenas viven 20 personas de forma permanente. Reino Unido la controló entre 1840 y 1887 antes de cederla a Francia. Ambos grupos figuran en la lista indicativa de la UNESCO desde 2015. No hay agua dulce ni sombra: llevarlo todo desde tierra.",
        dog_note="Se llega solo en barca de excursión y las islas son zona de anidamiento: los operadores no aceptan animales.",
        visit={
            "why": "Arrecife sano y aguas someras a un cuarto de hora de la capital, sin necesidad de organizar una expedición.",
            "see": "Corales, peces de arrecife, playas de arena blanca y, a veces, tortugas; el islote de Maskali al sureste.",
            "access": "Se contrata la barca en el puerto pesquero de Yibuti ciudad o a través de los centros de buceo; los 4x4 quedan aparcados en la capital. Las salidas de un día son habituales y no hay taquilla de isla. El pin marca Moucha; el objeto navegable en tierra es el puerto pesquero de la capital.",
            "when": "Noviembre–marzo, con mar más plano por la mañana. De junio a septiembre el calor es extremo (más de 45 °C en el interior; julio ronda los 40 °C en la isla).",
            "skip": "Con viento fuerte de mar: la travesía se vuelve incómoda y la visibilidad cae.",
        },
        links=[
            {"label": "Moucha Island (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Moucha_Island"},
            {"label": "Maskali Islands (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Maskali_Islands"},
            {"label": "Lista indicativa UNESCO · Yibuti (Îles Moucha et Maskali)", "url": "https://whc.unesco.org/en/statesparties/dj"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Plage_de_l'%C3%AEle_Moucha_avec_des_groupes_d'oiseaux_marins_le_long_de_la_mer_%C3%A9meraude,_Djibouti.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Plage_de_l'%C3%AEle_Moucha_avec_des_groupes_d'oiseaux_marins_le_long_de_la_mer_%C3%A9meraude,_Djibouti.jpg",
                "credit": "Anai171 · CC BY-SA 4.0",
                "caption": "Playa de la isla Moucha.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Groupe_d'oiseaux_marins_sur_la_plage_de_l'%C3%AEle_Moucha,_Djibouti.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Groupe_d'oiseaux_marins_sur_la_plage_de_l'%C3%AEle_Moucha,_Djibouti.jpg",
                "credit": "Anai171 · CC BY-SA 4.0",
                "caption": "Aves marinas en la orilla de Moucha.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Drome_ard%C3%A9ole_(Dromas_ardeola)_ou_Pluvier_crabier_sur_la_plage_de_l'%C3%AEle_Moucha,_Djibouti.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Drome_ard%C3%A9ole_(Dromas_ardeola)_ou_Pluvier_crabier_sur_la_plage_de_l'%C3%AEle_Moucha,_Djibouti.jpg",
                "credit": "Anai171 · CC BY-SA 4.0",
                "caption": "Dromas ardeola, el pluvial cangrejero, en Moucha.",
            },
        ],
    ),
    dict(
        n=10, name="Archipiélago de las Sept Frères · buceo en Bab el-Mandeb (Reserva de Biosfera UNESCO)", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=12.4674188, lon=43.3173933,  # Google Maps: Ras Siyyan (frente a las Sept Frères)
        desc="Seis islas volcánicas frente a la península de Ras Siyyan, en pleno estrecho de Bab el-Mandeb; el «séptimo hermano» no es una isla, sino el cono volcánico del extremo norte de Ras Siyyan. Es uno de los fondos más ricos del mar Rojo y, desde 2025, forma parte de la primera RESERVA DE BIOSFERA DE LA UNESCO del país. Aviso serio: el MAEC desaconseja expresamente el archipiélago por su proximidad a fronteras peligrosas, y las aguas de Bab el-Mandeb por piratería.",
        dog_note="Solo se llega en barco de varios días y son colonias de cría de charranes: acceso vetado a animales.",
        visit={
            "why": "Buceo de corriente en un estrecho por el que pasa el tráfico mundial, con arrecifes casi vírgenes.",
            "see": "Seis islas —Oeste (62 m), Doble (46 m), Baja (17 m), Grande (114 m), Este (83 m) y Sur (47 m)—, arrecifes y colonias de charranes.",
            "access": "Solo por mar, en crucero de buceo desde la capital o en barca desde Khor Angar/Obock; la isla Oeste queda a unos 4,5 km de Ras Siyyan. El pin de conducción es Ras Siyyan, final de pista al norte de Obock. ESTADO: zona desaconsejada por MAEC (fronteras peligrosas y piratería) y a menos de 16 km de la franja fronteriza eritrea que EE. UU. recomienda evitar. Comprobar el aviso vigente antes de contratar.",
            "when": "Noviembre–marzo por mar y temperatura. En julio la media ronda los 39 °C y de junio a septiembre el interior pasa de 45 °C.",
            "skip": "Descartarlo mientras sigan vigentes los avisos de piratería y frontera; no es un destino para improvisar.",
        },
        links=[
            {"label": "Seven Brothers Islands (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Seven_Brothers_Islands"},
            {"label": "Recomendaciones de viaje MAEC · Yibuti", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Yibuti"},
            {"label": "UNESCO · 26 nuevas reservas de biosfera (2025)", "url": "https://www.unesco.org/en/articles/26-new-biosphere-reserves-unescos-continues-unprecedented-expansion-its-global-network"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Seven_Brothers_Islands.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Seven_Brothers_Islands.jpg",
                "credit": "Skilla1st · CC BY-SA 3.0",
                "caption": "El archipiélago de las Sept Frères.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Seven_Brothers_(islands).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Seven_Brothers_(islands).jpg",
                "credit": "Skilla1st · CC BY-SA 3.0",
                "caption": "Las islas de las Siete Hermanas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bab-el-Mandeb_Seen_From_Midchannel_(cropped).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bab-el-Mandeb_Seen_From_Midchannel_(cropped).jpg",
                "credit": "Richard Weil · CC0",
                "caption": "El estrecho de Bab el-Mandeb desde el canal.",
            },
        ],
    ),
    dict(
        n=11, name="Ardoukôba · el volcán de 1978 y la falla del Rift", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="medio día",
        lat=11.6105556, lon=42.4758333,  # Google Maps: Ardoukoba
        desc="Volcán de fisura de 298 metros nacido en la ERUPCIÓN DEL 7 AL 14 DE NOVIEMBRE DE 1978, tras 3.000 años de reposo: doce millones de metros cúbicos de basalto fluido que corrieron hacia el Lac Assal y el Ghoubbet. La fisura sigue la dirección del Rift entre el bloque de Danakil y la depresión de Afar, y se camina por grietas abiertas donde África se está partiendo. La lava es cristal negro: botas rígidas y guantes, nada de chanclas.",
        dog_note="Lava cortante y roca negra que quema las almohadillas; no hay sombra ni agua en todo el campo de lava.",
        visit={
            "why": "Ver y pisar una falla tectónica activa que se abrió en vida de cualquier viajero adulto.",
            "see": "Cono de escorias, coladas negras de 1978, grietas del Rift y vistas al Ghoubbet y al Lac Assal desde el borde.",
            "access": "Está entre el Ghoubbet y el Lac Assal, junto a la RN-9 asfaltada; se deja el asfalto y se entra por pista corta de lava, dura pero practicable con 4x4 y buena distancia al suelo. Explanada sin problema para dos vehículos, sin taquilla ni horario. El pin marca el cono; el desvío no está señalizado, conviene track o guía.",
            "when": "Noviembre–marzo, de amanecer. De junio a septiembre el calor es extremo (más de 45 °C) y la roca negra multiplica la sensación térmica.",
            "skip": "A mediodía o en verano: el campo de lava es un horno sin salida rápida.",
        },
        links=[
            {"label": "Ardoukoba (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ardoukoba"},
            {"label": "Ghoubbet-el-Kharab (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ghoubbet-el-Kharab"},
            {"label": "Lake Assal (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Lake_Assal_(Djibouti)"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ardoukoba_Crater_Dec_2015.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ardoukoba_Crater_Dec_2015.jpg",
                "credit": "Albert Backer · CC BY-SA 4.0",
                "caption": "El cráter del Ardoukôba, nacido en 1978.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ardoukoba.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ardoukoba.jpg",
                "credit": "Rolfcosar · CC BY-SA 3.0",
                "caption": "Las coladas del Ardoukôba.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ardoukoba.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ardoukoba.JPG",
                "credit": "Autor desconocido · Public domain",
                "caption": "El volcán sobre la falla del Rift.",
            },
        ],
    ),
    dict(
        n=12, name="Khor Ambado y la Plage des Sables Blancs · las playas del golfo", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=11.5928279, lon=43.0196983,  # Google Maps: Plage Khor Ambado
        desc="Khor Ambado es la cala a la que escapa la capital: unos 20 kilómetros al oeste, se llega POR PISTA Y EN 4x4, cruzándose con nómadas y sus rebaños, y ofrece algo de sombra y buen snorkel. En la otra orilla del golfo, la Plage des Sables Blancs de Tadjoura es la playa de arena blanca del país, con un hotel-village a pie de agua. Aviso del MAEC: robos frecuentes en Doraleh y Khor Ambado al atardecer; no dejar nada en los vehículos ni quedarse de noche.",
        dog_note="Playas sin vigilancia ni chiringuito: el perro puede bajar, pero con sombra propia y sin dejarlo suelto entre los pescadores.",
        visit={
            "why": "Baño y snorkel sin salir del área metropolitana, y un cambio de ritmo entre dos etapas largas de pista.",
            "see": "Cala de grava y arena con arrecife bajo, acantilados bajos, pescadores y la silueta de la capital a lo lejos.",
            "access": "Pista de tierra desde la carretera de Doraleh, unos 20 km desde la capital; conviene 4x4 y llegar con luz. Aparcamiento libre sobre la playa, holgado para dos vehículos. Sin entrada ni horario. El pin marca la cala de Khor Ambado; la Plage des Sables Blancs está en la orilla norte, cerca de Tadjoura, y su coordenada exacta queda por confirmar.",
            "when": "Noviembre–marzo, por la mañana. De junio a septiembre el calor es extremo (más de 45 °C tierra adentro) y el agua pasa de 32 °C.",
            "skip": "Al atardecer y de noche: el MAEC señala robos frecuentes justo en esta playa.",
        },
        links=[
            {"label": "La plage de Khor Ambado · guía oficial de turismo", "url": "https://guide.visitdjibouti.dj/la-plage-de-khor-ambado/"},
            {"label": "Recomendaciones de viaje MAEC · Yibuti", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Yibuti"},
            {"label": "Hôtel Village Les Sables Blancs (Tadjoura)", "url": "https://www.sables-blancs-djibouti.com/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Khor_Ambado_beach,_Djibouti.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Khor_Ambado_beach,_Djibouti.jpg",
                "credit": "Nkm08pv7 · CC BY-SA 4.0",
                "caption": "La playa de Khor Ambado, también llamada Plage des Sables Blancs.",
            },
        ],
    ),
    dict(
        n=13, name="Grand Bara · el desierto llano y la carretera a Ali Sabieh", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=11.2346815, lon=42.6099723,  # Google Maps: Grand Bara
        desc="Antiguo fondo de lago convertido en una llanura de arena y arcilla de 103 km², tan plana y dura que la carretera que la cruza —40 kilómetros abiertos en 1981— parece una pista de aterrizaje. Es el escenario de la carrera anual GRAND BARA 15K. En julio y septiembre se inunda a tramos y brota hierba efímera. Advertencia: aunque tienta salirse a campo través, el llano es zona de maniobras militares y la orientación engaña; mejor no alejarse de la traza.",
        dog_note="Llanura abierta sin depredadores grandes, pero sin una sombra: solo parada corta y con el perro atado junto al vehículo.",
        visit={
            "why": "Es la conducción más limpia del país y la transición visual entre el Yibuti volcánico y el sedimentario.",
            "see": "Horizonte sin obstáculos, espejismos, dromedarios y campamentos afar dispersos; al fondo, las montañas rojas del sur.",
            "access": "Asfalto: la RN-1 sale de la capital y la carretera del Grand Bara la cruza de norte a sur hacia Ali Sabieh y Dikhil. Parar en el arcén es sencillo y hay sitio de sobra para dos 4x4. Sin entrada ni horario. El pin marca el centro de la llanura; conviene fijar el punto de parada por GPS porque no hay referencias.",
            "when": "Noviembre–marzo, con luz rasante de mañana o tarde. De junio a septiembre el calor es extremo (más de 45 °C) y sin sombra alguna.",
            "skip": "Tras lluvias fuertes: la arcilla se encharca y el llano se vuelve trampa.",
        },
        links=[
            {"label": "Grand Bara (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Grand_Bara"},
            {"label": "RN-1 (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/National_Highway_1_(Djibouti)"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/GrandBaraDesert.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:GrandBaraDesert.JPG",
                "credit": "Skilla1st · CC BY-SA 3.0",
                "caption": "El llano del Grand Bara.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/A_U.S._Air_Force_HC-130J_Combat_King_II_assigned_to_the_81st_Expeditionary_Rescue_Squadron_lands_on_an_unprepared_landing_zone_at_Grand_Bara,_Djibouti.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:A_U.S._Air_Force_HC-130J_Combat_King_II_assigned_to_the_81st_Expeditionary_Rescue_Squadron_lands_on_an_unprepared_landing_zone_at_Grand_Bara,_Djibouti.jpg",
                "credit": "Tech. Sgt. Dhruv Gopinath · Public domain",
                "caption": "El Grand Bara se usa como pista de aterrizaje improvisada.",
            },
        ],
    ),
    dict(
        n=14, name="Ali Sabieh · la ciudad de las montañas rojas y el ferrocarril", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=11.1542936, lon=42.7069057,  # Google Maps: Ali Sabieh
        desc="Segunda ciudad del país con 44.782 habitantes (censo de 2024), encajada a 756 metros entre cerros de arenisca rojiza y a solo 10 kilómetros de Etiopía. EL TREN LLEGÓ EL 14 DE JULIO DE 1900 y la vieja estación sigue en pie aunque la línea métrica está abandonada; la nueva línea eléctrica a Adís Abeba pasa cerca desde 2016. Sobre el pueblo, la montaña con el emblema nacional tallado. Zona fronteriza: llevar pasaporte y eVisa a mano en los controles.",
        dog_note="Ciudad tranquila y más fresca por la altura; atado en el centro y fuera del mercado.",
        visit={
            "why": "Es la única ciudad de montaña del sur, con el contraste de la arenisca roja y dos generaciones de ferrocarril.",
            "see": "Estación histórica de 1900, montaña del emblema nacional (801 m) sobre la ciudad, mercado somalí y los montes Arrei.",
            "access": "Asfalto: RN-5 desde Balbala, 85 km, pasando por Holhol, Danan y Ali Adde; también RN-1 y desvío. Aparcamiento fácil. La estación histórica se visita de palabra, sin taquilla ni horario. El pin marca la ciudad; el objeto navegable es la estación.",
            "when": "Noviembre–marzo; las mínimas invernales bajan a 15–16 °C y se agradecen. De junio a septiembre el interior supera los 45 °C (aquí 32–37 °C de media de máximas).",
            "skip": "Si no interesa el ferrocarril ni se va a subir a la montaña del emblema, es solo una parada de repostaje.",
        },
        links=[
            {"label": "Ali Sabieh (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ali_Sabieh"},
            {"label": "Ali Sabieh Mountain (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ali_Sabieh_Mountain"},
            {"label": "RN-5 (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/National_Highway_5_(Djibouti)"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/View_of_Ali_Sabieh.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:View_of_Ali_Sabieh.JPG",
                "credit": "Skilla1st · CC BY-SA 4.0",
                "caption": "Ali Sabieh en 2015.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Arrei_Mountains_see_from_Ali_Sabieh.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Arrei_Mountains_see_from_Ali_Sabieh.JPG",
                "credit": "Skilla1st · CC BY-SA 4.0",
                "caption": "Los montes Arrei desde Ali Sabieh.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ali_Sabieh.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ali_Sabieh.jpg",
                "credit": "SupaDane · Public domain",
                "caption": "Ali Sabieh desde una loma al sur.",
            },
        ],
    ),
    dict(
        n=15, name="Dikhil y el Petit Bara · la puerta del Lac Abbé", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=11.1054336, lon=42.3704744,  # Google Maps: Dikhil
        desc="Cabecera del suroeste, 27.378 habitantes (censo de 2024) sobre un espolón de los montes Okarre a 507 metros. Es LA ÚLTIMA GASOLINERA Y EL ÚLTIMO MERCADO antes del Lac Abbé, a 122 kilómetros de la capital por la RN-1 (unas 3 h en autobús). El Petit Bara se extiende al este, gemelo pequeño del Grand Bara. Los propios yibutianos suben aquí en verano por el clima; aun así, en julio las mínimas nocturnas rondan los 28 °C.",
        dog_note="Pueblo de paso sin restricciones conocidas; atado y a la sombra, y nunca suelto en el llano del Petit Bara.",
        visit={
            "why": "Parada obligada de logística y avituallamiento antes de la pista del Lac Abbé, con un llano fósil al lado.",
            "see": "Mercado de Dikhil, meseta de los Okarre, llanura del Petit Bara y caravanas de sal camino de Etiopía.",
            "access": "RN-1 asfaltada desde la capital, 122 km; desde aquí arranca la pista hacia el Lac Abbé. Aparcamiento libre en el pueblo. A 12 km de la frontera etíope: habrá control de documentación. El pin marca el centro de Dikhil.",
            "when": "Noviembre–marzo. De junio a septiembre el interior supera los 45 °C; incluso aquí, con el «clima sano» que le atribuyen, las noches de verano no bajan de 28 °C.",
            "skip": "Si no se va al Lac Abbé: el pueblo en sí no justifica el desvío.",
        },
        links=[
            {"label": "Dikhil (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Dikhil"},
            {"label": "RN-1 (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/National_Highway_1_(Djibouti)"},
            {"label": "Grand Bara (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Grand_Bara"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Porte_de_Dikhil.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Porte_de_Dikhil.JPG",
                "credit": "Cjulien21 · CC BY-SA 3.0",
                "caption": "La puerta de entrada de Dikhil.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Dikhil_2015.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Dikhil_2015.jpg",
                "credit": "Albert Backer · CC BY-SA 4.0",
                "caption": "Dikhil, sobre la RN1.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/View_approaching_Dikhil,_Djibouti_from_RN1_-_Mapillary_(382278977102494).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:View_approaching_Dikhil,_Djibouti_from_RN1_-_Mapillary_(382278977102494).jpg",
                "credit": "muda @ Mapillary · CC BY-SA 4.0",
                "caption": "Llegada a Dikhil por la RN1.",
            },
        ],
    ),
    dict(
        n=16, name="Puerto de Doraleh y las bases militares · el Yibuti geoestratégico", cat="Ciudad · servicios", prio="Media",
        dog="prohibido", time="medio día",
        lat=11.5938528, lon=43.1056507,  # Google Maps: Port de Doraleh
        desc="Cinco potencias tienen base militar en este país de 23.200 km²: Francia desde 1957 (BA 188), Estados Unidos en Camp Lemonnier desde 2001, Japón desde 2011 —su única base en el extranjero—, Italia desde 2013 y China desde 2017, junto al puerto de Doraleh. Los alquileres suman unos 300 millones de dólares al año, en torno al 10 % del PIB. Por el puerto pasa el 70 % de la carga con destino u origen en Etiopía. PROHIBIDO FOTOGRAFIAR puerto, aeropuerto y cualquier instalación militar.",
        dog_note="Zona portuaria y militar de acceso restringido: ni personas ni animales entran sin autorización.",
        visit={
            "why": "Entender de un vistazo por qué existe Yibuti como Estado: es el peaje del estrecho de Bab el-Mandeb.",
            "see": "Terminal de contenedores de Doraleh, tráfico de portacontenedores, convoyes militares y el perímetro de Camp Lemonnier junto al aeropuerto de Ambouli.",
            "access": "Doraleh queda 5 km al oeste de la ciudad, por asfalto. NO se entra: el recinto portuario y las bases son zona restringida y no hay visita turística. Se ve desde la carretera costera y desde la RN-1. El pin marca el puerto de Yibuti, con Doraleh justo al oeste. No sacar la cámara ni el móvil cerca de garitas o convoyes: hay multas, confiscación, detención y expulsión.",
            "when": "Todo el año, de paso; de junio a septiembre el calor es extremo (más de 45 °C en el interior) y no hay motivo para demorarse.",
            "skip": "Descartarlo si el grupo no puede resistirse a fotografiar: el riesgo legal no compensa.",
        },
        links=[
            {"label": "Foreign military bases in Djibouti (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Foreign_military_bases_in_Djibouti"},
            {"label": "Port of Djibouti (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Port_of_Djibouti"},
            {"label": "Camp Lemonnier (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Camp_Lemonnier"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_container_terminal_at_the_Port_of_Djibouti.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_container_terminal_at_the_Port_of_Djibouti.jpg",
                "credit": "Skilla1st · CC BY-SA 4.0",
                "caption": "La terminal de contenedores del puerto de Yibuti.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Djibouti_Port.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Djibouti_Port.JPG",
                "credit": "CharlesFred · CC BY-SA 3.0",
                "caption": "Barca de pesca frente a los contenedores.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/May_18_-_180510-N-FD185-8029_(42187958511).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:May_18_-_180510-N-FD185-8029_(42187958511).jpg",
                "credit": "U.S. Naval Forces Europe-Africa · Public domain",
                "caption": "La terminal de Doraleh.",
            },
        ],
    ),
    dict(
        n=17, name="Ferrocarril Adís Abeba–Yibuti · la estación de Nagad", cat="Cultura", prio="Media",
        dog="por confirmar", time="medio día",
        lat=11.5235251, lon=43.1282094,  # Google Maps: Gare de Nagad
        desc="La estación de Nagad, junto al aeropuerto de Ambouli, es la cabecera yibutiana del primer FERROCARRIL ELECTRIFICADO TRANSFRONTERIZO DE ÁFRICA: 759 kilómetros hasta Adís Abeba, 93 de ellos en Yibuti, con catenaria de 25 kV y trenes de pasajeros a 120 km/h. Se inauguró el 5 de octubre de 2016 en Etiopía y el 10 de enero de 2017 en Yibuti, con explotación comercial desde 2018. Sustituyó a la vieja línea métrica de 1900. La regularidad del servicio de pasajeros ha sido irregular: confirmar horarios en taquilla.",
        dog_note="No consta la política de la compañía sobre animales a bordo; hay que preguntar en la estación.",
        visit={
            "why": "Es la infraestructura que explica el país y una alternativa real para dejar los coches y cruzar a Etiopía en tren.",
            "see": "Andenes y locomotoras eléctricas de Nagad, el tramo diésel hacia Doraleh y, en el sur, el viaducto de 1900 en Holhol (29 m de alto y 45 de largo).",
            "access": "Asfalto hasta Nagad, al sur de la capital y junto al aeropuerto. Hay aparcamiento. Horarios y billetes solo en taquilla; el servicio de pasajeros ha sufrido interrupciones. El pin marca la estación de Nagad. OJO: fotografiar estaciones y trenes cerca de zona militar puede interpretarse mal; es zona de aeropuerto.",
            "when": "Todo el año; noviembre–marzo para cualquier plan combinado. De junio a septiembre el interior pasa de 45 °C y el trayecto a Etiopía se hace duro.",
            "skip": "Si no se va a montar en el tren: la estación en sí tiene poco que ver.",
        },
        links=[
            {"label": "Addis Ababa–Djibouti Railway (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Addis_Ababa%E2%80%93Djibouti_Railway"},
            {"label": "Nagad railway station (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Nagad_railway_station"},
            {"label": "Holhol y su viaducto de 1900 (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Holhol"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/R%C3%A9publique_de_Djibouti_-_gare_ferroviaire_de_Djibouti_(M%C3%A9diHAL_617651).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:R%C3%A9publique_de_Djibouti_-_gare_ferroviaire_de_Djibouti_(M%C3%A9diHAL_617651).jpg",
                "credit": "Stéphane Pouyllau · CC BY-SA 4.0",
                "caption": "La vieja estación del ferrocarril franco-etíope en Yibuti.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_Addis_Ababa%E2%80%93Djibouti_Railway,_near_Dasbiyo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_Addis_Ababa%E2%80%93Djibouti_Railway,_near_Dasbiyo.jpg",
                "credit": "Skilla1st · CC BY-SA 4.0",
                "caption": "La línea nueva Adís Abeba–Yibuti cerca de Dasbiyo.",
            },
        ],
    ),
    dict(
        n=18, name="Loyada · la frontera con Somalilandia", cat="Ciudad · servicios", prio="Media",
        dog="por confirmar", time="medio día",
        lat=11.4615657, lon=43.2500923,  # Google Maps: Loyada
        desc="Aldea costera a 25 kilómetros de la capital y ÚNICO PASO FRONTERIZO OFICIAL entre Yibuti y Somalilandia. Su nombre viene del afar «abrevadero blanco». Aquí terminó en 1976 el secuestro del autobús escolar francés: 31 niños retenidos, dos muertos y cinco heridos en el asalto del día siguiente. La frontera se ha cerrado por motivos políticos en varias ocasiones desde 1999 y volvió a abrir en 2002. El eVisa yibutiano sirve para entrada terrestre, pero conviene llevarlo impreso.",
        dog_note="No hay información sobre el trámite de un animal en este paso; conviene consultar antes con los servicios veterinarios de ambos lados.",
        visit={
            "why": "Es el punto de salida hacia Somalilandia y un buen sitio para entender la geografía de clanes de la región.",
            "see": "Puesto fronterizo, palmerales y playa; poco más: son 1.367 habitantes.",
            "access": "Asfalto desde la capital, 25 km. Trámite lento y con control minucioso; se necesita eVisa (tránsito 12 USD de 1 a 14 días, corta estancia 23 USD de 15 a 90 días) tramitado en evisa.gouv.dj, válido también en fronteras terrestres; el visado a la llegada solo se contempla para pasaportes diplomáticos, oficiales y de servicio. El pin marca la localidad; el objeto navegable es el puesto fronterizo. Prohibido fotografiar el paso.",
            "when": "Noviembre–marzo y a primera hora, cuando el puesto está menos saturado. De junio a septiembre el calor es extremo (más de 45 °C en el interior; aquí, 36 °C de media en julio).",
            "skip": "Si no se va a cruzar a Somalilandia, no hay razón para acercarse a un puesto fronterizo.",
        },
        links=[
            {"label": "Loyada (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Loyada"},
            {"label": "Política de visados de Yibuti (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Visa_policy_of_Djibouti"},
            {"label": "Recomendaciones de viaje MAEC · Yibuti", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Yibuti"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/19760203_PV_P32-PHOTO_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:19760203_PV_P32-PHOTO_01.jpg",
                "credit": "Paulu Francescu · CC BY-SA 4.0",
                "caption": "Vista aérea de la frontera de Loyada en 1976.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Djibouti_entry_stamp.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Djibouti_entry_stamp.jpg",
                "credit": "Ayaanle · CC BY-SA 4.0",
                "caption": "Sello de entrada por el paso de Loyada.",
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
    ("Paso fronterizo de Galafi (Etiopía → Yibuti)", "Frontera", 11.7168693, 41.8376077,  # Google Maps: Galafi
     "Paso terrestre principal desde Etiopía, en la RN-1, a 218 km de la capital y a 161 m de altitud. Es donde los overlanders obtienen el permiso temporal de importación del vehículo (10 días documentados). Tráfico intensísimo de camiones y carretera en mal estado. Pin comprobado en Google Maps («Galafi»)."),
    ("Paso fronterizo de Loyada (Yibuti → Somalilandia)", "Frontera", 11.4615657, 43.2500923,  # Google Maps: Loyada
     "Único paso oficial hacia Somalilandia, a 25 km de Yibuti ciudad, sobre una colina que domina la costa del golfo de Adén. Cierres periódicos por motivos políticos; reabierto en 2002. El MAEC desaconseja la zona fronteriza con Somalia (Somalilandia). Pin comprobado en Google Maps («Loyada»)."),
    ("Ali Sabieh / paso de Dewele (Etiopía → Yibuti)", "Frontera", 11.0331799, 42.6316246,  # Google Maps: Dewele (lado etíope del paso de Ali Sabieh)
     "Segunda ciudad del país (44.782 hab. en 2024), a 98 km de la capital, 756 m de altitud y 10 km de la frontera etíope; el paso de Dewele está a 18 km. Por aquí cruza el ferrocarril Adís Abeba-Yibuti y se hace el control fronterizo ferroviario. Pin comprobado en Google Maps («Dewele (lado etíope del paso de Ali Sabieh)»)."),
    ("Aeropuerto Internacional de Yibuti-Ambouli (JIB/HDAM)", "Frontera", 11.5520514, 43.14968,  # Google Maps: Aeropuerto Internacional Yibuti-Ambouli
     "Único aeropuerto internacional del país, a 6 km del centro y 15 m de altitud, con una sola pista (09/27). Uso civil y militar compartido: Camp Lemonnier estadounidense, base aérea francesa BA 188, base japonesa e italiana; el tráfico militar supone en torno al 75% de las operaciones. Visado a la llegada discrecional. PROHIBIDO FOTOGRAFIAR. Pin comprobado en Google Maps («Aeropuerto Internacional Yibuti-Ambouli»)."),
    ("Puerto de Yibuti", "Frontera", 11.6053, 43.1392,  # Google Maps: Puerto de Yibuti (sin objeto en Google Maps; coordenada de la fuente)
     "Entrada marítima principal y salida al mar de Etiopía, que supone en torno al 70% de la carga; unos 2.500 buques al año. Terminal de contenedores desde febrero de 1985 y ampliación en Doraleh. PROHIBIDO FOTOGRAFIAR. Pin comprobado en Google Maps («Puerto de Yibuti (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Embarcadero del ferry Yibuti–Tadjoura–Obock (Port de l'Escale)", "Frontera", 11.5951, 43.1481,  # Google Maps: Port de l'Escale (sin objeto en Google Maps; coordenada de la fuente)
     "Port de l'Escale, Route de Venise, al final del muelle que sale del palacio presidencial. Travesía del golfo de Tadjoura de unas 2 horas; ADMITE VEHÍCULOS, con hasta 1 hora de espera para asegurar plaza (reseña de viajero, mayo de 2019). Horarios y tarifas actuales por confirmar. Pin comprobado en Google Maps («Port de l'Escale (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Embajada de España en Adís Abeba (competente para Yibuti)", "Consular", 9.0620982, 38.7603164,  # Google Maps: Embassy of Spain (Adís Abeba, competente para Yibuti)
     "España NO tiene embajada residente en Yibuti: la competencia es de la Embajada en Adís Abeba, que en su web declara «También somos tu Embajada en Seychelles y Yibuti». Dirección: Botswana Street, Addis Abeba, P.O. Box 2312. Tel. +251 929 136 159 y +251 111 230 083. emb.addisabeba@maec.es. EMERGENCIA CONSULAR 24 h: +251 911 219 403. Pin comprobado en Google Maps («Embassy of Spain (Adís Abeba, competente para Yibuti)»)."),
    ("Viceconsulado Honorario de España en Yibuti", "Consular", 11.5885948, 43.1453647,  # Google Maps: Yibuti ciudad (el viceconsulado honorario no publica dirección ni figura en Google Maps)
     "Vicecónsul honoraria: Josefina Llorente Martín. Teléfonos publicados por el MAEC: +253 77 84 49 50 (recomendaciones de viaje) y +253 21 35 63 53 (ficha país). DIRECCIÓN EXACTA NO PUBLICADA: por confirmar con la embajada en Adís Abeba. Pin comprobado en Google Maps («Yibuti ciudad (el viceconsulado honorario no publica dirección ni figura en Google Maps)»)."),
    ("Hôpital Général Peltier (Yibuti ciudad)", "Hospital", 11.6083024, 43.1531881,  # Google Maps: Hopital Peltier
     "Principal hospital público del país y referencia de la lista de centros médicos de la embajada británica. BP 2123, Yibuti. Tel. +253 21 35 27 12, fax 21 35 30 14. El MAEC califica los servicios médicos del país de «muy deficientes». Pin comprobado en Google Maps («Hopital Peltier»)."),
    ("Hôpital Militaire Bouffard y Clinique Affi (Yibuti ciudad)", "Hospital", 11.5874786, 43.1527932,  # Google Maps: Hopital Bouffard
     "Hospital militar francés Bouffard (BP 85024, tel. +253 21 35 13 51), referencia habitual para europeos en urgencias graves; el acceso de civiles queda a criterio militar, por confirmar. Alternativa privada: Clinique Affi (BP 6193, tel. +253 21 34 44 97). Datos de la lista de la embajada británica de septiembre de 2015: reconfirmar teléfonos. Pin comprobado en Google Maps («Hopital Bouffard»)."),
    ("Repostaje en Yibuti ciudad antes del circuito interior", "Combustible", 11.5597724, 43.1522574,  # Google Maps: Total Station (Yibuti ciudad)
     "La red de estaciones se concentra en la capital y en el eje de la RN-1 hacia Galafi. Canadá avisa de que las gasolineras son escasas y están muy separadas. Gasolina en torno a 310 DJF/litro (1,50 €) a 18 de septiembre de 2026. Salir con depósito lleno y bidones para el triángulo Lac Assal – Grand Bara – Lac Abbé. Pago en efectivo, en francos. Pin comprobado en Google Maps («Total Station (Yibuti ciudad)»)."),
    ("Dikhil: último repostaje antes de Galafi y del Lac Abbé", "Combustible", 11.1054336, 42.3704744,  # Google Maps: Dikhil
     "Capital de la región de Dikhil (27.378 hab. en 2024, 507 m de altitud), a 122 km al suroeste de la capital por la RN-1 y 12 km de la frontera etíope, al este del Lac Abbé. Última población de entidad antes de Galafi y del desierto: última oportunidad razonable de repostar y comprar agua. Servicios concretos POR CONFIRMAR. Pin comprobado en Google Maps («Dikhil»)."),
    ("Carga de agua en Yibuti ciudad", "Agua potable", 11.5885948, 43.1453647,  # Google Maps: Yibuti (ciudad)
     "El agua del grifo NO es potable (riesgo de cólera según el MAEC), pero la red de la capital sirve para llenar depósitos de ducha y lavado. Para beber, embotellada o filtrada: botella de 1,5 l en torno a 100 DJF (0,49 €) a 18 de septiembre de 2026. Es el único punto fiable de carga del país: fuera de la capital la red es escasa y el agua salobre. Pin comprobado en Google Maps («Yibuti (ciudad)»)."),
]

DRONE_CALLOUT = ("danger", "El dron se queda en casa",
                 "El MAEC lo dice sin rodeos: «Se recomienda encarecidamente no venir al territorio de Yibuti en posesión de un dron de recreo ya que puede ser requisado». No hay normativa civil publicada —la Direction de l'Aviation Civile et de la Météorologie no ha emitido reglas de uso— pero sí hay cinco ejércitos extranjeros, un aeropuerto civil y militar compartido y una prohibición general de fotografiar puertos, aeropuertos, puentes, edificios públicos e instalaciones militares. Volar aquí es pedir la confiscación del equipo y, potencialmente, una detención. No compensa.")

STARLINK_CALLOUT = ("warn", "Starlink no funciona en Yibuti",
                    "Yibuti no está entre los mercados activos de Starlink: figura como «planificado, sin fecha comprometida», y el análisis mundial de mayo de 2026 sitúa a todo el Cuerno de África —Yibuti, Etiopía, Eritrea, Sudán— en el grupo de países donde la aprobación regulatoria está estancada. Somalia es la única excepción de la zona, con servicio activo. Encender un terminal sin licencia en un país con cinco bases militares extranjeras y un operador estatal en monopolio no compensa: hay que planificar el viaje asumiendo conexión solo por SIM local y solo en la capital y los ejes principales.")

DOG_MATRIX = [
    ("Entrada al país desde Etiopía (Galafi, Dewele)", "por confirmar", "Gestionar el permiso de importación por escrito con el ministerio yibutiano (maepe-rh.dj) antes de salir de España y llevar copia impresa en francés. Si no hay respuesta, plantear el viaje sin perro o dejarlo en custodia en Adís Abeba."),
    ("Yibuti ciudad, hoteles y comercios", "permitido con condiciones", "País musulmán: el perro no entra en restaurantes ni comercios y su presencia incomoda. Reservar alojamiento con aparcamiento a la sombra y confirmar por escrito que aceptan animal antes de llegar."),
    ("Lac Assal, Grand Bara y Lac Abbé de junio a septiembre", "no recomendado", "Por encima de 45 °C: inviable para el animal, y el relato de una visita al Lac Abbé habla de 9 horas de conducción con 42 °C. Reprogramar a noviembre-febrero; si aun así se va, recorrido solo al amanecer y al anochecer y perro en el vehículo con motor y aire acondicionado en marcha."),
    ("Zonas minadas de Obock y Tadjoura", "prohibido", "Perro siempre atado y nunca fuera del asfalto: el MAEC confirma minas sin desactivar y Canadá añade munición sin explotar. Sustituir por tramos transitados de la costa de Tadjoura."),
    ("Excursión de tiburón ballena y barcos del golfo", "por confirmar", "Ningún operador publica política de animales. Dejar al perro en el alojamiento con aire acondicionado y turnos entre los tres viajeros; en ningún caso en el coche parado."),
    ("Regreso a la UE (por avión o por Etiopía)", "permitido con condiciones", "Solo si la titulación antirrábica se hizo en la UE antes de salir, con 30 días tras la vacuna y 90 días de espera, y está anotada en el pasaporte. Sin ella, la reentrada no es posible sin regularización y habría que resolverla desde un país listado en el Reglamento 2026/636."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Yibuti (Ministerio de Asuntos Exteriores, UE y Cooperación; actualizado el 6 de mayo de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Yibuti"),
    ("MAEC · Ficha País Yibuti (PDF, Oficina de Información Diplomática; datos de 2024-2025)", "https://www.exteriores.gob.es/Documents/FichasPais/YIBUTI_FICHA%20PAIS.pdf"),
    ("Embajada de España en Adís Abeba (MAEC) — «También somos tu Embajada en Seychelles y Yibuti»", "https://www.exteriores.gob.es/Embajadas/addisabeba/es/Embajada/Paginas/index.aspx"),
    ("FCDO · Djibouti travel advice — Safety and security (Gobierno del Reino Unido, 2026)", "https://www.gov.uk/foreign-travel-advice/djibouti/safety-and-security"),
    ("FCDO · Djibouti travel advice — Entry requirements (Gobierno del Reino Unido, 2026)", "https://www.gov.uk/foreign-travel-advice/djibouti/entry-requirements"),
    ("FCDO · Djibouti travel advice — Warnings and insurance (Gobierno del Reino Unido; actualizado el 27 de julio de 2026)", "https://www.gov.uk/foreign-travel-advice/djibouti/warnings-and-insurance"),
    ("Gobierno de Canadá · Djibouti travel advice and advisories (2026)", "https://travel.gc.ca/destinations/djibouti"),
    ("TravelHealthPro · Djibouti (National Travel Health Network and Centre, Reino Unido, 2026)", "https://travelhealthpro.org.uk/country/65/djibouti"),
    ("Portail officiel eVisa de la République de Djibouti (sitio oficial; contenido dinámico, no legible por WebFetch)", "https://www.evisa.gouv.dj/"),
    ("Wikipedia · Visa policy of Djibouti (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Visa_policy_of_Djibouti"),
    ("Wikipedia · Djibouti (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Djibouti"),
    ("Wikipedia · Djibouti–Ethiopia border (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Djibouti%E2%80%93Ethiopia_border"),
    ("Wikipedia · Galafi (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Galafi"),
    ("Wikipedia · Loyada (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Loyada"),
    ("Wikipedia · Ali Sabieh (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Ali_Sabieh"),
    ("Wikipedia · Dikhil (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Dikhil"),
    ("Wikipedia · Djibouti–Ambouli International Airport (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Djibouti%E2%80%93Ambouli_International_Airport"),
    ("Wikipedia · Port of Djibouti (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Port_of_Djibouti"),
    ("Wikipedia · Addis Ababa–Djibouti Railway (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Addis_Ababa%E2%80%93Djibouti_Railway"),
    ("carnetdepassage.org · Djibouti (AIT/FIA; consultado en septiembre de 2026)", "https://www.carnetdepassage.org/country/djibouti"),
    ("Horizons Unlimited · Carnet de Passages en Douanes, list of countries (actualización de 2023)", "https://www.horizonsunlimited.com/node/2399"),
    ("COMESA Yellow Card · Yellow Card Overview (países emisores y aceptantes, incluido Yibuti)", "https://comesayellowcard.com/yellow-card-overview"),
    ("The Road Chose Me · «Into Djibouti», Dan Grec (entrada por Galafi con vehículo propio, permiso temporal de 10 días)", "https://theroadchoseme.com/into-djibouti"),
    ("Tripadvisor · Foro de Yibuti, «Can I enter Djibouti by land with eVisa?» (2022-2024)", "https://www.tripadvisor.com/ShowTopic-g293787-i10051-k14687786-Can_i_enter_Djibouti_by_land_with_eVisa-Djibouti.html"),
    ("Travel2Djibouti · How to Enter Djibouti: Visa and Borders, Air, Land and Sea Guide", "https://www.travel2djibouti.com/how-to-entry-djibouti-guide/"),
    ("Travel2Djibouti · Whale Shark Season in Djibouti: Best Time to Visit", "https://www.travel2djibouti.com/whale-shark-season-in-djibouti/"),
    ("Wandersmiles · Trekking the Salt Plains of Lake Assal, Djibouti", "https://www.wandersmiles.com/trekking-salt-plains-lake-assal-djibouti/"),
    ("Wandersmiles · Swimming with Whale Sharks in Djibouti", "https://www.wandersmiles.com/swimming-whale-sharks-djibouti/"),
    ("Monsoon Diaries · «Take a Chance… on Lake Abbe» (15 de mayo de 2023)", "https://monsoondiaries.com/2023/05/15/abbe/"),
    ("Madventure · Horn of Africa Overland, 39 días (edición de 24 de julio a 1 de septiembre de 2024)", "https://madventure.co.uk/horn-of-africa-overland/"),
    ("Petit Futé · Ferry Tadjourah-Obock, Djibouti (reseña de viajero de mayo de 2019)", "https://www.petitfute.com/v51482-djibouti/c1173-visites-points-d-interet/c1157-visites-guidees/c986-sur-l-eau/384445-ferry-tadjourah-obock.html"),
    ("Drone Laws · Djibouti (actualizado el 14 de enero de 2026; autoridad ACAM, +253 340 151)", "https://drone-laws.com/drone-laws-in-djibouti/"),
    ("Tech.africa · Starlink in Africa: countries, prices and speeds (2026)", "https://tech.africa/starlink-africa/"),
    ("Mappr · Mapped: Where Starlink Is Available Around the World (10 de mayo de 2026)", "https://www.mappr.co/starlink-availability-by-country/"),
    ("Traveltomtom · Prepaid SIM Card & eSIM for Djibouti (Djibouti Telecom en monopolio; guía de agosto de 2021)", "https://www.traveltomtom.net/destinations/africa/djibouti/sim-card-djibouti"),
    ("Ministère de l'Agriculture, de l'Eau, de la Pêche, de l'Élevage et des Ressources Halieutiques de la République de Djibouti (portal oficial; sin apartado de importación de animales)", "https://www.maepe-rh.dj/"),
    ("USDA APHIS · Export Live Animals to Djibouti (servicio veterinario oficial de EE. UU., 2026)", "https://www.aphis.usda.gov/live-animal-export/export-live-animals-djibouti"),
    ("EUR-Lex · Reglamento de Ejecución (UE) 2026/636, listas de terceros países para desplazamientos sin ánimo comercial de animales de compañía (aplicable desde el 22 de abril de 2026)", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600636&qid=1776938175276"),
    ("EUR-Lex · Reglamento Delegado (UE) 2026/131, de 20 de enero de 2026, por el que se completa el Reglamento (UE) 2016/429 en requisitos zoosanitarios para desplazamientos sin fines comerciales de animales de compañía (aplicable desde el 28 de marzo de 2026)", "https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=CELEX%3A32026R0131"),
    ("MAPA · Viajar con la mascota: perros, gatos y hurones (Ministerio de Agricultura, Pesca y Alimentación; plazos de titulación antirrábica y PEV)", "https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones"),
    ("Embajada británica en Yibuti · List of Medical Facilities/Practitioners in Djibouti (PDF, septiembre de 2015)", "https://assets.publishing.service.gov.uk/media/5a7f588d40f0b62305b86953/Djibouti_-_List_of_Medical_Facilities_September_2015.pdf"),
    ("HikersBay · Precios en Yibuti, junio-septiembre de 2026 (combustible y agua embotellada; dato de 18 de septiembre de 2026)", "https://hikersbay.com/prices/djibouti/p/djibouti?lang=fr"),
    ("Djibouti City (Wikipedia EN)", "https://en.wikipedia.org/wiki/Djibouti_City"),
    ("Mezquita Hamoudi (Wikipedia EN)", "https://en.wikipedia.org/wiki/Hamoudi_Mosque"),
    ("Guía oficial · Agence Nationale du Tourisme de Djibouti", "https://guide.visitdjibouti.dj/"),
    ("Lake Assal (Wikipedia EN)", "https://en.wikipedia.org/wiki/Lake_Assal_(Djibouti)"),
    ("Lago Assal (Wikipedia ES)", "https://es.wikipedia.org/wiki/Lago_Assal"),
    ("Lista indicativa UNESCO · Yibuti", "https://whc.unesco.org/en/statesparties/dj"),
    ("Lake Abbe (Wikipedia EN)", "https://en.wikipedia.org/wiki/Lake_Abbe"),
    ("Crónica de viaje · Atlas & Boots", "https://www.atlasandboots.com/travel-blog/lac-abbe-in-djibouti/"),
    ("Gulf of Tadjoura (Wikipedia EN)", "https://en.wikipedia.org/wiki/Gulf_of_Tadjoura"),
    ("Dolphin Excursions Djibouti · temporada de tiburón ballena", "https://www.divedjibouti.com/whalesharks"),
    ("Ghoubbet-el-Kharab (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ghoubbet-el-Kharab"),
    ("Tadjoura (Wikipedia EN)", "https://en.wikipedia.org/wiki/Tadjoura"),
    ("RN-9 (Wikipedia EN)", "https://en.wikipedia.org/wiki/National_Highway_9_(Djibouti)"),
    ("Tadjoura · Wikitravel", "https://wikitravel.org/en/Tadjoura"),
    ("Obock (Wikipedia EN)", "https://en.wikipedia.org/wiki/Obock"),
    ("US Travel Advisory · Djibouti", "https://travel.state.gov/en/international-travel/travel-advisories/djibouti.html"),
    ("Day Forest National Park (Wikipedia EN)", "https://en.wikipedia.org/wiki/Day_Forest_National_Park"),
    ("Randa (Wikipedia EN)", "https://en.wikipedia.org/wiki/Randa,_Djibouti"),
    ("Bankouale (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bankouale"),
    ("Goda Mountains · Walkopedia", "https://www.walkopedia.net/best-world-walks/Djibouti/Goda-Mountains"),
    ("Moucha Island (Wikipedia EN)", "https://en.wikipedia.org/wiki/Moucha_Island"),
    ("Maskali Islands (Wikipedia EN)", "https://en.wikipedia.org/wiki/Maskali_Islands"),
    ("Seven Brothers Islands (Wikipedia EN)", "https://en.wikipedia.org/wiki/Seven_Brothers_Islands"),
    ("UNESCO · 26 nuevas reservas de biosfera (2025)", "https://www.unesco.org/en/articles/26-new-biosphere-reserves-unescos-continues-unprecedented-expansion-its-global-network"),
    ("Ardoukoba (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ardoukoba"),
    ("La plage de Khor Ambado · guía oficial de turismo", "https://guide.visitdjibouti.dj/la-plage-de-khor-ambado/"),
    ("Hôtel Village Les Sables Blancs (Tadjoura)", "https://www.sables-blancs-djibouti.com/"),
    ("Grand Bara (Wikipedia EN)", "https://en.wikipedia.org/wiki/Grand_Bara"),
    ("RN-1 (Wikipedia EN)", "https://en.wikipedia.org/wiki/National_Highway_1_(Djibouti)"),
    ("Ali Sabieh Mountain (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ali_Sabieh_Mountain"),
    ("RN-5 (Wikipedia EN)", "https://en.wikipedia.org/wiki/National_Highway_5_(Djibouti)"),
    ("Foreign military bases in Djibouti (Wikipedia EN)", "https://en.wikipedia.org/wiki/Foreign_military_bases_in_Djibouti"),
    ("Camp Lemonnier (Wikipedia EN)", "https://en.wikipedia.org/wiki/Camp_Lemonnier"),
    ("Nagad railway station (Wikipedia EN)", "https://en.wikipedia.org/wiki/Nagad_railway_station"),
    ("Holhol y su viaducto de 1900 (Wikipedia EN)", "https://en.wikipedia.org/wiki/Holhol"),
]

# Bucle grande: capital · sur (Ali Sabieh–Dikhil–Lac Abbé) · Lac Assal–Ardoukôba · Tadjoura–Goda · Obock
CORRIDOR = [
    (11.5923, 43.14603),
    (11.52353, 43.12821),
    (11.46157, 43.25009),
    (11.30972, 42.92917),
    (11.15429, 42.70691),
    (11.23468, 42.60997),
    (11.10543, 42.37047),
    (11.19868, 41.78055),
    (11.5838, 42.82326),
    (11.5261, 42.6036),
    (11.61056, 42.47583),
    (11.66116, 42.4135),
    (11.78738, 42.88109),
    (11.83333, 42.66667),
    (11.96475, 43.28841),
    (12.46742, 43.31739),
    (11.5923, 43.14603),
]

# Regreso corto por la costa: Obock · Tadjoura · Ghoubbet · Arta · Khor Ambado · capital
CORRIDOR_ALT = [
    (11.96475, 43.28841),
    (11.78738, 42.88109),
    (11.66116, 42.4135),
    (11.5261, 42.6036),
    (11.5838, 42.82326),
    (11.59283, 43.0197),
    (11.5923, 43.14603),
]

HISTORIA_RESUMEN = "Yibuti es un país diminuto —unos 23.200 kilómetros cuadrados y poco más de un millón de habitantes— encajado entre Etiopía, Eritrea y Somalia, frente al estrecho de Bab el-Mandeb. Su historia es la de un cruce de caminos: sultanatos afares y somalíes islamizados desde muy pronto, una colonia francesa nacida en 1862 para servir de puerto y de cabeza del ferrocarril a Adís Abeba, y una independencia tardía, en 1977. Desde entonces lo gobiernan dos hombres de la misma familia, y desde 1999 Ismail Omar Guelleh. Hoy vive del puerto por el que respira Etiopía y del alquiler de bases militares a cuatro potencias. Es estable, caro y, según Freedom House, no libre."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>El rincón del Cuerno de África que hoy ocupa Yibuti aparece en los textos egipcios como parte del <em>país de Punt</em>, la tierra de la mirra y el incienso citada desde el tercer milenio antes de nuestra era, y más tarde quedó dentro del radio de influencia del reino de Aksum. La verdadera bisagra fue el islam: la proximidad de la península arábiga hizo que las poblaciones somalíes y afares de esta costa figuren entre las primeras del continente en abrazarlo, muy poco después de la hégira.</p><p>De esa islamización nacieron los estados medievales que organizaron el territorio. El sultanato de Ifat, fundado en 1285 por la dinastía Walashma con centro en Zeila, fue derrotado por el emperador etíope Amda Seyon I en 1332; su heredero, el sultanato de Adal, llegó a controlar buena parte de lo que hoy son Yibuti, Somalilandia, Eritrea y zonas de Etiopía. Más cerca en el tiempo, los sultanatos de Tadjoura y de Obock dominaban los puertos y las rutas de caravanas que subían la sal del lago Assal —a 155 metros bajo el nivel del mar, el punto más bajo de África— hasta el altiplano etíope, y la cambiaban por sorgo, café y marfil. Esas caravanas de camellos siguen siendo la imagen del lago.</p>"),
    ("Colonización",
     "<p>Francia llegó por el mar y por el comercio. En 1862 compró a los sultanes locales el fondeadero de Obock, y entre 1883 y 1887 firmó una serie de tratados con jefes afares y somalíes que ampliaron su protectorado. En 1894 Léonce Lagarde estableció una administración permanente y bautizó el conjunto como <em>Côte française des Somalis</em>, la Costa Francesa de los Somalíes; en 1896 la capital se trasladó de Obock a la ciudad de Yibuti, fundada sobre un buen abrigo natural.</p><p>La razón de ser de la colonia fue el ferrocarril. Las obras de la línea franco-etíope empezaron en 1897, el primer servicio comercial se abrió en 1901 y el tren alcanzó Adís Abeba en junio de 1917: desde entonces Yibuti es la salida al mar del interior etíope, y eso explica casi todo lo demás. La Segunda Guerra Mundial dejó al territorio del lado de Vichy; en junio de 1940 las tropas italianas ocuparon cerca de un tercio de la colonia, los británicos la bloquearon y hacia 1942 unos cuatro mil soldados británicos entraron en la ciudad, mientras un batallón local participaba en 1944 en la liberación de París.</p><p>Francia dejó la lengua, el trazado urbano, el código administrativo y una frontera que separa a afares y somalíes issas de sus parientes de Etiopía y Somalia.</p>"),
    ("Independencia y construcción del Estado",
     "<p>La descolonización fue lenta y disputada. En el referéndum de 1958 el territorio votó seguir vinculado a Francia, con un voto somalí mayoritariamente contrario y denuncias de manipulación. El de 19 de marzo de 1967 repitió el resultado, también empañado por el fraude y por la expulsión de unos diez mil somalíes; a continuación la colonia pasó a llamarse Territorio Francés de los Afares y los Issas, un nombre que reconocía por fin a los dos pueblos del país. La consulta del 8 de mayo de 1977 dio un 98,8% a favor de la separación y el 27 de junio de 1977 Yibuti fue independiente, ingresando ese mismo año en Naciones Unidas.</p><p>El primer presidente, Hassan Gouled Aptidon, convirtió el país en un Estado de partido único en 1981 al declarar su Agrupación Popular para el Progreso (RPP) única formación legal. La Constitución vigente data del 4 de septiembre de 1992, muy inspirada en el sistema francés aunque con algunos elementos de la sharía. Entre 1991 y 1994 el Estado libró una guerra civil contra el FRUD, guerrilla predominantemente afar, que firmó un acuerdo de paz en diciembre de 1994. En 1999 Gouled se retiró a los 83 años y le sucedió su sobrino Ismail Omar Guelleh; el acuerdo definitivo que cerró el conflicto se selló el 12 de mayo de 2001.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>El siglo XXI convirtió la posición de Yibuti en su principal industria. Estados Unidos arrendó en 2002 el antiguo cuartel francés de Camp Lemonnier —contrato renovado en 2014 por veinte años y unos 63 millones de dólares anuales—, Francia firmó en 2011 un tratado de cooperación de defensa en vigor desde 2014, Japón abrió aquí su única base permanente en el exterior y China inauguró en 2017 su primera instalación militar en el extranjero. España despliega aquí el destacamento Orión y participa en la operación Atalanta de la Unión Europea contra la piratería.</p><p>En paralelo llegaron las grandes obras: el ferrocarril eléctrico de vía estándar entre Adís Abeba y Yibuti, de 759 kilómetros y unos 4.500 millones de dólares financiados sobre todo por el Eximbank chino, se inauguró en 2016 y 2017 y arrancó el servicio comercial el 1 de enero de 2018, con terminal en Nagad, junto al aeropuerto de la capital; también se construyó el puerto de Tadjoura. La política interior se fue cerrando: una enmienda constitucional de 2010 suprimió el límite de mandatos y Guelleh fue reelegido en 2005, 2011, 2016 y 2021. En agosto de 2021 hubo choques entre afares e issas en varios barrios de la capital. Una reforma constitucional de noviembre de 2025 eliminó el límite de edad de 75 años y permitió que Guelleh, de 78, volviera a presentarse en abril de 2026.</p>"),
    ("Política y gobierno en 2026",
     "<p>Yibuti es formalmente una república presidencialista, con una Asamblea Nacional unicameral de 65 diputados elegidos cada cinco años. A fecha de septiembre de 2026, según la ficha país del Ministerio de Asuntos Exteriores de España (mayo de 2026), el jefe del Estado es Ismail Omar Guelleh, en el poder desde 1999, cuando sucedió a su tío; las últimas presidenciales se celebraron el 10 de abril de 2026 y las ganó con el 97,81% de los votos. El primer ministro es Abdoulkader Kamil Mohamed, nombrado en marzo de 2013. La misma fuente describe el sistema como de partido único dominante, con oposición en el Parlamento solo desde 2013.</p><p>En la práctica se trata de un régimen autoritario con formas electorales. Freedom House, en <em>Freedom in the World 2025</em>, clasifica al país como <strong>«Not Free»</strong> con 24 puntos sobre 100 —5 sobre 40 en derechos políticos y 19 sobre 60 en libertades civiles— y señala que la actuación de la oposición está severamente limitada y que los periodistas críticos son acosados o detenidos. Reporteros Sin Fronteras sitúa a Yibuti en el puesto 167 de 180 en 2026 y afirma que no hay ningún medio independiente radicado en el país. El Exterior español desaconseja las franjas fronterizas con Eritrea y Somalia por la presencia de minas sin desactivar. España no tiene embajada residente y se relaciona con el país desde Adís Abeba.</p>"),
    ("Economía y recursos",
     "<p>Yibuti no vive de lo que produce, sino de por dónde pasa. Los servicios —puerto, logística, zona franca, telecomunicaciones y banca— suponían en torno al 85% del PIB en 2023, frente a un 14% de industria y apenas un 1% de agricultura. El Banco Mundial cifra el PIB en unos 4.600 millones de dólares y el PIB per cápita entre 3.900 y 4.250 dólares según la serie consultada. La moneda es el franco yibutiano, muy estable: un euro equivalía a 206,3 francos en diciembre de 2025.</p><p>La clave es Etiopía, que perdió su salida al mar con la independencia de Eritrea en 1993 y canaliza por aquí su comercio exterior: es el destino del 58,42% de las exportaciones yibutianas, por delante de China (15,82%) y Estados Unidos (7,04%), mientras los principales proveedores son China, Arabia Saudí, Emiratos Árabes Unidos y Francia. A ello se suman el alquiler de las bases militares extranjeras, que pagan decenas de millones de dólares al año, la sal del lago Assal y un turismo pequeño pero singular, centrado en el buceo y en los tiburones ballena que se concentran en el golfo de Tadjoura entre noviembre y febrero. Los puntos débiles son crónicos: paro del 26,2% en 2023, deuda externa en torno al 64% del PIB en 2024 y una fuerte exposición a las crisis del mar Rojo.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Viven en Yibuti algo menos de 1,2 millones de personas, y cerca de 976.000 en la propia capital: es casi un país-ciudad. Las fuentes consultadas describen dos grandes grupos de población, los somalíes —en torno al 60%— y los afares, alrededor del 35%. Las lenguas oficiales son el francés y el árabe, mientras el somalí y el afar tienen rango de lenguas nacionales y son las de la calle; en carretera y en cualquier gestión oficial el francés es lo que funciona. El islam suní es la religión del Estado y agrupa a cerca del 95% de la población. La esperanza de vida ronda los 66 años.</p><p>La cocina mezcla influencias somalíes, afares, yemeníes, francesas e indias: el <em>lahoh</em> del desayuno, los guisos con arroz, el <em>fah-fah</em> de carne y las <em>sambusas</em>. El khat, que llega a diario desde Etiopía, marca el ritmo de las tardes. La fiesta nacional es el 27 de junio. Yibuti es Estado parte de la Convención del Patrimonio Mundial desde 2007, pero no tiene ningún bien inscrito: solo una lista indicativa de diez sitios.</p><p>Para quien viaja, tres cautelas. Conviene vestir con discreción. Está prohibido fotografiar edificios públicos, bases militares y residencias de autoridades, y no se fotografía a nadie sin permiso. El ramadán de 2027 empieza en torno al 8 de febrero y durante el día se come y se bebe con discreción.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Yibuti (Ministerio de Asuntos Exteriores, UE y Cooperación de España · PDF · mayo de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/YIBUTI_FICHA%20PAIS.pdf"),
    ("Recomendaciones de viaje: Yibuti (Ministerio de Asuntos Exteriores de España · consultado en septiembre de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Yibuti"),
    ("Djibouti: Freedom in the World 2025 (Freedom House · 2025)", "https://freedomhouse.org/country/djibouti/freedom-world/2025"),
    ("Djibouti (Reporteros Sin Fronteras · Índice Mundial de Libertad de Prensa · 2026)", "https://rsf.org/en/country/djibouti"),
    ("History of Djibouti (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/History_of_Djibouti"),
    ("Djibouti (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Djibouti"),
    ("Yibuti (Wikipedia en español · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Yibuti"),
    ("Djibouti (Wikipedia en francés · consultado en septiembre de 2026)", "https://fr.wikipedia.org/wiki/Djibouti"),
    ("Djibouti - States Parties (UNESCO · Centro del Patrimonio Mundial · consultado en septiembre de 2026)", "https://whc.unesco.org/en/statesparties/dj"),
    ("Djibouti - Datos del Banco Mundial (Banco Mundial · World Development Indicators · 2025)", "https://data.worldbank.org/country/djibouti"),
    ("Addis Ababa-Djibouti Railway (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Addis_Ababa%E2%80%93Djibouti_Railway"),
    ("Ethio-Djibouti Railways (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Ethio-Djibouti_Railways"),
    ("Lake Assal, Djibouti (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Lake_Assal_(Djibouti)"),
    ("Gulf of Tadjoura (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Gulf_of_Tadjoura"),
    ("Understanding whale sharks: from Djibouti to the Red Sea (Oceanographic Magazine · consultado en septiembre de 2026)", "https://oceanographicmagazine.com/features/whale-sharks-djibouti/"),
    ("Djiboutian cuisine (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Djiboutian_cuisine"),
    ("Djibouti (Encyclopaedia Britannica · consultado en septiembre de 2026)", "https://www.britannica.com/place/Djibouti"),
]

SPEC = dict(
    slug="yibuti", name="Yibuti", revision="18 sep 2026",
    sub="FUERA DE RUTA — la vuelta de 2027 termina en Kenia · ficha informativa para un viaje aparte desde Etiopía · Lac Assal, Lac Abbé y tiburón ballena, con calor extremo y cinco ejércitos extranjeros",
    chips=[
        ("ESTATUS", "FUERA DE RUTA. La vuelta de 2027 termina en Kenia; esta ficha es informativa…"),
        ("CÓMO LLEGAR", "Por tierra desde Etiopía (Galafi, Dewele/Ali Sabieh, Balho) o desde Somalilandia (Loyada)…"),
        ("VISADO", "OBLIGATORIO para españoles. eVisa en evisa.gouv.dj (12 USD tránsito de 1-14 días…"),
        ("VEHÍCULO", "CPD NO OBLIGATORIO (probable): AIT/FIA no tiene emisor en Yibuti…"),
        ("SEGURIDAD", "Precaución · vetadas fronteras Eritrea y Somalilandia"),
        ("SEGURO", "Carta Verde NO vale · COMESA Yellow Card"),
        ("SALUD", "Fiebre amarilla obligatoria · malaria todo el año"),
        ("DRONES", "No entrar con dron: se requisa (MAEC)"),
        ("STARLINK", "No disponible · regulación estancada (2026)"),
        ("4x4", "Imprescindible · convoy de dos · nunca de noche"),
        ("A PIE", "Solo en la capital y de día · nada fuera del asfalto"),
        ("PERRO", "SIN REQUISITOS PUBLICADOS por Yibuti. La web del ministerio competente (maepe-rh.dj) existe pero no publica…"),
        ("MONEDA", "Franco yibutiano (DJF), fijado al dólar. 1 EUR = 206,3 DJF (MAEC, diciembre de 2025)…"),
        ("VENTANA", "Semidesértico: 30 °C en enero y 45 °C en julio (Ficha País del MAEC)…"),
    ],
    center=[11.79, 42.55], zoom=7,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle grande: capital · sur (Ali Sabieh–Dikhil–Lac Abbé) · Lac Assal–Ardoukôba · Tadjoura–Goda · Obock",
    corridor_alt_label="Regreso corto por la costa: Obock · Tadjoura · Ghoubbet · Arta · Khor Ambado · capital",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Lake_Assal_1-Djibouti.jpg?width=1200",
    hero_credit="Lac Assal · Fishercd · Public domain",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Yibuti queda fuera de la ruta de 2027 por geografía, no por seguridad: la vuelta termina en Kenia y no sube al Cuerno de África, de modo que incluirlo obligaría a atravesar Etiopía entera de ida y vuelta —más de 4.000 km extra— para un país de 23.200 km² que se recorre en cinco o seis días. Hecho aparte sí es viable y bastante clásico: se entra desde Etiopía por Galafi o por Dewele/Ali Sabieh con el vehículo propio y un permiso temporal de aduana, o se vuela a Yibuti-Ambouli y se alquila un 4x4. El MAEC recomienda viajar con precaución y abstenerse de hacerlo por determinadas zonas —frontera con Eritrea, frontera con Somalia (Somalilandia), estrecho de Bab el-Mandeb—, pero la capital y el eje Lac Assal–Grand Bara–Lac Abbé son practicables. El factor que manda es el calor: de junio a septiembre se pasa de 45 °C y no hay PDI de interior que lo aguante; la ventana real es de noviembre a febrero, que además coincide con la temporada de tiburón ballena en el golfo de Tadjoura. Coste orientativo para tres personas y dos coches, dos semanas desde Adís Abeba: 2.500–3.500 € (visados, combustible caro, alojamiento con aire acondicionado, excursiones). Habría que decidir tres cosas antes de comprometerse: si el eVisa se acepta en frontera terrestre (no está confirmado), qué se hace con el perro —Yibuti no publica requisitos de entrada y la vuelta a la UE exige titulación antirrábica hecha con meses de antelación— y asumir que el dron se queda en casa.",
    facts=[
        ("Estatus", "FUERA DE RUTA. La vuelta de 2027 termina en Kenia; esta ficha es informativa, para un viaje aparte desde Etiopía."),
        ("Cómo llegar", "Por tierra desde Etiopía (Galafi, Dewele/Ali Sabieh, Balho) o desde Somalilandia (Loyada); en avión a Yibuti-Ambouli (JIB); en tren Adís Abeba–Nagad desde el 1 de enero de 2018."),
        ("Visado", "OBLIGATORIO para españoles. eVisa en evisa.gouv.dj (12 USD tránsito de 1-14 días; 23 USD estancia de 15-90 días) o embajada de Yibuti en París o Adís Abeba. El MAEC cifra el coste en 50-80 €."),
        ("Vehículo/aduana", "CPD NO OBLIGATORIO (probable): AIT/FIA no tiene emisor en Yibuti. Lo documentado es un permiso temporal de importación emitido en la propia frontera, con 10 días de validez en el caso registrado."),
        ("Seguro", "La Carta Verde europea NO cubre. Yibuti emite y acepta la COMESA Yellow Card, que cubre daños a terceros y urgencias médicas y admite matrículas extranjeras o temporales."),
        ("Moneda", "Franco yibutiano (DJF), fijado al dólar. 1 EUR = 206,3 DJF (MAEC, diciembre de 2025). País caro y de efectivo: fuera de la capital rechazan las tarjetas."),
        ("Perro", "SIN REQUISITOS PUBLICADOS por Yibuti. La web del ministerio competente (maepe-rh.dj) existe pero no publica trámite. Vuelta a la UE por vía A: titulación antirrábica hecha en la UE con 3 meses de antelación."),
        ("Drones", "DE FACTO PROHIBIDOS. El MAEC recomienda «encarecidamente» no entrar con un dron de recreo porque puede ser requisado. Prohibido además fotografiar puertos, aeropuertos, puentes, edificios públicos e instalaciones militares."),
        ("Starlink", "NO DISPONIBLE. Yibuti figura como «planificado, sin fecha»; la aprobación regulatoria está estancada en todo el Cuerno de África (mayo de 2026). Alternativa: SIM de Djibouti Telecom, en monopolio."),
        ("Seguridad", "MAEC: viajar con precaución y abstenerse por determinadas zonas. FCDO desaconseja TODO viaje a la frontera con Eritrea (27 de julio de 2026). Minas sin desactivar en Tadjoura y Obock."),
        ("Clima", "Semidesértico: 30 °C en enero y 45 °C en julio (Ficha País del MAEC). De junio a septiembre el interior es inviable. Ventana de viaje: noviembre-febrero."),
        ("Sanidad", "Fiebre amarilla exigida por el MAEC para mayores de 1 año. Malaria en todo el país. Cólera periódico. Servicios médicos «muy deficientes» y concentrados en la capital; seguro con repatriación aérea medicalizada."),
    ],
    alerts=[
        "CALOR EXTREMO de junio a septiembre: por encima de 45 °C a la sombra y noches que no bajan de 38 °C. Cualquier PDI de interior (Lac Assal, Lac Abbé, Grand Bara) es inviable en esos meses; la ventana razonable es de noviembre a febrero.",
        "FRONTERA CON ERITREA: el FCDO desaconseja TODO viaje a la zona (actualización de 27 de julio de 2026) y Canadá pide evitar los 10 km próximos. El MAEC añade la frontera con Somalia (Somalilandia) y el archipiélago de las Sept-Frères.",
        "MINAS SIN DESACTIVAR confirmadas por el MAEC en las regiones de Tadjoura y Obock. Canadá amplía la advertencia a munición sin explotar en las zonas fronterizas con Somalia y Etiopía y pide no abandonar el asfalto en Obock, Tadjoura y Ali Sabieh.",
        "FOTOGRAFÍA RESTRINGIDA. El FCDO señala que está prohibido fotografiar puertos, edificios públicos, aeropuertos, instalaciones militares y puentes, con confiscación del equipo y posible detención. Con cinco ejércitos extranjeros en un país pequeño, la restricción afecta a media capital.",
        "DRONES: el MAEC recomienda «encarecidamente no venir al territorio de Yibuti en posesión de un dron de recreo ya que puede ser requisado». No hay procedimiento de autorización publicado, así que no hay forma de legalizarlo desde España.",
        "VISADO ANTES DE LLEGAR. El MAEC recomienda obtenerlo antes del viaje; el visado en aeropuerto es discrecional y para estancias cortas, y una agencia local afirma que no existe visado a la llegada en las fronteras terrestres con Etiopía. Estancia irregular: 40.000 FDJ de multa pasados 30 días, 80.000 FDJ pasados 90, o 3-6 meses de prisión y 5 años de prohibición de entrada.",
        "FIEBRE AMARILLA obligatoria para mayores de 1 año según el MAEC. Hay además malaria en todo el país durante todo el año, cólera periódico y circulación de poliovirus derivado de vacuna, por lo que puede exigirse acreditación de vacunación antipoliomielítica al SALIR del país.",
        "AMENAZA TERRORISTA moderadamente alta por la presencia de Al Shabaab, que ha amenazado a Yibuti por su participación en operaciones de la Unión Africana. Sin atentados desde 2014, pero con vigilancia en lugares frecuentados por occidentales.",
        "CARRETERAS MALAS Y TRÁFICO PESADO. El corredor Etiopía-puerto de Yibuti canaliza en torno al 95% del comercio exterior de la zona IGAD y mueve miles de camiones al día; un overlander describe la RN-1 como «la carretera asfaltada más rota y destruida que he visto nunca en África». El MAEC pide 4x4 y convoy de dos vehículos, y nadie circula de noche.",
        "SIN STARLINK Y SIN COBERTURA FIABLE FUERA DE LA CAPITAL. Djibouti Telecom mantiene el monopolio y hay que contar con estar incomunicado en el Lac Abbé, el Grand Bara y el norte de Obock.",
        "PAÍS CARO Y DE EFECTIVO. La gasolina ronda 1,50 €/litro (310 DJF) y una botella de 1,5 l de agua unos 100 DJF (HikersBay, 18 de septiembre de 2026). El MAEC avisa de que fuera de la capital rechazan las tarjetas.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Llegada y capital", "Yibuti ciudad: plaza Mahmoud Harbi, mercado central, barrio europeo, Nagad", "~40 km · 2 días"),
        ("2 · Frontera sur", "Yibuti ciudad → Loyada → Yibuti ciudad", "~50 km · 1 día"),
        ("3 · Ferrocarril y montañas rojas", "Yibuti ciudad → Holhol → Ali Sabieh (RN-5)", "~100 km · 1 día"),
        ("4 · El llano", "Ali Sabieh → Grand Bara → Dikhil (RN-1)", "~130 km · 1 día"),
        ("5 · Pista del Abbé", "Dikhil → Lac Abbé (pista) y noche en campamento", "~110 km · 1 día"),
        ("6 · Vuelta al asfalto", "Lac Abbé → Dikhil → Arta (RN-1)", "~190 km · 1 día"),
        ("7 · Tiburón ballena", "Arta y plage d'Arta: salida de snorkel en el golfo de Tadjoura", "~30 km · 1 día"),
        ("8 · Rift y sal", "Arta → Ghoubbet → Ardoukôba → Lac Assal (RN-9)", "~90 km · 1 día"),
        ("9 · Al norte del golfo", "Lac Assal → Tadjoura → Plage des Sables Blancs (RN-9)", "~120 km · 1 día"),
        ("10 · Macizo de Goda", "Tadjoura → Randa → Forêt du Day → Bankoualé (RN-11 + pista)", "~70 km · 2 días"),
        ("11 · El norte", "Bankoualé → Tadjoura → Obock (RN-14)", "~100 km · 1 día"),
        ("12 · Bab el-Mandeb", "Obock → Khor Angar → Ras Siyyan / Sept Frères (según avisos de seguridad)", "~150 km · 2 días"),
        ("13 · Regreso", "Obock → Tadjoura → Yibuti ciudad (RN-14 + RN-9, o ferry)", "~190 km · 1 día"),
        ("14 · Playa y salida", "Khor Ambado y cierre en la capital", "~50 km · 1 día"),
    ],
    offroad=[
        "La pista de Dikhil al Lac Abbé es la ruta 4x4 de referencia del país: arena, grava y lecho seco, sin señalización, y las fuentes coinciden en que «la única forma práctica de visitar el Lac Abbé es en 4x4 desde Yibuti ciudad», normalmente con conductor-guía local (https://www.atlasandboots.com/travel-blog/lac-abbe-in-djibouti/).",
        "Solo el 12 % de las carreteras del país está asfaltado, de modo que fuera de la RN-1, la RN-5, la RN-9, la RN-11 y la RN-14 casi todo es pista (https://en.wikipedia.org/wiki/Grand_Bara).",
        "La travesía del Grand Bara se hace por la carretera de 40 km abierta en 1981; salirse a campo través por el lecho de arcilla es tentador pero peligroso tras las lluvias de julio y septiembre, cuando el llano se encharca (https://en.wikipedia.org/wiki/Grand_Bara).",
        "El desvío al cono y las coladas del Ardoukôba, entre el Ghoubbet y el Lac Assal, es una pista corta sobre lava de 1978: roca cortante, buena distancia al suelo y neumáticos reforzados (https://en.wikipedia.org/wiki/Ardoukoba).",
        "La subida de Randa a la Forêt du Day y a Bankoualé es pista de montaña con rampas y piedra suelta; Randa está a 927 m y el bosque a más de 950 m, a unos 16 km (https://en.wikipedia.org/wiki/Randa,_Djibouti, https://en.wikipedia.org/wiki/Day_Forest_National_Park).",
        "Los grabados de Abourma, en el macizo de Makarrassou (N 11,905050 · E 42,481649), se alcanzan por pista larga desde Tadjoura y exigen guía local y una caminata final de hora y media; están en la lista indicativa de la UNESCO desde 2015 (https://whc.unesco.org/en/tentativelists/5957/, https://www.christravelblog.com/djibouti-the-best-1-week-djibouti-roadtrip-itinerary-in-a-4x4/).",
        "ZONAS VETADAS: el MAEC desaconseja la franja fronteriza con Eritrea y con Somalia por grupos terroristas y MINAS SIN DESACTIVAR, sitúa los distritos de Tadjoura y Obock en riesgo por minas confirmadas y desaconseja el archipiélago de las Sept Frères; Estados Unidos añade que hay minas sin señalizar en la frontera eritrea y que conviene «no salir del asfalto» allí (https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Yibuti, https://travel.state.gov/en/international-travel/travel-advisories/djibouti.html).",
        "Ningún organismo publica un sistema de permisos de circulación 4x4 para turistas que se haya podido verificar; lo que sí es seguro es que el puerto de Doraleh, el aeropuerto y los perímetros de las bases militares son zona restringida y fotografiarlos acarrea multa, confiscación, detención o expulsión (https://travel.state.gov/en/international-travel/travel-advisories/djibouti.html).",
    ],
    senderismo=[
        "Subida a la montaña del emblema nacional de Ali Sabieh (801 m) desde el pueblo: la vía más sencilla es a pie y la cima domina la ciudad y los montes Arrei (https://en.wikipedia.org/wiki/Ali_Sabieh_Mountain).",
        "Recorrido entre las chimeneas del Lac Abbé al amanecer: caminata corta y llana entre agujas de caliza de hasta 50 m y fuentes termales, siempre con guía del campamento por el suelo caliente (https://en.wikipedia.org/wiki/Lake_Abbe).",
        "Vuelta por el campo de lava del Ardoukôba y sus grietas del Rift: terreno cortante, media jornada como mucho y nunca a mediodía (https://en.wikipedia.org/wiki/Ardoukoba).",
        "Travesías por el macizo de Goda entre Randa, Bankoualé y la Forêt du Day: valles cultivados, manantiales y el único bosque del país; Walkopedia recoge estas rutas como la principal caminata de Yibuti (https://www.walkopedia.net/best-world-walks/Djibouti/Goda-Mountains).",
        "Sendero de aves en la Forêt du Day: recorrido por la mancha de enebro de 900 hectáreas buscando el francolín de Yibuti y las otras dos aves exclusivas del parque (https://en.wikipedia.org/wiki/Day_Forest_National_Park).",
        "Caminata final a los grabados rupestres de Abourma: unos noventa minutos de aproximación por terreno pelado desde donde queda el 4x4, con guía local (https://www.christravelblog.com/djibouti-the-best-1-week-djibouti-roadtrip-itinerary-in-a-4x4/).",
        "Paseo por la orilla de sal del Lac Assal hasta el agua: quince o veinte minutos de costra sobre el punto más bajo de África, con calzado cerrado (https://en.wikipedia.org/wiki/Lake_Assal_(Djibouti)).",
        "Recorrido a pie por el casco encalado de Tadjoura entre sus mezquitas y el puerto, y por el trazado colonial de la capital entre la plaza Mahmoud Harbi y el mercado central (https://wikitravel.org/en/Tadjoura, https://en.wikipedia.org/wiki/Djibouti_City).",
    ],
    acampada=[
        "No existe una red de campings formales: fuera de la capital el alojamiento habitual son «campements» y «auberges» muy básicos, según la crónica en 4x4 de una vuelta de nueve días por el país (https://www.christravelblog.com/djibouti-the-best-1-week-djibouti-roadtrip-itinerary-in-a-4x4/).",
        "Lac Abbé: se duerme en campamentos afar de cabañas junto al lago, incluidos en los paquetes de dos días de los operadores locales; es la pernocta obligada si se quiere el amanecer entre chimeneas (https://www.atlasandboots.com/travel-blog/lac-abbe-in-djibouti/).",
        "Tadjoura: el Hôtel Village Les Sables Blancs, sobre la playa de arena blanca, es la opción de bungalós más citada de la orilla norte (https://www.sables-blancs-djibouti.com/).",
        "Macizo de Goda: Randa y Bankoualé concentran los campamentos de montaña y son la única pernocta fresca del país, por altitud (927 m en Randa) (https://en.wikipedia.org/wiki/Randa,_Djibouti).",
        "Khor Ambado: la playa admite pasar el día y hay algo de sombra, pero el MAEC avisa de robos frecuentes al atardecer, así que NO es sitio para dormir en los vehículos (https://guide.visitdjibouti.dj/la-plage-de-khor-ambado/, https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Yibuti).",
        "Acampada libre: en un país donde el territorio está salpicado de bases militares y zonas restringidas, plantar tienda sin permiso del jefe de la aldea o del campamento es mala idea; conviene preguntar siempre en el poblado más cercano.",
        "Zonas donde no acampar bajo ningún concepto: franja fronteriza con Eritrea y con Somalia (minas sin desactivar), entorno del puerto de Doraleh, aeropuerto y perímetros militares (https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Yibuti, https://travel.state.gov/en/international-travel/travel-advisories/djibouti.html).",
        "No he podido consultar iOverlander ni Tracks4Africa para Yibuti en esta ronda: las entradas concretas de acampada de overlanders quedan POR CONFIRMAR y habría que revisarlas antes de publicar la ficha.",
    ],
    visado=[
        "OBLIGATORIO para españoles, sin exención. Pasaporte con validez mínima de 6 meses y justificante de alojamiento y de billete de salida.",
        "Vías: eVisa en el portal oficial www.evisa.gouv.dj (tránsito de 1-14 días, 12 USD; estancia corta de 15-90 días, 23 USD, según la ficha de política de visados), embajada de Yibuti en París (+33 1 47 27 49 22) o en Adís Abeba, y visado en el aeropuerto de Ambouli, discrecional y solo para estancias cortas. El MAEC cifra el coste en 50-80 €.",
        "FRONTERA TERRESTRE: POR CONFIRMAR, y es el punto que hay que cerrar antes de comprar nada. La ficha de política de visados recoge que el titular de eVisa puede entrar «por el aeropuerto internacional de Ambouli o por cualquier otro paso fronterizo», pero una agencia local sostiene que el visado a la llegada no existe en las fronteras terrestres con Etiopía y hay viajeros a los que la propia embajada negó la validez del eVisa por tierra y les emitió visado en el pasaporte.",
        "Con vehículo propio, lo prudente es el visado físico en el pasaporte emitido por la embajada de Yibuti en Adís Abeba: un overlander lo obtuvo allí el mismo día por 90 USD. Cuesta más que el eVisa, pero no deja margen de discusión en Galafi.",
        "Estancia irregular: multa de 40.000 FDJ pasados 30 días y de 80.000 FDJ pasados 90; en su defecto, de 3 a 6 meses de prisión y 5 años de prohibición de entrada.",
        "Periodistas y cualquier trabajo de reportaje: se exige acreditación previa de las autoridades yibutianas. Grabar sin ella, en un país con cinco bases militares extranjeras, es buscarse un problema serio.",
    ],
    fronteras_rows=[
        ("Paso terrestre principal desde Etiopía", "Galafi (11°43′01″N 41°50′12″E, RN-1, 218 km de la capital)", "ABIERTO. Es el paso más usado y el único bien documentado por overlanders: aquí se emite el permiso temporal de importación del vehículo. Carretera en mal estado y tráfico continuo de camiones. Etiopía y Yibuti han acordado una hoja de ruta para convertirlo en puesto fronterizo de parada única; estado de las obras por confirmar. Fuente: Wikipedia y The Road Chose Me."),
        ("Paso terrestre sur desde Etiopía", "Dewele (Etiopía) / Ali Sabieh (Yibuti), a 18 km de Ali Sabieh y 98 km de la capital", "ABIERTO. Mejor asfaltado que Galafi según las guías locales, y es por donde cruza el ferrocarril Adís Abeba-Yibuti con su propio control fronterizo. Horarios y práctica con vehículo extranjero POR CONFIRMAR. Fuente: Travel2Djibouti y Wikipedia."),
        ("Paso terrestre norte desde Etiopía", "Balho (abierto el 20 de septiembre de 2020)", "ABIERTO sobre el papel, el más reciente de los tres pasos oficiales con Etiopía. Está en la zona montañosa del norte, cerca del área que el FCDO desaconseja por la frontera eritrea. Uso turístico y trámite de vehículo POR CONFIRMAR. Fuente: Wikipedia."),
        ("Paso terrestre a Somalilandia", "Loyada (11°28′00″N 43°14′45″E, 25 km de la capital)", "ABIERTO pero DESACONSEJADO. Único paso oficial hacia Somalilandia; ha sufrido cierres periódicos por motivos políticos y fue reabierto en 2002. El MAEC desaconseja la zona fronteriza con Somalia (Somalilandia). Fuente: Wikipedia y MAEC."),
        ("Frontera con Eritrea", "Frontera Yibuti-Eritrea (norte, región de Obock)", "NO UTILIZABLE. El FCDO desaconseja TODO viaje a esa frontera (27 de julio de 2026) y Canadá pide evitar los 10 km próximos por tensiones regionales. Fuente: FCDO y Gobierno de Canadá."),
        ("Aeropuerto internacional", "Yibuti-Ambouli (JIB/HDAM), 11°32′47″N 43°09′33″E, 6 km del centro", "OPERATIVO. Único aeropuerto internacional del país. Uso civil y militar compartido (Camp Lemonnier estadounidense, base aérea francesa BA 188, base japonesa, italiana y fuerza aérea yibutiana); el tráfico militar supone en torno al 75% de las operaciones. Visado a la llegada discrecional. PROHIBIDO FOTOGRAFIAR. Fuente: Wikipedia."),
        ("Puerto", "Puerto de Yibuti (11°36′19″N 43°08′21″E) y terminal de Doraleh", "OPERATIVO. Entrada marítima principal y salida al mar de Etiopía, que supone en torno al 70% de la carga; unos 2.500 buques al año. PROHIBIDO FOTOGRAFIAR. Envío de vehículo en contenedor: posible en teoría, sin documentación abierta localizada en esta revisión."),
        ("Ferry interior del golfo", "Yibuti ciudad (Port de l'Escale, Route de Venise) – Tadjoura – Obock", "OPERATIVO al menos hasta 2019, según reseña de viajero en Petit Futé: unas 2 horas de travesía, ADMITE VEHÍCULOS con hasta 1 hora de espera para asegurar plaza, embarque al final del muelle que sale del palacio presidencial. Horarios y tarifas actuales POR CONFIRMAR."),
        ("Tren", "Ferrocarril Adís Abeba (Sebeta) – Nagad (Yibuti), operativo desde el 1 de enero de 2018", "OPERATIVO pero marginal. Terminal de pasajeros en Nagad, junto al aeropuerto de la capital; el control fronterizo se hace entre Dewele y Ali Sabieh. En 2019 movió solo 84.073 viajeros. No consta transporte de vehículos particulares. Fuente: Wikipedia."),
    ],
    vehiculos=[
        "CPD NO CONFIRMADO COMO OBLIGATORIO. carnetdepassage.org (AIT/FIA) indica que no existe ninguna organización emisora de CPD en Yibuti, y el país no figura en las listas de países que exigen carnet de Horizons Unlimited (revisión de 2023). Llevarlo si ya se tiene por otros países de la ruta no estorba, pero no parece imprescindible.",
        "Lo que sí está documentado es un permiso temporal de importación emitido en la propia frontera: en Galafi, un overlander con vehículo extranjero y sin carnet obtuvo un «Temporary Import Permit» válido 10 días tras consulta del aduanero con su superior. Diez días son pocos para un recorrido tranquilo con dos coches: hay que preguntar en la aduana central de la capital por la prórroga nada más llegar.",
        "SEGURO: la Carta Verde europea no cubre Yibuti. El país es emisor y aceptante de la COMESA Yellow Card, que cubre lesiones y muerte de terceros, daños materiales y gastos médicos de urgencia, y puede emitirse para vehículos con matrícula extranjera o temporal. Si se llega desde Etiopía —también miembro—, lo lógico es contratarla allí; si no, seguro local en frontera.",
        "Permiso internacional de conducir EXIGIDO según el aviso oficial de Canadá. Se conduce POR LA DERECHA, herencia francesa, y el francés es lengua oficial: funciona mucho mejor que el inglés en ventanilla de aduana.",
        "Documentación a llevar: permiso de circulación, ficha técnica, seguro y, si el conductor no es el titular del vehículo, autorización notarial traducida al francés. Con dos coches y tres viajeros, conviene que cada vehículo tenga su carpeta completa.",
        "Carreteras: la RN-1 entre la capital y Galafi soporta el tráfico de camiones etíopes y está destrozada por tramos. El MAEC pide 4x4 y desplazarse en convoy de dos vehículos, que es exactamente la configuración del proyecto. No se circula de noche: sin iluminación, sin arcenes, conducción imprudente y controles con alambrada difíciles de ver.",
        "Fuera del asfalto, minas y munición sin explotar en Obock, Tadjoura y Ali Sabieh: en esas regiones no se sale de la carretera. La pista al Lac Abbé es de arena, arcilla y sal y exige 4x4 real; la bajada al Lac Assal es asfalto con pendiente fuerte y frenos calientes.",
        "Mantenimiento: con 45 °C y polvo permanente hay que entrar con filtros de aire y de combustible de repuesto, revisar refrigeración y llevar neumáticos en buen estado. No hay taller de referencia para un Ineos Grenadier ni para un Delica; la reparación fiable más cercana es Adís Abeba.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "MAEC: recomienda «encarecidamente» no entrar en Yibuti con un dron de recreo porque puede ser requisado. Es la única mención oficial española y no describe procedimiento alguno de autorización.",
        "No hay reglamento civil de drones publicado: la referencia sectorial (drone-laws.com, actualización de 14 de enero de 2026) afirma que «las operaciones con drones no están reguladas en Yibuti» y remite a la Direction de l'Aviation Civile et de la Météorologie (ACAM), teléfono +253 340 151.",
        "El vacío normativo no es permisivo. El aeropuerto de Ambouli es civil y militar a la vez, con el 75% de operaciones militares, y cualquier vuelo en la capital cae dentro de espacio sensible.",
        "El FCDO prohíbe fotografiar puertos, edificios públicos, aeropuertos, instalaciones militares y puentes, con confiscación del equipo y posible detención. Esa prohibición cubre por sí sola buena parte de los sitios donde se querría volar.",
        "Si aun así se quisiera intentar, el único camino es escribir a ACAM con mucha antelación y viajar con la respuesta impresa. Sin autorización en papel, la opción realista es declarar el dron en aduana y aceptar que quede depositado hasta la salida (procedimiento no confirmado).",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "NO DISPONIBLE a fecha de 2026. Yibuti aparece como «planificado, sin fecha» en el seguimiento de cobertura africana de Starlink, sin precio ni calendario.",
        "El análisis de disponibilidad mundial de 10 de mayo de 2026 agrupa a Yibuti con Etiopía, Eritrea y Sudán como países del Cuerno de África «donde la aprobación regulatoria se ha estancado»: no está en los 166 mercados activos, ni en los 42 lanzamientos anunciados para 2026, ni en la lista de prohibiciones expresas.",
        "Alternativa real: SIM local. Djibouti Telecom es empresa pública y «el único proveedor de internet móvil del país». La tarjeta prepago Evatis cuesta unos 1.000 DJF con 500 DJF de saldo, y hay paquetes de datos del tipo 5 GB por 3 días por 500 DJF. Se registra con pasaporte y se compra en tienda —por ejemplo en el Bawadi Mall, junto al puerto—, no en el aeropuerto (guía de 2021: confirmar precios actuales).",
        "Cobertura decente en la capital y el eje de la RN-1; nula o testimonial en el Lac Abbé, el Grand Bara y el norte de Obock. Para esos tramos, comunicación por satélite propia (mensajería tipo Garmin InReach) es la única forma real de pedir ayuda.",
        "Si se entra con terminal Starlink desde Etiopía, lo prudente es declararlo o llevarlo desmontado y sin usar: es equipo de comunicaciones por satélite en un país con presencia militar extranjera masiva y sensibilidad alta.",
    ],
    perro_intro=[
        "NO HAY REQUISITOS PUBLICADOS POR YIBUTI. La web del ministerio competente —Ministère de l'Agriculture, de l'Eau, de la Pêche, de l'Élevage et des Ressources Halieutiques, maepe-rh.dj— existe y abre, pero es un portal institucional genérico sin apartado de importación de animales de compañía. El servicio veterinario oficial estadounidense (APHIS) declara expresamente que los requisitos para perros y gatos hacia Yibuti «no son conocidos» y remite al importador a pedir un permiso de importación al ministerio. Hay que dar por hecho que hace falta permiso previo y gestionarlo con semanas de antelación.",
        "Lo mínimo exigible en cualquier escenario, y lo que hay que llevar sí o sí: microchip ISO, vacuna antirrábica vigente con al menos 21 días desde la primovacunación, certificado veterinario internacional REDACTADO EN FRANCÉS y firmado por veterinario oficial en los días previos a la entrada, y desparasitación interna y externa documentada.",
        "RAZAS PROHIBIDAS: no consta lista publicada por Yibuti. POR CONFIRMAR. Conviene contar con que un perro de tipo molosoide puede generar fricción en frontera aunque no exista norma escrita.",
        "VUELTA A LA UE: Yibuti NO figura en ninguno de los anexos del Reglamento de Ejecución (UE) 2026/636, aplicable desde el 22 de abril de 2026, y ningún país africano continental está en esas listas. Se aplica por tanto la vía A, con plazos que hay que respetar al día según el MAPA: microchip, vacuna antirrábica a partir de las 12 semanas de edad, extracción de sangre para la valoración serológica AL MENOS 30 DÍAS DESPUÉS de la vacunación, resultado igual o superior a 0,5 UI/ml en laboratorio autorizado, y 90 DÍAS DE ESPERA desde la fecha de extracción antes de entrar en la UE.",
        "La titulación se hace en España ANTES de salir y se anota en el pasaporte europeo del animal: si está hecha y vigente, la vuelta desde Yibuti no exige repetirla, solo el certificado zoosanitario firmado por veterinario oficial y la declaración según los modelos del Reglamento de Ejecución (UE) 2026/705. La entrada debe hacerse por un Punto de Entrada de Viajeros (PEV) autorizado, con control documental y de identidad.",
        "VETERINARIOS: no se ha localizado en fuente abierta ninguna clínica veterinaria de referencia en Yibuti ciudad. Existe una comunidad expatriada amplia —militar francesa, estadounidense, japonesa e italiana— que sostiene servicios veterinarios privados, pero hay que identificarlos y confirmarlos antes de salir. POR CONFIRMAR.",
        "RIESGOS PARA EL ANIMAL: el calor es el principal. Con 45 °C en verano y asfalto que quema, el perro no puede bajar del coche entre las 10 y las 18 h ni siquiera en la ventana buena. Añadir rabia presente en la fauna y los murciélagos, garrapatas, y agua no potable: el perro bebe embotellada o filtrada, igual que los viajeros. En el Lac Assal, además, la costra salina corta las almohadillas —un viajero advierte de que el suelo «te destroza los pies»—, así que botines o, mejor, dejarlo en el vehículo con el clima en marcha y turnarse entre los tres.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "FIEBRE AMARILLA: el MAEC la da como obligatoria para mayores de 1 año. TravelHealthPro matiza que el certificado se exige a quien llega de países con riesgo de transmisión y que Yibuti no es endémico. Con África por delante en cualquier ruta que llegue hasta aquí, se viaja vacunado y con el certificado encima.",
        "MALARIA en todo el país y durante todo el año, con transmisión alta según TravelHealthPro: profilaxis con atovacuona/proguanil, doxiciclina o mefloquina según criterio médico, más repelente y mosquitera. Circulan además dengue y chikungunya, de picadura diurna, así que la protección es de 24 horas.",
        "Vacunas recomendadas: hepatitis A y B, fiebre tifoidea, meningitis, tétanos al día y RABIA si hay exposición a animales, que es exactamente el caso viajando con perro. Se ha detectado poliovirus derivado de vacuna: puede exigirse acreditación de vacunación antipoliomielítica al salir del país.",
        "CÓLERA: el MAEC señala que «en Yibuti se registran periódicamente casos de cólera». Agua embotellada o filtrada siempre, nada de hielo, nada de crudos fuera de sitios de confianza e higiene estricta de manos.",
        "SERVICIOS MÉDICOS «muy deficientes y centralizados principalmente en la capital» (MAEC). Las tres referencias de la lista de la embajada británica son el Hôpital Général Peltier (+253 21 35 27 12), el Hôpital Militaire Bouffard (+253 21 35 13 51) y la Clinique Affi (+253 21 34 44 97), todas en Yibuti ciudad. Fuera de la capital no hay nada equiparable.",
        "SEGURO DE VIAJE con cobertura completa y repatriación aérea medicalizada: el MAEC lo exige expresamente. Sin él, una urgencia grave en el interior no tiene solución realista.",
        "GOLPE DE CALOR: es el riesgo sanitario real del viaje. Con más de 45 °C de junio a septiembre y visitas que implican 9 horas de conducción por desierto, contar tres litros de agua por persona y día como mínimo, sales, y ningún esfuerzo entre las 11 y las 17 h.",
    ],
    seguridad_intro="Yibuti no es un país en conflicto, pero está rodeado de ellos y vive de alquilar su territorio a cinco ejércitos extranjeros. El MAEC recomienda viajar con precaución y abstenerse de hacerlo por determinadas zonas: fronteras con Eritrea y con Somalia (Somalilandia), el archipiélago de las Sept-Frères y la navegación por Bab el-Mandeb y el golfo de Adén. La amenaza terrorista de Al Shabaab se considera moderadamente alta aunque no haya atentados desde 2014. Dentro de esas líneas rojas, la capital y el eje Lac Assal-Lac Abbé son practicables con sentido común y sin conducir de noche.",
    seguridad=[
        "ZONAS A EVITAR (MAEC): franjas fronterizas con Eritrea y con Somalia/Somalilandia, por presencia limitada de las fuerzas del orden y de grupos terroristas, y el archipiélago de las Sept-Frères. El FCDO desaconseja TODO viaje a la frontera con Eritrea (27 de julio de 2026) y Canadá pide evitar los 10 km próximos.",
        "MINAS SIN DESACTIVAR confirmadas por el MAEC en Tadjoura y Obock. Canadá amplía la advertencia a munición sin explotar en las zonas fronterizas con Somalia y Etiopía y pide no abandonar las carreteras asfaltadas en Obock, Tadjoura y Ali Sabieh. Regla operativa: en esas tres regiones no se sale del asfalto, ni para pernoctar.",
        "TERRORISMO: Al Shabaab ha amenazado a Yibuti por su participación en operaciones de paz de la Unión Africana. Objetivos potenciales según el FCDO: nudos de transporte, hoteles, restaurantes, zonas comerciales y actos religiosos o deportivos. Prudencia en los locales frecuentados por occidentales.",
        "DELINCUENCIA: robos y atracos nocturnos en la capital y robos en vehículos aparcados. El MAEC pide no exhibir objetos de valor y desaconseja las playas de Doraleh y Khor Ambado después del atardecer; Canadá añade no visitar playas aisladas a última hora de la tarde. Cámaras y pasaportes, ocultos.",
        "FOTOGRAFÍA: prohibida sobre puertos, edificios públicos, aeropuertos, instalaciones militares y puentes, con confiscación del equipo y posible detención. Con bases de Francia, Estados Unidos (Camp Lemonnier), China, Japón e Italia, más el Destacamento Orión español, conviene no sacar la cámara cerca de nada que parezca militar ni preguntar por ello.",
        "NO CONDUCIR DE NOCHE. Carreteras sin iluminación ni mantenimiento, conducción imprudente, muchos conductores bajo los efectos del khat y controles policiales con alambrada difíciles de ver. El MAEC recomienda 4x4 y convoy de dos vehículos, que es la configuración del proyecto.",
        "MANIFESTACIONES: el MAEC advierte de lanzamientos de piedras contra vehículos de occidentales durante las protestas. Evitar concentraciones y salir de la zona sin discutir.",
        "DROGAS Y KHAT: la posesión de drogas se castiga con 1 a 20 años de prisión. El khat es legal y de consumo masivo en Yibuti pero es ilegal en España: no se puede llevar de vuelta. El alcohol está permitido, aunque el FCDO avisa de que la embriaguez pública puede acarrear hasta 2 años de prisión. Durante el Ramadán, no comer, beber, fumar ni poner música alta en público de día.",
        "LGTBI: no hay prohibición expresa, pero el MAEC recomienda discreción y Canadá señala que las conductas entre personas del mismo sexo pueden perseguirse por leyes de moralidad.",
        "PIRATERÍA: riesgo significativo en el golfo de Adén y el estrecho de Bab el-Mandeb, que el MAEC desaconseja navegar. No afecta a un viaje terrestre, pero descarta cualquier travesía en embarcación pequeña hacia Yemen o Somalia.",
    ],
    agua=[
        "EL AGUA DEL GRIFO NO ES POTABLE. El MAEC y TravelHealthPro coinciden en exigir higiene estricta con agua y alimentos por el riesgo de cólera, presente de forma periódica. Para beber: embotellada o filtro con purificación química o UV.",
        "PARA LLENAR DEPÓSITOS de ducha y lavado, el agua de red de Yibuti ciudad sirve: la capital se abastece por bombeo y desalación para la población y las bases militares extranjeras, y la disponibilidad en la ciudad es razonable. Fuera de la capital la red es escasa y el agua, salobre.",
        "El interior es desierto real. Entre la capital, el Lac Assal, el Grand Bara y el Lac Abbé no hay puntos de agua fiables, y una visita al Lac Abbé son unas 9 horas de conducción desde la capital. Hay que salir con los depósitos llenos y con reserva de emergencia: mínimo 5 litros por persona y día con margen de 48 horas, más lo del perro.",
        "Con más de 45 °C el consumo se dispara: contar tres litros de bebida por persona y día como mínimo. El agua almacenada en bidones al sol se calienta hasta ser imbebible; depósitos a la sombra y bajo el vehículo.",
        "El agua embotellada es cara y no siempre hay stock fuera de la capital: una botella de 1,5 litros ronda los 100 DJF (unos 0,49 €) según HikersBay a 18 de septiembre de 2026. Cargar en Yibuti ciudad para todo el circuito.",
        "El perro bebe lo mismo que los viajeros: embotellada o filtrada, nunca de charcas ni de los pozos salobres del entorno del Lac Abbé.",
    ],
    combustible=[
        "Yibuti no produce hidrocarburos y todo el combustible es importado. Referencia de precio: en torno a 310 DJF por litro de gasolina, unos 1,50 €, según la base de precios de HikersBay actualizada a 18 de septiembre de 2026. Precio del gasóleo POR CONFIRMAR: GlobalPetrolPrices, la fuente habitual, devolvió error en esta revisión.",
        "La red de estaciones se concentra en la capital y en el eje de la RN-1 hacia Galafi, que es la ruta de los camiones etíopes. El aviso oficial de Canadá advierte de que «las gasolineras son escasas y están muy separadas entre sí»: repostar siempre que se pueda y no bajar de medio depósito.",
        "En el tramo etíope de aproximación existe mercado negro de combustible a precios parecidos a los oficiales, según el relato de un overlander; dentro de Yibuti conviene atenerse a estaciones de marca por la calidad del gasóleo.",
        "Dikhil, a 122 km de la capital por la RN-1, es la última población de entidad antes de Galafi y el punto de partida hacia el Lac Abbé: última oportunidad razonable de repostar y comprar agua antes del desierto.",
        "El Delica y el Grenadier deben salir de la capital con depósito lleno y bidones extra para el circuito Lac Assal – Grand Bara – Lac Abbé: no hay servicio en ese triángulo.",
        "Se paga en efectivo y en francos yibutianos; el MAEC avisa de que las tarjetas se rechazan fuera de la capital. Filtros de combustible y de aire de repuesto: el polvo del corredor de camiones y la arena del interior los matan rápido.",
    ],
    experiencias_intro="Yibuti recibe pocos overlanders y casi todos los relatos son de paso, camino de Etiopía o de Somalilandia; el material con vehículo propio es escaso y en buena medida anterior a 2020. Estos son los relatos y guías que aportan datos concretos y utilizables.",
    experiencias=[
        "Entrada por Galafi sin carnet, con permiso temporal de 10 días: Dan Grec, en «The Road Chose Me» (vuelta a África en Jeep), cruzó de Etiopía a Yibuti por Galafi. En la aduana le pusieron pegas por no llevar carnet de passages, pero tras consultar con su superior le emitieron un Temporary Import Permit de 10 días. El visado lo había sacado en la embajada de Yibuti en Adís Abeba por 90 USD, entregado el mismo día. Es el testimonio que sostiene que el CPD no es imprescindible aquí.",
        "La peor carretera asfaltada de África: en el mismo relato, Grec describe la RN-1 como «la carretera asfaltada más rota y destruida que he visto nunca en África», con 60 millas en cinco horas, polvo permanente de más de dos mil camiones diarios y más de 38 °C incluso después de la puesta de sol. La frontera acababa de reabrirse tras unas protestas. Dimensiona bien lo que cuesta cada kilómetro en este país.",
        "El eVisa por tierra, sin respuesta clara: en el foro de Yibuti de Tripadvisor (hilo «Can I enter Djibouti by land with eVisa?», consultas de 2022-2024) un viajero cuenta que la embajada le advirtió de que el eVisa no valdría en un cruce terrestre y le emitió visado en el pasaporte, mientras otro afirma lo contrario citando horarios de los puestos, y un tercero optó por entrar en tren para no arriesgarse. Refleja exactamente la incertidumbre que hay que resolver antes de salir.",
        "Tres pasos desde Etiopía y visado por adelantado: la guía de la agencia local Travel2Djibouti describe Galafi como el paso más usado pero con carretera sin asfaltar y llena de baches, y Dawale (Dewele) y Balho como mejor asfaltados; y afirma que «el visado debe obtenerse por adelantado en una embajada o consulado de Yibuti para los viajeros que llegan de Etiopía» porque el visado a la llegada no existe en las fronteras terrestres con Etiopía.",
        "Nueve horas de coche y 42 °C para llegar al Lac Abbé: el relato de Monsoon Diaries (mayo de 2023) describe la aproximación desde la capital como «nueve horas agotadoras de conducción bajo un sol opresivo de más de 40 °C», en convoy de ocho 4x4, cruzando los llanos de arcilla del Petit y el Grand Bara. El campamento son cabañas afar con catre y mosquitera, duchas destartaladas, nubes de insectos y hienas rondando de noche. Aun así, concluye que las chimeneas de caliza humeantes al amanecer compensan.",
        "La sal del Lac Assal destroza el calzado: Wandersmiles documenta la visita al lago —155 m bajo el nivel del mar, el punto más bajo de África, en uno de los lugares más calurosos del planeta— y da un consejo muy concreto: llevar calzado grueso para bajar al lago si no se quieren acabar los pies hechos trizas. El agua permite flotar pero no hay que tragarla, y la mejor época es de noviembre a enero. Aplicable directo al perro: ahí no pisa.",
        "Temporada de tiburón ballena de octubre-noviembre a febrero: Travel2Djibouti sitúa la temporada entre noviembre y febrero, con diciembre y enero como meses punta, y localiza los avistamientos en Ras Korali, la playa de Arta y el golfo de Tadjoura, con salidas a primera hora de la mañana por el estado del mar. Wandersmiles amplía la ventana a octubre-febrero y habla de unas 4 horas de barco con equipo de snorkel, sin apnea profunda. Coincide con la única ventana climática viable del país.",
        "El ferry del golfo admite coches: la ficha de Petit Futé sobre el ferry Tadjoura-Obock sitúa el embarque en el Port de l'Escale, Route de Venise, al final del muelle que sale del palacio presidencial, y recoge la reseña de un viajero de mayo de 2019: unas dos horas de travesía, ruidoso, con tienda a bordo, y hasta una hora de espera para asegurar plaza si se viaja con vehículo. Es la alternativa a rodear el golfo por carretera.",
        "Yibuti como etapa de tres días en los tours del Cuerno: el operador británico Madventure vende un «Horn of Africa Overland» de 39 días (edición del 24 de julio al 1 de septiembre de 2024, 2.240 £ más 1.000 USD de caja local) en el que Yibuti ocupa tres o cuatro días entre Somalilandia y Etiopía, entrando desde Harar y cubriendo la capital, el Lac Assal y el Lac Abbé. Sirve de referencia de tiempos y de coste, y confirma que el país se ve en poco más de tres días. Llamativo que lo programen en pleno verano.",
        "Gasolineras escasas y nada de noche: el aviso oficial de Canadá resume la parte práctica de conducir aquí —carreteras en mal estado y mal iluminadas, «no viajar después del anochecer», controles policiales con alambrada difíciles de ver, y estaciones de servicio escasas y muy separadas— y añade que se exige permiso internacional de conducir y que el país funciona en efectivo. Es la lista de comprobación mínima antes de salir de la capital.",
    ],
    pendientes=[
        ("Validez del eVisa en frontera terrestre", "Respuesta por escrito de la embajada de Yibuti en París o en Adís Abeba confirmando si el eVisa se acepta en Galafi, Dewele y Loyada. Cerrar con el correo archivado y fechado."),
        ("Duración, coste y prórroga del permiso temporal de importación del vehículo", "Confirmar con la Direction Générale des Douanes yibutiana el plazo estándar, las tasas y el procedimiento de prórroga en la capital. El único dato disponible son 10 días de un relato anterior a 2020."),
        ("Obligatoriedad real del CPD", "Consulta al RACE o a la aduana yibutiana. Cerrar cuando exista confirmación escrita de que se admite la entrada sin carnet mediante permiso temporal."),
        ("Seguro obligatorio de vehículo y precio", "Confirmar si la COMESA Yellow Card contratada en Etiopía se acepta en la frontera yibutiana o si obligan a seguro local, y a qué precio. Cerrar con factura o respuesta de aseguradora."),
        ("Requisitos de entrada del perro y razas prohibidas", "Respuesta escrita del Ministère de l'Agriculture (maepe-rh.dj) con el permiso de importación, los plazos del certificado veterinario y la lista de razas. Cerrar cuando exista documento oficial en francés."),
        ("Clínica veterinaria de referencia en Yibuti ciudad", "Localizar al menos una clínica con nombre, dirección y teléfono verificados por llamada o correo. Hoy no hay ninguna."),
        ("Precio del gasóleo en 2026", "Dato datado en DJF por litro de fuente solvente (GlobalPetrolPrices o prensa local yibutiana). Solo se tiene el precio de gasolina de HikersBay, 310 DJF a 18 de septiembre de 2026."),
        ("Ferry del golfo de Tadjoura: horarios, tarifas y plaza para vehículo", "Confirmar con la autoridad portuaria o el operador. El dato disponible (2 horas, admite coches, hasta 1 hora de espera) es una reseña de viajero de mayo de 2019."),
        ("Estado del paso de Balho y del proyecto de parada única en Galafi", "Noticia o comunicado de 2026 sobre apertura a extranjeros y sobre las obras del One-Stop Border Post. Cerrar con fuente datada."),
        ("Dirección exacta del Viceconsulado Honorario de España en Yibuti ciudad", "Ficha del viceconsulado en exteriores.gob.es o confirmación de la embajada en Adís Abeba. Se tienen dos teléfonos distintos (+253 77 84 49 50 y +253 21 35 63 53) y ninguna dirección postal."),
        ("Procedimiento de autorización de drones ante ACAM", "Respuesta escrita de la Direction de l'Aviation Civile et de la Météorologie (+253 340 151). Mientras no exista, el dron no viaja."),
        ("Camping y pernocta con vehículo en Lac Assal y Lac Abbé", "Confirmar si hay campamento organizado, pernocta tolerada y en qué condiciones de seguridad. Cerrar con iOverlander o testimonio posterior a 2023; solo consta el Lake Abbe Camp de cabañas afar."),
    ],
    sources=SOURCES,
    sources_note="Revisión cerrada el 18 de septiembre de 2026 con las páginas efectivamente abiertas en esa fecha: las recomendaciones de viaje del MAEC llevaban fecha de 6 de mayo de 2026 y las del FCDO de 27 de julio de 2026. Esto es una herramienta de planificación, no una autorización ni un documento oficial: los requisitos de visado, aduana y sanidad animal cambian sin aviso y deben confirmarse con la embajada de Yibuti y con la aduana yibutiana antes de salir. Todo lo marcado «por confirmar» no se ha podido verificar con fuente abierta en esta revisión y no debe darse por bueno.",
    emergency="EMERGENCIA CONSULAR 24 h (Embajada de España en Adís Abeba, competente para Yibuti): +251 911 219 403. Embajada: +251 929 136 159 y +251 111 230 083, emb.addisabeba@maec.es. Viceconsulado Honorario en Yibuti (Josefina Llorente Martín): +253 77 84 49 50 y +253 21 35 63 53. Emergencias locales según el MAEC: policía 19, bomberos y ambulancia 18, comisaría central +253 21 35 38 91. Hôpital Général Peltier: +253 21 35 27 12.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

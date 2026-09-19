# -*- coding: utf-8 -*-
"""Argelia — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Argelia está FUERA DE LA RUTA PREVISTA: la vuelta de 2027 baja por la costa atlántica (Marruecos y Sáhara Occidental) y no cruza el Magreb central. La ficha es INFORMATIVA, para un viaje aparte. La app solo tiene una ficha stub: hay que crearla entera con el formato del piloto de Túnez. Claves que decide la ficha: la frontera con Marruecos lleva CERRADA desde 1994 (y Argelia rompió relaciones con Rabat en 2021), así que no se puede encadenar con la ruta; la entrada realista es por ferry desde España (Almería o Alicante a Orán y Argel) o por Túnez. El visado es PRESENCIAL y difícil, y para el sur (Tassili, Hoggar, Djanet, Timimoun) hay que ir con agencia local autorizada y a menudo con escolta: documenta con fuente fechada qué wilayas lo exigen. Las fronteras con Libia, Níger, Mali y Mauritania están cerradas o desaconsejadas.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/argelia.json y audit/pdi/argelia.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Argel · la Casbah, la bahía y Notre-Dame d'Afrique (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=36.7848925, lon=3.0611962,  # Google Maps: Casbah de Argel
        desc="La medina otomana de Argel trepa desde el puerto hasta la ciudadela en un laberinto de callejones, arcos y casas con patio; es Patrimonio de la Humanidad desde 1992 (ref. 565). La ciudadela de los deys se levantó entre 1516 y 1592 y ocupa 9.000 m2. Arriba, en un acantilado de 124 m sobre la bahía, la basílica neobizantina de Notre-Dame d'Afrique (1858-1872) lleva en el ábside la inscripción «priez pour nous et pour les Musulmans». AVISO: buena parte de la Casbah está en ruina y con derrumbes; conviene entrar con guía local y no fotografiar edificios oficiales.",
        dog_note="Callejeo denso, escaleras y gentío en la Casbah; la basílica y los museos no admiten perros.",
        visit={
            "why": "Es la medina magrebí más vertical y menos turistificada del Mediterráneo, y el mirador de Notre-Dame d'Afrique resume de un vistazo la bahía y el puerto de entrada del ferry.",
            "see": "Ciudadela otomana, mezquita Ketchaoua (1436, catedral en época francesa y devuelta al culto islámico tras la independencia), palacios con patio y la basílica restaurada tras el terremoto de Boumerdès de 2003.",
            "access": "Asfalto hasta la Place des Martyrs; dejar los dos 4x4 en aparcamiento vigilado del bajo Argel o del puerto y subir a pie, porque dentro de la Casbah no se circula. A Notre-Dame d'Afrique se sube en coche por Bologhine con aparcamiento junto a la explanada. El pin marca la puerta baja de la Casbah, no el centroide del barrio. El MAEC no desaconseja Argel capital, pero prohíbe fotografiar instituciones e infraestructuras sensibles.",
            "when": "Primavera y otoño; la Casbah por la mañana y la basílica al atardecer, con la luz de poniente sobre la bahía.",
            "skip": "Si se viaja sin guía local y con prisa: perderse en la Casbah sin acompañante es incómodo y poco productivo.",
        },
        links=[
            {"label": "UNESCO · Kasbah of Algiers", "url": "https://whc.unesco.org/en/list/565"},
            {"label": "Wikipedia · Casbah of Algiers", "url": "https://en.wikipedia.org/wiki/Casbah_of_Algiers"},
            {"label": "Wikipedia · Notre-Dame d'Afrique", "url": "https://en.wikipedia.org/wiki/Notre-Dame_d%27Afrique"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Casbah_of_Algiers,_patio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Casbah_of_Algiers,_patio.jpg",
                "credit": "toufik Lerari · CC BY-SA 2.0",
                "caption": "Patio de una casa de la Casbah de Argel.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Abricot_march%C3%A9_de_la_casbah_d'Alger.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Abricot_march%C3%A9_de_la_casbah_d'Alger.JPG",
                "credit": "Reda Kerbush · CC BY-SA 3.0",
                "caption": "Mercado de albaricoques en la Casbah.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Alger_monochrome.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Alger_monochrome.jpg",
                "credit": "Cherif Meriam · CC BY-SA 4.0",
                "caption": "Uno de los grandes bulevares de Argel.",
            },
        ],
    ),
    dict(
        n=2, name="Tipasa · ruinas púnicas y romanas sobre el mar (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="por confirmar", time="medio día",
        lat=36.5906719, lon=2.4433723,  # Google Maps: Tipasa (parque arqueológico)
        desc="Antiguo emporio púnico convertido por Claudio en colonia militar, Tipasa llegó a 20.000 habitantes en el siglo IV y fue un foco cristiano con TRES BASÍLICAS. Las ruinas ocupan dos parques arqueológicos que caen directamente sobre el Mediterráneo: anfiteatro, basílica judicial, templos y la villa de los Frescos. Inscrita por la UNESCO en 1982 (ref. 193) junto con el Mausoleo real de Mauritania, y estuvo en la lista de Patrimonio en Peligro entre 2002 y 2006. Hay poca sombra: llevar agua.",
        dog_note="Recinto arqueológico vallado con taquilla; no hay norma publicada sobre perros: preguntar en la entrada.",
        visit={
            "why": "Es el yacimiento romano más fotogénico de Argelia porque las columnas terminan en el acantilado y el mar entra en el encuadre.",
            "see": "Los dos parques arqueológicos, la basílica cristiana, el anfiteatro, el templo anónimo y los mosaicos; la ciudad fue arrasada por los vándalos en 430, reconstruida por los bizantinos y abandonada tras la conquista omeya.",
            "access": "Autovía desde Argel (unos 70 km) y luego calle urbana; aparcamiento de superficie junto a la entrada, suficiente para dos 4x4. El pin marca la taquilla del parque arqueológico este, no el casco urbano. La wilaya de Tipasa aparece en zona naranja del aviso francés, sin restricción específica de acceso al yacimiento.",
            "when": "Primavera y otoño; a media mañana o a última hora, cuando la luz rasante saca el color a la piedra.",
            "skip": "Si ya se ha visto Djémila y Timgad y se va corto de días: Tipasa es la más pequeña de las tres.",
        },
        links=[
            {"label": "UNESCO · Tipasa", "url": "https://whc.unesco.org/en/list/193"},
            {"label": "Wikipedia · Tipaza", "url": "https://en.wikipedia.org/wiki/Tipaza"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tipasa_22.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tipasa_22.jpg",
                "credit": "Yelles · CC BY-SA 3.0",
                "caption": "Ruinas romanas de Tipasa sobre el Mediterráneo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Large_Christian_Basilica_(Tipasa)_03.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Large_Christian_Basilica_(Tipasa)_03.jpg",
                "credit": "Bernard Gagnon · CC BY 4.0",
                "caption": "La gran basílica cristiana de Tipasa.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tipasa,_Mauretania_Caesariensis,_Algeria_-_52574495528.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tipasa,_Mauretania_Caesariensis,_Algeria_-_52574495528.jpg",
                "credit": "Carole Raddato · CC BY-SA 2.0",
                "caption": "Tipasa, en la Mauretania Cesariense.",
            },
        ],
    ),
    dict(
        n=3, name="Mausoleo real de Mauritania · la «Tumba de la Cristiana» (UNESCO)", cat="Patrimonio UNESCO", prio="Media",
        dog="por confirmar", time="medio día",
        lat=36.5749611, lon=2.5527391,  # Google Maps: Mausoleo real de Mauritania
        desc="Túmulo real beréber del año 3 a. C. sobre la meseta del Sahel, a 11 km al sureste de Tipasa. Base cuadrada de unos 60 m de lado y unos 30-32 m de altura actual (los 40 m originales se perdieron por saqueos y cañoneos). Se atribuye a Juba II y Cleopatra Selene II, aunque LOS RESTOS YA NO ESTÁN ALLÍ. Forma parte de la inscripción UNESCO de Tipasa. El nombre árabe Kbor er Roumia y el francés Tombeau de la Chrétienne son un malentendido: nada tiene de cristiano.",
        dog_note="Recinto vallado con guarda; sin norma publicada, preguntar en la puerta.",
        visit={
            "why": "Es el monumento funerario númida mejor conservado del Magreb central y se ve desde kilómetros, plantado solo en la meseta.",
            "see": "El tambor escalonado con sesenta columnas jónicas adosadas, la falsa puerta con la cruz que dio origen al nombre y la vista sobre el Sahel y el mar.",
            "access": "Desvío asfaltado desde la N11 por Sidi Rached; pista corta de acceso y explanada amplia donde caben dos 4x4 sin problema. El pin marca el aparcamiento al pie del túmulo. Horario y entrada no publicados por una fuente oficial: POR CONFIRMAR sobre el terreno.",
            "when": "Fin de la tarde, con luz lateral sobre el tambor de piedra; evitar el mediodía de verano, no hay sombra.",
            "skip": "Si el tiempo aprieta y se ha visto Tipasa: son 20 minutos de visita real sobre una hora de desvío.",
        },
        links=[
            {"label": "UNESCO · Tipasa (propiedad en serie)", "url": "https://whc.unesco.org/en/list/193"},
            {"label": "Wikipedia · Royal Mausoleum of Mauretania", "url": "https://en.wikipedia.org/wiki/Royal_Mausoleum_of_Mauretania"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Royal_Mausoleum_of_Mauretania_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Royal_Mausoleum_of_Mauretania_01.jpg",
                "credit": "Bernard Gagnon · CC BY 4.0",
                "caption": "El mausoleo real de Mauritania, la «Tumba de la Cristiana».",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Royal_Mausoleum_of_Mauretania_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Royal_Mausoleum_of_Mauretania_02.jpg",
                "credit": "Bernard Gagnon · CC BY 4.0",
                "caption": "El túmulo escalonado desde el sur.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Royal_Mausoleum_of_Mauretania_2014.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Royal_Mausoleum_of_Mauretania_2014.jpg",
                "credit": "Dan Sloan · CC BY-SA 2.0",
                "caption": "El mausoleo sobre la meseta de Sidi Rached.",
            },
        ],
    ),
    dict(
        n=4, name="Cherchell · el museo y el litoral romano", cat="Cultura", prio="Media",
        dog="prohibido", time="medio día",
        lat=36.6083828, lon=2.1911359,  # Google Maps: Museo arqueológico de Cherchell
        desc="La púnica Iol fue refundada por Juba II como Caesarea Mauretaniae y llegó a ser capital de provincia; hoy es un puerto tranquilo a 89 km al oeste de Argel. Su museo arqueológico guarda ALGUNAS DE LAS MEJORES ESCULTURAS GRIEGAS Y ROMANAS DE ÁFRICA, con piezas como el Neptuno y la Venus halladas en el propio yacimiento. Del teatro, el anfiteatro y las termas marítimas queda poco: sirvieron de cantera en el siglo XIX. Hay mosaicos de las Tres Gracias y de la vendimia.",
        dog_note="El museo arqueológico no admite animales; queda el paseo marítimo.",
        visit={
            "why": "Por el museo, que concentra lo que en el yacimiento ya no se ve, y por el contraste entre el puerto vivo y los restos romanos metidos entre casas.",
            "see": "Museo arqueológico de Cherchell-Caesarea, restos del foro, el acueducto, las termas junto al mar y el anfiteatro rectangular de esquinas redondeadas.",
            "access": "Carretera costera N11 desde Tipasa, 25 km de curvas; aparcamiento en calle junto al museo, justo para dos vehículos largos. El pin marca la puerta del museo. Horario y tarifa no publicados por fuente oficial verificable: POR CONFIRMAR.",
            "when": "Mañana, cuando el museo está abierto; la costa de Cherchell gana con el mar en calma de primavera.",
            "skip": "Si no interesa la escultura antigua: las ruinas al aire libre están muy arrasadas.",
        },
        links=[
            {"label": "Wikipedia · Cherchell", "url": "https://en.wikipedia.org/wiki/Cherchell"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cherchell_Harbour_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cherchell_Harbour_01.jpg",
                "credit": "Bernard Gagnon · CC BY 4.0",
                "caption": "El puerto de Cherchell, la antigua Caesarea.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cherchell_Harbour_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cherchell_Harbour_02.jpg",
                "credit": "Bernard Gagnon · CC BY 4.0",
                "caption": "La bahía de Cherchell.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Rue_Allioui_Belkacem_(Cherchell).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Rue_Allioui_Belkacem_(Cherchell).jpg",
                "credit": "Bernard Gagnon · CC BY 4.0",
                "caption": "Calle del centro de Cherchell.",
            },
        ],
    ),
    dict(
        n=5, name="Constantina · la ciudad de los puentes y las gargantas del Rhummel", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=36.3723642, lon=6.6141792,  # Google Maps: Puente Sidi M'Cid (Constantina)
        desc="La antigua Cirta, fundada hacia el 203 a. C., se asienta a 694 m sobre un peñón partido por la garganta del Rhummel, y solo se sostiene gracias a sus puentes. El de Sidi M'Cid, colgante y de 168 m, y el viaducto de Sidi Rached, de 447 m y VEINTISIETE ARCOS, son ambos de 1912. Es una ciudad grande, con talleres, combustible y hoteles, buena base logística del este. El aviso francés sitúa la wilaya de Constantina entre las de riesgo elevado: evitar desplazamientos nocturnos por carreteras secundarias.",
        dog_note="Los puentes y miradores son vía pública; con correa corta y sin entrar en mezquitas ni museos.",
        visit={
            "why": "Porque el urbanismo es el espectáculo: una ciudad de medio millón de habitantes colgada sobre un tajo y cosida con puentes de principios del siglo XX.",
            "see": "Puente colgante de Sidi M'Cid, viaducto de Sidi Rached, el fondo de la garganta del Rhummel y el casco antiguo sobre el peñón.",
            "access": "Autopista Este-Oeste hasta Constantina; aparcar fuera del centro y moverse a pie, el tráfico interior es denso. El pin marca la cabecera del puente de Sidi M'Cid, que es donde se aparca y se cruza andando. Profundidad exacta de la garganta: POR CONFIRMAR, la Wikipedia no la da.",
            "when": "Todo el año; la mejor luz sobre los puentes es la de primera hora de la mañana.",
            "skip": "Si se busca solo arqueología: aquí lo que se visita es la ciudad, no un yacimiento.",
        },
        links=[
            {"label": "Wikipedia · Constantine, Algeria", "url": "https://en.wikipedia.org/wiki/Constantine,_Algeria"},
            {"label": "France Diplomatie · Algérie (sécurité)", "url": "https://www.diplomatie.gouv.fr/fr/conseils-aux-voyageurs/conseils-par-pays-destination/algerie/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pont_de_Sidi_M'Cid_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pont_de_Sidi_M'Cid_01.jpg",
                "credit": "Bernard Gagnon · CC BY 4.0",
                "caption": "El puente de Sidi M'Cid sobre las gargantas del Rhummel.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pont_El_Kantara_(Constantine).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pont_El_Kantara_(Constantine).jpg",
                "credit": "Bernard Gagnon · CC BY 4.0",
                "caption": "El puente de El Kantara, Constantina.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Rhummel_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Rhummel_2.jpg",
                "credit": "LBM1948 · CC BY-SA 4.0",
                "caption": "Las cascadas del Rhummel bajo la ciudad.",
            },
        ],
    ),
    dict(
        n=6, name="Timgad · la ciudad romana del Aurés (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=35.4944079, lon=6.4683965,  # Google Maps: Timgad
        desc="Colonia fundada por Trajano hacia el año 100 d. C. para veteranos, Timgad es el manual de urbanismo romano hecho piedra: retícula perfecta de cardo y decumano sobre la meseta del Aurés. Conserva el arco de Trajano de 12 m, un teatro de 3.500 plazas todavía en uso y UNA BIBLIOTECA PARA UNOS 3.000 ROLLOS, rareza en el mundo romano. Patrimonio de la Humanidad desde 1982 (ref. 194). No hay sombra ni agua dentro del recinto: entrar temprano y salir antes del mediodía.",
        dog_note="Yacimiento vallado, sin sombra y con losas ardiendo en verano; mejor dejarlo en el vehículo a la sombra.",
        visit={
            "why": "Es la ciudad romana de trazado ortogonal mejor legible del Mediterráneo, y se recorre entera a pie sin vallas interiores.",
            "see": "Arco de Trajano, foro, teatro de 3.500 plazas excavado en la ladera, las termas, la biblioteca y el museo de mosaicos junto a la entrada.",
            "access": "Asfalto desde Batna por la N88, unos 35 km; explanada de tierra frente a la entrada con sitio de sobra para dos 4x4. El pin marca la taquilla del yacimiento. El Aurés aparece citado en el aviso francés entre las zonas de riesgo elevado: no pernoctar en descampado ni circular de noche.",
            "when": "Marzo-mayo y octubre-noviembre; primera hora de la mañana. En verano el llano supera holgadamente los 35 grados.",
            "skip": "Nunca si se viene al este; solo si el calor es extremo y no se puede madrugar.",
        },
        links=[
            {"label": "UNESCO · Timgad", "url": "https://whc.unesco.org/en/list/194"},
            {"label": "Wikipedia · Timgad", "url": "https://en.wikipedia.org/wiki/Timgad"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Timgad_Ruins_Panorama.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Timgad_Ruins_Panorama.jpg",
                "credit": "Hamza-sia · CC BY-SA 3.0",
                "caption": "Panorámica de Timgad, la ciudad romana del Aurés.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Timgad_%D8%AA%D9%8A%D9%85%D9%82%D8%A7%D8%AF_4.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Timgad_%D8%AA%D9%8A%D9%85%D9%82%D8%A7%D8%AF_4.jpg",
                "credit": "Habib kaki · CC BY-SA 4.0",
                "caption": "El arco de Trajano en Timgad.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Timgad_ville.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Timgad_ville.jpg",
                "credit": "Yelles · CC BY-SA 3.0",
                "caption": "La plaza y el foro de Timgad.",
            },
        ],
    ),
    dict(
        n=7, name="Djémila · Cuicul, la ciudad romana de montaña (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=36.3138406, lon=5.7373838,  # Google Maps: Djémila
        desc="Cuicul se fundó bajo Nerva (96-98 d. C.) en un espolón A 900 M DE ALTITUD, y por eso su plano se retuerce para adaptarse a la montaña en lugar de imponer la retícula habitual: ahí está su valor. Conserva foro, templos, basílicas, el arco de Caracalla (216), el templo de la Gens Septimia (229) y un barrio cristiano del siglo V con tres basílicas y baptisterio. El museo reúne una colección notable de mosaicos. Recibe unos 30.000 visitantes al año: se recorre con calma y casi solo.",
        dog_note="Recinto arqueológico con taquilla y museo de mosaicos; el museo no admite animales.",
        visit={
            "why": "Porque es la excepción que confirma la regla romana: una ciudad que se pliega al relieve, y con las mejores vistas de las tres grandes de Argelia.",
            "see": "Foro severiano, arco de Caracalla, templo de la Gens Septimia, teatro colgado de la ladera, barrio cristiano y museo de mosaicos.",
            "access": "Desvío asfaltado desde Sétif hacia el norte, unos 50 km de carretera de montaña; aparcamiento junto al museo, amplio, dos 4x4 sin problema. El pin marca la entrada y el museo. Propiedad de 30,6 ha según la UNESCO: calcular dos o tres horas de paseo.",
            "when": "Primavera y otoño. En invierno hace frío y llueve a 900 m; en verano hay que madrugar.",
            "skip": "Si hay que elegir una sola ciudad romana y se prefiere la retícula limpia de Timgad.",
        },
        links=[
            {"label": "UNESCO · Djémila", "url": "https://whc.unesco.org/en/list/191"},
            {"label": "Wikipedia · Djemila", "url": "https://en.wikipedia.org/wiki/Djemila"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Roman_Ruins_of_Djemila_in_S%C3%A9tif,_Algeria.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Roman_Ruins_of_Djemila_in_S%C3%A9tif,_Algeria.jpg",
                "credit": "Alioueche Mokhtar · CC BY-SA 4.0",
                "caption": "Las ruinas de Cuicul, en Djémila.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Djemila_0610510.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Djemila_0610510.jpg",
                "credit": "Yelles · CC BY-SA 3.0",
                "caption": "El pueblo de Djémila y el yacimiento.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Algerie_Djemila_05.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Algerie_Djemila_05.jpg",
                "credit": "Paebi · CC BY-SA 4.0",
                "caption": "Columnas del foro de Djémila.",
            },
        ],
    ),
    dict(
        n=8, name="Orán · Santa Cruz, la Blanca y el frente de mar", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=35.6987388, lon=-0.6349319,  # Google Maps: Orán (el fuerte de Santa Cruz no figura como objeto)
        desc="Segunda ciudad del país y PUERTA DE ENTRADA REALISTA DEL VIAJE: los ferris desde Almería y Alicante atracan aquí. Fue española entre 1509 y 1708 y otra vez entre 1732 y 1792, y de ahí viene el fuerte de Santa Cruz, levantado en 1563 por Álvaro de Bazán en lo alto del monte Aïdour-Murdjadjo, a más de 300 m sobre el mar. Desde la explanada se domina toda la bahía. Abajo, la place du 1er Novembre y el teatro regional marcan el centro colonial. Ciudad grande: hay talleres, repuestos y gasóleo.",
        dog_note="Calle y paseo marítimo sí, con correa; el fuerte y la capilla de Santa Cruz están vallados y no hay norma publicada.",
        visit={
            "why": "Es el punto de desembarco y de arranque logístico, y además tiene el mejor mirador urbano de la costa argelina.",
            "see": "Fuerte de Santa Cruz y su capilla sobre el Murdjadjo, la bahía, el puerto, la place du 1er Novembre con el ayuntamiento y el teatro regional Abdelkader Alloula.",
            "access": "Del puerto al centro son minutos; al fuerte se sube por carretera asfaltada de curvas con aparcamiento en la explanada superior, suficiente para dos 4x4. El pin marca el fuerte, no el centro de la ciudad. Trámites de aduana del vehículo en el puerto: contar medio día.",
            "when": "Primavera y otoño; la subida a Santa Cruz al atardecer, con la ciudad iluminada al fondo.",
            "skip": "No se descarta: es el punto de entrada y salida del país por ferry.",
        },
        links=[
            {"label": "Wikipedia · Oran", "url": "https://en.wikipedia.org/wiki/Oran"},
            {"label": "MAEC · Recomendaciones de viaje, Argelia", "url": "https://www.exteriores.gob.es/Embajadas/argel/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ORAN_City_%26_Coast.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ORAN_City_%26_Coast.jpg",
                "credit": "Benba.d.mourad · CC BY-SA 4.0",
                "caption": "Orán y su golfo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Oran_Santa_Cruz.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Oran_Santa_Cruz.JPG",
                "credit": "Autor desconocido · Public domain",
                "caption": "El fuerte de Santa Cruz sobre el Murdjadjo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fort_Santa_Cruz_Oran_5.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fort_Santa_Cruz_Oran_5.jpg",
                "credit": "Ramy Maalouf · CC BY-SA 3.0",
                "caption": "La capilla de Santa Cruz.",
            },
        ],
    ),
    dict(
        n=9, name="Tremecén · Mansourah, Sidi Bumedián y el arte hispanomusulmán", cat="Cultura", prio="Alta",
        dog="prohibido", time="1 noche",
        lat=34.8778581, lon=-1.2896025,  # Google Maps: Mezquita de Sidi Boumediene (Tlemcen)
        desc="A 842 m de altitud, Tremecén fue capital del reino zayánida entre 1236 y 1554 y es el gran depósito de arte hispanomusulmán al sur del Estrecho. La Gran Mezquita SE TERMINÓ EN 1136 y es el ejemplo almorávide más notable que queda en pie. Fuera del casco, el mausoleo y la mezquita de Sidi Bumedián y las murallas arruinadas de Mansourah, levantadas por los meriníes durante el asedio de la ciudad. Altura del alminar de Mansourah y fechas exactas: POR CONFIRMAR, la Wikipedia consultada no las da.",
        dog_note="El conjunto gira en torno a mezquitas y mausoleos en uso; los animales no entran en recintos religiosos.",
        visit={
            "why": "Porque el vínculo con al-Ándalus se ve en el yeso y la cerámica, y porque es la parada natural antes o después de Orán.",
            "see": "Gran Mezquita almorávide de 1136, conjunto de Sidi Bumedián en El Eubbad, ruinas y alminar partido de Mansourah, y el entorno de cascadas y pinares de la meseta de Lalla Setti.",
            "access": "Autopista desde Orán, unas dos horas; los tres focos (centro, El Eubbad y Mansourah) están separados, conviene moverse en coche entre ellos. Aparcamiento de calle. El pin marca la puerta del conjunto de Sidi Bumedián. Vestimenta discreta en los recintos religiosos.",
            "when": "Primavera; en verano se suda y en invierno llueve. Media mañana, fuera de las horas de oración.",
            "skip": "Si no interesan la arquitectura islámica ni la huella andalusí: es un desvío largo hacia el oeste.",
        },
        links=[
            {"label": "Wikipedia · Tlemcen", "url": "https://en.wikipedia.org/wiki/Tlemcen"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tomb_of_Sidi_Boumediene_03.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tomb_of_Sidi_Boumediene_03.jpg",
                "credit": "Bernard Gagnon · CC BY 4.0",
                "caption": "La tumba de Sidi Boumediene, en Tlemcen.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tlemcen_-_20240424_150134.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tlemcen_-_20240424_150134.jpg",
                "credit": "Riad Salih · CC BY 4.0",
                "caption": "Vista de Tlemcen desde el túnel de acceso.",
            },
        ],
    ),
    dict(
        n=10, name="Valle del M'Zab · Ghardaïa y las cinco ciudades ibadíes (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=32.4943741, lon=3.64446,  # Google Maps: Ghardaïa
        desc="Cinco ksour fundados ENTRE 1012 Y 1350 por los mozabitas ibadíes —Ghardaïa, Beni Isguen, Melika, Bounoura y El Atteuf, la más antigua— forman una pentápolis de casas apiñadas en cono alrededor de la mezquita, a unos 600 km al sur de Argel. Es Patrimonio de la Humanidad desde 1982 (ref. 188) y fue referencia declarada de Le Corbusier. AVISO: Beni Isguen prohíbe a los no mozabitas el acceso a varias zonas y a cualquier extranjero pernoctar dentro de sus murallas; se entra con guía local de la puerta.",
        dog_note="Ksour habitados, muy conservadores, con mezquitas y normas de acceso estrictas; el perro estorba.",
        visit={
            "why": "Es el urbanismo sahariano más coherente que existe y sigue vivo, no es un decorado: gente, mercado y agua repartida según reglas centenarias.",
            "see": "El zoco en cono de Ghardaïa, los alminares de barro sin adornos, el laberinto blanco de Beni Isguen y el palmeral con su sistema de reparto de la crecida.",
            "access": "Carretera nacional asfaltada desde Argel o desde Ouargla; aparcamiento en la parte baja de Ghardaïa, cerca del mercado. Hay aeropuerto (Noumérat-Moufdi Zakaria). El pin marca la plaza del mercado de Ghardaïa, punto de encuentro habitual con los guías. En los ksour se entra a pie y con guía; foto restringida en muchas calles.",
            "when": "Octubre a abril; el verano sahariano es inviable. Mercado por la mañana.",
            "skip": "En pleno verano o si no se acepta ir acompañado por un guía local dentro de los ksour.",
        },
        links=[
            {"label": "UNESCO · M'Zab Valley", "url": "https://whc.unesco.org/en/list/188"},
            {"label": "Wikipedia · M'zab", "url": "https://en.wikipedia.org/wiki/M%27zab"},
            {"label": "Wikipedia · Ghardaia", "url": "https://en.wikipedia.org/wiki/Ghardaia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ksar_Ghardaia_place_march%C3%A9_1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ksar_Ghardaia_place_march%C3%A9_1.jpg",
                "credit": "Camille Gillet · CC BY-SA 4.0",
                "caption": "El ksar de Ghardaïa desde la plaza del mercado.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Vue_Ghardaia_Melika.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Vue_Ghardaia_Melika.jpg",
                "credit": "Camille Gillet · CC BY-SA 4.0",
                "caption": "El ksar de Melika, en el valle del M'Zab.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ksar_Beni_Isguen_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ksar_Beni_Isguen_2.jpg",
                "credit": "Camille Gillet · CC BY-SA 4.0",
                "caption": "Beni Isguen, la más cerrada de las cinco ciudades.",
            },
        ],
    ),
    dict(
        n=11, name="Timimoun y el Gourara · las foggaras y el ksar rojo", cat="Cultura", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=29.2616911, lon=0.2415964,  # Google Maps: Timimoun
        desc="La «oasis roja» del Gourara, a 288 m de altitud y 33.060 habitantes, debe su nombre AL OCRE ROJO DE SUS MUROS de adobe. Vive del agua de las foggaras, galerías drenantes de tipo qanat que suman miles de kilómetros en la región del Gourara y el Tuat y que ya se usaban con seguridad en el siglo XI. Al noroeste se abre una sebja salada. AVISO: Timimoun figura entre las wilayas del «Gran Sur» en las que el visado a la llegada solo se concede a viajes organizados por AGENCIA AUTORIZADA.",
        dog_note="Oasis y pistas al aire libre; fuera de mezquitas y casas particulares no hay problema, con correa.",
        visit={
            "why": "Por la arquitectura de tierra roja y por entender de primera mano un sistema hidráulico milenario que todavía riega el palmeral.",
            "see": "El ksar y el paseo colgado sobre la sebja, las bocas de las foggaras y sus peines de reparto de caudal, el palmeral y los ksour circundantes del Gourara.",
            "access": "Asfalto desde Adrar y desde El Menia; las visitas a las foggaras se hacen por pista corta y conviene guía local. Aparcamiento sin problema para dos 4x4. El pin marca el ksar de Timimoun. Embajada de Argelia en Bruselas (medida de visado del Gran Sur): el visado a la llegada se concede EXCLUSIVAMENTE a viajes organizados por AGENCIA DE VIAJES AUTORIZADA, para las wilayas de Tamanrasset, Illizi, Djanet, Tinduf, Adrar, Timimoun, Béchar, Beni Abbès, Bordj Badji Mokhtar, In Salah y Touggourt; validez máxima 30 días y autorización de embarque con código QR emitida por la agencia.",
            "when": "Noviembre a marzo; el sol de mediodía en el Gourara es durísimo.",
            "skip": "Si no se ha contratado agencia autorizada para el Gran Sur y se viaja con vehículo propio: los controles pueden devolverte.",
        },
        links=[
            {"label": "Wikipedia · Timimoun", "url": "https://en.wikipedia.org/wiki/Timimoun"},
            {"label": "Wikipedia · Foggara (qanat)", "url": "https://en.wikipedia.org/wiki/Foggara"},
            {"label": "Embajada de Argelia · visado del Gran Sur", "url": "https://embbrussels.mfa.gov.dz/announcements/algerian-great-south-tourist-destination-new-visa-issuance-measures"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Entr%C3%A9e_de_Timimoun_%D8%AA%D9%8A%D9%85%D9%8A%D9%85%D9%88%D9%86.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Entr%C3%A9e_de_Timimoun_%D8%AA%D9%8A%D9%85%D9%8A%D9%85%D9%88%D9%86.jpg",
                "credit": "Habib kaki · CC BY-SA 4.0",
                "caption": "La entrada roja de Timimoun.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Village_%C3%A0_Timimoun,_Adrar,_Alg%C3%A9rie.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Village_%C3%A0_Timimoun,_Adrar,_Alg%C3%A9rie.jpg",
                "credit": "Hakou Elarabi · CC BY-SA 4.0",
                "caption": "Antiguo pueblo zenete del Gourara.",
            },
        ],
    ),
    dict(
        n=12, name="Taghit y el Grand Erg Occidental · el palmeral bajo la duna", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=30.9169949, lon=-2.0295594,  # Google Maps: Taghit
        desc="Oasis de 6.317 habitantes a 623 m y 95 km de Béchar, con el ksar viejo encaramado sobre el palmeral y, justo detrás, el frente de dunas del Grand Erg Occidental, que se extiende hacia el este siguiendo el oued Zouzfana. En los alrededores hay MUCHOS GRABADOS RUPESTRES NEOLÍTICOS, el otro motivo de visita. Es la postal clásica del Sáhara argelino y la más accesible desde el norte. AVISO: Béchar figura entre las wilayas del Gran Sur sujetas a visado por agencia autorizada.",
        dog_note="Dunas y palmeral al aire libre; ojo con la arena a 60 grados al mediodía y con las almohadillas.",
        visit={
            "why": "Porque es el encuentro más limpio entre erg y palmeral de todo el país, y se llega por asfalto sin meterse en el desierto profundo.",
            "see": "El ksar de adobe sobre el oasis, el frente de dunas al atardecer y los paneles de grabados neolíticos del entorno.",
            "access": "Asfalto desde Béchar (95 km) por la carretera del oued Zouzfana; aparcamiento amplio al pie del ksar y explanadas de arena firme para los dos 4x4. El pin marca el ksar viejo. Embajada de Argelia en Bruselas (medida de visado del Gran Sur): el visado a la llegada se concede EXCLUSIVAMENTE a viajes organizados por AGENCIA DE VIAJES AUTORIZADA, para las wilayas de Tamanrasset, Illizi, Djanet, Tinduf, Adrar, Timimoun, Béchar, Beni Abbès, Bordj Badji Mokhtar, In Salah y Touggourt; validez máxima 30 días y autorización de embarque con código QR emitida por la agencia. Sahara Overland (página Argelia, con notas de 2025-2026): la escolta de agencia es oficialmente obligatoria para circular con vehículo propio hacia el extremo sur (120-150 EUR/día con coche de la agencia, 90 EUR/día si el escolta va en tu vehículo) y la gendarmería puede imponer escolta de carretera en cualquier control.",
            "when": "Noviembre a marzo; dunas al amanecer y al atardecer, nunca al mediodía.",
            "skip": "Entre mayo y septiembre, o si no se lleva agencia y permiso en regla para las wilayas del sur.",
        },
        links=[
            {"label": "Wikipedia · Taghit", "url": "https://en.wikipedia.org/wiki/Taghit"},
            {"label": "Embajada de Argelia · visado del Gran Sur", "url": "https://embbrussels.mfa.gov.dz/announcements/algerian-great-south-tourist-destination-new-visa-issuance-measures"},
            {"label": "Sahara Overland · Algeria", "url": "https://sahara-overland.com/algeria-3/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Vue_de_Taghit.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Vue_de_Taghit.jpg",
                "credit": "Mohamed Benguedda · CC BY-SA 3.0",
                "caption": "El ksar de Taghit y su palmeral.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Taghit_-_Bechar.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Taghit_-_Bechar.jpg",
                "credit": "Yane Casouf · CC BY-SA 4.0",
                "caption": "La duna sobre Taghit.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Taghit_sable._Jpg.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Taghit_sable._Jpg.jpg",
                "credit": "Nazim Bellifa · CC BY-SA 4.0",
                "caption": "Arena dorada del Gran Erg Occidental.",
            },
        ],
    ),
    dict(
        n=13, name="Tassili n'Ajjer · el arte rupestre del Sáhara (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="4–7 noches",
        lat=24.554151, lon=9.485429,  # Google Maps: Djanet (la oficina del parque del Tassili no figura como objeto)
        desc="Meseta de arenisca de 72.000 km2 en el sureste sahariano, parque nacional desde 1972, Patrimonio de la Humanidad desde 1982 (ref. 179) y reserva de la biosfera. Guarda MÁS DE 15.000 GRABADOS Y PINTURAS identificados, con dataciones que arrancan hace unos 12.000 años y documentan un Sáhara verde con elefantes, jirafas y ganado. También conserva el ciprés del Sáhara, Cupressus dupreziana, de los seres vivos más longevos. AVISO: solo se visita con agencia autorizada y hay controles militares en los accesos.",
        dog_note="Parque nacional y travesías de varios días a pie o en camello con agencia; ninguna agencia acepta perro.",
        visit={
            "why": "Es el mayor museo de arte prehistórico al aire libre del planeta y el argumento serio para venir a Argelia.",
            "see": "Paneles pintados del periodo bovidiense, bosques de piedra del Tadrart y la Tassili propiamente dicha, gargantas, gueltas y los cipreses relictos; punto más alto, el Adrar Afao, 2.158 m.",
            "access": "Se accede desde Djanet con vehículos y guías de la agencia; la subida a la meseta es a pie o con mulas y dura varios días. MAEC, ficha de Argelia, ÚLTIMA ACTUALIZACIÓN 7-5-2026 (consultada 13-9-2026): los no residentes deben comunicar sus desplazamientos fuera de su wilaya a la gendarmería o comisaría más próxima y, si el viaje recorre VARIAS WILAYAS, la agencia de viajes debe haber obtenido AUTORIZACIÓN PREVIA de las autoridades locales; en zonas desérticas el MAEC recomienda viajar en grupo y con guía. Embajada de Argelia en Bruselas (medida de visado del Gran Sur): el visado a la llegada se concede EXCLUSIVAMENTE a viajes organizados por AGENCIA DE VIAJES AUTORIZADA, para las wilayas de Tamanrasset, Illizi, Djanet, Tinduf, Adrar, Timimoun, Béchar, Beni Abbès, Bordj Badji Mokhtar, In Salah y Touggourt; validez máxima 30 días y autorización de embarque con código QR emitida por la agencia. Foro de viajeros: la meseta del Tassili y el Tadrart Rouge exigen guía y hay control militar a la entrada. El pin marca la oficina del parque en Djanet, no la meseta.",
            "when": "Noviembre a marzo. Fuera de esa ventana el calor hace inviable la travesía a pie.",
            "skip": "Si no se contrata agencia autorizada, o si se viaja con el perro: sencillamente no es compatible.",
        },
        links=[
            {"label": "UNESCO · Tassili n'Ajjer", "url": "https://whc.unesco.org/en/list/179"},
            {"label": "Wikipedia · Tassili n'Ajjer", "url": "https://en.wikipedia.org/wiki/Tassili_n%27Ajjer"},
            {"label": "MAEC · Recomendaciones de viaje, Argelia", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=argelia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_Tanzoumaitak_cave_painting_in_Tassili_n'ajjer.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_Tanzoumaitak_cave_painting_in_Tassili_n'ajjer.jpg",
                "credit": "IssamBarhoumi · CC BY-SA 4.0",
                "caption": "Pintura rupestre de Tanzoumaitak, en el Tassili n'Ajjer.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tassili_n'Ajjer-Tamghit_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tassili_n'Ajjer-Tamghit_02.jpg",
                "credit": "IssamBarhoumi · CC BY-SA 4.0",
                "caption": "La meseta de Tamghit, en el Tassili.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Esprit_nomade.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Esprit_nomade.JPG",
                "credit": "Hamdanmourad · CC BY-SA 3.0",
                "caption": "Tuareg en la duna de Timerzouga.",
            },
        ],
    ),
    dict(
        n=14, name="Hoggar · Tamanrasset, el Assekrem y los picos volcánicos", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="3–5 noches",
        lat=23.3047222, lon=6.3244444,  # Google Maps: Assekrem
        desc="El macizo del Hoggar es un campo volcánico sobre roca metamórfica de unos 2.000 MILLONES DE AÑOS, con agujas que son chimeneas de volcanes desmantelados por la erosión. Corona el monte Tahat, 2.908 m, techo de Argelia. El Assekrem, a 2.726 m, es el mirador clásico: allí levantó Charles de Foucauld su ermita en 1911 y todavía la habitan unos monjes. La base es Tamanrasset, 1.320 m y unos 141.000 habitantes. AVISO: wilaya del Gran Sur, con agencia autorizada obligatoria y control militar en el acceso.",
        dog_note="Se accede solo con agencia y escolta; ninguna operadora del Hoggar acepta animales en los vehículos.",
        visit={
            "why": "Por el amanecer desde el Assekrem, que es el paisaje de montaña más celebrado del Sáhara, y por la altitud, que suaviza el clima.",
            "see": "Agujas volcánicas como el Ilamen, la ermita de Foucauld, el mar de picos al alba y el mundo tuareg de Tamanrasset.",
            "access": "De Tamanrasset al Assekrem hay unos 80 km de pista de montaña que exige 4x4 y guía; se sube la víspera y se duerme en el refugio para ver salir el sol. MAEC, ficha de Argelia, ÚLTIMA ACTUALIZACIÓN 7-5-2026 (consultada 13-9-2026): los no residentes deben comunicar sus desplazamientos fuera de su wilaya a la gendarmería o comisaría más próxima y, si el viaje recorre VARIAS WILAYAS, la agencia de viajes debe haber obtenido AUTORIZACIÓN PREVIA de las autoridades locales; en zonas desérticas el MAEC recomienda viajar en grupo y con guía. Embajada de Argelia en Bruselas (medida de visado del Gran Sur): el visado a la llegada se concede EXCLUSIVAMENTE a viajes organizados por AGENCIA DE VIAJES AUTORIZADA, para las wilayas de Tamanrasset, Illizi, Djanet, Tinduf, Adrar, Timimoun, Béchar, Beni Abbès, Bordj Badji Mokhtar, In Salah y Touggourt; validez máxima 30 días y autorización de embarque con código QR emitida por la agencia. Foro de viajeros: hay control militar en el acceso al Assekrem. El pin marca la ermita, no Tamanrasset.",
            "when": "Noviembre a marzo; noches bajo cero a 2.700 m, hay que llevar saco de invierno.",
            "skip": "Sin agencia autorizada y sin margen de días: la logística del Hoggar no se improvisa.",
        },
        links=[
            {"label": "Wikipedia · Hoggar Mountains", "url": "https://en.wikipedia.org/wiki/Hoggar_Mountains"},
            {"label": "Wikipedia · Assekrem", "url": "https://en.wikipedia.org/wiki/Assekrem"},
            {"label": "Embajada de Argelia · visado del Gran Sur", "url": "https://embbrussels.mfa.gov.dz/announcements/algerian-great-south-tourist-destination-new-visa-issuance-measures"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Assekrem_(ahaggar_national_park).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Assekrem_(ahaggar_national_park).jpg",
                "credit": "Houcine.lk · CC BY-SA 3.0",
                "caption": "El Assekrem, en el parque nacional del Ahaggar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/%D8%A7%D8%B3%D9%83%D8%B1%D8%A7%D9%85_2_-_%D8%AA%D9%85%D9%86%D8%B1%D8%A7%D8%B3%D8%AA.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:%D8%A7%D8%B3%D9%83%D8%B1%D8%A7%D9%85_2_-_%D8%AA%D9%85%D9%86%D8%B1%D8%A7%D8%B3%D8%AA.jpg",
                "credit": "Mohammed Amri · CC BY-SA 4.0",
                "caption": "Los picos volcánicos del Hoggar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ahaggar_Mountains_1981_62.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ahaggar_Mountains_1981_62.jpg",
                "credit": "Smiley.toerist · CC BY-SA 4.0",
                "caption": "Oasis en un lecho seco del Ahaggar.",
            },
        ],
    ),
    dict(
        n=15, name="Djanet y el erg Admer · la puerta del Tassili", cat="Ciudad · servicios", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=24.2894163, lon=9.4657615,  # Google Maps: Aeropuerto de Djanet Tiska
        desc="Oasis tuareg a 1.035 m en el valle del oued Idjeriou, en el borde suroeste del Tassili, con unos 14.655 habitantes en 2008. Es LA BASE LOGÍSTICA DEL SURESTE: desde aquí salen todas las expediciones al Tassili n'Ajjer y al Tadrart, y al oeste se abre el erg Admer. Tiene aeropuerto a unos 30 km al sur, que es por donde entra la mayoría de visitantes con el visado a la llegada del Gran Sur. Está a 412 km al sur de Illizi. AVISO: la policía identifica a los extranjeros a la llegada y la agencia debe recogerlos.",
        dog_note="Base de expediciones con agencia obligatoria; las salidas al erg y al Tassili no admiten animales.",
        visit={
            "why": "Porque sin pasar por Djanet no hay Tassili ni Tadrart, y porque el erg Admer se visita en salidas de un día desde aquí.",
            "see": "El ksar viejo, el palmeral, el mercado tuareg, las dunas del erg Admer y los primeros paneles rupestres del entorno.",
            "access": "Asfalto desde Illizi (412 km) y pista/asfalto desde Tamanrasset; aeropuerto de Djanet Tiska Inedbirene a 30 km. MAEC, ficha de Argelia, ÚLTIMA ACTUALIZACIÓN 7-5-2026 (consultada 13-9-2026): los no residentes deben comunicar sus desplazamientos fuera de su wilaya a la gendarmería o comisaría más próxima y, si el viaje recorre VARIAS WILAYAS, la agencia de viajes debe haber obtenido AUTORIZACIÓN PREVIA de las autoridades locales; en zonas desérticas el MAEC recomienda viajar en grupo y con guía. Embajada de Argelia en Bruselas (medida de visado del Gran Sur): el visado a la llegada se concede EXCLUSIVAMENTE a viajes organizados por AGENCIA DE VIAJES AUTORIZADA, para las wilayas de Tamanrasset, Illizi, Djanet, Tinduf, Adrar, Timimoun, Béchar, Beni Abbès, Bordj Badji Mokhtar, In Salah y Touggourt; validez máxima 30 días y autorización de embarque con código QR emitida por la agencia. El pin marca el aeropuerto, punto de encuentro habitual con la agencia; el centro está 30 km al norte.",
            "when": "Noviembre a marzo, coincidiendo con la temporada de expediciones al Tassili.",
            "skip": "Si no se va a entrar al Tassili ni al Tadrart: Djanet por sí sola es una parada logística.",
        },
        links=[
            {"label": "Wikipedia · Djanet", "url": "https://en.wikipedia.org/wiki/Djanet"},
            {"label": "Embajada de Argelia · visado del Gran Sur", "url": "https://embbrussels.mfa.gov.dz/announcements/algerian-great-south-tourist-destination-new-visa-issuance-measures"},
            {"label": "MAEC · Recomendaciones de viaje, Argelia", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=argelia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Djanet_-_2019.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Djanet_-_2019.jpg",
                "credit": "Ghiles.toubal · CC BY-SA 4.0",
                "caption": "El paisaje desértico de Djanet.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sebe%C3%AFba_festival_sword_dance,_Djanet,_Algeria.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sebe%C3%AFba_festival_sword_dance,_Djanet,_Algeria.jpg",
                "credit": "KHALILI PHOTOS · CC BY-SA 4.0",
                "caption": "La danza de espadas de la Sebeïba, en Djanet.",
            },
        ],
    ),
    dict(
        n=16, name="Béjaïa y la Cabilia · el cabo Carbon y Gouraya", cat="Costa", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=36.7744026, lon=5.1021736,  # Google Maps: Cap Carbon (Béjaïa)
        desc="Capital hammadí desde 1067 y uno de los grandes focos científicos del Mediterráneo occidental medieval: aquí estuvo Fibonacci hacia 1202 y de aquí se llevó a Europa la numeración árabe. Hoy es un puerto de montaña con el parque nacional de Gouraya (20,8 km2, creado en 1984, reserva de la biosfera desde 2004) encajado sobre la ciudad. En el cabo Carbon, EL FARO DE 1906 ESTÁ A 220 M SOBRE EL MAR, el más alto del mundo por su emplazamiento natural, con un alcance de 33 millas.",
        dog_note="El parque de Gouraya protege macacos de Berbería en libertad: el perro genera conflicto y estrés a la fauna.",
        visit={
            "why": "Por la combinación de acantilado, bosque y mar que no se repite en el resto del país, y por el Pic des Singes con macacos en libertad.",
            "see": "Cabo Carbon y su faro, el monte Yemma Gouraya (660 m), las calas de Aiguades y el Pic des Singes, hábitat del macaco de Berbería.",
            "access": "Carretera de montaña estrecha y con curvas desde la ciudad hasta el aparcamiento del cabo Carbon; el último tramo al faro es a pie. Dos 4x4 caben, pero el cruce es justo. El pin marca el acceso al parque por el cabo Carbon. La wilaya de Béjaïa figura entre las de riesgo elevado del aviso francés: no circular de noche por la montaña.",
            "when": "Mayo a octubre para el mar; primavera para el bosque. Entre semana, porque el fin de semana se llena.",
            "skip": "Con temporal o lluvia: la carretera del cabo se vuelve incómoda y el mirador no ofrece nada.",
        },
        links=[
            {"label": "Wikipedia · Béjaïa", "url": "https://en.wikipedia.org/wiki/B%C3%A9ja%C3%AFa"},
            {"label": "Wikipedia · Gouraya National Park", "url": "https://en.wikipedia.org/wiki/Gouraya_National_Park"},
            {"label": "France Diplomatie · Algérie (sécurité)", "url": "https://www.diplomatie.gouv.fr/fr/conseils-aux-voyageurs/conseils-par-pays-destination/algerie/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cap_Carbon_(B%C3%A9ja%C3%AFa).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cap_Carbon_(B%C3%A9ja%C3%AFa).jpg",
                "credit": "Bernard Gagnon · CC BY 4.0",
                "caption": "El cabo Carbon, en Béjaïa.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Barbary_macaque_in_Cap_Carbon_(Gouraya_National_Park).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Barbary_macaque_in_Cap_Carbon_(Gouraya_National_Park).jpg",
                "credit": "Hamza-sia · CC BY-SA 3.0",
                "caption": "Macaco de Berbería en el parque de Gouraya.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/B%C3%A9jaia_%D8%A8%D8%AC%D8%A7%D9%8A%D8%A9_11.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:B%C3%A9jaia_%D8%A8%D8%AC%D8%A7%D9%8A%D8%A9_11.jpg",
                "credit": "Habib kaki · CC0",
                "caption": "La ciudad de Béjaïa.",
            },
        ],
    ),
    dict(
        n=17, name="Parque nacional del Djurdjura · Tikjda y las cumbres nevadas", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="1–2 noches",
        lat=36.4685319, lon=4.1866225,  # Google Maps: Parque nacional del Djurdjura
        desc="Creado el 23 de julio de 1983 y con 185 km2, el Djurdjura es la gran sierra caliza de la Cabilia y el último refugio argelino del MACACO DE BERBERÍA, un primate cuya área prehistórica cubría todo el norte de África. La estación de Tikjda, a 1.600 m, es la base: cedrales, paredes de escalada, la sima del Akouker y el mirador del Djurdjura. En días claros se ve el Mediterráneo. La wilaya de Bouira figura entre las de riesgo elevado del aviso francés: nada de rutas por libre ni pernocta improvisada.",
        dog_note="Parque nacional con macaco de Berbería protegido y simas abiertas; el perro suelto está descartado.",
        visit={
            "why": "Porque rompe el tópico de Argelia: nieve, cedros y calizas a menos de dos horas de la costa.",
            "see": "Cedrales del Djurdjura, macacos, el Point de vue du Djurdjura, el Gouffre de l'Akouker y las paredes de escalada de Tikjda.",
            "access": "Carretera de montaña asfaltada desde Bouira, estrecha y con nieve en invierno; aparcamiento en la estación de Tikjda con sitio para dos 4x4. El pin marca la estación, punto de partida de los senderos. Altura exacta de Lalla Khedidja: POR CONFIRMAR, no la dan las páginas consultadas.",
            "when": "Mayo a octubre para caminar; enero-febrero si se busca nieve, con cadenas.",
            "skip": "Si el aviso de seguridad de la Cabilia se endurece, o si llueve: la sierra se mete en la niebla.",
        },
        links=[
            {"label": "Wikipedia · Djurdjura National Park", "url": "https://en.wikipedia.org/wiki/Djurdjura_National_Park"},
            {"label": "Wikipedia · Tikjda", "url": "https://en.wikipedia.org/wiki/Tikjda"},
            {"label": "France Diplomatie · Algérie (sécurité)", "url": "https://www.diplomatie.gouv.fr/fr/conseils-aux-voyageurs/conseils-par-pays-destination/algerie/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Massif_of_The_Djurdjura_in_kabylia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Massif_of_The_Djurdjura_in_kabylia.jpg",
                "credit": "Ghiles Allali · CC BY-SA 4.0",
                "caption": "El macizo del Djurdjura, en Cabilia.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Behind_The_Djurdjura_Massif.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Behind_The_Djurdjura_Massif.jpg",
                "credit": "Belouahmia Reda Mounir · CC BY-SA 4.0",
                "caption": "Las cumbres del Djurdjura.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Massif_of_The_Djurdjura_kabyle.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Massif_of_The_Djurdjura_kabyle.jpg",
                "credit": "Ghiles Allali · CC BY-SA 4.0",
                "caption": "El parque nacional desde el norte.",
            },
        ],
    ),
    dict(
        n=18, name="Annaba e Hipona · la basílica y San Agustín", cat="Cultura", prio="Media",
        dog="prohibido", time="1 noche",
        lat=36.881805, lon=7.744749,  # Google Maps: Basílica de San Agustín (Annaba)
        desc="Hipona fue puerto fenicio desde el siglo XII a. C. y ciudad romana de primer orden; AQUÍ FUE OBISPO SAN AGUSTÍN DESDE EL AÑO 396 HASTA SU MUERTE, el 28 de agosto de 430, mientras los vándalos asediaban la ciudad. Los vándalos la hicieron su capital entre 435 y 439, Bizancio la recuperó en 534 y los musulmanes la tomaron en 698. Sobre las ruinas se alza la basílica de San Agustín. La Annaba moderna ha crecido encima del yacimiento: lo visitable es un recinto acotado junto a la basílica.",
        dog_note="Basílica en culto y yacimiento vallado; ni uno ni otro admiten animales.",
        visit={
            "why": "Por el peso histórico del lugar: es uno de los sitios fundacionales del cristianismo occidental y se visita en un par de horas.",
            "see": "El yacimiento de Hipona con su museo, la basílica decimonónica que lo domina desde la colina y, a media hora, las montañas de Seraïdi, que llegan a 1.080 m.",
            "access": "Autopista Este-Oeste hasta Annaba; la basílica tiene explanada propia con aparcamiento para dos 4x4 y las ruinas quedan justo debajo. El pin marca la basílica. Fecha de construcción y altura de la basílica: POR CONFIRMAR, no constan en las páginas consultadas.",
            "when": "Primavera y otoño; mañana para el yacimiento, tarde para la costa y Seraïdi.",
            "skip": "Si no se llega hasta el extremo este del país: queda a trasmano de la ruta romana Timgad-Djémila.",
        },
        links=[
            {"label": "Wikipedia · Hippo Regius", "url": "https://en.wikipedia.org/wiki/Hippo_Regius"},
            {"label": "Wikipedia · Annaba", "url": "https://en.wikipedia.org/wiki/Annaba"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Hippo_Regius_-_Annaba_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Hippo_Regius_-_Annaba_02.jpg",
                "credit": "Dzkouslavia · CC BY-SA 4.0",
                "caption": "Las ruinas de Hipona, en Annaba.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Annaba,_Alg%C3%A9rie.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Annaba,_Alg%C3%A9rie.jpg",
                "credit": "Nora Mahfouf · CC BY-SA 4.0",
                "caption": "El cabo de Garde, Annaba.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Annaba,_algeria04.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Annaba,_algeria04.jpg",
                "credit": "Dan Sloan · CC BY-SA 2.0",
                "caption": "La ciudad de Annaba.",
            },
        ],
    ),
    dict(
        n=19, name="Beni Abbès y el valle de la Saoura · el oasis y la duna", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=30.1312217, lon=-2.1662258,  # Google Maps: Béni Abbès
        desc="Oasis de 11.416 habitantes a 483 m, en la orilla izquierda del oued Saoura y rodeado por el Grand Erg Occidental por el norte, el este y el oeste. EL PALMERAL TIENE FORMA DE ESCORPIÓN y en la cola se levanta una gran duna roja, la imagen del pueblo. Aquí se instaló Charles de Foucauld en octubre de 1901 y terminó su capilla el 1 de diciembre de ese año. El centro nacional de investigación de zonas áridas mantiene un museo de etnografía, geología y zoología con jardín botánico.",
        dog_note="Oasis y duna al aire libre; el museo del centro de investigación y la ermita no admiten animales.",
        visit={
            "why": "Por el contraste del palmeral encajado en el valle y la duna roja encima, y por el museo del centro de zonas áridas, poco visitado y muy digno.",
            "see": "La gran duna, el palmeral en forma de escorpión, la ermita de Foucauld y el museo y jardín botánico del CNRZA.",
            "access": "Asfalto desde Béchar (241 km) por el valle de la Saoura; aparcamiento amplio junto a la ermita y explanadas de arena firme. El pin marca la ermita. Embajada de Argelia en Bruselas (medida de visado del Gran Sur): el visado a la llegada se concede EXCLUSIVAMENTE a viajes organizados por AGENCIA DE VIAJES AUTORIZADA, para las wilayas de Tamanrasset, Illizi, Djanet, Tinduf, Adrar, Timimoun, Béchar, Beni Abbès, Bordj Badji Mokhtar, In Salah y Touggourt; validez máxima 30 días y autorización de embarque con código QR emitida por la agencia. Beni Abbès es hoy wilaya propia y figura expresamente en esa lista.",
            "when": "Noviembre a marzo. En verano el valle de la Saoura es uno de los sitios más calurosos del país.",
            "skip": "Si ya se ha hecho Taghit y se va justo de días: el esquema de oasis y duna se repite.",
        },
        links=[
            {"label": "Wikipedia · Béni Abbès", "url": "https://en.wikipedia.org/wiki/B%C3%A9ni_Abb%C3%A8s"},
            {"label": "Embajada de Argelia · visado del Gran Sur", "url": "https://embbrussels.mfa.gov.dz/announcements/algerian-great-south-tourist-destination-new-visa-issuance-measures"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/B%C3%A9ni-Abb%C3%A9s_Oued_saoura.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:B%C3%A9ni-Abb%C3%A9s_Oued_saoura.JPG",
                "credit": "Trabelsiismail · CC BY-SA 3.0",
                "caption": "Béni Abbès y el valle de la Saoura.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/B%C3%A9ni_Abb%C3%A8s_commune_Building.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:B%C3%A9ni_Abb%C3%A8s_commune_Building.jpg",
                "credit": "Trabelsiismail · CC BY-SA 4.0",
                "caption": "El edificio municipal de Béni Abbès.",
            },
        ],
    ),
    dict(
        n=20, name="El Oued · la ciudad de las mil cúpulas y el Souf", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=33.367811, lon=6.8516511,  # Google Maps: El Oued
        desc="Capital del Souf, a solo 76 m de altitud y con 134.699 habitantes, El Oued se conoce como LA CIUDAD DE LAS MIL CÚPULAS por sus tejados abovedados de ladrillo, una rareza en un desierto donde casi todo se construye en adobe plano. El agua subterránea permite aquí el cultivo del palmeral en ghout, hoyos excavados hasta alcanzar la capa freática. Es una parada natural entre el Aurés y el M'Zab. El aviso francés incluye la wilaya de El Oued entre las de riesgo elevado y la franja fronteriza con Túnez y Libia en zona roja.",
        dog_note="Calle y zoco al aire libre con correa; las mezquitas quedan fuera.",
        visit={
            "why": "Por una arquitectura urbana que no se ve en ningún otro punto del Sáhara y por los ghouts del palmeral, un sistema agrícola único.",
            "see": "El perfil de cúpulas desde cualquier azotea, el zoco, y a las afueras los ghouts: cráteres de arena con palmeras plantadas en el fondo.",
            "access": "Asfalto desde Biskra, Touggourt y Tozeur (Túnez); ciudad llana y fácil de circular, con aparcamiento en calle. El pin marca el zoco central. NO acercarse a la franja fronteriza con Túnez y Libia, clasificada en zona roja por el aviso francés.",
            "when": "Noviembre a marzo; el zoco a primera hora y los ghouts con luz baja.",
            "skip": "Si se entra o sale por Túnez con prisa y hay que elegir: el M'Zab es más completo.",
        },
        links=[
            {"label": "Wikipedia · El Oued", "url": "https://en.wikipedia.org/wiki/El_Oued"},
            {"label": "France Diplomatie · Algérie (sécurité)", "url": "https://www.diplomatie.gouv.fr/fr/conseils-aux-voyageurs/conseils-par-pays-destination/algerie/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/La_ville_d'El_Oued_%D9%85%D8%AF%D9%8A%D9%86%D8%A9_%D8%A7%D9%84%D9%88%D8%A7%D8%AF%D9%8A.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:La_ville_d'El_Oued_%D9%85%D8%AF%D9%8A%D9%86%D8%A9_%D8%A7%D9%84%D9%88%D8%A7%D8%AF%D9%8A.jpg",
                "credit": "Habib kaki · CC BY-SA 4.0",
                "caption": "El Oued, la ciudad de las mil cúpulas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Oued_Souf_%D9%88%D8%A7%D8%AF_%D8%B3%D9%88%D9%81.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Oued_Souf_%D9%88%D8%A7%D8%AF_%D8%B3%D9%88%D9%81.jpg",
                "credit": "Habib kaki · CC BY-SA 4.0",
                "caption": "El Souf, el oasis bajo la arena.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Oued_Souf_%D9%88%D8%A7%D8%AF%D9%8A_%D8%B3%D9%88%D9%81_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Oued_Souf_%D9%88%D8%A7%D8%AF%D9%8A_%D8%B3%D9%88%D9%81_-_panoramio.jpg",
                "credit": "Habib kaki · CC BY 3.0",
                "caption": "Palmeral hundido del Souf.",
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
    ("Puerto de Orán (entrada en ferry desde Almería y Alicante)", "Frontera", 35.6987388, -0.6349319,  # Google Maps: Orán (la terminal de pasajeros no figura como objeto)
     "Principal puerto de entrada desde España con vehículo. Almería–Orán con Naviera Armas, unas 10 horas, una salida semanal (miércoles 22:00) según Direct Ferries 2026; Alicante–Orán con Algérie Ferries. Admite coche, furgoneta y autocaravana. Aquí se hace la admisión temporal del vehículo y se compra el seguro argelino obligatorio. Pin comprobado en Google Maps («Orán (la terminal de pasajeros no figura como objeto)»)."),
    ("Puerto de Argel (entrada en ferry desde Barcelona y Alicante)", "Frontera", 36.753768, 3.0587561,  # Google Maps: Argel (la gare maritime no figura como objeto)
     "Puerto de la capital, al abrigo de todos los vientos con dos dársenas artificiales según Wikipedia. Baleària opera Barcelona–Argel desde 185 € (2026) con vehículo; Algérie Ferries lo sirve desde Alicante. Es la mejor entrada si el plan es el centro y el este del país o salir después por Túnez. Pin comprobado en Google Maps («Argel (la gare maritime no figura como objeto)»)."),
    ("Puerto de Ghazaouet (entrada en ferry desde Almería)", "Frontera", 35.0936543, -1.861861,  # Google Maps: Ghazaouet
     "Puerto de la wilaya de Tlemecén, en el extremo oeste. Baleària publica Almería–Ghazaouet desde 143,60 € (2026) y Wikipedia lo describe como punto de entrada habitual desde Almería. Atención: está muy cerca de la frontera con Marruecos, que lleva CERRADA desde 1994 y no se puede cruzar. Pin comprobado en Google Maps («Ghazaouet»)."),
    ("Embajada de España en Argel", "Consular", 36.7610832, 3.043993,  # Google Maps: Chemin Ziryab, Argel (la embajada no figura como objeto)
     "3, Chemin Ziryab, B.P. 185, Argel. Teléfono +213 (0) 23 48 74 40 / 41. Correo emb.argel@maec.es. Emergencia consular 24 horas +213 770 99 98 99. El MAEC pide avisar previamente a la Embajada de los planes de viaje por el país. Pin comprobado en Google Maps («Chemin Ziryab, Argel (la embajada no figura como objeto)»)."),
    ("Consulado General de España en Argel", "Consular", 36.7325, 3.08722,  # Google Maps: (sin objeto en Google Maps; coordenada de la fuente)
     "10 rue Reda Houhou, Alger Centre. Teléfono +213 (0) 21 63 93 54. Correo cog.argel@maec.es. Emergencia consular +213 (0) 770 99 98 99. Es el punto de referencia para pérdida de pasaporte, problemas con la policía o asistencia en caso de accidente. Pin comprobado en Google Maps («(sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Consulado General de España en Orán", "Consular", 35.7031822, -0.6404653,  # Google Maps: Consulado de España en Orán
     "7, rue Mohamed Benabdeslem, Orán. Teléfono +213 (0) 42 06 76 96 / 98. Correo cog.oran@maec.es. Es el consulado competente para el oeste del país y el más útil si se entra por el ferry de Orán o de Ghazaouet. Pin comprobado en Google Maps («Consulado de España en Orán»)."),
    ("CHU Mustapha Pacha (hospital de referencia de Argel)", "Hospital", 36.7626705, 3.0560916,  # Google Maps: CHU Mustapha Pacha (Argel)
     "El hospital más grande de Argelia, 1.500 camas, fundado el 1 de agosto de 1854 y centro universitario del Ministerio de Sanidad. Dirección: Place du 1er Mai 1945, Sidi M'Hamed, Argel 16000. Teléfono +213 23 55 96 80. Es el destino natural de una urgencia grave en la capital, aunque con seguro de repatriación medicalizada el centro lo fija la aseguradora.dz, no se pudo abrir en esta sesión. Pin comprobado en Google Maps («CHU Mustapha Pacha (Argel)»)."),
    ("Tamanrasset (base del Hoggar y puerta del sur)", "Frontera", 22.7942358, 5.5361426,  # Google Maps: Tamanrasset
     "Capital de la wilaya homónima, a 1.320 m de altitud, 140.955 habitantes en 2025, con aeropuerto propio y cabecera de la Transahariana. Es el punto desde el que se organiza el Hoggar y Assekrem, SIEMPRE con agencia autorizada. Aquí es donde el FCDO recoge la posibilidad de visado a la llegada con reserva confirmada de agencia argelina. En enero de 2025 se secuestró a un turista español en Assekrem. Pin comprobado en Google Maps («Tamanrasset»)."),
    ("Combustible: red Naftal en el eje Orán–Argel (autopista Este-Oeste)", "Combustible", 35.6987388, -0.6349319,  # Google Maps: Orán (sin gasolinera concreta como objeto)
     "Naftal es la distribuidora estatal y cubre bien el norte y las nacionales. Gasolina a 47,00 DZD por litro a 9 de febrero de 2026 (GlobalPetrolPrices) y gasóleo en torno a 30 DZD por litro según Sahara Overland, con alto contenido en azufre. Hacia el sur las distancias entre estaciones crecen mucho: planificar por autonomía y llevar bidones. Pin comprobado en Google Maps («Orán (sin gasolinera concreta como objeto)»)."),
    ("Agua de uso general: red urbana de Argel", "Agua potable", 36.753768, 3.0587561,  # Google Maps: Argel
     "Para llenar depósitos de ducha y lavado, el agua de red de las ciudades grandes del norte sirve sin problema. NO es potable sin tratar: TravelHealthPro señala riesgo de fiebre tifoidea por agua contaminada, así que para beber, embotellada o filtro. Salir siempre con los depósitos llenos antes de dejar una ciudad grande, porque hacia el sur el agua escasea. Pin comprobado en Google Maps («Argel»)."),
    ("Paso terrestre con Túnez: Oum Teboul / Melloula (costa norte)", "Frontera", 36.8800568, 8.5624875,  # Google Maps: Oum Teboul
     "Paso costero del norte hacia Tabarka (Túnez), el más usado por extranjeros. Es la única frontera terrestre realmente practicable de Argelia junto con Bouchebka. El FCDO (24 de julio de 2026) solo autoriza viaje esencial a la franja de 30 km de la frontera tunecina, y desaconseja todo viaje en los tramos de Illizi y Ouargla. COORDENADAS APROXIMADAS, sin fuente verificada en esta sesión: hay que comprobarlas. Pin comprobado en Google Maps («Oum Teboul»)."),
    ("Frontera con Marruecos: Zouj Bghal (Oujda–Maghnia) CERRADA", "Frontera", 34.7860777, -1.8411074,  # Google Maps: Zouj Beghal
     "CERRADA DESDE 1994 y prohibido cruzarla (FCDO, 24 de julio de 2026). Argelia rompió relaciones con Marruecos el 24 de agosto de 2021 y cerró su espacio aéreo a aeronaves marroquíes el 22 de septiembre de 2021. Se incluye aquí solo para que quede constancia de que NO es una opción: es el motivo por el que Argelia sale de la ruta 2027. COORDENADAS APROXIMADAS, sin fuente verificada. Pin comprobado en Google Maps («Zouj Beghal»)."),
]

DRONE_CALLOUT = ("danger", "DRONES: NO LOS LLEVES",
                 "Argelia es uno de los países donde un dron en la maleta arruina el viaje en la primera aduana. El MAEC advierte de que drones de recreo, GPS, prismáticos, cámaras de vídeo y aparatos de filmación profesional exigen autorización previa del Ministerio de Comunicación, y de que sin ella hay confiscación en frontera o detención. Drone-laws.com recoge que los vuelos de visitantes extranjeros no están permitidos y que la autoridad de navegación aérea (ENNA) ni siquiera ha codificado un régimen civil. Dejar el dron en España es la única decisión sensata.")

STARLINK_CALLOUT = ("warn", "STARLINK: NO OPERATIVO EN ARGELIA",
                    "Starlink no presta servicio en Argelia a fecha de 2026. La Autorité de Régulation de la Poste et des Communications Électroniques (ARPCE) lanzó el 9 de abril de 2026 un concurso para adjudicar dos licencias de redes satelitales no geoestacionarias (NGSO), al que en teoría pueden concurrir Starlink, Eutelsat OneWeb y Amazon Kuiper, pero el proceso no se ha resuelto. Activar un terminal importado sin licencia local es, además, exactamente el tipo de equipo radioeléctrico que el MAEC dice que hay que declarar y autorizar.")

DOG_MATRIX = [
    ("Ferry con Algérie Ferries (Alicante y Almería)", "permitido con condiciones", "Confirmado en su propia guía del pasajero: reserva obligatoria del animal (unos 30 € por trayecto), certificado o pasaporte europeo, vacuna antirrábica y microchip. Va en la perrera del barco o en el coche; nunca en camarote."),
    ("Ferry con Baleària o Naviera Armas", "por confirmar", "Baleària anuncia acomodación pet friendly en sus rutas argelinas, pero sin condiciones detalladas. En la Almería–Orán de Naviera Armas, Direct Ferries dice que la mascota no se reserva online. Llamar a la naviera antes de comprar; si no la aceptan, desviar a Algérie Ferries."),
    ("Aduana y puerto argelino", "por confirmar", "Ninguna fuente oficial argelina abierta. Llevar certificado sanitario refrendado por veterinario oficial español y copia traducida al francés, y preguntar al consulado argelino al tramitar el visado."),
    ("Norte urbano (Argel, Orán, Constantina)", "permitido con condiciones", "País musulmán con poca cultura de perro en interiores: muchos hoteles y restaurantes no lo admiten. Dormir en el coche o en campings, y buscar alojamiento por teléfono antes de llegar."),
    ("Sáhara y wilayas del sur con agencia obligatoria", "no recomendado", "Calor extremo, etapas largas, escolta y horarios impuestos por la agencia. Si se baja al desierto, dejar el perro en España; no hay margen para adaptar el ritmo."),
    ("Regreso a la Unión Europea", "permitido con condiciones", "Argelia no está en las listas del Reglamento (UE) 2026/636: TITULACIÓN ANTIRRÁBICA HECHA EN ESPAÑA ANTES DE SALIR y anotada en el pasaporte. Sin ella, tres meses de espera fuera de la UE desde la toma de muestra."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Argelia (Ministerio de Asuntos Exteriores, actualizado el 7 de mayo de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Argelia"),
    ("MAEC · Ficha País Argelia (Oficina de Información Diplomática, PDF)", "https://www.exteriores.gob.es/Documents/FichasPais/ARGELIA_FICHA%20PAIS.pdf"),
    ("FCDO · Algeria travel advice (Gobierno del Reino Unido, actualizado el 24 de julio de 2026)", "https://www.gov.uk/foreign-travel-advice/algeria"),
    ("FCDO · Algeria: Safety and security (Gobierno del Reino Unido, 2026)", "https://www.gov.uk/foreign-travel-advice/algeria/safety-and-security"),
    ("FCDO · Algeria: Entry requirements (Gobierno del Reino Unido, 2026)", "https://www.gov.uk/foreign-travel-advice/algeria/entry-requirements"),
    ("TravelHealthPro / NaTHNaC · Algeria (National Travel Health Network and Centre, 2026)", "https://travelhealthpro.org.uk/country/3/algeria"),
    ("Wikipedia · Algeria–Morocco border (frontera cerrada desde 1994)", "https://en.wikipedia.org/wiki/Algeria%E2%80%93Morocco_border"),
    ("Wikipedia · Algeria–Morocco relations (ruptura diplomática del 24 de agosto de 2021)", "https://en.wikipedia.org/wiki/Algeria%E2%80%93Morocco_relations"),
    ("Wikipedia · Algérie Ferries (rutas y flota de ferries de pasaje y vehículos)", "https://en.wikipedia.org/wiki/Alg%C3%A9rie_Ferries"),
    ("Wikipedia · Algiers (coordenadas, puerto y aeropuerto Houari Boumediene)", "https://en.wikipedia.org/wiki/Algiers"),
    ("Wikipedia · Oran (coordenadas, clima y aeropuerto Ahmed Ben Bella)", "https://en.wikipedia.org/wiki/Oran"),
    ("Wikipedia · Ghazaouet (coordenadas y puerto de entrada desde Almería)", "https://en.wikipedia.org/wiki/Ghazaouet"),
    ("Baleària · Rutas de ferry en Argelia (horarios y precios 2026)", "https://www.balearia.com/es/rutas-horarios/regiones-argelia"),
    ("Direct Ferries · Ferry Almería–Orán: precios y horarios 2026", "https://www.directferries.es/ferry_almeria_oran.htm"),
    ("Sahara Overland · Algeria (guía de país para overlanders, 2026)", "https://sahara-overland.com/algeria-3/"),
    ("Horizons Unlimited (HUBB) · Guide/Report on how to visit Algeria without a guide, with your own vehicle", "https://www.horizonsunlimited.com/hubb/north-africa/guide-report-how-visit-algeria-103794"),
    ("Against the Compass · How to travel to Algeria in 2026", "https://againstthecompass.com/en/travel-algeria/"),
    ("GlobalPetrolPrices · Algeria gasoline prices (dato de 9 de febrero de 2026)", "https://www.globalpetrolprices.com/Algeria/gasoline_prices/"),
    ("Drone Laws · Drone Laws in Algeria (2026)", "https://drone-laws.com/drone-laws-in-algeria/"),
    ("Ecofin Agency · Algeria Opens Satellite Market to Competition (ARPCE, abril de 2026)", "https://www.ecofinagency.com/news-digital/1004-54580-algeria-opens-satellite-market-to-competition-inviting-global-operators"),
    ("AniVetVoyage · Algérie: condiciones de entrada de perros y gatos (verificado el 23 de julio de 2025)", "https://anivetvoyage.com/pays/algerie/"),
    ("Algérie Ferries · Guide du passager: Animaux (condiciones oficiales de la naviera para viajar con mascota)", "https://algerieferries.com/algerie-ferries/guide-de-passager/animaux"),
    ("VoyagerDZ · Algérie Ferries: quelles conditions pour voyager avec son animal (tarifa de 30 € por trayecto)", "https://voyagerdz.com/algerie-ferries-quelles-conditions-pour-voyager-avec-son-animal/"),
    ("BOE / DOUE · Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026, listas de terceros países para desplazamientos de animales de compañía (aplicable desde el 22 de abril de 2026)", "https://www.boe.es/buscar/doc.php?id=DOUE-L-2026-80458"),
    ("EUR-Lex · Reglamento Delegado (UE) 2026/131 de la Comisión, de 20 de enero de 2026 (titulación antirrábica; en vigor desde el 28 de marzo de 2026)", "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32026R0131"),
    ("El Español · Exteriores confirma el secuestro de un español en el sur de Argelia (17 de enero de 2025)", "https://www.elespanol.com/espana/20250117/ministerio-exteriores-confirma-secuestro-espanol-sur-argelia/917158277_0.html"),
    ("The Objective · Un grupo tuareg libera y entrega a Argelia al español secuestrado (21 de enero de 2025)", "https://theobjective.com/internacional/2025-01-21/tuareg-iberado-espanol-secuestrado-argelia/"),
    ("Where next Barney? (Ed Gill) · Visiting southern Algeria independently: a logistical guide (actualizado en enero de 2025)", "https://wherenextbarney.me/routes/route-guide-algeria-independently-by-motorbike/"),
    ("Tripadvisor · Foro de Argelia: Which parts of Algeria do you need a guide? (mensajes de 2023–2024)", "https://www.tripadvisor.com/ShowTopic-g293717-i9843-k14827147-Which_parts_of_Algeria_do_you_need_a_guide-Algeria.html"),
    ("Wikipedia · Mustapha Pacha hospital (coordenadas, camas y fundación del CHU de Argel)", "https://en.wikipedia.org/wiki/Mustapha_Pacha_hospital"),
    ("ALG DZ · CHU Mustapha Pacha à Alger: adresse et contact", "https://www.algdz.com/fr/guides/villes/alger/sante/chu-mustapha-pacha"),
    ("Wikipedia · Tamanrasset (coordenadas, altitud, población 2025 y aeropuerto)", "https://en.wikipedia.org/wiki/Tamanrasset"),
    ("Wikipedia · Djanet (oasis del Tassili n'Ajjer, aeropuerto y clima)", "https://en.wikipedia.org/wiki/Djanet"),
    ("Global Emergency Numbers · Algeria: police, fire, ambulance (norma UIT-T E.129)", "https://globalemergencynumbers.com/country/algeria"),
    ("UNESCO · Kasbah of Algiers", "https://whc.unesco.org/en/list/565"),
    ("Wikipedia · Casbah of Algiers", "https://en.wikipedia.org/wiki/Casbah_of_Algiers"),
    ("Wikipedia · Notre-Dame d'Afrique", "https://en.wikipedia.org/wiki/Notre-Dame_d%27Afrique"),
    ("UNESCO · Tipasa", "https://whc.unesco.org/en/list/193"),
    ("Wikipedia · Tipaza", "https://en.wikipedia.org/wiki/Tipaza"),
    ("Wikipedia · Royal Mausoleum of Mauretania", "https://en.wikipedia.org/wiki/Royal_Mausoleum_of_Mauretania"),
    ("Wikipedia · Cherchell", "https://en.wikipedia.org/wiki/Cherchell"),
    ("Wikipedia · Constantine, Algeria", "https://en.wikipedia.org/wiki/Constantine,_Algeria"),
    ("France Diplomatie · Algérie (sécurité)", "https://www.diplomatie.gouv.fr/fr/conseils-aux-voyageurs/conseils-par-pays-destination/algerie/"),
    ("UNESCO · Timgad", "https://whc.unesco.org/en/list/194"),
    ("Wikipedia · Timgad", "https://en.wikipedia.org/wiki/Timgad"),
    ("UNESCO · Djémila", "https://whc.unesco.org/en/list/191"),
    ("Wikipedia · Djemila", "https://en.wikipedia.org/wiki/Djemila"),
    ("MAEC · Recomendaciones de viaje, Argelia", "https://www.exteriores.gob.es/Embajadas/argel/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"),
    ("Wikipedia · Tlemcen", "https://en.wikipedia.org/wiki/Tlemcen"),
    ("UNESCO · M'Zab Valley", "https://whc.unesco.org/en/list/188"),
    ("Wikipedia · M'zab", "https://en.wikipedia.org/wiki/M%27zab"),
    ("Wikipedia · Ghardaia", "https://en.wikipedia.org/wiki/Ghardaia"),
    ("Wikipedia · Timimoun", "https://en.wikipedia.org/wiki/Timimoun"),
    ("Wikipedia · Foggara (qanat)", "https://en.wikipedia.org/wiki/Foggara"),
    ("Embajada de Argelia · visado del Gran Sur", "https://embbrussels.mfa.gov.dz/announcements/algerian-great-south-tourist-destination-new-visa-issuance-measures"),
    ("Wikipedia · Taghit", "https://en.wikipedia.org/wiki/Taghit"),
    ("UNESCO · Tassili n'Ajjer", "https://whc.unesco.org/en/list/179"),
    ("Wikipedia · Tassili n'Ajjer", "https://en.wikipedia.org/wiki/Tassili_n%27Ajjer"),
    ("MAEC · Recomendaciones de viaje, Argelia", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=argelia"),
    ("Wikipedia · Hoggar Mountains", "https://en.wikipedia.org/wiki/Hoggar_Mountains"),
    ("Wikipedia · Assekrem", "https://en.wikipedia.org/wiki/Assekrem"),
    ("Wikipedia · Béjaïa", "https://en.wikipedia.org/wiki/B%C3%A9ja%C3%AFa"),
    ("Wikipedia · Gouraya National Park", "https://en.wikipedia.org/wiki/Gouraya_National_Park"),
    ("Wikipedia · Djurdjura National Park", "https://en.wikipedia.org/wiki/Djurdjura_National_Park"),
    ("Wikipedia · Tikjda", "https://en.wikipedia.org/wiki/Tikjda"),
    ("Wikipedia · Hippo Regius", "https://en.wikipedia.org/wiki/Hippo_Regius"),
    ("Wikipedia · Annaba", "https://en.wikipedia.org/wiki/Annaba"),
    ("Wikipedia · Béni Abbès", "https://en.wikipedia.org/wiki/B%C3%A9ni_Abb%C3%A8s"),
    ("Wikipedia · El Oued", "https://en.wikipedia.org/wiki/El_Oued"),
]

# Norte y Sáhara occidental: Orán · Argel · Constantina · M'Zab · Gourara · Saoura
CORRIDOR = [
    (35.69874, -0.63493),
    (34.87786, -1.2896),
    (36.60838, 2.19114),
    (36.59067, 2.44337),
    (36.78489, 3.0612),
    (36.46853, 4.18662),
    (36.7744, 5.10217),
    (36.19, 5.41),
    (36.31384, 5.73738),
    (36.37236, 6.61418),
    (36.8818, 7.74475),
    (35.49441, 6.4684),
    (34.85, 5.733),
    (33.36781, 6.85165),
    (32.49437, 3.64446),
    (29.26278, -0.23889),
    (27.867, -0.283),
    (30.13122, -2.16623),
    (30.91699, -2.02956),
    (31.617, -2.217),
]

# Gran Sur solo con agencia: M'Zab · Tamanrasset · Assekrem · Djanet · Tassili
CORRIDOR_ALT = [
    (32.49437, 3.64446),
    (22.78889, 5.52556),
    (23.28889, 5.53361),
    (23.21128, 5.72822),
    (24.55415, 9.48543),
    (25.5, 9.0),
]

HISTORIA_RESUMEN = "Argelia es el país más extenso de África, 2.381.741 km² en los que el Sáhara ocupa la mayor parte y casi toda la población se concentra en la franja mediterránea. Su historia encadena reinos amazigh, Cartago y Roma, la islamización árabe, las dinastías medievales del Magreb y tres siglos de regencia otomana, antes de 132 años de colonización francesa y de una guerra que terminó con la independencia el 5 de julio de 1962. Desde entonces el poder gira en torno al Frente de Liberación Nacional y al ejército, con una economía sostenida por el gas y el petróleo. Para el viajero es un país de acceso complicado: visado obligatorio, frontera con Marruecos cerrada desde 1994 y un sur sahariano que solo se recorre con agencia local autorizada."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>El poblamiento del actual territorio argelino es antiquísimo: en Ain Hanech se han documentado herramientas de piedra atribuidas a una antigüedad en torno a 1,8 millones de años, y en 1954 se hallaron fósiles de <em>Homo erectus</em> de unos 700.000 años. Entre el sexto y el segundo milenio antes de nuestra era se desarrollaron culturas neolíticas cuyo testimonio más espectacular son los frescos rupestres del Tassili n'Ajjer, hoy Patrimonio Mundial.</p><p>Los pueblos amazigh —bereberes— son el sustrato de todo lo que vino después. Frente a la Cartago fundada por comerciantes fenicios de Tiro, <strong>Masinisa</strong> unificó el reino de Numidia en el siglo II a.C.; Roma destruyó Cartago en 146 a.C. y acabó anexionando los territorios amazigh, que se convirtieron en granero imperial y dejaron ciudades como Timgad, Djémila o Tipasa. Tras vándalos y bizantinos llegó la conquista árabe, resistida por el rey cristiano Kusayla, que venció a Sidi Ocba en 689, y por la reina <strong>Dihya, la Kahena</strong>, vencedora en Meskiana en 693; los omeyas completaron la conquista hacia 711.</p><p>Siguieron los rustemíes de Tiaret, los fatimíes, los ziríes y hammadíes, los almorávides, los almohades —que unificaron el Magreb hacia 1146-1160— y los zayyánidas de Tremecén. Desde 1516, con la llegada de los hermanos corsarios Aruj y Jeireddín Barbarroja, Argel quedó integrada en el Imperio otomano como regencia gobernada por beylerbeyes y, desde 1671, por deys.</p>"),
    ("Colonización",
     "<p>La potencia colonial fue <strong>Francia</strong>. El 14 de junio de 1830 unos 34.000 soldados franceses al mando del general De Bourmont desembarcaron en Sidi Ferruch, 27 kilómetros al oeste de Argel; la ciudad capituló el 5 de julio de 1830 y el dey Hussein se rindió. Lo que empezó como expedición punitiva se convirtió en una conquista larguísima: la resistencia del emir <strong>Abd el-Kader</strong> se prolongó entre 1832 y 1847 —con el paréntesis del tratado de Tafna de 1837, roto por Francia en 1839— y la pacificación del conjunto del territorio no se dio por concluida hasta 1903.</p><p>Argelia no fue una colonia cualquiera sino un territorio de poblamiento integrado en el Estado francés: desde 1848 el norte se organizó en tres departamentos —Argel, Orán y Constantina— jurídicamente parte de Francia. Los europeos pasaron de unos 25.000 en 1839 a más de 109.000 en 1847 y a 1,6 millones en 1962, en torno al 15% de la población. El decreto Crémieux de 24 de octubre de 1870 concedió la ciudadanía francesa a los judíos argelinos, mientras el <em>Code de l'indigénat</em>, formalizado el 28 de julio de 1881, mantenía a la mayoría musulmana en un estatuto subordinado.</p><p>La herencia colonial sigue visible: el trazado urbano y ferroviario, el uso extendido del francés y una memoria dolorosa cuyo hito más citado es la represión del 8 de mayo de 1945.</p>"),
    ("Independencia y construcción del Estado",
     "<p>El 1 de noviembre de 1954 el Frente de Liberación Nacional y su brazo armado, el Ejército de Liberación Nacional, iniciaron la insurrección conocida como <em>Toussaint Rouge</em>. La guerra duró siete años y cuatro meses e incluyó la batalla de Argel desde septiembre de 1956, el <em>putsch</em> de los generales del 22 de abril de 1961 y la violencia de la OAS. Los acuerdos de Évian, de marzo de 1962, abrieron el alto el fuego del 19 de marzo; el referéndum de julio arrojó un 99,72% a favor y la independencia se proclamó el <strong>5 de julio de 1962</strong>. Las cifras de muertos varían mucho: las francesas hablan de entre 140.000 y 153.000 combatientes argelinos, y las argelinas elevan el total, con civiles, a entre 400.000 y 1,5 millones. Unos 900.000 <em>pieds-noirs</em> salieron hacia Francia y muchos harkis sufrieron represalias.</p><p>La primera Constitución se promulgó en septiembre de 1963 con <strong>Ahmed Ben Bella</strong>. En 1965 <strong>Houari Boumédiène</strong> lo derrocó mediante un golpe militar e impuso un modelo de partido único, industrialización pesada y nacionalización de los hidrocarburos. El giro hacia el pluralismo acabó mal: el Frente Islámico de Salvación ganó la primera vuelta de las legislativas de 1991, el proceso se anuló y el país entró en la llamada década negra, una guerra civil que entre 1991 y 2002 causó más de 100.000 muertos.</p>"),
    ("Historia reciente (2000-2026)",
     "<p>El siglo se abre con <strong>Abdelaziz Buteflika</strong>, elegido presidente en 1999, que cerró la década negra mediante la Concordia Civil de 1999 y la Carta por la Paz y la Reconciliación Nacional de 2005, basadas en amnistías amplias. La reforma constitucional de 2008 eliminó el límite de mandatos y le permitió encadenar reelecciones pese a su mala salud. Los altos precios del petróleo financiaron una paz social costosa y Argelia sorteó las revueltas árabes de 2011 sin cambio de régimen.</p><p>El punto de inflexión llegó el <strong>22 de febrero de 2019</strong>, cuando el anuncio de un quinto mandato desencadenó el <em>Hirak</em>, un movimiento de protestas pacíficas y masivas. Buteflika dimitió el 2 de abril de 2019. Las presidenciales del 12 de diciembre de 2019, boicoteadas por buena parte del movimiento, las ganó <strong>Abdelmadjid Tebboune</strong> con el 58% de los votos y una participación inferior al 40%; tomó posesión el 19 de diciembre de 2019. Un referéndum constitucional del 1 de noviembre de 2020 aprobó una nueva reforma con un 66,68% de síes.</p><p>En paralelo se deterioraron las relaciones con Marruecos: Argel rompió relaciones diplomáticas el 24 de agosto de 2021, cerró su espacio aéreo a la aviación marroquí el 22 de septiembre y no renovó el contrato del gasoducto Magreb-Europa el 31 de octubre de ese mismo año.</p>"),
    ("Política y gobierno en 2026",
     "<p>Argelia es una república presidencialista desde 2008. A fecha de septiembre de 2026, según la Ficha País del Ministerio de Asuntos Exteriores de España de julio de 2026, el jefe del Estado es <strong>Abdelmadjid Tebboune</strong>, en el cargo desde el 19 de diciembre de 2019 y reelegido el 7 de septiembre de 2024 con el 84,3% de los votos y un 46,1% de participación; el primer ministro es <strong>Sifi Ghrieb</strong> desde 2025. Las últimas legislativas fueron el 2 de julio de 2026, ganadas por el Frente de Liberación Nacional con una participación mínima histórica en torno al 21%.</p><p>En la práctica no es una democracia. <strong>Freedom House</strong>, en <em>Freedom in the World 2025</em>, clasifica a Argelia como «Not Free» con <strong>31 puntos sobre 100</strong> —10 sobre 40 en derechos políticos y 21 sobre 60 en libertades civiles— y describe un país controlado por una élite militar y por el FLN, con elecciones fraudulentas, represión de las protestas y corrupción. Reporteros Sin Fronteras lo sitúa en el puesto 145 de 180 en 2026, con 37,38 puntos.</p><p>El Ministerio español, en su página del 7 de mayo de 2026, desaconseja los campamentos saharauis de Tinduf y pide precaución en las zonas fronterizas con Malí, Níger, Túnez y Libia. Con España rige el Tratado de Amistad de 2002 y con la Unión Europea el Acuerdo de Asociación del mismo año.</p>"),
    ("Economía y recursos",
     "<p>La principal fuente de riqueza son los hidrocarburos. Según la Ficha País del Ministerio de Asuntos Exteriores de España de julio de 2026, los hidrocarburos aportaron el 16,83% del PIB en 2024 —más del 30% contando los servicios asociados— y concentran cerca del <strong>90% de las exportaciones</strong>, gestionadas en gran medida por la empresa estatal Sonatrach. Las exportaciones sumaron 51.910 millones de dólares en 2024, con Italia (25,2%), España (16,6%) y Francia (13,1%) como principales clientes, y las importaciones 47.923 millones, con China (29,3%) al frente. Argelia suministra el 38,5% del gas que importa España.</p><p>La moneda es el <strong>dinar argelino</strong>, dividido en cien céntimos, con un cambio aproximado de 0,007 euros por dinar, aunque conviene contar con un mercado paralelo. El PIB per cápita estimado para 2025 es de unos 6.100 dólares según la misma ficha y de 6.051 dólares según el Banco Mundial, que sitúa el PIB total en unos 287.000 millones de dólares. El crecimiento fue del 3,6% en 2024 y del 3,8% en 2025, con un paro en torno al 11,6% y una inflación del 3,5% en 2025.</p><p>Esa dependencia es también la gran vulnerabilidad: en 2025 el déficit fiscal rondaba el 10,2% del PIB y el saldo por cuenta corriente el -7,7%, con reservas exteriores de unos 59.400 millones de dólares. El turismo sigue siendo marginal.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Argelia tenía 46,7 millones de habitantes en 2024 según la ficha española y 47,4 millones en 2025 según el Banco Mundial. Cerca del 70% es urbana, con unos 283 habitantes por kilómetro cuadrado en el norte y menos de 2 en el sur. La población es una mezcla de árabes y amazigh, con comunidades cabileñas, chaouis, mozabitas y tuareg. El árabe y el tamazight son lenguas oficiales —el tamazight desde 2016—, pero en la carretera lo práctico es el <strong>árabe dialectal y, sobre todo, el francés</strong>. El islam suní es la religión del 95%, con una minoría cristiana de unas 150.000 personas.</p><p>La cultura mezcla raíces amazigh, árabes, andalusíes y mediterráneas: el <em>raï</em> de Orán, el <em>chaabi</em>, la música andalusí y los cantos targui; cuscús, chorba y <em>makrout</em>. Son fiestas el 1 de noviembre, el 5 de julio y el Yennayer del 12 de enero. La UNESCO reconoce siete sitios: Tassili n'Ajjer, el valle del M'Zab, Timgad, Djémila, Tipasa, la Qal'a de Beni Hammad y la Casbah de Argel.</p><p>Conviene vestir discreto, con hombros y rodillas cubiertos, sobre todo fuera de Argel y Orán, y no fotografiar personas ni instalaciones militares sin permiso. El ramadán, que en 2027 empieza en torno al 8 de febrero, altera horarios: es de buen gusto no comer ni fumar en público durante el día. El alcohol existe, pero es caro y discreto.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Argelia (Ministerio de Asuntos Exteriores, UE y Cooperación de España · PDF · julio de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/ARGELIA_FICHA%20PAIS.pdf"),
    ("Recomendaciones de viaje: Argelia (MAEC España · actualizado 7 de mayo de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=argelia"),
    ("Recomendaciones de viaje (Embajada de España en Argel · actualizado 7 de mayo de 2026)", "https://www.exteriores.gob.es/Embajadas/argel/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"),
    ("Algeria: Freedom in the World 2025 (Freedom House · 2025)", "https://freedomhouse.org/country/algeria/freedom-world/2025"),
    ("Algeria (Reporteros Sin Fronteras · Índice Mundial de Libertad de Prensa · 2026)", "https://rsf.org/en/country/algeria"),
    ("Algeria: World Heritage Properties (UNESCO · States Parties · consultado en 2026)", "https://whc.unesco.org/en/statesparties/dz"),
    ("Algeria (Encyclopaedia Britannica · consultado en 2026)", "https://www.britannica.com/place/Algeria"),
    ("Historia de Argelia (Wikipedia en español · consultado en 2026)", "https://es.wikipedia.org/wiki/Historia_de_Argelia"),
    ("Argelia (Wikipedia en español · consultado en 2026)", "https://es.wikipedia.org/wiki/Argelia"),
    ("Algeria (Wikipedia en inglés · consultado en 2026)", "https://en.wikipedia.org/wiki/Algeria"),
    ("French Algeria (Wikipedia en inglés · consultado en 2026)", "https://en.wikipedia.org/wiki/French_Algeria"),
    ("Algerian War (Wikipedia en inglés · consultado en 2026)", "https://en.wikipedia.org/wiki/Algerian_War"),
    ("Algeria-Morocco relations (Wikipedia en inglés · consultado en 2026)", "https://en.wikipedia.org/wiki/Algeria%E2%80%93Morocco_relations"),
    ("Abdelmadjid Tebboune (Wikipedia en inglés · consultado en 2026)", "https://en.wikipedia.org/wiki/Abdelmadjid_Tebboune"),
    ("Algeria: datos del Banco Mundial (World Bank Open Data · datos de 2025)", "https://data.worldbank.org/country/algeria"),
    ("Algerie Ferries (Wikipedia en frances · consultado en 2026)", "https://fr.wikipedia.org/wiki/Alg%C3%A9rie_Ferries"),
]

SPEC = dict(
    slug="argelia", name="Argelia", revision="18 sep 2026",
    sub="FUERA DE RUTA — frontera con Marruecos CERRADA desde 1994 · solo se entra en ferry desde España o por Túnez · Sáhara con agencia autorizada",
    chips=[
        ("ESTATUS", "FUERA DE LA RUTA 2027. Ficha informativa para un viaje aparte: la frontera con Marruecos lleva cerrada desde…"),
        ("CÓMO LLEGAR", "En ferry desde Almería, Alicante, Valencia o Barcelona a Orán, Argel, Mostaganem o Ghazaouet (Algérie Ferries…"),
        ("VISADO", "PRESENCIAL y obligatorio. Se pide en la Embajada en Madrid o en los Consulados de…"),
        ("VEHÍCULO", "Admisión temporal de 90 días prorrogables otros 90; hay que salir con el mismo vehículo…"),
        ("SEGURIDAD", "Norte OK con cautela · sur y fronteras vetados"),
        ("SEGURO", "Carta Verde NO vale · seguro argelino en puerto"),
        ("SALUD", "Sin malaria · fiebre amarilla solo si vienes de zona"),
        ("DRONES", "PROHIBIDOS de hecho · confiscación en aduana"),
        ("STARLINK", "No operativo · SIM Mobilis como plan B"),
        ("4x4", "Sí, con TIP 90 días · gasóleo con mucho azufre"),
        ("A PIE", "Solo ciudades del norte · sur con agencia"),
        ("PERRO", "Se entra con microchip, pasaporte europeo, vacuna antirrábica en vigor y certificado sanitario…"),
        ("MONEDA", "Dinar argelino (DZD), NO convertible: no se puede importar ni sacar del país…"),
        ("VENTANA", "Mediterráneo en la costa (Orán: 32 °C de máxima en agosto…"),
    ],
    center=[30.09, 3.66], zoom=5,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Norte y Sáhara occidental: Orán · Argel · Constantina · M'Zab · Gourara · Saoura",
    corridor_alt_label="Gran Sur solo con agencia: M'Zab · Tamanrasset · Assekrem · Djanet · Tassili",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/The_Tanzoumaitak_cave_painting_in_Tassili_n'ajjer.jpg?width=1200",
    hero_credit="Tassili n'Ajjer · IssamBarhoumi · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Argelia queda fuera de la vuelta de 2027 por un motivo geográfico que no admite discusión: la frontera con Marruecos está CERRADA desde 1994 y Argelia rompió relaciones diplomáticas con Rabat el 24 de agosto de 2021, cerrando además su espacio aéreo a las aeronaves marroquíes el 22 de septiembre. Como la bajada de la expedición va por la costa atlántica (Marruecos y Sáhara Occidental), meter Argelia obligaría a deshacer camino hasta un puerto español, embarcar los dos coches y volver a salir por donde se entró o por Túnez. Hecho aparte sí es viable y es un viaje excelente: ferry Almería, Alicante, Valencia o Barcelona a Orán, Argel, Mostaganem o Ghazaouet con los vehículos a bordo, admisión temporal de 90 días prorrogables otros 90 (MAEC, 7 de mayo de 2026) y seguro de responsabilidad civil argelino que se compra al salir de aduana. El presupuesto orientativo para dos 4x4 y tres personas, dos semanas por el norte, sale por unos 2.500–3.500 € entre ferries de ida y vuelta (un coche con camarote ronda los 400–500 € por trayecto), visados, seguros y combustible casi regalado. Lo que habría que decidir antes: si se baja al Sáhara (Tassili, Hoggar, Djanet, Timimoun), porque ahí hay que contratar agencia local autorizada y escolta, lo que dispara el coste a 90–150 € por día de guía, y si el perro se queda en España.",
    facts=[
        ("Estatus", "FUERA DE LA RUTA 2027. Ficha informativa para un viaje aparte: la frontera con Marruecos lleva cerrada desde 1994 y no se puede encadenar con la bajada atlántica."),
        ("Cómo llegar", "En ferry desde Almería, Alicante, Valencia o Barcelona a Orán, Argel, Mostaganem o Ghazaouet (Algérie Ferries, Baleària, Naviera Armas), o por tierra desde Túnez. En avión a Argel, Orán, Tamanrasset y Djanet."),
        ("Visado", "PRESENCIAL y obligatorio. Se pide en la Embajada en Madrid o en los Consulados de Barcelona y Alicante con cuatro semanas de antelación. NO hay visado en frontera terrestre ni marítima."),
        ("Vehículo/aduana", "Admisión temporal de 90 días prorrogables otros 90; hay que salir con el mismo vehículo. Se emite un TIP gratuito en el puerto. El carnet de passages NO se ha podido confirmar como obligatorio."),
        ("Seguro", "La Carta Verde NO cubre Argelia. Seguro de responsabilidad civil argelino OBLIGATORIO, se compra en el puerto o el paso fronterizo nada más pasar aduana: en torno a 3.000 DZD por cuatro semanas."),
        ("Moneda", "Dinar argelino (DZD), NO convertible: no se puede importar ni sacar del país. Cambio oficial en torno a 140–150 DZD/€ frente a un mercado paralelo de 215–250 DZD/€."),
        ("Perro", "Se entra con microchip, pasaporte europeo, vacuna antirrábica en vigor y certificado sanitario. Argelia NO figura en las listas del Reglamento (UE) 2026/636, así que la vuelta exige TITULACIÓN DE ANTICUERPOS hecha ANTES de salir de España."),
        ("Drones", "En la práctica PROHIBIDOS al visitante extranjero. El MAEC avisa de que drones, GPS, prismáticos y cámaras profesionales exigen autorización del Ministerio de Comunicación; sin ella, confiscación en frontera o detención."),
        ("Starlink", "NO disponible. Starlink no opera en Argelia; la ARPCE abrió el 9 de abril de 2026 un concurso de dos licencias NGSO que todavía no se ha resuelto."),
        ("Seguridad", "El norte urbano (Argel, Orán, Constantina) es transitable con precaución. FCDO desaconseja todo viaje a 30 km de las fronteras con Libia, Mauritania, Mali y Níger, y el MAEC desaconseja Tinduf por amenaza terrorista contra españoles."),
        ("Clima", "Mediterráneo en la costa (Orán: 32 °C de máxima en agosto, 17 °C en enero) y desértico en el interior. El sur solo es practicable de noviembre a marzo; en verano es inviable."),
        ("Sanidad", "Sin riesgo de malaria ni de fiebre amarilla, pero se exige certificado de fiebre amarilla si se llega desde país endémico. Hay poliovirus derivado de vacuna circulando y rabia. Sanidad pública desigual: seguro con repatriación medicalizada imprescindible."),
    ],
    alerts=[
        "FRONTERA CON MARRUECOS CERRADA DESDE 1994 y prohibido cruzarla. Argelia rompió relaciones con Rabat el 24 de agosto de 2021 y cerró su espacio aéreo a aeronaves marroquíes el 22 de septiembre de 2021. No existe forma legal de encadenar Marruecos y Argelia por tierra.",
        "El visado es PRESENCIAL: pasaporte con más de seis meses de validez, dos fotos, seguro de viaje para toda la estancia y cuatro semanas de tramitación. No se concede en frontera ni al desembarcar del ferry.",
        "La Carta Verde europea NO es válida en Argelia. Hay que comprar seguro de responsabilidad civil argelino en el puerto o el paso, en el mismo momento de la entrada, o el vehículo no sale de la aduana.",
        "EL SUR SE RECORRE CON AGENCIA AUTORIZADA Y ESCOLTA. En el foro de Tripadvisor sobre Argelia, los viajeros sitúan la línea a partir de la cual el guía es obligatorio al sur de In Salah, con controles militares en el Tassili n'Ajjer, la Tadrart Rouge y el Ahaggar. Sahara Overland cifra el guía en 90–150 € al día más desplazamientos.",
        "UN TURISTA ESPAÑOL DE UNOS 60 AÑOS FUE SECUESTRADO EL 14 DE ENERO DE 2025 en la zona de Assekrem, cerca de Tamanrasset, por siete hombres armados argelinos y malienses que lo pasaron a Malí con la intención de venderlo al Estado Islámico del Sahel. Iba acompañado de guía y de argelinos, que fueron liberados en el acto. Lo liberó el Frente de Liberación del Azawad el 20 de enero de 2025. Ir con agencia NO es garantía de nada.",
        "El MAEC desaconseja los campamentos saharauis de Tinduf por amenaza terrorista concreta contra ciudadanos españoles, y pide extremar la precaución en Bouira, Tizi-Ouzou, Blida, Jijel, Tipasa, Tébessa, Jenchela y El Oued.",
        "Drones, GPS dedicados, prismáticos y cámaras de filmación profesional necesitan autorización del Ministerio de Comunicación. Sin ella, el material se confisca en frontera y puede haber detención.",
        "El dinar NO es convertible: no se puede entrar con dinares ni sacarlos. Hay que declarar el efectivo por encima de 5.000 € y gastar la moneda local antes de salir, porque no se recompra.",
        "Fuera de la wilaya de estancia conviene comunicar los desplazamientos a la gendarmería y avisar a la Embajada de España de los planes de viaje; de ahí pueden salir escoltas de protección obligatorias.",
        "Sobrepasar la estancia autorizada por el visado lleva a detención en el aeropuerto a la salida, proceso penal y hasta tres meses de prisión (FCDO, 24 de julio de 2026).",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 20 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Desembarco en Orán", "Puerto de Orán · trámites de aduana · Santa Cruz", "~30 km · 1–2 días"),
        ("2 · Orán → Tremecén → Orán", "N7/autopista · Mansourah y Sidi Bumedián", "~350 km · 2 días"),
        ("3 · Orán → Argel por la costa", "Mostaganem · Ténès · Cherchell · Tipasa · Mausoleo", "~470 km · 3 días"),
        ("4 · Argel → Tikjda (Djurdjura)", "Tizi Ouzou · carretera de montaña a Tikjda", "~180 km · 2 días"),
        ("5 · Tikjda → Béjaïa", "Descenso a la costa cabileña · Gouraya y cabo Carbon", "~150 km · 2 días"),
        ("6 · Béjaïa → Sétif → Djémila", "N9 · Sétif · desvío norte a Cuicul", "~200 km · 2 días"),
        ("7 · Djémila → Constantina", "N5 · gargantas del Rhummel y puentes", "~120 km · 1–2 días"),
        ("8 · Constantina → Annaba", "Autopista Este-Oeste · Hipona y la basílica", "~160 km · 1 día"),
        ("9 · Annaba → Timgad", "Guelma · Batna · Aurés", "~330 km · 2 días"),
        ("10 · Timgad → Biskra → El Oued", "Bajada al Sáhara por Biskra · Souf", "~430 km · 2 días"),
        ("11 · El Oued → Ghardaïa (M'Zab)", "Touggourt · Ouargla · pentápolis ibadí", "~400 km · 2 días"),
        ("12 · Ghardaïa → Timimoun", "El Menia · Gourara · foggaras", "~730 km · 3 días"),
        ("13 · Timimoun → Adrar → Beni Abbès → Taghit → Béchar", "Tuat y valle de la Saoura", "~820 km · 4 días"),
        ("14 · Béchar → Orán (cierre del bucle)", "Aïn Sefra · Sidi Bel Abbès · reembarque", "~700 km · 3 días"),
        ("15 · OPCIONAL con agencia · Gran Sur", "Ghardaïa → In Salah → Tamanrasset → Assekrem → Djanet → Tassili", "~2.000 km · 10–14 días"),
    ],
    offroad=[
        "Regla de oro antes de pisar cualquier pista: el MAEC (ficha de Argelia, última actualización 7-5-2026) obliga a los no residentes a comunicar sus desplazamientos fuera de la wilaya a la gendarmería o comisaría más próxima y exige que, en itinerarios por VARIAS WILAYAS, la agencia haya obtenido autorización previa de las autoridades locales; en zonas desérticas recomienda expresamente viajar en grupo y con guía.",
        "Para todo el Gran Sur —Tamanrasset, Illizi, Djanet, Adrar, Timimoun, Béchar, Beni Abbès, In Salah, Touggourt, Tinduf y Bordj Badji Mokhtar— la Embajada de Argelia limita el visado a la llegada a viajes organizados por AGENCIA AUTORIZADA, lo que en la práctica convierte el guía local en obligatorio para las pistas del sur.",
        "Sahara Overland describe la escolta de agencia como oficialmente obligatoria para circular con vehículo propio desde la frontera hacia el sur profundo, con tarifas de 120-150 EUR/día si el escolta lleva coche propio y unos 90 EUR/día si va en tu vehículo, más 50-100 EUR/día de posicionamiento; además la gendarmería puede imponer escolta de carretera en cualquier control, «nothing is set in stone in Algeria».",
        "Pistas y zonas realmente interesantes: el Hoggar y el Tassili en el sureste son, según Sahara Overland, «la zona más popular con diferencia» para el viaje por el desierto; la subida al Assekrem desde Tamanrasset son unos 80 km de pista de montaña en 4x4 con control militar en el acceso, según los relatos del foro de Tripadvisor.",
        "El Tadrart Rouge y la meseta del Tassili n'Ajjer se recorren solo con guía y con control militar a la entrada; el mismo foro señala que al sur de una línea este-oeste trazada por In Salah el guía es exigido en la práctica.",
        "Zonas vetadas o desaconsejadas: la pista del Tanezrouft hacia Mali por el oeste y la Trans-Sahara Highway al sur de Tamanrasset hacia Níger están descartadas —ningún overlander la ha cruzado hacia Níger desde 2011 según Sahara Overland—; al oeste de Béchar hacia Tinduf puede imponerse escolta militar, y el MAEC clasifica los campamentos de refugiados saharauis de Tinduf como zona de riesgo alto por amenaza terrorista.",
        "La franja fronteriza con Libia está en zona roja íntegra según France Diplomatie, y casi toda la frontera con Túnez también; el FCDO (act. 24-7-2026) advierte de riesgo elevado de secuestro en las zonas fronterizas y desérticas remotas del sur y el este.",
        "Combustible: proveedor único estatal (Naftal), con gasóleo en torno a 30 dinares/litro y gasolina 95 sobre 47 dinares/litro según Sahara Overland, pero el gasóleo argelino es de ALTO CONTENIDO EN AZUFRE: en motores Euro 6 como el del Grenadier hay que valorar el riesgo sobre el sistema de postratamiento antes de entrar.",
    ],
    senderismo=[
        "Travesía de la meseta del Tassili n'Ajjer desde Djanet: varios días a pie o con mulas entre paneles rupestres y bosques de piedra, solo con agencia autorizada y guía; es la caminata mayor del país.",
        "Amanecer en el Assekrem (2.726 m): se duerme en el refugio y se sube andando unos minutos al mirador sobre las agujas volcánicas del Hoggar; noches bajo cero en invierno.",
        "Ascensión al monte Tahat (2.908 m), techo de Argelia, en el Hoggar: jornada larga de alta montaña sahariana, siempre con guía tuareg.",
        "Senderos del parque nacional del Djurdjura desde Tikjda (1.600 m): Point de vue du Djurdjura, cedrales y la sima del Akouker; en días claros se ve el Mediterráneo.",
        "Pic des Singes y cabo Carbon, en el parque nacional de Gouraya (Béjaïa): paseo corto de acantilado hasta el faro de 1906, a 220 m sobre el mar, con macacos de Berbería por el camino.",
        "Vuelta al yacimiento de Timgad a pie: unas dos horas de recorrido por el cardo y el decumano, sin sombra, mejor a primera hora.",
        "Recorrido de Djémila, 30,6 ha en ladera: dos o tres horas con desnivel constante entre foro, teatro y barrio cristiano.",
        "Paseo por las foggaras del Gourara, en Timimoun: caminata corta y llana entre las bocas de las galerías y los peines de reparto de agua, con guía local para entender el sistema.",
    ],
    acampada=[
        "No se han localizado campings oficiales argelinos con web propia verificable: la infraestructura de camping reglado es casi inexistente y las guías consultadas no la mencionan. POR CONFIRMAR con iOverlander sobre el terreno.",
        "iOverlander y Tracks4Africa no se han podido consultar en esta sesión (fuera del alcance de las páginas abiertas), así que las referencias de acampada libre de este apartado quedan sin verificar y deben revisarse antes del viaje.",
        "Acampada libre en el norte: desaconsejada sin más. El aviso francés coloca en riesgo elevado las wilayas de Tizi Ouzou, Bouira, Boumerdès, Béjaïa, Jijel, Skikda, Tébessa, Constantina, El Oued y el macizo del Aurés, que es justo donde caen los PDIs del norte y la Cabilia.",
        "En el Gran Sur la acampada se hace dentro del programa de la agencia —vivac en el erg o en campamentos tuareg de Djanet y Tamanrasset—, porque el acceso mismo depende de esa agencia; no es una decisión libre del viajero.",
        "Alternativa realista en ciudad: hoteles y campamentos-auberge en Ghardaïa, Timimoun, Taghit, Beni Abbès y Djanet, con aparcamiento cerrado. El MAEC recomienda además comunicar los desplazamientos a la gendarmería, lo que encaja mal con el vivac improvisado.",
        "Con perro: la mayoría de hoteles urbanos argelinos no lo aceptan y no hay fuente publicada sobre ello; hay que contar con dormir en los vehículos en recintos cerrados y confirmar caso por caso. POR CONFIRMAR.",
        "Vivac sahariano fuera de agencia: solo en el eje asfaltado del oeste (Béchar-Taghit-Beni Abbès) y siempre a la vista del pueblo, nunca en descampado; aun así los controles de gendarmería suelen derivar al viajero al alojamiento del pueblo.",
        "Agua y sombra: en el Souf, el Gourara y la Saoura no hay áreas de servicio; el abastecimiento se hace en las gasolineras Naftal de las cabeceras de wilaya.",
    ],
    visado=[
        "OBLIGATORIO y PRESENCIAL para españoles. No hay eVisa ni visado en frontera terrestre o marítima; el DNI no sirve.",
        "Dónde: Embajada de Argelia en Madrid (resto de España), Consulado de Barcelona (Cataluña, Aragón, Baleares, Navarra, País Vasco, Cantabria, La Rioja y Burgos) y Consulado de Alicante (Comunidad Valenciana, Andalucía, Murcia, Ceuta y Melilla).",
        "Documentación: pasaporte con validez superior a seis meses, fotocopia del pasaporte, dos fotografías y seguro de viaje válido para toda la estancia. Algunos consulados piden además reserva de alojamiento o carta de invitación.",
        "Plazo: MÍNIMO CUATRO SEMANAS de antelación según el MAEC. Los relatos de viajeros hablan de una semana larga cuando el expediente va limpio, pero se deniega sin motivar.",
        "Coste orientativo: 65 € según Against the Compass (2026); un viajero documentó 105 € en otro consulado europeo en Horizons Unlimited. Confirmar la tarifa vigente en el consulado que corresponda.",
        "Excepción para el sur: el FCDO (24 de julio de 2026) recoge que puede concederse visado a la llegada en los aeropuertos del sur (Tamanrasset, Djanet) con reserva confirmada de una agencia argelina autorizada. Esa vía NO sirve para entrar en coche por el norte.",
    ],
    fronteras_rows=[
        ("Ferry principal desde España", "Puerto de Orán (Algérie Ferries desde Alicante; Naviera Armas desde Almería)", "ABIERTO. Direct Ferries (2026) da Almería–Orán en unas 10 horas, una salida semanal, miércoles a las 22:00. Admite coche, furgoneta y autocaravana. Comprar el seguro argelino nada más salir de aduana."),
        ("Ferry alternativo", "Puerto de Argel (Baleària desde Barcelona; Algérie Ferries desde Alicante)", "ABIERTO. Baleària publica Barcelona–Argel desde 185 € (2026) con vehículo y alojamiento pet friendly. Es la entrada más cómoda si se va al centro y este del país."),
        ("Ferry al oeste", "Puerto de Ghazaouet (Baleària y Algérie Ferries desde Almería)", "ABIERTO. Baleària da Almería–Ghazaouet desde 143,60 € (2026). Ojo: Ghazaouet está a menos de 50 km de la frontera marroquí, que NO se puede cruzar."),
        ("Ferry al centro-oeste", "Puerto de Mostaganem (Baleària desde Valencia)", "ABIERTO. Baleària publica Valencia–Mostaganem desde 135 € (2026). Algérie Ferries también lo sirve dentro de sus ocho rutas mediterráneas."),
        ("Frontera terrestre oeste", "Marruecos: Zouj Bghal / Oujda–Maghnia y el resto del trazado", "CERRADA DESDE 1994 y prohibido cruzarla (FCDO, 24 de julio de 2026). No hay excepción para extranjeros ni para vehículos. Es el dato que saca a Argelia de la ruta 2027."),
        ("Frontera terrestre este", "Túnez: Oum Teboul / Melloula (norte, costa) y Bouchebka (centro)", "ABIERTA a extranjeros y es el único paso terrestre operativo en la práctica. El FCDO solo autoriza viaje esencial a la franja de 30 km de esa frontera, y desaconseja TODO viaje en los tramos de Illizi y Ouargla."),
        ("Frontera sur", "Libia, Níger, Mali y Mauritania", "CERRADAS o desaconsejadas. El FCDO desaconseja todo viaje a 30 km de las fronteras con Libia, Mauritania, Mali y Níger por terrorismo y secuestro. Sahara Overland cita Mauritania como técnicamente abierta, pero no es practicable."),
        ("Aeropuerto principal", "Argel – Houari Boumediene (ALG), a 20 km del centro", "ABIERTO. Hub de Air Algérie con conexiones a España y Francia. Espacio aéreo CERRADO a aeronaves marroquíes desde el 22 de septiembre de 2021."),
        ("Aeropuertos del sur", "Tamanrasset y Djanet", "ABIERTOS. Son la vía por la que el FCDO recoge visado a la llegada con reserva confirmada de agencia argelina autorizada. Solo tienen sentido para una expedición sin vehículo propio."),
        ("Aeropuerto secundario", "Orán – Ahmed Ben Bella (ORN, Es-Senia)", "ABIERTO. Alternativa al ferry para llegar al oeste del país sin coche."),
    ],
    vehiculos=[
        "ADMISIÓN TEMPORAL de 90 días prorrogables otros 90, según el MAEC (7 de mayo de 2026). Es obligatorio salir del país con el mismo vehículo con el que se entró; si el coche se queda, hay problema penal y aduanero.",
        "En el puerto se emite un permiso de importación temporal (TIP) gratuito; un overlander lo documentó en Horizons Unlimited con validez de tres meses, expedido sin coste tras presentar visado y permiso de circulación.",
        "CARNET DE PASSAGES: por confirmar. No se ha podido abrir la web de la Direction Générale des Douanes argelina (douane.gov.dz bloquea el acceso automatizado) y los relatos de overlanders describen la entrada con TIP y sin CPD. No hay fuente oficial que lo exija ni que lo excluya.",
        "SEGURO ARGELINO OBLIGATORIO: la Carta Verde europea no cubre Argelia. Se compra en la ventanilla del propio puerto o paso fronterizo, justo después de la aduana. Sahara Overland cifra unos 3.000 DZD por cuatro semanas y un viajero en Horizons Unlimited unos 18 € al mes.",
        "Se conduce por la DERECHA. Permiso español válido con permiso internacional de conducción recomendado; conviene llevarlo porque los controles de gendarmería son constantes y piden documentación con frecuencia.",
        "Controles y checkpoints muy frecuentes, descritos como correctos y amables en los relatos recientes, pero lentos: hay que contar con perder tiempo a diario y llevar fotocopias del pasaporte, el visado y el permiso de circulación.",
        "Dos vehículos matriculados en España hacen el trámite por duplicado: cada coche necesita su TIP y su seguro. En el ferry se factura cada vehículo por separado; un coche con camarote ronda los 400–500 € por trayecto según Direct Ferries (2026).",
        "Estado de la red: asfalto razonable en el norte, con arena arrastrada, baches y conducción errática según el FCDO (24 de julio de 2026). En el sur, pistas de desierto que además exigen agencia autorizada.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "El MAEC (7 de mayo de 2026) incluye los drones de recreo en la lista de material que requiere autorización del Ministerio de Comunicación, junto con cámaras de vídeo, aparatos de filmación profesional, prismáticos, GPS y estaciones radioeléctricas.",
        "Consecuencia del incumplimiento según el propio MAEC: confiscación del material en frontera o detención. No es una multa administrativa menor.",
        "Drone-laws.com (2026) resume que los vuelos de visitantes extranjeros NO están permitidos y que el Establissement National de la Navigation Aérienne (ENNA) no ha publicado un régimen de drones civiles.",
        "El FCDO (24 de julio de 2026) confirma en la misma línea que equipos fotográficos, drones, prismáticos y telescopios requieren autorización.",
        "Fuentes de prensa argelina (DzairTube, 2026) hablan de un registro obligatorio de drones con fecha límite el 30 de abril de 2026, pero no se ha podido verificar el texto legal en una fuente oficial argelina: queda en pendientes.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "NO DISPONIBLE. Starlink no opera en Argelia a fecha de 2026 (Ecofin Agency, abril de 2026).",
        "La ARPCE abrió el 9 de abril de 2026 una licitación de dos licencias NGSO para abrir el mercado satelital a operadores globales; sin adjudicación conocida, no hay servicio legal.",
        "Un terminal Starlink entra en la categoría de estación radioeléctrica, que el MAEC señala como material sujeto a autorización del Ministerio de Comunicación. Meterlo sin permiso es arriesgarse a confiscación.",
        "Plan B realista: SIM local. Sahara Overland (2026) da una SIM de Mobilis por unos 1.500 DZD con datos abundantes y señala a Mobilis como el operador con mejor cobertura en el sur. Djezzy y Ooredoo cubren bien el norte.",
        "En el desierto profundo no hay cobertura móvil fiable: la agencia autorizada con la que es obligatorio ir suele llevar teléfono satelital propio.",
    ],
    perro_intro=[
        "ENTRADA: según AniVetVoyage (verificado el 23 de julio de 2025), Argelia admite perros con microchip (o tatuaje legible si es anterior al 3 de julio de 2011), pasaporte europeo de animal de compañía, vacuna antirrábica en vigor y certificado sanitario firmado por el veterinario y refrendado por un veterinario oficial antes de salir. NO se ha podido abrir ninguna página oficial argelina que lo confirme.",
        "La web de los servicios veterinarios argelinos (psl.madr.gov.dz, Direction des Services Vétérinaires del Ministerio de Agricultura) y la de la Dirección General de Aduanas (douane.gov.dz) NO se abrieron en esta sesión, así que no hay confirmación oficial argelina de nada de esto, ni lista de RAZAS PROHIBIDAS, ni número máximo de animales por viajero: todo eso queda por confirmar con el consulado argelino al pedir el visado.",
        "VUELTA A LA UE: comprobado en el Reglamento de Ejecución (UE) 2026/636, de 20 de marzo de 2026, aplicable desde el 22 de abril de 2026: Argelia NO figura en ninguna de sus listas. Los únicos territorios africanos listados son Mauricio, Ascensión y Santa Elena, todos insulares. Por tanto el regreso se rige por el Reglamento Delegado (UE) 2026/131, en vigor desde el 28 de marzo de 2026, que exige TITULACIÓN DE ANTICUERPOS ANTIRRÁBICOS en laboratorio autorizado.",
        "HAZ LA TITULACIÓN EN ESPAÑA ANTES DE SALIR (vía A) y que quede anotada en el pasaporte del perro. Si no se hace antes, al volver hay que sacar la muestra en Argelia y esperar TRES MESES fuera de la UE desde la toma. Con dos coches y un calendario cerrado, eso hunde el viaje.",
        "Si durante la estancia se vacuna o se analiza al animal en Argelia, el pasaporte europeo ya no basta al regresar: hace falta certificado sanitario emitido por la autoridad oficial argelina, válido diez días desde su expedición y hasta cuatro meses para movimientos posteriores dentro de la UE.",
        "RIESGO SANITARIO: la rabia está presente en Argelia (TravelHealthPro, 2026) y hay perros asilvestrados en zonas rurales y en los alrededores de los oasis. Vacuna del perro al día, correa corta y evitar contacto con animales locales.",
        "FERRY, CONFIRMADO: Algérie Ferries publica en su guía del pasajero que el animal viaja con certificado sanitario o pasaporte europeo, prueba de vacuna antirrábica y microchip o tatuaje legible, que LA RESERVA DEL ANIMAL ES OBLIGATORIA (unos 30 € por trayecto) y que no puede acceder a salones ni camarotes: o va en la perrera del barco o se queda en el coche del garaje, bajo responsabilidad del dueño y desaconsejado en verano por golpe de calor. Baleària declara acomodación pet friendly; en la Almería–Orán de Naviera Armas, Direct Ferries advierte de que la mascota no se reserva online.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "SIN MALARIA y sin riesgo de fiebre amarilla en el país, pero SÍ se exige certificado de vacunación de fiebre amarilla a quien llegue desde un país con transmisión o haya hecho tránsito de más de doce horas en un aeropuerto de zona afectada (TravelHealthPro, 2026). El certificado vale de por vida.",
        "Vacunas recomendadas por TravelHealthPro: las del calendario (triple vírica, difteria-tétanos-polio), hepatitis A y recuerdo de tétanos si han pasado más de diez años. El MAEC añade tos ferina, fiebre tifoidea y hepatitis B.",
        "POLIO: hay poliovirus derivado de vacuna circulando en Argelia. TravelHealthPro recomienda dosis de recuerdo a inmunodeprimidos, embarazadas y estancias de más de cuatro semanas. Una expedición de varias semanas entra en ese supuesto.",
        "RABIA presente. Vacuna preexposición a valorar para quien tenga contacto con animales o se quede más de un mes, y más aún viajando con perro. Ante mordedura, lavado y tratamiento postexposición inmediato.",
        "Otros riesgos citados por TravelHealthPro: leishmaniasis, fiebre del Valle del Rift y virus del Nilo Occidental por picaduras, fiebre tifoidea por agua y comida, y mal de altura por encima de 2.500 m (el Hoggar los supera).",
        "MEDICAMENTOS: el MAEC avisa de que entrar con medicación sin receta ni informe médico se persigue como tráfico de estupefacientes sea cual sea la cantidad. Llevar recetas y, a ser posible, traducción al francés.",
        "SEGURO: el MAEC recomienda seguro médico completo CON REPATRIACIÓN MEDICALIZADA. La sanidad privada de Argel y Orán es aceptable; fuera de las grandes ciudades, la asistencia es limitada y en el Sáhara la evacuación es cuestión de horas o días.",
    ],
    seguridad_intro="Argelia no es un país en guerra, pero tampoco un destino de ruta libre. Las ciudades del norte se recorren con normalidad tomando precauciones; el problema son las franjas fronterizas del sur y el este, donde AQMI y filiales del Dáesh mantienen capacidad de atentado y secuestro, y las montañas de la Cabilia, donde el MAEC pide extremar la precaución. A eso se suma un control estatal muy activo: escoltas impuestas, obligación de comunicar desplazamientos y agencia autorizada para el Sáhara. Se viaja donde y como dejan, no donde se quiere.",
    seguridad=[
        "El MAEC (7 de mayo de 2026) desaconseja los campamentos de refugiados saharauis de Tinduf por amenaza terrorista concreta contra ciudadanos españoles. Es la alerta más específica de toda la ficha.",
        "Riesgo medio con recomendación de extremar la precaución en las zonas fronterizas con Mali, Níger, Túnez y Libia, y en las wilayas de Bouira, Tizi-Ouzou, Blida, Jijel, Tipasa, Tébessa, Jenchela y El Oued (MAEC).",
        "El FCDO (24 de julio de 2026) desaconseja TODO viaje a la franja de 30 km de las fronteras con Libia, Mauritania, Mali y Níger, y a los 30 km de la frontera tunecina en Illizi y Ouargla y en los montes Chaambi; solo viaje esencial al resto de la franja tunecina.",
        "Grupos activos según el MAEC: AQMI en el oeste y en la frontera con Túnez, Yund Al Jilafa en Bouira y Tizi-Ouzou, y el Estado Islámico del Gran Sáhara en la frontera sur. El FCDO añade que los occidentales son objetivo declarado.",
        "SECUESTRO, CON UN CASO ESPAÑOL RECIENTE: el 14 de enero de 2025, un español de unos 60 años fue secuestrado en la zona de Assekrem, cerca de Tamanrasset, por siete hombres armados argelinos y malienses que lo cruzaron a Malí por Tinzaouatène con la intención de venderlo al Estado Islámico del Sahel. Viajaba con guía y acompañantes argelinos, liberados en el acto. El Frente de Liberación del Azawad lo liberó el 20 de enero y lo entregó a Argelia. El Gobierno argelino no paga rescates (FCDO).",
        "DÓNDE EMPIEZA LA OBLIGACIÓN DE GUÍA: en el foro de Tripadvisor sobre Argelia, viajeros de 2023 y 2024 sitúan la línea al sur de In Salah, con control militar y guía obligatorio en el Tassili n'Ajjer, la Tadrart Rouge y el Ahaggar-Assekrem. En Djanet, la policía identifica al turista al llegar al aeropuerto y exige que lo recoja un guía.",
        "SÁHARA CON AGENCIA: las wilayas del sur solo se recorren con agencia local autorizada. Sahara Overland (2026) cifra el guía con su propio coche en 120–150 € al día, el guía en tu coche en 90 € al día, y entre 50 y 100 € al día más por el desplazamiento del escolta hasta el punto de encuentro.",
        "TRÁFICO: alta siniestralidad vial según el MAEC. El FCDO añade arena en la calzada, baches y conducción errática. De noche, no conducir: es donde se concentran los accidentes y los controles se vuelven tensos.",
        "MARCO LEGAL: el Código Penal castiga los actos homosexuales y las ofensas públicas al pudor con dos a tres años de prisión. Durante el Ramadán no se come, bebe ni fuma en público a la luz del día, bajo sanción.",
    ],
    agua=[
        "El agua corriente NO es potable. TravelHealthPro señala riesgo de fiebre tifoidea por agua y alimentos contaminados. Para beber, agua embotellada o filtro con tratamiento químico o UV.",
        "PARA LLENAR DEPÓSITOS de ducha y lavado, el agua de red de las ciudades del norte (Argel, Orán, Constantina, Annaba) sirve sin problema: es agua tratada aunque no apta para beber directamente.",
        "En el norte, los puntos prácticos son las gasolineras de Naftal en las nacionales, las mezquitas y los campings de la costa. En el sur, los oasis y los pozos de los pueblos del Erg, donde el agua es escasa y compartirla con criterio es obligado.",
        "Cortes de suministro y restricciones estacionales son habituales en verano en el interior y el sur. Salir siempre con los depósitos llenos antes de dejar una ciudad grande.",
        "Con perro a bordo, contar unos 3 litros al día más para él en verano y no dejar que beba de charcas ni acequias: leptospirosis y parásitos.",
        "Dato sin confirmar: no se ha localizado un mapa público de puntos de agua para autocaravanas en Argelia equivalente a los de Marruecos o Túnez. Queda como pendiente para verificar en iOverlander.",
    ],
    combustible=[
        "MUY BARATO Y ES EL GRAN ARGUMENTO DEL PAÍS. GlobalPetrolPrices da la gasolina a 47,00 DZD por litro a 9 de febrero de 2026, es decir 0,36 USD por litro, frente a una media mundial de 1,19 USD. Lleva estable 47,00 DZD el último mes.",
        "Gasóleo todavía más barato: Sahara Overland (2026) lo sitúa en torno a 30 DZD por litro. Un overlander en Horizons Unlimited lo resumía en unos 0,25 € por litro. Llenar los dos 4x4 en Argelia cuesta una fracción de lo que cuesta en España.",
        "CALIDAD: el gasóleo argelino tiene ALTO CONTENIDO EN AZUFRE según Sahara Overland. Con motores modernos con filtro de partículas y AdBlue hay que contar con problemas; conviene informarse del umbral que aguanta cada coche antes de entrar y llevar filtros de repuesto.",
        "La red de Naftal, la distribuidora estatal, cubre bien el norte y las nacionales. Hacia el sur las distancias entre estaciones se disparan: en el Sáhara hay que planificar por autonomía y llevar bidones.",
        "AdBlue y aditivos específicos no son fáciles de encontrar fuera de Argel y Orán. Entrar con reserva suficiente para toda la estancia.",
        "Racionamiento: no consta un racionamiento general al viajero extranjero en las fuentes consultadas, aunque el combustible subvencionado genera colas y desabastecimientos puntuales en las zonas fronterizas por el contrabando. Queda como pendiente de confirmar con relatos de 2026.",
    ],
    experiencias_intro="Argelia recibe pocos overlanders y los relatos útiles se concentran en cuatro sitios: Sahara Overland, el foro Horizons Unlimited, el blog «Where next Barney?» y el foro de Argelia de Tripadvisor. No se han localizado bitácoras de españoles con dos vehículos y perro; lo que sigue es lo más aprovechable de 2019 a 2026, con lo que aporta cada uno.",
    experiencias=[
        "Se puede entrar con tu propio coche y sin guía en el norte: un viajero documentó en el foro Horizons Unlimited, en el hilo «Guide/Report on how to visit Algeria without a guide, with your own vehicle», cómo hizo el trámite solo. Visado en un consulado europeo por 105 €, entrada en ferry y, en la aduana del puerto, un permiso de importación temporal gratuito válido tres meses presentando visado, permiso de circulación y un teléfono de alojamiento. La inspección, minuciosa pero amable.",
        "El seguro se compra nada más salir de aduana: el mismo relato de Horizons Unlimited insiste en que la Carta Verde no vale y que hay que contratar el seguro argelino en el puerto en el momento, por unos 18 € al mes. Es el trámite que más gente olvida y el que bloquea la salida del vehículo de la zona aduanera. Conviene llegar con euros en efectivo porque la tarjeta extranjera no funciona en casi ningún sitio.",
        "El Sáhara cuesta dinero, no permisos sueltos: Sahara Overland (guía de país a 2026) desglosa que la escolta del sur va por días, no por trayecto. Guía con vehículo propio, 120–150 € al día; guía sentado en tu coche, 90 € al día; y de 50 a 100 € al día más para cubrir el tiempo que tarda en llegar hasta ti desde su base o la frontera. Para dos 4x4 una semana en el Hoggar, eso ya son cuatro cifras.",
        "Solo hay dos fronteras terrestres usables: Sahara Overland (2026) es tajante al afirmar que únicamente los pasos con Túnez y con Mauritania están abiertos a turistas extranjeros, y que la entrada alternativa es el ferry desde España o Francia. Confirma además que el papeleo en la entrada es largo y que el seguro de vehículo ronda los 3.000 dinares por cuatro semanas.",
        "El cambio paralelo duplica el presupuesto: tanto Sahara Overland como Against the Compass (guía «How to travel to Algeria in 2026») explican que el cambio oficial está en torno a 140–150 dinares por euro mientras la calle paga entre 215 y 250. Against the Compass señala la plaza Port Saïd de Argel como el punto de referencia y recuerda que el dinar no se recompra: lo que sobre, se pierde.",
        "El visado a la llegada existe, pero solo con agencia: Against the Compass (2026) detalla que la vía de visado en aeropuerto exige carta de invitación de un operador registrado y va por tramos de duración, de 35 € para dos días a 340 € para 16–30 días, con una a tres horas de espera en el aeropuerto. La vía de consulado, sobre 65 € y una semana de trámite, se deniega a veces sin explicación.",
        "La gasolina casi no se paga: varios relatos coinciden en que el combustible es el gran regalo del país, en torno a 0,25 € por litro, pero Sahara Overland advierte del alto contenido en azufre del gasóleo. Es un aviso relevante para un Grenadier y un Delica modernos, donde el filtro de partículas puede sufrir en un viaje largo.",
        "Se sale de Argelia hacia Europa por Túnez: el mismo relato de Horizons Unlimited describe encadenar la salida por la frontera tunecina y embarcar en Túnez hacia Italia con GNV por unos 100 € con camarote en oferta. Es la alternativa a repetir ferry a España y la única forma de no hacer el viaje de ida y vuelta por el mismo sitio.",
        "El aviso más serio lo da quien mejor conoce el sur: Ed Gill, que recorrió Argelia en moto, encabeza su guía logística de «Where next Barney?» con la actualización de enero de 2025 sobre el secuestro del turista español en Assekrem y su intento de venta al Estado Islámico. Pide «extrema precaución» en el sur profundo, describe cómo los controles de gendarmería se multiplican al sur de Ouargla y aconseja rastreador GPS, euros en efectivo y vehículos discretos: los cajeros no aceptan tarjetas occidentales fuera de las grandes ciudades.",
        "Dónde acaba la libertad de movimientos: en el hilo «Which parts of Algeria do you need a guide?» del foro de Tripadvisor, viajeros de 2023 y 2024 coinciden en que al sur de In Salah el guía es obligatorio en la práctica, con controles militares en el Tassili n'Ajjer, la Tadrart Rouge y el Ahaggar. En Djanet la policía identifica al viajero en el aeropuerto y exige que lo recoja un guía. Cifran el guía de desierto en 100–160 € al día.",
    ],
    pendientes=[
        ("Carnet de passages en douane", "Abrir douane.gov.dz (Direction Générale des Douanes, admisión temporal) o pedir confirmación por escrito al consulado argelino sobre si el CPD es exigible a un vehículo español. Cerrado cuando haya respuesta oficial o una fuente aduanera argelina."),
        ("Requisitos oficiales de entrada del perro", "Abrir psl.madr.gov.dz o madrp.gov.dz (Direction des Services Vétérinaires) o carta del consulado argelino confirmando certificado, plazos y si hace falta dérogation previa. Cerrado con documento oficial argelino."),
        ("Razas de perro prohibidas", "Localizar norma argelina sobre razas vetadas o número máximo de animales. Cerrado con texto legal o respuesta consular."),
        ("Lista de wilayas que exigen agencia autorizada y escolta", "Obtener el listado oficial (circular del Ministerio del Interior o de Turismo argelino) de wilayas del sur con agencia y escolta obligatorias. Hoy solo hay fuentes de viajeros y la mención genérica del FCDO. Cerrado con norma fechada."),
        ("Registro obligatorio de drones de abril de 2026", "Verificar el decreto o resolución citado por DzairTube en el Journal Officiel argelino o en la web de ENNA. Cerrado con texto oficial."),
        ("Coste vigente del visado en España", "Llamar a la Embajada de Argelia en Madrid y a los consulados de Barcelona y Alicante para la tarifa y el plazo reales de 2026-2027. Cerrado con tarifa confirmada por el consulado que corresponda."),
        ("Perro en los ferries a Argelia", "Algérie Ferries ya está confirmado en su propia web (reserva obligatoria, perrera o vehículo). Falta confirmar la tarifa exacta con su centro de llamadas (3307) y la política de Baleària y Naviera Armas por escrito. Cerrado con confirmación de las tres navieras."),
        ("Frecuencias y temporadas reales de los ferries", "Consultar el horario oficial de Algérie Ferries y Baleària para la temporada prevista: en verano hay refuerzo por la diáspora y en invierno las rutas se reducen. Cerrado con calendario publicado del año del viaje."),
        ("Agua y combustible sobre el terreno", "Rastrear iOverlander, Park4Night y Tracks4Africa en Argelia para puntos de agua y para colas o desabastecimiento de carburante en zonas fronterizas. Cerrado con cinco puntos de agua con coordenadas y dos testimonios del año en curso sobre combustible."),
        ("Clínicas privadas recomendadas a españoles", "El CHU Mustapha Pacha de Argel ya está localizado con dirección y coordenadas. Falta pedir a la Embajada de España en Argel el listado de clínicas privadas que recomienda a los españoles, y un centro de referencia en Orán. Cerrado con la lista consular."),
        ("Teléfonos de emergencia argelinos", "Verificar los números 17, 14, 1055 y 1054 en una fuente oficial argelina o en la página de emergencias de una embajada occidental en Argel (la de Estados Unidos devolvió 403). Cerrado con fuente oficial."),
        ("Estado exacto de los pasos con Túnez", "Verificar con el consulado o con relatos de 2026 si Oum Teboul/Melloula y Bouchebka siguen abiertos a extranjeros con vehículo extranjero. Cerrado con testimonio del año en curso o nota consular."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las fuentes que se pudieron abrir en esa fecha: MAEC (recomendaciones actualizadas el 7 de mayo de 2026), FCDO (24 de julio de 2026), TravelHealthPro, Wikipedia, las navieras y relatos de overlanders. No se pudieron abrir las webs oficiales argelinas (aduanas y servicios veterinarios), y eso está marcado en cada punto afectado. Esto es una herramienta de planificación, no una autorización: los requisitos de visado, aduana y entrada del animal hay que confirmarlos con el consulado argelino antes de moverse.",
    emergency="EMERGENCIA CONSULAR 24 HORAS de España en Argelia: +213 770 99 98 99. Embajada en Argel: +213 23 48 74 40 / 41, emb.argel@maec.es. Consulado General en Orán: +213 42 06 76 96 / 98. Números argelinos (Global Emergency Numbers, verificados según norma UIT-T E.129): POLICÍA 17, GENDARMERÍA 1055, PROTECCIÓN CIVIL (bomberos y ambulancia) 14, GUARDACOSTAS 1054. Prefijo del país, +213. Los números argelinos no figuran en la ficha del MAEC: confirmar al llegar.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

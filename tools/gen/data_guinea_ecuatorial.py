# -*- coding: utf-8 -*-
"""Guinea Ecuatorial — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Guinea Ecuatorial está FUERA DE LA RUTA PREVISTA aunque el corredor del viaje pasa cerca, por Camerún y Gabón. La app solo tiene un stub: créala entera con el formato del piloto de Túnez. Es el ÚNICO país de África con el español como lengua oficial, y eso condiciona toda la ficha: documentación, trato consular y fuentes en castellano. Claves que DECIDEN la ficha y hay que documentar con fuente fechada: Teodoro Obiang gobierna desde el golpe de 1979 y es el jefe de Estado con más años en el cargo del mundo; el país está en los últimos puestos de Freedom House; el petróleo disparó la renta per cápita sin repartirla. Para el viajero: el régimen de visados para españoles ha cambiado — verifica si sigue en vigor la exención anunciada y con qué condiciones; la fotografía de edificios oficiales, aeropuertos y militares está prohibida y se detiene por ello; hay controles policiales continuos en carretera que piden documentación; y el acceso a la isla de Bioko y a Annobón es solo aéreo o marítimo. Ciudad de la Paz (Djibloho/Oyala) es la capital administrativa construida en la selva continental.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/guinea-ecuatorial.json y audit/pdi/guinea-ecuatorial.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Malabo · casco colonial español y catedral de Santa Isabel", cat="Cultura", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=3.7570285, lon=8.7827462,  # Google Maps: Catedral de Santa Isabel
        desc="El corazón de la antigua Santa Isabel conserva manzanas enteras de arquitectura colonial española, con casas de madera del XIX en las calles Nigeria y Rey Boncoro. La catedral neogótica, proyectada por el claretiano Lluís Sagarra, se levantó entre 1899 y 1916 y sus DOS TORRES MIDEN 40 METROS. Un incendio dañó la cubierta el 15 de enero de 2020. Aquí está el único país africano de lengua española, y se nota en rótulos y trato. Advertencia: FOTOGRAFIAR EDIFICIOS OFICIALES ES DELITO y se detiene por ello.",
        dog_note="La calle se lleva bien con correa, pero el interior de la catedral y los edificios oficiales quedan descartados; nunca dejarlo solo en el coche por el calor.",
        visit={
            "why": "Es el conjunto colonial español mejor conservado del golfo de Guinea y el mejor sitio para entender de dónde viene el país. La catedral domina la plaza y se visita en media hora.",
            "see": "Plaza de la Independencia, catedral de Santa Isabel, Palacio del Pueblo (desde lejos y sin cámara), casas fernandinas de madera y el ayuntamiento colonial.",
            "access": "Asfalto en toda la ciudad; Malabo está a unos 9 km del aeropuerto por carretera buena. Aparcamiento en la calle en torno a la plaza, suficiente para dos 4x4 fuera de horas punta. El pin marca la fachada de la catedral, en el lado oeste de la plaza. La policía pide documentación con frecuencia: llevar pasaporte y permisos del vehículo siempre encima.",
            "when": "Primera hora de la mañana, antes del calor y con mejor luz; temporada seca de diciembre a febrero.",
            "skip": "Si hay acto oficial o desfile en la plaza, no te acerques con cámara: cámbialo de día.",
        },
        links=[
            {"label": "Malabo (Wikipedia)", "url": "https://es.wikipedia.org/wiki/Malabo"},
            {"label": "Catedral de Santa Isabel (Wikipedia)", "url": "https://es.wikipedia.org/wiki/Catedral_de_Santa_Isabel_(Malabo)"},
            {"label": "Recomendaciones de viaje MAEC", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Guinea+Ecuatorial"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Kathedrale_Santa_Isabel.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Kathedrale_Santa_Isabel.jpg",
                "credit": "B.traeger · CC BY-SA 3.0",
                "caption": "La catedral de Santa Isabel, en Malabo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Streetview_Malabo_3.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Streetview_Malabo_3.jpg",
                "credit": "Denis Barthel · CC BY-SA 3.0",
                "caption": "Una calle de Malabo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Malabo_a_13-oct-01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Malabo_a_13-oct-01.jpg",
                "credit": "Ipisking · CC BY-SA 3.0",
                "caption": "El frente colonial de Malabo.",
            },
        ],
    ),
    dict(
        n=2, name="Puerto de Malabo y la bahía · el muelle y el frente marítimo", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="medio día",
        lat=3.7576371, lon=8.7808258,  # Google Maps: Puerto de Malabo
        desc="La bahía de Malabo es un cráter volcánico inundado y explica por qué los británicos fundaron aquí Port Clarence en 1827. El puerto mueve unas 200.000 toneladas al año y enlaza con Bata, Douala y España; es la puerta de entrada realista para dos 4x4 mientras las fronteras terrestres sigan cerradas. El paseo del frente marítimo se recorre a pie en una hora. Advertencia: EL PUERTO ES ZONA SENSIBLE, nada de fotos al muelle, a los barcos ni a los militares.",
        dog_note="Zona portuaria con control militar y fotografía prohibida; un perro suelto complica cualquier registro policial.",
        visit={
            "why": "Para resolver la logística marítima del viaje (embarque o desembarque de los vehículos) y para ver la bahía volcánica que define la ciudad.",
            "see": "El muelle comercial, los pesqueros, la curva de la bahía con el Pico Basilé al fondo en días claros y los barrios bajos que bordean el agua.",
            "access": "Acceso asfaltado desde el centro; la zona de operaciones portuarias está controlada y se entra solo con gestión previa de la consignataria. Aparcamiento fácil fuera de la verja. El pin marca la entrada principal del puerto. Evita la zona de noche: el MAEC señala aumento de delincuencia nocturna en Malabo y Bata.",
            "when": "Mañana temprano, con el trasiego de pesqueros y menos calor.",
            "skip": "Si no tienes gestión pendiente con el puerto, media hora de paseo por el frente marítimo basta.",
        },
        links=[
            {"label": "Malabo (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Malabo"},
            {"label": "Puerto y capacidad (Wikipedia es)", "url": "https://es.wikipedia.org/wiki/Malabo"},
            {"label": "Aviso de Canadá (checkpoints y fotografía)", "url": "https://travel.gc.ca/destinations/equatorial-guinea"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Port_of_Malabo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Port_of_Malabo.jpg",
                "credit": "ColleBlanche · CC BY-SA 4.0",
                "caption": "El puerto de Malabo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Malabo_bay_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Malabo_bay_-_panoramio.jpg",
                "credit": "tadpolefarm · CC BY-SA 3.0",
                "caption": "La bahía de Malabo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Panoramic_view_of_Malabo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Panoramic_view_of_Malabo.jpg",
                "credit": "Amitsawant0812 · CC BY-SA 4.0",
                "caption": "Panorámica de Malabo desde el mar.",
            },
        ],
    ),
    dict(
        n=3, name="Pico Basilé · el volcán que domina Bioko (3.011 m)", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1 día",
        lat=3.6396672, lon=8.770147,  # Google Maps: Parque Nacional del Pico Basilé
        desc="Volcán en escudo basáltico de 3.011 m, el punto más alto del país y el techo de Bioko; su última erupción se registró en 1923. Una pista asfaltada y luego de tierra sube por la selva de montaña hasta las antenas de la cima, que sirven de emisora de RTVGE y de repetidor de microondas. Esa presencia técnica y militar es justo lo que complica la visita: SE EXIGE PERMISO DE SEGURIDAD y nada de cámaras arriba. Advertencia: niebla casi diaria a partir de media mañana.",
        dog_note="Parque nacional con control militar en la cima y permiso de seguridad obligatorio; no es sitio para bajar el perro del coche.",
        visit={
            "why": "Es la gran subida de la isla: 3.000 m de desnivel desde el mar cruzando cuatro pisos de vegetación, con vistas al golfo de Guinea si el día acompaña.",
            "see": "Selva de montaña, bosque de niebla, brezal de altura, las antenas de la cumbre y, con suerte, la silueta del Camerún y del monte Camerún al norte.",
            "access": "Carretera asfaltada desde Malabo y después pista; se sube en 4x4 en una a dos horas. El aviso de Canadá indica que hace falta PERMISO DE SEGURIDAD para Moka, Pico Basilé y San Antonio de Ureca. Aparcamiento amplio junto al control de la cima, suficiente para dos vehículos. El pin marca la entrada/control del parque, no la cumbre.",
            "when": "Salir antes del amanecer: la cumbre se cubre de nubes casi a diario a media mañana. Mejor de diciembre a febrero.",
            "skip": "Sin permiso tramitado con antelación, ni lo intentes: te darán la vuelta en el control.",
        },
        links=[
            {"label": "Pico Basilé (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Pico_Basil%C3%A9"},
            {"label": "Aviso de Canadá: permisos en Bioko", "url": "https://travel.gc.ca/destinations/equatorial-guinea"},
            {"label": "Operador local con permisos (Rumbo Malabo)", "url": "https://rumbomalabo.com/en/bioko-explorer/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pico_Basil%C3%A9.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pico_Basil%C3%A9.jpg",
                "credit": "Serge Moons · CC BY-SA 3.0",
                "caption": "El Pico Basilé, techo de Bioko.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_Great_Bioko_mountain.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_Great_Bioko_mountain.jpg",
                "credit": "Amitsawant0812 · CC BY-SA 4.0",
                "caption": "La mole del Basilé sobre la isla.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Limbe_view_with_Bioko.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Limbe_view_with_Bioko.jpg",
                "credit": "Autor desconocido · CC BY-SA 3.0",
                "caption": "Bioko vista desde el continente.",
            },
        ],
    ),
    dict(
        n=4, name="Gran Caldera de Luba · reserva científica de Bioko", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="3–4 noches",
        lat=3.3530389, lon=8.512362,  # Google Maps: Reserva científica de la Caldera de Luba
        desc="Caldera de un volcán en escudo de 2.261 m, segunda cima del país, protegida desde 2000 como reserva científica de 51.000 hectáreas. Es uno de los santuarios de primates más densos de África: de 1,2 a 3,3 encuentros por kilómetro cuadrado y, probablemente, LA MAYOR POBLACIÓN DE DRILES QUE QUEDA EN EL MUNDO. No hay carretera: los cazadores tardan dos días a pie en llegar. Advertencia: sin guía, permiso y logística de expedición es inabordable; no es una excursión de un día.",
        dog_note="Reserva científica con primates amenazados; la entrada de perros es incompatible con el protocolo de conservación y con dos días de marcha por selva.",
        visit={
            "why": "Selva primaria intacta con drill, colobo rojo de Bioko, cercopiteco de Preuss y colobo negro, además de playas de arena negra donde desovan tortugas.",
            "see": "El anfiteatro de la caldera, bosque de altura, arroyos encajados y las playas de Moraka y Moaba, con estaciones de biomonitoreo estacionales.",
            "access": "Sin acceso rodado hasta el interior. Se entra a pie desde Moka o desde la costa sur, con guía y porteadores; dos jornadas de marcha. Estaba en construcción una carretera de Belebu a Ureca que rozaría la reserva (estado actual por confirmar). Los 4x4 se quedan en el punto de partida. El pin marca el centro de la caldera, no un acceso rodado.",
            "when": "Temporada seca de noviembre a marzo; fuera de ella la lluvia hace impracticable la aproximación.",
            "skip": "Si no dispones de cuatro días y de un operador que gestione permisos, cámbialo por Moka y el lago Biaó.",
        },
        links=[
            {"label": "Luba Crater Scientific Reserve (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Luba_Crater_Scientific_Reserve"},
            {"label": "Bioko, reserva de biosfera (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bioko"},
            {"label": "UNESCO · Guinea Ecuatorial (lista indicativa)", "url": "https://whc.unesco.org/en/statesparties/gq"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lago_Bia%C3%B3.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lago_Bia%C3%B3.jpg",
                "credit": "Churlos · CC BY-SA 4.0",
                "caption": "El lago Biaó, en el sur de Bioko.",
            },
        ],
    ),
    dict(
        n=5, name="Playa de Arena Blanca · la costa oeste de Bioko", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=3.5280001, lon=8.5780364,  # Google Maps: Playa de Arena Blanca
        desc="La playa de arena clara más conocida de Bioko, al norte de Luba y a poco más de una hora en coche de Malabo, en una isla donde casi todo el litoral es de arena volcánica negra. Su rareza es entomológica: en la estación seca, de diciembre a febrero, se concentran NUBES DE MILES DE MARIPOSAS sobre la arena húmeda. Es la parada de baño lógica al bajar de la caldera o al volver de Luba. Advertencia: no hay socorristas y las corrientes son fuertes.",
        dog_note="Playa abierta sin fauna protegida nidificando; con correa y vigilando las corrientes, y siempre fuera del agua al anochecer.",
        visit={
            "why": "Es el mejor baño accesible de la isla y el contrapunto ligero a las jornadas de selva y control policial.",
            "see": "Arena clara, palmeras, el perfil de la caldera al sur y, en seca, la concentración de mariposas.",
            "access": "Carretera asfaltada Malabo-Luba y desvío corto; aproximadamente una hora desde Malabo. Aparcamiento informal junto al arenal, suficiente para dos 4x4. En algunos accesos se cobra una entrada simbólica (importe por confirmar). El pin marca el acceso a la playa desde la carretera de Luba.",
            "when": "Estación seca, de diciembre a febrero, que es también cuando aparecen las mariposas.",
            "skip": "Con mar de fondo o lluvia fuerte pierde todo el sentido: sigue a Luba.",
        },
        links=[
            {"label": "Playa de Arena Blanca (Atlas Obscura)", "url": "https://www.atlasobscura.com/places/playa-de-arena-blanca"},
            {"label": "Luba (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Luba,_Equatorial_Guinea"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Arena_Blanca_beach,_pirogues.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Arena_Blanca_beach,_pirogues.jpg",
                "credit": "ColleBlanche · CC BY-SA 4.0",
                "caption": "Cayucos varados en Arena Blanca.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Arena_Blanca_beach,_pirogues_1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Arena_Blanca_beach,_pirogues_1.jpg",
                "credit": "ColleBlanche · CC BY-SA 4.0",
                "caption": "La playa de Arena Blanca.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Arena_Blanca_beach,_pirogues_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Arena_Blanca_beach,_pirogues_2.jpg",
                "credit": "ColleBlanche · CC BY-SA 4.0",
                "caption": "Pesca artesanal en Arena Blanca.",
            },
        ],
    ),
    dict(
        n=6, name="Ureca y el sur de Bioko · tortugas marinas y el lugar más lluvioso de África", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=3.248638, lon=8.565981,  # Google Maps: San Antonio de Ureca
        desc="San Antonio de Ureca recibe unos 10.450 mm de lluvia al año: ES EL LUGAR MÁS LLUVIOSO DE ÁFRICA, por delante de Debundscha (Camerún), con junio y julio superando los 2.000 mm cada uno. Entre noviembre y marzo, cuando la lluvia afloja, cuatro especies de tortuga marina desovan en las playas negras del sur de la isla. Advertencia: hace falta PERMISO DE SEGURIDAD y la pista de bajada es la peor de Bioko; no se hace en el día.",
        dog_note="Playas de desove de tortugas marinas bajo vigilancia científica: la presencia de un perro es incompatible con los nidos y con el protocolo nocturno.",
        visit={
            "why": "Ver desovar tortugas laúd en una playa sin luces, en el extremo de una isla volcánica, es el momento más memorable posible en este país.",
            "see": "Playas de arena negra (Moaba, Moraka), acantilados, selva lluviosa densísima y cascadas que caen directamente al mar.",
            "access": "Pista de tierra muy exigente desde Luba por Belebu; imprescindible 4x4 y temporada seca. El aviso de Canadá exige permiso de seguridad para Ureca. Alojamiento básico en el pueblo o vivac organizado; el operador local ofrece pensión completa porque no hay servicios. El pin marca el pueblo de San Antonio de Ureca.",
            "when": "De noviembre a marzo, tanto por el desove como porque es la única ventana en que la pista es transitable.",
            "skip": "Fuera de la estación seca, descártalo: la lluvia deja la pista impracticable y no hay tortugas.",
        },
        links=[
            {"label": "San Antonio de Ureca (Wikipedia)", "url": "https://en.wikipedia.org/wiki/San_Antonio_de_Ureca"},
            {"label": "Ureca y su pluviometría (Wikipedia es)", "url": "https://es.wikipedia.org/wiki/San_Antonio_de_Ureca"},
            {"label": "Excursión con permisos (Rumbo Malabo)", "url": "https://rumbomalabo.com/en/bioko-explorer/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Riaba_Beach_View.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Riaba_Beach_View.JPG",
                "credit": "Denis Barthel · CC BY-SA 3.0",
                "caption": "Playa del sur de Bioko, en Riaba.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Riaba_20131226_151334.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Riaba_20131226_151334.jpg",
                "credit": "Denis Barthel · CC BY-SA 3.0",
                "caption": "La costa sur de la isla.",
            },
        ],
    ),
    dict(
        n=7, name="Luba · el segundo puerto de Bioko (antigua San Carlos)", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=3.4590145, lon=8.5528746,  # Google Maps: Luba
        desc="La antigua San Carlos es la capital de Bioko Sur y el segundo puerto de la isla: unos 7.700 habitantes en el casco y unos 24.000 en el área. Nació como puerto maderero y desde 1999 alberga el LUBA FREEPORT, terminal de aguas profundas para la industria petrolera. Conserva un hospital colonial y varias playas, y es la base logística obligada para bajar a la caldera o a Ureca. Advertencia: los alrededores del freeport son zona sensible, sin fotos.",
        dog_note="Pueblo pequeño y tranquilo; con correa no hay problema, salvo en la zona del freeport, que es recinto controlado.",
        visit={
            "why": "Última gasolina, comida y cobertura antes del sur de la isla, y un casco colonial modesto pero auténtico.",
            "see": "El muelle maderero, el hospital colonial, las playas próximas y el contraste entre el pueblo bubi y la terminal petrolera.",
            "access": "Carretera asfaltada desde Malabo, aproximadamente una hora. Aparcamiento cómodo en el pueblo para dos 4x4. El pin marca el centro de Luba, no el freeport, cuyo acceso está controlado.",
            "when": "Cualquier mañana; evita el atardecer si vas a seguir hacia el sur por pista.",
            "skip": "Si vas justo de tiempo, repostar y seguir: en sí misma la ciudad da para una hora.",
        },
        links=[
            {"label": "Luba (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Luba,_Equatorial_Guinea"},
            {"label": "Bioko Sur (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bioko_Sur"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Port_of_Luba,_Bioko,_2013.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Port_of_Luba,_Bioko,_2013.JPG",
                "credit": "Denis Barthel · CC BY-SA 3.0",
                "caption": "El puerto de Luba.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/View_on_Luba,_Bioko,_2013.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:View_on_Luba,_Bioko,_2013.JPG",
                "credit": "Denis Barthel · CC BY-SA 3.0",
                "caption": "Luba, antigua San Carlos.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Catholic_church,_Luba,_Bioko,_2013.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Catholic_church,_Luba,_Bioko,_2013.JPG",
                "credit": "Denis Barthel · CC BY-SA 3.0",
                "caption": "La iglesia de Luba.",
            },
        ],
    ),
    dict(
        n=8, name="Moka y el lago Biaó · el altiplano de Bioko", cat="Naturaleza", prio="Alta",
        dog="no recomendado", time="1 noche",
        lat=3.3457031, lon=8.6655592,  # Google Maps: Moca
        desc="Moka está a 1.380 m sobre un altiplano de praderas y bosque de niebla, con clima oceánico y noches frescas: el único sitio del país donde se duerme sin sudar. Debe el nombre al rey bubi Möókáta, que reinó entre 1835 y 1898. Desde el pueblo sale la marcha al LAGO BIAÓ, un lago de cráter en plena selva: unos 8 km y 559 m de desnivel, cuatro horas. Aquí opera el Moka Wildlife Center del programa de protección de la biodiversidad de Bioko. Advertencia: exige permiso de seguridad.",
        dog_note="El pueblo lo tolera, pero la marcha al lago Biaó entra en zona de primates protegidos y el Moka Wildlife Center desaconseja animales domésticos.",
        visit={
            "why": "Es la base natural para la montaña de Bioko y la puerta del lago Biaó y de las cascadas de Iladyi, con el mejor clima de todo el viaje.",
            "see": "Praderas de altura, poblados bubi, bosque de niebla, el cráter del lago Biaó y el centro de investigación de fauna.",
            "access": "Carretera asfaltada desde Malabo por Riaba o por Luba; el tramo final es de montaña y con niebla frecuente. Aparcamiento en el pueblo para dos vehículos. Permiso de seguridad obligatorio según el aviso canadiense. El pin marca el pueblo de Moka, punto de partida de las marchas.",
            "when": "Temporada seca, noviembre a marzo; salir al lago de madrugada para evitar la niebla de la tarde.",
            "skip": "Con niebla cerrada no se ve el lago ni el cráter: no merece las cuatro horas de marcha.",
        },
        links=[
            {"label": "Moka (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Moka,_Equatorial_Guinea"},
            {"label": "Moca, valle y municipio (Wikipedia es)", "url": "https://es.wikipedia.org/wiki/Moca_(Guinea_Ecuatorial)"},
            {"label": "Ruta al lago Biaó (Rumbo Malabo)", "url": "https://rumbomalabo.com/en/bioko-explorer/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lake_Biao.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lake_Biao.jpg",
                "credit": "Francesca Calisti · CC BY-SA 4.0",
                "caption": "El lago Biaó, en el altiplano de Moka.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Plant_in_Bioko,_2013_03.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Plant_in_Bioko,_2013_03.JPG",
                "credit": "Denis Barthel · CC BY-SA 3.0",
                "caption": "Flora del altiplano de Bioko.",
            },
        ],
    ),
    dict(
        n=9, name="Bata · la capital continental y su paseo marítimo", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=1.8679661, lon=9.7656891,  # Google Maps: P.º Marítimo de Bata
        desc="Con 309.345 habitantes en el censo de 2015, Bata es LA CIUDAD MÁS POBLADA DEL PAÍS y la capital de Río Muni. Su puerto, sin bahía natural, es de los de mayor calado de la región, con capacidad para 6,5 millones de toneladas al año, y de aquí salen los ferris a Malabo y Douala: el nudo logístico de todo el continente guineano. El paseo marítimo, con la Torre de la Libertad, es el mejor lugar para pasar la tarde. Advertencia: las explosiones de marzo de 2021 mataron al menos a 105 personas.",
        dog_note="Ciudad grande, con correa y de noche mejor en el alojamiento; el puerto y el aeropuerto son zonas vetadas.",
        visit={
            "why": "Es la base obligada para el interior continental y el punto de embarque de los vehículos; además tiene el mejor ambiente de calle del país.",
            "see": "Paseo marítimo, Torre de la Libertad, catedral, mercado central y el puerto desde fuera.",
            "access": "Asfalto en toda la ciudad y buenas carreteras hacia Niefang y Mongomo. Aparcamiento a lo largo del paseo, sin problema para dos 4x4. El pin marca el paseo marítimo. Controles de policía frecuentes en las entradas de la ciudad: pasaporte y documentación del vehículo a mano.",
            "when": "Atardecer en el paseo; cualquier mes, con menos lluvia de diciembre a febrero (octubre es el mes más lluvioso, 457 mm).",
            "skip": "Nada que ver si solo estás de paso y tienes la logística resuelta: es una ciudad de servicios.",
        },
        links=[
            {"label": "Bata (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bata,_Equatorial_Guinea"},
            {"label": "Bata (Wikipedia es)", "url": "https://es.wikipedia.org/wiki/Bata_(Guinea_Ecuatorial)"},
            {"label": "Recomendaciones de viaje MAEC", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Guinea+Ecuatorial"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bata-Equatoral-Guinea-banner.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bata-Equatoral-Guinea-banner.jpg",
                "credit": "Mehlauge · CC BY-SA 3.0",
                "caption": "El frente marítimo de Bata.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bata,_2015-02_Restaurante_Royal_Okangong,_Bata,_Equatorial_Guinea_(16325436798).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bata,_2015-02_Restaurante_Royal_Okangong,_Bata,_Equatorial_Guinea_(16325436798).jpg",
                "credit": "Ben Sutherland · CC BY 2.0",
                "caption": "Una calle de Bata.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/UNED_Bata_(2018).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:UNED_Bata_(2018).jpg",
                "credit": "Centro Cultural de España en Malabo · CC BY-SA 2.0",
                "caption": "El centro de la UNED en Bata.",
            },
        ],
    ),
    dict(
        n=10, name="Parque nacional de Monte Alén · la selva de Río Muni", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=1.5353324, lon=10.1255164,  # Google Maps: Parque Nacional del Monte Alén
        desc="El mayor parque del país, íntegramente de selva primaria entre 300 y 1.250 m, declarado por la Ley 3/1997 y gestionado desde 1992 con el proyecto europeo ECOFAC. Alberga más de 105 especies de mamíferos, 16 de primates —gorilas, chimpancés, mandriles, colobo negro—, elefantes de bosque, 265 especies de aves y la RANA GOLIAT, la mayor del mundo. Se llega en unas dos horas desde Bata. Advertencia: la caza furtiva sigue activa dentro del parque, incluso de especies protegidas.",
        dog_note="Parque nacional con gorilas, chimpancés y elefantes de bosque: la entrada de perros está descartada por riesgo sanitario y por los grandes mamíferos.",
        visit={
            "why": "Es la única selva ecuatorial de gran fauna accesible del país y la razón principal para cruzar Río Muni.",
            "see": "Selva primaria, el lago Atoc, cascadas, huellas y sonidos de gorila y chimpancé, aves de rango restringido y ranas goliat en el sector sur.",
            "access": "Carretera asfaltada Bata-Niefang y desvío; unas dos horas desde Bata en vehículo propio. Se exige permiso de entrada al parque y guía local; hay acampada organizada en zona designada. Aparcamiento en la base, suficiente para dos 4x4. El pin marca el centro del parque: confirma en Google Maps el acceso real por Niefang o Engong.",
            "when": "Estación seca, de diciembre a febrero y de junio a agosto; salidas de fauna a primera hora de la mañana.",
            "skip": "Si vienes sin guía ni permiso, no entras; y con lluvia fuerte los senderos son barro puro.",
        },
        links=[
            {"label": "Monte Alén National Park (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Monte_Alen_National_Park"},
            {"label": "Ficha KBA Monte Alén", "url": "https://www.keybiodiversityareas.org/site/factsheet/6381"},
            {"label": "Excursión desde Bata (Rumbo Malabo)", "url": "https://rumbomalabo.com/en/monte-alen/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Nationalpark_Monte_Al%C3%A9n.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Nationalpark_Monte_Al%C3%A9n.jpg",
                "credit": "Mehlauge · CC BY-SA 4.0",
                "caption": "La selva del parque nacional de Monte Alén.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Nationalpark_Monte_Al%C3%A9n_(Tafel).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Nationalpark_Monte_Al%C3%A9n_(Tafel).jpg",
                "credit": "Mehlauge · CC BY-SA 4.0",
                "caption": "Señalización del parque de Monte Alén.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Dissotis_sp_Bioko201306.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Dissotis_sp_Bioko201306.jpg",
                "credit": "Denis Barthel · CC BY-SA 3.0",
                "caption": "Flora de la selva ecuatoguineana.",
            },
        ],
    ),
    dict(
        n=11, name="Ciudad de la Paz (Djibloho) · la capital construida en la selva", cat="Ciudad · servicios", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=1.5991939, lon=10.8266975,  # Google Maps: Ciudad de la Paz
        desc="Llamada antes Oyala y Djibloho, es una capital entera levantada sobre la selva de Wele-Nzas, con 8.150 hectáreas planificadas para entre 160.000 y 200.000 habitantes. El Gobierno empezó a trasladarse en 2017 y EL 2 DE ENERO DE 2026 UN DECRETO LA CONVIRTIÓ EN CAPITAL DEL PAÍS, en lugar de Malabo. Avenidas de seis carriles vacías, campo de golf, universidad de torres de cristal y el Grand Hotel Djibloho de 380 habitaciones. Advertencia: fotografiar edificios oficiales aquí es especialmente arriesgado.",
        dog_note="Ciudad administrativa con fuerte presencia policial y militar; un perro atrae atención donde conviene pasar desapercibido.",
        visit={
            "why": "Es el mejor retrato posible de lo que el petróleo hizo con este país: una capital de manual urbanístico en mitad de la selva, casi sin gente.",
            "see": "Avenidas y viaductos sobredimensionados, el campus universitario, el Grand Hotel Djibloho, el campo de golf y la selva cerrada a 200 m de todo.",
            "access": "Autopista asfaltada desde Bata y Mongomo, en excelente estado; a unos 20 km del aeropuerto de Mengomeyén. Aparcamiento sobra en cualquier avenida. El pin marca el centro administrativo de la ciudad. Controles a la entrada: documentación en regla y cámara guardada.",
            "when": "Mediodía entre semana, cuando hay algo de actividad administrativa; cualquier época del año.",
            "skip": "Si vienes de Mongomo con prisa, puedes verla de paso: no hay servicios turísticos que retengan.",
        },
        links=[
            {"label": "Ciudad de la Paz (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Ciudad_de_la_Paz"},
            {"label": "Ciudad de la Paz / Oyala (Wikipedia es)", "url": "https://es.wikipedia.org/wiki/Ciudad_de_la_Paz_(Guinea_Ecuatorial)"},
            {"label": "2026 en Guinea Ecuatorial (traslado de capital)", "url": "https://en.wikipedia.org/wiki/2026_in_Equatorial_Guinea"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Br%C3%BCcke_Oyala_2011.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Br%C3%BCcke_Oyala_2011.jpg",
                "credit": "signieren · CC BY-SA 3.0 de",
                "caption": "Obras del puente de Oyala, hoy Ciudad de la Paz.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Autobahnbau_in_Oyala.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Autobahnbau_in_Oyala.JPG",
                "credit": "Mehlauge · CC BY-SA 3.0",
                "caption": "La autovía abierta en la selva de Djibloho.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Dschungel_bei_Oyala.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Dschungel_bei_Oyala.JPG",
                "credit": "Mehlauge · CC BY-SA 3.0",
                "caption": "La selva alrededor de Ciudad de la Paz.",
            },
        ],
    ),
    dict(
        n=12, name="Mongomo y la basílica de la Inmaculada Concepción", cat="Cultura", prio="Alta",
        dog="prohibido", time="medio día",
        lat=1.6227615, lon=11.2986142,  # Google Maps: Basílica de la Inmaculada Concepción
        desc="Mongomo es la ciudad natal de Teodoro Obiang, en el poder desde el golpe del 3 de agosto de 1979 y hoy SEGUNDO GOBERNANTE NO REAL CON MÁS AÑOS EN EL CARGO DEL MUNDO, solo por detrás de Paul Biya; Macías Nguema fue alcalde aquí. Su basílica, inaugurada en 2011, es el mayor edificio religioso de África central y la segunda iglesia católica más grande del continente, tras Yamusukro. Está a un kilómetro de la frontera gabonesa. Advertencia: zona políticamente sensible, prudencia con la cámara y con las conversaciones.",
        dog_note="Recinto religioso de primer rango y sede episcopal: el perro se queda fuera, a la sombra y con alguien al cuidado.",
        visit={
            "why": "Ninguna otra parada explica mejor la relación entre poder personal, petróleo y religión en este país.",
            "see": "La basílica y su explanada, la sede episcopal, el estadio construido para la Copa de África de 2015 y el ambiente de ciudad fronteriza con Gabón.",
            "access": "Carretera asfaltada desde Ciudad de la Paz y Ebebiyín, en buen estado. Aparcamiento amplio en la explanada de la basílica, sin problema para dos 4x4. El pin marca la basílica. La frontera con Gabón está a unos 1-4 km: no te acerques al paso sin trámite, sigue cerrado al tráfico terrestre.",
            "when": "Domingo por la mañana si quieres ver la basílica en uso; cualquier día para la visita arquitectónica.",
            "skip": "Fuera de horario de culto puede estar cerrada: confirma antes de desviarte.",
        },
        links=[
            {"label": "Mongomo (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Mongomo"},
            {"label": "Mongomo (Wikipedia es)", "url": "https://es.wikipedia.org/wiki/Mongomo"},
            {"label": "Guinea Ecuatorial (Wikipedia es)", "url": "https://es.wikipedia.org/wiki/Guinea_Ecuatorial"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Basilica_of_the_Immaculate_Conception,_Mongomo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Basilica_of_the_Immaculate_Conception,_Mongomo.jpg",
                "credit": "Kachelus · CC BY-SA 4.0",
                "caption": "La basílica de la Inmaculada Concepción, en Mongomo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mongomo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mongomo.jpg",
                "credit": "María Concepción Mongomo Carvallo · CC BY 4.0",
                "caption": "Mongomo, en la frontera con Gabón.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Stade-Mongomo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Stade-Mongomo.jpg",
                "credit": "AlgerianPanther · CC BY-SA 4.0",
                "caption": "El estadio de Mongomo.",
            },
        ],
    ),
    dict(
        n=13, name="Ebebiyín · la esquina con Camerún y Gabón", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="medio día",
        lat=2.1480123, lon=11.3313264,  # Google Maps: Ebibeyin
        desc="Capital de Kié-Ntem y tercera ciudad del país, con 36.565 habitantes en el casco y unos 61.000 en el área (2012). Se asienta justo en el TRIPLE PUNTO FRONTERIZO entre Guinea Ecuatorial, Gabón y Camerún y es el final de las tres rutas que llegan de Bata, Yaundé y el centro de Gabón: el punto por el que entraría la expedición si reabren las fronteras terrestres. Advertencia: cerradas desde el 15 de diciembre de 2025 según el MAEC, sin fecha de reapertura.",
        dog_note="Ciudad fronteriza con controles continuos; un perro complica los registros y la documentación sanitaria en un paso internacional.",
        visit={
            "why": "Es el nudo terrestre del país y la parada donde se resuelve —o se frustra— la entrada de dos 4x4 desde Camerún o Gabón.",
            "see": "El mercado transfronterizo, el Nuevo Estadio de Ebebiyín levantado para la Copa África de 2015, la catedral y el trasiego de tres nacionalidades.",
            "access": "Carretera asfaltada desde Mongomo y desde Bata, en buen estado. Aparcamiento fácil. El pin marca el centro de Ebebiyín, no el puesto fronterizo. Aduana y policía de fronteras a pocos kilómetros hacia Kye-Ossi (Camerún) y hacia Gabón; prohibido fotografiar el puesto.",
            "when": "Mañana de día laborable, cuando la aduana está operativa.",
            "skip": "Si las fronteras terrestres siguen cerradas y no tienes trámite, no tiene interés propio.",
        },
        links=[
            {"label": "Ebebiyín (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Ebebiy%C3%ADn"},
            {"label": "Recomendaciones de viaje MAEC", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Guinea+Ecuatorial"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mercado_en_Ebebiy%C3%ADn.png?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mercado_en_Ebebiy%C3%ADn.png",
                "credit": "Miguel Obono Ekieme · CC BY 2.0",
                "caption": "El mercado de Ebebiyín.",
            },
        ],
    ),
    dict(
        n=14, name="Niefang y el valle del río Wele · macizo interior (cascadas por confirmar)", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=1.8314265, lon=10.2487967,  # Google Maps: Niefang
        desc="Niefang, la antigua Sevilla de Niefang, se asienta sobre el río Benito (Wele) a medio camino entre Bata y el interior, y da nombre a la sierra donde se extiende el parque de Monte Alén. Su nombre significa «LÍMITE DE LOS FANG», la frontera tradicional del territorio fang hacia el oeste. Es la parada natural para acceder al parque y para ver el río grande de Río Muni. Advertencia: las «cascadas del río Ilelebé» no aparecen en ninguna fuente abierta; ver «notas».",
        dog_note="Pueblo y carretera sin restricción conocida; si se entra en Monte Alén desde aquí, el perro se queda fuera del parque.",
        visit={
            "why": "Parada de repostaje y de entrada al parque de Monte Alén, con el mejor tramo de río del interior continental.",
            "see": "El puente y el cauce del Wele/Benito, la sierra de Niefang y los poblados fang de la carretera de Bata a Mongomo.",
            "access": "Carretera asfaltada Bata-Mongomo, en buen estado según los avisos oficiales. Aparcamiento fácil en el pueblo. El pin marca el centro de Niefang. Controles policiales frecuentes en el eje Bata-interior.",
            "when": "Cualquier mañana; el río va más alto y vistoso al final de la estación lluviosa.",
            "skip": "Si no vas a entrar a Monte Alén, es solo una parada técnica de veinte minutos.",
        },
        links=[
            {"label": "Niefang (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Niefang"},
            {"label": "Cascadas de Iladyi (alternativa verificada)", "url": "https://es.wikipedia.org/wiki/Cascadas_de_Iladyi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Road_to_Mongomo_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Road_to_Mongomo_-_panoramio.jpg",
                "credit": "tadpolefarm · CC BY-SA 3.0",
                "caption": "La carretera del interior de Río Muni.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Benito_(Mbini)_River_Sendje_Equatorial_Guinea_1_2015_BNB-UM.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Benito_(Mbini)_River_Sendje_Equatorial_Guinea_1_2015_BNB-UM.jpg",
                "credit": "Blitz1980 · CC BY-SA 4.0",
                "caption": "El río Wele (Benito) en Sendje.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Benito_(Mbini)_River_Sendje_Equatorial_Guinea_4_2015_BNB-UM.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Benito_(Mbini)_River_Sendje_Equatorial_Guinea_4_2015_BNB-UM.jpg",
                "credit": "Blitz1980 · CC BY-SA 4.0",
                "caption": "El curso del Wele en el interior.",
            },
        ],
    ),
    dict(
        n=15, name="Estuario del Muni y Cogo · los manglares del sur", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=1.0883366, lon=9.7037615,  # Google Maps: Cogo
        desc="Cogo, la antigua PUERTO IRADIER —fundada en 1874 por el explorador alavés Manuel Iradier, que tiene monumento en el pueblo—, ocupa una península entre los ríos Congüe y Mitémele dentro del estuario del Muni. Está a 121 km de Bata y conserva arquitectura colonial española en ruinas. Es el punto de embarque hacia Corisco y las Elobey y, junto con Acalayong, uno de los dos pasos históricos a Gabón. Advertencia: el cruce a Cocobeach se hace en cayuco y está sujeto al cierre de fronteras.",
        dog_note="Pueblo y embarcadero sin restricción conocida; en cayuco, con calor y sin sombra, no es recomendable llevarlo.",
        visit={
            "why": "Manglares, estuario y un pueblo colonial devorado por la selva: el rincón más melancólico y más español del país.",
            "see": "Ruinas coloniales, el monumento a Iradier, el laberinto de manglares del estuario y los cayucos que cruzan a Gabón.",
            "access": "Carretera desde Bata, 121 km, con tramos finales de peor firme. Aparcamiento informal junto al embarcadero, aceptable para dos 4x4 pero sin vigilancia. El pin marca el pueblo de Cogo. Puesto fronterizo y policía marítima: documentación siempre encima y nada de fotos al embarcadero.",
            "when": "Marea alta para navegar el estuario; estación seca para la carretera.",
            "skip": "Si no vas a embarcar a Corisco o las Elobey, el desvío de 240 km ida y vuelta no compensa.",
        },
        links=[
            {"label": "Kogo / Cogo (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Cogo,_Equatorial_Guinea"},
            {"label": "Cogo (Wikipedia es)", "url": "https://es.wikipedia.org/wiki/Cogo"},
            {"label": "Acalayong, el otro paso del estuario", "url": "https://en.wikipedia.org/wiki/Acalayong"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mbini_Estuary.png?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mbini_Estuary.png",
                "credit": "NASA · Public domain",
                "caption": "El estuario del sur de Río Muni.",
            },
        ],
    ),
    dict(
        n=16, name="Isla de Corisco y las Elobey · las islas del estuario", cat="Costa", prio="Media",
        dog="por confirmar", time="1–2 noches",
        lat=0.917262, lon=9.3173746,  # Google Maps: Corisco
        desc="Corisco son 14 km² de arena blanca y palmeras a 35 m de altura máxima, con ocupación humana documentada desde el año 50 a. C. hasta el 1150 d. C. en los enterramientos de Nandá. España la adquirió en 1843 por acuerdo con los jefes benga, y EN MAYO DE 2025 LA CORTE INTERNACIONAL DE JUSTICIA cerró el litigio con Gabón reconociendo el título a Guinea Ecuatorial. Al lado, Elobey Chico fue capital colonial de Río Muni y hoy está abandonada. Advertencia: solo se llega en barco o avión.",
        dog_note="Traslado en cayuco o vuelo interno: ninguna fuente abierta aclara el régimen para animales; hay que preguntar en Cogo o Bata.",
        visit={
            "why": "Playas vírgenes sin infraestructura y, en Elobey Chico, las ruinas de una capital colonial tragada por la vegetación.",
            "see": "Arenales de Corisco, el poblado de Gobe, los restos administrativos de Elobey Chico y el canal de manglares hacia Elobey Grande.",
            "access": "Sin acceso rodado: los vehículos se quedan en Cogo o Bata. Cayuco desde Cogo o Acalayong, o vuelo interno al aeropuerto de Corisco. Alojamiento muy escaso; contrata con antelación. El pin marca el centro de la isla; el embarcadero real hay que confirmarlo en Google Maps sobre Gobe.",
            "when": "Estación seca y mar en calma; el cruce del estuario se cancela con mal tiempo.",
            "skip": "Con dos 4x4 y agenda apretada, es un desvío de tres días sin vehículo: descártalo si vas justo.",
        },
        links=[
            {"label": "Corisco (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Corisco"},
            {"label": "Elobey Grande y Elobey Chico (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Elobey_Grande"},
            {"label": "UNESCO · Guinea Ecuatorial (lista indicativa)", "url": "https://whc.unesco.org/en/statesparties/gq"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fiesta_tradicional_de_los_Benga,_Isla_Corisco_-_Guinea_Ecuatorial_04.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fiesta_tradicional_de_los_Benga,_Isla_Corisco_-_Guinea_Ecuatorial_04.jpg",
                "credit": "Rafael Toledano · CC BY-SA 4.0",
                "caption": "Fiesta tradicional benga en Corisco.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fiesta_tradicional_de_los_Benga,_Isla_Corisco_-_Guinea_Ecuatorial_09.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fiesta_tradicional_de_los_Benga,_Isla_Corisco_-_Guinea_Ecuatorial_09.jpg",
                "credit": "Rafael Toledano · CC BY-SA 4.0",
                "caption": "Los benga de Corisco.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fiesta_tradicional_de_los_Benga,_Isla_Corisco_-_Guinea_Ecuatorial_11.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fiesta_tradicional_de_los_Benga,_Isla_Corisco_-_Guinea_Ecuatorial_11.jpg",
                "credit": "Rafael Toledano · CC BY-SA 4.0",
                "caption": "Celebración en la isla de Corisco.",
            },
        ],
    ),
    dict(
        n=17, name="Annobón · la isla volcánica del Atlántico sur", cat="Naturaleza", prio="Media",
        dog="por confirmar", time="3–4 noches",
        lat=-1.4064574, lon=5.6313375,  # Google Maps: San Antonio de Palé
        desc="Volcán extinguido de la línea del Camerún, 20,9 km² de valles y montañas boscosas a 350 km de Cabo López (Gabón) y 180 km al suroeste de Santo Tomé: EL TERRITORIO MÁS AISLADO DEL PAÍS, con 5.323 habitantes en 2015. Su punto más alto es el pico Quioveo, 598 m, y en el interior hay un lago de cráter, el Lago A Pot. Aeropuerto y puerto abrieron en 2010 en el extremo norte. Advertencia: sin vuelo o ferry confirmado puedes quedarte varios días bloqueado.",
        dog_note="Solo se llega en avión o en el ferry semanal; el régimen para animales en esos transportes no consta en fuentes abiertas.",
        visit={
            "why": "Es el extremo del país y de cualquier itinerario africano: una isla volcánica hispanohablante en mitad del Atlántico, con lago de cráter y cero turismo.",
            "see": "San Antonio de Palé, el lago A Pot, el pico Quioveo, calas de roca volcánica y ballenas jorobadas en temporada (por confirmar).",
            "access": "Sin acceso rodado desde el resto del país. Vuelo desde Malabo o Bata al aeropuerto de Annobón, o ferry semanal; ambos irregulares. Los 4x4 se quedan en el continente o en Bioko. Alojamiento mínimo. El pin marca San Antonio de Palé, la capital y puerta de entrada.",
            "when": "Temporada seca y mar en calma; reserva el regreso antes de embarcar.",
            "skip": "Con vehículos propios y calendario cerrado, es incompatible: déjalo para un viaje aparte.",
        },
        links=[
            {"label": "Annobón (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Annob%C3%B3n"},
            {"label": "San Antonio de Palé (Wikipedia)", "url": "https://en.wikipedia.org/wiki/San_Antonio_de_Pal%C3%A9"},
            {"label": "UNESCO · Guinea Ecuatorial (lista indicativa)", "url": "https://whc.unesco.org/en/statesparties/gq"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Reserva_Particular_do_Patrimonio_Natural_Ano_Bom_Alexandre_Osvaldo_(01).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Reserva_Particular_do_Patrimonio_Natural_Ano_Bom_Alexandre_Osvaldo_(01).jpg",
                "credit": "Alexandre Osvaldo · CC BY-SA 4.0",
                "caption": "Annobón, la isla volcánica del Atlántico sur.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Reserva_Particular_do_Patrimonio_Natural_Ano_Bom_Alexandre_Osvaldo_(18).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Reserva_Particular_do_Patrimonio_Natural_Ano_Bom_Alexandre_Osvaldo_(18).jpg",
                "credit": "Alexandre Osvaldo · CC BY-SA 4.0",
                "caption": "Paisaje de Annobón.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/San_Antonio_de_Pal%C3%A9_Airport_SDV-1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:San_Antonio_de_Pal%C3%A9_Airport_SDV-1.jpg",
                "credit": "UR-SDV · GFDL",
                "caption": "La pista de San Antonio de Palé.",
            },
        ],
    ),
    dict(
        n=18, name="Evinayong y el interior de Centro Sur", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=1.4403613, lon=10.5718086,  # Google Maps: Evinayong
        desc="Capital de la provincia de Centro Sur, a 631 m de altitud sobre las colinas del sureste de Río Muni, con 9.155 habitantes en el casco y unos 36.500 en el área (2012). Es la ciudad de interior con mejor clima del continente guineano y sede episcopal. En sus alrededores hay cascadas, aunque ninguna fuente abierta da coordenadas ni acceso concreto. Advertencia: EL 19 DE JUNIO DE 2026 UN HELICÓPTERO MILITAR SE ESTRELLÓ entre Niefang y Evinayong; extremar la prudencia con la cámara en la zona.",
        dog_note="Ciudad pequeña de interior sin restricciones conocidas; con correa y fuera de los edificios oficiales.",
        visit={
            "why": "Rompe el trayecto entre Mongomo y Monte Alén con altura, aire fresco y un pueblo de mercado sin turismo.",
            "see": "El mercado, la catedral, las vistas sobre la selva de Centro Sur y las cascadas de los alrededores (acceso por confirmar en destino).",
            "access": "Carretera asfaltada desde Ciudad de la Paz y Niefang. Aparcamiento fácil en el centro. El pin marca el centro de Evinayong. Controles policiales habituales en el eje interior: documentación siempre a mano.",
            "when": "Día de mercado por la mañana; clima más llevadero por la altitud durante todo el año.",
            "skip": "Si vas directo de Mongomo a Bata por la carretera norte, no da para desvío.",
        },
        links=[
            {"label": "Evinayong (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Evinayong"},
            {"label": "2026 en Guinea Ecuatorial", "url": "https://en.wikipedia.org/wiki/2026_in_Equatorial_Guinea"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ISS022-E-35197_-_View_of_Equatorial_Guinea.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ISS022-E-35197_-_View_of_Equatorial_Guinea.jpg",
                "credit": "NASA Earth Science and Remote Sensing Unit · Public domain",
                "caption": "Río Muni desde la Estación Espacial Internacional.",
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
    ("Aeropuerto Internacional de Malabo (SSG)", "Frontera", 3.7517452, 8.7123141,  # Google Maps: Aeropuerto Internacional de Malabo
     "Punta Europa, isla de Bioko, a unos 9 km al este de Malabo. Principal puerta de entrada del país y ÚNICO punto habilitado documentado para la entrada de animales de compañía. Vuelos con Duala, Libreville, Adís Abeba, París, Fráncfort y Casablanca. Pin comprobado en Google Maps («Aeropuerto Internacional de Malabo»)."),
    ("Aeropuerto de Bata (BSG)", "Frontera", 1.9051215, 9.8045536,  # Google Maps: Aeropuerto Internacional de Bata
     "A 4 km al norte de Bata, en la región continental. Vuelos a Malabo con Ceiba Intercontinental y Cronos Airlines (30-40 minutos, varios diarios) y a Libreville con Afrijet. Es la entrada aérea al Río Muni mientras las fronteras terrestres sigan cerradas. Pin comprobado en Google Maps («Aeropuerto Internacional de Bata»)."),
    ("Puerto de Bata (ferry a Malabo y línea a Duala)", "Frontera", 1.8533177, 9.7790227,  # Google Maps: Bata (puerto)
     "Muelle de gran calado, 6,5 millones de toneladas y 300.000 TEU al año, con conexiones de ferry a Malabo y a Duala. Salida del «San Valentín 3» (SEMAPORT S.L.), travesía de 8 a 12 horas. Admisión de vehículos sin confirmar. Pin comprobado en Google Maps («Bata (puerto)»)."),
    ("Puerto de Malabo", "Frontera", 3.7576371, 8.7808258,  # Google Maps: Puerto de Malabo
     "Puerto de la capital histórica, en la bahía de Malabo, con capacidad teórica de unas 200.000 toneladas al año y conexiones con Bata y con Duala. Vía teórica para introducir un vehículo por mar; sin tarifas ni procedimiento aduanero publicados. Pin comprobado en Google Maps («Puerto de Malabo»)."),
    ("Paso fronterizo Ebebiyín – Kye-Ossi (Camerún)", "Frontera", 2.1480123, 11.3313264,  # Google Maps: Ebibeyin (paso a Kye-Ossi)
     "Paso del noreste, junto al trifinio con Camerún y Gabón, con carretera asfaltada a ambos lados. Sometido a cierres y reaperturas sin preaviso desde el 15 de diciembre de 2025 según el MAEC, que desaconseja el acceso terrestre a los no CEMAC. Pin comprobado en Google Maps («Ebibeyin (paso a Kye-Ossi)»)."),
    ("Embajada de España en Malabo", "Consular", 3.752521, 8.7729629,  # Google Maps: Embajada de España en Malabo
     "Carretera del Aeropuerto s/n, Malabo. Teléfonos +240 333 09 20 20 y +240 333 09 28 68. EMERGENCIA CONSULAR 24 h: +240 222 00 85 89. Embajador: Javier Conde y Martínez de Irujo. Pin comprobado en Google Maps («Embajada de España en Malabo»)."),
    ("Consulado General de España en Bata", "Consular", 1.8687995, 9.7667359,  # Google Maps: Consulado de España en Bata
     "Paseo Lumu Matindi s/n, Bata. Teléfono +240 333 08 26 35. EMERGENCIA CONSULAR: +240 222 28 56 77. Guinea Ecuatorial es uno de los poquísimos países africanos con doble representación española (embajada y consulado general). Pin comprobado en Google Maps («Consulado de España en Bata»)."),
    ("Hospital La Paz (Malabo)", "Hospital", 3.7628608, 8.8778718,  # Google Maps: Centro Médico La Paz (Malabo)
     "Centro privado de referencia que el MAEC da para los españoles en Malabo. Teléfono +240 555 666 160. Pago por adelantado y sin convenio de Seguridad Social; recordar que NO existe servicio de ambulancias en el país. Pin comprobado en Google Maps («Centro Médico La Paz (Malabo)»)."),
    ("Clínica Guadalupe (Malabo)", "Hospital", 3.7524425, 8.7817974,  # Google Maps: Clínica Virgen de Guadalupe (Malabo)
     "Segunda referencia sanitaria privada que da el MAEC para Malabo. Teléfono +240 222 573 173. Pago por adelantado y en efectivo. Pin comprobado en Google Maps («Clínica Virgen de Guadalupe (Malabo)»)."),
    ("Estaciones de servicio del eje Malabo – aeropuerto", "Combustible", 3.7523, 8.7742,  # Google Maps: Malabo (sin gasolinera concreta como objeto)
     "Corredor con la mayor densidad de gasolineras del país, en un Estado productor de crudo. Numbeo daba 625 FCFA por litro de gasolina (~0,95 €) en septiembre de 2026, con horquilla 500-750 FCFA; el precio del gasóleo no se ha podido datar. Pin comprobado en Google Maps («Malabo (sin gasolinera concreta como objeto)»)."),
    ("Bata: abastecimiento de agua y carburante", "Agua potable", 1.8533177, 9.7790227,  # Google Maps: Bata
     "Único núcleo continental donde se puede contar con agua embotellada, hoteles con suministro y estaciones de servicio para llenar depósitos, y punto de partida de los ejes Bata–Mongomo y Bata–Ebebiyín. El agua de red NO es potable: filtrar y clorar siempre. Pin comprobado en Google Maps («Bata»)."),
]

DRONE_CALLOUT = ("danger", "NO METER EL DRON EN EL PAÍS",
                 "Guinea Ecuatorial no tiene normativa de drones publicada: la Autoridad Aeronáutica (AAGE) no ha codificado reglas para aeronaves no tripuladas, así que no existe permiso que pedir ni trámite que acredite legalidad. A la vez, el FCDO advierte de que fotografiar edificios gubernamentales, militares o aeropuertos es ilegal y puede terminar en detención, y el MAEC añade dificultades para el uso de equipos profesionales de grabación. En ese hueco legal, un dron es una confiscación probable y un interrogatorio seguro: que se quede en Camerún o en Gabón.")

STARLINK_CALLOUT = ("warn", "STARLINK ACTIVO, PERO EN RÉGIMEN PROVISIONAL",
                    "Starlink se encendió en Guinea Ecuatorial el 29 de agosto de 2026 y es el trigésimo país africano con servicio, según Space in Africa. Opera con una aprobación provisional concedida por la Vicepresidencia el 29 de julio de 2026 y bajo supervisión de GITGE, la empresa estatal de infraestructura digital; el Gobierno aún no ha fijado las condiciones definitivas. El servicio puede cambiar de precio, de distribuidor o de estatus legal con poco aviso, y en un país que ya ha cortado internet en Annobón conviene no depender de él.")

DOG_MATRIX = [
    ("Entrada por el aeropuerto de Malabo (SSG)", "permitido con condiciones", "Microchip, rabia en vigor y certificado CEXGAN ASE-3505 emitido en los 10 días previos. Volar con el perro desde Duala o Libreville; confirmar antes con la compañía aérea y con la embajada."),
    ("Entrada por frontera terrestre (Ebebiyín, Río Campo)", "por confirmar", "No hay puesto de inspección veterinaria documentado y los pasos están cerrados o son erráticos. Plan B: no intentarlo; el perro se queda con los vehículos en Camerún o Gabón."),
    ("Isla de Annobón", "no recomendado", "El MAEC desaconseja el turismo en la isla, los vuelos son muy irregulares y Freedom House documenta cortes de comunicaciones. Plan B: descartar el desplazamiento."),
    ("Isla de Corisco", "prohibido", "Requiere autorización oficial previa para cualquier visitante (MAEC); sin ella no se accede, con perro o sin él. Plan B: no incluirla en ningún plan."),
    ("Ferry Malabo – Bata («San Valentín 3»)", "por confirmar", "Travesía de 8 a 12 horas sin reglamento de pasaje ni régimen de animales publicado, y con suspensiones técnicas como la de mayo-junio de 2026. Plan B: vuelo interno de Ceiba o Cronos, previa confirmación de transporte de animales."),
    ("Regreso a la UE desde Guinea Ecuatorial", "permitido con condiciones", "Vía A obligatoria: titulación antirrábica válida hecha en la UE antes de salir. Sin ella, tres meses de espera en un tercer país listado. Plan B: no llevar al perro al país."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Guinea Ecuatorial (Ministerio de Asuntos Exteriores, UE y Cooperación, consultado el 18-IX-2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Guinea%20Ecuatorial"),
    ("MAEC · Embajada de España en Malabo (portal oficial, consultado el 18-IX-2026)", "https://www.exteriores.gob.es/Embajadas/malabo/es/Embajada/Paginas/index.aspx"),
    ("Freedom House · Equatorial Guinea: Freedom in the World 2025 (5/100, no libre)", "https://freedomhouse.org/country/equatorial-guinea/freedom-world/2025"),
    ("FCDO · Equatorial Guinea travel advice: Safety and security (gov.uk, act. 8-I-2026)", "https://www.gov.uk/foreign-travel-advice/equatorial-guinea/safety-and-security"),
    ("FCDO · Equatorial Guinea travel advice: Entry requirements (gov.uk, act. 8-I-2026)", "https://www.gov.uk/foreign-travel-advice/equatorial-guinea/entry-requirements"),
    ("Gobierno de Canadá · Equatorial Guinea travel advice and advisories (travel.gc.ca, act. 9-IX-2026)", "https://www.travel.gc.ca/destinations/equatorial-guinea"),
    ("NaTHNaC / TravelHealthPro · Equatorial Guinea (act. 2-I-2024)", "https://travelhealthpro.org.uk/country/73/equatorial-guinea"),
    ("EUR-Lex · Reglamento de Ejecución (UE) 2026/636, listas de terceros países para desplazamientos sin ánimo comercial de animales de compañía (aplicable desde el 22-IV-2026)", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600636"),
    ("EUR-Lex · Reglamento Delegado (UE) 2026/131 de la Comisión, de 20 de enero de 2026", "https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=CELEX%3A32026R0131"),
    ("Carnet de Passages · Equatorial Guinea (AIT/FIA, consultado en 2026)", "https://carnetdepassage.org/country/equatorial-guinea/"),
    ("Handervet · Viajar con perro o gato a Guinea Ecuatorial, certificado CEXGAN modelo ASE-3505", "https://handervet.com/certificados/viajar-perro-gato-guinea-ecuatorial-cexgan/"),
    ("PetTravel · Equatorial Guinea Pet Import Requirements", "https://www.pettravel.com/information/pet-passports/equatorial-guinea-pet-import-requirements/"),
    ("Space in Africa · Starlink Is Live in Equatorial Guinea (31-VIII-2026)", "https://spaceinafrica.com/2026/08/31/starlink-is-live-in-equatorial-guinea/"),
    ("Drone Laws · Drone Laws in Equatorial Guinea (act. 23-I-2025)", "https://drone-laws.com/drone-laws-in-equatorial-guinea/"),
    ("AhoraEG · Conozca los acuerdos de supresión de visados firmados por la República de Guinea Ecuatorial (9-V-2026)", "https://ahoraeg.com/politica/2026/05/09/conozca-los-acuerdos-de-supresion-de-visados-firmados-por-la-republica-de-guinea-ecuatorial/"),
    ("Revista Equato · El ferry «San Valentín 3» suspende temporalmente la ruta Malabo-Bata (15-V-2026)", "https://www.revistaequato.com/el-ferry-san-valentin-3-suspende-temporalmente-la-ruta-malabo-bata-2/"),
    ("Radio Macuto · Guía completa de los sistemas de transporte en Guinea Ecuatorial 2025 (act. 12-XII-2025)", "https://radiomacuto.org/guia-completa-de-los-sistemas-de-transporte-en-guinea-ecuatorial-2025-como-moverse-por-el-pais/"),
    ("Casa África · Ficha de país: Guinea Ecuatorial (consultado en 2026)", "https://www.casafrica.es/en/node/27"),
    ("Numbeo · Gas Prices in Equatorial Guinea (consultado en septiembre de 2026)", "https://www.numbeo.com/gas-prices/country_result.jsp?country=Equatorial+Guinea"),
    ("Chris Travel Blog · Equatorial Guinea: best 10-day itinerary with island marvels and mainland hidden gems (viaje de enero de 2024)", "https://www.christravelblog.com/equatorial-guinea-best-10-day-itinerary-with-island-marvels-and-mainland-hidden-gems/"),
    ("Once Upon a Saga · How I visited Equatorial Guinea without flying (Torbjørn Pedersen, 3-II-2016)", "https://www.onceuponasaga.dk/blog/127-how-i-visited-equatorial-guinea-without-flying"),
    ("Mind of a Hitchhiker · Equatorial Guinea (página de planificación; la autora declara no haber visitado el país)", "https://mindofahitchhiker.com/equatorial-guinea/"),
    ("Wikivoyage (en) · Equatorial Guinea travel guide", "https://en.wikivoyage.org/wiki/Equatorial_Guinea"),
    ("Wikipedia (es) · Guinea Ecuatorial", "https://es.wikipedia.org/wiki/Guinea_Ecuatorial"),
    ("Wikipedia (en) · 2026 in Equatorial Guinea", "https://en.wikipedia.org/wiki/2026_in_Equatorial_Guinea"),
    ("Wikipedia (en) · Ciudad de la Paz (capital desde el 2 de enero de 2026)", "https://en.wikipedia.org/wiki/Ciudad_de_la_Paz"),
    ("Wikipedia (en) · Malabo", "https://en.wikipedia.org/wiki/Malabo"),
    ("Wikipedia (en) · Bata, Equatorial Guinea", "https://en.wikipedia.org/wiki/Bata,_Equatorial_Guinea"),
    ("Wikipedia (en) · Malabo International Airport", "https://en.wikipedia.org/wiki/Malabo_International_Airport"),
    ("Wikipedia (en) · Bata Airport", "https://en.wikipedia.org/wiki/Bata_Airport"),
    ("Wikipedia (en) · Ebibeyin", "https://en.wikipedia.org/wiki/Ebebiyin"),
    ("Guinea Ecuatorial eVisa · portal de solicitud citado por el MAEC", "https://equatorialguinea-evisa.com/"),
    ("Malabo (Wikipedia)", "https://es.wikipedia.org/wiki/Malabo"),
    ("Catedral de Santa Isabel (Wikipedia)", "https://es.wikipedia.org/wiki/Catedral_de_Santa_Isabel_(Malabo)"),
    ("Recomendaciones de viaje MAEC", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Guinea+Ecuatorial"),
    ("Aviso de Canadá (checkpoints y fotografía)", "https://travel.gc.ca/destinations/equatorial-guinea"),
    ("Pico Basilé (Wikipedia)", "https://en.wikipedia.org/wiki/Pico_Basil%C3%A9"),
    ("Operador local con permisos (Rumbo Malabo)", "https://rumbomalabo.com/en/bioko-explorer/"),
    ("Luba Crater Scientific Reserve (Wikipedia)", "https://en.wikipedia.org/wiki/Luba_Crater_Scientific_Reserve"),
    ("Bioko, reserva de biosfera (Wikipedia)", "https://en.wikipedia.org/wiki/Bioko"),
    ("UNESCO · Guinea Ecuatorial (lista indicativa)", "https://whc.unesco.org/en/statesparties/gq"),
    ("Playa de Arena Blanca (Atlas Obscura)", "https://www.atlasobscura.com/places/playa-de-arena-blanca"),
    ("Luba (Wikipedia)", "https://en.wikipedia.org/wiki/Luba,_Equatorial_Guinea"),
    ("San Antonio de Ureca (Wikipedia)", "https://en.wikipedia.org/wiki/San_Antonio_de_Ureca"),
    ("Ureca y su pluviometría (Wikipedia es)", "https://es.wikipedia.org/wiki/San_Antonio_de_Ureca"),
    ("Bioko Sur (Wikipedia)", "https://en.wikipedia.org/wiki/Bioko_Sur"),
    ("Moka (Wikipedia)", "https://en.wikipedia.org/wiki/Moka,_Equatorial_Guinea"),
    ("Moca, valle y municipio (Wikipedia es)", "https://es.wikipedia.org/wiki/Moca_(Guinea_Ecuatorial)"),
    ("Bata (Wikipedia es)", "https://es.wikipedia.org/wiki/Bata_(Guinea_Ecuatorial)"),
    ("Monte Alén National Park (Wikipedia)", "https://en.wikipedia.org/wiki/Monte_Alen_National_Park"),
    ("Ficha KBA Monte Alén", "https://www.keybiodiversityareas.org/site/factsheet/6381"),
    ("Excursión desde Bata (Rumbo Malabo)", "https://rumbomalabo.com/en/monte-alen/"),
    ("Ciudad de la Paz / Oyala (Wikipedia es)", "https://es.wikipedia.org/wiki/Ciudad_de_la_Paz_(Guinea_Ecuatorial)"),
    ("Mongomo (Wikipedia)", "https://en.wikipedia.org/wiki/Mongomo"),
    ("Mongomo (Wikipedia es)", "https://es.wikipedia.org/wiki/Mongomo"),
    ("Ebebiyín (Wikipedia)", "https://en.wikipedia.org/wiki/Ebebiy%C3%ADn"),
    ("Niefang (Wikipedia)", "https://en.wikipedia.org/wiki/Niefang"),
    ("Cascadas de Iladyi (alternativa verificada)", "https://es.wikipedia.org/wiki/Cascadas_de_Iladyi"),
    ("Kogo / Cogo (Wikipedia)", "https://en.wikipedia.org/wiki/Cogo,_Equatorial_Guinea"),
    ("Cogo (Wikipedia es)", "https://es.wikipedia.org/wiki/Cogo"),
    ("Acalayong, el otro paso del estuario", "https://en.wikipedia.org/wiki/Acalayong"),
    ("Corisco (Wikipedia)", "https://en.wikipedia.org/wiki/Corisco"),
    ("Elobey Grande y Elobey Chico (Wikipedia)", "https://en.wikipedia.org/wiki/Elobey_Grande"),
    ("Annobón (Wikipedia)", "https://en.wikipedia.org/wiki/Annob%C3%B3n"),
    ("San Antonio de Palé (Wikipedia)", "https://en.wikipedia.org/wiki/San_Antonio_de_Pal%C3%A9"),
    ("Evinayong (Wikipedia)", "https://en.wikipedia.org/wiki/Evinayong"),
]

# Río Muni continental: Ebebiyín – Mongomo – Ciudad de la Paz – Evinayong – Monte Alén – Niefang – Bata – Cogo – estuario del Muni
CORRIDOR = [
    (2.14801, 11.33133),
    (1.62276, 11.29861),
    (1.59919, 10.8267),
    (1.44036, 10.57181),
    (1.53533, 10.12552),
    (1.83143, 10.2488),
    (1.86797, 9.76569),
    (1.08834, 9.70376),
    (0.91726, 9.31737),
]

# Bucle de la isla de Bioko: Malabo – Pico Basilé – Riaba – Moka – Ureca – Caldera de Luba – Luba – Arena Blanca – Malabo
CORRIDOR_ALT = [
    (3.75764, 8.78083),
    (3.63967, 8.77015),
    (3.3457, 8.66556),
    (3.24864, 8.56598),
    (3.35304, 8.51236),
    (3.45901, 8.55287),
    (3.528, 8.57804),
    (3.75764, 8.78083),
]

HISTORIA_RESUMEN = "Guinea Ecuatorial es el único país de África con el español como lengua oficial, y esa singularidad condiciona todo lo demás: la documentación, el trato consular y las fuentes llegan en castellano. Fue colonia española hasta el 12 de octubre de 1968, sufrió once años de terror bajo Francisco Macías Nguema y, desde el golpe del 3 de agosto de 1979, la gobierna Teodoro Obiang Nguema Mbasogo, uno de los jefes de Estado con más tiempo en el cargo del mundo. El petróleo descubierto en los años noventa multiplicó la renta media sin repartirla: Freedom House le otorga 5 puntos sobre 100 en 2025 y la clasifica como país «no libre». Queda fuera de la ruta prevista para 2027, aunque el corredor por Camerún y Gabón pasa muy cerca."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>El poblamiento del territorio es muy antiguo. En el yacimiento de Mossumu, en la provincia continental del Litoral, se han documentado restos de presencia humana atribuidos a la industria sango y datados hacia el año 30000 antes de nuestra era. La isla de Bioko estuvo unida al continente hasta que la subida del nivel del mar, tras la última glaciación, la separó en torno al 8000 a. C. Esa fractura geográfica explica buena parte de la historia posterior: la isla y el continente siguieron caminos distintos durante milenios.</p><p>Antes de la llegada de los europeos no existía un Estado unificado, sino un mosaico de formaciones políticas. En Bioko se consolidó el conjunto de clanes <em>bubi</em>, que el rey Moka llegó a unificar en buena medida a finales del siglo XIX. En la franja costera se asentaron los pueblos <em>ndowe</em>, y en Corisco el reino <em>benga</em>, que mediaría después en el comercio atlántico. El interior continental estaba organizado en villas-estado de clanes <em>fang</em>, sin autoridad central, y algunas estructuras protoestatales recibieron influencia del reino de Oyo y del reino del Congo. Los annoboneses, en cambio, son una población posterior, formada en la isla de Annobón a partir del tráfico de esclavos, con criollo propio.</p>"),
    ("Colonización",
     "<p>El navegante portugués Fernão do Pó situó Bioko en los mapas europeos en 1471 y el 1 de enero de 1472 se avistó Annobón, que tomó el nombre del día. Desde 1494 Portugal instaló factorías esclavistas en Bioko, Annobón y Corisco. Los tratados de San Ildefonso (1777) y de El Pardo (1778) traspasaron las islas a España junto con derechos de comercio en el golfo de Guinea. La expedición del conde de Argelejo zarpó de Montevideo en abril de 1778 para tomar posesión; el territorio quedó bajo la jurisdicción del Virreinato del Río de la Plata hasta 1810.</p><p>Entre 1827 y 1843 los británicos ocuparon Fernando Poo con el pretexto de combatir la trata y fundaron Port Clarence, luego Santa Isabel y hoy Malabo. Juan José Lerena reafirmó la soberanía española en marzo de 1843. Río Muni fue protectorado en 1885 y colonia en 1900, con los límites fijados por el tratado de París. En 1926 islas y continente se unificaron como colonia de Guinea Española. España levantó grandes plantaciones de cacao en Fernando Poo con miles de braceros nigerianos, pero apenas dejó infraestructura. En 1959 el territorio pasó a ser provincia española de ultramar y en diciembre de 1963 un referéndum aprobó la autonomía. Lo que quedó al marcharse fue una lengua, el español, y una economía de plantación.</p>"),
    ("Independencia y construcción del Estado",
     "<p>Un referéndum aprobó la Constitución en agosto de 1968 con cerca del 63 % de los votos, bajo observación de Naciones Unidas, y el 12 de octubre se proclamó la independencia. Francisco Macías Nguema fue el primer presidente. La concentración de poder fue inmediata: el opositor Bonifacio Ondó Edu murió en enero de 1969 y una supuesta intentona sirvió de coartada para una represión masiva. En julio de 1970 nació el partido único, en julio de 1972 Macías se proclamó presidente vitalicio y en 1973 una nueva Constitución liquidó el reparto de poder.</p><p>El régimen cerró las escuelas en 1975, prohibió todo culto cristiano en junio de 1978 y africanizó la toponimia: Santa Isabel pasó a llamarse Malabo. Más de 100.000 personas huyeron a los países vecinos, al menos 50.000 de las que se quedaron murieron y otras 40.000 fueron condenadas a trabajos forzados. El 3 de agosto de 1979 su sobrino, el teniente coronel Teodoro Obiang Nguema Mbasogo, lo derrocó en el llamado «Golpe de la Libertad»; Macías fue juzgado y ejecutado, y un Consejo Militar Supremo gobernó hasta la Constitución de 1982. El partido gubernamental se fundó en 1987 y Obiang venció como candidato único en 1989. La apertura de 1991 fue nominal: en las legislativas de 1993 diez de los catorce partidos quedaron fuera y la abstención rozó el 80 %.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>El petróleo lo cambió todo. Mobil inició la extracción a mediados de los años noventa y el país pasó a ser uno de los mayores productores del África subsahariana, aunque, según Britannica, el entorno del presidente se apropió del grueso de esos ingresos. En 2004 fracasó una trama de mercenarios para derrocar a Obiang. La reforma constitucional de 2011 creó un Parlamento bicameral y límites de mandato, leídos por los observadores como un refuerzo del ejecutivo. El hijo mayor del presidente, Teodoro Nguema Obiang Mangue, «Teodorín», fue nombrado vicepresidente y condenado en París en 2017 por corrupción.</p><p>Las intentonas de 2017 y 2019 derivaron en el macroproceso de Bata-Ngolo, con 130 condenados en 2019 a penas de hasta noventa y seis años. En 2021 la explosión de un polvorín cerca de Bata causó unos 98 muertos. En 2022 se abolió la pena de muerte. En julio de 2024 el Gobierno cortó las comunicaciones de Annobón tras las protestas contra la minería y detuvo a manifestantes que la ONU consideró presos arbitrarios; entraron en el indulto de 476 reclusos de junio de 2025. Ese mismo año la Corte Internacional de Justicia le dio la razón frente a Gabón por las islas Mbañé, Conga y Cocoteros. En enero de 2026 Obiang declaró capital a Ciudad de la Paz, la urbe construida en la selva continental, en sustitución de Malabo.</p>"),
    ("Política y gobierno en 2026",
     "<p>Es una república presidencialista. A septiembre de 2026, según la Ficha País del Exteriores español de julio, el jefe del Estado es Teodoro Obiang Nguema Mbasogo, en el cargo desde el golpe del 3 de agosto de 1979 y uno de los gobernantes con más años del mundo. El primer ministro es Manuel Osa Nsue Nsua y el vicepresidente es su hijo Teodorín. Las últimas generales fueron las de noviembre de 2022, arrasadas por el partido gubernamental; las siguientes se prevén para 2029.</p><p>No es una democracia. Freedom House lo clasificó en 2025 como «no libre» con 5 puntos sobre 100 —cero de cuarenta en derechos políticos— y afirma que «celebra elecciones periódicas, pero el voto no es ni libre ni justo», que el poder y la riqueza petrolera se concentran en la familia presidencial y que la seguridad tortura con impunidad. No hay medios independientes: la televisión estatal y un canal «privado» del vicepresidente, que Reporteros Sin Fronteras considera propaganda. En corrupción ocupó el puesto 173 de 180 en 2024. Sin conflicto armado, el Exteriores advierte el 19 de junio de 2026 del aumento de la delincuencia en Malabo y Bata y de los continuos controles policiales y militares en carretera. Con España rige un Tratado de Amistad y Cooperación desde 1980, y pertenece a la Unión Africana, que admitió el español como lengua de trabajo en 2020.</p>"),
    ("Economía y recursos",
     "<p>La riqueza del país está en el subsuelo. Según el Exteriores español, en julio de 2026 los hidrocarburos suponían entre el 35 % y el 40 % del PIB nominal y más del 90 % de las exportaciones; el resto, la madera, los productos químicos y el cacao, con pesca y agricultura poco desarrolladas. El PIB rondó los 12.800 millones de dólares en 2024 según el Banco Mundial. La renta por habitante ronda los 8.000 dólares nominales, alta para la región pero sin reflejo en el bienestar: el Exteriores estima la pobreza en torno al 61 % en 2025 y Amnistía Internacional, citando al Banco Mundial, en el 57 % en 2024.</p><p>La economía lleva en recesión desde 2013, con la salvedad de 2022. El Banco Mundial calcula una caída del 5,4 % en 2025 y el Fondo Monetario otro del 2,7 % en 2026, arrastrados por los precios del crudo y el declive de los yacimientos. La deuda pública rondaba el 36 % del PIB en 2025. La moneda es el franco CFA, con paridad fija con el euro en torno a 656 francos, dentro de la zona monetaria que comparte con Camerún, Gabón, Chad, Congo y la República Centroafricana. Los grandes proyectos apuntan al gas, con inversión estadounidense de ConocoPhillips y Chevron, y al plan de diversificación «Horizonte 2035». La obra más visible es Ciudad de la Paz.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>La población rondaba 1,67 millones de habitantes en 2025 según la estadística oficial del Exteriores español, con un 76 % urbano y un 90 % de alfabetización. El español es la lengua oficial y la vehicular real; el francés, cooficial desde 1998, y el portugués, desde 2010, tienen penetración irrelevante. En la carretera y en los controles uno se entiende en castellano, aunque en casa se hablan el fang, el bubi, el annobonés y el criollo <em>pichinglish</em>. Según cifras de 2020, los fang son el 85,7 % de la población y los bubis el 6,5 %; el cristianismo reúne al 88,7 %.</p><p>La danza <em>balele</em> recorre la costa, concentrándose en Bioko en Navidad. La cocina se apoya en la yuca, el ñame y el plátano macho; el plato más popular es el <em>pepesup</em>, sopa picante de pescado, y se bebe vino de palma o <em>topé</em> y <em>malamba</em> de caña. La fiesta nacional es el 12 de octubre. No hay bienes inscritos en la Lista del Patrimonio Mundial, pero sí seis candidaturas, como el parque nacional de Monte Alén. Para quien viaja: vestir con discreción, <strong>no fotografiar jamás militares, policía, aeropuertos ni edificios oficiales</strong> y llevar pasaporte y visado, porque los controles los piden a diario. El alcohol es legal y el ramadán, que en 2027 empieza hacia el 8 de febrero, apenas afecta fuera de la minoría musulmana.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Guinea Ecuatorial (MAEC España · Oficina de Información Diplomática · julio de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/GUINEAECUATORIAL_FICHA%20PAIS.pdf"),
    ("Recomendaciones de viaje: Guinea Ecuatorial (MAEC España · actualizado 19 de junio de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Guinea+Ecuatorial"),
    ("Equatorial Guinea: Freedom in the World 2025 (Freedom House · 2025)", "https://freedomhouse.org/country/equatorial-guinea/freedom-world/2025"),
    ("Equatorial Guinea: Independence (Encyclopaedia Britannica · consultado en septiembre de 2026)", "https://www.britannica.com/place/Equatorial-Guinea/Independence"),
    ("Guinea Ecuatorial (Wikipedia en español · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Guinea_Ecuatorial"),
    ("Equatorial Guinea (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Equatorial_Guinea"),
    ("Teodoro Obiang (Wikipedia en español · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Teodoro_Obiang"),
    ("Equatorial Guinea: States Parties (UNESCO · Centro del Patrimonio Mundial · consultado en septiembre de 2026)", "https://whc.unesco.org/en/statesparties/gq"),
    ("Equatorial Guinea (Reporteros Sin Fronteras · Clasificación Mundial de la Libertad de Prensa · consultado en septiembre de 2026)", "https://rsf.org/en/country/equatorial-guinea"),
    ("Human rights in Equatorial Guinea (Amnistía Internacional · informe anual 2025)", "https://www.amnesty.org/en/location/africa/west-and-central-africa/equatorial-guinea/report-equatorial-guinea/"),
    ("Obiang designa la Ciudad de la Paz como nueva capital de Guinea Ecuatorial (Infobae · EFE · 3 de enero de 2026)", "https://www.infobae.com/america/agencias/2026/01/03/obiang-designa-la-ciudad-de-la-paz-como-nueva-capital-de-guinea-ecuatorial/"),
    ("Gastronomía de Guinea Ecuatorial (Wikipedia en español · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Gastronom%C3%ADa_de_Guinea_Ecuatorial"),
    ("Cultura de Guinea Ecuatorial (Wikipedia en español · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Cultura_de_Guinea_Ecuatorial"),
]

SPEC = dict(
    slug="guinea-ecuatorial", name="Guinea Ecuatorial", revision="18 sep 2026",
    sub="FUERA DE RUTA — fronteras terrestres cerradas desde el 15-XII-2025 · solo avión o barco · visado obligatorio de 105 € · el único país africano de lengua española",
    chips=[
        ("ESTATUS", "FUERA DE RUTA. El corredor pasa al lado, por Camerún y Gabón…"),
        ("CÓMO LLEGAR", "En la práctica solo por aire o mar: aeropuertos de Malabo (SSG, isla de Bioko) y Bata (BSG, continente)…"),
        ("VISADO", "OBLIGATORIO para españoles. No hay exención en vigor…"),
        ("VEHÍCULO", "Sin organización AIT/FIA emisora de CPD en el país (carnetdepassage.org)…"),
        ("SEGURIDAD", "Precaución (MAEC) · Freedom House 5/100, no libre"),
        ("SEGURO", "Carta Verde no vale · Carte Rose CEMAC sin confirmar"),
        ("SALUD", "Fiebre amarilla OBLIGATORIA · malaria alto riesgo"),
        ("DRONES", "Sin normativa · foto de edificios oficiales penada"),
        ("STARLINK", "Activo desde 29-VIII-2026, aprobación provisional"),
        ("4x4", "Inviable: Bioko es isla y el continente está cerrado"),
        ("A PIE", "Solo de día · pasaporte y visado siempre encima"),
        ("PERRO", "Microchip ISO, rabia en vigor y certificado veterinario oficial (CEXGAN, modelo ASE-3505, válido 10 días)…"),
        ("MONEDA", "Franco CFA de África Central (XAF), paridad fija 1 € = 655,957 FCFA…"),
        ("VENTANA", "Ecuatorial: media anual en torno a 25 °C y más de 2.000 mm de lluvia…"),
    ],
    center=[1.18, 8.48], zoom=6,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Río Muni continental: Ebebiyín – Mongomo – Ciudad de la Paz – Evinayong – Monte Alén – Niefang – Bata – Cogo – estuario del Muni",
    corridor_alt_label="Bucle de la isla de Bioko: Malabo – Pico Basilé – Riaba – Moka – Ureca – Caldera de Luba – Luba – Arena Blanca – Malabo",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Pico_Basil%C3%A9.jpg?width=1200",
    hero_credit="Pico Basilé · Serge Moons · CC BY-SA 3.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Guinea Ecuatorial queda fuera de la ruta de 2027 aunque el corredor Camerún–Gabón pase a pocos kilómetros de Ebebiyín. La razón es operativa, no sentimental: el MAEC certifica que las fronteras terrestres del Río Muni sufren «constantes cierres y reaperturas, generalmente sin preaviso» desde el 15 de diciembre de 2025 y desaconseja expresamente el acceso terrestre a quien no sea nacional de la CEMAC. A eso se suma un visado obligatorio de 105 € que hay que tramitar antes, la ausencia de organización emisora de CPD en el país, un régimen que Freedom House puntúa con 5 sobre 100 y la prohibición penal de fotografiar edificios oficiales, aeropuertos y militares. Con dos 4x4 españoles, un perro y una media de 250 km/día, meter aquí una incógnita de frontera que puede costar días o el rechazo directo no compensa. Si algún día se quisiera hacer, la forma realista es dejar los coches en Kribi o Libreville y entrar en avión a Malabo (SSG) desde Duala o Libreville: cuatro o cinco días y del orden de 1.200 a 1.600 € por persona entre visado, vuelos, transporte local y alojamiento, con el perro esperando en Gabón o Camerún. Lo que habría que decidir antes es si hay reapertura estable de Ebebiyín/Kye-Ossi confirmada por escrito por la embajada y si se acepta pagar un desvío que no aporta ruta.",
    facts=[
        ("Estatus", "FUERA DE RUTA. El corredor pasa al lado, por Camerún y Gabón, pero no se entra: fronteras terrestres cerradas o erráticas y visado previo obligatorio."),
        ("Cómo llegar", "En la práctica solo por aire o mar: aeropuertos de Malabo (SSG, isla de Bioko) y Bata (BSG, continente), y ferry Malabo–Bata. Bioko y Annobón no tienen acceso por carretera."),
        ("Visado", "OBLIGATORIO para españoles. No hay exención en vigor. eVisa en equatorialguinea-evisa.com, 105 € para estancias de menos de 90 días (MAEC, 2026)."),
        ("Vehículo/aduana", "Sin organización AIT/FIA emisora de CPD en el país (carnetdepassage.org). Admisión temporal por passavant de aduana, sin procedimiento publicado: POR CONFIRMAR."),
        ("Seguro", "La Carta Verde NO cubre. Zona CEMAC: hace falta seguro local o Carte Rose CEMAC contratada en frontera o en aseguradora de Malabo o Bata. Importe POR CONFIRMAR."),
        ("Moneda", "Franco CFA de África Central (XAF), paridad fija 1 € = 655,957 FCFA. Efectivo obligatorio: las tarjetas apenas se aceptan (MAEC)."),
        ("Perro", "Microchip ISO, rabia en vigor y certificado veterinario oficial (CEXGAN, modelo ASE-3505, válido 10 días). Entrada de animales por el aeropuerto de Malabo."),
        ("Drones", "Sin normativa publicada y fotografía de edificios oficiales, aeropuertos y militares penada con detención. En la práctica: NO LLEVAR DRON."),
        ("Starlink", "ACTIVO desde el 29 de agosto de 2026 con aprobación provisional del Gobierno y supervisión de GITGE. Kit estándar ~451.200 FCFA; plan residencial ~52.200 FCFA/mes."),
        ("Seguridad", "MAEC: «se recomienda viajar con precaución». Freedom House 2025: 5/100, «no libre». Controles policiales y militares continuos con petición de documentación."),
        ("Clima", "Ecuatorial: media anual en torno a 25 °C y más de 2.000 mm de lluvia. En Malabo, 1.850 mm y estación seca corta de diciembre a febrero; en el continente, lluvias en abril-mayo y octubre-diciembre."),
        ("Sanidad", "Fiebre amarilla OBLIGATORIA desde los 9 meses. Malaria de alto riesgo en todo el país y todo el año. Sin convenio de Seguridad Social y sin servicio de ambulancias."),
    ],
    alerts=[
        "FRONTERAS TERRESTRES CERRADAS. El MAEC informa de cierres y reaperturas constantes sin preaviso desde el 15 de diciembre de 2025 y desaconseja el acceso terrestre a los no nacionales de la CEMAC.",
        "VISADO OBLIGATORIO Y CARO. 105 € para menos de 90 días, tramitado antes por eVisa; no existe exención para españoles pese a los anuncios de supresión de visados que circulan.",
        "FOTOGRAFIAR ES DELITO. El FCDO advierte de que fotografiar edificios gubernamentales, militares o aeropuertos es ilegal y puede acabar en arresto y detención.",
        "CONTROLES CONTINUOS. Policía y militares paran a diario en carretera y piden pasaporte y visado; Canadá documenta intentos de cobro de sobornos en los retenes de Malabo y Bata.",
        "BIOKO Y ANNOBÓN SOLO POR AIRE O MAR. Malabo está en una isla: un 4x4 europeo no llega por carretera. Annobón está a cientos de kilómetros en el Atlántico y el MAEC desaconseja visitarla.",
        "SIN CPD EMISOR NI PROCEDIMIENTO PUBLICADO. AIT/FIA no tiene asociación emisora en el país y no hay norma pública de admisión temporal de vehículos extranjeros.",
        "RÉGIMEN AUTORITARIO. Teodoro Obiang gobierna desde el golpe del 3 de agosto de 1979 y es el jefe de Estado con más años en el cargo del mundo; Freedom House le da 0/40 en derechos políticos y 5/60 en libertades civiles.",
        "SANIDAD PRECARIA. No hay ambulancias; se exige seguro con evacuación médica y la referencia son dos centros privados de Malabo que cobran por adelantado.",
        "CORISCO Y ZONAS MILITARES CON PERMISO. El MAEC señala que Corisco requiere autorización oficial previa y que hay que evitar instalaciones militares y presidenciales.",
        "EFECTIVO O NADA. Franco CFA en un país con aceptación mínima de tarjeta: hay que entrar con euros en metálico y cambiar.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada por Ebebiyín", "Kye-Ossi (Camerún) o frontera gabonesa – Ebebiyín", "~20 km · 1 día (trámites)"),
        ("2 · Ebebiyín – Mongomo", "Ebebiyín – Nsok-Nsomo – Mongomo", "~95 km · 1 día"),
        ("3 · Mongomo – Ciudad de la Paz", "Mongomo – Mengomeyén – Ciudad de la Paz (Djibloho)", "~60 km · 1 día"),
        ("4 · Ciudad de la Paz – Evinayong", "Djibloho – Añisoc o Nsork-Nsomo – Evinayong", "~90 km · 1 día"),
        ("5 · Evinayong – Monte Alén", "Evinayong – acceso al Parque Nacional de Monte Alén", "~70 km · 1 día"),
        ("6 · Monte Alén", "Base del parque – lago Atoc – vivac – regreso", "~25 km + marcha · 2 días"),
        ("7 · Monte Alén – Bata", "Monte Alén – Niefang – Bata", "~130 km · 1 día"),
        ("8 · Bata", "Ciudad, puerto, paseo marítimo, logística y repostaje", "0 km · 1 día"),
        ("9 · Bata – Cogo", "Bata – Mbini – Acalayong – Cogo (Puerto Iradier)", "~121 km · 1 día"),
        ("10 · Estuario del Muni", "Cogo – Elobey Chico – Corisco (en cayuco, sin vehículos)", "~60 km náuticos · 2 días"),
        ("11 · Regreso a Bata", "Cogo – Bata", "~121 km · 1 día"),
        ("12 · Travesía a Bioko", "Bata – Malabo en ferry (Viteoca / naviera Doña Cándida); carga de vehículos POR CONFIRMAR", "~250 km marítimos · 1 día"),
        ("13 · Bioko norte", "Malabo – Pico Basilé – Malabo (con permiso)", "~90 km · 1 día"),
        ("14 · Bioko sur", "Malabo – Riaba – Moka – Luba – Arena Blanca – Ureca – Malabo", "~230 km · 4 días"),
    ],
    offroad=[
        "El país tiene, según Wikivoyage, uno de los mejores sistemas de carreteras de África central: los ejes Bata-Niefang-Mongomo-Ebebiyín y Malabo-Luba están asfaltados y en buen estado, así que aquí el 4x4 no sirve para ir más lejos sino para llegar a los sitios donde no hay asfalto.",
        "La verdadera pista del país es la bajada de Luba a San Antonio de Ureca por Belebu, en el sur de Bioko: barro, pendientes y vadeos, solo transitable en temporada seca y con permiso de seguridad tramitado, según el aviso oficial canadiense que exige autorización para Moka, Pico Basilé y Ureca.",
        "La subida al Pico Basilé combina asfalto y pista hasta las antenas de la cumbre, a 3.011 m; es la ascensión rodada más espectacular del país, pero termina en una instalación de RTVGE y de comunicaciones donde la fotografía está prohibida y el control es militar.",
        "El interior de la Gran Caldera de Luba NO tiene acceso rodado: la reserva científica se alcanza a pie tras dos días de marcha, y Wikipedia documenta que hacia 2010 estaba en construcción una carretera de Belebu a Ureca que atravesaría la reserva; su estado actual está por confirmar y conviene comprobarlo en destino.",
        "En Río Muni, las pistas forestales de los alrededores de Monte Alén y de la sierra de Niefang solo se recorren con guía y permiso del parque: el operador local incluye permisos de entrada y acompañamiento, y la caza furtiva activa dentro del parque hace desaconsejable circular por libre.",
        "Zonas vetadas de facto: los accesos a puertos, aeropuertos, instalaciones militares y al entorno del palacio presidencial; el aviso canadiense recoge que los controles y registros son habituales dentro y alrededor de Malabo y Bata, y el británico que en los controles se piden pasaporte y documentación del vehículo y se dan casos frecuentes de petición de soborno.",
        "No se conduce de noche: tanto el MAEC como el FCDO desaconsejan expresamente los desplazamientos por carretera después del anochecer por robos, mala iluminación y conducción agresiva.",
        "Lo que NO hemos podido verificar: no hay información abierta sobre importación temporal de vehículos, carnet de passages, seguro obligatorio ni permiso internacional de conducir para Guinea Ecuatorial. La ficha de WikiOverland devolvió error 401 y no existe cobertura de Tracks4Africa ni de iOverlander para el país. Hay que consultarlo con la embajada antes de planificar.",
    ],
    senderismo=[
        "Lago Biaó desde Moka: unos 8 km y 559 m de desnivel, alrededor de 4 horas ida y vuelta por selva de montaña hasta un lago de cráter; es la marcha más accesible y mejor documentada de Bioko (fuente: Rumbo Malabo).",
        "Cumbre del Pico Basilé: 3.011 m; se puede subir en 4x4 casi hasta arriba, pero el último tramo a pie por el brezal de altura es la única forma de pisar el techo del país. Permiso de seguridad obligatorio.",
        "Cascadas de Iladyi (Ilachi) desde Moka: sendero selvático hasta un salto de tres ramas encajado en un cañón, en el valle de Moka; sin datos abiertos de distancia ni de altura de la cascada.",
        "Cascadas de Bilelipa, en el este de Bioko: travesía de jungla de unas 6 horas desde un poblado cercano a Riaba, con ruinas coloniales, varios vados de río y baño en la poza; el operador la describe como una de las cascadas más altas de la isla.",
        "Travesía a la Gran Caldera de Luba: dos jornadas de marcha por selva primaria hasta el interior de la reserva científica, con vivac; es la excursión más exigente del país y requiere guía, porteadores y permisos.",
        "Playas de desove de Ureca (Moaba y Moraka): caminatas cortas por la costa sur, casi siempre nocturnas y acompañadas de guía, de noviembre a marzo, para ver desovar tortugas marinas.",
        "Monte Alén: la red de senderos del parque está trazada y mantenida según Wikipedia; la ruta clásica es la marcha desde la base hasta el lago Atoc, con vivac y salida de fauna al amanecer.",
        "Estuario del Muni desde Cogo: no es senderismo propiamente dicho, sino paseos cortos por los manglares y por las ruinas coloniales combinados con cayuco; útil como jornada suave entre etapas largas.",
    ],
    acampada=[
        "No hay campings comerciales documentados en Guinea Ecuatorial: ninguna fuente abierta consultada (Wikivoyage, operadores locales, avisos oficiales) menciona un solo camping con instalaciones.",
        "iOverlander apenas cubre el país: las búsquedas solo devolvieron una ficha, y no de acampada sino de embarque de vehículos («ferry to Malabo · Vehicle Shipping»), cuyo detalle no se pudo leer porque la página exige inicio de sesión. Tracks4Africa no devolvió nada. Esto es, en sí mismo, un dato: aquí no hay comunidad overlander establecida y no se puede planificar con fichas de terceros.",
        "La acampada organizada existe dentro del Parque Nacional de Monte Alén: el operador local incluye tiendas y una zona designada de acampada junto al lago Atoc, con permiso de entrada al parque incluido.",
        "En Bioko, la referencia es la playa de Moaba, cerca de Ureca: el operador local la describe como el mejor lugar del país para acampar, sin hoteles en los alrededores, y advierte expresamente de acampar EN LA SELVA Y NUNCA SOBRE LA PROPIA PLAYA, por los nidos de tortuga.",
        "La Caldera de Luba se recorre en régimen de vivac: hay estaciones estacionales de biomonitoreo en las playas de Moraka y Moaba, pero no son alojamiento público; cualquier pernocta allí pasa por un operador o por el programa científico.",
        "Acampada libre por libre: desaconsejada. Con controles policiales continuos, prohibición de fotografiar y un aviso de delincuencia nocturna en aumento en Malabo y Bata, plantar tienda sin permiso ni contacto local es pedir un problema administrativo.",
        "Alternativa realista para dos 4x4 con tienda de techo: dormir en recintos cerrados de hoteles en Malabo, Bata y Luba, que es caro (Wikivoyage habla de 100-400 euros por habitación básica), y reservar la tienda para Monte Alén y Ureca con operador.",
        "Consejo de la fuente local para acampar aquí: repelente, linterna, agua, sábana ligera en vez de manta, botiquín y hoguera; el clima ronda los 25 °C todo el año y la molestia principal son cangrejos y hormigas, no el frío.",
    ],
    visado=[
        "OBLIGATORIO para españoles. El MAEC no reconoce ninguna exención en vigor: los acuerdos de supresión de visados firmados por Guinea Ecuatorial —38 países según AhoraEG, 9 de mayo de 2026— no incluyen a España ni a ningún Estado de la UE, y casi todos se limitan a pasaportes diplomáticos, oficiales y de servicio.",
        "MODALIDAD: eVisa previa en https://equatorialguinea-evisa.com/, con alternativa presencial en la Embajada de Guinea Ecuatorial. El FCDO cita un plazo de tramitación de 72 horas; un viajero documentó en enero de 2024 que el sistema electrónico no le funcionó y tuvo que tramitarlo por embajada, con los documentos traducidos al inglés.",
        "COSTE: 105 € para estancias inferiores a 90 días (MAEC, recomendaciones de viaje vigentes en 2026).",
        "PASAPORTE con validez mínima de seis meses y certificado de vacunación contra la fiebre amarilla. El MAEC insiste en llevar documentación original y no usar intermediarios.",
        "EN FRONTERA TERRESTRE no hay visado a la llegada y el eVisa no garantiza el paso: el MAEC desaconseja el acceso terrestre a los no CEMAC y los puestos cierran sin aviso. Hay que exigir el SELLO DE ENTRADA en el pasaporte antes de salir del puesto; el FCDO documenta problemas posteriores por sellos mal puestos.",
        "MÁS DE 90 DÍAS: permiso de residencia de un año ante el Ministerio de Seguridad Nacional (FCDO, 8-I-2026). Canadá añade que a sus nacionales se les exige además certificado de antecedentes penales.",
    ],
    fronteras_rows=[
        ("Aeropuerto internacional", "Malabo (SSG), Punta Europa, isla de Bioko", "Vía de entrada realista. Conexiones con Duala, Libreville, Adís Abeba, París, Fráncfort y Casablanca. Único punto documentado de entrada para animales de compañía (Wikipedia / PetTravel, 2026)."),
        ("Aeropuerto", "Bata (BSG), a 4 km al norte de Bata, continente", "Segunda puerta de entrada. Vuelos a Malabo con Ceiba y Cronos (30-40 min, varios diarios) y a Libreville con Afrijet. Vuelos a Annobón muy irregulares y a menudo cancelados (Radio Macuto, act. 12-XII-2025)."),
        ("Paso terrestre con Camerún", "Ebebiyín / Kye-Ossi (noreste, junto al trifinio)", "Carretera asfaltada por los dos lados, pero CERRADO O ERRÁTICO: cierres y reaperturas sin preaviso desde el 15-XII-2025 (MAEC). Canadá cita cierres periódicos por zonas fronterizas en disputa pese al acuerdo de 2020."),
        ("Paso terrestre con Camerún", "Campo / Río Campo (costa noroeste)", "Wikivoyage advierte de que el acceso desde Campo «puede estar cerrado con frecuencia» y Casa África recuerda que el MAEC avisa de cierres frecuentes en Río Campo y Ebebiyín. Estado 2026 SIN CONFIRMAR."),
        ("Paso terrestre con Gabón", "Ebebiyín / Meyo-Kye (Bitam por el lado gabonés)", "Mismo régimen de cierres del continente. Es el eje por el que se ha documentado alguna entrada overland, pero ninguna reciente ni verificable."),
        ("Paso fluvial con Gabón", "Acalayong / Cocobeach (estuario del Muni)", "Solo en barca o piragua por el estuario: NO SIRVE PARA VEHÍCULO PROPIO. Horarios y estado 2026: por confirmar."),
        ("Enlace marítimo interior", "Ferry Malabo – Bata, buque «San Valentín 3» (SEMAPORT S.L.)", "Travesía de 8 a 12 horas. Suspendido del 22 de mayo al 30 de junio de 2026 por revisión técnica programada (Revista Equato, 15-V-2026). Admisión de vehículos: POR CONFIRMAR. Teléfonos de SEMAPORT: 222 78 24 88 / 222 08 10 22."),
        ("Puerto internacional", "Puerto de Malabo y puerto de Bata", "Bata tiene uno de los muelles más profundos de la región (6,5 Mt y 300.000 TEU/año) con línea a Duala; Malabo, unas 200.000 t/año. Vía teórica para meter un vehículo, sin tarifas ni procedimiento publicados."),
        ("Destino con permiso", "Isla de Corisco y Annobón", "Corisco exige autorización oficial previa (MAEC). Annobón: el MAEC desaconseja el turismo y Freedom House documenta cortes de internet y de telefonía móvil impuestos en la isla en 2024."),
    ],
    vehiculos=[
        "NO HAY RUTA POSIBLE CON LOS COCHES. Malabo está en Bioko y solo se alcanza por aire o mar; el continente (Río Muni) está detrás de fronteras cerradas o erráticas desde diciembre de 2025.",
        "CPD: carnetdepassage.org confirma que AIT/FIA NO tiene ninguna organización emisora de carnet de passages en Guinea Ecuatorial y que los vehículos matriculados allí deben obtenerlo fuera. Que se admita un CPD extranjero en frontera está SIN CONFIRMAR.",
        "ADMISIÓN TEMPORAL: sin norma pública localizada. Lo previsible en la zona CEMAC es un passavant o laissez-passer de aduana de validez corta emitido en el puesto, pero no hay fuente oficial que lo documente para este país.",
        "SEGURO: la Carta Verde europea no tiene validez en África Central. El sistema regional es la Carte Rose CEMAC, exigible para circular; habría que contratarla en frontera o en una aseguradora local. Importe y punto de venta POR CONFIRMAR.",
        "CONDUCCIÓN POR LA DERECHA, igual que en España y que en Camerún y Gabón.",
        "PERMISO DE CONDUCIR: el MAEC señala «cierta indefinición jurídica» sobre la validez del permiso internacional y recomienda convalidar el permiso ante la Dirección General de Tráfico ecuatoguineana. Llevar permiso español y permiso internacional de todos modos.",
        "CARRETERAS: la red asfaltada del continente es de las mejores de África Central según Wikivoyage, con los ejes Bata–Mongomo, Bata–Ebebiyín y Bata–Kogo, y en Bioko la autovía Malabo–Luba. Canadá describe conducción agresiva, alcohol al volante y retenes frecuentes cerca de Malabo y Bata donde se intenta cobrar sobornos.",
        "NO CONDUCIR DE NOCHE: el MAEC lo desaconseja expresamente tanto en ciudad como en zona rural, y recomienda no usar taxis no oficiales.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "SIN NORMATIVA. Drone Laws (actualización de 23 de enero de 2025) confirma que la Autoridad Aeronáutica de Guinea Ecuatorial (AAGE) no ha publicado reglas para UAS y que el vuelo de visitantes extranjeros figura como restringido o desaconsejado.",
        "El único contacto localizado de la autoridad es el teléfono de la AAGE, +240 222 27 66 07. No hay portal de trámites, formulario ni tasa publicada.",
        "La prohibición real no es de dron sino de imagen: el FCDO (8-I-2026) y Canadá (9-IX-2026) coinciden en que fotografiar instalaciones militares, edificios de gobierno, aeropuertos y puertos está prohibido y se detiene por ello.",
        "El MAEC recomienda obtener autorizaciones previas para equipos profesionales de grabación; sin un contacto oficial identificado que las emita, esa vía es teórica.",
        "Recomendación operativa: el dron se queda fuera del país. Si hubiera que entrar con él por conexión aérea, declararlo en aduana y asumir depósito o confiscación.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "DISPONIBLE desde el 29 de agosto de 2026, con página de pedidos activa en starlink.com (Space in Africa, 31-VIII-2026).",
        "Precios de lanzamiento: kit Mini unos 383.600 FCFA (~680 USD) y kit estándar unos 451.200 FCFA (~800 USD); plan estándar 34.800 FCFA/mes (~62 USD) y residencial ilimitado 52.200 FCFA/mes (~92 USD).",
        "Aprobación PROVISIONAL de julio de 2026 supervisada por GITGE: el marco regulatorio definitivo está pendiente, así que no se puede dar el servicio por estable de cara a 2027.",
        "Si se entrase con un terminal propio en itinerancia regional, hay que contar con que la aduana lo trate como equipo de telecomunicaciones y pida justificación. Sin fuente que lo confirme: POR CONFIRMAR.",
        "Operadores móviles y SIM turística: el mercado lo cubren Muni (GETESA) y Orange GQ, pero los requisitos de registro de SIM para extranjeros no se han podido verificar. POR CONFIRMAR.",
    ],
    perro_intro=[
        "ENTRADA: microchip ISO 11784/11785 implantado antes de la vacunación, vacuna antirrábica en vigor —entre 30 días y 12 meses antes de la entrada según PetTravel, con un mínimo de 21 días desde la primovacunación en la práctica CEXGAN— y certificado veterinario oficial del país de origen.",
        "CERTIFICADO: desde España se tramita por CEXGAN con el modelo ASE-3505 específico de Guinea Ecuatorial, o bien certificado genérico CEXGAN más CVS, o pasaporte europeo legalizado por veterinario acreditado. Examen clínico como máximo 10 días antes y desparasitación entre 10 y 30 días antes; el certificado CADUCA A LOS 10 DÍAS de emitirse.",
        "PERMISO PREVIO: PetTravel indica que los perros y gatos que viajan con su dueño NO necesitan permiso de importación, y que no habrá cuarentena si se cumplen los requisitos. Sin confirmación por fuente oficial ecuatoguineana.",
        "PUNTO DE ENTRADA: los animales de compañía deben entrar por el Aeropuerto Internacional de Malabo. No hay constancia de puesto de inspección fronteriza terrestre habilitado para animales.",
        "RAZAS PROHIBIDAS: Guinea Ecuatorial no publica lista oficial de razas prohibidas (PetTravel). No se ha localizado ninguna norma al respecto.",
        "VUELTA A LA UE: Guinea Ecuatorial NO figura en las listas del Reglamento de Ejecución (UE) 2026/636, aplicable desde el 22 de abril de 2026 —de África solo aparecen Ascensión, Mauricio y Santa Elena—. Por tanto, regreso por VÍA A: titulación de anticuerpos antirrábicos en laboratorio autorizado por la UE, con la muestra tomada al menos 30 días después de la vacunación y al menos 3 meses antes de la entrada, hecha ANTES de salir de la UE y anotada en el pasaporte del animal, conforme al Reglamento Delegado (UE) 2026/131.",
        "RIESGOS SANITARIOS: rabia presente en animales domésticos (TravelHealthPro), calor y humedad ecuatoriales constantes con más de 2.000 mm de lluvia al año, y ninguna clínica veterinaria verificada en Malabo ni en Bata. Para un perro europeo, el país es un destino sin red de apoyo.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "FIEBRE AMARILLA OBLIGATORIA. TravelHealthPro exige certificado a todo viajero desde los 9 meses de edad y el MAEC lo confirma como requisito de entrada. Sin él no se embarca ni se entra.",
        "MALARIA DE ALTO RIESGO EN TODO EL PAÍS y durante todo el año. Quimioprofilaxis recomendada (atovacuona/proguanil, doxiciclina o mefloquina) más protección antimosquito de día y de noche.",
        "VACUNAS RECOMENDADAS: hepatitis A, fiebre tifoidea, tétanos-difteria, hepatitis B, triple vírica y rabia según exposición. El MAEC añade cólera y verificación del estado de polio y sarampión.",
        "OTROS RIESGOS: dengue y zika presentes, esquistosomiasis en agua dulce —nada de bañarse en ríos ni lagos— y rabia en animales domésticos.",
        "NO HAY CONVENIO DE SEGURIDAD SOCIAL con España. Seguro de viaje con cobertura amplia y EVACUACIÓN MÉDICA imprescindible: el MAEC advierte de que no existe servicio de ambulancias en el país.",
        "CENTROS DE REFERENCIA en Malabo, ambos privados y con pago por adelantado: Hospital La Paz, +240 555 666 160, y Clínica Guadalupe, +240 222 573 173. Para el continente, el centro de referencia en Bata está POR CONFIRMAR con el Consulado General de España.",
        "AGUA Y ALIMENTOS: agua embotellada o tratada siempre, y precaución con hielo y crudos. TravelHealthPro insiste en higiene estricta de comida y agua; el FCDO llegó a citar cuestionarios de cribado sobre viajes a países afectados por ébola.",
    ],
    seguridad_intro="Guinea Ecuatorial no es un país en guerra, es un país vigilado. El MAEC recomienda viajar con precaución y describe un deterioro de la seguridad en Malabo y Bata; Freedom House le da 5 puntos sobre 100 y la clasifica como «no libre», con 0 sobre 40 en derechos políticos. El riesgo para el viajero no es el crimen organizado, es el aparato: retenes continuos, detenciones por fotografiar lo que no toca, extorsión en carretera y una justicia sin garantías. A eso se suman robos y atracos nocturnos en las dos ciudades principales.",
    seguridad=[
        "MAEC: «SE RECOMIENDA VIAJAR CON PRECAUCIÓN». La seguridad se ha deteriorado, especialmente en Malabo y Bata.",
        "ZONAS VETADAS: instalaciones militares y dependencias presidenciales, y la isla de Annobón, que el MAEC desaconseja para turismo en este momento. Corisco, solo con autorización oficial.",
        "DETENCIÓN POR FOTOGRAFIAR. El FCDO es explícito: fotografiar edificios de gobierno, instalaciones militares o aeropuertos es ilegal y puede acabar en arresto y detención. Un viajero que recorrió el país en enero de 2024 describió restricciones fotográficas estrictas en las ciudades y verificación de permisos turísticos.",
        "RETENES Y EXTORSIÓN. Los controles policiales y militares son habituales en todas las carreteras; Canadá (9-IX-2026) documenta que en los retenes cercanos a Malabo y Bata los agentes intentan obtener sobornos.",
        "DOCUMENTACIÓN SIEMPRE ENCIMA. Pasaporte con visado vigente en mano: el FCDO avisa de que no llevar documento de identidad puede llevar a detención.",
        "DETENCIONES ARBITRARIAS. El FCDO señala que las disputas comerciales pueden derivar en confinamiento prolongado, sin garantías procesales ni judicatura independiente.",
        "DELINCUENCIA COMÚN: desde hurto y tirones hasta robo con violencia y carjacking, con más incidencia de noche en Malabo y Bata. No conducir de noche ni usar taxis no reservados de antemano.",
        "LGTBI: el MAEC advierte de que las manifestaciones públicas de afecto entre personas del mismo sexo pueden perseguirse como «escándalo público».",
        "COMUNICACIONES CORTABLES. Freedom House documenta restricciones de internet y de telefonía móvil impuestas en Annobón durante 2024, además de detenciones de activistas por críticas en redes: hay que asumir que la conectividad es un privilegio revocable.",
    ],
    agua=[
        "AGUA DE BOCA: solo embotellada o tratada. La red urbana no es potable y TravelHealthPro mantiene la advertencia de higiene estricta de agua y alimentos.",
        "AGUA DE USO GENERAL para llenar depósitos de ducha y lavado: no hay ninguna red de puntos de llenado documentada para overlanders. Lo realista sería depender de hoteles, estaciones de servicio y contactos locales en Malabo y Bata, que son los dos únicos núcleos con suministro fiable.",
        "CLIMA A FAVOR: más de 2.000 mm de lluvia al año en el continente y unos 1.850 mm en Malabo hacen viable la recogida de agua de lluvia, pero eso no sustituye a un filtro serio.",
        "FILTRACIÓN Y CLORACIÓN propias obligatorias si se llena de red o de pozo. Nada de asumir potabilidad fuera de la botella.",
        "SIN DATOS VERIFICADOS en iOverlander, Tracks4Africa ni blogs de autocaravanistas sobre puntos concretos de agua en Guinea Ecuatorial: POR CONFIRMAR.",
    ],
    combustible=[
        "PAÍS PRODUCTOR DE PETRÓLEO: tercer productor de crudo del África subsahariana y con el 89 % de sus exportaciones en hidrocarburos (Casa África), lo que se traduce en carburante barato para la región.",
        "PRECIO 2026: Numbeo daba 625 FCFA por litro de gasolina (horquilla 500-750 FCFA) en la consulta de septiembre de 2026, es decir, en torno a 0,95 € por litro con la paridad fija del CFA. Dato colaborativo, no oficial: confirmar sobre el terreno.",
        "RED: estaciones de servicio concentradas en Malabo, en Bata y en los ejes Bata–Mongomo y Bata–Ebebiyín. Fuera de esos corredores la densidad cae y conviene viajar con autonomía de reserva.",
        "DIÉSEL: disponible en las estaciones principales, pero ni la calidad del gasóleo ni el contenido de azufre están documentados. Para motores europeos modernos, filtro adicional y prudencia.",
        "RACIONAMIENTO: no hay constancia de racionamiento en 2025-2026, pero tampoco fuente que lo descarte. POR CONFIRMAR.",
        "La ficha de GlobalPetrolPrices para Guinea Ecuatorial no se pudo abrir en esta sesión (error 404), así que no hay cifra oficial datada de gasóleo.",
    ],
    experiencias_intro="Apenas hay relatos overland recientes de Guinea Ecuatorial: el visado caro, las fronteras cerradas y la desconfianza hacia los extranjeros han secado el flujo. Lo poco que circula son viajes de mochilero, crónicas de country-collectors y avisos oficiales, casi siempre en avión o en transporte local.",
    experiencias=[
        "Entrar sin volar costó cuatro meses y un enchufe: Torbjørn Pedersen, el danés de Once Upon a Saga que recorre el mundo sin avión, contó en febrero de 2016 que tardó cuatro meses en lograr el visado —rechazado en Yaundé y concedido en el consulado de Duala por 51.000 CFA— y que las fronteras terrestres llevaban tres meses cerradas sin motivo oficial. Solo cruzó desde Gabón acompañado de un francés con «estatus especial» que trabajaba en obra pública del Gobierno.",
        "El e-visa que no funciona: Chris Travel Blog publicó en enero de 2024 un itinerario de diez días por el país y avisa de que el sistema de e-visa no le funcionó y tuvo que tramitarlo en la embajada de Berlín, con todos los documentos traducidos al inglés y una traducción bilingüe rechazada. Recomienda volar con Cronos por puntualidad y evitar la estatal Ceiba, «que tiende a seguir su propio horario».",
        "Permisos turísticos y cámaras guardadas: el mismo relato de enero de 2024 describe restricciones fotográficas estrictas en las ciudades, verificación de permisos turísticos por parte de la policía y la necesidad de contactar con el ministerio de turismo en algunos casos. Alojamientos de referencia: Colinas Hotel en Malabo, Hotel Moka en Moka, Hotel Panafrica en Bata y el Grand Hotel Djibloho en Oyala. Un miembro del grupo cayó por deshidratación y coincidió con un brote vírico en el continente.",
        "El país con mejores carreteras y peor recibimiento: Wikivoyage, consultada en 2026, describe que Guinea Ecuatorial «tiene uno de los mejores sistemas viales de África Central», con acceso asfaltado desde Camerún y Gabón, y a la vez advierte de que la extorsión por las fuerzas de seguridad «no es infrecuente», de que fotografiar propiedad gubernamental está prohibido y de que a algunos extranjeros se les ha denegado la entrada en Kye-Ossi y Ebebiyín sin justificación.",
        "El paso de Campo se cierra más de lo que se abre: la misma guía señala que «el acceso desde Campo puede estar cerrado con frecuencia», y Casa África recuerda que el MAEC pide precaución con Río Campo y Ebebiyín por cierres frecuentes. Coincide con el aviso canadiense de septiembre de 2026 sobre cierres periódicos ligados a zonas fronterizas en disputa pese al acuerdo de 2020.",
        "Retenes que cobran: el aviso oficial de Canadá actualizado el 9 de septiembre de 2026 describe conductores agresivos, alcohol al volante y controles frecuentes cerca de Malabo y Bata donde los agentes «pueden intentar obtener sobornos». Es la descripción más concreta y reciente de lo que se encuentra un extranjero al volante en el país, y explica por sí sola por qué los relatos de viajeros independientes son tan escasos.",
        "Detenido por una foto: el Foreign Office británico, en su revisión del 8 de enero de 2026, resume la experiencia repetida de los visitantes en una frase: fotografiar edificios gubernamentales, militares o aeropuertos es ilegal «y podría ser arrestado y detenido». Añade que los retenes son frecuentes, que las fuerzas de seguridad piden explicaciones sobre por qué se está en la zona y que conviene comprobar que sellan bien el pasaporte al entrar.",
        "El ferry que se para: Revista Equato informó el 15 de mayo de 2026 de que el «San Valentín 3», el buque de la ruta Malabo–Bata operado por SEMAPORT S.L., suspendía el servicio del 22 de mayo al 30 de junio por revisión técnica, sin alternativa anunciada. La guía de Radio Macuto, actualizada en diciembre de 2025, cifra la travesía en 8 a 12 horas y describe los vuelos a Annobón como muy irregulares.",
        "Annobón, apagada: Freedom House documentó en su informe de 2025 que durante 2024 el Gobierno restringió el acceso a internet y a la telefonía móvil en la isla de Annobón y detuvo a manifestantes ecologistas acusándolos de vínculos separatistas, además de registrar la muerte bajo custodia de un preso político en septiembre. Cualquier plan que incluyera la isla parte de esa realidad, y el MAEC la desaconseja expresamente para turismo.",
        "Sin overlanders que contar: no se ha localizado en esta sesión ningún relato de cruce con vehículo propio matriculado en Europa posterior a 2016 en iOverlander, Tracks4Africa, Overland Bound ni en blogs de viaje. El vacío es en sí mismo el dato: en la ruta Camerún–Gabón, los overlanders rodean Guinea Ecuatorial por Kye-Ossi y Bitam en lugar de atravesarla.",
    ],
    pendientes=[
        ("Estado real de las fronteras terrestres en 2027", "Confirmación escrita de la Embajada de España en Malabo o del Consulado General en Bata de que Ebebiyín/Kye-Ossi y Ebebiyín/Meyo-Kye están abiertos a extranjeros no CEMAC, con fecha de la respuesta."),
        ("Admisión temporal de vehículo extranjero", "Norma o instrucción de la Dirección General de Aduanas ecuatoguineana, o respuesta escrita de la embajada, que diga si se admite CPD o qué passavant se emite, con coste y validez."),
        ("Carte Rose CEMAC", "Confirmar si Guinea Ecuatorial la integra efectivamente, dónde se compra (frontera o aseguradora local), coste por vehículo y duración mínima contratable."),
        ("Página oficial del organismo veterinario", "Localizar el portal del Ministerio de Agricultura y Ganadería o del ICA con los requisitos de importación de animales, o respuesta escrita de la embajada que los fije."),
        ("Permiso previo y cuarentena para el perro", "Confirmar con la Embajada de Guinea Ecuatorial en Madrid si se exige permiso de importación y si hay cuarentena, más allá de lo que afirma PetTravel."),
        ("Precio del gasóleo en 2026", "Cifra datada de gasóleo por litro en fuente abierta (GlobalPetrolPrices, prensa local o relato de viajero), ya que solo se ha podido datar la gasolina vía Numbeo."),
        ("Ferry Malabo – Bata", "Horario y tarifa vigentes del «San Valentín 3» y confirmación de si admite vehículos, contactando con SEMAPORT S.L. (222 78 24 88 / 222 08 10 22)."),
        ("Vuelos a Annobón", "Operador, frecuencia real y si requieren autorización previa; confirmar con Ceiba Intercontinental y con el Consulado."),
        ("Hospital de referencia en Bata", "Nombre, dirección y teléfono verificados a través del Consulado General de España en Bata."),
        ("Registro de SIM para extranjeros", "Requisitos de Muni (GETESA) y Orange GQ para dar de alta una SIM con pasaporte, y si es posible sin residencia."),
        ("Itinerancia de Starlink y trato en aduana", "Confirmar si un terminal europeo en plan roaming funciona tras la aprobación provisional de julio de 2026 y cómo lo trata la aduana en el aeropuerto de Malabo."),
        ("Coordenadas exactas de embajada, consulado y hospitales", "Verificar sobre el mapa o por teléfono la ubicación de la Embajada (Carretera del Aeropuerto s/n, Malabo), del Consulado (Paseo Lumu Matindi s/n, Bata) y de los dos centros sanitarios: las coordenadas de esta ficha son aproximadas."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las páginas efectivamente abiertas en esa fecha; cada dato procede de una de ellas y lo que no se ha podido confirmar queda marcado como «por confirmar». En este país el visado, las fronteras y la sanidad cambian sin preaviso, así que todo lo pendiente debe verificarse con la Embajada de España en Malabo o el Consulado General en Bata antes de mover nada. Es una herramienta de planificación, no una autorización de viaje ni un documento con valor legal.",
    emergency="EMERGENCIA CONSULAR ESPAÑOLA 24 h: Malabo +240 222 00 85 89; Bata +240 222 28 56 77. Embajada de España en Malabo: +240 333 09 20 20 y +240 333 09 28 68. Consulado General en Bata: +240 333 08 26 35. POLICÍA: 113 y 114. BOMBEROS Y PROTECCIÓN CIVIL: 112 y 115. AMBULANCIAS: NO EXISTE SERVICIO en el país; ante una urgencia hay que llamar al Hospital La Paz de Malabo (+240 555 666 160) o a la Clínica Guadalupe (+240 222 573 173) y organizar el traslado por medios propios.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

# -*- coding: utf-8 -*-
"""Comoras — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Comoras está FUERA DE LA RUTA PREVISTA por ser insular: tres islas (Gran Comora, Anjouan y Mohéli) entre Mozambique y Madagascar, sin conexión terrestre ni ferry de vehículos con el continente. La app solo tiene un stub: créala entera con el formato del piloto de Túnez. Claves que DECIDEN la ficha y hay que documentar con fuente fechada: el país ha vivido una veintena de golpes o intentos desde la independencia de 1975 y Azali Assoumani gobierna desde 2016 tras haber dado un golpe en 1999; las elecciones de enero de 2024 fueron impugnadas y hubo disturbios; Mayotte, la cuarta isla del archipiélago, votó quedarse con Francia y Comoras la sigue reclamando, lo que condiciona los movimientos marítimos de toda la zona (y el ciclón Chido de diciembre de 2024 dejó a Mayotte arrasada). Para el viajero: el visado se saca a la llegada, el volcán Karthala sigue activo, y los enlaces entre islas son en avioneta o en barco de línea irregular. El país es además uno de los mayores productores de ylang-ylang y vainilla del mundo.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/comoras.json y audit/pdi/comoras.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Moroni · medina y Antigua Mezquita del Viernes (Badjanani)", cat="Cultura", prio="Alta",
        dog="prohibido", time="medio día",
        lat=-11.6575375, lon=43.2890469,  # Google Maps: Mosquée du Vendredi de Moroni
        desc="El casco viejo de Moroni es un laberinto de callejones de piedra de coral volcado sobre el mar, con la vieja mezquita del viernes —la Badjanani— asomada al muelle. La Wikipedia la fecha en 1427, con el minarete añadido en 1921, y compara la medina con una versión reducida del casco antiguo de Lamu. Es el mejor sitio del país para entender la mezcla suajili-árabe-francesa. AVISO: la medina está mal conservada y sin señalizar, y el acceso al interior de la mezquita depende del criterio del imán; se visita vestido de forma discreta.",
        dog_note="Recinto religioso en uso: el perro no entra en la mezquita ni en su patio; en los callejones de la medina, con correa corta y evitando la hora del rezo.",
        visit={
            "why": "Es el núcleo histórico de la capital y la imagen postal de Comoras: mezquita blanca, dhows y muelle en el mismo encuadre.",
            "see": "Callejones de la medina, puertas talladas, la Badjanani con su minarete de 1921 y la fachada marítima del puerto viejo.",
            "access": "Se llega por la carretera de circunvalación hasta el frente marítimo de Moroni; las calles de la medina son intransitables para un 4x4, hay que aparcar en el paseo del puerto o junto al mercado y entrar a pie. No hay entrada ni horario publicados en fuente oficial; MAEC (actualizado 18-05-2026) pide extremar la precaución y avisa de carterismo en mercados. El pin marca la mezquita antigua, en el borde del puerto.",
            "when": "Primera hora de la mañana o última de la tarde; se evitan las horas de rezo del viernes.",
            "skip": "Si se viaja en viernes a mediodía o si el grupo no quiere dejar los vehículos sin vigilancia en el paseo del puerto.",
        },
        links=[
            {"label": "Moroni (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Moroni,_Comoros"},
            {"label": "MAEC · Recomendaciones de viaje Comoras", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Comoras"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ancienne_Mosquee_du_Vendredi_(10886895544).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ancienne_Mosquee_du_Vendredi_(10886895544).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La vieja Mezquita del Viernes de Moroni.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Moroni_City_Comoros.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Moroni_City_Comoros.JPG",
                "credit": "Ikissai · CC BY-SA 4.0",
                "caption": "Moroni desde el mar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Nouvelle_Mosquee_du_Vendredi_(10861894275).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Nouvelle_Mosquee_du_Vendredi_(10861894275).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La nueva Mezquita del Viernes.",
            },
        ],
    ),
    dict(
        n=2, name="Mercado Volo Volo y puerto de Moroni", cat="Ciudad · servicios", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=-11.6916396, lon=43.2559287,  # Google Maps: Marché Volo Volo
        desc="Volo Volo es el mercado grande de Moroni, al norte de la ciudad, y el punto donde se resuelve el avituallamiento de toda la expedición: fruta, pescado, especias, clavo, vainilla y ylang-ylang. A un paso está el puerto, un muelle modesto de 80 metros con 3,5 metros de calado desde el que salen los enlaces con las otras islas y con el continente. AVISO: los pagos son en efectivo y en francos comorenses, y el MAEC señala el carterismo en mercados como el principal riesgo del país.",
        dog_note="Mercado abarrotado, puestos de pescado y carne y perros callejeros: mejor dejarlo en el vehículo a la sombra o con un miembro del grupo.",
        visit={
            "why": "Reabastecimiento real de la expedición y el mejor sitio para comprar vainilla y clavo a precio local.",
            "see": "Puestos de especias y pescado en Volo Volo; el muelle del puerto viejo con los dhows y los barcos de línea entre islas.",
            "access": "Ambos puntos quedan sobre la carretera principal de Moroni; hay explanadas donde caben dos 4x4 cerca del mercado, aunque el tráfico es caótico. Sin horario ni entrada publicados en fuente oficial. Según la FCDO (actualizado 10-12-2025), los ferris entre islas van a menudo sobrecargados, en mal estado y sin chalecos. El pin marca la entrada del mercado Volo Volo.",
            "when": "De 7 a 11 de la mañana, cuando llega el pescado y aún no aprieta el calor.",
            "skip": "Si ya se ha comprado en Mitsamiouli o si se viaja con poco espacio de carga.",
        },
        links=[
            {"label": "Moroni · mercados y puerto (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Moroni,_Comoros"},
            {"label": "FCDO · Comoros safety and security", "url": "https://www.gov.uk/foreign-travel-advice/comoros/safety-and-security"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Volo_Volo_Market_(10912886835).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Volo_Volo_Market_(10912886835).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "El mercado Volo Volo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fish_section_in_Comoros_market.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fish_section_in_Comoros_market.jpg",
                "credit": "Rokaso · CC BY-SA 4.0",
                "caption": "El puesto de pescado del mercado.",
            },
        ],
    ),
    dict(
        n=3, name="Monte Karthala · volcán activo y caldera cimera", cat="Naturaleza", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=-11.7451182, lon=43.3584284,  # Google Maps: Karthala
        desc="El Karthala es el punto más alto del país, 2.361 m, y uno de los volcanes más activos del mundo: lleva más de veinte erupciones desde el siglo XIX, con episodios en 1991, 2005, 2006 y enero de 2007. Su caldera cimera mide 3 por 4 kilómetros, una de las mayores del planeta en relación al edificio volcánico. Se sube a pie desde la vertiente oeste, con guía, cruzando bosque húmedo entre 1.200 y 1.800 m y luego landa. AVISO: la erupción puede producirse en cualquier momento; Canadá y el MAEC piden consultar a las autoridades locales antes de emprender la subida.",
        dog_note="Parque nacional, dos jornadas de marcha sin agua, lava suelta y gases sulfurosos en el borde de la caldera: inviable para el perro.",
        visit={
            "why": "Es la gran caminata del archipiélago y la razón geológica de que existan las Comoras.",
            "see": "El bosque húmedo de altura con aves endémicas, la landa cimera y el enorme anfiteatro de la caldera, humeante.",
            "access": "Pista de tierra desde la circunvalación hacia los pueblos de la ladera oeste (Boboni / Mvouni); los vehículos quedan en el pueblo, donde hay sitio para dos 4x4, y se contrata guía y porteador localmente. La ascensión es de dos días con vivac en la cima. Sin tarifa oficial publicada. Canadá (actualizado 09-09-2026) advierte de que las erupciones pueden ocurrir en cualquier momento. El pin marca la cumbre; el punto navegable es el pueblo de inicio.",
            "when": "Estación seca, de mayo a octubre; salida antes del amanecer para evitar la niebla de tarde.",
            "skip": "Si hay alerta volcánica, si llueve (la landa se vuelve barro) o si no se consigue guía.",
        },
        links=[
            {"label": "Mount Karthala (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Mount_Karthala"},
            {"label": "Karthala National Park (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Karthala_National_Park"},
            {"label": "Canadá · Travel advice Comoros", "url": "https://travel.gc.ca/destinations/comoros"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Karthala_volcano-Comoros.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Karthala_volcano-Comoros.jpg",
                "credit": "alKomor.com · CC BY-SA 2.0",
                "caption": "El Karthala, el volcán activo de Gran Comora.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Hiking_to_Karthala_crater.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Hiking_to_Karthala_crater.jpg",
                "credit": "Rokaso · CC BY-SA 4.0",
                "caption": "Subida al cráter del Karthala.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lava_Flows_of_Mount_Karthala_volcano_in_Grande_Comore.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lava_Flows_of_Mount_Karthala_volcano_in_Grande_Comore.jpg",
                "credit": "David Stanley · CC BY 3.0",
                "caption": "Coladas de lava del Karthala.",
            },
        ],
    ),
    dict(
        n=4, name="Playa de Chomoni y la costa este de Gran Comore", cat="Costa", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=-11.6460615, lon=43.394005,  # Google Maps: Chomoni
        desc="Chomoni es la playa de arena blanca más conocida de la costa este de Gran Comore, con cocoteros detrás y bloques de lava negra clavados en la arena, un contraste que no se ve en ningún otro sitio del Índico. A marea baja quedan pozas entre las rocas volcánicas donde se ve fauna de arrecife. Está a poco más de quince kilómetros de Moroni cruzando la isla. AVISO: no hay socorristas, ni duchas, ni chiringuitos; la corriente en el canal exterior es fuerte y el baño se hace cerca de la orilla.",
        dog_note="Playa pública sin vigilancia: con correa cerca de las barcas de los pescadores y agua dulce a bordo, porque no hay sombra fija ni fuentes.",
        visit={
            "why": "Es el baño más cómodo de la isla grande y la mejor parada a media jornada en la vuelta a Ngazidja.",
            "see": "Arena blanca entre coladas de lava, cocoteros, pozas de marea y barcas de pesca tradicionales.",
            "access": "Asfalto desde Moroni por la transversal y luego la costera del este; los últimos metros hasta la arena son pista y hay explanada de tierra para dos 4x4. Sin entrada ni horario publicados; los visitantes de Tripadvisor describen tres vestuarios, dos árboles con sombra y unas paillotes, alguna con cama para pasar la noche. El pin marca la playa; conviene no dejar nada visible dentro de los vehículos.",
            "when": "De mayo a octubre, a media mañana, con marea baja para las pozas.",
            "skip": "En temporada de ciclones (diciembre–abril) o con mar de fondo.",
        },
        links=[
            {"label": "Chomoni Beach · ficha y coordenadas", "url": "https://aroundus.com/p/174464308-chomoni-beach"},
            {"label": "Chomoni Beach (Tripadvisor)", "url": "https://www.tripadvisor.com/Attraction_Review-g480174-d480354-Reviews-Chomoni_Beach-Grande_Comore.html"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Chomoni_Beach_(10952257536).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Chomoni_Beach_(10952257536).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La playa de Chomoni.",
            },
        ],
    ),
    dict(
        n=5, name="Iconi y el acantilado de Mawéni · la vieja capital del sultanato de Bambao", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=-11.7437186, lon=43.2500031,  # Google Maps: Iconi
        desc="Iconi, a los pies del monte Djabal y a diez minutos al sur de Moroni, fue la capital del sultanato de Bambao y conserva el palacio de Kapviridjohé, restaurado, con la tumba del príncipe Saïd Ibrahim. Sobre el pueblo se alza el acantilado de Mawéni, ligado a la leyenda de Fatima Karibangwé, que según la tradición se arrojó al vacío antes que ser esclavizada por los piratas malgaches. Con 8.817 habitantes en 2012 es la segunda ciudad de la isla. AVISO: no hay centro de visitantes; se necesita alguien del pueblo para que abran el palacio.",
        dog_note="El palacio Kapviridjohé alberga una tumba y hay mezquitas de barrio: se mantiene fuera de los recintos religiosos.",
        visit={
            "why": "Es el punto donde la historia de los sultanatos comorenses y las razias malgaches se vuelve visible sobre el terreno.",
            "see": "El palacio Kapviridjohé y la tumba del príncipe Saïd Ibrahim, la gran mezquita del viernes con el manantial de Bichioni enfrente y el acantilado de Mawéni sobre el mar.",
            "access": "Asfalto desde Moroni por la costera del sur (el taxi colectivo cuesta 250 francos comorenses, unos 0,51 €); el pueblo es de calles estrechas y conviene aparcar en la entrada, donde caben dos 4x4. Sin horario ni tarifa publicados. El pin marca el palacio; al acantilado se sube a pie desde el pueblo.",
            "when": "Media tarde, con luz rasante sobre el acantilado.",
            "skip": "Si no se consigue quien abra el palacio y el interés es solo arquitectónico.",
        },
        links=[
            {"label": "Iconi (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Iconi"},
            {"label": "Iconi · coordenadas", "url": "https://latitude.to/articles-by-country/km/comoros/248370/iconi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Terrain_Annexe_du_Stade_Omnisports_de_Iconi-Malouzini.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Terrain_Annexe_du_Stade_Omnisports_de_Iconi-Malouzini.jpg",
                "credit": "TeamLVF · CC BY-SA 4.0",
                "caption": "Iconi-Malouzini, al sur de Moroni.",
            },
        ],
    ),
    dict(
        n=6, name="Lago Salé (Lac Niamawi) · cráter del norte de Gran Comore", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=-11.37539, lon=43.37321,  # Google Maps: Lago Salé (Lac Niamawi) (sin objeto en Google Maps; coordenada de la fuente)
        desc="Un cráter volcánico junto al extremo norte de la isla, relleno de agua salada, cuyo color pasa del aguamarina al verde azulado profundo a lo largo del día. La tradición local cuenta que el pueblo de Niamawi fue tragado por el volcán tras negar agua a un santón, y el lago ocupa su lugar. Hay un sendero que rodea el cráter y el cono contiguo, con vistas al océano. AVISO: está a una hora larga de coche de Moroni por carretera en mal estado y no hay servicios de ningún tipo en el borde.",
        dog_note="Espacio abierto sin gestión ni taquilla; con correa en el borde del cráter, que cae a plomo, y sin beber del lago (es agua salada).",
        visit={
            "why": "Es el paisaje volcánico más fotogénico de la isla sin tener que subir al Karthala.",
            "see": "El lago salado encajado en el cráter, el reborde de roca volcánica y el océano al fondo desde el sendero de circunvalación.",
            "access": "Asfalto degradado desde Mitsamiouli hacia Bangoi Kouni y un ramal corto de tierra hasta el mirador; hay explanada para dos 4x4. Sin entrada ni horario oficiales. Atlas Obscura calcula una hora de coche desde Moroni «y algo más por el estado de la carretera». El pin marca el mirador del borde del cráter.",
            "when": "Mediodía, cuando el color del agua es más intenso; estación seca.",
            "skip": "Con lluvia fuerte: el ramal de tierra se embarra y el sendero del borde resbala.",
        },
        links=[
            {"label": "Lac Salé / Lac Niamawi (Atlas Obscura)", "url": "https://www.atlasobscura.com/places/lac-sale-lac-niamawi-comoros"},
            {"label": "Mitsamiouli (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Mitsamiouli"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lac_sal%C3%A9_Bangoi-kouni_Comores.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lac_sal%C3%A9_Bangoi-kouni_Comores.jpg",
                "credit": "Comoria de la république · CC BY-SA 4.0",
                "caption": "El Lac Salé, en un cráter del norte.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/LAC_SALE_MISTAMIHOULI_COMORES.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:LAC_SALE_MISTAMIHOULI_COMORES.JPG",
                "credit": "Ikissai · CC BY-SA 4.0",
                "caption": "El lago salado visto desde el borde.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Old_volcanic_crater-Grande_Comore.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Old_volcanic_crater-Grande_Comore.jpg",
                "credit": "Woodlouse · CC BY-SA 2.0",
                "caption": "Cráter volcánico del norte de Gran Comora.",
            },
        ],
    ),
    dict(
        n=7, name="Mitsamiouli y la costa norte · playas y buceo", cat="Costa", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=-11.3899368, lon=43.2945007,  # Google Maps: Mitsamiouli
        desc="Mitsamiouli, 6.100 habitantes en la costa noroeste, es el centro turístico histórico de Gran Comore: aquí estaba el Galawa Beach Hotel y aquí se concentran las playas y los arrecifes que dieron fama al país entre los viajeros de luna de miel europeos. Frente a esta costa se estrelló en noviembre de 1996 el vuelo 961 de Ethiopian Airlines: de 175 pasajeros murieron 125, y fueron pescadores y turistas locales quienes rescataron a los supervivientes. AVISO: la infraestructura hotelera está muy mermada; conviene confirmar alojamiento y centro de buceo antes de llegar.",
        dog_note="Playas abiertas sin normativa publicada; con correa en el pueblo y vigilado en la arena, porque hay perros sueltos y barcas de pesca.",
        visit={
            "why": "Mejor combinación de playa, arrecife y servicios fuera de la capital, y base natural para el Lago Salé.",
            "see": "Playas de arena clara, arrecife somero accesible desde la orilla, el pueblo pesquero y las ruinas del complejo hotelero.",
            "access": "Asfalto por la circunvalación norte desde Moroni (unos 35 km); aparcamiento informal en la playa, espacio suficiente para dos 4x4. Sin entradas ni horarios. MAEC desaconseja pasear solo de noche por playas y centros urbanos. El pin marca el centro del pueblo; el acceso a la arena está al oeste.",
            "when": "Mayo a octubre, con mar en calma; para el buceo, primeras horas del día.",
            "skip": "En temporada de ciclones o si no se ha confirmado alojamiento abierto.",
        },
        links=[
            {"label": "Mitsamiouli (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Mitsamiouli"},
            {"label": "Mitsamiouli · coordenadas", "url": "https://latlong.info/comoros/grande-comore/mitsamiouli"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mitsamiouli_beach_1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mitsamiouli_beach_1.jpg",
                "credit": "Radosław Botev · CC BY-SA 4.0",
                "caption": "La playa de Mitsamiouli.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mitsamiouli_street.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mitsamiouli_street.jpg",
                "credit": "Radosław Botev · Attribution",
                "caption": "Una calle de Mitsamiouli.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Palm_trees_near_Mitsamiouli_beach_1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Palm_trees_near_Mitsamiouli_beach_1.jpg",
                "credit": "Radosław Botev · CC BY-SA 4.0",
                "caption": "Cocoteros junto a la playa.",
            },
        ],
    ),
    dict(
        n=8, name="Bosque de Moya y las destilerías de ylang-ylang (Anjouan)", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="medio día",
        lat=-12.3090253, lon=44.4364706,  # Google Maps: Moya (Anjouan)
        desc="Comoras produce alrededor del 80 % del ylang-ylang del mundo, y el sur de Anjouan es donde se ve el ciclo completo: la flor, el alambique y el aceite. Encima de la costa de Moya sobrevive el bosque de Moya, unas 500 hectáreas de selva relicta dentro del Parque del Mont Ntringui, con lémures y murciélagos endémicos. La playa de Moya, en herradura entre acantilados, es de las mejores del archipiélago. AVISO: las destilerías son artesanales y funcionan por campañas; hay que preguntar en el pueblo si están destilando.",
        dog_note="Bosque relicto dentro del Parque del Mont Ntringui, con lémures y la roussette de Livingstone; las destilerías son instalaciones de trabajo con calderas abiertas.",
        visit={
            "why": "Une el gran producto de exportación del país con el último bosque de baja altitud de Anjouan y una playa excepcional.",
            "see": "Alambiques de cobre humeando entre plantaciones, el bosque de Moya y la bahía cerrada de arena de Moya.",
            "access": "Asfalto degradado y tramos de pista desde Mutsamudu por el interior (unos 40 km, curvas continuas); aparcamiento informal en el pueblo, justo para dos 4x4. Canadá advierte (09-09-2026) de que en Anjouan los servicios de emergencia son «extremadamente limitados». El pin marca el pueblo/playa de Moya; el bosque queda ladera arriba y pide guía local.",
            "when": "Campaña de ylang-ylang y estación seca, de mayo a octubre, por la mañana.",
            "skip": "Si llueve (las pistas del interior de Anjouan se vuelven impracticables) o si no hay guía para el bosque.",
        },
        links=[
            {"label": "Mount Ntringui National Park · bosque de Moya (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Mount_Ntringui_National_Park"},
            {"label": "Comoras · producción de ylang-ylang (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Comoros"},
            {"label": "Moya · coordenadas", "url": "https://latlong.info/comoros/anjouan/moya"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mutsamudu_Hotel_Al_Amal_Beach_(9983243486).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mutsamudu_Hotel_Al_Amal_Beach_(9983243486).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La costa de Anjouan.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Indian_Ocean_Sunset_(9983308503).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Indian_Ocean_Sunset_(9983308503).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "Atardecer en el Índico desde Anjouan.",
            },
        ],
    ),
    dict(
        n=9, name="Mutsamudu (Anjouan) · la ciudadela y la medina", cat="Cultura", prio="Alta",
        dog="no recomendado", time="1 noche",
        lat=-12.166963, lon=44.397016,  # Google Maps: Citadelle de Mutsamudu
        desc="Mutsamudu es la capital de Anjouan y la ciudad histórica mejor conservada del archipiélago: una medina del siglo XV apretada entre dos calles paralelas y, encima, una ciudadela levantada en 1786 con ayuda británica para defender la ciudad de los negreros malgaches. Abajo está el único puerto de aguas profundas del país, construido en 1982, por donde sale el ylang-ylang, el clavo y la vainilla. AVISO: Anjouan ha sido foco de tensión política y los servicios de emergencia son mínimos; conviene moverse de día.",
        dog_note="Callejuelas muy estrechas y concurridas y mezquitas a pie de calle; la ciudadela tiene muros sin proteger y suelo irregular.",
        visit={
            "why": "Es la parada patrimonial de más peso de Comoras y el punto de entrada por mar y aire a Anjouan.",
            "see": "La ciudadela de 1786 sobre la ciudad, la medina del siglo XV, las puertas talladas y el puerto de aguas profundas.",
            "access": "Asfalto desde el aeropuerto de Ouani; la medina no admite vehículos, hay que aparcar en el frente portuario y subir andando a la ciudadela (cuesta corta pero fuerte). Sin horario ni tarifa publicados en fuente oficial. Canadá (09-09-2026) recuerda que en Anjouan la asistencia de emergencia es extremadamente limitada y la FCDO señala que puede haber protestas, sobre todo en época electoral. El pin marca la ciudadela.",
            "when": "Primera hora de la tarde, con el sol dando sobre las murallas.",
            "skip": "Durante disturbios o convocatorias políticas, o si solo se dispone de unas horas en la isla.",
        },
        links=[
            {"label": "Mutsamudu (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Mutsamudu"},
            {"label": "FCDO · Comoros safety and security", "url": "https://www.gov.uk/foreign-travel-advice/comoros/safety-and-security"},
            {"label": "Canadá · Travel advice Comoros", "url": "https://travel.gc.ca/destinations/comoros"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Citadel_of_Mutsamudu_(9983241846).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Citadel_of_Mutsamudu_(9983241846).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La ciudadela de Mutsamudu.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mutsamudu_Stone_Stairway_(9983185465).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mutsamudu_Stone_Stairway_(9983185465).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "Escalinata de piedra de la medina.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mutsamudu_Friday_Mosque_(9983245486).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mutsamudu_Friday_Mosque_(9983245486).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La Mezquita del Viernes de Mutsamudu.",
            },
        ],
    ),
    dict(
        n=10, name="Cascadas de Dziancoundré y el interior de Anjouan (Hombo)", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=-12.1742856, lon=44.4015006,  # Google Maps: Hombo (Mutsamudu)
        desc="SUSTITUYE al «Dziani Boundouni de Anjouan» del guion, que en realidad es el lago de cráter de Mohéli (ficha 16). La excursión real del interior de Anjouan son las cascadas de Dziancoundré, al sur de Mutsamudu, sobre el plateau de Hombo: se sigue la conducción de agua de fundición que va al captación y se entra en un valle encajado con varios saltos, el principal de unos doce metros. AVISO: hay un paso escabroso sobre la tubería y el sendero no está señalizado; conviene ir con alguien del pueblo.",
        dog_note="Sendero de montaña sin gestión ni fauna peligrosa, pero con pasos expuestos junto a la conducción de agua: solo con perro seguro en terreno técnico.",
        visit={
            "why": "Es la estampa del Anjouan verde —la «isla de los perfumes»— sin necesidad de subir al Ntringui.",
            "see": "El valle encajado, la sucesión de saltos y la cascada principal de unos 12 m, con las canteras artesanales de grava en el camino.",
            "access": "Se sale de Mutsamudu hacia el sur por asfalto hasta el plateau de Hombo y se continúa a pie junto a la conducción de agua; sitio para dejar dos 4x4 en el borde de la carretera de Hombo. Sin entrada ni horario. El blog consultado describe «un paso escabroso»; coordenadas del salto POR CONFIRMAR. El pin marca Hombo, cabecera del sendero.",
            "when": "Después de la estación húmeda (abril–junio), cuando hay caudal pero el sendero ya está practicable.",
            "skip": "Con lluvia en curso: la conducción y las rocas se vuelven muy resbaladizas.",
        },
        links=[
            {"label": "Cascades de Dziancoundré (relato de viaje)", "url": "https://cariboumahore.wordpress.com/2014/11/02/voyage-aux-comores-cascades-de-dziancoundre/"},
            {"label": "Anjouan · cascadas de Dziancoundré (guía)", "url": "https://africatourismguide.com/fr/destinations/comoros/places/anjouan"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mutsamudu_port1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mutsamudu_port1.jpg",
                "credit": "Peioma · CC BY-SA 3.0",
                "caption": "El puerto de Mutsamudu.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mutsamudu_2006.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mutsamudu_2006.jpg",
                "credit": "alKomor.com · CC BY-SA 2.0",
                "caption": "Mutsamudu y su ladera.",
            },
        ],
    ),
    dict(
        n=11, name="Monte Ntringui · el techo de Anjouan y el lago Dzialandzé", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=-12.2111111, lon=44.4252778,  # Google Maps: Ntingui
        desc="Con 1.595 metros, el Ntringui es el punto más alto de Anjouan y el núcleo del parque nacional creado en 2010; el conjunto es además sitio Ramsar desde el 12 de noviembre de 2006, con 3.000 hectáreas protegidas. En su flanco sudeste está el lago Dzialandzé, a 910 m, unas tres hectáreas y 280 por 150 metros: la principal reserva de agua de la isla. Aquí vive la roussette de Livingstone, uno de los mayores murciélagos frugívoros del mundo. AVISO: los caminos nacen de la carretera Koni-Djodjo–Dindi y no están señalizados.",
        dog_note="Parque nacional y sitio Ramsar con fauna amenazada (roussette de Livingstone, lémur mangosta): no procede entrar con perro.",
        visit={
            "why": "El último bosque de montaña de Anjouan y el mirador natural sobre todo el archipiélago.",
            "see": "Bosque húmedo de altura, el lago de cráter Dzialandzé y, con buen tiempo, Mohéli y Mayotte desde la cima.",
            "access": "Asfalto irregular hasta la carretera Koni-Djodjo–Dindi y después sendero de un kilómetro al lago; a la cima, varias horas más con guía. Hay dónde dejar dos 4x4 en el arcén del collado. Sin tarifa publicada por la agencia de parques. El pin marca el centroide del sitio Ramsar del Mont Ntringui; el punto navegable es el inicio del sendero en Dindi.",
            "when": "Estación seca (mayo–octubre) y salida temprana: a mediodía la cima suele estar en la nube.",
            "skip": "Sin guía o con previsión de lluvia; la niebla deja la ascensión sin vistas.",
        },
        links=[
            {"label": "Ramsar · Le Mont Ntringui (sitio 1650)", "url": "https://rsis.ramsar.org/ris/1650"},
            {"label": "Mount Ntringui National Park (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Mount_Ntringui_National_Park"},
            {"label": "Lac Dzialandzé (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Lac_Dzialandz%C3%A9"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lac_dzialandze.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lac_dzialandze.JPG",
                "credit": "Peioma · Public domain",
                "caption": "El lago Dzialandzé, en las alturas de Anjouan.",
            },
        ],
    ),
    dict(
        n=12, name="Domoni · la vieja capital sultánica de Anjouan", cat="Cultura", prio="Media",
        dog="prohibido", time="medio día",
        lat=-12.2632051, lon=44.5290018,  # Google Maps: Domoni
        desc="Domoni, en la costa este de Anjouan, fue la capital del sultanato de Nzwani antes de que Abdallah I la trasladara a Mutsamudu. La arqueología sitúa su fundación en el siglo XII y en el XV ya comerciaba con África, Persia, Arabia y la India. Su medina se divide en tres barrios —Hari ya muji, Maweni y Momoni— y el blanco mausoleo de cuatro minaretes guarda a Ahmed Abdallah, primer presidente del país, asesinado por un guardia presidencial en 1989. AVISO: es una ciudad viva y conservadora; conviene ropa cubierta y pedir permiso antes de fotografiar.",
        dog_note="El mausoleo de Ahmed Abdallah es un recinto funerario musulmán y la medina está llena de mezquitas de barrio.",
        visit={
            "why": "Es el relato completo del poder comorense, del sultanato medieval a los golpes de la independencia, en cinco manzanas.",
            "see": "La medina de tres barrios, las puertas talladas, la costa de bloques de lava y el mausoleo blanco de cuatro minaretes.",
            "access": "Asfalto en mal estado desde Mutsamudu por la costa este (unos 30 km de curvas); se aparca en la entrada del pueblo, hay hueco para dos 4x4. Sin horario ni tarifa. El pin marca el mausoleo, en el barrio Hari ya Muzhi.",
            "when": "Mañana, antes del calor; fuera de la oración del viernes.",
            "skip": "Si el tiempo en Anjouan es justo: Mutsamudu concentra más patrimonio por hora invertida.",
        },
        links=[
            {"label": "Domoni (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Domoni"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Domani-Anjouan_1930.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Domani-Anjouan_1930.jpg",
                "credit": "Emile Vienne · Public domain",
                "caption": "Domoni en los años treinta.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Anjouan_-_Islands_of_Comoros.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Anjouan_-_Islands_of_Comoros.jpg",
                "credit": "Haryamouji · CC BY-SA 3.0",
                "caption": "La costa de Anjouan.",
            },
        ],
    ),
    dict(
        n=13, name="Fomboni (Mohéli) · la capital de la isla pequeña", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=-12.2830423, lon=43.7407167,  # Google Maps: Fomboni
        desc="Fomboni, unos 19.000 habitantes, concentra más de un tercio de la población de Mohéli y es la quinta localidad del país: casas de una planta, mercado, embarcadero, correos, bancos y hospital. Da nombre a los Acuerdos de Fomboni de 2001, el pacto que reordenó la constitución comorense tras la crisis separatista. El aeropuerto de Mohéli Bandar Es Eslam queda a unos 3 km, en Djoezi. AVISO: es la última gasolinera y el último cajero antes del sur de la isla; se llena depósito aquí.",
        dog_note="Pueblo abierto, sin recintos cerrados; con correa en el mercado y fuera de la mezquita.",
        visit={
            "why": "Base logística obligada de Mohéli y puerta de entrada a su parque nacional.",
            "see": "El mercado y el embarcadero, la fachada marítima de casas bajas y la vida de la única ciudad de la isla.",
            "access": "Asfalto desde el aeropuerto de Djoezi (3 km); aparcamiento en la calle principal y en el embarcadero, suficiente para dos 4x4. Clima tropical marítimo, unos 2.000 mm anuales, entre 19 y 32 °C, con estación húmeda de noviembre a abril. El pin marca el centro de Fomboni.",
            "when": "Cualquier mañana; la estación seca (mayo–octubre) es la practicable para el resto de la isla.",
            "skip": "Si solo se va a Mohéli por las ballenas y se duerme directamente en Nioumachoua.",
        },
        links=[
            {"label": "Fomboni (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Fomboni"},
            {"label": "Mohéli (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Moh%C3%A9li"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fomboni-Ship.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fomboni-Ship.jpg",
                "credit": "alKomor.com · CC BY-SA 2.0",
                "caption": "El embarcadero de Fomboni.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Moheli_d_(21).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Moheli_d_(21).jpg",
                "credit": "Willerhawk · CC BY-SA 4.0",
                "caption": "Mohéli, la isla pequeña.",
            },
        ],
    ),
    dict(
        n=14, name="Parque Nacional de Mohéli · tortugas y ballenas jorobadas", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=-12.3173217, lon=43.7004741,  # Google Maps: Mwali National Park
        desc="Fue el primer espacio protegido del país: parque marino el 19 de abril de 2001, parque nacional en 2010 y ampliado en 2015 hasta cubrir alrededor de tres cuartas partes de la superficie terrestre de Mohéli, con 643,62 km² en total. Protege tortuga verde y carey, dugongos, ocho especies de delfines, ballenas jorobadas y el celacanto, con una laguna de 10 a 60 metros y ocho islotes de cría de aves marinas. AVISO: Mongabay documentó en 2022 que buena parte de las instalaciones de ecoturismo comunitario no están operativas; hay que confirmar antes de llegar.",
        dog_note="Playas de puesta de tortuga verde y carey bajo vigilancia de ecoguardas: el perro es incompatible con los nidos y las crías.",
        visit={
            "why": "Es lo mejor de Comoras en naturaleza: puesta nocturna de tortugas e, en temporada, ballenas jorobadas con cría.",
            "see": "Playas de nidificación (Itsamia), arrecife de franja, islotes de aves marinas y, de julio a octubre, jorobadas.",
            "access": "Pista desde Fomboni hacia la costa sur; los últimos tramos a Itsamia y Nioumachoua son de tierra y exigen 4x4 en época de lluvias. Alojamiento en bungalows comunitarios de los pueblos y salidas en barca concertadas con las asociaciones. Tasas de parque no publicadas en fuente oficial abierta: POR CONFIRMAR. El pin marca el centroide del parque; los puntos navegables son Nioumachoua e Itsamia.",
            "when": "Ballenas jorobadas de julio a octubre; puesta de tortugas todo el año, con salidas nocturnas guiadas.",
            "skip": "En plena estación húmeda, cuando las pistas del sur se cortan, o si no se ha confirmado bungalow abierto.",
        },
        links=[
            {"label": "Mohéli National Park (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Moh%C3%A9li_National_Park"},
            {"label": "Mongabay · Comoros amplía su red de parques (2022)", "url": "https://news.mongabay.com/2022/05/for-20-years-comoros-had-only-1-national-park-its-now-creating-5-more/"},
            {"label": "Mohéli (Wikivoyage)", "url": "https://en.wikivoyage.org/wiki/Moheli"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ouallah-Moh%C3%A9li-Corail.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ouallah-Moh%C3%A9li-Corail.jpg",
                "credit": "alKomor.com · CC BY-SA 2.0",
                "caption": "Coral del parque de Mohéli.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Moh%C3%A9li-Beach.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Moh%C3%A9li-Beach.jpg",
                "credit": "alKomor.com · CC BY-SA 2.0",
                "caption": "Una playa del parque nacional.",
            },
        ],
    ),
    dict(
        n=15, name="Islotes de Nioumachoua · el archipiélago del sur de Mohéli", cat="Costa", prio="Media",
        dog="prohibido", time="1 noche",
        lat=-12.3675138, lon=43.717019,  # Google Maps: Nioumachoua
        desc="Frente a Nioumachoua —3.400 habitantes, segunda localidad de Mohéli— se alinean ocho islotes cuyos nombres empiezan todos por «shisiwa», isla en comorense. Varios tienen las playas de arena blanca más bonitas del archipiélago y son colonias de aves marinas dentro del parque nacional. Desde el pueblo se contratan salidas en barca para bucear en el arrecife, pescar o pasar la noche en un islote. AVISO: las barcas son pequeñas y sin equipo de seguridad; el canal se pica por la tarde.",
        dog_note="Los islotes son colonias de cría de aves marinas dentro del parque nacional: no se desembarca con perro.",
        visit={
            "why": "La estampa más redonda del país: ocho islotes deshabitados a media hora de barca de la playa.",
            "see": "Playas de arena blanca en los islotes, arrecife coralino, aves marinas y, en temporada, jorobadas de camino.",
            "access": "Pista de tierra desde Fomboni (unos 25 km) hasta el pueblo; se deja el 4x4 en la explanada de la playa y se negocia la barca con la asociación local. Sin tarifa publicada: POR CONFIRMAR. La FCDO avisa de embarcaciones sobrecargadas y sin chalecos en Comoras. El pin marca el embarcadero de Nioumachoua.",
            "when": "Mar en calma, por la mañana, entre mayo y octubre.",
            "skip": "Con viento del sur o si no hay chalecos a bordo.",
        },
        links=[
            {"label": "Nioumachoua (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Nioumachoua"},
            {"label": "Nioumachoua · coordenadas", "url": "https://latlong.info/comoros/moheli/nioumachoua"},
            {"label": "Mohéli (Wikivoyage)", "url": "https://en.wikivoyage.org/wiki/Moheli"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/%C3%8Elot_de_Nioumachoua.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:%C3%8Elot_de_Nioumachoua.jpg",
                "credit": "Fatima771 · CC BY 3.0",
                "caption": "Los islotes de Nioumachoua.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Panorama_mangrove_de_nioumachoua.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Panorama_mangrove_de_nioumachoua.jpg",
                "credit": "Daryl Wallace · CC BY-SA 2.0",
                "caption": "El manglar de Nioumachoua.",
            },
        ],
    ),
    dict(
        n=16, name="Lago Dziani Boundouni · el lago de cráter de Mohéli (Ramsar)", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=-12.3795327, lon=43.8488115,  # Google Maps: Dziani Boundouni
        desc="En el este de Mohéli, un cráter volcánico de unas 30 hectáreas guarda uno de los pocos lagos de agua dulce del archipiélago; es sitio Ramsar desde el 9 de febrero de 1995. Acoge zampullines, garzas, garcetas y limícolas, y se sospecha que mantiene conexiones subterráneas con el océano, señal de actividad volcánica bajo la superficie. Está a unos 15 km al sureste de Fomboni, a 138 metros de altitud. AVISO: no hay mirador acondicionado ni sendero marcado; la orilla es fangosa y hay mosquitos al atardecer.",
        dog_note="Humedal Ramsar sin infraestructura ni vigilancia; con correa por las aves acuáticas que crían en la orilla.",
        visit={
            "why": "Cierra el circuito natural de Mohéli y es el mejor punto de observación de aves acuáticas del país.",
            "see": "El lago de cráter encajado en la selva, con zampullines, garzas y limícolas en la orilla.",
            "access": "Pista desde la carretera del sur de Mohéli; el último tramo es de tierra y exige 4x4 en época de lluvias, con sitio justo para dos vehículos en el arcén. Sin entrada ni horario; la ficha Ramsar 717 devolvió error 502 en la consulta. El pin marca el lago; el acceso real es por el pueblo de Boundouni.",
            "when": "Primera hora de la mañana, en estación seca, para las aves.",
            "skip": "Tras lluvias fuertes, cuando la pista de acceso se corta.",
        },
        links=[
            {"label": "Lac Dziani Boundouni (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Lac_Dziani_Boundouni"},
            {"label": "Mohéli National Park · lago Dziani-Boudouni (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Moh%C3%A9li_National_Park"},
            {"label": "Dziani Boundouni · coordenadas", "url": "https://km.geoview.info/dziani_boundouni,1090834"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ilha_Moh%C3%A9li_no_Arquip%C3%A9lago_de_Comores,_no_Oceano_%C3%8Dndico.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ilha_Moh%C3%A9li_no_Arquip%C3%A9lago_de_Comores,_no_Oceano_%C3%8Dndico.jpg",
                "credit": "INPE / Coordenação-Geral de Observação da Terra · CC BY-SA 2.0",
                "caption": "El interior de Mohéli, donde está el lago de cráter.",
            },
        ],
    ),
    dict(
        n=17, name="Bahía de Chindini y el canal hacia Mohéli", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=-11.9235496, lon=43.4891529,  # Google Maps: Chindini
        desc="Chindini, en el extremo sur de Gran Comore, es el punto desde el que salen las barcas hacia Mohéli: lanchas rápidas de alrededor de una hora, para las que el extranjero necesita un permiso de policía, o cargueros que hacen la travesía de noche. Es un pueblo pequeño —1.107 habitantes en el censo de 1991— con playa y vista al canal. AVISO: la FCDO y Canadá documentan naufragios por sobrecarga y falta de chalecos en estas travesías; no es un trayecto para hacer a la ligera.",
        dog_note="Playa y embarcadero informales; con correa entre las barcas y las redes de los pescadores.",
        visit={
            "why": "Es el enlace marítimo real entre las dos islas y el mirador natural sobre el canal de Mohéli.",
            "see": "La bahía, las lanchas y los cargueros cargando, y la silueta de Mohéli al sur en días claros.",
            "access": "Asfalto en mal estado desde Moroni por la costera del sur (unos 45 km); el pueblo tiene explanada junto al embarcadero, espacio para dos 4x4. Según Wikivoyage, lancha rápida ≈1 h por unos 10.000 KMF más 10.000 KMF de permiso policial para extranjeros, o carguero nocturno al mismo precio sin permiso. El pin marca el pueblo y su embarcadero.",
            "when": "Mañana temprano, que es cuando salen las barcas y el canal está más tranquilo.",
            "skip": "Con mar de fondo, de noche o si la embarcación va sobrecargada.",
        },
        links=[
            {"label": "Chindini (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Chindini"},
            {"label": "Mohéli · cómo llegar (Wikivoyage)", "url": "https://en.wikivoyage.org/wiki/Moheli"},
            {"label": "Chindini · coordenadas", "url": "https://latlong.info/comoros/grande-comore/chindini"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pahoehoe_Lava_at_Chindini_beach_in_Comoros.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pahoehoe_Lava_at_Chindini_beach_in_Comoros.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "Lava pahoehoe en la playa de Chindini.",
            },
        ],
    ),
    dict(
        n=18, name="Mbéni y el norte agrícola de Gran Comore", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=-11.5044906, lon=43.3861683,  # Google Maps: Mbéni
        desc="Mbéni, capital de la prefectura de Hamahamet-Mboinkou en el noreste de Gran Comore, se conoce como «la ciudad de los minaretes»: reúne 26 mezquitas y varias escuelas coránicas a las que acuden alumnos de toda la isla. Fue fundada en el siglo XV por el sultán Inyehele y ronda los 7.893 habitantes (2013). Alrededor se extiende el cinturón agrícola de la isla, con clavo, vainilla y ylang-ylang. AVISO: es una ciudad religiosa y conservadora; vestimenta cubierta y nada de fotografiar mezquitas sin permiso.",
        dog_note="Localidad con 26 mezquitas y escuelas coránicas: el perro suelto está fuera de lugar; con correa y al margen de los recintos.",
        visit={
            "why": "Permite ver el islam comorense fuera de la capital y el paisaje agrícola que sostiene las exportaciones del país.",
            "see": "El bosque de minaretes sobre los tejados, la mezquita central, las escuelas coránicas y las plantaciones de clavo y vainilla.",
            "access": "Circunvalación asfaltada desde Moroni; la Wikipedia francesa cifra el trayecto en 75 km. Aparcamiento en la calle principal, justo para dos 4x4. Sin horarios ni entradas. El pin marca el centro de Mbéni; las coordenadas proceden del infobox de la Wikipedia francesa (11°30'S, 43°23'E) y conviene REVISARLAS en el mapa, porque el punto cae algo tierra adentro respecto al pueblo costero.",
            "when": "Media mañana entre semana; fuera del rezo del viernes.",
            "skip": "Si el tiempo aprieta: aporta menos que Moroni o Iconi y queda fuera del bucle rápido.",
        },
        links=[
            {"label": "Mbéni (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Mb%C3%A9ni"},
            {"label": "Mbéni · coordenadas", "url": "https://latlong.info/comoros/grande-comore/mbeni"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ISS029-E-36311_-_View_of_Comoros.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ISS029-E-36311_-_View_of_Comoros.jpg",
                "credit": "NASA Earth Science and Remote Sensing Unit · Public domain",
                "caption": "Gran Comora desde la Estación Espacial Internacional.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Homme_portant_le_kofia_comorien.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Homme_portant_le_kofia_comorien.jpg",
                "credit": "Benomar01 · CC BY-SA 4.0",
                "caption": "El kofia, el gorro tradicional comorense.",
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
    ("Aeropuerto Internacional Príncipe Said Ibrahim (HAH)", "Frontera", -11.5352529, 43.2716378,  # Google Maps: Aeropuerto Internacional Príncipe Said Ibrahim
     "Único punto de entrada internacional realista. Hahaya, 15 km al norte de Moroni. Pista de asfalto de 2.900 m. Visado a la llegada: 30 € o 15.000 KMF en efectivo, 45 días, una entrada. Ethiopian, Kenya Airways, Air Tanzania, Precision Air, Air Austral, Ewa Air y Turkish (estacional). Pin comprobado en Google Maps («Aeropuerto Internacional Príncipe Said Ibrahim»)."),
    ("Puerto de Moroni", "Frontera", -11.6989, 43.2561,  # Google Maps: Puerto de Moroni (sin objeto en Google Maps; coordenada de la fuente)
     "Puerto de la capital, muelle de unos 80 m. Cabecera del RoPax YAMEELA hacia Mutsamudu desde septiembre de 2025 (45 vehículos), pero SOLO interinsular. No recibe buques del continente con vehículos. Pin comprobado en Google Maps («Puerto de Moroni (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Puerto de Mutsamudu (Anjouan)", "Frontera", -12.1669504, 44.3930894,  # Google Maps: Mutsamudu Port
     "Único puerto de aguas profundas del país, construido en 1982. Tres cuartas partes de su tráfico es transbordo de contenedores hacia las otras islas. Única vía teórica para introducir un vehículo en contenedor. Terminal del RoPax YAMEELA. Pin comprobado en Google Maps («Mutsamudu Port»)."),
    ("Embajada de España en Pretoria (competente para Comoras)", "Consular", -25.7702496, 28.2507774,  # Google Maps: Embajada de España en Pretoria
     "España NO tiene embajada residente en Moroni. La Embajada en Pretoria tiene acreditadas Comoras, Lesoto, Madagascar y Mauricio. Lord Charles Complex, 337 Brooklyn Road, Brooklyn, Pretoria 0181. Tel. +27 12 460 01 23. Emergencia consular: +27 761 146 152. Pin comprobado en Google Maps («Embajada de España en Pretoria»)."),
    ("Viceconsulado de España en Moroni", "Consular", -11.7061223, 43.2517012,  # Google Maps: Moroni
     "El MAEC publica un teléfono de viceconsulado en Moroni: +269 3688964. Dirección, horario y actividad real POR CONFIRMAR. Pin comprobado en Google Maps («Moroni»)."),
    ("Centre Hospitalier National El-Maarouf, Moroni", "Hospital", -11.6951357, 43.2542664,  # Google Maps: Hôpital El-Maarouf
     "Hospital nacional de referencia, abierto en 1954 y en obras de modernización desde 2017 (proyecto de unos 55 millones de euros). Sin estándares occidentales; huelga indefinida de contratados desde el 9-3-2026 con servicios mínimos. Cualquier urgencia seria exige evacuación a Reunión, Nairobi o Sudáfrica. Pin comprobado en Google Maps («Hôpital El-Maarouf»)."),
    ("Estaciones de servicio del eje Moroni-Hahaya", "Combustible", -11.6986, 43.2567,  # Google Maps: Estaciones de servicio del eje Moroni-Hahaya (sin objeto en Google Maps; coordenada de la fuente)
     "Red concentrada en Moroni y el eje hacia Hahaya y Chindini. Tarifas de la subida de mayo de 2026, hoy suspendida: gasolina 1.000 KMF/l y gasóleo 950 KMF/l, desde 750 y 650 KMF/l. Racionamiento de 3.000 l diarios por estación en junio de 2026. Pin comprobado en Google Maps («Estaciones de servicio del eje Moroni-Hahaya (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Suministro de agua en Moroni", "Agua potable", -11.7061223, 43.2517012,  # Google Maps: Moroni
     "El agua de red NO es potable y el bombeo depende de la electricidad, cortada por la escasez de gasóleo en 2026: hacen falta doce horas seguidas de corriente para llenar los depósitos. Comprar embotellada. Cólera activo desde febrero de 2024. Pin comprobado en Google Maps («Moroni»)."),
]

DRONE_CALLOUT = ("danger", "DRONES: VACÍO LEGAL, RIESGO REAL DE REQUISA",
                 "Comoras NO tiene normativa publicada sobre drones. La autoridad es la Agence Nationale de l'Aviation Civile et de la Météorologie (ANACM), cuyo repertorio de reglamentos aeronáuticos no incluye ninguna norma de aeronaves no tripuladas. Los repertorios especializados clasifican el vuelo de visitantes extranjeros como NO PERMITIDO. En un país con inestabilidad crónica, contencioso territorial abierto con Francia por Mayotte y patrullas navales en el canal, el vacío legal no protege: deja la decisión al funcionario de aduanas. Lo previsible es requisa en Hahaya, sin recibo ni devolución. No llevar dron.")

STARLINK_CALLOUT = ("warn", "STARLINK: TODAVÍA NO ACTIVO EN COMORAS",
                    "A fecha de junio de 2026, Comoras NO tiene servicio Starlink operativo. Figura entre los países africanos marcados como «previsto en 2026», pero sin fecha firme: el despliegue depende de la licencia del regulador comorense y de la infraestructura de pasarela terrestre en la región, no solo de la cobertura satelital. El mapa oficial de starlink.com no devolvió el estado del país al consultarlo. Hasta que se confirme, la conectividad depende de la red móvil local, limitada, y del wifi de hoteles y restaurantes de Moroni.")

DOG_MATRIX = [
    ("Entrada al país (aeropuerto de Hahaya)", "permitido con condiciones", "Microchip, pasaporte, antirrábica en vigor y certificado sanitario internacional de menos de 72 horas. Requisito no confirmado en fuente oficial: pedir confirmación escrita a la aduana comorense antes de volar."),
    ("Llegada con el vehículo propio", "prohibido", "No existe ferry de vehículos desde el continente: el perro tendría que volar en bodega con Ethiopian o Kenya Airways, sujeto a sus embargos por calor y a sus propias normas. Verificar con la aerolínea."),
    ("RoPax interinsular Moroni-Mutsamudu (YAMEELA)", "por confirmar", "El buque admite 45 vehículos desde septiembre de 2025, pero no hay política publicada sobre animales a bordo. Preguntar a Serdal International antes de contar con ello."),
    ("Vuelos interinsulares en avioneta", "no recomendado", "Aparatos pequeños, cancelaciones constantes y sin protocolo de animales. Si el perro viaja, quedarse en Gran Comora."),
    ("Espacios públicos y alojamientos", "no recomendado", "País musulmán al 99,6 %: el perro es socialmente rechazado y la oferta se reduce a Airbnb. Confirmar por escrito con cada anfitrión antes de reservar."),
    ("Regreso a la UE desde Comoras", "permitido con condiciones", "Titulación antirrábica ANOTADA EN EL PASAPORTE antes de salir de España y certificado zoosanitario expedido como máximo 10 días antes de entrar en la UE. Sin titulación previa: bloqueo de tres meses."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Comoras (Ministerio de Asuntos Exteriores, España; actualizado 18-5-2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Comoras"),
    ("Embajada de España en Pretoria · Página institucional, con países acreditados (MAEC; consultada 19-9-2026)", "https://www.exteriores.gob.es/Embajadas/pretoria/es/Embajada/Paginas/index.aspx"),
    ("Contact Details of Spanish Embassy in Pretoria, South Africa (South Africa Portal; consultada 19-9-2026)", "https://southafricaportal.com/embassy-of-spain/"),
    ("Comoros (Wikipedia en inglés; consultada 19-9-2026)", "https://en.wikipedia.org/wiki/Comoros"),
    ("Moroni, Comoros (Wikipedia en inglés; consultada 19-9-2026)", "https://en.wikipedia.org/wiki/Moroni,_Comoros"),
    ("Mutsamudu (Wikipedia en inglés; consultada 19-9-2026)", "https://en.wikipedia.org/wiki/Mutsamudu"),
    ("Prince Said Ibrahim International Airport (Wikipedia en inglés; consultada 19-9-2026)", "https://en.wikipedia.org/wiki/Prince_Said_Ibrahim_International_Airport"),
    ("Mayotte (Wikipedia en inglés; consultada 19-9-2026)", "https://en.wikipedia.org/wiki/Mayotte"),
    ("Cyclone Chido (Wikipedia en inglés; consultada 19-9-2026)", "https://en.wikipedia.org/wiki/Cyclone_Chido"),
    ("2025 in the Comoros (Wikipedia en inglés; consultada 19-9-2026)", "https://en.wikipedia.org/wiki/2025_in_the_Comoros"),
    ("2026 in the Comoros (Wikipedia en inglés; consultada 19-9-2026)", "https://en.wikipedia.org/wiki/2026_in_the_Comoros"),
    ("Centre hospitalier national El-Maarouf (Wikipedia en francés; consultada 19-9-2026)", "https://fr.wikipedia.org/wiki/Centre_hospitalier_national_El-Maarouf"),
    ("FCDO · Foreign travel advice: Comoros (Gobierno del Reino Unido; vigente a 12-9-2026, última actualización 10-12-2025)", "https://www.gov.uk/foreign-travel-advice/comoros"),
    ("FCDO · Comoros: Entry requirements (Gobierno del Reino Unido; consultada 19-9-2026)", "https://www.gov.uk/foreign-travel-advice/comoros/entry-requirements"),
    ("Travel advice and advisories for Comoros (Gobierno de Canadá; actualizado 9-9-2026)", "https://travel.gc.ca/destinations/comoros"),
    ("NaTHNaC / TravelHealthPro · Comoros (Reino Unido; información vigente a marzo de 2026)", "https://travelhealthpro.org.uk/country/54/comoros"),
    ("Freedom in the World 2026 · Comoros: 41/100, parcialmente libre (Freedom House, 2026)", "https://freedomhouse.org/country/comoros/freedom-world/2026"),
    ("Carnet de Passages en Douane · Comoros (carnetdepassage.org, AIT/FIA; consultada 19-9-2026)", "https://www.carnetdepassage.org/country/comoros"),
    ("Code des douanes de l'Union des Comores, versión 2024 · admisión temporal, arts. 239-245 (justice.gouv.km, PDF)", "https://justice.gouv.km/wp-content/uploads/2025/03/code_des_douanes_union_des_comores_2024.pdf"),
    ("Direction Générale des Douanes de l'Union des Comores · portal oficial (consultada 19-9-2026)", "https://www.douane.gov.km/"),
    ("Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026 · listas de terceros países (EUR-Lex)", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600636"),
    ("Reglamento Delegado (UE) 2026/131 de la Comisión, de 20 de enero de 2026 · arts. 13, 14, 18 y 19 y anexo XXI (EUR-Lex, PDF)", "https://eur-lex.europa.eu/legal-content/ES/TXT/PDF/?uri=OJ%3AL_202600131"),
    ("Anivetvoyage · Comores: condiciones de entrada de perros y gatos (ficha actualizada 7-1-2023)", "https://anivetvoyage.com/pays/comores/"),
    ("Anivetvoyage · Afrique: índice de países y requisitos (consultada 19-9-2026)", "https://anivetvoyage.com/continents/afrique/"),
    ("ANACM · Règlements aéronautiques comoriens (Agence Nationale de l'Aviation Civile et de la Météorologie; consultada 19-9-2026)", "https://anacm-comores.com/reglementation.php"),
    ("Drone Laws in the Comoros (drone-laws.com; consultada 19-9-2026)", "https://drone-laws.com/drone-laws-in-the-comoros/"),
    ("Starlink · mapa de disponibilidad (starlink.com; consultado 19-9-2026, sin estado devuelto para Comoras)", "https://www.starlink.com/map"),
    ("Starlink in Africa: countries, prices and speeds (tech.africa; actualizado 16-6-2026)", "https://tech.africa/starlink-africa/"),
    ("Serdal International launches new ferry service in The Comoros · RoPax YAMEELA (Shippax, 11-9-2025)", "https://www.shippax.com/en/news/serdal-international-launches-new-ferry-service-in-the-comoros.aspx"),
    ("Prix du carburant: une forte hausse de 35 % à la pompe (La Gazette des Comores, 10-5-2026)", "https://www.lagazettedescomores.com/soci%C3%A9t%C3%A9/prix-du-carburant-une-forte-hausse-de-35-%C3%A0-la-pompe-.html"),
    ("Les Comores suspendent la hausse des prix du carburant après des affrontements mortels (Boursorama / AFP, 16-5-2026)", "https://www.boursorama.com/actualite-economique/actualites/les-comores-suspendent-la-hausse-des-prix-du-carburant-apres-des-affrontements-mortels-0bcdd2dd1c678a83938b77cd497e99db"),
    ("Aux Comores, une pénurie de carburant paralyse l'économie, coupe l'eau et force le gouvernement à reculer sur les prix (La Voix de France, 2026)", "https://www.lavoixdefrance.fr/actualites/aux-comores-une-penurie-de-carburant-paralyse-leconomie-coupe-leau-et-force-le-gouvernement-a-reculer-sur-les-prix-8748/"),
    ("Comores: des contractuels de l'hôpital El-Maarouf entament une grève illimitée (Anadolu Agency, 9-3-2026)", "https://www.aa.com.tr/fr/afrique/comores-des-contractuels-de-l-h%C3%B4pital-el-maarouf-entament-une-gr%C3%A8ve-illimit%C3%A9e-pour-r%C3%A9clamer-une-hausse-des-salaires/3855763"),
    ("Comoros Islands Travel Guide — Everything You Need To Know (Unusual Traveler; actualización de noviembre de 2019)", "https://www.unusualtraveler.com/comoros-everything/"),
    ("Everything I Wish I Had Known Before Traveling to the Comoros Islands (Heart My Backpack; visita 2017, actualizado abril de 2022)", "https://www.heartmybackpack.com/comoros/travel-guide-2/"),
    ("Comoros Driving Guide (International Drivers Association; consultada 19-9-2026 — fuente comercial, usada solo para lado de conducción y estado de la red)", "https://internationaldriversassociation.com/comoros-driving-guide/"),
    ("Comoros Travel Guide 2026 (We Will Nomad; consultada 19-9-2026 — descartada por dar información de visado incorrecta)", "https://www.wewillnomad.com/destination/comoros"),
    ("FCDO · Comoros safety and security", "https://www.gov.uk/foreign-travel-advice/comoros/safety-and-security"),
    ("Mount Karthala (Wikipedia EN)", "https://en.wikipedia.org/wiki/Mount_Karthala"),
    ("Karthala National Park (Wikipedia EN)", "https://en.wikipedia.org/wiki/Karthala_National_Park"),
    ("Chomoni Beach · ficha y coordenadas", "https://aroundus.com/p/174464308-chomoni-beach"),
    ("Chomoni Beach (Tripadvisor)", "https://www.tripadvisor.com/Attraction_Review-g480174-d480354-Reviews-Chomoni_Beach-Grande_Comore.html"),
    ("Iconi (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Iconi"),
    ("Iconi · coordenadas", "https://latitude.to/articles-by-country/km/comoros/248370/iconi"),
    ("Lac Salé / Lac Niamawi (Atlas Obscura)", "https://www.atlasobscura.com/places/lac-sale-lac-niamawi-comoros"),
    ("Mitsamiouli (Wikipedia EN)", "https://en.wikipedia.org/wiki/Mitsamiouli"),
    ("Mitsamiouli · coordenadas", "https://latlong.info/comoros/grande-comore/mitsamiouli"),
    ("Mount Ntringui National Park · bosque de Moya (Wikipedia EN)", "https://en.wikipedia.org/wiki/Mount_Ntringui_National_Park"),
    ("Moya · coordenadas", "https://latlong.info/comoros/anjouan/moya"),
    ("Cascades de Dziancoundré (relato de viaje)", "https://cariboumahore.wordpress.com/2014/11/02/voyage-aux-comores-cascades-de-dziancoundre/"),
    ("Anjouan · cascadas de Dziancoundré (guía)", "https://africatourismguide.com/fr/destinations/comoros/places/anjouan"),
    ("Ramsar · Le Mont Ntringui (sitio 1650)", "https://rsis.ramsar.org/ris/1650"),
    ("Lac Dzialandzé (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Lac_Dzialandz%C3%A9"),
    ("Domoni (Wikipedia EN)", "https://en.wikipedia.org/wiki/Domoni"),
    ("Fomboni (Wikipedia EN)", "https://en.wikipedia.org/wiki/Fomboni"),
    ("Mohéli (Wikipedia EN)", "https://en.wikipedia.org/wiki/Moh%C3%A9li"),
    ("Mohéli National Park (Wikipedia EN)", "https://en.wikipedia.org/wiki/Moh%C3%A9li_National_Park"),
    ("Mongabay · Comoros amplía su red de parques (2022)", "https://news.mongabay.com/2022/05/for-20-years-comoros-had-only-1-national-park-its-now-creating-5-more/"),
    ("Mohéli (Wikivoyage)", "https://en.wikivoyage.org/wiki/Moheli"),
    ("Nioumachoua (Wikipedia EN)", "https://en.wikipedia.org/wiki/Nioumachoua"),
    ("Nioumachoua · coordenadas", "https://latlong.info/comoros/moheli/nioumachoua"),
    ("Lac Dziani Boundouni (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Lac_Dziani_Boundouni"),
    ("Dziani Boundouni · coordenadas", "https://km.geoview.info/dziani_boundouni,1090834"),
    ("Chindini (Wikipedia EN)", "https://en.wikipedia.org/wiki/Chindini"),
    ("Chindini · coordenadas", "https://latlong.info/comoros/grande-comore/chindini"),
    ("Mbéni (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Mb%C3%A9ni"),
    ("Mbéni · coordenadas", "https://latlong.info/comoros/grande-comore/mbeni"),
]

# Bucle de las tres islas: Ngazidja (circunvalación) + Mwali + Ndzuwani, con saltos en avioneta o barco
CORRIDOR = [
    (-11.69164, 43.25593),
    (-11.74372, 43.25),
    (-11.74512, 43.35843),
    (-11.92355, 43.48915),
    (-11.64606, 43.394),
    (-11.50449, 43.38617),
    (-11.37539, 43.37321),
    (-11.38994, 43.2945),
    (-12.28304, 43.74072),
    (-12.36751, 43.71702),
    (-12.37953, 43.84881),
    (-12.16696, 44.39702),
    (-12.17429, 44.4015),
    (-12.26321, 44.529),
    (-12.30903, 44.43647),
    (-11.69164, 43.25593),
]

# Solo Gran Comore: vuelta completa a Ngazidja por la circunvalación (RN1)
CORRIDOR_ALT = [
    (-11.69164, 43.25593),
    (-11.74372, 43.25),
    (-11.92355, 43.48915),
    (-11.64606, 43.394),
    (-11.50449, 43.38617),
    (-11.38994, 43.2945),
    (-11.69164, 43.25593),
]

HISTORIA_RESUMEN = "Comoras es un archipiélago del canal de Mozambique formado por tres islas —Gran Comora, Anjouan y Mohéli— que suman 1.862 kilómetros cuadrados y algo más de un millón de habitantes, según la ficha país del Ministerio de Asuntos Exteriores español actualizada en enero de 2026. Nació como Estado el 6 de julio de 1975 y desde entonces ha vivido más de veinte golpes o intentos de golpe, una cifra que explica buena parte de su historia contemporánea. Azali Assoumani, que llegó al poder mediante un golpe militar en 1999, gobierna de forma continuada desde 2016. La cuarta isla del archipiélago, Mayotte, sigue siendo francesa y Moroni nunca ha dejado de reclamarla. El país es, además, el primer productor mundial de ylang-ylang."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>Las Comoras se poblaron por oleadas sucesivas. Britannica sitúa la llegada de grupos de posible ascendencia malayo-polinesia entre los siglos V y VI, a los que se sumaron poblaciones procedentes de África oriental, de Madagascar y del mundo árabe. La Wikipedia en español fecha el primer desarrollo histórico documentado en la influencia suajili y en la fase de Dembeni, entre los siglos IX y X, cuando el archipiélago quedó engarzado en las rutas comerciales del océano Índico.</p><p>Entre los siglos XI y XV, comerciantes llegados de Oriente Medio y de Madagascar ampliaron su presencia y el islam se convirtió en el cemento social de las islas. De aquel periodo arranca la tradición de los <em>sultanatos</em>: ciudades-Estado con sus medinas, mezquitas y linajes rivales. La UNESCO inscribió en 2026 «Las medinas de los sultanatos históricos de las Comoras», un bien en serie de seis ciudades históricas cuyos núcleos urbanos surgieron, como mínimo, en el siglo XI y que se transformaron en ciudades-Estado durante los siglos XIV y XV. Aquella organización social —costumbres matrilineales, clases de edad, autoridad religiosa— sigue activa hoy, según la propia UNESCO.</p>"),
    ("Colonización",
     "<p>Los primeros europeos en frecuentar el archipiélago fueron portugueses: la Wikipedia en español fecha sus visitas desde 1505 y Britannica sitúa las primeras expediciones en el siglo XVI. Ninguno se quedó. Quien se quedó fue Francia. Según Britannica, París tomó posesión de Mayotte en 1843 —la Wikipedia en español adelanta la ocupación a 1841— y extendió su protectorado sobre las otras tres islas en 1886. En 1912 el conjunto quedó incorporado administrativamente a Madagascar, gobernado desde otra colonia.</p><p>La colonización dejó tres herencias que todavía pesan. La primera, una economía de plantación orientada a la exportación de productos aromáticos, que sigue siendo el grueso de las ventas exteriores. La segunda, el francés como lengua administrativa, hoy oficial junto al árabe y el comorano, según la ficha país del Ministerio de Asuntos Exteriores español actualizada en enero de 2026. La tercera, y la más explosiva, la separación de <strong>Mayotte</strong>: en 1946 las islas obtuvieron el estatuto de territorio de ultramar y, cuando llegó la hora de la independencia, la cuarta isla tomó un camino distinto al de las otras tres. Esa fractura, más que ninguna otra cosa, condiciona hoy los movimientos marítimos de toda la zona.</p>"),
    ("Independencia y construcción del Estado",
     "<p>El 6 de julio de 1975 el Parlamento comorano declaró la independencia del conjunto del archipiélago, con Ahmed Abdallah al frente. Mayotte no siguió: en el referéndum de 1974 el 63,8 % de sus votantes se pronunció contra la independencia y en 1976 el respaldo a Francia llegó al 99,4 %, según la Wikipedia en inglés. Naciones Unidas reconoció la integridad territorial comorana, pero Francia conservó la isla y en 1976 vetó en solitario una resolución del Consejo de Seguridad favorable a Moroni.</p><p>Lo que vino después fue un carrusel. Ali Soilih derrocó a Abdallah semanas más tarde e intentó levantar una república laica y socialista; fue capturado el 13 de mayo de 1978 y ejecutado poco más tarde. El mercenario francés Bob Denard repuso a Abdallah y se convirtió, en palabras de la Wikipedia en español, en el «virrey de las Comoras» durante una década. Abdallah fue asesinado en noviembre de 1989. En 1997 Anjouan y Mohéli proclamaron su secesión y el Estado tardó años en recuperar el control. En febrero de 1999 el coronel <strong>Azali Assoumani</strong> tomó el poder en un golpe de Estado. El país, que se llamaba Estado de las Comoras, fue República Federal Islámica desde 1978 hasta finales de 2001.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>La crisis secesionista se cerró con una constitución aprobada en diciembre de 2001 que instauró una presidencia rotatoria entre las tres islas; el 23 de ese mes el país adoptó el nombre de Unión de las Comoras, según la ficha del ministerio español. Assoumani regresó por la vía electoral y ganó las presidenciales de 2016 con el 41,43 % frente al 39,67 % de su rival. El 30 de julio de 2018, otro referéndum boicoteado por la oposición reforzó los poderes del presidente, suprimió la vicepresidencia y el Tribunal Constitucional y permitió dos mandatos consecutivos.</p><p>Reelegido en 2019, Assoumani volvió a serlo el <strong>14 de enero de 2024</strong> con el 57,02 % de los votos. Los cinco candidatos de la oposición rechazaron el resultado; entre el 17 y el 18 de enero hubo disturbios en la capital, con al menos un muerto, veinticinco heridos y toque de queda, y el Tribunal Supremo validó los comicios el 24 de enero. Mayotte siguió su rumbo: el 29 de marzo de 2009 un 95,5 % de sus votantes aprobó convertirse en departamento francés, consumado el 31 de marzo de 2011. El 15 de diciembre de 2024 el ciclón <em>Chido</em> la arrasó —racha máxima de 226 km/h en el aeropuerto de Pamandzi, 40 muertos y hasta 100.000 desplazados—; en Comoras no hubo víctimas mortales, pero sí 64.150 afectados.</p>"),
    ("Política y gobierno en 2026",
     "<p>Comoras es, según la ficha país del Ministerio de Asuntos Exteriores español actualizada en enero de 2026, una «república presidencialista federal multipartidista» con un parlamento unicameral de 33 diputados y mandatos de cinco años. El jefe del Estado y del Gobierno es Azali Assoumani, que llegó al poder por un golpe en 1999 y que, según esa ficha, fue elegido o reelegido en 2002, 2016, 2019 y 2024. En las legislativas del 12 de enero de 2025, con baja participación y boicot de parte de la oposición, su partido arrasó; el ministerio habla de «máxima polarización política» y de «rumores de una sucesión dinástica» en torno al hijo del presidente.</p><p>Freedom House lo clasificó en 2025 como <strong>«Partly Free»</strong>, parcialmente libre, con 42 puntos sobre 100: 16 sobre 40 en derechos políticos y 26 sobre 60 en libertades civiles. Sostiene que desde 2019 Assoumani «ha consolidado el poder reprimiendo a la oposición y limitando la libertad de prensa». Ni dictadura cerrada ni democracia plena. Reporteros Sin Fronteras lo sitúa en el puesto 72 de 180 en su índice de 2026. En mayo de 2026 una subida del gasóleo del 46 % desató protestas con dos muertos y 39 detenidos, según el CIVICUS Monitor. Con España «apenas existen relaciones bilaterales», resume el ministerio; la Unión Europea es «el principal socio económico», con 22 millones de euros para 2025-2027.</p>"),
    ("Economía y recursos",
     "<p>Comoras es un país pequeño y pobre. Según la ficha del Ministerio de Asuntos Exteriores español (enero de 2026), el PIB rondaba los 1.440 millones de dólares en 2024, con una renta por habitante de unos 1.620 dólares, un crecimiento del 3,3 % y una inflación del 5 %. La moneda es el franco comorano. La agricultura, la silvicultura y la pesca aportan el 36,6 % del producto y los servicios el 50,1 %. El desequilibrio comercial es extremo: 13 millones de dólares exportados frente a 274 millones importados.</p><p>Lo que sale del archipiélago son aromas. Comoras es el <strong>primer productor mundial de ylang-ylang</strong> —en torno al 80 % de la oferta global, según la Wikipedia en inglés— y exporta también vainilla y clavo. Sus principales clientes son India, con el 37,3 %, y Francia, con el 19,7 %. El motor está fuera: el Banco Mundial describe una economía impulsada por las remesas y el consumo interno, y la Wikipedia en francés cifra en un 25 % del PIB los envíos de la diáspora. El mismo Banco Mundial estimaba un 3,8 % de crecimiento en 2025 y un 18 % de pobreza con el umbral de 4,20 dólares diarios. El suelo es volcánico y el Karthala, de 2.361 metros, sigue activo, con erupciones en 2005, 2006 y 2007.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>La ficha del ministerio español cifra la población en 1,03 millones de habitantes en 2024 y la esperanza de vida en 67 años. Los idiomas oficiales son el árabe, el francés y el comorano, lengua emparentada con el suajili, con un dialecto por isla: shingazidja, shindzuani y shimwali. Por carretera uno se entiende en comorano y, con frecuencia, en francés. El 98 % de la población es musulmana, fundamentalmente suní, según el ministerio, que describe el país como «comoranos 97 %; makua 2 %», con minorías suajili, malgache y árabe.</p><p>La música más característica es el <em>twarab</em>, importado de Zanzíbar. La cocina gira en torno al madaba y el samusa, y la gran boda, el <em>anda</em>, es la institución social de Gran Comora. Su único bien del Patrimonio Mundial son las medinas de los sultanatos históricos, inscritas en 2026. El visado se saca a la llegada, entre 30 y 50 euros, y los ferris entre islas están «mal regulados», según el Departamento de Estado estadounidense. Conviene la ropa discreta, con hombros y rodillas cubiertos, y pedir permiso antes de fotografiar a alguien. Durante el ramadán, que en 2027 empieza en torno al 8 de febrero, no se come ni se bebe en público de día. El alcohol es marginal en un país casi enteramente musulmán: fuera de algún hotel, no se busca.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha país Unión de Comoras (Ministerio de Asuntos Exteriores, España · PDF · enero de 2026)", "https://www.exteriores.gob.es/documents/fichaspais/uniondecomoras_ficha%20pais.pdf"),
    ("Comoros: Freedom in the World 2025 (Freedom House · ficha de país · 2025)", "https://freedomhouse.org/country/comoros/freedom-world/2025"),
    ("Comoros — History (Encyclopaedia Britannica · sección de historia · consultada en septiembre de 2026)", "https://www.britannica.com/place/Comoros/History"),
    ("Comoros (Encyclopaedia Britannica · página principal del país · consultada en septiembre de 2026)", "https://www.britannica.com/place/Comoros"),
    ("Comoras (Wikipedia en español · artículo de país · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Comoras"),
    ("Comoros (Wikipedia en inglés · artículo de país · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Comoros"),
    ("Union des Comores (Wikipedia en francés · artículo de país · consultado en septiembre de 2026)", "https://fr.wikipedia.org/wiki/Union_des_Comores"),
    ("2024 Comorian presidential election (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2024_Comorian_presidential_election"),
    ("Politics of the Comoros (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Politics_of_the_Comoros"),
    ("Mayotte (Wikipedia en inglés · referéndums y estatuto · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Mayotte"),
    ("Cyclone Chido (Wikipedia en inglés · balance del ciclón de diciembre de 2024)", "https://en.wikipedia.org/wiki/Cyclone_Chido"),
    ("Mount Karthala (Wikipedia en inglés · erupciones del volcán · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Mount_Karthala"),
    ("2026 in the Comoros (Wikipedia en inglés · cronología del año · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2026_in_the_Comoros"),
    ("Comoros — States Parties (UNESCO, Centro del Patrimonio Mundial · consultado en septiembre de 2026)", "https://whc.unesco.org/en/statesparties/km"),
    ("The Medinas of the Historic Sultanates of the Comoros (UNESCO · bien inscrito en 2026)", "https://whc.unesco.org/en/list/1768"),
    ("Comoros (Reporteros Sin Fronteras · Clasificación Mundial de la Libertad de Prensa 2026)", "https://rsf.org/en/country/comoros"),
    ("Comoros Overview (Banco Mundial · actualizado el 29 de junio de 2026)", "https://www.worldbank.org/en/country/comoros/overview"),
    ("Fuel price increases trigger strikes and deadly protests (CIVICUS Monitor · protestas de mayo de 2026)", "https://monitor.civicus.org/explore/fuel-price-increases-trigger-strikes-and-deadly-protests/"),
    ("Comoros Travel Advisory (Departamento de Estado de EE. UU. · nivel 2 · 12 de enero de 2026)", "https://travel.state.gov/en/international-travel/travel-advisories/comoros.html"),
]

SPEC = dict(
    slug="comoras", name="Comoras", revision="18 sep 2026",
    sub="FUERA DE RUTA — tres islas sin enlace con el continente · solo en avión · Karthala, ylang-ylang y el contencioso de Mayotte",
    chips=[
        ("ESTATUS", "FUERA DE RUTA. Archipiélago sin conexión terrestre ni ferry de vehículos con el continente…"),
        ("CÓMO LLEGAR", "Solo en avión: aeropuerto Príncipe Said Ibrahim (HAH/FMCH), Hahaya, a 15 km de Moroni…"),
        ("VISADO", "A LA LLEGADA en el aeropuerto: 30 € o 15.000 KMF, 45 días, UNA SOLA ENTRADA, EN EFECTIVO…"),
        ("VEHÍCULO", "SIN VÍA PRACTICABLE desde el continente. Solo flete RoRo o contenedor contratado hasta Mutsamudu…"),
        ("SEGURIDAD", "MAEC: extremar precaución · disturbios mortales 2026"),
        ("SEGURO", "Carta Verde NO vale · póliza local en destino"),
        ("SALUD", "Malaria alta · cólera activo · fiebre amarilla no exigida"),
        ("DRONES", "Sin normativa ANACM · asumir requisa en aduana"),
        ("STARLINK", "No activo · previsto 2026, sin fecha firme"),
        ("4x4", "Inútil: sin ferry al continente · 40 €/día con chófer"),
        ("A PIE", "Moroni de día sí · nunca solo de noche"),
        ("PERRO", "Entrada: microchip, pasaporte, antirrábica en vigor y certificado sanitario internacional emitido MENOS DE 72…"),
        ("MONEDA", "Franco comorense (KMF), anclado al euro: 1 € ≈ 491-492 KMF…"),
        ("VENTANA", "Tropical húmedo, 2.700 mm anuales en Moroni. Lluvias y ciclones de diciembre a abril: el…"),
    ],
    center=[-11.88, 43.89], zoom=7,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle de las tres islas: Ngazidja (circunvalación) + Mwali + Ndzuwani, con saltos en avioneta o barco",
    corridor_alt_label="Solo Gran Comore: vuelta completa a Ngazidja por la circunvalación (RN1)",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Karthala_volcano-Comoros.jpg?width=1200",
    hero_credit="Monte Karthala · alKomor.com · CC BY-SA 2.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Comoras queda FUERA DE LA RUTA DE 2027 por un motivo estructural, no por seguridad: son tres islas en pleno canal de Mozambique y NO existe ningún ferry que lleve vehículos desde el continente africano ni desde Madagascar. Desde septiembre de 2025 sí hay un RoPax interinsular, el YAMEELA de Serdal International, que une Moroni con Mutsamudu con capacidad para 45 coches, pero solo navega entre islas: no resuelve el salto desde tierra firme. Meter el Grenadier y la Delica exigiría contratar flete marítimo en contenedor o RoRo desde Dar es Salam, Mombasa o Durban hasta Mutsamudu —el único puerto de aguas profundas del país, construido en 1982 y dedicado en tres cuartas partes a transbordo de contenedores—, con despacho aduanero, admisión temporal (arts. 239-245 del Código de Aduanas comorense de 2024) y seguro local. El coste del flete ida y vuelta está por confirmar, pero es de miles de euros por vehículo, más semanas de espera, para recorrer una isla que se cruza entera en un día por 40 € de coche con conductor. No compensa. Si algún día se hiciera, sería una excursión aparte: vuelo desde Nairobi, Adís Abeba o Dar es Salam a Hahaya (HAH) y visado de 30 € a la llegada. Lo que habría que decidir antes es el perro: Comoras es tercer país de situación antirrábica desfavorable y no figura en el Reglamento de Ejecución (UE) 2026/636, así que la vuelta a la UE exige titulación antirrábica hecha ANTES de salir de España.",
    facts=[
        ("Estatus", "FUERA DE RUTA. Archipiélago sin conexión terrestre ni ferry de vehículos con el continente. Ficha informativa, no operativa."),
        ("Cómo llegar", "Solo en avión: aeropuerto Príncipe Said Ibrahim (HAH/FMCH), Hahaya, a 15 km de Moroni. Ethiopian (Adís Abeba), Kenya Airways (Nairobi), Air Tanzania y Precision Air (Dar es Salam), Air Austral (Reunión), Ewa Air (Dzaoudzi) y Turkish (Estambul, estacional)."),
        ("Visado", "A LA LLEGADA en el aeropuerto: 30 € o 15.000 KMF, 45 días, UNA SOLA ENTRADA, EN EFECTIVO. Pasaporte con 6 meses de validez, billete de vuelta, reserva de alojamiento y unos 30 €/día de medios (MAEC, 18-5-2026)."),
        ("Vehículo/aduana", "SIN VÍA PRACTICABLE desde el continente. Solo flete RoRo o contenedor contratado hasta Mutsamudu. Admisión temporal regulada en los arts. 239-245 del Código de Aduanas de 2024. Entre islas sí hay RoPax desde 2025."),
        ("Seguro", "La Carta Verde NO cubre Comoras y el país no pertenece a ningún sistema regional de tarjeta (ni Carte Brune CEDEAO, ni Carte Rose CEMAC, ni COMESA Yellow Card). Seguro local obligatorio en destino."),
        ("Moneda", "Franco comorense (KMF), anclado al euro: 1 € ≈ 491-492 KMF. Economía casi solo en efectivo; cajeros escasos y concentrados en Moroni, Mitsamiouli y el puerto."),
        ("Perro", "Entrada: microchip, pasaporte, antirrábica en vigor y certificado sanitario internacional emitido MENOS DE 72 HORAS antes de llegar. Sin fuente oficial comorense localizada. Para volver a la UE hace falta titulación antirrábica."),
        ("Drones", "NO REGULADOS. La ANACM (anacm-comores.com) no publica ningún reglamento de aeronaves no tripuladas. Los repertorios dan el vuelo de extranjeros por no permitido. Asumir requisa en aduana: no llevar dron."),
        ("Starlink", "NO ACTIVO. Comoras figura como «previsto en 2026» en el seguimiento de despliegue africano (16-6-2026), sin fecha firme. Móvil: Comoros Telecom y Telma; datos por alrededor de 1 €/GB."),
        ("Seguridad", "MAEC: EXTREMAR LA PRECAUCIÓN. Freedom House 2026 lo puntúa con 41/100, «parcialmente libre» y a la baja. Disturbios mortales por el carburante en mayo de 2026."),
        ("Clima", "Tropical húmedo, 2.700 mm anuales en Moroni. Lluvias y ciclones de diciembre a abril: el ciclón Chido (dic. 2024) golpeó las tres islas. Karthala (2.361 m) activo a 10 km de la capital."),
        ("Sanidad", "Muy deficiente. Cólera declarado en febrero de 2024. Malaria de riesgo ALTO en todo el país. El hospital de referencia, El-Maarouf, estuvo en huelga indefinida en marzo de 2026. Seguro con repatriación imprescindible."),
    ],
    alerts=[
        "NO HAY FORMA REGULAR DE LLEVAR UN VEHÍCULO PROPIO DESDE EL CONTINENTE. El único RoPax que transporta coches, el YAMEELA (desde septiembre de 2025), navega SOLO entre Moroni y Mutsamudu: es interinsular, no conecta con África ni con Madagascar.",
        "Inestabilidad política crónica: más de veinte golpes o intentos desde la independencia de 1975. Azali Assoumani tomó el poder por golpe en 1999 y preside de nuevo desde 2016; Freedom House le atribuye represión de la oposición y limitación de la libertad de prensa.",
        "Las elecciones presidenciales de enero de 2024 dieron a Azali un 63 % rechazado por la oposición, con impugnación y disturbios. En enero de 2025 su partido se llevó 28 de los 33 escaños de la Asamblea.",
        "Mayo de 2026: el Gobierno subió el gasóleo un 46 % y la gasolina un 35 % el día 9; seis días de huelga y disturbios con dos muertos forzaron la suspensión del alza el 16-17 de mayo. El conflicto sigue abierto.",
        "Escasez recurrente de carburante en 2026: en junio las estaciones de Moroni estaban racionadas a 3.000 litros diarios. Sin gasóleo no hay bombeo eléctrico y el agua corriente se corta.",
        "El contencioso de Mayotte —cuarta isla del archipiélago, francesa tras los referendos de 1974 y 1976 y departamento desde 2011— mantiene militarizado el canal: Francia patrulla contra las travesías de kwassa-kwassa y la ONU llegó a pronunciarse a favor de Comoras.",
        "Naufragios de migrantes constantes en la ruta Anjouan-Mayotte: seis muertos y cinco desaparecidos en mayo de 2025, diecisiete cuerpos recuperados en marzo de 2026. El mar de la zona no es agua segura.",
        "El ciclón Chido (diciembre de 2024, vientos de 215 km/h) arrasó Mayotte —40 muertos y el 90 % de las construcciones dañadas— y golpeó Gran Comora, Anjouan y Mohéli. La temporada ciclónica va de diciembre a abril.",
        "El volcán Karthala (2.361 m), uno de los más activos del mundo, está a 10 km de Moroni. Sus episodios eruptivos cierran el espacio aéreo y contaminan con ceniza las cisternas de agua.",
        "Epidemia de cólera declarada en febrero de 2024, con foco en el norte de Gran Comora, todavía citada por el MAEC en mayo de 2026. Malaria de riesgo alto en todas las islas y todo el año.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Llegada y Moroni", "Aeropuerto de Hahaya → Moroni (medina, Badjanani, Volo Volo, puerto)", "~25 km · 1 día"),
        ("2 · Iconi y sur próximo", "Moroni → Iconi → Mitsoudjé → regreso a Moroni", "~35 km · 1 día"),
        ("3 · Karthala (subida)", "Moroni → Boboni/Mvouni → vivac en la caldera", "~20 km + marcha · 1 día"),
        ("4 · Karthala (bajada)", "Caldera → Boboni → Moroni", "~20 km + marcha · 1 día"),
        ("5 · Sur y costa este", "Moroni → Chindini → Foumbouni → Chomoni", "~110 km · 1 día"),
        ("6 · Norte de Ngazidja", "Chomoni → Mbéni → Lago Salé → Mitsamiouli", "~75 km · 1 día"),
        ("7 · Cierre del anillo", "Mitsamiouli → Ntsaoueni → Itsandra → Moroni", "~40 km · 1 día"),
        ("8 · Salto a Mohéli", "Moroni → Chindini (barca) o Hahaya (avioneta) → Fomboni", "~50 km + travesía · 1 día"),
        ("9 · Sur de Mohéli", "Fomboni → Nioumachoua (islotes, parque nacional)", "~30 km · 1 día"),
        ("10 · Tortugas y lago", "Nioumachoua → Itsamia → Lago Dziani Boundouni → Fomboni", "~70 km · 1 día"),
        ("11 · Salto a Anjouan", "Fomboni → Ouani (avioneta) → Mutsamudu", "~15 km + vuelo · 1 día"),
        ("12 · Mutsamudu y Hombo", "Mutsamudu (ciudadela, medina) → cascadas de Dziancoundré", "~20 km · 1 día"),
        ("13 · Ntringui y Domoni", "Mutsamudu → Dindi (lago Dzialandzé / Ntringui) → Domoni", "~55 km · 1 día"),
        ("14 · Moya y regreso", "Domoni → Moya (bosque y destilerías) → Ouani → vuelo a Moroni", "~60 km + vuelo · 1 día"),
    ],
    offroad=[
        "No existe una red 4x4 recreativa en Comoras: lo que hay es una circunvalación asfaltada en Gran Comore, razonablemente mantenida según la FCDO (10-12-2025), y a partir de ahí pistas de servicio agrícola; la propia FCDO dice que «muchas otras carreteras están en mal estado».",
        "Las pistas secundarias y rurales no están pavimentadas, están mal mantenidas y pueden volverse intransitables en la estación de lluvias, de noviembre a abril, según la ficha de conducción de Carol.rent; hay que asumir tramos de grava, polvo y superficie irregular.",
        "El acceso al Karthala es la única «ruta» de montaña relevante: ramal de tierra desde la circunvalación hasta los pueblos de la ladera oeste, y de ahí a pie con guía; Canadá recuerda (09-09-2026) que las erupciones pueden producirse en cualquier momento y que hay que consultar a las autoridades locales antes de subir.",
        "En Mohéli la carretera principal Fomboni–costa sur da paso a pistas de tierra hacia Nioumachoua e Itsamia dentro del parque nacional: son las pistas donde el 4x4 es realmente necesario, y circulan dentro de un área protegida, así que la velocidad y las salidas del trazado están de facto limitadas por los ecoguardas del parque.",
        "En Anjouan la red es de asfalto degradado con curvas continuas y fuertes pendientes (Mutsamudu–Domoni, Mutsamudu–Moya); Canadá advierte de carreteras estrechas, baches, iluminación deficiente y animales sueltos, y desaconseja conducir de noche en todo el país.",
        "No hay zonas militarmente vetadas documentadas para el viajero, pero sí un riesgo político: FCDO y Canadá avisan de que las protestas pueden estallar sin aviso, sobre todo en periodo electoral, con cortes de carretera y toques de queda, y el MAEC recuerda la sensibilidad por Mayotte.",
        "Autonomía: las gasolineras son escasas y se concentran en Moroni y Mutsamudu, así que se reposta siempre que se puede; se circula por la derecha y el permiso extranjero se acepta temporalmente (tres meses para el carnet británico según la FCDO).",
        "Permisos: para cruzar en barca de Chindini a Mohéli, Wikivoyage indica que el extranjero necesita un permiso de policía (unos 10.000 KMF) si va en lancha rápida; ese trámite, y no la pista, es el cuello de botella real del itinerario.",
    ],
    senderismo=[
        "Ascensión al Karthala (Gran Comore): dos jornadas desde los pueblos de la ladera oeste hasta el borde de la caldera de 3 x 4 km, con vivac arriba; obligatorio guía y porteador, agua para todo el recorrido y consulta previa del estado del volcán.",
        "Vuelta al cráter del Lago Salé (norte de Gran Comore): sendero corto que rodea el cráter y la colina volcánica vecina, con vistas al océano; una o dos horas, sin desnivel serio.",
        "Cascadas de Dziancoundré (Anjouan): desde el plateau de Hombo, al sur de Mutsamudu, se sigue la conducción de agua hasta la captación y se entra en un valle con varios saltos, el mayor de unos 12 m; hay un paso escabroso sobre la tubería.",
        "Lago Dzialandzé (Anjouan): sendero de un kilómetro desde la carretera Koni-Djodjo–Dindi hasta el lago de cráter, a 910 m de altitud, 280 por 150 metros; es la marcha más asequible del interior de Anjouan.",
        "Cumbre del Mont Ntringui (Anjouan, 1.595 m): continuación del anterior por el bosque húmedo de altura, dentro del parque nacional y del sitio Ramsar; medio día largo con guía, mejor salir antes del amanecer porque la cima se encapota.",
        "Bosque de Moya (Anjouan): recorrido corto por las 500 hectáreas de selva relicta sobre la costa de Moya, con opción de ver lémures y la roussette de Livingstone; se entra con guía del pueblo.",
        "Vigilancia nocturna de tortugas en Itsamia (Mohéli): caminata por la playa al anochecer con las asociaciones locales para ver la puesta de tortuga verde; se hace sin linternas blancas y siguiendo las instrucciones de los ecoguardas.",
        "Islotes de Nioumachoua (Mohéli): tras la travesía en barca, vueltas a pie por los islotes de arena blanca y sus colonias de aves marinas; recorridos de menos de una hora, sin sombra ni agua.",
    ],
    acampada=[
        "No se ha localizado ningún camping formal en las Comoras en las fuentes abiertas consultadas; tampoco hay fichas de iOverlander ni de Tracks4Africa accesibles para el archipiélago, coherente con que no exista acceso overland por carretera.",
        "La fórmula real de pernocta en naturaleza son los bungalows comunitarios de los pueblos de Mohéli: Wikivoyage cita Nioumachoua, Itsamia y Ouallah 1 y 2, gestionados por las asociaciones locales y ligados al parque nacional.",
        "Wikivoyage menciona expresamente la posibilidad de dormir en los islotes del Parque Nacional de Mohéli «rodeado de la naturaleza más intacta», organizando el transporte en barca desde Nioumachoua; es la acampada más atractiva y la que exige acuerdo previo con el parque.",
        "Vivac en la caldera del Karthala: es la pernocta de montaña habitual de la ascensión de dos días, sin refugio ni agua; hay que subirlo todo y contar con viento y frío nocturnos a 2.361 m.",
        "Acampada libre en playa (Chomoni, Mitsamiouli, Chindini): no hay norma publicada que la prohíba, pero el MAEC desaconseja expresamente pasear solo de noche por playas y el FCDO señala mayor riesgo en playas nocturnas; si se hace, con el grupo junto y permiso del pueblo.",
        "Protocolo de pueblo: en las tres islas la tierra está muy repartida y todo tiene dueño; la práctica sensata es pedir permiso al jefe del pueblo o a la asociación local antes de montar tienda, como se hace para las salidas de tortugas y los islotes.",
        "Estacionalidad: la temporada de ciclones va de diciembre a abril según Canadá (monzones y ciclones tropicales), con inundaciones y corrimientos; acampar fuera de esa ventana.",
        "Salud: hay epidemia de cólera declarada desde febrero de 2024 según el MAEC, además de malaria y dengue; acampando hay que extremar el tratamiento del agua y la protección antimosquitos.",
    ],
    visado=[
        "MODALIDAD: VISADO A LA LLEGADA. No hay eVisa ni trámite previo obligatorio en embajada para españoles; se emite en el aeropuerto de Hahaya (HAH) y en los demás puntos de entrada.",
        "COSTE: 30 € o 15.000 KMF, EN EFECTIVO (euros, dólares o francos comorenses). No se admite tarjeta: llevar los billetes encima.",
        "VALIDEZ: 45 días, UNA SOLA ENTRADA. Prórrogas y entradas adicionales se gestionan en la Dirección de Inmigración, en Moroni.",
        "REQUISITOS: pasaporte con SEIS MESES de validez desde la llegada, billete de vuelta o de continuación, reserva de alojamiento y acreditar unos 30 €/día de medios de subsistencia (MAEC, 18-5-2026; FCDO, requisitos de entrada).",
        "NO HAY FRONTERA TERRESTRE: el archipiélago no linda con ningún país, así que la figura de «visado válido en frontera terrestre» NO APLICA. Todas las entradas son aéreas o portuarias.",
        "Para consultas previas, la embajada de Comoras en París es la representación de referencia que cita el FCDO. España no tiene embajada residente en Moroni.",
    ],
    fronteras_rows=[
        ("Entrada internacional (aérea)", "Aeropuerto Internacional Príncipe Said Ibrahim (HAH/FMCH), Hahaya, Gran Comora", "ABIERTO. Pista de asfalto de 2.900 m, 15 km al norte de Moroni. Visado a la llegada por 30 € en efectivo. Único punto de entrada realista. Fuentes: Wikipedia (aeropuerto) y MAEC 18-5-2026."),
        ("Entrada secundaria (aérea)", "Aeropuerto de Ouani, Anjouan (AJN)", "OPERATIVO para vuelos interinsulares y algún enlace con Dar es Salam vía Precision Air. Servicio irregular, con cancelaciones frecuentes. Frecuencias de 2026 POR CONFIRMAR."),
        ("Entrada secundaria (aérea)", "Aeropuerto de Bandar Es Eslam, Mohéli (NWA)", "OPERATIVO solo para avionetas interinsulares; sin tráfico internacional regular. Estado exacto en 2026 POR CONFIRMAR con la aviación civil comorense."),
        ("Puerto principal", "Puerto de Moroni, Gran Comora", "OPERATIVO pero MUY LIMITADO: muelle de unos 80 m. Desde septiembre de 2025 es cabecera del RoPax YAMEELA hacia Mutsamudu. No recibe buques del continente con vehículos. Fuentes: Wikipedia (Moroni) y Shippax 11-9-2025."),
        ("Puerto de aguas profundas", "Puerto de Mutsamudu, Anjouan (12,1675° S / 44,3939° E)", "ÚNICO puerto de aguas profundas del país, de 1982; tres cuartas partes de su tráfico es transbordo de contenedores. Es la única vía teórica para meter un vehículo en contenedor. Costes POR CONFIRMAR. Fuente: Wikipedia (Mutsamudu)."),
        ("Enlace interinsular con vehículos", "RoPax YAMEELA · Moroni – Mutsamudu (Serdal International / Noatum Maritime)", "ACTIVO desde el 11 de septiembre de 2025. 190 pasajeros y 45 vehículos. SOLO INTERINSULAR: no conecta con el continente. Horarios y tarifas POR CONFIRMAR. Fuente: Shippax."),
        ("Enlace interinsular rápido", "Chindini (sur de Gran Comora) – Mohéli / Anjouan", "Barcos rápidos, unas 4 salidas diarias, hasta 2 h, ~75 € por trayecto. Sin horario garantizado. Canadá advierte de sobrecarga y mal mantenimiento (9-9-2026)."),
        ("Paso terrestre", "No existe ninguno", "NO APLICA: Comoras no tiene frontera terrestre con ningún país. Mayotte, la cuarta isla, es departamento francés y su acceso está fuertemente militarizado contra la inmigración irregular."),
    ],
    vehiculos=[
        "NO HAY VÍA PRACTICABLE para entrar con el Grenadier y la Delica desde el continente: ningún ferry de vehículos une África oriental o Madagascar con las Comoras.",
        "Desde el 11 de septiembre de 2025 el RoPax YAMEELA (Serdal International, 560 GT, 190 pasajeros y 45 coches) une Moroni con Mutsamudu, pero es un servicio ESTRICTAMENTE INTERINSULAR.",
        "La única opción teórica de entrada es flete marítimo contratado —contenedor de 20/40 pies o RoRo— desde Dar es Salam, Mombasa o Durban hasta Mutsamudu, con despacho aduanero completo. Coste y plazos POR CONFIRMAR con un transitario.",
        "ADMISIÓN TEMPORAL: regulada en los artículos 239 a 245 del Código de Aduanas de la Unión de las Comoras de 2024, con exoneración total o parcial de derechos para mercancías reexportadas sin modificación. El texto no menciona el carnet de passages ni el triptyque.",
        "CARNET DE PASSAGES: AIT/FIA NO tiene ninguna organización emisora ni avalista en Comoras y remite a tramitarlo en países vecinos. Si la aduana comorense lo exige o no está SIN CONFIRMAR: preguntar a douane@douane.gov.km o al +269 773 18 89.",
        "SEGURO: la Carta Verde española no cubre Comoras y el país no está en ningún sistema regional de tarjeta. Habría que contratar póliza de responsabilidad civil local a la llegada.",
        "CONDUCCIÓN POR LA DERECHA, herencia francesa. Las guías comerciales de permisos dan el permiso internacional de conducción por obligatorio; su exigencia legal real está POR CONFIRMAR, pero conviene llevarlo.",
        "RED VIARIA: en Gran Comora, unos 70 de los 88 km de carretera están asfaltados pero en mal estado general; solo los ejes Hahaya-Moroni y Moroni-Chindini están decentes. Canadá reporta accidentes mortales frecuentes (9-9-2026). No conducir de noche fuera de zona urbana.",
        "ALTERNATIVA REALISTA Y BARATA: coche con conductor local por 30-40 €/día con combustible incluido, o taxi compartido en Moroni por unos 0,50 €. Cubre cualquier visita razonable sin exponerse al racionamiento de carburante.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "AUTORIDAD: Agence Nationale de l'Aviation Civile et de la Météorologie (ANACM), servicio administrativo bajo tutela del Ministerio de Aviación Civil. Contacto: direction@anacm-comores.com, +269 773 80 03, Moroni.",
        "ESTADO: NO REGULADO. La página de reglamentación de la ANACM (anacm-comores.com/reglementation.php) organiza sus normas en AGA, AIG, AIR, ANS, LEG, OPS, ORG, PEL, SGS y Sûreté, sin ninguna categoría de drones, UAS ni RPAS.",
        "Los repertorios especializados (drone-laws.com, consultado en 2026) dan el vuelo de visitantes extranjeros como «no permitido» y solo reconocen operaciones gubernamentales con registro. A falta de norma, recomiendan atenerse a los estándares OACI: línea de visión, 150 m de altura máxima, 50 m de separación y 8 km de los aeropuertos.",
        "Ni el MAEC (18-5-2026) ni Canadá (9-9-2026) mencionan drones en sus fichas. El FCDO sí advierte de reglas estrictas de importación y de la obligación de declarar en aduana cualquier mercancía sujeta a prohibición o gravamen.",
        "RIESGO OPERATIVO CONCRETO: el contencioso de Mayotte, la presencia naval francesa y las patrullas antimigración hacen que cualquier vuelo sobre costa, puerto o instalación oficial se lea como actividad hostil. Si alguna vez se planteara, el único camino sería autorización escrita previa de la ANACM, tramitada con meses de antelación. No hay procedimiento publicado.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "NO DISPONIBLE a día de hoy. Comoras aparece como «previsto en 2026» en el seguimiento sectorial del despliegue africano (tech.africa, actualizado 16-6-2026), junto a otros 18 países del continente, sin fecha concreta.",
        "El bloqueo es regulatorio y de infraestructura: hace falta licencia de la autoridad comorense de telecomunicaciones y una pasarela terrestre regional. CRITERIO DE CIERRE: comprobar el mapa oficial de starlink.com, que en esta consulta no devolvió el estado del país.",
        "OPERADORES MÓVILES: Comoros Telecom (marca Huri) y Telma Comores. SIM local con paquete de datos por alrededor de 1 €/GB, según relatos de viajeros.",
        "La cobertura y la velocidad son muy irregulares fuera de Moroni; en Mohéli y en el interior de Gran Comora hay que contar con quedarse sin datos.",
        "Wifi utilizable en hoteles de Moroni (Itsandra) y algunos restaurantes. No planificar trabajo remoto que dependa de conexión estable, y menos durante los cortes eléctricos por falta de gasóleo.",
    ],
    perro_intro=[
        "ENTRADA (fuente especializada, NO oficial): microchip o identificación electrónica, pasaporte del animal, VACUNA ANTIRRÁBICA EN VIGOR y CERTIFICADO SANITARIO INTERNACIONAL emitido por un veterinario MENOS DE 72 HORAS antes de la llegada. No se exige validación por veterinario oficial ni titulación antirrábica para entrar (Anivetvoyage, ficha de 7-1-2023).",
        "NO HEMOS LOCALIZADO NINGUNA PÁGINA OFICIAL del servicio veterinario nacional comorense que publique estos requisitos. El dato de entrada queda como PROBABLE, no confirmado: hay que validarlo con la aduana (douane@douane.gov.km, +269 773 18 89) o con la embajada de Comoras en París.",
        "SALIDA DE COMORAS: la misma fuente indica que la titulación antirrábica SÍ es obligatoria para salir del país. Coherente con la clasificación de Comoras como tercer país de situación antirrábica DESFAVORABLE.",
        "RAZAS PROHIBIDAS: sin información publicada. El problema práctico no es la norma escrita: Comoras es musulmana en un 99,6 % y el perro tiene muy mala consideración social; el rechazo cotidiano y la negativa de alojamientos son el obstáculo real.",
        "VUELTA A LA UE: Comoras NO FIGURA en los anexos del Reglamento de Ejecución (UE) 2026/636. Se aplica la vía A del Reglamento Delegado (UE) 2026/131: microchip (art. 13), primovacunación antirrábica completa al menos 21 días antes del desplazamiento (art. 14.b) y PRUEBA DE VALORACIÓN DE ANTICUERPOS ANTIRRÁBICOS válida conforme al anexo XXI, punto 1 (art. 14.c).",
        "LA TITULACIÓN HAY QUE LLEVARLA HECHA Y ANOTADA EN EL PASAPORTE ANTES DE SALIR DE ESPAÑA. Si se hace desde Comoras, se activa el periodo de espera que impone el anexo XXI (tres meses en el régimen clásico) y el perro se queda bloqueado en las islas. Además, el certificado zoosanitario de entrada en la UE se expide como máximo DIEZ DÍAS antes de la llegada (art. 19) y vale seis meses desde el control fronterizo (art. 18).",
        "VETERINARIOS Y RIESGOS: no hemos podido confirmar que exista clínica veterinaria con estándares europeos en Moroni. Rabia endémica en la región, garrapatas y enfermedades vectoriales, calor y humedad extremos, y ninguna posibilidad de evacuación veterinaria. Dar por hecho que no hay atención utilizable.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "MALARIA DE RIESGO ALTO EN TODO EL PAÍS Y TODO EL AÑO (TravelHealthPro/NaTHNaC, marzo de 2026). Quimioprofilaxis obligatoria en la práctica: atovacuona/proguanil o doxiciclina (desde 1-2 días antes) o mefloquina (desde 2-3 semanas antes).",
        "FIEBRE AMARILLA: NO hay requisito de certificado bajo el Reglamento Sanitario Internacional (TravelHealthPro y Canadá, 2026). Si se llega de país endémico conviene llevarlo igualmente, porque la exigencia se aplica de forma discrecional.",
        "EPIDEMIA DE CÓLERA declarada en febrero de 2024, con foco en el norte de Gran Comora; el MAEC la seguía citando el 18 de mayo de 2026. Vacuna recomendada para estancias con acceso limitado a agua segura.",
        "VACUNAS: hepatitis A para todo el mundo, tétanos si la última dosis tiene más de diez años, fiebre tifoidea, rabia para estancias largas o zonas remotas, y hepatitis B. Dengue y chikungunya presentes: repelente de día y de noche.",
        "ASISTENCIA MUY DEFICIENTE. El hospital de referencia es el Centre Hospitalier National El-Maarouf, en Moroni, abierto en 1954 y en obras de modernización desde 2017 (proyecto de unos 55 millones de euros). Sus contratados iniciaron huelga indefinida el 9 de marzo de 2026, con solo servicios mínimos de urgencias.",
        "SEGURO PRIVADO CON REPATRIACIÓN IMPRESCINDIBLE. Cualquier urgencia seria significa evacuación aérea a Reunión, Nairobi o Sudáfrica, con coste de decenas de miles de euros y sujeta a que haya vuelo.",
        "Corrientes de resaca frecuentes: Canadá reporta varios ahogamientos al año y no hay servicio de socorrismo en ninguna playa.",
    ],
    seguridad_intro="El MAEC pide EXTREMAR LA PRECAUCIÓN en todo el país, sin zonas formalmente desaconsejadas, y Canadá habla de «alto grado de precaución» por la falta de servicios de emergencia. La delincuencia común es baja —carteristas en mercados y parques—, pero el riesgo real es político: más de veinte golpes o intentos desde 1975, unas presidenciales impugnadas en enero de 2024 y una huelga de seis días en mayo de 2026 por el carburante que dejó dos muertos. Freedom House bajó la nota a 41/100 en 2026. A eso se suma un canal militarizado por Mayotte.",
    seguridad=[
        "MAEC (18-5-2026): SE RECOMIENDA EXTREMAR LA PRECAUCIÓN DURANTE EL VIAJE. No hay zonas explícitamente vetadas, pero sí vigilancia reforzada en todo el territorio.",
        "Canadá (9-9-2026): «alto grado de precaución» por la limitada disponibilidad de servicios de emergencia y unas instalaciones médicas inadecuadas.",
        "Freedom House 2026: 41/100, «parcialmente libre», un punto menos que el año anterior; 16/40 en derechos políticos y 25/60 en libertades civiles, con deterioro de la libertad religiosa por intolerancia hacia confesiones no suníes.",
        "Inestabilidad crónica: más de veinte golpes o intentos desde 1975. Azali Assoumani llegó al poder por golpe en 1999, volvió en 2016 y, según Freedom House, ha consolidado el poder reprimiendo a la oposición y limitando la prensa.",
        "Enero de 2024: victoria oficial de Azali con el 63 %, rechazo de la oposición, impugnación y disturbios. En enero de 2025 su partido se llevó 28 de 33 escaños. El clima no se ha normalizado.",
        "Mayo de 2026: huelga general de seis días contra la subida del carburante, con DOS MUERTOS en los enfrentamientos. El Gobierno suspendió el alza el 16-17 de mayo y abrió negociaciones.",
        "Las manifestaciones degeneran con poco aviso y los toques de queda se decretan sin preaviso (Canadá). Evitar cualquier concentración y no fotografiar despliegues policiales.",
        "PIRATERÍA: el MAEC advierte de riesgo para embarcaciones pequeñas. Además, el canal Anjouan-Mayotte concentra naufragios de kwassa-kwassa con migrantes: seis muertos en mayo de 2025, diecisiete cuerpos en marzo de 2026.",
        "Contencioso de Mayotte: Comoras reclama la cuarta isla, francesa tras los referendos de 1974 y 1976 y departamento desde 2011. Francia patrulla con la gendarmería marítima y vetó en 1976 una resolución del Consejo de Seguridad favorable a Comoras. La tensión es permanente.",
    ],
    agua=[
        "EL AGUA DE RED NO ES POTABLE en ninguna isla. Para beber, solo embotellada o tratada con filtro y purificador. Ojo también con el hielo y las verduras crudas.",
        "Para llenar depósitos de ducha y lavado, el suministro es INESTABLE porque depende del bombeo eléctrico: las autoridades cifraban en 2026 la necesidad de «doce horas seguidas de electricidad» para llenar los depósitos de la red.",
        "La escasez de gasóleo de 2026 encadenó cortes de agua en Moroni: sin carburante no giran las bombas y la distribución se vuelve aleatoria. No dar por hecho que se puede repostar agua en la capital.",
        "Moroni recibe unos 2.700 mm de lluvia al año, con precipitación abundante casi todo el año: en estación húmeda (diciembre-abril) la recogida de agua de lluvia es una alternativa real, filtrando y tratando siempre.",
        "Las cenizas del Karthala contaminan cisternas y depósitos tras los episodios eruptivos. Después de una erupción, no usar agua recogida sin filtrar y hervir.",
        "PRECAUCIÓN AÑADIDA: cólera activo desde febrero de 2024 con foco en el norte de Gran Comora. Tratar toda el agua como sospechosa, también la de los alojamientos.",
    ],
    combustible=[
        "PRECIOS DE LA SUBIDA DEL 11-5-2026 (La Gazette des Comores, 10-5-2026): GASOLINA 1.000 KMF/l (≈2,03 €/l), desde 750 KMF; GASÓLEO 950 KMF/l (≈1,93 €/l), desde 650 KMF. Subidas del 33 % y del 46 % respectivamente.",
        "Esa subida provocó seis días de huelga y dos muertos, y el presidente la SUSPENDIÓ el 16-17 de mayo de 2026 abriendo negociaciones. El precio vigente hoy está POR CONFIRMAR: previsiblemente de vuelta a 750 y 650 KMF/l.",
        "ESCASEZ ESTRUCTURAL: en junio de 2026 las estaciones de Moroni estaban racionadas a 3.000 litros diarios. La importación depende de la Société Comorienne des Hydrocarbures (SCH), que controla más de la mitad del gasóleo y acumula unos 16 millones de euros de pérdidas por revenderlo bajo coste a la eléctrica Sonelec.",
        "La red de estaciones se concentra en Moroni y en el eje hacia Hahaya y Chindini. Fuera de ahí, contar con bidones y con reventa informal a precio inflado.",
        "CALIDAD: sin datos verificados sobre azufre ni filtrado. Con motores diésel modernos como los del Grenadier y la Delica, asumir riesgo y llevar filtros de repuesto. En periodo de racionamiento, el riesgo de combustible sucio sube.",
        "El coche con conductor local (30-40 €/día) lleva el combustible incluido: es la forma sensata de moverse sin pelearse con el racionamiento ni con las colas.",
    ],
    experiencias_intro="No hay relatos de overlanders con vehículo propio en Comoras, sencillamente porque no se puede llegar por carretera ni embarcar un coche desde el continente: todo lo publicado son viajes en avión con transporte local. Recogemos lo que aporta cada uno sobre logística real, con su fuente y su año.",
    experiencias=[
        "Visado fácil, todo lo demás no: Unusual Traveler confirma que cualquiera obtiene el visado de 45 días a la llegada por 30 €, con reserva de alojamiento y billete de vuelta. No hay vuelos directos desde fuera de África Oriental: las mejores conexiones son Kenya Airways vía Nairobi y Ethiopian vía Adís Abeba, con retrasos frecuentes en las rutas por Madagascar, Tanzania o Reunión. El relato desmonta la idea de llegar por libre desde Europa.",
        "Barcos entre islas: 75 € y gente que se ahoga: el mismo blog describe los ferries rápidos Chindini-Mohéli, unas cuatro salidas diarias, hasta dos horas y 75 € por trayecto. Los vuelos locales cuestan lo mismo pero «se cancelan a menudo». Remata con una frase que vale por todo un análisis de riesgo: «los accidentes y los ahogamientos no son desconocidos». Sin seguro específico, no subir.",
        "Los vuelos domésticos son un billete a ninguna parte: Heart My Backpack (visita de 2017, actualizado en abril de 2022) los califica de «increíblemente poco fiables, cancelados o retrasados constantemente» y recomienda los barcos rápidos, unos 150 € ida y vuelta con traslados incluidos. Su consejo operativo es de manual: nunca hacer el trayecto interinsular el mismo día del vuelo internacional de salida.",
        "Moverse por Gran Comora cuesta 40 € al día: Heart My Backpack fija los precios reales de tierra: taxi compartido en Moroni por unos 0,50 €, traslado al aeropuerto por 10 € y coche privado con conductor la jornada completa por 40 €. Con esas cifras, meter un 4x4 propio en la isla deja de tener sentido económico antes incluso de mirar el precio del flete marítimo.",
        "Carreteras: dos tramos buenos y el resto, baches: Unusual Traveler resume que solo los ejes aeropuerto-Moroni y Moroni-Chindini están en condiciones. Las guías de conducción cifran en unos 70 de 88 km el asfalto de Gran Comora, «en mal estado general». Canadá (9-9-2026) completa el cuadro con «problemas graves de seguridad vial» y accidentes mortales frecuentes.",
        "Economía de efectivo y cajeros contados: Unusual Traveler sitúa los cajeros en Moroni, Mitsamiouli y el puerto (actualización de noviembre de 2019) y fija el cambio en 1 € ≈ 491 KMF. Canadá lo confirma en 2026: economía «mayoritariamente de efectivo» con cajeros limitados. Hay que entrar con euros en metálico, también para pagar el visado, que no admite tarjeta.",
        "Conectividad: SIM local a 1 €/GB y poco más: Heart My Backpack recomienda comprar SIM comorense con paquete de datos por alrededor de 1 €/GB. Unusual Traveler describe un internet limitado, con wifi utilizable en el hotel Itsandra y el restaurante New Select de Moroni. Ninguno de los dos menciona conexión fiable fuera de la capital, y Starlink sigue sin activarse.",
        "Alojamiento: Airbnb o nada: Unusual Traveler avisa de que no hay hostales ni casas de huéspedes al uso y que la oferta real es Airbnb, entre 35 y 44 €. Heart My Backpack da una horquilla de 32 a 80 € por noche, en algunos casos con comidas incluidas. Sin camping ni áreas de pernocta: otra razón por la que un vehículo propio no aportaría nada aquí.",
        "Seguridad percibida frente a seguridad real: Unusual Traveler dice haberse sentido «100 % seguro» y recuerda que la población es musulmana suní casi al completo, con recomendación de vestir con recato. Heart My Backpack recibió atención médica sin incidentes. Ninguno de los dos viajó durante los disturbios de 2024 ni durante la huelga del carburante de mayo de 2026: sus impresiones son de otro momento.",
        "Lo que nadie cuenta porque no se puede hacer: no hemos encontrado un solo relato de overlander con vehículo propio en Comoras entre 2019 y 2026, ni en blogs ni en foros. La ausencia es el dato: sin enlace marítimo de coches con el continente, el país queda fuera del circuito overland del este de África, que salta de Tanzania a Malaui o Mozambique por tierra. El único movimiento rodado posible es el RoPax interinsular abierto en 2025.",
    ],
    pendientes=[
        ("Requisitos oficiales de entrada del perro", "Obtener respuesta escrita de la aduana comorense (douane@douane.gov.km, +269 773 18 89) o de la embajada de Comoras en París confirmando microchip, antirrábica y certificado sanitario de menos de 72 horas."),
        ("Página oficial del organismo veterinario nacional", "Localizar y abrir un portal institucional comorense (ministerio de agricultura o servicios veterinarios) que publique requisitos de importación de animales. Hoy solo existe accesible el portal de aduanas."),
        ("Precio vigente del carburante", "Confirmar en La Gazette des Comores o en la SCH si tras la suspensión de mayo de 2026 el precio volvió a 750 KMF/l de gasolina y 650 KMF/l de gasóleo, o si se fijó otro."),
        ("Coste real del flete marítimo de un vehículo", "Pedir presupuesto en firme a un transitario para contenedor de 20 pies Dar es Salam-Mutsamudu ida y vuelta, con despacho y admisión temporal incluidos."),
        ("Exigencia de CPD en la aduana comorense", "Confirmar con la Direction Générale des Douanes si un vehículo extranjero en admisión temporal (arts. 239-245 del Código de 2024) necesita carnet de passages o basta con un documento local."),
        ("Horarios, tarifas y política de animales del RoPax YAMEELA", "Contactar con Serdal International o Noatum Maritime y obtener el horario Moroni-Mutsamudu, la tarifa por vehículo y si admite perros a bordo."),
        ("Consulado honorario o viceconsulado en Moroni", "Verificar con el MAEC si el vicecónsul del teléfono +269 3688964 mantiene oficina abierta, su dirección exacta y su horario."),
        ("Starlink", "Consultar el mapa oficial de starlink.com y confirmar si Comoras ha pasado de «previsto 2026» a activo, con fecha y precio."),
        ("Normativa de drones de la ANACM", "Escribir a direction@anacm-comores.com pidiendo si existe reglamento de aeronaves no tripuladas y, de haberlo, el procedimiento de autorización para extranjeros."),
        ("Estado operativo de los aeropuertos de Anjouan (AJN) y Mohéli (NWA)", "Confirmar con Precision Air o con la ANACM qué rutas siguen activas en 2026 y con qué frecuencia."),
        ("Atención veterinaria en Moroni", "Verificar si existe alguna clínica veterinaria con capacidad de urgencias y su contacto; si no la hay, dejarlo escrito en el dosier del perro."),
        ("Coordenadas del hospital El-Maarouf y del puerto de Moroni", "Verificar sobre cartografía: las que damos son aproximadas, derivadas del centro de Moroni, no de una ficha con coordenadas publicadas."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las páginas abiertas en esa sesión; cada dato procede de una fuente citada y fechada, y lo que no se ha podido confirmar aparece como «por confirmar» y en la lista de pendientes. Esto es una herramienta de planificación, no una autorización: los requisitos de entrada, aduana, veterinarios y sanitarios los fija cada administración y cambian sin aviso, y en Comoras el precio del carburante y el suministro de agua han cambiado varias veces en un mismo año. Verificar siempre en la fuente oficial antes de moverse.",
    emergency="TELÉFONOS verificados en el MAEC (ficha de 18-5-2026) y en travel.gc.ca (9-9-2026). EMERGENCIA CONSULAR DE ESPAÑA: +27 761 146 152, de la Embajada en Pretoria, competente para Comoras (Lord Charles Complex, 337 Brooklyn Road; centralita +27 12 460 01 23). VICECONSULADO EN MORONI: +269 3688964. POLICÍA: 17, o +269 773 46 63. BOMBEROS: 18. URGENCIAS MÉDICAS: +269 772 03 73. No existe un 112 operativo. Llevar los números en papel: la cobertura móvil falla y la economía es de efectivo.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

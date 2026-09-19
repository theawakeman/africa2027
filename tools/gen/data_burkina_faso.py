# -*- coding: utf-8 -*-
"""Burkina Faso — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Burkina Faso está EXCLUIDO POR PROTOCOLO: junta militar desde los golpes de enero y septiembre de 2022, insurgencia yihadista que controla o disputa buena parte del territorio, salida de la CEDEAO junto a Mali y Níger (Alianza de Estados del Sahel) y desaconsejo total del MAEC. La app solo tiene una ficha stub: créala entera con el formato del piloto de Túnez. La ficha es INFORMATIVA: cada PDI tiene que decir en qué región está y qué dice el MAEC de esa región con fecha, porque el suroeste (Banfora, Bobo) y el este o el Sahel no están igual. Documenta también qué ha pasado con los visados y las tasas desde la salida de la CEDEAO y si la Carte Brune sigue sirviendo.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/burkina-faso.json y audit/pdi/burkina-faso.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Uagadugú · Museo Nacional, catedral y mercado Rood Woko", cat="Ciudad · servicios", prio="Alta",
        dog="no recomendado", time="1-2 noches",
        lat=12.3764764, lon=-1.4729382,  # Google Maps: Museo Nacional de Burkina Faso
        desc="Capital mossi de algo más de 2,4 millones de habitantes (censo 2019) a 305 m de altitud, y una de las POCAS CAPITALES DEL MUNDO QUE NO ESTA NI EN LA COSTA NI JUNTO A UN RIO: se abastece de la presa de Ziga, 45 km al este. La parada útil son el Museo Nacional, la catedral de la Inmaculada Concepcion y Rood Wooko, el mayor mercado del país. Es además el único sitio del país con embajadas, talleres serios y combustible garantizado. Aviso: el MAEC desaconseja el viaje a todo Burkina Faso, capital incluida, y recomienda no hacer por carretera el trayecto Uagadugú-Bobo.",
        dog_note="El museo y la catedral no admiten animales; el gran mercado es un gentio con motos. Perro en el vehículo o en el alojamiento.",
        visit={
            "why": "Es la base logística obligada: repostaje, visados, reparaciones y el único museo nacional del país. Sin esta parada no hay expedición.",
            "see": "Coleccion etnográfica y de mascaras del Museo Nacional, la catedral de ladrillo de la Inmaculada Concepcion y el laberinto de Rood Wooko, el mayor mercado de Burkina Faso.",
            "access": "Asfalto en todos los accesos (RN1 al oeste, RN4 al este); aparcamiento vigilado en hoteles del centro y de Ouaga 2000, suficiente para dos 4x4. Horarios y tarifas del museo POR CONFIRMAR: no hemos localizado página oficial operativa. Región de Kadiogo (antes Centre). El pin marca la entrada del Museo Nacional.",
            "when": "Noviembre a febrero, en harmatan seco; visitar el mercado a primera hora, antes del calor.",
            "skip": "Descartar el país entero mientras el MAEC mantenga el desaconsejo total del 19-05-2025; si se entra, reducir Uagadugú a lo administrativo.",
        },
        links=[
            {"label": "Uagadugú (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ouagadougou"},
            {"label": "Rood Wooko (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Rood_Wooko"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ouagadougou_street_in_2004.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ouagadougou_street_in_2004.jpg",
                "credit": "Syced · CC0",
                "caption": "Una calle de Uagadugú.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/July_2004_Ouagadougou_5.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:July_2004_Ouagadougou_5.jpg",
                "credit": "Syced · CC0",
                "caption": "El centro de Uagadugú.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/July_2004_Ouagadougou_streets_12.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:July_2004_Ouagadougou_streets_12.jpg",
                "credit": "Syced · CC0",
                "caption": "Calles de la capital burkinesa.",
            },
        ],
    ),
    dict(
        n=2, name="Bobo-Diulasso · gran mezquita de adobe y barrio de Dioulassoba", cat="Cultura", prio="Alta",
        dog="prohibido", time="1-2 noches",
        lat=11.1649219, lon=-4.3051542,  # Google Maps: Bobo-Diulasso (la gran mezquita no figura como objeto)
        desc="Segunda ciudad del país, con 1.129.000 habitantes según el censo de 2023. Su gran mezquita de banco, levantada en 1880 o 1893 fruto del pacto entre el rey de Sia y el almami Sidiki Sanou, es POSIBLEMENTE EL MAYOR EJEMPLO DE ARQUITECTURA SUDANO-SAHELIANA DE BURKINA FASO. A su lado, Dioulassoba conserva el nucleo del viejo pueblo de Sia, aunque fue muy alterado en 1932 al abrirse una gran arteria. Advertencia: el MAEC cita Bobo como una de las dos ciudades donde se puede permanecer, pero desaconseja llegar por carretera desde Uagadugú.",
        dog_note="Recinto religioso en uso: el perro no entra en la mezquita ni en su patio. Puede quedarse con un adulto en el aparcamiento.",
        visit={
            "why": "Es el mejor conjunto de arquitectura de barro del país y el contrapunto urbano al Sahel: más verde, más comerciante, más relajado.",
            "see": "Los contrafuertes y torreones de la gran mezquita, los callejones y los altares de Dioulassoba-Kibidwe, y la estación ferroviaria colonial de la línea Abiyan-Uagadugú.",
            "access": "Asfalto por la RN1. Guía local obligatorio de facto en Dioulassoba y propina esperada; entrada a la mezquita solo por el exterior para no musulmanes, TARIFAS POR CONFIRMAR. Aparcamiento para dos 4x4 en los hoteles del centro. Región de Guiriko (antes Hauts-Bassins). El pin marca la explanada delante de la gran mezquita.",
            "when": "Noviembre a febrero; a primera hora de la mañana la luz rasante sobre el adobe y menos calor.",
            "skip": "Si se llega por el eje Uagadugú-Bobo por carretera contra el criterio del MAEC, mejor no ir en absoluto.",
        },
        links=[
            {"label": "Bobo-Dioulasso (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bobo-Dioulasso"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
            {"label": "Consejos de viaje de Canadá · Burkina Faso", "url": "https://travel.gc.ca/destinations/burkina-faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bobo-Dioulasso_Mosque.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bobo-Dioulasso_Mosque.jpg",
                "credit": "Jurgen · CC BY 2.0",
                "caption": "La gran mezquita de adobe de Bobo-Diulasso.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Moschee_von_Bobo-Dioulasso.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Moschee_von_Bobo-Dioulasso.jpg",
                "credit": "qiv · CC BY-SA 2.0",
                "caption": "Los contrafuertes de la mezquita de Dioulassoba.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bobo-Dioulasso_TownHall2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bobo-Dioulasso_TownHall2.jpg",
                "credit": "Maarten van der Bent · CC BY-SA 2.0",
                "caption": "El ayuntamiento colonial de Bobo-Diulasso.",
            },
        ],
    ),
    dict(
        n=3, name="Banfora · cascadas de Karfiguéla y domos de Fabédougou", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=10.6979278, lon=-4.8179222,  # Google Maps: Karfiguela
        desc="A unos 12 km al noroeste de Banfora, el Comoé se despeña en una escalera de saltos entre plantaciones de caña: son LAS CASCADAS MÁS VISITADAS DEL PAÍS según la propia Wikipedia francesa. A 5 km, los domos de Fabédougou forman un laberinto de bloques calizo-areniscos erosionados en colmena, buenos para caminar al amanecer. Banfora (117.452 habitantes en 2019) es la sexta ciudad del país y la base lógica. Advertencia: la pista final hasta las cascadas es de tierra y se embarra en agosto y septiembre.",
        dog_note="Sitios abiertos sin fauna peligrosa; perro atado por las rocas mojadas y los cultivos de caña. No dejarlo suelto en las pozas.",
        visit={
            "why": "Es el paisaje más agradecido de Burkina Faso y el único tramo donde el agua manda: cascadas, cañaverales y domos en 15 km.",
            "see": "Los saltos escalonados del Comoé en Karfiguéla y, a un cuarto de hora en coche, los domos de Fabédougou (10.74482, -4.80186).",
            "access": "Desde Banfora, asfalto y después pista de tierra practicable con 4x4; aparcamiento informal junto al puesto de guías, sobra sitio para dos vehículos. Se cobra entrada y guía en el acceso, IMPORTE POR CONFIRMAR (no hay tarifa oficial publicada). Región de Tannounyan (antes Cascades). El pin marca el aparcamiento y el puesto de guías al pie de las cascadas.",
            "when": "De octubre a diciembre: caudal alto y pista ya seca. En marzo-abril el salto se queda en un hilo.",
            "skip": "Descartar en plena estación de lluvias (julio-septiembre), cuando la pista final se hace intransitable.",
        },
        links=[
            {"label": "Cascades de Karfiguéla (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Cascades_de_Karfigu%C3%A9la"},
            {"label": "Banfora (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Banfora"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cascades_de_karfiguela_%C3%A0_Banfora.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cascades_de_karfiguela_%C3%A0_Banfora.jpg",
                "credit": "Masséni Héma · CC BY-SA 4.0",
                "caption": "Las cascadas de Karfiguéla.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Waterfalls_at_Karfiguela,_Burkina_Faso.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Waterfalls_at_Karfiguela,_Burkina_Faso.jpg",
                "credit": "c.hug · CC BY-SA 2.0",
                "caption": "Los saltos de Karfiguéla en estación seca.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cascades_de_Karfiguela_(12568284134).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cascades_de_Karfiguela_(12568284134).jpg",
                "credit": "Maarten van der Bent · CC BY-SA 2.0",
                "caption": "El río sobre la roca de Karfiguéla.",
            },
        ],
    ),
    dict(
        n=4, name="Lago Tengréla · hipopótamos y piraguas", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="medio día",
        lat=10.639689, lon=-4.808578,  # Google Maps: Lago Tengrela
        desc="Laguna somera de 7 km por 1 km y 580 hectáreas al oeste de Banfora, PROTEGIDA POR EL CONVENIO RAMSAR. Su emisario se junta con el Comoé unos 3 km al sureste. Los piragueros del pueblo llevan al visitante a buscar la familia de hipopótamos entre los nenúfares, y desde los años dos mil el campamento de Kegnigohi ofrece alojamiento y alquiler de vehículos. Advertencia: los hipopótamos son el animal que más gente mata en África; hay que obedecer al piraguero y no forzar la distancia para una foto.",
        dog_note="Hay hipopótamos y cocodrilos en la orilla; el perro no sube a la piragua y no debe quedarse suelto junto al agua.",
        visit={
            "why": "Es la forma más sencilla y barata de ver hipopótamos salvajes en Burkina Faso, a media hora de Banfora.",
            "see": "Piraguas de balancin entre nenúfares, hipopótamos a distancia prudente, pescadores y aves acuáticas.",
            "access": "Pista de tierra corta desde Banfora, practicable con cualquier 4x4; se aparca junto al embarcadero del pueblo, espacio justo pero suficiente para dos coches. Piragua y guía se pagan en el embarcadero, PRECIO POR CONFIRMAR. Región de Tannounyan (antes Cascades). El pin marca el embarcadero de piraguas, no el centro del lago.",
            "when": "Amanecer o última hora de la tarde, cuando los hipopótamos estan activos; de noviembre a febrero.",
            "skip": "Saltarselo si ya se ha visto fauna acuática mejor en otro país o si el nivel del agua está muy bajo en abril-mayo.",
        },
        links=[
            {"label": "Lac de Tengréla (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Lac_de_Tengr%C3%A9la"},
            {"label": "Banfora (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Banfora"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lac_de_Tengrela_vu_sud.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lac_de_Tengrela_vu_sud.jpg",
                "credit": "Tidjanehema · CC BY-SA 4.0",
                "caption": "El lago Tengréla desde el sur.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lac_de_Tengrela_vu_sud-ouest.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lac_de_Tengrela_vu_sud-ouest.jpg",
                "credit": "Tidjanehema · CC BY-SA 4.0",
                "caption": "El lago Tengréla, donde se ven los hipopótamos.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lac_de_Tengrela_vu_du_lac_vers_les_si%C3%A8ges_pour_visiteurs.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lac_de_Tengrela_vu_du_lac_vers_les_si%C3%A8ges_pour_visiteurs.jpg",
                "credit": "Tidjanehema · CC BY-SA 4.0",
                "caption": "El embarcadero del lago Tengréla.",
            },
        ],
    ),
    dict(
        n=5, name="Picos de Sindou · agujas de arenisca del país senufo", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=10.656944, lon=-5.1525,  # Google Maps: Pics de Sindou
        desc="Cadena de agujas de arenisca erosionada unos cientos de metros al este de Sindou, a 40 km al oeste de Banfora. Alcanzan los 415 m y son, según la Wikipedia francesa, EL SEGUNDO PUNTO MÁS ALTO DEL PAÍS. Para los senufo son un lugar místico y una protección frente al peligro, y la diversidad de habitats ha llevado a protegerlos como reserva natural. Hay senderos balizados, miradores y aparcamiento accesible por la ruta regional 21. Advertencia: la roca quema al mediodía y no hay sombra ni agua en el recorrido.",
        dog_note="Se camina por roca desnuda y cornisas: perro atado, con agua, y fuera de los puntos considerados sagrados por los senufo.",
        visit={
            "why": "Es el paisaje más fotogénico de Burkina Faso y la única caminata de verdad del suroeste, con desnivel corto y vistas largas.",
            "see": "Un cortado de agujas y torres de arenisca sobre la llanura senufo, con miradores escalonados y aldeas de cultivo al pie.",
            "access": "Asfalto hasta Sindou desde Banfora y acceso por la ruta regional 21, al sureste del pueblo, con aparcamiento junto a la entrada: cabe de sobra para dos 4x4. Guía local habitual y entrada módica, IMPORTES POR CONFIRMAR. Región de Tannounyan (antes Cascades), provincia de Léraba. El pin marca el aparcamiento y la entrada a los senderos.",
            "when": "Primera hora de la mañana o última de la tarde, de noviembre a febrero; la luz de tarde saca el color de la arenisca.",
            "skip": "Evitarlo en pleno mediodía de marzo-mayo (más de 40 grados sobre roca) o si la seguridad en la franja fronteriza con Malí se degrada.",
        },
        links=[
            {"label": "Pics de Sindou (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Pics_de_Sindou"},
            {"label": "Sindou (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Sindou"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/PicsdeSindou.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:PicsdeSindou.jpg",
                "credit": "croucrou / Sylvain · CC BY-SA 3.0",
                "caption": "Las agujas de arenisca de Sindou.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Aerial_view_Pics_de_Sindou,_Burkina_Faso.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Aerial_view_Pics_de_Sindou,_Burkina_Faso.jpg",
                "credit": "Rwhaun · CC BY-SA 4.0",
                "caption": "Los picos de Sindou desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pic_de_sindou.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pic_de_sindou.JPG",
                "credit": "Wegmann · CC BY-SA 3.0",
                "caption": "Los domos de Fabédougou, cerca de Banfora.",
            },
        ],
    ),
    dict(
        n=6, name="Ruinas de Loropéni · fortaleza de piedra del oro (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=10.2927366, lon=-3.5319407,  # Google Maps: Loropéni
        desc="Primer bien burkines inscrito en la Lista del Patrimonio Mundial, en 2009. Son murallas de piedra seca DE HASTA SEIS METROS DE ALTURA que cercan un asentamiento abandonado: la mejor conservada de las diez fortalezas del país lobi y parte de una red de un centenar de recintos ligados al comercio transahariano del oro. Datan al menos del siglo XI y tuvieron su apogeo entre los siglos XIV y XVII. Advertencia: el bien protegido apenas supera 1,1 hectáreas; se ve en una hora y no hay centro de visitantes en condiciones.",
        dog_note="Recinto arqueológico protegido y con guardas; lo habitual es dejar al perro fuera, en el vehículo a la sombra.",
        visit={
            "why": "Es el único monumento monumental en piedra de Burkina Faso y la puerta a la historia del oro lobi. Sin ella la ficha del país queda coja.",
            "see": "Un cuadrilátero de muros de laterita de hasta 6 m, con vanos y compartimentos interiores, comido por la vegetación.",
            "access": "Loropéni está a unos 40 km al oeste de Gaoua, con asfalto hasta el pueblo y pista corta al recinto. Aparcamiento de tierra junto a la caseta de guardas, suficiente para dos 4x4. Guarda-guía y entrada módica, TARIFAS Y HORARIOS POR CONFIRMAR. Región de Djôrô (antes Sud-Ouest). El pin marca la entrada y la caseta de guardas, no el centro del recinto.",
            "when": "Manana temprano, de noviembre a febrero; con la hierba alta de la estación humeda los muros casi no se ven.",
            "skip": "Si se viaja con poco margen y la prioridad es Banfora, se puede sacrificar: son 250 km de desvío desde el eje principal.",
        },
        links=[
            {"label": "Ruins of Loropéni · UNESCO", "url": "https://whc.unesco.org/en/list/1225"},
            {"label": "Loropéni (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Loropeni"},
            {"label": "Ruines de Loropéni (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Ruines_de_Lorop%C3%A9ni"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/2016.05-441-131ap_wall_Lorop%C3%A9ni_Ruins_nr.Lorop%C3%A9ni(Poni_Prv.),BF_sun15may2016-1106h.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:2016.05-441-131ap_wall_Lorop%C3%A9ni_Ruins_nr.Lorop%C3%A9ni(Poni_Prv.),BF_sun15may2016-1106h.jpg",
                "credit": "Rik Schuiling / TropCrop-TCS · CC BY-SA 4.0",
                "caption": "Las murallas de las ruinas de Loropéni.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/2016.05-441-134ap_archeology,excavation_Lorop%C3%A9ni_Ruins_nr.Lorop%C3%A9ni(Poni_Prv.),BF_sun15may2016-1119h.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:2016.05-441-134ap_archeology,excavation_Lorop%C3%A9ni_Ruins_nr.Lorop%C3%A9ni(Poni_Prv.),BF_sun15may2016-1119h.jpg",
                "credit": "Rik Schuiling / TropCrop-TCS · CC BY-SA 4.0",
                "caption": "Excavaciones arqueológicas en Loropéni.",
            },
        ],
    ),
    dict(
        n=7, name="Tiébélé · cour royale kassena de casas pintadas (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="medio día",
        lat=11.0966798, lon=-0.9649688,  # Google Maps: Tiébélé
        desc="Conjunto de arquitectura de tierra del siglo XVI, a 172 km al sur de Uagadugú y a unos 15 km de la frontera con Ghana, INSCRITO EN LA LISTA DEL PATRIMONIO MUNDIAL EN 2024 por el criterio (iii). Los hombres de la corte levantan las casas y las mujeres las decoran con motivos simbólicos: casas en ocho para las madres y los mayores, cuadrangulares para los recien casados y circulares para los solteros. El bien protegido mide 1,84 hectáreas. Advertencia: es una residencia real en uso, no un museo; se entra solo con permiso y guía de la corte.",
        dog_note="Recinto habitado, con altares y tumbas ancestrales dentro del patio: el perro no entra. Dejarlo en el vehículo, a la sombra.",
        visit={
            "why": "Es el bien cultural más reciente y más vivo del país: arquitectura de barro decorada que se sigue repintando cada año.",
            "see": "Fachadas pintadas en blanco, negro y ocre con geometrías kassena, el patio ceremonial, las tumbas de los ancestros y los distintos tipos de casa según el estatus.",
            "access": "Asfalto desde Pô y pista corta hasta el pueblo; aparcamiento de tierra junto a la entrada del recinto, holgado para dos 4x4. Se paga entrada y guía obligatorio en la corte, IMPORTES Y HORARIOS POR CONFIRMAR. Prohibido fotografiar sin permiso. Región de Nazinon (antes Centre-Sud), provincia de Nahouri. El pin marca la entrada de la cour royale.",
            "when": "Entre noviembre y febrero, después de que las mujeres repinten las fachadas al final de la estación humeda.",
            "skip": "Descartar si la frontera con Ghana o el eje Pô-Tiébélé estan cerrados por operaciones militares.",
        },
        links=[
            {"label": "La Cour royale de Tiébélé · UNESCO", "url": "https://whc.unesco.org/en/list/1713/"},
            {"label": "Tiébélé (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ti%C3%A9b%C3%A9l%C3%A9"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tiebele_village_in_Burkina_Faso_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tiebele_village_in_Burkina_Faso_02.jpg",
                "credit": "Alexander Leisser · CC BY-SA 4.0",
                "caption": "Las casas pintadas kassena de Tiébélé.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tiebele_village_in_Burkina_Faso_07.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tiebele_village_in_Burkina_Faso_07.jpg",
                "credit": "Alexander Leisser · CC BY-SA 4.0",
                "caption": "Decoración geométrica de una fachada.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tiebele_village_in_burkina_faso.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tiebele_village_in_burkina_faso.jpg",
                "credit": "Alexander Leisser · CC BY-SA 4.0",
                "caption": "La corte real de Tiébélé.",
            },
        ],
    ),
    dict(
        n=8, name="Sitios de metalurgia antigua del hierro · Tiwêga, Yamané, Kindibo y Békuy (UNESCO)", cat="Patrimonio UNESCO", prio="Media",
        dog="no recomendado", time="medio día",
        lat=13.0881208, lon=-1.1063164,  # Google Maps: Tiwèga (mezquita del pueblo; el sitio metalúrgico no figura)
        desc="Bien en serie inscrito en 2019 con cinco componentes: Douroula, Tiwêga, Yamané, Kindibo y Békuy. Reune alrededor de quince hornos en pie repartidos por varias provincias y documenta MÁS DE 2.700 AÑOS DE PRODUCCIÓN DE HIERRO: Douroula, del siglo VIII antes de Cristo, es la prueba más antigua de metalurgia del hierro del país. En Yamané y Kindibo los hornos conviven con comunidades de herreros todavía activas. Advertencia: los cinco componentes estan muy dispersos y varios caen en provincias que el MAEC califica de riesgo extremo.",
        dog_note="Recintos arqueológicos con hornos fragiles y aldeas de herreros en activo; el perro estorba y puede danar estructuras.",
        visit={
            "why": "Es el único bien mundial del país que explica de verdad la economía precolonial mossi: hierro, no oro ni barro.",
            "see": "Hornos de reducción troncocónicos en pie, escoriales, pozos de extracción y, en Yamané y Kindibo, herreros trabajando.",
            "access": "Tiwêga está cerca de Kaya (región de Kuilsé); Békuy queda en la reserva forestal de Maro, región de Guiriko (11.63333, -3.88333); Douroula está en Bankui (antes Boucle du Mouhoun). Pistas de tierra y guía local imprescindible. COORDENADAS DE YAMANE Y KINDIBO POR CONFIRMAR: no aparecen en GeoNames. Sin aparcamiento formal; se deja el coche a la entrada de la aldea. El pin marca el sitio metalurgico de Tiwêga.",
            "when": "Estacion seca, de noviembre a febrero; con lluvia las pistas de acceso a las aldeas se cortan.",
            "skip": "Descartar Tiwêga y Douroula mientras persista la presion yihadista en el Centro-Norte y el Mouhoun; Békuy, al suroeste, es el componente más plausible.",
        },
        links=[
            {"label": "Ancient Ferrous Metallurgy Sites of Burkina Faso · UNESCO", "url": "https://whc.unesco.org/en/list/1602"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/A_Makera_(Blacksmith)_cultural_performance._By_Sani_Maikatanga.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:A_Makera_(Blacksmith)_cultural_performance._By_Sani_Maikatanga.jpg",
                "credit": "Sani Maikatanga · CC BY-SA 4.0",
                "caption": "Herrería tradicional en África occidental (imagen de contexto: los hornos de Tiwêga y Békuy no tienen fotografía en Commons).",
            },
        ],
    ),
    dict(
        n=9, name="Ranch de Nazinga · los elefantes del sur", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1-2 noches",
        lat=11.0491892, lon=-1.4184939,  # Google Maps: Nazinga
        desc="Rancho de caza y conservación creado en 1979 por los hermanos Robert y Clark Lungren, en el sur del país junto a la frontera con Ghana. Es EL SITIO MÁS FIABLE DE AFRICA OCCIDENTAL PARA VER ELEFANTES A CORTA DISTANCIA, porque en la estación seca se concentran en las represas artificiales excavadas por el propio proyecto. Hay campamento dentro del recinto y circuitos con guarda. Advertencia: los elefantes de Nazinga estan habituados pero no son mansos; hay conflictos documentados con los cultivos vecinos.",
        dog_note="Área protegida con elefantes, leones y hienas: el perro no entra ni en vehículo. Habria que dejarlo en Pô o en Uagadugú.",
        visit={
            "why": "Es la única fauna grande accesible del país sin entrar en la zona de guerra del este: elefantes, antílopes y primates en un día.",
            "see": "Manadas de elefantes en las represas al atardecer, antílopes ruanos, cobos, facoceros, babuinos y más de trescientas especies de aves.",
            "access": "Desde Uagadugú por la RN5 hasta Pô y después pista de tierra hasta la puerta del ranch; 4x4 recomendable y guarda obligatorio para los circuitos interiores. Aparcamiento amplio en el campamento. TARIFAS, HORARIOS Y ESTADO DE APERTURA POR CONFIRMAR: no hemos localizado página oficial operativa. Región de Nazinon (antes Centre-Sud). El pin marca la entrada principal del ranch.",
            "when": "Marzo y abril, final de la estación seca, cuando los elefantes dependen de las represas; salidas al amanecer y al atardecer.",
            "skip": "Descartar si el ranch está cerrado por seguridad o si no se puede dejar al perro atendido fuera.",
        },
        links=[
            {"label": "Nazinga Game Ranch (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Nazinga_Game_Ranch"},
            {"label": "GeoNames · Foret Classee de Nazinga", "url": "https://www.geonames.org/search.html?q=Nazinga&country=BF"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Elephants_Nazinga_MS5175.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Elephants_Nazinga_MS5175.JPG",
                "credit": "Marco Schmidt · CC BY-SA 3.0",
                "caption": "Elefantes en el rancho de Nazinga.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Elephant_eating_Shea_MS5162.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Elephant_eating_Shea_MS5162.JPG",
                "credit": "Marco Schmidt · CC BY-SA 3.0",
                "caption": "Elefante comiendo karité en Nazinga.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Coton_-_route_pour_Nazinga_-_Burkina_Faso.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Coton_-_route_pour_Nazinga_-_Burkina_Faso.jpg",
                "credit": "Stefyguida · CC BY-SA 4.0",
                "caption": "Campos de algodón en la carretera de Nazinga.",
            },
        ],
    ),
    dict(
        n=10, name="Parque nacional de Arly · complejo W-Arly-Pendjari (UNESCO)", cat="Patrimonio UNESCO", prio="Media",
        dog="prohibido", time="1-2 noches",
        lat=11.6129173, lon=1.2891036,  # Google Maps: Parque Nacional de Arli
        desc="Parque de 760 km2 en la provincia de Tapoa, parte burkinesa del complejo transfronterizo W-Arly-Pendjari, inscrito en 1996 y ampliado en 2017 a Benín y Burkina Faso. El conjunto suma 1.714.831 hectáreas y concentra EL 85 POR CIENTO DE LOS ELEFANTES DE SABANA DE AFRICA OCCIDENTAL, la única población viable de leones de la región y probablemente el último guepardo occidental. Advertencia: el este de Burkina Faso es el frente más activo de la insurgencia; el MAEC cita Diapaga y Kompienga como zonas de riesgo extremo. HOY ES INVIABLE.",
        dog_note="Parque nacional con leones y elefantes; prohibido por reglamento y suicida en la práctica.",
        visit={
            "why": "Sobre el papel es el mejor parque de África occidental; se documenta para tenerlo listo si algún día vuelve a abrir.",
            "see": "Unos doscientos elefantes, doscientos hipopótamos y un centenar de leones según la Wikipedia inglesa, además de bufalos, antílopes ruanos y cobos.",
            "access": "Desde Fada N'Gourma por la RN18 hacia Diapaga y después pista; en tiempos hubo pista de aterrizaje en Arly. El parque está gestionado por la ONG burkinesa NATURAMA desde 1993. ESTADO DE APERTURA POR CONFIRMAR: se dan por cerradas o inaccesibles las zonas del este desde 2018-2019. Región de Tapoa (antes Est). El pin marca la entrada del parque.",
            "when": "Sobre el papel, de febrero a mayo. En la práctica, no hay temporada: la zona está vetada.",
            "skip": "DESCARTAR SIEMPRE mientras el MAEC mantenga Diapaga y Gourma como riesgo extremo; no es una parada, es una ficha de archivo.",
        },
        links=[
            {"label": "W-Arly-Pendjari Complex · UNESCO", "url": "https://whc.unesco.org/en/list/749"},
            {"label": "Arly National Park (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Arly_National_Park"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Arli-NP_MS1219.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Arli-NP_MS1219.jpg",
                "credit": "Marco Schmidt · CC BY-SA 3.0",
                "caption": "El río Arli, en el parque nacional.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pendjari.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pendjari.JPG",
                "credit": "Martin Wegmann · CC BY-SA 3.0",
                "caption": "La sabana arbolada del complejo W-Arly-Pendjari.",
            },
        ],
    ),
    dict(
        n=11, name="Laongo · esculturas en granito al aire libre", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=12.512755, lon=-1.2761823,  # Google Maps: Escuela de Laongo (junto al sitio de esculturas)
        desc="Museo al aire libre a 35 km al este de Uagadugú, cerca de Ziniaré, donde los afloramientos de granito gris rosado sirven de soporte y de materia a las obras. El PRIMER SIMPOSIO INTERNACIONAL SE CELEBRO EN 1988 con dieciocho escultores de trece países de África, Asia, Europa y América; después hubo ediciones en 1989, 1991, 1996, 1998, 2001 y 2003, y han intervenido unos sesenta artistas. Abre todos los días de 8 a 18 h (7 a 18 h los fines de semana) y la entrada cuesta 2.500 FCFA por persona.",
        dog_note="Recinto al aire libre sin fauna peligrosa; perro atado y lejos de las obras. Conviene avisar en recepcion.",
        visit={
            "why": "Es la excursion de medio día más fácil desde Uagadugú y el único arte contemporaneo visitable del país.",
            "see": "Unas decenas de esculturas talladas directamente sobre domos y bolos de granito, repartidas por un circuito señalizado.",
            "access": "Asfalto por la RN4 hasta Ziniaré y desvío corto; aparcamiento junto a la recepcion, amplio para dos 4x4. Abierto a diario de 8 a 18 h y de 7 a 18 h los fines de semana; entrada 2.500 FCFA; guía disponible y libro-guía en recepcion (datos de la Oficina Nacional de Turismo). Región de Oubri (antes Plateau-Central). El pin marca la recepcion del sitio.",
            "when": "Primera hora de la mañana, de noviembre a febrero; la sombra escasea y el granito acumula calor.",
            "skip": "Saltarselo si el tiempo en Uagadugú es escaso: es agradable pero no imprescindible.",
        },
        links=[
            {"label": "Sculpture sur granit de Laongo · Oficina Nacional de Turismo (ONTB)", "url": "https://www.ontb.bf/visites/sites-touristiques/sculpture-sur-granit-de-laongo"},
            {"label": "GeoNames · Laongo", "url": "https://www.geonames.org/search.html?q=Laongo&country=BF"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sculpture_sur_granite_%C3%A0_Laongo_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sculpture_sur_granite_%C3%A0_Laongo_01.jpg",
                "credit": "Fasouagadougou · CC BY-SA 4.0",
                "caption": "Escultura en granito en Laongo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sculpture_sur_granite_%C3%A0_Laongo_03.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sculpture_sur_granite_%C3%A0_Laongo_03.jpg",
                "credit": "Fasouagadougou · CC BY-SA 4.0",
                "caption": "Otra obra del simposio de Laongo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/SYMPATHIE_A_LAONGO_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:SYMPATHIE_A_LAONGO_01.jpg",
                "credit": "CelitoArtwork · CC BY-SA 4.0",
                "caption": "«Sympathie», en el sitio de Laongo.",
            },
        ],
    ),
    dict(
        n=12, name="Bazoulé · el lago de los cocodrilos sagrados", cat="Cultura", prio="Media",
        dog="prohibido", time="medio día",
        lat=12.319599, lon=-1.7088793,  # Google Maps: Bazoulé
        desc="Aldea a unos 30 km de Uagadugú donde los cocodrilos son tótem y conviven con la gente. La tradición local cuenta que CAYERON DEL CIELO CON LA LLUVIA HACE 570 AÑOS, cuando el pueblo se moria de sed. Cada año la fiesta de Kom-Lakré congrega ofrendas de aves para pedir salud y protección. Se llega por la RN1 en dirección a Bobo-Diulasso y se gira a la derecha por una pista señalizada pasado Tanghin-Dassouri. Advertencia: son animales salvajes; la escena de tocarlos es una atraccion pagada, no una garantia.",
        dog_note="Cocodrilos del Nilo sueltos en la orilla y gallinas de cebo: llevar al perro sería ponerlo delante del depredador.",
        visit={
            "why": "Es la parada cultural más rapida desde Uagadugú y una lectura directa de la relacion mossi con los totems.",
            "see": "Una charca con decenas de cocodrilos del Nilo, el guía cebándolos con una gallina y el campamento de la aldea.",
            "access": "RN1 hacia Bobo y desvío a la derecha por pista señalizada después de Tanghin-Dassouri; pista corta y llana, sin problema para dos 4x4. Hay campamento y guías en el pueblo (teléfonos publicados por la Oficina Nacional de Turismo). TARIFAS Y HORARIOS POR CONFIRMAR en esta ficha oficial. Región de Kadiogo. El pin marca la charca y el punto de acogida de los guías.",
            "when": "Mediodia de estación seca, cuando los cocodrilos salen a tomar el sol a la orilla.",
            "skip": "Si ya se visita Sabou, con esta basta una de las dos: la escena es prácticamente la misma.",
        },
        links=[
            {"label": "Mare aux crocodiles sacres de Bazoulé · ONTB", "url": "https://www.ontb.bf/visites/sites-touristiques/mare-aux-crocodiles-sacres-de-bazoule"},
            {"label": "GeoNames · Bazoulé", "url": "https://www.geonames.org/search.html?q=Bazoule&country=BF"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bazoule_sacred_crocodiles_MS_6709cropped.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bazoule_sacred_crocodiles_MS_6709cropped.JPG",
                "credit": "Marco Schmidt · CC BY-SA 3.0",
                "caption": "Los cocodrilos sagrados de Bazoulé.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bazoule_sacred_crocodiles_MS_6703.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bazoule_sacred_crocodiles_MS_6703.JPG",
                "credit": "Marco Schmidt · CC BY-SA 3.0",
                "caption": "El lago de Bazoulé.",
            },
        ],
    ),
    dict(
        n=13, name="Sabou · cocodrilos místicos y aldea", cat="Cultura", prio="Media",
        dog="prohibido", time="medio día",
        lat=12.0601301, lon=-2.2261265,  # Google Maps: Sabou
        desc="Pueblo de 15.060 habitantes sobre la RN1, a mitad de camino entre Uagadugú y Koudougou. En la charca del norte viven MÁS DE CIEN COCODRILOS SAGRADOS que, según la tradición, son las almás de los descendientes de la familia Kaboré: un antepasado sediento habria sido salvado por un cocodrilo que le dio de beber. Hay guías de día, guardas de noche, alojamiento y comida en el propio sitio. Tarifas oficiales: 1.500 FCFA por persona en grupos de menos de cinco, hasta 500 FCFA a partir de veinte visitantes.",
        dog_note="Más de cien cocodrilos sueltos junto a la charca; el perro no debe bajar del coche.",
        visit={
            "why": "Es la parada natural en la RN1 camino de Koudougou y Bobo, y la version más organizada del rito de los cocodrilos.",
            "see": "La charca del norte del pueblo con más de cien cocodrilos, el cebo con gallina y la aldea de la familia Kaboré.",
            "access": "Sobre la RN1 asfaltada, en la provincia de Boulkiemdé; aparcamiento de tierra junto a la charca, holgado para dos 4x4. Entrada de 1.500 FCFA (menos de 5 personas), 1.000 (5-10), 750 (11-20) y 500 (más de 20); alojamiento 3.300 FCFA individual y 3.600 doble, según la Oficina Nacional de Turismo. Región de Nando (antes Centre-Ouest). El pin marca la charca y la recepcion.",
            "when": "Mediodia, con los cocodrilos fuera del agua; estación seca de noviembre a marzo.",
            "skip": "Descartar si ya se ha parado en Bazoulé: el contenido se repite.",
        },
        links=[
            {"label": "Mares aux crocodiles sacres de Sabou · ONTB", "url": "https://www.ontb.bf/visites/sites-touristiques/mares-aux-crocodiles-sacres-de-sabou"},
            {"label": "Sabou (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Sabou"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Crocodile_de_Sabou.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Crocodile_de_Sabou.jpg",
                "credit": "Jacoma226 · CC0",
                "caption": "Alimentando a un cocodrilo en Sabou.",
            },
        ],
    ),
    dict(
        n=14, name="Cascadas de Tagbaladougou y valle del Comoé", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=10.78333, lon=-4.7,  # Google Maps: (sin objeto en Google Maps; coordenada de la fuente)
        desc="Saltos secundarios del valle del Comoé, entre Banfora y Bobo-Diulasso, mucho menos frecuentados que Karfiguéla. Son la alternativa cuando el aparcamiento de Karfiguéla está lleno de autocares y sirven además para entender el corredor del Comoé, EL RIO QUE ORGANIZA TODO EL SUROESTE y que luego atraviesa Costa de Marfil hasta el golfo de Guinea. Advertencia: la información publicada es escasa; GeoNames sitúa Tagbaladougou en la región de Hauts-Bassins (Guiriko) y no en Cascades, POR CONFIRMAR sobre el terreno.",
        dog_note="Sitio abierto sin fauna peligrosa conocida; perro atado por las rocas resbaladizas y los campos de caña.",
        visit={
            "why": "Es el plan B de Karfiguéla y una parada de río tranquila entre Bobo y Banfora, sin apenas visitantes.",
            "see": "Una sucesion de pozas y saltos bajos sobre roca, cañaverales y huertas de ribera.",
            "access": "Desvio desde la RN7 Bobo-Banfora y pista de tierra corta; sin aparcamiento formal, se deja el coche a la entrada del pueblo. ENTRADA, GUIA Y HORARIO POR CONFIRMAR: no hemos encontrado fuente oficial. Región POR CONFIRMAR entre Guiriko y Tannounyan. El pin marca el acceso al pueblo de Tagbaladougou, desde donde parte el sendero a las pozas.",
            "when": "Octubre a diciembre, con caudal y pistas ya firmes.",
            "skip": "Si el tiempo aprieta, es el primero de la lista del suroeste que se puede sacrificar.",
        },
        links=[
            {"label": "GeoNames · Tagbaladougou", "url": "https://www.geonames.org/search.html?q=Tagbaladougou&country=BF"},
            {"label": "Cascades de Karfiguéla (Wikipedia FR, contexto del Comoé)", "url": "https://fr.wikipedia.org/wiki/Cascades_de_Karfigu%C3%A9la"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Falls_near_Banfora_26.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Falls_near_Banfora_26.jpg",
                "credit": "Syced · CC0",
                "caption": "Saltos del Comoé cerca de Banfora.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Map_Comoe-Leraba_MS_4512.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Map_Comoe-Leraba_MS_4512.jpg",
                "credit": "Marco Schmidt · CC BY-SA 3.0",
                "caption": "Mapa pintado a mano de la reserva de Comoé-Léraba.",
            },
        ],
    ),
    dict(
        n=15, name="Koudougou · la tercera ciudad y el tejido burkines", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=12.2562183, lon=-2.3517526,  # Google Maps: Koudougou
        desc="TERCERA CIUDAD DE BURKINA FASO tras Uagadugú y Bobo-Diulasso, con 160.239 habitantes en el censo de 2019. Su economía gira en torno al algodon y a varias fábricas textiles, y en la ciudad funciona desde hace años un taller de reciclaje y confeccion de ropa. Es la parada natural en la RN1 entre Uagadugú y Bobo y una base razonable para dormir con dos vehículos. Advertencia: el MAEC desaconseja precisamente ese trayecto por carretera, de modo que está parada solo tiene sentido si ya se ha asumido el eje terrestre.",
        dog_note="Ciudad y talleres textiles: el perro puede acompañar atado por la calle, pero no entra en los mercados cubiertos.",
        visit={
            "why": "Es la mejor ciudad media para reponer, dormir y ver tejido burkines sin la escala de Uagadugú.",
            "see": "El gran mercado, los talleres de algodon teñido y tejido a mano y la arquitectura colonial de la estación.",
            "access": "Asfalto por la RN1 desde Uagadugú y enlace hacia Dédougou; aparcamiento en hoteles del centro, suficiente para dos 4x4. HORARIOS Y PRECIOS DE TALLERES POR CONFIRMAR. Región de Nando (antes Centre-Ouest), provincia de Boulkiemdé. El pin marca el gran mercado, punto de referencia del centro.",
            "when": "Día de mercado, de mañana; estación seca de noviembre a febrero.",
            "skip": "Prescindible si se va justo de días: Bobo cubre lo mismo con más interes.",
        },
        links=[
            {"label": "Koudougou (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Koudougou"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Koudougou_-_Burkina_Faso.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Koudougou_-_Burkina_Faso.jpg",
                "credit": "Stefyguida · CC BY-SA 4.0",
                "caption": "El mercado de Koudougou.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Koudougou-TrainStation.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Koudougou-TrainStation.JPG",
                "credit": "Autor desconocido · CC BY-SA 3.0",
                "caption": "La estación de ferrocarril de Koudougou.",
            },
        ],
    ),
    dict(
        n=16, name="Uahiguya y el Yatenga · reino mossi del norte", cat="Cultura", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=13.5668258, lon=-2.4109908,  # Google Maps: Ouahigouya
        desc="Capital del Yatenga, uno de los reinos mossi, FUNDADA EN 1757; su nombre significa «venid a postraros». Tiene 124.587 habitantes según el censo de 2019 y conserva la tumba del Naaba Kango, el recinto del Yatenga Naaba y un lago artificial. Es la puerta histórica del norte mossi y la última ciudad grande antes del Sahel. Advertencia: el MAEC cita Yatenga, Lorum y Titao entre las provincias de RIESGO EXTREMO y pide no pasar al norte del eje Uahiguya-Bogandé: en 2027 esto es una ficha documental, no una etapa.",
        dog_note="Recintos reales y tumbas con normas propias; además la zona es de riesgo extremo y no conviene llamar la atención.",
        visit={
            "why": "Es la única corte mossi del norte visitable sobre el papel y explica el equilibrio entre Uagadugú y el Yatenga.",
            "see": "La tumba del Naaba Kango, el recinto del Yatenga Naaba y el lago artificial de la ciudad.",
            "access": "Asfalto por la RN2 desde Uagadugú (unos 180 km). SIN CONDICIONES DE ACCESO FIABLES: el MAEC pide no pasar al norte del eje Uahiguya-Bogandé y la región ha sufrido ataques y desplazamientos masivos. Región de Yaadga (antes Nord). El pin marca el recinto del Yatenga Naaba, en el centro de la ciudad.",
            "when": "Sobre el papel, estación seca. En la práctica, no hay ventana segura.",
            "skip": "DESCARTAR mientras el MAEC mantenga Yatenga y Titao como riesgo extremo (aviso del 19-05-2025).",
        },
        links=[
            {"label": "Ouahigouya (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ouahigouya"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
            {"label": "Consejos de viaje de Canadá · Burkina Faso", "url": "https://travel.gc.ca/destinations/burkina-faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ouahigouya_road.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ouahigouya_road.jpg",
                "credit": "Martin Wegmann · CC BY-SA 3.0",
                "caption": "La carretera de Ouahigouya hacia Mali.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ouahigouya_street-1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ouahigouya_street-1.jpg",
                "credit": "Fernando Hidalgo Marchione · CC BY-SA 2.0",
                "caption": "Una calle de Ouahigouya, capital del Yatenga.",
            },
        ],
    ),
    dict(
        n=17, name="Gorom-Gorom · mercado del Sahel y dunas de Oursi", cat="Cultura", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=14.4443987, lon=-0.2357065,  # Google Maps: Marché de Gorom-Gorom
        desc="Capital de la provincia de Oudalan, en pleno Sahel, con 9.752 habitantes en 2019 y UN MERCADO SEMANAL QUE LA WIKIPEDIA INGLESA DESCRIBE COMO EL MAYOR DE BURKINA FASO, punto de encuentro de fulbe, tuaregs, songhai y bella. A un centenar de kilómetros al oeste está la mare d'Oursi, con sus dunas y su yacimiento arqueológico. Advertencia: unos 20.000 desplazados internos viven en Gorom-Gorom y dependen de organizaciones como Médicos Sin Fronteras para tener agua y comida. La zona está vetada.",
        dog_note="Mercado abarrotado, calor extremo y zona militarizada; el perro sería un problema añadido.",
        visit={
            "why": "Sobre el papel es el mejor mercado saheliano de África occidental y el único contacto real con el mundo nómada del país.",
            "see": "El mercado semanal con ganado, sal y platería tuareg; a un centenar de kilómetros, las dunas y la charca de Oursi.",
            "access": "Pista y asfalto degradado desde Dori. SIN ACCESO VIABLE: la provincia de Oudalan está dentro de la región de Liptako, que el MAEC señala integra como riesgo extremo. COORDENADAS DE OURSI POR CONFIRMAR (no hemos podido abrir su ficha). Región de Liptako (antes Sahel). El pin marca la explanada del mercado.",
            "when": "Sobre el papel, día de mercado en estación fresca (diciembre-enero). En la práctica, no hay ventana.",
            "skip": "DESCARTAR SIEMPRE: el MAEC sitúa todas las provincias de Liptako en riesgo extremo (aviso del 19-05-2025).",
        },
        links=[
            {"label": "Gorom-Gorom (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Gorom-Gorom"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
            {"label": "Consejos de viaje de Canadá · Burkina Faso", "url": "https://travel.gc.ca/destinations/burkina-faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Marche_de_Gorom_Gorom001.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Marche_de_Gorom_Gorom001.jpg",
                "credit": "C. Hugues · CC BY-SA 2.0",
                "caption": "El mercado de Gorom-Gorom.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Dune_Oursi_MS0769.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Dune_Oursi_MS0769.jpg",
                "credit": "Marco Schmidt · CC BY-SA 2.5",
                "caption": "La duna de Oursi, en el Sahel burkinés.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Songhay_pottery_gorom_gorom_market.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Songhay_pottery_gorom_gorom_market.jpg",
                "credit": "C. Hugues · CC BY-SA 2.0",
                "caption": "Alfareras songhay en el mercado de Gorom-Gorom.",
            },
        ],
    ),
    dict(
        n=18, name="Fada N'Gourma y el este · la puerta de los parques", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=12.0601649, lon=0.3654204,  # Google Maps: Fada N'Gourma
        desc="Capital gourmantché sobre la RN4 entre Uagadugú y Niamey, con 73.200 habitantes en 2019. Fue capital de un Estado gurma que GUERREO REPETIDAMENTE CONTRA EL IMPERIO SONGHAI en los siglos XVI y XVII y sigue siendo la sede del rey de los gurma. Es la puerta logística de Arly y de la Pendjari beninesa. Advertencia: el este es el frente más activo de la insurgencia; en 2021 una unidad militar de protección de fauna fue emboscada a 15 km de su base en Natiaboni, cerca de la ciudad.",
        dog_note="Ciudad de paso hacia parques con grandes depredadores y zona de operaciones militares; el perro no aporta nada y complica todo.",
        visit={
            "why": "Es la única base con combustible y taller antes de los parques del este; sin ella no hay acceso a Arly.",
            "see": "El palacio del rey gurma, el mercado y el cruce de la RN4 hacia Níger y de la RN18 hacia Diapaga.",
            "access": "Asfalto por la RN4 desde Uagadugú (unos 220 km). SIN ACCESO VIABLE: el MAEC sitúa Gourma y Kompienga en riesgo extremo. Aparcamiento en hoteles del centro, suficiente para dos 4x4 si algún día se abre. Región de Goulmou (antes Est). El pin marca el palacio del Gourmantché Naba, referencia del centro.",
            "when": "Sobre el papel, estación seca. En la práctica, no hay ventana segura.",
            "skip": "DESCARTAR SIEMPRE mientras el MAEC mantenga Gourma, Kompienga y Diapaga como riesgo extremo (aviso del 19-05-2025).",
        },
        links=[
            {"label": "Fada N'gourma (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Fada_N%27gourma"},
            {"label": "Recomendaciones de viaje MAEC · Burkina Faso", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"},
            {"label": "Consejos de viaje de Canadá · Burkina Faso", "url": "https://travel.gc.ca/destinations/burkina-faso"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fada_N_Gourma_2.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fada_N_Gourma_2.JPG",
                "credit": "Martin Wegmann · CC BY-SA 3.0",
                "caption": "La calle principal de Fada N'Gourma.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Burkina_Faso_Gourma.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Burkina_Faso_Gourma.JPG",
                "credit": "Martin Wegmann · CC BY-SA 3.0",
                "caption": "La provincia del Gourma.",
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
    ("Aeropuerto Internacional Thomas Sankara de Uagadugú (OUA / DFFD)", "Frontera", 12.3549934, -1.513994,  # Google Maps: Aeropuerto de Uagadugú (Thomas Sankara)
     "Único acceso aéreo internacional real del país: concentra el 98 % del tráfico comercial y está a 1,5 km al sureste del centro de Uagadugú. Exige eVisa impreso, fiche de voyage y certificado de fiebre amarilla. Está prevista su sustitución por el nuevo aeropuerto de Donsin, 35 km al noreste. Pin comprobado en Google Maps («Aeropuerto de Uagadugú (Thomas Sankara)»)."),
    ("Paso fronterizo de Niangoloko (Costa de Marfil – Burkina Faso)", "Frontera", 10.2818967, -4.916759,  # Google Maps: Niangoloko
     "Paso con Costa de Marfil, lado marfileño Laleraba. Mercancías de 6.30 a 18.00, pasajeros 24/7, todos los días. A 131 km de Bobo-Dioulasso, unas 2 h 30. Gestiona la Direction Générale des Douanes, contacto Sr. HAMADO, 70 26 47 45. Zona de riesgo extremo para el MAEC. Pin comprobado en Google Maps («Niangoloko»)."),
    ("Paso fronterizo de Koloko – Hèrèmakono (Mali – Burkina Faso)", "Frontera", 11.0810345, -5.3123577,  # Google Maps: Koloko
     "Paso con Mali en el eje Bobo-Dioulasso – Sikasso. Mercancías de 6.00 a 18.00, pasajeros 24/7. A 132 km de Bobo-Dioulasso, 2 h 45 en turismo. La nacional N8 está asfaltada pero con muchos baches que obligan a reducir la velocidad. Pin comprobado en Google Maps («Koloko»)."),
    ("Paso fronterizo de Cinkansé (Togo – Burkina Faso)", "Frontera", 11.1179757, 0.0094472,  # Google Maps: Cinkansé
     "Poste de Contrôle Juxtaposé en el corredor hacia el puerto de Lomé. Mercancías de 6.30 a 18.00, pasajeros 24/7. A 105 km de Tenkodogo por la N16. N4 y N16 asfaltadas y en buen estado, con cinco puestos de control hasta Uagadugú. Pin comprobado en Google Maps («Cinkansé»)."),
    ("Paso fronterizo de Kantchari (Níger – Burkina Faso)", "Frontera", 12.4801981, 1.5152229,  # Google Maps: Kantchari
     "Paso con Níger, lado nigerino Torodi, a 152 km de Fada N'Gourma y 148 km del aeropuerto de Niamey. Abierto sobre el papel, pero el Logistics Cluster no evaluó la carretera por presencia de grupos terroristas y advierte de que el eje «es objeto cada vez más frecuente de ataques». Desaconsejado sin matices. Pin comprobado en Google Maps («Kantchari»)."),
    ("Paso fronterizo de Nadiagou – Porga (Benín – Burkina Faso)", "Frontera", 11.1584403, 0.8377957,  # Google Maps: Nadiagou
     "Paso con Benín en el eje hacia Natitingou. Mercancías de 6.30 a 18.00, pasajeros 24/7. A 20 km de Pama y 344 km de Uagadugú (7 h). Carretera no evaluada por inseguridad desde noviembre de 2021 y descrita como muy dañada. Jefe de puesto: Sr. SALOU, 70 32 40 14. Pin comprobado en Google Maps («Nadiagou»)."),
    ("Viceconsulado Honorario de España en Uagadugú", "Consular", 12.3679516, -1.5184418,  # Google Maps: Koulouba, Uagadugú (el viceconsulado no figura como objeto)
     "Sr. Ziad Azar. Avenue J.F. Kennedy, Kuluba, Uagadugú. Tel. (+226) 50 33 16 32. Correo CH.OUAGADOUGOU@maec.es. Es la única representación española sobre el terreno. ATENCIÓN: las coordenadas son las del centro de Uagadugú, no las del edificio; hay que verificarlas. Pin comprobado en Google Maps («Koulouba, Uagadugú (el viceconsulado no figura como objeto)»)."),
    ("Embajada de España en Mali y Burkina Faso (Bamako)", "Consular", 12.6277833, -8.0259599,  # Google Maps: Embajada de España en Bamako
     "ACI 2000, en face de l'École de Maintien de la Paix, BP E-3230, Bamako (Mali). Tel. (+223) 44 98 24 30. Emergencia consular 24 h (+223) 73 31 23 24. Correos emb.bamako@maec.es y emb.bamako.sc@maec.es. Es la embajada competente para Burkina Faso. Pin comprobado en Google Maps («Embajada de España en Bamako»)."),
    ("CHU Yalgado Ouédraogo, Uagadugú", "Hospital", 12.3835886, -1.5064573,  # Google Maps: CHU Yalgado Ouédraogo
     "Principal hospital universitario de referencia del país y mejor dotado de Burkina Faso. Para casos complejos se deriva a Abiyán, Accra o París. Pin comprobado en Google Maps («CHU Yalgado Ouédraogo»)."),
    ("CHU Sourou Sanou, Bobo-Dioulasso", "Hospital", 11.1700367, -4.301191,  # Google Maps: CHU Sourô Sanou (Bobo-Diulasso)
     "Hospital universitario de referencia del oeste: 593 camas y 1.115 empleados, con urgencias, cirugía, traumatología ortopédica, maternidad, hemodiálisis y resonancia magnética. Sede principal en el sector 8, barrio Sikasso-Cira. Pin comprobado en Google Maps («CHU Sourô Sanou (Bobo-Diulasso)»)."),
    ("Estaciones de servicio del eje central, Uagadugú", "Combustible", 12.3714277, -1.5196603,  # Google Maps: Uagadugú (sin gasolinera concreta como objeto)
     "Gasóleo a 675 XOF/litro (dato de 09-02-2026) y gasolina a 850 XOF/litro (dato de 12-01-2026), precios fijados por el Gobierno. Red fiable solo en Uagadugú, Bobo-Dioulasso y capitales regionales del eje central; fuera de ahí, bidones y riesgo de adulteración. Pin comprobado en Google Maps («Uagadugú (sin gasolinera concreta como objeto)»)."),
    ("Llenado de agua no potable, Uagadugú", "Agua potable", 12.3714277, -1.5196603,  # Google Maps: Uagadugú
     "Estaciones de servicio y hoteles del centro de Uagadugú como punto realista de llenado para ducha y lavado. Agua de red NO potable y brotes de cólera registrados: filtro más tratamiento obligatorio incluso para uso no alimentario. Punto concreto por confirmar, sin registros verificados de iOverlander. Pin comprobado en Google Maps («Uagadugú»)."),
]

DRONE_CALLOUT = ("danger", "El dron se queda en la aduana, y puede acabar en un juzgado",
                 "La ANAC exige que todo dron utilizado en Burkina Faso esté declarado ante ella y autorizado antes de volar, sea de ocio, de fotografía o profesional, y advierte de que la importación puede requerir autorización previa. Volar sin permiso acarrea multa, CONFISCACIÓN del aparato y acciones judiciales. A esto se suma que el FCDO prohíbe fotografiar instalaciones militares o gubernamentales, y que en un país con ocho regiones en estado de emergencia cualquier aparato volando sobre una columna de vehículos se interpreta como reconocimiento hostil. Recomendación operativa: el dron no entra en el país.")

STARLINK_CALLOUT = ("danger", "Starlink no está autorizado y usarlo es un riesgo legal",
                    "La ARCEP burkinesa advirtió en marzo de 2024 de que Starlink carece de autorización en el país y amenazó con perseguir a quienes ofrezcan o utilicen el servicio. La importación de terminales está técnicamente prohibida desde entonces, aunque la venta informal continúa. En julio de 2026 la ministra de Transición Digital habló de avances en las negociaciones, pero no hay licencia publicada ni calendario ni tarifas. Entrar con una antena en un país con ocho regiones en estado de emergencia añade una acusación de comunicaciones no autorizadas a cualquier control de carretera.")

DOG_MATRIX = [
    ("Uagadugú y área metropolitana", "por confirmar", "Requisitos concretos sin fuente oficial abierta. Plan B: confirmar por escrito con el viceconsulado honorario de España en Uagadugú y con una clínica veterinaria de la capital antes de comprometer nada."),
    ("Bobo-Dioulasso y suroeste (Hauts-Bassins, Cascades)", "no recomendado", "Ambas regiones están bajo estado de emergencia y el eje de acceso desde la capital está desaconsejado por el MAEC. Plan B: sustituir el tramo por el norte de Ghana y Costa de Marfil, que es lo que ya prevé la ruta global."),
    ("Sahel, Nord, Centre-Nord, Est", "prohibido", "Zona de riesgo extremo, secuestro y minas; el eje Kaya–Dori solo se recorre en convoy escoltado. Plan B: no hay; ni con perro ni sin él."),
    ("Pasos fronterizos terrestres", "por confirmar", "Ninguna fuente abierta confirma qué exigen los puestos terrestres para un animal de compañía. Plan B: dar por hecho que se exige autorización previa de importación y llevarla tramitada con 14 días de margen."),
    ("Parques nacionales (Arly, W, Deux Balé)", "prohibido", "Parques en zona de operaciones militares y con presencia de grupos armados; además el acceso de perros a áreas protegidas suele estar vetado. Plan B: ninguno."),
    ("Vuelta a la UE desde Burkina Faso", "permitido con condiciones", "País no listado en el Reglamento (UE) 2026/636: titulación antirrábica previa anotada en el pasaporte antes de salir de España. Plan B: si no se hizo antes, esperar tres meses desde la extracción de sangre antes de poder entrar en la UE."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje para Burkina Faso, actualizado 19 de mayo de 2025", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina%20Faso"),
    ("MAEC · Ficha País de Burkina Faso, abril de 2026 (PDF)", "https://www.exteriores.gob.es/Documents/FichasPais/BURKINAFASO_FICHA%20PAIS.pdf"),
    ("MAEC · Embajada de España en Mali y Burkina Faso, Bamako (web oficial, 2026)", "https://www.exteriores.gob.es/Embajadas/bamako/es/Paginas/index.aspx"),
    ("FCDO · Foreign travel advice: Burkina Faso (Gobierno del Reino Unido, 2026)", "https://www.gov.uk/foreign-travel-advice/burkina-faso"),
    ("FCDO · Burkina Faso: Safety and security (Gobierno del Reino Unido, 2026)", "https://www.gov.uk/foreign-travel-advice/burkina-faso/safety-and-security"),
    ("Gobierno de Canadá · Burkina Faso travel advice, actualizado 9 de septiembre de 2026", "https://travel.gc.ca/destinations/burkina-faso"),
    ("Servicio Exterior de Bélgica · Transport au Burkina Faso, consejos a los viajeros", "https://diplomatie.belgium.be/fr/pays/burkina-faso/voyager-au-burkina-faso-conseils-aux-voyageurs/transport-au-burkina-faso"),
    ("NaTHNaC TravelHealthPro · Burkina Faso, página de país (noticias hasta julio de 2026)", "https://travelhealthpro.org.uk/country/37/burkina-faso"),
    ("Nomedic · Healthcare in Burkina Faso: Visitor Guide (2026)", "https://nomedic.co/travel/burkina-faso"),
    ("Visa Burkina · Entry visas to Burkina Faso: the short term visa (portal oficial del eVisa, tarifas)", "https://www.visaburkina.bf/en/entry-visas-to-burkina-faso-the-short-term-visa/"),
    ("Visa Burkina · Portal oficial del eVisa, página principal en inglés", "https://www.visaburkina.bf/en/"),
    ("Visa Burkina · Entry visas to Burkina Faso: the AES visa (página publicada sin contenido)", "https://www.visaburkina.bf/en/entry-visas-to-burkina-faso-the-aes-visa/"),
    ("Agence Ecofin · L'AES discute d'un visa unique pour ses États membres, 3 de febrero de 2025", "https://www.agenceecofin.com/actualites/0302-125490-l-aes-discute-d-un-visa-unique-pour-ses-etats-membres"),
    ("Africanews · Burkina: les visas gratuits pour les ressortissants des pays africains, 15 de septiembre de 2025", "https://fr.africanews.com/amp/2025/09/13/burkina-les-visas-gratuits-pour-les-ressortissants-des-pays-africains/"),
    ("Fragomen · Burkina Faso/Mali/Niger: ECOWAS Withdrawal to Eventually Change Business and Tourist Visa Entry Requirements, 31 de enero de 2025", "https://www.fragomen.com/insights/burkina-fasomaliniger-ecowas-withdrawal-to-eventually-change-business-and-tourist-visa-entry-requirements.html"),
    ("Carte Brune d'Assurance CEDEAO · Ficha del Estado miembro Burkina Faso (bureau nacional)", "https://www.cartebrune.org/Burkina-Faso.html"),
    ("Carte Brune d'Assurance CEDEAO · Actualités, noticias hasta el 5 de agosto de 2026", "https://www.cartebrune.org/-Actualites-.html"),
    ("Carnet de Passage · Ficha de Burkina Faso (AIT/FIA)", "https://carnetdepassage.org/country/burkina-faso"),
    ("UN Logistics Cluster · 2.3.1 Burkina Faso Border Crossing of Faramana", "https://lca.logcluster.org/231-burkina-faso-border-crossing-faramana"),
    ("UN Logistics Cluster · 2.3.2 Burkina Faso Border Crossing of Koloko", "https://lca.logcluster.org/232-burkina-faso-border-crossing-koloko"),
    ("UN Logistics Cluster · 2.3.3 Burkina Faso Border Crossing of Niangoloko", "https://lca.logcluster.org/233-burkina-faso-border-crossing-niangoloko"),
    ("UN Logistics Cluster · 2.3.5 Burkina Faso Border Crossing of Dakola", "https://lca.logcluster.org/235-burkina-faso-border-crossing-dakola"),
    ("UN Logistics Cluster · 2.3.6 Burkina Faso Border Crossing of Cinkanse", "https://lca.logcluster.org/236-burkina-faso-border-crossing-cinkanse"),
    ("UN Logistics Cluster · 2.3.7 Burkina Faso Border Crossing of Nadiagou", "https://lca.logcluster.org/237-burkina-faso-border-crossing-nadiagou"),
    ("UN Logistics Cluster · 2.3.8 Burkina Faso Border Crossing of Kantchari", "https://lca.logcluster.org/238-burkina-faso-border-crossing-kantchari"),
    ("ANAC-BF · Agence Nationale de l'Aviation Civile, página oficial sobre drones", "https://anac.bf/drones/"),
    ("Notre Afrik · Starlink au Burkina Faso: vers une autorisation après 2 ans, actualizado julio de 2026", "https://notreafrik.com/starlink-burkina-faso-negociation-autorisation/"),
    ("GlobalPetrolPrices · Precio de la gasolina en Burkina Faso, dato de 12 de enero de 2026", "https://www.globalpetrolprices.com/Burkina-Faso/gasoline_prices/"),
    ("GlobalPetrolPrices · Precio del gasóleo en Burkina Faso, dato de 9 de febrero de 2026", "https://www.globalpetrolprices.com/Burkina-Faso/diesel_prices/"),
    ("EUR-Lex · Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026, listas de terceros países para desplazamientos sin ánimo comercial de animales de compañía", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600636"),
    ("Service Public du Burkina Faso · Demande d'autorisation d'importation des animaux, des produits animaux et des produits d'origine animale (portal oficial de trámites)", "https://www.service-public.gov.bf/thematiques/secteur-de-lelevage/demande-dautorisation-dimportation-des-animaux-des-produits-animaux-et-des-produits-dorigine-animale"),
    ("Sidwaya · Axe Kaya-Dori: quand l'attente du convoi devient une source de revenus, 24 de julio de 2025", "https://www.sidwaya.info/axe-kaya-dori-quand-lattente-du-convoi-devient-une-source-de-revenus/"),
    ("Wikipedia · Ouagadougou (coordenadas, clima, aeropuerto)", "https://en.wikipedia.org/wiki/Ouagadougou"),
    ("Wikipedia · Thomas Sankara International Airport (códigos OUA/DFFD, aeropuerto de Donsin)", "https://en.wikipedia.org/wiki/Thomas_Sankara_International_Airport"),
    ("Wikipedia · List of airports in Burkina Faso (coordenadas de OUA y BOY)", "https://en.wikipedia.org/wiki/List_of_airports_in_Burkina_Faso"),
    ("Wikipedia · Transport in Burkina Faso (red viaria, ferrocarril Sitarail)", "https://en.wikipedia.org/wiki/Transport_in_Burkina_Faso"),
    ("Wikipédia · Centre hospitalier universitaire Sourou Sanou, Bobo-Dioulasso", "https://fr.wikipedia.org/wiki/Centre_hospitalier_universitaire_Sourou_Sanou"),
    ("The Road Chose Me · Categoría Burkina Faso, vuelta a África de Dan Grec en Jeep Wrangler (2016-2019)", "https://theroadchoseme.com/category/burkina-faso"),
    ("Into the World · Burkina Faso: Ouagadougou and Bobo Dioulasso, cruce en moto, septiembre de 2011", "https://intotheworld.eu/burkina-faso-ouagadougou-bobo-dioulasso/"),
    ("Overland Diaries · Burkina Faso, travesía de febrero-marzo de 2010", "https://overlanddiaries.com/burkina-faso/"),
    ("Andy's World Journeys · I Visited Burkina Faso... So You Don't Have To! Twice!, 7 de mayo de 2020", "https://andysworldjourneys.com/2020/05/07/visit-burkina-faso/"),
    ("Looking for Dongxi · Roadtrip in the wild west of Burkina Faso, Bobo-Dioulasso – Ouagadougou, 16 de marzo de 2018", "https://lookingfordongxi.co/2018/03/16/roadtrip-bobo-dioulasso-ouagadougou/"),
    ("Fiche de voyage · Portal oficial del formulario obligatorio de viaje desde el 8 de abril de 2026 (citado por el MAEC)", "https://fichedevoyage.gov.bf/"),
    ("Rood Wooko (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Rood_Wooko"),
    ("Recomendaciones de viaje MAEC · Burkina Faso", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"),
    ("Bobo-Dioulasso (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bobo-Dioulasso"),
    ("Cascades de Karfiguéla (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Cascades_de_Karfigu%C3%A9la"),
    ("Banfora (Wikipedia EN)", "https://en.wikipedia.org/wiki/Banfora"),
    ("Lac de Tengréla (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Lac_de_Tengr%C3%A9la"),
    ("Pics de Sindou (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Pics_de_Sindou"),
    ("Sindou (Wikipedia EN)", "https://en.wikipedia.org/wiki/Sindou"),
    ("Ruins of Loropéni · UNESCO", "https://whc.unesco.org/en/list/1225"),
    ("Loropéni (Wikipedia EN)", "https://en.wikipedia.org/wiki/Loropeni"),
    ("Ruines de Loropéni (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Ruines_de_Lorop%C3%A9ni"),
    ("La Cour royale de Tiébélé · UNESCO", "https://whc.unesco.org/en/list/1713/"),
    ("Tiébélé (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ti%C3%A9b%C3%A9l%C3%A9"),
    ("Ancient Ferrous Metallurgy Sites of Burkina Faso · UNESCO", "https://whc.unesco.org/en/list/1602"),
    ("Nazinga Game Ranch (Wikipedia EN)", "https://en.wikipedia.org/wiki/Nazinga_Game_Ranch"),
    ("GeoNames · Foret Classee de Nazinga", "https://www.geonames.org/search.html?q=Nazinga&country=BF"),
    ("W-Arly-Pendjari Complex · UNESCO", "https://whc.unesco.org/en/list/749"),
    ("Arly National Park (Wikipedia EN)", "https://en.wikipedia.org/wiki/Arly_National_Park"),
    ("Sculpture sur granit de Laongo · Oficina Nacional de Turismo (ONTB)", "https://www.ontb.bf/visites/sites-touristiques/sculpture-sur-granit-de-laongo"),
    ("GeoNames · Laongo", "https://www.geonames.org/search.html?q=Laongo&country=BF"),
    ("Mare aux crocodiles sacres de Bazoulé · ONTB", "https://www.ontb.bf/visites/sites-touristiques/mare-aux-crocodiles-sacres-de-bazoule"),
    ("GeoNames · Bazoulé", "https://www.geonames.org/search.html?q=Bazoule&country=BF"),
    ("Mares aux crocodiles sacres de Sabou · ONTB", "https://www.ontb.bf/visites/sites-touristiques/mares-aux-crocodiles-sacres-de-sabou"),
    ("Sabou (Wikipedia EN)", "https://en.wikipedia.org/wiki/Sabou"),
    ("GeoNames · Tagbaladougou", "https://www.geonames.org/search.html?q=Tagbaladougou&country=BF"),
    ("Koudougou (Wikipedia EN)", "https://en.wikipedia.org/wiki/Koudougou"),
    ("Ouahigouya (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ouahigouya"),
    ("Gorom-Gorom (Wikipedia EN)", "https://en.wikipedia.org/wiki/Gorom-Gorom"),
    ("Fada N'gourma (Wikipedia EN)", "https://en.wikipedia.org/wiki/Fada_N%27gourma"),
]

# Bucle sur y suroeste (el único defendible): Uagadugú - Nazinga - Tiébélé - Loropéni - Banfora - Bobo - Uagadugú
CORRIDOR = [
    (12.37648, -1.47294),
    (12.51276, -1.27618),
    (12.3196, -1.70888),
    (12.06013, -2.22613),
    (12.25622, -2.35175),
    (11.16492, -4.30515),
    (10.78333, -4.7),
    (10.63969, -4.80858),
    (10.69793, -4.81792),
    (10.63969, -4.80858),
    (10.65694, -5.1525),
    (10.29274, -3.53194),
    (11.04919, -1.41849),
    (11.08922, 0.96186),
    (12.37648, -1.47294),
]

# Bucle norte y este (VETADO por el MAEC: Yatenga, Liptako, Gourma y Tapoa en riesgo extremo)
CORRIDOR_ALT = [
    (12.37648, -1.47294),
    (12.51276, -1.27618),
    (13.08812, -1.10632),
    (13.56683, -2.41099),
    (14.4444, -0.23571),
    (12.06016, 0.36542),
    (11.58333, 1.46667),
    (12.37648, -1.47294),
]

HISTORIA_RESUMEN = "Burkina Faso —«la patria de los hombres íntegros»— es un país sin salida al mar en el corazón del Sahel, heredero de los reinos mossi que resistieron durante siglos a los imperios del Níger y a la expansión del islam antes de caer ante Francia en 1896. Independiente desde el 5 de agosto de 1960 con el nombre de Alto Volta, su historia ha sido una sucesión de golpes militares, con el paréntesis revolucionario de Thomas Sankara, asesinado en 1987, y los veintisiete años de Blaise Compaoré, derribado por la insurrección popular de 2014. Desde los dos golpes de 2022 gobierna una junta encabezada por el capitán Ibrahim Traoré, con elecciones aplazadas sin fecha, salida de la CEDEAO y una insurgencia yihadista que disputa buena parte del territorio."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>El territorio del actual Burkina Faso estuvo poblado desde muy antiguo por cazadores-recolectores y, más tarde, por comunidades agrícolas: la Wikipedia en español sitúa los primeros asentamientos agrarios entre el 3600 y el 2600 antes de nuestra era y recuerda que los dogon ocuparon el centro y el norte antes de emigrar hacia el oeste.</p><p>La historia política del país la marcan los reinos mossi. La tradición oral los hace nacer de la princesa Yennenga, hija de Naa Gbewaa, y del cazador mandé Rialé; su hijo Ouédraogo fundó Tenkodogo y su nieto Oubri, que habría reinado entre 1050 y 1090, está considerado el fundador de la dinastía de Uagadugú. De ahí salieron los reinos de Uagadugú —cuyo soberano lleva el título de <em>Mogho Naaba</em>, «rey de todo el mundo»—, Tenkodogo, Fada N'Gourma, Zondoma y Boussouma, datados por las distintas tradiciones entre los siglos XI y XV.</p><p>Fueron potencias militares: en el siglo XV los mossi tomaron Tombuctú y saquearon Oualata, y resistieron la guerra santa que les declaró en 1497 Askia Mohammad I, del imperio songhai. En el suroeste, las ruinas de Loropéni —ocupadas desde el siglo XI y en su apogeo entre los siglos XIV y XVII— atestiguan el control del oro por los pueblos lohron y koulango dentro del comercio transahariano.</p>"),
    ("Colonización",
     "<p>La conquista francesa fue tardía y rápida. Francia derrotó a los reinos mossi en 1896 y hacia 1898 controlaba nominalmente casi todo el territorio, que quedó encuadrado en el África Occidental Francesa. La reorganización de 1904 lo integró en la colonia de Alto Senegal y Níger, con capital en Bamako.</p><p>La colonia autónoma del Alto Volta se creó el 1 de marzo de 1919, se desmanteló el 5 de septiembre de 1932 —repartida entre las colonias vecinas, en buena medida para surtir de mano de obra a las plantaciones de Costa de Marfil— y se restableció con sus fronteras anteriores el 4 de septiembre de 1947. Los franceses mantuvieron en pie las estructuras mossi y gobernaron a través de ellas, lo que explica que el Mogho Naaba siga siendo hoy una autoridad moral respetada.</p><p>La huella colonial se reconoce en tres cosas: unas fronteras trazadas sin relación con los reinos, una economía orientada a la exportación de algodón y a la emigración de trabajadores hacia la costa —todavía hoy viven unos tres millones de burkineses en Costa de Marfil— y el francés como lengua de la administración. El 11 de diciembre de 1958 el Alto Volta se proclamó república con autogobierno dentro de la Comunidad Francesa, antesala de la independencia.</p>"),
    ("Independencia y construcción del Estado",
     "<p>El Alto Volta accedió a la independencia el 5 de agosto de 1960, con Maurice Yaméogo como primer presidente. Su deriva autoritaria acabó en 1966 con un golpe encabezado por Sangoulé Lamizana; siguieron los de Saye Zerbo en 1980 y Jean-Baptiste Ouédraogo en 1982. El MAEC resume esas décadas como «una serie de golpes de estado y gobiernos militares».</p><p>El 4 de agosto de 1983 un golpe llevó al poder al capitán Thomas Sankara, nacido en 1949 y con 33 años entonces. Su gobierno, de inspiración marxista, emprendió campañas de vacunación —dos millones de personas entre 1983 y 1985—, alfabetización, plantación masiva de árboles contra la desertización y prohibición de la mutilación genital femenina, el matrimonio forzoso y la poligamia. El 4 de agosto de 1984 rebautizó el país como Burkina Faso, «la patria de los hombres íntegros», y le dio la bandera actual.</p><p>El 15 de octubre de 1987 Sankara fue asesinado en el golpe dirigido por su compañero de armas Blaise Compaoré, que gobernaría veintisiete años. Compaoré abrió el multipartidismo con la Constitución de 1991 y ganó todas las presidenciales —1991, 1998, 2005 y 2010—, combinando una apertura formal y un papel de mediador regional con el control férreo del aparato del Estado.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>El sistema de Compaoré se rompió en octubre de 2014, cuando su intento de reformar la Constitución para volver a presentarse desencadenó una insurrección popular; dimitió el 31 de octubre de 2014. Tras una transición dirigida por Michel Kafando y un golpe fallido en septiembre de 2015, Roch Marc Christian Kaboré ganó las elecciones del 29 de noviembre de 2015 y fue reelegido en 2020 con el 57,87 % de los votos.</p><p>Mientras tanto, la insurgencia yihadista iniciada el 23 de agosto de 2015 se extendió desde el norte a casi todo el país, con el JNIM, el Estado Islámico en el Gran Sáhara y Ansarul Islam como principales actores y con las milicias de Voluntarios para la Defensa de la Patria, legalizadas en enero de 2020, como respuesta del Estado. Las matanzas de Solhan en junio de 2021, Seytenga en junio de 2022 y Barsalogho en agosto de 2024 —entre 200 y 400 muertos según el MAEC— marcaron el deterioro.</p><p>El 24 de enero de 2022 el teniente coronel Paul-Henri Damiba derrocó a Kaboré; el 30 de septiembre de 2022 el capitán Ibrahim Traoré derrocó a Damiba. Ese mismo año se juzgó por fin el magnicidio de Sankara: el 6 de abril de 2022 Compaoré fue condenado en rebeldía a cadena perpetua.</p>"),
    ("Política y gobierno en 2026",
     "<p>A fecha de septiembre de 2026 gobierna una junta militar de transición. El jefe del Estado es el capitán Ibrahim Traoré, que tomó el poder en el golpe del 30 de septiembre de 2022; el primer ministro es Rimtalba Jean Emmanuel Ouédraogo. Las últimas elecciones fueron las presidenciales de 2020. Las <em>assises nationales</em> de mayo de 2024 prorrogaron la transición cinco años desde el 2 de julio de 2024 y, según el MAEC, la Carta adoptada el 27 de marzo de 2026 suprimió los plazos electorales: no hay fecha de elecciones.</p><p>Freedom House lo clasifica como <strong>«Not Free»</strong>, con 25 puntos sobre 100: 3 sobre 40 en derechos políticos y 22 sobre 60 en libertades civiles; su informe de 2025 describe una junta que se atrinchera en el poder y reprime la disidencia. No es una democracia limitada, sino un régimen autoritario militar. Reporteros Sin Fronteras lo sitúa en el puesto 110 de 180 en 2026.</p><p>El MAEC desaconseja todo viaje salvo por extrema necesidad (aviso del 19 de mayo de 2025) y advierte de que el terrorismo y el secuestro están presentes «en todo el país», incluidas Uagadugú y Bobo-Dioulasso, únicas ciudades cuya estancia contempla; cita observadores que calculan hasta un 70 % del territorio fuera del control estatal. El país fundó la Alianza de Estados del Sahel en septiembre de 2023 y salió de la CEDEAO el 29 de enero de 2025. España mantiene relaciones desde 1964 y lo atiende desde Bamako.</p>"),
    ("Economía y recursos",
     "<p>Burkina Faso es uno de los países más pobres del mundo: ocupaba el puesto 185 del índice de desarrollo humano del PNUD en 2022 y el Banco Mundial estima su PIB per cápita en unos 1.150 dólares corrientes en 2025, con un PIB de unos 27.600 millones y un crecimiento del 5,3 %. El MAEC, con datos del FMI de abril de 2026, da unos 3.230 dólares per cápita en paridad de poder adquisitivo.</p><p>La riqueza sale del subsuelo y del campo. El oro es con diferencia la primera exportación —unos 2.170 millones de dólares según el MAEC—, seguido del algodón, con unos 252 millones y alrededor del 4 % del PIB. La agricultura aporta cerca del 23 % del PIB pero ocupa al 85 % de la población activa: sorgo, mijo, maíz, cacahuete, arroz y ganadería. La minería artesanal del oro financia también a grupos armados, y pesan mucho las remesas y la ayuda internacional, recortada tras la ruptura con Francia en 2023.</p><p>La moneda es el franco CFA de África Occidental, con paridad fija de 655,957 por euro. Desde marzo de 2025 la Alianza de Estados del Sahel aplica un arancel común del 0,5 % a las importaciones de fuera del bloque y emite pasaporte propio. El visado es obligatorio y electrónico, y la Carte Brune de seguro de la CEDEAO seguía listando a Burkina Faso como Estado miembro en septiembre de 2026.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Burkina Faso tiene unos 24 millones de habitantes, según el UNFPA de 2025 citado por el MAEC, y más de sesenta grupos de población. Los mossi son mayoría, en torno al 52 %, junto a fulani, bobo, senufo, gurunsi, lobi y dagara. La reforma constitucional de diciembre de 2023 elevó las lenguas nacionales a oficiales y dejó el francés como lengua de trabajo. Por carretera, el mooré sirve en casi toda la meseta central, el dioula en el oeste y el suroeste y el fulfuldé en el norte; el francés se entiende en ciudades y administración.</p><p>El censo de 2019 recogido por el MAEC da un 63,8 % de musulmanes, un 20,1 % de católicos, un 6,2 % de protestantes y un 9 % de practicantes de religiones tradicionales, muy presentes en la vida cotidiana. Uagadugú acoge el FESPACO, mayor festival de cine africano, creado en 1969. El balafón es el instrumento emblemático y la cocina gira en torno al <em>tô</em>, el arroz graso, el «pollo bicicleta» y el <em>dolo</em>, cerveza de mijo. La UNESCO tiene inscritos cuatro bienes, entre ellos Loropéni y la corte real de Tiébélé.</p><p>Conviene vestir con discreción, con hombros y rodillas cubiertos, sobre todo en el norte musulmán. Pida permiso antes de fotografiar a personas y nunca fotografíe militares, controles ni edificios oficiales. En 2027 el ramadán empieza en torno al 8 de febrero, con menos restaurantes abiertos de día; el alcohol se consume con normalidad en el sur y el oeste, y con discreción en zonas musulmanas.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Burkina Faso (MAEC España · Oficina de Información Diplomática · abril de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/BURKINAFASO_FICHA%20PAIS.pdf"),
    ("Recomendaciones de viaje: Burkina Faso (MAEC España · actualizada el 19 de mayo de 2025)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burkina+Faso"),
    ("Freedom in the World 2025: Burkina Faso (Freedom House · 2025)", "https://freedomhouse.org/country/burkina-faso/freedom-world/2025"),
    ("World Report 2026: Burkina Faso (Human Rights Watch · enero de 2026)", "https://www.hrw.org/world-report/2026/country-chapters/burkina-faso"),
    ("Burkina Faso (Reporteros Sin Fronteras · Índice Mundial de Libertad de Prensa 2026)", "https://rsf.org/en/country/burkina-faso"),
    ("Burkina Faso Data (Banco Mundial · indicadores 2024-2025)", "https://data.worldbank.org/country/burkina-faso"),
    ("Burkina Faso — States Parties (UNESCO Centro del Patrimonio Mundial · consultado en 2026)", "https://whc.unesco.org/en/statesparties/bf"),
    ("Ruins of Loropéni (UNESCO Centro del Patrimonio Mundial · inscrito en 2009)", "https://whc.unesco.org/en/list/1225/"),
    ("Burkina Faso (Wikipedia en español · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Burkina_Faso"),
    ("Burkina Faso (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Burkina_Faso"),
    ("Mossi Kingdoms (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Mossi_Kingdoms"),
    ("Thomas Sankara (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Thomas_Sankara"),
    ("Ibrahim Traoré (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Ibrahim_Traor%C3%A9"),
    ("Alliance of Sahel States (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Alliance_of_Sahel_States"),
    ("Jihadist insurgency in Burkina Faso (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Jihadist_insurgency_in_Burkina_Faso"),
    ("Visa policy of Burkina Faso (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Visa_policy_of_Burkina_Faso"),
    ("Culture du Burkina Faso (Wikipedia en francés · consultado en septiembre de 2026)", "https://fr.wikipedia.org/wiki/Culture_du_Burkina_Faso"),
    ("Carte Brune d'Assurance CEDEAO — Burkina Faso (cartebrune.org · consultado en septiembre de 2026)", "https://www.cartebrune.org/Burkina-Faso.html"),
    ("Burkina Faso (International Crisis Group · CrisisWatch, agosto de 2026)", "https://www.crisisgroup.org/africa/sahel/burkina-faso"),
    ("Burkina Faso (Encyclopaedia Britannica · consultado en septiembre de 2026)", "https://www.britannica.com/place/Burkina-Faso"),
]

SPEC = dict(
    slug="burkina-faso", name="Burkina Faso", revision="18 sep 2026",
    sub="EXCLUIDO POR PROTOCOLO — conflicto activo, desaconsejo total de MAEC, FCDO y Canadá · ficha informativa",
    chips=[
        ("ESTATUS", "EXCLUIDO POR PROTOCOLO. MAEC: se desaconseja el viaje salvo por razones de extrema necesidad…"),
        ("CÓMO LLEGAR", "Por aire al aeropuerto internacional Thomas Sankara de Uagadugú (OUA)…"),
        ("VISADO", "OBLIGATORIO para españoles. eVisa desde el 1 de febrero de 2023 en visaburkina.bf…"),
        ("VEHÍCULO", "No existe organización emisora de CPD en Burkina Faso (AIT/FIA)…"),
        ("SEGURIDAD", "MAEC: desaconsejado salvo extrema necesidad (19-05-25)"),
        ("SEGURO", "Carta Verde no vale · Carte Brune CEDEAO en frontera"),
        ("SALUD", "Fiebre amarilla OBLIGATORIA (≥9 meses) · malaria alta"),
        ("DRONES", "Prohibidos sin autorización ANAC · confiscación"),
        ("STARLINK", "NO autorizado · ARCEP amenaza sanción (jul-2026)"),
        ("4x4", "Diésel 675 XOF/l (feb-2026) · minas en los ejes"),
        ("A PIE", "Solo casco urbano y de día · nunca interurbano"),
        ("PERRO", "Entrada regulada por la autorización de importación de animales del portal oficial service-public.gov.bf (3 a…"),
        ("MONEDA", "Franco CFA de África Occidental (XOF), con paridad fija: 1 EUR = 655,957 FCFA…"),
        ("VENTANA", "Semiárido cálido (BSh). Lluvias de mayo a septiembre…"),
    ],
    center=[12.37, -1.93], zoom=6,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle sur y suroeste (el único defendible): Uagadugú - Nazinga - Tiébélé - Loropéni - Banfora - Bobo - Uagadugú",
    corridor_alt_label="Bucle norte y este (VETADO por el MAEC: Yatenga, Liptako, Gourma y Tapoa en riesgo extremo)",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Tiebele_village_in_Burkina_Faso_02.jpg?width=1200",
    hero_credit="Tiébélé · Alexander Leisser · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Burkina Faso queda fuera de la ruta de 2027 por protocolo, y con los datos actuales no es una decisión discutible. El MAEC desaconseja el viaje salvo por razones de extrema necesidad a TODO el país (19 de mayo de 2025), el FCDO desaconseja todo viaje sin excepción territorial y Canadá mantiene «evitar todo viaje» en su revisión de 9 de septiembre de 2026: los tres coinciden y ninguno salva región alguna. La junta de Ibrahim Traoré gobierna desde septiembre de 2022, hay estado de emergencia en ocho regiones y JNIM y el Estado Islámico disputan buena parte del territorio; el FCDO documenta ataques crecientes contra las carreteras principales, incluido el uso de minas, y el propio MAEC desaconseja el eje Uagadugú–Bobo-Dioulasso, columna vertebral del país. Eso vacía de sentido el modelo de la expedición: 250 km diarios, pernocta autónoma y un perro a bordo. Añádase que España no tiene embajada residente en Uagadugú —la competencia es de Bamako, a casi 900 km y en la misma crisis— y que una evacuación sería lenta, cara y sin plan para el animal. Si algún día cambiara, la forma realista no sería el overland sino un vuelo a Uagadugú (OUA) y un operador local con vehículo y conductor para Banfora y Bobo-Dioulasso: del orden de 1.200 a 1.800 € por persona, más un seguro con cobertura en zona desaconsejada que hoy casi nadie emite. Lo pendiente no es si se entra, sino confirmar que el tramo se sustituye por el norte de Ghana y Costa de Marfil.",
    facts=[
        ("Estatus", "EXCLUIDO POR PROTOCOLO. MAEC: se desaconseja el viaje salvo por razones de extrema necesidad, todo el país (19-05-2025). FCDO: se desaconseja todo viaje. Canadá: evitar todo viaje (09-09-2026)."),
        ("Cómo llegar", "Por aire al aeropuerto internacional Thomas Sankara de Uagadugú (OUA), que concentra el 98 % del tráfico comercial del país. Por tierra hay pasos operativos con seis países vecinos, pero los ejes de acceso están en zona de emboscada y minas."),
        ("Visado", "OBLIGATORIO para españoles. eVisa desde el 1 de febrero de 2023 en visaburkina.bf; hay que imprimirlo y presentarlo. Turismo: 33.000 FCFA una entrada (unos 50 €) y 55.000 FCFA múltiples entradas, estancia máxima 90 días. Desde el 8 de abril de 2026 se exige además la «fiche de voyage» en las 72 h previas (fichedevoyage.gov.bf)."),
        ("Vehículo/aduana", "No existe organización emisora de CPD en Burkina Faso (AIT/FIA). El carnet se emite en el país de matriculación: en España, el RACE. En frontera se trabaja con admisión temporal y laissez-passer de aduanas; el último importe documentado son 5.000 FCFA, pero es de 2011."),
        ("Seguro", "La Carta Verde europea NO cubre Burkina Faso. El seguro de responsabilidad civil es obligatorio en el país. El sistema regional es la Carte Brune CEDEAO, y cartebrune.org sigue listando a Burkina Faso como Estado miembro con bureau nacional activo en Uagadugú y nueve aseguradoras afiliadas."),
        ("Moneda", "Franco CFA de África Occidental (XOF), con paridad fija: 1 EUR = 655,957 FCFA. El euro se acepta con frecuencia. Efectivo imprescindible fuera de las dos grandes ciudades."),
        ("Perro", "Entrada regulada por la autorización de importación de animales del portal oficial service-public.gov.bf (3 a 14 días hábiles, coste variable); el detalle para perros no está publicado. Para volver a la UE, Burkina Faso NO está en la lista del Reglamento (UE) 2026/636: hace falta titulación antirrábica previa."),
        ("Drones", "Todo dron debe declararse ante la ANAC y estar autorizado antes de volar (Ley n.º 028-2021/AN, de 17 de mayo de 2021). Sin autorización: multa, CONFISCACIÓN y acciones judiciales. En la práctica, el dron no entra en el país."),
        ("Starlink", "NO autorizado. La ARCEP advirtió en marzo de 2024 de que el servicio carece de licencia y amenazó con perseguir a quien lo ofrezca o use. En julio de 2026 el Gobierno hablaba de «avances» en las negociaciones, sin licencia publicada."),
        ("Seguridad", "Estado de emergencia en Centre-Est, Est, Centre-Nord, Nord, Boucle du Mouhoun, Sahel, Hauts-Bassins y Cascades (FCDO). Amenaza muy alta de secuestro por grupos afines a Al Qaeda y al Estado Islámico; los europeos se consideran objetivo legítimo."),
        ("Clima", "Semiárido cálido (BSh). Lluvias de mayo a septiembre; estación seca y fresca de octubre a febrero, con mínimas de 16 °C; estación cálida de marzo a abril, con máximas de hasta 43 °C y harmattan. Unos 800 mm anuales en Uagadugú."),
        ("Sanidad", "Fiebre amarilla OBLIGATORIA con certificado internacional para todo viajero de 9 meses en adelante; el certificado es válido de por vida. Malaria de alto riesgo en todo el país y todo el año. Sanidad pública muy limitada; evacuación médica a Abiyán, Accra o París para lo complejo."),
    ],
    alerts=[
        "Los tres avisos oficiales de referencia coinciden sin matices territoriales: MAEC desaconseja el viaje salvo extrema necesidad a todo el país (19-05-2025), FCDO desaconseja todo viaje y Canadá pide evitar todo viaje en su revisión de 9 de septiembre de 2026.",
        "El FCDO advierte de ataques crecientes contra las carreteras principales «incluido el uso de minas terrestres», y cita expresamente los ejes hacia Bobo-Dioulasso, Níger, Benín y Togo: son justamente las cuatro salidas útiles del país.",
        "El MAEC desaconseja específicamente los desplazamientos por carretera entre Uagadugú y Bobo-Dioulasso. Sin ese eje no hay forma de enlazar la capital con el suroeste turístico de Banfora y las cascadas.",
        "Amenaza muy alta de secuestro de occidentales por JNIM y por grupos afiliados al Estado Islámico; el FCDO indica que los nacionales europeos se consideran objetivo legítimo.",
        "Hay ejes donde circular exige convoy escoltado: el Kaya–Dori, de 165 km, lleva más de dos años recorriéndose solo en convoy securizado, con una tasa de 1.500 FCFA por conductor (Sidwaya, 24 de julio de 2025).",
        "Viajar contra la recomendación oficial invalida la mayoría de seguros de viaje y de asistencia en carretera. Sin cobertura no hay evacuación médica pagada, y la sanidad local no resuelve un politraumatismo.",
        "España no tiene embajada residente en Uagadugú: la competencia es de la Embajada en Bamako (Mali), un país en crisis paralela. Sobre el terreno solo hay un viceconsulado honorario.",
        "La «fiche de voyage» es obligatoria desde el 8 de abril de 2026 y se rellena en las 72 h previas; sin ella la entrada puede denegarse aunque el eVisa sea correcto.",
        "Los drones se confiscan: la ANAC exige declaración y autorización previa, y el FCDO recuerda la prohibición de fotografiar instalaciones militares o gubernamentales. Con dos 4x4 llamativos, cualquier vuelo es un incidente.",
        "Starlink no tiene licencia y su uso ha sido amenazado con persecución por la ARCEP; la cobertura móvil fuera de las ciudades es limitada y el FCDO recomienda teléfono satelital, cuyo régimen de importación tampoco está claro.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Uagadugú", "Llegada, trámites, Museo Nacional, catedral y Rood Wooko", "~0 km · 2 días"),
        ("2 · Laongo y Bazoulé", "Uagadugú - Laongo (Ziniaré) - Bazoulé - Uagadugú", "~140 km · 1 día"),
        ("3 · Sabou y Koudougou", "Uagadugú - Sabou - Koudougou", "~110 km · 1 día"),
        ("4 · Koudougou - Bobo", "Koudougou - Boromo - Bobo-Diulasso por la RN1", "~260 km · 1 día"),
        ("5 · Bobo-Diulasso", "Gran mezquita, Dioulassoba y servicios", "~0 km · 1 día"),
        ("6 · Bobo - Banfora", "Bobo - Tagbaladougou - Banfora por la RN7", "~95 km · 1 día"),
        ("7 · Banfora oeste", "Karfiguéla, Fabédougou y lago Tengréla", "~60 km · 1 día"),
        ("8 · Sindou", "Banfora - Sindou - Banfora", "~85 km · 1 día"),
        ("9 · Banfora - Gaoua", "Banfora - Gaoua por Diébougou o Batié", "~290 km · 2 días"),
        ("10 · Loropéni", "Gaoua - Loropéni - Gaoua", "~80 km · 1 día"),
        ("11 · Gaoua - Pô", "Gaoua - Léo - Pô", "~300 km · 2 días"),
        ("12 · Nazinga", "Pô - Ranch de Nazinga - Pô", "~90 km · 2 días"),
        ("13 · Pô - Tiébélé", "Pô - Tiébélé (cour royale) - Pô", "~80 km · 1 día"),
        ("14 · Pô - Uagadugú", "Pô - Uagadugú por la RN5 y salida del país", "~150 km · 1 día"),
    ],
    offroad=[
        "El eje asfaltado principal es la RN1 Uagadugú-Boromo-Bobo-Diulasso; el MAEC (19-05-2025) DESACONSEJA TOTALMENTE hacerlo por carretera y recomienda tomar el avión entre las dos ciudades, así que cualquier plan 4x4 arranca ya en contradicción con el aviso oficial.",
        "Desde diciembre de 2025 se construye la autopista Uagadugú-Bobo-Diulasso, 332 km entre Yimdi y Bobo, con hasta ocho carriles y 140 km/h previstos; el desbroce completo del trazado estaba terminado el 15 de febrero de 2026, de modo que en 2027 hay que contar con obras, desvios y cortes en todo el corredor.",
        "En el suroeste, las pistas cortas de tierra a Karfiguéla, Fabédougou y Tengréla son practicables con cualquier 4x4 en estación seca y se embarran de julio a septiembre; son el único off-road realmente recomendable del país.",
        "El acceso a los picos de Sindou se hace por la ruta regional 21, al sureste del pueblo, con aparcamiento en la entrada de los senderos: no hace falta reducción, solo altura libre.",
        "En el Ranch de Nazinga los circuitos interiores son pistas de tierra y arena y exigen guarda del ranch; no se puede circular libremente ni de noche, y los elefantes tienen preferencia de paso.",
        "El acceso a los componentes de la metalurgia del hierro (Tiwêga, Yamané, Kindibo, Douroula) son pistas de aldea que solo se encuentran con guía local; además caen en provincias que el MAEC clasifica de riesgo extremo (Sanmatenga, Yatenga, Kossi, Sourou).",
        "ZONAS VETADAS PARA CUALQUIER PISTA: todo el Sahel (Liptako y Soum), el norte del eje Uahiguya-Bogandé, y el este (Gourma, Kompienga, Diapaga/Tapoa), incluidas las pistas de Arly y del complejo W-Arly-Pendjari. El MAEC pide además evitar TODAS las zonas fronterizas.",
        "No hemos localizado fuentes recientes y fiables de overlanders 4x4 en Burkina Faso: iOverlander y Tracks4Africa no se pudieron consultar en esta ronda y los relatos de ruta disponibles son anteriores a 2019. TODA LA INFORMACIÓN DE PISTAS ES POR CONFIRMAR SOBRE EL TERRENO.",
    ],
    senderismo=[
        "Picos de Sindou: senderos balizados y miradores sobre las agujas de arenisca, con aparcamiento en la entrada por la ruta regional 21; recorrido corto, sin sombra ni agua, mejor al amanecer.",
        "Domos de Fabédougou: paseo libre de una o dos horas entre bloques erosionados en colmena, a 5 km de las cascadas de Karfiguéla.",
        "Cascadas de Karfiguéla: subida escalonada a pie desde el aparcamiento hasta los saltos altos, por roca resbaladiza; calzado con suela agarrada.",
        "Monte Tenakourou, el punto más alto del país: Sindou es la base de las excursiones según la Wikipedia inglesa; ITINERARIO, DESNIVEL Y PERMISOS POR CONFIRMAR, además de estar pegado a la frontera con Malí.",
        "Ruinas de Loropéni: vuelta al perímetro amurallado con el guarda, menos de una hora, mejor con la hierba baja de la estación seca.",
        "Laongo: circuito a pie entre los afloramientos de granito y las esculturas, con libro-guía en recepcion; abre de 8 a 18 h y cuesta 2.500 FCFA.",
        "Orillas del lago Tengréla: paseo corto por los caminos entre huertas y cañaverales antes de embarcar en la piragua; no acercarse a las zonas de hipopótamos a pie.",
        "En el resto del país NO hay senderismo planteable: el Sahel, el norte y el este estan vetados, y en los parques del este no se camina fuera del vehículo por la presencia de leones.",
    ],
    acampada=[
        "Campamento de Kegnigohi, en el lago Tengréla: la Wikipedia francesa lo describe como alojamiento con alquiler de vehículos, activo desde los años dos mil; PRECIOS Y ESTADO ACTUAL POR CONFIRMAR.",
        "Sabou ofrece alojamiento en el propio sitio de los cocodrilos: 3.300 FCFA la habitacion individual y 3.600 la doble según la Oficina Nacional de Turismo; hay sitio para aparcar dos 4x4.",
        "Bazoulé tiene campamento de aldea con teléfonos de contacto publicados por la Oficina Nacional de Turismo (+226 70 77 85 09); TARIFAS POR CONFIRMAR.",
        "El Ranch de Nazinga dispone de campamento dentro del recinto, la opcion más lógica para dormir cerca de los elefantes; ESTADO DE APERTURA, PRECIOS Y SI ADMITEN TIENDA DE TECHO POR CONFIRMAR.",
        "La Oficina Nacional de Turismo lista «campings» entre sus categorías de alojamiento, pero no hemos podido abrir un listado con nombres y direcciones concretas.",
        "Acampada libre: DESACONSEJADA EN TODO EL PAÍS. Con un desaconsejo total del MAEC, controles militares frecuentes y riesgo de secuestro, dormir fuera de recinto vigilado es la peor decision posible.",
        "En la práctica, el patron razonable es dormir en hoteles con patio cerrado en Uagadugú, Koudougou, Bobo-Diulasso, Banfora y Pô, y usar el techo de los coches solo dentro de recintos vigilados.",
        "No hemos podido consultar iOverlander ni Tracks4Africa en esta ronda: NO HAY FUENTE DE ACAMPADA VERIFICADA Y ACTUALIZADA para Burkina Faso en esta ficha.",
    ],
    visado=[
        "VISADO OBLIGATORIO para españoles. No hay exención, y no se puede dar por segura la expedición a la llegada en un paso terrestre.",
        "Se tramita en línea como eVisa en visaburkina.bf, disponible desde el 1 de febrero de 2023 según el MAEC. Hay que IMPRIMIRLO y presentarlo a la llegada.",
        "Tarifas oficiales de corta duración (visaburkina.bf): turismo 33.000 FCFA una entrada y 55.000 FCFA múltiples entradas; «express» 104.500 FCFA; negocios 77.000 / 93.500 FCFA. Al cambio fijo, 33.000 FCFA son unos 50 € y 55.000 FCFA unos 84 €.",
        "Estancia máxima 90 días. Documentación exigida: pasaporte en vigor, formulario, dos fotos de 3,5 × 4,5 cm, justificante del motivo del viaje, certificado médico, seguro de salud y timbres.",
        "Desde el 8 de abril de 2026 hay que cumplimentar además la «fiche de voyage» en fichedevoyage.gov.bf dentro de las 72 horas anteriores al viaje (MAEC).",
        "Tras la salida de la CEDEAO no ha cambiado nada para los españoles: la gratuidad de visados anunciada en Consejo de Ministros en septiembre de 2025 es SOLO para ciudadanos de países africanos y no tenía fecha de aplicación. El visado común de la AES, llamado «Visa Liptako», sigue en fase de discusión desde las reuniones de expertos de Bamako del 1 y 2 de febrero de 2025 y NO existe.",
        "Validez en frontera terrestre POR CONFIRMAR: el eVisa se concibió para la llegada por el aeropuerto de Uagadugú y no hemos podido verificar en fuente oficial que los puestos terrestres lo admitan sin trámite adicional.",
    ],
    fronteras_rows=[
        ("Aeropuerto internacional", "Uagadugú — Thomas Sankara International (OUA/DFFD), 12,35375 N / 1,512 W", "Única vía de acceso razonable si algún día se hiciera la visita; concentra el 98 % del tráfico comercial del país y está a 1,5 km al sureste del centro. Exige eVisa impreso, fiche de voyage y certificado de fiebre amarilla (Wikipedia; MAEC 19-05-2025)."),
        ("Paso terrestre · Costa de Marfil", "Niangoloko — lado marfileño Laleraba (10,266963 N / 4,925856 W)", "ABIERTO y operativo: mercancías de 6.30 a 18.00 y pasajeros 24/7, todos los días. A 131 km de Bobo-Dioulasso, 2 h 30. Gestiona la Direction Générale des Douanes, con seguimiento electrónico COTRACK. Zona de riesgo extremo para el MAEC (LogCluster LCA)."),
        ("Paso terrestre · Costa de Marfil", "Yendéré", "Segundo paso del eje suroeste hacia Ferkessédougou. Estado operativo 2025-2026 POR CONFIRMAR: no tiene ficha propia en el LCA. Toda la región de Cascades está bajo estado de emergencia (FCDO)."),
        ("Paso terrestre · Mali", "Faramana — lado maliense Kouri", "ABIERTO: mercancías de 6.30 a 18.00 y pasajeros 24/7, solo cierra el 1 de enero. A 44 km de Koundougou. El LCA NO evaluó la carretera «por el aumento de la inseguridad en esta zona, con presencia de grupos terroristas y riesgo de emboscada y secuestro». Sin coordenadas publicadas."),
        ("Paso terrestre · Mali", "Koloko — lado maliense Hèrèmakono (11,091976 N / 5,328377 W)", "ABIERTO: mercancías de 6.00 a 18.00 y pasajeros 24/7. A 132 km de Bobo-Dioulasso, 2 h 45 en turismo. La nacional N8 está asfaltada pero con muchos tramos de baches que obligan a reducir. El LCA no anota aviso de inseguridad específico (LogCluster LCA)."),
        ("Paso terrestre · Togo", "Cinkansé — Poste de Contrôle Juxtaposé (11,115378 N / 0,007538 E)", "ABIERTO: mercancías de 6.30 a 18.00 y pasajeros 24/7. A 105 km de Tenkodogo por la N16. N4 y N16 asfaltadas y en buen estado, pero CINCO puestos de control entre Cinkansé y Uagadugú. El FCDO cita la carretera hacia Togo entre las atacadas (LogCluster LCA)."),
        ("Paso terrestre · Ghana", "Dakola — lado ghanés Paga", "ABIERTO: mercancías de 7.00 a 18.30 y pasajeros 24/7. A 26 km de Pô por la N5, «asfaltada y en buen estado» según el LCA. Es el paso menos expuesto sobre el papel, pero el MAEC desaconseja igualmente todas las zonas fronterizas. Sin coordenadas publicadas."),
        ("Paso terrestre · Benín", "Nadiagou — lado beninés Porga (11,157722 N / 0,839083 E)", "ABIERTO: mercancías de 6.30 a 18.00 y pasajeros 24/7. A 20 km de Pama y 344 km de Uagadugú (7 h). El LCA NO evaluó la carretera por inseguridad desde noviembre de 2021 y la describe «muy dañada, llena de baches». Jefe de puesto: Sr. SALOU, 70 32 40 14."),
        ("Paso terrestre · Níger", "Kantchari — lado nigerino Torodi (12,490685 N / 1,517059 E)", "ABIERTO sobre el papel: mercancías de 6.30 a 18.00 y pasajeros 24/7. A 152 km de Fada N'Gourma. El LCA advierte de que «la carretera a Kantchari es objeto cada vez más frecuente de ataques terroristas» y no la evaluó por riesgo de emboscada y secuestro. Es el peor paso posible."),
        ("Eje interior crítico", "Uagadugú – Bobo-Dioulasso (RN1)", "El MAEC DESACONSEJA expresamente los desplazamientos por carretera en este eje (19-05-2025). En diciembre de 2025 se lanzaron las obras de una autopista de 2x4 carriles, sin efecto sobre la situación actual."),
        ("Eje interior crítico", "Kaya – Dori (165 km, hacia el Sahel)", "Solo se recorre en CONVOY SECURIZADO desde hace más de dos años, con una tasa de 1.500 FCFA por conductor repartida entre transportistas y municipio (Sidwaya, 24 de julio de 2025). Da la medida de lo que significa circular en la mitad norte."),
    ],
    vehiculos=[
        "Se conduce POR LA DERECHA. Permiso de conducción internacional recomendable junto al español; documentación del vehículo siempre a bordo. El seguro de responsabilidad civil frente a terceros es obligatorio en el país, aunque la mayoría de conductores locales no lo tienen (SPF belga).",
        "CPD: no existe organización emisora de carnets de passages en Burkina Faso según carnetdepassage.org. El carnet debe emitirse en el país de matriculación, es decir el RACE en España, y tiene validez de un año desde la emisión.",
        "En frontera, la vía habitual para un vehículo extranjero es la admisión temporal con laissez-passer expedido por la Direction Générale des Douanes. El último importe que hemos podido documentar son 5.000 FCFA en aduana, pero procede de un relato de septiembre de 2011 y hay que reconfirmarlo.",
        "La Carta Verde europea NO tiene validez en Burkina Faso. Hay que contratar seguro local o Carte Brune CEDEAO en el propio paso: el bureau nacional sigue activo en Uagadugú (BP 3233, tel. +226 50 30 69 40, apsab@fasonet.bf) con nueve aseguradoras afiliadas.",
        "La salida de la CEDEAO fue efectiva el 29 de enero de 2025, con un periodo transitorio de seis meses para la libre circulación de personas. Pese a ello, cartebrune.org sigue listando a Burkina Faso como Estado miembro del sistema de seguro y sus noticias, actualizadas hasta el 5 de agosto de 2026, NO mencionan ninguna retirada: la Carte Brune parece seguir sirviendo, pero conviene reconfirmarlo con la aseguradora antes de salir.",
        "En los pasos se aplican tasas de tránsito de mercancías (BSTR/BSTT 2.500 FCFA, BSVN 2.500 FCFA por vehículo, documento único de aduanas). A un vehículo particular no deberían aplicarse todas, pero conviene llevar efectivo en FCFA para lo que salga.",
        "Hay múltiples puestos de control en todos los corredores: cinco solo entre Cinkansé y Uagadugú. El convoy escoltado es obligatorio de facto en el eje Kaya–Dori, y hay que asumir que puede imponerse en otros ejes del norte y del este sin previo aviso.",
        "Red viaria escasa: 12.506 km totales y solo 2.001 km asfaltados, con baches peligrosos, señalización ausente y sin marcas de separación de carriles. Fuera de los ejes principales hace falta 4x4 de verdad.",
        "Conducción nocturna descartada: el FCDO la desaconseja expresamente por el mal estado de la vía y la falta de iluminación, y es cuando se concentran los asaltos armados. El MAEC añade evitar las zonas periféricas de Uagadugú y Bobo-Dioulasso de noche.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Marco legal: Ley n.º 028-2021/AN, de 17 de mayo de 2021, sobre el régimen jurídico aplicable a los drones civiles en Burkina Faso.",
        "Autoridad competente: Agence Nationale de l'Aviation Civile (ANAC-BF). Todo dron debe estar DECLARADO ante la ANAC y autorizado antes de su uso, tanto de ocio como de fotografía o profesional.",
        "Prohibido volar cerca de aeropuertos, sobre campos militares, sobre edificios oficiales, sobre multitudes y de noche sin autorización especial. Hay que mantener el dron a la vista y respetar las altitudes autorizadas.",
        "Sanciones que la propia ANAC enumera: multa, confiscación del dron y acciones judiciales. Existe además prohibición de grabar a personas sin su consentimiento.",
        "La importación del aparato puede exigir autorización previa y declaración a las autoridades; los drones no autorizados se incautan en aduana.",
        "Plazos y tasas exactas de la autorización POR CONFIRMAR: la página de la ANAC no publica ni el formulario ni el importe, y no hemos localizado la circular que los fije.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado a 2026: NO AUTORIZADO. No hay licencia publicada para Starlink en Burkina Faso.",
        "La ARCEP, autoridad reguladora de comunicaciones electrónicas, emitió en marzo de 2024 una advertencia sobre la falta de autorización del servicio y la posibilidad de perseguir a usuarios y revendedores.",
        "El 25 de julio de 2026 la ministra de Transición Digital anunció «avances» en las conversaciones con Starlink, sin calendario, tarifas ni acuerdo definitivo. La importación de terminales sigue técnicamente prohibida, aunque la venta informal continúa.",
        "La alternativa es la SIM local de los operadores móviles (Orange Burkina Faso, Moov Africa, Telecel Faso); cobertura razonable en Uagadugú y Bobo-Dioulasso, escasa en el resto del país.",
        "El FCDO recomienda teléfono satelital por la limitada cobertura telefónica; su régimen de importación en Burkina Faso está POR CONFIRMAR y en la región suele ser sensible.",
    ],
    perro_intro=[
        "Entrada: el portal oficial de trámites service-public.gov.bf recoge la «Demande d'autorisation d'importation des animaux, des produits animaux et des produits d'origine animale», con plazo de 3 a 14 días hábiles y coste variable. Exige solicitud timbrada a la autoridad competente, copia legalizada del pasaporte y los justificantes del caso, pero no detalla nada específico sobre perros.",
        "Documentación que cabe esperar por práctica regional y que hay que confirmar con el servicio veterinario: microchip, vacuna antirrábica en vigor y certificado veterinario internacional reciente. Régimen exacto POR CONFIRMAR: no hemos podido abrir ninguna página nacional del servicio veterinario burkinés que lo desarrolle.",
        "Razas prohibidas o restringidas: sin información en fuente oficial. POR CONFIRMAR.",
        "VUELTA A LA UE: Burkina Faso NO figura en las listas del Reglamento de Ejecución (UE) 2026/636 —el único territorio africano listado es Mauricio—, así que se aplica la vía A del Reglamento Delegado (UE) 2026/131: titulación de anticuerpos antirrábicos hecha ANTES de salir de España y anotada en el pasaporte del animal. Si se hiciera ya en África, hay que esperar tres meses desde la extracción.",
        "Riesgo sanitario alto para el perro: la rabia está presente en el país (TravelHealthPro) y la atención veterinaria de calidad se limita a Uagadugú y Bobo-Dioulasso; fuera de ahí, según la propia guía sanitaria, la asistencia es muy básica y circulan medicamentos falsificados.",
        "Calor extremo: con máximas de hasta 43 °C en marzo y abril, el perro no puede quedarse en el vehículo ni caminar sobre asfalto en horas centrales. En la estación de lluvias, de junio a octubre, aparecen inundaciones y el riesgo de esquistosomiasis en cualquier charca.",
        "En un país excluido por protocolo, el argumento decisivo es operativo: una evacuación de emergencia con animal es prácticamente imposible, porque ninguna de las opciones de salida rápida —vuelo, convoy, evacuación consular— contempla al perro.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "FIEBRE AMARILLA OBLIGATORIA: certificado internacional de vacunación exigido a todo viajero de 9 meses en adelante bajo el Reglamento Sanitario Internacional (TravelHealthPro). Desde julio de 2016 el certificado es válido de por vida.",
        "Malaria de alto riesgo en todo el país y todo el año. TravelHealthPro recomienda quimioprofilaxis con atovacuona/proguanil, doxiciclina o mefloquina; la doxiciclina no es adecuada para menores de 12 años.",
        "Vacunas recomendadas: hepatitis A y B, tétanos, fiebre tifoidea, triple vírica y meningocócica ACWY en determinados grupos. El MAEC añade dengue, polio y meningitis.",
        "Otros riesgos confirmados: cólera con brotes periódicos, dengue frecuente, rabia presente, chikungunya y esquistosomiasis. No bañarse ni vadear agua dulce: la bilharziasis se contrae por contacto con la piel.",
        "Agua y alimentos: precaución estricta. Solo agua embotellada o tratada, también para lavarse los dientes. El MAEC advierte expresamente del riesgo de bilharziasis por agua no tratada.",
        "Hospitales de referencia: CHU Yalgado Ouédraogo en Uagadugú, el principal del país, y CHU Sourou Sanou en Bobo-Dioulasso, con 593 camas, 1.115 empleados, urgencias, traumatología ortopédica, hemodiálisis y resonancia magnética. Fuera de las dos ciudades la asistencia es muy básica.",
        "Para casos complejos se deriva a Abiyán, Accra o París, así que el seguro con repatriación sanitaria es imprescindible, con la salvedad de que la mayoría de pólizas decae al viajar contra la recomendación del MAEC. Las farmacias autorizadas llevan cruz verde; en los mercados informales circulan medicamentos falsificados.",
    ],
    seguridad_intro="Burkina Faso es hoy uno de los países más peligrosos del mundo para un viajero europeo. El MAEC desaconseja el viaje a todo el territorio salvo por extrema necesidad, el FCDO desaconseja todo viaje y Canadá pide evitar todo viaje en su revisión de septiembre de 2026. Hay estado de emergencia en ocho regiones, insurgencia consolidada de JNIM y del Estado Islámico, ataques crecientes con minas en las carreteras principales, ejes que solo se recorren en convoy escoltado y una amenaza muy alta de secuestro de occidentales. No es cuestión de prudencia sino de protocolo: el país queda fuera.",
    seguridad=[
        "MAEC, actualización de 19 de mayo de 2025: «SE DESACONSEJA EL VIAJE SALVO POR RAZONES DE EXTREMA NECESIDAD» para todo el país, con riesgo extremo en las 17 regiones del mapa administrativo de 2025.",
        "Zonas que el MAEC cita expresamente como de riesgo extremo: Kénédugu (Guiriko), Kossi y Sourou, Lorum, Yatenga, Titao (Yaagda), Liptako, Gourma y Kopienga (Goulmou), Diapaga (Tapoa) y Kulpélogo (Nakambé); el eje norte Ouahigouya–Bogandé; y TODAS las zonas fronterizas.",
        "El MAEC clasifica Uagadugú y Bobo-Dioulasso como riesgo medio por delincuencia común, y desaconseja circular de noche por las zonas periféricas. Es el único matiz territorial que existe, y no convierte ninguna zona en visitable.",
        "FCDO: estado de emergencia declarado en Centre-Est, Est, Centre-Nord, Nord, Boucle du Mouhoun, Sahel, Hauts-Bassins y Cascades, es decir también en el suroeste que se suele creer tranquilo. Uagadugú presenta un riesgo terrorista cada vez más elevado.",
        "Grupos activos: JNIM, vinculado a Al Qaeda, y el Estado Islámico. El FCDO señala que los nacionales británicos —y por extensión los europeos— se consideran objetivo legítimo de secuestro, y Canadá indica que los secuestros «ocurren con regularidad», sobre todo cerca de Níger y Mali.",
        "Carreteras: ataques crecientes contra ejes y rutas de transporte «incluido el uso de minas terrestres». Rutas expresamente citadas por el FCDO: hacia y desde Bobo-Dioulasso, Níger, Benín y Togo. El LCA de Naciones Unidas dejó sin evaluar por inseguridad las carreteras de Faramana, Nadiagou y Kantchari.",
        "Convoyes: el eje Kaya–Dori, de 165 km, lleva más de dos años recorriéndose únicamente en convoy securizado, con una tasa de 1.500 FCFA por conductor (Sidwaya, 24 de julio de 2025). Hay que asumir esperas largas e imposibilidad de planificar etapas.",
        "Delincuencia: asaltos armados y delitos contra vehículos en aumento; delincuencia callejera seria en Uagadugú, especialmente en la zona del Rond-point des Nations Unies. El teléfono para agresiones en carretera es el 1010.",
        "Normas prácticas: no fotografiar instalaciones militares ni gubernamentales, llevar siempre identificación, evitar manifestaciones y concentraciones políticas, circular solo de día y con vigilancia alta. Las relaciones homosexuales están penalizadas.",
        "Estacionalidad: la estación de lluvias de junio a octubre provoca inundaciones y corta pistas; suma un factor de bloqueo a un escenario ya inaceptable. El tren Abiyán–Uagadugú está desaconsejado por seguridad según el servicio exterior belga.",
    ],
    agua=[
        "Agua de red NO potable. Para beber, solo embotellada o tratada; el MAEC advierte del riesgo de bilharziasis con agua no tratada y TravelHealthPro confirma esquistosomiasis en el país.",
        "Para llenar depósitos de ducha y lavado, la opción realista son las estaciones de servicio y los hoteles de Uagadugú y Bobo-Dioulasso. Filtro de sedimentos más tratamiento químico o UV obligatorio incluso para uso no alimentario, por el riesgo de contacto con la piel.",
        "No usar agua dulce de ríos, embalses, las cascadas de Karfiguéla ni los lagos del suroeste, ni siquiera para lavar: la esquistosomiasis se contrae por contacto cutáneo, no por ingestión.",
        "El país es semiárido, con unos 800 mm anuales en Uagadugú concentrados de mayo a septiembre. En la estación seca la disponibilidad fuera de las ciudades se reduce mucho y conviene viajar con autonomía completa.",
        "Se han registrado brotes de cólera (MAEC), lo que obliga a tratar cualquier agua de origen local como contaminada por defecto, también la de los depósitos de estación de servicio.",
        "Puntos concretos de llenado POR CONFIRMAR: no hay registros recientes de iOverlander ni de Tracks4Africa que hayamos podido verificar en esta sesión, porque prácticamente nadie ha recorrido el país desde 2019.",
    ],
    combustible=[
        "Gasolina: 850 XOF/litro, equivalentes a 1,51 USD, dato de 12 de enero de 2026 (GlobalPetrolPrices). Es un 9,5 % más cara que la media mundial.",
        "Gasóleo: 675 XOF/litro, equivalentes a 1,23 USD, dato de 9 de febrero de 2026 (GlobalPetrolPrices). Al cambio fijo del franco CFA, unos 1,03 € por litro.",
        "Los precios llevan un año sin variar porque el Gobierno los fija administrativamente. Da estabilidad, pero también riesgo de desabastecimiento cuando el precio regulado no cubre el coste de importación.",
        "Burkina Faso no tiene refinería ni salida al mar: todo el combustible entra por carretera desde los puertos de Abiyán, Lomé, Tema y Cotonú, por los mismos corredores que el FCDO señala bajo ataque. Cualquier corte del corredor se traduce en colas y racionamiento.",
        "Red de estaciones fiable solo en Uagadugú, Bobo-Dioulasso y las capitales regionales del eje central. Fuera de ahí, bidones y venta informal, con riesgo de combustible adulterado. Como referencia histórica, un viajero pagaba 640-690 FCFA/litro en 2011, muy cerca del precio regulado actual.",
        "Episodios concretos de racionamiento en 2025-2026 POR CONFIRMAR: no hemos podido documentarlos en fuente abierta en esta sesión, ni acceder a comunicados de la SONABHY.",
    ],
    experiencias_intro="No hay relatos recientes de overlanders en Burkina Faso: el conflicto ha cerrado la ruta del Sahel y prácticamente nadie la ha recorrido desde 2019. Lo que sigue combina los últimos relatos disponibles con su fecha y la documentación logística y de seguridad que sí está actualizada, con la fuente citada dentro de cada entrada.",
    experiencias=[
        "El corredor que ya no se recorre: Dan Grec, autor de The Road Chose Me, mantiene una categoría dedicada a Burkina Faso de su vuelta a África en Jeep Wrangler (theroadchoseme.com, viaje de 2016-2019), cuando todavía se cruzaba el país de Mali a Ghana. Es el tipo de relato que hoy no tiene continuación: quienes hacen la costa occidental desde 2019 saltan el interior del Sahel y bajan por Senegal, Guinea y Costa de Marfil.",
        "Cuánto costaba entrar con el vehículo: el blog Into the World documenta el cruce Mali–Burkina en septiembre de 2011 con una Yamaha XT660Z Ténéré. Visado en la embajada de Bamako por 47.000 FCFA el mismo día, o 94.000 FCFA en la frontera para 90 días y una entrada, más un laissez-passer de aduanas por 5.000 FCFA. Combustible a 640-690 FCFA/litro y cajeros hasta en pueblos pequeños. Son las únicas cifras de admisión temporal que hemos podido documentar, y tienen quince años.",
        "Dónde dormía uno en Uagadugú: el mismo relato de Into the World señala que no había campings oficiales y que el OK-INN Hotel de Uagadugú dejaba acampar en su aparcamiento previo acuerdo; Overland Diaries cuenta lo mismo en febrero-marzo de 2010, un hotel «con un aparcamiento enorme» donde se acampaba gratis usando el restaurante y la piscina. Esa era la infraestructura de pernocta del país, y no hay nada que indique que siga existiendo.",
        "El país como cruce de caminos, no como destino: Overland Diaries describe su paso de 2010 —Mali, Burkina, Ghana y vuelta— sobre todo como la parada donde se tramitaban los visados de los países siguientes en Uagadugú, y recomienda las cascadas de Banfora y Bobo-Dioulasso. Hoy esa función de hub de visados la cumplen Accra y Abiyán, que es exactamente el motivo por el que el tramo se puede sustituir sin perder nada logístico.",
        "Lo que se visitaba cuando se podía: Andy's World Journeys publicó en mayo de 2020 un repaso de sus dos visitas, una por tierra desde Níger y otra en avión, con Uagadugú, Bobo-Dioulasso y sobre todo Banfora, sus baobabs, sus termiteros y su destilería. El propio autor reconoce que fue «hace más de diez años» y que el país «no ha estado en la mejor estabilidad en años recientes». Es el mejor resumen del desfase entre la guía turística y la realidad.",
        "La carretera que nadie ha evaluado: el Logistics Cluster de Naciones Unidas documenta los pasos de Faramana, Nadiagou y Kantchari y anota en los tres que «la carretera no fue evaluada debido al aumento de la inseguridad en esta zona, con presencia de grupos terroristas y riesgo de emboscada y secuestro» (lca.logcluster.org, evaluaciones vigentes en 2026). Si los equipos humanitarios no recorren un eje, un particular tampoco.",
        "Niangoloko sigue abierto, y eso confunde: la misma evaluación del Logistics Cluster describe el paso de Niangoloko con Costa de Marfil funcionando con normalidad, mercancías de 6.30 a 18.00 y pasajeros 24 horas, a 131 km y dos horas y media de Bobo-Dioulasso. Que la frontera esté abierta y operativa no significa que la carretera que lleva hasta ella sea segura: son dos cosas distintas y es el error clásico al planificar sobre el papel.",
        "Esperar el convoy como forma de vida: el diario burkinés Sidwaya publicó el 24 de julio de 2025 un reportaje sobre el eje Kaya–Dori, 165 km que desde hace más de dos años solo se recorren en convoy securizado, con autobuses y camiones pagando 1.500 FCFA por conductor y una economía entera montada alrededor de la espera. Es la imagen exacta de lo que significa circular en la mitad norte del país.",
        "Minas en las carreteras principales: el FCDO recoge en su aviso de viaje que «los ataques contra carreteras y rutas de transporte por parte de terroristas están aumentando, incluido el uso de minas terrestres», y cita las rutas hacia y desde Bobo-Dioulasso, Níger, Benín y Togo. Para una expedición de 250 km diarios eso elimina de golpe todos los ejes útiles del país.",
        "Sin embajada a la que llamar: el propio FCDO advierte de que «no hay embajada británica en Burkina Faso», de que el apoyo consular se presta a distancia desde Accra y de que no puede garantizar asistencia en una evacuación. España está igual: la competencia es de Bamako, a casi 900 km y en otro país en crisis, con solo un viceconsulado honorario sobre el terreno. Es la lección operativa más repetida por quienes han pasado un susto en el Sahel.",
    ],
    pendientes=[
        ("Validez del eVisa en pasos terrestres", "Confirmación escrita de la Direction Générale de la Police Nationale o del viceconsulado honorario de España en Uagadugú de que el eVisa impreso se admite en Dakola, Niangoloko, Koloko y Cinkansé."),
        ("Visado común AES («Visa Liptako»)", "Comunicado oficial de la Confederación AES o publicación en visaburkina.bf que confirme si el visado se ha lanzado, su tasa, su validez en los tres países y si aplica a europeos. Hoy sigue en discusión desde febrero de 2025 y la página del sitio oficial dedicada al visado AES está publicada pero vacía."),
        ("Gratuidad de visados para africanos", "Verificar si la medida anunciada en Consejo de Ministros en septiembre de 2025 llegó a aplicarse y si en algún momento se extiende a otros pasaportes; a 12 de septiembre de 2025 el portal seguía cobrando."),
        ("Régimen de admisión temporal del vehículo", "Documento de la Direction Générale des Douanes que fije el laissez-passer aplicable a un turismo extranjero, su duración y su coste actual en FCFA. El único importe documentado, 5.000 FCFA, es de 2011."),
        ("Vigencia de la Carte Brune CEDEAO tras la salida", "Nota del bureau nacional de Uagadugú (apsab@fasonet.bf, +226 50 30 69 40) o del Conseil des Bureaux confirmando por escrito si Burkina Faso sigue en el sistema después del 29 de enero de 2025. El sitio oficial lo sigue listando como miembro y no publica nada en contra."),
        ("Requisitos de entrada del perro", "Ficha o circular del servicio veterinario nacional burkinés que detalle microchip, plazo del certificado veterinario, antigüedad de la vacuna antirrábica y si hace falta autorización previa de importación para un animal de compañía."),
        ("Razas de perro prohibidas o restringidas", "Norma nacional publicada; si no existe, declaración expresa del servicio veterinario de que no hay lista de razas vetadas."),
        ("Estado operativo del paso de Yendéré", "Ficha del Logistics Cluster o comunicado aduanero de 2025-2026 que confirme si está abierto a extranjeros y en qué horario; es el único de los pasos relevantes sin ficha propia."),
        ("Coordenadas de Faramana y Dakola", "Obtener las coordenadas de ambos pasos en GeoNames o en una fuente oficial; el Logistics Cluster describe los dos puestos pero no las publica."),
        ("Escolta militar obligatoria fuera del eje Kaya–Dori", "Confirmar con la gendarmería o con el servicio exterior de un país europeo con embajada residente en qué otros ejes se impone convoy y con qué trámite."),
        ("Teléfono operativo de la Embajada de España en Bamako", "El MAEC publica (+223) 20 70 73 50 en Recomendaciones de viaje y (+223) 44 98 24 30 en la Ficha País y en la web de la Embajada. Confirmar cuál está en servicio."),
        ("Coordenadas exactas del viceconsulado honorario y de los hospitales", "Verificar en Google Maps con los anclajes indicados en gmaps_query; las coordenadas actuales son del centro de Uagadugú y no del edificio."),
        ("Racionamiento de combustible 2025-2026", "Noticia o comunicado de la SONABHY que documente episodios de desabastecimiento, su duración y los ejes afectados."),
        ("Régimen de importación de teléfonos satelitales", "Norma de la ARCEP o de aduanas que aclare si un teléfono satelital puede entrarse y usarse legalmente, dado que el FCDO lo recomienda."),
    ],
    sources=SOURCES,
    sources_note="Revisión cerrada el 18 de septiembre de 2026 con las páginas que se pudieron abrir en esa fecha; cada dato de esta ficha procede de una de ellas. Es una herramienta de planificación, no una autorización de viaje ni un sustituto de la consulta oficial: Burkina Faso está desaconsejado por el MAEC, el FCDO y Canadá, y todo lo relativo a visado, aduana y sanidad debe reconfirmarse en la fuente oficial antes de actuar. Donde no se ha podido verificar, la ficha lo dice expresamente y lo recoge en «pendientes».",
    emergency="Emergencia consular 24 h de la Embajada de España en Mali y Burkina Faso, en Bamako: (+223) 73 31 23 24. Centralita: (+223) 44 98 24 30, emb.bamako@maec.es. Viceconsulado honorario en Uagadugú: (+226) 50 33 16 32, CH.OUAGADOUGOU@maec.es. Policía: 17. Bomberos de Uagadugú: 18. Gendarmería de Uagadugú: (+226) 80 00 11 45 y (+226) 25 30 62 71. Agresiones en carretera: 1010. Verificados en el MAEC y en la web de la Embajada.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

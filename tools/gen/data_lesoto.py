# -*- coding: utf-8 -*-
"""Lesoto — ficha completa (12 sep 2026): ALTERNATIVA (no está en la ruta fija),
pero es la más fácil de encajar de las cuatro: es un ENCLAVE dentro de Sudáfrica,
se entra y se sale desde ella y cabe entero dentro del corredor sudafricano.
Es, junto con Namibia, el mejor destino 4x4 del bloque sur."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"
NOFOTO = "Sin fotografía verificada en esta revisión (ver pendientes)"

POIS = [
    dict(n=1, name="Butha-Buthe y la puerta norte", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-28.7667, lon=28.2500,
         desc="Primera ciudad tras el paso fronterizo de Caledonspoort y el arranque de la travesía del norte. Aquí se reposta, se compra y se decide: por un lado sube la A1 hacia los pasos de Moteng y Tlaeeng, por otro se entra a Ts'ehlanyane. El nombre significa «lugar de acostarse» y es donde Moshoeshoe I tuvo su primer asentamiento antes de mudarse a Thaba-Bosiu. Última gasolinera fiable antes de 100 km de montaña.",
         credit=NOFOTO, source=""),
    dict(n=2, name="Parque Nacional de Ts'ehlanyane", cat="Naturaleza", prio="Alta", dog="por confirmar", time="2 noches",
         lat=-28.9170, lon=28.5830,
         desc="El mejor parque de Lesoto y uno de los grandes secretos de África austral: 5.600 hectáreas de naturaleza agreste al pie del paso de Holomo, entre los 1.940 y los 3.112 m, con uno de los poquísimos bosques autóctonos que le quedan al país. Lo llaman así por el BAMBÚ DE MONTAÑA (che-che), del que este parque es probablemente el refugio más importante de toda la cordillera Maloti-Drakensberg. Más de 220 especies de flores, fynbos de montaña que no existe en ningún otro sitio, 24 especies de caza y más de 60 de aves. De aquí sale el sendero de 39 km hasta la reserva de Bokong. A 45 minutos de asfalto desde la frontera de Caledonspoort: es la entrada más cómoda al país. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=3, name="Liphofung · cuevas y arte rupestre", cat="Cultura", prio="Media", dog="por confirmar", time="medio día",
         lat=-28.8670, lon=28.5330,
         desc="Abrigo de arenisca en la subida hacia Oxbow, con pinturas rupestres san y un pequeño centro cultural basotho. Su nombre significa «lugar del eland» y aquí se refugió Moshoeshoe I en sus desplazamientos. Es la parada corta perfecta entre Butha-Buthe y los pasos altos: media hora de visita guiada que explica de golpe las dos capas de historia del país, la de los san cazadores-recolectores y la de los basotho de Moshoeshoe. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=4, name="Paso de Moteng y Oxbow", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="medio día",
         lat=-28.7333, lon=28.6833,
         desc="La primera gran subida de la A1: el paso de Moteng (2.820 m) trepa en horquillas cerradísimas con pendientes que castigan a los camiones y vistas que se abren de golpe sobre los valles del norte. Arriba aparece Oxbow, un puñado de casas junto al río Malibamatso en un anfiteatro de montañas donde nieva de verdad en invierno. Está asfaltado, pero es asfalto de montaña seria: hielo negro de mayo a septiembre, niebla y cero quitamiedos en algunos tramos.",
         credit=NOFOTO, source=""),
    dict(n=5, name="Afriski (paso de Mahlasela) · esquiar en África", cat="Naturaleza", prio="Alta", dog="por confirmar", time="1–2 noches",
         lat=-28.8228, lon=28.7281,
         desc="SÍ, SE PUEDE ESQUIAR EN ÁFRICA. Afriski está a unos 3.050 m en el paso de Mahlasela (3.222 m), es una de las dos únicas estaciones de esquí del África subsahariana y la única de Lesoto: una pista de 1 km con 305 m de desnivel, del 2.917 al 3.222, cañones de nieve y temporada de JUNIO A AGOSTO, que es exactamente cuando el viaje estará en el sur. Fuera de temporada funciona como base de montaña para trail running, bici y senderismo. Aunque no se esquíe, el sitio es un hito absurdo y memorable: nieve, telesquí y bandera de Lesoto a 3.000 m en pleno trópico.",
         credit=NOFOTO, source=""),
    dict(n=6, name="Paso de Tlaeeng · la carretera asfaltada más alta de África austral", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="medio día",
         lat=-28.8700, lon=28.7600,
         desc="Poco después de Afriski, la A1 corona el paso de Tlaeeng a unos 3.275 m: es la CARRETERA ASFALTADA MÁS ALTA DE ÁFRICA AUSTRAL y uno de los puntos de carretera más altos de todo el continente. No hay nada arriba salvo el cartel, el viento y una panorámica de 360 grados sobre las Maloti peladas; en invierno se cubre de nieve y se cierra. Para un viaje que ha atravesado el Sáhara y el ecuador, cruzar aquí a más de 3.200 m con los dos vehículos es uno de los hitos del recorrido. Altitud y coordenadas aproximadas, por confirmar sobre el terreno.",
         credit=NOFOTO, source=""),
    dict(n=7, name="Mokhotlong", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-29.2900, lon=29.0700,
         desc="La ciudad más aislada del país y última base antes del Sani Pass: combustible (no siempre garantizado), tienda, y poco más. Es territorio de pastores a caballo con manta basotho y gorro mokorotlo, y el sitio donde se ve cómo se vive de verdad a 2.400 m. Desde aquí arranca el tramo que hace mítica la travesía: la pista hacia el Sani, y el acceso al Thabana Ntlenyana. Repostar aquí es obligatorio, y conviene llevar garrafa.",
         credit=NOFOTO, source=""),
    dict(n=8, name="Thabana Ntlenyana · el techo de África austral", cat="Naturaleza", prio="Alta", dog="por confirmar", time="1 día",
         lat=-29.4670, lon=29.2670,
         desc="3.482 m: el pico más alto de África al sur del Kilimanjaro, y se sube ANDANDO, sin material técnico. Está en la cresta de Mohlesi, justo al norte del Sani Pass, y se ataca desde Sani Top o desde la carretera de Mokhotlong en una caminata larga de un día por pradera de altura, sin sendero marcado y con el viento como único obstáculo serio. No hay cumbre más fácil de alcanzar con un techo tan alto en todo el continente. Niebla frecuente: brújula y GPS obligatorios, y ropa de abrigo de verdad aunque sea verano.",
         credit=NOFOTO, source=""),
    dict(n=9, name="Sani Pass · el acceso 4x4 mítico", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-29.5881, lon=29.2927,
         desc="EL TRAMO 4x4 MÁS FAMOSO DE ÁFRICA AUSTRAL. La pista sube 1.332 m —de 1.544 a 2.876 m— por la pared del Drakensberg en una sucesión de horquillas de grava con RAMPAS DE HASTA EL 33% (1:3). Sudáfrica solo permite subirlo en 4x4; el puesto fronterizo está arriba del todo, en la cima, lo que significa que todo el paso está técnicamente en territorio sudafricano y solo se entra en Lesoto al coronar. Los dos puestos abren de 6:00 a 18:00 y NO SE PUEDE CRUZAR FUERA DE ESE HORARIO. Se ha ido asfaltando por fases desde el lado sudafricano (los primeros 14 km en 2012, y una segunda fase casi terminada en 2021), pero el tramo final sigue siendo grava, y el paso ha costado vidas: por el camino se ven restos de vehículos que no lo consiguieron.",
         credit="Wikimedia Commons", source=W + "Lesotho%20-%20South%20Africa%20Border%20-%20Sani%20Pass.jpg?width=900"),
    dict(n=10, name="Sani Top · el pub más alto de África", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="1 noche",
         lat=-29.5836, lon=29.2879,
         desc="Justo al coronar el Sani Pass, a 2.874 m, está el Sani Mountain Lodge y su bar, que se anuncia como EL PUB MÁS ALTO DE ÁFRICA: chimenea encendida, cerveza Maluti y un ventanal sobre el precipicio por el que se acaba de subir. Es el premio clásico de la travesía y una de las pocas «instituciones» del overland africano que está a la altura de su fama. Hay alojamiento y sitio para acampar, y desde aquí salen las caminatas al Thabana Ntlenyana y por el borde del escarpe. Dormir arriba tiene además una ventaja práctica: se evita la carrera contra el cierre de la frontera a las 18:00. Coordenadas aproximadas, por confirmar.",
         credit="Wikimedia Commons", source=W + "Sani%20Pass%20Lesotho%202.jpg?width=900"),
    dict(n=11, name="Presa de Katse", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-29.3370, lon=28.5061,
         desc="La obra que explica la economía del país: una presa de arco de hormigón de 185 m de altura y 710 m de coronación sobre el río Malibamatso, la SEGUNDA MÁS ALTA DE ÁFRICA y la de mayor altitud del continente (1.993 m). Forma parte del Lesotho Highlands Water Project, que vende agua a Sudáfrica —unos 30 m³ por segundo— a cambio de unos 35 millones de dólares anuales más royalties. Terminada en 1996, costó 8.000 millones de dólares. Se visita con guía por dentro del muro, hay centro de visitantes y un jardín botánico de plantas alpinas rescatadas antes de la inundación, y el embalse serpentea entre montañas peladas creando una de las conducciones más espectaculares del país.",
         credit=NOFOTO, source=""),
    dict(n=12, name="Paso de Mafika Lisiu y reserva de Bokong", cat="Naturaleza", prio="Alta", dog="por confirmar", time="medio día",
         lat=-29.2500, lon=28.3500,
         desc="La subida a Katse desde Pitseng corona el paso de MAFIKA LISIU a unos 3.090 m, otro de los grandes puertos asfaltados del país, con un mirador en lo alto sobre un mar de crestas. Justo arriba está la Reserva Natural de Bokong, el centro de visitantes más alto de África austral, colgado sobre el barranco del Lepaqoa, cuya cascada SE CONGELA EN INVIERNO formando una columna de hielo de decenas de metros. Desde aquí sale el sendero de 39 km hasta Ts'ehlanyane. Altitud y coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=13, name="Presa de Mohale y su carretera", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="medio día",
         lat=-29.4670, lon=28.0830,
         desc="La segunda presa del Lesotho Highlands Water Project, de escollera y unos 145 m, conectada con Katse por un túnel de trasvase de 32 km. Lo interesante para el viaje no es la presa sino LA CARRETERA: la A3 de Maseru a Mohale es una obra de ingeniería que trepa y se descuelga por cornisas con vistas continuas, y es la forma más bonita de entrar al interior montañoso desde la capital. Hay mirador, centro de información y alojamiento junto al embalse. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=14, name="Maseru", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-29.3100, lon=27.4800,
         desc="La capital, pegada al río Caledon y a la frontera del Maseru Bridge, es la única base logística de verdad del país: bancos, supermercados sudafricanos, talleres, hospitales y las oficinas donde se tramitan permisos. No es una ciudad monumental, pero tiene el mercado de artesanía basotho, la catedral y el Basotho Hat, y es el sitio para repostar, comprar y resolver papeleo antes de meterse en la montaña. Todo lo que falta aquí se compra al otro lado del puente, en Ladybrand (Sudáfrica), a 20 km.",
         credit="Wikimedia Commons", source=W + "Maseru%2C%20Lesotho.jpg?width=900"),
    dict(n=15, name="Thaba-Bosiu · la montaña fortaleza de Moshoeshoe", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="medio día",
         lat=-29.3503, lon=27.6714,
         desc="LA CUNA DE LA NACIÓN BASOTHO, a 24 km de Maseru. En julio de 1824 Moshoeshoe I, huyendo de las guerras del Mfecane, subió con su gente a esta meseta de arenisca de 2 km² y 1.804 m rodeada de cortados verticales, con ocho manantiales dentro y solo seis pasos de acceso — el principal, el de Khubelu. La llamó «montaña de la noche» porque llegaron de noche. Desde aquí resistió los asedios de los ndebele, los bóeres y los británicos, y aquí nació Lesoto como estado, razón por la que es el único país del sur de África que nunca fue absorbido por Sudáfrica. Moshoeshoe I y Moshoeshoe II están enterrados arriba. Se sube a pie con guía desde el centro de información; hay aldea cultural y alojamiento en rondavel al pie.",
         credit=NOFOTO, source=""),
    dict(n=16, name="Morija · museo y huellas de dinosaurio", cat="Cultura", prio="Media", dog="permitido con condiciones", time="medio día",
         lat=-29.6333, lon=27.5000,
         desc="El pueblo de la primera misión evangélica francesa (1833), que trajo la imprenta y fijó por escrito el sesotho: aquí está el Museo y Archivos de Morija, el mejor museo del país, con paleontología, etnografía e historia basotho, y la imprenta más antigua de Lesoto. En las lajas de arenisca de los alrededores hay HUELLAS DE DINOSAURIO perfectamente visibles, y a media hora a pie se llega a la colina de Makhoarane con vistas sobre todo el valle. En septiembre u octubre celebra el festival de artes de Morija, el evento cultural más importante del país.",
         credit=NOFOTO, source=""),
    dict(n=17, name="Malealea", cat="Cultura", prio="Alta", dog="por confirmar", time="2 noches",
         lat=-29.8500, lon=27.6167,
         desc="Una vieja tienda comercial de 1905 convertida en lodge en un valle de montaña, y el sitio donde la mayoría de los viajeros descubre el LESOTO A CABALLO: los ponis basotho, pequeños, duros y criados para estas laderas, son aquí el medio de transporte normal, y se hacen salidas de un día o de varios con guías del pueblo, durmiendo en aldeas. También hay senderos a pie a cascadas, pinturas rupestres y la garganta de Ribaneng. El acceso se hace por el «Gates of Paradise Pass», donde una placa dice: «Vas ahora a entrar en la Puerta del Paraíso». Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=18, name="Semonkong y la cascada de Maletsunyane", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-29.8686, lon=28.0517,
         desc="EL SALTO Y EL RÉCORD. La cascada de Maletsunyane cae 192 M DE UN SOLO CHORRO en un anfiteatro de basalto, y la nube de agua pulverizada que levanta da nombre al pueblo: Semonkong, «el lugar del humo». Desde el borde, el Semonkong Lodge opera el DESCENSO EN RÁPEL COMERCIAL MÁS LARGO DEL MUNDO según el Guinness: 204 m de cuerda, más altos que la propia cascada. Aunque no se haga, el pueblo es el mejor sitio del país para ver la vida basotho real: los jinetes bajan al mercado envueltos en mantas y con el poni cargado, y en invierno todo se cubre de nieve. Hay ruta a caballo hasta la base del salto y senderos a otras dos cascadas.",
         credit=NOFOTO, source=""),
    dict(n=19, name="Quthing (Moyeni) · las huellas de dinosaurio", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="medio día",
         lat=-30.4001, lon=27.7002,
         desc="La ciudad más meridional del país, a 1.500 m sobre el río Senqu (el Orange en su cabecera) y junto a la frontera del Tele Bridge con el Cabo Oriental. A la entrada, y prácticamente al borde de la carretera, hay un yacimiento de HUELLAS DE DINOSAURIO del Jurásico Inferior grabadas en la arenisca, de las más accesibles de África: se ven las pisadas de tres dedos sin necesidad de caminar nada. Cerca está la Masitise Cave House, una casa misionera de 1866 CONSTRUIDA DENTRO DE UN ABRIGO DE ROCA, hoy pequeño museo, y hay arte rupestre san por toda la comarca. Quthing fue fundada en 1877, abandonada en la Guerra de los Fusiles de 1880 y reconstruida después.",
         credit=NOFOTO, source=""),
    dict(n=20, name="Parque Nacional de Sehlabathebe", cat="Patrimonio UNESCO", prio="Alta", dog="prohibido", time="2–3 noches",
         lat=-29.8989, lon=29.1211,
         desc="El rincón más salvaje y remoto de Lesoto: 69,5 km² a una altitud media de 2.400 m, en el extremo sureste contra el escarpe del Drakensberg, dentro del bien Patrimonio de la Humanidad de MALOTI-DRAKENSBERG que Lesoto comparte con Sudáfrica. Es un paisaje surrealista de praderas de altura, formaciones de arenisca erosionadas en arcos y setas, lagunas y cascadas, con 65 YACIMIENTOS DE ARTE RUPESTRE SAN identificados y el pez endémico amenazado maluti redfin. Casi no hay nadie: fauna escasa y esquiva (rhebok, chacales, quizá algún íbice), pero silencio absoluto. El acceso es por pista dura desde Qacha's Nek o Sehonghong, y desde el parque se puede bajar a pie a Sudáfrica por el paso de Bushman's Nek (solo peatonal).",
         credit=NOFOTO, source=""),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul", "cultura": "morado",
              "patrimonio unesco": "marron", "costa": "turquesa"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = ("https://commons.wikimedia.org/wiki/File:" + _m.group(1)) if _m else ""
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Caledonspoort (con Sudáfrica, Free State)", "Frontera", -28.6833, 28.3667,
     "Entrada norte, desde Fouriesburg/Clarens: la puerta cómoda del país y la más cercana a Ts'ehlanyane (45 minutos de asfalto). Horario amplio (aprox. 06:00–22:00, confirmar). Coordenadas aproximadas."),
    ("Frontera · Maseru Bridge (con Sudáfrica, Free State)", "Frontera", -29.3167, 27.4667,
     "El paso principal del país, junto a la capital y a 20 km de Ladybrand. ABIERTO 24 HORAS. Es el más transitado y el de trámite más formal: la referencia si hay que resolver papeleo."),
    ("Frontera · Sani Pass (con Sudáfrica, KwaZulu-Natal)", "Frontera", -29.5836, 29.2879,
     "El puesto está ARRIBA DEL TODO, en la cima del paso, a 2.874 m. Abre de 6:00 a 18:00 en ambos lados y no se cruza fuera de horario. Sudáfrica exige 4x4 para subir. Es la salida espectacular del país hacia el Drakensberg de KZN."),
    ("Frontera · Qacha's Nek (con Sudáfrica, Cabo Oriental)", "Frontera", -30.1167, 28.6833,
     "Puerta del sureste y acceso rodado a Sehlabathebe. Horario limitado. Alternativa: Ramatseliso's Gate, más al este y más cerca del parque, pero con pista dura. Coordenadas aproximadas."),
    ("Frontera · Tele Bridge (con Sudáfrica, Cabo Oriental)", "Frontera", -30.4333, 27.7333,
     "Paso del extremo sur junto a Quthing, hacia Sterkspruit. Útil para entrar o salir por el sur combinando con las huellas de dinosaurio. Coordenadas aproximadas."),
    ("Embajada de España en Pretoria (competente para Lesoto)", "Consular", -25.7500, 28.2333,
     "No hay representación española en Lesoto: la competencia es de la Embajada de España en Pretoria (Sudáfrica). Comprobar teléfono de emergencia consular vigente antes de entrar."),
    ("Queen 'Mamohato Memorial Hospital, Maseru", "Hospital", -29.3100, 27.4800,
     "Principal hospital de referencia del país. Para cualquier cosa seria, la práctica es evacuación a Bloemfontein o Johannesburgo (Sudáfrica), que están cerca: es una de las ventajas de que Lesoto sea un enclave."),
    ("Combustible · Butha-Buthe, Maseru, Mokhotlong, Thaba-Tseka, Semonkong, Quthing", "Combustible", -29.3100, 27.4800,
     "Red escasa y de fiabilidad variable en la montaña. Repostar SIEMPRE que se pueda y llevar garrafas: entre Butha-Buthe y Mokhotlong por la A1, y en el interior (Thaba-Tseka, Semonkong, Sehlabathebe), la disponibilidad no está garantizada."),
    ("Agua potable y de uso general · Maseru, Butha-Buthe, Semonkong", "Agua potable", -29.3100, 27.4800,
     "Agua embotellada en Maseru y en las cabeceras de distrito. El agua de los arroyos de altura es de las más limpias del continente (es la que Lesoto vende a Sudáfrica), pero hay ganado por todas partes: filtrar y potabilizar siempre. Lodges de Semonkong, Malealea y Ts'ehlanyane permiten llenar el depósito de uso general."),
]

DRONE_CALLOUT = ("warn", "Menos restrictivo que Uganda o Ruanda, pero con reglas propias: registro y autorización de la LCAA",
                 "Lesoto regula los drones a través de la Lesotho Civil Aviation Authority (LCAA), con registro y autorización previa para el uso de aeronaves no tripuladas. El régimen es sensiblemente menos duro que el de Uganda o Ruanda —no hay historial conocido de requisas sistemáticas en frontera— pero tampoco es libre: no se vuela sobre el aeropuerto de Moshoeshoe I, instalaciones gubernamentales, presas (Katse y Mohale son infraestructura estratégica vendida a Sudáfrica: NO volar ahí) ni dentro de las áreas protegidas sin permiso. El régimen exacto está POR CONFIRMAR con la LCAA: está en los pendientes.")

STARLINK_CALLOUT = ("warn", "Disponibilidad por confirmar — la red terrestre de Vodacom Lesotho es el respaldo real",
                    "El estado de Starlink en Lesoto debe confirmarse antes del viaje: el país es pequeño y montañoso, y la disponibilidad comercial no se ha podido verificar en esta revisión. Lo que sí funciona es la red móvil de Vodacom Lesotho y Econet Telecom Lesotho, con buena cobertura en Maseru y las cabeceras de distrito y cobertura irregular en los pasos altos y los valles profundos. Una SIM sudafricana en roaming es cara pero a veces engancha desde las crestas. Criterio del proyecto: no depender de la conexión en el interior montañoso y avisar de los planes antes de entrar.")

DOG_MATRIX = [
    ("Sehlabathebe (Patrimonio UNESCO Maloti-Drakensberg)", "prohibido",
     "Parque nacional dentro de un bien Patrimonio de la Humanidad: no admite mascotas. Plan B: dejarlo en Qacha's Nek con uno de los tres viajeros, o planificar el parque como bloque de dos o tres días con turnos."),
    ("Ts'ehlanyane, Bokong y las reservas gestionadas", "por confirmar",
     "No hay grandes depredadores en Lesoto —no hay leones, ni elefantes, ni búfalos—, así que la prohibición típica de los parques del sur de África NO tiene aquí la misma justificación de seguridad. Algunas reservas gestionadas por el Lesotho Northern Parks admiten perro con correa y otras no. HAY QUE PREGUNTAR PARQUE POR PARQUE: está en los pendientes y es una de las mejores oportunidades del viaje para ver naturaleza con el perro."),
    ("Sani Pass, Tlaeeng, Mafika Lisiu y toda la travesía de montaña", "permitido con condiciones",
     "LO MEJOR DE LESOTO CON EL PERRO: los pasos, las crestas y los valles son terreno abierto, sin recinto y sin fauna peligrosa. Se puede caminar con él prácticamente en todas partes. Cuidado con los PERROS PASTORES basotho, que son territoriales y van sueltos con los rebaños, y con el frío nocturno: por encima de 3.000 m se hiela de verdad."),
    ("Semonkong, Malealea, Morija, Thaba-Bosiu", "permitido con condiciones",
     "Lodges y aldeas acostumbrados a animales; varios alojamientos admiten perro — confirmar por escrito antes. Thaba-Bosiu se sube a pie por un camino abierto: en principio sin problema con correa."),
    ("Maseru, Butha-Buthe, Mokhotlong, Quthing", "permitido con condiciones",
     "Sin problema con correa. Hay veterinarios en Maseru, pero para cualquier cosa seria lo sensato es cruzar a Ladybrand o Bloemfontein (Sudáfrica), que están muy cerca."),
    ("Frontera · régimen SACU", "por confirmar",
     "Lesoto está en la Unión Aduanera de África Austral (SACU) con Sudáfrica, Namibia, Botsuana y Esuatini. LA PREGUNTA CLAVE DEL PROYECTO: si el permiso interterritorial de movimiento sudafricano (gratuito, tres sellos, ventana de 7 días para cruzar y 30 días de repatriación) cubre la ida y la vuelta Sudáfrica→Lesoto→Sudáfrica, o si hace falta un permiso de importación sudafricano NUEVO para reentrar, porque el permiso sudafricano es de UNA SOLA EXPEDICIÓN. Ver los pendientes: es lo que hay que resolver por escrito antes de entrar."),
]

SOURCES = [
    ("The Travelling Sloth · guía overland de Lesoto", "https://www.thetravellingsloth.com/lesotho-overlanding-travel-guide/"),
    ("Toone's Travels · guía de conducción del Sani Pass 2025", "https://www.chris-toone.com/blog/self-driving-sani-pass-guide"),
    ("Embajada de España en Pretoria · consulados y competencias", "https://www.exteriores.gob.es/Embajadas/pretoria/es/Embajada/Paginas/Consulados.aspx"),
    ("Visit Lesotho · web oficial de turismo (Lesotho Tourism Development Corporation)", "https://www.visitlesotho.travel/"),
    ("UNESCO · Parque Maloti-Drakensberg, Patrimonio de la Humanidad (incluye Sehlabathebe)", "https://whc.unesco.org/en/list/985/"),
    ("Wikipedia · Sani Pass (altitud, rampas de 1:3, horario de frontera 6:00-18:00, asfaltado por fases)", "https://en.wikipedia.org/wiki/Sani_Pass"),
    ("Wikipedia · Cataratas de Maletsunyane (192 m) y el rápel comercial más largo del mundo (204 m)", "https://en.wikipedia.org/wiki/Maletsunyane_Falls"),
    ("Wikipedia · Presa de Katse (185 m, segunda más alta de África, Lesotho Highlands Water Project)", "https://en.wikipedia.org/wiki/Katse_Dam"),
    ("Wikipedia · Thabana Ntlenyana (3.482 m, se sube andando)", "https://en.wikipedia.org/wiki/Thabana_Ntlenyana"),
    ("Wikipedia · Parque Nacional de Sehlabathebe (69,5 km², 65 yacimientos de arte rupestre)", "https://en.wikipedia.org/wiki/Sehlabathebe_National_Park"),
    ("Wikipedia · Thaba Bosiu (Moshoeshoe I, julio de 1824, 1.804 m)", "https://en.wikipedia.org/wiki/Thaba_Bosiu"),
    ("Wikipedia · Afriski (3.050 m, temporada de junio a agosto, paso de Mahlasela 3.222 m)", "https://en.wikipedia.org/wiki/Afriski"),
    ("Wikipedia · Parque Nacional de Ts'ehlanyane (bambú de montaña, sendero de 39 km a Bokong)", "https://en.wikipedia.org/wiki/Ts%27ehlanyane_National_Park"),
    ("Wikipedia · Quthing / Moyeni (huellas de dinosaurio, Masitise Cave House, Tele Bridge)", "https://en.wikipedia.org/wiki/Quthing"),
    ("Wikipedia · Lesoto (único país enteramente por encima de 1.000 m; punto más bajo a 1.400 m; SACU)", "https://en.wikipedia.org/wiki/Lesotho"),
    ("Wikipedia · Política de visados de Lesoto (exención para ciudadanos de la UE; eVisa con tramitación suspendida)", "https://en.wikipedia.org/wiki/Visa_policy_of_Lesotho"),
    ("iOverlander · puntos de combustible, agua y acampada verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África austral", "https://tracks4africa.co.za/"),
]

# Travesía del norte: entrada por Caledonspoort, A1 por los pasos altos y salida por el Sani
CORRIDOR = [(-28.6833, 28.3667), (-28.7667, 28.2500), (-28.9170, 28.5830), (-28.8670, 28.5330),
            (-28.7333, 28.6833), (-28.8228, 28.7281), (-28.8700, 28.7600), (-29.2900, 29.0700),
            (-29.4670, 29.2670), (-29.5836, 29.2879), (-29.5881, 29.2927)]

# Bucle interior y sur: entrada por Maseru Bridge, presas, Semonkong, Quthing y salida por el sureste
CORRIDOR_ALT = [(-29.3167, 27.4667), (-29.3100, 27.4800), (-29.3503, 27.6714), (-29.4670, 28.0830),
                (-29.2500, 28.3500), (-29.3370, 28.5061), (-29.5333, 28.6167), (-29.8686, 28.0517),
                (-29.8500, 27.6167), (-29.6333, 27.5000), (-30.4001, 27.7002), (-30.1167, 28.6833),
                (-29.8989, 29.1211)]

HISTORIA_RESUMEN = ("Lesoto existe porque una montaña resultó inexpugnable: en 1824 Moshoeshoe I refugió a su gente en la meseta de Thaba-Bosiu, resistió las guerras del Mfecane, a los bóeres y a los británicos, y consiguió que su reino sobreviviera "
                    "como protectorado británico separado en lugar de ser absorbido por lo que sería Sudáfrica. Independiente desde 1966, es hoy una monarquía constitucional, el único país del mundo enteramente por encima de los 1.000 metros, "
                    "y una economía que vive de vender agua a su vecino, de la confección textil y de las remesas de sus mineros.")

HISTORIA_SECCIONES = [
    ("Los san y los primeros basotho",
     "Antes que nadie estuvieron los san, cazadores-recolectores cuyo arte rupestre cubre los abrigos de arenisca de todo el país: solo en Sehlabathebe se han catalogado 65 yacimientos, y hay más en Liphofung, Quthing y las gargantas de Malealea. "
     "A partir del siglo XVII, grupos de habla sesotho fueron poblando las tierras altas, dedicados al ganado y al cultivo del sorgo en los valles."),
    ("Moshoeshoe I y la montaña de la noche",
     "Las guerras del Mfecane de las primeras décadas del siglo XIX desarticularon toda la región. En julio de 1824, un jefe llamado Moshoeshoe condujo a sus seguidores hasta la meseta de Thaba-Bosiu —2 km² de arenisca con cortados verticales, ocho manantiales dentro y solo seis accesos— "
     "y la convirtió en capital y fortaleza. Desde allí acogió a refugiados de todos los clanes dispersos, y de esa agregación nació la nación basotho. Resistió los asedios de los ndebele, de los bóeres del Estado Libre de Orange y de los británicos."),
    ("Protectorado, guerra de los fusiles e independencia",
     "En 1868, acosado por los bóeres, Moshoeshoe pidió la protección británica: Basutolandia se convirtió en protectorado, lo que le costó la mitad de las tierras bajas fértiles (el «territorio conquistado», hoy en Sudáfrica) pero le salvó la existencia como entidad separada. "
     "En 1880 la Guerra de los Fusiles enfrentó a los basotho con la administración del Cabo, que quería desarmarlos; los basotho ganaron. Esa doble historia —resistencia y protectorado— es la razón de que Lesoto sea hoy un país independiente rodeado por Sudáfrica, y no una provincia más. "
     "La independencia llegó el 4 de octubre de 1966."),
    ("El país moderno: agua, mantas y montaña",
     "Lesoto es una monarquía constitucional con una historia política reciente de golpes, inestabilidad e intervenciones militares sudafricanas, hoy razonablemente estabilizada. Su gran activo es el agua: el Lesotho Highlands Water Project, con las presas de Katse y Mohale, "
     "vende a Sudáfrica unos 30 m³ por segundo a cambio de unos 35 millones de dólares anuales. La confección textil y las remesas de los mineros completan el cuadro. Culturalmente, la manta basotho y el sombrero mokorotlo —que está en la bandera— "
     "siguen siendo prendas de uso diario, y el poni basotho continúa siendo transporte real en las aldeas sin carretera. Es un país con una de las tasas de VIH más altas del mundo, dato que conviene conocer sin que afecte a la seguridad del viajero."),
]

HISTORIA_FUENTES = [
    ("BBC News · Lesotho country profile", "https://www.bbc.com/news/world-africa-13031816"),
    ("Encyclopaedia Britannica · Lesotho, History", "https://www.britannica.com/place/Lesotho/History"),
    ("UNESCO · Parque Maloti-Drakensberg (Lesoto comparte el bien con Sudáfrica)", "https://whc.unesco.org/en/list/985/"),
    ("Wikipedia · Thaba Bosiu, la fortaleza de Moshoeshoe I", "https://en.wikipedia.org/wiki/Thaba_Bosiu"),
]

SPEC = dict(
    slug="lesoto", name="Lesoto", revision="12 sep 2026",
    sub="ALTERNATIVA — pero la más fácil de encajar: ENCLAVE dentro de Sudáfrica · el mejor 4x4 del bloque sur después de Namibia",
    chips=[
        ("ESTATUS", "ALTERNATIVA — no está en la ruta fija, pero cabe entera dentro del corredor sudafricano"),
        ("COSTE DEL DESVÍO", "+900 km y +8-11 días (travesía completa norte-sur)"),
        ("VERSIÓN CORTA", "+350 km y +3-4 días: solo el Sani Pass y el norte"),
        ("VISADO", "NO HACE FALTA: españoles y ciudadanos de la UE, exentos — la condición del dueño se cumple sin trámite"),
        ("ENTRADA/SALIDA", "Siempre desde Sudáfrica: Caledonspoort, Maseru Bridge, Sani Pass, Qacha's Nek, Tele Bridge"),
        ("4x4", "SANI PASS: 1.332 m de desnivel con rampas de hasta el 33%"),
        ("EL PUB MÁS ALTO DE ÁFRICA", "Sani Top, 2.874 m"),
        ("ALTITUD", "Único país del mundo entero por encima de 1.000 m; su punto MÁS BAJO está a 1.400"),
        ("ESQUÍ", "Afriski, 3.050 m, temporada JUN-AGO — justo cuando el viaje estará en el sur"),
        ("PERRO", "SIN grandes depredadores: la mejor oportunidad del sur para caminar con él"),
    ],
    center=[-29.6, 28.3], zoom=8,
    notice="Documento de planificación de una ALTERNATIVA que aún no está decidida, aunque es la de encaje más sencillo de las cuatro. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Norte · la travesía del Techo de África",
    corridor_alt_label="Oeste y sur · el bucle interior",
    hero_img=W + "Sani%20Pass%20Lesotho%202.jpg?width=900",
    hero_credit="Sani Pass · Wikimedia Commons",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("LESOTO NO ESTÁ EN LA RUTA FIJA, pero es la alternativa MÁS FÁCIL DE ENCAJAR de las cuatro, y con diferencia. "
              "(1) VISADO: no hace falta ninguno. Los ciudadanos españoles y del resto de la UE están EXENTOS de visado para entrar en Lesoto; existe un sistema de eVisa desde 2017, pero su tramitación electrónica ha llegado a estar suspendida y, en cualquier caso, no aplica a quien está exento. "
              "La condición que el dueño puso —«si tienen eVisa»— aquí se cumple de la forma más cómoda posible: no hay trámite previo, se sella el pasaporte en el puesto terrestre y se entra. Confirmar la duración exacta de la exención (habitualmente 90 días) antes de entrar. "
              "(2) TIEMPO: es un ENCLAVE DENTRO DE SUDÁFRICA, así que no hay que ir a buscarlo: se entra por un lado, se atraviesa y se sale por otro, y se sigue estando en el corredor sudafricano. "
              "La travesía completa norte-sur son unos 900 km y 8-11 días. La versión mínima —subir el Sani Pass desde KwaZulu-Natal, dormir arriba, ver el norte y bajar por Caledonspoort— son unos 350 km y 3-4 días, y ya justifica el desvío por sí sola. "
              "(3) POR QUÉ ENTRA: es, junto con Namibia, el MEJOR DESTINO 4x4 DEL BLOQUE SUR. El Sani Pass es el tramo 4x4 más famoso de África austral; el Tlaeeng es la carretera asfaltada más alta de África austral; "
              "y el país entero está por encima de los 1.000 m, con el punto más bajo a 1.400. Además NO HAY GRANDES DEPREDADORES —ni leones, ni elefantes, ni búfalos—, lo que convierte a Lesoto en la mejor oportunidad de todo el bloque sur para caminar por naturaleza abierta CON EL PERRO. "
              "(4) LA ÚNICA PEGA REAL ES ADUANERA, NO DE RUTA: el permiso de importación de animales sudafricano es de UNA SOLA EXPEDICIÓN, así que hay que confirmar por escrito si el permiso interterritorial de movimiento de la SACU cubre la salida y el regreso, "
              "o si hace falta un permiso sudafricano nuevo para reentrar con el perro. Eso es lo que hay que resolver antes, y está en los pendientes."),
    facts=[
        ("Estatus", "ALTERNATIVA, no ruta fija — pero de encaje trivial: es un enclave dentro de Sudáfrica y se entra y se sale desde ella."),
        ("Coste en ruta", "Travesía completa norte-sur: ~900 km y 8-11 días. Versión mínima (Sani Pass y el norte): ~350 km y 3-4 días. Cálculo sobre 250 km/día, con la advertencia de que en Lesoto los kilómetros valen doble: son todos de montaña."),
        ("Visado", "CONFIRMADO: ciudadanos de la UE, incluidos los españoles, EXENTOS de visado. Sin trámite previo, sin eVisa. Confirmar duración exacta de la exención (habitualmente 90 días) y llevar pasaporte con validez de 6 meses."),
        ("Entrada y salida", "Siempre desde Sudáfrica. Norte: Caledonspoort (la más cómoda). Capital: Maseru Bridge (24 h). Este: Sani Pass (solo 4x4, 6:00-18:00). Sureste: Qacha's Nek y Ramatseliso's Gate. Sur: Tele Bridge."),
        ("El tramo 4x4", "SANI PASS: sube 1.332 m (de 1.544 a 2.876) con rampas de hasta el 33% (1:3). Sudáfrica solo permite subirlo en 4x4. El puesto fronterizo está EN LA CIMA y cierra a las 18:00."),
        ("Altitud", "Único estado independiente del mundo situado ENTERAMENTE por encima de los 1.000 m. Su punto más bajo, a 1.400 m, es el punto más bajo más alto de cualquier país del planeta."),
        ("Esquí", "Afriski, a unos 3.050 m en el paso de Mahlasela: una de las dos únicas estaciones de esquí del África subsahariana. Temporada de JUNIO A AGOSTO, que coincide con el paso del viaje por el sur."),
        ("Moneda y aduana", "El loti está a la par con el rand sudafricano y el rand circula con normalidad. Lesoto está en la SACU: no hay aranceles internos, pero SÍ hay control fronterizo de personas, vehículos y animales."),
        ("Vehículo", "Se conduce por la IZQUIERDA, igual que en Sudáfrica. Seguro sudafricano: CONFIRMAR que cubre Lesoto; si no, se compra en frontera. Carné internacional recomendable."),
        ("Perro", "NO HAY GRANDES DEPREDADORES en Lesoto. La prohibición típica de los parques del sur aquí no tiene la misma justificación: hay que preguntar reserva por reserva, y es la mejor oportunidad del bloque sur para caminar con él."),
        ("Drones", "Régimen de la LCAA, menos duro que el de Uganda o Ruanda, pero con registro y autorización. NO volar sobre las presas de Katse y Mohale. Por confirmar el detalle."),
        ("Clima", "Nieve frecuente en las tierras altas de mayo a septiembre, y posible todo el año en las cumbres. Si el viaje pasa en invierno austral, hay que contar con hielo negro, pasos cerrados y noches muy por debajo de cero."),
    ],
    alerts=[
        "ESTATUS ALTERNATIVA: no está en la ruta fija. Pero como es un enclave dentro de Sudáfrica, es la de decisión más barata: se puede decidir sobre la marcha, ya estando en el corredor sudafricano.",
        "INVIERNO AUSTRAL: el viaje pasará por el sur entre junio y agosto, que es exactamente la temporada de NIEVE en Lesoto. Es una oportunidad (Afriski, cascadas congeladas, paisajes blancos) y un riesgo real: hielo negro en los pasos de Moteng, Tlaeeng y Mafika Lisiu, cierres temporales de carretera, y noches de −10 °C o menos a 3.000 m. Cadenas, anticongelante, sacos de invierno y calefacción en los vehículos.",
        "SANI PASS: el puesto fronterizo abre de 6:00 a 18:00 EN AMBOS LADOS. Si se sube tarde y no se corona a tiempo, no se cruza. Sudáfrica exige 4x4 para la subida. Rampas de hasta el 33% y grava en el tramo final: bajar en primera corta y usar freno motor, no el pedal.",
        "COMBUSTIBLE: es el problema logístico real del país. La red es escasa y la disponibilidad en la montaña (Mokhotlong, Thaba-Tseka, Semonkong, Sehlabathebe) no está garantizada. Repostar siempre que se pueda y llevar garrafas llenas.",
        "PERRO Y ADUANA SACU: el permiso de importación sudafricano es de UNA SOLA EXPEDICIÓN. Hay que confirmar POR ESCRITO si el permiso interterritorial de movimiento de la SACU (gratuito, tres sellos, ventana de 7 días para cruzar y 30 días de repatriación) cubre el viaje de ida y vuelta, o si hace falta un permiso sudafricano NUEVO para volver a entrar con el perro. Es el único punto que puede complicar el desvío.",
        "PERROS PASTORES: los rebaños de las tierras altas van con perros territoriales sueltos. Es el riesgo más concreto para nuestro perro en todo el país, muy por encima de cualquier fauna salvaje. Llevarlo con correa cerca de los rebaños.",
        "ALTITUD: se circula de forma continuada por encima de los 2.500 m y se cruzan pasos de más de 3.200. Los motores pierden potencia (los turbodiésel lo notan menos), y hay que contar con mal de altura leve en quien no esté aclimatado.",
        "Pistas interiores: fuera de la A1 y de las carreteras de las presas, la red es de tierra y en mal estado, con vados sin puente que se vuelven intransitables con la lluvia de verano (dic-feb, tormentas fuertes).",
        "Sanidad: Lesoto tiene una de las tasas de VIH más altas del mundo y una red sanitaria limitada. Para cualquier cosa seria, la solución es salir a Sudáfrica (Bloemfontein o Johannesburgo), que están cerca. Comprobar que el seguro cubre la evacuación transfronteriza.",
        "Delincuencia: baja en general, pero hay hurtos y algún robo de vehículo en Maseru. Aparcamiento vigilado en la capital y prudencia estándar; en la montaña, el país es notablemente seguro.",
    ],
    ruta_intro=("Dos travesías que no se solapan y que se pueden hacer por separado o encadenadas, porque Lesoto es un enclave y siempre se entra y se sale desde Sudáfrica. La del norte es la clásica «Roof of Africa»: se entra por Caledonspoort, "
                "se sube la A1 por los pasos de Moteng, Mahlasela y Tlaeeng —el asfalto más alto de África austral—, se cruza el altiplano hasta Mokhotlong y se sale bajando el Sani Pass al Drakensberg de KwaZulu-Natal. "
                "La del sur entra por Maseru Bridge y recorre el interior: Thaba-Bosiu, las presas de Mohale y Katse por el paso de Mafika Lisiu, Semonkong y su cascada de 192 m, Malealea y los ponis, las huellas de dinosaurio de Quthing "
                "y el remoto Sehlabathebe. Etapas sobre 250 km/día, con la advertencia de que aquí un kilómetro de montaña vale por dos de llanura."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada norte", "Caledonspoort → Butha-Buthe → Ts'ehlanyane", "~60 km · 2-3 días"),
        ("2 · Cuevas y subida", "Ts'ehlanyane → Liphofung → paso de Moteng → Oxbow", "~60 km · 1 día"),
        ("3 · Nieve en África", "Oxbow → Afriski (Mahlasela, 3.222 m) → paso de Tlaeeng (3.275 m)", "~25 km · 1-2 días"),
        ("4 · El altiplano", "Tlaeeng → Mokhotlong", "~110 km · 1 día"),
        ("5 · El techo del sur", "Mokhotlong → Thabana Ntlenyana (3.482 m, a pie) → Sani Top", "~90 km + caminata de 1 día · 2-3 días"),
        ("6 · Salida mítica", "Sani Top (pub más alto de África) → bajada del Sani Pass → KwaZulu-Natal", "~35 km · 1 día (cruzar antes de las 18:00)"),
        ("7 · Entrada oeste", "Maseru Bridge → Maseru (compras, combustible, papeleo)", "~5 km · 1-2 días"),
        ("8 · La cuna de la nación", "Maseru → Thaba-Bosiu → vuelta", "~50 km · medio día"),
        ("9 · Las presas", "Maseru → presa de Mohale → paso de Mafika Lisiu (3.090 m) → Bokong → presa de Katse", "~230 km · 2-3 días"),
        ("10 · El corazón vacío", "Katse → Thaba-Tseka → Semonkong (pista dura)", "~200 km · 2 días"),
        ("11 · El salto de 192 m", "Semonkong: cascada de Maletsunyane, rápel de 204 m, ruta a caballo", "2 días de parada"),
        ("12 · Los ponis", "Semonkong → Malealea (Gates of Paradise Pass)", "~60 km · 2 días"),
        ("13 · Museo y dinosaurios", "Malealea → Morija (museo y huellas) → Mohale's Hoek", "~90 km · 1-2 días"),
        ("14 · El sur profundo", "Mohale's Hoek → Quthing (huellas de dinosaurio, Masitise)", "~60 km · 1 día"),
        ("15 · Al rincón remoto", "Quthing → Qacha's Nek → Sehlabathebe", "~180 km · 2 días de pista"),
        ("16 · Patrimonio UNESCO", "Sehlabathebe: arte rupestre san, arcos de arenisca, lagunas", "2-3 días de parada"),
        ("17 · Salida sureste", "Sehlabathebe → Ramatseliso's Gate o Qacha's Nek → Sudáfrica", "~60-120 km · 1 día"),
    ],
    offroad=[
        "SANI PASS (el mítico): 1.332 m de desnivel en pocos kilómetros por la pared del Drakensberg, con rampas de hasta el 33% (1:3), grava suelta, horquillas de radio mínimo y precipicio sin protección. Sudáfrica solo autoriza la subida a vehículos 4x4. Reductora obligatoria, bajar con freno motor y no tocar el pedal, y contar con que el puesto de la cima cierra a las 18:00. Por el camino se ven restos de vehículos que no lo consiguieron: no es folclore.",
        "SANI PASS A MOKHOTLONG (la continuación que casi nadie hace): coronado el paso, la pista sigue por el altiplano hasta Mokhotlong entre aldeas de pastores, vados y baches. Es donde empieza el Lesoto de verdad y donde el 4x4 deja de ser un capricho.",
        "LA A1 DE LOS PASOS ALTOS (Butha-Buthe → Moteng → Mahlasela → Tlaeeng → Mokhotlong): está ASFALTADA, pero es asfalto de alta montaña con pendientes brutales, curvas de herradura y, en invierno, hielo negro y nieve. El Tlaeeng, a unos 3.275 m, es la carretera asfaltada más alta de África austral. Es la ruta de la carrera de enduro «Roof of Africa».",
        "PASO DE MAFIKA LISIU (unos 3.090 m, Pitseng → Katse): el gran puerto de la carretera de las presas, con mirador arriba y la reserva de Bokong colgada sobre el barranco del Lepaqoa. Asfaltado y espectacular.",
        "KATSE → THABA-TSEKA → SEMONKONG: el cruce del interior, y el tramo de pista de tierra más largo y duro del país. Vados sin puente, roca suelta, aldeas sin combustible. Es la travesía que separa a quien viene a ver el Sani de quien viene a ver Lesoto.",
        "ACCESO A SEHLABATHEBE (desde Qacha's Nek o Sehonghong): pista de montaña dura y lenta hasta el rincón más remoto del país. Con lluvia, los vados obligan a esperar.",
        "GATES OF PARADISE PASS (acceso a Malealea): corto, con grava y una placa en lo alto que anuncia la entrada a «la Puerta del Paraíso». Manejable, pero con pendiente.",
        "AVISO DE INVIERNO: entre mayo y septiembre, cualquiera de estos pasos puede estar nevado o helado. Cadenas y, sobre todo, criterio: si el Tlaeeng está cerrado, se da la vuelta.",
    ],
    senderismo=[
        "THABANA NTLENYANA (3.482 m): el pico más alto de África al sur del Kilimanjaro y SE SUBE ANDANDO, sin material técnico. Caminata larga de un día desde Sani Top o desde la carretera de Mokhotlong, por pradera de altura sin sendero marcado. Brújula y GPS obligatorios por la niebla; ropa de abrigo aunque sea verano.",
        "Borde del escarpe desde Sani Top: caminatas de medias jornadas por el filo del Drakensberg, asomándose 1.000 m sobre KwaZulu-Natal. Lo mejor que se puede hacer a pie sin comprometerse a una cumbre, y PERFECTO PARA HACER CON EL PERRO.",
        "Sendero Ts'ehlanyane – Bokong (39 km): la travesía a pie clásica del norte, de dos o tres días entre las dos reservas, por bambú de montaña y valles de altura. Se puede hacer también a caballo.",
        "Cascada de Maletsunyane (Semonkong): sendero hasta el mirador del salto de 192 m y bajada a la poza de la base (unas 3-4 horas ida y vuelta, con desnivel serio). Y la variante a caballo, que es como se hace tradicionalmente.",
        "EL RÁPEL COMERCIAL MÁS LARGO DEL MUNDO: 204 m de descenso por la pared de Maletsunyane, operado por el Semonkong Lodge y reconocido por el Guinness. Más alto que la propia cascada. No es senderismo, pero es la actividad a pie más memorable del país.",
        "Sehlabathebe: red de senderos por praderas de altura, arcos de arenisca erosionada, lagunas y cascadas, con 65 yacimientos de arte rupestre san catalogados. Se puede bajar caminando a Sudáfrica por el paso de Bushman's Nek (solo peatonal).",
        "Thaba-Bosiu: subida a pie de una hora con guía local a la meseta de Moshoeshoe, con las tumbas reales arriba y el relato de los asedios. Corta, histórica y accesible.",
        "Malealea: senderos de un día a la garganta de Ribaneng, a pinturas rupestres y a cascadas, además de las rutas de varios días a caballo durmiendo en aldeas.",
        "Bokong: pasarela sobre el barranco del Lepaqoa y sendero a la cascada, que EN INVIERNO SE CONGELA entera formando una columna de hielo — hay quien la escala.",
        "Morija: subida a la colina de Makhoarane (media hora) con vistas sobre el valle, y paseo a las lajas con huellas de dinosaurio.",
        "Rutas a caballo en poni basotho (Malealea, Semonkong, Ts'ehlanyane): en Lesoto el caballo no es una atracción turística, es el transporte de las aldeas sin carretera. Salidas de un día o de varios con guías locales.",
    ],
    acampada=[
        "Sani Top: se puede acampar junto al Sani Mountain Lodge, a 2.874 m, con el pub más alto de África al lado. Frío de verdad por la noche todo el año.",
        "Ts'ehlanyane: camping del parque y el Maliba Lodge; el entorno más cómodo y bonito del norte.",
        "Afriski: alojamiento de estación de montaña, con aparcamiento; útil como base en invierno.",
        "Semonkong Lodge: campings junto al río, con caballos, y organización de las actividades del salto. Uno de los mejores sitios del país para parar varios días.",
        "Malealea Lodge: camping y rondavels en un valle precioso, con programa comunitario del pueblo (música y danza por la tarde).",
        "Katse: alojamiento y zona de acampada junto al embalse, con centro de visitantes.",
        "Sehlabathebe: acampada libre dentro del parque y una lodge básica; sin servicios, hay que entrar autosuficiente.",
        "Thaba-Bosiu: rondavels y camping al pie de la meseta.",
        "AVISO GENERAL: en Lesoto se puede acampar casi en cualquier sitio con permiso del jefe de la aldea, que es la costumbre local y se pide directamente. La altitud manda: incluso en verano, de noche hace frío.",
    ],
    visado=[
        "CIUDADANOS DE LA UE, INCLUIDOS LOS ESPAÑOLES: EXENTOS DE VISADO. No hace falta tramitar nada antes de entrar: se sella el pasaporte en el puesto fronterizo terrestre.",
        "CRITERIO DEL DUEÑO — VÁLIDO POR TIERRA: sí, y de la forma más cómoda posible. Lesoto tiene un sistema de eVisa desde mayo de 2017, pero su tramitación electrónica ha llegado a estar SUSPENDIDA y, en cualquier caso, no afecta a quien está exento. La condición «si tienen eVisa» se cumple aquí por la vía de no necesitarla.",
        "Confirmar la duración exacta de la exención antes de entrar (habitualmente 90 días, con variantes de 14 días para algunas nacionalidades) en el portal de inmigración de Lesoto o en la Alta Comisión.",
        "Pasaporte con validez mínima de 6 meses y páginas libres para los sellos de entrada y salida.",
        "IMPORTANTE: aunque Lesoto esté en la SACU con Sudáfrica, HAY CONTROL FRONTERIZO REAL de personas, vehículos y animales. Salir de Sudáfrica a Lesoto es una salida y una entrada a efectos del visado sudafricano: comprobar que el visado o la estancia autorizada de Sudáfrica permite reentrar después.",
    ],
    fronteras_rows=[
        ("Entrada norte (preferente)", "Caledonspoort (Free State)", "Desde Fouriesburg/Clarens. La puerta más cómoda, a 45 minutos de asfalto de Ts'ehlanyane. Horario amplio pero NO 24 h: confirmar."),
        ("Entrada/salida capital", "Maseru Bridge (Free State)", "ABIERTO 24 HORAS, el más transitado. A 20 km de Ladybrand. Es la referencia si hay que resolver papeleo del perro o de los vehículos."),
        ("Salida este (la mítica)", "Sani Pass (KwaZulu-Natal)", "Puesto EN LA CIMA a 2.874 m. Abre 6:00–18:00 en ambos lados. Sudáfrica exige 4x4 para la subida. Es la salida espectacular del país."),
        ("Entrada/salida sureste", "Qacha's Nek (Cabo Oriental)", "Acceso rodado a Sehlabathebe. Horario limitado. Alternativa: Ramatseliso's Gate, más cerca del parque pero con pista dura."),
        ("Entrada/salida sur", "Tele Bridge (Cabo Oriental)", "Junto a Quthing, hacia Sterkspruit. Útil para combinar con las huellas de dinosaurio del sur."),
        ("Otros pasos", "Ficksburg Bridge, Maputsoe, Van Rooyen's Gate, Makhaleng Bridge", "Hay una veintena de pasos menores con Sudáfrica, muchos con horario corto y algunos solo peatonales. Confirmar horario y aptitud para vehículo antes de contar con cualquiera de ellos."),
    ],
    vehiculos=[
        "Se conduce por la IZQUIERDA, igual que en Sudáfrica: no hay cambio de lado al entrar.",
        "SEGURO: comprobar si la póliza sudafricana cubre Lesoto. Muchas pólizas del sur de África cubren los países de la SACU, pero hay que verlo por escrito; si no, hay seguro de frontera.",
        "El vehículo extranjero paga una tasa de circulación / road levy al entrar: importe pequeño, en rand o loti. Por confirmar el importe vigente.",
        "CPD: al estar en la SACU con Sudáfrica, el trámite de vehículo suele ser un permiso temporal simple en el puesto; confirmar si se exige presentar el CPD y sellarlo, para no romper la cadena de sellos del cuaderno.",
        "Carné de conducir internacional recomendable junto con el nacional.",
        "Vehículo de montaña de verdad: reductora, neumáticos con flanco reforzado, freno motor y frenos en buen estado. Las bajadas largas de los pasos calientan los frenos más que las subidas los motores.",
        "En invierno: cadenas, anticongelante adecuado y gasóleo de invierno. Las noches a 3.000 m gelifican el gasóleo de verano.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Registro y autorización previa ante la Lesotho Civil Aviation Authority (LCAA): régimen POR CONFIRMAR en su detalle, sensiblemente menos restrictivo que el de Uganda o Ruanda.",
        "NO VOLAR sobre las presas de Katse y Mohale: son infraestructura estratégica del Lesotho Highlands Water Project y la sensibilidad es alta.",
        "No volar sobre el aeropuerto internacional de Moshoeshoe I, instalaciones gubernamentales ni el palacio real.",
        "Dentro de Sehlabathebe (Patrimonio de la Humanidad) y del resto de áreas protegidas, pedir autorización expresa a la gestión del parque.",
        "En terreno abierto de montaña, y siempre con el trámite de la LCAA resuelto, Lesoto es de los mejores sitios del viaje para el dron: paisaje espectacular y espacio aéreo vacío. Pero primero el papel.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Disponibilidad comercial de Starlink en Lesoto: POR CONFIRMAR antes del viaje. No darla por hecha.",
        "Red móvil de Vodacom Lesotho y Econet Telecom Lesotho: buena en Maseru y en las cabeceras de distrito, irregular en los pasos altos y mala en los valles profundos y en Sehlabathebe.",
        "Desde las crestas altas a veces engancha la red sudafricana en roaming (caro, pero útil como salida de emergencia).",
        "Criterio del proyecto: dejar dicho el plan de ruta antes de entrar en el interior montañoso y no contar con conexión entre Katse, Thaba-Tseka y Semonkong.",
    ],
    perro_intro=[
        "Lesoto está en la SACU con Sudáfrica, Namibia, Botsuana y Esuatini: según el dosier del proyecto, la entrada terrestre del perro es PROBABLE bajo régimen SACU, con permiso de importación de los servicios veterinarios (Department of Livestock Services, Ministry of Agriculture, Maseru).",
        "LA PREGUNTA CRÍTICA, y es aduanera, no de Lesoto: el permiso de importación SUDAFRICANO es «válido por un periodo limitado y para UNA SOLA EXPEDICIÓN». Si se sale de Sudáfrica a Lesoto y se vuelve a entrar, hay que saber si sirve el permiso interterritorial de movimiento de la SACU (gratuito, con tres sellos —veterinario propio, veterinario estatal local y veterinario estatal de destino—, ventana de 7 días para cruzar y plazo de repatriación de 30 días) o si hace falta un permiso de importación sudafricano NUEVO.",
        "Testimonio útil del dosier: en el caso de Esuatini, el permiso nombraba el país de destino y los funcionarios de frontera QUISIERON QUEDÁRSELO en lugar de devolverlo. Pedir copia sellada o llevar un permiso por país.",
        "Certificado veterinario internacional, vacuna antirrábica en vigor y vacunaciones anuales sin saltarse ningún año (el permiso de movimiento de la SACU lo exige expresamente).",
        "Veterinarios en Maseru; para cualquier cosa seria, cruzar a Ladybrand o Bloemfontein (Sudáfrica), que están a una o dos horas. La cercanía de la red veterinaria sudafricana es una gran ventaja de este desvío.",
        "LO BUENO: en Lesoto NO HAY GRANDES DEPREDADORES. No hay leones, ni elefantes, ni búfalos, ni hipopótamos. La prohibición estándar de los parques del sur de África no tiene aquí la misma base de seguridad, y hay que preguntar reserva por reserva en lugar de darla por supuesta.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "SIN MALARIA: la altitud elimina el riesgo en todo el país. Es uno de los poquísimos destinos de la ruta donde no hace falta profilaxis antipalúdica.",
        "Fiebre amarilla: certificado exigido solo si se procede de país endémico. Viniendo de Sudáfrica, no aplica.",
        "MAL DE ALTURA: se circula de forma continuada por encima de los 2.500 m y se duerme a 2.874 en Sani Top o a 3.050 en Afriski. Subir con calma, hidratarse y no encadenar el primer día de altitud con una cumbre.",
        "FRÍO: el riesgo sanitario real del país. De mayo a septiembre hay nieve, y las noches a 3.000 m bajan de −10 °C. Hipotermia y congelaciones son posibles si se sale a caminar mal equipado.",
        "Agua: los arroyos de altura son de las aguas más limpias del continente (es lo que el país vende a Sudáfrica), pero hay ganado por todas partes. Filtrar y potabilizar siempre.",
        "Lesoto tiene una de las tasas de VIH más altas del mundo y una red sanitaria limitada: el Queen 'Mamohato Memorial Hospital de Maseru es la referencia nacional, pero la solución real para cualquier urgencia seria es salir a Bloemfontein o Johannesburgo. Comprobar que el seguro cubre la evacuación transfronteriza.",
    ],
    seguridad_intro=("Lesoto es un país tranquilo y notablemente seguro en la montaña, donde el riesgo real no es la delincuencia ni la fauna sino el TERRENO Y EL CLIMA: pasos de más de 3.000 m, hielo, niebla, pistas sin protección y "
                     "una red de servicios muy escasa. La prudencia aquí consiste en conducir bien y en no quedarse sin combustible, no en vigilar la mochila."),
    seguridad=[
        "El mayor riesgo del país es la CONDUCCIÓN DE MONTAÑA: pendientes muy fuertes, horquillas sin quitamiedos, hielo negro de mayo a septiembre, niebla repentina y ganado en la calzada. No conducir de noche bajo ningún concepto, criterio general del proyecto y aquí más que en ningún sitio.",
        "SANI PASS: bajar en marcha corta con freno motor. Los frenos recalentados son la causa habitual de los accidentes del paso, no la falta de tracción.",
        "Combustible: quedarse sin gasóleo en el interior montañoso es un problema serio de verdad, no una molestia. Repostar siempre que se pueda y llevar garrafas.",
        "Perros pastores territoriales sueltos con los rebaños: el riesgo más concreto para nuestro perro. Correa cerca de los rebaños.",
        "Delincuencia baja en general. En Maseru hay hurtos y algún robo de vehículo: aparcamiento vigilado y nada de valor a la vista. En la montaña, el país es muy seguro y la gente extraordinariamente hospitalaria.",
        "Costumbre local: para acampar fuera de sitios establecidos se pide permiso al jefe de la aldea. Es lo correcto y además la mejor garantía de tranquilidad nocturna.",
        "Estabilidad política: Lesoto ha tenido episodios de inestabilidad e intervenciones militares en el pasado reciente. Hoy la situación es tranquila, pero conviene consultar la recomendación oficial antes de entrar y evitar concentraciones.",
        "Niños pidiendo dulces o dinero en los pasos de montaña: es habitual y pacífico. Criterio del proyecto: no repartir dinero desde el vehículo en marcha.",
    ],
    agua=[
        "Maseru y las cabeceras de distrito: agua embotellada en supermercados (cadenas sudafricanas).",
        "Recarga del depósito de uso general: lodges y campings de Ts'ehlanyane, Semonkong, Malealea, Katse y Sani Top permiten llenar con manguera; confirmar en recepción.",
        "Arroyos de altura: el agua de Lesoto es la que se vende a Sudáfrica y es de excelente calidad, pero hay ganado en todas las cuencas. Filtrar y potabilizar siempre antes de beber.",
        "En invierno hay que contar con tuberías y depósitos congelados por la mañana: llenar por la tarde, no al amanecer.",
    ],
    combustible=[
        "EL PUNTO DÉBIL DEL PAÍS. La red es escasa y la disponibilidad en el interior no está garantizada: puede haber estación sin suministro durante días.",
        "Eje norte: repostar A TOPE en Butha-Buthe. Entre Butha-Buthe y Mokhotlong (~180 km de montaña) la única opción intermedia poco fiable es Oxbow/Afriski. En Mokhotlong hay estación, pero puede estar seca.",
        "Eje sur y central: repostar en Maseru, que es donde el suministro es seguro. Thaba-Tseka, Semonkong y Qacha's Nek tienen estación pero con disponibilidad irregular.",
        "Antes de Sehlabathebe hay que entrar con autonomía completa de ida y vuelta: allí no hay nada.",
        "Alternativa siempre disponible: salir a repostar a Sudáfrica. Es la ventaja de ser un enclave — Ladybrand, Fouriesburg, Underberg o Sterkspruit están a poca distancia de los respectivos pasos.",
        "Presupuestar un consumo notablemente superior al de llanura: la montaña continua y la altitud penalizan mucho.",
    ],
    experiencias_intro=("Relatos y datos recogidos de la comunidad overland y de guías de conducción especializadas. No son información oficial: contrastar siempre la fecha antes de confiar en un dato de frontera, pista o parque. "
                        "En esta revisión no se ha podido acceder a iOverlander ni a Tracks4Africa desde la sesión de trabajo, así que lo que sigue procede de guías de viaje publicadas, del dosier canino del propio proyecto y de fuentes documentales, y está marcado como tal:"),
    experiencias=[
        "El Sani Pass es el tramo del que todo el mundo escribe, y la advertencia repetida en las guías de conducción es siempre la misma: el problema no es subir, es BAJAR. Marcha corta, freno motor, no tocar el pedal, y contar con que el tramo final sigue siendo grava pese al asfaltado por fases desde el lado sudafricano.",
        "El horario de la frontera es lo que más gente pilla: 6:00 a 18:00 en ambos lados. Quien empieza la subida a media tarde se arriesga a no coronar a tiempo. La solución que todos recomiendan es dormir arriba, en Sani Top, y cruzar al día siguiente con el día entero por delante.",
        "El pub más alto de África cumple: chimenea, cerveza Maluti y un ventanal sobre el precipicio. Es de las pocas «instituciones» del overland africano que no decepciona, y además resuelve el problema del horario de frontera.",
        "La queja recurrente de quien solo hace el Sani es que se pierde el país: el Sani es la puerta, pero Lesoto empieza al otro lado. Quien atraviesa de Mokhotlong a Katse y baja a Semonkong coincide en que ese es el viaje de verdad, y en que hay que contar con pista de tierra durante días.",
        "El combustible aparece en todos los relatos como el problema práctico número uno: estaciones sin suministro, sobre todo en Mokhotlong, Thaba-Tseka y Semonkong. La regla que repite todo el mundo es repostar siempre que se pueda y llevar garrafas.",
        "El invierno divide opiniones: unos dicen que la nieve convierte a Lesoto en el sitio más increíble de África y otros avisan de pasos cerrados y noches infernales. Las dos cosas son ciertas, y el viaje pasará por el sur justo en esa ventana (junio-agosto).",
        "Afriski sorprende a todo el mundo: una pista de esquí de 1 km a 3.000 m en pleno sur de África, con cañones de nieve y gente esquiando en junio. Aunque no se esquíe, la foto y el contraste con el resto del viaje valen la parada.",
        "Los ponis basotho no son una atracción: son el transporte. En Malealea y Semonkong se hacen salidas de uno o varios días con guías del pueblo, durmiendo en aldeas, y es la forma de llegar a valles a los que no llega ninguna carretera.",
        "Perro (dosier del proyecto): la entrada terrestre es PROBABLE bajo el régimen de la SACU. El testimonio documentado de cruces terrestres con perro dentro de la SACU —«cruzar la frontera dentro de la SACU no había sido difícil»— es la mejor noticia de todo el bloque sur. El aviso: el permiso nombra el país de destino y en la frontera han intentado quedárselo.",
        "La ventaja de ser un enclave, que nadie menciona hasta que la necesita: cualquier problema serio —mecánico, médico, veterinario, de suministro— se resuelve saliendo a Sudáfrica, que nunca está a más de unas horas. Lesoto es, seguramente, el destino remoto más seguro de todo el viaje.",
    ],
    pendientes=[
        ("DECISIÓN DE FONDO", "Decidir si entra y en qué versión: travesía completa (~900 km, 8-11 días) o solo el Sani Pass y el norte (~350 km, 3-4 días). Se puede decidir sobre la marcha, ya en el corredor sudafricano"),
        ("PERRO · el punto crítico", "Confirmar POR ESCRITO con DALRRD (VetPermits@daff.gov.za) si el permiso interterritorial de movimiento de la SACU cubre la salida y la reentrada Sudáfrica→Lesoto→Sudáfrica, o si hace falta un permiso de importación sudafricano NUEVO. El permiso sudafricano es de UNA SOLA EXPEDICIÓN"),
        ("Perro · permiso de Lesoto", "Escribir al Department of Livestock Services (Ministry of Agriculture, Maseru) pidiendo confirmación de entrada terrestre y NOMBRANDO el puesto (Caledonspoort, Maseru Bridge o Sani Pass)"),
        ("Perro · parques", "Preguntar UNO A UNO a Ts'ehlanyane, Bokong y Sehlabathebe si admiten perro con correa: al no haber grandes depredadores, la prohibición estándar del sur de África puede no aplicar aquí. Es la mejor oportunidad del bloque sur para ver naturaleza con el perro"),
        ("Visado", "Confirmar la duración exacta de la exención para españoles (habitualmente 90 días) y comprobar que salir de Sudáfrica a Lesoto no compromete la reentrada en Sudáfrica"),
        ("Seguro del vehículo", "Verificar por escrito si la póliza sudafricana cubre Lesoto; si no, prever seguro de frontera"),
        ("CPD", "Confirmar si el cuaderno se sella en la frontera de Lesoto o si basta el permiso temporal de la SACU, para no romper la cadena de pares de sellos"),
        ("Ventana de invierno", "Decidir si se entra en pleno invierno austral (jun-ago: nieve, Afriski, cascadas heladas, pero hielo y pasos cerrados) o si se busca un hueco de primavera. Llevar cadenas y gasóleo de invierno si se entra en la ventana fría"),
        ("Sani Pass", "Planificar la subida para coronar con margen antes de las 18:00, y reservar en Sani Top si se quiere dormir arriba"),
        ("Combustible", "Confirmar disponibilidad real en Mokhotlong, Thaba-Tseka y Semonkong poco antes, y presupuestar garrafas llenas para toda la travesía interior"),
        ("Dron", "Confirmar con la Lesotho Civil Aviation Authority el régimen exacto de registro y autorización. No volar en ningún caso sobre las presas de Katse y Mohale"),
        ("Starlink", "Confirmar disponibilidad comercial en Lesoto: no se ha podido verificar en esta revisión"),
        ("FOTOGRAFÍAS", "En esta revisión NO se pudo acceder a commons.wikimedia.org desde la sesión (bloqueo de red), así que solo tres PDIs llevan foto verificada. Pendiente: completar los nombres de archivo de Wikimedia Commons de los 17 PDIs restantes, verificándolos uno a uno. No inventarlos"),
        ("Coordenadas aproximadas", "Verificar sobre el terreno o con cartografía las coordenadas marcadas como aproximadas: Ts'ehlanyane, Liphofung, Tlaeeng, Mafika Lisiu, Mohale, Malealea, Sani Top y los pasos fronterizos"),
    ],
    sources=SOURCES,
    sources_note=("Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. "
                  "LESOTO ES UNA ALTERNATIVA: no está en la ruta fija, pero es la de encaje más sencillo de las cuatro porque es un enclave dentro de Sudáfrica. Horarios de frontera, disponibilidad de combustible y estado de los pasos en invierno hay que revalidarlos poco antes de entrar."),
    emergency="Sin representación española en Lesoto — competencia de la Embajada de España en Pretoria (Sudáfrica); confirmar el teléfono de emergencia consular vigente antes de entrar. Emergencias locales en Lesoto: policía 123 (Maseru) / 112, ambulancia 121. Para urgencias graves, la vía real es la evacuación a Bloemfontein o Johannesburgo.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

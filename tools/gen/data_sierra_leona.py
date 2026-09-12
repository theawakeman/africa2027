# -*- coding: utf-8 -*-
"""Sierra Leona — ficha completa, ALTERNATIVA: bucle opcional insertado en la SUBIDA (12 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== TRAMO 1 · ENTRADA DESDE GUINEA, FREETOWN Y LA PENÍNSULA =====
    dict(n=1, name="Gbalamuya / Kambia · la puerta de entrada", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=9.1167, lon=-12.9167,
         desc="Gbalamuya es el puesto fronterizo principal del país, justo enfrente del guineano de Pamelap, en la carretera Conakry-Freetown: es el paso que usa prácticamente todo el tráfico regional y el único documentado con garantías. A 15 km está Kambia, capital de distrito, primera población con mercado, combustible, cambio de moneda y alojamiento elemental. Aquí es donde se resuelve la entrada: control de inmigración (el visado a la llegada se expide en este puesto, ver la sección de visado), aduana del vehículo, seguro Brown Card de la CEDEAO y el certificado de fiebre amarilla, que se comprueba. La web oficial de turismo avisa de que el cruce puede llevar varias horas por colas y trámites, y recomienda cruzar siempre de día. Coordenada del puesto aproximada: confirmar sobre el terreno.",
         credit="Wikimedia Commons", source=W + "Cotton%20Tree%20(Sierra%20Leone).jpg?width=900"),
    dict(n=2, name="Freetown · la ciudad de los libertos", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=8.4840, lon=-13.2299,
         desc="Capital y única base logística de talla nacional: el mayor puerto natural de África, bancos con cajero, supermercados, talleres, hospitales y las embajadas. Fundada en 1792 por colonos negros llegados de Nueva Escocia —antiguos esclavos que habían luchado con los británicos en la guerra de independencia americana— y ampliada después con africanos liberados de barcos negreros interceptados por la Marina Real: de ahí la cultura krio, angloafricana y urbana, que sigue siendo la seña de identidad de la ciudad. AVISO IMPORTANTE Y ACTUALIZADO: el célebre Cotton Tree, el árbol del algodón bajo el que rezaron los colonos de 1792 y que aparecía en los billetes del país, SE DERRUMBÓ en gran parte el 24 de mayo de 2023 durante una tormenta. Sobreviven parte del tronco y una gran agalla con hojas, y el gobierno trasladó la parte caída a un museo para convertirla en monumento. Ya no se viene a ver el árbol: se viene a ver lo que queda y el lugar. Lo demás sigue en pie: el Big Market, la St John's Maroon Church, la King Jimmy Market a pie de mar, el Museo Nacional y el caos vivísimo de una ciudad encajada entre montaña y océano.",
         credit="Christian Trede · CC BY-SA 2.0 DE", source=W + "Cotton%20Tree%20(Sierra%20Leone).jpg?width=900"),
    dict(n=3, name="Museo Nacional del Ferrocarril (Cline Town, Freetown)", cat="Cultura", prio="Media", dog="pendiente de confirmación", time="1–2 h",
         lat=8.4880, lon=-13.2050,
         desc="Una de las visitas más inesperadas de África occidental y una historia de supervivencia en sí misma. El ferrocarril del gobierno de Sierra Leona funcionó hasta 1974; cuando se cerró, el material rodante quedó abandonado en los antiguos talleres, y durante la guerra civil la colección estuvo a punto de desaparecer del todo. Se rescató a partir de 2004 y el museo abrió en 2005 en Cline Town. Dentro hay locomotoras de vapor —una Garratt 4-8-2+2-8-4, una Hunslet de tanque—, diésel, vagones históricos, el coche del gobernador y, la pieza estrella, el vagón preparado especialmente para la visita de la reina Isabel II en 1961, con su tapicería original. Además, fotografías, billetes, mapas y horarios de la línea. Abierto de lunes a sábado, 10:00-16:00; entrada simbólica (150 SLE en enero de 2025), y conviene dejar un donativo. Coordenada de Cline Town aproximada.",
         credit="Wikimedia Commons", source=W + "Cotton%20Tree%20(Sierra%20Leone).jpg?width=900"),
    dict(n=4, name="Santuario de chimpancés de Tacugama", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="½ día",
         lat=8.4200, lon=-13.1800,
         desc="A menos de media hora del centro de Freetown, dentro del bosque del Parque Nacional de la Península, el santuario que fundó Bala Amarasekaran en 1995 para acoger chimpancés huérfanos y confiscados del comercio ilegal. Es hoy la institución de conservación más conocida del país, con un centenar largo de chimpancés occidentales —especie en peligro crítico— en recintos forestales, programa de reintroducción, senderos de bosque y eco-lodges donde se puede dormir oyendo a los chimpancés al amanecer. Visitas guiadas en horarios fijos, con reserva previa. PERRO: no se ha localizado una norma publicada, pero es un centro de grandes simios y el riesgo de transmisión de enfermedades hace que la prohibición sea la práctica universal en este tipo de instalaciones. Planificar como prohibido: uno se queda con el perro en el vehículo a la sombra o en el alojamiento de Freetown, y se hacen turnos. Coordenada aproximada dentro del bosque de la península: confirmar al reservar.",
         credit="BigMikeSndTech · CC BY 2.0", source=W + "West%20African%20Chimpanzee.jpg?width=900"),
    dict(n=5, name="Parque Nacional de la Península Occidental (Sugar Loaf, Guma)", cat="Naturaleza", prio="Alta", dog="permitido con precaución", time="1 día",
         lat=8.3406, lon=-13.1578,
         desc="18.337 hectáreas de selva semidecidua de dosel cerrado colgadas sobre Freetown y sus playas: reserva forestal desde 1916, parque nacional desde 2012 y sitio en la lista indicativa de la UNESCO. Es el bosque cerrado más occidental del país, área importante para las aves según BirdLife, con tres especies de duiker, y la razón de que la península tenga ese perfil de montaña verde cayendo directamente al mar. Dentro está Tacugama, y desde sus faldas arrancan las subidas al Sugar Loaf (unos 760 m, la cumbre que domina Freetown) y al Picket Hill, además del embalse de Guma, que abastece la capital. Es la mejor excursión a pie del país fuera de las Loma y, al ser un parque sin grandes depredadores, la más compatible con el perro — con correa, mucha agua y evitando las horas centrales, porque la humedad es brutal. El parque sufre una presión de deforestación urbana muy seria por el crecimiento de Freetown: parte de los límites están en discusión.",
         credit="BigMikeSndTech · CC BY 2.0", source=W + "West%20African%20Chimpanzee.jpg?width=900"),
    dict(n=6, name="River No. 2 Beach", cat="Costa", prio="Alta", dog="permitido", time="1–2 días",
         lat=8.3230, lon=-13.1866,
         desc="La playa de postal de África occidental y la más conocida del país: una lengua de arena blanquísima donde un río de agua dulce baja de la montaña y desemboca en el Atlántico formando una laguna, con la selva del parque nacional detrás y las palmeras dando sombra natural. La gestiona desde los años noventa una asociación comunitaria del pueblo —uno de los primeros proyectos de turismo comunitario del país—, con chiringuitos, cabañas sencillas y barcas que suben el río. Está a unos 30 km de Freetown por la carretera de la península, asfaltada. Es la base natural para dos o tres días de descanso y una de las pocas playas del viaje donde el perro puede estar realmente suelto en la arena a primera y última hora, con agua dulce para lavarlo después del baño.",
         credit="Christian Trede · Attribution", source=W + "River%20No.%202%20Beach%20(Sierra%20Leone).jpg?width=900"),
    dict(n=7, name="Tokeh Beach", cat="Costa", prio="Media", dog="permitido", time="1 día",
         lat=8.2833, lon=-13.2000,
         desc="Cinco kilómetros de arena al sur de River No. 2, con montaña al fondo y el pueblo de pescadores en un extremo. Fue la playa de moda de Sierra Leona antes de la guerra —hubo aquí un complejo hotelero francés que la guerra arrasó— y ha vuelto a la vida con un par de resorts y varios chiringuitos. Es más larga, más abierta y con más oleaje que River No. 2, y por tanto mejor para caminar kilómetros y peor para bañarse con niños. La carretera de la península la conecta con Freetown por asfalto. Buena alternativa si River No. 2 está lleno un fin de semana. Coordenada aproximada — confirmar sobre el terreno.",
         credit="Christian Trede · Attribution", source=W + "River%20No.%202%20Beach%20(Sierra%20Leone).jpg?width=900"),
    dict(n=8, name="Bureh Beach · la playa del surf", cat="Costa", prio="Media", dog="permitido", time="1–2 días",
         lat=8.2600, lon=-13.1900,
         desc="En el extremo sur de la península, la playa donde nació el surf en Sierra Leona: el Bureh Beach Surf Club, montado por jóvenes del pueblo, alquila tablas, da clases y gestiona cabañas y camping en la arena, y es uno de los proyectos comunitarios más citados del país. La ola es de arena, larga y constante de mayo a noviembre —justo la estación de lluvias, que es la trampa de calendario de toda esta costa— y más suave en seca, lo que la hace perfecta para aprender. Ambiente relajado, sin resorts, con hogueras por la noche. Es también el sitio más práctico para acampar con los vehículos en la península. Coordenada aproximada — confirmar sobre el terreno.",
         credit="Christian Trede · Attribution", source=W + "River%20No.%202%20Beach%20(Sierra%20Leone).jpg?width=900"),
    dict(n=9, name="Islas Banana (Dublin, Ricketts y Mes-Meheux)", cat="Naturaleza · costa", prio="Alta", dog="no confirmado", time="1–2 días",
         lat=8.1167, lon=-13.2167,
         desc="Tres islas frente a la bahía de Yawri, al final de la península: Dublin y Ricketts unidas por una calzada de piedra, y la diminuta Mes-Meheux deshabitada. Unos 900 habitantes en total, descendientes de esclavos liberados asentados aquí a finales del XVIII y principios del XIX. Dublin es de arena y tiene el embarcadero, la ruina de una iglesia de 1881 y, en la punta norte, el viejo muelle de esclavos; Ricketts es selva cerrada. Bajo el agua hay pecios con cañones y coral: es el mejor buceo y snorkel del país. Se llega en barca desde Kent, en el extremo de la península (20-40 minutos), y hay alojamientos sencillos —Daltons Banana Guest House, Banana Island Chalets—. PERRO: no es una norma sino una decisión del patrón de la barca; plan B, contratar la barca entera o dejarlo en el alojamiento de Kent/Bureh por turnos.",
         credit="Christian Trede · Attribution", source=W + "Banana%20Islands%20(Sierra%20Leone).jpg?width=900"),
    dict(n=10, name="Bunce Island · la isla de la trata", cat="Patrimonio", prio="Alta", dog="no confirmado", time="½–1 día",
         lat=8.5697, lon=-13.0406,
         desc="Río Sierra Leona arriba, a una hora larga de barca desde Freetown, las ruinas del castillo negrero británico que operó desde hacia 1670 hasta su cierre en torno a 1840. Lo levantó la Royal African Company y por él pasaron decenas de miles de africanos embarcados hacia las colonias del norte de América, muy específicamente hacia las plantaciones de arroz de Carolina del Sur y Georgia, donde los traficantes pagaban más por gente de esta costa por su conocimiento del cultivo del arroz: es el origen documentado de la cultura gullah-geechee de Estados Unidos. Quedan dos torres de vigilancia, la fortificación para ocho cañones, el polvorín y las tumbas de los tratantes, comidas por la vegetación y dañadas además por un huracán en 1974. Sitio histórico protegido desde 1948, gestionado por la Monuments and Relics Commission. No es una visita agradable ni pretende serlo: es de los lugares más cargados de toda la ruta atlántica, comparable a Gorée o a Elmina, y mucho menos visitado que ninguno de los dos. Se contrata la barca en Freetown (Aberdeen o Tagrin) o con un operador.",
         credit="Wikimedia Commons", source=W + "Banana%20Islands%20(Sierra%20Leone).jpg?width=900"),
    # ===== TRAMO 2 · EL SURESTE: BO, KENEMA, GOLA-TIWAI Y LA COSTA PERDIDA =====
    dict(n=11, name="Bo · la segunda ciudad", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=7.9564, lon=-11.7400,
         desc="Segunda ciudad del país (unos 230.000 habitantes), capital del Protectorado entre 1930 y la independencia de 1961, y el centro financiero, educativo y comercial de todo el sur. Es el nudo obligado entre Freetown, Kenema y el norte: aquí se reposta a fondo, se saca dinero y se compran provisiones antes de bajar a Tiwai y a Gola, porque más al sureste la red formal se acaba. Universidad de Njala, el Bo Government Secondary School de 1906 —la escuela de la élite del protectorado—, un mercado grande y el estadio. Ciudad sin monumentos, muy útil, con la mezcla mende-krio-fula que define el sur. La vieja estación del ferrocarril, cerrado en 1974, todavía marca el trazado urbano.",
         credit="Wikimedia Commons", source=W + "Cotton%20Tree%20(Sierra%20Leone).jpg?width=900"),
    dict(n=12, name="Kenema y el país de los diamantes", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=7.8767, lon=-11.1875,
         desc="Tercera ciudad del país, en un paso natural de las colinas de Kambui a 173 m, y la capital administrativa del diamante aluvial de Sierra Leona: aquí está la Government Diamond Office, creada en 1959, donde se valoran, licencian y certifican las piedras de toda la Provincia Oriental. Es la ciudad que explica la expresión «diamantes de sangre»: los yacimientos aluviales de este rincón financiaron la guerra civil y fueron el detonante del Proceso de Kimberley. Se puede ver el mercado del diamante y los talleres de talla, pero no se compran piedras a particulares bajo ningún concepto. Segundo dato, muy relevante para la salud del viaje: el Hospital Gubernamental de Kenema tiene una de las pocas unidades del mundo dedicadas a la fiebre de Lassa, endémica en esta región, y fue aquí donde el 25 de mayo de 2014 se diagnosticó el primer caso de ébola del país. Base logística para Gola y para las colinas de Kambui.",
         credit="Wikimedia Commons", source=W + "Cotton%20Tree%20(Sierra%20Leone).jpg?width=900"),
    dict(n=13, name="Parque Nacional de Gola Rainforest (UNESCO 2025)", cat="Patrimonio UNESCO", prio="Alta", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=7.5000, lon=-10.9200,
         desc="71.070 hectáreas de selva tropical de tierras bajas en la frontera con Liberia, el mayor bloque de selva primaria que queda en Sierra Leona y segundo parque nacional del país desde 2010. En 2025 fue inscrito como Patrimonio Mundial de la UNESCO dentro del complejo Gola-Tiwai: el PRIMER sitio de Patrimonio Mundial de Sierra Leona. Más de 330 especies de aves, 650 de mariposas, 49 de mamíferos, más de 300 chimpancés occidentales, hipopótamo pigmeo y elefante de bosque. Lo gestionan conjuntamente el gobierno, la Conservation Society of Sierra Leone y la RSPB británica, con un proyecto transfronterizo con el bosque de Gola del lado liberiano. La visita es caminata de bosque cerrado con guía comunitario desde los pueblos del borde, con observación de aves como plato fuerte —es uno de los mejores destinos ornitológicos de África occidental—. No hay safari ni observatorios: se viene a caminar por selva primaria. PERRO: descartado en zona núcleo, como en todo espacio con grandes simios. Base en Kenema; coordenada del parque aproximada.",
         credit="BigMikeSndTech · CC BY 2.0", source=W + "West%20African%20Chimpanzee.jpg?width=900"),
    dict(n=14, name="Isla de Tiwai · once especies de primates", cat="Patrimonio UNESCO", prio="Alta", dog="no confirmado — tratar como prohibido", time="2 días",
         lat=7.5442, lon=-11.3489,
         desc="Una isla fluvial de 12 km² en medio del río Moa, a 15 km de Potoru, con una de las mayores densidades de primates registradas del planeta: ONCE especies conviviendo en 1.200 hectáreas — chimpancé occidental, mangabey gris, mono de Diana, mona de Campbell, cercopiteco de nariz blanca, cercopiteco verde, colobo rojo occidental, colobo rey, colobo aceitunado, poto de Bosman y gálago de Demidoff. Además, hipopótamo pigmeo (aquí hay una de las mejores opciones del mundo de encontrar rastro) y más de 135 especies de aves. La gestiona la Environmental Foundation for Africa, una ONG local que reconstruyó las instalaciones de investigación y de visita después de la guerra; hay campamento de tiendas sobre plataforma, guías del pueblo y paseos en barca al amanecer y de noche. Desde 2025 forma parte, con Gola, del primer Patrimonio Mundial del país. ACCESO: pista de tierra desde Potoru y después barca; el último tramo es 4x4 y en lluvias puede cortarse. PERRO: descartado en la isla — hay chimpancés. Plan B: turnos, con uno quedándose en Potoru o en Kenema.",
         credit="BigMikeSndTech · CC BY 2.0", source=W + "West%20African%20Chimpanzee.jpg?width=900"),
    dict(n=15, name="Sulima y la desembocadura del Moa", cat="Costa", prio="Baja", dog="permitido", time="1 día",
         lat=6.9694, lon=-11.5750,
         desc="El extremo suroriental del país, donde el río Moa —el mismo que rodea Tiwai— desemboca en el Atlántico, casi en la frontera de Liberia. Sulima fue puesto comercial en el siglo XIX y acogió después a mucha población desplazada por la guerra liberiana; hoy es un pueblo de pescadores con una playa larguísima, absolutamente vacía, y un estuario enorme. Está en las listas de proyectos de desarrollo turístico del país y también en las de un posible puerto de mineral de hierro, así que puede cambiar. Es el punto más remoto y menos visitado de todo el bucle: se llega por la pista desde Zimmi, que conviene confirmar antes de meterse. Con el perro, es la playa más libre del país — nadie a quien molestar en kilómetros.",
         credit="Christian Trede · Attribution", source=W + "River%20No.%202%20Beach%20(Sierra%20Leone).jpg?width=900"),
    dict(n=16, name="Islas Turtle (archipiélago sherbro)", cat="Naturaleza · costa", prio="Media", dog="no confirmado", time="2 días",
         lat=7.5500, lon=-12.9500,
         desc="Ocho islas de arena blanca repartidas sobre 13 km de bajíos, al oeste de la isla de Sherbro, en el distrito de Bonthe: Yele, Bakie, Bumpetuk, Chepo, Hoong, Mut, Nyangei y Sei. Siete están habitadas por sherbros que viven de la pesca y del coco, con una cultura propia intacta: las tardes se pasan cantando canciones tradicionales de valentía y de amor, y la isla de Hoong está reservada a los hombres iniciados como parte de sus ritos de paso — no se pisa. Es el rincón más remoto y más difícil de alcanzar de Sierra Leona: se llega en barca desde Freetown (unas tres horas) o desde Shenge/Bonthe, con transporte irregular y estándares de seguridad que conviene mirar de cerca antes de embarcar. Hay una amenaza real de fondo: la subida del nivel del mar, que según las estimaciones citadas podría sumergirlas hacia 2040. VISITA OPCIONAL Y CARA EN TIEMPO: solo tiene sentido con varios días de margen. Coordenada aproximada del archipiélago — confirmar.",
         credit="Christian Trede · Attribution", source=W + "Banana%20Islands%20(Sierra%20Leone).jpg?width=900"),
    # ===== TRAMO 3 · REGRESO POR EL NORTE: MAKENI, KABALA, LAS LOMA Y OUTAMBA =====
    dict(n=17, name="Makeni · capital del norte", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=8.8817, lon=-12.0442,
         desc="Quinta ciudad del país (unos 85.000 habitantes en el censo de 2021) y centro económico de la Provincia del Norte, a unos 175 km de Freetown por la carretera principal asfaltada. Es la última plaza con servicios completos antes de subir a Kabala y a las montañas: combustible formal, bancos, mercado grande, la Universidad de Makeni —la mayor privada del país— y el Holy Spirit Hospital, el mayor hospital privado del norte, que es la referencia sanitaria realista de todo el tramo de montaña. Ciudad temne, ordenada y tranquila. Nota de salud: la zona es endémica de fiebre amarilla y de malaria.",
         credit="Wikimedia Commons", source=W + "Cotton%20Tree%20(Sierra%20Leone).jpg?width=900"),
    dict(n=18, name="Kabala y la colina de Gbawuria", cat="Cultura", prio="Media", dog="permitido", time="1 noche",
         lat=9.5833, lon=-11.5500,
         desc="Capital del distrito de Koinadugu, a unos 320 km de Freetown, rodeada de montañas y con el aire más seco y fresco del país: es la base obligada de todo el bloque de montaña. Al oeste del pueblo se levanta la colina de Gbawuria, donde cada 1 de enero sube media Sierra Leona a celebrar el año nuevo — una de las tradiciones populares más singulares del país, y una subida a pie corta y bonita cualquier otro día del año. Kabala es kuranko, fula, mandinga, yalunka y limba a la vez, con hospital gubernamental, mercado y alojamiento elemental. AVISO OPERATIVO: no hay electricidad de red, solo generadores, y el último tramo de acceso incluye unos 40 km de pista sin asfaltar desde la carretera principal — confirmar el estado actual, porque la red asfaltada del país ha avanzado en los últimos años.",
         credit="Wikimedia Commons", source=W + "Cotton%20Tree%20(Sierra%20Leone).jpg?width=900"),
    dict(n=19, name="Monte Bintumani (1.945 m) y las montañas Loma", cat="Naturaleza", prio="Alta", dog="permitido con precaución", time="3–4 días",
         lat=9.2250, lon=-11.1167,
         desc="El techo de Sierra Leona y el punto más alto de toda África occidental al oeste del Camerún: 1.945 m, en la cadena de las Loma, declarada reserva forestal de caza vedada desde 1952 (33.201 ha) y área importante para las aves. La ascensión es el gran objetivo a pie del país: se sube desde los pueblos del pie de monte —Sinekoro es el punto de partida clásico— con guía y porteadores del pueblo, cruzando selva de galería, bosque de montaña y, en lo alto, una pradera de altura abierta desde la que se ven Guinea y medio país. Tres o cuatro días ida y vuelta desde Kabala contando el acercamiento. En la selva baja hay hipopótamo pigmeo, cocodrilo enano, el búho pescador rojizo y varias especies de primates. ESTACIÓN: solo tiene sentido en seca (diciembre-marzo); en lluvias la pista de aproximación es impracticable. PERRO: es reserva forestal comunitaria, no parque nacional con grandes depredadores, y la subida transcurre por terreno de pueblo — es de las pocas montañas del viaje donde el perro puede ir, con correa y valorando el calor y los tres días de esfuerzo. Confirmar con los guías del pueblo. Coordenada de la cumbre: 9°13′30″N 11°07′00″W.",
         credit="BigMikeSndTech · CC BY 2.0", source=W + "West%20African%20Chimpanzee.jpg?width=900"),
    dict(n=20, name="Parque Nacional de Outamba-Kilimi", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="2 días",
         lat=9.7694, lon=-12.0261,
         desc="1.109 km² en el extremo noroeste, pegado a la frontera de Guinea, en dos sectores: Outamba (741 km²) y Kilimi (368 km²). Reserva de caza desde 1974 y parque nacional desde octubre de 1995. Terreno llano de sabana arbolada, bosque de galería y pradera, cruzado por ríos que corren al suroeste — y esos ríos son lo que se viene a ver: hipopótamo común, hipopótamo pigmeo, chimpancé occidental, elefante de bosque, colobos y bongo, con más de cien especies de aves y categoría de área importante para las aves de BirdLife. Es el único sitio de Sierra Leona donde se ve fauna grande de sabana y el más parecido a un safari que tiene el país, aunque el avistamiento es difícil y la gestión, frágil. Alojamiento en cabañas sencillas de materiales locales, individuales y colectivas. Alrededor viven susus, con una franja de amortiguación de 1 km. ACCESO 4x4 desde Kamakwie por pista; Kabala es la ciudad de referencia. PERRO: hay chimpancés e hipopótamos —que son un peligro real para un animal— así que se planifica como prohibido.",
         credit="BigMikeSndTech · CC BY 2.0", source=W + "West%20African%20Chimpanzee.jpg?width=900"),
]

_CAT_COLOR = {
    "ciudad · servicios": "azul", "costa": "turquesa", "naturaleza · costa": "turquesa",
    "naturaleza": "verde", "naturaleza · montaña": "verde",
    "patrimonio": "marron", "patrimonio unesco": "marron", "cultura": "morado",
}
for _p in POIS:
    _url = _p.pop("source")
    _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower()
    _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada del bucle — Gbalamuya / Pamelap (desde Guinea)", "Frontera", 9.1167, -12.9167,
     "El paso principal del país y el único bien documentado: enfrente del puesto guineano de Pamelap, en la carretera Conakry-Freetown, asfaltada de punta a punta. La web oficial de turismo de Sierra Leona lo describe como el punto de entrada principal para quien llega de Conakry y de África occidental, con 6-8 horas de trayecto total Conakry-Freetown, y avisa de que el cruce puede llevar varias horas por colas y trámites administrativos. Requisitos del vehículo según esa misma fuente: permiso de circulación, carnet de conducir y pasaporte, seguro de responsabilidad civil válido en Sierra Leona (se recomienda expresamente la Brown Card de la CEDEAO) y carnet de paso en aduana O permiso de importación temporal. Certificado de fiebre amarilla comprobado. Cruzar siempre de día. Coordenada aproximada."),
    ("Frontera · Salida por defecto — Gbalamuya / Pamelap (de vuelta a Guinea)", "Frontera", 9.1167, -12.9167,
     "La salida conservadora del bucle: se sale por donde se entró y se retoma el corredor guineano de subida por Forécariah-Coyah-Kindia-Mamou-Labé. Tiene la ventaja de ser el único paso con garantías y el inconveniente de repetir el tramo Kambia-Freetown. Si se elige esta opción, conviene hacer el bucle en sentido horario (sur primero, norte después) para no repetir carretera dentro de Sierra Leona."),
    ("Frontera · Salida alternativa norte — Kamakwie / Madina Oula (hacia Kindia, Guinea)", "Frontera", 9.9500, -12.2500,
     "POR CONFIRMAR. Paso menor del noroeste, en la zona de Outamba-Kilimi, que permitiría salir directamente desde el parque hacia el eje guineano de Kindia sin repetir Gbalamuya. No se ha localizado documentación operativa: puede no tener aduana habilitada para vehículos extranjeros ni capacidad para sellar CPD, que es el riesgo real. NO contar con este paso hasta verificarlo con overlanders recientes o con la aduana. Coordenada aproximada."),
    ("Frontera · Salida alternativa noreste — Kabala / Faranah (hacia la Alta Guinea)", "Frontera", 9.7000, -11.2000,
     "POR CONFIRMAR. Paso de montaña del noreste que conectaría Kabala y las Loma directamente con Faranah, en Guinea — es decir, con el nacimiento del Níger y con el corredor guineano de subida por Dabola. Sería, sobre el papel, el encaje perfecto del bucle: entrar por Gbalamuya y salir por aquí, sin repetir un solo kilómetro. Pero es un paso secundario, mal documentado, en pista, y con aduana incierta para un vehículo extranjero con CPD. VERIFICAR ANTES DE CONTAR CON ÉL. Coordenada aproximada."),
    ("Frontera · Jendema / Bo-Waterside (hacia Liberia)", "Frontera", 6.8500, -11.2500,
     "Paso del sureste hacia Liberia, operativo y con tráfico comercial. NO se usa en este plan: Liberia está excluida de la ruta fija por el problema del visado (ver la ficha de Liberia). Se documenta porque es uno de los tres puntos donde Sierra Leona expide visado a la llegada y porque, si el problema liberiano se resolviera, sería la puerta de enlace natural desde Sulima y Zimmi."),
    ("Cobertura consular española — Embajada en Conakry (Guinea)", "Consular", 9.5300, -13.6800,
     "España no tiene embajada en Freetown: la demarcación consular corresponde a la Embajada de España en Conakry. Cancillería +224 664 20 22 01 · Sección consular +224 613 33 90 90 · Emergencia consular grave +224 664 33 54 93. Es una ventaja relativa de este bucle: la embajada de referencia está a un día de camino, en el país por el que se entra y se sale."),
    ("Connaught Hospital — Freetown", "Hospital", 8.4870, -13.2340,
     "Principal hospital público de referencia del país, en el centro de Freetown. Capacidad limitada para politraumatismos graves. Coordenada urbana aproximada."),
    ("Holy Spirit Hospital — Makeni", "Hospital", 8.8817, -12.0442,
     "El mayor hospital privado de la Provincia del Norte y la referencia sanitaria realista de todo el tramo de montaña (Kabala, Loma, Outamba). Entre Makeni y las Loma no hay nada equivalente."),
    ("Kenema Government Hospital · unidad de fiebre de Lassa", "Hospital", 7.8767, -11.1875,
     "Una de las pocas unidades del mundo dedicadas al tratamiento y la investigación de la fiebre de Lassa, en funcionamiento desde los años setenta con el Viral Hemorrhagic Fever Consortium. Fue aquí donde se diagnosticó el primer caso de ébola de Sierra Leona el 25 de mayo de 2014. Referencia del sureste."),
    ("Combustible · Freetown", "Combustible", 8.4840, -13.2299,
     "Mejor oferta y calidad del país (Total, NP/Petroleum SL, Leonoil). Repostar a fondo aquí antes de la península y antes de bajar al sureste."),
    ("Combustible · Bo, Kenema, Makeni", "Combustible", 7.9564, -11.7400,
     "Estaciones formales en las tres ciudades grandes del interior, que son los tres puntos de repostaje seguros del bucle. Bo es el último antes de Tiwai y Gola; Makeni, el último antes de Kabala y de la montaña."),
    ("Combustible · Kabala y Kamakwie (incierto)", "Combustible", 9.5833, -11.5500,
     "Puntos de venta elementales y a veces en garrafa. NO dar por hecho el suministro: salir de Makeni con depósitos y garrafas llenos para cubrir Kabala, la aproximación a las Loma, Kamakwie y Outamba-Kilimi y la vuelta (~500-600 km de ida y vuelta con consumo de pista)."),
    ("Agua · Freetown y ciudades principales", "Agua potable", 8.4840, -13.2299,
     "Agua embotellada y en bolsa en Freetown, Bo, Kenema y Makeni. Para el depósito de uso general (ducha, aseo, limpieza), estaciones de servicio, hoteles y misiones permiten llenar con manguera. Nunca beber del grifo."),
    ("Agua · península de Freetown y montaña", "Agua potable", 8.3230, -13.1866,
     "En la península hay agua corriente en los alojamientos de River No. 2, Tokeh y Bureh, y arroyos de montaña abundantes — tratar siempre. En las Loma y en Outamba, el agua es de río o de pozo del pueblo: filtro mecánico más tratamiento químico o ebullición, sin excepción. Salir de Kabala con los depósitos llenos."),
]

DRONE_CALLOUT = ("warn", "Sin procedimiento turístico publicado: tratar como restringido y no volar sin autorización escrita",
                  "No se ha localizado un procedimiento público de autorización de drones para visitantes en Sierra Leona. La autoridad competente es la Sierra Leone Civil Aviation Authority (SLCAA), pero no se ha podido verificar que publique un régimen turístico ni un formulario de solicitud — POR CONFIRMAR por escrito antes de entrar. El criterio del proyecto es no volar sin autorización previa y por escrito. En ningún caso volar sobre Freetown (puerto, aeropuerto de Lungi, edificios de gobierno), sobre Bunce Island y los sitios de la Monuments and Relics Commission, sobre Tacugama ni sobre las zonas núcleo de Gola y Tiwai, que son espacios con grandes simios y normativa propia. Las zonas mineras de diamante del este (Kenema, Kono) son además terreno sensible: no volar sobre concesiones ni sobre yacimientos aluviales.")

STARLINK_CALLOUT = ("ok", "Starlink ACTIVO en Sierra Leona: uno de los primeros mercados de la región",
                     "Sierra Leona figura entre los mercados africanos con servicio Starlink operativo y en funcionamiento a mediados de 2026 — fue de los primeros de África occidental en tenerlo, y es una diferencia real respecto a Guinea, que a fecha de esta revisión sigue en la lista de «próximamente». Esto convierte al bucle de Sierra Leona en una buena ventana para resolver trámites pesados (visados del bloque siguiente, gestiones del perro, copias de seguridad) que en Guinea son difíciles. Revisar el mapa oficial 30-60 días antes por si cambia el marco de itinerancia, y mantener SIM local (Orange SL, Africell) como respaldo urbano.")

DOG_MATRIX = [
    ("Entrada en el país (frontera de Gbalamuya)", "no confirmado — agujero documental",
     "NO se ha localizado ninguna fuente oficial sobre la importación de animales de compañía en Sierra Leona, ni norma publicada ni testimonio de viajero. El dosier del perro del proyecto ya marcaba el país como «sin confirmar». Preparación mínima recomendada por analogía con los vecinos: microchip, pasaporte europeo de animal de compañía, vacuna antirrábica en vigor con menos de 12 meses y certificado veterinario internacional reciente (conseguirlo en Conakry antes de cruzar). Escribir con 6 meses de antelación al Ministerio de Agricultura y Seguridad Alimentaria y a la embajada/alta comisión de Sierra Leona. ES EL PUNTO QUE MÁS PUEDE HACER FRACASAR EL BUCLE."),
    ("Playas de la península (River No. 2, Tokeh, Bureh, Kent)", "permitido",
     "Playas comunitarias y de pueblo, sin espacio protegido de por medio. Es de lo mejor que tiene el viaje para el perro: arena, sombra de palmera y agua dulce de río en River No. 2 para lavarlo después del baño. Correa cerca de los chiringuitos y de las barcas de pesca; atención a los perros de pueblo y a las horas centrales, que son brutales de humedad."),
    ("Parque Nacional de la Península Occidental (Sugar Loaf, Guma)", "permitido con precaución",
     "Parque sin grandes depredadores y con senderos de bosque. No se ha localizado una prohibición expresa de mascotas: preguntar en la entrada. Correa, mucha agua y evitar el mediodía. Es la mejor excursión del país compatible con el perro fuera de las Loma."),
    ("Tacugama, Gola y Tiwai (grandes simios)", "no confirmado — tratar como prohibido",
     "Tres espacios con chimpancés: el riesgo de transmisión de enfermedades a grandes simios hace que la prohibición sea la práctica universal, aunque no haya norma publicada. PLAN B obligatorio: turnos entre los tres viajeros — uno se queda con el perro en Freetown (Tacugama), en Kenema (Gola) o en Potoru (Tiwai). Es perfectamente asumible: son visitas de medio día o de un día."),
    ("Outamba-Kilimi", "no confirmado — tratar como prohibido",
     "Hay chimpancés y, sobre todo, hipopótamos en los ríos, que son un peligro real y directo para un perro. Planificar como prohibido y no negociarlo sobre el terreno aunque el guarda lo autorice."),
    ("Monte Bintumani y montañas Loma", "permitido con precaución",
     "Reserva forestal de caza vedada gestionada con los pueblos del pie de monte, no parque nacional con depredadores, y la subida transcurre por terreno comunitario con guías y porteadores del pueblo. Es de las pocas montañas grandes del viaje donde el perro puede ir. Pero son tres o cuatro días de esfuerzo en calor húmedo: valorar honestamente si le conviene, llevar agua para él y confirmarlo con los guías antes de salir."),
    ("Barcas a las islas Banana, Bunce y Turtle", "no confirmado",
     "No es una norma sino una decisión del patrón de la barca, igual que en las islas de Los en Guinea. PLAN B: contratar la barca entera en vez de plaza colectiva, o dejar al perro en el alojamiento de Kent, Bureh o Freetown y hacer la excursión por turnos."),
    ("Freetown, Bo, Kenema, Makeni (ciudades)", "permitido con condiciones",
     "Sin restricción legal identificada. Correa siempre: mucho perro callejero, tráfico muy denso en Freetown y calor húmedo extremo. Confirmar por teléfono la política del alojamiento antes de llegar. Nunca dejarlo solo en el vehículo."),
]

SOURCES = [
    ("VisitSierraLeone (web oficial de turismo) · llegar por tierra: pasos fronterizos, requisitos del vehículo y Brown Card", "https://www.visitsierraleone.org/getting-to-sierra-leone-by-land/"),
    ("Wikipedia · Política de visados de Sierra Leona (visado a la llegada en Gbalamuya y Jendema desde 2019; gratuito para la UE)", "https://en.wikipedia.org/wiki/Visa_policy_of_Sierra_Leone"),
    ("Wikipedia · Sierra Leona (clima, estación de lluvias mayo-noviembre, red viaria: 11.300 km de los que solo el 8 % asfaltado)", "https://en.wikipedia.org/wiki/Sierra_Leone"),
    ("Wikipedia · Cotton Tree (Sierra Leone): el árbol se derrumbó el 24 de mayo de 2023", "https://en.wikipedia.org/wiki/Cotton_Tree_(Sierra_Leone)"),
    ("Wikipedia · Isla de Tiwai: 12 km², once especies de primates, hipopótamo pigmeo, gestión de la Environmental Foundation for Africa", "https://en.wikipedia.org/wiki/Tiwai_Island"),
    ("Wikipedia · Parque Nacional de Gola Rainforest: 71.070 ha, UNESCO 2025 dentro del complejo Gola-Tiwai", "https://en.wikipedia.org/wiki/Gola_Rainforest_National_Park"),
    ("Wikipedia · Parque Nacional de Outamba-Kilimi: 1.109 km², fauna, acceso y cabañas", "https://en.wikipedia.org/wiki/Outamba-Kilimi_National_Park"),
    ("Wikipedia · Montañas Loma: reserva forestal desde 1952, 33.201 ha, área importante para las aves", "https://en.wikipedia.org/wiki/Loma_Mountains"),
    ("Wikipedia · Monte Bintumani: 1.945 m, coordenadas 9°13′30″N 11°07′00″W, fauna del pie de monte", "https://en.wikipedia.org/wiki/Mount_Bintumani"),
    ("Wikipedia · Parque Nacional de la Península Occidental: 18.337 ha, lista indicativa de la UNESCO, Tacugama", "https://en.wikipedia.org/wiki/Western_Area_Peninsula_National_Park"),
    ("Wikipedia · Islas Banana: Dublin, Ricketts y Mes-Meheux, acceso desde Kent, pecios y alojamientos", "https://en.wikipedia.org/wiki/Banana_Islands"),
    ("Wikipedia · Bunce Island: castillo negrero británico (h. 1670-1840), ruinas y protección desde 1948", "https://en.wikipedia.org/wiki/Bunce_Island"),
    ("Wikipedia · Islas Turtle: ocho islas sherbro, 3 h de barca desde Freetown, riesgo de sumersión hacia 2040", "https://en.wikipedia.org/wiki/Turtle_Islands,_Sierra_Leone"),
    ("Wikipedia · Kenema: Government Diamond Office, unidad de fiebre de Lassa, primer diagnóstico de ébola del país (2014)", "https://en.wikipedia.org/wiki/Kenema"),
    ("Wikipedia · Bo: segunda ciudad, capital del Protectorado 1930-1961, servicios", "https://en.wikipedia.org/wiki/Bo,_Sierra_Leone"),
    ("Wikipedia · Makeni: centro económico del norte, Holy Spirit Hospital, endemia de fiebre amarilla y malaria", "https://en.wikipedia.org/wiki/Makeni"),
    ("Wikipedia · Kabala: colina de Gbawuria, clima, sin electricidad de red, acceso final por pista", "https://en.wikipedia.org/wiki/Kabala,_Sierra_Leone"),
    ("Wikipedia · Sulima: desembocadura del río Moa, historia y proyectos de puerto y turismo", "https://en.wikipedia.org/wiki/Sulima,_Sierra_Leone"),
    ("Wikipedia · Museo Nacional del Ferrocarril de Sierra Leona: horarios, entrada y colección (vagón de Isabel II, 1961)", "https://en.wikipedia.org/wiki/Sierra_Leone_National_Railway_Museum"),
    ("tech.africa · disponibilidad de Starlink en África (junio 2026): Sierra Leona y Liberia activos, Guinea «próximamente»", "https://tech.africa/starlink-africa/"),
    ("Embajada de España en Guinea · contacto (cobertura consular de Sierra Leona)", "https://www.exteriores.gob.es/Embajadas/conakry/es/Embajada/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx"),
    ("Wikipedia · Misiones diplomáticas en Sierra Leona (sin embajada española)", "https://en.wikipedia.org/wiki/List_of_diplomatic_missions_in_Sierra_Leone"),
    ("Comisión Europea · animales de compañía (requisitos de reentrada en la UE)", "https://europa.eu/youreurope/citizens/travel/carry/pets-and-other-animals/index_es.htm"),
    ("iOverlander · puntos de combustible, agua y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Tramo 1-2 (entrada y sur): Gbalamuya -> Kambia -> Freetown -> península -> Bunce -> Bo -> Kenema -> Gola -> Tiwai -> Sulima
CORRIDOR = [
    (9.1167, -12.9167),   # Gbalamuya (entrada desde Guinea)
    (9.1250, -12.9200),   # Kambia
    (8.7667, -12.7833),   # Port Loko
    (8.4840, -13.2299),   # Freetown
    (8.4200, -13.1800),   # Tacugama
    (8.3230, -13.1866),   # River No. 2
    (8.2833, -13.2000),   # Tokeh
    (8.2600, -13.1900),   # Bureh
    (8.1167, -13.2167),   # Islas Banana (Kent)
    (8.5697, -13.0406),   # Bunce Island
    (8.4840, -13.2299),   # Freetown (vuelta)
    (7.9564, -11.7400),   # Bo
    (7.8767, -11.1875),   # Kenema
    (7.5000, -10.9200),   # Gola Rainforest NP
    (7.5442, -11.3489),   # Isla de Tiwai
    (6.9694, -11.5750),   # Sulima
]

# Tramo 3 (regreso por el norte): Sulima -> Bo -> Makeni -> Kabala -> Loma/Bintumani -> Kamakwie -> Outamba -> frontera
CORRIDOR_ALT = [
    (6.9694, -11.5750),   # Sulima
    (7.9564, -11.7400),   # Bo
    (8.8817, -12.0442),   # Makeni
    (9.5833, -11.5500),   # Kabala
    (9.2250, -11.1167),   # Monte Bintumani (Loma)
    (9.5833, -11.5500),   # Kabala (vuelta)
    (9.4833, -12.2333),   # Kamakwie
    (9.7694, -12.0261),   # Outamba-Kilimi
    (9.1167, -12.9167),   # Gbalamuya (salida a Guinea)
]

CORRIDOR_LABEL = "Bucle · entrada y sur"
CORRIDOR_ALT_LABEL = "Bucle · regreso por el norte"

EXPERIENCIAS = [
    "El cruce de Gbalamuya no es difícil, es lento. La propia web oficial de turismo del país lo dice sin adornos: el paso puede llevar varias horas por las colas y los trámites, con inspección del vehículo y despacho de aduana. Es la carretera principal entre Conakry y Freetown y por ella pasan camiones y autobuses todo el día. La recomendación que se repite —oficial y de viajeros— es la misma: cruzar de día y no llegar con la tarde encima.",
    "Lo que piden por el vehículo está documentado y es coherente con el resto de la CEDEAO: permiso de circulación, carnet de conducir y pasaporte, seguro de responsabilidad civil válido en Sierra Leona —la Brown Card de la CEDEAO es lo que recomiendan expresamente— y carnet de paso en aduana o, en su defecto, permiso de importación temporal emitido en el puesto. Es una de las pocas fronteras de la ruta donde la fuente oficial acepta explícitamente las dos vías.",
    "El dato que cambia el cálculo del bucle: Sierra Leona expide visado A LA LLEGADA en la propia frontera terrestre de Gbalamuya desde septiembre de 2019, y para los ciudadanos de la Unión Europea es gratuito. Es exactamente lo contrario del caso liberiano, que es la razón por la que Liberia está fuera de la ruta. Conviene confirmarlo por escrito antes de salir —es un dato que cambia con facilidad—, pero si se sostiene, la barrera administrativa del bucle es baja.",
    "Las playas de la península son la sorpresa que todo el mundo cuenta: River No. 2 aparece en casi todas las listas de mejores playas de África occidental y sigue gestionada por una asociación del pueblo, no por una cadena hotelera. Tokeh es más larga y más abierta; Bureh es la del surf, con un club montado por chavales del pueblo que alquilan tablas y dejan acampar en la arena. Es el mejor bloque de descanso posible antes de encarar el regreso hacia Senegal.",
    "El Cotton Tree ya no está como en las fotos. El árbol del algodón bajo el que rezaron los colonos de 1792, símbolo del país y de sus billetes, se vino abajo en gran parte durante una tormenta el 24 de mayo de 2023. Sobreviven parte del tronco y una agalla con hojas, y la parte caída se trasladó para convertirla en monumento. Cualquier guía anterior a 2023 —y la versión previa de esta misma ficha— lo describe como si siguiera en pie.",
    "Tiwai es el sitio del que vuelve hablando todo el que va: once especies de primates en 12 km² de isla fluvial, campamento de tiendas sobre plataforma, y paseos en barca al amanecer buscando rastro de hipopótamo pigmeo. Lo gestiona una ONG local, la Environmental Foundation for Africa, que reconstruyó las instalaciones después de la guerra. El acceso es lo que hay que mirar: pista de tierra desde Potoru y después barca, con el último tramo comprometido en cuanto llueve.",
    "Gola y Tiwai entraron en la lista del Patrimonio Mundial de la UNESCO en 2025 como «complejo Gola-Tiwai»: es el primer sitio de Patrimonio Mundial de Sierra Leona. Todavía no se nota en el número de visitantes, pero es razonable esperar que cambie algo en los próximos años — y también que mejore la información pública sobre accesos y tasas, que hoy es escasa.",
    "La estación de lluvias es el factor que decide si este bucle se hace o no se hace. Llueve de mayo a noviembre, y en el norte agosto pasa de 380 mm en un mes. Con solo el 8 % de los 11.300 km de red asfaltados, eso significa que las pistas a Tiwai, a Sinekoro (Bintumani) y a Outamba se vuelven impracticables o directamente peligrosas. El bucle es un plan de estación seca: de diciembre a abril, y preferiblemente de enero a marzo.",
    "Kabala y la montaña son otro país: aire seco, noches frescas y mucha menos humedad que la costa. Los viajeros que suben a Bintumani coinciden en que lo duro no es la cumbre sino la aproximación —pista larga, pueblos sin servicios— y en que se hace con guías y porteadores contratados en el pueblo del pie de monte. Tres o cuatro días desde Kabala, ida y vuelta.",
    "Las Turtle Islands son el punto donde la logística se rompe. Tres horas de barca desde Freetown, transporte irregular, y una advertencia que aparece en las propias descripciones del sitio: los estándares de seguridad de las embarcaciones no siempre son los que uno esperaría. Con un perro a bordo y sin margen de calendario, es la visita más fácil de sacrificar del bucle.",
    "PENDIENTE HONESTO: no se ha localizado ni un solo relato de un overlander que haya entrado en Sierra Leona con vehículo propio Y con animal de compañía. El marco del vehículo está razonablemente documentado gracias a la web oficial de turismo; el del perro, no lo está en absoluto. Antes de activar el bucle hay que preguntar activamente en iOverlander y en los foros overland, y escribir al ministerio. Es el mismo agujero que teníamos en Guinea, pero en Guinea ya se cerró la parte legal y aquí todavía no.",
]

HISTORIA_RESUMEN = ("Sierra Leona nació como un experimento abolicionista —Freetown, «ciudad libre», fundada en 1792 para reasentar a esclavos liberados— y acabó dando nombre a la peor cara del comercio de diamantes: entre 1991 y 2002 vivió una guerra civil "
                     "de once años, con niños soldado y amputaciones masivas de civiles, financiada por los «diamantes de sangre». Desde 2002 encadena elecciones democráticas con alternancia pacífica, un logro notable en la región, y sobrevivió al brote de ébola "
                     "de 2014-2016, uno de los peores del mundo; sigue siendo uno de los países más pobres del planeta y uno de los menos visitados de África occidental.")

HISTORIA_SECCIONES = [
    ("Freetown, la colonia de los libertos",
     "La península de Freetown, poblada por temnes y sherbros, se convirtió en 1787 en el escenario de un experimento abolicionista británico: reasentar allí a antiguos esclavos liberados. El primer intento fracasó, pero en 1792 llegaron desde Nueva Escocia más de mil «Black Loyalists» —afroamericanos que habían luchado del lado británico en la guerra de independencia de Estados Unidos a cambio de su libertad— y fundaron Freetown, la «ciudad libre». Se les sumaron después los cimarrones de Jamaica y, sobre todo, decenas de miles de africanos liberados de los barcos negreros que interceptaba la Marina Real tras la abolición del comercio de esclavos en 1807. De esa mezcla nació la sociedad krio, angloafricana, cristiana, urbana y letrada, que dominó la vida política y comercial de la colonia — y cuyo idioma, el krio, habla hoy el 96 % del país. El Cotton Tree, el árbol bajo el que rezaron los colonos de 1792, fue durante dos siglos el símbolo de esa fundación, hasta que se derrumbó en una tormenta el 24 de mayo de 2023."),
    ("Bunce Island y la ironía del lugar",
     "La contradicción está a solo 30 km río arriba de Freetown: en Bunce Island funcionó desde hacia 1670 y hasta cerca de 1840 uno de los principales castillos negreros británicos de la costa, por el que pasaron decenas de miles de personas embarcadas hacia Carolina del Sur y Georgia. Los traficantes de las plantaciones de arroz americanas pagaban precios más altos por cautivos de esta costa precisamente por su dominio del cultivo del arroz, y de ahí procede la cultura gullah-geechee del sureste de Estados Unidos. Que la ciudad de los libertos y el castillo de la trata estén en el mismo estuario resume la historia entera del país."),
    ("Colonia y protectorado: dos países en uno",
     "Gran Bretaña gobernó por separado la colonia costera —krio, con derechos y educación— y el protectorado del interior, declarado en 1896, donde vivían mendes y temnes bajo administración indirecta y sin los mismos privilegios. Esa división administrativa creó una fractura entre costa e interior que la independencia de 1961 no resolvió y que está en el origen de buena parte de la política sierraleonesa posterior. Bo fue la capital del protectorado desde 1930, y el ferrocarril, hoy museo en Cline Town, fue el eje de penetración colonial hasta su cierre en 1974."),
    ("La guerra civil (1991-2002) y los diamantes de sangre",
     "En marzo de 1991 el Frente Revolucionario Unido (RUF) entró desde Liberia con apoyo de Charles Taylor y desencadenó once años de guerra. Fue un conflicto de una crueldad específica y deliberada: reclutamiento masivo de niños soldado y amputación de manos y brazos a civiles como método de terror. Lo financiaba el diamante aluvial del este —Kono, Kenema—, los «diamantes de sangre», vendidos fuera de todo control; la respuesta internacional fue el Proceso de Kimberley de certificación, que sigue vigente. La guerra dejó decenas de miles de muertos y más de dos millones de desplazados, y terminó en 2002 tras la intervención británica de la Operación Palliser y el despliegue de UNAMSIL, una de las mayores misiones de paz de la ONU. El Tribunal Especial para Sierra Leona juzgó después a los máximos responsables, incluido Charles Taylor. Esto se cuenta porque condiciona lo que se ve —un país reconstruido desde cero— y porque es materia sensible: no se pregunta a la ligera."),
    ("El ébola de 2014-2016",
     "El 25 de mayo de 2014, el laboratorio de fiebre de Lassa del hospital de Kenema diagnosticó el primer caso de ébola del país. El brote de África occidental, iniciado en la Guinea forestal, golpeó a Sierra Leona con especial dureza: casi 4.000 muertos confirmados, un sistema sanitario ya frágil desbordado, escuelas cerradas, fronteras cerradas y una economía detenida durante casi dos años. El país fue declarado libre de transmisión en 2016. La huella sigue ahí —en los protocolos de lavado de manos que se ven a la entrada de muchos edificios, en la desconfianza inicial y en el personal sanitario que se perdió—, pero también dejó una vigilancia epidemiológica y una capacidad de respuesta bastante mejores que las de antes."),
    ("Situación actual: estabilidad pobre y poco visitada",
     "Desde 2002 Sierra Leona ha celebrado elecciones sucesivas con alternancia pacífica de poder entre el SLPP y el APC, un historial notable para la región. Sigue dependiendo de la minería —diamante, rutilo (tiene uno de los mayores depósitos del mundo de este mineral de titanio), hierro y bauxita— con la agricultura empleando al 80 % de la población, y figura sistemáticamente entre los países más pobres del planeta. Hubo protestas serias en 2022 y un ataque armado en Freetown en noviembre de 2023, ambos superados. Para el viajero, el resultado es un país estable, cordial, con una de las mejores costas de África occidental y prácticamente sin turismo."),
]

HISTORIA_FUENTES = [
    ("BBC News · Sierra Leone country profile", "https://www.bbc.com/news/world-africa-14094194"),
    ("Encyclopaedia Britannica · Sierra Leone, History", "https://www.britannica.com/place/Sierra-Leone/History"),
    ("United Nations · UNAMSIL, misión de paz en Sierra Leona", "https://peacekeeping.un.org/en/mission/past/unamsil/"),
    ("Wikipedia · Cotton Tree (Sierra Leone): derrumbe del 24 de mayo de 2023", "https://en.wikipedia.org/wiki/Cotton_Tree_(Sierra_Leone)"),
    ("Wikipedia · Bunce Island", "https://en.wikipedia.org/wiki/Bunce_Island"),
]

SPEC = dict(
    slug="sierra-leona", name="Sierra Leona", revision="12 sep 2026",
    sub="ALTERNATIVA · bucle opcional de la subida · playas, primates y el techo de África occidental",
    chips=[
        ("ESTATUS", "ALTERNATIVA — NO está en la ruta fija. Bucle opcional que solo se activa en la SUBIDA, «si hay tiempo y ganas»"),
        ("COSTE DE LA DESVIACIÓN", "versión completa ~2.000 km y 14-18 días · versión mínima (península + Tiwai) ~1.100 km y 8-10 días"),
        ("ENTRADA", "Gbalamuya/Pamelap desde Guinea · VISADO A LA LLEGADA gratuito para la UE (por confirmar)"),
        ("SALIDA", "de vuelta a Guinea por Gbalamuya (segura) · o por el norte, Kamakwie o Kabala-Faranah (POR CONFIRMAR)"),
        ("PDIs", "20 puntos: 16 en el tramo de entrada y sur, 4 en el regreso por el norte"),
        ("UNESCO", "complejo Gola-Tiwai, Patrimonio Mundial desde 2025 — el PRIMERO del país"),
        ("A PIE", "monte Bintumani 1.945 m, techo de África occidental fuera de Camerún · Sugar Loaf · Gbawuria"),
        ("4x4", "accesos a Tiwai (Potoru), a las Loma (Sinekoro) y a Outamba-Kilimi (Kamakwie) · solo el 8 % de la red está asfaltada"),
        ("COSTA", "River No. 2, Tokeh y Bureh: de las mejores playas de África occidental, y casi vacías"),
        ("LLUVIAS", "mayo-noviembre, de las más duras de África. El bucle SOLO tiene sentido en seca: diciembre-abril"),
        ("STARLINK", "ACTIVO — de los primeros de la región. Ventana para resolver trámites que en Guinea no se pueden"),
        ("PERRO", "AGUJERO NEGRO: sin ninguna fuente localizada sobre importación de animales"),
        ("SALUD", "fiebre amarilla obligatoria · malaria intensa · Lassa endémica en el este · secuelas del ébola 2014-2016"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[8.6, -11.9], zoom=7,
    notice="Documento de planificación de una ALTERNATIVA: Sierra Leona no forma parte de la ruta fija. Se documenta como bucle opcional insertable en el corredor de subida, para poder decidir con datos. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y de nuevo 72 h antes de cada frontera.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("<strong>Sierra Leona no está en la ruta fija.</strong> Es una <strong>alternativa</strong>: un bucle opcional que se inserta en el corredor de <strong>subida</strong>, entre Guinea y Senegal, "
                   "y que solo se activa «si tenemos tiempo y ganas». Esta ficha existe para que esa decisión se pueda tomar con números encima de la mesa, no con intuiciones. "
                   "Lo que hay dentro justifica la duda: <strong>las mejores playas de África occidental</strong> —River No. 2, Tokeh, Bureh— en una península de montaña verde a media hora de la capital; "
                   "<strong>la isla de Tiwai</strong>, con once especies de primates en 12 km²; <strong>Gola</strong>, la mayor selva primaria que le queda al país, que en <strong>2025 se convirtió, junto con Tiwai, "
                   "en el primer Patrimonio Mundial de la UNESCO de Sierra Leona</strong>; <strong>Bunce Island</strong>, el castillo negrero más cargado y menos visitado de la costa atlántica; y el "
                   "<strong>monte Bintumani (1.945 m)</strong>, el techo de toda África occidental al oeste del Camerún, que se sube a pie en tres o cuatro días. Y casi nadie va: es de los países menos visitados del continente. "
                   "A favor del bucle juegan además dos cosas administrativas nada menores — <strong>visado a la llegada en la propia frontera terrestre, gratuito para la UE</strong>, y <strong>Starlink activo</strong>, "
                   "que en este tramo del viaje es un lujo. En contra: los kilómetros, los días, y un <strong>agujero documental total sobre la entrada del perro</strong>."),
    decision=("<strong>ESTATUS: ALTERNATIVA, NO RUTA FIJA.</strong> Decisión literal del dueño del proyecto: «dejaremos Sierra Leona para la subida si tenemos tiempo y ganas». No se planifica como país de paso obligado: "
              "se planifica como un <strong>bucle cerrado que se inserta en el corredor de subida</strong> y del que hay que saber, antes de nada, cuánto cuesta.<br><br>"
              "<strong>Lo que cuesta.</strong> Versión completa (península + sureste + regreso por la montaña): <strong>~2.000 km y 14-18 días</strong>. "
              "Versión intermedia (península + Bunce + Bo/Kenema + Tiwai y vuelta): ~1.400 km y 10-12 días. "
              "Versión mínima (solo península de Freetown, Bunce y las Banana): <strong>~700 km y 5-7 días</strong>, entrando y saliendo por Gbalamuya. "
              "Esa escala de tres versiones es la herramienta real de decisión: el bucle es <strong>modular</strong> y se puede recortar sobre la marcha sin perderlo entero.<br><br>"
              "<strong>Cómo se inserta.</strong> Se entra desde Guinea por <strong>Gbalamuya/Pamelap</strong>, el único paso bien documentado, desviándose del eje guineano en Coyah o en Forécariah. "
              "La salida por defecto es <strong>la misma frontera</strong>, retomando después el corredor guineano de subida por Kindia-Mamou-Labé hacia Koundara y Senegal. "
              "Existen dos salidas alternativas por el norte que evitarían repetir kilómetros —<strong>Kamakwie/Madina Oula</strong> hacia Kindia, y sobre todo <strong>Kabala/Faranah</strong> hacia la Alta Guinea, "
              "que encajaría de maravilla con el corredor guineano de subida por Dabola—, pero <strong>ninguna de las dos está documentada</strong> para un vehículo extranjero con CPD. "
              "Verificarlas es la pregunta técnica más rentable de esta ficha: si Kabala-Faranah funciona, el bucle deja de ser un desvío y pasa a ser una <strong>variante de ruta sin coste de repetición</strong>.<br><br>"
              "<strong>La ventana de calendario manda.</strong> La estación de lluvias (mayo-noviembre, con agosto por encima de 380 mm en el norte) deja impracticables las pistas a Tiwai, a las Loma y a Outamba, "
              "y solo el 8 % de los 11.300 km de red del país está asfaltado. Si la subida cae en lluvias, el bucle completo <strong>no se hace</strong>: como mucho, la península de Freetown, que es todo asfalto. "
              "Si cae entre diciembre y abril, el bucle completo es perfectamente viable.<br><br>"
              "<strong>DECISIONES ABIERTAS PARA EL DUEÑO:</strong> (1) qué versión del bucle —completa, intermedia o mínima— según los días que sobren al llegar a Guinea en la subida; "
              "(2) si merece la pena invertir tiempo antes del viaje en verificar el paso de Kabala-Faranah, que es lo que convertiría el desvío en variante; "
              "(3) si el agujero documental del perro se considera asumible: hoy no hay ninguna fuente sobre la entrada de animales en Sierra Leona, y ese es el riesgo que puede hacer que el bucle se caiga en la propia frontera."),
    facts=[
        ("Estatus en la ruta", "ALTERNATIVA. Fuera de la ruta fija. Bucle opcional insertable en el corredor de SUBIDA, entre Guinea y Senegal."),
        ("Ventana prevista", "Solo en la subida, después del corredor guineano de la Alta Guinea y antes de encarar Koundara y Senegal."),
        ("Coste de la desviación", "Completa ~2.000 km / 14-18 días · intermedia ~1.400 km / 10-12 días · mínima ~700 km / 5-7 días."),
        ("Entrada", "Gbalamuya/Pamelap desde Guinea, carretera Conakry-Freetown asfaltada. Único paso bien documentado."),
        ("Salida", "Por defecto, la misma frontera. Alternativas por el norte (Kamakwie/Madina Oula y Kabala/Faranah) POR CONFIRMAR."),
        ("Visado", "Visado A LA LLEGADA disponible en Gbalamuya desde septiembre de 2019 y GRATUITO para ciudadanos de la UE, un mes de validez. Es la gran ventaja administrativa frente a Liberia. CONFIRMAR por escrito antes de salir."),
        ("Vehículo", "La web oficial de turismo acepta expresamente carnet de paso en aduana O permiso de importación temporal, más seguro Brown Card de la CEDEAO."),
        ("Perro", "AGUJERO NEGRO DOCUMENTAL: ninguna fuente oficial ni testimonio localizado. Es el mayor riesgo del bucle."),
        ("Calendario", "Solo en seca: diciembre-abril, óptimo enero-marzo. En lluvias (mayo-noviembre) las pistas a Tiwai, Loma y Outamba son impracticables."),
        ("Seguridad", "Estable y cordial, sin conflicto activo. Precaución normal. El riesgo real es la carretera y el aislamiento, no la violencia."),
        ("Salud", "Fiebre amarilla obligatoria. Malaria intensa todo el año. Fiebre de Lassa endémica en el este (Kenema). El brote de ébola de 2014-2016 terminó en 2016."),
        ("Comunicaciones", "Starlink ACTIVO (de los primeros de África occidental). SIM local Orange SL / Africell en ciudades."),
        ("Dinero", "Leone (SLE). Cajeros en Freetown, Bo, Kenema y Makeni; fuera de ahí, efectivo. Llevar euros o dólares como respaldo."),
    ],
    alerts=[
        "ESTATUS: Sierra Leona NO está en la ruta fija. Todo lo que hay en esta ficha es condicional a que sobren días en el corredor de subida. No comprometer reservas ni trámites hasta que esa decisión esté tomada.",
        "Perro — AGUJERO NEGRO: no se ha localizado ninguna fuente oficial ni ningún testimonio sobre la importación de animales de compañía en Sierra Leona. El dosier del perro del proyecto ya marcaba el país como «sin confirmar». Es el punto que puede hacer fracasar el bucle EN LA PROPIA FRONTERA, y hay que resolverlo por escrito con seis meses de antelación.",
        "Estación de lluvias: de mayo a noviembre, con agosto por encima de 380 mm en el norte. Con solo el 8 % de la red asfaltada, las pistas a Tiwai, a Sinekoro (Bintumani) y a Outamba se vuelven impracticables. Si la subida cae en lluvias, el bucle se reduce a la península de Freetown o se cancela.",
        "Salidas alternativas por el norte (Kamakwie/Madina Oula y Kabala/Faranah) SIN VERIFICAR: son pasos menores que pueden no tener aduana habilitada para vehículo extranjero ni capacidad de sellar CPD. No planificar el bucle contando con ellos hasta confirmarlos.",
        "Visado a la llegada: la fuente localizada indica que se expide en Gbalamuya y que es gratuito para la UE, pero es un régimen que cambia con facilidad y la fuente no es el propio servicio de inmigración. CONFIRMAR por escrito 30-60 días antes; llevar plan B de eVisa tramitada.",
        "Certificado de fiebre amarilla obligatorio y comprobado en frontera. Llevarlo encima con el pasaporte, no en el fondo de una mochila.",
        "Fiebre de Lassa endémica en la Provincia Oriental (Kenema, Kailahun): se transmite por contacto con excretas de roedores. No dormir sobre el suelo en zonas rurales del este, guardar toda la comida cerrada, y no manipular roedores ni carne de monte bajo ningún concepto.",
        "El Cotton Tree de Freetown SE DERRUMBÓ el 24 de mayo de 2023: cualquier guía o ficha anterior lo describe como si siguiera en pie. Queda parte del tronco y el lugar, no el árbol.",
        "Drones: sin procedimiento turístico verificado. Criterio del proyecto, no volar sin autorización escrita de la SLCAA. Evitar en cualquier caso Freetown, Lungi, Bunce Island, Tacugama, Gola, Tiwai y las zonas mineras del este.",
        "Sin embajada de España en Freetown: la referencia consular es la Embajada en Conakry (Guinea). Ventaja relativa de este bucle: está a un día de camino, en el país por el que se entra y se sale.",
        "No comprar diamantes ni piedras a particulares en Kenema ni en Kono bajo ningún concepto: además del riesgo legal y de estafa, es la economía que financió la guerra.",
        "La guerra civil (1991-2002) y el ébola (2014-2016) son materia sensible y reciente: hay gente con amputaciones por la calle y familias que perdieron a todos sus miembros en el brote. No se fotografía, no se pregunta a la ligera y no se convierte en anécdota de viaje.",
    ],
    ruta_intro=("El bucle se recorre en sentido horario para no repetir carretera dentro del país. El <strong>primer tramo</strong> entra por Gbalamuya, baja a Freetown y dedica varios días a la "
                "<strong>península</strong> —las playas, el parque nacional, Tacugama, las islas Banana y Bunce Island— para después cruzar al <strong>sureste</strong> por Bo y Kenema hasta Gola, Tiwai y, si hay margen, "
                "la costa perdida de Sulima. El <strong>segundo tramo</strong> vuelve hacia el norte por Makeni y Kabala, sube el <strong>monte Bintumani</strong> y sale por <strong>Outamba-Kilimi</strong> hacia la frontera. "
                "Etapas calculadas sobre <strong>250 km/día</strong>, reducidos a <strong>100-120 km/día</strong> en las pistas de Tiwai, Sinekoro y Outamba. "
                "Las etapas marcadas como OPCIONAL son las primeras que se recortan si el calendario aprieta: sin ellas, el bucle baja a ~1.400 km y 10-12 días; quedándose solo en la península, a ~700 km y 5-7 días."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bucle 1 · Entrada", "Coyah/Forécariah (Guinea) → Pamelap → Gbalamuya → Kambia → Port Loko → Freetown", "~185 km en Sierra Leona · 1-2 días (la frontera se come medio día)"),
        ("Bucle 2 · Capital", "Freetown: Cotton Tree, Big Market, Museo del Ferrocarril, trámites y taller", "2-3 noches · base logística del bucle"),
        ("Bucle 3 · Bosque de la península", "Freetown → Tacugama → Sugar Loaf / Guma", "~40 km · 1-2 días (senderismo)"),
        ("Bucle 4 · Las playas", "Freetown → River No. 2 → Tokeh → Bureh → Kent", "~50 km · 3-4 días — el bloque de descanso del bucle"),
        ("Bucle 5 · Islas Banana", "Kent → Dublin/Ricketts (barca) → Kent", "barca 20-40 min · 1-2 días"),
        ("Bucle 6 · Bunce Island", "Freetown (Aberdeen/Tagrin) → Bunce Island → Freetown", "barca ~1 h cada trayecto · ½-1 día"),
        ("Bucle 7 · Islas Turtle (OPCIONAL)", "Freetown → Turtle Islands (barca, 3 h) → Freetown", "~6 h de barca · 2-3 días — la primera etapa que se cae"),
        ("Bucle 8 · Al sureste", "Freetown → Masiaka → Moyamba Junction → Bo", "~250 km · 1 día de asfalto"),
        ("Bucle 9 · El país del diamante", "Bo → Kenema (+ colinas de Kambui)", "~65 km · 1 noche"),
        ("Bucle 10 · Selva UNESCO", "Kenema → Gola Rainforest NP (caminatas con guía comunitario)", "~90 km · 1-2 días"),
        ("Bucle 11 · Los once primates", "Kenema → Potoru → Isla de Tiwai (pista + barca)", "~110 km · 2 días — el punto natural fuerte del país"),
        ("Bucle 12 · Costa perdida (OPCIONAL)", "Potoru → Zimmi → Sulima (desembocadura del Moa) → Zimmi", "~180 km ida y vuelta · 1-2 días — pista, confirmar estado"),
        ("Bucle 13 · Regreso al norte", "Zimmi/Potoru → Bo → Makeni", "~300 km · 1-2 días"),
        ("Bucle 14 · A la montaña", "Makeni → Kabala (Gbawuria)", "~120 km · 1 noche"),
        ("Bucle 15 · El techo de África occidental", "Kabala → Sinekoro → monte Bintumani (1.945 m) → Kabala", "~180 km ida y vuelta + 3-4 días a pie"),
        ("Bucle 16 · Sabana y hipopótamos", "Kabala → Kamakwie → Outamba-Kilimi → Kamakwie", "~270 km ida y vuelta · 2-3 días"),
        ("Bucle 17 · Salida", "Kamakwie → Kambia → Gbalamuya (Guinea) — o salida norte POR CONFIRMAR", "~200 km · 1-2 días"),
    ],
    offroad=[
        "Acceso a la isla de Tiwai desde Potoru (~15 km de pista + barca sobre el Moa): es el tramo 4x4 clásico del país. Pista de tierra roja por plantaciones y bosque hasta el embarcadero, con vados y roderas profundas; en cuanto llueve en serio se corta. Los vehículos se dejan en el embarcadero y se cruza en barca a la isla. Confirmar el estado con la Environmental Foundation for Africa antes de salir de Kenema.",
        "Aproximación al monte Bintumani desde Kabala hasta los pueblos del pie de monte (Sinekoro y alrededores, ~90 km): pista de montaña larga, con vados y tramos de laterita profunda, en una zona sin servicios ni cobertura. Es el acceso más comprometido del bucle y solo tiene sentido en seca. Los dos vehículos juntos, autonomía completa de combustible desde Makeni y aviso en Kabala de a dónde se va y cuándo se vuelve.",
        "Kabala → Kamakwie → Fintonia / Outamba-Kilimi (~210 km): pistas de sabana del noroeste, llanas pero con vados de río que son el problema real, porque el parque está precisamente definido por sus ríos. Terreno bueno de conducir en seca, impracticable en lluvias. Es el tramo que enlaza la montaña con el parque y con la frontera norte.",
        "Zimmi → Sulima (~60 km): pista al extremo suroriental del país, hasta la desembocadura del Moa. Poco tráfico, estado muy variable y ninguna referencia reciente localizada: preguntar en Zimmi antes de meterse. Es la pista más remota del bucle.",
        "Carretera de la península de Freetown (asfaltada): no es 4x4, pero merece mención porque es una de las carreteras costeras más bonitas de África occidental — cornisa entre montaña selvática y playas, con las curvas colgadas sobre el mar entre Lakka, River No. 2, Tokeh y Bureh hasta Kent. Se hace entera en una mañana y es el contrapunto fácil a las pistas del interior.",
        "Estacionalidad, resumen operativo: solo el 8 % de los 11.300 km de red del país está asfaltado, y la estación de lluvias (mayo-noviembre, pico en julio-septiembre) convierte el 92 % restante en barro. La red asfaltada —Gbalamuya-Freetown, Freetown-Bo-Kenema, Freetown-Makeni-Kabala— aguanta todo el año; todo lo demás es un plan de diciembre a abril.",
    ],
    senderismo=[
        "Monte Bintumani (1.945 m), montañas Loma · 3-4 días: la gran excursión del país y el punto más alto de África occidental al oeste del Camerún. Se sube desde los pueblos del pie de monte —Sinekoro es el arranque clásico— con guía y porteadores contratados allí, atravesando bosque de galería y selva de montaña hasta una pradera de altura abierta con vistas sobre Guinea. Reserva forestal de caza vedada desde 1952 (33.201 ha) y área importante para las aves. Solo en seca. Es terreno comunitario, no parque nacional con depredadores: el perro puede ir, con correa y valorando el esfuerzo y el calor.",
        "Sugar Loaf (~760 m) y Picket Hill, Parque Nacional de la Península: la montaña que domina Freetown, con senderos de selva semidecidua que arrancan de los pueblos de la península y del entorno del embalse de Guma. Media jornada larga, mucha humedad, y vistas sobre la ciudad, el estuario y el Atlántico. La mejor caminata del país compatible con el perro.",
        "Senderos de Tacugama: además del recorrido guiado por los recintos de chimpancés, el santuario mantiene senderos de bosque dentro del parque nacional. Reservar con antelación. El perro se queda fuera.",
        "Colina de Gbawuria, Kabala: subida corta desde el pueblo, con vistas sobre el valle y las montañas de Koinadugu. Cada 1 de enero sube media Sierra Leona a celebrar el año nuevo; el resto del año está vacía. Apta para el perro.",
        "Caminatas de selva en Gola Rainforest (UNESCO): rutas con guía comunitario desde los pueblos del borde del parque, de medio día a varios días. No es safari: es bosque primario, aves —más de 330 especies, uno de los mejores destinos ornitológicos de África occidental— y rastros. Botas, humedad extrema.",
        "Isla de Tiwai: la isla se recorre a pie por senderos marcados, con guías del pueblo, buscando las once especies de primates; hay además salidas nocturnas para gálagos y potos, y paseos en barca al amanecer por el Moa buscando rastro de hipopótamo pigmeo. Es caminata fácil en terreno llano, pero larga y muy húmeda.",
        "Colinas de Kambui (Kenema): reserva forestal a las puertas de la ciudad, con senderos poco frecuentados y buena observación de aves. Es la caminata de relleno del sureste si sobra medio día.",
        "Playas de la península: entre Lakka y Kent se pueden encadenar kilómetros de arena a pie a primera hora, saltando de cala en cala. River No. 2 → Tokeh es la combinación más cómoda, con el río de agua dulce al final.",
    ],
    acampada=[
        "Bureh Beach: el sitio más fácil del país para acampar con los vehículos. El club de surf del pueblo gestiona cabañas y camping en la propia arena, con ambiente de viajeros y hogueras por la noche. Es la base recomendada de la península si se va con vehículo propio.",
        "River No. 2: alojamiento comunitario en cabañas gestionadas por la asociación del pueblo, con explanada para aparcar. Menos «camping» y más bungalow, pero es el sitio más bonito de la costa.",
        "Tokeh: resorts y chiringuitos con aparcamiento; opción de pagar por acampar preguntando en el pueblo.",
        "Freetown: aparcamiento vigilado obligatorio. La densidad urbana y el tráfico hacen desaconsejable dejar los vehículos sin vigilancia. Hoteles de Aberdeen y Lumley con recinto cerrado.",
        "Isla de Tiwai: campamento de tiendas sobre plataforma de madera gestionado por la Environmental Foundation for Africa, con guías del pueblo. Los vehículos se quedan en el embarcadero de Potoru — confirmar la custodia al reservar.",
        "Outamba-Kilimi: cabañas sencillas de materiales locales, individuales y colectivas, dentro del parque. Es alojamiento básico de verdad: llevar saco, mosquitera y comida.",
        "Montañas Loma: vivac de montaña con los porteadores en los altos de la ruta a Bintumani, y alojamiento elemental en los pueblos del pie de monte con permiso del jefe del pueblo. No hay infraestructura ninguna.",
        "Regla general del interior: fuera de la península y de las ciudades grandes, la fórmula que funciona es pedir permiso al jefe del pueblo antes de instalarse. A cambio se consigue vigilancia informal y a menudo agua.",
    ],
    visado=[
        "VENTAJA CLAVE DEL BUCLE: Sierra Leona expide VISADO A LA LLEGADA en la frontera terrestre, y no solo en el aeropuerto. Según la fuente localizada, el régimen está en vigor desde el 5 de septiembre de 2019 y se aplica en tres puntos: el aeropuerto internacional de Freetown y los pasos terrestres de Gbalamuya (Guinea) y Jendema (Liberia). Es exactamente lo contrario del caso liberiano y la razón por la que este bucle es viable y el liberiano no.",
        "Para ciudadanos de la Unión Europea el visado a la llegada es GRATUITO, con un mes de validez. Otros países pagan 80 USD. CONFIRMAR por escrito 30-60 días antes: la fuente localizada no es el propio servicio de inmigración y este tipo de régimen cambia con facilidad.",
        "PLAN B recomendado de todas formas: llevar tramitada la eVisa sierraleonesa antes de salir de España o desde Conakry. Cuesta dinero, pero elimina el único riesgo administrativo serio de la entrada y evita depender del criterio del funcionario de turno en Gbalamuya.",
        "Certificado internacional de fiebre amarilla obligatorio y comprobado en el puesto, sin excepciones.",
        "Un mes de validez es de sobra para cualquiera de las tres versiones del bucle, incluso la completa de 18 días. No hay problema de duración.",
        "Llevar fotocopias del pasaporte, del sello de entrada y de la documentación del vehículo para los controles de carretera.",
    ],
    fronteras_rows=[
        ("Entrada del bucle", "Gbalamuya / Pamelap (desde Guinea)", "Carretera Conakry-Freetown, asfaltada de punta a punta; el paso principal del país y el único bien documentado. Visado a la llegada disponible aquí (gratuito UE, por confirmar). Vehículo: permiso de circulación, carnet, pasaporte, seguro válido en Sierra Leona (Brown Card CEDEAO recomendada) y CPD o permiso de importación temporal. Fiebre amarilla comprobada. Varias horas de trámite por colas: cruzar de día."),
        ("Salida por defecto", "Gbalamuya / Pamelap (de vuelta a Guinea)", "Se sale por donde se entró y se retoma el corredor guineano de subida por Forécariah-Coyah-Kindia-Mamou-Labé. Segura y documentada; el precio es repetir el tramo Kambia-Freetown dentro de Sierra Leona, que se minimiza haciendo el bucle en sentido horario."),
        ("Salida alternativa · POR CONFIRMAR", "Kamakwie / Madina Oula (hacia Kindia, Guinea)", "Paso menor del noroeste, a la salida de Outamba-Kilimi. Evitaría repetir Gbalamuya. SIN DOCUMENTACIÓN OPERATIVA localizada: verificar que tiene aduana habilitada para vehículo extranjero y que puede sellar el CPD antes de contar con él."),
        ("Salida alternativa · POR CONFIRMAR", "Kabala / Faranah (hacia la Alta Guinea)", "Sería el encaje ideal: conectaría Kabala y las Loma directamente con Faranah y con el corredor guineano de subida por Dabola, sin repetir un solo kilómetro. Paso secundario, en pista, con aduana incierta. VERIFICARLO es la pregunta técnica más rentable de esta ficha."),
        ("No se usa", "Jendema / Bo-Waterside (hacia Liberia)", "Operativo y con visado sierraleonés a la llegada, pero NO se usa: Liberia está excluida de la ruta fija por el problema del visado liberiano (ver su ficha). Se documenta por si ese problema se resolviera."),
    ],
    vehiculos=[
        "La web oficial de turismo de Sierra Leona acepta expresamente DOS vías para el vehículo: carnet de paso en aduana (CPD) O permiso de importación temporal emitido en la frontera. Es una de las pocas fronteras de la ruta donde la fuente oficial reconoce las dos.",
        "Seguro de responsabilidad civil válido en Sierra Leona: la Brown Card / Carte Brune de la CEDEAO está expresamente recomendada por la fuente oficial. Confirmar que la póliza contratada cubre Sierra Leona por nombre y que la vigencia alcanza las fechas del bucle.",
        "Permiso internacional de conducir, permiso de circulación y pasaporte: se piden juntos en el puesto y en los controles.",
        "Inspección del vehículo y despacho de aduana en la frontera, con varias horas posibles de espera por colas de camiones.",
        "Autonomía de combustible: el punto crítico es el bloque de montaña. Salir de Makeni con depósitos y garrafas llenos para cubrir Kabala, la aproximación a Bintumani, Kamakwie y Outamba y la vuelta (~500-600 km con consumo de pista y suministro incierto en Kabala y Kamakwie).",
        "Neumáticos y suspensión: laterita profunda y vados en todos los accesos buenos (Tiwai, Sinekoro, Outamba). Freetown es la única plaza con recambios de cierto nivel; Bo y Makeni tienen talleres elementales.",
        "Filtro de embudo para el gasóleo fuera de Freetown: en Kabala y Kamakwie el combustible se compra a veces en garrafa.",
        "Conducción por la DERECHA, como en Guinea y en toda la subregión: no hay cambio de lado en este bucle.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Sin procedimiento turístico verificado: solicitar autorización previa y por escrito a la Sierra Leone Civil Aviation Authority (SLCAA) o, en su defecto, no volar el dron en el país. POR CONFIRMAR si existe formulario público.",
        "Nunca sobrevolar Freetown, el puerto, el aeropuerto internacional de Lungi ni edificios de gobierno.",
        "Nunca sobrevolar Bunce Island ni los demás sitios de la Monuments and Relics Commission sin permiso expreso: son monumentos nacionales protegidos desde 1948.",
        "Nunca sobrevolar Tacugama, Gola ni Tiwai: son espacios con grandes simios y normativa propia; el ruido de un dron es una perturbación seria.",
        "Zonas mineras del este (Kenema, Kono) y concesiones de rutilo y hierro: seguridad privada y sensibilidad alta. No volar.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio ACTIVO confirmado en las fuentes consultadas a mediados de 2026: Sierra Leona fue de los primeros mercados de África occidental en tener Starlink operativo.",
        "Consecuencia operativa concreta: este bucle es una buena ventana para resolver todo lo que en Guinea es difícil o imposible por falta de ancho de banda — visados del bloque siguiente, gestiones del perro, copias de seguridad, llamadas largas. Aprovecharlo desde Freetown o desde las playas de la península.",
        "SIM/eSIM local (Orange SL, Africell) como respaldo urbano y para gestiones cotidianas. Cobertura móvil aceptable en Freetown, la península, Bo, Kenema, Makeni y Kabala.",
        "Cobertura nula o muy degradada en las Loma (aproximación y ascensión a Bintumani), en Outamba-Kilimi, en Tiwai y en la pista de Sulima: dar por hecho 2-3 días incomunicados en cada bloque y avisar antes de entrar.",
        "Revisar el mapa oficial 30-60 días antes por si cambia el marco de itinerancia o la cobertura.",
    ],
    perro_intro=[
        "AGUJERO NEGRO DOCUMENTAL — es el mayor riesgo de este bucle. No se ha localizado NINGUNA fuente oficial sobre la importación de animales de compañía en Sierra Leona: ni norma publicada, ni ficha veterinaria internacional, ni testimonio de viajero. El dosier del perro del proyecto ya clasificaba el país como «sin confirmar», y esta revisión no ha podido cerrarlo.",
        "AUTORIDAD PROBABLE: el Ministerio de Agricultura y Seguridad Alimentaria (Ministry of Agriculture and Food Security) de Sierra Leona, a través de su servicio veterinario y de ganadería. NO se ha podido verificar el nombre exacto de la dirección competente ni un procedimiento publicado: POR CONFIRMAR. Interlocutores adicionales: la Alta Comisión / Embajada de Sierra Leona ante España o Francia, y la Embajada de España en Conakry, que es la que cubre el país.",
        "PREPARACIÓN MÍNIMA por analogía con los vecinos de la CEDEAO (Guinea, Costa de Marfil, Liberia), mientras no haya respuesta oficial: microchip; pasaporte europeo de animal de compañía; vacuna antirrábica en vigor y con menos de 12 meses; certificado veterinario internacional expedido por veterinario habilitado lo más cerca posible de la fecha de cruce (asumir una ventana de 72 h, que es lo que exigen Guinea y varios vecinos); y titulación serológica de anticuerpos antirrábicos hecha desde España — no la exige ningún país de la zona, pero SÍ es imprescindible para volver a la UE.",
        "DÓNDE CONSEGUIR EL CERTIFICADO: si la ventana es de 72 h, hay que obtenerlo en Guinea justo antes de cruzar. Conakry es la plaza realista; el Laboratoire Régional Vétérinaire de Labé, ya identificado en la ficha de Guinea, es el recurso del interior. Planificar el bucle de forma que el cruce de Gbalamuya caiga pocos días después de pasar por una de las dos.",
        "IDIOMA: al contrario que todos sus vecinos, Sierra Leona es ANGLÓFONA. Eso significa que el pasaporte europeo de animal de compañía en su versión inglesa sirve aquí directamente, mientras que en Guinea y Costa de Marfil hace falta francés. Es una simplificación pequeña pero real.",
        "DOBLE CRUCE: si se sale por Gbalamuya y se vuelve a entrar en Guinea, hará falta un NUEVO certificado internacional para la reentrada guineana dentro de su ventana de 72 h — conseguido en Freetown. Localizar un veterinario habilitado en Freetown ANTES de entrar, no al salir. Este punto se olvida con facilidad y es el que puede dejar el bucle bloqueado por el lado de vuelta.",
        "REGLA DE TRABAJO DEL PROYECTO: «no mencionado ≠ prohibido». No hay ninguna fuente que prohíba la entrada terrestre de un perro en Sierra Leona; simplemente no hay ninguna fuente. Se trabaja como viable con documentación completa, pero sin darlo por cerrado y con la decisión del bucle explícitamente condicionada a conseguir una respuesta por escrito.",
        "CRITERIO DE SEGURIDAD: la rabia circula y hay muchísimo perro sin vacunar en pueblos y ciudades. Vacuna al día, correa siempre y ninguna interacción con perros locales. La vacunación antirrábica del propio viajero (preexposición) es especialmente recomendable aquí.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional OBLIGATORIO y comprobado en frontera, sin excepciones. La zona de Makeni y el norte son endémicas.",
        "Malaria en todo el país y todo el año, con transmisión muy intensa: es uno de los países con mayor carga del mundo. Profilaxis a valorar con Sanidad Exterior, mosquitera, repelente con DEET y manga larga al atardecer.",
        "FIEBRE DE LASSA: endémica en la Provincia Oriental (Kenema, Kailahun) — precisamente la zona de Gola y Tiwai. Se transmite por contacto con orina y excrementos de roedores, o con sus secreciones. Medidas concretas: no dormir directamente sobre el suelo en alojamientos rurales del este, guardar TODA la comida en recipientes cerrados, no dejar restos, no manipular roedores y no comer carne de monte bajo ningún concepto. El Kenema Government Hospital tiene una de las pocas unidades del mundo especializadas, en funcionamiento desde los años setenta.",
        "ÉBOLA — contexto y situación actual: el brote de África occidental de 2014-2016 golpeó a Sierra Leona con una dureza extrema (cerca de 4.000 muertos confirmados) y el primer caso del país se diagnosticó en Kenema el 25 de mayo de 2014. El país fue declarado libre de transmisión en 2016 y NO hay transmisión activa: la situación sanitaria actual es completamente distinta. Lo que queda es una vigilancia epidemiológica reforzada, protocolos de lavado de manos a la entrada de muchos edificios y un sistema sanitario que perdió mucho personal. Comprobar de todos modos el estado epidemiológico con la OMS y el ECDC 30-60 días antes de entrar, como con cualquier país de la región.",
        "Agua: no beber del grifo en ningún punto del país. Agua embotellada o en bolsa en Freetown, Bo, Kenema y Makeni; en la península hay agua corriente en los alojamientos. En Tiwai, las Loma y Outamba, el agua es de río o de pozo: filtro mecánico más tratamiento químico o ebullición, siempre.",
        "Vacunación recomendada además: hepatitis A y B, fiebre tifoidea, tétanos-difteria, meningitis, poliomielitis y RABIA (preexposición) — esta última especialmente relevante viajando con perro y con alta densidad de perros sin vacunar.",
        "Referencias hospitalarias: Connaught Hospital en Freetown (el principal, con capacidad limitada para politraumatismos), Holy Spirit Hospital en Makeni (el mayor privado del norte y la referencia del bloque de montaña) y Kenema Government Hospital en el este. En las Loma, en Outamba y en Tiwai no hay absolutamente nada.",
        "Seguro con evacuación médica AÉREA imprescindible: la evacuación realista desde Sierra Leona es a Dakar o a Europa. Con el bloque de Bintumani, además, hay que contar con uno o dos días solo para bajar de la montaña.",
        "Calor y humedad: la costa y el sureste son húmedos y agotadores todo el año; Kabala y la montaña son secos y frescos, y son el sitio donde se descansa de verdad. Planificar los bloques de esfuerzo (Bintumani) en el norte y los de descanso en la península.",
    ],
    seguridad_intro=("Sierra Leona es hoy un país estable, sin conflicto activo, con elecciones democráticas sucesivas desde 2002 y fama merecida de ser uno de los más cordiales de África occidental. "
                     "El riesgo real del bucle <strong>no es la seguridad personal</strong>: es la <strong>carretera</strong> —solo el 8 % de la red está asfaltada y la estación de lluvias arrasa el resto— y el "
                     "<strong>aislamiento</strong> de los tramos buenos (las Loma, Outamba, Tiwai, Sulima), donde no hay cobertura, ni combustible, ni tráfico del que depender."),
    seguridad=[
        "Sin conflicto armado ni zonas vedadas en el itinerario. Hubo protestas violentas en agosto de 2022 y un ataque armado en Freetown en noviembre de 2023, ambos superados, pero indican que la tensión política puede aflorar: evitar concentraciones y revalidar el estado del país 30-60 días antes.",
        "No conducir de noche fuera de Freetown y de la península: firme irregular, ausencia de señalización, peatones, ganado y camiones sin luces. Es la causa de accidente número uno del país.",
        "Aislamiento de los tramos buenos: en las Loma, en Outamba, en Tiwai y en la pista de Sulima no hay cobertura móvil ni tráfico. Los dos vehículos siempre juntos, autonomía completa de agua y combustible, y dejar dicho en Kabala, Kamakwie o Potoru a dónde se va y cuándo se vuelve.",
        "Freetown: delincuencia urbana común (tirones, robos en atascos, carterismo en los mercados). Ventanillas subidas en atasco, nada visible en el salpicadero, aparcamiento vigilado y no circular de noche por la ciudad.",
        "Controles de carretera: existen y son en general correctos. Documentación en carpeta con copias, saludo en inglés o en krio, paciencia. Las peticiones informales son moderadas comparadas con otros países de la ruta.",
        "No fotografiar instalaciones militares, policiales, el puerto, el aeropuerto de Lungi ni las concesiones mineras. En el mercado del diamante de Kenema, preguntar antes de sacar la cámara.",
        "No comprar diamantes ni piedras a particulares: riesgo legal, estafa garantizada y una economía que financió once años de guerra.",
        "Barcas: es el punto donde más se relajan los estándares. En las travesías a las Banana, a Bunce y sobre todo a las Turtle, comprobar chalecos, no embarcar sobrecargado y no salir con mal tiempo. Es un riesgo real, no teórico.",
        "Sensibilidad histórica: la guerra civil terminó en 2002 y el ébola en 2016; hay gente con amputaciones por la calle y familias que perdieron a todos sus miembros. No se fotografía, no se pregunta a la ligera, no se convierte en anécdota.",
        "Dinero: cajeros en Freetown, Bo, Kenema y Makeni; fuera de ahí, efectivo. Llevar euros o dólares como respaldo y cambiar en banco o casa de cambio, no en la calle.",
    ],
    agua=[
        "Freetown, Bo, Kenema y Makeni: agua embotellada y en bolsa en supermercados y tiendas. Para el depósito de uso general (ducha, aseo, limpieza), estaciones de servicio, hoteles y misiones permiten llenar con manguera.",
        "Península de Freetown (River No. 2, Tokeh, Bureh, Kent): agua corriente en los alojamientos y arroyos de montaña abundantes que bajan del parque nacional. River No. 2 tiene además el río de agua dulce en la propia playa, ideal para lavar el equipo y al perro después del baño. Tratar siempre el agua de arroyo.",
        "Sureste (Gola, Tiwai, Sulima): agua de río o de pozo del pueblo, sin excepción. Filtro mecánico más tratamiento químico o ebullición. En Tiwai la proporciona el campamento; tratarla igualmente. Salir de Kenema con los depósitos llenos.",
        "Bloque de montaña (Kabala, Loma, Outamba): agua de pozo y de río. Es la zona más seca del país y la de menos infraestructura: llenar a fondo en Makeni y de nuevo en Kabala antes de subir a Sinekoro o de bajar a Kamakwie.",
        "En zona rural, preguntar en el pueblo antes de usar un pozo comunitario. Nunca beber del grifo en ningún punto del país.",
    ],
    combustible=[
        "Sin ningún hueco de 500 km en el bucle: la red formal cubre Freetown, Bo, Kenema y Makeni, y los tres ejes asfaltados (Gbalamuya-Freetown, Freetown-Bo-Kenema, Freetown-Makeni-Kabala) tienen estaciones suficientes.",
        "Repostar a fondo en Freetown, que tiene la mejor oferta y calidad del país, antes de bajar a la península y antes de salir hacia el sureste.",
        "Bo es el último repostaje seguro antes de Tiwai, Gola y Sulima: bajar con el depósito lleno y garrafas, porque en Potoru y en Zimmi el suministro es informal.",
        "AVISO — bloque de montaña: Makeni es el último repostaje seguro. Kabala y Kamakwie tienen puntos de venta elementales y a veces en garrafa, sin garantía. Salir de Makeni con depósitos y garrafas al 100 % para cubrir Kabala + aproximación a Bintumani + Kamakwie + Outamba + vuelta (~500-600 km con consumo de pista).",
        "Filtro de embudo obligatorio fuera de Freetown y de las capitales: la calidad del gasóleo en garrafa es imprevisible.",
        "Confirmar puntos recientes en iOverlander antes de cada tramo rural; las estaciones del interior pueden estar secas durante días.",
    ],
    experiencias_intro=("Relatos, avisos y datos de campo de otros viajeros y de la propia web oficial de turismo del país, para contrastar con la planificación. Sierra Leona está mucho mejor documentada que Guinea en lo que toca a "
                        "fronteras y vehículo —tiene una web oficial de turismo que responde preguntas concretas— y mucho peor en todo lo demás. Se marca expresamente lo que sigue sin testimonio:"),
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("DECISIÓN DEL DUEÑO · activar o no el bucle", "Decidir, al llegar a Guinea en la subida, qué versión del bucle cabe en el calendario: completa (~2.000 km / 14-18 días), intermedia (~1.400 km / 10-12 días), mínima (~700 km / 5-7 días) o ninguna. Criterio de cierre: días disponibles reales y estación (solo tiene sentido de diciembre a abril)"),
        ("Perro · AGUJERO NEGRO", "Escribir con 6 meses de antelación al Ministerio de Agricultura y Seguridad Alimentaria de Sierra Leona y a la representación diplomática sierraleonesa en España o Francia: confirmar (1) requisitos de entrada de un perro de compañía por frontera TERRESTRE, (2) si hace falta permiso de importación previo, (3) ventana de validez del certificado veterinario. Criterio de cierre: respuesta por escrito, o confirmación verbal registrada con nombre y cargo. SIN ESTO, EL BUCLE NO SE ACTIVA"),
        ("Perro · certificado de reentrada en Guinea", "Localizar un veterinario habilitado en FREETOWN antes de entrar, para el certificado internacional que exigirá Guinea al volver dentro de su ventana de 72 h. Es el punto que se olvida y que puede bloquear la salida del bucle"),
        ("Perro · testimonio overland", "Buscar activamente en iOverlander y en foros overland a alguien que haya entrado en Sierra Leona con vehículo propio y animal de compañía. No se ha localizado ni uno"),
        ("Visado a la llegada", "Confirmar por escrito con el servicio de inmigración sierraleonés o con su representación diplomática que el visado a la llegada sigue vigente en Gbalamuya y sigue siendo gratuito para la UE. PLAN B: tramitar eVisa antes de salir. Criterio de cierre: confirmación documental 30-60 días antes"),
        ("Paso de Kabala / Faranah", "PREGUNTA TÉCNICA MÁS RENTABLE DE ESTA FICHA. Verificar si el paso Kabala-Faranah existe, está abierto a extranjeros, tiene aduana capaz de sellar CPD y es practicable en 4x4. Si funciona, el bucle deja de ser un desvío y se convierte en una variante de ruta sin repetición de kilómetros"),
        ("Paso de Kamakwie / Madina Oula", "Verificar lo mismo para la salida noroeste desde Outamba-Kilimi hacia Kindia. Segunda opción tras Kabala-Faranah"),
        ("Pistas de Tiwai, Sinekoro y Outamba", "Confirmar estado 7-15 días antes con la Environmental Foundation for Africa (Tiwai), con los guías de Kabala (Loma) y con la administración del parque (Outamba). En lluvias, dar por perdidos los tres accesos"),
        ("Tiwai · reserva", "Contactar con la Environmental Foundation for Africa para reservar el campamento, confirmar tasas, guías y la custodia de los dos vehículos en el embarcadero de Potoru"),
        ("Bintumani · guías y porteadores", "Organizar desde Kabala con antelación: guía, porteadores, permisos de los pueblos del pie de monte, y confirmar si el perro puede acompañar en la subida"),
        ("Gola · acceso tras la declaración UNESCO", "Confirmar con la Conservation Society of Sierra Leone el procedimiento de visita, tasas y guías; la inscripción como Patrimonio Mundial en 2025 puede haber cambiado el régimen de acceso"),
        ("Pista de Sulima", "Confirmar el estado de la pista Zimmi-Sulima antes de meterse. Es la más remota del bucle y no hay referencias recientes localizadas"),
        ("Drones · SLCAA", "Resolver autorización por escrito ante la Sierra Leone Civil Aviation Authority o excluir el dron del país. POR CONFIRMAR si existe procedimiento publicado"),
        ("Salud · Lassa y ébola", "Comprobar con OMS y ECDC el estado epidemiológico de la Provincia Oriental (Lassa) 30-60 días antes de entrar"),
        ("Barcas a las islas", "Confirmar operadores y estado de las embarcaciones para Banana, Bunce y Turtle, y si admiten al perro. Las Turtle son la etapa más fácil de sacrificar del bucle"),
        ("Fotos pendientes de sustituir", "Todos los PDIs de esta ficha reutilizan cuatro imágenes de Sierra Leona verificadas en Wikimedia Commons (Cotton Tree, chimpancé occidental, River No. 2 e islas Banana), porque no se ha podido verificar ningún otro archivo. Sustituir por fotos propias o por archivos verificados a medida que aparezcan. AVISO: la foto del Cotton Tree es anterior a su derrumbe de mayo de 2023"),
    ],
    sources=SOURCES,
    sources_note=("Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha documenta una ALTERNATIVA, no un tramo de la ruta fija: Sierra Leona solo se visita si sobran días en el corredor de subida. "
                  "Es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Correcciones importantes de esta revisión: (1) el Cotton Tree de Freetown se derrumbó el 24 de mayo de 2023 y la versión "
                  "anterior de esta ficha lo describía como si siguiera en pie; (2) el complejo Gola-Tiwai fue inscrito como Patrimonio Mundial de la UNESCO en 2025, el primero del país; (3) Sierra Leona expide visado a la llegada en la "
                  "frontera terrestre de Gbalamuya, gratuito para la UE — lo contrario del caso liberiano; (4) la salida hacia Liberia que figuraba en la versión anterior queda eliminada del plan, porque Liberia está excluida de la ruta. "
                  "Sigue abierto, y es el mayor riesgo del bucle, el agujero documental sobre la entrada del perro."),
    emergency="Policía 019 · Emergencias 999 (numeración poco estandarizada: verificar localmente al llegar) · Sin embajada de España en Freetown: emergencia consular española grave (Conakry) +224 664 33 54 93 · Embajada de España en Conakry +224 664 20 22 01 · Sección consular +224 613 33 90 90.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

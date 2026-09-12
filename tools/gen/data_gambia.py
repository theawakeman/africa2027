# -*- coding: utf-8 -*-
"""Gambia — ficha completa, país de SOLO SUBIDA con dos corredores alternativos (12 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

# Solo hay dos imágenes de Gambia verificadas en Wikimedia Commons para esta revisión.
# Se reutilizan como IMAGEN DE REFERENCIA en los PDIs que aún no tienen foto propia, y así se
# dice expresamente en cada descripción. Ver "Fotos pendientes de sustituir" en decisiones.
IMG_RIO = W + "James%20Island%20near%20Juffureh%20(4129325186).jpg?width=900"
IMG_COSTA = W + "Kotu%20Beach%2C%20The%20Gambia%20(16197149546).jpg?width=900"

POIS = [
    # ===== EJE COSTERO (corredor principal): Séléti -> Kombos -> Banjul -> ferry -> Kunta Kinteh -> Amdalai =====
    dict(n=1, name="Kartong · playa, Folonko y el río Allahein", cat="Costa", prio="Media", dog="permitido", time="1 noche",
         lat=13.0833, lon=-16.7583,
         desc="El pueblo más al sur de Gambia, justo en la desembocadura del río Allahein, que es la frontera misma con la Casamance senegalesa — al otro lado de la ría se ve ya Senegal, y los vecinos la cruzan en piragua. Playa larguísima, prácticamente vacía, con una comunidad de ecoturismo veterana (Kartong es donde nació el turismo responsable gambiano), un observatorio de aves en las lagunas de la antigua cantera de arena, y la poza sagrada de FOLONKO, un estanque de cocodrilos venerado como lugar de fertilidad, mucho más discreto y menos turístico que el de Katchikally. Si se entra por el paso litoral en vez de por Séléti, ésta es la primera parada del país. Excelente para el perro: arena abierta, sin gestión de parque y alojamientos pequeños. Imagen de referencia de la costa gambiana, no de la propia Kartong.",
         credit="Wikimedia Commons", source=IMG_COSTA),
    dict(n=2, name="Tanji · pueblo de pescadores, museo y reserva de aves", cat="Costa", prio="Alta", dog="permitido con condiciones", time="½–1 día",
         lat=13.3500, lon=-16.7900,
         desc="La playa de pesca más viva del país: a media tarde vuelven las piraguas pintadas y toda la arena se convierte en un mercado de pescado, ahumaderos y hielo, con un ruido y un color que no tienen nada de espectáculo montado para turistas. Al lado, el TANJE VILLAGE MUSEUM reconstruye un complejo familiar mandinga tradicional con artesanos trabajando en vivo. A unos 3 km está la RESERVA DE AVES DEL RÍO TANJI (612 ha), con dunas, lagunas y las islas Bijol frente a la costa, la única colonia importante de charranes y gaviotas del país y zona de puesta de tortugas — las islas son de acceso restringido, se observan desde la playa o en barca. Uno de los mejores puntos de observación de aves costeras de África occidental. Perro con correa corta en la playa de pesca (mucho pescado, muchos perros locales) y fuera de la reserva.",
         credit="Wikimedia Commons", source=IMG_COSTA),
    dict(n=3, name="Reserva Natural de Abuko · la más antigua del país", cat="Naturaleza", prio="Alta", dog="prohibido", time="½ día",
         lat=13.3958, lon=-16.6456,
         desc="107 hectáreas de galería forestal a 20 minutos de Serrekunda, y el origen de toda la conservación gambiana: el arroyo de Lamin se valló en 1916 como captación de agua, y en 1968, por empeño del oficial de fauna Eddie Brewer, se convirtió en la PRIMERA RESERVA DE FAUNA DECLARADA DE GAMBIA — de ella nació el Departamento de Vida Silvestre. En un circuito a pie de dos horas se ven tres especies de mono (verde, colobo rojo y patas), cocodrilos del Nilo y enanos en la poza, varanos, y sobre todo más de 270 ESPECIES DE AVES en un espacio diminuto: turacos verdes, cálaos pintados occidentales, francolines de Ahanta. Es Área Importante para las Aves de BirdLife y la mejor introducción posible a la avifauna del país. También hay un orfanato de fauna con hienas. Perro prohibido: hay cocodrilos, monos y serpientes venenosas.",
         credit="Wikimedia Commons", source=IMG_COSTA),
    dict(n=4, name="Makasutu · bosque sagrado y el bolong de Mandina", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1 día",
         lat=13.2800, lon=-16.5800,
         desc="«Makasutu» significa bosque sagrado en mandinga, y es el ejemplo mejor montado de ecoturismo privado del país: unas 400 hectáreas junto a Brikama que reúnen de golpe los cuatro paisajes de Gambia — manglar de mareas, palmeral, sabana y bosque de galería — recorridas en piragua por el bolong de Mandina al amanecer, a pie con guía mandinga, y con babuinos, monos y un catálogo largo de aves. Dentro está el Mandina Lodge, con cabañas flotantes sobre el manglar. Es caro para el estándar del país, pero la salida en piragua por el bolong con la marea subiendo es de las cosas que mejor explican qué es Gambia. Confirmar la política de mascotas al reservar: es propiedad privada, no parque nacional, así que hay margen. Coordenada aproximada — confirmar sobre el terreno. Imagen de referencia del río Gambia, no del propio Makasutu.",
         credit="Wikimedia Commons", source=IMG_RIO),
    dict(n=5, name="Bijilo Forest Park (Monkey Park) y la franja de Kololi", cat="Naturaleza", prio="Media", dog="prohibido en el parque", time="½ día",
         lat=13.4328, lon=-16.7264,
         desc="51 hectáreas de bosque costero vallado justo detrás de los hoteles de Kololi, con 4,5 km de sendero entre dunas, matorral litoral y palmeras. Lo llaman Monkey Park porque los monos verdes, los colobos rojos de Temminck, las monas de Campbell y los patas bajan al camino sin miedo, y hay además gálagos de Senegal, genetas y más de 133 especies de aves — cálaos de pico rojo, buitres palmeros, charranes caspios en el tramo de playa. El «sendero ornitológico», paralelo a la costa, es una de las caminatas de aves más fáciles del país y se hace en dos horas al amanecer. Perdió parte de su estatus de reserva en 2018 por la construcción de un centro de congresos. Enfrente arranca LA FRANJA DE SENEGAMBIA (Kololi), la milla turística del país: hoteles, restaurantes, cambio de moneda, policía turística y también la mayor concentración de «bumsters» — ver la sección de seguridad.",
         credit="Wikimedia Commons", source=IMG_COSTA),
    dict(n=6, name="Kotu y Bakau · playas, Kotu Bridge y observación de aves", cat="Costa", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=13.4526, lon=-16.7069,
         desc="La franja hotelera clásica y la base más cómoda del país para parar varios días: playa de arena con rompiente, alojamientos con aparcamiento, supermercados, cajeros y agencias. Lo que la hace singular no es la playa sino EL PUENTE DE KOTU (Kotu Bridge) y el arroyo de Kotu Creek: un simple puentecito de carretera sobre un cauce de marea donde, sin moverse veinte metros, se ven martines pescadores, garzas, alcaravanes, abejarucos y los famosos picozapatos de la zona de arrozales; es, literalmente, el punto de observación de aves más famoso de Gambia y donde cualquier guía local empieza sus rutas. Al lado, los campos de golf y los arrozales de Kotu Ponds completan el circuito. Bakau añade el pequeño jardín botánico, Cape Point y el mercado de pescado. Perro: playas abiertas sin problema fuera de la zona hotelera concurrida; confirmar en recepción, casi ningún hotel publica su política.",
         credit="Mark Hodson Photos · CC BY 2.0", source=IMG_COSTA),
    dict(n=7, name="Cocodrilario sagrado de Katchikally (Bakau)", cat="Cultura", prio="Alta", dog="prohibido en la poza", time="½ día",
         lat=13.4806, lon=-16.6697,
         desc="En pleno Bakau, una poza de agua dulce rodeada de bosquecillo donde viven alrededor de ochenta cocodrilos del Nilo considerados sagrados desde hace siglos por la familia Bojang, que sigue custodiando el lugar. Es un santuario de FERTILIDAD: las mujeres gambianas acuden a lavarse con el agua de la poza y el rito sigue absolutamente vivo, lo que convierte la visita en algo bastante más serio que una atracción — conviene comportarse en consecuencia. Los cocodrilos, alimentados y habituados, se dejan tocar (el patriarca, «Charlie», es el veterano de la casa) y no hay registro de ataques, pero son animales salvajes. Hay un pequeño museo etnográfico con instrumentos, aperos y fotografía histórica. Perro: NO acercarlo a la poza bajo ningún concepto; dejarlo en el vehículo aparcado a la sombra, lejos del agua. Coordenada del centro de Bakau, aproximada. Imagen de referencia de Gambia, no del propio Katchikally.",
         credit="Wikimedia Commons", source=IMG_RIO),
    dict(n=8, name="Serrekunda · el mayor mercado del país", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=13.4383, lon=-16.6781,
         desc="Banjul es la capital, pero SERREKUNDA es la ciudad de verdad: el área metropolitana mayor del país, corazón del conurbano de los Kombos, donde vive casi la mitad de la población de Gambia y se concentra el 40 % de los negocios del país. Su mercado es el mayor del territorio, un laberinto de callejones de tela, batik, especias, herramientas y electrónica que se desborda sobre la carretera, con el barrio de los tintoreros y los talleres de carpintería alrededor. Es también la base logística real del viaje: talleres mecánicos, neumáticos, recambios, bancos, supermercados y las mejores clínicas veterinarias del país. Inviable con el perro dentro del mercado por pura densidad de gente. Imagen de referencia de la zona de los Kombos, no del propio mercado.",
         credit="Wikimedia Commons", source=IMG_COSTA),
    dict(n=9, name="Banjul · Arco 22, Albert Market y la isla de Santa María", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="½–1 día",
         lat=13.4542, lon=-16.5753,
         desc="Una capital rarísima: apenas 30.000 habitantes en una isla plana (Santa María) rodeada de manglar, a la que se entra bajo el ARCO 22, un arco triunfal de 35 m —de las estructuras más altas del país— levantado por Yahya Jammeh para conmemorar su propio golpe de Estado del 22 de julio de 1994, con la estatua del soldado desconocido en la base y un pequeño museo textil y un mirador panorámico arriba; que el monumento a un golpe siga en pie en una Gambia ya democrática dice mucho del país. Abajo, el Albert Market, la vieja plaza McCarthy, la catedral anglicana, el National Museum y el embarcadero del ferry. También aquí está la Six-Gun Battery, una de las piezas del conjunto UNESCO de Kunta Kinteh. Es donde están la embajada, el hospital de referencia y el puerto. Imagen de referencia del estuario del río Gambia, no del propio Banjul.",
         credit="Wikimedia Commons", source=IMG_RIO),
    dict(n=10, name="Travesía del río Gambia · ferry Banjul–Barra", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2–5 h",
         lat=13.4667, lon=-16.5667,
         desc="El gran rito overlander del país: unos 4 km de estuario entre el embarcadero de Banjul y el de Barra, en la orilla norte, en un transbordador de vehículos que es a la vez mercado flotante, autobús y espectáculo. La travesía en sí son 30-45 minutos; lo que se lleva el tiempo es la COLA, que puede ser de dos a cinco horas en día malo y que funciona más por presencia y paciencia que por horario. La flota ha sufrido averías y suspensiones repetidas, así que hay que confirmarlo el día antes y tener asumido el plan B (rodear por el puente de Senegambia, en Farafenni, a unos 110 km río arriba). Consejos recogidos de otros viajeros: llegar al alba, no dejar el vehículo sin vigilancia, cerrar todo, y contar con vendedores subiéndose al ferry. Con el perro: dentro del vehículo, con sombra y agua — la espera al sol es dura. Imagen de referencia del río Gambia, no del propio ferry.",
         credit="Wikimedia Commons", source=IMG_RIO),
    dict(n=11, name="Fuerte Bullen y Barra · la boca del río", cat="Patrimonio UNESCO", prio="Media", dog="permitido con condiciones", time="1–2 h",
         lat=13.4833, lon=-16.5500,
         desc="Nada más desembarcar del ferry, en la punta misma de la orilla norte, está el FUERTE BULLEN, construido por los británicos en 1826 —tras la abolición— no para comerciar con esclavos sino para IMPEDIRLO: sus cañones cruzaban fuego con los de la Six-Gun Battery de Banjul para cerrar la boca del río a los barcos negreros que seguían operando. Forma parte del conjunto Patrimonio Mundial «Isla de Kunta Kinteh y sitios relacionados», que reúne siete puntos repartidos por el estuario y narra la trata atlántica desde su inicio hasta su abolición. Volvió a usarse como posición defensiva en la Segunda Guerra Mundial. Barra, alrededor, es un pueblo-embarcadero caótico y el arranque de la carretera del norte hacia Amdalai y Senegal.",
         credit="Wikimedia Commons", source=IMG_RIO),
    dict(n=12, name="Juffureh y Albreda · el museo de la esclavitud", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=13.3386, lon=-16.3825,
         desc="A 30 km río arriba por la orilla norte, dos pueblos pegados que son el punto de partida de la visita a Kunta Kinteh. ALBREDA fue factoría francesa y JUFFUREH pueblo mandinga; en el edificio colonial de los Maurel Frères está el NATIONAL MUSEUM OF THE NORTH BANK, el museo de la esclavitud del país, y en la orilla la «puerta sin retorno» simbólica y el monumento de la Libertad. Juffureh es, según «Raíces» de Alex Haley (1976), el pueblo de donde fue arrancado su antepasado Kunta Kinte, y la familia Kinte sigue recibiendo visitantes — el impacto del libro transformó la aldea y trajo escuelas, mercado e infraestructura, y en 1999 se abrió aquí el complejo Alex Haley. Los historiadores llevan décadas discutiendo la exactitud genealógica del relato; lo que no se discute es que este tramo de río fue durante siglos un centro real de la trata. Visita guiada por la comunidad, tasa conjunta con la isla.",
         credit="Wikimedia Commons", source=IMG_RIO),
    dict(n=13, name="Isla de Kunta Kinteh (antigua James Island) · UNESCO", cat="Patrimonio UNESCO", prio="Alta", dog="no aplicable (isla, acceso en barco)", time="½ día",
         lat=13.3175, lon=-16.3614,
         desc="Un islote que se está comiendo el río —hoy es una sexta parte de lo que era— con las ruinas del fuerte y unos baobabs aferrados a la orilla, a menos de 3 km de Albreda. Los portugueses la avistaron en 1456 y la llamaron San Andrés; los curlandeses (sí, letones) levantaron aquí el fuerte Jacob en 1651; ingleses, holandeses y franceses se la quitaron unos a otros durante dos siglos, y los británicos la rebautizaron James Island en 1664 y la usaron para oro, marfil y esclavos hasta su abandono en 1870. En 2011 se renombró Isla de Kunta Kinteh. Patrimonio Mundial desde 2003 (ref. 761rev-001, criterios iii y vi) como pieza central del conjunto «Isla de Kunta Kinteh y sitios relacionados». Se llega en piragua desde Albreda, 15 minutos, y es una visita corta y muy seca: quedan los muros de la celda, el aljibe y poco más — la carga está en el sitio, no en las piedras. El perro se queda en tierra con un miembro del grupo.",
         credit="Leonora (Ellie) Enking · CC BY-SA 2.0", source=IMG_RIO),
    dict(n=14, name="Parque Nacional de Niumi y la isla de Jinack", cat="Naturaleza", prio="Media", dog="prohibido en el parque", time="1 día–1 noche",
         lat=13.5417, lon=-16.5236,
         desc="49 km² de franja litoral en el extremo noroeste, declarados en 1987 y Ramsar desde 2008: es la parte gambiana del DELTA DEL SALOUM, que continúa sin costura en Senegal, y combina marisma dulce, lagunas salobres, manglar y flechas de arena. Más de 200 especies de aves en las llanuras de marea, con colonias importantes de charranes y gaviotas, además de tortuga verde, delfín jorobado del Atlántico y manatí africano —los tres vulnerables—, patas, cercopitecos verdes, hienas manchadas y facóqueros. Dentro está JINACK ISLAND, una isla-barrera larga y estrecha con una de las playas más vacías de África occidental y un par de campamentos muy básicos; se llega en piragua desde Barra o Bakau y la frontera con Senegal cruza la propia isla — hay que aclararlo con el puesto antes de pasear hacia el norte. Perro prohibido en el parque; en la playa de Jinack fuera del área gestionada, confirmar con el campamento.",
         credit="Wikimedia Commons", source=IMG_COSTA),
    # ===== VARIANTE DEL RÍO ARRIBA: orilla sur -> Kiang West -> Soma/puente -> Janjanbureh -> Wassu -> Farafenni =====
    dict(n=15, name="Parque Nacional de Kiang West y Tendaba", cat="Naturaleza", prio="Alta", dog="prohibido en el parque", time="1–2 noches",
         lat=13.3833, lon=-15.9167,
         desc="115 km² en la orilla sur, a unos 145 km de Banjul, y el gran espacio natural continental del país: sabana de Guinea, bosque seco caducifolio de baobabs y acacias rojas, llanuras de marea y una red de bolongs de manglar. Conserva casi toda la fauna que le queda a Gambia —leopardo, hiena manchada, facóquero, sitatunga, manatí africano y delfín jorobado en el bolong de Jarin— y más de 300 ESPECIES DE AVES, más de la mitad de todas las registradas en el país, lo que le vale la categoría de Área Importante para las Aves; su emblema es el águila volatinera. El mirador de TUBABKOLLON POINT, sobre una playa de arena en el noreste, es el mejor puesto de observación. La base es el veterano TENDABA CAMP, funcionando desde los años setenta, desde donde salen las piraguas al manglar del Bao Bolong, enfrente, y los recorridos en vehículo por el parque. Mejor de noviembre a enero. Recibe muy pocos visitantes. Perro prohibido dentro; el campamento es la pieza del plan B.",
         credit="Wikimedia Commons", source=IMG_RIO),
    dict(n=16, name="Reserva de humedales de Bao Bolong · el manglar grande", cat="Naturaleza", prio="Media", dog="prohibido en la reserva", time="½–1 día",
         lat=13.5667, lon=-15.8167,
         desc="Justo enfrente de Kiang West, en la orilla norte y a unos 18 km de Farafenni, 220 km² declarados en 1996 y PRIMER HUMEDAL RAMSAR DE GAMBIA. Lo que lo hace excepcional es una franja de manglar denso de dos kilómetros y medio de ancho con ejemplares de hasta 20 metros de altura — algo prácticamente único en toda Senegambia. Alrededor, marisma salina, sabana inundable y pastizal alto. 268 especies de aves de 62 familias (garzas, garcetas, águilas pescadoras, martines pescadores), 32 de mamíferos incluidos sitatunga y antílope jeroglífico, y manatí africano. La visita natural es en piragua desde Tendaba, cruzando el río: es la excursión estrella de esa base y una de las mejores mañanas de aves de todo el viaje. Perro prohibido; se queda en el campamento con un miembro del grupo. Imagen de referencia del río Gambia, no de la propia reserva.",
         credit="Wikimedia Commons", source=IMG_RIO),
    dict(n=17, name="Janjanbureh (Georgetown) y la isla de MacCarthy", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="1 noche",
         lat=13.5333, lon=-14.7667,
         desc="A 300 km de la costa, la vieja GEORGETOWN colonial sobre una isla fluvial: el capitán británico Alexander Grant compró la isla de Lemain al rey de Niani en 1823 y fundó aquí un ASENTAMIENTO PARA ESCLAVOS LIBERADOS, que llegó a ser el segundo núcleo del país y decayó cuando el comercio fluvial se apagó. Hoy es un pueblo somnoliento de calles de arena con casas coloniales en ruina, la vieja casa de la CFAO, el edificio conocido como «la casa de los esclavos» (su papel real está discutido: no hay consenso documental sobre si fue depósito de esclavos o almacén comercial — tratarlo con cautela), la cárcel principal del país, y el mejor ambiente de río de Gambia. Se entra por puente desde la orilla sur y se sale en ferry de plataforma hacia la orilla norte (Lamin Koto), que es el enganche natural con Wassu. Base para los paseos en barca del río alto, con hipopótamos y cocodrilos. Imagen de referencia del río Gambia, no de la propia Janjanbureh.",
         credit="Wikimedia Commons", source=IMG_RIO),
    dict(n=18, name="Círculos de piedra de Wassu · megalitos senegambianos (UNESCO)", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con correa", time="½ día",
         lat=13.6914, lon=-14.8731,
         desc="A 22 km de Lamin Koto, en la orilla norte, ONCE CÍRCULOS de columnas de laterita labradas a mano y clavadas de pie, con sus piedras frontales delante, sobre un campo de túmulos funerarios; aquí está la columna más alta de todo el conjunto, de 2,59 m. Forman parte del Patrimonio Mundial «Círculos de piedra de Senegambia» (2006), cuatro sitios —Wassu y Kerr Batch en Gambia, Sine Ngayène y Wanar en Senegal— escogidos entre MÁS DE MIL círculos repartidos por una banda de 350 por 100 km a ambos lados del río. Los de Wassu están datados entre el 927 y el 1305 d. C. Se desconoce casi todo de quién los levantó: es el mayor complejo megalítico de África y uno de los más densos del mundo. Hay un pequeño museo interpretativo y la costumbre local de dejar piedrecitas sobre las columnas. Complementario: KERR BATCH, 40 km al oeste, con la única piedra bífida en V de toda la región. Sitio abierto y llano, cómodo con el perro atado.",
         credit="Wikimedia Commons", source=IMG_RIO),
    dict(n=19, name="Parque Nacional del río Gambia · las islas de los chimpancés", cat="Naturaleza", prio="Media", dog="no aplicable (acceso prohibido a las islas)", time="½ día",
         lat=13.6417, lon=-14.9639,
         desc="585 hectáreas de archipiélago —las BABOON ISLANDS, una isla grande y cuatro pequeñas— en el río, aguas abajo de Janjanbureh. Desde 1979 albergan el CHIMPANCEE REHABILITATION PROJECT, iniciado por Stella Marsden: chimpancés confiscados del tráfico ilegal, reintroducidos y mantenidos en semilibertad en las tres islas mayores; hacia 2006 eran unos 77 y siguen siendo una de las poblaciones reintroducidas más exitosas de África. ATENCIÓN, dato que hay que tener claro antes de planificar: EL PARQUE NO ESTÁ ABIERTO AL PÚBLICO, desembarcar en las islas está prohibido por la agresividad de los chimpancés, y desde 1998 se restringió drásticamente incluso la navegación alrededor. La única forma legal de verlo es el crucero fluvial del propio proyecto (Chimp Rehab / campamento de Badi Mayo) o desde el cauce a distancia con operador autorizado. Hay además hipopótamo, cocodrilo del Nilo, babuino de Guinea, colobo rojo occidental y manatí. CONFIRMAR con el proyecto antes de contar con ello. Imagen de referencia del río Gambia, no del propio parque.",
         credit="Wikimedia Commons", source=IMG_RIO),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "naturaleza": "verde", "cultura": "morado",
              "costa": "turquesa", "patrimonio unesco": "marron"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Séléti (desde la Casamance, eje Ziguinchor-Brikama)", "Frontera", 13.1000, -16.5200,
     "Paso principal desde la Casamance senegalesa por la carretera de Ziguinchor a Brikama y los Kombos. Es la entrada natural del corredor de subida. COORDENADA APROXIMADA y horario POR CONFIRMAR 72 h antes. Al entrar se sale de la zona del franco CFA y se pasa al dalasi: cambiar solo lo justo."),
    ("Frontera · Entrada alternativa — Darsilami / Kartong-Allahein (litoral)", "Frontera", 13.0833, -16.7583,
     "Alternativa litoral para entrar directamente a Kartong desde la Basse Casamance. El cruce del río Allahein es en piragua para peatones: POR CONFIRMAR si existe paso practicable con vehículo o si obliga a rodear por Darsilami/Séléti. No darlo por bueno sin verificación."),
    ("Frontera · Salida oeste — Amdalai / Karang (hacia la Petite Côte y Dakar)", "Frontera", 13.4917, -16.5333,
     "Salida del eje costero: carretera del norte desde Barra, ~30 km. Es el paso que enlaza con Toubacouta, el delta del Saloum, Kaolack y Dakar, y por tanto con el lago Retba. Muy transitado y bien rodado por overlanders; horario amplio pero cruzar por la mañana. Coordenada aproximada del lado gambiano."),
    ("Frontera · Salida este — Keur Ayib / Farafenni (Trans-Gambia)", "Frontera", 13.5933, -15.6058,
     "Salida de la variante del río arriba, al norte de Farafenni por la carretera Trans-Gambia. Enlaza con Kaolack por el interior. Coordenada tomada de la ficha de Senegal para mantener la coherencia entre las dos fichas."),
    ("Ferry de vehículos · Banjul – Barra", "Frontera", 13.4542, -16.5753,
     "Transbordador de vehículos de ~4 km sobre el estuario, gestionado por Gambia Ferries Services. Travesía 30-45 min, cola de 2-5 h en día malo. Historial de averías y suspensiones: CONFIRMAR que opera el día antes. Plan B: puente de Senegambia (Farafenni-Soma), ~110 km río arriba."),
    ("Puente de Senegambia (Farafenni – Soma)", "Frontera", 13.4900, -15.5500,
     "Puente de 1,9 km (942 m sobre el río) abierto a vehículos ligeros el 21 de enero de 2019; financiado por el Banco Africano de Desarrollo (65 M$ de 93 M$) y construido por Isolux Corsán (España) con el grupo senegalés Arezki. Redujo el trayecto Dakar-Ziguinchor de un día a unas cinco horas y sustituyó al viejo ferry de la Trans-Gambia, que llegaba a acumular esperas de 10-20 días para camiones. ES LA OPCIÓN FIABLE PARA CRUZAR EL RÍO CON VEHÍCULO. Peaje: POR CONFIRMAR (hay disputa documentada entre Gambia Ferries Services y la National Roads Authority sobre la recaudación). Coordenada aproximada."),
    ("Embajada de España en Banjul (referencia: Dakar)", "Consular", 13.4549, -16.5790,
     "España NO tiene embajada residente en Banjul: la competencia es de la Embajada de España en Dakar (Senegal), que es la referencia consular real de todo el tramo. Existe representación honoraria en Banjul — CONFIRMAR dirección, teléfono y vigencia 30-60 días antes; dato pendiente de verificación directa."),
    ("Edward Francis Small Teaching Hospital (ex Royal Victoria) — Banjul", "Hospital", 13.4540, -16.5776,
     "Principal hospital de referencia del país, en Banjul. Capacidad limitada para traumatismos graves: el seguro con evacuación médica (a Dakar, que está a 300 km y tiene el mejor nivel de la subregión) es imprescindible. Coordenada urbana aproximada."),
    ("Clínicas privadas y veterinarios · Kombos (Serrekunda, Kololi, Fajara)", "Hospital", 13.4383, -16.6781,
     "Las clínicas privadas de la zona de los Kombos cubren urgencias menores mejor que el hospital público. Es también donde están los veterinarios del país; para cualquier cosa seria, Dakar. Coordenada urbana aproximada."),
    ("Combustible · Kombos (Serrekunda, Kololi, Bakau, Brikama)", "Combustible", 13.4383, -16.6781,
     "Mejor oferta y calidad del país (GACH, Jah Oil, Total). Repostar a fondo aquí antes de subir el río: al este de Soma la red se vuelve escasa."),
    ("Combustible · Soma / Farafenni (nudo de la Trans-Gambia)", "Combustible", 13.4300, -15.5300,
     "Nudo de las dos orillas junto al puente de Senegambia y última oferta razonable antes del tramo largo hacia Janjanbureh. Llegar lleno y salir lleno."),
    ("Combustible · Janjanbureh / Bansang", "Combustible", 13.5333, -14.7667,
     "Oferta limitada e irregular del río arriba. POR CONFIRMAR sobre el terreno; llevar garrafa de reserva desde Soma. Coordenada aproximada."),
    ("Agua potable y de uso general · Kombos y Tendaba", "Agua potable", 13.4526, -16.7069,
     "Agua embotellada sin problema en toda la franja costera y en Serrekunda. Los hoteles de Kotu/Kololi y el Tendaba Camp permiten llenar el depósito de uso general con manguera; confirmar en recepción. Del río arriba, garantizar la reserva completa antes de salir de Soma."),
]

DRONE_CALLOUT = ("warn", "Normativa poco desarrollada y, por eso mismo, imprevisible",
                  "Gambia no tiene un régimen de drones tan articulado como Ghana o Marruecos, y esa falta de norma clara es precisamente el riesgo: sin un procedimiento público al que acogerse, la decisión queda en manos del funcionario de aduana o del policía de turno. La autoridad competente es la GAMBIA CIVIL AVIATION AUTHORITY (GCAA). Norma prudente del proyecto: solicitar información y autorización por escrito a la GCAA con antelación y, si no llega respuesta, NO introducir el dron — sobre todo porque se entra desde Senegal y se sale hacia Senegal, y el equipo viene ya de atravesar Marruecos, donde la confiscación en aduana es práctica habitual. Nunca volar sobre el aeropuerto de Banjul, el puerto, la State House, el Arco 22, cuarteles, la cárcel de Janjanbureh ni el entorno de los pasos fronterizos.")

STARLINK_CALLOUT = ("warn", "Sin confirmación de servicio activo a la fecha de esta revisión",
                     "No se ha localizado confirmación de que Starlink esté licenciado y activo en Gambia a mediados de 2026 — no aparece entre los mercados africanos documentados. Tratarlo como NO GARANTIZADO y no planificar ninguna dependencia de él en este tramo. La buena noticia es que Gambia es diminuta y está densamente poblada en la franja costera: la cobertura móvil es razonable en todos los Kombos y a lo largo del río, y solo se degrada en el interior norte. SIM local: Africell (la de mejor cobertura), Qcell y Gamcel. Como el país se atraviesa en pocos días y se entra y se sale de Senegal, una alternativa práctica es mantener activa la SIM senegalesa en roaming y comprar una gambiana solo si se va a subir el río.")

DOG_MATRIX = [
    ("Playas y costa: Kartong, Tanji, Kotu, Bakau, Jinack", "permitido",
     "El mejor tramo del país para el perro: arena abierta, sin gestión de parque y alojamientos pequeños que suelen aceptarlo aunque casi ninguno lo publique — confirmar SIEMPRE en recepción al reservar. En la playa de pesca de Tanji, correa corta: hay mucho pescado, mucha actividad y bastantes perros locales sueltos."),
    ("Kombos urbanos (Serrekunda, Kololi, Banjul, Brikama)", "permitido con condiciones",
     "Sin restricción específica publicada, pero calor húmedo y tráfico denso: correa corta y paseos a primera y última hora. El mercado de Serrekunda es inviable con perro por densidad de gente. Aparcamiento vigilado siempre. Los veterinarios del país están aquí; para cualquier cosa seria, Dakar (300 km)."),
    ("Reserva Natural de Abuko", "prohibido",
     "Prohibido, y con razón de seguridad: cocodrilos del Nilo y enanos en la poza, tres especies de mono y serpientes venenosas (cobra escupidora, mamba verde, bitis). Plan B fácil: la visita son 2-3 horas y está a 20 minutos de Serrekunda, así que se resuelve en una mañana con turnos desde el alojamiento de Kotu."),
    ("Bijilo Forest Park (Monkey Park)", "prohibido en el parque",
     "Parque vallado con tropas de monos habituadas a la gente: el perro no entra. Plan B inmejorable: está pegado a la playa de Kololi, así que quien se queda con el perro tiene paseo de arena a cincuenta metros mientras los otros hacen el sendero (2 h)."),
    ("Cocodrilario de Katchikally", "prohibido en la poza",
     "No acercar al perro al agua bajo ningún concepto: son cocodrilos del Nilo salvajes aunque estén habituados y alimentados. Es además un santuario religioso vivo. Dejarlo en el vehículo aparcado a la sombra, lejos de la poza."),
    ("Parque Nacional de Kiang West y Parque Nacional de Niumi", "prohibido en el parque",
     "Prohibido dentro de los parques gestionados por el Department of Parks and Wildlife Management. Plan B concreto en Kiang West: el TENDABA CAMP está FUERA del parque, tiene aparcamiento y sombra, y desde su embarcadero salen las piraguas al manglar del Bao Bolong — quien se queda con el perro puede hacer perfectamente el paseo por el poblado y la orilla. Turnarse al día siguiente. CONFIRMAR por escrito con el campamento que admiten perro en el recinto."),
    ("Reserva de humedales de Bao Bolong", "prohibido en la reserva",
     "Reserva Ramsar: perro fuera. La excursión es en piragua desde Tendaba y dura media mañana, así que se cubre con turnos desde el campamento."),
    ("Isla de Kunta Kinteh y travesías en piragua", "no aplicable",
     "La piragua a la isla es corta (15 min) pero estrecha y con poca sombra, y la isla no tiene dónde dejarlo. El perro se queda en Albreda/Juffureh con un miembro del grupo; hay sombra y el museo se visita por turnos."),
    ("Parque Nacional del río Gambia (islas de los chimpancés)", "no aplicable",
     "El parque está cerrado al público y desembarcar está prohibido para todo el mundo, así que la cuestión canina no llega a plantearse. Si finalmente se hace el crucero del proyecto, confirmar con ellos: un perro a bordo cerca de chimpancés semisalvajes es mala idea de todas formas."),
    ("Ferry de Banjul–Barra", "permitido con condiciones",
     "El perro viaja dentro del vehículo. Lo duro no es la travesía sino la COLA, que puede ser de horas al sol: llegar al amanecer, aparcar buscando sombra, ventilación y agua abundante. Si la espera se descontrola, el puente de Senegambia (110 km río arriba) es una alternativa mucho más humana para el animal."),
    ("Círculos de piedra de Wassu y Janjanbureh", "permitido con correa",
     "Sitios abiertos, llanos y sin gestión de parque: el perro atado no es problema. En Wassu, respeto elemental — es un cementerio. Sombra escasa en el campo de megalitos: visitar a primera o última hora."),
    ("Entrada y salida del país", "por confirmar",
     "No se ha localizado fuente oficial gambiana sobre importación de animales de compañía (Department of Livestock Services / Ministry of Agriculture). Llevar certificado veterinario internacional en INGLÉS (Gambia es anglófona, a diferencia de todos sus vecinos) con rabia en vigor, pasaporte UE y microchip, y tener presente que se entra y se sale por fronteras distintas en el mismo viaje. Ver decisiones pendientes."),
]

SOURCES = [
    ("UNESCO · Isla de Kunta Kinteh y sitios relacionados, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/761/"),
    ("UNESCO · Círculos de piedra de Senegambia, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/1226/"),
    ("Wikipedia · Kunta Kinteh Island (coordenadas, historia, estatus UNESCO)", "https://en.wikipedia.org/wiki/Kunta_Kinteh_Island"),
    ("Wikipedia · Senegambian stone circles (Wassu, Kerr Batch, dataciones y coordenadas)", "https://en.wikipedia.org/wiki/Wassu_stone_circles"),
    ("Wikipedia · Abuko Nature Reserve", "https://en.wikipedia.org/wiki/Abuko_Nature_Reserve"),
    ("Wikipedia · River Gambia National Park (proyecto de rehabilitación de chimpancés)", "https://en.wikipedia.org/wiki/River_Gambia_National_Park"),
    ("Wikipedia · Kiang West National Park", "https://en.wikipedia.org/wiki/Kiang_West_National_Park"),
    ("Wikipedia · Niumi National Park", "https://en.wikipedia.org/wiki/Niumi_National_Park"),
    ("Wikipedia · Bao Bolong Wetland Reserve", "https://en.wikipedia.org/wiki/Bao_Bolong_Wetland_Reserve"),
    ("Wikipedia · Bijilo Forest Park", "https://en.wikipedia.org/wiki/Bijilo_Forest_Park"),
    ("Wikipedia · Senegambia Bridge (Farafenni-Soma)", "https://en.wikipedia.org/wiki/Senegambia_Bridge"),
    ("Wikipedia · Trans-Gambia Highway", "https://en.wikipedia.org/wiki/Trans-Gambia_Highway"),
    ("Wikipedia · Janjanbureh (Georgetown, isla de MacCarthy)", "https://en.wikipedia.org/wiki/Janjanbureh,_Gambia"),
    ("Wikipedia · Juffureh y Albreda", "https://en.wikipedia.org/wiki/Juffureh"),
    ("Wikipedia · Barra (ferry y Fuerte Bullen)", "https://en.wikipedia.org/wiki/Barra,_Gambia"),
    ("Wikipedia · Banjul", "https://en.wikipedia.org/wiki/Banjul"),
    ("Wikipedia · Arch 22", "https://en.wikipedia.org/wiki/Arch_22"),
    ("Wikipedia · Bakau (Katchikally)", "https://en.wikipedia.org/wiki/Bakau"),
    ("Wikipedia · Serrekunda", "https://en.wikipedia.org/wiki/Serrekunda"),
    ("Wikipedia · Brikama", "https://en.wikipedia.org/wiki/Brikama"),
    ("Wikipedia · Kololi", "https://en.wikipedia.org/wiki/Kololi"),
    ("Wikipedia · Tanji", "https://en.wikipedia.org/wiki/Tanji"),
    ("Wikipedia · Kartong", "https://en.wikipedia.org/wiki/Kartong"),
    ("Wikipedia · The Gambia (país, clima, lengua, economía)", "https://en.wikipedia.org/wiki/Gambia"),
    ("Wikipedia · Visa policy of the Gambia", "https://en.wikipedia.org/wiki/Visa_policy_of_the_Gambia"),
    ("Wikipedia · Gambian dalasi", "https://en.wikipedia.org/wiki/Gambian_dalasi"),
    ("Wikipedia · List of birds of the Gambia (621 especies registradas)", "https://en.wikipedia.org/wiki/List_of_birds_of_the_Gambia"),
    ("thingstodoingambia.com · requisitos de entrada", "https://thingstodoingambia.com/entry-requirements/"),
    ("Lost In A 4x4 · guía del cruce Senegal-Gambia paso a paso con vehículo propio", "https://lostina4x4.com/senegal-to-the-gambia-border-crossing-guide-overland-step-by-step/"),
    ("Feathery Travels · cruce fronterizo Gambia/Senegal (Amdallai-Karang)", "https://www.featherytravels.com/gambiasenegalborderkarang/"),
    ("ECOWAS Brown Card · esquema regional de seguro de vehículos", "https://www.browncard.org/"),
    ("iOverlander · puntos de combustible, agua, acampada y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía, puntos overland y blog de viajeros por África", "https://tracks4africa.co.za/"),
]

# EJE COSTERO: Séléti -> Brikama -> Abuko -> Kombos -> Banjul -> ferry -> Barra -> Juffureh/Kunta Kinteh -> Amdalai
CORRIDOR = [(13.1000, -16.5200), (13.2667, -16.6500), (13.0833, -16.7583), (13.3500, -16.7900),
            (13.3958, -16.6456), (13.4328, -16.7264), (13.4526, -16.7069), (13.4806, -16.6697),
            (13.4383, -16.6781), (13.4542, -16.5753), (13.4833, -16.5500), (13.3386, -16.3825),
            (13.3175, -16.3614), (13.5417, -16.5236), (13.4917, -16.5333)]

# VARIANTE DEL RÍO ARRIBA: Kombos -> orilla sur -> Kiang West/Tendaba -> Soma/puente -> Janjanbureh -> Wassu -> Farafenni -> Keur Ayib
CORRIDOR_ALT = [(13.4383, -16.6781), (13.2800, -16.5800), (13.2667, -16.6500), (13.3833, -15.9167),
                (13.4300, -15.5300), (13.4900, -15.5500), (13.5333, -14.7667), (13.6417, -14.9639),
                (13.6914, -14.8731), (13.5667, -15.8167), (13.5667, -15.6000), (13.5933, -15.6058)]

CORRIDOR_LABEL = "Eje corto costero (Banjul y el ferry)"
CORRIDOR_ALT_LABEL = "Variante del río arriba (Tendaba, Janjanbureh y Wassu)"

EXPERIENCIAS = [
    "El ferry de Banjul–Barra es EL tema recurrente de los overlanders en Gambia. La travesía son 30-45 minutos, pero la cola de vehículos puede comerse media jornada, no funciona por horario publicado sino por presencia, y la flota ha tenido averías y suspensiones repetidas a lo largo de los años. La recomendación unánime de quienes lo han hecho: llegar al amanecer, no separarse del vehículo, cerrarlo todo, y tener decidido de antemano el plan B. Desde que existe el puente de Senegambia, muchos viajeros con vehículo simplemente NO usan el ferry y rodean por Farafenni: son ~110 km más pero con hora de llegada previsible. Decidir sobre el terreno, según cómo esté el día.",
    "El puente de Senegambia (2019) cambió la logística del país entero: el trayecto Dakar–Ziguinchor pasó de un día a unas cinco horas, y el viejo ferry de la Trans-Gambia, donde los camiones llegaban a esperar de diez a veinte días, dejó de ser el cuello de botella del África occidental atlántica. Para nosotros significa que cruzar el río con dos vehículos de expedición es hoy un trámite trivial si se acepta rodear por Farafenni. El peaje y su gestión están POR CONFIRMAR: hay una disputa documentada entre Gambia Ferries Services y la National Roads Authority sobre quién cobra.",
    "«Bumsters» — hay que entenderlo bien y sin caricatura. Son jóvenes gambianos que se ganan la vida abordando turistas en las playas y en la franja de Senegambia, ofreciéndose como guía, amigo o acompañante, a veces con expectativa de relación sentimental o de patrocinio a largo plazo. NO es delincuencia violenta: es presión social insistente, y responde a un desempleo juvenil altísimo en un país que vive del turismo. El gobierno creó una policía turística precisamente por esto. Lo que funciona, según los viajeros: ser educado pero claro desde el primer segundo, no aceptar «te acompaño un momento», no dar el número de teléfono, y no entrar en la dinámica de la culpa. Lo que no funciona: la evasiva. Fuera de la franja hotelera (Kartong, Tanji, el río arriba) el fenómeno prácticamente desaparece.",
    "Gambia es una isla anglófona rodeada de un océano francófono, y eso se nota en todo: los trámites se hacen en inglés, los papeles del perro y del vehículo conviene llevarlos en inglés AQUÍ y en francés en Senegal, y los precios se negocian en dalasis, no en francos CFA. Como el país se entra y se sale en pocos días, el consejo repetido es cambiar poco: lo justo para combustible, tasas y comida, porque el dalasi no se recoloca fácilmente fuera del país.",
    "Observación de aves: es el motivo por el que la mayoría de los viajeros especializados van a Gambia, y no es publicidad. En un país del tamaño de Asturias hay 621 especies registradas, sin ningún endemismo pero con una densidad y una facilidad de observación excepcionales, porque los hábitats (manglar, sabana, bosque de galería, marisma, costa atlántica) están todos a menos de una hora unos de otros y la red de guías locales formados es la mejor de África occidental. El punto icónico es el puente de Kotu, donde se ven decenas de especies desde el propio asfalto; Abuko concentra 270 especies en 107 hectáreas, Kiang West más de 300, Bao Bolong 268. Noviembre a febrero es la ventana buena, con los migrantes paleárticos ya instalados y sin calor extremo.",
    "El río arriba (Soma → Janjanbureh → Basse) es otro país: se acaban los turistas, el asfalto empeora, el combustible escasea y aparece la Gambia rural de verdad. Los viajeros que lo hacen coinciden en que compensa si se tienen dos o tres días, y en que no compensa si se va con prisa — y en que hay que llevar garrafa de reserva. La carretera de la orilla sur (South Bank Road) es la vía principal y está en mejor estado que la del norte.",
    "El Parque Nacional del río Gambia (islas de los chimpancés) es la decepción recurrente de los viajeros que llegan sin informarse: NO está abierto al público, desembarcar está prohibido y desde 1998 se restringió incluso navegar alrededor. Quien quiera verlos tiene que ir a través del propio Chimpanzee Rehabilitation Project. Conviene resolverlo por correo antes de subir el río y no plantarse allí esperando comprar una entrada.",
    "Sobre la carga histórica de Juffureh y Kunta Kinteh: los viajeros que han hecho también Elmina y Cape Coast en Ghana suelen describir Gambia como una experiencia distinta y más íntima — aquí no hay mazmorras impresionantes, hay un islote erosionado, un museo pequeño y una comunidad que lleva cincuenta años contando la misma historia. La exactitud genealógica del relato de Alex Haley está discutida académicamente desde hace décadas; el papel del estuario del Gambia en la trata atlántica, no.",
]

HISTORIA_RESUMEN = ("Gambia es una franja de apenas unos kilómetros a cada lado de su río, enclavada dentro de Senegal, y debe su forma absurda a la rivalidad colonial anglo-francesa; su isla de Kunta Kinteh (la antigua James Island) "
                     "fue uno de los puntos de embarque de la trata atlántica de esclavos y hoy es Patrimonio de la Humanidad, mientras el país vive del turismo costero, de la pesca y del cacahuete, y consolida una recuperación democrática tras veintidós años de dictadura.")

HISTORIA_SECCIONES = [
    ("El río como vía comercial y como ruta de esclavos",
     "El río Gambia fue durante siglos la mejor vía navegable hacia el interior del África occidental, y por eso mismo el escenario de una competencia europea feroz. Los portugueses avistaron la isla de San Andrés en 1456; los curlandeses —del actual territorio letón— levantaron allí el fuerte Jacob en 1651; ingleses, holandeses y franceses se la arrebataron unos a otros durante dos siglos. Los británicos la rebautizaron James Island en 1664 y la usaron para el oro, el marfil y, sobre todo, para las personas esclavizadas que se embarcaban hacia América. La novela «Raíces» de Alex Haley (1976) situó en Juffureh el origen de su antepasado y convirtió este tramo de río en un lugar de peregrinación de la diáspora afroamericana. Mucho antes, entre los siglos X y XIV, alguien de quien casi no sabemos nada levantó a orillas del mismo río más de mil círculos de piedra: los megalitos senegambianos de Wassu y Kerr Batch, el mayor complejo megalítico de África."),
    ("Una colonia británica dentro del Senegal francés",
     "La forma alargada y estrechísima de Gambia —menos de 50 km de ancho en su punto máximo, 11.300 km² en total, el país más pequeño del África continental— es resultado directo de los acuerdos anglo-franceses de finales del siglo XIX, que fijaron la frontera a pocos kilómetros de cada orilla del río navegable, dejando un enclave británico completamente rodeado por el Senegal francés. Entre 1758 y 1779 el territorio formó parte de la Senegambia británica. Gambia se independizó del Reino Unido en 1965 y se convirtió en república en 1970; entre 1982 y 1989 ensayó con Senegal una confederación, la Senegambia, que acabó disolviéndose."),
    ("Los veintidós años de Yahya Jammeh",
     "Un golpe de Estado en 1994 llevó al poder al teniente Yahya Jammeh, que gobernó durante veintidós años con un régimen represivo, desapariciones forzadas y episodios delirantes —como su anuncio de haber encontrado una cura para el sida—, y que dejó su marca física en la capital: el Arco 22 de Banjul conmemora precisamente su golpe. Perdió las elecciones de diciembre de 2016 frente a Adama Barrow, se negó durante semanas a entregar el poder y finalmente se exilió en enero de 2017 ante la presión militar y diplomática de la CEDEAO."),
    ("Situación actual",
     "Gambia vive desde 2017 una transición democrática con una comisión de verdad, reparación y reconciliación que ha documentado los abusos de la era Jammeh. Es un país estable, pobre y muy joven, con la economía apoyada en el turismo costero, la pesca, el cacahuete y las remesas, y con un desempleo juvenil que explica buena parte de la presión sobre el visitante en la franja hotelera. La apertura del puente de Senegambia en 2019 lo ha convertido, por primera vez, en un país de paso cómodo entre el norte de Senegal y la Casamance en vez de en un tapón."),
]

HISTORIA_FUENTES = [
    ("BBC News · The Gambia country profile", "https://www.bbc.com/news/world-africa-13376517"),
    ("UNESCO · Isla de Kunta Kinteh y sitios relacionados", "https://whc.unesco.org/en/list/761/"),
    ("UNESCO · Círculos de piedra de Senegambia", "https://whc.unesco.org/en/list/1226/"),
    ("Encyclopaedia Britannica · The Gambia, History", "https://www.britannica.com/place/The-Gambia/History"),
]

SPEC = dict(
    slug="gambia", name="Gambia", revision="12 sep 2026",
    sub="Solo en la subida · dos corredores alternativos · el país de las aves",
    chips=[
        ("ROL EN LA RUTA", "ÚNICO PAÍS QUE SE VISITA SOLO A LA VUELTA · entre la Casamance y Dakar"),
        ("EJE CORTO", "Séléti → Kombos → Banjul → ferry → Kunta Kinteh → Amdalai/Karang · ~220 km"),
        ("VARIANTE DEL RÍO", "Kombos → Tendaba/Kiang West → puente de Senegambia → Janjanbureh → Wassu → Keur Ayib · ~700 km ida y vuelta"),
        ("PDIs", "19 puntos repartidos entre los dos corredores"),
        ("AVES", "621 especies registradas en 11.300 km²: LA especialidad del país"),
        ("UNESCO", "Kunta Kinteh y sitios relacionados · Círculos de piedra de Senegambia"),
        ("EL RÍO", "ferry Banjul–Barra (cola de horas) o puente de Senegambia (fiable)"),
        ("PERRO", "playas y pueblos sí, parques no · trámite de entrada POR CONFIRMAR"),
        ("VISADO", "POR CONFIRMAR para pasaporte español — punto crítico de esta ficha"),
        ("MONEDA", "dalasi (GMD): se sale de la zona CFA y se vuelve a entrar a los pocos días"),
        ("IDIOMA", "anglófono, rodeado de francófonos"),
        ("SEGURIDAD", "estable · el único tema real son los «bumsters» de la franja turística"),
    ],
    center=[13.47, -15.6], zoom=8,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    hero_img=IMG_RIO,
    hero_credit="Isla de Kunta Kinteh, cerca de Juffureh · Leonora (Ellie) Enking · CC BY-SA 2.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Gambia es el <strong>único país de todo el viaje que se visita exclusivamente en el corredor de subida</strong>. En la bajada se pasa de largo por el Ferlo senegalés; a la vuelta, en cambio, la ruta entra por la "
                   "<strong>Casamance</strong>, atraviesa el país de sur a norte cruzando el río Gambia, y sale otra vez a Senegal camino de Dakar y el lago Retba. Como solo hay una pasada, esta ficha no propone bajada y subida sino "
                   "<strong>dos variantes reales del mismo recorrido</strong>: un <strong>eje corto costero</strong> (Kombos, Banjul, el ferry de Barra y el conjunto UNESCO de Kunta Kinteh, unos 220 km y 4-6 días) y una "
                   "<strong>variante del río arriba</strong> que remonta la orilla sur hasta Janjanbureh y los megalitos de Wassu antes de salir por Farafenni (unos 700 km y 8-10 días). "
                   "Es un país diminuto —11.300 km², el más pequeño del África continental, menos de 50 km de ancho— pero con tres cosas que no tiene ningún vecino: es <strong>anglófono en pleno mundo francófono</strong>, tiene "
                   "<strong>dos sitios Patrimonio de la Humanidad</strong> en cien kilómetros de río, y es probablemente <strong>el mejor país del mundo para empezar a mirar aves</strong>: 621 especies registradas, todos los hábitats a menos de una hora unos de otros, "
                   "y la red de guías ornitológicos locales más veterana de África occidental."),
    decision=("Gambia deja de ser el «desvío opcional» que era en versiones anteriores de esta ficha: pasa a ser una <strong>parada confirmada del corredor de subida</strong>, por decisión expresa del dueño del proyecto "
              "(«a la vuelta me gustaría ir por el suroeste de Senegal, cruzar Gambia y subir hacia Dakar y pasar por el lago rosa»). Lo que sigue abierto no es SI se entra, sino POR DÓNDE se sale: "
              "<strong>Amdalai/Karang</strong> (eje corto, salida al delta del Saloum y la Petite Côte) o <strong>Keur Ayib/Farafenni</strong> (variante del río arriba, salida al interior por Kaolack). "
              "Ojo: la ficha de Senegal sigue describiendo Gambia como «alternativa que no forma parte del corredor base» — hay que actualizarla para que las dos sean coherentes."),
    facts=[
        ("Rol en la ruta", "ÚNICO país del viaje que se visita solo a la vuelta. Se entra desde la Casamance (suroeste de Senegal) y se sale de nuevo a Senegal por el norte, camino de Dakar y el lago Retba."),
        ("Ventana prevista", "Tramo final del viaje, dentro del corredor de subida por la costa occidental; entre Senegal (Casamance) y Senegal (Dakar). Estación seca — noviembre a mayo — que además es la ventana buena para las aves."),
        ("Entrada", "Séléti, desde la Casamance por la carretera Ziguinchor-Brikama. Alternativa litoral por Darsilami/Kartong POR CONFIRMAR (el cruce del Allahein puede no ser practicable con vehículo)."),
        ("Salida", "Amdalai/Karang (eje corto, hacia el delta del Saloum y la Petite Côte) o Keur Ayib/Farafenni (variante del río, hacia Kaolack). Entrada y salida por puntos distintos en ambos casos."),
        ("El río", "Dos formas de cruzarlo: el ferry Banjul-Barra (rito overlander, pero cola de 2-5 h y averías recurrentes) o el puente de Senegambia en Farafenni (1,9 km, abierto en 2019, fiable). El puente es el plan seguro."),
        ("Visado", "PUNTO CRÍTICO SIN CERRAR: la versión anterior de esta ficha daba por buena una exención para españoles, pero no se ha podido verificar con fuente oficial en esta revisión. Confirmar con la Gambia Immigration Department o la embajada antes de contar con ello."),
        ("Vehículos", "Permiso temporal de importación en frontera; la ECOWAS Brown Card (Carte Brune CEDEAO) es válida — Gambia es miembro de la CEDEAO, igual que Senegal, así que el seguro del tramo occidental sigue cubriendo."),
        ("Moneda", "Dalasi (GMD), ~73 dalasis por dólar a principios de 2026. Se sale de la zona del franco CFA al entrar y se vuelve a ella al salir, en cuestión de días: cambiar solo lo imprescindible."),
        ("Idioma", "Inglés, única lengua oficial (mandinga como primera lengua del 38 % de la población). Es el único país anglófono de todo el bloque Senegal-Mauritania-Marruecos: llevar los papeles también en inglés."),
        ("Aves", "621 especies registradas y ningún endemismo, en un país de 11.300 km². Es su mayor atractivo y la razón por la que tiene turismo especializado propio."),
        ("Seguridad", "País estable, sin alertas relevantes. El único tema recurrente son los «bumsters» de la franja turística: presión insistente, no delincuencia violenta."),
        ("Perro", "Sin fuente oficial localizada sobre importación de mascotas: es de los agujeros documentales de la ruta. Playas y pueblos cómodos; parques nacionales prohibidos."),
    ],
    alerts=[
        "VISADO — el punto más importante que hay que cerrar de esta ficha. La revisión anterior afirmaba exención para pasaportes españoles, pero en esta revisión no se ha podido confirmar con fuente oficial: la política de visados publicada nombra exención para los estados de la CEDEAO y un puñado de microestados europeos, y contempla visado a la llegada para algunas nacionalidades. NO dar por supuesta la exención: confirmar por escrito con la Gambia Immigration Department o con la embajada/alto comisionado antes de salir de Europa, y de nuevo 30-60 días antes.",
        "El río se cruza dos veces en la variante corta (ida por el ferry, vuelta no hace falta) y la decisión ferry-vs-puente condiciona un día entero de calendario. El ferry Banjul-Barra tiene historial de averías y suspensiones: confirmarlo el día antes y no construir el plan sobre él.",
        "Parque Nacional del río Gambia (chimpancés): NO está abierto al público y desembarcar en las islas está PROHIBIDO. Solo se ve a través del propio Chimpanzee Rehabilitation Project. Resolverlo por correo antes de subir el río.",
        "Dos fronteras extra en el tramo final del viaje (entrada desde Casamance y salida hacia Senegal norte), con cambio de moneda y de idioma en medio, a pocas semanas de volver a Europa: prever tiempo y no apurar el calendario de la reentrada del perro a la UE.",
        "Perro: no se ha localizado fuente oficial gambiana sobre importación de animales de compañía. Es un agujero documental y hay que cerrarlo por escrito con el Department of Livestock Services antes de llegar.",
        "Malaria en todo el territorio y todo el año, con pico en la estación húmeda (junio-octubre). El río arriba y el manglar son los puntos de mayor exposición.",
        "Estacionalidad: la ventana buena es de noviembre a mayo (seco). En julio-septiembre las pistas del interior se degradan, el calor húmedo es duro para el perro y muchos campamentos del río cierran.",
        "Dron: normativa poco desarrollada y, por lo mismo, imprevisible. Sin autorización escrita de la GCAA, no introducirlo.",
    ],
    ruta_intro=("Un solo paso por el país, en la subida, pero con <strong>dos formas muy distintas de atravesarlo</strong>. El <strong>eje corto costero</strong> entra por Séléti, hace los Kombos y Banjul, cruza el río en el ferry de Barra, "
                "remata el conjunto UNESCO de Kunta Kinteh y sale por Amdalai: unos 220 km y 4-6 días, y es la opción si el calendario aprieta. La <strong>variante del río arriba</strong> añade la Gambia real: remonta la orilla sur hasta "
                "Kiang West y Tendaba, cruza por el puente de Senegambia, llega a Janjanbureh y a los megalitos de Wassu, y sale por Keur Ayib — unos 700 km ida y vuelta y 8-10 días. "
                "Las dos se pueden combinar: hacer los Kombos y la costa, subir el río, y volver a bajar para el bloque de Kunta Kinteh antes de salir por Amdalai. "
                "Etapas calculadas sobre una media de <strong>250 km/día</strong>, aunque en Gambia la limitación nunca es la distancia sino los cruces de río y el ritmo del país."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Eje corto 1 · Entrada y sur de los Kombos", "Séléti → Brikama → Kartong → Tanji", "~90 km · 2 días · playas vacías y el primer bloque de aves"),
        ("Eje corto 2 · Los Kombos y la costa turística", "Tanji → Bijilo/Kololi → Kotu → Bakau (Katchikally) → Serrekunda", "~30 km · 2 días · base logística, mercado, veterinario, Kotu Bridge"),
        ("Eje corto 3 · Abuko y Makasutu", "Serrekunda → Abuko → Makasutu (bolong de Mandina)", "~60 km en bucle · 1-2 días · perro prohibido en Abuko"),
        ("Eje corto 4 · Capital y cruce del río", "Serrekunda → Banjul (Arco 22) → ferry → Barra (Fuerte Bullen)", "~25 km · 1 día ENTERO por la cola del ferry"),
        ("Eje corto 5 · El bloque UNESCO del estuario", "Barra → Juffureh/Albreda → isla de Kunta Kinteh → Barra", "~60 km ida y vuelta · 1 día · piragua incluida"),
        ("Eje corto 6 · Niumi y salida al Saloum", "Barra → Niumi NP / Jinack → Amdalai/Karang (Senegal)", "~40 km · 1-2 días · enlaza con Toubacouta y el delta del Saloum"),
        ("Variante río 1 · Orilla sur hasta Tendaba", "Serrekunda → Brikama → South Bank Road → Tendaba (Kiang West)", "~145 km · 1-2 días · el mejor parque continental del país"),
        ("Variante río 2 · Manglar de Bao Bolong", "Tendaba → piragua al Bao Bolong → Tendaba", "medio día en barca · 1 día · 268 especies de aves"),
        ("Variante río 3 · Cruce por el puente", "Tendaba → Soma → puente de Senegambia → Farafenni", "~70 km · ½ día · alternativa fiable al ferry"),
        ("Variante río 4 · Río arriba a Janjanbureh", "Soma → Bansang → Janjanbureh (isla de MacCarthy)", "~180 km · 2 días · combustible escaso, garrafa de reserva"),
        ("Variante río 5 · Megalitos y chimpancés", "Janjanbureh → ferry a Lamin Koto → Wassu → (río Gambia NP desde el cauce)", "~50 km · 1-2 días · parque cerrado al público, confirmar antes"),
        ("Variante río 6 · Regreso y salida este", "Wassu → Kuntaur → orilla norte → Farafenni → Keur Ayib (Senegal)", "~190 km · 2 días · enlaza con Kaolack por el interior"),
        ("Enlace con Senegal (contexto)", "Salida → Kaolack o delta del Saloum → Dakar → Lac Rose (lago Retba)", "~250-320 km · 2-3 días · ya en ficha de Senegal"),
    ],
    offroad=[
        "Pistas del sur de los Kombos (Kartong, Gunjur, Sanyang, Tanji): la carretera costera está asfaltada a tramos, pero los accesos a las playas y a los campamentos son arena blanda y pista de laterita. El acceso a la playa de Kartong y los ramales de Sanyang Point son arena de verdad: reducir presión de neumáticos y no bajar solo con un vehículo. Es el único tramo genuinamente 4x4 de la franja costera.",
        "North Bank Road (Barra → Juffureh → Kerewan → Farafenni): la carretera de la orilla norte está en peor estado que la del sur, con tramos de laterita, baches severos y pasos de bolong. Es el enlace natural entre el bloque UNESCO del estuario y el río arriba si se quiere hacer todo por el norte sin volver a cruzar. Confirmar el estado sobre el terreno: cambia mucho de una estación a otra.",
        "Accesos a Kiang West y a Tubabkollon Point: dentro del parque se circula por pistas de tierra y arena entre sabana y baobabs, con vados de bolong y zonas de barro en cuanto llueve. Es el único sitio del país donde se conduce de verdad en terreno natural, y hay que ir con guía del Department of Parks and Wildlife Management. Perro prohibido.",
        "Ramales del río arriba (Kuntaur, Wassu, Kerr Batch, Georgetown): pistas de arena y laterita entre campos de cacahuete y mijo, con poco tráfico y ningún servicio. Nada técnico, pero muy expuesto: sin combustible, sin taller y con cobertura irregular. Garrafa de reserva obligatoria desde Soma.",
        "Jinack Island: solo se llega en piragua desde Barra o desde Bakau. No hay acceso rodado desde Gambia (por el lado senegalés sí existe pista desde el Saloum, POR CONFIRMAR si es practicable y si tiene sentido aduanero). Los vehículos se quedan en tierra.",
        "Norma del proyecto en Gambia: no conducir de noche. No es por inseguridad — es por peatones, bicicletas sin luz, burros y carros en todas las carreteras, incluida la South Bank Road.",
    ],
    senderismo=[
        "SENDERO ORNITOLÓGICO DE BIJILO (Monkey Park), Kololi: 4,5 km de circuito entre bosque costero, matorral de duna y playa, con el ramal paralelo al mar que usan todos los guías de aves. Dos horas al amanecer, llano, con monos a un metro del camino. Es la mejor primera mañana posible en Gambia. Perro prohibido.",
        "CIRCUITO A PIE DE ABUKO: dos a tres horas por el bosque de galería del arroyo Lamin, con la poza de los cocodrilos, el observatorio sobre el agua y el orfanato de fauna. 270 especies de aves en 107 hectáreas y la mejor densidad de observación del país. Llano y sombreado, pero húmedo y con mosquitos: repelente. Perro prohibido.",
        "KOTU BRIDGE Y KOTU PONDS: no es una excursión, es un paseo de dos kilómetros por el puente, el arroyo y los arrozales que pueden dar cuarenta especies en una mañana sin esforzarse. El sitio de observación de aves más famoso del país y el punto de encuentro de los guías locales. Se hace con el perro atado, aunque mejor sin él si se va a mirar de verdad.",
        "TUBABKOLLON POINT, Kiang West: caminata corta desde la pista hasta el escarpe sobre el río, el mejor mirador del parque para ver fauna bajando a beber y para el águila volatinera, emblema del sitio. Guía del parque obligatorio. Perro prohibido.",
        "BOSQUE DE MAKASUTU: recorrido guiado a pie por los cuatro hábitats (manglar, palmeral, sabana y bosque de galería), combinado con la piragua por el bolong de Mandina al amanecer o con la marea subiendo. Media jornada, llano, con guía mandinga. Es propiedad privada: la política de mascotas se puede negociar.",
        "PLAYA DE KARTONG A LA BOCA DEL ALLAHEIN: paseo largo de arena, varios kilómetros, hasta la desembocadura que hace de frontera con la Casamance, con las lagunas del observatorio de aves y la poza sagrada de Folonko de remate. Sin sombra: al amanecer o al atardecer. El mejor paseo del país para hacer con el perro suelto.",
        "CAMPO DE MEGALITOS DE WASSU: no es una caminata, pero el circuito entre los once círculos, los túmulos y el museo se hace a pie en una hora larga. Llano, sin sombra, y con la lección de humildad de estar delante del mayor complejo megalítico de África sin saber casi nada de quién lo hizo.",
        "JANJANBUREH A PIE: la vuelta completa al viejo Georgetown colonial son un par de horas por calles de arena entre casas en ruina, el embarcadero, el mercado y la orilla. Se complementa con el paseo en barca del río alto al amanecer, buscando hipopótamos.",
    ],
    acampada=[
        "Kombos (Kotu, Kololi, Bakau, Fajara): no hay campings al uso, pero sí abundantes hoteles y guesthouses pequeños con aparcamiento en recinto cerrado, a precios muy bajos fuera de temporada alta europea. Es lo que sale a cuenta: la acampada libre en la franja turística no es viable ni recomendable.",
        "Sur de los Kombos (Kartong, Gunjur, Sanyang, Tanji): pequeños ecolodges y campamentos junto a la arena, con espacio para los vehículos, mucho menos concurridos y mucho más baratos. Es la mejor pernocta del país para el perro.",
        "Tendaba Camp (Kiang West): el clásico del río, funcionando desde los años setenta, con aparcamiento, restaurante y embarcadero propio para las salidas al Bao Bolong. Pieza central de la variante del río arriba y del plan B del perro.",
        "Janjanbureh: un par de campamentos sencillos en la isla y en la orilla, con espacio para vehículos. Confirmar que siguen abiertos: la oferta del río arriba fluctúa y varios sitios cerraron tras la caída del turismo.",
        "Jinack Island: campamentos muy básicos en la isla-barrera; se llega en piragua, así que los vehículos se quedan en Barra. Solo tiene sentido si se quiere una noche de playa absolutamente vacía.",
        "Acampada libre: el país es pequeño, llano y muy poblado en la costa, así que apenas hay espacio discreto; del río arriba sí existe, y la norma de la subregión es pedir permiso al alcalde o al jefe del pueblo antes de instalarse. En general, en Gambia sale más a cuenta el guesthouse barato que el vivac.",
        "Aparcamiento de los vehículos durante el ferry: NO dejarlos sin vigilancia en la cola del embarcadero de Banjul. Si se hace el bloque de Kunta Kinteh dejando los vehículos en el sur, buscar recinto cerrado en Banjul y cruzar a pie: es una opción real y mucho más rápida.",
    ],
    visado=[
        "PUNTO CRÍTICO SIN CERRAR. La revisión anterior de esta ficha daba por buena una exención de visado para pasaportes españoles; en esta revisión NO se ha podido confirmar con fuente oficial. La política de visados publicada nombra exención para los estados de la CEDEAO y para un grupo reducido de microestados europeos (Andorra, Liechtenstein, San Marino, Mónaco, Vaticano), y visado a la llegada para algunas nacionalidades concretas. España no aparece en las listas que se han podido verificar.",
        "ACCIÓN: confirmar por escrito con la Gambia Immigration Department (o con el Alto Comisionado/embajada de Gambia acreditada ante España) si el pasaporte español necesita visado, si existe visado a la llegada en frontera TERRESTRE (no solo en el aeropuerto de Banjul, que es la trampa habitual) y cuál es la estancia concedida. Es la pregunta número uno de esta ficha.",
        "Si finalmente hace falta visado, la gestión natural es en Dakar, en la bajada o al llegar a Senegal en la subida — no dejarlo para la frontera.",
        "Certificado internacional de fiebre amarilla: exigible si se procede de zona endémica, que es exactamente nuestro caso (venimos de todo el golfo de Guinea y África central). Llevarlo siempre accesible.",
        "Pasaporte con vigencia holgada: se entra y se sale en pocos días pero son dos sellos más, y quedan todavía Senegal, Mauritania y Marruecos por delante.",
    ],
    fronteras_rows=[
        ("Entrada (ambos corredores)", "Séléti (desde la Casamance, eje Ziguinchor-Brikama)", "Paso principal del sur y la entrada natural desde la Casamance. Se sale del franco CFA y se entra en el dalasi. POR CONFIRMAR horario real y coordenada exacta 72 h antes."),
        ("Entrada alternativa", "Darsilami / Kartong-Allahein (litoral)", "Entrada directa a Kartong desde la Basse Casamance. El cruce del río Allahein es en piragua para peatones: POR CONFIRMAR si existe paso practicable con vehículo. No planificar sobre esta opción sin verificarla."),
        ("Salida (eje corto)", "Amdalai / Karang (hacia Senegal, Petite Côte)", "A 30 km al norte de Barra. Enlaza con Toubacouta, el delta del Saloum, Kaolack y Dakar — y por tanto con el lago Retba. Muy usado por overlanders. Cruzar por la mañana."),
        ("Salida (variante del río)", "Keur Ayib / Farafenni (Trans-Gambia)", "Al norte de Farafenni. Enlaza con Kaolack por el interior. Coordenada coherente con la que ya figura en la ficha de Senegal."),
        ("Cruce interior del río", "Ferry Banjul–Barra", "No es frontera, pero funciona como tal en tiempo: 30-45 min de travesía y 2-5 h de cola. Historial de averías. Confirmar operación el día antes."),
        ("Cruce interior del río (alternativa fiable)", "Puente de Senegambia (Farafenni–Soma)", "1,9 km, abierto a vehículos ligeros el 21 de enero de 2019. Es la opción previsible. Peaje POR CONFIRMAR."),
    ],
    vehiculos=[
        "PERMISO TEMPORAL DE IMPORTACIÓN en frontera para cada vehículo. POR CONFIRMAR si se admite/exige carnet de paso (CPD) para una estancia tan corta, o si basta el passavant/permiso temporal que se emite en el puesto. Preguntarlo en Séléti al entrar y guardar el documento: hay que presentarlo al salir.",
        "SEGURO · ECOWAS BROWN CARD (Carte Brune CEDEAO): Gambia es miembro de la CEDEAO y participa en el esquema, igual que Senegal, así que la tarjeta que se viene usando desde el golfo de Guinea sigue siendo válida. Comprobar la fecha de validez antes de entrar: si caduca en este tramo, se renueva mejor en Dakar que en Banjul.",
        "Permiso internacional de conducir: llevarlo accesible junto al carnet nacional. Conducción por la derecha.",
        "Dos vehículos, dos juegos de papeles: como se entra y se sale por puntos distintos y en pocos días, conviene fotografiar todos los documentos y sellos al entrar, por si hay discrepancia al salir.",
        "El estado de la red es razonable en la costa y en la South Bank Road, y bastante peor en la orilla norte. Nada exige 4x4 salvo las pistas de playa y las de Kiang West, pero los baches profundos sí castigan la suspensión: velocidad moderada.",
        "Norma del proyecto en Gambia: no conducir de noche — peatones, bicicletas sin luz y animales en todas las carreteras.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autoridad competente: Gambia Civil Aviation Authority (GCAA). No se ha localizado un procedimiento público de registro y autorización equivalente al de Ghana o Marruecos — esa ausencia de norma clara es el riesgo, porque deja la decisión al criterio del funcionario.",
        "Solicitar información y autorización POR ESCRITO a la GCAA con antelación. Sin respuesta por escrito, no introducir el dron: se entra y se sale de Senegal en pocos días y no compensa arriesgar el equipo.",
        "Nunca volar sobre el aeropuerto internacional de Banjul, el puerto, la State House, el Arco 22, instalaciones militares, la cárcel de Janjanbureh ni el entorno de los pasos fronterizos y del embarcadero del ferry.",
        "Contexto de ruta: el dron llega a Gambia después de haber atravesado Marruecos, donde la confiscación en aduana es práctica habitual y documentada. Si se ha optado por dejarlo fuera del viaje en el tramo marroquí, este apartado es irrelevante; si viaja, aquí conviene mantenerlo guardado.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Sin confirmación de servicio activo ni de licencia en Gambia a la fecha de esta revisión: tratar como NO GARANTIZADO y no planificar ninguna dependencia.",
        "SIM local: Africell es la de mejor cobertura, con Qcell y Gamcel como alternativas. Registro con pasaporte.",
        "Alternativa práctica para un país que se cruza en días: mantener activa la SIM senegalesa en roaming y comprar gambiana solo si se sube el río, donde la cobertura se vuelve irregular.",
        "Cobertura móvil razonable en todos los Kombos, en el eje de la South Bank Road y en los núcleos del río; se degrada en el interior norte y en Kiang West.",
        "Mensajería satelital independiente: no es imprescindible en Gambia por lo pequeño y poblado del país, pero si ya se lleva del tramo sahariano, mantenerla activa en el bloque del río arriba.",
    ],
    perro_intro=[
        "AGUJERO DOCUMENTAL: no se ha localizado fuente oficial gambiana (Department of Livestock Services / Ministry of Agriculture) con requisitos publicados de importación de animales de compañía. El dossier del perro del proyecto clasifica Gambia como «sin confirmar», y además es el único país que se cruza SOLO en la vuelta, así que basta con un permiso, no dos.",
        "ACCIÓN: escribir al Department of Livestock Services de Gambia y, en paralelo, al Alto Comisionado/embajada, preguntando expresamente por ENTRADA TERRESTRE desde Senegal, nombrando el puesto (Séléti) y el de salida (Amdalai/Karang o Keur Ayib). Hacerlo desde Senegal, con 3-4 semanas de margen.",
        "Documentación mínima a llevar, en INGLÉS (Gambia es anglófona, a diferencia de todos sus vecinos): pasaporte europeo de animal de compañía, microchip legible, certificado veterinario internacional reciente y vacuna antirrábica en vigor. Llevar también la versión francesa, que es la que valdrá en Senegal a ambos lados.",
        "Regla común de la subregión francófona —y previsiblemente también aquí—: rabia administrada entre 30 días y 12 meses antes de la entrada. Si el perro lleva vacuna trienal, revacunar anualmente de todos modos, que es además lo que protege la titulación serológica para la reentrada a la UE.",
        "Veterinarios: los hay en los Kombos (Serrekunda, Fajara, Kololi) para lo básico. Para cualquier cosa seria, Dakar está a 300 km y es el mejor punto veterinario de África occidental.",
        "Gambia está a pocas semanas del final del viaje: es un buen momento para revisar que la cartilla y los plazos de la reentrada a la UE siguen cuadrando, con Dakar todavía por delante como última gran plaza veterinaria antes de Marruecos.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en todo el país y todo el año, con pico en la estación húmeda (junio-octubre) y máxima exposición en el manglar y el río arriba: profilaxis a valorar con Sanidad Exterior, más repelente y mosquitera. Es el riesgo sanitario número uno.",
        "Fiebre amarilla: certificado internacional exigible si se procede de zona endémica — que es nuestro caso. Llevarlo accesible.",
        "Agua: no beber del grifo. Agua embotellada disponible sin problema en la franja costera y en los núcleos del río; del río arriba, cargar reserva completa antes de salir de Soma.",
        "Cólera, tifoidea y hepatitis A endémicas: vacunas recomendables. Precaución con el marisco y el pescado crudo pese a la tentación de la playa de Tanji.",
        "Bilharziosis (esquistosomiasis) en aguas dulces estancadas del río: no bañarse en el río Gambia ni en los bolongs. El baño es en el mar.",
        "Calor húmedo todo el año en la costa: es el factor que más condiciona el ritmo diario, sobre todo para el perro. Conducir a primera hora y descansar en las horas centrales.",
        "Edward Francis Small Teaching Hospital (Banjul) es la referencia del país, con capacidad limitada. Seguro con evacuación médica imprescindible: la evacuación realista es a Dakar, a 300 km.",
    ],
    seguridad_intro=("Gambia es un país pequeño, estable y sin conflicto, y la ruta no está condicionada por la seguridad en ningún punto. La transición democrática desde 2017 ha sido pacífica y el país tiene incluso una policía turística propia. "
                     "Lo único que sí hay que entender antes de llegar es el fenómeno de los «bumsters», que no es un riesgo de seguridad sino una forma de presión social continua en la franja hotelera; y lo único que hay que gestionar de verdad es el ferry, "
                     "el aparcamiento y el calor."),
    seguridad=[
        "«BUMSTERS»: jóvenes que abordan a los turistas en las playas y en la franja de Senegambia ofreciéndose como guía, amigo o acompañante, a veces buscando una relación sentimental o un patrocinio a largo plazo. No es delincuencia violenta: es insistencia, y responde a un desempleo juvenil altísimo en un país que vive del turismo. Lo que funciona es ser educado pero inequívoco desde el primer segundo, no aceptar compañía «un momento» y no dar el teléfono; lo que no funciona es la evasiva amable, que se lee como una puerta abierta. Fuera de la franja hotelera el fenómeno prácticamente desaparece.",
        "Policía turística: existe y patrulla la franja de Kololi/Senegambia. Es un recurso real si una situación se vuelve incómoda.",
        "Robo oportunista en el mercado de Serrekunda, en el Albert Market de Banjul y en la cola del ferry: carteristas y descuidos. Nada violento como norma. Aparcamiento vigilado siempre y nada visible dentro del vehículo.",
        "Cola del ferry de Banjul: es el punto de mayor concentración de gente y de espera del país. No dejar los vehículos sin vigilancia, cerrar todo y no separar al grupo.",
        "Controles de carretera: existen pero son poco frecuentes y en general correctos. Llevar a mano pasaporte, visado si finalmente hace falta, permiso internacional, papeles del vehículo y la Brown Card.",
        "Drogas: penas severas. Evitar cualquier ofrecimiento, que en la franja turística los hay.",
        "Fotografía: no fotografiar instalaciones militares, el puerto, la State House ni el entorno de los pasos fronterizos, norma común a toda la subregión.",
        "Revisar el aviso de Exteriores 72 h antes de la entrada. La referencia consular es la Embajada de España en DAKAR, no Banjul.",
    ],
    agua=[
        "Agua de boca: embotellada disponible sin problema en toda la franja costera, en Serrekunda y en los núcleos de la South Bank Road. Del río arriba (Janjanbureh, Kuntaur, Wassu) la oferta es mucho más limitada: cargar la reserva completa antes de salir de Soma.",
        "Recarga del depósito de uso general (ducha, aseo, vajilla, limpieza): los hoteles y guesthouses de Kotu, Kololi y Bakau permiten llenar con manguera, igual que el Tendaba Camp, que es el punto clave de la variante del río. Confirmar en recepción.",
        "No beber del grifo en ningún punto del país. Filtrar o potabilizar el agua de recarga si se va a usar para cocinar.",
        "No bañarse en el río ni en los bolongs (bilharziosis): el agua dulce es para el depósito, no para el cuerpo.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje costero: la conurbación Brikama-Serrekunda-Kololi-Banjul concentra estaciones formales (GACH, Jah Oil, Total) a pocos kilómetros unas de otras, y es donde hay que repostar a fondo.",
        "Orilla sur hasta Soma: oferta razonable en los núcleos de la South Bank Road (Brikama, Bwiam, Kalagi, Soma). Soma/Farafenni, junto al puente, es el último nudo fiable antes del río arriba.",
        "Del río arriba (Soma → Bansang → Janjanbureh → Kuntaur): oferta escasa e irregular. Salir de Soma con depósitos llenos y GARRAFA DE RESERVA. POR CONFIRMAR sobre el terreno cuáles de las estaciones del interior están operativas.",
        "Orilla norte (Barra → Kerewan → Farafenni): oferta limitada. Repostar en Barra nada más desembarcar si se va a hacer el bloque de Juffureh y luego subir hacia Farafenni.",
        "Moneda: dalasi (GMD), ~73 por dólar a principios de 2026. Muchas estaciones no aceptan tarjeta: llevar efectivo en dalasis. Cambiar solo lo imprescindible, porque se vuelve a la zona CFA en cuestión de días.",
    ],
    experiencias_intro="Relatos y comentarios reales de otros overlanders y viajeros sobre Gambia, para contrastar con el contenido oficial de esta ficha. El país está muy documentado por el turismo europeo de playa y de aves, y bastante menos por overlanders con vehículo propio: los puntos calientes son siempre el ferry, el cambio de moneda y los «bumsters».",
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("VISADO · pasaporte español", "LA PREGUNTA NÚMERO UNO DE ESTA FICHA. Confirmar por escrito con la Gambia Immigration Department o la representación diplomática gambiana: ¿hace falta visado?, ¿hay visado a la llegada en frontera TERRESTRE (no solo en el aeropuerto de Banjul)?, ¿qué estancia se concede? La revisión anterior daba por buena una exención que no se ha podido verificar"),
        ("Salida del país · qué frontera", "Decidir entre Amdalai/Karang (eje corto, salida al delta del Saloum y la Petite Côte) y Keur Ayib/Farafenni (variante del río, salida por el interior a Kaolack). La decisión depende de si se sube el río o no"),
        ("Coherencia con la ficha de Senegal", "La ficha de Senegal sigue describiendo Gambia como «alternativa que no forma parte del corredor base». Actualizarla para reflejar que Gambia es ahora una parada confirmada del corredor de subida"),
        ("Entrada por Séléti", "Confirmar coordenada exacta, horario real y trámite de vehículo (¿CPD o passavant?) 72 h antes"),
        ("Entrada litoral por Kartong/Allahein", "Confirmar si el cruce del río Allahein es practicable con vehículo o si es solo peatonal en piragua. Si no lo es, el acceso a Kartong se hace desde dentro de Gambia, no desde Casamance"),
        ("Ferry Banjul–Barra vs puente de Senegambia", "Confirmar el día antes que el ferry opera y decidir sobre el terreno; el puente es el plan fiable pero añade ~110 km. Confirmar también el peaje del puente, hoy sin dato"),
        ("Perro · requisitos de entrada", "Escribir al Department of Livestock Services de Gambia desde Senegal, con 3-4 semanas de margen, preguntando por entrada TERRESTRE y nombrando el puesto de entrada y el de salida. Es un agujero documental del dossier del perro"),
        ("Perro · Tendaba Camp", "Confirmar por escrito que el campamento admite al perro en el recinto mientras los demás hacen el parque y el Bao Bolong: es la pieza del plan B de la variante del río"),
        ("Perro · alojamientos de playa", "Confirmar política de mascotas en Kartong, Tanji, Kotu y Kololi antes de reservar: casi ninguno la publica"),
        ("Parque Nacional del río Gambia (chimpancés)", "Escribir al Chimpanzee Rehabilitation Project / campamento de Badi Mayo para saber si hay salida autorizada disponible en nuestra ventana. El parque NO está abierto al público: sin respuesta, se cae del plan"),
        ("Dron", "Solicitar información y autorización escrita a la Gambia Civil Aviation Authority; sin respuesta por escrito, no introducirlo"),
        ("Starlink", "Verificar en el mapa oficial 30-60 días antes si Gambia ha pasado a estar licenciada; hoy no consta"),
        ("Representación consular en Banjul", "Verificar si existe consulado honorario español operativo y su contacto; la referencia real es la Embajada de España en Dakar"),
        ("Estado de la North Bank Road", "Confirmar en iOverlander/Tracks4Africa el estado real del eje Barra-Kerewan-Farafenni antes de planificar el enlace por la orilla norte"),
        ("Combustible del río arriba", "Confirmar qué estaciones están operativas entre Soma y Kuntaur; hoy solo se puede dar por buena la de Soma/Farafenni"),
        ("Fotos pendientes de sustituir", "Solo hay dos fotos de Gambia verificadas en Wikimedia Commons para esta revisión (isla de Kunta Kinteh y playa de Kotu), reutilizadas como IMAGEN DE REFERENCIA en el resto de PDIs y así indicado en cada descripción. Sustituir por fotos propias cuando las tengamos"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. El apartado de visado está expresamente SIN CERRAR y es lo primero que hay que resolver.",
    emergency="Policía 117 · Bomberos 118 · Ambulancia 116 (verificar los números vigentes al entrar: en Gambia cambian con frecuencia y la cobertura del servicio es limitada). Sin embajada de España residente en Banjul: la referencia consular es la EMBAJADA DE ESPAÑA EN DAKAR (Senegal), a 300 km.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

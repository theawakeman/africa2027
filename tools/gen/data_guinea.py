# -*- coding: utf-8 -*-
"""Guinea (Conakry) — ficha completa, corredor doble bajada/subida (12 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== BAJADA · FOUTA DJALLON: Koundara -> Labé -> Mali/Loura -> Pita -> Doucki -> Dalaba -> Mamou -> Kindia -> Conakry =====
    dict(n=1, name="Koundara y el Parque Nacional del Badiar", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido", time="½–1 día",
         lat=12.4833, lon=-13.3000,
         desc="Primera población guineana tras el paso de Sambaïlo y capital de la prefectura del extremo noroeste. A pocos kilómetros al norte está el Parque Nacional del Badiar, unas 38.000 hectáreas de sabana arbolada y bosque de galería que son la continuación directa del Parque Nacional de Niokolo-Koba (Senegal) al otro lado de la frontera: juntos forman el complejo transfronterizo Niokolo-Badiar. Hay antílopes, facóqueros, babuinos, hipopótamos en los ríos y una avifauna muy rica, aunque la presión de caza y pastoreo ha sido intensa y la gestión es débil. POR CONFIRMAR sobre el terreno: si el parque tiene personal, tasas y pistas practicables en 2027, o si es un parque solo sobre el papel. Koundara tiene combustible, mercado y alojamiento elemental: es donde se hace la primera noche del país si la frontera se ha comido la tarde.",
         credit="Maarten van der Bent · CC BY-SA 2.0", source=W + "Fouta%20Djallon%20(14604722652).jpg?width=900"),
    dict(n=2, name="Labé · capital del Fouta Djallon", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=11.3167, lon=-12.2833,
         desc="Segunda o tercera ciudad del país y capital indiscutible de la Guinea Media: a 1.000 m de altitud, con clima fresco, el mayor mercado del altiplano —donde se ve la sociedad fulani del Fouta en estado puro, con sus tejidos índigo, su ganado y su artesanía de cuero— y la mejor base logística entre Conakry y la frontera senegalesa. Aquí hay combustible formal, talleres, banco con cajero, hospital regional y hoteles con aparcamiento. Detalle muy relevante para nosotros: Labé alberga el Laboratorio Regional Veterinario, uno de los pocos servicios veterinarios oficiales del interior del país y el recurso más cercano si hay que resolver algo con el perro fuera de Conakry. Es el nudo de los dos corredores: se pasa por aquí en la bajada y en la subida.",
         credit="Maarten van der Bent · CC BY-SA 2.0", source=W + "Fouta%20Djallon%20(14604722652).jpg?width=900"),
    dict(n=3, name="Monte Loura y la Dama de Mali (1.515 m)", cat="Naturaleza", prio="Alta", dog="permitido con precaución", time="1–2 días",
         lat=12.0833, lon=-12.3000,
         desc="El techo del Fouta Djallon y el punto más alto de toda África occidental fuera de las tierras altas camerunesas: 1.515 m sobre el borde norte del altiplano, junto al pueblo de Mali, a unos 120 km al norte de Labé. Su seña de identidad es «la Dame de Mali» (Fouta Djallon la llama «la Dama»), un perfil rocoso de decenas de metros que asoma sobre el vacío y que reproduce con una nitidez casi inquietante un rostro humano de mujer mirando al horizonte. Desde el borde de la meseta se domina la llanura senegalesa: es una de las vistas grandes de África occidental. El pueblo de Mali está a 1.400 m y es el sitio más fresco de Guinea —se duerme con manta y en diciembre-enero puede haber escarcha—. Subida a pie cómoda desde el pueblo, con guía local; excursión perfectamente compatible con el perro al estar fuera de espacio protegido. La carretera Labé-Mali es de las más espectaculares y peor asfaltadas del país.",
         credit="Maarten van der Bent · CC BY-SA 2.0", source=W + "Fouta%20Djallon%20(14604722652).jpg?width=900"),
    dict(n=4, name="Pita y las cataratas de Kinkon", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=10.9833, lon=-12.4000,
         desc="Pita es el centro del Fouta Djallon central y la base para las dos grandes cascadas de la región. Las chutes de Kinkon están a unos 12 km, sobre el río Kokoulo: una caída de unos 80 m en un cañón de arenisca, con una central hidroeléctrica en la parte alta que condiciona el caudal (si la presa retiene agua, la cascada se queda en nada: preguntar en Pita antes de ir). El entorno del cañón es magnífico, con paredes verticales de arenisca roja y bosque de galería en el fondo. Acceso por pista corta desde la carretera principal Labé-Mamou, practicable con 4x4 todo el año. Al ser zona de central eléctrica, no fotografiar las instalaciones ni volar el dron.",
         credit="Sayd224 · CC BY 4.0", source=W + "Chute%20de%20Kinkon.jpg?width=900"),
    dict(n=5, name="Cataratas de Kambadaga", cat="Naturaleza", prio="Alta", dog="permitido con precaución", time="½–1 día",
         lat=11.0167, lon=-12.5167,
         desc="La otra gran cascada de Pita y, para muchos viajeros, la mejor de Guinea: una sucesión de tres saltos escalonados sobre el mismo río Kokoulo, encajados en un cañón de arenisca, con pozas profundas y verdes donde se puede nadar. En plena estación húmeda el caudal es imponente; en seca se reduce, pero se puede bajar al cauce y recorrerlo. Está a unos 25 km de Pita por una pista de tierra con baches y vados, transitable en 4x4 salvo en lluvias fuertes. No hay entrada formal ni instalaciones: se paga una propina al pueblo y se baja a pie por el sendero. Excelente sitio para acampar con permiso del jefe del pueblo, y apto para el perro con correa en los tramos de roca mojada.",
         credit="Sayd224 · CC BY 4.0", source=W + "Chute%20de%20Kinkon.jpg?width=900"),
    dict(n=6, name="Doucki · el «Gran Cañón de Guinea»", cat="Naturaleza", prio="Alta", dog="permitido con precaución", time="3–4 días",
         lat=11.1500, lon=-12.6000,
         desc="El sitio de senderismo más famoso de África occidental entre mochileros, y probablemente el mejor del viaje entre Marruecos y Camerún. Un pueblo de unos 500 habitantes en el borde del altiplano, donde la meseta de arenisca se rompe en un sistema de cañones de varios cientos de metros de caída que baja hacia la llanura. Todo gira alrededor de Hassan Bah, el guía y anfitrión que lleva décadas abriendo y bautizando rutas: «Grand Canyon» (4 km, fácil), «Indiana Jones World» (5 km), «Hyena's Rock» (8 km), «Vultures Rock» (9 km), «The Caves» (8 km), «Bob Marley Stage» (14 km), «Wet & Wild» (13 km), «Chutes & Ladders» (~20 km, duro) y la «Valley Hike» (10-16 km, dura). Alojamiento en su campamento de cabañas sencillas con baño compartido; la fórmula habitual es todo incluido (cama, tres comidas, guía) por unos 50 USD al día por persona, sin tasas de entrada. Mínimo recomendado por quienes han ido: TRES noches. Acceso desde Pita: 2-3 horas por pista con baches. Mejor época: febrero-marzo. El perro puede acompañar en las rutas fáciles —es terreno comunitario, no parque— pero no en las de escalada por grietas y cuerdas: confirmarlo con Hassan.",
         credit="Maarten van der Bent · CC BY-SA 2.0", source=W + "Fouta%20Djallon%20(14604722652).jpg?width=900"),
    dict(n=7, name="Dalaba · la estación de altura colonial", cat="Cultura", prio="Media", dog="permitido", time="1 noche",
         lat=10.6833, lon=-12.2500,
         desc="A 1.200 m, en el corazón del Fouta, Dalaba fue la estación climática de la administración colonial francesa: el sitio donde los funcionarios subían a escapar del calor de Conakry, con jardines, huertas de fresas y hortalizas de clima templado que todavía se cultivan. Conserva el Chalet de Dalaba (la residencia del gobernador, de madera), los jardines de Chevalier, el antiguo sanatorio y —la joya— la Case à Palabres, una casa de asamblea tradicional fulani de planta circular cuyo interior está enteramente cubierto de esteras trenzadas y paneles de madera tallada y policromada por artesanos locales en los años cincuenta. Es uno de los mejores ejemplos vivos de arquitectura fulani del país. Clima fresco, buen mercado y la parada natural entre Pita y Mamou.",
         credit="Maarten van der Bent · CC BY-SA 2.0", source=W + "Fouta%20Djallon%20(14604722652).jpg?width=900"),
    dict(n=8, name="Cataratas de Ditinn", cat="Naturaleza", prio="Alta", dog="permitido con precaución", time="½ día",
         lat=10.7500, lon=-12.1667,
         desc="A unos 50 km al noreste de Dalaba, la cascada más fotogénica de Guinea: un chorro único que se descuelga en caída libre desde un labio de arenisca de unos 70-80 m sobre un circo de paredes verticales y vegetación colgante, con una poza al pie. Se puede ver desde el mirador superior o bajar al fondo del circo por el valle, que es la aproximación que recomiendan los guías locales y la que permite entender la escala del sitio. Acceso por pista desde Ditinn; propina al pueblo, sin infraestructura turística. Caudal muy dependiente de la estación: espectacular de julio a noviembre, hilo de agua en marzo-abril. Con el perro, correa en el borde del circo.",
         credit="Sayd224 · CC BY 4.0", source=W + "Chute%20de%20Kinkon.jpg?width=900"),
    dict(n=9, name="Kindia · el Velo de la Novia y el monte Gangan", cat="Naturaleza", prio="Alta", dog="permitido con precaución", time="1 noche",
         lat=10.0500, lon=-12.8542,
         desc="Cuarta ciudad del país, a 135 km de Conakry sobre la vieja línea del ferrocarril colonial, y la puerta del Fouta desde la costa. A pocos kilómetros está el Voile de la Mariée (el «Velo de la Novia»), una cascada de unos 70 m que se abre en abanico sobre una pared de granito —de ahí el nombre— con un área recreativa, bungalows y pozas para bañarse al pie; es la excursión clásica de fin de semana de los conakrianos y, por tanto, el sitio del país con más facilidad de acceso. Detrás se levanta el monte Gangan (1.117 m), un macizo de granito con paredes que atrae a escaladores y con rutas de subida a pie desde la carretera. Kindia tiene además el antiguo Institut Pasteur de Kindia (Pastoria), centro histórico de primatología donde se investigó con chimpancés desde los años veinte. Buena parada con el perro: agua, sombra y sendero.",
         credit="Alpha hmd · CC BY-SA 4.0", source=W + "Un%20aper%C3%A7u%20de%20la%20ville%20de%20conakry.jpg?width=900"),
    dict(n=10, name="Conakry", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=9.5092, lon=-13.7122,
         desc="Capital en una península estrecha de unos 35 km que se adentra en el Atlántico, con el centro administrativo y el puerto en la punta (Kaloum) y la ciudad real extendiéndose kilómetros hacia el interior. Es la única base logística de talla nacional: puerto, aeropuerto internacional, embajada de España, embajadas de Costa de Marfil y del resto del bloque (imprescindibles para los visados siguientes), bancos, supermercados, talleres y el Hôpital National Donka. Para ver: el Museo Nacional, la Gran Mezquita Fayçal (una de las mayores del África subsahariana), el mercado de Madina —un laberinto enorme— y el Palacio del Pueblo. Y la música: Conakry es una de las capitales musicales de África occidental, cuna del Bembeya Jazz National y de toda la escuela de orquestas nacionales de los años sesenta y setenta. Nudo compartido: se pasa por aquí en la bajada, y es donde se resuelven los trámites del bloque siguiente.",
         credit="Alpha hmd · CC BY-SA 4.0", source=W + "Un%20aper%C3%A7u%20de%20la%20ville%20de%20conakry.jpg?width=900"),
    dict(n=11, name="Islas de Los (Room, Kassa, Tamara)", cat="Costa", prio="Media", dog="no confirmado", time="1 día",
         lat=9.4500, lon=-13.8300,
         desc="Archipiélago a unos 20 minutos de lancha del puerto de Conakry: tres islas principales —Tamara (Factory), Room y Kassa— con playas de arena, cocoteros y agua tranquila, que fueron enclave británico hasta 1904 (cuando se cedieron a Francia) y antes puesto de la trata. Room es la más visitada, con restaurantes de playa y alojamientos sencillos; Kassa tiene explotación de bauxita en una parte y playas en la otra; Tamara conserva la antigua prisión colonial. Es la escapada de fin de semana de Conakry y la única costa realmente agradable del itinerario guineano. PERRO: por confirmar con el operador de la lancha — es una decisión del patrón, no una norma, y depende de si se contrata una piragua entera o se va en la lancha colectiva. Alternativa si no se puede: dejar al perro en el alojamiento de Conakry por turnos.",
         credit="Cnes - Spot Image · CC BY-SA 3.0", source=W + "Los%20island%20SPOT%201386.jpg?width=900"),
    dict(n=12, name="Boké y la costa de Boffa (variante costera)", cat="Cultura", prio="Baja", dog="permitido", time="½–1 día",
         lat=10.9333, lon=-14.3000,
         desc="VARIANTE OPCIONAL, fuera de los dos corredores principales: la carretera de la costa norte (N3) desde Conakry hacia Boffa y Boké. Boké conserva el Fortin de Boké, puesto colonial francés de 1878 junto al río Nunez, hoy museo regional con colecciones etnográficas y la celda donde estuvo preso el almamy Samory Touré; es una de las piezas de patrimonio colonial mejor conservadas del país. Por el camino, las playas de Bel Air y de Cap Verga (Boffa), largas, vacías y con arena firme. Es también la región de la bauxita: Boké es el centro minero más grande de Guinea y el tráfico de camiones y el polvo rojo marcan la carretera. ATENCIÓN: esta variante se acerca a la frontera de Guinea-Bisáu, que el protocolo del proyecto excluye sin excepción — se puede recorrer la costa, pero no se cruza ni se roza la frontera.",
         credit="Aboubacarkhoraa · CC BY-SA 4.0", source=W + "Mus%C3%A9e%20de%20Bok%C3%A9.jpg?width=900"),
    # ===== BAJADA · TRAVESÍA AL SURESTE: Mamou -> Faranah -> Kissidougou -> Macenta -> Nzérékoré -> Lola -> frontera CI =====
    dict(n=13, name="Faranah y el nacimiento del río Níger", cat="Naturaleza", prio="Alta", dog="permitido", time="1–2 días",
         lat=10.0333, lon=-10.7500,
         desc="Faranah es la ciudad del alto Níger —ciudad natal de Sékou Touré, con su mezquita monumental y un trazado de avenidas desproporcionado para su tamaño— y la base para el sitio geográfico más simbólico de toda África occidental: el nacimiento del río Níger, en las estribaciones de los montes Loma, cerca de la frontera con Sierra Leona. El tercer río más largo de África, que recorre 4.200 km describiendo un arco gigantesco por Malí y Níger hasta desembocar en Nigeria, arranca aquí como un manantial que se puede cruzar de un paso. El lugar es un claro de bosque con un pequeño monumento y un santuario local; se llega por pista desde Faranah y se termina a pie con guía del pueblo, que cobra propina. Coordenada del manantial aproximada: confirmar en Faranah. Que el Fouta Djallon y sus estribaciones den origen al Níger, al Senegal y al Gambia es lo que le vale a Guinea el apodo de «castillo de agua de África occidental».",
         credit="Alpha hmd · CC BY-SA 4.0", source=W + "Un%20aper%C3%A7u%20de%20la%20ville%20de%20conakry.jpg?width=900"),
    dict(n=14, name="Bosque de Ziama (Macenta) · Reserva de la Biosfera", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=8.4000, lon=-9.3167,
         desc="Unas 116.000 hectáreas de selva tropical húmeda de tierras bajas en la prefectura de Macenta, la mayor masa forestal que queda en Guinea y Reserva de la Biosfera de la UNESCO desde 1980. Es un fragmento del bloque forestal de Alto Guinea —uno de los 34 focos mundiales de biodiversidad— con elefantes de bosque (la última población de Guinea, muy reducida), chimpancés, búfalos enanos, cefalofines, pangolines y una avifauna excepcional. La base es Sérédou, antigua estación de investigación de la quina en plena selva. El acceso es por pista desde la carretera Macenta-Nzérékoré y la visita es caminata de bosque cerrado con guía comunitario: no hay safari ni observatorios, y ver un elefante es prácticamente imposible, pero el bosque primario en sí es lo que se viene a ver. POR CONFIRMAR: gestión, tasas y guías — depende del Centre Forestier de Nzérékoré. La zona forestal es también la región donde surgió el brote de ébola de 2013-2016: ver la sección de salud.",
         credit="Maarten van der Bent · CC BY-SA 2.0", source=W + "Fouta%20Djallon%20(14604722652).jpg?width=900"),
    dict(n=15, name="Nzérékoré y la Guinea forestal", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=7.7561, lon=-8.8179,
         desc="Tercera ciudad de Guinea y capital de la Guinée Forestière, un mundo completamente distinto al resto del país: selva húmeda en lugar de sabana, 1.800 mm de lluvia al año, y los pueblos kpelle, kissi, toma y guerzé en lugar de fulanis y malinkés — con sus máscaras y sus sociedades iniciáticas de bosque, que son una de las tradiciones vivas más potentes de África occidental. Nzérékoré es un gran mercado regional y un centro de orfebrería de plata, y funciona como el nudo logístico del sureste: combustible, banco, hospital regional, hoteles y el último sitio con servicios antes de la frontera de Costa de Marfil. Es la base tanto de la visita a los montes Nimba como del enlace hacia Lola. Ciudad activa, caótica y cordial.",
         credit="Alpha hmd · CC BY-SA 4.0", source=W + "Un%20aper%C3%A7u%20de%20la%20ville%20de%20conakry.jpg?width=900"),
    dict(n=16, name="Montes Nimba (UNESCO) · la triple frontera", cat="Patrimonio UNESCO", prio="Alta", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=7.6032, lon=-8.3910,
         desc="Reserva Natural Integral del Monte Nimba, Patrimonio Mundial de la UNESCO desde 1981 (y en la Lista del Patrimonio Mundial en Peligro desde 1992 por la presión minera): 17.632 hectáreas repartidas entre Guinea (12.540 ha) y Costa de Marfil (5.000 ha), en la cadena que hace de triple frontera con Liberia. Es una isla de praderas de altura sobre un mar de selva, con más de 317 especies de vertebrados —107 de ellas mamíferos— y más de 2.500 de invertebrados, muchas endémicas. Dos rarezas mundiales: el sapo vivíparo del Nimba (Nimbaphrynoides occidentalis), el único anfibio del mundo que pare crías vivas completamente formadas en lugar de poner huevos, y una población de chimpancés que usa piedras como herramientas. La visita se organiza desde Lola o Nzérékoré con guía obligatorio; es reserva integral, lo que significa que el acceso está restringido y hay zonas vedadas. PERRO: descartado, es reserva natural integral con grandes simios. Confirmar permisos con el Centre de Gestion de l'Environnement du Nimba-Simandou (CEGENS) antes de subir.",
         credit="Maarten van der Bent · CC BY-SA 2.0", source=W + "Fouta%20Djallon%20(14604722652).jpg?width=900"),
    # ===== SUBIDA · ALTA GUINEA: frontera CI -> Lola -> Nzérékoré -> Beyla -> Kankan -> Kouroussa -> Dabola -> Tougué -> Labé -> Koundara =====
    dict(n=17, name="Kankan · capital de la Alta Guinea", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=10.3853, lon=-9.3057,
         desc="Segunda ciudad del país por población y capital histórica del mundo malinké guineano, a orillas del río Milo, afluente del Níger. Es el gran centro del islam en Guinea —la Gran Mezquita de Kankan es uno de los santuarios más venerados del país— y una ciudad de erudición coránica desde el siglo XVIII. Universidad Julius Nyerere, mercado enorme, y la mejor plaza de servicios de todo el corredor de subida entre Nzérékoré y Labé: combustible formal, banco, hospital regional y hoteles con patio. Es también el corazón de la cultura griot mandinga, de donde salen los grandes intérpretes de kora y balafón. El calor es seco y fuerte (sabana, no selva): otro mundo respecto al Fouta.",
         credit="Alpha hmd · CC BY-SA 4.0", source=W + "Un%20aper%C3%A7u%20de%20la%20ville%20de%20conakry.jpg?width=900"),
    dict(n=18, name="Kouroussa y el Parque Nacional del Alto Níger", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=10.6500, lon=-9.8833,
         desc="Kouroussa es la ciudad del Níger propiamente dicho: aquí el río, que nació como un manantial cerca de Faranah, ya es navegable, y desde este punto arrancaban históricamente los vapores fluviales hacia Bamako. Es la ciudad natal del escritor Camara Laye, autor de «El niño africano». Al oeste se extiende el Parque Nacional del Alto Níger, unas 120.000 hectáreas de bosque seco y sabana en torno al bosque de Mafou —una de las últimas masas de bosque seco guineano intactas de África occidental— con hipopótamos, chimpancés de sabana, antílopes roanos y una avifauna notable, y núcleo de una Reserva de la Biosfera. Es el espacio protegido más grande de Guinea y también uno de los peor dotados: POR CONFIRMAR si hay guardas, pistas y campamento operativos. Se accede desde Kouroussa o desde Faranah.",
         credit="Maarten van der Bent · CC BY-SA 2.0", source=W + "Fouta%20Djallon%20(14604722652).jpg?width=900"),
    dict(n=19, name="Dabola y las cataratas del Tinkisso", cat="Naturaleza", prio="Media", dog="permitido con precaución", time="½ día",
         lat=10.7500, lon=-11.1167,
         desc="Dabola está en la bisagra entre la sabana de la Alta Guinea y el pie oriental del Fouta Djallon, y es la parada natural del corredor de subida entre Kouroussa y Tougué. A pocos kilómetros están las cataratas del Tinkisso, sobre el río del mismo nombre —el principal afluente de cabecera del Níger, que nace en el Fouta—: una cortina ancha y escalonada, con una pequeña central hidroeléctrica histórica que lleva décadas alimentando la ciudad, pozas para bañarse y un entorno de bosque de galería. Menos espectacular que las cascadas del Fouta central pero mucho más solitaria, y la única parada de agua del corredor de subida. Dabola tiene combustible y mercado.",
         credit="Sayd224 · CC BY 4.0", source=W + "Chute%20de%20Kinkon.jpg?width=900"),
    dict(n=20, name="Tougué y el Fouta oriental", cat="Naturaleza", prio="Media", dog="permitido", time="1 noche",
         lat=11.4333, lon=-11.6667,
         desc="La prefectura menos visitada del Fouta Djallon y la más difícil de alcanzar: el flanco oriental del altiplano, donde la meseta cae hacia la cuenca del Tinkisso en una sucesión de escarpes, gargantas y pueblos fulani prácticamente sin tráfico. La pista Dabola-Tougué-Labé es el tramo 4x4 más exigente y más solitario de todo el corredor guineano, y la razón principal para elegir este corredor de subida en vez de repetir el eje Mamou-Labé: cientos de kilómetros de paisaje de altiplano sin un solo viajero. Tougué tiene mercado, alojamiento elemental y combustible incierto —llegar con autonomía—. Es también una de las zonas de mayor concentración de «tapades», los huertos cercados de las casas fulani que son el sistema agrícola característico del Fouta. POR CONFIRMAR el estado de la pista y si es practicable fuera de la estación seca.",
         credit="Maarten van der Bent · CC BY-SA 2.0", source=W + "Fouta%20Djallon%20(14604722652).jpg?width=900"),
]

_CAT_COLOR = {
    "ciudad · servicios": "azul", "costa": "turquesa", "naturaleza · costa": "turquesa",
    "naturaleza · montaña": "verde", "naturaleza": "verde", "patrimonio": "marron",
    "patrimonio unesco": "marron", "cultura": "morado",
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
    ("Frontera · Entrada bajada — Sambaïlo / Koundara (desde Manda-Kalifourou, Senegal)", "Frontera", 12.5500, -13.3500,
     "El paso más fácil entre Senegal y Guinea y el que usa la práctica totalidad del tráfico: carretera asfaltada en buen estado a los dos lados, del puesto senegalés de Manda-Kalifourou al guineano de Sambaïlo, en la prefectura de Koundara. Evita por completo el territorio de Guinea-Bisáu, excluido por protocolo del proyecto. AVISOS: (1) el visado NO se expide en la frontera — hay que llegar con la eVisa o el visado consular ya emitido; (2) las fronteras de Guinea CIERRAN DE NOCHE: llegar con margen de varias horas de luz; (3) hay ~20 km de tierra de nadie entre los dos puestos; (4) se paga un laissez-passer de frontera del orden de 50.000 GNF que fija la duración de la estancia — comprobar que la fecha que escriben cubre todo el tramo previsto; (5) el ferry sobre el río Bantala, en la variante antigua, ha estado averiado con frecuencia: confirmar qué ruta está operativa. Es también la frontera de SALIDA de la subida."),
    ("Frontera · Salida bajada — N'Zo / Gbapleu (hacia Danané, Costa de Marfil)", "Frontera", 7.5500, -8.4500,
     "Paso principal entre la Guinea forestal y el oeste de Costa de Marfil, en la prefectura de Lola: del puesto guineano de N'Zo al marfileño de Gbapleu, y de ahí a Danané y Man. Reabierto en septiembre de 2016 tras el cierre sanitario por el ébola. Es la salida obligada de la bajada, porque LIBERIA ESTÁ EXCLUIDA de la ruta por la imposibilidad de obtener visado en frontera terrestre: de Guinea se va directo a Costa de Marfil. POR CONFIRMAR: horarios exactos, si sellan CPD y el estado del asfalto en el tramo Nzérékoré-Lola-N'Zo. Frontera cerrada de noche."),
    ("Frontera · Entrada subida — N'Zo / Gbapleu (desde Costa de Marfil)", "Frontera", 7.5500, -8.4500,
     "Mismo paso en sentido inverso. Aquí se abre el segundo visado guineano y el segundo permiso temporal del vehículo. Alternativa teórica más al norte (Sipilou / Kérouané-Beyla) que evitaría repetir el puesto, PERO está muy poco documentada y la carretera es incierta: POR CONFIRMAR antes de contar con ella. Salvo que se verifique, la entrada de la subida repite N'Zo y la diferenciación de corredores se consigue en el interior del país, no en la frontera."),
    ("Frontera · Variante de salida — Pamelap (hacia Sierra Leona)", "Frontera", 9.3000, -13.0500,
     "Paso costero Forécariah-Pamelap-Kambia, asfaltado de punta a punta, hacia Freetown. Solo se activa si se ejecuta la variante opcional de Sierra Leona en el tramo de subida que contempla la ruta global. No es la salida prevista por defecto."),
    ("Frontera · EXCLUIDA — todos los pasos con Guinea-Bisáu y con Malí", "Frontera", 12.0000, -13.8000,
     "Guinea-Bisáu queda excluida por protocolo del proyecto: ninguna variante debe rozar su territorio, ni siquiera como atajo. Malí queda excluido por conflicto: eso descarta el eje Siguiri-Kourémalé y toda la franja fronteriza del noreste (prefecturas de Siguiri y Mandiana), donde además hay presión de grupos armados del Sahel. El corredor de subida por la Alta Guinea se mantiene deliberadamente al sur y al oeste de esa franja."),
    ("Embajada de España en Conakry", "Consular", 9.5300, -13.6800,
     "Place Almamy Samory Touré, Bâtiment R2000, 6º piso, Moussoudougou, Coléah. Cancillería +224 664 20 22 01 · Sección consular +224 613 33 90 90 · Emergencia consular grave +224 664 33 54 93. Coordenada urbana aproximada."),
    ("Embajada de Costa de Marfil en Conakry", "Consular", 9.5350, -13.6750,
     "Punto crítico del itinerario: es donde se tramita el visado marfileño para la salida de la bajada. Confirmar dirección, horarios y requisitos por teléfono nada más llegar a Conakry, con margen de varios días. Coordenada urbana aproximada — POR CONFIRMAR."),
    ("Hôpital National Donka — Conakry", "Hospital", 9.5350, -13.6950,
     "Principal hospital de referencia del país; capacidad limitada para politraumatismos. El seguro con evacuación aérea es imprescindible en todo el país: la evacuación realista desde Guinea es a Dakar o a Europa. Coordenada urbana aproximada."),
    ("Hôpital Régional de Labé", "Hospital", 11.3167, -12.2833,
     "Recurso sanitario de referencia de todo el Fouta Djallon y del corredor norte. Para casos graves, evacuación a Conakry o a Dakar. Coordenada urbana aproximada."),
    ("Laboratoire Régional Vétérinaire de Labé", "Servicio", 11.3167, -12.2833,
     "Uno de los pocos servicios veterinarios oficiales del interior de Guinea, dependiente de la Direction Nationale des Services Vétérinaires (DNSV). Es el recurso más cercano si hay que resolver algo con el perro —un certificado, una vacuna, un problema sanitario— fuera de Conakry, y está justo en el nudo de los dos corredores. Coordenada urbana aproximada: localizar en Labé al llegar."),
    ("Hôpital Régional de Nzérékoré", "Hospital", 7.7561, -8.8179,
     "Única referencia hospitalaria seria de toda la Guinea forestal y del sureste. Entre Kankan y Nzérékoré no hay nada equivalente."),
    ("Hôpital Régional de Kankan", "Hospital", 10.3853, -9.3057,
     "Referencia hospitalaria del corredor de subida por la Alta Guinea."),
    ("Combustible · Conakry", "Combustible", 9.5092, -13.7122,
     "Mejor oferta y calidad del país (Total, Vivo/Shell, Petroguinée). Repostar a fondo aquí antes de cualquier tramo interior."),
    ("Combustible · Labé, Pita, Mamou, Dalaba, Kindia", "Combustible", 11.3167, -12.2833,
     "Estaciones formales en todas las ciudades del eje Labé-Mamou-Kindia-Conakry: es el corredor con mejor cobertura del país. Repostar en Labé antes de subir a Mali/Loura o de bajar a Doucki."),
    ("Combustible · Faranah, Kissidougou, Macenta, Nzérékoré", "Combustible", 7.7561, -8.8179,
     "Estaciones formales en las capitales del eje sureste, pero con roturas de suministro puntuales. Autonomía recomendada Mamou → Nzérékoré (~650 km) con garrafas, y no depender de Macenta."),
    ("Combustible · Kankan, Kouroussa, Dabola (escaso a partir de Tougué)", "Combustible", 10.3853, -9.3057,
     "Kankan y Dabola tienen estaciones formales. AVISO: a partir de Dabola, la pista Tougué-Labé del corredor de subida no tiene garantía de combustible — salir de Dabola con depósitos y garrafas llenos (~350 km hasta Labé, pero con consumo de pista)."),
    ("Agua potable y de uso general · Conakry, Labé, Kankan, Nzérékoré", "Agua potable", 9.5092, -13.7122,
     "Agua embotellada y en bolsa disponible en todas las ciudades. Para el depósito de uso general: estaciones de servicio, hoteles y misiones católicas suelen permitir llenar con manguera. En el Fouta el agua de manantial es abundante pero hay que tratarla igualmente."),
    ("Agua · Fouta Djallon (el castillo de agua de África occidental)", "Agua potable", 11.0833, -12.4000,
     "Paradoja útil: es la región con más agua de África occidental —de aquí nacen el Níger, el Senegal y el Gambia— y a la vez una donde el agua de superficie no es potable sin tratar. Manantiales y arroyos constantes en todo el altiplano: filtro mecánico más tratamiento químico o ebullición, siempre. En los campamentos de Doucki y Kambadaga el agua es de pozo o manantial."),
]

DRONE_CALLOUT = ("warn", "Sin procedimiento turístico publicado: tratar como restringido y no volar sin autorización escrita",
                  "No se ha localizado un procedimiento público de autorización de drones para visitantes en Guinea. La autoridad competente es la Agence Nationale de l'Aviation Civile (ANAC-Guinée), con el Ministerio de Transportes por encima, pero no publica un régimen turístico. En un país que ha vivido un golpe de Estado en 2021 y sigue en transición política, con presencia militar visible y sensibilidad alta ante cualquier forma de vigilancia, el criterio del proyecto es NO volar sin autorización previa y por escrito. En ningún caso volar sobre Conakry (aeropuerto, puerto, Camp Samory Touré, edificios de gobierno), sobre las instalaciones mineras de bauxita de Boké y Kamsar —que son zonas industriales con seguridad privada— ni sobre las centrales hidroeléctricas de Kinkon, Garafiri o Tinkisso. En el Fouta Djallon rural, lejos de todo, el riesgo práctico es menor, pero sigue sin haber cobertura legal.")

STARLINK_CALLOUT = ("warn", "Sin confirmación de disponibilidad activa: no planificarlo como comunicación primaria",
                     "Guinea no ha aparecido de forma consistente como mercado activo de Starlink en las fuentes consultadas a fecha de esta revisión, y no se ha localizado una licencia pública de la Autorité de Régulation des Postes et Télécommunications (ARPT) guineana. Revisar el mapa oficial de Starlink 30-60 días antes de entrar y, mientras tanto, planificar con SIM local. Cobertura móvil (Orange Guinée, MTN Guinée) aceptable en Conakry, Kindia, Mamou, Labé, Kankan y Nzérékoré, y muy degradada o nula en Doucki, Tougué, Mali/Loura, el bosque de Ziama y el acceso al Nimba: dar por hecho 2-3 días incomunicados en cada uno de esos bloques y avisar en casa antes de entrar.")

DOG_MATRIX = [
    ("Entrada en el país (frontera de Sambaïlo y de N'Zo)", "permitido con condiciones",
     "Documentación: microchip, pasaporte europeo de animal de compañía, vacuna antirrábica en vigor con MENOS DE 12 MESES, y certificado veterinario internacional expedido dentro de las 72 h previas a la llegada. Base legal: la Ley L/2018/026/AN (Código de Ganadería y Productos Animales) somete todo animal vivo presentado a la importación a control sanitario veterinario ANTES del despacho de aduana, y exige certificado sanitario y certificado de vacunación en todo paso de frontera. La ventana de 72 h es el problema operativo real: hay que conseguir el certificado en Tambacounda o Kédougou (Senegal) en la víspera del cruce, y lo mismo en Man o Danané (Costa de Marfil) para la entrada de la subida. Ver la sección del perro para el detalle y los pendientes."),
    ("Fouta Djallon: Labé, Mali/Loura, Pita, Doucki, Dalaba, cascadas", "permitido",
     "Es LA mejor región del viaje para el perro entre Marruecos y Camerún: terreno comunitario, no parque nacional; clima fresco (1.000-1.500 m, se duerme con manta); agua constante; y senderos largos por meseta abierta. Correa en los bordes de cañón y en la roca mojada de Kinkon, Kambadaga y Ditinn, que son caídas verticales sin protección. En Doucki, confirmar con Hassan Bah qué rutas admiten perro: las fáciles sí, las de grietas y cuerdas no. Cuidado con los perros de los pastores fulani y con el ganado en las tapades."),
    ("Kindia (Voile de la Mariée) y monte Gangan", "permitido con precaución",
     "Área recreativa con bungalows y pozas, fuera de espacio protegido. Correa en la zona de la cascada por el gentío de fin de semana y por la roca mojada."),
    ("Conakry, Kankan, Nzérékoré, Kindia (ciudades)", "permitido con condiciones",
     "Sin restricción legal identificada. Correa siempre puesta: mucho perro callejero, tráfico denso y calor húmedo intenso en Conakry y Nzérékoré. Confirmar por teléfono la política del hotel antes de llegar; los alojamientos con patio del interior suelen no poner problema. Nunca dejarlo solo en el vehículo."),
    ("Islas de Los (trayecto en lancha desde Conakry)", "no confirmado",
     "No es una norma sino una decisión del patrón de la lancha. PLAN B: contratar una piragua entera en vez de plaza en la lancha colectiva, o dejar al perro en el alojamiento de Conakry y hacer la excursión por turnos entre los tres viajeros."),
    ("Montes Nimba (UNESCO) y bosque de Ziama", "no confirmado — tratar como prohibido",
     "El Nimba es Reserva Natural INTEGRAL (la categoría más restrictiva) con chimpancés y endemismos extremos, y Ziama es Reserva de la Biosfera con chimpancés y elefante de bosque: el riesgo de transmisión de enfermedades a grandes simios hace que la prohibición sea la práctica universal en este tipo de espacios, aunque no haya norma publicada. PLAN B: turnos entre los tres viajeros —uno se queda con el perro en Nzérékoré o en Macenta—. Confirmar por escrito con el CEGENS (Nimba) y con el Centre Forestier de Nzérékoré (Ziama)."),
    ("Parques Nacionales del Badiar y del Alto Níger", "no confirmado — tratar como prohibido",
     "Sin norma publicada y con gestión débil, lo que en la práctica significa que la respuesta dependerá del guarda que esté ese día. Planificar como prohibido y, si se autoriza sobre el terreno, valorarlo con criterio propio: hay hipopótamos y babuinos, que son un riesgo real para un perro."),
    ("Frontera de Guinea-Bisáu y franja fronteriza con Malí", "zona excluida",
     "Excluidas del itinerario por protocolo y por conflicto, no por el perro. No aplica."),
]

SOURCES = [
    ("Anivetvoyage · formalidades veterinarias de entrada en Guinea (microchip, rabia <12 meses, certificado internacional en 72 h)", "https://www.anivetvoyage.com/formalites-pays/g/301-guinee.html"),
    ("USDA APHIS · Pet Travel from the United States to Guinea (certificado sanitario internacional; no consta restricción de puerto de entrada)", "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-united-states-guinea"),
    ("Asamblea Nacional de Guinea · Ley L/2018/026/AN, Código de Ganadería y Productos Animales (arts. 21, 41 y 117: control veterinario previo al despacho aduanero y certificados en frontera)", "https://cnt.gov.gn/archive.assemblee/www.assemblee.gov.gn/conakry-le-03-juillet-2018-l2018026an-loi-portant-code-de-lelevage-et-des-produits-animaux.html"),
    ("Ministère de l'Agriculture et de l'Élevage de Guinée · Direction Nationale des Services Vétérinaires (DNSV)", "https://www.agriculture.gov.gn/reunion-avec-les-equipes-de-la-direction-nationale-des-services-veterinaires-dnsv-bonne-lecture/"),
    ("MAGEL · catálogo de servicios ofrecidos al ciudadano (incluye la DNSV)", "https://magel.gov.gn/wp-content/uploads/2023/02/Identification-des-services-offert-par-le-MAGEL-aux-citoyens.pdf"),
    ("Wikipedia (fr) · Laboratoire régional vétérinaire de Labé", "https://fr.wikipedia.org/wiki/Laboratoire_r%C3%A9gional_v%C3%A9t%C3%A9rinaire_de_Lab%C3%A9"),
    ("Fouta Découverte · entrar en Guinea: todos los pasos fronterizos terrestres, documentación y laissez-passer", "https://www.foutadecouverte.com/2017/01/pour-entrer-en-guinee-infos-aux-frontieres.html"),
    ("Fouta Découverte · primeros días en Guinea llegando desde Senegal por la N5", "https://www.foutadecouverte.com/2024/10/premiers-jours-en-guinee-9.html"),
    ("Matt's Next Steps · guía completa de senderismo en Doucki (rutas, precios, Hassan Bah, temporada)", "https://mattsnextsteps.com/hiking-in-fouta-djallon-complete-guide-to-doucki/"),
    ("The Candy Trail · Doucki, el Gran Cañón de Guinea", "https://www.thecandytrail.com/doucki-fouta-djallon-guinea/"),
    ("The Road Chose Me (Dan Grec) · senderismo en Doucki, Fouta Djallon", "https://theroadchoseme.com/hiking-in-doucki-the-fouta-djallon-1"),
    ("Hiking in Guinea · quién es Hassan Bah (Doucki)", "https://hikinginguinea.wordpress.com/about/"),
    ("Kumakonda · senderismo en el Fouta Djallon", "https://kumakonda.com/fouta-djallon/"),
    ("Scoot West Africa · guía completa del Fouta Djallon", "https://scootwestafrica.com/guide-fouta-djallon-guinea/"),
    ("Exploring Wild · dónde hacer senderismo en África occidental", "https://exploringwild.com/west-africa-hiking/"),
    ("UNESCO · Mount Nimba Strict Nature Reserve (Patrimonio Mundial en Peligro)", "https://whc.unesco.org/en/list/155/"),
    ("Wikipedia · Fouta Djallon (geografía, monte Loura, ríos que nacen aquí)", "https://en.wikipedia.org/wiki/Fouta_Djallon"),
    ("Wikipedia · Kindia (coordenadas, Voile de la Mariée, monte Gangan)", "https://en.wikipedia.org/wiki/Kindia"),
    ("Wikipedia · Nzérékoré (Guinea forestal, accesos)", "https://en.wikipedia.org/wiki/Nzerekore"),
    ("Digital Logistics Capacity Assessment · paso fronterizo de Sambaïlo", "https://lca.logcluster.org/235-guinea-border-crossing-sambailo"),
    ("PAF Guinée · información oficial de visado", "https://www.paf.gov.gn/dnpaf/?page_id=335&lang=en"),
    ("Visamundi · e-Visa de Guinea Conakry", "https://www.visamundi.co/en/destinations/guinea/"),
    ("Travel.State.gov · Guinea travel advisory (referencia internacional)", "https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Guinea.html"),
    ("Embajada de España en Guinea · horario, localización y contacto", "https://www.exteriores.gob.es/Embajadas/conakry/es/Embajada/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx"),
    ("Starlink · mapa oficial de disponibilidad", "https://starlink.com/map"),
    ("Comisión Europea · animales de compañía (requisitos de reentrada en la UE)", "https://europa.eu/youreurope/citizens/travel/carry/pets-and-other-animals/index_es.htm"),
    ("iOverlander · puntos de combustible, agua y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Bajada: Koundara -> Labé -> Mali/Loura -> Labé -> Pita/Kinkon -> Kambadaga -> Doucki -> Dalaba -> Ditinn -> Mamou -> Kindia -> Conakry -> Mamou -> Faranah -> Kissidougou -> Macenta/Ziama -> Nzérékoré -> Lola/Nimba -> N'Zo
CORRIDOR = [
    (12.5500, -13.3500),  # Sambaïlo (entrada desde Senegal)
    (12.4833, -13.3000),  # Koundara
    (11.3167, -12.2833),  # Labé
    (12.0833, -12.3000),  # Mali / monte Loura
    (11.3167, -12.2833),  # Labé (vuelta)
    (11.0833, -12.4000),  # Pita
    (10.9833, -12.4000),  # Chutes de Kinkon
    (11.0167, -12.5167),  # Chutes de Kambadaga
    (11.1500, -12.6000),  # Doucki
    (10.6833, -12.2500),  # Dalaba
    (10.7500, -12.1667),  # Chutes de Ditinn
    (10.3833, -12.0833),  # Mamou
    (10.0500, -12.8542),  # Kindia
    (9.5092, -13.7122),   # Conakry
    (10.3833, -12.0833),  # Mamou (vuelta al interior)
    (10.0333, -10.7500),  # Faranah
    (9.1833, -10.1000),   # Kissidougou
    (8.5500, -9.4667),    # Macenta / Ziama
    (7.7561, -8.8179),    # Nzérékoré
    (7.8000, -8.5333),    # Lola
    (7.6032, -8.3910),    # Montes Nimba
    (7.5500, -8.4500),    # N'Zo (salida a Costa de Marfil)
]

# Subida: N'Zo -> Lola -> Nzérékoré -> Beyla -> Kankan -> Kouroussa -> Dabola -> Tougué -> Labé -> Koundara -> Sambaïlo
CORRIDOR_ALT = [
    (7.5500, -8.4500),    # N'Zo (entrada desde Costa de Marfil)
    (7.8000, -8.5333),    # Lola
    (7.7561, -8.8179),    # Nzérékoré
    (8.6833, -8.6500),    # Beyla
    (10.3853, -9.3057),   # Kankan
    (10.6500, -9.8833),   # Kouroussa
    (10.7500, -11.1167),  # Dabola / Tinkisso
    (11.4333, -11.6667),  # Tougué
    (11.3167, -12.2833),  # Labé
    (12.4833, -13.3000),  # Koundara
    (12.5500, -13.3500),  # Sambaïlo (salida a Senegal)
]

CORRIDOR_LABEL = "Bajada"
CORRIDOR_ALT_LABEL = "Subida"

EXPERIENCIAS = [
    "Doucki es el sitio que todo el mundo recuerda. Es, con diferencia, el lugar de Guinea del que más han escrito los viajeros independientes, y todos coinciden: tres noches como mínimo, porque con una te quedas en la puerta. Hassan Bah, el guía y anfitrión del pueblo —ya sesentón cuando lo visitaron los autores de las guías más recientes—, lleva décadas abriendo rutas por el borde del altiplano y bautizándolas con nombres que son ya parte del folclore mochilero de África occidental: «Indiana Jones World», «Bob Marley Stage», «Hyena's Rock», «Vultures Rock», «Chutes & Ladders». La fórmula es todo incluido por unos 50 USD al día (cama, tres comidas, guía, sin tasas de entrada) y la descripción de las tardes en el porche viendo la puesta de sol con los otros viajeros se repite en casi todos los relatos.",
    "El acceso a Doucki es parte de la experiencia: 2-3 horas desde Pita por pista con baches, que en taxi-brousse se hace pagando plazas de más. Para nosotros, con vehículo propio, es una ventaja evidente — y también significa que podemos llevar los dos coches hasta el pueblo en vez de depender de transporte.",
    "El Fouta Djallon es el mejor senderismo de África occidental, y los propios viajeros que han recorrido toda la región lo dicen sin matices. No hay infraestructura, no hay señalización, no hay tasas y no hay nadie: hay un altiplano de arenisca de 1.000-1.500 m partido por cañones, con cascadas de 70-80 m y pueblos fulani. La mayoría de las guías de senderismo de África occidental que existen dedican a Guinea más espacio que a cualquier otro país de la costa atlántica.",
    "El caudal de las cascadas lo cambia todo, y hay una trampa: las chutes de Kinkon dependen de una presa hidroeléctrica aguas arriba, así que el caudal no es una cuestión de estación sino de lo que decida la central ese día. Preguntar en Pita antes de conducir hasta allí. Kambadaga y Ditinn sí son estacionales: espectaculares de julio a noviembre, hilo de agua al final de la seca.",
    "La mejor época para el Fouta según quienes lo han caminado: febrero-marzo. Seca, fresca, pistas practicables y cielos limpios. La estación húmeda da cascadas llenas y paisaje verde, pero con pistas que se convierten en barro y accesos que se cortan. Es el conflicto de calendario clásico de este país.",
    "Entrar por Sambaïlo/Koundara desde Senegal es el cruce fácil: los relatos coinciden en que es el mejor paso de los seis vecinos de Guinea, con asfalto bueno a los dos lados (Manda-Kalifourou en Senegal, Sambaïlo en Guinea). Las alternativas del este senegalés son pistas malas. Dos avisos recogidos por los viajeros francófonos que mejor conocen la zona: el visado NO se da en frontera, y las fronteras de Guinea cierran de noche.",
    "El laissez-passer de frontera (unos 50.000 GNF) fija por escrito cuántos días puedes estar: es un documento distinto del visado y lo emite el puesto. Los viajeros con vehículo recomiendan comprobar la fecha que escriben antes de irse, porque corregirla después es un problema.",
    "Documentación del vehículo que piden en la frontera guineana, según los relatos: carnet de paso en aduana (CPD) o carnet ATA, permiso internacional de conducir, seguro válido CEDEAO, certificado de vacunación y el laissez-passer. Recomiendan además llevar extintor, botiquín y triángulos, que se comprueban.",
    "La frontera con Costa de Marfil (Danané-Gbapleu / N'Zo-Lola) reabrió en septiembre de 2016 tras haber estado cerrada por el ébola. Es el paso que usa el tráfico entre la Guinea forestal y el oeste marfileño, pero está mucho peor documentado que el de Senegal: conviene contactar con overlanders recientes antes de comprometer el calendario.",
    "Guinea es un país con muy poca información pública en comparación con sus vecinos, y eso se nota también en el perro: no existe un solo relato localizado de un viajero que haya cruzado la frontera guineana con un animal de compañía. Lo que sí hemos podido cerrar es el marco legal y los requisitos veterinarios (ver la sección del perro), pero la práctica de ventanilla en Sambaïlo y en N'Zo sigue sin testimonio. Si alguien de la comunidad overland lo ha hecho, es el dato más valioso que podemos conseguir antes de salir.",
]

HISTORIA_RESUMEN = ("Guinea (Guinea-Conakry) fue la primera colonia francesa en África en optar por la independencia inmediata en 1958, rechazando en referéndum la propuesta de comunidad francesa de De Gaulle, un gesto de dignidad que le costó una ruptura brutal con Francia "
                     "y décadas de dictaduras (Sékou Touré, luego Lansana Conté) sostenidas sobre una de las mayores reservas de bauxita del planeta, con una frágil transición democrática interrumpida por sucesivos golpes de Estado, el último en 2021.")

HISTORIA_SECCIONES = [
    ("Imperios y reinos previos a la colonización",
     "El territorio formó parte de la periferia del imperio de Malí y albergó posteriormente el imperio fulani del Futa Jalón (siglo XVIII), una teocracia islámica en las tierras altas centrales que dejó una fuerte impronta religiosa y política en la Guinea actual, con una organización en provincias (diwe) y una tradición de erudición islámica en lengua pular que todavía estructura la sociedad del altiplano."),
    ("Colonización francesa y resistencia armada",
     "Francia encontró una resistencia prolongada a la conquista, encabezada por el almamy Samory Touré, cuyo imperio Wassulu resistió durante casi dos décadas antes de su derrota en 1898; Guinea fue integrada después en el África Occidental Francesa como colonia de plantación y extracción minera, con el ferrocarril de Conakry a Kankan como eje de penetración y ciudades como Kindia y Dalaba creadas o transformadas por la administración colonial."),
    ("El «no» de 1958 y la era de Sékou Touré",
     "En el referéndum de 1958 sobre la comunidad francesa propuesta por De Gaulle, Guinea fue la única colonia en votar «no», bajo el liderazgo de Ahmed Sékou Touré —nieto de Samory— con la célebre frase «preferimos la pobreza en libertad a la riqueza en la esclavitud»; Francia respondió retirando abruptamente personal y equipamiento, y Sékou Touré gobernó hasta su muerte en 1984 con un régimen de partido único marcado por la represión política y el campo de Boiro, pero también por un extraordinario mecenazgo musical: las orquestas nacionales (Bembeya Jazz, Balla et ses Balladins, Les Amazones) que hicieron de Conakry una capital sonora de África."),
    ("Situación actual: recursos minerales y fragilidad democrática",
     "Tras la muerte de Sékou Touré, el país vivió otra larga dictadura militar bajo Lansana Conté (1984-2008) y sucesivos golpes de Estado, el más reciente en septiembre de 2021, cuando el coronel Mamadi Doumbouya derrocó al presidente Alpha Condé e instauró el CNRD con una transición cuyo calendario se ha ido prorrogando. Guinea alberga algunas de las mayores reservas mundiales de bauxita y de mineral de hierro (el megaproyecto de Simandou, en el sureste, es el mayor yacimiento de hierro sin explotar del mundo), una riqueza mineral que convive con niveles de pobreza muy elevados. El estado exacto de la transición política en 2027 es un dato a revalidar antes del viaje."),
]

HISTORIA_FUENTES = [
    ("BBC News · Guinea country profile", "https://www.bbc.com/news/world-africa-13442051"),
    ("Encyclopaedia Britannica · Guinea, History", "https://www.britannica.com/place/Guinea/History"),
    ("Reuters · cobertura de la transición política en Guinea", "https://www.reuters.com/world/africa/"),
]

SPEC = dict(
    slug="guinea", name="Guinea", revision="12 sep 2026",
    sub="Corredor doble bajada/subida · el mejor senderismo de África occidental · documentación · logística",
    chips=[
        ("BAJADA", "Sambaïlo/Koundara → Labé → Loura → Pita → Doucki → Dalaba → Kindia → Conakry → Faranah → Nzérékoré → Nimba → N'Zo · ~1.900 km"),
        ("SUBIDA", "N'Zo → Nzérékoré → Beyla → Kankan → Kouroussa → Dabola → Tougué → Labé → Koundara · ~1.250 km"),
        ("PDIs", "20 puntos repartidos entre los dos corredores; solo Labé y el eje Nzérékoré-Lola se repiten"),
        ("A PIE", "Doucki, el «Gran Cañón de Guinea»: 10 rutas con nombre propio · monte Loura 1.515 m · Gangan · Nimba"),
        ("4x4", "pista Dabola-Tougué-Labé (Fouta oriental) · accesos a Kambadaga, Doucki y Ditinn · carretera Labé-Mali"),
        ("AGUA", "castillo de agua de África occidental: aquí nacen el Níger, el Senegal y el Gambia"),
        ("VISADO", "eVisa previa OBLIGATORIA — no se expide en frontera. Fronteras cerradas de noche"),
        ("PERRO", "agujero negro parcialmente CERRADO: marco legal y requisitos identificados (ver ficha)"),
        ("SALUD", "fiebre amarilla obligatoria · historial de ébola y Marburgo en la Guinea forestal"),
        ("EXCLUIDO", "Guinea-Bisáu (protocolo) y la franja fronteriza con Malí (conflicto)"),
    ],
    center=[10.2, -11.3], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y de nuevo 72 h antes de cada frontera. La frontera con Guinea-Bisáu queda excluida sin excepción por protocolo del proyecto, y la franja fronteriza con Malí por conflicto.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Guinea es, junto con Angola, el país más infravalorado de toda la ruta: espectacular, casi sin turismo y con el <strong>mejor senderismo de África occidental</strong>. "
                   "Se cruza <strong>dos veces</strong>, y las dos veces de punta a punta, porque la geografía obliga: se entra por el noroeste (Senegal) y se sale por el sureste (Costa de Marfil), con 1.000 km de diagonal por medio. "
                   "En la <strong>bajada</strong> se recorre el corazón del país: el <strong>Fouta Djallon</strong> —el altiplano de arenisca de donde nacen el Níger, el Senegal y el Gambia, con sus cañones, sus cascadas de 80 m y el pueblo de Doucki— y después Conakry y la travesía al sureste por Faranah (nacimiento del Níger), el bosque de Ziama y los montes Nimba. "
                   "En la <strong>subida</strong> se vuelve por la <strong>Alta Guinea</strong>, un mundo completamente distinto —sabana malinké, el Níger ya navegable en Kouroussa, Kankan— y se remonta al Fouta por su flanco oriental, la pista solitaria de Dabola-Tougué-Labé. "
                   "Los dos corredores solo comparten Labé y el tramo forzoso de Nzérékoré-Lola. "
                   "Recordatorio de ruta: <strong>Liberia está excluida</strong> por la imposibilidad de obtener visado en frontera terrestre, así que de Guinea se pasa directamente a Costa de Marfil."),
    decision=("<strong>Por qué dos travesías completas y no un atajo.</strong> Guinea no se puede cruzar en línea recta: la entrada obligada desde Senegal está en el extremo noroeste (Koundara) y la salida obligada hacia Costa de Marfil está en el extremo sureste (Lola), a más de 1.000 km. "
              "Eso convierte a Guinea, pese a su tamaño modesto, en uno de los países con más kilómetros interiores de toda la ruta atlántica — y en uno de los que más merece esos kilómetros. "
              "<strong>La diferenciación de los corredores se consigue en el interior, no en las fronteras:</strong> las dos entradas y las dos salidas son forzosamente las mismas (Sambaïlo y N'Zo), porque no hay alternativas verificadas —el paso de Sipilou desde Costa de Marfil está sin documentar, los de Guinea-Bisáu están excluidos por protocolo y los de Malí por conflicto—. "
              "Lo que sí cambia radicalmente es lo que hay entre medias: la bajada va por el <strong>eje central y occidental</strong> (Fouta Djallon, Conakry, Faranah, Kissidougou, Macenta) y la subida por el <strong>eje oriental</strong> (Beyla, Kankan, Kouroussa, Dabola, Tougué), que es sabana malinké en vez de altiplano fulani y selva. "
              "<strong>Decisión abierta para el dueño del proyecto:</strong> el corredor de subida por Tougué es el más bonito y el más solitario, pero también el peor documentado y el que tiene menos garantía de combustible. La alternativa conservadora es subir por Dabola-Mamou-Labé, por asfalto, renunciando a Tougué. Conviene decidirlo con información de pista fresca, no de antemano. "
              "<strong>Segunda decisión abierta:</strong> el calendario. El Fouta quiere febrero-marzo (seco, fresco, pistas practicables) y las cascadas quieren julio-noviembre (caudal). Con dos pasadas se puede cubrir las dos cosas, pero hay que decidir cuál va en cada una."),
    facts=[
        ("Ventana prevista", "Bajada: tras Senegal, antes de Costa de Marfil. Subida: desde Costa de Marfil hacia Senegal, en el tramo de regreso."),
        ("Entrada bajada", "Sambaïlo/Koundara desde Manda-Kalifourou (Senegal): el paso más fácil de los seis vecinos, asfaltado a ambos lados. Evita por completo Guinea-Bisáu."),
        ("Salida bajada", "N'Zo/Gbapleu hacia Danané (Costa de Marfil), desde Lola. Liberia queda excluida de la ruta: de Guinea se va directo a Costa de Marfil."),
        ("Entrada y salida de la subida", "Las mismas: N'Zo y Sambaïlo. La diferenciación se consigue en el interior, con el corredor de la Alta Guinea."),
        ("Visado", "eVisa previa OBLIGATORIA para pasaporte español (~90 días, entrada única, ~129 €, 72 h de trámite). NO se expide visado en frontera terrestre. Como el país se cruza dos veces, hacen falta DOS visados o uno de entrada múltiple: confirmar si existe."),
        ("Fronteras", "Las fronteras de Guinea CIERRAN DE NOCHE. Llegar con varias horas de luz por delante. Se paga un laissez-passer de frontera (~50.000 GNF) que fija por escrito la duración de la estancia."),
        ("Perro", "Agujero negro PARCIALMENTE CERRADO en esta revisión: marco legal identificado (Ley L/2018/026/AN), autoridad identificada (DNSV, Ministerio de Agricultura y Ganadería) y requisitos prácticos localizados. Lo que sigue abierto es la práctica de ventanilla en frontera terrestre. Ver la sección del perro."),
        ("Seguridad", "Sin conflicto activo en el itinerario. Situación política en transición tras el golpe de 2021 — revalidar. Excluidas: la frontera de Guinea-Bisáu (protocolo) y la franja fronteriza con Malí (prefecturas de Siguiri y Mandiana)."),
        ("Salud", "Fiebre amarilla obligatoria sin excepción. La Guinea forestal (Guéckédou, Macenta, Nzérékoré) fue el origen de la epidemia de ébola de 2013-2016 y tuvo brotes posteriores de ébola y de Marburgo: comprobar el estado epidemiológico antes de entrar."),
        ("Combustible", "Buena cobertura en el eje Conakry-Mamou-Labé y en las capitales regionales. Tramos comprometidos: Mamou→Nzérékoré (~650 km con roturas de suministro) y Dabola→Labé por Tougué (~350 km de pista sin garantía)."),
        ("Comunicaciones", "Starlink SIN CONFIRMAR como mercado activo. SIM local (Orange Guinée, MTN) como base; sin cobertura en Doucki, Tougué, Loura, Ziama y el acceso al Nimba."),
        ("Dinero", "Franco guineano (GNF). Retirada en cajero muy limitada (~40 € por operación): llevar euros en efectivo como respaldo y cambiar en Conakry o Labé."),
    ],
    alerts=[
        "Visado: la eVisa es OBLIGATORIA y previa — no hay visado en frontera terrestre en Guinea, sin excepción. Tramitarla con 10 días de margen sobre las 72 h nominales. Y como el país se cruza dos veces con meses de diferencia, hay que resolver el segundo visado: confirmar si existe la entrada múltiple o si hay que tramitar el segundo desde Costa de Marfil (embajada de Guinea en Abiyán).",
        "Fronteras cerradas de noche: es una norma real y afecta a la planificación de las dos jornadas de cruce. Llegar a Sambaïlo o a N'Zo con varias horas de luz por delante; si no se llega, hay que pernoctar en el lado de origen.",
        "Frontera de Guinea-Bisáu: exclusión total por protocolo del proyecto — ninguna variante de ruta debe rozar su territorio, ni siquiera como atajo de emergencia. Esto afecta a la variante costera de Boké, que se puede recorrer pero no prolongar hacia el norte.",
        "Franja fronteriza con Malí EXCLUIDA: las prefecturas de Siguiri y Mandiana y el eje Kankan-Kourémalé quedan fuera del itinerario por la inestabilidad del Sahel maliense y la presión de grupos armados. El corredor de subida por la Alta Guinea se mantiene deliberadamente al sur y al oeste de esa franja.",
        "Liberia excluida de la ruta: por la imposibilidad de obtener visado en frontera terrestre. Eso significa que de Guinea se pasa DIRECTAMENTE a Costa de Marfil por N'Zo/Gbapleu, y que no hay una salida alternativa por el sur si ese paso falla. Es el punto único de fallo del corredor de bajada.",
        "Certificado de fiebre amarilla obligatorio sin excepción para entrar en Guinea: llevarlo siempre encima junto al pasaporte, no en el fondo de una mochila.",
        "Salud — Guinea forestal: la prefectura de Guéckédou fue el foco de origen de la epidemia de ébola de África occidental de 2013-2016, y la región tuvo un rebrote en 2021 además del primer caso de virus de Marburgo de África occidental. El corredor de bajada atraviesa esta región (Macenta, Nzérékoré). No es motivo para evitarla, pero sí para comprobar el estado epidemiológico con el ECDC y la OMS antes de entrar y para extremar la higiene.",
        "Retirada de efectivo muy limitada (~40 € por operación en cajeros) y cobertura de cajeros restringida a Conakry, Labé, Kankan y poco más: llevar euros en efectivo como respaldo real, no como reserva simbólica.",
        "Situación política en transición tras el golpe de Estado de septiembre de 2021: el calendario de vuelta al orden constitucional se ha ido prorrogando y las manifestaciones en Conakry pueden derivar en cortes de carretera y en represión. Revalidar el estado del país 30-60 días antes y evitar concentraciones. Estado exacto en 2027: POR CONFIRMAR.",
        "Drones: sin procedimiento turístico publicado y con un contexto político sensible. El criterio del proyecto es no volar sin autorización escrita de la ANAC-Guinée.",
        "Caudal de las cascadas: las chutes de Kinkon dependen de la presa hidroeléctrica aguas arriba y pueden estar secas cualquier día del año por decisión de la central. Preguntar en Pita antes de conducir hasta allí.",
    ],
    ruta_intro=("Guinea se recorre dos veces de punta a punta, por rutas interiores casi completamente distintas. La <strong>bajada</strong> (~1.900 km) es la travesía diagonal completa: entra por el noroeste, "
                "sube al Fouta Djallon y se queda allí varios días —Labé, el monte Loura, Pita y sus dos cascadas, Doucki, Dalaba, Ditinn—, baja a Kindia y Conakry, y vuelve al interior para atravesar el país hasta "
                "la Guinea forestal (Faranah, Kissidougou, Macenta, Nzérékoré) y salir a Costa de Marfil por el Nimba. La <strong>subida</strong> (~1.250 km) hace la diagonal inversa pero por el <strong>este</strong>: "
                "Beyla, Kankan, Kouroussa, Dabola y la pista solitaria de Tougué, que remonta el Fouta por su flanco oriental hasta Labé. Etapas calculadas sobre <strong>250 km/día</strong>, reducidos a 120-150 km/día "
                "en las pistas del Fouta y en el tramo de Tougué."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bajada 1 · Entrada", "Sambaïlo/Koundara → (Badiar) → Labé", "~180 km · 1-2 días (la frontera se come medio día)"),
        ("Bajada 2 · El techo del Fouta", "Labé → Mali / monte Loura (1.515 m) → Labé", "~240 km ida y vuelta · 2 días con la subida a pie"),
        ("Bajada 3 · Las cascadas de Pita", "Labé → Pita → Kinkon → Kambadaga", "~120 km · 2 días"),
        ("Bajada 4 · El Gran Cañón", "Pita → Doucki (senderismo con Hassan Bah)", "~60 km · 3-4 días — el bloque clave del país"),
        ("Bajada 5 · Estación de altura", "Doucki → Pita → Dalaba → Ditinn → Dalaba", "~180 km · 2 días"),
        ("Bajada 6 · Bajada a la costa", "Dalaba → Mamou → Kindia (Voile de la Mariée, Gangan)", "~250 km · 2 días"),
        ("Bajada 7 · Capital y mar", "Kindia → Conakry → Islas de Los", "~135 km + lancha · 2-3 días (visados, taller, descanso)"),
        ("Bajada 8 · Variante costera (opcional)", "Conakry → Boffa → Boké → Conakry", "~600 km ida y vuelta · 2 días — OPCIONAL"),
        ("Bajada 9 · Al nacimiento del Níger", "Conakry → Mamou → Faranah (fuente del Níger)", "~440 km · 2 días"),
        ("Bajada 10 · Hacia la selva", "Faranah → Kissidougou → Macenta (bosque de Ziama)", "~290 km · 2 días"),
        ("Bajada 11 · Guinea forestal", "Macenta → Nzérékoré", "~140 km · 1-2 días"),
        ("Bajada 12 · Salida por el Nimba", "Nzérékoré → Lola → montes Nimba → N'Zo/Gbapleu", "~130 km · 2 días con la visita al Nimba"),
        ("Subida 1 · Reentrada", "N'Zo/Gbapleu → Lola → Nzérékoré", "~130 km · 1 día"),
        ("Subida 2 · Al mundo malinké", "Nzérékoré → Beyla → Kankan", "~400 km · 2-3 días"),
        ("Subida 3 · El Níger navegable", "Kankan → Kouroussa (+ Parque N. del Alto Níger)", "~130 km · 1-2 días"),
        ("Subida 4 · A la bisagra", "Kouroussa → Dabola → cataratas del Tinkisso", "~160 km · 1 día"),
        ("Subida 5 · Fouta oriental (4x4)", "Dabola → Tougué → Labé", "~350 km · 2-3 días de pista — el tramo más solitario"),
        ("Subida 6 · Salida", "Labé → Koundara → Sambaïlo (frontera de Senegal)", "~180 km · 1-2 días"),
    ],
    offroad=[
        "Pista Dabola → Tougué → Labé (~350 km): el tramo 4x4 más exigente y más solitario de todo el corredor guineano y la razón principal para elegir este corredor de subida. Remonta el flanco oriental del Fouta Djallon por escarpes y gargantas que caen hacia la cuenca del Tinkisso, entre pueblos fulani sin tráfico. Sin garantía de combustible desde Dabola, con cobertura móvil nula en tramos largos y con vados que en lluvias se vuelven impasables. POR CONFIRMAR el estado actual y si es practicable fuera de la seca; la alternativa conservadora es subir por asfalto vía Mamou.",
        "Carretera Labé → Mali (monte Loura), ~120 km: una de las más espectaculares y peor asfaltadas del país, subiendo al borde norte del altiplano hasta 1.400 m. Asfalto degradado que alterna con tramos de laterita; el paisaje —tapades fulani, escarpes y vistas sobre la llanura senegalesa— compensa de sobra.",
        "Acceso a las cataratas de Kambadaga desde Pita (~25 km): pista de tierra con baches, vados y una bajada final pronunciada. Transitable en 4x4 todo el año salvo en lluvias fuertes. Al final hay que bajar a pie al cauce.",
        "Pita → Doucki (~60 km, 2-3 horas): pista con baches sostenidos hasta el borde del altiplano. Los viajeros sin vehículo propio pagan plazas de más en un taxi-brousse para hacerla; nosotros llegamos con los dos coches hasta el campamento de Hassan, que es una ventaja logística grande para el bloque de senderismo.",
        "Acceso a las cataratas de Ditinn desde Dalaba (~50 km): pista de tierra por la meseta hasta el pueblo de Ditinn, y desde ahí la bajada al valle para ver el circo desde abajo, que es la aproximación buena.",
        "Acceso al bosque de Ziama desde la carretera Macenta-Nzérékoré (Sérédou): pistas forestales de laterita en selva húmeda, con barro serio en estación de lluvias — que en la Guinea forestal es de marzo a noviembre, es decir, casi todo el año. Guía comunitario indispensable.",
        "Subida a los montes Nimba desde Lola: pistas de montaña dentro de una reserva natural integral, con acceso restringido y guía obligatorio del CEGENS. No es un tramo de conducción libre: hay que ir con el permiso resuelto.",
        "Estacionalidad, resumen operativo: el Fouta y la Alta Guinea tienen una seca marcada (noviembre-abril, óptimo febrero-marzo) y una húmeda dura (mayo-octubre). La Guinea forestal es otra cosa: llueve de marzo a noviembre y caen 1.800 mm al año, así que el sureste nunca está del todo seco. Planificar el Fouta en seca y asumir que Ziama y el Nimba se harán con barro.",
    ],
    senderismo=[
        "Doucki · el «Gran Cañón de Guinea» (3-4 días): el mejor senderismo de África occidental y el bloque a pie más importante de todo el viaje entre Marruecos y Camerún. Diez rutas con nombre propio abiertas por Hassan Bah a lo largo de décadas, desde el «Grand Canyon» (4 km, fácil) hasta «Chutes & Ladders» (~20 km, duro) y la «Valley Hike» (10-16 km, dura), pasando por «Indiana Jones World», «Hyena's Rock», «Vultures Rock», «The Caves», «Bob Marley Stage» y «Wet & Wild». Alojamiento y comidas en su campamento, todo incluido por unos 50 USD/día/persona, sin tasas de entrada. Contacto: Hassane Doucki Hiking Guide and Host ADT, +224 622 45 75 53. Mínimo tres noches; óptimo febrero-marzo.",
        "Monte Loura y la Dame de Mali (1.515 m): la cumbre más alta de África occidental fuera de Camerún, con subida cómoda desde el pueblo de Mali y guía local. El perfil rocoso de «la Dama» asomando sobre el vacío y la vista sobre la llanura senegalesa son de las imágenes grandes del viaje. Fuera de espacio protegido: apta para el perro.",
        "Monte Gangan (1.117 m), Kindia: macizo de granito con paredes que atraen a escaladores y rutas de subida a pie desde la carretera de Kindia. Jornada asequible con vistas sobre la llanura costera; se combina con el baño en el Voile de la Mariée.",
        "Cataratas de Kambadaga (Pita): bajada a pie por sendero hasta los tres saltos escalonados y las pozas del cañón del Kokoulo, con posibilidad de recorrer el cauce en seca. La mejor combinación de caminata y baño del Fouta.",
        "Cataratas de Ditinn: aproximación por el valle hasta el fondo del circo de arenisca, bajo el chorro de 70-80 m. Es más larga y más bonita que asomarse al mirador superior, y es lo que recomiendan los guías locales.",
        "Cataratas de Kinkon (Pita): sendero por el borde del cañón del Kokoulo hasta los miradores sobre la caída de 80 m y las paredes de arenisca roja. Corto, pero el cañón es magnífico. No fotografiar la central hidroeléctrica.",
        "Montes Nimba (UNESCO): ascensión guiada a las praderas de altura de la reserva integral, en la triple frontera con Costa de Marfil y Liberia. Es senderismo de alta montaña tropical con endemismos extremos —el sapo vivíparo del Nimba, único en el mundo— y acceso restringido: permiso del CEGENS obligatorio.",
        "Bosque de Ziama (Sérédou, Macenta): caminatas de selva primaria cerrada con guía comunitario, de medio día a varios días. No es safari: es bosque húmedo, rastros, aves y árboles gigantes, con la posibilidad remota de rastro de elefante de bosque. Botas, humedad extrema y sanguijuelas.",
        "Nacimiento del río Níger (Faranah): caminata corta pero simbólica desde el final de la pista hasta el manantial, en un claro de bosque de las estribaciones de los montes Loma, con guía del pueblo. Poder cruzar de un paso el tercer río más largo de África es de las cosas que se cuentan al volver.",
        "Travesías de pueblo en pueblo por el Fouta: fuera de Doucki, la región entera es caminable. Cualquier pueblo del altiplano —Timbi Madina, Ley-Saré, los alrededores de Télimélé— permite contratar a un guía local por el día y caminar entre tapades, arroyos y escarpes sin ver a otro viajero. Es la mejor forma de usar los días que sobren.",
    ],
    acampada=[
        "Regla general: Guinea es un país amable para el vivac en el interior, pero la fórmula que mejor funciona es pedir permiso al jefe del pueblo (el «chef de village») antes de instalarse. En el Fouta esto se resuelve con una conversación y una propina, y a cambio se consigue vigilancia informal y, a menudo, agua y leña.",
        "Doucki: campamento de Hassan Bah, con cabañas sencillas y baño compartido. Hay sitio para los vehículos y la fórmula de pensión completa incluye guía. Es la base del bloque de senderismo: tres noches mínimo.",
        "Kambadaga (Pita): el mejor sitio de acampada libre del Fouta central, junto al cañón del Kokoulo, con permiso del pueblo. Agua abundante y pozas para bañarse.",
        "Mali / monte Loura: vivac en alto a 1.400 m, el punto más fresco de Guinea — en diciembre-enero puede haber escarcha. Permiso del pueblo de Mali.",
        "Labé, Dalaba, Mamou, Kindia: hoteles y bungalows sencillos con patio y aparcamiento; Dalaba, a 1.200 m, es la noche más agradable del eje central.",
        "Conakry: aparcamiento vigilado obligatorio. La densidad urbana y el tráfico de la península hacen que dejar los vehículos sin vigilancia toda la noche sea una mala idea. Hoteles de Kaloum y Kipé con recinto.",
        "Corredor sureste (Faranah, Kissidougou, Macenta, Nzérékoré): misiones católicas y hoteles sencillos con patio en todas las capitales. En la Guinea forestal la acampada libre es poco recomendable por la lluvia constante y por la densidad de población rural.",
        "Corredor de subida (Kankan, Kouroussa, Dabola, Tougué): alojamientos elementales con patio en las capitales prefecturales. En la pista de Tougué, vivac con permiso del pueblo: es la zona más solitaria del país.",
        "Islas de Los: alojamientos sencillos de playa en Room; los vehículos se quedan en Conakry.",
    ],
    visado=[
        "eVisa OBLIGATORIA y previa para pasaporte español: ~90 días de validez, entrada única, coste aproximado 129 €, trámite nominal de 72 h — pedirla con 10 días de margen. NO se expide visado en frontera terrestre guineana, sin excepción.",
        "Requisitos: pasaporte con 6+ meses de vigencia, certificado internacional de fiebre amarilla, foto biométrica reciente, justificante de itinerario o de alojamiento.",
        "PROBLEMA DEL DOBLE CRUCE: la eVisa estándar es de entrada única y 90 días, y el país se cruza dos veces con varios meses de diferencia. Confirmar con la embajada de Guinea si existe eVisa o visado consular de ENTRADA MÚLTIPLE con vigencia larga. Si no existe, hay que planificar el segundo visado en ruta: la opción realista es la embajada de Guinea en Abiyán (Costa de Marfil) antes de la subida — CONFIRMAR que expide a extranjeros no residentes.",
        "Confirmar 30-60 días antes que el puesto de Sambaïlo acepta la eVisa impresa sin trámite adicional, y lo mismo para el de N'Zo, que está mucho peor documentado.",
        "Además del visado, en la frontera se emite un laissez-passer de entrada (del orden de 50.000 GNF) que fija por escrito la duración autorizada de la estancia. Comprobar la fecha antes de irse del puesto: corregirla después es un problema.",
        "Llevar muchas fotocopias del pasaporte, del visado y del sello de entrada para los controles de carretera, que en Guinea son frecuentes aunque mucho menos numerosos que en Nigeria.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Sambaïlo / Koundara (desde Manda-Kalifourou, Senegal)", "El paso más fácil de los seis vecinos de Guinea: asfalto bueno a ambos lados. ~20 km de tierra de nadie. Visado ya emitido (no se da en frontera), laissez-passer de ~50.000 GNF, CPD o carnet ATA, permiso internacional, seguro CEDEAO y certificado de vacunación. CIERRA DE NOCHE: llegar con varias horas de luz."),
        ("Salida bajada", "N'Zo / Gbapleu (hacia Danané, Costa de Marfil)", "Paso principal entre la Guinea forestal y el oeste marfileño, reabierto en 2016 tras el cierre por ébola. Es la ÚNICA salida prevista: Liberia está excluida de la ruta por el visado. POR CONFIRMAR horarios, sellado de CPD y estado del asfalto Nzérékoré-Lola-N'Zo."),
        ("Entrada subida", "N'Zo / Gbapleu (desde Costa de Marfil)", "Mismo paso, sentido inverso. Segundo visado guineano y segundo laissez-passer. La diferenciación del corredor se consigue en el interior (Alta Guinea), no en la frontera."),
        ("Salida subida", "Sambaïlo / Koundara (hacia Senegal)", "Mismo paso que la entrada de la bajada. Desde Labé son ~180 km. Cerrar el laissez-passer y el CPD."),
        ("Alternativa por verificar", "Sipilou / Kérouané-Beyla (desde Costa de Marfil)", "Paso más al norte que permitiría no repetir N'Zo en la subida y entrar directamente a la Alta Guinea. MUY POCO DOCUMENTADO: confirmar existencia, horario, aduana y estado de la carretera antes de contar con él. Si se verifica, mejora mucho la diferenciación de corredores."),
        ("Variante opcional", "Pamelap / Forécariah (hacia Sierra Leona)", "Asfaltado de punta a punta hacia Kambia y Freetown. Solo se activa si se ejecuta la variante opcional de Sierra Leona prevista en la ruta global del viaje."),
        ("Zona excluida", "Todos los pasos con Guinea-Bisáu y con Malí", "Guinea-Bisáu por protocolo del proyecto; Malí por conflicto. Esto descarta el eje Siguiri-Kourémalé y toda la franja fronteriza del noreste."),
    ],
    vehiculos=[
        "CPD (carnet de paso en aduana) o carnet ATA: los relatos de viajeros con vehículo en Guinea lo dan como requisito en la frontera. Alternativa si no se dispone de él: laissez-passer temporal emitido en la aduana — confirmar el procedimiento antes de llegar.",
        "Permiso internacional de conducir obligatorio y comprobado en los controles.",
        "Carte Brune / Brown Card de la CEDEAO como seguro de responsabilidad civil regional: confirmar que la póliza contratada cubre expresamente Guinea y que la vigencia llega a la segunda pasada.",
        "Equipamiento que se comprueba en frontera y en controles, según los relatos de viajeros francófonos: extintor, botiquín y triángulos de señalización. Llevarlos accesibles, no enterrados.",
        "Llevar copias impresas de toda la documentación: los puestos de Sambaïlo y de N'Zo no siempre disponen de medios para verificar documentos digitales.",
        "Autonomía de combustible: garrafas para cubrir Mamou → Nzérékoré (~650 km, con roturas de suministro puntuales en Macenta) en la bajada y Dabola → Labé por Tougué (~350 km de pista sin garantía) en la subida.",
        "Neumáticos y suspensión: la combinación de asfalto degradado y laterita del Fouta y del corredor de Tougué es exigente. Conakry es la única plaza con recambios de cierto nivel; Labé y Kankan tienen talleres elementales.",
        "Filtro de embudo para el gasóleo fuera de Conakry: la calidad es variable y en el interior se compra a veces en garrafa.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Sin procedimiento turístico publicado: solicitar autorización previa y por escrito a la Agence Nationale de l'Aviation Civile (ANAC-Guinée) o, en su defecto, no volar el dron en el país.",
        "Nunca sobrevolar Conakry (aeropuerto, puerto, Camp Samory Touré, edificios de gobierno) bajo ninguna circunstancia.",
        "Nunca sobrevolar las instalaciones mineras de bauxita de Boké y Kamsar ni las centrales hidroeléctricas de Kinkon, Garafiri o Tinkisso: son zonas industriales con seguridad privada y sensibilidad alta.",
        "Nunca sobrevolar los montes Nimba ni el bosque de Ziama sin permiso expreso de los gestores: son espacios protegidos con normativa propia.",
        "Contexto político: el país está en transición tras un golpe de Estado y hay presencia militar visible. Un dron mal interpretado es un problema desproporcionado. Criterio del proyecto: no volar sin papel.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Revisar el mapa oficial de Starlink 30-60 días antes de entrar: Guinea no está confirmada como mercado activo a fecha de esta revisión y no se ha localizado licencia pública de la ARPT guineana.",
        "SIM/eSIM local (Orange Guinée, MTN Guinée) como conectividad principal. Comprar en Conakry con pasaporte; Orange tiene la mejor cobertura del interior.",
        "Cobertura aceptable en Conakry, Kindia, Mamou, Dalaba, Labé, Kankan y Nzérékoré. Degradada o nula en Doucki, en la pista de Tougué, en Mali/Loura, en el bosque de Ziama y en el acceso al Nimba: dar por hecho 2-3 días incomunicados en cada bloque y avisar en casa antes de entrar.",
        "Si Starlink no está disponible, Guinea es el tramo con peor conectividad de toda la ruta atlántica entre Marruecos y Nigeria: planificar la gestión de trámites (visados del bloque siguiente, permisos del perro) para hacerla desde Conakry, que es donde sí hay ancho de banda.",
    ],
    perro_intro=[
        "CIERRE PARCIAL DEL AGUJERO NEGRO. El dosier del perro del proyecto señalaba Guinea como uno de los tres «agujeros negros documentales» de la ruta, sin ninguna fuente sobre la entrada del animal. En esta revisión se ha localizado el marco legal, la autoridad competente y los requisitos prácticos. Sigue sin localizarse un solo testimonio de cruce terrestre con animal.",
        "MARCO LEGAL: la Ley L/2018/026/AN, de 3 de julio de 2018, Código de Ganadería y Productos Animales de Guinea, es la norma aplicable. Su artículo 41 establece que todo animal vivo presentado a la importación está sometido a control sanitario veterinario ANTES del despacho de aduana, y su artículo 21 exige que los animales que cruzan la frontera vayan acompañados de certificado sanitario y certificado de vacunación contra las enfermedades de declaración obligatoria. El artículo 117 confirma que existen puestos de control fronterizo («postes-frontières») en el sistema.",
        "AUTORIDAD COMPETENTE identificada: la Direction Nationale des Services Vétérinaires (DNSV), dependiente del Ministère de l'Agriculture et de l'Élevage (MAGEL) de Guinea. Es el interlocutor al que hay que escribir. En el interior existe además el Laboratoire Régional Vétérinaire de Labé, que está justo en el nudo de nuestros dos corredores.",
        "REQUISITOS PRÁCTICOS localizados (fuente veterinaria especializada francófona, coherente con el marco legal): identificación electrónica (microchip) y pasaporte del animal; vacuna antirrábica en vigor con MENOS DE 12 MESES; y certificado veterinario internacional expedido por un veterinario habilitado DENTRO DE LAS 72 HORAS previas a la llegada. La titulación serológica de anticuerpos NO es exigida para entrar en Guinea, pero SÍ lo es para volver a la UE, de modo que hay que tenerla hecha igualmente desde España.",
        "LA VENTANA DE 72 HORAS ES EL PROBLEMA OPERATIVO REAL. Obliga a conseguir el certificado internacional en el país anterior justo antes de cruzar: en Tambacounda o Kédougou (Senegal) para la bajada, y en Man o Danané (Costa de Marfil) para la subida. Hay que localizar un veterinario habilitado en esas ciudades con antelación, no improvisarlo. Es el punto que más puede descarrilar el cruce.",
        "PERMISO PREVIO DE IMPORTACIÓN: no aparece exigido para animales de compañía en las fuentes localizadas, pero el Código de Ganadería sí somete la importación de animales vivos a autorización y control del ministro competente. POR CONFIRMAR con la DNSV si un perro de compañía en tránsito turístico necesita autorización previa o basta con el certificado en frontera.",
        "ENTRADA TERRESTRE: no existe ninguna prohibición conocida. El USDA-APHIS, que sí documenta restricciones de puerto de entrada cuando existen, no menciona ninguna para Guinea. Y el propio Código de Ganadería guineano regula el paso de animales por los puestos fronterizos terrestres, lo que implica que está contemplado. Aplicando la regla de trabajo del dosier del proyecto («no mencionado por una web de vuelos ≠ prohibido»), la entrada terrestre se considera VIABLE mientras no aparezca una fuente oficial que la prohíba.",
        "DOBLE CRUCE: como el país se recorre dos veces con meses de diferencia, hay que contar con DOS certificados internacionales (uno por cada entrada, cada uno dentro de su ventana de 72 h) salvo que la DNSV confirme por escrito lo contrario.",
        "IDIOMA: Guinea es francófona. Toda la documentación en francés o con traducción jurada al francés — la versión inglesa del pasaporte europeo no basta en Sambaïlo ni en N'Zo.",
        "LO QUE SIGUE ABIERTO: la práctica de ventanilla. No se ha localizado ni un solo relato de un viajero que haya cruzado una frontera terrestre guineana con un animal de compañía. Preguntar activamente en los foros overland y en iOverlander antes de salir, y escribir a la DNSV y a la Embajada de Guinea en Madrid o París en paralelo, con 6 meses de antelación.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional OBLIGATORIO, sin excepciones, para entrar en el país y comprobado en frontera.",
        "Malaria en todo el territorio y todo el año, con transmisión especialmente intensa en la Guinea forestal y en la costa: profilaxis a valorar con Sanidad Exterior, mosquitera y repelente con DEET.",
        "ÉBOLA Y MARBURGO — la Guinea forestal: la prefectura de Guéckédou, en el sureste, fue el foco de origen de la epidemia de ébola de África occidental de 2013-2016, la mayor de la historia; la región tuvo un rebrote en 2021 y registró además el primer caso de virus de Marburgo detectado en África occidental. Nuestro corredor de bajada atraviesa esta región (Macenta, Nzérékoré). NO es motivo para evitarla —la epidemia terminó hace años y la vigilancia epidemiológica de la zona es hoy de las mejores de la región—, pero SÍ para comprobar el estado epidemiológico con la OMS y el ECDC 30-60 días antes de entrar, extremar la higiene de manos, evitar la carne de monte sin excepción y no acercarse a colonias de murciélagos en cuevas.",
        "Agua: no beber del grifo en ningún punto del país. Agua embotellada o en bolsa en las ciudades; en el Fouta el agua de manantial es abundante pero hay que tratarla (filtro mecánico más tratamiento químico o ebullición). Paradoja del «castillo de agua»: mucha agua, poca potable.",
        "Vacunación recomendada además: hepatitis A y B, fiebre tifoidea, tétanos-difteria, meningitis, poliomielitis y rabia — esta última especialmente relevante viajando con perro y con alta densidad de perros sin vacunar.",
        "Referencias hospitalarias: Hôpital National Donka en Conakry (capacidad limitada para politraumatismos), hospitales regionales de Labé, Kankan y Nzérékoré. Fuera de Conakry el nivel cae mucho; en Doucki, Tougué, Ziama y el Nimba no hay nada.",
        "Seguro con evacuación médica AÉREA imprescindible: la evacuación realista desde Guinea es a Dakar o directamente a Europa, no dentro del país. Es uno de los tramos del viaje donde más lejos se puede estar de un hospital utilizable.",
        "Altitud y frío: el Fouta a 1.000-1.500 m tiene noches frescas de verdad (en Mali, a 1.400 m, puede helar en diciembre-enero). Es una ventaja enorme para descansar y para el perro, pero hay que llevar saco y ropa de abrigo — se olvida fácilmente viniendo del Sahel.",
    ],
    seguridad_intro=("Guinea no tiene conflicto armado activo en el itinerario previsto y es, en la práctica cotidiana, uno de los países más tranquilos y hospitalarios del tramo atlántico. Los dos factores a vigilar son distintos: "
                     "la <strong>situación política</strong>, en transición desde el golpe de Estado de septiembre de 2021, con manifestaciones y cortes de carretera ocasionales en Conakry; y el <strong>aislamiento</strong> "
                     "de los tramos buenos —Doucki, Tougué, el Loura, Ziama—, donde el riesgo real no es la violencia sino quedarse sin cobertura, sin combustible y sin tráfico del que depender."),
    seguridad=[
        "Situación política: transición abierta desde el golpe de Estado de septiembre de 2021. Las manifestaciones en Conakry pueden derivar en cortes de carretera, cierre de internet y represión. Evitar concentraciones, no fotografiar protestas ni despliegues policiales, y revalidar el estado del país 30-60 días antes y de nuevo 72 h antes de entrar.",
        "Franja fronteriza con Malí EXCLUIDA (prefecturas de Siguiri y Mandiana, eje Kankan-Kourémalé): la inestabilidad del Sahel maliense y la presión de grupos armados hacen que el noreste quede fuera del itinerario. El corredor de subida por la Alta Guinea se mantiene deliberadamente al sur y al oeste.",
        "Frontera de Guinea-Bisáu: exclusión total por protocolo del proyecto, incluida la variante costera de Boké, que puede recorrerse pero no prolongarse hacia el norte.",
        "No conducir de noche fuera de los núcleos urbanos: el estado de las carreteras, la ausencia de señalización, el ganado suelto y los camiones sin luces lo hacen desaconsejable. Además, las fronteras cierran de noche, lo que en la práctica ya obliga a planificar en horario diurno.",
        "Controles de carretera: frecuentes pero mucho más llevaderos que en Nigeria. Documentación en carpeta con copias, saludo en francés, paciencia y ninguna prisa. Las peticiones de «quelque chose» existen pero son moderadas.",
        "No fotografiar NUNCA instalaciones militares, el Camp Samory Touré de Conakry, puertos, aeropuertos, centrales hidroeléctricas (Kinkon, Garafiri, Tinkisso) ni las minas de bauxita de Boké y Kamsar.",
        "Aislamiento de los tramos buenos: en Doucki, en la pista de Tougué, en el Loura y en Ziama no hay cobertura móvil ni tráfico del que depender en caso de avería. Los dos vehículos siempre juntos, autonomía completa de agua y combustible, y dejar dicho en el alojamiento anterior a dónde se va y cuándo se vuelve.",
        "Conakry: delincuencia urbana común (tirones, robos en atascos, carterismo en el mercado de Madina). Ventanillas subidas en atasco, nada visible en el salpicadero, aparcamiento vigilado y no circular de noche por la península.",
        "Dinero: llevar euros en efectivo como respaldo real. Los cajeros son escasos fuera de Conakry, Labé y Kankan, y el límite por operación es muy bajo (~40 €). Cambiar en casas de cambio o bancos, no en la calle.",
        "Minería: Guinea es un país minero y las zonas de concesión (Boké, Kamsar, Simandou, Nimba) tienen seguridad privada, tráfico pesado y accesos restringidos. No improvisar desvíos por pistas mineras.",
    ],
    agua=[
        "Conakry, Labé, Kankan, Nzérékoré y todas las capitales regionales: agua embotellada y en bolsa en supermercados y tiendas. Para el depósito de uso general, estaciones de servicio, hoteles y misiones católicas suelen permitir llenar con manguera.",
        "Fouta Djallon: es el «castillo de agua de África occidental» —de aquí nacen el Níger, el Senegal y el Gambia— y hay manantiales y arroyos constantes en todo el altiplano. Pero el agua de superficie NO es potable sin tratar: filtro mecánico más tratamiento químico o ebullición, siempre.",
        "Doucki y Kambadaga: agua de pozo o de manantial en los campamentos. En Doucki, el campamento de Hassan la proporciona; tratarla igualmente para beber.",
        "Corredor de subida (Kankan, Kouroussa, Dabola, Tougué): la Alta Guinea es sabana seca y el agua es más escasa que en el Fouta. Llenar depósitos a fondo en Kankan y en Dabola antes de la pista de Tougué.",
        "En zona rural, confirmar con la comunidad antes de usar un pozo compartido: en el Fouta el agua es un bien gestionado colectivamente y no se toma sin preguntar.",
    ],
    combustible=[
        "Eje central (Conakry → Kindia → Mamou → Dalaba → Pita → Labé → Koundara): la mejor cobertura del país, con estaciones formales en todas las ciudades. Sin ningún hueco comprometido.",
        "AVISO — bajada: el tramo Mamou → Faranah → Kissidougou → Macenta → Nzérékoré (~650 km) tiene estaciones formales en las capitales pero con roturas de suministro puntuales, especialmente en Macenta. Salir de Mamou con garrafas llenas y repostar en cuanto haya oportunidad, sin esperar a estar bajo.",
        "AVISO — subida: a partir de Dabola, la pista Tougué-Labé (~350 km) no tiene garantía de combustible. Salir de Dabola con depósitos y garrafas al 100 %, contando además con el mayor consumo en pista.",
        "Repostar a fondo en Conakry, que tiene la mejor oferta y calidad del país (Total, Vivo, Petroguinée), y otra vez en Labé y en Kankan, que son las mejores plazas del interior.",
        "Evitar el combustible de garrafa informal salvo necesidad: calidad imprevisible. Filtro de embudo obligatorio fuera de Conakry.",
        "Confirmar puntos recientes en iOverlander antes de cada tramo: la red formal es limitada y algunas estaciones rurales pueden estar secas durante días.",
    ],
    experiencias_intro=("Relatos y comentarios reales de otros viajeros sobre Guinea, para contrastar con la planificación oficial de esta ficha. Guinea tiene muchísima menos información pública que sus vecinos —es de los países peor documentados de toda la ruta atlántica— "
                        "con una excepción llamativa: Doucki y el Fouta Djallon, que llevan décadas siendo un secreto a voces de la comunidad mochilera:"),
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Perro · DNSV", "Escribir a la Direction Nationale des Services Vétérinaires (Ministère de l'Agriculture et de l'Élevage, Conakry) y a la Embajada de Guinea en Madrid o París EN PARALELO, con 6 meses de antelación: confirmar (1) si un perro de compañía en tránsito necesita autorización previa de importación además del certificado; (2) que la ventana del certificado internacional es de 72 h también en entrada TERRESTRE; (3) si hace falta un certificado por cada una de las dos entradas. Criterio de cierre: respuesta por escrito, o confirmación verbal registrada con nombre y cargo"),
        ("Perro · ventana de 72 h", "Localizar con antelación un veterinario habilitado en Tambacounda o Kédougou (Senegal) para la bajada y en Man o Danané (Costa de Marfil) para la subida. Es el punto que más puede descarrilar el cruce y no se puede improvisar"),
        ("Perro · testimonio overland", "Buscar activamente en foros overland e iOverlander a alguien que haya cruzado una frontera terrestre guineana con animal de compañía. No se ha localizado ni uno. Es el dato que falta para cerrar el agujero negro del todo"),
        ("Perro · Nimba y Ziama", "Confirmar por escrito con el CEGENS (montes Nimba) y con el Centre Forestier de Nzérékoré (Ziama) la política de mascotas; damos por hecho que es no y planificamos turnos, pero conviene tenerlo por escrito"),
        ("Visado · doble entrada", "Confirmar si existe eVisa o visado consular guineano de ENTRADA MÚLTIPLE; si no, confirmar que la embajada de Guinea en Abiyán expide a extranjeros no residentes ANTES de salir de España"),
        ("Frontera de N'Zo/Gbapleu", "Confirmar horarios, sellado de CPD y estado del asfalto Nzérékoré-Lola-N'Zo. Es el punto único de fallo del corredor de bajada, porque Liberia está excluida y no hay salida alternativa por el sur"),
        ("Paso de Sipilou (alternativa)", "Verificar si existe y es practicable el paso Sipilou/Kérouané-Beyla desde Costa de Marfil: permitiría no repetir N'Zo en la subida y mejoraría mucho la diferenciación de corredores"),
        ("Pista Dabola-Tougué-Labé", "Confirmar el estado real de la pista y si es practicable fuera de la estación seca. Si no lo es, la subida vuelve por asfalto vía Mamou y se pierde el mejor tramo 4x4 del país. DECISIÓN DEL DUEÑO"),
        ("Doucki · reserva", "Contactar con Hassan Bah (+224 622 45 75 53) para reservar 3-4 noches, confirmar que se puede llegar y aparcar con los dos vehículos y decidir qué rutas admiten al perro"),
        ("Cascadas del Fouta", "Preguntar en Pita por el caudal de Kinkon (depende de la presa, no de la estación) antes de conducir hasta allí. Kambadaga y Ditinn son estacionales: julio-noviembre para caudal, febrero-marzo para pistas"),
        ("Calendario · el conflicto de fondo", "El Fouta quiere febrero-marzo (seco, fresco, pistas) y las cascadas quieren julio-noviembre (caudal). Con dos pasadas se puede cubrir las dos cosas: decidir cuál va en cada una. DECISIÓN DEL DUEÑO"),
        ("Parques del Badiar y del Alto Níger", "Confirmar sobre el terreno si tienen guardas, tasas y pistas practicables en 2027, o si son parques solo sobre el papel"),
        ("Montes Nimba · permiso", "Confirmar con el CEGENS el procedimiento de acceso a la reserva natural integral, tasas y guías, con antelación desde Nzérékoré"),
        ("Salud · estado epidemiológico", "Comprobar con OMS y ECDC el estado de la Guinea forestal (ébola, Marburgo) 30-60 días antes de entrar, en cada una de las dos pasadas"),
        ("Starlink", "Revisar el mapa oficial 30-60 días antes; si sigue sin estar activo, planificar todos los trámites pesados para hacerlos desde Conakry"),
        ("Situación política", "Revalidar el estado de la transición y de la conflictividad en Conakry 30-60 días antes y de nuevo 72 h antes de cada frontera"),
        ("Dron", "Resolver autorización por escrito ante la ANAC-Guinée o excluirlo del país. La recomendación del proyecto es no volar sin papel"),
        ("Fotos pendientes de sustituir", "La mayoría de los PDIs de esta ficha usan imágenes de referencia de otro punto del país (solo hay cinco archivos de Guinea verificados en Wikimedia Commons): sustituir por fotos propias o por archivos verificados a medida que aparezcan"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Novedad de esta revisión: el «agujero negro» documental del perro en Guinea que señalaba el dosier del proyecto queda PARCIALMENTE CERRADO — se han identificado el marco legal (Ley L/2018/026/AN), la autoridad competente (DNSV) y los requisitos prácticos (microchip, rabia <12 meses, certificado internacional en 72 h), y no se ha encontrado ninguna fuente oficial que prohíba la entrada terrestre. Lo que sigue abierto es la práctica de ventanilla en Sambaïlo y en N'Zo, para la que no existe ni un solo testimonio localizado.",
    emergency="Policía 117 · Gendarmería 122 · Bomberos 118 (números variables según región: verificar localmente) · Emergencia consular española grave: +224 664 33 54 93 · Embajada de España en Conakry: +224 664 20 22 01 · Sección consular: +224 613 33 90 90.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

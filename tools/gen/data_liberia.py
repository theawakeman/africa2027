# -*- coding: utf-8 -*-
"""Liberia — ficha completa, país EXCLUIDO de la ruta fija por el visado terrestre (12 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== CORREDOR HIPOTÉTICO A · COSTA, DE OESTE A SURESTE =====
    dict(n=1, name="Bo-Waterside · la frontera que no podemos cruzar", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=6.8500, lon=-11.2500,
         desc="El paso fronterizo principal del oeste de Liberia, frente al sierraleonés de Jendema, con tráfico comercial denso de camiones y autobuses. Es la puerta natural desde Sierra Leona y la primera que se activaría si el problema del visado se resolviera. Y es exactamente donde está el problema: el visado electrónico liberiano, en vigor desde el 11 de marzo de 2025, es un «visado electrónico a la llegada» que SOLO se expide en el aeropuerto internacional de Monrovia. En una frontera terrestre no sirve: hay que presentarse con un visado estampado por una misión diplomática liberiana. Sin ese papel, este puesto es una pared. Con él, Liberia se abre entera. Ver el bloque de visado para el detalle y para la vía de solución.",
         credit="Wikimedia Commons", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
    dict(n=2, name="Robertsport · surf de clase mundial", cat="Costa · surf", prio="Alta", dog="permitido", time="2–3 días",
         lat=6.7500, lon=-11.3667,
         desc="A 80 km al noroeste de Monrovia y a apenas 16 km de la frontera sierraleonesa, sobre la península de Cape Mount: una lengua de tierra entre el lago Piso y el Atlántico, dominada por un promontorio de granito de 300 m que Pedro de Sintra bautizó Cabo do Monte a mediados del siglo XV. Es uno de los mejores puntos de surf de África y el más reconocido internacionalmente de toda la costa: cinco o seis olas de izquierdas con nombre propio —Fisherman's Point, Cotton Trees, Cassava Point, Camp Point, Cutting Point— que rompen largas y limpias sobre puntas de arena y piedra, con los cocoteros pegados a la arena. El Tubman Center of African Culture, construido en 1964 para el cumpleaños del presidente Tubman, quedó destruido en la guerra y solo se conservan las ruinas. Playa enorme, poca gente y buen sitio para el perro. Lo que frena el turismo aquí no es el lugar, es el estado de la carretera y la falta de servicios.",
         credit="Bethel. Anthony Chisom · CC BY-SA 4.0", source=W + "Robertsport%20Beach%2C%20Cape%20Mount%20County.jpg?width=900"),
    dict(n=3, name="Lago Piso (sitio Ramsar)", cat="Naturaleza", prio="Media", dog="permitido con precaución", time="½–1 día",
         lat=6.7353, lon=-11.2511,
         desc="La laguna salobre de 103 km² que separa Robertsport del interior: el mayor lago de Liberia, 30 km de largo por 16 de ancho, conectado con el Atlántico por una bocana estrecha que los locales llaman «bar mouth». Es el ÚNICO humedal de importancia internacional designado por el país —sitio Ramsar n.º 1306 desde el 2 de julio de 2003, con 76.091 hectáreas de humedales asociados— y área importante para las aves según BirdLife. Hay islas dentro, como Massatin, que funcionan como refugio de monos y aves. Se recorre en piragua con pescadores del pueblo: manglar, aves acuáticas y pesca artesanal, a un paso de la playa de surf. Combinación muy buena de dos días: olas por la mañana y laguna por la tarde.",
         credit="Bethel. Anthony Chisom · CC BY-SA 4.0", source=W + "Robertsport%20Beach%2C%20Cape%20Mount%20County.jpg?width=900"),
    dict(n=4, name="Monrovia · la capital más lluviosa del mundo", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=6.3131, lon=-10.8014,
         desc="Capital sobre el cabo Mesurado, con 1,76 millones de habitantes en el censo de 2022 y un área metropolitana de más de 2,2 millones: un tercio del país entero vive aquí. Ostenta un récord que hay que tener muy presente para planificar: es la CAPITAL MÁS LLUVIOSA DEL MUNDO, con una media de 4.600 mm al año. Barrios con carácter propio: Mamba Point, el barrio diplomático sobre el mar; Sinkor, el centro moderno de hoteles y negocios; Waterside, el mercado grande frente al puerto natural; y West Point, una península densísima de bajos ingresos que es también uno de los símbolos urbanos del país. Para ver: el Museo Nacional de Liberia, el mercado de Waterside y, sobre todo, la ruina del Hotel Ducor, el hotel de lujo de los años sesenta encaramado sobre el cabo, hoy esqueleto de hormigón con la mejor vista de la ciudad. Única base logística seria: puerto franco, bancos, talleres, hospitales y —lo más importante para nosotros— todas las embajadas.",
         credit="Mark Fischer · CC BY-SA 2.0", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
    dict(n=5, name="Providence Island · donde empezó Liberia", cat="Patrimonio", prio="Alta", dog="no confirmado", time="2–3 h",
         lat=6.3300, lon=-10.7950,
         desc="Una islita en la desembocadura del río Mesurado, dentro de Monrovia, donde en 1822 desembarcó el primer contingente de afroamericanos libres enviados por la American Colonization Society: es literalmente el punto cero de Liberia. Los agentes Robert F. Stockton y Eli Ayers negociaron allí el llamado Contrato Ducor con los jefes gola, dei y kru, que cedió el territorio entre el Atlántico y el Mesurado — y que, según la documentación histórica, los jefes firmaron sin compartir el concepto europeo de propiedad: creían estar cediendo el USO de la tierra, no vendiéndola. Ese malentendido fundacional explica buena parte de la historia posterior del país. Hoy quedan restos del asentamiento, algún edificio histórico y un pequeño espacio museístico; el Ministerio de Información, Asuntos Culturales y Turismo lo propuso en 2017 como candidato a Patrimonio Mundial de la UNESCO. Coordenada aproximada dentro de Monrovia.",
         credit="Mark Fischer · CC BY-SA 2.0", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
    dict(n=6, name="Harbel · la mayor plantación de caucho del mundo", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=6.2833, lon=-10.3500,
         desc="A una hora de Monrovia, camino del aeropuerto Roberts, empieza una cosa difícil de imaginar hasta que se atraviesa: un millón de acres —unas 400.000 hectáreas— de hevea plantada en filas perfectas, la mayor explotación continua de caucho natural del planeta. Firestone la obtuvo del gobierno liberiano en 1926 con un arrendamiento a 99 años por seis centavos el acre, en una operación que hipotecó literalmente la economía del país durante décadas; en 2005 se renegoció a 37 años y cincuenta centavos. El nombre, Harbel, es la contracción de Harvey y Bell, el fundador de Firestone y su mujer. La carretera la cruza durante kilómetros: hileras infinitas de árboles sangrados con su cuenco, poblados de trabajadores, y una historia laboral muy dura que ha llegado a los tribunales internacionales. No es un «sitio turístico»; es una de las cosas que mejor explican Liberia. No fotografiar instalaciones ni trabajadores sin permiso.",
         credit="Mark Fischer · CC BY-SA 2.0", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
    dict(n=7, name="Buchanan y las playas de Grand Bassa", cat="Costa", prio="Media", dog="permitido", time="1–2 días",
         lat=5.8800, lon=-10.0500,
         desc="A unos 110 km al sureste de Monrovia, el tercer puerto del país y el punto donde termina el ferrocarril minero de 250 km que baja el hierro desde Yekepa, en los montes Nimba — una de las pocas líneas férreas en funcionamiento de África occidental. Fundada en 1832 por cuáqueros negros como Port Cresson y refundada como Bassa Cove tras el conflicto de 1835 con los bassa, se libró relativamente de la destrucción de la primera guerra civil y sirvió de refugio. Lo que interesa al viajero está fuera del puerto: playas aisladas y lagunas a lo largo de toda la costa de Grand Bassa, prácticamente vacías, con cocoteros y pueblos de pescadores kru. Es la última parada con servicios reales antes de meterse en el sureste, que es otro mundo. Aquí se reposta a fondo y se cargan provisiones.",
         credit="Bethel. Anthony Chisom · CC BY-SA 4.0", source=W + "Robertsport%20Beach%2C%20Cape%20Mount%20County.jpg?width=900"),
    dict(n=8, name="Greenville (Sinoe) · la puerta de Sapo", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=5.4111, lon=-8.4146,
         desc="Capital del condado de Sinoe, a unos 150 km al sureste de Monrovia en línea recta pero mucho más por carretera, sobre una laguna junto a la desembocadura del río Sinoe. Unos 16.000 habitantes, tercer puerto del país con dos muelles y seis metros de calado, y una economía que gira alrededor de la madera. La fundó hacia 1838 la Mississippi Colonization Society y lleva el nombre de un plantador de Misisipi que financió el traslado de sus antiguos esclavos; quedó destruida en la guerra civil y se reconstruyó después. El dato que la define: 185 días de lluvia al año. Es la base logística obligatoria para Sapo —el último sitio con combustible, provisiones y un teléfono— y el punto donde hay que tener resuelta la autorización de la Forestry Development Authority antes de seguir.",
         credit="Wikimedia Commons", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
    dict(n=9, name="Parque Nacional de Sapo", cat="Naturaleza", prio="Alta", dog="prohibido", time="3–5 días",
         lat=5.4000, lon=-8.8000,
         desc="1.804 km² de selva tropical primaria en el condado de Sinoe: el primer parque nacional de Liberia (1983) y la SEGUNDA mayor masa de selva primaria continua de África occidental, solo por detrás de Taï en Costa de Marfil. Forma parte del bloque forestal de Alto Guinea, que Conservation International describe como la región con mayor diversidad de especies de mamíferos del mundo. Unas 125 especies de mamíferos y 590 de aves: entre 500 y 1.640 chimpancés occidentales, elefante de bosque, siete especies de duiker y —la joya— el hipopótamo pigmeo, fotografiado por primera vez en Liberia precisamente aquí, en 2008. El pueblo sapo considera tabú cazar al chimpancé, lo que ha ayudado a su supervivencia. AVISO OPERATIVO DE PRIMER ORDEN: al parque SOLO se entra A PIE. No hay carreteras de acceso al interior y no hay senderos establecidos; hace falta autorización previa de la Forestry Development Authority y guías del parque. Esto no es un desvío de medio día: es una expedición de varios días con porteadores, desde Greenville. Ha sufrido tala ilegal, caza furtiva y, tras 2003, una fiebre del oro que metió a miles de ocupantes ilegales hasta su desalojo en 2005. El perro no entra bajo ningún concepto.",
         credit="Raimond Spekking · CC BY-SA 4.0", source=W + "Zwergflusspferd%20-%20Pygmy%20Hippopotamus%20-%20Hexaprotodon%20liberiensis.jpg?width=900"),
    dict(n=10, name="Harper y Cabo Palmas · las mansiones en ruinas", cat="Patrimonio", prio="Alta", dog="permitido", time="2 días",
         lat=4.3758, lon=-7.7008,
         desc="El rincón más extraordinario y más difícil de alcanzar de Liberia: la punta suroriental del país, en Cabo Palmas, a un paso de Costa de Marfil. Harper fue la capital de la República de Maryland, un estado independiente fundado por colonos afroamericanos de Maryland que existió por su cuenta entre 1834 y 1857, cuando se anexionó a Liberia. Sus barrios antiguos están construidos a imagen de las plantaciones del sur de Estados Unidos, y el reportaje de Smithsonian Magazine que mejor lo ha contado dice que «ningún lugar captura el mundo ambiguo de los américo-liberianos mejor que Harper, cuyos barrios más antiguos recuerdan a Nueva Orleans». Hoy son mansiones señoriales tragadas por la selva, con columnas, galerías y buhardillas americanas cayéndose a pedazos: la mansión arruinada del presidente William Tubman —que nació aquí— y la Logia Masónica son las dos piezas mayores. ACCESO: es notoriamente difícil por tierra. La propia documentación del lugar describe el transporte a Monrovia por agua —de tres a seis días en piragua vía Greenville— antes que por carretera, lo que dice todo sobre el estado de la vía costera del sureste. Ver el bloque de pistas 4x4.",
         credit="Wikimedia Commons", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
    # ===== CORREDOR HIPOTÉTICO B · INTERIOR, DE SURESTE A NORESTE =====
    dict(n=11, name="Zwedru (Grand Gedeh)", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=6.0667, lon=-8.1333,
         desc="Capital del condado de Grand Gedeh, a 435 km de Monrovia, cerca del río Cavalla y de la frontera marfileña: unos 24.000 habitantes krahn, mandingo, grebo, fulani, gio y mano, y el principal nudo de transporte del interior sureste. Es la ciudad natal de Samuel Doe, el sargento que dio el golpe de Estado de 1980 y puso fin a 133 años de dominio américo-liberiano, y que invirtió aquí en infraestructuras durante su mandato. Tiene aeródromo de tierra, tres emisoras locales, cobertura móvil de Lonestar y Orange, y un campus universitario. Para el viajero es la parada obligada entre Harper y Ganta: la carretera Zwedru-Ganta son 238 km y es el eje principal del interior sureste.",
         credit="Wikimedia Commons", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
    dict(n=12, name="Ganta · el nudo del noreste", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=7.2333, lon=-8.9833,
         desc="Segunda ciudad más poblada de Liberia (unos 41.000 habitantes en 2008) en el condado de Nimba, a 323 km de Monrovia y justo en la frontera guineana, que aquí marca el río Mano. Es un mercado fronterizo en ebullición, con cinco bancos, hoteles y el Ganta Hospital, que atiende a unas 450.000 personas de todo el condado. Su mezquita blanca de minaretes decorados es el edificio más reconocible. Ganta es el cruce de todo: al norte, Guinea y Nzérékoré; al este, la salida a Costa de Marfil por Loguatuo y Danané; al sur, los 238 km a Zwedru; al oeste, Gbarnga y Monrovia. Es la última ciudad con servicios completos antes de cualquiera de las tres fronteras del noreste y el punto donde se reposta a fondo.",
         credit="Wikimedia Commons", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
    dict(n=13, name="Yekepa y el monte Nimba liberiano", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=7.5833, lon=-8.5333,
         desc="CORRECCIÓN IMPORTANTE RESPECTO A VERSIONES ANTERIORES DE ESTA FICHA: el lado liberiano del macizo de Nimba NO forma parte del Patrimonio Mundial de la UNESCO. La inscripción de la Reserva Natural Integral del Monte Nimba cubre 17.632 ha repartidas solo entre Guinea (12.540 ha) y Costa de Marfil (5.000 ha); la propia documentación de la UNESCO explica que la parte liberiana quedó EXCLUIDA de la protección porque está «muy degradada por antiguas actividades mineras». Esa minería es Yekepa: la ciudad-mina que construyó la LAMCO sueco-americana en los años sesenta para explotar el hierro del Nimba, con su ferrocarril de 250 km hasta el puerto de Buchanan. Del lado liberiano el espacio protegido es la Reserva Natural de Nimba Este, mucho más reciente y modesta — POR CONFIRMAR su régimen de visita, tasas y guías con la Forestry Development Authority. Lo que sí ofrece la zona es paisaje de montaña, aire fresco, bosque de ladera y la memoria industrial de una company town entera construida en la selva. Coordenada aproximada.",
         credit="Guy Debonnet · CC BY-SA 3.0 IGO", source=W + "Mount%20Nimba%20Strict%20Nature%20Reserve-108453.jpg?width=900"),
    dict(n=14, name="Gbarnga (Bong)", cat="Ciudad · servicios", prio="Baja", dog="permitido con condiciones", time="1 noche",
         lat=6.9956, lon=-9.4722,
         desc="Capital del condado de Bong, en el centro geográfico del país, a mitad de camino entre Monrovia y Ganta por la carretera asfaltada principal. Durante la primera guerra civil fue la capital de facto del territorio controlado por Charles Taylor y su Frente Patriótico Nacional, la llamada «Gran Liberia» — un dato incómodo que forma parte de la historia del lugar y que conviene conocer antes de sacarlo en una conversación. Hoy es una ciudad de mercado y de universidad (Cuttington University, una de las más antiguas de África occidental, está a pocos kilómetros), con combustible, banco y hospital. Es la base para las cataratas de Kpatawee y el punto medio natural de la travesía interior.",
         credit="Wikimedia Commons", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
    dict(n=15, name="Cataratas de Kpatawee", cat="Naturaleza", prio="Media", dog="permitido con precaución", time="½ día",
         lat=6.9667, lon=-9.6167,
         desc="La cascada más conocida de Liberia y la excursión clásica del interior: un salto de unos 25 m sobre roca, en el condado de Bong, a media hora larga de Gbarnga por pista, rodeado de bosque y con una poza al pie donde se puede nadar. Hay un pequeño complejo de bungalows y zona recreativa que ha ido abriendo y cerrando según el momento. El caudal es muy estacional: espectacular en plena estación húmeda y modesto al final de la seca. Acceso por pista de laterita desde la carretera principal Monrovia-Gbarnga, exigente en lluvias. Es apto para el perro —no es espacio protegido con fauna mayor— con correa en la roca mojada. COORDENADA APROXIMADA: no se ha podido verificar en fuente cartográfica, confirmar sobre el terreno.",
         credit="Wikimedia Commons", source=W + "Robertsport%20Beach%2C%20Cape%20Mount%20County.jpg?width=900"),
    dict(n=16, name="Bosque de Gola liberiano (frontera con Sierra Leona)", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=7.4000, lon=-10.7000,
         desc="La continuación al sur del Parque Nacional de Gola Rainforest sierraleonés, con el que forma un bloque transfronterizo de selva primaria de Alto Guinea gestionado en cooperación entre los dos países: chimpancé occidental, hipopótamo pigmeo, elefante de bosque y una avifauna excepcional. Del lado sierraleonés, Gola entró en 2025 en la lista del Patrimonio Mundial de la UNESCO dentro del complejo Gola-Tiwai; del lado liberiano el proceso de protección ha ido por detrás y existe además el proyecto del Parque Nacional de Lofa-Mano en la misma franja. POR CONFIRMAR el estatus legal exacto, el régimen de visita y quién lo gestiona sobre el terreno. Acceso desde la zona de Kongo/Bopolu o desde el norte del condado de Gbarpolu, por pistas forestales. Es el gran comodín natural del oeste liberiano y la pieza que conectaría, sobre el mapa, este país con el bucle sierraleonés. Coordenada aproximada.",
         credit="Raimond Spekking · CC BY-SA 4.0", source=W + "Zwergflusspferd%20-%20Pygmy%20Hippopotamus%20-%20Hexaprotodon%20liberiensis.jpg?width=900"),
    dict(n=17, name="Loguatuo · la salida hacia Costa de Marfil", cat="Ciudad · servicios", prio="Baja", dog="permitido con condiciones", time="½ día",
         lat=7.2833, lon=-8.1667,
         desc="El paso fronterizo del noreste, a unos 40 km de Ganta, por el que se sale hacia Danané y Man, en el oeste de Costa de Marfil. Sería la salida natural del corredor liberiano si el país estuviera en la ruta, y el punto donde el itinerario volvería a engancharse con el trazado marfileño ya previsto. Mismos avisos que en toda frontera de la región: cruzar de día, tener el CPD o el permiso temporal en regla, el seguro Brown Card de la CEDEAO vigente y el certificado de fiebre amarilla a mano. POR CONFIRMAR horarios y si sella CPD. Coordenada aproximada.",
         credit="Wikimedia Commons", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
]

_CAT_COLOR = {
    "ciudad · servicios": "azul", "costa": "turquesa", "costa · surf": "turquesa",
    "naturaleza": "verde", "naturaleza · frontera": "verde",
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
    ("Frontera · BLOQUEADA para nosotros — Bo-Waterside / Jendema (desde Sierra Leona)", "Frontera", 6.8500, -11.2500,
     "Puesto principal del oeste, con tráfico comercial denso de camiones y autobuses. Operativo y funcional — pero no para un pasaporte español sin visado estampado previo: el visado electrónico liberiano solo se expide en el aeropuerto internacional de Monrovia, no en frontera terrestre. Con visado consular en mano, es el paso más lógico desde Sierra Leona."),
    ("Frontera · BLOQUEADA para nosotros — Ganta / Nzérékoré (desde Guinea)", "Frontera", 7.2333, -8.9833,
     "Paso del noreste desde la Guinea forestal, marcado por el río Mano. Sería la entrada natural si Liberia se insertara entre Guinea y Costa de Marfil, que es exactamente el hueco que el proyecto ha tenido que cerrar saltando directo de Guinea a Costa de Marfil por N'Zo/Gbapleu. Mismo bloqueo de visado."),
    ("Frontera · Salida hipotética — Loguatuo / Ganta (hacia Danané, Costa de Marfil)", "Frontera", 7.2833, -8.1667,
     "Paso principal hacia el oeste marfileño. Sería la salida del corredor liberiano y el punto de reenganche con el trazado ya previsto de Costa de Marfil. POR CONFIRMAR horarios y sellado de CPD. Coordenada aproximada."),
    ("Embajada de Liberia en Conakry (Guinea) · LA VÍA DE SOLUCIÓN", "Consular", 9.5350, -13.6750,
     "PIEZA CLAVE DE ESTA FICHA. Liberia mantiene embajada en Conakry, en Freetown, en Abiyán, en Accra y en Dakar. Cualquiera de ellas puede, en principio, estampar un visado en el pasaporte antes de llegar a la frontera terrestre, que es exactamente lo que el visado electrónico no resuelve. Conakry es la más útil para nosotros porque el corredor del proyecto pasa por allí, y porque coincide con la parada donde ya hay que tramitar otros visados del bloque. POR CONFIRMAR por teléfono o correo: si expide a extranjeros NO residentes en Guinea, requisitos, plazo de tramitación y coste. Coordenada urbana aproximada — localizar la dirección exacta al confirmar."),
    ("Embajada de Liberia en París (cubre España)", "Consular", 48.8566, 2.3522,
     "Liberia NO tiene embajada en España: la demarcación corresponde a su embajada en París, que cubre además Bulgaria, Chipre, Grecia, Mónaco, Portugal, Suiza y la UNESCO. Es la vía para sacar el visado ANTES de salir de Barcelona. El problema es de calendario, no de trámite: un visado turístico suele tener una ventana de validez de tres meses desde su emisión, y Liberia caería en el tercer o cuarto mes de la bajada — es decir, probablemente caducado antes de llegar. POR CONFIRMAR si existe una modalidad de validez larga o de entrada diferida. Coordenada de referencia de París."),
    ("Embajada de España en Abidjan (cobertura de Liberia)", "Consular", 5.3600, -3.9700,
     "Impasse Ablaha Pokou, Cocody Danga Nord, Abiyán. +225 22 44 48 50 · emb.abidjan@maec.es. España no tiene embajada en Monrovia desde 1990: la referencia consular para cualquier incidencia grave en Liberia está en Costa de Marfil."),
    ("John F. Kennedy Medical Center — Monrovia", "Hospital", 6.2900, -10.7600,
     "Principal hospital de referencia del país. Capacidad limitada para politraumatismos graves; la evacuación realista es a Accra, a Dakar o a Europa. Coordenada urbana aproximada."),
    ("Ganta Hospital — Nimba", "Hospital", 7.2333, -8.9833,
     "Atiende a unas 450.000 personas del condado de Nimba y de la región fronteriza: la única referencia sanitaria seria de todo el noreste."),
    ("Combustible · Monrovia", "Combustible", 6.3131, -10.8014,
     "Mejor oferta y calidad del país (Total, Aminata, Srimex/LPRC). Repostar a fondo aquí antes de cualquier tramo interior o del sureste."),
    ("Combustible · Buchanan, Gbarnga, Ganta, Zwedru", "Combustible", 5.8800, -10.0500,
     "Estaciones formales en las ciudades del eje asfaltado Monrovia-Gbarnga-Ganta y en Buchanan. Zwedru tiene suministro pero irregular. Buchanan es el último repostaje seguro antes del sureste."),
    ("Combustible · sureste (Greenville, Harper) — INCIERTO", "Combustible", 5.0167, -9.0333,
     "AVISO SERIO: entre Buchanan y Harper, pasando por Greenville, no hay ninguna garantía de suministro formal y buena parte del combustible se compra en garrafa a pie de carretera. Con los ~600 km de vía costera del sureste en el estado en que están, este es el tramo de mayor riesgo logístico de todo el país. Autonomía completa y garrafas llenas desde Buchanan."),
    ("Agua · Monrovia y ciudades del eje asfaltado", "Agua potable", 6.3131, -10.8014,
     "Agua embotellada en supermercados de Monrovia y en las ciudades del eje Gbarnga-Ganta. Para el depósito de uso general, estaciones de servicio, hoteles y misiones permiten llenar con manguera. Nunca beber del grifo."),
    ("Agua · sureste y Sapo", "Agua potable", 5.4000, -8.8000,
     "En el sureste y en la aproximación a Sapo no hay ningún punto fiable: agua de río tratada con filtro mecánico más tratamiento químico o ebullición. Salir de Greenville con toda la reserva llena. Paradoja: es el país más lluvioso de la región y a la vez uno de los más difíciles para conseguir agua potable fuera de la capital."),
]

DRONE_CALLOUT = ("warn", "Sin procedimiento turístico publicado: tratar como restringido y no volar sin autorización escrita",
                  "No se ha localizado normativa pública específica para visitantes con dron en Liberia. La autoridad competente es la Liberia Civil Aviation Authority (LCAA). Criterio del proyecto: solicitar autorización previa por escrito o, en su defecto, no volar. En ningún caso sobrevolar Monrovia (puerto franco, aeropuerto Roberts, Mamba Point y el barrio diplomático, edificios de gobierno), las instalaciones de Firestone en Harbel, las minas y el ferrocarril de hierro de Yekepa-Buchanan, ni las zonas núcleo de Sapo y del Nimba.")

STARLINK_CALLOUT = ("ok", "Starlink ACTIVO en Liberia",
                     "Liberia figura entre los mercados africanos con servicio Starlink operativo a mediados de 2026, con tarifas fijadas directamente en dólares (unos 55 USD/mes de servicio residencial y unos 390 USD el kit estándar en las fuentes consultadas). Sería una herramienta muy útil en un país donde el sureste está literalmente incomunicado. Revisar el mapa oficial 30-60 días antes. SIM local (Orange Liberia, Lonestar/MTN) como base urbana; el dólar estadounidense circula como moneda legal junto al dólar liberiano, lo que simplifica los pagos.")

DOG_MATRIX = [
    ("Entrada en el país", "no confirmado — irrelevante mientras el visado bloquee la entrada",
     "No se ha localizado ninguna fuente oficial sobre importación de animales de compañía en Liberia. Preparación mínima por analogía regional: microchip, pasaporte europeo, rabia en vigor con menos de 12 meses y certificado veterinario internacional reciente. La autoridad probable es el Ministerio de Agricultura liberiano — POR CONFIRMAR. Nota operativa: este punto solo se investiga a fondo SI el problema del visado se resuelve; mientras tanto es trabajo que no toca hacer."),
    ("Parque Nacional de Sapo (todo el parque)", "prohibido",
     "Selva primaria con chimpancés, elefante de bosque e hipopótamo pigmeo, y acceso exclusivamente a pie con autorización de la Forestry Development Authority. El perro no entra bajo ningún concepto, y además la visita es una expedición de varios días: PLAN B obligatorio, dejarlo en Greenville o en Monrovia con cuidador y hacer turnos entre los viajeros. Es el caso más claro de todo el país."),
    ("Reserva de Nimba Este (Yekepa) y bosque de Gola liberiano", "no confirmado — tratar como prohibido",
     "Espacios con grandes simios y con régimen de gestión poco documentado. Planificar como prohibido y confirmar por escrito con la Forestry Development Authority si alguna vez se activa el país."),
    ("Robertsport, lago Piso y playas de Grand Bassa", "permitido",
     "Playas abiertas, pueblos de pescadores y laguna: es lo mejor que tendría Liberia para el perro. Arena kilométrica y vacía en Robertsport y en Buchanan. Correa cerca de las barcas y de los tendederos de pescado, y precaución en las salidas en piragua por el lago Piso."),
    ("Harbel (plantación de Firestone)", "permitido con condiciones",
     "Es propiedad privada industrial atravesada por carretera pública: se pasa, no se pasea. Perro dentro del vehículo en el tramo de plantación."),
    ("Monrovia, Buchanan, Gbarnga, Ganta, Zwedru (ciudades)", "permitido con condiciones",
     "Sin restricción legal identificada. Correa siempre: mucho perro callejero, tráfico caótico en Monrovia y humedad extrema —es la capital más lluviosa del mundo—. Confirmar la política del alojamiento por teléfono. Nunca dejarlo solo en el vehículo."),
    ("Sureste (Greenville-Harper)", "permitido con precaución",
     "No hay restricción, pero sí hay un problema práctico: es el tramo con peor acceso sanitario del país y no hay veterinario en cientos de kilómetros. Si el perro tiene un problema en la vía costera del sureste, no hay solución cercana."),
]

SOURCES = [
    ("Wikipedia · Política de visados de Liberia: eVisa desde el 11 de marzo de 2025, expedida ÚNICAMENTE en el aeropuerto internacional de Monrovia", "https://en.wikipedia.org/wiki/Visa_policy_of_Liberia"),
    ("Wikipedia · Misiones diplomáticas de Liberia (embajadas en Conakry, Freetown, Abiyán, Accra y Dakar; España cubierta desde París)", "https://en.wikipedia.org/wiki/List_of_diplomatic_missions_of_Liberia"),
    ("Wikipedia · Liberia (clima, estación de lluvias mayo-octubre, red viaria: 10.590 km de los que solo ~657 km asfaltados)", "https://en.wikipedia.org/wiki/Liberia"),
    ("Wikipedia · Monrovia: la capital más lluviosa del mundo, 4.600 mm anuales; barrios, puerto y aeropuertos", "https://en.wikipedia.org/wiki/Monrovia"),
    ("Wikipedia · Parque Nacional de Sapo: 1.804 km², acceso solo a pie, autorización de la Forestry Development Authority, fauna", "https://en.wikipedia.org/wiki/Sapo_National_Park"),
    ("UNESCO · Reserva Natural Integral del Monte Nimba: la parte liberiana NO está inscrita, «muy degradada por antiguas actividades mineras»", "https://whc.unesco.org/en/list/155/"),
    ("Wikipedia · Robertsport: olas de izquierdas, Cape Mount, Tubman Center en ruinas, 80 km de Monrovia", "https://en.wikipedia.org/wiki/Robertsport"),
    ("Wikipedia · Lago Piso: sitio Ramsar n.º 1306 (2003), 103 km², área importante para las aves", "https://en.wikipedia.org/wiki/Lake_Piso"),
    ("Wikipedia · Providence Island, Liberia: desembarco de 1822, Contrato Ducor, candidatura UNESCO de 2017", "https://en.wikipedia.org/wiki/Providence_Island,_Liberia"),
    ("Wikipedia · Harper, Liberia: capital de la República de Maryland (1834-1857), mansiones américo-liberianas, acceso por agua", "https://en.wikipedia.org/wiki/Harper,_Liberia"),
    ("Wikipedia · Buchanan: puerto, ferrocarril del hierro desde Yekepa, playas y lagunas", "https://en.wikipedia.org/wiki/Buchanan,_Liberia"),
    ("Wikipedia · Greenville, Liberia: puerto de Sinoe, 185 días de lluvia al año, puerta de Sapo", "https://en.wikipedia.org/wiki/Greenville,_Liberia"),
    ("Wikipedia · Ganta: segunda ciudad, frontera del río Mano, 238 km a Zwedru, Ganta Hospital", "https://en.wikipedia.org/wiki/Ganta,_Liberia"),
    ("Wikipedia · Zwedru: 435 km de Monrovia, nudo del interior sureste, cobertura Lonestar y Orange", "https://en.wikipedia.org/wiki/Zwedru"),
    ("Wikipedia · Firestone Natural Rubber Company: Harbel, un millón de acres, concesión de 1926 y renegociación de 2005", "https://en.wikipedia.org/wiki/Firestone_Natural_Rubber_Company"),
    ("Digital Logistics Capacity Assessment · paso fronterizo de Bo-Waterside", "https://lca.logcluster.org/2315-liberia-border-crossing-bo-waterside-sierra-leone"),
    ("tech.africa · disponibilidad de Starlink en África (junio 2026): Liberia activo, con tarifas en dólares", "https://tech.africa/starlink-africa/"),
    ("Wikipedia · Embajada de España en Liberia (cerrada desde 1990, cobertura desde Abidjan)", "https://es.wikipedia.org/wiki/Embajada_de_Espa%C3%B1a_en_Liberia"),
    ("Embajada de España en Abidjan · consulados y demarcación", "https://www.exteriores.gob.es/Embajadas/abidjan/es/Embajada/Paginas/Consulados.aspx"),
    ("Comisión Europea · animales de compañía (requisitos de reentrada en la UE)", "https://europa.eu/youreurope/citizens/travel/carry/pets-and-other-animals/index_es.htm"),
    ("iOverlander · puntos de combustible, agua y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Corredor hipotético A · costa: Bo-Waterside -> Robertsport -> Monrovia -> Harbel -> Buchanan -> Greenville -> Sapo -> Harper
CORRIDOR = [
    (6.8500, -11.2500),   # Bo-Waterside (entrada desde Sierra Leona)
    (6.7500, -11.3667),   # Robertsport
    (6.7353, -11.2511),   # Lago Piso
    (6.3131, -10.8014),   # Monrovia
    (6.2833, -10.3500),   # Harbel (Firestone)
    (5.8800, -10.0500),   # Buchanan
    (5.0167, -9.0333),    # Greenville
    (5.4111, -8.4146),    # Parque Nacional de Sapo
    (4.3758, -7.7008),    # Harper (Cabo Palmas)
]

# Corredor hipotético B · interior: Harper -> Zwedru -> Ganta -> Gbarnga -> Kpatawee -> Ganta -> Yekepa -> Loguatuo
CORRIDOR_ALT = [
    (4.3758, -7.7008),    # Harper
    (6.0667, -8.1333),    # Zwedru
    (7.2333, -8.9833),    # Ganta
    (6.9956, -9.4722),    # Gbarnga
    (6.9667, -9.6167),    # Cataratas de Kpatawee
    (6.9956, -9.4722),    # Gbarnga (vuelta)
    (7.2333, -8.9833),    # Ganta
    (7.5833, -8.5333),    # Yekepa / Nimba liberiano
    (7.2833, -8.1667),    # Loguatuo (salida a Costa de Marfil)
]

CORRIDOR_LABEL = "Hipotético · costa y sureste"
CORRIDOR_ALT_LABEL = "Hipotético · regreso por el interior"

EXPERIENCIAS = [
    "El visado es el muro, y conviene entender exactamente dónde está. Liberia puso en marcha el 11 de marzo de 2025 un sistema de visado electrónico que se anunció como una gran apertura al turismo, y lo es — para quien llega en avión. La letra pequeña es que ese visado electrónico «a la llegada» SOLO se expide en el aeropuerto internacional de Monrovia. Quien llega por carretera necesita un visado estampado por una misión diplomática liberiana antes de presentarse en la frontera. Para un viaje overland es exactamente el peor diseño posible, y es la razón por la que este país está fuera de la ruta.",
    "La vía de solución existe y está identificada: Liberia tiene embajada en CONAKRY, en Freetown, en Abiyán, en Accra y en Dakar. Es decir, en cuatro de las capitales por las que pasa o casi pasa nuestro itinerario. Sacar el visado en Conakry, durante la parada que de todas formas hay que hacer allí para otros trámites, sería el camino natural. Lo que falta por confirmar es lo de siempre en África occidental: si esa embajada expide a extranjeros NO residentes en Guinea, en cuánto tiempo y por cuánto dinero. Esas tres respuestas son las que deciden si Liberia vuelve o no a la ruta.",
    "Sacarlo en España no funciona bien por calendario, no por trámite. Liberia no tiene embajada en España: nos cubre su embajada en París. Se podría pedir antes de salir de Barcelona, pero un visado turístico suele venir con una ventana de validez de unos tres meses desde la emisión, y Liberia caería en el tercer o cuarto mes de la bajada — probablemente caducado al llegar. Salvo que exista una modalidad de validez larga, la solución real es en ruta.",
    "El sureste es el tramo que asusta de verdad, y no por seguridad. La documentación del propio Harper describe el trayecto a Monrovia por AGUA —de tres a seis días en piragua vía Greenville— antes que por carretera. Cuando una fuente describe la piragua como la forma normal de llegar a una capital de condado, ya sabes en qué estado está la vía costera. Sumado a que el país tiene unos 10.600 km de red con apenas 657 asfaltados (un 6 %), el corredor Buchanan-Greenville-Harper es el tramo más comprometido que tendría Liberia.",
    "Monrovia es la capital más lluviosa del mundo: 4.600 mm de media anual. No es un dato de curiosidad, es una restricción de calendario. Con la estación húmeda de mayo a octubre y esa cantidad de agua, el sureste queda directamente descartado media parte del año, y Sapo —al que solo se entra a pie— con más motivo todavía.",
    "Sapo no es un desvío, es una expedición. Es la segunda selva primaria continua de África occidental y no tiene carreteras de acceso al interior ni senderos establecidos: se entra a pie, con autorización previa de la Forestry Development Authority y guías del parque, desde Greenville. Quien quiera ver hipopótamo pigmeo —fotografiado aquí por primera vez en el país en 2008— tiene que contar con varios días, porteadores y una preparación que no se improvisa sobre la marcha.",
    "Robertsport es el sitio del que todo el mundo habla bien, y está a 16 km de la frontera de Sierra Leona. Cinco o seis olas de izquierdas con nombre propio rompiendo bajo un promontorio de granito, entre el Atlántico y la laguna del lago Piso. La ironía de la ruta es notable: el mejor punto de Liberia está pegado a Sierra Leona, que SÍ da visado en frontera terrestre y SÍ está documentada como alternativa viable en esta guía.",
    "CORRECCIÓN QUE HAY QUE TENER PRESENTE: el lado liberiano del monte Nimba no es Patrimonio de la UNESCO. La inscripción cubre solo Guinea y Costa de Marfil, y la propia UNESCO explica que la parte liberiana quedó excluida porque está muy degradada por la minería antigua. Versiones anteriores de esta ficha —y muchas guías— lo daban por incluido.",
    "PENDIENTE HONESTO: no se ha localizado ningún relato de un overlander que haya entrado en Liberia por tierra con visado estampado y vehículo propio después de la reforma de 2025, ni ninguno que lo haya hecho con animal de compañía. Como el país está fuera de la ruta, tampoco tiene sentido invertir esfuerzo en buscarlo — pero si alguien de la comunidad overland aporta ese dato, es lo que reabriría el expediente.",
]

HISTORIA_RESUMEN = ("Liberia es un caso único en África: nunca fue colonia europea, sino un estado fundado por antiguos esclavos afroamericanos reasentados desde 1822 con apoyo de sociedades de colonización estadounidenses, que en 1847 proclamaron "
                     "la primera república del continente. Esa élite américo-liberiana gobernó sobre la mayoría indígena durante 133 años, hasta el golpe de Samuel Doe en 1980; siguieron dos guerras civiles devastadoras (1989-2003) con unos 250.000 muertos, "
                     "la primera presidenta electa de África en 2005 y el brote de ébola de 2014-2016. Hoy es una democracia frágil pero funcional, con alternancias pacíficas en 2018 y 2024.")

HISTORIA_SECCIONES = [
    ("Un proyecto de colonización afroamericana (1822)",
     "La American Colonization Society, con apoyo de figuras políticas estadounidenses y bajo una premisa profundamente controvertida ya en su época —que el regreso a África era la solución al «problema racial» de Estados Unidos—, empezó a reasentar en la costa de la actual Liberia a antiguos esclavos y afroamericanos libres. El desembarco fundacional fue en 1822 en Providence Island, en la desembocadura del Mesurado, tras el llamado Contrato Ducor, firmado con jefes gola, dei y kru que, según la documentación histórica, no compartían el concepto europeo de propiedad de la tierra y creían estar cediendo su uso, no vendiéndola. La capital se llamó Monrovia en honor al presidente estadounidense James Monroe. En paralelo surgieron otros asentamientos con sus propios patrocinadores: la Maryland Colonization Society fundó Harper en Cabo Palmas, que llegó a ser la República de Maryland, un estado independiente entre 1834 y 1857."),
    ("Independencia en 1847 y 133 años de dominio américo-liberiano",
     "Liberia se declaró independiente en 1847, la primera república de África. Pero el poder quedó en manos de la minoría américo-liberiana —descendientes de los colonos, apenas un pequeño porcentaje de la población— que gobernó durante 133 años bajo un único partido, el True Whig Party, con constitución, bandera y arquitectura calcadas de las de Estados Unidos, marginando política y económicamente a los pueblos indígenas del interior. Las mansiones en ruinas de Harper son el retrato físico de ese mundo. La economía se hipotecó en 1926, cuando el gobierno arrendó a Firestone un millón de acres durante 99 años a seis centavos el acre para plantar la que sigue siendo la mayor explotación continua de caucho del planeta."),
    ("El golpe de Samuel Doe (1980) y las dos guerras civiles",
     "En 1980 el sargento Samuel Doe, natural de Zwedru, derrocó y ejecutó al presidente William Tolbert en un golpe sangriento que puso fin al dominio américo-liberiano, pero abrió una etapa de autoritarismo e inestabilidad étnica. En 1989 Charles Taylor entró desde Costa de Marfil y desencadenó la primera guerra civil; Doe fue capturado y asesinado en 1990. Siguió una segunda guerra (1999-2003). Entre ambas dejaron alrededor de 250.000 muertos, un país arrasado y el uso masivo y sistemático de niños soldado. Taylor, que llegó a gobernar desde Gbarnga y después desde Monrovia, financió además a la guerrilla del RUF en Sierra Leona: las dos guerras fueron, en la práctica, un mismo conflicto regional. Fue condenado en 2012 por el Tribunal Especial para Sierra Leona. Esto se cuenta con seriedad porque está a una generación de distancia y porque el país entero se reconstruyó desde cero después."),
    ("Ellen Johnson Sirleaf, el ébola y la reconstrucción",
     "Tras el fin de la guerra en 2003 y el despliegue de la misión de paz de la ONU, Liberia eligió en 2005 a Ellen Johnson Sirleaf, la primera mujer elegida jefa de Estado en África, Nobel de la Paz en 2011, que gobernó hasta 2018. Su mandato afrontó el brote de ébola de 2014-2016, uno de los peores de la historia, que golpeó a Liberia con especial dureza —más de 4.800 muertos—, cerró el país durante meses y devastó un sistema sanitario ya frágil. El país fue declarado libre de transmisión en 2016."),
    ("Situación actual",
     "Liberia ha encadenado desde entonces dos transferencias pacíficas de poder por las urnas: George Weah (2018-2023), el futbolista que ganó el Balón de Oro, y Joseph Boakai desde 2024. La economía combina agricultura (casi el 39 % del PIB), caucho —Firestone sigue siendo el mayor empleador privado del país—, hierro y aceite de palma, con una tasa de empleo formal de apenas el 15 %. Circulan como moneda legal tanto el dólar liberiano como el dólar estadounidense. El inglés es la lengua oficial, con más de veinte lenguas indígenas —kpelle, bassa, vai, kru, mandingo— habladas a diario. Para el viajero, el país es hoy estable y sin conflicto activo: el problema de Liberia en este proyecto es puramente administrativo."),
]

HISTORIA_FUENTES = [
    ("BBC News · Liberia country profile", "https://www.bbc.com/news/world-africa-13729504"),
    ("Encyclopaedia Britannica · Liberia, History", "https://www.britannica.com/place/Liberia/History"),
    ("Nobel Prize · Ellen Johnson Sirleaf", "https://www.nobelprize.org/prizes/peace/2011/johnson_sirleaf/facts/"),
    ("Wikipedia · Liberia (situación política y económica actual)", "https://en.wikipedia.org/wiki/Liberia"),
    ("Wikipedia · Providence Island, Liberia (desembarco de 1822 y Contrato Ducor)", "https://en.wikipedia.org/wiki/Providence_Island,_Liberia"),
]

SPEC = dict(
    slug="liberia", name="Liberia", revision="12 sep 2026",
    sub="EXCLUIDA de la ruta fija · ficha informativa · el problema del visado terrestre y cómo se resolvería",
    chips=[
        ("ESTATUS", "EXCLUIDA DE LA RUTA FIJA — no se hace. Ficha informativa por si cambian las condiciones"),
        ("MOTIVO", "el eVisa liberiano SOLO se expide en el aeropuerto de Monrovia: no sirve en frontera terrestre"),
        ("QUÉ TENDRÍA QUE CAMBIAR", "conseguir visado ESTAMPADO en la Embajada de Liberia en Conakry (existe) antes de llegar"),
        ("SI SE RESOLVIERA", "entraría entre Guinea y Costa de Marfil, o entre Sierra Leona y Costa de Marfil · ~1.700 km / 14-18 días"),
        ("PDIs", "17 puntos repartidos entre el corredor costero y el interior (trazado hipotético)"),
        ("LO MEJOR", "Sapo, la 2.ª selva primaria de África occidental · Robertsport, surf de clase mundial · Harper y sus mansiones"),
        ("4x4", "vía costera del sureste (Buchanan-Greenville-Harper): el tramo más duro documentado de la región"),
        ("A PIE", "Sapo se recorre EXCLUSIVAMENTE a pie, con permiso de la FDA: expedición de varios días"),
        ("LLUVIA", "Monrovia es la capital MÁS LLUVIOSA DEL MUNDO: 4.600 mm/año. Húmeda de mayo a octubre"),
        ("CARRETERAS", "unos 10.600 km de red con apenas 657 asfaltados (6 %)"),
        ("STARLINK", "ACTIVO · el dólar estadounidense es moneda legal"),
        ("PERRO", "sin fuente localizada — trabajo aparcado mientras el visado bloquee la entrada"),
        ("SALUD", "fiebre amarilla obligatoria · malaria intensa · sin transmisión activa de ébola desde 2016"),
    ],
    center=[6.3, -9.5], zoom=7,
    notice="ESTE PAÍS ESTÁ EXCLUIDO DE LA RUTA FIJA. La ficha se mantiene completa y actualizada como información de reserva, por si el problema del visado se resolviera o cambiaran las condiciones. No planificar nada sobre ella sin haber cerrado antes el visado estampado.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("<strong>Liberia está fuera de la ruta fija, y el motivo es administrativo, no de seguridad ni de interés.</strong> El país es estable, cordial y tiene algunas de las piezas más fuertes de toda la costa atlántica: "
                   "<strong>Sapo</strong>, la segunda selva primaria continua de África occidental, con hipopótamo pigmeo y elefante de bosque; <strong>Robertsport</strong>, cinco olas de izquierdas de clase mundial junto a un lago Ramsar; "
                   "<strong>Harper</strong>, con las mansiones américo-liberianas pudriéndose bajo la selva en Cabo Palmas; y una historia que no se parece a la de ningún otro país del continente. "
                   "El problema es concreto y verificado: el <strong>visado electrónico liberiano, en vigor desde marzo de 2025, solo se expide en el aeropuerto internacional de Monrovia</strong>. Para entrar por carretera hace falta un "
                   "<strong>visado estampado previamente por una misión diplomática liberiana</strong>, y sin ese papel la frontera terrestre es una pared. "
                   "Esta ficha documenta el país entero —como si se fuera a hacer— y, sobre todo, documenta <strong>exactamente qué tendría que pasar para que volviera a la ruta</strong>."),
    decision=("<strong>ESTATUS: EXCLUIDA DE LA RUTA FIJA.</strong> Decisión del dueño del proyecto: «deja las fichas de Liberia y Gabón como alternativas por tener su información pero no lo haremos». "
              "La ficha se mantiene completa por dos razones: porque la información no se tira, y porque el motivo de la exclusión es <strong>reversible</strong> y conviene tener escrito cómo se revertiría.<br><br>"
              "<strong>EL PROBLEMA, EXACTAMENTE.</strong> Liberia lanzó el 11 de marzo de 2025 un sistema de visado electrónico que se presentó como una apertura al turismo. Lo es — para quien llega en avión. "
              "El documento que se obtiene por internet es un <strong>«visado electrónico a la llegada» que solo puede expedirse en el aeropuerto internacional de Monrovia</strong>. "
              "Quien llega por carretera queda fuera del sistema y necesita un <strong>visado estampado en el pasaporte por una misión diplomática liberiana</strong> antes de presentarse en Bo-Waterside o en Ganta. "
              "Para un viaje overland es el peor diseño posible, y por eso el proyecto saltó directamente de Guinea a Costa de Marfil por N'Zo/Gbapleu.<br><br>"
              "<strong>QUÉ TENDRÍA QUE CAMBIAR — la vía real, identificada en esta revisión.</strong> Liberia mantiene <strong>embajada en Conakry (Guinea)</strong>, y también en <strong>Freetown, Abiyán, Accra y Dakar</strong>. "
              "Cuatro de esas cinco capitales están en el itinerario o a un paso de él. La solución operativa sería <strong>tramitar el visado estampado en la Embajada de Liberia en Conakry</strong>, durante la parada que el corredor de bajada "
              "ya hace allí para otros visados del bloque. <strong>LO QUE FALTA POR CONFIRMAR son exactamente tres datos</strong>, y son baratos de conseguir con una llamada y un correo: "
              "(1) ¿expide visados a extranjeros <em>no residentes</em> en Guinea?; (2) ¿cuánto tarda la tramitación —días hábiles, y si retienen el pasaporte, que es el punto crítico con dos vehículos esperando—?; "
              "(3) ¿cuánto cuesta y qué requisitos pide (carta de invitación, reserva de hotel, itinerario, fotos)? "
              "No se ha podido verificar ninguna de las tres en fuentes públicas: <strong>son la tarea concreta que reabriría el expediente</strong>.<br><br>"
              "<strong>POR QUÉ NO SE SACA EN ESPAÑA.</strong> Liberia no tiene embajada en España; nos cubre la de <strong>París</strong>. Se podría pedir antes de salir, pero el obstáculo es de calendario: un visado turístico suele traer una "
              "ventana de validez de unos tres meses desde la emisión, y Liberia caería en el tercer o cuarto mes de la bajada — es decir, probablemente <strong>caducado al llegar</strong>. Salvo que exista una modalidad de validez larga o de "
              "entrada diferida (POR CONFIRMAR), la vía realista es en ruta.<br><br>"
              "<strong>DÓNDE ENCAJARÍA SI SE RESOLVIERA.</strong> Dos opciones, ambas limpias: <strong>(A)</strong> en la <strong>bajada</strong>, entre Guinea y Costa de Marfil — se entraría desde la Guinea forestal por Ganta y se saldría por "
              "Loguatuo hacia Danané, rellenando justamente el hueco que hoy se salta; <strong>(B)</strong> encadenada con el <strong>bucle de Sierra Leona</strong> en la subida, entrando por Bo-Waterside desde Jendema — que tiene la ventaja de "
              "que Robertsport está a 16 km de esa frontera. Coste estimado del país completo: <strong>~1.700 km y 14-18 días</strong>, condicionados por el estado de la vía costera del sureste.<br><br>"
              "<strong>DECISIÓN ABIERTA PARA EL DUEÑO:</strong> ¿merece la pena dedicar una llamada y un correo a la Embajada de Liberia en Conakry antes de salir, para tener la respuesta por escrito? Es trabajo de una tarde y es lo único que "
              "separa a este país de volver a estar sobre la mesa. Si la respuesta es que sí expiden a no residentes en 48-72 horas, Liberia deja de ser una alternativa teórica."),
    facts=[
        ("Estatus en la ruta", "EXCLUIDA de la ruta fija. Ficha informativa de reserva."),
        ("Motivo exacto de la exclusión", "El visado electrónico liberiano (vigente desde el 11 de marzo de 2025) SOLO se expide en el aeropuerto internacional de Monrovia. No sirve para entrar por carretera."),
        ("Qué tendría que cambiar", "Obtener un visado ESTAMPADO en una misión diplomática liberiana antes de llegar a la frontera. La más útil es la Embajada de Liberia en CONAKRY, que existe y está en el itinerario."),
        ("Datos que faltan para reabrir el expediente", "(1) si Conakry expide a no residentes; (2) plazo de tramitación y si retienen el pasaporte; (3) coste y requisitos. POR CONFIRMAR — ninguno verificado en fuentes públicas."),
        ("Por qué no en España", "Liberia no tiene embajada en España: cubre la de París. El problema sería la ventana de validez de ~3 meses frente a un viaje de 8."),
        ("Dónde encajaría", "(A) en la bajada, entre Guinea y Costa de Marfil, por Ganta y Loguatuo; (B) en la subida, encadenada con el bucle de Sierra Leona, por Bo-Waterside."),
        ("Coste estimado", "~1.700 km y 14-18 días, condicionados por el estado de la vía costera del sureste (Buchanan-Greenville-Harper)."),
        ("Calendario", "Solo en seca, de noviembre a abril. Monrovia es la capital más lluviosa del mundo (4.600 mm/año) y llueve de mayo a octubre."),
        ("Carreteras", "Unos 10.600 km de red con apenas 657 asfaltados (~6 %). El eje Monrovia-Gbarnga-Ganta está asfaltado; el sureste, no."),
        ("Seguridad", "Estable, sin conflicto activo, con alternancias pacíficas en 2018 y 2024. Precaución normal."),
        ("Salud", "Fiebre amarilla obligatoria. Malaria intensa. Sin transmisión activa de ébola desde 2016."),
        ("Comunicaciones y dinero", "Starlink ACTIVO. El dólar estadounidense es moneda de curso legal junto al dólar liberiano, lo que simplifica mucho los pagos."),
    ],
    alerts=[
        "EXCLUSIÓN: Liberia NO forma parte de la ruta fija. Nada de esta ficha debe planificarse ni reservarse mientras el visado terrestre no esté resuelto por escrito.",
        "EL PROBLEMA, EN UNA FRASE: el eVisa liberiano es un visado electrónico A LA LLEGADA que solo se expide en el aeropuerto internacional de Monrovia. En Bo-Waterside o en Ganta no sirve.",
        "LA SOLUCIÓN, EN OTRA: visado estampado en la Embajada de Liberia en Conakry (o Freetown, Abiyán, Accra, Dakar) antes de llegar a la frontera. Faltan por confirmar tres datos: si expide a no residentes, plazo y coste.",
        "Riesgo operativo del trámite consular: si la embajada retiene el pasaporte varios días, eso inmoviliza a los tres viajeros y a los dos vehículos en Conakry. Confirmar ESE punto antes que el precio.",
        "Vía costera del sureste (Buchanan-Greenville-Harper): la propia documentación de Harper describe el viaje a Monrovia en piragua, de tres a seis días, antes que por carretera. Es el tramo peor documentado y más comprometido de toda la región; en lluvias, directamente descartado.",
        "Parque Nacional de Sapo: se entra EXCLUSIVAMENTE A PIE, sin carreteras de acceso al interior ni senderos establecidos, con autorización previa de la Forestry Development Authority y guías del parque. Es una expedición de varios días desde Greenville, no un desvío.",
        "CORRECCIÓN de versiones anteriores de esta ficha: el lado LIBERIANO del monte Nimba NO está inscrito en el Patrimonio Mundial de la UNESCO. La inscripción cubre solo Guinea y Costa de Marfil; la parte liberiana quedó excluida por su degradación minera.",
        "Certificado internacional de fiebre amarilla obligatorio para entrar, sin excepciones.",
        "Sin embajada de España en Monrovia desde 1990: la referencia consular es la Embajada en Abidjan (Costa de Marfil), a un país de distancia.",
        "Drones: sin procedimiento turístico publicado. Criterio del proyecto, no volar sin autorización escrita de la LCAA.",
        "La guerra civil (1989-2003), con unos 250.000 muertos y uso masivo de niños soldado, y el ébola de 2014-2016 (más de 4.800 muertos) están a una generación de distancia. Materia sensible: no se fotografía, no se pregunta a la ligera, no se convierte en anécdota.",
    ],
    ruta_intro=("<strong>Trazado hipotético</strong>, documentado por si el país volviera a la ruta. Se plantea como una travesía en U: el <strong>corredor costero</strong> entra desde Sierra Leona por Bo-Waterside, baja por Robertsport, "
                "Monrovia, Harbel y Buchanan y se mete en el sureste hacia Greenville, Sapo y Harper; el <strong>corredor interior</strong> vuelve desde Harper por Zwedru y Ganta, con el desvío a Gbarnga y Kpatawee y la subida a Yekepa, "
                "y sale hacia Costa de Marfil por Loguatuo. Etapas calculadas sobre <strong>250 km/día</strong> en el eje asfaltado Monrovia-Gbarnga-Ganta, y reducidas a <strong>80-120 km/día</strong> en la vía costera del sureste, que es "
                "el factor que descuadra el cálculo entero. Si el sureste resultara impracticable —cosa probable fuera de la seca—, la versión corta del país (Robertsport, Monrovia, Buchanan, Gbarnga, Ganta, Nimba) son "
                "<strong>~800 km y 7-9 días</strong>, y se pierde Sapo y Harper, que son justo lo que hace especial a Liberia."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Costa 1 · Entrada", "Jendema (Sierra Leona) → Bo-Waterside → Robertsport", "~60 km · 1 día (con el trámite de frontera)"),
        ("Costa 2 · Surf y laguna", "Robertsport + lago Piso (piragua)", "~40 km locales · 2-3 días"),
        ("Costa 3 · A la capital", "Robertsport → Monrovia", "~130 km · 1 día"),
        ("Costa 4 · Monrovia", "Providence Island, Museo Nacional, Waterside, ruina del Ducor", "2-3 noches · trámites, taller, provisiones"),
        ("Costa 5 · El caucho", "Monrovia → Harbel (Firestone) → Buchanan", "~130 km · 1-2 días"),
        ("Costa 6 · Al sureste (el tramo duro)", "Buchanan → Greenville", "~230 km · 2-3 días — pista, confirmar estado"),
        ("Costa 7 · Sapo (expedición)", "Greenville → Sapo NP (a pie, con guías y permiso de la FDA) → Greenville", "~60 km al punto de partida + 3-5 días a pie"),
        ("Costa 8 · A Cabo Palmas", "Greenville → Harper", "~300 km · 3-4 días — el tramo peor documentado del país"),
        ("Interior 1 · Harper", "Mansiones américo-liberianas, Logia Masónica, casa de Tubman", "2 días"),
        ("Interior 2 · Hacia el norte", "Harper → Zwedru", "~270 km · 2 días"),
        ("Interior 3 · El eje de Nimba", "Zwedru → Ganta", "~238 km · 1-2 días"),
        ("Interior 4 · Desvío a las cataratas (OPCIONAL)", "Ganta → Gbarnga → Kpatawee → Gbarnga → Ganta", "~260 km ida y vuelta · 1-2 días"),
        ("Interior 5 · La montaña del hierro", "Ganta → Yekepa (Nimba liberiano) → Ganta", "~180 km ida y vuelta · 1-2 días"),
        ("Interior 6 · Salida", "Ganta → Loguatuo → Danané (Costa de Marfil)", "~40 km · ½-1 día"),
        ("VARIANTE CORTA (si el sureste está impracticable)", "Bo-Waterside → Robertsport → Monrovia → Buchanan → Gbarnga → Kpatawee → Ganta → Nimba → Loguatuo", "~800 km · 7-9 días — sin Sapo ni Harper"),
    ],
    offroad=[
        "Vía costera del sureste, Buchanan → Greenville → Harper (~530 km): el tramo 4x4 más serio que tendría Liberia y el peor documentado de esta parte de África. Laterita, vados, puentes de madera y tramos que en estación húmeda desaparecen. El indicio más elocuente del estado real de esta vía es que la documentación de Harper describe el trayecto a Monrovia en piragua —de tres a seis días vía Greenville— antes que por carretera. Solo tiene sentido en plena seca, con los dos vehículos juntos, autonomía completa de combustible desde Buchanan y varios días de margen en el calendario.",
        "Acceso a Sapo desde Greenville: pista de tierra hasta el punto donde se deja el vehículo — y ahí se acaba la conducción, porque al parque SOLO se entra a pie. No hay carreteras interiores ni senderos establecidos. La parte 4x4 es corta; la parte a pie es la expedición.",
        "Acceso a las cataratas de Kpatawee desde la carretera Monrovia-Gbarnga: pista de laterita corta pero exigente en lluvias, con la bajada final al río. Es la pista más accesible del país.",
        "Subida a Yekepa y al Nimba liberiano desde Ganta (~90 km): carretera minera de montaña, en general en mejor estado que la media del país precisamente por el tráfico de la explotación, con tramos de pista en la aproximación a la reserva. Atención al tráfico pesado y a los accesos restringidos de la concesión.",
        "Eje asfaltado Monrovia → Gbarnga → Ganta (~300 km): la única carretera principal en condiciones del país, y la columna vertebral de cualquier itinerario liberiano. Se hace en una jornada larga.",
        "Estacionalidad, resumen operativo: con unos 10.600 km de red y apenas 657 asfaltados (~6 %), y con la estación húmeda de mayo a octubre en el país más lluvioso de la región —4.600 mm anuales en Monrovia, 185 días de lluvia al año en Greenville—, todo lo que no sea el eje Monrovia-Ganta es un plan estricto de noviembre a abril.",
    ],
    senderismo=[
        "Parque Nacional de Sapo (3-5 días): la gran caminata del país y, de hecho, la ÚNICA forma de conocerlo. No hay carreteras de acceso al interior ni senderos establecidos: se entra a pie desde el borde, con autorización previa de la Forestry Development Authority, guías del parque y porteadores, desde Greenville. Selva primaria cerrada del bloque de Alto Guinea, con la mayor diversidad de mamíferos del mundo según Conservation International: chimpancé occidental, elefante de bosque, siete duikers y el hipopótamo pigmeo. No es un safari: es marchar por selva húmeda buscando rastros. Humedad extrema, sanguijuelas y noches en hamaca.",
        "Cabo Mount y el promontorio de Robertsport (~300 m): subida corta desde el pueblo al granito que domina la península, con vista sobre las cinco olas de izquierdas, el lago Piso y el Atlántico a los dos lados. Media mañana, apta para el perro.",
        "Monte Nimba liberiano (Yekepa): rutas de ladera hacia la cresta del macizo desde la zona de Yekepa. El lado liberiano no está inscrito en la UNESCO y está degradado por la minería antigua, pero sigue siendo montaña de verdad con bosque de ladera y aire fresco. POR CONFIRMAR el régimen de acceso de la Reserva Natural de Nimba Este con la Forestry Development Authority.",
        "Cataratas de Kpatawee: bajada a pie al pie del salto y a la poza, desde el aparcamiento. Corto y agradecido, y compatible con el perro.",
        "Bosque de Gola liberiano: caminatas de selva con guía comunitario en la franja fronteriza con Sierra Leona, en continuidad con el parque sierraleonés que la UNESCO inscribió en 2025. Régimen de visita POR CONFIRMAR.",
        "Orillas del lago Piso: además de la piragua, hay recorridos a pie por la orilla y por los manglares, con buena observación de aves — es área importante para las aves de BirdLife.",
    ],
    acampada=[
        "Robertsport: campamentos sencillos y alojamientos orientados al surf con sitio para los vehículos, junto a la playa. Es el mejor sitio del país para pernoctar con vehículo propio.",
        "Monrovia: aparcamiento vigilado obligatorio. Hoteles de Mamba Point y Sinkor con recinto cerrado; la densidad urbana y el tráfico hacen inviable dejar los vehículos sueltos.",
        "Buchanan y costa de Grand Bassa: playas aisladas y lagunas con posibilidad de vivac preguntando en el pueblo de pescadores más cercano. Zona tranquila.",
        "Sureste (Greenville, Harper): alojamiento muy básico en las dos ciudades y prácticamente nada entre medias. Preguntar siempre al jefe del pueblo antes de instalarse; es un tramo donde la hospitalidad rural es el sistema de alojamiento real.",
        "Sapo: dentro del parque se duerme en campamento de expedición con los guías, en hamaca o tienda. Los vehículos se quedan en Greenville o en el borde del parque — confirmar custodia con la FDA.",
        "Eje interior (Gbarnga, Ganta, Zwedru): hoteles sencillos con patio y aparcamiento en las tres ciudades. Ganta es la mejor plaza del noreste.",
        "Regla general: con 4.600 mm de lluvia anual en la costa, la acampada en Liberia es un ejercicio de gestión del agua. Toldo, suelo elevado y nada de montar en vaguadas.",
    ],
    visado=[
        "EL PUNTO QUE EXCLUYE AL PAÍS. Desde el 11 de marzo de 2025 Liberia dispone de un sistema de visado electrónico con respuesta en unos tres días y entrega por PDF o código QR. Pero ese visado electrónico SOLO PUEDE EXPEDIRSE EN EL AEROPUERTO INTERNACIONAL DE MONROVIA: es, en la práctica, un visado a la llegada por vía aérea. No habilita la entrada por frontera terrestre.",
        "PARA ENTRAR POR CARRETERA hace falta un visado ESTAMPADO por una misión diplomática liberiana antes de presentarse en el puesto. No hay atajo conocido: el sistema electrónico no cubre este caso.",
        "DÓNDE SE PUEDE CONSEGUIR EN RUTA: Liberia mantiene embajada en CONAKRY (Guinea), FREETOWN (Sierra Leona), ABIYÁN (Costa de Marfil, con acreditación también en Burkina Faso), ACCRA (Ghana, con acreditación en Togo) y DAKAR (Senegal, con acreditación en Cabo Verde, Gambia y Mauritania). Cuatro de esas cinco están en el itinerario del proyecto o a un paso.",
        "LA OPCIÓN MÁS PRÁCTICA SERÍA CONAKRY, porque el corredor de bajada ya para allí para tramitar otros visados del bloque. TRES DATOS POR CONFIRMAR, y son los que deciden todo: (1) si expide a extranjeros NO residentes en Guinea; (2) el plazo de tramitación y, sobre todo, SI RETIENEN EL PASAPORTE —con dos vehículos y tres personas esperando, ese es el riesgo real—; (3) el coste y los requisitos (carta de invitación, reserva, itinerario, fotos).",
        "DESDE ESPAÑA NO FUNCIONA BIEN: Liberia no tiene embajada en España y nos cubre la de PARÍS. El trámite sería posible, pero la ventana de validez habitual de un visado turístico (unos tres meses desde la emisión) no llega hasta el tercer o cuarto mes del viaje, que es cuando tocaría Liberia. POR CONFIRMAR si existe una modalidad de validez larga o de entrada diferida.",
        "Certificado internacional de fiebre amarilla obligatorio para entrar, expresamente exigido.",
        "Los ciudadanos de los 14 estados de la CEDEAO entran sin visado por 90 días — lo que explica por qué el tráfico regional cruza estas fronteras sin problema y por qué el diseño del sistema no tiene en cuenta al viajero extracomunitario por carretera.",
    ],
    fronteras_rows=[
        ("BLOQUEADA sin visado estampado", "Bo-Waterside / Jendema (desde Sierra Leona)", "Paso principal del oeste, con tráfico comercial denso. Operativo, pero inútil para nosotros sin visado consular previo: el eVisa solo vale en el aeropuerto de Monrovia. Con el visado resuelto, sería la entrada natural desde el bucle sierraleonés — y Robertsport está a solo 16 km."),
        ("BLOQUEADA sin visado estampado", "Ganta / Nzérékoré (desde Guinea)", "Entrada natural desde la Guinea forestal, con el río Mano como frontera. Es exactamente el hueco que el proyecto ha tenido que saltar yendo de Guinea directamente a Costa de Marfil por N'Zo/Gbapleu."),
        ("Salida hipotética", "Loguatuo / Ganta (hacia Danané, Costa de Marfil)", "Paso principal hacia el oeste marfileño y punto de reenganche con el trazado ya previsto de Costa de Marfil. POR CONFIRMAR horarios y sellado de CPD."),
        ("Trámite que desbloquearía todo", "Embajada de Liberia en Conakry (Guinea)", "La pieza que falta. Confirmar por teléfono o correo: si expide a no residentes, plazo de tramitación, si retienen el pasaporte, coste y requisitos. Alternativas equivalentes: Freetown, Abiyán, Accra, Dakar."),
        ("No aplica", "Embajada de Liberia en París (cubre España)", "Vía teórica para sacarlo antes de salir; el obstáculo es la ventana de validez de ~3 meses frente a un viaje de 8 meses. POR CONFIRMAR si hay modalidad de validez larga."),
    ],
    vehiculos=[
        "CPD (carnet de paso en aduana) recomendado; permiso de importación temporal emitido en la frontera como alternativa. POR CONFIRMAR el procedimiento real en Bo-Waterside y en Ganta, que no se ha podido verificar en fuente oficial.",
        "Carte Brune / Brown Card de la CEDEAO como seguro de responsabilidad civil regional: confirmar que la póliza cubre Liberia por nombre.",
        "Permiso internacional de conducir obligatorio.",
        "Conducción por la DERECHA, como en toda la subregión.",
        "Autonomía de combustible: el punto crítico es el sureste. Entre Buchanan y Harper, pasando por Greenville, no hay garantía de suministro formal. Salir de Buchanan con depósitos y garrafas al 100 %, contando con consumo de pista.",
        "Neumáticos, suspensión y protección de bajos: la vía costera del sureste es el terreno más exigente del país. Monrovia es la única plaza con recambios de cierto nivel; Ganta y Gbarnga tienen talleres elementales.",
        "Filtro de embudo obligatorio fuera de Monrovia: en el sureste el gasóleo se compra a menudo en garrafa.",
        "Ventaja práctica: el dólar estadounidense es moneda de curso legal en Liberia, lo que simplifica repostajes, peajes informales y compras sin depender del cambio local.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Sin procedimiento turístico publicado: solicitar autorización previa y por escrito a la Liberia Civil Aviation Authority (LCAA) o, en su defecto, no volar el dron en el país.",
        "Nunca sobrevolar Monrovia: puerto franco, aeropuerto Roberts, Mamba Point y el barrio diplomático, ni edificios de gobierno.",
        "Nunca sobrevolar la plantación de Firestone en Harbel ni las instalaciones mineras y el ferrocarril del hierro de Yekepa-Buchanan: son concesiones privadas con seguridad propia.",
        "Nunca sobrevolar Sapo ni la reserva de Nimba Este sin permiso expreso de la Forestry Development Authority.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio ACTIVO confirmado en las fuentes consultadas a mediados de 2026, con tarifas fijadas directamente en dólares (~55 USD/mes residencial, ~390 USD el kit estándar).",
        "Sería especialmente útil en el sureste, donde la cobertura móvil es nula durante cientos de kilómetros y donde una avería sin comunicación es el riesgo más serio del país.",
        "SIM local (Orange Liberia, Lonestar/MTN) como base urbana. Cobertura aceptable en Monrovia, el eje Gbarnga-Ganta, Buchanan y Zwedru; nula en la vía costera del sureste y en Sapo.",
        "Revisar el mapa oficial 30-60 días antes por si cambia el marco de itinerancia.",
    ],
    perro_intro=[
        "AVISO DE PRIORIDAD: mientras el visado terrestre bloquee la entrada, este trabajo NO toca hacerlo. Se documenta lo que se sabe y se deja aparcado. Si el visado se resuelve, esta sección pasa a ser prioritaria y hay que abrirla con seis meses de antelación.",
        "No se ha localizado ninguna fuente oficial sobre la importación de animales de compañía en Liberia: ni norma publicada, ni ficha veterinaria internacional fiable, ni testimonio de viajero. Es un agujero documental equivalente al de Sierra Leona.",
        "PREPARACIÓN MÍNIMA por analogía con los vecinos de la CEDEAO, si alguna vez se activa: microchip; pasaporte europeo de animal de compañía; vacuna antirrábica en vigor con menos de 12 meses; certificado veterinario internacional reciente (asumir una ventana de 72 h, que es lo que exige Guinea); y titulación serológica hecha desde España, imprescindible para la reentrada en la UE.",
        "AUTORIDAD PROBABLE: el Ministerio de Agricultura de Liberia, a través de sus servicios veterinarios. POR CONFIRMAR el nombre exacto de la dirección competente y si existe un procedimiento publicado. Interlocutores: ese ministerio y la propia embajada de Liberia donde se tramite el visado, que es la ocasión natural para preguntar por el perro en el mismo trámite.",
        "VENTAJA DE IDIOMA: Liberia es anglófona, igual que Sierra Leona. La versión inglesa del pasaporte europeo de animal de compañía sirve aquí directamente, sin traducción al francés.",
        "PROBLEMA ESPECÍFICO DEL PAÍS: no es la entrada, es el sureste. Entre Buchanan y Harper no hay atención veterinaria en cientos de kilómetros, la humedad es extrema y las jornadas de pista son largas. Si se hiciera el corredor completo, habría que asumir que cualquier problema del perro en ese tramo no tiene solución local.",
        "SAPO: el perro no entra, sin discusión. Y como la visita es una expedición a pie de varios días, el plan B no es «esperar en el coche»: hay que dejarlo con cuidador en Greenville o en Monrovia y organizar turnos entre los tres viajeros.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional OBLIGATORIO y expresamente exigido para entrar.",
        "Malaria en todo el territorio y todo el año, con transmisión muy intensa: profilaxis a valorar con Sanidad Exterior, mosquitera y repelente con DEET.",
        "ÉBOLA — contexto y situación actual: el brote de 2014-2016 golpeó a Liberia con una dureza extrema (más de 4.800 muertos) y cerró el país durante meses. Fue declarado libre de transmisión en 2016 y NO hay transmisión activa: la situación sanitaria actual es completamente distinta. Quedan protocolos de higiene reforzados y un sistema sanitario que perdió mucho personal. Comprobar el estado epidemiológico con la OMS y el ECDC antes de entrar, como en toda la región.",
        "Lluvia y enfermedades de agua: con 4.600 mm anuales en Monrovia y 185 días de lluvia al año en Greenville, el saneamiento es un problema estructural. No beber del grifo en ningún punto del país; agua embotellada en Monrovia y en el eje asfaltado, y tratamiento completo en el resto.",
        "Vacunación recomendada además: hepatitis A y B, fiebre tifoidea, tétanos-difteria, meningitis, poliomielitis y rabia (preexposición), esta última especialmente relevante viajando con perro.",
        "Referencias hospitalarias: John F. Kennedy Medical Center en Monrovia (el principal, con capacidad limitada para politraumatismos) y Ganta Hospital en el noreste, que atiende a unas 450.000 personas. En el sureste y en Sapo no hay nada.",
        "Seguro con evacuación médica AÉREA imprescindible: la evacuación realista desde Liberia es a Accra, a Dakar o a Europa. Desde Sapo o desde la vía costera del sureste, además, hay que contar con días solo para llegar a un punto evacuable.",
        "Calor y humedad constantes: el país es equatorial y no tiene altiplano donde refrescar, salvo la zona de Yekepa y el Nimba. Planificar los esfuerzos a primera hora y descansar al mediodía.",
    ],
    seguridad_intro=("Liberia es hoy un país estable, sin conflicto activo, con dos transferencias pacíficas de poder por las urnas desde 2018. El riesgo del país <strong>no es político ni de violencia organizada</strong>: es "
                     "<strong>logístico</strong> — las carreteras del sureste, el aislamiento de Sapo, la ausencia de servicios entre Buchanan y Harper — y, por encima de todo, <strong>administrativo</strong>, que es lo que "
                     "lo ha dejado fuera de la ruta."),
    seguridad=[
        "Sin conflicto armado ni zonas vedadas. Alternancias pacíficas en 2018 (George Weah) y 2024 (Joseph Boakai). Precaución general normal y revalidación del aviso de Exteriores 72 h antes.",
        "No conducir de noche fuera de Monrovia y del eje asfaltado: firme irregular, ausencia de señalización y motos («penpen») por todas partes.",
        "Aislamiento del sureste: entre Buchanan y Harper no hay cobertura móvil fiable, ni combustible garantizado, ni asistencia mecánica, ni atención sanitaria. Los dos vehículos siempre juntos, autonomía completa y aviso en Buchanan y en Greenville de a dónde se va y cuándo se vuelve.",
        "Monrovia: delincuencia urbana común (tirones, robos en atascos, carterismo en Waterside). Ventanillas subidas en atasco, nada visible, aparcamiento vigilado y no circular de noche.",
        "West Point y otros barrios densos de Monrovia: no entrar por libre ni con cámara. Si interesa, se hace con guía local y con acuerdo previo.",
        "Controles de carretera: existen y son en general correctos. Documentación en carpeta con copias y paciencia.",
        "No fotografiar instalaciones militares o policiales, el puerto franco, el aeropuerto Roberts, las instalaciones de Firestone ni las minas y el ferrocarril del hierro.",
        "Sensibilidad histórica extrema: dos guerras civiles con unos 250.000 muertos y uso masivo de niños soldado, y un brote de ébola que mató a más de 4.800 personas, todo dentro de una generación. No se fotografía, no se pregunta a la ligera y no se convierte en anécdota de viaje. En Gbarnga, además, conviene saber que fue la capital de facto de Charles Taylor antes de sacar el tema.",
        "Dinero: el dólar estadounidense circula como moneda legal, lo que reduce el riesgo de cambio callejero. Cajeros en Monrovia y poco más; llevar efectivo para el interior.",
    ],
    agua=[
        "Monrovia y eje asfaltado (Gbarnga, Ganta): agua embotellada en supermercados y tiendas. Para el depósito de uso general, estaciones de servicio, hoteles y misiones permiten llenar con manguera.",
        "Buchanan y costa de Grand Bassa: agua embotellada disponible en la ciudad; en las playas y lagunas, nada — salir con la reserva llena.",
        "Sureste (Greenville, Harper) y Sapo: sin ningún punto fiable. Agua de río tratada con filtro mecánico más tratamiento químico o ebullición. Salir de Greenville con toda la reserva antes de entrar en el parque o de seguir hacia Harper.",
        "Paradoja del país: es el más lluvioso de la región —4.600 mm anuales en Monrovia, 185 días de lluvia al año en Greenville— y a la vez uno de los más difíciles para conseguir agua potable fuera de la capital. El agua de lluvia recogida es una opción real en el sureste, tratada igualmente.",
        "Nunca beber del grifo en ningún punto del país.",
    ],
    combustible=[
        "Monrovia: mejor oferta y calidad del país. Repostar a fondo aquí antes de cualquier tramo interior o del sureste.",
        "Eje asfaltado Monrovia → Gbarnga → Ganta (~300 km) y Buchanan: estaciones formales suficientes, sin huecos comprometidos. Zwedru tiene suministro pero irregular.",
        "AVISO SERIO — sureste: entre Buchanan y Harper, pasando por Greenville (~530 km de pista), no hay ninguna garantía de suministro formal y buena parte del combustible se compra en garrafa a pie de carretera. Es el tramo de mayor riesgo logístico del país: salir de Buchanan con depósitos y garrafas al 100 % y contar con el mayor consumo en pista.",
        "Filtro de embudo obligatorio fuera de Monrovia y del eje asfaltado.",
        "Confirmar puntos recientes en iOverlander antes de cada tramo rural; en el sureste no hay que esperar encontrar ninguno.",
    ],
    experiencias_intro=("Datos de campo y avisos recogidos para entender por qué este país está fuera de la ruta y qué haría falta para reabrirlo. Liberia está razonablemente documentada en lo institucional —visados, embajadas, parques— "
                        "y muy mal en lo overland: casi no hay relatos recientes de viajeros con vehículo propio, precisamente porque la barrera del visado terrestre expulsa a ese perfil:"),
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("EL PENDIENTE QUE DECIDE TODO · Embajada de Liberia en Conakry", "Llamar o escribir a la Embajada de Liberia en Conakry y obtener por escrito tres respuestas: (1) ¿expide visado turístico a extranjeros NO residentes en Guinea?; (2) ¿cuánto tarda y RETIENE EL PASAPORTE durante la tramitación?; (3) ¿cuánto cuesta y qué requisitos pide? Criterio de cierre: respuesta escrita o verbal registrada con nombre y cargo. ES TRABAJO DE UNA TARDE Y ES LO ÚNICO QUE SEPARA A LIBERIA DE VOLVER A LA RUTA. DECISIÓN DEL DUEÑO: si se hace o no"),
        ("Alternativas consulares", "Si Conakry no expide a no residentes, preguntar lo mismo a las embajadas de Liberia en Freetown, Abiyán, Accra y Dakar. Freetown sería la opción natural si se ejecuta el bucle de Sierra Leona"),
        ("Visado desde París", "Confirmar con la Embajada de Liberia en París (que cubre España) si existe una modalidad de visado con validez superior a tres meses o con entrada diferida, que permitiría sacarlo antes de salir de Barcelona"),
        ("Confirmar la restricción del eVisa", "Verificar con fuente oficial liberiana que el visado electrónico sigue limitado al aeropuerto internacional de Monrovia y no se ha extendido a fronteras terrestres. Si se extendiera, el país vuelve a la ruta sin más trámite. Revisar cada 6 meses hasta la salida"),
        ("Vía costera del sureste", "Si el país se reactivara: confirmar el estado real de Buchanan-Greenville-Harper con overlanders recientes y con la comunidad local ANTES de comprometer el calendario. Es el tramo que puede consumir una semana entera o resultar impracticable"),
        ("Sapo · Forestry Development Authority", "Si el país se reactivara: solicitar autorización de entrada, guías y porteadores con mucha antelación, y confirmar la custodia de los vehículos en Greenville. Recordar que solo se entra a pie y que son 3-5 días"),
        ("Nimba Este", "Confirmar con la Forestry Development Authority el estatus y el régimen de visita de la Reserva Natural de Nimba Este, del lado liberiano. Recordar que NO es Patrimonio de la UNESCO"),
        ("Gola liberiano y Lofa-Mano", "Confirmar el estatus legal, la gestión y el acceso del bosque de Gola del lado liberiano y del proyecto de Parque Nacional de Lofa-Mano"),
        ("Cataratas de Kpatawee", "Confirmar coordenada exacta y estado del acceso y de las instalaciones: no se ha podido verificar en fuente cartográfica"),
        ("Perro", "APARCADO mientras el visado bloquee la entrada. Si se reactiva: escribir al Ministerio de Agricultura liberiano y preguntar en la misma embajada donde se tramite el visado"),
        ("Drones · LCAA", "Si el país se reactivara: resolver autorización por escrito ante la Liberia Civil Aviation Authority o excluir el dron"),
        ("Fotos pendientes de sustituir", "Todos los PDIs de esta ficha reutilizan cuatro imágenes de Liberia verificadas en Wikimedia Commons (West Point/Monrovia, playa de Robertsport, hipopótamo pigmeo y monte Nimba), porque no se ha podido verificar ningún otro archivo. Sustituir a medida que aparezcan archivos verificados"),
    ],
    sources=SOURCES,
    sources_note=("Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha documenta un país EXCLUIDO de la ruta fija: se mantiene completa como información de reserva y, sobre todo, para dejar escrito exactamente qué tendría que "
                  "cambiar para que Liberia volviera al itinerario. Hallazgos de esta revisión: (1) el motivo de la exclusión queda verificado y precisado — el visado electrónico liberiano, vigente desde el 11 de marzo de 2025, solo se expide en el "
                  "aeropuerto internacional de Monrovia; (2) la vía de solución queda identificada — Liberia mantiene embajadas en Conakry, Freetown, Abiyán, Accra y Dakar, cualquiera de las cuales podría estampar el visado, y faltan por confirmar "
                  "únicamente tres datos (si expide a no residentes, plazo y coste); (3) Liberia no tiene embajada en España, la cubre París, y la ventana de validez de ~3 meses hace inviable tramitarlo antes de salir; (4) CORRECCIÓN de la versión "
                  "anterior: el lado liberiano del monte Nimba NO está inscrito en el Patrimonio Mundial de la UNESCO; (5) el acceso a Sapo es exclusivamente a pie, con autorización de la Forestry Development Authority. "
                  "Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación."),
    emergency="Policía 911 (variable según región: verificar localmente) · Sin embajada de España en Monrovia desde 1990: emergencia consular española a través de la Embajada de España en Abidjan (Costa de Marfil) +225 22 44 48 50 · emb.abidjan@maec.es.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

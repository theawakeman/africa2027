# -*- coding: utf-8 -*-
"""Angola — ficha completa, corredor doble bajada/subida (11 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== BAJADA: Lufu/Luvo (RD Congo) -> Luanda -> Malanje -> altiplano -> Moxico -> Caripande (Zambia) =====
    dict(n=1, name="Luanda", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-8.8383, lon=13.2344,
         desc="Capital y mayor base logística del país: puerto, aeropuerto internacional, embajada de España, talleres y recambios de todo tipo. Marginal (paseo marítimo), Fortaleza de San Miguel y el Museo Nacional de Antropología como referencia urbana e histórica. Punto de paso obligado tanto en la bajada como en la subida.",
         credit="Chimpanz APe · CC BY 2.0", source=W + "2009%20Luanda%20Angola%203818325721.jpg?width=900"),
    dict(n=2, name="Miradouro da Lua", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=-9.1667, lon=13.0333,
         desc="Paisaje erosionado de cañones y formaciones lunares sobre el Atlántico, a 40 km al sur de Luanda; mirador espectacular al atardecer y parada obligada nada más salir de la capital.",
         credit="Paulo César Santos · CC0", source=W + "Miradouro%20da%20Lua%20(Angola).jpg?width=900"),
    dict(n=3, name="Pedras Negras de Pungo Andongo", cat="Naturaleza", prio="Alta", dog="permitido", time="½–1 día",
         lat=-9.6625, lon=15.5839,
         desc="Descomunales monolitos de roca negra que emergen de la sabana verde, visibles desde 50 km de distancia; lugar de leyenda de la reina Nzinga (huellas talladas en la roca) y ruinas de un fuerte portugués del siglo XVII. Uno de los mejores vivac salvajes documentados por otros overlanders en Angola, junto a arroyos claros entre los bloques de granito. Hay rutas a pie cortas entre los monolitos.",
         credit="Wikimedia Commons", source=W + "Pungo%20Andongo%2C%20Malange%2C%20Angola.JPG?width=900"),
    dict(n=4, name="Cascadas de Kalandula (Calandula)", cat="Naturaleza", prio="Alta", dog="permitido", time="½–1 día",
         lat=-9.0758, lon=16.0033,
         desc="Con 105 m de altura y 400 m de anchura, la segunda mayor catarata de África por caudal tras las Victoria Falls, sobre el río Lucala en la provincia de Malanje; a unos 360 km de Luanda. Se puede bajar a pie hasta la base por un sendero empinado para ver el salto desde abajo, con arcoíris permanente en la niebla de agua.",
         credit="Wikimedia Commons", source=W + "Kalandula%20waterfalls%20of%20the%20Lucala-River%20in%20Malange%2C%20Angola.JPG?width=900"),
    dict(n=5, name="Parque Nacional de Cangandala · palanca negra gigante", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="1 día",
         lat=-9.9167, lon=16.4000,
         desc="El parque más pequeño de Angola (630 km², a unos 50 km al sur de la ciudad de Malanje) y el único lugar del mundo, junto con la vecina reserva de Luando, donde vive la PALANCA NEGRA GIGANTE: el símbolo nacional de Angola, un antílope en peligro crítico de cuernos inmensos que se creyó extinto tras la guerra civil. En 2026 se reunieron más de 200 ejemplares, un hito de conservación. Convive con pukú, sitatunga, búfalo, leopardo y león. Coordenada aproximada (el parque no publica una puerta oficial): confirmar acceso con el INBAC antes de ir. Foto: ejemplar de la especie, no del propio parque.",
         credit="Wikimedia Commons", source=W + "Stavenn%20Hippotragus%20niger%20variani%2000.jpg?width=900"),
    dict(n=6, name="Waku Kungo (hipopótamos y plantaciones de café)", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="½–1 día",
         lat=-11.3500, lon=15.1167,
         desc="En el altiplano de Kwanza Sul, entre las antiguas grandes plantaciones de café coloniales hoy semiabandonadas, hay lagunas donde se pueden observar hipopótamos en libertad y sin entrar en ningún parque nacional — lo que lo convierte en una de las mejores opciones de fauna salvaje compatible con llevar el perro en el vehículo. Parada natural a medio camino entre Malanje y el altiplano de Huambo.",
         credit="Wikimedia Commons", source=W + "Waku%20Kungo%2C%20Angola%20-%20panoramio.jpg?width=900"),
    dict(n=7, name="Bailundo (reino del Bailundo)", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=-12.1833, lon=15.8167,
         desc="Antigua capital del reino de Bailundo, uno de los grandes reinos ovimbundu del altiplano y todavía hoy una monarquía tradicional viva: se puede solicitar audiencia con la autoridad tradicional (o soba) y asistir a ceremonias y danzas. Uno de los pocos lugares del viaje donde la parada es puramente cultural y no paisajística. Imagen de referencia del altiplano de la región, no del propio Bailundo.",
         credit="Wikimedia Commons", source=W + "Igreja%20Matriz%20de%20Waku%20Kungo%20-%20panoramio.jpg?width=900"),
    dict(n=8, name="Morro do Moco · techo de Angola (2.620 m)", cat="Naturaleza", prio="Alta", dog="permitido con correa", time="1–2 días",
         lat=-12.4667, lon=15.1667,
         desc="El punto más alto de Angola, a 70 km al oeste de Huambo, con la aldea de Kanjonde al pie como punto de partida de la subida a pie. Conserva los últimos bosques afromontanos del país y es Área Importante para las Aves: 233 especies, varias endémicas o amenazadas (francolín de Swierstra, chat de las cuevas de Angola, papamoscas pizarroso angoleño). Entre julio y septiembre florecen las proteas tras las quemas de la hierba. Sin estatus de protección ni infraestructura: guía local de Kanjonde imprescindible. LA gran excursión a pie de Angola.",
         credit="Wikimedia Commons", source=W + "Morro%20do%20Moco%2C%20Huambo%2C%20Angola.jpg?width=900"),
    dict(n=9, name="Luena (Moxico)", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-11.7833, lon=19.9167,
         desc="Capital de Moxico y última ciudad con servicios reales (combustible formal, taller, hospital, mercado) antes de los más de 400 km de pistas hacia Cazombo y la frontera de Zambia. Punto de no retorno logístico de la bajada: lo que no se consiga aquí, no se consigue hasta Zambia.",
         credit="Wikimedia Commons", source=W + "Luena%20Angola.jpg?width=900"),
    # ===== SUBIDA: Namibia -> desierto del Namibe -> meseta -> costa -> Luanda -> Lufu/Luvo =====
    dict(n=10, name="Parque Nacional de Iona", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=-16.7000, lon=12.3333,
         desc="15.200 km² de desierto del Namib angoleño gestionados por African Parks: oryx, cebras, springbok, guepardo, leopardo, hiena parda y jirafas angoleñas reintroducidas en 2023-2024 tras desaparecer en la guerra civil; welwitschias milenarias (posiblemente de más de 2.000 años). Pistas de tierra y arena sin señalización fija — llevar GPX o guía local.",
         credit="Wikimedia Commons", source=W + "Welwitschia%20in%20the%20Namibe%20desert.JPG?width=900"),
    dict(n=11, name="Foz do Cunene", cat="Naturaleza", prio="Media", dog="permitido con precaución", time="1 noche",
         lat=-17.3000, lon=11.6667,
         desc="Desembocadura del río Cunene, frontera natural con Namibia, entre dunas y un paisaje casi lunar; aguas termales río arriba (extremar precaución, hay cocodrilos aguas abajo). Combinar con Iona en un mismo bucle de 2-3 días desde Namibe. Imagen de referencia del entorno desértico costero de la provincia de Namibe — no es una foto exacta de la desembocadura.",
         credit="Wikimedia Commons", source=W + "Angola%20Namibe%20Bentiaba%20OM%2020170710%20(19).jpg?width=900"),
    dict(n=12, name="Baía dos Tigres (avanzado, opcional)", cat="Naturaleza", prio="Media", dog="permitido con precaución", time="2–3 días (expedición)",
         lat=-16.6167, lon=11.7833,
         desc="Antigua península convertida en isla en 1962, con el pueblo pesquero abandonado tragado por la arena; el tramo mítico de duna-hasta-el-mar del sur de Angola. Se llega desde Tombwa cruzando el paso de marea 'Doodsakker', navegable solo con marea baja y luna llena o nueva. Mínimo 2 vehículos 4x4, equipo de recuperación y planificación de mareas — es exactamente el tipo de expedición 4x4 que buscamos para el bloque sur, pero exige preparación experta o un guía local.",
         credit="Wikimedia Commons", source=W + "Ilha%20dos%20Tigres%201466540%20960%20720.jpg?width=900"),
    dict(n=13, name="Tchitundu-Hulu · arte rupestre", cat="Cultura", prio="Alta", dog="permitido", time="1 día",
         lat=-15.9406, lon=12.8793,
         desc="Conjunto de arte rupestre sobre varios inselbergs en plena semidesierto, a 37 km al suroeste de Virei y 150 km al sur de Moçâmedes: cuatro yacimientos repartidos en un kilómetro (Tchitundu-Hulu Mumule, Tchitundu-Hulu Mucai, Pedra das Zebras y Pedra da Lagoa) con grabados y pinturas en rojo y blanco, sobre todo geométricos (círculos concéntricos) pero también antílopes, serpientes y felinos. Datación discutida, entre el primer milenio a.C. y comienzos del primer milenio d.C. Candidato a Patrimonio Mundial de la UNESCO desde 2017. Acceso solo en 4x4 por pista. Imagen de referencia del desierto del Namibe, no del yacimiento.",
         credit="Wikimedia Commons", source=W + "Angola%20Namibe%20Bentiaba%20OM%2020170710%20(19).jpg?width=900"),
    dict(n=14, name="Lagoa do Arco (Lake Arco)", cat="Naturaleza", prio="Alta", dog="permitido", time="1 noche",
         lat=-15.7661, lon=12.0667,
         desc="Oasis de agua dulce en pleno desierto del Namibe, encajado entre dos grandes arcos de arenisca, con aves acuáticas, rapaces y tejedores. La aldea vecina de Njambasana ha montado un aparcamiento y un camping básico de gestión comunitaria donde se paga una tasa: una de las pocas pernoctas organizadas del desierto angoleño y, por ello, muy recomendable. Importante: la laguna se secó tras las malas lluvias de 2013-2014 y estuvo seca mucho tiempo — confirmar si tiene agua antes de desviarse.",
         credit="Wikimedia Commons", source=W + "Mini%20oasis%20in%20the%20namibe%20desert%2C%20Angola.JPG?width=900"),
    dict(n=15, name="Namibe (Moçâmedes)", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-15.1961, lon=12.1522,
         desc="Ciudad y puerto donde el desierto del Namibe llega literalmente al Atlántico; arquitectura colonial portuguesa en la Marginal, base logística para el desierto, Tundavala, Serra da Leba, Lagoa do Arco, Tchitundu-Hulu y la expedición avanzada a la Baía dos Tigres.",
         credit="Wikimedia Commons", source=W + "Marginal%20of%20Namibe.JPG?width=900"),
    dict(n=16, name="Serra da Leba", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=-15.0711, lon=13.2486,
         desc="El puerto de montaña más fotografiado de Angola: la EN280 sube en herraduras cerradas desde la llanura costera (~720 m) hasta 1.845 m de altitud, enlazando Namibe con la meseta de Lubango. Asfaltado pero exigente; mirador junto a la carretera con vistas a todo el valle y posibilidad de caminar por el borde del escarpe.",
         credit="Wikimedia Commons", source=W + "Serra%20da%20Leba-Road.jpg?width=900"),
    dict(n=17, name="Tundavala (Fenda da Tundavala)", cat="Naturaleza", prio="Alta", dog="permitido con correa corta", time="½–1 día",
         lat=-14.8177, lon=13.3814,
         desc="Grieta de unos 800 m en el borde de la meseta de Humpata, a 18 km de Lubango, con un salto de más de 1.000 m hasta la llanura; una de las 7 Maravillas Naturales de Angola. Pista de tierra desde Lubango y varios senderos por el borde del acantilado con vistas de 10.000 km² hacia Moçâmedes. El mirador está en el mismo borde: correa corta imprescindible.",
         credit="Wikimedia Commons", source=W + "Tundavala%20Gap.jpg?width=900"),
    dict(n=18, name="Benguela", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-12.5783, lon=13.4055,
         desc="La ciudad colonial portuguesa mejor conservada de la costa angoleña, cabecera del histórico ferrocarril de Benguela que cruzaba el continente hasta el Congo; playas urbanas (Praia Morena, Coatinha) y centro histórico paseable. Más tranquila y agradable que Lobito para pernoctar.",
         credit="Wikimedia Commons", source=W + "Praia%20Morena%20Benguela.jpg?width=900"),
    dict(n=19, name="Lobito", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-12.3644, lon=13.5456,
         desc="Ciudad portuaria sobre una restinga arenosa entre el océano y la bahía, con arquitectura colonial portuguesa bien conservada (Igreja da Arrábida); gran plaza logística de la costa junto con Benguela, a 30 km.",
         credit="Robertoago · CC BY-SA 3.0", source=W + "Lobito%20restinga2.jpg?width=900"),
    dict(n=20, name="Cabo Ledo", cat="Costa", prio="Media", dog="permitido", time="1–2 noches",
         lat=-9.6833, lon=13.2167,
         desc="Bahía de arena a unos 120 km al sur de Luanda, conocida por una de las olas izquierdas más largas de África y por sus acantilados rojos sobre la playa; camping y alojamientos sencillos junto a la arena, ambiente relajado y perro sin problema. Buen sitio para descomprimir un par de días antes de afrontar Luanda y la frontera del norte.",
         credit="Wikimedia Commons", source=W + "Cabo%20Ledo%20beach%2C%20Angola%2002.jpg?width=900"),
    dict(n=21, name="Parque Nacional de Kissama (Quiçama)", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido", time="1 día",
         lat=-9.7500, lon=13.5830,
         desc="A unos 70 km al sur de Luanda, el único parque nacional angoleño realmente operativo y el más accesible del país, repoblado tras la guerra con la 'Operación Arca de Noé' (elefantes y otras especies traídos de Botsuana y Sudáfrica); baobabs, candelabros y sabana junto al río Kwanza. Reserva de la Biosfera UNESCO desde 2025.",
         credit="Wikimedia Commons", source=W + "Kissama%20003.JPG?width=900"),
    dict(n=22, name="Mussulo", cat="Costa", prio="Media", dog="permitido con condiciones", time="½–1 día",
         lat=-8.9833, lon=13.1667,
         desc="Larga lengua de arena frente a Luanda que encierra una laguna de agua tranquila, con restaurantes de pescado y playas a un lado y bahía mansa al otro; se llega en barco-taxi desde la capital. Última parada ligera del viaje antes de encarar de nuevo el tramo centroafricano hacia el norte.",
         credit="Wikimedia Commons", source=W + "Mussulo%20Island%20banner%20view%20from%20taxi%20boat.jpg?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "naturaleza": "verde", "cultura": "morado", "costa": "turquesa"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada bajada — Lufu/Luvo (desde RD Congo)", "Frontera", -5.9167, 13.9667,
     "Cruce del puente fronterizo con RD Congo; registro y sellado ~500 m dentro de Angola. Desvío opcional a M'banza-Kongo (Patrimonio Mundial UNESCO, antigua capital del Reino del Kongo) a poca distancia. También es la frontera de SALIDA en la subida, cerrando el corredor angoleño."),
    ("Frontera · Salida bajada — Caripande (hacia Zambia, cerca de Cazombo)", "Frontera", -11.9000, 22.9000,
     "Paso remoto en el extremo este de Angola (provincia de Moxico), frente al puesto zambiano de Chavuma. Otros overlanders describen la oficina de inmigración angoleña como muy precaria (secuelas de la guerra) y el trámite en portugués; más de 100 km de pistas de arena con charcos profundos entre Cazombo y la zona previa a la frontera, intransitables o muy lentos en temporada de lluvias (octubre-marzo). Cruzar solo en temporada seca (mayo-septiembre) y registrarse en la policía de Cazombo."),
    ("Frontera · Entrada subida — Santa Clara/Oshikango (desde Namibia)", "Frontera", -17.3500, 15.7500,
     "Paso principal y más transitado entre Angola y Namibia; carretera asfaltada en ambos lados, infraestructura de control moderna. Punto de entrada de la subida hacia Namibe, Serra da Leba y Tundavala."),
    ("Frontera · Alternativa subida — Calueque/Ruacana (desde Namibia)", "Frontera", -17.2825, 14.5347,
     "Paso alternativo más al oeste, junto a la presa de Calueque sobre el río Cunene y el puesto namibio de Ruacana/Omahenene; pista sin asfaltar en el lado angoleño, más lenta que Santa Clara pero da acceso directo a las cataratas de Ruacana, Epupa (lado namibio) y al Parque Nacional de Iona sin desvío adicional."),
    ("Embajada de España en Luanda", "Consular", -8.8167, 13.2333,
     "Rua Frederico Welwitsch 84, Torre Maculusso, 12º andar C, Postal 3061, Luanda. Tel. +244 222 391 166/187/188 · Emergencia consular: +244 929 900 900."),
    ("Hospital Américo Boavida — Luanda", "Hospital", -8.8147, 13.2302,
     "Principal hospital de referencia de la capital. Coordenada urbana aproximada."),
    ("Hospital Central da Huíla — Lubango", "Hospital", -14.9077, 13.4925,
     "Referencia hospitalaria del tramo de Serra da Leba y Tundavala, en la subida entre Namibe y la costa."),
    ("Combustible · Luanda / Lobito", "Combustible", -8.8383, 13.2344,
     "Mejor oferta y calidad del país (Sonangol, Pumangol) en las dos grandes ciudades costeras; repostar a fondo en ambas."),
    ("Combustible · M'banza-Kongo / Uíge (eje norte)", "Combustible", -6.2667, 14.2500,
     "Estaciones formales en el desvío norte antes de bajar a Luanda; confirmar disponibilidad, oferta más limitada que en la costa."),
    ("Combustible · Malanje", "Combustible", -9.5402, 16.3410,
     "Base del triángulo de Malanje (Pedras Negras, Kalandula, Cangandala): combustible formal, hospital provincial, hoteles y mercado. Última plaza grande antes del altiplano."),
    ("Huambo · base logística del altiplano", "Combustible", -12.7761, 15.7392,
     "Segunda ciudad del país (la antigua Nova Lisboa), a 1.700 m: combustible, talleres, hospital provincial y hoteles. Punto de partida hacia el Morro do Moco (70 km al oeste, hasta la aldea de Kanjonde) y hacia Bailundo."),
    ("Combustible · Kuito (Bié)", "Combustible", -12.3833, 16.9333,
     "Capital de Bié y única parada de servicios entre Huambo y Luena; repostar aquí aunque el depósito no esté bajo, porque el siguiente tramo son ~400 km de asfalto degradado."),
    ("Benguela · servicios de costa", "Combustible", -12.5783, 13.4055,
     "Junto con Lobito (30 km), la gran plaza de servicios de la costa central en la subida: combustible, talleres, recambios, hospital y alojamiento."),
    ("Tombwa · último servicio antes del desierto profundo", "Combustible", -15.8000, 11.8500,
     "Último pueblo con combustible (irregular) antes de Baía dos Tigres y del desvío a Virei/Tchitundu-Hulu; confirmar existencias y salir con garrafas llenas desde Namibe."),
    ("Combustible · Cazombo (extremo este, escaso)", "Combustible", -11.9000, 22.9000,
     "Oferta muy limitada e irregular; llegar con depósitos y garrafas de reserva llenas desde Luena, sobre todo si el cruce a Zambia se complica por barro."),
    ("Combustible · Namibe / Lubango (eje sur)", "Combustible", -15.1961, 12.1522,
     "Estaciones formales en ambas ciudades; repostar en Namibe antes de Baía dos Tigres/Iona (sin oferta) y de nuevo en Lubango tras Serra da Leba."),
    ("Agua potable y de uso general · Luanda", "Agua potable", -8.8383, 13.2344,
     "Agua embotellada sin problema en supermercados de la capital; estaciones de servicio y hoteles de Luanda y Lobito permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria: tratar como restringido",
                  "Angola exige autorización previa del Instituto Nacional de Aviação Civil (INAVIC) para cualquier vuelo de dron, con especial sensibilidad cerca de instalaciones petroleras y portuarias (Luanda, Lobito, Cabinda) y de la presa de Calueque. Norma prudente del proyecto: no volar sin permiso escrito, y evitar cualquier vuelo cerca de infraestructura energética, militar o de los parques nacionales sin autorización expresa.")

STARLINK_CALLOUT = ("warn", "Anunciado para 2026, aún no activo a mediados de año: tratar como no disponible",
                     "Angola figura entre los mercados africanos con Starlink previsto («coming in 2026») pero sin confirmación de servicio activo a mediados de 2026. Tratarlo como no disponible hasta confirmación oficial y mantener SIM local (Unitel, Africell) como conectividad principal; en el tramo remoto de Moxico (bajada hacia Zambia) no dar por hecho tampoco cobertura móvil continua.")

DOG_MATRIX = [
    ("Waku Kungo (hipopótamos en libertad)", "permitido con condiciones",
     "LA mejor opción de fauna salvaje del país compatible con el perro: las lagunas con hipopótamos del altiplano de Kwanza Sul están FUERA de cualquier parque nacional, así que no aplica la prohibición de mascotas. Mantener distancia real con los hipopótamos (son el animal grande más peligroso de África) y el perro atado y dentro del vehículo cerca del agua."),
    ("Luanda, Benguela, Lobito, Namibe, Mussulo, Cabo Ledo", "permitido con condiciones",
     "Ciudades y playas sin restricción específica; Cabo Ledo y Mussulo son las paradas más cómodas del viaje para el perro. Calor seco en el sur, más húmedo en la franja costera norte."),
    ("Miradouro da Lua, Pedras Negras, Kalandula, Serra da Leba, Tundavala, Morro do Moco, Tchitundu-Hulu, Lagoa do Arco", "permitido",
     "Todos son sitios abiertos sin gestión de parque nacional. Correa corta obligatoria en los bordes de acantilado (Tundavala, Serra da Leba) y en el sendero de bajada a Kalandula. En el Moco, consultar con el guía de Kanjonde si el perro puede acompañar la subida."),
    ("Parque Nacional de Iona / Kissama / Cangandala", "no confirmado",
     "Los tres tienen grandes depredadores o megafauna (Iona: guepardo, leopardo, hiena parda; Kissama: leones y elefantes reintroducidos; Cangandala: leopardo y león, además de la palanca negra gigante en peligro crítico). Tratar como prohibido hasta confirmación escrita de African Parks (Iona) y del INBAC (Kissama, Cangandala). Plan B: mirador o puerta de entrada con un miembro del grupo quedándose con el perro, o sustituir por Waku Kungo, que sí es compatible."),
    ("Baía dos Tigres, Foz do Cunene", "permitido con precaución",
     "Sol y calor extremos sin sombra natural en Baía dos Tigres — llevar toldo y agua de sobra; en Foz do Cunene mantener al perro lejos de la orilla por los cocodrilos del Cunene aguas abajo."),
]

SOURCES = [
    ("Angola-Visa.com · proceso de e-visa para viajeros overland", "https://www.angola-visa.com/overland/"),
    ("Hinterland Travel · requisitos de visado de Angola para ciudadanos españoles", "https://www.hinterlandtravel.com/spain/destinations/angola"),
    ("WhirledAway · cruce de frontera Lufu (RD Congo) / Luvo (Angola)", "https://whirled-away.com/border-crossing-drc-angola/"),
    ("Embajada de España en Angola · contacto", "https://www.exteriores.gob.es/Embajadas/luanda/es/Paginas/index.aspx"),
    ("tech.africa · disponibilidad de Starlink en África (2026)", "https://tech.africa/starlink-africa/"),
    ("UNESCO · Mbanza Kongo, vestigios de la capital del antiguo Reino del Kongo", "https://whc.unesco.org/en/list/1473/"),
    ("iOverlander · puntos de combustible, agua y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía, puntos overland y blog de viajeros por África", "https://tracks4africa.co.za/"),
    ("Tracks4Africa Blog · «Angola… an acquired taste» — guía práctica de overland por Angola", "https://blog.tracks4africa.co.za/angola-acquired-taste/"),
    ("Paul Godard · relato de expedición 4x4 por el sur de Angola (2022)", "https://www.paulgodard.com/blog/79"),
    ("Africa Overland Blog · cruce de frontera Zambia-Angola por Chavuma/Caripande y travesía hasta Kalandula", "https://africaoverland.blog/2019/12/08/road-tripping-across-angola/"),
    ("kumakonda.com · expedición 4x4 a Baía dos Tigres y Foz do Cunene", "https://kumakonda.com/ilha-da-baia-dos-tigres-angola/"),
    ("Wikipedia · Iona National Park", "https://en.wikipedia.org/wiki/Iona_National_Park"),
    ("African Parks · Parque Nacional de Iona", "https://www.africanparks.org/the-parks/iona"),
    ("Wikipedia · Quiçama National Park", "https://en.wikipedia.org/wiki/Qui%C3%A7ama_National_Park"),
    ("Wikipedia · Kalandula Falls", "https://en.wikipedia.org/wiki/Kalandula_Falls"),
    ("Wikipedia · Black Rocks at Pungo Andongo", "https://en.wikipedia.org/wiki/Black_Rocks_at_Pungo_Andongo"),
    ("Wikipedia · Tundavala Gap", "https://en.wikipedia.org/wiki/Tundavala_Gap"),
    ("Wikipedia · Serra da Leba", "https://en.wikipedia.org/wiki/Serra_da_Leba"),
    ("Wikipedia · Cazombo", "https://en.wikipedia.org/wiki/Cazombo"),
    ("Wikipedia · Calueque", "https://en.wikipedia.org/wiki/Calueque"),
    ("Angola Tourism (web oficial de turismo) · naturaleza y parques", "https://angola-tourism.com/nature/"),
    ("Angola Tourism (web oficial de turismo) · regiones de Huambo y Bié", "https://angola-tourism.com/huambo-and-bie/"),
    ("Wikipedia · Mount Moco (Morro do Moco)", "https://en.wikipedia.org/wiki/Mount_Moco"),
    ("Wikipédia (pt) · Parque Nacional da Cangandala", "https://pt.wikipedia.org/wiki/Parque_Nacional_da_Cangandala"),
    ("Fundação Kissama · la palanca negra gigante", "https://fundacaokissama.co.ao/index.php/pt/palancanegra/palanca"),
    ("Wikipedia · Tchitundu-Hulu (arte rupestre)", "https://en.wikipedia.org/wiki/Tchitundu-Hulu"),
    ("UNESCO · Site Archéologique de Tchitundu-Hulu (lista indicativa)", "https://whc.unesco.org/en/tentativelists/6251/"),
    ("British Museum · African Rock Art, Tchitundu-Hulu", "https://africanrockart.britishmuseum.org/country/angola/tchitundu-hulu/"),
    ("Wikipedia · Lake Arco (Lagoa do Arco)", "https://en.wikipedia.org/wiki/Lake_Arco"),
    ("Wikipedia · Bicuari National Park", "https://en.wikipedia.org/wiki/Bicuari_National_Park"),
    ("Angola Expert · conducir y hacer overland por Angola, estado de las carreteras", "https://www.angolaexpert.com/en/angola-roads-a-guide-to-driving-across-the-country/"),
    ("Take Your Backpack · guías de rutas a pie en Angola (Moco, Tundavala, Serra da Leba)", "https://www.takeyourbackpack.com/backpacking-in-angola/hike-mount-moco-trail/"),
]

# Bajada: frontera norte -> Luanda -> Malanje -> altiplano de Huambo -> Bié -> Moxico -> Zambia
CORRIDOR = [(-5.9167, 13.9667), (-8.8383, 13.2344), (-9.1667, 13.0333), (-9.6625, 15.5839),
            (-9.0758, 16.0033), (-9.5402, 16.3410), (-9.9167, 16.4000), (-11.3500, 15.1167),
            (-12.1833, 15.8167), (-12.4667, 15.1667), (-12.7761, 15.7392), (-12.3833, 16.9333),
            (-11.7833, 19.9167), (-11.9000, 22.9000)]

# Subida: frontera sur -> desierto del Namibe -> meseta de Lubango -> costa -> Luanda -> frontera norte
CORRIDOR_ALT = [(-17.3500, 15.7500), (-16.7000, 12.3333), (-17.3000, 11.6667), (-16.6167, 11.7833),
                (-15.9406, 12.8793), (-15.7661, 12.0667), (-15.1961, 12.1522), (-15.0711, 13.2486),
                (-14.8177, 13.3814), (-12.5783, 13.4055), (-12.3644, 13.5456), (-9.6833, 13.2167),
                (-9.7500, 13.5830), (-8.9833, 13.1667), (-8.8383, 13.2344), (-5.9167, 13.9667)]

EXPERIENCIAS = [
    "Expedición 2022 por el sur de Angola (Paul Godard, 4 semanas, 2 vehículos): entrada por Santa Clara con e-visa (120 $/persona, 80 $ pagando en moneda local); ruta real Ondjiva → Xangongo → Calueque → cataratas de Ruacana → Epupa → Parque de Iona → desembocadura del Cunene → Namibe → Serra da Leba → Lubango → Tundavala → Kalandula → Pedras Negras → Kissama → Luanda. La EN140 la describen como «la peor carretera asfaltada jamás vista», con baches de hasta 80 cm; acampada libre en casi todo el trayecto, avisando siempre al jefe del pueblo o los ancianos locales.",
    "Cruce Zambia→Angola por Chavuma/Caripande (Africa Overland Blog, ruta este-oeste hasta Kalandula): oficina de inmigración angoleña descrita como «una sala diminuta y sucia, con agujeros de bala de la guerra civil»; trámite negociado en portugués. Más de 100 km de pistas de arena con charcos profundos y puentes de madera inestables; velocidad real de 10-20 km/h. Llevar cuerdas de remolque — ayudar a vehículos varados es una norma no escrita en estas pistas. Cruzaron en diciembre, al inicio de las lluvias, y lo describen como muy exigente: recomendable evitarlo en plena temporada húmeda (octubre-marzo).",
    "Baía dos Tigres (kumakonda.com): el paso de marea 'Doodsakker' solo es practicable con marea baja y luna llena o nueva; se recomienda mínimo 2 vehículos, equipo de recuperación y, si se quiere llegar a la propia isla, una embarcación auxiliar. Los operadores especializados insisten en que es una expedición que requiere planificación profesional, no un tramo para improvisar en solitario.",
    "Consejos generales de Tracks4Africa para overlanders en Angola: TIP (importación temporal) y seguro local de terceros obligatorios en cualquier frontera; llevar un embudo con filtro para el combustible, ya que la calidad del gasóleo/gasolina es irregular fuera de las grandes ciudades; la acampada libre está generalmente permitida en zonas remotas; los controles de policía a la entrada de los pueblos suelen ser correctos y sin problemas.",
    "Política de mascotas en Iona y Kissama: no se ha localizado ninguna normativa pública específica sobre perros en ninguno de los dos parques. Dado que ambos tienen depredadores grandes (Iona: guepardo, leopardo, hiena parda; Kissama: leones reintroducidos) o megafauna (elefantes en Kissama), la práctica habitual en parques africanos comparables es prohibirlos dentro del vehículo en zona de fauna — contactar directamente con African Parks (Iona) y con el operador de Kissama antes de viajar para confirmar, y tener un plan B (mirador de entrada, o turnos para quedarse con el perro fuera del parque).",
]

CORRIDOR_LABEL = "Bajada"
CORRIDOR_ALT_LABEL = "Subida"

HISTORIA_RESUMEN = ("Angola, heredera del gran reino de Ndongo y del reino de Kongo, sufrió casi cinco siglos de presencia colonial portuguesa centrada en la trata de esclavos hacia Brasil, y tras una independencia tardía en 1975 se sumió de inmediato en una guerra civil de 27 años "
                     "(1975-2002) que fue uno de los grandes escenarios de la Guerra Fría en África, con Cuba y la URSS apoyando al gobierno marxista y Sudáfrica y Estados Unidos a la guerrilla de UNITA; la paz de 2002 dio paso a un boom petrolero que ha transformado Luanda en una de las ciudades más caras del mundo.")

HISTORIA_SECCIONES = [
    ("Los reinos de Kongo y Ndongo",
     "El norte del actual territorio formó parte del reino de Kongo, mientras que el reino de Ndongo, gobernado en el siglo XVII por la célebre reina Nzinga Mbandi —hoy símbolo nacional de resistencia—, libró una larga lucha contra el avance portugués antes de sucumbir a la ocupación colonial."),
    ("Cinco siglos de colonización portuguesa y la trata de esclavos",
     "Portugal estableció su presencia en la costa angoleña ya en el siglo XV, y Angola se convirtió en uno de los mayores puntos de origen de la trata negrera atlántica, con millones de personas embarcadas hacia Brasil a lo largo de tres siglos; el dominio colonial portugués, uno de los más prolongados y tardíos en abandonar África, se mantuvo hasta 1975."),
    ("Independencia y la guerra civil de la Guerra Fría (1975-2002)",
     "Angola alcanzó la independencia en 1975 tras una guerra de liberación, pero la rivalidad entre los movimientos independentistas MPLA, UNITA y FNLA derivó de inmediato en una guerra civil que se convirtió en uno de los grandes conflictos por delegación de la Guerra Fría: Cuba y la Unión Soviética respaldaron al gobierno marxista del MPLA, mientras Sudáfrica del apartheid y Estados Unidos apoyaron a la guerrilla anticomunista de UNITA liderada por Jonas Savimbi; el conflicto se prolongó, con altibajos, hasta la muerte de Savimbi en 2002."),
    ("Situación actual: boom petrolero y desigualdad",
     "Desde el fin de la guerra, Angola ha vivido un notable boom económico basado en sus enormes reservas petroleras (una de las mayores de África) y, en menor medida, en diamantes, que ha convertido a Luanda en una de las capitales más caras del mundo para expatriados, conviviendo con una desigualdad social muy marcada; el partido MPLA, en el poder desde la independencia, mantiene el control político del país bajo el presidente João Lourenço desde 2017."),
]

HISTORIA_FUENTES = [
    ("BBC News · Angola country profile", "https://www.bbc.com/news/world-africa-13036732"),
    ("Encyclopaedia Britannica · Angola, History", "https://www.britannica.com/place/Angola/History"),
    ("Council on Foreign Relations · Angola's civil war", "https://www.cfr.org/timeline/angolas-civil-war"),
]

SPEC = dict(
    slug="angola", name="Angola", revision="11 sep 2026",
    sub="Corredor doble bajada/subida · documentación · seguridad · logística",
    chips=[
        ("BAJADA", "Lufu/Luvo → Malanje → altiplano de Huambo → Moxico → Caripande (Zambia) · ~2.600 km"),
        ("SUBIDA", "Santa Clara → Iona/Namibe → Leba/Tundavala → Benguela → Kissama → Luanda → Lufu/Luvo · ~2.400 km"),
        ("PDIs", "22 puntos repartidos entre los dos corredores, sin solapamiento salvo Luanda"),
        ("4x4 MÍTICO", "Baía dos Tigres (duna al mar) · Serra da Leba · Iona · pista de Tchitundu-Hulu"),
        ("A PIE", "Morro do Moco 2.620 m · Tundavala · base de Kalandula"),
        ("FAUNA CON PERRO", "Waku Kungo (hipopótamos fuera de parque) — la mejor opción del país"),
        ("VISADO", "exención de 30 días para españoles — verificar vigencia y doble entrada"),
        ("SEGURIDAD", "estable · precaución normal, aislamiento real en Moxico"),
    ],
    center=[-12.0, 15.5], zoom=5,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Angola se recorre DOS VECES en direcciones distintas: en la <strong>bajada</strong>, tras RD Congo, un eje corto por Luanda y un desvío interior a las cascadas de Kalandula y Pedras Negras antes de internarse hacia el este remoto de Moxico y cruzar a Zambia por Caripande/Cazombo; "
                   "en la <strong>subida</strong>, ya de vuelta desde Namibia, el país se cruza por el extremo suroeste — el desierto del Namibe, el Parque Nacional de Iona, Serra da Leba y Tundavala — antes de subir por la costa (Lobito, Kissama) hasta Luanda y salir de nuevo por Lufu/Luvo hacia RD Congo. "
                   "Los dos corredores solo comparten Luanda y la propia frontera del norte; el resto del país se ve por completo distinto en cada pasada."),
    facts=[
        ("Ventana prevista", "Bajada: tras RD Congo, antes de Zambia. Subida: tras Namibia, antes de continuar por RD Congo/Congo hacia el norte."),
        ("Entrada bajada", "Lufu/Luvo desde RD Congo; desvío opcional a M'banza-Kongo (UNESCO) a poca distancia."),
        ("Salida bajada", "Caripande, cerca de Cazombo, hacia Zambia (Chavuma): paso remoto, pistas de arena, solo en temporada seca."),
        ("Entrada subida", "Santa Clara/Oshikango desde Namibia (o Calueque/Ruacana como alternativa más al oeste)."),
        ("Salida subida", "Lufu/Luvo hacia RD Congo, cerrando el corredor angoleño antes de continuar la subida por Congo/Camerún."),
        ("Visado", "Exención de visado de turismo de 30 días para pasaportes españoles a fecha de esta revisión — confirmar vigencia 30-60 días antes; comprobar también si permite las dos entradas (bajada y subida) o si hace falta e-Visa de entrada múltiple."),
        ("Seguridad", "Estable en todo el país, precaución normal; el único tramo que exige planificación adicional es el extremo este (Moxico) en la bajada, por aislamiento y estado de las pistas, no por inseguridad."),
        ("Comunicaciones", "Starlink anunciado para 2026, no confirmado activo; SIM local (Unitel, Africell) como base, con cobertura muy limitada en el tramo de Moxico."),
    ],
    alerts=[
        "Visado: la exención de 30 días para españoles debe reconfirmarse 30-60 días antes de viajar — Angola ha ajustado su política de visados varias veces en los últimos años; si hay cualquier duda, tramitar el e-Visa como respaldo, y verificar expresamente si admite dos entradas separadas (bajada y subida) dentro del mismo viaje.",
        "Reentrada: al tratarse de un corredor doble (se sale hacia Zambia y se vuelve a entrar meses después desde Namibia), confirmar con la representación consular angoleña si la exención de 30 días cubre dos entradas o si hace falta gestionar dos trámites distintos.",
        "Tramo Malanje–Cazombo (bajada): más de 100 km de pista de arena con posibles charcos profundos y puentes de madera; viajar solo en temporada seca (mayo-septiembre) y llevar combustible y agua de reserva — la oferta de ambos es escasa a partir de Malanje.",
        "M'banza-Kongo: desvío que añade tiempo y pista adicional cerca de la frontera de entrada — valorar según el calendario general del tramo centroafricano, que ya acumula varias fronteras complejas seguidas.",
        "Baía dos Tigres: tramo avanzado que depende de mareas y fase lunar; no intentarlo sin al menos 2 vehículos y, idealmente, apoyo de un operador local (p. ej. Sandura Tours) — tratarlo como opcional según tiempo y experiencia del grupo en arena.",
    ],
    ruta_intro=("Angola se cruza dos veces por regiones completamente distintas: la bajada por el interior "
                "(Luanda → Malanje → altiplano de Huambo → Bié → Moxico) hasta Zambia, y la subida por el suroeste "
                "desértico (Iona, Namibe, Serra da Leba, Tundavala) y la costa hasta Luanda. Etapas calculadas sobre "
                "una media de <strong>250 km/día</strong>: ~2.600 km en la bajada (unos 14-16 días con paradas) y "
                "~2.400 km en la subida (unos 14-18 días, más lentos por las pistas del desierto)."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bajada 1 · Entrada y capital", "Lufu/Luvo → (M'banza-Kongo, UNESCO, opcional) → Luanda", "~350 km · 2-3 días con el desvío"),
        ("Bajada 2 · Salida de Luanda", "Luanda → Miradouro da Lua → Malanje", "~400 km · 2 días"),
        ("Bajada 3 · Triángulo de Malanje", "Pedras Negras → Kalandula → Cangandala (palanca negra)", "~250 km en bucle · 3 días"),
        ("Bajada 4 · Altiplano de Kwanza Sul", "Malanje → Waku Kungo (hipopótamos y cafetales)", "~450 km · 2-3 días"),
        ("Bajada 5 · Reino y techo de Angola", "Waku Kungo → Bailundo → Morro do Moco (2.620 m) → Huambo", "~300 km · 3-4 días con la subida a pie al Moco"),
        ("Bajada 6 · Travesía del este", "Huambo → Kuito → Luena", "~650 km · 3 días, asfalto degradado"),
        ("Bajada 7 · Moxico remoto y frontera", "Luena → Cazombo → Caripande (frontera de Zambia)", "~450 km · 3-4 días de pista; solo temporada seca"),
        ("Subida 1 · Entrada y desierto", "Santa Clara/Oshikango (o Calueque/Ruacana) → Parque de Iona → Foz do Cunene", "~500 km · 3-4 días, pista lenta"),
        ("Subida 2 · Costa del Namibe", "Foz do Cunene → Baía dos Tigres (opcional, avanzado) → Tombwa", "~250 km · 2-3 días si se hace Tigres"),
        ("Subida 3 · Arte rupestre y oasis", "Tombwa → Tchitundu-Hulu (Virei) → Lagoa do Arco → Namibe", "~450 km · 3 días, todo pista"),
        ("Subida 4 · Puerto de montaña y fenda", "Namibe → Serra da Leba → Lubango → Tundavala", "~250 km · 2-3 días"),
        ("Subida 5 · Bajada a la costa", "Lubango → Benguela → Lobito", "~500 km · 2-3 días"),
        ("Subida 6 · Costa de Luanda y cierre", "Lobito → Cabo Ledo → Kissama → Mussulo → Luanda → Lufu/Luvo", "~800 km · 4-5 días"),
    ],
    offroad=[
        "Baía dos Tigres (avanzado, opcional): EL tramo mítico de 'duna que llega al mar' del sur de Angola, a través del paso de marea 'Doodsakker' desde Tombwa — solo con marea baja y luna llena o nueva, mínimo 2 vehículos y equipo de recuperación. Encaja exactamente con lo que buscamos para el bloque sur, pero exige preparación experta o guía local.",
        "Serra da Leba (EN280): el puerto de montaña más icónico de Angola, con curvas de herradura cerradas subiendo de ~720 m a 1.845 m entre Namibe y Lubango; asfaltado pero exigente, parada fotográfica obligada con los 4x4.",
        "Parque Nacional de Iona: pistas de arena y tierra por paisaje semidesértico sin señalización fija; jornada completa desde Namibe, GPX o guía recomendado.",
        "Pista a Tchitundu-Hulu (Virei): 150 km al sur de Moçâmedes y 37 km más al suroeste de Virei por pista de semidesierto hasta los inselbergs del arte rupestre; sin servicios en todo el trayecto, autonomía completa de agua y combustible.",
        "Acceso a la Lagoa do Arco: pista de arena y roca por el desierto hasta el oasis; la propia aldea de Njambasana gestiona aparcamiento y camping, así que es el vivac natural del tramo.",
        "Tundavala: pista de tierra de ~18 km desde Lubango hasta el borde de la fenda (2.200 m); terreno suelto en tramos, correa corta para el perro en el propio mirador por el desnivel de más de 1.000 m.",
        "Tramo Luena–Cazombo–Caripande (bajada): más de 100 km de arena profunda con charcos y puentes de madera, y barro intransitable en temporada de lluvias según relatos de otros overlanders; velocidades reales de 10-20 km/h. En temporada seca es largo pero asumible con 4x4 estándar.",
        "Acceso al Morro do Moco: pista desde Huambo hasta Kanjonde (~70 km) y después a pie; la pista final es de tierra y empeora en lluvias.",
    ],
    senderismo=[
        "Morro do Moco (2.620 m), Huambo: LA gran excursión a pie del país. Subida al punto más alto de Angola desde la aldea de Kanjonde, atravesando los últimos bosques afromontanos; guía local de la aldea imprescindible (no hay sendero señalizado ni estatus de protección). Jornada completa, mejor entre julio y septiembre, cuando florecen las proteas. 233 especies de aves, varias endémicas.",
        "Tundavala (Huíla): varios senderos cortos por el borde del escarpe de la meseta de Humpata, con vistas de más de 10.000 km² y un desnivel de 1.000 m a los pies. Sin protección en el borde: extremar precaución y llevar al perro con correa corta.",
        "Cascadas de Kalandula (Malanje): sendero empinado que baja hasta la base del salto para verlo desde abajo, entre la niebla de agua y el arcoíris permanente. Resbaladizo; calzado con suela agarrada.",
        "Pedras Negras de Pungo Andongo (Malanje): rutas cortas entre los monolitos de granito, incluyendo las huellas talladas atribuidas a la reina Nzinga y las ruinas del fuerte portugués.",
        "Fenda do Bimbi (Huíla): otra grieta del escarpe cerca de Lubango, menos conocida que Tundavala y habitual como caminata corta entre los viajeros que pasan por la zona; confirmar acceso y estado del sendero en Lubango antes de ir.",
        "Serra da Leba: se puede caminar por el borde del escarpe junto al mirador del puerto, con los cerros y las curvas de herradura a la vista.",
    ],
    acampada=[
        "Pedras Negras: vivac salvaje entre los bloques de granito, citado por otros overlanders como uno de los mejores del país; pedir permiso o avisar en el pueblo más cercano.",
        "Lagoa do Arco: camping básico de gestión comunitaria montado por la aldea de Njambasana, con aparcamiento y tasa — la pernocta organizada más cómoda del desierto del Namibe.",
        "Kanjonde (pie del Morro do Moco): pernocta en la aldea o junto a ella, acordada con el guía local, como base para subir al amanecer.",
        "Cabo Ledo: camping y alojamientos sencillos junto a la playa; el mejor sitio del país para parar dos días con el perro.",
        "Luanda: alojamientos con parking vigilado, opción más práctica que la acampada libre en la capital.",
        "Benguela, Lobito, Namibe, Lubango y Huambo: hoteles con aparcamiento; bases urbanas de cada tramo.",
        "Tramo de Moxico (bajada): acampada libre habitual, pero registrarse siempre en la policía local (práctica confirmada en Cazombo por otros viajeros) y pedir orientación a los ancianos del pueblo sobre el estado de la pista.",
    ],
    visado=[
        "Exención de visado de turismo (30 días) para pasaportes españoles a fecha de esta revisión; confirmar vigencia 30-60 días antes de viajar.",
        "Confirmar expresamente si la exención permite dos entradas (bajada y subida) dentro del mismo viaje o si hace falta gestionar el e-Visa de entrada múltiple con antelación.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Lufu/Luvo (RD Congo)", "Cruce del puente fronterizo; registro y sellado ~500 m dentro de Angola; desvío opcional a M'banza-Kongo cerca de aquí."),
        ("Salida bajada", "Caripande, cerca de Cazombo (Zambia)", "Paso remoto en Moxico; oficina angoleña muy precaria según otros overlanders, trámite en portugués; solo en temporada seca."),
        ("Entrada subida", "Santa Clara/Oshikango (Namibia)", "Paso más transitado hacia Namibia; carretera asfaltada e infraestructura de control moderna en ambos lados."),
        ("Alternativa entrada subida", "Calueque/Ruacana (Namibia)", "Más al oeste, junto a la presa de Calueque; pista sin asfaltar pero acceso directo a Ruacana, Epupa e Iona."),
        ("Salida subida", "Lufu/Luvo (RD Congo)", "Mismo paso que la entrada de la bajada, cerrando el corredor angoleño antes de continuar la subida hacia el norte."),
    ],
    vehiculos=[
        "CPD recomendado; confirmar si Angola exige también una importación temporal adicional del vehículo, dado que el país no pertenece a CEDEAO ni a CEMAC.",
        "Seguro de responsabilidad civil local obligatorio: contratarlo al entrar por Lufu/Luvo o Santa Clara si no se dispone de cobertura previa válida.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
        "Depósitos y garrafas de combustible/agua llenos antes de Malanje→Cazombo (bajada) y antes de Namibe→Baía dos Tigres/Iona (subida): son los dos tramos del país sin garantía de suministro.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa por escrito al INAVIC antes de intentar introducir el dron en el país.",
        "No volar cerca de instalaciones petroleras o portuarias (Luanda, Lobito), de la presa de Calueque, ni de zonas militares o de los parques nacionales sin autorización expresa.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado no confirmado a mediados de 2026 pese al anuncio de llegada dentro del año: revisar el mapa oficial 30-60 días antes.",
        "SIM local (Unitel, Africell) como conectividad principal en Luanda y el eje costero; no dar por hecha cobertura móvil en el tramo remoto de Moxico.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE).",
        "Ver la matriz por zona más abajo: los dos parques nacionales (Iona, Kissama) son la única duda seria pendiente de confirmar.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio, con mayor intensidad en el norte: profilaxis a valorar con Sanidad Exterior.",
        "Hospital Américo Boavida (Luanda) y Hospital Central da Huíla (Lubango) como referencias hospitalarias de cada corredor; seguro con evacuación médica imprescindible, sobre todo en el tramo remoto de Moxico.",
    ],
    seguridad_intro="País estable con precaución normal en todo el corredor previsto; el único factor a gestionar con cuidado es el aislamiento del tramo de Moxico (bajada) y la logística de mareas de Baía dos Tigres (subida), no la inseguridad.",
    seguridad=[
        "Sin zonas excluidas por seguridad en ninguno de los dos corredores previstos.",
        "Extremar la precaución documental en el cruce de Lufu/Luvo: primer país fuera de las zonas de seguro regional CEDEAO/CEMAC del tramo.",
        "Tramo de Moxico (bajada): aislamiento real más que inseguridad — llevar siempre combustible, agua y comida de reserva, y registrarse en la policía local como hacen otros overlanders.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
    ],
    agua=[
        "Luanda: agua embotellada en supermercados sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio y hoteles de Luanda, Lobito y Namibe permiten llenar el depósito con manguera; confirmar en recepción.",
        "Tramo de Moxico y Baía dos Tigres: sin garantía ninguna — salir con depósitos llenos al 100%.",
    ],
    combustible=[
        "Bajada: sin riesgo de gap de 500 km hasta Malanje (Lufu/Luvo → Luanda ~350 km → Malanje ~350 km, con estaciones formales en cada núcleo); a partir de Malanje hacia Cazombo la oferta se espacía mucho — depósitos llenos y garrafas de reserva.",
        "Subida: Santa Clara/Oshikango → Namibe (~300 km) con oferta razonable; sin garantía entre Namibe y Baía dos Tigres/Iona — llenar en Namibe. Namibe → Lubango (Serra da Leba) → Lobito → Luanda con estaciones formales en cada ciudad.",
    ],
    experiencias_intro="Relatos y comentarios reales de otros overlanders sobre Angola, para contrastar con la planificación oficial de esta ficha:",
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Visado de doble entrada", "Confirmar si la exención de 30 días cubre las dos pasadas (bajada y subida) o si hace falta e-Visa de entrada múltiple"),
        ("Frontera Caripande/Cazombo", "Confirmar horario, estado real de la pista y si el trámite acepta inglés o solo portugués, 30-60 días antes"),
        ("Perro en Iona, Kissama y Cangandala", "Contactar con African Parks (Iona) y el INBAC (Kissama, Cangandala) para confirmar si el perro puede ir en el vehículo dentro del parque"),
        ("Cangandala · acceso real", "Confirmar con el INBAC si el parque está ya abierto al público, cuál es la puerta de entrada y su coordenada exacta, y si la palanca negra gigante es avistable sin guía oficial"),
        ("Morro do Moco · guía local", "Contactar con la aldea de Kanjonde para la subida a pie y confirmar si el perro puede acompañar o se queda en el vehículo en la aldea"),
        ("Lagoa do Arco · ¿tiene agua?", "Confirmar antes de desviarse: estuvo seca varios años tras las lluvias fallidas de 2013-2014"),
        ("Bicuar (Huíla)", "Parque en reconstrucción con elefantes volviendo; confirmar si es visitable en 2027 y si compensa el desvío de 120 km desde Lubango"),
        ("Fotos pendientes de sustituir", "Bailundo, Tchitundu-Hulu y Foz do Cunene usan imágenes de referencia de su región, no del propio sitio: sustituir por fotos propias cuando las tengamos"),
        ("Baía dos Tigres", "Decidir si se intenta en solitario (2 vehículos + mareas) o se contrata apoyo local, y si encaja en el calendario del bloque sur"),
        ("M'banza-Kongo", "Decidir si el desvío UNESCO entra en el calendario del tramo centroafricano"),
        ("Seguro e importación del vehículo", "Confirmar el procedimiento exacto al entrar por Lufu/Luvo y por Santa Clara, fuera de CEDEAO/CEMAC"),
        ("Dron", "Contactar con el INAVIC o descartar el vuelo en el país"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 11 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Luanda): +244 929 900 900 · Embajada: +244 222 391 166.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

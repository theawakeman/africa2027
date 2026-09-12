# -*- coding: utf-8 -*-
"""Malaui — ficha completa (12 sep 2026): ALTERNATIVA al bucle sur/este, no está en la ruta fija.

Encaja insertándose en el bucle entre Tanzania y Mozambique (y, en una variante menor, con Zambia).
Se escribe como alternativa real: con el coste en kilómetros y días calculado, para poder decidir.
"""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

# --- Imágenes verificadas del proyecto -------------------------------------------------------
# En esta revisión NO se pudo abrir commons.wikimedia.org desde el entorno de trabajo (dominio
# bloqueado por el proxy) ni verificar nombres de archivo nuevos. Para no colgar ninguna imagen
# rota, se reutilizan ÚNICAMENTE las cinco fotos de Malaui ya verificadas dentro del proyecto y
# cada PDI que usa una foto que no es suya lo dice expresamente en su descripción.
IMG_ZOMBA = W + "Zomba%20Plateau.jpg?width=900"
IMG_LIWONDE = W + "Elephants%20in%20Liwonde%20National%20Park.JPG?width=900"
IMG_CAPE = W + "Otter%20Point%2C%20Cape%20Maclear%20(Malawi).jpg?width=900"
IMG_LILONGWE = W + "Lilongwe%2C%20Malawi.JPG?width=900"
IMG_LAGO = W + "Lake%20malawi%20mozambico%20coast.jpg?width=900"

_F = " (Foto provisional: %s — pendiente de sustituir por una de este punto.)"

POIS = [
    # ===== NORTE: entrada desde Tanzania por Songwe =====
    dict(n=1, name="Karonga y el Centro Cultural y Museo", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½–1 día",
         lat=-9.9333, lon=33.9333,
         desc="Primera ciudad al entrar desde Tanzania, a 478 m sobre la orilla noroeste del lago y a unos 45 km de la frontera de Songwe. Su Cultural & Museum Centre es la mejor parada cultural del norte: expone el MALAWISAURUS, dinosaurio saurópodo hallado en la zona, y la mandíbula de homínido de Malema (excavaciones del profesor Friedemann Schrenk, a 10 km de la ciudad), con una muestra titulada «From Dinosaurs to Democracy» que recorre toda la historia local. Karonga es además el sitio donde repostar y comprar antes de subir al escarpe." + _F % "la costa del lago Malaui",
         credit="Wikimedia Commons", source=IMG_LAGO),
    dict(n=2, name="Livingstonia y la carretera de las curvas de herradura", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-10.6083, lon=34.1167,
         desc="LA PARADA MÍTICA DEL NORTE. La misión escocesa se fundó en 1894 tras dos intentos fallidos —Cabo Maclear (1875) y Bandawe— abandonados por la malaria: solo funcionó al subirla a la meseta, por encima de los mosquitos. Robert Laws la dirigió 52 años; se conserva la Stone House (su casa, hoy hotel con museo), la iglesia de vidrieras y el hospital David Gordon Memorial (1911). Pero lo que la hace imprescindible para este viaje es el ACCESO: la carretera S103/T305 sube desde Chitimba los ~15 km del escarpe en una sucesión de unas veinte curvas de herradura sin quitamiedos, con el lago abriéndose 900 m más abajo. Es el tramo 4x4 más famoso de Malaui." + _F % "la meseta de Zomba, paisaje de altura equivalente",
         credit="Wikimedia Commons", source=IMG_ZOMBA),
    dict(n=3, name="Cataratas de Manchewe", cat="Naturaleza", prio="Media", dog="permitido con correa", time="½ día",
         lat=-10.6167, lon=34.1333,
         desc="Justo antes de llegar a Livingstonia, el río se despeña por el escarpe en una caída larga y estrecha sobre la garganta, con la llanura del lago al fondo. Hay sendero hasta el mirador y una bajada corta y resbaladiza hasta una cueva detrás de la cortina de agua, que la tradición local vincula a los escondites usados durante la trata de esclavos (relato local, no dato documentado). Sin vallas en los bordes: correa corta con el perro. Coordenada aproximada, verificar sobre el terreno." + _F % "la meseta de Zomba",
         credit="Wikimedia Commons", source=IMG_ZOMBA),
    dict(n=4, name="Meseta de Nyika · Parque Nacional de Nyika", cat="Naturaleza", prio="Alta", dog="prohibido", time="3–4 días",
         lat=-10.5667, lon=33.8000,
         desc="EL PARQUE MÁS GRANDE DEL PAÍS (3.200 km², creado en 1966 y ampliado en 1978) y el paisaje más inesperado de África oriental: praderas de altura ondulando entre 2.000 y 2.600 m, sin árboles, con antílopes (desde duikers hasta elands), cebras, más de 400 especies de aves —incluida la avutarda de Denham— y una de las densidades de leopardo más altas de África central. Más de 200 especies de orquídeas florecen con las lluvias. El propio nombre significa «de donde viene el agua». La meseta hace de frontera con Zambia. Se accede por una única pista de tierra que sube el escarpe suroeste desde el eje Rumphi-Katumbi hasta Chelinda, el campamento central, recientemente rehabilitado. Se recorre en 4x4, a pie y —cosa rarísima en un parque africano— también en bicicleta de montaña." + _F % "la meseta de Zomba, otra pradera de altura malauí",
         credit="Wikimedia Commons", source=IMG_ZOMBA),
    dict(n=5, name="Mzuzu", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-11.4581, lon=34.0150,
         desc="Capital del Norte y tercera ciudad del país (221.000 hab.), encajada en un paso de los montes Viphya sobre la M1. Es la plaza logística de todo el bloque norte: bancos, supermercados, talleres, hospital y combustible antes de meterse en Nyika, en Livingstonia o en la costa. De aquí arranca la M5 hacia Nkhata Bay, cruzando el mayor bosque plantado de África (Viphya/Chikangawa), un tramo de pinos y niebla que no parece África." + _F % "Lilongüe",
         credit="Wikimedia Commons", source=IMG_LILONGWE),
    dict(n=6, name="Nkhata Bay", cat="Costa", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-11.6000, lon=34.3000,
         desc="El puerto principal de la orilla norte y el gran clásico del circuito overland de África oriental: una ensenada tropical de agua transparente entre cerros boscosos, con casas colgadas sobre la roca. Escala fija del vapor MV Ilala. Su escuela de buceo llegó a ser citada por The Daily Telegraph como el curso de submarinismo más barato del mundo: aquí se bucea en agua dulce entre cardúmenes de cíclidos mbuna de colores. Alojamientos junto al agua muy tolerantes con el perro." + _F % "la costa del lago Malaui",
         credit="Wikimedia Commons", source=IMG_LAGO),
    dict(n=7, name="Chintheche y la costa de Bandawe", cat="Costa", prio="Alta", dog="permitido", time="1–2 noches",
         lat=-11.8500, lon=34.1667,
         desc="El mejor tramo de playa abierta del lago: 40 km de arena blanca, baobabs y agua poco profunda entre Nkhata Bay y Dwangwa, con los campamentos que usan todos los camiones de expedición. Aquí estuvo la segunda misión escocesa, Bandawe, abandonada como la primera por la malaria; queda el cementerio misionero junto a la playa, con lápidas de gente que murió a los veintipocos años. Es el sitio del país donde el perro está más cómodo: playa abierta, sombra y campings con parcela." + _F % "la costa del lago Malaui",
         credit="Wikimedia Commons", source=IMG_LAGO),
    dict(n=8, name="Likoma y la catedral de San Pedro", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="2–3 días (sin vehículo)",
         lat=-12.0667, lon=34.7333,
         desc="UNA RAREZA GEOPOLÍTICA Y ARQUITECTÓNICA. Likoma (18 km², unos 10.000 habitantes) y la vecina Chizumulu son EXCLAVES DE MALAUI ENTERAMENTE RODEADOS DE AGUAS TERRITORIALES MOZAMBIQUEÑAS, a 7 km de Cobué (Mozambique). En el pueblo de Mbamba se levanta la catedral anglicana de San Pedro, una de las iglesias más grandes de África —construida a escala de catedral inglesa en una isla sin carreteras, por la Universities' Mission to Central Africa—, con sillería de coro y vidrieras. Se llega en el MV Ilala (escala semanal) o en avioneta; el vehículo se queda en tierra, así que es una escapada de mochila de dos o tres días." + _F % "el lago Malaui desde la costa mozambiqueña, las aguas que rodean Likoma",
         credit="Wikimedia Commons", source=IMG_LAGO),
    # ===== CENTRO =====
    dict(n=9, name="Reserva de Nkhotakota (African Parks)", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 días",
         lat=-12.9167, lon=34.0000,
         desc="La reserva más antigua y más grande del país (1.800 km²), desde el escarpe a 1.638 m hasta la orilla del lago, con miombo, dambos, bosque de galería y gargantas de río. Fue el escenario de UNA DE LAS MAYORES TRASLOCACIONES DE ELEFANTES DE LA HISTORIA: entre 2016 y 2017 African Parks movió unos 500 elefantes desde Liwonde y Majete hasta aquí, después de que la población hubiera caído de 1.500 a menos de 100 por la caza furtiva. Hoy tiene más de 280 especies de aves y han reaparecido el antílope ruano y el ratel. Se visita desde el río Bua; alojamientos Tongole Wilderness y Bua River Lodge." + _F % "elefantes en Liwonde, el parque de origen de los 500 trasladados aquí",
         credit="Brian Dell · dominio público", source=IMG_LIWONDE),
    dict(n=10, name="Nkhotakota, la capital histórica de la trata", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=-12.9167, lon=34.3000,
         desc="Uno de los asentamientos más antiguos y peculiares del lago: fue el cuartel general del jefe esclavista suajili Jumbe, punto de embarque de miles de personas esclavizadas que cruzaban el lago hacia Kilwa, y por eso mismo el lugar donde David Livingstone intentó en 1863 convencer al Jumbe de que abandonara la trata, bajo una higuera que aún se señala junto a la misión anglicana. Es la parada histórica que explica por qué existe todo lo demás: las misiones, Livingstonia, el protectorado." + _F % "la costa del lago Malaui",
         credit="Wikimedia Commons", source=IMG_LAGO),
    dict(n=11, name="Senga Bay y Salima", cat="Costa", prio="Media", dog="permitido", time="1–2 noches",
         lat=-13.7667, lon=34.6167,
         desc="La playa del lago más cercana a la capital (~105 km de Lilongüe), y por eso la más fácil de encajar aunque se recorte el viaje: arena, granito, pescadores y las islas Marelli/Nankoma a un paseo en barca, con águilas pescadoras y cormoranes. Escala del MV Ilala. Buena oferta de campings con parcela para vehículo y perro. Punto natural para descansar antes o después del bloque de la capital." + _F % "la costa del lago Malaui",
         credit="Wikimedia Commons", source=IMG_LAGO),
    dict(n=12, name="Parque Nacional de Kasungu", cat="Naturaleza", prio="Media", dog="prohibido", time="1–2 días",
         lat=-13.0333, lon=33.1667,
         desc="Segundo parque del país (2.316 km², creado en 1970), a ~175 km al norte de Lilongüe y pegado a la frontera zambiana, a unos 1.000 m: miombo abierto, dambos herbáceos y los ríos Dwangwa y Lingadzi con hipopótamos. Tiene elefantes (en julio de 2022 el IFAW trasladó aquí 263 más, una operación que generó un conflicto real con las comunidades vecinas por muertes y daños en cultivos, con demandas de compensación en curso), antílopes sable, kudús, cebras, búfalos, hienas, licaones y servales; es Unidad de Conservación del León desde 2005. Suele cerrar en marzo por las lluvias; mejor de junio a septiembre. Es un parque poco visitado, barato y sin multitudes." + _F % "elefantes en Liwonde",
         credit="Brian Dell · dominio público", source=IMG_LIWONDE),
    dict(n=13, name="Lilongüe", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-13.9833, lon=33.7681,
         desc="Capital política desde 1975 (casi un millón de habitantes, a 1.050 m), dividida en Old Town —mercados, transporte, la vida real— y City Centre —ministerios, embajadas, hoteles—. Es la mejor plaza logística del país junto con Blantyre: talleres, recambios, neumáticos, supermercados grandes, bancos, y el Kamuzu Central Hospital como referencia sanitaria. Aquí se tramitan los permisos (perro, dron) y aquí está el Lilongwe Wildlife Centre, único santuario de fauna rescatada del país. A 110 km de la frontera zambiana de Mchinji.",
         credit="NASA Astronauts · dominio público", source=IMG_LILONGWE),
    dict(n=14, name="Arte rupestre de Chongoni (UNESCO) y Dedza", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con correa", time="1 día",
         lat=-14.2933, lon=34.2792,
         desc="PATRIMONIO MUNDIAL DESDE 2006 Y EL CONJUNTO DE ARTE RUPESTRE MÁS DENSO DE ÁFRICA CENTRAL: 127 yacimientos en 126,4 km² de colinas graníticas boscosas, a unos 80 km al sureste de Lilongüe. Dos tradiciones superpuestas: los cazadores-recolectores BaTwa, que pintaron en rojo, y los agricultores chewa, que pintaron en blanco, en un arte ligado a los ritos de iniciación femenina, a las ceremonias de lluvia y a los funerales, y todavía vivo en la sociedad secreta NYAU y sus máscaras gule wamkulu. Tres conjuntos están abiertos al público: Chentcherere (seis abrigos), Namzeze (geométricos rojos y pinturas blancas) y Mphunzi (figuras de animales). La base es Dedza (1.590 m, la ciudad más alta de Malaui, a 85 km de la capital por la M1), con su alfarería y su montaña de 2.198 m." + _F % "la meseta de Zomba",
         credit="Wikimedia Commons", source=IMG_ZOMBA),
    dict(n=15, name="Mua · Centro Kungoni de Cultura y Arte", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=-14.2167, lon=34.5333,
         desc="Misión católica en el escarpe entre Dedza y el lago que alberga el Chamare Museum, la mejor colección etnográfica del país: tres salas dedicadas a chewa, ngoni y yao, con centenares de máscaras GULE WAMKULU (la danza de los espíritus, Patrimonio Inmaterial de la UNESCO) explicadas una a una, más un taller de talla en madera. Es la pieza que da sentido al arte rupestre de Chongoni y a la sociedad Nyau. Coordenada aproximada: verificar." + _F % "Lilongüe",
         credit="Wikimedia Commons", source=IMG_LILONGWE),
    # ===== EL LAGO Y EL SUR =====
    dict(n=16, name="Cabo Maclear y el Parque Nacional del Lago Malaui (UNESCO)", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="3–4 noches",
         lat=-14.0206, lon=34.8306,
         desc="EL CORAZÓN DEL PAÍS Y EL MOTIVO POR EL QUE SE VIENE. Patrimonio Mundial desde 1984 y primer parque nacional de agua dulce del mundo creado para proteger peces: 94 km² en el extremo sur del lago, con 13 islas (Mumbo, Domwe, Thumbi West y East, Otter, Zimbabwe…) y unas 700 especies de CÍCLIDOS, casi todas endémicas, muchas aún sin describir y algunas limitadas a una sola roca. Es un caso de radiación adaptativa comparado con los pinzones de Darwin, y hace del lago Malaui el lago con MÁS ESPECIES DE PECES DEL MUNDO. Chembe, en Cabo Maclear, es el mayor pueblo de pescadores dentro del parque y la base de todo: kayak a Domwe y Mumbo, snorkel en Otter Point sobre bancos de mbuna naranjas y azules, barcas al atardecer con águilas pescadoras. OJO: el baño en el lago implica riesgo real de bilharzia (ver la sección de salud).",
         dog_note="Chembe es un pueblo habitado dentro del parque y sus campings y lodges de playa aceptan perro sin problema: es una de las mejores bases caninas del viaje. Lo que NO se puede es entrar con él en las zonas de parque propiamente dichas ni subirlo a las excursiones en barca a las islas. Y no dejarle beber ni bañarse sin haber consultado antes lo de la bilharzia con el veterinario.",
         credit="Hans Hillewaert · CC BY-SA 4.0", source=IMG_CAPE),
    dict(n=17, name="Parque Nacional de Liwonde (African Parks)", cat="Naturaleza", prio="Alta", dog="prohibido", time="2–3 días",
         lat=-14.8333, lon=35.3167,
         desc="548 km² a lo largo de 30 km del río Shire y la orilla del lago Malombe, gestionado por African Parks desde agosto de 2015 y convertido en la historia de recuperación más espectacular de África austral: rinocerontes negros (17 traídos de Sudáfrica en noviembre de 2019, sobre el núcleo del santuario vallado de 1993), los PRIMEROS GUEPARDOS SALVAJES DE MALAUI EN VEINTE AÑOS (siete en mayo de 2017, hoy 21) y leones reintroducidos a principios de 2018, con la primera cría nacida en 2020. Elefantes en cantidad, hipopótamos y cocodrilos a docenas y una de las mejores listas de aves de la región. Safaris en vehículo y —lo que lo hace distinto— en barca por el Shire. Alojamientos Mvuu, Kutengo y Chimwala.",
         credit="Brian Dell · dominio público", source=IMG_LIWONDE),
    dict(n=18, name="Zomba y su meseta", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-15.3833, lon=35.3167,
         desc="Antigua capital colonial a los pies de una meseta de sienita granítica de 130 km² que culmina a 2.087 m, partida en dos por el valle de Domasi (Zomba al sur, Malosa al norte). Arriba: pinares, retazos de bosque de niebla original, fresas y moras silvestres, el embalse de Mulunguzi (2000), miradores sobre todo el valle del Shire y la carretera panorámica de subida y bajada en sentido único, una de las conducciones más bonitas del país. La ciudad conserva el trazado colonial, el jardín botánico y el mercado. Es el mejor sitio del sur para dormir fresco.",
         credit="Dr. Ferdinand Groeger · CC BY-SA 3.0", source=IMG_ZOMBA),
    dict(n=19, name="Blantyre", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=-15.7861, lon=35.0058,
         desc="Capital comercial e industrial (800.000 hab., a 1.039 m), fundada por misioneros escoceses y bautizada con el pueblo natal de Livingstone. Es la mejor plaza de servicios del sur: talleres, recambios, seguros y el Queen Elizabeth Central Hospital, principal hospital de referencia del país. Dos visitas que merecen la parada: la iglesia de St Michael and All Angels (1891), levantada por albañiles locales sin ningún conocimiento de arquitectura europea y con un resultado asombroso, y la Mandala House (1882), el edificio más antiguo de Malaui, hoy monumento nacional con biblioteca, galería y café. Rodeada de montes: Soche, Ndirande, Michiru y Chiradzulu." + _F % "Lilongüe",
         credit="Wikimedia Commons", source=IMG_LILONGWE),
    dict(n=20, name="Monte Mulanje · Sapitwa 3.002 m (UNESCO 2025)", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="3–5 días",
         lat=-15.9667, lon=35.6333,
         desc="UNA DE LAS GRANDES MONTAÑAS DE SENDERISMO DE ÁFRICA. Inselberg colosal formado por una intrusión magmática hace unos 130 millones de años, que se levanta de golpe sobre los cultivos de té a 65 km al este de Blantyre y culmina en SAPITWA (3.002 m), el punto más alto de Malaui y de toda África central-meridional al norte del Drakensberg. Arriba no hay pico sino una meseta ondulada de pradera a 1.800-2.200 m recortada por barrancos boscosos, con refugios de montaña repartidos (Chambe, Lichenya, Thuchila, Chinzama, Sombani, Minunu, Chisepo) que permiten travesías de varios días. La cara oeste del pico Chambe es LA ESCALADA EN ROCA MÁS LARGA DE ÁFRICA. Alberga el cedro de Mulanje (Widdringtonia whytei), árbol nacional, en peligro crítico por la tala ilegal pese a la plantación de 250.000 plantones al año. En 2025 fue inscrito como Patrimonio Mundial en la categoría de PAISAJE CULTURAL: la montaña es residencia de espíritus en la tradición local." + _F % "la meseta de Zomba",
         credit="Wikimedia Commons", source=IMG_ZOMBA),
    dict(n=21, name="Plantaciones de té de Thyolo y Mulanje", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½–1 día",
         lat=-16.0667, lon=35.1333,
         desc="Malaui fue el primer país de África donde se cultivó té con éxito comercial, y las laderas de Thyolo y Mulanje siguen siendo un mar verde de setos recortados entre neblina, con casas coloniales de plantación y fincas que ofrecen visita de fábrica, cata y alojamiento (la más conocida es Satemwa, en Thyolo, que también produce té blanco y de autor). Es el contrapunto amable al esfuerzo de Mulanje y una conducción preciosa entre Blantyre, Thyolo y Mulanje." + _F % "la meseta de Zomba",
         credit="Wikimedia Commons", source=IMG_ZOMBA),
    dict(n=22, name="Reserva de Majete (African Parks)", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 días",
         lat=-15.9700, lon=34.7597,
         desc="700 km² en el bajo valle del Shire, junto a las cataratas de Kapachira y a poco más de una hora de Blantyre. En 2003 African Parks firmó aquí su PRIMER ACUERDO EN EL MUNDO, con una reserva que era «reserva solo de nombre», vaciada por la caza furtiva; hoy tiene más de 12.000 animales y en agosto de 2012, con la reintroducción de los leones, se convirtió en la PRIMERA RESERVA DE BIG FIVE DE MALAUI (búfalo, elefante, leopardo, león y rinoceronte). Los visitantes pasaron de casi cero a unos 7.000 al año. Admite autoconducción por su red de pistas y tiene campamento propio (Thawale) además del lodge Mkulumadzi sobre el río." + _F % "elefantes en Liwonde",
         credit="Brian Dell · dominio público", source=IMG_LIWONDE),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul", "cultura": "morado",
              "costa": "turquesa", "patrimonio unesco": "marron"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Songwe / Kasumulu (Tanzania)", "Frontera", -9.5333, 33.5500,
     "El paso natural de entrada si Malaui se inserta viniendo de Tanzania: puente sobre el río Songwe, en la M1 al norte de Karonga, enfrentado a Kasumulu (Tanzania) y a una hora larga de Mbeya. Es el único cruce carretero relevante con Tanzania y está bien rodado por el tráfico regional. Coordenada aproximada: verificar. Horario y trámite de vehículo por confirmar 72 h antes."),
    ("Frontera · Chiponde / Mandimba (Mozambique — Niassa)", "Frontera", -14.4500, 35.6333,
     "SALIDA PREFERENTE de la variante corta: desde Mangochi hacia Mandimba y de ahí a Cuamba o Lichinga, es decir, directamente al Niassa mozambiqueño. Es el paso que permite hacer Malaui SIN renunciar al norte de Mozambique (Niassa, Nampula, Ilha de Moçambique). Pista en el lado mozambiqueño; confirmar estado y horario. Coordenada aproximada."),
    ("Frontera · Mwanza / Zóbuè (Mozambique — corredor de Tete)", "Frontera", -15.6136, 34.3856,
     "Salida del bucle completo, a ~110 km de Blantyre por asfalto: es el corredor de camiones de Tete y el mismo paso que la ficha de Mozambique ya identifica como plan B de entrada al país. Tráfico pesado y colas. Lleva a Tete y al sur/centro de Mozambique, renunciando al norte."),
    ("Frontera · Muloza / Milange (Mozambique — Zambezia)", "Frontera", -16.0833, 35.7500,
     "Tercera salida posible, al pie de Mulanje, hacia Mocuba y Quelimane. Encaja muy bien si el último bloque es Mulanje y el té, pero deja fuera Majete. Menos transitada que Zóbuè. Coordenada aproximada: verificar."),
    ("Frontera · Mchinji / Mwami (Zambia)", "Frontera", -13.7667, 32.7333,
     "El paso con Zambia, a ~110 km al oeste de Lilongüe, enfrentado a Chipata (Zambia) y a la puerta de South Luangwa. Solo relevante en la variante que entra o sale por Zambia; obliga a replantear el corredor norte zambiano, que en la ruta actual termina en Nakonde. Coordenada aproximada."),
    ("Frontera · Chitipa / Kameme (Zambia, extremo norte)", "Frontera", -9.7000, 33.2700,
     "Cruce remoto del extremo noroeste, hacia Isoka (Zambia), que permitiría entrar a Malaui desde el norte de Zambia sin pasar por Tanzania. Pista, poco tráfico y muy poco documentado: POR CONFIRMAR que admite vehículos extranjeros y que emite/valida el visado. Coordenada aproximada."),
    ("Consulado Honorario de España en Lilongwe", "Consular", -13.9626, 33.7741,
     "María Ángeles Soriano, Blantyre Street 279, Area 10, Lilongüe. Tel./WhatsApp (+265) 999 846 081. Depende de la Embajada de España en Harare (Zimbabue), que también cubre Zambia."),
    ("Embajada de España en Harare (competente para Malaui)", "Consular", -17.8292, 31.0522,
     "16 Phillips Ave., Belgravia, P.O. Box 3300, Harare (Zimbabue). Tel. +263 (0)242 250740/1 · Emergencia consular: +263 (0)772 436 620. Referencia diplomática de Malaui y Zambia; para gestiones ordinarias, contactar primero con el consulado honorario de Lilongüe."),
    ("Hospital Kamuzu Central, Lilongwe", "Hospital", -13.9553, 33.7614,
     "Hospital de referencia de la capital y del centro del país; para lo serio, la práctica regional es la evacuación a Sudáfrica."),
    ("Queen Elizabeth Central Hospital, Blantyre", "Hospital", -15.7861, 35.0058,
     "Principal hospital de referencia nacional, en la capital comercial; mejor opción del sur, junto con las clínicas privadas de Blantyre y Limbe."),
    ("Hospital de Mzuzu (norte)", "Hospital", -11.4581, 34.0150,
     "Referencia sanitaria del bloque norte: Nyika, Livingstonia, Nkhata Bay y toda la costa hasta Karonga dependen de aquí."),
    ("Combustible · Karonga / Mzuzu / Rumphi (norte)", "Combustible", -11.4581, 34.0150,
     "Las tres plazas del norte. Repostar a fondo en Mzuzu o Rumphi antes de subir a Nyika y antes del escarpe de Livingstonia: arriba no hay nada."),
    ("Combustible · Lilongwe", "Combustible", -13.9833, 33.7681,
     "Mejor oferta y calidad del país junto con Blantyre (Puma, Total, Petroda). Punto de repostaje a fondo."),
    ("Combustible · Blantyre / Zomba (sur)", "Combustible", -15.7861, 35.0058,
     "Plaza principal del sur; última oferta grande antes de Mulanje, Thyolo, Majete y las fronteras mozambiqueñas."),
    ("Agua potable y de uso general · Lilongwe, Blantyre, Mzuzu", "Agua potable", -13.9833, 33.7681,
     "Agua embotellada sin problema en supermercados de las tres ciudades; lodges y campings permiten llenar el depósito de uso general con manguera."),
    ("Agua · campings del lago (Cabo Maclear, Nkhata Bay, Chintheche, Senga Bay)", "Agua potable", -14.0206, 34.8306,
     "Todos los campings de la orilla tienen agua corriente y duchas; potabilizar antes de beber. NO usar agua del lago sin filtrar y tratar (bilharzia)."),
]

DRONE_CALLOUT = ("warn", "Registro y autorización previa obligatorios ante la autoridad de aviación civil",
                  "Malaui exige registro del aparato y autorización previa del Departamento/Autoridad de Aviación Civil para volar un dron, también con fines recreativos y de fotografía, y el trámite puede llevar semanas. Es un país con experiencia real en drones —alberga desde 2017 el corredor humanitario de pruebas de drones impulsado con UNICEF y la African Drone and Data Academy— y precisamente por eso la administración está acostumbrada a exigir el papel. Norma prudente del proyecto: iniciar el trámite con semanas de antelación, llevar la autorización impresa y NO volar en ningún parque o reserva (Nyika, Liwonde, Majete, Nkhotakota, Kasungu, PN del Lago Malaui) sin permiso específico del gestor del área.")

STARLINK_CALLOUT = ("warn", "Dado por activo en revisiones anteriores del proyecto — NO se ha podido reverificar",
                     "La revisión anterior de esta ficha daba Starlink por operativo comercialmente en Malaui, apoyándose en una nota de Connecting Africa sobre el lanzamiento del servicio en el país. En esta revisión NO se ha podido reabrir esa fuente ni el mapa oficial de disponibilidad desde el entorno de trabajo, así que el dato queda marcado como pendiente de reconfirmación: comprobar el mapa oficial de Starlink 30-60 días antes de entrar y no planificar dependiendo de él. SIM local (TNM, Airtel Malawi) como base garantizada en todo el corredor.")

DOG_MATRIX = [
    ("Costa del lago: Cabo Maclear, Nkhata Bay, Chintheche, Senga Bay, Chitimba", "permitido",
     "LA MEJOR PARTE DE MALAUI CON EL PERRO, y de las mejores de todo el viaje: decenas de campings y lodges de playa con parcela, sombra y acceso directo al agua, y una cultura de alojamiento acostumbrada a overlanders con animales. Ojo con el calor de mediodía y con dejarle beber agua del lago (bilharzia también afecta a perros: consultar con el veterinario antes de entrar)."),
    ("Mesetas y montañas: Zomba, Mulanje, Dedza, Chongoni", "permitido con condiciones",
     "No son parques nacionales sino reservas forestales y monumentos, gestionadas por el Departamento de Forestal y por el Mulanje Mountain Conservation Trust: el perro no está prohibido por norma, pero HAY QUE PREGUNTAR en la oficina forestal de Likhubula (Mulanje) y en la de Zomba antes de subir. Hay leopardo en Mulanje y en Zomba, y babuinos por todas partes: correa corta obligatoria. En Mulanje, además, el esfuerzo (3.002 m, refugios sin agua fácil, varios días) desaconseja subirlo con perro."),
    ("Ciudades: Lilongüe, Blantyre, Mzuzu, Zomba, Karonga", "permitido con condiciones",
     "Sin restricción específica; hay veterinarios reales en Lilongüe y Blantyre (los únicos del país con nivel), y el Lilongwe Wildlife Centre como referencia de contacto. Es donde se tramita cualquier papel del perro."),
    ("Parques y reservas: Nyika, Liwonde, Majete, Nkhotakota, Kasungu, PN del Lago Malaui", "prohibido",
     "El DNPW malauí no admite mascotas en parques nacionales y reservas, y los tres que gestiona African Parks (Liwonde, Majete, Nkhotakota) tampoco: hay leones, leopardos, rinocerontes y elefantes, y la prohibición es de seguridad, no burocrática. PLAN B REAL Y FÁCIL EN ESTE PAÍS: los campings del lago (Cabo Maclear, Senga Bay, Chintheche) y de Zomba están a 1-3 h de todos los parques del sur y del centro, así que se puede dejar el perro con uno de los tres viajeros en la base y hacer el parque por turnos en el día, sin necesidad de guardería. Para Nyika, la base equivalente es Rumphi o Mzuzu."),
    ("Likoma (isla)", "pendiente de verificar",
     "Se llega en el MV Ilala dejando los vehículos en tierra. No hay información sobre transporte de animales en el ferry: si se hace Likoma, lo razonable es que el perro se quede en el continente con uno de los viajeros. POR CONFIRMAR con la naviera."),
]

SOURCES = [
    ("Embajada de España en Harare · Malaui (consulado honorario de Lilongüe)", "https://www.exteriores.gob.es/Embajadas/harare/es/Embajada/tambien-somos-tu-embajada-en/Paginas/Malawi.aspx"),
    ("thingstodoinmalawi.com · requisitos de entrada y visado para Malaui", "https://thingstodoinmalawi.com/entry-requirements/"),
    ("Wikipedia · Visa policy of Malawi (eVisa, exenciones y cambio de 3 de enero de 2026)", "https://en.wikipedia.org/wiki/Visa_policy_of_Malawi"),
    ("Bordercrossinghub.com · cruce de Mwanza/Zóbuè", "https://bordercrossinghub.com/mwanza-zobue-border-crossing/"),
    ("Tracks4Africa Blog · Carnet de Passage en el sur de África", "https://blog.tracks4africa.co.za/2888-2/"),
    ("PetTravel.com · requisitos de importación de mascotas a Malaui", "https://www.pettravel.com/information/pet-passports/malawi-pet-import-requirements/"),
    ("connectingafrica.com · lanzamiento de Starlink en Malaui (no reverificado en esta revisión)", "https://www.connectingafrica.com/broadband/spacex-s-starlink-launches-in-malawi"),
    ("UNESCO · Lago Malaui, Patrimonio de la Humanidad (1984)", "https://whc.unesco.org/en/list/289/"),
    ("Wikipedia · Lake Malawi National Park (UNESCO 1984, 94 km², 13 islas, ~700 cíclidos)", "https://en.wikipedia.org/wiki/Lake_Malawi_National_Park"),
    ("Wikipedia · Lake Malawi (dimensiones, más especies de peces que ningún lago del mundo, bilharzia)", "https://en.wikipedia.org/wiki/Lake_Malawi"),
    ("Wikipedia · Mount Mulanje / Mulanje Massif (Sapitwa 3.002 m, refugios, UNESCO 2025)", "https://en.wikipedia.org/wiki/Mount_Mulanje"),
    ("Wikipedia · Nyika National Park (3.200 km², acceso, Chelinda, 400 aves)", "https://en.wikipedia.org/wiki/Nyika_National_Park"),
    ("Wikipedia · Livingstonia (misión de 1894, Stone House, carretera S103/T305 de curvas)", "https://en.wikipedia.org/wiki/Livingstonia"),
    ("Wikipedia · Likoma Island (exclave malauí, catedral de San Pedro, MV Ilala)", "https://en.wikipedia.org/wiki/Likoma_Island"),
    ("Wikipedia · Liwonde National Park (African Parks 2015, rinocerontes, guepardos, leones)", "https://en.wikipedia.org/wiki/Liwonde_National_Park"),
    ("Wikipedia · Majete Wildlife Reserve (African Parks 2003, primer big five del país)", "https://en.wikipedia.org/wiki/Majete_Wildlife_Reserve"),
    ("Wikipedia · Nkhotakota Wildlife Reserve (traslocación de ~500 elefantes 2016-2017)", "https://en.wikipedia.org/wiki/Nkhotakota_Wildlife_Reserve"),
    ("Wikipedia · Kasungu National Park (2.316 km², 263 elefantes del IFAW en 2022)", "https://en.wikipedia.org/wiki/Kasungu_National_Park"),
    ("Wikipedia · Chongoni Rock Art Area (UNESCO 2006, 127 yacimientos, nyau)", "https://en.wikipedia.org/wiki/Chongoni_Rock_Art_Area"),
    ("Wikipedia · Zomba Plateau (2.087 m, 130 km², embalse de Mulunguzi)", "https://en.wikipedia.org/wiki/Zomba_Plateau"),
    ("Wikipedia · Blantyre (St Michael and All Angels, Mandala House, QECH)", "https://en.wikipedia.org/wiki/Blantyre"),
    ("Wikipedia · Lilongwe (capital, Old Town y City Centre, Kamuzu Central Hospital)", "https://en.wikipedia.org/wiki/Lilongwe"),
    ("Wikipedia · Mzuzu (capital del norte, M1 y M5, Viphya)", "https://en.wikipedia.org/wiki/Mzuzu"),
    ("Wikipedia · Nkhata Bay (puerto, buceo, MV Ilala)", "https://en.wikipedia.org/wiki/Nkhata_Bay"),
    ("Wikipedia · Karonga (Cultural & Museum Centre, Malawisaurus, homínidos de Malema)", "https://en.wikipedia.org/wiki/Karonga"),
    ("Wikipedia · Dedza (1.590 m, alfarería, monte de 2.198 m, 85 km de Lilongüe)", "https://en.wikipedia.org/wiki/Dedza"),
    ("Wikipedia · Mangochi (Fort Johnston, torre del reloj, carretera a Chiponde)", "https://en.wikipedia.org/wiki/Mangochi"),
    ("Wikipedia · MV Ilala (ruta semanal Monkey Bay-Chilumba, 12 escalas, Likoma)", "https://en.wikipedia.org/wiki/MV_Ilala"),
    ("Wikipedia · Transport in Malawi (red viaria, 45% asfaltada, ferrocarril de Mchinji)", "https://en.wikipedia.org/wiki/Transport_in_Malawi"),
    ("iOverlander · puntos de combustible, agua y campings verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Bucle completo: Songwe (Tanzania) -> norte -> lago -> Lilongüe -> lago sur -> Blantyre/Mulanje -> Mwanza (Mozambique)
CORRIDOR = [(-9.5333, 33.5500), (-9.9333, 33.9333), (-10.5833, 34.1833), (-10.6083, 34.1167),
            (-11.0167, 33.8583), (-10.5667, 33.8000), (-11.0167, 33.8583), (-11.4581, 34.0150),
            (-11.6000, 34.3000), (-11.8500, 34.1667), (-12.9167, 34.3000), (-13.7667, 34.6167),
            (-13.9833, 33.7681), (-14.3333, 34.3333), (-14.2167, 34.5333), (-14.0206, 34.8306),
            (-14.8333, 35.3167), (-15.3833, 35.3167), (-15.7861, 35.0058), (-15.9667, 35.6333),
            (-16.0667, 35.1333), (-15.9700, 34.7597), (-15.6136, 34.3856)]

# Variante corta: entra por Songwe y sale a Niassa por Chiponde, sin el bloque sur ni Nyika
CORRIDOR_ALT = [(-9.5333, 33.5500), (-9.9333, 33.9333), (-10.5833, 34.1833), (-11.4581, 34.0150),
                (-11.6000, 34.3000), (-11.8500, 34.1667), (-12.9167, 34.3000), (-13.7667, 34.6167),
                (-14.0206, 34.8306), (-14.4600, 35.2700), (-14.4500, 35.6333)]

EXPERIENCIAS = [
    "Aviso previo de método: en esta revisión NO se pudo abrir iOverlander ni Tracks4Africa desde el entorno de trabajo (dominios bloqueados por el proxy). Lo que sigue es lo que repiten de forma coincidente los relatos publicados del circuito overland de África oriental, y debe reverificarse punto por punto en iOverlander y Tracks4Africa antes de depender de ello.",
    "Malaui es «el país fácil» del circuito: los relatos coinciden en que es el tramo donde todo el mundo se relaja — distancias cortas, gente extraordinariamente amable (de ahí «the warm heart of Africa»), campings baratos junto al agua y ninguna zona que haya que evitar. Es exactamente lo contrario del esfuerzo de Angola o del papeleo de los dos Congos.",
    "La carretera de Livingstonia es EL tema recurrente del norte: quienes la han subido la describen como quince kilómetros de pista estrecha con unas veinte curvas de herradura cerradísimas, sin quitamiedos y con caídas largas, que en seco es divertida con 4x4 y en mojado es seria. Los relatos recomiendan subir por la mañana (menos tráfico de bajada), no cruzarse en las curvas y contar hora y media. Varios cuentan que los coches de alquiler 2x4 se quedan a mitad.",
    "Chitimba y el escarpe: los dos alojamientos que aparecen una y otra vez son el camping de la playa de Chitimba, al pie de la subida, y un eco-lodge en mitad del escarpe con vistas verticales sobre el lago, muy citado por su terraza. Mucha gente deja el vehículo abajo y sube en transporte local o a pie, precisamente por la carretera.",
    "Costa norte (Nkhata Bay y Chintheche): el clásico absoluto del circuito. Los campings de playa con parcela para vehículo y el buceo barato en agua dulce salen en casi todos los diarios de viaje; Chintheche es donde paran los camiones de expedición y por eso tiene la infraestructura más rodada. Es también donde más gente reporta quedarse más días de los previstos.",
    "Nyika: coincidencia general en que es el sitio más sorprendente del país y el que más gente se salta por el desvío. Advierten de que hace FRÍO de verdad de noche (por encima de 2.000 m), de que hay que entrar con depósito lleno y provisiones porque en Chelinda no hay repostaje, y de que la pista de subida es larga y lenta aunque no técnica.",
    "Combustible: el aviso más repetido de los últimos años sobre Malaui son las COLAS Y DESABASTECIMIENTOS PUNTUALES de gasóleo, ligados a la falta de divisas del país. Los viajeros recomiendan repostar siempre que se pueda sin esperar a la reserva y llevar garrafas llenas. Es un riesgo operativo real en un país por lo demás fácil: confirmar la situación antes de entrar.",
    "Bilharzia: es el otro tema que sale en todos los relatos, porque todo el mundo se baña en el lago. La actitud mayoritaria de los viajeros de larga duración es «báñate, disfruta y trátate después»: asumir la exposición y tomar praziquantel pasadas unas semanas, en lugar de renunciar al lago. No es consejo médico, pero explica por qué casi nadie se abstiene.",
    "Fronteras: Songwe con Tanzania y Mwanza con Mozambique aparecen descritas como trámites largos pero ordenados, con las tasas de vehículo (seguro de terceros, tasa de carreteras) pagándose en ventanillas separadas. Recomiendan llevar dólares en efectivo y billetes pequeños, y no aceptar cambio de moneda de los gestores informales que abordan en el aparcamiento.",
    "Perro: los relatos de viajeros con animales por África oriental señalan sistemáticamente la costa de Malaui como una de las zonas más cómodas de todo el continente, por la cantidad de alojamientos de playa con parcela y por lo tolerante del trato. Lo contrario ocurre con los parques, cerrados a cal y canto.",
]

HISTORIA_RESUMEN = ("Malaui creció alrededor del gran lago que le da nombre, cruce de rutas de comercio y de la trata de esclavos árabe-swahili hasta que el misionero David Livingstone impulsó su freno; "
                     "convertido en el protectorado británico de Niasalandia, alcanzó la independencia en 1964 bajo Hastings Banda, cuyo régimen autoritario de partido único duró tres décadas, y hoy es uno de los países más estables y tranquilos del corredor de regreso.")

HISTORIA_SECCIONES = [
    ("El lago y las rutas de comercio",
     "El lago Malaui, tercero más grande de África, ha sido durante siglos el eje de la vida de los pueblos chewa, yao y ngoni que se asentaron en sus orillas. "
     "En el siglo XIX, mercaderes árabe-swahilis remontaron el lago desde la costa mozambiqueña y tanzana para comerciar con marfil y personas esclavizadas, convirtiendo la región en uno de los últimos grandes escenarios de la trata de esclavos en el interior de África oriental. "
     "Nkhotakota, en la orilla occidental, fue el cuartel general del jefe suajili Jumbe y el gran punto de embarque hacia Kilwa."),
    ("Livingstone y el protectorado británico",
     "El misionero y explorador escocés David Livingstone llegó al lago en 1859 y dedicó buena parte de su carrera a denunciar la trata de esclavos en la región, lo que impulsó la presencia misionera y comercial británica posterior. "
     "Las misiones escocesas intentaron asentarse primero en Cabo Maclear (1875) y luego en Bandawe, y solo prosperaron al trasladarse en 1894 a la meseta de Livingstonia, por encima de la malaria. "
     "En 1891 el territorio se convirtió en el protectorado británico de Niasalandia, integrado entre 1953 y 1963 en la Federación de Rodesia y Niasalandia junto a las actuales Zimbabue y Zambia, una unión impuesta y resistida por la población africana."),
    ("Independencia y la era de Hastings Banda",
     "Malaui alcanzó la independencia en 1964 bajo el liderazgo de Hastings Kamuzu Banda, quien gobernó como presidente vitalicio de partido único hasta 1994, con un régimen autoritario de censura estricta y culto a la personalidad, "
     "pero también de relativa estabilidad y ausencia de los conflictos armados que sacudieron a varios de sus vecinos en esas décadas. La transición a un sistema multipartidista llegó en 1994 tras un referéndum."),
    ("Situación actual: uno de los tramos más tranquilos de la región",
     "Desde los años 90, Malaui ha mantenido un sistema democrático con alternancia de poder, sin conflictos armados ni insurgencias activas en su territorio, aunque continúa siendo uno de los países más pobres del mundo y arrastra una crisis crónica de divisas que se traduce, para un viajero, en episodios de escasez de combustible y en un kwacha muy devaluado. "
     "Para este viaje, ese contexto significa un tramo sin zonas excluidas: todo el itinerario, de Songwe a Mulanje, se recorre con precaución normal de viaje."),
]

HISTORIA_FUENTES = [
    ("BBC News · Malawi country profile", "https://www.bbc.com/news/world-africa-13864367"),
    ("Encyclopaedia Britannica · Malawi, History", "https://www.britannica.com/place/Malawi/History"),
    ("UNESCO · Lago Malaui, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/289/"),
]

SPEC = dict(
    slug="malaui", name="Malaui", revision="12 sep 2026",
    sub="ALTERNATIVA — no está en la ruta fija · bucle opcional entre Tanzania y Mozambique",
    chips=[
        ("ESTATUS", "ALTERNATIVA · NO está en la ruta fija — solo si sobra tiempo en el bucle sur/este"),
        ("DÓNDE ENCAJA", "Insertado en el bucle: Tanzania (Songwe) → Malaui → Mozambique (Chiponde o Zóbuè)"),
        ("COSTE · BUCLE COMPLETO", "~1.900 km y 16–21 días añadidos al viaje"),
        ("COSTE · VARIANTE CORTA", "~1.100 km y 9–12 días, saliendo a Niassa por Chiponde"),
        ("PDIs", "22 puntos, del museo de Karonga a Majete"),
        ("LO ÚNICO", "El lago con MÁS ESPECIES DE PECES DEL MUNDO (UNESCO) y Mulanje, 3.002 m (UNESCO 2025)"),
        ("A PIE", "Mulanje y Nyika: dos de los mejores trekkings de África austral"),
        ("4x4", "Las ~20 curvas de herradura del escarpe de Livingstonia · pistas de Nyika"),
        ("PERRO", "De lo más fácil del viaje en la costa del lago · parques cerrados, pero con base a 1–3 h"),
        ("SALUD", "BILHARZIA en todo el lago — dato crítico, todo el mundo se baña"),
        ("VISADO", "eVisa obligatoria… salvo que se confirme la exención para España de enero de 2026"),
    ],
    center=[-13.2, 34.3], zoom=6,
    hero_img=W + "Otter%20Point%2C%20Cape%20Maclear%20(Malawi).jpg?width=900",
    hero_credit="Otter Point, Cabo Maclear, Parque Nacional del Lago Malaui · Hans Hillewaert · CC BY-SA 4.0",
    notice="Documento de planificación de una ALTERNATIVA que hoy NO forma parte de la ruta fija. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada si finalmente se decide hacerlo.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle completo (Songwe → sur → Mwanza/Zóbuè)",
    corridor_alt_label="Variante corta (Songwe → Chiponde, hacia Niassa)",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("<strong>Malaui no está en la ruta fija.</strong> Es una alternativa que solo se hace si el calendario del bucle sur/este da de sí. "
                   "Ahora bien, si entra, entra bien: es un país pequeño (de punta a punta cabe en un tercio de Angola) y densísimo, y se inserta de forma "
                   "casi natural entre <strong>Tanzania</strong> y <strong>Mozambique</strong>, que son dos países que ya están en la ruta y que hacen frontera con él. "
                   "Dentro hay un lago que es Patrimonio Mundial y que tiene <strong>más especies de peces que ningún otro lago del planeta</strong> (unos 700 cíclidos, "
                   "casi todos endémicos), la montaña de senderismo más importante de África central-meridional (<strong>Mulanje, 3.002 m</strong>, Patrimonio Mundial desde 2025), "
                   "una meseta de praderas de altura del tamaño de una provincia (<strong>Nyika</strong>), el conjunto de arte rupestre más denso de África central "
                   "(<strong>Chongoni</strong>, UNESCO), tres parques de African Parks con big five y rinoceronte, y <strong>la carretera de las veinte curvas de herradura "
                   "de Livingstonia</strong>, que es exactamente la clase de tramo por la que se llevan dos 4x4."),
    decision=("<strong>ESTATUS: ALTERNATIVA. Malaui NO está en la ruta fija del proyecto.</strong> Se documenta entero para poder decidir con datos, no para darlo por hecho. "
              "La pregunta no es si merece la pena —lo merece— sino <em>cuánto cuesta en días</em>, y ese es el número que esta ficha existe para dar.<br><br>"
              "<strong>Dónde encaja exactamente.</strong> Malaui hace frontera con tres países que ya están en la ruta: Tanzania, Mozambique y Zambia. "
              "La inserción limpia es <strong>entre Tanzania y Mozambique</strong>, en la bajada del bucle: cuando la ruta baja de Kenia por Tanzania camino de Mozambique, "
              "en vez de seguir de Mbeya hacia el sureste, se entra a Malaui por <strong>Songwe/Kasumulu</strong> (a una hora de Mbeya), se recorre el país de norte a sur y se sale a Mozambique. "
              "La entrada por Zambia (Mchinji, desde Chipata) es posible pero obliga a romper el corredor norte zambiano, que hoy termina en Nakonde: no compensa.<br><br>"
              "<strong>Las dos opciones de salida, y por qué importa cuál.</strong> "
              "<em>(A) Bucle completo</em>: norte → lago → Lilongüe → Cabo Maclear → Liwonde → Zomba → Blantyre → Mulanje → Majete → salida por <strong>Mwanza/Zóbuè</strong> al corredor de Tete. "
              "Son unos <strong>1.900 km y 16-21 días</strong>, lo ve todo… pero deja a Mozambique entrando por Tete, es decir, <strong>renunciando a todo el norte mozambiqueño</strong> "
              "(Niassa, Nampula, Ilha de Moçambique). Ojo: Zóbuè es precisamente el paso que la ficha de Mozambique ya tiene identificado como plan B de entrada, así que la coherencia está. "
              "<em>(B) Variante corta</em>: norte → lago → Cabo Maclear → Mangochi → salida por <strong>Chiponde/Mandimba</strong> directamente al Niassa mozambiqueño. "
              "Son unos <strong>1.100 km y 9-12 días</strong>, se queda sin Nyika, sin Mulanje y sin el bloque de Blantyre… pero <strong>no cuesta nada del itinerario mozambiqueño</strong>, "
              "porque aterriza justo donde habría aterrizado el paso de Matchedje.<br><br>"
              "<strong>La recomendación honesta de esta ficha:</strong> si hay dos semanas, la variante corta (B) es casi gratis en términos de ruta y se lleva el lago, que es el motivo por el que se viene. "
              "Si hay tres semanas largas y se acepta renunciar al norte de Mozambique, el bucle completo (A) añade Nyika, Mulanje y Majete, que son de primer nivel mundial. "
              "Lo que no tiene sentido es entrar a Malaui y hacerlo con prisa: es un país de parar."),
    facts=[
        ("Estatus en el proyecto", "ALTERNATIVA. No está en la ruta fija. Se hace solo si el calendario del bucle sur/este lo permite."),
        ("Dónde encaja", "En el bucle, entre Tanzania (bajando de Kenia) y Mozambique. Entrada por Songwe, salida por Chiponde (Niassa) o por Mwanza/Zóbuè (Tete)."),
        ("Coste en ruta · opción A", "Bucle completo Songwe → Mulanje/Majete → Mwanza: ~1.900 km, 16-21 días. Renuncia al norte de Mozambique."),
        ("Coste en ruta · opción B", "Variante corta Songwe → Cabo Maclear → Chiponde: ~1.100 km, 9-12 días. NO cuesta itinerario mozambiqueño."),
        ("Entrada", "Songwe/Kasumulu desde Tanzania, en la M1 al norte de Karonga, a ~1 h de Mbeya. Único cruce carretero relevante con Tanzania."),
        ("Salidas posibles", "Chiponde/Mandimba (a Niassa), Mwanza/Zóbuè (a Tete), Muloza/Milange (a Zambezia), Mchinji (a Zambia, Chipata)."),
        ("Visado", "PENDIENTE DE CONFIRMAR. España no era país exento en el régimen vigente desde febrero de 2024 (eVisa obligatoria en evisa.gov.mw); una revisión del régimen con efecto 3 de enero de 2026 habría restablecido la exención para España. Verificar en la autoridad de inmigración antes de contar con ello."),
        ("Carreteras", "~15.450 km de red, de los que un 45% asfaltado. El eje M1 (Songwe-Karonga-Mzuzu-Lilongüe-Blantyre) y la M5 lacustre son asfalto con baches; lo interesante está en las pistas."),
        ("Combustible", "Estaciones formales en todas las ciudades, PERO con episodios recurrentes de escasez por falta de divisas: no esperar a la reserva y llevar garrafas."),
        ("Perro", "Uno de los mejores países del viaje para el perro en la costa del lago; prohibido en los seis parques y reservas. Base a 1-3 h de cada parque: se resuelve por turnos."),
        ("Salud", "Malaria intensa en todo el país y BILHARZIA en todo el lago Malaui: es el dato sanitario que define el tramo."),
        ("Comunicaciones", "Starlink dado por activo en revisiones anteriores del proyecto pero NO reverificado aquí; SIM local (TNM, Airtel) como base segura."),
    ],
    alerts=[
        "ESTATUS: esta ficha documenta una ALTERNATIVA. Malaui no está en la ruta fija y no hay que tramitar nada hasta que se decida incluirlo.",
        "BILHARZIA (esquistosomiasis) EN TODO EL LAGO MALAUI, y este es el dato importante porque el lago es el motivo del viaje y todo el mundo se baña en él. El caracol endémico Bulinus nyassanus actúa como hospedador intermedio en aguas abiertas del propio lago desde mediados de los años ochenta: no es solo un problema de orillas con juncos junto a los pueblos. Ningún tramo del lago puede considerarse garantizadamente seguro. Ver la sección de salud para el protocolo que sigue de hecho casi todo el mundo (bañarse y tratarse después con praziquantel) y decidirlo con Sanidad Exterior ANTES de salir.",
        "VISADO SIN CERRAR: hasta febrero de 2024 España quedó fuera de la lista de países exentos y la eVisa (evisa.gov.mw) era obligatoria; el visado a la llegada dejó de emitirse en marzo de 2020. Consta un cambio de régimen con efecto 3 de enero de 2026 que restablecería la exención para España, pero NO se ha podido confirmar en fuente oficial malauí en esta revisión. Planificar asumiendo eVisa y verificar antes de viajar: llegar a Songwe con el supuesto equivocado es quedarse en la frontera.",
        "Escasez de combustible: Malaui arrastra una crisis crónica de divisas y ha tenido episodios repetidos de desabastecimiento de gasóleo y colas largas. Es el principal riesgo operativo de un país por lo demás fácil. Repostar siempre que se pueda, llevar garrafas llenas y comprobar la situación 30 días antes de entrar.",
        "Perro prohibido en los seis parques y reservas (Nyika, Liwonde, Majete, Nkhotakota, Kasungu y el PN del Lago Malaui). La buena noticia es que el país es pequeño: en todos los casos hay una base con camping a 1-3 h, así que se resuelve por turnos entre los tres viajeros sin necesidad de guardería.",
        "Mulanje mata gente. Es una montaña seria de 3.002 m con niebla repentina (el «chiperoni»), sin cobertura y con rutas de cumbre a Sapitwa que exigen manos. Subir con guía contratado en la oficina forestal de Likhubula, informar del itinerario y no subir en temporada de lluvias (noviembre-abril).",
        "Nyika: por encima de 2.000 m hace frío de verdad de noche, no hay combustible en Chelinda y la pista de subida es larga. Entrar con depósito lleno, provisiones y ropa de abrigo — es la última cosa que uno espera de África oriental y la que más pilla desprevenido.",
        "Bordes sin protección en Manchewe, en Chingwe's Hole (Zomba) y en toda la meseta de Mulanje; y cocodrilos e hipopótamos en el Shire (Liwonde, Majete, Mangochi) y en las desembocaduras de los ríos del lago. Preguntar SIEMPRE en el alojamiento antes de dejar que el perro se acerque al agua.",
        "Dron: registro y autorización previa obligatorios, con semanas de trámite, y prohibición de facto dentro de parques y reservas sin permiso específico del gestor.",
    ],
    ruta_intro=("Dos formas de hacer Malaui, y la diferencia entre ellas no son kilómetros sino <strong>lo que le cuestan a Mozambique</strong>. "
                "El <strong>bucle completo</strong> (~1.900 km) recorre el país entero de Songwe a Mulanje y sale por Tete, renunciando al norte mozambiqueño. "
                "La <strong>variante corta</strong> (~1.100 km) se queda con el lago y sale a Niassa por Chiponde, sin coste para el itinerario de Mozambique. "
                "Etapas calculadas sobre una media de <strong>250 km/día</strong>; en Malaui las distancias son cortas y el ritmo real lo marcan las paradas, no la conducción."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada y primer museo", "Songwe (frontera) → Karonga", "~45 km · 1 día (el cruce se lleva media jornada)"),
        ("2 · La costa del escarpe", "Karonga → Chilumba → Chitimba", "~105 km · 1 día"),
        ("3 · LAS VEINTE CURVAS", "Chitimba → Livingstonia (S103/T305) → Manchewe → Chitimba", "~30 km ida y vuelta · 2 días (1-1,5 h solo la subida)"),
        ("4 · A la meseta de altura", "Chitimba → Rumphi → Thazima → Chelinda (Nyika)", "~200 km · 1-2 días de pista"),
        ("5 · Nyika", "Chelinda: praderas, Jalawe, cataratas de Chisanga, bici y caminatas", "en el parque · 3-4 días"),
        ("6 · Bajada al norte urbano", "Chelinda → Rumphi → Mzuzu", "~170 km · 1 día · taller, banco, repostaje"),
        ("7 · El lago por el norte", "Mzuzu → Nkhata Bay → Chintheche", "~85 km · 3-4 días de parada"),
        ("Opcional · Likoma", "Nkhata Bay → MV Ilala → Likoma (catedral) → vuelta", "sin vehículo · 2-3 días, sujeto al horario semanal del Ilala"),
        ("8 · Costa central y trata", "Chintheche → Dwangwa → Nkhotakota (reserva y ciudad)", "~210 km · 2-3 días"),
        ("9 · Playa de la capital", "Nkhotakota → Salima → Senga Bay", "~145 km · 1-2 días"),
        ("10 · Capital y logística", "Senga Bay → Lilongüe", "~105 km · 1-2 días de taller, permisos y compras"),
        ("Opcional · Kasungu", "Lilongüe → Kasungu NP → Lilongüe", "~350 km ida y vuelta · 2 días"),
        ("11 · Arte rupestre", "Lilongüe → Dedza → Chongoni (Chentcherere, Mphunzi, Namzeze) → Mua", "~150 km · 2 días"),
        ("12 · EL LAGO, el bueno", "Mua → Monkey Bay → Cabo Maclear (PN del Lago Malaui)", "~200 km · 3-4 días de parada"),
        ("Variante corta · SALIDA", "Cabo Maclear → Mangochi → Chiponde/Mandimba (Mozambique, Niassa)", "~165 km · 1 día + el cruce"),
        ("13 · Rinocerontes y guepardos", "Cabo Maclear → Liwonde NP", "~130 km · 2-3 días"),
        ("14 · La meseta fresca", "Liwonde → Zomba y la carretera panorámica de la meseta", "~60 km · 2 días"),
        ("15 · Capital comercial", "Zomba → Blantyre", "~65 km · 1-2 días"),
        ("16 · LA MONTAÑA", "Blantyre → Mulanje (Likhubula) → travesía a Sapitwa y vuelta", "~65 km + 3-5 días a pie en la montaña"),
        ("17 · El té", "Mulanje → Thyolo (Satemwa) → Blantyre", "~120 km · 1 día"),
        ("18 · Big five y salida", "Blantyre → Majete → Mwanza/Zóbuè (Mozambique)", "~200 km · 2-3 días"),
    ],
    offroad=[
        "LA CARRETERA DE LIVINGSTONIA (S103/T305, Chitimba → Livingstonia): el tramo 4x4 mítico del país y la razón por la que Malaui merece un 4x4 y no un turismo. Unos 15 km para subir el escarpe desde la orilla del lago (~500 m) hasta la meseta de la misión (~1.000 m), en una sucesión de aproximadamente veinte curvas de herradura cerradísimas, sin quitamiedos, de firme de tierra y roca suelta y con un carril justo para un vehículo. En seco es exigente pero disfrutable; con barro es seria de verdad. Subir por la mañana, bajar con luz, y contar hora y media por sentido.",
        "Acceso a Nyika por Thazima (desde Rumphi): la vía principal, una única pista de tierra que se desgaja del eje Rumphi-Katumbi y sube el escarpe suroeste hasta la meseta y, ya arriba, otro largo tramo hasta Chelinda. No es técnica pero sí larga, lenta y sin servicios: 4x4 con altura, depósito lleno y provisiones. Con lluvias (enero-abril) el barro de la subida es el problema.",
        "Travesías de la propia meseta de Nyika: decenas de kilómetros de pistas de pradera entre 2.000 y 2.600 m, sin árboles, con vistas de horizonte y fauna a los lados. Es de las conducciones más bonitas y menos conocidas de África austral, y el parque es además uno de los poquísimos donde también se permite recorrerla en bicicleta de montaña.",
        "Pistas de Chongoni (Dedza): accesos cortos de tierra desde la M1 hasta los abrigos de Chentcherere, Mphunzi y Namzeze, entre bolos de granito y bosque. Fáciles en seco, resbaladizas en lluvias; el interés es que llevan a arte rupestre al que casi nadie va.",
        "Red interior de Majete: la reserva admite AUTOCONDUCCIÓN por su malla de pistas de tierra hacia los hides y el río Shire. Es la única de las tres de African Parks en Malaui donde se puede recorrer con vehículo propio sin guía obligatorio — confirmar la norma vigente al reservar.",
        "Bajada al bajo Shire (Blantyre → Chikwawa → Majete): el descenso del escarpe desde los 1.000 m de Blantyre hasta los ~100 m del valle, con cambio brutal de clima y vegetación en 60 km. Asfalto con tramos rotos y mucho tráfico lento.",
        "Costa norte de Nkhata Bay hacia Usisya y Ruarwe: pistas costeras muy duras, prácticamente sin salida, que llegan a pueblos a los que normalmente se accede solo en barco. Solo para quien quiera meterse expresamente; preguntar sobre el terreno antes, y no ir solo con un vehículo.",
        "Interior de Kasungu y de Vwaza Marsh: pistas de miombo y dambo, fáciles en seco y complicadas con lluvia; Kasungu cierra habitualmente en marzo.",
    ],
    senderismo=[
        "MONTE MULANJE — LA GRAN CAMINATA DEL PAÍS. Se sube desde Likhubula (oficina forestal, donde se paga, se contrata guía y porteadores y se registra el itinerario): entre 3 y 6 horas por alguno de los varios senderos hasta plantarse en la meseta, y a partir de ahí una red de refugios de montaña (Chambe, Lichenya, Thuchila, Chinzama, Sombani, Minunu, Chisepo) que permite encadenar travesías. La ruta clásica de 3-5 días es Likhubula → Chambe → Chisepo → SAPITWA (3.002 m, la cumbre se ataca mejor desde Chisepo, y el último tramo exige trepar entre bloques) → Thuchila → Lichenya → bajada. Los refugios son básicos: catre o suelo, chimenea, guardés; hay que llevar saco, comida y hornillo. Temporada de mayo a agosto (seco y fresco); evitar de noviembre a abril. La niebla «chiperoni» puede cerrar la meseta en minutos: sin guía, no.",
        "Chambe West Face (Mulanje): la escalada en roca más larga de África, de varios días, para escaladores de verdad. No es nuestro plan, pero conviene saber que la pared está ahí y que la vista de Chambe desde la meseta es media razón para subir.",
        "NYIKA — caminar sin senderos. La meseta se recorre a pie casi en cualquier dirección: pradera abierta, sin vegetación densa y sin grandes depredadores peligrosos a la vista, algo excepcional en un parque africano. Rutas de referencia desde Chelinda: el circuito del embalse y los pinares, la roca de Jalawe (mirador sobre el escarpe con el lago Malaui al fondo), las cataratas de Chisanga en el borde occidental y las cumbres redondeadas del entorno de Domwe. Hay además travesías guiadas de varios días por la meseta que el parque organiza con porteadores: PENDIENTE confirmar con el DNPW cuáles se ofrecen actualmente, incluida la bajada del escarpe hacia Livingstonia que citan las guías.",
        "MESETA DE ZOMBA: el «Potato Path», el sendero histórico por el que suben los porteadores desde la ciudad hasta la meseta, es la caminata clásica del sur (2-3 h de subida fuerte). Arriba, red de pistas y senderos entre pinares hacia el mirador del Emperador, la vista de la Reina, el embalse de Mulunguzi, las cascadas de Williams y el Chingwe's Hole, una sima de profundidad desconocida rodeada de leyendas. Todo se puede hacer por tramos desde el vehículo.",
        "Cataratas de Manchewe (Livingstonia): sendero corto al mirador y bajada empinada y resbaladiza hasta la cueva situada tras la cortina de agua. Media mañana, con vistas al lago desde 900 m por encima.",
        "Chongoni (Dedza): caminatas cortas entre bolos de granito y bosque de miombo hasta los abrigos con pinturas rojas de los BaTwa y blancas de los chewa. Los tres conjuntos abiertos —Chentcherere, Mphunzi y Namzeze— se hacen en un día con guía local del comité del sitio.",
        "Monte Dedza (2.198 m): se sube por la pista de mantenimiento de las antenas de la cumbre, caminata fácil y sin pérdida con vistas a la frontera mozambiqueña; buena opción de medio día con el perro.",
        "Montes de Blantyre: Michiru, Ndirande, Soche y Chiradzulu rodean la ciudad y todos tienen senderos; el área de conservación de Michiru es la más organizada y la más cómoda para una caminata de mañana antes de seguir viaje.",
        "Cabo Maclear: la subida al cerro sobre el pueblo de Chembe para ver la puesta de sol sobre las islas (1 h), el sendero de Otter Point y las caminatas por las islas de Domwe y Mumbo, a las que se va en kayak desde la playa. Combinación de andar y agua que es lo mejor del lago.",
        "Kapachira Falls (junto a Majete): los rápidos del bajo Shire donde Livingstone tuvo que abandonar su barco de vapor; paseo corto y con carga histórica, fuera del recinto de fauna de la reserva.",
    ],
    acampada=[
        "La costa del lago es, sin discusión, el mejor sitio del viaje para acampar con vehículo y perro: decenas de campings y lodges de playa con parcela, sombra, duchas y acceso directo al agua, en Cabo Maclear (Chembe), Nkhata Bay, Chintheche, Senga Bay y Chitimba. Son baratos y están acostumbrados a overlanders.",
        "Chitimba, al pie del escarpe de Livingstonia, y los alojamientos colgados a mitad de la subida son las bases naturales para hacer la carretera de las curvas sin prisa; varios viajeros dejan el vehículo abajo y suben ligeros.",
        "Nyika: camping y cabañas en Chelinda, dentro del parque, a más de 2.000 m — abrigo de verdad, y sin repostaje ni tienda: subir autosuficiente. Perro no.",
        "Zomba: camping y alojamiento en la meseta (entorno del Ku Chawe y de la piscifactoría de truchas), la mejor pernocta fresca del sur.",
        "Liwonde, Majete y Nkhotakota tienen campamentos propios gestionados por African Parks o por los lodges concesionarios, con parcelas para vehículo; hay que reservar y el perro no entra.",
        "Lilongüe y Blantyre tienen campings urbanos clásicos del circuito, con recinto cerrado, bar y aparcamiento vigilado: es donde se hacen los papeleos y las reparaciones.",
        "Mulanje: se duerme en los refugios de montaña de la meseta (llevar saco y comida) y en alojamientos con camping en Likhubula, al pie de la subida, que además guardan el vehículo mientras se está arriba.",
        "Regla general: acampada libre poco habitual y poco necesaria, porque la oferta formal es barata y está bien repartida. Si se vivaquea en zona rural, avisar siempre al jefe del pueblo.",
    ],
    visado=[
        "SITUACIÓN SIN CERRAR — es la primera cosa que hay que verificar si Malaui entra en la ruta. El visado a la llegada dejó de emitirse el 25 de marzo de 2020: desde entonces el sistema es la eVisa (plataforma evisa.gov.mw, en funcionamiento desde el 1 de noviembre de 2019) o la exención.",
        "En el régimen de exenciones vigente desde el 7 de febrero de 2024, España NO figuraba entre los países exentos, de modo que la eVisa era obligatoria para pasaportes españoles (referencia de coste manejada en la revisión anterior de esta ficha: ~75 USD, entrada única, 30 días, 5-10 días laborables de tramitación).",
        "Consta una revisión del régimen de visados con efecto 3 de enero de 2026 que habría RESTABLECIDO la exención para varios países, entre ellos España. No se ha podido confirmar en fuente oficial malauí desde el entorno de trabajo de esta revisión, así que el dato queda marcado como POR CONFIRMAR.",
        "Criterio operativo: planificar como si la eVisa fuera obligatoria (es el supuesto que no rompe nada si nos equivocamos) y confirmar el régimen real con el Departamento de Inmigración de Malaui o con el consulado honorario de Lilongüe antes de acercarse a Songwe. Llegar a la frontera confiando en una exención no confirmada es el único modo de quedarse fuera.",
        "Los exentos entran 30 días, prorrogables hasta un máximo de 90. Ciudadanos de la SADC y la COMESA entran sin visado 30 días — no nos aplica, pero explica el tráfico regional del paso de Songwe.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica (Tanzania y Zambia lo son en parte): llevarlo siempre.",
    ],
    fronteras_rows=[
        ("Entrada (única razonable)", "Songwe / Kasumulu (desde Tanzania)",
         "En la M1 al norte de Karonga, sobre el río Songwe, a una hora larga de Mbeya. Es el cruce carretero relevante con Tanzania y está muy rodado por el tráfico regional. Confirmar horario, tasas de vehículo y trámite del CPD 72 h antes."),
        ("Salida A (variante corta) · RECOMENDADA", "Chiponde / Mandimba (hacia Mozambique, Niassa)",
         "Desde Mangochi hacia Mandimba y de ahí a Cuamba/Lichinga. Es el paso que permite hacer Malaui SIN renunciar al norte de Mozambique, porque aterriza en el mismo Niassa al que llevaría el paso de Matchedje. Confirmar estado de la pista mozambiqueña y horario."),
        ("Salida B (bucle completo)", "Mwanza / Zóbuè (hacia Mozambique, corredor de Tete)",
         "A ~110 km de Blantyre por asfalto, corredor de camiones. Coherente con la ficha de Mozambique, que ya lo tiene identificado como plan B de entrada al país. Coste: se entra a Mozambique por Tete y se pierde todo el norte mozambiqueño."),
        ("Salida C (alternativa sur)", "Muloza / Milange (hacia Mozambique, Zambezia)",
         "Al pie de Mulanje, hacia Mocuba y Quelimane. Encaja perfecto si el último bloque es Mulanje y el té, pero deja fuera Majete. Menos transitada. Por confirmar horario y trámite de vehículo."),
        ("Alternativa de entrada/salida", "Mchinji / Mwami (Zambia, frente a Chipata)",
         "A ~110 km de Lilongüe. Solo tiene sentido si se replantea el corredor zambiano, que hoy termina en Nakonde; obligaría a renunciar al norte de Zambia (cascadas, Bangweulu, Tanganyika). No recomendado."),
        ("Alternativa remota", "Chitipa / Kameme (Zambia, extremo norte, hacia Isoka)",
         "Permitiría entrar desde el norte de Zambia sin pasar por Tanzania. Pista, muy poco tráfico y muy poco documentado: POR CONFIRMAR que admite vehículos extranjeros y que resuelve visado y aduana."),
    ],
    vehiculos=[
        "CPD aceptado; si no, permiso temporal de importación (TIP) emitido en la frontera. Confirmar cuál se aplica en Songwe antes de llegar, y que sellan correctamente el par de entrada.",
        "Seguro de terceros obligatorio: Malaui es miembro de COMESA (Yellow Card) y de la SADC. Si no se lleva Yellow Card válida, se compra el seguro local en la propia frontera.",
        "Tasas de frontera para vehículo extranjero (tasa de carreteras/acceso y otras): varias ventanillas y pago en efectivo. Llevar dólares en billetes pequeños además de kwacha.",
        "Permiso internacional de conducción recomendado; hay controles de policía frecuentes pero rutinarios en los ejes principales.",
        "Repostar a fondo antes de Nyika, antes del escarpe de Livingstonia y antes de cualquier bloque de parque: arriba no hay nada, y a nivel nacional hay episodios de desabastecimiento.",
        "Dos vehículos es la configuración correcta para la subida a Livingstonia y para la pista de Nyika: ninguna de las dos tiene tráfico del que depender.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Registrar el aparato y solicitar autorización previa ante la autoridad de aviación civil de Malaui, con semanas de margen; llevar el permiso impreso.",
        "No volar en Nyika, Liwonde, Majete, Nkhotakota, Kasungu ni en el Parque Nacional del Lago Malaui sin autorización específica del gestor del área.",
        "Los mejores sitios para volar con permiso, por estar fuera de parque, son el escarpe de Livingstonia, la meseta de Zomba, las plantaciones de té y la costa fuera del PN del Lago Malaui.",
        "No volar sobre instalaciones oficiales, aeropuertos ni el palacio presidencial de Lilongüe.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado dado por activo en revisiones anteriores del proyecto, pero NO reverificado en esta: comprobar el mapa oficial de disponibilidad 30-60 días antes de entrar.",
        "SIM local (TNM, Airtel Malawi) como base garantizada: cobertura razonable en el eje M1 y en la costa del lago, irregular en Nyika, en el escarpe y en el interior de los parques.",
        "Contar con 1-3 días sin cobertura útil en Nyika y en la meseta de Mulanje: avisar del itinerario antes de subir a cualquiera de las dos.",
    ],
    perro_intro=[
        "Permiso de importación previo del Department of Animal Health and Livestock Development (Lilongüe) — el dosier canino del proyecto lo marca como PROBABLE, no confirmado: escribir con antelación y no darlo por resuelto en la frontera.",
        "Certificado veterinario internacional reciente y vacuna antirrábica en vigor, además de los requisitos comunes del proyecto (microchip, pasaporte UE, titulación serológica ya obtenida).",
        "Malaui es uno de los países MÁS FÁCILES del viaje con el perro fuera de los parques: toda la costa del lago está llena de campings y lodges con parcela que lo aceptan sin problema.",
        "Prohibido en los seis parques y reservas. No hace falta guardería: el país es tan pequeño que en todos los casos hay una base a 1-3 h donde se queda uno de los tres viajeros con el perro mientras los otros hacen el parque en el día.",
        "Riesgos específicos para el perro aquí: calor y sol en la costa, cocodrilos e hipopótamos en el Shire y en las desembocaduras, babuinos en Zomba y Mulanje, y bilharzia también en el agua del lago — consultar con el veterinario antes de entrar si se le va a dejar bañarse.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "BILHARZIA (esquistosomiasis) EN EL LAGO MALAUI — el dato sanitario clave de este país, y el que más gente ignora. El parásito se transmite por larvas liberadas por caracoles de agua dulce que penetran la piel intacta con solo estar dentro del agua unos minutos; no hace falta beber ni tragar. En el lago Malaui el caracol endémico Bulinus nyassanus actúa como hospedador intermedio desde mediados de los años ochenta, lo que significa que el riesgo NO se limita a las orillas someras con vegetación junto a los pueblos: también hay transmisión documentada en aguas del propio lago. Ningún tramo puede darse por seguro, ni siquiera Cabo Maclear o las islas.",
        "Qué se hace en la práctica: la mayoría de viajeros de larga duración se baña y asume la exposición, y después se trata con praziquantel (dosis única según peso) pasadas unas semanas desde el último contacto con el agua, porque el tratamiento antes de que el parásito madure no es eficaz; alternativamente se hace serología unas semanas después. Esto NO es una recomendación médica: es el protocolo que hay que consultar y cerrar con Sanidad Exterior o con un centro de medicina del viajero ANTES de salir de España, llevando el fármaco encima si así se decide.",
        "Medidas que reducen el riesgo sin eliminarlo: evitar las orillas someras con juncos y con actividad humana, preferir agua profunda y alejada de la costa, salir y secarse enérgicamente con toalla, y no usar nunca agua del lago sin filtrar y tratar para beber o lavar los dientes.",
        "Malaria intensa en todo el país y todo el año, especialmente en la costa del lago y en el valle del Shire (Liwonde, Majete); menos en altura (Zomba, Nyika, Mulanje, Dedza). Profilaxis a valorar con Sanidad Exterior, más mosquitera y repelente: es de los tramos de mayor exposición del viaje.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Cólera: Malaui ha sufrido brotes importantes en los últimos años ligados a la estación de lluvias. Agua embotellada o tratada siempre, y comprobar la situación epidemiológica antes de entrar.",
        "Cocodrilos e hipopótamos: reales y peligrosos en el río Shire (Liwonde, Majete, Mangochi) y en las desembocaduras de los ríos del lago. En las playas abiertas del lago el riesgo es bajo pero no nulo: preguntar SIEMPRE en el alojamiento.",
        "Referencias sanitarias: Kamuzu Central (Lilongüe) y Queen Elizabeth Central (Blantyre), más las clínicas privadas de ambas ciudades; hospital de Mzuzu en el norte. Para lo serio, evacuación a Sudáfrica: seguro con evacuación médica real imprescindible.",
    ],
    seguridad_intro=("Malaui es de los tramos más tranquilos que puede recorrer este viaje: sin conflicto armado, sin insurgencia, sin zonas excluidas y con una reputación de amabilidad que es casi un tópico "
                     "(«the warm heart of Africa»). Los riesgos reales aquí no son de seguridad ciudadana, sino de carretera, de agua y de montaña."),
    seguridad=[
        "Sin zonas excluidas por seguridad en ninguno de los dos corredores previstos.",
        "Delincuencia común de oportunidad en Lilongüe (Old Town, mercados) y Blantyre: aparcamiento vigilado, nada a la vista dentro del vehículo, y precaución de noche a pie. Nada fuera de lo normal.",
        "Carretera: el riesgo número uno del país. La M1 y la M5 son estrechas, con arcén ocupado por peatones, bicicletas y carros, baches profundos y camiones lentos. NO conducir de noche bajo ningún concepto.",
        "La subida de Livingstonia y la pista de Nyika: conducir despacio, con luz de día, tocando el claxon en las curvas ciegas y sin cruzarse en las horquillas.",
        "Montaña: Mulanje es la causa habitual de accidentes graves de turistas en Malaui — niebla repentina, terreno de bloques y falta de cobertura. Guía obligatorio en la práctica, itinerario registrado en la oficina forestal, y no subir con lluvia.",
        "Agua: cocodrilos e hipopótamos en el Shire y en las desembocaduras, y corrientes y tormentas repentinas en el lago, que tiene 560-580 km de largo y oleaje real cuando sopla el mwera. Preguntar antes de bañarse o salir en kayak.",
        "Combustible y divisas: llevar efectivo, no depender de tarjeta fuera de Lilongüe y Blantyre, y no apurar el depósito ante el riesgo de colas o desabastecimiento.",
    ],
    agua=[
        "Lilongüe, Blantyre, Mzuzu y Zomba: agua embotellada sin problema en supermercados.",
        "Recarga del depósito de uso general (ducha, aseo, limpieza): todos los campings y lodges del lago (Cabo Maclear, Nkhata Bay, Chintheche, Senga Bay, Chitimba) y los de Zomba, Lilongüe y Blantyre permiten llenar con manguera; confirmar en recepción.",
        "NUNCA tomar agua directamente del lago ni de los ríos sin filtrar y tratar: además del riesgo microbiológico habitual, el lago es foco de bilharzia y el país ha tenido brotes de cólera.",
        "Nyika y la meseta de Mulanje: subir con los depósitos al 100% y con capacidad de filtrado; arriba hay arroyos pero ningún suministro tratado.",
    ],
    combustible=[
        "Sin ningún hueco de 500 km en el itinerario: Songwe → Karonga (~45 km) → Mzuzu (~195 km) → Nkhata Bay (~45 km) → Nkhotakota (~210 km) → Salima (~145 km) → Lilongüe (~105 km) → Monkey Bay (~200 km) → Liwonde (~130 km) → Blantyre (~125 km) → Mwanza (~110 km), todos con estaciones formales.",
        "Mejores plazas: Lilongüe y Blantyre, después Mzuzu, Zomba y Karonga. Marcas habituales: Puma, Total y Petroda.",
        "EL PROBLEMA NO ES LA DISTANCIA, ES EL SUMINISTRO: por la crisis crónica de divisas, Malaui ha tenido episodios repetidos de desabastecimiento de gasóleo con colas de horas. Repostar siempre que haya, llevar garrafas llenas y comprobar la situación antes de entrar al país.",
        "Sin repostaje dentro de Nyika (Chelinda), ni arriba en Livingstonia, ni en la meseta de Zomba ni en los parques: entrar lleno en los cuatro casos.",
    ],
    experiencias_intro=("Relatos y datos recurrentes de otros overlanders sobre Malaui. Léase con la advertencia del primer punto: en esta revisión no se pudo acceder directamente "
                        "a iOverlander ni a Tracks4Africa, así que esta sección es un punto de partida a contrastar, no una fuente cerrada."),
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("DECISIÓN PRINCIPAL", "Decidir si Malaui entra o no en la ruta, y en cuál de las dos formas: bucle completo (~1.900 km / 16-21 días, con salida por Tete y renuncia al norte de Mozambique) o variante corta (~1.100 km / 9-12 días, con salida a Niassa por Chiponde y sin coste para el itinerario mozambiqueño)"),
        ("Visado", "CONFIRMAR en fuente oficial malauí si la exención para España con efecto 3 de enero de 2026 está realmente en vigor, o si sigue haciendo falta eVisa en evisa.gov.mw. Es el primer trámite del país y no admite suposiciones"),
        ("Frontera de Songwe", "Confirmar horario real, tasas de vehículo y si sellan CPD o emiten TIP; y comprobar el efecto sobre el visado si se llega sin eVisa"),
        ("Frontera de Chiponde", "Confirmar el estado de la pista en el lado mozambiqueño y el horario del paso: de ello depende que la variante corta funcione"),
        ("Bilharzia", "Cerrar con Sanidad Exterior o medicina del viajero el protocolo concreto (praziquantel preventivo tras exposición vs. serología posterior) y llevar la pauta por escrito antes de salir de España"),
        ("Combustible", "Comprobar la situación de suministro de gasóleo en el país 30 días antes de entrar; es el riesgo operativo real de Malaui"),
        ("Perro", "Escribir al Department of Animal Health and Livestock Development (Lilongüe) para confirmar el permiso de importación y el puesto fronterizo concreto (Songwe) — el dosier canino lo tiene como PROBABLE, no confirmado"),
        ("Perro y Likoma", "Confirmar con la naviera del MV Ilala si admite animales; si no, el perro se queda en el continente con uno de los viajeros"),
        ("Mulanje", "Contactar con el Mulanje Mountain Conservation Trust / oficina forestal de Likhubula para tasas, guías, porteadores, reserva de refugios y política sobre perros al pie de la montaña"),
        ("Nyika", "Confirmar con el DNPW las tasas, el estado de la pista de Thazima, la disponibilidad de Chelinda y qué travesías guiadas de varios días se ofrecen actualmente"),
        ("Majete", "Confirmar si sigue permitida la autoconducción por la red de pistas y si el campamento admite vehículo propio"),
        ("Dron", "Iniciar el trámite de registro y autorización ante la autoridad de aviación civil con semanas de antelación, o descartar el dron en este país"),
        ("Starlink", "Reverificar el estado real del servicio en el mapa oficial: en esta revisión no se pudo confirmar"),
        ("FOTOS", "Los 22 PDIs usan solo las cinco imágenes de Malaui ya verificadas en el proyecto, porque en esta revisión commons.wikimedia.org no era accesible desde el entorno de trabajo. Los 17 PDIs que llevan foto prestada lo dicen en su descripción: sustituir una a una cuando se puedan verificar nombres de archivo"),
        ("Experiencias de overlanders", "Reverificar toda la sección en iOverlander y Tracks4Africa: en esta revisión los dominios no fueron accesibles"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Ficha de una ALTERNATIVA que hoy no forma parte de la ruta fija. Es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Consulado Honorario de España en Lilongüe: (+265) 999 846 081 · Embajada de España en Harare (competente para Malaui), emergencia consular: +263 (0)772 436 620.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

# -*- coding: utf-8 -*-
"""Uganda — ficha completa (12 sep 2026): ALTERNATIVA (no está en la ruta fija).
Desvío desde Kenia (Malaba/Busia) con salida hacia Ruanda (Cyanika/Katuna) o
regreso a Tanzania (Mutukula). Criterio del dueño: solo entra si hay tiempo y si
la eVisa sirve para ENTRADA TERRESTRE."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"
NOFOTO = "Sin fotografía verificada en esta revisión (ver pendientes)"

POIS = [
    dict(n=1, name="Cataratas de Sipi", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=1.3344, lon=34.3900,
         desc="Primera parada natural nada más entrar desde Kenia y una de las mejores sorpresas del país: tres saltos escalonados en la ladera noroeste del monte Elgon — Sipi (95 m), Ngasire (unos 85 m) y Simba (74 m) — unidos por un sendero de medio día entre cafetales de arábica bugisu. El pueblo de Sipi está a unos 1.775 m, así que se duerme fresco, y hay campings con vistas al salto principal. Se combina con visitas a las cooperativas de café y con abseil comercial por la pared del salto grande.",
         credit=NOFOTO, source=""),
    dict(n=2, name="Monte Elgon · pico Wagagai y la caldera", cat="Naturaleza", prio="Media", dog="prohibido en el parque", time="4–5 días si se hace la travesía",
         lat=1.1378, lon=34.5603,
         desc="Volcán apagado gigantesco en la frontera con Kenia, con una de las calderas intactas más grandes del mundo y el pico Wagagai (4.321 m) íntegramente en territorio ugandés. Es un trekking mucho menos masificado y mucho más barato que el Kilimanjaro o el monte Kenia, sin necesidad de escalada técnica: 4–5 días por las rutas de Sasa, Piswa o Sipi. Dentro están las cuevas de sal (Kitum y Makingeny) a las que los elefantes entran de noche a rascar la roca.",
         credit=NOFOTO, source=""),
    dict(n=3, name="Jinja y la fuente del Nilo", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=0.4233, lon=33.2039,
         desc="Aquí el Nilo Blanco sale del lago Victoria y empieza sus 6.700 km hasta el Mediterráneo: es literalmente el arranque del río que el viaje ya habrá cruzado o bordeará. Speke describió en 1862 unas cataratas «de unos cuatro metros de caída y ciento cincuenta de ancho» (las Ripon) que la presa de Owen Falls anegó en 1954. Hoy Jinja es la capital ugandesa de la aventura: rafting de aguas bravas de clase IV-V en los rápidos de aguas abajo, puenting sobre el río, kayak y quads. Segunda economía del país y buena base de servicios a 81 km de Kampala.",
         credit=NOFOTO, source=""),
    dict(n=4, name="Kampala", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=0.3476, lon=32.5825,
         desc="Capital repartida sobre siete colinas y la gran base logística del desvío: talleres, recambios, veterinarios de buen nivel, supermercados y bancos. Tiene además un patrimonio que casi nadie visita: las Tumbas de los Kabaka de Kasubi (Patrimonio de la Humanidad, mausoleo de los reyes de Buganda, reconstruido tras el incendio de 2010), el palacio del Kabaka con las cámaras de tortura de Idi Amín en el subsuelo, la catedral de Namirembe y el enorme mercado de Owino. Tráfico denso y caótico: conviene entrar y salir a primera hora.",
         credit="Todd Huffman · CC BY 2.0", source=W + "Kampala%20skyline.jpg?width=900"),
    dict(n=5, name="Entebbe · jardines botánicos y la orilla del Victoria", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=0.0500, lon=32.4600,
         desc="Península sobre el lago Victoria a 34 km de Kampala, mucho más tranquila que la capital y mejor sitio para dormir con el perro. Los Jardines Botánicos Nacionales, trazados en 1898, bajan hasta la propia orilla y son un paseo de sombra con colobos y turacos; al lado está el Centro de Educación de Vida Silvestre (el antiguo zoo), y desde el embarcadero salen las lanchas a la isla de Ngamba, santuario de chimpancés huérfanos. Es también el aeropuerto internacional del país: punto de entrada y salida de recambios y de gente que se incorpore al viaje.",
         credit=NOFOTO, source=""),
    dict(n=6, name="Islas Ssese (lago Victoria)", cat="Costa", prio="Media", dog="por confirmar", time="2 noches",
         lat=-0.4000, lon=32.3000,
         desc="Archipiélago de 84 islas en el noroeste del lago Victoria, con playas de arena, bosque y una calma total; se llega en ferry desde Entebbe (a Kalangala, en la isla de Bugala) o desde Bukakata, cerca de Masaka, con un ferry corto que admite vehículos y es gratuito. Es el descanso de playa del interior de África: hamacas, pescado y cero tráfico. Ojo: hay bilharzia en gran parte de la orilla del lago Victoria, así que bañarse no es recomendable ni para las personas ni para el perro.",
         credit=NOFOTO, source=""),
    dict(n=7, name="Santuario de rinocerontes de Ziwa", cat="Naturaleza", prio="Alta", dog="prohibido", time="1 noche",
         lat=1.4856, lon=32.0953,
         desc="El único sitio de Uganda donde hay rinocerontes en libertad: el país los perdió por completo con la caza furtiva de los años setenta y ochenta, y en 2005 se reintrodujeron seis ejemplares de rinoceronte blanco que en julio de 2025 ya eran 48. Lo excepcional es la actividad: el seguimiento se hace A PIE, acompañando a los rastreadores hasta unos metros de los animales, que es una experiencia radicalmente distinta a mirarlos desde el coche. Está a 164 km al norte de Kampala, justo en la carretera de Murchison Falls: parada natural de camino. También hay excursión al pantano en busca del picozapato.",
         credit=NOFOTO, source=""),
    dict(n=8, name="Cataratas Murchison · el Nilo estrangulado", cat="Naturaleza", prio="Alta", dog="prohibido", time="2–3 noches",
         lat=2.2783, lon=31.6856,
         desc="El espectáculo hidráulico más brutal del viaje: todo el caudal del Nilo Victoria, un río de cientos de metros de ancho, se comprime en una grieta de MENOS DE 10 METROS y se despeña 43 m con un estruendo que se oye antes de verlo. Uganda rechazó en 2019 un proyecto hidroeléctrico para no tocarlo. Se ve desde arriba (hay un sendero corto desde el aparcamiento hasta el «Top of the Falls») y desde abajo, en la lancha que sube desde Paraa. El parque que lo rodea es el mayor del país, con elefantes, jirafas de Rothschild, leones y el delta del Nilo Victoria, uno de los mejores sitios del mundo para ver el picozapato.",
         credit=NOFOTO, source=""),
    dict(n=9, name="Parque Nacional del Valle de Kidepo", cat="Naturaleza", prio="Alta", dog="prohibido", time="3 noches",
         lat=3.9000, lon=33.8500,
         desc="EL PARQUE MÁS REMOTO Y SALVAJE DE UGANDA, en el extremo noreste contra la frontera con Sudán del Sur: 1.442 km² de sabana entre montañas, con dos valles fluviales estacionales (Kidepo y Narus) y una sensación de vacío que no tiene ningún otro parque de África oriental. 77 especies de mamíferos y 476 de aves, con avestruces, guepardos, caracales y licaones que no están en el resto del país, más de 400 elefantes y jirafas reintroducidas. Está a 520 km de Kampala por carretera: es un desvío dentro del desvío, pero quien llega coincide en que es el mejor parque del país. Territorio karamojong: cultura pastoril viva.",
         credit=NOFOTO, source=""),
    dict(n=10, name="Gulu y el norte", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=2.7747, lon=32.2990,
         desc="Principal ciudad del norte y nudo logístico obligado del bucle a Kidepo: combustible fiable, talleres, bancos y hospitales. Fue el epicentro del conflicto del Ejército de Resistencia del Señor (LRA) de Joseph Kony entre 1987 y 2006, con cientos de miles de desplazados; hoy la región está en paz y reconstruida, y merece la pena entenderlo antes de cruzarla. Desde aquí salen las pistas hacia Kitgum y Kidepo por el este, y hacia Murchison Falls por el sur.",
         credit=NOFOTO, source=""),
    dict(n=11, name="Fort Portal y los lagos de cráter de Ndali-Kasenda", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=0.6710, lon=30.2750,
         desc="Ciudad de altura al pie de los Rwenzori, capital del reino tradicional de Toro y una de las zonas más bonitas y menos visitadas del país: alrededor hay más de cincuenta lagos de cráter volcánico, verdes y redondos, encajados entre plantaciones de té y bananeras. Se recorren en un bucle de pistas de tierra ideal para el 4x4, con miradores como el de Top of the World sobre el lago Nkuruba, y se pueden caminar y hasta nadar en varios de ellos (los cráteres no tienen bilharzia ni cocodrilos, a diferencia del Victoria). Buen sitio para acampar y para el perro.",
         credit=NOFOTO, source=""),
    dict(n=12, name="Parque Nacional de Kibale · chimpancés", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 noches",
         lat=0.5000, lon=30.4000,
         desc="La mayor concentración de primates de África oriental: trece especies en un mismo bosque, incluidos varios grupos de chimpancés habituados a la presencia humana. El seguimiento de chimpancés dura una hora con el grupo, y existe además una modalidad de día completo (habituación) que permite acompañarlos desde que se despiertan. Junto al parque, el pantano comunitario de Bigodi es un proyecto local excelente y mucho más barato, con paseo de dos horas entre monos y aves. Fuera del parque, el perro puede quedarse en los alojamientos de Bigodi o Fort Portal.",
         credit=NOFOTO, source=""),
    dict(n=13, name="Montes Rwenzori · las Montañas de la Luna", cat="Patrimonio UNESCO", prio="Alta", dog="prohibido en el parque", time="7–9 días la travesía completa",
         lat=0.3858, lon=29.8717,
         desc="LA GRAN CAMINATA DEL DESVÍO y una rareza planetaria: glaciares permanentes prácticamente sobre el ecuador. Ptolomeo las llamó las Montañas de la Luna y las señaló como fuente del Nilo. El pico Margherita, en el monte Stanley (5.109 m), es el tercero más alto de África tras el Kilimanjaro y el monte Kenia, y el único de los tres que exige travesía de glaciar con cuerda, crampones y piolet. Hay dos circuitos: el Central Circuit (7–9 días, desde Nyakalengija) y la ruta de Kilembe por el sur. Aunque no se suba al pico, los tres o cuatro primeros días atraviesan un bosque de brezos gigantes, lobelias y senecios arborescentes que parece de otro planeta. Patrimonio de la Humanidad. Los glaciares están en retroceso acelerado: de 43 glaciares en 1906 a menos de la mitad en 2005.",
         credit=NOFOTO, source=""),
    dict(n=14, name="Katwe · salinas y campo de cráteres", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="medio día",
         lat=-0.1333, lon=29.8833,
         desc="Al norte del canal de Kazinga se abre un campo volcánico de cráteres jóvenes, y en uno de ellos, el lago Katwe, se extrae sal a mano desde hace siglos en salinas de estanques familiares: los trabajadores entran en la salmuera a cortar bloques de sal con las piernas protegidas. Es un sitio duro y fascinante, fuera del recinto de pago del parque, así que se puede visitar sin entrada de parque nacional y, en principio, con el perro dentro del vehículo. La pista de los cráteres (Explosion Crater Drive) es uno de los recorridos con mejores vistas del país.",
         credit=NOFOTO, source=""),
    dict(n=15, name="Parque Nacional Queen Elizabeth · canal de Kazinga", cat="Naturaleza", prio="Alta", dog="prohibido", time="2–3 noches",
         lat=-0.1372, lon=30.0411,
         desc="1.978 km² entre el lago George y el lago Edward, con 95 especies de mamíferos y más de 600 de aves — una de las cifras más altas de África para un solo parque. Su joya es el CANAL DE KAZINGA, un brazo natural de 32 km que une los dos lagos y donde se acumula la mayor concentración de hipopótamos del continente: el crucero de dos horas por el canal es, por relación calidad-precio, la mejor actividad de fauna de Uganda, con elefantes y búfalos bajando a beber a pocos metros de la barca. La carretera pública que cruza el parque hacia Kasese se puede recorrer sin pagar entrada.",
         credit=NOFOTO, source=""),
    dict(n=16, name="Ishasha · los leones trepadores", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 noches",
         lat=-0.6167, lon=29.6667,
         desc="Sector sur de Queen Elizabeth y una de las dos únicas poblaciones del mundo donde los leones suben habitualmente a los árboles: aquí se tumban en las ramas horizontales de las higueras sicómoro, con los machos de melena negra colgando las patas, a veces cinco o seis en el mismo árbol. Nadie ha explicado del todo por qué lo hacen (¿moscas?, ¿calor?, ¿ver mejor los kob?). No hay garantía de verlos, pero el sector es además la vía natural de paso hacia Bwindi: cae de camino. Coordenadas aproximadas del sector, por confirmar sobre el terreno.",
         credit=NOFOTO, source=""),
    dict(n=17, name="Bosque Impenetrable de Bwindi (Buhoma)", cat="Patrimonio UNESCO", prio="Alta", dog="prohibido", time="2–3 noches",
         lat=-1.0500, lon=29.6167,
         desc="EL MOTIVO DE TODO EL DESVÍO. Selva de montaña de 25.000 años de antigüedad, Patrimonio de la Humanidad, que alberga cerca de la mitad de los gorilas de montaña que quedan en el planeta. El seguimiento es a pie por ladera empinada y barro, entre dos y ocho horas de caminata, para pasar exactamente UNA HORA con una familia de gorilas a siete metros. Hay cuatro sectores con cupos separados — Buhoma (norte, el clásico), Ruhija (este, el más alto), Rushaga y Nkuringo (sur, los más cercanos a Kisoro y a Ruanda) —, y el permiso se asigna a un sector concreto, así que hay que elegirlo al reservar. En Rushaga existe además la «habituación», cuatro horas con un grupo aún en proceso de acostumbrarse. Cupo diario muy limitado: se reserva con meses de antelación.",
         credit="Giles Laurent · CC BY-SA 4.0", source=W + "068%20Mountain%20gorilla%20close-up%20at%20Bwindi%20Impenetrable%20Forest%20National%20Park%20Photo%20by%20Giles%20Laurent.jpg?width=900"),
    dict(n=18, name="Parque Nacional de los Gorilas de Mgahinga", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 noches",
         lat=-1.3694, lon=29.6403,
         desc="El parque más pequeño de Uganda (33,9 km²) y el más espectacular de ver: la esquina ugandesa de los volcanes Virunga, con tres conos apagados — Muhabura (4.127 m), Gahinga y Sabyinyo — sobre los que se puede subir a pie en el día. En la cumbre del Sabyinyo se pisan a la vez Uganda, Ruanda y RD Congo. Tiene un grupo de gorilas de montaña (el Nyakagezi, que a veces cruza a Ruanda) y, sobre todo, los MONOS DORADOS, endémicos de los Virunga y mucho más baratos de ver que los gorilas. Además está el Batwa Trail, recorrido guiado por los propios batwa (pigmeos) expulsados del bosque en 1991, que cuentan su vida anterior dentro de él. Alternativa seria a Bwindi si los permisos de Bwindi están agotados.",
         credit=NOFOTO, source=""),
    dict(n=19, name="Lago Bunyonyi", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-1.2833, lon=29.9167,
         desc="«El lugar de los muchos pajarillos»: un lago de 40 m de profundidad encajado entre colinas aterrazadas, con 29 islas y más de 200 especies de aves, a 7 km de Kabale y a 1.960 m de altitud. Es el sitio donde descansar antes o después del trekking de gorilas, y el mejor lugar del suroeste para estar con el perro: campings en la orilla, canoas de madera y una temperatura fresca y sin mosquitos de malaria por la altura. Entre las islas está Akampene, la «isla del castigo», donde se abandonaba a las muchachas embarazadas fuera del matrimonio. Se puede nadar: no hay cocodrilos ni hipopótamos, y es uno de los pocos lagos africanos sin bilharzia documentada (aun así, confirmar en el momento).",
         credit=NOFOTO, source=""),
    dict(n=20, name="Parque Nacional del Lago Mburo", cat="Naturaleza", prio="Media", dog="prohibido", time="1 noche",
         lat=-0.6278, lon=30.9667,
         desc="El parque pequeño (260 km²) que cae justo en la carretera principal Kampala–Mbarara, a 240 km de la capital: la parada perfecta para no hacer de un tirón el regreso desde el suroeste. Es el único sitio de Uganda con cebras en cantidad, y tiene impalas, elands, búfalos, hipopótamos, jirafas de Rothschild reintroducidas en 2015 y más de 300 especies de aves. Al no haber leones desde los años ochenta, aquí SÍ se permiten los safaris a pie con ranger y los paseos a caballo, cosa imposible en los parques grandes.",
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
    ("Frontera · Entrada — Malaba (con Kenia)", "Frontera", 0.6333, 34.2667,
     "Principal paso del Corredor Norte desde Kenia; puesto de ventanilla única (OSBP) con tráfico pesado de camiones y esperas variables. La eVisa ugandesa hay que llevarla YA IMPRESA."),
    ("Frontera · Entrada alternativa — Busia (con Kenia)", "Frontera", 0.4667, 34.0833,
     "Alternativa a Malaba, también OSBP y bastante menos congestionada de camiones; suele ser más rápida para turismo. Enlaza igual de bien con Jinja."),
    ("Frontera · Salida — Cyanika (con Ruanda)", "Frontera", -1.2333, 29.6333,
     "Paso del extremo suroeste, entre Kisoro y Musanze (Ruanda): la salida lógica si se encadena Bwindi/Mgahinga con el Parque de los Volcanes. Puesto pequeño y rápido. HORARIO LIMITADO (no 24 h): confirmar antes de llegar."),
    ("Frontera · Salida alternativa — Katuna/Gatuna (con Ruanda)", "Frontera", -1.2333, 29.9833,
     "Paso principal entre Kabale y Kigali, en la carretera troncal: más tráfico y trámite más formal que Cyanika, pero mejor asfalto. Estuvo cerrado por la crisis Ruanda-Uganda de 2019-2022 y volvió a abrir: confirmar estado real antes de contar con él."),
    ("Frontera · Salida alternativa — Mutukula (con Tanzania)", "Frontera", -1.0000, 31.4000,
     "Si no se sigue a Ruanda, es la salida al sur hacia Bukoba y el lago Victoria tanzano; cae bien tras el Lago Mburo. Coordenadas aproximadas, por confirmar."),
    ("Embajada de España en Nairobi (competente para Uganda)", "Consular", -1.2977, 36.8129,
     "No hay embajada de España en Uganda. CBA Building, 3ª planta, Mara & Ragati Roads, Upper Hill, Nairobi (Kenia). Tel. +254 20 272 02 22/3/4/5; emergencia consular +254 733 63 11 44."),
    ("International Hospital Kampala / Mulago National Referral Hospital", "Hospital", 0.3419, 32.5764,
     "Mulago es el hospital nacional de referencia; el International Hospital Kampala (IHK, privado) es la opción habitual para extranjeros. Para casos serios, la práctica regional es evacuación a Nairobi."),
    ("Combustible · Kampala, Jinja, Gulu, Mbarara, Kasese, Kabale", "Combustible", 0.3476, 32.5825,
     "Estaciones formales (Shell/Vivo, TotalEnergies, Stabex, City Oil) en todas las ciudades del eje. Repostar a fondo en Gulu antes del bucle a Kidepo y en Kabale/Kisoro antes del tramo final a Bwindi."),
    ("Agua potable y de uso general · Kampala, Entebbe, Jinja, Fort Portal", "Agua potable", 0.0500, 32.4600,
     "Agua embotellada sin problema en todas las ciudades. Para el depósito de uso general, los campings de Jinja, Entebbe, Fort Portal, Bunyonyi y Buhoma permiten llenar con manguera; confirmar en recepción."),
]

DRONE_CALLOUT = ("danger", "Uno de los países más restrictivos de la ruta: permiso previo y riesgo de requisa en aduana",
                 "Uganda exige autorización previa de la Uganda Civil Aviation Authority (UCAA) para cualquier vuelo, incluido el recreativo, y el trámite es lento y poco predecible. Además hay casos documentados de RETENCIÓN DEL DRON EN ADUANA a la entrada por Entebbe cuando no se lleva permiso previo, con devolución a la salida. Dentro de los parques de la Uganda Wildlife Authority (Bwindi, Queen Elizabeth, Murchison, Kidepo) el vuelo está prohibido salvo autorización expresa del UWA, que en la práctica no se concede a particulares. Norma del proyecto: NO volar en Uganda salvo permiso escrito ya en la mano, y declarar el dron en frontera terrestre.")

STARLINK_CALLOUT = ("ok", "Activo comercialmente — el respaldo más fiable del desvío",
                    "Starlink opera en Uganda desde 2023 y da cobertura razonable en todo el país, incluido el suroeste (Kabale, Kisoro, Bwindi) y el norte (Gulu, Kidepo), que es donde la red móvil flaquea. La red terrestre de MTN Uganda y Airtel Uganda es buena en el eje Kampala-Jinja-Mbarara y decente en el suroeste; en Kidepo y en el interior de los parques es intermitente. Confirmar el estado del servicio 30-60 días antes por si hubiera pausas de altas nuevas, como ha pasado en Kenia.")

DOG_MATRIX = [
    ("TODOS los parques de la Uganda Wildlife Authority", "prohibido",
     "Bwindi, Mgahinga, Queen Elizabeth, Murchison Falls, Kidepo, Kibale, Rwenzori, Lago Mburo y Elgon no admiten mascotas. En los de gorilas y chimpancés la prohibición es SANITARIA y absoluta, no administrativa: los grandes simios comparten patógenos con el perro y con nosotros (por eso hay distancia mínima y mascarilla obligatoria). Plan B: turnos entre los tres viajeros con base en Kisoro, Kabale, Bunyonyi, Kasese o Fort Portal."),
    ("Bwindi y Mgahinga (zona de gorilas)", "prohibido",
     "Además del reglamento del parque, hay un motivo sanitario específico y bien documentado: existe literatura publicada sobre TRIPANOSOMIASIS CANINA en la zona de Bwindi-Mgahinga y Queen Elizabeth, es decir, riesgo alto para el propio perro (mosca tsetse). Es una zona donde el perro no solo estorba: corre peligro. Dejarlo en Kisoro o en Bunyonyi, y profilaxis antiparasitaria sin fallos."),
    ("Kampala, Entebbe, Jinja, Fort Portal, Kabale, Kisoro, Gulu", "permitido con condiciones",
     "Zonas urbanas sin problema con correa. Kampala y Entebbe tienen veterinarios de buen nivel y residencias caninas; Entebbe es mejor sitio que Kampala para dormir con el perro (menos tráfico, más verde, orilla del lago)."),
    ("Lago Bunyonyi y lagos de cráter de Fort Portal", "permitido con condiciones",
     "La mejor zona del país con el perro: campings en la orilla, fresco de altura, sin mosquitos de malaria y fuera de recinto de parque. Es la base natural para los turnos durante el trekking de gorilas."),
    ("Katwe (salinas y cráteres) y carretera pública de Queen Elizabeth", "por confirmar",
     "Las salinas de Katwe y la carretera pública que cruza el parque hacia Kasese quedan fuera del recinto de pago: en principio se pasa con el perro dentro del vehículo sin entrar en el parque. CONFIRMAR en la puerta del UWA antes de darlo por bueno."),
    ("Orilla del lago Victoria (Entebbe, Ssese, Jinja)", "permitido con condiciones",
     "Cuidado real: BILHARZIA en gran parte de la orilla del Victoria y cocodrilos en algunas zonas. No dejar que el perro beba ni se bañe en el lago; sí es seguro en los lagos de cráter de Fort Portal y en Bunyonyi."),
]

SOURCES = [
    ("Uganda Immigration · portal oficial de visados electrónicos", "https://visas.immigration.go.ug/"),
    ("Uganda Wildlife Authority · permisos de trekking de gorilas y tarifas", "https://www.ugandawildlife.org/"),
    ("Uganda Civil Aviation Authority · normativa de drones", "https://www.caa.co.ug/"),
    ("UNESCO · Bosque Impenetrable de Bwindi, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/682/"),
    ("UNESCO · Montes Rwenzori, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/684/"),
    ("Wikipedia · Política de visados de Uganda (eVisa obligatoria y Visado Turístico de África Oriental)", "https://en.wikipedia.org/wiki/Visa_policy_of_Uganda"),
    ("Wikipedia · Cataratas Murchison (el Nilo comprimido en menos de 10 m)", "https://en.wikipedia.org/wiki/Murchison_Falls"),
    ("Wikipedia · Parque Nacional del Valle de Kidepo (superficie, fauna y distancias)", "https://en.wikipedia.org/wiki/Kidepo_Valley_National_Park"),
    ("Wikipedia · Santuario de rinocerontes de Ziwa (48 rinocerontes en julio de 2025, seguimiento a pie)", "https://en.wikipedia.org/wiki/Ziwa_Rhino_Sanctuary"),
    ("Wikipedia · Montes Rwenzori (monte Stanley 5.109 m y retroceso glaciar)", "https://en.wikipedia.org/wiki/Rwenzori_Mountains"),
    ("Wikipedia · Cataratas de Sipi (alturas de los tres saltos)", "https://en.wikipedia.org/wiki/Sipi_Falls"),
    ("Wikipedia · Parque Nacional Queen Elizabeth (canal de Kazinga, Ishasha, cráteres de Katwe)", "https://en.wikipedia.org/wiki/Queen_Elizabeth_National_Park"),
    ("Wikipedia · Lago Bunyonyi (profundidad, islas, distancia a Kabale)", "https://en.wikipedia.org/wiki/Lake_Bunyonyi"),
    ("Wikipedia · Parque Nacional de Kibale (13 especies de primates)", "https://en.wikipedia.org/wiki/Kibale_National_Park"),
    ("Wikipedia · Parque Nacional de los Gorilas de Mgahinga (volcanes y monos dorados)", "https://en.wikipedia.org/wiki/Mgahinga_Gorilla_National_Park"),
    ("Wikipedia · Monte Elgon (pico Wagagai 4.321 m, caldera y cueva de Kitum)", "https://en.wikipedia.org/wiki/Mount_Elgon"),
    ("Wikipedia · Jinja y la fuente del Nilo", "https://en.wikipedia.org/wiki/Jinja,_Uganda"),
    ("Wikipedia · Parque Nacional del Lago Mburo", "https://en.wikipedia.org/wiki/Lake_Mburo_National_Park"),
    ("Wikipedia · Entebbe (jardines botánicos de 1898, distancia a Kampala)", "https://en.wikipedia.org/wiki/Entebbe"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("iOverlander · puntos de combustible, agua y acampada verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Corredor de entrada: Malaba → este (Elgon/Sipi) → Jinja → Kampala/Entebbe → Ziwa → Murchison → Kidepo → Gulu → Kampala
CORRIDOR = [(0.6333, 34.2667), (1.3344, 34.3900), (1.1378, 34.5603), (0.4233, 33.2039),
            (0.3476, 32.5825), (0.0500, 32.4600), (0.3476, 32.5825), (1.4856, 32.0953),
            (2.2783, 31.6856), (2.7747, 32.2990), (3.9000, 33.8500), (2.7747, 32.2990),
            (0.3476, 32.5825)]

# Corredor de salida: Kampala → Fort Portal → Kibale → Rwenzori → QENP/Kazinga → Ishasha → Bwindi → Mgahinga → Bunyonyi → Cyanika (Ruanda)
CORRIDOR_ALT = [(0.3476, 32.5825), (0.6710, 30.2750), (0.5000, 30.4000), (0.3858, 29.8717),
                (-0.1333, 29.8833), (-0.1372, 30.0411), (-0.6167, 29.6667), (-1.0500, 29.6167),
                (-1.3694, 29.6403), (-1.2833, 29.9167), (-1.2333, 29.6333)]

HISTORIA_RESUMEN = ("Uganda combina varios reinos tradicionales de gran profundidad histórica —sobre todo Buganda, en torno a Kampala— con un colonialismo británico que dejó fronteras que agruparon a decenas de pueblos distintos, una independencia en 1962 pronto ensombrecida "
                    "por la dictadura de Idi Amín en los años setenta y por la guerra del Ejército de Resistencia del Señor en el norte hasta 2006, y una recuperación posterior que ha convertido al país en uno de los últimos refugios del gorila de montaña y en un destino de naturaleza de primer nivel.")

HISTORIA_SECCIONES = [
    ("El reino de Buganda y otros reinos tradicionales",
     "El territorio de la actual Uganda albergaba varios reinos centralizados de gran antigüedad y sofisticación política, en particular el reino de Buganda (en torno al lago Victoria y la actual Kampala), junto con Bunyoro, Toro y Busoga, "
     "con monarquías (el kabaka de Buganda, el omukama de Toro) que conservan hoy un papel ceremonial y cultural reconocido dentro del estado moderno. Las Tumbas de los Kabaka de Kasubi, en Kampala, son Patrimonio de la Humanidad."),
    ("El protectorado británico",
     "Gran Bretaña estableció un protectorado sobre Uganda en 1894, gobernando en gran medida a través de una alianza con la aristocracia de Buganda, a la que otorgó privilegios frente a otros reinos y pueblos del territorio — una dinámica de favoritismo colonial "
     "que sembró tensiones interregionales que se prolongarían mucho después de la independencia. Winston Churchill la llamó «la perla de África» tras su viaje de 1907, frase que el país sigue usando como lema turístico."),
    ("Independencia, Idi Amín y el terror de los años setenta",
     "Uganda se independizó en 1962. Tras un periodo de inestabilidad política que incluyó la abolición de los reinos tradicionales, el general Idi Amín tomó el poder en 1971 y gobernó hasta 1979 mediante una de las dictaduras más brutales de la historia africana reciente, "
     "con cientos de miles de muertos y la expulsión en 1972 de la minoría asiática del país, hasta ser derrocado tras la guerra con la Tanzania de Julius Nyerere. En 1976 el aeropuerto de Entebbe fue escenario del secuestro del vuelo de Air France y del asalto israelí para liberar a los rehenes."),
    ("La guerra del norte y el Ejército de Resistencia del Señor",
     "Entre 1987 y 2006, el norte del país (Gulu, Kitgum, Lira) sufrió la insurgencia del Ejército de Resistencia del Señor de Joseph Kony, caracterizada por el secuestro masivo de niños como soldados y por el desplazamiento de cerca de dos millones de personas a campos. "
     "El conflicto se desplazó después a RD Congo, Sudán del Sur y República Centroafricana, y el norte ugandés lleva dos décadas en paz y reconstrucción — dato relevante porque el bucle hacia Kidepo atraviesa precisamente esa región."),
    ("Situación actual: estabilidad bajo Museveni y naturaleza como motor turístico",
     "Yoweri Museveni gobierna el país desde 1986, en un periodo de relativa estabilidad y crecimiento económico marcado también por sucesivas reformas constitucionales para prolongar su mandato y por restricciones a la oposición y la prensa, "
     "un asunto con debate internacional activo. Uganda se ha consolidado entretanto como destino de naturaleza de referencia, con el trekking de gorilas de montaña en Bwindi como su gran atractivo, motivo de esta parada opcional del proyecto."),
]

HISTORIA_FUENTES = [
    ("BBC News · Uganda country profile", "https://www.bbc.com/news/world-africa-14107906"),
    ("Encyclopaedia Britannica · Uganda, History", "https://www.britannica.com/place/Uganda/History"),
    ("UNESCO · Bosque Impenetrable de Bwindi", "https://whc.unesco.org/en/list/682/"),
    ("UNESCO · Tumbas de los Kabaka de Buganda en Kasubi", "https://whc.unesco.org/en/list/1022/"),
]

SPEC = dict(
    slug="uganda", name="Uganda", revision="12 sep 2026",
    sub="ALTERNATIVA — no está en la ruta fija · desvío desde Kenia · gorilas de Bwindi · salida a Ruanda",
    chips=[
        ("ESTATUS", "ALTERNATIVA: solo si hay tiempo y si la eVisa sirve en frontera terrestre"),
        ("COSTE DEL DESVÍO", "+2.400 km y +18-24 días sobre la ruta fija (bucle completo)"),
        ("VERSIÓN CORTA", "+1.300 km y +9-11 días si solo se hace el suroeste (gorilas)"),
        ("eVISA", "OBLIGATORIA y SÍ válida por tierra — se tramita online, se imprime y se presenta"),
        ("ENTRADA", "Malaba o Busia (desde Kenia)"),
        ("SALIDA", "Cyanika o Katuna (a Ruanda) · Mutukula (a Tanzania)"),
        ("EL DATO DECISIVO", "Permiso de gorilas en Bwindi: 800 USD/persona — 2.400 USD los tres"),
        ("A PIE", "Rwenzori (Margherita, 5.109 m, con glaciar) · Elgon · Sipi · Sabyinyo"),
        ("PERRO", "Prohibido en todos los parques; zona de tsetse en Bwindi/QENP"),
        ("DRONES", "Muy restrictivo: permiso UCAA y riesgo de requisa en aduana"),
    ],
    center=[1.2, 32.3], zoom=7,
    notice="Documento de planificación de una ALTERNATIVA que aún no está decidida. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, si finalmente se incluye este desvío.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Entrada por el este y bucle del norte",
    corridor_alt_label="Oeste, gorilas y salida a Ruanda",
    hero_img=W + "068%20Mountain%20gorilla%20close-up%20at%20Bwindi%20Impenetrable%20Forest%20National%20Park%20Photo%20by%20Giles%20Laurent.jpg?width=900",
    hero_credit="Gorila de montaña en Bwindi · Giles Laurent · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("UGANDA NO ESTÁ EN LA RUTA FIJA. El dueño del proyecto la situó expresamente entre las alternativas: «Ruanda / Uganda, Esuatini / Lesoto y Gabón como alternativas si hay tiempo y si tienen eVisa». "
              "Las dos condiciones se responden así: (1) eVISA: SÍ, y sirve para entrada terrestre. Uganda obliga a tramitar la eVisa ONLINE ANTES de viajar (visas.immigration.go.ug) y a presentarla IMPRESA en el puesto fronterizo; "
              "no es un visado de aeropuerto como el de Gabón, y los pasos de Malaba, Busia, Cyanika, Katuna y Mutukula la aceptan con normalidad — la eVisa ugandesa no excluye la vía terrestre. Existe además el VISADO TURÍSTICO DE ÁFRICA ORIENTAL (100 USD, 90 días, "
              "entradas múltiples entre Kenia, Uganda y Ruanda), que es la opción inteligente si se hacen los tres países: hay que usarlo por primera vez en el país que lo emite. "
              "(2) TIEMPO: el desvío completo cuesta unos 2.400 km y 18-24 días (entrada por Malaba, este, Kampala, Murchison, Kidepo, oeste, gorilas y salida a Ruanda). Una versión corta solo del suroeste — entrar por Malaba, bajar directo a Bwindi por Mbarara y salir a Ruanda — "
              "cuesta unos 1.300 km y 9-11 días. El tercer factor, que no es de ruta sino de dinero: el permiso de gorilas de Bwindi son 800 USD POR PERSONA, o sea 2.400 USD para los tres, más la entrada al país y el alojamiento. "
              "Encaja de forma natural con Ruanda (se sale por Cyanika directamente al Parque de los Volcanes), y las dos juntas son el mismo desvío: si se hace una, se hace la otra. "
              "Si se hacen ambas, hacer el trekking de gorilas SOLO en Uganda (800 USD frente a 1.500 en Ruanda) y dejar Ruanda para Nyungwe, Kivu y Kigali es la decisión económicamente evidente."),
    facts=[
        ("Estatus", "ALTERNATIVA, no ruta fija. Depende de que sobre tiempo tras Kenia y de la decisión económica sobre el permiso de gorilas."),
        ("Coste en ruta", "Bucle completo: +2.400 km y 18-24 días. Versión corta (solo suroeste y gorilas): +1.300 km y 9-11 días. Cálculo sobre la media del proyecto de 250 km/día, con parques descontados como días sin conducir."),
        ("eVisa y entrada terrestre", "CONFIRMADO que la eVisa es obligatoria y se tramita online antes de viajar; los pasos terrestres de Malaba, Busia, Cyanika, Katuna y Mutukula la aceptan. Hay que llevar la confirmación IMPRESA, no solo en el móvil."),
        ("Visado regional", "Visado Turístico de África Oriental (EATV): 100 USD, 90 días, entradas múltiples entre Kenia, Uganda y Ruanda. Debe usarse por primera vez en el país emisor. Es la opción a estudiar si se hacen los tres."),
        ("Entrada", "Malaba (principal, mucho camión) o Busia (más rápida para turismo), ambas desde Kenia."),
        ("Salida", "Cyanika (Kisoro → Musanze, Ruanda) o Katuna (Kabale → Kigali). Alternativa sur: Mutukula hacia Tanzania."),
        ("El dato decisivo", "Permiso de trekking de gorilas en Bwindi o Mgahinga: 800 USD por persona y hora de visita para no residentes (subió desde 700 USD en julio de 2024) — POR CONFIRMAR la tarifa vigente en 2027 con la UWA. La habituación de Rushaga, unos 1.500 USD. Chimpancés en Kibale, del orden de 250 USD."),
        ("Comparación con Ruanda", "El mismo animal, en el mismo macizo: 800 USD en Uganda frente a 1.500 USD en Ruanda. Si se hacen los dos países, el trekking se hace en Uganda."),
        ("Vehículo", "CPD exigido en la práctica; seguro COMESA (tarjeta amarilla) válido; carné internacional obligatorio."),
        ("Perro", "Prohibido en todos los parques de la UWA. Además, zona documentada de tripanosomiasis canina en Bwindi-Mgahinga y Queen Elizabeth: riesgo real para el animal."),
        ("Drones", "Muy restrictivo: permiso previo de la UCAA y casos documentados de requisa en aduana. Norma del proyecto: no volar."),
        ("Starlink", "Activo desde 2023, buena cobertura incluido el norte y el suroeste. Respaldo: MTN Uganda / Airtel."),
    ],
    alerts=[
        "ESTATUS ALTERNATIVA: nada de lo que hay aquí está comprometido. Este desvío se decide después de Kenia, con el calendario real en la mano.",
        "El permiso de gorilas de Bwindi tiene CUPO DIARIO MUY LIMITADO (ocho personas por familia de gorilas y día) y se agota con meses de antelación en temporada seca (jun-sep, dic-feb). Si se decide hacerlo, hay que reservar mucho antes de entrar en Uganda, y el permiso se asigna a un SECTOR concreto (Buhoma, Ruhija, Rushaga o Nkuringo): elegirlo condiciona por dónde se entra y se sale del parque.",
        "La eVisa hay que tramitarla ONLINE ANTES DE LLEGAR A LA FRONTERA y llevarla IMPRESA. No es un visado que se compre en el puesto, y no basta con enseñarla en el móvil.",
        "Certificado internacional de FIEBRE AMARILLA exigido en frontera: lo piden de verdad en los pasos terrestres desde Kenia.",
        "Perro prohibido en todos los parques nacionales; y en Bwindi, Mgahinga y Queen Elizabeth hay además riesgo documentado de TRIPANOSOMIASIS CANINA (mosca tsetse). Profilaxis antiparasitaria sin fallos y base fija en Kisoro, Kabale o Bunyonyi.",
        "Drones: permiso previo de la UCAA obligatorio, con casos documentados de retención del aparato en aduana. Declararlo en frontera y asumir que no se vuela.",
        "Frontera de Katuna/Gatuna con Ruanda: estuvo CERRADA entre 2019 y 2022 por la crisis diplomática entre ambos países. Está reabierta, pero es una frontera que ya ha cerrado una vez: confirmar su estado 72 h antes y tener Cyanika como plan B.",
        "Norte y noreste (Karamoja, camino de Kidepo): región tranquila hoy, pero con historial de robo de ganado armado entre comunidades karamojong. Viajar de día, informarse en Gulu y Kitgum, y no improvisar rutas.",
        "Frontera oeste con RD Congo (norte del lago Alberto, Rwenzori, Ishasha): grupos armados activos EN EL LADO CONGOLEÑO. No cruzar en ningún caso y no acampar pegado a la línea fronteriza en el sector de Ishasha.",
        "Malaria en casi todo el país. Excepciones útiles por altitud: Kabale, Bunyonyi, Kisoro y las cumbres del Rwenzori y Elgon.",
    ],
    ruta_intro=("Dos corredores que no se solapan. El primero entra desde Kenia por Malaba, sube al monte Elgon y a las cataratas de Sipi, baja a la fuente del Nilo en Jinja, hace base en Kampala y Entebbe, y se lanza al norte "
                "por Ziwa y Murchison Falls hasta el remoto Kidepo. El segundo sale de Kampala hacia el oeste: Fort Portal y sus lagos de cráter, los chimpancés de Kibale, los glaciares del Rwenzori, el canal de Kazinga, "
                "los leones trepadores de Ishasha, los gorilas de Bwindi y Mgahinga, el lago Bunyonyi y la salida a Ruanda por Cyanika. Etapas calculadas sobre la media del proyecto de 250 km/día."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada y el monte Elgon", "Malaba/Busia → Mbale → Sipi Falls", "~140 km · 2-3 días (4-5 más si se sube al Wagagai)"),
        ("2 · La fuente del Nilo", "Sipi → Jinja (rafting, puenting, fuente del Nilo)", "~230 km · 2-3 días"),
        ("3 · Capital y logística", "Jinja → Kampala → Entebbe", "~120 km · 3 días de parada (talleres, veterinario, gestiones)"),
        ("4 · Opcional: el lago", "Entebbe → ferry a las islas Ssese → vuelta", "~100 km + ferry · 2-3 días"),
        ("5 · Rinocerontes a pie", "Kampala → Ziwa Rhino Sanctuary", "~165 km · 1 día"),
        ("6 · El Nilo estrangulado", "Ziwa → Murchison Falls (Paraa, Top of the Falls, delta)", "~140 km · 3 días"),
        ("7 · Al norte remoto", "Murchison → Gulu → Kitgum → Kidepo Valley", "~480 km · 3 días de pista"),
        ("8 · Kidepo", "Parque del Valle de Kidepo: valles de Narus y Kidepo, Karamoja", "3 días de parada"),
        ("9 · Vuelta al centro", "Kidepo → Gulu → Kampala", "~600 km · 3 días"),
        ("10 · Al oeste, al té y los cráteres", "Kampala → Fort Portal y los lagos de cráter de Ndali-Kasenda", "~300 km · 3 días"),
        ("11 · Chimpancés", "Fort Portal → Kibale (chimpancés) y pantano de Bigodi", "~35 km · 2 días"),
        ("12 · Las Montañas de la Luna", "Fort Portal → Kasese → Rwenzori (Central Circuit o Kilembe)", "~80 km · 2 días, o 7-9 si se hace la travesía"),
        ("13 · Kazinga y los cráteres", "Kasese → Katwe (salinas) → Queen Elizabeth y crucero por el canal", "~120 km · 3 días"),
        ("14 · Leones en los árboles", "Kazinga → sector de Ishasha", "~110 km · 1-2 días"),
        ("15 · Los gorilas", "Ishasha → Bwindi (Buhoma o Rushaga/Nkuringo)", "~80-160 km según sector · 3 días"),
        ("16 · Volcanes y monos dorados", "Bwindi → Kisoro → Mgahinga (Sabyinyo o Muhabura a pie)", "~80 km · 2 días"),
        ("17 · Descanso en el lago", "Kisoro → lago Bunyonyi (Kabale)", "~80 km · 2-3 días de parada con el perro"),
        ("18 · Salida a Ruanda", "Bunyonyi/Kisoro → Cyanika o Katuna → Ruanda", "~30-50 km · 1 día"),
        ("Alt. · Salida a Tanzania", "Kabale → Mbarara → Lago Mburo → Mutukula", "~440 km · 3-4 días"),
    ],
    offroad=[
        "BUCLE DE LOS CRÁTERES DE FORT PORTAL (Ndali-Kasenda): la mejor pista 4x4 «de postal» del país. Decenas de kilómetros de tierra roja entre más de cincuenta lagos de cráter, plantaciones de té y bananeras, con miradores sobre los lagos Nkuruba, Nyinambuga y Lyantonde. Barro serio en época de lluvias (mar-may y sep-nov), fácil en seco.",
        "EXPLOSION CRATER DRIVE (Queen Elizabeth, entre Kazinga y Katwe): pista de 27 km por el borde de un campo de cráteres volcánicos jóvenes, con vistas al lago Edward y a los Rwenzori al fondo cuando el cielo está limpio. Es el recorrido con mejores panorámicas del parque.",
        "GULU → KITGUM → KIDEPO: el tramo 4x4 largo del país. Murram (laterita) durante cientos de kilómetros, con lavadero y baches profundos; en lluvias hay tramos que se ponen muy resbaladizos. Es el precio de llegar al parque más remoto de Uganda, y por eso está casi vacío.",
        "PISTA FINAL A BWINDI (Kabale → Ruhija → Buhoma, o Kisoro → Rushaga/Nkuringo): montaña pura, tierra empapada casi todo el año, pendientes fuertes y curvas cerradas sobre precipicio. 4x4 obligatorio de verdad, no recomendable. Reducir presiones y calcular el doble de tiempo que la distancia sugiere.",
        "SECTOR DE ISHASHA: pistas de arena y barro negro dentro del parque, con vados; el barro negro de algodón se vuelve intransitable tras la lluvia.",
        "PISTAS DE LOS VALLES DE NARUS Y KIDEPO: arena de lecho seco y vados; el valle de Kidepo solo es practicable en seco.",
        "ACCESO A SIPI Y AL MONTE ELGON: pistas de montaña desde Mbale con pendientes muy fuertes; en seco es fácil, en lluvias exige tracción real.",
    ],
    senderismo=[
        "PICO MARGHERITA (5.109 m), montes Rwenzori: el gran objetivo a pie del desvío y el tercer pico de África. Central Circuit de 7-9 días desde Nyakalengija, o ruta de Kilembe por el sur. ES EL ÚNICO DE LOS TRES GRANDES QUE EXIGE TÉCNICA: travesía de glaciar con cuerda, crampones y piolet en el tramo final. Guía y porteadores obligatorios por la Rwenzori Mountaineering Services o Rwenzori Trekking Services.",
        "Rwenzori sin cumbre: aunque no se suba al Margherita, los tres o cuatro primeros días del Central Circuit (hasta el valle del Bujuku o el Mubuku) atraviesan un bosque de brezos gigantes, lobelias de tres metros y senecios arborescentes cubiertos de musgo que es de los paisajes más extraños de África. Se puede hacer como trek corto de 3-4 días.",
        "PICO WAGAGAI (4.321 m), monte Elgon: 4-5 días por las rutas de Sasa (la más directa y dura), Piswa o Sipi, cruzando la caldera. Sin técnica, sin masificación y muchísimo más barato que el Kilimanjaro. Incluye las cuevas de sal (Kitum, Makingeny) a las que entran los elefantes.",
        "Sendero de las tres cataratas de Sipi: circuito de medio día que une los saltos de Sipi (95 m), Ngasire (85 m) y Simba (74 m) entre cafetales. Guía local barato y obligatorio en la práctica. Hay abseil comercial por la pared del salto grande.",
        "Monte Sabyinyo (3.669 m), Mgahinga: subida de un día por escaleras y pasamanos de madera hasta una cumbre donde se pisan a la vez Uganda, Ruanda y RD Congo. Una de las cumbres con mejor relación esfuerzo-recompensa de África oriental.",
        "Monte Muhabura (4.127 m), Mgahinga: cono perfecto, subida y bajada en un día largo y muy exigente (unas 8 horas), con un lago de cráter en la cima y vistas a toda la cadena de los Virunga.",
        "Seguimiento de rinocerontes A PIE en Ziwa: no es una caminata deportiva, pero es la única forma de acercarse a un rinoceronte blanco andando en toda la ruta. Una o dos horas con rastreadores.",
        "Pantano de Bigodi (junto a Kibale): paseo comunitario de 2-3 horas por pasarelas entre ocho especies de primates y más de 200 de aves. Proyecto gestionado por la asociación local KAFRED, barato y excelente.",
        "Sendero del picozapato en el delta del Nilo Victoria (Murchison) y en el pantano de Ziwa: caminata corta y de barro para buscar el ave más extraña de África.",
        "Batwa Trail (Mgahinga): recorrido guiado por los propios batwa expulsados del bosque en 1991, que enseñan cómo vivían dentro de él. Media jornada, con un componente cultural serio y no folclórico.",
        "Vuelta al lago Bunyonyi por las colinas aterrazadas y subida al mirador de Arcadia Lodge: caminatas de medio día, fresco de altura, sin mosquitos y PERFECTAS PARA HACER CON EL PERRO.",
        "Safari a pie con ranger en el Lago Mburo: el único parque del país donde se permite caminar entre cebras, elands e impalas, por no haber leones.",
    ],
    acampada=[
        "Jinja: varios campings a orillas del Nilo orientados a overlanders (zona de Bujagali), con parcela para vehículo, duchas y agua. De los mejores sitios del país para parar y arreglar cosas.",
        "Entebbe: alojamientos y campings junto al lago, mucho más tranquilos que Kampala y mejores para el perro.",
        "Sipi: campings en la ladera con vistas directas al salto principal; frescos por la altura.",
        "Ziwa Rhino Sanctuary: tiene campsite propio dentro de la finca, con restaurante — se duerme dentro y se hace el seguimiento a primera hora.",
        "Murchison Falls (Paraa) y Kidepo (Apoka): campsites del UWA dentro del parque, básicos, con fauna suelta alrededor. En Murchison hay opciones fuera de puerta en Masindi para las noches con perro.",
        "Fort Portal y los lagos de cráter: campings a orillas de los cráteres (zona de Kasenda/Nkuruba), con baño en agua sin bilharzia. Uno de los mejores sitios del país para acampar.",
        "Lago Bunyonyi: campings en la orilla y en las islas; la base natural para los días de gorilas, con el perro.",
        "Kisoro y Buhoma: lodges y campamentos junto a las puertas de Mgahinga y Bwindi, varios con parcela para vehículo propio.",
    ],
    visado=[
        "eVISA OBLIGATORIA para españoles: se tramita online en visas.immigration.go.ug ANTES de viajar, con pasaporte (validez mínima 6 meses), foto, certificado de fiebre amarilla y justificante de alojamiento. Uganda no es un país de visado en ventanilla.",
        "CRITERIO DEL DUEÑO — VÁLIDA POR TIERRA: sí. A diferencia del caso de Gabón (eVisa solo para entrada aérea), la eVisa ugandesa se acepta en los puestos terrestres de Malaba, Busia, Cyanika, Katuna y Mutukula. La condición que el dueño puso para considerar el desvío SE CUMPLE.",
        "Hay que presentar la confirmación de la eVisa IMPRESA en papel en el puesto fronterizo; el visado físico se sella allí. No basta con la pantalla del móvil.",
        "Visado ordinario de turista: 50 USD, entrada única, 90 días. Confirmar tarifa vigente al tramitar.",
        "VISADO TURÍSTICO DE ÁFRICA ORIENTAL (EATV): 100 USD, 90 días, entradas múltiples entre KENIA, UGANDA y RUANDA. Debe usarse por primera vez en el país que lo emite. Si se hacen los tres países (que es exactamente el escenario de este desvío), sale más barato y evita tres trámites: estudiarlo en serio.",
        "Certificado internacional de fiebre amarilla EXIGIDO en frontera y comprobado de verdad en los pasos terrestres.",
    ],
    fronteras_rows=[
        ("Entrada (principal)", "Malaba (Kenia)", "Corredor Norte, OSBP de ventanilla única. Mucho camión y esperas variables: llegar temprano. eVisa impresa + fiebre amarilla + CPD."),
        ("Entrada (alternativa)", "Busia (Kenia)", "OSBP menos congestionado de camiones y habitualmente más rápido para turismo. Enlaza igual de bien con Jinja."),
        ("Salida a Ruanda (preferente)", "Cyanika", "Kisoro → Musanze. Es la salida natural si se encadena Mgahinga con el Parque de los Volcanes: 25 km entre los dos parques. Puesto pequeño, HORARIO LIMITADO: confirmar antes de llegar."),
        ("Salida a Ruanda (alternativa)", "Katuna / Gatuna", "Kabale → Kigali, carretera troncal con mejor asfalto. ESTUVO CERRADO 2019-2022 por la crisis Ruanda-Uganda: confirmar estado 72 h antes."),
        ("Salida a Tanzania", "Mutukula", "Si no se sigue a Ruanda: hacia Bukoba y el oeste del lago Victoria. Cae bien tras el Lago Mburo. Coordenadas y horario por confirmar."),
        ("NO utilizable", "Frontera con RD Congo (Bunagana, Mpondwe, Ishasha)", "Grupos armados activos en el lado congoleño. Fuera de cualquier variante."),
    ],
    vehiculos=[
        "CPD (Carnet de Passages en Douane) exigido en la práctica en frontera terrestre; con CPD el trámite es rápido. Sin él, permiso temporal de importación con depósito.",
        "Seguro de terceros COMESA (tarjeta amarilla) válido en Uganda como miembro de la región: si se compró en Kenia, cubre. Verificar que el certificado incluya Uganda entre los países.",
        "Tasa de carretera / road user charge en frontera para vehículos extranjeros: presupuestar unos 20-25 USD por vehículo, por confirmar el importe vigente.",
        "Carné de conducir internacional obligatorio junto con el nacional.",
        "Se conduce por la IZQUIERDA, igual que en Kenia y Tanzania. Los boda-boda (mototaxis) son el mayor riesgo de la conducción urbana.",
        "Triángulos, extintor y chaleco reflectante: controles frecuentes de la policía de tráfico en las carreteras principales.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autorización previa de la Uganda Civil Aviation Authority (UCAA) obligatoria para cualquier vuelo, incluido el recreativo. Proceso lento y poco predecible.",
        "Hay casos documentados de RETENCIÓN DEL DRON EN ADUANA a la entrada, con devolución a la salida del país, cuando no se lleva permiso previo. Declararlo en frontera y llevar factura.",
        "Dentro de los parques de la Uganda Wildlife Authority (Bwindi, Mgahinga, Queen Elizabeth, Murchison, Kidepo) el vuelo está prohibido salvo autorización expresa del UWA, que en la práctica no se concede a particulares.",
        "Norma del proyecto para Uganda: NO volar. Si aun así se quiere intentar, iniciar el trámite con 3-4 meses de antelación.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo desde 2023 con cobertura en todo el país; es el mejor respaldo para el norte (Gulu, Kidepo) y el suroeste (Kabale, Kisoro, Bwindi).",
        "SIM local de MTN Uganda o Airtel Uganda como respaldo: buena en el eje Kampala-Jinja-Mbarara, aceptable en el suroeste, intermitente en Kidepo y dentro de los parques.",
        "Confirmar 30-60 días antes que no haya pausas de altas nuevas, como ha ocurrido en Kenia por sobrecarga de red.",
    ],
    perro_intro=[
        "Permiso de importación previo del MAAIF (Ministry of Agriculture, Animal Industry and Fisheries), Commissioner for Animal Health, Entebbe — según el dosier del proyecto, entrada terrestre PROBABLE pero sin confirmación escrita todavía.",
        "Certificado veterinario internacional reciente, vacuna antirrábica en vigor y desparasitación; documentación en inglés.",
        "Nombrar EXPLÍCITAMENTE el puesto terrestre (Malaba o Busia) en la solicitud del permiso, como marca el criterio general del dosier canino: el error fatal no es cruzar por tierra, es llegar a un puesto terrestre con un permiso que nombra el aeropuerto de Entebbe.",
        "Kampala y Entebbe tienen veterinarios de buen nivel y residencias caninas: son la base para los días de parque.",
        "AVISO SANITARIO ESPECÍFICO: existe literatura publicada sobre tripanosomiasis canina en la zona de Bwindi-Mgahinga y Queen Elizabeth. El suroeste ugandés es zona de mosca tsetse y de riesgo alto para el perro, no solo zona de prohibición administrativa.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria en casi todo el país y durante todo el año: profilaxis a valorar con Sanidad Exterior. Excepciones por altitud: Kabale, Bunyonyi, Kisoro y las cumbres del Rwenzori y el Elgon.",
        "Fiebre amarilla: certificado internacional exigido en frontera y comprobado de verdad en los pasos terrestres.",
        "BILHARZIA (esquistosomiasis) en gran parte de la orilla del lago Victoria y del lago Alberto: no bañarse en el Victoria ni dejar que el perro beba en la orilla. Los lagos de cráter de Fort Portal y el Bunyonyi se consideran seguros, pero conviene confirmarlo en el momento.",
        "Mosca tsetse (tripanosomiasis) en el suroeste y el oeste: ropa cubierta, evitar azul y negro, repelente. Riesgo también para el perro.",
        "Ébola y Marburgo: Uganda ha tenido brotes localizados y breves en varias ocasiones (el último de Sudan ebolavirus en 2022-2023). No es un riesgo del viaje, pero SÍ puede cerrar distritos y fronteras de un día para otro: consultar el estado epidemiológico antes de entrar.",
        "Altitud: el Rwenzori y el Elgon superan los 4.000 m. Aclimatación real, no simbólica, y plan de descenso.",
        "International Hospital Kampala (privado) y Mulago National Referral Hospital como referencias; evacuación a Nairobi para casos serios. Comprobar que el seguro cubre la evacuación desde el interior del país.",
    ],
    seguridad_intro=("Uganda es un país tranquilo para viajar en su eje turístico y el nivel de delincuencia contra viajeros es bajo, pero tiene dos periferias que condicionan la ruta: la frontera occidental con RD Congo, que no se toca, "
                     "y el noreste de Karamoja, que exige informarse sobre el terreno. El resto es precaución normal, con el tráfico como mayor riesgo real."),
    seguridad=[
        "FRONTERA OCCIDENTAL CON RD CONGO: grupos armados activos en el lado congoleño (ADF y otros) en el entorno de Bunagana, Mpondwe y el norte del Rwenzori. No cruzar bajo ningún concepto y no acampar pegado a la línea en el sector de Ishasha.",
        "Karamoja y el camino a Kidepo (Gulu-Kitgum-Kaabong): historial de robo de ganado armado entre comunidades. Hoy es transitable, pero conviene informarse en Gulu y Kitgum, viajar siempre de día y no improvisar rutas alternativas.",
        "Evitar manifestaciones y concentraciones políticas, especialmente en periodo electoral: las protestas se disuelven con contundencia y las comunicaciones pueden cortarse.",
        "Tráfico: el mayor riesgo real del país. Boda-bodas por todas partes, camiones lentos en las cuestas y ausencia de arcén. No conducir de noche fuera de ciudad, criterio general del proyecto.",
        "En el trekking de gorilas, seguir al pie de la letra las instrucciones del guía: distancia mínima de 7-10 m, mascarilla obligatoria y prohibición de acercarse si se tienen síntomas de resfriado. No es una formalidad: es la razón por la que quedan gorilas.",
        "Aparcamiento vigilado en Kampala; prudencia estándar contra el hurto en mercados (Owino) y estaciones de taxi.",
        "Legislación LGTBI: Uganda aprobó en 2023 una de las leyes antihomosexualidad más severas del mundo. No afecta a la seguridad de este grupo de viajeros, pero es un dato que conviene conocer antes de decidir el desvío.",
    ],
    agua=[
        "Kampala, Entebbe, Jinja, Mbale, Gulu, Fort Portal, Mbarara y Kabale: agua embotellada sin problema en supermercados.",
        "Recarga del depósito de uso general: campings de Jinja (Bujagali), Entebbe, Fort Portal, Bunyonyi y Buhoma permiten llenar con manguera; confirmar en recepción.",
        "Bucle norte (Gulu-Kitgum-Kidepo): cargar a tope en Gulu. En Kidepo el agua del campsite de Apoka es limitada y conviene no depender de ella.",
        "NO tomar agua de la orilla del lago Victoria ni del lago Alberto por bilharzia, ni siquiera filtrada para uso general sin tratar. Los lagos de cráter de Fort Portal y el Bunyonyi son mucho más seguros.",
    ],
    combustible=[
        "Eje principal sin problemas: Malaba/Busia → Mbale (~80 km) → Jinja (~150 km) → Kampala (~80 km) → Mbarara (~270 km) → Kabale (~140 km) → Kisoro (~80 km). Todas con estaciones formales.",
        "Eje oeste: Kampala → Fort Portal (~300 km) → Kasese (~75 km) → Katunguru (~60 km) → Ishasha (~110 km), con estaciones en Fort Portal, Kasese y Rukungiri. Repostar en Kasese antes del sector de Ishasha.",
        "TRAMO CRÍTICO — bucle norte: repostar a fondo en GULU antes de Kitgum y Kidepo. Entre Kitgum y Kidepo (~200 km) no hay estación fiable y en Kidepo no hay surtidor: hay que entrar y salir con autonomía completa y garrafas.",
        "Repostar a fondo también en KABALE o KISORO antes del tramo final de montaña a Bwindi: las pistas consumen mucho más de lo que sugiere la distancia.",
        "Sin gaps de 500 km en ningún tramo del eje principal: el problema de Uganda no es la distancia entre gasolineras, es el estado de la pista.",
    ],
    experiencias_intro=("Relatos y datos recogidos de la comunidad overland y de fuentes especializadas. No son información oficial: contrastar siempre la fecha antes de confiar en un dato de frontera, pista o parque. "
                        "En esta revisión no se ha podido acceder a iOverlander ni a Tracks4Africa desde la sesión de trabajo, así que lo que sigue procede de fuentes documentales y del dosier canino del propio proyecto, y está marcado como tal:"),
    experiencias=[
        "El permiso manda sobre la ruta: quien ha hecho Bwindi coincide en que lo primero no es planificar el camino, es conseguir el permiso — y como el permiso se asigna a UN SECTOR concreto (Buhoma, Ruhija, Rushaga o Nkuringo), es el permiso el que decide por dónde se entra al parque y por dónde se sale. Reservar primero, trazar después.",
        "Uganda frente a Ruanda, la comparación que todo el mundo hace: el mismo animal, en el mismo macizo volcánico, a 800 USD en Uganda y 1.500 USD en Ruanda. A cambio, en Ruanda la caminata suele ser más corta y la carretera de acceso mucho mejor; en Uganda el bosque es más selvático, más barro y más horas de camino. Para tres personas la diferencia son 2.100 USD: si se hacen los dos países, el trekking se hace en Uganda.",
        "Mgahinga es el as en la manga: tiene un grupo de gorilas (el Nyakagezi) y permisos que se agotan mucho menos que los de Bwindi, además de los monos dorados, bastante más baratos. Si Bwindi está lleno en las fechas que toquen, Mgahinga salva el desvío — con el aviso de que el grupo Nyakagezi ha cruzado alguna vez a Ruanda y el trekking puede cancelarse.",
        "Las pistas engañan con la distancia: en el suroeste y en el norte hay que contar con medias de 25-35 km/h de verdad. Tramos como Kabale-Ruhija-Buhoma o Kitgum-Kidepo se planifican por horas, no por kilómetros, y se doblan en temporada de lluvias (mar-may y sep-nov).",
        "Kidepo tiene fama entre los overlanders de ser el mejor parque de Uganda precisamente porque casi nadie llega: 520 km desde Kampala y el último tramo de murram. Quien lo hace lo describe como un Serengeti vacío rodeado de montañas.",
        "Jinja es la parada de mantenimiento favorita del eje: campings a orillas del Nilo pensados para vehículos de expedición, con espacio para trabajar en el coche, y una oferta de actividades (rafting clase V, puenting) que hace que la gente se quede más días de los previstos.",
        "El crucero del canal de Kazinga aparece sistemáticamente como la mejor relación calidad-precio del país: dos horas de barca con la mayor concentración de hipopótamos de África y elefantes bajando a beber, por una fracción de lo que cuesta cualquier permiso de primate.",
        "Perro (dosier del proyecto): entrada terrestre PROBABLE con permiso del MAAIF/Commissioner for Animal Health de Entebbe, y buenos veterinarios en Kampala. El aviso serio es sanitario: hay estudio publicado de tripanosomiasis canina en Bwindi-Mgahinga y Queen Elizabeth, o sea que el suroeste es zona de riesgo alto para el animal.",
        "Drones: la experiencia repetida de viajeros es que el aparato se queda retenido en aduana a la entrada si no se lleva permiso previo de la UCAA, y se devuelve al salir. Merece la pena declararlo y asumir que en Uganda no se vuela.",
        "Rwenzori, el aviso de quien lo ha hecho: no es el Kilimanjaro. Llueve prácticamente todos los días, se camina sobre barro profundo y tramos de turbera durante días, y el tramo de cumbre exige glaciar. Mucha gente hace solo los 3-4 primeros días por el bosque de brezos gigantes y vuelve encantada.",
    ],
    pendientes=[
        ("DECISIÓN DE FONDO", "Decidir si el desvío entra: cuesta +2.400 km y 18-24 días en versión completa, o +1.300 km y 9-11 días en versión corta (solo suroeste y gorilas). Se decide con el calendario real en la mano al llegar a Kenia"),
        ("Permiso de gorilas: el gasto", "Confirmar con la UWA la tarifa vigente para 2027 (800 USD/persona en la última subida conocida, de julio de 2024) y decidir si van los tres viajeros o solo parte. Tres permisos son 2.400 USD"),
        ("Reserva del permiso y sector", "Si se decide hacerlo, reservar con varios meses de antelación y ELEGIR SECTOR (Buhoma, Ruhija, Rushaga o Nkuringo): el sector determina el trazado de entrada y salida del parque"),
        ("Uganda o Ruanda para los gorilas", "Decisión conjunta con la ficha de Ruanda: 800 USD frente a 1.500 USD por el mismo animal. Recomendación de esta ficha: trekking en Uganda, y Ruanda para Nyungwe, Kivu y Kigali"),
        ("Visado Turístico de África Oriental", "Comparar el EATV (100 USD, 90 días, Kenia+Uganda+Ruanda) con tres visados sueltos, y comprobar que se puede emitir en el país correcto según el orden de entrada"),
        ("Perro · permiso de importación", "Escribir al MAAIF / Commissioner for Animal Health (Entebbe) pidiendo confirmación escrita de entrada terrestre y NOMBRANDO el puesto (Malaba o Busia). Sigue en [PROBABLE] en el dosier canino"),
        ("Perro · base durante los parques", "Reservar residencia o cuidador en Kisoro, Kabale/Bunyonyi o Kampala para los bloques de Bwindi, QENP y Murchison, y organizar los turnos entre los tres viajeros"),
        ("Frontera de Katuna", "Confirmar 72 h antes que sigue abierta (cerró entre 2019 y 2022) y tener Cyanika como plan B; comprobar también el horario de Cyanika, que no es 24 h"),
        ("Rwenzori", "Decidir si se hace la travesía (7-9 días con glaciar y material técnico) o solo el tramo de bosque de 3-4 días, y quién se queda con el perro y los vehículos"),
        ("Kidepo", "Decidir si compensa el bucle de 1.100 km ida y vuelta desde Kampala, y revalidar la seguridad de Karamoja poco antes"),
        ("Dron", "Decidir si se solicita permiso a la UCAA con 3-4 meses de antelación o se asume no volar y se declara el aparato en frontera"),
        ("FOTOGRAFÍAS", "En esta revisión NO se pudo acceder a commons.wikimedia.org desde la sesión (bloqueo de red), así que solo dos PDIs llevan foto verificada. Pendiente: completar los nombres de archivo de Wikimedia Commons de los 18 PDIs restantes, verificándolos uno a uno. No inventarlos"),
        ("Estado epidemiológico", "Consultar brotes de ébola/Marburgo antes de entrar: pueden cerrar distritos y fronteras con muy poco aviso"),
    ],
    sources=SOURCES,
    sources_note=("Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. "
                  "UGANDA ES UNA ALTERNATIVA: no está en la ruta fija y solo entra si sobra tiempo tras Kenia. Las tarifas de permisos y visados son las últimas conocidas y hay que revalidarlas con la UWA y con Inmigración antes de comprometer nada."),
    emergency="Sin representación española propia en Uganda — gestionar emergencias a través de la Embajada de España en Nairobi (Kenia), competente para el país: +254 20 272 02 22/3/4/5; emergencia consular +254 733 63 11 44. Emergencias locales: policía 999 / 112, ambulancia 911.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

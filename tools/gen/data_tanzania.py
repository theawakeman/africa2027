# -*- coding: utf-8 -*-
"""Tanzania — ficha completa, corredor doble interior/costa (11 sep 2026).

Tanzania se cruza DOS VECES en el bucle:
  · corridor      = "Subida por el interior": Tunduma/Nakonde (Zambia) -> Namanga (Kenia)
  · corridor_alt  = "Bajada por la costa":    Horohoro/Lunga Lunga (Kenia) -> Mtwara (Mozambique)
"""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ==================================================================================
    # CORREDOR 1 — SUBIDA POR EL INTERIOR (Tunduma/Nakonde -> Namanga)
    # ==================================================================================
    dict(n=1, name="Lago Ngozi · cráter de los Poroto", cat="Naturaleza", prio="Alta", dog="permitido con correa", time="½–1 día",
         lat=-9.0081, lon=33.5531,
         desc="Lago de caldera a unos 30 km al sur de Mbeya, camino de Tukuyu, en los montes Poroto: 3,1 km² de agua verde encajada a 74 m de profundidad en un cráter de paredes forestadas, descrito como el segundo mayor lago de cráter de África. Se llega por la carretera de Tukuyu y una pista corta, y se sube caminando media hora entre bosque de montaña hasta el borde, con un descenso empinado opcional hasta la orilla (las paredes tienen cortados y desprendimientos: no todo el perímetro es accesible). Primera parada natural del país al entrar desde Zambia y un sitio excelente con el perro porque está FUERA de cualquier parque nacional. Imagen: paisaje de referencia de las Tierras Altas del Sur, no del propio lago — pendiente de sustituir.",
         credit="Wikimedia Commons", source=W + "Southern%20Highlands%20(Tanzania)%20banner.jpg?width=900"),
    dict(n=2, name="Parque Nacional de Kitulo · el «Serengeti de las flores»", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 días",
         lat=-9.0500, lon=33.8333,
         desc="412 km² de pradera de altura a unos 2.600 m entre los montes Kipengere, Poroto y Livingstone, que los vecinos llaman «Bustani ya Mungu» (el jardín de Dios) y los botánicos el Serengeti de las flores: unas 350 especies de flores silvestres, entre ellas 45 orquídeas endémicas que no existen en ningún otro lugar del mundo. Es el único parque nacional de África tropical creado principalmente por su flora, y uno de los pocos donde se camina libremente en lugar de conducir. Floración de noviembre a abril; septiembre-noviembre es soleado y bueno para andar; junio-agosto es frío y con niebla. A 70-110 km de Mbeya. Tasa TANAPA baja (35,40 USD/persona).",
         credit="Wikimedia Commons", source=W + "Kitulo%20National%20Park%20Entry.JPG?width=900"),
    dict(n=3, name="Parque Nacional de Katavi (el oeste salvaje)", cat="Naturaleza", prio="Media", dog="prohibido", time="2–3 días",
         lat=-6.8833, lon=31.1667,
         desc="Tercer parque más grande del país y uno de los menos visitados de África: llanuras inundables del Katuma con concentraciones enormes de búfalo e hipopótamo en la estación seca, cuando los ríos se reducen a pozas. Apenas recibe visitantes porque está a 1.000 km de Arusha, en el camino de tierra del oeste (Sumbawanga–Mpanda). Tasa TANAPA baja (35,40 USD/persona), pero hay moscas tsé-tsé: se controlan con banderas azules y negras impregnadas, y es un factor serio a valorar con el perro incluso fuera del parque. Puerta y poblado de servicios en Sitalike. Solo temporada seca. Imagen: construcción tradicional en Katavi, no vista de fauna.",
         credit="Wikimedia Commons", source=W + "Nyumba%20ya%20makuti%2C%20Katavi%20Tanzania.jpg?width=900"),
    dict(n=4, name="Kigoma y Ujiji · «Dr. Livingstone, I presume?»", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-4.8769, lon=29.6267,
         desc="Puerto principal de Tanzania en el lago Tanganyika, con la estación término del ferrocarril central alemán y el histórico vapor MV Liemba (botado en 1913 como Graf von Götzen, desmontado y transportado a lomos desde la costa, y todavía en servicio). A 8 km al sur está UJIJI, el lugar donde en noviembre de 1871 Henry Morton Stanley encontró a David Livingstone y pronunció la frase más famosa de la historia de la exploración africana; hay un monumento y un pequeño museo bajo un mango plantado como esqueje del original. Jakobsen Beach, a las puertas de la ciudad, es el camping de referencia de los overlanders en el lago: agua transparente a 26 °C. Base para Gombe y Mahale. Imagen: barco histórico en el lago Tanganyika.",
         credit="Wikimedia Commons", source=W + "Oldest%20ship%20in%20lake%20Tanganyika.jpg?width=900"),
    dict(n=5, name="Mahale Mountains y Gombe Stream · chimpancés", cat="Naturaleza", prio="Alta", dog="prohibido", time="3–4 días",
         lat=-6.1000, lon=29.7667,
         desc="Los dos parques de chimpancés del lago Tanganyika, accesibles SOLO EN BARCO (no hay carretera hasta las puertas). Mahale, sobre la ladera selvática que cae al lago, alberga el mayor grupo de chimpancés protegido del mundo y una población estudiada desde los años 60 por investigadores japoneses; Gombe, más al norte junto a Kigoma, es donde Jane Goodall empezó en 1960 el estudio de primates más largo de la historia. Tasas TANAPA altas: Gombe 118 USD/persona y Mahale 94,40 USD/persona, a las que hay que sumar el barco desde Kigoma (caro y lento: Mahale está a unos 120 km al sur). Decisión de presupuesto y de días: son los dos puntos más caros y más lentos de todo el corredor interior. Imagen: chimpancés en Gombe.",
         credit="Wikimedia Commons", source=W + "Gombe%20Stream%20NP%20gegenseitiges%20Lausen.jpg?width=900"),
    dict(n=6, name="Parque Nacional de Ruaha (el mayor del país)", cat="Naturaleza", prio="Alta", dog="prohibido", time="3–4 días",
         lat=-7.6833, lon=34.8167,
         desc="Unos 20.000 km² (más de 30.000 con los humedales anexionados), el parque nacional más grande de Tanzania y de África oriental, en la transición entre la sabana de acacias del este y el bosque de miombo del sur: una de las mayores poblaciones de elefante del continente, manadas de leones enormes, perro salvaje africano, kudú mayor y menor en el mismo sitio, y el río Ruaha con sus pozas en la seca. Mucho menos masificado que el circuito norte y con tasa TANAPA baja (35,40 USD/persona), lo que lo convierte en la mejor relación calidad-precio de safari del país. Puerta y sede en Msembe, a unos 130 km de Iringa por pista.",
         credit="Wikimedia Commons", source=W + "Ruaha%20National%20Park%20Panorama.jpg?width=900"),
    dict(n=7, name="Udzungwa Mountains · cascadas de Sanje", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 días",
         lat=-7.8436, lon=36.8833,
         desc="El parque de senderismo de Tanzania: no hay pistas de safari, se recorre solo a pie. Parte del Arco Oriental, un archipiélago de bosques de montaña aislados con un nivel de endemismo comparable al de las Galápagos (dos especies de mono descritas aquí por primera vez, el colobo rojo de Iringa y el mangabey de Sanje). La excursión clásica es la de las CASCADAS DE SANJE, 170 m de salto en tres niveles, con una poza para bañarse a media altura; 5-6 horas ida y vuelta con guía obligatorio desde la puerta de Mang'ula. Más largas: las cataratas del príncipe Bernhard y la travesía de 2 días a la meseta de Mwanihana. Tasa baja (35,40 USD/persona). A 30 km del cruce de Mikumi, así que encaja con una visita corta al Parque Nacional de Mikumi (misma tarifa), el más accesible del sur.",
         credit="Wikimedia Commons", source=W + "Waterfall%20on%20Sanje%20Falls%20trail%20at%20Udzungwa%20Mountains%20National%20Park.jpg?width=900"),
    dict(n=8, name="Isimila · yacimiento de la Edad de Piedra e Iringa", cat="Cultura", prio="Media", dog="permitido", time="½ día",
         lat=-7.9167, lon=35.6000,
         desc="A unos 20 km al suroeste de Iringa, una garganta de erosión donde hace unos 60.000-100.000 años hubo una laguna somera en cuyas orillas se acumularon miles de herramientas achelenses de piedra (hachas de mano, raederas) junto a huesos de hipopótamo de patas cortas y de un jirafoide extinto de cuello corto: uno de los yacimientos de la Edad de Piedra mejor conservados de África oriental. Hoy la erosión ha esculpido además un bosque de PILARES DE ARENISCA de hasta 10 m que se recorre a pie en un par de horas. Hay museo pequeño y guía local. Iringa, a 1.600 m sobre el Ruaha, es la base logística del tramo sur (combustible, talleres, mercado) y tiene la roca de Gangilonga, donde el jefe hehe Mkwawa celebraba consejo antes de su guerra contra los alemanes.",
         credit="Wikimedia Commons", source=W + "Ismila-Stone-Age-Site-Tanzania.jpg?width=900"),
    dict(n=9, name="Parque Nacional de Tarangire · los baobabs", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 días",
         lat=-3.6833, lon=35.9667,
         desc="La puerta sur del circuito norte y el parque de los BAOBABS: bosques abiertos de estos árboles descomunales sobre el valle del río Tarangire, que en la estación seca (julio-octubre) concentra la mayor densidad de elefantes de Tanzania y unas concentraciones de fauna que se han comparado con las del Serengeti. También termiteros gigantes, pitones en los árboles y más de 550 especies de aves. Tasa TANAPA media (59 USD/persona). Es el parque del circuito norte más barato y el más fácil de autoconducir, y por eso el mejor candidato si hay que recortar días de safari.",
         credit="Wikimedia Commons", source=W + "Baobab%20tree%2C%20Tarangire%20National%20Park%20(4)%20(28062313514).jpg?width=900"),
    dict(n=10, name="Parque Nacional del lago Manyara", cat="Naturaleza", prio="Media", dog="prohibido", time="1 día",
         lat=-3.5833, lon=35.8250,
         desc="Franja estrecha de 330 km² entre el escarpe del Rift y un lago alcalino somero, al pie de la subida a Ngorongoro: bosque de acuíferos con manantiales, babuinos en bandadas enormes, los célebres LEONES TREPADORES DE ÁRBOLES (aquí es donde se documentó el comportamiento), hipopótamos y miles de flamencos y pelícanos en la orilla. Es el parque más compacto del circuito norte: se ve en medio día desde Mto wa Mbu, con tasa de 59 USD/persona. También tiene una pasarela de copas de árboles (treetop walkway) y safaris nocturnos, poco habituales en TANAPA.",
         credit="Wikimedia Commons", source=W + "Sleeping%20lion%202%2C%20Lake%20Manyara%20National%20Park%20(2015).jpg?width=900"),
    dict(n=11, name="Cráter del Ngorongoro", cat="Patrimonio UNESCO", prio="Alta", dog="prohibido", time="1–2 noches",
         lat=-3.2000, lon=35.5000,
         desc="Caldera volcánica de 20 km de diámetro y 600 m de paredes, Patrimonio de la Humanidad y el recinto natural de fauna más denso de África: los «Big Five» en 260 km², con una de las poblaciones de rinoceronte negro más accesibles del continente. No es un parque TANAPA sino un Área de Conservación (NCAA) gestionada junto a los masái, que siguen pastoreando dentro. ES EL PUNTO MÁS CARO DE TODO EL VIAJE: 70,80 USD/persona/24 h de entrada, tasa de vehículo extranjero por peso (177 USD para 2.001-3.000 kg, 236 USD para 3.001-7.000 kg), TASA DE DESCENSO AL CRÁTER de 295 USD por vehículo y ranger obligatorio de 40 USD en efectivo. Un solo día de cráter con 3 personas y un vehículo pasa fácilmente de 700 USD. Ver las alertas.",
         credit="Arnold Tibaijuka · CC BY-SA 4.0", source=W + "Wide%20aerial%20landscape%20of%20the%20Ngorongoro%20ecosystem.jpg?width=900"),
    dict(n=12, name="Garganta de Olduvai (Oldupai)", cat="Cultura", prio="Alta", dog="prohibido", time="½ día",
         lat=-2.9917, lon=35.3500,
         desc="Barranco de 48 km dentro del Área de Conservación del Ngorongoro, en el camino entre el cráter y el Serengeti, que es probablemente el yacimiento paleoantropológico más importante del mundo: aquí Mary y Louis Leakey encontraron en 1959 el cráneo de Paranthropus boisei y después los restos que dieron nombre al Homo habilis, además de la industria lítica olduvayense, la más antigua reconocida. A 45 km están las huellas de Laetoli, de 3,6 millones de años. Hay un museo reconstruido en 2017 sobre el borde de la garganta y visitas guiadas a pie al fondo. La entrada se cobra aparte de la tasa del Ngorongoro: confirmar importe al entrar por la puerta de Loduare.",
         credit="Wikimedia Commons", source=W + "Panoramic%20view%20of%20Olduvai%20Gorge.jpg?width=900"),
    dict(n=13, name="Parque Nacional del Serengeti", cat="Patrimonio UNESCO", prio="Alta", dog="prohibido", time="3–4 días",
         lat=-2.4333, lon=34.8333,
         desc="14.750 km² de llanura infinita interrumpida solo por los KOPJES, islas de granito donde se tumban los leones, y escenario de la GRAN MIGRACIÓN: unos 1,3 millones de ñus y cientos de miles de cebras y gacelas en un circuito anual que en enero-marzo pare en las llanuras cortas del sur (Ndutu), en mayo-junio cruza hacia el oeste y en julio-septiembre salta el río Mara hacia Kenia. Patrimonio de la Humanidad. Tasa TANAPA alta (82,60 USD/persona/día) más vehículo, y camping público de 35,40 USD/persona/noche: 3 personas y 3 noches dentro salen por encima de 1.000 USD solo en tasas. Autoconducción permitida; pistas de grava corrugada y roca donde rara vez se pasa de 25-40 km/h.",
         credit="Wikimedia Commons", source=W + "Kopjes%20on%20the%20serengeti%20national%20park%20tanzania%20africa%20landscape.jpg?width=900"),
    dict(n=14, name="Lago Natron y Engare Sero", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-2.4500, lon=36.0167,
         desc="Lago de sosa de un rojo imposible al pie del Rift, el ÚNICO LUGAR DE CRÍA REGULAR DEL FLAMENCO ENANO de toda África oriental (el 75 % de la población mundial nace aquí), con temperaturas del agua de hasta 60 °C y costras de natrón que matan a casi todo lo demás. No es parque nacional sino un Área de Gestión de Fauna comunitaria (WMA): se pagan tasas de aldea en Engare Sero, unos 35 USD entre varios conceptos más 11,80 USD de actividad y tasa de vehículo, y se acampa en campings comunitarios por 17-24 USD. Eso significa que EL PERRO NO ESTÁ SUJETO A LA PROHIBICIÓN DE TANAPA: es el mejor punto de fauna espectacular del corredor interior compatible con llevarlo. Además: la garganta y la cascada de Engare Sero, y las huellas humanas fósiles de Engare Sero (unas 400, de hace 5.000-19.000 años, el mayor conjunto de huellas de Homo sapiens de África). Calor extremo: planificar agua y sombra.",
         credit="Wikimedia Commons", source=W + "Lago%20natron.PNG?width=900"),
    dict(n=15, name="Ol Doinyo Lengai · la montaña de Dios (2.962 m)", cat="Naturaleza", prio="Alta", dog="prohibido en la ascensión", time="1–2 días",
         lat=-2.7642, lon=35.9142,
         desc="Volcán activo y sagrado para los masái, el ÚNICO DEL MUNDO que emite natrocarbonatita: una lava tan fría (500-600 °C) y fluida que de día parece barro negro y solo brilla de noche, y que al contacto con la humedad se vuelve blanca como la nieve. La ascensión es LA gran excursión nocturna de Tanzania: se sale hacia medianoche desde el pie, 1.600 m de desnivel en apenas 5 km (11,2 km ida y vuelta, unos 400 m de subida por kilómetro), 6-10 horas, sobre roca suelta y resbaladiza, para llegar al cráter al amanecer. Guía masái obligatorio, alrededor de 100 USD por persona según los relatos recientes, y 4x4 imprescindible para llegar al inicio. Una de las ascensiones más duras y más extraordinarias de África: no es un paseo, hay que ir en forma.",
         credit="Wikimedia Commons", source=W + "Ol%20Doinyo%20Lengai%20Crater.jpg?width=900"),
    dict(n=16, name="Arusha y el monte Meru (4.562 m)", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-3.3869, lon=36.6830,
         desc="Capital logística del norte y mejor plaza de servicios de todo el corredor interior: talleres y recambios de 4x4, neumáticos, supermercados grandes, clínicas privadas, tramitación de permisos de parque y la única oferta real de cuidado del perro del tramo (clínica y refugio Mbwa Wa Africa, en Usa River, a 25 km). Sobre la ciudad se levanta el MONTE MERU, segunda cumbre de Tanzania y quinta de África, un estratovolcán con un cráter de herradura abierto por un colapso: la ascensión son 3-4 días por el Parque Nacional de Arusha, con refugios, ranger armado obligatorio (hay búfalo y elefante en la base) y una cresta final espectacular sobre el cráter con el Kilimanjaro enfrente. Bastante más barata que el Kilimanjaro (tasa de parque de 59 USD/persona/día frente a 82,60) y, para mucha gente, más bonita.",
         credit="Khalidsalewa · CC BY-SA 4.0", source=W + "Mount%20meru%20with%20snow%2C%20Arusha%20Region%2C%20Tanzania.jpg?width=900"),
    dict(n=17, name="Kilimanjaro (5.895 m) · decisión de presupuesto", cat="Naturaleza", prio="Media", dog="prohibido", time="6–9 días si se sube",
         lat=-3.0674, lon=37.3556,
         desc="El techo de África y la montaña aislada más alta del planeta, a 80 km al este de Arusha. Subirlo NO es una excursión, es una expedición cara y reglada: guía y porteadores obligatorios por ley, 5-10 días según ruta (Marangu con refugios, Machame, Lemosho, Rongai, Umbwe), y tasas de parque de 70 USD/persona/día de conservación + 50 USD/persona/noche de acampada (o 60 en los refugios de Marangu) + 10 USD de tasa forestal + 20 USD de rescate, TODO con un 18 % de IVA encima. Solo en tasas de parque, una subida de 7 días ronda los 1.000-1.200 USD por persona, y el paquete completo con operador va de 2.500 a 5.500 USD por persona. Alternativas honestas: el monte Meru (3-4 días, mucho más barato), la caminata de un día a la puerta de Marangu y las cascadas, o la ruta de los pueblos chagga y las cuevas de Marangu, sin entrar al parque. DECISIÓN DEL DUEÑO: con 3 viajeros son 7.500-16.000 USD — es el gasto único más grande de todo el viaje africano.",
         credit="Wikimedia Commons", source=W + "Kibo%20Summit%2C%20Mount%20Kilimanjaro%2C%20Tanzania%20(30819102678).jpg?width=900"),
    # ==================================================================================
    # CORREDOR 2 — BAJADA POR LA COSTA (Horohoro/Lunga Lunga -> Mtwara)
    # ==================================================================================
    dict(n=18, name="Tanga y las cuevas de Amboni", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-5.0689, lon=39.0989,
         desc="Primera ciudad tras la frontera costera, a unos 60 km de Horohoro: puerto colonial alemán tranquilo, con el cementerio de guerra, la casa de Bagamoyo Road y un ritmo muy distinto al de Dar. A 8 km al norte están las CUEVAS DE AMBONI, el mayor sistema de cuevas de piedra caliza de África oriental —unos 234 km² de formación, de los que se visita un circuito guiado de cámaras y estalactitas— con una larga historia de uso como refugio (los Mau Mau kenianos se esconderían aquí, según la tradición local) y de culto: todavía se dejan ofrendas en algunas salas. A 8 km más, los MANANTIALES SULFUROSOS DE GALANOS, pozas termales de agua caliente en medio del bosque. Todo fuera de parque nacional: sitios compatibles con el perro.",
         credit="Wikimedia Commons", source=W + "Tanga%2C%20Tanzania%2C%20town%20centre.JPG?width=900"),
    dict(n=19, name="Montes Usambara occidentales (Lushoto)", cat="Naturaleza", prio="Alta", dog="permitido con correa", time="2–3 noches",
         lat=-4.7833, lon=38.2833,
         desc="Bloque de montaña del Arco Oriental que se eleva desde la sabana caliente hasta 2.000 m de bosque nuboso, con un clima fresco y niebla que los alemanes convirtieron en su sanatorio de altura. LA MEJOR ZONA DE SENDERISMO LIBRE DE TANZANIA: una red de caminos entre aldeas, plantaciones de té y bosque primario gestionada por programas de turismo cultural comunitario, con rutas de medio día (mirador de IRENTE, sobre un cortado de 1.000 m con toda la llanura de Mazinde a los pies) y travesías de 2-4 días de Lushoto a Mtae o Mambo, durmiendo en casas de huéspedes de pueblo. Fuera de parque nacional, así que el perro puede acompañar; camaleones endémicos, y bosque de Magamba para caminatas cortas. Base: Lushoto, a 32 km del desvío de Mombo en la carretera principal. Imagen: los Usambara desde la carretera de Korogwe.",
         credit="Wikimedia Commons", source=W + "Road%20to%20Korogwe%2C%20with%20the%20Usambara%20Mountains.%20Tanzania.jpg?width=900"),
    dict(n=20, name="Pangani y el Parque Nacional de Saadani", cat="Costa", prio="Media", dog="permitido con condiciones", time="2–3 noches",
         lat=-5.4264, lon=38.9803,
         desc="Pueblo suajili somnoliento en la desembocadura del río Pangani, con casas omaníes desconchadas, el antiguo boma alemán y la historia dura de haber sido terminal de una de las rutas de caravanas de esclavos y marfil; playas largas y vacías al norte y al sur, snorkel en la isla de Maziwe y un ferry local para cruzar el río. Al sur empieza el PARQUE NACIONAL DE SAADANI, el único de África oriental que da directamente al Índico: «donde el arbusto se encuentra con la playa», con elefantes y búfalos que bajan a la arena, delta del Wami con hipopótamos y cocodrilos, y tortugas verdes que desovan en la costa. Tasa TANAPA baja (35,40 USD/persona), acceso por pista (4x4 en lluvias), y se puede rodear por fuera si se viaja con el perro, durmiendo en la playa de Pangani. Imagen: calle de Pangani.",
         credit="Wikimedia Commons", source=W + "Street%20Scene%20in%20Pangani%20Mashariki%2001.jpg?width=900"),
    dict(n=21, name="Bagamoyo y las ruinas de Kaole", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-6.4400, lon=38.9000,
         desc="«Bwaga-moyo», deja aquí tu corazón: primera capital del África Oriental Alemana y el puerto donde terminaban las caravanas de esclavos y marfil del interior antes de embarcar hacia Zanzíbar. Conserva el boma alemán, la vieja aduana, la misión católica de 1868 —la más antigua de África oriental, con el museo donde reposó el cuerpo de Livingstone camino de Inglaterra— y un casco histórico degradado pero intensísimo. A 5 km, las RUINAS DE KAOLE: una ciudad suajili de los siglos XIII-XVI con dos mezquitas (una de las más antiguas de África oriental) y tumbas de pilar, mucho más tranquilas y atmosféricas que las de Zanzíbar. Estuvo en la lista indicativa de la UNESCO. Imagen: ruinas de Kaole.",
         credit="Wikimedia Commons", source=W + "Kaole%20Ruins%20in%20Bagamoyo%2C%20Tanzania.jpg?width=900"),
    dict(n=22, name="Dar es Salaam", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-6.7924, lon=39.2083,
         desc="Mayor ciudad y puerto del país y la plaza logística clave del corredor costero: embajada de España, talleres y recambios de todo tipo, Muhimbili como hospital de referencia nacional, supermercados grandes, y el puerto de donde salen los ferrys a Zanzíbar. Para nosotros es además el nudo de decisión del perro: es la única ciudad del corredor costero con veterinarios y opciones de cuidado, y la base natural si se decide dejarlo aquí durante Zanzíbar o Nyerere. El mercado de pescado de Kivukoni al amanecer, el Museo Nacional con los fósiles de Olduvai y el Village Museum son las paradas urbanas que merecen la pena. Repostar y revisar los dos vehículos aquí antes de la bajada al sur.",
         credit="Muhammad Mahdi Karim · GFDL", source=W + "Dar%20es%20Salaam%20City%20Skyline.jpg?width=900"),
    dict(n=23, name="Zanzíbar · Stone Town (decisión con perro)", cat="Patrimonio UNESCO", prio="Media", dog="no recomendado — ver matriz", time="3–4 días",
         lat=-6.1659, lon=39.1917,
         desc="Ciudad de piedra suajili-omaní, Patrimonio de la Humanidad: callejuelas imposibles, puertas de teca talladas, la Casa de las Maravillas, el mercado de esclavos sobre el que se construyó la catedral anglicana, y el archipiélago de especias y playas alrededor (Nungwi, Jambiani, Mnemba). Se llega en ferry rápido de pasajeros desde Dar (2 h) o embarcando el vehículo en un ferry de carga, que es otro trámite y otro precio. PUNTO DELICADO DEL PROYECTO: Zanzíbar es un territorio semiautónomo con su propio control de entrada (sellan el pasaporte aunque no sea frontera internacional), de población mayoritariamente musulmana donde el perro se percibe como animal impuro y es raro verlo suelto, con calor húmedo extremo y sin infraestructura veterinaria comparable a la de Dar. Nuestra recomendación: ir sin el vehículo y sin el perro, dejándolo con cuidador en Dar, o saltarse la isla. Ver la matriz canina.",
         credit="Kgbo · CC BY-SA 4.0", source=W + "Stone%20Town%2C%20Zanzibar%2C%202021%2C%2036.jpg?width=900"),
    dict(n=24, name="Parque Nacional de Nyerere (ex-Selous)", cat="Naturaleza", prio="Alta", dog="prohibido", time="3–4 días",
         lat=-7.7500, lon=37.9000,
         desc="30.893 km² segregados en 2019 de la antigua Reserva de Caza de Selous (que era, con 50.000 km², la mayor área protegida de África): hoy es EL PARQUE NACIONAL MÁS GRANDE DEL CONTINENTE. Lo define el río Rufiji, con un laberinto de lagos y canales que permite algo poco frecuente en Tanzania: SAFARI EN BARCA entre hipopótamos y cocodrilos, además de caminatas guiadas. Una de las mayores poblaciones de perro salvaje africano del mundo, elefantes, búfalos y el antílope nyala. Tasa TANAPA alta (82,60 USD/persona/día), igual que el Serengeti. Acceso desde Dar por Kibiti hasta la puerta de Mtemere (unos 250 km, últimos 80-100 km de pista) o por Morogoro hasta Matambwe. Autoconducción posible en seco. Imagen: elefantes en el Rufiji.",
         credit="Wikimedia Commons", source=W + "ElefantenAmRufiji.jpg?width=900"),
    dict(n=25, name="Kilwa Kisiwani y Songo Mnara", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-8.9578, lon=39.5206,
         desc="La mayor ciudad suajili de su tiempo: desde el siglo XI al XVI, Kilwa controló el comercio del oro de Zimbabue hacia el Índico, acuñó su propia moneda y deslumbró a Ibn Battuta, que en el siglo XIV la describió como una de las ciudades más hermosas del mundo, con más de 10.000 habitantes. Patrimonio de la Humanidad desde 1981. Hoy la isla tiene unos mil pescadores y, entre los baobabs, la GRAN MEZQUITA (la mezquita en pie más antigua de la costa suajili, con su bosque de columnas y cúpulas, conservada porque quedó sepultada por el sedimento), el palacio de Husuni Kubwa con su piscina octogonal, el fuerte portugués y un cementerio. La isla gemela de Songo Mnara está 8 km al sur. Se cruza en 20 minutos en dhow desde Kilwa Masoko, con permiso de la oficina de antigüedades y guía obligatorio; con marea baja hay que vadear barro. Kilwa Beach Lodge tiene camping en la playa por unos 10 USD/persona.",
         credit="Wikimedia Commons", source=W + "Great%20Mosque%20Kilwa%20Kisiwani%20Tanzania.jpg?width=900"),
    dict(n=26, name="Mtwara, Lindi y la meseta makonde", cat="Cultura", prio="Media", dog="permitido con condiciones", time="2–3 noches",
         lat=-10.2667, lon=40.1833,
         desc="El extremo sur del país y el último punto de Tanzania antes de Mozambique. Lindi y Mtwara son dos puertos tranquilos con arquitectura colonial alemana y portuguesa y playas casi vacías (Msimbati, en la reserva marina de la bahía de Mnazi, con arrecife y manglar). Tierra adentro se levanta la MESETA MAKONDE, un altiplano de escarpe sobre la llanura costera habitado por los makonde, los escultores más célebres de África: de aquí sale la talla en madera de ébano (mpingo) del estilo shetani, con las figuras retorcidas de espíritus que hoy se venden en medio mundo — se pueden ver los talleres en Mtwara y en los pueblos de la meseta. El yacimiento de Mikindani, antiguo puerto de esclavos con boma restaurado, queda a 10 km de Mtwara. Imagen: el escarpe de la meseta makonde.",
         credit="Wikimedia Commons", source=W + "Makonde%20Plateau%20escarpment.JPG?width=900"),
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
    # ---- Fronteras ----
    ("Frontera · Entrada interior — Tunduma/Nakonde (desde Zambia)", "Frontera", -9.3000, 32.7667,
     "El gran paso del corredor TANZAM y el más transitado del sur: puesto de ventanilla única (OSBP), mucho camión, colas largas y gestores informales. Llegar temprano, contar con varias horas y no perder de vista la documentación del vehículo. Aquí se tramitan el visado, el permiso temporal de importación del vehículo (TIP) o el sellado del CPD, la tasa de carretera (~25 USD/mes/vehículo según relatos de overlanders) y el seguro de terceros si no se lleva Tarjeta Amarilla COMESA válida."),
    ("Frontera · Salida interior — Namanga (hacia Kenia)", "Frontera", -2.5450, 36.7867,
     "Paso principal del corredor norte, junto al Parque de Amboseli, de alto tránsito turístico y bien equipado. Aviso: durante las protestas poselectorales de octubre-noviembre de 2025 este paso sufrió cierres y disturbios en el lado keniano; confirmar normalidad 72 h antes. Devolver el TIP y obtener el sello de salida del vehículo."),
    ("Frontera · Entrada costa — Horohoro/Lunga Lunga (desde Kenia)", "Frontera", -4.6000, 39.1054,
     "Paso COSTERO sobre la A14 Mombasa-Dar, distinto del de subida: puesto de ventanilla única moderno con funcionarios de los dos países en el mismo edificio, abierto 24 h, asfalto en buen estado en ambos lados, combustible a menos de 1 km y 4G. Tiempos de espera normales de 15-30 minutos; horas punta de 7 a 10 de la mañana y fines de semana. Nuevo TIP y nueva tasa de carretera al reentrar (ojo: hay relatos de cobros duplicados de la tasa de 25 USD en la reentrada — pedir justificante)."),
    ("Frontera · Salida costa (opción A) — Kilambo/Namoto, ferry del Rovuma", "Frontera", -10.4667, 40.4167,
     "ATENCIÓN, PUNTO CRÍTICO: NO es un puente, es un FERRY de barcaza sobre la desembocadura del río Rovuma, a unos 40 km de Mtwara, con capacidad para unos 6 vehículos 4x4. Horario del lado mozambiqueño 07:00-19:00 y del lado tanzano muy restringido (se cita 07:00-08:00); la salida depende de la MAREA (hace falta un mínimo de 3 m de agua) y puede implicar dormir esperando la marea siguiente. Además, el lado mozambiqueño (Quionga, Palma, Mocímboa da Praia, norte de Cabo Delgado) está bajo una insurgencia activa y las fuentes especializadas recomiendan expresamente NO usar este paso. Coordenada aproximada: confirmar."),
    ("Frontera · Salida costa (opción B) — Mtambaswala/Negomano, puente de la Unidad", "Frontera", -11.4144, 38.4942,
     "El verdadero PUENTE DE LA UNIDAD sobre el Rovuma, inaugurado el 12 de mayo de 2010: 720 m, 18 vanos, dos carriles. Pero NO está junto a Mtwara: está unos 180 km al interior, en Mtambaswala (lado tanzano) frente a Negomano (lado mozambiqueño), y se llega desde Masasi. Es la alternativa terrestre seria al ferry de Kilambo y deja en el norte de Niassa/Cabo Delgado occidental, más alejado de la zona de insurgencia costera. Confirmar 60 días antes que el puesto emite visado y despacha vehículos particulares, y revisar el estado de seguridad del corredor de Negomano."),
    # ---- Consular / sanidad ----
    ("Embajada de España en Dar es Salaam", "Consular", -6.7900, 39.2600,
     "99 B Kinondoni Road, P.O. Box 842, Dar es Salaam. Tel. (+255) 022 266 60 18/19 · Emergencia consular 24h: (+255) 754 04 21 23 · emb.daressalaam@maec.es. Es la única representación española del país: relevante sobre todo para el corredor de la costa."),
    ("Muhimbili National Hospital, Dar es Salaam", "Hospital", -6.8083, 39.2764,
     "Principal hospital de referencia del país. Mejor opción sanitaria del corredor costero; para casos graves, la práctica regional es la evacuación a Nairobi o Sudáfrica."),
    ("Clínicas privadas de Arusha", "Hospital", -3.3869, 36.6830,
     "Referencia sanitaria del corredor interior y del circuito norte (hospital del Monte Meru y varias clínicas privadas). Lo más cercano a Ngorongoro, Serengeti, Natron y Kilimanjaro: a partir de aquí, hacia el Serengeti, la evacuación es aérea."),
    ("Hospital de referencia · Mbeya", "Hospital", -8.9000, 33.4500,
     "Hospital zonal de referencia del sur, el primero tras entrar desde Zambia y el único serio antes de Iringa."),
    ("Mbwa Wa Africa · clínica veterinaria y refugio (Usa River, Arusha)", "Servicio", -3.3667, 36.8500,
     "Clínica veterinaria y refugio de animales en Usa River, a unos 25 km de Arusha camino de Moshi (P.O. Box 89; tel. refugio +255 626 515 750, clínica +255 627 593 149; lun-vie 9-17, sáb 9-14). LA referencia veterinaria del norte de Tanzania y el primer contacto a explorar para dejar al perro durante los días de Ngorongoro, Serengeti y, si se hace, Kilimanjaro. Confirmar por escrito si aceptan alojamiento de un perro viajero antes de contar con ello."),
    # ---- Ciudades de servicio / combustible ----
    ("Mbeya · base logística del sur", "Combustible", -8.9000, 33.4500,
     "Primera ciudad grande tras Tunduma (110 km) y base del altiplano del sur: combustible formal (TotalEnergies, Puma, Oryx), talleres, hospital, mercado. Punto de partida del lago Ngozi, de Kitulo y del desvío al oeste (Sumbawanga-Mpanda-Kigoma). Repostar a fondo antes de cualquiera de las tres cosas."),
    ("Combustible · Sumbawanga / Mpanda (eje del oeste)", "Combustible", -7.9667, 31.6167,
     "Las dos únicas plazas con suministro fiable del corredor occidental hacia Katavi y Kigoma. Entre ellas y hasta Kigoma hay cientos de kilómetros de grava: salir con depósitos y garrafas llenos. Sitalike, a la puerta de Katavi, no garantiza nada."),
    ("Combustible · Iringa", "Combustible", -7.7700, 35.6900,
     "Base logística del tramo sur a 1.600 m: combustible, talleres, recambios, hospital regional y buen mercado. Último suministro seguro antes de Ruaha (130 km de pista hasta Msembe) y punto de paso obligado entre Mbeya y Dodoma."),
    ("Dodoma · capital administrativa y nudo central", "Combustible", -6.1630, 35.7516,
     "Capital oficial del país desde 1973 (y sede del parlamento), en el centro geográfico: combustible, talleres, hospital y alojamiento. Nudo del corredor interior entre Iringa y Babati/Tarangire, con el desvío a la zona vinícola de Dodoma, poco conocida. No es una parada turística, pero sí el repostaje obligado de un tramo de 700 km."),
    ("Combustible · Arusha / Moshi", "Combustible", -3.3869, 36.6830,
     "Mejor oferta y calidad del corredor interior, con todas las marcas. Repostar a fondo antes de Ngorongoro-Serengeti (dentro de los parques no hay suministro fiable) y antes del desvío al lago Natron, donde no hay nada."),
    ("Combustible · Karatu (puerta del Ngorongoro)", "Combustible", -3.3333, 35.6667,
     "Última plaza con combustible, cajeros, supermercado y talleres antes de entrar al Área de Conservación del Ngorongoro y al Serengeti. Fundamental: el circuito Ngorongoro-Olduvai-Serengeti-Natron puede sumar 600-800 km sin una estación de servicio de confianza."),
    ("Combustible · Tanga / Dar es Salaam (eje de la costa)", "Combustible", -5.0689, 39.0989,
     "Corredor costero con estaciones formales en Tanga, Muheza, Korogwe, Bagamoyo y Dar es Salaam; sin gaps relevantes en el tramo norte de la costa."),
    ("Combustible · Kibiti / Kilwa Masoko / Lindi / Mtwara (sur de la costa)", "Combustible", -8.9333, 39.5167,
     "Eje sur de la costa por la T6 (recientemente mejorada): estaciones en Kibiti, Ikwiriri, Kilwa Masoko, Lindi y Mtwara. El gap real es el acceso a Nyerere/Mtemere (80-100 km de pista sin nada) y el desvío de Masasi hacia el puente de la Unidad."),
    # ---- Agua ----
    ("Agua potable y de uso general · Arusha, Dar es Salaam, Mbeya", "Agua potable", -3.3869, 36.6830,
     "Agua embotellada sin problema en supermercados de las tres ciudades; campings, lodges y hoteles permiten llenar el depósito de uso general con manguera. Confirmar siempre en recepción."),
    ("Agua · campings de los parques del norte", "Agua potable", -3.2000, 35.5000,
     "Los campings públicos del Ngorongoro (Simba) y del Serengeti (Seronera) tienen agua corriente y aseos, pero el suministro es irregular y no potable sin tratar. Entrar al circuito con los depósitos llenos al 100 % desde Karatu."),
    ("Agua · lago Natron y corredor del oeste", "Agua potable", -2.4500, 36.0167,
     "Sin garantía ninguna: en Engare Sero el agua es escasa y el calor extremo (hay que contar 5-6 litros por persona y día), y en el eje Sumbawanga-Mpanda-Kigoma no hay recarga fiable fuera de las ciudades. Salir al 100 % y llevar filtro."),
]

DRONE_CALLOUT = ("danger", "De hecho inviable para nosotros: registro de 100 USD, licencia de piloto de 200 USD y prohibición en parques nacionales",
                  "Tanzania es uno de los países más restrictivos de África con los drones. Todo dron debe estar REGISTRADO en la Tanzania Civil Aviation Authority (TCAA), con un coste de unos 100 USD y prueba de propiedad; para operaciones de categoría 2 y 3 (uso privado y comercial) el piloto necesita además licencia —21 años mínimo, certificado médico, acreditación de inglés, licencia de radiotelefonía, formación y exámenes— por unos 200 USD. Los visitantes extranjeros deben obtener permiso previo de la TCAA, acreditación del país de origen y, en la práctica, aprobación del Ministerio de Defensa; los drones de más de 7 kg requieren aprobación militar explícita. EL VUELO SOBRE PARQUES NACIONALES ESTÁ PROHIBIDO, y TANAPA añade un permiso de pago adicional que rara vez se concede a particulares. Altura máxima 121 m, prohibido de noche, 3 km de aeropuertos domésticos y 5 km de internacionales. Norma del proyecto: dar el dron por INUTILIZABLE en Tanzania salvo que se tramite todo con meses de antelación, y no intentar introducirlo sin papeles (hay confiscaciones documentadas en la aduana).")

STARLINK_CALLOUT = ("warn", "Tanzania es el agujero de la región: anunciado para 2026, sin servicio residencial activo — tratar como NO disponible",
                     "Starlink solicitó licencia en Tanzania a finales de 2024 y fue preseleccionada por la TCRA, y parte del mercado ya se sirve mediante un acuerdo directo-a-dispositivo con Airtel Africa, pero el servicio residencial pleno seguía pendiente de aprobación a mediados de 2026: Tanzania figura entre los países «previstos durante 2026», junto con Uganda, Angola y Namibia. Es llamativo porque TODOS sus vecinos del bucle ya están activos (Kenia, Zambia, Mozambique y Malaui). Conclusión operativa: entrar dando Starlink por no disponible, llevar SIM local (Vodacom, Airtel Tanzania, Halotel) como conectividad principal, y reconfirmar el estado 30-60 días antes. Añadido de 2025: durante las protestas poselectorales hubo un apagón total de internet de unos cinco días y restricciones posteriores a redes sociales — no depender de una sola vía de comunicación.")

DOG_MATRIX = [
    ("TODOS los parques nacionales de TANAPA (Serengeti, Tarangire, Manyara, Ruaha, Nyerere, Udzungwa, Kitulo, Katavi, Mahale, Gombe, Saadani, Mikumi, Kilimanjaro, Arusha)", "prohibido",
     "La normativa de TANAPA prohíbe introducir animales ajenos al parque; en los parques con grandes depredadores y megafauna es además inviable. Plan B obligatorio: TURNOS entre los tres viajeros, quedándose uno con el perro en el camping o el alojamiento de la puerta (Karatu para Ngorongoro/Serengeti, Mto wa Mbu para Manyara, Mang'ula para Udzungwa, Iringa para Ruaha, Sitalike para Katavi), o cuidador en Arusha (clínica/refugio Mbwa Wa Africa, Usa River) para los bloques largos."),
    ("Área de Conservación del Ngorongoro (NCAA)", "prohibido",
     "No es TANAPA sino NCAA, pero aplica la misma prohibición de mascotas y se suma que el ranger es obligatorio para el descenso. Además el cráter se hace en un solo día de 12 horas: es el escenario perfecto para el reparto por turnos, con dos viajeros bajando y uno quedándose con el perro en el camping de Simba o en Karatu."),
    ("Lago Natron y Engare Sero (WMA comunitaria)", "permitido con condiciones",
     "LA MEJOR OPCIÓN DEL CORREDOR INTERIOR CON EL PERRO: no es parque nacional sino Área de Gestión de Fauna gestionada por las aldeas masái, así que no aplica la prohibición de TANAPA — se pagan tasas de aldea y de actividad y se acampa en campings comunitarios. Hay flamencos enanos por decenas de miles y un volcán activo enfrente. Condiciones reales: calor extremo sin sombra (toldo y 5-6 l de agua por persona y día), hienas y chacales de noche (perro dentro del vehículo), y la ascensión al Ol Doinyo Lengai NO es apta para él: se queda en el camping con un viajero."),
    ("Lago Ngozi, Isimila, montes Usambara, cuevas de Amboni, manantiales de Galanos", "permitido con correa",
     "Todos fuera de parque nacional y por tanto compatibles: son, junto con Natron, los puntos fuertes del viaje con el perro. En los Usambara la red de caminos entre aldeas es ideal para caminar con él; correa corta en el mirador de Irente (cortado de 1.000 m sin protección) y en el borde del cráter del Ngozi. En las cuevas de Amboni, consultar al guía: hay tramos estrechos y murciélagos."),
    ("Ciudades y costa: Arusha, Mbeya, Iringa, Dodoma, Dar es Salaam, Tanga, Pangani, Bagamoyo, Kilwa, Mtwara", "permitido con condiciones",
     "Sin restricción específica; correa y sombra. Calor y humedad muy altos en toda la franja costera (Tanga a Mtwara) — evitar las horas centrales y vigilar la deshidratación. En los pueblos costeros, de mayoría musulmana, el perro se percibe como impuro: llevarlo siempre atado, no entrar con él en patios, mercados cubiertos ni recintos religiosos, y preguntar antes en cualquier alojamiento."),
    ("Zanzíbar", "no recomendado",
     "Caso aparte y nuestra recomendación es NO llevarlo. Tres razones: (1) es un territorio semiautónomo con su propio control de entrada y la normativa sanitaria para animales no está clara — puede exigir trámite propio; (2) llevar el vehículo exige un ferry de carga aparte, con lo que el perro tendría que viajar en un ferry rápido de pasajeros donde no está previsto; (3) es una sociedad de mayoría musulmana con calor húmedo extremo, callejuelas abarrotadas en Stone Town y sin la infraestructura veterinaria de Dar. PLAN: hacer Zanzíbar a pie, 3 días, dejando vehículos y perro en Dar es Salaam con cuidador o en un alojamiento con parking vigilado y personal que lo atienda; o saltarse la isla y dedicar esos días a Kilwa y Saadani, que son más nuestro tipo de sitio y sí admiten al perro."),
    ("Katavi y el corredor del oeste", "prohibido (parque) / precaución extrema (fuera)",
     "Aparte de la prohibición dentro del parque, el oeste es zona de MOSCA TSÉ-TSÉ: transmite tripanosomiasis, que en perros es a menudo mortal y para la que no hay profilaxis fiable. Es un argumento de peso para descartar el bucle del oeste con el perro a bordo, o para no salir de los tramos asfaltados. Consultar con el veterinario antes de decidir."),
]

SOURCES = [
    ("Tanzania eVisa · guía oficial de solicitud (Immigration Department)", "https://visa.immigration.go.tz/guidelines"),
    ("TANAPA · Parques Nacionales de Tanzania, tarifas e información para visitantes", "https://www.tanzaniaparks.go.tz/tourism/visitor-information/tariff"),
    ("TANAPA · planificar la visita", "https://www.tanzaniaparks.go.tz/plan-a-trip"),
    ("Ngorongoro Conservation Area Authority (NCAA) · tarifas oficiales", "https://www.ncaa.go.tz/tariffs/"),
    ("Roadtrip Africa · tasas y permisos de los parques nacionales de Tanzania para autoconducción", "https://roadtripafrica.com/en/tanzania/practical-info/national-parks/"),
    ("Roadtrip Africa · conducir en Tanzania (límites, controles, estado de las carreteras)", "https://www.roadtripafrica.com/tanzania/practical-info/driving-in-tanzania/"),
    ("Roadtrip Africa · autoconducción en el Área de Conservación del Ngorongoro", "https://www.roadtripafrica.com/travel-blog/travelling-the-ngorongoro-conservation-area/"),
    ("Roadtrip Africa · guía de autoconducción al lago Natron", "https://www.roadtripafrica.com/travel-blog/visiting-lake-natron/"),
    ("Self Drive Tanzania · pago de tasas de parque para clientes de autoconducción", "https://www.selfdrivetanzania.com/ultimate-guide-on-park-fee-payment-for-self-drive-clients-in-tanzania/"),
    ("Altezza Travel · tasas del Parque Nacional del Kilimanjaro 2026, desglose completo", "https://altezzatravel.com/articles/kilimanjaro-park-fees"),
    ("Altezza Travel · normas de los parques nacionales de Tanzania", "https://altezzatravel.com/articles/national-parks-rules"),
    ("Journeyera · relato detallado de la ascensión nocturna al Ol Doinyo Lengai", "https://www.journeyera.com/ol-doinyo-lengai-volcano/"),
    ("Journeyera · travesía a pie de los Usambara, de Lushoto a Mtae", "https://www.journeyera.com/usambara-mountains-lushoto-to-mtae/"),
    ("Tracks4Africa Blog · Tanzania occidental (Kigoma, Katavi, Mpanda): estado real de las pistas", "https://blog.tracks4africa.co.za/western-tanzania/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
    ("Tracks4Africa Padkos · ficha del paso fronterizo de Namoto (ferry del Rovuma)", "https://tracks4africa.co.za/listings/item/w240781/namoto-ruvuma-ferry-border-post-tzmoz-07h00-19h00/"),
    ("Accommodation Mozambique · paso fronterizo del ferry Namoto/Kilambo: horarios, mareas y aviso de seguridad", "https://www.accommodationmozambique.co.za/mozambique-border-gates-and-times/namoto-kilambo-ferry-border-post-crossing/"),
    ("Accommodation Mozambique · paso fronterizo de Negomano/Mtambaswala (puente de la Unidad)", "https://www.accommodationmozambique.co.za/mozambique-border-gates-and-times/negomane-mtambaswala-unity-bridge-border-post-crossing/"),
    ("Border Crossing Hub · paso de Horohoro/Lunga Lunga (Tanzania-Kenia, costa)", "https://bordercrossinghub.com/horohoro-lunga-lunga-border-crossing/"),
    ("Logistics Cluster (LCA) · paso fronterizo de Mtambaswala/Negomano", "https://lca.logcluster.org/238-tanzania-border-crossing-mtambaswala-mozambique"),
    ("The Road Chose Me (Dan Grec) · entrada a Tanzania con vehículo propio: tasas reales y discusión del CPD", "https://theroadchoseme.com/into-tanzania"),
    ("Horizons Unlimited · Tanzania: permiso temporal de importación frente a carnet de paso", "https://www.horizonsunlimited.com/hubb/sub-saharan-africa/tanzania-temporary-import-permit-carnet-26300"),
    ("Tucks' Truck · registro de cruces de frontera en África con importes pagados (Songwe, Namanga)", "https://tuckstruck.net/overland-planning/overlanding-africa/border-crossings-africa/"),
    ("Stuck In Low Gear · visita overland a las ruinas de Kilwa Kisiwani (permiso, dhow, camping)", "https://stuckinlowgear.com/unesco-ruins-kilwa-swahilli-coast/"),
    ("Stuck In Low Gear · lago Natron en autoconducción", "https://stuckinlowgear.com/exploring-lake-natron/"),
    ("Drone Laws · normativa de drones de Tanzania (TCAA): registro, licencia, prohibiciones", "https://drone-laws.com/drone-laws-in-tanzania/"),
    ("tech.africa · Starlink en África, estado por país 2026 (Tanzania: previsto 2026, aún no activo)", "https://tech.africa/starlink-africa/"),
    ("Space in Africa · solicitud de licencia de Starlink en Tanzania", "https://spaceinafrica.com/2024/11/16/starlink-applies-for-licenses-to-operate-in-tanzania/"),
    ("Embajada de Tanzania (Berlín) · permiso de importación de mascotas: autoridad, documentos y tasas", "https://www.de.tzembassy.go.tz/services/import-permit-food-plants-pets-and-animal-products"),
    ("PetTravel.com · requisitos de importación de mascotas a Tanzania", "https://www.pettravel.com/information/pet-passports/tanzania-pet-import-requirements/"),
    ("Mbwa Wa Africa · clínica veterinaria y refugio en Usa River (Arusha)", "https://mbwa-wa-africa.org/"),
    ("Tanzania Tourism (web oficial de turismo) · Parque Nacional de Kitulo", "https://www.tanzaniatourism.com/destination/kitulo-national-park"),
    ("Tanzania Tourism (web oficial de turismo) · yacimiento de Isimila", "https://www.tanzaniatourism.com/destination/isimila-stone-age-site"),
    ("Tanzania Tourism (web oficial de turismo) · ruinas de Kaole, Bagamoyo", "https://www.tanzaniatourism.com/safari/kaole-ruins-bagamoyo"),
    ("TAWA · ruinas de Kilwa Kisiwani y Songo Mnara, Patrimonio de la Humanidad", "https://www.tawa.go.tz/attraction-details/ruins-kilwa-and-songo-mnara-world-heritage-site"),
    ("UNESCO · Stone Town de Zanzíbar", "https://whc.unesco.org/en/list/173/"),
    ("UNESCO · Área de Conservación de Ngorongoro", "https://whc.unesco.org/en/list/39/"),
    ("UNESCO · Parque Nacional del Serengeti", "https://whc.unesco.org/en/list/156/"),
    ("UNESCO · Ruinas de Kilwa Kisiwani y de Songo Mnara", "https://whc.unesco.org/en/list/144/"),
    ("UNESCO · Parque Nacional del Kilimanjaro", "https://whc.unesco.org/en/list/403/"),
    ("Wikipedia · Lake Ngozi", "https://en.wikipedia.org/wiki/Lake_Ngozi"),
    ("Wikipedia · Udzungwa Mountains National Park", "https://en.wikipedia.org/wiki/Udzungwa_Mountains_National_Park"),
    ("Wikipedia · Isimila Stone Age Site", "https://en.wikipedia.org/wiki/Isimila_Stone_Age_Site"),
    ("Wikipedia · Olduvai Gorge", "https://en.wikipedia.org/wiki/Olduvai_Gorge"),
    ("Wikipedia · Ol Doinyo Lengai", "https://en.wikipedia.org/wiki/Ol_Doinyo_Lengai"),
    ("Wikipedia · Amboni Caves", "https://en.wikipedia.org/wiki/Amboni_Caves"),
    ("Wikipedia · Unity Bridge (puente del Rovuma)", "https://en.wikipedia.org/wiki/Unity_Bridge"),
    ("Wikipedia · Selous Game Reserve / Nyerere National Park", "https://en.wikipedia.org/wiki/Selous_Game_Reserve"),
    ("Wikipedia · protestas electorales de Tanzania de 2025", "https://en.wikipedia.org/wiki/2025_Tanzanian_election_protests"),
    ("iOverlander · puntos de combustible, agua, camping y fronteras verificados por la comunidad", "https://ioverlander.com/"),
]

# Corredor 1 — SUBIDA POR EL INTERIOR: Tunduma/Nakonde -> Mbeya -> Iringa -> Ruaha -> Udzungwa
# -> Iringa -> Dodoma -> Tarangire -> Manyara -> Ngorongoro -> Serengeti -> Natron -> Arusha -> Namanga
CORRIDOR = [(-9.3000, 32.7667), (-8.9000, 33.4500), (-9.0081, 33.5531), (-9.0500, 33.8333),
            (-8.9000, 33.4500), (-7.7700, 35.6900), (-7.9167, 35.6000), (-7.6833, 34.8167),
            (-7.7700, 35.6900), (-7.8436, 36.8833), (-7.7700, 35.6900), (-6.1630, 35.7516),
            (-4.2167, 35.7500), (-3.6833, 35.9667), (-3.5833, 35.8250), (-3.3333, 35.6667),
            (-3.2000, 35.5000), (-2.9917, 35.3500), (-2.4333, 34.8333), (-2.4500, 36.0167),
            (-2.7642, 35.9142), (-2.4500, 36.0167), (-3.3869, 36.6830), (-3.0674, 37.3556),
            (-3.3869, 36.6830), (-2.5450, 36.7867)]

# Variante del interior: bucle del oeste salvaje (Katavi, Kigoma, Mahale) desde Mbeya
CORRIDOR_WEST = [(-8.9000, 33.4500), (-7.9667, 31.6167), (-6.8833, 31.1667),
                 (-6.1000, 29.7667), (-4.8769, 29.6267)]

# Corredor 2 — BAJADA POR LA COSTA: Horohoro/Lunga Lunga -> Tanga -> Usambara -> Pangani
# -> Saadani -> Bagamoyo -> Dar -> (Zanzíbar) -> Nyerere -> Kilwa -> Lindi -> Mtwara -> Mozambique
CORRIDOR_ALT = [(-4.6000, 39.1054), (-5.0689, 39.0989), (-4.7833, 38.2833), (-5.4264, 38.9803),
                (-6.0167, 38.7833), (-6.4400, 38.9000), (-6.7924, 39.2083), (-6.1659, 39.1917),
                (-6.7924, 39.2083), (-7.7500, 37.9000), (-8.9333, 39.5167), (-8.9578, 39.5206),
                (-9.9833, 39.7167), (-10.2667, 40.1833), (-10.4667, 40.4167)]

EXPERIENCIAS = [
    "Tanzania occidental en 4x4 (blog de Tracks4Africa): estado real de las pistas del corredor del oeste, el tramo que estamos valorando para Katavi y Kigoma. La B3 hacia el sureste, «bastante bacheada»; la grava de la B8 entre Nyakanazi y Kigoma empieza mal y después «mejora tremendamente»; la ruta de montaña de Kigoma a Mwese son 45 km de pista técnica con roca que les llevó 3 horas y media y exige 4x4 con reductora; y la B8 sur entre Mpanda y Kapili, «un poco corrugada, pero nada comparado con las carreteras de entrada al Serengeti o a Mana Pools», con medias de 50-60 km/h. Camping de referencia: Jakobsen Beach, junto a Kigoma, con agua del Tanganyika a 26 grados. Avisan de dos cosas: apenas se habla inglés en el oeste profundo, y hay moscas tsé-tsé.",
    "Entrada a Tanzania con vehículo propio (Dan Grec, The Road Chose Me): visado 50 USD por persona y tasa de carretera de 25 USD al mes pagada en el banco de la frontera; por tres meses, 75 USD. El funcionario de aduanas le exigió primero un Carnet de Passage para su vehículo matriculado en Canadá diciendo que era obligatorio para vehículos extranjeros y, tras una negociación larga, acabó emitiéndole un permiso temporal de importación (TIP) de tres meses. Su conclusión, literal: «las normas cambian cada tres meses y cada agente de frontera hace lo que le parece». Lección para nosotros: llevar el CPD en regla y no depender de que acepten un TIP, pero saber que el TIP existe.",
    "Tasas de frontera documentadas (Tucks' Truck, registro de cruces con importes): en Songwe, visado 50 USD por persona (3 meses), tasas de carretera de 25 y 5 USD, seguro cubierto con la Tarjeta Amarilla COMESA, y carnet procesado con un TIP de cortesía encima. En Namanga, al reentrar desde Kenia con visado de Comunidad de África Oriental aún válido, les volvieron a cobrar 25 USD de tasa de carretera; meses después, en Songwe, otros funcionarios les confirmaron que Namanga se lo había cobrado indebidamente. Pedir siempre justificante de cada tasa.",
    "Permiso de importación de la mascota: el cruce de frontera terrestre es el punto ciego. La Embajada de Tanzania informa de que el permiso lo emite el Director de Servicios Veterinarios del ministerio competente (oficina veterinaria de Temeke, Dar es Salaam; tel. +255 22 2862592, zoosanitary@mifugo.go.tz), con carta de solicitud indicando raza, edad y PUERTO DE ENTRADA PREVISTO, certificado de vacunación antirrábica (1-3 años antes) y una tasa de 30.000 TSh (más 20.000 al sacarlo). PetTravel, en cambio, afirma que las mascotas «solo pueden entrar por vía aérea por los aeropuertos de Dar es Salaam o Kilimanjaro». Las dos cosas no pueden ser ciertas a la vez para un viaje overland: hay que resolverlo por escrito con el Director de Servicios Veterinarios ANTES de salir de Europa, indicando Tunduma y Horohoro como puertos de entrada.",
    "Kilwa Kisiwani en overland (Stuck In Low Gear): llegaron por la T6 desde Songea y Lindi, una carretera recién mejorada con financiación estadounidense que describen como ancha, con arcenes y «relajada» comparada con otras rutas tanzanas — buena noticia para nuestra bajada al sur. Para la isla hace falta permiso de la oficina local de antigüedades, guía obligatorio y barca; pidieron un dhow a vela en lugar de lancha y la travesía fue de unos 20 minutos, con un vadeo por barro al llegar si la marea está baja. Durmieron en Kilwa Beach Lodge, camping en la playa por 10 USD por persona con sombrajo y baños limpios.",
    "Frontera sur hacia Mozambique, el punto más delicado de toda la ficha: el paso de Kilambo/Namoto, a 40 km de Mtwara, NO es el puente de la Unidad sino una barcaza sobre la desembocadura del Rovuma con capacidad para unos 6 vehículos 4x4, cuya salida depende de la marea (hacen falta 3 m de agua) y que puede obligar a dormir esperando; hay un número de contacto del patrón para confirmar horarios. Las fuentes especializadas de Mozambique recomiendan expresamente NO entrar por ahí ni viajar por el norte de Cabo Delgado (Palma, Mocímboa da Praia, Quionga, Pangane) por los ataques de la insurgencia, y proponen usar otros pasos. El puente de la Unidad real está en Mtambaswala/Negomano, 180 km tierra adentro vía Masasi.",
    "Autoconducción en el Ngorongoro (Roadtrip Africa, contrastado con relatos de viajeros): el ranger es OBLIGATORIO para bajar al cráter, 40 USD y SOLO EN EFECTIVO, y no puede conducir el vehículo; no hace falta si solo se atraviesa el Área de Conservación sin bajar. El permiso no se compra en la puerta, hay que gestionarlo antes a través de un operador. Horario 06:00-18:00, pase de día válido 12 horas y pase con pernocta 24 horas. Las pistas del fondo del cráter están bien mantenidas y señalizadas. Del cráter a la puerta de Naabi Hill del Serengeti hay 85 km y se tarda 2-3 horas: hay que salir con margen porque las puertas cierran a las 18:00 y está prohibido conducir de noche. Camping público económico: Simba A, en el borde del cráter.",
    "Pago de tasas de parque: los permisos de TANAPA se compran al llegar, sin reserva previa, pero SOLO CON TARJETA VISA O MASTERCARD — no aceptan efectivo ni tarjetas de débito. Conviene llevar dos tarjetas de crédito operativas y avisar al banco, porque un rechazo en la puerta de Naabi Hill con 3.000 km de viaje detrás es un problema serio. Excepciones en efectivo: el ranger del cráter (40 USD) y las tasas comunitarias del lago Natron.",
    "Conducir en Tanzania (Roadtrip Africa): límite de 80 km/h en carretera (los Land Cruiser se clasifican como camión), 40 km/h en poblado y 35 km/h dentro de los parques; controles frecuentes de la policía de tráfico, de uniforme blanco, que revisan seguro, neumáticos y permiso —el carnet nacional se acepta— y radares con multa que se paga por ingreso bancario. Las carreteras del norte están asfaltadas pero llenas de badenes y baches; las secundarias C y D son de tierra con erosión; las pistas principales del Serengeti son de roca y corrugado y obligan a ir por debajo de 25 km/h. Recomiendan expresamente no conducir de noche.",
]

CORRIDOR_LABEL = "Subida por el interior (Zambia → Kenia)"
CORRIDOR_ALT_LABEL = "Bajada por la costa (Kenia → Mozambique)"

HISTORIA_RESUMEN = ("Tanzania nace de la unión en 1964 de Tanganica y el sultanato de Zanzíbar, dos historias muy distintas — el interior bantú de las rutas del marfil y el emporio comercial suajili-omaní de la costa — "
                     "fusionadas bajo el liderazgo de Julius Nyerere y su particular experimento socialista africano (ujamaa); durante décadas fue uno de los países más estables del continente, aunque las elecciones de octubre de 2025 y su represión abrieron la crisis política más grave de su historia reciente. "
                     "En su territorio están tanto la garganta de Olduvai, donde se escribió el capítulo decisivo del origen humano, como el Serengeti y el Ngorongoro, epicentro mundial de la conservación de fauna.")

HISTORIA_SECCIONES = [
    ("La cuna de la humanidad",
     "El norte de Tanzania guarda la secuencia más completa del origen humano que existe: en la garganta de Olduvai, Mary y Louis Leakey encontraron en 1959 el cráneo de Paranthropus boisei y poco después los restos que darían nombre al Homo habilis, junto a la industria lítica olduvayense, la tecnología reconocida más antigua; "
     "a 45 km, en Laetoli, unas huellas de hace 3,6 millones de años demuestran que los australopitecos ya caminaban erguidos. Más al sur, Isimila conserva un campamento achelense de decenas de miles de años, y junto al lago Natron hay unas 400 huellas humanas de entre 5.000 y 19.000 años, el mayor conjunto de huellas de Homo sapiens de África."),
    ("La costa suajili y el sultanato de Zanzíbar",
     "Durante más de un milenio, la costa tanzana formó parte del mundo suajili, una civilización mestiza de comerciantes bantúes, árabes y persas que edificó ciudades-estado prósperas con el oro, el marfil y los esclavos. Kilwa Kisiwani fue la mayor de todas: controló la salida del oro de Zimbabue, acuñó moneda propia y deslumbró a Ibn Battuta en el siglo XIV. "
     "En el siglo XIX el sultanato omaní trasladó su capital a Zanzíbar, convirtiendo la isla en el mayor mercado de esclavos y de clavo del Índico occidental, con Stone Town como corazón y Bagamoyo como puerto terminal de las caravanas del interior."),
    ("Colonización alemana y británica del interior",
     "El interior, poblado por más de cien grupos étnicos bantúes, nilóticos y cusitas, fue colonizado por Alemania a finales del siglo XIX como África Oriental Alemana, con una represión especialmente dura durante la rebelión Maji Maji (1905-1907), que dejó cientos de miles de muertos en el sur; "
     "el jefe hehe Mkwawa, que resistió desde Iringa, es hoy un héroe nacional. Tras la Primera Guerra Mundial el territorio pasó a administración británica como Tanganica, mientras Zanzíbar seguía siendo un protectorado aparte con su sultanato nominal."),
    ("Independencia, unión y el socialismo de Nyerere",
     "Tanganica se independizó en 1961 y Zanzíbar en 1963, pero una revolución popular derrocó al sultán apenas un mes después. En 1964 ambos territorios se unieron para formar Tanzania bajo el liderazgo de Julius Nyerere, que impulsó el ujamaa, un socialismo africano de aldeas comunales, y el suajili como lengua nacional unificadora: "
     "una política de resultados económicos pobres pero que dejó al país una cohesión nacional y una estabilidad política excepcionales en la región, sin las fracturas étnicas que marcaron a sus vecinos."),
    ("Situación actual: estabilidad cuestionada y capital mundial de los safaris",
     "Tanzania fue durante décadas un referente de estabilidad, pero las elecciones generales del 29 de octubre de 2025 —con la oposición excluida y un resultado oficial del 98 % para la presidenta Samia Suluhu Hassan— desencadenaron protestas masivas en Dar es Salaam, Arusha y Mwanza y una represión cuyo número de muertos sigue en disputa: "
     "la ONU confirmó 10, la BBC habló de más de 500 y una comisión gubernamental cifró en abril de 2026 un total de 518, mientras la oposición y organizaciones de derechos humanos manejan cifras mucho mayores. Hubo un apagón total de internet de cinco días y cientos de detenidos por traición. "
     "En paralelo, el país sigue albergando algunos de los ecosistemas más importantes del planeta —Serengeti, Ngorongoro, Kilimanjaro, Ruaha, Nyerere— convertidos en el eje de una industria turística carísima y muy regulada."),
]

HISTORIA_FUENTES = [
    ("BBC News · Tanzania country profile", "https://www.bbc.com/news/world-africa-14095868"),
    ("Encyclopaedia Britannica · Tanzania, History", "https://www.britannica.com/place/Tanzania/History"),
    ("UNESCO · Stone Town de Zanzíbar, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/173/"),
    ("UNESCO · Área de Conservación de Ngorongoro, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/39/"),
    ("UNESCO · Ruinas de Kilwa Kisiwani y de Songo Mnara", "https://whc.unesco.org/en/list/144/"),
    ("Wikipedia · protestas electorales de Tanzania de 2025", "https://en.wikipedia.org/wiki/2025_Tanzanian_election_protests"),
]

SPEC = dict(
    slug="tanzania", name="Tanzania", revision="11 sep 2026",
    sub="Corredor doble interior/costa · el país más caro del bucle · documentación · logística",
    chips=[
        ("INTERIOR (hacia Kenia)", "Tunduma/Nakonde → Mbeya → Ruaha → Iringa → Dodoma → circuito norte → Natron → Arusha → Namanga · ~3.000 km"),
        ("COSTA (hacia Mozambique)", "Horohoro/Lunga Lunga → Tanga → Usambara → Bagamoyo → Dar → Nyerere → Kilwa → Mtwara · ~1.700 km"),
        ("PDIs", "26 puntos repartidos entre los dos corredores, sin solapamiento"),
        ("DINERO", "El país más caro del viaje: Ngorongoro ~700-1.000 USD el día de cráter · tasas SOLO con tarjeta"),
        ("A PIE", "Ol Doinyo Lengai de noche · monte Meru 4.562 m · Sanje (Udzungwa) · travesías de los Usambara · Kitulo · cráter del Ngozi"),
        ("4x4", "Pista del oeste a Katavi y Kigoma · acceso al lago Natron · Serengeti y descenso al cráter · T6 al sur"),
        ("PERRO", "Prohibido en TODOS los parques TANAPA y en el NCAA · lago Natron SÍ (es WMA comunitaria) · Zanzíbar: dejarlo en Dar"),
        ("DRON", "De hecho inviable: registro 100 USD + licencia 200 USD y prohibido en parques"),
        ("STARLINK", "Tanzania es el agujero de la región: NO activo, a diferencia de todos sus vecinos"),
        ("SEGURIDAD", "Revisar: crisis poselectoral de octubre-noviembre de 2025 con represión y apagón de internet"),
    ],
    center=[-6.5, 36.0], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada. Esta ficha se reescribió por completo el 11 de septiembre de 2026: la versión anterior describía una entrada desde Malaui que ya no forma parte de la ruta.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Wide%20aerial%20landscape%20of%20the%20Ngorongoro%20ecosystem.jpg?width=1600",
    hero_credit="Cráter del Ngorongoro · Arnold Tibaijuka · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Tanzania es el país que se cruza DOS VECES por rutas que no se parecen en nada. En la <strong>subida por el interior</strong> "
                   "se entra desde Zambia por Tunduma/Nakonde y se atraviesa el país de suroeste a noreste: el altiplano del sur (lago Ngozi, Kitulo), "
                   "el gran parque de Ruaha, las cascadas de Udzungwa, Iringa e Isimila, Dodoma, y después el circuito norte completo —Tarangire, Manyara, "
                   "Ngorongoro, Olduvai, Serengeti—, el lago Natron con el volcán activo Ol Doinyo Lengai y Arusha, para salir hacia Kenia por Namanga, "
                   "junto a Amboseli. Hay además un <strong>bucle opcional por el oeste salvaje</strong> (Katavi, Kigoma, Ujiji y los chimpancés de Mahale y Gombe), "
                   "unos 2.000 km de ida y vuelta de grava. En la <strong>bajada por la costa</strong>, meses después, se entra desde Kenia por el paso costero de "
                   "Horohoro/Lunga Lunga y se baja por el mundo suajili: Tanga y las cuevas de Amboni, los montes Usambara, Pangani y Saadani, Bagamoyo, "
                   "Dar es Salaam, Zanzíbar, el inmenso Nyerere y las ruinas de Kilwa Kisiwani, hasta Mtwara y la meseta makonde. Los dos corredores "
                   "<strong>no comparten ni un solo punto</strong>. Tanzania es también, con diferencia, el país <strong>más caro</strong> de todo el viaje: "
                   "hay que presupuestarlo aparte."),
    facts=[
        ("Rol en la ruta", "Corredor DOBLE del bucle: se sube por el interior de Zambia a Kenia y se baja por la costa de Kenia a Mozambique, por rutas completamente distintas."),
        ("Entrada interior", "Tunduma/Nakonde desde Zambia (suroeste): el gran paso del corredor TANZAM, ventanilla única, mucho camión y colas."),
        ("Salida interior", "Namanga hacia Kenia, junto a Amboseli. Revisar estado del paso: sufrió disturbios en noviembre de 2025."),
        ("Entrada costa", "Horohoro/Lunga Lunga desde Kenia, sobre la A14 Mombasa-Dar: ventanilla única moderna, 24 h, asfalto bueno. Paso DISTINTO al de subida."),
        ("Salida costa", "Dos opciones y ninguna sencilla: el ferry de Kilambo/Namoto (40 km de Mtwara, dependiente de marea, con la zona mozambiqueña bajo insurgencia) o el puente de la Unidad de Mtambaswala/Negomano, 180 km tierra adentro vía Masasi. Decisión abierta."),
        ("Visado", "e-Visa obligatoria para españoles: 50 USD, validez hasta 90 días, tramitación de hasta 10 días. SE NECESITAN DOS ENTRADAS: valorar el visado de entrada múltiple (100 USD) o dos e-Visa de entrada única."),
        ("Presupuesto de parques", "Crítico. TANAPA cobra por persona y día (35,40 USD en Ruaha/Udzungwa/Katavi/Mikumi/Saadani; 59 en Tarangire/Manyara/Arusha; 82,60 en Serengeti/Nyerere/Kilimanjaro; 94,40 en Mahale; 118 en Gombe) más vehículo y más 35,40-59 USD por persona y noche de acampada. El Ngorongoro va aparte: 70,80/persona + tasa de vehículo por peso (177-236 USD) + 295 USD de descenso al cráter + 40 USD de ranger en efectivo."),
        ("Pago", "Los permisos de TANAPA se pagan en la puerta SOLO con tarjeta de crédito Visa o Mastercard: no aceptan efectivo ni débito. Llevar dos tarjetas operativas y avisar al banco."),
        ("Perro", "Prohibido en todos los parques nacionales de TANAPA y en el Área de Conservación del Ngorongoro. La excepción buena es el lago Natron, que es un área comunitaria (WMA) y no parque. Zanzíbar: no llevarlo."),
        ("Comunicaciones", "Starlink NO activo (único hueco de la región). SIM local Vodacom/Airtel/Halotel como base."),
        ("Seguridad", "País históricamente estable, pero con una crisis poselectoral grave en octubre-noviembre de 2025 (protestas, represión con víctimas en disputa, apagón de internet de cinco días). Revalidar 30 días antes."),
    ],
    alerts=[
        "Presupuesto: Tanzania es el país más caro de todo el viaje y puede descuadrar el presupuesto general. Un solo día en el cráter del Ngorongoro con 3 personas y un vehículo de 2-3 toneladas suma 70,80×3 + 177 de vehículo + 295 de descenso + 40 de ranger = unos 724 USD, y eso sin acampada; con los dos vehículos dentro pasa de 900. Tres noches en el Serengeti para 3 personas superan los 1.000 USD solo en tasas. Hay que decidir POR ADELANTADO qué parques entran y cuántos días, y aceptar que algunos se ven desde fuera.",
        "Pago con tarjeta obligatorio: las tasas de TANAPA no se pagan en efectivo ni con tarjeta de débito, solo con Visa o Mastercard de crédito en la puerta. Llevar dos tarjetas de crédito distintas, probadas y con límite suficiente, y avisar a los bancos de las fechas — un rechazo en la puerta de Naabi Hill deja el safari en tierra.",
        "Doble entrada: se entra dos veces en el país, meses aparte y por fronteras distintas. Confirmar si conviene un visado de entrada múltiple (100 USD, hasta 12 meses) o dos e-Visa de entrada única (50 USD cada una), y comprobar que el e-Visa es válido en los puestos terrestres de Tunduma y Horohoro concretamente. Tanzania exige además mostrar billete de salida en el punto de entrada: preparar una explicación documentada del viaje overland.",
        "PERRO Y FRONTERA TERRESTRE — punto sin resolver: hay contradicción entre la información consular tanzana (permiso del Director de Servicios Veterinarios indicando el puerto de entrada previsto, tasa de 30.000 TSh) y PetTravel, que afirma que las mascotas solo pueden entrar por los aeropuertos de Dar es Salaam o Kilimanjaro. Hay que resolverlo POR ESCRITO con el Director de Servicios Veterinarios (zoosanitary@mifugo.go.tz) antes de salir de Europa, citando expresamente Tunduma y Horohoro. Es un bloqueante potencial de toda la ruta del bucle.",
        "Perro y parques: TANAPA prohíbe los animales ajenos al parque y el NCAA también. Con 18 de los 26 PDIs del interior dentro de un parque nacional, el corredor interior solo funciona con un plan de turnos muy bien hecho: uno de los tres viajeros se queda fuera con el perro cada vez. Las bases para eso son Karatu (Ngorongoro/Serengeti), Mto wa Mbu (Manyara), Iringa (Ruaha), Mang'ula (Udzungwa) y Arusha (bloques largos, con la clínica Mbwa Wa Africa por confirmar).",
        "Frontera sur hacia Mozambique — el punto más crítico de la ficha. El paso de Kilambo/Mtwara NO es un puente: es una barcaza sobre la desembocadura del Rovuma, dependiente de la marea (mínimo 3 m de agua), con horario tanzano muy restringido y que deja en la zona del norte de Cabo Delgado donde las fuentes especializadas recomiendan expresamente NO entrar por los ataques de la insurgencia. El puente de la Unidad está en Mtambaswala/Negomano, 180 km tierra adentro. Hay que decidir la salida del bucle antes de cerrar el calendario, y coordinarla con la ficha de Mozambique.",
        "Kilimanjaro: subirlo cuesta 1.000-1.200 USD por persona solo en tasas de parque y 2.500-5.500 USD con operador (guía y porteadores obligatorios por ley), es decir entre 7.500 y 16.000 USD para tres personas. Es el gasto único mayor de todo el viaje africano. Alternativas reales: el monte Meru (3-4 días, tasa de 59 USD/persona/día en vez de 70 + acampada), o ninguna cumbre y quedarse con el Ol Doinyo Lengai, que es una ascensión extraordinaria y cuesta unos 100 USD de guía.",
        "Dron: dar el dron por inutilizable en Tanzania. Registro de unos 100 USD en la TCAA, licencia de piloto de unos 200 USD con exámenes, permiso previo para extranjeros, aprobación del Ministerio de Defensa y PROHIBICIÓN de volar sobre parques nacionales. No intentar introducirlo sin papeles.",
        "Temporada: el corredor interior tiene ventanas en conflicto. Las pistas del oeste (Katavi, Kigoma) y los accesos a Ruaha y Nyerere solo son fiables en seco (junio-octubre); la gran migración del Serengeti está en el sur en enero-marzo y salta al Mara en julio-septiembre; Kitulo florece de noviembre a abril, justo cuando las pistas empeoran; y el lago Natron es más tolerable de junio a agosto pero tiene más flamencos en diciembre-enero. Imposible tenerlo todo: elegir.",
        "Seguridad poselectoral: las elecciones de octubre de 2025 derivaron en protestas y una represión con un número de víctimas en disputa (de 10 confirmadas por la ONU a más de 500 según la BBC y 518 según una comisión gubernamental de abril de 2026), apagón total de internet durante cinco días y disturbios con efecto en el paso fronterizo de Namanga. Revalidar la situación política y la recomendación del MAEC 30 días antes y de nuevo 72 h antes de cada frontera.",
    ],
    ruta_intro=("Dos travesías completamente distintas del mismo país. El <strong>corredor interior</strong> sube de suroeste a noreste, "
                "de Tunduma a Namanga: unos 3.000 km sin el bucle del oeste (14-16 días de conducción pura, y realistamente 30-40 días con "
                "los parques, las cumbres y los días de descanso), o unos 5.000 km si se añade el bucle del oeste. El <strong>corredor costero</strong> "
                "baja de Horohoro a Mtwara: unos 1.700 km (7-8 días de conducción, 18-25 días con Zanzíbar, Nyerere y Kilwa). "
                "Etapas calculadas sobre una media de <strong>250 km/día</strong>."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        # --- INTERIOR ---
        ("Interior 1 · Entrada y altiplano del sur", "Tunduma/Nakonde → Mbeya → lago Ngozi → Tukuyu", "~230 km · 2-3 días"),
        ("Interior 2 · El jardín de Dios", "Mbeya → Parque Nacional de Kitulo (y vuelta)", "~220 km ida y vuelta · 2-3 días a pie"),
        ("Interior 3 (opcional) · Bucle del oeste salvaje", "Mbeya → Sumbawanga → Mpanda/Katavi → Kigoma y Ujiji → Mahale (barco) → vuelta por Mpanda", "~2.100 km ida y vuelta · 10-14 días, grava y barco"),
        ("Interior 4 · Subida a Iringa", "Mbeya → Makambako → Iringa", "~320 km · 2 días"),
        ("Interior 5 · El mayor parque del país", "Iringa → Ruaha (Msembe) y vuelta", "~260 km ida y vuelta · 3-4 días"),
        ("Interior 6 · Cascadas y bosque del Arco Oriental", "Iringa → Mikumi → Udzungwa (Mang'ula): Sanje y vuelta", "~700 km ida y vuelta · 3-4 días"),
        ("Interior 7 · Edad de Piedra e Iringa", "Isimila (20 km de Iringa) y roca de Gangilonga", "~50 km · ½-1 día"),
        ("Interior 8 · Travesía central", "Iringa → Dodoma → Babati", "~500 km · 2-3 días"),
        ("Interior 9 · Baobabs y Rift", "Babati → Tarangire → Mto wa Mbu → lago Manyara → Karatu", "~280 km · 3-4 días"),
        ("Interior 10 · Cráter y origen humano", "Karatu → Loduare → cráter del Ngorongoro → garganta de Olduvai", "~120 km · 2-3 días"),
        ("Interior 11 · La llanura infinita", "Olduvai → Naabi Hill → Seronera (Serengeti) y norte", "~200 km · 3-4 días"),
        ("Interior 12 · Hacia el lago rojo", "Serengeti (Klein's Gate) → Wasso/Sonjo → lago Natron (Engare Sero)", "~220 km de pista · 2 días"),
        ("Interior 13 · La montaña de Dios", "Engare Sero → ascensión nocturna al Ol Doinyo Lengai → cascada de Engare Sero", "in situ · 2 días"),
        ("Interior 14 · Hacia Arusha", "Lago Natron → Longido → Arusha (o por Engaruka y Mto wa Mbu)", "~240 km · 2 días"),
        ("Interior 15 (opcional) · Cumbres", "Arusha → monte Meru (3-4 días) y/o Moshi/Marangu → Kilimanjaro (6-9 días)", "~260 km ida y vuelta · 4-13 días"),
        ("Interior 16 · Salida a Kenia", "Arusha → Namanga (frontera, junto a Amboseli)", "~110 km · 1 día"),
        # --- COSTA ---
        ("Costa 1 · Entrada y Tanga", "Horohoro/Lunga Lunga → Tanga → cuevas de Amboni → manantiales de Galanos", "~80 km · 2 días"),
        ("Costa 2 · Montes Usambara", "Tanga → Muheza → Mombo → Lushoto (Irente, travesía a Mtae/Mambo)", "~200 km · 3-4 días a pie"),
        ("Costa 3 · Costa suajili norte", "Lushoto → Korogwe → Pangani (ferry del río) → Saadani", "~290 km · 3-4 días"),
        ("Costa 4 · Deja aquí tu corazón", "Saadani → Bagamoyo y ruinas de Kaole → Dar es Salaam", "~190 km · 2-3 días"),
        ("Costa 5 (opcional) · Zanzíbar", "Dar → ferry → Stone Town y la isla → vuelta a Dar (sin vehículo ni perro)", "ferry 2 h · 3-4 días"),
        ("Costa 6 · El mayor parque de África", "Dar → Kibiti → Mloka → Nyerere (Mtemere): safari en barca por el Rufiji", "~500 km ida y vuelta · 4-5 días"),
        ("Costa 7 · La ciudad de Ibn Battuta", "Nyerere → Ikwiriri → Kilwa Masoko → Kilwa Kisiwani y Songo Mnara (dhow)", "~300 km · 3 días"),
        ("Costa 8 · Extremo sur", "Kilwa → Lindi → Mtwara y Mikindani → meseta makonde y Msimbati", "~330 km · 3 días"),
        ("Costa 9 · Salida a Mozambique (decisión)", "Opción A: Mtwara → Kilambo (ferry del Rovuma, 40 km) · Opción B: Mtwara → Masasi → Mtambaswala (puente de la Unidad, 180 km)", "40 o 300 km · 1-2 días"),
    ],
    offroad=[
        "Pista del oeste a Katavi y Kigoma (bucle opcional del interior): EL tramo 4x4 grande de Tanzania. Desde Mbeya por Sumbawanga hasta Mpanda y Katavi, y de ahí a Kigoma, son centenares de kilómetros de grava de calidad muy variable. Los overlanders de Tracks4Africa describen la B8 sur entre Mpanda y Kapili como «un poco corrugada, pero nada comparado con las carreteras de entrada al Serengeti o a Mana Pools», con medias de 50-60 km/h; y la ruta de montaña de Kigoma a Mwese como 45 km de pista técnica con roca que exige 4x4 con reductora y se tarda 3 horas y media en recorrer. Solo en temporada seca, con depósitos y garrafas llenos desde Sumbawanga o Mpanda, y con tsé-tsé como factor real (decisivo con el perro).",
        "Acceso al lago Natron: la bajada al Rift. Dos opciones, las dos de grava. Desde Mto wa Mbu por Engaruka, unas 2,5 horas, con los últimos 20 km cada vez más rotos; o desde Longido por Oldonyosambu y Engare Nanyuki, unas 7 horas de asfalto secundario y grava de todo tiempo, más escénica. Viniendo del Serengeti por Klein's Gate son 4-5 horas de grava por Wasso y Sonjo. Polvo, piedra volcánica suelta y vados secos: el acceso 4x4 más bonito del corredor interior.",
        "Descenso al cráter del Ngorongoro: pista empinada de tierra y roca por la pared de la caldera, con sentidos únicos señalizados para bajar y subir, y fondo de cráter con pistas bien mantenidas. Tracción 4x4 exigida por la autoridad del parque, ranger obligatorio de 40 USD en efectivo a bordo, 25 km/h de límite y salida antes de las 18:00. No es técnico pero no admite improvisación.",
        "Pistas del Serengeti: roca y corrugado permanente donde rara vez se pasa de 25-40 km/h; los propios operadores las citan como la referencia de mal firme del país. Prohibido salir de pista. Del cráter a Naabi Hill, 85 km en 2-3 horas; de ahí a Seronera, otro tanto. Llevar dos ruedas de repuesto por vehículo y revisar suspensión antes de entrar.",
        "Acceso a Ruaha: unos 130 km de pista desde Iringa hasta la puerta de Msembe, y después pistas internas de arena y vados del Gran Ruaha. Con 35,40 USD de tasa por persona es el safari grande más barato del país: el esfuerzo de la pista se compensa.",
        "Acceso a Nyerere/Mtemere (costa): desde Dar por Kibiti hasta Mloka, con los últimos 80-100 km de pista que se degrada mucho en lluvias. En seco es asumible con 4x4 estándar; en lluvias hay tramos que se cierran. Alternativa por Morogoro hasta la puerta de Matambwe.",
        "T6 al sur, hacia Mtwara: la carretera del extremo sur está recién mejorada y los overlanders la describen como ancha, con arcenes y «relajada» comparada con otras rutas tanzanas — buena noticia, porque era el tramo que más dudas daba. Lo que sigue siendo pista es el desvío de Masasi al puente de la Unidad y los accesos a la meseta makonde y a Msimbati.",
        "Ferry del río Pangani y pista de la costa a Saadani: el cruce del Pangani se hace en una barcaza local y el tramo de Pangani a Saadani y a Bagamoyo es pista de arena costera con tramos de barro negro en lluvias. Es el trozo más bonito de la costa norte y el que más se parece a conducir por la playa.",
        "Acceso a Kitulo: pista de montaña desde Chimala (la célebre «carretera de las 57 curvas», Chimala Escarpment Road) o desde Mbeya por Isyonje: grava de altura que se vuelve resbaladiza con la niebla y la lluvia del altiplano.",
    ],
    senderismo=[
        "Ol Doinyo Lengai (2.962 m), lago Natron — LA gran excursión nocturna de Tanzania y la más dura de la ficha. Salida hacia medianoche para llegar al cráter con el amanecer: 11,2 km ida y vuelta con 1.600 m de desnivel concentrados en 5 km, es decir unos 400 m de subida por kilómetro, sobre roca suelta y resbaladiza, en 6-10 horas. Guía masái obligatorio (unos 100 USD por persona según relatos recientes) y 4x4 para llegar al inicio. Es el único volcán del mundo que emite natrocarbonatita, una lava fría y negra que de noche brilla. No es un paseo: hay que llegar en forma y con frontal, guantes y calzado de suela rígida. El perro NO puede subir: se queda en el camping con un viajero.",
        "Monte Meru (4.562 m), Parque Nacional de Arusha — la alternativa seria al Kilimanjaro. 3-4 días por la cresta de un estratovolcán con el cráter abierto por un colapso, durmiendo en refugios (Miriakamba y Saddle Hut), con ranger armado obligatorio porque en la base hay búfalo, elefante y jirafa, y una cresta final estrecha sobre el cráter con el Kilimanjaro de frente al amanecer. Tasa de parque de 59 USD/persona/día, muy por debajo del Kilimanjaro. Segunda cumbre de Tanzania y quinta de África.",
        "Kilimanjaro (5.895 m) — 5 a 10 días según ruta (Marangu con refugios, Machame, Lemosho, Rongai, Umbwe), guía y porteadores obligatorios por ley, y un coste real que lo convierte en una decisión de presupuesto más que de senderismo: 70 USD/persona/día de conservación + 50/noche de acampada (o 60 en refugio) + 10 de tasa forestal + 20 de rescate, todo con 18 % de IVA, y 2.500-5.500 USD por persona con operador. Si no entra: caminata de un día a la puerta de Marangu, las cascadas y las cuevas de Marangu, y la ruta de los pueblos chagga, todo fuera del parque.",
        "Cascadas de Sanje, Udzungwa Mountains — 170 m de salto en tres niveles, con poza para bañarse en el nivel intermedio. 5-6 horas ida y vuelta desde la puerta de Mang'ula con guía obligatorio, subiendo por bosque de montaña con colobos rojos de Iringa y mangabeyes de Sanje. Variantes: las cataratas del príncipe Bernhard (más corta) y la travesía de 2 días a la meseta de Mwanihana. El único parque de Tanzania que se recorre solo a pie.",
        "Travesías de los montes Usambara occidentales (Lushoto) — LA mejor zona de senderismo libre del país y, además, compatible con el perro porque no es parque nacional. Red de caminos entre aldeas, plantaciones de té y bosque nuboso, con programas de turismo cultural comunitario que organizan guías y alojamiento en casas de pueblo: medio día al mirador de IRENTE (cortado de 1.000 m sobre la llanura de Mazinde), bosque de Magamba, y travesías de 2-4 días de Lushoto a Mtae o a Mambo. Clima fresco, muy agradecido después de la costa.",
        "Parque Nacional de Kitulo — 412 km² de pradera a 2.600 m que se recorren a pie, con caminatas libres por la meseta, ascensión a cerros con vistas al lago Malaui y a la playa de Matema, y 350 especies de flor silvestre incluidas 45 orquídeas endémicas. Floración de noviembre a abril; septiembre-noviembre es el mejor compromiso para caminar. El perro no entra (es TANAPA).",
        "Cráter del lago Ngozi (Poroto, Mbeya) — media hora de subida por bosque de montaña hasta el borde de la caldera y un descenso empinado opcional hasta la orilla del lago. Corto, fácil, gratis, fuera de parque y por tanto apto para el perro con correa: la primera caminata del país al entrar desde Zambia. Cortados y desprendimientos en parte del perímetro: no dar la vuelta completa sin guía.",
        "Garganta de Olduvai — visitas guiadas a pie al fondo de la garganta desde el museo del borde, sobre las capas de sedimento donde aparecieron Paranthropus boisei y Homo habilis. No es una caminata exigente, es una caminata que cambia la perspectiva.",
        "Pilares de Isimila (Iringa) — un par de horas entre el bosque de pilares de arenisca esculpidos por la erosión y el yacimiento achelense, con guía local. Fuera de parque: el perro puede ir.",
        "Cuevas de Amboni (Tanga) — recorrido guiado por el mayor sistema de cuevas calizas de África oriental; tramos estrechos y murciélagos, consultar con el guía si se va con perro.",
    ],
    acampada=[
        "Karatu (puerta del Ngorongoro): la base logística del circuito norte para autoconductores, con campings orientados a overlanders, talleres, supermercado, cajeros y combustible. ES ADEMÁS LA BASE DEL PLAN DEL PERRO: aquí se queda uno de los tres viajeros con él mientras los otros dos bajan al cráter.",
        "Simba A, borde del cráter del Ngorongoro: camping público de la NCAA, la opción económica dentro del área (35,40 USD/persona/noche). Frío y viento en el borde a 2.300 m; elefantes y búfalos entran por la noche.",
        "Seronera y otros campings públicos del Serengeti: 35,40 USD/persona/noche, sin vallas y con fauna alrededor; los campings especiales cuestan 59 USD/persona/noche. Reservar con margen en temporada de migración.",
        "Engare Sero (lago Natron): campings comunitarios gestionados por las aldeas masái, 17-24 USD por noche, con sombrajos y duchas básicas; es el mejor vivac del corredor interior y admite perro. Pagar las tasas de aldea en el pueblo.",
        "Jakobsen Beach (Kigoma): camping privado en una cala del lago Tanganyika con agua a 26 °C, el punto de referencia de los overlanders en el oeste.",
        "Sitalike (puerta de Katavi) y Mang'ula (puerta de Udzungwa): campings y guest houses sencillos a la entrada de cada parque, útiles también como base para el turno del perro.",
        "Lushoto y los pueblos de los Usambara: casas de huéspedes comunitarias y sitios para acampar asociados a los programas de turismo cultural; frío de montaña por la noche.",
        "Pangani y la costa de Ushongo: campings y bandas sencillos sobre playas prácticamente vacías; el mejor sitio de la costa para parar varios días con el perro.",
        "Kilwa Beach Lodge (Kilwa Masoko): camping en la playa por unos 10 USD por persona, con sombrajo y baños limpios, y punto donde se organiza el dhow a Kilwa Kisiwani.",
        "Dar es Salaam: sin acampada práctica en el centro; alojamientos con parking vigilado en Msasani y la península, que son además la opción para dejar perro y vehículos durante Zanzíbar.",
        "Arusha y Usa River: campings de overlanders y lodges con parcela; base para los bloques largos (Meru, Kilimanjaro) y para el cuidado del perro.",
    ],
    visado=[
        "e-Visa obligatoria para ciudadanos españoles (no exentos): visado ordinario de turismo 50 USD, validez de hasta 90 días, tramitación de hasta 10 días hábiles según la guía oficial de Inmigración. Solicitar online en visa.immigration.go.tz con semanas de antelación.",
        "SE ENTRA DOS VECES: valorar el visado de entrada múltiple (100 USD, hasta 12 meses, con estancias de 90 días como máximo por visita) frente a dos e-Visa de entrada única. Comprobar expresamente la elegibilidad para pasaportes españoles, porque la entrada múltiple aparece reservada a categorías concretas en la guía oficial.",
        "Confirmar que el e-Visa es válido en los puestos terrestres CONCRETOS que vamos a usar: Tunduma (desde Zambia) y Horohoro (desde Kenia). El visado a la llegada existe como respaldo para la mayoría de nacionalidades, pero no conviene depender de él en un paso con mucho camión.",
        "Tanzania exige mostrar billete de salida en el punto de entrada: preparar documentación del viaje overland (itinerario, documentación de los vehículos, seguros) para justificar la salida por tierra.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica: aplica viniendo de Zambia y, en la bajada, de Kenia. Llevarlo siempre encima.",
        "Zanzíbar tiene control de entrada propio y sella el pasaporte aunque no sea frontera internacional: llevar pasaporte incluso para el ferry de pasajeros.",
    ],
    fronteras_rows=[
        ("Entrada interior", "Tunduma/Nakonde (Zambia)", "Gran paso del corredor TANZAM, ventanilla única, mucho camión y gestores informales. Llegar temprano. Aquí: visado, TIP o sellado del CPD, tasa de carretera (~25 USD/mes/vehículo) y seguro de terceros si no se lleva Tarjeta Amarilla COMESA."),
        ("Salida interior", "Namanga (Kenia)", "Paso principal del corredor norte junto a Amboseli, de alto tránsito turístico. Sufrió cierres y disturbios en noviembre de 2025: confirmar normalidad 72 h antes. Obtener sello de salida del vehículo y devolver el TIP."),
        ("Entrada costa", "Horohoro/Lunga Lunga (Kenia)", "Paso COSTERO sobre la A14 Mombasa-Dar, distinto del de subida: ventanilla única moderna en un solo edificio, abierto 24 h, asfalto bueno, combustible a 1 km, 4G. Espera normal 15-30 min; punta de 7 a 10 h. Nuevo TIP y nueva tasa de carretera: pedir justificante (hay relatos de cobros duplicados)."),
        ("Salida costa · opción A", "Kilambo/Namoto (Mozambique), ferry del Rovuma", "NO es un puente: barcaza para ~6 vehículos 4x4 sobre la desembocadura del Rovuma, a 40 km de Mtwara, dependiente de marea (mínimo 3 m de agua) y con horario tanzano muy restringido. Deja en el norte de Cabo Delgado, zona donde las fuentes especializadas recomiendan NO entrar por la insurgencia. Coordenada aproximada."),
        ("Salida costa · opción B", "Mtambaswala/Negomano (Mozambique), puente de la Unidad", "El verdadero puente de la Unidad (720 m, 18 vanos, inaugurado el 12 de mayo de 2010), pero 180 km tierra adentro vía Masasi, no junto a Mtwara. Alternativa terrestre seria al ferry. Confirmar 60 días antes que emite visado y despacha vehículos particulares, y revisar la seguridad del corredor de Negomano."),
    ],
    vehiculos=[
        "CPD: llevarlo en regla y con todos los pares de sellos. La práctica en frontera es contradictoria — hay relatos de agentes que lo exigen como obligatorio para vehículos extranjeros y otros que emiten un permiso temporal de importación (TIP) de hasta tres meses sin él. Ir con CPD y saber que el TIP existe como alternativa, no al revés.",
        "Tasa de carretera para vehículo extranjero: unos 25 USD por vehículo y mes según relatos recientes, que se paga en el banco de la frontera. Se vuelve a pagar al reentrar en la bajada por la costa; guardar justificantes, porque hay casos documentados de cobro duplicado en Namanga.",
        "Seguro de responsabilidad civil: Tanzania es miembro de COMESA, así que la Tarjeta Amarilla COMESA sirve; si no se lleva, contratar seguro local en el propio puesto fronterizo.",
        "Permiso de conducir: el carnet nacional se acepta en los controles según las fuentes de autoconducción del país, pero llevar también el permiso internacional — no cuesta nada y evita discusiones.",
        "Dentro de los parques: 4x4 exigido en el Ngorongoro y recomendable en todos los demás; prohibido salir de pista, prohibido conducir de noche (puertas de 06:00 a 18:00) y límites de 50 km/h (25 en el Ngorongoro, 35 según otras fuentes). Dos ruedas de repuesto por vehículo antes del Serengeti.",
        "Tasas de vehículo en parques: las cifras públicas que hemos encontrado (10-20 USD/día) corresponden a vehículos con matrícula tanzana — la tarifa para vehículo EXTRANJERO en parques TANAPA no está confirmada y puede ser mucho mayor. Sí está confirmada la del Ngorongoro, por peso: 47,20 USD hasta 2.000 kg, 177 USD de 2.001 a 3.000 kg y 236 USD de 3.001 a 7.000 kg. Pesar Grenadier y Delica antes de presupuestar.",
        "Ferry de vehículos a Zanzíbar: es un ferry de CARGA distinto del rápido de pasajeros, con trámite y precio aparte. Nuestra recomendación es no llevar los vehículos a la isla.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Registro del dron ante la TCAA (unos 100 USD) con prueba de propiedad, antes de cualquier intento de vuelo.",
        "Licencia de piloto para categorías 2 y 3 (unos 200 USD): 21 años, certificado médico, inglés, licencia de radiotelefonía, formación y exámenes. Inviable de improvisar.",
        "Visitantes extranjeros: permiso previo de la TCAA, acreditación del país de origen y, en la práctica, aprobación del Ministerio de Defensa. Drones de más de 7 kg requieren aprobación militar explícita.",
        "PROHIBIDO volar sobre parques nacionales. TANAPA exige además un permiso propio de pago que rara vez se concede a particulares: no intentarlo en Serengeti, Ngorongoro, Kilimanjaro ni ningún otro.",
        "Altura máxima 121 m, visual directa obligatoria, prohibido de noche, 3 km de aeropuertos domésticos y 5 km de internacionales, prohibido sobre multitudes sin permiso.",
        "Decisión recomendada del proyecto: dejar el dron guardado y precintado durante todo el paso por Tanzania, declarándolo si se pregunta, o no entrarlo en el país.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado a mediados de 2026: licencia solicitada y preseleccionada por la TCRA, cobertura parcial vía acuerdo directo-a-dispositivo con Airtel Africa, sin servicio residencial pleno. Tanzania figura como «previsto durante 2026», igual que Uganda, Angola y Namibia.",
        "Contraste regional: Kenia, Zambia, Mozambique y Malaui ya están activos. Tanzania es el único hueco del bucle — planificar la desconexión, no la conexión.",
        "SIM local (Vodacom, Airtel Tanzania, Halotel) como conectividad principal; cobertura razonable en el eje central y la costa, escasa en el oeste, en Natron y dentro de los parques.",
        "Riesgo político añadido: en 2025 hubo un apagón total de internet de unos cinco días y restricciones posteriores a redes sociales. No depender de una sola vía: llevar alternativa satelital de mensajería (InReach o similar) para el corredor interior.",
    ],
    perro_intro=[
        "PERMISO DE IMPORTACIÓN PREVIO, no se resuelve en frontera: lo emite el Director de Servicios Veterinarios (oficina veterinaria de Temeke, Dar es Salaam; zoosanitary@mifugo.go.tz, +255 22 2862592), con carta de solicitud indicando raza, edad y PUERTO DE ENTRADA PREVISTO, certificado de vacunación antirrábica (administrada entre 30 días y 3 años antes según validez de la vacuna) y una tasa de 30.000 TSh, más 20.000 TSh al sacarlo del país.",
        "Certificado veterinario internacional expedido o endosado por veterinario oficial dentro de los 14 días previos a la entrada, además de las vacunas DHLP recomendadas y las copias del historial del animal.",
        "CONTRADICCIÓN SIN RESOLVER Y BLOQUEANTE: PetTravel afirma que las mascotas solo pueden entrar en Tanzania por vía aérea por los aeropuertos de Dar es Salaam o Kilimanjaro, mientras la vía consular habla de indicar el puerto de entrada previsto sin restringirlo a aeropuertos. Hay que obtener confirmación POR ESCRITO del Director de Servicios Veterinarios citando Tunduma y Horohoro antes de salir de Europa. Si la entrada terrestre con perro no fuera posible, cae toda la arquitectura del bucle.",
        "Dentro del país: prohibido en todos los parques nacionales de TANAPA y en el Área de Conservación del Ngorongoro. La excepción buena es el lago Natron, que es área comunitaria. Ver la matriz por zonas.",
        "Contacto sanitario y posible cuidado: clínica y refugio Mbwa Wa Africa, Usa River (Arusha), +255 627 593 149 — confirmar por escrito si aceptan alojar un perro viajero antes de contar con ello.",
        "Riesgo sanitario específico: la mosca tsé-tsé del oeste (Katavi, Kigoma) y de algunos parques transmite tripanosomiasis, a menudo mortal en perros y sin profilaxis fiable. Consultar con el veterinario antes de decidir el bucle del oeste.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en todo el territorio por debajo de 1.800 m, incluidas la costa y Zanzíbar, y con transmisión durante todo el año: profilaxis a valorar con Sanidad Exterior. Las zonas altas (Kitulo, Usambara, Arusha, Ngorongoro) tienen riesgo mucho menor.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica (aplica viniendo de Zambia y de Kenia). Llevarlo siempre encima, no en el fondo del vehículo.",
        "Bilharzia (esquistosomiasis) en el lago Tanganyika y en los remansos del Rufiji, el Ruaha y el Pangani: no bañarse en agua dulce estancada; las pozas de Sanje y de Ngozi se consideran de bajo riesgo pero preguntar en cada sitio.",
        "Altura: el Kilimanjaro y el Meru exigen aclimatación real (hay casos graves de mal de altura todos los años en el Kilimanjaro, y las rutas cortas son las más peligrosas precisamente por eso). El Ol Doinyo Lengai, a 2.962 m, no plantea problema de altura pero sí de esfuerzo y calor.",
        "Calor extremo en el lago Natron y en toda la costa sur: 5-6 litros de agua por persona y día, sales, sombra artificial.",
        "Referencias hospitalarias: Muhimbili (Dar es Salaam) a nivel nacional, clínicas privadas de Arusha para el corredor interior y el circuito norte, hospital zonal de Mbeya en el sur. Seguro con EVACUACIÓN MÉDICA AÉREA imprescindible: desde el Serengeti, Katavi, Mahale o Nyerere no hay otra salida rápida.",
    ],
    seguridad_intro=("Tanzania fue durante décadas uno de los países más estables de África, sin conflictos internos activos, y la delincuencia que afecta al viajero es sobre todo oportunista. "
                     "Eso cambió de grado en octubre-noviembre de 2025: las elecciones generales y su represión abrieron la crisis política más grave de la historia del país, con protestas en Dar es Salaam, Arusha y Mwanza, un número de víctimas en disputa, apagón total de internet durante cinco días y afectación del paso fronterizo de Namanga. "
                     "Nada indica hoy una zona excluida de nuestro itinerario, pero esta ficha debe revalidarse políticamente antes de entrar, no solo logísticamente."),
    seguridad=[
        "Revalidar la situación política y la recomendación de viaje del MAEC 30 días antes de cada entrada y de nuevo 72 h antes de cada frontera. Evitar concentraciones, manifestaciones y fotografiar despliegues policiales; tener plan B de comunicación por si hay restricciones de internet.",
        "Frontera de Namanga: sufrió cierres y disturbios en noviembre de 2025 con efecto en el comercio regional. Confirmar que está operativa antes de comprometer el calendario de salida hacia Kenia.",
        "Sur del país hacia Mozambique: Tanzania está tranquila, pero el otro lado de la frontera (norte de Cabo Delgado: Palma, Mocímboa da Praia, Quionga) sufre una insurgencia activa y las fuentes especializadas recomiendan expresamente no entrar por el ferry de Kilambo. Esta es la decisión de seguridad más importante del tramo.",
        "Delincuencia oportunista en Dar es Salaam, Arusha, Stone Town y Mwanza: robos de bolsos y cámaras, tirones desde moto. Parking vigilado siempre, nada de valor a la vista en el vehículo, no caminar de noche por el paseo marítimo de Dar.",
        "Carretera: no conducir de noche (lo recomiendan expresamente las propias guías de autoconducción del país, por baches invisibles y luces largas de frente). Badenes sin señalizar, camiones en el corredor TANZAM y en la A14 costera, y radares con multa por ingreso bancario. Límites: 80 km/h en carretera, 40 en poblado, 25-50 en parques.",
        "Controles de la policía de tráfico (uniforme blanco), frecuentes y en general correctos: revisan seguro, neumáticos y permiso. Trato educado, documentación a mano y copias.",
        "Fauna: respetar distancias y las indicaciones del ranger; búfalo y elefante en los campings del Ngorongoro, del Serengeti y en la base del Meru. Hipopótamos y cocodrilos en el Rufiji, el Ruaha y el Pangani. De noche, perro dentro del vehículo en cualquier punto del corredor.",
        "Aislamiento real en el bucle del oeste (Sumbawanga-Mpanda-Kigoma) y en el lago Natron: sin cobertura fiable, sin Starlink y sin suministro. Avisar del itinerario y llevar reservas de agua, combustible y comida.",
    ],
    agua=[
        "Arusha, Dar es Salaam, Mbeya, Iringa, Dodoma y Tanga: agua embotellada sin problema en supermercados.",
        "Recarga de depósito de uso general: campings de overlanders de Karatu y Arusha, lodges de la costa, campings de Kilwa y Pangani y hoteles de las ciudades permiten llenar con manguera; confirmar en recepción.",
        "Campings públicos del Ngorongoro (Simba) y del Serengeti (Seronera): tienen agua corriente y aseos, pero el suministro es irregular y no potable sin tratar. Entrar al circuito norte con los depósitos al 100 % desde Karatu.",
        "Lago Natron: agua escasa y calor extremo — 5-6 litros por persona y día, y el perro aparte. Salir lleno de Mto wa Mbu o Longido.",
        "Bucle del oeste (Sumbawanga-Mpanda-Katavi-Kigoma): sin recarga fiable fuera de las ciudades. Filtro y depósitos llenos.",
        "Filtrar y tratar siempre el agua de ríos y pozas, por clara que parezca (bilharzia en el Tanganyika y en los remansos del Rufiji, el Ruaha y el Pangani).",
    ],
    combustible=[
        "Corredor interior, sin gaps graves en el eje principal: Tunduma → Mbeya (~110 km) → Makambako → Iringa (~320 km) → Dodoma (~270 km) → Babati → Arusha, todos con estaciones formales (TotalEnergies, Puma, Oryx). Karatu es el último suministro de confianza antes del circuito Ngorongoro-Serengeti.",
        "Tramos sin garantía del interior: los 130 km de pista Iringa-Ruaha y las pistas internas del parque; el desvío al lago Natron (desde Mto wa Mbu o Longido no hay nada hasta Engare Sero); y el circuito Ngorongoro-Olduvai-Serengeti-Klein's Gate-Natron, que puede sumar 600-800 km sin una estación fiable. Entrar con depósitos y garrafas llenos.",
        "Bucle del oeste: Sumbawanga y Mpanda son las únicas plazas fiables entre Mbeya y Kigoma. Sitalike, a la puerta de Katavi, no garantiza nada. Autonomía completa obligatoria.",
        "Corredor costero: estaciones formales en Tanga, Muheza, Korogwe, Bagamoyo, Dar es Salaam, Kibiti, Ikwiriri, Kilwa Masoko, Lindi y Mtwara. El único gap real es el acceso a Nyerere/Mtemere (80-100 km de pista sin suministro) y los desvíos de la meseta makonde y de Masasi al puente de la Unidad.",
        "Calidad: aceptable en las estaciones de marca de las ciudades, irregular en el oeste y en los pueblos de pista. Llevar embudo con filtro como en Angola.",
    ],
    experiencias_intro=("Relatos y datos reales de otros overlanders sobre Tanzania, que es donde más diverge la información oficial de lo que pasa en la frontera y en la pista. "
                        "Especialmente relevantes para nosotros: el estado de las pistas del oeste, lo que se paga de verdad en Tunduma y Namanga, el lío del permiso del perro y la frontera sur hacia Mozambique:"),
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("PERRO · entrada terrestre", "BLOQUEANTE. Obtener confirmación POR ESCRITO del Director de Servicios Veterinarios (zoosanitary@mifugo.go.tz) de que el perro puede entrar por Tunduma y por Horohoro, y no solo por los aeropuertos de Dar o Kilimanjaro como afirma PetTravel. Tramitar el permiso de importación con el puerto de entrada indicado. Resolver antes de salir de Europa."),
        ("Salida hacia Mozambique", "Decidir entre el ferry de Kilambo (40 km de Mtwara, dependiente de marea, con el lado mozambiqueño bajo insurgencia y recomendación expresa de no usarlo) y el puente de la Unidad de Mtambaswala/Negomano (180 km tierra adentro vía Masasi). Coordinar con la ficha de Mozambique y confirmar que el puesto elegido emite visado y despacha vehículos particulares."),
        ("Presupuesto de parques", "Cerrar la lista definitiva de parques y días ANTES del viaje y presupuestarla: el corredor interior puede pasar fácilmente de 4.000-6.000 USD en tasas para 3 personas y 2 vehículos. Decidir qué se ve de verdad y qué se ve desde fuera."),
        ("Tasa de vehículo extranjero en TANAPA", "Sin confirmar. Las cifras públicas (10-20 USD/día) son para matrícula tanzana. Pedir a TANAPA la tarifa para vehículo extranjero por peso, y pesar el Grenadier y la Delica (en el Ngorongoro la diferencia entre la banda de 2.001-3.000 kg y la de 3.001-7.000 kg es de 177 a 236 USD por vehículo y entrada)."),
        ("Kilimanjaro · decisión", "Decidir si se sube (7.500-16.000 USD para tres personas con operador), si se sustituye por el monte Meru (3-4 días, tasa de 59 USD/persona/día) o si se renuncia a ambos y se queda el Ol Doinyo Lengai. Es el gasto único mayor de todo el viaje africano."),
        ("Bucle del oeste · decisión", "Decidir si entran los ~2.100 km ida y vuelta por Sumbawanga, Katavi, Kigoma y Mahale (10-14 días, grava, barco caro, tsé-tsé). Es la parte más salvaje del país y la más costosa en días; el perro es un argumento serio en contra por la tripanosomiasis."),
        ("Zanzíbar · decisión", "Decidir si se hace (3-4 días a pie desde Dar, sin vehículos ni perro, con cuidador en Dar) o si se cambia por más días en Kilwa y Saadani. Confirmar si Zanzíbar tiene trámite sanitario propio para animales."),
        ("Cuidado del perro en Arusha y Karatu", "Confirmar por escrito con Mbwa Wa Africa (Usa River) y buscar alternativas en Karatu y Mto wa Mbu: son la base del plan de turnos del circuito norte. Sin esto, el corredor interior se queda sin los parques del norte."),
        ("Visado de doble entrada", "Confirmar si para pasaportes españoles es elegible el visado de entrada múltiple (100 USD) o si hay que tramitar dos e-Visa de entrada única, y que ambos son válidos en Tunduma y Horohoro."),
        ("Permiso del cráter del Ngorongoro", "El permiso no se compra en la puerta: hay que gestionarlo antes a través de un operador. Identificar un operador de Karatu o Arusha que lo tramite para autoconductores y confirmar el procedimiento y el plazo."),
        ("Temporada", "Resolver el conflicto de ventanas: seco para el oeste, Ruaha y Nyerere (junio-octubre); migración del Serengeti en el sur (enero-marzo) o en el Mara (julio-septiembre); floración de Kitulo (noviembre-abril); Natron tolerable (junio-agosto) o con más flamencos (diciembre-enero)."),
        ("Seguridad poselectoral", "Revalidar la situación política 30 días antes de cada entrada y 72 h antes de cada frontera, y confirmar que Namanga está operativa."),
        ("Olduvai · tasa de entrada", "Confirmar el importe y si se cobra aparte de la tasa del Ngorongoro al pasar por la puerta de Loduare."),
        ("Dron", "Decidir si se intenta el registro TCAA (100 USD) + licencia (200 USD) con meses de antelación, o si simplemente no se vuela en Tanzania. Recomendación de esta ficha: no volar."),
        ("Fotos pendientes de sustituir", "Lago Ngozi (imagen de referencia de las Tierras Altas del Sur), Katavi (construcción, no fauna), Mahale (chimpancés de Gombe) y Usambara (vista desde la carretera de Korogwe) usan imágenes de la región o de la especie, no del propio sitio."),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 11 de septiembre de 2026. Ficha reescrita por completo: la versión anterior describía una entrada desde Malaui y solo 4 PDIs, y ya no corresponde a la ruta confirmada. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Dar es Salaam, 24h): (+255) 754 04 21 23 · Embajada de España en Dar es Salaam: (+255) 022 266 60 18/19 · Veterinario de referencia (Arusha/Usa River, Mbwa Wa Africa): (+255) 627 593 149.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

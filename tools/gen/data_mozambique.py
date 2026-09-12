# -*- coding: utf-8 -*-
"""Mozambique — ficha completa (12 sep 2026): travesía norte-sur del bucle, Tanzania -> Zimbabue."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== NORTE-OESTE: entrada desde Tanzania por el Rovuma (Matchedje), meseta del Niassa =====
    dict(n=1, name="Lichinga y la meseta del Niassa", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-13.3128, lon=35.2406,
         desc="Primera plaza con servicios reales tras entrar por el Rovuma: capital de la provincia de Niassa, a 1.300 m sobre una meseta fresca de pinares y plantaciones, con combustible formal, bancos, mercado y hospital provincial. Está a 232 km del puesto de Matchedje, y entre medias NO hay nada: es el primer sitio donde repostar, reabastecer y recuperar cobertura. El clima de altura aquí es un alivio después del calor de la costa tanzana.",
         credit="Wikimedia Commons", source=W + "Lichinga%20-%20Julius%20Nyerere%20street.JPG?width=900"),
    dict(n=2, name="Lago Niassa · Metangula, Cóbuè e islas", cat="Naturaleza", prio="Alta", dog="permitido", time="2–3 noches",
         lat=-12.6892, lon=34.8181,
         desc="La orilla mozambiqueña del LAGO MALAUI (aquí Niassa), el tercer lago más grande de África y el de mayor diversidad de peces del planeta: cientos de especies de cíclidos endémicos en agua transparente, sin bilharzia declarada en las zonas de corriente y con playas de arena entre calas rocosas. Metangula y Cóbuè son pueblos de pescadores con lodges sencillos y camping a pie de agua, y en la reserva de Manda Wilderness hay senderos y comunidades. Es la mejor pernocta del norte con el perro: no es parque nacional, es orilla abierta. Baño excelente, muy poca gente y precios bajos.",
         credit="Wikimedia Commons", source=W + "Lake%20malawi%20mozambico%20coast.jpg?width=900"),
    dict(n=3, name="Reserva Especial de Niassa (EXCLUIDA por seguridad)", cat="Referencia · conflicto", prio="Descartada", dog="irrelevante: no se entra", time="no se visita",
         lat=-12.1667, lon=37.5000,
         desc="ZONA EXCLUIDA. Sobre el papel es la joya: 42.000 km² de miombo virgen a orillas del Lugenda y el Rovuma, uno de los espacios protegidos más grandes de África, con elefantes, licaones y una de las últimas poblaciones grandes de león del continente, y un potencial 4x4 enorme. En la práctica, el Departamento de Estado de EE. UU. la clasifica en NIVEL 4 «NO VIAJAR» por ataques yihadistas a campamentos de caza dentro de la propia reserva, y el FCDO británico desaconseja todo viaje a distritos vecinos de Niassa. Se marca en el mapa precisamente para que quede claro que NO se entra, y para no reinventarla como «desvío tentador» más adelante.",
         credit="Wikimedia Commons", source=W + "Mozambique%20location%20map.svg?width=900"),
    dict(n=4, name="Cuamba y el ferrocarril de Nacala", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-14.8036, lon=36.5372,
         desc="Nudo ferroviario en mitad del interior, donde la línea de Nacala cruza hacia Malaui: uno de los pocos trenes de pasajeros que siguen funcionando en África austral pasa por aquí y sigue siendo la espina dorsal social de toda la región. Mercado grande, combustible y talleres básicos; es el punto de reabastecimiento obligado entre Lichinga y Nampula, un tramo de ~350 km sin nada. Los inselbergs de granito del entorno anuncian el paisaje de Nampula. Imagen: genérica de Mozambique — pendiente de sustituir por una foto de Cuamba.",
         credit="Wikimedia Commons", source=W + "Mozambique%20126.jpg?width=900"),
    dict(n=5, name="Gurué, el monte Namuli y las plantaciones de té", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-15.4667, lon=36.9833,
         desc="El rincón verde y fresco que casi nadie asocia con Mozambique: laderas escalonadas de té a 1.000 m, cascadas, niebla y antiguas casas coloniales de las compañías tealeras. Encima se levanta el MONTE NAMULI (2.419 m), el segundo pico del país, un macizo de granito con bosque de niebla, endemismos propios (varias aves y anfibios que no existen en ningún otro sitio) y una subida de 2 días con guía local desde la aldea de Mucunha. Pistas de tierra hasta las plantaciones, 4x4 recomendado. Imagen: Gurué.",
         credit="Wikimedia Commons", source=W + "Guru%C3%A9%20Mo%C3%A7ambique.jpg?width=900"),
    # ===== COSTA NORTE: Nampula e Ilha de Moçambique =====
    dict(n=6, name="Nampula", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-15.1165, lon=39.2666,
         desc="Tercera ciudad del país y la gran plaza logística de todo el norte: talleres, neumáticos, recambios, supermercados, hospital central y bancos. Rodeada de inselbergs de granito espectaculares y con el Museo Nacional de Etnografía, el mejor del país para entender las culturas makua y makonde. Es el sitio donde revisar los vehículos antes del largo descenso hacia Quelimane y el Zambeze. Imagen: calle de Maputo — pendiente de sustituir por una de Nampula.",
         credit="Wikimedia Commons", source=W + "2010-10-18%2010-55-38%20Mozambique%20Maputo%20Chamanculo%20%E2%80%9DB%E2%80%9D.jpg?width=900"),
    dict(n=7, name="Ilha de Moçambique (Patrimonio de la Humanidad)", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-15.0347, lon=40.7358,
         desc="EL GRAN IMPRESCINDIBLE DEL NORTE. Una isla de coral de 3 km por 500 m, unida al continente por un puente de un solo carril de 3,8 km, que fue capital de todo el África Oriental Portuguesa durante casi cuatro siglos. Patrimonio de la Humanidad desde 1991: la Fortaleza de São Sebastião (1558-1620), la capilla de Nossa Senhora do Baluarte (1522), la más antigua del hemisferio sur; la Cidade de Pedra e Cal de casonas swahili-portuguesas medio en ruinas y la Cidade de Macuti de casas de palma al otro extremo. Se recorre entera a pie en un día, no hace falta mover el coche. El puente es de un solo carril con paso alternado: comprobar antes limitaciones de peso y ancho con los vehículos cargados (por confirmar).",
         credit="Wikimedia Commons", source=W + "Forte%20de%20S%C3%A3o%20Sebasti%C3%A3o%20-%20Igreja.jpg?width=900"),
    dict(n=8, name="Chocas-Mar, las Cabaceiras y la bahía de Mossuril", cat="Costa", prio="Alta", dog="permitido", time="2 noches",
         lat=-14.9667, lon=40.6167,
         desc="Justo enfrente de Ilha, al otro lado de la bahía, un rosario de playas de arena blanca y manglares al que se llega por PISTAS DE ARENA entre cocoteros: Chocas-Mar, Cabaceira Pequena y Cabaceira Grande, con la iglesia portuguesa del siglo XVII más antigua del hemisferio sur y cisternas coloniales todavía en uso. Es el sitio evidente para acampar y dejar suelto al perro tras la disciplina de la isla: playa abierta, sin parque nacional de por medio y prácticamente sin turismo. Con marea baja se puede cruzar a pie parte de los bancos de arena; con marea alta, no. Acceso 4x4 real, arena blanda en los últimos kilómetros.",
         credit="Wikimedia Commons", source=W + "Sand%20Rd%20(4x4%20requied)%2C%20Mozambique%20-%20panoramio%20(1).jpg?width=900"),
    dict(n=9, name="Pemba y el archipiélago de las Quirimbas (EXCLUIDOS)", cat="Referencia · conflicto", prio="Descartada", dog="irrelevante: no se entra", time="no se visita",
         lat=-12.9740, lon=40.5178,
         desc="ZONA EXCLUIDA. Pemba, la bahía natural más grande de África después de Sídney, la isla de Ibo con sus tres fuertes portugueses y el archipiélago de las Quirimbas serían, sin el conflicto, dos semanas completas de viaje. Toda la provincia de CABO DELGADO está clasificada en NIVEL 4 «NO VIAJAR» por el Departamento de Estado de EE. UU. desde el inicio de la insurgencia de ISIS-Mozambique en 2017, y los operadores de fronteras desaconsejan expresamente entrar por el norte. Se marca aquí para dejar constancia de la renuncia consciente y de dónde está el límite: al norte de Nampula NO se sube.",
         credit="Wikimedia Commons", source=W + "Pemba%20port%20(8443551177).jpg?width=900"),
    # ===== CENTRO: Zambézia, el Zambeze y Tete =====
    dict(n=10, name="Quelimane", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-17.8786, lon=36.8883,
         desc="Puerto fluvial sobre el río dos Bons Sinais, la ciudad del cocotero y punto de partida histórico de la travesía de África de Livingstone. Arquitectura colonial deteriorada pero con carácter, catedral antigua, mercado enorme y una de las pocas plazas con servicios entre Nampula y Beira. A 30 km está Zalala, playa de arena larguísima bordeada de cocoteros y prácticamente vacía, buena para acampar y para el perro. Ciudad húmeda y calurosa: malaria alta todo el año.",
         credit="Wikimedia Commons", source=W + "Tribunal%20Judicial%20da%20Prov%C3%ADncia%20de%20Zamb%C3%A9zia%2C%20Quelimane%2C%20Mo%C3%A7ambique.jpg?width=900"),
    dict(n=11, name="Caia y el puente del Zambeze", cat="Cultura", prio="Media", dog="permitido", time="½ día",
         lat=-17.8286, lon=35.3336,
         desc="El punto donde la EN1 cruza el ZAMBEZE por el puente Armando Emílio Guebuza (2.376 m, inaugurado en 2009), que sustituyó a la barcaza que durante décadas partió el país en dos. Es el nudo que decide la ruta: desde aquí se sigue al sur hacia Gorongosa y Beira, o se gira al oeste por la variante interior del Zambeze hacia Sena, Mutarara y Tete. Parada de camioneros con combustible, comida y poco más, pero estratégica: es el último repostaje fiable antes de cualquiera de los dos ramales. Imagen: la presa de Cahora Bassa, aguas arriba en el mismo Zambeze — pendiente de sustituir por una del puente de Caia.",
         credit="Wikimedia Commons", source=W + "Cahorra%20bassa.jpg?width=900"),
    dict(n=12, name="Tete, Cahora Bassa y el puente colgante", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=-16.1564, lon=33.5867,
         desc="Corazón de la variante interior. Tete es la ciudad más calurosa de Mozambique (más de 45 °C en octubre) y su puente colgante sobre el Zambeze, de 1973, sigue siendo una imagen icónica del país. A 150 km al oeste está la PRESA DE CAHORA BASSA, uno de los mayores embalses artificiales de África (2.700 km²), con la ciudad-modelo de Songo colgada sobre la garganta, visitas a la central hidroeléctrica y pesca de tigerfish. La garganta aguas abajo, entre paredes de roca, es el paisaje más espectacular del interior. Combustible fiable y buen enlace al corredor de Chimoio.",
         credit="Wikimedia Commons", source=W + "Cahorra%20bassa.jpg?width=900"),
    # ===== CENTRO-SUR: Gorongosa, Beira, Manica =====
    dict(n=13, name="Parque Nacional de Gorongosa", cat="Naturaleza", prio="Alta", dog="prohibido", time="2–3 noches",
         lat=-18.9814, lon=34.3517,
         desc="EL PARQUE DE REFERENCIA MUNDIAL EN RESTAURACIÓN. La guerra civil borró el 90-95% de la fauna grande; desde 2004 el proyecto de restauración de Gorongosa la ha reconstruido hasta las decenas de miles de animales, y hoy es el caso de estudio que se cita en todo el mundo. El valle del Rift con sus palmerales de borassus, los lagos estacionales de Urema, leones, elefantes, licaones reintroducidos y un programa científico y comunitario muy serio. OJO, DOS REGLAS DURAS: la AUTOCONDUCCIÓN ESTÁ PROHIBIDA (solo safaris guiados en vehículo abierto, saliendo de Chitengo o de Montebelo Lodge) y LAS MASCOTAS ESTÁN PROHIBIDAS salvo perros guía. Tasa de conservación 20 USD/adulto internacional y día, vehículos gratis; puertas 06:00-18:00. Camping propio en Chitengo, donde el perro sí puede quedarse con un cuidador.",
         credit="Brian Dell · dominio público", source=W + "Gorongosa%20Park%20Gate.JPG?width=900"),
    dict(n=14, name="Monte Gorongosa y las cascadas de Murombodzi", cat="Naturaleza", prio="Alta", dog="prohibido dentro del área del parque", time="1–2 días",
         lat=-18.4333, lon=34.0667,
         desc="LA MEJOR CAMINATA DEL CENTRO DEL PAÍS. El macizo de Gorongosa (1.863 m), incorporado al parque en 2010 precisamente porque su bosque de niebla es la fábrica de agua que alimenta el valle, se sube desde la aldea de Sadjunjira. La ruta clásica llega a las CASCADAS DE MUROMBODZI, un salto de unos 80 m en plena selva de montaña, en unas 3-4 horas de ida entre plantaciones de café de sombra del proyecto comunitario. Guía obligatorio del parque. Es senderismo de verdad, no un mirador: subida constante, calor y humedad. Imagen: monte Gorongosa.",
         credit="Wikimedia Commons", source=W + "Mount%20Gorongosa%2C%20Gorongosa%20National%20Park%2C%20Mozambique%20(46316615492).jpg?width=900"),
    dict(n=15, name="Beira", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-19.8437, lon=34.8389,
         desc="Segunda ciudad del país y cabecera del corredor de Beira hacia Zimbabue: el mejor sitio del centro para talleres, recambios, neumáticos y aprovisionamiento serio. La Sé da Beira y el Grande Hotel —un coloso art déco de 1954 abandonado y hoy habitado por cientos de familias— son dos de las imágenes más potentes de Mozambique. La ciudad fue arrasada por el CICLÓN IDAI en marzo de 2019 (el 90% de los edificios dañados) y se ha reconstruido: es el recordatorio físico de por qué la ventana de enero-marzo no vale para este viaje.",
         credit="Rosino · CC BY-SA 2.0", source=W + "S%C3%A9%20da%20Beira.jpg?width=900"),
    dict(n=16, name="Chimoio, Manica y el arte rupestre de Chinhamapere", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=-19.1164, lon=33.4833,
         desc="Última plaza grande antes de la frontera de Machipanda, en la meseta de Manica: clima fresco, buenos servicios y base para el bloque montañoso. A 70 km, el pueblo de Manica conserva el mirador de Penha Longa sobre la frontera, minas de oro artesanales visitables y, sobre todo, CHINHAMAPERE, un abrigo con pinturas rupestres san de miles de años que sigue siendo lugar sagrado activo: lo custodian mujeres médium de la comunidad, que acompañan la visita y hacen la ofrenda previa. Está en la lista indicativa de la UNESCO. Se sube andando 20-30 minutos. Imagen: la sierra de Chimanimani desde el lado zimbabuense, el mismo macizo que cierra la meseta de Manica — pendiente de sustituir por una de Chinhamapere.",
         credit="Wikimedia Commons", source=W + "Chimanimani%20Zimbabwe1%20var.jpg?width=900"),
    dict(n=17, name="Reserva Nacional de Chimanimani y el monte Binga (2.436 m)", cat="Naturaleza", prio="Alta", dog="prohibido dentro de la reserva", time="3–4 días",
         lat=-19.7647, lon=33.0619,
         desc="EL TECHO DE MOZAMBIQUE y la mejor travesía a pie del país. El monte Binga (2.436 m) corona la sierra de Chimanimani, en la frontera con Zimbabue: cuarcitas blancas, praderas de altura, bosque de galería y cascadas. Desde el lado mozambiqueño se accede por Sussundenga y Rotanda; los últimos 22 km hasta la aldea de Nbabawa son PISTA 4x4. La subida es de 2-3 días con campamento intermedio (Mosquito Camp) y desvío a las cascadas de Mubvumodzi; guía local obligatorio en la práctica (unos 450 MT/día) y tasas del parque muy bajas (~2.500 MT por dos personas y tres noches). PROHIBIDO hacer cumbre por libre en la temporada de lluvias (diciembre-marzo): los arroyos se convierten en ríos infranqueables.",
         credit="Wikimedia Commons", source=W + "Mt%20Binga%20Mozambique.JPG?width=900"),
    # ===== SUR: la gran costa índica =====
    dict(n=18, name="Inhassoro y la península de San Sebastián", cat="Costa", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-21.5333, lon=35.2000,
         desc="El acceso terrestre más salvaje del archipiélago. Desde Inhassoro sale la PISTA DE ARENA de la PENÍNSULA DE SAN SEBASTIÁN, un dedo de dunas y matorral costero de unos 60 km que apunta hacia Bazaruto y que es una reserva privada de conservación con antílopes, y uno de los pocos sitios de Mozambique donde todavía queda arena profunda de verdad y ni un alma. Se hace con presión muy baja, en convoy y consultando marea y accesos en la barrera de entrada. Inhassoro es además el embarque más corto a la isla de Bazaruto.",
         credit="Wikimedia Commons", source=W + "Sand%20Rd%20(4x4%20requied)%2C%20Mozambique%20-%20panoramio%20(1).jpg?width=900"),
    dict(n=19, name="Vilanculos y el archipiélago de Bazaruto", cat="Naturaleza", prio="Alta", dog="no en las islas", time="3 noches",
         lat=-22.0027, lon=35.3133,
         desc="Parque nacional marino de cinco islas con DUNAS DE ARENA BLANCA DE 100 M cayendo al mar, arrecifes de coral, mantas y la última población viable de DUGONGO del océano Índico occidental. A las islas solo se llega en barco (dhow tradicional o lancha) desde Vilanculos, que es la base logística: campings orientados a overlanders, combustible, mercado y talleres. El perro se queda en tierra: en el camping de Vilanculos sí, en el parque marino no. Vilanculos es también el punto donde la EN1 deja de ser buena hacia el norte, así que sirve de bisagra en los dos sentidos.",
         credit="Copernicus Sentinel-2 (Unión Europea) · Attribution", source=W + "Bazaruto%20Archipelago%20National%20Park%2C%20Mozambique.jpg?width=900"),
    dict(n=20, name="Tofo, Barra e Inhambane", cat="Costa", prio="Alta", dog="permitido en las playas de Tofo y Barra", time="3–4 noches",
         lat=-23.8544, lon=35.5453,
         desc="LA CAPITAL MUNDIAL DEL TIBURÓN BALLENA Y LA MANTA GIGANTE. La bahía de Tofo tiene una de las agregaciones más constantes del planeta de ambas especies (la Marine Megafauna Foundation nació aquí), y entre junio y octubre pasan además las ballenas jorobadas. Enfrente, la PENÍNSULA DE BARRA se recorre por pista de arena profunda entre cocoteros hasta el faro, con campings a pie de playa que admiten perro. Inhambane, al fondo del estuario, es la ciudad colonial más bonita del sur: catedral del XVIII, mezquitas, dhows cruzando a Maxixe y mercado. Bloque obligado de varios días.",
         credit="Wikimedia Commons", source=W + "Church%20Inhambane%20(3984583818).jpg?width=900"),
    dict(n=21, name="Maputo", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-25.9692, lon=32.5732,
         desc="Capital, embajada de España y la mayor base de servicios del país: talleres de 4x4, recambios, hospital central y clínicas privadas (Cruz Azul), supermercados grandes y consulados para el resto del bucle. Avenidas de acacias y jacarandás, la Casa de Ferro de Eiffel, la estación de ferrocarril de 1910 (una de las más bonitas del mundo), el mercado del Peixe y el Fortaleza. Desde 2018 el PUENTE DE KATEMBE, el colgante más largo de África (680 m de vano), abre el camino directo al sur hacia Ponta do Ouro sin barcaza.",
         credit="F Mira from Lisbon, Portugal · CC BY-SA 2.0", source=W + "Avenida%20Samora%20Machel%20towards%20Maputo%20City%20Hall.jpg?width=900"),
    dict(n=22, name="Ponta do Ouro, Ponta Malongane y el Parque Nacional de Maputo", cat="Costa", prio="Alta", dog="permitido fuera del parque", time="3–4 noches",
         lat=-26.8433, lon=32.8917,
         desc="EL EXTREMO SUR DE MOZAMBIQUE Y EL PARAÍSO 4x4 DEL PAÍS. Desde el puente de Katembe la carretera acaba y empieza el laberinto de PISTAS DE ARENA PROFUNDA entre dunas boscosas, lagos interiores (Sugi, Sotiva, Piti) y las puntas sucesivas: Malongane, Mamoli, Dobela y Ponta do Ouro, a 10 km de la frontera sudafricana de Kosi Bay. Aquí está la población residente de DELFINES MULARES con la que se nada desde la playa, los mejores fondos de buceo del país (Pinnacles) y avistamiento de ballenas de junio a noviembre. El Parque Nacional de Maputo (antigua Reserva de Elefantes, gestionado con Peace Parks) protege el corredor de Futi con elefantes que vuelven a moverse hasta Sudáfrica: AQUÍ SÍ SE PERMITE LA AUTOCONDUCCIÓN, con campings propios en Xinguti (hipopótamos y cocodrilos) y Ponta Membene (bosque, lagos y playa). Puertas 06:00-17:00 de octubre a marzo y 07:00-16:00 de abril a septiembre; reservas en reservas@parquemaputo.gov.mz, +258 85 6000 900. Dentro del parque el perro NO entra, pero los campings de Ponta do Ouro y Malongane sí lo admiten.",
         credit="Wikimedia Commons", source=W + "Ponta%20do%20Ouro%20in%20the%20morning.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul", "cultura": "morado",
              "patrimonio unesco": "marron", "costa": "turquesa", "referencia · conflicto": "gris"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada RECOMENDADA — Matchedje / Puente de la Unidad 2 (desde Tanzania)", "Frontera", -11.5800, 35.4295,
     "SÍ ES UN PUENTE. Este puesto corresponde al PUENTE DE LA UNIDAD 2 (Unity Bridge 2 / Ponte da Unidade II) sobre el río Rovuma, entre Kivikoni (Tanzania) y Lupilichi-Segunda Congresso (Mozambique), en 11°34′46″S 35°25′47″E — las mismas coordenadas que las guías de fronteras publican como «Matchedje». Horario 06:00-18:00 los siete días. Tel. +258 27 120 446 / +258 82 464 1600. Songea a 130 km al norte, Lichinga a 232 km al sur. Es el ÚNICO paso del Rovuma que NO desemboca en Cabo Delgado: entra directamente en la provincia de Niassa por el oeste. Fama de contrabando de rubíes: registro probable. Repostar a fondo en Songea: entre la frontera y Lichinga no hay suministro."),
    ("Frontera · Entrada DESCARTADA — Negomano/Mtambaswala (Puente de la Unidad 1)", "Frontera", -11.4193, 38.4962,
     "El Puente de la Unidad original: 720 m de longitud y 13,8 m de ancho, 18 vanos de hormigón pretensado y dos carriles, construido por China Geo-Engineering entre 2005 y 2010 por 35 millones de dólares, en 11°24′52″S 38°29′39″E. Horario 07:30-16:00. Infraestructura excelente, destino imposible: DESCARTADO porque desemboca en el distrito de Mueda (Cabo Delgado), provincia clasificada en nivel 4 «no viajar», y a ~180 km tierra adentro de Mtwara vía Masasi. Las propias guías de fronteras de Mozambique desaconsejan expresamente usarlo."),
    ("Frontera · Entrada DESCARTADA — Kilambo/Namoto (barcaza del Rovuma)", "Frontera", -10.4700, 40.4400,
     "NO ES UN PUENTE: es una barcaza para ~6 vehículos 4x4 (u 8 pequeños) en la desembocadura del Rovuma, a unos 40 km al sur de Mtwara. Depende de la marea (necesita ~3 m de agua) y a veces carga y zarpa a la mañana siguiente; el lado mozambiqueño abre 07:00-19:00 pero el tanzano SOLO 07:00-08:00. Contacto operativo: capitán Dula, +255 78 772 4928. DESCARTADO doblemente: por la logística y porque deja al viajero en Quionga, dentro de la zona de ataques. Coordenadas aproximadas."),
    ("Frontera · Entrada ALTERNATIVA — Zóbuè/Mwanza (desde Malaui)", "Frontera", -15.6136, 34.3856,
     "Plan B si la entrada por el Rovuma se descarta por completo: bajar por Malaui y entrar a Mozambique por el corredor de Tete. Carretera asfaltada, tráfico pesado de camiones. Obliga a añadir Malaui a la ruta global y renuncia a todo el norte mozambiqueño (Niassa, Nampula, Ilha de Moçambique). Coordenadas aproximadas: verificar."),
    ("Frontera · Salida — Machipanda/Forbes (hacia Zimbabue)", "Frontera", -19.0059, 32.7171,
     "Salida prevista del país, a 95 km de Chimoio y a 8 km de Mutare (Zimbabue). Enlace económico principal entre Harare y el puerto de Beira: MUCHÍSIMO camión y atascos que llegan a bloquear la carretera. Llegar temprano. Horario: las fuentes discrepan entre 06:00-20:00 y apertura 24 h acordada en enero de 2024 — confirmar. Tel. +258 25 165 011."),
    ("Embajada de España en Maputo", "Consular", -25.9700, 32.5850,
     "Rua Damião de Góis, 347, Caixa Postal 1331, Maputo. Tel. (+258) 21 49 20 25/27/30 · Emergencia consular 24 h: (+258) 84 32 82 900. Es la única representación española del país: cualquier trámite mayor se gestiona aquí, a 2.500 km de la frontera de entrada."),
    ("Hospital Central de Maputo", "Hospital", -25.9575, 32.5789,
     "Principal hospital de referencia del país. Para lo serio, la práctica regional es la evacuación a Sudáfrica (Nelspruit o Johannesburgo, a 5-6 h por carretera desde Maputo). Alternativa privada: Clínica Cruz Azul."),
    ("Hospital Central de Nampula", "Hospital", -15.1165, 39.2666,
     "Mejor referencia sanitaria de todo el norte y el centro-norte: lo más cercano a Ilha de Moçambique, Cuamba y Gurué. Entre Lichinga y Nampula solo hay hospitales rurales."),
    ("Hospital Central da Beira", "Hospital", -19.8437, 34.8389,
     "Referencia del centro del país, la mejor opción entre Quelimane y Maputo; cubre Gorongosa, Chimoio y Chimanimani."),
    ("Combustible · Lichinga (norte)", "Combustible", -13.3128, 35.2406,
     "Primer repostaje formal tras entrar por Matchedje, a 232 km de la frontera. Salir de Songea (Tanzania) con los depósitos y garrafas llenos: en ese tramo no hay garantía ninguna."),
    ("Combustible · Cuamba y Nampula", "Combustible", -14.8036, 36.5372,
     "Cuamba es el único repostaje fiable entre Lichinga y Nampula (~350 km). Nampula concentra la mejor oferta y calidad del norte (Petromoc, Total, Puma)."),
    ("Combustible · Quelimane, Caia y Beira (centro)", "Combustible", -17.8286, 35.3336,
     "Caia, junto al puente del Zambeze, es el nudo: último repostaje fiable antes de Gorongosa o antes de la variante interior hacia Tete. Beira es la mejor plaza del centro."),
    ("Combustible · Vilanculos, Inhambane y Maputo (sur)", "Combustible", -22.0027, 35.3133,
     "El sur está bien servido: la EN1 tiene estaciones con regularidad. Repostar a fondo en Vilanculos antes de subir al norte, donde la EN1 empeora mucho. Regla overlander local: repostar al llegar al 50% del depósito a partir de Vilanculos hacia el norte."),
    ("Agua potable y de uso general · Nampula, Beira, Vilanculos y Maputo", "Agua potable", -19.8437, 34.8389,
     "Agua embotellada sin problema en supermercados de las cuatro. Campings, lodges y estaciones de servicio permiten llenar el depósito de uso general con manguera; confirmar en recepción."),
    ("Agua · costa de Inhambane y Ponta do Ouro", "Agua potable", -23.8544, 35.5453,
     "Los campings de Tofo, Barra, Ponta do Ouro y Malongane tienen agua corriente y duchas; agua de pozo salobre en algunos, tratar antes de beber. Brotes de cólera recurrentes en el país: no beber agua no embotellada ni tratada, en ninguna provincia."),
]

DRONE_CALLOUT = ("warn", "Autorización previa del IACM obligatoria · prohibido en parques y en todo el norte",
                 "Mozambique no prohíbe los drones de forma general, pero el Instituto de Aviação Civil de Moçambique (IACM) exige registro y autorización previa para el uso de aeronaves no tripuladas, y la práctica varía mucho de provincia a provincia. En un país con insurgencia activa y presencia militar en el norte, volar un dron sin papel es una forma rápida de acabar detenido. Norma del proyecto: autorización escrita antes de volar, nunca en Cabo Delgado ni en Niassa, nunca cerca de instalaciones militares, portuarias o de gas, y nunca dentro de parques nacionales.")

STARLINK_CALLOUT = ("ok", "Disponible y operativo",
                    "Starlink está activo comercialmente en Mozambique y da servicio en buena parte del país, incluida la costa y el corredor de Beira. Es la mejor solución para el tramo norte (Niassa, Cuamba, Gurué), donde la cobertura móvil es irregular. Configurar el kit y el plan de roaming antes de entrar y comprobar la política de itinerancia regional vigente.")

DOG_MATRIX = [
    ("Lago Niassa (Metangula, Cóbuè), Chocas-Mar y las Cabaceiras, Zalala", "permitido",
     "Orilla y playa abiertas, sin figura de parque nacional: es la mejor parte del norte con el perro. Sombra, agua y horarios de calor son la única precaución real; cocodrilos en las desembocaduras del lago, preguntar siempre en el alojamiento."),
    ("Playas de Tofo, Barra, Vilanculos, Inhassoro, Ponta do Ouro y Malongane", "permitido",
     "Toda la costa sur fuera de parques admite perro y hay campings explícitamente pet-friendly en Ponta do Ouro, Malongane, Tofo y Barra. Es el gran alivio del tramo tras tantos parques prohibidos: semanas enteras de playa con el perro suelto. Confirmar por escrito al reservar, la política varía por establecimiento."),
    ("Ciudades: Lichinga, Nampula, Quelimane, Beira, Chimoio, Maputo", "permitido con condiciones",
     "Sin restricción específica; correa, sombra y calor húmedo. Veterinarios reales solo en Maputo, Beira y Nampula. En Ilha de Moçambique, correa corta: es una isla habitada y muy transitada, no un sitio para soltarlo."),
    ("Parque Nacional de Gorongosa", "prohibido",
     "Regla oficial del parque: mascotas prohibidas salvo perros guía documentados. Y además NO se permite la autoconducción: se entra en vehículo abierto con guía. Plan B: acampar en Chitengo y turnarse — dos viajeros al safari y uno con el perro en el campamento; confirmar por adelantado con safari@gorongosa.net que se puede dejar el perro en la parcela."),
    ("Reserva Nacional de Chimanimani y monte Binga", "prohibido dentro de la reserva",
     "Área protegida con guía obligatorio y campamentos de altura: no es sitio para el perro. Plan B: dejarlo en Chimoio o Sussundenga con alojamiento que lo admita, durante los 3-4 días de la travesía."),
    ("Archipiélago de Bazaruto y Parque Nacional de Maputo", "prohibido",
     "Bazaruto es parque marino y solo se accede en barco; Maputo NP es parque nacional con elefantes, aunque aquí SÍ se permite la autoconducción y hay camping propio (Xinguti, Ponta Membene). Plan B: el perro se queda en el camping de Vilanculos o de Ponta do Ouro, ambos con sombra y vigilancia, mientras se hace la salida; o turnos entre los tres viajeros."),
    ("Reserva Especial de Niassa, Quirimbas, Pemba y todo Cabo Delgado", "no aplica",
     "No se entra en ningún caso, por seguridad. No hay plan B porque no hay plan A."),
]

SOURCES = [
    ("Departamento de Estado de EE. UU. · Mozambique Travel Advisory (nivel 4 «no viajar» en Cabo Delgado, Reserva de Niassa y distritos de Memba y Erati)", "https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories/mozambique-travel-advisory.html"),
    ("FCDO (Reino Unido) · Mozambique travel advice, seguridad y delincuencia", "https://www.gov.uk/foreign-travel-advice/mozambique"),
    ("ACLED · Mozambique Conflict Monitor Update, 17 de junio de 2026", "https://acleddata.com/update/mozambique-conflict-monitor-update-17-june-2026"),
    ("ACLED · Mozambique Conflict Monitor Update, 3 de junio de 2026", "https://acleddata.com/update/mozambique-conflict-monitor-update-3-june-2026"),
    ("ISS Africa · «Cabo Delgado insurgency persists amid failed military strategy»", "https://issafrica.org/iss-today/cabo-delgado-insurgency-persists-amid-failed-military-strategy"),
    ("Accommodation Mozambique · paso de Negomano/Mtambaswala (puente de la Unidad): horario y advertencia de seguridad", "https://www.accommodationmozambique.co.za/mozambique-border-gates-and-times/negomane-mtambaswala-unity-bridge-border-post-crossing/"),
    ("Accommodation Mozambique · paso de Namoto/Kilambo (barcaza del Rovuma): capacidad, mareas y contacto", "https://www.accommodationmozambique.co.za/mozambique-border-gates-and-times/namoto-kilambo-ferry-border-post-crossing/"),
    ("Accommodation Mozambique · paso de Matchedje (Niassa)", "https://www.accommodationmozambique.co.za/mozambique-border-gates-and-times/matchedje-border-post-crossing/"),
    ("Accommodation Mozambique · paso de Machipanda/Forbes (Zimbabue)", "https://www.accommodationmozambique.co.za/mozambique-border-gates-and-times/machipanda-forbes-border-post-crossing/"),
    ("Wikipedia · Unity Bridge (Negomano/Mtambaswala): 720 m, dos carriles, inaugurado en 2010", "https://en.wikipedia.org/wiki/Unity_Bridge"),
    ("Wikipedia · Unity Bridge 2 (Kivikoni–Lupilichi), el puente del paso de Matchedje", "https://en.wikipedia.org/wiki/Unity_Bridge_2"),
    ("Horizons Unlimited (HUBB) · relatos del cruce fronterizo norte de Mozambique-Tanzania", "https://www.horizonsunlimited.com/hubb/sub-saharan-africa/northern-mozambique-tanzania-border-crossing-45073"),
    ("Tracks4Africa Padkos · Negomano/Mtambaswala Unity Bridge Border Post", "https://tracks4africa.co.za/listings/item/w240639/negomanomtambaswala-unity-bridge-border-post-moztanz-07h30-16h00/"),
    ("Tracks4Africa Padkos · Forbes Border Post (Zimbabue/Mozambique)", "https://tracks4africa.co.za/listings/item/w147572/forbes-border-post/"),
    ("Club of Mozambique · la frontera Mozambique-Zimbabue pasa a operar 24/7", "https://clubofmozambique.com/news/mozambique-zimbabwe-border-crossing-now-open-247-252349/"),
    ("Fragomen · programa de exención de visado de Mozambique (España incluida, 30 días, decreto 10/2023)", "https://www.fragomen.com/insights/new-visa-exemption-program-launched.html"),
    ("EY · nuevo registro electrónico previo al viaje para nacionales exentos de visado (desde el 24 de abril de 2025)", "https://www.ey.com/en_gl/technical/tax-alerts/mozambique-announces-new-pre-travel-registration-requirement-for-visa-exempt-foreign-nationals"),
    ("Club of Mozambique · exención de visado para 29 países, en vigor", "https://clubofmozambique.com/news/mozambique-visa-waiver-for-29-countries-effective-since-monday-236642/"),
    ("Gorongosa National Park (web oficial) · tasas y reglas del parque: mascotas prohibidas, sin autoconducción", "https://gorongosa.org/park-fees-and-rules/"),
    ("Parque Nacional de Maputo (web oficial) · autoconducción, campings de Xinguti y Ponta Membene, horarios y reservas", "https://parquemaputo.gov.mz/en/explore/activities/self-drive-safari-adventure-at-maputo-national-park/"),
    ("Peace Parks Foundation · Parque Nacional de Maputo", "https://www.peaceparks.org/parks/maputo-special-reserve/"),
    ("African Parks · Parque Nacional del Archipiélago de Bazaruto", "https://www.africanparks.org/the-parks/bazaruto"),
    ("SafariFind · tasas y disponibilidad de los parques nacionales de Mozambique 2026", "https://safarifind.com/blog/mozambique-national-park-fees-availability-2026"),
    ("PetTravel.com · requisitos de importación de mascotas a Mozambique", "https://www.pettravel.com/information/pet-passports/mozambique-pet-import-requirements/"),
    ("Nomad and in Love · guía de conducción en Mozambique: equipamiento obligatorio, seguro y policía", "https://nomadandinlove.com/driving-in-mozambique/"),
    ("The Travelling Sloth · itinerario overland de 16 días por Mozambique", "https://www.thetravellingsloth.com/overlanding-mozambique-road-trip-guide-16-day-itinerary/"),
    ("Overland Travel Tips · Overlanding Mozambique: rutas, fronteras y campings", "https://overlandtraveltips.com/en/overlanding-mozambique-routes-borders-travel-guide/"),
    ("4x4 Africa · Mozambique para el viajero off-road (EN8, Niassa, Chimanimani, Bazaruto)", "https://4x4africa.co.za/offroad-traveller-tourism/mozambique-tourism-for-the-off-road-traveler/"),
    ("Ponta do Ouro Accommodation · rutas 4x4 y lagos de Ponta do Ouro", "https://www.pontadoouroaccommodation.co.za/activities-and-attractions/4x4-trails-in-ponta-do-ouro/"),
    ("SA Adventure · «Crossing the Rovuma», relato del cruce en barcaza en la desembocadura", "https://www.saadventure.co.za/crossingtherovuma"),
    ("4x4community.co.za · hilo «Crossing the Rovuma river»", "https://www.4x4community.co.za/forum/showthread.php/151727-Crossing-the-Rovuma-river"),
    ("4x4community.co.za · hilo «Moz Beach Driving Permits»", "https://www.4x4community.co.za/forum/showthread.php/281426-Moz-Beach-Driving-Permits"),
    ("Real World Adventures · cómo subir el monte Binga (guía, tasas, acceso 4x4, temporada)", "https://realworldadventures.com/summit-mt-binga/"),
    ("SummitPost · Mount Binga", "https://www.summitpost.org/mount-binga/150603"),
    ("iOverlander · Chitengo Camp, Parque Nacional de Gorongosa", "https://www.ioverlander.com/places/38753-chitengo-camp-gorongosa-np"),
    ("iOverlander · puntos de combustible, agua y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
    ("Connecting Africa · Starlink entra en servicio en Mozambique", "https://www.connectingafrica.com/broadband/spacex-s-starlink-goes-live-in-mozambique"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("Drone Laws · normativa de drones en Mozambique", "https://drone-laws.com/drone-laws-in-mozambique/"),
    ("UNICEF Mozambique · ciclones Idai y Kenneth", "https://www.unicef.org/mozambique/en/cyclone-idai-and-kenneth"),
    ("Al Jazeera · el juicio a Venâncio Mondlane y la crisis política mozambiqueña (septiembre de 2026)", "https://www.aljazeera.com/news/2026/9/8/what-does-mondlanes-trial-mean-for-mozambique"),
    ("GIS Reports · la crisis política de Mozambique tras las elecciones de 2024", "https://www.gisreportsonline.com/r/mozambique-election-crisis/"),
    ("Visit Mozambique · portal turístico del país", "https://www.visitmozambique.net/"),
    ("UNESCO · Ilha de Moçambique, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/599/"),
    ("Embajada de España en Maputo · contacto", "https://www.exteriores.gob.es/Embajadas/maputo/es/Paginas/index.aspx"),
]

# Eje principal: Matchedje (Rovuma) -> Niassa -> Nampula/Ilha -> Quelimane -> Gorongosa/Beira
# -> costa sur hasta Ponta do Ouro -> regreso por la EN1 y salida por Machipanda.
CORRIDOR = [
    (-11.5800, 35.4295), (-13.3128, 35.2406), (-12.6892, 34.8181), (-13.3128, 35.2406),
    (-14.8036, 36.5372), (-15.1165, 39.2666), (-15.0347, 40.7358), (-14.9667, 40.6167),
    (-15.1165, 39.2666), (-15.4667, 36.9833), (-17.8786, 36.8883), (-17.8286, 35.3336),
    (-18.9814, 34.3517), (-19.8437, 34.8389), (-21.5333, 35.2000), (-22.0027, 35.3133),
    (-23.8650, 35.3833), (-23.8544, 35.5453), (-25.9692, 32.5732), (-26.8433, 32.8917),
    (-25.9692, 32.5732), (-19.8437, 34.8389), (-19.1164, 33.4833), (-19.0059, 32.7171),
]

# Variante interior del Zambeze: desde Caia por la orilla sur del río hasta Tete y Cahora Bassa,
# y bajada al corredor de Beira por Changara y Chimoio (evita Gorongosa y la costa).
CORRIDOR_ALT = [
    (-17.8286, 35.3336), (-17.4500, 35.0000), (-17.3833, 35.0167), (-16.7500, 34.4000),
    (-16.1564, 33.5867), (-15.5842, 32.7031), (-16.1564, 33.5867), (-16.9167, 33.2500),
    (-19.1164, 33.4833), (-19.0059, 32.7171),
]

EXPERIENCIAS = [
    "El cruce del Rovuma por la barcaza, contado por quien lo hizo (SA Adventure, expedición «Northward Bound»): en Namoto la «barcaza» eran tres botes de pesca de madera con tablas encima atadas con cuerda y un fueraborda de 15 CV, capaz de llevar UN 4x4 por viaje. La marea bajó antes de lo previsto y paralizó la operación cuatro horas: lo que debía ser un cruce de 4 horas se convirtió en 14, con negociación de precio, peticiones de dinero extra sobre la marcha y barro profundo en los accesos. La alternativa que barajaron era un desvío de dos días a otro paso. Es el relato que mejor explica por qué NO entramos por ahí.",
    "Estado actual de la barcaza (guías de fronteras de Mozambique): hoy hay una embarcación tipo pontón algo mejor, para unos 6 vehículos 4x4 u 8 pequeños, pero sigue dependiendo de que haya al menos 3 m de agua y a veces carga y zarpa a la mañana siguiente. El lado tanzano solo despacha entre las 07:00 y las 08:00. El contacto que dan los viajeros es el capitán Dula, +255 78 772 4928.",
    "Policía y controles (overlanders del itinerario de 16 días por Mozambique): más de 15 controles policiales en dos semanas. Su receta, que coincide con la de todos los foros: carpeta física con COPIAS IMPRESAS de todo (pasaportes, registro del vehículo, seguro de terceros, permiso internacional de conducir), saludar en portugués, mantener la calma, y si ponen multa, exigir siempre RECIBO. Si parece injusta, discutirla en la comisaría, no en la cuneta.",
    "Estado de la EN1 (mismos viajeros): asfalto correcto hasta Vilanculos y a partir de ahí hacia el norte «really rough shape», con tramos que obligan a contar dos días donde el mapa dice uno. Su regla de combustible: repostar al llegar al 50% del depósito a partir de Vilanculos. Tarjetas VISA funcionan mejor que Mastercard, y hay que llevar metical en efectivo.",
    "Gorongosa sin coche propio: varios viajeros avisan con mayúsculas de que NO SE PERMITE LA AUTOCONDUCCIÓN en el parque; hay que contratar el safari guiado en vehículo abierto desde Chitengo o desde Montebelo Lodge. El camping de Chitengo está registrado en iOverlander y es la pernocta estándar para overlanders, con parcelas, piscina y restaurante.",
    "Monte Binga con guía local: los que lo han subido desde Mozambique recomiendan a Gilbert Bhuku (+263 773 246 889) por unos 450 MT al día (~7 USD), que además carga mochila; las tasas del parque salieron por unos 2.500 MT para dos personas y tres noches, camping incluido. Los últimos 22 km hasta la aldea de Nbabawa son pista de 4x4. Insisten en que hacer cumbre por libre en la temporada de lluvias está prohibido y es peligroso de verdad: los arroyos se vuelven ríos infranqueables.",
    "Pistas 4x4 del sur (comunidad 4x4 sudafricana y guías de Ponta do Ouro): desde Ponta do Ouro salen rutas de arena a los lagos Sugi (6 km al norte), Sotiva (18 km al noroeste) y Piti (30 km al norte, ya en el Parque Nacional de Maputo), entre bosque de dunas, llanuras de inundación y pantanos interiores, con nyala, duiker rojo, reedbuck, suni, cocodrilos e hipopótamos. Es arena blanda continua: se baja presión al llegar y no se vuelve a subir hasta salir a asfalto.",
    "Conducir por la playa: en los foros 4x4 sudafricanos aparece recurrentemente el tema de los «Moz beach driving permits». La circulación por la playa está restringida y sancionada en Mozambique salvo en accesos autorizados de botadura, y ha habido campañas de multas. Conviene preguntar en cada camping cuál es el acceso legal antes de meter el vehículo en la arena de la playa: las pistas de arena entre dunas son otra cosa y esas sí se hacen con normalidad.",
    "Ruta del interior (viajeros del norte): la EN8 entre Nacala y Chiponde, más de 700 km de tierra y grava atravesando sabana y bosque casi tropical, es la travesía off-road larga del norte de Mozambique que citan los off-roaders sudafricanos. Queda fuera de nuestro trazado principal pero es el tipo de pista que este país todavía ofrece.",
    "El paso de Niassa por dentro (foro Horizons Unlimited, relato antiguo pero muy útil): los que cruzaron por el puente nuevo de Congresso/Lupilichi contaban que el puesto todavía no estaba inaugurado oficialmente y que los funcionarios mozambiqueños trabajaban «en cabañas de paja»; en el lado tanzano había que presentarse en inmigración de SONGEA, a 102 km, para pagar el visado en un banco, registrar la aduana ante la TRA y sellar el carnet. Hoy ese mismo punto es el Puente de la Unidad 2 con puesto formal, pero el mensaje de fondo sigue valiendo: es un paso remoto donde los trámites pueden no cerrarse en la propia frontera. Confirmar antes de llegar dónde se sella realmente cada cosa.",
    "Ruta del lago (mismo foro): existe un acceso desde Lichinga a Cóbuè y de ahí a Congresso siguiendo la orilla del lago Niassa, rehabilitado en su día por cooperación irlandesa. Es la variante bonita de la entrada —orilla, aldeas de pescadores y bosque— frente al enlace directo Matchedje-Lichinga por la meseta. Estado actual por confirmar.",
    "Seguro de terceros: se puede comprar por internet antes de cruzar (Hollard, DriveMoz) o en la propia frontera. Los viajeros avisan de que circular con matrícula extranjera sin seguro de terceros mozambiqueño es infracción sancionable y de los primeros papeles que pide la policía.",
]

HISTORIA_RESUMEN = ("Mozambique fue durante siglos un cruce de rutas swahilis del Índico antes de convertirse en la colonia portuguesa más longeva de África (casi 500 años); su independencia en 1975 dio paso casi de inmediato a una guerra civil devastadora, "
                    "y hoy el país reconstruido convive con una insurgencia yihadista activa en el extremo norte que condiciona por completo cómo se puede entrar por tierra desde Tanzania.")

HISTORIA_SECCIONES = [
    ("Antes de la colonización: rutas del Índico",
     "Mucho antes de la llegada europea, la costa mozambiqueña formaba parte del mundo swahili: puertos comerciales donde pueblos bantúes del interior intercambiaban oro, marfil y esclavos con mercaderes árabes, persas e indios que llegaban con los monzones. "
     "Ilha de Moçambique, en el norte, y Sofala, cerca de la actual Beira, fueron los grandes puertos de esta red, conectados por tierra con el imperio de Gran Zimbabue y sus sucesores, que controlaban las minas de oro del interior."),
    ("Colonización portuguesa: casi 500 años",
     "Vasco da Gama tocó la costa mozambiqueña en 1498 de camino a la India, y Portugal fue construyendo aquí, de forma lenta y desigual, la colonia europea más duradera de África: formalmente hasta 1975. Ilha de Moçambique fue su capital durante casi cuatro siglos. "
     "El dominio efectivo del interior no llegó hasta bien entrado el siglo XX, y se sostuvo en gran medida sobre el trabajo forzado (chibalo) y una economía de exportación de mano de obra hacia las minas y plantaciones de Sudáfrica y Rodesia, "
     "más que sobre un desarrollo interno del país."),
    ("Independencia y guerra civil (1975-1992)",
     "El FRELIMO (Frente de Liberación de Mozambique) libró una guerra de independencia desde 1964 y tomó el poder en 1975, tras la Revolución de los Claveles en Portugal. "
     "Casi de inmediato, el nuevo Estado de orientación marxista se vio enfrentado a la RENAMO, un movimiento insurgente armado y financiado primero por la Rodesia blanca y después por el apartheid sudafricano como forma de desestabilizar a un vecino hostil. "
     "La guerra civil resultante (1977-1992) causó alrededor de un millón de muertos, vació de fauna parques como Gorongosa y dejó el país entre los más pobres del mundo al firmarse la paz de Roma en 1992."),
    ("Situación actual: reconstrucción, ciclones y la insurgencia de Cabo Delgado",
     "Desde los años 90 Mozambique vivió una recuperación económica notable, apoyada después por el descubrimiento de enormes reservas de gas natural frente a las costas de Cabo Delgado, en el extremo norte del país. "
     "Precisamente esa provincia, una de las más pobres y marginadas históricamente, es desde 2017 escenario de una insurgencia yihadista vinculada a ISIS-Mozambique, con centenares de miles de desplazados, ataques periódicos a poblaciones, campamentos de caza y proyectos de gas, y uso creciente de artefactos explosivos improvisados en las carreteras. "
     "A ello se suma la exposición extrema del país a los ciclones del Índico: Idai (2019) arrasó Beira, Kenneth (2019) golpeó Cabo Delgado y Freddy (2023) entró dos veces. Ambas cosas —conflicto y ciclones— determinan por dónde y cuándo se puede cruzar el país."),
]

HISTORIA_FUENTES = [
    ("BBC News · Mozambique country profile", "https://www.bbc.com/news/world-africa-13890416"),
    ("Encyclopaedia Britannica · Mozambique, History", "https://www.britannica.com/place/Mozambique/History"),
    ("ISS Africa · la insurgencia de Cabo Delgado", "https://issafrica.org/iss-today/cabo-delgado-insurgency-persists-amid-failed-military-strategy"),
    ("UNESCO · Ilha de Moçambique, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/599/"),
    ("UNICEF Mozambique · ciclones Idai y Kenneth", "https://www.unicef.org/mozambique/en/cyclone-idai-and-kenneth"),
]

SPEC = dict(
    slug="mozambique", name="Mozambique", revision="12 sep 2026",
    sub="Travesía norte-sur del bucle · Tanzania → Zimbabue",
    chips=[
        ("ENTRADA", "Matchedje / Puente de la Unidad 2 (Rovuma, Niassa) — el ÚNICO paso del Rovuma fuera de Cabo Delgado"),
        ("SALIDA", "Machipanda/Forbes (Zimbabue), a 8 km de Mutare"),
        ("SEGURIDAD", "Cabo Delgado, Reserva de Niassa y los distritos de Memba y Erati: nivel 4, NO se entra"),
        ("PDIs", "22 puntos, del lago Niassa a Ponta do Ouro"),
        ("4x4", "Península de San Sebastián · Barra · dunas y lagos de Ponta do Ouro"),
        ("A PIE", "Monte Binga (2.436 m) · monte Namuli · cascadas de Murombodzi · Ilha de Moçambique"),
        ("PERRO", "La mejor costa del viaje: playas y campings SÍ · parques nacionales no"),
        ("VISADO", "Españoles EXENTOS (30 días) + registro electrónico previo obligatorio"),
        ("TEMPORADA", "Ciclones de enero a marzo: cruzar entre mayo y octubre"),
    ],
    center=[-18.5, 36.0], zoom=5,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    hero_img=W + "Forte%20de%20S%C3%A3o%20Sebasti%C3%A3o%20-%20Igreja.jpg?width=900",
    hero_credit="Fortaleza de São Sebastião, Ilha de Moçambique · Wikimedia Commons",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Eje principal costero (Rovuma → Ponta do Ouro → Machipanda)",
    corridor_alt_label="Variante interior del Zambeze (Caia → Tete y Cahora Bassa → Chimoio)",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Mozambique es el país más largo del bucle: <strong>2.500 km de costa índica</strong> de norte a sur, con dos cosas que no ofrece ningún otro país "
                   "de la ruta: <strong>pistas de arena junto al mar durante semanas</strong> y, por fin, <strong>playas y campings donde el perro puede estar</strong>. "
                   "Se entra cruzando el río Rovuma desde Tanzania y se sale hacia Zimbabue por Machipanda. Todo el atractivo del extremo norte "
                   "—Pemba, las Quirimbas, Ibo, la reserva de Niassa— está clasificado como zona de no viajar por la insurgencia de Cabo Delgado, y la ficha lo trata como "
                   "una renuncia consciente, no como una posibilidad abierta. El eje principal suma unos <strong>5.300 km</strong> (21-22 días de conducción a 250 km/día, "
                   "más los días de parada) contando la bajada hasta Ponta do Ouro y el regreso al norte para salir por Machipanda."),
    decision=("<strong>Entrada desde Tanzania: se entra por MATCHEDJE, no por el Rovuma costero.</strong> Los tres pasos del río Rovuma no son equivalentes. "
              "(1) <strong>Kilambo/Namoto</strong>, en la desembocadura, a 40 km de Mtwara, NO ES UN PUENTE: es una barcaza dependiente de la marea (necesita ~3 m de agua) "
              "con capacidad para unos 6 vehículos 4x4, cuyo lado tanzano solo despacha entre las 07:00 y las 08:00 y que a veces carga y zarpa al día siguiente; "
              "además deja al viajero en Quionga, dentro de la zona de ataques. "
              "(2) El <strong>Puente de la Unidad</strong> original sí existe y es una obra seria —720 m, 13,8 m de ancho, dos carriles, inaugurado en mayo de 2010 tras cinco años de obra y 35 millones de dólares— y está en "
              "<strong>Mtambaswala/Negomano</strong>, en 11°24′52″S 38°29′39″E, 180 km tierra adentro vía Masasi, horario 07:30-16:00. El problema no es el puente: es que desemboca en el distrito de Mueda, en pleno Cabo Delgado. "
              "Las propias guías de fronteras mozambiqueñas desaconsejan expresamente AMBOS pasos y proponen como alternativa Matchedje o la entrada vía Malaui. "
              "(3) <strong>MATCHEDJE es también un puente sobre el Rovuma, y además un puente nuevo: el PUENTE DE LA UNIDAD 2</strong> (Unity Bridge 2 / Ponte da Unidade II), entre Kivikoni (Tanzania) y "
              "Lupilichi-Segunda Congresso (Mozambique), en 11°34′46″S 35°25′47″E — exactamente las coordenadas que las guías publican como «puesto de Matchedje». Horario 06:00-18:00, a 130 km al sur de Songea, "
              "entra directamente en la provincia de NIASSA por el oeste, a 232 km de Lichinga y a más de 600 km de la zona de conflicto. Es la única entrada terrestre desde Tanzania defendible en 2027, y no obliga a renunciar al puente: hay puente. "
              "<strong>Conclusión operativa:</strong> se cruza el Rovuma, sí, pero por Matchedje; y <strong>al norte de Nampula no se sube</strong>. "
              "Si en el momento del viaje Matchedje estuviera cerrado o el conflicto se hubiera desplazado al oeste de Niassa, el plan B es bajar por Malaui y entrar por Zóbuè/Mwanza al corredor de Tete, "
              "renunciando a todo el norte mozambiqueño.")
    ,
    facts=[
        ("Rol en la ruta", "Penúltimo país del bucle antes de virar al oeste. Se cruza UNA vez, de norte a sur, con entrada y salida distintas."),
        ("Entrada", "Matchedje / Puente de la Unidad 2 sobre el Rovuma, 06:00-18:00, 130 km al sur de Songea (Tanzania) y 232 km al norte de Lichinga. Sin combustible en ese tramo."),
        ("Salida", "Machipanda/Forbes hacia Zimbabue, a 95 km de Chimoio. Corredor de camiones Harare-Beira: atascos importantes, llegar temprano."),
        ("Zonas excluidas", "Toda la provincia de Cabo Delgado, la Reserva Especial de Niassa y los distritos de Memba y Erati (norte de Nampula): nivel 4 «no viajar» del Departamento de Estado de EE. UU."),
        ("Visado", "Los españoles están EXENTOS de visado (decreto 10/2023, 30 días prorrogables 30 más), pero desde el 24 de abril de 2025 hay que hacer un REGISTRO ELECTRÓNICO PREVIO al menos 48 h antes."),
        ("Vehículo", "CPD no obligatorio: permiso temporal de importación en frontera. Seguro de terceros mozambiqueño OBLIGATORIO, y equipamiento obligatorio revisado por la policía en cada control."),
        ("Temporada", "Ventana útil de mayo a octubre. De enero a marzo es temporada de ciclones (Idai arrasó Beira en marzo de 2019) y las pistas del norte se vuelven impracticables."),
        ("Perro", "El mejor país del bucle para el perro: toda la costa fuera de parques lo admite, con campings explícitamente pet-friendly. Prohibido en Gorongosa, Bazaruto, Maputo NP y Chimanimani."),
        ("Comunicaciones", "Starlink activo y operativo; SIM local (Vodacom, Movitel, Tmcel) como respaldo. Cobertura móvil irregular en Niassa y Zambézia."),
    ],
    alerts=[
        "Cabo Delgado, completo: nivel 4 «no viajar». Pemba, Mocímboa da Praia, Palma, Macomia, Muidumbe, Quionga, Mueda, las Quirimbas e Ibo quedan FUERA de cualquier versión de la ruta. ACLED registraba en junio de 2026 al menos 11 episodios de violencia política en dos semanas, con artefactos explosivos improvisados colocados en las carreteras alrededor del bosque de Catupa y más de 21.000 desplazados en Ancuabe, Chiúre y Montepuez.",
        "La Reserva Especial de Niassa está también en nivel 4 por ataques a campamentos de caza DENTRO de la reserva: no es un desvío disponible, por mucho que aparezca en las guías de off-road como el gran territorio 4x4 del país.",
        "Norte de Nampula: los distritos de Memba y Erati están en nivel 4. Ilha de Moçambique y Nampula ciudad quedan al sur de esa franja y son la parte visitable, pero la línea es fina: revalidar el aviso oficial 72 h antes de subir a la costa norte y no improvisar desvíos hacia el noreste.",
        "Ciclones: la temporada va de noviembre a abril con el pico en enero-marzo. Idai (marzo 2019) dañó el 90% de Beira, Kenneth (abril 2019) golpeó Cabo Delgado y Freddy (2023) entró dos veces. Cruzar Mozambique en esa ventana es exponerse a carreteras cortadas y puentes caídos, no solo a lluvia.",
        "Gorongosa: NO se permite la autoconducción. Hay que contratar safari guiado en vehículo abierto desde Chitengo o Montebelo. Y las mascotas están prohibidas salvo perros guía.",
        "Policía de tráfico: es el clásico del país. Equipamiento obligatorio completo (dos triángulos, dos chalecos reflectantes amarillos, documentación y seguro de terceros mozambiqueño), copias impresas de todo, y exigir SIEMPRE recibo de cualquier multa.",
        "Malaria alta en todo el país y durante todo el año, con máxima intensidad en la costa y el valle del Zambeze; brotes recurrentes de cólera. Profilaxis y agua tratada sin excepción.",
        "RIESGO POLÍTICO ABIERTO EN 2027: tras las presidenciales de octubre de 2024 el país vivió meses de protestas con más de 300 muertos, cortes de carretera y paralización del corredor de Maputo. El líder opositor Venâncio Mondlane afronta cinco cargos ante el Tribunal Supremo (entre ellos instigación al terrorismo) y su juicio arrancaba a finales de 2026: una sentencia puede reactivar los disturbios justo en la ventana del viaje. Vigilar el calendario judicial antes de entrar y tener plan de salida alternativo si se cortan la EN1 o el corredor de Beira.",
        "El backtrack del sur: bajar hasta Ponta do Ouro y volver a subir a Machipanda son unos 1.300 km de repetición de la EN1. Es la decisión de ruta más cara de esta ficha — ver decisiones pendientes.",
    ],
    ruta_intro=("Descenso completo del país de norte a sur por la costa, con una variante interior por el Zambeze, y regreso al centro para salir hacia Zimbabue. "
                "Etapas calculadas sobre una media de 250 km/día."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada por el Rovuma", "Songea (Tanzania) → Matchedje → Lichinga", "~360 km · 2 días (232 km sin servicios)"),
        ("2 · El lago", "Lichinga → Metangula/Cóbuè (lago Niassa) → Lichinga", "~270 km ida y vuelta · 3 días"),
        ("3 · Interior del Niassa", "Lichinga → Mandimba → Cuamba", "~340 km · 2 días"),
        ("4 · Hacia la costa", "Cuamba → Nampula", "~350 km · 2 días"),
        ("5 · La isla", "Nampula → Monapo → Ilha de Moçambique → Chocas-Mar y las Cabaceiras", "~250 km · 4-5 días"),
        ("6 · Té y montaña (desvío)", "Nampula → Alto Molócuè → Gurué y el monte Namuli", "~400 km · 3-4 días"),
        ("7 · Zambézia", "Gurué → Mocuba → Quelimane (y playa de Zalala)", "~350 km · 2-3 días"),
        ("8 · El Zambeze", "Quelimane → Nicoadala → Caia (puente del Zambeze)", "~280 km · 1-2 días"),
        ("Variante interior · Tete", "Caia → Sena/Mutarara → Tete → Cahora Bassa/Songo → Changara → Chimoio", "~900 km · 5-6 días (en lugar de las etapas 9-10)"),
        ("9 · Gorongosa", "Caia → Inchope → Chitengo (Gorongosa) y monte Gorongosa", "~250 km · 4-5 días"),
        ("10 · Beira", "Gorongosa → Inchope → Beira", "~200 km · 2 días de taller y logística"),
        ("11 · Montaña de Manica (desvío)", "Beira → Chimoio → Manica/Chinhamapere → Sussundenga → Rotanda → monte Binga", "~350 km · 5-6 días con la travesía a pie"),
        ("12 · Bajada a la costa sur", "Beira → Muxungue → Inhassoro y la península de San Sebastián", "~500 km · 3-4 días"),
        ("13 · Bazaruto", "Inhassoro → Vilanculos (archipiélago de Bazaruto)", "~100 km · 3 días"),
        ("14 · Tiburón ballena", "Vilanculos → Massinga → Inhambane → Tofo y la península de Barra", "~450 km · 4-5 días"),
        ("15 · Capital", "Tofo → Xai-Xai → Maputo", "~500 km · 3 días"),
        ("16 · El extremo sur y las dunas", "Maputo → puente de Katembe → Parque Nacional de Maputo → Ponta Malongane → Ponta do Ouro", "~150 km de arena · 4 días"),
        ("17 · Regreso y salida", "Ponta do Ouro → Maputo → EN1 → Inchope → Chimoio → Machipanda (frontera)", "~1.300 km · 6 días"),
    ],
    offroad=[
        "PENÍNSULA DE SAN SEBASTIÁN (desde Inhassoro): el tramo de arena profunda más largo y salvaje del país fuera del extremo sur, unos 60 km de dunas y matorral costero apuntando a Bazaruto, dentro de una reserva privada con fauna. Presión muy baja (1,2-1,4 bar), convoy obligatorio con los dos vehículos, y consultar el estado de los accesos y las mareas en la barrera de entrada antes de meterse.",
        "DUNAS Y LAGOS DE PONTA DO OURO: desde el puente de Katembe el asfalto se acaba y empieza el laberinto de arena entre bosque de dunas: lago Sugi (6 km al norte), lago Sotiva (18 km al noroeste) y lago Piti (30 km al norte, ya dentro del Parque Nacional de Maputo), más el enlace entre Ponta Malongane, Ponta Mamoli, Ponta Dobela y Ponta do Ouro. Arena blanda continua: se desinfla al entrar y no se vuelve a inflar hasta salir a asfalto. Es el tramo 4x4 más divertido de Mozambique.",
        "PENÍNSULA DE BARRA (Inhambane): pista de arena profunda entre cocoteros desde Tofo hasta el faro de Barra, con campings a pie de playa por el camino. Corta pero exigente y muy fotogénica; en las horas de calor la arena está más suelta, mejor temprano.",
        "CHOCAS-MAR Y LAS CABACEIRAS (frente a Ilha de Moçambique): últimos kilómetros de arena blanda entre cocoteros y manglar para llegar a las playas y a la iglesia portuguesa más antigua del hemisferio sur. Combinar con marea baja para los bancos de arena.",
        "ACCESO AL MONTE BINGA: los últimos 22 km desde Rotanda hasta la aldea de Nbabawa son pista de 4x4 real, con vados; se deja el vehículo en la aldea y se sigue a pie. En lluvias, impracticable.",
        "VARIANTE INTERIOR DEL ZAMBEZE (Caia → Sena → Mutarara → Tete): la orilla sur del Zambeze, con el histórico puente ferroviario Dona Ana (3,6 km, uno de los más largos de África) reconvertido en su día a tráfico rodado. Mezcla de asfalto irregular y tierra; comprobar el estado del cruce antes de comprometerse, ha cambiado varias veces de uso.",
        "MATCHEDJE → LICHINGA: 232 km de pista y asfalto irregular por la meseta del Niassa, sin combustible ni servicios. No es técnico pero sí remoto: es el tramo donde hay que entrar con garrafas llenas.",
        "EN8 NACALA-CHIPONDE (fuera del trazado principal): más de 700 km de tierra y grava a través del interior de Nampula y Niassa, citada por los off-roaders sudafricanos como la gran travesía de tierra del norte. Alternativa al eje Nampula-Cuamba si se busca pista en vez de asfalto.",
        "Conducir por la PLAYA propiamente dicha está restringido y sancionado en Mozambique salvo accesos autorizados de botadura: preguntar en cada camping cuál es el acceso legal antes de bajar el vehículo a la arena de la orilla. Las pistas de arena entre dunas son otra cosa y son perfectamente normales.",
    ],
    senderismo=[
        "MONTE BINGA (2.436 m), el techo de Mozambique: travesía de 2-3 días desde la aldea de Nbabawa (Chimanimani), con campamento intermedio en Mosquito Camp y desvío a las cascadas de Mubvumodzi. Cuarcitas blancas, praderas de altura y vistas a Zimbabue. Guía local en la práctica obligatorio (~450 MT/día) y tasas del parque muy bajas. Prohibido hacer cumbre por libre en la temporada de lluvias.",
        "MONTE NAMULI (2.419 m), sobre Gurué: el segundo pico del país, macizo de granito con bosque de niebla y endemismos que no existen en ningún otro lugar del planeta. Subida de 2 días con guía desde la aldea de Mucunha, entre plantaciones de té. Mucho menos transitado que el Binga.",
        "CASCADAS DE MUROMBODZI y monte Gorongosa: unas 3-4 horas de subida desde Sadjunjira, con guía del parque, entre cafetales de sombra del proyecto comunitario, hasta un salto de unos 80 m en pleno bosque de niebla. La caminata insignia de Gorongosa y la única forma de ver la montaña que alimenta el parque.",
        "ILHA DE MOÇAMBIQUE A PIE: la isla entera mide 3 km por 500 m y se recorre andando en un día largo, de la Fortaleza de São Sebastião y la capilla de Nossa Senhora do Baluarte (1522) a la Cidade de Macuti. No hace falta mover el coche en toda la estancia.",
        "CHINHAMAPERE (Manica): 20-30 minutos de subida hasta el abrigo con arte rupestre san, acompañados por las mujeres médium que custodian el sitio y que hacen la ofrenda previa. Lugar sagrado activo, en la lista indicativa de la UNESCO.",
        "MIRADOR DE PENHA LONGA (Manica): corta ascensión con vista sobre la frontera de Zimbabue y toda la meseta, buen plan de media tarde antes de la salida del país.",
        "SENDEROS DE LA ORILLA DEL LAGO NIASSA (Manda Wilderness, Cóbuè): red de caminos comunitarios entre aldeas de pescadores y bosque de miombo, con posibilidad de hacer varios días enlazando poblados. La caminata más tranquila del viaje, y de las pocas donde el perro puede ir.",
        "DUNAS DE BAZARUTO: si se hace la salida en barco a la isla, la subida a pie a las grandes dunas de arena blanca (más de 100 m sobre el mar) es media jornada y la mejor vista del archipiélago.",
    ],
    acampada=[
        "Costa sur (Tofo, Barra, Vilanculos, Inhassoro, Ponta do Ouro, Ponta Malongane): la mejor oferta de campings a pie de playa de todo el viaje, mucha de ella orientada a overlanders sudafricanos, con parcelas, sombra, duchas y aparcamiento vigilado. Varios admiten perro explícitamente.",
        "Chitengo Camp (Gorongosa): el camping oficial del parque, registrado en iOverlander, con parcelas, piscina y restaurante. Es la base de los safaris guiados; confirmar por adelantado si se puede dejar el perro en la parcela.",
        "Lago Niassa (Metangula, Cóbuè): lodges sencillos con camping a pie de agua, precios bajos y prácticamente nadie. La mejor pernocta del norte.",
        "Ilha de Moçambique: no hay camping en la isla; se duerme en pensiones de la Cidade de Pedra o se acampa en Chocas-Mar, al otro lado de la bahía.",
        "Chocas-Mar y las Cabaceiras: acampada de playa muy tranquila, con acceso 4x4 y casi sin turismo. Buena para varios días con el perro.",
        "Zalala (30 km de Quelimane): playa larguísima de cocoteros con alojamiento sencillo, buena parada en un tramo donde hay poca cosa.",
        "Chimoio y Sussundenga: base con alojamiento para dejar al perro y equipo mientras se hace la travesía del Binga.",
        "Tete: alojamiento urbano si se hace la variante interior; el calor extremo (más de 45 °C en octubre) desaconseja acampar en tienda de techo en esa zona.",
        "Regla general del país: evitar la acampada libre en la EN1 y sus áreas de descanso; buscar siempre recinto cerrado o vigilado, especialmente en el corredor Xai-Xai–Maputo.",
    ],
    visado=[
        "ESPAÑA ESTÁ EN LA LISTA DE EXENCIÓN de visado de Mozambique (decreto 10/2023, en vigor desde 2023, junto con otros 28 países): estancia de 30 días, prorrogable 30 más justificándolo ya dentro del país.",
        "PERO desde el 24 de abril de 2025 los exentos deben completar un REGISTRO ELECTRÓNICO PREVIO AL VIAJE con al menos 48 horas de antelación. Sin ese registro, la exención no sirve. Verificar la plataforma oficial vigente y guardar el justificante impreso.",
        "Hay además una tasa de tramitación en la llegada (del orden de 650 MZN según la nota original del programa): llevar efectivo. Importe por confirmar en 2027.",
        "Si por algún motivo la exención no aplicara, sigue existiendo visado a la llegada (~50 USD) y eVisa previa. Confirmar 30-60 días antes que el puesto remoto de MATCHEDJE aplica la exención y el registro previo sin problemas: es un puesto pequeño y no es evidente que tenga el sistema al día.",
        "30 días es MUY JUSTO para los ~5.300 km del eje principal más las paradas. Planificar la prórroga de 30 días en Nampula o Beira, o recortar el itinerario.",
        "Certificado internacional de fiebre amarilla exigible si se procede de país con riesgo: comprobar el estatus de Tanzania en el momento del cruce.",
    ],
    fronteras_rows=[
        ("Entrada (recomendada)", "Matchedje / Puente de la Unidad 2 (Tanzania → Niassa)", "06:00-18:00 los 7 días. GPS -11.5800, 35.4295 (11°34′46″S 35°25′47″E). Es el Unity Bridge 2 sobre el Rovuma, entre Kivikoni y Lupilichi/Segunda Congresso. Songea a 130 km al norte, Lichinga a 232 km al sur, SIN combustible entre medias. Fama de contrabando de rubíes: registro de vehículo probable, paciencia y documentación impecable."),
        ("Entrada (descartada)", "Negomano/Mtambaswala — Puente de la Unidad 1", "07:30-16:00. GPS -11.4193, 38.4962. Puente de 720 m y dos carriles inaugurado en 2010, a ~180 km de Mtwara vía Masasi. DESCARTADO: entra en el distrito de Mueda, Cabo Delgado, nivel 4."),
        ("Entrada (descartada)", "Kilambo/Namoto — barcaza del Rovuma", "Mozambique 07:00-19:00; Tanzania SOLO 07:00-08:00. Barcaza para ~6 vehículos 4x4, dependiente de marea (≥3 m). DESCARTADO por logística y por seguridad (Quionga)."),
        ("Entrada (plan B)", "Zóbuè/Mwanza (Malaui → Tete)", "Solo si se renuncia al norte y se reencamina la ruta global por Malaui. Asfalto, corredor de camiones. Obliga a replantear Tanzania y Malaui."),
        ("Salida", "Machipanda/Forbes (→ Zimbabue)", "GPS -19.0059, 32.7171, a 95 km de Chimoio y 8 km de Mutare. Corredor Harare-Beira: colas de camiones que llegan a bloquear la carretera, llegar temprano. Horario: fuentes discrepan entre 06:00-20:00 y 24 h desde 2024 — confirmar 72 h antes."),
    ],
    vehiculos=[
        "CPD no obligatorio: se expide un permiso temporal de importación (TIP) en la propia frontera para cada vehículo. Llevar el CPD igualmente como respaldo.",
        "SEGURO DE TERCEROS MOZAMBIQUEÑO OBLIGATORIO para matrícula extranjera: se compra en la frontera o por internet antes de cruzar (Hollard, DriveMoz). Circular sin él es infracción sancionable y es de los primeros papeles que pide la policía.",
        "EQUIPAMIENTO OBLIGATORIO que revisa la policía: DOS triángulos de emergencia rojos y DOS chalecos reflectantes amarillos (uno por ocupante delantero), además de la documentación del vehículo y la autorización del titular si no es propio. Los vehículos extranjeros deben llevar el distintivo de nacionalidad.",
        "Permiso internacional de conducir: llevarlo siempre junto al carné español. Se conduce por la IZQUIERDA.",
        "Carpeta física con copias impresas de todo: pasaportes, registro previo de entrada, TIP, seguro, permisos. En Mozambique el papel impreso resuelve controles que la pantalla del móvil no resuelve.",
        "Multas: si la infracción es real, pagarla y EXIGIR RECIBO siempre; si es inventada, mantener la calma, pedir identificación y proponer ir a la comisaría. Los foros overland coinciden en que el recibo es la barrera que separa la multa del soborno.",
        "Límites de velocidad orientativos: 60 km/h en población, 80-100 km/h en carretera. Radares y controles frecuentes en la EN1, sobre todo a la entrada y salida de cada pueblo.",
        "Ruedas y arena: llevar compresor, desinflador y planchas. Entre Inhassoro, Barra y Ponta do Ouro se pasan días enteros a baja presión.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Registro y autorización previa ante el Instituto de Aviação Civil de Moçambique (IACM) antes de cualquier vuelo. Régimen exacto y tasas por confirmar en 2027.",
        "PROHIBICIÓN ABSOLUTA autoimpuesta: nada de drones en Cabo Delgado ni en Niassa (zonas de operación militar), ni cerca de instalaciones portuarias, de gas o militares en Pemba, Palma, Nacala, Beira y Maputo.",
        "No volar dentro de parques nacionales (Gorongosa, Bazaruto, Maputo NP) sin autorización expresa del gestor del parque, además de la del IACM.",
        "Los mejores sitios para volar con papeles en regla son la costa fuera de parques: Chocas-Mar, Zalala, península de San Sebastián, Barra y las puntas del sur.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo y operativo en Mozambique; es la solución práctica para el tramo norte (Matchedje-Lichinga-Cuamba-Gurué), donde la cobertura móvil es irregular o inexistente.",
        "SIM local de respaldo: Vodacom (mejor cobertura general), Movitel (mejor en zonas rurales) y Tmcel. Datos baratos; registro del SIM con pasaporte.",
        "Comprobar el plan de itinerancia regional antes de entrar: la política de roaming de Starlink en África ha cambiado varias veces y conviene confirmarla 30 días antes.",
    ],
    perro_intro=[
        "PERMISO DE IMPORTACIÓN PREVIO del Ministerio de Agricultura de Mozambique: hay que tramitarlo con antelación, NO se resuelve en la frontera.",
        "Microchip ISO de 15 dígitos, vacuna antirrábica administrada al menos 30 DÍAS antes de la entrada (las vacunas plurianuales NO se aceptan como tales: puede hacer falta revacunar), certificado sanitario internacional emitido dentro de los 10 días previos, y vacunas de moquillo, hepatitis, parvovirosis y leptospirosis, más desparasitación interna y externa. Todos los documentos deben citar el número de microchip.",
        "ATENCIÓN, PUNTO A RESOLVER: las guías de importación de mascotas describen el procedimiento pensando en la llegada por el aeropuerto de Maputo. La entrada por un puesto terrestre remoto como Matchedje no está documentada: hay que confirmar por escrito con los servicios veterinarios mozambiqueños que ese puesto puede despachar el animal, o buscar despacho alternativo.",
        "La buena noticia: fuera de los parques nacionales, Mozambique es el mejor país del bucle para el perro. Toda la costa —Chocas-Mar, Zalala, Tofo, Barra, Vilanculos, Inhassoro, Ponta do Ouro, Malongane— tiene playas abiertas y campings que lo admiten.",
        "Calor y humedad extremos en la costa y en Tete: sombra, agua constante y evitar las horas centrales. Cocodrilos en desembocaduras del lago Niassa y del Zambeze: preguntar siempre antes de dejarlo acercarse al agua dulce.",
        "Veterinarios reales solo en Maputo, Beira y Nampula. Llevar botiquín canino completo, antiparasitario de garrapata al día y tratamiento de emergencia para picadura.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "MALARIA en todo el país, todo el año, con transmisión especialmente intensa en la costa, el valle del Zambeze y el norte: profilaxis a valorar con Sanidad Exterior, más mosquitera, repelente y ropa cubierta al atardecer. Es el riesgo sanitario número uno del tramo.",
        "CÓLERA: brotes recurrentes y estacionales, agravados tras cada ciclón o inundación. No beber agua no embotellada o no tratada en ninguna provincia, ni hielo de origen dudoso.",
        "Fiebre amarilla: certificado exigible si se procede de país con riesgo — comprobar el estatus de Tanzania en el momento del cruce.",
        "Bilharzia en aguas dulces estancadas del Zambeze y de los ríos del interior. El lago Niassa se considera de riesgo bajo en zonas de corriente y orilla rocosa, pero no nulo: preguntar en cada sitio.",
        "Sanidad: Hospital Central de Maputo y Clínica Cruz Azul en la capital; Hospital Central da Beira en el centro; Hospital Central de Nampula en el norte. Entre Lichinga y Nampula solo hay hospitales rurales. Seguro con EVACUACIÓN MÉDICA REAL imprescindible: la referencia regional para lo serio es Sudáfrica.",
        "Sol, calor y deshidratación: Tete supera los 45 °C en octubre y la humedad costera es alta todo el año. Sal, sombra y planificación de horarios.",
    ],
    seguridad_intro=("Mozambique se divide en dos países distintos a efectos de seguridad. El norte-nordeste (Cabo Delgado, la Reserva de Niassa y la franja de Memba/Erati) está en guerra abierta y queda excluido sin excepción. "
                     "El resto —Niassa occidental, Nampula, Zambézia, Sofala, Manica, Inhambane, Gaza y Maputo— es un país manejable con precaución normal, donde los problemas reales son la carretera, la policía de tráfico y la delincuencia urbana."),
    seguridad=[
        "Zonas EXCLUIDAS sin excepción: toda la provincia de Cabo Delgado, la Reserva Especial de Niassa, y los distritos de Memba y Erati (norte de Nampula). No hay versión de la ruta que entre ahí.",
        "Artefactos explosivos improvisados: ISIS-Mozambique los ha convertido en táctica central en las carreteras del interior de Cabo Delgado. Es otra razón por la que la entrada por Negomano queda descartada: el riesgo no está solo en los pueblos, está en la pista.",
        "No conducir de noche en ningún tramo del país: ni por la fauna ni por los baches ni por los atracos ocasionales. La EN1 entre Xai-Xai y Maputo tiene antecedentes concretos de robo a vehículos.",
        "Maputo y Beira: delincuencia urbana con cuchillo y, en menor medida, arma de fuego. Aparcamiento vigilado, nada de valor a la vista en el coche, no exhibir cámaras ni móviles en la calle.",
        "Policía: el FCDO documenta casos de acoso e intimidación por parte de agentes, incluidas peticiones de soborno. Documentación impecable, tono cordial, recibo siempre, y anotar número de placa si la cosa se tuerce.",
        "Tensión política: las protestas postelectorales de 2024-2025 dejaron más de 300 muertos y se manifestaron sobre todo en forma de CORTES DE CARRETERA, barricadas y paros generales, especialmente en el corredor de Maputo y en las ciudades. El juicio a Venâncio Mondlane sigue abierto. En caso de rebrote: no atravesar concentraciones, no fotografiar manifestaciones ni policía, y esperar en un sitio seguro a que se despeje la carretera.",
        "Minas antipersona: las conocidas están limpias y el país se declaró libre de minas en 2015, pero sigue habiendo riesgo residual en zonas remotas del centro y del sur. No salir de pistas marcadas en el interior rural.",
        "Ciclones y crecidas: entre noviembre y abril, y sobre todo de enero a marzo, comprobar el parte diariamente. Un ciclón corta carreteras y tira puentes; la EN1 se ha partido en dos varias veces por esa causa.",
        "Aislamiento del tramo Matchedje-Lichinga y del interior de Zambézia: llevar combustible, agua y comida de reserva, y dejar el itinerario avisado.",
    ],
    agua=[
        "Nampula, Beira, Vilanculos, Inhambane y Maputo: agua embotellada sin problema en supermercados.",
        "Recarga del depósito de uso general: campings y lodges de toda la costa sur (Tofo, Barra, Vilanculos, Inhassoro, Ponta do Ouro), Chitengo, Metangula y las ciudades permiten llenar con manguera. Confirmar en recepción.",
        "Tramo Matchedje → Lichinga (232 km) y el interior de Zambézia: sin garantía, entrar con los depósitos al 100%.",
        "Por los brotes de cólera, TRATAR SIEMPRE el agua que no venga embotellada, aunque proceda de un grifo de lodge. Filtro más desinfección química o UV.",
    ],
    combustible=[
        "Plazas fiables: Lichinga, Cuamba, Nampula, Nampula-Monapo, Quelimane, Mocuba, Caia, Beira, Chimoio, Tete, Vilanculos, Inhambane, Xai-Xai y Maputo.",
        "Tramos sin garantía: Songea → Matchedje → Lichinga (~360 km), Lichinga → Cuamba (~340 km) y las pistas de arena del extremo sur, donde no hay estación entre Katembe y Ponta do Ouro. Llevar garrafas llenas en los tres.",
        "Regla de los overlanders en Mozambique: a partir de Vilanculos hacia el norte, repostar al llegar al 50% del depósito, no al cuarto.",
        "La conducción en arena dispara el consumo: contar hasta un 40-50% más en los tramos de San Sebastián, Barra y Ponta do Ouro respecto al asfalto.",
        "Pago: efectivo en metical en las estaciones pequeñas; VISA funciona mejor que Mastercard en el país. Cajeros fiables en las capitales provinciales.",
    ],
    experiencias_intro="Relatos y datos reales de otros overlanders sobre Mozambique, con especial atención al cruce del Rovuma, a la policía de tráfico y a las pistas de arena, que es lo que no aparece en las guías oficiales:",
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Entrada por Matchedje", "Confirmar 30-60 días antes que el puesto está operativo, que aplica la exención de visado española y el registro electrónico previo, y que puede despachar el permiso temporal de importación de los dos vehículos"),
        ("El perro en frontera terrestre", "Confirmar por escrito con los servicios veterinarios mozambiqueños que Matchedje puede despachar la entrada del perro; las guías describen solo el aeropuerto de Maputo. Tramitar el permiso de importación previo del Ministerio de Agricultura"),
        ("El backtrack del sur (~1.300 km)", "DECISIÓN DEL DUEÑO: ¿se baja hasta Ponta do Ouro y se vuelve a subir a Machipanda, o se corta en Vilanculos y se entra a Zimbabue desde Chimoio, ahorrando ~2.000 km pero renunciando a Tofo, Maputo y las dunas del sur? Alternativa: reordenar la ruta global para salir de Mozambique hacia Sudáfrica por Ressano Garcia o Kosi Bay y hacer Zimbabue más tarde"),
        ("Visado de 30 días vs. 5.300 km", "30 días no dan para el eje completo con paradas. Decidir entre tramitar la prórroga de 30 días dentro del país (Nampula o Beira) o recortar el itinerario antes de entrar"),
        ("Gorongosa sin autoconducción", "Reservar safari guiado con antelación en safari@gorongosa.net y confirmar que se puede dejar el perro en la parcela de Chitengo con uno de los tres viajeros"),
        ("Monte Binga", "Contactar guía local con antelación y confirmar tasas y estado de la pista de Rotanda a Nbabawa; imposible en temporada de lluvias"),
        ("Horario de Machipanda", "Las fuentes discrepan entre 06:00-20:00 y apertura 24 h desde enero de 2024: confirmar 72 h antes de la salida"),
        ("Permisos de conducción en playa", "Aclarar qué accesos a la arena de la orilla son legales en Inhambane, Vilanculos y Ponta do Ouro antes de bajar el vehículo a la playa"),
        ("Seguridad de la franja de Nampula", "Revalidar el aviso oficial sobre Memba y Erati 72 h antes de subir a Ilha de Moçambique; si la línea se hubiera movido al sur, Ilha cae y hay que replantear el norte entero"),
        ("Situación política", "Seguir el calendario del juicio a Venâncio Mondlane y el clima social antes de fijar fechas: una sentencia puede reactivar cortes de carretera generalizados como los de 2024-2025"),
        ("Dron", "Tramitar autorización del IACM si se quiere volar; confirmar régimen y tasas vigentes en 2027"),
        ("Fotos pendientes de sustituir", "Lichinga, lago Niassa, Cuamba, Gurué/Namuli, Nampula y Manica/Chinhamapere usan imágenes de la región o de otro lugar del país, no del propio sitio"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Los avisos de seguridad sobre Cabo Delgado, Niassa y el norte de Nampula deben revalidarse obligatoriamente antes de entrar al país.",
    emergency="Emergencia consular española (Maputo, 24 h): (+258) 84 32 82 900 · Embajada de España en Maputo: (+258) 21 49 20 25/27/30 · Emergencias generales en Mozambique: 119 (policía), 198 (bomberos).",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

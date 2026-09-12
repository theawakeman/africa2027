# -*- coding: utf-8 -*-
"""Esuatini — ficha completa (12 sep 2026): ALTERNATIVA (no está en la ruta fija).
Enclave entre Sudáfrica y Mozambique: encaja como desvío CORTO entre ambos, sin
salirse del corredor. Reino tradicional vivo, montaña, rinocerontes y la mina más
antigua del mundo."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"
NOFOTO = "Sin fotografía verificada en esta revisión (ver pendientes)"

POIS = [
    dict(n=1, name="Ngwenya · la mina más antigua del mundo", cat="Patrimonio UNESCO", prio="Alta", dog="por confirmar", time="medio día",
         lat=-26.2017, lon=31.0339,
         desc="Nada más cruzar la frontera de Oshoek, en la loma de Bomvu Ridge, está el yacimiento minero más antiguo conocido de la humanidad: LA LION CAVERN, datada por radiocarbono entre hace 41.000 Y 43.000 AÑOS. Los primeros habitantes no buscaban hierro sino OCRE ROJO y especularita —hematites de brillo metálico— para cosmética y ritual: es decir, la minería empezó en el mundo por motivos simbólicos, no utilitarios. La mina moderna de hierro funcionó de 1964 a 1977 y de 2011 a 2014, sacó unos 20 millones de toneladas con mineral de hasta el 60% de hierro, y dejó un cráter espectacular. El centro de visitantes abrió en 2005 y ARDIÓ EN 2018, destruyendo artefactos antiguos: confirmar qué se puede visitar hoy. La gestiona la Eswatini National Trust Commission, dentro de Malolotja.",
         credit=NOFOTO, source=""),
    dict(n=2, name="Fábrica de vidrio de Ngwenya", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1–2 horas",
         lat=-26.2000, lon=31.0333,
         desc="A un paso de la frontera y de la mina antigua, una vidriería artesanal que trabaja EXCLUSIVAMENTE CON VIDRIO RECICLADO recogido en todo el país: se ve soplar las piezas desde una pasarela sobre el taller, y el resultado —animales, vasos, cuencos— es el souvenir clásico de Esuatini y una de las pocas industrias artesanales de África austral con proyección internacional. Es una parada de una hora que además tiene cafetería y aparcamiento cómodo: buen sitio para estirar las piernas y el perro justo después del papeleo de frontera. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=3, name="Reserva Natural de Malolotja", cat="Naturaleza", prio="Alta", dog="por confirmar", time="2–3 noches",
         lat=-26.1333, lon=31.1167,
         desc="EL MEJOR SENDERISMO DEL PAÍS Y DE LOS MEJORES DE ÁFRICA AUSTRAL: 180 km² de montaña abierta en la frontera noroccidental, con solo 25 km de carretera dentro y una red de senderos que permite caminatas de un día o travesías de varios días con vivac. Dentro está el monte Ngwenya (1.829 m, segunda cumbre del país) y las CATARATAS DE MALOLOTJA, el salto más alto de Esuatini con 89 m. Es paisaje de pradera de altura, gargantas y flores —un santuario botánico— con cebras, ñus, antílopes y el buitre del Cabo. Al no haber grandes depredadores se camina en libertad, sin ranger obligatorio: una rareza en esta parte de África. Coordenadas aproximadas, por confirmar.",
         credit="Wikimedia Commons", source=W + "Malolotja%20Scenery%20(31722500693).jpg?width=900"),
    dict(n=4, name="Malolotja Canopy Tour · la tirolina del cañón", cat="Naturaleza", prio="Alta", dog="prohibido", time="medio día",
         lat=-26.1350, lon=31.1200,
         desc="Dentro de Malolotja, un recorrido de tirolinas de plataforma en plataforma sobre el cañón del río Majolomba, con un PUENTE COLGANTE de unos 50 m de altura sobre la garganta como remate. Se anuncia como la tirolina más larga de África austral — dato POR CONFIRMAR con el operador, pero en cualquier caso es la actividad de adrenalina del país y una forma imbatible de ver el cañón. Dura unas dos o tres horas, con equipo y guías incluidos. No apto para el perro, evidentemente: se queda en el camping de la reserva. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=5, name="Presa de Maguga y el valle del Komati", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-26.0333, lon=31.2167,
         desc="Una presa de escollera de 115 m sobre el río Komati, al norte de Malolotja, que embalsa un lago serpenteante entre montañas y crea uno de los mejores miradores de carretera del país. Hay lodge y camping en la orilla, pesca de black bass y paseos en barca, y la carretera MR1 que baja desde Piggs Peak es una conducción preciosa de curvas continuas. Es la parada lógica entre Malolotja y el arte rupestre de Nsangwini. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=6, name="Arte rupestre de Nsangwini", cat="Cultura", prio="Media", dog="por confirmar", time="medio día",
         lat=-26.0000, lon=31.2000,
         desc="El único abrigo con arte rupestre san abierto al público en Esuatini, en un balcón de roca sobre el valle del Komati al que se baja por un sendero corto pero empinado. Tiene un panel excepcional con FIGURAS ALADAS —seres humanos con alas, interpretados como chamanes en trance— y elefantes, antílopes y cazadores, con varios miles de años de antigüedad. Lo gestiona la comunidad local, que pone el guía: es un proyecto comunitario pequeño y muy honesto, y de las visitas más memorables del país. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=7, name="Cascadas de Phophonyane", cat="Naturaleza", prio="Media", dog="por confirmar", time="1 noche",
         lat=-25.9500, lon=31.2000,
         desc="Reserva privada junto a Piggs Peak en torno a una sucesión de saltos y pozas del río Phophonyane, encajados en un bosque autóctono de ribera con más de 250 especies de aves. Hay senderos cortos, pozas naturales en las que bañarse y un lodge con casas de campaña bajo los árboles. Es el rincón fresco y verde del norte, y un contraste absoluto con el lowveld seco del este. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=8, name="Mbabane", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-26.3167, lon=31.1333,
         desc="La capital administrativa, en el highveld a unos 1.100 m, con clima fresco y un tamaño muy manejable: bancos, supermercados sudafricanos, talleres, hospitales y el mercado de artesanía como principal atractivo urbano. No es una ciudad monumental —la capital real, la de la monarquía, es Lobamba—, pero es donde se resuelven las gestiones. Desde aquí se sube a Sibebe en veinte minutos.",
         credit=NOFOTO, source=""),
    dict(n=9, name="Sibebe · el monolito de granito", cat="Naturaleza", prio="Alta", dog="por confirmar", time="medio día",
         lat=-26.2833, lon=31.1667,
         desc="A 10 km de Mbabane se levanta una cúpula de granito desnudo que se describe como EL SEGUNDO MONOLITO MÁS GRANDE DEL MUNDO DESPUÉS DE ULURU y el mayor plutón de granito expuesto del planeta: 350 m de pared sobre el valle del Mbuluzi. Y la gracia es que SE SUBE A PIE, sin material, por la roca desnuda: una subida de dos o tres horas con tramos en los que se trepa a cuatro patas por pura fricción, y una cumbre plana con vistas de 360 grados sobre todo el highveld. Cada año se celebra el «Sibebe Survivor», una marcha benéfica multitudinaria hasta arriba. No hay recinto de parque nacional: es terreno comunitario con guía local. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=10, name="Valle de Ezulwini", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-26.4333, lon=31.1667,
         desc="«El valle del cielo»: el corredor entre Mbabane y Manzini donde se concentra casi todo lo que hay que ver en Esuatini, y la base natural del desvío. Reúne el mercado de artesanía de Ezulwini, las fuentes termales de Cuddle Puddle, hoteles y campings, el santuario de Mlilwane, el poblado cultural de Mantenga y, un poco más allá, Lobamba con el Parlamento, el Museo Nacional, el memorial del rey Sobhuza II y el recinto real de Ludzidzini donde se celebran la Umhlanga y la Incwala. Todo en unos veinte kilómetros: se puede dormir en un sitio y no mover el vehículo en tres días.",
         credit=NOFOTO, source=""),
    dict(n=11, name="Mantenga · poblado cultural suazi y las cascadas", cat="Cultura", prio="Alta", dog="por confirmar", time="medio día",
         lat=-26.4500, lon=31.1833,
         desc="Reserva natural de la Eswatini National Trust Commission que contiene la mejor reconstrucción de una ALDEA SUAZI TRADICIONAL de mediados del siglo XIX: dieciséis estructuras de paja y barro levantadas con técnica auténtica —el kraal de ganado, las cabañas de las esposas, el corral, el granero— con visita guiada que explica cómo funcionaba de verdad la familia extensa y la homestead. Dos veces al día hay espectáculo de DANZA SIBHACA, que no es un montaje para turistas sino la danza competitiva real de los hombres suazis. Al lado están las cascadas de Mantenga, sobre el río Lusushwana, y enfrente se ve la silueta de la Roca de la Ejecución (Nyonyane). Coordenadas aproximadas, por confirmar.",
         credit="Wikimedia Commons", source="https://commons.wikimedia.org/wiki/Special:FilePath/Mantenga%20nature%20reserve%20(37097743884).jpg?width=900"),
    dict(n=12, name="Santuario de Vida Silvestre de Mlilwane", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=-26.4691, lon=31.1619,
         desc="4.560 hectáreas en el valle de Ezulwini y el área protegida más antigua del país, rehabilitada por la familia Reilly sobre antiguas tierras de cultivo y minas de estaño. Su singularidad es que NO TIENE GRANDES DEPREDADORES, así que aquí se puede recorrer la reserva A PIE, EN BICICLETA DE MONTAÑA Y A CABALLO entre cebras, ñus, impalas, facóqueros y antílopes — algo imposible en cualquier parque de Sudáfrica o Botsuana. Hay manantiales cálidos, el pico Nyonyane con la Roca de la Ejecución (desde la que, según la tradición, se despeñaba a los condenados), y un camping y alojamiento en cabañas de paja con facóqueros pastando entre las tiendas. Es LA joya del desvío para quien quiere fauna sin encierro.",
         credit="Wikimedia Commons", source=W + "Plains%20zebra%20in%20Mlilwane%20Wildlife%20Sanctuary%2001.jpg?width=900"),
    dict(n=13, name="Manzini", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-26.4833, lon=31.3667,
         desc="La mayor ciudad y el corazón comercial e industrial del país, a media hora de Ezulwini. Su atractivo real es EL MERCADO: el de productos frescos abajo y, arriba, el de artesanía, que los jueves y viernes por la mañana es cuando llegan los artesanos rurales y es el mejor de Esuatini con diferencia. Es también el nudo de carreteras del país —de aquí salen las vías al este (Hlane, Mkhaya, Mozambique) y al sur (Lavumisa/Golela y KwaZulu-Natal)— y el sitio con más talleres y repuestos.",
         credit=NOFOTO, source=""),
    dict(n=14, name="Reserva de Mkhaya · el rinoceronte negro", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 noches",
         lat=-26.6250, lon=31.7375,
         desc="El sitio con mejor reputación de África austral para ver RINOCERONTE NEGRO de cerca, y una reserva con una historia particular: se creó en 1979 para salvar de la extinción al GANADO NGUNI autóctono, y acabó convertida en refugio de especies amenazadas. NO SE PUEDE ENTRAR CON VEHÍCULO PROPIO: hay que dejar el coche en el punto de encuentro de Phuzumoya y todo se hace guiado y con reserva previa, en vehículo abierto o a pie. Está gestionada y patrullada íntegramente por personal suazi y se autofinancia solo con los ingresos de visitantes. Tiene rinoceronte negro y blanco, elefante, búfalo, antílopes raros y muy pocas plazas: es cara y hay que reservarla con antelación, pero quien va la pone por encima de casi cualquier parque de la región.",
         credit=NOFOTO, source=""),
    dict(n=15, name="Parque Nacional Real de Hlane", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=-26.2500, lon=31.8833,
         desc="300 km² en el lowveld nororiental, a unos 67 km de Manzini: el ÁREA PROTEGIDA MÁS GRANDE DEL PAÍS y el antiguo coto de caza real, que hoy el rey Mswati III mantiene en fideicomiso para la nación. «Hlane» significa «tierra salvaje», y el nombre se lo puso el rey Sobhuza II. Tiene LEONES, ELEFANTES, RINOCERONTE BLANCO, jirafas y guepardos reintroducidos, y en la estación seca los ñus, cebras e impalas se concentran en las charcas. Para los aficionados a las aves es excepcional: LA MAYOR DENSIDAD DE BUITRE DORSIBLANCO NIDIFICANTE DE ÁFRICA y el punto de nidificación más meridional del marabú. Se recorre con vehículo propio por pistas llanas (mejor con altura libre) y tiene dos campamentos: Ndlovu, junto a la entrada, y Bhubesi, al norte. Coordenadas aproximadas, por confirmar.",
         credit="Wikimedia Commons", source="https://commons.wikimedia.org/wiki/Special:FilePath/Hlane%20Royal%20National%20Park%20banner%20White%20Rhinos%20wallowing%20and%20resting%20in%20the%20bushes.jpg?width=900"),
    dict(n=16, name="Lubombo y el Shewula Mountain Camp", cat="Naturaleza", prio="Media", dog="por confirmar", time="1 noche",
         lat=-26.1333, lon=31.9500,
         desc="En el escarpe de los montes Lubombo, contra la frontera de Mozambique, está el primer campamento comunitario del país: lo gestiona íntegramente la comunidad de Shewula, con cabañas sencillas asomadas al borde de la meseta y vistas al valle del Mbuluzi y a Hlane. Se hacen paseos con guías del pueblo, visita a curanderos tradicionales y a la escuela, y se come comida suazi de verdad. Es la parada lógica antes de salir hacia Mozambique por Lomahasha, y el contrapunto honesto a los lodges del valle de Ezulwini. Cerca queda la reserva de Mlawula y las gargantas del Mbuluzi. Coordenadas aproximadas, por confirmar.",
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
    ("Frontera · Ngwenya / Oshoek (con Sudáfrica, Mpumalanga)", "Frontera", -26.2000, 31.0167,
     "EL PASO PRINCIPAL del país, en la carretera de Johannesburgo y Mbabane, y el más cercano a la mina de Ngwenya y a Malolotja. Es el más transitado y el de horario más amplio (aprox. 07:00–22:00, CONFIRMAR). Coordenadas aproximadas."),
    ("Frontera · Matsamo / Jeppe's Reef (con Sudáfrica, Mpumalanga)", "Frontera", -25.7167, 31.3167,
     "Paso del norte, el enlace natural con el Kruger por Malelane. Útil si el desvío se encaja viniendo del Kruger. Horario limitado. Coordenadas aproximadas."),
    ("Frontera · Lavumisa / Golela (con Sudáfrica, KwaZulu-Natal)", "Frontera", -27.3167, 31.9167,
     "Paso del sur, en la N2 hacia Durban y el Drakensberg. Es la salida lógica si el desvío se encadena con Lesoto y el sur de Sudáfrica. Horario amplio. Coordenadas aproximadas."),
    ("Frontera · Lomahasha / Namaacha (con Mozambique)", "Frontera", -25.9833, 31.9833,
     "El paso del noreste hacia Namaacha y Maputo: la salida directa a Mozambique sin volver a entrar en Sudáfrica, que es lo que convierte a Esuatini en un desvío CORTO y no en un rodeo. Confirmar horario. Coordenadas aproximadas."),
    ("Frontera · Mhlumeni / Goba (con Mozambique)", "Frontera", -26.2333, 31.9833,
     "Alternativa a Lomahasha, más al sur y con carretera nueva hacia Maputo; suele ser más rápido. Coordenadas aproximadas, horario por confirmar."),
    ("Embajada de España en Maputo (también embajada en Esuatini)", "Consular", -25.9667, 32.5833,
     "No hay embajada de España en Esuatini: la competencia es de la Embajada de España en Maputo (Mozambique), que es además el país al que se sale por el este. Confirmar el teléfono de emergencia consular vigente antes de entrar."),
    ("Mbabane Government Hospital / clínicas privadas de Ezulwini", "Hospital", -26.3167, 31.1333,
     "Red sanitaria limitada. Para cualquier cosa seria, la práctica es evacuación a Nelspruit/Mbombela o Johannesburgo (Sudáfrica), que están cerca. Comprobar que el seguro cubre la evacuación transfronteriza."),
    ("Combustible · Mbabane, Ezulwini, Manzini, Piggs Peak, Simunye, Big Bend", "Combustible", -26.4833, 31.3667,
     "Red buena y fiable para el tamaño del país (Galp, Total, Puma, Engen), con precios habitualmente algo más baratos que en Sudáfrica. No hay ningún gap de autonomía relevante: Esuatini mide 200 km de norte a sur."),
    ("Agua potable y de uso general · Ezulwini, Mbabane, Manzini", "Agua potable", -26.4333, 31.1667,
     "Agua embotellada en supermercados de todo el país. Campings de Mlilwane, Malolotja, Hlane, Maguga y Phophonyane permiten llenar el depósito de uso general con manguera; confirmar en recepción."),
]

DRONE_CALLOUT = ("warn", "Menos restrictivo que Uganda o Ruanda, pero hay dos líneas rojas: la monarquía y las ceremonias",
                 "Esuatini regula los drones a través de la Eswatini Civil Aviation Authority (ESWACAA), con registro y autorización previa: el régimen es de los más manejables de la ruta, muy lejos de la dureza de Uganda o Ruanda. Ahora bien, hay dos líneas rojas absolutas: NO se vuela sobre los recintos reales (Lobamba, Ludzidzini, los palacios) ni sobre las ceremonias de la Umhlanga y la Incwala, y no se vuela dentro de las áreas protegidas de Big Game Parks (Hlane, Mkhaya, Mlilwane) ni de la Eswatini National Trust Commission sin permiso escrito. Esuatini es una monarquía absoluta y la sensibilidad en torno a la figura del rey es máxima: un dron sobre un acto real no es una infracción administrativa, es un problema serio. El régimen exacto está POR CONFIRMAR con la ESWACAA.")

STARLINK_CALLOUT = ("warn", "Disponibilidad por confirmar — pero es un país pequeño con buena red móvil",
                    "El estado comercial de Starlink en Esuatini debe confirmarse antes del viaje: no se ha podido verificar en esta revisión. En la práctica importa poco: el país mide unos 200 km de norte a sur, la red de Eswatini Mobile y MTN Eswatini cubre bien el corredor Mbabane–Ezulwini–Manzini y razonablemente el lowveld, y desde casi cualquier punto se está a pocas horas de Sudáfrica o Mozambique. Comprar SIM local con pasaporte a la entrada es barato y resuelve el desvío entero.")

DOG_MATRIX = [
    ("Hlane y Mkhaya (Big Game Parks)", "prohibido",
     "Hlane tiene leones, elefantes y rinocerontes, y Mkhaya rinoceronte negro y búfalo: la prohibición es de seguridad y es firme. En Mkhaya, además, NO se entra con vehículo propio, así que el perro se quedaría solo en el aparcamiento de Phuzumoya — no es opción. Plan B: base en Simunye o Manzini con turnos entre los tres viajeros."),
    ("Mlilwane", "prohibido",
     "Aunque NO tiene grandes depredadores y se recorre a pie y en bici, es reserva de Big Game Parks y no admite mascotas. MERECE LA PENA PREGUNTAR POR ESCRITO de todas formas: es la reserva del sur de África donde la excepción tendría más sentido, porque el argumento de seguridad no aplica. Está en los pendientes."),
    ("Malolotja, Mantenga, Mlawula (Eswatini National Trust Commission)", "por confirmar",
     "Gestión distinta de la de Big Game Parks y SIN grandes depredadores en Malolotja. La política de mascotas hay que preguntarla reserva por reserva a la ENTC: es la vía más prometedora del desvío para caminar con el perro en naturaleza."),
    ("Sibebe, Nsangwini, Maguga, valle del Komati", "por confirmar",
     "No son recintos de parque sino terreno comunitario o privado con guía local: la decisión la toma la comunidad o el propietario, y suele ser flexible. Preguntar en el momento; Sibebe es una subida abierta por roca y sería una caminata perfecta con el perro si lo permiten."),
    ("Ezulwini, Mbabane, Manzini, Ngwenya", "permitido con condiciones",
     "Zonas urbanas y de valle sin problema con correa. Varios lodges y campings del valle de Ezulwini admiten perro — confirmar por escrito antes. Hay veterinarios en Mbabane y Manzini, y la red sudafricana de Mbombela está a dos horas."),
    ("Frontera · régimen SACU", "permitido con condiciones",
     "ES EL MEJOR DATO DE TODO EL BLOQUE SUR: el dosier canino del proyecto recoge un TESTIMONIO DIRECTO DE CRUCE TERRESTRE CON PERRO a Esuatini — «entrada sencilla, el permiso funcionó como se esperaba», y salida y reentrada a Sudáfrica descritas como «un proceso fácil». AVISO: el permiso nombraba el país de destino y LOS FUNCIONARIOS DE FRONTERA QUISIERON QUEDÁRSELO en lugar de devolverlo. Pedir copia sellada o llevar un permiso por país."),
]

SOURCES = [
    ("thingstodoineswatini.com · requisitos de entrada 2026", "https://thingstodoineswatini.com/entry-requirements/"),
    ("Embajada de España en Maputo · también embajada en Esuatini", "https://www.exteriores.gob.es/Embajadas/maputo/es/Embajada/Paginas/Tambien-somos-tu-embajada-en.aspx"),
    ("Drive South Africa · guía de cruces fronterizos con Sudáfrica", "https://www.drivesouthafrica.com/blog/south-africa-border-crossing-guide/"),
    ("The Kingdom of Eswatini · web oficial de turismo", "https://www.thekingdomofeswatini.com/"),
    ("Big Game Parks · Hlane, Mkhaya y Mlilwane (reservas y tarifas)", "https://www.biggameparks.org/"),
    ("Eswatini National Trust Commission · Malolotja, Mantenga, Mlawula, Ngwenya", "https://www.entc.org.sz/"),
    ("Wikipedia · Parque Nacional Real de Hlane (300 km², leones, buitres dorsiblancos)", "https://en.wikipedia.org/wiki/Hlane_Royal_National_Park"),
    ("Wikipedia · Reserva Natural de Malolotja (180 km², cataratas de 89 m, monte Ngwenya 1.829 m)", "https://en.wikipedia.org/wiki/Malolotja_Nature_Reserve"),
    ("Wikipedia · Mina de Ngwenya (41.000-43.000 años, la mina más antigua conocida, Lion Cavern)", "https://en.wikipedia.org/wiki/Ngwenya_Mine"),
    ("Wikipedia · Sibebe (segundo monolito del mundo, mayor plutón de granito expuesto, 350 m)", "https://en.wikipedia.org/wiki/Sibebe"),
    ("Wikipedia · Reserva de Mkhaya (rinoceronte negro, ganado nguni, solo visita guiada)", "https://en.wikipedia.org/wiki/Mkhaya_Game_Reserve"),
    ("Wikipedia · Santuario de Mlilwane (4.560 ha, a pie, en bici y a caballo)", "https://en.wikipedia.org/wiki/Mlilwane_Wildlife_Sanctuary"),
    ("Wikipedia · Umhlanga, la danza de las cañas (finales de agosto o principios de septiembre, Ludzidzini)", "https://en.wikipedia.org/wiki/Umhlanga_(ceremony)"),
    ("Wikipedia · Incwala (solsticio de verano austral, ceremonia de un mes)", "https://en.wikipedia.org/wiki/Incwala"),
    ("iOverlander · puntos de combustible, agua y acampada verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África austral", "https://tracks4africa.co.za/"),
]

# Entrada desde Sudáfrica por Ngwenya/Oshoek y bajada del highveld hasta Manzini
CORRIDOR = [(-26.2000, 31.0167), (-26.2017, 31.0339), (-26.1333, 31.1167), (-26.0333, 31.2167),
            (-26.0000, 31.2000), (-25.9500, 31.2000), (-26.3167, 31.1333), (-26.2833, 31.1667),
            (-26.4333, 31.1667), (-26.4500, 31.1833), (-26.4691, 31.1619), (-26.4833, 31.3667)]

# El lowveld del este y la salida a Mozambique
CORRIDOR_ALT = [(-26.4833, 31.3667), (-26.6250, 31.7375), (-26.2500, 31.8833), (-26.1333, 31.9500),
                (-25.9833, 31.9833)]

HISTORIA_RESUMEN = ("Esuatini es uno de los últimos reinos con poder real efectivo del mundo y la única monarquía absoluta que queda en África: un estado suazi consolidado en el siglo XIX bajo los reyes Sobhuza I y Mswati II —de quien viene el nombre del pueblo—, "
                    "protegido por los británicos frente a bóeres y zulúes, independiente desde 1968 y gobernado hoy por Mswati III, que en 2018 cambió el nombre oficial del país de Suazilandia a Esuatini. "
                    "Es un país pequeño, tradicionalista y muy vivo culturalmente, con dos grandes ceremonias reales anuales —la Umhlanga y la Incwala— y un debate político interno sobre democratización que se agudizó con las protestas de 2021.")

HISTORIA_SECCIONES = [
    ("Los primeros habitantes y la mina más antigua del mundo",
     "En Bomvu Ridge, junto a la actual frontera de Ngwenya, se encuentra la Lion Cavern: el yacimiento minero más antiguo conocido de la humanidad, datado por radiocarbono entre hace 41.000 y 43.000 años. Lo que se extraía no era metal sino OCRE ROJO y especularita, "
     "usados como pigmento cosmético y ritual. Es un dato extraordinario: la minería empezó en el mundo por razones simbólicas. Milenios después, los san dejaron arte rupestre por todo el territorio, con el abrigo de Nsangwini y sus enigmáticas figuras aladas como mejor ejemplo accesible."),
    ("La formación del reino suazi",
     "Los ancestros de los suazis llegaron desde el norte en las migraciones bantúes y se asentaron en la zona en el siglo XVIII bajo el clan Dlamini. El rey Sobhuza I consolidó el reino en el primer tercio del siglo XIX frente a la presión zulú del Mfecane, "
     "y su sucesor Mswati II lo expandió y le dio nombre: de Mswati viene «suazi». El sistema de gobierno dual entre el rey (Ngwenyama, «el león») y la reina madre (Ndlovukazi, «la elefanta») sigue vigente hoy."),
    ("Protectorado, oro y protección británica",
     "La segunda mitad del siglo XIX trajo una avalancha de concesiones mineras y de tierras a europeos que despojó al reino de buena parte de su territorio. Tras la Segunda Guerra Bóer, Suazilandia pasó a ser protectorado británico en 1903. "
     "El rey Sobhuza II, que reinó de 1921 a 1982 —uno de los reinados documentados más largos de la historia—, dedicó décadas a recomprar tierras para la nación y a negociar la independencia, que llegó el 6 de septiembre de 1968."),
    ("La monarquía absoluta y el debate actual",
     "En 1973 Sobhuza II derogó la Constitución, disolvió los partidos políticos y asumió el poder absoluto; el sistema se mantiene en lo esencial bajo Mswati III, coronado en 1986. Los partidos siguen sin poder concurrir a elecciones y el Parlamento de Lobamba tiene competencias limitadas. "
     "En 2021 hubo protestas prodemocráticas de gran escala reprimidas con dureza y con decenas de muertos, y el debate sigue abierto. En 2018, en el 50º aniversario de la independencia, el rey cambió el nombre oficial del país de Swazilandia a ESUATINI, «tierra de los suazis». "
     "Para el viajero, el país es tranquilo y hospitalario, pero conviene entrar sabiendo dónde está la línea: la crítica pública a la monarquía no es un tema de conversación."),
    ("Cultura viva: la Umhlanga y la Incwala",
     "Esuatini conserva dos ceremonias reales que no son reconstrucciones folclóricas sino ritos vivos de participación masiva. La UMHLANGA o danza de las cañas se celebra a finales de agosto o principios de septiembre en el recinto real de Ludzidzini: "
     "decenas de miles de jóvenes solteras cortan cañas, las llevan a la reina madre y desfilan ante la familia real. La INCWALA, la «ceremonia de la primera fruta», gira en torno al solsticio de verano austral (diciembre-enero), dura cerca de un mes "
     "y es el rito de renovación del rey y del año agrícola, con la recogida de agua sagrada por los bemanti, la búsqueda del árbol lusekwane por los jóvenes y la captura a mano del toro. Es la ceremonia más sagrada del país y la que más restricciones tiene para los de fuera."),
]

HISTORIA_FUENTES = [
    ("BBC News · Eswatini country profile", "https://www.bbc.com/news/world-africa-14650437"),
    ("Encyclopaedia Britannica · Eswatini, History", "https://www.britannica.com/place/Eswatini/History"),
    ("Wikipedia · Mina de Ngwenya, la más antigua conocida del mundo", "https://en.wikipedia.org/wiki/Ngwenya_Mine"),
    ("Wikipedia · Umhlanga, la danza de las cañas", "https://en.wikipedia.org/wiki/Umhlanga_(ceremony)"),
    ("Wikipedia · Incwala, la ceremonia de la primera fruta", "https://en.wikipedia.org/wiki/Incwala"),
]

SPEC = dict(
    slug="esuatini", name="Esuatini", revision="12 sep 2026",
    sub="ALTERNATIVA — no está en la ruta fija · ENCLAVE entre Sudáfrica y Mozambique: desvío corto entre ambos",
    chips=[
        ("ESTATUS", "ALTERNATIVA — pero es el desvío MÁS BARATO en tiempo de los cuatro"),
        ("COSTE DEL DESVÍO", "+400 km y +5-7 días · versión mínima: +250 km y 3 días"),
        ("VISADO", "NO HACE FALTA: españoles y ciudadanos de la UE, exentos (30 días) — confirmar"),
        ("ENTRADA", "Ngwenya/Oshoek (Sudáfrica) · Matsamo desde el Kruger"),
        ("SALIDA", "Lomahasha o Mhlumeni (MOZAMBIQUE) — sin volver a Sudáfrica"),
        ("PERRO", "CRUCE TERRESTRE CON PERRO DOCUMENTADO — el mejor dato del bloque sur"),
        ("A PIE", "Sibebe (2º monolito del mundo) · Malolotja · Mlilwane a pie y en bici"),
        ("HISTORIA", "Ngwenya: la mina más antigua del mundo, 43.000 años"),
        ("CEREMONIAS", "Umhlanga (ago-sep) e Incwala (dic-ene) — comprobar fechas"),
        ("MONARQUÍA", "Última monarquía absoluta de África: cero bromas con el rey"),
    ],
    center=[-26.5, 31.5], zoom=8,
    notice="Documento de planificación de una ALTERNATIVA que aún no está decidida. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Entrada desde Sudáfrica · el highveld",
    corridor_alt_label="El lowveld del este y la salida a Mozambique",
    hero_img=W + "Malolotja%20Scenery%20(31722500693).jpg?width=900",
    hero_credit="Reserva Natural de Malolotja · Wikimedia Commons",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("ESUATINI NO ESTÁ EN LA RUTA FIJA. El dueño lo situó entre las alternativas: «Ruanda / Uganda, Esuatini / Lesoto y Gabón como alternativas si hay tiempo y si tienen eVisa». Respuesta a las dos condiciones: "
              "(1) VISADO: no hace falta. Los ciudadanos españoles y de la UE están EXENTOS de visado para entrar en Esuatini (estancias cortas, habitualmente 30 días — confirmar la duración exacta). "
              "Existe un portal de eVisa para las nacionalidades que sí lo necesitan, pero para nosotros no aplica: se sella el pasaporte en el puesto terrestre y se entra. La condición del dueño se cumple por la vía de no necesitar trámite. "
              "(2) TIEMPO: es el desvío MÁS BARATO de los cuatro. El país mide unos 200 km de norte a sur y 130 de este a oeste. Lo decisivo es que ES UN ENCLAVE ENTRE SUDÁFRICA Y MOZAMBIQUE: "
              "se entra desde Sudáfrica por Ngwenya/Oshoek y SE SALE DIRECTAMENTE A MOZAMBIQUE por Lomahasha o Mhlumeni, de modo que no hay que deshacer camino. Encaja como un tramo del corredor Sudáfrica→Mozambique, no como un rodeo. "
              "El recorrido completo son unos 400 km y 5-7 días; la versión mínima —entrar por Oshoek, ver Ezulwini y Mlilwane, cruzar el lowveld por Hlane y salir a Mozambique— son unos 250 km y 3 días. "
              "(3) POR QUÉ ENTRA: por el PERRO y por la CULTURA. En Mlilwane, que no tiene grandes depredadores, se recorre la reserva a pie, en bicicleta y a caballo entre cebras y ñus, cosa imposible en Sudáfrica o Botsuana; "
              "Sibebe se sube andando por roca desnuda; Malolotja tiene el mejor senderismo libre de la zona; y la mina de Ngwenya es el yacimiento minero más antiguo del mundo. "
              "Y sobre todo: el dosier canino del proyecto recoge un TESTIMONIO DIRECTO DE CRUCE TERRESTRE CON PERRO A ESUATINI que funcionó sin problemas — es el único país de todo el bloque sur con esa confirmación de primera mano. "
              "(4) LA PEGA, la misma que en Lesoto: el permiso de importación sudafricano es de UNA SOLA EXPEDICIÓN. Aquí importa menos, porque saliendo a Mozambique NO se reentra en Sudáfrica — pero hay que tenerlo claro al planificar el orden de los países."),
    facts=[
        ("Estatus", "ALTERNATIVA, no ruta fija — pero el desvío más barato en tiempo de los cuatro, porque es un enclave que se atraviesa de Sudáfrica a Mozambique sin deshacer camino."),
        ("Coste en ruta", "Recorrido completo: ~400 km y 5-7 días. Versión mínima (Ezulwini + Hlane + salida a Mozambique): ~250 km y 3 días."),
        ("Visado", "Ciudadanos de la UE, incluidos los españoles, EXENTOS para estancias cortas (habitualmente 30 días). Sin trámite previo. Hay portal de eVisa para quien sí lo necesita. CONFIRMAR duración exacta de la exención antes de entrar."),
        ("Entrada", "Ngwenya/Oshoek desde Mpumalanga (el principal), o Matsamo/Jeppe's Reef si se viene del Kruger. Lavumisa/Golela desde KwaZulu-Natal si se viene del sur."),
        ("Salida", "Lomahasha/Namaacha o Mhlumeni/Goba hacia MOZAMBIQUE: es lo que hace que el desvío no cueste kilómetros de vuelta."),
        ("Perro · el mejor dato del sur", "El dosier del proyecto recoge un testimonio directo de CRUCE TERRESTRE CON PERRO a Esuatini: «entrada sencilla, el permiso funcionó como se esperaba». Es el único país del bloque sur con confirmación de primera mano. Aviso: el permiso nombra el destino y en la frontera quisieron quedárselo."),
        ("Fauna a pie", "Mlilwane NO tiene grandes depredadores: se recorre A PIE, EN BICI Y A CABALLO entre cebras, ñus e impalas. Es la experiencia de fauna más distinta de todo el bloque sur."),
        ("Rinocerontes", "Hlane tiene rinoceronte blanco, leones y elefantes y se recorre con vehículo propio; Mkhaya tiene rinoceronte NEGRO pero NO admite vehículo propio: todo guiado y con reserva previa."),
        ("Historia", "La mina de Ngwenya (Lion Cavern) es el yacimiento minero más antiguo conocido del mundo: 41.000-43.000 años, y no se extraía metal sino ocre rojo para ritual y cosmética."),
        ("Ceremonias reales", "UMHLANGA (danza de las cañas): finales de agosto o principios de septiembre, en Ludzidzini. INCWALA: en torno al solsticio de verano austral (dic-ene), dura cerca de un mes. Comprobar fechas exactas del año en curso: cambian y las fija la casa real."),
        ("Moneda y aduana", "El lilangeni está a la par con el rand sudafricano y el rand circula con normalidad. Esuatini está en la SACU: sin aranceles internos, pero con control fronterizo real de personas, vehículos y animales."),
        ("Vehículo", "Se conduce por la IZQUIERDA, igual que en Sudáfrica y Mozambique. Carreteras principales en buen estado; la MR3 atraviesa Hlane."),
        ("Drones", "Régimen de la ESWACAA, manejable, pero con dos líneas rojas: recintos reales y ceremonias. Por confirmar el detalle."),
    ],
    alerts=[
        "ESTATUS ALTERNATIVA: no está en la ruta fija. Pero es la que menos cuesta decidir, porque se atraviesa de camino de Sudáfrica a Mozambique.",
        "MONARQUÍA ABSOLUTA: Esuatini es la última monarquía absoluta de África. No se critica públicamente al rey, no se fotografían recintos reales ni comitivas, no se vuela un dron sobre nada relacionado con la corona, y no se entra en debates políticos con desconocidos. En 2021 hubo protestas prodemocráticas reprimidas con dureza; la situación está tranquila, pero el tema no es conversación de bar.",
        "CEREMONIAS REALES: si el paso coincide con la UMHLANGA (finales de agosto o principios de septiembre) es una oportunidad excepcional, PERO hay que informarse antes de las normas: acceso, vestimenta y sobre todo FOTOGRAFÍA, que está restringida. Con la INCWALA (dic-ene) las restricciones son mucho mayores porque es la ceremonia más sagrada del país. Confirmar fechas y condiciones con la oficina de turismo, no improvisar.",
        "MKHAYA NO ADMITE VEHÍCULO PROPIO: hay que dejar los coches en el punto de encuentro de Phuzumoya y entrar en vehículo de la reserva, con reserva previa obligatoria y plazas muy limitadas. Si se quiere ver rinoceronte negro, hay que reservarlo con antelación desde Sudáfrica.",
        "HLANE ESTÁ PARTIDO POR LA CARRETERA MR3: la vía pública atraviesa el parque desde los años sesenta y provoca atropellos de fauna. Conducir ese tramo despacio y nunca de noche.",
        "PERRO: ningún parque de Big Game Parks (Hlane, Mkhaya, Mlilwane) admite mascotas. Merece la pena preguntar por escrito en Mlilwane —donde no hay depredadores— y a la Eswatini National Trust Commission por Malolotja y Mantenga: es la vía más prometedora del desvío.",
        "PERMISO SACU DE UNA SOLA EXPEDICIÓN: el permiso de importación sudafricano vale para una sola entrada. Saliendo a Mozambique no hay que reentrar en Sudáfrica, así que aquí el problema es menor que en Lesoto — pero condiciona el ORDEN de los países y hay que planificarlo.",
        "Malaria: hay riesgo estacional en el LOWVELD del este y el noreste (Hlane, Mkhaya, Simunye, Big Bend, Lubombo), sobre todo de noviembre a mayo. El highveld (Mbabane, Ezulwini, Malolotja) se considera libre de riesgo. Profilaxis a valorar con Sanidad Exterior según por dónde se pase y en qué mes.",
        "Esuatini tiene una de las tasas de VIH más altas del mundo y una red sanitaria limitada: para cualquier urgencia seria, la solución es Mbombela (Nelspruit) o Johannesburgo. Comprobar que el seguro cubre la evacuación transfronteriza.",
        "Horarios de frontera: casi ninguno de los pasos es de 24 horas. Confirmar el horario del puesto concreto 72 h antes, sobre todo en Lomahasha y Mhlumeni hacia Mozambique.",
    ],
    ruta_intro=("Dos corredores que atraviesan el país de oeste a este sin solaparse. El primero entra desde Sudáfrica por Ngwenya/Oshoek y recorre el HIGHVELD montañoso del noroeste: la mina más antigua del mundo, la vidriería de Ngwenya, "
                "Malolotja y su tirolina, la presa de Maguga, el arte rupestre de Nsangwini, las cascadas de Phophonyane, Mbabane, Sibebe y todo el valle de Ezulwini con Mantenga, Lobamba y Mlilwane, hasta Manzini. "
                "El segundo baja al LOWVELD del este: los rinocerontes negros de Mkhaya, los leones y buitres de Hlane, el escarpe de Lubombo con el campamento comunitario de Shewula, y salida directa a Mozambique. "
                "Etapas sobre 250 km/día, aunque en un país de 200 km lo que manda no son los kilómetros sino las paradas."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada y prehistoria", "Oshoek/Ngwenya → mina de Ngwenya → fábrica de vidrio", "~10 km · medio día"),
        ("2 · La montaña", "Ngwenya → Reserva de Malolotja (senderismo y canopy tour)", "~20 km · 2-3 días"),
        ("3 · El norte del Komati", "Malolotja → presa de Maguga → Nsangwini → Phophonyane (Piggs Peak)", "~70 km · 2 días"),
        ("4 · La capital y el monolito", "Piggs Peak → Mbabane → Sibebe (subida a pie)", "~65 km · 1-2 días"),
        ("5 · El valle del cielo", "Mbabane → Ezulwini: mercado, termas, Mantenga y el poblado cultural", "~20 km · 2 días de parada"),
        ("6 · Fauna a pie", "Ezulwini → Mlilwane: a pie, en bici y a caballo entre cebras y ñus", "~5 km · 2 días de parada"),
        ("7 · La capital real", "Ezulwini → Lobamba: Parlamento, Museo Nacional, memorial de Sobhuza II, Ludzidzini", "~10 km · medio día"),
        ("8 · El mercado", "Lobamba → Manzini (mercado de artesanía, jueves y viernes por la mañana)", "~35 km · 1 día"),
        ("9 · El rinoceronte negro", "Manzini → Mkhaya (dejar vehículo en Phuzumoya, entrada guiada)", "~65 km · 1-2 días"),
        ("10 · Leones y buitres", "Mkhaya → Hlane Royal NP (Ndlovu o Bhubesi)", "~90 km · 2 días"),
        ("11 · El escarpe", "Hlane → Shewula Mountain Camp (Lubombo) y gargantas del Mbuluzi", "~50 km · 1 día"),
        ("12 · Salida a Mozambique", "Shewula → Lomahasha/Namaacha (o Mhlumeni/Goba) → Maputo", "~40 km · 1 día"),
        ("Alt. · Salida al sur", "Manzini → Big Bend → Lavumisa/Golela → KwaZulu-Natal", "~130 km · 1 día"),
    ],
    offroad=[
        "Esuatini NO es un destino 4x4 como Lesoto o Namibia: las carreteras principales están asfaltadas y en buen estado, y el país se cruza en un día. Lo que hay son tramos de pista cortos pero muy disfrutables, y una red secundaria de tierra excelente para conducción lenta.",
        "PISTAS DE MALOLOTJA: solo hay 25 km de carretera dentro de los 180 km² de la reserva, y son de tierra, con vados y rampas. Se puede recorrer en 4x4, en bici de montaña o a pie: es la mejor conducción de tierra del país y la que da acceso a las cabeceras de los senderos.",
        "CARRETERA MR1 PIGGS PEAK – MAGUGA – MBABANE: asfalto de montaña con curvas continuas y miradores sobre el embalse del Komati. No es offroad, pero es la conducción más bonita de Esuatini.",
        "ACCESO A NSANGWINI: pista de tierra desde la MR1 y después bajada a pie por sendero empinado hasta el abrigo. Con lluvia, resbaladiza.",
        "PISTAS INTERIORES DE HLANE: el parque se recorre con vehículo propio por pistas llanas de arena y tierra; se recomienda ALTURA LIBRE para algunos circuitos, y con lluvia hay tramos que se embarran. El circuito de Bhubesi, al norte, es el más salvaje.",
        "SUBIDA AL ESCARPE DE LUBOMBO (Shewula): pista de tierra con pendiente y algún tramo suelto hasta el borde de la meseta. Vistas enormes al llegar.",
        "AVISO: en Mkhaya NO se conduce. Hay que dejar los vehículos en Phuzumoya y entrar en el transporte de la reserva.",
    ],
    senderismo=[
        "SIBEBE: la caminata estrella del país y una de las más raras de África. Se sube A PIE por la roca desnuda de una cúpula de granito de 350 m —descrita como el segundo monolito más grande del mundo tras Uluru y el mayor plutón de granito expuesto del planeta—, con tramos de trepada a cuatro patas por pura fricción. Dos o tres horas, guía local recomendable, y una cumbre plana con 360 grados de highveld. Cada año se celebra el «Sibebe Survivor», una marcha benéfica multitudinaria hasta arriba.",
        "MALOLOTJA: EL MEJOR SENDERISMO DEL DESVÍO. Red de senderos de un día y travesías de varios días con vivac por 180 km² de montaña, con solo 25 km de carretera en toda la reserva. Al no haber grandes depredadores SE CAMINA SIN RANGER, algo impensable en Sudáfrica o Botsuana. Imprescindible: el sendero a las CATARATAS DE MALOLOTJA (89 m, el salto más alto del país) y la subida al monte Ngwenya (1.829 m).",
        "MLILWANE A PIE Y EN BICI: la reserva se recorre por senderos autoguiados y en bicicleta de montaña de alquiler entre cebras, ñus, impalas y facóqueros, porque no hay depredadores grandes. También hay rutas a caballo guiadas. Subida al pico Nyonyane y a la Roca de la Ejecución, con la leyenda de los condenados despeñados.",
        "MALOLOTJA CANOPY TOUR: tirolinas de plataforma en plataforma sobre el cañón del Majolomba, con un puente colgante de unos 50 m de altura. Se anuncia como la tirolina más larga de África austral (POR CONFIRMAR con el operador). Dos o tres horas.",
        "Cascadas de Mantenga: sendero corto hasta el salto del río Lusushwana, combinable con el poblado cultural y el espectáculo de danza sibhaca.",
        "Cascadas y pozas de Phophonyane: senderos cortos entre bosque de ribera, con pozas naturales para bañarse y más de 250 especies de aves.",
        "Nsangwini: bajada corta y empinada por un balcón de roca hasta el panel de arte rupestre san con las figuras aladas. Guía comunitario obligatorio, y lo mejor de la visita es precisamente el guía.",
        "Mlawula y las gargantas del Mbuluzi (Lubombo): senderos poco transitados por el escarpe oriental, con vistas a Mozambique. Paseos comunitarios desde el Shewula Mountain Camp con guías del pueblo.",
        "Hlane: hay caminatas guiadas con ranger en zonas sin depredadores dentro del parque real — preguntar en Ndlovu Camp. En un parque con leones, caminar es una experiencia distinta a conducir.",
    ],
    acampada=[
        "Mlilwane (Ezulwini): el camping más conocido del país, con facóqueros y antílopes pastando entre las tiendas y cabañas de paja tradicionales. Base ideal del desvío: desde aquí no hace falta mover el vehículo en tres días.",
        "Malolotja: zonas de acampada repartidas por la reserva, incluidas plataformas de vivac en los senderos largos. Frío de noche por la altitud.",
        "Hlane (Ndlovu Camp y Bhubesi Camp): camping dentro del parque real, con charca iluminada junto a Ndlovu donde beben rinocerontes y elefantes al anochecer. Sin electricidad en Bhubesi.",
        "Maguga Dam: lodge y camping en la orilla del embalse, con vistas al valle del Komati.",
        "Phophonyane (Piggs Peak): casas de campaña y camping en bosque de ribera, junto a las pozas.",
        "Shewula Mountain Camp (Lubombo): campamento comunitario sencillo en el borde de la meseta, gestionado íntegramente por la comunidad. Lo más honesto que se puede dormir en el país.",
        "Ezulwini: varios lodges y campings del valle admiten perro — confirmar por escrito antes de contar con ello.",
    ],
    visado=[
        "CIUDADANOS DE LA UE, INCLUIDOS LOS ESPAÑOLES: EXENTOS de visado para estancias cortas, habitualmente 30 días. No hace falta trámite previo: se sella el pasaporte en el puesto fronterizo terrestre.",
        "CRITERIO DEL DUEÑO — VÁLIDO POR TIERRA: sí. Esuatini dispone además de un portal de eVisa para las nacionalidades que sí necesitan visado, y es utilizable para entrada terrestre, pero para un pasaporte español no aplica porque la exención lo cubre. La condición se cumple por la vía de no necesitar trámite.",
        "CONFIRMAR la duración exacta de la exención y las condiciones vigentes antes de entrar, en el Departamento de Inmigración de Esuatini o en la Alta Comisión: es un dato que conviene verificar y no dar por bueno de memoria.",
        "Pasaporte con validez mínima de 6 meses y páginas libres para los sellos.",
        "Certificado de fiebre amarilla solo si se procede de país endémico. Viniendo de Sudáfrica no aplica; si se entrara desde Mozambique tampoco, pero conviene llevarlo por si acaso.",
        "IMPORTANTE: aunque Esuatini esté en la SACU, HAY CONTROL FRONTERIZO REAL. Salir de Sudáfrica a Esuatini es una salida a efectos del visado sudafricano: si después se quiere volver a entrar en Sudáfrica, comprobar que la estancia autorizada lo permite.",
    ],
    fronteras_rows=[
        ("Entrada (principal)", "Ngwenya / Oshoek (Sudáfrica, Mpumalanga)", "El paso más transitado, en la carretera de Johannesburgo a Mbabane, y el más cercano a la mina de Ngwenya y a Malolotja. Horario amplio (aprox. 07:00–22:00) pero NO 24 h: confirmar."),
        ("Entrada (desde el Kruger)", "Matsamo / Jeppe's Reef (Sudáfrica, Mpumalanga)", "Paso del norte, el enlace natural si el desvío se encaja saliendo del Kruger por Malelane. Horario limitado."),
        ("Entrada/salida (sur)", "Lavumisa / Golela (Sudáfrica, KwaZulu-Natal)", "En la N2 hacia Durban: la opción si el desvío se encadena con Lesoto y el sur de Sudáfrica. Horario amplio."),
        ("SALIDA (la que hace rentable el desvío)", "Lomahasha / Namaacha (MOZAMBIQUE)", "Noreste, hacia Namaacha y Maputo. Permite salir a Mozambique SIN volver a entrar en Sudáfrica, que es lo que convierte a Esuatini en un tramo del corredor y no en un rodeo. Confirmar horario."),
        ("Salida (alternativa a Mozambique)", "Mhlumeni / Goba", "Más al sur, con carretera nueva hacia Maputo y habitualmente más rápido que Lomahasha. Confirmar horario."),
        ("Otros pasos", "Mananga, Sandlane/Nerston, Sicunusa, Bulembu/Josefsdal", "Hay una decena de pasos menores con Sudáfrica, varios con horario muy corto y alguno con pista de montaña (Bulembu). Confirmar horario y estado antes de contar con ellos."),
    ],
    vehiculos=[
        "Se conduce por la IZQUIERDA, igual que en Sudáfrica y Mozambique: no hay cambio de lado en ninguna de las dos fronteras del desvío.",
        "Tasa de circulación para vehículo extranjero al entrar (road toll): importe pequeño, en emalangeni o rand. Por confirmar el importe vigente.",
        "SEGURO: comprobar si la póliza sudafricana cubre Esuatini (muchas cubren la SACU); si no, hay seguro de frontera obligatorio de terceros.",
        "CPD: al estar en la SACU, el trámite del vehículo suele ser un permiso temporal simple. Confirmar si se sella el cuaderno para no romper la cadena de pares de sellos.",
        "Carné de conducir internacional recomendable junto con el nacional.",
        "Carreteras principales asfaltadas y en buen estado (MR3, MR1, MR8). Cuidado con el ganado suelto y con los peatones en el arcén, y con el tramo de la MR3 que atraviesa Hlane.",
        "No conducir de noche, criterio general del proyecto: aquí el motivo concreto son el ganado y la fauna que cruza la MR3.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Registro y autorización previa ante la Eswatini Civil Aviation Authority (ESWACAA): régimen POR CONFIRMAR en su detalle, bastante más manejable que el de Uganda o Ruanda.",
        "LÍNEA ROJA 1: no volar sobre recintos reales (Lobamba, Ludzidzini, palacios) ni sobre comitivas oficiales. Es una monarquía absoluta y esto no se negocia.",
        "LÍNEA ROJA 2: no volar sobre la Umhlanga ni sobre la Incwala. La fotografía en las ceremonias ya está restringida; un dron sería un problema serio.",
        "No volar dentro de las reservas de Big Game Parks (Hlane, Mkhaya, Mlilwane) ni de la Eswatini National Trust Commission (Malolotja, Mantenga) sin permiso escrito de la gestión.",
        "Fuera de esos supuestos, y con el trámite de la ESWACAA resuelto, Malolotja y el escarpe de Lubombo son sitios magníficos para el dron.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Disponibilidad comercial de Starlink en Esuatini: POR CONFIRMAR antes del viaje. No se ha podido verificar en esta revisión.",
        "Red móvil de Eswatini Mobile y MTN Eswatini: buena en el corredor Mbabane–Ezulwini–Manzini y razonable en el lowveld; más floja en Malolotja y en el escarpe de Lubombo.",
        "SIM local barata, se compra con pasaporte a la entrada y resuelve el desvío entero.",
        "El país es pequeño: desde casi cualquier punto se está a pocas horas de Sudáfrica o de Maputo, así que la dependencia de la conexión es baja.",
    ],
    perro_intro=[
        "EL MEJOR DATO DE TODO EL BLOQUE SUR: el dosier canino del proyecto recoge un TESTIMONIO DIRECTO de cruce terrestre con perro a Esuatini — «entrada sencilla, el permiso funcionó como se esperaba» — y describe la salida y la reentrada a Sudáfrica como «un proceso fácil». Es el único país del sur con confirmación de primera mano de un cruce terrestre con animal.",
        "AVISO DEL MISMO TESTIMONIO: el permiso NOMBRA EL PAÍS DE DESTINO y los funcionarios de frontera QUISIERON QUEDÁRSELO en lugar de devolverlo para seguir usándolo. Pedir copia sellada, o llevar un permiso por país, o fotografiarlo todo antes de entregarlo.",
        "Régimen SACU: permiso de importación de los servicios veterinarios de Esuatini (Ministry of Agriculture, Department of Veterinary and Livestock Services), más el permiso interterritorial de movimiento sudafricano (gratuito, tres sellos, ventana de 7 días para cruzar, 30 días de repatriación) y vacunaciones anuales al día sin saltarse ningún año.",
        "Certificado veterinario internacional, rabia en vigor y desparasitación. Documentación en inglés.",
        "Veterinarios en Mbabane y Manzini; para cualquier cosa seria, Mbombela (Nelspruit) está a unas dos horas de la frontera de Ngwenya.",
        "Ningún parque de Big Game Parks (Hlane, Mkhaya, Mlilwane) admite mascotas. La vía prometedora son las reservas de la Eswatini National Trust Commission (Malolotja, Mantenga) y el terreno comunitario o privado (Sibebe, Nsangwini, Maguga), donde la decisión la toma la comunidad o el propietario.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "MALARIA: riesgo estacional en el LOWVELD del este y noreste (Hlane, Mkhaya, Simunye, Big Bend, Lubombo), sobre todo de noviembre a mayo. El HIGHVELD (Mbabane, Ezulwini, Malolotja, Piggs Peak) se considera libre de riesgo. Profilaxis a valorar con Sanidad Exterior según el mes y el itinerario exacto: si solo se hace el highveld, probablemente no haga falta.",
        "Fiebre amarilla: certificado exigido solo si se procede de país endémico. No aplica viniendo de Sudáfrica.",
        "Bilharzia en ríos y embalses del lowveld: no bañarse en aguas estancadas ni dejar que el perro beba en ellas. Las pozas de Phophonyane y los arroyos de montaña de Malolotja son otra cosa, pero conviene preguntar en el momento.",
        "Esuatini tiene una de las tasas de VIH más altas del mundo y una red sanitaria limitada. El Mbabane Government Hospital y las clínicas privadas de Ezulwini cubren lo básico; para cualquier cosa seria, la vía es Mbombela (Nelspruit) o Johannesburgo, a pocas horas.",
        "Comprobar que el seguro cubre la evacuación transfronteriza a Sudáfrica: es la clave sanitaria del desvío.",
        "Calor y humedad en el lowveld en verano austral; el highveld es fresco y agradable todo el año.",
    ],
    seguridad_intro=("Esuatini es un país tranquilo y hospitalario, con delincuencia moderada y sin conflictos activos. Los dos condicionantes reales del desvío no son de seguridad física sino de PRUDENCIA POLÍTICA —es una monarquía absoluta— "
                     "y de RESPETO CEREMONIAL, si el paso coincide con la Umhlanga o la Incwala."),
    seguridad=[
        "MONARQUÍA ABSOLUTA: no se critica públicamente al rey, no se fotografían recintos reales, comitivas ni militares, y no se entra en debates políticos con desconocidos. En 2021 hubo protestas prodemocráticas reprimidas con dureza y con decenas de muertos; la situación está tranquila pero el asunto sigue siendo sensible. Consultar la recomendación oficial antes de entrar y evitar cualquier concentración.",
        "CEREMONIAS: durante la Umhlanga y la Incwala hay normas estrictas de vestimenta, acceso y fotografía. Informarse antes con la oficina de turismo o con el alojamiento, y en caso de duda no fotografiar. Nada de drones.",
        "Delincuencia: hurtos y robos ocasionales en Manzini y Mbabane. Aparcamiento vigilado, nada de valor a la vista y prudencia estándar. En las reservas y en el campo, el país es muy seguro.",
        "Conducción: el riesgo real. Ganado suelto, peatones en el arcén y la MR3 atravesando Hlane con fauna cruzando. No conducir de noche.",
        "Hlane y Mkhaya tienen leones, elefantes, rinocerontes y búfalos: seguir las normas del parque y no bajarse del vehículo fuera de las zonas autorizadas. En Mlilwane, donde se camina, no hay depredadores grandes, pero SÍ hay facóqueros y ñus que embisten si se les acorrala.",
        "Horarios de frontera: casi ningún paso es de 24 h. Quedarse fuera de horario en un puesto pequeño significa dormir donde se pueda: confirmar el horario 72 h antes.",
        "Sibebe: es una subida por roca desnuda, sin barandillas. Con la roca mojada es peligrosa de verdad: no subir con lluvia ni con la piedra húmeda.",
    ],
    agua=[
        "Mbabane, Ezulwini, Manzini y las localidades del lowveld: agua embotellada sin problema en supermercados (cadenas sudafricanas).",
        "Recarga del depósito de uso general: campings de Mlilwane, Malolotja, Hlane, Maguga y Phophonyane permiten llenar con manguera; confirmar en recepción.",
        "Arroyos de montaña de Malolotja: agua limpia, pero filtrar y potabilizar siempre.",
        "No usar agua de embalses ni ríos del lowveld sin tratar, por bilharzia.",
    ],
    combustible=[
        "Red buena y fiable para el tamaño del país: Mbabane, Ezulwini, Manzini, Piggs Peak, Simunye, Big Bend y Nhlangano tienen estaciones formales (Galp, Total, Puma, Engen).",
        "Los precios suelen ser algo MÁS BARATOS que en Sudáfrica: merece la pena repostar a fondo dentro de Esuatini antes de salir.",
        "No hay ningún gap de autonomía relevante: el país mide unos 200 km de norte a sur.",
        "Antes de entrar en Hlane o en Malolotja, repostar: dentro de las reservas no hay surtidor.",
        "Repostar a fondo antes de cruzar a MOZAMBIQUE por Lomahasha o Mhlumeni: el combustible es más caro y menos fiable al otro lado, sobre todo fuera de Maputo.",
    ],
    experiencias_intro=("Relatos y datos recogidos de la comunidad overland y de fuentes documentales. No son información oficial: contrastar siempre la fecha antes de confiar en un dato de frontera, pista o parque. "
                        "En esta revisión no se ha podido acceder a iOverlander ni a Tracks4Africa desde la sesión de trabajo, así que lo que sigue procede del dosier canino del propio proyecto y de fuentes documentales, y está marcado como tal:"),
    experiencias=[
        "PERRO — el testimonio clave de todo el bloque sur (dosier del proyecto, relato de The Pack Track): cruzaron por tierra a Esuatini con perros y describen la entrada como «sencilla», con el permiso funcionando «como se esperaba»; la salida y la reentrada a Sudáfrica, «un proceso fácil». Es la única confirmación directa de un cruce terrestre con animal en toda la región, y es la razón principal por la que este desvío merece considerarse en serio.",
        "PERRO — el aviso del mismo relato: el permiso de importación NOMBRA EL PAÍS DE DESTINO y en la frontera QUISIERON QUEDÁRSELO en vez de devolverlo para seguir usándolo. La recomendación práctica es llevar copias, pedir que lo sellen y devuelvan, o tramitar un permiso por país.",
        "PERRO — la frase que resume el régimen SACU en boca de quien lo hizo: «cruzar la frontera dentro de la SACU no había sido difícil». Después de meses de papeleo africano, este bloque es el fácil.",
        "Mlilwane es lo que más sorprende: después de semanas de parques donde no te puedes bajar del coche, aquí se sale a caminar, a pedalear y a montar a caballo entre cebras, ñus e impalas. Quien lo hace lo describe como recuperar la escala humana de la sabana. Los facóqueros que pastan entre las tiendas del camping son parte del paquete.",
        "Mkhaya tiene una reputación desproporcionada para su tamaño: es el sitio donde la gente ve rinoceronte negro de cerca, y se la considera de las mejores experiencias de fauna del sur de África. El precio y la obligación de reservar y dejar el vehículo fuera son la contrapartida.",
        "Sibebe es la caminata que nadie espera: una losa de granito desnudo de 350 m que se sube a pura fricción, sin material, con tramos a cuatro patas. Los que la hacen dicen que es una de las subidas más divertidas de África, y que con la roca mojada no se debe ni intentar.",
        "Malolotja es el secreto del país: 180 km² de montaña con apenas 25 km de carretera, senderos de varios días con vivac y la posibilidad de caminar sin ranger porque no hay depredadores grandes. Para quien viene del sur de África, caminar libre por un parque es una rareza.",
        "La Umhlanga impresiona a todo el que coincide con ella: decenas de miles de jóvenes desfilando ante la familia real en Ludzidzini. El consejo repetido es informarse antes de las normas de fotografía y vestimenta, y comportarse como invitado y no como turista.",
        "La mina de Ngwenya es el dato que más gusta contar después: la minería empezó en el mundo hace 43.000 años, aquí, y no para sacar metal sino ocre rojo para pintarse. El problema es que el centro de visitantes ardió en 2018: conviene confirmar qué se puede ver hoy antes de desviarse.",
        "La ventaja estratégica que casi nadie aprovecha: se puede entrar desde Sudáfrica y SALIR DIRECTAMENTE A MOZAMBIQUE por Lomahasha o Mhlumeni, sin deshacer camino. Eso convierte a Esuatini en un tramo del corredor y no en un desvío, y es lo que lo hace tan barato en tiempo.",
    ],
    pendientes=[
        ("DECISIÓN DE FONDO", "Decidir si entra y en qué versión: recorrido completo (~400 km, 5-7 días) o versión mínima (~250 km, 3 días). Es el desvío más barato en tiempo de los cuatro y se puede decidir ya estando en el corredor sudafricano"),
        ("PERRO · permiso SACU", "Confirmar por escrito con DALRRD (VetPermits@daff.gov.za) y con los servicios veterinarios de Esuatini el procedimiento exacto, y PEDIR QUE DEVUELVAN EL PERMISO en la frontera (hay testimonio de que intentan quedárselo). Llevar copias selladas"),
        ("PERRO · Mlilwane", "Escribir a Big Game Parks preguntando expresamente si Mlilwane, que NO tiene grandes depredadores, admite perro con correa. Es donde la excepción tendría más sentido de todo el sur de África"),
        ("PERRO · reservas de la ENTC", "Escribir a la Eswatini National Trust Commission por Malolotja y Mantenga: sin depredadores grandes en Malolotja, es la mejor opción del desvío para caminar con el perro"),
        ("Visado", "Confirmar la duración exacta de la exención para españoles (habitualmente 30 días) y comprobar que salir de Sudáfrica no compromete un eventual regreso a Sudáfrica"),
        ("CEREMONIAS · fechas", "Comprobar las fechas exactas de la UMHLANGA (finales de agosto o principios de septiembre) y de la INCWALA (en torno al solsticio de verano austral, dic-ene) del año en curso: las fija la casa real y cambian. Si el paso coincide, informarse de las normas de acceso, vestimenta y fotografía ANTES"),
        ("Mkhaya", "Reservar con antelación si se quiere ver rinoceronte negro: no se entra con vehículo propio, hay que dejar los coches en Phuzumoya y las plazas son limitadas"),
        ("Ngwenya · qué se visita hoy", "El centro de visitantes de la mina ardió en 2018: confirmar con la Eswatini National Trust Commission qué parte del yacimiento y de la Lion Cavern se puede visitar actualmente"),
        ("Canopy tour de Malolotja", "Confirmar con el operador si sigue activo y si la afirmación de «la tirolina más larga de África austral» es la vigente"),
        ("Horarios de frontera", "Confirmar 72 h antes el horario de Oshoek/Ngwenya y, sobre todo, de Lomahasha y Mhlumeni hacia Mozambique: ninguno es de 24 h"),
        ("Seguro del vehículo", "Verificar por escrito si la póliza sudafricana cubre Esuatini; si no, prever seguro de frontera"),
        ("Dron", "Confirmar con la Eswatini Civil Aviation Authority el régimen de registro y autorización. En cualquier caso, no volar sobre recintos reales ni ceremonias"),
        ("Starlink", "Confirmar disponibilidad comercial en Esuatini: no se ha podido verificar en esta revisión"),
        ("FOTOGRAFÍAS", "En esta revisión NO se pudo acceder a commons.wikimedia.org desde la sesión (bloqueo de red), así que solo dos PDIs llevan foto verificada. Pendiente: completar los nombres de archivo de Wikimedia Commons de los 14 PDIs restantes, verificándolos uno a uno. No inventarlos"),
        ("Coordenadas aproximadas", "Verificar sobre el terreno o con cartografía las coordenadas marcadas como aproximadas: Malolotja, canopy tour, Maguga, Nsangwini, Phophonyane, Sibebe, Mantenga, Hlane, Shewula y todos los pasos fronterizos"),
    ],
    sources=SOURCES,
    sources_note=("Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. "
                  "ESUATINI ES UNA ALTERNATIVA: no está en la ruta fija, pero es el desvío más barato en tiempo de los cuatro porque se atraviesa de Sudáfrica a Mozambique sin deshacer camino. "
                  "Fechas de las ceremonias reales, horarios de frontera y política de mascotas de las reservas hay que revalidarlos poco antes de entrar."),
    emergency="Sin embajada de España en Esuatini — competencia de la Embajada de España en Maputo (Mozambique); confirmar el teléfono de emergencia consular vigente antes de entrar. Emergencias locales: policía 999, ambulancia 977, bomberos 933. Para urgencias graves, la vía real es la evacuación a Mbombela (Nelspruit) o Johannesburgo.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

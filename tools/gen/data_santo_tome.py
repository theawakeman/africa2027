# -*- coding: utf-8 -*-
"""Santo Tomé y Príncipe — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Santo Tomé y Príncipe está FUERA DE LA RUTA PREVISTA por ser insular: no hay conexión terrestre con el continente ni ferry que admita vehículos. La app solo tiene un stub: créala entera con el formato del piloto de Túnez. Es uno de los países más estables y seguros de África — el MAEC no desaconseja viajar — y eso hay que decirlo con claridad para que no se confunda con los vecinos del golfo de Guinea. Claves que DECIDEN la ficha y hay que documentar con fuente fechada: el archipiélago es un estado de dos islas principales con alternancia democrática desde 1991, aunque con inestabilidad de gobiernos y un intento de asalto a un cuartel en noviembre de 2022; la economía vive del cacao, del turismo y de la ayuda; y la isla de Príncipe entera es Reserva de la Biosfera de la UNESCO desde 2012. El paisaje de las ROÇAS — las plantaciones coloniales portuguesas, muchas en ruina y algunas rehabilitadas como hotel — es el hilo que ordena la visita. Verifica el régimen de visados para españoles (exención de corta estancia) y la tasa de entrada, si existe.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/santo-tome.json y audit/pdi/santo-tome.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Ciudad de São Tomé · catedral, fuerte de São Sebastião y mercado", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=0.3460274, lon=6.7394473,  # Google Maps: Forte de São Sebastião
        desc="La capital cabe en un paseo de una mañana: la Sé Catedral de Nossa Senhora da Graça, levantada a finales del siglo XV y rehecha en 1576-1578, 1814 y 1956; el fuerte de São Sebastião, construido en 1566 contra los piratas y convertido en Museo Nacional a finales de los años setenta; y un mercado ruidoso donde se ve el cacao antes de que se vuelva chocolate. Es la ÚNICA base real de la isla: bancos, taller, combustible y hospital. Cuidado con los desplazamientos nocturnos y los carteristas en aglomeraciones.",
        dog_note="Puede pasear por el malecón y la Praça da Independência, pero el Museo Nacional del fuerte y la catedral no admiten animales; hay que turnarse.",
        visit={
            "why": "Es el punto de entrada, el único sitio con servicios del archipiélago y el mejor resumen de quinientos años de historia colonial en un kilómetro cuadrado.",
            "see": "Catedral de Nossa Senhora da Graça en la Praça do Povo junto al Palacio Presidencial, fuerte de São Sebastião sobre la bahía de Ana Chaves y el mercado municipal.",
            "access": "Todo asfaltado, aunque con baches grandes según el aviso canadiense; la EN1 y la EN2 arrancan aquí. Aparcamiento para dos 4x4 sin problema en la explanada del fuerte, junto al mar. El pin marca el fuerte de São Sebastião / Museo Nacional, que es el objeto al que se conduce; la catedral está 700 m al oeste (0.3384, 6.7327). Horarios y tarifa del museo: por confirmar, ninguna fuente oficial los publica.",
            "when": "Mañana temprano para el mercado y última hora de la tarde para el malecón; en seca (junio-septiembre) el calor es más llevadero.",
            "skip": "No se descarta: sin pasar por aquí no hay combustible, dinero ni repuestos en toda la isla.",
        },
        links=[
            {"label": "Museo Nacional / Forte de São Sebastião (Wikipedia)", "url": "https://en.wikipedia.org/wiki/S%C3%A3o_Sebasti%C3%A3o_Museum"},
            {"label": "Sé Catedral de Nossa Senhora da Graça (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Our_Lady_of_Grace_Cathedral,_S%C3%A3o_Tom%C3%A9"},
            {"label": "Ciudad de São Tomé (Wikipedia)", "url": "https://en.wikipedia.org/wiki/S%C3%A3o_Tom%C3%A9"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sao_tome_fort.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sao_tome_fort.jpg",
                "credit": "Autor desconocido · CC BY-SA 3.0",
                "caption": "El fuerte de São Sebastião, en la bahía de Ana Chaves.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fort_S%C3%A3o_Sebasti%C3%A3o_(S%C3%A3o_Tom%C3%A9)_(6).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fort_S%C3%A3o_Sebasti%C3%A3o_(S%C3%A3o_Tom%C3%A9)_(6).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "El museo nacional, dentro del fuerte.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sao_Tome_20_(16061446708).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sao_Tome_20_(16061446708).jpg",
                "credit": "Chuck Moravec · CC BY 2.0",
                "caption": "Una calle de la ciudad de São Tomé.",
            },
        ],
    ),
    dict(
        n=2, name="Roça Agostinho Neto · la mayor plantación colonial de la isla", cat="Cultura", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=0.3664732, lon=6.643769,  # Google Maps: Roça Agostinho Neto
        desc="Fundada en 1865 como Roça Rio do Ouro, es la plantación más imponente del país: una pequeña ciudad de cacao con hospital, capilla, almacenes y barracones de trabajadores, hoy medio en ruinas y medio habitada por unas mil personas. La casa señorial alberga un museo. OJO: no forma parte de la inscripción UNESCO de 2026, que eligió otras seis roças; aquí se ven la escala y la decadencia sin el barniz de la rehabilitación. El suelo está irregular y hay cascotes: calzado cerrado.",
        dog_note="Recinto abierto y semihabitado, con gente y perros locales; atado y sin entrar en el antiguo hospital ni en las viviendas.",
        visit={
            "why": "Para entender de golpe qué era el sistema de la roça: no una finca, sino una fábrica-pueblo levantada sobre trabajo forzado.",
            "see": "El patio central, el hospital arruinado, los secaderos de cacao, la capilla y el museo instalado en la casa del administrador.",
            "access": "Desvío corto desde la carretera de Guadalupe, asfalto hasta casi la entrada. Aparcamiento amplio para dos 4x4 en la explanada del patio. Entrada con propina o pequeña tarifa a un guía local: importe por confirmar. El pin marca la entrada del recinto de la roça.",
            "when": "Por la mañana, con luz y con la gente del poblado en la calle; evitar después de lluvia fuerte, el patio se embarra.",
            "skip": "Si el tiempo aprieta y se va a visitar Monte Café y Sundy, que sí son UNESCO, esta se puede dejar.",
        },
        links=[
            {"label": "Agostinho Neto / Roça Rio do Ouro (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Agostinho_Neto,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"},
            {"label": "Las roças de Santo Tomé y Príncipe (UNESCO, lista 1750)", "url": "https://whc.unesco.org/en/list/1750/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ro%C3%A7a_Agostinho_Neto_(S%C3%A3o_Tom%C3%A9)_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ro%C3%A7a_Agostinho_Neto_(S%C3%A3o_Tom%C3%A9)_(1).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "La roça Agostinho Neto.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ro%C3%A7a_Agostinho_Neto_(S%C3%A3o_Tom%C3%A9)_(4).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ro%C3%A7a_Agostinho_Neto_(S%C3%A3o_Tom%C3%A9)_(4).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "El hospital de la roça, en ruinas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ro%C3%A7a_Agostinho_Neto_(S%C3%A3o_Tom%C3%A9)_(14).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ro%C3%A7a_Agostinho_Neto_(S%C3%A3o_Tom%C3%A9)_(14).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "Viviendas de los trabajadores.",
            },
        ],
    ),
    dict(
        n=3, name="Parque natural Obô de São Tomé · la selva del interior", cat="Naturaleza", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=0.2886556, lon=6.6122827,  # Google Maps: Jardim Botânico do Bom Sucesso
        desc="195 km² de selva atlántica creados por la Lei 06/2006 del 13 de junio de 2006, repartidos en tres bloques: el macizo central con el Pico de São Tomé y el Pico Cão Grande, la zona de Malanza al sur y la de Praia das Conchas y Lagoa Azul al norte. Alberga DIECISÉIS aves endémicas, del ibis de Santo Tomé al picogordo. El centro de visitantes y jardín botánico de Bom Sucesso es la puerta real. La entrada al bosque exige guía acreditado y las trilhas son barrizales permanentes.",
        dog_note="Bosque con dieciséis aves endémicas y guía obligatorio; ningún operador acepta perro en las trilhas. Dejarlo en la base con uno de los tres.",
        visit={
            "why": "Es uno de los bosques con mayor densidad de endemismos del planeta y el corazón de la isla; sin él, Santo Tomé es solo playa y cacao.",
            "see": "Selva primaria de altura, helechos arborescentes, orquídeas y begonias endémicas, el jardín botánico de Bom Sucesso y, con suerte y guía, el loro gris y el ibis santomense.",
            "access": "Asfalto desde Trindade hasta Monte Café y pista corta hasta Bom Sucesso; con lluvia conviene el 4x4. Hay sitio para dos vehículos junto a la sede. El guía es obligatorio: unos 40 € por persona para Lagoa Amélia. El pin de la ficha marca el centroide del parque que da Wikipedia; la consulta de Maps lleva a Bom Sucesso, que es donde se aparca y se contrata.",
            "when": "Seca grande de junio a septiembre; salir al amanecer, la niebla se cierra a media mañana.",
            "skip": "Si llueve sin parar y no hay dos días de margen: las trilhas se vuelven un tobogán de barro.",
        },
        links=[
            {"label": "Parque Natural Obô de São Tomé (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Parque_Natural_Ob%C3%B4_de_S%C3%A3o_Tom%C3%A9"},
            {"label": "Trilha de Lagoa Amélia desde Bom Sucesso (Mucumbli Explore)", "url": "https://mucumbliexplore.com/trekking-2/lagoa-amelia/"},
            {"label": "Recorridos del Parque Nacional do Obô (São Tomé Trekking)", "url": "https://saotome-principe-trekking.com/des-parcours/parc-national-de-lobo"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Obo_National_Park_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Obo_National_Park_2.jpg",
                "credit": "Yakoo1986 · CC BY-SA 4.0",
                "caption": "La selva del parque natural Obô.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/%C3%93bo_(4238094175).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:%C3%93bo_(4238094175).jpg",
                "credit": "Maria Cartas · CC BY-SA 2.0",
                "caption": "Interior del Obô de São Tomé.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Philothamnus_thomensis._Endemic_snake_of_S%C3%A3o_Tom%C3%A9_in_the_Ob%C3%B4_Natural_Park.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Philothamnus_thomensis._Endemic_snake_of_S%C3%A3o_Tom%C3%A9_in_the_Ob%C3%B4_Natural_Park.jpg",
                "credit": "FrankBanalis · CC BY 4.0",
                "caption": "Culebra endémica del Obô.",
            },
        ],
    ),
    dict(
        n=4, name="Pico Cão Grande · la aguja volcánica de la selva del sur", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=0.1180133, lon=6.5659945,  # Google Maps: Pico Cão Grande
        desc="Un tapón volcánico de fonolita de 663 m que sobresale 370 m sobre la selva, formado hace unos 3,5 millones de años en la línea volcánica de Camerún. Es la imagen de portada del país. Solo se subió por primera vez en FEBRERO DE 1991, por un equipo japonés; en 2018 los hermanos Pou abrieron «Leve Leve» en 8b+. Para el viajero normal es un mirador de carretera: la roca está cubierta de musgo y hay serpientes. La pista desde Angolares hacia el sur está muy deteriorada.",
        dog_note="Los miradores están al borde de la carretera y son parada corta; atado y lejos del asfalto. Al interior del bosque, no.",
        visit={
            "why": "Es el icono del archipiélago y una de las agujas volcánicas más fotogénicas del mundo; se ve desde la propia carretera.",
            "see": "La aguja emergiendo de la selva del Obô, a veces decapitada por la nube; el pueblo de Vila Clotilde queda 3 km al este.",
            "access": "Carretera del sur desde São João dos Angolares: asfalto pésimo y baches profundos, mejor con 4x4, aunque un turismo alto pasa. Se aparca en el arcén, hay dos o tres ensanches con sitio para dos vehículos. El pin marca la cima; para conducir, usar el mirador de la carretera. Subir la aguja exige escalada técnica y permiso: descartado.",
            "when": "Primera hora de la mañana, antes de que la nube tape la punta; la seca de junio a septiembre da más días despejados.",
            "skip": "Si el cielo está cerrado y no hay margen para volver otro día, no merece el destrozo de la pista.",
        },
        links=[
            {"label": "Pico Cão Grande (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Pico_C%C3%A3o_Grande"},
            {"label": "Parque Natural Obô de São Tomé (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Parque_Natural_Ob%C3%B4_de_S%C3%A3o_Tom%C3%A9"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pico_C%C3%A3o_Grande.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pico_C%C3%A3o_Grande.jpg",
                "credit": "Philippe Bourachot · CC BY-SA 3.0",
                "caption": "El Pico Cão Grande.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/C%C3%A3o_Grande_et_C%C3%A3o_Pequeno_%C3%A0_S%C3%A3o_Tom%C3%A9_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:C%C3%A3o_Grande_et_C%C3%A3o_Pequeno_%C3%A0_S%C3%A3o_Tom%C3%A9_(1).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "El Cão Grande y el Cão Pequeno.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/2012SaoTome-308_(8042899981).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:2012SaoTome-308_(8042899981).jpg",
                "credit": "Helena Van Eykeren · CC BY 2.0",
                "caption": "La aguja volcánica sobre la selva.",
            },
        ],
    ),
    dict(
        n=5, name="Pico de São Tomé · el techo del archipiélago", cat="Naturaleza", prio="Media",
        dog="prohibido", time="2 días",
        lat=0.2882896, lon=6.5463156,  # Google Maps: Pico de São Tomé
        desc="2.024 m, techo del país y prominencia total de 2.024 m: se levanta desde el mar sin nada que lo iguale. Se sube desde Bom Sucesso vía Carvalho o desde la plantación de Ponta Figo, con campamento en Pico Mesa a 1.875 m. La travesía de Ponta Figo se puede hacer de un tirón en DIECIOCHO HORAS, pero entonces no se ve nada de la fauna. Exige dos guías por seguridad y equipo de vivac; la lluvia deja el sendero resbaladizo casi todo el año.",
        dog_note="Dos días de travesía con vivac dentro del parque, guía obligatorio y fauna endémica sensible: no es sitio para el perro.",
        visit={
            "why": "Es la cumbre del archipiélago y la travesía más seria del país, entre bosque de nube y vegetación de altura.",
            "see": "Bosque primario de niebla, epífitas, musgos colgantes y, desde arriba en días raros, las dos vertientes de la isla a la vez.",
            "access": "Se conduce hasta Bom Sucesso (asfalto desde Trindade hasta Monte Café y pista corta después) y a partir de ahí es todo a pie. Aparcamiento junto a la sede del parque. Dos guías obligatorios, desde unos 180 € solo los guías; la variante Bom Sucesso–Ponta Figo son 2 días. El pin marca la cima; a Maps hay que pedirle Bom Sucesso.",
            "when": "Solo en la seca grande, de junio a septiembre; salir de noche para llegar a la cumbre antes de que se cierre.",
            "skip": "Si no hay dos días limpios, experiencia de montaña y ropa que pueda mojarse hasta el final, se descarta sin discusión.",
        },
        links=[
            {"label": "Pico de São Tomé (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Pico_de_S%C3%A3o_Tom%C3%A9"},
            {"label": "Travesías del Parque Nacional do Obô (São Tomé Trekking)", "url": "https://saotome-principe-trekking.com/des-parcours/parc-national-de-lobo"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/C%C3%A3o_Grande_%C3%A0_S%C3%A3o_Tom%C3%A9.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:C%C3%A3o_Grande_%C3%A0_S%C3%A3o_Tom%C3%A9.jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "El relieve volcánico del interior de la isla.",
            },
        ],
    ),
    dict(
        n=6, name="Monte Café y las tierras altas del cacao (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=0.3004869, lon=6.6390931,  # Google Maps: Monte Café
        desc="A 670 m de altitud, una de las plantaciones más antiguas de la isla: establecida en 1858 y todavía viva, con familias jóvenes intentando recuperar el arábica y el cacao. Desde julio de 2026 es una de las SEIS roças inscritas en la Lista del Patrimonio Mundial de la UNESCO como «Las roças de Santo Tomé y Príncipe: sistema agrícola colonial y migración forzada» (criterio iv). Está de paso hacia Bom Sucesso. La niebla llega pronto y la pista final se embarra.",
        dog_note="Poblado vivo con familias y animales sueltos; atado en el recinto y fuera del museo y de la zona de secado.",
        visit={
            "why": "Es la roça que sigue funcionando y la que la UNESCO eligió como ejemplo del sistema colonial de café y cacao en altura.",
            "see": "Secaderos, la casa grande, el hospital, las senzalas de trabajadores y las terrazas de café arábica en la ladera.",
            "access": "Asfalto desde Trindade, 4,5 km al oeste, con los últimos metros en pista; aparcamiento holgado para dos 4x4 en el patio. Visita guiada por vecinos, propina o pequeña tarifa: importe por confirmar. El pin marca el núcleo de la roça; es el punto al que se conduce.",
            "when": "Antes de las once, cuando la niebla todavía no ha subido; combinar con Bom Sucesso el mismo día.",
            "skip": "Si ya se ha visto Agostinho Neto y solo se quiere una roça en ruina; aquí lo interesante es que sigue produciendo.",
        },
        links=[
            {"label": "Las roças de Santo Tomé y Príncipe (UNESCO, lista 1750)", "url": "https://whc.unesco.org/en/list/1750/"},
            {"label": "Monte Café (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Monte_Caf%C3%A9,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"},
            {"label": "Roça Bombaim y Roça Monte Café (Got2Globe)", "url": "https://www.got2globe.com/en/Editorial/roca-bombay-monte-cafe-sao-tome/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mus%C3%A9e_du_Caf%C3%A9_%C3%A0_Monte_Caf%C3%A9_(S%C3%A3o_Tom%C3%A9)_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mus%C3%A9e_du_Caf%C3%A9_%C3%A0_Monte_Caf%C3%A9_(S%C3%A3o_Tom%C3%A9)_(1).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "El museo del café de Monte Café.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Coop%C3%A9rative_de_Monte_Caf%C3%A9_(S%C3%A3o_Tom%C3%A9).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Coop%C3%A9rative_de_Monte_Caf%C3%A9_(S%C3%A3o_Tom%C3%A9).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "La cooperativa de Monte Café.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Grains_de_caf%C3%A9_et_f%C3%A8ves_de_cacao_grill%C3%A9s_%C3%A0_Monte_Caf%C3%A9_(S%C3%A3o_Tom%C3%A9).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Grains_de_caf%C3%A9_et_f%C3%A8ves_de_cacao_grill%C3%A9s_%C3%A0_Monte_Caf%C3%A9_(S%C3%A3o_Tom%C3%A9).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "Café y cacao tostados en Monte Café.",
            },
        ],
    ),
    dict(
        n=7, name="Lagoa Azul y el norte seco de la isla", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=0.4061199, lon=6.6088756,  # Google Maps: Lagoa Azul
        desc="Una pequeña bahía del norte, 4 km al noroeste de Guadalupe, con agua transparente y uno de los mejores fondos de la isla para bucear. Sorprende el contraste: aquí el paisaje es seco, con baobabs y matorral, a media hora de la selva empapada del interior. Forma parte del bloque norte del Parque Natural Obô, junto con Praia das Conchas. Hay un faro de 1997 cerca. No hay servicios, sombra escasa y el acceso final es pista.",
        dog_note="Cala abierta sin vigilancia y sin prohibición conocida; atado cerca de bañistas y fuera del agua donde haya gente buceando.",
        visit={
            "why": "Es el mejor snorkel accesible en coche de la isla y la cara seca y africana de un país que uno espera solo verde.",
            "see": "Bahía turquesa, fondos de roca volcánica, baobabs en la ladera y el faro de Lagoa Azul de 1997.",
            "access": "Asfalto hasta Guadalupe y desvío de pista corta hacia el noroeste; se pasa bien con 4x4 y hay explanada junto a la cala para dos vehículos. Sin entrada ni horario. El pin marca la bahía, que es donde se aparca.",
            "when": "Marea baja y primera hora, antes de que el viento rice el agua; los fines de semana se llena de familias.",
            "skip": "Con marejada o agua turbia pierde todo el sentido: es un sitio para meter la cabeza en el agua.",
        },
        links=[
            {"label": "Lagoa Azul (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Lagoa_Azul"},
            {"label": "Parque Natural Obô de São Tomé (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Parque_Natural_Ob%C3%B4_de_S%C3%A3o_Tom%C3%A9"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lagoa_Azul_(S%C3%A3o_Tom%C3%A9)_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lagoa_Azul_(S%C3%A3o_Tom%C3%A9)_(1).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "La Lagoa Azul.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Baobabs_%C3%A0_Lagoa_Azul_(S%C3%A3o_Tom%C3%A9)_(3).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Baobabs_%C3%A0_Lagoa_Azul_(S%C3%A3o_Tom%C3%A9)_(3).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "Baobabs en el norte seco de la isla.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sao_Tome_Blue_Lagoon_4_(16061430518).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sao_Tome_Blue_Lagoon_4_(16061430518).jpg",
                "credit": "Chuck Moravec · CC BY 2.0",
                "caption": "La costa de la Lagoa Azul.",
            },
        ],
    ),
    dict(
        n=8, name="Praia dos Tamarindos · la costa norte", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=0.4088684, lon=6.646107,  # Google Maps: Praia dos Tamarindos
        desc="Arenal en media luna de la costa norte, cerca de Morro Peixe y a un paso de la Roça Agostinho Neto, con agua templada y sombra natural de tamarindos. Es playa de fin de semana santomense, con puestos de comida y bungalós. AVISO: el nombre del PDI original la emparejaba con Praia Piscina como «costa nordeste», y no es así: Praia Piscina está en el extremo sur, a medio camino entre Praia Inhame y Praia Jalé, y se trata en la ficha 10. Cuidado con los robos y con la basura de los domingos.",
        dog_note="Playa pública sin vigilancia; atado los fines de semana, que se llena de gente, y lejos de los puestos de comida.",
        visit={
            "why": "Es el baño fácil del norte, a veinte minutos de la mayor roça del país, y sirve de descanso tras la visita a Agostinho Neto.",
            "see": "Media luna de arena, tamarindos que dan sombra, barcas de pesca y puestos de comida local.",
            "access": "EN1 hacia el norte y desvío de pista hacia el mar; el estado del ramal aconseja 4x4. Sitio de sobra para dos vehículos junto a la arena. Sin entrada ni horario. El pin marca el acceso a la playa. Vigilar objetos en el coche: hay denuncias de robos.",
            "when": "Entre semana y por la mañana; el fin de semana se llena y queda basura.",
            "skip": "Si ya se ha parado en Lagoa Azul o Praia das Conchas el mismo día, es redundante.",
        },
        links=[
            {"label": "Praia dos Tamarindos (SaoTomeExpert)", "url": "https://www.saotomeexpert.pt/en/the-beaches/praia-dos-tamarindos/"},
            {"label": "Las playas más bonitas de Santo Tomé y Príncipe (Alma de Viajante)", "url": "https://www.almadeviajante.com/praias-sao-tome-e-principe/"},
            {"label": "Lista de playas de Santo Tomé y Príncipe (Wikipedia)", "url": "https://en.wikipedia.org/wiki/List_of_beaches_of_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Football_sur_la_plage_des_Tamarins_(S%C3%A3o_Tom%C3%A9)_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Football_sur_la_plage_des_Tamarins_(S%C3%A3o_Tom%C3%A9)_(1).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "Fútbol en la praia dos Tamarindos.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fillettes_jouant_sur_la_plage_des_Tamarins_(S%C3%A3o_Tom%C3%A9)_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fillettes_jouant_sur_la_plage_des_Tamarins_(S%C3%A3o_Tom%C3%A9)_(1).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "La playa de los Tamarindos.",
            },
        ],
    ),
    dict(
        n=9, name="São João dos Angolares y la costa sur · Roça São João (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=0.139087, lon=6.6476518,  # Google Maps: Roça São João dos Angolares
        desc="Capital del distrito de Caué y corazón de los angolares, la comunidad de pescadores cuyo criollo, el ngola, todavía se habla aquí. La Roça São João está rehabilitada como hotel, restaurante y centro de arte, y es UNA DE LAS SEIS roças inscritas por la UNESCO en 2026. Es la última base cómoda antes del sur profundo: desde aquí la carretera se degrada de verdad. Buen sitio para dormir y comer antes de atacar Cão Grande y Porto Alegre.",
        dog_note="La roça es hotel y restaurante: hay que pedir permiso a la casa; en el pueblo y la carretera, atado.",
        visit={
            "why": "Une en un solo alto patrimonio mundial, cocina santomense de verdad y la mejor terraza sobre la costa sur.",
            "see": "La casa grande de la roça sobre la bahía, los secaderos, el pueblo de pescadores y las playas de la vuelta.",
            "access": "Asfalto en buen estado desde la capital, alrededor de una hora y cuarto por la costa este. Aparcamiento propio de la roça para dos 4x4. A partir de aquí hacia el sur la carretera está llena de socavones y conviene reducir. El pin marca el núcleo del pueblo; para conducir, pedir la Roça São João.",
            "when": "Llegar para la comida y quedarse a dormir; en seca (junio-septiembre) la costa sur es mucho más transitable.",
            "skip": "Solo si no se va a bajar al sur: como parada intermedia no tiene sustituto.",
        },
        links=[
            {"label": "Las roças de Santo Tomé y Príncipe (UNESCO, lista 1750)", "url": "https://whc.unesco.org/en/list/1750/"},
            {"label": "São João dos Angolares (Wikipedia)", "url": "https://en.wikipedia.org/wiki/S%C3%A3o_Jo%C3%A3o_dos_Angolares"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Habitations_%C3%A0_S%C3%A3o_Jo%C3%A3o_dos_Angolares_(S%C3%A3o_Tom%C3%A9)_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Habitations_%C3%A0_S%C3%A3o_Jo%C3%A3o_dos_Angolares_(S%C3%A3o_Tom%C3%A9)_(1).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "São João dos Angolares.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Wharf_at_Praia_Sao_Jo%C3%A3o_de_Angolares_(21047452755).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Wharf_at_Praia_Sao_Jo%C3%A3o_de_Angolares_(21047452755).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "El embarcadero de los Angolares.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sortie_de_S%C3%A3o_Jo%C3%A3o_dos_Angolares_(S%C3%A3o_Tom%C3%A9).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sortie_de_S%C3%A3o_Jo%C3%A3o_dos_Angolares_(S%C3%A3o_Tom%C3%A9).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "La carretera de la costa sur.",
            },
        ],
    ),
    dict(
        n=10, name="Praia Jalé y el sur profundo · las tortugas", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1 noche",
        lat=0.0545449, lon=6.5150587,  # Google Maps: Praia Jalé
        desc="El extremo sur de la isla: arena, cocoteros, un ecolodge de cabañas sin electricidad y, sobre todo, tortugas. En el archipiélago anidan CINCO especies —verde, olivácea, carey, laúd y ocasionalmente boba— entre septiembre y abril, con el pico de noviembre a febrero. El Programa Tatô vigila 52 playas y organiza las salidas nocturnas. Praia Piscina, con su piscina natural, queda a medio camino entre Praia Inhame y Jalé. La pista desde Angolares es la peor de la isla.",
        dog_note="Playa de desove vigilada por el Programa Tatô: un perro suelto entre nidos y crías es inaceptable, y de noche está prohibido el acceso libre.",
        visit={
            "why": "Ver salir una tortuga a desovar o soltar crías al amanecer es la experiencia más fuerte del viaje, y aquí está organizada y bien controlada.",
            "see": "Playa virgen, cocotero sobre la arena, las charcas de Praia Piscina en el camino y, en temporada, nidos y crías de tortuga.",
            "access": "Desde São João dos Angolares la carretera se degrada mucho y hace falta 4x4 real; el último tramo a Jalé es pista. Aparcamiento junto al ecolodge, cabe un par de vehículos. Solo se accede a la playa de noche con guardas del programa. El pin marca el ecolodge, que es hasta donde se conduce.",
            "when": "De noviembre a febrero para las tortugas; el resto del año la playa está vacía pero sin el espectáculo.",
            "skip": "Fuera de la temporada de desove y con lluvia, la paliza de pista no compensa: quedarse en Angolares.",
        },
        links=[
            {"label": "Programa Tatô · São Tomé", "url": "https://www.programatato.org/en/sao-tome"},
            {"label": "Praia Jalé (Visit São Tomé)", "url": "http://www.visitsaotome.com/beach/praia-jale.html"},
            {"label": "Praia Inhame (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Praia_Inhame"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Praia_Jal%C3%A9_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Praia_Jal%C3%A9_-_panoramio.jpg",
                "credit": "Luís Rochinha · CC BY 3.0",
                "caption": "La praia Jalé.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Entre_a_Praia_Jal%C3%A9_e_a_Praia_Piscina_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Entre_a_Praia_Jal%C3%A9_e_a_Praia_Piscina_-_panoramio.jpg",
                "credit": "Luís Rochinha · CC BY 3.0",
                "caption": "Entre Jalé y la praia Piscina.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/S%C3%A3o_Tom%C3%A9_-_Praia_Jal%C3%A8.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:S%C3%A3o_Tom%C3%A9_-_Praia_Jal%C3%A8.jpg",
                "credit": "Paulacastelli · CC BY-SA 4.0",
                "caption": "El sur profundo de la isla.",
            },
        ],
    ),
    dict(
        n=11, name="Ilhéu das Rolas · la línea del Ecuador", cat="Naturaleza", prio="Alta",
        dog="por confirmar", time="1 noche",
        lat=-0.0069495, lon=6.5223089,  # Google Maps: Ilhéu das Rolas
        desc="Islote de 2 km² separado del extremo sur de la isla por el canal das Rolas y atravesado por la LÍNEA DEL ECUADOR, hecho que comprobó el navegante Gago Coutinho; hay un monumento que marca el paralelo cero. Lo ocupa en buena parte el resort Pestana Equador. Se llega solo en barca desde Ponta Baleia, en São Tomé. Los vehículos se quedan en tierra: hay que dejarlos aparcados y vigilados en Porto Alegre.",
        dog_note="Se llega en barca y el islote lo ocupa casi entero un resort; hay que preguntar al Pestana Equador antes de embarcar.",
        visit={
            "why": "Pisar la línea del Ecuador en una isla diminuta del golfo de Guinea es una de esas paradas que no se repiten.",
            "see": "El monumento del Ecuador, playas de ambos hemisferios, el canal das Rolas y fondos buenos para snorkel.",
            "access": "Carretera hasta Porto Alegre (pista mala desde Angolares) y barca desde el embarcadero de Ponta Baleia; no hay transbordador de vehículos. Los dos 4x4 se dejan en el muelle o en el pueblo. Horarios y precio de la barca: por confirmar, se pactan con el resort o con pescadores. El pin de la ficha marca el islote; a Maps hay que pedirle Ponta Baleia.",
            "when": "Mar en calma y mañana temprano; seca de junio a septiembre para la travesía.",
            "skip": "Con mar picado o si no se puede dejar los vehículos con garantías en tierra.",
        },
        links=[
            {"label": "Ilhéu das Rolas (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Ilh%C3%A9u_das_Rolas"},
            {"label": "Porto Alegre (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Porto_Alegre,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/S%C3%A3o_Tom%C3%A9_-_Ilh%C3%A9u_das_Rolas_HDR.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:S%C3%A3o_Tom%C3%A9_-_Ilh%C3%A9u_das_Rolas_HDR.jpg",
                "credit": "Rui Almeida · CC BY 2.0",
                "caption": "El ilhéu das Rolas, cortado por el Ecuador.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/S%C3%A3o_Tom%C3%A9_-_Ilh%C3%A9u_das_Rolas_-_Praia_de_Santo_Ant%C3%B3nio_(3).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:S%C3%A3o_Tom%C3%A9_-_Ilh%C3%A9u_das_Rolas_-_Praia_de_Santo_Ant%C3%B3nio_(3).jpg",
                "credit": "Rui Almeida · CC BY 2.0",
                "caption": "Praia de Santo António, en Rolas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ilheu_das_Rolas_(4056240841).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ilheu_das_Rolas_(4056240841).jpg",
                "credit": "Maria Cartas · CC BY-SA 2.0",
                "caption": "La isla de las Rolas desde el mar.",
            },
        ],
    ),
    dict(
        n=12, name="Roça Bombaim y las plantaciones del interior", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=0.2456814, lon=6.632414,  # Google Maps: Roça Bombaim
        desc="Al final de la pista del interior, en el borde del Parque Natural Obô, queda una roça que se apaga: DIECIOCHO habitantes en el censo de 2012, frente a treinta en 2001, y buena parte de los edificios tomados por las higueras. Es lo contrario de Monte Café: la ruina sin rehabilitar, con la selva comiéndose el patio. Desde aquí sale la travesía a pie hacia São João dos Angolares. La pista de acceso es de tierra y se embarra en cuanto llueve.",
        dog_note="Recinto casi desierto, con dieciocho vecinos y alguna gallina; atado y sin entrar en las viviendas ocupadas.",
        visit={
            "why": "Es la roça abandonada más accesible del interior y la mejor imagen del final del ciclo del cacao.",
            "see": "Casa grande vacía, secaderos invadidos por la vegetación, la pista que se pierde en el bosque y el arranque de las trilhas del Obô.",
            "access": "Desde Trindade, asfalto y después pista de tierra; a unos 8 km al suroeste de Trindade y 6 km al sur de Monte Café. Con lluvia hace falta 4x4 y tracción real. Hay espacio para dos vehículos en el patio. Alojamiento sencillo en la propia roça. El pin marca el núcleo de la roça.",
            "when": "En seca, junio-septiembre; por la mañana, antes de que la niebla baje del Obô.",
            "skip": "Si ha llovido con ganas: la pista final se convierte en barro y no hay dónde dar la vuelta.",
        },
        links=[
            {"label": "Bombaim (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bombaim"},
            {"label": "Roça Bombaim y Roça Monte Café (Got2Globe)", "url": "https://www.got2globe.com/en/Editorial/roca-bombay-monte-cafe-sao-tome/"},
            {"label": "Monte Forte (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Monte_Forte,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Vestiges_de_l'ancienne_ro%C3%A7a_Bombaim_(S%C3%A3o_Tom%C3%A9)_(3).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Vestiges_de_l'ancienne_ro%C3%A7a_Bombaim_(S%C3%A3o_Tom%C3%A9)_(3).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "Restos de la roça Bombaim.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cr%C3%A9puscule_%C3%A0_la_ro%C3%A7a_Bombaim_(S%C3%A3o_Tom%C3%A9)_(2).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cr%C3%A9puscule_%C3%A0_la_ro%C3%A7a_Bombaim_(S%C3%A3o_Tom%C3%A9)_(2).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "Anochecer en Bombaim.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pousada_Ro%C3%A7a_Bombaim_(S%C3%A3o_Tom%C3%A9)_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pousada_Ro%C3%A7a_Bombaim_(S%C3%A3o_Tom%C3%A9)_(1).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "La pousada de Bombaim.",
            },
        ],
    ),
    dict(
        n=13, name="Neves, Monte Forte y el oeste · la cervecería y la costa de barlovento", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=0.3560223, lon=6.5489836,  # Google Maps: Neves
        desc="Segunda población de la isla, 10.068 habitantes, capital de Lembá y sede de la Cervejeira Rosema, la fábrica que hace la cerveza nacional. Tiene puerto de aguas profundas con un espigón de 400 m capaz de recibir dos Panamax, construido con Nigeria en 2012. Al sur quedan Monte Forte, con su secadero de cacao, y la Roça Diogo Vaz, una de las SEIS inscritas por la UNESCO en 2026. El asfalto del oeste termina en Santa Catarina: más allá no hay carretera.",
        dog_note="Puerto industrial y pueblo: atado siempre. La fábrica de cerveza no es visitable con animales.",
        visit={
            "why": "Es el punto de avituallamiento del oeste y la puerta de la costa de barlovento, con la roça Diogo Vaz (UNESCO) de camino.",
            "see": "El puerto y las barcas de pesca, la cervecería Rosema, los secaderos de Monte Forte y la fachada atlántica hasta Santa Catarina.",
            "access": "Asfalto por la EN1 desde la capital rodeando el norte, alrededor de una hora. Aparcamiento fácil en el frente portuario para dos 4x4. La visita a la cervecería no tiene régimen publicado: por confirmar. El pin marca el pueblo; en Maps, pedir la Cervejeira Rosema.",
            "when": "Media mañana, cuando entra la pesca; en seca, la carretera del oeste está bastante mejor.",
            "skip": "Si no se va a seguir hasta Santa Catarina o Diogo Vaz, el pueblo en sí no justifica el desvío.",
        },
        links=[
            {"label": "Neves (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Neves,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"},
            {"label": "Diogo Vaz (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Diogo_Vaz,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"},
            {"label": "Las roças de Santo Tomé y Príncipe (UNESCO, lista 1750)", "url": "https://whc.unesco.org/en/list/1750/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sao_Tome_Neves_1_(16062959309).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sao_Tome_Neves_1_(16062959309).jpg",
                "credit": "Chuck Moravec · CC BY 2.0",
                "caption": "Neves, en la costa de barlovento.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Maisons_de_p%C3%AAcheurs_%C3%A0_Neves_(S%C3%A3o_Tom%C3%A9).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Maisons_de_p%C3%AAcheurs_%C3%A0_Neves_(S%C3%A3o_Tom%C3%A9).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "Casas de pescadores en Neves.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Architecture_coloniale_%C3%A0_Neves_(S%C3%A3o_Tom%C3%A9).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Architecture_coloniale_%C3%A0_Neves_(S%C3%A3o_Tom%C3%A9).jpg",
                "credit": "Ji-Elle · CC BY-SA 4.0",
                "caption": "Arquitectura colonial en Neves.",
            },
        ],
    ),
    dict(
        n=14, name="Boca do Inferno y la costa de Água Izé", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=0.21345, lon=6.72627,  # Google Maps: Boca do Inferno (sin objeto fiable en Google Maps; coordenada de la fuente)
        desc="Una furna de soplo en la costa este: el mar entra por una galería de lava y sale disparado por un agujero del acantilado. Está a media hora al sur del centro de la capital y a cinco minutos a pie de la carretera principal, lo que la convierte en la parada más rentable de la EN2. Al lado queda la Roça Água Izé, otra de las SEIS inscritas por la UNESCO en 2026, con edificios conservados de los años diez. La roca está mojada y resbala.",
        dog_note="Mirador sobre acantilado con roca resbaladiza y chorro de agua a presión: atado y corto, nunca suelto cerca del agujero.",
        visit={
            "why": "Es un fenómeno geológico espectacular que se ve en diez minutos y está literalmente al borde de la ruta del sur.",
            "see": "El chorro del géiser marino contra el acantilado, la playa Izé 180 m al norte y, a un paso, los almacenes y viviendas de la Roça Água Izé.",
            "access": "EN2 asfaltada desde la capital, unos 30 minutos; se deja el coche en el arcén, hay hueco para dos vehículos, y se baja andando cinco minutos. Sin entrada ni horario. El pin marca el mirador; coordenadas tomadas de un mapa colaborativo, pendientes de verificar sobre el terreno.",
            "when": "Con marea alta y mar de fondo, que es cuando el chorro funciona de verdad; cualquier hora del día.",
            "skip": "Con mar plano no sopla nada y se queda en un agujero en la roca.",
        },
        links=[
            {"label": "Água Izé (Wikipedia)", "url": "https://en.wikipedia.org/wiki/%C3%81gua_Iz%C3%A9"},
            {"label": "Boca do Inferno, Cantagalo (Mapcarta)", "url": "https://mapcarta.com/N2848219674"},
            {"label": "Las roças de Santo Tomé y Príncipe (UNESCO, lista 1750)", "url": "https://whc.unesco.org/en/list/1750/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Casa_das_Caldeiras_Sao_Tome_Island.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Casa_das_Caldeiras_Sao_Tome_Island.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La casa das Caldeiras de Água Izé.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Former_Hospital_Ro%C3%A7a_Agua_Iz%C3%A9.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Former_Hospital_Ro%C3%A7a_Agua_Iz%C3%A9.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "El antiguo hospital de Água Izé.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cocoa_Warehouse_Ro%C3%A7a_Agua_Iz%C3%A9_on_Sao_Tome_Island.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cocoa_Warehouse_Ro%C3%A7a_Agua_Iz%C3%A9_on_Sao_Tome_Island.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "Almacén de cacao en Água Izé.",
            },
        ],
    ),
    dict(
        n=15, name="Santo António do Príncipe · la capital más pequeña de África", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=1.6367611, lon=7.417857,  # Google Maps: Santo António (Príncipe)
        desc="2.620 habitantes, el 35 % de la población de Príncipe: se la llama la capital más pequeña de África, aunque ninguna fuente oficial consultada lo certifica y conviene manejarlo como dato popular. Fundada en 1502 sobre la caña de azúcar, fue capital colonial del archipiélago entre 1753 y 1852, y desde el 29 de abril de 1995 es capital de la Región Autónoma de Príncipe. Base única de la isla: 18 km de carretera en total y ni una agencia formal de alquiler.",
        dog_note="Pueblo tranquilo, sin prohibición conocida; atado. Llegar a Príncipe en avión con perro exige trámite sanitario aparte.",
        visit={
            "why": "Es la base de todo Príncipe y un pueblo colonial portugués intacto y sin turistas, con edificios que se caen a cámara lenta.",
            "see": "La plaza, la iglesia, el antiguo ayuntamiento, el puerto fluvial y las casas coloniales del casco.",
            "access": "Se llega en avión desde São Tomé (30-40 minutos, STP Airways y Africa's Connection, 18 vuelos semanales) o en barco, 6-12 horas: NO hay transbordador de vehículos. En la isla no operan agencias de alquiler; se contrata un 4x4 con conductor a través del alojamiento por unos 60 €/día. El pin marca el pueblo.",
            "when": "Seca de junio a septiembre; el traslado del aeropuerto son 3 km y 15-20 minutos.",
            "skip": "Si no se puede dedicar a Príncipe tres días completos, no compensa el puente aéreo.",
        },
        links=[
            {"label": "Santo António (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Santo_Ant%C3%B3nio"},
            {"label": "Región Autónoma de Príncipe (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Autonomous_Region_of_Pr%C3%ADncipe"},
            {"label": "Cómo moverse por Príncipe (SaoTomeExpert)", "url": "https://www.saotomeexpert.pt/en/sao-tome-principe-island-getting-around/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Santo_Ant%C3%B3nio,_Capital_of_Pr%C3%ADncipe.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Santo_Ant%C3%B3nio,_Capital_of_Pr%C3%ADncipe.JPG",
                "credit": "Yellowcarpenter · CC BY-SA 4.0",
                "caption": "Santo António, capital de Príncipe.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Street_in_Santo_Antonio_-_Principe_2015.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Street_in_Santo_Antonio_-_Principe_2015.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "Una calle de Santo António.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Igreja_Nossa_Senhora_do_Ros%C3%A1rio_in_Santo_Antonio_-_Principe_2015.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Igreja_Nossa_Senhora_do_Ros%C3%A1rio_in_Santo_Antonio_-_Principe_2015.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La iglesia de Nossa Senhora do Rosário.",
            },
        ],
    ),
    dict(
        n=16, name="Roça Sundy · el eclipse de 1919 y la relatividad (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=1.6697083, lon=7.3837351,  # Google Maps: Roça Sundy
        desc="Aquí, el 29 DE MAYO DE 1919, Arthur Eddington fotografió el eclipse total que confirmó la relatividad general: llovió esa mañana, hizo dieciséis placas y para el 3 de junio ya sabía que Einstein tenía razón; el resultado se presentó en noviembre en Londres. Sundi acogió en 1822 la primera plantación de cacao del archipiélago. La casa grande está restaurada como hotel y la roça es una de las SEIS inscritas por la UNESCO en 2026. Está a 20 minutos del aeropuerto.",
        dog_note="La casa grande es hotel de la Príncipe Collection y el recinto está reglado; sin autorización previa, no.",
        visit={
            "why": "Pocos sitios del mundo pueden decir que ahí se comprobó una teoría física; y encima es patrimonio mundial desde 2026.",
            "see": "La casa grande restaurada, la placa del eclipse, el hospital y la iglesia en ruina, las senzalas y los secaderos de cacao.",
            "access": "Pista desde Santo António, unos 5 km; desde el aeropuerto son 20 minutos de conducción. Sin agencia de alquiler en la isla: se llega con conductor o en taxi. Aparcamiento en el patio de la roça. Horario y tarifa de visita: por confirmar, el recinto lo gestiona el hotel. El pin es aproximado, deducido de la posición de Sundy Praia.",
            "when": "Mañana, con la luz baja sobre el patio; 1-2 horas bastan para recorrerlo.",
            "skip": "No se descarta: es el motivo principal para volar a Príncipe.",
        },
        links=[
            {"label": "Las roças de Santo Tomé y Príncipe (UNESCO, lista 1750)", "url": "https://whc.unesco.org/en/list/1750/"},
            {"label": "Experimento de Eddington (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Eddington_experiment"},
            {"label": "Cómo llegar a Roça Sundy (Príncipe Collection)", "url": "https://www.principecollection.com/en/hotels/roca-sundy/getting-to-roca-sundy"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Principe_1399.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Principe_1399.jpg",
                "credit": "César J. Pollo · CC BY-SA 4.0",
                "caption": "La roça Sundy, en Príncipe.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Principe_1468.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Principe_1468.jpg",
                "credit": "César J. Pollo · CC BY-SA 4.0",
                "caption": "Dependencias de la roça Sundy.",
            },
        ],
    ),
    dict(
        n=17, name="Praia Banana y las playas de Príncipe", cat="Costa", prio="Alta",
        dog="por confirmar", time="medio día",
        lat=1.6901259, lon=7.4418641,  # Google Maps: Praia das Bananas
        desc="La media luna de arena bajo Belo Monte es la playa más fotografiada del país y sale en los anuncios de una marca de café desde los años ochenta. Se llega bajando desde la Roça Belo Monte, antigua plantación de cacao de 1922 hoy convertida en resort de naturaleza y, desde 2026, una de las SEIS roças UNESCO. Enfrente queda el Ilhéu Bom Bom, unido a Príncipe por una pasarela peatonal. El acceso a la playa suele estar controlado por el resort.",
        dog_note="El acceso pasa por la finca de Belo Monte, hoy resort privado: depende del permiso de la casa.",
        visit={
            "why": "Es la postal del archipiélago y el mejor baño de Príncipe, con la roça UNESCO de Belo Monte justo encima.",
            "see": "La media luna de arena entre selva y roca, el mirador de Belo Monte y, a 3 km al noroeste, la pasarela al Ilhéu Bom Bom.",
            "access": "Pista desde Santo António hacia el noreste; hacen falta 4x4 y conductor local, porque no hay señalización. Aparcamiento en la roça y bajada a pie de unos minutos. Condiciones de acceso y posible tarifa: por confirmar con Belo Monte. El pin es aproximado, de mapa colaborativo.",
            "when": "Mañana, antes de que el resort ocupe la arena; seca de junio a septiembre.",
            "skip": "Si el resort cierra el paso ese día, redirigir a Praia Macaco o a Bom Bom.",
        },
        links=[
            {"label": "Belo Monte (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Belo_Monte,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"},
            {"label": "Ilhéu Bom Bom (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Ilh%C3%A9u_Bom_Bom"},
            {"label": "Las roças de Santo Tomé y Príncipe (UNESCO, lista 1750)", "url": "https://whc.unesco.org/en/list/1750/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/BAN_-_Panoramic_view_of_Praia_Banana,_Principe,_Sao_Tome_and_Principe,_2021.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:BAN_-_Panoramic_view_of_Praia_Banana,_Principe,_Sao_Tome_and_Principe,_2021.jpg",
                "credit": "Josep M. Gracia · CC BY-SA 4.0",
                "caption": "La praia Banana.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/BAN_-_Tropical_beach_landscape_at_Praia_Banana,_Principe,_Sao_Tome_and_Principe,_2021.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:BAN_-_Tropical_beach_landscape_at_Praia_Banana,_Principe,_Sao_Tome_and_Principe,_2021.jpg",
                "credit": "Josep M. Gracia · CC BY-SA 4.0",
                "caption": "La curva de la praia Banana.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/BAN_-_Rocky_cove_at_Praia_Banana,_Principe,_Sao_Tome_and_Principe,_2021.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:BAN_-_Rocky_cove_at_Praia_Banana,_Principe,_Sao_Tome_and_Principe,_2021.jpg",
                "credit": "Josep M. Gracia · CC BY-SA 4.0",
                "caption": "Cala rocosa junto a la playa.",
            },
        ],
    ),
    dict(
        n=18, name="Parque natural Obô do Príncipe · la Reserva de la Biosfera", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1 día",
        lat=1.5793994, lon=7.3804721,  # Google Maps: Parque Natural Obô do Príncipe
        desc="85 km² creados por la Lei 07/2006 del 13 de junio de 2006 sobre la mitad sur de la isla. Príncipe entera es Reserva de la Biosfera de la UNESCO DESDE 2012 —71.592 ha entre tierra y mar, islotes incluidos— y en septiembre de 2025 el país se convirtió en el primer Estado del mundo con todo su territorio declarado reserva de la biosfera. Aquí viven el tordo y el autillo de Príncipe, ambos en peligro crítico. Solo se entra con guía acreditado; al sur de Ribeira Fria no hay carreteras.",
        dog_note="Guía acreditado obligatorio para entrar y dos endemismos en peligro crítico (tordo y autillo de Príncipe): el perro se queda en Santo António.",
        visit={
            "why": "Es el núcleo de la primera reserva de la biosfera que cubre un país entero y uno de los bosques insulares menos alterados del Atlántico.",
            "see": "Selva húmeda cerrada, el Pico do Papagaio, la cascada de Oquê Pipi, la roça Infante abandonada y aves que no existen en ningún otro sitio.",
            "access": "Se conduce hasta el borde norte del parque por las pistas de la isla; el sur es solo a pie. Guía acreditado OBLIGATORIO, se contrata en el hotel, en la oficina del parque en Santo António o en las asociaciones de guías. Pico do Papagaio: 6 h ida y vuelta con cuerdas fijas en lo más empinado. Tasas: por confirmar. El pin marca el centro del parque.",
            "when": "Estación seca de junio a septiembre; salida al amanecer, la senda es fango resbaladizo casi siempre.",
            "skip": "Si llueve o no hay guía disponible: entrar sin él no está permitido.",
        },
        links=[
            {"label": "Parque Natural Obô do Príncipe (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Parque_Natural_Ob%C3%B4_do_Pr%C3%ADncipe"},
            {"label": "Reserva de la Biosfera de la Isla de Príncipe (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Island_of_Pr%C3%ADncipe_Biosphere_Reserve"},
            {"label": "26 nuevas reservas de la biosfera, 2025 (UNESCO)", "url": "https://www.unesco.org/en/articles/26-new-biosphere-reserves-unescos-continues-unprecedented-expansion-its-global-network"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pr%C3%ADncipe_Island_Biosphere_Reserve_-_Praia_Caix%C3%A3o_mangorve.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pr%C3%ADncipe_Island_Biosphere_Reserve_-_Praia_Caix%C3%A3o_mangorve.jpg",
                "credit": "Antoniodabreu · CC BY-SA 4.0",
                "caption": "Manglar de la reserva de la biosfera de Príncipe.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Principe_Island_3155.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Principe_Island_3155.jpg",
                "credit": "César J. Pollo · CC BY-SA 4.0",
                "caption": "La selva del Obô de Príncipe.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pr%C3%ADncipe_Island_Biosphere_Reserve_-_Praia_Salgada.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pr%C3%ADncipe_Island_Biosphere_Reserve_-_Praia_Salgada.jpg",
                "credit": "Antoniodabreu · CC BY-SA 4.0",
                "caption": "Praia Salgada, en Príncipe.",
            },
        ],
    ),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul", "cultura": "morado",
              "patrimonio unesco": "marron", "costa": "turquesa"}
for _p in POIS:
    # La portada de la tarjeta, el globo del mapa y el modal es siempre la primera foto de la galería.
    _p["img"] = _p["photos"][0]["img"]
    _p["source"] = _p["photos"][0]["source"]
    _p["credit"] = _p["photos"][0]["credit"]
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")

LOGISTICS = [
    ("Aeropuerto Internacional de São Tomé (TMS)", "Frontera", 0.3775266, 6.7126096,  # Google Maps: Aeropuerto Internacional de São Tomé
     "Único punto de entrada internacional realista. Pista 11/29 de 2.220 m, a 5 km de la capital. TAP, STP Airways, TAAG, ASKY y Afrijet. Tasa de turismo de 25 € por persona a la llegada; sin visado hasta 15 días para españoles. SIM de CST o Unitel a la venta en el aeropuerto. Pin comprobado en Google Maps («Aeropuerto Internacional de São Tomé»)."),
    ("Aeropuerto de Príncipe (PCP)", "Frontera", 1.6651361, 7.4126229,  # Google Maps: Aeropuerto de Príncipe
     "Aeropuerto de la isla de Príncipe, cerca de Santo António. Pista 18/36 de 1.750 m ampliada entre 2012 y 2015. Solo enlaces con São Tomé (STP Airways, 20 plazas; Afrijet, 70), media hora de vuelo, con cancelaciones frecuentes. Tasa de turismo de 10 € si se entra por aquí. Pin comprobado en Google Maps («Aeropuerto de Príncipe»)."),
    ("Puerto de São Tomé, bahía de Ana Chaves", "Frontera", 0.3411127, 6.7273746,  # Google Maps: Baía de Ana Chaves
     "Puerto principal del país para mercancía sólida, construido a finales de los años cincuenta sobre terreno ganado al mar: muelle de 200 m y 3 m de calado. Salida del barco interinsular Olivia C. Sin línea regular que admita vehículos rodados. Pin comprobado en Google Maps («Baía de Ana Chaves»)."),
    ("Embajada de España en Libreville (competente para Santo Tomé y Príncipe)", "Consular", 0.389406, 9.443011,  # Google Maps: Embajada de España en Libreville
     "Immeuble Diamant, 2ème étage, Bd. de la Nation, Arrondissement 3, B.P. 1157, Libreville (Gabón). Emergencia consular +241 66 44 47 47. España NO tiene embajada residente en Santo Tomé. Pin comprobado en Google Maps («Embajada de España en Libreville»)."),
    ("Consulado Honorario de España en Santo Tomé", "Consular", 0.3364, 6.7273,  # Google Maps: Ciudad de São Tomé (el consulado honorario no figura como objeto)
     "Cónsul honorario: Miguel Martín Alomar. Teléfonos +239 997 80 22 y +34 601 41 12 84 (MAEC, 1 jun. 2026). DIRECCIÓN EXACTA POR CONFIRMAR: el MAEC no la publica. Es el contacto más útil para cerrar trámites locales (perro, aduana, tasas). Pin comprobado en Google Maps («Ciudad de São Tomé (el consulado honorario no figura como objeto)»)."),
    ("Hospital Ayres de Menezes (São Tomé)", "Hospital", 0.3567807, 6.7222851,  # Google Maps: Hospital Ayres de Menezes
     "Hospital principal del país, en la capital. Hemodiálisis desde 2009 y TAC desde junio de 2017. Teléfono +239 222 12 22 (MAEC). Medios muy básicos: para cualquier cosa seria, evacuación a Libreville o Lisboa. Pin comprobado en Google Maps («Hospital Ayres de Menezes»)."),
    ("Último repostaje y último cajero bajando al sur: São João dos Angolares", "Combustible", 0.1333856, 6.6491132,  # Google Maps: São João dos Angolares
     "Pueblo del sureste, sede de la roça São João (hoy hotel y restaurante, y uno de los seis componentes del bien UNESCO 2026). Alma de Viajante avisa de que aquí están los últimos cajeros antes de bajar a Porto Alegre y Praia Jalé, donde la carretera empeora mucho. Pin comprobado en Google Maps («São João dos Angolares»)."),
    ("EMAE — Empresa de Água e Electricidade (São Tomé)", "Agua potable", 0.3341344, 6.7318379,  # Google Maps: EMAE — Direção das Águas
     "Empresa pública del agua y la electricidad: 15 sistemas de abastecimiento en São Tomé y 1 en Príncipe, 7 estaciones de tratamiento y 10 puestos de cloración. Contacto: geral@emae.st, +239 22 44 700. Más de la mitad de la población no tiene acceso a agua potable y se pierde el 40 % del agua tratada: no beber del grifo. Pin comprobado en Google Maps («EMAE — Direção das Águas»)."),
]

DRONE_CALLOUT = ("warn", "Drones: sin norma escrita, pero con prohibiciones fotográficas muy reales",
                 "El archipiélago es uno de los pocos países de África sin regulación de drones publicada: drone-laws.com (act. 21 ene. 2026) recoge que «drone operations are not regulated in Sao Tome and Principe» y remite al Instituto Nacional de Aviação Civil (inac.st) para cualquier consulta. Vacío legal no es permiso. Canadá (1 sep. 2026) advierte de que está PROHIBIDO fotografiar aeropuertos, instalaciones militares y edificios gubernamentales, y en un país de 230.000 habitantes con policía muy visible un dron se nota al instante. Sin autorización escrita del INAC, el decomiso es posible aunque no haya artículo que lo ampare.")

STARLINK_CALLOUT = ("", "Starlink: activo desde diciembre de 2025",
                    "Santo Tomé y Príncipe tiene Starlink operativo desde el 12 de diciembre de 2025, cuando entró como 26.º país africano con servicio activo (Space in Africa, 11 dic. 2025; TechAfrica News, 12 dic. 2025). Para un archipiélago que depende de un único cable submarino es un salto grande: es la primera alternativa real a CST y Unitel. Lo que esas fuentes no publican es el precio del kit ni de la suscripción, ni si el plan Roam está habilitado allí; antes de contar con ello hay que mirar el mapa de starlink.com con una dirección de São Tomé.")

DOG_MATRIX = [
    ("Entrada por el aeropuerto de São Tomé (TMS)", "por confirmar", "Sin requisitos oficiales publicados. Llevar pasaporte UE, certificado veterinario internacional y titulación, y pedir por escrito al consulado honorario qué exige la aduana ANTES de comprar el billete."),
    ("Vuelo Lisboa–São Tomé (cabina o bodega)", "permitido con condiciones", "Normas de TAP o STP Airways: 8 kg en cabina, hasta 45 kg en bodega con jaula IATA, braquicéfalos prohibidos en bodega. Plan B: dejar al perro en España durante la extensión insular."),
    ("Parque Natural do Obô y Reserva de la Biosfera de Príncipe", "no recomendado", "Toda Príncipe es Reserva de la Biosfera desde 2012 y las dos islas desde 2025: un perro suelto en un ecosistema endémico es mala idea. Dejarlo en el alojamiento con una persona del grupo."),
    ("Roças Patrimonio Mundial (Monte Café, Água Izé, São João, Sundy, Belo Monte, Diogo Vaz)", "por confirmar", "Desde julio de 2026 son bien UNESCO y varias funcionan como hotel o restaurante con criterios propios. Preguntar una por una al reservar."),
    ("Travesía interinsular en el Olivia C", "por confirmar", "El barco no publica condiciones para animales. Plan B: el vuelo interinsular o renunciar a Príncipe con el perro."),
    ("Vuelta a la UE desde São Tomé", "permitido con condiciones", "Titulación antirrábica hecha en España y anotada en el pasaporte antes de salir, vacuna en vigor y entrada por un Punto de Entrada de Viajeros español. Sin eso, ~4 meses varados."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Santo Tomé y Príncipe (act. 1 jun. 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Santo%20Tom%C3%A9%20y%20Pr%C3%ADncipe"),
    ("MAEC · Ficha País Santo Tomé y Príncipe (nov. 2025, PDF)", "https://www.exteriores.gob.es/documents/fichaspais/santotome_ficha%20pais.pdf"),
    ("FCDO (Reino Unido) · Foreign travel advice: São Tomé and Príncipe (act. 10 dic. 2025)", "https://www.gov.uk/foreign-travel-advice/sao-tome-and-principe"),
    ("FCDO · São Tomé and Príncipe: Safety and security (dic. 2025)", "https://www.gov.uk/foreign-travel-advice/sao-tome-and-principe/safety-and-security"),
    ("FCDO · São Tomé and Príncipe: Entry requirements (dic. 2025)", "https://www.gov.uk/foreign-travel-advice/sao-tome-and-principe/entry-requirements"),
    ("Gobierno de Canadá · Travel advice and advisories for Sao Tome and Principe (act. 1 sep. 2026)", "https://travel.gc.ca/destinations/sao-tome-and-principe"),
    ("NaTHNaC / TravelHealthPro · Sao Tome and Principe (salud del viajero)", "https://travelhealthpro.org.uk/countries/sao-tome-and-principe"),
    ("Freedom House · Freedom in the World 2025: São Tomé and Príncipe (84/100, «Free»)", "https://freedomhouse.org/country/sao-tome-and-principe/freedom-world/2025"),
    ("Gobierno de Santo Tomé y Príncipe · Portal oficial (contacto y ministerios)", "https://stp.gov.st/ministerios"),
    ("Gobierno de Santo Tomé y Príncipe · Detalle de ministerio (portal oficial)", "https://stp.gov.st/ministerios_detail?id=usz5fq60yyepysg5dz680aja"),
    ("Dirección de Turismo de Santo Tomé y Príncipe · Portal oficial turismo.gov.st", "https://turismo.gov.st/pt"),
    ("Dirección de Turismo de Santo Tomé y Príncipe · Taxa de turismo (25 € São Tomé / 10 € Príncipe)", "https://turismo.gov.st/pt/taxa-de-turismo"),
    ("UNESCO · The Roças of Sao Tome and Principe: Colonial Agricultural System and Forced Migration (inscrito en 2026, 48.ª sesión)", "https://whc.unesco.org/en/list/1750/"),
    ("Africanews · São Tomé and Príncipe's historic plantations added to UNESCO world heritage list (28 jul. 2026)", "https://www.africanews.com/2026/07/28/sao-tome-and-principes-historic-plantations-added-to-unesco-world-heritage-list/"),
    ("Wikipedia · São Tomé and Príncipe (país)", "https://en.wikipedia.org/wiki/S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("Wikipedia · Príncipe (isla; Reserva de la Biosfera 2012, ampliada 2025)", "https://en.wikipedia.org/wiki/Pr%C3%ADncipe"),
    ("Wikipedia · São Tomé International Airport (TMS)", "https://en.wikipedia.org/wiki/S%C3%A3o_Tom%C3%A9_International_Airport"),
    ("Wikipedia · Príncipe Airport (PCP)", "https://en.wikipedia.org/wiki/Pr%C3%ADncipe_Airport"),
    ("Wikipedia · Ana Chaves Bay (puerto de São Tomé, coordenadas y calado)", "https://en.wikipedia.org/wiki/Ana_Chaves_Bay"),
    ("Wikipedia · Hospital Ayres de Menezes", "https://en.wikipedia.org/wiki/Hospital_Ayres_de_Menezes"),
    ("Wikipedia · Visa policy of São Tomé and Príncipe", "https://en.wikipedia.org/wiki/Visa_policy_of_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("Wikipedia · 2026 São Toméan presidential election (Vila Nova reelegido el 19 jul. 2026)", "https://en.wikipedia.org/wiki/2026_S%C3%A3o_Tom%C3%A9an_presidential_election"),
    ("Wikipedia · 2026 in São Tomé and Príncipe (legislativas del 27 sep. 2026; UNESCO 27 jul. 2026)", "https://en.wikipedia.org/wiki/2026_in_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("Carnet de Passages · Sao Tome and Principe (sin organización emisora AIT/FIA en el país)", "https://carnetdepassage.org/country/sao-tome-and-principe/"),
    ("Drone Laws · Drone Laws in Sao Tome and Principe (act. 21 ene. 2026)", "https://drone-laws.com/drone-laws-in-sao-tome-and-principe/"),
    ("EUR-Lex · Reglamento de Ejecución (UE) 2026/636, listas de terceros países (aplicable 22 abr. 2026)", "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32026R0636"),
    ("TAP Air Portugal · Viajar com animais de estimação (cabina, bodega, tarifas, braquicéfalos)", "https://www.flytap.com/pt-at/viajar-com-animais/animais-de-estimacao"),
    ("DGAV (Portugal) · Exportação de animais para países terceiros", "https://www.dgav.pt/comerciointernacional/conteudo/exportacao-para-paises-terceiros/animais/"),
    ("OFESAUTO · Carta Verde (ámbito territorial del sistema)", "https://www.ofesauto.es/carta-verde/"),
    ("TechAfrica News · Starlink Launches in São Tomé and Príncipe (12 dic. 2025)", "https://techafricanews.com/2025/12/12/starlink-launches-in-sao-tome-and-principe-expanding-africa-presence/"),
    ("Space in Africa · Starlink Begins Service in São Tomé and Príncipe (11 dic. 2025)", "https://spaceinafrica.com/2025/12/11/starlink-begins-service-in-sao-tome-and-principe/"),
    ("Things to do in São Tomé · SIM Card & eSIM guide (CST, Unitel, cobertura, 2026)", "https://thingstodoinsaotome.com/connectivity/"),
    ("EMAE · Empresa de Água e Electricidade: produção e distribuição de água", "https://www.emae.st/PT/produtos/agua"),
    ("RTP África · «Mais de metade da população são-tomense não tem acesso a água potável» (4 dic. 2024)", "https://africa.rtp.pt/noticias-africa/mais-de-metade-da-populacao-sao-tomense-nao-tem-acesso-a-agua-potavel/"),
    ("STP Digital · «Preço de combustíveis passa a ser igual em todo o país» (9 dic. 2021)", "https://stpdigital.net/economia/preco-de-combustiveis-passa-a-ser-igual-em-todo-o-pais"),
    ("Energypedia · Fuel Price Data Sao Tome and Principe (serie GIZ)", "https://energypedia.info/wiki/Fuel_Price_Data_Sao_Tome_and_Principe"),
    ("VOA Português · «Quatro anos depois, retomada a ligação marítima entre as ilhas de São Tomé e Príncipe» (barco Olivia C)", "https://www.voaportugues.com/a/6997941.html"),
    ("Soluções Logísticas · Carga para São Tomé e Príncipe (flete marítimo, plazos y despacho)", "https://www.solucoeslogisticas.pt/servicos/carga-sao-tome"),
    ("Bradt Guides, Kathleen Becker · «A world of roças: historic plantations on São Tomé & Príncipe» (7 may. 2021)", "https://www.bradtguides.com/a-world-of-rocas-historic-plantations-on-sao-tome-principe/"),
    ("Viagem a São Tomé · «Principais Roças de São Tomé e Príncipe»", "https://viagemasaotome.com/principais-rocas-de-sao-tome-e-principe/"),
    ("Alma de Viajante · «Roteiro em São Tomé e Príncipe» (abr. 2024, act. 15 sep. 2026)", "https://www.almadeviajante.com/roteiro-sao-tome-principe/"),
    ("Ir em Viagem · «São Tomé e Príncipe: um guia de viagem» (3 nov. 2025)", "https://iremviagem.com/2025/11/03/sao-tome-e-principe-um-guia-de-viagem/"),
    ("Traveltomtom · «Country 123: Sao Tome & Principe — 11 Days Stuck in Paradise»", "https://www.traveltomtom.net/visit-every-country-in-the-world/sao-tome-principe-travel-blog"),
    ("Chris Travel Blog · «A São Tomé itinerary to all the well kept secrets of the island» (abr. 2018)", "https://www.christravelblog.com/sao-tome-principe-a-sao-tome-itinerary-to-all-the-well-kept-secrets-of-the-island/"),
    ("Sven's Travel Venues · «Sao Tome – Is a 4x4 car necessary?» (mar. 2020)", "https://www.travelsvenue.com/2020/03/sao-tome-is-4wd-car-necessary.html"),
    ("The Chocolate Islands · Rent a Car in São Tomé (tarifas 2026)", "https://www.thechocolateislands.com/sao-tome-car-hire"),
    ("Museo Nacional / Forte de São Sebastião (Wikipedia)", "https://en.wikipedia.org/wiki/S%C3%A3o_Sebasti%C3%A3o_Museum"),
    ("Sé Catedral de Nossa Senhora da Graça (Wikipedia)", "https://en.wikipedia.org/wiki/Our_Lady_of_Grace_Cathedral,_S%C3%A3o_Tom%C3%A9"),
    ("Ciudad de São Tomé (Wikipedia)", "https://en.wikipedia.org/wiki/S%C3%A3o_Tom%C3%A9"),
    ("Agostinho Neto / Roça Rio do Ouro (Wikipedia)", "https://en.wikipedia.org/wiki/Agostinho_Neto,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("Parque Natural Obô de São Tomé (Wikipedia)", "https://en.wikipedia.org/wiki/Parque_Natural_Ob%C3%B4_de_S%C3%A3o_Tom%C3%A9"),
    ("Trilha de Lagoa Amélia desde Bom Sucesso (Mucumbli Explore)", "https://mucumbliexplore.com/trekking-2/lagoa-amelia/"),
    ("Recorridos del Parque Nacional do Obô (São Tomé Trekking)", "https://saotome-principe-trekking.com/des-parcours/parc-national-de-lobo"),
    ("Pico Cão Grande (Wikipedia)", "https://en.wikipedia.org/wiki/Pico_C%C3%A3o_Grande"),
    ("Pico de São Tomé (Wikipedia)", "https://en.wikipedia.org/wiki/Pico_de_S%C3%A3o_Tom%C3%A9"),
    ("Monte Café (Wikipedia)", "https://en.wikipedia.org/wiki/Monte_Caf%C3%A9,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("Roça Bombaim y Roça Monte Café (Got2Globe)", "https://www.got2globe.com/en/Editorial/roca-bombay-monte-cafe-sao-tome/"),
    ("Lagoa Azul (Wikipedia)", "https://en.wikipedia.org/wiki/Lagoa_Azul"),
    ("Praia dos Tamarindos (SaoTomeExpert)", "https://www.saotomeexpert.pt/en/the-beaches/praia-dos-tamarindos/"),
    ("Las playas más bonitas de Santo Tomé y Príncipe (Alma de Viajante)", "https://www.almadeviajante.com/praias-sao-tome-e-principe/"),
    ("Lista de playas de Santo Tomé y Príncipe (Wikipedia)", "https://en.wikipedia.org/wiki/List_of_beaches_of_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("São João dos Angolares (Wikipedia)", "https://en.wikipedia.org/wiki/S%C3%A3o_Jo%C3%A3o_dos_Angolares"),
    ("Programa Tatô · São Tomé", "https://www.programatato.org/en/sao-tome"),
    ("Praia Jalé (Visit São Tomé)", "http://www.visitsaotome.com/beach/praia-jale.html"),
    ("Praia Inhame (Wikipedia)", "https://en.wikipedia.org/wiki/Praia_Inhame"),
    ("Ilhéu das Rolas (Wikipedia)", "https://en.wikipedia.org/wiki/Ilh%C3%A9u_das_Rolas"),
    ("Porto Alegre (Wikipedia)", "https://en.wikipedia.org/wiki/Porto_Alegre,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("Bombaim (Wikipedia)", "https://en.wikipedia.org/wiki/Bombaim"),
    ("Monte Forte (Wikipedia)", "https://en.wikipedia.org/wiki/Monte_Forte,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("Neves (Wikipedia)", "https://en.wikipedia.org/wiki/Neves,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("Diogo Vaz (Wikipedia)", "https://en.wikipedia.org/wiki/Diogo_Vaz,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("Água Izé (Wikipedia)", "https://en.wikipedia.org/wiki/%C3%81gua_Iz%C3%A9"),
    ("Boca do Inferno, Cantagalo (Mapcarta)", "https://mapcarta.com/N2848219674"),
    ("Santo António (Wikipedia)", "https://en.wikipedia.org/wiki/Santo_Ant%C3%B3nio"),
    ("Región Autónoma de Príncipe (Wikipedia)", "https://en.wikipedia.org/wiki/Autonomous_Region_of_Pr%C3%ADncipe"),
    ("Cómo moverse por Príncipe (SaoTomeExpert)", "https://www.saotomeexpert.pt/en/sao-tome-principe-island-getting-around/"),
    ("Experimento de Eddington (Wikipedia)", "https://en.wikipedia.org/wiki/Eddington_experiment"),
    ("Cómo llegar a Roça Sundy (Príncipe Collection)", "https://www.principecollection.com/en/hotels/roca-sundy/getting-to-roca-sundy"),
    ("Belo Monte (Wikipedia)", "https://en.wikipedia.org/wiki/Belo_Monte,_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("Ilhéu Bom Bom (Wikipedia)", "https://en.wikipedia.org/wiki/Ilh%C3%A9u_Bom_Bom"),
    ("Parque Natural Obô do Príncipe (Wikipedia)", "https://en.wikipedia.org/wiki/Parque_Natural_Ob%C3%B4_do_Pr%C3%ADncipe"),
    ("Reserva de la Biosfera de la Isla de Príncipe (Wikipedia)", "https://en.wikipedia.org/wiki/Island_of_Pr%C3%ADncipe_Biosphere_Reserve"),
    ("26 nuevas reservas de la biosfera, 2025 (UNESCO)", "https://www.unesco.org/en/articles/26-new-biosphere-reserves-unescos-continues-unprecedented-expansion-its-global-network"),
]

# Bucle de la isla de São Tomé: capital → norte → oeste → interior → costa este → sur profundo → Rolas
CORRIDOR = [
    (0.34603, 6.73945),
    (0.36647, 6.64377),
    (0.40612, 6.60888),
    (0.40887, 6.64611),
    (0.36647, 6.64377),
    (0.35602, 6.54898),
    (0.28829, 6.54632),
    (0.30049, 6.63909),
    (0.24568, 6.63241),
    (0.21345, 6.72627),
    (0.13909, 6.64765),
    (0.11801, 6.56599),
    (0.05454, 6.51506),
    (-0.00695, 6.52231),
]

# Bucle de Príncipe (paréntesis aéreo, sin vehículos propios): Santo António → Sundy → Bom Bom → Belo Monte → Praia Banana
CORRIDOR_ALT = [
    (1.63676, 7.41786),
    (1.66971, 7.38374),
    (1.69013, 7.44186),
    (1.63676, 7.41786),
]

HISTORIA_RESUMEN = "Santo Tomé y Príncipe es un archipiélago ecuatorial del golfo de Guinea que Portugal encontró deshabitado hacia 1470 y convirtió en laboratorio de la plantación esclavista: primero azúcar y después cacao, hasta ser el primer productor mundial a comienzos del siglo XX. De aquella economía quedan las roças, las haciendas coloniales que la UNESCO inscribió como Patrimonio Mundial en julio de 2026 y que ordenan hoy la visita. Independiente desde el 12 de julio de 1975 y democrático desde 1991, es uno de los países más libres y seguros de África: Freedom House lo clasifica «Free» con 84 puntos sobre 100 y el Ministerio de Asuntos Exteriores español no desaconseja viajar. Vive del cacao, de un turismo incipiente y de la ayuda exterior."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>A diferencia de casi toda África, Santo Tomé y Príncipe no tuvo reinos ni pueblos anteriores a la colonización. Las fuentes consultadas coinciden en que las islas estaban <strong>deshabitadas</strong> cuando los navegantes portugueses las avistaron en el último tercio del siglo XV: Britannica sitúa el hallazgo «alrededor de 1470» y la Wikipedia en español atribuye la llegada a João de Santarém y Pedro Escobar entre 1469 y 1472. No hay, por tanto, sustrato indígena que reconstruir ni memoria precolonial que visitar.</p><p>Eso convierte al archipiélago en un caso singular dentro del continente. Todo lo que hoy es santotomense —la lengua, la cocina, la música, los apellidos, el propio paisaje— nació ya dentro del sistema colonial, por mezcla forzada de colonos portugueses y de africanos esclavizados traídos del continente. El país se compone de dos islas principales, Santo Tomé y Príncipe, más varios islotes rocosos, y suma 1.001 kilómetros cuadrados, según la ficha del Ministerio de Asuntos Exteriores español; es el Estado más pequeño de cuantos tienen el portugués como lengua oficial. La isla mayor mide unos cincuenta kilómetros de largo por treinta y dos de ancho y culmina en el pico de São Tomé, de algo más de dos mil metros. Quien viaja aquí no visita un África anterior a Europa, sino el lugar donde se ensayó la plantación atlántica.</p>"),
    ("Colonización",
     "<p>El poblamiento efectivo arrancó en 1493, cuando el rey Juan II entregó la isla a Álvaro Caminha, que la colonizó con desterrados, convictos y niños judíos sefardíes arrancados a sus familias, junto a africanos esclavizados. Con los ingenios instalados desde 1515, Santo Tomé fue a mediados del siglo XVI el principal exportador de azúcar de África y, brevemente, el mayor del mundo, hasta que la competencia brasileña hundió el negocio. Las islas quedaron entonces como plataforma del tráfico de esclavos hacia América, que Wikipedia data desde 1525.</p><p>En julio de 1595 un esclavo llamado <strong>Amador</strong> encabezó una rebelión que destruyó sesenta de los ochenta y cinco ingenios antes de ser sofocada; hoy se recuerda como acto fundacional de la resistencia nacional. El café y el cacao llegaron en el siglo XIX y lo cambiaron todo: hacia 1908 el archipiélago era el primer productor mundial de cacao y lo siguió siendo, según Britannica, durante las dos primeras décadas del siglo. La esclavitud se abolió formalmente en 1875, pero fue sustituida por el trabajo «contratado» de <em>serviçais</em> angoleños, caboverdianos y mozambiqueños en condiciones casi idénticas. De ese sistema nacieron las <strong>roças</strong>, haciendas autosuficientes con hospital, capilla, secaderos y barracones. La represión culminó en la masacre de Batepá, en 1953, con varios cientos de muertos, que encendió la conciencia anticolonial.</p>"),
    ("Independencia y construcción del Estado",
     "<p>El Movimiento de Liberación de Santo Tomé y Príncipe (MLSTP) se organizó desde el exilio —Britannica lo data en 1960 y la Wikipedia en español lo remonta a los años cincuenta, con base en Gabón— y negoció el traspaso de poderes tras la Revolución de los Claveles portuguesa de abril de 1974. La independencia se proclamó el <strong>12 de julio de 1975</strong>, sin guerra de liberación previa. Manuel Pinto da Costa, secretario general del movimiento, fue el primer presidente, y Miguel Trovoada ocupó la jefatura del Gobierno.</p><p>Siguieron quince años de partido único de orientación marxista, tal como lo resume la ficha del MAEC. Las roças fueron nacionalizadas y la producción de cacao se desplomó; la marcha de los técnicos portugueses, la caída de los precios internacionales y el tamaño diminuto del mercado interno dejaron al país dependiendo de la ayuda exterior, rasgo que no ha desaparecido.</p><p>El giro llegó con el final de la Guerra Fría. Una nueva Constitución, aprobada en referéndum y que el MAEC data en 1990, consagró el multipartidismo y un régimen de libertades, y en 1991 se celebraron las primeras elecciones libres, descritas por las fuentes como pacíficas, libres y transparentes. Las ganó Miguel Trovoada, regresado del exilio como candidato independiente. Desde entonces ha habido alternancia real entre partidos rivales, algo poco frecuente en la región.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>Fradique de Menezes ganó la presidencia en 2001 y repitió en 2006. En julio de 2003 un golpe militar lo apartó brevemente del poder, pero la mediación internacional, incluida la estadounidense, lo revirtió sin derramamiento de sangre; en febrero de 2009 fracasó otra intentona. Evaristo Carvalho presidió desde 2016 y Carlos Vila Nova, entonces en las filas de la ADI, venció en 2021 y tomó posesión en octubre de ese año. Las legislativas del 25 de septiembre de 2022 dieron a la ADI mayoría absoluta, con 30 de los 55 escaños, frente a los 18 del histórico MLSTP-PSD.</p><p>Dos meses después, entre el 24 y el 25 de noviembre de 2022, cuatro hombres asaltaron el cuartel general de las Fuerzas Armadas en la capital. Murieron cuatro personas. El cabecilla, Arlécio Costa, fue condenado a quince años de prisión, pena confirmada en agosto de 2024 según Freedom House, mientras que el entonces presidente de la Asamblea Nacional, Delfim Neves, resultó exonerado. Siete militares seguían pendientes de juicio castrense por presuntas torturas y muertes de detenidos durante aquellos hechos.</p><p>La inestabilidad ha sido de gobiernos, no de régimen. Tras la dimisión de Ilza Amado Vaz, Américo d'Oliveira dos Ramos fue investido primer ministro el 12 de enero de 2025. La inflación había tocado el 25 % en enero de 2023 y aún rondaba el 11 % en 2025.</p>"),
    ("Política y gobierno en 2026",
     "<p>A fecha de septiembre de 2026 el jefe del Estado es <strong>Carlos Manuel Vila Nova</strong>, presidente desde octubre de 2021 y reelegido en primera vuelta el 19 de julio de 2026 con el 55,88 % frente al 41,46 % de Nito Abreu. El jefe de Gobierno es <strong>Américo d'Oliveira dos Ramos</strong>, investido el 12 de enero de 2025 según el MAEC (noviembre de 2025), sin relevo posterior conocido. Las legislativas estaban convocadas para el <strong>27 de septiembre de 2026</strong>: su resultado no puede darse por sabido.</p><p>El régimen es una república unitaria semipresidencialista regida por la Constitución de 1990. Freedom House, en su informe de 2025, lo clasifica como <strong>«Free»</strong> con 84 puntos sobre 100 —35 de 40 en derechos políticos y 49 de 60 en libertades civiles— y subraya sus elecciones competitivas y sus varios traspasos de poder entre partidos rivales. Es, en la práctica, una democracia plena, lastrada por instituciones frágiles y corrupción: en 2024 el Tribunal de Cuentas denunció que casi ningún organismo público rindió cuentas. La prensa es libre: 3 puntos sobre 4 en pluralidad de medios. No hay conflicto armado ni amenaza yihadista y el MAEC <strong>no desaconseja viajar</strong>: recomienda «viajar con precaución» (1 de junio de 2026). Con España las relaciones son cordiales pero escasas y sin embajada residente —la competente es la de Gabón—; la UE es gran donante.</p>"),
    ("Economía y recursos",
     "<p>La economía es diminuta y abierta. El Banco Mundial cifra el PIB de 2025 en unos 981 millones de dólares para algo más de 240.000 habitantes, con un PIB per cápita cercano a los 4.100 dólares; el MAEC lo sitúa en 6.230 dólares en paridad de poder adquisitivo (2024). El crecimiento fue del 1 % en 2025 y la inflación, del 11 %. La moneda es la <strong>nueva dobra</strong> (STN), anclada al euro desde enero de 2018 a razón de 24,5 dobras por euro.</p><p>El <strong>cacao</strong> sigue siendo la exportación insignia —el 44 % de las ventas exteriores en 2022—, seguido del aceite de palma y el café. Aun así, en 2023 las exportaciones apenas alcanzaron 57 millones de dólares frente a 186 millones de importaciones, y el desequilibrio se cubre con ayuda exterior. Portugal, Angola y Gabón son los principales proveedores; Pakistán y Alemania, los grandes compradores de cacao.</p><p>El <strong>turismo</strong> es la apuesta de futuro, todavía menor: unos 41.000 visitantes en 2024, más de la mitad portugueses. La pesca se rige por un acuerdo con la Unión Europea cuyo protocolo 2025-2029 aporta 825.000 euros anuales. El petróleo, prometido durante dos décadas en la zona de desarrollo conjunto pactada con Nigeria en el Tratado de Abuja de 2001, nunca ha llegado a producirse. China ha financiado la modernización del aeropuerto internacional por unos cien millones de dólares.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Viven unos 235.000 habitantes (MAEC) o 240.000 (Banco Mundial, 2025), casi todos en Santo Tomé: Príncipe apenas reúne ocho mil. La lengua oficial es el <strong>portugués</strong>, que entiende casi todo el mundo y basta para moverse por carretera; conviven con él el forro, el angolar y el principense o lung'ie, más el caboverdiano. La población mezcla lusoafricanos, forros (descendientes de esclavos liberados), angolares y tongas. El censo de 2020 da un 81 % de cristianos —71,9 % católicos— y un 13 % sin religión; el MAEC, un 73 % de católicos y un 23 % de otros cristianos.</p><p>La cultura es criolla: los ritmos <em>ússua</em> y <em>socopé</em> en Santo Tomé, el <em>dêxa</em> en Príncipe y el <strong>tchiloli</strong>, teatro cantado y danzado de raíz portuguesa. En la mesa mandan el pescado, las judías, el maíz y la banana cocida. El patrimonio UNESCO es reciente: seis roças —Monte Café, Água Izé, Diogo Vaz, São João, Sundy y Belo Monte— son Patrimonio Mundial desde julio de 2026, y Príncipe, Reserva de la Biosfera desde 2012.</p><p>Tres reglas prácticas. Fuera de la playa conviene vestir con discreción, sobre todo en iglesias y oficinas. Pida permiso antes de fotografiar y evite cuarteles, policía y aeropuerto. El alcohol es legal, y el ramadán, que en 2027 empieza en torno al 8 de febrero, apenas se nota en un país de mayoría cristiana.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Santo Tomé y Príncipe (MAEC España · PDF · noviembre 2025)", "https://www.exteriores.gob.es/documents/fichaspais/santotome_ficha%20pais.pdf"),
    ("Recomendaciones de viaje: Santo Tomé y Príncipe (MAEC España · actualizado 1 junio 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Santo+Tom%C3%A9+y+Pr%C3%ADncipe"),
    ("Freedom in the World 2025: São Tomé and Príncipe (Freedom House · 2025)", "https://freedomhouse.org/country/sao-tome-and-principe/freedom-world/2025"),
    ("Sao Tome and Principe — History (Encyclopædia Britannica · consultado septiembre 2026)", "https://www.britannica.com/place/Sao-Tome-and-Principe/History"),
    ("Sao Tome and Principe (Encyclopædia Britannica · consultado septiembre 2026)", "https://www.britannica.com/place/Sao-Tome-and-Principe"),
    ("Santo Tomé y Príncipe (Wikipedia en español · consultado septiembre 2026)", "https://es.wikipedia.org/wiki/Santo_Tom%C3%A9_y_Pr%C3%ADncipe"),
    ("São Tomé and Príncipe (Wikipedia en inglés · consultado septiembre 2026)", "https://en.wikipedia.org/wiki/S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe"),
    ("2026 São Toméan presidential election (Wikipedia en inglés · consultado septiembre 2026)", "https://en.wikipedia.org/wiki/2026_S%C3%A3o_Tom%C3%A9an_presidential_election"),
    ("2026 São Toméan parliamentary election (Wikipedia en inglés · consultado septiembre 2026)", "https://en.wikipedia.org/wiki/2026_S%C3%A3o_Tom%C3%A9an_parliamentary_election"),
    ("2022 São Tomé and Príncipe coup attempt (Wikipedia en inglés · consultado septiembre 2026)", "https://en.wikipedia.org/wiki/2022_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe_coup_attempt"),
    ("Américo Ramos (Wikipedia en inglés · consultado septiembre 2026)", "https://en.wikipedia.org/wiki/Am%C3%A9rico_Ramos"),
    ("Sao Tome and Principe — States Parties (UNESCO Centro del Patrimonio Mundial · consultado septiembre 2026)", "https://whc.unesco.org/en/statesparties/st"),
    ("Island of Príncipe Biosphere Reserve (UNESCO · Programa MAB · consultado septiembre 2026)", "https://www.unesco.org/en/mab/island-principe"),
    ("São Tomé and Príncipe achieves full Biosphere Reserve status (Macao News · 29 septiembre 2025)", "https://macaonews.org/news/lusofonia/sao-tome-principe-biosphere-reserve/"),
    ("São Tomé Roças Join the UNESCO World Heritage List (Rio Times · julio 2026)", "https://www.riotimesonline.com/sao-tome-rocas-world-heritage-2026/"),
    ("Sao Tome and Principe — Datos (Banco Mundial · Open Data · consultado septiembre 2026)", "https://data.worldbank.org/country/sao-tome-and-principe"),
]

SPEC = dict(
    slug="santo-tome", name="Santo Tomé y Príncipe", revision="18 sep 2026",
    sub="FUERA DE RUTA — país insular, sin ferry que admita vehículos · roças del cacao (Patrimonio Mundial desde 2026), Príncipe Reserva de la Biosfera y el país más seguro y libre de África central",
    chips=[
        ("ESTATUS", "FUERA DE RUTA 2027 por insularidad, NO por riesgo. Archipiélago en el golfo de Guinea a ~250 km de Gabón: sin…"),
        ("CÓMO LLEGAR", "SOLO EN AVIÓN. São Tomé (TMS): TAP (Lisboa, Accra), STP Airways (Lisboa), TAAG (Luanda), ASKY (Libreville…"),
        ("VISADO", "Españoles: SIN VISADO hasta 15 DÍAS con pasaporte de validez ≥6 meses (MAEC, 1 jun. 2026)…"),
        ("VEHÍCULO", "NO APLICA: no se puede llegar rodando. Vehículo propio solo en contenedor…"),
        ("SEGURIDAD", "Freedom House 84/100 «Free» · sin zonas vetadas"),
        ("SEGURO", "Carta Verde NO vale · repatriación obligatoria"),
        ("SALUD", "Malaria alta todo el año · amarilla si hay escala"),
        ("DRONES", "Sin norma publicada · preguntar al INAC antes"),
        ("STARLINK", "Activo desde el 12 de diciembre de 2025"),
        ("4x4", "Solo para el sur, Praia Jalé y el Obô"),
        ("A PIE", "Capital y roças sin problema · de noche, no"),
        ("PERRO", "Entrada: requisitos nacionales NO publicados en ninguna web oficial accesible (por confirmar)…"),
        ("MONEDA", "Dobra (STN) con PARIDAD FIJA 1 € = 24,5 STN desde enero de 2018 (MAEC…"),
        ("VENTANA", "Ecuatorial húmedo. Gravana seca de junio a septiembre y gravanita en enero–febrero…"),
    ],
    center=[0.84, 6.98], zoom=7,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle de la isla de São Tomé: capital → norte → oeste → interior → costa este → sur profundo → Rolas",
    corridor_alt_label="Bucle de Príncipe (paréntesis aéreo, sin vehículos propios): Santo António → Sundy → Bom Bom → Belo Monte → Praia Banana",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Pico_C%C3%A3o_Grande.jpg?width=1200",
    hero_credit="Pico Cão Grande · Philippe Bourachot · CC BY-SA 3.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Santo Tomé y Príncipe queda FUERA de la ruta 2027 por geografía, no por seguridad: es un archipiélago a unos 250 km de Gabón, sin conexión terrestre y sin ferry regular que admita vehículos. Se llega solo en avión —Lisboa con TAP o STP Airways, Accra, Libreville con ASKY o Afrijet, Luanda con TAAG— a São Tomé (TMS), y a Príncipe (PCP) en avioneta o en el barco Olivia C. Nada de eso sirve para el Grenadier ni para la Delica: meter un 4x4 propio exigiría contenedor desde Lisboa, con 15–30 días de travesía y 500–3.000 € de flete (Soluções Logísticas, 2026), más despacho en el puerto de Ana Chaves —muelle de 200 m y 3 m de calado— y una admisión temporal que ninguna fuente oficial documenta. Para dos coches y dos semanas de isla, no se justifica. Cómo se haría aparte: un viaje propio de 10–14 días volando desde Lisboa (6 h 30) y alquilando allí un 4x4 por 25–135 €/día (Traveltomtom; The Chocolate Islands, 2026). Hay un argumento nuevo a favor: en julio de 2026 la UNESCO inscribió las roças como primer Patrimonio Mundial del país. Habría que decidir si se hace como extensión o como viaje aparte, si el perro va —el vuelo en bodega y la titulación antirrábica son el punto crítico— y en qué estación, porque las lluvias de marzo a mayo destrozan las pistas del sur.",
    facts=[
        ("Estatus", "FUERA DE RUTA 2027 por insularidad, NO por riesgo. Archipiélago en el golfo de Guinea a ~250 km de Gabón: sin frontera terrestre y sin ferry que admita vehículos."),
        ("Cómo llegar", "SOLO EN AVIÓN. São Tomé (TMS): TAP (Lisboa, Accra), STP Airways (Lisboa), TAAG (Luanda), ASKY (Libreville, Lomé), Afrijet (Libreville). A Príncipe (PCP), avioneta de 20–70 plazas o el barco Olivia C."),
        ("Visado", "Españoles: SIN VISADO hasta 15 DÍAS con pasaporte de validez ≥6 meses (MAEC, 1 jun. 2026). Más de 15 días, eVisa previa (e-VisaST, ~7 días hábiles)."),
        ("Vehículo / aduana", "NO APLICA: no se puede llegar rodando. Vehículo propio solo en contenedor. Conducción POR LA DERECHA y PERMISO INTERNACIONAL OBLIGATORIO (MAEC, FCDO, Canadá). Admisión temporal: sin fuente oficial, POR CONFIRMAR."),
        ("Seguro", "La Carta Verde NO cubre el país (solo EEE más Marruecos, Túnez, Turquía, Ucrania y otros; OFESAUTO). No pertenece a CEDEAO ni a la CEMAC, así que ni Carte Brune ni Carte Rose. Con coche alquilado, seguro a todo riesgo incluido en la tarifa."),
        ("Moneda", "Dobra (STN) con PARIDAD FIJA 1 € = 24,5 STN desde enero de 2018 (MAEC; Ficha País, nov. 2025). Euros aceptados casi en todas partes; los cajeros NO admiten tarjetas extranjeras (Canadá, sep. 2026). Efectivo en euros imprescindible."),
        ("Perro", "Entrada: requisitos nacionales NO publicados en ninguna web oficial accesible (por confirmar). Vuelta a la UE: el país NO figura en el Reg. de Ejecución (UE) 2026/636 → TITULACIÓN ANTIRRÁBICA ≥0,5 UI/ml, mejor hecha en España y anotada en el pasaporte antes de salir."),
        ("Drones", "SIN REGULACIÓN publicada: «Drone operations are not regulated in Sao Tome and Principe» (drone-laws.com, 21 ene. 2026). Autoridad: INAC (inac.st). Prohibido fotografiar aeropuertos, instalaciones militares y edificios oficiales (Canadá)."),
        ("Starlink", "DISPONIBLE desde el 12 de diciembre de 2025: 26.º país africano con servicio activo (TechAfrica News; Space in Africa). Móvil: CST y Unitel STP, 4G en casi toda São Tomé, 10–25 Mbps."),
        ("Seguridad", "EL PAÍS MÁS SEGURO Y LIBRE DE LA REGIÓN: Freedom House le da 84/100 y estatus «Free» (2025); el MAEC no desaconseja ninguna zona y Canadá aplica «precauciones normales». Hurtos en playas y mercados; nada que ver con sus vecinos."),
        ("Clima", "Ecuatorial húmedo. Gravana seca de junio a septiembre y gravanita en enero–febrero; lluvias fuertes de marzo a mayo y de octubre a noviembre, con desprendimientos que cortan carreteras (FCDO, dic. 2025; iremviagem, nov. 2025)."),
        ("Sanidad", "MALARIA DE RIESGO ALTO EN TODO EL PAÍS todo el año, con profilaxis recomendada (MAEC; TravelHealthPro). Medios «muy básicos»: seguro con repatriación imprescindible. Hospital Ayres de Menezes (São Tomé), +239 222 12 22."),
    ],
    alerts=[
        "No hay manera de llegar con los vehículos: ninguna línea regular admite coches, ni desde el continente ni desde Europa. El único camino para un 4x4 propio es el contenedor, con 15–30 días de travesía y 500–3.000 € de flete (Soluções Logísticas, 2026).",
        "EXENCIÓN DE VISADO DE SOLO 15 DÍAS para españoles (MAEC, 1 jun. 2026; FCDO, dic. 2025; Canadá, sep. 2026): una de las más cortas de África. Pasar de ahí exige eVisa previa.",
        "TASA DE TURISMO OFICIAL: 25 € por persona en São Tomé y 10 € en Príncipe, pago único en el aeropuerto, exentos los menores de 12 años (portal oficial turismo.gov.st). El FCDO habla de 20 € y el MAEC de 75.000 dobras por noche: llevar 30 € sueltos por cabeza y no discutir.",
        "MALARIA DE RIESGO ALTO en todo el territorio (MAEC; TravelHealthPro: «high risk», quimioprofilaxis con atovacuona/proguanil, doxiciclina o mefloquina). Empezar quince días antes y seguir quince días después del viaje.",
        "Sanidad muy limitada: el MAEC exige en la práctica seguro con REPATRIACIÓN; Canadá avisa de que hay que pagar en efectivo por adelantado, de que apenas hay ambulancias y de que la evacuación médica es carísima. La salida real es Libreville o Lisboa.",
        "Los cajeros NO admiten tarjetas extranjeras y solo los hoteles internacionales aceptan tarjeta (Canadá, sep. 2026; iremviagem, nov. 2025: «levantar dinheiro está fora de questão»). Entrar con euros en efectivo.",
        "El enlace interinsular es frágil: el MAEC avisa de que las aerolíneas «interrumpen temporalmente los vuelos» São Tomé–Príncipe, y los blogs recomiendan poner Príncipe al principio del viaje por las cancelaciones (Alma de Viajante, 2024/2026). El barco Olivia C reanudó en 2023 una ruta parada cuatro años tras el accidente del Anfitrite.",
        "Las ROÇAS son Patrimonio Mundial de la UNESCO desde julio de 2026 —primer bien inscrito del país, seis plantaciones: Monte Café, Água Izé, Diogo Vaz, São João, Sundy y Belo Monte— y toda Príncipe es Reserva de la Biosfera desde 2012, ampliada a las dos islas en 2025: esperar más control y más tasas.",
        "MÁS DE LA MITAD DE LA POBLACIÓN no tiene acceso a agua potable y el 40 % del agua tratada se pierde en tuberías coloniales (EMAE, vía RTP África, 4 dic. 2024). Para beber, embotellada o filtrada, siempre.",
        "El perro no puede volver a la UE por la vía simple: el país NO está en las listas del Reg. de Ejecución (UE) 2026/636, aplicable desde el 22 de abril de 2026.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Llegada y capital", "Aeropuerto de São Tomé → ciudad de São Tomé (catedral, fuerte de São Sebastião, mercado)", "~10 km · 1 día"),
        ("2 · Norte y roça grande", "São Tomé → Guadalupe → Lagoa Azul → Praia dos Tamarindos → Roça Agostinho Neto → São Tomé", "~90 km · 1 día"),
        ("3 · Oeste y barlovento", "São Tomé → Neves (Rosema) → Monte Forte → Diogo Vaz → Santa Catarina → Neves", "~110 km · 1 día"),
        ("4 · Tierras altas del cacao", "Neves → São Tomé → Trindade → Monte Café (UNESCO) → Bom Sucesso", "~75 km · 1 día"),
        ("5 · Obô a pie", "Bom Sucesso: Lagoa Amélia y jardín botánico; noche en Monte Café o Bombaim", "~15 km · 1 día"),
        ("6 · Roça del interior", "Monte Café → Roça Bombaim → Trindade → São Tomé", "~50 km · 1 día"),
        ("7 · Pico de São Tomé (opcional)", "Bom Sucesso → Pico Mesa → Pico de São Tomé → Bom Sucesso, con vivac", "~25 km a pie · 2 días"),
        ("8 · Costa este", "São Tomé → Santana → Água Izé (UNESCO) → Boca do Inferno → Ribeira Afonso → São João dos Angolares", "~65 km · 1 día"),
        ("9 · Sur y aguja volcánica", "São João dos Angolares → Pico Cão Grande → Praia Piscina → Praia Inhame → Praia Jalé", "~45 km · 1 día"),
        ("10 · Tortugas y Ecuador", "Praia Jalé → Porto Alegre → Ponta Baleia → Ilhéu das Rolas (barca, vehículos en tierra)", "~15 km + barca · 1 día"),
        ("11 · Regreso al norte", "Ilhéu das Rolas → Porto Alegre → São João dos Angolares → São Tomé", "~90 km · 1 día"),
        ("12 · Vuelo a Príncipe", "São Tomé (aeropuerto) → Príncipe (aeropuerto) → Santo António", "vuelo 30–40 min + 3 km · 1 día"),
        ("13 · Sundy y el norte de Príncipe", "Santo António → Roça Sundy (UNESCO) → Sundy Praia → Ilhéu Bom Bom → Santo António", "~25 km · 1 día"),
        ("14 · Belo Monte, Praia Banana y Obô", "Santo António → Belo Monte (UNESCO) → Praia Banana → trilha del Obô do Príncipe → vuelo a São Tomé", "~30 km · 2 días"),
    ],
    offroad=[
        "La red viaria es ridícula para lo acostumbrado en el continente: una carretera principal que casi circunvala la isla de São Tomé, asfaltada y en general practicable, con el aviso canadiense recordando que fuera de la capital está «pavimentada y en condición aceptable, pero peligrosa» por falta de arcén e iluminación, ganado suelto y peatones, y que puede quedar impracticable en la estación de lluvias, de septiembre a mayo (travel.gc.ca, 1 de septiembre de 2026).",
        "El tramo que de verdad exige 4x4 es el sur: un blog de overlander que recorrió la isla describe el firme como aceptable en general pero «incredibly shit» a la altura del Pico Cão Grande y peor todavía hacia Praia Jalé; el mismo autor sostiene que con un turismo alto se puede, de modo que para dos 4x4 pesados el problema no es la tracción sino los socavones y los bajos.",
        "Un relato portugués de la misma ruta es más tajante: hasta São João dos Angolares «a estrada está em boas condições», y de ahí hacia el sur «é de fugir: os buracos têm muita pouca estrada», recomendando jeep. Ese es el kilometraje que hay que planificar despacio, con dos vehículos y sin prisa.",
        "El eje interior Trindade–Monte Café–Bom Sucesso–Bombaim es la única pista de montaña real de la isla: asfalto hasta Monte Café y tierra después, con Bombaim a 8 km al suroeste de Trindade y 6 km al sur de Monte Café, en el borde del Parque Natural Obô. Se embarra en cuanto llueve y no hay apenas sitio para dar la vuelta.",
        "La costa oeste termina en Santa Catarina (0.2703, 6.4730): más allá no hay carretera y el suroeste de la isla es inaccesible en vehículo. Cualquier traza que aparezca en mapas hacia Ponta Figo o el Pico es sendero de montaña, no pista rodada.",
        "En Príncipe hay unos 18 km de carretera en total, con tramos recién asfaltados y tramos de tierra muy erosionados; al sur de Ribeira Fria «no hay carreteras en absoluto, solo senderos». Se recomienda 4x4 y se sugiere un Suzuki Jimny por lo estrecho del firme: los dos vehículos de la expedición son demasiado grandes para esa isla aunque pudieran llegar.",
        "No existen agencias formales de alquiler en Príncipe: se pacta con guías o alojamientos por unos 60 €/día con combustible. En São Tomé sí hay alquiler informal desde unos 25 €/día. Ningún vehículo propio puede llegar al archipiélago: no hay transbordador de vehículos ni entre islas ni con el continente.",
        "Zonas vetadas: el interior del Parque Natural Obô, en ambas islas, solo se recorre a pie y con guía acreditado; en Príncipe el guía es obligatorio por norma del parque. El Pico Cão Grande solo se asciende con escalada técnica. Ninguna autoridad consultada —MAEC ni Canadá— señala región alguna del país como zona de riesgo.",
    ],
    senderismo=[
        "Lagoa Amélia desde Bom Sucesso: la entrada estándar al Obô, 3 horas, +450 / -450 m hasta el cráter de 1.475 m, dificultad media, guía obligatorio incluido desde unos 40 € por persona, con el jardín botánico al final.",
        "Pico de São Tomé desde Bom Sucesso: 2 días (3 si se quiere observar fauna), unos 1.200 m de desnivel acumulado, dificultad alta, DOS guías obligatorios por seguridad desde 180 € solo los guías, con vivac. La variante clásica de Ponta Figo permite hacerlo de un tirón en 18 horas.",
        "Pico Calvário: 3,5-4 horas de subida y 3 de bajada hasta los 1.600 m, dificultad media con buena forma física, unos 70 € en el día y 130-180 € con noche de acampada; humedad altísima y bosque cargado de epífitas.",
        "Bom Sucesso–Bombaim por Trás-os-Montes: 6-7 horas, +400 / -1.000 m, media-alta, 40-50 € el guía; se atraviesan roças abandonadas y se termina en un alojamiento en funcionamiento.",
        "Bombaim–São João dos Angolares: la travesía larga del interior, 10-11 horas de marcha (12-13 con paradas), dificultad alta de resistencia, 120 € con tres días de antelación; poco recorrida, bosque primario y secundario hasta el nivel del mar.",
        "Bom Sucesso–Ponta Figo: 2 días, hasta ~2.700 m acumulados, dificultad alta, guía obligatorio y transporte de regreso a concertar; se puede hacer sin coronar el Pico.",
        "Pico do Papagaio, en Príncipe: 6 horas ida y vuelta (unas 2,5 de subida y 1,5 de bajada), difícil, terreno empinado, resbaladizo y embarrado, con cuerdas fijas en los tramos finales; guía muy recomendado y obligatorio en ciertas zonas del parque. Mejor de junio a septiembre.",
        "Cascada de Oquê Pipi y trilha de la Roça Infante, en Príncipe: 4 horas de dificultad moderada la primera, con piscina natural al final, y 6 horas la segunda hasta una plantación abandonada.",
    ],
    acampada=[
        "No hay camping de carretera al uso en ninguna de las dos islas y NO se ha localizado una sola ficha de iOverlander para Santo Tomé y Príncipe: el único resultado de iOverlander con ese nombre corresponde a Farol de São Tomé, en Brasil. Hay que darlo por zona sin cobertura overlander.",
        "La acampada real y organizada está ligada al trekking del Obô: la travesía del Pico de São Tomé se hace con vivac (campamento clásico en Pico Mesa, 1.875 m) y los operadores incluyen el material en el precio; el Pico Calvário se ofrece con noche de acampada por 130-180 €.",
        "Dentro del parque se acampa con guía acreditado y en los puntos que él indique; entrar por libre no está previsto. En Príncipe el guía es obligatorio por norma del parque, lo que descarta el vivac autónomo.",
        "Alternativa habitual a la tienda: dormir en las roças rehabilitadas. Roça São João dos Angolares es hotel, restaurante y centro de arte; Roça Sundy y Belo Monte son hoteles de la Príncipe Collection; en Bombaim hay alojamiento sencillo en la propia roça.",
        "En la costa sur, el Jalé Ecolodge ofrece cabañas rústicas sin electricidad sobre la playa de desove; la playa está vigilada por guardas del Programa Tatô que despiertan a los huéspedes para ver tortugas. Es lo más parecido a acampar en la arena de forma legal.",
        "Acampada libre en playa: desaconsejada. El aviso canadiense recomienda expresamente evitar las playas desiertas y las zonas mal iluminadas después del anochecer, y el MAEC desaconseja los desplazamientos nocturnos. Además, buena parte de las playas del este y del sur son de desove entre septiembre y abril.",
        "Plataformas comerciales (Pitchup, Tripadvisor) listan «campings» en el país, pero al revisarlos se trata de alojamientos tipo lodge y de un «MIP Wild Camping» en Príncipe; no son campings para vehículos. Dato flojo: por confirmar sobre el terreno.",
        "Conclusión práctica para la app: en Santo Tomé y Príncipe no se planifica noche en vehículo. Se duerme en roça, en ecolodge o en vivac guiado dentro del parque.",
    ],
    visado=[
        "ESPAÑOLES: EXENTOS de visado para estancias de HASTA 15 DÍAS, con pasaporte en vigor y validez mínima de 6 meses (MAEC, 1 jun. 2026). El DNI no sirve.",
        "TASA DE TURISMO (dato oficial): 25 € por persona al entrar por São Tomé y 10 € por Príncipe, pago ÚNICO —no por noche— en el propio aeropuerto, con QR para pago en línea; exentos los menores de 12 años, los santotomenses y los residentes (turismo.gov.st).",
        "Discrepancia a tener en cuenta: el FCDO (dic. 2025) habla de «a 20-euro entry fee» y el MAEC de una tasa turística de 75.000 dobras (~3,5 €) por turista y noche desde el 15 de junio de 2016. Llevar 30 € por persona en efectivo y no contar con cambio.",
        "MÁS DE 15 DÍAS, o viaje de trabajo, estudios o negocios: visado previo por el sistema e-VisaST, en línea, resuelto en unos 7 días hábiles (política de visados del país; FCDO). Portal oficial: no localizado en esta sesión.",
        "Los titulares de visado Schengen o estadounidense en vigor entran 15 días sin trámite adicional.",
        "FRONTERA TERRESTRE: NO EXISTE. Todos los controles son el aeropuerto de São Tomé (TMS), el de Príncipe (PCP) y el puerto de Ana Chaves para llegadas marítimas.",
    ],
    fronteras_rows=[
        ("Entrada principal (aire)", "Aeropuerto Internacional de São Tomé (TMS / FPST)", "Único punto de entrada realista. Pista 11/29 de 2.220 m a 5 km de la capital (Wikipedia). Pasaporte ≥6 meses, tasa de turismo de 25 € a la llegada, certificado de fiebre amarilla si se llega desde país con riesgo. Sin visado hasta 15 días."),
        ("Entrada secundaria (aire)", "Aeropuerto de Príncipe (PCP / FPPR)", "Pista 18/36 de 1.750 m, ampliada entre 2012 y 2015. Solo enlaces con São Tomé: STP Airways (aviones de 20 plazas) y Afrijet (70), media hora largo de vuelo, con cancelaciones frecuentes (MAEC; Alma de Viajante). Tasa de turismo de 10 € si se entra por aquí."),
        ("Entrada marítima", "Puerto de Ana Chaves (São Tomé)", "Puerto principal del país para mercancía sólida, construido a finales de los años cincuenta sobre terreno ganado al mar: muelle de 200 m y solo 3 m de calado (Wikipedia). NO hay línea regular de pasajeros con vehículos. Un 4x4 propio solo llega en contenedor; despacho y admisión temporal POR CONFIRMAR."),
        ("Enlace interinsular (mar)", "São Tomé – Santo António do Príncipe (barco Olivia C)", "Barco de 300 plazas comprado en Grecia por el empresario João Cardoso que en 2023 reanudó una conexión parada cuatro años tras el accidente del Anfitrite; ida y vuelta ~130 USD (≈3.000 dobras), muy por debajo del avión (VOA Português; RSTP/UCCLA, mar. 2023). Horarios y admisión de vehículos: POR CONFIRMAR."),
        ("Puerto secundario", "Puerto de Neves (noroeste de São Tomé)", "Segundo puerto del país según Wikipedia, ligado a la terminal de combustibles. Uso para pasajeros o vehículos: POR CONFIRMAR."),
        ("Frontera terrestre", "NINGUNA", "Santo Tomé y Príncipe no tiene frontera terrestre con ningún país. El vecino más próximo es Gabón, a unos 250 km de mar abierto; entre las dos islas principales hay otros 150 km."),
    ],
    vehiculos=[
        "NO HAY RÉGIMEN DE ADMISIÓN TEMPORAL DOCUMENTADO: ninguna fuente oficial santotomense accesible describe cómo entra un vehículo extranjero, porque en la práctica nadie llega con el suyo. POR CONFIRMAR con la aduana.",
        "CPD (carnet de passages en douane): carnetdepassage.org es explícito —«AIT/FIA currently does not have any official CPD-issuing organization in the country»—, o sea, no hay club emisor local; si se usara, habría que emitirlo en España (RACE).",
        "CONDUCCIÓN POR LA DERECHA, herencia portuguesa. El MAEC es taxativo: «es necesario estar en posesión de un permiso internacional»; el FCDO exige llevar a la vez el carné nacional y el internacional, y Canadá lo repite. Llevar los dos.",
        "CARRETERAS: una sola vía principal rodea casi toda la isla de São Tomé, con asfalto aceptable en el norte y pistas de tierra en el sur y el interior. «Many roads are in poor condition and unlit, particularly outside the capital» (FCDO, dic. 2025). Animales sueltos de noche y desprendimientos tras las lluvias; el MAEC desaconseja conducir de noche.",
        "4x4: no es imprescindible para la vuelta a la isla —Sven's Travel Venues la hizo entera en 2WD (2020) y Traveltomtom dice lo mismo—, pero sí para bajar a Porto Alegre y Praia Jalé, donde «a estrada está mesmo muito má» pasada Agripalma (Alma de Viajante), y para las pistas del Obô y la Lagoa Amélia (The Chocolate Islands).",
        "DISTANCIAS: la isla grande son 50 x 30 km; de norte a sur, unos 40 km que se hacen en 2–3 horas, y nada está a más de dos horas (Sven's Travel Venues; Chris Travel Blog). El GPS de Google Maps funciona, pero falla en zonas remotas y no hay señalización.",
        "ALQUILER, la alternativa realista: 25 €/día un jeep de particular (Traveltomtom) y de 42,50 € un Daihatsu Terios a 135 € un Land Cruiser Prado en operador formal, con seguro a todo riesgo, asistencia y fianza de 100–150 € (The Chocolate Islands, 2026). Edad mínima 18 años y carné europeo o internacional.",
        "SEGURO: la Carta Verde española no cubre el país —el sistema abarca el EEE más Marruecos, Túnez, Turquía, Ucrania y otros (OFESAUTO)— y no hay tarjeta regional aplicable: Santo Tomé y Príncipe no pertenece ni a la CEDEAO (Carte Brune) ni a la CEMAC (Carte Rose). Existencia de seguro local de frontera: POR CONFIRMAR.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Estado legal: SIN REGULACIÓN codificada (drone-laws.com, act. 21 ene. 2026). No hay ley, registro ni tasa publicada; tampoco prohibición expresa localizada.",
        "Autoridad competente: Instituto Nacional de Aviação Civil (INAC), inac.st. Escribir antes de viajar y llevar la respuesta impresa es la única forma de cubrirse.",
        "A falta de norma local, drone-laws.com recomienda aplicar las reglas OACI: vista directa permanente, por debajo de 150 m, 50 m de separación de personas y bienes y 8 km de cualquier aeropuerto.",
        "PROHIBIDO fotografiar aeropuertos, instalaciones militares y edificios gubernamentales (Gobierno de Canadá, 1 sep. 2026): la prohibición vale igual con cámara que con dron, y con seis roças inscritas por la UNESCO en 2026 cabe esperar restricciones nuevas sobre los conjuntos protegidos.",
        "Sanciones, decomiso en aduana y trámite de autorización: POR CONFIRMAR. Ninguna fuente abierta en esta sesión documenta un caso real de confiscación ni un permiso concedido.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "DISPONIBLE: servicio activo desde el 12 de diciembre de 2025, 26.º país africano en tenerlo (Space in Africa; TechAfrica News, dic. 2025).",
        "Precio del kit y de la suscripción residencial o Roam en el país: POR CONFIRMAR (las noticias de lanzamiento no publican tarifas).",
        "Operadores móviles: CST (Companhia Santomense de Telecomunicações) y Unitel STP. SIM a la venta en el aeropuerto y en la ciudad; Unitel suele salir más barata para el viajero (Alma de Viajante; thingstodoinsaotome, 2026).",
        "Cobertura 4G en casi toda la isla de São Tomé y en las zonas pobladas de Príncipe, con 10–25 Mbps típicos y zonas muertas en el interior. Hay eSIM de Airalo apoyada en las redes locales, pero cuesta dos o tres veces más por giga que una SIM local.",
        "El país depende de un único cable submarino para su conexión internacional, lo que explica el interés oficial por el satélite; la conexión es «aceitável» pero no siempre fiable (Alma de Viajante, act. sep. 2026).",
    ],
    perro_intro=[
        "ENTRADA: NO existe —o no es accesible— ninguna página oficial santotomense que publique los requisitos de importación de animales de compañía. Ni el MAEC, ni el FCDO, ni Canadá mencionan mascotas en sus fichas del país. Lo lógico (microchip ISO, rabia en vigor puesta ≥21–30 días antes, certificado veterinario internacional reciente) es DEDUCCIÓN, no fuente. POR CONFIRMAR.",
        "PERMISO PREVIO DE IMPORTACIÓN: no se puede confirmar ni descartar. La vía práctica para cerrarlo es el Consulado Honorario de España en Santo Tomé o la Embajada en Libreville, competente para el país.",
        "RAZAS PROHIBIDAS: sin fuente. No consta lista de razas vetadas ni normativa de perros potencialmente peligrosos.",
        "VUELO: al ser destino solo aéreo, el perro viaja en cabina si no supera 8 kg con transportín flexible de 45x30x23 cm, o en bodega hasta 45 kg con transportín rígido IATA; TAP cobra desde 150 € por trayecto en intercontinental y no admite razas braquicéfalas en bodega (flytap.com). Reservar con mucha antelación: las plazas de bodega se limitan en temporada alta africana (junio–septiembre, diciembre–enero, marzo).",
        "VUELTA A LA UE: el país NO figura en los Anexos I ni II del Reg. de Ejecución (UE) 2026/636 (aplicable desde el 22 de abril de 2026; de los territorios insulares africanos y atlánticos solo están Mauricio, Santa Elena y Ascensión). Rige por tanto la vía de país NO listado: titulación de anticuerpos ≥0,5 UI/ml en laboratorio aprobado por la UE.",
        "VÍA A (la buena): si la titulación se hace en España ANTES de salir y queda anotada en el pasaporte europeo, la vacuna antirrábica sigue en vigor y no se revacuna fuera de la UE, el perro vuelve con el pasaporte y NO se aplica la espera de 90 días (Reg. Delegado (UE) 2026/131). Si la rabia caduca en ruta, son unos cuatro meses de espera.",
        "RIESGOS EN DESTINO: rabia presente en la región, calor y humedad ecuatoriales todo el año, malaria y filariosis por mosquito, y atención veterinaria muy escasa —hay consulta veterinaria en la capital, pero no se ha podido abrir su web—. Botiquín propio y antiparasitario externo de amplio espectro.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "MALARIA: riesgo ALTO en todo el país y todo el año. El MAEC (1 jun. 2026) recomienda iniciar la profilaxis quince días antes y mantenerla quince días después; TravelHealthPro propone atovacuona/proguanil, doxiciclina o mefloquina. Es el riesgo sanitario número uno del destino.",
        "FIEBRE AMARILLA: certificado OBLIGATORIO para quien llegue desde un país con riesgo de transmisión —en la práctica, cualquier escala africana—, no exigido en vuelo directo desde Europa (MAEC; FCDO, dic. 2025; Canadá, sep. 2026). TravelHealthPro considera el riesgo local bajo y no recomienda la vacuna con carácter general.",
        "OTRAS VACUNAS: hepatitis A, tétanos y fiebre tifoidea para casi todos los viajeros; hepatitis B, rabia, sarampión, dengue y BCG según perfil (TravelHealthPro). El MAEC añade hepatitis B y tétanos.",
        "DENGUE, CHIKUNGUNYA Y ESQUISTOSOMIASIS presentes (TravelHealthPro): repelente de día y de noche —el mosquito del dengue pica de día— y nada de baños en agua dulce estancada. El MAEC confirma casos registrados de dengue.",
        "SANIDAD: medios «muy básicos» según el MAEC, que recomienda seguro con repatriación. Canadá añade que hay que pagar en efectivo por adelantado, que las ambulancias apenas existen fuera de las ciudades y que la evacuación médica es muy cara. Referencia: Hospital Ayres de Menezes, São Tomé (+239 222 12 22), con hemodiálisis desde 2009 y TAC desde 2017.",
        "AGUA Y ALIMENTOS: no beber del grifo. Hervir, filtrar o embotellar; precauciones estándar con la comida (TravelHealthPro).",
        "Seguro con cobertura de EVACUACIÓN AÉREA: imprescindible. La evacuación realista sale hacia Libreville o Lisboa; en la isla no hay alternativa.",
    ],
    seguridad_intro="Conviene decirlo sin rodeos para que no se confunda con sus vecinos del golfo de Guinea: Santo Tomé y Príncipe es de los países más seguros y libres de África. Freedom House le da 84 sobre 100 y estatus «Free» (2025); el MAEC no desaconseja viajar, habla de situación «habitualmente tranquila» y no señala ninguna zona de especial peligro; Canadá aplica su nivel más bajo y el FCDO dice que la criminalidad es «generally low». Lo que hay son hurtos en playas y mercados y una inestabilidad política crónica pero no violenta.",
    seguridad=[
        "MAEC (1 jun. 2026): «SE RECOMIENDA VIAJAR CON PRECAUCIÓN», el escalón más bajo de aviso. Situación «habitualmente tranquila» y NINGUNA zona de especial peligro señalada. No desaconseja ningún viaje.",
        "Freedom House, Freedom in the World 2025: 84/100 y estatus «Free» (35/40 en derechos políticos, 49/60 en libertades civiles). «Holds regular, competitive elections and has undergone multiple transfers of power between rival parties». Es de las mejores puntuaciones del continente.",
        "Gobierno de Canadá (1 sep. 2026): «precauciones de seguridad normales», equivalentes a las de Canadá. Tirones y carterismo en mercados, playas y zonas concurridas; asaltos a mano armada y robos en domicilios, raros pero existentes.",
        "FCDO (10 dic. 2025): «the crime rate in São Tomé and Príncipe is generally low, but burglaries and armed robberies can happen». No llevar joyas, efectivo abundante ni objetos de valor a la playa.",
        "El MAEC sí advierte de robos, agresiones e incluso violaciones contra turistas, sobre todo en playas y mercados, y desaconseja pasear en solitario de noche.",
        "INESTABILIDAD POLÍTICA CRÓNICA, no violenta: en 24 años se sucedieron 16 gobiernos sin que ninguno completara la legislatura (Ficha País MAEC, nov. 2025). En enero de 2025 el presidente destituyó al primer ministro Patrice Trovoada, que calificó la medida de inconstitucional.",
        "ASALTO A UN CUARTEL EN NOVIEMBRE DE 2022: intento de golpe fallido en el que murieron cuatro civiles desarmados; el Tribunal Supremo confirmó una condena de 15 años al superviviente y siete militares seguían pendientes de juicio por tortura y asesinato a finales de 2024 (Ficha País MAEC; Freedom House 2025).",
        "CALENDARIO ELECTORAL 2026: Carlos Vila Nova fue reelegido presidente en primera vuelta el 19 de julio de 2026 con el 55,9 %, con una abstención récord del 58,6 %, y hay elecciones legislativas el 27 de septiembre de 2026. Evitar mítines y concentraciones en esas fechas.",
        "PROHIBIDO fotografiar aeropuertos, instalaciones militares y edificios gubernamentales, y penas severas por drogas (Canadá, sep. 2026). Conducción nocturna desaconsejada por el MAEC: sin iluminación, con peatones y animales en la calzada y desprendimientos tras la lluvia.",
    ],
    agua=[
        "NO BEBER DEL GRIFO: hervir, filtrar o embotellar (TravelHealthPro). Para ducha y lavado no hay advertencia específica en las fuentes consultadas, pero la red es frágil.",
        "EMAE (Empresa de Água e Electricidade) es la empresa pública del agua y la luz: opera 15 sistemas en São Tomé y 1 en la Región Autónoma de Príncipe, con el 71,5 % del agua de manantial y el 28,5 % de río, 7 estaciones de tratamiento y 10 puestos de cloración (emae.st). Contacto: geral@emae.st, +239 22 44 700.",
        "La realidad es peor que el organigrama: MÁS DE LA MITAD de los 230.000 habitantes no tiene acceso a agua potable y el 40 % del agua tratada se pierde en tuberías de época colonial, sobre todo en la capital; los distritos más afectados son São Tomé, Lembá, Cauê y Cantagalo (EMAE vía RTP África, 4 dic. 2024).",
        "Islas muy lluviosas —el sur y el interior pasan holgadamente de los 2.000 mm anuales— y con ríos abundantes: el problema no es la cantidad de agua sino su tratamiento y su distribución.",
        "Agua embotellada disponible en la capital y en los alojamientos; fuera de São Tomé la infraestructura turística es «prácticamente nula» (Sven's Travel Venues, 2020), así que conviene salir con reservas al bajar al sur.",
        "Puntos concretos de llenado de depósitos, campings y fuentes públicas: POR CONFIRMAR. Ninguna fuente abierta en esta sesión los documenta.",
    ],
    combustible=[
        "Precio aproximado más reciente: EN TORNO A 1 €/LITRO (iremviagem, guía publicada el 3 de noviembre de 2025). Con la paridad fija de 24,5 STN/€ son unas 24–25 dobras por litro.",
        "Último precio oficial con cifra exacta localizado: GASOLINA 30 dobras/l y GASÓLEO 25 dobras/l tras la unificación de precios entre las dos islas (STP Digital, 9 dic. 2021) ≈ 1,22 €/l y 1,02 €/l. PRECIO EXACTO 2026: POR CONFIRMAR.",
        "Hasta esa unificación Príncipe pagaba más caro que São Tomé (32 dobras la gasolina y 27 el gasóleo); el precio lo negocian el Gobierno central, el Gobierno Regional del Príncipe y ENCO, la empresa nacional de combustibles.",
        "RED ESCASA: las gasolineras se concentran en la capital y el eje norte. Chris Travel Blog avisa de llevar combustible propio porque «gasoline is limited», y los últimos cajeros bajando al sur están en São João dos Angolares (Alma de Viajante). Salir de São Tomé con el depósito lleno antes de bajar a Porto Alegre o Praia Jalé.",
        "Ha habido episodios de ESCASEZ DE GASOLINA con colas y especulación de precios (VOA Português; Notícias ao Minuto): todo llega en barco, y un retraso del buque vacía el mercado.",
        "Pago en efectivo en dobras; las tarjetas extranjeras no funcionan en cajeros (Canadá, sep. 2026). Calidad del gasóleo y aptitud para Euro 6 con AdBlue: POR CONFIRMAR, ningún relato lo documenta.",
    ],
    experiencias_intro="No hay ni un solo relato de overlander con vehículo propio: es imposible llegar rodando y nadie documenta haber metido un 4x4 en contenedor. Lo que sigue son nueve relatos y fuentes de viajeros que alquilaron coche en la isla o describen el transporte real del archipiélago, entre 2018 y 2026.",
    experiencias=[
        "Sven's Travel Venues (marzo 2020) — «¿hace falta 4x4 en São Tomé?»: dio la vuelta entera a la isla con un 2WD y concluye que «a 2WD was absolutely sufficient and of course much cheaper». Baches, charcos y barro tras la lluvia, una sola carretera principal y 40 km de norte a sur en 2–3 horas. Le prometieron un 4x4 a las 7 y llegó un 2WD a las 10, con el depósito vacío.",
        "Alma de Viajante (abr. 2024, act. 15 sep. 2026) — el relato más útil: recomienda un Suzuki Jimny para bajar al sur porque «a estrada está mesmo muito má» pasada Agripalma camino de Porto Alegre, tres horas hasta el sur sin paradas, últimos cajeros en São João dos Angolares, cambio de 25 dobras por euro y SIM de CST o Unitel en el aeropuerto. Consejo clave: ir a Príncipe al principio, porque los vuelos se cancelan.",
        "Traveltomtom (blog de la vuelta al mundo, país 123) — alquiló un jeep por 25 €/día a un particular por WhatsApp, dice que no hace falta 4x4 salvo en el sur, donde el firme es «horrible», compró la SIM barata en la ciudad y resume el país como «one of the safest countries to visit in Africa». Detalla precios reales: 230 USD el vuelo desde Duala, 50 USD/noche en Domus Praia Jalé.",
        "Chris Travel Blog (abr. 2018) — itinerario de cinco días con coche: nada está a más de dos horas, Google Maps funciona, «it's perfectly safe to drive around yourself», carné internacional recomendado y aviso de llevar combustible porque la gasolina es limitada. Roças visitadas: Água Izé sin restaurar, Monte Café como la mejor conservada, São João dos Angolares con menú de degustación y Diogo Vaz y Monte Forte en el norte.",
        "Ir em Viagem (3 nov. 2025) — guía de viaje con los números del bolsillo: dobra a 25 por euro, euros aceptados en todas partes pero el cambio en dobras, «não existem caixas multibanco (exceto os de bancos locais), por isso, levantar dinheiro está fora de questão», combustible en torno a 1 €/litro, 4x4 recomendado, carreteras sin señalización y GPS imprescindible, y la gravana de junio a septiembre como mejor época.",
        "The Chocolate Islands (2026) — operador local de alquiler: 42,50 €/día un Daihatsu Terios, 50 € un Mitsubishi Sport, 75 € un Suzuki Jimny y 90–135 € un Toyota Prado, con seguro a todo riesgo, asistencia y fianza de 100–150 €, desde los 18 años y con carné europeo o internacional. Confirma que el 4x4 solo es imprescindible para Praia Jalé, el Obô y la Lagoa Amélia.",
        "VOA Português — la reanudación del enlace marítimo: tras cuatro años sin barco entre islas por el accidente del Anfitrite, el empresario santotomense João Cardoso compró en Grecia el Olivia C, de 300 plazas, y reabrió la ruta con ida y vuelta a unos 130 dólares (≈3.000 dobras), muy por debajo del avión. El mismo reportaje recuerda que en dos décadas naufragaron más de media docena de barcos en estas rutas, «frequentemente por excesso de carga».",
        "Bradt Guides, Kathleen Becker (7 may. 2021) — «A world of roças» explica el hilo que ordena la visita: hubo unas 150 plantaciones a principios del siglo XX y unas 200 se nacionalizaron tras la independencia de 1975; muchas se cayeron a pedazos y otras son hoy hoteles. Agostinho Neto es la mayor con 3.380 ha y está en ruina; Água Izé, 2.600 ha, es la cuna del cacao comercial; Sundy, 1.657 ha, es hotel.",
        "UNESCO y Africanews (27–28 jul. 2026) — el cambio de estatus: el Comité del Patrimonio Mundial reunido en Busan inscribió «The Roças of Sao Tome and Principe: Colonial Agricultural System and Forced Migration», primer bien del país, con seis componentes —Monte Café, Água Izé, Diogo Vaz, São João, Sundy y Belo Monte— y 72,9 ha de bien, por documentar el trabajo forzado que sostuvo el cacao tras la abolición de la esclavitud.",
        "FCDO y Gobierno de Canadá (dic. 2025 y sep. 2026) — la letra pequeña del día a día: taxis y mototaxis («motoqueiros») son el único transporte público y «are often unsafe and in poor condition»; carreteras asfaltadas con baches grandes en la capital y regulares fuera, intransitables con lluvia, sin ninguna asistencia en carretera y sin posibilidad de sacar dinero de un cajero con tarjeta extranjera.",
    ],
    pendientes=[
        ("Tasa de entrada: 25 € oficiales frente a 20 € del FCDO y 75.000 dobras/noche del MAEC", "Confirmar por escrito con el Consulado Honorario de España en Santo Tomé o con turismo.gov.st qué se cobra exactamente a un español a la llegada y si la tasa por noche del MAEC sigue viva."),
        ("Portal oficial de la eVisa santotomense", "Localizar y abrir la página gubernamental del sistema e-VisaST (coste, plazo, requisitos). Hoy solo se confirma su existencia por Wikipedia y el FCDO; turismo.gov.st no publica visados."),
        ("Requisitos de entrada del perro", "Obtener del ministerio competente en agricultura (servicios veterinarios) o del consulado honorario el listado oficial: microchip, rabia, plazo del certificado, permiso previo y razas vetadas. Criterio de cierre: respuesta escrita o página oficial abierta."),
        ("Admisión temporal de vehículos y despacho en Ana Chaves", "Confirmar con la aduana santotomense si existe régimen de importación temporal para vehículos de turistas, su plazo y si se exige depósito o CPD. Hoy no hay ninguna fuente."),
        ("Seguro de responsabilidad civil para un vehículo importado", "Verificar si alguna aseguradora local emite póliza de frontera y su coste; descartar formalmente Carte Rose CEMAC y Carte Brune CEDEAO por escrito de OFESAUTO o del asegurador."),
        ("Precio exacto del combustible en 2026", "Encontrar un dato datado de 2025 o 2026 (prensa santotomense, ENCO o GlobalPetrolPrices) que sustituya al «en torno a 1 €/l» y a las 30/25 dobras de diciembre de 2021. globalpetrolprices.com y diesel-fuel-prices.com no se abrieron en esta sesión."),
        ("Precio y roaming de Starlink en el país", "Consultar el mapa y la tienda de starlink.com con una dirección de São Tomé: disponibilidad de kit, tarifa mensual y si el plan Roam funciona allí."),
        ("Regulación de drones del INAC", "Escribir al Instituto Nacional de Aviação Civil (inac.st) y pedir por escrito si hace falta autorización, con qué plazo y qué sanción hay. Criterio de cierre: respuesta del INAC o norma publicada."),
        ("Fiabilidad y horarios reales del Olivia C en 2026", "Frecuencia, precio y estado de servicio del barco interinsular, y si admite vehículos o solo pasajeros y carga suelta. Criterio: confirmación del armador o de una agencia local."),
        ("Coste real de meter un 4x4 en contenedor", "Presupuesto en firme de un transitario Lisboa–São Tomé para un vehículo de 5 m: flete, despacho, tasas portuarias y devolución. Las horquillas de 500–3.000 € son genéricas de carga, no de coches."),
        ("Puntos de agua, campings y acampada libre", "Sin ninguna fuente sobre llenado de depósitos ni campings en las dos islas; cerrar con iOverlander, Park4Night o un operador local."),
        ("Efectos de la inscripción UNESCO de 2026 en la visita a las roças", "Comprobar si las seis roças inscritas han pasado a cobrar entrada, a exigir guía o a limitar el acceso rodado y los drones."),
    ],
    sources=SOURCES,
    sources_note="Revisión hecha el 18 de septiembre de 2026 con las páginas abiertas en esa fecha; todos los datos proceden de fuentes consultadas una a una y lo que no se ha podido confirmar aparece marcado como «por confirmar». Los visados, las tasas y los requisitos sanitarios cambian sin aviso, y ninguna de estas fuentes sustituye a la consulta directa con la Embajada de España en Libreville o con el Consulado Honorario en Santo Tomé. Esta ficha es una herramienta de planificación, no una autorización ni un documento oficial.",
    emergency="EMERGENCIA CONSULAR de la Embajada de España en Libreville, competente para Santo Tomé y Príncipe: +241 66 44 47 47. Consulado Honorario en Santo Tomé (Miguel Martín Alomar): +239 997 80 22 y +34 601 41 12 84. POLICÍA 113 o +239 222 22 22; ASISTENCIA MÉDICA +239 221 221; BOMBEROS 112 (Gobierno de Canadá, 1 sep. 2026). Hospital Ayres de Menezes: +239 222 12 22 (MAEC). Sin rescate ni asistencia en carretera: seguro con repatriación imprescindible.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

# -*- coding: utf-8 -*-
"""Guinea-Bisáu — ficha completa (18 sep 2026): EXCLUIDO POR PROTOCOLO.

Guinea-Bisáu está EXCLUIDA POR PROTOCOLO del proyecto por su inestabilidad política recurrente (golpes y disolución del Parlamento; comprueba la situación de 2025-2026 con fuentes fechadas). El corredor Senegal→Guinea de la ruta 2027 (Kalifourou–Sambaïlo) la evita expresamente. La ficha es INFORMATIVA y completa por si en el futuro se plantea un desvío desde Casamance (Ziguinchor–Mpack–São Domingos) o una escapada a los Bijagós: PDIs, historia, trámites, dejando claro el estado de seguridad y el visado.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/guinea-bisau.json y audit/pdi/guinea-bisau.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Bisáu · Bissau Velho, fortaleza de Amura y palacio presidencial", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=11.8604702, lon=-15.5788643,  # Google Maps: Fort São José da Amura
        desc="Capital fundada en 1687 como factoría portuguesa y capital colonial solo desde 1941, cuando Bolama perdió el título. El casco viejo (Bissau Velho) conserva casas coloniales descascarilladas junto al puerto de Pidjiguiti, donde el 3 de agosto de 1959 la policía mató a 50 estibadores en huelga, chispa de la guerra de liberación. La fortaleza de São José da Amura (1753, planta Vauban) es cuartel y alberga el MAUSOLEO DE AMÍLCAR CABRAL. El palacio presidencial fue bombardeado en la guerra civil de 1998-99 y reconstruido en 2013. Ciudad tranquila pero con hurtos habituales; no caminar de noche.",
        dog_note="Paseo por Bissau Velho y el puerto de Pidjiguiti sin problema; dentro de la fortaleza (cuartel y mausoleo) mejor dejarlo en el coche vigilado.",
        visit={
            "why": "Es la única ciudad con servicios reales del país (bancos, combustible fiable, embajadas) y el punto de partida obligado hacia los Bijagós.",
            "see": "Fortaleza de Amura con el mausoleo de Cabral, calles de Bissau Velho, monumento de Pidjiguiti en el puerto, palacio presidencial y Museo Etnográfico Nacional (solo mañanas).",
            "access": "Asfalto desde São Domingos (N1/N3) y desde el este (N1). El pin marca la fortaleza, en el extremo sur de Bissau Velho junto al puerto; la entrada al mausoleo depende del oficial de guardia (recinto militar, sin horario publicado). Aparcar dos 4x4 en la Avenida Amílcar Cabral o en el hotel; las calles de la capital están en mal estado. Hurtos y tirones frecuentes en la capital (FCDO).",
            "when": "Primera hora de la mañana para el museo y la fortaleza; estación seca (noviembre-mayo).",
            "skip": "Si hay manifestaciones o despliegue militar tras el golpe de 2025: evitar edificios oficiales e instalaciones militares (FCDO/MAEC).",
        },
        links=[
            {"label": "Fortaleza de Amura (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Fortaleza_de_S%C3%A3o_Jos%C3%A9_da_Amura"},
            {"label": "Bissau (Wikivoyage)", "url": "https://en.wikivoyage.org/wiki/Bissau"},
            {"label": "MAEC · recomendaciones Guinea-Bissau", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Guinea-Bissau"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/View_of_Bissau_Velho,_Bissau.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:View_of_Bissau_Velho,_Bissau.jpg",
                "credit": "Jcornelius · CC BY-SA 4.0",
                "caption": "Bissau Velho, el casco histórico junto al puerto.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Interior_da_Fortaleza_de_S%C3%A3o_Jos%C3%A9_de_Amura,_Bissau.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Interior_da_Fortaleza_de_S%C3%A3o_Jos%C3%A9_de_Amura,_Bissau.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Interior de la fortaleza de São José da Amura.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bissau_city_center.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bissau_city_center.jpg",
                "credit": "Nammarci · CC BY-SA 3.0",
                "caption": "Centro de Bisáu desde la Pensão Central.",
            },
        ],
    ),
    dict(
        n=2, name="Quinhámel y la costa de Biombo", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=11.8722338, lon=-15.8756123,  # Google Maps: Hotel e Restaurante Mar Azul (Quinhámel)
        desc="Capital de la región de Biombo, a unos 35 km al oeste de Bisáu, en tierra del pueblo papel. Es el escape de fin de semana de la capital: el Mar Azul Lodge, bungalós redondos con piscina sobre la desembocadura del río a unos 45 min del aeropuerto, playas fangosas de marea, bolanhas de arroz y aldeas papel. Sirve de parada previa a los Bijagós (el lodge tiene lancha propia con aviso). Sin más servicios que los del lodge, que las reseñas describen como venido a menos; combustible en Bisáu.",
        dog_note="Playas y lodge sin restricción conocida; atado en las tabancas papel (cerdos, gallinas) y ojo con las mareas de fango.",
        visit={
            "why": "Primera noche tranquila fuera de la capital, con aparcamiento cerrado y lancha hacia el archipiélago sin pasar por el puerto de Bisáu.",
            "see": "Estuario y manglares del Mansoa, aldeas papel con casas de adobe y palma, telares, atardeceres sobre el agua.",
            "access": "Asfalto Bisáu–Quinhámel (unos 35 km); pista corta hasta el lodge. El pin marca el Mar Azul Lodge, que en iOverlander figura como hotel con posibilidad de aparcar; confirmar acampada por teléfono. Aparcamiento para dos 4x4 dentro del recinto.",
            "when": "Estación seca; marea alta para el baño y la lancha.",
            "skip": "Si se va directo a los Bijagós desde el puerto de Bisáu, es una desviación prescindible.",
        },
        links=[
            {"label": "Quinhamel (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Quinhamel"},
            {"label": "Mar Azul Lodge (Tripadvisor)", "url": "https://www.tripadvisor.com/Hotel_Review-g2282953-d2516322-Reviews-Mar_Azul_Lodge-Quinhamel_Biombo_Region.html"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Quinhamel_port_mar_azul.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Quinhamel_port_mar_azul.jpg",
                "credit": "Nammarci · CC BY-SA 3.0",
                "caption": "La orilla del Mar Azul en Quinhámel.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Quinhamel_main_street.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Quinhamel_main_street.jpg",
                "credit": "Nammarci · CC BY 3.0",
                "caption": "Calle principal y mercado de Quinhámel.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Biombo_coastal_mangrove.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Biombo_coastal_mangrove.jpg",
                "credit": "Nammarci · CC BY 3.0",
                "caption": "Manglar costero de la región de Biombo.",
            },
        ],
    ),
    dict(
        n=3, name="Cacheu · fuerte portugués y memorial de la esclavitud", cat="Cultura", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=12.2776893, lon=-16.1659317,  # Google Maps: Memorial da Escravatura e do Tráfico Negreiro de Cacheu
        desc="Uno de los asentamientos europeos más antiguos del África subsahariana: capitanía y fuerte desde 1588, villa en 1605 y puerto negrero portugués de la Alta Guinea. El fuerte de piedra de la década de 1640 sigue en pie, con estatuas coloniales portuguesas retiradas de Bisáu apiladas en su patio. El Memorial da Escravatura e do Tráfico Negreiro, abierto el 8 de julio de 2016 en la Casa Gouveia con fondos de la UE y la Fundación Mário Soares, expone cadenas, látigos y hierros de marcar. Calles pavimentadas con cáscara de palma; pueblo pequeño y tranquilo.",
        dog_note="El memorial es un museo (Casa Gouveia) y el fuerte un recinto histórico: dejarlo en el coche a la sombra o turnarse.",
        visit={
            "why": "Es la lectura histórica imprescindible del país: el punto de embarque de esclavos hacia Cabo Verde y América.",
            "see": "Fuerte del siglo XVII con cañones y estatuas, memorial con sala permanente, embarcadero del río Cacheu y sede del parque de manglares.",
            "access": "Asfalto desde São Domingos (N3 hacia el sur, desvío en Canchungo) o desde Bisáu por Bula y Canchungo. El pin marca el memorial, junto al fuerte y al río; aparcamiento en la explanada. Horario y precio no publicados en la web del memorial (fallo de carga): preguntar en la sede del parque a la entrada del pueblo.",
            "when": "Mañana; combinar con la piragua por los manglares según la marea.",
            "skip": "Si no hay tiempo, la fortaleza de Amura en Bisáu cubre la parte militar portuguesa; el memorial no tiene sustituto.",
        },
        links=[
            {"label": "Cacheu (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Cacheu"},
            {"label": "Memorial da Escravatura (Wikipédia pt)", "url": "https://pt.wikipedia.org/wiki/Memorial_da_Escravatura_e_do_Tr%C3%A1fico_Negreiro"},
            {"label": "Parque dos Tarrafes do Rio Cacheu · IBAP ecoturismo", "url": "https://ecoturismo.ibapgbissau.org/pntc.html"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Memorial_da_escravatura_e_do_tr%C3%A1fico_negreiro,_Cacheu_1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Memorial_da_escravatura_e_do_tr%C3%A1fico_negreiro,_Cacheu_1.jpg",
                "credit": "Jcornelius · CC BY-SA 4.0",
                "caption": "Memorial de la Esclavitud y del Tráfico Negrero de Cacheu.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Museu_Cacheu_06.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Museu_Cacheu_06.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Museo de la trata de esclavos, Cacheu.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Padr%C3%A3o_da_Rotunda_do_Porto,_Cacheu_4.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Padr%C3%A3o_da_Rotunda_do_Porto,_Cacheu_4.jpg",
                "credit": "Jcornelius · CC BY-SA 4.0",
                "caption": "Padrão de la rotonda del puerto de Cacheu.",
            },
        ],
    ),
    dict(
        n=4, name="Parque natural de los manglares del río Cacheu", cat="Naturaleza", prio="Media",
        dog="por confirmar", time="medio día",
        lat=12.2732631, lon=-16.1669156,  # Google Maps: Cacheu (sede del parque a la entrada del pueblo; el parque no figura como objeto en Google Maps)
        desc="Creado el 1 de diciembre de 2000, 886 km² con el 68 % cubierto de manglar: el MAYOR MANGLAR COMPACTO DE ÁFRICA OCCIDENTAL, sitio Ramsar desde el 22 de mayo de 2015. Aves migratorias invernantes, bosques sagrados y tabancas felupe con arrozales de marea entre Cacheu y São Domingos. Se visita en piragua desde Cacheu o São Domingos, siempre según horario de marea. Sin infraestructura: guías comunitarios de IBAP.",
        dog_note="Parque IBAP con código de conducta; en piragua no suele aceptarse; sin grandes depredadores terrestres, pero cocodrilos en el estuario.",
        visit={
            "why": "Es el manglar más extenso de la región y la forma de ver el país felupe desde el agua, en un tramo que además queda de paso desde Casamance.",
            "see": "Canales de manglar del río Blimbom, aves acuáticas, aldeas de Cobiana, Elalab y Elia, bosques sagrados.",
            "access": "La sede del parque está a la entrada de Cacheu (también información en São Domingos y en IBAP Bisáu, barrio de Luanda); allí se alquila piragua con guía. Las salidas dependen de la marea. El pin marca la sede/embarcadero de Cacheu; aparcamiento en la explanada del fuerte. Tarifas no publicadas online.",
            "when": "Noviembre-marzo (aves migratorias) y marea alta para navegar los canales.",
            "skip": "En la estación de lluvias (junio-octubre) o si ya se hace la salida en piragua de Cantanhez u Orango.",
        },
        links=[
            {"label": "Parque dos Tarrafes do Rio Cacheu · IBAP ecoturismo", "url": "https://ecoturismo.ibapgbissau.org/pntc.html"},
            {"label": "Cacheu River Mangroves NP (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Cacheu_River_Mangroves_Natural_Park"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Parque_Natural_dos_Tarrafes_do_Rio_Cacheu_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Parque_Natural_dos_Tarrafes_do_Rio_Cacheu_02.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Cartel de una de las entradas del parque de los Tarrafes.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/MULHERES_RURAIS_LIDERAM_MUDAN%C3%87AS_NAS_COMUNIDADES.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:MULHERES_RURAIS_LIDERAM_MUDAN%C3%87AS_NAS_COMUNIDADES.jpg",
                "credit": "Djibril Iero · CC BY-SA 4.0",
                "caption": "Comunidad de Djendem, santuario de ostras dentro del parque (Wiki Loves Africa 2024).",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Rio_Farim-Cacheu,_S%C3%A3o_Vicente,_Guinea-Bissau_(9087168099).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Rio_Farim-Cacheu,_S%C3%A3o_Vicente,_Guinea-Bissau_(9087168099).jpg",
                "credit": "jbdodane · CC BY 2.0",
                "caption": "El río Cacheu cerca de São Vicente.",
            },
        ],
    ),
    dict(
        n=5, name="Varela · playas del extremo noroeste", cat="Costa", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=12.286254, lon=-16.594543,  # Google Maps: Varela
        desc="Aldea felupe de unos 600 habitantes en la esquina noroeste del país, a 53 km de pista de laterita desde São Domingos y a la vista de Cap Skirring por la playa. La Praia de Varela pasa por LA MEJOR PLAYA CONTINENTAL DEL PAÍS: kilómetros de arena abierta al Atlántico tras las dunas y las palmeras, playa de pescadores con marisma de marea, laguna con pelícanos y nenúfares, ostras de Susana y langosta. Hay dos o tres alojamientos sencillos (Chez Hélène, Avó Anisa). La pista es de barro y puede ser lenta en lluvias.",
        dog_note="Playa abierta y aparthotel de gestión italiana sin restricción conocida; atarlo cerca de las aldeas felupe y vigilar hipopótamos en la laguna de Catão.",
        visit={
            "why": "Playa casi vacía a un paso de Casamance: la escapada más lógica si solo se pisa Guinea-Bisáu un par de días.",
            "see": "Praia de Varela y Praia dos Pescadores, dunas con palmeras, laguna, aldeas felupe de Susana (12 km antes), estación ambiental de AD con pequeño museo marino.",
            "access": "Desde São Domingos, 53 km de pista de laterita/arcilla sin asfaltar (4x4 recomendado; en lluvias puede tardar horas). El pin marca el Aparthotel Chez Hélène; se puede llegar en 4x4 hasta la playa por las dunas. Zona a menos de 20 km de la frontera senegalesa que Canadá desaconseja salvo viaje esencial; MAEC pide evitar pistas secundarias fronterizas.",
            "when": "Estación seca (noviembre-mayo); marea baja para caminar la playa grande.",
            "skip": "Con lluvias (junio-octubre) o si el aviso de la frontera Casamance empeora; entonces quedarse en Cap Skirring, en el lado senegalés.",
        },
        links=[
            {"label": "Varela (Wikipedia de)", "url": "https://de.wikipedia.org/wiki/Varela_(Guinea-Bissau)"},
            {"label": "Varela beach · Travel Tomorrow", "url": "https://traveltomorrow.com/guinea-bissau-varela-beach-a-madness-worthwhile/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Praia_de_Varela_(2).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Praia_de_Varela_(2).jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Reparando la piragua en la playa de Varela.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Paisagem_em_Varela,_Guin%C3%A9.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Paisagem_em_Varela,_Guin%C3%A9.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Sendero de la tabanca de Varela a la playa.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Praia_de_Varela_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Praia_de_Varela_(1).jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Playa de Varela.",
            },
        ],
    ),
    dict(
        n=6, name="Canchungo y São Domingos · la puerta desde Casamance", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=12.4100993, lon=-16.1963248,  # Google Maps: São Domingos
        desc="São Domingos es el primer pueblo bisauguineano tras el puesto de Mpack (Senegal) / Jegue (Guinea-Bisáu), en la carretera Ziguinchor–Bisáu. Ya había factoría portuguesa aquí en 1535 (Buguendo), antes de que el comercio se mudara a Cacheu. Canchungo, 40 km al sur, es la antigua Vila Teixeira Pinto, capital manjaco, con hospital nuevo y cruce hacia Cacheu y Caió. Ninguna de las dos tiene más que gasolinera, mercado y pensiones: la frontera cierra al mediodía (12:30-13:30) y tras las 18:00.",
        dog_note="Trámite fronterizo: llevar cartilla con rabia vigente y certificado sanitario; el veterinario de frontera puede no existir y el control es discrecional.",
        visit={
            "why": "Es el punto de decisión: aquí se cruza, se cambia moneda (mismo franco CFA) y se elige entre Varela, Cacheu o directo a Bisáu.",
            "see": "Puesto de Jegue, mercado de São Domingos con artesanía felupe (cucharas, ollas, machetes), y en Canchungo la plaza colonial y la carretera a Cacheu.",
            "access": "Asfalto Ziguinchor–Mpack–São Domingos–Ingoré–Bisáu (eje Dakar-Lagos). MAEC: cruzar siempre por la mañana; el puesto cierra 12:30-13:30 y después de las 18:00. Seguro carta verde CEDEAO y permiso internacional de conducir obligatorios. Vehículo: passavant (2.500 CFA, 2 semanas) o carnet de passages. El pin marca São Domingos; el puesto de Jegue queda unos km al norte, en la carretera.",
            "when": "Mañana temprano, en día laborable.",
            "skip": "Si la junta cierra fronteras (como el 26-11-2025) o si el aviso de Casamance se agrava: entonces la ruta 2027 sigue por Kalifourou–Sambaïlo sin tocar el país.",
        },
        links=[
            {"label": "São Domingos (Wikipedia)", "url": "https://en.wikipedia.org/wiki/S%C3%A3o_Domingos_(Guinea-Bissau)"},
            {"label": "Canchungo (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Canchungo"},
            {"label": "WikiOverland · Guinea-Bissau", "url": "http://wikioverland.org/Guinea-Bissau"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Road_sign_in_S%C3%A3o_Domingos,_Guinea-Bissau_(9087836224).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Road_sign_in_S%C3%A3o_Domingos,_Guinea-Bissau_(9087836224).jpg",
                "credit": "jbdodane · CC BY 2.0",
                "caption": "Cruce de São Domingos: Farim, Ingoré y Varela.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Posto_Galp_em_S%C3%A3o_Domingos,_Guin%C3%A9_(2).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Posto_Galp_em_S%C3%A3o_Domingos,_Guin%C3%A9_(2).jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Gasolinera Galp a la salida de São Domingos.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Avenida_principal_em_Canchungo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Avenida_principal_em_Canchungo.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Avenida principal de Canchungo.",
            },
        ],
    ),
    dict(
        n=7, name="Bolama · la antigua capital abandonada", cat="Cultura", prio="Media",
        dog="no recomendado", time="1–2 noches",
        lat=11.5770712, lon=-15.4800382,  # Google Maps: Bolama (ciudad)
        desc="Primera capital de la Guinea Portuguesa (1879-1941), disputada entre Portugal y Gran Bretaña hasta que en 1870 el arbitraje del presidente ULYSSES S. GRANT la adjudicó a Portugal. Perdió la capitalidad por falta de agua dulce y desde entonces se pudre con elegancia: palacio del gobernador en ruinas, cuartel colonial convertido en hospital, avenidas con columnatas, monumento al hidroavión estrellado en 1931 y casas vacías llenas de murciélagos. Es la isla de los Bijagós más cercana al continente. No hay coches: se llega en piragua desde São João o en lancha desde Bisáu.",
        dog_note="Hay que cruzar en piragua o lancha y dejar los coches en el continente; logística muy incómoda con perro.",
        visit={
            "why": "Ciudad fantasma colonial única en África Occidental, con playas y manglares alrededor.",
            "see": "Palacio del gobernador, iglesia, plaza y edificios administrativos abandonados, monumento al hidroavión, mercado y embarcadero.",
            "access": "Sin acceso rodado. Opción A: ferry Consulmar Bisáu–Enxudé (lunes a sábado 08:00, 45 min), camión a São João (30 km de pista que pueden llevar 4 h) y piragua a Bolama (350 CFA); exige dos días. Opción B: lancha privada directa desde el puerto de Bisáu. Los 4x4 se quedan en Bisáu (hotel con vigilancia). El pin marca el centro de la villa. MAEC y Canadá desaconsejan las piraguas.",
            "when": "Estación seca; salir con la primera marea.",
            "skip": "Con solo 2-3 días en el país, priorizar Bubaque/Orango; Bolama es un capricho histórico que consume dos jornadas.",
        },
        links=[
            {"label": "Bolama (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bolama_(town)"},
            {"label": "Bolama · Consulmar Travel", "url": "https://www.consulmartravel.com/en/bolama-colonial-history-and-traditions-on-an-island-with-charm/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Edif%C3%ADcios_Coloniais_em_Bolama,_Guin%C3%A9-Bissau_06.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Edif%C3%ADcios_Coloniais_em_Bolama,_Guin%C3%A9-Bissau_06.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Edificio colonial en el viejo centro de Bolama.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Amanhecer_em_Bolama,_Bolama,_Guin%C3%A9-Bissau_%E2%80%93_2018-03-03_%E2%80%93_DSCN1078.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Amanhecer_em_Bolama,_Bolama,_Guin%C3%A9-Bissau_%E2%80%93_2018-03-03_%E2%80%93_DSCN1078.jpg",
                "credit": "Helena Maria Pestana · CC BY-SA 4.0",
                "caption": "Amanecer en Bolama.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Avenida_Am%C3%ADlcar_Cabral,_Bolama,_Guin%C3%A9-Bissau_%E2%80%93_2018-03-02_%E2%80%93_DSCN1071.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Avenida_Am%C3%ADlcar_Cabral,_Bolama,_Guin%C3%A9-Bissau_%E2%80%93_2018-03-02_%E2%80%93_DSCN1071.jpg",
                "credit": "Helena Maria Pestana · CC BY-SA 4.0",
                "caption": "Avenida Amílcar Cabral, Bolama.",
            },
        ],
    ),
    dict(
        n=8, name="Bubaque · puerta del archipiélago de los Bijagós (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=11.3042531, lon=-15.83591,  # Google Maps: Hôtel Kasa Afrikana (Bubaque, junto al puerto)
        desc="Isla de 75 km² y principal puerto del archipiélago de los Bijagós: unas 88 islas e islotes, reserva de la biosfera desde 1996 y desde 2025 PATRIMONIO MUNDIAL UNESCO («Ecosistemas costeros y marinos del archipiélago de los Bijagós – Omatí Minhô», criterios ix y x, 394.067 ha). Bubaque tiene la sede de la reserva, un pequeño museo, lodges de todos los precios y la Praia de Bruce al sur. Es el único delta activo del Atlántico africano y una sociedad bijagó con fuerte peso de las mujeres. Ferry de unas 4 h desde Bisáu; lanchas más caras y rápidas.",
        dog_note="Ferry de pasaje de 4 h y lodges sin política de mascotas publicada; los coches se quedan en Bisáu. Consultar con el lodge antes.",
        visit={
            "why": "Base para todo el archipiélago: hipopótamos de Orango, tortugas de Poilão, playas de Rubane, y el ambiente de un puerto isleño sin coches.",
            "see": "Puerto y mercado, museo de la reserva, Praia de Bruce (13 km al sur, en moto), aldeas bijagó, atardeceres.",
            "access": "Sin vehículos: ferry de pasaje desde el puerto comercial de Bisáu los viernes (unas 4 h; ~15.000 CFA ida y vuelta según IBAP, 16.500 CFA ida según guía reciente), regreso los domingos desde Bubaque; lanchas de hoteles 30.000-35.000 CFA. Consulmar aclara que ya NO opera el ferry a Bubaque: confirmar operador en el puerto. En la isla todo se hace a pie o en moto. Los 4x4 quedan en Bisáu. Tasas de parque 5.000 CFA/día en islas protegidas. El pin marca el puerto.",
            "when": "Noviembre-abril; en la estación de lluvias las travesías se cancelan.",
            "skip": "Si no se dispone de 3-4 días completos (ida, vuelta y una excursión) o si el estado del mar/piraguas no da confianza.",
        },
        links=[
            {"label": "UNESCO · Bijagós – Omatí Minhô", "url": "https://whc.unesco.org/en/list/1431/"},
            {"label": "Reserva da Biosfera Bolama-Bijagós · IBAP", "url": "https://ecoturismo.ibapgbissau.org/rbabb.html"},
            {"label": "Bubaque (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bubaque"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bubaque_port.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bubaque_port.jpg",
                "credit": "Nammarci · CC BY 3.0",
                "caption": "Puerto de Bubaque, donde atraca el ferry de Bisáu.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bubaque_beach.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bubaque_beach.jpg",
                "credit": "Mooonswimmer · CC BY-SA 4.0",
                "caption": "Playa de Bubaque.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bubaque_Bruce_Beach.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bubaque_Bruce_Beach.jpg",
                "credit": "Mooonswimmer · CC BY-SA 4.0",
                "caption": "Praia de Bruce, en el sur de la isla.",
            },
        ],
    ),
    dict(
        n=9, name="Parque nacional de Orango · hipopótamos de agua salada", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=11.1816114, lon=-16.1399882,  # Google Maps: Hotel Orango Parque (Eticoga)
        desc="Parque creado en diciembre de 2000, 1.582 km² en parte marinos, sobre las islas Orango, Orangozinho, Meneque, Canogo e Imbone. Orango (272 km²) es la mayor del archipiélago y fue sede de la reina OKINKA PAMPA hasta su muerte en 1930. Sus lagunas de Anôr acogen hipopótamos que nadan en el mar y pastan en la playa, único caso conocido; también loros grises, manatíes, delfines y unas 250 especies de aves. Desde Eticoga, el Orango Parque Hotel organiza la caminata a la laguna (unos 20 min con guía local). Tasa de parque de 5.000 CFA/día.",
        dog_note="Parque nacional con hipopótamos (el animal más peligroso del continente) y cocodrilos; se camina 20 min hasta la laguna con guía. Sin perro.",
        visit={
            "why": "Ver hipopótamos en una laguna a un paso de la playa y dormir en una aldea bijagó donde la mujer elige marido.",
            "see": "Lagunas de Anôr con plataformas de observación, tumba de Okinka Pampa en Eticoga, arrozales (agosto-diciembre), manglares en kayak, isla de Imbone.",
            "access": "Solo en lancha desde Bubaque o Bisáu (hoteles y Consulmar). Se pernocta en el Orango Parque Hotel (~130 €/día pensión completa) o en la casa comunitaria de Anôr; Anôr está a 12 km a pie de Eticoga. El pin marca el hotel-embarcadero de Eticoga (coordenadas del parque, verificar en Maps). Tasa IBAP 5.000 CFA/día.",
            "when": "Octubre-diciembre, cuando las lagunas aún están llenas y los hipopótamos se concentran; visitas al amanecer.",
            "skip": "En lluvias (junio-septiembre) el mar impide las travesías; sin 2 días completos desde Bubaque no compensa.",
        },
        links=[
            {"label": "Parque Nacional de Orango · IBAP ecoturismo", "url": "https://ecoturismo.ibapgbissau.org/pno.html"},
            {"label": "Orango Parque Hotel · hipopótamos", "url": "https://www.orangohotel.com/en/hippos-on-the-island-of-orango-guinea-bissau/"},
            {"label": "Orango NP (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Orango_Islands_National_Park"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lagoa_com_hipop%C3%B3tamos_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lagoa_com_hipop%C3%B3tamos_01.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Laguna de los hipopótamos de agua salada, isla de Orango.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lagoa_com_hipop%C3%B3tamos_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lagoa_com_hipop%C3%B3tamos_02.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Paisaje de Orango junto a la laguna de los hipopótamos.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Orango_Parque_Hotel_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Orango_Parque_Hotel_01.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Orango Parque Hotel, en Ponta Anabaca (base para ver los hipopótamos).",
            },
        ],
    ),
    dict(
        n=10, name="Parque nacional marino João Vieira–Poilão · tortugas verdes", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1 noche",
        lat=10.866667, lon=-15.716667,  # Google Maps: Poilão (isla)
        desc="Parque marino creado en agosto de 2000 (decreto 6-A/2000): 495 km², de ellos 479 de mar, en torno a cuatro islas deshabitadas del sureste del archipiélago (João Vieira, Cavalos, Meio y Poilão). Poilão es sagrada para los bijagó de Canhabaque, y ese tabú la convirtió en la MAYOR PLAYA DE NIDIFICACIÓN DE TORTUGA VERDE DE ÁFRICA: de 7.400 nidos contados en 2000 a 40.000 en 2014 y hasta 62.000 en 2020, con noches de más de mil hembras. Visitas solo con autorización, en lancha y con guardas del parque.",
        dog_note="Islas sagradas bijagó y playa de nidificación protegida; acceso solo en lancha con guía IBAP.",
        visit={
            "why": "Uno de los cinco mayores nidales de tortuga verde del planeta, en una isla sin nadie.",
            "see": "Desove nocturno (julio-octubre) y eclosiones, playas de arena blanca, bosque de la isla de João Vieira, aves marinas.",
            "access": "Solo por mar: lanchas desde Bubaque (varias horas; el parque queda al sur del archipiélago). Tasa y guía de IBAP obligatorios; las cuatro islas son sagradas y propiedad tradicional de cuatro tabancas de Canhabaque, con zonas vetadas. Alojamiento en el lodge Chez Claude de João Vieira (+245 966 179 577) o pernocta en Bubaque. El pin marca la isla de Poilão (coordenadas del parque en Wikipedia).",
            "when": "Julio-octubre para el desove, que coincide con la estación de lluvias y mar difícil; septiembre-octubre es el compromiso.",
            "skip": "Fuera de la temporada de desove o con mar de fondo; sin guía IBAP no se puede desembarcar.",
        },
        links=[
            {"label": "PNM João Vieira e Poilão · IBAP ecoturismo", "url": "https://ecoturismo.ibapgbissau.org/pnmjvp.html"},
            {"label": "João Vieira–Poilão (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Jo%C3%A3o_Vieira_and_Poil%C3%A3o_Marine_National_Park"},
            {"label": "UNESCO · Bijagós – Omatí Minhô", "url": "https://whc.unesco.org/en/list/1431/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tidal_landscapes_of_the_Bijag%C3%B3s_Archipelago,_Guinea-Bissau_(Copernicus_2026-05-05).webp?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tidal_landscapes_of_the_Bijag%C3%B3s_Archipelago,_Guinea-Bissau_(Copernicus_2026-05-05).webp",
                "credit": "European Union, Copernicus Sentinel-2 imagery · Attribution",
                "caption": "El archipiélago de los Bijagós visto por Sentinel-2 (Copernicus, 2026).",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Chelonia_mydas_183369049.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Chelonia_mydas_183369049.jpg",
                "credit": "Marius Burger · CC0",
                "caption": "Tortuga verde (Chelonia mydas), la especie que anida en Poilão (foto de la especie, no del lugar).",
            },
        ],
    ),
    dict(
        n=11, name="Isla de Rubane y Bijagós del sur", cat="Costa", prio="Media",
        dog="por confirmar", time="1–2 noches",
        lat=11.3036452, lon=-15.8033595,  # Google Maps: Ponta Anchaca (Rubane)
        desc="Rubane está frente a Bubaque, al otro lado de un estrecho canal, con 165 habitantes (2009) y un solo alojamiento de lujo, Ponta Anchaca, sobre una playa de arena blanca donde se come marisco a unos 15.000 CFA. Es la puerta hacia el sur del archipiélago: Canhabaque (isla tradicional de iniciaciones), Kéré (campamento de pesca francés) y los parques de Orango y João Vieira-Poilão. Todo se mueve en lancha y depende del mar; en lluvias muchas travesías se suspenden.",
        dog_note="Isla privada-hotelera (Ponta Anchaca) sin política publicada; el resto del sur son islas sagradas o parques con normas IBAP.",
        visit={
            "why": "Descanso de playa de calidad a 10 minutos de Bubaque y punto de salida de excursiones en lancha por el sur.",
            "see": "Playa de Ponta Anchaca, manglares del canal, aldeas bijagó de Canhabaque, pesca deportiva en Kéré.",
            "access": "Lancha del hotel desde Bubaque o directa desde Bisáu (Consulmar/hoteles). El pin marca el lodge Ponta Anchaca. Los 4x4 se quedan en Bisáu. Respetar los espacios sagrados donde solo entran sacerdotisas.",
            "when": "Noviembre-abril.",
            "skip": "Si el presupuesto es de campamento: Rubane es el tramo caro del archipiélago; alternativas Bubaque (Mango Lodge) o casa comunitaria de Anôr.",
        },
        links=[
            {"label": "Rubane (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Rubane"},
            {"label": "Guía Bijagós · Scoot West Africa", "url": "https://scootwestafrica.com/guide-bijagos-islands-guinea-bissau/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Hotel_Ecolodge_Ponta_Anchaca_05.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Hotel_Ecolodge_Ponta_Anchaca_05.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "Playa frente al ecolodge de Ponta Anchaca, isla de Rubane.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bubaque_Rubane_view.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bubaque_Rubane_view.jpg",
                "credit": "Mooonswimmer · CC BY-SA 4.0",
                "caption": "Rubane vista desde Bubaque.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Hotel_Ecolodge_Ponta_Anchaca_04.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Hotel_Ecolodge_Ponta_Anchaca_04.jpg",
                "credit": "Joehawkins · CC BY-SA 4.0",
                "caption": "La playa del ecolodge de Ponta Anchaca.",
            },
        ],
    ),
    dict(
        n=12, name="Bafatá · ciudad colonial y casa de Amílcar Cabral", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=12.1650608, lon=-14.6613326,  # Google Maps: Casa Amílcar Cabral (Bafatá)
        desc="Segunda ciudad histórica del interior, fundada a mediados del XIX por el comerciante mandinga Malam Santi a orillas del Geba (su nombre significa «el río está lleno»); el presidio de Geba se trasladó aquí en 1906 y fue villa en 1913. Aquí nació AMÍLCAR CABRAL el 12 de septiembre de 1924. Su casa natal se anunció como museo en 2017 y el proyecto sigue sin cerrarse: comprobar in situ. Calle principal de fachadas coloniales, catedral, mercado y muelle sobre un río que se seca hasta el barro en la estación seca. Gasolina y pensiones básicas.",
        dog_note="Paseo urbano y ribera del Geba sin restricción; la casa-museo (si abre) es interior.",
        visit={
            "why": "Parada lógica en la N1 hacia Gabú y Guinea, con la referencia biográfica del padre de la independencia.",
            "see": "Casa de Cabral, avenida colonial con soportales, catedral, mercado, orilla del Geba.",
            "access": "Asfalto N1 desde Bisáu (unos 150 km por Mansoa y Bambadinca). El pin marca la casa de Cabral en el centro; aparcar en la avenida principal. Horario de la casa-museo no publicado: puede estar cerrada o en obras.",
            "when": "Mañana; en lluvias el Geba luce lleno.",
            "skip": "Si no interesa la historia de la independencia: Bafatá es sobre todo una parada de servicios.",
        },
        links=[
            {"label": "Bafatá (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bafat%C3%A1"},
            {"label": "Casa de Cabral · noticia UCCLA 2017", "url": "https://www.uccla.pt/noticias/governo-guineense-vai-recuperar-casa-de-amilcar-cabral-para-fazer-museu"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Birth_house_of_Am%C3%ADlcar_Cabral,_Bafat%C3%A1_1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Birth_house_of_Am%C3%ADlcar_Cabral,_Bafat%C3%A1_1.jpg",
                "credit": "Jcornelius · CC BY-SA 4.0",
                "caption": "Casa natal de Amílcar Cabral, Bafatá.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bafat%C3%A1_cathedral,_Bafat%C3%A1,_Guinea-Bissau_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bafat%C3%A1_cathedral,_Bafat%C3%A1,_Guinea-Bissau_2.jpg",
                "credit": "Jcornelius · CC BY-SA 4.0",
                "caption": "Catedral de Bafatá.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Birth_house_of_Am%C3%ADlcar_Cabral,_Bafat%C3%A1_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Birth_house_of_Am%C3%ADlcar_Cabral,_Bafat%C3%A1_2.jpg",
                "credit": "Jcornelius · CC BY-SA 4.0",
                "caption": "Casa natal de Amílcar Cabral (detalle).",
            },
        ],
    ),
    dict(
        n=13, name="Gabú · capital del este y el reino de Kaabu", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=12.2766525, lon=-14.2211956,  # Google Maps: Mercado de Gabu Ferra Sinhu
        desc="Mayor ciudad del este (37.525 hab. en 2010), antigua Nova Lamego colonial y capital de la región de Gabú, de mayoría fula y musulmana. Hereda el nombre del reino mandinga de KAABU (1537-1867), que dominó desde aquí Casamance y Gambia hasta que el ejército del Fouta Djalon arrasó su capital Kansala en 1867 tras un sitio de once días en que el mansaba hizo estallar la pólvora. Hoy es mercado de frontera con Senegal y Guinea y última ciudad con gasolina y bancos antes de las pistas hacia Koundara (Guinea) o Pirada (Senegal).",
        dog_note="Ciudad musulmana fula: perro atado y fuera del mercado y de las mezquitas.",
        visit={
            "why": "Punto de servicios y de historia mandinga; enlaza con la ruta 2027 por Kalifourou/Pirada si algún día se autoriza el país.",
            "see": "Gran mercado con productos de Senegal, Guinea y Costa de Marfil; mezquitas; el yacimiento de Kansala (12.53639, -14.19472, unos 28 km al norte, excavado por primera vez en 2024) para quien busque el mito.",
            "access": "Asfalto N1 desde Bafatá (unos 50 km). El pin marca el mercado central; aparcamiento en la calle o en el hotel. Kansala: sin señalización ni infraestructura de visita documentada; acceso POR CONFIRMAR.",
            "when": "Día de mercado por la mañana.",
            "skip": "Si no se sale de Guinea-Bisáu por el este, no hay motivo para llegar hasta aquí.",
        },
        links=[
            {"label": "Gabú (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Gab%C3%BA"},
            {"label": "Reino de Kaabu (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Kaabu"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Gabumainstreet.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Gabumainstreet.jpg",
                "credit": "(WT-en) Pis bus at English Wikivoyage · Public domain",
                "caption": "Calle principal de Gabú.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/20130613-DSC_9092_(9294085582).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:20130613-DSC_9092_(9294085582).jpg",
                "credit": "jbdodane · CC BY 2.0",
                "caption": "Casas en Piche, en la carretera Gabú–Koundara hacia Guinea.",
            },
        ],
    ),
    dict(
        n=14, name="Saltinho · cascadas del río Corubal", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=11.6181794, lon=-14.6868626,  # Google Maps: Pousada de Saltinho (junto al puente)
        desc="Rápidos y saltos del Corubal, el gran río que baja del Fouta Djalon (unos 560 km), donde el agua se despeña sobre gradas de roca junto al puente de arco de hormigón General Craveiro Lopes (1955). Está a 175 km por carretera al sureste de Bisáu, en el cruce de la N1 hacia Guinea. El antiguo cuartel portugués de la guerra colonial es hoy la POUSADA DO SALTINHO (habitaciones ~20.000 CFA y comidas), el único sitio del interior donde dormir con el ruido del agua. Baño solo en las pozas laterales: en agosto el río pasa de 1.600 m³/s.",
        dog_note="Río con corriente fuerte y posibles cocodrilos e hipopótamos aguas abajo (Cufada): correa en la orilla.",
        visit={
            "why": "El paisaje fluvial más fotogénico del país y la parada natural entre Bafatá/Gabú y el sur (Cufada, Cantanhez).",
            "see": "Cascadas y rápidos, puente de 1955, lavanderas y bañistas locales, bosque de galería; posible hipopótamo aguas abajo hacia Cufada.",
            "access": "Asfalto: N1 desde Bafatá o Bambadinca hacia Quebo; el pin marca el puente, y la pousada queda en la orilla junto a él. Aparcamiento amplio en el recinto del antiguo cuartel; overlanders han acampado en el hotel de la cascada. Unas 3 h desde Bisáu.",
            "when": "Octubre-diciembre: mucha agua y ya sin lluvias; en abril-mayo el caudal cae a mínimos.",
            "skip": "En plena estación seca tardía, cuando los saltos se reducen a hilos entre rocas.",
        },
        links=[
            {"label": "Saltinho (Wikipedia de)", "url": "https://de.wikipedia.org/wiki/Saltinho_(Guinea-Bissau)"},
            {"label": "Río Corubal (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Corubal_River"},
            {"label": "Pousada do Saltinho · listado IBAP", "url": "https://ecoturismo.ibapgbissau.org/pnlc.html"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Saltinho_brug_(Guin%C3%A9e-Bissau).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Saltinho_brug_(Guin%C3%A9e-Bissau).jpg",
                "credit": "Gadogado123 · CC BY-SA 4.0",
                "caption": "Puente de Saltinho sobre el Corubal.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/DSC_3152_Rio_curubal,_Saltinho_Guine-Bissau.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:DSC_3152_Rio_curubal,_Saltinho_Guine-Bissau.jpg",
                "credit": "Danilo Vaz · CC BY-SA 4.0",
                "caption": "Los rápidos del Corubal en Saltinho.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/DSC_7187_Rio_Corubal,_Saltinho_Guin%C3%A9-Bissau.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:DSC_7187_Rio_Corubal,_Saltinho_Guin%C3%A9-Bissau.jpg",
                "credit": "Danilo Vaz · CC BY-SA 4.0",
                "caption": "El Corubal en Saltinho.",
            },
        ],
    ),
    dict(
        n=15, name="Parque nacional de Cantanhez · chimpancés", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=11.2750327, lon=-14.9856176,  # Google Maps: Parque Nacional Bosques de Cantanhez
        desc="Creado el 1 de octubre de 2007, 1.057 km² de selva semihúmeda, sabana y manglar en la orilla del río Cacine, en el extremo sur del país: el último bosque tropical de Guinea-Bisáu y refugio de CHIMPANCÉS OCCIDENTALES estudiados internacionalmente, además de búfalos, colobos, elefantes en tránsito y aves (IBA). Base en la aldea de Iemberém (Jemberém), a unos 250 km de Bisáu, con campamento ecoturístico del parque y guías locales; la salida para ver chimpancés empieza antes del amanecer. Los últimos 60 km son pista forestal difícil.",
        dog_note="Parque nacional con chimpancés (riesgo de transmisión de enfermedades), búfalos y elefantes; seguimiento a pie con guía. Sin perro.",
        visit={
            "why": "Chimpancés salvajes sin vallas, en una selva que casi nadie visita, con el cuartel de Guiledje (guerra de liberación) al lado.",
            "see": "Chimpancés bajando de los nidos (a unos 150 m), colobos, búfalos, bosques sagrados de Lautchandé, manglares de Canamina, museo de la cantera colonial de Balana-Guiledje, isla de Melo.",
            "access": "Asfalto hasta Buba/Quebo y después unos 60 km de pista forestal lenta hasta Iemberém (4x4; en lluvias puede cortarse: un overlander tuvo que dar la vuelta en un vado). Sede del parque y tasas en Iemberém o IBAP Bisáu; guías, canoas y bicicletas de alquiler. El pin marca Iemberém (coordenadas del parque). Aparcamiento en el campamento. Canadá señala posibles minas en la región de Tombali fuera de las pistas.",
            "when": "Noviembre-mayo; salidas al alba.",
            "skip": "En estación de lluvias (mayo-noviembre, hasta 2.600 mm) la pista es impracticable.",
        },
        links=[
            {"label": "Parque Nacional de Cantanhez · IBAP ecoturismo", "url": "https://ecoturismo.ibapgbissau.org/pnc.html"},
            {"label": "Cantanhez (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Cantanhez_Forests_National_Park"},
            {"label": "Visita a Cantanhez · Kumakonda", "url": "https://kumakonda.com/visiting-the-cantanhez-national-park-in-guinea-bissau/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Papilio_sosia_-_Ricardo_Lima_-_242547321.jpeg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Papilio_sosia_-_Ricardo_Lima_-_242547321.jpeg",
                "credit": "Ricardo Lima · CC0",
                "caption": "Papilio sosia en Jemberém, dentro del parque de Cantanhez (iNaturalist, 2022).",
            },
        ],
    ),
    dict(
        n=16, name="Lagunas de Cufada · parque natural (Ramsar)", cat="Naturaleza", prio="Media",
        dog="prohibido", time="medio día",
        lat=11.7120253, lon=-15.0791228,  # Google Maps: Parque natural de las Lagunas de Cufada
        desc="Sitio Ramsar desde el 14 de mayo de 1990 y parque natural desde el 1 de diciembre de 2000: 890 km² entre el Corubal y la carretera Buba–Fulacunda, con las lagunas de Cufada, Bionra y Bedasse, la MAYOR LAGUNA DE AGUA DULCE DEL PAÍS. Hipopótamos, manatíes, cocodrilos enanos, antílopes, primates, 54 mamíferos y 337 aves (flamencos y acuáticas). La sede está en Buba: allí se contrata guía y se pagan las tasas. Recorridos: bosques de Bacar Conté por la orilla del Corubal (1,5 h, hipopótamos y macareo) y canoa hasta el mirador de la laguna (3 h).",
        dog_note="Hipopótamos y cocodrilos en las lagunas y en el Corubal; excursiones en canoa y a pie con guía IBAP.",
        visit={
            "why": "El único sitio del continente donde ver hipopótamos con relativa facilidad, de camino entre Saltinho y Cantanhez.",
            "see": "Laguna de Cufada desde el mirador, hipopótamos del Corubal, aves acuáticas, 33 tabancas de la carretera Buba-Fulacunda.",
            "access": "Asfalto N2 hasta Buba; el pin marca la sede del parque en Buba (información, tasas y guías). Pistas de tierra hacia las lagunas al noroeste; en lluvias, canoa. Alojamiento en Buba (Pousada Bela Vista, Berço do Rio, Buba Hotel) o campamentos turísticos del parque.",
            "when": "Estación seca, con marea favorable para el macareo del Corubal.",
            "skip": "Si ya se han visto hipopótamos en Orango y falta tiempo para Cantanhez.",
        },
        links=[
            {"label": "PN Lagoas de Cufada · IBAP ecoturismo", "url": "https://ecoturismo.ibapgbissau.org/pnlc.html"},
            {"label": "PNLC · IBAP", "url": "https://ibapgbissau.org/pnlc-ap/"},
            {"label": "Lagoas de Cufada (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Lagoas_de_Cufada_Natural_Park"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Earth_from_Space-_Guinea-Bissau_ESA523998.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Earth_from_Space-_Guinea-Bissau_ESA523998.jpg",
                "credit": "European Space Agency · Attribution",
                "caption": "El estuario del Geba y el sur de Guinea-Bisáu por Sentinel-2 (ESA); las lagunas de Cufada quedan al sur del río.",
            },
        ],
    ),
    dict(
        n=17, name="Buba y el estuario del Rio Grande de Buba", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=11.5920466, lon=-14.9943814,  # Google Maps: Buba
        desc="Capital de la región de Quinara, a 223 km de Bisáu, en el fondo del estuario del Rio Grande de Buba, una ría de aguas tranquilas famosa por la pesca. Factoría portuguesa desde 1670 (Bolola), centro de la trata (unos 3.000 esclavos al año hacia 1625) y PRIMER CENTRO COMERCIAL DE LA GUINEA PORTUGUESA entre 1840 y 1870, hasta el hundimiento del cacahuete. Kumba Yalá quiso trasladar aquí la capital y Angola proyectó un puerto de bauxita, parado tras el golpe de 2012. Base de servicios para Cufada y Cantanhez, con pousadas junto al río.",
        dog_note="Pueblo y ribera sin restricción; atado por el ganado y los cocodrilos del estuario.",
        visit={
            "why": "Última ciudad con gasolina y camas antes de las pistas del sur, y una ría fotogénica donde se pesca barracuda.",
            "see": "Estuario y embarcadero, mercado biafada-mandinga, Pousada Bela Vista sobre el río, sede del parque de Cufada.",
            "access": "Asfalto N2 desde Bambadinca/Saltinho y desde Bisáu por Enxudé o por el norte. El pin marca el centro de Buba; las pousadas están en la orilla. Aparcamiento en los alojamientos.",
            "when": "Atardecer en la ría; estación seca.",
            "skip": "Si Cufada y Cantanhez quedan fuera del plan, Buba no justifica la desviación.",
        },
        links=[
            {"label": "Buba (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Buba"},
            {"label": "Buba (Wikipédia pt)", "url": "https://pt.wikipedia.org/wiki/Buba"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Harbour_of_Buba,_Guinea-Bissau.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Harbour_of_Buba,_Guinea-Bissau.jpg",
                "credit": "Jcornelius · CC BY-SA 4.0",
                "caption": "Puerto de Buba sobre el Rio Grande.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/DSC_6003_Rio_Buba,_Quinara_,_Guin%C3%A9-Bissau.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:DSC_6003_Rio_Buba,_Quinara_,_Guin%C3%A9-Bissau.jpg",
                "credit": "Danilo Vaz · CC BY-SA 4.0",
                "caption": "El Rio Grande de Buba, región de Quinara.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Colonial_building_in_Buba,_Guinea-Bissau.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Colonial_building_in_Buba,_Guinea-Bissau.jpg",
                "credit": "Jcornelius · CC BY-SA 4.0",
                "caption": "Edificio colonial en Buba.",
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
    ("Paso fronterizo Mpack–São Domingos (Djegue)", "Frontera", 12.4100993, -16.1963248,  # Google Maps: São Domingos (el puesto de Djegue no figura como objeto; Mpak en el lado senegalés)
     "Principal paso con Senegal (Casamance). Cierra 12:30–13:30 y desde 18:00 (MAEC). Visado NO fiable aquí. Pin comprobado en Google Maps («São Domingos (el puesto de Djegue no figura como objeto; Mpak en el lado senegalés)»)."),
    ("Paso fronterizo de Pirada (Senegal, Kolda)", "Frontera", 12.6615335, -14.1495096,  # Google Maps: Pirada
     "Puesto con visado a la llegada según Wikipedia; estado 2025-26 por confirmar. Pin comprobado en Google Maps («Pirada»)."),
    ("Paso fronterizo Buruntuma–Kandika (Guinea)", "Frontera", 12.4536227, -13.6974889,  # Google Maps: Buruntuma
     "Pista muy mala a ambos lados; salida fácil sin tasas (2019). Pin comprobado en Google Maps («Buruntuma»)."),
    ("Aeropuerto Internacional Osvaldo Vieira (OXB)", "Frontera", 11.8888675, -15.6511506,  # Google Maps: Aeropuerto Internacional Osvaldo Vieira
     "TAP Lisboa, Royal Air Maroc, Air Senegal, Air Côte d'Ivoire, ASKY. Visado a la llegada teórico. Pin comprobado en Google Maps («Aeropuerto Internacional Osvaldo Vieira»)."),
    ("Puerto Pidjiguiti / Porto Cais – ferry Consulmar a Bijagós", "Frontera", 11.8598207, -15.5767391,  # Google Maps: Porto de Bissau
     "Embarque del ferry a Bubaque/Enxudé; oficina Consulmar en Av. 3 de Agosto 40, tel. +245 969 02 55 55. Pin comprobado en Google Maps («Porto de Bissau»)."),
    ("Embajada de España en Bissau", "Consular", 11.8638703, -15.5849111,  # Google Maps: Presidential Palace, Bissau (Praça dos Heróis Nacionais; la embajada no figura como objeto)
     "Praça dos Heróis Nacionais s/n. Tel. +245 966 72 22 46 (embajada), +245 966 87 51 52 (consular), EMERGENCIA +245 966 001 010. bissau-em@maec.es. L–V 9:00–14:00. Pin comprobado en Google Maps («Presidential Palace, Bissau (Praça dos Heróis Nacionais; la embajada no figura como objeto)»)."),
    ("Hospital Nacional Simão Mendes", "Hospital", 11.8640669, -15.5800472,  # Google Maps: Hospital Nacional Simão Mendes
     "Hospital nacional de referencia (>500 camas en 2018); medios muy limitados; para lo grave, evacuación a Dakar. Pin comprobado en Google Maps («Hospital Nacional Simão Mendes»)."),
    ("Hospital de Cumura", "Hospital", 11.8513572, -15.6371393,  # Google Maps: Hospital de Cumura
     "Hospital misionero citado por el MAEC como referencia; coordenadas aproximadas (Cumura, sector de Prábis): verificar. Pin comprobado en Google Maps («Hospital de Cumura»)."),
    ("Gasolineras de Bissau (eje Av. 14 de Novembro / Bissalanca)", "Combustible", 11.8582419, -15.5802533,  # Google Maps: Petromar (Avenida Amílcar Cabral)
     "Diésel ~700 XOF/l (mar-2026). Llenar en Bissau antes de salir a pista; también en Bafatá y Gabú. Punto orientativo, verificar en Maps. Pin comprobado en Google Maps («Petromar (Avenida Amílcar Cabral)»)."),
    ("Agua: hoteles y lodges de Bissau", "Agua potable", 11.8592645, -15.5904585,  # Google Maps: Hotel CEIBA (Avenida Francisco Mendes)
     "Agua corriente no potable; llenar depósitos de ducha en hotel y beber embotellada/filtrada. Punto orientativo, sin fuente concreta. Pin comprobado en Google Maps («Hotel CEIBA (Avenida Francisco Mendes)»)."),
]

DRONE_CALLOUT = ("warn", "Sin ley de drones, pero «no permitidos» a visitantes",
                 "Guinea-Bisáu no tiene normativa específica de drones. Los portales especializados (drone-laws.com, 14-1-2026; UAV Coach 2023) indican que los vuelos de visitantes extranjeros no están permitidos y que la confiscación en aduana es imprevisible: «unos oficiales confiscan y otros no». El MAEC, FCDO y Canadá no mencionan drones. Con una junta militar en el poder y cuarteles en el centro de Bissau, la recomendación de la app es no llevarlo o dejarlo precintado y declarado en la aduana de entrada.")

STARLINK_CALLOUT = ("", "Starlink operativo desde junio de 2025",
                    "Guinea-Bisáu es el 23.º mercado africano de Starlink: licencia provisional de la ARN-TIC en diciembre de 2024, aprobación final en abril de 2025 y lanzamiento el 18 de junio de 2025 (Technext, Connecting Africa). Kit estándar 228.000 XOF y cuota 36.000 XOF/mes; kit Mini 117.000 XOF con plan de 250 GB a 18.000 XOF. Un terminal en roaming registrado en España debería funcionar; el mapa oficial de starlink.com no se pudo leer en esta sesión, así que la cobertura efectiva en Bijagós queda por confirmar.")

DOG_MATRIX = [
    ("Frontera São Domingos (Casamance)", "por confirmar", "Presentar pasaporte UE + certificado <7 días; si el aduanero pide permiso previo, volver a Ziguinchor y dormir en Senegal."),
    ("Bissau ciudad", "permitido con condiciones", "Perro siempre con correa y en el coche en controles; muchos perros callejeros: no soltar."),
    ("Bijagós (Bubaque, Orango, João Vieira)", "no recomendado", "Ferry sin política de mascotas conocida y parques nacionales IBAP: dejar el perro con un cuidador en Bissau o no ir."),
    ("Parques nacionales (Cantanhez, Cacheu, Orango)", "por confirmar", "Consultar al IBAP en Bissau; asumir prohibición dentro de los parques."),
    ("Pistas del interior (Bafatá, Gabú, Oio)", "no recomendado", "Riesgo de minas y UXO fuera del asfalto: el perro no sale del vehículo salvo en zonas pisadas."),
    ("Alojamientos", "por confirmar", "Preguntar antes en cada lodge; acampar en recinto vigilado con el perro dentro del coche."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje Guinea-Bisáu (actualizado 19-3-2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Guinea%20Bissau"),
    ("MAEC · Ficha País Guinea-Bisáu (PDF, diciembre 2018)", "https://www.exteriores.gob.es/Documents/FichasPais/GUINEABISSAU_FICHA%20PAIS.pdf"),
    ("MAEC · Embajada de España en Bissau: horario, localización y contacto (2026)", "https://www.exteriores.gob.es/Embajadas/bissau/es/Embajada/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx"),
    ("MAEC · Embajada en Bissau: Viajar a Guinea-Bisáu (índice)", "https://www.exteriores.gob.es/Embajadas/bissau/es/ViajarA"),
    ("Wikipedia · 2026 Guinea-Bissau general election", "https://en.wikipedia.org/wiki/2026_Guinea-Bissau_general_election"),
    ("Africanews · Guinea-Bissau votes 'yes' in referendum for new constitution (2-9-2026)", "https://www.africanews.com/2026/09/02/guinea-bissau-votes-yes-in-referendum-for-new-constitution/"),
    ("GlobalSecurity.org · Guinea-Bissau Politics 2025", "https://www.globalsecurity.org/military/world/africa/gnb-politics-2025.htm"),
    ("Vanguard/AFP · G.Bissau military announces reopening of borders following coup (nov-2025)", "https://www.vanguardngr.com/2025/11/g-bissau-military-announces-reopening-of-borders-following-coup/"),
    ("APA News · ECOWAS suspends Guinea-Bissau from all decision-making bodies (1-12-2025)", "https://apanews.net/ecowas-suspends-guinea-bissau-from-all-decision-making-bodies/"),
    ("Freedom House · Freedom in the World 2026: Guinea-Bissau", "https://freedomhouse.org/country/guinea-bissau/freedom-world/2026"),
    ("FCDO · Guinea-Bissau travel advice (10-12-2025, vigente 14-8-2026)", "https://www.gov.uk/foreign-travel-advice/guinea-bissau"),
    ("FCDO · Guinea-Bissau safety and security", "https://www.gov.uk/foreign-travel-advice/guinea-bissau/safety-and-security"),
    ("FCDO · Guinea-Bissau warnings and insurance", "https://www.gov.uk/foreign-travel-advice/guinea-bissau/warnings-and-insurance"),
    ("Gobierno de Canadá · Travel advice Guinea-Bissau (9-9-2026)", "https://travel.gc.ca/destinations/guinea-bissau"),
    ("TravelHealthPro/NaTHNaC · Guinea-Bissau (rev. ene-2024)", "https://travelhealthpro.org.uk/country/98/guinea-bissau"),
    ("Wikipedia · Visa policy of Guinea-Bissau", "https://en.wikipedia.org/wiki/Visa_policy_of_Guinea-Bissau"),
    ("Mind of a Hitchhiker · Getting the Guinea-Bissau visa in Ziguinchor (marzo 2025)", "https://mindofahitchhiker.com/getting-the-guinea-bissau-visa-in-ziguinchor-senegal/"),
    ("Tripadvisor · Visa on Arrival Senegal border? (foro)", "https://www.tripadvisor.com/ShowTopic-g293800-i9390-k14896239-Visa_on_Arrival_Senegal_boder-Guinea_Bissau.html"),
    ("Tripadvisor · Ferry schedule to Bubaque Island (foro, 2025)", "https://www.tripadvisor.com/ShowTopic-g293800-i9390-k14944973-Ferry_schedule_to_Bubaque_Island-Guinea_Bissau.html"),
    ("The Sightseer's Syllabus · Gambia to Bissau overland (2025)", "https://thesightseersyllabus.com/gambia-to-bissau-overland-a-step-by-step-guide/"),
    ("carnetdepassage.org · Guinea-Bissau", "https://www.carnetdepassage.org/country/guinea-bissau"),
    ("Horizons Unlimited · Carnet de Passages: list of countries", "https://www.horizonsunlimited.com/node/2399"),
    ("WikiOverland · Guinea-Bissau (agosto 2016)", "http://wikioverland.org/Guinea-Bissau"),
    ("The Road Chose Me · Into Guinea-Bissau (2016)", "http://theroadchoseme.com/into-guinea-bissau"),
    ("Overlandbirds · Bissau to Conakry border Buruntuma (marzo 2019)", "https://www.overlandbirds.com/bissau-to-conakry-border-buruntuma/"),
    ("Scoot West Africa · Do you need a carnet de passage to overland West Africa? (2023)", "https://scootwestafrica.com/carnet-de-passage-overlanding/"),
    ("Scoot West Africa · ECOWAS Brown Card insurance (act. 2023)", "https://scootwestafrica.com/insurance-for-vehicles-traveling-west-africa/"),
    ("Scoot West Africa · Visiting the Bijagós Islands (act. 9-5-2025)", "https://scootwestafrica.com/guide-bijagos-islands-guinea-bissau/"),
    ("OFESAUTO · Carta Verde", "https://www.ofesauto.es/carta-verde/"),
    ("drone-laws.com · Guinea-Bissau drone laws (14-1-2026)", "https://drone-laws.com/drone-laws-in-guinea-bissau/"),
    ("UAV Coach · Drone laws in Guinea Bissau (2023)", "https://uavcoach.com/drone-laws-in-guinea-bissau/"),
    ("Technext · Starlink goes live in Guinea-Bissau (18-6-2025)", "https://technext24.com/2025/06/18/starlink-goes-live-in-guinea-bissau/"),
    ("Connecting Africa · Starlink enters Guinea-Bissau (19-6-2025)", "https://www.connectingafrica.com/connectivity/starlink-enters-guinea-bissau"),
    ("Consulmar · Ferry routes Bissau–Bijagós", "https://www.consulmarbissau.com/en/ferry-routes-bissau-bijagos-bubaque-orango"),
    ("Consulmar · Boat timetable (semana 38/2026)", "https://consulmarbissau.com/en/boat-timetable-bissau-bijagos-bubaque-bolama-enxude"),
    ("AfroFuel · Fuel prices Guinea-Bissau (1-3-2026)", "https://afrotools.com/fr/tools/suivi-carburant/guinea-bissau/"),
    ("EUR-Lex · Reglamento de Ejecución (UE) 2026/636 (listas de terceros países, aplicable 22-4-2026)", "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202600636"),
    ("EUR-Lex · Reglamento Delegado (UE) 2026/131 (20-1-2026)", "https://eur-lex.europa.eu/eli/reg_del/2026/131/oj"),
    ("MAPA · Viajar con la mascota: perros, gatos, hurones (act. 12-8-2026)", "https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones"),
    ("DGAV (Portugal) · Exportação para países terceiros: animais", "https://www.dgav.pt/comerciointernacional/conteudo/exportacao-para-paises-terceiros/animais/"),
    ("Portal do Governo da Guiné-Bissau · Ministérios", "https://bissaugov.com/ministerios"),
    ("Wikipedia · Osvaldo Vieira International Airport", "https://en.wikipedia.org/wiki/Osvaldo_Vieira_International_Airport"),
    ("Wikipedia · São Domingos (Guinea-Bissau)", "https://en.wikipedia.org/wiki/S%C3%A3o_Domingos_(Guinea-Bissau)"),
    ("Wikipedia · Hospital Nacional Simão Mendes", "https://en.wikipedia.org/wiki/Hospital_Nacional_Sim%C3%A3o_Mendes"),
    ("GeoNames · Pirada (GW)", "https://www.geonames.org/search.html?q=pirada&country=GW"),
    ("GeoNames · Buruntuma (GW)", "https://www.geonames.org/search.html?q=buruntuma&country=GW"),
    ("Prepaid Data SIM Card Wiki · Guinea-Bissau (operadores y tarifas, sin fecha)", "https://prepaid-data-sim-card.fandom.com/wiki/Guinea-Bissau"),
    ("Fortaleza de Amura (Wikipedia)", "https://en.wikipedia.org/wiki/Fortaleza_de_S%C3%A3o_Jos%C3%A9_da_Amura"),
    ("Bissau (Wikivoyage)", "https://en.wikivoyage.org/wiki/Bissau"),
    ("MAEC · recomendaciones Guinea-Bissau", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Guinea-Bissau"),
    ("Quinhamel (Wikipedia)", "https://en.wikipedia.org/wiki/Quinhamel"),
    ("Mar Azul Lodge (Tripadvisor)", "https://www.tripadvisor.com/Hotel_Review-g2282953-d2516322-Reviews-Mar_Azul_Lodge-Quinhamel_Biombo_Region.html"),
    ("Cacheu (Wikipedia)", "https://en.wikipedia.org/wiki/Cacheu"),
    ("Memorial da Escravatura (Wikipédia pt)", "https://pt.wikipedia.org/wiki/Memorial_da_Escravatura_e_do_Tr%C3%A1fico_Negreiro"),
    ("Parque dos Tarrafes do Rio Cacheu · IBAP ecoturismo", "https://ecoturismo.ibapgbissau.org/pntc.html"),
    ("Cacheu River Mangroves NP (Wikipedia)", "https://en.wikipedia.org/wiki/Cacheu_River_Mangroves_Natural_Park"),
    ("Varela (Wikipedia de)", "https://de.wikipedia.org/wiki/Varela_(Guinea-Bissau)"),
    ("Varela beach · Travel Tomorrow", "https://traveltomorrow.com/guinea-bissau-varela-beach-a-madness-worthwhile/"),
    ("Canchungo (Wikipedia)", "https://en.wikipedia.org/wiki/Canchungo"),
    ("Bolama (Wikipedia)", "https://en.wikipedia.org/wiki/Bolama_(town)"),
    ("Bolama · Consulmar Travel", "https://www.consulmartravel.com/en/bolama-colonial-history-and-traditions-on-an-island-with-charm/"),
    ("UNESCO · Bijagós – Omatí Minhô", "https://whc.unesco.org/en/list/1431/"),
    ("Reserva da Biosfera Bolama-Bijagós · IBAP", "https://ecoturismo.ibapgbissau.org/rbabb.html"),
    ("Bubaque (Wikipedia)", "https://en.wikipedia.org/wiki/Bubaque"),
    ("Parque Nacional de Orango · IBAP ecoturismo", "https://ecoturismo.ibapgbissau.org/pno.html"),
    ("Orango Parque Hotel · hipopótamos", "https://www.orangohotel.com/en/hippos-on-the-island-of-orango-guinea-bissau/"),
    ("Orango NP (Wikipedia)", "https://en.wikipedia.org/wiki/Orango_Islands_National_Park"),
    ("PNM João Vieira e Poilão · IBAP ecoturismo", "https://ecoturismo.ibapgbissau.org/pnmjvp.html"),
    ("João Vieira–Poilão (Wikipedia)", "https://en.wikipedia.org/wiki/Jo%C3%A3o_Vieira_and_Poil%C3%A3o_Marine_National_Park"),
    ("Rubane (Wikipedia)", "https://en.wikipedia.org/wiki/Rubane"),
    ("Bafatá (Wikipedia)", "https://en.wikipedia.org/wiki/Bafat%C3%A1"),
    ("Casa de Cabral · noticia UCCLA 2017", "https://www.uccla.pt/noticias/governo-guineense-vai-recuperar-casa-de-amilcar-cabral-para-fazer-museu"),
    ("Gabú (Wikipedia)", "https://en.wikipedia.org/wiki/Gab%C3%BA"),
    ("Reino de Kaabu (Wikipedia)", "https://en.wikipedia.org/wiki/Kaabu"),
    ("Saltinho (Wikipedia de)", "https://de.wikipedia.org/wiki/Saltinho_(Guinea-Bissau)"),
    ("Río Corubal (Wikipedia)", "https://en.wikipedia.org/wiki/Corubal_River"),
    ("Pousada do Saltinho · listado IBAP", "https://ecoturismo.ibapgbissau.org/pnlc.html"),
    ("Parque Nacional de Cantanhez · IBAP ecoturismo", "https://ecoturismo.ibapgbissau.org/pnc.html"),
    ("Cantanhez (Wikipedia)", "https://en.wikipedia.org/wiki/Cantanhez_Forests_National_Park"),
    ("Visita a Cantanhez · Kumakonda", "https://kumakonda.com/visiting-the-cantanhez-national-park-in-guinea-bissau/"),
    ("PNLC · IBAP", "https://ibapgbissau.org/pnlc-ap/"),
    ("Lagoas de Cufada (Wikipedia)", "https://en.wikipedia.org/wiki/Lagoas_de_Cufada_Natural_Park"),
    ("Buba (Wikipedia)", "https://en.wikipedia.org/wiki/Buba"),
    ("Buba (Wikipédia pt)", "https://pt.wikipedia.org/wiki/Buba"),
]

# Casamance → São Domingos → Cacheu/Varela → Bisáu → Bafatá → Gabú → Saltinho → Buba → Cantanhez
CORRIDOR = [
    (12.4101, -16.19632),
    (12.27326, -16.16692),
    (12.06722, -16.03333),
    (12.10389, -15.70806),
    (11.86047, -15.57886),
    (11.87223, -15.87561),
    (11.86047, -15.57886),
    (12.033, -14.867),
    (12.16506, -14.66133),
    (12.27665, -14.2212),
    (12.16506, -14.66133),
    (11.61818, -14.68686),
    (11.59205, -14.99438),
    (11.71203, -15.07912),
    (11.28333, -15.25),
    (11.27503, -14.98562),
]

# Escapada Casamance–Varela–Cacheu (bucle norte, 2-3 días)
CORRIDOR_ALT = [
    (12.4101, -16.19632),
    (12.28625, -16.59454),
    (12.4101, -16.19632),
    (12.06722, -16.03333),
    (12.27326, -16.16692),
    (12.06722, -16.03333),
    (12.4101, -16.19632),
]

HISTORIA_RESUMEN = "Guinea-Bisáu es un pequeño país atlántico encajado entre Senegal y Guinea, heredero del reino mandinga de Kaabu y de cuatro siglos de presencia portuguesa que hasta principios del siglo XX apenas pasó de las factorías de Cacheu y Bissau. Proclamó unilateralmente su independencia en 1973, tras diez años de guerra dirigida por el PAIGC de Amílcar Cabral, y Portugal la reconoció en 1974. Desde entonces ha encadenado golpes de Estado, una guerra civil y una sucesión de gobiernos efímeros, con el narcotráfico como telón de fondo. A fecha de septiembre de 2026 lo gobierna una junta militar surgida del golpe del 26 de noviembre de 2025, que ha convocado elecciones para el 6 de diciembre de 2026. La ruta 2027 lo evita; esta ficha es informativa."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>El territorio de la actual Guinea-Bisáu estuvo habitado durante al menos un milenio por cazadores-recolectores y, después, por agricultores animistas, según la <em>Encyclopaedia Britannica</em>. A partir del siglo XIII la expansión del Imperio de Malí empujó a parte de esos pueblos hacia la costa y mezcló a otros con los mandé. De esa expansión nació el reino de <strong>Kaabu</strong> —Gabú en las fuentes españolas—, fundado en la década de 1230 como provincia de Malí por Tiramakhan Traoré. Cuando Malí decayó, Kaabu se independizó hacia 1537 y fue el Estado mandinga más poderoso del oeste: una federación de reinos gobernada por la élite guerrera <em>nyancho</em>, no musulmana y enriquecida con los cautivos de sus guerras, según Wikipedia en inglés. Su capital, Kansala, estaba en el nordeste del país actual.</p><p>Los fula, pastores seminómadas, llegaron desde el siglo XII, pero solo en el siglo XV en grandes números. La rivalidad terminó en 1867 en la batalla de Kansala: tras once días de asedio, las fuerzas fula de Alfa Molo derrotaron a los mandinga y de las ruinas de Kaabu surgió el Estado de Fuladu. En la costa y las islas vivían pueblos ajenos a esos reinos —balantas, papeles, manjacos y, en el archipiélago, los bijagós— que resistieron a los poderes continentales hasta el siglo XX. Esa mezcla de sabana musulmana y costa animista sigue definiendo el país.</p>"),
    ("Colonización",
     "<p>El primer europeo documentado, el navegante portugués Nuno Tristão, murió en 1446 o 1447 a manos de los habitantes de la costa, según Britannica. Portugal instaló factorías más que colonias: Cacheu se fundó en 1588 y Bissau se levantó como fortaleza a finales del siglo XVII, de acuerdo con Wikipedia en español. Durante siglos el negocio fue la trata: decenas de miles de guineanos fueron llevados a Cabo Verde para trabajar en sus plantaciones y vendidos en los barracones de Cacheu, Bissau y Bolama a los <em>lançados</em> y a las <em>senhoras</em>, comerciantes de ascendencia mixta. Cabo Verde y Guinea se administraron juntas hasta 1879, cuando pasaron a ser colonias separadas, y en mayo de 1886 Portugal cedió Casamance a Francia, lo que fijó la frontera actual con Senegal.</p><p>El control efectivo del interior llegó tarde y con violencia. Las campañas de «pacificación» dirigidas por el capitán João Teixeira Pinto entre 1913 y 1915 aplastaron la resistencia continental, y aún hubo otras tres campañas mayores, la última en enero de 1936, año en que también fueron sometidas las islas Bijagós, según Wikipedia en inglés. La Guinea portuguesa quedó como una colonia pobre y sin apenas colonos. Lo que dejó Portugal fue el idioma oficial, una lengua criolla que hoy habla la mayoría, las ciudades-fuerte del litoral y una economía de exportación agraria que apenas ha cambiado de naturaleza.</p>"),
    ("Independencia y construcción del Estado",
     "<p>En 1956 un grupo de caboverdianos, con Amílcar Cabral al frente, fundó el Partido Africano para la Independencia de Guinea y Cabo Verde, el <strong>PAIGC</strong>. En agosto de 1959 la represión de una huelga de estibadores en el muelle de Pidjiguiti, en Bissau, dejó numerosos muertos y convenció al partido de que solo cabía la vía armada. La guerra empezó en enero de 1963. Cabral fue asesinado el 20 de enero de 1973, pero el 24 de septiembre de ese año el PAIGC proclamó la independencia; la revolución de Lisboa del 25 de abril de 1974 llevó a Portugal a reconocerla el 10 de septiembre de 1974, según Britannica y Wikipedia.</p><p>Luís Cabral, hermano de Amílcar, fue el primer presidente, en la órbita soviética según la Ficha País del MAEC. El 14 de noviembre de 1980 João Bernardo «Nino» Vieira lo derrocó y rompió la unidad con Cabo Verde. Vieira gobernó como hombre fuerte hasta la apertura al multipartidismo: en 1994 se celebraron las primeras elecciones libres, que el PAIGC ganó y Vieira revalidó por poco. En 1998 destituyó al jefe militar Ansumane Mané, que se sublevó; la guerra civil de 1998-1999 acabó con la rendición de Vieira en mayo de 1999 y su exilio en Portugal. Kumba Ialá, del Partido de Renovación Social, ganó en enero de 2000 y fue el primer presidente ajeno al PAIGC.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>Ialá, cada vez más represivo, cayó en un golpe incruento el 14 de septiembre de 2003. Vieira volvió del exilio y ganó las presidenciales de 2005, pero el 2 de marzo de 2009 fue asesinado por soldados que lo culpaban de la muerte, horas antes, del jefe del Ejército, Tagme Na Waie. Es el periodo que el MAEC llama la «Narcorrepública» (2000-2010) por el tránsito de cocaína. Malam Bacai Sanhá ganó en julio de 2009 y murió en el cargo en enero de 2012; el 12 de abril un nuevo golpe abrió una transición que cerraron las elecciones de mayo de 2014, ganadas por José Mário Vaz con el 61,9 % de los votos. Hasta 2019 se sucedieron siete gobiernos, según el MAEC.</p><p>Umaro Sissoco Embaló, del MADEM-G15, venció en la segunda vuelta del 29 de diciembre de 2019 y tomó posesión en febrero de 2020 con el resultado en disputa. Sobrevivió a un intento de golpe el 1 de febrero de 2022, disolvió la Asamblea Nacional Popular en mayo de 2022, convocó legislativas para junio de 2023 y volvió a disolverla en diciembre de 2023 tras un choque armado entre la Guardia Nacional y el Ejército. Las generales se celebraron el 23 de noviembre de 2025 y, el 26, un día antes de anunciarse los resultados, los militares tomaron el poder.</p>"),
    ("Política y gobierno en 2026",
     "<p>A fecha de septiembre de 2026, según la Ficha País del MAEC (abril de 2026), Guinea-Bisáu vive bajo una <strong>junta militar</strong>. El Alto Mando Militar designó presidente de transición al general Horta Inta-a Na Man y primer ministro a Ilídio Vieira Té. La Carta de Transición fija un año máximo y veta a ambos como candidatos. Embaló se exilió y el opositor Domingos Simões Pereira fue detenido, según Wikipedia en inglés. Por decreto del 21 de enero de 2026 se convocaron presidenciales y legislativas para el <strong>6 de diciembre de 2026</strong>, y el 30 de agosto un referéndum boicoteado por la oposición aprobó, con el 70,42 % de los votos, una constitución presidencialista que reduce el Parlamento de 102 a 65 escaños.</p><p>Formalmente es una república semipresidencialista, pero Freedom House 2025 la clasificaba ya antes del golpe como «Partly Free» con 41 sobre 100; hoy es en la práctica un régimen militar de transición. Reporteros Sin Fronteras la sitúa en el puesto 100 de 180 en 2026. El MAEC recomienda «viajar con precaución» (19 de marzo de 2026), con riesgo alto en la frontera norte por guerrilla residual y bandidaje. España tiene embajada en Bissau desde 2007 y es el primer inversor privado del país; la UE es su principal socio de cooperación, con 107 millones de euros para 2021-2027.</p>"),
    ("Economía y recursos",
     "<p>Guinea-Bisáu es uno de los países más pobres del mundo: la Ficha País del MAEC cifra el PIB en unos 2.100 millones de dólares en 2024, el PIB per cápita en 953 dólares corrientes y el índice de desarrollo humano en 0,514, puesto 174. Casi todo depende del <strong>anacardo</strong>, alrededor del 80 % de las exportaciones, con campañas algo por encima de las 150.000 toneladas vendidas en bruto sobre todo a la India (56,8 % de las exportaciones en 2023). Le siguen la madera sin procesar, hacia Portugal y China, y la pesca, regulada con la UE por un protocolo 2024-2029 de 17 millones de euros anuales.</p><p>La moneda es el franco CFA de la UEMOA, con paridad fija de 655,957 francos por euro. El crecimiento ronda el 5 % anual (4,8 % en 2024), pero la inflación fue del 7,2 % ese año y la deuda pública ronda el 80 % del PIB. El país vive de la ayuda exterior y, en la sombra, del tránsito de cocaína que le valió desde mediados de la década de 2000 la etiqueta de «narcoestado», según Wikipedia en inglés. En las fuentes consultadas no constan grandes proyectos mineros ni petroleros; el MAEC destaca la agroindustria del anacardo y el maracuyá, y advierte de que cajeros y pago con tarjeta son escasos.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>El país tiene 2,2 millones de habitantes (Banco Mundial, 2024) en 36.125 kilómetros cuadrados, según el MAEC. Los grupos principales son fula (25,5 %), balanta (19,3 %) y mandinga (17,8 %), según Wikipedia en inglés. El idioma oficial es el portugués, pero la lengua de todos es el <strong>criollo</strong> guineano, hablado por el 90 % de la población; por carretera hacia Senegal o Guinea se sale adelante con francés, criollo y algo de portugués. En religión las fuentes discrepan: el MAEC da 45,1 % de musulmanes, 22,1 % de cristianos y 14,9 % de animistas; Wikipedia en inglés (2025) da 49,6 % y 37,8 %.</p><p>La música nacional es el <em>gumbé</em>, cantado en criollo; se come arroz en la costa y mijo en el interior, y el carnaval paraliza Bissau tres días. El único bien Patrimonio Mundial, inscrito por la UNESCO en 2025, son los ecosistemas costeros y marinos del archipiélago de los Bijagós – Omatí Minhô, con hipopótamos en agua salada y playas de anidación de tortugas. Para quien viaja: ropa discreta en el interior musulmán, pedir permiso antes de fotografiar y respetar los espacios rituales de las islas; el alcohol se vende en Bissau, pero en el ramadán de 2027, desde el 8 de febrero aproximadamente, conviene no comer ni beber en público en zonas musulmanas. Fiebre amarilla obligatoria y visado en origen, según el MAEC.</p>"),
]

HISTORIA_FUENTES = [
    ("MAEC España · Ficha País Guinea-Bissau (PDF) · abril de 2026", "https://www.exteriores.gob.es/Documents/FichasPais/GUINEA-BISSAU_FICHA%20PAIS.pdf"),
    ("MAEC España · Recomendaciones de viaje Guinea-Bissau · 19 de marzo de 2026", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Guinea-Bissau"),
    ("Freedom House · Guinea-Bissau, Freedom in the World 2025", "https://freedomhouse.org/country/guinea-bissau/freedom-world/2025"),
    ("Britannica · Guinea-Bissau, History (precolonial y colonial)", "https://www.britannica.com/place/Guinea-Bissau/History"),
    ("Britannica · Guinea-Bissau, Independence (1974–2025)", "https://www.britannica.com/place/Guinea-Bissau/Independence"),
    ("Wikipedia (es) · Guinea-Bisáu", "https://es.wikipedia.org/wiki/Guinea-Bisáu"),
    ("Wikipedia (en) · Guinea-Bissau", "https://en.wikipedia.org/wiki/Guinea-Bissau"),
    ("Wikipedia (en) · History of Guinea-Bissau", "https://en.wikipedia.org/wiki/History_of_Guinea-Bissau"),
    ("Wikipedia (en) · Kaabu", "https://en.wikipedia.org/wiki/Kaabu"),
    ("Wikipedia (en) · Kumba Ialá", "https://en.wikipedia.org/wiki/Kumba_Ial%C3%A1"),
    ("Wikipedia (en) · 2025 Guinea-Bissau coup d'état", "https://en.wikipedia.org/wiki/2025_Guinea-Bissau_coup_d%27%C3%A9tat"),
    ("Wikipedia (en) · 2026 Guinea-Bissau general election", "https://en.wikipedia.org/wiki/2026_Guinea-Bissau_general_election"),
    ("Wikipedia (en) · 2026 Guinea-Bissau constitutional referendum", "https://en.wikipedia.org/wiki/2026_Guinea-Bissau_constitutional_referendum"),
    ("Wikipedia (en) · Bijagós Islands", "https://en.wikipedia.org/wiki/Bijag%C3%B3s_Islands"),
    ("Wikipedia (pt) · Guiné-Bissau", "https://pt.wikipedia.org/wiki/Guin%C3%A9-Bissau"),
    ("UNESCO World Heritage Centre · Guinea-Bissau (Estado parte)", "https://whc.unesco.org/en/statesparties/gw"),
    ("UNESCO World Heritage Centre · Coastal and Marine Ecosystems of the Bijagós Archipelago – Omatí Minhô (2025)", "https://whc.unesco.org/en/list/1431/"),
    ("Reporteros Sin Fronteras · Guinea-Bissau, índice 2025 y 2026", "https://rsf.org/en/country/guinea-bissau"),
    ("Africa Center for Strategic Studies · Guinea-Bissau Constitutional Referendum: An Explainer · 26 de agosto de 2026", "https://africacenter.org/spotlight/guinea-bissau-constitutional-referendum-explainer/"),
    ("Al Jazeera · Vote count starts in Guinea-Bissau referendum · 30 de agosto de 2026", "https://www.aljazeera.com/news/2026/8/30/vote-count-starts-in-guinea-bissau-referendum-on-strengthening-presidency"),
]

SPEC = dict(
    slug="guinea-bisau", name="Guinea-Bisáu", revision="18 sep 2026",
    sub="EXCLUIDO POR PROTOCOLO — junta militar desde noviembre de 2025 · ficha informativa (Casamance–São Domingos y Bijagós)",
    chips=[
        ("ESTATUS", "EXCLUIDO POR PROTOCOLO. Junta militar desde el 26-11-2025; suspendido de CEDEAO y UA…"),
        ("CÓMO LLEGAR", "Por tierra desde Casamance (Ziguinchor–Mpack–São Domingos, principal paso)…"),
        ("VISADO", "OBLIGATORIO para españoles. Embajada en Madrid (Av…"),
        ("VEHÍCULO", "Sin CPD el aduanero emite un passavant de 2 semanas (2.500 XOF, relatos 2016)…"),
        ("SEGURIDAD", "Junta militar · minas fuera de Bissau · no de noche"),
        ("SEGURO", "Carta Verde NO · Carte Brune CEDEAO obligatoria"),
        ("SALUD", "Fiebre amarilla OBLIGATORIA · malaria alta todo el año"),
        ("DRONES", "Sin ley · visitantes no autorizados · confiscación"),
        ("STARLINK", "Operativo desde jun-2025 · 36.000 XOF/mes"),
        ("4x4", "Asfalto roto · pistas · lluvias jun–oct intransitables"),
        ("A PIE", "Bissau de día sí · Bijagós solo sin coche"),
        ("PERRO", "MAEC: identificación, vacuna antirrábica y certificado internacional de salud de MENOS DE UNA SEMANA…"),
        ("MONEDA", "Franco CFA de África Occidental (XOF, 1 € = 655,957 XOF fijo)…"),
        ("VENTANA", "Lluvias de junio a octubre: muchas pistas intransitables (MAEC)…"),
    ],
    center=[11.64, -15.41], zoom=7,
    notice="Documento de planificación de un país EXCLUIDO POR PROTOCOLO: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Casamance → São Domingos → Cacheu/Varela → Bisáu → Bafatá → Gabú → Saltinho → Buba → Cantanhez",
    corridor_alt_label="Escapada Casamance–Varela–Cacheu (bucle norte, 2-3 días)",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Lagoa_com_hipop%C3%B3tamos_01.jpg?width=1200",
    hero_credit="Parque nacional de Orango · Joehawkins · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Guinea-Bisáu queda fuera de la ruta 2027 por protocolo: el 26 de noviembre de 2025 el ejército anuló las elecciones del 23 de noviembre y entregó el poder a una junta («Alto Mando Militar para la Restauración del Orden») presidida por el general Horta Inta-A Na Man; la CEDEAO y la Unión Africana suspendieron al país (1 de diciembre de 2025), un referéndum constitucional del 30 de agosto de 2026 amplió los poderes presidenciales y las elecciones están convocadas para el 6 de diciembre de 2026 (Wikipedia, Africanews, APA). El MAEC (19 de marzo de 2026) habla de «nueva etapa de inestabilidad institucional y política» y Freedom House 2026 lo califica «Parcialmente libre» (33/100). Es el noveno golpe consumado desde 1974: la inestabilidad es estructural, no coyuntural. La ruta Senegal→Guinea por Kalifourou–Sambaïlo lo evita. Si algún día se planteara un desvío, la opción realista sería una escapada de 4–6 días desde Ziguinchor por Mpack–São Domingos hasta Bissau (unos 130 km, asfalto degradado) con visado obtenido ANTES en el consulado de Ziguinchor (25.000 XOF/30 días en 2025), passavant aduanero de 2 semanas (2.500 XOF en relatos antiguos) y Carte Brune CEDEAO; a los Bijagós solo se iría sin coches (ferry o lancha, 16.500–30.000 XOF por persona). Coste orientativo del desvío: 400–700 € por vehículo sin contar Bijagós. Habría que decidir: resultado y aceptación de las elecciones de diciembre de 2026, situación de la frontera norte (Casamance) y si compensa el riesgo con perro y dos vehículos.",
    facts=[
        ("Estatus", "EXCLUIDO POR PROTOCOLO. Junta militar desde el 26-11-2025; suspendido de CEDEAO y UA; elecciones previstas el 6-12-2026. MAEC: «viajar con precaución»; Canadá: evitar la franja de 20 km junto a Senegal."),
        ("Cómo llegar", "Por tierra desde Casamance (Ziguinchor–Mpack–São Domingos, principal paso), desde Tambacounda/Vélingara por Pirada, o desde Guinea por Buruntuma–Kandika. Avión: aeropuerto Osvaldo Vieira (OXB) con TAP Lisboa, Royal Air Maroc, Air Senegal, ASKY."),
        ("Visado", "OBLIGATORIO para españoles. Embajada en Madrid (Av. de América 16) o consulado de Ziguinchor (25.000 XOF/30 días, en el día, 2025). eVisa paralizada; visado en frontera terrestre NO fiable (MAEC)."),
        ("Vehículo/aduana", "Sin CPD el aduanero emite un passavant de 2 semanas (2.500 XOF, relatos 2016); con CPD debería sellarse gratis, pero los relatos describen confusión del personal. Conducción por la DERECHA; MAEC exige permiso internacional; Canadá dice que no lo reconoce (3 meses con carné propio)."),
        ("Seguro", "Carta Verde española NO cubre. Obligatorio seguro RC de zona CEDEAO (Carte Brune), que se compra en Senegal (CNART) o en frontera; 10.000–20.000 XOF/mes por vehículo en relatos."),
        ("Moneda", "Franco CFA de África Occidental (XOF, 1 € = 655,957 XOF fijo). EUR/USD se cambian en bancos; cajeros escasos fuera de Bissau."),
        ("Perro", "MAEC: identificación, vacuna antirrábica y certificado internacional de salud de MENOS DE UNA SEMANA. Sin web oficial veterinaria localizada. Vuelta a la UE: país NO listado → titulación antirrábica anotada en el pasaporte antes de salir."),
        ("Drones", "Sin normativa específica; portales especializados (ene-2026) indican que los vuelos de visitantes extranjeros NO están permitidos y que la confiscación en aduana es imprevisible. Autoridad: aviación civil (ANSAC/DGAC)."),
        ("Starlink", "OPERATIVO desde el 18 de junio de 2025 (licencia ARN-TIC dic-2024/abr-2025). Kit 228.000 XOF, cuota 36.000 XOF/mes; mini 117.000 XOF."),
        ("Seguridad", "Sin atentados terroristas registrados; robos nocturnos, carteristas, bandidaje en carretera y controles frecuentes. Minas/UXO fuera de Bissau (Bafatá, Biombo, Oio). Frontera norte: cruzar solo por la mañana."),
        ("Clima", "Lluvias de junio a octubre: muchas pistas intransitables (MAEC). Seca de noviembre a mayo, la ventana lógica para cualquier desvío."),
        ("Sanidad", "Fiebre amarilla OBLIGATORIA (>1 año). Malaria de alto riesgo todo el año y todo el país. Sanidad «gravemente deficiente»: seguro con evacuación imprescindible. Referencia: Hospital Nacional Simão Mendes y Hospital de Cumura."),
    ],
    alerts=[
        "GOLPE DE ESTADO del 26 de noviembre de 2025: junta militar, elecciones anuladas, país suspendido de CEDEAO y UA; transición de un año con elecciones el 6-12-2026. Cualquier desvío se decide DESPUÉS de conocer el resultado y su aceptación.",
        "Visado obligatorio y NO fiable en frontera terrestre (MAEC, mar-2026): obtenerlo antes en Madrid o en Ziguinchor. La web de eVisa está paralizada.",
        "Frontera norte con Casamance: cierra entre 12:30 y 13:30 y de 18:00 hasta la mañana; cruzar SIEMPRE por la mañana (MAEC).",
        "Canadá (9-9-2026) desaconseja los viajes no esenciales a menos de 20 km de la frontera con Senegal por restos del conflicto de Casamance y minas.",
        "Minas y UXO fuera de Bissau (Bafatá, Biombo, Oio; FCDO y Canadá): no salir del asfalto ni acampar en descampados no usados.",
        "Fiebre amarilla OBLIGATORIA con certificado; malaria de alto riesgo todo el año (TravelHealthPro).",
        "Sanidad «gravemente deficiente» en todo el país (MAEC): seguro con evacuación y botiquín completo.",
        "Carreteras en «muy malas condiciones» y sin iluminación; NUNCA conducir de noche. Junio–octubre muchas pistas intransitables.",
        "Sobornos en controles policiales «extremadamente comunes» (WikiOverland, The Road Chose Me): extintor, triángulos y chalecos a mano, paciencia y no pagar.",
        "Bijagós: no usar piraguas tradicionales (MAEC); ferry irregular (avisos de «en mantenimiento» en 2025). Sin vehículos: los 4x4 se quedan en Bissau.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 17 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Ziguinchor – São Domingos – Varela", "Mpack/Jegue, asfalto a São Domingos, 53 km de pista a Varela", "~110 km · 1 día"),
        ("2 · Varela – Cacheu", "Pista de vuelta a São Domingos, asfalto a Canchungo y Cacheu; fuerte y memorial", "~130 km · 1 día"),
        ("3 · Cacheu – Bisáu", "Canchungo, Bula, N3 a la capital; Amura y Bissau Velho", "~130 km · 1 día"),
        ("4 · Bisáu – Quinhámel – Bisáu", "Costa de Biombo y Mar Azul; regreso o lancha a Bijagós", "~70 km · 1 día"),
        ("5 · Bijagós (Bubaque, Orango, Rubane)", "Ferry/lancha desde Bisáu; coches en la capital", "0 km · 3–4 días"),
        ("6 · Bisáu – Bafatá – Gabú", "N1 por Mansoa y Bambadinca; casa de Cabral; mercado de Gabú", "~210 km · 1 día"),
        ("7 · Gabú – Saltinho", "Regreso a Bambadinca y N1 sur hasta el puente del Corubal", "~150 km · 1 día"),
        ("8 · Saltinho – Buba – Cufada", "N2 vía Quebo; sede del parque y salida a las lagunas", "~90 km · 1 día"),
        ("9 · Buba – Iemberém (Cantanhez)", "Asfalto a Catió y ~60 km de pista forestal; chimpancés al alba", "~120 km · 2 días"),
        ("10 · Iemberém – Bisáu", "Regreso por Buba, Bambadinca y N1 (o Enxudé–ferry)", "~300 km · 1–2 días"),
        ("11 · Bisáu – São Domingos – Ziguinchor", "Salida por el mismo paso; cruzar por la mañana", "~150 km · 1 día"),
    ],
    offroad=[
        "Las carreteras principales (N1 Bisáu–Bafatá–Gabú, N3 a São Domingos, N2 a Buba) están asfaltadas y en buen estado según overlanders (WikiOverland 2016 y The Road Chose Me: «main highways are extremely good – without even potholes»); los controles policiales se repiten cada ~100 km y piden seguro, extintor, triángulo y limpiaparabrisas.",
        "Pista de laterita São Domingos–Susana–Varela: 53 km sin asfaltar, apta para 4x4, lenta y embarrada en lluvias; único acceso a la mejor playa continental (Wikipedia de, Travel Tomorrow).",
        "Pista final a Cantanhez: unos 60 km de pista forestal desde el asfalto de Catió/Quebo hasta Iemberém, «terrible pero hermosa» (Kumakonda); un overlander tuvo que dar media vuelta en un vado cerca de Quebo en la estación húmeda (The Road Chose Me). Solo estación seca.",
        "Pista Enxudé–São João (acceso a Bolama): 30 km de pista que se estrecha a senda de arbustos, hasta 4 h en camión (blog 2019); solo tiene sentido en el vehículo local, los 4x4 se quedan en Bisáu.",
        "Zonas vetadas: pistas secundarias de la franja fronteriza con Casamance (MAEC: guerrilla residual y bandidaje; Canadá: evitar viajes no esenciales a menos de 20 km de la frontera con Senegal) y todo lo que salga de la pista marcada en Bafatá, Biombo, Oio, Quinara y Tombali por restos de minas (Canadá, FCDO). No conducir de noche (FCDO).",
        "Pistas de los parques (Cufada, Cantanhez, Tarrafes del Cacheu) requieren guía local y pago de tasas en la sede IBAP correspondiente (Buba, Iemberém, Cacheu); las islas del parque de Orango cobran 5.000 CFA/día.",
        "Salida al este hacia Guinea (Gabú–Pirada o Gabú–Buruntuma–Koundara) y al sur (Quebo–Boké): sin fuentes abiertas en esta sesión sobre el estado actual de la pista; POR CONFIRMAR con Tracks4Africa/iOverlander.",
        "Ferry de vehículos: Consulmar Bisáu–Enxudé (lunes-sábado 08:00) admite carga; no hay ferry de vehículos a Bubaque ni a Bolama. Un cruce con los dos 4x4 a Enxudé acortaría el viaje al sur (Buba) solo si se confirma la rampa y la tarifa de carga.",
    ],
    senderismo=[
        "Volta de Bissau: circuito a pie de unas 4 h por el casco viejo, el puerto de Pidjiguiti y la fortaleza de Amura (Wikivoyage Bissau).",
        "Praia de Varela: caminata de varios km por la playa abierta al Atlántico, desde la playa de pescadores hasta las dunas, con la laguna de nenúfares y pelícanos detrás (Travel Tomorrow); marea baja.",
        "Cacheu: paseo por el fuerte, el memorial y el embarcadero, y circuito guiado por los bosques sagrados y aldeas felupe del parque de los Tarrafes (IBAP PNTC).",
        "Orango: caminata de unos 20 min desde el hotel a la primera laguna de Anôr con guía local; ruta larga Eticoga–Anôr de 12 km a pie por sabana y arrozales (IBAP PNO, Orango Parque Hotel).",
        "Cantanhez: ruta de Lautchandé (bosque denso, chimpancés, búfalos, colobos) al amanecer; ruta de Canamina (manglares y primates); Balana-Guiledje (cantera colonial y museos de la guerra); Ilha de Melo para aves (IBAP PNC).",
        "Cufada: pista de los bosques de Bacar Conté por la orilla del Corubal, ~1,5 h, con hipopótamos y macareo; canoa hasta el mirador de la laguna, ~3 h con picnic (IBAP PNLC).",
        "Saltinho: paseo por las rocas y pozas de los rápidos y el puente de 1955 (Wikipedia de); no vadear el cauce principal.",
        "Bolama: recorrido a pie por la ciudad colonial abandonada (palacio del gobernador, avenidas, monumento al hidroavión) y senderos a las playas y manglares de la isla (Wikipedia, Consulmar Travel).",
    ],
    acampada=[
        "No hay campings formales en el país. WikiOverland (2016): acampada en hoteles y recintos por 2.000-5.000 CFA/persona; acampada libre posible en zonas rurales, pero fuera de la franja de Casamance y de las áreas con minas (Canadá, FCDO).",
        "The Road Chose Me: durmió gratis en el aparcamiento de un hotel-restaurante italiano cerrado por lluvias en la costa cerca de Bisáu (permiso del guarda), en el hotel de la cascada de Saltinho y en un hotel de Bisáu mientras esperaba visado.",
        "Pousada do Saltinho (+245 955 99 88 00): antiguo cuartel con recinto amplio junto al puente; habitaciones ~20.000 CFA; es el sitio natural para dos 4x4 en el interior.",
        "Buba: Pousada Bela Vista y Berço do Rio junto al estuario; IBAP menciona «vários acampamentos turísticos» dentro del parque de Cufada.",
        "Iemberém (Cantanhez): campamento ecoturístico del parque / Camp U'Anan con bungalós y comidas; casas comunitarias en Guiledje, Faro Sadjuma y Cabudo (IBAP).",
        "Varela: Aparthotel Chez Hélène, Avó Anisa y Casa Aberta Kasumayaku; acampada en la playa no documentada.",
        "Quinhámel: Mar Azul Lodge figura en iOverlander como hotel (ficha no legible sin sesión); preguntar por aparcar y dormir en el vehículo.",
        "Bijagós: sin coche; lodges de 20.000 CFA (Mango Lodge, Bubaque) a 130 € (Orango Parque Hotel) y casa comunitaria de Anôr (Scoot West Africa, IBAP).",
    ],
    visado=[
        "ESPAÑOLES: visado OBLIGATORIO, también menores; pasaporte con 6 meses de validez (MAEC, 19-3-2026).",
        "Vía ordinaria: Sección Consular de la Embajada de Guinea-Bisáu en Madrid, Avenida de América 16, 1ª planta. Coste y plazo en Madrid: por confirmar.",
        "Vía overland: consulado en Ziguinchor (Senegal): 25.000 XOF (~40 €) por 30 días, 35.000 por 60, 40.000 por 90; pegatina en el día, sin fotos (Mind of a Hitchhiker, marzo de 2025). Teléfonos 77 531 62 28 / 77 371 66 69.",
        "eVisa: la web «en principio» existe pero su funcionamiento «se encuentra paralizado» (MAEC); Wikipedia: servicio suspendido.",
        "Visado a la llegada: el MAEC lo cita como posible pero «ni claro ni estable»; un foro de Tripadvisor afirma que el puesto de São Domingos NO expide visados. Wikipedia lo limita al aeropuerto y a Djegue II, Cambadju, Pirada y Buruntuma. NO contar con ello.",
        "Validez en frontera terrestre: el visado de Ziguinchor se acepta en São Domingos (relatos 2016–2025). Tasa de entrada informal de 1.000 XOF en 2025 (The Sightseer's Syllabus).",
    ],
    fronteras_rows=[
        ("Paso terrestre principal (Senegal/Casamance)", "Mpack (SN) – Djegue/São Domingos (GW)", "Abierto: MAEC (mar-2026) lo describe con horario partido (cierra 12:30–13:30 y a partir de 18:00). Relato de paso a pie/taxi en marzo de 2025. Visado NO expedido aquí según foro. Fuente: MAEC, Mind of a Hitchhiker 2025."),
        ("Paso terrestre secundario (Senegal, Kolda/Vélingara)", "Pirada (región de Gabú)", "Listado por Wikipedia como puesto con visado a la llegada. Estado 2025-26 y horario: POR CONFIRMAR (sin relato reciente)."),
        ("Paso terrestre con Guinea", "Buruntuma (GW) – Kandika (GN)", "Pista en mal estado a ambos lados; salida de GW «muy fácil» sin tasas (Overlandbirds, marzo 2019). Estado 2025-26: POR CONFIRMAR."),
        ("Aeropuerto internacional", "Osvaldo Vieira (OXB), Bissalanca", "TAP Lisboa, Royal Air Maroc, Air Senegal, Air Côte d'Ivoire, ASKY; Turkish Airlines pospuso su ruta (feb-2026). Visado a la llegada teóricamente posible. Fuente: Wikipedia."),
        ("Puerto / ferry Bijagós", "Porto Cais (Pidjiguiti), Bissau → Bubaque", "Consulmar: viernes Bissau→Bubaque, vuelta domingo; 3–4 h según marea; 16.500 XOF/persona; avisos de «ferry en mantenimiento» en 2025. Solo pasajeros. Fuente: consulmarbissau.com (sem. 38/2026), Tripadvisor 2025."),
        ("Cierre general de fronteras", "Todas (tierra, aire, mar)", "Cerradas el 26-11-2025 por la junta y reabiertas al día siguiente (Vanguard/AFP). Sin cierres posteriores conocidos, pero un nuevo cierre súbito es un riesgo real."),
    ],
    vehiculos=[
        "Conducción por la DERECHA. Carné español + PERMISO INTERNACIONAL (MAEC lo exige; Canadá afirma que el país no lo reconoce y admite el carné nacional 3 meses). Llevar ambos.",
        "Aduana: sin CPD se emite un passavant/permiso de importación temporal de 2 semanas por 2.500 XOF, prorrogable en Bissau (WikiOverland 2016, The Road Chose Me 2016). Con CPD debería ser gratis, pero en Buruntuma (2019) el personal no sabía qué hacer con él. carnetdepassage.org solo indica que no hay club emisor en el país.",
        "Seguro: la Carta Verde española NO cubre Guinea-Bisáu (OFESAUTO). El MAEC exige seguro de la zona CEDEAO (Carte Brune), que se compra en Senegal (CNART) o en cualquier aseguradora local; 10.000–20.000 XOF/mes por vehículo (relatos), 25.000 XOF/año para moto (Scoot West Africa 2023).",
        "Documentación del vehículo: permiso de circulación original (FCDO cita la «vehicle registration card» como requisito). Fotocopias para los controles.",
        "Controles policiales frecuentes con intentos de extorsión (extintor, limpiaparabrisas, triángulos): llevar todo en regla y no pagar (The Road Chose Me 2016).",
        "Carreteras: asfalto degradado en los ejes Bissau–São Domingos y Bissau–Gabú; últimos km a Buruntuma en pista destrozada (10 h Bissau–Koundara en 2019). Sin conducción nocturna.",
        "Combustible: todas las ciudades tienen gasolinera y siempre hay gasolina (WikiOverland); diésel a 700 XOF/l (mar-2026). Repostar en Bissau, Bafatá y Gabú antes de salir a pista.",
        "Bijagós: el ferry Consulmar es solo de pasajeros y carga; los vehículos se dejan en Bissau (parking de hotel vigilado, por confirmar).",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autoridad: aviación civil de Guinea-Bisáu (ANSAC/DGAC, tel. +245 44 325 64 75 según drone-laws.com; sin web). No hay reglamento publicado: se aplican criterios OACI por defecto.",
        "drone-laws.com (14-1-2026): «los vuelos de drones de visitantes extranjeros no están permitidos»; permiso exigido a >25 kg o uso comercial.",
        "UAV Coach: sin leyes localizadas; la ausencia de normativa «puede significar que las autoridades se opongan al uso de drones, sobre todo por turistas»; confiscación en aduana aleatoria.",
        "Fuentes oficiales españolas, británicas y canadienses NO citan drones: el vacío legal juega en contra del viajero ante militares y policía.",
        "Si se lleva: nunca sobre Bissau, cuarteles, puerto, aeropuerto ni fronteras; en Bijagós pedir permiso al jefe de aldea y al IBAP en parques.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Disponible desde el 18-6-2025 con venta directa en starlink.com; velocidades anunciadas de hasta 150 Mbps (Technext, 18-6-2025).",
        "Precios locales: kit 228.000 XOF (~400 $), cuota 36.000 XOF/mes; Mini 117.000 XOF y plan 250 GB a 18.000 XOF/mes (Connecting Africa, 19-6-2025).",
        "Penetración de internet del 32,5 % (ene-2025): fuera de Bissau la cobertura móvil es pobre; Starlink es la única conexión fiable en pista y en Bijagós.",
        "Operadores móviles: Orange Bissau (52 % de cuota, 4G LTE en banda 3) y MTN (cobertura algo menor, 4G «difícil de encontrar»). SIM Orange 1.000 XOF, MTN 500 XOF, sin registro de pasaporte; datos Orange hasta 75 GB/mes por 50.000 XOF (Prepaid Data SIM Card Wiki, sin fecha; confirmar en tienda oficial).",
    ],
    perro_intro=[
        "ENTRADA (MAEC, 19-3-2026): el animal debe ir identificado, vacunado contra la rabia y con certificado internacional de buena salud de NO MÁS DE UNA SEMANA de antigüedad. No hay más detalle oficial.",
        "No se localizó página oficial de los servicios veterinarios de Guinea-Bisáu (Ministério da Agricultura e Desenvolvimento Rural / Direcção Geral da Pecuária); el portal bissaugov.com solo da un correo genérico (geral@gov.gw). Permiso previo de importación y razas prohibidas: POR CONFIRMAR.",
        "Certificado práctico: pasaporte UE + certificado oficial de exportación español emitido por el veterinario oficial (Sanidad Exterior/CCAA) en los 7 días previos; en Senegal, hacer uno nuevo con un veterinario en Ziguinchor si el de España ha caducado.",
        "RABIA: TravelHealthPro considera la rabia «un riesgo» con casos en animales domésticos; perros callejeros abundantes en Bissau y aldeas. Vacuna del perro al día y evitar contacto.",
        "VUELTA A LA UE: Guinea-Bisáu NO figura en la lista del Reg. de Ejecución (UE) 2026/636 (ningún país de África continental lo está) → titulación de anticuerpos antirrábicos ≥0,5 UI/ml en laboratorio autorizado, muestra ≥30 días tras la vacuna, hecha en la UE ANTES de salir y anotada en el pasaporte (vía A), lo que exime de la espera de 3 meses (MAPA, 12-8-2026; Reg. Delegado (UE) 2026/131).",
        "Veterinarios: no se localizó ninguna clínica veterinaria de referencia en Bissau; farmacia veterinaria de Ianda Guiné inaugurada en 2023. Llevar antiparasitarios y medicación propia.",
        "Riesgos en el terreno: garrapatas, filaria (mosquitos todo el año), agua estancada con esquistosomiasis, calor extremo en la seca, minas fuera del asfalto.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "FIEBRE AMARILLA: certificado OBLIGATORIO para todo viajero mayor de 1 año; riesgo de transmisión en todo el país (TravelHealthPro; MAEC: «imprescindible»).",
        "MALARIA: riesgo ALTO todo el año y en todo el país; profilaxis con atovacuona-proguanil, doxiciclina o mefloquina (TravelHealthPro).",
        "Vacunas recomendadas: hepatitis A y B, tifoidea, tétanos, meningococo ACWY, triple vírica; rabia para estancias largas (TravelHealthPro, MAEC).",
        "Dengue, cólera, tifoidea y esquistosomiasis presentes (MAEC, TravelHealthPro): repelente de día, agua embotellada/filtrada, nada de baños en agua dulce.",
        "Sanidad «gravemente deficiente» en todo el país, Bissau incluida (MAEC, Canadá): seguro con EVACUACIÓN obligatorio; el hospital útil más cercano está en Dakar.",
        "Hospitales de referencia: Hospital Nacional Simão Mendes (Bissau) y Hospital de Cumura (misión, a las afueras) según MAEC.",
        "Teléfonos: policía 117, ambulancia 119, bomberos 118 (Canadá, 9-9-2026); no verificados por el MAEC, que solo da la emergencia consular.",
    ],
    seguridad_intro="Guinea-Bisáu combina baja violencia cotidiana con inestabilidad política crónica: nueve golpes consumados desde 1974, el último el 26 de noviembre de 2025, con fronteras cerradas 24 horas, toque de queda y medios suspendidos. El MAEC (19-3-2026) recomienda «viajar con precaución»; Canadá (9-9-2026) pide «alto grado de cautela» y evitar la franja de 20 km junto a Senegal; el FCDO (10-12-2025) subraya minas fuera de Bissau. Narcotráfico y corrupción condicionan policía y controles. El riesgo para un convoy overland no es el crimen, sino un cierre súbito del país.",
    seguridad=[
        "Situación política: junta militar de transición; referéndum del 30-8-2026 aprobado con el 70 % y boicot opositor; elecciones el 6-12-2026. Evitar manifestaciones y seguir medios locales (FCDO).",
        "Zonas desaconsejadas por el MAEC: carreteras secundarias de la frontera norte (restos de guerrilla y bandidaje) y barrios periféricos de Bissau de noche (Barrio Militar, Antula, Gabuzinho).",
        "Canadá: evitar viajes no esenciales a menos de 20 km de la frontera con Senegal (rebeldes de Casamance). La ruta directa Mpack–São Domingos–Ingoré es la única excepción razonable, de día.",
        "Minas y municiones sin explotar fuera de Bissau (Bafatá, Biombo, Oio): no abandonar el asfalto ni acampar fuera de recintos usados (FCDO, Canadá).",
        "Delincuencia: robos nocturnos, carteristas en mercados y aeropuerto, bandidaje en carretera y carjacking (MAEC, Canadá): puertas cerradas, nada de noche.",
        "Terrorismo: sin atentados registrados, pero riesgo regional reconocido (MAEC, FCDO).",
        "Controles policiales frecuentes con sobornos «extremadamente comunes» (WikiOverland); Freedom House cita corrupción agravada por el narcotráfico.",
        "«Timo del oro» y estafas a extranjeros en aumento (MAEC).",
        "Escoltas y permisos: no exigidos por ninguna fuente oficial abierta; en parques (IBAP) se paga entrada (5.000 XOF/día en Orango, Scoot West Africa 2025).",
    ],
    agua=[
        "El agua corriente NO es potable para visitantes (WikiOverland; TravelHealthPro: beber hervida, filtrada o embotellada).",
        "Para depósitos de ducha/lavado: grifos de hoteles y lodges en Bissau, Bubaque y Varela; en aldeas, pozos y bombas manuales (pedir permiso y filtrar). Puntos concretos en iOverlander no consultados: por confirmar.",
        "Agua embotellada disponible en Bissau, Bafatá y Gabú; escasa en pistas y en Bijagós fuera de los lodges.",
        "Esquistosomiasis y cólera presentes: no llenar depósitos de ríos ni lagunas sin filtrar y clorar.",
        "Temporada de lluvias (junio–octubre): agua abundante pero turbia; en seca, los pozos de aldea son el recurso.",
    ],
    combustible=[
        "Precios (AfroFuel, 1-3-2026): gasolina 720 XOF/l (~1,10 €), diésel 700 XOF/l (~1,07 €), GLP 900 XOF/kg; estimación de terceros, «varían por estación y proveedor».",
        "Referencia histórica: gasolina 594 y diésel 603 XOF/l en agosto de 2016 (WikiOverland).",
        "Red: «todas las ciudades tienen gasolinera y todas tienen siempre gasolina» (WikiOverland); diésel y calidad fuera de Bissau, Bafatá y Gabú: por confirmar.",
        "Racionamiento: sin noticias de escasez abiertas en esta sesión; tras el golpe de 2025 no consta desabastecimiento. Llenar en Bissau antes de cualquier pista.",
        "GlobalPetrolPrices no tiene página para Guinea-Bisáu (404 en esta sesión).",
    ],
    experiencias_intro="No hay relatos overland en vehículo propio posteriores al golpe de noviembre de 2025; los más recientes con coche son de 2019 y los de 2025 son de viajeros en transporte público. Se usan con su fecha.",
    experiencias=[
        "Visado en Ziguinchor en diez minutos (Mind of a Hitchhiker, marzo 2025): el consulado de Guinea-Bisáu en Ziguinchor expide visado pegatina de 30 días por 25.000 XOF (40 €), sin fotos ni papeles, «dentro y fuera en menos de diez minutos»; conviene ir entre 9 y 11 de la mañana y llamar antes. El viaje Mpack–São Domingos se hace en taxi colectivo y moto; la carretera se degrada a medida que uno se aleja de Senegal.",
        "Gambia–Ziguinchor–Bissau en un día (The Sightseer's Syllabus, principios de 2025): unas 10 horas y 11.650 XOF en transporte público; la frontera abre a las 7:00 y cobran tasas informales de 1.000 XOF en la salida de Senegal y en la entrada de Guinea-Bisáu, más otra «inexplicada» en Safim. Muestra que el corredor Casamance–Bissau funciona con normalidad antes del golpe.",
        "Salida por Buruntuma con Land Rover (Overlandbirds, marzo 2019): pista terrible en los últimos kilómetros a ambos lados de la frontera; trámite «muy fácil» y sin tasas, pero los aduaneros no sabían qué hacer con el CPD al no haber passavant, y les pusieron dos sellos de salida. Bissau–Koundara, 10 horas. iOverlander situaba mal el puesto (Pichè).",
        "Entrada desde Casamance con Jeep (The Road Chose Me, 2016): visado de un mes en Ziguinchor, permiso de importación temporal de dos semanas por 2.500 XOF prorrogable en Bissau, y un control policial que intentó extorsionarle con el extintor y los limpiaparabrisas; no pagó. «La selva es realmente densa aquí».",
        "Ficha WikiOverland (agosto 2016): passavant de dos semanas por 2.500 XOF (gratis con CPD), visado doble entrada de un mes por 20.000 XOF en Ziguinchor, Carte Brune a 10.000–20.000 XOF/mes, gasolina a 594 y diésel a 603 XOF/l, camping a 2.000–5.000 XOF/persona y acampada libre tolerada en zonas rurales; sobornos «extremadamente comunes».",
        "Guía de Bijagós (Scoot West Africa, actualizada mayo 2025): ferry Consulmar a Bubaque por 16.500 XOF y unas 4 horas, speedboat 30.000 XOF los viernes y domingos, canoas a 3.500 XOF; lodges de 20.000 a 120.000 XOF; Orango con hipopótamos de agua salada y entrada de parque de 5.000 XOF/día. Ningún dato sobre llevar vehículos: se quedan en Bissau.",
        "Ferry en mantenimiento (foro Tripadvisor, 2025): Consulmar anunció «ferry en mantenimiento, sin servicio hasta nuevo aviso»; antes salía los viernes a las 13:00 y volvía los domingos a las 11:00; alternativa, lancha privada por unos 500 €. El horario oficial de la semana 38 de 2026 vuelve a mostrar viernes/domingo, pero otra página de la misma empresa dice que no opera Bubaque: llamar antes.",
        "Foro Tripadvisor sobre visado en frontera (2024-2025): un residente afirma que «la oficina de inmigración de la frontera Guinea-Bisáu–Senegal no expide visados»; solo el aeropuerto y los consulados de Ziguinchor o Dakar. Coincide con el MAEC en no fiarse del visado a la llegada por tierra.",
    ],
    pendientes=[
        ("Situación política tras el 6-12-2026", "Elecciones celebradas, resultado aceptado y MAEC sin «inestabilidad» en su aviso; sin cierres de frontera en 90 días."),
        ("Visado en Madrid: coste y plazo", "Llamar/escribir a la Embajada de Guinea-Bisáu en Madrid (Av. de América 16) y anotar tarifa, plazo y validez."),
        ("Visado a la llegada en São Domingos", "Confirmación escrita de la Embajada de España o dos relatos 2026 de overlanders que lo hayan obtenido allí."),
        ("Passavant vs CPD en 2026", "Relato 2025-26 con vehículo propio en São Domingos indicando precio, días y si sellan el CPD."),
        ("Carte Brune: dónde comprarla en Ziguinchor", "Nombre de aseguradora, precio por vehículo y validez; confirmar que cubre Guinea-Bisáu."),
        ("Servicios veterinarios oficiales", "Web, correo o teléfono de la Direcção Geral da Pecuária; permiso previo y razas prohibidas."),
        ("Paso de Pirada 2025-26", "Fuente fechada que confirme apertura a extranjeros y horario."),
        ("Ferry Bissau–Bubaque", "Llamada a Consulmar (+245 969 02 55 55) confirmando día, hora, precio y política de mascotas."),
        ("Operadores móviles y SIM turística", "Página oficial de Orange Bissau o MTN confirmando precio de SIM, registro con pasaporte y paquetes 2026."),
        ("Teléfonos de emergencia 117/119/118", "Confirmación por MAEC o Embajada de España."),
        ("Cobertura Starlink en Bijagós", "Mapa oficial starlink.com abierto o relato 2026 con terminal en Bubaque."),
        ("Parking seguro en Bissau para dejar los 4x4", "Dos hoteles con parking vigilado y precio, o confirmación de la Embajada."),
    ],
    sources=SOURCES,
    sources_note="Revisión documental del 18 de septiembre de 2026 con fuentes abiertas en esta sesión; los datos de aduana y combustible proceden en parte de relatos de 2016–2019 por falta de testimonios posteriores al golpe de 2025. Esta ficha es una herramienta de planificación, no una autorización: antes de cualquier desvío hay que releer el aviso del MAEC y confirmar visado, frontera y ferry.",
    emergency="Emergencia consular Embajada de España en Bissau: +245 966 001 010 (24 h); centralita +245 966 72 22 46 y sección consular +245 966 87 51 52; bissau-em@maec.es (MAEC). Teléfonos locales según Canadá (9-9-2026): policía 117, ambulancia 119, bomberos 118; el MAEC no los publica, por confirmar. Para lo grave: evacuación a Dakar vía seguro.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

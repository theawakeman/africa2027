#!/usr/bin/env python3
"""Auditoría editorial reproducible del grupo 8: Esuatini y Lesoto.

Los pines se contrastaron uno a uno con Google Maps. Cuando Google contiene
un punto engañoso o no contiene el acceso correcto (Mkhaya), prevalece la
coordenada publicada por el gestor y la excepción queda documentada en la
auditoría manual. Las portadas representan el lugar concreto y las galerías
evitan reutilizar la misma fotografía entre PDIs.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]


def commons(filename: str, credit: str, caption: str) -> dict[str, str]:
    encoded = quote(filename.replace(" ", "_"), safe="(),-._~'")
    return {
        "img": f"https://commons.wikimedia.org/wiki/Special:FilePath/{encoded}?width=1200",
        "source": f"https://commons.wikimedia.org/wiki/File:{encoded}",
        "credit": credit,
        "caption": caption,
    }


def external(img: str, source: str, credit: str, caption: str) -> dict[str, str]:
    return {"img": img, "source": source, "credit": credit, "caption": caption}


def entry(desc: str, why: str, see: str, access: str, when: str, skip: str) -> dict:
    return {
        "desc": desc,
        "visit": {"why": why, "see": see, "access": access, "when": when, "skip": skip},
    }


COORDS = {
    "esuatini": {
        1: (-26.1925369, 31.0305069), 2: (-26.2220580, 31.0311897),
        3: (-26.1411446, 31.1175614), 4: (-26.1407413, 31.1351138),
        5: (-26.0639588, 31.2483291), 6: (-26.0693238, 31.2922655),
        7: (-25.8980625, 31.2930625), 8: (-26.3265299, 31.1409367),
        9: (-26.2615925, 31.1737208), 10: (-26.4162595, 31.1782678),
        11: (-26.4461535, 31.1623541), 12: (-26.4799870, 31.1944294),
        13: (-26.4990422, 31.3756566), 14: (-26.6838310, 31.7467220),
        15: (-26.2596472, 31.8749574), 16: (-26.1410060, 32.0395970),
    },
    "lesoto": {
        1: (-28.7690886, 28.2861149), 2: (-28.9141875, 28.4364375),
        3: (-28.7529054, 28.4956766), 4: (-28.7558330, 28.6002780),
        5: (-28.8203625, 28.7272528), 6: (-28.9431975, 28.8285369),
        7: (-29.2875557, 29.0605389), 8: (-29.4679580, 29.2690909),
        9: (-29.5879785, 29.2921966), 10: (-29.5846507, 29.2882526),
        11: (-29.3440910, 28.5065405), 12: (-29.0714444, 28.4255278),
        13: (-29.4785420, 28.0613873), 14: (-29.3130504, 27.4784482),
        15: (-29.3463224, 27.6638307), 16: (-29.6263228, 27.5088085),
        17: (-29.8280062, 27.5999060), 18: (-29.8701526, 28.0535076),
        19: (-30.4050444, 27.6432830), 20: (-29.9035304, 29.1107486),
    },
}


NAMES = {
    "esuatini": {
        1: "Lion Cavern · antigua mina de Ngwenya",
        2: "Ngwenya Glass · fábrica y taller",
        3: "Malolotja · acceso de la reserva",
        4: "Malolotja Canopy Tour",
        5: "Maguga Dam · presa y valle del Komati",
        6: "Nsangwini Rock Art",
        7: "Phophonyane Falls Nature Reserve",
        8: "Mbabane · Swazi Plaza y servicios",
        9: "Sibebe Rock",
        10: "Ezulwini Handcraft Market y valle",
        11: "Mantenga Cultural Village y reserva",
        12: "Mlilwane Wildlife Sanctuary",
        13: "Manzini Main Market",
        14: "Mkhaya · punto oficial de encuentro",
        15: "Hlane · Ndlovu Camp",
        16: "Shewula Mountain Camp",
    },
    "lesoto": {
        1: "Butha-Buthe Mountain",
        2: "Ts’ehlanyane · Maliba Lodge y parque",
        3: "Liphofung Cave y centro de visitantes",
        4: "Moteng Pass",
        5: "Afriski Mountain Resort",
        6: "Tlaeeng Pass",
        7: "Mokhotlong · base del altiplano",
        8: "Thabana Ntlenyana · cumbre",
        9: "Sani Pass",
        10: "Sani Top · lodge y escarpe",
        11: "Katse Dam Information Centre",
        12: "Bokong Nature Reserve · visitantes",
        13: "Mohale Dam · lodge y visitas",
        14: "Maseru · Basotho Hat y servicios",
        15: "Thaba Bosiu Cultural Village",
        16: "Morija Museum & Archives",
        17: "Malealea Lodge y rutas a caballo",
        18: "Maletsunyane Falls",
        19: "Masitise Cave House and Museum",
        20: "Sehlabathebe National Park",
    },
}


LINKS = {
    "esuatini": {
        1: [("Turismo de Esuatini · Lion Cavern", "https://www.thekingdomofeswatini.com/north-west-eswatini/ngwenya-mine-lion-cavern/")],
        2: [("Ngwenya Glass · visita a la fábrica", "https://shop.ngwenyaglass.co.sz/factory-tour")],
        3: [("ENTC · Malolotja Nature Reserve", "https://entc.org.sz/malolotja-nature-reserve/")],
        4: [("ENTC · Canopy Tours", "https://entc.org.sz/canopy-tours/")],
        5: [("Turismo de Esuatini · Maguga Viewsite", "https://www.thekingdomofeswatini.com/responsible-travel/community-tourism/")],
        6: [("Turismo de Esuatini · Nsangwini Rock Art", "https://www.thekingdomofeswatini.com/north-west-eswatini/nsangwini-rock-art/")],
        7: [("Turismo de Esuatini · Phophonyane", "https://www.thekingdomofeswatini.com/north-west-eswatini/phophonyane-nature-reserve/")],
        8: [("Turismo de Esuatini · Mbabane", "https://www.thekingdomofeswatini.com/central-eswatini/mbabane/")],
        9: [("Turismo de Esuatini · Sibebe Rock", "https://www.thekingdomofeswatini.com/central-eswatini/sibebe-rock/")],
        10: [("Turismo de Esuatini · Ezulwini Valley", "https://www.thekingdomofeswatini.com/central-eswatini/ezulwini-valley/")],
        11: [("ENTC · Mantenga Nature Reserve", "https://entc.org.sz/mantenga-nature-reserve/")],
        12: [("Big Game Parks · Mlilwane", "https://biggameparks.org/properties/mlilwane-wildlife-sanctuary")],
        13: [("Turismo de Esuatini · Manzini", "https://www.thekingdomofeswatini.com/central-eswatini/manzini/")],
        14: [("Big Game Parks · Mkhaya y punto oficial", "https://biggameparks.org/properties/mkhaya-game-reserve")],
        15: [("Big Game Parks · Hlane", "https://biggameparks.org/properties/hlane-royal-national-park")],
        16: [("Turismo de Esuatini · Shewula", "https://www.thekingdomofeswatini.com/north-east-eswatini/shewula-nature-reserve/shewula-mountain-camp/")],
    },
    "lesoto": {
        1: [("Visit Lesotho · ruta histórica de Moshoeshoe", "https://www.visitlesotho.org.ls/place-to-visit/king-moshoeshoe-historical-route")],
        2: [("Visit Lesotho · Ts’ehlanyane", "https://www.visitlesotho.org.ls/place-to-visit/tsehlanyane-national-park")],
        3: [("Visit Lesotho · Liphofung", "https://www.visitlesotho.org.ls/place-to-visit/liphoofung-nature-reserve")],
        4: [("Visit Lesotho · ruta de las Highlands", "https://www.visitlesotho.org.ls/place-to-visit/highlands-ski-route")],
        5: [("Visit Lesotho · Afriski", "https://www.visitlesotho.org.ls/place-to-visit/afriski-mountain-resort")],
        6: [("Visit Lesotho · mapa de pasos del altiplano", "https://www.visitlesotho.org.ls/wp-content/uploads/2025/05/1703-Output-5.2-National-Tourism-Master-Plan-compressed-copy.pdf")],
        7: [("Visit Lesotho · ruta 4x4 por Mokhotlong", "https://www.visitlesotho.org.ls/place-to-visit/mountain-biking-4x4-route")],
        8: [("Visit Lesotho · Thabana Ntlenyana", "https://www.visitlesotho.org.ls/wp-content/uploads/2025/05/LTDC-Investment-Opportunities.pdf")],
        9: [("Visit Lesotho · Sani Pass y altiplano", "https://www.visitlesotho.org.ls/place-to-visit/sani-top-thabana-ntlenyana")],
        10: [("Sani Mountain Escape · sitio del alojamiento", "https://sanimountain.co.za/")],
        11: [("LHDA · turismo en Katse", "https://www.lhda.org.ls/home/tourism")],
        12: [("Visit Lesotho · Bokong", "https://www.visitlesotho.org.ls/place-to-visit/bookong-nature-reserve")],
        13: [("LHDA · turismo en Mohale", "https://www.lhda.org.ls/home/tourism")],
        14: [("Visit Lesotho · Maseru", "https://www.visitlesotho.org.ls/place-to-visit/maseru")],
        15: [("UNESCO · Thaba Bosiu", "https://whc.unesco.org/en/tentativelists/6920/")],
        16: [("Morija Museum & Archives", "https://morijamuseum.org/")],
        17: [("Malealea Lodge · actividades y reserva", "https://malealealodge.com/")],
        18: [("Visit Lesotho · Maletsunyane Falls", "https://www.visitlesotho.org.ls/place-to-visit/maletsunyane-falls")],
        19: [("Travel Lesotho · Masitise Cave House", "https://www.travellesotho.com/places-to-visit/masitise-cave-house/")],
        20: [("Visit Lesotho · Sehlabathebe", "https://www.visitlesotho.org.ls/place-to-visit/sehlabathebe-national-park")],
    },
}


def links(country: str, number: int) -> list[dict[str, str]]:
    return [{"label": label, "url": url} for label, url in LINKS[country][number]]


CONTENT = {"esuatini": {
    1: entry(
        "Lion Cavern conserva evidencias de extracción prehistórica de ocre en Bomvu Ridge. El centro de visitantes ardió en 2018: hay que confirmar qué parte está abierta antes de desviarse.",
        "Conecta el comienzo de la minería conocida con un lugar arqueológico concreto, muy cerca de la frontera.",
        "La cavidad de Lion Cavern, hematita especular y el paisaje de la mina moderna; no todo el cráter es zona visitable.",
        "El pin coincide con Lion Cavern en Google Maps. Contactar con ENTC y entrar solo con acceso o guía confirmado.",
        "Mañana seca, enlazándolo con Ngwenya Glass o Malolotja.",
        "Descartarlo si ENTC no confirma reapertura, guía o acceso seguro."),
    2: entry(
        "Taller de vidrio reciclado donde la pasarela permite observar a los artesanos soplando y moldeando piezas. Es una parada breve y concreta, no una ficha genérica de compras.",
        "Permite ver el proceso completo y resolver comida, aparcamiento y regalos tras la frontera.",
        "Horno, soplado de vidrio y tienda; los horarios de demostración pueden no cubrir toda la jornada.",
        "El pin coincide con Ngwenya Glass en Google Maps. Consultar el horario de la fábrica antes de llegar.",
        "Entre semana y durante una sesión activa del taller.",
        "Omitirlo si solo está abierta la tienda o si no interesa la demostración artesanal."),
    3: entry(
        "Reserva de highveld con praderas, gargantas, cascadas y una amplia red de senderos. El pin se sitúa en el objeto de acceso de Google Maps, no en el centro geométrico del parque.",
        "Es la mejor base del país para caminar por montaña y entender el contraste entre highveld y lowveld.",
        "Vistas de valle, pastizal, avifauna y rutas de distinta duración; la cascada exige un itinerario específico.",
        "Confirmar recepción, sendero, acampada y política de mascotas con ENTC. Llevar navegación y agua.",
        "Día despejado y seco; reservar más margen si se hace travesía.",
        "No caminar con niebla cerrada, tormenta, incendio o sin registro de ruta."),
    4: entry(
        "Circuito guiado de diez tirolinas, once plataformas y un puente colgante de unos 50 m sobre el cañón. Se ha eliminado el superlativo no demostrado sobre su longitud.",
        "Añade una actividad de aventura bien definida dentro de Malolotja y vistas difíciles de obtener desde carretera.",
        "Líneas sobre la garganta, plataformas y puente colgante; es una actividad comercial separada de la reserva.",
        "El pin coincide con Malolotja Canopy Tour. Reserva previa, equipo del operador y peso/edad confirmados.",
        "Sesión de mañana, con viento moderado y previsión estable.",
        "Descartarlo con tormenta, viento fuerte, cierre del operador o sin plan seguro para el perro."),
    5: entry(
        "Presa sobre el Komati rodeada por un valle sinuoso. Es una parada paisajística de carretera; los miradores, el craft outlet y el alojamiento son puntos distintos.",
        "Rompe el tramo norte con una panorámica clara y encaja naturalmente entre Malolotja, Piggs Peak y Nsangwini.",
        "Muro, embalse y laderas del Komati; el nivel de agua y la luz cambian mucho la experiencia.",
        "El pin coincide con Maguga Dam en Google Maps. Usar solo apartaderos o el viewsite autorizado.",
        "Primera o última hora con buena visibilidad.",
        "Omitirlo con niebla, lluvia fuerte o si no hay parada segura fuera de la calzada."),
    6: entry(
        "Abrigo con pinturas san sobre el valle del Komati, gestionado por la comunidad. El acceso incluye pista de tierra y un sendero corto pero empinado.",
        "Es el sitio de arte rupestre abierto al público mejor interpretado del país y financia un proyecto local.",
        "Figuras humanas y animales, incluidas representaciones aladas cuya interpretación debe explicarla el guía.",
        "El pin coincide con Nsangwini Rock Art en Google Maps. La fuente oficial indica 7,5 km de pista y descenso a pie.",
        "Mañana seca; prever unos 20 minutos de bajada y 25 de subida.",
        "No bajar con tormenta, barro fuerte, movilidad insuficiente o sin guía local disponible."),
    7: entry(
        "Reserva privada de bosque y cascadas junto a Piggs Peak, con senderos y alojamiento. Las pozas y el caudal dependen de la temporada.",
        "Ofrece una pausa verde y fresca muy distinta del lowveld y permite dormir junto al bosque.",
        "Saltos de agua, bosque ribereño y avifauna; no se promete baño sin confirmación local.",
        "El pin coincide con Phophonyane Falls Ecolodge. Consultar acceso diario, senderos y política de mascotas.",
        "Tras lluvias moderadas pero con senderos firmes; evitar el calor central.",
        "Descartarlo con crecida, pista dañada o si solo se busca una parada gratuita de carretera."),
    8: entry(
        "Swazi Plaza es un ancla precisa en Mbabane para compras y servicios. La ciudad sirve sobre todo para banco, salud, comunicaciones y reparaciones.",
        "Es la base logística más completa del país y queda cerca de Sibebe y Ezulwini.",
        "Centro urbano, mercado y servicios; los recintos reales están en Lobamba, no aquí.",
        "El pin coincide con Swazi Plaza. Aparcar vigilado y agrupar gestiones para no alargar la escala.",
        "Horario comercial entre semana.",
        "Reducir la visita si no hay gestiones: no compensa convertirla en una jornada turística genérica."),
    9: entry(
        "Gran domo de granito al norte de Mbabane, con rutas comunitarias sobre roca expuesta. Los superlativos internacionales varían según la fuente y no se presentan como hechos medidos.",
        "La subida combina geología, esfuerzo corto y vistas amplias del highveld.",
        "Placas de granito, vegetación de altura y panorámica; la ruta exacta debe acordarse localmente.",
        "El pin coincide con Sibebe Rock en Google Maps. Contratar guía comunitario y confirmar punto de inicio.",
        "Primera hora, con roca completamente seca.",
        "No subir con lluvia, tormenta, niebla, calor fuerte o sin un acceso reconocido."),
    10: entry(
        "Mercado artesanal concreto dentro del corredor de Ezulwini, elegido como ancla en vez de un pin difuso del valle. Mlilwane, Mantenga y Lobamba siguen siendo visitas independientes.",
        "Permite valorar artesanía local y organizar desde una base única varios PDIs cercanos.",
        "Puestos de talla, tejidos y objetos decorativos, además del paisaje del valle.",
        "El pin coincide con Ezulwini Handcraft Market. Aparcar dentro del recinto y negociar con respeto.",
        "Mañana o primeras horas de la tarde, combinándolo con Mantenga.",
        "Omitir el mercado si está inactivo; no confundirlo con una visita a Lobamba o Mlilwane."),
    11: entry(
        "Reserva y aldea cultural interpretada junto a Ezulwini, con arquitectura doméstica, demostraciones y sendero a las cascadas.",
        "Es la introducción cultural más accesible del desvio y se entiende mejor con guía.",
        "Estructuras del poblado, explicación de la homestead, danza programada y cascada; horarios separados.",
        "El pin coincide con Mantenga Nature Reserve and Cultural Village. Confirmar función, paseo y fotografía.",
        "Llegar antes de una visita guiada y evitar la franja de más calor.",
        "Descartarlo si no hay actividad interpretativa o si la lluvia impide el sendero."),
    12: entry(
        "Santuario sin grandes depredadores en el valle de Ezulwini, recorrible a pie, en bicicleta o a caballo. Sigue siendo una reserva de fauna con normas propias.",
        "Permite observar herbívoros fuera del coche y descansar en un entorno protegido.",
        "Cebras, antílopes, facóqueros, llanuras y rutas; cada actividad tiene condiciones distintas.",
        "El pin coincide con Mlilwane Wildlife Sanctuary. Confirmar alojamiento, actividad y prohibición de mascotas.",
        "Amanecer y última hora; dedicar una noche si se quiere caminar y pedalear.",
        "No entrar con el perro ni abandonar rutas autorizadas; omitirlo si no existe plan de custodia."),
    13: entry(
        "El mercado principal de Manzini es el PDI urbano, no la ciudad entera. Reúne alimentos, ropa, artesanía y actividad comercial cotidiana.",
        "Es una parada con vida local real y la ocasión de resolver suministros antes del lowveld.",
        "Naves y puestos del mercado, mercancía rural y calles comerciales cercanas.",
        "El pin coincide con Manzini Main Market. Aparcar vigilado, llevar poco equipo visible y no bloquear pasos.",
        "Jueves por la mañana es la recomendación de la oficina de turismo; cualquier horario comercial sirve para logística.",
        "Omitir el paseo si está cerrado o muy vacío; mantener solo la parada de servicios si hace falta."),
    14: entry(
        "Reserva guiada centrada en especies amenazadas. El vehículo propio se deja en Phuzumoya: Google conduce a una puerta trasera sin personal y el gestor advierte expresamente que no se use.",
        "Ofrece una probabilidad alta de encuentros cercanos con rinocerontes en grupos pequeños.",
        "Rinoceronte negro y blanco, bosque seco y Stone Camp; los avistamientos nunca están garantizados.",
        "El pin usa el punto oficial publicado por Big Game Parks: 26.683831 S, 31.746722 E. Reserva y hora de encuentro obligatorias.",
        "Llegar con margen a la hora indicada en la reserva.",
        "No ir sin reserva ni dejar al perro solo en el aparcamiento; hace falta un plan externo real."),
    15: entry(
        "Ndlovu Camp es la base de acceso a Hlane, parque de lowveld con elefantes, rinocerontes y una zona de leones de entrada controlada.",
        "Es el safari más fácil de integrar antes de Mozambique y permite combinar conducción propia con actividades guiadas.",
        "Charca de Ndlovu, rinocerontes, elefantes y aves; leones y caminatas dependen de circuitos autorizados.",
        "El pin coincide con Hlane Ndlovu Camp. Registrar el vehículo y respetar puertas y zonas de bajada.",
        "Amanecer, última hora y estación seca para concentración de fauna.",
        "No entrar con mascota ni improvisar circulación nocturna; omitirlo sin custodia segura del perro."),
    16: entry(
        "Campamento comunitario en el escarpe de Lubombo, con rondavels, camping y vistas sobre el lowveld. Es una base cultural y paisajística, no un safari garantizado.",
        "Los ingresos permanecen en la comunidad y el lugar encaja naturalmente antes de cruzar a Mozambique.",
        "Miradores, alojamiento tradicional y paseos comunitarios con guía.",
        "El pin coincide con Main Camp Shewula Nature Reserve. Confirmar reserva, comidas y acceso final.",
        "Llegar de día para la vista y pasar una noche si se hace paseo comunitario.",
        "Descartarlo con acceso dañado, tormenta o sin confirmación de alojamiento/camping."),
}}


CONTENT["lesoto"] = {
    1: entry(
        "Butha-Buthe Mountain fue uno de los primeros asentamientos fortificados de Moshoeshoe antes de Thaba Bosiu. El pin marca la montaña histórica, no el centro de la ciudad.",
        "Da contexto territorial al nacimiento del reino basotho y encaja al entrar por Caledonspoort.",
        "Meseta y paisaje norteño; los restos y accesos se comprenden mejor con acompañamiento local.",
        "El pin coincide con Butha Buthe Mountain en Google Maps. Preguntar localmente por acceso y guía; no abrir pista por cuenta propia.",
        "Mañana despejada, antes de internarse hacia Liphofung o Ts’ehlanyane.",
        "Omitir la subida si no hay acceso claro, guía o lugar seguro para dejar el vehículo."),
    2: entry(
        "Parque de montaña con bosque autóctono, cascadas y senderos en el norte de Lesoto. El pin se ha trasladado a Maliba Lodge, base operativa dentro del parque, porque la ficha genérica de Google aparecía fuera de lugar.",
        "Es el acceso más sencillo a un paisaje boscoso muy escaso en el resto del país.",
        "Valle del Holomo, bosque, flora subalpina y rutas a pie o a caballo; cada sendero requiere tiempo propio.",
        "El pin coincide con Maliba Lodge en Google Maps. La fuente oficial indica un acceso final de grava: reservar y confirmar estado.",
        "Dos noches si se quiere caminar; mañana estable para las rutas largas.",
        "Descartarlo con crecida, nieve fuerte, acceso cortado o sin confirmación de la política de mascotas."),
    3: entry(
        "Pequeña reserva alrededor de un gran abrigo de arenisca con arte san y memoria asociada a Moshoeshoe. El centro de visitantes ofrece alojamiento básico.",
        "Reúne en una visita corta las dos capas históricas clave del norte: poblaciones san y formación basotho.",
        "Pinturas, abrigo rocoso, interpretación y construcciones del centro; no todas las marcas son igual de visibles.",
        "El pin coincide con Liphofung Cave Chalets y centro. Sendero con tramos empinados; confirmar guía y apertura.",
        "Parada diurna entre Butha-Buthe y Moteng, con roca seca.",
        "No tocar las pinturas ni acceder si el centro está cerrado o el sendero resulta inseguro."),
    4: entry(
        "Puerto asfaltado de curvas cerradas en la A1, sobre el valle de Moteng. Es un punto de conducción y paisaje, no una atracción con recinto.",
        "Es la primera gran subida del corredor norte y muestra de golpe la escala de las Maloti.",
        "Horquillas, laderas y vistas hacia el valle; Oxbow es una parada separada.",
        "El pin coincide con Moteng Pass en Google Maps. Parar solo fuera de la calzada y bajar con freno motor.",
        "Con luz, visibilidad y firme seco; comprobar hielo o nieve en invierno.",
        "No detenerse con niebla, viento severo, hielo o sin un apartadero completamente seguro."),
    5: entry(
        "Complejo de montaña de gran altitud con esquí estacional y actividades de verano. La nieve y la apertura de pistas dependen del tiempo y de la operación del resort.",
        "Es una rareza regional y una base cómoda para experimentar el altiplano sin autonomía total.",
        "Pista, remontes y paisaje de las Maloti; fuera de invierno predominan bici, senderismo y otras actividades.",
        "El pin coincide con Afriski en Google Maps. Comprobar carretera, alojamiento, temporada y equipos directamente con el resort.",
        "Invierno para esquiar solo con apertura confirmada; verano para montaña.",
        "Omitirlo si se busca nieve sin parte operativo, o si el acceso exige asumir hielo sin equipo adecuado."),
    6: entry(
        "Tlaeeng es un puerto del altiplano de más de 3.200 m. Es un hito de carretera expuesto al viento, la niebla y la nieve, no un mirador equipado.",
        "Marca uno de los momentos más altos de toda la conducción del viaje sin exigir un desvío.",
        "Cartel del puerto, carretera y panorámica de pastizales alpinos.",
        "El pin coincide con Tlaeeng Pass en Google Maps. Confirmar el estado del acceso y la ruta localmente: la información publicada sobre firme y trazado no es uniforme.",
        "Solo de día y con previsión estable; llevar abrigo incluso con sol.",
        "No cruzarlo con cierre, hielo, tormenta eléctrica o visibilidad insuficiente."),
    7: entry(
        "Mokhotlong es la base urbana del extremo oriental: combustible, provisiones y consulta de la carretera antes de Sani o Thabana Ntlenyana. La disponibilidad concreta puede variar.",
        "Es el último punto razonable para reorganizar combustible, comida y meteorología antes de rutas remotas.",
        "Vida del altiplano y servicios básicos; no se presenta como ciudad monumental.",
        "El pin coincide con Mokhotlong en Google Maps. Repostar cuando haya suministro y verificar el siguiente tramo localmente.",
        "Horario comercial y llegada con luz.",
        "No salir hacia una ruta remota con depósitos o reservas de agua insuficientes."),
    8: entry(
        "La cumbre de 3.482 m es el punto más alto de Lesoto y de África austral. La ruta es remota, poco marcada y muy expuesta aunque no requiera escalada técnica normal.",
        "Aporta una jornada de alta montaña auténtica desde el entorno de Sani Top.",
        "Pastizal alpino, cresta y mojón de cumbre; la vista desaparece rápidamente con niebla.",
        "El pin coincide con la cumbre en Google Maps, no con un aparcamiento. Contratar guía y acordar inicio, ruta y retorno.",
        "Salida muy temprana con previsión estable y ropa para frío severo.",
        "No intentarlo con niebla, tormenta, nieve, inicio tardío o sin navegación y guía fiables."),
    9: entry(
        "Paso fronterizo espectacular entre Lesoto y KwaZulu-Natal, con fuertes horquillas en el escarpe. El firme y los requisitos del tramo cambian con las obras y deben verificarse antes del viaje.",
        "Es uno de los grandes hitos de conducción de África austral y una entrada directa al altiplano.",
        "Escarpe, curvas y puestos fronterizos; el pin marca la parte alta, no el control sudafricano inferior.",
        "El pin coincide con Sani Pass y se sincroniza con la ficha de Sudáfrica. Confirmar horario, estado y requisito 4x4 con las autoridades.",
        "Subir o bajar con varias horas de luz y tiempo estable.",
        "No entrar con frontera cerrada, hielo, lluvia fuerte, niebla o vehículo que no cumpla la exigencia vigente."),
    10: entry(
        "Alojamiento junto al borde superior del Sani, con vistas inmediatas del escarpe. Su bar se promociona como el más alto de África; se presenta como reclamo del operador, no como récord independiente.",
        "Permite dormir arriba, caminar por el borde y evitar una travesía apresurada de la frontera.",
        "Edificios del lodge, bar y vistas hacia Sudáfrica; Thabana Ntlenyana requiere otra jornada.",
        "El pin coincide con Sani Mountain Escape en Google Maps. Reservar y confirmar el nombre comercial y servicios vigentes.",
        "Atardecer y noche despejada, con abrigo serio.",
        "Descartarlo si no hay reserva o si la carretera/frontera impiden llegar con luz."),
    11: entry(
        "Centro de información para conocer Katse Dam y la primera fase del Lesotho Highlands Water Project. Las visitas técnicas dependen de autorización y horario.",
        "La presa explica una parte central de la ingeniería, el agua y la economía contemporánea del país.",
        "Muro de arco, embalse e interpretación del sistema; el jardín botánico es una visita separada cercana.",
        "El pin coincide con Katse Dam Information Center. Concertar el tour con LHDA y seguir restricciones de seguridad y fotografía.",
        "Horario laboral y día de visibilidad razonable.",
        "No acceder a instalaciones cerradas ni usar dron; omitir el tour si LHDA no lo confirma."),
    12: entry(
        "Centro de visitantes de una reserva alpina junto a la A25, con vista al valle del Lepaqoa y sendero hacia la cascada. El salto puede helarse en invierno, pero no se garantiza.",
        "Es la parada natural del camino de Katse y ofrece una caminata corta de gran altitud.",
        "Pastizal alpino, valle y Lepaqoa Falls; las aves y el hielo dependen de estación y suerte.",
        "El pin usa las coordenadas oficiales publicadas por Visit Lesotho: S29°04’17.2 E28°25’31.9.",
        "Mañana estable; en invierno confirmar hielo y estado de la A25.",
        "No caminar con tormenta, niebla cerrada o si el centro desaconseja la ruta."),
    13: entry(
        "Mohale Lodge sirve como ancla verificable para organizar la visita al embalse y la presa. El muro y las instalaciones de LHDA no están en este mismo pin.",
        "La carretera de acceso y el sistema de trasvase complementan Katse con menos afluencia.",
        "Embalse, paisaje de montaña y, si LHDA lo autoriza, instalaciones de la presa.",
        "El pin coincide con Mohale Lodge. Concertar cualquier visita técnica con LHDA; no seguir un pin genérico hasta infraestructura cerrada.",
        "Llegada diurna y tiempo estable para la carretera.",
        "Omitir la visita técnica si no está confirmada y no volar dron sobre la infraestructura."),
    14: entry(
        "Basotho Hat es una referencia urbana reconocible de Maseru y un punto concreto para artesanía. La capital sigue siendo ante todo la gran base logística del país.",
        "Permite combinar una parada cultural breve con banco, mercado, hospital, taller y abastecimiento.",
        "Edificio inspirado en el mokorotlo y artesanía; otros monumentos urbanos quedan fuera de esta ficha.",
        "El pin coincide con Basotho Hat en Google Maps. Aparcar vigilado y agrupar todas las gestiones por zonas.",
        "Horario comercial entre semana.",
        "Acortar la visita si no hay gestiones; no dejar equipaje visible ni circular innecesariamente de noche."),
    15: entry(
        "Aldea cultural al pie de Thaba Bosiu, la meseta fortificada asociada a Moshoeshoe I y a la formación de la nación basotho. La visita a la cima es una actividad distinta.",
        "Es el lugar esencial para comprender la historia política de Lesoto con contexto local.",
        "Reconstrucción cultural, centro interpretativo y silueta de la montaña; tumbas y restos están arriba.",
        "El pin coincide con Thaba Bosiu Cultural Village. Contratar guía si se sube y respetar los lugares de memoria.",
        "Mañana fresca, reservando media jornada si se incluye la cima.",
        "No reducirlo a una foto del poblado ni subir con tormenta o sin tiempo suficiente."),
    16: entry(
        "Museo y archivo en la misión histórica de Morija, con colecciones sobre historia, cultura y paleontología de Lesoto. Las huellas de dinosaurio del entorno requieren indicaciones aparte.",
        "Es la institución más útil del país para ordenar el relato histórico antes de recorrer sus lugares.",
        "Exposiciones, documentos y edificios de la misión; confirmar con el museo cualquier paseo exterior.",
        "El pin coincide con Morija Museum & Archives. Revisar horario y solicitar guía para sitios cercanos.",
        "Mañana o primera tarde en día de apertura.",
        "Descartarlo si está cerrado; no buscar huellas por fincas o laderas sin permiso."),
    17: entry(
        "Lodge comunitario que organiza rutas a caballo y a pie por aldeas y gargantas. El poni basotho es aquí un medio de movilidad local, no solo una atracción escénica.",
        "Es la base más consolidada para una experiencia rural de uno o varios días con guías locales.",
        "Valle, rutas, vida comunitaria y Gates of Paradise; cada excursión tiene dificultad y duración propias.",
        "El pin coincide con Malealea Lodge. Reservar alojamiento y actividad y comunicar experiencia ecuestre real.",
        "Dos noches como mínimo para no convertirlo en una parada superficial.",
        "Omitir rutas largas con tormenta, crecida, lesión o sin plan confirmado para el perro."),
    18: entry(
        "Maletsunyane cae en un único gran salto cerca de Semonkong y es el principal paisaje de cascada del país. El rápel comercial es una actividad del operador, no parte automática de la visita.",
        "El anfiteatro basáltico y el acceso a pie justifican el desvío incluso sin realizar actividades de aventura.",
        "Cascada, garganta y miradores; caudal, spray y visibilidad cambian con la estación.",
        "El pin coincide con Maletsunyane Falls en Google Maps. Contratar guía para rutas a la base o actividades técnicas.",
        "Mañana o última hora con luz lateral y sin tormenta.",
        "No acercarse al borde con niebla, viento, roca mojada o fuera de senderos reconocidos."),
    19: entry(
        "Casa misionera construida bajo un abrigo de roca en 1866–67 y convertida en pequeño museo. Sustituye al antiguo pin genérico de Quthing y muestra el PDI concreto descrito.",
        "Combina arquitectura singular, historia baphuthi y misionera y una visita manejable en el sur del país.",
        "Estancias bajo la roca y colección local; las huellas y pinturas del distrito no están todas en el museo.",
        "El pin coincide con Masitise Cave House and Museum. Seguir las indicaciones hacia el recinto de la iglesia y confirmar apertura.",
        "Horario diurno, preferiblemente con aviso previo.",
        "Omitirlo si está cerrado; no presentar como parte del museo ningún yacimiento no visitado."),
    20: entry(
        "Parque remoto de pradera, humedales y formaciones de arenisca integrado en el sitio Maloti-Drakensberg. La ficha de Google marca el parque, no garantiza la posición de la recepción.",
        "Es el paisaje protegido más aislado de Lesoto y combina geología, arte rupestre y silencio.",
        "Arcos y formas de arenisca, lagunas y rutas; el arte rupestre requiere guía y máximo cuidado.",
        "El pin coincide con Sehlabathebe National Park en Google Maps. Confirmar por escrito puerta, lodge, pista y combustible antes de salir.",
        "Dos o tres noches con ventana seca y vehículo preparado.",
        "No entrar con pista cortada, tormenta, combustible justo, mascota prohibida o sin confirmación del alojamiento."),
}


PHOTOS = {
    "esuatini": {
        1: [
            commons("Ngwenya Mine.jpg", "Heather Dowd · CC BY-SA 2.0", "Frente de la mina de Ngwenya, donde se encuentra Lion Cavern."),
            commons("Ngwenya Mine (7045532451) (12).jpg", "thomas · CC BY-SA 2.0", "Estratos y excavación del complejo minero de Ngwenya."),
            commons("Ngwenya Mine (6899436572) (4).jpg", "thomas · CC BY-SA 2.0", "Paisaje de Bomvu Ridge y la mina; la visita arqueológica depende de ENTC."),
        ],
        2: [
            commons("Ngwenya Glass Factory.jpg", "Heather Dowd · CC BY-SA 2.0", "Interior del taller de Ngwenya Glass."),
            commons("Glass Elephant.jpg", "Ngwenya Glass · CC BY-SA 4.0", "Elefante elaborado en vidrio reciclado por el taller."),
            commons("Elephant 02.jpg", "Ngwenya Glass · CC BY-SA 4.0", "Detalle de una pieza de vidrio soplado de Ngwenya Glass."),
        ],
        3: [
            commons("Malolotja Scenery (31722500693).jpg", "Bernard DUPONT · CC BY-SA 2.0", "Praderas y relieve de Malolotja Nature Reserve."),
            commons("Protea caffra in Eswatini.jpg", "Ton Rulkens · CC BY-SA 2.0", "Protea caffra fotografiada en el paisaje de Malolotja."),
            commons("Malolotja Nature Reserve banner Highveld Crag Lizard.jpg", "Bernard DUPONT · CC BY-SA 2.0", "Lagarto del highveld en Malolotja; detalle de biodiversidad, no vista del acceso."),
        ],
        4: [
            external("https://entc.org.sz/wp-content/uploads/2025/04/IMG_5145-768x512.jpg", "https://entc.org.sz/canopy-tours/", "ENTC · sitio oficial", "Puente colgante del circuito Malolotja Canopy Tour."),
            external("https://entc.org.sz/wp-content/uploads/2025/04/IMG_5141-768x512.jpg", "https://entc.org.sz/canopy-tours/", "ENTC · sitio oficial", "Vista sobre la garganta desde el puente del circuito."),
            external("https://entc.org.sz/wp-content/uploads/2025/04/IMG_5047.jpg", "https://entc.org.sz/canopy-tours/", "ENTC · sitio oficial", "Participantes equipados por el operador en el propio canopy."),
        ],
        5: [
            commons("Maguga Dam at Komati River, Eswatini.jpg", "FreddieA · CC BY-SA 3.0", "Muro y embalse de Maguga sobre el río Komati."),
            commons("Maguga dam.jpg", "René C. Nielsen · CC BY-SA 2.0", "Vista amplia de Maguga Dam y el valle."),
        ],
        6: [
            commons("Nsangwini Rock Art 1.jpg", "Daniel Kraft · CC BY-SA 3.0", "Panel de arte rupestre en el abrigo de Nsangwini."),
            commons("Nsangwini Rock Art 2.jpg", "Daniel Kraft · CC BY-SA 3.0", "Figuras pintadas en la roca de Nsangwini."),
            commons("Nsangwini Rock Art 3.jpg", "Daniel Kraft · CC BY-SA 3.0", "Otro detalle del panel; la lectura debe hacerse con guía."),
        ],
        7: [
            commons("Phophonyane Falls.jpg", "Daniel Kraft · CC BY-SA 3.0", "Uno de los saltos de Phophonyane Falls."),
            commons("Phophonyane Falls Nature Reserve, Swaziland.jpg", "Steven Belcher · CC BY-SA 2.0", "Bosque y agua dentro de Phophonyane Falls Nature Reserve."),
            commons("Phophonyane Falls 01.jpg", "Africaspotter · CC BY-SA 3.0", "Detalle de la cascada en la reserva."),
        ],
        8: [
            commons("Swazi Plaza, Mbabane, Eswatini.jpg", "Bakhile · CC BY-SA 4.0", "Swazi Plaza, el punto concreto marcado en Mbabane."),
            commons("Mbabane WV banner.jpg", "Athena Lao · CC BY 2.0", "Vista urbana de Mbabane; complemento al punto de servicios."),
        ],
        9: [
            commons("Granite monolith.jpg", "theswazigirl · CC BY-SA 3.0", "Participantes sobre la roca de Sibebe durante una actividad organizada."),
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmAeCqe-w1smd3f4pO8OhnPjVB85CXPL_MC1HKUa3TWwc2T-CuyQ-VaDJxOoOD_uGJijhMteJVe1eGsNhGeO9qLxFPa8LDdCkTiCEshY8TlVjRdkMwq-M1DVZbMOQWf50WGqGmkJg=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Sibebe+Rock+Eswatini", "Google Maps · autor visible en la ficha", "Roca de Sibebe fotografiada en el propio PDI de Google Maps."),
        ],
        10: [
            commons("SZ-ezulwini-markt-4.jpg", "Bgabel · CC BY-SA 3.0", "Puestos del mercado artesanal de Ezulwini."),
            commons("SZ-ezulwini-markt-2.jpg", "Bgabel · CC BY-SA 3.0", "Artesanía expuesta en el mercado de Ezulwini."),
            commons("SZ-ezulwini-markt-3.jpg", "Bgabel · CC BY-SA 3.0", "Otra zona de venta del mismo mercado."),
        ],
        11: [
            commons("Mantenga Cultural Village (6899343892) (4).jpg", "thomas · CC BY-SA 2.0", "Estructuras de la aldea cultural de Mantenga."),
            commons("Mantenga Cultural Village (7045456249) (4).jpg", "thomas · CC BY-SA 2.0", "Recinto y arquitectura del propio poblado."),
            commons("Mantenga Cultural Village (7045494313) (8).jpg", "thomas · CC BY-SA 2.0", "Detalle del conjunto visitable de Mantenga."),
        ],
        12: [
            commons("Lake in Mlilwane Wildlife Sanctuary.jpg", "Bernard Gagnon · CC BY-SA 4.0", "Lago y paisaje de Mlilwane Wildlife Sanctuary."),
            commons("Mlilwane Wildlife Sanctuary in Eswatini 01.jpg", "Bernard Gagnon · CC BY-SA 4.0", "Fauna y llanura dentro del santuario."),
            commons("Zabras in Mlilwane Wildlife Sanctuary.jpg", "Vaiz Ha · CC BY 2.0", "Cebras fotografiadas en Mlilwane."),
        ],
        13: [
            external("https://www.thekingdomofeswatini.com/wp-content/uploads/2018/02/Manzini-SWZ-1-STA-scaled-1200x614.jpg", "https://www.thekingdomofeswatini.com/central-eswatini/manzini/", "Eswatini Tourism Authority · sitio oficial", "Entrada y actividad exterior de Manzini Market."),
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmI2ZFVL9QE0bwprE1gOj6mL-kEgToDD88qRCpt6aStLoX0mm8pQi-_KmRmGzP1ps7haaqDU-JsX8QMYL_S4wTBrJ6hVms5SJwYkjRAWA3ZoaqmJBwICuLlDo1ypG8YsPhYFRsEEg=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Manzini+Main+Market+Eswatini", "Google Maps · autor visible en la ficha", "Puestos interiores fotografiados en la ficha exacta de Manzini Main Market."),
        ],
        14: [
            external("https://biggameparks.org/img/mkyanaslider.jpg", "https://biggameparks.org/properties/mkhaya-game-reserve", "Big Game Parks · sitio oficial", "Rinoceronte observado durante una actividad guiada de Mkhaya."),
            commons("Mkhaya Game Reserve banner Nguni cattle.jpg", "Justinjerez · CC BY-SA 3.0", "Ganado nguni en Mkhaya, especie vinculada al origen de la reserva."),
        ],
        15: [
            commons("Hlane Royal National Park banner White Rhinos wallowing and resting in the bushes.jpg", "Bernard DUPONT · CC BY-SA 2.0", "Rinocerontes blancos en Hlane Royal National Park."),
            commons("Hlane-Basic-Hide-At-Hippo-Pool.JPG", "Bjørn Christian Tørrissen · CC BY-SA 4.0", "Observatorio junto a la charca en Hlane."),
            commons("Mr3 hlane.jpg", "Antonio Olmedo · CC BY-SA 2.0", "Carretera MR3 atravesando el paisaje de Hlane."),
        ],
        16: [
            external("https://www.thekingdomofeswatini.com/wp-content/uploads/2018/07/DSC1390-JOHNHALE-5.jpg", "https://www.thekingdomofeswatini.com/north-east-eswatini/shewula-nature-reserve/shewula-mountain-camp/", "Eswatini Tourism Authority · sitio oficial", "Rondavel y vista del lowveld desde Shewula Mountain Camp."),
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkdSDpggMkwZUmgD1qkbUo-G5Bsvd5IU3g5mAqGB4Qsgoxx4zVEbJx4mNZVdh7XcqU-D5TfUZvi3KRMU_Yu_o6NFahaMnX8D6unRlFKzbOGJ57UqXiaSb1JRFtGOZLQlPooqkgJ=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Main+Camp+Shewula+Nature+Reserve+Eswatini", "Google Maps · autor visible en la ficha", "Vista del campamento comunitario en la ficha exacta de Google Maps."),
        ],
    },
    "lesoto": {
        1: [
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlRmrYUwHD3G76RfSh4FNwnSh_vpJfH2A2w0gglXa_JpqzIcL8YG0d3OObJDgLmcRDRNI9S3bLIwyc-i5JWYhpGjcRxSPe36qib22Jp-fTY0TdCbadV3Gt_sycenhunvTqSktVU=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Butha-Buthe+Mountain+Lesotho", "Google Maps · autor visible en la ficha", "Butha-Buthe Mountain en la ficha exacta de Google Maps."),
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlw7fgbsiM7nZtacV4tmyxQ_aiGeGarUUKbRuZ1G8zjO-gU8CuL40kq_lk8zZmDuDRSduee4iMjHs9G1OAl0EusFMFr02p323IxQbJ1SrdV_QJ7N3a1Eeenpwc46B2hgnnKEpArZw=w900-h1200-k-no", "https://www.google.com/maps/search/?api=1&query=Butha-Buthe+Mountain+Lesotho", "Google Maps · autor visible en la ficha", "Otra vista tomada en el mismo PDI histórico."),
        ],
        2: [
            commons("Tšehlanyane National Park.jpg", "kevincure · CC BY 2.0", "Paisaje de Ts’ehlanyane National Park."),
            external("https://www.visitlesotho.org.ls/wp-content/uploads/2025/04/Lesotho-1911-0363_original2.jpg", "https://www.visitlesotho.org.ls/place-to-visit/tsehlanyane-national-park", "Visit Lesotho · sitio oficial", "Senderos y vegetación del parque según la galería oficial."),
            external("https://www.visitlesotho.org.ls/wp-content/uploads/2025/04/Lesotho-1911-0373_original2.jpg", "https://www.visitlesotho.org.ls/place-to-visit/tsehlanyane-national-park", "Visit Lesotho · sitio oficial", "Otra vista del parque y de su entorno de montaña."),
        ],
        3: [
            external("https://www.visitlesotho.org.ls/wp-content/uploads/2025/04/IMG_0802-copy.jpg", "https://www.visitlesotho.org.ls/place-to-visit/liphoofung-nature-reserve", "Visit Lesotho · sitio oficial", "Gran abrigo de arenisca de Liphofung."),
            external("https://www.visitlesotho.org.ls/wp-content/uploads/2025/04/Lesotho-1911-0610_original.jpg", "https://www.visitlesotho.org.ls/place-to-visit/liphoofung-nature-reserve", "Visit Lesotho · sitio oficial", "Detalle de las pinturas rupestres del abrigo."),
            external("https://www.visitlesotho.org.ls/wp-content/uploads/2025/04/Lesotho-1911-0615_original.jpg", "https://www.visitlesotho.org.ls/place-to-visit/liphoofung-nature-reserve", "Visit Lesotho · sitio oficial", "Construcciones del centro cultural de Liphofung."),
        ],
        4: [
            commons("Moteng pass.jpg", "Jaco van Tonder · CC BY 2.5", "Horquillas y relieve de Moteng Pass."),
            commons("Moteng Pass - panoramio.jpg", "tadpolefarm · CC BY-SA 3.0", "Vista desde el propio paso de Moteng."),
            commons("Moteng Pass 2809 meter.jpg", "Willem.erasmus · CC BY-SA 4.0", "Cartel y carretera en Moteng Pass."),
        ],
        5: [
            commons("AfriSki.jpg", "Jacovt · CC BY 2.5", "Pista e instalaciones de Afriski."),
            commons("Afriski in Summer, bring on the winter - panoramio.jpg", "Graham Maclachlan · CC BY-SA 3.0", "Afriski fuera de la temporada de nieve."),
        ],
        6: [
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlWFFYwpzT9jUF9_jyOFBU0GjEsLj7-n1HMMFe-w88I9xc7DfqiBJ3kV9jlw0LheCGui5P4kHP28-sbm5-qOqgUZqReOzrGk8MkK2od5G8tC9rhg-eYot-pjZ1TQ6UHPtwA8ERJonfmB6BI=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Tlaeeng+Pass+Lesotho", "Google Maps · autor visible en la ficha", "Cartel y paisaje del Tlaeeng Pass."),
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmrQmkWLimbDhXrgCa45S8StZD05E37x4QsedGqqCqdlevQv86vfxusN7mMKw_p55t-g_iKupq7EBm-rk6vYQVCxCUcKo9Gya0TKSK9DCVLphkoPMGyzXa_DL5gWEtJse6L0fucAjQ4FJ8=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Tlaeeng+Pass+Lesotho", "Google Maps · autor visible en la ficha", "Carretera de gran altitud fotografiada en el mismo paso."),
        ],
        7: [
            commons("Mokhotlong par la route.jpg", "HAF932 · CC0", "Mokhotlong visto desde la carretera del altiplano."),
            commons("Mokhotlong-Centre-and-Airport-2009.jpg", "Bjørn Christian Tørrissen · CC BY-SA 3.0", "Centro urbano y aeródromo de Mokhotlong en 2009."),
        ],
        8: [
            commons("Sehlohlolong sa Thabana Ntlenyana.jpg", "Pereng051 · CC0", "Cumbre de Thabana Ntlenyana."),
            commons("Almost at the top of Thabana Ntlenyana.jpg", "TwinMosia · CC BY-SA 4.0", "Tramo final de ascenso hacia la cumbre."),
            commons("Thabana Ntlenyana from Giants Ridge.jpg", "Ghaznavid · CC BY-SA 4.0", "Thabana Ntlenyana visto desde Giants Ridge."),
        ],
        9: [
            commons("Sani Pass heading into Lesotho.jpg", "Vaiz Ha · CC BY 2.0", "Horquillas de Sani Pass en dirección a Lesoto."),
            commons("Sanipass Grenzposten Lesotho.jpg", "Pechristener · CC BY-SA 4.0", "Puesto fronterizo de Lesoto en la parte alta del paso."),
            commons("Lesotho Border Post at Sani Pass.jpg", "Vaiz Ha · CC BY 2.0", "Entrada a Lesoto en Sani Pass."),
        ],
        10: [
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkQz7R1VzOvcHJ-tdexAilmsWpYH15KHzHCu6bKUpz_Obta4nGXY7K6f6IfINqExj-OF_Fo1xyQ4GzmbVW5qDe7o8e2Kqc41KZq_fCI1fC_YF_THB3FsQzUztnxzCxJy8jS8wi6xgoa2Ek=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Sani+Mountain+Escape+Lesotho", "Google Maps · autor visible en la ficha", "Edificio del alojamiento en la ficha exacta de Sani Mountain Escape."),
            commons("View down into South Africa from top of Sani Pass in Lesotho.jpg", "Michael Denne · CC BY-SA 2.0", "Vista del escarpe desde Sani Top."),
            commons("Sani Pass Lesotho.jpg", "Martin Schärli · CC BY-SA 3.0", "Paisaje inmediato de Sani Top y el paso."),
        ],
        11: [
            commons("Katse Dam,Lesotho,Africa.jpg", "Christian Wörtz · CC BY-SA 2.5", "Vista general de Katse Dam."),
            commons("Katse Dam - 2017 (36467442231).jpg", "Stuart Bassil · CC BY 2.0", "Muro y embalse de Katse en 2017."),
            commons("Katse dam intake tower.jpg", "Beest · CC BY-SA 2.5", "Torre de toma del sistema de Katse."),
        ],
        12: [
            external("https://www.visitlesotho.org.ls/wp-content/uploads/2025/04/Lesotho-1911-0454_original.jpg", "https://www.visitlesotho.org.ls/place-to-visit/bookong-nature-reserve", "Visit Lesotho · sitio oficial", "Valle observado desde el entorno de Bokong Nature Reserve."),
            external("https://www.visitlesotho.org.ls/wp-content/uploads/2025/04/Lesotho-1911-0467_original.jpg", "https://www.visitlesotho.org.ls/place-to-visit/bookong-nature-reserve", "Visit Lesotho · sitio oficial", "Lepaqoa Falls y el borde rocoso de Bokong."),
        ],
        13: [
            commons("Mohaledam.jpg", "David Love · dominio público", "Embalse y muro de Mohale Dam."),
            commons("Mohale Dam 2008.jpg", "Egbert · CC BY-SA 2.0", "Mohale Dam fotografiada en 2008."),
            commons("Mohale Dam 904478270.jpg", "Bruce Paulmac · CC BY-SA 3.0", "Paisaje del embalse de Mohale."),
        ],
        14: [
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmRutO1CXFz-9QZAbZMl9TXD6u7hPau_5Jvmvah7Dsjq_xL9CLIIE_GTfimYCSPeSRDsjmKajEhs5ZPH8GXmFK0bNBRhGdl-1UlePaguMfri-uaJ6NvKOpxAvfvjaXSEVuZ8cCQ=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Basotho+Hat+Maseru+Lesotho", "Google Maps · autor visible en la ficha", "Edificio Basotho Hat en Maseru."),
            commons("KingswayMaseru.jpg", "Michael Denne · CC BY-SA 2.0", "Kingsway, eje urbano central de Maseru."),
            commons("Maseru Town.jpg", "Lschefa · CC BY-SA 4.0", "Vista del centro de Maseru."),
        ],
        15: [
            commons("685 Thaba Bosiu.jpg", "Marduk · CC0", "Meseta de Thaba Bosiu y su entorno."),
            commons("Thaba Bosiu - panoramio.jpg", "Graham Maclachlan · CC BY-SA 3.0", "Vista lateral de la montaña fortaleza."),
        ],
        16: [
            commons("Morija Museum and Archives in Morija, Lesotho.jpg", "Niall McNulty · CC BY 2.0", "Edificio del Morija Museum & Archives."),
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmiZBovtuMxV1bVyLwMHoRoJ0o9GRxG23JR8E2Bv5GsqgYz-bdO1wf5jXVYT3npzt063MxitZ2wgG-TK23sHStoYh5K4BB6ndZSCRvydITPIvjjvgQcN9P3bSqsR6J3BoUhNgMhhQ=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Morija+Museum+and+Archives+Lesotho", "Google Maps · autor visible en la ficha", "Otra vista del museo en su ficha exacta de Google Maps."),
        ],
        17: [
            commons("Malealea.jpg", "Tjeerd Wiersma · CC BY 2.0", "Paisaje rural de Malealea."),
            commons("Sunrise at Malealea, Lesotho.jpg", "Di.Malealea · CC BY 2.0", "Amanecer en Malealea."),
        ],
        18: [
            commons("Maletsunyanefalls.JPG", "BagelBelt · dominio público", "Caída completa de Maletsunyane Falls."),
            commons("Lesotho maletsunyane falls.jpg", "Tim Sandell · CC BY-SA 3.0", "Cascada y garganta de Maletsunyane."),
        ],
        19: [
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlN-GGPbAovp23w_SgXSE-WA98OY6h_mGsHScbUfMSX9Irt-yNRmxe8x_CG2k70f2YvHbpRb4CW-VNfpXSWXxeP0AvINUa1rAZnqEi69MSdlevq6Q9rSaRtv_Mhhda8FW0zYzyb5A=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Masitise+Cave+House+and+Museum+Lesotho", "Google Maps · autor visible en la ficha", "Fachada de Masitise Cave House bajo el abrigo rocoso."),
            external("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWln0GjeJ7RDQSZPiHl-YSnAwIMqZjB9CeK1euE9RjlIOkQvu7aLbPyXdyO8R98Ti5SZx3J8QXOkXoSd2eSgWHmMsBlypslpgdBh78yhXdOMwrTqnp4aDPi0LVqeolvdLXmzFtu-=w1200-h800-k-no", "https://www.google.com/maps/search/?api=1&query=Masitise+Cave+House+and+Museum+Lesotho", "Google Maps · autor visible en la ficha", "Interior y colección del mismo museo de Masitise."),
        ],
        20: [
            commons("Sehlabathebe National Park.jpg", "Luke N. Vargas Dontexpect · dominio público", "Formaciones de arenisca en Sehlabathebe National Park."),
            commons("Early Morning view from Sehlabathebe House - panoramio.jpg", "Graham Maclachlan · CC BY-SA 3.0", "Vista matinal desde Sehlabathebe House dentro del parque."),
        ],
    },
}


HISTORY = {
    "esuatini": {
        "historia_resumen": "La historia de Esuatini enlaza la extracción prehistórica de ocre en Ngwenya y el arte san con la formación de un reino dlamini, la presión colonial por la tierra y una independencia obtenida en 1968 bajo Sobhuza II. La ruptura constitucional de 1973, el sistema Tinkhundla y la Constitución de 2005 explican por qué la monarquía conserva amplios poderes. Lion Cavern, Lobamba, Mantenga y los proyectos comunitarios permiten recorrer estas capas sin reducir el país a ceremonias o safaris.",
        "historia_secciones": [
            ["Ngwenya y las huellas más antiguas", "Bomvu Ridge conserva una historia minera mucho anterior al hierro industrial: en Lion Cavern se extrajeron hematita especular y ocre durante la prehistoria. La datación y el alcance exacto han variado entre publicaciones, por lo que la ficha usa el intervalo que comunica la autoridad turística y evita convertirlo en un récord indiscutible. El arte rupestre de Nsangwini documenta otra capa de comunidades san; sus figuras se interpretan localmente, pero no todas permiten una lectura única."],
            ["Formación del reino suazi", "Grupos nguni vinculados a la casa Dlamini consolidaron poder en la región entre los siglos XVIII y XIX. Sobhuza I estableció el centro del reino en el territorio actual y Mswati II amplió y cohesionó su influencia; de su nombre derivó Swazi. El reino se construyó mediante alianzas, incorporaciones, conflicto y organización por hogares y regimientos, una realidad más compleja que la imagen turística de una cultura inmóvil."],
            ["Concesiones, tierra y dominio colonial", "A finales del siglo XIX, europeos obtuvieron numerosas concesiones mineras, ganaderas y de tierra mediante acuerdos muy desiguales. La administración pasó por arreglos con la República Sudafricana y, tras la guerra sudafricana, por el control británico; desde 1906 Swazilandia fue administrada como protectorado. Gran parte de la tierra quedó en manos de colonos, y la recuperación de territorio se convirtió en un eje político duradero."],
            ["Sobhuza II e independencia", "Sobhuza II fue reconocido como jefe supremo durante la etapa colonial y encabezó una estrategia prolongada de peticiones, negociación y recompra de tierras. La movilización política creció en los años sesenta y el país alcanzó la independencia el 6 de septiembre de 1968 como monarquía constitucional. El largo reinado de Sobhuza II conectó instituciones tradicionales, propiedad territorial y construcción del nuevo Estado."],
            ["El decreto de 1973 y Tinkhundla", "Tras las elecciones de 1972, Sobhuza II abrogó la Constitución de independencia mediante la proclamación de abril de 1973 y asumió poderes legislativos, ejecutivos y judiciales. En 1978 se restableció un Parlamento dentro del sistema Tinkhundla, basado en circunscripciones y representación sin competencia partidista ordinaria. La Constitución de 2005 reconoce derechos e instituciones separadas, pero mantiene al rey como jefe de Estado ceremonial y ejecutivo y con amplias facultades de nombramiento."],
            ["Esuatini contemporánea", "Mswati III reina desde 1986 y en 2018 cambió oficialmente el nombre inglés del país de Swaziland a Eswatini. Modernización, industria regional, VIH, desempleo y desigualdad conviven con la centralidad de la monarquía y de las ceremonias nacionales. Las protestas prodemocráticas de 2021 y la respuesta letal de las fuerzas de seguridad siguen siendo un asunto abierto: la auditoría lo documenta con una fuente de derechos humanos y no presenta la estabilidad actual como ausencia de conflicto político."],
        ],
        "historia_fuentes": [
            ["Turismo de Esuatini · Lion Cavern", "https://www.thekingdomofeswatini.com/north-west-eswatini/ngwenya-mine-lion-cavern/"],
            ["Parliament of Eswatini · Background", "https://www.parliament.gov.sz/about/background/"],
            ["Gobierno de Esuatini · Constitution 2005", "https://www.gov.sz/index.php/resources/constitution"],
            ["Encyclopaedia Britannica · Eswatini, History", "https://www.britannica.com/place/Eswatini/History"],
            ["ENTC · patrimonio y reservas", "https://entc.org.sz/"],
            ["Human Rights Watch · protestas de 2021", "https://www.hrw.org/report/2025/10/30/youll-die-waiting-for-justice/impunity-for-security-forces-abuses-in-june-2021"],
        ],
    },
    "lesoto": {
        "historia_resumen": "Lesoto se formó alrededor de la diplomacia y las fortalezas de Moshoeshoe I durante las crisis regionales del siglo XIX. La protección británica preservó un territorio basotho separado del futuro Estado sudafricano, pero no evitó pérdidas de tierra ni dominio colonial. Desde la independencia de 1966, la monarquía constitucional ha convivido con golpes, disputas electorales, intervenciones regionales y gobiernos de coalición. Thaba Bosiu, Butha-Buthe, Liphofung, Morija y las presas del LHWP permiten leer historia política, cultural e hidráulica en lugares concretos.",
        "historia_secciones": [
            ["Antes de la nación basotho", "El territorio conserva abrigos y pinturas asociados a comunidades san cazadoras-recolectoras, hoy visibles en lugares como Liphofung y Sehlabathebe. Agricultores y pastores de lenguas bantú se asentaron posteriormente y formaron comunidades diversas, entre ellas grupos sotho-tswana y baphuthi. Hablar de una sola población que reemplaza a otra borra siglos de convivencia, incorporación, desplazamiento y memoria viva."],
            ["Moshoeshoe, Butha-Buthe y Thaba Bosiu", "A comienzos del siglo XIX, Moshoeshoe reunió clanes y personas desplazadas durante un periodo de guerra, sequía y movimientos regionales. Butha-Buthe fue una de sus primeras fortalezas; en 1824 trasladó el centro a Thaba Bosiu, una meseta más defendible. Su autoridad combinó capacidad militar, alianzas, acogida y diplomacia. La candidatura de UNESCO presenta estos lugares como una red de formación nacional, no como monumentos aislados."],
            ["Misioneros, escritura y guerras por la tierra", "Misioneros protestantes franceses llegaron en 1833 y Morija se convirtió en un centro de imprenta, educación y producción escrita en sesotho. Al mismo tiempo, la expansión de colonos bóeres desde el oeste provocó tratados disputados y las guerras del Estado Libre–Basotho. Ante la pérdida territorial, Moshoeshoe solicitó protección británica en 1868. Las fronteras posteriores dejaron amplias tierras basotho fuera del territorio de Lesoto."],
            ["Basutolandia y la Guerra de los Fusiles", "Basutolandia fue anexada a la Colonia del Cabo en 1871. La resistencia a una política de desarme desembocó en la Guerra de los Fusiles de 1880–81, tras la que la administración colonial del Cabo perdió capacidad de imponer su programa. En 1884 el territorio volvió al control directo de la Corona británica. Autoridades coloniales y jefaturas coexistieron de forma tensa hasta el desarrollo de consejos y partidos modernos en el siglo XX."],
            ["Independencia y crisis constitucionales", "Basutolandia se convirtió en el Reino de Lesoto independiente el 4 de octubre de 1966, con Moshoeshoe II como monarca y Leabua Jonathan como primer ministro. En 1970 Jonathan anuló unas elecciones que iba perdiendo y suspendió el orden constitucional. Un golpe militar lo depuso en 1986; el gobierno electo regresó en 1993. La crisis postelectoral de 1998 produjo violencia e intervención regional, y episodios posteriores mostraron que la competencia entre partidos y fuerzas de seguridad seguía siendo frágil."],
            ["Agua, coaliciones y Lesoto actual", "El tratado de 1986 con Sudáfrica creó el Lesotho Highlands Water Project: Katse, Mohale, túneles y generación hidroeléctrica transformaron carreteras e ingresos, pero también desplazaron comunidades y exigieron compensación y restauración de medios de vida. Desde 2012 se han sucedido coaliciones y reformas institucionales en un país muy dependiente de Sudáfrica, las remesas, el textil, el agua y los diamantes. La montaña no es un decorado vacío: sostiene aldeas, pastoreo y decisiones sobre recursos."],
        ],
        "historia_fuentes": [
            ["Gobierno de Lesoto · historia y datos del país", "https://www.gov.ls/about-lesotho/"],
            ["UNESCO · Basotho Nation-building Cluster", "https://whc.unesco.org/en/tentativelists/6920/"],
            ["Embassy of Lesotho · historia de Moshoeshoe", "https://www.lesothoemb-usa.gov.ls/about-lesotho/"],
            ["Morija Museum & Archives", "https://morijamuseum.org/"],
            ["Encyclopaedia Britannica · Lesotho, History", "https://www.britannica.com/place/Lesotho/History"],
            ["LHDA · historia del Lesotho Highlands Water Project", "https://www.lhda.org.ls/about/ourStory"],
        ],
    },
}


HISTORY_NOTES = {
    "esuatini": [
        "Lion Cavern se presenta con el intervalo comunicado por la autoridad turística, no como un récord universal indiscutible.",
        "El decreto de 1973, el restablecimiento parlamentario de 1978 y la Constitución de 2005 se distinguen cronológicamente.",
        "Las protestas de 2021 y la ausencia de rendición de cuentas se apoyan en una investigación específica de derechos humanos.",
    ],
    "lesoto": [
        "La formación basotho se explica como alianza e incorporación de comunidades, no como una historia étnica lineal.",
        "La protección británica de 1868 se distingue de la anexión al Cabo en 1871 y del control directo de la Corona desde 1884.",
        "El LHWP se presenta con beneficios, desplazamientos y obligaciones de compensación; se han eliminado royalties y costes antiguos que podían inducir a error.",
    ],
}


# La ficha operativa anterior contenía varios eslóganes turísticos presentados
# como hechos y daba por confirmadas recargas de agua que aún no han pasado la
# auditoría específica. Se conserva su estructura y diseño, pero se rebajan esas
# afirmaciones a lo que realmente permiten sostener las fuentes consultadas.
FICHA_REPLACEMENTS = {
    "esuatini": {
        "Sibebe (2º monolito del mundo) · Malolotja · Mlilwane a pie y en bici":
            "Sibebe · Malolotja · Mlilwane a pie y en bici",
        "Ngwenya: la mina más antigua del mundo, 43.000 años":
            "Ngwenya: extracción prehistórica de ocre en Lion Cavern",
        "el yacimiento minero más antiguo del mundo":
            "un yacimiento prehistórico de extracción de ocre",
        "la mina más antigua del mundo":
            "Lion Cavern y su extracción prehistórica de ocre",
        "La mina de Ngwenya (Lion Cavern) es el yacimiento minero más antiguo conocido del mundo: 41.000-43.000 años, y no se extraía metal sino ocre rojo para ritual y cosmética.":
            "Lion Cavern conserva evidencias de extracción prehistórica de ocre y hematita. Las dataciones publicadas varían; consultar la interpretación vigente de ENTC antes de presentar una cifra como definitiva.",
        "La mina de Ngwenya (Lion Cavern) es un yacimiento prehistórico de extracción de ocre: 41.000-43.000 años, y no se extraía metal sino ocre rojo para ritual y cosmética.":
            "Lion Cavern conserva evidencias de extracción prehistórica de ocre y hematita. Las dataciones publicadas varían; consultar la interpretación vigente de ENTC antes de presentar una cifra como definitiva.",
        "descrita como el segundo monolito más grande del mundo tras Uluru y el mayor plutón de granito expuesto del planeta":
            "una gran cúpula de granito expuesto, sin recurrir a clasificaciones mundiales no comparables",
        "la minería empezó en el mundo hace 43.000 años, aquí":
            "Lion Cavern conserva evidencias muy antiguas de extracción de ocre",
        "Agua embotellada en supermercados de todo el país. Campings de Mlilwane, Malolotja, Hlane, Maguga y Phophonyane permiten llenar el depósito de uso general con manguera; confirmar en recepción.":
            "Agua embotellada en supermercados de todo el país. Mlilwane, Malolotja, Hlane, Maguga y Phophonyane son candidatos de recarga, no puntos confirmados: pedir por escrito acceso del vehículo, manguera o rosca, caudal, coste y uso permitido.",
        "Recarga del depósito de uso general: campings de Mlilwane, Malolotja, Hlane, Maguga y Phophonyane permiten llenar con manguera; confirmar en recepción.":
            "Recarga del depósito de uso general: esos campings son candidatos pendientes; no contar con ellos hasta confirmar por escrito acceso del vehículo, conexión, caudal, coste y permiso para llenar.",
        "Arroyos de montaña de Malolotja: agua limpia, pero filtrar y potabilizar siempre.":
            "Arroyos de montaña de Malolotja: no asumir potabilidad ni caudal; filtrar y potabilizar si la gestión autoriza la captación.",
    },
    "lesoto": {
        "SANI PASS: 1.332 m de desnivel con rampas de hasta el 33%":
            "SANI PASS: cruce 4x4 de montaña; confirmar firme y horario",
        "EL PUB MÁS ALTO DE ÁFRICA": "SANI TOP",
        "Sani Top, 2.874 m": "Lodge y escarpe junto al paso; cota aproximada",
        "el Tlaeeng es la carretera asfaltada más alta de África austral":
            "Tlaeeng es un puerto de más de 3.200 m cuya información publicada sobre trazado y firme no es uniforme",
        "Tlaeeng —el asfalto más alto de África austral—":
            "Tlaeeng —un corredor de alta montaña—",
        "paso de Tlaeeng (3.275 m)":
            "paso de Tlaeeng (más de 3.200 m; la cota publicada varía)",
        "El Tlaeeng, a unos 3.275 m, es la carretera asfaltada más alta de África austral.":
            "Tlaeeng supera los 3.200 m; confirmar el trazado, el firme y el estado con información local, porque las fuentes publicadas no son uniformes.",
        "Sani Top (pub más alto de África)": "Sani Top (lodge en el escarpe)",
        "con el pub más alto de África al lado":
            "junto al pub que el operador promociona como el más alto de África",
        "El pub más alto de África cumple":
            "El pub que el operador promociona como el más alto de África",
        "rampas de hasta el 33% (1:3)": "rampas muy pronunciadas",
        "Rampas de hasta el 33%": "Rampas muy pronunciadas",
        "1.332 m de desnivel en pocos kilómetros": "un gran desnivel en pocos kilómetros",
        "Reductora obligatoria":
            "La reductora puede ser necesaria según el vehículo y el estado de la pista; confirmar condiciones",
        "Agua embotellada en Maseru y en las cabeceras de distrito. El agua de los arroyos de altura es de las más limpias del continente (es la que Lesoto vende a Sudáfrica), pero hay ganado por todas partes: filtrar y potabilizar siempre. Lodges de Semonkong, Malealea y Ts'ehlanyane permiten llenar el depósito de uso general.":
            "Agua embotellada en Maseru y en las cabeceras de distrito. No asumir potabilidad en arroyos de altura: hay ganado en las cuencas. Semonkong, Malealea y Ts'ehlanyane son candidatos de recarga, no puntos confirmados; verificar acceso, conexión, caudal, coste y permiso.",
        "Recarga del depósito de uso general: lodges y campings de Ts'ehlanyane, Semonkong, Malealea, Katse y Sani Top permiten llenar con manguera; confirmar en recepción.":
            "Recarga del depósito de uso general: esos lodges y campings son candidatos pendientes; no contar con ellos hasta confirmar por escrito acceso del vehículo, conexión, caudal, coste y permiso para llenar.",
        "Arroyos de altura: el agua de Lesoto es la que se vende a Sudáfrica y es de excelente calidad, pero hay ganado en todas las cuencas. Filtrar y potabilizar siempre antes de beber.":
            "Arroyos de altura: no extrapolar la calidad del agua exportada a una captación superficial. Hay ganado en las cuencas; filtrar y potabilizar, y captar solo donde esté permitido.",
    },
}


COMMON_FICHA_REPLACEMENTS = {
    "Puntos verificados o de referencia para esta recarga:":
        "Candidatos todavía pendientes de auditoría operativa para esta recarga:",
    "Puntos y comentarios recientes verificados también en":
        "Consultar también comentarios recientes en",
}


def replace_deep(value, replacements):
    if isinstance(value, str):
        for old, new in replacements.items():
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [replace_deep(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: replace_deep(item, replacements) for key, item in value.items()}
    return value


def apply_country(country: str) -> None:
    path = ROOT / "content" / "pois" / f"{country}.json"
    pois = json.loads(path.read_text(encoding="utf-8"))
    by_number = {poi["n"]: poi for poi in pois}
    expected = set(by_number)
    for label, values in (
        ("coordenadas", COORDS[country]), ("nombres", NAMES[country]),
        ("contenido", CONTENT[country]), ("enlaces", LINKS[country]),
        ("fotografías", PHOTOS[country]),
    ):
        if set(values) != expected:
            raise ValueError(
                f"{country}: {label} incompletos; "
                f"faltan={sorted(expected-set(values))}; sobran={sorted(set(values)-expected)}"
            )
    for number, poi in by_number.items():
        poi["name"] = NAMES[country][number]
        poi["lat"], poi["lon"] = COORDS[country][number]
        poi["desc"] = CONTENT[country][number]["desc"]
        poi["visit"] = CONTENT[country][number]["visit"]
        poi["links"] = links(country, number)
        poi["photos"] = PHOTOS[country][number]
        primary = poi["photos"][0]
        poi["img"], poi["source"], poi["credit"] = primary["img"], primary["source"], primary["credit"]
    path.write_text(json.dumps(pois, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def apply_history(country: str) -> None:
    path = ROOT / "content" / "ficha" / f"{country}.json"
    ficha = json.loads(path.read_text(encoding="utf-8"))
    ficha.update(HISTORY[country])
    replacements = {**COMMON_FICHA_REPLACEMENTS, **FICHA_REPLACEMENTS[country]}
    ficha = replace_deep(ficha, replacements)
    if country == "esuatini":
        revised_sources = []
        for label, url in ficha.get("sources", []):
            if label.startswith("Wikipedia · Mina de Ngwenya"):
                revised_sources.append((
                    "Turismo de Esuatini · Lion Cavern y mina de Ngwenya",
                    "https://www.thekingdomofeswatini.com/north-west-eswatini/ngwenya-mine-lion-cavern/",
                ))
            elif label.startswith("Wikipedia · Sibebe"):
                revised_sources.append((
                    "Turismo de Esuatini · Sibebe Rock",
                    "https://www.thekingdomofeswatini.com/central-eswatini/sibebe-rock/",
                ))
            else:
                revised_sources.append((label, url))
        ficha["sources"] = revised_sources
    stale_labels = ("FOTOGRAFÍAS", "FOTOS PENDIENTES DE SUSTITUIR", "COORDENADAS APROXIMADAS", "Coordenadas aproximadas")
    cleaned_sections = []
    for section in ficha.get("custom_sections_post", []):
        cleaned_fields = []
        for field in section:
            if not isinstance(field, str):
                cleaned_fields.append(field)
                continue
            for label in stale_labels:
                field = re.sub(
                    rf"<tr ><td>{re.escape(label)}</td><td>.*?</td></tr>",
                    "",
                    field,
                    flags=re.DOTALL,
                )
            cleaned_fields.append(field)
        cleaned_sections.append(cleaned_fields)
    if cleaned_sections:
        ficha["custom_sections_post"] = cleaned_sections
    path.write_text(json.dumps(ficha, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    audit_path = ROOT / "audit" / "historia" / f"{country}.json"
    audit = {"slug": country, **HISTORY[country], "notas": HISTORY_NOTES[country]}
    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    for country_name in ("esuatini", "lesoto"):
        apply_country(country_name)
        apply_history(country_name)

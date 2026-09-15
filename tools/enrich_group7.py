#!/usr/bin/env python3
"""Auditoría editorial explícita del grupo 7.

Zimbabue, Botsuana y Sudáfrica. Los pines se comprobaron contra el objeto,
entrada, recepción o embarcadero visible en Google Maps. Las imágenes de
Commons se eligieron tras leer sus metadatos; una galería corta y exacta tiene
preferencia sobre una galería de relleno.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote, unquote


ROOT = Path(__file__).resolve().parents[1]


def commons(filename: str, credit: str, caption: str) -> dict[str, str]:
    encoded = quote(filename.replace(" ", "_"), safe="(),-._~'")
    return {
        "img": f"https://commons.wikimedia.org/wiki/Special:FilePath/{encoded}?width=1200",
        "source": f"https://commons.wikimedia.org/wiki/File:{encoded}",
        "credit": credit,
        "caption": caption,
    }


def existing_photo(poi: dict, caption: str) -> dict[str, str]:
    return {"img": poi["img"], "source": poi.get("source", ""),
            "credit": poi.get("credit", "Wikimedia Commons"), "caption": caption}


COORDS = {
    "zimbabue": {
        1: (-18.9508857, 32.6472909), 2: (-19.1189518, 32.7829751),
        3: (-18.2955556, 32.8419444), 4: (-18.4862536, 32.7937600),
        5: (-18.1447587, 32.6355953), 6: (-19.8050464, 32.8704041),
        7: (-20.2714635, 30.9327465), 8: (-20.1968115, 30.9993953),
        9: (-21.4435821, 32.0852065), 10: (-20.1557888, 28.5964800),
        11: (-20.4937625, 28.5137344), 12: (-20.1428081, 28.4232472),
        13: (-18.7307301, 26.9518970), 14: (-17.9248762, 25.8471380),
        15: (-17.9284388, 25.8572030), 16: (-17.9782777, 25.7101789),
        17: (-17.8249306, 31.0490431), 18: (-17.6105758, 31.1733842),
        19: (-17.3563676, 30.1299654), 20: (-15.7196224, 29.3697596),
        21: (-16.5221068, 28.7616692), 22: (-17.6460745, 27.8769037),
    },
    "botsuana": {
        1: (-17.7904370, 25.2627612), 2: (-17.8439677, 25.1434398),
        3: (-18.5649269, 24.0643615), 4: (-18.2955550, 23.9077560),
        5: (-19.1726216, 23.7523124), 6: (-19.1827346, 23.4113791),
        7: (-19.1945609, 23.2715508), 8: (-19.9788375, 23.4287228),
        9: (-19.8466520, 23.4022950), 10: (-18.3673364, 21.8389726),
        11: (-18.7585797, 21.7371520), 12: (-20.0230082, 21.3551783),
        13: (-21.5198275, 21.9447633), 14: (-21.4393011, 23.8138552),
        15: (-20.1121417, 24.7691109), 16: (-20.4554677, 24.5164678),
        17: (-20.8930000, 25.8190000), 18: (-20.3358281, 26.2540675),
        19: (-22.2344400, 26.7200800), 20: (-22.2140642, 29.1383946),
        21: (-24.6449002, 25.9073942),
    },
    "sudafrica": {
        1: (-26.2378709, 28.0083713), 2: (-26.2385326, 27.9088071),
        3: (-25.9671341, 27.6625094), 4: (-24.5721968, 30.7988405),
        5: (-25.0243125, 31.2401875), 6: (-28.3566100, 32.4202300),
        7: (-28.0687693, 32.1412880), 8: (-29.8527722, 31.0241951),
        9: (-28.7274420, 28.8908910), 10: (-28.5062938, 28.6187756),
        11: (-29.5879785, 29.2921966), 12: (-32.0412282, 29.1092604),
        13: (-34.0231825, 23.8960121), 14: (-33.3922296, 22.2143879),
        15: (-34.8332012, 19.9999780), 16: (-34.4204565, 19.2437189),
        17: (-33.9483352, 18.4029463), 18: (-34.3568425, 18.4739882),
        19: (-33.9064912, 18.4224036), 20: (-33.9374344, 18.8631788),
        21: (-32.3745153, 19.0623478), 22: (-32.3757643, 20.8108407),
        23: (-26.4725589, 20.6121781), 24: (-28.5912782, 20.3400825),
        25: (-30.1632648, 17.7780609), 26: (-28.1252047, 16.8912170),
    },
}


NAMES = {
    "zimbabue": {
        1: "Christmas Pass · mirador de Mutare", 2: "Vumba Botanical Garden",
        3: "Monte Nyangani · cumbre", 4: "Mtarazi Falls · mirador",
        5: "Ziwa Site Museum y terrazas", 6: "Chimanimani · oficina del parque",
        7: "Great Zimbabwe National Monument", 8: "Lake Mutirikwi Recreational Park",
        9: "Chilojo Cliffs · Gonarezhou", 10: "Natural History Museum · Bulawayo",
        11: "Matobo Hills · World’s View", 12: "Khami World Heritage Site",
        13: "Hwange National Park · Main Camp", 14: "Victoria Falls · entrada principal",
        15: "Victoria Falls Bridge", 16: "Zambezi National Park",
        17: "National Gallery of Zimbabwe · Harare", 18: "Domboshawa · roca y pinturas",
        19: "Chinhoyi Caves · Sleeping Pool", 20: "Mana Pools · base de Nyamepi",
        21: "Kariba Dam", 22: "Chizarira · Mucheni Gorge Viewpoint",
    },
    "botsuana": {
        1: "Kazungula Bridge", 2: "Chobe Riverfront · Sedudu Gate",
        3: "Savuti · campamento", 4: "Linyanti · campsite",
        5: "Khwai · North Gate", 6: "Moremi · Xakanaxa",
        7: "Mboma Island · salida de excursiones", 8: "Maun · Nhabe Museum",
        9: "Okavango · estación de mokoro Boro 2", 10: "Shakawe · Panhandle del Okavango",
        11: "Tsodilo Hills · museo y oficina", 12: "Gcwihaba Caves",
        13: "D’Kar · Kuru Art Project", 14: "CKGR · Deception Valley",
        15: "Baines Baobabs", 16: "Makgadikgadi · acceso de Khumaga",
        17: "Kubu Island · Lekhubu", 18: "Nata Bird Sanctuary",
        19: "Khama Rhino Sanctuary · entrada", 20: "Northern Tuli · acceso de Pont Drift",
        21: "Three Dikgosi Monument · Gaborone",
    },
    "sudafrica": {
        1: "Apartheid Museum · Johannesburgo", 2: "Mandela House · Soweto",
        3: "Cuna de la Humanidad · Maropeng", 4: "Three Rondavels View Point",
        5: "Kruger · Phabeni Gate", 6: "iSimangaliso · Bhangazi Gate",
        7: "Hluhluwe-iMfolozi · Memorial Gate", 8: "KwaMuhle Museum · Durban",
        9: "Drakensberg · Sentinel Car Park", 10: "Golden Gate · Glen Reenen",
        11: "Sani Pass", 12: "Hole-in-the-Wall",
        13: "Tsitsikamma · Storms River Mouth", 14: "Cango Caves",
        15: "Cabo Agulhas · extremo austral", 16: "Hermanus · Old Harbour Museum",
        17: "Table Mountain · estación inferior", 18: "Cape of Good Hope",
        19: "Robben Island · Nelson Mandela Gateway", 20: "Stellenbosch Village Museum",
        21: "Cederberg · Algeria Campsite", 22: "SALT · observatorio de Sutherland",
        23: "Kgalagadi · Twee Rivieren", 24: "Augrabies Falls",
        25: "Namaqua · Skilpad Rest Camp", 26: "Richtersveld · Sendelingsdrift",
    },
}


LINKS = {
    "zimbabue": {
        1: [("Gobierno de Manicaland · destinos de la región", "https://zimtreasury.co.zw/wp-content/uploads/2025/07/Manicaland-Compendium-Final-2025.pdf")],
        2: [("Gobierno de Manicaland · Bvumba", "https://zimtreasury.co.zw/wp-content/uploads/2025/07/Manicaland-Compendium-Final-2025.pdf")],
        3: [("ZimParks · Nyanga National Park", "https://www.zimparks.org.zw/nyanga-national-park/")],
        4: [("ZimParks · Nyanga National Park", "https://www.zimparks.org.zw/nyanga-national-park/")],
        5: [("NMMZ · museos de sitio", "https://www.nmmz.co.zw/site-museums/")],
        6: [("ZimParks · Chimanimani National Park", "https://www.zimparks.org.zw/chimanimani-national-park/")],
        7: [("UNESCO · Great Zimbabwe", "https://whc.unesco.org/en/list/364/")],
        8: [("Zimbabwe Tourism Authority · Lake Mutirikwi", "https://zimbabwetourism.net/portfolios/lake-mutirikwi-recreational-park/")],
        9: [("Gonarezhou · información práctica", "https://gonarezhou.org/visit-gonarezhou-national-park/frequently-asked-questions/")],
        10: [("NMMZ · Natural History Museum", "https://www.nmmz.co.zw/western-region-bulawayo/")],
        11: [("UNESCO · Matobo Hills", "https://whc.unesco.org/en/list/306/")],
        12: [("UNESCO · Khami Ruins", "https://whc.unesco.org/en/list/365/")],
        13: [("ZimParks · Hwange National Park", "https://www.zimparks.org.zw/hwange-national-park/")],
        14: [("UNESCO · Mosi-oa-Tunya / Victoria Falls", "https://whc.unesco.org/en/list/509/")],
        15: [("NMMZ · Victoria Falls y garganta", "https://www.nmmz.co.zw/western-region-bulawayo/")],
        16: [("ZimParks · Zambezi National Park", "https://www.zimparks.org.zw/zambezi-national-park/")],
        17: [("National Gallery of Zimbabwe", "https://www.nationalgallery.co.zw/")],
        18: [("NMMZ · museos de sitio", "https://www.nmmz.co.zw/site-museums/")],
        19: [("ZimParks · Chinhoyi Caves", "https://www.zimparks.org.zw/chinhoyi-caves-recreational-park/")],
        20: [("ZimParks · Mana Pools", "https://www.zimparks.org.zw/mana-pools-national-park/")],
        21: [("Zambezi River Authority · Kariba Dam", "https://www.zambezira.org/")],
        22: [("ZimParks · Chizarira National Park", "https://www.zimparks.org.zw/chizarira-national-park/")],
    },
    "botsuana": {
        1: [("African Development Bank · Kazungula Bridge", "https://www.afdb.org/en/projects-and-operations/p-z1-db0-031")],
        2: [("Botswana Tourism · Chobe", "https://www.botswanatourism.co.bw/explore/chobe-national-park")],
        3: [("Botswana Tourism · Chobe y Savuti", "https://www.botswanatourism.co.bw/explore/chobe-national-park")],
        4: [("Botswana Tourism · Chobe y Linyanti", "https://www.botswanatourism.co.bw/explore/chobe-national-park")],
        5: [("Botswana Tourism · Moremi", "https://www.botswanatourism.co.bw/explore/moremi-game-reserve")],
        6: [("Botswana Tourism · Moremi", "https://www.botswanatourism.co.bw/explore/moremi-game-reserve")],
        7: [("Botswana Tourism · Moremi", "https://www.botswanatourism.co.bw/explore/moremi-game-reserve")],
        8: [("Botswana Tourism · Maun", "https://botswanatourism.co.bw/index.php/explore/maun")],
        9: [("UNESCO · Okavango Delta", "https://whc.unesco.org/en/list/1432/")],
        10: [("Botswana Tourism · Okavango", "https://www.botswanatourism.co.bw/explore/okavango-delta")],
        11: [("UNESCO · Tsodilo", "https://whc.unesco.org/en/list/1021/")],
        12: [("Botswana Tourism · Gcwihaba Caves", "https://botswanatourism.co.bw/explore/gcwihaba-caves-and-aha-hills")],
        13: [("Kuru Art Project · visita y contacto", "https://kuruart.com/contact-us/")],
        14: [("Botswana Tourism · Central Kalahari", "https://www.botswanatourism.co.bw/explore/central-kalahari-game-reserve")],
        15: [("Botswana Tourism · Nxai Pan", "https://www.botswanatourism.co.bw/explore/nxai-pan-national-park")],
        16: [("Botswana Tourism · Makgadikgadi", "https://www.botswanatourism.co.bw/explore/makgadikgadi-pans-game-reserve")],
        17: [("Gaing O Community Trust · Lekhubu", "https://www.kubuisland.com/")],
        18: [("Botswana Tourism · Nata Bird Sanctuary", "https://www.botswanatourism.co.bw/explore/nxai-pan-national-park")],
        19: [("Khama Rhino Sanctuary", "https://www.khamarhinosanctuary.org.bw/")],
        20: [("Botswana Tourism · Northern Tuli", "https://botswanatourism.co.bw/explore/northern-tuli-game-reserve")],
        21: [("Botswana Tourism · Gaborone", "https://www.botswanatourism.co.bw/explore/gaborone")],
    },
    "sudafrica": {
        1: [("Apartheid Museum · visita", "https://www.apartheidmuseum.org/")],
        2: [("Mandela House · sitio oficial", "https://www.mandelahouse.com/")],
        3: [("Maropeng · Cuna de la Humanidad", "https://www.maropeng.co.za/")],
        4: [("Mpumalanga Tourism · Blyde River Canyon", "https://www.mpumalanga.com/our-provincial-parks/blyde-river-canyon-nature-reserve")],
        5: [("SANParks · Kruger", "https://www.sanparks.org/parks/kruger")],
        6: [("iSimangaliso · mapas y accesos", "https://www.isimangaliso.com/download-maps/")],
        7: [("Ezemvelo · Hluhluwe-iMfolozi", "https://www.kznwildlife.com/hluhluwe-imfolozi-park.html")],
        8: [("Durban Tourism · KwaMuhle Museum", "https://visitdurban.travel/space/kwamuhle-museum")],
        9: [("Ezemvelo · Royal Natal", "https://www.kznwildlife.com/royal-natal-national-park.html")],
        10: [("SANParks · Golden Gate Highlands", "https://www.sanparks.org/parks/golden-gate")],
        11: [("Border Management Authority · puertos de entrada", "https://www.bma.gov.za/wp-content/uploads/2025/02/South-African-Ports-of-Entry-21-1.pdf")],
        12: [("Eastern Cape Parks · Wild Coast", "https://www.visiteasterncape.co.za/regions/wild-coast/")],
        13: [("SANParks · Storms River Mouth", "https://www.sanparks.org/parks/garden-route/camps/storms-river-mouth")],
        14: [("Cango Caves · visita oficial", "https://www.cango-caves.co.za/")],
        15: [("SANParks · Agulhas", "https://www.sanparks.org/parks/agulhas")],
        16: [("Hermanus Tourism · Old Harbour Museum", "https://hermanus-tourism.co.za/things-to-do/museums-and-culture/")],
        17: [("Table Mountain Aerial Cableway", "https://www.tablemountain.net/plan-your-visit/")],
        18: [("SANParks · Cape Point y Cape of Good Hope", "https://www.sanparks.org/parks/table-mountain/what-to-do/attractions/cape-point")],
        19: [("Robben Island Museum · tipos de visita", "https://www.robben-island.org.za/tour-types/")],
        20: [("Stellenbosch Museum · Village Museum", "https://stelmus.co.za/village-museum/")],
        21: [("CapeNature · Cederberg", "https://www.capenature.co.za/reserves/cederberg-wilderness-area")],
        22: [("SAAO · visitar Sutherland", "https://www.saao.ac.za/visit-sutherland/")],
        23: [("SANParks · Kgalagadi", "https://www.sanparks.org/parks/kgalagadi")],
        24: [("SANParks · Augrabies Falls", "https://www.sanparks.org/parks/augrabies")],
        25: [("SANParks · Namaqua", "https://www.sanparks.org/parks/namaqua")],
        26: [("SANParks · Richtersveld", "https://www.sanparks.org/parks/richtersveld")],
    },
}


def links(country: str, number: int) -> list[dict[str, str]]:
    return [{"label": label, "url": url} for label, url in LINKS[country][number]]


def entry(desc: str, why: str, see: str, access: str, when: str, skip: str) -> dict:
    return {"desc": desc, "visit": {"why": why, "see": see, "access": access,
                                     "when": when, "skip": skip}}


CONTENT = {"zimbabue": {
    1: entry(
        "El paso montañoso que abre la vista sobre Mutare es una parada breve y una buena lectura del cambio de paisaje al entrar desde Mozambique.",
        "Ofrece una primera panorámica clara de las Eastern Highlands sin exigir un gran desvío.",
        "Valle de Mutare, laderas y trazado del paso; el museo urbano es una visita distinta.",
        "El pin coincide con Christmas Pass en Google Maps. Detenerse solo en apartadero seguro y sin invadir la calzada.",
        "Primera hora o final de la tarde, con visibilidad y tráfico moderado.",
        "Omitirlo con niebla, lluvia fuerte o si no hay un lugar seguro donde sacar el vehículo."),
    2: entry(
        "Jardín botánico de montaña en los Bvumba, con bosque húmedo, grandes árboles y notable avifauna. No representa todos los montes ni da acceso automático a fincas privadas.",
        "Es la forma más sencilla y concreta de conocer el ambiente fresco y boscoso de Bvumba.",
        "Senderos del jardín, vegetación afromontana y aves; Bunga Forest y Leopard Rock requieren planes separados.",
        "El pin coincide con la entrada de Vumba Botanical Garden. Confirmar apertura, estacionamiento y política de mascotas.",
        "Mañana despejada; llevar protección de lluvia incluso en estación relativamente seca.",
        "Descartarlo si el jardín está cerrado o las pistas de acceso están afectadas por lluvia."),
    3: entry(
        "La cumbre más alta de Zimbabue es una caminata de montaña dentro de Nyanga National Park. El pin marca la cima, no el aparcamiento ni una ruta de conducción.",
        "Aporta la jornada de alta montaña más clara del país y un paisaje de meseta distinto al safari.",
        "Pastizales, cabeceras de ríos y la cumbre; las vistas dependen por completo de la niebla.",
        "El pin coincide con Mount Nyangani en Google Maps. Registrar la salida y confirmar inicio, guía y ruta con ZimParks.",
        "Salida temprana con previsión estable, navegación y ropa impermeable.",
        "No subir con niebla cerrada, tormenta, inicio tardío o sin medio fiable de navegación."),
    4: entry(
        "Mirador sobre Mtarazi Falls y el valle de Honde, dentro del área de Nyanga. La altura y el vacío exigen permanecer en estructuras y senderos autorizados.",
        "Es la cascada más espectacular de las Eastern Highlands y una excursión razonable desde Nyanga.",
        "Salto, garganta y valle; tirolina y pasarela son actividades comerciales separadas.",
        "El pin coincide con Mtarazi Falls Viewpoint en Google Maps. Confirmar acceso y estado de la pista con el gestor.",
        "Con visibilidad y viento moderado; la mañana suele dar más margen meteorológico.",
        "Omitirlo con niebla, tormenta, viento fuerte o cierres del mirador."),
    5: entry(
        "Ziwa conserva recintos, muros, terrazas y estructuras excavadas que explican el paisaje agrícola histórico de Nyanga. Es un sitio arqueológico, no una reconstrucción completa.",
        "Permite ver un patrimonio menos conocido que Great Zimbabwe y leer cómo se organizó la ladera.",
        "Museo de sitio, muros, terrazas y estructuras de asentamiento con interpretación local.",
        "El pin coincide con Ziwa Site Museum. Llegar de día y confirmar guía, horario y permiso fotográfico.",
        "Mañana seca, con tiempo para recorrer el sitio sin prisa.",
        "No entrar si está cerrado ni caminar sobre muros o terrazas fuera del recorrido indicado."),
    6: entry(
        "La oficina del parque en Chimanimani es el ancla operativa para registrar rutas de varios días por montañas remotas. No se presenta el pin como refugio ni como cumbre.",
        "Es la base adecuada para decidir una travesía seria por uno de los paisajes más agrestes del país.",
        "Información de rutas, valle y acceso a montaña; Bailey’s Folly y refugios dependen del itinerario acordado.",
        "El pin coincide con Chimanimani National Park Office. Registrar plan, contactos y retorno antes de abandonar la base.",
        "Ventana seca y estable, con días de margen y equipo de montaña.",
        "No salir sin registro, cartografía, previsión, agua y confirmación local de senderos y fronteras."),
    7: entry(
        "Capital medieval de piedra seca y principal conjunto arqueológico del país, con complejo de la colina, Gran Recinto y ruinas del valle.",
        "Es la visita histórica imprescindible para comprender el origen del nombre y símbolos nacionales.",
        "Muros sin mortero, torre cónica, pasos de la colina y museo; cada sector requiere tiempo.",
        "El pin coincide con Great Zimbabwe National Monument. Aparcar en el recinto y contratar guía oficial si se desea interpretación.",
        "Primera hora para evitar calor y dedicar entre media jornada y una jornada tranquila.",
        "No reducirlo a una foto exterior ni subir la colina con calor extremo o movilidad insuficiente."),
    8: entry(
        "Área recreativa en la orilla de Lake Mutirikwi, separada de la ciudad de Masvingo y del monumento de Great Zimbabwe. Sirve como pausa lacustre y base de descanso.",
        "Añade paisaje de embalse y una noche tranquila sin convertir Masvingo en una ficha logística genérica.",
        "Orilla, vegetación y vistas del lago; pesca o navegación solo con operador y permiso.",
        "El pin coincide con Lake Mutirikwi Recreational Park. Confirmar acceso, camping y zonas permitidas al llegar.",
        "Final de la tarde o una noche entre Great Zimbabwe y el siguiente tramo.",
        "Descartarlo si no hay camping confirmado, el acceso está cerrado o se pretende bañarse sin evaluación local."),
    9: entry(
        "Muralla de arenisca roja sobre el río Runde, dentro de Gonarezhou. La ficha se ancla en el mirador real de Chilojo, no en el centro del parque.",
        "Es el paisaje más reconocible de Gonarezhou y recompensa un desvío de safari remoto.",
        "Acantilados, valle del Runde y fauna posible sin garantía; Chipinda Pools es otra zona del parque.",
        "El pin coincide con Chilojo Cliffs en Google Maps. Reserva, 4x4, combustible y estado de cruces deben confirmarse antes.",
        "Varios días y estación accesible; luz lateral al amanecer o atardecer desde zona autorizada.",
        "No ir con lluvias, vados inciertos, autonomía insuficiente o sin campamento reservado."),
    10: entry(
        "Museo de historia natural de Bulawayo con colecciones zoológicas, geológicas y arqueológicas; convierte la parada urbana en una visita concreta.",
        "Aporta contexto científico al viaje y puede combinarse con reparaciones y aprovisionamiento.",
        "Salas de fauna, geología y culturas regionales; comprobar qué exposiciones están abiertas.",
        "El pin coincide con Natural History Museum of Zimbabwe. Usar estacionamiento vigilado y consultar horario.",
        "Día laborable o mañana de fin de semana con apertura confirmada.",
        "No desplazarse hasta allí sin verificar apertura ni contar con acceso del perro al interior."),
    11: entry(
        "World’s View ocupa una cumbre sagrada de Matobo y contiene la tumba de Cecil Rhodes, figura colonial controvertida. El paisaje y la memoria viva requieren una lectura crítica y respetuosa.",
        "Combina los grandes kopjes graníticos con una capa histórica y política que no debe simplificarse.",
        "Panorama de Matobo y tumbas coloniales; arte rupestre y rastreo de rinoceronte son visitas separadas.",
        "El pin coincide con Grave of Cecil Rhodes/World’s View. Pagar entrada y seguir las indicaciones culturales y del parque.",
        "Mañana o tarde con roca seca; reservar tiempo adicional para un abrigo rupestre guiado.",
        "No tratar el lugar como homenaje acrítico ni improvisar vivac, agua o recorridos fuera de sendero."),
    12: entry(
        "Khami conserva plataformas aterrazadas y muros decorados de piedra seca posteriores al auge de Great Zimbabwe. Suele requerir menos tiempo y recibe menos visitantes.",
        "Permite comparar dos tradiciones urbanas sin repetir exactamente la experiencia de Great Zimbabwe.",
        "Terrazas, motivos murales, pasos y paisaje del río Khami con interpretación arqueológica.",
        "El pin coincide con Khami World Heritage Site. Confirmar horario y estado del último acceso desde Bulawayo.",
        "Media jornada con luz suave y terreno seco.",
        "No subir a muros ni ir tras lluvias fuertes sin confirmar que la pista final es practicable."),
    13: entry(
        "Main Camp es la puerta práctica al sector oriental de Hwange y a sus circuitos de pozas. La ficha no promete cifras de fauna ni avistamientos concretos.",
        "Hwange ofrece uno de los grandes safaris de la ruta y Main Camp facilita una primera visita autónoma.",
        "Pistas, pozas y fauna de sabana; cada circuito depende de agua, mantenimiento y cierres.",
        "El pin coincide con Hwange Main Camp. Entrar con reserva, combustible y horarios de puerta confirmados.",
        "Mínimo dos noches; primeras y últimas horas del día son las mejores para observar fauna.",
        "No entrar con mascota, sin alojamiento o con autonomía insuficiente para cambios de circuito."),
    14: entry(
        "La entrada principal del lado zimbabuense da acceso al sendero de miradores del bosque lluvioso frente a Victoria Falls. Caudal y spray cambian mucho según la estación.",
        "Es una de las grandes visitas naturales del viaje y el lado zimbabuense ofrece una larga sucesión de miradores.",
        "Cortina de agua, garganta y bosque húmedo; algunos miradores pueden quedar casi ocultos por spray.",
        "El pin coincide con Victoria Falls Main Entrance. Comprar entrada oficial y proteger equipo y documentación del agua.",
        "Primera hora; elegir ropa impermeable con alto caudal y valorar mejor visibilidad en caudal menor.",
        "No acercarse a bordes no autorizados ni confundir actividades de Livingstone Island con este acceso."),
    15: entry(
        "Puente histórico y fronterizo sobre la segunda garganta, con vistas al Batoka y al spray de las cataratas. Cruzarlo implica controles internacionales, aunque se visite solo el puente.",
        "Añade una lectura de ingeniería y una perspectiva distinta de la garganta.",
        "Arco metálico, garganta y frontera; puenting y otras actividades requieren operador aparte.",
        "El pin coincide con Victoria Falls Bridge. Llevar documentación y consultar cómo acceder sin completar un cruce fronterizo.",
        "De día, con tráfico moderado y visibilidad.",
        "No detener el vehículo sobre el puente ni iniciar trámites fronterizos sin comprender el retorno y los visados."),
    16: entry(
        "Parque ribereño aguas arriba de Victoria Falls, útil para un safari corto desde la ciudad. El pin marca el objeto del parque; puerta y actividad se confirman al reservar.",
        "Permite añadir ribera del Zambeze y fauna sin asumir una expedición de varios días.",
        "Bosque de ribera, río y fauna posible; no sustituye a Hwange ni garantiza especies.",
        "El pin coincide con Zambezi National Park en Google Maps, pero no con una recepción concreta. Confirmar puerta, guía y recogida.",
        "Mañana o tarde, como actividad reservada desde Victoria Falls.",
        "No intentar localizar una entrada por el pin general ni dejar al perro en el coche durante el safari."),
    17: entry(
        "Galería nacional de Harare con arte moderno y contemporáneo de Zimbabue y la región. Es una visita cultural concreta dentro de una escala principalmente logística.",
        "Evita reducir la capital a trámites y muestra prácticas artísticas que no aparecen en los sitios arqueológicos.",
        "Exposiciones temporales y colección; contenido y salas cambian, por lo que conviene consultar programa.",
        "El pin coincide con National Gallery of Zimbabwe. Llegar de día y usar estacionamiento seguro.",
        "Día laborable o fin de semana con horario confirmado.",
        "No ir sin revisar apertura ni contar con acceso del perro al edificio."),
    18: entry(
        "Afloramiento granítico visitable cerca de Harare con vistas y pinturas rupestres en abrigo. Sustituye la mezcla anterior con Epworth: esta ficha trata solo Domboshawa.",
        "Es una excursión corta que combina paisaje, caminata y arqueología sin un largo desvío.",
        "Gran losa de granito, panorámica y paneles rupestres; su estado exige no tocar las pinturas.",
        "El pin coincide con Domboshawa en Google Maps. Pagar acceso, preguntar por guía y aparcar en el recinto.",
        "Mañana o última hora con roca seca y tiempo para bajar antes de oscuridad.",
        "No subir con tormenta, roca mojada o calor extremo ni entrar en abrigos cerrados."),
    19: entry(
        "Sistema de cavidades con el intenso azul del Sleeping Pool, accesible por escaleras dentro de un parque recreativo. Profundidad y buceo no deben tratarse como actividad casual.",
        "Es una parada geológica muy singular en el corredor Harare–Kariba.",
        "Boca de la cueva, paredes calizas y Sleeping Pool desde los puntos habilitados.",
        "El pin coincide con Chinhoyi Caves. Confirmar horario y permanecer en pasarelas y escaleras autorizadas.",
        "Con luz diurna y calzado de agarre; reservar una o dos horas.",
        "No bañarse, bucear ni acercarse al agua fuera de una actividad técnica expresamente autorizada."),
    20: entry(
        "Nyamepi es la base principal de la llanura aluvial de Mana Pools. El pin se ha fijado en un campsite operativo y no en un punto genérico del parque.",
        "Permite vivir el Zambeze y sus bosques de ribera en uno de los espacios más remotos de la ruta.",
        "Llanura aluvial, pozas, río y fauna posible; caminar solo se decide según normas y briefing vigentes.",
        "El pin coincide con Nyamepi 27. Reserva, puerta, combustible, comida y agua deben cerrarse antes de la larga aproximación.",
        "Varios días en temporada de acceso, con llegadas diurnas y margen para la pista.",
        "No entrar sin reserva ni interpretar la fama de caminar como permiso automático para hacerlo sin guía."),
    21: entry(
        "La presa de Kariba cruza el Zambeze y explica el enorme embalse compartido por Zimbabue y Zambia. Es infraestructura crítica y el acceso puede cambiar.",
        "Ofrece una escala de ingeniería y paisaje lacustre distinta de los parques de fauna.",
        "Muro, aliviaderos y lago desde puntos permitidos; Matusadona exige otro plan y otro acceso.",
        "El pin coincide con Kariba Dam. Llevar documentación y obedecer controles, prohibiciones de parada y fotografía.",
        "De día, con nivel y restricciones consultados previamente.",
        "No bloquear la vía, volar dron ni fotografiar zonas sensibles; omitirlo si la autoridad restringe visitas."),
    22: entry(
        "Mucheni Gorge Viewpoint permite leer la gran escarpa de Chizarira desde un punto concreto. El aislamiento del parque es parte del atractivo y del riesgo logístico.",
        "Es una opción para quien busca un parque remoto y paisaje de garganta más que densidad garantizada de fauna.",
        "Escarpa, garganta y bosque; servicios, agua y fauna pueden ser muy limitados.",
        "El pin coincide con Mucheni Gorge Viewpoint. Confirmar apertura, pistas, campamento y combustible con ZimParks.",
        "Con varios días, tiempo seco y llegada temprana.",
        "Descartarlo sin comunicaciones, autonomía, reserva o información reciente del estado de las pistas."),
}, "botsuana": {
    1: entry(
        "El puente carretero y ferroviario sobre el Zambeze enlaza Botsuana y Zambia. El pin marca el puente real, no el centro de Kasane ni un supuesto punto cuádruple visitable.",
        "Es una obra fronteriza clave de la ruta y permite entender la singular geografía de Kazungula.",
        "El gran arco sobre el río y la actividad fronteriza; las cuatro fronteras no convergen en un monumento accesible.",
        "El pin coincide con Kazungula Bridge. Cruzarlo exige completar inmigración, aduana y trámites de vehículo.",
        "A primera hora, dejando margen para colas y comprobaciones.",
        "No parar ni caminar por zonas aduaneras salvo indicación expresa."),
    2: entry(
        "Sedudu Gate es la entrada concreta al Riverfront de Chobe, uno de los circuitos de fauna más accesibles del país. Un crucero por el río es una actividad diferente.",
        "Concentra paisaje fluvial y buenas posibilidades de observar fauna en una jornada bien planificada.",
        "Río, llanuras y fauna silvestre sin garantía de especie ni distancia.",
        "El pin coincide con Sedudu Gate. Confirmar permiso, reserva, horario y normas del vehículo antes de entrar.",
        "Amanecer o tarde; dedicar medio día como mínimo.",
        "No entrar con mascota ni confiar en que el coche pueda sustituir un cuidado seguro."),
    3: entry(
        "Savuti es el sector seco y remoto de Chobe articulado alrededor de su canal y su campamento. La arena profunda cambia mucho con la estación.",
        "Ofrece una experiencia de sabana muy distinta del Riverfront y justifica varias noches.",
        "Canal, marismas estacionales, baobabs y fauna posible; ningún avistamiento está garantizado.",
        "El pin coincide con Savuti Camp. Reserva obligatoria, 4x4, dos vehículos, combustible y presiones ajustables.",
        "Dos o más noches en periodo transitable y llegando con luz.",
        "Descartarlo sin reserva, autonomía, recuperación o información reciente de la pista."),
    4: entry(
        "Linyanti Campsite es una pequeña base remota junto al río, en el extremo occidental de Chobe. No debe confundirse con alojamientos privados de la concesión.",
        "Interesa por la ribera tranquila y el aislamiento, no como escala rápida.",
        "Bosque de ribera, agua y fauna posible desde una zona de acampada muy limitada.",
        "El pin coincide con Linyanti Campsite 1. Confirmar reserva y ruta de acceso exacta con DWNP.",
        "Con al menos dos noches y llegada diurna.",
        "No asumir agua, combustible, cobertura ni disponibilidad de parcela."),
    5: entry(
        "North Gate es el acceso a Moremi desde Khwai y un punto operativo mucho más útil que un pin genérico en la reserva.",
        "Permite enlazar Khwai con los circuitos de Moremi sin retroceder a Maun.",
        "Bosque, llanuras y pasos de agua; los cruces y la fauna dependen de la estación.",
        "El pin coincide con North Gate. Llevar reserva, combustible, 4x4 y estado actualizado de puentes y vados.",
        "Llegada temprana y siempre con margen de luz.",
        "No cruzar agua sin reconocer profundidad ni entrar con mascota."),
    6: entry(
        "Xakanaxa es el nodo de campamento y embarcaderos de Moremi donde se encuentran canales permanentes y tierra seca.",
        "Es una base excelente para combinar conducción de safari y salida en barca reservada.",
        "Lagunas, canales y fauna posible; Third Bridge es otro sector y puede requerir ruta distinta.",
        "El pin coincide con Xakanaxa Camp. Confirmar parcela, embarcadero, operador y pista de llegada.",
        "Dos o tres noches, con actividades a primera y última hora.",
        "No depender de disponibilidad espontánea ni improvisar cruces inundados."),
    7: entry(
        "Mboma Island Expeditions es un punto concreto de salida para recorridos acuáticos desde Moremi. La ficha no presenta toda la isla como acceso libre.",
        "Añade una lectura silenciosa de canales y humedales que no se obtiene desde el coche.",
        "Mokoro o barca según nivel, operador y reserva; fauna posible sin garantía.",
        "El pin coincide con Mboma Island Expeditions. Reservar directamente y acordar llegada, aparcamiento y equipaje.",
        "Mañana, con viento y nivel de agua adecuados.",
        "No presentarse sin reserva ni llevar mascota a la actividad."),
    8: entry(
        "Nhabe Museum ocupa un edificio histórico de Maun y explica culturas y paisaje del noroeste. Convierte la parada logística en una visita breve y concreta.",
        "Da contexto humano al delta antes o después de los safaris.",
        "Colecciones y exposiciones locales; su disponibilidad puede variar.",
        "El pin coincide con Nhabe Museum. Confirmar apertura y estacionar dentro o en zona vigilada.",
        "En horario diurno, combinado con compras y combustible.",
        "Omitirlo si está cerrado; no contar con acceso del perro al interior."),
    9: entry(
        "Boro 2 es una estación comunitaria de salida en mokoro al sur de Maun. No es un mirador libre ni una coordenada genérica del delta.",
        "Ofrece una primera experiencia de canales con guías locales sin internarse varios días.",
        "Mokoro, juncos y canales; recorrido y duración dependen del nivel del agua.",
        "El pin coincide con Boro 2 Mokoro Polers Station. Acordar operador, traslado, chaleco y custodia del vehículo.",
        "Primera hora, evitando calor y viento.",
        "No ir sin confirmación de agua suficiente ni dejar al perro sin cuidador verificado."),
    10: entry(
        "Shakawe es la base urbana del Panhandle, la sección estrecha y permanente del Okavango. El interés está en el río, no en el centro de la población.",
        "Permite descansar, reabastecer y organizar una salida fluvial antes de Tsodilo.",
        "Canal principal, papiros y aves; pesca y navegación solo con operador.",
        "El pin marca Shakawe como ancla urbana. Elegir alojamiento con embarcadero y estacionamiento confirmado.",
        "Una noche o dos, con salida al amanecer o tarde.",
        "No usar el pin urbano como embarcadero ni asumir agua apta para consumo."),
    11: entry(
        "El museo de Tsodilo es el punto correcto para registrarse antes de recorrer colinas sagradas con miles de pinturas rupestres.",
        "Es uno de los conjuntos de arte rupestre más importantes del continente y exige interpretación local.",
        "Museo, senderos guiados y paneles de arte; las colinas no son un parque temático ni un recorrido libre.",
        "El pin coincide con Tsodilo Hills Museum. Registrarse, contratar guía y preguntar por camping y agua.",
        "Mañana fresca; reservar media jornada o más.",
        "No tocar pinturas, abandonar senderos ni fotografiar donde la comunidad lo restrinja."),
    12: entry(
        "Gcwihaba es un sistema de cuevas remoto en el Kalahari. Su acceso y visita requieren preparación; el pin marca el objeto real en Google Maps.",
        "Interesa por sus salas, espeleotemas y aislamiento, muy distintos del delta.",
        "Cavidades y fauna cavernícola; el recorrido depende de guía y condiciones.",
        "Confirmar por adelantado oficina, guía, pista, combustible, agua y lugar de acampada.",
        "Solo con reserva y varios días de margen en tiempo seco.",
        "Descartarlo sin contacto confirmado, equipo, dos vehículos o navegación fiable."),
    13: entry(
        "Kuru Art Project en D’Kar trabaja con artistas san contemporáneos. Es un estudio y proyecto cultural real, no una aldea presentada como espectáculo.",
        "Permite conocer voces actuales del Kalahari y comprar obra con trazabilidad.",
        "Estudio, grabados, pinturas y tienda según actividad del día.",
        "El pin coincide con Kuru Art Project. Concertar visita; el proyecto indica D’Kar, a unos 35 km de Ghanzi.",
        "Día laborable con cita o apertura confirmada.",
        "No fotografiar personas u obras sin permiso ni esperar demostraciones preparadas."),
    14: entry(
        "Deception Valley es un sector remoto del Central Kalahari Game Reserve. El pin marca el valle en Google Maps, no una puerta ni un campamento garantizado.",
        "Ofrece horizontes inmensos y una experiencia de autosuficiencia genuina en el Kalahari.",
        "Pans, pastizal y fauna estacional; las distancias entre servicios son enormes.",
        "Reservar campsite y confirmar puerta, ruta y pistas; llevar combustible, agua, comida y comunicaciones de sobra.",
        "Varios días, idealmente con dos vehículos y llegada diurna.",
        "No entrar con mascota, un solo margen de combustible o información antigua de la pista."),
    15: entry(
        "Los siete baobabs de Baines forman un hito histórico y paisajístico junto a Kudiakam Pan, dentro de Nxai Pan National Park.",
        "Es uno de los lugares más fotogénicos de las salinas y conserva una comparación excepcional con la pintura de 1862.",
        "Baobabs y borde de la salina; el estado del pan cambia por completo con la lluvia.",
        "El pin coincide con Baines Baobabs. Confirmar reserva, acceso 4x4 y condición de la pista.",
        "Luz de mañana o tarde y temporada transitable.",
        "No cruzar una salina húmeda ni entrar con mascota."),
    16: entry(
        "Khumaga es el acceso occidental de Makgadikgadi Pans National Park junto al Boteti; el cruce puede depender de puente o transbordador operativo.",
        "Da acceso a una ribera con fauna y a paisajes distintos de la salina abierta.",
        "Río Boteti, escarpa y fauna posible; el ferry no debe darse por garantizado.",
        "El pin coincide con Khumaga Camp. Confirmar con DWNP la vía de acceso y reservar camping.",
        "Dos noches y llegada con luz.",
        "No entrar con mascota ni depender de un transbordador sin confirmación reciente."),
    17: entry(
        "Lekhubu o Kubu Island es un afloramiento granítico con baobabs en medio de Sowa Pan, gestionado por un fideicomiso comunitario.",
        "Es la experiencia paisajística más singular de las salinas cuando el acceso es seguro.",
        "Baobabs, roca y horizonte blanco; no es una isla rodeada de agua en la estación seca.",
        "El pin coincide con Kubu Island. Reservar y obtener ruta y estado del pan del gestor comunitario.",
        "Solo en condiciones secas verificadas, con dos vehículos y navegación.",
        "No cruzar el pan con humedad ni circular fuera de trazas autorizadas."),
    18: entry(
        "Santuario comunitario junto a Nata con acceso a las orillas de Sua Pan. Las concentraciones de aves dependen del agua y la estación.",
        "Es la forma más sencilla de aproximarse a las salinas y su avifauna sin una travesía remota.",
        "Miradores, salina y aves variables; no se prometen flamencos.",
        "El pin coincide con Nata Bird Sanctuary. Consultar estado de pistas y observaciones recientes al entrar.",
        "Amanecer o tarde, especialmente tras periodos con agua.",
        "Omitirlo si el acceso está anegado o si se espera una especie concreta como garantía."),
    19: entry(
        "Reserva comunitaria cercada cerca de Serowe centrada en la conservación del rinoceronte. La entrada real sustituye el pin urbano anterior.",
        "Ofrece una escala de fauna manejable entre Makgadikgadi y el sureste.",
        "Circuitos de conducción y rinocerontes posibles sin garantía de encuentro.",
        "El pin coincide con la entrada de Khama Rhino Sanctuary. Reservar alojamiento y confirmar reglas del vehículo.",
        "Una o dos noches, con circuitos a primera o última hora.",
        "No entrar con mascota ni abandonar las rutas permitidas."),
    20: entry(
        "Pont Drift es el paso del Limpopo que da acceso al Northern Tuli. El cruce puede ser vado o transporte alternativo según el nivel del río.",
        "Permite enlazar un paisaje rocoso e histórico con la frontera sudafricana.",
        "Río Limpopo, paisaje del Tuli y restos históricos; las reservas privadas exigen reserva.",
        "El pin coincide con Pont Drift Border Post. Confirmar apertura, modalidad de cruce y admisión del vehículo.",
        "De día y con margen suficiente para ambos puestos.",
        "No intentar vadear con caudal ni asumir que este paso admite todo vehículo o mascota."),
    21: entry(
        "Monumento de Gaborone dedicado a Khama III, Sebele I y Bathoen I, los tres dikgosi que viajaron a Gran Bretaña en 1895.",
        "Resume un episodio decisivo de la formación territorial del país en una visita urbana breve.",
        "Tres figuras de bronce y paneles; el distrito gubernamental aporta contexto contemporáneo.",
        "El pin coincide con Three Dikgosi Monument. Llegar de día y estacionar en zona formal.",
        "Una hora, combinada con gestiones en Gaborone.",
        "No convertirlo en sustituto de Tsodilo o D’Kar; es una lectura política distinta."),
}, "sudafrica": {
    1: entry(
        "Museo de Johannesburgo que recorre la institucionalización, resistencia y fin del apartheid. Requiere tiempo y puede resultar emocionalmente intenso.",
        "Es la introducción histórica más completa para comprender la Sudáfrica contemporánea.",
        "Exposición permanente, testimonios y muestras temporales; no es una visita ligera.",
        "El pin coincide con Apartheid Museum. Confirmar apertura, entrada y aparcamiento vigilado.",
        "Mínimo medio día, preferiblemente por la mañana.",
        "No encajarlo entre dos desplazamientos largos ni contar con acceso del perro."),
    2: entry(
        "La casa de Vilakazi Street donde vivió Nelson Mandela es hoy un museo pequeño dentro de un barrio vivo, no una síntesis completa de Soweto.",
        "Aporta una escala humana a la historia política explicada en el Apartheid Museum.",
        "Casa, objetos y paneles; Hector Pieterson Memorial es otra visita cercana.",
        "El pin coincide con Mandela House. Usar guía u operador fiable y estacionamiento acordado.",
        "De día, evitando prisas y grandes concentraciones.",
        "No dejar objetos visibles ni convertir el barrio en decorado fotográfico."),
    3: entry(
        "Maropeng es el centro de visitantes de la Cuna de la Humanidad y explica la evolución humana; las cuevas de Sterkfontein son un sitio separado.",
        "Organiza un patrimonio paleontológico complejo antes de decidir otras visitas de campo.",
        "Exposiciones y Tumulus; comprobar por separado qué cuevas y excavaciones admiten visita.",
        "El pin coincide con Maropeng Visitor Centre. Reservar franja y revisar avisos oficiales.",
        "Media jornada, preferiblemente entre semana.",
        "No asumir que la entrada incluye Sterkfontein ni ignorar cierres técnicos de cuevas."),
    4: entry(
        "Mirador de Three Rondavels sobre el Blyde River Canyon y el embalse. El pin se ha movido desde un punto genérico a la plataforma real.",
        "Ofrece la panorámica más clara del cañón en una parada corta de carretera.",
        "Tres torres rocosas, cañón y embalse; God’s Window es otro mirador.",
        "El pin coincide con Three Rondavels View Point. Aparcar en el recinto y permanecer en barreras.",
        "Primera hora, antes de nubes y autocares.",
        "Omitirlo con niebla cerrada, tormenta o cierre del acceso."),
    5: entry(
        "Phabeni Gate es una puerta occidental de Kruger próxima a Hazyview. La ficha se ancla en la barrera real, no en el centro del parque.",
        "Es una entrada práctica para recorrer el sur de Kruger con reservas cerradas.",
        "Rutas de safari y fauna posible; ningún animal ni recorrido está garantizado.",
        "El pin coincide con Phabeni Gate. Reservar parque y campamento, respetar cupo y horario.",
        "Varios días, entrando a la apertura.",
        "No entrar con mascota ni llegar después del cierre de puertas."),
    6: entry(
        "Bhangazi Gate es el acceso físico a la sección oriental de iSimangaliso. Google Maps no ofrece un objeto nominal fiable: el pin documenta la barrera cartografiada.",
        "Permite acceder a humedales, bosque costero y playas de un paisaje Patrimonio Mundial.",
        "Lagos, dunas y costa según el sector abierto; Cape Vidal requiere continuar dentro del parque.",
        "Usar el pin como puerta física y contrastarlo con el mapa oficial de iSimangaliso antes de conducir.",
        "De día, con tiempo para regresar antes del cierre.",
        "No entrar con mascota ni confiar en rutas fuera del mapa oficial."),
    7: entry(
        "Memorial Gate es la puerta norte de Hluhluwe-iMfolozi, no un pin general sobre la reserva. Da acceso a circuitos de colinas y sabana.",
        "Es uno de los parques históricos de conservación de rinoceronte y una alternativa compacta a Kruger.",
        "Paisaje ondulado y fauna posible; ningún avistamiento está garantizado.",
        "El pin coincide con Memorial Gate. Confirmar horario, alojamiento y estado de carreteras.",
        "Una o dos noches, con recorridos tempranos y vespertinos.",
        "No entrar con mascota ni salir de vehículo fuera de zonas autorizadas."),
    8: entry(
        "KwaMuhle Museum ocupa una antigua oficina de administración nativa y explica segregación, trabajo y vida urbana en Durban.",
        "Aporta historia local concreta más allá del frente marítimo.",
        "Edificio histórico y exposiciones sobre la ciudad; el programa puede cambiar.",
        "El pin coincide con KwaMuhle Museum. Confirmar apertura y estacionamiento seguro.",
        "En horario diurno, combinado con una escala urbana.",
        "No ir sin comprobar apertura ni contar con acceso del perro al interior."),
    9: entry(
        "Sentinel Car Park es el inicio habitual de la exigente ruta al Amphitheatre por las Chain Ladders. El pin marca el aparcamiento, no la cima.",
        "Da acceso a una de las grandes caminatas panorámicas del Drakensberg.",
        "Pared del Amphitheatre, altiplano y escaleras metálicas; la cascada depende del agua.",
        "Confirmar pista, permiso, registro, tiempo y seguridad; llevar navegación y equipo de montaña.",
        "Salida muy temprana con jornada estable.",
        "No subir con tormenta, viento fuerte, vértigo incapacitante o tiempo insuficiente."),
    10: entry(
        "Glen Reenen es el campamento y base real de Golden Gate Highlands, entre paredones de arenisca. Sustituye un pin paisajístico impreciso.",
        "Es una escala de montaña accesible que combina carretera escénica y senderos cortos.",
        "Formaciones doradas, pastizales y rutas señalizadas; Basotho Cultural Village queda aparte.",
        "El pin coincide con Glen Reenen Rest Camp. Confirmar camping y senderos con SANParks.",
        "Una noche o dos, con luz de tarde sobre la arenisca.",
        "No caminar con tormenta eléctrica ni asumir que el perro entra en el parque."),
    11: entry(
        "Sani Pass es una pista de alta montaña y frontera con Lesoto. El pin marca el paso, no el control sudafricano ni un permiso de cruce.",
        "Es una ruta espectacular, pero su valor depende de seguridad, meteorología y legalidad del cruce.",
        "Zigzags, valle y escarpa; el pub en Lesoto implica haber completado frontera.",
        "Confirmar requisitos de 4x4, puestos, horarios y estado de pista antes de salir.",
        "Día seco y despejado, con margen amplio.",
        "No subir con nieve, hielo, lluvia fuerte, cierre fronterizo o frenos dudosos."),
    12: entry(
        "Arco natural separado de la costa cerca del poblado Hole-in-the-Wall. La aproximación por la Wild Coast requiere tiempo y criterio local.",
        "Es uno de los paisajes costeros más singulares de Sudáfrica y conserva significado xhosa.",
        "Arco, acantilados y playa; el estado del mar condiciona por completo la visita.",
        "El pin coincide con Hole in the Wall. Llegar de día, pactar guía y aparcamiento y evitar conducir por playa.",
        "Marea y luz favorables, con una noche en la zona.",
        "No vadear, nadar con mar fuerte ni seguir atajos propuestos sin verificación."),
    13: entry(
        "Storms River Mouth Rest Camp es la base costera de Tsitsikamma y el acceso a pasarelas y al inicio del Otter Trail.",
        "Combina bosque, costa rocosa y estuario en un recinto bien definido.",
        "Puentes colgantes, desembocadura y senderos; el Otter Trail requiere permiso independiente.",
        "El pin coincide con el rest camp. Reservar entrada y alojamiento con SANParks.",
        "Una noche o dos; mañana para senderos y tarde para costa.",
        "No confundir una visita corta con acceso al Otter Trail ni entrar con mascota."),
    14: entry(
        "Complejo de cuevas calizas cerca de Oudtshoorn con recorridos oficiales de distinta dificultad. La ruta Adventure exige movilidad real.",
        "Es la gran visita geológica del Karoo meridional y funciona incluso con mal tiempo exterior.",
        "Grandes salas y espeleotemas; no se garantiza fotografía libre en todos los sectores.",
        "El pin coincide con Cango Caves. Reservar el tour adecuado y llegar antes de la hora.",
        "Por la mañana o en horas de menor afluencia.",
        "No elegir Adventure Tour con claustrofobia, movilidad limitada o sin cumplir requisitos."),
    15: entry(
        "El monumento del extremo austral marca la latitud donde se encuentran convencionalmente Atlántico e Índico. No es el punto más meridional de todo el continente por cada roca aislada.",
        "Cierra un hito geográfico claro y un tramo de costa agreste.",
        "Monumento, costa rocosa y faro cercano; el naufragio de Meisho Maru queda aparte.",
        "El pin coincide con Southernmost Tip of Africa. Usar pasarela y aparcamiento oficial.",
        "Amanecer o tarde con viento manejable.",
        "No acercarse a roca mojada con oleaje fuerte ni volar dron sin autorización."),
    16: entry(
        "Old Harbour Museum conserva el antiguo puerto pesquero de Hermanus, sus cobertizos y embarcaciones. El avistamiento de ballenas es estacional y nunca seguro.",
        "Añade historia marítima a una parada habitualmente reducida a los miradores costeros.",
        "Puerto histórico y acantilados; ballenas solo si coinciden estación y fortuna.",
        "El pin coincide con Old Harbour Museum. Confirmar apertura y aparcar en zona formal.",
        "De día; combinar con Cliff Path si el viento lo permite.",
        "No prometer avistamientos ni acercarse a bordes con temporal."),
    17: entry(
        "La estación inferior del teleférico es el punto operativo para subir a Table Mountain. La montaña puede cerrar por viento incluso con cielo despejado.",
        "Facilita la gran panorámica de Ciudad del Cabo sin convertirla en una ascensión técnica.",
        "Cabina giratoria, meseta y vistas; subir a pie requiere otra preparación.",
        "El pin coincide con Lower Cableway Station. Comprar billete oficial y comprobar estado el mismo día.",
        "Primera franja despejada; mantener plan alternativo flexible.",
        "No subir ni bajar a pie sin ruta, agua, abrigo y previsión; no contar con acceso del perro."),
    18: entry(
        "El cartel de Cape of Good Hope se encuentra en la costa del parque de Table Mountain. Cape Point y su faro son otra parada del mismo sector.",
        "Es un hito paisajístico clásico dentro de una península de gran biodiversidad.",
        "Costa, acantilados y fauna posible; no alimentar babuinos ni acercarse a avestruces.",
        "El pin coincide con Cape of Good Hope. Entrar por puerta oficial y respetar la hora de salida.",
        "Temprano, antes de autocares y viento fuerte.",
        "No entrar con mascota ni confundirlo con el punto más austral, que es Agulhas."),
    19: entry(
        "Nelson Mandela Gateway en el V&A Waterfront es el punto de salida de los ferris oficiales a Robben Island, no la isla ni la prisión.",
        "La visita enlaza memoria del apartheid, encarcelamiento político y relatos de antiguos presos.",
        "Ferri, recorrido en bus y prisión; el itinerario depende del operador y del mar.",
        "El pin coincide con Nelson Mandela Gateway. Reservar solo en el canal oficial y llegar con antelación.",
        "Primera salida con mar razonable y varias horas libres.",
        "No comprar billetes informales ni dejar al perro en el coche durante la excursión."),
    20: entry(
        "Village Museum reúne cuatro casas históricas amuebladas que explican distintos periodos de Stellenbosch. No representa por sí solo toda la historia de la región.",
        "Es una visita urbana compacta antes de recorrer el paisaje vitivinícola.",
        "Arquitectura doméstica, interiores y jardín; las bodegas son visitas comerciales separadas.",
        "El pin coincide con Stellenbosch Village Museum. Confirmar horario y estacionar fuera del núcleo más congestionado.",
        "Mañana entre semana.",
        "No contar con acceso del perro al interior ni conducir después de catas."),
    21: entry(
        "Algeria Campsite es una base de CapeNature en Cederberg. Google Maps la señala temporalmente cerrada: no debe presentarse como alojamiento disponible.",
        "Si reabre, da acceso directo a arenisca, río y senderos del Cederberg central.",
        "Camping y rutas de montaña; Maltese Cross y Wolfberg requieren permisos y accesos propios.",
        "El pin coincide con Algeria Campsite. Reservar solo si CapeNature confirma por escrito apertura y parcela.",
        "Primavera u otoño, evitando calor y crecidas.",
        "Descartarlo mientras siga cerrado o sin confirmación oficial; usar una base alternativa autorizada."),
    22: entry(
        "SALT es el gran telescopio óptico del observatorio de Sutherland. La visita pública se realiza mediante tours programados y no equivale a una sesión de observación científica.",
        "Hace visible la ciencia que aprovecha los cielos oscuros del Karoo.",
        "Cúpula, telescopio y conjunto de observatorios; cada tour tiene alcance distinto.",
        "El pin coincide con Southern African Large Telescope activo. Reservar con SAAO y seguir controles del recinto.",
        "Tour diurno; para astronomía nocturna reservar la actividad específica.",
        "No seguir el segundo resultado de Google marcado cerrado ni llegar sin reserva."),
    23: entry(
        "Twee Rivieren es la puerta y campamento principal del Kgalagadi, junto a la frontera con Botsuana. No es un pin genérico sobre las dunas.",
        "Es la base más sencilla para explorar los cauces secos y paisajes rojos del parque.",
        "Lechos de los ríos, dunas y fauna posible sin garantía.",
        "El pin coincide con Twee Rivieren Rest Camp. Reservar y aclarar si se cruzará la frontera.",
        "Mínimo dos noches, con salidas tempranas.",
        "No entrar con mascota, sin combustible o fuera del horario de puerta."),
    24: entry(
        "El mirador de Augrabies Falls muestra al Orange River encajonado en granito. Caudal, ruido y aspecto cambian mucho con la estación.",
        "Es una parada geológica potente en el corredor del Northern Cape.",
        "Cascada, pasarelas y garganta; no se debe acceder a roca fuera del recorrido.",
        "El pin coincide con Augrabies Falls. Entrar por SANParks y seguir pasarelas habilitadas.",
        "Primera hora o tarde; llevar protección solar.",
        "No acercarse a bordes ni entrar con mascota."),
    25: entry(
        "Skilpad Rest Camp es la base del sector de flores de Namaqua. La floración depende de lluvia, temperatura, sol y viento: no tiene fecha garantizada.",
        "En buenas condiciones ofrece una de las transformaciones estacionales más memorables de la ruta.",
        "Campos de flores y granito; fuera de temporada sigue siendo paisaje semiárido.",
        "El pin coincide con Skilpad Rest Camp. Consultar avisos de floración, reserva y carretera con SANParks.",
        "En temporada comunicada oficialmente y con sol suficiente.",
        "No hacer el largo desvío basándose en calendarios antiguos ni entrar con mascota."),
    26: entry(
        "Sendelingsdrift es la recepción y acceso del Richtersveld junto al Orange. El transbordador internacional a Namibia puede no operar.",
        "Abre un desierto montañoso remoto con flora suculenta extraordinaria.",
        "Montañas, valles secos y plantas adaptadas; los campamentos interiores carecen de servicios amplios.",
        "El pin coincide con Sendelingsdrift. Confirmar parque, ferry, combustible, agua, pistas y reserva.",
        "Varios días fuera del calor extremo y llegando con luz.",
        "No entrar sin 4x4, autonomía, comunicaciones o confirmación reciente de accesos."),
}}


PHOTOS = {
    "zimbabue": {
        1: [commons("Mutare Area, Zimbabwe.jpg", "Seabifar · CC BY-SA 3.0", "Christmas Pass sobre Mutare; esta es la carretera y el paisaje del PDI.")],
        2: [
            commons("Yellow-bellied waxbill, Estrilda quartinia, Vumba National Botanical Garden, Zimbabwe (21655564689).jpg", "Derek Keats · CC BY 2.0", "Ave fotografiada dentro de Vumba Botanical Garden; ilustra su valor ornitológico."),
            commons("Yellow-bellied waxbill, Estrilda quartinia, Vumba National Botanical Garden, Zimbabwe (21654395060).jpg", "Derek Keats · CC BY 2.0", "Vegetación y avifauna del propio Vumba Botanical Garden."),
        ],
        3: [
            commons("Nyangani from nyamuziwa source.jpg", "Babakathy · dominio público", "Mount Nyangani visto desde la meseta."),
            commons("Nyangani south end.jpg", "Babakathy · dominio público", "Extremo sur del macizo de Nyangani."),
            commons("Nyangani.jpg", "Babakathy · CC BY-SA 3.0", "Relieve de Mount Nyangani, cuya cumbre marca el pin."),
        ],
        4: [
            commons("Mutarazi Falls00.jpg", "Bart Wursten · CC BY-SA 3.0", "Mtarazi Falls y la pared de su garganta."),
            commons("Mtarazi falls.jpg", "Seabifar · CC BY-SA 4.0", "Vista de Mtarazi Falls desde el sector del mirador."),
        ],
        5: [
            commons("Ziwa ruins pitentrance.JPG", "Damien Farrell · CC BY-SA 3.0", "Entrada de una estructura excavada en las ruinas de Ziwa."),
            commons("Ziwa ruins wall.JPG", "Damien Farrell · CC BY-SA 3.0", "Muro de piedra seca del sitio arqueológico de Ziwa."),
            commons("Ziwa enclosure trees.JPG", "Damien Farrell · CC BY-SA 3.0", "Recinto y arbolado de Ziwa Site Museum."),
        ],
        6: [commons("Eastern Highlands banner Chimanimani mountains.png", "Ton Rulkens · CC BY-SA 2.0", "Montañas de Chimanimani; la ficha se ancla en la oficina del parque, no en una cumbre.")],
        7: [
            commons("Groß Simbabwe, Konischer Turm.JPG", "Graph Geo · CC BY-SA 4.0", "Torre cónica dentro del Gran Recinto de Great Zimbabwe."),
            commons("Great-zim-aerial-looking-West.JPG", "Janice Bell · CC BY-SA 4.0", "Vista aérea del conjunto arqueológico de Great Zimbabwe."),
            commons("Gr Zimb Shona Dorf.jpg", "Thomas Wozniak · CC BY 3.0", "Arquitectura interpretativa junto al monumento; no es una ruina original."),
        ],
        8: [commons("Lake Kyle00.jpg", "Arthur Murray Harmsworth · CC BY-SA 3.0", "Lake Mutirikwi, llamado Lake Kyle en el archivo histórico.")],
        9: [commons("Zimbabwe Gonarezhou Landscape Chilojo Cliffs.jpg", "Ralf Ellerich · CC BY-SA 3.0", "Los acantilados de Chilojo; esta es la formación exacta del PDI.")],
        10: [
            commons("Natural History Museum Zimbabwe Bulawayo.jpg", "Sputniktilt · CC BY-SA 4.0", "Fachada del Natural History Museum of Zimbabwe en Bulawayo."),
            commons("Lobengula Bulawayo Museum.jpg", "Fritz Joubert · CC BY-SA 4.0", "Figura de Lobengula expuesta en el museo."),
            commons("BSAC Flag Bulawayo Museum.jpg", "Mangwanani · CC BY-SA 4.0", "Objeto histórico de la colección del museo."),
        ],
        11: [
            commons("Sunrise Matobo Zimbabwe.jpg", "Macvivo · CC BY-SA 3.0", "Kopjes de Matobo al amanecer; World’s View ocupa una de estas cumbres."),
            commons("Motherandchild Matobo.jpg", "Dominio público", "Formaciones graníticas de Matobo Hills."),
            commons("Pomongwe cave.jpg", "Sindiept · CC BY-SA 4.0", "Abrigo de Pomongwe, otra visita de Matobo; no es World’s View."),
        ],
        12: [
            commons("Khami ruins (ZW).jpg", "Ulamm · dominio público", "Plataformas y muros de Khami."),
            commons("ZW Khami Ruins.JPG", "Digr · CC BY-SA 4.0", "Detalle del sitio arqueológico de Khami."),
            commons("Khami Ruins, so-called Monolith Platform.jpg", "Robert Stewart Burrett · CC BY-SA 4.0", "Plataforma llamada Monolith Platform en Khami."),
        ],
        13: [
            commons("Hwange National Park, Zimbabwe (48595118982).jpg", "Fabio Achilli · CC BY 2.0", "Paisaje y fauna fotografiados dentro de Hwange; el avistamiento no se garantiza."),
            commons("Hwange National Park, Zimbabwe (48595102272).jpg", "Fabio Achilli · CC BY 2.0", "Poza y sabana de Hwange National Park."),
            commons("Hwange National Park, Zimbabwe (48594967867).jpg", "Fabio Achilli · CC BY 2.0", "Fauna de Hwange; la portada no promete repetir este encuentro."),
        ],
        14: [
            commons("Victoria Falls, Zimbabwe 01.jpg", "Bernard Gagnon · CC BY-SA 4.0", "Victoria Falls desde el recorrido del lado zimbabuense."),
            commons("Cataratas Victoria, Zambia-Zimbabue, 2018-07-27, DD 29.jpg", "Diego Delso · CC BY-SA 4.0", "Cortina de agua y garganta de Victoria Falls."),
            commons("Zimbabwe, Victoria Falls - panoramio.jpg", "Frans-Banja Mulder · CC BY 3.0", "Vista panorámica de Victoria Falls."),
        ],
        15: [
            commons("Puente de las cataratas Victoria, Zambia-Zimbabue, 2018-07-27, DD 10.jpg", "Diego Delso · CC BY-SA 4.0", "Victoria Falls Bridge sobre la garganta del Batoka."),
            commons("Victoria Falls Bridge, Africa 092.jpg", "Adam Annfield · CC BY 2.0", "Arco metálico del puente fronterizo."),
            commons("Cataratas Victoria, Zambia-Zimbabue, 2018-07-27, DD 16-20 PAN.jpg", "Diego Delso · CC BY-SA 4.0", "El puente dentro del paisaje de cataratas y gargantas."),
        ],
        16: [
            commons("Facocero común (Phacochoerus africanus), parque nacional de Zambeze, Zimbabue, 2018-07-28, DD 01.jpg", "Diego Delso · CC BY-SA 4.0", "Facócero fotografiado en Zambezi National Park; no garantiza avistamiento."),
        ],
        17: [
            commons("National Gallery Zimbabwe.jpg", "Awinda · CC BY-SA 3.0", "Edificio de la National Gallery of Zimbabwe en Harare."),
            commons("Zimbabwe Art Gallery Harare.jpg", "Tips for Travellers · CC BY 2.0", "Acceso y fachada de la galería nacional."),
        ],
        18: [
            commons("Domboshava rock.jpg", "Jwild · CC BY-SA 3.0", "Gran afloramiento granítico de Domboshawa."),
            commons("Domboshawa cave.jpg", "Fanny Schertzer · CC BY 3.0", "Abrigo rocoso de Domboshawa."),
            commons("Domboshawa rock paintings (4).jpg", "Fanny Schertzer · CC BY 3.0", "Pinturas rupestres del propio Domboshawa."),
        ],
        19: [
            commons("Chinhoyi caves, Zimbabwe.JPG", "Suesen · CC BY-SA 3.0", "Entrada de Chinhoyi Caves."),
            commons("Sleeping Pool, Chinhoyi Caves, Zimbabwe.JPG", "Suesen · CC BY-SA 3.0", "El agua azul del Sleeping Pool."),
            commons("Chinhoyi Caves Administration office, Zimbabwe.JPG", "Suesen · CC BY-SA 3.0", "Oficina de acceso al parque de Chinhoyi Caves."),
        ],
        20: [
            commons("Island in the Zambezi River at Mana Pools National Park-1.jpg", "Babakathy · CC0", "Zambeze frente a las llanuras de Mana Pools."),
            commons("ManaPoolsAug2003.jpg", "Radozw · CC BY-SA 3.0", "Llanura aluvial de Mana Pools en estación seca."),
            commons("Rukomechisand.JPG", "Babakathy · CC0", "Arena y ribera de Mana Pools; Nyamepi es la base de la ficha."),
        ],
        21: [
            commons("Kariba, Zimbabwe 11.JPG", "Suesen · CC BY-SA 3.0", "Muro y entorno de Kariba Dam."),
            commons("Kariba, Zimbabwe 10.JPG", "Suesen · CC BY-SA 3.0", "Infraestructura de la presa de Kariba."),
            commons("Kariba Dam Wall.jpg", "JonGT · CC BY-SA 4.0", "Vista del muro de Kariba Dam."),
        ],
        22: [commons("Chizarira National Park, Zimbabwe.jpg", "Dissoxciate · CC BY-SA 4.0", "Escarpa y paisaje de Chizarira National Park.")],
    },
    "botsuana": {
        1: [
            commons("Kazungula Bridge.jpg", "Gribeco · CC BY-SA 4.0", "Kazungula Bridge terminado sobre el Zambeze."),
            commons("The new bridge at Kazangula.jpg", "JonGT · CC BY-SA 4.0", "Vista lateral del puente internacional de Kazungula."),
            commons("The future connection.jpg", "Tracy Anne Brooks · CC BY-SA 4.0", "El puente durante su construcción; documenta la obra, no su estado actual."),
        ],
        2: [
            commons("Chobe Riverfront, Botswana (2611398068).jpg", "Joachim Huber · CC BY-SA 2.0", "Riverfront de Chobe desde el sector de Sedudu."),
            commons("Chobe Riverfront, Botswana (2633821123).jpg", "Joachim Huber · CC BY-SA 2.0", "Ribera y fauna de Chobe; el encuentro no se garantiza."),
            commons("Chobe Riverfront, Botswana (2634631410).jpg", "Joachim Huber · CC BY-SA 2.0", "Paisaje fluvial dentro de Chobe National Park."),
        ],
        3: [
            commons("Lion-savuti-botswana-april-2025.jpg", "Richardk85 · CC0", "León fotografiado en Savuti en 2025; no garantiza un avistamiento."),
            commons("Savuti Channel - Botswana - panoramio.jpg", "Diego Cue · CC BY-SA 3.0", "Canal de Savuti dentro del sector del PDI."),
            commons("Baobab in Savuti - Botswana - panoramio.jpg", "Diego Cue · CC BY-SA 3.0", "Baobab en el paisaje de Savuti."),
        ],
        4: [
            commons("Namibia from Linyanti River.jpg", "Dicklyon · CC BY-SA 4.0", "Río Linyanti visto desde la orilla de Botsuana hacia Namibia."),
        ],
        5: [
            commons("Palm trees at Khwai, Botswana in summer 03.jpg", "Mothusi Sekhomba · CC BY-SA 4.0", "Palmeras y llanura del río Khwai."),
            commons("Palm trees at Khwai, Botswana in summer 06.jpg", "Mothusi Sekhomba · CC BY-SA 4.0", "Paisaje del sector Khwai junto a North Gate."),
            commons("Palm trees at Khwai, Botswana in summer 01.jpg", "Mothusi Sekhomba · CC BY-SA 4.0", "Vegetación del corredor de Khwai."),
        ],
        6: [commons("Okavangodelta Xakanaxa.jpg", "Hp.Baumeler · CC BY-SA 4.0", "Canales y vegetación de Xakanaxa, el lugar exacto de la ficha.")],
        7: [commons("Equus quagga in Moremi Game Reserve, Botswana, -12 Nov. 2011 a.jpg", "Diego Cue · CC BY-SA 3.0", "Fauna de Moremi como contexto; la foto no muestra el embarcadero de Mboma.")],
        8: [
            commons("Maun - Botswana - panoramio.jpg", "Pavel Špindler · CC BY 3.0", "Tejido urbano de Maun, donde se encuentra Nhabe Museum."),
        ],
        9: [
            commons("Mokoro In the Kavango Delta Botswana.jpg", "Ilka Nghinamupika · CC BY-SA 4.0", "Mokoro en los canales del delta; el punto de salida de la ficha es Boro 2."),
            commons("Botswana 2026 12.jpg", "Hp.Baumeler · CC BY-SA 4.0", "Mokoro y vegetación acuática del Okavango."),
            commons("Botswana 2026 13.jpg", "Hp.Baumeler · CC BY-SA 4.0", "Canal del delta visto desde una embarcación tradicional."),
        ],
        10: [
            commons("Shakawe (2019), Version A.jpg", "Hp.Baumeler · CC BY-SA 4.0", "Canal principal del Okavango en Shakawe."),
            commons("Shakawe (2019), Version B.jpg", "Hp.Baumeler · CC BY-SA 4.0", "Ribera de Shakawe en el Panhandle."),
            commons("Shakawe (2019), Version C.jpg", "Hp.Baumeler · CC BY-SA 4.0", "Paisaje fluvial del propio Shakawe."),
        ],
        11: [
            commons("Tsodilo Hills rock paintings4.jpg", "Joachim Huber · CC BY-SA 2.0", "Panel de arte rupestre de Tsodilo Hills."),
            commons("Animals Rock Art Tsodilo.jpg", "Oliver Vass · CC BY-SA 3.0", "Figuras animales pintadas en Tsodilo."),
            commons("Geometric Shapes Tsodilo.jpg", "Oliver Vass · CC BY-SA 3.0", "Motivos geométricos del conjunto rupestre de Tsodilo."),
        ],
        12: [commons("Niambia botswanaensis (10.3897-subtbiol.40.72499) Figure 4.jpg", "Monticelli, Cardoso et al. · CC BY 4.0", "Fotografías científicas tomadas en Gcwihaba Caves; muestran roca y cavidades reales.")],
        13: [
            {"img": "https://kuruart.com/wp-content/uploads/2023/10/32EE3397-7737-42AD-9598-729A8B951873.png", "source": "https://kuruart.com/about-us/", "credit": "Kuru Art Project · fuente oficial enlazada", "caption": "Obra y actividad de Kuru Art Project en D’Kar."},
            {"img": "https://stwetuproduction.blob.core.windows.net/azure-blob-resources-wetu-production/Resources/293841%2F2.jpeg", "source": "https://portfoliocollection.com/activities/botswana/hainaveld-and-ghanzi-farms/kuru-art-project-visit-to-kuru-art-studio-tour-and-craft-and-coffee-shops/", "credit": "Kuru Art Project / Portfolio Collection · fuente enlazada", "caption": "Mural del proyecto artístico de D’Kar; consultar la fuente antes de reutilizar."},
        ],
        14: [commons("Kalahari PICT0036.JPG", "Winfried Bruenken · CC BY-SA 2.5", "Paisaje del Kalahari Central como contexto; no identifica un campsite de Deception Valley.")],
        15: [
            commons("Baines Baobabs, Nxai Pan (48591925422).jpg", "Fabio Achilli · CC BY 2.0", "Conjunto de Baines Baobabs junto a Kudiakam Pan."),
            commons("Baines Baobabs, Nxai Pan (48591815006).jpg", "Fabio Achilli · CC BY 2.0", "Baobabs vistos desde el borde de la salina."),
            commons("Baines Baobabs, Nxai Pan (48591783816).jpg", "Fabio Achilli · CC BY 2.0", "Escala del afloramiento y sus baobabs."),
        ],
        16: [
            commons("Auto- und Personenfähre über den Boteti.jpg", "EinfachFrankfurt · CC BY-SA 4.0", "Transbordador del Boteti; confirmar si sigue siendo la modalidad operativa de cruce."),
            commons("Makgadikgadi Basin - Botswana - panoramio.jpg", "Diego Cue · CC BY-SA 3.0", "Paisaje de Makgadikgadi como contexto del sector Khumaga."),
        ],
        17: [
            commons("Boababs at Kubu.jpg", "Hein Waschefort · CC BY-SA 3.0", "Baobabs sobre la roca de Kubu Island."),
        ],
        18: [
            commons("Nata Bird Sanctuary, Botswana (2652921427).jpg", "Joachim Huber · CC BY-SA 2.0", "Orilla y aves en Nata Bird Sanctuary."),
            commons("Nata Bird Sanctuary, Botswana (2652907113).jpg", "Joachim Huber · CC BY-SA 2.0", "Paisaje de Sua Pan desde el santuario."),
        ],
        19: [
            commons("Rinoceronte blanco (Ceratotherium simum), Santuario de Rinocerontes Khama, Botsuana, 2018-08-02, DD 06.jpg", "Diego Delso · CC BY-SA 4.0", "Rinoceronte blanco fotografiado en Khama Rhino Sanctuary."),
            commons("Rinoceronte blanco (Ceratotherium simum), Santuario de Rinocerontes Khama, Botsuana, 2018-08-02, DD 10.jpg", "Diego Delso · CC BY-SA 4.0", "Otro encuentro dentro del santuario; no se garantiza repetirlo."),
        ],
        20: [
            commons("Lions Tuli Block Botswana.jpg", "Stefanie · CC BY 3.0", "Leones fotografiados en Tuli Block; el avistamiento no se garantiza."),
            commons("Fort Tuli foundations.jpg", "Todinirunganga · CC BY-SA 4.0", "Restos de Fort Tuli dentro del paisaje histórico de la zona."),
        ],
        21: [commons("Three Dikgosi Monument, Gaborone, Botswana.jpg", "CivArmy · CC BY 4.0", "Las tres figuras de bronce del Three Dikgosi Monument.")],
    },
    "sudafrica": {
        1: [
            commons("RSA GP Johannesburg Apartheidsmuseum1.jpg", "Mart Bouter · CC BY-SA 4.0", "Arquitectura exterior del Apartheid Museum."),
        ],
        2: [
            commons("Soweto, Mandela House (2).jpg", "Pierre Andre Leclercq · CC BY-SA 4.0", "Mandela House en Vilakazi Street."),
            commons("Soweto, Mandela House (3).jpg", "Pierre Andre Leclercq · CC BY-SA 4.0", "Fachada y calle frente a Mandela House."),
            commons("Mandela House 8115.jpg", "Richard Matthews · CC BY 2.0", "El número 8115 de Vilakazi Street, hoy casa-museo."),
        ],
        3: [
            commons("Maropeng visitor centre, Cradle of Humankind, South Africa.jpg", "Olga Ernst · CC BY-SA 4.0", "Tumulus de Maropeng, centro de visitantes de la Cuna de la Humanidad."),
            commons("Maropeng in June 2009.jpg", "Heather Elke · CC BY-SA 4.0", "Centro de visitantes de Maropeng."),
        ],
        4: [
            commons("The Three Rondavels, Blyde River Canyon.jpg", "Claidheamhmor · CC BY-SA 4.0", "Three Rondavels y Blyde River Canyon desde el mirador exacto."),
            commons("Three Rondavels, Blyde River Canyon Nature Reserve, Mpumalanga, South Africa.jpg", "Claudirene · CC BY-SA 3.0", "Las formaciones desde la reserva de Blyde River Canyon."),
            commons("Blyde River Canyon with 3 Rondavels panorama.jpeg", "Hansm · CC BY-SA 3.0", "Panorama desde Three Rondavels View Point."),
        ],
        5: [
            commons("Elephant side-view Kruger.jpg", "Felix Andrews · CC BY-SA 3.0", "Elefante fotografiado en Kruger; no garantiza avistamiento."),
        ],
        6: [
            commons("Greater St. Lucia Wetland Park,South Africa.jpg", "Christian Wörtz · CC BY-SA 2.5", "Humedal de iSimangaliso como contexto del acceso de Bhangazi."),
            commons("Hippopotamus amphibius subsp. capensis, iSimangaliso Wetland Park 02.jpg", "Ossewa · CC BY-SA 4.0", "Hipopótamo fotografiado cerca de Bhangazi; no garantiza avistamiento."),
            commons("Kudu, iSimangaliso Wetland Park.jpg", "Ossewa · CC BY-SA 4.0", "Kudú fotografiado en iSimangaliso; no garantiza avistamiento."),
        ],
        7: [commons("Hluhluwe-Rhinos-and-Lions.JPG", "Bjørn Christian Tørrissen · CC BY-SA 4.0", "Fauna fotografiada en Hluhluwe-iMfolozi; no garantiza un encuentro.")],
        8: [{"img": "https://durbanhistorymuseums.org.za/wp-content/uploads/2015/05/Museum-Thumbnail-Home-KwaMuhle1.jpg", "source": "https://durbanhistorymuseums.org.za/", "credit": "Durban Local History Museums · fuente oficial enlazada", "caption": "KwaMuhle Museum en Durban; consultar la fuente antes de reutilizar."}],
        9: [
            commons("Amphitheatre Drakensberg.jpg", "Bothar · dominio público", "Pared del Amphitheatre vista desde el valle."),
            commons("Drakensbergen Amphitheater 09.jpg", "Ad Meskens · CC BY-SA 4.0", "Escarpa y altiplano del Drakensberg."),
        ],
        10: [
            commons("Golden Gate Highlands National Park, South Africa (Unsplash).jpg", "Pawel Janiak · CC0", "Paredones dorados del parque cerca de Glen Reenen."),
            commons("Golden Gate Highlands National Park, South Africa - panoramio.jpg", "Pavel Špindler · CC BY 3.0", "Carretera y arenisca de Golden Gate Highlands."),
            commons("Golden Gate Highlands National Park, South Africa - panoramio (3).jpg", "Pavel Špindler · CC BY 3.0", "Paisaje al este de Glen Reenen."),
        ],
        11: [
            commons("Sani Pass heading into Lesotho.jpg", "Vaiz Ha · CC BY 2.0", "Zigzags superiores de Sani Pass hacia Lesoto."),
            commons("SANI - Southern approach to Sani Pass, South Africa, 2017.jpg", "Josep M. Gracia · CC BY-SA 4.0", "Aproximación sur al paso fronterizo."),
            commons("SANI - Final hairpin bends below Sani Pass, South Africa, 2017.jpg", "Josep M. Gracia · CC BY-SA 4.0", "Curvas finales de la pista de Sani Pass."),
        ],
        12: [
            commons("Hole in the Wall - South Africa (2418545120).jpg", "South African Tourism · CC BY 2.0", "El arco natural de Hole-in-the-Wall en la Wild Coast."),
            commons("Hole In The Wall.jpg", "Vincentvanoosten · CC0", "Hole-in-the-Wall y la desembocadura en Coffee Bay."),
            commons("Town of hole in the wall.jpg", "GrantsJ1 · CC BY-SA 4.0", "Costa y asentamiento junto al PDI exacto."),
        ],
        13: [
            commons("Storms river mouth rest camp (32517159604).jpg", "Theo Crazzolara · CC BY 2.0", "Costa en Storms River Mouth Rest Camp."),
            commons("Storms river mouth rest camp (33350355866).jpg", "Theo Crazzolara · CC BY 2.0", "El campamento y el litoral de Storms River Mouth."),
            commons("Most western view of the Storms River Mouth Rest Camp - panoramio.jpg", "Hendrik van den Berg · CC BY 3.0", "Vista occidental del propio rest camp."),
        ],
        14: [
            commons("Inside Cango Caves.jpg", "Satdeep Gill · CC BY-SA 4.0", "Sala y espeleotemas dentro de Cango Caves."),
        ],
        15: [
            commons("Cape Agulhas panorama.jpg", "Dewet · CC BY-SA 2.5", "Costa de Cabo Agulhas en el extremo austral."),
        ],
        16: [
            commons("Old Harbour, Hermanus, South Africa.jpg", "Andrew Hall · CC BY-SA 3.0", "Antiguo puerto pesquero del museo."),
        ],
        17: [
            commons("Table Mountain cableway base station.jpg", "Daniel Case · CC BY-SA 3.0", "Estación inferior, punto exacto marcado en el mapa."),
            commons("Table Mountain cableway from Signal Hill.jpg", "Mike Peel · CC BY-SA 4.0", "Teleférico y ladera vistos desde Signal Hill."),
            commons("Table Mountain cableway, upper station.jpg", "Ossewa · CC BY-SA 4.0", "Estación superior; es el destino, no el pin de acceso."),
        ],
        18: [
            commons("Cape Town (ZA), Cape Peninsula National Park, Cape of Good Hope -- 2024 -- 3276.jpg", "Dietmar Rabich · CC BY-SA 4.0", "Cartel y costa de Cape of Good Hope."),
            commons("Cabo de Buena Esperanza, Sudáfrica, 2018-07-23, DD 62.jpg", "Diego Delso · CC BY-SA 4.0", "Paisaje del sector de Cape of Good Hope."),
        ],
        19: [
            commons("Maximum Security Prison, Robben Island (02).jpg", "Moheen Reeyad · CC BY-SA 4.0", "Edificio del antiguo penal de Robben Island."),
            commons("B-Section courtyard, Maximum Security Prison, Robben Island (01).jpg", "Moheen Reeyad · CC BY-SA 4.0", "Patio de la sección B durante la visita oficial."),
            commons("B-Section, Maximum Security Prison, Robben Island (01).jpg", "Moheen Reeyad · CC BY-SA 4.0", "Sección B del penal; el embarque se hace en el Waterfront."),
        ],
        20: [
            commons("Stellenbosch Village Museum.JPG", "SmartRebeccaJoy · CC BY-SA 3.0", "Una de las casas del Stellenbosch Village Museum."),
        ],
        21: [
            commons("Cederberg, South Africa 2023 22.jpg", "Dconvertini · CC BY-SA 2.0", "Formaciones de arenisca del Cederberg."),
            commons("Cederberg, South Africa 2023 17.jpg", "Dconvertini · CC BY-SA 2.0", "Paisaje del Cederberg central."),
            commons("Cederberg, South Africa 2023 2.jpg", "Dconvertini · CC BY-SA 2.0", "Vegetación y roca de la reserva; confirmar la reapertura de Algeria."),
        ],
        22: [
            commons("Southern African Large Telescope.jpg", "Lengau · CC BY-SA 4.0", "Cúpula del Southern African Large Telescope activo."),
        ],
        23: [
            commons("Kgalagadi Transfrontier Park banner Red dunes.JPG", "Bougnat87 · CC BY-SA 3.0", "Dunas rojas del Kgalagadi; Twee Rivieren es la puerta de la ficha."),
        ],
        24: [
            commons("Augrabies Falls, March 2008.jpg", "Zaian · dominio público", "Caudal de Augrabies Falls en marzo de 2008; varía por estación."),
            commons("Augrabies Falls, Augrabies Falls National Park (8722361583).png", "South African Tourism · CC BY 2.0", "Cascada dentro del parque nacional."),
            commons("Augrabies Falls 2.JPG", "Octagon · CC BY 3.0", "Pasarelas del mirador de Augrabies Falls."),
        ],
        25: [
            commons("Namaqua banner.jpg", "Winfried Bruenken · CC BY 3.0", "Floración en el sector Skilpad; no garantiza iguales condiciones."),
            commons("Namaqua NP1.jpg", "Winfried Bruenken · CC BY 3.0", "Campos de flores del propio sector Skilpad."),
            commons("Namaqua NP3.jpg", "Winfried Bruenken · CC BY 3.0", "Paisaje estacional del parque cerca de Skilpad."),
        ],
        26: [
            commons("Richtersveld World Heritage Site, Mountain scene near Kuboes.JPG", "Andrew Hall · CC BY-SA 3.0", "Paisaje montañoso del Richtersveld."),
        ],
    },
}


HISTORY = {
    "zimbabue": {
        "historia_resumen": "La historia de Zimbabue no empieza con Rodesia: enlaza la ocupación antiquísima de Matobo, los estados shona de arquitectura en piedra y las redes comerciales del Índico con la conquista colonial, dos guerras de liberación y una independencia que abrió grandes expectativas en 1980. La represión de Gukurahundi, la concentración de poder, la reforma agraria violenta y las crisis monetarias posteriores también forman parte de esa trayectoria. Great Zimbabwe, Khami, Matobo y los museos del país permiten leerla sobre el terreno sin reducirla a una sola figura política.",
        "historia_secciones": [
            ["Matobo antes de los reinos", "Los abrigos de Matobo conservan una asociación humana con el paisaje de al menos 100.000 años y evidencias arqueológicas que se remontan mucho más atrás. UNESCO fecha las pinturas rupestres más antiguas en al menos 13.000 años y subraya que los santuarios y la religión Mwari siguen vivos. Por eso World’s View no debe leerse solo como la tumba de Cecil Rhodes: ocupa un paisaje sagrado que existía mucho antes de la colonización y continúa teniendo significado local."],
            ["Great Zimbabwe, Khami y el mundo del Índico", "Great Zimbabwe se levantó principalmente entre los siglos XI y XV y fue el centro de un estado shona conectado con rutas de oro, ganado y marfil hacia la costa del Índico. Su arquitectura de piedra seca y los Pájaros de Zimbabue desmienten las teorías coloniales que negaban autoría africana al conjunto. Tras el desplazamiento de su centro político, Khami floreció como capital de la dinastía Torwa entre aproximadamente 1450 y 1650; porcelanas y otros objetos importados documentan redes de larga distancia, no aislamiento."],
            ["Mutapa, Rozvi y el estado ndebele", "Los siglos siguientes estuvieron marcados por estados y redes de poder cambiantes, entre ellos Mutapa y Rozvi, que negociaron y combatieron con comerciantes y agentes portugueses. En la década de 1830, Mzilikazi y grupos ndebele procedentes del sur se asentaron en el suroeste y formaron un nuevo estado con capital cerca de la actual Bulawayo. La relación entre comunidades shona, ndebele y otros grupos no cabe en una sucesión lineal de «tribus»: hubo conflicto, incorporación, intercambio y territorios superpuestos."],
            ["Conquista de la BSAC y las Chimurenga", "La British South Africa Company de Cecil Rhodes obtuvo concesiones disputadas y ocupó Mashonaland en 1890. La guerra de 1893 destruyó el reino ndebele y los levantamientos shona y ndebele de 1896–97, recordados como la Primera Chimurenga, fueron derrotados. La colonia de Rodesia del Sur consolidó la apropiación de tierras, el trabajo coercitivo y una jerarquía racial. Las tumbas coloniales de Matobo y los museos de Bulawayo deben visitarse junto a esta historia, no como monumentos neutrales."],
            ["Rodesia, UDI y guerra de liberación", "En 1965 el gobierno de Ian Smith declaró unilateralmente la independencia para preservar el poder de la minoría blanca. Sanciones, lucha armada y represión siguieron durante catorce años, con ZANLA y ZIPRA vinculadas respectivamente a ZANU y ZAPU. Los acuerdos de Lancaster House de 1979 condujeron a elecciones y a la independencia reconocida el 18 de abril de 1980. La Segunda Chimurenga sigue presente en memoriales, relatos familiares y divisiones políticas."],
            ["Independencia, Gukurahundi y crisis posteriores", "El primer gobierno de Robert Mugabe amplió educación y servicios, pero entre 1983 y 1987 fuerzas estatales cometieron asesinatos y abusos masivos en Matabeleland y Midlands durante Gukurahundi. La reforma agraria acelerada desde 2000 corrigió una desigualdad colonial real mediante un proceso violento y politizado que también desplomó producción y confianza. A ello siguieron hiperinflación, dolarización parcial y repetidos cambios monetarios. El relevo militar de Mugabe en 2017 no cerró esas tensiones; para el viaje, las divisas y medios de pago deben verificarse en el momento, sin fijar una cotización en esta historia."],
        ],
        "historia_fuentes": [
            ["UNESCO · Great Zimbabwe National Monument", "https://whc.unesco.org/en/list/364/"],
            ["UNESCO · Khami Ruins National Monument", "https://whc.unesco.org/en/list/365/"],
            ["UNESCO · Matobo Hills", "https://whc.unesco.org/en/list/306/"],
            ["NMMZ · National Museums and Monuments of Zimbabwe", "https://www.nmmz.co.zw/"],
            ["Encyclopaedia Britannica · Zimbabwe, History", "https://www.britannica.com/place/Zimbabwe/History"],
            ["Catholic Commission for Justice and Peace · Breaking the Silence (Gukurahundi)", "https://archive.org/details/BreakingTheSilenceBuildingTruePeace"],
        ],
    },
    "botsuana": {
        "historia_resumen": "Botsuana reúne historias san del Kalahari, estados tswana organizados alrededor del ganado y el agua, un protectorado británico periférico y una independencia obtenida en 1966 con muy poca infraestructura. La gestión pública de los diamantes financió una transformación excepcional, aunque no eliminó desigualdad, dependencia minera ni disputas por tierra y conservación. Tsodilo, D’Kar, Three Dikgosi y los parques cuentan capas distintas de esa historia y no deben fundirse en un relato simple de «estabilidad».",
        "historia_secciones": [
            ["Tsodilo y las sociedades san", "Comunidades cazadoras-recolectoras habitaron el Kalahari durante milenios antes de la expansión de pueblos de lengua bantú. Tsodilo conserva más de 4.500 pinturas en unos 400 lugares y mantiene un profundo valor espiritual para comunidades san y hambukushu. Las imágenes pertenecen a periodos y autores distintos; la visita guiada ayuda a evitar el error de tratar «lo san» como una cultura congelada en el pasado."],
            ["Estados tswana, ganado y kgotla", "Desde siglos anteriores al protectorado se consolidaron polidades tswana como Bangwato, Bakwena, Bangwaketse y Batawana. El ganado, el acceso al agua, las relaciones de tributo y la kgotla como espacio de deliberación estructuraron la vida política, aunque la participación nunca fue igual para todas las personas y comunidades. Moremi fue proclamada en 1963 por iniciativa batawana para proteger fauna y territorio, pero la historia de conservación también incluye desplazamientos y restricciones de uso que merecen preguntarse localmente."],
            ["Bechuanalandia y la misión de los tres dikgosi", "Gran Bretaña declaró el protectorado de Bechuanalandia en 1885. Diez años después, Khama III, Sebele I y Bathoen I viajaron a Gran Bretaña para oponerse a que sus territorios fueran entregados a la British South Africa Company. Lograron limitar esa transferencia, aunque la administración colonial conservó poder y la capital del protectorado quedó fuera del territorio, en Mafeking. Three Dikgosi Monument conmemora precisamente esa misión de 1895, no la creación inicial del protectorado."],
            ["Seretse Khama y la independencia", "Seretse Khama, heredero bangwato, fue apartado de su jefatura durante la controversia colonial provocada por su matrimonio interracial con Ruth Williams. Regresó a la política partidista, encabezó el gobierno previo a la independencia y el 30 de septiembre de 1966 se convirtió en el primer presidente de la República de Botsuana. El nuevo Estado partió con una red muy reducida de carreteras pavimentadas, escuelas y personal cualificado, y apostó por instituciones nacionales por encima de los viejos centros coloniales."],
            ["Diamantes, Debswana y transformación", "El descubrimiento de diamantes poco después de la independencia y la empresa conjunta Debswana dieron al Estado ingresos extraordinarios. Gobiernos sucesivos los destinaron a carreteras, educación, sanidad y reservas, produciendo décadas de crecimiento. Esa historia de éxito no elimina la dependencia de un solo recurso, el desempleo, la desigualdad ni el coste social de la epidemia de VIH; la respuesta pública al VIH fue a su vez una de las políticas sanitarias más importantes del país."],
            ["Democracia, alternancia y conservación", "Botsuana mantuvo elecciones multipartidistas regulares desde 1965, pero el Botswana Democratic Party gobernó de forma continua hasta 2024. Las elecciones de ese año produjeron la primera alternancia nacional, una transición pacífica que matiza la idea de estabilidad sin competencia. El modelo turístico de bajo volumen y alto valor protege territorios sensibles y encarece mucho el acceso; también convive con debates sobre derechos de comunidades san, caza, agua y beneficios locales."],
        ],
        "historia_fuentes": [
            ["UNESCO · Tsodilo", "https://whc.unesco.org/en/list/1021/"],
            ["UNESCO · Okavango Delta", "https://whc.unesco.org/en/list/1432/"],
            ["Parliament of Botswana · History", "https://parliament.gov.bw/index.php?Itemid=163&id=6&option=com_content&view=article"],
            ["Encyclopaedia Britannica · Botswana, History", "https://www.britannica.com/place/Botswana/History"],
            ["Kuru Art Project · historia y artistas", "https://kuruart.com/about-us/"],
            ["IEC Botswana · elecciones", "https://www.iec.gov.bw/"],
        ],
    },
    "sudafrica": {
        "historia_resumen": "Sudáfrica condensa una historia humana de enorme profundidad, sociedades khoisan, reinos africanos, esclavitud colonial, conquista, industrialización minera y segregación antes y durante el apartheid. La transición negociada de 1990–94 creó una democracia constitucional de referencia, pero no borró la geografía de desigualdad y violencia heredada. Maropeng, KwaMuhle, Soweto, Robben Island, el Apartheid Museum y paisajes como el Drakensberg permiten conectar esas etapas con lugares concretos.",
        "historia_secciones": [
            ["Profundidad humana, khoisan y primeras agriculturas", "Los yacimientos de la Cuna de la Humanidad conservan un registro excepcional de homínidos que abarca varios millones de años. Mucho más tarde, sociedades san cazadoras-recolectoras y comunidades khoikhoi ganaderas dejaron lenguas, rutas, conocimiento ecológico y arte rupestre que siguen vivos, pese a desposesión y violencia. Agricultores y metalúrgicos de lenguas bantú se establecieron en distintas regiones desde el primer milenio de nuestra era y desarrollaron sociedades muy diversas; Mapungubwe, cerca de Tuli, fue un importante estado comercial antes de Great Zimbabwe."],
            ["El Cabo: compañía, esclavitud y frontera", "La VOC estableció en 1652 un puesto de abastecimiento en Table Bay. La colonia creció mediante apropiación de tierra y trabajo esclavizado traído de África y Asia, además del sometimiento de comunidades khoikhoi y san. De esa sociedad surgieron identidades afrikáneres y comunidades coloured y malayas del Cabo, entre otras. Gran Bretaña tomó control definitivo a comienzos del siglo XIX; Stellenbosch y Ciudad del Cabo conservan arquitectura atractiva, pero sus museos deben explicar también quién construyó y sostuvo esas economías."],
            ["Reinos africanos, Gran Trek y conquista", "Durante el siglo XIX, reinos y polidades zulu, xhosa, sotho, tswana y ndebele defendieron y ampliaron territorios mientras colonos británicos y voortrekkers avanzaban desde el Cabo. El ascenso del reino zulu bajo Shaka formó parte de transformaciones regionales que el término Mfecane explica de manera discutida y a veces demasiado simple. El Gran Trek originó repúblicas bóeres, pero no atravesó un interior vacío: produjo alianzas, guerras, tratados y nuevas desposesiones."],
            ["Diamantes, oro y la Unión segregada", "Los diamantes de Kimberley y el oro del Witwatersrand convirtieron el sur africano en una economía industrial y de trabajo migrante. Tras la guerra sudafricana de 1899–1902, que incluyó campos de concentración británicos para civiles bóeres y africanos, la Unión Sudafricana nació en 1910 excluyendo a la mayoría negra del poder nacional. La Natives Land Act de 1913 y otras leyes anteriores a 1948 ya limitaron tierra, residencia y movilidad; el apartheid sistematizó una segregación que no empezó de cero."],
            ["Apartheid y resistencias", "Desde 1948 el National Party clasificó racialmente a la población, impuso pases, expulsiones y educación desigual, y convirtió los bantustanes en instrumentos para negar ciudadanía plena. La resistencia adoptó formas sindicales, comunitarias, culturales, armadas y de desobediencia. Sharpeville en 1960, el encarcelamiento de Mandela y otros dirigentes, el levantamiento de Soweto en 1976 y la movilización de los años ochenta no son episodios aislados: KwaMuhle, Vilakazi Street y Robben Island muestran mecanismos y respuestas diferentes."],
            ["Negociación, Constitución y memoria", "La liberación de Nelson Mandela en 1990 abrió una negociación marcada también por violencia política. Las elecciones del 27 de abril de 1994 dieron lugar al primer gobierno elegido por sufragio universal; la Constitución de 1996 consolidó derechos amplios y un Tribunal Constitucional fuerte. La Comisión de Verdad y Reconciliación hizo públicos miles de testimonios, pero reconciliación, justicia y reparación siguen siendo debates abiertos, no una historia cerrada por Mandela."],
            ["Treinta años de democracia", "La democracia amplió vivienda, electricidad, protección social y acceso a servicios, mientras corrupción, desempleo, violencia y desigualdad persistieron y la crisis de Eskom afectó la vida cotidiana. En 2024 el ANC perdió por primera vez la mayoría parlamentaria nacional y se formó un gobierno de unidad con varios partidos. Ese cambio no borra diferencias enormes entre barrios y provincias: para el viajero, la infraestructura avanzada y los riesgos urbanos coexisten, y ambos deben describirse sin estereotipos."],
        ],
        "historia_fuentes": [
            ["UNESCO · Fossil Hominid Sites of South Africa", "https://whc.unesco.org/en/list/915/"],
            ["South African History Online · historia y cronologías", "https://www.sahistory.org.za/"],
            ["Apartheid Museum · exposiciones", "https://www.apartheidmuseum.org/"],
            ["Constitutional Court of South Africa · Constitution", "https://www.concourt.org.za/index.php/constitution"],
            ["Robben Island Museum · patrimonio y visitas", "https://www.robben-island.org.za/"],
            ["Electoral Commission of South Africa · 2024 election report", "https://www.elections.org.za/content/Documents/Election-reports/National-and-Provincial-Elections/2024-National-and-Provincial-Elections-Report/"],
        ],
    },
}


HISTORY_NOTES = {
    "zimbabue": [
        "Se separan el paisaje sagrado y la ocupación antigua de Matobo del monumento colonial de World’s View.",
        "La cronología distingue la Primera Chimurenga, la guerra de liberación y la independencia reconocida de 1980.",
        "No se fija una cotización ni se presenta un medio de pago actual como permanente: debe comprobarse durante el viaje.",
    ],
    "botsuana": [
        "El protectorado se fecha en 1885; el viaje de los tres dikgosi a Gran Bretaña se fecha por separado en 1895.",
        "Moremi se explica como iniciativa batawana de 1963 sin ocultar los conflictos que también ha producido la conservación.",
        "La primera alternancia nacional se sitúa en las elecciones de 2024 y no se confunde con el inicio de las elecciones multipartidistas.",
    ],
    "sudafrica": [
        "La segregación territorial y laboral anterior a 1948 se distingue de su sistematización posterior bajo el apartheid.",
        "El término Mfecane se presenta como una interpretación discutida y no como explicación única de los cambios del siglo XIX.",
        "La transición de 1994 y la Constitución de 1996 no se presentan como cierre de las desigualdades ni de los debates sobre reparación.",
        "La referencia política más reciente es la pérdida de la mayoría parlamentaria del ANC y el gobierno de unidad formado tras las elecciones de 2024.",
    ],
}


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
            raise ValueError(f"{country}: {label} incompletos; faltan={sorted(expected-set(values))}; sobran={sorted(set(values)-expected)}")
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
    # La ficha heredada de Zimbabue conservaba dos filas de una auditoría
    # anterior que ya no son ciertas tras cerrar todas las fotos y coordenadas.
    # Se eliminan en la fuente reproducible para que no reaparezcan al regenerar.
    stale_labels = ("FOTOS PENDIENTES DE SUSTITUIR", "COORDENADAS APROXIMADAS")
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
    for country_name in ("zimbabue", "botsuana", "sudafrica"):
        apply_country(country_name)
        apply_history(country_name)

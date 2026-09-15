#!/usr/bin/env python3
"""Pasada retroactiva de PDIs del grupo 2.

La tarjeta conserva un resumen breve. El texto largo auditado previamente se
traslada al modal como contexto de «qué se ve», y se añaden decisión, acceso,
momento, descarte, enlace específico y tres fotografías inequívocas.
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


def google_photo(base: str, query: str, caption: str) -> dict[str, str]:
    return external(
        f"{base}=w1200-h675-k-no",
        "https://www.google.com/maps/search/?api=1&query=" + quote(query),
        "Google Maps · aportación de usuario; autor y condiciones en la ficha",
        caption,
    )


def entry(
    desc: str,
    why: str,
    access: str,
    when: str,
    skip: str,
    link_label: str,
    link_url: str,
    photos: list[dict[str, str]],
    *,
    name: str | None = None,
    coords: tuple[float, float] | None = None,
    see: str | None = None,
) -> dict:
    value = {
        "desc": desc,
        "visit": {
            "why": why,
            "see": see,
            "access": access,
            "when": when,
            "skip": skip,
        },
        "links": [{"label": link_label, "url": link_url}],
        "photos": photos,
    }
    if name is not None:
        value["name"] = name
    if coords is not None:
        value["lat"], value["lon"] = coords
    return value


DATA: dict[str, dict[int, dict]] = {
    "guinea": {
        3: entry(
            "La Dama de Mali es un perfil rocoso natural bajo la cumbre del monte Loura, en el extremo norte del Fouta Djallon. La visita exige guía local y una jornada de montaña.",
            "Es la formación geológica más reconocible del Fouta y una buena lectura del relieve del altiplano.",
            "El pin conserva la cumbre cartográfica contrastada con OSM; la ficha genérica «Monte Loura» de Google Maps aparece desplazada y no se usa. Contratar guía en Mali-ville y confirmar pista y punto de inicio.",
            "Estación seca, salida al amanecer y día completo con agua propia.",
            "Descartarlo con niebla, tormenta, pista mojada, guía no confirmado o poca autonomía; no prometer acceso del perro en pasos expuestos.",
            "Información del monte Loura",
            "https://fr.wikipedia.org/wiki/Mont_Loura",
            [
                commons("La Dame du Mali du Mont Loura.png", "Fatoumata D · CC BY-SA 4.0", "Perfil de la Dama de Mali en el monte Loura."),
                commons("Dame de Maali, Mount Loura.jpg", "Hcaudill · CC BY 2.5", "Formación rocosa vista desde otra vertiente del Loura."),
                commons("Dame de Mali 2022.jpg", "Aboubacarkhoraa · CC BY-SA 4.0", "Escala del farallón y la Dama de Mali en 2022."),
            ],
        ),
        4: entry(
            "Kinkon es una gran cascada del Kokoulo junto a Pita, aguas abajo de una presa. El acceso final requiere comprobar localmente la pista y mantenerse lejos del borde.",
            "Permite ver una de las caídas más potentes del Fouta sin convertir Pita en una simple escala logística.",
            "El pin se ha ajustado a la ficha exacta Chutes de Kinkon de Google Maps. Llegar con guía local, aparcar antes del firme dudoso y acercarse solo por senderos pisados.",
            "Tras las lluvias ofrece más caudal, pero solo con firme estable; mañana o tarde sin tormenta.",
            "Omitir con crecida, barro, lluvia activa o si nadie local confirma el acceso seguro; no bañarse bajo la descarga.",
            "Ficha de Chutes de Kinkon en Google Maps",
            "https://www.google.com/maps/search/?api=1&query=Chutes%20de%20Kinkon%20Guinea",
            [
                commons("Chute de Kinkon.jpg", "Sayd224 · CC BY 4.0", "Caída principal de Kinkon en la Guinea Media."),
                commons("Chute d'eau de kinkon.jpg", "Sayd224 · CC BY 4.0", "Otra vista de la cascada de Kinkon."),
                commons("Chute de kinkon.jpg", "Saidriame081 · CC BY-SA 4.0", "Cortina de agua y pared rocosa del salto."),
            ],
            coords=(11.0558088, -12.454538),
        ),
        5: entry(
            "Kambadaga encadena varios saltos del Kokoulo dentro de un cañón verde cerca de Pita. El atractivo real es el conjunto de cascadas y miradores, no una poza garantizada para bañarse.",
            "Es el sistema de cascadas más variado del bloque de Pita y justifica medio día con guía.",
            "El pin coincide con el nodo cartográfico de la cascada; Google Maps no ofrece una ficha inequívoca. Confirmar la pista en Pita, entrar acompañado y no cruzar el puente de lianas sin permiso y revisión local.",
            "Final de lluvias o comienzo de la seca, con luz de mañana y terreno asentado.",
            "Descartarlo con barro profundo, tormenta, caudal violento o guía improvisado; evitar bordes y roca mojada.",
            "Información local de Pita y Kambadaga",
            "https://fr.wikipedia.org/wiki/Pita_(Guin%C3%A9e)",
            [
                commons("Wasserfälle Kambadaga 256.jpg", "Flucco · CC BY-SA 4.0", "Vista amplia de los saltos escalonados de Kambadaga."),
                commons("Kambadaga Pita.jpg", "M Saidou · CC BY-SA 4.0", "Uno de los niveles de la cascada cerca de Pita."),
                commons("Chutte de kambadaga.jpg", "M Saidou · CC BY-SA 4.0", "Agua y vegetación del cañón de Kambadaga."),
            ],
        ),
        8: entry(
            "Ditinn cae en un salto alto y estrecho desde la meseta del Fouta a una cubeta forestal. La excursión combina pista rural y descenso a pie con guía.",
            "La gran caída vertical y la vista del valle la hacen distinta de Kinkon y Kambadaga.",
            "El pin se ajusta a la ficha exacta Chutes de Ditinn de Google Maps. Acordar guía y vehículo en Dalaba o Ditinn y no asumir que el último tramo sea conducible.",
            "Con caudal visible y firme seguro, preferentemente por la mañana; reservar el día completo.",
            "Omitir con lluvia fuerte, barrancos resbaladizos, crecida o sin retorno pactado; no acampar en la zona inundable.",
            "Relato de acceso a la chute de Ditinn",
            "https://www.foutadecouverte.com/2018/09/au-fouta-djalon-la-chute-de-ditinn-relie-terre-et-ciel.html",
            [
                commons("Chute de Ditinn à Dalaba.jpg", "Maarten van der Bent · CC BY-SA 2.0", "Caída completa de Ditinn dentro del circo rocoso."),
                external("https://img.over-blog-kiwi.com/0/95/90/05/20180903/ob_413152_p1080586.JPG", "https://www.foutadecouverte.com/2018/09/au-fouta-djalon-la-chute-de-ditinn-relie-terre-et-ciel.html", "Fouta Découverte · derechos en la fuente", "Vista frontal documentada de la chute de Ditinn."),
                external("https://img.over-blog-kiwi.com/0/95/90/05/20180903/ob_c44605_p1080856.JPG", "https://www.foutadecouverte.com/2018/09/au-fouta-djalon-la-chute-de-ditinn-relie-terre-et-ciel.html", "Fouta Découverte · derechos en la fuente", "Mirador superior y profundidad del salto de Ditinn."),
            ],
            coords=(10.8164008, -12.1859401),
        ),
        9: entry(
            "El Voile de la Mariée es una cascada de varios hilos en Bendougou, cerca de Kindia. Se visita como excursión corta y no representa toda la ciudad ni el monte Gangan.",
            "Es una parada accesible y visual entre el Fouta y Conakry, con un objeto claro que valorar.",
            "El pin se mueve desde el centro genérico de Kindia a la ficha exacta La voile de la mariée Kindia de Google Maps. Confirmar horario y estado del acceso al llegar.",
            "Temporada con agua, primera hora o final de tarde; una o dos horas.",
            "Omitir en estiaje extremo, con recinto cerrado o si el desvío obliga a conducir de noche.",
            "Ficha del Voile de la Mariée en Google Maps",
            "https://www.google.com/maps/search/?api=1&query=La%20voile%20de%20la%20mari%C3%A9e%20Kindia",
            [
                commons("Voile de la marié kindia séguéya.jpg", "M keita1321 · CC BY-SA 4.0", "Cascada y vegetación del Voile de la Mariée de Kindia."),
                commons("Voile de la marié kindia.jpg", "M keita1321 · CC BY-SA 4.0", "Hilos de agua sobre la pared rocosa del lugar."),
                commons("Voile de la Marié kindia.jpg", "M keita1321 · CC BY-SA 4.0", "Otra perspectiva del salto de Bendougou."),
            ],
            name="Voile de la Mariée de Kindia",
            coords=(9.9816544, -12.7938486),
        ),
        10: entry(
            "Conakry es la base nacional para documentación, salud, talleres y abastecimiento. La visita urbana se concentra en Kaloum y debe planificarse por tráfico y estacionamiento.",
            "Es el único nodo capaz de resolver gestiones complejas antes de continuar hacia Sierra Leona o el interior.",
            "El pin se ajusta a la ficha de ciudad de Google Maps porque el PDI describe una base urbana. Elegir alojamiento con aparcamiento vigilado y agrupar trámites por barrio.",
            "Días laborables para organismos y talleres; desplazamientos de día y fuera de horas punta.",
            "Reducir el turismo urbano si no hay estacionamiento seguro o si una gestión obliga a cruzar repetidamente la península.",
            "Información práctica de Conakry",
            "https://en.wikipedia.org/wiki/Conakry",
            [
                commons("Un aperçu de la ville de conakry.jpg", "Alpha hmd · CC BY-SA 4.0", "Vista urbana reconocible de Conakry."),
                commons("2013 Conakry Guinea 14418728438.jpg", "Maarten van der Bent · CC BY-SA 2.0", "Conakry vista desde el frente marítimo en 2013."),
                commons("Aéroport international de Conakry Gbessia vu de l'extérieur.jpg", "Fawaz.tairou · CC BY-SA 4.0", "Exterior del aeropuerto de Conakry-Gbessia como referencia logística."),
            ],
            coords=(9.5090945, -13.7119312),
        ),
        11: entry(
            "Las Îles de Los forman un archipiélago frente a Conakry con playas, roca y aldeas insulares. La experiencia depende por completo de una lancha y un regreso fiables.",
            "Ofrecen una pausa costera muy distinta de la capital sin una larga etapa por carretera.",
            "El pin se ajusta a la ficha Islas de Los de Google Maps y representa el archipiélago, no un muelle. Pactar isla, embarque, chalecos, precio y regreso antes de salir.",
            "Estación seca, mar tranquilo y salida temprana con margen de luz.",
            "Descartarlas con oleaje, tormenta, barco sin chalecos o retorno incierto; confirmar expresamente si aceptan perro.",
            "Información de las Îles de Los",
            "https://en.wikipedia.org/wiki/%C3%8Eles_de_Los",
            [
                external("https://3.bp.blogspot.com/-N8osfZFk0M0/Vim64JkqwBI/AAAAAAAAABg/ucUyDCw8vXs/s1600/GUIILESDELOS.jpg", "https://alookatmyguinea.blogspot.com/2015/10/things-to-do-and-to-see.html", "A Look at My Guinea · derechos en la fuente", "Cala rocosa y vegetación de las Îles de Los."),
                external("https://travel2unlimited.com/wp-content/uploads/2022/11/322242597_554706179852643_560747414307576947_n_10160702493543701-495x400.jpg", "https://travel2unlimited.com/guinea-kassa-island-le-bamana-beach/", "Travel2Unlimited · derechos en la fuente", "Arena, oleaje y rocas rojizas de Le Bamana Beach, en la isla Kassa."),
                external("https://travel2unlimited.com/wp-content/uploads/2022/11/322368240_458954896440368_332198352448384027_n_10160702495483701-495x400.jpg", "https://travel2unlimited.com/guinea-kassa-island-le-bamana-beach/", "Travel2Unlimited · derechos en la fuente", "Rocas rojizas y arena de Le Bamana Beach, isla Kassa."),
            ],
            coords=(9.4769, -13.7855),
        ),
        12: entry(
            "El antiguo fuerte de Boké alberga el museo regional junto al río Nunez. Es una visita histórica concreta dentro de una variante costera que debe decidirse aparte.",
            "Da contexto a la trata, el comercio fluvial y la ocupación colonial del norte de Guinea.",
            "El pin se corrige a la ficha exacta Musée de Boke de Google Maps. Confirmar apertura antes de desviar la ruta y no confundirlo con una visita genérica a Boffa.",
            "Día laborable y por la mañana; una o dos horas de visita.",
            "Omitir con museo cerrado o si la variante costera compromete la etapa principal.",
            "Ficha del Musée de Boké en Google Maps",
            "https://www.google.com/maps/search/?api=1&query=Mus%C3%A9e%20de%20Boke%20Guinea",
            [
                commons("Musée de Boké.jpg", "Aboubacarkhoraa · CC BY-SA 4.0", "Edificio del museo regional de Boké."),
                commons("Canon musée de Boké.jpg", "Aboubacarkhoraa · CC BY-SA 4.0", "Cañón histórico expuesto en el museo."),
                commons("Tableau du musée de Boké.jpg", "Aboubacarkhoraa · CC BY-SA 4.0", "Pieza interpretativa dentro del museo de Boké."),
            ],
            name="Museo regional de Boké",
            coords=(10.9333162, -14.2959859),
        ),
        14: entry(
            "Sérédou es la base navegable para el macizo forestal de Ziama, no el centro de la reserva. Cualquier entrada al bosque requiere autorización y guía local confirmados.",
            "Permite valorar uno de los principales remanentes de selva guineana sin fingir una puerta turística inexistente.",
            "El pin se ajusta a la ficha de Sérédou en Google Maps. Contactar con la administración o un guía acreditado antes de llegar; la coordenada no autoriza a internarse por pistas forestales.",
            "Estación relativamente seca y con reserva previa; prever un día completo.",
            "Omitir sin permiso, guía o información reciente del firme; el perro no debe entrar en el área protegida.",
            "UNESCO · Reserva de la Biosfera del macizo de Ziama",
            "https://www.unesco.org/en/mab/massif-du-ziama",
            [
                commons("Landscape of Ziama Massif.jpg", "Yakoo1986 · CC BY-SA 4.0", "Relieve forestal del macizo de Ziama."),
                commons("Lowland rainforest of Ziama Massif.jpg", "Yakoo1986 · CC BY-SA 4.0", "Selva húmeda de tierras bajas dentro de Ziama."),
                commons("Montane rainforest near to Sérédou (Ziama).jpg", "Yakoo1986 · CC BY-SA 4.0", "Bosque montano cerca de la base de Sérédou."),
            ],
            name="Sérédou · acceso al macizo de Ziama",
            coords=(8.371919, -9.2868745),
        ),
        16: entry(
            "La Reserva Natural Integral del Monte Nimba protege el macizo fronterizo de mayor biodiversidad del país. El pin identifica el espacio protegido; el acceso efectivo se confirma con su administración.",
            "Es el paisaje natural más excepcional del sureste y un sitio UNESCO amenazado que exige visita responsable.",
            "El pin se ajusta a la ficha de la reserva en Google Maps, no a una recepción. Organizar permiso, guía y puerta concreta desde Lola o la base que indique el gestor.",
            "Estación seca, varios días disponibles y condiciones acordadas antes de salir.",
            "Omitir sin autorización escrita, con actividad minera o fronteriza conflictiva, o si no se garantiza que el perro quede fuera del área estricta.",
            "UNESCO · Reserva Natural Integral del Monte Nimba",
            "https://whc.unesco.org/en/list/155/",
            [
                commons("Mount Nimba Strict Nature Reserve-108453.jpg", "Guy Debonnet · CC BY-SA 3.0 IGO", "Relieve montañoso de la Reserva Natural Integral del Monte Nimba."),
                commons("Mount Nimba Strict Nature Reserve-123989.jpg", "Guy Debonnet · CC BY-SA 3.0 IGO", "Bosque y laderas del macizo protegido."),
                commons("Nimba montanegrassland.jpg", "Yakoo1986 · CC BY-SA 4.0", "Pastizal montano característico del Nimba guineano."),
            ],
            coords=(7.6378125, -8.4184375),
        ),
    },
    "sierra-leona": {
        2: entry(
            "Freetown es la gran base logística del país y una ciudad construida entre puerto, colinas y barrios costeros. El histórico Cotton Tree cayó en 2023: sus fotos son memoria, no una promesa de visita.",
            "Concentra servicios, patrimonio krio y los operadores necesarios para islas, playas y reservas.",
            "El pin se ajusta a la ficha de Freetown en Google Maps porque describe el nodo urbano. Reservar estacionamiento vigilado y planear cada salida por el tráfico de la península.",
            "Días laborables para gestiones; recorridos urbanos de mañana y antes del anochecer.",
            "Reducir la visita si las lluvias, atascos o falta de aparcamiento seguro impiden moverse con margen.",
            "Ministerio de Turismo · historia de Sierra Leona",
            "https://tourismsierraleone.com/where-to-go/freetown/",
            [
                commons("Freetown-aerialview.jpg", "David Hond · CC BY 2.0", "Freetown y su gran estuario vistos desde el aire."),
                commons("Cotton Tree (Sierra Leone).jpg", "Christian Trede · CC BY-SA 2.0 DE", "El Cotton Tree antes de su caída en mayo de 2023."),
                commons("Aberdeen, Freetown, Sierra Leone - panoramio.jpg", "Ghassan Mroue · CC BY-SA 3.0", "Costa y tejido urbano de Aberdeen, Freetown."),
            ],
            coords=(8.4870803, -13.2354918),
        ),
        3: entry(
            "El museo ferroviario de Cline Town conserva locomotoras y coches del antiguo Sierra Leone Government Railway. Es una colección visitable con horario y contacto publicados.",
            "Cuenta de forma tangible cómo funcionó el transporte interior antes del cierre de la red en 1974.",
            "El pin se corrige a National Railway Museum en Google Maps. Abre de lunes a viernes 09:30–16:30 y sábados con cita; llamar antes según la web oficial.",
            "Mañana de día laborable, reservando entre una y dos horas.",
            "Omitir si el museo no confirma apertura o si no hay estacionamiento seguro en Cline Town.",
            "Museo ferroviario · horarios y contacto",
            "https://www.sierraleonerailwaymuseum.org/visit-us",
            [
                commons("Freetown Railway Museum.jpg", "Davidbstanley · dominio público", "Material ferroviario preservado en el museo de Freetown."),
                commons("Hunslet 2-6-2 loco in Sierra Leone.jpg", "Davidbstanley · CC BY-SA 3.0", "Locomotora Hunslet número 81 de la colección."),
                external("https://www.radiomuseum.org/museum/wal/national-railway-museum-of-sierra-leone-freetown/images/wal_freetown_gallery4.jpg", "https://www.radiomuseum.org/museum/wal/national-railway-museum-of-sierra-leone-freetown/", "Radiomuseum.org · derechos en la fuente", "Locomotora Beyer-Garratt n.º 73 conservada dentro del museo de Freetown."),
            ],
            coords=(8.4893757, -13.208807),
        ),
        4: entry(
            "Tacugama rescata y rehabilita chimpancés dentro del bosque de la península. Las visitas y eco-lodges se reservan directamente y pueden suspenderse por conservación o seguridad.",
            "Es la mejor experiencia educativa sobre el chimpancé occidental cerca de Freetown y financia conservación real.",
            "El pin se corrige a la ficha exacta del santuario en Google Maps. Reservar por la web o WhatsApp oficial y confirmar el estado de la pista; no presentarse sin cita.",
            "Tour de mañana reservado; estación seca facilita el acceso por carretera.",
            "Omitir sin confirmación escrita, durante un cierre del santuario o si no se puede dejar al perro fuera de la visita.",
            "Tacugama · visitas y reservas",
            "https://www.tacugama.com/",
            [
                external("https://www.bigworldsmallpockets.com/wp-content/uploads/2023/03/Sierra-Leone-Tacugama-Sanctuary-Male-Chimp.jpg", "https://www.bigworldsmallpockets.com/tacugama-chimpanzee-sanctuary/", "Big World Small Pockets · derechos en la fuente", "Chimpancés rescatados dentro de un recinto forestal de Tacugama."),
                external("https://www.africaoutlookmag.com/media/2024/12/SierraLeone-Hannemann1-jpg.webp", "https://www.africaoutlookmag.com/economy/the-national-tourist-board-of-sierra-leone", "Africa Outlook · derechos en la fuente", "Entrada identificable del santuario de Tacugama."),
                external("https://patintheworld.com/wp-content/uploads/2023/08/pxl_20230813_133752275.jpg", "https://patintheworld.com/2025/11/02/tacugama-chimpanzee-sanctuary/", "Pat in the World · derechos en la fuente", "Cartel del santuario entre la vegetación."),
            ],
            coords=(8.4169179, -13.2072019),
        ),
        6: entry(
            "River No. 2 combina una playa clara con la desembocadura de un río y gestión comunitaria. Es fácil de alcanzar desde Freetown, pero el baño depende de mar, corrientes y marea.",
            "Es el paisaje costero más completo de la península para una visita de medio día.",
            "El pin se corrige a River No 2 Beach en Google Maps. Usar la entrada comunitaria, pagar los servicios acordados y estacionar donde indiquen los responsables.",
            "Entre semana y por la mañana; comprobar marea y oleaje.",
            "Omitir con mar fuerte, lluvia intensa, playa saturada o si no hay vigilancia razonable del vehículo.",
            "Ministerio de Turismo · playas de Sierra Leona",
            "https://tourismsierraleone.com/attractions/river-no-2-beach/",
            [
                commons("River No. 2 Beach (Sierra Leone).jpg", "Christian Trede · Attribution", "Arena, río y montaña en River No. 2 Beach."),
                commons("The Number 2 , Sierra Leone.jpg", "Hussein Kefel · CC BY-SA 3.0", "La desembocadura de Number 2 y su paisaje costero."),
                external("https://images.squarespace-cdn.com/content/v1/695878164097753f1257ad8a/1767405595424-U85BRTDD5437RPZJN02B/birdseye%2Bof%2Bbeach%2B%281%29.jpg", "https://www.growingthegrassroots.org/river-no2-beach", "Growing the Grassroots · derechos en la fuente", "Vista aérea de la barra de arena y el estuario de River No. 2."),
            ],
            coords=(8.3334978, -13.2037767),
        ),
        8: entry(
            "Bureh Beach reúne playa, pueblo y un club de surf de raíz comunitaria. Las clases y tablas deben reservarse o confirmarse con el club, no darse por supuestas.",
            "Permite decidir entre descanso costero y una actividad de surf con impacto local.",
            "El pin se corrige a la playa exacta de Google Maps; el anterior estaba varios kilómetros desplazado. Preguntar en el pueblo por el club activo y respetar la zona de pescadores.",
            "Mañana con previsión de mar adecuada; mejor entre semana.",
            "No entrar al agua sin información local de corrientes, con tormenta o sin material y supervisión adecuados.",
            "Ministerio de Turismo · Bureh Beach",
            "https://tourismsierraleone.com/attractions/bureh-beach/",
            [
                external("https://www.surfertoday.com/images/stories/bureh-surf-club.jpg", "https://www.surfertoday.com/surfing/bureh-beach-surf-club-is-founded-in-sierra-leone", "SurferToday · derechos en la fuente", "Primer local identificado del Bureh Beach Surf Club."),
                external("https://www.surfer.com/.image/c_fill%2Cw_1200%2Ch_1200%2Cg_faces%3Acenter/MTk2Mjc2ODEzNDYyNzA5Nzg3/img_1073.jpg", "https://www.surfer.com/culture/sierra-leone-surf-club", "SURFER · derechos en la fuente", "Surfistas y tablas delante del club comunitario de Bureh."),
                external("https://images.squarespace-cdn.com/content/v1/5a17221c49fc2bfdcee7e37e/33c16852-40e3-4218-9292-5f70c7e659ce/SB%2BBBC.jpg", "https://www.dreamtown.ngo/stories/2022/10/21/surf-bunkers-x-dreamtown", "Dreamtown · derechos en la fuente", "Actividad comunitaria de surf en Bureh Beach."),
            ],
            coords=(8.2113922, -13.1554723),
        ),
        9: entry(
            "Las Islas Banana reúnen playas, senderos y memoria de la trata en Dublin y Ricketts, unidas por una calzada. Se llega en barca desde Kent y conviene pasar al menos una noche.",
            "Aportan la mejor combinación insular de paisaje, vida local e historia del país, distinta de las playas de la península.",
            "El pin coincide con la ficha exacta Banana Islands de Google Maps y representa el archipiélago, no el embarcadero. Reservar el traslado desde Kent con el alojamiento, exigir chalecos y pactar equipaje, perro, precio y regreso antes de embarcar.",
            "Estación seca, mar tranquilo y salida temprana desde Kent; una o dos jornadas.",
            "Omitir con mala mar, barco sin chalecos, alojamiento no confirmado o negativa expresa a llevar al perro; no improvisar la vuelta al anochecer.",
            "Sierra Leone Tourism · Banana Islands",
            "https://tourismsierraleone.com/attractions/banana-islands/",
            [
                commons("Banana Islands (Sierra Leone).jpg", "Christian Trede · Attribution", "Costa y relieve de las Islas Banana vistos desde el mar."),
                external("https://rainbowtours.imgix.net/1973/banana-island-5-awesome.jpg?auto=enhance&crop=focalpoint&fit=crop&fp-x=0.5&fp-y=0.5&fp-z=1&h=490&w=726", "https://www.rainbowtours.co.uk/tours/africa/sierra-leone-natural-history-explorer", "Rainbow Tours · derechos en la fuente", "Orilla boscosa de Banana Island con las embarcaciones locales."),
                external("https://oldturtlebay.com/wp-content/uploads/2024/04/beach5-1024x920.jpeg", "https://oldturtlebay.com/", "Old Turtle Bay Beach Resort · derechos en la fuente", "Playa de Old Turtle Bay en Ricketts, una de las Islas Banana."),
            ],
            coords=(8.1158998, -13.2115287),
        ),
        10: entry(
            "Bunce Island conserva las ruinas de uno de los principales fuertes británicos de trata esclavista del estuario. La visita exige embarcación y guía para comprender el lugar y regresar con seguridad.",
            "Es el PDI histórico más importante del país por su vínculo directo con la diáspora de Carolina y Georgia.",
            "El pin se ajusta a la isla exacta de Google Maps. Contratar barco con chalecos y guía autorizado, fijar marea, punto de embarque y hora límite de retorno.",
            "Mañana, mar y río tranquilos, con al menos medio día disponible.",
            "Omitir con tormenta, embarcación insegura, guía no confirmado o regreso después del anochecer; el perro no debe desembarcar.",
            "Ministerio de Turismo · Bunce Island",
            "https://tourismsierraleone.com/attractions/bunce-island/",
            [
                commons("Bunce Island Fortress Wall 01.jpg", "Pierre Chrzanowski · CC0", "Muros conservados del fuerte de Bunce Island."),
                commons("Bunce Island Fortress Cannon.jpg", "Pierre Chrzanowski · CC0", "Cañón y ruinas del recinto histórico."),
                commons("Bunce Island Beach.jpg", "Pierre Chrzanowski · CC0", "Orilla donde desembarcan las visitas a Bunce Island."),
            ],
            coords=(8.5698616, -13.0403748),
        ),
        13: entry(
            "Gola Rainforest forma con Tiwai el primer sitio Patrimonio Mundial de Sierra Leona, inscrito en 2025. La selva se visita solo con coordinación previa y acceso indicado por el parque.",
            "Protege el mayor bloque de selva baja del país y permite entender conservación comunitaria a escala de paisaje.",
            "El pin se ajusta a la ficha del parque en Google Maps, pero no representa una puerta. Contactar antes con la administración; se recomienda 4x4 y guía, y debe confirmarse el acceso concreto desde Kenema.",
            "Estación seca y reserva previa, con uno o dos días disponibles.",
            "Omitir sin respuesta del parque, tras lluvias fuertes o si se espera un safari de avistamientos garantizados; el perro no entra.",
            "UNESCO · Complejo Gola-Tiwai",
            "https://whc.unesco.org/en/list/1746",
            [
                google_photo("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkAb4Xql1XivdDNWziMXqVTQhVTtIaHvtEpG_UmyYPNJOw6-pp-BrFkGD5Rs0OrXNRr0Z-gxi63rHKw8phZTmqWFSjXcwNh_qntighWd50ih21zhm09NbBjzsAyJhV84suNFzcIwg", "Gola Rainforest National Park Sierra Leone", "Fotografía aportada a la ficha exacta de Gola Rainforest National Park."),
                commons("Leptopelis macrotis (10.3897-zse.90.7120) Figure 2 (cropped).jpg", "Roedel et al. · CC BY 4.0", "Anfibio fotografiado en Gola; ejemplo de la biodiversidad que protege."),
                commons("NW160-12 Acraea camaena (3430976449).jpg", "NSG group · CC0", "Mariposa documentada en Gola Forest East."),
            ],
            coords=(7.6663373, -10.841529),
        ),
        14: entry(
            "Tiwai es una isla de selva en el río Moa con campamento, senderos y recorridos guiados. Forma parte del sitio UNESCO Gola-Tiwai y mantiene una web de reservas activa.",
            "Ofrece la experiencia de selva más operativa del país y beneficia directamente a las comunidades vecinas.",
            "El pin se ajusta a Tiwai Island Wildlife Sanctuary en Google Maps. Reservar alojamiento, comida, guía y cruce en canoa a través de la web oficial; llevar efectivo y sacar los residuos.",
            "Estación seca, mínimo una noche y actividades de amanecer o atardecer.",
            "Omitir sin reserva, con río crecido o traslado nocturno; no llevar al perro al santuario.",
            "Tiwai Island · visita y reservas",
            "https://www.tiwaiisland.org/visit/",
            [
                commons("Tiwai Island River.jpg", "Stephanie Zito · CC BY-SA 1.0", "Cruce del río Moa hacia el santuario de Tiwai."),
                commons("Tiwai Island - flickr (banner).jpg", "Dorothy Voorhees · CC BY-SA 2.0", "Bosque y orilla de la isla de Tiwai."),
                commons("Tiwa Island - flickr.jpg", "Dorothy Voorhees · CC BY-SA 2.0", "Sendero y vegetación dentro de la isla."),
            ],
            coords=(7.55415, -11.3553667),
        ),
        19: entry(
            "Bintumani es la cumbre más alta de Sierra Leona y una travesía remota en las montañas Loma. Requiere guía, porteadores y varios días; no es una excursión espontánea desde Kabala.",
            "Es el gran objetivo de montaña del país para quien quiera dedicarle una expedición propia.",
            "El pin se corrige a la cumbre Bintumani de Google Maps. Organizar permisos, guía, campamentos, comida y evacuación con un operador que conozca la ruta actual.",
            "Estación seca, salida muy temprana y margen meteorológico de varios días.",
            "Descartarlo sin equipo, guía o comunicación de emergencia, con lesión o lluvia; no llevar al perro a esta travesía.",
            "Ministerio de Turismo · montaña de Bintumani",
            "https://tourismsierraleone.com/where-to-go/loma-mountains-and-mount-bintumani/",
            [
                commons("Mountain Bintunami.jpg", "Rokaso · CC BY-SA 4.0", "Perfil de Bintumani al comienzo de la estación lluviosa."),
                commons("Mount Bintumani 1992 or 93.jpg", "sierra-leone143 · CC BY 2.0", "Laderas de la cumbre durante una ascensión."),
                commons("Mount Bintumani 1992 or 93 (2).jpg", "sierra-leone143 · CC BY 2.0", "Tramo de subida al monte Bintumani."),
            ],
            coords=(9.2166667, -11.1166667),
        ),
        20: entry(
            "Outamba-Kilimi combina sabana húmeda, bosque de galería y recorridos en canoa en dos sectores separados. La infraestructura es básica y debe confirmarse antes del desvío.",
            "Es el parque más interesante del norte para combinar paisaje, huellas de fauna y navegación tranquila.",
            "Google Maps no devuelve una ficha inequívoca; se conserva la referencia cartográfica auditada del sector Outamba. Confirmar oficina, guía, alojamiento y estado de la pista desde Kamakwie antes de salir.",
            "Estación seca y primera hora; prever al menos una noche y combustible de reserva.",
            "Omitir tras lluvias, sin contacto del parque o si la canoa carece de chalecos; el perro no entra en el área protegida.",
            "Ministerio de Turismo · Outamba-Kilimi",
            "https://tourismsierraleone.com/where-to-go/outamba-kilimi-national-park/",
            [
                commons("Vista of Outamba Kilimi Park.JPG", "Leasmhar · CC BY-SA 3.0", "Vista de sabana y bosque desde el sendero Karangia."),
                commons("Outamba Kilimi Park Sierra Leone.JPG", "Leasmhar · CC BY-SA 3.0", "Recorrido en canoa dentro de Outamba-Kilimi."),
                commons("Karangia Trail Outamba-Kilimi Park Sierra Leone.JPG", "Leasmhar · CC BY-SA 3.0", "Guía local en el sendero Karangia del parque."),
            ],
        ),
    },
    "liberia": {
        2: entry(
            "Robertsport ocupa una península entre el Atlántico y el lago Piso, con varias rompientes y un club local de surf. Las condiciones del mar cambian y no todas las olas sirven a principiantes.",
            "Combina el mejor paisaje costero del país con una actividad gestionada localmente.",
            "El pin se ajusta a la ficha de Robertsport en Google Maps; acordar después playa, clase y alojamiento concretos con el club u operador. No dejar el vehículo aislado en la arena.",
            "Estación seca para carretera y mañana con previsión de oleaje adecuada.",
            "Omitir el surf con corrientes, tormenta o sin guía local; convertirlo en visita costera si el mar no acompaña.",
            "Autoridad de Turismo · Grand Cape Mount",
            "https://enjoyliberia.travel/blog/post/robertsport-liberia-the-ultimate-surfing-guide/",
            [
                commons("Robertsport Beach, Cape Mount County.jpg", "Bethel Anthony Chisom · CC BY-SA 4.0", "Playa de Robertsport en Grand Cape Mount."),
                commons("Robertsport Liberia.jpg", "Erik Cleves Kristensen · CC BY 2.0", "Península y asentamiento de Robertsport."),
                commons("ASC Leiden - F. van der Kraaij Collection - 05 - 057 - The bay of Robertsport with houses, the beach, and the Atlantic ocean - Robertsport, Grand Cape Mount County, Liberia, 1977.tiff", "Fred van der Kraaij · CC BY-SA 4.0", "Bahía, casas y playa de Robertsport en 1977."),
            ],
            coords=(6.7509063, -11.367219),
        ),
        3: entry(
            "Lake Piso es la mayor laguna costera de Liberia y un humedal Ramsar junto a Robertsport. La navegación o pesca debe contratarse con gente local que conozca la bocana y las mareas.",
            "Aporta manglar, aves y paisaje lagunar en contraste con el océano del lado opuesto de la península.",
            "El pin se ajusta a Lago Piso en Google Maps y representa el agua, no un embarcadero. Elegir con el operador un punto seguro, chalecos y hora de regreso.",
            "Amanecer o última hora, estación seca y marea confirmada.",
            "Omitir con viento, tormenta o embarcación sin chalecos; no conducir siguiendo el pin hacia la orilla sin una pista confirmada.",
            "Ramsar · Lake Piso",
            "https://rsis.ramsar.org/ris/1306",
            [
                commons("Lake Piso.jpg", "Bethel Anthony Chisom · CC BY-SA 4.0", "Vista abierta del lago Piso."),
                commons("A view of Lake Piso, Bomi County.jpg", "Bethel Anthony Chisom · CC BY-SA 4.0", "Orilla y vegetación del humedal."),
                commons("Lake Piso Drone Shot.jpg", "Bwoart · CC BY 4.0", "Vista aérea de la laguna y su escala."),
            ],
            coords=(6.7362206, -11.2637155),
        ),
        4: entry(
            "El Museo Nacional de Liberia ocupa el antiguo Legislative Building en Broad Street. Ofrece una visita concreta para entender la república, sus presidentes y la cultura material del país.",
            "Es la mejor introducción histórica de Monrovia y evita presentar toda la capital como un único PDI difuso.",
            "El pin se mueve a la ficha exacta Museo nacional de Liberia de Google Maps. Confirmar apertura el mismo día y aparcar con vigilancia en el centro.",
            "Mañana de día laborable; reservar una o dos horas y combinar gestiones por la zona.",
            "Omitir con museo cerrado, manifestaciones o imposibilidad de estacionar con seguridad.",
            "Liberia Tourism · sitios históricos",
            "https://enjoyliberia.travel/blog/post/a-guide-for-activities-shopping-and-tours-in-liber/",
            [
                commons("JFC-UA service members visit Liberian National Museum 150120-A-YF937-211.jpg", "Spc. Caitlyn Byrne · dominio público", "Sala y piezas del Museo Nacional de Liberia."),
                commons("JFC-UA service members visit Liberian National Museum 150120-A-YF937-233.jpg", "Spc. Caitlyn Byrne · dominio público", "Exposición interior distribuida en las plantas del museo."),
                commons("President Tubman's limousine.jpg", "Jforest59 · CC BY-SA 4.0", "Automóvil presidencial conservado en el Museo Nacional."),
            ],
            name="Museo Nacional de Liberia · Monrovia",
            coords=(6.3167718, -10.8039201),
        ),
        5: entry(
            "Providence Island es el lugar de desembarco de los colonos afroamericanos en 1822 y conserva monumentos sobre la fundación y los conflictos posteriores. La visita se coordina, no es un parque de acceso libre garantizado.",
            "Permite abordar las tensiones entre retorno, colonización, pueblos locales y nacimiento de Liberia en el lugar físico donde confluyen.",
            "Google Maps no ofrece una ficha inequívoca; se conserva el pin cartográfico de la isla junto al Gabriel Tucker Bridge. Organizar guía con Turismo o Cultura antes de ir.",
            "Mañana de día laborable y con visita confirmada.",
            "Omitir sin guía, con recinto cerrado o si el entorno no permite estacionar de forma segura.",
            "Autoridad de Turismo · Providence Island",
            "https://lnta.gov.lr/tourism-investment/",
            [
                commons("Providence Island.jpg", "Jforest59 · CC BY-SA 4.0", "Lado oriental de Providence Island desde el puente."),
                commons("Providence Island monument.jpg", "Jforest59 · CC BY-SA 4.0", "Monumento del árbol de armas en la isla."),
                commons("ASC Leiden - F. van der Kraaij Collection - 05 - 022 - A close up of Providence Island in full, in the Mesurado river - Monrovia, Mamba Point, Montserrado, Liberia, 1975.tif", "Fred van der Kraaij · CC BY-SA 4.0", "Providence Island completa en el río Mesurado en 1975."),
            ],
        ),
        9: entry(
            "Sapo protege una enorme extensión de selva primaria en Sinoe. La oferta turística sigue siendo remota y debe confirmarse con la autoridad o un operador; el pin no es una puerta de carretera.",
            "Es el principal parque de selva de Liberia y un refugio clave para hipopótamo pigmeo, elefante de bosque y chimpancé occidental.",
            "El pin se corrige a la ficha Parque nacional Sapo de Google Maps, más de 40 km al este del anterior; sigue siendo una referencia de área. No salir sin permiso, guía, puerta y campamento escritos.",
            "Estación seca, varios días, 4x4 preparado y autonomía completa.",
            "Descartarlo si la autoridad no confirma una visita operativa, con pista inundada o si se esperan avistamientos garantizados; el perro no entra.",
            "Liberia Tourism · Sapo National Park",
            "https://enjoyliberia.travel/pages/sapo-national-park/",
            [
                external("https://b-cdn.springnest.com/media/img/15n/dji_01664200e09.jpg?crop=1600%2C640%2C0%2C353&width=1500", "https://enjoyliberia.travel/pages/sapo-national-park/", "Liberia Tourism · derechos en la fuente", "Canopia continua del Parque Nacional de Sapo."),
                external("https://b-cdn.springnest.com/media/img/15n/dscf3146d7d45e7.jpg?height=916", "https://enjoyliberia.travel/pages/sapo-national-park/", "Liberia Tourism · derechos en la fuente", "Interior de selva documentado en la ficha oficial de Sapo."),
                external("https://b-cdn.springnest.com/media/img/15n/dscf3097a8b139c.jpg?width=800", "https://enjoyliberia.travel/pages/sapo-national-park/", "Liberia Tourism · derechos en la fuente", "Actividad guiada dentro del paisaje del parque."),
            ],
            coords=(5.4603195, -8.4403573),
        ),
        10: entry(
            "Harper conserva el trazado y algunos edificios de la antigua República de Maryland junto a Cabo Palmas. Su interés está en recorrer la ciudad y el faro con contexto, no en prometer mansiones visitables.",
            "Es el final cultural y costero más singular antes de Costa de Marfil.",
            "El pin se ajusta a Harper en Google Maps porque las huellas están dispersas. Contratar guía local, preguntar por accesos y no entrar en ruinas inestables.",
            "Estación seca, luz de mañana y al menos una noche en la ciudad.",
            "Omitir con carretera cortada, sin alojamiento seguro o si solo se dispone de una parada breve.",
            "Liberia Tourism · destinos y patrimonio",
            "https://visitliberia.com/things-to-do-in-liberia/",
            [
                commons("ASC Leiden - F. van der Kraaij Collection - 15 - 37 - The lighthouse Cape Palmas Light on a peninsula in the Atlantic Ocean - Harper city, Maryland County, Liberia - 1979.tif", "Fred van der Kraaij · CC BY-SA 4.0", "Faro de Cabo Palmas y pista de acceso en 1979."),
                commons("HEARD(1898) 50 Church of Harper, Cape Palmas.jpg", "William H. Heard · dominio público", "Iglesia histórica de Harper a finales del siglo XIX."),
                commons("Cape Palmas etch.jpg", "Wagner & C. · dominio público", "Vista histórica de Cabo Palmas en 1853."),
            ],
            coords=(4.3759676, -7.7009416),
        ),
        13: entry(
            "East Nimba Nature Reserve conserva el lado liberiano del macizo y las huellas de la minería LAMCO. No forma parte del bien UNESCO de Guinea y Costa de Marfil, aunque comparte el mismo paisaje fronterizo.",
            "Combina una montaña excepcional, historia industrial, Blue Lake y rutas guiadas desde Yekepa.",
            "El pin se corrige a East Nimba Nature Reserve Cornerstone en Google Maps. Pasar por la recepción, pagar la entrada y contratar guía; confirmar si la pista histórica admite el vehículo ese día.",
            "Estación seca y salida de mañana; una noche en Yekepa o Nimba Ecolodge evita correr.",
            "Omitir sin guía, con niebla o lluvia fuerte, o si la actividad minera restringe accesos; el perro queda fuera de senderos sensibles.",
            "Liberia Tourism · Mount Nimba",
            "https://enjoyliberia.travel/pages/mount-nimba/",
            [
                external("https://b-cdn.springnest.com/media/img/15n/dji_063752250b4.jpg?crop=1600%2C640%2C0%2C294&width=1500&quality=78", "https://enjoyliberia.travel/pages/mount-nimba/", "Liberia Tourism · derechos en la fuente", "Relieve y antigua pista minera de East Nimba."),
                external("https://b-cdn.springnest.com/media/img/15n/blue_lake_waterfalls_ennr6682dac.png?height=1204", "https://enjoyliberia.travel/pages/mount-nimba/", "Liberia Tourism · derechos en la fuente", "Blue Lake dentro del paisaje minero rehabilitado de East Nimba."),
                external("https://b-cdn.springnest.com/media/img/15n/lamco_ruins_ennr_247cd699.png?width=800", "https://enjoyliberia.travel/pages/mount-nimba/", "Liberia Tourism · derechos en la fuente", "Restos de la etapa LAMCO absorbidos por la vegetación."),
            ],
            name="East Nimba Nature Reserve · Yekepa",
            coords=(7.5558497, -8.4732243),
        ),
        15: entry(
            "Kpatawee tiene dos cascadas, pozas, senderos y un ecolodge operativo cerca de Gbarnga. La primera caída es sencilla; la segunda requiere aproximadamente una hora a pie según el gestor.",
            "Es la parada natural más fácil de ejecutar en el interior liberiano, con alojamiento y reserva directa.",
            "El pin se ajusta a la ficha Cascada Kpatawee de Google Maps. Reservar con el ecolodge, seguir al guía hacia la segunda caída y no cruzar roca mojada fuera de las rutas.",
            "Estación seca o transición con caudal moderado; mañana antes de grupos locales.",
            "Omitir con crecida, tormenta o si el resort no confirma acceso; no bañarse fuera de la zona indicada por el socorrista.",
            "Kpatawee Waterfalls Ecolodge · reservas",
            "https://www.kpataweewaterfalls.com/",
            [
                commons("Front View of Kpatawee Falls.jpg", "Bethel Anthony Chisom · CC BY-SA 4.0", "Vista frontal de la cascada principal de Kpatawee."),
                external("https://b-cdn.springnest.com/media/img/15n/dji_04736490596.jpg?width=800", "https://enjoyliberia.travel/pages/kpatawee-waterfall/", "Liberia Tourism · derechos en la fuente", "Vista elevada del conjunto de Kpatawee."),
                external("https://b-cdn.springnest.com/media/img/15n/kpatawee_falls_ecolodge5753ec7.jpg?width=800", "https://enjoyliberia.travel/pages/kpatawee-waterfall/", "Liberia Tourism · derechos en la fuente", "Cascada y equipamiento del ecolodge junto al sendero."),
            ],
            coords=(7.1223645, -9.6407703),
        ),
    },
    "costa-de-marfil": {
        1: entry(
            "La reserva estricta del monte Nimba ocupa el macizo fronterizo compartido con Guinea. Su régimen de protección exige permisos y guía; el pin identifica el área, no una entrada libre.",
            "Es el gran paisaje montano del oeste marfileño y un sitio UNESCO de biodiversidad excepcional.",
            "El pin se ajusta a la ficha marfileña de la Reserva Natural Integral del Monte Nimba en Google Maps. Coordinar puerta, autorización y guía con OIPR antes de acercarse.",
            "Estación seca y varios días de margen desde Man o Danané.",
            "Omitir sin permiso, con restricciones fronterizas o mineras, o si no se puede dejar al perro fuera de la reserva.",
            "UNESCO · Reserva Natural Integral del Monte Nimba",
            "https://whc.unesco.org/en/list/155/",
            [
                commons("Réserve naturelle intégrale du mont Nimba.webp", "Jojoy99 · CC BY-SA 4.0", "Laderas forestales de la reserva del monte Nimba."),
                commons("Mount Nimba Strict Nature Reserve-108448.jpg", "Guy Debonnet · CC BY-SA 3.0 IGO", "Relieve y mosaico vegetal del macizo protegido."),
                commons("Musoke Deo MDK-MUSO 45 THE CANOPY FORMED BY BAMBOO TREES ON MOUNT-NIMBA TRASBOUNDARY PROTECTED AREA IN IVORY COAST.png", "MDK-MUSO · CC BY-SA 4.0", "Dosel de bambú en el sector marfileño del Nimba."),
            ],
            coords=(7.5819758, -8.4183833),
        ),
        3: entry(
            "La Dent de Man es la cumbre rocosa que domina la ciudad y se asciende por senderos desde aldeas del pie. No debe confundirse con la Cascade de Man, situada en Zadepleu.",
            "Es la caminata emblemática de Man y ofrece una vista completa del anfiteatro montañoso.",
            "Google Maps no devuelve una ficha inequívoca; se conserva la cumbre OSM auditada. Contratar guía en Man y confirmar el inicio en Glongouin, Zogoualé o Bantégouen.",
            "Amanecer o primera mañana de estación seca; reservar medio día.",
            "Descartarla con tormenta, roca mojada, niebla densa o sin guía; no asumir que el perro supere trepadas o bloques.",
            "Google Maps · Dent de Man",
            "https://www.google.com/maps/search/?api=1&query=Dent%20de%20Man%20C%C3%B4te%20d%27Ivoire",
            [
                commons("The Dent de Man mountain.jpg", "Milequem Diarassouba · CC BY-SA 4.0", "Perfil reconocible de la Dent de Man."),
                commons("Dent de Man montagne.jpg", "Zenman/Letsgoforward · CC BY-SA 3.0", "La cumbre vista desde el entorno urbano."),
                commons("Dent de Man 23-08-2024.jpg", "BeraDigle · CC0", "Vista hacia Man desde la propia montaña."),
            ],
        ),
        5: entry(
            "La Cascade de Man cae dentro de un bosque de bambú cerca de Zadepleu. Es una visita corta y distinta de la subida a la Dent de Man.",
            "Ofrece el acceso natural más sencillo del bloque de Man y funciona incluso sin dedicar un día entero a montaña.",
            "El pin se ajusta a Man's Waterfalls en Google Maps. Usar la entrada señalizada, pagar al custodio si corresponde y permanecer en el sendero.",
            "Mañana, con caudal moderado y antes de la mayor afluencia.",
            "Omitir con crecida, tormenta o sendero cerrado; no subir por roca húmeda fuera del recorrido.",
            "Google Maps · Cascade de Man",
            "https://www.google.com/maps/search/?api=1&query=Cascade%20de%20Man%20C%C3%B4te%20d%27Ivoire",
            [
                commons("Les cascades de Man.jpg", "Sahi Tia · CC BY-SA 4.0", "Cascada de Man rodeada de vegetación."),
                commons("Les chutes d'eau de la Cascade de Man dans la région du Tonkpi 02.jpg", "Yasield · CC0", "Caída principal cerca de Zadepleu."),
                commons("CASCADE DE MAN 2.jpg", "Petrus yh · CC BY 4.0", "Poza y pared rocosa de la Cascade de Man."),
            ],
            coords=(7.41205, -7.5849645),
        ),
        6: entry(
            "El puente de lianas de Lieupleu/Vatouo es una pasarela ritual mantenida por comunidades dan cerca de la frontera liberiana. La visita necesita permiso local y no es una infraestructura vial.",
            "Es una obra de ingeniería vegetal viva y una experiencia cultural difícil de encontrar en otro tramo de la ruta.",
            "Google Maps no ofrece ficha inequívoca; se conserva el nodo exacto del puente auditado en OSM, a 21 km al sur de Danané. Llegar con guía local y preguntar antes de cruzar o fotografiar.",
            "Estación seca y de día, dejando margen para la pista desde Danané.",
            "Omitir tras lluvias, si la comunidad no autoriza, si el puente está en reparación o si la pista obliga a regresar de noche.",
            "Turismo del oeste marfileño · puentes de lianas",
            "https://baobab-gourmantche.over-blog.com/2016/09/le-pont-de-lianes-de-lieupleu.html",
            [
                commons("Pont de lianes de Lieupleu.jpg", "Drorita · CC BY-SA 4.0", "Puente de lianas de Lieupleu sobre el río Cavally, fotografiado en 2018."),
                external("https://img.over-blog-kiwi.com/0/84/17/29/20160928/ob_851292_16-09-177-lieupleu-cavally.jpg", "https://baobab-gourmantche.over-blog.com/2016/09/le-pont-de-lianes-de-lieupleu.html", "Le Baobab Gourmantché · derechos en la fuente", "Vista completa del puente de Lieupleu y del caudal del Cavally."),
                external("https://img.over-blog-kiwi.com/0/84/17/29/20160928/ob_33412c_16-09-184-lieupleu-cavally.jpg", "https://baobab-gourmantche.over-blog.com/2016/09/le-pont-de-lianes-de-lieupleu.html", "Le Baobab Gourmantché · derechos en la fuente", "Entramado de lianas y paso sobre el Cavally en Lieupleu."),
            ],
        ),
        8: entry(
            "La Basílica de Nuestra Señora de la Paz domina Yamoussoukro con su gran cúpula y columnata. Tiene visita interior reglada y sigue siendo lugar de culto.",
            "Es el edificio contemporáneo más monumental del itinerario y permite leer la ambición política de Houphouët-Boigny.",
            "El pin se corrige a la ficha exacta de la basílica en Google Maps. Confirmar horario y normas de vestimenta; aparcar en el recinto indicado.",
            "Mañana, fuera de celebraciones multitudinarias; prever dos horas.",
            "Omitir el interior durante oficio, cierre o si no se aceptan las normas; el perro queda fuera.",
            "Sitio oficial de la Basílica de Yamoussoukro",
            "https://basilique-notredamedelapaix.com/",
            [
                commons("Basilique notre Dame de la Paix de Yamoussoukro 9.jpg", "Didierwiki · CC0", "Vista frontal y cúpula de la basílica."),
                commons("Basilique notre Dame de la Paix de Yamoussoukro 19.jpg", "Didierwiki · CC0", "Columnata y escala del edificio."),
                commons("Basilique notre Dame de la Paix de Yamoussoukro 16.jpg", "Didierwiki · CC0", "Perspectiva elevada del conjunto basilical."),
            ],
            coords=(6.8148643, -5.2930753),
        ),
        9: entry(
            "Taï protege el mayor bloque de selva primaria del país y poblaciones estudiadas de chimpancé occidental. Las visitas se organizan desde bases concretas; el pin del parque no es una recepción.",
            "Es la experiencia de selva más importante de Costa de Marfil y un sitio UNESCO de primer nivel.",
            "El pin se ajusta a la ficha del parque en Google Maps. Reservar con OIPR o un operador reconocido y obtener por escrito puerta, guía, alojamiento y reglas del área.",
            "Estación relativamente seca, varios días y salidas de amanecer.",
            "Omitir sin permiso o guía, con pista inundada o si se esperan chimpancés garantizados; el perro no entra.",
            "UNESCO · Parque Nacional de Taï",
            "https://whc.unesco.org/en/list/195/",
            [
                commons("Taï National Park (24148248710) (cropped).jpg", "yakovlev.alexey · CC BY-SA 2.0", "Dosel y vegetación del Parque Nacional de Taï."),
                commons("Parc national de Taï.jpg", "Jojoy99 · CC BY-SA 4.0", "Paisaje forestal identificado del parque."),
                google_photo("https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlnunrxNn7RTl09Qxfm7I9bQiDPowcXx1dRlEQ42q6TetDCOufSWyyd8e7DWgT9yX5ROaJuSx09XX12MPPhUn-7L1deUuESk4HqttmEUIyIZGVNnO0kJ0_4Dr8zAC2Um2VtV9xAA22oeygU", "Parc national de Taï Côte d'Ivoire", "Fotografía aportada a la ficha exacta del Parque Nacional de Taï."),
            ],
            coords=(5.69, -6.9394444),
        ),
        11: entry(
            "Sassandra conserva el antiguo wharf, el puente Weygand y edificios históricos alrededor de una bahía pesquera. Es una escala costera con elementos concretos, no solo una playa genérica.",
            "Combina patrimonio portuario, actividad actual y costa en un lugar compacto.",
            "El pin se corrige a Old Sassandra wharf en Google Maps. Recorrer de día, preguntar antes de entrar en estructuras y mantener distancia de ruinas y oleaje.",
            "Mañana para el puerto o tarde para el frente marítimo; prever medio día.",
            "Omitir con temporal, acceso al wharf cerrado o si la carretera obliga a terminar la etapa de noche.",
            "Información de Sassandra",
            "https://fr.wikipedia.org/wiki/Sassandra",
            [
                commons("Sassandra1.jpg", "Bound8 · CC BY-SA 3.0", "Antiguo wharf de Sassandra sobre el Atlántico."),
                commons("Pont Weygand de Sassandra 06 2026.jpg", "Asunachibi · CC BY-SA 4.0", "Puente Weygand de Sassandra en 2026."),
                commons("Bâtiments historiques à Sassandra 01.jpg", "Slick linda · CC BY-SA 4.0", "Ruinas de un edificio histórico de Sassandra."),
            ],
            coords=(4.9521085, -6.0808884),
        ),
        13: entry(
            "Le Plateau concentra la silueta moderna, la catedral, la gran mezquita y buena parte de las gestiones de Abiyán. La ciudad es ante todo una base logística y debe recorrerse por zonas.",
            "Permite resolver trámites y entender la metrópoli lagunar sin convertir toda Abiyán en una visita interminable.",
            "El pin se ajusta al barrio Plateau de Google Maps. Elegir alojamiento con aparcamiento vigilado, usar conductor local si conviene y agrupar visitas para evitar cruzar puentes repetidamente.",
            "Días laborables para gestiones; primera hora o final de tarde para vistas.",
            "Reducir la visita con tráfico extremo, protestas o falta de estacionamiento seguro.",
            "Côte d'Ivoire Tourisme · Abiyán",
            "https://www.tourismecotedivoire.ci/",
            [
                commons("Plateau 2010, Abidjan.jpg", "RyansWorld · CC BY-SA 3.0", "Silueta diurna de Le Plateau."),
                commons("Plateau Abidjan de nuit.jpg", "abdallahh · CC BY 2.0", "Torres de Le Plateau iluminadas de noche."),
                commons("WikiConvFr23 à Abidjan en Cote d'Ivoire vue panoramique de la ville du Plateau depuis Grand Hotel.jpg", "Adoscam · CC0", "Panorama del distrito desde el Grand Hôtel."),
            ],
            coords=(5.3325471, -4.023869),
        ),
        14: entry(
            "El Quartier France de Grand-Bassam conserva edificios administrativos y viviendas de la primera capital colonial. El valor está en caminar el conjunto y entender su relación con laguna, comercio y segregación urbana.",
            "Es el mejor paisaje urbano histórico del país y Patrimonio Mundial desde 2012.",
            "Google Maps no devuelve una ficha única del barrio; se conserva el ancla auditada dentro del conjunto UNESCO. Aparcar y recorrer a pie de día, sin entrar en edificios cerrados o inestables.",
            "Mañana o última tarde; medio día permite combinar museo y calles.",
            "Omitir interiores cerrados, zonas dañadas o la playa con oleaje peligroso; el barrio sigue habitado.",
            "UNESCO · Ciudad histórica de Grand-Bassam",
            "https://whc.unesco.org/en/list/1322/",
            [
                commons("Historic town of Grand-Bassam 24092023 080.jpg", "Yamen · CC BY-SA 4.0", "Edificio del conjunto histórico de Grand-Bassam."),
                commons("Historic town of Grand-Bassam 24092023 012.jpg", "Yamen · CC BY-SA 4.0", "Calle y arquitectura del Quartier France."),
                commons("Historic town of Grand-Bassam 24092023 002.jpg", "Yamen · CC BY-SA 4.0", "Otra fachada conservada dentro del bien UNESCO."),
            ],
        ),
        15: entry(
            "Assinie-Mafia ocupa un cordón estrecho entre océano y laguna, con manglar, embarcaciones y alojamientos dispersos. El PDI marca el pueblo; cada playa o embarcadero se elige después.",
            "Es la última gran pausa costera antes de Ghana y combina agua dulce, laguna y Atlántico.",
            "El pin se ajusta a Assinie-Mafia en Google Maps, corrigiendo la antigua referencia de Assouindé. Reservar alojamiento con estacionamiento y pactar cualquier cruce en piragua con chalecos.",
            "Entre semana, estación seca y con marea y mar consultados.",
            "Omitir con oleaje fuerte, tormenta, alojamiento no confirmado o embarcación insegura.",
            "Côte d'Ivoire Tourisme · litoral",
            "https://www.visitcotedivoire.com/decouvrez/le-carnet-d-assinie",
            [
                commons("Assinie , Par Nabil ZORKOT.jpg", "Singoloua225 · CC BY-SA 4.0", "Cordón litoral y agua en Assinie."),
                commons("La mangrove d'Assinie.jpg", "Pol fourier · CC BY 4.0", "Manglar de la laguna de Assinie-Mafia."),
                commons("Assinie en 2025 04.jpg", "Dadrik · CC BY-SA 4.0", "Paisaje de Assinie documentado en diciembre de 2025."),
            ],
            coords=(5.1398055, -3.3237824),
        ),
        16: entry(
            "La mezquita de Sorobango, a 18 km de Bondoukou, es una de las ocho mezquitas sudanesas inscritas por UNESCO en 2021. Bondoukou sirve de base; el pin debe caer en el edificio, no en la ciudad.",
            "Convierte la etapa oriental en una visita patrimonial precisa y muestra arquitectura de tierra todavía vinculada a su comunidad.",
            "El pin se corrige a Grande Mosquée de Sorobango en Google Maps. Pedir permiso local antes de entrar o fotografiar y asumir que el interior puede no estar abierto a visitantes.",
            "Mañana, fuera de la oración del viernes y con tiempo seco.",
            "Omitir si la comunidad no autoriza, durante culto o si la pista está impracticable; el perro queda fuera del recinto.",
            "UNESCO · mezquitas sudanesas del norte marfileño",
            "https://whc.unesco.org/en/list/1648/",
            [
                commons("Mosquée sacrée de Sorobango.jpg", "AZIMIE · CC0", "Fachada actual de la mezquita de Sorobango."),
                commons("Pg168 Mosquée de Sorobango.jpg", "dominio público · autor en la fuente", "Documento histórico de la mezquita de Sorobango."),
                commons("Mosquée de Sorobango-1892 (cropped).jpg", "Édouard Riou · dominio público", "Grabado de la mezquita publicado en 1892."),
            ],
            name="Mezquita UNESCO de Sorobango · Bondoukou",
            coords=(8.1737936, -2.7089936),
        ),
        17: entry(
            "Comoé es un parque inmenso de sabana y bosque de galería, pero la situación de seguridad del noreste puede invalidar la visita. Kakpin se conserva como referencia sur, no como promesa de acceso.",
            "Solo merece el desvío si OIPR confirma una operación segura y guiada; el paisaje y el río son excepcionales.",
            "La ficha de Google Maps usa un centroide inútil a 9,-3.5; se mantiene Kakpin, puerta sur auditada, y se exige confirmar acceso con OIPR. Nunca improvisar entrada por Kafolo.",
            "Únicamente en estación seca, de día y con confirmación reciente del gestor y de seguridad.",
            "Descartarlo ante cualquier duda de seguridad, sin guía, con cierre o con pistas mojadas; el perro no entra.",
            "UNESCO · Parque Nacional de la Comoé",
            "https://whc.unesco.org/en/list/227/",
            [
                commons("Comoe savannah.jpg", "ETF89 · CC BY-SA 4.0", "Sabana del Parque Nacional de la Comoé."),
                commons("Comoe river.jpg", "ETF89 · CC BY-SA 4.0", "Río Comoé y bosque de galería dentro del parque."),
                commons("Kob de Buffon, mâles, Kobus kob (Erxleben,1777) du Parc National de la Comoé (Nord-Est de la Côte d'Ivoire).jpg", "Saxette · CC BY-SA 4.0", "Kobs de Buffon fotografiados en el parque."),
            ],
        ),
        20: entry(
            "Korhogo es la principal base senufo para conocer tejido, talla, manteca de karité y patrimonio regional. La visita se centra en el museo y talleres acordados, no en espectáculos improvisados.",
            "Es la escala cultural más rica del norte y permite comprar artesanía directamente a quienes la producen.",
            "El pin se corrige al Musée Régional Péléforo Gbon Coulibaly de Korhogo en Google Maps. Confirmar apertura y pedir en el museo o Turismo un taller visitable con consentimiento.",
            "Mañana de día laborable; reservar medio día o una noche.",
            "Omitir talleres si no hay acuerdo previo o si se presiona para fotografiar rituales; reducir a escala logística con museo cerrado.",
            "Côte d'Ivoire Tourisme · Korhogo",
            "https://www.visitcotedivoire.com/",
            [
                commons("The sisterhood preparing shea butter in Korhogo, Ivory Coast.jpg", "Gwendoline Créno · CC BY-SA 4.0", "Trabajo colectivo de manteca de karité en Korhogo."),
                commons("COLLECTIE TROPENMUSEUM Een houtsnijder bezig met het vervaardigen van een sculptuur met op de achtergrond twee beelden TMnr 20012842.jpg", "Tropenmuseum/SNV · CC BY-SA 3.0", "Tallador trabajando una escultura en Korhogo."),
                commons("Légende de statue devant le Musée Régional de Korhogo.jpg", "Aristidek5maya · CC BY-SA 4.0", "Elemento interpretativo ante el Museo Regional de Korhogo."),
            ],
            name="Korhogo · museo y artesanía senufo",
            coords=(9.4559375, -5.6273125),
        ),
    },
}


REMOVE: dict[str, set[int]] = {
    "guinea": {1, 2, 6, 7, 13, 15, 17, 18, 19, 20},
    "sierra-leona": {1, 5, 7, 11, 12, 15, 16, 17, 18},
    "liberia": {1, 6, 7, 8, 11, 12, 14, 16, 17},
    "costa-de-marfil": {2, 4, 7, 10, 12, 18, 19, 21, 22},
}


FICHA_META = {
    "guinea": {
        "hero_img": DATA["guinea"][3]["photos"][0]["img"],
        "hero_credit": "Dama de Mali, monte Loura · Fatoumata D · CC BY-SA 4.0",
        "poi_chip": "10 puntos auditados con galería exacta, enlace útil y coordenadas contrastadas",
    },
    "sierra-leona": {
        "hero_img": DATA["sierra-leona"][2]["photos"][0]["img"],
        "hero_credit": "Freetown y su estuario · David Hond · CC BY 2.0",
        "poi_chip": "11 puntos auditados entre la península, las islas, la selva y el norte",
    },
    "liberia": {
        "hero_img": DATA["liberia"][2]["photos"][0]["img"],
        "hero_credit": "Playa de Robertsport · Bethel Anthony Chisom · CC BY-SA 4.0",
        "poi_chip": "8 puntos auditados para valorar la variante si se resuelve el visado terrestre",
    },
    "costa-de-marfil": {
        "hero_img": DATA["costa-de-marfil"][1]["photos"][0]["img"],
        "hero_credit": "Reserva Natural Integral del monte Nimba · Jojoy99 · CC BY-SA 4.0",
        "poi_chip": "13 puntos auditados y seleccionados entre los dos corredores",
    },
}


def clean_stale_photo_notes(value):
    """Retira avisos heredados que afirmaban que las fotos eran genéricas."""
    if isinstance(value, str):
        value = value.replace(
            "Última revisión de esta versión: 12 de septiembre de 2026.",
            "Última revisión de esta versión: 15 de septiembre de 2026.",
        )
        return re.sub(
            r'<tr ><td>Fotos pendientes de sustituir</td><td>.*?</td></tr>',
            "",
            value,
            flags=re.DOTALL,
        )
    if isinstance(value, list):
        return [clean_stale_photo_notes(item) for item in value]
    if isinstance(value, dict):
        return {key: clean_stale_photo_notes(item) for key, item in value.items()}
    return value


def apply_country(country: str) -> None:
    path = ROOT / "content" / "pois" / f"{country}.json"
    pois = json.loads(path.read_text(encoding="utf-8"))
    removed = REMOVE[country]
    pois = [poi for poi in pois if poi["n"] not in removed]
    updates = DATA[country]
    expected = {poi["n"] for poi in pois}
    if set(updates) != expected:
        raise ValueError(
            f"{country}: cobertura incompleta; faltan={sorted(expected-set(updates))}; "
            f"sobran={sorted(set(updates)-expected)}"
        )
    for poi in pois:
        old_desc = poi["desc"]
        update = updates[poi["n"]]
        if update["visit"]["see"] is None:
            update["visit"]["see"] = old_desc
        for key in ("name", "lat", "lon", "desc", "visit", "links", "photos"):
            if key in update:
                poi[key] = update[key]
        primary = poi["photos"][0]
        poi["img"] = primary["img"]
        poi["source"] = primary["source"]
        poi["credit"] = primary["credit"]
    path.write_text(json.dumps(pois, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def apply_ficha(country: str) -> None:
    path = ROOT / "content" / "ficha" / f"{country}.json"
    ficha = json.loads(path.read_text(encoding="utf-8"))
    ficha = clean_stale_photo_notes(ficha)
    meta = FICHA_META[country]
    ficha["hero_img"] = meta["hero_img"]
    ficha["hero_credit"] = meta["hero_credit"]
    for chip in ficha.get("chips", []):
        if isinstance(chip, list) and chip and chip[0] == "PDIs":
            chip[1] = meta["poi_chip"]
    ficha["revision"] = "15 sep 2026"
    ficha["verificado"] = True
    path.write_text(json.dumps(ficha, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    for country in DATA:
        apply_country(country)
        apply_ficha(country)


if __name__ == "__main__":
    main()

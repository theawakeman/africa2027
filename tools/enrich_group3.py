#!/usr/bin/env python3
"""Auditoría retroactiva de PDIs del grupo 3: Ghana, Togo, Benín y Nigeria.

La tarjeta conserva un resumen breve; el modal recibe criterios de decisión,
acceso real, momento, descarte, un enlace específico y tres fotos identificadas.
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


def entry(desc, why, access, when, skip, label, url, photos, *, name=None, coords=None, see=None):
    value = {
        "desc": desc,
        "visit": {"why": why, "see": see, "access": access, "when": when, "skip": skip},
        "links": [{"label": label, "url": url}],
        "photos": photos,
    }
    if name is not None:
        value["name"] = name
    if coords is not None:
        value["lat"], value["lon"] = coords
    return value


DATA: dict[str, dict[int, dict]] = {
    "ghana": {
        1: entry(
            "Nzulezu es una aldea sobre pilotes en el lago Tadane. La visita depende de una canoa oficial desde Beyin y muestra un asentamiento vivo, no un decorado.",
            "Es uno de los paisajes culturales más singulares de Ghana y permite entender la vida ligada al humedal.",
            "El pin cae en Nzulezu, no en el embarcadero. Comprar la visita en el centro de Beyin, confirmar nivel del agua, chalecos, precio y permiso para perro antes de embarcar.",
            "Primera hora y estación con canal navegable; reservar entre tres y cuatro horas.",
            "Omitir con tormenta, canoa sin chalecos, retorno incierto o rechazo del perro; pedir permiso antes de fotografiar residentes.",
            "Ghana Tourism Authority · Nzulezu",
            "https://visitghana.com/attractions/nzulezu-stilt-village/",
            [
                commons("Nzulezo, Ghana.jpg", "Pambelle12 · CC BY-SA 4.0", "Viviendas y pasarela de madera de Nzulezu."),
                commons("Nzulenzu Village in Ghana.jpg", "Enock Manoba · CC BY-SA 4.0", "Canoa junto al asentamiento lacustre."),
                commons("Nzulezo village 5.jpg", "KwesiRaul · CC BY-SA 4.0", "Casas sobre pilotes vistas desde el agua."),
            ],
        ),
        2: entry(
            "Cape Three Points combina el extremo meridional de Ghana con un faro histórico y costa selvática. La pista final y la visita al faro deben confirmarse localmente.",
            "Ofrece una costa remota y un hito geográfico muy distinto de las playas urbanizadas.",
            "El pin marca el faro. Preguntar en el pueblo por pista, aparcamiento y acceso; no asumir que el interior o la linterna estén abiertos.",
            "Estación seca, llegada de día y margen para regresar antes del anochecer.",
            "Descartarlo con pista embarrada, oleaje fuerte, faro cerrado si ese es el objetivo o poca autonomía.",
            "Ghana Tourism Authority · región occidental",
            "https://visitghana.com/western-region/",
            [
                commons("Cape Three Points Lighthouse 1875.jpg", "Friedmut Abel · CC BY-SA 4.0", "Faro de Cape Three Points."),
                commons("DSC01739 (15318781703).jpg", "Tini Maier · CC BY 2.0", "Costa y vegetación de Cape Three Points."),
                commons("DSC01774 (15938288632).jpg", "Tini Maier · CC BY 2.0", "Playa del cabo vista desde el sendero."),
            ],
        ),
        3: entry(
            "Busua es una bahía pesquera y de surf con arena amplia y servicios sencillos. Funciona como descanso entre Cape Three Points y los castillos de la costa.",
            "Es una de las mejores bases costeras del oeste sin exigir una excursión organizada.",
            "El pin está en la playa de Busua. Elegir alojamiento con aparcamiento, preguntar por corrientes y no dejar el vehículo aislado en la arena.",
            "Entre semana, mañana o última tarde; una noche permite disfrutarla sin prisas.",
            "Omitir el baño con bandera, corriente fuerte o sin vigilancia; reducir a parada breve con mal tiempo.",
            "Ghana Tourism Authority · playas del oeste",
            "https://visitghana.com/western-region/",
            [
                commons("Busua Beach Western Region.jpg", "aripeskoe2 · CC BY 2.0", "Bahía y pueblo pesquero de Busua."),
                commons("Busua Beach on rainy day 04.jpg", "Tom Lubbe · CC BY-SA 3.0", "Busua en un día de lluvia."),
                commons("Alaska Beach Resort - Busua - Ghana (4734840567).jpg", "Adam Jones · CC BY-SA 2.0", "Arena y palmeras de la costa de Busua."),
            ],
        ),
        4: entry(
            "El castillo de Elmina, fundado por Portugal en 1482, fue centro del comercio de oro y después de la trata atlántica. La visita guiada recorre patios y mazmorras.",
            "Es una pieza esencial para comprender la costa atlántica y el sistema de fuertes europeo-africanos.",
            "El pin coincide con la entrada del castillo. Usar estacionamiento formal, comprobar horario y reservar guía; el perro no entra en interiores.",
            "A primera hora, antes de calor y grupos; dos o tres horas con el puerto.",
            "No reducirlo a una foto exterior si se busca contexto; omitir interiores si no se resuelve el cuidado seguro del perro.",
            "UNESCO · fuertes y castillos de Ghana",
            "https://whc.unesco.org/en/list/34/",
            [
                commons("Elmina Castle - Ghana.jpg", "Damien Halleux Radermecker · CC BY-SA 2.0", "Castillo de Elmina junto al puerto."),
                commons("Elmina Castle Ramparts (3587901478).jpg", "Francisco Anzola · CC BY 2.0", "Rampas y patios interiores del castillo."),
                commons("Castle, Elmina (P1100192).jpg", "Matti Blume · CC BY-SA 4.0", "Murallas blancas de São Jorge da Mina."),
            ],
        ),
        5: entry(
            "Cape Coast Castle fue sede británica en la Costa del Oro y uno de los principales lugares de embarque de personas esclavizadas. Conserva mazmorras y museo.",
            "La museografía y la visita guiada complementan Elmina sin repetir exactamente su historia.",
            "El pin cae en la entrada del castillo. Confirmar horario, aparcar en zona autorizada y prever custodia del perro fuera del monumento.",
            "Primera hora o final de tarde; dos horas como mínimo.",
            "Omitir si no se puede hacer la visita con respeto o resolver al perro; evitar horas punta si ya se visitó Elmina el mismo día.",
            "UNESCO · fuertes y castillos de Ghana",
            "https://whc.unesco.org/en/list/34/",
            [
                commons("Castle, Cape Coast (P1100223).jpg", "Matti Blume · CC BY-SA 4.0", "Fachada marítima de Cape Coast Castle."),
                commons("Castle, Cape Coast (P1100221).jpg", "Matti Blume · CC BY-SA 4.0", "Patio interior del castillo."),
                commons("Entrance of Cape Coast Castle.jpg", "Afus199620 · CC0", "Entrada pública de Cape Coast Castle."),
            ],
        ),
        6: entry(
            "Kakum protege bosque tropical y ofrece una pasarela elevada entre las copas. La experiencia es turística y guiada; no garantiza fauna visible.",
            "Permite leer el dosel desde arriba y rompe con la sucesión de visitas históricas de la costa.",
            "El pin coincide con el centro de visitantes. Llegar temprano, confirmar apertura de la pasarela y dejar al perro fuera del parque con cuidado seguro.",
            "Al abrir, en día seco y con poca gente; medio día.",
            "Omitir con tormenta, viento fuerte, vértigo incapacitante o sin solución para el perro.",
            "Ghana Tourism Authority · Kakum",
            "https://visitghana.com/attractions/kakum-national-park/",
            [
                commons("Kakum National Park, Jukwa (P1100159-Pano).jpg", "Matti Blume · CC BY-SA 4.0", "Pasarela de dosel en Kakum."),
                commons("Rocky terrace.jpg", "Kobebigs · CC BY-SA 4.0", "Sendero y vegetación del parque."),
                commons("KakumNationalPark forestPath3.jpg", "Kobina ebo · CC BY-SA 3.0", "Camino dentro del bosque de Kakum."),
            ],
        ),
        7: entry(
            "Accra concentra Jamestown, Independence Square, museos, talleres y gestiones. Es una base urbana para recorrer por zonas, no un PDI de una sola puerta.",
            "Aúna historia ga, memoria de la independencia y todos los servicios complejos del país.",
            "El pin se mantiene como ancla urbana. Reservar alojamiento con aparcamiento, moverse de día y comprobar accesos concretos; no fotografiar instalaciones oficiales sin permiso.",
            "Días laborables para gestiones y primera hora para Jamestown; una o dos noches.",
            "Reducir visitas con tráfico extremo, actos oficiales o falta de estacionamiento seguro.",
            "Ghana Tourism Authority · Greater Accra",
            "https://visitghana.com/greater-accra-region/",
            [
                commons("Jamestown Lighthouse 20170122.jpg", "Gereon K. · CC BY-SA 4.0", "Faro de Jamestown en Accra."),
                commons("Jamestown View from Lighthouse 2011 B003.jpg", "Mike Norton · CC BY 2.0", "Jamestown visto desde el faro."),
                commons("Jamestown Lighthouse, Accra (P1100267).jpg", "Matti Blume · CC BY-SA 4.0", "Faro y tejido urbano de Jamestown."),
            ],
        ),
        8: entry(
            "El parque memorial de Kwame Nkrumah reúne el mausoleo, una exposición y el lugar de la proclamación de independencia. Es la visita histórica más clara de Accra.",
            "Explica el nacimiento de Ghana, el panafricanismo y las contradicciones del gobierno de Nkrumah.",
            "El pin coincide con la entrada del parque renovado. Consultar horario y norma de acceso con perro; prever custodia para el museo interior.",
            "Mañana de día laborable; entre una y dos horas.",
            "Omitir interiores si está cerrado o no hay cuidado del perro, pero no sustituir la visita por una foto exterior sin contexto.",
            "Ghana Tourism Authority · memorial de Nkrumah",
            "https://visitghana.com/kwame-nkrumah-memorial-park/",
            [
                commons("Kwame Nkrumah Memorial Park & Mausoleum.jpg", "Fquasie · CC BY-SA 4.0", "Mausoleo de Kwame Nkrumah."),
                commons("OSAGYEFO DR. KWAME NKRUMAH Grave at Kwame Nkrumah mausoleum.jpg", "Maame1Yaa · CC BY 4.0", "Sepultura dentro del memorial."),
                commons("Kwame Nkrumah Monument at the Kwame Nkrumah Mausoleum and Memorial Park, Accra 01.jpg", "Nkansahrexford · CC BY-SA 4.0", "Monumento a Nkrumah en el parque."),
            ],
        ),
        9: entry(
            "Shai Hills combina sabana, afloramientos rocosos y patrimonio shai cerca de Accra. Los recorridos se hacen con el personal de la reserva.",
            "Es la salida natural más accesible desde la capital y ofrece paisaje y fauna sin llegar a Mole.",
            "El pin marca la reserva; entrar por la puerta operativa que confirme el gestor. Contratar guía y dejar al perro fuera del área protegida.",
            "Al amanecer o última tarde, en día seco; de dos horas a medio día.",
            "Omitir con calor extremo, incendio, cierre o sin custodia segura para el perro.",
            "Ghana Tourism Authority · Shai Hills",
            "https://visitghana.com/greater-accra-region/",
            [
                commons("Shai Hills, Shai-Osudoku (P1100035).jpg", "Matti Blume · CC BY-SA 4.0", "Sabana y roca en Shai Hills."),
                commons("Shai Hills, Shai-Osudoku (P1100078).jpg", "Matti Blume · CC BY-SA 4.0", "Afloramiento rocoso de la reserva."),
                commons("Shai Hills, Shai-Osudoku (P1100104).jpg", "Matti Blume · CC BY-SA 4.0", "Fauna visible en el paisaje de Shai Hills."),
            ],
        ),
        10: entry(
            "La presa de Akosombo contiene el lago Volta y es una pieza decisiva de la industrialización de Ghana. La visita debe hacerse desde un mirador o tour autorizado.",
            "Ayuda a entender energía, aluminio, desplazamientos humanos y la escala artificial del lago Volta.",
            "El pin corresponde a la presa. No detenerse ni fotografiar desde zonas de seguridad; solicitar visita autorizada o usar el mirador indicado localmente.",
            "Día laborable y con confirmación previa; una o dos horas.",
            "Omitir si no hay acceso autorizado, controles reforzados o el desvío compromete la etapa.",
            "Ghana Tourism Authority · Eastern Region",
            "https://visitghana.com/eastern-region/",
            [
                commons("Akosombo dam.jpg", "Stig Nygaard · CC BY 2.0", "Presa de Akosombo y lago Volta."),
                commons("Akosombo dam ghana.jpg", "Edward Kamau · CC BY-SA 3.0", "Estructura de la presa desde aguas abajo."),
                commons("Akosombo Dam from the Volta Hotel.JPG", "SandisterTei · CC BY-SA 3.0", "Vista autorizada de Akosombo desde Volta Hotel."),
            ],
        ),
        11: entry(
            "Ada Foah ocupa la desembocadura del Volta entre estuario, islas arenosas y Atlántico. La experiencia depende de marea, mar y barca contratada.",
            "Es el mejor paisaje de estuario de la costa oriental y una pausa antes de Togo.",
            "El pin se mantiene en Ada Foah, no en un embarcadero concreto. Pactar punto, chalecos, ruta y regreso; preguntar por corrientes antes de bañarse.",
            "Mañana, mar tranquilo y luz suficiente para regresar; medio día o una noche.",
            "Descartarlo con oleaje, tormenta, barco sin chalecos o alojamiento sin aparcamiento seguro.",
            "Ghana Tourism Authority · Ada Foah",
            "https://visitghana.com/ada-foah-tourism/",
            [
                commons("Ada Foah Beach 2.jpg", "Philip Nalangan · CC BY 4.0", "Arena y oleaje en Ada Foah."),
                commons("Ada Foah Beach 1.jpg", "Philip Nalangan · CC BY 4.0", "Litoral de Ada Foah."),
                commons("Ada Resort close to Volta Estuary.jpg", "Rberchie · CC BY-SA 4.0", "Paisaje junto al estuario del Volta."),
            ],
        ),
        12: entry(
            "Tafi Atome es un santuario comunitario donde monos mona viven alrededor del bosque sagrado. La visita debe ser guiada y sin alimentar por cuenta propia.",
            "Conecta conservación comunitaria, tradición local y observación cercana de primates.",
            "El pin coincide con el santuario. Confirmar horario y guía; el perro no debe entrar ni acercarse a los monos.",
            "Primera hora, cuando hay actividad y menos calor; una o dos horas.",
            "Omitir sin custodia para el perro, con guía que fomente contacto inseguro o si el recinto está cerrado.",
            "Ghana Tourism Authority · Volta Region",
            "https://visitghana.com/volta-region/",
            [
                commons("A monkey on top of a tree at the Tafi Atome Monkey Sanctuary in the Volta Region of Ghana.jpg", "Treysam · CC BY-SA 4.0", "Mono mona en Tafi Atome."),
                commons("Tafi Atome Monkey Sanctuary 6.jpg", "Selorm18 · CC BY-SA 3.0", "Bosque del santuario comunitario."),
                commons("Sunset at tafi atome monkey sanctuary.jpg", "Jones Anlimah · CC BY-SA 4.0", "Atardecer en Tafi Atome."),
            ],
        ),
        13: entry(
            "Amedzofe es una localidad de montaña al pie del Gemi, con vistas del altiplano y una subida corta hasta la cruz de la cumbre.",
            "Ofrece clima fresco, paisaje habitado y una caminata más breve que Afadja.",
            "El pin se corrige a la referencia del monte Gemi. Preguntar en el pueblo por guía, sendero y aparcamiento; no seguir atajos entre cultivos.",
            "Amanecer o última tarde despejada; de dos a tres horas.",
            "Omitir con niebla, tormenta, roca mojada o si no se confirma el acceso final.",
            "Ghana Tourism Authority · Amedzofe",
            "https://visitghana.com/amedzofe-village/",
            [
                commons("Amedzofe village Ghana.jpg", "Williams Penuku · CC BY-SA 4.0", "Amedzofe en el relieve de Volta."),
                commons("Amedzofe Town Facing the mountain Gemi.jpg", "Amuzujoe · CC BY-SA 4.0", "El pueblo frente al monte Gemi."),
                commons("Gemi Mountain (German Evangelical Mission) at Amedzofe in the Volta Region of Ghana.jpg", "Amuzujoe · CC BY-SA 4.0", "Cruz y cumbre del monte Gemi."),
            ],
        ),
        14: entry(
            "Wli es la cascada más alta de Ghana por caída total, en el borde de la cordillera de Togo. El sendero inferior es la opción razonable; el circuito superior es exigente.",
            "La gran pared y el bosque lleno de murciélagos frugívoros justifican el desvío incluso sin hacer la ruta larga.",
            "El pin cae en Wli Agumatsa Falls. Registrarse en el centro, contratar guía cuando sea obligatorio y confirmar la política del perro.",
            "Mañana y firme seco; dos horas para la inferior o medio día largo para la superior.",
            "Omitir la ruta alta con lluvia, calor fuerte o forma insuficiente; no entrar bajo la caída con crecida.",
            "Ghana Tourism Authority · Volta Region",
            "https://visitghana.com/volta-region/",
            [
                commons("Wli Agumatse Waterfall aerial view.jpg", "Cornelius Agordome · CC BY-SA 4.0", "Caída completa de Wli desde el aire."),
                commons("Wli Agumatse Waterfall (Close view).jpg", "Cornelius Agordome · CC BY-SA 4.0", "Vista cercana de Wli Agumatsa."),
                commons("Wli waterfall hike.jpg", "Stig Nygaard · CC BY 2.0", "Sendero de acceso a la cascada."),
            ],
        ),
        15: entry(
            "Afadja es una subida corta pero muy empinada desde Liati Wote, con vistas de la cordillera fronteriza. No es un paseo pese a su distancia reducida.",
            "Es la ascensión emblemática de Ghana y permite comparar el relieve con Gemi y Wli.",
            "El pin coincide con la referencia de Afadjato. Registrarse en Liati Wote, tomar guía local y dejar claro el punto de inicio y retorno.",
            "Salida muy temprana y terreno seco; reservar de tres a cuatro horas.",
            "Omitir con tormenta, barro, calor extremo o rodillas comprometidas; llevar agua y no contar con fuentes en ruta.",
            "Ghana Tourism Authority · Volta Region",
            "https://visitghana.com/volta-region/",
            [
                commons("Mount Afadja(Mt Afadjato or “Avedzeto.”).jpg", "Ace Shogun · CC BY-SA 4.0", "Relieve del monte Afadja."),
                commons("Mount Afadja Signboard 01.jpg", "Amuzujoe · CC BY-SA 4.0", "Señal del acceso a Afadja."),
                commons("Beautiful Landscape view on the Afadjato Mountain with vegetation1.jpg", "Treysam · CC BY-SA 4.0", "Vista de la montaña y su vegetación."),
            ],
        ),
        16: entry(
            "Boti forma un doble salto en el bosque de Yilo Krobo; en temporada seca puede perder mucho caudal. El recinto incluye escalones y otros hitos turísticos.",
            "Es una cascada accesible desde Accra y Akosombo, especialmente atractiva con caudal medio.",
            "El pin coincide con Boti Falls. Confirmar caudal, horario y estado de escaleras; no asumir que el baño sea seguro.",
            "Tras lluvias moderadas y a primera hora; de dos a tres horas.",
            "Omitir en estiaje extremo, con tormenta, escalones resbaladizos o aforo alto.",
            "Ghana Tourism Authority · Boti Falls",
            "https://visitghana.com/attractions/boti-falls/",
            [
                commons("BOTI FALLS at its best.jpg", "Ananyaelixir · CC BY-SA 3.0", "Los dos saltos de Boti con caudal."),
                commons("Boti Falls and environs 04.jpg", "Nkansahrexford · CC BY-SA 4.0", "Entorno forestal de Boti Falls."),
                commons("Boti Water Falls.jpg", "Brans Wyte GH · CC BY-SA 4.0", "Vista frontal de la cascada."),
            ],
        ),
        17: entry(
            "Kumasi es la capital cultural asante: Manhyia aporta contexto histórico y Kejetia muestra la intensidad comercial actual. Conviene dividir la visita por zonas.",
            "Es el lugar principal para comprender el poder asante vivo, no solo su pasado colonial.",
            "El pin se mantiene como ancla urbana. Priorizar Manhyia con horario confirmado; visitar Kejetia con guía, sin joyas visibles y sin dejar el coche en la calle.",
            "Día laborable, museo por la mañana y mercado con luz; una noche como mínimo.",
            "Reducir el mercado con aglomeración, protesta o estacionamiento inseguro; no fotografiar personas sin permiso.",
            "Ghana Tourism Authority · Manhyia Palace Museum",
            "https://visitghana.com/manhyia-palace-museum-2/",
            [
                commons("Manhyia Palace Museum.jpg", "Nkansahrexford · CC BY-SA 3.0", "Edificio del museo del palacio Manhyia."),
                commons("Modern market hall of Kejetia market.jpg", "Afus199620 · CC0", "Gran nave moderna del mercado de Kejetia."),
                commons("Market Women - Kejetia Market - Kumasi - Ghana (4755543337).jpg", "Adam Jones · CC BY-SA 2.0", "Actividad comercial en Kejetia."),
            ],
        ),
        18: entry(
            "El santuario de Besease es uno de los edificios tradicionales asante inscritos por UNESCO. Su arquitectura de tierra y madera exige visita comunitaria respetuosa.",
            "Es el complemento material de Manhyia y uno de los pocos santuarios tradicionales conservados cerca de Kumasi.",
            "El pin coincide con Besease Traditional Shrine. Buscar al custodio, acordar visita y no entrar ni fotografiar rituales sin permiso.",
            "Mañana de día laborable y tiempo seco; alrededor de una hora.",
            "Omitir si no aparece el custodio, hay ceremonia privada o la comunidad pide no entrar; el perro queda fuera.",
            "UNESCO · edificios tradicionales asante",
            "https://whc.unesco.org/en/list/35/",
            [
                commons("Besease Traditional Shrine (Ejisu, Ghana 2019).jpg", "Sucram Yef · CC BY 2.0", "Santuario tradicional de Besease."),
                commons("Ejisu Bebease Shrine 1.jpg", "Joy Agyepong · CC BY-SA 4.0", "Patio y decoración del santuario."),
                commons("Besease Shrine (5).jpg", "Noahalorwu · CC BY-SA 4.0", "Arquitectura de tierra y madera de Besease."),
            ],
        ),
        20: entry(
            "Mole es la principal reserva de sabana de Ghana, con safaris guiados y observación frecuente de elefantes. La fauna nunca está garantizada.",
            "Es el PDI de naturaleza más completo del país y justifica el largo desvío al norte.",
            "El pin se ajusta al área de visitantes y oficina, no al centroide del parque. Reservar alojamiento y safari; el perro no entra en vehículos ni senderos del parque.",
            "Estación seca, safari al amanecer y al menos dos noches por la distancia.",
            "Omitir sin reserva, con alerta regional o sin custodia fiable para el perro; no bajar del vehículo fuera de indicación del guía.",
            "Ghana Tourism Authority · Mole National Park",
            "https://visitghana.com/mole-national-park/",
            [
                commons("Mole Ghana 2.jpg", "Lalambala · CC BY-SA 4.0", "Elefantes en una charca de Mole."),
                commons("Mole National Park Ghana.jpg", "Stig Nygaard · CC BY 2.0", "Sabana y elefante en Mole."),
                commons("Rich Fauna Ghana.jpg", "Dieu-Donné Gameli · CC BY-SA 3.0", "Fauna observada dentro del parque."),
            ],
            coords=(9.26227, -1.85339),
        ),
        21: entry(
            "La mezquita de Larabanga es un edificio de tierra de tradición sudanesa, mantenido por la comunidad junto a Mole. El interior no es una atracción abierta sin más.",
            "Añade patrimonio islámico y arquitectura viva a una etapa dominada por la fauna.",
            "El pin coincide con la mezquita. Buscar guía o custodio, acordar donación y pedir permiso para fotografiar; visitantes no musulmanes pueden quedar fuera.",
            "Mañana o tarde, fuera de la oración del viernes.",
            "Omitir durante culto o si no hay consentimiento; perro siempre fuera del recinto.",
            "Ghana Tourism Authority · mezquita de Larabanga",
            "https://visitghana.com/larabanga-mosque/",
            [
                commons("Larabanga Mosque Ghana.jpg", "Sathyan Velumani · CC BY-SA 3.0", "Fachada de tierra de la mezquita de Larabanga."),
                commons("Larabanga Mosque Best View.jpg", "Dieu-Donné Gameli · CC BY-SA 3.0", "Contrafuertes y torres de Larabanga."),
                commons("Larabanga Mosque 0.jpg", "Amuzujoe · CC BY-SA 4.0", "Vista lateral del edificio mantenido por la comunidad."),
            ],
        ),
        22: entry(
            "El estanque sagrado de Paga alberga cocodrilos del Nilo habituados a la presencia humana. La visita es cultural, pero los animales siguen siendo salvajes.",
            "Es una tradición comunitaria singular en la frontera con Burkina Faso, no un zoológico convencional.",
            "El pin coincide con Paga Crocodile Pond. Entrar solo con guía autorizado, mantener distancia y rechazar poses o contacto que parezcan inseguros; dejar al perro lejos.",
            "De día, con calor moderado y situación de seguridad del extremo norte confirmada.",
            "Omitir con alerta regional, guía informal, presión para tocar al animal o sin custodia para el perro.",
            "Ghana Tourism Authority · Upper East Region",
            "https://visitghana.com/upper-east-region/",
            [
                commons("Paga crocodile pond Julu 2024.jpg", "Knowledge and philosophy · CC BY-SA 4.0", "Cocodrilo en el estanque sagrado de Paga."),
                commons("Friendly Paga Crocodile I.jpg", "Dieu-Donné Gameli · CC BY-SA 3.0", "Encuentro guiado documentado en Paga; no imitar sin control."),
                commons("Paga Crocodile Pond 3.jpg", "Dieu-Donné Gameli · CC BY-SA 3.0", "Orilla del estanque y uno de sus cocodrilos."),
            ],
        ),
    },
    "togo": {
        1: entry(
            "Lomé combina Grand Marché, catedral, paseo marítimo y patrimonio colonial. Es también la gran base de servicios del país y se recorre por zonas.",
            "Permite entender la capital comercial y resolver gestiones antes de los corredores costero e interior.",
            "El pin se mantiene como ancla urbana. Reservar estacionamiento vigilado, evitar fotografiar controles y visitar el mercado con guía si se lleva equipo visible.",
            "Día laborable y primera hora; una noche para no encadenar ciudad y frontera.",
            "Reducir el recorrido con protesta, tráfico extremo o sin aparcamiento seguro.",
            "Togo Tourisme · Lomé",
            "https://togotourisme.tg/destinations/lome/",
            [
                commons("Lomé Grand Marché with the Cathédrale du Sacré Coeur (33592985581).jpg", "Dan Sloan · CC BY-SA 2.0", "Grand Marché y catedral del Sagrado Corazón."),
                commons("Lomé grand market.jpg", "Ognakossan · CC BY-SA 4.0", "Actividad en el Grand Marché de Lomé."),
                commons("Cathédrale du Sacré-Cœur de Lomé 3.jpg", "Edison McCullen · CC BY 4.0", "Fachada de la catedral de Lomé."),
            ],
        ),
        2: entry(
            "Akodesséwa es un mercado de objetos rituales y materia animal asociado a prácticas vodun. Requiere mediación y no debe tratarse como espectáculo exótico.",
            "Aporta contexto sobre medicina y religión tradicionales, siempre que la visita sea explicada por alguien del lugar.",
            "El pin coincide con el mercado. Acordar guía, precio y permiso fotográfico antes de sacar la cámara; no comprar productos de fauna protegida.",
            "Mañana y con tiempo para conversar; alrededor de una hora.",
            "Omitir con presión comercial, fotografía no consentida o si incomoda la presencia de restos animales; perro fuera.",
            "Togo Tourisme · recorridos culturales",
            "https://togotourisme.tg/types-de-voyages-une-multitude-de-possibilites-2/",
            [
                commons("In the Akodessewa Fetish Market (33632321458).jpg", "Francisco Anzola · CC BY 2.0", "Puesto documentado del mercado de Akodesséwa."),
                commons("Skulls at Akodessawa Fetish Market 2016.jpg", "Alexander Sarlay · CC BY-SA 4.0", "Restos animales ofrecidos en el mercado."),
                commons("Akodessawa Fetish Market 2005.jpg", "Alexander Sarlay · CC BY-SA 4.0", "Vista del mercado en 2005."),
            ],
        ),
        3: entry(
            "El antiguo palacio de los gobernadores, construido en 1905, es desde 2019 un centro de arte y cultura con exposiciones y jardines frente al mar.",
            "Es la mejor recuperación arquitectónica de Lomé y permite leer la etapa alemana y los usos posteriores del edificio.",
            "El pin coincide con Palais de Lomé. Consultar exposiciones, horario y entradas; confirmar si el jardín admite perro y asumir que las salas no.",
            "Día de apertura, preferentemente por la mañana; dos horas.",
            "Omitir interiores con cierre o sin custodia para el perro; no prometer una exposición concreta sin revisar programa.",
            "Togo Tourisme · Palais de Lomé",
            "https://togotourisme.tg/site/palais-de-lome/",
            [
                commons("Palais de Lomé - elewacja południowa.jpg", "Nero2022 · CC BY-SA 4.0", "Fachada sur del Palais de Lomé."),
                commons("Palais de Lomé.jpg", "Ognakossan · CC BY-SA 4.0", "Palacio restaurado junto al paseo marítimo."),
                commons("Les expositions du Palais de Lomé 16.jpg", "Lome2023 · CC BY-SA 4.0", "Una exposición dentro del centro cultural."),
            ],
        ),
        5: entry(
            "La Maison Wood de Agbodrafo conserva un sótano asociado a la trata clandestina del siglo XIX. La interpretación depende del guía local.",
            "Hace visible una fase posterior a la abolición legal que suele quedar fuera de los grandes castillos de Ghana.",
            "El pin coincide con Maison des Esclaves. Confirmar apertura y guía; el espacio es pequeño, sensible y no adecuado para perro.",
            "Mañana o primera tarde; una hora, combinable con el lago Togo.",
            "Omitir si no hay guía o custodia para el perro; no repetir afirmaciones no documentadas como hechos.",
            "Togo Tourisme · patrimonio de la trata",
            "https://togotourisme.tg/un-patrimoine-historique/",
            [
                commons("Maison des Esclaves d’Agbodrafo 08.jpg", "Beaugardo · CC BY-SA 4.0", "Exterior de la Maison des Esclaves."),
                commons("Maison des Esclaves d’Agbodrafo 16.jpg", "Beaugardo · CC BY-SA 4.0", "Espacio interior de la Maison Wood."),
                commons("Maison des Esclaves d’Agbodrafo 01.jpg", "Beaugardo · CC BY-SA 4.0", "Detalle del edificio histórico de Agbodrafo."),
            ],
        ),
        6: entry(
            "Togoville es una localidad histórica de la orilla norte del lago Togo, ligada al tratado de 1884, a santuarios vodun y a la catedral.",
            "Reúne historia colonial, vida lagunar y religión viva en un lugar compacto.",
            "El pin cae en el centro de Togoville. Se llega por carretera o piragua; si se cruza el lago, pactar chalecos y regreso. Visitar santuarios solo con permiso.",
            "Mañana, con mar y viento tranquilos si se usa piragua; medio día.",
            "Omitir la barca sin chalecos o con tormenta; no fotografiar altares ni rituales sin consentimiento.",
            "Togo Tourisme · Togoville",
            "https://togotourisme.tg/destinations/togoville/",
            [
                commons("Togoville harbour.jpg", "Alexandra Pugachevsky · CC BY-SA 3.0", "Embarcadero de Togoville en el lago."),
                commons("Au marché de Togoville.jpg", "Le bon Sos · CC BY-SA 4.0", "Mercado local de Togoville."),
                commons("Panneau Indicatif du centre ADANU de Togoville.jpg", "Razak23 · CC BY-SA 4.0", "Señal de un centro comunitario de Togoville."),
            ],
        ),
        7: entry(
            "Aného y Glidji forman un paisaje costero y ritual ligado a la historia guin-mina y a la fiesta Epe Ekpe. Fuera del festival sigue siendo una visita cultural.",
            "Es la escala con más contexto histórico y religioso antes de la frontera de Hillacondji.",
            "El pin se mantiene en Aného. Contratar guía local para Glidji, confirmar cada recinto y no entrar en ceremonias privadas.",
            "De día; septiembre solo si las fechas y condiciones de Epe Ekpe están confirmadas.",
            "Omitir actos masivos sin plan o cualquier santuario sin permiso; no fotografiar participantes por defecto.",
            "Togo Tourisme · Aného",
            "https://togotourisme.tg/detailsite?slug=aneho&type=ville",
            [
                commons("Retrait du filet avec des poissons.jpg", "Alfrednadjere · CC BY-SA 4.0", "Pescadores retirando una red en Aného."),
                commons("Temple de la divinité Osabu de Glidji.jpg", "Wisdom Mensah de Linitiateur · CC BY-SA 4.0", "Templo de la divinidad Osabu en Glidji."),
                commons("Anèho, Cérémonies rituelles et traditionnelles de Épé-Ekpé, départ de Akléma pour Glidji.jpg", "Wisdom Mensah de Linitiateur · CC BY-SA 4.0", "Ceremonia Epe Ekpe documentada en Aného."),
            ],
        ),
        9: entry(
            "Sarakawa es un parque de fauna cercado al noroeste de Kara, con especies locales y otras introducidas. No debe confundirse con un parque nacional salvaje.",
            "Ofrece una parada de fauna accesible en el eje norte, con expectativas más realistas que una reserva remota.",
            "El pin coincide con el parque. Confirmar horario, vehículo de visita y política de animales; el perro no entra.",
            "A primera hora o última tarde, con seguridad regional confirmada; dos o tres horas.",
            "Omitir con cierre, alerta en Kara o sin custodia para el perro; no salir de rutas indicadas.",
            "Togo Tourisme · Sarakawa",
            "https://togotourisme.tg/tour-item/kara-bassar-sokode-atakpame-2/",
            [
                commons("Piquet PARC SARAKAWA 04.jpg", "Alfrednadjere · CC BY 4.0", "Señal identificativa del parque de Sarakawa."),
                commons("Barrage artificiel de la réserve de faune de Sarakawa au Togo 10.jpg", "Akouete · CC BY-SA 4.0", "Lámina de agua dentro de Sarakawa."),
                commons("La végétation dans le parc animalier de Sarakawa 07.jpg", "Ubkoumbogny · CC BY-SA 4.0", "Sabana arbolada del parque."),
            ],
        ),
        10: entry(
            "Koutammakou es el paisaje cultural vivo de los batammariba, conocido por sus casas-fortaleza de tierra o takienta. UNESCO lo protege a ambos lados de la frontera.",
            "Es el conjunto arquitectónico y cultural más importante de Togo, siempre que se visite con la comunidad.",
            "El pin es una referencia dentro del paisaje, no una taquilla universal. Organizar guía en Kandé o con la comunidad y confirmar seguridad antes de subir al norte.",
            "Estación seca, de día y con una jornada completa.",
            "Descartarlo ante alerta al norte de Kandé, sin guía o permiso; no entrar en casas ni fotografiar personas sin acuerdo.",
            "UNESCO · Koutammakou",
            "https://whc.unesco.org/en/list/1140/",
            [
                commons("Koutammakou.jpg", "Emmanuel effe · CC0", "Takienta dentro del paisaje de Koutammakou."),
                commons("Toit dallé 02.jpg", "Kadi1366 · CC BY-SA 4.0", "Cubierta y espacios domésticos de una takienta."),
                commons("Bâtiments du village.jpg", "Hermannkass · CC BY-SA 4.0", "Conjunto de edificios de tierra batammariba."),
            ],
        ),
        11: entry(
            "La falla de Alédjo es un paso rocoso estrecho atravesado por la RN1 cerca de Bafilo. El interés está en la geología y el paisaje, no en parar sobre la carretera.",
            "Es el punto visual más claro del eje central y no exige una excursión larga.",
            "El pin coincide con la ficha y con fotos georreferenciadas de Google/Commons. Detenerse solo en apartadero seguro, nunca en el túnel o el carril.",
            "Con luz de día y firme seco; parada de veinte a cuarenta minutos.",
            "Omitir con tráfico, niebla, lluvia o sin espacio fuera de la calzada.",
            "Togo Tourisme · itinerario de Alédjo",
            "https://togotourisme.tg/?p=4843",
            [
                commons("Faille d'Alédjo , région de la kara au Togo 03.jpg", "Adewi97 · CC BY-SA 4.0", "Paso rocoso de la falla de Alédjo."),
                commons("Faille d'Alédjo au Nord-Togo (région de la Kara) 20.jpg", "Ametovenak · CC BY-SA 4.0", "Carretera atravesando la falla."),
                commons("Faille d'Alédjo au Togo 17.jpg", "Alfrednadjere · CC BY-SA 4.0", "Paredes de roca junto a la RN1."),
            ],
        ),
        13: entry(
            "Los altos hornos tradicionales de Bassar y Nangbani conservan evidencias de una metalurgia del hierro de larga duración. La visita necesita guía local para localizar estructuras.",
            "Es un patrimonio arqueológico poco habitual que explica tecnología, comercio y paisaje del norte.",
            "El pin se ajusta a Nangbani como pueblo de referencia, no finge marcar un horno concreto. Contactar con Turismo o guía en Bassar antes de desviarse.",
            "Día seco, por la mañana y con medio día disponible.",
            "Omitir sin guía o confirmación de acceso, con alerta regional o si la pista está mojada.",
            "Ministerio de Turismo · hornos de Bassar y Nangbani",
            "https://tourisme.gouv.tg/madame-lambassadrice-jocelyne-caballero-a-visite-les-hauts-fourneaux-de-bassar-et-de-nangbani/",
            [
                external("https://www.republicoftogo.com/var/site/storage/images/toutes-les-rubriques/culture/un-tresor-archeologique/2958285-1-fre-FR/un-tresor-archeologique_i1920.jpg", "https://www.republicoftogo.com/toutes-les-rubriques/culture/un-tresor-archeologique", "République Togolaise · derechos en la fuente", "Estructuras de fundición tradicionales de Bassar."),
                external("https://tourisme.gouv.tg/wp-content/uploads/2021/02/AMBS-BASSAR1.jpeg", "https://tourisme.gouv.tg/madame-lambassadrice-jocelyne-caballero-a-visite-les-hauts-fourneaux-de-bassar-et-de-nangbani/", "Ministerio de Turismo de Togo · derechos en la fuente", "Visita documentada a los hornos de Bassar y Nangbani."),
                external("https://archeologie.culture.gouv.fr/sites/archeologie/files/styles/archeologie_fiche_site_cover/public/upload/images/cover/figure1.jpg?itok=4TKlvFnz", "https://archeologie.culture.gouv.fr/en/ancient-metallurgy-west-africa", "Ministère de la Culture de France · derechos en la fuente", "Horno de reducción de hierro de la región de Bassar."),
            ],
            coords=(9.2668305, 0.7984398),
        ),
        15: entry(
            "Aklowa cae por una pared boscosa cerca de Badou. El acceso final es una caminata guiada exigente y puede rondar cuarenta minutos por trayecto.",
            "Es una de las cascadas más espectaculares de la región de Plateaux y menos urbanizada que Womé.",
            "Google Maps confunde a veces Aklowa con Yikpa; se conserva la coordenada auditada por cartografía y fotos locales. Salir con guía de Badou.",
            "Con caudal moderado, mañana y terreno asentado; medio día largo.",
            "Omitir con lluvia, barro, crecida o sin guía; no contar con cobertura ni agua potable.",
            "Togo Tourisme · cascade d'Aklowa",
            "https://togotourisme.tg/site/cascade-dakloa/",
            [
                commons("Cascade d'Akroa (près de Badou, Togo).jpg", "SebEsteban · CC BY-SA 4.0", "Caída de Aklowa/Akloa cerca de Badou."),
                external("https://togotourisme.tg/wp-content/uploads/2020/09/e86d513b94ccf796ebf14dfb2a9c8c4a01695a9a.jpeg", "https://togotourisme.tg/site/cascade-dakloa/", "Togo Tourisme · derechos en la fuente", "Vista oficial de la cascada de Aklowa."),
                external("https://atop.tg/assets/uploads/2024/07/v-scaled.jpg", "https://atop.tg/la-cascade-daklowa-un-site-exotique-et-apaisant/", "Agence Togolaise de Presse · derechos en la fuente", "Cascada y pared vegetal documentadas por la prensa togolesa."),
            ],
        ),
        16: entry(
            "Kpalimé es la base de la región de Plateaux, con arquitectura colonial, mercado, talleres y acceso a bosques y cascadas. Conviene escoger visitas concretas.",
            "Es el mejor nodo para organizar guías y entender la economía de cacao, café y artesanía.",
            "El pin se mantiene como ancla urbana. Elegir alojamiento con aparcamiento y contratar guía identificado para excursiones; no seguir vendedores improvisados.",
            "Día laborable y al menos una noche si se combina con Womé o Agou.",
            "Reducir a base logística si no se concreta taller, paseo o museo; evitar conducción nocturna de regreso.",
            "Togo Tourisme · Kpalimé",
            "https://togotourisme.tg/destinations/kpalime/",
            [
                commons("Kpalime.jpg", "HpBob · dominio público", "Vista urbana de Kpalimé."),
                commons("Postoffice Agome-Palime (Togo).jpg", "Jakob Spieth · dominio público", "Documento histórico de Agomé-Palimé."),
                commons("Plantes parc missahoe Togo 03.jpg", "Theophile-kk · CC BY-SA 4.0", "Vegetación del entorno de Missahoé."),
            ],
        ),
        17: entry(
            "Womé es una cascada en un anfiteatro verde cerca de Kpalimé, alcanzada por pista y sendero con guía comunitario.",
            "Ofrece una excursión de agua y bosque más corta que Aklowa.",
            "El pin coincide con Cascade de Womé. Registrarse en el pueblo, contratar guía y aparcar donde indiquen; la última pista cambia con las lluvias.",
            "Mañana y caudal moderado; dos o tres horas.",
            "Omitir con tormenta, barro profundo o crecida; no saltar desde roca ni asumir que la poza sea segura.",
            "Togo Tourisme · región de Plateaux",
            "https://togotourisme.tg/destinations/kpalime/",
            [
                commons("Cascade de Womé.jpg", "Archideus · CC BY-SA 4.0", "Caída principal de Womé."),
                commons("Cascade de Womé au togo 49.jpg", "Ubkoumbogny · CC BY-SA 4.0", "Poza y pared rocosa de Womé."),
                commons("Cascade de Womé au togo 01.jpg", "Ubkoumbogny · CC BY-SA 4.0", "Sendero y entorno forestal de la cascada."),
            ],
        ),
        19: entry(
            "El monte Agou es la mayor elevación de Togo y se asciende por rutas que atraviesan aldeas y cultivos. La cumbre tiene instalaciones de comunicaciones.",
            "Es la caminata de montaña más completa del sur y ofrece vistas del mosaico agrícola.",
            "El pin marca la cumbre, no el inicio. Contratar guía en Agou, definir ruta y transporte de retorno y respetar las zonas técnicas.",
            "Salida al amanecer, día seco y jornada completa.",
            "Omitir con niebla, tormenta, calor fuerte, guía no confirmado o poca forma física.",
            "Togo Tourisme · ecoturismo de Agou",
            "https://togotourisme.tg/types-de-voyages-une-multitude-de-possibilites-2/",
            [
                commons("Mont agou.png", "Christophe GUILLOUX · CC BY-SA 3.0", "Relieve del monte Agou."),
                commons("Agou view - 3329598987.jpg", "Jeff Attaway · CC BY 2.0", "Vista desde las laderas de Agou."),
                commons("Agou mist.jpg", "Jeff Attaway · CC BY 2.0", "Niebla sobre el paisaje de Agou."),
            ],
        ),
    },
    "benin": {
        1: entry(
            "La Bouche du Roy es la desembocadura del Mono: manglar, laguna, dunas y Atlántico dentro de una reserva de biosfera. Se visita en barca con guía local.",
            "Es el paisaje natural más completo de la costa beninesa y permite observar el contacto entre río y mar.",
            "El pin marca la desembocadura, no el embarcadero. Organizar la salida en Grand-Popo, confirmar chalecos, duración, marea y regreso antes de embarcar.",
            "Primera hora, mar estable y luz suficiente; el portal oficial calcula dos o tres horas.",
            "Omitir con tormenta, oleaje, barca sin chalecos o rechazo del perro; no prometer tortugas fuera de temporada.",
            "Bénin Tourisme · La Bouche du Roy",
            "https://benintourisme.bj/en/destinations/the-bouche-du-roy/",
            [
                commons("Bouche du Roi in Grand Popo Benin.jpg", "Kulttuurinavigaattori · CC BY-SA 4.0", "Desembocadura del Mono en La Bouche du Roy."),
                commons("Fleuve de la Bouche du Roy à Grand-popo au Bénin.jpg", "EGOUNLETY Eudoxie · CC BY-SA 4.0", "Canal y vegetación de la reserva."),
                commons("Bouche du Roy vue de face.jpg", "BILLA1994 · CC BY-SA 4.0", "Frente de agua entre laguna y Atlántico."),
            ],
        ),
        2: entry(
            "La Ruta de los Cautivos de Ouidah enlaza espacios de memoria hasta la Puerta del No Retorno. Los monumentos actuales interpretan un proceso histórico traumático.",
            "Es el recorrido de memoria más importante de Benín y conecta la ciudad con la costa atlántica.",
            "El pin se mantiene en la Puerta del No Retorno. Recorrer con guía acreditado desde Ouidah y distinguir lugares históricos, tradiciones orales y monumentos recientes.",
            "Primera hora o última tarde; reservar medio día.",
            "No hacerlo como una sucesión de fotos sin explicación; omitir actos o recintos cerrados sin permiso.",
            "Bénin Tourisme · Ruta de los Cautivos",
            "https://benintourisme.bj/en/destinations/the-route-of-the-enslaved/",
            [
                commons("Porte du non-retour au Benin.jpg", "Borisghost · CC0", "Puerta del No Retorno en la costa de Ouidah."),
                commons("Slave route Ouidah Benin.jpg", "jbdodane · CC BY 2.0", "Tramo de la Ruta de los Cautivos."),
                commons("Monument fosse commune de la route des esclaves. Ouidah.jpg", "Eric Emeraux · CC BY-SA 4.0", "Monumento de la fosa común en la ruta."),
            ],
        ),
        3: entry(
            "El Templo de las Pitones y el fuerte portugués permiten leer en Ouidah el vodun vivo y la presencia comercial europea. Son recintos distintos.",
            "La proximidad de ambos lugares muestra historias religiosas y atlánticas que no deben confundirse.",
            "El pin cae en el Templo de las Pitones. Confirmar horarios por separado, pedir permiso fotográfico y no manipular animales; el fuerte puede tener acceso condicionado por obras.",
            "Mañana, fuera de ceremonias y con dos horas para ambos si están abiertos.",
            "Omitir contacto forzado con pitones, visita sin guía o cualquier recinto cerrado; perro fuera.",
            "Bénin Tourisme · Templo de las Pitones",
            "https://benintourisme.bj/en/destinations/the-temple-of-pythons/",
            [
                commons("Entrée du Temple des Pythons (Ouidah).jpg", "Ji-Elle · CC BY-SA 4.0", "Entrada del Templo de las Pitones."),
                commons("Ouidah-Temple des Pythons-Petite case ronde (2).jpg", "Ji-Elle · CC BY-SA 4.0", "Recinto interior del templo."),
                commons("Fort Ouidah Benin.JPG", "Tienstwatrankil · CC BY-SA 3.0", "Antiguo fuerte portugués de Ouidah."),
            ],
        ),
        5: entry(
            "El lago Ahémé es un sistema de agua y pesca entre Possotomé y comunidades lacustres. La visita cobra sentido con barca o interpretación local.",
            "Ofrece un paisaje habitado más tranquilo que Ganvié y permite hablar de pesca y manglar.",
            "El pin se mantiene como referencia del lago. Organizar salida en Possotomé, pactar embarcadero, chalecos y regreso; no seguir pistas ribereñas sin confirmar.",
            "Amanecer o última tarde, sin tormenta; dos o tres horas.",
            "Omitir sin guía o barca segura, con viento fuerte o si solo se dispone de una parada desde carretera.",
            "Google Maps · lago Ahémé",
            "https://www.google.com/maps/search/?api=1&query=Lake%20Aheme%20Possotome%20Benin",
            [
                commons("LE LAC AHEME AU BENIN en 2018.jpg", "Adoscam · CC BY-SA 4.0", "Vista amplia del lago Ahémé."),
                commons("Pirogue sur le lac Ahémé à Possotomé.jpg", "Fawaz.tairou · CC BY-SA 4.0", "Piragua en Possotomé."),
                commons("Vue panoramique de mangroves sur le lac Ahémé au Sud-Ouest du Bénin.jpg", "Dagnon · CC BY-SA 4.0", "Manglar en la ribera del lago."),
            ],
        ),
        8: entry(
            "Ganvié es una ciudad lacustre viva sobre el lago Nokoué, recorrida en piragua entre viviendas, mercados y pesca. No es una escenografía para turistas.",
            "Es el paisaje urbano sobre el agua más reconocido del país y explica una adaptación histórica excepcional.",
            "El pin cae dentro de Ganvié; la salida se contrata en el embarcadero oficial. Confirmar precio, guía, chalecos y permiso para perro antes de pagar.",
            "Primera hora; el portal oficial recomienda dos o tres horas.",
            "Omitir con tormenta, barca insegura o retorno incierto; pedir permiso antes de fotografiar casas o residentes.",
            "Bénin Tourisme · Ganvié",
            "https://benintourisme.bj/en/destinations/ganvie/",
            [
                commons("Ganvie, The Venice Of Africa.jpg", "Kume Akpubi · CC BY-SA 4.0", "Viviendas y canoas en Ganvié."),
                commons("Ganvié, cité lacustre du Bénin (25).jpg", "Yai.isac · CC BY-SA 4.0", "Calle de agua en la ciudad lacustre."),
                commons("GANVIÉ LA BELLE CITÉ LACUSTRE 20.jpg", "Fermi12 · CC0", "Actividad cotidiana sobre el lago Nokoué."),
            ],
        ),
        9: entry(
            "Dantokpa es el gran mercado de Cotonú, extendido junto a la laguna y la pasarela. Su interés es la actividad comercial real, con aglomeración intensa.",
            "Muestra la escala económica de Cotonú y el intercambio regional mejor que un recorrido urbano genérico.",
            "El pin coincide con el mercado. Ir con guía local, sin objetos visibles, dejar el coche en aparcamiento vigilado y acordar punto de reunión.",
            "Temprano y de día; entre una y dos horas.",
            "Omitir con protestas, aglomeración extrema o sin guía; no fotografiar puestos ni personas sin permiso.",
            "Bénin Tourisme · Cotonú",
            "https://benintourisme.bj/en/cities/cotonou/",
            [
                commons("Sur la passerelle du marché dantokpa à Cotonou Bénin.jpg", "Adoscam · CC BY-SA 4.0", "Pasarela y puestos de Dantokpa."),
                commons("VENDEUSE DE CONDIMENTS SUR LA PASSERELLE MARCHE DANTOKPA-COTONOU BENIN.jpg", "Adoscam · CC BY-SA 4.0", "Vendedora de condimentos en Dantokpa."),
                commons("Pirogue déchargeant marchandises pour marché dantokpa à Cotonou Bénin.jpg", "Adoscam · CC BY-SA 4.0", "Mercancías llegando en piragua al mercado."),
            ],
        ),
        10: entry(
            "Porto-Novo conserva la Gran Mezquita de inspiración afrobrasileña, el palacio Honmè y barrios históricos. Es la capital política, no la mayor ciudad.",
            "Su arquitectura y museos explican el reino de Hogbonu y los retornos afrobrasileños.",
            "El pin se mantiene como ancla urbana. Priorizar la Gran Mezquita y Honmè con horarios confirmados; recorrer con guía y aparcamiento acordado.",
            "Día laborable, por la mañana; medio día o una noche.",
            "Omitir interiores durante culto o con museo cerrado; no prometer acceso a espacios palaciegos.",
            "Bénin Tourisme · Porto-Novo",
            "https://benintourisme.bj/en/cities/porto-novo/",
            [
                commons("Grande Mosquée de Porto-Novo au Bénin 03.jpg", "Gildaskiki · CC BY-SA 4.0", "Fachada de la Gran Mezquita de Porto-Novo."),
                commons("Courtyard Musee Honme Porto Novo Benin Dec 2017.jpg", "Kulttuurinavigaattori · CC BY-SA 4.0", "Patio del museo Honmè."),
                commons("Musee Honmè de Porto-Novo au Bénin.jpg", "Adoscam · CC BY-SA 4.0", "Edificio del antiguo palacio Honmè."),
            ],
        ),
        11: entry(
            "Las Tres Mamelles de Savè son inselbergs graníticos que dominan la ciudad. La caminata debe concretarse con guía porque el pin no define un inicio universal.",
            "Es una parada geológica potente en el eje central, con vistas del mosaico urbano y agrícola.",
            "El pin corresponde al conjunto rocoso auditado. Acordar guía e inicio en Savè, estacionar donde indiquen y no invadir lugares rituales.",
            "Salida muy temprana, día seco y de dos a cuatro horas según ruta.",
            "Omitir con tormenta, roca mojada, calor fuerte o guía no confirmado.",
            "Gobierno de Benín · Savè y sus mamelles",
            "https://www.gouv.bj/article/936/destination-benin---save--vous-accueille-sous-mamelles/",
            [
                external("https://expresstourisme.com/image/news/les-mamelles-de-save-tourisme-Benin-65dc6e54b1cf8.webp", "https://expresstourisme.com/news.benin/104-tourisme-au-benin-a-la-decouverte-des-mamelles-de-save", "Express Tourisme · derechos en la fuente", "Panorama de las Tres Mamelles de Savè."),
                external("https://www.gouv.bj/upload/images/articles/ckeditor/WhatsApp%20Image%202020-11-12%20at%2010_34_38%20AM.jpeg", "https://www.gouv.bj/article/936/destination-benin---save--vous-accueille-sous-mamelles/", "Gobierno de Benín · derechos en la fuente", "Promontorios rocosos sobre Savè."),
                commons("Les mamelles de Savè au centre du Bénin, vues du ciel 03.jpg", "Fawaz.tairou · CC BY-SA 4.0", "Vista aérea georreferenciada de las Mamelles de Savè."),
            ],
        ),
        12: entry(
            "Dassa-Zoumè está rodeada de colinas graníticas con cuevas, miradores y lugares de peregrinación. La basílica de Arigbo es uno de varios puntos posibles.",
            "Combina paisaje, historia local y espiritualidad sin exigir el desvío largo del norte.",
            "El pin coincide con el recinto de Arigbo. Para subir a las colinas, escoger ruta y guía por separado; respetar ceremonias y espacios sagrados.",
            "Primera hora; el portal oficial calcula dos o tres horas para las colinas.",
            "Omitir la subida con calor, tormenta o roca mojada; no presentar una aparición religiosa como hecho verificable.",
            "Bénin Tourisme · colinas de Dassa",
            "https://benintourisme.bj/en/destinations/the-dassa-hills/",
            [
                external("https://media-cdn.tripadvisor.com/media/photo-s/15/42/9e/1b/entree.jpg", "https://www.tripadvisor.com/Attraction_Review-g1218460-d12478533-Reviews-Grotte_Mariale_Notre_Dame_d_Arigbo-Dassa_Zoume_Collines_Department.html", "Tripadvisor · aportación de usuario; autor en la fuente", "Entrada del recinto mariano de Arigbo."),
                external("https://media.vaticannews.va/media/content/dam-archive/vaticannews/multimedia/2022/08/24/Aribgo-Dassa--copy--rsz.jpeg/_jcr_content/renditions/cq5dam.thumbnail.cropped.750.422.jpeg", "https://www.vaticannews.va/fr/afrique/news/2022-08/cloture-de-la-68e-edition-du-pelerinage-marial-national-du-benin.html", "Vatican News · derechos en la fuente", "Peregrinación documentada en Arigbo-Dassa."),
                external("https://i0.wp.com/hobletsonthego.com/wp-content/uploads/2025/01/20250113-Benin-Dassa-Zoume-King-of-the-Hill-1-2-1-e1737578839645.jpg?fit=980%2C654&ssl=1", "https://hobletsonthego.com/where-weve-been/africa/benin/king-of-the-hill/", "Hoblets on the Go · derechos en la fuente", "Sendero rocoso en las colinas de Dassa."),
            ],
        ),
        13: entry(
            "Los palacios reales de Abomey conservan arquitectura de tierra, bajorrelieves y colecciones del antiguo Dahomey. Parte del conjunto puede estar en restauración.",
            "Es el gran sitio histórico de Benín y la mejor introducción al reino, las agoodjié y la trata atlántica.",
            "El pin coincide con el museo histórico del conjunto. Confirmar entrada operativa, visita guiada y salas abiertas; el perro no entra.",
            "Primera hora y al menos dos o tres horas.",
            "Omitir interiores sin custodia para el perro o con cierre; no tocar muros ni fotografiar donde esté prohibido.",
            "Bénin Tourisme · palacios reales de Abomey",
            "https://benintourisme.bj/en/destinations/the-royal-palaces-of-abomey/",
            [
                commons("Royal Palaces of Abomey-133466.jpg", "Karalyn Monteil · CC BY-SA 3.0 IGO", "Edificio del conjunto palaciego de Abomey."),
                commons("Abomey royal palace wall.jpg", "Willem Heerbaart · CC BY 2.0", "Muro de tierra del palacio real."),
                commons("Abomey 2006 1.jpg", "Joachim Huber · CC BY-SA 2.0", "Patio y arquitectura del museo de Abomey."),
            ],
        ),
        15: entry(
            "Tanéka Béri es una aldea histórica de montaña con arquitectura de piedra y tierra y espacios rituales activos. No es una visita libre sin mediación.",
            "Permite conocer un paisaje cultural del noroeste distinto de los palacios fon y de Koutammakou.",
            "El pin coincide con Tanéka Béri. Contratar guía comunitario desde Copargo o el acceso indicado, acordar fotografías y llegar solo de día.",
            "Estación seca, por la mañana y con medio día.",
            "Omitir sin guía o permiso, con alerta regional o pista mojada; no entrar en espacios rituales por cuenta propia.",
            "Google Maps · Tanéka Béri",
            "https://www.google.com/maps/search/?api=1&query=Taneka%20Beri%20Benin",
            [
                commons("L'entrée du village Tanéka Béri 1.jpg", "Aimeabibis · CC BY-SA 4.0", "Entrada de la aldea Tanéka Béri."),
                commons("Tanéka-Béri (3).jpg", "Ji-Elle · CC BY-SA 4.0", "Arquitectura tradicional de Tanéka Béri."),
                commons("Toits de Tanéka-Béri (3).jpg", "Ji-Elle · CC BY-SA 4.0", "Cubiertas y relieve de la aldea."),
            ],
        ),
    },
    "nigeria": {
        1: entry(
            "Badagry conserva museos, barracones y la ruta de memoria que cruza la laguna hasta el Punto de No Retorno. La jornada necesita guía y barca.",
            "Es la mejor introducción nigeriana a la trata atlántica y enlaza directamente con Ouidah.",
            "El pin cae en el Punto de No Retorno; el recorrido empieza en Badagry. Contratar guía identificado, pactar chalecos y regreso y distinguir monumentos de lugares históricos.",
            "Primera hora y medio día; evitar combinar frontera, visita y llegada nocturna a Lagos.",
            "Omitir el cruce con mal tiempo o barca insegura; no hacer la ruta como simple sesión fotográfica.",
            "Gobierno de Lagos · patrimonio de Badagry",
            "https://lagosstate.gov.ng/news/all/view/68accfd888319a643b6098ec",
            [
                commons("Gberefu Island Point of No Return, Badagry - The Original Slave Route.jpg", "Kamilu Tope · CC BY-SA 4.0", "Punto de No Retorno en la isla Gberefu."),
                commons("POINT OF NO RETURN, Slave Trade route, Badagry, Lagos.tif", "Spakinrinwa · CC BY-SA 4.0", "Monumento final de la ruta de Badagry."),
                commons("Badagry slave route. 04.jpg", "Yemi festus · CC BY-SA 4.0", "Tramo documentado de la ruta de los esclavos."),
            ],
        ),
        2: entry(
            "Lagos es una megaciudad de lagunas e islas: Lagos Island, Balogun, el Museo Nacional y Victoria Island exigen visitas separadas. Es ante todo una base logística.",
            "Permite entender la escala económica y cultural de Nigeria y resolver servicios que no existen en el interior.",
            "El pin se mantiene como ancla urbana. Reservar alojamiento con aparcamiento y generador, usar conductor local si conviene y planificar cada cruce por tráfico.",
            "Días laborables para servicios; mínimo dos noches si se visita la ciudad.",
            "Reducir turismo urbano con protestas, inundaciones, tráfico bloqueado o sin estacionamiento seguro.",
            "Tour Nigeria · Lagos",
            "https://tournigeria.gov.ng/lagos-2/",
            [
                commons("Lagos-centre-from-executive-lounge-Continental-hotel-2026-IMG 7970.jpg", "FrankvEck · CC BY-SA 4.0", "Centro de Lagos documentado en 2026."),
                commons("Balogun Market, Lagos Island.jpg", "Yellowcrunchy · CC BY-SA 4.0", "Actividad en Balogun Market."),
                commons("National Museum Lagos, Nigeria.jpg", "Beendy234 · CC BY-SA 4.0", "Edificio del Museo Nacional de Lagos."),
            ],
        ),
        3: entry(
            "Lekki Conservation Centre protege humedal y bosque urbano con senderos y pasarela elevada. Es una reserva gestionada, no una zona de paseo libre.",
            "Ofrece naturaleza accesible dentro de Lagos y un contraste claro con el centro urbano.",
            "El pin coincide con la entrada. Confirmar horario y estado de la pasarela con Nigerian Conservation Foundation; el perro no entra.",
            "Al abrir, en día seco; dos o tres horas.",
            "Omitir con tormenta, pasarela cerrada, calor fuerte o sin custodia segura para el perro.",
            "Nigerian Conservation Foundation · Lekki",
            "https://www.ncfnigeria.org/",
            [
                commons("LEKKI CONSERVATION CENTRE (LCC) 10.jpg", "Ashinze · CC BY-SA 4.0", "Pasarela elevada de Lekki Conservation Centre."),
                commons("Biodiversity of Lekki Conservation Centre, Lagos State, Nigeria 58.jpg", "MediaMOF · CC BY-SA 4.0", "Vegetación dentro de la reserva."),
                commons("Lekki Conservation Centre Caution Board.jpg", "James Moore200 · CC BY-SA 4.0", "Señal de seguridad del centro."),
            ],
        ),
        4: entry(
            "Benin City conserva el palacio del Oba y el patrimonio artístico edo. MOWAA es un centro distinto y en 2026 limita el acceso público a cita previa.",
            "Es el lugar central para comprender el reino de Benín, el saqueo de 1897 y el debate sobre restitución.",
            "El pin se corrige al palacio del Oba. Confirmar visita local y no fotografiar sin permiso; consultar MOWAA por separado antes de contar con su acceso.",
            "Día laborable, con cita confirmada si se incluye MOWAA; medio día o una noche.",
            "Omitir interiores sin autorización o durante ceremonia; perro fuera. No presentar MOWAA como museo de entrada libre.",
            "MOWAA · acceso y programa actual",
            "https://wearemowaa.org/",
            [
                commons("Royal Palace of the Oba of Benin.jpg", "Kelechukwu Ajoku · CC BY-SA 4.0", "Acceso al palacio real del Oba de Benín."),
                commons("Gateway entrance to Oba palace.3.jpg", "MediaMOF · CC BY-SA 4.0", "Puerta exterior del recinto palaciego."),
                commons("Wooden Pillar of a Benin Palace 02.jpg", "Adesolive · CC BY-SA 4.0", "Pilar de madera asociado a la arquitectura palaciega."),
            ],
            name="Benin City · palacio del Oba y patrimonio edo",
        ),
        6: entry(
            "Calabar conserva Duke Town, el museo y una fuerte cultura efik; también es la base para Drill Ranch y el sureste de Cross River.",
            "Funciona como nodo cultural y logístico antes de las carreteras más exigentes hacia Ikom y Camerún.",
            "El pin se mantiene como ancla urbana. Elegir alojamiento con aparcamiento, confirmar museo y recorrer Duke Town de día con guía.",
            "Día laborable y una o dos noches para preparar el corredor interior.",
            "Reducir visitas con lluvia intensa, protestas o museo cerrado; no conducir de noche hacia Ikom.",
            "Cross River State · portal oficial",
            "https://crossriverstate.gov.ng/",
            [
                commons("Duke Town, Calabar, Nigeria - panoramio.jpg", "stone wu · CC BY-SA 3.0", "Duke Town y el río en Calabar."),
                commons("Nigeria masquerade Calabar.jpg", "Orokbest1 · CC BY-SA 4.0", "Mascarada cultural documentada en Calabar."),
                commons("Nigeria cultural dance group.Cross River State.jpg", "Orokbest1 · CC BY-SA 4.0", "Grupo de danza de Cross River State."),
            ],
        ),
        7: entry(
            "Drill Ranch Calabar rehabilita drills y chimpancés rescatados y ofrece visita guiada. Es un centro de conservación activo, no un zoológico de contacto.",
            "Permite conocer una especie muy amenazada y el trabajo que después continúa en Afi Mountain.",
            "El pin coincide con la sede de Calabar. Contactar antes aunque la web indique apertura diaria; seguir al personal y dejar al perro fuera.",
            "Primera hora, evitando grupos escolares; una o dos horas.",
            "Omitir sin confirmación, con emergencia animal o sin custodia para el perro; nunca tocar ni alimentar primates.",
            "Pandrillus · Drill Ranch",
            "https://www.pandrillus.org/projects/drill-ranch/",
            [
                commons("Endangered Drill monkeys at Driving ranch, calabar,Nigeria 02.jpg", "Imanueljnr · CC BY-SA 4.0", "Drills en el centro de Calabar."),
                commons("Endangered Drill monkeys at Driving ranch, calabar,Nigeria 03.jpg", "Imanueljnr · CC BY-SA 4.0", "Grupo de drills rehabilitados."),
                commons("Endangered Drill monkeys at Driving ranch, calabar,Nigeria 01.jpg", "Imanueljnr · CC BY-SA 4.0", "Recinto naturalizado de los primates."),
            ],
        ),
        8: entry(
            "Cross River National Park protege dos divisiones no contiguas, Oban y Okwangwo. El PDI representa el espacio, no una puerta turística comprobada.",
            "Conserva una de las últimas grandes selvas nigerianas, pero solo merece la pena con acceso oficial organizado.",
            "El pin se mantiene como referencia del sector Oban. Contactar con Nigeria Park Service para puerta, permiso, guía y seguridad; perro prohibido.",
            "Estación menos lluviosa y solo con confirmación reciente; jornada completa.",
            "Descartarlo sin respuesta del parque, con alerta, pista mojada o sin custodia del perro; no internarse por cuenta propia.",
            "Nigeria Park Service · Cross River National Park",
            "https://nigeriaparkservice.gov.ng/blog/2014/08/12/cross-river-national-park/",
            [
                commons("Oban Hills, Cross River State.jpg", "Auskid1215 · CC BY-SA 4.0", "Relieve selvático de Oban Hills."),
                commons("Ime river.jpg", "Dotun55 · CC BY-SA 4.0", "Curso de agua en el paisaje de Cross River."),
                commons("Papilio zalmoxis Nigeria.jpg", "Rdwarre57 · CC BY-SA 4.0", "Mariposa Papilio zalmoxis documentada en Nigeria."),
            ],
        ),
        9: entry(
            "Los monolitos de Alok/Ikom son piedras talladas de los siglos XVI–XX, distribuidas por comunidades del alto Cross River y en la lista indicativa de UNESCO.",
            "Son el patrimonio arqueológico más singular del corredor hacia Camerún.",
            "El pin coincide con el conjunto de Alok. Llegar con guía local o Turismo de Cross River, pedir permiso comunitario y no tocar ni mover las piedras.",
            "Mañana, tiempo seco y dos o tres horas desde Ikom.",
            "Omitir sin guía, con pista impracticable o alerta local; no inventar significados de las inscripciones.",
            "UNESCO · monolitos de Alok/Ikom",
            "https://whc.unesco.org/en/tentativelists/5170/",
            [
                commons("Ikom monolith 3.jpg", "Dotun55 · CC BY-SA 4.0", "Monolito tallado del conjunto de Ikom."),
                commons("Ikom Monolith 1.jpg", "Dotun55 · CC BY-SA 4.0", "Detalle antropomorfo de una piedra de Alok."),
                commons("Ikom monoliths.jpg", "Dotun55 · CC BY-SA 4.0", "Varios monolitos conservados en su entorno."),
            ],
        ),
        10: entry(
            "Agbokim reúne siete brazos de cascada cerca de la frontera camerunesa. El acceso por carretera ha sido descrito como deficiente por el propio estado.",
            "Es el conjunto de saltos más espectacular de Cross River cuando el caudal permite distinguir sus brazos.",
            "El pin coincide con la cascada. Preguntar en Ikom por firme y seguridad el mismo día, contratar guía y aparcar antes del tramo dudoso.",
            "Con caudal moderado, por la mañana y sin lluvia activa; medio día.",
            "Omitir con pista embarrada, crecida, tormenta o alerta fronteriza; no bajar a roca mojada.",
            "Cross River State · visita oficial a Agbokim",
            "https://news.crossriverstate.gov.ng/criver-tourism-ministry-embarks-on-familiarization-tour-of-agbokim-waterfalls-alok-ikom-monoliths/",
            [
                commons("Agbokim waterfalls.jpg", "MuaMee · CC BY-SA 4.0", "Varios brazos de Agbokim Waterfalls."),
                commons("Agbokim Waterfalls, Agbokim, Cross River state.jpg", "Ei'eke · CC BY-SA 4.0", "Caída principal en temporada con agua."),
                commons("Agbokim Waterfalls Small falls 05.jpg", "Ransome E Owan · CC BY-SA 4.0", "Uno de los saltos menores del conjunto."),
            ],
        ),
        11: entry(
            "Afi Mountain combina un santuario forestal estatal y el centro de campo de Drill Ranch. Las caminatas son abruptas y la fauna salvaje es esquiva.",
            "Es una experiencia de conservación profunda, valiosa por el bosque y el proyecto aunque no se vea un gorila.",
            "El pin es una referencia del santuario. Reservar con Pandrillus, pedir estado de los últimos 6 km y puentes y llegar con comida, agua y combustible desde Ikom u Obudu.",
            "Estación menos lluviosa, reserva previa y una o más noches.",
            "Omitir sin confirmación, con vehículo pesado para los puentes, alerta o sin custodia del perro; guía obligatorio.",
            "Pandrillus · información de visita a Afi",
            "https://www.pandrillus.org/projects/drill-ranch/visitor-information/",
            [
                commons("Afi Mountain Wildlife Sanctuary.jpg", "Obongha oguni · CC BY-SA 4.0", "Bosque y relieve del santuario de Afi."),
                commons("View from Afi Mountain Wildlife Sanctuary.jpg", "Dotun55 · CC BY-SA 4.0", "Vista desde Afi Mountain."),
                commons("Odiga Waterfall.jpg", "Dotun55 · CC BY-SA 4.0", "Cascada Odiga en el entorno de Afi."),
            ],
        ),
        12: entry(
            "Obudu Mountain Resort ocupa una meseta fresca con vistas, senderos y antiguas infraestructuras turísticas. No debe darse por operativo ningún servicio sin confirmarlo.",
            "El paisaje de altitud es excepcional en Nigeria y puede cerrar bien el eje de Cross River.",
            "El pin coincide con el resort. Llamar antes para carretera, alojamiento, electricidad y actividades; la imagen del teleférico es histórica y no prueba que funcione.",
            "Estación seca, llegada con luz y una o dos noches.",
            "Omitir con niebla densa, carretera dañada o sin reserva confirmada; no planificar alrededor del teleférico.",
            "Google Maps · Obudu Mountain Resort",
            "https://www.google.com/maps/search/?api=1&query=Obudu%20Mountain%20Resort%20Nigeria",
            [
                commons("Obudu Mountain Resort 02.jpg", "Bassnificient · CC BY-SA 4.0", "Paisaje de la meseta de Obudu."),
                commons("Obudu Cattle ranch Gate, Obudu, Cross river state3.jpg", "MediaMOF · CC BY-SA 4.0", "Puerta de acceso al antiguo Cattle Ranch."),
                commons("Cable Car, Obudu Cattle Ranch, Obudu, Cross river state 01.jpg", "Ei'eke · CC BY-SA 4.0", "Teleférico de Obudu fotografiado; confirmar operación actual."),
            ],
        ),
        13: entry(
            "Osun-Osogbo es un bosque sagrado yoruba con santuarios, esculturas y el río Osun. Es un lugar religioso vivo y Patrimonio Mundial.",
            "Combina paisaje forestal, arte de Susanne Wenger y continuidad ritual de una forma única.",
            "El pin coincide con el acceso del bosque. Entrar con guía, seguir las normas de cada santuario y dejar al perro fuera.",
            "Primera hora y fuera del festival si se busca calma; dos o tres horas.",
            "Omitir con ceremonia privada, cierre o sin custodia del perro; no tocar esculturas ni fotografiar rituales sin permiso.",
            "UNESCO · Osun-Osogbo Sacred Grove",
            "https://whc.unesco.org/en/list/1118/",
            [
                commons("Osun Sacred Grove Forest - Shrine II.jpg", "Tosin Odunfa · CC BY-SA 4.0", "Santuario dentro del bosque de Osun-Osogbo."),
                commons("Osun Osogbo Sacred Groove - The Forest Pathway.jpg", "Tunde Akangbe · CC BY-SA 4.0", "Sendero forestal del bosque sagrado."),
                commons("Deity in Osogbo Groove 02.jpg", "Love Ifechukwu ObianujuAku Nebo · CC BY-SA 4.0", "Escultura ritual en Osun-Osogbo."),
            ],
        ),
        14: entry(
            "Mapo Hall domina el casco histórico de Ibadan y ofrece contexto sobre la administración colonial; Cocoa House recuerda el auge regional del cacao.",
            "Convierte una escala urbana difusa en dos hitos concretos con lectura histórica y económica.",
            "El pin se corrige a Mapo Hall mediante coordenada georreferenciada. Confirmar acceso y aparcamiento; Cocoa House es un edificio distinto en Dugbe.",
            "Día laborable y primera hora; una o dos horas.",
            "Omitir interiores sin autorización o con actos oficiales; no detenerse en calzada congestionada para fotografiar.",
            "Google Maps · Mapo Hall",
            "https://www.google.com/maps/search/?api=1&query=Mapo%20Hall%20Ibadan%20Nigeria",
            [
                commons("Aerial view of Mapo Hall in ibadan city.jpg", "Ayorinde Ogundele · CC BY-SA 4.0", "Vista aérea georreferenciada de Mapo Hall."),
                commons("Cocoa House, Ibadan.JPG", "Ibadan234 · CC BY-SA 4.0", "Cocoa House en el distrito de Dugbe."),
                commons("Further images of Ibadan city from Mapo Hall 12.jpg", "Kaizernify · dominio público", "Ibadan visto desde Mapo Hall."),
            ],
            name="Ibadan · Mapo Hall y Cocoa House",
            coords=(7.376231, 3.895901),
        ),
        15: entry(
            "Olumo Rock es un afloramiento sobre Abeokuta usado como refugio en el siglo XIX. El recinto tiene escalones y pasajes naturales; servicios mecánicos pueden no operar.",
            "Combina historia egba, geología y una gran vista urbana en una visita manejable.",
            "El pin coincide con la entrada de Olumo Rock. Confirmar horario, guía y estado de accesos; no contar con ascensor ni dejar objetos en el coche.",
            "A primera hora, con roca seca; dos horas.",
            "Omitir con tormenta, calor extremo, movilidad reducida sin alternativa confirmada o controles de seguridad insuficientes.",
            "Google Maps · Olumo Rock",
            "https://www.google.com/maps/search/?api=1&query=Olumo%20Rock%20Abeokuta%20Nigeria",
            [
                commons("Olumo Rock Abk.2.jpg", "F.Samuel95 · CC BY-SA 4.0", "Afloramiento de Olumo Rock sobre Abeokuta."),
                commons("Olumo Rock Shrine in Abeokuta.jpg", "Akintoye Dekalu · CC BY-SA 4.0", "Santuario dentro del conjunto de Olumo."),
                commons("Natural look of OlumoRock.jpg", "Adenekan19 · CC BY-SA 4.0", "Pasajes de roca natural en Olumo."),
            ],
        ),
    },
}


REMOVE = {
    "ghana": {19},
    "togo": {4, 8, 12, 14, 18},
    "benin": {4, 6, 7, 14, 16, 17, 18, 19},
    "nigeria": {5},
}


FICHA_META = {
    "ghana": (1, "21 puntos auditados con galería exacta, enlace útil y coordenadas contrastadas"),
    "togo": (10, "14 puntos auditados entre el corredor costero y el eje interior"),
    "benin": (2, "11 puntos auditados; el norte inseguro se excluye de la selección"),
    "nigeria": (1, "14 puntos auditados en los corredores sur, Cross River y suroeste"),
}


def clean_stale(value):
    if isinstance(value, str):
        value = value.replace("12 de septiembre de 2026", "15 de septiembre de 2026")
        return re.sub(r'<tr ><td>Fotos pendientes de sustituir</td><td>.*?</td></tr>', "", value, flags=re.DOTALL)
    if isinstance(value, list):
        return [clean_stale(item) for item in value]
    if isinstance(value, dict):
        return {key: clean_stale(item) for key, item in value.items()}
    return value


def apply_country(country: str) -> None:
    path = ROOT / "content" / "pois" / f"{country}.json"
    pois = json.loads(path.read_text(encoding="utf-8"))
    pois = [poi for poi in pois if poi["n"] not in REMOVE[country]]
    updates = DATA[country]
    expected = {poi["n"] for poi in pois}
    if set(updates) != expected:
        raise ValueError(f"{country}: faltan={sorted(expected-set(updates))}; sobran={sorted(set(updates)-expected)}")
    for poi in pois:
        old_desc = poi["desc"]
        update = updates[poi["n"]]
        if update["visit"]["see"] is None:
            update["visit"]["see"] = old_desc
        for key in ("name", "lat", "lon", "desc", "visit", "links", "photos"):
            if key in update:
                poi[key] = update[key]
        primary = poi["photos"][0]
        poi["img"], poi["source"], poi["credit"] = primary["img"], primary["source"], primary["credit"]
    path.write_text(json.dumps(pois, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def apply_ficha(country: str) -> None:
    path = ROOT / "content" / "ficha" / f"{country}.json"
    ficha = clean_stale(json.loads(path.read_text(encoding="utf-8")))
    hero_n, chip_text = FICHA_META[country]
    photo = DATA[country][hero_n]["photos"][0]
    ficha["hero_img"] = photo["img"]
    ficha["hero_credit"] = photo["caption"] + " · " + photo["credit"]
    for chip in ficha.get("chips", []):
        if isinstance(chip, list) and chip and chip[0] == "PDIs":
            chip[1] = chip_text
    ficha["revision"] = "15 sep 2026"
    ficha["verificado"] = True
    path.write_text(json.dumps(ficha, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    for country in DATA:
        apply_country(country)
        apply_ficha(country)


if __name__ == "__main__":
    main()

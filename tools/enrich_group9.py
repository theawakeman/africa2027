#!/usr/bin/env python3
"""Auditoría editorial reproducible del grupo 9: Namibia.

Las 24 coordenadas se contrastaron una a una con el objeto real de Google
Maps. Para espacios extensos se fija un acceso, recepción, mirador o elemento
visitable concreto; la excepción es la pintura White Lady, cuyo pin representa
el panel al que se llega a pie y no un aparcamiento inexistente.
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


def entry(desc: str, why: str, see: str, access: str, when: str, skip: str) -> dict:
    return {
        "desc": desc,
        "visit": {"why": why, "see": see, "access": access, "when": when, "skip": skip},
    }


COORDS = {
    1: (-27.5891682, 17.6145749),
    2: (-26.4814114, 18.2375665),
    3: (-26.5947881, 16.0757057),
    4: (-26.6477353, 15.1518021),
    5: (-26.7016875, 15.2320625),
    6: (-24.7277568, 15.4725668),
    7: (-24.7592732, 15.2923894),
    8: (-23.3030703, 15.7736518),
    9: (-22.9733978, 14.4785799),
    10: (-23.3571081, 14.4986540),
    11: (-22.6806338, 14.5191099),
    12: (-21.8395132, 15.2015866),
    13: (-21.7716993, 13.9524077),
    14: (-21.4112059, 14.2163411),
    15: (-21.1106969, 14.6625695),
    16: (-20.5904535, 14.3720279),
    17: (-19.8863142, 13.9365328),
    18: (-21.1727036, 13.6696429),
    19: (-19.1809447, 15.9163519),
    20: (-17.6333333, 12.7000000),
    21: (-17.0018086, 13.2408032),
    22: (-17.3941201, 14.2194575),
    23: (-22.5688266, 17.0879955),
    24: (-20.5163693, 17.2452939),
}


NAMES = {
    1: "Fish River Canyon · mirador principal",
    2: "Quiver Tree Forest y Giant's Playground",
    3: "Garub · caballos del desierto",
    4: "Lüderitz · waterfront y memoria portuaria",
    5: "Kolmanskop · entrada del poblado minero",
    6: "Dune 45 · Sossusvlei",
    7: "Deadvlei",
    8: "Kuiseb River Viewpoint",
    9: "Walvis Bay · Flamingo Lagoon",
    10: "Sandwich Harbour",
    11: "Swakopmund · Jetty Pier",
    12: "Spitzkoppe · Community Restcamp",
    13: "Cape Cross Seal Reserve",
    14: "Messum Crater",
    15: "Brandberg · White Lady",
    16: "Twyfelfontein · centro de visitantes",
    17: "Palmwag · lodge y concesión",
    18: "Skeleton Coast · Ugab Gate",
    19: "Etosha · charca de Okaukuejo",
    20: "Van Zyl's Pass",
    21: "Epupa Falls · mirador",
    22: "Ruacana Falls · mirador",
    23: "Windhoek · Independence Memorial Museum",
    24: "Waterberg · recepción de NWR",
}


LINKS = {
    1: [("NWR · Hobas Lodge y acceso al cañón", "https://www.nwr.com.na/resorts/hobas-lodge/")],
    2: [("Quivertree Forest Rest Camp · visita oficial", "https://quivertreeforest.com/about")],
    3: [("MEFT · plan de gestión de los caballos de Garub", "https://www.meft.gov.na/files/files/Horses%20of%20the%20Namib%20Management%20Plan.pdf")],
    4: [("Lüderitz Waterfront Development Company", "https://luderitzwaterfront.com.na/")],
    5: [("Kolmanskuppe · horarios, permisos y visitas", "https://kolmanskuppe.com/tours-prices/")],
    6: [("MEFT · Namib-Naukluft Park", "https://meft.gov.na/national-parks/namib-naukluft-park/224/")],
    7: [("NWR · traslado vigente hacia Deadvlei", "https://www.nwr.com.na/nwr-announcement-on-shuttle-service-update-in-the-sossusvlei-area/")],
    8: [("MEFT · Namib-Naukluft y valle del Kuiseb", "https://meft.gov.na/national-parks/namib-naukluft-park/224/")],
    9: [("Ramsar · humedales de importancia internacional de Namibia", "https://rsis.ramsar.org/sites/default/files/rsiswp_search/exports/Ramsar-Sites-annotated-summary-Namibia.pdf")],
    10: [("MEFT · permisos para Sandwich Harbour", "https://www.meft.gov.na/frequently-asked-questions/what-are-the-entry-permit-requirements-for-the-various-parks-in-namibia-/136/")],
    11: [("Swakopmund · historia y visita de la Jetty", "https://www.swakopmundnamibia.com/jetty-in-swakopmund/")],
    12: [("Spitzkoppe Rest Camp · web del gestor", "https://spitzkoppe.com/")],
    13: [("MEFT · Cape Cross Seal Reserve", "https://meft.gov.na/national-parks/cape-cross-seal-reserve/214/")],
    14: [("Travel Namibia · Messum Crater y permiso", "https://travelnam.com/crater-with-a-difference-messum-crater/")],
    15: [("National Heritage Council · White Lady", "https://www.travel.na/download/Heritage_Sites_April_2024_25.pdf")],
    16: [("UNESCO · Twyfelfontein o /Ui-//aes", "https://whc.unesco.org/en/list/1255")],
    17: [("Palmwag Lodge · alojamiento y actividades del gestor", "https://gondwana-collection.com/accommodation/palmwag-lodge")],
    18: [("MEFT · Skeleton Coast Park", "https://meft.gov.na/national-parks/skeleton-coast-park/227/")],
    19: [("NWR · Okaukuejo Waterhole", "https://www.nwr.com.na/okaukuejo-waterhole-live-streaming-now-available-on-dstv/")],
    20: [("Visit Namibia · Arid Eden y Kaokoland", "https://visitnamibia.com.na/arid-eden-route-2/")],
    21: [("Visit Namibia · ruta del noroeste y Epupa", "https://visitnamibia.com.na/arid-eden-route-2/")],
    22: [("Visit Namibia · Roof of Namibia y Ruacana", "https://visitnamibia.com.na/roof-of-namibia/")],
    23: [("Windhoek City Council · Independence Memorial Museum", "https://www.windhoekcc.org.na/independence-memorial-museum/")],
    24: [("NWR · Waterberg Resort", "https://www.nwr.com.na/resorts/waterberg-resort/")],
}


def links(number: int) -> list[dict[str, str]]:
    return [{"label": label, "url": url} for label, url in LINKS[number]]


CONTENT = {
    1: entry(
        "El mirador principal abre la vista sobre las curvas encajadas del Fish River Canyon. Hobas es la base de acceso; la travesía de varios días es otra actividad y exige reserva.",
        "Permite entender la escala del cañón sin comprometerse con la exigente travesía integral.",
        "Paredes estratificadas, el cauce en el fondo y varios miradores enlazados por pista; Ai-Ais queda en otro acceso.",
        "El pin coincide con Fish River Canyon Viewpoint en Google Maps. Entrar por Hobas, pagar el parque y respetar cierres y barreras.",
        "Primera o última hora, con visibilidad limpia; reservar aparte cualquier caminata larga.",
        "Omitir la caminata con cierre estacional, calor fuerte, falta de reserva o sin resolver el perro fuera del parque."),
    2: entry(
        "En la granja Gariganus se visitan un bosque de kokerbooms y, a pocos kilómetros, los bloques de dolerita de Giant's Playground. La recepción del rest camp es el acceso comprobable.",
        "Reúne botánica, geología y fotografía en una parada manejable cerca de Keetmanshoop.",
        "Aloidendron dichotomum entre roca oscura y el corto recorrido por los bloques apilados de Giant's Playground.",
        "El pin coincide con Quivertree Forest Rest Camp. Pagar la visita en recepción y confirmar horario, senderos y mascotas.",
        "Atardecer para los árboles; luz diurna suficiente para recorrer los bloques con seguridad.",
        "No entrar fuera de horario ni caminar sobre roca mojada; descartar si la propiedad no autoriza al perro."),
    3: entry(
        "El observatorio de Garub permite buscar la pequeña población de caballos ferales adaptada al borde oriental del Namib. Su origen combina varias hipótesis y los avistamientos no están garantizados.",
        "Es un encuentro singular entre historia ferroviaria, adaptación animal y paisaje desértico.",
        "Caballos y, a veces, órix en torno al abrevadero; también quedan restos ferroviarios de Garub.",
        "El pin coincide con Garub Desert Horses en Google Maps. Observar desde el hide y no alimentar ni aproximarse al rebaño.",
        "Mañana o última hora; prever que puede no aparecer ningún caballo.",
        "Omitirlo con calor central, mala visibilidad o si el plan depende de un avistamiento asegurado."),
    4: entry(
        "El waterfront es una ancla precisa para recorrer el puerto de Lüderitz y visitar el Namibia Maritime Museum. La arquitectura, Shark Island y la historia colonial requieren una lectura crítica.",
        "Aporta contexto portuario y servicios antes de Kolmanskop y de los tramos remotos de la costa.",
        "Bahía, antiguo edificio industrial, museo marítimo y fachadas históricas; los lugares de memoria no son decorado turístico.",
        "El pin coincide con Lüderitz Waterfront Development Company. Aparcar en zona autorizada y comprobar el horario del museo.",
        "Horario diurno, dejando margen para caminar y para el viento costero.",
        "Reducirlo a escala logística si el museo está cerrado; no sustituye la visita guiada a Kolmanskop."),
    5: entry(
        "Kolmanskop conserva edificios del antiguo enclave diamantífero invadidos por arena. El permiso se obtiene en la entrada y la visita guiada ayuda a separar historia laboral, segregación y estética de ruina.",
        "Es uno de los testimonios más legibles del auge y abandono de la minería colonial del sur.",
        "Hospital, casino, viviendas y habitaciones colmatadas; solo se entra en edificios autorizados.",
        "El pin coincide con Kolmanskop Entrance en Google Maps. Consultar horario, permiso ordinario o fotográfico y condiciones del operador.",
        "Primera visita guiada del día o permiso fotográfico reservado.",
        "No entrar sin permiso, fuera de horario ni en estancias cerradas por estabilidad o conservación."),
    6: entry(
        "Dune 45 es la duna señalizada junto a la carretera de Sossusvlei. Se puede contemplar desde el aparcamiento o subir por la cresta, sin presentarla como un récord mundial.",
        "Ofrece una lectura clara de la forma y el color de las dunas con acceso mucho más sencillo que las pistas finales.",
        "Cresta, cara de deslizamiento y mar de dunas; el nombre procede de su posición aproximada en la ruta.",
        "El pin coincide con Dune 45 en Google Maps. Entrar por Sesriem, respetar horario del parque y aparcar fuera de la calzada.",
        "Amanecer o primera hora, antes del calor y del tráfico.",
        "No subir con calor fuerte, viento de arena o si el parque no admite el plan previsto para el perro."),
    7: entry(
        "Deadvlei es una cubeta clara con antiguos troncos de camelthorn, aislada del flujo del Tsauchab por las dunas. El último tramo combina arena profunda y caminata.",
        "El contraste entre arcilla blanca, troncos oscuros y dunas rojas es distinto de la visita a Dune 45.",
        "La cubeta, los árboles conservados por la aridez y el borde de Big Daddy; no tocar ni trepar los troncos.",
        "El pin coincide con Deadvlei. Confirmar en Sesriem el traslado vigente: NWR anunció en 2024 que su shuttle salía desde el campsite.",
        "Muy temprano, con agua suficiente y regreso antes del calor.",
        "Descartarlo sin transporte autorizado, con tormenta de arena o sin una solución real para el perro."),
    8: entry(
        "Este mirador se asoma al valle encajado del Kuiseb desde la pista C14. La antigua ficha mezclaba aquí Welwitschia Drive, que es otro recorrido y requiere su propio permiso.",
        "Rompe el largo tramo entre Solitaire y Walvis Bay y muestra la frontera natural entre grava y campos de dunas.",
        "Cauce efímero, paredes oscuras y carretera de paso; no es un centro de visitantes ni la entrada a Welwitschia Drive.",
        "El pin coincide con Kuiseb River Viewpoint en Google Maps. Parar solo fuera de la calzada y permanecer en suelo consolidado.",
        "Luz lateral y tiempo estable; visita breve de carretera.",
        "No parar con polvo denso, niebla, tráfico o sin espacio seguro para sacar completamente el vehículo."),
    9: entry(
        "Flamingo Lagoon fija un punto concreto del paseo de Walvis Bay desde el que observar el humedal Ramsar. La cantidad y posición de las aves cambian con marea y estación.",
        "Permite observar aves costeras sin excursión en barco y entender el valor ecológico de la bahía.",
        "Flamencos mayores y menores, limícolas y bancos intermareales; nunca se promete una concentración concreta.",
        "El pin coincide con Flamingo Lagoon en Google Maps. Usar el paseo, mantener distancia y no entrar en el fango.",
        "Dos horas alrededor de bajamar suelen exponer más zona de alimentación; comprobar la tabla local.",
        "Omitirlo con niebla cerrada o perturbación; perro siempre atado y lejos de las aves."),
    10: entry(
        "Sandwich Harbour combina laguna, playa y dunas costeras dentro de Namib-Naukluft. El acceso motorizado exige permiso previo y depende de marea, arena y ruta autorizada.",
        "Es el encuentro más directo entre el mar de arena del Namib y el Atlántico.",
        "Laguna, aves y laderas que alcanzan la costa; las fotos corresponden al propio humedal.",
        "El pin coincide con Sandwich Harbour en Google Maps. MEFT exige permiso previo; contratar guía si no se domina arena y mareas.",
        "Solo con ventana de marea y previsión estable confirmadas el mismo día.",
        "No entrar con marea subiendo, sin permiso, en solitario, sin compresor o sin un plan externo para el perro."),
    11: entry(
        "La Jetty Pier es el hito costero elegido para una ficha que antes marcaba la ciudad entera. Swakopmund sigue siendo la gran base de talleres, permisos y descanso del litoral.",
        "Combina un paseo corto por historia portuaria con servicios difíciles de encontrar en los tramos siguientes.",
        "Pasarela sobre el Atlántico, frente marítimo y arquitectura urbana; el restaurante no es imprescindible para visitar el muelle.",
        "El pin coincide con Jetty Pier - End of Pier en Google Maps. Aparcar en zona urbana y confirmar cierres por oleaje o mantenimiento.",
        "Atardecer si el viento y la niebla permiten buena visibilidad.",
        "Omitir el muelle con cierre, oleaje fuerte o falta de luz; conservar la escala logística si hace falta."),
    12: entry(
        "El rest camp comunitario es la puerta operativa al paisaje de granito de Spitzkoppe, sus arcos y algunos abrigos con arte rupestre. Los campamentos interiores son rústicos y dispersos.",
        "Permite caminar, acampar entre inselbergs y contribuir a una operación ligada a la comunidad local.",
        "Arco de roca, vistas del macizo, senderos y arte rupestre solo donde el gestor autorice.",
        "El pin coincide con Spitzkoppe Community Restcamp. Pagar acceso en recepción y confirmar guía, camping y mascotas.",
        "Tarde y amanecer; reservar noche para evitar una visita apresurada.",
        "No escalar sin equipo ni guía, caminar sobre roca mojada o asumir agua y electricidad en la parcela."),
    13: entry(
        "La pasarela de Cape Cross atraviesa una gran colonia reproductora de lobos marinos del Cabo y conduce a réplicas del padrão portugués. Es un espacio protegido, no una playa libre.",
        "Reúne observación de fauna, historia de navegación y memoria de una costa explotada durante siglos.",
        "Colonia, chacales ocasionales, pasarela interpretativa y monumentos; el número de animales varía por temporada.",
        "El pin coincide con Cape Cross Seal Reserve. Entrar por la puerta de la C34 y permanecer en la pasarela, como exige MEFT.",
        "Mañana, con ropa para viento, frío, olor intenso y salpicaduras.",
        "No entrar con perro, salirse de la pasarela ni acercarse a crías; omitirlo si el parque está cerrado."),
    14: entry(
        "Messum es una gran estructura volcánica erosionada del interior costero. El pin representa el objeto cartográfico, no una recepción: no hay carretera señalizada ni servicios en el cráter.",
        "Aporta geología, aislamiento y un paisaje real muy distinto de la foto genérica que antes compartía con Sandwich Harbour.",
        "Anillo montañoso erosionado, afloramientos volcánicos y planicie interior; las tres fotos son del propio Messum.",
        "El pin coincide con Messum Crater en Google Maps. Obtener permiso, llevar track fiable y entrar solo con 4x4 autónomo y otro vehículo.",
        "Jornada completa con luz, tiempo seco y margen de combustible y agua.",
        "Descartarlo sin permiso, track, convoy, satélite o autonomía; no crear nuevas roderas sobre la costra."),
    15: entry(
        "White Lady es un panel de arte rupestre en el abrigo Maack, dentro de la garganta Tsisab del Brandberg. Se alcanza a pie con guía oficial; el nombre histórico no describe con certeza la figura.",
        "La caminata permite ver el arte en su paisaje y corregir interpretaciones coloniales que lo atribuían a culturas mediterráneas.",
        "Figura central, órices y otras siluetas del panel; está prohibido tocar, mojar o alterar la pintura.",
        "El pin coincide con La Dama de Blanco en Google Maps y marca el panel, no el aparcamiento. Registrarse en la entrada y seguir al guía.",
        "Primera hora, antes del calor; prever al menos 45–60 minutos de marcha por sentido según ritmo.",
        "No ir con calor extremo, movilidad insuficiente, sin guía o si no se ha confirmado la custodia del perro."),
    16: entry(
        "El centro de visitantes organiza recorridos guiados por los petroglifos de Twyfelfontein o /Ui-//aes, inscritos por UNESCO. Las imágenes documentan prácticas rituales y económicas de cazadores-recolectores.",
        "Ofrece una de las lecturas más completas de arte rupestre del viaje con gestión e interpretación local.",
        "Grabados de jirafas, rinocerontes, huellas y otros animales sobre arenisca; cada circuito muestra paneles diferentes.",
        "El pin coincide con Twyfelfontein Visitors Centre. Pagar en recepción, usar guía y caminar solo por la ruta asignada.",
        "Primera hora o última visita disponible, con calzado firme y agua.",
        "No entrar sin guía, tocar los paneles o improvisar atajos; confirmar la política de mascotas antes de llegar."),
    17: entry(
        "Palmwag Lodge es la base verificable junto a una extensa concesión comunal de paisaje árido y fauna libre. Ver elefantes o rinocerontes requiere actividad autorizada y nunca está garantizado.",
        "Permite comprender cómo turismo, concesiones y conservancies financian parte del seguimiento de fauna del noroeste.",
        "Valle del Uniab, palmeras, geología rojiza y fauna si aparece; la ficha no promete rastrear animales por libre.",
        "El pin coincide con Palmwag Lodge en Google Maps. Comprar el permiso correspondiente y contratar guía para zonas restringidas.",
        "Dos noches si se reserva actividad; evitar las horas de más calor.",
        "Omitir salidas sin permiso o guía y no contar con recarga de agua o aceptación del perro sin confirmación escrita."),
    18: entry(
        "Ugab Gate es la entrada sur concreta a Skeleton Coast Park. Desde aquí comienza un largo corredor de grava, niebla y litoral desértico; gran parte del norte permanece restringida.",
        "Convierte una idea difusa de la costa en una decisión real de acceso, horario, combustible y pernocta.",
        "Puerta, paisaje de dunas bajas, costa y restos dispersos; no todos los pecios famosos están en el tramo público.",
        "El pin coincide con Ugab Gate en Google Maps. Confirmar en MEFT la ruta permitida, horario, reserva y puerta de salida.",
        "Entrar temprano y con combustible suficiente para completar el itinerario autorizado con luz.",
        "No entrar tarde, sin reserva cuando sea exigida, con perro, cobertura insuficiente o esperando un safari convencional."),
    19: entry(
        "La charca iluminada de Okaukuejo es un punto concreto y observable de Etosha, junto al resort. La presencia de elefantes, rinocerontes y otros animales cambia por hora y estación.",
        "Permite observar fauna desde un recinto estable incluso después de cerrar las carreteras del parque.",
        "Charca, torre y fauna de paso; conviene alternarla con recorridos diurnos autorizados dentro de Etosha.",
        "El pin coincide con Okaukuejo Waterhole. Reservar alojamiento o acceso, respetar puertas y resolver el perro fuera del parque.",
        "Estación seca y franjas de amanecer, atardecer y noche, sin garantía de especies.",
        "Descartarlo sin reserva o custodia canina real; nunca salir del vehículo fuera de las zonas autorizadas."),
    20: entry(
        "Van Zyl's Pass es una pista rocosa remota del Kaokoveld que desciende hacia el Marienfluss. La ficha ya no presenta como norma legal un sentido único que las fuentes oficiales consultadas no publican.",
        "Es un reto técnico genuino y un mirador sobre un paisaje casi sin infraestructuras.",
        "Escalones de roca, laderas y vegetación adaptada; una sola foto muestra la pista porque no se rellenó con imágenes de otros lugares.",
        "El pin coincide con Van Zyl's Pass en Google Maps. Confirmar sentido recomendado y estado localmente, ir en convoy y reconocer a pie cada obstáculo.",
        "Solo con varios días secos, luz completa, conductores expertos y comunicación satelital.",
        "Descartarlo sin reductora, protección, rescate, autonomía o alternativa; no usarlo para aprender conducción 4x4."),
    21: entry(
        "Epupa es una sucesión de saltos del Kunene entre palmeras makalani, en la frontera con Angola. El mirador evita confundir la cascada con cualquiera de los campings ribereños.",
        "Combina un paisaje fluvial inesperado con una parada larga después de las pistas del Kaokoland.",
        "Canales, caídas, palmeras y garganta; el caudal varía mucho y el río alberga cocodrilos.",
        "El pin coincide con Epupa Falls Viewpoint. Preguntar por senderos, guía y límites de propiedad antes de caminar.",
        "Mañana o atardecer, con dos noches para descansar y explorar sin prisa.",
        "No bañarse ni acercar el perro a la orilla; evitar bordes mojados, crecidas y senderos no autorizados."),
    22: entry(
        "Ruacana Falls depende del caudal liberado en un río regulado por infraestructura hidroeléctrica. El mirador queda junto al complejo fronterizo y puede requerir identificarse ante los agentes.",
        "Cuando lleva agua ofrece otra lectura del Kunene y, aun seca, ayuda a entender la presa y la frontera.",
        "Salto rocoso y garganta; no se promete una cortina de agua permanente ni se reutilizan fotos de Epupa.",
        "El pin coincide con Viewpoint to Ruacana Falls. Visit Namibia indica avisar en el puesto fronterizo antes de ir al aparcamiento.",
        "Tras confirmar caudal, horario y acceso; mejor con luz lateral.",
        "Omitirlo si frontera o seguridad niegan el paso, si no hay caudal y no interesa la infraestructura, o con roca mojada."),
    23: entry(
        "El Independence Memorial Museum recorre represión colonial, guerra de liberación y camino a la independencia. Es la ancla cultural de Windhoek; la ciudad sigue siendo la principal base logística.",
        "Da contexto histórico nacional antes de visitar Waterberg, Lüderitz o los antiguos enclaves coloniales.",
        "Tres galerías, vistas urbanas y el conjunto cercano de Christuskirche y Alte Feste.",
        "El pin coincide con Independence Museum en Google Maps. Consultar el horario oficial y separar la visita de las gestiones urbanas.",
        "Entre semana por la mañana, dejando margen para la exposición completa.",
        "Omitirlo si está cerrado; no sustituir sus contenidos por una panorámica superficial de la ciudad."),
    24: entry(
        "La recepción de NWR es la base real para los senderos y actividades del Waterberg Plateau Park. El macizo también conserva la memoria de la batalla de 1904 y la persecución posterior.",
        "Combina caminata, geología, conservación y una historia inseparable del genocidio ovaherero y nama.",
        "Escarpe de arenisca, senderos cortos, cementerio y fauna en recorridos autorizados sobre la meseta.",
        "El pin coincide con Waterberg Camp - NWR (Reception). Registrar la entrada y reservar por separado drives o travesías.",
        "Mañana fresca; dedicar una noche si se combina historia y senderismo.",
        "No entrar con perro, caminar fuera de ruta, ni hacer senderos largos con calor, incendio o sin reserva."),
}


PHOTOS = {
    1: [
        commons("Fish River Canyon Namibia.jpg", "Thomas Schoch · CC BY-SA 3.0", "Vista del Fish River Canyon desde el borde superior."),
        commons("Namibia Fischfluss-Canyon 18.jpg", "Zairon · CC BY-SA 4.0", "Meandros y paredes estratificadas del propio cañón."),
        commons("Namibia Fish River Canyon top-down-view.jpg", "Ralf Junghanns · CC BY-SA 3.0", "Vista vertical hacia el cauce del Fish River."),
    ],
    2: [
        commons("Quiver Tree Forest Namibia.jpg", "Falcodigiada · CC BY-SA 4.0", "Kokerbooms del bosque cercano a Keetmanshoop."),
        commons("Quiver Tree Forest (2006) 01.jpg", "LBM1948 · CC BY-SA 4.0", "Llanura de Gariganus cubierta por kokerbooms."),
        commons("RK 1910 R0010725 Pano Giants Playground.jpg", "Reinhard Kraasch · CC BY-SA 4.0", "Bloques de dolerita de Giant's Playground, la segunda visita del recinto."),
    ],
    3: [
        commons("NA-garub-wildpferde-1.jpg", "Bgabel · CC BY-SA 3.0", "Caballos ferales fotografiados en Garub."),
        commons("Desert Horses close to Aus - Namibia.jpg", "Raymond June · CC BY 2.0", "Caballos junto a la antigua estación ferroviaria de Garub."),
        commons("Wild Horses and Gemsbok (18706192823).jpg", "David Stanley · CC BY 2.0", "Caballos y órix comparten el abrevadero de Garub."),
    ],
    4: [
        commons("Lüderitz Waterfront 3.jpg", "Zairon · CC BY-SA 4.0", "Waterfront y puerto de Lüderitz."),
        commons("NA-luederitz-waterfront-2.jpg", "Balou46 · CC BY-SA 4.0", "Bahía e instalaciones portuarias de Lüderitz."),
        commons("Lüderitz Shark Island auf die Waterfront 1.jpg", "Zairon · CC BY-SA 4.0", "El waterfront visto desde Shark Island."),
    ],
    5: [
        commons("Kolmanskop, Namibia-1.jpg", "Sara&Joachim · CC BY-SA 2.0", "Arena acumulada dentro de una vivienda de Kolmanskop."),
        commons("Kolmanskop hospital, Lüderitz (Namibia).jpg", "Olga Ernst · CC BY-SA 4.0", "Antiguo hospital del poblado minero."),
        commons("Kolmanskop, Namibia (3147328441).jpg", "Joachim Huber · CC BY-SA 2.0", "Interior abandonado en el recinto de Kolmanskop."),
    ],
    6: [
        commons("Duna 45, Sossusvlei, Namibia, 2018-08-06, DD 009.jpg", "Diego Delso · CC BY-SA 4.0", "Dune 45 y su cresta accesible desde el aparcamiento."),
        commons("Dune 45 Panorama.jpg", "Daniel Kraft · CC BY-SA 3.0", "Panorámica de Dune 45 y las dunas vecinas."),
        commons("006 Dune 45 in Sossusvlei at sunrise Photo by Giles Laurent.jpg", "Giles Laurent · CC BY-SA 4.0", "Dune 45 al amanecer."),
    ],
    7: [
        commons("Dead Vlei, Sossusvlei, Namibia, 2018-08-06, DD 101-104 PAN.jpg", "Diego Delso · CC BY-SA 4.0", "Panorámica de Deadvlei con los antiguos camelthorn."),
        commons("Dead Vlei, Sossusvlei, Namibia, 2018-08-06, DD 086.jpg", "Diego Delso · CC BY-SA 4.0", "Tronco conservado por la aridez en la cubeta clara."),
        commons("054e Dead camel thorn tree in Deadvlei Photo by Giles Laurent.jpg", "Giles Laurent · CC BY-SA 4.0", "Camelthorn ennegrecido ante las dunas de Deadvlei."),
    ],
    8: [
        commons("Namibia Kuiseb-Canyon 11.jpg", "Zairon · CC BY-SA 4.0", "Valle del Kuiseb desde la carretera del Namib-Naukluft."),
        commons("Namibia Kuiseb-Canyon 09.jpg", "Zairon · CC BY-SA 4.0", "Paredes y cauce efímero del Kuiseb."),
        commons("Namibia Kuiseb-Canyon 08.jpg", "Zairon · CC BY-SA 4.0", "Otro ángulo del cañón; no es Welwitschia Drive."),
    ],
    9: [
        commons("Greater Flamingos (19186336580).jpg", "David Stanley · CC BY 2.0", "Flamencos en los bancos de Lagoon Promenade, Walvis Bay."),
        commons("Flying flamingo at Walvis bay lagoon.jpg", "Ndatipo1998 · CC BY-SA 4.0", "Flamenco en vuelo sobre la laguna de Walvis Bay."),
        commons("Laagon.jpg", "Nhinda · CC BY-SA 4.0", "Vista amplia del humedal urbano de Walvis Bay."),
    ],
    10: [
        commons("Sandwich Harbour (2006) 24.jpg", "LBM1948 · CC BY-SA 4.0", "Dunas y playa en Sandwich Harbour."),
        commons("Sandwich Harbour (2006) 06.jpg", "LBM1948 · CC BY-SA 4.0", "Laguna y dunas del propio humedal."),
        commons("Sandwich Harbour (2006) 21.jpg", "LBM1948 · CC BY-SA 4.0", "Pelícanos sobre la laguna de Sandwich Harbour."),
    ],
    11: [
        commons("Jetty, Swakopmund, Namibia, 2018-08-04, DD 68-70 HDR.jpg", "Diego Delso · CC BY-SA 4.0", "Jetty Pier de Swakopmund vista desde la playa."),
        commons("Swakopmund Jetty HDR.jpg", "Daniel Kraft · CC BY-SA 3.0", "Pasarela de la Jetty orientada hacia el Atlántico."),
        commons("Mole, Jetty and Lighthouse Swakopmund, Namibia.jpg", "Olga Ernst · CC BY-SA 4.0", "Mole, Jetty y faro en el frente marítimo."),
    ],
    12: [
        commons("Spitzkoppe Rock Arch Panorama with even sky.jpg", "Daniel Kraft · CC BY-SA 3.0", "Arco de roca con Spitzkoppe al fondo."),
        commons("Spitzkoppe Rock Arch Viewpoint.jpg", "Daniel Kraft · CC BY-SA 3.0", "Vista del macizo desde Rock Arch."),
        commons("Spitzkoppe, Namibia, 2018-08-04, DD 14-22 PAN.jpg", "Diego Delso · CC BY-SA 4.0", "Panorámica del paisaje granítico de Spitzkoppe."),
    ],
    13: [
        commons("CC - Large Cape fur seal colony at Cape Cross, Namibia, 2007.jpg", "Josep M. Gracia · CC BY-SA 4.0", "Vista general de la colonia de Cape Cross."),
        commons("CC - Visitors observing the Cape fur seal colony at Cape Cross, Namibia, 2007.jpg", "Josep M. Gracia · CC BY-SA 4.0", "Pasarela de observación dentro de la reserva."),
        commons("CC - Black-backed jackal among Cape fur seals at Cape Cross, Namibia, 2007.jpg", "Josep M. Gracia · CC BY-SA 4.0", "Chacal de lomo negro entre lobos marinos del Cabo."),
    ],
    14: [
        commons("Inside Messum Crater-02.jpg", "Hans Stieglitz · CC BY-SA 3.0", "Planicie y relieve interior de Messum Crater."),
        commons("Inside Messum Crater-01.jpg", "Hans Stieglitz · CC BY-SA 3.0", "Afloramientos dentro de la estructura volcánica."),
        commons("Krajina v oblasti Messum Crater - panoramio (4).jpg", "Martin Cígler · CC BY-SA 3.0", "Paisaje del área de Messum Crater."),
    ],
    15: [
        commons("Brandberg white lady-namibia - panoramio.jpg", "Jola Sik · CC BY 3.0", "Panel conocido como White Lady en el Brandberg."),
        commons("Weiße Dame Brandberg.JPG", "Harald Süpfle · CC BY-SA 2.5", "Detalle de la figura y del conjunto pintado."),
        commons("DSC06188 Namibia L4 White Lady Brandberg (49568783511).jpg", "Heribert Bechen · CC BY-SA 2.0", "Abrigo y entorno inmediato de la visita White Lady."),
    ],
    16: [
        commons("Twyfelfontein Rock Engraving, Namibia.jpg", "Jean & Nathalie · CC BY 2.0", "Grabado rupestre en Twyfelfontein."),
        commons("Giraffe, Twyfelfontein.jpg", "Schnobby · CC BY-SA 3.0", "Jirafa grabada sobre arenisca en /Ui-//aes."),
        commons("Animal Rock Engravings by Bushmen (23908707618).jpg", "Sonse · CC BY 2.0", "Conjunto de figuras animales en el sitio UNESCO."),
    ],
    17: [
        commons("020525081Namibia.JPG", "Graf-flugplatz · CC BY-SA 3.0", "Cauce del Uniab en Palmwag."),
        commons("Palmwag Sunset - panoramio.jpg", "eftejo · CC BY 3.0", "Atardecer en el paisaje de Palmwag."),
        commons("Gemsbok, Palmwag, Namibia (3927374692).jpg", "Frank Vassen · CC BY 2.0", "Órix fotografiado en Palmwag; la fauna nunca está garantizada."),
    ],
    18: [
        commons("Skeleton Coast Dunes.jpg", "Daniel Kraft · CC BY-SA 3.0", "Dunas y vegetación dispersa dentro de Skeleton Coast Park."),
        commons("Namib Skeleton Coast Park, Namibia (3046182890).jpg", "Joachim Huber · CC BY-SA 2.0", "Paisaje costero del parque al que da acceso Ugab Gate."),
        commons("Skeleton Coast, Namibia (17105818219).jpg", "Domenico Convertini · CC BY-SA 2.0", "Litoral desértico dentro de Skeleton Coast Park."),
    ],
    19: [
        commons("Waterhole Okaukuejo Camp in Etosha National Park.jpg", "Hka1987 · CC0", "Charca de Okaukuejo al amanecer."),
        commons("Oryx at the Okaukuejo Waterhole, Etosha National Park, Namibia.jpg", "Christoph Strässler · CC BY-SA 2.0", "Órix en la charca de Okaukuejo."),
        commons("Giraffe at the Okaukuejo Waterhole, Etosha National Park, Namibia.jpg", "Christoph Strässler · CC BY-SA 2.0", "Jirafa observada desde el recinto de la charca."),
    ],
    20: [
        commons("Van Zyl´s Pass.jpg", "Hans Stieglitz · CC BY-SA 3.0", "Vehículo descendiendo un escalón de roca en Van Zyl's Pass."),
        commons("Commiphora multijuga 2463.jpg", "SAplants · CC BY-SA 4.0", "Commiphora en la ladera del propio Van Zyl's Pass."),
        commons("Sterculia africana 2469.jpg", "SAplants · CC BY-SA 4.0", "Vegetación adaptada fotografiada en el paso."),
    ],
    21: [
        commons("Epupa Falls 2.jpg", "Dr. Thomas Wagner · CC BY-SA 3.0", "Canales y saltos de Epupa en el Kunene."),
        commons("Epupa falls 1.jpg", "Hans Hillewaert · CC BY-SA 3.0", "Caída principal de Epupa Falls."),
        commons("Epupafaelle3.JPG", "Harald Bungsche · CC BY-SA 2.5", "Garganta aguas abajo de la cascada."),
    ],
    22: [
        commons("Namibia Ruacana Falls.jpg", "Rubend nazario · dominio público", "Ruacana Falls con caudal visible desde el lado namibio."),
        commons("Ruacana Falls at High Water from distance in 03-2011 by Tom Jakobi.JPG", "Tom Jakobi / ImperatoM · CC BY-SA 3.0", "Vista distante de Ruacana durante una crecida de 2011."),
        commons("Ruacana.jpg", "Dr. Thomas Wagner · CC BY-SA 3.0", "Garganta y saltos de Ruacana vistos desde Namibia."),
    ],
    23: [
        commons("Windhuk Christuskirche & Independence Memorial Museum 3.jpg", "Zairon · CC BY-SA 4.0", "Independence Memorial Museum y Christuskirche."),
        commons("Unabhängigkeits-Gedenkmuseum Windhoek, Luftaufnahme (2017).jpg", "Olga Ernst & Hp.Baumeler · CC BY-SA 4.0", "Vista aérea del museo en el centro de Windhoek."),
        commons("Windhuk Independence Memorial Museum Blick auf den Tintenpalast 2.jpg", "Zairon · CC BY-SA 4.0", "Parlamento visto desde el Independence Memorial Museum."),
    ],
    24: [
        commons("Waterberg Plateau National Park, Namibia (16579001653).jpg", "Domenico Convertini · CC BY-SA 2.0", "Escarpe de arenisca en Waterberg Plateau Park."),
        commons("Waterberg, Namibia Luftaufnahme von Osten.jpg", "jthetzel · CC BY 2.0", "Vista aérea del Waterberg desde el este."),
        commons("Waterberg Fels.jpg", "Ikiwaner · GFDL 1.2", "Afloramiento de arenisca del Waterberg."),
    ],
}


HISTORY = {
    "historia_resumen": "La historia de Namibia enlaza milenios de ocupación cazadora-recolectora y pastoril con redes nama, ovaherero, damara y ovambo, la colonización alemana y el genocidio de 1904–1908. Sudáfrica ocupó después el territorio, impuso segregación y apartheid y resistió durante décadas la descolonización exigida por la ONU. La movilización nacionalista, la guerra y la negociación desembocaron en elecciones supervisadas por UNTAG y la independencia del 21 de marzo de 1990. Twyfelfontein, Lüderitz, Waterberg, Windhoek y las conservancies permiten leer esa historia en lugares concretos y también sus desigualdades persistentes.",
    "historia_secciones": [
        ["Cazadores-recolectores, pastores y arte rupestre", "Twyfelfontein y el Brandberg conservan registros materiales de comunidades cazadoras-recolectoras que usaron el territorio durante milenios; UNESCO relaciona los grabados de /Ui-//aes con prácticas rituales y económicas, no con una cultura detenida en el tiempo. Posteriormente convivieron y se desplazaron comunidades khoekhoe, damara y de lenguas bantú. La aridez condicionó movilidad, pastoreo, intercambio y el valor político de fuentes, ríos efímeros y corredores estacionales."],
        ["Redes nama, ovaherero, ovambo y oorlam", "Antes de la conquista europea no existía un Estado namibio único. En el centro y el sur, grupos nama, ovaherero, damara y oorlam negociaron tierra, ganado y rutas comerciales, y también combatieron entre sí. Al norte se consolidaron reinos y autoridades ovambo con economías agrícolas y ganaderas conectadas a Angola. Comerciantes, misioneros y armas de fuego alteraron estas relaciones durante el siglo XIX, pero no convirtieron a las sociedades locales en actores pasivos."],
        ["Dominio alemán y genocidio, 1884–1908", "Alemania proclamó el África del Sudoeste Alemana en 1884 y amplió el control mediante tratados desiguales, expropiación de tierras, trabajo coercitivo y fuerza militar. Las guerras iniciadas en 1904 contra los ovaherero y después contra los nama derivaron en órdenes de expulsión, muerte en el Omaheke, campos de concentración y trabajo forzado, incluido Shark Island. Alemania reconoce hoy estos hechos, desde la perspectiva actual, como genocidio; el contenido evita cerrar como resuelto un proceso de reparación que sigue siendo discutido por comunidades descendientes."],
        ["Ocupación sudafricana, mandato y apartheid", "Fuerzas sudafricanas ocuparon el territorio durante la Primera Guerra Mundial y la Sociedad de Naciones concedió a Sudáfrica un mandato. Tras 1945, Pretoria intentó conservar el control pese a la supervisión internacional y extendió reservas, segregación y, desde 1948, estructuras de apartheid. Líderes como Hosea Kutako llevaron peticiones a la ONU; las decisiones internacionales fueron desmontando la legitimidad del mandato, aunque la administración sudafricana continuó durante décadas."],
        ["Nacionalismo, guerra y negociación", "SWAPO se formó en 1960 y su brazo armado inició la lucha en 1966, dentro de un conflicto regional conectado con Angola y la Guerra Fría. La Resolución 435 del Consejo de Seguridad, aprobada en 1978, estableció el marco para una transición supervisada, pero su aplicación se demoró hasta 1989. UNTAG vigiló el alto el fuego y las elecciones constituyentes; SWAPO obtuvo mayoría sin alcanzar por sí sola los dos tercios, y la Constitución negociada entró en vigor con la independencia el 21 de marzo de 1990."],
        ["Democracia, conservación y desigualdad", "Desde 1990 Namibia ha mantenido elecciones multipartidistas e instituciones constitucionales, aunque SWAPO ha gobernado de forma continuada. Netumbo Nandi-Ndaitwah asumió la presidencia en marzo de 2025 como primera mujer en el cargo. Minería, servicios, agricultura y turismo sostienen la economía; las conservancies comunales han creado ingresos y capacidad local de gestión, pero no borran conflictos sobre tierra y fauna. El Banco Mundial sigue describiendo desigualdad, desempleo y vulnerabilidad climática como problemas estructurales ligados también al legado colonial y del apartheid."],
    ],
    "historia_fuentes": [
        ["UNESCO · Twyfelfontein o /Ui-//aes", "https://whc.unesco.org/en/list/1255"],
        ["Parliament of Namibia · Overview", "https://www.parliament.gov.na/?page_id=4040"],
        ["Ministerio de Justicia de Namibia · Estado e independencia", "https://www.moj.gov.na/about-namibia1"],
        ["Naciones Unidas en Namibia · camino a la independencia", "https://namibia.un.org/en/175155-uns-role-namibian-independence"],
        ["Ministerio alemán de Exteriores · reconocimiento del genocidio", "https://www.auswaertiges-amt.de/en/newsroom/news/2463598-2463598"],
        ["Banco Mundial · panorama de Namibia", "https://www.worldbank.org/ext/en/country/namibia"],
    ],
}


HISTORY_NOTES = [
    "Se elimina la etiqueta debatible de «primer genocidio del siglo XX» y se describen hechos, responsables, víctimas y reconocimiento actual.",
    "La administración sudafricana se separa del mandato de la Sociedad de Naciones y de la disputa posterior ante Naciones Unidas.",
    "La sección contemporánea incorpora el cambio presidencial de marzo de 2025 y evita presentar estabilidad, conservación o riqueza como ausencia de desigualdad.",
]


VERIFIED_SOURCES = [
    ["MHAISS · fact sheet oficial de visado y puestos autorizados", "https://eservices.mhaiss.gov.na/form/FactSheetVisaRequirementstoNamibia.pdf"],
    ["MHAISS · portal oficial de e-visa y visado a la llegada", "https://eservices.mhaiss.gov.na/visaonarrival"],
    ["Government Gazette 8877 · tasas de parques desde abril de 2026", "https://www.lac.org.na/laws/2026/8877.pdf"],
    ["MEFT · permisos, oficinas y prohibición de mascotas en parques", "https://www.meft.gov.na/frequently-asked-questions/what-are-the-entry-permit-requirements-for-the-various-parks-in-namibia-/136/"],
    ["NWR · reservas de alojamientos y campings", "https://www.nwr.com.na/"],
    ["CRAN · comunicados oficiales sobre la licencia de Starlink", "https://www.cran.na/media-statements/?cp=2"],
    ["NCAA · requisitos oficiales para drones y viajeros extranjeros", "https://ncaa.com.na/"],
    ["Namibia Trade Information Portal · importación de mascotas", "https://namibiatradeportal.gov.na/trade-goods/procedure-details/view_express_entity/1173"],
    ["Veterinary Association of Namibia · documentación y analíticas para mascotas", "https://www.van.org.na/section.php?menuid=52&secid=52"],
    ["Embajada de España en Windhoek · contacto y emergencia consular", "https://www.exteriores.gob.es/Embajadas/windhoek/es/Embajada/Paginas/Contacto.aspx"],
    ["Embajada de España en Windhoek · recomendaciones de viaje", "https://www.exteriores.gob.es/Embajadas/windhoek/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"],
    ["UNESCO · Twyfelfontein o /Ui-//aes", "https://whc.unesco.org/en/list/1255"],
    ["UNESCO · Namib Sand Sea", "https://whc.unesco.org/en/list/1430"],
    ["Tracks4Africa · ficha de Van Zyl's Pass", "https://tracks4africa.co.za/listings/item/w207682/van-zyls-pass/"],
]


REPLACEMENTS = {
    "Namibia es el último país del bucle y, con Sudáfrica, el mejor preparado del continente para viajar en vehículo propio: pistas de grava bien mantenidas, una red de campings pensada para overlanders, agua del grifo potable y talleres de nivel europeo.":
        "Namibia cierra el bucle entre Sudáfrica y Angola. Su red principal y su oferta de servicios facilitan el viaje en vehículo propio, pero las pistas remotas, el combustible, el agua y las comunicaciones deben planificarse sin asumir disponibilidad.",
    "Es también, con diferencia, el país donde más 4x4 de verdad hay que hacer":
        "Aquí se concentran algunos de los tramos 4x4 más exigentes del itinerario",
    "Es también, con diferencia, <strong>el país donde más 4x4 de verdad hay que hacer</strong>":
        "Aquí se concentran <strong>algunos de los tramos 4x4 más exigentes del itinerario</strong>",
    "Verificar si el puesto TERRESTRE de Noordoewer lo emite.":
        "El fact sheet oficial incluye Noordoewer entre los puestos que aceptan e-visa y visado a la llegada; Ruacana solo acepta e-visa.",
    "Confirmar expresamente que el puesto TERRESTRE de Noordoewer emite el visado a la llegada y no solo los aeropuertos: de eso depende toda la entrada.":
        "El listado oficial incluye Noordoewer para e-visa y visado a la llegada. Si se prevé Ruacana, tramitar antes la e-visa: allí no se admite solicitar el visado al llegar.",
    "Permitido en las concesiones comunales del Damaraland y el Kaokoland, en Spitzkoppe, en las granjas privadas y en las ciudades.":
        "Fuera de los parques no hay una regla única: confirmar por escrito la admisión con cada concesión, camping, granja o monumento.",
    "Uno de los países más seguros de África; el riesgo real y estadísticamente dominante es la conducción en grava.":
        "Separar el riesgo vial de los hurtos urbanos y revisar avisos oficiales antes de cada tramo.",
    "Starlink NO disponible (licencia denegada marzo 2026, apelación desestimada junio 2026).":
        "Starlink no dispone de licencia: CRAN confirmó en junio de 2026 la desestimación de las solicitudes de reconsideración.",
    "Dormir dentro de la puerta de Sesriem es la única forma de estar en Dune 45 al amanecer.":
        "Dormir dentro de la puerta de Sesriem facilita el acceso antes que desde alojamientos exteriores; confirmar los horarios vigentes.",
    "dormir dentro de la puerta de Sesriem es lo único que permite estar en Dune 45 al amanecer — desde fuera se llega siempre tarde.":
        "dormir dentro de la puerta de Sesriem permite entrar antes que desde alojamientos exteriores; confirmar los horarios vigentes.",
    "Namibia fue escenario del primer genocidio del siglo XX, perpetrado por Alemania contra los pueblos herero y nama entre 1904 y 1908, y pasó después a ser administrada durante 75 años por Sudáfrica bajo un régimen que extendió allí su propio apartheid, hasta lograr la independencia en 1990 como uno de los últimos países africanos en descolonizarse; hoy es uno de los países más estables, mejor gestionados y menos poblados del continente, con una economía basada en minería y en un turismo de naturaleza de primer nivel.":
        "La colonización alemana desembocó en el genocidio contra los pueblos ovaherero y nama entre 1904 y 1908. Tras la ocupación sudafricana y décadas de segregación y apartheid, la transición supervisada por la ONU condujo a la independencia en 1990; el país actual combina instituciones multipartidistas, economía minera y turística y desigualdades persistentes.",
    "Donde se reservan los campings de Etosha, Sesriem, Terrace Bay y Torra Bay y donde se tramitan los PERMISOS ESPECIALES (Skeleton Coast norte, Welwitschia Drive).":
        "NWR gestiona reservas de sus alojamientos y campings. Los permisos de parques y de zonas especiales corresponden al MEFT, que advierte expresamente que NWR no los expide.",
    "Oficina del MEFT/NWR en Swakopmund":
        "Oficina del MEFT en Swakopmund",
    "El público Windhoek Central y los privados Lady Pohamba y Roman Catholic Hospital son la referencia real del país; nivel notablemente superior al resto del corredor salvo Sudáfrica. Coordenada urbana aproximada.":
        "Windhoek Central, Lady Pohamba y Roman Catholic Hospital son referencias urbanas que deben confirmarse con el seguro antes de una derivación. Coordenada urbana aproximada.",
    "Clínica privada de referencia de toda la costa, la mejor opción entre Windhoek y el norte. Coordenada urbana aproximada.":
        "Clínica privada de Swakopmund; confirmar especialidad, admisión y cobertura con el seguro antes de acudir. Coordenada urbana aproximada.",
    "ÚLTIMO SUMINISTRO SEGURO antes del Kaokoland profundo. Opuwo es la capital del Kunene y la última plaza con banco, supermercado y taller. Palmwag tiene surtidor de la concesión. A partir de aquí, garrafas.":
        "Opuwo es la principal base de banco, supermercado y taller antes de las pistas del Kaokoland. Palmwag y Sesfontein son candidatos de combustible, pero hay que confirmar existencias y entrar con autonomía completa y margen.",
    "por 1.850-2.250 N$/persona":
        "con tarifa por persona a confirmar",
    "unos 1.850-2.250 N$ por persona":
        "un precio que debe confirmarse con el operador",
    "uno de los pasos 4x4 más duros de África y un rito de paso del overland africano":
        "un paso 4x4 remoto y técnico que exige experiencia, convoy y plan de retirada",
    "es una de las mejores rutas 4x4 organizadas del país":
        "es una ruta 4x4 organizada que exige reserva y condiciones confirmadas",
    "vistas de las mejores del país":
        "vistas amplias sobre el escarpe",
    "Residencias caninas profesionales solo en WINDHOEK y SWAKOPMUND.":
        "No se ha verificado una red de residencias en las puertas de los parques; buscar y reservar una custodia concreta antes de entrar.",
    "que son las dos únicas plazas con kennels profesionales":
        "con un establecimiento concreto previamente comprobado",
    "Namibia tiene cientos de guest farms privadas con fauna propia (órix, kudú, cebra, a veces guepardo o rinoceronte) donde el perro sí entra si se pacta con el propietario: es el modelo alternativo a Etosha.":
        "Las guest farms tienen normas individuales y la presencia de fauna puede hacer incompatible la entrada del perro; solo cuentan como alternativa cuando una propiedad concreta lo confirme por escrito.",
    "Sin restricciones específicas conocidas; abundante alojamiento pet-friendly y veterinarios de nivel europeo en Windhoek y Swakopmund.":
        "En ciudad siguen rigiendo las normas de cada alojamiento y espacio; seleccionar previamente hospedaje y veterinario que confirmen el servicio necesario.",
    "Malaria: presente de forma estacional en el NORTE del país —franja de Etosha, Kunene, Kavango y Zambezi— sobre todo en la estación húmeda (noviembre-junio). El centro, el sur y toda la costa están libres. Valorar profilaxis con Sanidad Exterior solo para el tramo norte (Etosha, Kaokoland, Epupa).":
        "Malaria: el riesgo cambia por región y estación. Consultar Sanidad Exterior con el itinerario y fechas exactos; aplicar medidas antimosquitos y no convertir una delimitación genérica en consejo médico individual.",
    "Regla: 4-5 litros por persona y día en ruta, más el perro, y no caminar en dunas entre las 10 y las 16 horas.":
        "Dimensionar agua de consumo y una reserva de emergencia según personas, perro, temperatura y días hasta el siguiente punto confirmado; evitar actividad exigente con calor fuerte.",
    "Sanidad de primer nivel para estándares africanos:":
        "Centros de referencia en la planificación:",
    "Veterinarios de nivel europeo en Windhoek, Swakopmund y Otjiwarongo. A partir de Opuwo, nada: llevar botiquín veterinario completo con antibiótico de amplio espectro, antiinflamatorio, suero y material de sutura.":
        "Preseleccionar veterinarios en Windhoek, Swakopmund y Otjiwarongo y confirmar atención antes del noroeste. El botiquín y cualquier medicamento deben acordarse con el veterinario habitual; no improvisar antibióticos ni suturas.",
    "El peligro real, medido en muertos, es LA CARRETERA: el país pierde entre 400 y 450 personas al año en accidentes sobre una población de 2,6 millones, una tasa varias veces superior a la europea, y los vuelcos en grava son un riesgo grave y repetido para visitantes.":
        "La carretera merece un protocolo propio: las salidas de vía y los vuelcos en grava son un riesgo grave, distinto de los hurtos urbanos.",
    "GRAVA, EL RIESGO NÚMERO UNO: el límite legal en pista sin asfaltar es 80 km/h y los overlanders experimentados recomiendan 70.":
        "GRAVA: respetar la señalización y reducir velocidad por debajo del límite cuando lo exijan corrugado, carga, visibilidad o adherencia.",
    "Adelantamientos en las B roads asfaltadas (sobre todo la B1 y la B2): las colisiones frontales por adelantar sin visibilidad son la segunda causa de siniestro grave del país.":
        "Adelantamientos en las B roads asfaltadas (sobre todo la B1 y la B2): no adelantar sin distancia de visibilidad y margen suficientes.",
    "No hay zonas excluidas por seguridad en el itinerario previsto.":
        "Revisar las recomendaciones oficiales y la situación local antes de fijar campamentos o recorridos urbanos.",
    "Prohibido en TODOS los parques nacionales sin excepción y sin servicio de guardería en las puertas: esto obliga a planificar, no a improvisar.":
        "El MEFT prohíbe mascotas en todos los parques nacionales. La custodia fuera del recinto debe quedar identificada y confirmada antes de llegar.",
    "Perro prohibido en todos los parques nacionales sin excepción y sin guardería en las puertas: hay que resolver Etosha (3 días) y Sossusvlei con residencia canina en Windhoek o Swakopmund, o con turnos entre los tres viajeros y los dos vehículos.":
        "El MEFT prohíbe mascotas en todos los parques nacionales: resolver Etosha y Sossusvlei mediante una custodia concreta previamente confirmada o mediante turnos entre viajeros y vehículos.",
    "Prohibido en TODOS los parques nacionales sin excepción ni guardería en puerta.":
        "El MEFT prohíbe mascotas en todos los parques nacionales; resolver una custodia concreta fuera antes de la visita.",
    "El MEFT no admite mascotas en ninguna área protegida namibia, sin excepciones y sin guardería en las puertas.":
        "El MEFT prohíbe mascotas en todos los parques nacionales. La fuente consultada no documenta guarderías en puerta.",
    "sin excepciones y sin guardería en las puertas.":
        "según la norma publicada por MEFT. La fuente consultada no documenta guarderías en puerta.",
    "Es una anomalía llamativa: el país mejor preparado del corredor para viajar en vehículo propio es también el único del bloque sur sin Starlink.":
        "La situación regulatoria puede cambiar antes del viaje y debe revalidarse con CRAN.",
    "la cobertura 4G namibia es buena en el eje principal":
        "la cobertura debe comprobarse por operador y tramo",
    "es el único tramo de la ruta con dos vehículos donde no habrá ninguna forma de pedir ayuda":
        "es una salvaguarda esencial en tramos sin cobertura terrestre confirmada",
    "Van Zyl's Pass, sentido único de verdad (blog de Tracks4Africa y foros 4x4 sudafricanos)":
        "Van Zyl's Pass, sentido recomendado por fuentes de viajeros (no presentado como norma legal)",
    "varios viajeros describen el momento de asomarse al valle desde lo alto del paso como lo mejor del viaje entero a Namibia — 60 km de hierba dorada entre montañas, con los «círculos de hadas» y ni un alma.":
        "los relatos consultados destacan la vista del Marienfluss desde lo alto del paso; es una valoración subjetiva, no una garantía de condiciones ni de aislamiento.",
    "Spitzkoppe como mejor vivac del país":
        "Spitzkoppe como camping muy citado por viajeros",
    "y que las comunidades locales tienen rastreadores que se contratan por poco dinero en Twyfelfontein o Palmwag.":
        "y que conviene contratar un rastreador local autorizado, confirmando disponibilidad y precio.",
    "el punto de acuerdo general es que Opuwo y Sesfontein son las últimas plazas fiables":
        "Opuwo y Sesfontein son las principales plazas candidatas, pero las existencias deben confirmarse",
    "La solución que aparece en los relatos de quienes viajan con perro por el sur de África es la misma que la nuestra: dejarlo en una residencia canina en Windhoek o Swakopmund durante los días de Etosha, y concentrar el viaje con perro en las concesiones comunales del Damaraland y el Kaokoland, donde la fauna es libre y las normas las pone la comunidad, no el Estado.":
        "Las opciones son una custodia concreta y reservada fuera del parque o turnos entre viajeros; en concesiones comunales tampoco se presupone la admisión, porque cada gestor fija sus normas.",
    "Carnet de conducir internacional obligatorio, junto con el nacional, en todos los controles.":
        "Llevar permiso nacional e internacional y confirmar su aceptación para cada conductor y vehículo antes del viaje.",
    "Tablas de arena, gato de alta elevación (tipo Hi-Lift o neumático), correa de remolque y pala: obligatorio para Sandwich Harbour, Sossusvlei y el Kaokoland.":
        "Equipo de recuperación adecuado al vehículo —tablas, pala, compresor y puntos de remolque— y formación para usarlo antes de entrar en arena o pasos técnicos.",
    "Windhoek tiene concesionarios oficiales de la mayoría de marcas y es la mejor plaza técnica entre Ciudad del Cabo y Luanda.":
        "Windhoek concentra talleres y algunos concesionarios; comprobar por adelantado la marca, el recambio y la capacidad que realmente se necesita.",
    "Sandwich Harbour (mareas) · Van Zyl's Pass (sentido único) · Skeleton Coast · Messum":
        "Sandwich Harbour (mareas) · Van Zyl's Pass (trazado a confirmar) · Skeleton Coast · Messum",
    "Puntos verificados o de referencia para esta recarga:":
        "Candidatos pendientes de auditoría operativa para esta recarga:",
    "Puntos y comentarios recientes verificados también en":
        "Consultar también comentarios recientes en",
    "AGUA DEL GRIFO POTABLE en las principales ciudades, algo excepcional en el corredor africano. Campings y lodges de todo el país permiten llenar el depósito de uso general con manguera: la infraestructura namibia está pensada para vehículos propios.":
        "El abastecimiento urbano y los campings son candidatos de recarga, no puntos verificados. No contar con ellos hasta comprobar potabilidad o uso permitido, acceso del vehículo, conexión, caudal, coste y autorización para llenar.",
    "Los campings de Etosha, Sesriem, Torra Bay y Terrace Bay tienen agua corriente (en la costa, salobre y solo de uso general). En el Kaokoland y el Marienfluss NO HAY AGUA: cargar todo lo necesario en Opuwo o Sesfontein y contar 5-6 días de autonomía.":
        "Etosha, Sesriem, Torra Bay, Terrace Bay, Opuwo y Sesfontein quedan como candidatos de recarga. No asumir disponibilidad, calidad ni permiso hasta la auditoría específica; entrar al Kaokoland con autonomía holgada.",
    "AGUA DEL GRIFO POTABLE en las principales ciudades, algo excepcional en todo el corredor africano: buena oportunidad para descansar del protocolo de potabilización. En el campo y en los campings remotos, tratarla.":
        "No dar por auditada la potabilidad urbana ni el agua de campings. Para beber, usar una fuente confirmada o tratarla; para ducha y lavado, verificar acceso, conexión, coste y permiso antes de planificar la recarga.",
    "Van Zyl's Pass es de SENTIDO ÚNICO (este→oeste) y no se debe entrar con un solo vehículo.":
        "Van Zyl's Pass suele recomendarse de este a oeste; no se presenta como norma legal hasta obtener una fuente oficial y no se debe entrar con un solo vehículo.",
    "SENTIDO ÚNICO DE ESTE A OESTE (bajando)":
        "TRAZADO HABITUAL DE ESTE A OESTE (a confirmar localmente)",
    "todos los relatos coinciden en que se baja de este a oeste y NUNCA se sube":
        "los relatos consultados recomiendan bajarlo de este a oeste; confirmar el trazado operativo antes de entrar",
    "confirmar el sentido único vigente y el estado del paso con":
        "confirmar la dirección práctica recomendada, el estado del paso y cualquier restricción vigente con",
    "Monumentos nacionales y sitios comunales, no parques: el perro entra en el recinto y en el camping, aunque la visita guiada al arte rupestre del Brandberg y a Twyfelfontein se hace a pie sin él.":
        "Monumentos y sitios con gestores distintos: no asumir que el perro entra. Confirmar por escrito recinto, camping y visita guiada en Spitzkoppe, Brandberg, Twyfelfontein, Epupa, Ruacana y Messum.",
    "NO SON PARQUES NACIONALES sino terreno comunal gestionado por conservancies: aquí sí se puede circular y acampar con el perro":
        "Son terrenos comunales y concesiones con normas propias: circular, acampar o entrar con perro requiere autorización del gestor",
    "la laguna de Walvis Bay es paseo público urbano, y los lechos secos del Damaraland son pista abierta.":
        "la laguna de Walvis Bay tiene paseo urbano, pero cada lecho, concesión y pista del Damaraland exige comprobar acceso y mascotas.",
    "uno de los países más seguros de África":
        "un país donde el viaje por carretera exige una gestión muy conservadora",
    "el riesgo de crimen contra viajeros es estadísticamente marginal en la ruta prevista":
        "los hurtos urbanos y el riesgo vial exigen medidas distintas y ninguno debe minimizarse",
    "la causa número uno de muerte de turistas es el vuelco de un único vehículo por exceso de velocidad en pista de grava":
        "los vuelcos en grava son un riesgo grave y repetido para visitantes",
    "la causa número uno de muerte de turistas en Namibia, muy por delante del crimen":
        "un riesgo grave para viajeros, distinto del hurto urbano",
    "donde el perro sí puede ir":
        "donde la admisión del perro depende del gestor y debe confirmarse",
    "donde hay elefantes del desierto y rinoceronte negro en libertad y el perro sí puede ir":
        "donde existe fauna libre y la admisión del perro debe confirmarse con cada gestor",
    "Fotos pendientes de sustituir</td><td>Garub, Kuiseb, Walvis Bay, Sandwich Harbour, Messum, Brandberg, Cape Cross, Damaraland, Kaokoland y Ruacana usan imágenes de referencia de la región o de un sitio próximo, no del propio lugar: sustituir por fotos propias cuando las tengamos":
        "Fotografías de PDIs</td><td>Las 24 galerías se revisaron en el grupo 9: cada portada y cada imagen representa el lugar indicado y conserva fuente, autoría, licencia y pie",
    "PUNTO CRÍTICO POR CONFIRMAR: la mayoría de las fuentes hablan de «visa on arrival» sin aclarar si se emite también en los pasos TERRESTRES o solo en los aeropuertos de Windhoek y Walvis Bay. Como entramos por carretera en Noordoewer, hay que confirmarlo expresamente con la embajada de Namibia (en París o en Madrid) y, si hay la menor duda, tramitar el e-visa desde casa.":
        "El fact sheet oficial de MHAISS incluye Noordoewer entre los puestos que admiten e-visa y visado a la llegada. Ruacana figura únicamente para e-visa; si se elige esa salida, llevarla tramitada antes de llegar al puesto.",
    "Confirmar con la embajada de Namibia que el visado de turista para españoles se emite EN EL PUESTO TERRESTRE de Noordoewer y no solo en aeropuertos; si hay duda, tramitar el e-visa desde casa antes de salir de Sudáfrica":
        "Revalidar el fact sheet de MHAISS antes del viaje: en la versión auditada Noordoewer admite e-visa y visado a la llegada, mientras Ruacana solo admite e-visa",
    "AGUA DEL GRIFO POTABLE, algo excepcional en todo el corredor. Beber y llenar sin tratamiento.":
        "La red urbana es un candidato de recarga, no una garantía universal de potabilidad ni de permiso para llenar el vehículo. Confirmar cada toma y tratar el agua de bebida si no hay análisis o aviso vigente.",
    "Recarga de depósito de uso general: la red de campings, lodges y estaciones de servicio de todo el país está pensada para vehículos propios y permite llenar con manguera. Confirmar en recepción; en algunos sitios del desierto cobran por el agua, y es razonable que lo hagan.":
        "Para ducha, aseo y limpieza, pedir autorización en cada camping, lodge o estación y comprobar que el vehículo llega a la toma, el tipo de conexión, el caudal y el coste. Hasta la auditoría específica, ninguno cuenta como recarga confirmada.",
    "Campings de la NWR (Etosha, Sesriem, Waterberg): agua corriente potable. En la costa (Torra Bay, Terrace Bay) el agua es salobre y solo de uso general.":
        "Los campings de NWR son candidatos operativos, pero no se presupone potabilidad, disponibilidad continua ni posibilidad de conectar una manguera. Confirmarlo con el establecimiento para las fechas concretas.",
    "KAOKOLAND Y MARIENFLUSS: NO HAY AGUA. Última recarga fiable en Opuwo o Sesfontein; cargar autonomía completa para 5-6 días contando el perro y un margen por avería.":
        "KAOKOLAND Y MARIENFLUSS: no planificar ninguna recarga sin confirmación reciente. Opuwo y Sesfontein son candidatos de última recarga; salir con autonomía holgada para personas, perro y una avería.",
    "Skeleton Coast y Messum: sin recarga en todo el tramo. Entrar con los depósitos al 100% desde Henties Bay, Uis o Palmwag.":
        "Skeleton Coast y Messum: tratar el tramo como autosuficiente hasta verificar una toma concreta. Completar depósitos en un punto previamente confirmado antes de entrar.",
    "El Cunene (Epupa, Ruacana) lleva agua todo el año, pero con cocodrilos y bilharzia: filtrar y tratar siempre, y no recogerla desde la orilla.":
        "El Cunene no debe figurar como recarga ordinaria: el caudal, el acceso seguro y el riesgo sanitario requieren evaluación local. No aproximarse a la orilla con el perro y, en emergencia, aplicar tratamiento adecuado antes de beber.",
    "Red buena y bien distribuida en el eje principal: Engen, Puma, Total y Shell, diésel fiable. Namibia y Sudáfrica son los dos países del viaje donde menos hay que preocuparse por esto… salvo en el noroeste.":
        "El eje principal concentra estaciones de varias marcas, pero cada parada sigue siendo un candidato: confirmar existencia, horario, stock y medio de pago antes de los tramos largos, especialmente en el noroeste.",
    "EJE INTERIOR, sin gaps preocupantes:":
        "EJE INTERIOR, secuencia de localidades candidatas:",
    "Solitaire es el único repostaje formal del corredor de Sossusvlei (Sesriem tiene surtidor, pero no se puede dar por seguro)":
        "Solitaire y Sesriem son los candidatos de repostaje del corredor de Sossusvlei, sin dar por seguro el stock",
    "KAOKOLAND, el tramo crítico del país: OPUWO Y SESFONTEIN SON LAS ÚLTIMAS PLAZAS FIABLES.":
        "KAOKOLAND, el tramo crítico del país: Opuwo y Sesfontein son las principales plazas candidatas y hay que comprobar existencias.",
    "Precio del diésel homogéneo y regulado; se paga en efectivo o tarjeta según la estación, y muchas son atendidas (no autoservicio). Llevar siempre efectivo en dólares namibios o rand.":
        "Precio, disponibilidad y pago pueden cambiar; llevar efectivo compatible y tarjeta, y no apurar el depósito antes de un tramo remoto.",
    "El patrón es siempre el mismo — vuelco de un único vehículo por exceso de velocidad en pista corrugada.":
        "Un escenario recurrente es la salida de vía o el vuelco tras perder el control en pista corrugada.",
    "El patrón del accidente típico es siempre el mismo — velocidad alta sobre corrugado, una corrección brusca del volante, el vehículo se cruza y vuelca.":
        "La combinación de velocidad inadecuada, corrugado y una corrección brusca puede provocar una salida de vía o un vuelco.",
    "Marea en Sandwich Harbour: el único riesgo del país donde quedarse atascado puede ser grave de verdad.":
        "Marea en Sandwich Harbour: quedarse atascado con la marea subiendo es un riesgo específico que exige planificación.",
    "permiso obligatorio del MEFT/NWR en Swakopmund":
        "permiso del MEFT conforme a las condiciones vigentes, que debe tramitarse por el canal que indique el ministerio",
    "Permiso obligatorio del MEFT/NWR (zona Namib-Naukluft), que se saca en Swakopmund.":
        "El acceso requiere permiso del MEFT y debe confirmarse con el ministerio el canal y la oficina vigentes.",
    "AL NORTE DE TERRACE BAY empieza la Skeleton Coast Wilderness, zona restringida a la que solo se accede con PERMISO ESPECIAL tramitado en la oficina de parques de Windhoek o con operador concesionario: es la parte mítica (Rocky Point, cabo Frio, el Hoanib), y vale la pena intentar el permiso con antelación.":
        "AL NORTE DE TERRACE BAY comienza una zona restringida. No se presupone un permiso individual: confirmar con MEFT y operadores concesionarios qué acceso existe, para quién y bajo qué condiciones.",
    "Intentar el PERMISO ESPECIAL en la oficina de parques de Windhoek para la zona al norte de Terrace Bay (Rocky Point, cabo Frio, Hoanib): es la parte mítica y no se puede improvisar":
        "Consultar a MEFT y a operadores concesionarios si existe acceso autorizado al norte de Terrace Bay; no tratarlo como un permiso individual disponible hasta recibir confirmación escrita",
    "Noordoewer/Vioolsdrif desde Sudáfrica, sobre el río Orange: paso principal del sur, operativo 24 h.":
        "Noordoewer/Vioolsdrif desde Sudáfrica, sobre el río Orange: paso principal del sur; confirmar horario y operativa antes de viajar.",
    "Paso principal del sur sobre el río Orange, OPERATIVO 24 H. Colas largas en vacaciones sudafricanas. Pagar el CBC del vehículo en la oficina de la Road Fund Administration. Confirmar el trámite aduanero sudafricano de salida del vehículo extranjero vigente en 2027.":
        "Paso principal del sur sobre el río Orange. Confirmar horario, afluencia, tasas y formalidades de salida del vehículo vigentes en 2027.",
    "Última plaza fiable de combustible, Opuwo y Sesfontein; entrar al Marienfluss con autonomía de ida y vuelta más margen.":
        "Opuwo y Sesfontein son las principales plazas candidatas; confirmar existencias y entrar al Marienfluss con autonomía de ida y vuelta más margen.",
    "Opuwo (última plaza real)":
        "Opuwo (última base principal, stock a confirmar)",
    "Mejor oferta y calidad del país (Engen, Puma, Total, Shell); diésel fiable. Repostar a fondo en las tres antes de los tramos largos del desierto y del noroeste.":
        "Windhoek, Swakopmund y Walvis Bay concentran estaciones y servicios. Elegir puntos concretos, comprobar stock y llenar antes de los tramos largos del desierto y del noroeste.",
    "Oferta fiable en el eje sur. Aus y Lüderitz son las últimas antes del desvío a la costa del Sperrgebiet.":
        "Keetmanshoop, Aus y Lüderitz son las plazas candidatas del eje sur. Confirmar estación, horario y stock antes del desvío a la costa del Sperrgebiet.",
    "Un surtidor, una panadería famosa por su tarta de manzana y coches oxidados en el jardín: el punto de repostaje formal del eje hacia Sossusvlei y un clásico de la ruta namibia. No depender de encontrar otra opción en el tramo.":
        "Solitaire es un candidato de repostaje del eje hacia Sossusvlei. Confirmar que el surtidor opera y tiene stock; no iniciar el tramo dependiendo de una única estación sin verificación reciente.",
    "Punto donde se compran los permisos del Namib-Naukluft (incluido Sandwich Harbour y el Welwitschia Drive) y donde se confirma el estado de las pistas de la costa antes de salir.":
        "Referencia administrativa en Swakopmund para consultar permisos del Namib-Naukluft y el estado de las pistas; confirmar dirección, horario y competencia con MEFT antes de acudir.",
    "Reservar Etosha, Sesriem y (si aplica) Torra Bay desde casa con meses de antelación; sin reserva no hay Dune 45 al amanecer":
        "Consultar disponibilidad de Etosha, Sesriem y, si aplica, Torra Bay con antelación; dormir dentro puede ampliar el margen de acceso temprano, sujeto al horario vigente",
}


def replace_deep(value):
    if isinstance(value, str):
        for old, new in REPLACEMENTS.items():
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [replace_deep(item) for item in value]
    if isinstance(value, dict):
        return {key: replace_deep(item) for key, item in value.items()}
    return value


def apply_pois() -> None:
    path = ROOT / "content" / "pois" / "namibia.json"
    pois = json.loads(path.read_text(encoding="utf-8"))
    by_number = {poi["n"]: poi for poi in pois}
    expected = set(by_number)
    for label, values in (("coordenadas", COORDS), ("nombres", NAMES), ("contenido", CONTENT), ("enlaces", LINKS), ("fotografías", PHOTOS)):
        if set(values) != expected:
            raise ValueError(f"namibia: {label} incompletos; faltan={sorted(expected-set(values))}; sobran={sorted(set(values)-expected)}")
    for number, poi in by_number.items():
        poi["name"] = NAMES[number]
        poi["lat"], poi["lon"] = COORDS[number]
        poi["desc"] = CONTENT[number]["desc"]
        poi["visit"] = CONTENT[number]["visit"]
        poi["links"] = links(number)
        poi["photos"] = PHOTOS[number]
        primary = poi["photos"][0]
        poi["img"], poi["source"], poi["credit"] = primary["img"], primary["source"], primary["credit"]
    path.write_text(json.dumps(pois, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def apply_ficha() -> None:
    path = ROOT / "content" / "ficha" / "namibia.json"
    ficha = json.loads(path.read_text(encoding="utf-8"))
    ficha.update(HISTORY)
    ficha = replace_deep(ficha)
    ficha["verificado"] = True
    chip_values = {
        "PERRO": "Parques nacionales: no · fuera de ellos: confirmar cada gestor y recinto",
        "VISADO": "Españoles: visado desde abril de 2025 · condiciones distintas según el puesto",
        "RIESGOS": "Grava y tramos remotos: conducción conservadora · en ciudad, prevenir hurtos",
    }
    ficha["chips"] = [
        ["RIESGOS" if label == "RIESGO Nº1" else label,
         chip_values.get("RIESGOS" if label == "RIESGO Nº1" else label, value)]
        for label, value in ficha.get("chips", [])
    ]
    for item in ficha.get("logistics", []):
        if item.get("name", "").startswith("Frontera · Entrada — Noordoewer"):
            item["info"] = (
                "Paso principal con Sudáfrica sobre el río Orange, en la N7/B1. Confirmar el horario "
                "vigente y los trámites del vehículo antes de salir; pagar las tasas aplicables en el "
                "puesto y no convertir referencias históricas de horario en una garantía para 2027."
            )
    ficha["sources"] = VERIFIED_SOURCES
    ficha["hero_img"] = PHOTOS[1][0]["img"]
    ficha["hero_credit"] = "Fish River Canyon · " + PHOTOS[1][0]["credit"]
    ficha["sources_note"] = "Última revisión de esta versión: 15 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación."
    stale_labels = ("FOTOGRAFÍAS", "FOTOS PENDIENTES DE SUSTITUIR", "COORDENADAS APROXIMADAS", "Coordenadas aproximadas")
    cleaned_sections = []
    for section in ficha.get("custom_sections_post", []):
        cleaned_fields = []
        for field in section:
            if isinstance(field, str):
                for label in stale_labels:
                    field = re.sub(rf"<tr ><td>{re.escape(label)}</td><td>.*?</td></tr>", "", field, flags=re.DOTALL)
            cleaned_fields.append(field)
        cleaned_sections.append(cleaned_fields)
    if cleaned_sections:
        ficha["custom_sections_post"] = cleaned_sections
    path.write_text(json.dumps(ficha, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    audit_path = ROOT / "audit" / "historia" / "namibia.json"
    audit = {"slug": "namibia", **HISTORY, "notas": HISTORY_NOTES}
    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    apply_pois()
    apply_ficha()

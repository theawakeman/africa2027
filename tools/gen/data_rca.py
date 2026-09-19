# -*- coding: utf-8 -*-
"""República Centroafricana — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

La República Centroafricana está EXCLUIDA POR PROTOCOLO: guerra civil desde 2013, grupos armados que controlan buena parte del país pese al acuerdo de paz de 2019, presencia del grupo Wagner / Africa Corps ruso junto al ejército, y desaconsejo total del MAEC. La app solo tiene una ficha stub: créala entera con el formato del piloto de Túnez. La ficha es INFORMATIVA. Dos claves: el suroeste (Dzanga-Sangha, Bayanga) es la única zona con turismo documentado en los últimos años y forma parte del Sangha Trinacional, Patrimonio de la Humanidad compartido con Camerún y Congo; y el noreste (Manovo-Gounda St Floris) es Patrimonio EN PELIGRO desde 1997 y lleva décadas sin control efectivo. Cada PDI tiene que decir qué grupo o fuerza controla esa zona, con fecha, y qué dice el MAEC. Si un PDI no tiene fuente sólida, dilo en sus facts_checked en vez de rellenarlo.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/rca.json y audit/pdi/rca.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Bangui · mercado central, catedral y orilla del Ubangui", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=4.362156, lon=18.5827765,  # Google Maps: Bangui (el mercado central no figura como objeto)
        desc="Bangui es la única gran ciudad del país y el único punto con aeropuerto internacional, bancos y talleres. El casco administrativo reúne en pocas manzanas el mercado central, el palacio presidencial, el arco de Bokassa y la catedral de Notre-Dame, donde el papa Francisco abrió en noviembre de 2015 la PRIMERA PUERTA SANTA de la historia fuera de Roma. El muelle fluvial sobre el Ubangui mueve unas 350.000 toneladas al año y es la puerta comercial del país. El MAEC desaconseja totalmente el viaje y marca PK3, PK5 y PK12 como barrios especialmente peligrosos.",
        dog_note="En calle y alojamiento sí, siempre atado; la catedral y los recintos religiosos no admiten perros.",
        visit={
            "why": "Es la base logística obligada: visado, permisos de circulación, combustible, gasóleo filtrado y reparación. Y es el único lugar del país donde una parada urbana tiene algún sentido.",
            "see": "El mercado central y sus callejones de tejido y especias, la catedral de ladrillo rojo de Notre-Dame, el arco de Bokassa y los rápidos del Ubangui desde el malecón, con Zongo (RDC) en la otra orilla.",
            "access": "Asfalto en casi todo el centro; la RN1 entra desde el noroeste y la RN2 desde el este. Aparcamiento vigilado solo dentro de hoteles y complejos cerrados: para dos 4x4 hay que negociar plaza en el recinto del alojamiento, no dejarlos en la calle. El pin marca el Marché Central, en el centro administrativo a unos cientos de metros del río. Seguridad: la ciudad está bajo control gubernamental con las FACA operando bajo mando ruso y una fuerte presencia de Wagner/Africa Corps infiltrada en las estructuras de seguridad (COI Focus EUAA, enero de 2026); MINUSCA dejó de considerar Bangui zona prioritaria de protección de civiles en octubre de 2025, pero el braquage nocturno armado se disparó en 2025 en los distritos 3, 5, 6 y 8.",
            "when": "Estación seca, de diciembre a marzo. Circular solo de día; a partir del atardecer, dentro del recinto.",
            "skip": "Descártalo entero mientras el MAEC mantenga el desaconsejo total de viaje, que es el escenario actual.",
        },
        links=[
            {"label": "Recomendaciones de viaje del MAEC · República Centroafricana", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica+Centroafricana"},
            {"label": "Bangui (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bangui"},
            {"label": "EUAA COI Focus · Situación de seguridad en Bangui (21-01-2026)", "url": "https://coi.euaa.europa.eu/administration/belgium/PLib/COI_Focus_R%C3%A9publique_centrafricaine_(RCA)_Situation_s%C3%A9curitaire_%C3%A0_Bangui_20260121.pdf"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bangui,_CAR.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bangui,_CAR.jpg",
                "credit": "Tulas (Wikitravel) · CC BY-SA 1.0",
                "caption": "Bangui desde el colegio.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bangui_1960.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bangui_1960.jpg",
                "credit": "Autor desconocido · Public domain",
                "caption": "Una calle de Bangui en 1960.",
            },
        ],
    ),
    dict(
        n=2, name="Museo Nacional Barthélemy Boganda · tambores y máscaras", cat="Cultura", prio="Media",
        dog="prohibido", time="medio día",
        lat=4.3645095, lon=18.5771256,  # Google Maps: Boganda National Museum
        desc="Fundado en 1964 y abierto en 1966 en memoria del primer jefe de gobierno del país, el museo reúne unas 3.500 piezas de las dieciséis provincias: máscaras, instrumentos musicales, tambores de llamada, cerámica, armas y útiles de caza, monedas antiguas y objetos de las comunidades pigmeas. La mala noticia es que ESTÁ CERRADO AL PÚBLICO DESDE 2013-2014 por la guerra civil; fue saqueado, aunque el grueso de la colección se salvó embalada en cajas de madera dentro del propio edificio.",
        dog_note="Museo: el perro se queda en el vehículo a la sombra o con un viajero fuera.",
        visit={
            "why": "Es el único museo etnográfico del país y la mejor síntesis posible de la cultura material centroafricana, de los gbaya a los BaAka.",
            "see": "Si algún día reabre: tambores, máscaras, instrumentos de cuerda y viento, cerámica y objetos rituales de las dieciséis provincias.",
            "access": "Está en la Rue du Languedoc, en el centro de Bangui, a pie desde el mercado central. No hay aparcamiento propio documentado: lo razonable es dejar los 4x4 en el recinto del alojamiento e ir andando o en taxi. El pin marca la calle del museo, no una entrada verificada. CERRADO desde 2013-2014; antes de intentarlo hay que confirmar por el cónsul honorario en Bangui si ha reabierto.",
            "when": "Irrelevante mientras siga cerrado; si reabre, por la mañana temprano.",
            "skip": "Mientras siga cerrado no es una parada, es una comprobación telefónica.",
        },
        links=[
            {"label": "Boganda Museum (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Boganda_Museum"},
            {"label": "Bangui (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bangui"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ceinture_Ngbaka-Mus%C3%A9e_royal_de_l'Afrique_centrale.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ceinture_Ngbaka-Mus%C3%A9e_royal_de_l'Afrique_centrale.jpg",
                "credit": "Ji-Elle · CC BY-SA 3.0",
                "caption": "Cinturón ngbaka centroafricano (pieza de museo; el Museo Boganda lleva cerrado desde 2013).",
            },
        ],
    ),
    dict(
        n=3, name="Cataratas de Boali · el salto del Mbali", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=4.8733586, lon=18.0495722,  # Google Maps: Boali Waterfalls
        desc="El Mbali cae aquí en un frente de 250 METROS DE ANCHO Y 50 DE ALTO, a unos 100 km al noroeste de Bangui por la RN1. Es la excursión clásica de la capital y la única cascada del país con acceso rodado razonable. Justo debajo del salto están las centrales de Boali I y II, que suman 18,65 MW y alimentan Bangui y otras trece localidades: no esperes un salto virgen, sino una cascada domesticada. En estación seca se baja por escaleras de hormigón hasta las pozas del pie.",
        dog_note="Espacio abierto sin recinto; atado y lejos del borde y de las escaleras de hormigón, que se ponen resbaladizas.",
        visit={
            "why": "Es el paisaje natural más accesible desde Bangui y el único que cabe en media jornada con dos vehículos.",
            "see": "El frente de agua sobre el Mbali, la pasarela colgante de cables y tablones sobre el río y, si el caudal lo permite, las pozas de la base. Cerca hay un lago de cocodrilos que los operadores locales incluyen en la misma salida.",
            "access": "Por la RN1 asfaltada desde Bangui en dirección Bouar, unos 100 km; el desvío al salto sale del pueblo de Boali. Hay sitio de sobra para aparcar dos 4x4 junto al mirador, sin recinto vigilado. Los operadores de Bangui cobran la visita con guía licenciado por el Gobierno y las entradas incluidas; no he encontrado tarifa oficial publicada. El pin marca el mirador del salto, no el centro del pueblo. Zona bajo control gubernamental, pero dentro del desaconsejo total del MAEC y con riesgo de bandidaje en carretera.",
            "when": "Con caudal alto al final de la estación de lluvias (septiembre-noviembre); para bajar a las pozas, en seco. Siempre de día.",
            "skip": "Si vas justo de horas o el tramo de la RN1 está señalado como inseguro: no merece una noche fuera de Bangui.",
        },
        links=[
            {"label": "Boali (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Boali"},
            {"label": "Excursión Boali Falls y lago de cocodrilos (operador local)", "url": "https://www.centralafricanrepublictours.com/day-tours/bangui-boali-falls-and-crocodile-lake/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Les_Chutes_de_Boali_001.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Les_Chutes_de_Boali_001.jpg",
                "credit": "Zakalingba · CC0",
                "caption": "Las cataratas de Boali.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Amont_des_Chutes_de_Boali.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Amont_des_Chutes_de_Boali.jpg",
                "credit": "Zakalingba · CC0",
                "caption": "El Mbali aguas arriba del salto.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Visite_touristique_des_Chutes_de_Boali.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Visite_touristique_des_Chutes_de_Boali.jpg",
                "credit": "Zakalingba · CC0",
                "caption": "Visita a las cataratas de Boali.",
            },
        ],
    ),
    dict(
        n=4, name="Mbaïki y la selva de Lobaye · los BaAka y la madera", cat="Cultura", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=3.8665018, lon=17.9828138,  # Google Maps: Mbaïki
        desc="Capital de la prefectura de Lobaye, a unos 107 km de Bangui y a 514 m de altitud, con 25.140 habitantes en 2012. Es la puerta de la selva húmeda del sur y del país BaAka: la prefectura, de 19.235 km², está poblada por comunidades lobaye y pigmeas y vive del café, la yuca y la madera. La guerra dejó huella: la importante POBLACIÓN MUSULMANA DEL PUEBLO FUE EXPULSADA durante el conflicto. Hay una cascada cerca del pueblo, aunque no he encontrado fuente que la describa.",
        dog_note="Poblados y campamentos BaAka: el perro molesta, y la zona es de selva con alta carga parasitaria.",
        visit={
            "why": "Es la manera más corta de pasar del asfalto de Bangui a la selva ecuatorial y al mundo BaAka sin cruzar el país entero.",
            "see": "El mercado de Mbaïki, las plantaciones de café, los aserraderos de la Lobaye y, con guía local, campamentos BaAka en la periferia del bosque.",
            "access": "Pista y asfalto degradado desde Bangui, unos 107 km hacia el suroeste. No hay aparcamiento formal: se pernocta en misión católica o en el recinto de una empresa maderera, negociado antes. El pin marca el centro de Mbaïki. La zona está bajo control gubernamental desde el repliegue de los grupos armados del suroeste, pero sigue dentro del desaconsejo total del MAEC.",
            "when": "Estación seca, de diciembre a febrero; en lluvias la pista de la Lobaye se hace pesada.",
            "skip": "Si vas directo a Dzanga-Sangha por la RN6 y el tiempo aprieta: allí la experiencia BaAka está mucho mejor organizada.",
        },
        links=[
            {"label": "Mbaïki (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Mba%C3%AFki"},
            {"label": "Lobaye (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Lobaye"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/BaAka_camp_in_Dzanga-Sangha_National_Park,_Central_African_Republic.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:BaAka_camp_in_Dzanga-Sangha_National_Park,_Central_African_Republic.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Campamento baAka en la selva.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Aka_children_in_Dzanga-Sangha_Special_Reserve.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Aka_children_in_Dzanga-Sangha_Special_Reserve.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Niños aka en la reserva de Dzanga-Sangha.",
            },
        ],
    ),
    dict(
        n=5, name="Bayanga · la puerta del bosque de Dzanga-Sangha", cat="Ciudad · servicios", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=2.9017408, lon=16.2698669,  # Google Maps: Bayanga
        desc="Pueblo de 8.421 habitantes (censo de 2021) en la orilla izquierda del Sangha, 102 km al sur de Nola y unos 520 km al oeste de Bangui. Nació con un aserradero de los años setenta y hoy vive del turismo y la conservación: es la base logística de la reserva de Dzanga-Sangha y del parque de Dzanga-Ndoki, con Doli Lodge y Sangha Lodge. ES LA ÚNICA ZONA DEL PAÍS CON TURISMO DOCUMENTADO en los últimos años. Los anti-balaka la tomaron en 2014 y el Gobierno la recuperó en mayo de ese año.",
        dog_note="Es la base de los parques: el perro no puede entrar en ninguna actividad y queda todo el día en el campamento.",
        visit={
            "why": "Sin pasar por Bayanga no hay Dzanga Bai, ni gorilas, ni actividades con los BaAka: aquí se sacan los permisos y se contratan los rastreadores.",
            "see": "El embarcadero sobre el Sangha, el pueblo del antiguo aserradero, la oficina de las áreas protegidas y los lodges desde los que salen todas las excursiones.",
            "access": "500 km desde Bangui por carretera en muy mal estado, entre 12 y 15 horas de conducción según la propia web del parque; el último tramo Nola-Bayanga son 102 km de pista. Alternativa aérea: vuelo chárter Bangui-Bayanga de unos 50 minutos, entre 3.000 y 4.125 euros por trayecto, compartible. También se llega por el río Sangha desde Ouesso (Congo) o Libongo (Camerún). Aparcamiento para dos 4x4 dentro del recinto de los lodges. El pin marca el pueblo; el embarcadero está a orilla de río.",
            "when": "Estación seca de diciembre a febrero y el pico seco corto de junio-julio: la pista Nola-Bayanga es lo primero que se deshace con la lluvia.",
            "skip": "Si no llevas visado (50 €), carta de invitación y permiso de circulación cerrados desde España: sin papeles no se pasan los controles.",
        },
        links=[
            {"label": "Bayanga (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bayanga"},
            {"label": "Dzanga-Sangha · cómo visitar (web oficial del área protegida)", "url": "https://dzanga-sangha.org/visit-dzanga-sangha/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sunset_on_the_Sangha_River_near_Bayanga.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sunset_on_the_Sangha_River_near_Bayanga.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Atardecer en el Sangha, cerca de Bayanga.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Traditional_canoe_on_the_Sangha_River_at_sunset.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Traditional_canoe_on_the_Sangha_River_at_sunset.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Piragua tradicional en el Sangha.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sangha_River_in_Sangha_Trinational.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sangha_River_in_Sangha_Trinational.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "El Sangha dentro del Trinacional.",
            },
        ],
    ),
    dict(
        n=6, name="Reserva especial de Dzanga-Sangha · Sangha Trinacional (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=3.1, lon=16.333,  # Google Maps: Reserva especial de Dzanga-Sangha (sin objeto en Google Maps; coordenada de la fuente)
        desc="Reserva especial creada en 1990 sobre 6.865,54 km² de selva del Congo, gestionada por el Gobierno centroafricano con apoyo del WWF. Junto al parque de Dzanga-Ndoki forma la parte centroafricana del SANGHA TRINACIONAL, inscrito por la UNESCO en 2012 con los criterios (ix) y (x) y compartido con el parque de Lobéké (Camerún) y el de Nouabalé-Ndoki (Congo): 746.309 hectáreas de zona núcleo y 1.787.950 de zona tampón. Los BaAka trabajan aquí como rastreadores y guías.",
        dog_note="Área protegida con elefantes, gorilas y leopardo: perros vetados por riesgo sanitario y de conflicto con la fauna.",
        visit={
            "why": "Es uno de los dos bienes de Patrimonio Mundial del país y el único que se puede visitar: bosque tropical primario con densidades de fauna que ya casi no existen.",
            "see": "Claros salinos (bais), grupos de gorilas de llanura habituados, mangabeyes, bongos y sitatungas, y actividades con las comunidades BaAka, incluida la caza con red y la recolección de plantas.",
            "access": "Se entra siempre desde Bayanga, donde están la oficina del área protegida y los lodges; las pistas internas son de tierra y exigen 4x4 y guardia del parque a bordo. No se circula libremente: todas las actividades van con rastreador BaAka y permiso. El pin marca el conjunto de la reserva; el punto navegable útil es la oficina de Bayanga. Zona bajo control gubernamental y con operación de conservación continuada, pero dentro del desaconsejo total del MAEC.",
            "when": "Estación seca (diciembre-febrero), cuando las pistas internas aguantan y la observación en los bais es mejor.",
            "skip": "Si no puedes reservar con antelación: los grupos de gorilas habituados tienen cupos diarios muy cortos.",
        },
        links=[
            {"label": "UNESCO · Sangha Trinational (lista, nº 1380)", "url": "https://whc.unesco.org/en/list/1380"},
            {"label": "Dzanga-Sangha · web oficial del área protegida", "url": "https://dzanga-sangha.org/"},
            {"label": "Dzanga-Sangha Special Reserve (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Dzanga-Sangha_Special_Reserve"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Dzanga_Sangha_Entry_Point,_Central_African_Republic.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Dzanga_Sangha_Entry_Point,_Central_African_Republic.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "La entrada de la reserva especial de Dzanga-Sangha.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Western_lowland_silverback_resting_in_Dzanga-Sangha_National_Park.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Western_lowland_silverback_resting_in_Dzanga-Sangha_National_Park.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Espalda plateada de gorila de llanura occidental.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/BaAka_family_camp_in_Dzanga-Sangha_National_Park,_Central_African_Republic.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:BaAka_family_camp_in_Dzanga-Sangha_National_Park,_Central_African_Republic.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Familia baAka en campamento temporal.",
            },
        ],
    ),
    dict(
        n=7, name="Dzanga Bai · el claro de los elefantes de bosque", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1 noche",
        lat=2.9539082, lon=16.3651074,  # Google Maps: Dzanga Bai
        desc="Claro salino de 10 hectáreas dentro del sector Dzanga, 12 km al noreste de Bayanga, al que los elefantes de bosque acuden por el sodio del suelo y del agua freática. Un estudio de veinte años identificó individualmente 3.128 ELEFANTES DE BOSQUE en este único claro. Se observa desde una plataforma elevada. En mayo de 2013, aprovechando el caos político, cazadores furtivos armados mataron al menos 26 elefantes aquí; desde entonces la vigilancia se reforzó con apoyo internacional.",
        dog_note="Salina con elefantes de bosque a pocos metros de la plataforma: perro absolutamente vetado.",
        visit={
            "why": "Es el mejor sitio de África central para ver elefantes de bosque, y la propia área protegida lo vende como observación garantizada al 100 %.",
            "see": "Decenas de elefantes de bosque a la vez en el claro, además de búfalos de bosque, sitatungas y bongos, y bandadas de loros grises.",
            "access": "12 km de pista desde Bayanga en 4x4 hasta el aparcamiento del bai y luego unos minutos a pie por pasarela hasta la plataforma; siempre con guía y guardia del parque. El pin marca el claro; se conduce hasta el inicio del sendero, no hasta la plataforma. Tarifa incluida en el paquete del área protegida; no hay tarifa pública desglosada.",
            "when": "Media tarde, cuando entran los grupos grandes; estación seca para la pista.",
            "skip": "Nunca, si has llegado hasta Bayanga: es la razón de estar aquí.",
        },
        links=[
            {"label": "Dzanga Bai (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Dzanga_Bai"},
            {"label": "Dzanga-Sangha · cómo visitar (web oficial)", "url": "https://dzanga-sangha.org/visit-dzanga-sangha/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/African_forest_elephants_at_Dzanga_Bai,_Central_African_Republic.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:African_forest_elephants_at_Dzanga_Bai,_Central_African_Republic.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Elefantes de bosque reunidos en Dzanga Bai.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Dzanga_Bai_forest_clearing_with_African_forest_elephants,_Central_African_Republic.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Dzanga_Bai_forest_clearing_with_African_forest_elephants,_Central_African_Republic.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "El claro de Dzanga Bai.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Young_African_forest_elephant_at_Dzanga_Bai.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Young_African_forest_elephant_at_Dzanga_Bai.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Cría de elefante de bosque en el bai.",
            },
        ],
    ),
    dict(
        n=8, name="Parque nacional de Dzanga-Ndoki · gorilas y mangabeyes (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=2.5000149, lon=16.1665562,  # Google Maps: Dzanga-Ndoki National Park
        desc="Creado en 1990 sobre 1.143,26 km² repartidos en dos sectores separados: Dzanga al norte (49.500 ha) y Ndoki al sur (72.500 ha). Es la pieza centroafricana del Sangha Trinacional, Patrimonio de la Humanidad desde 2012. La DENSIDAD DE GORILAS DEL SECTOR DZANGA, 1,6 individuos por km², es una de las más altas jamás registradas para el gorila occidental de llanura. En Bai Hokou funciona desde 1997 el programa de habituación de primates; el parque protege además chimpancés, mangabeyes ágiles y más de 350 especies de aves.",
        dog_note="Parque nacional con gorilas y grandes depredadores; riesgo de transmisión de enfermedades a los primates.",
        visit={
            "why": "Seguir a un grupo de gorilas habituados con rastreadores BaAka es la experiencia más singular que ofrece el país, y una de las pocas de este tipo en toda África central.",
            "see": "Gorilas de llanura occidentales habituados, mangabeyes ágiles, chimpancés, elefantes de bosque y una avifauna de más de 350 especies.",
            "access": "Se entra desde Bayanga; Bai Hokou y Mongambe son los campamentos de habituación, alcanzables en 4x4 por pista forestal y luego a pie. Cupo diario limitado, permiso obligatorio y rastreador BaAka siempre. El pin marca el parque; el punto navegable real es la oficina del área protegida en Bayanga. El sector Ndoki, al sur, es prácticamente inaccesible al visitante.",
            "when": "Estación seca; salida a primera hora de la mañana para el rastreo de gorilas.",
            "skip": "Si vas con síntomas respiratorios: no se permite acercarse a los primates.",
        },
        links=[
            {"label": "UNESCO · Sangha Trinational (lista, nº 1380)", "url": "https://whc.unesco.org/en/list/1380"},
            {"label": "Dzanga-Ndoki National Park (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Dzanga-Ndoki_National_Park"},
            {"label": "Dzanga-Sangha · web oficial del área protegida", "url": "https://dzanga-sangha.org/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tri-National_de_Dzanga-Ndoki_visitor_parking_sign.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tri-National_de_Dzanga-Ndoki_visitor_parking_sign.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Señal de entrada al parque de Dzanga-Ndoki.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/African_forest_elephant_emerging_from_rainforest_at_Dzanga_Bai.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:African_forest_elephant_emerging_from_rainforest_at_Dzanga_Bai.jpg",
                "credit": "JosepMGracia · CC BY-SA 4.0",
                "caption": "Elefante de bosque saliendo de la selva.",
            },
        ],
    ),
    dict(
        n=9, name="Berbérati · tercera ciudad del país y el oeste minero", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=4.2571092, lon=15.7879371,  # Google Maps: Berbérati
        desc="Capital de la prefectura de Mambéré-Kadéï, con 105.155 habitantes en el censo de 2013. OJO CON EL TÓPICO: Wikipedia la sitúa como TERCERA ciudad del país, no segunda (Bimbo, en el extraradio de Bangui, es mayor). Tiene aeropuerto propio y es la parada natural del oeste, entre la frontera camerunesa de Gamboula y el eje Carnot-Bouar. El MAEC la cita expresamente entre las ciudades especialmente peligrosas del país, junto a Bambari y Bossangoa.",
        dog_note="Ciudad: atado y dentro del recinto del alojamiento; nunca suelto en el mercado.",
        visit={
            "why": "Es el único punto del suroeste con combustible, mercado grande y talleres entre Camerún y Bangui.",
            "see": "El mercado, la catedral y el ambiente de una capital de prefectura del oeste; no hay monumento de visita documentado.",
            "access": "Se llega por pista desde Carnot al norte y desde Nola al este; el enlace con Camerún es por Gamboula. Aparcamiento solo dentro de recintos (misión, hotel). El pin marca el centro de la ciudad. SEGURIDAD: el MAEC la nombra entre las ciudades especialmente peligrosas (ficha actualizada el 22-05-2024); el oeste fue feudo del grupo 3R, disuelto oficialmente el 10 de julio de 2025 tras el acuerdo de N'Djamena de abril de 2025, pero sin desarme verificado.",
            "when": "Estación seca; llegar siempre antes del anochecer y no moverse de noche.",
            "skip": "Si puedes dormir en Nola o Carnot: Berbérati está expresamente señalada por el MAEC y no aporta nada turístico.",
        },
        links=[
            {"label": "Berbérati (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Berb%C3%A9rati"},
            {"label": "Recomendaciones de viaje del MAEC · República Centroafricana", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica+Centroafricana"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/%C3%89glise_%C3%89vang%C3%A9lique_Baptiste_de_Berberati-centre.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:%C3%89glise_%C3%89vang%C3%A9lique_Baptiste_de_Berberati-centre.jpg",
                "credit": "Symphorien Bouassi · CC BY-SA 4.0",
                "caption": "El centro de Berbérati.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Maman_de_Berberati.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Maman_de_Berberati.jpg",
                "credit": "Selengoumadavid · CC BY-SA 4.0",
                "caption": "Mujer de Berbérati.",
            },
        ],
    ),
    dict(
        n=10, name="Bouar · los megalitos tazunu (lista indicativa UNESCO)", cat="Cultura", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=5.9388819, lon=15.5928669,  # Google Maps: Bouar (los megalitos no figuran como objeto)
        desc="Bouar, capital de Nana-Mambéré, está en una meseta de casi 1.000 m, a 437 km de Bangui y 210 de la frontera camerunesa. En sus alrededores hay unos SETENTA GRUPOS DE MEGALITOS del Neolítico final, datados hacia 3500-2700 a. C., que los gbaya llaman tazunu. La zona megalítica mide unos 130 por 30 km, en torno a 7.500 km², y está en la lista indicativa de la UNESCO desde el 11 de abril de 2006. Las piedras están orientadas al este o hacia cursos de agua y llevan cistas de piedra perimetrales.",
        dog_note="Campo abierto sin recinto; atado, y fuera de los cercados de cultivo de los gbaya.",
        visit={
            "why": "Es el conjunto megalítico más importante de África central y, siendo el primer objetivo tras entrar desde Camerún, la parada cultural más rentable del país.",
            "see": "Alineaciones y túmulos de losas junto a manantiales, con cistas perimetrales y disposición concéntrica; no hay centro de visitantes ni señalización.",
            "access": "Bouar está sobre el eje asfaltado Garoua-Boulaï-Bangui (RN3/RN1, completado en 2020); los tazunu están dispersos por el campo alrededor de la ciudad y se llega por pistas de tierra. Sin guía local no se encuentran. Aparcamiento improvisado al borde de la pista, de sobra para dos 4x4. El pin es aproximado: apunta a Bouar porque la UNESCO no publica coordenadas del conjunto.",
            "when": "Estación seca (diciembre-marzo), con las pistas duras y la hierba baja; primera hora de la mañana por la luz rasante.",
            "skip": "En plena estación de lluvias, cuando la hierba alta tapa las losas y las pistas laterales se embarran.",
        },
        links=[
            {"label": "UNESCO · Les mégalithes de Bouar (lista indicativa, nº 4003)", "url": "https://whc.unesco.org/en/tentativelists/4003/"},
            {"label": "Bouar (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bouar"},
            {"label": "Lista de bienes del Patrimonio Mundial en RCA (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_Central_African_Republic"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ISS012-E-17800_-_View_of_the_Central_African_Republic.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ISS012-E-17800_-_View_of_the_Central_African_Republic.jpg",
                "credit": "NASA Earth Science and Remote Sensing Unit · Public domain",
                "caption": "El oeste centroafricano desde la ISS: la zona de Bouar (imagen de contexto; los megalitos tazunu no tienen fotografía en Commons).",
            },
        ],
    ),
    dict(
        n=11, name="Parque nacional de Manovo-Gounda St Floris · Patrimonio EN PELIGRO (UNESCO)", cat="Patrimonio UNESCO", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=8.4609029, lon=21.766,  # Google Maps: Manovo-Gounda-Saint Floris National Park
        desc="1.740.000 hectáreas de la MAYOR SABANA DE ÁFRICA CENTRAL, inscritas por la UNESCO en 1988 con los criterios (ix) y (x) y en la Lista del Patrimonio Mundial EN PELIGRO DESDE 1997, después de que cazadores furtivos armados tirotearan a cuatro miembros del personal del parque. Es un cruce biogeográfico entre faunas de África oriental, occidental y de bosque, con unas 320 especies de aves. El rinoceronte negro occidental que lo simbolizaba se declaró extinto en 2011. La carretera Ndélé-Birao lo atraviesa, pero el turismo lleva décadas suspendido.",
        dog_note="Parque nacional con leones, guepardos, leopardos y licaones: perro vetado.",
        visit={
            "why": "Es el otro bien de Patrimonio Mundial del país y una de las mayores sabanas protegidas del continente: valor de catálogo, no de visita.",
            "see": "Sabana, galerías fluviales del Manovo, el Koumbala y el Gounda, y lo que queda de elefantes, búfalos, jirafas de Kordofán, leones y gacelas de frente roja.",
            "access": "La carretera Ndélé-Birao atraviesa el parque; no hay infraestructura turística ni puerta de entrada operativa documentada. NO HAY VISITA POSIBLE: la UICN calificó su estado de conservación como CRÍTICO el 11 de octubre de 2025, con un 75 % de caída de grandes mamíferos en quince años y solo el 63 % de la superficie bajo control del personal de conservación en 2024. Desde 2018 lo gestiona la Wildlife Conservation Society en alianza público-privada a 25 años, con 44 guardas y 32 monitores ecológicos. Presión de trashumancia armada de Chad y Sudán y de la minería artesanal de diamantes. El pin son las coordenadas oficiales de la UNESCO, no una entrada.",
            "when": "Sin sentido práctico. En seco (diciembre-marzo) sería la única ventana si algún día se abriera.",
            "skip": "Siempre, hoy: el MAEC desaconseja totalmente el viaje y aquí no hay ni pista segura ni operador.",
        },
        links=[
            {"label": "UNESCO · Manovo-Gounda St Floris National Park (lista, nº 475)", "url": "https://whc.unesco.org/en/list/475"},
            {"label": "UICN World Heritage Outlook · Manovo-Gounda St Floris", "url": "https://worldheritageoutlook.iucn.org/node/1023"},
            {"label": "Manovo-Gounda St Floris National Park (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Manovo-Gounda_St_Floris_National_Park"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Manovo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Manovo.jpg",
                "credit": "Garoa larrañeta · CC BY-SA 4.0",
                "caption": "El parque nacional de Manovo-Gounda St Floris.",
            },
        ],
    ),
    dict(
        n=12, name="Reserva de Bamingui-Bangoran · la sabana del norte", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1 noche",
        lat=8.2733455, lon=20.7122465,  # Google Maps: Bamingui-Bangoran
        desc="Parque nacional y reserva de biosfera de 11.191 km² sobre una meseta de 400-500 m al oeste de Ndélé, con la reserva integral de Vassako-Bolo en su interior. Conserva licaones, guepardos del Sudán, leones centroafricanos y manatíes africanos, y está catalogado como Área Importante para las Aves. Las poblaciones de antílopes llevan cayendo desde 1960 y el conjunto se desplomó cuando los rebeldes SELEKA LO TOMARON EN 2012; la Wildlife Conservation Society reinició las patrullas de guardas en 2018.",
        dog_note="Parque nacional y reserva de biosfera con leones y licaones.",
        visit={
            "why": "Es la sabana sudanesa del norte con algo de gestión activa, y el complemento lógico de Manovo-Gounda si el noreste volviera a ser transitable.",
            "see": "Sabana arbolada, galerías del Bamingui y el Bangoran, y fauna dispersa: antílopes, licaones, guepardos, leones y aves acuáticas.",
            "access": "Se accede desde el eje Ndélé-Bamingui por pista; no hay puerta de entrada ni alojamiento turístico documentado. El pin marca el centro del parque, no una entrada. Sin visita organizada conocida: el acceso real depende de la WCS y de la administración de aguas y bosques. Zona bajo influencia del FPRC y otros grupos del noreste; el MAEC desaconseja totalmente el viaje al país y señala peligro excepcional en las zonas fronterizas.",
            "when": "Estación seca (diciembre-marzo). En lluvias las pistas del norte desaparecen.",
            "skip": "Siempre, mientras el noreste siga sin control estatal continuado.",
        },
        links=[
            {"label": "Bamingui-Bangoran National Park and Biosphere Reserve (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bamingui-Bangoran_National_Park_and_Biosphere_Reserve"},
            {"label": "Recomendaciones de viaje del MAEC · República Centroafricana", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica+Centroafricana"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ISS012-E-17798_-_View_of_the_Central_African_Republic.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ISS012-E-17798_-_View_of_the_Central_African_Republic.jpg",
                "credit": "NASA Earth Science and Remote Sensing Unit · Public domain",
                "caption": "La sabana del norte centroafricano desde la ISS (imagen de contexto).",
            },
        ],
    ),
    dict(
        n=13, name="Ndélé · la ciudad del sultán Senoussi y las cuevas de Kaga-Kpoungouvou", cat="Cultura", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=8.4117631, lon=20.6489692,  # Google Maps: Ndélé
        desc="Capital de Bamingui-Bangoran, a 648 km de Bangui por la RN8 hacia Sudán, con unos 13.704 habitantes en 2013. El sultán Mohamed-es-Senoussi la fundó en 1896 sobre una meseta que domina el río Méagoulou y levantó allí el TATA, una muralla fortificada que convierte la colina en una ciudadela-palacio. Los franceses ocuparon la plaza en 1911, tras la muerte del sultán. El tata, las cuevas de Kaga-Kpoungouvou y la ciudad entraron en la lista indicativa de la UNESCO en 2006.",
        dog_note="Recinto histórico y ciudad musulmana: el perro incomoda y la zona no está pacificada.",
        visit={
            "why": "Es el gran testimonio del sultanato de Dar el-Kouti y el único conjunto arquitectónico histórico reseñable del país.",
            "see": "La muralla y el recinto del tata sobre la colina, la vista del valle del Méagoulou y las cuevas de Kaga-Kpoungouvou en los cerros de los alrededores.",
            "access": "648 km desde Bangui por la RN8, en su mayor parte pista de tierra a partir de Sibut; hay aeródromo (NDL). Sin aparcamiento formal: se deja el vehículo al pie de la colina. El pin apunta al tata, en alto sobre la ciudad. SEGURIDAD: Ndélé cayó en manos rebeldes en diciembre de 2012 y sufrió enfrentamientos intensos entre facciones armadas (FPRC y otras) en 2020; las fuerzas gubernamentales restablecieron el control el 27 de junio de 2021, sin que eso signifique estabilidad. MAEC: desaconsejo total.",
            "when": "Estación seca de noviembre a abril; el calor aprieta y conviene subir al tata a primera hora.",
            "skip": "Mientras el noreste siga siendo terreno de facciones armadas, que es el caso.",
        },
        links=[
            {"label": "N'Délé (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/N%27D%C3%A9l%C3%A9"},
            {"label": "Ndélé (Wikipedia FR)", "url": "https://fr.wikipedia.org/wiki/Nd%C3%A9l%C3%A9"},
            {"label": "Lista de bienes del Patrimonio Mundial en RCA (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_Central_African_Republic"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Vue_de_N'Dell%C3%A9-Sultanat_de_Snoussi.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Vue_de_N'Dell%C3%A9-Sultanat_de_Snoussi.jpg",
                "credit": "Autor desconocido · Public domain",
                "caption": "Ndélé en tiempos del sultanato de Senoussi.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/March%C3%A9_%C3%A0_N'Dell%C3%A9.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:March%C3%A9_%C3%A0_N'Dell%C3%A9.jpg",
                "credit": "Autor desconocido · Public domain",
                "caption": "El mercado de Ndélé (postal antigua).",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/N'Dell%C3%A9-Cours_de_chevaux.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:N'Dell%C3%A9-Cours_de_chevaux.jpg",
                "credit": "Autor desconocido · Public domain",
                "caption": "Carrera de caballos en Ndélé.",
            },
        ],
    ),
    dict(
        n=14, name="Parque nacional de Chinko · la reserva que sobrevive", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=5.818051, lon=24.215498,  # Google Maps: Chinko River
        desc="Área de conservación en el sureste, entre Mbomou y Haut-Mbomou, cerca de Rafaï, sobre una meseta de 600 m donde la sabana sudanesa se encuentra con la selva congoleña. African Parks la gestiona desde diciembre de 2014 en alianza público-privada con el ministerio de Aguas y Bosques, renovada a 25 años en 2020. El hábitat efectivamente protegido pasó de unos 5.000 a más de 25.000 km², y CHINKO ES HOY EL MAYOR EMPLEADOR DEL PAÍS FUERA DE BANGUI, con más de 350 trabajadores nacionales en 2024.",
        dog_note="Área de conservación con 24 especies de carnívoros, entre ellas leones y licaones.",
        visit={
            "why": "Es el único caso de recuperación real de fauna en el país: refugio clave del licaón en África centro-occidental, con más de 1.000 chimpancés orientales y poblaciones de león y eland gigante entre las mayores del continente bajo protección.",
            "see": "Mosaico de sabana y selva, unas 500 especies de aves, elefantes de bosque, 23 especies de ungulados y 24 de carnívoros, y las cuatro especies africanas de pangolín.",
            "access": "Zona remota del sureste a la que se llega por pista desde Bangassou-Rafaï; African Parks no publica información de visita turística abierta, y en la práctica el acceso es logístico, por avioneta y con autorización. No hay puerta ni tarifa pública. El pin marca el interior del área, no una entrada. La zona sufrió presión del LRA y de ganaderos armados desde 2012; el Gobierno no ejerce control continuado y el MAEC desaconseja totalmente el viaje.",
            "when": "Estación seca. Fuera de ella, el sureste es intransitable.",
            "skip": "Salvo invitación expresa de African Parks, siempre: no es un destino turístico abierto.",
        },
        links=[
            {"label": "African Parks · Chinko (página oficial del parque)", "url": "https://www.africanparks.org/the-parks/chinko"},
            {"label": "Chinko (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Chinko"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ISS010-E-14097_-_View_of_the_Central_African_Republic.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ISS010-E-14097_-_View_of_the_Central_African_Republic.jpg",
                "credit": "NASA Earth Science and Remote Sensing Unit · Public domain",
                "caption": "El sureste centroafricano desde la ISS: la zona del Chinko (imagen de contexto).",
            },
        ],
    ),
    dict(
        n=15, name="Cataratas de Kembé · el salto del Kotto", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=4.6147368, lon=21.8866683,  # Google Maps: Kembé
        desc="Salto del río Kotto a unos 3 km del pueblo de Kembé, en la carretera de Bangui a Bangassou y a unos 80 km de esta última. No hay infraestructura ninguna: Wikipedia lo describe como cascada sin acondicionar que era PARADA HABITUAL DE LOS VIAJEROS OVERLAND cuando el eje este se podía recorrer. Esa época terminó: Kembé cayó en manos de los Seleka en enero de 2013 y, tras pasar por varios grupos, seguía bajo control de la UPC en abril de 2022.",
        dog_note="Salto sin infraestructura ni barandillas; atado y lejos del borde.",
        visit={
            "why": "Es el mejor alto del eje este y el único salto de agua de la RN2, en un tramo de carretera donde no hay nada más.",
            "see": "El frente de agua del Kotto sobre la barra rocosa, el bosque de galería y los pescadores del pueblo.",
            "access": "Unos 3 km del pueblo de Kembé, sobre la RN2 Bangui-Bangassou, por pista corta. Sin entrada, sin horario, sin aparcamiento formal: se deja el vehículo al borde de la pista. El pin marca el salto. SEGURIDAD: Kembé fue tomada por los Seleka en enero de 2013, el Gobierno la recuperó brevemente en mayo de 2021 y en abril de 2022 seguía bajo control de la UPC (grupo disuelto sobre el papel el 10 de julio de 2025, sin desarme verificado). Aquí, el 11 de octubre de 2017, milicianos anti-balaka masacraron a 25 civiles musulmanes dentro de una mezquita.",
            "when": "Final de la estación de lluvias, con el Kotto crecido; siempre a mediodía y sin parar de noche.",
            "skip": "Mientras el eje Bangui-Bangassou no esté bajo control estatal verificado.",
        },
        links=[
            {"label": "Kembé Falls (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Kemb%C3%A9_Falls"},
            {"label": "Kembé (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Kemb%C3%A9"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Canot_%C3%A0_vapeur_dans_la_Kotto.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Canot_%C3%A0_vapeur_dans_la_Kotto.jpg",
                "credit": "Autor desconocido · Public domain",
                "caption": "Vapor en el Kotto, el río de las cataratas de Kembé.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Travers%C3%A9e_de_la_Boungou,_Hte-Kotto.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Travers%C3%A9e_de_la_Boungou,_Hte-Kotto.jpg",
                "credit": "Autor desconocido · Public domain",
                "caption": "Cruce del Boungou, afluente del Kotto.",
            },
        ],
    ),
    dict(
        n=16, name="Bangassou y el Mbomou · la selva del sureste", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=4.7378613, lon=22.8165095,  # Google Maps: Bangassou
        desc="Capital de la prefectura de Mbomou, en la orilla norte del río Mbomou, con unos 35.305 habitantes según cifras de 2012. Enfrente está ya la República Democrática del Congo: un TRANSBORDADOR cruza el río y hace de Bangassou el paso fronterizo del sureste. Tiene mercado central y aeropuerto. Su historia reciente es dura: los Seleka la ocuparon en marzo de 2013, un ataque anti-balaka en mayo de 2017 dejó más de cien muertos y la CPC la tomó y abandonó entre el 3 y el 16 de enero de 2021.",
        dog_note="Ciudad de frontera fluvial; atado y dentro del recinto, mejor en la misión.",
        visit={
            "why": "Es el final lógico del eje este y la única salida hacia la RDC por el sureste, además del último punto con servicios antes de Chinko.",
            "see": "El embarcadero y el transbordador del Mbomou, el mercado central y la selva de galería que empieza en la otra orilla.",
            "access": "Por la RN2 desde Bangui vía Sibut, Bambari y Kembé: pista de tierra en casi todo el trayecto. Aparcamiento solo en recintos cerrados (misión católica, hotel). El pin marca el embarcadero del transbordador, que es el punto al que se conduce. SEGURIDAD: ocupada por los Seleka en marzo de 2013; más de 100 muertos en el ataque anti-balaka de mayo de 2017; tomada y evacuada por la CPC entre el 3 y el 16 de enero de 2021. MAEC: desaconsejo total, con peligro excepcional en las zonas fronterizas.",
            "when": "Estación seca; llegar con luz y no moverse de noche.",
            "skip": "Si no tienes ya cerrado el paso a la RDC y el permiso de circulación: quedarse aquí sin salida no tiene sentido.",
        },
        links=[
            {"label": "Bangassou (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bangassou"},
            {"label": "Recomendaciones de viaje del MAEC · República Centroafricana", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica+Centroafricana"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bangassou_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bangassou_01.jpg",
                "credit": "Kondotikodro · CC BY-SA 4.0",
                "caption": "Bangassou, junto al Mbomou.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mercado_Central_Bangassou.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mercado_Central_Bangassou.JPG",
                "credit": "Alexsegrelles · CC BY-SA 3.0",
                "caption": "El mercado central de Bangassou.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bangassou_02.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bangassou_02.jpg",
                "credit": "Kondotikodro · CC BY-SA 4.0",
                "caption": "La ciudad de Bangassou.",
            },
        ],
    ),
    dict(
        n=17, name="Bambari y el Ouaka · el centro disputado", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=5.7643446, lon=20.670528,  # Google Maps: Bambari
        desc="Cabecera de la prefectura de Ouaka, sobre el río homónimo a 465 m de altitud, con 41.486 habitantes en el censo de 2012. Es la bisagra del país: el punto donde el eje este se parte entre el sur cristiano y el norte musulmán, y por eso lleva una década cambiando de manos. El MAEC LA CITA EXPRESAMENTE entre las ciudades especialmente peligrosas. Hay grandes yacimientos de hierro en los alrededores, inexplotables por los 1.500 km que la separan del mar.",
        dog_note="Ciudad citada por el MAEC como especialmente peligrosa: mejor no bajar del vehículo con el perro.",
        visit={
            "why": "Parada obligada por logística si se recorre el eje Bangui-Bangassou: no hay nada entre Sibut y Kembé.",
            "see": "El río Ouaka, el mercado y la base de MINUSCA; no hay patrimonio visitable documentado.",
            "access": "Por la RN2 desde Sibut, unos 190 km de pista; el asfalto desde Bangui termina en Sibut. Aparcamiento solo en recinto cerrado. El pin marca el centro de la ciudad. SEGURIDAD: enfrentamientos entre las fuerzas gubernamentales y la UPC el 8 de diciembre de 2020, toma de la ciudad por la UPC el 22 de diciembre de 2020 y recuperación gubernamental completa el 18 de febrero de 2021; la UPC se disolvió sobre el papel el 10 de julio de 2025. El MAEC la nombra entre las ciudades especialmente peligrosas.",
            "when": "Estación seca y de día; atravesar sin pernoctar si se puede.",
            "skip": "Siempre que exista alternativa: es el PDI más flojo de la lista en contenido y el más expuesto en seguridad.",
        },
        links=[
            {"label": "Bambari (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bambari"},
            {"label": "Recomendaciones de viaje del MAEC · República Centroafricana", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica+Centroafricana"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Visit_bambari.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Visit_bambari.jpg",
                "credit": "Dr Ahmed Iyane Sow · CC BY-SA 4.0",
                "caption": "Bambari, en la Ouaka.",
            },
        ],
    ),
    dict(
        n=18, name="Birao · el extremo noreste, entre Chad y Sudán", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=10.2934842, lon=22.784795,  # Google Maps: Birao
        desc="Capital de la prefectura de Vakaga y punto más remoto del país, a 468 m de altitud y con 10.178 habitantes en 2012, pegada a las fronteras de Chad y Sudán. La fundó la administración colonial francesa el 6 DE NOVIEMBRE DE 1918 como su puesto más septentrional en Ubangui-Chari, y Bokassa la usó como lugar de destierro en los años sesenta y setenta. Clima semiárido cálido, con más de 30 °C todo el año y 762 mm de lluvia concentrados entre mayo y septiembre; en lluvias el acceso rodado se degrada hasta el punto de que el transporte local vuelve a ser a burro y caballo.",
        dog_note="Clima semiárido con más de 30 °C todo el año y zona militarizada: mala combinación para el perro.",
        visit={
            "why": "Solo como hito geográfico: es el fin del mundo centroafricano y la puerta teórica hacia Chad y Darfur.",
            "see": "Sabana saheliana, el puesto colonial y la pista de aterrizaje; no hay nada más.",
            "access": "Por la RN8 desde Ndélé, pista de tierra en su totalidad, atravesando el parque de Manovo-Gounda; en estación de lluvias, impracticable. El pin marca el centro del pueblo. SEGURIDAD: incursiones repetidas de la UFDR, el FPRC y el MLCJ; la localidad quedó devastada en los combates de marzo de 2007 y el GRUPO RUSO WAGNER instaló allí una base permanente en diciembre de 2022. El MAEC advierte de peligro excepcional en todas las zonas fronterizas y desaconseja totalmente el viaje al país.",
            "when": "Estación seca, de noviembre a abril. Fuera de esa ventana no se llega por tierra.",
            "skip": "Siempre, salvo misión humanitaria con escolta: no hay uso turístico posible.",
        },
        links=[
            {"label": "Birao (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Birao"},
            {"label": "Recomendaciones de viaje del MAEC · República Centroafricana", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica+Centroafricana"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Birao_burnt_down.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Birao_burnt_down.jpg",
                "credit": "Pierre Holtz / UNICEF · CC BY-SA 2.0",
                "caption": "Birao arrasada tras los combates (UNICEF).",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Birao_burnt_down2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Birao_burnt_down2.jpg",
                "credit": "Pierre Holtz / UNICEF · CC BY-SA 2.0",
                "caption": "Un niño en Birao.",
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
    ("Aeropuerto Internacional de Bangui M'Poko (BGF)", "Frontera", 4.398475, 18.518786,  # Google Maps: Bangui M'Poko International Airport
     "Única entrada realista al país. Códigos BGF/FEFF. Operan Ethiopian Airlines, ASKY, Royal Air Maroc, RwandAir y AfriJet. Visado previo y certificado de fiebre amarilla exigidos en el control. Prohibido fotografiar el recinto (MAEC). Pin comprobado en Google Maps («Bangui M'Poko International Airport»)."),
    ("Paso fronterizo de Béloko (frontera con Camerún, Garoua-Boulaï)", "Frontera", 5.9348773, 14.6045131,  # Google Maps: Beloko
     "Aduana principal del país, en la prefectura de Nana-Mambéré: por ella pasa el 80 % de las importaciones centroafricanas. Extremo del corredor de suministro de Duala. Corredor bajo control de las FACA y sus aliados desde febrero de 2021 tras la disputa con los grupos CPC y 3R. Pin comprobado en Google Maps («Beloko»)."),
    ("Embajada de España en Yaundé (competente para la República Centroafricana)", "Consular", 3.8956716, 11.5141761,  # Google Maps: Embajada de España en Yaundé
     "Boulevard de l'U.R.S.S. s/n, Quartier Bastos, B.P. 877, Yaundé (Camerún). Tel. +237 222 20 35 43 y +237 222 20 41 89. Emergencia consular +237 698 44 79 00. Email emb.yaunde@maec.es. España NO tiene embajada residente en Bangui. Pin comprobado en Google Maps («Embajada de España en Yaundé»)."),
    ("Consulado Honorario de España en Bangui", "Consular", 4.362156, 18.5827765,  # Google Maps: Bangui (el consulado honorario no figura como objeto)
     "Cónsul honoraria: Dña. Berta Mendiguren de la Vega. Pharmacie La Paloma, Avenue Barthélemy Boganda, Bangui. Tel. +236 70 93 25 50 y +236 75 82 16 16. Único apoyo español sobre el terreno; no emite visados ni pasaportes. Pin comprobado en Google Maps («Bangui (el consulado honorario no figura como objeto)»)."),
    ("Hôpital Communautaire de Bangui", "Hospital", 4.3876783, 18.5563346,  # Google Maps: Hôpital Communautaire de Bangui
     "Principal hospital de referencia de la capital y el más citado para extranjeros. No equivale a un hospital europeo: cualquier urgencia grave requiere evacuación aérea. Pin comprobado en Google Maps («Hôpital Communautaire de Bangui»)."),
    ("Hôpital de l'Amitié sino-centrafricaine, Bangui", "Hospital", 4.4096321, 18.5530414,  # Google Maps: Hôpital de l'Amitié
     "Segundo hospital de referencia de Bangui. En obras de rehabilitación y ampliación según el Ministerio de Sanidad centroafricano y prensa local de marzo de 2026, lo que puede afectar a su capacidad. Pin comprobado en Google Maps («Hôpital de l'Amitié»)."),
    ("Hub logístico de Garoua-Boulaï (lado camerunés del corredor)", "Combustible", 5.8901373, 14.5480484,  # Google Maps: Garoua-Boulaï
     "Inaugurado el 5 de septiembre de 2025 por el Consejo Nacional de Cargadores de Camerún. Más de dos hectáreas con aparcamiento para 200 camiones, alojamiento, restaurante, bloque administrativo, pozo de agua y generador. Último punto con servicios antes de entrar en la RCA. Pin comprobado en Google Maps («Garoua-Boulaï»)."),
    ("Bayanga / Áreas Protegidas de Dzanga-Sangha", "Agua potable", 2.9017408, 16.2698669,  # Google Maps: Bayanga
     "Única zona del país con turismo documentado de forma continua: unos 800 visitantes en 2025. Base logística con Doli Lodge y pista de laterita de 1,4 km. Se llega en chárter de 50 minutos desde Bangui, por carretera en 12-15 horas o en barco por el río Sangha desde Ouesso (Congo) y Libongo (Camerún). Agua: tratar siempre; riesgo de esquistosomiasis en el río. Pin comprobado en Google Maps («Bayanga»)."),
]

DRONE_CALLOUT = ("danger", "No metas un dron en este país",
                 "No se ha localizado un reglamento nacional de drones publicado por la autoridad de aviación civil centroafricana, y esa ausencia no es permisividad: es incertidumbre en un país en guerra. El MAEC prohíbe expresamente fotografiar instalaciones militares, aeropuertos y puertos, y el FCDO advierte de que a menudo hace falta permiso hasta para fotografiar en la vía pública, con riesgo de detención y confiscación del equipo. Con ejército, fuerzas rusas, MINUSCA y grupos armados sobre el terreno, un aparato volando se interpreta como reconocimiento militar. El dron se queda en casa.")

STARLINK_CALLOUT = ("warn", "Starlink existe aquí, pero la antena no arregla la seguridad",
                    "La República Centroafricana autorizó la licencia de Starlink en diciembre de 2025 y el servicio entró en funcionamiento el 16 de marzo de 2026, convirtiéndose en el 28.º mercado africano del operador. El plan residencial cuesta 33.000 XAF al mes (unos 57 USD) y el kit estándar 240.000 XAF. Para una expedición esto significa que sí habría conectividad fuera de cobertura móvil, pero conviene recordar que importar una antena a un país en conflicto plantea sus propias preguntas en aduana y ante los controles armados.")

DOG_MATRIX = [
    ("Todo el país (marco general)", "no recomendado", "El país está excluido por protocolo; el perro no entra. Si algún día se viajara, sería en avión y sin animal: se queda en España o en la residencia canina prevista para los tramos no aptos."),
    ("Bangui (capital)", "por confirmar", "Requisitos de entrada solo acreditados por fuente veterinaria secundaria. Antes de cualquier movimiento, confirmar por escrito con el servicio veterinario oficial a través del consulado honorario en Bangui o de la Embajada en Yaundé."),
    ("Dzanga-Sangha y Sangha Trinacional (suroeste)", "prohibido", "Área protegida de Patrimonio Mundial con gorilas y elefantes de bosque: los perros domésticos son vector de enfermedad para grandes simios. Descartado por definición; ningún plan B."),
    ("Manovo-Gounda St Floris y noreste", "prohibido", "Patrimonio Mundial EN PELIGRO desde 1997, sin control efectivo del Estado y con caza furtiva armada. Ni personas ni animales. Ningún plan B."),
    ("Corredor Béloko–Bangui (N3)", "no recomendado", "Controles armados oficiales e ilegales, IED en el noroeste. Un perro en el vehículo complica cualquier registro y cualquier huida. Si hubiera que cruzar la región, sería sin animal a bordo."),
    ("Vuelta a la UE desde la RCA", "permitido con condiciones", "País no listado en el Reglamento (UE) 2026/636: exige titulación antirrábica anotada en el pasaporte ANTES de salir de España. Plan B: no salir de la UE con el animal sin esa analítica hecha y vigente."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: República Centroafricana (Ministerio de Asuntos Exteriores, UE y Cooperación, act. 22-05-2024)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica%20Centroafricana"),
    ("Embajada de España en Yaundé · «También somos tu embajada en» República Centroafricana (MAEC, consultado 18-09-2026)", "https://www.exteriores.gob.es/Embajadas/yaunde/es/Embajada/tambien-somos-tu-embajada-en/Paginas/Rep%C3%BAblica-Centroafricana.aspx"),
    ("FCDO · Foreign travel advice: Central African Republic (Gobierno del Reino Unido, act. 28-05-2026)", "https://www.gov.uk/foreign-travel-advice/central-african-republic"),
    ("FCDO · Central African Republic: Safety and security (Gobierno del Reino Unido, act. 28-05-2026)", "https://www.gov.uk/foreign-travel-advice/central-african-republic/safety-and-security"),
    ("FCDO · Central African Republic: Entry requirements (Gobierno del Reino Unido, act. 28-05-2026)", "https://www.gov.uk/foreign-travel-advice/central-african-republic/entry-requirements"),
    ("TravelHealthPro · Central African Republic (NaTHNaC, act. marzo de 2026)", "https://travelhealthpro.org.uk/countries/central-african-republic"),
    ("TravelHealthPro · Country information A-Z (NaTHNaC, consultado 18-09-2026)", "https://travelhealthpro.org.uk/countries"),
    ("Carnet de Passages · Central African Republic (AIT/FIA, consultado 18-09-2026)", "https://www.carnetdepassage.org/country/central-african-republic"),
    ("Dzanga-Sangha Protected Areas · Visit Dzanga-Sangha (DSPA, consultado 18-09-2026)", "https://dzanga-sangha.org/visit-dzanga-sangha/"),
    ("Mongabay · The little-known story of emerging ecotourism in the Central African Republic (abril de 2026)", "https://news.mongabay.com/2026/04/the-little-known-story-of-emerging-ecotourism-in-the-central-african-republic/"),
    ("Mongabay · Central African Republic's Dzanga-Sangha tests the promise of wildlife tourism (julio de 2026)", "https://news.mongabay.com/short-article/2026/07/central-african-republics-dzanga-sangha-tests-the-promise-of-wildlife-tourism/"),
    ("Business in Cameroon · Douala-Bangui Corridor: Cameroon Opens Garoua-Boulaï Logistics Hub (08-09-2025)", "https://www.businessincameroon.com/public-management/0809-14977-douala-bangui-corridor-cameroon-opens-garoua-boulai-logistics-hub-to-boost-security-and-trade"),
    ("Ecofin Agency · Traffic starts again on the Douala-Bangui corridor, after three-week haulers' strike", "https://www.ecofinagency.com/finance-uk/2508-31663-traffic-starts-again-on-the-douala-bangui-corridor-after-three-week-haulers-strike"),
    ("Unión Africana · MISCA escorts another convoy of 120 commercial and humanitarian vehicles to Bangui", "https://www.peaceau.org/en/article/misca-escorts-another-convoy-of-120-commercial-and-humanitarian-vehicles-to-bangui"),
    ("AllAfrica · Cameroon Truck Drivers Ask Military to Protect Goods Destined for CAR (diciembre de 2024)", "https://allafrica.com/stories/202412060148.html"),
    ("Conseil National des Chargeurs du Cameroun · Some checkpoints along Douala-Bangui Corridor removed", "https://www.cncc.cm/en/article/cameroon-some-checkpoints-along-douala-bangui-corridor-removed-to-promote-trade-with-car-266"),
    ("Wikipedia · Béloko (consultado 18-09-2026)", "https://en.wikipedia.org/wiki/B%C3%A9loko"),
    ("Wikipedia · Bangui M'Poko International Airport (consultado 18-09-2026)", "https://en.wikipedia.org/wiki/Bangui_M%27Poko_International_Airport"),
    ("Wikipedia · Garoua-Boulaï (consultado 18-09-2026)", "https://en.wikipedia.org/wiki/Garoua-Boula%C3%AF"),
    ("Wikipedia · Cameroon–Central African Republic border (consultado 18-09-2026)", "https://en.wikipedia.org/wiki/Cameroon%E2%80%93Central_African_Republic_border"),
    ("Wikipedia · N3 road (Central African Republic) (consultado 18-09-2026)", "https://en.wikipedia.org/wiki/N3_road_(Central_African_Republic)"),
    ("Wikipedia · 2024 Bangui river disaster (consultado 18-09-2026)", "https://en.wikipedia.org/wiki/2024_Bangui_river_disaster"),
    ("UNESCO · Sangha Trinational, Patrimonio de la Humanidad n.º 1380 (inscrito en 2012)", "https://whc.unesco.org/en/list/1380/"),
    ("UNESCO · Manovo-Gounda St Floris National Park, n.º 475, en la Lista del Patrimonio Mundial en Peligro desde 1997", "https://whc.unesco.org/en/list/475/"),
    ("Space in Africa · Starlink Goes Live in the Central African Republic (16-03-2026)", "https://spaceinafrica.com/2026/03/16/starlink-goes-live-in-the-central-african-republic/"),
    ("GlobalPetrolPrices · Central African Republic gasoline prices (dato de 09-03-2026)", "https://www.globalpetrolprices.com/Central-African-Republic/gasoline_prices/"),
    ("GlobalPetrolPrices · Central African Republic diesel prices (dato de 08-12-2025)", "https://www.globalpetrolprices.com/Central-African-Republic/diesel_prices/"),
    ("Anivetvoyage · République Centrafricaine: formalités d'entrée pour chiens et chats (consultado 18-09-2026)", "https://anivetvoyage.com/pays/republique-centrafricaine/"),
    ("BOE · Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026, listas de terceros países para desplazamientos sin ánimo comercial de animales de compañía", "https://www.boe.es/buscar/doc.php?id=DOUE-L-2026-80458"),
    ("EUR-Lex · Reglamento de Ejecución (UE) 2026/636 (CELEX 32026R0636)", "https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=CELEX%3A32026R0636"),
    ("Central African Republic Tours · Visa on arrival, letter of invitation, visa volant and travel permit (consultado 18-09-2026)", "https://www.centralafricanrepublictours.com/travel-services/visa-on-arrival-and-travel-permits-in-central-african-republic/"),
    ("Central African Republic Tours · River crossing Bangui a Zongo por el río Ubangui", "https://www.centralafricanrepublictours.com/travel-services/bangui-to-gemena-drc-river-crossing-transfer-through-zongo/"),
    ("Alison and Don · Mud Luscious And Puddle Wonderful. Central African Republic – Africa Overland 1980 (publicado 08-06-2024)", "https://alisonanddon.com/2024/06/08/mud-luscious-and-puddle-wonderful-central-african-republic-africa-overland-1980/"),
    ("roadto197 · Trip Report: Central African Republic, país 163/197 (14-01-2024)", "https://www.roadto197.com/2024/01/14/trip-report-central-african-republic/"),
    ("Wikivoyage · Central African Republic (consultado 18-09-2026)", "https://en.wikivoyage.org/wiki/Central_African_Republic"),
    ("Oubangui Médias · Centrafrique: les travaux de réhabilitation de l'Hôpital de l'Amitié avancent à grands pas (09-03-2026)", "https://oubanguimedias.com/2026/03/09/centrafrique-les-travaux-de-rehabilitation-de-lhopital-de-lamitie-avancent-a-grands-pas/"),
    ("Petit Futé · Hôpital Communautaire, Bangui (consultado 18-09-2026)", "https://www.petitfute.co.uk/v57171-bangui/c1172-pense-fute-services/c1136-sante/361792-hopital-communautaire.html"),
    ("ADF Magazine · Russia Pushes CAR to Choose Africa Corps Over Wagner Mercenaries (octubre de 2025)", "https://adf-magazine.com/2025/10/russia-pushes-car-to-choose-africa-corps-over-wagner-mercenaries/"),
    ("France Diplomatie · République centrafricaine, Conseils aux voyageurs — Sécurité (Ministère de l'Europe et des Affaires étrangères, act. 15-09-2026)", "https://www.diplomatie.gouv.fr/fr/information-par-pays/republique-centrafricaine/conseils-aux-voyageurs-securite"),
    ("France Diplomatie · République centrafricaine — Santé (consultado 18-09-2026)", "https://www.diplomatie.gouv.fr/fr/information-par-pays/republique-centrafricaine/conseils-aux-voyageurs-sante"),
    ("EUAA · COI Focus: République centrafricaine — Situation sécuritaire à Bangui (Cedoca, Bélgica, 21-01-2026)", "https://coi.euaa.europa.eu/administration/belgium/PLib/COI_Focus_R%C3%A9publique_centrafricaine_(RCA)_Situation_s%C3%A9curitaire_%C3%A0_Bangui_20260121.pdf"),
    ("MAEC · Ficha País: República Centroafricana (Oficina de Información Diplomática, PDF)", "https://www.exteriores.gob.es/Documents/FichasPais/REPUBLICACENTROAFRICANA_FICHA%20PAIS.pdf"),
    ("BOE · Texto íntegro del Reglamento de Ejecución (UE) 2026/636 con sus anexos, en PDF", "https://www.boe.es/doue/2026/636/L00001-00007.pdf"),
    ("AllAfrica · Afrique Centrale: Les corridors de la région perdent encore des camions sans que personne ne sache exactement où (18-09-2026)", "https://fr.allafrica.com/stories/202609180755.html"),
    ("Ministère de la Santé et de la Population de la RCA · Réhabilitation et extension de l'Hôpital de l'Amitié sino-centrafricaine", "https://www.sante.gouv.cf/mission/330"),
    ("FANAF · Carte Rose CEMAC, carta internacional de seguro de responsabilidad civil automóvil", "http://fanaf.org/article/cartes-internationales-d-assurance-8/carte-rose-cemac-65/"),
    ("Corbeau News Centrafrique · Carte Rose CEMAC: un projet d'intégration régionale qui ne fonctionne pas", "https://corbeaunews-centrafrique.org/carte-rose-cemac-un-projet-dintegration-regionale-qui-ne-fonctionne-pas/"),
    ("Recomendaciones de viaje del MAEC · República Centroafricana", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica+Centroafricana"),
    ("Bangui (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bangui"),
    ("Boganda Museum (Wikipedia EN)", "https://en.wikipedia.org/wiki/Boganda_Museum"),
    ("Boali (Wikipedia EN)", "https://en.wikipedia.org/wiki/Boali"),
    ("Excursión Boali Falls y lago de cocodrilos (operador local)", "https://www.centralafricanrepublictours.com/day-tours/bangui-boali-falls-and-crocodile-lake/"),
    ("Mbaïki (Wikipedia EN)", "https://en.wikipedia.org/wiki/Mba%C3%AFki"),
    ("Lobaye (Wikipedia EN)", "https://en.wikipedia.org/wiki/Lobaye"),
    ("Bayanga (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bayanga"),
    ("UNESCO · Sangha Trinational (lista, nº 1380)", "https://whc.unesco.org/en/list/1380"),
    ("Dzanga-Sangha · web oficial del área protegida", "https://dzanga-sangha.org/"),
    ("Dzanga-Sangha Special Reserve (Wikipedia EN)", "https://en.wikipedia.org/wiki/Dzanga-Sangha_Special_Reserve"),
    ("Dzanga Bai (Wikipedia EN)", "https://en.wikipedia.org/wiki/Dzanga_Bai"),
    ("Dzanga-Ndoki National Park (Wikipedia EN)", "https://en.wikipedia.org/wiki/Dzanga-Ndoki_National_Park"),
    ("Berbérati (Wikipedia EN)", "https://en.wikipedia.org/wiki/Berb%C3%A9rati"),
    ("UNESCO · Les mégalithes de Bouar (lista indicativa, nº 4003)", "https://whc.unesco.org/en/tentativelists/4003/"),
    ("Bouar (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bouar"),
    ("Lista de bienes del Patrimonio Mundial en RCA (Wikipedia EN)", "https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_Central_African_Republic"),
    ("UNESCO · Manovo-Gounda St Floris National Park (lista, nº 475)", "https://whc.unesco.org/en/list/475"),
    ("UICN World Heritage Outlook · Manovo-Gounda St Floris", "https://worldheritageoutlook.iucn.org/node/1023"),
    ("Manovo-Gounda St Floris National Park (Wikipedia EN)", "https://en.wikipedia.org/wiki/Manovo-Gounda_St_Floris_National_Park"),
    ("Bamingui-Bangoran National Park and Biosphere Reserve (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bamingui-Bangoran_National_Park_and_Biosphere_Reserve"),
    ("N'Délé (Wikipedia EN)", "https://en.wikipedia.org/wiki/N%27D%C3%A9l%C3%A9"),
    ("Ndélé (Wikipedia FR)", "https://fr.wikipedia.org/wiki/Nd%C3%A9l%C3%A9"),
    ("African Parks · Chinko (página oficial del parque)", "https://www.africanparks.org/the-parks/chinko"),
    ("Chinko (Wikipedia EN)", "https://en.wikipedia.org/wiki/Chinko"),
    ("Kembé Falls (Wikipedia EN)", "https://en.wikipedia.org/wiki/Kemb%C3%A9_Falls"),
    ("Kembé (Wikipedia EN)", "https://en.wikipedia.org/wiki/Kemb%C3%A9"),
    ("Bangassou (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bangassou"),
    ("Bambari (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bambari"),
    ("Birao (Wikipedia EN)", "https://en.wikipedia.org/wiki/Birao"),
]

# Bucle suroeste: Camerún → Bouar → Bangui → Dzanga-Sangha → Berbérati → Camerún
CORRIDOR = [
    (5.93888, 15.59287),
    (5.267, 17.65),
    (4.87336, 18.04957),
    (4.36451, 18.57713),
    (3.8665, 17.98281),
    (3.533, 16.067),
    (2.90174, 16.26987),
    (2.95391, 16.36511),
    (3.1, 16.333),
    (2.50001, 16.16656),
    (3.533, 16.067),
    (4.25711, 15.78794),
    (4.94, 15.87),
    (5.93888, 15.59287),
]

# Ejes este y noreste (RN2 y RN8) · TRAZADO TEÓRICO, zona vetada por el MAEC
CORRIDOR_ALT = [
    (4.36451, 18.57713),
    (5.73778, 19.08667),
    (5.76434, 20.67053),
    (4.61474, 21.88667),
    (4.73786, 22.81651),
    (6.05139, 23.89639),
    (8.41176, 20.64897),
    (8.183, 20.233),
    (9.0, 21.5),
    (10.29348, 22.78479),
]

HISTORIA_RESUMEN = "La República Centroafricana es un país interior de unos 623.000 kilómetros cuadrados y cinco millones y medio de habitantes que acumula recursos —diamantes, oro, madera, uranio— y una de las rentas por habitante más bajas del mundo. Desde la independencia de Francia en 1960 ha encadenado golpes de Estado, el imperio de Bokassa y, desde 2013, una guerra civil que vació el Estado de buena parte del territorio. El acuerdo de paz de 2019 no la cerró: el Gobierno de Faustin-Archange Touadéra se sostiene sobre la misión de la ONU y sobre operadores militares rusos. Para el viajero es, a fecha de septiembre de 2026, un país cerrado: España desaconseja el viaje bajo cualquier circunstancia."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>El poblamiento de la cuenca del Ubangui es muy antiguo. Britannica recoge que prospectores de diamantes han hallado en el país herramientas pulidas de sílex y cuarzo de al menos ocho mil años, y que hace unos dos mil quinientos años comunidades agrícolas levantaron los megalitos de las cercanías de Bouar, señal de sociedades ya organizadas. La Wikipedia inglesa sitúa esos megalitos entre el 3500 y el 1700 antes de nuestra era.</p><p>Hasta el siglo XV la región era un mosaico de asentamientos pequeños y relativamente aislados, dedicados a la caza y a la roza. Lo que rompió ese equilibrio fue la trata. Desde el siglo XVII los tratantes de esclavos de habla árabe extendieron sus rutas hasta aquí, y a mediados del XIX pueblos como los bobangi se convirtieron en intermediarios que razziaban a baya y mandjia; Britannica subraya que aquella violencia desarticuló sociedades enteras y dejó tensiones que todavía pesan.</p><p>De ese siglo XIX datan también los Estados mejor documentados del territorio: el sultanato de <strong>Dar al-Kuti</strong> en el norte y los reinos <strong>zande</strong> y <strong>bandia</strong>, entre ellos el de Bangassou, fundado por los bandia-nzakara. Desde 1875 el sultán sudanés Rabih az-Zubayr dominó el Alto Ubangui, hasta que los franceses lo derrotaron en la batalla de Kousséri en 1900.</p>"),
    ("Colonización",
     "<p>La penetración europea fue tardía y rápida. En 1889 los franceses instalaron un puesto comercial en el río Ubangui que sería Bangui —la Wikipedia en español lo atribuye a la iniciativa de Pierre Savorgnan de Brazza— y en 1894 Francia declaró territorio francés el <strong>Ubangui-Chari</strong>. Hacia 1903 el control estaba consolidado y entre 1906 y 1910 la colonia quedó integrada en el África Ecuatorial Francesa, gobernada desde Brazzaville.</p><p>El modelo de explotación fue el de las <em>compañías concesionarias</em>: París repartió el territorio entre empresas privadas que recibieron el monopolio del caucho, el algodón y la madera a cambio de un canon. La Wikipedia en español describe sin rodeos los «métodos brutales y atroces» empleados para arrancar trabajo a la población. El trabajo forzado, los cupos de recolección y los castigos provocaron despoblamiento y huidas masivas, y acabaron desembocando en la <strong>rebelión Kongo-Wara</strong> de 1928 a 1931, que la Wikipedia inglesa califica como quizá la mayor revuelta anticolonial del África de entreguerras.</p><p>La herencia colonial explica buena parte del país actual: unas fronteras trazadas sobre el mapa, una economía orientada a la extracción y a la exportación, una red de carreteras mínima para un territorio del tamaño de Francia y España juntas, y el francés como lengua de la administración.</p>"),
    ("Independencia y construcción del Estado",
     "<p>El 1 de diciembre de 1958 Ubangui-Chari se convirtió en territorio autónomo dentro de la Comunidad Francesa bajo <strong>Barthélemy Boganda</strong>, figura fundacional del país, muerto en accidente aéreo el 29 de marzo de 1959. La independencia llegó el <strong>13 de agosto de 1960</strong>, con David Dacko como presidente. Hacia 1962 Dacko había construido un Estado de partido único y en enero de 1964 se hizo elegir sin oposición.</p><p>La noche del 31 de diciembre de 1965 el coronel <strong>Jean-Bédel Bokassa</strong> derrocó a su primo Dacko y se dirigió al país por radio la madrugada del 1 de enero de 1966. En marzo de 1972 se proclamó presidente vitalicio y el 4 de diciembre de 1976 convirtió la república en el <strong>Imperio Centroafricano</strong>. Su coronación como Bokassa I, el 4 de diciembre de 1977, costó unos veinte millones de dólares, cerca de un tercio del presupuesto anual. En abril de 1979 un centenar de escolares detenidos murieron a golpes en la prisión de Ngaragba; la <em>Operación Barracuda</em> francesa lo derribó entre el 19 y el 21 de septiembre de 1979.</p><p>André Kolingba dio un nuevo golpe el 1 de septiembre de 1981 y gobernó doce años. En 1993 las primeras elecciones multipartidistas llevaron al poder a <strong>Ange-Félix Patassé</strong>, con el 52,5 por ciento en segunda vuelta; los motines militares de 1996 y 1997 cerraron la década.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>El 25 de octubre de 2002 el general <strong>François Bozizé</strong> atacó aprovechando un viaje de Patassé y tomó el poder en 2003; en 2004 estalló la primera guerra civil, cerrada en falso con el acuerdo de Birao de abril de 2007.</p><p>En diciembre de 2012 la coalición rebelde <strong>Séléka</strong> tomó N'Délé y el norte, y el <strong>24 de marzo de 2013</strong> entró en Bangui: Bozizé huyó al Congo y Michel Djotodia se proclamó presidente al día siguiente. Disolvió formalmente Séléka el 13 de septiembre de 2013 sin controlar a sus mandos, y como reacción surgieron las milicias <strong>antibalaka</strong>, que el 5 de diciembre atacaron Bangui en una jornada con más de mil civiles muertos. Francia desplegó la operación Sangaris y Djotodia dimitió el 10 de enero de 2014.</p><p>El Consejo de Seguridad creó la <strong>MINUSCA</strong> por la resolución 2149, de 10 de abril de 2014; la misión tomó el relevo el 15 de septiembre. Touadéra ganó las presidenciales de febrero de 2016. El <strong>acuerdo de paz</strong> firmado en Jartum el 5 de febrero de 2019 y rubricado en Bangui al día siguiente reunió al Gobierno y a catorce grupos armados, pero no cerró la guerra: la coalición CPC, formada el 19 de diciembre de 2020, atacó Bangui el 13 de enero de 2021 y fue repelida con apoyo ruso. Ha desplazado a más de 1,1 millones de personas.</p>"),
    ("Política y gobierno en 2026",
     "<p>A fecha de septiembre de 2026 el jefe del Estado es <strong>Faustin-Archange Touadéra</strong>, presidente desde 2016 y reelegido en 2020, en un régimen presidencialista. El referéndum del <strong>30 de julio de 2023</strong> alargó el mandato de cinco a siete años y suprimió el límite de dos mandatos, con un 95,03 por ciento de síes y una participación oficial del 57,23 que la oposición, que lo boicoteó, cifró por debajo del 15. En las generales del <strong>28 de diciembre de 2025</strong> Touadéra obtuvo un tercer mandato con el 76,15 por ciento provisional, frente al 14,66 de Anicet-Georges Dologuélé y el 3,19 de Henri-Marie Dondra.</p><p>Freedom House lo clasifica en 2025 como <em>Not Free</em>, «no libre», con <strong>5 puntos sobre 100</strong>: 1 sobre 40 en derechos políticos y 4 sobre 60 en libertades civiles. Con los límites de mandato suprimidos y la oposición reprimida, en la práctica es un régimen autoritario, no una democracia. Reporteros Sin Fronteras lo sitúa en 2026 en el puesto 81 de 180, con 56,73 puntos, y describe medios bajo control ruso desde 2018.</p><p>La Unión Africana advirtió el 9 de abril de 2026 de que los recortes de MINUSCA están cerrando bases y crean «un riesgo real de vacío de seguridad». España desaconseja «el viaje bajo cualquier circunstancia», sin embajada residente —depende de la de Camerún—, y la Unión Europea es el principal donante.</p>"),
    ("Economía y recursos",
     "<p>Según el Banco Mundial, el producto interior bruto de 2025 fue de unos 3.070 millones de dólares para 5,51 millones de habitantes, alrededor de <strong>556 dólares por habitante</strong>, con un crecimiento del 4,5 por ciento. El 71,6 por ciento de la población vivía en 2021 por debajo de los tres dólares diarios en paridad de poder adquisitivo, y la renta por habitante cayó entre un 45 y un 48 por ciento entre 2013 y 2022 por efecto de la guerra.</p><p>La moneda es el <strong>franco CFA de África Central</strong>, con paridad fija frente al euro a 655,957 francos. La ficha del Ministerio español, de 2018, describía una economía con la agricultura en torno al 58 por ciento del producto: mandioca, plátano, maíz, café, algodón y tabaco, en buena parte de subsistencia. Las exportaciones reales son madera y <strong>diamantes</strong>, a los que se suman oro, reservas de uranio en Bakouma y petróleo en Vakaga que nunca se han explotado a escala.</p><p>Esa riqueza mineral es hoy parte del problema. Los operadores militares rusos controlan la mina de oro de Ndassima a través de Midas Ressources, la comercializadora de diamantes Diamville desde 2019 y, desde 2021, explotaciones madereras en Lobaye asociadas a la empresa Bois Rouge. El turismo es marginal y se reduce, en la práctica, al suroeste forestal.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Viven en el país unos 5,5 millones de personas (Banco Mundial, 2025), con una esperanza de vida de 58 años y más de ochenta grupos de población con lengua propia. Los idiomas oficiales son el <strong>francés</strong> y el <strong>sango</strong>: el francés sirve en la administración y en la ciudad, pero por carretera uno se entiende en sango, la lengua vehicular.</p><p>Las cifras de religión varían según la fuente: para 2020 se da un 73,2 por ciento de cristianos, un 13,9 de musulmanes y un 12 de creencias tradicionales; la ficha española de 2018 daba un 25 por ciento de católicos, otro 25 de protestantes y un 15 de musulmanes, sobre todo norteños. Hay dos bienes UNESCO: el parque de <strong>Manovo-Gounda St Floris</strong>, de 1988, en la lista de <em>Patrimonio en Peligro desde 1997</em> por la caza furtiva de rinocerontes, elefantes y jirafas; y el <strong>Sangha Trinacional</strong>, de 2012, compartido con Camerún y Congo, cuya parte centroafricana es el parque de Dzanga-Ndoki, junto a Bayanga.</p><p>Conviene vestir de forma discreta y cubierta, sobre todo en el norte musulmán. Hay que pedir permiso antes de fotografiar personas y evitar militares, controles e instalaciones oficiales. El ramadán de 2027 empieza en torno al 8 de febrero: en el norte no se come ni se bebe en público de día. El alcohol es corriente en Bangui y el sur, pero mejor no beberlo ante interlocutores musulmanes.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha país República Centroafricana (MAEC España · PDF · marzo 2018)", "https://www.exteriores.gob.es/Documents/FichasPais/REPUBLICACENTROAFRICANA_FICHA%20PAIS.pdf"),
    ("Recomendaciones de viaje: República Centroafricana (MAEC España · actualizado 22/05/2024)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica+Centroafricana"),
    ("Central African Republic (Freedom House · Freedom in the World 2025)", "https://freedomhouse.org/country/central-african-republic/freedom-world/2025"),
    ("Central African Republic — History (Encyclopaedia Britannica · consultada 09/2026)", "https://www.britannica.com/place/Central-African-Republic/History"),
    ("República Centroafricana (Wikipedia en español · consultada 09/2026)", "https://es.wikipedia.org/wiki/Rep%C3%BAblica_Centroafricana"),
    ("Central African Republic (Wikipedia en inglés · consultada 09/2026)", "https://en.wikipedia.org/wiki/Central_African_Republic"),
    ("History of the Central African Republic (Wikipedia en inglés · consultada 09/2026)", "https://en.wikipedia.org/wiki/History_of_the_Central_African_Republic"),
    ("Jean-Bédel Bokassa (Wikipedia en inglés · consultada 09/2026)", "https://en.wikipedia.org/wiki/Jean-B%C3%A9del_Bokassa"),
    ("Central African Republic Civil War (Wikipedia en inglés · consultada 09/2026)", "https://en.wikipedia.org/wiki/Central_African_Republic_Civil_War"),
    ("Wagner Group activities in the Central African Republic (Wikipedia en inglés · consultada 09/2026)", "https://en.wikipedia.org/wiki/Wagner_Group_activities_in_the_Central_African_Republic"),
    ("2023 Central African constitutional referendum (Wikipedia en inglés · consultada 09/2026)", "https://en.wikipedia.org/wiki/2023_Central_African_constitutional_referendum"),
    ("CAR's top court confirms constitutional referendum results (Africanews · 22/08/2023)", "https://www.africanews.com/2023/08/22/central-african-republics-top-court-confirms-constitutional-referendum-results/"),
    ("El presidente Touadéra de la República Centroafricana gana las elecciones (SWI swissinfo.ch · enero 2026)", "https://www.swissinfo.ch/spa/el-presidente-touad%C3%A9ra-de-la-rep%C3%BAblica-centroafricana-gana-las-elecciones/90729845"),
    ("Comunicado de la 1338.ª reunión del Consejo de Paz y Seguridad de la UA sobre la RCA (Unión Africana · 09/04/2026)", "https://www.peaceau.org/en/article/communique-of-the-1338th-meeting-of-the-psc-held-on-9-april-2026-on-consideration-of-the-situation-in-the-central-african-republic-car"),
    ("About MINUSCA (Naciones Unidas · MINUSCA · consultada 09/2026)", "https://minusca.unmissions.org/en/about"),
    ("Political Agreement for Peace and Reconciliation (Khartoum Accord) (PA-X Peace Agreements Database · 2019)", "https://www.peaceagreements.org/agreements/wgg/2147/"),
    ("Central African Republic — States Parties (UNESCO World Heritage Centre · consultada 09/2026)", "https://whc.unesco.org/en/statesparties/cf"),
    ("Manovo-Gounda St Floris National Park (UNESCO World Heritage Centre · inscrito 1988)", "https://whc.unesco.org/en/list/475"),
    ("Sangha Trinational (UNESCO World Heritage Centre · inscrito 2012)", "https://whc.unesco.org/en/list/1380"),
    ("Dzanga-Sangha Special Reserve (Wikipedia en inglés · consultada 09/2026)", "https://en.wikipedia.org/wiki/Dzanga-Sangha_Special_Reserve"),
    ("Central African Republic (Reporteros Sin Fronteras · Índice de Libertad de Prensa 2026)", "https://rsf.org/en/country/central-african-republic"),
    ("Central African Republic — Data (Banco Mundial · datos 2024-2025)", "https://data.worldbank.org/country/central-african-republic"),
]

SPEC = dict(
    slug="rca", name="República Centroafricana", revision="18 sep 2026",
    sub="EXCLUIDO POR PROTOCOLO — conflicto armado activo y desaconsejo total del MAEC · ficha informativa",
    chips=[
        ("ESTATUS", "EXCLUIDO POR PROTOCOLO. MAEC: se desaconseja el viaje bajo cualquier circunstancia y se pide a los españoles…"),
        ("CÓMO LLEGAR", "En avión a Bangui M'Poko (BGF): Ethiopian, ASKY, Royal Air Maroc, RwandAir, AfriJet…"),
        ("VISADO", "OBLIGATORIO y previo. Para españoles, la vía ordinaria es la Embajada de la RCA en París…"),
        ("VEHÍCULO", "Sin organización emisora de carnet de passages en el país (AIT/FIA)…"),
        ("SEGURIDAD", "MAEC: abandone el país · conflicto armado activo"),
        ("SEGURO", "Carta Verde no vale · Carte Rose CEMAC local"),
        ("SALUD", "Fiebre amarilla OBLIGATORIA · malaria alto riesgo"),
        ("DRONES", "No llevarlo · detención y confiscación"),
        ("STARLINK", "Operativo desde 16-03-2026 · 33.000 XAF/mes"),
        ("4x4", "Corredor único Béloko–Bangui · IED en el noroeste"),
        ("A PIE", "Descartado · secuestro frecuente fuera de Bangui"),
        ("PERRO", "Entrada con microchip, vacuna antirrábica de más de 2 semanas y menos de 6 meses y certificado sanitario…"),
        ("MONEDA", "Franco CFA de África Central (XAF), paridad fija: 1 EUR = 655,957 XAF…"),
        ("VENTANA", "Tropical. Estación de lluvias de mayo a noviembre…"),
    ],
    center=[6.4, 19.9], zoom=6,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle suroeste: Camerún → Bouar → Bangui → Dzanga-Sangha → Berbérati → Camerún",
    corridor_alt_label="Ejes este y noreste (RN2 y RN8) · TRAZADO TEÓRICO, zona vetada por el MAEC",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/African_forest_elephants_at_Dzanga_Bai,_Central_African_Republic.jpg?width=1200",
    hero_credit="Dzanga Bai · JosepMGracia · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="La República Centroafricana queda FUERA DE LA RUTA 2027 por protocolo, sin excepciones. El MAEC (actualización de 22 de mayo de 2024) no se limita a desaconsejar el viaje: «SE DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA Y SE RECOMIENDA A LOS ESPAÑOLES QUE SE ENCUENTREN EN EL PAÍS QUE LO ABANDONEN». El FCDO británico (28 de mayo de 2026) desaconseja todo viaje a todo el país salvo Bangui, y allí todo viaje no esencial. España no tiene embajada residente en Bangui: la competencia es de la Embajada en Yaundé (Camerún), a 1.000 km y dos fronteras de distancia, con un consulado honorario en Bangui como único apoyo sobre el terreno. Con guerra civil desde 2013, grupos armados en buena parte del territorio pese al acuerdo de Jartum de 2019, presencia rusa (Wagner y su sucesor Africa Corps) junto al ejército, secuestro criminal frecuente fuera de la capital y artefactos explosivos improvisados en el noroeste, ningún seguro de viaje español cubre el país y la asistencia en carretera es inexistente. Si algún día fuera viable, la única modalidad sensata sería un viaje APARTE, sin los vehículos: vuelo a Bangui (BGF) y chárter a Bayanga para Dzanga-Sangha, contratando un operador local que gestione visado, permisos y logística. Coste orientativo: 3.000–4.125 € el chárter Bangui–Bayanga (compartible), más vuelos, permisos y alojamiento; no menos de 6.000–8.000 € por persona. Lo que habría que decidir no es la ruta, sino si se acepta viajar a un país que el propio Estado español pide abandonar.",
    facts=[
        ("Estatus", "EXCLUIDO POR PROTOCOLO. MAEC: se desaconseja el viaje bajo cualquier circunstancia y se pide a los españoles que abandonen el país (22-05-2024). Ficha meramente informativa."),
        ("Cómo llegar", "En avión a Bangui M'Poko (BGF): Ethiopian, ASKY, Royal Air Maroc, RwandAir, AfriJet. Por tierra, el eje real es Duala–Garoua-Boulaï/Béloko–Bangui, por donde pasa el 80 % de las importaciones. Al suroeste turístico (Bayanga), chárter de 50 min desde Bangui, 500 km de pista, o barco por el río Sangha desde Congo y Camerún."),
        ("Visado", "OBLIGATORIO y previo. Para españoles, la vía ordinaria es la Embajada de la RCA en París (30 rue des Perchamps, 75016). El «visa volant» a la llegada existe pero lo tramitan operadores locales con carta de invitación."),
        ("Vehículo/aduana", "Sin organización emisora de carnet de passages en el país (AIT/FIA). Para un vehículo extranjero, admisión temporal con laissez-passer aduanero; el CPD emitido en España sigue siendo la vía limpia. POR CONFIRMAR con la aduana centroafricana."),
        ("Seguro", "Carta Verde NO cubre. Rige el seguro regional CEMAC (Carte Rose), que debe contratarse en la zona. Ninguna póliza española de asistencia en viaje cubre un país con desaconsejo total del MAEC."),
        ("Moneda", "Franco CFA de África Central (XAF), paridad fija: 1 EUR = 655,957 XAF. Economía de efectivo; el MAEC señala que solo se acepta VISA, y únicamente en agencias aéreas y hoteles internacionales."),
        ("Perro", "Entrada con microchip, vacuna antirrábica de más de 2 semanas y menos de 6 meses y certificado sanitario internacional de menos de 72 horas. No hay página oficial nacional verificada; dato de fuente veterinaria secundaria."),
        ("Drones", "Sin normativa nacional localizada en fuente oficial. El MAEC sí prohíbe fotografiar instalaciones militares, aeropuertos y puertos, y el FCDO advierte de detención y confiscación de cámaras. Volar un dron aquí es un riesgo de detención."),
        ("Starlink", "OPERATIVO desde el 16 de marzo de 2026, licencia aprobada en diciembre de 2025. Residencial 33.000 XAF/mes (~57 USD); kit estándar 240.000 XAF, kit mini 123.000 XAF."),
        ("Seguridad", "Conflicto armado activo desde 2013. Grupos armados en el norte y el sureste, secuestro criminal frecuente fuera de Bangui, controles ilegales y artefactos explosivos improvisados en el noroeste (FCDO, 28-05-2026)."),
        ("Clima", "Tropical. Estación de lluvias de mayo a noviembre, durante la cual el FCDO describe las carreteras como «en condiciones extremadamente malas». La ventana seca practicable es de diciembre a abril."),
        ("Sanidad", "Fiebre amarilla OBLIGATORIA con certificado internacional para todo mayor de 9 meses. País de alto riesgo de malaria. Brote activo de mpox clado I (TravelHealthPro, marzo de 2026). Sanidad pública mínima; evacuación médica imprescindible."),
    ],
    alerts=[
        "El MAEC no solo desaconseja el viaje: pide a los españoles que se encuentren en el país que LO ABANDONEN (actualización de 22 de mayo de 2024). Es el escalón máximo del sistema español y basta por sí solo para excluir el país de la ruta.",
        "España NO tiene embajada residente en Bangui. La competencia consular es de la Embajada de España en Yaundé (Camerún) y el único apoyo sobre el terreno es un consulado honorario. Emergencia consular: +237 698 44 79 00.",
        "El FCDO británico (28 de mayo de 2026) desaconseja todo viaje a todo el país salvo Bangui, y en Bangui todo viaje que no sea esencial. Reino Unido tampoco tiene embajada y atiende a distancia desde la RDC.",
        "Secuestro criminal frecuente fuera de Bangui. El FCDO documenta controles de carretera ilegales y ataques indiscriminados a viajeros en zonas remotas, con robo de vehículos, heridos y muertos.",
        "Hay artefactos explosivos improvisados sin identificar en el noroeste del país (FCDO). Esto afecta directamente al eje por el que entra el tráfico desde Camerún.",
        "El MAEC señala expresamente la «inexistencia de fuerzas de seguridad» y desaconseja circular solo, sobre todo de noche. No existe asistencia en carretera de ningún tipo.",
        "Presencia militar rusa junto al ejército centroafricano: Wagner primero y, desde 2025, su transición al Africa Corps estatal. Añade un actor armado más ante el que un extranjero con dos 4x4 y cámaras es sospechoso por defecto.",
        "Fotografiar instalaciones militares, aeropuertos y puertos está prohibido (MAEC). El FCDO advierte de que a menudo hace falta permiso incluso para fotografiar en la vía pública, con riesgo de detención y confiscación del equipo.",
        "Ninguna aseguradora española de asistencia en viaje cubre estancias en países con desaconsejo total del MAEC: sin cobertura no hay evacuación médica, y la sanidad local no permite tratar un politraumatismo.",
        "France Diplomatie (act. 15 de septiembre de 2026, la fuente más reciente disponible) mantiene TODO el país fuera de Bangui y Bimbo en zona ROJA formalmente desaconsejada. Tres cancillerías europeas coinciden: no es una lectura española aislada.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada por Camerún", "Garoua-Boulaï (frontera) → Baboua → Bouar", "~160 km · 1 día"),
        ("2 · Los megalitos", "Bouar y los tazunu de los alrededores", "~60 km · 1 día"),
        ("3 · Hacia el centro", "Bouar → Baoro → Bossembélé", "~290 km · 2 días"),
        ("4 · El salto del Mbali", "Bossembélé → Boali (cataratas) → Bangui", "~160 km · 1 día"),
        ("5 · Base Bangui", "Bangui: mercado, catedral, Ubangui, permisos y taller", "0 km · 2 días"),
        ("6 · La Lobaye", "Bangui → Mbaïki y la selva de Lobaye", "~110 km · 1 día"),
        ("7 · Bajada al Sangha", "Mbaïki → Boda → Nola", "~330 km · 2 días"),
        ("8 · Puerta del bosque", "Nola → Bayanga (pista)", "~100 km · 1 día"),
        ("9 · Dzanga-Sangha", "Bayanga: Dzanga Bai, Bai Hokou (Dzanga-Ndoki), BaAka", "~60 km · 3 días"),
        ("10 · Vuelta al oeste", "Bayanga → Nola → Berbérati", "~280 km · 2 días"),
        ("11 · Cierre del bucle", "Berbérati → Carnot → Bouar", "~340 km · 2 días"),
        ("12 · (Alt) Eje este I", "Bangui → Sibut → Bambari", "~380 km · 2 días"),
        ("13 · (Alt) Eje este II", "Bambari → Kembé (cataratas) → Bangassou", "~330 km · 2 días"),
        ("14 · (Alt) Eje noreste", "Sibut → Kaga-Bandoro → Ndélé → Manovo-Gounda → Birao", "~1.100 km · 5 días"),
    ],
    offroad=[
        "El único eje asfaltado continuo del país es el Bangui–Bossembélé–Bouar–Garoua-Boulaï (RN1/RN3): el enlace asfaltado con Camerún no se completó hasta 2020, y al norte de Bossembélé la RN1 pasa a tierra estrecha y mal desarrollada hasta la frontera chadiana, en Békoro (fuente: Wikipedia N1 road).",
        "La pista Bangui–Bayanga es la ruta 4x4 de referencia del país: 500 km en 12 a 15 horas de conducción sobre firme en muy mal estado, según la propia web del área protegida de Dzanga-Sangha; el último tramo, Nola–Bayanga (102 km), es el que primero se corta con la lluvia.",
        "Dentro de Dzanga-Sangha y Dzanga-Ndoki NO se circula libremente: todas las pistas internas hacia Dzanga Bai, Bai Hokou y Mongambe exigen permiso, guardia del parque a bordo y rastreador BaAka, y se recorren en 4x4 hasta el inicio de los senderos.",
        "El eje este (RN2 Bangui–Sibut–Bambari–Kembé–Bangassou) es tierra a partir de Sibut, que marca el final del asfalto desde Bangui; Bambari y Kembé han cambiado de manos repetidamente y el MAEC cita Bambari entre las ciudades especialmente peligrosas: tramo VETADO.",
        "El eje noreste (RN8 Sibut–Kaga-Bandoro–Ndélé–Birao, 648 km solo hasta Ndélé) es pista integral y atraviesa el parque de Manovo-Gounda St Floris; en Birao hay base permanente del grupo ruso Wagner desde diciembre de 2022 y en estación de lluvias el transporte local vuelve al burro y el caballo: tramo VETADO.",
        "Chinko, en el sureste, no tiene acceso rodado turístico documentado: African Parks no publica ninguna información de visita y el acceso real es logístico y con autorización; el área sufrió presión del LRA y de ganaderos armados desde 2012.",
        "Los pasos fronterizos utilizables son Garoua-Boulaï y Kenzou/Gamboula con Camerún (por el oeste), el río Sangha desde Ouesso (Congo) o Libongo (Camerún) hacia Bayanga, y el transbordador del Mbomou en Bangassou hacia la RDC; todas las zonas fronterizas están señaladas por el MAEC como de peligro excepcional.",
        "Nada de esto se puede hacer sin papeles: el visado se obtiene en París o como visa volant con carta de invitación tramitada por un operador local, y la circulación interior exige permiso; los controles de carretera son constantes y están en manos mezcladas de FACA, Wagner y gendarmería.",
    ],
    senderismo=[
        "Rastreo de gorilas de llanura occidentales desde Bai Hokou (Dzanga-Ndoki): salida a pie al amanecer con rastreadores BaAka tras un grupo habituado desde el programa de habituación iniciado en 1997; cupo diario muy corto y permiso obligatorio.",
        "Sendero y pasarela de Dzanga Bai: 12 km de pista desde Bayanga y después unos minutos a pie por pasarela hasta la plataforma elevada sobre el claro salino de 10 hectáreas; es la caminata más rentable del país.",
        "Caza con red y recolección con las comunidades BaAka en la reserva de Dzanga-Sangha: jornada a pie por el sotobosque acompañando a los cazadores, incluida en la oferta del área protegida.",
        "Mongambe, el segundo campamento de investigación del sector Dzanga: acceso a pie por sendero forestal desde el final de la pista, con guardia del parque.",
        "Bajada a las pozas de las cataratas de Boali: en estación seca se desciende por escaleras de hormigón hasta el pie del salto, y hay una pasarela colgante de cables y tablones sobre el río; corta pero expuesta si hay caudal.",
        "Subida al tata del sultán Senoussi en Ndélé: ascenso corto por la colina que domina el valle del Méagoulou hasta el recinto amurallado; en la zona están también las cuevas de Kaga-Kpoungouvou, en la lista indicativa de la UNESCO desde 2006. Zona vetada.",
        "Paseos por los campos de megalitos tazunu de Bouar: los yacimientos están dispersos por unos 7.500 km² alrededor de la ciudad, junto a manantiales, y se recorren a pie desde el punto donde se deja el vehículo; imprescindible guía local, no hay señalización.",
        "POR CONFIRMAR: no he encontrado ninguna fuente que describa senderos señalizados, balizados o cartografiados en ningún punto del país. Todo lo anterior son recorridos guiados, no rutas autoguiadas.",
    ],
    acampada=[
        "NO existe ninguna red de campings en República Centroafricana: no he localizado ni una sola ficha de camping establecido en el país en las fuentes consultadas.",
        "La única infraestructura de alojamiento verificada fuera de Bangui es la de Bayanga: Doli Lodge, citado por la web oficial del área protegida de Dzanga-Sangha, y Sangha Lodge; en sus recintos es donde se puede aparcar y pernoctar con dos 4x4.",
        "En Bangui, la pernocta razonable es dentro del recinto cerrado de un hotel o de una misión, con vehículo vigilado: la propia EUAA documenta una escalada de braquages nocturnos con arma de fuego en 2025 en los distritos 3, 5, 6 y 8.",
        "La acampada libre es DESACONSEJABLE en todo el país: los controles de carretera están en manos mezcladas de FACA, Wagner y grupos armados, y el MAEC advierte de peligro excepcional en todas las zonas fronterizas.",
        "Fuera de Bangui y Bayanga, el recurso habitual de los viajeros es la misión católica o el recinto de una empresa (aserradero, minera), negociado con antelación; es lo que se hace en Mbaïki, Nola, Berbérati y Bangassou.",
        "Las cataratas de Kembé fueron durante años parada habitual de los viajeros overland del eje este, según Wikipedia, pero el pueblo seguía bajo control de la UPC en abril de 2022: hoy no es un sitio donde dormir.",
        "FUENTE QUE FALLA: no he podido consultar fichas de iOverlander ni de Tracks4Africa para la RCA; las búsquedas devuelven campings de Tanzania y Sudáfrica, no del país. Por tanto, ninguna de las líneas anteriores se apoya en datos de acampada verificados sobre el terreno.",
        "Regla práctica para este viaje: planificar por etapas que terminen SIEMPRE en recinto cerrado y con luz, y no contar con ningún punto de acampada informal.",
    ],
    visado=[
        "VISADO OBLIGATORIO y PREVIO para españoles. No hay exención ni acuerdo de supresión con España.",
        "Vía ordinaria: Embajada de la República Centroafricana en PARÍS, 30 rue des Perchamps, 75016 (MAEC, 22-05-2024). No hay representación centroafricana en España.",
        "Pasaporte con validez mínima de SEIS MESES a la fecha de entrada, y certificado internacional de vacunación de fiebre amarilla exigido en el control fronterizo.",
        "Existe un «visa volant» a la llegada a Bangui, pero lo gestionan operadores locales con carta de invitación tramitada con dos semanas de antelación y, según ellos, exige contratar al menos un tour. No es un visado en frontera de libre acceso.",
        "Coste: la web de Dzanga-Sangha cifra el visado en 50 €. Tarifa y procedimiento POR CONFIRMAR directamente con la Embajada en París, que según el FCDO puede cambiarlos sin previo aviso.",
        "Validez en frontera TERRESTRE por confirmar: no hay fuente que garantice que un visado obtenido en París se acepta sin fricción en Béloko o Zongo. Asumir que puede exigirse ordre de mission para moverse fuera de Bangui.",
    ],
    fronteras_rows=[
        ("Aeropuerto internacional", "Bangui M'Poko (BGF/FEFF), 4,3985 N / 18,5188 E", "Única entrada realista. Operan Ethiopian Airlines, ASKY, Royal Air Maroc, RwandAir y AfriJet (Wikipedia, consultada 18-09-2026). Fiebre amarilla y visado previo exigidos en el control."),
        ("Paso terrestre principal", "Garoua-Boulaï (Camerún) – Béloko (RCA), 5,9353 N / 14,6056 E", "Corredor de suministro de Duala. La aduana de Béloko canaliza el 80 % de las importaciones del país. Camerún inauguró el 5 de septiembre de 2025 un hub logístico en Garoua-Boulaï con capacidad para 200 camiones, motivado expresamente por la inseguridad vial del corredor (Business in Cameroon, 08-09-2025)."),
        ("Paso terrestre secundario (Camerún)", "Kenzou (Camerún) – Gamboula (RCA)", "Ruta alternativa desde Yaundé citada por operadores locales de transfer por carretera. Estado operativo y horarios POR CONFIRMAR: no hay fuente oficial abierta en esta sesión."),
        ("Paso fluvial", "Bangui – Zongo (RD Congo), río Ubangui", "Cruce en barca con trámite de inmigración; operadores locales lo ofrecen como transfer asistido hacia Gemena. No es un paso apto para vehículos propios. Precaución: en 2024 hubo un desastre fluvial con numerosas víctimas en Bangui."),
        ("Paso terrestre este", "Bangassou (RCA) – Ndu (RD Congo)", "Zona sureste con presencia de grupos armados según el FCDO (28-05-2026). Sin fuente abierta que confirme apertura a extranjeros. POR CONFIRMAR."),
        ("Paso terrestre norte", "Sido (frontera con Chad)", "Eje norte hacia Sarh. Sin fuente abierta en esta sesión sobre su estado 2025-2026 ni sobre quién lo controla. POR CONFIRMAR."),
        ("Paso terrestre noreste", "Bambouti (frontera con Sudán del Sur)", "Extremo oriental, zona históricamente sin control estatal efectivo. Operadores ofrecen transfer por carretera RCA–Sudán del Sur, pero no hay confirmación oficial de paso habilitado. POR CONFIRMAR."),
        ("Acceso al suroeste turístico", "Bayanga / Dzanga-Sangha (vía aérea o fluvial)", "Chárter desde Bangui, 50 minutos, pista de laterita de 1,4 km (operadores Lapara Centrafrique y Via Air), 3.000–4.125 €. Por carretera desde Bangui, unos 500 km y 12–15 horas. También se llega en barco por el río Sangha desde Ouesso (Congo) y Libongo (Camerún)."),
    ],
    vehiculos=[
        "Se conduce por la DERECHA. Permiso de conducción internacional recomendable junto al español; requisito exacto POR CONFIRMAR con la aduana centroafricana.",
        "CARNET DE PASSAGES: la base de datos de la AIT/FIA (carnetdepassage.org) indica que NO existe organización emisora de CPD en la República Centroafricana. Eso dice quién lo emite, no si el país lo exige a la entrada: el dato de exigencia queda POR CONFIRMAR.",
        "Para un vehículo matriculado en España, la vía documental es la admisión temporal con laissez-passer aduanero emitido en el puesto fronterizo, o bien un CPD emitido por el RACE antes de salir. El CPD evita depositar fianza y es lo que funciona en el resto de la región.",
        "SEGURO: la Carta Verde europea NO tiene validez aquí. Rige la Carte Rose CEMAC, el seguro regional de responsabilidad civil de la Comunidad Económica y Monetaria de África Central, que se contrata en la zona (no desde España). Su funcionamiento real está cuestionado incluso por la prensa centroafricana.",
        "La Carte Brune CEDEAO (África Occidental) y la Yellow Card COMESA (África Oriental y Austral) NO cubren la RCA: es zona CEMAC. Hay que cambiar de tarjeta regional al entrar desde Camerún.",
        "El eje N3 desde Béloko hasta Bangui es el único corredor con tráfico pesado regular. El FCDO describe las carreteras como en condiciones extremadamente malas, sobre todo de mayo a noviembre, y advierte de no salir de las rutas principales.",
        "Controles de carretera oficiales e ilegales a lo largo del recorrido, con petición de soborno documentada por el FCDO. Un Ineos Grenadier y un Delica con matrícula española son un objetivo llamativo en este contexto.",
        "ESCOLTA ARMADA: NO consta obligación para particulares. France Diplomatie (act. 15-09-2026) no exige ni recomienda escolta o convoy; solo advierte de «coupeurs de route» en ejes principales y secundarios y de no circular de noche. Lo que sí está documentado es la escolta del TRANSPORTE DE MERCANCÍAS: convoyes de camiones bajo protección de cascos azules (convoyes automáticos de 60 vehículos ya en 2015 según Ecofin Agency, y escolta de la MINUSCA según el Consejo Nacional de Cargadores de Camerún). Es un servicio a la logística profesional, no algo a lo que pueda acogerse un viajero particular.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Sin normativa nacional de drones localizada en fuente oficial centroafricana en esta sesión. Las bases de datos comerciales de legislación de drones recogen fichas del país, pero ninguna cita un texto legal vigente verificable.",
        "PROHIBIDO fotografiar sitios y emplazamientos militares, aeropuertos y puertos (MAEC, 22-05-2024). Esta prohibición se aplica a cualquier soporte, incluida la cámara de un dron.",
        "El FCDO (28-05-2026) advierte de que a menudo se necesita permiso para hacer fotos en lugares públicos y de que hay riesgo de detención o confiscación de la cámara.",
        "Registros y detenciones arbitrarias por parte de policía y grupos armados afectan tanto a nacionales como a extranjeros (FCDO). Un dron en el equipaje es material probatorio en su contra.",
        "Regla operativa de la expedición: si el país estuviera alguna vez en ruta, el dron viajaría precintado y declarado, y no se volaría sin autorización escrita de la autoridad de aviación civil. En la práctica, no se lleva.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "OPERATIVO. Starlink se lanzó oficialmente en la República Centroafricana el 16 de marzo de 2026, tras la aprobación de su licencia en diciembre de 2025 por el Ministerio de Economía Digital, Correos y Telecomunicaciones (Space in Africa, 16-03-2026).",
        "Precios de lanzamiento: plan residencial 33.000 XAF/mes (~57 USD); kit estándar 240.000 XAF (~418 USD); kit mini 123.000 XAF (~214 USD).",
        "Es el 28.º mercado africano de Starlink y el segundo país africano incorporado en 2026, después de Senegal en febrero.",
        "Si Starlink Roaming cubre el país con un terminal comprado en Europa es un extremo POR CONFIRMAR en el mapa de disponibilidad de starlink.com, que no se ha podido abrir en esta sesión.",
        "Cobertura móvil terrestre: los operadores locales y la disponibilidad de SIM turística no se han podido verificar en fuente abierta. Fuera de Bangui y de las capitales de prefectura, asumir ausencia de datos móviles.",
    ],
    perro_intro=[
        "ENTRADA: los requisitos localizados son microchip, vacuna antirrábica administrada hace más de 2 semanas y menos de 6 meses, resto de vacunas al día y certificado sanitario internacional emitido por veterinario con menos de 72 HORAS de antelación a la llegada, acreditando que el animal está libre de parásitos.",
        "ATENCIÓN A LA FUENTE: estos requisitos proceden de una base de datos veterinaria francesa de referencia (Anivetvoyage), no de una página oficial del Gobierno centroafricano. No se ha localizado el portal del servicio veterinario nacional. Tratar como ORIENTATIVO y confirmar antes de mover al animal.",
        "RAZAS PROHIBIDAS: no se ha localizado ninguna lista de razas prohibidas ni restringidas en la República Centroafricana. Ausencia de dato, no ausencia de norma.",
        "VUELTA A LA UE: COMPROBADO. La República Centroafricana NO figura en ninguno de los anexos del Reglamento de Ejecución (UE) 2026/636, de 20 de marzo de 2026. En las listas no hay ningún país africano continental: los únicos territorios africanos son Santa Elena y Ascensión, ambos insulares. La RCA no es la excepción insular. Se aplica la vía de país NO LISTADO.",
        "Eso significa TITULACIÓN DE ANTICUERPOS ANTIRRÁBICOS (valoración serológica) hecha en laboratorio autorizado por la UE y ANOTADA EN EL PASAPORTE ANTES DE SALIR de España, más el periodo de espera reglamentario. La fuente veterinaria consultada lo confirma: la titulación no es obligatoria para entrar en el país, pero sí para volver.",
        "VETERINARIOS: no hay constancia de clínica veterinaria de referencia con estándar europeo en Bangui. Fuera de la capital, ninguna. Cualquier urgencia veterinaria implicaría evacuación a Yaundé o Duala.",
        "RIESGOS PARA EL PERRO: rabia presente en animales domésticos (TravelHealthPro), tripanosomiasis africana transmitida por la mosca tsé-tsé, calor y humedad tropicales, y parásitos. A esto se suma el riesgo de que el animal sea un problema en un control armado. No se lleva.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "FIEBRE AMARILLA OBLIGATORIA. Certificado internacional de vacunación exigido a todo viajero mayor de 9 meses bajo el Reglamento Sanitario Internacional, y comprobado en el control fronterizo (TravelHealthPro; MAEC).",
        "Vacunas recomendadas: hepatitis A, tétanos (refuerzo si han pasado más de 10 años), fiebre tifoidea, triple vírica, meningocócica ACWY, refuerzo de polio y rabia para actividades de riesgo (TravelHealthPro, marzo de 2026). El MAEC añade hepatitis B.",
        "MALARIA DE ALTO RIESGO en todo el país y todo el año. TravelHealthPro recomienda quimioprofilaxis con atovacuona/proguanil, doxiciclina o mefloquina, siempre junto a medidas de protección frente a picaduras.",
        "BROTE ACTIVO DE MPOX CLADO I según TravelHealthPro (marzo de 2026). El MAEC también cita riesgo de meningitis, cólera, VIH y mpox. El país está dentro del cinturón africano ampliado de la meningitis.",
        "Otros riesgos: dengue y chikungunya, rabia en animales domésticos, esquistosomiasis en aguas dulces y tripanosomiasis africana (enfermedad del sueño) transmitida por la mosca tsé-tsé.",
        "Agua y alimentos: higiene estricta, solo agua hervida o filtrada. El MAEC desaconseja el consumo de agua del grifo en todo el país.",
        "SANIDAD LOCAL MÍNIMA. Referencias en Bangui: Hôpital Communautaire de Bangui y Hôpital de l'Amitié (este último en obras de rehabilitación y ampliación en marzo de 2026). Ninguno equivale a un hospital europeo: cualquier urgencia grave exige evacuación médica aérea, que ningún seguro español cubre en un país con desaconsejo total.",
    ],
    seguridad_intro="Es el país más desaconsejado de toda la ruta. El MAEC pide a los españoles que abandonen el territorio, y el FCDO desaconseja todo viaje salvo a Bangui, donde solo admite el estrictamente esencial. Hay guerra civil desde 2013, grupos armados ocupando el norte y el sureste pese al acuerdo de paz de 2019, secuestro criminal habitual fuera de la capital, artefactos explosivos improvisados en el noroeste y fuerzas rusas desplegadas junto al ejército. El MAEC resume el problema en tres palabras: «inexistencia de fuerzas de seguridad». Para una expedición en vehículo propio no hay lectura matizada posible.",
    seguridad=[
        "MARCO OFICIAL: el MAEC (22-05-2024) pide a los españoles que abandonen el país; el FCDO (28-05-2026) desaconseja todo viaje salvo a Bangui, y allí solo el esencial; France Diplomatie (15-09-2026) pinta de ROJO todo el territorio fuera de Bangui y Bimbo. Grupos armados siguen ocupando el norte y el sureste pese al acuerdo de paz de 2019.",
        "France Diplomatie (act. 15-09-2026) clasifica TODO el territorio fuera de Bangui y Bimbo en ROJO (formalmente desaconsejado) y Bangui y Bimbo en NARANJA. El MAEC cita como alto riesgo los barrios PK3, PK5 y PK12 de Bangui y las ciudades de Bambari, Berbérati, Bossangoa, Ndélé, Sibut y Kabo, y advierte de que las áreas fronterizas son especialmente peligrosas.",
        "SECUESTRO: el FCDO documenta secuestro criminal frecuente fuera de Bangui. Grupos armados y bandidos usan controles de carretera ilegales y han atacado indiscriminadamente a viajeros en zonas remotas, con robo de vehículos, heridos y muertos.",
        "ARTEFACTOS EXPLOSIVOS IMPROVISADOS sin identificar en el noroeste del país (FCDO), precisamente la región por la que discurre el corredor de entrada desde Camerún.",
        "PRESENCIA MILITAR RUSA: Wagner desplegado junto a las FACA desde 2018, con unos 1.500-2.000 mercenarios que, según el COI Focus de la EUAA (21-01-2026), han infiltrado el conjunto de las estructuras de seguridad y ejercen mando de facto sobre unidades de las FACA en el interior. Desde 2025 Rusia presiona para sustituir Wagner por el Africa Corps estatal. La MINUSCA desplegaba 14.046 militares y 2.999 policías en octubre de 2025 y ya no considera Bangui zona prioritaria.",
        "Fotografía muy restringida: prohibido fotografiar emplazamientos militares, aeropuertos y puertos (MAEC), y a menudo hace falta permiso hasta en la vía pública, con riesgo de detención y confiscación del equipo (FCDO).",
        "Registros y detenciones arbitrarias por parte de policía y de grupos armados, que afectan a nacionales y extranjeros por igual (FCDO). No circular de noche y no circular solo (MAEC).",
        "El COI Focus de la EUAA sobre Bangui (21-01-2026) cifra en 47 los incidentes violentos registrados por ACLED en la capital entre principios de 2024 y finales de 2025, con 32 muertos, y describe una explosión de inseguridad criminal con robos a mano armada nocturnos en los que se sospecha participación de policías y militares.",
    ],
    agua=[
        "NO beber agua del grifo en ningún punto del país. TravelHealthPro exige higiene estricta con agua hervida o filtrada; el MAEC desaconseja el consumo de agua corriente.",
        "Para llenar depósitos de uso general (ducha y lavado), la única fuente razonablemente fiable serían los puntos de agua de hoteles internacionales y bases de organizaciones en Bangui. Fuera de la capital, asumir que no hay red tratada.",
        "El hub logístico de Garoua-Boulaï, ya en lado camerunés del corredor, dispone de pozo de agua y generador eléctrico (Business in Cameroon, 08-09-2025): es el último punto de servicio con infraestructura antes de la frontera.",
        "Riesgo de esquistosomiasis en aguas dulces (TravelHealthPro): no bañarse ni llenar depósitos en ríos y lagos, incluido el Ubangui.",
        "Cólera citado como riesgo por el MAEC. Con brotes de cólera, el agua de uso general deja de ser un problema menor: filtrar y clorar incluso el agua de ducha si hay heridas abiertas.",
        "POR CONFIRMAR: no se ha localizado ningún punto de agua potable documentado en iOverlander ni en bases de datos de viajeros para la República Centroafricana en esta sesión.",
    ],
    combustible=[
        "GASOLINA: 1.050 XAF por litro, equivalente a 1,603 € o 1,861 USD, dato de 9 de marzo de 2026 (GlobalPetrolPrices). Un 38 % por encima de la media mundial de ese periodo (759 XAF).",
        "DIÉSEL: 1.300 XAF por litro, equivalente a 1,98 € o 2,31 USD, dato de 8 de diciembre de 2025 (GlobalPetrolPrices). Casi el DOBLE de la media mundial de la fecha (701 XAF).",
        "Es uno de los combustibles más caros del mundo, en un país sin refinería y sin salida al mar: todo el carburante entra por carretera desde Duala, unos 1.500 km, a través del corredor de Garoua-Boulaï.",
        "Esa dependencia de un único corredor convierte cualquier bloqueo, huelga de transportistas o incidente de seguridad en desabastecimiento inmediato. El corredor ya sufrió una huelga de transportistas de tres semanas que cortó el tráfico, y en 2022 hubo una crisis de combustible con venta callejera en Bangui.",
        "Fuera de Bangui y de las capitales de prefectura, no contar con estaciones de servicio fiables. Autonomía y bidones son obligatorios: para un tramo Béloko–Bangui de unos 600 km habría que salir con depósito lleno desde Camerún.",
        "CALIDAD: no hay dato verificado sobre contenido de azufre ni sobre la idoneidad del gasóleo local para motores diésel modernos con filtro de partículas. POR CONFIRMAR antes de repostar con el Delica o el Grenadier.",
    ],
    experiencias_intro="No existen relatos recientes de overlanders españoles cruzando la República Centroafricana en vehículo propio: el conflicto ha vaciado el país de viajeros independientes desde 2013. Lo que sí hay es turismo organizado al suroeste, crónicas de viajeros de países y algún testimonio histórico anterior a la guerra.",
    experiencias=[
        "Dzanga-Sangha sigue recibiendo visitantes, y son unos 800 al año: Mongabay publicó en abril de 2026 que alrededor de 800 turistas visitaron Dzanga-Sangha durante 2025, procedentes de unas veinte nacionalidades —entre ellas España, Alemania, Rusia y Estados Unidos— y generando cerca de un millón de dólares. Es el dato que desmonta la idea de que el país entero está cerrado: el suroeste funciona, con un modelo de reparto de ingresos en el que el 30 % va a las comunidades locales y el 35 % al propio parque.",
        "El acceso a Bayanga es aéreo o fluvial, no por carretera desde Europa: la propia web de las Áreas Protegidas de Dzanga-Sangha (consultada en septiembre de 2026) detalla que el chárter desde Bangui tarda 50 minutos y aterriza en una pista de laterita de 1,4 km con Lapara Centrafrique o Via Air, por 3.000 a 4.125 € compartibles. Por carretera desde Bangui son unos 500 km y de 12 a 15 horas. También se llega en barco por el río Sangha desde Ouesso, en Congo, y desde Libongo, en Camerún.",
        "La logística del país cabe en una sola carretera: Business in Cameroon informó el 8 de septiembre de 2025 de la inauguración del hub logístico de Garoua-Boulaï, con aparcamiento para 200 camiones, alojamiento, restaurante, pozo y generador, construido expresamente para reducir el estacionamiento incontrolado y mitigar la inseguridad vial del corredor Duala–Bangui, por donde pasan unos 55.000 millones de XAF (89 millones de dólares) de mercancías al año.",
        "El corredor se corta con facilidad, y lleva haciéndolo una década: Ecofin Agency informó el 25 de agosto de 2015 de la reanudación del tráfico Duala–Bangui tras tres semanas de huelga de transportistas cameruneses en protesta por los ataques que sufrían en territorio centroafricano. Unos 400 camiones quedaron parados en Garoua-Boulaï. El artículo describe el tramo entre Baboua y Bouar como «el camino de la muerte» por las bandas armadas que asaltan y matan conductores, y detalla que los camiones circulaban escoltados por cascos azules de la ONU en convoyes automáticos de 60 vehículos.",
        "La escolta del corredor es para mercancías, no para viajeros: la Unión Africana documentó cómo la MISCA escoltó un convoy de 120 vehículos comerciales y humanitarios hasta Bangui, el Consejo Nacional de Cargadores de Camerún explica que los conductores van ahora escoltados por fuerzas de la MINUSCA frente a los rebeldes, y AllAfrica recogió en diciembre de 2024 que los camioneros cameruneses seguían pidiendo protección militar. Es logística profesional bajo protección de una misión de paz, no un servicio al que pueda acogerse un particular.",
        "Béloko es la llave aduanera del país: la ficha de Wikipedia sobre Béloko (5,9353 N / 14,6056 E, prefectura de Nana-Mambéré) recoge que por su aduana pasa el 80 % de las importaciones centroafricanas, y que el corredor Bangui–Garoua-Boulaï quedó bajo control de las FACA y sus aliados en febrero de 2021, tras haber sido disputado por los grupos CPC y 3R entre 2020 y 2023. La disputa por ese eje es la disputa por el país.",
        "Quien va hoy, va con operador y carta de invitación: la web de Central African Republic Tours explica que el «visa volant» a la llegada se tramita con una carta de invitación solicitada con un mínimo de dos semanas de antelación y que exige contratar al menos un tour, algo que presentan como requisito legal. Es el reverso exacto del viaje independiente: en la RCA de 2026 el viajero suelto no tiene vía administrativa propia.",
        "El recuerdo de cuando se podía cruzar: el blog Alison and Don publicó en junio de 2024 una crónica retrospectiva titulada «Mud Luscious And Puddle Wonderful» sobre su travesía de la República Centroafricana dentro de un África overland en 1980. Es un documento útil precisamente por contraste: describe un país que se atravesaba con barro y paciencia, no con escoltas, y que lleva más de una década sin ser esa ruta.",
        "Los corredores siguen perdiendo carga en 2026: AllAfrica publicó el 18 de septiembre de 2026 que los transportistas del eje Duala-Bangui son asaltados por individuos armados en áreas de descanso, que los precintos de carga aparecen rotos y la mercancía desaparece, y que hay conductores que han dejado de rodar después del anochecer por miedo. Añade que el 30 % de las empresas logísticas camerunesas sufrió pérdidas por actos criminales y que en el corredor hermano Duala-Yamena hay 64 paradas impuestas en 1.392 km, una cada 21,75 km.",
        "Bangui no es el resto del país, pero tampoco es segura: el COI Focus de la EUAA de 21 de enero de 2026 registra, con datos de ACLED, 47 incidentes violentos en Bangui entre principios de 2024 y finales de 2025, con 32 muertos, y describe una explosión de inseguridad criminal con robos a mano armada nocturnos en los que se sospecha participación de policías y militares. Las FACA aparecen como actor de 22 incidentes y Wagner de 16.",
    ],
    pendientes=[
        ("Exigencia real de CPD en frontera", "Confirmación escrita de la Direction Générale des Douanes centroafricana o del RACE sobre si el carnet de passages es exigido o si basta el laissez-passer de admisión temporal."),
        ("Estado y titular del control de los pasos de Sido, Bambouti y Bangassou–Ndu", "Fuente fechada de 2025-2026 (MINUSCA, ACLED, OCHA o FCDO) que confirme si están abiertos a extranjeros y qué fuerza los controla."),
        ("Acceso de un particular a los convoyes escoltados del corredor", "Confirmado que NO hay escolta obligatoria para particulares (France Diplomatie, 15-09-2026). Queda por saber si la MINUSCA o los cargadores admitirían a un vehículo particular en un convoy comercial escoltado: preguntar a la MINUSCA y al Consejo Nacional de Cargadores de Camerún."),
        ("Normativa nacional de drones", "Texto publicado por la autoridad de aviación civil de la RCA (ANAC) o confirmación por escrito de la Embajada de España en Yaundé de que no existe o de que la prohibición es total."),
        ("Página oficial del servicio veterinario nacional", "Localizar el portal del Ministerio de Agricultura o de los servicios veterinarios de la RCA con los requisitos de importación de animales de compañía, y sustituir la fuente secundaria actual."),
        ("Permiso previo y razas prohibidas para el perro", "Respuesta del servicio veterinario oficial, vía consulado honorario en Bangui, sobre si se exige permiso previo de importación y si existe lista de razas prohibidas."),
        ("Cobertura de Starlink Roaming con terminal europeo", "Comprobación en el mapa de disponibilidad de starlink.com de si el país admite el plan Roaming y si un kit comprado en España funciona allí."),
        ("Operadores móviles y SIM turística", "Fuente de 2025-2026 (regulador ARCEP centroafricano u operador) con la lista de operadores, cobertura y requisitos de registro de SIM para extranjeros."),
        ("Validez del visado de París en frontera terrestre", "Confirmación de la Embajada de la RCA en París de que un visado emitido allí se admite en entrada terrestre por Béloko, y si se exige ordre de mission para circular por el interior."),
        ("Calidad del gasóleo", "Especificación de azufre del gasóleo comercializado en la RCA, para valorar si es compatible con los motores del Grenadier y el Delica."),
        ("Puntos de agua y combustible verificados", "Entradas de iOverlander o Tracks4Africa de 2024-2026 con coordenadas de estaciones de servicio y puntos de agua operativos en el eje Béloko–Bangui."),
        ("Cobertura aseguradora", "Confirmación por escrito de la aseguradora de la expedición de si existe alguna póliza que cubra evacuación médica en un país con desaconsejo total del MAEC, y a qué precio."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las fuentes listadas, todas abiertas en esa fecha. Los datos de seguridad, fronteras y precios de un país en conflicto caducan deprisa: comprobar de nuevo el MAEC y el FCDO antes de cualquier decisión. Esta ficha es una herramienta de planificación e información, no una autorización de viaje ni una recomendación de visitar el país.",
    emergency="EMERGENCIA CONSULAR ESPAÑOLA: +237 698 44 79 00 (Embajada de España en Yaundé, competente para la RCA). Centralita: +237 222 20 35 43 y +237 222 20 41 89. Consulado honorario en Bangui: +236 70 93 25 50 y +236 75 82 16 16. Los números nacionales de policía, ambulancia y bomberos NO figuran en la ficha del MAEC ni del FCDO y quedan POR CONFIRMAR. Con «inexistencia de fuerzas de seguridad» (MAEC), el recurso real es el consulado.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

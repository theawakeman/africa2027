# -*- coding: utf-8 -*-
"""Burundi — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Burundi está FUERA DE LA RUTA PREVISTA aunque es continental y limita con países del corredor (Tanzania, Ruanda y RD Congo). La app solo tiene un stub: créala entera con el formato del piloto de Túnez. Claves que DECIDEN la ficha y hay que documentar con fuente fechada: la crisis del tercer mandato de Nkurunziza en 2015 dejó cientos de muertos y cientos de miles de refugiados, y aunque Évariste Ndayishimiye gobierna desde 2020 con cierta normalización diplomática, Freedom House sigue clasificando al país entre los no libres; la frontera con Ruanda se cerró en enero de 2024 por la acusación burundesa de apoyo al grupo armado RED-Tabara y hay que verificar su estado actual; y el este del país sufre las réplicas del conflicto del Kivu. Para el viajero: el visado se tramita en línea o a la llegada — verifícalo —, hay toque de queda y controles frecuentes, está prohibido fotografiar instalaciones oficiales, y Gitega es la capital política desde 2019 aunque Buyumbura sigue siendo la económica. El país NO tiene ningún bien inscrito en la Lista del Patrimonio Mundial: compruébalo antes de etiquetar ningún PDI.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/burundi.json y audit/pdi/burundi.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Buyumbura · centro, mercado y paseo del lago", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=-3.36278, lon=29.36556,  # Google Maps: Buyumbura (sin objeto en Google Maps; coordenada de la fuente)
        desc="Capital económica y antiguo centro político de Burundi, a orillas del Tanganica y con 1,1 millones de habitantes en su área urbana. Es la única base logística seria del país: bancos, talleres, combustible, embajadas y hospital de referencia. El mercado central ardió por completo el 27 de enero de 2013 y la actividad se repartió por los mercados de barrio. ADVERTENCIA: está PROHIBIDO fotografiar instalaciones oficiales, y el MAEC desaconseja circular a pie por la ciudad entre las 18:00 y las 06:00.",
        dog_note="Calle y hoteles con jardín sí; mercados y edificios oficiales, no. Nunca dejarlo en el coche por el calor.",
        visit={
            "why": "Es el punto de reabastecimiento obligado: gasolina, cambio, repuestos y gestiones antes de salir al interior. También concentra el poco tejido de restaurantes y alojamiento con aparcamiento cerrado del país.",
            "see": "La avenida Rwagasore y el mercado, la catedral Regina Mundi, el Monumento a los Héroes de la Independencia y el paseo del lago hacia el sur. El Musée Vivant reúne fauna y una reconstrucción de poblado tradicional.",
            "access": "Asfalto en el centro, con baches; RN1 hacia Gitega y RN3 hacia el sur salen de la ciudad. Aparcamiento para dos 4x4 solo en hoteles con recinto vallado: no dejar los coches en la calle de noche. El pin marca la plaza de la Independencia, en pleno centro, como punto de referencia para navegar.",
            "when": "Mañana temprano para trámites; la estación seca (junio–septiembre) evita el barro en los accesos.",
            "skip": "Descártala si el viaje entra y sale por tierra en el mismo día o si hay disturbios: el FCDO y el MAEC advierten de inseguridad urbana y de un ataque con granada en la capital en 2024.",
        },
        links=[
            {"label": "Buyumbura (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bujumbura"},
            {"label": "Recomendaciones de viaje MAEC · Burundi", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burundi"},
            {"label": "FCDO travel advice · Burundi", "url": "https://www.gov.uk/foreign-travel-advice/burundi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/BUJUMBURA-BURUNDI_BINDOVILLE_03.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:BUJUMBURA-BURUNDI_BINDOVILLE_03.jpg",
                "credit": "Edouard mhg · CC0",
                "caption": "Buyumbura, junto al Tanganica.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/BUJUMBURA-BURUNDI_BINDOVILLE_05.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:BUJUMBURA-BURUNDI_BINDOVILLE_05.jpg",
                "credit": "Edouard mhg · CC0",
                "caption": "Una calle de Buyumbura.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bujumbura_%26_Lake_Tanganyika.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bujumbura_%26_Lake_Tanganyika.JPG",
                "credit": "Andreas31 · CC BY-SA 3.0",
                "caption": "Buyumbura y el lago Tanganica.",
            },
        ],
    ),
    dict(
        n=2, name="Lago Tanganica y playa de Saga · la costa de Buyumbura", cat="Costa", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=-3.3541236, lon=29.3230382,  # Google Maps: Saga plage
        desc="La franja de arena al sur de Buyumbura es la «costa» de Burundi: agua dulce transparente, palmeras y chiringuitos que se llenan los domingos. El Tanganica es el lago de agua dulce MÁS LARGO DEL MUNDO —673 km— y el segundo más profundo del planeta, con 1.470 m, solo por detrás del Baikal. Merece la parada por el contraste entre playa tropical y altiplano. ADVERTENCIA: hay hipopótamos y cocodrilos; báñate solo donde lo hagan los locales y nunca al amanecer o al atardecer.",
        dog_note="Playas privadas suelen admitirlo atado; prohibido meterlo en el agua por hipopótamos y cocodrilos.",
        visit={
            "why": "Es la parada de descanso natural antes o después de cruzar el país, y el mejor sitio para ver el lago desde la orilla burundesa.",
            "see": "Playas de arena clara sobre la Chaussée d'Uvira, pescadores con piraguas, montañas de RD Congo enfrente y atardeceres sobre el agua.",
            "access": "Asfalto en mal estado desde el centro por la Chaussée d'Uvira, unos 5–7 km al sur. Los recintos de playa privados cobran una entrada simbólica y tienen aparcamiento vallado donde caben dos 4x4. El pin marca el acceso a Saga Plage, no la línea de costa. Evita la zona AL OESTE del río Rusizi: el FCDO desaconseja todo viaje allí.",
            "when": "Laborables por la mañana; fines de semana está muy concurrida. Estación seca para el agua más clara.",
            "skip": "Sáltala si vas justo de días o si hay aviso de seguridad en la carretera de Uvira: es ocio, no patrimonio.",
        },
        links=[
            {"label": "Lago Tanganica (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Lake_Tanganyika"},
            {"label": "Saga Beach · Lonely Planet", "url": "https://www.lonelyplanet.com/points-of-interest/saga-beach/1013772"},
            {"label": "El lago Tanganica en la Lista Indicativa de la UNESCO", "url": "https://whc.unesco.org/en/statesparties/bi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Beach_in_Bujumbura.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Beach_in_Bujumbura.jpg",
                "credit": "Macabe5387 · CC BY-SA 4.0",
                "caption": "Playa del Tanganica en Buyumbura.",
            },
        ],
    ),
    dict(
        n=3, name="Monumento Livingstone-Stanley de Mugere", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=-3.4819725, lon=29.3525834,  # Google Maps: Piedra de Livingstone y Stanley
        desc="Dos piedras con una placa, 12 km al sur de Buyumbura, marcan donde David Livingstone y Henry Morton Stanley acamparon del 25 al 27 de noviembre de 1871 mientras exploraban el norte del Tanganica. Sobre la roca todavía se lee la fecha 25 DE NOVIEMBRE DE 1871 grabada. Aviso importante: aquí NO se produjo el famoso encuentro «Doctor Livingstone, supongo», que tuvo lugar en Ujiji (Tanzania) el 10 de noviembre de 1871, pese a lo que diga el guía.",
        dog_note="Recinto al aire libre sin fauna peligrosa; atado por los niños y los vendedores del aparcamiento.",
        visit={
            "why": "Es el hito histórico más conocido de Burundi y una parada corta y barata a la salida sur de la capital, con vistas al lago.",
            "see": "Las dos rocas con las iniciales y la fecha, la placa conmemorativa y un mirador sobre el Tanganica y el delta del Mugere.",
            "access": "Asfalto por la Chaussée d'Uvira (RN3 sur) hasta un desvío señalizado; explanada de tierra con sitio de sobra para dos 4x4. Suele haber un guardés que cobra una entrada simbólica y espera propina; no hay horario fijo publicado. El pin marca la desembocadura del Mugere, junto a la que está el monumento.",
            "when": "Primera hora de la mañana, con luz lateral sobre el lago y menos calor.",
            "skip": "Sáltalo si esperas un museo: son dos piedras y una placa, y la visita completa no llega a veinte minutos.",
        },
        links=[
            {"label": "Livingstone–Stanley Monument (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Livingstone%E2%80%93Stanley_Monument"},
            {"label": "Río Mugere (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Mugere_River"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/La_Pierre_de_Livingstone_et_Stanley_01_(15924542368).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:La_Pierre_de_Livingstone_et_Stanley_01_(15924542368).jpg",
                "credit": "Stefan Krasowski · CC BY 2.0",
                "caption": "La piedra de Livingstone y Stanley, en Mugere.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/La_Pierre_de_Livingstone_et_Stanley_2_(15489648584).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:La_Pierre_de_Livingstone_et_Stanley_2_(15489648584).jpg",
                "credit": "Stefan Krasowski · CC BY 2.0",
                "caption": "El monumento sobre el lago.",
            },
        ],
    ),
    dict(
        n=4, name="Parque nacional de la Rusizi · el delta y sus hipopótamos", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="medio día",
        lat=-3.3512672, lon=29.2638805,  # Google Maps: Parque nacional de Rusizi
        desc="El parque del delta del Rusizi, 15 km al norte de Buyumbura, protege 10.673 hectáreas en dos sectores: el Delta (1.363 ha) donde el río entra en el Tanganica y la Palmeraie (8.867 ha), con el palmeral endémico de Hyphaene. Hay 19 especies de mamíferos —hipopótamo incluido— y 350 DE AVES, con hasta 6.000 dendrocignas en el río en plena migración. Aquí vivía GUSTAVE, el cocodrilo del Nilo al que se atribuyen 300 muertes. ADVERTENCIA SERIA: el FCDO desaconseja TODO viaje al parque.",
        dog_note="Parque nacional con hipopótamos y cocodrilos del Nilo: el perro se queda en Buyumbura.",
        visit={
            "why": "Es el único safari acuático accesible del país y la mejor foto de hipopótamos de Burundi, a media hora de la capital.",
            "see": "Manadas de hipopótamos en el delta, antílopes sitatunga entre el papiro, aves acuáticas y el palmeral endémico de Hyphaene del sector Palmeraie.",
            "access": "Asfalto por la RN5 hacia Gatumba y pista de tierra hasta la entrada; con lluvia el último tramo se embarra. Gestiona el OBPE (Office Burundais pour la Protection de l'Environnement): guía obligatorio y entrada de pago, tarifas no publicadas en fuente verificable. El pin marca la zona del parque, NO la puerta: confírmala con el OBPE. Zona desaconsejada por FCDO y MAEC.",
            "when": "Estación seca (junio–septiembre), a primera hora de la mañana, cuando los hipopótamos siguen en el agua.",
            "skip": "Descártalo mientras siga vigente el aviso de «no viajar» del FCDO para el oeste del Rusizi, o si viajas con el perro y no tienes dónde dejarlo.",
        },
        links=[
            {"label": "Parc National de la Rusizi · CHM Biodiversité du Burundi (oficial)", "url": "https://bi.chm-cbd.net/fr/protected-areas/parc-nati-rusizi"},
            {"label": "Parque nacional de la Rusizi (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Rusizi_National_Park"},
            {"label": "FCDO travel advice · Burundi", "url": "https://www.gov.uk/foreign-travel-advice/burundi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Rusizi_NP_hippopotamus.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Rusizi_NP_hippopotamus.jpg",
                "credit": "Dave Proffer · CC BY 2.0",
                "caption": "Hipopótamos en el parque de la Rusizi.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Rusizi_National_Park_-_Flickr_-_Dave_Proffer.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Rusizi_National_Park_-_Flickr_-_Dave_Proffer.jpg",
                "credit": "Dave Proffer · CC BY 2.0",
                "caption": "El delta de la Rusizi.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Rusizi_National_Park_-_Flickr_-_Dave_Proffer_(2).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Rusizi_National_Park_-_Flickr_-_Dave_Proffer_(2).jpg",
                "credit": "Dave Proffer · CC BY 2.0",
                "caption": "La llanura del parque.",
            },
        ],
    ),
    dict(
        n=5, name="Gitega · capital política y Museo Nacional", cat="Cultura", prio="Alta",
        dog="no recomendado", time="1 noche",
        lat=-3.4182177, lon=29.9086115,  # Google Maps: Museo Nacional de Burundi (Gitega)
        desc="Gitega es CAPITAL POLÍTICA DE BURUNDI DESDE EL 16 DE ENERO DE 2019, cuando el Parlamento aprobó el traslado desde Buyumbura, aunque sigue siendo una ciudad de plateau de apenas 135.000 habitantes. Su Museo Nacional, fundado en 1955 en época belga, guarda objetos de la corte de los mwami y es el mayor museo público del país, pese a exponerlo todo en una sola sala. Merece la parada por el contexto monárquico que explica Gishora. Está a 62 km al este de Buyumbura.",
        dog_note="El museo no admite animales y la ciudad tiene muchos edificios oficiales donde no conviene pasear con perro.",
        visit={
            "why": "Da la clave histórica del país —la monarquía y el tambor real— en una hora, y es la base natural para dormir antes de Gishora.",
            "see": "La colección etnográfica de la corte real, los santuarios de tambores karyenda, el barrio colonial y el mercado de la ciudad alta.",
            "access": "RN1 asfaltada desde Buyumbura, 62 km de curvas de montaña; aparcamiento junto al museo con sitio para dos 4x4. Horarios y precio no publicados en fuente verificable: POR CONFIRMAR in situ. El pin marca el museo, no el centro administrativo. Prohibido fotografiar edificios oficiales, muy numerosos desde el traslado de la capital.",
            "when": "Cualquier mañana entre semana; el museo recibía apenas 20–50 visitantes por semana, así que nunca hay cola.",
            "skip": "Sáltalo si vienes de museos etnográficos africanos mejores: la colección es valiosa pero está mal expuesta.",
        },
        links=[
            {"label": "Gitega (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Gitega"},
            {"label": "Museo Nacional de Gitega (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/National_Museum_of_Gitega"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Burundi_National_Museum_at_Gitega_-_Flickr_-_Dave_Proffer.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Burundi_National_Museum_at_Gitega_-_Flickr_-_Dave_Proffer.jpg",
                "credit": "Dave Proffer · CC BY 2.0",
                "caption": "El Museo Nacional de Gitega.",
            },
        ],
    ),
    dict(
        n=6, name="Tambores sagrados de Gishora · residencia real (Patrimonio Inmaterial UNESCO)", cat="Cultura", prio="Alta",
        dog="prohibido", time="medio día",
        lat=-3.3628585, lon=29.9219594,  # Google Maps: Gishora Drum Sanctuary
        desc="Colina real fundada por el mwami Ntare Rugamba en la primera mitad del siglo XIX tras vencer al jefe rebelde Ntibirangwa, 7 km al norte de Gitega. En el primer patio, el Intangaro, se guardan los tambores sagrados Ruciteme y Murimirwa, custodiados por los batimbo. OJO CON LA ETIQUETA: la danza ritual del tambor real es Patrimonio Cultural INMATERIAL de la Humanidad desde 2014, pero Burundi NO tiene ningún bien en la Lista del Patrimonio Mundial; Gishora solo está en Lista Indicativa desde 2007.",
        dog_note="Recinto ritual con santuario de tambores: no se entra con animales.",
        visit={
            "why": "Es la única experiencia cultural de primer nivel del país: los abatimbo tocan y bailan con los tambores sobre la cabeza en el recinto original.",
            "see": "Las tres cortes del recinto, las chozas de materiales vegetales, el santuario de tambores y la actuación de los tamborileros, que se contrata en el sitio.",
            "access": "Pista de tierra corta desde la RN2 al norte de Gitega, transitable con cualquier 4x4; explanada con sitio de sobra para dos coches. La actuación se paga aparte y conviene avisar con antelación; tarifa no publicada en fuente verificable. El pin marca la colina del recinto, que está señalizada desde la carretera.",
            "when": "Media mañana, para que dé tiempo a reunir al grupo de tamborileros; evita los días de lluvia fuerte, el patio es de tierra.",
            "skip": "Sáltalo solo si no puedes pagar la actuación: el recinto vacío pierde casi todo su interés.",
        },
        links=[
            {"label": "Gishora (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Gishora"},
            {"label": "Danza ritual del tambor real · UNESCO Patrimonio Inmaterial (2014)", "url": "https://ich.unesco.org/en/RL/ritual-dance-of-the-royal-drum-00989"},
            {"label": "Résidence Royale de Gishora · Lista Indicativa UNESCO", "url": "https://whc.unesco.org/en/tentativelists/6927"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Les_tambourinaires_de_Gitega.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Les_tambourinaires_de_Gitega.jpg",
                "credit": "NSENGIYUMVA Joseph · CC BY-SA 4.0",
                "caption": "Los tamborileros de Gitega.",
            },
        ],
    ),
    dict(
        n=7, name="Parque nacional de la Kibira · la selva de montaña del noroeste", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=-2.91466, lon=29.43361,  # Google Maps: Parque nacional de la Kibira (coordenada de la fuente; Google solo da un centroide redondeado)
        desc="Cuatrocientos kilómetros cuadrados de selva de montaña sobre la cresta Congo-Nilo, por encima de los 1.100 m, que continúan sin solución de continuidad en el parque ruandés de Nyungwe. Fue coto de caza real hasta 1933 y reserva forestal hasta 1980. Alberga 98 especies de mamíferos —chimpancés y colobos incluidos— y 200 de aves, y sus cuencas dan MÁS DE TRES CUARTAS PARTES del agua de la principal presa hidroeléctrica del país. ADVERTENCIA: MAEC y FCDO desaconsejan viajar a la Kibira por presencia de grupos armados.",
        dog_note="Parque nacional con chimpancés y primates: los perros transmiten enfermedades y están vetados.",
        visit={
            "why": "Es la única selva de montaña de Burundi y el mejor lugar del país para ver primates y aves de altura, con las plantaciones de té de Teza al borde.",
            "see": "Dosel de bosque nuboso, chimpancés y colobos blanquinegros, aves endémicas del arco Albertino, las cuevas de Inangurire junto al monte Teza, las fuentes termales de Ku Mahoro, el embalse de Rwegura y los campos de té de Teza.",
            "access": "Cuatro sectores: Teza, Rwegura, Mabayi y Musigati. La guía oficial da RN1 desde Buyumbura hasta Bugarama (una hora) y luego Kayanza; desde Kayanza, 122 km por la RN10 hacia Rugombo; desde Ngozi, 35 km por Kayanza. Hay que registrarse en la oficina del parque y está PROHIBIDO entrar sin guía autorizado. Alojamiento en el Kibira Park Lodge de Bugarama (28 habitaciones, hasta 40.000 francos burundeses) y casas del parque en Teza. El pin marca el interior del parque, no una puerta. FCDO y MAEC desaconsejan viajar aquí.",
            "when": "Estación seca (junio–septiembre); las pistas del parque son intransitables con lluvia fuerte.",
            "skip": "Descártalo mientras sigan los avisos de «no viajar» de FCDO y MAEC: no compensa el riesgo.",
        },
        links=[
            {"label": "Guide touristique · Destination Parc National de la Kibira (PDF oficial, OBPE/CHM)", "url": "https://bi.chm-cbd.net/sites/bi/files/2020-04/guide-tourist-pnk.pdf"},
            {"label": "Parque nacional de la Kibira (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Kibira_National_Park"},
            {"label": "FCDO travel advice · Burundi", "url": "https://www.gov.uk/foreign-travel-advice/burundi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Parc_National_de_la_kibira.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Parc_National_de_la_kibira.jpg",
                "credit": "NZISABIRA Léopold · CC BY-SA 4.0",
                "caption": "La selva de montaña de la Kibira.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/L'entr%C3%A9e_du_Parc_National_de_la_kibira.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:L'entr%C3%A9e_du_Parc_National_de_la_kibira.jpg",
                "credit": "NZISABIRA Léopold · CC BY-SA 4.0",
                "caption": "La entrada del parque de la Kibira.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Kibira_national_park.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Kibira_national_park.jpg",
                "credit": "KUBWIMANA Bienvenu · CC BY-SA 4.0",
                "caption": "El dosel de la Kibira.",
            },
        ],
    ),
    dict(
        n=8, name="Reserva natural de Bururi · el bosque del sur", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="medio día",
        lat=-3.9378168, lon=29.5976979,  # Google Maps: Reserva natural de Bururi
        desc="Treinta y tres kilómetros cuadrados de bosque de altura junto a la ciudad de Bururi, protegidos desde 1951 y clasificados como área silvestre de categoría UICN Ib. Se han censado 93 especies de árboles y 87 de aves, entre ellas la apalis plateada (Apalis argentea), amenazada. El río Siguvyaye lo atraviesa por el sur con saltos de agua y miradores. Es la alternativa razonable a la Kibira porque queda FUERA de las zonas desaconsejadas por MAEC y FCDO.",
        dog_note="Reserva de categoría UICN Ib con primates; aunque no hay grandes depredadores, la gestión no contempla animales domésticos.",
        visit={
            "why": "Da bosque de montaña y aves del arco Albertino sin entrar en las provincias vetadas del noroeste, y está a un paso de la carretera del sur.",
            "see": "Bosque denso de Strombosia y Myrianthus, monos, aves de altura y las cascadas del Siguvyaye en el sector sur.",
            "access": "Asfalto desde Rumonge o Matana hasta Bururi y pista corta hasta la reserva; hay explanada para aparcar dos 4x4 junto a la casa forestal. Gestionada por el INECN/OBPE; guía local recomendable y tarifas no publicadas en fuente verificable. El pin marca el interior de la reserva: la entrada está en el borde norte, junto a la ciudad de Bururi.",
            "when": "Estación seca; sale a 1.800–2.000 m, así que amanece fresco y con niebla, y a media mañana ya se ve el bosque.",
            "skip": "Sáltala si vienes de Nyungwe o de la Kibira: es el mismo tipo de bosque a menor escala.",
        },
        links=[
            {"label": "Reserva natural forestal de Bururi (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bururi_Forest_Nature_Reserve"},
            {"label": "Bururi (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Bururi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Foret_de_Bururi.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Foret_de_Bururi.jpg",
                "credit": "Ferdinand IF99 · CC BY-SA 4.0",
                "caption": "El bosque de Bururi.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Vue_de_face_de_la_r%C3%A9serve_naturelle_for%C3%A9stiere_de_bururi.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Vue_de_face_de_la_r%C3%A9serve_naturelle_for%C3%A9stiere_de_bururi.jpg",
                "credit": "Ferdinand IF99 · CC BY-SA 4.0",
                "caption": "La reserva natural de Bururi.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/PancarteLa_r%C3%A9serve_naturelle_de_la_for%C3%AAt_de_Bururi.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:PancarteLa_r%C3%A9serve_naturelle_de_la_for%C3%AAt_de_Bururi.jpg",
                "credit": "Ferdinand IF99 · CC BY-SA 4.0",
                "caption": "Señalización de la reserva.",
            },
        ],
    ),
    dict(
        n=9, name="Fuente meridional del Nilo en Rutovu · la pirámide de Kasumo", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=-3.9151459, lon=29.8378669,  # Google Maps: Source du Nil (Rutovu)
        desc="En la ladera norte del monte Kikizi (2.145 m), un hilo de agua marcado por una pequeña pirámide de piedra es la FUENTE MÁS MERIDIONAL DEL NILO, identificada por el explorador alemán Burkhart Waldecker en 1934. De aquí sale el Ruvyironza, que por el Gasenyi, el Kigira y el Kagera llega al lago Victoria y, 6.000 km después, al Mediterráneo. La UNESCO lo tiene en Lista Indicativa desde 2007. ADVERTENCIA: la pirámide es modesta; lo que se visita es la idea, no el monumento.",
        dog_note="Monumento al aire libre sin vallar ni fauna peligrosa; llévalo atado por el ganado de las colinas.",
        visit={
            "why": "Pocas paradas del continente cuentan tanto con tan poco: es el punto de partida geográfico del río más famoso del mundo.",
            "see": "La pirámide conmemorativa, el manantial entre eucaliptos, los cobertizos para visitantes y las colinas de Bururi a 2.000 m de altura.",
            "access": "Carretera asfaltada en buen estado desde Buyumbura, unos 132 km según la ficha UNESCO, y pista final corta; explanada de tierra con espacio para dos 4x4. Sin horario ni taquilla: hay un guardés que pide propina. El pin marca la cima del Kikizi, según Wikipedia; la fuente y la pirámide están en su ladera norte, POR CONFIRMAR sobre el terreno.",
            "when": "Mañana despejada de estación seca: desde la loma se ven las crestas del sur del país.",
            "skip": "Sáltalo si buscas espectáculo visual: la recompensa es simbólica, no paisajística.",
        },
        links=[
            {"label": "Monte Kikizi (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Mount_Kikizi"},
            {"label": "Rutovu (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Rutovu"},
            {"label": "Gasumo, la source la plus méridionale du Nil · Lista Indicativa UNESCO", "url": "https://whc.unesco.org/en/tentativelists/5144/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_source_of_the_Nile,_or_so_the_locals_say_-_Flickr_-_Dave_Proffer.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_source_of_the_Nile,_or_so_the_locals_say_-_Flickr_-_Dave_Proffer.jpg",
                "credit": "Dave Proffer · CC BY 2.0",
                "caption": "La fuente meridional del Nilo, en Rutovu.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_source_of_the_Nile,_or_so_the_locals_say,_nice_PVC_pipe..._-_Flickr_-_Dave_Proffer.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_source_of_the_Nile,_or_so_the_locals_say,_nice_PVC_pipe..._-_Flickr_-_Dave_Proffer.jpg",
                "credit": "Dave Proffer · CC BY 2.0",
                "caption": "El manantial de Kasumo.",
            },
        ],
    ),
    dict(
        n=10, name="Chutes de la Karera · las cascadas del este", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=-3.8301948, lon=30.0793956,  # Google Maps: Chutes de la Karera
        desc="Al sur de Rutana, el río se despeña en seis brazos repartidos en tres rellanos dentro de un recinto protegido de 142 hectáreas. El salto principal ronda los 80 METROS y a poniente hay otro de unos 50. Es la cascada más fotogénica de Burundi y la parada obligada del este, con una cueva considerada sagrada junto al agua. ADVERTENCIA: las rocas del sendero son muy resbaladizas y no hay barandillas; en estación de lluvias el caudal se dispara.",
        dog_note="Sendero abierto sin fauna peligrosa; atado por el barro y los escalones junto al agua.",
        visit={
            "why": "Es el paisaje natural más espectacular y accesible del país, y encaja perfectamente con la falla de Nyakazu en la misma jornada.",
            "see": "Los tres rellanos de saltos, la selva galería de Newtonia buchananii, la gruta sagrada a la que acude gente de todo el país y los senderos señalizados Gisuma, Bunya, Mihama y el de la galería.",
            "access": "Comunas de Mpinga-Kayove y Musongati, provincia de Rutana. Desde Buyumbura, RN7 por Ijenda y Matana hasta Gitaba, 129 km, y luego la carretera Rutana-Gitega; desde Gitega, 66 km por la RN8. La OFICINA DEL OBPE EN EL CENTRO DE SHANGA facilita los guías, y el sitio tiene pasarelas y barandillas de seguridad. Hoteles en Matana, Bukirasazi y Rutana; bancos en Rutana. El pin marca el conjunto de saltos. Zona no incluida en los avisos de «no viajar» de FCDO ni MAEC.",
            "when": "Final de la estación de lluvias o principio de la seca (abril–junio): mucho caudal y pistas ya transitables.",
            "skip": "Sáltalas en plena estación seca avanzada, cuando el caudal baja mucho, o si la pista está embarrada.",
        },
        links=[
            {"label": "Atouts touristiques et monuments naturels de l'Est du Burundi (PDF oficial, Ministerio de Medio Ambiente/CHM)", "url": "https://bi.chm-cbd.net/sites/bi/files/2022-03/attout-tourist-monum-natur-est-bi.pdf"},
            {"label": "Chutes de la Karera (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Karera_waterfalls"},
            {"label": "Les Chutes de Karera · Lista Indicativa UNESCO", "url": "https://whc.unesco.org/en/tentativelists/6932/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Indication_des_chutes_de_karera_%C3%A0_rutana.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Indication_des_chutes_de_karera_%C3%A0_rutana.jpg",
                "credit": "Zamennest · CC BY-SA 4.0",
                "caption": "Indicación de las cascadas de la Karera.",
            },
        ],
    ),
    dict(
        n=11, name="Falla de Nyakazu · la Brecha de los Alemanes", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=-3.89528, lon=30.12694,  # Google Maps: Falla de Nyakazu (sin objeto en Google Maps; coordenada de la fuente)
        desc="Una fractura tectónica reciente del Rift de África Oriental abre acantilados de HASTA 300 METROS y una cascada estacional de más de 100 m sobre bosque galería, en unas 600 hectáreas y a 23 km de la Karera. El documento oficial burundés explica el nombre: por estas grietas se retiraron las tropas alemanas cuando atacaron los belgas, y en la colina de Nyakazu queda la base de un antiguo puesto militar alemán, hoy mirador y zona de acampada. Está sin vallar y sin barandillas: no te asomes al borde.",
        dog_note="Mirador abierto sin cierre ni fauna peligrosa; atado, porque el borde del acantilado cae 300 m.",
        visit={
            "why": "Es el mejor mirador geológico del país, explica de un vistazo por qué el Rift partió África en dos y se encadena con la Karera en la misma jornada.",
            "see": "Los tres rellanos sucesivos de paredes verticales con fracturas ortogonales, el precipicio sobre el valle de Kumoso, la cascada estacional, los cimientos del puesto alemán y, en las galerías profundas, Entandrophragma excelsum, cercopitecos y pitones de buen tamaño.",
            "access": "A 23 km de las chutes de la Karera, con la que comparte la oficina del OBPE en el centro de Shanga; asfalto hasta Rutana o Musongati y pista de tierra hasta el borde, dura en lluvias. Hay explanada para dos 4x4 y el documento oficial menciona acampada panorámica sobre los cimientos del puesto alemán. El pin usa la coordenada de la ficha UNESCO (colina Burunga, comuna de Musongati): verifícalo antes de conducir.",
            "when": "Estación de lluvias o justo después para ver la cascada estacional; a mediodía, con el sol alto, se ve mejor el fondo del corte.",
            "skip": "Sáltala si vas justo de tiempo y ya has hecho la Karera, o si no puedes confirmar el punto de acceso.",
        },
        links=[
            {"label": "Atouts touristiques et monuments naturels de l'Est du Burundi (PDF oficial, Ministerio de Medio Ambiente/CHM)", "url": "https://bi.chm-cbd.net/sites/bi/files/2022-03/attout-tourist-monum-natur-est-bi.pdf"},
            {"label": "La faille de Nyakazu · Lista Indicativa UNESCO (2026)", "url": "https://whc.unesco.org/en/tentativelists/6930/"},
            {"label": "Provincia de Rutana (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Rutana_Province"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Le_Faille_de_Nyakazu_(des_Allemands).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Le_Faille_de_Nyakazu_(des_Allemands).jpg",
                "credit": "John Busokoza · CC BY-SA 4.0",
                "caption": "La falla de Nyakazu, la Brecha de los Alemanes.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Une_chute_d'eau_au_Faille_des_Allemands_(Nyakazu).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Une_chute_d'eau_au_Faille_des_Allemands_(Nyakazu).jpg",
                "credit": "John Busokoza · CC BY-SA 4.0",
                "caption": "Cascada en la falla de Nyakazu.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Failles_de_Nyakazu_3.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Failles_de_Nyakazu_3.jpg",
                "credit": "Grâce Aurore · CC BY-SA 4.0",
                "caption": "El escarpe de Nyakazu.",
            },
        ],
    ),
    dict(
        n=12, name="Lago Rwihinda · el lago de las aves de Kirundo", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="medio día",
        lat=-2.548984, lon=30.0809664,  # Google Maps: Lake Rwihinda
        desc="Llamado «el lago de los pájaros», este humedal de 425 hectáreas a 1.420 m de altitud es Reserva Natural Ordenada dentro del Paisaje Acuático Protegido del Norte, figura creada en 2005. Más de 60 ESPECIES DE AVES lo visitan estacionalmente —pelícanos blancos, cormoranes africanos, garcetas comunes— y la isla de Akagwa conserva palmeras Phoenix y papiro. Recibe solo 200–300 observadores al año. ADVERTENCIA: los proyectos de desecación de las marismas amenazan el nivel del agua.",
        dog_note="Reserva natural ordenada dedicada a aves acuáticas: un perro suelto espanta la colonia.",
        visit={
            "why": "Es la mejor parada ornitológica de Burundi y encaja en el bucle norte junto con Ngozi y Muyinga.",
            "see": "Pelícanos y cormoranes desde la orilla o en piragua, la isla de Akagwa, papirales y las colinas de Kirundo al fondo.",
            "access": "Asfalto desde Ngozi hasta Kirundo y pista de tierra corta hasta la orilla; hay sitio para aparcar dos 4x4 sobre hierba. La piragua se contrata con pescadores del lugar. El pin marca el lago, no un embarcadero fijo. La frontera con Ruanda está muy cerca y está CERRADA: no te acerques a los pasos.",
            "when": "Amanecer, cuando las aves están activas y el agua en calma; estación seca para la pista.",
            "skip": "Sáltalo si no te interesan las aves: no hay ninguna otra cosa que hacer allí.",
        },
        links=[
            {"label": "Lago Rwihinda (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Lake_Rwihinda"},
            {"label": "Kirundo (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Kirundo"},
            {"label": "Les Lacs du Nord du Burundi · Lista Indicativa UNESCO", "url": "https://whc.unesco.org/en/statesparties/bi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Le_coucher_du_soleil_au_bord_du_lac_Rwihinda_appel%C3%A9_aussi_lac_aux_oiseaux_%C3%A0_Kirundo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Le_coucher_du_soleil_au_bord_du_lac_Rwihinda_appel%C3%A9_aussi_lac_aux_oiseaux_%C3%A0_Kirundo.jpg",
                "credit": "NIHEREWENIMANA Richard · CC BY-SA 4.0",
                "caption": "Atardecer en el lago Rwihinda.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Les_oiseaux_dans_l'air_en_haut_du_lac_Rwihinda_%C3%A0_Kirundo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Les_oiseaux_dans_l'air_en_haut_du_lac_Rwihinda_%C3%A0_Kirundo.jpg",
                "credit": "NIHEREWENIMANA Richard · CC BY-SA 4.0",
                "caption": "Aves sobre el lago Rwihinda.",
            },
        ],
    ),
    dict(
        n=13, name="Parque nacional de la Ruvubu · la sabana del noreste", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=-3.1666667, lon=30.3333333,  # Google Maps: Parque nacional de Ruvubu
        desc="Con 508 km² repartidos entre Karuzi, Muyinga, Cankuzo y Ruyigi, es el mayor parque de Burundi y EL ÚLTIMO VESTIGIO del ecosistema de pradera natural que cubría el noreste del país. Creado en 1980 y humedal Ramsar desde 2013, lo recorre el río Ruvubu, con hipopótamos, cocodrilos del Nilo, búfalos cafre, cobos de agua, cinco especies de primates y unas 200 de aves. ADVERTENCIA: el MAEC incluye el Parque Nacional de la Ruvubu entre las zonas a evitar.",
        dog_note="Parque nacional con búfalos, hipopótamos y cocodrilos del Nilo: acceso vetado a animales domésticos.",
        visit={
            "why": "Es el único safari de sabana del país y la mejor opción para dormir en plena naturaleza si la situación lo permite.",
            "see": "Meandros del Ruvubu con hipopótamos, manadas de búfalos, cobos de agua, duikers y colinas de pradera quemada.",
            "access": "Asfalto por la RN6 hasta Muyinga o Cankuzo y pistas de tierra hasta las entradas; la red interior es de tierra y exige 4x4 real. Gestión del OBPE con guía obligatorio; tarifas no publicadas en fuente verificable. El pin marca el interior del parque, no una puerta concreta. MAEC lo desaconseja expresamente: consulta antes de entrar.",
            "when": "Estación seca (junio–septiembre), cuando la hierba está baja y los animales bajan al río.",
            "skip": "Descártalo mientras el MAEC lo mantenga entre las zonas a evitar, o si vienes de Tanzania o Kenia: la densidad de fauna no compite.",
        },
        links=[
            {"label": "Parque nacional de la Ruvubu (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ruvubu_National_Park"},
            {"label": "Recomendaciones de viaje MAEC · Burundi", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burundi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Parc_national_de_la_RUVUBU.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Parc_national_de_la_RUVUBU.jpg",
                "credit": "Regis Mugenzi · CC BY-SA 4.0",
                "caption": "La sabana del parque de la Ruvubu.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/At_Ruvubu_National_Park.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:At_Ruvubu_National_Park.jpg",
                "credit": "NZISABIRA Léopold · CC BY-SA 4.0",
                "caption": "El valle del Ruvubu.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/La_splendeur_du_parc_de_la_Ruvubu_et_ses_petits_arbres.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:La_splendeur_du_parc_de_la_Ruvubu_et_ses_petits_arbres.jpg",
                "credit": "Johanna ciella · CC BY-SA 4.0",
                "caption": "Arbolado del parque de la Ruvubu.",
            },
        ],
    ),
    dict(
        n=14, name="Ngozi y el norte cafetero", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=-2.9107175, lon=29.8243599,  # Google Maps: Ngozi
        desc="Tercera ciudad del país, a 1.806 m sobre el nivel del mar y en el corazón de la zona cafetera y tealera del norte. Pasó de 14.511 habitantes en 1990 a 39.884 en 2008, un CRECIMIENTO DEL 175%, y tiene universidad privada desde 1999. Es la escala lógica entre Gitega y los lagos de Kirundo, con combustible, mercado y alojamiento básico. ADVERTENCIA: por Ngozi pasa la línea de alta tensión que une las redes de Ruanda y Burundi; no fotografíes instalaciones eléctricas ni militares.",
        dog_note="Ciudad y fincas al aire libre; atado, por el tráfico y los perros locales.",
        visit={
            "why": "Es la única parada con servicios entre el plateau central y la frontera norte, y la puerta a las colinas del café.",
            "see": "El mercado, las lavaderos de café de las colinas, las plantaciones de té de la zona y el ambiente universitario del centro.",
            "access": "RN6 asfaltada desde Kayanza y Gitega; las pistas a las fincas son de tierra roja, resbaladizas con lluvia. Aparcamiento en hoteles con recinto; dos 4x4 caben sin problema. El pin marca el centro urbano. La frontera con Ruanda, al norte, está CERRADA desde enero de 2024: no planifiques salir por ahí.",
            "when": "Estación seca; la cosecha del café va de abril a julio, cuando los lavaderos están en marcha.",
            "skip": "Sáltala si no necesitas repostar ni dormir: la ciudad en sí tiene poco que ver.",
        },
        links=[
            {"label": "Ngozi (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ngozi,_Burundi"},
            {"label": "FCDO travel advice · Burundi", "url": "https://www.gov.uk/foreign-travel-advice/burundi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Caf%C3%A9_Burundi_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Caf%C3%A9_Burundi_01.jpg",
                "credit": "Edouard mhg · CC0",
                "caption": "Café burundés, el cultivo del norte.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Caf%C3%A9_Burundi_09.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Caf%C3%A9_Burundi_09.jpg",
                "credit": "Edouard mhg · CC0",
                "caption": "Secado del café en Burundi.",
            },
        ],
    ),
    dict(
        n=15, name="Rumonge y la costa sur del Tanganica", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=-3.9754049, lon=29.4388014,  # Google Maps: Rumonge
        desc="Cuarta ciudad de Burundi con 35.931 habitantes en el censo de 2008, capital provincial y puerto sobre el Tanganica: es EL ÚNICO PUNTO DE DESEMBARCO IMPORTANTE del país y un nudo comercial del lago hacia África Oriental. Alrededor se extienden los palmerales de aceite que dan nombre a la comarca. ADVERTENCIA: en mayo de 2024 las crecidas del río Murembwe desplazaron a cientos de familias y, en 2025, las ofensivas del M23 en RD Congo hundieron la actividad del puerto.",
        dog_note="Playas y puerto abiertos; atado y lejos del agua por los cocodrilos.",
        visit={
            "why": "Es la mejor base del sur del lago y la parada obligada entre Buyumbura y Makamba, con playas más tranquilas que las de la capital.",
            "see": "El puerto y las piraguas de pesca, los palmerales, las playas de arena al norte y al sur de la ciudad y las aguas termales de la zona.",
            "access": "RN3 asfaltada desde Buyumbura por la orilla del lago, unos 75 km de curvas; tramos deteriorados. Alojamientos con recinto vallado donde caben dos 4x4. El pin marca el puerto, punto de referencia claro para navegar. Zona no incluida en los avisos de «no viajar» del FCDO.",
            "when": "Estación seca, y última hora de la tarde para el atardecer sobre el lago desde la playa.",
            "skip": "Sáltala si ya has dormido en la costa de Buyumbura y vas directo a Makamba o a Bururi.",
        },
        links=[
            {"label": "Rumonge (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Rumonge"},
            {"label": "Lago Tanganica (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Lake_Tanganyika"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Photo_prise_%C3%A0_Rumonge_au_Burundi.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Photo_prise_%C3%A0_Rumonge_au_Burundi.jpg",
                "credit": "Ntahonsigaye · CC BY-SA 4.0",
                "caption": "Rumonge, en la costa sur del Tanganica.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Beaut%C3%A9_Naturelle_et_Modernit%C3%A9,_Rumonge_se_Transforme.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Beaut%C3%A9_Naturelle_et_Modernit%C3%A9,_Rumonge_se_Transforme.jpg",
                "credit": "Ntahonsigaye · CC0",
                "caption": "El frente lacustre de Rumonge.",
            },
        ],
    ),
    dict(
        n=16, name="Makamba y el extremo sur · la frontera con Tanzania", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=-4.1384805, lon=29.803397,  # Google Maps: Makamba
        desc="Capital de la provincia homónima, a 1.472 m de altitud y con 26.644 habitantes en 2012, es la última ciudad con servicios antes del extremo meridional del país. Por aquí pasa el eje hacia Nyanza-Lac y los pasos hacia Tanzania, LA ÚNICA FRONTERA TERRESTRE OPERATIVA de Burundi mientras siga cerrada la ruandesa. El artículo de Wikipedia es un esbozo muy pobre: casi todo lo práctico hay que confirmarlo sobre el terreno. ADVERTENCIA: escasez recurrente de combustible en el sur.",
        dog_note="Tránsito y ciudad; en puestos fronterizos no se baja del coche con el perro suelto.",
        visit={
            "why": "Es el punto logístico obligado para entrar o salir hacia Tanzania por el sur y para cerrar el bucle del país.",
            "see": "El mercado provincial, las colinas de Buragane y, a poca distancia, la costa del Tanganica en Nyanza-Lac.",
            "access": "Asfalto desde Rumonge y Bururi; el ramal a los pasos fronterizos alterna asfalto y tierra. Hoteles básicos con patio donde caben dos 4x4. El pin marca el centro de la ciudad. El FCDO confirma que la frontera con Tanzania está abierta, pero advierte de opciones de transporte limitadas por la escasez de carburante.",
            "when": "Estación seca; llega con el depósito lleno desde Rumonge o Buyumbura.",
            "skip": "Sáltala si no vas a cruzar a Tanzania: como destino turístico no aporta nada.",
        },
        links=[
            {"label": "Makamba (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Makamba,_Burundi"},
            {"label": "FCDO travel advice · Burundi", "url": "https://www.gov.uk/foreign-travel-advice/burundi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Makamba_Lookout.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Makamba_Lookout.jpg",
                "credit": "Alain Fortuné14 · CC BY-SA 4.0",
                "caption": "El paisaje de Makamba.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Nyaruremba_%C3%A0_Makamba.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Nyaruremba_%C3%A0_Makamba.jpg",
                "credit": "Alain Fortuné14 · CC BY-SA 4.0",
                "caption": "Nyaruremba, en la provincia de Makamba.",
            },
        ],
    ),
    dict(
        n=17, name="Muyinga y el noreste · el eje hacia Kobero", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=-2.8460748, lon=30.3395007,  # Google Maps: Muyinga
        desc="Con 100.715 habitantes en 2012 es una de las ciudades mayores del país, a 1.731 m de altitud en el noreste, sobre la RN6 que lleva al paso de Kobero hacia Tanzania. Funciona como base para el Parque Nacional de la Ruvubu y como escala entre Kirundo y el este. Clima tropical de altura, con unos 1.145 mm de lluvia al año. ADVERTENCIA: Wikipedia no documenta la distancia ni el estado de la carretera hasta Kobero; verifícalo antes de planificar el cruce.",
        dog_note="Ciudad de paso; atado en el mercado y fuera de recintos oficiales.",
        visit={
            "why": "Es la única ciudad con servicios reales del noreste y la puerta natural a la Ruvubu y al paso fronterizo de Kobero.",
            "see": "El mercado, el paisaje de colinas del Bweru y, a media hora, los accesos norte del Parque Nacional de la Ruvubu.",
            "access": "RN6 asfaltada desde Ngozi y Karuzi, con tramos deteriorados; el ramal a la Ruvubu es de tierra. Hoteles con patio cerrado para dos 4x4. El pin marca el centro urbano. Recuerda que el MAEC desaconseja entrar en la Ruvubu.",
            "when": "Estación seca, entre junio y septiembre, para combinarla con la Ruvubu.",
            "skip": "Sáltala si no vas a la Ruvubu ni cruzas a Tanzania por Kobero.",
        },
        links=[
            {"label": "Muyinga (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Muyinga"},
            {"label": "Parque nacional de la Ruvubu (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ruvubu_National_Park"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Muyinga.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Muyinga.jpg",
                "credit": "NIHEREWENIMANA Richard · CC BY-SA 4.0",
                "caption": "Muyinga, en el nordeste.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Maison_de_muyinga.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Maison_de_muyinga.jpg",
                "credit": "NIHEREWENIMANA Richard · CC BY-SA 4.0",
                "caption": "Vivienda tradicional en Muyinga.",
            },
        ],
    ),
    dict(
        n=18, name="Cibitoke y la llanura del Rusizi · la frontera con RD Congo", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="medio día",
        lat=-2.9107321, lon=29.1262613,  # Google Maps: Cibitoke
        desc="Capital provincial a solo 915 m de altitud en la llanura caliente del Rusizi, con 23.885 habitantes en 2008 y seis comunas a su cargo. Es la Burundi tropical y llana, de plátano y caña, pegada a la frontera con RD Congo. ZONA MÁS PELIGROSA DEL PAÍS: el FCDO desaconseja TODO viaje a las comunas de Mugina, Cibitoke, Bukinyayana, Bubanza y Mpanda y a la RN5 al norte del aeropuerto, y el MAEC pide evitar las provincias de Cibitoke y Bubanza y la frontera con RD Congo.",
        dog_note="Zona con controles militares frecuentes: un perro complica cada parada y no hay dónde dejarlo.",
        visit={
            "why": "Solo por completar la ficha del país: geográficamente cierra el bucle noroeste entre el lago y la Kibira.",
            "see": "La llanura aluvial del Rusizi, los plataneros, el paisaje de la falla occidental del Rift y las montañas congoleñas enfrente.",
            "access": "RN5 asfaltada desde Buyumbura, unos 60 km, con controles militares frecuentes. NO hay condiciones de seguridad para pernoctar: el FCDO desaconseja todo viaje a esta zona por incursiones armadas desde RD Congo y presencia rebelde en la Kibira. El pin marca el centro de la ciudad. Prohibido fotografiar puestos, puentes y controles.",
            "when": "No aplica mientras siga vigente el aviso: si algún día se levanta, estación seca y siempre de día.",
            "skip": "Descártalo por defecto. Es el PDI que hay que saltarse salvo que FCDO y MAEC cambien su recomendación.",
        },
        links=[
            {"label": "Cibitoke (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Cibitoke"},
            {"label": "FCDO travel advice · Burundi", "url": "https://www.gov.uk/foreign-travel-advice/burundi"},
            {"label": "Recomendaciones de viaje MAEC · Burundi", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burundi"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Road_in_Cibitoke_Province.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Road_in_Cibitoke_Province.jpg",
                "credit": "pmbuya · CC BY-SA 4.0",
                "caption": "Carretera en la provincia de Cibitoke.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Les_eaux_thermales_de_Ruhwa_en_province_Cibitoke_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Les_eaux_thermales_de_Ruhwa_en_province_Cibitoke_01.jpg",
                "credit": "Kibengado · CC0",
                "caption": "Las aguas termales de Ruhwa.",
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
    ("Aeropuerto Internacional de Buyumbura - Melchior Ndadaye (BJM)", "Frontera", -3.3185123, 29.321004,  # Google Maps: Aeropuerto Internacional Melchior Ndadaye
     "Único aeropuerto internacional y única pista asfaltada del país; 787 m de altitud. En obras de ampliación desde agosto de 2024. Visado a la llegada según el MAEC y punto de entrada documentado para mascotas. Pin comprobado en Google Maps («Aeropuerto Internacional Melchior Ndadaye»)."),
    ("Paso fronterizo Kobero - Kabanga (Tanzania)", "Frontera", -2.664491, 30.4103505,  # Google Maps: Kobero Border Crossing
     "Principal paso operativo del país y eje de carga hacia Dar es Salaam por la RN6. Abierto con normalidad según el FCDO (21-5-2026). Pin comprobado en Google Maps («Kobero Border Crossing»)."),
    ("Paso fronterizo Gatumba - Kavimvira (RD Congo)", "Frontera", -3.3340422, 29.2478551,  # Google Maps: Gatumba
     "Salida hacia Uvira, a unos 15 km al oeste de Buyumbura. Reabierto el 23 de febrero de 2026 tras dos meses cerrado por la ofensiva del M23. Zona desaconsejada por el MAEC y sujeta a cierres sin aviso. Pin comprobado en Google Maps («Gatumba»)."),
    ("Puerto de Buyumbura (lago Tanganica)", "Frontera", -3.377056, 29.345802,  # Google Maps: Puerto de Buyumbura (lago Tanganica) (sin objeto en Google Maps; coordenada de la fuente)
     "Mayor puerto del lago Tanganica, por donde pasa el 80% del comercio exterior. Enlaces con Kigoma (Tanzania), Kalemie (RD Congo) y Mpulungu (Zambia). Modernización al 98% en mayo de 2024. Transbordo de vehículos particulares, por confirmar. Pin comprobado en Google Maps («Puerto de Buyumbura (lago Tanganica) (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Embajada de España en Dar es Salaam (acreditada en Burundi)", "Consular", -6.7905332, 39.2783378,  # Google Maps: Embajada de España en Dar es Salaam
     "99 B Kinondoni Road, P.O. Box 842, Dar es Salaam (Tanzania). Tel. +255 22 266 6018 / 6019 / 266 6936. Emergencia consular +255 754 042 123. emb.daressalaam@maec.es. Acreditada ante Burundi y Ruanda. COORDENADAS APROXIMADAS del barrio de Kinondoni: verificar. Pin comprobado en Google Maps («Embajada de España en Dar es Salaam»)."),
    ("Consulado Honorario de España en Buyumbura", "Consular", -3.361378, 29.3598782,  # Google Maps: Buyumbura
     "Cónsul honoraria: Almudena Moreno del Pozo. Tel. +257 76 71 58 25 y +257 79 51 80 50 (MAEC, 6-5-2026). Dirección exacta no publicada en la ficha del MAEC: por confirmar. Pin comprobado en Google Maps («Buyumbura»)."),
    ("Kira Hospital (Kinindo, Buyumbura)", "Hospital", -3.3996408, 29.3592219,  # Google Maps: Kira Hospital
     "Hospital privado abierto en 2015, 130 camas y 14 servicios (cardiología, imagen, oncología, neurocirugía, traumatología). Es la mejor referencia del país, aunque su gestión se deterioro tras la intervención estatal de 2022. Al oeste del Boulevard de la Liberté, al sur del río Muha. Pin comprobado en Google Maps («Kira Hospital»)."),
    ("Clinique Prince Louis Rwagasore (centro de Buyumbura)", "Hospital", -3.38778, 29.36778,  # Google Maps: Clinique Prince Louis Rwagasore (centro de Buyumbura) (sin objeto en Google Maps; coordenada de la fuente)
     "Hospital público en pleno centro, al sur del antiguo mercado central, entre la Avenue Croix Rouge, el Boulevard Patrice Lumumba y la Avenue Pierre Ngendandumwe. Infrafinanciado: en 2022 se le reprochaba equipamiento envejecido y suministro de agua irregular. Urgencias de proximidad, no de referencia. Pin comprobado en Google Maps («Clinique Prince Louis Rwagasore (centro de Buyumbura) (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Último repostaje fiable antes de entrar: Ngara (Tanzania)", "Combustible", -2.495627, 30.6458749,  # Google Maps: Ngara (Tanzania)
     "Los últimos overlanders documentados (marzo de 2025) repostaron en Ngara Oil, lado tanzano, a 3.069 TZS por litro, justo antes de Kabanga, porque en Burundi había escasez de diesel. Entrar con jerricanes llenos. Pin comprobado en Google Maps («Ngara (Tanzania)»)."),
    ("Buyumbura: única zona con red de gasolineras y cajeros", "Combustible", -3.3822, 29.3644,  # Google Maps: Buyumbura: única zona con red de gasolineras y cajeros (sin objeto en Google Maps; coordenada de la fuente)
     "Buyumbura y Gitega son las únicas ciudades con cajeros automáticos (Canadá, 9-9-2026) y con red de estaciones de servicio. En abril de 2026 esa red estaba seca: surtidores sin producto y mercado negro entre 18.000 y 40.000 BIF/litro frente a 4.000 oficiales. Pin comprobado en Google Maps («Buyumbura: única zona con red de gasolineras y cajeros (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Agua: red urbana de Buyumbura (uso general, no potable)", "Agua potable", -3.3869917, 29.3615275,  # Google Maps: REGIDESO Headquarters
     "La red urbana de Buyumbura sirve para llenar depósitos de ducha y lavado, nunca para beber sin filtrar y potabilizar. El suministro es intermitente incluso en el centro. Fuera de Buyumbura y Gitega no contar con red fiable. Puntos concretos verificados, por confirmar. Pin comprobado en Google Maps («REGIDESO Headquarters»)."),
]

DRONE_CALLOUT = ("warn", "Legales sobre el papel, peligrosos en la práctica",
                 "Burundi no prohibe los drones: la Autoridad de Aviación Civil (AACB) los regula por clases de peso y uso, exige registro también a los visitantes, limita el vuelo recreativo a 300 pies y veta los 10 km alrededor de aeródromos (drone-laws.com, actualizado el 8 de enero de 2026). El problema es otro: está prohibido fotografiar instalaciones militares, puertos, edificios oficiales y uniformados, y hay ataques con granada y controles constantes. Un dron en el aire en un país no libre con 13/100 en Freedom House es una invitación a que te confisquen el equipo y te interroguen.")

STARLINK_CALLOUT = ("", "Starlink activo, pero la electricidad y el combustible no",
                    "Burundi figura entre los 26 países africanos con Starlink operativo en junio de 2026, y el servicio se autorizó en 2024. Para la expedición eso resuelve la conectividad en un país donde la cobertura móvil fuera de Buyumbura y Gitega es irregular. Lo que no resuelve es la energía: con una crisis de combustible que en abril de 2026 dejo los surtidores secos, alimentar el plato depende enteramente del sistema solar y de batería de los vehículos. El régimen de Roam para terminales extranjeras, y si aduanas cuestiona la antena, están por confirmar.")

DOG_MATRIX = [
    ("Entrada por aeropuerto de Buyumbura (BJM)", "permitido con condiciones", "Microchip, rabia +30 días, certificado endosado y permiso previo del Ministerio de Agricultura y Ganadería. Pedir el permiso por correo con varias semanas de margen."),
    ("Entrada por tierra desde Tanzania (Kobero-Kabanga)", "por confirmar", "Ninguna fuente documenta entrada de mascotas por paso terrestre. Plan B: confirmar por escrito con el servicio veterinario antes de salir de Dar es Salaam; si no hay respuesta, no intentarlo."),
    ("Entrada por Gatumba desde RD Congo", "no recomendado", "Paso reabierto el 23 de febrero de 2026 pero en zona de conflicto y sujeto a cierres sin aviso. Con perro y dos vehículos, no."),
    ("Parques nacionales (Kibira, Ruvubu, Rusizi)", "prohibido", "Perros no admitidos en areas protegidas con fauna, y además Kibira y Ruvubu están desaconsejados por el MAEC. Plan B: dejar el itinerario en lago y ciudades."),
    ("Alojamientos y hoteles en Buyumbura y Gitega", "por confirmar", "Sin fuente. Plan B: dormir en los vehículos en recintos vigilados y confirmar caso a caso por teléfono."),
    ("Regreso a la UE desde Burundi", "permitido con condiciones", "Titulación antirrábica hecha en la UE antes de salir y certificado zoosanitario; entrada por punto de entrada de viajeros designado. Plan B: si falta la titulación, el perro no vuelve: 3 meses de espera tras la extracción."),
]

SOURCES = [
    ("MAEC - Recomendaciones de viaje: Burundi (Ministerio de Asuntos Exteriores, actualizado 6 de mayo de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Burundi"),
    ("Embajada de España en Tanzania - Dar es Salaam, acreditada ante Burundi y Ruanda (MAEC, consultado en septiembre de 2026)", "https://www.exteriores.gob.es/Embajadas/daressalaam/es/Paginas/index.aspx"),
    ("Foreign travel advice: Burundi (FCDO, Reino Unido, actualizado el 21 de mayo de 2026)", "https://www.gov.uk/foreign-travel-advice/burundi"),
    ("Burundi travel advice - Safety and security (FCDO, Reino Unido, 2026)", "https://www.gov.uk/foreign-travel-advice/burundi/safety-and-security"),
    ("Burundi travel advice and advisories (Gobierno de Canadá, actualizado el 9 de septiembre de 2026)", "https://travel.gc.ca/destinations/burundi"),
    ("Burundi: Freedom in the World 2026 (Freedom House, 2026)", "https://freedomhouse.org/country/burundi/freedom-world/2026"),
    ("2026 in Burundi (Wikipedia, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2026_in_Burundi"),
    ("2025 in Burundi (Wikipedia, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/2025_in_Burundi"),
    ("Burundi (Wikipedia, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Burundi"),
    ("Visa policy of Burundi (Wikipedia, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Visa_policy_of_Burundi"),
    ("Updated Status of Burundi-Rwanda Border 2026 (4x4 Uganda, 28 de abril de 2026)", "https://www.4x4uganda.com/news/updated-status-of-burundi-rwanda-border-2026.html"),
    ("Burundi: the fuel shortage paralyzes transportation throughout Bujumbura (SOS Médias Burundi, 30 de abril de 2026)", "https://www.sosmediasburundi.org/en/2026/04/30/burundi-the-fuel-shortage-paralyzes-transportation-throughout-bujumbura/"),
    ("Burundi gasoline prices (GlobalPetrolPrices, dato de 9 de febrero de 2026)", "https://www.globalpetrolprices.com/Burundi/gasoline_prices/"),
    ("Kobero Border (Live The Life Expeditions / dinotruck.com, relato de overlanders del 5 de marzo de 2025)", "https://www.dinotruck.com/africa/kobero-border/"),
    ("Carnet de Passages en Douane - Burundi (carnetdepassage.org, consultado en septiembre de 2026)", "https://www.carnetdepassage.org/country/burundi"),
    ("Drone Laws in Burundi (drone-laws.com, actualizado el 8 de enero de 2026)", "https://drone-laws.com/drone-laws-in-burundi/"),
    ("Starlink in África: countries, prices and speeds (tech.africa, junio de 2026)", "https://tech.africa/starlink-africa/"),
    ("Burundi Pet Import Requirements (PetTravel.com, consultado en septiembre de 2026)", "https://www.pettravel.com/information/pet-passports/burundi-pet-import-requirements/"),
    ("Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026, listas de terceros países para desplazamientos sin ánimo comercial de animales de compañía (EUR-Lex)", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600636"),
    ("Reglamento Delegado (UE) 2026/131 de la Comisión, de 20 de enero de 2026 (EUR-Lex)", "https://eur-lex.europa.eu/legal-content/ES/TXT/PDF/?uri=OJ%3AL_202600131"),
    ("Burundi - States Parties, Lista del Patrimonio Mundial (UNESCO, consultado en septiembre de 2026)", "https://whc.unesco.org/en/statesparties/bi"),
    ("Melchior Ndadaye International Airport (Wikipedia, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Melchior_Ndadaye_International_Airport"),
    ("Port of Bujumbura (Wikipedia, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Port_of_Bujumbura"),
    ("Gatumba (Wikipedia, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Gatumba"),
    ("Kira Hospital (Wikipedia, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Kira_Hospital"),
    ("Prince Louis Rwagasore Clinical Hospital (Wikipedia, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Prince_Louis_Rwagasore_Clinical_Hospital"),
    ("Burundi-Rwanda rivalry: RED-Tabara rebel attacks add to regional tensions (The Conversation, 2024)", "https://theconversation.com/burundi-rwanda-rivalry-red-tabara-rebel-attacks-add-to-regional-tensions-225801"),
    ("Ficha País: Burundi (Oficina de Información Diplomática, MAEC, marzo de 2026, PDF)", "https://www.exteriores.gob.es/Documents/FichasPais/BURUNDI_FICHA%20PAIS.pdf"),
    ("Ministère de l'Environnement, de l'Agriculture et de l'Élevage - MINEAGRIE (web oficial, en construcción, consultada en septiembre de 2026)", "https://www.mineagrie.gov.bi/"),
    ("Rwanda and Burundi Land Border Crossing Status (Eco Adventure Safaris, 31 de mayo de 2025)", "https://ecoadventuresafaris.com/rwanda-and-burundi-land-border-crossing-status/"),
    ("Is Burundi Safe To Travel? New Travel Restrictions In 2026? (Augustine Tours, actualizado el 14 de mayo de 2026)", "https://augustinetours.com/is-burundi-safe-to-travel/"),
    ("Camping in Burundi (M Travel and Tours Burundi, 9 de junio de 2025)", "https://mtravelandtoursbi.com/blog/2025/06/09/camping-in-burundi/"),
    ("Buyumbura (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bujumbura"),
    ("Lago Tanganica (Wikipedia EN)", "https://en.wikipedia.org/wiki/Lake_Tanganyika"),
    ("Saga Beach · Lonely Planet", "https://www.lonelyplanet.com/points-of-interest/saga-beach/1013772"),
    ("Livingstone–Stanley Monument (Wikipedia EN)", "https://en.wikipedia.org/wiki/Livingstone%E2%80%93Stanley_Monument"),
    ("Río Mugere (Wikipedia EN)", "https://en.wikipedia.org/wiki/Mugere_River"),
    ("Parc National de la Rusizi · CHM Biodiversité du Burundi (oficial)", "https://bi.chm-cbd.net/fr/protected-areas/parc-nati-rusizi"),
    ("Parque nacional de la Rusizi (Wikipedia EN)", "https://en.wikipedia.org/wiki/Rusizi_National_Park"),
    ("Gitega (Wikipedia EN)", "https://en.wikipedia.org/wiki/Gitega"),
    ("Museo Nacional de Gitega (Wikipedia EN)", "https://en.wikipedia.org/wiki/National_Museum_of_Gitega"),
    ("Gishora (Wikipedia EN)", "https://en.wikipedia.org/wiki/Gishora"),
    ("Danza ritual del tambor real · UNESCO Patrimonio Inmaterial (2014)", "https://ich.unesco.org/en/RL/ritual-dance-of-the-royal-drum-00989"),
    ("Résidence Royale de Gishora · Lista Indicativa UNESCO", "https://whc.unesco.org/en/tentativelists/6927"),
    ("Guide touristique · Destination Parc National de la Kibira (PDF oficial, OBPE/CHM)", "https://bi.chm-cbd.net/sites/bi/files/2020-04/guide-tourist-pnk.pdf"),
    ("Parque nacional de la Kibira (Wikipedia EN)", "https://en.wikipedia.org/wiki/Kibira_National_Park"),
    ("Reserva natural forestal de Bururi (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bururi_Forest_Nature_Reserve"),
    ("Bururi (Wikipedia EN)", "https://en.wikipedia.org/wiki/Bururi"),
    ("Monte Kikizi (Wikipedia EN)", "https://en.wikipedia.org/wiki/Mount_Kikizi"),
    ("Rutovu (Wikipedia EN)", "https://en.wikipedia.org/wiki/Rutovu"),
    ("Gasumo, la source la plus méridionale du Nil · Lista Indicativa UNESCO", "https://whc.unesco.org/en/tentativelists/5144/"),
    ("Atouts touristiques et monuments naturels de l'Est du Burundi (PDF oficial, Ministerio de Medio Ambiente/CHM)", "https://bi.chm-cbd.net/sites/bi/files/2022-03/attout-tourist-monum-natur-est-bi.pdf"),
    ("Chutes de la Karera (Wikipedia EN)", "https://en.wikipedia.org/wiki/Karera_waterfalls"),
    ("Les Chutes de Karera · Lista Indicativa UNESCO", "https://whc.unesco.org/en/tentativelists/6932/"),
    ("La faille de Nyakazu · Lista Indicativa UNESCO (2026)", "https://whc.unesco.org/en/tentativelists/6930/"),
    ("Provincia de Rutana (Wikipedia EN)", "https://en.wikipedia.org/wiki/Rutana_Province"),
    ("Lago Rwihinda (Wikipedia EN)", "https://en.wikipedia.org/wiki/Lake_Rwihinda"),
    ("Kirundo (Wikipedia EN)", "https://en.wikipedia.org/wiki/Kirundo"),
    ("Parque nacional de la Ruvubu (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ruvubu_National_Park"),
    ("Ngozi (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ngozi,_Burundi"),
    ("Rumonge (Wikipedia EN)", "https://en.wikipedia.org/wiki/Rumonge"),
    ("Makamba (Wikipedia EN)", "https://en.wikipedia.org/wiki/Makamba,_Burundi"),
    ("Muyinga (Wikipedia EN)", "https://en.wikipedia.org/wiki/Muyinga"),
    ("Cibitoke (Wikipedia EN)", "https://en.wikipedia.org/wiki/Cibitoke"),
]

# Bucle de Burundi · Buyumbura – norte – plateau – este – sur – Buyumbura
CORRIDOR = [
    (-3.36278, 29.36556),
    (-3.35127, 29.26388),
    (-2.91073, 29.12626),
    (-2.91466, 29.43361),
    (-2.91072, 29.82436),
    (-2.54898, 30.08097),
    (-2.84607, 30.3395),
    (-3.16667, 30.33333),
    (-3.41822, 29.90861),
    (-3.36286, 29.92196),
    (-3.83019, 30.0794),
    (-3.89528, 30.12694),
    (-4.13848, 29.8034),
    (-3.9754, 29.4388),
    (-3.93782, 29.5977),
    (-3.91515, 29.83787),
    (-3.36278, 29.36556),
]

# Bucle corto del sur · Buyumbura – Rumonge – Makamba – Bururi – Rutovu – Gitega
CORRIDOR_ALT = [
    (-3.36278, 29.36556),
    (-3.48197, 29.35258),
    (-3.9754, 29.4388),
    (-4.13848, 29.8034),
    (-3.93782, 29.5977),
    (-3.91515, 29.83787),
    (-3.41822, 29.90861),
    (-3.36278, 29.36556),
]

HISTORIA_RESUMEN = "Burundi es un país pequeño, montañoso y densamente poblado del corazón de los Grandes Lagos, heredero de un reino anterior a la llegada de los europeos que Alemania y después Bélgica administraron junto a Ruanda. Desde la independencia en 1962 su historia ha estado marcada por golpes de Estado, matanzas y una guerra civil que terminó con los acuerdos de Arusha y la llegada al poder del CNDD-FDD en 2005. La crisis del tercer mandato de Pierre Nkurunziza en 2015 dejó centenares de muertos y cientos de miles de refugiados, y aunque Évariste Ndayishimiye preside el país desde 2020 con cierta normalización diplomática, Freedom House lo sigue clasificando como «no libre». Hoy combina una pobreza extrema con las réplicas del conflicto del este del Congo."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>Burundi pertenece al reducido grupo de Estados africanos cuyas fronteras no las dibujó Europa, sino una monarquía anterior a la colonización. Según la <em>Encyclopædia Britannica</em>, el territorio lo poblaron primero los twa, cazadores-recolectores; hacia el año 1000 llegaron agricultores hutu y más tarde los tutsi, que en el siglo XVI establecieron una monarquía bajo la figura fundacional de Ntare Rushatsi.</p><p>El reino estaba encabezado por el <em>mwami</em>, un soberano sacro rodeado de linajes principescos, y se organizaba en colinas — la unidad básica del poblamiento que todavía estructura el país. Britannica subraya un matiz decisivo para entender lo que vino después: la identificación étnica era <strong>fluida</strong>. Pese a las diferencias físicas descritas por las fuentes, los matrimonios cruzados y una <strong>lengua común, el kirundi</strong>, permitían movilidad social entre grupos, de modo que hutu y tutsi funcionaban más como categorías sociales y ganaderas que como naciones separadas.</p><p>Esa unidad lingüística sigue siendo excepcional en África: la Wikipedia en español cifra en torno al noventa y siete por ciento los hablantes de kirundi como lengua materna. El viajero encontrará, por tanto, un país culturalmente homogéneo cuya fractura política no nació de la diversidad idiomática.</p>"),
    ("Colonización",
     "<p>Los primeros europeos llegaron tarde. Britannica sitúa la visita de exploradores británicos en 1858 y la incorporación del territorio al protectorado alemán de África Oriental en <strong>1890</strong>. Alemania gobernó de forma indirecta, apoyándose en el <em>mwami</em> y en las estructuras del reino, sin desmontarlas.</p><p>Tras la Primera Guerra Mundial el mapa cambió: Burundi y Ruanda fueron adjudicados a Bélgica como el <strong>mandato de Ruanda-Urundi</strong>, primero bajo la Sociedad de Naciones y después como fideicomiso de Naciones Unidas. La administración belga es la que deja la herencia más pesada. Según Britannica, los colonizadores <strong>rigidificaron las categorías étnicas</strong>, hasta entonces permeables, y favorecieron sistemáticamente a los tutsi sobre los hutu en la administración, concentrando el poder en una minoría y convirtiendo una diferencia social en una jerarquía administrativa fija.</p><p>A ese sesgo se sumaron la evangelización católica — que explica el peso actual de la Iglesia — y una economía orientada a la exportación de café. La ficha país del Ministerio de Asuntos Exteriores español, actualizada en marzo de 2026, resume el resultado con crudeza: desde la independencia el país «ha vivido una tensión política y social constante derivada del enfrentamiento entre las dos principales etnias, hutu y tutsi». Ese enfrentamiento es, en buena medida, una construcción colonial.</p>"),
    ("Independencia y construcción del Estado",
     "<p>Burundi accedió a la independencia el <strong>1 de julio de 1962</strong>, separado de Ruanda y con la monarquía restaurada bajo el rey Mwambutsa IV. El proceso nació herido: el príncipe Luis Rwagasore, líder nacionalista y figura aglutinadora, había sido asesinado en <strong>1961</strong>, y Britannica data ahí el inicio de una crisis persistente.</p><p>La monarquía cayó pronto. La Wikipedia en español sitúa la proclamación de la república en <strong>1966</strong>; Britannica precisa que Michel Micombero presidió la Primera República hasta 1976, cuando Jean-Baptiste Bagaza inauguró la Segunda. El episodio más oscuro de ese periodo son las <strong>matanzas de 1972</strong>, que según Britannica eliminaron entre cien mil y doscientos mil hutu y descabezaron a toda una generación instruida.</p><p>Los años noventa trajeron una apertura y una catástrofe. El asesinato del primer presidente hutu elegido en las urnas desencadenó una guerra civil que, según la Wikipedia en español, entre 1993 y 1999 produjo «centenares de miles de refugiados y unos 250 000 muertos». La salida fue negociada: el Ministerio español recuerda que la mediación internacional — con Tanzania y Sudáfrica al frente y con Julius Nyerere y Nelson Mandela como facilitadores — condujo a los <strong>acuerdos de Arusha</strong>, con despliegue de Naciones Unidas para su aplicación.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>Arusha organizó un reparto étnico del poder y abrió la transición. El antiguo movimiento rebelde CNDD-FDD pasó a la vía parlamentaria tras los acuerdos de 2003 y domina la política desde <strong>2005</strong>, año en que <strong>Pierre Nkurunziza</strong> fue elegido presidente por el Parlamento, según la Wikipedia en inglés.</p><p>La ruptura llegó el <strong>25 de abril de 2015</strong>, cuando Nkurunziza anunció que optaría a un tercer mandato, en aparente contradicción con los límites fijados en Arusha. Siguieron protestas masivas y, el <strong>13 de mayo de 2015</strong>, un golpe fallido encabezado por el general Godefroid Niyombare. Nkurunziza ganó las elecciones de julio con la oposición en el boicot. La misma fuente cifra el saldo de la represión en torno a <strong>mil setecientos civiles muertos y trescientos noventa mil refugiados</strong>. El Ministerio español recuerda que la comisión de investigación de Naciones Unidas concluyó que probablemente se cometieron «crímenes contra la humanidad», y que Burundi se retiró de la Corte Penal Internacional en <strong>2017</strong>.</p><p>Un referéndum de mayo de 2018 amplió el mandato presidencial de cinco a siete años. Nkurunziza murió el <strong>8 de junio de 2020</strong> — infarto según la versión oficial — y le sucedió Évariste Ndayishimiye, que ya había ganado las presidenciales del 20 de mayo con el sesenta y siete por ciento de los votos.</p>"),
    ("Política y gobierno en 2026",
     "<p>A septiembre de 2026, según la ficha país del Ministerio de Asuntos Exteriores español (marzo de 2026), Burundi es una <strong>república presidencialista</strong> que preside <strong>Évariste Ndayishimiye</strong> desde 2020, con <strong>Nestor Ntahontuye</strong> como primer ministro. En las legislativas del <strong>5 de junio de 2025</strong> el CNDD-FDD obtuvo el 96,51 % de los votos y <em>todos</em> los escaños. <strong>Gitega</strong> es la capital oficial desde 2019 y Buyumbura la administrativa y motor económico.</p><p>No es una democracia. Freedom House la clasifica en <em>Freedom in the World 2025</em> como <strong>«Not Free»</strong>, con <strong>15 sobre 100</strong> — 4 de 40 en derechos políticos y 11 de 60 en libertades civiles —: los avances de la posguerra «han sido deshechos por un giro hacia la política autoritaria y la represión violenta». Human Rights Watch recoge en su Informe Mundial 2026 <strong>892 detenciones arbitrarias y 605 ejecuciones extrajudiciales</strong> entre enero de 2024 y mayo de 2025, y Reporteros Sin Fronteras lo sitúa en el <strong>puesto 119 de 180</strong> en libertad de prensa (2026).</p><p>La frontera con Ruanda <strong>sigue cerrada</strong> desde el 15 de enero de 2024, por la acusación burundesa de que Kigali apoya al grupo armado RED-Tabara. Según HRW, más de setenta mil congoleños han huido al país por el conflicto del este. El Ministerio español señala el levantamiento de sanciones de la UE; con España hay relaciones desde 1969 y embajada concurrente en Tanzania.</p>"),
    ("Economía y recursos",
     "<p>Burundi es uno de los países más pobres del mundo. La ficha del Ministerio español cifra el PIB de 2024 en <strong>2.160 millones de dólares</strong> y el <strong>PIB per cápita en 255 dólares</strong>; el Banco Mundial da <strong>233,8 dólares per cápita en 2025</strong> y un crecimiento del 4,2 %. La moneda es el <strong>franco burundés</strong>.</p><p>La estructura productiva sigue siendo agraria: según el Ministerio, en 2024 el sector primario aportaba el 40 % del PIB, la industria el 15 % y los servicios el 45 %. En las exportaciones de 2025 los alimentos — <strong>café y té</strong>, ante todo — suponían el 65 %, los minerales y metales el 20 % y las manufacturas el 11 %. El país depende de la ayuda externa y de las remesas, que el Banco Mundial estima en el 8,1 % del PIB.</p><p>El cuadro es frágil. El Ministerio registra una inflación del 20,2 % en 2024 y un índice de desarrollo humano de 0,426 en 2021, puesto 187 de 191; Human Rights Watch habla de un 40 % de inflación en febrero de 2025 y de una <strong>escasez crónica de combustible</strong> que paraliza el transporte. El Banco Mundial cifra el acceso a la electricidad en el 20,1 % de la población. Para el viajero overland eso significa colas de gasolina, cortes de luz y una economía de divisas tensionada.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Con unos <strong>14,3 millones de habitantes</strong> en 2025 y <strong>505 por kilómetro cuadrado</strong>, Burundi tiene una de las densidades más altas de África, según el Ministerio español. Los idiomas oficiales son el <strong>kirundi y el francés</strong>, y el kiswahili se habla en algunas zonas: en carretera, el francés resuelve casi todo trámite. La misma fuente da un 61,4 % de católicos, un 21,4 % de protestantes y un 2,5 % de musulmanes. Las fuentes describen la población como hutu, tutsi y twa.</p><p>La expresión cultural más reconocible es el <strong>tambor</strong>. La UNESCO inscribió en 2014 la danza ritual del tambor real en la Lista Representativa del Patrimonio Cultural Inmaterial: una docena larga de tambores en número impar en semicírculo, con poesía heroica y canto. En cambio, Burundi <strong>no tiene ningún bien inscrito en la Lista del Patrimonio Mundial</strong>, aunque mantiene diez sitios en lista indicativa. La cocina gira en torno a batata, maíz y guisantes.</p><p>Tres apuntes de convivencia. Viste sobrio: el país es conservador y muy religioso. <strong>No fotografíes instalaciones oficiales, militares ni policiales</strong>, y pide permiso antes de retratar a personas: los controles de carretera son frecuentes. El alcohol se consume con normalidad, pero durante el ramadán — que en 2027 empieza en torno al 8 de febrero — conviene ser discreto al comer o beber en los barrios musulmanes de Buyumbura.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Burundi (Ministerio de Asuntos Exteriores, España · PDF · marzo de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/BURUNDI_FICHA%20PAIS.pdf"),
    ("Burundi: Freedom in the World 2025 (Freedom House · 2025)", "https://freedomhouse.org/country/burundi/freedom-world/2025"),
    ("Burundi — History (Encyclopædia Britannica · consultado 19/09/2026)", "https://www.britannica.com/place/Burundi/History"),
    ("Burundi (Encyclopædia Britannica · actualizado 18/09/2026)", "https://www.britannica.com/place/Burundi"),
    ("Burundi (Wikipedia en español · consultado 19/09/2026)", "https://es.wikipedia.org/wiki/Burundi"),
    ("Pierre Nkurunziza (Wikipedia en inglés · consultado 19/09/2026)", "https://en.wikipedia.org/wiki/Pierre_Nkurunziza"),
    ("Burundi–Rwanda relations (Wikipedia en inglés · consultado 19/09/2026)", "https://en.wikipedia.org/wiki/Burundi%E2%80%93Rwanda_relations"),
    ("Visa policy of Burundi (Wikipedia en inglés · consultado 19/09/2026)", "https://en.wikipedia.org/wiki/Visa_policy_of_Burundi"),
    ("Burundi — States Parties (UNESCO, Centro del Patrimonio Mundial · consultado 19/09/2026)", "https://whc.unesco.org/en/statesparties/bi"),
    ("Ritual dance of the royal drum (UNESCO, Patrimonio Cultural Inmaterial · inscrito en 2014)", "https://ich.unesco.org/en/RL/ritual-dance-of-the-royal-drum-00989"),
    ("Burundi (Reporteros Sin Fronteras · Clasificación Mundial de la Libertad de Prensa 2026)", "https://rsf.org/en/country/burundi"),
    ("Burundi — World Report 2026 (Human Rights Watch · 2026)", "https://www.hrw.org/world-report/2026/country-chapters/burundi"),
    ("Burundi Situation (ACNUR · Operational Data Portal · datos a 31/08/2026)", "https://data.unhcr.org/en/situations/burundi"),
    ("Burundi — Datos del país (Banco Mundial · valores de 2025)", "https://data.worldbank.org/country/burundi"),
    ("Rwanda, Burundi Officials Acknowledge Setbacks as Border Standoff Nears Two Years (Breaking Burundi · consultado 19/09/2026)", "https://breakingburundi.com/rwanda-burundi-officials-acknowledge-setbacks-as-border-standoff-nears-two-years/"),
]

SPEC = dict(
    slug="burundi", name="Burundi", revision="18 sep 2026",
    sub="FUERA DE RUTA — frontera con Ruanda CERRADA desde enero de 2024 · solo se entra por Tanzania o en avión · lago Tanganica y Gitega",
    chips=[
        ("ESTATUS", "FUERA DE RUTA. País continental de 26.338 km² y 14,3 millones de habitantes…"),
        ("CÓMO LLEGAR", ""),
        ("VISADO", "OBLIGATORIO para españoles. eVisa en migration.gov.bi con 15 días de antelación…"),
        ("VEHÍCULO", "Importación temporal en frontera. El carnet de passages se acepta y se sella (relato en Kobero…"),
        ("SEGURIDAD", "No libre 13/100 · granadas y conflicto en el oeste"),
        ("SEGURO", "Carta Verde NO vale · Yellow Card COMESA en frontera"),
        ("SALUD", "Fiebre amarilla OBLIGATORIA · malaria endémica"),
        ("DRONES", "Legales con registro · fotografiar oficial, prohibido"),
        ("STARLINK", "Activo desde 2024 · energía a cargo del vehículo"),
        ("4x4", "Solo por Tanzania · entrar con depósito lleno"),
        ("A PIE", "No de noche · ni calle ni transporte tras el ocaso"),
        ("PERRO", "Entrada con microchip ISO, rabia al menos 30 días antes…"),
        ("MONEDA", "Franco burundés (BIF). Economía de efectivo: cajeros solo en Buyumbura y Gitega (Canadá…"),
        ("VENTANA", "Ecuatorial de altitud: la meseta ronda los 1.700 m y suaviza el calor…"),
    ],
    center=[-3.34, 29.73], zoom=7,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle de Burundi · Buyumbura – norte – plateau – este – sur – Buyumbura",
    corridor_alt_label="Bucle corto del sur · Buyumbura – Rumonge – Makamba – Bururi – Rutovu – Gitega",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Le_Faille_de_Nyakazu_(des_Allemands).jpg?width=1200",
    hero_credit="Falla de Nyakazu · John Busokoza · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Burundi queda fuera de la ruta de 2027 por logística, no por falta de interés. Es continental y limita con tres vecinos del corredor, pero la frontera con Ruanda sigue CERRADA desde enero de 2024: lo confirman el FCDO el 21 de mayo de 2026 y el Gobierno de Canadá el 9 de septiembre de 2026. El acceso natural desde el norte no existe. Solo quedan Tanzania, por Kobero-Kabanga, y Gatumba hacia Uvira, esta última en zona de conflicto y con cierres sin aviso. A eso se suma una crisis crónica de combustible que en abril de 2026 puso el litro de mercado negro entre 18.000 y 40.000 francos frente a los 4.000 oficiales, con surtidores secos en Buyumbura. Entrar con dos 4x4 y un perro en un fondo de saco sin garantía de repostar no compensa. El único acceso practicable hoy es el rodeo por Tanzania: Kigali-Rusumo 167 km, Rusumo-Kobero 56 km y Kobero-Gitega 124 km, con visado tanzano aparte. Si se reabriera la frontera ruandesa y se normalizase el carburante, Burundi encajaría como desvio de 4 a 6 días: Buyumbura, el lago Tanganica, las cataratas de Karera y la fuente sur del Nilo en Gasumo. Coste orientativo: 90 USD de visado por persona y 300-500 USD entre combustible y seguro regional. Y quedaría por decidir que hacer con el perro, porque Burundi no figura en el Reglamento (UE) 2026/636 y obliga a titulación antirrábica para volver a la UE.",
    facts=[
        ("Estatus", "FUERA DE RUTA. País continental de 26.338 km² y 14,3 millones de habitantes, con Gitega como capital oficial desde 2019 y Buyumbura como capital económica (Ficha País del MAEC, marzo de 2026). Limita con tres vecinos del corredor, pero no tiene salida natural: la frontera con Ruanda sigue cerrada desde enero de 2024 (Canadá, 9-9-2026; FCDO, 21-5-2026)."),
        ("Como llegar", "Por tierra solo desde Tanzania (Kobero-Kabanga, eje de carga a Dar es Salaam) o desde RD Congo por Gatumba-Kavimvira, reabierto el 23 de febrero de 2026 tras dos meses cerrado por la ofensiva del M23. En avión, Buyumbura-Melchior Ndadaye (BJM)."),
        ("Visado", "OBLIGATORIO para españoles. eVisa en migration.gov.bi con 15 días de antelación, 90 USD para un mes; también se expide a la llegada en el aeropuerto y, según relatos de overlanders, en los pasos terrestres (MAEC, 6-5-2026)."),
        ("Vehículo / aduana", "Importación temporal en frontera. El carnet de passages se acepta y se sella (relato en Kobero, marzo de 2025), pero ninguna fuente oficial abierta lo declara obligatorio: llevarlo es lo prudente. No hay entidad emisora de CPD en el país (carnetdepassage.org)."),
        ("Seguro", "La Carta Verde europea NO cubre Burundi. Se compra seguro local en frontera o Carte Jaune COMESA (Yellow Card), que Burundi reconoce como estado miembro del COMESA. Importe y ventanilla, por confirmar."),
        ("Moneda", "Franco burundés (BIF). Economía de efectivo: cajeros solo en Buyumbura y Gitega (Canadá, 9-9-2026). Los dólares solo se aceptan si son posteriores a 2006 y están en buen estado (MAEC). Tarjetas casi inútiles."),
        ("Perro", "Entrada con microchip ISO, rabia al menos 30 días antes, certificado sanitario endosado y permiso de importación del Ministerio de Medio Ambiente, Agricultura y Ganadería (PetTravel). Punto de entrada citado: aeropuerto de Buyumbura. Entrada por tierra con perro, POR CONFIRMAR."),
        ("Drones", "No hay prohibición general: la AACB los regula por clases, con registro obligatorio también para visitantes, techo de 300 pies en uso recreativo y veto a 10 km de aeródromos (drone-laws.com, 8-1-2026). En la práctica, volar cerca de cualquier instalación oficial es buscarse un problema serio."),
        ("Starlink", "Operativo. Burundi figura entre los 26 países africanos con servicio activo en junio de 2026 (tech.africa). Servicio residencial autorizado desde 2024; el régimen de Roam para extranjeros, por confirmar."),
        ("Seguridad", "Freedom House 2026: NO LIBRE, 13/100 (2/40 en derechos políticos, 11/60 en libertades civiles). Ataques con granada frecuentes en Buyumbura, réplicas del conflicto del Kivu en el oeste y presencia de RED-Tabara desde Kivu del Sur."),
        ("Clima", "Ecuatorial de altitud: la meseta ronda los 1.700 m y suaviza el calor. Estación de lluvias de febrero a mayo, con inundaciones y riesgo sísmico señalados por el MAEC; en julio de 2025 hubo un terremoto de magnitud 5,1 en Rumonge."),
        ("Sanidad", "Fiebre amarilla OBLIGATORIA con certificado internacional desde el año de edad. Malaria endémica, cólera, dengue y riesgo de ébola y mpox citados por el MAEC. Sanidad pública deficiente; seguro con evacuación médica imprescindible."),
    ],
    alerts=[
        "FRONTERA CON RUANDA CERRADA desde enero de 2024 por la acusación burundesa de que Kigali apoya al grupo armado RED-Tabara. Sigue cerrada: lo confirman el Gobierno de Canadá el 9 de septiembre de 2026 y el FCDO el 21 de mayo de 2026, y una guía regional del 28 de abril de 2026 añade que no hay perspectiva de reapertura.",
        "SIN FRONTERA RUANDESA, EL PAÍS ES UN FONDO DE SACO. Para entrar desde Kigali hay que rodear por Tanzania (Rusumo y Kobero), unos 350 km adicionales y un visado tanzano de más, y salir por el mismo sitio. Con dos vehículos y un perro, el desvio pesa más que lo que se va a ver.",
        "CRISIS DE COMBUSTIBLE CRÓNICA. El 30 de abril de 2026 SOS Médias Burundi describía Buyumbura paralizada, con el litro de mercado negro entre 18.000 y 40.000 BIF frente a los 4.000 oficiales. El FCDO advierte de que no se puede dar por hecho que haya carburante.",
        "GUERRA EN EL KIVU AL OTRO LADO DE LA FRONTERA. El 15 de diciembre de 2025 el M23 afirmó haber capturado a cientos de soldados burundeses en su ofensiva congoleña; el paso de Gatumba-Kavimvira estuvo cerrado dos meses y no reabrio hasta el 23 de febrero de 2026.",
        "ZONAS DESACONSEJADAS POR EL MAEC (6-5-2026): la frontera con RD Congo, las provincias de Cibitoke y Bubanza, el Parque Nacional de Ruvubu y el Parque Nacional de Kibira. Es decir, buena parte de lo que un viajero iría a ver.",
        "EL FCDO DESACONSEJA TODO VIAJE a las comunas de Mugina, Cibitoke, Bukinyayana, Bubanza y Mpanda, a la RN5 al norte del aeropuerto, a la franja al oeste del río Rusizi y a las RN6 y RN10 al oeste de Kayanza por el Parque Nacional de Kibira.",
        "PROHIBIDO FOTOGRAFIAR instalaciones militares, puertos, edificios gubernamentales y personal uniformado; hay que pedir permiso antes de fotografiar estructuras oficiales o personas (Gobierno de Canadá, 9-9-2026). Con dos 4x4 extranjeros y cámaras a la vista, el riesgo de detención es real.",
        "NO CIRCULAR DE NOCHE. El MAEC desaconseja pernoctar fuera de núcleos urbanos después de las 18:00 y el FCDO desaconseja los desplazamientos nocturnos por carretera fuera de Buyumbura. Los controles son frecuentes y mal equipados.",
        "GRANADAS Y ATENTADOS. El FCDO señala ataques con granada frecuentes en Buyumbura y no descarta atentados terroristas; el MAEC cita la amenaza de Al Shabaab y un atentado en Buyumbura en 2024. El 31 de marzo de 2026 la explosión de un depósito de municiones en Buyumbura dejo 13 muertos y 57 heridos.",
        "PAÍS NO LIBRE. Freedom House 2026 da a Burundi 13 puntos sobre 100 y cero en medios independientes, libertad de reunión y judicatura independiente. Las relaciones homosexuales son delito, con penas de 3 meses a 2 años (FCDO).",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Buyumbura", "Llegada, trámites, mercado y paseo del lago", "~30 km · 2 días"),
        ("2 · Costa de Buyumbura", "Saga Plage y monumento Livingstone-Stanley (Mugere)", "~40 km · 1 día"),
        ("3 · Delta del Rusizi", "Buyumbura – PN Rusizi – Buyumbura (solo si se levanta el aviso)", "~40 km · 1 día"),
        ("4 · Subida al plateau", "Buyumbura – Bugarama – Gitega (RN1)", "~65 km · 1 día"),
        ("5 · Gitega y Gishora", "Museo Nacional y santuario de tambores", "~20 km · 1 día"),
        ("6 · Plateau norte", "Gitega – Kayanza – Ngozi (RN6)", "~85 km · 1 día"),
        ("7 · Lagos del norte", "Ngozi – Kirundo – lago Rwihinda", "~70 km · 1 día"),
        ("8 · Noreste", "Kirundo – Muyinga (RN6)", "~90 km · 1 día"),
        ("9 · PN Ruvubu", "Muyinga – Gisagara – interior del parque (sujeto a aviso MAEC)", "~60 km · 2 días"),
        ("10 · Bajada al este", "Muyinga – Karuzi – Gitega – Rutana", "~190 km · 1 día"),
        ("11 · Karera y Nyakazu", "Rutana – chutes de la Karera – falla de Nyakazu", "~60 km · 1 día"),
        ("12 · Extremo sur", "Rutana – Makamba – Nyanza-Lac", "~150 km · 1 día"),
        ("13 · Costa sur", "Nyanza-Lac – Rumonge (RN3)", "~70 km · 1 día"),
        ("14 · Bosque y fuente del Nilo", "Rumonge – Bururi – Rutovu (fuente del Nilo) – Buyumbura", "~200 km · 2 días"),
    ],
    offroad=[
        "La red principal (RN1 Buyumbura-Gitega, RN3 por la costa del Tanganica, RN6 Gitega-Ngozi-Muyinga) es asfalto con baches y curvas cerradas, y a 250 km/día de media una etapa larga en Burundi se come el día entero: el país mide poco pero se circula despacio.",
        "Las pistas de acceso a los PDIs naturales —Karera, Nyakazu, lago Rwihinda, reserva de Bururi, entradas de la Ruvubu— son de tierra roja lateralítica y se vuelven jabón con lluvia: en estación húmeda hay que contar con tracción, neumáticos con taco y recuperación entre los dos coches.",
        "Los parques nacionales (Rusizi, Kibira, Ruvubu) los gestiona el OBPE y exigen guía: la guía oficial de la Kibira obliga a registrarse en la oficina del parque y PROHÍBE expresamente entrar sin guía autorizado, así que no hay pista interior autoguiada (tarifas y horarios, POR CONFIRMAR con el OBPE).",
        "La Kibira está atravesada por las RN6 y RN10 entre Kayanza y Cibitoke: el FCDO desaconseja TODO viaje por esos ejes por presencia de un grupo rebelde, de modo que la pista más atractiva del país está vetada de facto.",
        "El eje RN5 Buyumbura-Gatumba-Cibitoke y toda la llanura al oeste del río Rusizi están igualmente desaconsejados por FCDO y MAEC por incursiones armadas desde RD Congo: es zona de controles militares, no de conducción recreativa.",
        "La frontera terrestre con Ruanda está CERRADA desde enero de 2024, así que no hay tránsito 4x4 por el norte: la única salida terrestre operativa es hacia Tanzania (Kobero en el noreste y los pasos del sur por Makamba), con la advertencia del FCDO sobre escasez de carburante.",
        "El combustible es el cuello de botella real del país: hay desabastecimiento recurrente, y la autonomía entre Buyumbura, Gitega y Muyinga conviene planificarla con bidones y no con la reserva del depósito.",
        "Está PROHIBIDO fotografiar instalaciones oficiales, y hay controles frecuentes: bajar la ventanilla, apagar cámaras y llevar la documentación de los dos vehículos a mano ahorra problemas en cada puesto.",
    ],
    senderismo=[
        "Senderos señalizados de la Karera —Gisuma, Bunya, Mihama y el del bosque galería—, con pasarelas y barandillas ya instaladas y guías de la oficina del OBPE en el centro de Shanga. Una a dos horas, muy resbaladizo con lluvia.",
        "Borde de la falla de Nyakazu: recorrido por el filo del acantilado de hasta 300 m sobre el valle de Kumoso, con la cascada estacional al fondo. Sin protecciones; no apto de noche ni con niebla.",
        "Ascensión al monte Kikizi (2.145 m) desde Rutovu, pasando por la pirámide de la fuente meridional del Nilo: subida suave por colinas cultivadas, media jornada.",
        "Bosque de Bururi: senderos forestales de la reserva de 33 km² hasta las cascadas del río Siguvyaye, buenos para primates y las 87 especies de aves censadas. Guía local del INECN/OBPE recomendable.",
        "Kibira, sector de Teza: seguimiento de chimpancés, circuitos ornitológicos, las cuevas de Inangurire junto a la cima del monte Teza y las fuentes termales de Ku Mahoro, siempre con guarda del parque (entrar sin guía está prohibido). HOY DESACONSEJADO por FCDO y MAEC.",
        "Orilla del lago Rwihinda: paseo llano por la ribera y los papirales para observar pelícanos y cormoranes, combinable con una vuelta en piragua a la isla de Akagwa.",
        "Colinas de té de Teza y Rwegura, en el borde de la Kibira: caminos entre plantaciones con vistas a la cresta Congo-Nilo (mismo aviso de seguridad que el parque).",
        "Paseo de la orilla del Tanganica al sur de Buyumbura, entre Saga Plage y la desembocadura del Mugere: llano y fácil, pero nunca al amanecer ni al anochecer por los hipopótamos.",
    ],
    acampada=[
        "No hay campings comerciales documentados en fuente oficial en Burundi: la información disponible procede de operadores locales y blogs, no de webs de parques.",
        "Un operador local (M Travel and Tours Burundi) ofrece acampada organizada en las plantaciones de té de Teza (Muramvya), en las chutes de la Karera (Rutana), en el Parque Nacional de la Kibira y a orillas del lago Rwihinda (Kirundo), con tiendas, guía, comidas y vigilancia nocturna, sin precios publicados.",
        "El mismo operador propone acampada en aldea (Bugarama o Gishora) conviviendo con la comunidad; es la fórmula más segura para pernoctar fuera de ciudad, porque implica permiso del jefe de colina.",
        "El documento oficial del Ministerio de Medio Ambiente sobre el este del país menciona ACAMPADA PANORÁMICA en la colina de Nyakazu, sobre los cimientos del antiguo puesto militar alemán: es el único emplazamiento de acampada citado por una fuente institucional burundesa.",
        "En los parques nacionales (Rusizi, Kibira, Ruvubu) la acampada depende del OBPE y no hay áreas señalizadas ni tarifas publicadas: hay que negociarlo en la oficina del parque. En la Kibira la guía oficial ofrece en su lugar el Kibira Park Lodge de Bugarama (28 habitaciones, hasta 40.000 francos burundeses) y casas del parque en el sector de Teza, donde el visitante lleva su propia comida.",
        "La acampada libre NO es recomendable: el MAEC desaconseja estar en la calle entre las 18:00 y las 06:00 en Buyumbura y en las capitales provinciales, y hay controles y toque de queda de facto en buena parte del país.",
        "La alternativa realista para dos 4x4 es dormir en hoteles y misiones con patio cerrado (Buyumbura, Gitega, Ngozi, Muyinga, Rumonge) y montar tienda de techo dentro del recinto, previo permiso del propietario.",
        "En la costa del Tanganica, los recintos de playa privados al sur de Buyumbura y en Rumonge suelen tener parcela vallada y vigilante: es el compromiso habitual entre acampada y seguridad.",
        "No se han encontrado registros verificables de iOverlander ni de Tracks4Africa con puntos de acampada concretos en Burundi durante esta investigación: el único listado localizado en Tracks4Africa es el de la falla de Nyakazu, sin datos de pernocta.",
    ],
    visado=[
        "OBLIGATORIO para españoles. No hay exención ni régimen especial.",
        "eVisa en el portal de la Comisaría General de Migración (migration.gov.bi). El MAEC recomienda solicitarlo con 15 días de antelación.",
        "COSTE: 90 USD un mes, 180 USD dos meses, 270 USD tres meses (Wikipedia, política de visados de Burundi). El MAEC confirma los 90 USD y la validez de un mes.",
        "A LA LLEGADA: el MAEC cita la expedición presencial en el aeropuerto de Buyumbura. La política de visados recoge también los pasos terrestres, y un relato de overlanders de marzo de 2025 documenta un visado de tránsito de 3 días por 40 USD en Kobero.",
        "Pasaporte con validez mínima durante la estancia y una página en blanco según el MAEC; el Gobierno de Canadá exige 6 meses de validez. Viajar con el criterio más estricto: 6 meses.",
        "Certificado internacional de vacunación contra la fiebre amarilla EXIGIDO en frontera, y billete de salida según Canadá. Sin fiebre amarilla no se entra.",
    ],
    fronteras_rows=[
        ("Aeropuerto", "Buyumbura - Melchior Ndadaye (BJM / HBBA)", "Único aeropuerto internacional del país y único con pista asfaltada. En obras de ampliación sino-burundesa desde agosto de 2024. Conexiones históricas con Adis Abeba, Nairobi, Entebbe, Kigali, Dar es Salaam y Bruselas. Punto de entrada citado para mascotas."),
        ("Frontera terrestre", "Kanyaru Haut / Akanyaru (RN1, hacia Butare y Kigali)", "CERRADO. Burundi cerró la frontera con Ruanda en enero de 2024 y sigue cerrada según el Gobierno de Canadá (9-9-2026) y el FCDO (21-5-2026). No hay fecha de reapertura."),
        ("Frontera terrestre", "Gasenyi / Nemba (hacia Kirundo y Kigali)", "CERRADO. Mismo cierre de enero de 2024. Una guía regional del 28 de abril de 2026 señala que no hay perspectiva de reapertura a corto plazo."),
        ("Frontera terrestre", "Ruhwa / Rusizi I (RN5, Cyangugu-Bukavu hacia Buyumbura)", "CERRADO. Es el paso más cómodo entre ambos países en condiciones normales, pero una agencia regional confirmaba el 31 de mayo de 2025 que la frontera terrestre Ruanda-Burundi sigue cerrada tanto para ciudadanos como para turistas extranjeros. Además discurre por la franja oeste que el FCDO desaconseja por completo."),
        ("Frontera terrestre", "Kobero - Kabanga (Tanzania, RN6, eje de carga a Dar es Salaam)", "ABIERTO y operativo. El FCDO (21-5-2026) dice que la frontera con Tanzania funciona con normalidad, aunque el transporte se resiente de la escasez de combustible. Relato de marzo de 2025: 3 horas de trámites, CPD sellado por ambas aduanas, control de fiebre amarilla y asfalto 200 m después del puesto."),
        ("Frontera terrestre", "Mugina (Makamba) hacia Tanzania / eje de Kigoma", "POR CONFIRMAR. No se ha encontrado fuente fechada sobre su estado ni sobre si admite extranjeros con vehículo propio. Ojo: hay otra Mugina en Cibitoke, que el FCDO incluye entre las comunas a las que desaconseja todo viaje."),
        ("Frontera terrestre", "Gatumba - Kavimvira (RD Congo, hacia Uvira)", "REABIERTO el 23 de febrero de 2026 tras dos meses cerrado por la ofensiva del M23 en Kivu del Sur. El Gobierno de Canadá avisa de que puede volver a cerrarse sin previo aviso y el MAEC desaconseja toda la franja fronteriza con RD Congo."),
        ("Puerto lacustre", "Puerto de Buyumbura (lago Tanganica)", "Mayor puerto del lago y vía del 80% del comercio exterior del país; modernización al 98% en mayo de 2024, con terminal de contenedores. Enlaza con Kigoma (Tanzania), Kalemie (RD Congo) y Mpulungu (Zambia). Servicio regular de pasajeros y, sobre todo, transbordo de VEHÍCULOS: POR CONFIRMAR."),
    ],
    vehiculos=[
        "Se conduce por la DERECHA. Permiso de conducción internacional recomendable junto al español; ninguna fuente abierta en esta sesión lo detalla para Burundi.",
        "Importación temporal del vehículo en el propio puesto fronterizo. El relato de Kobero (marzo de 2025) describe el sellado del carnet de passages por las aduanas de Tanzania y de Burundi, junto a un certificado sanitario gratuito y la comprobación del certificado de fiebre amarilla.",
        "CARNET DE PASSAGES: recomendable llevarlo. Se acepta y se sella, pero ninguna fuente oficial abierta lo declara obligatorio, así que conviene contar también con el trámite alternativo de admisión temporal en ventanilla.",
        "No hay entidad emisora de CPD dentro de Burundi (carnetdepassage.org): el carnet hay que sacarlo antes en España, vía RACE, y encajar Burundi en la lista de países del documento.",
        "SEGURO: la Carta Verde europea gestionada por OFESAUTO no cubre Burundi. Burundi es estado miembro del COMESA, cuyo sistema de tarjeta amarilla (Yellow Card) cubre responsabilidad civil transfronteriza; precio, ventanilla y validez para matrículas europeas, POR CONFIRMAR.",
        "Carreteras: la mayoría sin asfaltar y mal mantenidas, con accidentes graves frecuentes según el FCDO. La estacion de lluvias de febrero a mayo empeora firmes y pasos. El eje asfaltado útil es la RN6 Kobero-Muyinga-Gitega-Buyumbura.",
        "PROHIBIDO circular de noche fuera de Buyumbura (FCDO) y pernoctar fuera de núcleos urbanos pasadas las 18:00 (MAEC). Planificar etapas cortas: la media de 250 km/día del proyecto es aquí optimista.",
        "Prohibido desde agosto de 2019 introducir bolsas de plástico en el equipaje y, por extensión, en el vehículo (MAEC). Revisar bodegas y organizadores antes de llegar a la aduana.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autoridad competente: Autorité de l'Aviation Civile du Burundi (AACB / BCAA), aacb.gov.bi. La web histórica aacb.bi aparece caída en la ficha de drone-laws.com.",
        "Clases por peso: Clase 1 hasta 5 kg, Clase 2 de 5 a 25 kg, Clase 3 más de 25 kg, y categorías por uso recreativo, privado o comercial. REGISTRO OBLIGATORIO incluso para turistas.",
        "Límites operativos: solo de día y en condiciones visuales, siempre en línea de vista, techo de 300 pies en uso recreativo sin autorización expresa, prohibido sobrevolar multitudes y prohibido operar a menos de 10 km de un aeródromo.",
        "Prohibición penal separada y más relevante: nada de fotografiar instalaciones militares, puertos, edificios gubernamentales ni personal uniformado (Gobierno de Canadá, 9-9-2026).",
        "Recomendación operativa: no llevar el dron a Burundi. Si se lleva, declararlo en aduana y no sacarlo de la caja sin autorización escrita de la AACB. Procedimiento exacto de registro y tasas, POR CONFIRMAR.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Starlink figura como servicio activo en Burundi en el recuento de junio de 2026 de tech.africa, dentro de los 26 países africanos operativos.",
        "La autorización se tramitó en 2024; tarifas locales y disponibilidad de kits en Buyumbura, POR CONFIRMAR (no se han abierto precios de Burundi en esta sesión).",
        "Uso de terminal extranjera en Roam y trato aduanero de la antena al entrar por Kobero: POR CONFIRMAR. En países vecinos ha habido incidencias con antenas declaradas como equipo de telecomunicaciones.",
        "Alternativa móvil: SIM local Lumitel, documentada por overlanders en marzo de 2025 a 20.000 BIF la tarjeta y 23.000 BIF el paquete de 7 GB por semana. Operadores principales: Lumitel, Econet Leo y Onatel/Onamob (verificar oferta actual).",
    ],
    perro_intro=[
        "ENTRADA: PetTravel resume microchip ISO 11784/11785 de 15 dígitos, vacuna antirrábica aplicada al menos 30 días antes de la llegada para animales mayores de tres meses, certificado sanitario original de veterinario colegiado y endoso por el servicio veterinario oficial del país de origen.",
        "PERMISO PREVIO DE IMPORTACIÓN expedido por el Ministerio de Medio Ambiente, Agricultura y Ganadería (MINEAGRIE). Su web oficial, mineagrie.gov.bi, existe pero está EN CONSTRUCCIÓN y solo ofrece el correo genérico info@mineagri.gov.bi: no hay formulario, plazo ni tasa publicados. Es el mayor agujero de esta ficha.",
        "RAZAS: Burundi no publica lista de razas prohibidas. Si están vetados los híbridos de lobo y los felinos híbridos con menos de cinco generaciones de separación.",
        "PUNTO DE ENTRADA: la única vía documentada para mascotas es el aeropuerto de Buyumbura. Entrar con el perro por Kobero en vehículo propio no está documentado en ninguna fuente abierta: POR CONFIRMAR con la aduana y con el servicio veterinario.",
        "VUELTA A LA UE: Burundi NO figura en las listas del Reglamento de Ejecución (UE) 2026/636, aplicable desde el 22 de abril de 2026 (el único país africano listado es Mauricio). Se aplica por tanto la vía de tercer país no listado del Reglamento Delegado (UE) 2026/131: microchip, primovacunación antirrábica completa al menos 21 días antes, TITULACIÓN DE ANTICUERPOS ANTIRRÁBICOS válida y certificado zoosanitario, con entrada obligatoria por un punto de entrada de viajeros designado.",
        "La titulación hay que tenerla hecha y anotada ANTES de salir de la UE, en laboratorio autorizado; si caduca la vacuna, caduca todo. El certificado zoosanitario vale seis meses desde los controles fronterizos o hasta que expire la vacunación antirrábica, lo que ocurra antes.",
        "VETERINARIOS: no se ha localizado en esta sesión ninguna clínica veterinaria de referencia en Buyumbura con fuente fiable. Riesgos para el perro: rabia endémica, garrapatas, calor y altitud moderada, y la escasez de agua potable y de combustible para mantener el vehículo climatizado.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "FIEBRE AMARILLA OBLIGATORIA con certificado internacional de vacunación, exigible desde el año de edad (MAEC, 6-5-2026) y comprobada en frontera según el relato de Kobero de marzo de 2025.",
        "Altamente recomendadas por el MAEC: difteria, tétanos, poliomielitis, hepatitis A, fiebre tifoidea y cólera. Recomendadas: tuberculosis, hepatitis B, rabia y meningitis.",
        "MALARIA ENDÉMICA en todo el país: profilaxis obligatoria en la práctica, repelente y mosquitera. El MAEC cita además cólera, dengue, virus Zika, difteria y riesgo de ébola y viruela del mono.",
        "En enero de 2026 murieron más de 25 refugiados congoleños en un brote de cólera en Burundi, y en marzo de 2026 se notificó un brote de enfermedad no identificada en el distrito de Mpanda con cinco muertos y 35 casos.",
        "Servicios sanitarios deficientes según el MAEC y por debajo del estándar occidental según Canadá. La referencia privada es el Kira Hospital de Kinindo (Buyumbura), con 130 camas y 14 servicios, aunque su gestión se deterioro tras la intervención estatal de 2022.",
        "SEGURO DE VIAJE CON EVACUACIÓN MÉDICA IMPRESCINDIBLE: el MAEC insiste en contratar la mayor cobertura posible y Canadá considera esencial la cobertura de evacuación. La evacuación realista es a Nairobi o Kigali, y Kigali implica frontera cerrada: contarlo por vía aérea.",
        "Agua no potable: no beber del grifo, ni con hielo. Riesgo sísmico y de inundaciones entre febrero y mayo señalado por el MAEC.",
    ],
    seguridad_intro="Burundi es un país no libre en crisis desde 2015: Freedom House le da 13 puntos sobre 100 en 2026, con cero en medios independientes, libertad de reunión y judicatura. Sobre ese fondo se superponen los ataques con granada en Buyumbura, la presión del conflicto del Kivu en toda la franja occidental y la actividad de RED-Tabara desde Kivu del Sur. España no tiene embajada residente. Para dos 4x4 extranjeros, el riesgo dominante no es el atentado, sino el control policial, la sospecha por una cámara y no poder repostar.",
    seguridad=[
        "ZONAS QUE EL MAEC DESACONSEJA (6-5-2026): la frontera con RD Congo, las provincias de Cibitoke y Bubanza, el Parque Nacional de Ruvubu y el Parque Nacional de Kibira. Además, no pernoctar fuera de núcleos urbanos después de las 18:00.",
        "ZONAS A LAS QUE EL FCDO DESACONSEJA TODO VIAJE (21-5-2026): comunas de Mugina, Cibitoke, Bukinyayana, Bubanza y Mpanda; la RN5 al norte del aeropuerto Melchior Ndadaye y la franja al oeste del río Rusizi; y las RN6 y RN10 al oeste de Kayanza a través del Parque Nacional de Kibira.",
        "EL GOBIERNO DE CANADÁ (9-9-2026) pide evitar todo viaje no esencial al país y evitar por completo Cibitoke, Bubanza y la RN5 y su oeste en Bujumbura Rural, por enfrentamientos militares y actividad de grupos armados.",
        "GRANADAS: el FCDO describe ataques con granada frecuentes, sobre todo en Buyumbura. El 31 de marzo de 2026 la explosión de un depósito de municiones militar en Buyumbura causó 13 muertos y 57 heridos, atribuida oficialmente a un cortocircuito.",
        "CONFLICTO REGIONAL: el ejército burundés está desplegado en RD Congo contra el M23; el 15 de diciembre de 2025 el M23 afirmó haber capturado a cientos de soldados burundeses, y en enero de 2026 ocho personas fueron acusadas de espiar para el M23. Ser extranjero con cámaras en la franja oeste es mala idea.",
        "DELINCUENCIA COMÚN ALTA: atracos, robos de vehículo con violencia y asaltos a domicilios. El FCDO recomienda no andar por la calle ni usar transporte público después del anochecer; el MAEC describe a la policía como poco disciplinada, ineficaz y mal equipada.",
        "PROHIBICIONES QUE ACABAN EN COMISARÍA: fotografiar instalaciones militares, puertos, edificios oficiales o uniformados. Pedir permiso antes de fotografiar a cualquier persona o edificio publico.",
        "LEGISLACIÓN: las relaciones homosexuales son delito, con penas de 3 meses a 2 años de prisión, en una sociedad socialmente conservadora (FCDO). Las penas por drogas incluyen largas condenas de cárcel.",
        "CONSULAR: la embajada competente esta en Dar es Salaam (Tanzania) y en Buyumbura solo hay Consulado Honorario. La asistencia sobre el terreno será limitada y lenta.",
    ],
    agua=[
        "El agua corriente no es potable: no beber del grifo ni tomar hielo. Para boca, agua embotellada o filtrada y potabilizada a bordo.",
        "Para llenar depósitos de ducha y lavado, la red urbana de Buyumbura y Gitega es la única razonablemente fiable; fuera de ellas el suministro es intermitente.",
        "El suministro urbano no es constante ni siquiera en instalaciones críticas: un informe de 2022 sobre la Clinique Prince Louis Rwagasore, en pleno centro de Buyumbura, citaba la disponibilidad irregular de agua entre sus problemas estructurales.",
        "Lago Tanganica: agua abundante pero con riesgo de esquistosomiasis y contaminación portuaria. Servir solo para lavado exterior y nunca para ducha sin tratar.",
        "Estrategia recomendada: entrar desde Tanzania con los depósitos llenos y rellenar solo en hoteles o recintos de Buyumbura y Gitega, con filtro y cloración. Puntos concretos de llenado verificados, POR CONFIRMAR.",
    ],
    combustible=[
        "PRECIO OFICIAL: gasolina 95 a 4.000 BIF por litro, equivalente a unos 1,35 USD, en el dato de GlobalPetrolPrices del 9 de febrero de 2026. El problema no es el precio sino que no haya.",
        "MERCADO NEGRO: el 30 de abril de 2026 SOS Médias Burundi documentaba el litro entre 18.000 y 40.000 BIF, de 4,5 a 10 veces el precio oficial, con los autobuses de Buyumbura inmovilizados en las gasolineras.",
        "CRISIS CRÓNICA: el mismo medio habla de una crisis de carburante de más de cinco años, agravada en 2026 por las tensiones energeticas internacionales. El FCDO advierte de que la escasez es severa y de que no se puede dar por hecho que haya combustible.",
        "DIESEL: el relato de overlanders de marzo de 2025 en Kobero ya registraba escasez de diesel en Burundi, y la referencia de repostaje era el lado tanzano (Ngara Oil a 3.069 TZS por litro).",
        "REGLA OPERATIVA: entrar con autonomía completa de ida y vuelta desde Tanzania, jerricanes llenos incluidos, y no contar con repostar dentro del país. Con dos vehículos y una media de 250 km/día, eso significa reservar unos 800-1.000 km de autonomía real.",
        "Calidad del carburante y disponibilidad de diesel de bajo azufre, POR CONFIRMAR. Racionamiento formal por matrícula o cupo, POR CONFIRMAR.",
    ],
    experiencias_intro="Hay muy pocos relatos recientes de overlanders en Burundi: el cierre de la frontera ruandesa en 2024, la guerra del Kivu y la escasez de combustible han vaciado la ruta. Estos son los testimonios y fuentes fechadas que se han podido abrir en esta sesión, con su año.",
    experiencias=[
        "Kobero en tres horas, con CPD y fiebre amarilla: el blog Live The Life Expeditions (dinotruck.com) describe su paso de Kabanga (Tanzania) a Muyinga el 5 de marzo de 2025. Tres horas de trámites por afluencia, certificado sanitario gratuito, comprobación del certificado de fiebre amarilla, sellado del carnet de passages por ambas aduanas y asfalto 200 metros después del puesto. Coordenadas del aparcamiento: 2,646602 S / 30,459020 E.",
        "Cuarenta dólares por tres días: el mismo relato de marzo de 2025 documenta que el visado se expidio en el propio paso de Kobero, 40 USD para tres días de tránsito, con un cambio de 2.948 BIF por dólar. Es la prueba práctica de que la vía a la llegada funciona en frontera terrestre, aunque el MAEC solo mencione el aeropuerto.",
        "Cambistas agresivos y catorce dólares de propinas: en Kobero, marzo de 2025, los viajeros de dinotruck.com tuvieron que pedir ayuda a la policía para quitarse de encima a los cambistas informales y a los vendedores de SIM, y contabilizaron unos 14 USD en pagos no oficiales a policías e intermediarios. Presupuestar propinas y no cambiar dinero en el puesto.",
        "Diesel escaso ya en 2025: el mismo equipo repostó en el lado tanzano, en Ngara Oil a 3.069 chelines por litro, precisamente porque en Burundi había escasez de diesel en marzo de 2025. La regla de entrar lleno desde Tanzania no es una precaución teórica: es lo que hizo el último overlander documentado.",
        "SIM Lumitel a 20.000 francos: el relato de marzo de 2025 detalla la compra de SIM Lumitel por 20.000 BIF y un paquete de 7 GB semanales por 23.000 BIF. Útil como referencia de precio y para saber que hay conectividad móvil razonable en el corredor Kobero-Buyumbura.",
        "Bujumbura paralizada, abril de 2026: SOS Médias Burundi contó el 30 de abril de 2026 como la escasez de combustible dejo los autobuses inmovilizados en las gasolineras desde el fin de semana anterior, con vecinos caminando kilómetros y taxis pasando de 600 a 5.000 francos por trayecto. No es un relato de viajero, pero describe el escenario real al que llegaría la expedición.",
        "Frontera ruandesa sin horizonte: una guía regional de autocaravanas y 4x4 (4x4uganda.com) actualizaba el 28 de abril de 2026 el estado de la frontera Burundi-Ruanda y concluía que sigue cerrada desde 2024, que no hay perspectiva clara de reapertura y que la alternativa es volar o conducir a través de Tanzania, cuyo lado está abierto con ambos países.",
        "El cierre visto desde el terreno: SOS Médias Burundi publicó en julio de 2025 un reportaje sobre el viaje de Burundi a Ruanda convertido en travesía clandestina y peligrosa por el cierre, y en marzo de 2024 otro en el que la reapertura no se veía próxima. Sirve para calibrar que el cierre no es administrativo, sino político y duradero.",
        "Gatumba reabierto tras el M23: el 23 de febrero de 2026 el paso de Kavimvira, frente a Gatumba, volvió a abrirse después de dos meses cerrado por la ofensiva del M23 en Kivu del Sur. Es la única frontera congoleña operativa y la más volátil: el Gobierno de Canadá avisa de que puede cerrarse sin aviso.",
        "El rodeo de 347 kilómetros: Eco Adventure Safaris confirmaba el 31 de mayo de 2025 que la frontera terrestre Ruanda-Burundi sigue cerrada para ciudadanos y turistas, y detallaba el único itinerario viable: Kigali-Rusumo 167 km en unas 4 horas, Rusumo-Kobero 56 km en una hora y Kobero-Gitega 124 km en tres horas, con visado tanzano de 100 USD y burundés de 40 USD por encima del presupuesto previsto.",
    ],
    pendientes=[
        ("Reapertura de la frontera con Ruanda", "Comunicado oficial del Gobierno de Burundi o de la EAC, o actualización del MAEC/FCDO/Canadá que diga que los pasos de Kanyaru Haut y Gasenyi están abiertos a extranjeros con vehículo."),
        ("Seguro obligatorio y Carte Jaune COMESA", "Confirmar en ycmis.comesa.int o con una aseguradora burundesa el precio, la ventanilla en Kobero y si cubre matrículas europeas; alternativa, seguro local de frontera."),
        ("Obligatoriedad real del CPD", "Respuesta escrita de la Oficina Burundesa de Ingresos (OBR) o del RACE, o dos relatos de overlanders posteriores a 2024 que describan el trámite sin carnet."),
        ("Permiso de importación del perro (MINEAGRIE)", "La web oficial mineagrie.gov.bi está en construcción: escribir a info@mineagri.gov.bi y al Consulado Honorario de España en Buyumbura y obtener por escrito el impreso, el plazo y la tasa."),
        ("Entrada del perro por paso terrestre", "Confirmación escrita del servicio veterinario burundés de que Kobero admite mascotas, o relato documentado de un overlander con animal."),
        ("Estado del paso de Mugina (Makamba) hacia Tanzania", "Fuente fechada de 2025-2026 que diga si está abierto a extranjeros con vehículo propio y a que horario."),
        ("Transbordo de vehículos Buyumbura-Kigoma", "Confirmar con ARNOLAC/BATRALAC o con el puerto si existe servicio que admita 4x4 particulares y a que precio."),
        ("Toque de queda", "Verificar si hay toque de queda formal vigente en 2026: ninguna de las fuentes abiertas en esta sesión lo menciona; solo restricciones de facto de circulación nocturna."),
        ("Precio y disponibilidad de Starlink en Burundi", "Mapa oficial de starlink.com o tarifa local publicada, y régimen de Roam para terminales extranjeras."),
        ("Registro de drones ante la AACB", "Abrir el reglamento RAB 06 en aacb.gov.bi y confirmar impreso, tasa y plazo para visitantes."),
        ("Clínica veterinaria de referencia en Buyumbura", "Nombre, dirección y teléfono verificados de al menos una clínica que atienda perros de expatriados."),
        ("Puntos fiables de agua y combustible", "Entradas de iOverlander o Tracks4África posteriores a 2024 con gasolineras y puntos de agua operativos en el eje Kobero-Gitega-Buyumbura."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las páginas efectivamente abiertas en esa fecha; cada dato remite a la fuente y a su fecha de actualización. Las recomendaciones oficiales cambian sin aviso en un país con conflicto fronterizo activo: reverificar MAEC, FCDO y Gobierno de Canadá antes de cualquier decisión. Esto es una herramienta de planificación, no una autorización de viaje ni un asesoramiento jurídico o sanitario.",
    emergency="Emergencia consular de España, vía Embajada en Dar es Salaam, acreditada ante Burundi: +255 754 042 123. Centralita +255 22 266 6018 / 6019 / 266 6936, emb.daressalaam@maec.es. Consulado Honorario en Buyumbura: +257 76 71 58 25 y +257 79 51 80 50. Números locales verificados por el MAEC el 6 de mayo de 2026: policía 117, ambulancia 112, bomberos 118. Fuera de Buyumbura la respuesta es lenta: el teléfono útil de verdad es el del seguro con evacuación médica.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

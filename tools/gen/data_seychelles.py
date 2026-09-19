# -*- coding: utf-8 -*-
"""Seychelles — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Seychelles está FUERA DE LA RUTA PREVISTA por ser insular: 115 islas a 1.500 km de la costa africana, sin conexión terrestre ni travesía de vehículos. La app solo tiene un stub: créala entera con el formato del piloto de Túnez. Es uno de los países más seguros y con mayor renta per cápita de África, con alternancia democrática desde 2020 — decirlo con claridad es parte de la ficha. Claves que DECIDEN la ficha y hay que documentar con fuente fechada: no hace falta visado para ninguna nacionalidad, pero SÍ una Autorización de Viaje (Seychelles Travel Authorisation) previa y de pago — verifica importe y vigencia; hay DOS bienes del Patrimonio Mundial, el atolón de Aldabra y el Valle de Mai de Praslin, y el primero solo se alcanza en expedición marítima con permiso de la Seychelles Islands Foundation; casi la mitad del territorio es área protegida. Ordena los PDIs por isla (Mahé, Praslin, La Digue y las exteriores) para que se entienda.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/seychelles.json y audit/pdi/seychelles.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Victoria (Mahé) · la capital y su mercado", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=-4.6213393, lon=55.4513226,  # Google Maps: Sir Selwyn Selwyn-Clarke Market
        desc="Victoria concentra en unas pocas manzanas todo el aparato de un Estado: puerto, ministerios, catedral y la torre del reloj plateada de 1903, copia del Little Ben londinense. El mercado Sir Selwyn Selwyn-Clarke es el corazón del barrio: pescado, fruta, especias y ruido criollo desde primera hora. Con unos 30.000 habitantes, alrededor del 30 % del país, figura entre LAS CAPITALES MÁS PEQUEÑAS DEL MUNDO; el título de «la más pequeña de África» es de uso turístico y no lo hemos podido certificar. Aparcar en el centro es complicado entre semana: mejor dejar los coches en la zona del puerto.",
        dog_note="Calles y paseo marítimo sí, con correa; el mercado cubierto y el museo, no.",
        visit={
            "why": "Es la única ciudad del país y el punto donde se resuelven trámites, dinero, SIM y billetes de ferry. También es la puerta de entrada al mercado y a la cocina criolla.",
            "see": "Torre del reloj, mercado cubierto, catedral de la Inmaculada Concepción, templo hindú Arulmigu Navasakti Vinayagar y el Inter Island Quay.",
            "access": "Carretera asfaltada desde el aeropuerto (unos 10 km, vía rápida con límite de 80 km/h). Aparcamiento en superficie junto al puerto y en Palm Street; calles estrechas y sentido único en el casco. El pin marca la entrada del mercado, en Market Street.",
            "when": "De lunes a sábado por la mañana temprano, cuando el mercado de pescado está en plena faena; los domingos la ciudad está cerrada.",
            "skip": "Si el viaje es corto y sólo interesan playas y bosque, basta con cruzarla camino del ferry.",
        },
        links=[
            {"label": "Victoria (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Victoria,_Seychelles"},
            {"label": "Seychelles Electronic Border System (oficial)", "url": "https://seychelles.govtas.com/en"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Market_Street_Victoria_Seychelles.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Market_Street_Victoria_Seychelles.jpg",
                "credit": "Henning Leweke · CC BY-SA 2.0",
                "caption": "La calle del mercado de Victoria.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fish_Mongers_Victoria_Market_Seychelles.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fish_Mongers_Victoria_Market_Seychelles.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "Pescaderos en el mercado de Victoria.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Market_in_Victoria,_Mahe_Island,_Seychelles_-_6301879058.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Market_in_Victoria,_Mahe_Island,_Seychelles_-_6301879058.jpg",
                "credit": "Fabio Achilli · CC BY 2.0",
                "caption": "El mercado Selwyn-Clarke.",
            },
        ],
    ),
    dict(
        n=2, name="Jardín Botánico Nacional y Parque Nacional del Morne Seychellois", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1 día",
        lat=-4.63074, lon=55.45299,  # Google Maps: Jardín Botánico Nacional y Parque Nacional del Morne Seychellois (sin objeto en Google Maps; coordenada de la fuente)
        desc="A diez minutos a pie del mercado, el Jardín Botánico Nacional, fundado en 1901 por el agrónomo mauriciano Paul Rivalz Dupont, reúne en 6 hectáreas más del 60 % de las plantas con flor endémicas de las islas graníticas. Detrás se levanta el Parque Nacional del Morne Seychellois: 3.045 hectáreas, MÁS DEL 20 % DE MAHÉ, con el pico Morne Seychellois (905 m) y más de 15 km de senderos señalizados. Los senderos cierran a las 16:00 y el del Morne Seychellois sólo abre de 8:00 a 12:00.",
        dog_note="Jardín botánico con tortugas gigantes en libertad y parque nacional: perros vetados.",
        visit={
            "why": "Es la forma más rápida de ver coco de mar, tortugas gigantes de Aldabra y palmeras endémicas sin salir de Mahé, y el arranque de todas las rutas de montaña del país.",
            "see": "Arboreto, centro de biodiversidad, colonia de zorros voladores y, ya en el parque, los senderos de Copolia, Morne Blanc, Trois Frères, Anse Major y Mare aux Cochons.",
            "access": "Asfalto hasta la verja del jardín en Mont Fleuri Road, con aparcamiento propio suficiente para dos 4x4. Tasas SPGA/SNPA para no residentes mayores de 12 años: Copolia 100 SCR, Trois Frères 150 SCR, Anse Major 150 SCR, Morne Seychellois 250 SCR; residentes gratis. Parque abierto 8:00–16:00. El pin marca la entrada del jardín botánico.",
            "when": "Primera hora de la mañana; en los senderos altos, de mayo a septiembre el terreno está más seco.",
            "skip": "Con lluvia fuerte, las rocas graníticas de Copolia y Trois Frères se vuelven resbaladizas y no compensa.",
        },
        links=[
            {"label": "Seychelles Parks and Gardens Authority · información al visitante", "url": "https://www.spga.gov.sc/visitor-information"},
            {"label": "Parque Nacional del Morne Seychellois (SPGA)", "url": "https://www.spga.gov.sc/parks/morne-seychellois"},
            {"label": "Jardín Botánico Nacional (Wikipedia)", "url": "https://en.wikipedia.org/wiki/National_Botanical_Garden_of_Seychelles"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Botanical_Gardens_Victoria_Seychelles_(32664948700).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Botanical_Gardens_Victoria_Seychelles_(32664948700).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "El Jardín Botánico Nacional.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pandanus_sechellarum_-_Seychelles_Botanical_Garden_1a.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pandanus_sechellarum_-_Seychelles_Botanical_Garden_1a.jpg",
                "credit": "S Molteno · CC BY-SA 4.0",
                "caption": "Pandanus endémico en el jardín botánico.",
            },
        ],
    ),
    dict(
        n=3, name="Beau Vallon y la costa norte de Mahé", cat="Costa", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=-4.615603, lon=55.4228491,  # Google Maps: Beau Vallon Beach
        desc="Beau Vallon es la bahía más frecuentada de Mahé: tres kilómetros de arena en la costa noroeste, con hoteles, buceo y el mercado de pescado de los miércoles. Desde el extremo oeste, en Bel Ombre, arranca el sendero de Anse Major, la única vía de acceso a esa cala. Ojo con el mar: el FCDO británico avisa de que la COSTA OESTE es peligrosa durante el monzón del noroeste, de diciembre a marzo, con corrientes de resaca y casi ningún socorrista. También es una de las zonas donde más se denuncian robos de oportunidad.",
        dog_note="Playa pública sin veto conocido, pero es la más concurrida de la isla: correa y horas tranquilas.",
        visit={
            "why": "Base logística barata del norte de Mahé, con supermercados, buceo, gasolinera y salida de barcos a Silhouette y a los parques marinos.",
            "see": "La ensenada completa desde Glacis hasta Bel Ombre, el puerto pesquero de Bel Ombre y la puesta de sol sobre Silhouette.",
            "access": "Carretera asfaltada desde Victoria por Glacis o por la cuesta de Bel Air, unos 25 km de curvas cerradas. Aparcamiento público junto a la playa, holgado para dos 4x4. Estado de seguridad: delincuencia no violenta pero real (robos y allanamientos); el FCDO cita expresamente Beau Vallon. El pin marca el aparcamiento público del centro de la playa.",
            "when": "De mayo a septiembre, con el alisio del sureste, el agua en la costa norte está más calmada; de diciembre a marzo, oleaje.",
            "skip": "Si se busca playa vacía, aquí no la hay: hay que irse al sur de la isla.",
        },
        links=[
            {"label": "Beau Vallon (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Beau_Vallon,_Seychelles"},
            {"label": "FCDO · Seychelles, seguridad", "url": "https://www.gov.uk/foreign-travel-advice/seychelles/safety-and-security"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Beau_Vallon_beach_Mahe_Seychelles.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Beau_Vallon_beach_Mahe_Seychelles.jpg",
                "credit": "Dino Sassi / Marcel Fayon · Public domain",
                "caption": "La playa de Beau Vallon.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Aerial_of_Beau_Vallon_Mahe,_Seychelles_(38911468714).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Aerial_of_Beau_Vallon_Mahe,_Seychelles_(38911468714).jpg",
                "credit": "dronepicr · CC BY 2.0",
                "caption": "Beau Vallon desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Poissons_grill%C3%A9s_au_Bazar_Labrin_chaque_mercredi_soir_%C3%A0_Beau_Vallon_sur_l'%C3%AEle_de_Mah%C3%A9.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Poissons_grill%C3%A9s_au_Bazar_Labrin_chaque_mercredi_soir_%C3%A0_Beau_Vallon_sur_l'%C3%AEle_de_Mah%C3%A9.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "El bazar Labrin de los miércoles.",
            },
        ],
    ),
    dict(
        n=4, name="Anse Intendance y Anse Takamaka · el sur de Mahé", cat="Costa", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=-4.7840006, lon=55.4992692,  # Google Maps: Anse Intendance
        desc="El sur de Mahé cambia de registro: playas abiertas al oleaje, sin arrecife delante y casi sin construcción. Anse Intendance mide 1,2 km, está gestionada por la Seychelles National Parks Authority y es un sitio de puesta importante de TORTUGA CAREY entre el 1 de septiembre y el 31 de marzo. Anse Takamaka, unos kilómetros al este, es algo más abrigada y tiene chiringuito. El acceso a Intendance es una pista de hormigón de 1,7 km desde la comisaría de Quatre Bornes; el baño es peligroso cuando hay mar de fondo.",
        dog_note="Playa de nidificación de tortuga carey entre septiembre y marzo: mejor dejar el perro fuera.",
        visit={
            "why": "Es la cara salvaje de Mahé y la mejor oportunidad de ver rastros de tortuga marina sin salir de la isla principal.",
            "see": "Arena gruesa, bosque de takamaka, rompientes y, en temporada, huellas y nidos señalizados de tortuga carey.",
            "access": "Asfalto por la South Coast Road o la Grand Anse Road hasta Quatre Bornes y luego 1,7 km de hormigón hasta la playa; sin problema para dos 4x4, aparcamiento informal junto al arenal. Sin taquilla ni entrada. El pin marca el desvío del camino de acceso desde Quatre Bornes.",
            "when": "De mayo a septiembre el sureste levanta oleaje fuerte; la mejor luz y el mar más manejable, de octubre a abril y a primera hora.",
            "skip": "Con bandera de resaca o mar de fondo, mirar y no bañarse; si se viaja con niños, mejor Anse Royale.",
        },
        links=[
            {"label": "Anse Intendance (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Anse_Intendance"},
            {"label": "Takamaka, Seychelles (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Takamaka,_Seychelles"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Anse_Intendance.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Anse_Intendance.jpg",
                "credit": "Didi0032 · CC BY-SA 3.0",
                "caption": "Anse Intendance, en el sur de Mahé.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Anse_Intendance_Mahe_(39589914582).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Anse_Intendance_Mahe_(39589914582).jpg",
                "credit": "dronepicr · CC BY 2.0",
                "caption": "El oleaje de Anse Intendance.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Strand_Anse_Intendance_Mahe_Luftbild_(27842316439).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Strand_Anse_Intendance_Mahe_Luftbild_(27842316439).jpg",
                "credit": "dronepicr · CC BY 2.0",
                "caption": "Anse Intendance desde el aire.",
            },
        ],
    ),
    dict(
        n=5, name="Mission Lodge · ruinas de Venn's Town", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=-4.65526, lon=55.44427,  # Google Maps: Mission Lodge (sin objeto en Google Maps; coordenada de la fuente)
        desc="En lo alto de la carretera de Sans Souci, a 450 m, quedan los cimientos de la escuela que la Church Missionary Society abrió para los hijos de africanos liberados de los buques negreros: el primer grupo, 252 personas, desembarcó del HMS Lyra el 14 de mayo de 1861 y el centro funcionó hasta 1889. Sobreviven las trazas de cinco edificios sobre 540 m² y el cementerio. Seychelles lo inscribió en la LISTA INDICATIVA de la UNESCO el 1 de febrero de 2013. La plataforma-mirador domine todo el oeste de Mahé.",
        dog_note="Sitio arqueológico dentro del parque nacional y candidato a Patrimonio Mundial: mejor sin perro.",
        visit={
            "why": "Es el lugar de memoria de la abolición en Seychelles y, de paso, el mejor mirador de la isla, con el océano al oeste y la selva debajo.",
            "see": "Cimientos de los dormitorios y el lavadero con sus 19 celdillas, el cementerio de los niños y la plataforma panorámica moderna.",
            "access": "Asfalto por la Sans Souci Road (Victoria–Port Glaud) y un desvío corto, estrecho y empinado señalizado a la derecha; aparcamiento pequeño pero suficiente para dos vehículos. Dentro del Parque Nacional del Morne Seychellois, horario general 8:00–16:00. No hemos podido confirmar si se cobra entrada (por confirmar). El pin marca el mirador.",
            "when": "Media mañana, antes de que suba la nube baja que tapa el valle.",
            "skip": "Con niebla o lluvia cerrada no se ve nada y las ruinas son escuetas.",
        },
        links=[
            {"label": "UNESCO · Mission Ruins of Venn's Town (lista indicativa)", "url": "https://whc.unesco.org/en/tentativelists/5796/"},
            {"label": "Seychelles Heritage Foundation", "url": "https://www.seyheritage.sc/heritage-sites/venns-town-mission-ruins"},
            {"label": "Mission Ruins of Venn's Town (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Mission_Ruins_of_Venn%27s_Town"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/View_from_Mission_Lodge_Lookout,_Mah%C3%A9,_Seychelles.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:View_from_Mission_Lodge_Lookout,_Mah%C3%A9,_Seychelles.jpg",
                "credit": "cotterillmike · CC0",
                "caption": "La vista desde el mirador de Mission Lodge.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Venn's_Town_lookout_Seychelles.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Venn's_Town_lookout_Seychelles.jpg",
                "credit": "Radosław Botev · CC0",
                "caption": "Las ruinas de Venn's Town.",
            },
        ],
    ),
    dict(
        n=6, name="Port Launay y Baie Ternay · los parques marinos del oeste", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1 día",
        lat=-4.6531882, lon=55.3999687,  # Google Maps: Port Launay Beach
        desc="El distrito de Port Glaud guarda los dos parques marinos del oeste de Mahé: Port Launay, con su humedal costero inscrito en el convenio Ramsar y manglares detrás de la arena, y Baie Ternay, una bahía cerrada que sólo se alcanza en barco y que tiene el mejor coral accesible de la isla. La SPGA cobra entrada a los no residentes mayores de 12 años, entre 200 y 300 SCR según el parque, y abre de 8:00 a 17:00. Prohibido pescar, recoger conchas y usar fusil submarino.",
        dog_note="Parques nacionales marinos gestionados por la SPGA, con manglar protegido y sitio Ramsar.",
        visit={
            "why": "Es el snorkel más fácil y más rico de Mahé, con aguas resguardadas y, en temporada, paso de tiburón ballena frente a la costa oeste.",
            "see": "Manglar y humedal Ramsar de Port Launay, arrecife y peces de arrecife en Baie Ternay, y la silueta de Thérèse e Île aux Vaches Marines.",
            "access": "Asfalto hasta Port Launay por la costa oeste desde Port Glaud; aparcamiento junto a la playa, correcto para dos 4x4. Baie Ternay NO tiene acceso rodado: se contrata barco en Port Launay o Beau Vallon. Entrada SPGA de 200 a 300 SCR para no residentes de más de 12 años; abierto 8:00–17:00; pago con tarjeta en el sitio. El pin marca la playa y el aparcamiento de Port Launay.",
            "when": "De abril a mayo y de octubre a noviembre, entre monzones, el agua está más clara y calmada.",
            "skip": "Con el monzón del noroeste (diciembre a marzo) la costa oeste se enturbia y el snorkel deja de tener sentido.",
        },
        links=[
            {"label": "SPGA · información al visitante y tarifas", "url": "https://www.spga.gov.sc/visitor-information"},
            {"label": "Port Glaud (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Port_Glaud"},
            {"label": "Ramsar · humedales costeros de Port Launay", "url": "https://www.ramsar.org/document/wetland-tourism-case-study-seychelles-port-launay-coastal-wetlands"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Port_Launay_Marine_NP.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Port_Launay_Marine_NP.jpg",
                "credit": "Dino Sassi / Marcel Fayon · Public domain",
                "caption": "El parque marino de Port Launay.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Port_Launay_Beach_(11207817916).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Port_Launay_Beach_(11207817916).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La playa de Port Launay.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Acropora_muricata,_Port_Launay,_Seychelles.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Acropora_muricata,_Port_Launay,_Seychelles.jpg",
                "credit": "Josuevg · CC BY-SA 3.0",
                "caption": "Coral en el parque marino.",
            },
        ],
    ),
    dict(
        n=7, name="Valle de Mai · el coco de mar, Praslin (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="medio día",
        lat=-4.3318526, lon=55.7401062,  # Google Maps: Reserva Natural del Valle de Mai
        desc="Diecinueve hectáreas y media de palmeral primitivo en el centro de Praslin, Patrimonio de la Humanidad desde 1983 por los criterios (vii), (viii), (ix) y (x). Aquí sobrevive la mayor población mundial de coco de mar, la palmera cuyo fruto bilobulado es LA SEMILLA MÁS GRANDE DEL REINO VEGETAL, hasta 42 kg, y el loro negro de Seychelles, que anida casi sólo en troncos muertos de esa palmera. Abre de 8:30 a 16:30, última entrada a las 15:30, y cuesta 450 SCR. Prohibido fumar.",
        dog_note="Reserva natural de Patrimonio Mundial gestionada por la SIF: sólo visitantes a pie, sin animales.",
        visit={
            "why": "Es el bien natural más accesible del país y el único sitio donde se ve el bosque de coco de mar casi intacto, con seis palmeras endémicas.",
            "see": "Coco de mar macho y hembra, loro negro de Seychelles, bulbul, y tres o cuatro itinerarios de entre 1,5 y 4 km por el fondo del valle.",
            "access": "Asfalto: está en la carretera que cruza Praslin entre Baie Sainte Anne y Grand'Anse; aparcamiento propio en el centro de visitantes, suficiente para dos 4x4. Horario 8:30–16:30 (última entrada 15:30), cerrado el 25 de diciembre y el 1 de enero; entrada 450 SCR, se paga en rupias, euros, dólares o libras, en efectivo o con tarjeta. El pin marca el centro de visitantes.",
            "when": "Nada más abrir, a las 8:30: menos grupos de Mahé y más actividad de los loros.",
            "skip": "Si ya se ha hecho Fond Ferdinand con guía, el valle aporta menos de lo que cuesta.",
        },
        links=[
            {"label": "UNESCO · Vallée de Mai Nature Reserve", "url": "https://whc.unesco.org/en/list/261"},
            {"label": "Seychelles Islands Foundation · Vallée de Mai", "url": "https://www.sif.sc/vdm"},
            {"label": "Vallée de Mai (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Vall%C3%A9e_de_Mai"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Vallee_de_Mai_Praslin_Seychelles.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Vallee_de_Mai_Praslin_Seychelles.jpg",
                "credit": "Radosław Botev · CC BY-SA 4.0",
                "caption": "El Valle de Mai, en Praslin.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Vallee_de_Mai_(1).JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Vallee_de_Mai_(1).JPG",
                "credit": "Remi Jouan · CC BY-SA 3.0",
                "caption": "El bosque de coco de mar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ailuronyx_tachyscopaeus_in_Vall%C3%A9e_de_Mai%3B_Praslin.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ailuronyx_tachyscopaeus_in_Vall%C3%A9e_de_Mai%3B_Praslin.jpg",
                "credit": "Fabiologist · CC BY 4.0",
                "caption": "Gecko endémico del Valle de Mai.",
            },
        ],
    ),
    dict(
        n=8, name="Anse Lazio y Anse Georgette · el norte de Praslin", cat="Costa", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=-4.2936687, lon=55.7015064,  # Google Maps: Anse Lazio
        desc="Las dos mejores playas de Praslin están a un kilómetro y medio una de otra en el extremo noroeste. Anse Lazio, granito redondeado y agua turquesa, fue cuarta del mundo para CNN en 2016 y desde 2024 es PLAYA NO MOTORIZADA. Anse Georgette, medio kilómetro de arena entre bloques, está dentro de la finca del Constance Lémuria: el acceso está restringido y hay que pedir permiso previo si no se aloja allí, o llegar a pie desde Anse Lazio o en barco. Ninguna de las dos tiene arrecife delante.",
        dog_note="Anse Georgette está dentro de un resort privado y Anse Lazio es playa no motorizada muy vigilada.",
        visit={
            "why": "Es la postal de Praslin y el mejor baño de la isla cuando el mar del norte está en calma.",
            "see": "Bloques de granito, takamakas sobre la arena y, desde el collado, la vista hacia Curieuse.",
            "access": "Asfalto hasta Anse Boudin y luego una cuesta corta y empinada con aparcamiento al pie de Anse Lazio, justo para dos 4x4 si no hay grupos. Anse Georgette no tiene acceso rodado público: permiso del Constance Lémuria, sendero desde Anse Lazio o barco. El pin marca el aparcamiento de Anse Lazio.",
            "when": "De mayo a septiembre, con el alisio del sureste, el norte de Praslin queda a resguardo.",
            "skip": "Si el resort no da permiso, Anse Georgette se descarta sin más; y con mar de fondo Anse Lazio pierde el atractivo.",
        },
        links=[
            {"label": "Anse Lazio (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Anse_Lazio"},
            {"label": "Anse Georgette (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Anse_Georgette"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Anse_Lazio_beach_Praslin_Seychelles.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Anse_Lazio_beach_Praslin_Seychelles.jpg",
                "credit": "Svein-Magne Tunli · CC BY-SA 4.0",
                "caption": "Anse Lazio.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Seychelles_praslin_anselazio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Seychelles_praslin_anselazio.jpg",
                "credit": "Autor desconocido · CC BY-SA 2.0 de",
                "caption": "El granito de Anse Lazio.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Anse_Lazio-rama_2015.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Anse_Lazio-rama_2015.JPG",
                "credit": "Bjørn Christian Tørrissen · CC BY-SA 4.0",
                "caption": "Panorámica de Anse Lazio.",
            },
        ],
    ),
    dict(
        n=9, name="Reserva de Fond Ferdinand · el interior de Praslin", cat="Naturaleza", prio="Media",
        dog="prohibido", time="medio día",
        lat=-4.3540847, lon=55.7583444,  # Google Maps: Fond Ferdinand
        desc="La alternativa al Valle de Mai, en el sureste de Praslin cerca de Anse Marie-Louise. Más de 6.000 cocos de mar, algunos de más de ochenta años, en un valle que se sube por un sendero de unos 2 km hasta el mirador de Zimbabwe Point, con vista de 360 grados sobre Praslin, La Digue y las islas satélite. La visita ES SIEMPRE GUIADA y dura unas dos horas; entrada de 300 SCR en efectivo, abierto de 8:30 a 15:30 y última salida hacia la una del mediodía.",
        dog_note="Reserva con visita obligatoriamente guiada por bosque endémico de coco de mar.",
        visit={
            "why": "Se ven los mismos cocos de mar que en el Valle de Mai pero con guía incluida, menos gente y un mirador que el valle no tiene.",
            "see": "Palmeral de coco de mar, endemismos de Praslin y el panorama del archipiélago interior desde Zimbabwe Point.",
            "access": "Asfalto hacia el sur desde Baie Sainte Anne en dirección a Anse Marie-Louise; el desvío lo marca un cartel rojo pequeño. Aparcamiento gratuito en la propia entrada, sobrado para dos 4x4. Entrada 300 SCR en efectivo, guía incluida; horario 8:30–15:30, última caminata sobre las 13:00. El pin marca la entrada de la reserva.",
            "when": "A primera hora: la subida da el sol de lleno a partir de media mañana.",
            "skip": "Con lluvia el sendero embarra y el mirador no ofrece nada.",
        },
        links=[
            {"label": "Praslin (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Praslin"},
            {"label": "Guía de Fond Ferdinand (Lilla Green)", "url": "https://lillagreen.com/fond-ferdinand-nature-reserve-praslin-seychelles/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Archaius_tigris_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Archaius_tigris_2.jpg",
                "credit": "Hans Stieglitz · CC BY-SA 3.0",
                "caption": "Camaleón tigre, endémico de Seychelles.",
            },
        ],
    ),
    dict(
        n=10, name="Isla Curieuse · las tortugas gigantes y el manglar", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="1 día",
        lat=-4.3496065, lon=55.7620086,  # Google Maps: Baie Sainte Anne (Praslin)
        desc="A un cuarto de hora de barco desde Praslin, Curieuse tiene 2,93 km² y una historia doble: fue leprosería entre 1829 y 1965 y, entre 1978 y 1982, destino de las tortugas gigantes traídas de Aldabra. Hoy viven allí MÁS DE 300 TORTUGAS EN LIBERTAD y la isla, declarada parque nacional marino en 1979, conserva un manglar con pasarela y la antigua casa del médico, convertida en museo. La visita se hace en excursión de día: no hay alojamiento ni transporte propio.",
        dog_note="Parque nacional marino con tortugas gigantes en libertad: acceso sólo a pie y sin animales.",
        visit={
            "why": "Es el sitio más fácil del archipiélago interior para ver tortugas gigantes sueltas, y se combina con snorkel y un manglar bien interpretado.",
            "see": "Tortugas de Aldabra, la Doctor's House de Anse St. Joseph, la pasarela del manglar y la playa de Baie Laraie.",
            "access": "No hay acceso rodado: se embarca en Baie Sainte Anne o en Côte d'Or (Praslin), con operador. Entrada del parque marino gestionada por la SPGA, entre 200 y 300 SCR para no residentes mayores de 12 años; horario del parque 8:00–17:00. El pin marca el embarcadero de Baie Sainte Anne, al que sí se conduce.",
            "when": "De mayo a septiembre el mar entre Praslin y Curieuse está más plano; salidas siempre por la mañana.",
            "skip": "Con aviso de mar gruesa la travesía se cancela y el día se pierde.",
        },
        links=[
            {"label": "Curieuse Island (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Curieuse_Island"},
            {"label": "SPGA · información al visitante y tarifas", "url": "https://www.spga.gov.sc/visitor-information"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ile_Praslin_-_Baie_Sainte-Anne_(1).JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ile_Praslin_-_Baie_Sainte-Anne_(1).JPG",
                "credit": "Remi Jouan · CC BY-SA 3.0",
                "caption": "La bahía de Baie Sainte-Anne.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Praslin_marina.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Praslin_marina.jpg",
                "credit": "Radosław Botev · CC BY 3.0 pl",
                "caption": "El embarcadero de Praslin.",
            },
        ],
    ),
    dict(
        n=11, name="Cousin y Aride · las islas santuario de aves", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1 día",
        lat=-4.3169478, lon=55.7476916,  # Google Maps: Anse Volbert Village
        desc="Dos reservas especiales frente a Praslin, las dos sólo visitables en excursión guiada. Cousin, 29 hectáreas declaradas reserva especial en 1975 y gestionada por Nature Seychelles, salvó al curruca de Seychelles, que pasó de 26 aves en 1959 a unas 3.000 en el archipiélago; sólo abre las mañanas de días laborables. Aride, 68 hectáreas a 10 km al norte de Praslin, reúne MÁS DE 1,25 MILLONES DE AVES MARINAS reproductoras y la única población mundial de la gardenia de Wright. El desembarco es por playa, sin muelle.",
        dog_note="Reservas especiales libres de depredadores introducidos: no entra ningún animal doméstico.",
        visit={
            "why": "Son las dos mejores colonias de aves marinas accesibles en un día desde Praslin, con desembarco entre miles de charranes y nodis.",
            "see": "Curruca y fody de Seychelles, nodi menor, rabijunco, pardela, tortuga carey anidando y, en Aride, la gardenia de Wright.",
            "access": "No hay acceso rodado: se contrata barco en Praslin (Côte d'Or o Baie Sainte Anne) con operador autorizado; desembarco en playa, mojándose los pies. Cousin abre sólo mañanas de días laborables. Aride es de difícil acceso entre junio y septiembre porque el alisio del sureste bloquea su única playa, orientada al sur. El pin marca la playa de Anse Volbert, donde se embarca.",
            "when": "De abril a mayo y de octubre a noviembre; en Aride evitar junio-septiembre.",
            "skip": "Si el operador avisa de mar de fondo, se anula: el desembarco en Aride es delicado.",
        },
        links=[
            {"label": "Cousin Island (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Cousin_Island"},
            {"label": "Aride Island (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Aride_Island"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Praslin_Anse_Volbert.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Praslin_Anse_Volbert.JPG",
                "credit": "Marek Gehrmann · CC BY-SA 3.0",
                "caption": "Anse Volbert, la Côte d'Or.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Seychellen_-_Praslin_-_Strand_Cote_D'or.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Seychellen_-_Praslin_-_Strand_Cote_D'or.jpg",
                "credit": "Christoph Scholz · CC BY-SA 4.0",
                "caption": "La playa de la Côte d'Or.",
            },
        ],
    ),
    dict(
        n=12, name="La Digue · Anse Source d'Argent y las rocas de granito", cat="Costa", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=-4.36315, lon=55.82562,  # Google Maps: La Digue (sin objeto en Google Maps; coordenada de la fuente)
        desc="La Digue tiene 10,08 km² y unos 2.800 habitantes, y la bicicleta sigue siendo el medio de transporte principal: no hay aeropuerto y se llega en ferry desde Praslin. Anse Source d'Argent, dos kilómetros de arena entre bloques de granito erosionado, se entra por L'Union Estate, una antigua plantación reconvertida en reserva con casa colonial, molino de copra movido por bueyes, vainilla y tortugas gigantes. Es probablemente LA PLAYA MÁS FOTOGRAFIADA DEL MUNDO; a mediodía está llena y la marea baja deja el agua a un palmo.",
        dog_note="Se entra por la finca privada de L'Union Estate, con tortugas gigantes en recinto abierto.",
        visit={
            "why": "Es la imagen que todo el mundo asocia a Seychelles y, además, la única isla donde se recorre todo a pie o en bici sin coche.",
            "see": "Bloques de granito, la Grann Kaz colonial, el molino de copra, el cementerio de los primeros colonos y las tortugas gigantes de la finca.",
            "access": "Se llega en ferry de 15 minutos desde Baie Sainte Anne (Praslin) o en Cat Cocos desde Victoria, 1 h 45; en la isla no hay coche de alquiler para turistas, se va en bici desde La Passe. Entrada de pago a L'Union Estate, importe no confirmado. El pin marca la puerta de L'Union Estate, en La Passe.",
            "when": "A primera hora o al atardecer; la marea alta es el único momento en que se puede nadar de verdad.",
            "skip": "A mediodía en temporada alta la playa está saturada y la marea baja deja un charco.",
        },
        links=[
            {"label": "L'Union Estate (Wikipedia)", "url": "https://en.wikipedia.org/wiki/L%27Union_Estate"},
            {"label": "Anse Source d'Argent (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Anse_Source_d%27Argent"},
            {"label": "La Digue (Wikipedia)", "url": "https://en.wikipedia.org/wiki/La_Digue"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Anse_Source_d'Argent-La_Digue-Seychellen.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Anse_Source_d'Argent-La_Digue-Seychellen.jpg",
                "credit": "Tobias Alt · CC BY-SA 4.0",
                "caption": "Anse Source d'Argent, en La Digue.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Anse_Source_d'Argent_3-La_Digue.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Anse_Source_d'Argent_3-La_Digue.jpg",
                "credit": "Tobias Alt · CC BY-SA 4.0",
                "caption": "Los bloques de granito de Source d'Argent.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Clear_kayaks_-_crystal_kayaks_-_Anse_Source_d'Argent_-_La_Digue_-_Seychelles_-_1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Clear_kayaks_-_crystal_kayaks_-_Anse_Source_d'Argent_-_La_Digue_-_Seychelles_-_1.jpg",
                "credit": "NorbertNagel · CC BY-SA 4.0",
                "caption": "Kayaks en Source d'Argent.",
            },
        ],
    ),
    dict(
        n=13, name="Reserva de la Veuve · el interior de La Digue", cat="Naturaleza", prio="Media",
        dog="prohibido", time="medio día",
        lat=-4.3478359, lon=55.8328987,  # Google Maps: La Passe (La Digue)
        desc="En el centro de La Digue, un bosque bajo de takamaka y Calophyllum protege al monarca colilargo de Seychelles, la «veuve», ave clasificada como vulnerable por la UICN y con una población de sólo unos cientos de ejemplares. La reserva la gestiona la SPGA y abre de 8:00 a 16:00 de lunes a viernes y de 9:00 a 15:00 los sábados. La entrada para no residentes se revisó en junio de 2019 a 11 USD sin guía y 15 USD con guía. En 2008 se trasladaron 23 aves a Denis para crear una segunda población.",
        dog_note="Reserva especial creada para una de las aves más amenazadas del mundo: sin perros.",
        visit={
            "why": "Es la única posibilidad realista de ver la veuve, un endemismo que no existe en ningún otro sitio salvo la población trasladada a Denis.",
            "see": "Monarca colilargo macho, de cola muy larga y negro azabache, bosque de Calophyllum y una charca con terrapenes.",
            "access": "Se llega en bicicleta desde el embarcadero de La Passe por caminos llanos; no hay aparcamiento porque no hay coches. Horario 8:00–16:00 de lunes a viernes y 9:00–15:00 los sábados; entrada 11 USD sin guía y 15 USD con guía para no residentes. El pin marca el centro de la reserva.",
            "when": "Primera hora de la mañana, cuando los machos cantan y se mueven.",
            "skip": "Si el tiempo en La Digue es corto, Anse Source d'Argent y Grand Anse tienen prioridad.",
        },
        links=[
            {"label": "SPGA · información al visitante y tarifas", "url": "https://www.spga.gov.sc/visitor-information"},
            {"label": "Monarca colilargo de Seychelles (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Seychelles_paradise_flycatcher"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/La_Digue_Marina_-_La_Digue_-_Seychelles.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:La_Digue_Marina_-_La_Digue_-_Seychelles.jpg",
                "credit": "NorbertNagel · CC BY-SA 4.0",
                "caption": "El puerto de La Passe, en La Digue.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Grand_Anse-La_Digue-Seychellen.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Grand_Anse-La_Digue-Seychellen.jpg",
                "credit": "Tobias Alt · CC BY-SA 4.0",
                "caption": "Grand Anse, en La Digue.",
            },
        ],
    ),
    dict(
        n=14, name="Isla Bird · el santuario de charranes", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=-3.7206202, lon=55.2052085,  # Google Maps: Bird Island
        desc="Isla coralina de 0,94 km² a 100 km al norte de Mahé, la más septentrional del país. Entre finales de marzo y octubre acoge la colonia de charrán sombrío más espectacular del archipiélago: UNAS 700.000 PAREJAS anidando en el suelo, de forma que la isla se recorre entre aves. Vive allí Esmeralda, tortuga gigante de más de 300 kg y unos 170 años, citada como la tortuga en libertad más grande y pesada del mundo. Sólo hay siete chalés y una pista de aterrizaje: se reserva con mucha antelación.",
        dog_note="Isla privada de conservación donde se erradicaron ratas y conejos: no entra ningún animal.",
        visit={
            "why": "Es un espectáculo de fauna difícil de igualar y una de las pocas islas exteriores accesibles con un vuelo corto desde Mahé.",
            "see": "Charrán sombrío en temporada, charrán blanco, nodi común, tortuga carey desovando y Esmeralda.",
            "access": "No hay acceso rodado ni barco regular: vuelo doméstico de unos 30 minutos desde el aeropuerto internacional de Mahé al aeródromo de Bird Island, incluido normalmente en la reserva del lodge. Bungalós deliberadamente básicos, sin aire acondicionado, teléfono ni televisión. El pin marca la terminal doméstica del aeropuerto de Mahé, que es el punto al que se conduce.",
            "when": "De abril a septiembre, con la colonia de charrán sombrío ocupada; fuera de esa ventana la isla está mucho más vacía.",
            "skip": "Fuera de la temporada de charrán y sin reserva en el lodge, no tiene sentido.",
        },
        links=[
            {"label": "Bird Island, Seychelles (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bird_Island,_Seychelles"},
            {"label": "Bird Island Lodge · guía de la isla", "url": "https://www.seyvillas.com/en/guide/islands/inner-islands/bird"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bird_Island_aerial.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bird_Island_aerial.jpg",
                "credit": "Phil Guest / Radosław Botev · CC BY-SA 2.0",
                "caption": "La isla Bird desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sooty_Tern_Bird_Island_Seychelles.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sooty_Tern_Bird_Island_Seychelles.jpg",
                "credit": "Tribalninja · CC BY 3.0",
                "caption": "Charranes sombríos en Bird.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Bird_Island_birds.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Bird_Island_birds.jpg",
                "credit": "Phil Guest · CC BY-SA 2.0",
                "caption": "La colonia de aves de Bird.",
            },
        ],
    ),
    dict(
        n=15, name="Denis y Silhouette · las islas interiores del norte", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=-4.6204838, lon=55.4167072,  # Google Maps: Bel Ombre (Mahé)
        desc="Dos islas opuestas. Denis es coralina y llana, 1,4 km² a 60 km al norte de Mahé, con faro de 1910, pista de aterrizaje y un programa de reintroducción que en 2004 recibió 47 fodys y 58 currucas de Seychelles. Silhouette es granítica y montañosa, 20,1 km² a 20 km al noroeste de Mahé, con el Mont Dauban de 751 m y CINCO CUMBRES POR ENCIMA DE 500 m; en 2010 se creó el Parque Nacional de Silhouette, que protege el 93 % de la superficie. Es uno de los puntos de mayor biodiversidad del Índico occidental.",
        dog_note="Parque nacional en Silhouette y programa de reintroducción de aves en Denis: sin animales domésticos.",
        visit={
            "why": "Silhouette ofrece el bosque primario y las travesías de montaña que ya no quedan en Mahé; Denis, un atolón-jardín con aves endémicas reintroducidas.",
            "see": "Mont Dauban y el bosque de Silhouette, murciélago de cola envainada de Seychelles, faro de Denis, fody y curruca reintroducidos.",
            "access": "Silhouette: ferry o lancha desde Bel Ombre o Beau Vallon (Mahé), unos 45 minutos. Denis: sólo vuelo desde la terminal doméstica de Mahé, normalmente incluido en la reserva del lodge. Ninguna de las dos tiene carretera pública. El pin marca el embarcadero de Bel Ombre, en Mahé, al que sí se conduce.",
            "when": "De mayo a septiembre para caminar por Silhouette con menos humedad; Denis, todo el año.",
            "skip": "Si no se pernocta, la logística de ambas se come el día entero.",
        },
        links=[
            {"label": "Denis Island (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Denis_Island"},
            {"label": "Silhouette Island (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Silhouette_Island"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Silhouette_Island,_Seychelles_(6291538872).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Silhouette_Island,_Seychelles_(6291538872).jpg",
                "credit": "Fabio Achilli · CC BY 2.0",
                "caption": "La isla Silhouette.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Silhouette_Island,_Seychelles_(6291528600).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Silhouette_Island,_Seychelles_(6291528600).jpg",
                "credit": "Fabio Achilli · CC BY 2.0",
                "caption": "El relieve de Silhouette.",
            },
        ],
    ),
    dict(
        n=16, name="Atolón de Aldabra · el mayor atolón coralino elevado del mundo (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="1–2 semanas (expedición marítima)",
        lat=-9.4236984, lon=46.3432781,  # Google Maps: Aldabra
        desc="Aldabra está a 1.120 km al suroeste de Victoria y más cerca de la costa africana que de Mahé. Mide 34 por 13 km, 155,4 km² de tierra, y es EL MAYOR ARRECIFE CORALINO ELEVADO DEL MUNDO, con 8 m de altura máxima. Patrimonio de la Humanidad desde el 19 de noviembre de 1982 por los criterios (vii), (ix) y (x), alberga unas 100.000 tortugas gigantes, la mayor población del planeta. No hay pista, ni puerto, ni helipuerto: sólo se llega en barco con autorización previa de la Seychelles Islands Foundation.",
        dog_note="Reserva natural estricta de Patrimonio Mundial con control de especies invasoras: acceso sólo con personal de la SIF.",
        visit={
            "why": "Es el gran objetivo natural del Índico: un ecosistema casi intacto con la mayor población mundial de tortugas gigantes y unos 900 visitantes al año.",
            "see": "Tortugas gigantes de Aldabra, laguna interior, rabihorcados, rascón de Cuvier —la última ave no voladora del Índico— y la estación de investigación de La Gigi, en Picard.",
            "access": "No hay acceso rodado ni vuelo directo: charter a Assumption (a unos 45-50 km) y transbordo en barco, o travesía de varios días desde Mahé en barco de expedición. Toda embarcación necesita autorización previa de la SIF (info@sif.sc). Tasa de impacto de 250 USD por persona y día. Sólo se accede a zonas concretas y SIEMPRE acompañado por personal de la SIF. Seguridad: el MAEC desaconseja vivamente navegar por la Zona Económica Exclusiva de Seychelles por ataques de piratas, así que sólo tiene sentido con operador profesional. El pin marca la sede de la Seychelles Islands Foundation en Victoria, donde se tramita.",
            "when": "Las travesías de expedición se concentran entre noviembre y abril, fuera del alisio fuerte.",
            "skip": "Sin plaza en un crucero de expedición y sin presupuesto de cuatro cifras al día, se descarta.",
        },
        links=[
            {"label": "UNESCO · Aldabra Atoll", "url": "https://whc.unesco.org/en/list/185"},
            {"label": "Seychelles Islands Foundation · visitar Aldabra", "url": "https://www.sif.sc/aldabra"},
            {"label": "Aldabra (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Aldabra"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Aldabra_Islands.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Aldabra_Islands.jpg",
                "credit": "C. Keller · Public domain",
                "caption": "El atolón de Aldabra.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Seychelles_outer_islands_25.08.2009_10-19-35.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Seychelles_outer_islands_25.08.2009_10-19-35.jpg",
                "credit": "Simisa · CC BY-SA 3.0",
                "caption": "Las islas exteriores de Seychelles.",
            },
        ],
    ),
    dict(
        n=17, name="Islas Amirantes y Desroches · las exteriores del suroeste", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 semanas",
        lat=-5.6952285, lon=53.6583166,  # Google Maps: Isla Desroches
        desc="Las Amirantes son un rosario coralino de 20 islas repartidas a lo largo de 155 km, con apenas 11,5 km² de tierra y 15 m de altura máxima. Las DESCUBRIÓ VASCO DA GAMA en su segundo viaje, en 1503, y de ahí el nombre portugués «Ilhas do Almirante». Desroches es la mayor y la única con infraestructura: 4 km² a 227 km al suroeste de Victoria, pista asfaltada de 1.372 m con vuelos desde Mahé al menos cuatro veces por semana y un centro de conservación abierto en 2009.",
        dog_note="Islas de conservación con centro de la Island Conservation Society y playas de puesta de tortuga.",
        visit={
            "why": "Es el buceo y la pesca de altura más remotos que se pueden hacer sin expedición: pared del Drop, tortugas verdes y carey anidando.",
            "see": "Playas vírgenes, unas 79 tortugas verdes desovando al año en Desroches, el centro de conservación de la ICS y los atolones vecinos de Poivre y D'Arros.",
            "access": "Sin acceso rodado ni ferry: vuelo desde la terminal doméstica de Mahé, al menos cuatro frecuencias semanales y varias diarias en temporada alta; barcaza de suministro dos veces al mes. Alojamiento sólo en el resort. El pin marca la terminal doméstica del aeropuerto de Mahé.",
            "when": "De octubre a abril, con el mar más manejable para las travesías y el buceo.",
            "skip": "Si el presupuesto no da para el resort, no hay alternativa de alojamiento.",
        },
        links=[
            {"label": "Amirante Islands (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Amirante_Islands"},
            {"label": "Desroches Island (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Desroches_Island"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Desroches_beach_(Pietervisser)_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Desroches_beach_(Pietervisser)_01.jpg",
                "credit": "Pieter Visser · CC BY 3.0",
                "caption": "La playa de Desroches.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Desroches_ISS022.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Desroches_ISS022.jpg",
                "credit": "NASA, mosaico de Szczureq · Public domain",
                "caption": "Desroches desde la Estación Espacial Internacional.",
            },
        ],
    ),
    dict(
        n=18, name="Alphonse y St. Joseph · los atolones exteriores del sur", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 semanas",
        lat=-7.0055424, lon=52.7268663,  # Google Maps: Islas Alphonse
        desc="Alphonse está a 400 km al sur de Victoria: una sola isla de 1,71 km² dentro de un atolón de 19 km², con pista de 1.220 m que la cruza en diagonal y dos a cinco vuelos semanales de la IDC. Es un destino de PESCA CON MOSCA en las llanuras de St. François, a 2 km al sur. St. Joseph, en cambio, pertenece a las Amirantes: 13 islotes deshabitados y 1,21 km², vendidos junto a D'Arros en agosto de 2012 por 60 millones de dólares y gestionados hoy como reserva por la Save Our Seas Foundation.",
        dog_note="Reservas privadas de conservación (Alphonse Foundation y Save Our Seas): acceso muy restringido.",
        visit={
            "why": "Alphonse es uno de los pocos lugares del mundo donde se pesca a mosca en llanuras de arena intactas; St. Joseph es un laboratorio de conservación marina cerrado al turismo general.",
            "see": "Llanuras de St. François, tiburones de arrecife, tortugas, y más especies de aves migratorias registradas que en ningún otro punto al sur de las islas graníticas salvo Aldabra.",
            "access": "Sin acceso rodado: vuelos IDC desde la terminal doméstica de Mahé a Alphonse, dos a cinco por semana; St. Joseph comparte con D'Arros una pista de tierra (FSDA) y su acceso está restringido por la Save Our Seas Foundation. El pin marca la terminal doméstica del aeropuerto de Mahé.",
            "when": "La temporada de pesca con mosca en Alphonse va de octubre a mayo, fuera del alisio fuerte.",
            "skip": "Si no se va a pescar ni a bucear, el coste y la logística no se justifican.",
        },
        links=[
            {"label": "Alphonse Atoll (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Alphonse_Atoll"},
            {"label": "St. Joseph Atoll (Wikipedia)", "url": "https://en.wikipedia.org/wiki/St._Joseph_Atoll"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Silhouette_55.23504E_4.48511S.png?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Silhouette_55.23504E_4.48511S.png",
                "credit": "NASA · Public domain",
                "caption": "Imagen de satélite de las islas exteriores.",
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
    ("Aeropuerto Internacional de Seychelles (SEZ)", "Frontera", -4.6709458, 55.5114812,  # Google Maps: Aeropuerto Internacional de Seychelles
     "Único punto de entrada aéreo internacional, en Mahé, a 11 km al sureste de Victoria. Código IATA SEZ, ICAO FSIA, pista única de 2.997 m. Operan Emirates, Qatar, Etihad, Turkish, Ethiopian, Kenya Airways, Air France y Condor. Aquí se presenta la Seychelles Travel Authorisation y se expide el Visitor's Permit gratuito de 3 meses. Pin comprobado en Google Maps («Aeropuerto Internacional de Seychelles»)."),
    ("Port Victoria (puerto de entrada marítimo e Inter Island Quay)", "Frontera", -4.6231555, 55.4550151,  # Google Maps: Victoria (Port Victoria)
     "Único puerto de entrada y salida del país para embarcaciones. Contacto con Port Control por VHF canal 12 dos horas antes de llegar, pabellón Q y despacho a bordo en el fondeadero de cuarentena. Aduana y puerto de 08:00 a 12:00 y de 13:00 a 15:00 de lunes a viernes. Desde el Inter Island Quay salen los catamaranes Cat Cocos a Praslin y La Digue, solo pasajeros. Pin comprobado en Google Maps («Victoria (Port Victoria)»)."),
    ("Embajada de España en Adís Abeba (competente para Seychelles)", "Consular", 9.03, 38.74,  # Google Maps: Embajada de España en Adís Abeba (competente para Seychelles) (sin objeto en Google Maps; coordenada de la fuente)
     "España no tiene embajada residente en Victoria: la competencia es de la Embajada en Adís Abeba, que cubre Etiopía, Seychelles y Yibuti. Dirección: Haile Melekot Street, Gullele Subcity, Woreda 01, House n.º 036, P.O. Box 2312, Adís Abeba. Centralita +251 929 136 159, consular +251 929 136 161, correo emb.addisabeba@maec.es y emb.addisabeba.consu@maec.es. EMERGENCIA CONSULAR 24 h: +251 911 219 403. Pin comprobado en Google Maps («Embajada de España en Adís Abeba (competente para Seychelles) (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Consulado Honorario de España en Victoria", "Consular", -4.6191, 55.4513,  # Google Maps: Consulado Honorario de España en Victoria (sin objeto en Google Maps; coordenada de la fuente)
     "Consulado honorario en Victoria (Mahé), a cargo de Selwyn Edmond según la Ficha País del MAEC. Teléfono +248 4 303300. Es el primer contacto sobre el terreno, pero la asistencia consular plena depende de la Embajada en Adís Abeba. POR CONFIRMAR la dirección postal exacta. Pin comprobado en Google Maps («Consulado Honorario de España en Victoria (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Seychelles Hospital (Mont Fleuri, Victoria)", "Hospital", -4.6312562, 55.4557617,  # Google Maps: Seychelles Hospital Mont Fleuri
     "Hospital público de referencia nacional, en el distrito de Mont Fleuri de Victoria, con 211 camas. Es el centro al que se deriva cualquier urgencia grave del país. Teléfono +248 438 8000 según el MAEC. Recordatorio: sin seguro de viaje acreditado la asistencia puede ser denegada. Pin comprobado en Google Maps («Seychelles Hospital Mont Fleuri»)."),
    ("Baie Ste Anne Hospital (Praslin)", "Hospital", -4.3167, 55.7417,  # Google Maps: Baie Ste Anne Hospital (Praslin) (sin objeto en Google Maps; coordenada de la fuente)
     "Hospital de referencia de Praslin, la segunda isla del país, incluido en el listado oficial del Ministerio de Salud. Atiende también a La Digue. Centralita del sistema sanitario: +248 4388000. Los casos graves se evacúan al Seychelles Hospital de Victoria. Pin comprobado en Google Maps («Baie Ste Anne Hospital (Praslin) (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Estaciones de servicio de Victoria (Mahé)", "Combustible", -4.6167, 55.45,  # Google Maps: Estaciones de servicio de Victoria (Mahé) (sin objeto en Google Maps; coordenada de la fuente)
     "La red de estaciones se concentra en Victoria y en los ejes principales de Mahé, con oferta menor en Praslin y prácticamente inexistente en La Digue. Gasolina 95 a 20,50 SCR por litro (1,26 €) según GlobalPetrolPrices, 9 de febrero de 2026. Todo el combustible es importado y se descarga en Port Victoria. Pin comprobado en Google Maps («Estaciones de servicio de Victoria (Mahé) (sin objeto en Google Maps; coordenada de la fuente)»)."),
    ("Red de agua potable de Mahé (Public Utilities Corporation)", "Agua potable", -4.6216554, 55.4507524,  # Google Maps: Public Utilities Corporation
     "El suministro de Mahé y Praslin lo gestiona la Public Utilities Corporation y el agua de red es apta para uso general; para beber, lo habitual es agua embotellada fuera de Mahé. Hay estrés hídrico estacional durante el monzón del sureste, de mayo a septiembre. POR CONFIRMAR si existe racionamiento vigente en 2026. Pin comprobado en Google Maps («Public Utilities Corporation»)."),
    ("Animal Biosecurity Section (permisos de importación de animales)", "Consular", -4.6208203, 55.4544261,  # Google Maps: Ministry of Fisheries and Agriculture (Victoria)
     "Border Control and Support Division del Ministry of Fisheries, Agriculture and Blue Economy: Maison Collet, 2.ª planta, Palm Street, Victoria (Mahé), P.O. Box 408. Teléfono +248 4672300, correo info@mofbe.gov.sc. Es donde se tramita el permiso previo de importación de un perro y donde se resuelven las condiciones veterinarias. Pin comprobado en Google Maps («Ministry of Fisheries and Agriculture (Victoria)»)."),
    ("Anse Royale Hospital (sur de Mahé)", "Hospital", -4.7400736, 55.5169341,  # Google Maps: Anse Royale Hospital
     "Segundo hospital de Mahé, en la costa sureste, incluido en el listado oficial del Ministerio de Salud de Seychelles. Útil como referencia si la urgencia se produce lejos de Victoria, a unos 25 km por carretera de montaña. Centralita sanitaria +248 4388000. Pin comprobado en Google Maps («Anse Royale Hospital»)."),
]

DRONE_CALLOUT = ("warn", "Legales sobre el papel, confiscados en la práctica",
                 "Volar dron en Seychelles es legal y la Seychelles Civil Aviation Authority (SCAA) no exige licencia de piloto a los visitantes, pero sí registro previo de todo aparato de 200 gramos o más. El problema está en la aduana: hay casos documentados de drones intervenidos a la llegada pese a cumplir la norma. Con casi la mitad del país declarada área protegida, el margen para volar legalmente es estrecho. Si el dron no es imprescindible, la decisión limpia es dejarlo en casa.")

STARLINK_CALLOUT = ("", "Starlink activo desde julio de 2026",
                    "El Gabinete de Seychelles aprobó la licencia de Starlink el 18 de febrero de 2026 y el servicio se activó el 18 de julio, como 28.º mercado africano del operador. Para un viaje corto aporta poco: la cobertura 4G y 5G de Cable & Wireless y Airtel en Mahé, Praslin y La Digue es buena y el país ya tenía un 87 % de uso de internet en 2025. Starlink compite aquí como resiliencia y como cobertura para islas exteriores y uso marítimo, no como acceso básico. En travesía a Aldabra o Alphonse sí es la única opción.")

DOG_MATRIX = [
    ("Entrada por el aeropuerto de Mahé (SEZ)", "permitido con condiciones", "Permiso veterinario previo por escrito, microchip, rabia, titulación, antiparasitario 48 h antes y CUARENTENA mínima de 14 días. Para un viaje corto no compensa: dejar al perro en el continente o en España."),
    ("Entrada en velero por Port Victoria", "prohibido", "Sin autorización escrita de la Sección Veterinaria el animal NO puede pisar tierra. El desembarco ilegal se sanciona con multa, prisión y confiscación. Plan B: el perro permanece a bordo todo el fondeo."),
    ("Estancia turística inferior a seis meses", "no recomendado", "Noonsite (2024) indica que no se aceptan mascotas por menos de seis meses. Plan B: descartar Seychelles de cualquier itinerario con perro y planificarlo como viaje sin animal."),
    ("Islas exteriores y Aldabra", "prohibido", "Reservas naturales estrictas gestionadas por la Seychelles Islands Foundation, con control de especies invasoras. Ningún animal doméstico entra. Plan B: no existe."),
    ("Parques nacionales y reservas de Mahé y Praslin (Morne Seychellois, Valle de Mai)", "por confirmar", "No se ha localizado norma publicada sobre perros en áreas protegidas terrestres. Criterio prudente: asumir prohibición. Plan B: preguntar a la Seychelles National Parks Authority antes de moverse."),
    ("Regreso a la Unión Europea desde Mahé", "permitido con condiciones", "País NO listado en el Reglamento (UE) 2026/636: exige titulación antirrábica anotada ANTES de salir de la UE (vía A). Plan B: si no se hizo, analítica en laboratorio autorizado y tres meses de espera antes de volar."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Seychelles — Ministerio de Asuntos Exteriores, Unión Europea y Cooperación, consultado el 18 de septiembre de 2026", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Seychelles"),
    ("MAEC · Ficha País Seychelles (PDF) — Oficina de Información Diplomática, datos de 2024-2025", "https://www.exteriores.gob.es/Documents/FichasPais/SEYCHELLES_FICHA%20PAIS.pdf"),
    ("Embajada de España en Adís Abeba — MAEC, competencia sobre Etiopía, Seychelles y Yibuti, consultado en septiembre de 2026", "https://www.exteriores.gob.es/Embajadas/addisabeba/es/Paginas/index.aspx"),
    ("Seychelles Electronic Border System — portal oficial de la Travel Authorisation, Gobierno de Seychelles, 2026", "https://seychelles.govtas.com/en"),
    ("Seychelles Electronic Border System · FAQ sobre el precio de la Travel Authorisation — Gobierno de Seychelles, 2026", "https://seychelles.govtas.com/en/FAQ/dc3d5be6-d29e-4881-84f8-ad93a2759682"),
    ("Visa policy of Seychelles — Wikipedia, revisión de 2026 (tarifas de la ETA y Visitor's Permit)", "https://en.wikipedia.org/wiki/Visa_policy_of_Seychelles"),
    ("Seychelles — Wikipedia, revisión de 2026 (115 islas, 42 % de territorio protegido, elecciones 2020 y 2025)", "https://en.wikipedia.org/wiki/Seychelles"),
    ("Transport in Seychelles — Wikipedia, revisión de 2026 (conducción por la izquierda, 453 km de carretera, SPTC, Port Victoria)", "https://en.wikipedia.org/wiki/Transport_in_Seychelles"),
    ("Seychelles International Airport — Wikipedia, revisión de 2026 (coordenadas, aerolíneas, códigos SEZ/FSIA)", "https://en.wikipedia.org/wiki/Seychelles_International_Airport"),
    ("Aldabra — Wikipedia, revisión de 2026 (UNESCO 1982, 1.120 km de Mahé, Seychelles Islands Foundation, acceso con permiso)", "https://en.wikipedia.org/wiki/Aldabra"),
    ("Vallée de Mai Nature Reserve — UNESCO World Heritage Centre, ficha del bien n.º 261, inscrito en 1983", "https://whc.unesco.org/en/list/261/"),
    ("Seychelles Hospital — Wikipedia, revisión de 2026 (Mont Fleuri, Victoria, 211 camas, coordenadas)", "https://en.wikipedia.org/wiki/Seychelles_Hospital"),
    ("Seychelles Hospitals — Ministry of Health de Seychelles, listado de centros, consultado en septiembre de 2026", "https://www.health.gov.sc/seychelles-hospitals/"),
    ("Foreign travel advice: Seychelles · Safety and security — FCDO, Gobierno del Reino Unido, consultado en septiembre de 2026", "https://www.gov.uk/foreign-travel-advice/seychelles/safety-and-security"),
    ("Freedom in the World 2026: Seychelles — Freedom House, 81/100, estatus LIBRE", "https://freedomhouse.org/country/seychelles/freedom-world/2026"),
    ("Seychelles — TravelHealthPro, National Travel Health Network and Centre (NaTHNaC), actualizado en junio de 2026", "https://travelhealthpro.org.uk/country/194/seychelles"),
    ("Veterinary Import Conditions for Cats and Dogs, VS/REG/05/11/01 — Seychelles Agricultural Agency, Veterinary Services (PDF)", "https://anivetvoyage.com/wp-content/uploads/2022/04/Veterinary-Import-Conditions-for-Cats-and-Dogs1.pdf"),
    ("Seychelles · Pets — Noonsite, actualizado en enero de 2024 (permiso, cuarentena, prohibición de desembarco)", "https://www.noonsite.com/place/seychelles/view/pets/"),
    ("Seychelles · Clearance — Noonsite, actualizado en 2025 (Port Victoria único puerto de entrada, SMSA, tasas)", "https://www.noonsite.com/place/seychelles/view/clearance/"),
    ("Application to import live animals into the Republic of Seychelles (PDF) — Gobierno de Seychelles, 2024", "https://environment.gov.sc/wp-content/uploads/2024/02/APPLICATION-TO-IMPORT-LIVE-ANIMALS-INTO-THE-REPUBLIC-OF-SEYCHELLES.pdf"),
    ("Border Control and Support Division — Ministry of Fisheries, Agriculture and Blue Economy de Seychelles, 2026", "https://mofbe.gov.sc/agriculture-department/border-control-and-support-division/"),
    ("Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026, listas de terceros países para desplazamientos de animales de compañía — BOE/DOUE (PDF)", "https://www.boe.es/doue/2026/636/L00001-00007.pdf"),
    ("Reglamento Delegado (UE) 2026/131 de la Comisión, de 20 de enero de 2026 — EUR-Lex (PDF)", "https://eur-lex.europa.eu/legal-content/ES/TXT/PDF/?uri=OJ%3AL_202600131"),
    ("Cat Cocos · ferry Mahé–Praslin–La Digue — SeyFerry, horarios y tarifas vigentes hasta el 31 de diciembre de 2027", "https://www.seyferry.com/en_GB/cat-cocos-ferry-mahe-praslin-la-digue"),
    ("Seychelles Drone Laws 2026 — drone-laws.com, registro SCAA desde 200 g y casos de confiscación", "https://drone-laws.com/drone-laws-in-seychelles/"),
    ("Gasoline prices, Seychelles — GlobalPetrolPrices, dato de 9 de febrero de 2026 (20,50 SCR/litro)", "https://www.globalpetrolprices.com/Seychelles/gasoline_prices/"),
    ("Carnet de Passages en Douane · Seychelles — carnetdepassage.org, sin organización emisora AIT/FIA en el país", "https://www.carnetdepassage.org/country/seychelles"),
    ("Starlink goes live in Seychelles, VP confirms — Seychelles News Agency, julio de 2026", "https://www.seychellesnewsagency.com/articles/22195/starlink-goes-live-in-seychelles-vp-confirms"),
    ("Starlink Goes Live in Seychelles — Space in Africa, 18 de julio de 2026", "https://spaceinafrica.com/2026/07/18/starlink-goes-live-in-seychelles/"),
    ("Customs and Excises — Seychelles Revenue Commission, consultado en septiembre de 2026", "https://src.gov.sc/customs-and-excises/"),
    ("Viajar con la mascota. Perros, gatos, hurones — Ministerio de Agricultura, Pesca y Alimentación (MAPA), España", "https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones"),
    ("Travel advice and advisories for Seychelles — Government of Canada, actualizado el 9 de septiembre de 2026 (nivel de riesgo, permiso internacional de conducción)", "https://travel.gc.ca/destinations/seychelles"),
    ("Diesel prices, Seychelles — GlobalPetrolPrices, dato de 8 de diciembre de 2025 (20,54 SCR/litro)", "https://www.globalpetrolprices.com/Seychelles/diesel_prices/"),
    ("Victoria (Wikipedia)", "https://en.wikipedia.org/wiki/Victoria,_Seychelles"),
    ("Seychelles Parks and Gardens Authority · información al visitante", "https://www.spga.gov.sc/visitor-information"),
    ("Parque Nacional del Morne Seychellois (SPGA)", "https://www.spga.gov.sc/parks/morne-seychellois"),
    ("Jardín Botánico Nacional (Wikipedia)", "https://en.wikipedia.org/wiki/National_Botanical_Garden_of_Seychelles"),
    ("Beau Vallon (Wikipedia)", "https://en.wikipedia.org/wiki/Beau_Vallon,_Seychelles"),
    ("Anse Intendance (Wikipedia)", "https://en.wikipedia.org/wiki/Anse_Intendance"),
    ("Takamaka, Seychelles (Wikipedia)", "https://en.wikipedia.org/wiki/Takamaka,_Seychelles"),
    ("UNESCO · Mission Ruins of Venn's Town (lista indicativa)", "https://whc.unesco.org/en/tentativelists/5796/"),
    ("Seychelles Heritage Foundation", "https://www.seyheritage.sc/heritage-sites/venns-town-mission-ruins"),
    ("Mission Ruins of Venn's Town (Wikipedia)", "https://en.wikipedia.org/wiki/Mission_Ruins_of_Venn%27s_Town"),
    ("Port Glaud (Wikipedia)", "https://en.wikipedia.org/wiki/Port_Glaud"),
    ("Ramsar · humedales costeros de Port Launay", "https://www.ramsar.org/document/wetland-tourism-case-study-seychelles-port-launay-coastal-wetlands"),
    ("UNESCO · Vallée de Mai Nature Reserve", "https://whc.unesco.org/en/list/261"),
    ("Seychelles Islands Foundation · Vallée de Mai", "https://www.sif.sc/vdm"),
    ("Vallée de Mai (Wikipedia)", "https://en.wikipedia.org/wiki/Vall%C3%A9e_de_Mai"),
    ("Anse Lazio (Wikipedia)", "https://en.wikipedia.org/wiki/Anse_Lazio"),
    ("Anse Georgette (Wikipedia)", "https://en.wikipedia.org/wiki/Anse_Georgette"),
    ("Praslin (Wikipedia)", "https://en.wikipedia.org/wiki/Praslin"),
    ("Guía de Fond Ferdinand (Lilla Green)", "https://lillagreen.com/fond-ferdinand-nature-reserve-praslin-seychelles/"),
    ("Curieuse Island (Wikipedia)", "https://en.wikipedia.org/wiki/Curieuse_Island"),
    ("Cousin Island (Wikipedia)", "https://en.wikipedia.org/wiki/Cousin_Island"),
    ("Aride Island (Wikipedia)", "https://en.wikipedia.org/wiki/Aride_Island"),
    ("L'Union Estate (Wikipedia)", "https://en.wikipedia.org/wiki/L%27Union_Estate"),
    ("Anse Source d'Argent (Wikipedia)", "https://en.wikipedia.org/wiki/Anse_Source_d%27Argent"),
    ("La Digue (Wikipedia)", "https://en.wikipedia.org/wiki/La_Digue"),
    ("Monarca colilargo de Seychelles (Wikipedia)", "https://en.wikipedia.org/wiki/Seychelles_paradise_flycatcher"),
    ("Bird Island, Seychelles (Wikipedia)", "https://en.wikipedia.org/wiki/Bird_Island,_Seychelles"),
    ("Bird Island Lodge · guía de la isla", "https://www.seyvillas.com/en/guide/islands/inner-islands/bird"),
    ("Denis Island (Wikipedia)", "https://en.wikipedia.org/wiki/Denis_Island"),
    ("Silhouette Island (Wikipedia)", "https://en.wikipedia.org/wiki/Silhouette_Island"),
    ("UNESCO · Aldabra Atoll", "https://whc.unesco.org/en/list/185"),
    ("Seychelles Islands Foundation · visitar Aldabra", "https://www.sif.sc/aldabra"),
    ("Amirante Islands (Wikipedia)", "https://en.wikipedia.org/wiki/Amirante_Islands"),
    ("Desroches Island (Wikipedia)", "https://en.wikipedia.org/wiki/Desroches_Island"),
    ("Alphonse Atoll (Wikipedia)", "https://en.wikipedia.org/wiki/Alphonse_Atoll"),
    ("St. Joseph Atoll (Wikipedia)", "https://en.wikipedia.org/wiki/St._Joseph_Atoll"),
]

# Bucle de Mahé + salto en ferry a Praslin y La Digue
CORRIDOR = [
    (-4.63074, 55.45299),
    (-4.62134, 55.45132),
    (-4.6156, 55.42285),
    (-4.62048, 55.41671),
    (-4.65526, 55.44427),
    (-4.65319, 55.39997),
    (-4.65526, 55.44427),
    (-4.784, 55.49927),
    (-4.65526, 55.44427),
    (-4.62134, 55.45132),
    (-4.33185, 55.74011),
    (-4.29367, 55.70151),
    (-4.36315, 55.82562),
]

# Variante marítima y aérea a las islas exteriores (Bird, Denis, Silhouette, Amirantes, Alphonse, Aldabra)
CORRIDOR_ALT = [
    (-4.62134, 55.45132),
    (-3.72062, 55.20521),
    (-3.80361, 55.67028),
    (-4.4875, 55.23),
    (-5.69523, 53.65832),
    (-5.4, 53.3),
    (-7.00554, 52.72687),
    (-9.4237, 46.34328),
]

HISTORIA_RESUMEN = "Seychelles es el caso más nítido de África de un país sin población anterior a la colonización: las 115 islas del archipiélago estaban deshabitadas cuando Francia las anexionó en 1756 y las bautizó con el apellido de un ministro de Luis XV. De la plantación esclavista nació una sociedad criolla que hoy habla seselwa, inglés y francés. Independiente desde el 29 de junio de 1976, sufrió un golpe de Estado en 1977 y catorce años de partido único socialista antes de recuperar el multipartidismo en 1993. Desde entonces ha encadenado dos alternancias pacíficas, en 2020 y en 2025, y Freedom House la clasifica como libre con 80 puntos sobre 100. Vive del turismo y del atún, y protege cerca de la mitad de su territorio."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>Seychelles no tuvo reinos ni pueblos anteriores a la colonización, y esa ausencia es el punto de partida de todo lo demás: las islas estaban vacías de habitantes cuando llegaron los europeos. El archipiélago se sitúa a unos 1.500 kilómetros al este del continente africano y sus 115 islas —cuarenta y dos graníticas, restos de un antiguo supercontinente, y setenta y tres coralinas— suman apenas 455 kilómetros cuadrados de tierra firme repartidos por un océano inmenso.</p><p>Los navegantes árabes y austronesios de la ruta del Índico conocían estas aguas, pero no dejaron asentamiento permanente. La Wikipedia en español atribuye a Vasco da Gama un avistamiento el 15 de marzo de 1503; para la Enciclopedia Británica, el primer desembarco documentado es el de una expedición de la Compañía Británica de las Indias Orientales en 1609, que describió unas «islas deshabitadas». Durante el siglo XVII y buena parte del XVIII fueron sobre todo una aguada donde cargar agua, tortugas y madera, y un refugio de corsarios del Índico. Esa falta de sustrato precolonial explica que toda la identidad seychelense —lengua, cocina, música— sea una creación posterior, nacida ya dentro del sistema colonial.</p>"),
    ("Colonización",
     "<p>Francia llegó primero. Lazare Picault exploró el archipiélago en 1742 y 1744 y en 1756 el capitán Nicholas Morphey depositó en Mahé una «piedra de posesión» que formalizó la anexión. El nombre honra a Jean Moreau de Séchelles, ministro de Finanzas de Luis XV; los británicos lo transformarían después en Seychelles. El poblamiento fue obra del sistema de plantación: colonos franceses llegados de Isla de Francia con población esclavizada de África oriental y Madagascar para cultivar algodón, especias y cereales. De ese encuentro forzado nació el criollo seselwa.</p><p>Las guerras napoleónicas cambiaron la bandera. Tras la rendición de Mauricio en 1810 las islas pasaron a manos británicas y el Tratado de París de 1814 las cedió formalmente. Londres las administró como dependencia de Mauricio hasta 1903, cuando se convirtieron en colonia de la Corona con administración propia. La abolición de la esclavitud en la década de 1830 obligó a los plantadores a virar hacia cultivos menos intensivos en mano de obra —coco, vainilla y canela— y Victoria recibió además africanos liberados de barcos negreros interceptados por la Royal Navy. En 1948 se introdujo un Consejo Legislativo con miembros electos, primer esbozo de vida política local. El legado es visible: derecho y administración británicos, catolicismo y toponimia franceses, lengua criolla de base francesa.</p>"),
    ("Independencia y construcción del Estado",
     "<p>La descolonización fue tardía y negociada. El Reino Unido concedió el autogobierno en 1975 y la independencia el 29 de junio de 1976, dentro de la Commonwealth. El primer presidente fue James Mancham, partidario de una república abierta al turismo internacional y a los vínculos con Occidente; su primer ministro era France-Albert René, de orientación socialista.</p><p>El equilibrio duró poco más de un año. En 1977, con Mancham en el extranjero, René tomó el poder mediante un golpe de Estado y ocupó la presidencia. Una nueva Constitución convirtió al país en un Estado socialista de partido único, con el Frente Progresista del Pueblo de Seychelles como única formación legal. Fueron años de economía dirigida y de fuerte inversión pública en educación y sanidad —de ahí los buenos indicadores sociales actuales—, pero también de exilio opositor e intentos de desestabilización.</p><p>La presión internacional posterior a la Guerra Fría forzó el giro. René anunció en 1991 el regreso al multipartidismo y en 1993 una nueva Constitución, aprobada en referéndum, restableció las elecciones competitivas; sigue siendo la norma fundamental vigente. René las ganó y fue reelegido en varias ocasiones, de modo que la apertura formal convivió durante toda la década con la continuidad del mismo partido en el poder.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>René dimitió en abril de 2004 y entregó la presidencia a su vicepresidente, James Michel, reelegido en 2006, 2011 y 2015. La época estuvo marcada por la dependencia del turismo, un endeudamiento elevado y la piratería somalí, que llegó a operar en la zona económica exclusiva y empujó al país a cooperar en materia naval con la Unión Europea y España.</p><p>El deshielo político llegó por el Parlamento. En 2016 una coalición opositora obtuvo por primera vez la mayoría en la Asamblea Nacional, hito que Freedom House señala como el arranque del pluralismo real. Michel dimitió a finales de ese año y le sucedió su vicepresidente, Danny Faure. En octubre de 2020 el sacerdote anglicano Wavel Ramkalawan, de Linyon Demokratik Seselwa, ganó la presidencia con el 54,9% de los votos: era la primera vez que la oposición conquistaba el Ejecutivo desde 1977, y ocurrió sin violencia.</p><p>La segunda alternancia llegó cinco años después. En las generales del 27 de septiembre de 2025 y la segunda vuelta del 9 al 11 de octubre, Patrick Herminie devolvió el poder a United Seychelles con una participación superior al 86%. La campaña giró en buena medida sobre el medio ambiente y, en particular, sobre la cesión por setenta años de la isla de Assumption, vecina de Aldabra, a una cadena hotelera catarí, acuerdo que Herminie prometió cancelar.</p>"),
    ("Política y gobierno en 2026",
     "<p>Seychelles es una república presidencialista unitaria regida por la Constitución de 1993, según la ficha país del Ministerio de Asuntos Exteriores español actualizada en julio de 2026. El presidente es a la vez jefe del Estado y del Gobierno, elegido por sufragio universal para cinco años. A fecha de septiembre de 2026 el cargo lo ocupa <strong>Patrick Herminie</strong>, de United Seychelles, que tomó posesión el 26 de octubre de 2025 tras vencer en segunda vuelta a Wavel Ramkalawan por algo menos de cinco puntos; el vicepresidente es Sebastien Pillay. La Asamblea Nacional tiene 34 escaños, 25 electos y 9 proporcionales: United Seychelles obtuvo 19 y Linyon Demokratik Seselwa 15. Las próximas elecciones corresponderían a 2030.</p><p>Es una democracia efectiva, no una fachada. Freedom House la clasifica en «Freedom in the World 2025» como <em>Free</em> con 80 puntos sobre 100 —34 sobre 40 en derechos políticos y 46 sobre 60 en libertades civiles— y señala como problemas la corrupción, la prisión preventiva prolongada y la vulnerabilidad de los trabajadores migrantes. Reporteros Sin Fronteras la sitúa en el puesto 35 de 180 en 2026, con 73,04 puntos, tras despenalizarse la difamación en 2021. No hay conflicto armado: el MAEC solo desaconseja navegar por la zona económica exclusiva por riesgo de piratería y advierte de un repunte de robos. España mantiene relaciones desde 1978, sin embajada residente, y la Unión Europea firmó en abril de 2026 un acuerdo de pesca sostenible vigente hasta 2030 que ampara a una treintena de atuneros españoles con base en Victoria.</p>"),
    ("Economía y recursos",
     "<p>Seychelles tiene la renta por habitante más alta de África y, a la vez, una economía minúscula y muy expuesta. El Banco Mundial cifra el PIB de 2025 en unos 2.390 millones de dólares y el PIB per cápita en unos 19.400 dólares; la ficha del MAEC maneja 2.230 millones según el Fondo Monetario Internacional y un crecimiento del 5,1% en 2025. La moneda es la rupia de Seychelles, con un cambio medio de 17,2 rupias por euro en 2025.</p><p>El motor es el turismo: según el MAEC aportó en 2025 en torno al 70% del PIB y el 72% de los ingresos, lo que deja al país a merced de la coyuntura internacional. El segundo pilar es la pesca, y sobre todo el atún: la industria pesquera supuso más del 90% de las exportaciones en 2025, y Victoria funciona como puerto base y centro conservero del Índico occidental. La agricultura apenas alcanza el 2,6% del PIB, de modo que casi todo lo que se come llega en barco. Los principales clientes son Emiratos Árabes Unidos, Francia y el Reino Unido; entre los proveedores, España ocupa el tercer lugar con el 7%. La deuda pública rondaba el 57,6% del PIB en 2024 y el paro es testimonial, un 2,6%, aunque una cuarta parte de la población vivía bajo el umbral de pobreza en 2018.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Viven en el archipiélago unas 122.000 personas, según el Banco Mundial para 2025, casi todas en las islas graníticas —Mahé, Praslin y La Digue— y buena parte en Victoria, la capital. La población es abrumadoramente criolla, en torno al 97%, con minorías india y china. Hay tres lenguas oficiales: el criollo seselwa, materno para más del 90% de los habitantes, el inglés y el francés; por carretera uno se entiende en inglés, lengua de la administración y del turismo. En el censo de 2022 el 74,9% se declaró cristiano —61,3% católico y 5% anglicano—, un 5,4% hindú y un 2,4% musulmán.</p><p>La cultura es de matriz africana y francesa. La moutya, danza nacida en la esclavitud, entró en 2021 en el Patrimonio Cultural Inmaterial de la Unesco, y la cocina gira en torno al pescado, el curry de coco y el ladob. El calendario mezcla lo cívico y lo católico: el 1 de febrero recuerda la abolición de la esclavitud, el 18 de junio la Constitución y el 29 de junio la independencia. La Unesco reconoce dos bienes naturales: el atolón de Aldabra, de 1982, que solo se alcanza en expedición marítima de varios días y con autorización previa de la Seychelles Islands Foundation, y el Valle de Mai de Praslin, de 1983, donde crece el coco de mer. Cerca de la mitad del territorio está protegido.</p><p>En lo práctico, ninguna nacionalidad necesita visado, pero todo viajero debe tramitar antes de volar la Autorización de Viaje electrónica, de 10,90 euros. Conviene vestir con discreción fuera de la playa y pedir permiso antes de fotografiar a la gente. El alcohol se vende con normalidad y el ramadán, que en 2027 empieza en torno al 8 de febrero, apenas altera la vida cotidiana.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Seychelles (MAEC España · Oficina de Información Diplomática · julio 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/SEYCHELLES_FICHA%20PAIS.pdf"),
    ("Recomendaciones de viaje: Seychelles (MAEC España · consultado 19-09-2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Seychelles"),
    ("Seychelles: Freedom in the World 2025 (Freedom House · 2025)", "https://freedomhouse.org/country/seychelles/freedom-world/2025"),
    ("Seychelles — History (Encyclopaedia Britannica · consultado 19-09-2026)", "https://www.britannica.com/place/Seychelles/History"),
    ("Seychelles (Encyclopaedia Britannica · consultado 19-09-2026)", "https://www.britannica.com/place/Seychelles"),
    ("Seychelles (Wikipedia en español · consultado 19-09-2026)", "https://es.wikipedia.org/wiki/Seychelles"),
    ("Seychelles (Wikipedia en inglés · censo de 2022 · consultado 19-09-2026)", "https://en.wikipedia.org/wiki/Seychelles"),
    ("2025 Seychellois general election (Wikipedia en inglés · consultado 19-09-2026)", "https://en.wikipedia.org/wiki/2025_Seychellois_general_election"),
    ("Seychelles — States Parties (UNESCO Centro del Patrimonio Mundial · consultado 19-09-2026)", "https://whc.unesco.org/en/statesparties/sc"),
    ("Aldabra Atoll — World Heritage List (UNESCO · inscrito en 1982)", "https://whc.unesco.org/en/list/185/"),
    ("Vallée de Mai Nature Reserve — World Heritage List (UNESCO · inscrito en 1983)", "https://whc.unesco.org/en/list/261/"),
    ("Aldabra (Seychelles Islands Foundation · consultado 19-09-2026)", "https://www.sif.sc/aldabra"),
    ("Travelling to Seychelles (Ministry of Foreign Affairs and the Diaspora de Seychelles · consultado 19-09-2026)", "https://mfa.gov.sc/travelling-to-seychelles/"),
    ("Seychelles Electronic Border System — Travel Authorisation (Gobierno de Seychelles · consultado 19-09-2026)", "https://seychelles.govtas.com/"),
    ("Seychelles (Reporteros Sin Fronteras · Clasificación Mundial de la Libertad de Prensa 2026)", "https://rsf.org/en/country/seychelles"),
    ("Seychelles — Data (Banco Mundial · datos de 2025 · consultado 19-09-2026)", "https://data.worldbank.org/country/seychelles"),
    ("Public holidays in Seychelles (Wikipedia en inglés · consultado 19-09-2026)", "https://en.wikipedia.org/wiki/Public_holidays_in_Seychelles"),
]

SPEC = dict(
    slug="seychelles", name="Seychelles", revision="18 sep 2026",
    sub="FUERA DE RUTA — archipiélago a 1.500 km de África, sin conexión terrestre · solo en avión · Aldabra y el Valle de Mai",
    chips=[
        ("ESTATUS", "FUERA DE RUTA. País insular sin conexión terrestre ni ferry de vehículos desde África…"),
        ("CÓMO LLEGAR", "Solo en avión al aeropuerto de Mahé (SEZ), a 11 km de Victoria…"),
        ("VISADO", "NINGUNA nacionalidad necesita visado. Pero SÍ es obligatoria la Seychelles Travel…"),
        ("VEHÍCULO", "Imposible llegar por carretera. Entrar con vehículo propio exigiría CONTENEDOR marítimo y admisión temporal…"),
        ("SEGURIDAD", "País seguro · Freedom House 2026: 81/100, LIBRE"),
        ("SEGURO", "Seguro médico OBLIGATORIO: sin él deniegan asistencia"),
        ("SALUD", "Sin malaria · fiebre amarilla solo desde zona endémica"),
        ("DRONES", "Registro SCAA desde 200 g · confiscaciones en aduana"),
        ("STARLINK", "Activo desde julio de 2026 · 4G/5G buena en las islas"),
        ("4x4", "Inútil: 453 km de carretera y se conduce por la izquierda"),
        ("A PIE", "Excelente: senderos de Mahé, Valle de Mai y La Digue"),
        ("PERRO", "MUY RESTRICTIVO. Permiso de importación previo, cuarentena obligatoria y no se admiten mascotas para estancias…"),
        ("MONEDA", "Rupia seychelense (SCR). 1 € ≈ 17,2 SCR (media 2025, Ficha País MAEC)…"),
        ("VENTANA", "Tropical, 24–30 °C todo el año. Monzón del noroeste diciembre–marzo (lluvias fuertes)…"),
    ],
    center=[-6.57, 51.09], zoom=6,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle de Mahé + salto en ferry a Praslin y La Digue",
    corridor_alt_label="Variante marítima y aérea a las islas exteriores (Bird, Denis, Silhouette, Amirantes, Alphonse, Aldabra)",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Anse_Source_d'Argent-La_Digue-Seychellen.jpg?width=1200",
    hero_credit="La Digue · Tobias Alt · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Seychelles queda fuera de la ruta de 2027 por una razón puramente geográfica: son 115 islas en pleno océano Índico, a unos 1.500 km de la costa africana (Wikipedia, 2026), sin puente, sin túnel y sin ferry de vehículos desde el continente. El único enlace regular es aéreo, al aeropuerto internacional de Mahé (SEZ), y el único puerto de entrada marítimo es Port Victoria, reservado de hecho a veleros y cruceros (Noonsite, 2025). Llevar el Grenadier o la Delica exigiría embarcarlos en contenedor de 20 o 40 pies desde Mombasa, Dar es Salaam o Durban, pagar flete de ida y vuelta, gestionar admisión temporal en aduana y recuperarlos semanas después: un coste realista de 4.000–7.000 € por vehículo solo en flete y trámites, sin contar seguro local ni estancia, para moverse por 453 km de carretera repartidos casi todos en Mahé y Praslin. No tiene sentido operativo dentro de una expedición overland. Si algún día se hace, se haría como viaje aparte: vuelo desde Nairobi, Adís Abeba, Dubái o Estambul, coche de alquiler en Mahé y ferry de pasajeros a Praslin y La Digue. Lo que habría que decidir antes es qué se hace con el perro: la entrada exige permiso previo y cuarentena, y Seychelles no acepta animales de compañía por estancias cortas, así que el viaje solo encaja dejándolo en el continente.",
    facts=[
        ("Estatus", "FUERA DE RUTA. País insular sin conexión terrestre ni ferry de vehículos desde África. Ficha informativa, no etapa."),
        ("Cómo llegar", "Solo en avión al aeropuerto de Mahé (SEZ), a 11 km de Victoria. Emirates, Qatar, Etihad, Turkish, Ethiopian, Kenya Airways, Air France y Condor."),
        ("Visado", "NINGUNA nacionalidad necesita visado. Pero SÍ es obligatoria la Seychelles Travel Authorisation previa y de pago (seychelles.govtas.com)."),
        ("Vehículo/aduana", "Imposible llegar por carretera. Entrar con vehículo propio exigiría CONTENEDOR marítimo y admisión temporal. Se conduce por la IZQUIERDA."),
        ("Seguro", "SEGURO MÉDICO DE VIAJE OBLIGATORIO. El MAEC advierte de que se deniega la asistencia médica sin seguro, incluso en emergencia vital."),
        ("Moneda", "Rupia seychelense (SCR). 1 € ≈ 17,2 SCR (media 2025, Ficha País MAEC). Euros y dólares se aceptan con frecuencia; tarjeta muy extendida."),
        ("Perro", "MUY RESTRICTIVO. Permiso de importación previo, cuarentena obligatoria y no se admiten mascotas para estancias cortas. En la práctica, inviable."),
        ("Drones", "Registro obligatorio ante la SCAA para drones de 200 g o más. Hay casos documentados de confiscación en aduana. Prohibido sobre parques y aeropuertos."),
        ("Starlink", "Operativo. Licencia aprobada el 18-02-2026 y servicio activo desde el 18-07-2026, 28.º mercado africano. Cobertura 4G/5G buena en Mahé, Praslin y La Digue."),
        ("Seguridad", "Uno de los países más seguros de África. Freedom House 2026: 81/100, LIBRE. Delincuencia menor (robos en coches y alojamientos) y piratería en aguas exteriores."),
        ("Clima", "Tropical, 24–30 °C todo el año. Monzón del noroeste diciembre–marzo (lluvias fuertes); monzón del sureste mayo–septiembre (viento y mar)."),
        ("Sanidad", "Seychelles Hospital de Victoria (211 camas, +248 4388000) como referencia nacional. SIN MALARIA. Brote de chikunguña activo desde finales de 2025."),
    ],
    alerts=[
        "Ninguna nacionalidad necesita visado, pero sin Seychelles Travel Authorisation aprobada NO se embarca: la aerolínea la exige en el mostrador.",
        "El MAEC advierte de que las autoridades de Seychelles deniegan la asistencia médica a quien no acredite seguro de viaje, incluso en emergencias vitales.",
        "No existe ferry de vehículos desde el continente africano ni entre islas: Cat Cocos e Inter Island Ferry son catamaranes SOLO de pasajeros.",
        "El atolón de Aldabra, Patrimonio Mundial desde 1982, está a 1.120 km de Mahé, no tiene pista de aterrizaje y solo se alcanza en expedición marítima con permiso de la Seychelles Islands Foundation.",
        "El 42 % del territorio es área protegida: hay tasas de desembarco en casi todas las islas (20–30 € por persona) y restricciones de acceso.",
        "El MAEC desaconseja la navegación en la Zona Económica Exclusiva y, en particular, en torno a Astove, Marie Louise, Desneufs, Boudeuse, Bancs Africains y Rémire por riesgo de piratería y narcotráfico.",
        "Legislación antidroga extremadamente dura: el FCDO avisa de penas de multa y prisión, hasta cadena perpetua, también por tenencia, con escáneres avanzados en el aeropuerto.",
        "Brote de chikunguña: más de 166 casos en viajeros europeos procedentes de Seychelles desde noviembre de 2025 (TravelHealthPro, junio de 2026). También dengue y Zika.",
        "El perro no puede desembarcar sin autorización escrita de los Servicios Veterinarios: el desembarco ilegal se castiga con multa elevada, prisión y confiscación del animal, que puede ser sacrificado (Noonsite, 2024).",
        "Seychelles NO figura en las listas del Reglamento de Ejecución (UE) 2026/636: para volver a la UE con el perro hace falta titulación antirrábica anotada ANTES de salir de la Unión.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Llegada a Mahé", "Aeropuerto Internacional (Pointe Larue) → Victoria", "~10 km · 1 día"),
        ("2 · Victoria y Mont Fleuri", "Victoria (mercado, torre del reloj) → Jardín Botánico Nacional", "~6 km · medio día"),
        ("3 · Costa norte", "Victoria → Glacis → Beau Vallon → Bel Ombre", "~25 km · 1 día"),
        ("4 · Sans Souci y las alturas", "Victoria → Sans Souci → Mission Lodge (Venn's Town) → Port Glaud", "~22 km · 1 día"),
        ("5 · Parques marinos del oeste", "Port Glaud → Port Launay → Baie Ternay (en barco)", "~10 km + travesía · 1 día"),
        ("6 · Sur de Mahé", "Port Glaud → Anse Boileau → Baie Lazare → Anse Intendance → Anse Takamaka", "~40 km · 1 día"),
        ("7 · Costa este de vuelta", "Takamaka → Anse Royale → Anse aux Pins → Victoria", "~35 km · 1 día"),
        ("8 · Travesía a Praslin", "Victoria (Inter Island Quay) → Baie Sainte Anne en Cat Cocos, 1 h 15", "~45 km de mar · medio día"),
        ("9 · Valle de Mai", "Baie Sainte Anne → Vallée de Mai → Grand'Anse Praslin", "~15 km · 1 día"),
        ("10 · Norte de Praslin", "Grand'Anse → Anse Kerlan → Anse Georgette → Anse Lazio", "~20 km · 1 día"),
        ("11 · Sureste de Praslin", "Baie Sainte Anne → Anse Marie-Louise (Fond Ferdinand)", "~8 km · medio día"),
        ("12 · Islas satélite", "Baie Sainte Anne → Curieuse, Cousin y Aride en barco", "~30 km de mar · 1–2 días"),
        ("13 · La Digue", "Baie Sainte Anne → La Passe (ferry 15 min) → L'Union Estate, Veuve, Grand Anse", "~15 km en bicicleta · 1–2 días"),
        ("14 · Islas exteriores y regreso", "Mahé → Bird / Denis / Desroches / Alphonse / Aldabra (avión o expedición marítima) → Victoria", "~100–1.150 km de aire o mar · 2–12 días"),
    ],
    offroad=[
        "No hay off-road real en Seychelles: la red rodada se limita a Mahé y Praslin y está asfaltada de punta a punta, sin autopistas salvo el tramo doble Victoria-aeropuerto; el resto son carreteras estrechas de montaña con curvas de horquilla, ángulos muertos y precipicios sin quitamiedos (FCDO, actualizado el 21 de enero de 2026).",
        "Las guías locales son explícitas: un turismo automático basta para todas las carreteras principales y para la inmensa mayoría de los accesos a playa; el 4x4 no aporta nada y sí estorba en aparcamientos y cruces estrechos.",
        "Se circula por la IZQUIERDA, con límites de 40 km/h en zona urbana, 65 km/h en carretera general y 80 km/h en el tramo doble del aeropuerto, con radares en la vía Victoria-aeropuerto y junto a los colegios.",
        "Lo más exigente que hay es la subida de Sans Souci, que cruza el Parque Nacional del Morne Seychellois hasta unos 500 m, y el desvío corto, estrecho y muy empinado que sube a Mission Lodge: asfalto, pero en primera y con paciencia si viene otro de frente.",
        "El único tramo que se puede llamar pista es el hormigón de 1,7 km que baja de Quatre Bornes a Anse Intendance; es firme y transitable con cualquier coche.",
        "Las zonas vetadas no son off-road sino áreas protegidas: los parques nacionales marinos (Ste. Anne, Curieuse, Port Launay, Baie Ternay, Île Cocos) prohíben fondear fuera de las zonas señaladas, la pesca, el fusil submarino y la recogida de conchas, y Aldabra exige autorización escrita de la Seychelles Islands Foundation para cualquier embarcación.",
        "En La Digue no hay alquiler de coches para turistas: se circula en bicicleta y en carros de bueyes, así que ningún vehículo de la expedición tendría sentido allí.",
        "Los dos 4x4 de la expedición NO pueden llegar: no existe transbordador de vehículos entre el continente africano y Seychelles, y el Cat Cocos entre islas sólo admite pasajeros, equipaje y bicicletas (100 SCR por bici y trayecto).",
    ],
    senderismo=[
        "Copolia (Mahé, Parque Nacional del Morne Seychellois): la más popular, sube a una losa de granito con vista sobre Victoria y Ste. Anne; 100 SCR para no residentes mayores de 12 años, horario 8:00-16:00, plantas carnívoras en la cima.",
        "Morne Blanc (Mahé): subida corta y fuerte desde la carretera de Sans Souci hasta un balcón sobre la costa oeste y las islas; es uno de los ocho itinerarios oficiales del parque.",
        "Trois Frères (Mahé): tres cumbres con panorámica sobre Victoria; 150 SCR para no residentes, dentro del mismo parque.",
        "Anse Major (Mahé): desde Bel Ombre, unas 3 horas ida y vuelta por la ladera hasta una cala sin carretera, antiguo terreno de vainilla y canela; 150 SCR.",
        "Morne Seychellois (Mahé): la cumbre del país, 905 m; el sendero SÓLO abre de 8:00 a 12:00 y cuesta 250 SCR, y es la ruta más exigente de las ocho oficiales.",
        "Mare aux Cochons y Dans Gallas (Mahé): humedal de altura con ruinas de una destilería de canela y travesía por las plantaciones forestales; itinerarios oficiales del parque, más largos y menos transitados.",
        "Valle de Mai (Praslin): varios circuitos llanos de entre 1,5 y 4 km por el palmeral, con folleto y mapa gratuitos en la entrada.",
        "Fond Ferdinand (Praslin): unos 2 km con guía obligatorio, de 1,5 a 2,5 horas, dificultad fácil-moderada, hasta el mirador de 360 grados de Zimbabwe Point.",
    ],
    acampada=[
        "ACAMPAR NO ES UNA OPCIÓN en Seychelles: no existe ninguna red de campings ni de áreas de autocaravana en Mahé, Praslin ni La Digue, y no hemos encontrado ninguna web oficial que regule la acampada libre.",
        "En los foros de viajeros, los moderadores locales de Tripadvisor afirman que acampar en la playa está terminantemente prohibido; no hemos localizado el texto legal que lo respalde, así que queda como dato por confirmar con la Seychelles Tourism Board.",
        "El sistema de entrada refuerza de hecho esa prohibición, y esto SÍ está en fuente oficial: la Immigration and Civil Status exige alojamiento confirmado, billete de salida y fondos suficientes para expedir el Permiso de Visitante, y el Ministerio de Exteriores pide la reserva de alojamiento ya en la solicitud de la Travel Authorisation (ics.gov.sc y mfa.gov.sc). Llegar sin dónde dormir no es una opción.",
        "Tampoco hay acampada dentro de los espacios protegidos: el Parque Nacional del Morne Seychellois y los parques marinos cierran a las 16:00 y 17:00 respectivamente y no admiten pernocta, y en Aldabra la Seychelles Islands Foundation no facilita alojamiento en tierra (hay que dormir a bordo).",
        "Lo más parecido a un campamento son los eco-camps de lujo de las islas exteriores, tipo Cosmoledo, que son alojamiento reservado y de precio alto, no acampada libre.",
        "La alternativa real y barata son los self-catering y guesthouses: en Beau Vallon y La Digue hay apartamentos desde unos 50 euros la noche según los propios foros locales.",
        "iOverlander y Tracks4Africa no tienen cobertura útil del país: al no haber acceso terrestre, no hay registros de overlanders, y las búsquedas no devolvieron puntos verificables (por confirmar).",
        "Si algún día se planteara el viaje, la fórmula lógica sería vehículo de alquiler pequeño en Mahé, guesthouse en Beau Vallon o Victoria, ferry a Praslin y bicicleta en La Digue.",
    ],
    visado=[
        "SIN VISADO para todas las nacionalidades, españoles incluidos. A la llegada se expide un Visitor's Permit gratuito, inicialmente de 3 meses, prorrogable hasta 12 meses en total.",
        "OBLIGATORIA la Seychelles Travel Authorisation (autorización electrónica previa), tramitada en el portal oficial https://seychelles.govtas.com/ antes de embarcar.",
        "Coste según la urgencia del trámite: 10 € en modalidad estándar (24 h), 30 € premium (6 h) y 70 € exprés (60 min). Se paga con tarjeta.",
        "Se solicita hasta 30 días antes del viaje. Hay que aportar pasaporte válido, billete de vuelta o continuación, reserva de alojamiento y prueba de fondos suficientes.",
        "La autorización llega por correo electrónico y se presenta tanto en el embarque como en el control de entrada. Sin ella hay penalización a la llegada.",
        "No hay fronteras terrestres: el concepto de validez en paso terrestre NO APLICA. Los veleros también necesitan Travel Authorisation antes de entrar en Port Victoria.",
    ],
    fronteras_rows=[
        ("Aeropuerto internacional", "Seychelles International Airport (SEZ), Mahé", "ABIERTO. Único punto de entrada aéreo internacional, 11 km al sureste de Victoria. Emirates, Qatar, Etihad, Turkish, Ethiopian, Kenya Airways, Air France y Condor. Fuente: Wikipedia, 2026."),
        ("Puerto de entrada marítimo", "Port Victoria, Mahé", "ABIERTO y ÚNICO. Noonsite (2025): «Port Victoria on Mahé is the only port of entry and exit». Contacto con Port Control por VHF canal 12 dos horas antes, pabellón Q y despacho a bordo."),
        ("Ferry interinsular", "Cat Cocos · Inter Island Quay (Victoria) – Baie Sainte Anne (Praslin) – La Passe (La Digue)", "OPERATIVO, SOLO PASAJEROS. Mahé–Praslin 1 h 15 min desde 56 €; Mahé–La Digue 1 h 45 min desde 68 €. NO admite vehículos (seyferry.com, horario vigente hasta 31-12-2027)."),
        ("Ferry interinsular", "Inter Island Ferry / Cat Rose, Praslin – La Digue", "OPERATIVO, SOLO PASAJEROS. Travesía corta entre Baie Sainte Anne y La Passe. No transporta turismos; en La Digue el transporte local es bicicleta y carro de bueyes."),
        ("Vuelo interinsular", "Air Seychelles, Mahé (SEZ) – Aeropuerto de Praslin", "OPERATIVO. Puente aéreo de unos 15 minutos, el enlace doméstico principal. Hay catorce aeródromos en el país, solo seis asfaltados (Wikipedia, 2026)."),
        ("Acceso restringido", "Atolón de Aldabra (Patrimonio Mundial, 1982)", "SOLO CON PERMISO de la Seychelles Islands Foundation. A 1.120 km de Victoria, sin pista de aterrizaje ni instalaciones de desembarco. Unos 900 visitantes al año, en crucero o barco de expedición."),
        ("Paso terrestre", "No existe ninguno", "NO APLICA. Seychelles no tiene frontera terrestre con ningún país. Cualquier planificación overland termina en el puerto de embarque continental."),
        ("Entrada de vehículo propio", "Terminal de contenedores de Port Victoria", "POR CONFIRMAR el régimen exacto de admisión temporal para turistas. La vía sería contenedor desde Mombasa, Dar es Salaam o Durban. La Seychelles Revenue Commission gestiona la aduana."),
    ],
    vehiculos=[
        "NO SE PUEDE LLEGAR POR CARRETERA. Ni el Ineos Grenadier ni la Mitsubishi Delica pueden alcanzar Seychelles por sus propios medios: el archipiélago está a 1.500 km del continente.",
        "La única forma de llevar un vehículo propio es el CONTENEDOR marítimo (20 o 40 pies) desde un puerto de África oriental o austral, con flete de ida y vuelta y despacho de admisión temporal en Port Victoria.",
        "Se conduce por la IZQUIERDA (Wikipedia, Transport in Seychelles). Vehículo español con volante a la izquierda: adelantamientos incómodos y ángulo muerto en carreteras estrechas de montaña.",
        "La red es de 453 km, de los que unos 400 están asfaltados, prácticamente toda en Mahé y Praslin. En La Digue apenas hay coches: bicicleta, carro de bueyes y algún vehículo autorizado.",
        "PERMISO INTERNACIONAL DE CONDUCCIÓN EXIGIDO: los consejos de viaje del Gobierno de Canadá, actualizados el 9 de septiembre de 2026, indican que se requiere permiso internacional para conducir en Seychelles. Hay que llevarlo junto al permiso español en vigor.",
        "El FCDO advierte de carreteras estrechas, sinuosas y de montaña, sin quitamiedos, con desagües sin tapar, baches súbitos tras la lluvia y conducción errática asociada al alcohol.",
        "Seguro: la Carta Verde europea NO cubre Seychelles y no existe sistema regional aplicable (ni Carte Brune CEDEAO, ni Carte Rose CEMAC, ni COMESA Yellow Card operativo para el archipiélago). Habría que contratar seguro local.",
        "Alternativa sensata: alquilar en Mahé. El parque de alquiler es amplio, con volante a la derecha, seguro local incluido y sin ningún trámite aduanero.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autoridad competente: Seychelles Civil Aviation Authority (SCAA), con sección específica de operaciones con drones y portal de registro (scaa.sc).",
        "REGISTRO OBLIGATORIO de todo dron de 200 g o más antes de operarlo. No se exige licencia de piloto ni a aficionados ni a visitantes; solo los operadores gubernamentales la necesitan.",
        "Prohibido volar cerca de aeropuertos y helipuertos sin autorización, sobre zonas urbanas densas, propiedad privada, eventos públicos, de noche y sobre infraestructura sensible. Siempre dentro del campo visual.",
        "Con el 42 % del territorio protegido, los parques nacionales y reservas marinas quedan de hecho vetados. POR CONFIRMAR el procedimiento concreto de permiso en el Valle de Mai y en Aldabra, que gestiona la Seychelles Islands Foundation.",
        "Riesgo real de confiscación en el control aduanero del aeropuerto de Mahé: conviene declarar el aparato, llevar impreso el registro SCAA y asumir que puede quedar retenido hasta la salida.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Starlink ENTRÓ EN SERVICIO el 18 de julio de 2026, convirtiendo a Seychelles en el 28.º mercado africano del operador. La licencia de proveedor de internet la aprobó el Gabinete presidido por Patrick Herminie el 18 de febrero de 2026, sujeta a condiciones específicas (Space in Africa, julio de 2026).",
        "POR CONFIRMAR las tarifas locales de kit y suscripción: no se publicaron con el lanzamiento. Space in Africa apunta que la asequibilidad es menos problemática que en el continente por tratarse de una economía de renta alta, con un 87 % de uso de internet en 2025.",
        "Cobertura móvil terrestre buena en las islas interiores: los dos operadores son Cable & Wireless Seychelles y Airtel Seychelles, con SIM turística disponible en el aeropuerto de Mahé.",
        "En las islas exteriores (Aldabra, Astove, Alphonse, Farquhar) no hay red móvil: la comunicación es satelital y depende del barco.",
        "POR CONFIRMAR si el uso marítimo de Starlink en aguas de Seychelles requiere alguna autorización adicional de la autoridad de telecomunicaciones.",
    ],
    perro_intro=[
        "ENTRADA MUY RESTRICTIVA. El organismo competente es la Animal Biosecurity Section de la Border Control and Support Division (Ministry of Fisheries, Agriculture and Blue Economy), en Maison Collet, Palm Street, Victoria: +248 4672300, info@mofbe.gov.sc. Exige PERMISO DE IMPORTACIÓN PREVIO tramitado antes del embarque en un procedimiento de cinco pasos.",
        "Noonsite (actualización de enero de 2024) recoge que Seychelles «no acepta mascotas para periodos inferiores a seis meses»: para un viaje turístico la entrada es, en la práctica, INVIABLE.",
        "CUARENTENA OBLIGATORIA A LA LLEGADA para todo animal vivo, en la instalación de biosseguridad designada: mínimo 14 días desde países con rabia controlada y hasta 180 días desde países de alta incidencia. La tasa estándar es de unas 1.000 SCR por dos semanas, con permiso, recogida, transporte y estancia incluidos.",
        "Requisitos del animal: edad mínima de 16 semanas, microchip, vacunación antirrábica entre 30 días y 12 meses antes de la entrada, titulación de anticuerpos antirrábicos y tratamiento antiparasitario en las 48 horas previas al viaje. Toda vacuna, al menos 2 semanas antes de la salida.",
        "RAZAS: hay un listado (Anexo 1 del documento veterinario) de más de cuarenta razas —rottweiler, pastor alemán, pit bull y otras— que exigen esterilización quirúrgica previa a la entrada.",
        "VUELTA A LA UE: Seychelles NO aparece en las listas del Reglamento de Ejecución (UE) 2026/636 (sí Mauricio, por ejemplo). El regreso se hace por la VÍA A del Reglamento Delegado (UE) 2026/131: titulación antirrábica igual o superior a 0,5 UI/ml en laboratorio autorizado, ANOTADA EN EL PASAPORTE ANTES de salir de la Unión. Si se hace ya fuera, el MAPA avisa de que la entrada solo se autoriza 90 días después de la extracción de sangre. La llegada debe producirse por un Punto de Entrada de Viajeros (PEV) autorizado, declarando el animal a la Guardia Civil.",
        "Si el perro llega en velero, NO PUEDE DESEMBARCAR sin autorización escrita de la Sección Veterinaria. El desembarco ilegal acarrea multa elevada, prisión y confiscación del animal, que puede ser sacrificado.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "SEGURO MÉDICO OBLIGATORIO. El MAEC es explícito: las autoridades de Seychelles deniegan la asistencia médica a quien no acredite seguro de viaje, incluso en emergencias vitales. Es el requisito sanitario más importante del país.",
        "FIEBRE AMARILLA: certificado exigido solo a viajeros procedentes de zonas endémicas. Quien llegue directo desde España no lo necesita; quien venga de África oriental o central, SÍ. También se exige certificado de poliomielitis a procedentes de zonas endémicas.",
        "NO HAY MALARIA en Seychelles: es uno de los pocos países africanos libres de paludismo, así que no hace falta profilaxis.",
        "BROTE DE CHIKUNGUÑA ACTIVO: TravelHealthPro registraba en junio de 2026 más de 166 casos en viajeros europeos procedentes de Seychelles desde noviembre de 2025. Circulan además dengue y Zika, todos por mosquito de picadura diurna.",
        "Vacunas recomendadas: tétanos-difteria-polio al día, hepatitis A y B, fiebre tifoidea según exposición, y las vacunas de dengue y chikunguña donde estén indicadas. Riesgo de rabia bajo, evitando el contacto con murciélagos.",
        "Sanidad muy centralizada: el Seychelles Hospital de Mont Fleuri (Victoria, 211 camas) es el centro terciario de referencia nacional, teléfono +248 4388000. Completan la red el hospital de Baie Sainte Anne (Praslin), el de Anse Royale (sur de Mahé) y St. Mary's, más centros de salud primaria repartidos por las islas. Fuera de Mahé los medios son limitados y una urgencia grave obliga a evacuación.",
        "Agua y alimentos: higiene habitual de viaje. La red de Mahé es de calidad razonable, pero en islas menores conviene el agua embotellada para beber.",
    ],
    seguridad_intro="Seychelles es de los países más seguros de África y uno de los de mayor renta per cápita del continente: 81 sobre 100 y categoría LIBRE en Freedom House 2026, con alternancia democrática real —la oposición ganó por primera vez en 2020 con Wavel Ramkalawan y el poder volvió a cambiar de manos en octubre de 2025 con Patrick Herminie—. No hay terrorismo, ni conflicto, ni secuestro. Los riesgos son otros: robos de oportunidad, corrientes marinas, carreteras de montaña y, mar adentro, piratería y narcotráfico.",
    seguridad=[
        "Freedom House 2026: 81/100, estatus LIBRE (35/40 en derechos políticos, 46/60 en libertades civiles). Elecciones libres, oposición con opciones reales de gobernar y alternancia efectiva en 2020 y 2025.",
        "El Gobierno de Canadá, en su aviso actualizado el 9 de septiembre de 2026, sitúa Seychelles en el nivel más bajo: «tomar las precauciones de seguridad habituales», el mismo que se aplicaría en casa. Sin zonas vetadas en tierra, sin terrorismo y sin necesidad de escoltas ni permisos especiales.",
        "El MAEC no desaconseja el viaje a las islas interiores. La única zona de riesgo alto que señala es la NAVEGACIÓN en la Zona Económica Exclusiva, con mención expresa a Astove, Marie Louise, Desneufs, Boudeuse, Bancs Africains y Rémire.",
        "Riesgo medio, con vigilancia reforzada, en las aguas de las islas interiores (Mahé, Praslin, La Digue, Silhouette, Frégate) y en el archipiélago del suroeste por tráficos ilícitos.",
        "DELINCUENCIA COMÚN al alza: el FCDO avisa de allanamientos, robos con fuerza y hurtos de oportunidad, sobre todo en coches aparcados, alojamientos y playas. Precaución en Beau Vallon, en las calles traseras de Victoria y en zonas aisladas de noche.",
        "DROGAS: tolerancia cero. Multas y penas de prisión que pueden llegar a cadena perpetua, también por tenencia, incluido el cannabis, con escáneres avanzados en el aeropuerto.",
        "PIRATERÍA: el riesgo regional persiste en el Índico occidental, especialmente hacia la costa somalí. Cualquier travesía a las islas exteriores debe consultar los avisos marítimos vigentes.",
        "MAR: corrientes de retorno fuertes. La costa noroeste es peligrosa entre diciembre y marzo y la sureste entre mayo y septiembre; hay ahogamientos registrados y Beau Vallon tiene corrientes con mar gruesa.",
        "METEOROLOGÍA: lluvias torrenciales e inundaciones entre diciembre y febrero, con desprendimientos en las carreteras de montaña de Mahé.",
    ],
    agua=[
        "El agua corriente de Mahé y Praslin procede de la red pública y es apta para uso general (ducha, lavado, llenado de depósitos) sin tratamiento especial.",
        "Para beber, el criterio habitual del viajero es agua embotellada, sobre todo fuera de Mahé y en alojamientos pequeños de La Digue e islas menores.",
        "Seychelles sufre ESTRÉS HÍDRICO estacional: durante el monzón del sureste (mayo a septiembre) las reservas bajan y ha habido restricciones de suministro. POR CONFIRMAR si hay racionamiento vigente en 2026.",
        "Buena parte del agua de las islas menores procede de desalación y de recogida de lluvia: el consumo es caro y conviene ser austero, en especial con depósitos grandes.",
        "No aplica la logística overland de llenado en gasolineras y campings: en Seychelles no hay red de campings ni áreas de servicio para autocaravanas.",
    ],
    combustible=[
        "Gasolina 95: 20,50 SCR por litro, equivalente a 1,26 € o 1,50 USD por litro, dato de GlobalPetrolPrices a 9 de febrero de 2026. Es un 15 % más cara que la media mundial.",
        "Gasóleo: 20,54 SCR por litro, equivalente a 1,27 € o 1,48 USD por litro, dato de GlobalPetrolPrices a 8 de diciembre de 2025. Prácticamente el mismo precio que la gasolina.",
        "Todo el combustible es IMPORTADO y se descarga en Port Victoria, que además funciona como puerto de aprovisionamiento (bunkering) de la flota atunera del Índico.",
        "Red de estaciones suficiente en Mahé y Praslin, concentrada en Victoria y en los ejes principales. En La Digue y en las islas menores la oferta es testimonial o inexistente.",
        "No hay racionamiento conocido ni problemas de calidad reportados. La autonomía nunca es un problema real: la isla mayor tiene poco más de 400 km de carretera asfaltada.",
    ],
    experiencias_intro="No existen relatos de overlanders en Seychelles porque no se puede llegar conduciendo: el archipiélago no aparece en las rutas de Tracks4Africa ni en los diarios de la Cairo–Ciudad del Cabo. Lo que sí hay es literatura de navegantes y de viajeros de isla, y de ahí sale lo aprovechable.",
    experiencias=[
        "Port Victoria es la única puerta marítima: Noonsite, en su guía de despacho actualizada en 2025, es tajante: «Port Victoria on Mahé is the only port of entry and exit». Se contacta con Port Control por VHF canal 12 dos horas antes, se entra con pabellón Q y sanidad, aduana e inmigración suben a bordo en el fondeadero de cuarentena. Aduana y puerto trabajan de 08:00 a 12:00 y de 13:00 a 15:00, de lunes a viernes.",
        "Moverse entre islas con barco propio exige permiso: Noonsite (2025) explica que los veleros de 10 metros o más necesitan aprobación de salida de la SMSA con dos días de antelación y una tasa de 200 rupias para visitar las islas interiores o exteriores. A eso se suman tasas de desembarco de 20 a 30 euros por persona en casi todas las islas, consecuencia de que el 42 % del país es área protegida.",
        "El perro se queda a bordo: la ficha de mascotas de Noonsite, revisada en enero de 2024, deja claro que ningún animal puede pisar tierra sin permiso escrito de la Sección Veterinaria y que el desembarco ilegal acarrea multa fuerte, prisión y confiscación del animal, que puede ser sacrificado. Añade el dato que lo cambia todo para un viaje turístico: el país no acepta mascotas para estancias inferiores a seis meses.",
        "Aldabra no es un destino, es una expedición: recibe unos 900 visitantes al año y no tiene pista de aterrizaje ni instalaciones de desembarco, así que solo se llega en crucero o barco de expedición con autorización previa. Está a 1.120 km de Victoria, de hecho 630 km más cerca de la costa africana que de Mahé, y la Seychelles Islands Foundation lo gestiona desde 1979 con doce personas en Picard.",
        "El ferry no es un ferry de coches: la web oficial de Cat Cocos (seyferry.com, horario vigente hasta diciembre de 2027) describe catamaranes rápidos exclusivamente de pasajeros. Mahé–Praslin son 1 h 15 min desde 56 euros y Mahé–La Digue 1 h 45 min desde 68 euros, con 25 kg de equipaje incluido en económica. Quien cuente con cruzar el vehículo a Praslin se lleva un chasco.",
        "El dron puede quedarse en la aduana: las recopilaciones de drone-laws.com para 2026 confirman que volar es legal, que la SCAA exige registro a partir de 200 gramos y que no se pide licencia al visitante, pero recogen también el testimonio de un viajero al que le confiscaron el aparato en la aduana. La lectura práctica es que cumplir la norma no garantiza pasar el control.",
        "El seguro no es un consejo, es la puerta: la ficha de recomendaciones del MAEC advierte de que las autoridades de Seychelles deniegan la atención médica a quien no acredite seguro de viaje, «incluso en emergencias vitales». Es la clase de detalle que en el resto de África se da por hecho y que aquí conviene llevar impreso.",
        "La carretera de Mahé sorprende: el FCDO describe vías estrechas, sinuosas y de montaña, sin quitamiedos, con desagües abiertos en la cuneta y baches que aparecen tras la lluvia, más conducción errática asociada al alcohol. Con volante a la izquierda y circulación por la izquierda, la combinación pide calma en los adelantamientos.",
        "La conectividad dejó de ser un problema en 2026: la Seychelles News Agency y Space in Africa informaron en julio de 2026 de la entrada en servicio de Starlink en el país, confirmada por el vicepresidente. Sumado a la cobertura 4G y 5G de Cable & Wireless y Airtel en las islas interiores, el viajero que quiera trabajar desde Mahé o Praslin no necesita nada especial.",
        "Chikunguña, el riesgo real de 2026: TravelHealthPro registraba en junio de 2026 más de 166 casos confirmados en viajeros europeos que regresaban de Seychelles desde noviembre de 2025. En un país sin malaria y con sanidad razonable, el mosquito de picadura diurna es la amenaza sanitaria que más está afectando a los visitantes.",
    ],
    pendientes=[
        ("Validez del certificado sanitario del perro", "Obtener de la Animal Biosecurity Section (+248 4672300, info@mofbe.gov.sc) el plazo máximo en días entre la firma del certificado veterinario y el embarque."),
        ("Entrada del perro para estancia turística", "Confirmar con la Animal Biosecurity Section si existe algún supuesto por debajo de seis meses o si sigue vigente la prohibición que recoge Noonsite (2024)."),
        ("Condiciones veterinarias en dominio oficial", "Localizar el documento VS/REG/05/11/01 o su sustituto alojado en un dominio .gov.sc, para no depender de un repositorio de terceros."),
        ("Admisión temporal de vehículo extranjero", "Obtener de la Seychelles Revenue Commission el régimen aplicable a un turismo matriculado fuera llegado en contenedor: documento exigido, fianza, plazo y coste."),
        ("CPD en Seychelles", "Confirmar con el RACE o con la AIT/FIA si el carnet de passages se acepta en Port Victoria, dado que el país no tiene club emisor propio."),
        ("Tarifas de la Travel Authorisation", "Reconfirmar los importes de 10, 30 y 70 euros en el propio portal seychelles.govtas.com antes de pagar: la FAQ oficial abierta no mostraba el importe."),
        ("Tarifas de Starlink en Seychelles", "Consultar starlink.com para el país y anotar precio de kit y suscripción, y si el plan Roam funciona sin contrato nacional."),
        ("Drones en áreas protegidas y procedimiento SCAA", "La página scaa.sc/index.php/drone-operations devuelve error 404. Localizar la sección vigente de la SCAA con el formulario de registro y el régimen en parques nacionales."),
        ("Restricciones de agua 2026", "Confirmar con la Public Utilities Corporation si hay racionamiento o restricciones de suministro durante el monzón del sureste."),
        ("Dirección exacta del consulado honorario de España", "Obtener del MAEC la dirección postal completa del consulado honorario en Victoria: solo consta el teléfono +248 4 303300."),
        ("Coste real del flete en contenedor", "Pedir cotización a una naviera para un 4x4 en contenedor de 20 pies Mombasa–Victoria ida y vuelta, para fijar el coste orientativo del párrafo de decisión."),
        ("Coordenadas de puntos urbanos", "Verificar en Google Maps las coordenadas del consulado honorario, la oficina de biosseguridad, los hospitales de Praslin y Anse Royale y los puntos de combustible y agua, hoy aproximadas."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las páginas citadas, todas abiertas en esa fecha. Los datos de burocracia (tarifas de la Travel Authorisation, condiciones veterinarias, precios de combustible y ferry) cambian sin aviso: hay que reconfirmarlos antes de comprar nada. Esto es una herramienta de planificación, no una autorización ni un documento oficial de viaje.",
    emergency="EMERGENCIA CONSULAR 24 h (Embajada de España en Adís Abeba, competente para Seychelles): +251 911 219 403. Consulado Honorario de España en Victoria: +248 4 303300. POLICÍA: 999. Seychelles Hospital de Victoria, urgencias y ambulancia: +248 4388000 (también centralita del Ministerio de Salud). BOMBEROS: POR CONFIRMAR el número directo, que el MAEC no publica en su ficha. Centralita de la Embajada en Adís Abeba +251 929 136 159; sección consular +251 929 136 161; emb.addisabeba.consu@maec.es.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

# -*- coding: utf-8 -*-
"""Sudán del Sur — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Sudán del Sur está EXCLUIDO POR PROTOCOLO: independiente desde 2011, guerra civil de 2013 a 2018, acuerdo de paz incumplido, elecciones aplazadas una y otra vez, violencia intercomunitaria y crisis humanitaria agravada por la guerra de Sudán y el corte del oleoducto. El MAEC desaconseja viajar. La app solo tiene una ficha stub: créala entera con el formato del piloto de Túnez. La ficha es INFORMATIVA. Clave positiva que hay que documentar bien: en 2023-2024 se confirmó por censo aéreo la mayor migración terrestre de mamíferos del mundo entre Boma y Badingilo, con unos seis millones de antílopes, un dato reciente y verificable. Cada PDI tiene que decir en qué estado está y qué dice el MAEC, y si un PDI no tiene fuente sólida, dilo en vez de rellenarlo.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/sudan-del-sur.json y audit/pdi/sudan-del-sur.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Yuba · mausoleo de John Garang, mercado Konyo Konyo y el Nilo Blanco", cat="Ciudad · servicios", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=4.8489247, lon=31.5827439,  # Google Maps: Dr John Garang Mausoleum (Yuba)
        desc="Capital y única base logística real del país: aduana, embajadas, combustible, talleres y los pocos alojamientos con muro y guardia. El mausoleo de John Garang, líder del SPLM muerto en accidente de helicóptero el 30 de julio de 2005 —seis meses después de firmar el acuerdo de paz de Nairobi del 9 de enero de 2005—, preside la plaza donde se declaró la independencia. A un paso, Konyo Konyo, el mayor mercado del país, y el puente sobre el Nilo Blanco. AVISO: el MAEC desaconseja el viaje bajo cualquier circunstancia y describe atracos a mano armada en Yuba a cualquier hora.",
        dog_note="El mausoleo es recinto conmemorativo oficial con guardia militar y el mercado es un hervidero: con perro solo el paseo por la orilla del Nilo, y siempre atado.",
        visit={
            "why": "Es donde se resuelve todo —visado, permisos de movimiento, gasóleo, repuestos— y donde se entiende de un vistazo la historia reciente del país más joven del mundo.",
            "see": "La plaza y el mausoleo de Garang, el bullicio de Konyo Konyo y la orilla del Nilo Blanco junto al puente de Yuba, puerto fluvial y término sur de la navegación por el Nilo.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Se llega por la A43 asfaltada desde Nimule (192 km, rehabilitada por USAID entre 2007 y 2012). Aparcamiento para dos 4x4 solo dentro de recintos vallados (hoteles y compounds de ONG); en la calle, nunca sin vigilancia. Horarios y entrada del mausoleo: POR CONFIRMAR, no hay web oficial. El pin marca el mausoleo, que es el objeto navegable; el mercado y el puente están a menos de 3 km.",
            "when": "Estación seca, de diciembre a marzo; en la ciudad, salir solo de día y evitar desplazarse tras el anochecer.",
            "skip": "Descártalo entero mientras siga vigente el aviso del MAEC de abandono inmediato del país.",
        },
        links=[
            {"label": "Yuba (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Juba"},
            {"label": "MAEC · recomendaciones de viaje Sudán del Sur", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"},
            {"label": "John Garang (Wikipedia)", "url": "https://en.wikipedia.org/wiki/John_Garang"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Juba_City.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Juba_City.jpg",
                "credit": "Rigan123 · CC BY-SA 4.0",
                "caption": "Panorámica de Yuba.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sudan_Juba_bridge.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sudan_Juba_bridge.jpg",
                "credit": "User DEMOSH on flickr.com · CC BY 2.0",
                "caption": "El puente sobre el Nilo Blanco en Yuba.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pupils_at_Saint_Pupil's_Primary_School_in_Juba,_South_Sudan_attending_a_contest_in_2022.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pupils_at_Saint_Pupil's_Primary_School_in_Juba,_South_Sudan_attending_a_contest_in_2022.jpg",
                "credit": "Bida thomas · CC BY-SA 4.0",
                "caption": "Escolares en Yuba.",
            },
        ],
    ),
    dict(
        n=2, name="Parque nacional de Nimule · elefantes y los rápidos de Fula", cat="Naturaleza", prio="Alta",
        dog="prohibido", time="medio día",
        lat=3.6399611, lon=32.1064668,  # Google Maps: Nimule National Park
        desc="410 km² declarados en 1954 —el parque más antiguo del país— pegados a la frontera de Uganda, en el codo donde el Nilo entra en Sudán del Sur. Es el más accesible de todos: la A43 asfaltada pasa por la puerta. Su fama son los elefantes y los rápidos de Fula, a unos 6,5 km al norte de la ciudad de Nimule, donde el Gobierno lleva años queriendo levantar su principal central hidroeléctrica, proyecto parado por la inseguridad desde 2013. ADVERTENCIA: el corredor Yuba–Nimule ha sufrido emboscadas.",
        dog_note="Parque nacional con elefantes, hipopótamos y cocodrilos del Nilo; los perros no entran en parques nacionales y aquí serían además un imán para el conflicto.",
        visit={
            "why": "Es el único parque del país al que se llega por asfalto y el que concentra los últimos elefantes del sur, con el Nilo recién entrado desde Uganda como telón.",
            "see": "Elefantes y ribera del Nilo Blanco, y los rápidos de Fula (3.67312 N, 31.97481 E) corriente arriba del pueblo.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). A pie de la A43 Yuba–Nimule, asfaltada, 192 km desde Yuba. Aparcamiento para dos 4x4 sin problema en la sede del parque, que es una explanada de tierra. Tarifas y horarios oficiales: POR CONFIRMAR, no hay web del parque. El MAEC señala que todas las carreteras presentan riesgos extremos, con ataques y emboscadas diarias, y en 2017 hubo una emboscada mortal en la Nimule–Yuba. El pin marca la sede/entrada del parque, no el centroide.",
            "when": "Estación seca, de diciembre a marzo; a primera hora de la mañana para ver fauna en la orilla.",
            "skip": "Si vais sin guarda armado del parque o si el tramo Yuba–Nimule está cerrado por incidentes.",
        },
        links=[
            {"label": "Parque nacional de Nimule (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Nimule_National_Park"},
            {"label": "Rápidos de Fula (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Fula_Rapids"},
            {"label": "Nimule (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Nimule"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_view_of_River_Nile_from_REI_residential_areas_in_nimule_Game_Park.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_view_of_River_Nile_from_REI_residential_areas_in_nimule_Game_Park.jpg",
                "credit": "Bior ajang · CC BY-SA 4.0",
                "caption": "El Nilo desde el parque de Nimule.",
            },
        ],
    ),
    dict(
        n=3, name="Montes Imatong y monte Kinyeti · el techo del país", cat="Naturaleza", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=4.026986, lon=32.775681,  # Google Maps: Katire (acceso a los montes Imatong)
        desc="El monte Kinyeti, 3.187 m, es el PUNTO MÁS ALTO DE SUDÁN DEL SUR, en los Imatong, a unos 190 km al sureste de Yuba y a caballo de la frontera ugandesa. Por encima de los 1.000 m empieza el bosque de montaña con podocarpos, crotones y albizias que llega hasta los 2.900 m; la reserva forestal central de los Imatong, 1.100 km², data de 1952. El acceso rodado termina en Katire, antigua estación forestal británica. A partir de ahí, solo a pie y con guía local.",
        dog_note="Trek de 3–4 días por bosque cerrado que se abre a machete, sin agua garantizada cada tramo y con reserva forestal de por medio; no es terreno para el perro.",
        visit={
            "why": "Es el techo del país y el único bosque nuboso de Sudán del Sur, un mundo aparte del calor de la sabana.",
            "see": "Bosque montano con podocarpos hasta los 2.900 m, la cumbre de Kinyeti a 3.187 m y Gilo, aldea de la ladera norte donde los británicos pusieron un puesto de observación hacia 1929 a unos 2.200 m.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Desde Torit, pista de tierra recientemente nivelada hasta Katire, 1,5–2 horas en 4x4 según SummitPost; desde Katire, solo senderos. Hay sitio de sobra para dos 4x4 en el campamento de Katire. SummitPost indica que el permiso de montaña se saca en el Ministerio de Fauna, Conservación y Turismo en Torit, junto al mercado principal. Ida y vuelta a la cumbre: 3 días para gente en forma, 4 para la mayoría. El pin marca Katire, el final del recorrido en coche.",
            "when": "De noviembre a marzo, en seco; con lluvia las pistas se vuelven intransitables.",
            "skip": "Si no conseguís guía local con machete y el permiso de Torit, o si no podéis dejar los coches custodiados varios días en Katire.",
        },
        links=[
            {"label": "Montes Imatong (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Imatong_Mountains"},
            {"label": "Monte Kinyeti (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Kinyeti"},
            {"label": "Mount Kinyeti · SummitPost (ruta y permisos)", "url": "https://www.summitpost.org/mount-kinyeti/761688"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mount_Kinyeti.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mount_Kinyeti.jpg",
                "credit": "AIMikhin · CC BY-SA 3.0",
                "caption": "Panorámica desde la cima del monte Kinyeti.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Equatoria_(South_Sudan)_banner_Mount_Kinyeti.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Equatoria_(South_Sudan)_banner_Mount_Kinyeti.jpg",
                "credit": "AIMikhin · CC BY-SA 3.0",
                "caption": "Los montes Imatong.",
            },
        ],
    ),
    dict(
        n=4, name="Torit y el Ecuatoria Oriental · la cuna del motín de 1955", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=4.4102396, lon=32.5740376,  # Google Maps: Torit
        desc="El 18 de agosto de 1955 el Cuerpo de Ecuatoria se amotinó aquí antes que aceptar su traslado a Jartum, y ese motín es el ARRANQUE DE LA PRIMERA GUERRA CIVIL SUDANESA, medio siglo de conflicto que acabó en la independencia de 2011. Torit es hoy la capital administrativa del Ecuatoria Oriental, a unos 150 km al este de Yuba por la carretera de Lokichoggio, y la puerta obligada hacia los Imatong. Poca cosa que ver: el valor es histórico y logístico.",
        dog_note="Ciudad sin recintos cerrados al perro, pero con calor extremo y perros callejeros: atado, con agua y sin dejarlo en el coche.",
        visit={
            "why": "Es el lugar donde empezó la guerra que terminó creando el país, y la base desde la que se sacan permisos y guías para los Imatong.",
            "see": "El trazado colonial de la ciudad, el mercado principal y el Ministerio de Fauna, Conservación y Turismo donde se gestionan los permisos de montaña.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Por la carretera Yuba–Lokichoggio, unos 150 km desde Yuba. Sin problema de aparcamiento para dos 4x4 en la zona del mercado. Sin entradas ni horarios: no hay museo ni monumento formalizado del motín, POR CONFIRMAR si existe alguna placa. El pin marca el mercado principal, referencia local y punto de encuentro con guías.",
            "when": "Estación seca; por la mañana, cuando funciona el mercado.",
            "skip": "Si no vais a subir a los Imatong ni a seguir hacia Kapoeta: por sí sola, Torit no justifica un desvío.",
        },
        links=[
            {"label": "Torit (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Torit"},
            {"label": "MAEC · recomendaciones de viaje Sudán del Sur", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Yei_township_(South_Sudan)_banner.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Yei_township_(South_Sudan)_banner.jpg",
                "credit": "SuSanA Secretariat · CC BY 2.0",
                "caption": "Poblado del Equatoria, la región de Torit (imagen de contexto).",
            },
        ],
    ),
    dict(
        n=5, name="Parque nacional de Badingilo · la migración de tiangs y gacelas (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=5.5750333, lon=32.174605,  # Google Maps: Bandingilo National Park
        desc="Declarado en 1992 y con más de 10.000 km², Badingilo se extiende por la antigua Ecuatoria y mete sus marismas en Jonglei, allí donde el Sudd se encuentra con la sabana sudanesa oriental. Es el extremo occidental de la migración: tiangs, gacelas de Mongalla y cobos de orejas blancas cruzan hasta Boma y siguen hasta el parque de Gambela, en Etiopía. Desde julio de 2026 forma parte del bien UNESCO Boma–Badingilo. Gestionado por African Parks desde el 25 de agosto de 2022. AVISO: no hay infraestructura turística montada.",
        dog_note="Parque nacional con león, guepardo, licaón y hiena manchada; el perro no entra y además sería presa.",
        visit={
            "why": "Es la mitad accesible desde Yuba del mayor movimiento de mamíferos terrestres del planeta y, desde 2026, Patrimonio Mundial.",
            "see": "Rebaños de cobo de orejas blancas, tiang y gacela de Mongalla; también jirafa nubia en peligro crítico, guepardo del noreste de África, león, licaón, caracal y unas 400 especies de aves.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Sin carretera asfaltada: pistas de tierra desde la Yuba–Bor y desde Terekeka, intransitables en lluvias. Tarifas, puertas y horarios oficiales: POR CONFIRMAR, la web de African Parks no publica información de visita, permisos ni accesos para el público. Cualquier entrada exige coordinarse previamente con African Parks y el Ministerio de Fauna. El pin marca la referencia de acceso al parque; NO hay taquilla formalizada documentada.",
            "when": "Estación seca de diciembre a marzo, que es además cuando se concentra la migración en la zona sur.",
            "skip": "Si no lleváis acuerdo previo con African Parks: presentarse sin avisar en un parque que no recibe turismo es perder el viaje.",
        },
        links=[
            {"label": "Badingilo y Boma · African Parks (oficial)", "url": "https://www.africanparks.org/the-parks/badingilo-boma"},
            {"label": "Boma–Badingilo Migratory Landscape · UNESCO nº 1808", "url": "https://whc.unesco.org/en/list/1808/"},
            {"label": "Parque nacional de Bandingilo (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bandingilo_National_Park"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ugandan_kob_(Kobus_kob_thomasi)_male.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ugandan_kob_(Kobus_kob_thomasi)_male.jpg",
                "credit": "Charles J. Sharp · CC BY-SA 4.0",
                "caption": "Kob macho (foto de la especie: el kob de orejas blancas es el protagonista de la migración).",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ugandan_kobs_(Kobus_kob_thomasi)_female_and_calf.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ugandan_kobs_(Kobus_kob_thomasi)_female_and_calf.jpg",
                "credit": "Charles J. Sharp · CC BY-SA 4.0",
                "caption": "Hembra de kob con cría.",
            },
        ],
    ),
    dict(
        n=6, name="Parque nacional de Boma · la mayor migración terrestre del mundo (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="prohibido", time="1–2 noches",
        lat=6.3236039, lon=33.9750018,  # Google Maps: Boma National Park
        desc="22.800 km² en el este del país, junto a la frontera etíope. El censo aéreo de 2023-2024 de African Parks, con el Ministerio de Fauna y el apoyo de The Wilderness Project, confirmó aquí la MAYOR MIGRACIÓN TERRESTRE DE MAMÍFEROS DEL MUNDO: 5.896.373 ± 909.495 antílopes sobre 122.774 km², unos seis millones. Dos avionetas tomaron más de 330.000 imágenes y siete licenciados de la Universidad de Yuba analizaron 59.718 fotos de 64 transectos. El bien UNESCO entró en 2026 directamente en la Lista del Patrimonio Mundial EN PELIGRO.",
        dog_note="Parque nacional con grandes depredadores y fauna migratoria: los perros no entran.",
        visit={
            "why": "Porque aquí se midió y se confirmó el mayor movimiento de mamíferos terrestres del planeta, por delante del Serengeti, y es el corazón del primer Patrimonio Mundial de Sudán del Sur.",
            "see": "Cobo de orejas blancas (5.089.421 ± 882.775 ejemplares), gacela de Mongalla (346.273 ± 87.265), tiang (298.776 ± 179.937) y cobo de los juncos bohor (161.903 ± 88.863), además de elefante de sabana, licaón y lechwe del Nilo.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). El acceso rodado desde Yuba es de pista, muy largo y atraviesa Jonglei, estado que el MAEC describe sumido en violencia y desorden permanente. No hay puerta de entrada, horario ni tarifa publicados: POR CONFIRMAR con African Parks, que no difunde información de visita. En la práctica, los pocos accesos se hacen en avioneta y con la organización gestora. El pin marca el centroide del parque publicado por Wikipedia, NO una entrada.",
            "when": "Estación seca de diciembre a marzo; el grueso de la migración se mueve entre Boma y Badingilo con las lluvias.",
            "skip": "Con los vehículos y sin cobertura logística de African Parks es directamente inviable: descártalo como etapa rodada.",
        },
        links=[
            {"label": "African Parks · se confirma la mayor migración terrestre del mundo", "url": "https://www.africanparks.org/worlds-largest-land-mammal-migration-confirmed-south-sudan"},
            {"label": "Boma–Badingilo Migratory Landscape · UNESCO nº 1808", "url": "https://whc.unesco.org/en/list/1808/"},
            {"label": "Parque nacional de Boma (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Boma_National_Park"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/A_village_in_Boma_payam.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:A_village_in_Boma_payam.jpg",
                "credit": "Jenna Randolph · CC BY 4.0",
                "caption": "Una aldea en el payam de Boma.",
            },
        ],
    ),
    dict(
        n=7, name="El Sudd · el mayor humedal de África y el Nilo perdido", cat="Naturaleza", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=8.0, lon=31.0,  # Google Maps: El Sudd (sin objeto en Google Maps; coordenada de la fuente)
        desc="Pantano inmenso formado por el tramo Bahr al Jabal del Nilo Blanco: 30.000 km² de media, 57.000 km² protegidos como sitio Ramsar desde el 5 de junio de 2006 (nº 1622) y más de 130.000 km² en crecida. Es el mayor humedal de agua dulce de la cuenca del Nilo y el que se tragó durante siglos las expediciones que buscaban las fuentes. El canal de Jonglei, empezado en 1978 para esquivarlo, se quedó en 240 de 360 km excavados en 1984. En la lista indicativa de la UNESCO desde el 4 de octubre de 2017.",
        dog_note="Humedal con cocodrilos, hipopótamos y mosquitos a millones; desplazarse es en barca y no hay dónde bajar al perro.",
        visit={
            "why": "Es uno de los grandes humedales del mundo, el laberinto que durante siglos impidió remontar el Nilo, y alberga unos 7.000 picozapatos y unos 11.000 lechwes del Nilo.",
            "see": "Papiro hasta el horizonte, canales y lagunas, unas 470 especies de aves, más de 100 de peces y 100 de mamíferos; y las dos mayores migraciones de ungulados del mundo en sus bordes.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). NO SE VISITA EN COCHE: al Sudd se entra en barca desde los embarcaderos del Nilo, y el más razonable desde Yuba es el de Bor, al final de la Yuba–Bor asfaltada. No existen operadores ni tarifas publicadas: POR CONFIRMAR. El MAEC sitúa Jonglei y Alto Nilo en violencia permanente. El pin marca el puerto fluvial de Bor, punto de embarque lógico, no el humedal, que carece de punto navegable.",
            "when": "Final de la estación seca (febrero–marzo), con el agua baja y menos mosquito; en crecida, de abril a noviembre, es impracticable.",
            "skip": "Sin embarcación fiable y sin escolta, descártalo: es zona de conflicto activo y no hay rescate posible.",
        },
        links=[
            {"label": "El Sudd (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Sudd"},
            {"label": "Sudd wetland · lista indicativa UNESCO", "url": "https://whc.unesco.org/en/tentativelists/6276/"},
            {"label": "Sudán del Sur · Estado parte UNESCO", "url": "https://whc.unesco.org/en/statesparties/ss"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Merol_Market,_Bor_Town,_Jonglei_State,_South_Sudan.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Merol_Market,_Bor_Town,_Jonglei_State,_South_Sudan.jpg",
                "credit": "Mr leroy playpus (Tuttle) · CC BY-SA 4.0",
                "caption": "El mercado de Merol, en Bor.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Little_house_with_garden_in_Bor,_South_Sudan.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Little_house_with_garden_in_Bor,_South_Sudan.jpg",
                "credit": "Mr leroy playpus · CC BY 4.0",
                "caption": "Casa con huerto en Bor.",
            },
        ],
    ),
    dict(
        n=8, name="Bor y el país dinka · los campamentos de ganado", cat="Cultura", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=6.2132663, lon=31.5655424,  # Google Maps: Bor
        desc="En la orilla oriental del Nilo Blanco, capital de Jonglei y centro administrativo del pueblo dinka bor desde el Sudán anglo-egipcio. Bor TIENE EL MAYOR CENSO GANADERO DEL PAÍS, y sus campamentos de vacas —humo de boñiga contra el mosquito, cuernos tallados, cantos de ganado— son la estampa más reconocible de Sudán del Sur. También carga la memoria del motín de mayo de 1983 que abrió la Segunda Guerra Civil y de la masacre de 1991. La Yuba–Bor está asfaltada.",
        dog_note="Los campamentos de ganado son espacios de trabajo y de prestigio de las familias dinka: un perro suelto entre el ganado es una ofensa y un riesgo.",
        visit={
            "why": "Es el acceso por asfalto al mundo dinka y al borde del Sudd, con los campamentos de ganado que definen la cultura del país.",
            "see": "Los campamentos de ganado a las afueras, la orilla del Nilo Blanco y el puerto fluvial.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Por la autovía Yuba–Bor, asfaltada, lo que hace de Bor la ciudad regional más accesible del país. Aparcamiento para dos 4x4 solo en recintos con guardia. Sin entradas ni horarios: los campamentos son propiedad privada de las familias, hay que pedir permiso y pagar propina por fotografiar. El MAEC sitúa Jonglei entre los estados en violencia y desorden permanente. El pin marca el centro de Bor.",
            "when": "Estación seca; los campamentos se ven al amanecer y al atardecer, cuando se ordeña y se enciende el humo.",
            "skip": "En época de razias de ganado o de enfrentamientos intercomunitarios en Jonglei, que son recurrentes.",
        },
        links=[
            {"label": "Bor (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bor,_South_Sudan"},
            {"label": "MAEC · recomendaciones de viaje Sudán del Sur", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Dinka_Bull,_Wau._Sudan_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Dinka_Bull,_Wau._Sudan_-_panoramio.jpg",
                "credit": "Michael Walsh · CC BY 3.0",
                "caption": "Toro dinka, el centro de la vida de los campamentos de ganado.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Dinka_Catle,_Wau,_Sudan_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Dinka_Catle,_Wau,_Sudan_-_panoramio.jpg",
                "credit": "Michael Walsh · CC BY 3.0",
                "caption": "Ganado dinka.",
            },
        ],
    ),
    dict(
        n=9, name="Malakal y el Nilo Blanco · la ciudad disputada", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="medio día",
        lat=9.5279875, lon=31.6682347,  # Google Maps: Malakal
        desc="Capital del Alto Nilo, sobre el Nilo Blanco a unos 650 km al norte de Yuba y cerca de las fronteras de Sudán y Etiopía. Fue el gran puerto fluvial del sur —desde aquí se navegaba hasta Jartum— y el símbolo de la destrucción de la guerra: para octubre de 2015 HABÍA CAMBIADO DE MANOS DOCE VECES y quedó completamente arrasada. El campo de protección de civiles de UNMISS sigue abierto y en junio de 2023 murieron allí 13 civiles en enfrentamientos. Ficha informativa: no es una parada planteable.",
        dog_note="Ciudad arrasada con campo de desplazados de la ONU al lado; no es sitio para bajar al perro del coche.",
        visit={
            "why": "Por entender qué significó la guerra civil en una ciudad concreta, y por el eje fluvial hacia Jartum.",
            "see": "El puerto sobre el Nilo Blanco, las ruinas del centro y la escala del campo de desplazados.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). 650 km al norte de Yuba, sin corredor terrestre seguro: el acceso práctico es por el aeropuerto internacional de Malakal, uno de los dos internacionales del país. El MAEC señala expresamente Alto Nilo como estado en violencia y desorden permanente. Sin entradas ni horarios. El pin marca el puerto fluvial.",
            "when": "Irrelevante: no hay ventana recomendable mientras dure el aviso.",
            "skip": "Siempre, con los avisos actuales: es de las zonas más expuestas del país.",
        },
        links=[
            {"label": "Malakal (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Malakal"},
            {"label": "MAEC · recomendaciones de viaje Sudán del Sur", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Malakal_post_office_March_2011_DSC01488_822_kb.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Malakal_post_office_March_2011_DSC01488_822_kb.jpg",
                "credit": "Leovdvxxx · CC BY-SA 4.0",
                "caption": "La oficina de correos de Malakal.",
            },
        ],
    ),
    dict(
        n=10, name="Wau · la catedral de Santa María y la vieja estación de ferrocarril", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=7.7091884, lon=27.9834738,  # Google Maps: Wau
        desc="La segunda ciudad del país, en la orilla oeste del río Jur y a unos 650 km al noroeste de Yuba. Conserva dos huellas coloniales poco comunes en Sudán del Sur: la catedral católica de Santa María, levantada entre 1951 y 1956 —la diócesis se erigió el 12 de diciembre de 1974—, y la estación de ferrocarril, TERMINAL DEL RAMAL DE VÍA ESTRECHA de los Ferrocarriles de Sudán desde Babanusa. En enero de 2020 la estación estaba sin servicio, con el edificio ocupado por la policía y las vías comidas por la arena.",
        dog_note="La catedral es recinto religioso en uso y no admite perros; la estación está ocupada por la policía sursudanesa.",
        visit={
            "why": "Por las dos piezas de arquitectura colonial mejor conservadas del país y por el final de vía del único ferrocarril que llegó al sur.",
            "see": "La catedral de Santa María (1951-1956) y la estación de Wau, justo al sur del aeropuerto, con las vías desaparecidas bajo la arena.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Wau está en el cruce de cinco carreteras: B38 al norte a Gogrial, B43 al sur a Tonj, A44 al sur a Tumbura, B41 al oeste a Raga y B43 al norte a Aweil; ninguna asfaltada de forma continua. Aeropuerto con una pista asfaltada de 2.500 m. Aparcamiento para dos 4x4 en el atrio de la catedral. Horarios y misas: POR CONFIRMAR, la diócesis no publica web propia. El MAEC incluye Bahr el Ghazal Occidental entre las zonas peligrosas por milicias locales. El pin marca la catedral.",
            "when": "Estación seca, de diciembre a marzo; domingo por la mañana si se quiere ver la catedral llena.",
            "skip": "Si la ruta no llega ya hasta el Bahr el Ghazal: son 650 km de pista desde Yuba para dos edificios.",
        },
        links=[
            {"label": "Wau (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Wau,_South_Sudan"},
            {"label": "Estación de ferrocarril de Wau (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Wau_Railway_Station"},
            {"label": "Diócesis católica de Wau (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Roman_Catholic_Diocese_of_Wau"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Huts_outside_Wau,Sudan.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Huts_outside_Wau,Sudan.jpg",
                "credit": "Bertramz · CC BY-SA 3.0",
                "caption": "Chozas a las afueras de Wau.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cattle_Wau_Sudan.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cattle_Wau_Sudan.jpg",
                "credit": "Bertramz · CC BY-SA 3.0",
                "caption": "Un hombre muestra su ganado en Wau.",
            },
        ],
    ),
    dict(
        n=11, name="Kapoeta y los toposa · el este seco y el oro artesanal", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=4.7713162, lon=33.5923941,  # Google Maps: Kapoeta
        desc="Última población grande antes de Kenia: la carretera principal de Lokichogio a Yuba pasa por aquí. El este seco es país toposa, pastores que dominan las llanuras, mientras los didinga cultivan las tierras altas más húmedas del sur. La comarca es conocida por la minería de oro artesanal, pero OJO: la Wikipedia de Kapoeta NO documenta esa minería, así que el dato del oro queda marcado como por confirmar y no se debe dar por bueno en la ficha sin una fuente mejor.",
        dog_note="Zona ganadera toposa: el perro solo atado y nunca cerca del ganado ni de los campamentos.",
        visit={
            "why": "Por el paisaje semidesértico y por el mundo pastoril toposa, muy distinto de la Ecuatoria verde.",
            "see": "Poblados y rebaños toposa en las llanuras, el mercado de Kapoeta y el contraste con las tierras altas didinga.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Sobre la carretera Yuba–Lokichogio (Kenia), unos 275 km al este de Yuba; el tramo de Torit a Kapoeta es de pista. Espacio de sobra para dos 4x4. Sin entradas ni horarios. El MAEC advierte de que todas las carreteras presentan riesgos extremos, con ataques, emboscadas y controles militares diarios. El pin marca el pueblo de Kapoeta.",
            "when": "Estación seca; el este es el rincón más árido y caluroso del país.",
            "skip": "Si no vais a salir o entrar por la frontera keniana de Nadapal: no hay motivo para el desvío.",
        },
        links=[
            {"label": "Kapoeta (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Kapoeta"},
            {"label": "MAEC · recomendaciones de viaje Sudán del Sur", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Toposa_village.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Toposa_village.jpg",
                "credit": "Steve Evans · CC BY 2.0",
                "caption": "Poblado toposa, en el Equatoria Oriental.",
            },
        ],
    ),
    dict(
        n=12, name="Rumbek · la capital provisional de los años de guerra", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=6.8072494, lon=29.6788877,  # Google Maps: Rumbek
        desc="En el estado de los Lagos, a unos 377 km al noroeste de Yuba y a 420 m de altitud. Tras el acuerdo que cerró la Segunda Guerra Civil, el SPLM ELIGIÓ RUMBEK COMO SEDE ADMINISTRATIVA PROVISIONAL del Sudán del Sur antes de que Yuba fuese capital definitiva: durante unos años aquí estuvo el gobierno del sur, en barracones. Hoy es un nudo de la A43 entre Yuba y Wau, con aeropuerto con vuelos regulares y chárter, y una de las pocas ciudades intermedias con servicios básicos para reponer.",
        dog_note="Ciudad abierta y sin recintos vetados; atado y con sombra, que a 420 m y en sabana el calor aprieta.",
        visit={
            "why": "Es la escala obligada y con servicios entre Yuba y Wau, y el lugar donde se administró el sur antes de la independencia.",
            "see": "El trazado de la vieja sede administrativa del SPLM, el mercado y el nudo de carreteras hacia Yirol, Yuba, Wau y Durbuoni.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Sobre la carretera principal A43 Yuba–Wau; desde 2005 se han reparado tramos, pero no es asfalto continuo. Aeropuerto de Rumbek con vuelos regulares y chárter. Aparcamiento para dos 4x4 en compounds con guardia. Sin entradas ni horarios. El pin marca el centro de la ciudad.",
            "when": "Estación seca, de diciembre a marzo: en lluvias la A43 se embarra.",
            "skip": "Si vais directos de Yuba a Wau sin necesidad de reponer combustible ni agua.",
        },
        links=[
            {"label": "Rumbek (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Rumbek"},
            {"label": "MAEC · recomendaciones de viaje Sudán del Sur", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cattle_Herders_at_Cattle_Camp_in_Rumbek,_South_Sudan.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cattle_Herders_at_Cattle_Camp_in_Rumbek,_South_Sudan.jpg",
                "credit": "JennaCB123 · CC BY-SA 3.0",
                "caption": "Pastores en un campamento de ganado cerca de Rumbek.",
            },
        ],
    ),
    dict(
        n=13, name="Yei y el Ecuatoria Occidental · el corredor verde a Uganda", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=4.0917156, lon=30.6764537,  # Google Maps: Yei
        desc="Cabecera del condado de Yei River, en Ecuatoria Central, a 831 m de altitud: el rincón fértil del país, la «zona de medios de vida de maíz y mandioca ecuatorial» que antes de 2016 producía excedente de cereal. La escalada del conflicto ese año lo cambió todo: la cosecha PASÓ DE EXCEDENTE A DÉFICIT y la población huyó en masa a Uganda; en 2020 el condado contaba unos 67.511 desplazados internos y 10.097 retornados. Carreteras a Maridi, Lainya-Yuba, Kaya y la frontera de la RDC.",
        dog_note="Zona agrícola y templada, la más llevadera del país para el perro; atado y con precaución por perros de aldea.",
        visit={
            "why": "Es el Sudán del Sur verde y templado, el contrapunto agrícola de la sabana, y el eje natural hacia Uganda y la RDC.",
            "see": "Plantaciones de maíz y mandioca, colinas boscosas y el movimiento de retornados por la carretera de Kaya.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Cuatro ejes: Yei–Maridi al noroeste, Yei–Lainya al noreste hacia Yuba, Yei–Kaya al sur hacia Uganda y Yei–Aba/Lasu al suroeste hacia la RDC; todos de tierra. Aparcamiento para dos 4x4 sin problema. El MAEC incluye Ecuatoria Central y Occidental entre las zonas peligrosas por milicias locales y señala que los asaltos aumentan en la estación lluviosa, de abril a noviembre. El pin marca el centro del pueblo.",
            "when": "Estación seca; las pistas de tierra del corredor verde se hacen intransitables con lluvia.",
            "skip": "Si hay actividad de grupos armados en el corredor Yei–Kaya, que es de las zonas más volátiles de Ecuatoria.",
        },
        links=[
            {"label": "Condado de Yei River (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Yei,_South_Sudan"},
            {"label": "Aeropuerto de Yei (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Yei_Airport"},
            {"label": "MAEC · recomendaciones de viaje Sudán del Sur", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Huts_in_Yei_township,_South_Sudan.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Huts_in_Yei_township,_South_Sudan.jpg",
                "credit": "SuSanA Secretariat · CC BY 2.0",
                "caption": "Chozas de paja en Yei.",
            },
        ],
    ),
    dict(
        n=14, name="Reserva de fauna de Ez Zeraf · la isla del Nilo", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=9.2681678, lon=31.0260773,  # Google Maps: Bahr ez Zeraf
        desc="8.000 km² de pradera y bosque estacionalmente inundados declarados en 1939, junto con la reserva de Fanyikang, y clasificados como categoría VI de la UICN. Buena parte ocupa la ISLA DE ZERAF, aislada por el Nilo Blanco al oeste y el Bahr el Zeraf al este; el Bahr el Zeraf recorre 280 km por la reserva y se reincorpora al Nilo cerca de New Fangak. Es internacionalmente importante por sus concentraciones de grandes mamíferos —lechwe del Nilo y sitatunga— y está dentro del sitio Ramsar del Sudd.",
        dog_note="Área protegida con hipopótamos y fauna de humedal; no entra el perro y, en todo caso, el acceso es en barca.",
        visit={
            "why": "Es el corazón del Sudd protegido desde 1939 y uno de los últimos refugios del lechwe del Nilo, antílope que solo vive en estos humedales.",
            "see": "Lechwe del Nilo, sitatunga e hipopótamos sobre praderas inundadas; canales del Bahr el Zeraf y los cortes artificiales de 1910 y 1913 que doblaron su caudal.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). NO HAY ACCESO RODADO: la reserva es una isla fluvial estacionalmente inundada y solo se entra en barca; la ciudad más próxima es Malakal. Sin infraestructura, sin puerta, sin tarifa: nada documentado. El MAEC sitúa Jonglei y Alto Nilo en violencia y desorden permanente. El pin marca el centroide publicado por Wikipedia, NO un punto navegable.",
            "when": "Final de la estación seca, cuando la isla está transitable; en crecida es inaccesible.",
            "skip": "Con estos vehículos, siempre: no es un PDI rodable y va en la ficha por completitud.",
        },
        links=[
            {"label": "Reserva de fauna de Ez Zeraf (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Ez_Zeraf_Game_Reserve"},
            {"label": "Bahr el Zeraf (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bahr_el_Zeraf"},
            {"label": "Sudd wetland · lista indicativa UNESCO", "url": "https://whc.unesco.org/en/tentativelists/6276/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pantanal_Sudd,_Sud%C3%A3o_do_Sul.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pantanal_Sudd,_Sud%C3%A3o_do_Sul.jpg",
                "credit": "INPE / Coordenação-Geral de Observação da Terra · CC BY-SA 2.0",
                "caption": "El Sudd desde satélite (CBERS-4).",
            },
        ],
    ),
    dict(
        n=15, name="Bentiu y el Alto Nilo · el petróleo y las inundaciones", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="medio día",
        lat=9.231487, lon=29.8005027,  # Google Maps: Bentiu
        desc="Capital del estado de Unidad, a unos 654 km al noroeste de Yuba, en la zona petrolera: los yacimientos de Heglig —a caballo de la frontera con Sudán— y de Unidad, y el arranque del oleoducto del Gran Nilo hacia Port Sudan. En abril de 2014 cientos de civiles fueron masacrados aquí. El pueblo tenía unos 6.500 habitantes en 2010; el CAMPO DE LA ONU AL LADO HA LLEGADO A 160.000. A la guerra se sumaron en 2023 dos años seguidos de inundaciones por lluvias intensas.",
        dog_note="Campo de desplazados de más de 100.000 personas, terreno inundado y crisis sanitaria: no es sitio para bajar al perro.",
        visit={
            "why": "Es donde se ven juntas las dos fuerzas que han marcado al país: el petróleo que lo financia y el agua que lo está anegando.",
            "see": "El paisaje petrolero de Unidad, los diques contra la inundación y la escala del campo de desplazados.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). 654 km al noroeste de Yuba por pistas que se inundan; el MAEC nombra expresamente Unidad como estado en violencia y desorden permanente, y las carreteras fronterizas con Sudán como peligrosas. Sin entradas, horarios ni servicios turísticos. El pin marca Bentiu.",
            "when": "Irrelevante: no hay ventana recomendable con los avisos vigentes.",
            "skip": "Siempre, salvo que la situación cambie por completo: es zona petrolera militarizada y frontera caliente con Sudán.",
        },
        links=[
            {"label": "Bentiu (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Bentiu"},
            {"label": "MAEC · recomendaciones de viaje Sudán del Sur", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sudan07-_bentiu-_contesto-_COSV.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sudan07-_bentiu-_contesto-_COSV.jpg",
                "credit": "COSV · CC BY-SA 3.0",
                "caption": "Bentiu, en el estado de Unidad.",
            },
        ],
    ),
    dict(
        n=16, name="Aweil y el Bahr el Ghazal del Norte", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=8.7670867, lon=27.3998369,  # Google Maps: Aweil
        desc="Capital del Bahr el Ghazal del Norte, a unos 100 km al sur de la frontera de Sudán y a 425 m sobre un terreno relativamente alto, cerca de la confluencia del río Lol con el Pongo. El ferrocarril Jartum–Aweil–Wau se construyó en 1961 y el tramo de Aweil a Wau, con su estación, SE RESTAURÓ EN 2010 tras los destrozos de la guerra. Economía de ganado, sorgo, cacahuete y sésamo, con plantaciones de teca y de arroz. Se llega por la A43; hay pista de tierra de 2.000 m.",
        dog_note="Ciudad de sabana sin recintos vetados; el problema es el calor y la falta de sombra, no la normativa.",
        visit={
            "why": "Es el extremo noroeste transitable del país y el punto donde el ferrocarril sudanés entraba en el sur.",
            "see": "La estación y la vía Aweil–Wau restaurada en 2010, la confluencia del Lol con el Pongo, la plantación de arroz y el mercado de mujeres.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Por la A43 desde Wau; pista de tierra, muy mala en lluvias, con unos 95 mm anuales repartidos en unos 125 días de lluvia. Aparcamiento para dos 4x4 sin dificultad. Sin entradas ni horarios. El MAEC advierte del peligro de las zonas fronterizas con Sudán. El pin marca el centro de Aweil.",
            "when": "Estación seca, de diciembre a marzo.",
            "skip": "Si la guerra de Sudán está empujando población o combates hacia la frontera, que está a solo 100 km.",
        },
        links=[
            {"label": "Aweil (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Aweil,_South_Sudan"},
            {"label": "MAEC · recomendaciones de viaje Sudán del Sur", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sudan_Aweil_huts_2006.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sudan_Aweil_huts_2006.jpg",
                "credit": "Kai Breker · CC BY-SA 3.0",
                "caption": "Chozas de paja en Aweil.",
            },
        ],
    ),
    dict(
        n=17, name="Yirol y el lago No · los lagos del Sudd", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=6.5609799, lon=30.5020001,  # Google Maps: Yirol
        desc="Yirol, en el estado de los Lagos, a unos 313 km al noroeste de Yuba, vive del ganado, la pesca y la agricultura de subsistencia en los lagos Yirol, Nyiboor y Anyii y el río Payii. Más al norte, ya en pleno Sudd, el lago No (100 km² de superficie máxima) marca la CONFLUENCIA DEL BAHR AL JABAL CON EL BAHR EL GHAZAL y el punto exacto donde el río pasa a llamarse Nilo Blanco propiamente dicho: está a 1.156 km aguas abajo del lago Alberto. Yirol es rodable; el lago No, no.",
        dog_note="Orillas con cocodrilos e hipopótamos y comunidades pesqueras que trabajan en la ribera; el perro, atado y lejos del agua.",
        visit={
            "why": "Yirol da acceso por tierra al mundo lacustre dinka, y el lago No es el hito geográfico donde nace formalmente el Nilo Blanco.",
            "see": "Pesca en los lagos Yirol, Nyiboor y Anyii, rebaños y, si se navega, la confluencia del lago No.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Yirol está conectado por pista con Rumbek al oeste, Bentiu al norte y Yuba al sur, y tiene aeropuerto propio. El lago No (9.49722 N, 30.45556 E) NO tiene acceso rodado: solo en barca desde el Nilo. Sin entradas ni horarios. El pin marca el pueblo de Yirol, que es el objeto navegable; el lago No queda a más de 300 km al norte.",
            "when": "Estación seca, de diciembre a marzo.",
            "skip": "El lago No, siempre con estos vehículos; Yirol, si la A43 obliga a ir directo de Yuba a Rumbek.",
        },
        links=[
            {"label": "Yirol (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Yirol"},
            {"label": "Lago No (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Lake_No"},
            {"label": "El Sudd (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Sudd"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_Yirol_Road,_Just_outside_Yirol_Town,_South_Sudan.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_Yirol_Road,_Just_outside_Yirol_Town,_South_Sudan.jpg",
                "credit": "JennaCB123 · CC BY-SA 3.0",
                "caption": "La carretera de Yirol.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Yirol_Church.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Yirol_Church.jpg",
                "credit": "Ernst Ulz · CC BY-SA 3.0",
                "caption": "La iglesia católica de Yirol.",
            },
        ],
    ),
    dict(
        n=18, name="Kajo-Keji y la frontera de Uganda · el retorno de los refugiados", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=3.8550654, lon=31.656829,  # Google Maps: Kajo Keji
        desc="A unos 150 km al sur de Yuba y pegado a la frontera de Uganda, es el país de los kuku y sede de la diócesis anglicana de Kajo-Keji. Nimule, el paso fronterizo más importante —donde el Nilo Victoria entra en Sudán del Sur—, queda a unos 50 km al sureste. El condado se vació casi por completo hacia los campos ugandeses tras 2016 y desde entonces es uno de los termómetros del retorno de refugiados. CURIOSIDAD: tiene la única sucursal de Equity Bank del condado.",
        dog_note="Zona rural templada; el perro puede bajar atado, pero la catedral anglicana y los recintos de la diócesis no admiten animales.",
        visit={
            "why": "Por ver de cerca el pulso del retorno de refugiados desde Uganda, que es la historia viva del sur del país.",
            "see": "El paisaje kuku de colinas y cultivos, la sede de la diócesis anglicana y el trasiego de la frontera.",
            "access": "El MAEC DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a Sudán del Sur y pide a los españoles que se encuentren en el país que lo abandonen de inmediato (ficha actualizada el 28/03/2025, vigente a 05/08/2026). Unos 150 km al sur de Yuba por pista; enlaza con Nimule, a unos 50 km al sureste, y con el paso de Uganda. Aparcamiento para dos 4x4 sin dificultad. Sin entradas ni horarios. El MAEC incluye Ecuatoria Central entre las zonas peligrosas por milicias locales. El pin marca el pueblo de Kajo-Keji.",
            "when": "Estación seca, de diciembre a marzo.",
            "skip": "Si vais a entrar o salir por Nimule por la A43 asfaltada: el desvío a Kajo-Keji es pista y añade un día.",
        },
        links=[
            {"label": "Kajo Keji (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Kajo_Keji"},
            {"label": "Nimule (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Nimule"},
            {"label": "MAEC · recomendaciones de viaje Sudán del Sur", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Downtown_Kajo_Keji,_Sudan_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Downtown_Kajo_Keji,_Sudan_-_panoramio.jpg",
                "credit": "Russell Lindberg · CC BY-SA 3.0",
                "caption": "El centro de Kajo-Keji.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Kajo_Keji_Horizon_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Kajo_Keji_Horizon_-_panoramio.jpg",
                "credit": "Russell Lindberg · CC BY-SA 3.0",
                "caption": "El horizonte de Kajo-Keji.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Kajo_Keji,_South_Sudan_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Kajo_Keji,_South_Sudan_-_panoramio.jpg",
                "credit": "Russell Lindberg · CC BY-SA 3.0",
                "caption": "Kajo-Keji, en la frontera de Uganda.",
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
    ("Aeropuerto Internacional de Yuba (JUB/HJJJ)", "Frontera", 4.8661935, 31.6017367,  # Google Maps: Aeropuerto Internacional de Yuba
     "Única vía de entrada realista al país y ÚNICO punto de entrada admitido para mascotas. Terminal nueva inaugurada el 29 de octubre de 2018. Vuelos a Nairobi, Adís Abeba, El Cairo, Dubái y Port Sudan. Certificado de fiebre amarilla exigido en el control. Pin comprobado en Google Maps («Aeropuerto Internacional de Yuba»)."),
    ("Paso fronterizo de Nimule (lado sursudanés)", "Frontera", 3.5915846, 32.0638586,  # Google Maps: Nimule
     "Paso terrestre principal del país, con Uganda. Puesto fronterizo de parada única abierto en el lado de Nimule en febrero de 2020. Arranque de la carretera asfaltada de 197 km a Yuba. Sufre bloqueos de transportistas de varios días. Pin comprobado en Google Maps («Nimule»)."),
    ("Paso fronterizo de Elegu (lado ugandés)", "Frontera", 3.5641307, 32.0713785,  # Google Maps: Elegu (lado ugandés)
     "Contraparte ugandesa de Nimule, en el distrito de Amuru, a 105 km por carretera al norte de Gulu. Convertido en puesto de parada única entre 2015 y 2018 con 6,6 millones de dólares de TradeMark East Africa; inaugurado en noviembre de 2018. Pin comprobado en Google Maps («Elegu (lado ugandés)»)."),
    ("Embajada de España en Jartum (competente para Sudán del Sur)", "Consular", 15.6063636, 32.5704099,  # Google Maps: Embassy of Spain (Jartum)
     "La Embajada de España en Jartum cubre la demarcación consular de la República de Sudán del Sur. Dirección publicada: International Fair Road, Building 1, Block 7/A, Burri El Daraisa, P.O. Box 274, Jartum. Tel. +249 183 763 639 / +249 183 269 891; emergencia consular +249 912 363 377; emb.jartum@maec.es. ATENCIÓN: el MAEC indica residencia temporal en El Cairo (41 Ismail Mohamed, Zamalek). COORDENADAS APROXIMADAS DE CIUDAD, no de la cancillería: verificar. Pin comprobado en Google Maps («Embassy of Spain (Jartum)»)."),
    ("Embajada de España en Jartum · sede temporal en El Cairo", "Consular", 30.0623764, 31.2225602,  # Google Maps: Embajada de España en El Cairo (sede temporal)
     "Sede temporal indicada por el MAEC en sus recomendaciones de viaje a Sudán del Sur: 41 Ismail Mohamed, Zamalek, El Cairo. Email emb.jartum@maec.es. Es el punto de contacto consular práctico mientras dure el conflicto sudanés. COORDENADAS APROXIMADAS del barrio de Zamalek: verificar. Pin comprobado en Google Maps («Embajada de España en El Cairo (sede temporal)»)."),
    ("MRDC International (Yuba)", "Hospital", 4.8503981, 31.6086987,  # Google Maps: Juba Teaching Hospital
     "Centro médico recomendado por el MAEC y único servicio de ambulancia operativo citado. Tel. +211 954 044 333 y +211 954 044 222; urgencias jubaemergency@mrdc-int.com. Pago en efectivo por adelantado. COORDENADAS APROXIMADAS del centro de Yuba: verificar. Pin comprobado en Google Maps («Juba Teaching Hospital»)."),
    ("Juba Medical Complex (Yuba)", "Hospital", 4.8538566, 31.5825254,  # Google Maps: Yuba
     "Segundo centro recomendado por el MAEC. Tel. +211 955 523 371. Condiciones sanitarias del país calificadas de «muy deficientes» por el MAEC, con servicios básicos solo en Yuba y pago en efectivo previo. COORDENADAS APROXIMADAS del centro de Yuba: verificar. Pin comprobado en Google Maps («Yuba»)."),
    ("Repostaje en Yuba (eje de entrada desde Nimule)", "Combustible", 4.8538566, 31.5825254,  # Google Maps: Yuba (sin gasolinera concreta como objeto)
     "Yuba concentra casi toda la red de gasolineras fiable del país, con colas y racionamiento por la escasez derivada del corte del oleoducto. Radio Tamazuj situaba el litro en torno a 20.000 SSP en julio de 2026, con subidas del 45-105 % en tres meses según FEWS NET. Pago en efectivo. NO hay punto concreto documentado: coordenadas de la ciudad, POR CONFIRMAR sobre el terreno. Pin comprobado en Google Maps («Yuba (sin gasolinera concreta como objeto)»)."),
    ("Último repostaje seguro antes de la frontera: Elegu / Gulu (Uganda)", "Combustible", 3.5641307, 32.0713785,  # Google Maps: Elegu (Uganda)
     "Recomendación operativa de la ficha: entrar con los depósitos llenos y jerricanes cargados desde Uganda, donde el suministro es regular, porque en Sudán del Sur el abastecimiento no está garantizado. Gulu queda 105 km al sur de Elegu por carretera. Pin comprobado en Google Maps («Elegu (Uganda)»)."),
    ("Agua de uso general en Yuba (camiones cisterna del Nilo)", "Agua potable", 4.8538566, 31.5825254,  # Google Maps: Yuba
     "El abastecimiento urbano depende de camiones cisterna que captan agua del Nilo, y se corta cuando falta gasóleo. NO ES POTABLE: filtrar y tratar toda el agua de consumo. Brotes de cólera activos en 2026. No hay punto de llenado documentado para overlanders: coordenadas de la ciudad, POR CONFIRMAR. Pin comprobado en Google Maps («Yuba»)."),
    ("Parque Nacional de Badingilo (Patrimonio Mundial de la UNESCO)", "Frontera", 5.5750333, 32.174605,  # Google Maps: Bandingilo National Park
     "Unos 10.000 km² creados en 1992 y gestionados por African Parks desde agosto de 2022. Junto con Boma forma el paisaje migratorio inscrito como primer Patrimonio Mundial de la UNESCO del país el 24 de julio de 2026, con unos 12 millones de hectáreas. Jirafa nubia, guepardo norteafricano, león, licaón y unas 400 especies de aves. Acceso solo con «alien travel permit» y escolta armada de guardas. Es el destino que justificaría volver. Pin comprobado en Google Maps («Bandingilo National Park»)."),
]

DRONE_CALLOUT = ("danger", "Con el dron no se juega: ni se saca de la bolsa",
                 "Sudán del Sur no tiene reglamento de drones codificado, y eso no es permisividad sino lo contrario: drone-laws.com, en su revisión de 21 de enero de 2026, recoge que los vuelos de visitantes extranjeros NO están permitidos y que solo los operadores gubernamentales pueden volar. La autoridad es la South Sudan Civil Aviation Authority. Añádase que fotografiar exige permiso del Ministerio del Interior, 50 dólares según el Departamento de Estado, y que están prohibidas las imágenes de instalaciones militares e infraestructuras. Un dron en el equipaje es una acusación de espionaje esperando a ocurrir.")

STARLINK_CALLOUT = ("warn", "Starlink funciona, pero el problema no es la cobertura",
                    "Sudán del Sur es uno de los países africanos donde Starlink está autorizado: la National Communication Authority concedió licencia provisional a finales de junio de 2024 y el servicio se lanzó en julio de ese año, con tarifas aprobadas por el regulador y pago en libras sursudanesas equivalentes al precio en dólares. MTN South Sudan lo comercializa a escala nacional. Dicho esto, una antena Starlink en el techo de un 4x4 extranjero es, en un país con controles militares constantes y paranoia con las comunicaciones, un imán para preguntas incómodas. La conectividad no es el cuello de botella aquí.")

DOG_MATRIX = [
    ("Entrada por el Aeropuerto Internacional de Yuba", "permitido con condiciones", "Único punto de entrada admitido para mascotas según PetTravel: rabia entre 30 días y 12 meses antes, certificado veterinario de menos de 10 días refrendado por veterinario oficial y microchip ISO. Confirmar por vía consular antes de volar."),
    ("Entrada por el paso terrestre de Nimule (Uganda)", "por confirmar", "Ninguna fuente documenta el paso de un perro por frontera terrestre. Plan B real: el perro no entra en Sudán del Sur y se queda en Uganda, con residencia canina o con uno de los tres viajeros en Gulu o Entebbe."),
    ("Yuba: alojamientos y compounds", "por confirmar", "No hay información abierta sobre alojamientos que admitan perros. Los compounds internacionales suelen tener normas propias: preguntar caso por caso antes de reservar."),
    ("Parques nacionales de Boma y Badingilo", "prohibido", "Los perros no entran en los parques nacionales, que además exigen escolta armada de guardas para cualquier visitante. Llevar un perro a una zona con rabia endémica, leones y hienas es exponerlo sin necesidad."),
    ("Desplazamientos por carretera fuera de Yuba", "no recomendado", "Canadá recomienda evitar todo viaje por carretera; con controles armados, calor extremo y sin atención veterinaria disponible, el perro no tiene margen de error. Plan B: dejarlo en Uganda."),
    ("Regreso a la UE desde Sudán del Sur", "permitido con condiciones", "País no listado: vía A con titulación antirrábica hecha EN ESPAÑA antes de salir, más certificado sanitario de entrada a la UE y control en Punto de Control Fronterizo. Sin la titulación previa, el perro no vuelve."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje a Sudán del Sur (Ministerio de Asuntos Exteriores, UE y Cooperación, actualización de 28 de marzo de 2025)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n%20del%20Sur"),
    ("MAEC · Embajada de España en Jartum: «También somos tu embajada en Sudán del Sur» (demarcación consular, direcciones y teléfonos; consultada el 18 de septiembre de 2026)", "https://www.exteriores.gob.es/Embajadas/jartum/es/Embajada/tambien-somos-tu-embajada-en/Paginas/Sud%C3%A1n-del-Sur.aspx"),
    ("FCDO · South Sudan travel advice: entry requirements (Gobierno del Reino Unido, actualización de 25 de agosto de 2026)", "https://www.gov.uk/foreign-travel-advice/south-sudan/entry-requirements"),
    ("Government of Canada · Travel advice and advisories for South Sudan (actualización de 1 de septiembre de 2026)", "https://travel.gc.ca/destinations/south-sudan"),
    ("TravelHealthPro · South Sudan (National Travel Health Network and Centre, Reino Unido, contenido a agosto de 2026)", "https://travelhealthpro.org.uk/countries/south-sudan"),
    ("Ministry of Foreign Affairs and International Cooperation of South Sudan · Visas (portal oficial, consultado el 18 de septiembre de 2026)", "https://mofaic.gov.ss/visas/"),
    ("Wikipedia · Visa policy of South Sudan (consultada el 18 de septiembre de 2026)", "https://en.wikipedia.org/wiki/Visa_policy_of_South_Sudan"),
    ("Wikivoyage · South Sudan travel guide (entrada por tierra, visados en frontera, registro, conducción; dato de abril de 2024, consultada en 2026)", "https://en.wikivoyage.org/wiki/South_Sudan"),
    ("Wikipedia · Juba International Airport (coordenadas 4,87194 N / 31,60111 E; terminal de 2018)", "https://en.wikipedia.org/wiki/Juba_International_Airport"),
    ("Wikipedia · Nimule (coordenadas 3,59611 N / 32,06361 E; OSBP de febrero de 2020; carretera Yuba–Nimule)", "https://en.wikipedia.org/wiki/Nimule"),
    ("Wikipedia · Elegu (coordenadas 3,56639 N / 32,07056 E; puesto de parada única inaugurado en noviembre de 2018)", "https://en.wikipedia.org/wiki/Elegu"),
    ("East African Community · Uganda and South Sudan commit to enhance cooperation and border operations at the Elegu/Nimule border post", "https://www.eac.int/press-releases/157-trade/3073-uganda-and-south-sudan-commit-to-enhance-cooperation-and-border-operations-at-the-elegu-nimule-border-post"),
    ("Radio Tamazuj · South Sudan–Uganda Elegu border blockade by truckers enters eighth day", "https://www.radiotamazuj.org/en/news/article/south-sudan-uganda-elegu-border-blockade-by-truckers-enters-eighth-day"),
    ("Daily Monitor (Uganda) · Uganda–South Sudan border blockade enters sixth day", "https://www.monitor.co.ug/uganda/news/national/uganda-south-sudan-border-blockade-enters-sixth-day-5445508"),
    ("Pachodo.org · Kenyan transporters warned against using Nimule–Juba highway in South Sudan after 4 PM", "https://pachodo.org/news-from-various-sources/44230-kenyan-transporters-warned-against-using-nimule%E2%80%93juba-highway-in-south-sudan-after-4-pm"),
    ("Tracks4Africa Padkos · Nimule Border Post (Uganda/South Sudan)", "https://tracks4africa.co.za/listings/item/w255961/nimule-border-post-ugandasouth-sudan/"),
    ("carnetdepassage.org · South Sudan (AIT/FIA: no hay organización emisora de CPD en el país; actualización de 15 de noviembre de 2022)", "https://www.carnetdepassage.org/country/south-sudan"),
    ("drone-laws.com · Drone laws in South Sudan (actualización de 21 de enero de 2026)", "https://drone-laws.com/drone-laws-in-south-sudan/"),
    ("Developing Telecoms · Starlink launches services in South Sudan as NCA approves tariffs (16 de julio de 2024)", "https://developingtelecoms.com/telecom-technology/satellite-communications-networks/17010-starlink-launches-services-in-south-sudan-as-nca-approves-tariffs.html"),
    ("African Parks · The world's largest land mammal migration confirmed in South Sudan (censo aéreo presentado el 25 de junio de 2024)", "https://www.africanparks.org/worlds-largest-land-mammal-migration-confirmed-south-sudan"),
    ("African Parks · Badingilo & Boma (fichas de los parques)", "https://www.africanparks.org/the-parks/badingilo-boma"),
    ("Wikipedia · Boma–Badingilo Migratory Landscape", "https://en.wikipedia.org/wiki/Boma%E2%80%93Badingilo_Migratory_Landscape"),
    ("PetTravel.com · South Sudan pet import requirements (fuente comercial, no oficial; consultada el 18 de septiembre de 2026)", "https://www.pettravel.com/information/pet-passports/south-sudan-pet-import-requirements/"),
    ("D+C Development and Cooperation · Paralysed by fuel shortages: how fuel shortages in South Sudan lead to water shortages", "https://www.dandc.eu/en/article/fuel-shortages-south-sudan-lead-water-shortages"),
    ("Eye Radio (Yuba) · Fuel prices shoot up to SSP 2,995 per liter in Juba", "https://www.eyeradio.org/fuel-prices-shoot-up-to-ssp2995-per-liter-in-juba/"),
    ("Wikipedia · Roads in South Sudan", "https://en.wikipedia.org/wiki/Roads_in_South_Sudan"),
    ("Wikipedia · South Sudan Civil Aviation Authority", "https://en.wikipedia.org/wiki/South_Sudan_Civil_Aviation_Authority"),
    ("Wikipedia · Juba–Nimule Road", "https://en.wikipedia.org/wiki/Juba%E2%80%93Nimule_Road"),
    ("evisa.gov.ss · Portal oficial del eVisa de Sudán del Sur", "https://www.evisa.gov.ss/"),
    ("Travel.State.gov · South Sudan travel advisory (Departamento de Estado de EE. UU.)", "https://travel.state.gov/en/international-travel/travel-advisories/south-sudan.html"),
    ("Travel.State.gov · South Sudan international travel information (Departamento de Estado de EE. UU.: sin visado a la llegada, registro en 3 días, permiso de fotografía de 50 USD, permiso internacional de conducción y seguro obligatorio; aviso de nivel 4 de 17 de mayo de 2026)", "https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/SouthSudan.html"),
    ("Travel and Tour World · South Sudan travel sees limited road access and strict permits beyond Juba (4 de septiembre de 2026: «alien travel permits», autorizaciones militares y escolta armada de guardas en parques)", "https://www.travelandtourworld.com/news/article/9312rznc43a2/"),
    ("Embassy of the Republic of South Sudan in Washington D.C. · Visa services (tarifario oficial: 100 USD para pasaportes europeos)", "https://www.ssembassydc.org/visa-services/"),
    ("African Parks · Boma–Badingilo Migratory Landscape becomes South Sudan's first UNESCO World Heritage Site (inscripción de 24 de julio de 2026, unos 12 millones de hectáreas)", "https://www.africanparks.org/boma-badingilo-migratory-landscape-becomes-south-sudans-first-unesco-world-heritage-site"),
    ("Radio Tamazuj · Feature: The cost of moving, inside South Sudan's fuel crisis (19 de julio de 2026: litro en torno a 20.000 SSP; FEWS NET, +45-105 % en tres meses hasta mayo de 2026)", "https://www.radiotamazuj.org/en/news/article/feature-the-cost-of-moving-inside-south-sudans-fuel-crisis"),
    ("COMESA · Yellow Card Management Information System, Status (13 países participantes; Sudán del Sur NO figura)", "https://ycmis.comesa.int/index.php?page=status"),
    ("COMESA Yellow Card · Frequently asked questions (la tarjeta puede emitirse en Sudán del Sur por acuerdos B2B, pero la cobertura opera en países miembros)", "https://comesayellowcard.org/frequently-asked-questions"),
    ("Wikipedia · Bandingilo National Park (coordenadas 5,4328 N / 32,2775 E; 10.000 km²; gestión de African Parks desde agosto de 2022)", "https://en.wikipedia.org/wiki/Bandingilo_National_Park"),
    ("Wikipedia · Kaya, South Sudan (coordenadas 3,55 N / 30,88 E; frente a Oraba, Uganda)", "https://en.wikipedia.org/wiki/Kaya,_South_Sudan"),
    ("United Nations in South Sudan · UN Country Team welcomes Boma-Badingilo as South Sudan's first UNESCO World Heritage site", "https://southsudan.un.org/en/320569-un-country-team-welcomes-historic-moment-boma-badingilo-migratory-landscape-becomes-south"),
    ("Yuba (Wikipedia)", "https://en.wikipedia.org/wiki/Juba"),
    ("MAEC · recomendaciones de viaje Sudán del Sur", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Sud%C3%A1n+del+Sur"),
    ("John Garang (Wikipedia)", "https://en.wikipedia.org/wiki/John_Garang"),
    ("Parque nacional de Nimule (Wikipedia)", "https://en.wikipedia.org/wiki/Nimule_National_Park"),
    ("Rápidos de Fula (Wikipedia)", "https://en.wikipedia.org/wiki/Fula_Rapids"),
    ("Montes Imatong (Wikipedia)", "https://en.wikipedia.org/wiki/Imatong_Mountains"),
    ("Monte Kinyeti (Wikipedia)", "https://en.wikipedia.org/wiki/Kinyeti"),
    ("Mount Kinyeti · SummitPost (ruta y permisos)", "https://www.summitpost.org/mount-kinyeti/761688"),
    ("Torit (Wikipedia)", "https://en.wikipedia.org/wiki/Torit"),
    ("Boma–Badingilo Migratory Landscape · UNESCO nº 1808", "https://whc.unesco.org/en/list/1808/"),
    ("Parque nacional de Boma (Wikipedia)", "https://en.wikipedia.org/wiki/Boma_National_Park"),
    ("El Sudd (Wikipedia)", "https://en.wikipedia.org/wiki/Sudd"),
    ("Sudd wetland · lista indicativa UNESCO", "https://whc.unesco.org/en/tentativelists/6276/"),
    ("Sudán del Sur · Estado parte UNESCO", "https://whc.unesco.org/en/statesparties/ss"),
    ("Bor (Wikipedia)", "https://en.wikipedia.org/wiki/Bor,_South_Sudan"),
    ("Malakal (Wikipedia)", "https://en.wikipedia.org/wiki/Malakal"),
    ("Wau (Wikipedia)", "https://en.wikipedia.org/wiki/Wau,_South_Sudan"),
    ("Estación de ferrocarril de Wau (Wikipedia)", "https://en.wikipedia.org/wiki/Wau_Railway_Station"),
    ("Diócesis católica de Wau (Wikipedia)", "https://en.wikipedia.org/wiki/Roman_Catholic_Diocese_of_Wau"),
    ("Kapoeta (Wikipedia)", "https://en.wikipedia.org/wiki/Kapoeta"),
    ("Rumbek (Wikipedia)", "https://en.wikipedia.org/wiki/Rumbek"),
    ("Condado de Yei River (Wikipedia)", "https://en.wikipedia.org/wiki/Yei,_South_Sudan"),
    ("Aeropuerto de Yei (Wikipedia)", "https://en.wikipedia.org/wiki/Yei_Airport"),
    ("Reserva de fauna de Ez Zeraf (Wikipedia)", "https://en.wikipedia.org/wiki/Ez_Zeraf_Game_Reserve"),
    ("Bahr el Zeraf (Wikipedia)", "https://en.wikipedia.org/wiki/Bahr_el_Zeraf"),
    ("Bentiu (Wikipedia)", "https://en.wikipedia.org/wiki/Bentiu"),
    ("Aweil (Wikipedia)", "https://en.wikipedia.org/wiki/Aweil,_South_Sudan"),
    ("Yirol (Wikipedia)", "https://en.wikipedia.org/wiki/Yirol"),
    ("Lago No (Wikipedia)", "https://en.wikipedia.org/wiki/Lake_No"),
    ("Kajo Keji (Wikipedia)", "https://en.wikipedia.org/wiki/Kajo_Keji"),
]

# Ecuatoria y eje del Nilo · Nimule → Yuba → Imatong → Kapoeta → Bor → Sudd → Malakal
CORRIDOR = [
    (3.63996, 32.10647),
    (3.7, 31.95),
    (3.85507, 31.65683),
    (4.09172, 30.67645),
    (4.84892, 31.58274),
    (4.41024, 32.57404),
    (3.9475, 32.90889),
    (4.77132, 33.59239),
    (5.43278, 32.2775),
    (6.21327, 31.56554),
    (6.49, 33.91),
    (8.0, 31.0),
    (8.8, 30.5),
    (9.49722, 30.45556),
    (9.52799, 31.66823),
]

# Bucle del Bahr el Ghazal · Yuba → Yirol → Rumbek → Wau → Aweil → Bentiu
CORRIDOR_ALT = [
    (4.84892, 31.58274),
    (6.56098, 30.502),
    (6.80725, 29.67889),
    (7.70919, 27.98347),
    (8.76709, 27.39984),
    (9.23149, 29.8005),
]

HISTORIA_RESUMEN = "Sudán del Sur es el Estado más joven del mundo: se independizó de Sudán el 9 de julio de 2011 tras un referéndum en el que el 98,83 % votó por la separación, según el MAEC español. Detrás quedaban dos guerras civiles sudanesas y casi medio siglo de combates. La paz duró poco: en diciembre de 2013 estalló una guerra entre el presidente Salva Kiir y su antiguo vicepresidente Riek Machar que dejó unos 400.000 muertos hasta 2018. El acuerdo revitalizado de 2018 y el gobierno de unidad de 2020 nunca se consolidaron, las elecciones se han aplazado cinco veces y Machar fue detenido en marzo de 2025. Freedom House clasifica el país como «no libre», con 1 punto sobre 100."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>El poblamiento de la cuenca del Nilo Blanco es muy antiguo. Según la Wikipedia en inglés, pueblos protonilóticos comenzaron a desplazarse hacia las regiones del Alto Nilo hacia el año 3000 a.C., y la gran expansión nilótica desde las marismas del Sudd se produjo en el siglo XIV, coincidiendo con el desmoronamiento de los reinos cristianos de Nubia. De esos movimientos salen los grupos que todavía hoy estructuran el país.</p><p>La formación política más sólida fue el reino shilluk. La tradición sitúa entre 1490 y 1517 al líder Nyikang, que impuso su dominio a lo largo del Nilo Blanco, y entre 1690 y 1710 al <em>reth</em> Tugo, que fijó la capital en Fashoda. Los shilluk controlaban el tráfico fluvial y mantenían una monarquía sagrada que impresionó después a los administradores europeos. Por el suroeste, los azande entraron en el actual Sudán del Sur en el siglo XVI y levantaron jefaturas sólidas en la frontera con el Congo.</p><p>Dinka y nuer, en cambio, no construyeron Estados centralizados: eran sociedades ganaderas, móviles y segmentarias, organizadas en torno al ganado y a la trashumancia estacional entre pantano y sabana. El <strong>Sudd</strong>, la inmensa marisma del Nilo, actuó durante siglos como barrera natural frente a cualquier penetración desde el norte.</p>"),
    ("Colonización",
     "<p>La conquista llegó desde Egipto. En 1821 el sultanato Funj se derrumbó ante la invasión ordenada por Muhammad Alí, y entre 1839 y 1842 las expediciones del almirante Salim Qabudan remontaron el Nilo hasta la zona de Yuba. En 1851 la región se abrió a comerciantes y misioneros europeos, y con ellos llegó la peor herencia del periodo turco-egipcio: entre las décadas de 1850 y 1870 el comercio de esclavos se disparó hasta unas treinta mil personas esclavizadas al año a mediados de 1870, según la Wikipedia en inglés. Samuel Baker fue nombrado gobernador de Ecuatoria en 1869 y Charles Gordon en 1874, con el encargo formal de reprimir ese tráfico.</p><p>Tras el incidente de Fashoda se estableció en 1899 el <strong>condominio anglo-egipcio</strong>. Londres gobernó el sur como un territorio aparte: en 1905 un decreto restringió la actividad misionera al norte del paralelo diez, en 1922 entró en vigor la <em>Closed District Ordinance</em> que aisló administrativamente el sur, y en 1928 el documento de política meridional de Harold MacMichael consagró esa separación.</p><p>El resultado fue un sur cristianizado por las misiones, escolarizado en inglés y deliberadamente desconectado del norte árabe y musulmán, sin apenas administración ni infraestructuras. El propio MAEC recuerda que el país conserva hoy en torno a doscientos kilómetros de carretera asfaltada.</p>"),
    ("Independencia y construcción del Estado",
     "<p>La independencia de Sudán llegó en 1956 sin resolver esa fractura. Cuatro meses antes, el 18 de agosto de 1955, el motín de la guarnición de Torit abrió la <strong>primera guerra civil sudanesa</strong>, que se prolongó hasta 1972. En 1962 varios grupos guerrilleros del sur se unieron bajo el nombre de Anyanya. El acuerdo de Adís Abeba de 1972 puso fin a los combates y creó la Región Autónoma del Sur de Sudán.</p><p>La tregua duró once años. El 5 de junio de 1983 Jartum abolió la autonomía e impuso la sharía en todo el país, y estalló la <strong>segunda guerra civil</strong>. Ese mismo año nació el Ejército y Movimiento de Liberación del Pueblo de Sudán, el <strong>SPLA/SPLM</strong>, dirigido por <strong>John Garang</strong>, un coronel dinka formado en Estados Unidos que defendía un «Sudán nuevo» unido y laico antes que la secesión.</p><p>La guerra fue también interna. En 1991 la facción de Nasir, encabezada por Riek Machar, se escindió del SPLA y la masacre de Bor dejó unos dos mil civiles muertos. Ese cisma entre dinka y nuer marcaría todo lo que vino después. La Wikipedia en español cifra en unos dos millones los muertos del conflicto entre 1983 y 2005, en su mayoría por hambre y desplazamiento.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>El <strong>Acuerdo General de Paz</strong> de 2005, negociado en Kenia, cerró la segunda guerra y abrió un periodo transitorio con derecho de autodeterminación. El referéndum se celebró entre el 9 y el 15 de enero de 2011 y arrojó un 98,83 % a favor. El 9 de julio de 2011 Sudán del Sur proclamó la independencia con Salva Kiir Mayardit como primer presidente. En enero de 2012 cerró su producción petrolera por una disputa de tarifas con Sudán y el PIB cayó un 48 %.</p><p>El 15 de diciembre de 2013 los combates entre guardias presidenciales en el barrio de Munuki, en Yuba, abrieron la <strong>guerra civil sursudanesa</strong>. Kiir denunció un golpe; Machar lo negó. El acuerdo de 2015 fracasó tras los combates de julio de 2016 en Yuba, con más de trescientos muertos. En abril de 2018 se estimaban unos 400.000 muertos y más de cuatro millones de desplazados; en 2017 se había declarado hambruna.</p><p>El 12 de septiembre de 2018 se firmó el acuerdo revitalizado, y el 22 de febrero de 2020 Kiir y Machar formaron un gobierno de unidad. Desde abril de 2023 la guerra de Sudán mantiene paralizado el oleoducto hacia Port Sudán. El 26 de marzo de 2025 Machar fue puesto en arresto domiciliario y el 11 de septiembre acusado de asesinato, traición y crímenes contra la humanidad.</p>"),
    ("Política y gobierno en 2026",
     "<p>Sudán del Sur es formalmente una <strong>república presidencialista</strong>, según el MAEC. <strong>Salva Kiir Mayardit</strong> es jefe de Estado y de Gobierno desde el 9 de julio de 2011; llegó al poder al frente del SPLM tras el acuerdo de 2005. Riek Machar figura como primer vicepresidente desde el 21 de febrero de 2020, pero está suspendido desde septiembre de 2025; Human Rights Watch denuncia que pasó seis meses incomunicado antes de conocer los cargos.</p><p>Las primeras elecciones generales están convocadas para el <strong>22 de diciembre de 2026</strong>, fecha confirmada por la Comisión Nacional de Elecciones en junio de 2026 tras cinco aplazamientos desde 2015. A fecha de septiembre de 2026, <strong>Freedom House</strong> (informe 2025) clasifica el país como <em>Not Free</em> con <strong>1 punto sobre 100</strong>: −3 sobre 40 en derechos políticos y 4 sobre 60 en libertades civiles. Es, en la práctica, un régimen autoritario: nunca ha habido comicios nacionales y la corrupción es generalizada.</p><p>Reporteros Sin Fronteras lo sitúa en el puesto 118 de 180 en 2026, con al menos nueve periodistas asesinados desde 2014. España reconoció pronto la independencia y lo atiende desde la embajada en Jartum —trasladada a El Cairo en septiembre de 2023—, con consulado honorario en Yuba y 11,3 millones de euros de ayuda humanitaria desde 2011. El MAEC indica que no hay acuerdos firmados entre la UE y el país.</p>"),
    ("Economía y recursos",
     "<p>La economía es, casi literalmente, el petróleo: según la Wikipedia en español aporta más del 98 % del presupuesto estatal. Al independizarse, el país se quedó con cerca de tres cuartas partes de la producción del antiguo Sudán, casi medio millón de barriles diarios, pero los yacimientos están en el interior y la única salida al mar es el oleoducto que atraviesa Sudán hasta Port Sudán.</p><p>Esa dependencia ha sido ruinosa. El cierre de 2012 hundió el PIB un 48 %; en 2013 la producción había bajado a 222.000 barriles diarios; y desde abril de 2023 los combates en Sudán junto a los oleoductos han paralizado la exportación. El MAEC describe suspensión de pagos a los funcionarios, conflictividad social creciente y colapso de las infraestructuras. La moneda es la <strong>libra sursudanesa</strong>, con una inflación que llegó al 79,5 % en mayo de 2012.</p><p>En 2021 las exportaciones sumaron 564 millones de dólares, el 80,8 % crudo, con China como cliente del 79,6 %. El MAEC da un PIB nominal de 1.750 millones de dólares en 2023; la Wikipedia en inglés estima un PIB per cápita nominal de unos 313 dólares en 2025, de los más bajos del mundo. El índice de desarrollo humano es de 0,381, puesto 192 de 193, y el 67,3 % vivía bajo el umbral de pobreza en 2017. Hay oro, diamantes y cobre sin explotar.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>El Banco Mundial cifraba la población en 11,48 millones en 2023; Yuba ronda los 564.000. El <strong>inglés</strong> es el idioma oficial de trabajo del Estado y la enseñanza, y unas sesenta lenguas indígenas tienen rango de nacionales: dinka, con 1,35 millones de hablantes, y nuer, con 740.000. Por carretera se habla el <strong>árabe de Yuba</strong>, un criollo que sirve de lengua franca.</p><p>En religión, el Pew Research Center daba en 2020 un 60,5 % de cristianos, un 32,9 % de creencias tradicionales y un 6,2 % de musulmanes. Los grupos son sobre todo nilóticos: dinka en torno al 40 %, nuer al 20 % y azande al 10 %. En música domina el afrobeat; el artista más conocido es Emmanuel Jal.</p><p>El país ratificó la Convención del Patrimonio Mundial en 2016 y en 2026 inscribió su primer bien: el <strong>paisaje migratorio de Boma-Badingilo</strong>, 11,2 millones de hectáreas, a la vez en la Lista del Patrimonio en Peligro. Un censo aéreo de African Parks presentado el 25 de junio de 2024 estimó <strong>5.896.373 antílopes</strong>, la mayor migración terrestre de mamíferos del mundo. Para quien viaje: vestir con discreción, pedir permiso antes de fotografiar y nunca hacerlo a militares o edificios oficiales; respetar el ramadán, que en 2027 empieza hacia el 8 de febrero; el alcohol es normal en el sur cristiano, pero no en todas partes.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Sudán del Sur (MAEC España · PDF · actualizada 2025)", "https://www.exteriores.gob.es/Documents/FichasPais/SUDANDELSUR_FICHA%20PAIS.pdf"),
    ("South Sudan: Freedom in the World 2025 (Freedom House · 2025)", "https://freedomhouse.org/country/south-sudan/freedom-world/2025"),
    ("South Sudan — History (Encyclopædia Britannica · consultada 2026)", "https://www.britannica.com/place/South-Sudan/History"),
    ("South Sudan (Encyclopædia Britannica · consultada 2026)", "https://www.britannica.com/place/South-Sudan"),
    ("Sudán del Sur (Wikipedia en español · consultada 2026)", "https://es.wikipedia.org/wiki/Sud%C3%A1n_del_Sur"),
    ("South Sudan (Wikipedia en inglés · consultada 2026)", "https://en.wikipedia.org/wiki/South_Sudan"),
    ("History of South Sudan (Wikipedia en inglés · consultada 2026)", "https://en.wikipedia.org/wiki/History_of_South_Sudan"),
    ("South Sudanese Civil War (Wikipedia en inglés · consultada 2026)", "https://en.wikipedia.org/wiki/South_Sudanese_Civil_War"),
    ("2026 South Sudanese general election (Wikipedia en inglés · consultada 2026)", "https://en.wikipedia.org/wiki/2026_South_Sudanese_general_election"),
    ("Riek Machar (Wikipedia en inglés · consultada 2026)", "https://en.wikipedia.org/wiki/Riek_Machar"),
    ("Vice President of South Sudan (Wikipedia en inglés · consultada 2026)", "https://en.wikipedia.org/wiki/Vice_President_of_South_Sudan"),
    ("South Sudan — States Parties (UNESCO Centro del Patrimonio Mundial · consultada 2026)", "https://whc.unesco.org/en/statesparties/ss"),
    ("Boma–Badingilo Migratory Landscape (UNESCO Centro del Patrimonio Mundial · inscrito 2026)", "https://whc.unesco.org/en/list/1808/"),
    ("The World's Largest Land Mammal Migration Confirmed in South Sudan (African Parks · 25 junio 2024)", "https://www.africanparks.org/worlds-largest-land-mammal-migration-confirmed-south-sudan"),
    ("South Sudan: Ensure Due Process, Fair Trials of Opposition (Human Rights Watch · 15 septiembre 2025)", "https://www.hrw.org/news/2025/09/15/south-sudan-ensure-due-process-fair-trials-of-opposition"),
    ("South Sudan (Reporteros Sin Fronteras · Clasificación Mundial 2026)", "https://rsf.org/en/country/south-sudan"),
]

SPEC = dict(
    slug="sudan-del-sur", name="Sudán del Sur", revision="18 sep 2026",
    sub="EXCLUIDO POR PROTOCOLO — el MAEC desaconseja el viaje bajo cualquier circunstancia · ficha informativa",
    chips=[
        ("ESTATUS", "EXCLUIDO POR PROTOCOLO. MAEC 28-03-2025: se desaconseja el viaje bajo cualquier circunstancia a todo el país…"),
        ("CÓMO LLEGAR", "En la práctica, en avión a Yuba (JUB) desde Nairobi, Adís Abeba, El Cairo o Dubái…"),
        ("VISADO", "OBLIGATORIO para españoles. eVisa en evisa.gov.ss o Embajada de Sudán del Sur en París…"),
        ("VEHÍCULO", "No hay organización emisora de CPD en el país (carnetdepassage.org, 15-11-2022)…"),
        ("SEGURIDAD", "MAEC: no viajar bajo ninguna circunstancia"),
        ("SEGURO", "Sin cobertura: ni Carta Verde ni COMESA Yellow Card"),
        ("SALUD", "Fiebre amarilla OBLIGATORIA · malaria alta"),
        ("DRONES", "Prohibidos a extranjeros · fotos con permiso (50 USD)"),
        ("STARLINK", "Operativo desde julio de 2024 (licencia NCA)"),
        ("4x4", "Obligatorio fuera de Yuba · permiso y minas"),
        ("A PIE", "Descartado · asaltos armados día y noche"),
        ("PERRO", "Rabia entre 30 días y 12 meses antes, certificado veterinario emitido dentro de los 10 días previos y…"),
        ("MONEDA", "Libra sursudanesa (SSP). MAEC (febrero de 2025): ~130 SSP por dólar…"),
        ("VENTANA", "Tropical con estación de lluvias de abril-mayo a octubre-noviembre: las pistas no…"),
    ],
    center=[6.58, 30.69], zoom=6,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Ecuatoria y eje del Nilo · Nimule → Yuba → Imatong → Kapoeta → Bor → Sudd → Malakal",
    corridor_alt_label="Bucle del Bahr el Ghazal · Yuba → Yirol → Rumbek → Wau → Aweil → Bentiu",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Ugandan_kob_(Kobus_kob_thomasi)_male.jpg?width=1200",
    hero_credit="Parque nacional de Badingilo · Charles J. Sharp · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Sudán del Sur queda fuera de la ruta de 2027 por protocolo, no por logística. El MAEC, en su actualización de 28 de marzo de 2025, DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a todo el país e insta a los españoles a abandonarlo; el FCDO y Canadá (1 de septiembre de 2026) mantienen «avoid all travel», y Canadá añade «avoid all overland travel». Con esa redacción ninguna póliza de la expedición cubre el país, y sin cobertura no se entra: la misma regla que aplicamos a Libia y a Sudán. Además el corredor natural —Egipto y Sudán— está roto por la guerra desde abril de 2023, así que solo sería alcanzable subiendo desde Uganda por Nimule y volviendo por el mismo sitio: un fondo de saco de unos 400 km entre Elegu y Yuba que no encaja en la media de 250 km/día. Hay un motivo real para volver algún día: el 24 de julio de 2026 el paisaje migratorio Boma–Badingilo fue inscrito como primer Patrimonio Mundial de la UNESCO del país, con seis millones de antílopes. Si se rebajan los avisos, la forma sensata sería hacerlo aparte: vuelo a Yuba desde Nairobi o Entebbe, coche con conductor local y salida guiada a Boma o Badingilo con operador acreditado y escolta de guardas, del orden de 3.500–6.000 euros por persona y diez días, dejando los 4x4 y el perro en Uganda. Habría que decidir quién asegura, quién custodia los vehículos y qué se hace con el perro.",
    facts=[
        ("Estatus", "EXCLUIDO POR PROTOCOLO. MAEC 28-03-2025: se desaconseja el viaje bajo cualquier circunstancia a todo el país; FCDO y Canadá, «avoid all travel»."),
        ("Cómo llegar", "En la práctica, en avión a Yuba (JUB) desde Nairobi, Adís Abeba, El Cairo o Dubái. Por tierra, solo el corredor Uganda–Nimule tiene tráfico civil normal."),
        ("Visado", "OBLIGATORIO para españoles. eVisa en evisa.gov.ss o Embajada de Sudán del Sur en París, acreditada ante España. Tarifa de 100 USD para pasaportes europeos (Embajada de Sudán del Sur en Washington). SIN visado a la llegada."),
        ("Vehículo/aduana", "No hay organización emisora de CPD en el país (carnetdepassage.org, 15-11-2022). Para el vehículo extranjero se usa laissez-passer/admisión temporal en frontera: procedimiento POR CONFIRMAR."),
        ("Seguro", "La Carta Verde NO cubre el país y Sudán del Sur NO figura entre los 13 países del sistema COMESA Yellow Card. EE. UU. indica que conducir exige seguro de responsabilidad civil contratado con el Gobierno sursudanés."),
        ("Moneda", "Libra sursudanesa (SSP). MAEC (febrero de 2025): ~130 SSP por dólar. No se admiten tarjetas extranjeras ni hay cajeros fiables; se viaja con dólares en efectivo posteriores a 2006."),
        ("Perro", "Rabia entre 30 días y 12 meses antes, certificado veterinario emitido dentro de los 10 días previos y refrendado por veterinario oficial; entrada de mascotas por el aeropuerto de Yuba (PetTravel). Sin web oficial nacional localizada."),
        ("Drones", "Sin normativa codificada. Drone-laws.com (21-01-2026): los vuelos de visitantes extranjeros «no están permitidos». Fotografiar sin permiso del Ministerio de Información ya es motivo de detención."),
        ("Starlink", "Operativo. Licencia provisional de la National Communication Authority a finales de junio de 2024 y lanzamiento en julio de 2024, con tarifas aprobadas y pago en libras sursudanesas."),
        ("Seguridad", "Delincuencia violenta generalizada, secuestros, robos a mano armada en Yuba de día y de noche, toque de queda no oficial de 19:00 a 06:00 y emboscadas diarias en carretera (MAEC)."),
        ("Clima", "Tropical con estación de lluvias de abril-mayo a octubre-noviembre: las pistas no asfaltadas se vuelven intransitables (Wikivoyage). La ventana practicable es diciembre–marzo."),
        ("Sanidad", "«Muy deficientes» según el MAEC, con servicios básicos solo en Yuba y pago en efectivo por adelantado. Evacuación médica internacional obligatoria de facto."),
    ],
    alerts=[
        "MAEC, 28 de marzo de 2025: SE DESACONSEJA EL VIAJE BAJO CUALQUIER CIRCUNSTANCIA a todo el país, y se pide a los españoles que ya estén allí que lo abandonen inmediatamente.",
        "Con ese nivel de aviso, ninguna de las pólizas de viaje, asistencia en carretera ni evacuación de la expedición da cobertura: entrar significa viajar sin seguro.",
        "Canadá (1 de septiembre de 2026) recomienda literalmente evitar TODO desplazamiento por carretera dentro del país; hay controles, minas antipersona y bloqueos.",
        "El MAEC señala como especialmente peligrosos los estados de Unity, Alto Nilo y Jonglei, con milicias activas también en Ecuatoria Central y Occidental y Bahr el Ghazal Occidental.",
        "La frontera con Sudán es zona de conflicto armado activo desde abril de 2023: el corredor Egipto–Sudán–Sudán del Sur, que sería la vía natural de la expedición, está roto.",
        "En Yuba hay asaltos a mano armada de día y de noche; el MAEC recomienda no oponer resistencia y no circular con menos de dos ocupantes por vehículo.",
        "Toque de queda no oficial entre las 19:00 y las 06:00 en Yuba, con calles casi sin iluminación (MAEC).",
        "Salir de Yuba exige «alien travel permit» y, según destino, autorización militar adicional; en los parques nacionales la visita requiere escolta armada de guardas (Travel and Tour World, 4 de septiembre de 2026).",
        "No se admiten tarjetas de crédito extranjeras ni hay cajeros fiables: todo el viaje se financia con dólares en efectivo, lo que multiplica el riesgo de robo.",
        "La escasez crónica de combustible derivada del corte del oleoducto por la guerra de Sudán provoca colas, racionamiento y precios de mercado negro.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada por Nimule", "Frontera de Elegu (Uganda) → Nimule → P.N. de Nimule y rápidos de Fula", "~20 km · 1 día (trámites de frontera)"),
        ("2 · Nimule → Yuba", "Nimule → Yuba por la A43 asfaltada", "~192 km · 1 día"),
        ("3 · Yuba", "Mausoleo de John Garang, Konyo Konyo, Nilo Blanco; visados, permisos y combustible", "0 km · 2 días"),
        ("4 · Yuba → Torit", "Yuba → Torit por la carretera de Lokichoggio", "~150 km · 1 día"),
        ("5 · Torit → Katire → Kinyeti", "Torit → Katire en 4x4 y trek de ida y vuelta al monte Kinyeti", "~60 km · 4–5 días (3–4 de trek)"),
        ("6 · Torit → Kapoeta", "Torit → Kapoeta, país toposa", "~125 km · 1 día"),
        ("7 · Kapoeta → Yuba", "Regreso por la misma carretera", "~275 km · 2 días"),
        ("8 · Yuba → Bor", "Yuba → Bor por la autovía asfaltada; borde de Badingilo y del Sudd", "~190 km (por confirmar) · 1 día"),
        ("9 · Bor → Yuba → Yirol", "Vuelta a Yuba y subida a Yirol por la A43", "~500 km · 2 días"),
        ("10 · Yirol → Rumbek", "Yirol → Rumbek por pista", "~110 km (por confirmar) · 1 día"),
        ("11 · Rumbek → Wau", "Rumbek → Wau por la A43", "~270 km · 1–2 días"),
        ("12 · Wau → Aweil", "Wau → Aweil por la B43 norte, junto al trazado del ferrocarril", "~170 km (por confirmar) · 1 día"),
        ("13 · Wau → Yuba", "Regreso Wau → Rumbek → Yuba", "~650 km · 3 días"),
        ("14 · Yuba → Kajo-Keji → Nimule", "Yuba → Kajo-Keji por pista y bajada a Nimule para salir a Uganda", "~200 km · 2 días"),
    ],
    offroad=[
        "Solo hay dos tramos de asfalto continuo útiles: la A43 Yuba–Nimule (192 km, asfaltada por USAID entre 2007 y 2012, contratista principal Louis Berger, unos 225 millones de dólares) y la autovía Yuba–Bor; todo lo demás es pista.",
        "La Yuba–Nimule sale de la rotonda de Custome en Yuba, cruza el Nilo Blanco por el puente de Yuba y baja por Sirsiri hasta la frontera; tiene un cruce en T con la carretera de Torit en Likiberi, que es por donde se entra a Ecuatoria Oriental.",
        "La subida a los Imatong es la única pista 4x4 con descripción técnica publicada: de Torit a Katire, «pista de tierra recientemente nivelada», 1,5–2 horas de 4x4 según SummitPost, y el permiso se saca en el Ministerio de Fauna, Conservación y Turismo de Torit, junto al mercado principal.",
        "Wau es el nudo de pistas del oeste: B38 al norte a Gogrial, B43 al sur a Tonj, A44 al sur a Tumbura, B41 al oeste a Raga y B43 al norte a Aweil; ninguna asfaltada de punta a punta.",
        "ZONAS VETADAS DE FACTO: el MAEC describe Unidad, Alto Nilo y Jonglei sumidos en violencia y desorden permanente, y Ecuatoria Central y Occidental y Bahr el Ghazal Occidental como igualmente peligrosas por milicias locales, además de las zonas fronterizas y la frontera sudanesa.",
        "Canadá es todavía más taxativo con la conducción: «debe evitar todo desplazamiento por carretera en Sudán del Sur, incluso acompañado de un guía experimentado», y advierte de que los controles son frecuentes y se montan de noche, con los documentos del vehículo siempre a mano.",
        "Badingilo, Boma y Ez Zeraf EXIGEN acuerdo previo: los dos primeros los gestiona African Parks desde el 25 de agosto de 2022 con un contrato a diez años, y ninguna de sus páginas publica accesos, permisos ni tarifas para visitantes; Ez Zeraf es una isla fluvial sin acceso rodado.",
        "Ventana de conducción: diciembre–marzo. El MAEC señala que los asaltos aumentan en la estación lluviosa (abril–noviembre) y SummitPost añade que con lluvia las pistas del este se vuelven intransitables.",
    ],
    senderismo=[
        "Monte Kinyeti (3.187 m) desde Katire: la gran caminata del país, 3 días para gente en forma y 4 para la mayoría, con guía local y machete para abrir camino; agua cada 2–3 horas según SummitPost.",
        "Bosque montano de los Imatong entre 1.000 y 2.900 m: recorridos de un día por podocarpos, crotones, macarangas y albizias dentro de la reserva forestal central de 1.100 km² creada en 1952.",
        "Gilo, en la ladera norte de los Imatong: subida a la aldea y al viejo puesto de observación británico de hacia 1929, a unos 2.200 m.",
        "Rápidos de Fula, 6,5 km al norte de Nimule: paseo corto hasta el salto del Nilo donde se proyecta la central hidroeléctrica; solo con guarda del parque.",
        "Ribera del Nilo Blanco en Yuba, entre el puente y el puerto fluvial: paseo urbano de una hora, el único andar tranquilo del país y aun así solo de día.",
        "Tierras altas didinga, al sur de Kapoeta: caminatas por el escalón fértil que contrasta con las llanuras toposa. SIN RUTA DOCUMENTADA: itinerarios y accesos POR CONFIRMAR.",
        "Orillas de los lagos Yirol, Nyiboor y Anyii: caminatas cortas de observación de aves y pesca dinka. Sin señalización ni rutas publicadas.",
        "AVISO GENERAL: ninguna de estas caminatas tiene señalización, mapa oficial ni rescate; el FCDO desaconseja todo viaje al país (actualizado el 25 de agosto de 2026) y Canadá pide evitar todo desplazamiento terrestre.",
    ],
    acampada=[
        "Campamento de Katire, al pie de los Imatong: es el ÚNICO camping con descripción publicada que he encontrado, «excelente, con instalaciones limpias y agua cerca» según SummitPost; es la base lógica para el trek al Kinyeti.",
        "Yuba: no hay camping. El alojamiento real son compounds vallados con guardia (hoteles y bases de ONG) donde se puede aparcar y dormir en los vehículos previa negociación. Tarifas y nombres: POR CONFIRMAR, ninguna fuente abierta fiable.",
        "ACAMPADA LIBRE: desaconsejada en todo el país. El MAEC describe ataques, emboscadas y controles militares diarios en todas las carreteras y atracos a mano armada en Yuba a cualquier hora; Canadá advierte de que los controles se montan con frecuencia después del anochecer.",
        "iOverlander: NO he podido consultar registros de Sudán del Sur; las búsquedas solo devuelven la portada y fichas de otros países. El país está prácticamente vacío en la base de datos.",
        "Tracks4Africa y Lonely Planet: no he localizado fichas de camping para Sudán del Sur con acceso abierto. Fuente que falla.",
        "Parques nacionales: Badingilo y Boma no publican zonas de acampada ni normas de pernocta. African Parks no difunde información de visita para estos dos parques. POR CONFIRMAR con la organización.",
        "Bor, Rumbek, Wau y Aweil: posible pernocta en recintos de misión o de ONG, práctica habitual entre cooperantes, pero sin ninguna referencia publicada de precios ni condiciones.",
        "Regla práctica para la expedición: pernoctar SIEMPRE dentro de recinto vallado con vigilancia y no conducir de noche en ningún tramo, ni siquiera en la A43 asfaltada.",
    ],
    visado=[
        "OBLIGATORIO para españoles. Pasaporte con validez mínima de seis meses —la Embajada de Sudán del Sur en Washington pide 180 días desde la llegada— y DOS hojas libres sin sellar (MAEC).",
        "NO HAY VISADO A LA LLEGADA. El Departamento de Estado de EE. UU. lo dice expresamente («no visa on arrival available… you must apply for and obtain a visa before arriving») y el Gobierno de Canadá lo confirma. Wikivoyage menciona visados en frontera por 100 USD: NO fiarse.",
        "Dos vías oficiales: eVisa en https://www.evisa.gov.ss/ (cuenta, pago con tarjeta y descarga del PDF en 72 horas; el MAEC advierte de problemas técnicos frecuentes) o solicitud presencial en la Embajada de Sudán del Sur en París, acreditada ante España, +33 1 4563 7273. También se tramita en Egipto, Kenia, Uganda y Etiopía.",
        "COSTE: 100 USD para titulares de pasaporte europeo, según el tarifario de la Embajada de Sudán del Sur en Washington (50 USD para países africanos limítrofes, gratis para la Comunidad de África Oriental y Egipto, 160 USD para estadounidenses). Se exige carta de invitación u organizativa que explique el motivo del viaje.",
        "Certificado internacional de vacunación contra la FIEBRE AMARILLA exigido en el control de entrada desde los 9 meses de edad y válido de por vida (TravelHealthPro, agosto de 2026; FCDO, 25 de agosto de 2026). Kenia y Etiopía también lo piden a la salida.",
        "REGISTRO obligatorio tras la llegada: el Departamento de Estado de EE. UU. indica inscripción en el Department of Immigration and Aliens Control del Ministerio del Interior, en Yuba, si la estancia supera los 3 días. El FCDO habla de 5 días en comisaría local y Wikivoyage de 72 horas: hacerlo el primer día hábil y no discutir el plazo.",
    ],
    fronteras_rows=[
        ("Aeropuerto internacional (vía real de entrada)", "Aeropuerto Internacional de Yuba (JUB/HJJJ), 4,87194 N / 31,60111 E", "Terminal nueva inaugurada el 29 de octubre de 2018. Vuelos a Nairobi (Kenya Airways), Adís Abeba (Ethiopian), El Cairo (Egyptair), Dubái (flydubai) y Port Sudan (Tarco); Turkish Airlines suspendido. Es también el ÚNICO punto de entrada admitido para mascotas (PetTravel). Fuente: Wikipedia, Juba International Airport."),
        ("Paso terrestre principal con Uganda", "Nimule (Sudán del Sur) / Elegu (Uganda), 3,59611 N / 32,06361 E y 3,56639 N / 32,07056 E", "ABIERTO y es el paso principal: puesto fronterizo de parada única (OSBP) inaugurado en noviembre de 2018 en el lado ugandés y en febrero de 2020 en el de Nimule. Wikivoyage confirma que cruzar desde Uganda «es posible» (dato de abril de 2024). Sufre bloqueos periódicos de transportistas. Carretera Yuba–Nimule, 197 km asfaltados, con aviso a transportistas kenianos de no circular después de las 16:00. Fuentes: Wikipedia (Nimule, Elegu), EAC, Wikivoyage."),
        ("Paso terrestre secundario con Uganda", "Kaya (Ecuatoria Central, condado de Morobo), 3,55 N / 30,88 E, frente a Oraba (Uganda)", "Centro comercial activo con tráfico de Sudán del Sur, Uganda y RD Congo; el trifinio con RDC queda pocos kilómetros al sur. Infraestructura recuperada progresivamente desde 2005, con banca y mercados. NO se ha localizado fuente fechada que confirme su estado para extranjeros en 2025-2026: POR CONFIRMAR. Fuente: Wikipedia, Kaya, South Sudan."),
        ("Paso terrestre con Kenia", "Nadapal / Nakodok (Kenia–Sudán del Sur, corredor Lokichoggio–Kapoeta)", "Ruta remota en zona de conflicto intercomunitario (Estado de Ecuatoria Oriental). No se ha localizado fuente fechada que confirme su apertura ordinaria a extranjeros. POR CONFIRMAR."),
        ("Pasos terrestres con Sudán", "Renk y Joda (Estado del Alto Nilo)", "NO UTILIZABLES. Zona de conflicto armado activo desde abril de 2023 y punto de entrada masiva de refugiados y retornados que huyen de Sudán (Wikivoyage). El MAEC califica la frontera con Sudán como zona de conflicto armado activo."),
        ("Paso terrestre con la República Centroafricana", "Bambouti (triple frontera RCA–Sudán del Sur)", "NO UTILIZABLE en la práctica: zona sin control estatal efectivo a ambos lados. Sin fuente abierta que documente un cruce civil. POR CONFIRMAR / descartado."),
        ("Paso terrestre con RD Congo", "Aba (Haut-Uélé, RDC) – Ecuatoria Occidental", "Sin fuente abierta en esta sesión. El FCDO solo menciona que quien cruce por tierra desde RDC o Uganda puede encontrar cribado sanitario por el brote de Ébola. POR CONFIRMAR."),
        ("Control sanitario en frontera", "Todos los pasos terrestres desde RDC y Uganda", "Cribado sanitario activo por Ébola (FCDO, 25 de agosto de 2026). Canadá advierte de cuarentena de 21 días a la vuelta. Certificado de fiebre amarilla exigido en todos los puntos de entrada."),
        ("Salida hacia Sudán", "Cualquier paso con Sudán (Renk, Joda)", "El Departamento de Estado de EE. UU. advierte de que salir hacia Sudán exige visado o permiso de entrada sudanés obtenido CON ANTELACIÓN. Con la guerra sudanesa activa desde abril de 2023, es una salida inviable."),
        ("Control interno tras la frontera", "Yuba y cualquier desplazamiento fuera de la capital", "Registro en el Department of Immigration and Aliens Control (Ministerio del Interior, Yuba) si se pasa de 3 días, y «alien travel permit» más posible autorización militar para salir de Yuba. Es un segundo filtro tan determinante como la propia frontera. Fuentes: Departamento de Estado de EE. UU.; Travel and Tour World, 4 de septiembre de 2026."),
    ],
    vehiculos=[
        "Se conduce por la DERECHA (Wikivoyage). El Departamento de Estado de EE. UU. indica que conducir en Sudán del Sur exige PERMISO INTERNACIONAL DE CONDUCCIÓN y seguro de responsabilidad civil contratado con el Gobierno: llevar el permiso internacional siempre.",
        "CPD: AIT/FIA no tiene ninguna organización emisora de carnet de passages en Sudán del Sur (carnetdepassage.org, consultado con fecha de actualización de 15 de noviembre de 2022). No consta que el país exija CPD; la entrada del vehículo extranjero se resuelve con laissez-passer o admisión temporal en el puesto fronterizo.",
        "El MAEC no publica el procedimiento aduanero para vehículo propio. El trámite real en Nimule (documento de importación temporal, tasas, plazo) NO está documentado en ninguna fuente abierta en esta sesión: POR CONFIRMAR con la aduana sursudanesa o con la asociación automovilística ugandesa antes de cualquier intento.",
        "Seguro: la Carta Verde europea NO cubre Sudán del Sur, y el país NO figura entre los 13 participantes del sistema COMESA Yellow Card (Burundi, RDC, Yibuti, Eritrea, Etiopía, Kenia, Malaui, Ruanda, Sudán, Tanzania, Uganda, Zambia y Zimbabue). La propia COMESA precisa que la tarjeta PUEDE EMITIRSE en Sudán del Sur por acuerdos B2B, pero la cobertura solo opera mientras se circula por países miembros: NO asegura dentro de Sudán del Sur. Hay que comprar seguro local de responsabilidad civil, que EE. UU. describe como contratado con el Gobierno.",
        "Vehículo: 4x4 obligatorio fuera de Yuba según el Gobierno de Canadá (1 de septiembre de 2026). El Ineos Grenadier y el Delica cumplen, pero la altura libre y los neumáticos mandan: fuera del eje Yuba–Nimule casi todo son pistas de tierra.",
        "Carreteras: salvo el eje asfaltado Yuba–Nimule, la red es de tierra y se vuelve intransitable en la estación de lluvias (Wikivoyage). Canadá advierte de controles, barreras improvisadas y MINAS ANTIPERSONA.",
        "PERMISO DE MOVIMIENTO INTERNO: confirmado. Los visitantes extranjeros que salen de Yuba necesitan un «alien travel permit» explícito y, según el destino, autorizaciones militares adicionales; en los parques nacionales la visita exige escolta armada de guardas (Travel and Tour World, 4 de septiembre de 2026). El organismo emisor concreto, el coste y el plazo NO están publicados en ninguna fuente oficial abierta: POR CONFIRMAR.",
        "Escolta: confirmada como obligatoria para entrar en parques nacionales (escolta armada de guardas). Fuera de los parques se cita para operadores y ONG, sin norma publicada: POR CONFIRMAR.",
        "Divisas y vehículo: máximo 5.000 SSP a la entrada y a la salida, y no se aceptan dólares deteriorados ni emitidos antes de 2006 (Departamento de Estado de EE. UU.). Las tasas de aduana y de seguro se pagarán en efectivo.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autoridad competente: South Sudan Civil Aviation Authority (SSCAA), www.ssdcaa.com. No ha codificado normativa específica de drones.",
        "Drone-laws.com (actualización de 21 de enero de 2026): los vuelos de visitantes extranjeros NO están permitidos; los vuelos gubernamentales sí, con registro.",
        "El MAEC no menciona drones de forma explícita, pero prohíbe fotografiar sin permiso especial del Ministerio de Información, con riesgo de detención. El Departamento de Estado de EE. UU. cifra ese permiso en 50 USD, expedido por el Ministerio del Interior.",
        "Canadá (1 de septiembre de 2026) exige permiso del Ministerio de Información para fotografiar y prohíbe imágenes de instalaciones militares, edificios gubernamentales, infraestructuras y servicios públicos.",
        "Recomendación operativa de la ficha: no introducir dron en el país en ningún caso; ni siquiera declarado. No se ha localizado ningún testimonio de overlander que haya obtenido permiso.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "DISPONIBLE. Licencia provisional de la National Communication Authority a finales de junio de 2024; lanzamiento comercial en julio de 2024, con tarifas aprobadas por el regulador (Developing Telecoms, 16 de julio de 2024).",
        "El pago se hace en libras sursudanesas por el equivalente a los precios en dólares fijados por Starlink, según la propia NCA. Importe mensual exacto para 2026: POR CONFIRMAR en starlink.com.",
        "MTN South Sudan anuncia Starlink por satélite a escala nacional a través de sus canales, lo que facilita conseguir kit y soporte en Yuba.",
        "Operadores móviles: MTN y Zain. Wikivoyage recomienda comprar SIM local con el teléfono liberado. El registro de SIM exige documentación: llevar pasaporte y visado.",
        "La penetración de internet era del 12,1 % en enero de 2024, de las más bajas del mundo: fuera de Yuba no hay que contar con datos móviles útiles.",
    ],
    perro_intro=[
        "NO se ha localizado ninguna página oficial nacional del servicio veterinario de Sudán del Sur que publique los requisitos de entrada de animales de compañía. Lo que sigue procede de PetTravel.com, una fuente comercial, no gubernamental: tratar como orientativo y confirmar por vía consular antes de cualquier movimiento.",
        "Requisitos recogidos por PetTravel: vacuna antirrábica administrada entre 30 días y 12 meses antes de la entrada (no se aceptan vacunas plurianuales salvo que se hayan puesto dentro de los 12 meses previos); certificado veterinario cumplimentado por veterinario colegiado dentro de los 10 días anteriores a la entrada y emitido o refrendado por un veterinario oficial del país de origen.",
        "Microchip ISO 11784 de 15 dígitos: recomendado, no obligatorio según esa misma fuente. Para la expedición es obligatorio de facto, porque el regreso a la UE lo exige.",
        "Permiso de importación previo: PetTravel afirma que NO se exige para mascotas que entran acompañadas de su dueño. Razas prohibidas: Sudán del Sur no publica lista. Cuarentena: se exime si se cumple todo; si no, cuarentena, devolución o eutanasia a costa del propietario.",
        "TODAS las mascotas deben entrar por el Aeropuerto Internacional de Yuba según PetTravel. No hay ninguna fuente que describa la entrada de un perro por el paso terrestre de Nimule: para la expedición, que viaja por carretera, esto es un bloqueo en sí mismo.",
        "Vuelta a la UE: el régimen de importación no comercial se rige por el Reglamento Delegado (UE) 2026/131 y la lista de terceros países del Reglamento de Ejecución (UE) 2026/636. Esa lista NO incluye países africanos continentales, y Sudán del Sur no es una excepción insular, así que el retorno sería por la VÍA A: titulación de anticuerpos antirrábicos en laboratorio autorizado por la UE, con muestra tomada al menos 30 días después de la vacunación y al menos 3 meses antes de la entrada en la UE, anotada en el pasaporte europeo ANTES de salir de España. Verificar el número exacto de los reglamentos en EUR-Lex antes de usarlos: no se han podido abrir en esta sesión.",
        "Veterinarios: no se ha localizado ninguna clínica veterinaria de referencia en Yuba en fuente abierta. Riesgos para el perro: rabia endémica, garrapatas, tripanosomiasis africana (mosca tse-tsé), leishmaniasis y calor extremo. POR CONFIRMAR.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "FIEBRE AMARILLA OBLIGATORIA: certificado internacional de vacunación exigido para entrar, desde los 9 meses de edad y con validez de por vida (TravelHealthPro, agosto de 2026; FCDO, 25 de agosto de 2026; MAEC).",
        "MALARIA de riesgo alto en todo el país y todo el año. TravelHealthPro recomienda quimioprofilaxis con atovacuona/proguanil, doxiciclina o mefloquina, además de la pauta ABCD de prevención de picaduras.",
        "Vacunas recomendadas: hepatitis A, tétanos, fiebre tifoidea y pauta de rutina (triple vírica, difteria-tétanos-polio) para todos; hepatitis B, meningocócica ACWY, refuerzo de polio, rabia y BCG en perfiles concretos. El MAEC añade cólera y meningitis A+C+W135.",
        "Brotes activos recogidos por TravelHealthPro en agosto de 2026: mpox clado I, cólera y poliovirus variante. El FCDO añade cribado sanitario por Ébola en los pasos terrestres desde RDC y Uganda, y Canadá impone cuarentena de 21 días al regreso.",
        "Otros riesgos: dengue, esquistosomiasis, leishmaniasis, enfermedad del sueño (tripanosomiasis africana), fiebre botonosa africana y fiebre del valle del Rift. Agua y alimentos: precauciones estrictas, nada de agua no tratada ni hielo.",
        "Sanidad «muy deficiente» (MAEC), con servicios básicos solo en Yuba y pago EN EFECTIVO por adelantado antes de atender. Centros de referencia citados por el MAEC: MRDC International (+211 954 044 333 / +211 954 044 222) y Juba Medical Complex (+211 955 523 371).",
        "Seguro de evacuación médica internacional imprescindible; el MAEC recomienda evacuación inmediata en casos graves. Con el nivel de aviso vigente, ninguna aseguradora española estándar lo cubrirá: haría falta póliza específica de zona de alto riesgo.",
    ],
    seguridad_intro="No hay matices que hacer aquí: el MAEC desaconseja el viaje bajo cualquier circunstancia a todo el país y pide a los españoles que ya estén dentro que salgan de inmediato. Independiente desde 2011, Sudán del Sur arrastra la guerra civil de 2013-2018, un acuerdo de paz incumplido, elecciones aplazadas una y otra vez, violencia intercomunitaria endémica y una crisis humanitaria agravada por la guerra de Sudán y el corte del oleoducto. Canadá, en su revisión de 1 de septiembre de 2026, mantiene «avoid all travel» y pide evitar todo desplazamiento por carretera.",
    seguridad=[
        "MAEC (28-03-2025): riesgo alto en TODO el país. Especialmente peligrosos los estados de Unity, Alto Nilo y Jonglei; milicias activas en Ecuatoria Central y Occidental y en Bahr el Ghazal Occidental.",
        "Yuba: asaltos a mano armada de día y de noche. El MAEC recomienda expresamente NO OPONER RESISTENCIA en caso de agresión y desplazarse en vehículos con un mínimo de dos ocupantes.",
        "Toque de queda no oficial entre las 19:00 y las 06:00 en Yuba, con muy pocas calles iluminadas.",
        "Canadá: delincuencia violenta generalizada en todo el país, incluidos SECUESTROS, robos a mano armada y robos de vehículo con violencia.",
        "Carreteras: ataques y emboscadas diarios según el MAEC; desaconsejado circular de noche. A los transportistas kenianos se les ha advertido de no usar la carretera Nimule–Yuba después de las 16:00 (Pachodo, prensa regional).",
        "Controles y barreras improvisadas frecuentes, y presencia de MINAS ANTIPERSONA fuera de las vías principales (Canadá).",
        "Frontera con Sudán: zona de conflicto armado activo desde abril de 2023. Renk y Joda son además puntos de entrada masiva de refugiados y retornados.",
        "Marco legal: prohibidas las relaciones homosexuales y las extramatrimoniales, con penas severas; tráfico de drogas castigado con dureza (MAEC).",
        "Registro obligatorio en el Registro de Viajeros del MAEC (registroviajeros.exteriores.gob.es) antes de cualquier desplazamiento, aunque la ficha sea informativa.",
    ],
    agua=[
        "El agua corriente NO es potable en ninguna parte del país. TravelHealthPro (agosto de 2026) exige precauciones estrictas con agua y alimentos, con brotes activos de cólera confirmados.",
        "Para llenar depósitos de ducha y lavado, la práctica habitual en Yuba es comprar a camiones cisterna que distribuyen agua captada del Nilo; ninguna fuente abierta en esta sesión documenta puntos concretos fiables para overlanders. POR CONFIRMAR con iOverlander sobre el terreno.",
        "La escasez de combustible se traduce directamente en escasez de agua, porque el reparto depende de los camiones cisterna y de las bombas de gasóleo: así lo describe el reportaje de D+C sobre el desabastecimiento en Sudán del Sur.",
        "Plan operativo si algún día se entrase: filtro de sedimentos más filtro de 0,1 micras o menos, y cloración o luz UV para el agua de boca; el depósito de servicios se llena con agua no tratada y se trata la de consumo aparte.",
        "Agua embotellada disponible en Yuba pero cara y de suministro irregular; fuera de la capital no hay que contar con ella.",
    ],
    combustible=[
        "Sudán del Sur es productor de petróleo pero importa casi todo el combustible refinado a través de Uganda y Kenia, lo que lo hace muy vulnerable al tipo de cambio y a cualquier interrupción (Radio Tamazuj, 19 de julio de 2026).",
        "PRECIO 2026: unos 20.000 SSP por litro en julio de 2026, según el reportaje de Radio Tamazuj sobre la crisis del combustible. Ese mismo trabajo cita a FEWS NET: los precios subieron entre un 45 % y un 105 % en tres meses hasta mayo de 2026. Eye Radio había publicado antes un pico de 2.995 SSP/litro, cifra que da la magnitud del desplome de la libra.",
        "Causa de fondo: la guerra de Sudán ha interrumpido el oleoducto que saca el crudo sursudanés por Port Sudan, hundiendo los ingresos del Estado y la moneda. El resultado son colas, racionamiento y desvío al mercado negro (D+C).",
        "Fuera del eje Yuba–Nimule la red de gasolineras es mínima e irregular. Autonomía real exigida: depósito lleno más jerricanes para cubrir al menos 800-1.000 km sin repostaje garantizado. Entrar con todo lleno desde Uganda.",
        "Calidad no garantizada: agua y sedimentos son habituales en suministros informales. Filtro de gasóleo de repuesto y prefiltro decantador obligatorios; el Delica, con su gasóleo, es el más sensible de los dos vehículos.",
        "Pago en efectivo, en libras sursudanesas o en dólares posteriores a 2006 sin marcas; no se admiten tarjetas extranjeras (MAEC) y solo pueden entrarse 5.000 SSP por persona (Departamento de Estado de EE. UU.).",
    ],
    experiencias_intro="No hay relatos recientes de overlanders europeos cruzando Sudán del Sur con vehículo propio: el conflicto ha vaciado el país de viajeros independientes desde 2013 y lo poco que circula son crónicas de transportistas, de prensa regional y de conservación. Lo que sigue son las fuentes realmente abiertas en esta sesión, con su fecha, y hay que leerlas sabiendo que ninguna describe la ruta completa que haría la expedición.",
    experiencias=[
        "La mayor migración terrestre del planeta, confirmada por censo aéreo: el 25 de junio de 2024 el presidente Salva Kiir presentó el censo aéreo hecho por African Parks con el Ministerio de Fauna y Turismo sobre 122.774 km² del paisaje Boma–Badingilo–Jonglei. Unos 6 millones de antílopes: 5,1 millones de cob de orejas blancas, 346.000 gacelas de Mongalla, 299.000 tiang y 162.000 redunca, a partir de 330.000 fotografías aéreas y 251 collares. Es el mayor argumento para volver algún día.",
        "Patrimonio Mundial desde 2026: el 24 de julio de 2026, según African Parks, el paisaje migratorio Boma–Badingilo fue inscrito como PRIMER SITIO DE PATRIMONIO MUNDIAL DE LA UNESCO de Sudán del Sur, con unos 12 millones de hectáreas entre los parques de Boma y Badingilo y los corredores que los unen, y sin figurar en la Lista en Peligro. La ONU en el país y la delegación de la UE lo celebraron públicamente. Es el cambio más relevante de la ficha.",
        "El reverso del mismo informe: African Parks, en esa misma publicación de 2024, compara los datos con los censos de los años ochenta y constata caídas fuertes en las especies no migratorias —elefante, búfalo, hipopótamo— y señala la caza furtiva comercial como amenaza inmediata sobre un ecosistema del que dependen más de trece grupos étnicos. La migración existe, pero no está a salvo.",
        "Nimule–Elegu, el paso que sí funciona: Wikipedia y la Comunidad de África Oriental documentan que el cruce se convirtió en puesto fronterizo de parada única entre 2015 y 2018, con 6,6 millones de dólares de financiación de TradeMark East Africa, inauguración en el lado ugandés en noviembre de 2018 y apertura del OSBP del lado de Nimule en febrero de 2020. Es el único paso del país con infraestructura moderna.",
        "El bloqueo de los transportistas: Radio Tamazuj cubrió en varias piezas el bloqueo del paso de Elegu por camioneros, que llegó al sexto y al octavo día, con detención por parte de la seguridad ugandesa del líder de los conductores kenianos (Daily Monitor). Demuestra que el paso «abierto» puede quedar inutilizado durante más de una semana sin previo aviso, algo que ninguna planificación de expedición puede absorber.",
        "La carretera Yuba–Nimule tiene horario no escrito: el portal Pachodo recogió el aviso a transportistas kenianos de no circular por la Nimule–Yuba después de las 16:00. Son 197 kilómetros asfaltados, el mejor tramo del país, y aun así tiene hora de cierre de facto por emboscadas. Cualquier cálculo de etapa tiene que salir de Nimule por la mañana temprano.",
        "Cruzar desde Uganda es posible, pero con reglas propias: Wikivoyage, con dato de abril de 2024, confirma que el cruce desde Uganda se puede hacer, menciona visados en frontera por 100 dólares con duración de uno a seis meses, registro presencial obligatorio en Yuba en las 72 horas siguientes a la llegada y permiso obligatorio del Ministerio de Información para fotografiar. Contrasta con Canadá, que niega el visado a la llegada.",
        "Sobre el terreno, el combustible manda: el reportaje de D+C sobre el desabastecimiento explica cómo la escasez de carburante arrastra a la escasez de agua, porque el reparto urbano depende de camiones cisterna. Para una expedición autosuficiente esto se traduce en llevar autonomía de combustible y de agua propias, sin contar con la red local.",
        "El dato que cierra la discusión: el Gobierno de Canadá, en su revisión de 1 de septiembre de 2026, escribe literalmente «avoid all overland travel across South Sudan» y recuerda que hace falta 4x4 fuera de Yuba, que hay controles y barreras y que existen minas antipersona. Es la frase que convierte esta ficha en informativa y no en operativa.",
        "El coste de moverse: Radio Tamazuj publicó el 19 de julio de 2026 un reportaje sobre la crisis del combustible con el litro en torno a 20.000 SSP y un trayecto de 170 km que consume 40 litros, es decir 800.000 SSP, más de lo que ingresa el conductor en pasajes. Los ministerios de Petróleo y Finanzas declinaron comentar. Es la mejor radiografía de lo que cuesta rodar allí.",
    ],
    pendientes=[
        ("Sede real de la Embajada de España competente", "El MAEC dice que la Embajada en Jartum tiene residencia temporal en El Cairo (41 Ismail Mohamed, Zamalek), mientras la web de la propia Embajada sigue publicando la dirección de Jartum. Cerrar llamando o escribiendo a emb.jartum@maec.es y anotando dirección y teléfono operativos."),
        ("Organismo emisor del «alien travel permit» para salir de Yuba", "Confirmado que el permiso existe (Travel and Tour World, 4 de septiembre de 2026), pero no el organismo, el coste ni el plazo. Cerrar con el Ministerio del Interior sursudanés o con la Embajada en París, por escrito."),
        ("Coste y validez exactos del eVisa", "El tarifario consular de Washington da 100 USD para europeos, pero evisa.gov.ss no publica tarifa ni validez. Cerrar completando una solicitud en evisa.gov.ss hasta la pantalla de pago y anotando importe, validez y número de entradas."),
        ("Plazo exacto del registro tras la llegada", "EE. UU. dice 3 días en el Department of Immigration and Aliens Control, el FCDO 5 días en comisaría y Wikivoyage 72 horas en Yuba. Cerrar con la fuente oficial sursudanesa."),
        ("Régimen aduanero del vehículo extranjero", "No hay fuente que describa el laissez-passer ni la admisión temporal en Nimule. Cerrar con la South Sudan Revenue Authority o con el Automobile Association of Uganda, pidiendo el documento y la tasa."),
        ("Seguro de responsabilidad civil válido dentro del país", "La COMESA Yellow Card no cubre la circulación dentro de Sudán del Sur y EE. UU. habla de seguro contratado con el Gobierno. Cerrar identificando la aseguradora o ventanilla que lo emite en Nimule y su tarifa."),
        ("Estado de los pasos de Kaya, Nadapal, Bambouti y Aba", "Ninguno tiene fuente fechada que confirme apertura a extranjeros. Cerrar con boletines de la EAC, de OCHA o de prensa regional de 2026."),
        ("Organismo veterinario nacional y web oficial", "No localizado. Cerrar identificando la dirección de servicios veterinarios del Ministry of Livestock and Fisheries y su procedimiento de importación de animales de compañía."),
        ("Entrada del perro por frontera terrestre", "PetTravel limita la entrada de mascotas al aeropuerto de Yuba. Cerrar confirmando si Nimule admite animales de compañía; si no, el perro se queda en Uganda."),
        ("Numeración exacta de los reglamentos de la UE para el retorno del perro", "Verificar en EUR-Lex el Reglamento Delegado (UE) 2026/131 y el de Ejecución (UE) 2026/636 y comprobar que Sudán del Sur no figura en la lista de terceros países."),
        ("Condiciones de acceso a Boma y Badingilo tras la inscripción en la UNESCO", "Confirmar con African Parks qué operadores están acreditados, si la escolta de guardas es obligatoria y cerrada, y cuánto cuesta una salida de varios días desde Yuba."),
        ("Coordenadas verificadas de hospitales, embajada y puntos de agua", "Las de Yuba, Jartum y El Cairo que figuran en logistics son aproximadas de ciudad o barrio. Cerrar verificándolas en Google Maps con el gmaps_query indicado."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las fuentes citadas arriba, todas abiertas en esa fecha. Los avisos oficiales de seguridad cambian sin preaviso y los trámites de visado y aduana de Sudán del Sur no están publicados de forma estable, así que todo lo marcado como «por confirmar» debe verificarse antes de cualquier movimiento. Esta ficha es una herramienta de planificación e información, no una autorización de viaje ni una recomendación de entrar en el país.",
    emergency="Emergencia consular española: Embajada de España en Jartum, competente para Sudán del Sur, +249 912 363 377; centralita +249 183 763 639 y +249 183 269 891; emb.jartum@maec.es (el MAEC indica sede temporal en El Cairo, 41 Ismail Mohamed, Zamalek). Policía y emergencias en Sudán del Sur: 777, servicio que el propio MAEC califica de muy deficiente. Ambulancias: no hay servicio público; el único operativo citado es MRDC, +211 954 044 333. BOMBEROS: NO EXISTE servicio telefónico, según el MAEC.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

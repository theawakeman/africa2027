# -*- coding: utf-8 -*-
"""República del Congo (Congo-Brazzaville) — ficha completa, corredor doble (12 sep 2026).

BAJADA · «expedición a los gorilas»: Ntam/Souanké (desde Camerún) → Sembé → Ouesso →
Odzala-Kokoua (gorilas de llanura occidental y bais) → Etoumbi → Oyo → Brazzaville →
ferry a Kinshasa. Desvío opcional al suroeste (Dolisie, Pointe-Noire, Diosso, Conkouati).

SUBIDA · «tránsito rápido»: ferry desde Kinshasa → Brazzaville → mesetas Batéké
(Léfini/Lésio-Louna, Djambala, Lékana) → Okoyo → Boundji → Owando → Makoua → Ouesso →
Socambo (barcaza sobre el Ngoko) hacia Moloundou (Camerún). SIN parada de gorilas.
"""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ============ BAJADA: Ntam/Souanké → Sembé → Ouesso → Odzala → Brazzaville → ferry ============
    dict(n=1, name="Souanké y Sembé · eje fronterizo del noroeste", cat="Ciudad · servicios", prio="Media",
         dog="permitido con condiciones", time="1 noche",
         lat=2.0667, lon=14.0500,
         desc="Las dos primeras poblaciones congoleñas tras cruzar desde Camerún por Ntam. La carretera Sembé–Souanké–Ntam (143 km) fue inaugurada asfaltada en marzo de 2020 por el propio presidente Sassou Nguesso, dentro del corredor internacional Brazzaville–Yaundé financiado por el Banco Africano de Desarrollo: es, sobre el papel, el mejor tramo de todo el acceso. Souanké es cabecera de distrito con gendarmería, mercado y combustible irregular (a menudo en bidones); Sembé, 100 km al este, es la siguiente plaza. Aquí es donde hay que hacer el trámite de entrada completo si el puesto de Ntam no lo cubre todo: confirmar dónde se sella realmente el pasaporte y el CPD. Imagen de referencia de una ciudad congoleña, no de Souanké.",
         credit="Wikimedia Commons", source=W + "Dolisie.jpg?width=900"),
    dict(n=2, name="Ouesso · capital de la Sangha", cat="Ciudad · servicios", prio="Alta",
         dog="permitido con condiciones", time="1–2 noches",
         lat=1.6167, lon=16.0500,
         desc="La gran plaza logística de todo el norte forestal: aeropuerto, hospital de referencia, bancos, mercado, hoteles y las últimas estaciones de servicio formales antes de internarse hacia Odzala o hacia Nouabalé-Ndoki. Está sobre el río Sangha, afluente del Congo, y es el nudo donde confluyen la carretera del corredor camerunés (Ntam–Souanké–Sembé), la nacional 2 hacia Brazzaville y el paso fluvial de Socambo hacia Moloundou (Camerún), que es nuestra salida en la subida. Lo que no se consiga en Ouesso no se consigue hasta Owando (400 km al sur). Imagen de referencia del norte congoleño, no de Ouesso.",
         credit="Wikimedia Commons", source=W + "Makoua%20(Republic%20of%20the%20Congo)%20-%20Former%20bell%20tower.JPG?width=900"),
    dict(n=3, name="Parque Nacional de Nouabalé-Ndoki · bai de Mbeli (UNESCO)", cat="Patrimonio UNESCO", prio="Media",
         dog="prohibido — riesgo sanitario para los simios", time="3–5 días (expedición)",
         lat=2.2000, lon=16.1833,
         desc="4.000 km² de selva primaria sin caminos ni aldeas en el extremo norte, parte del Trinacional de la Sangha (Patrimonio Mundial de la UNESCO junto con Lobéké en Camerún y Dzanga-Sangha en RCA) y una de las selvas menos alteradas del planeta. La sede del parque está en Bomassa, a unas 3 horas en coche o 2 en barca desde Ouesso (Kabo queda a 1 hora). Sus joyas son los BAIS: Mbeli Bai, un claro pantanoso con plataforma de observación donde se estudian gorilas de llanura occidental desde 1995, y Wali Bai, más pequeño y a menos de una hora de Bomassa, con elefantes de bosque. Mondika es el sitio de gorilas habituados. Mejor época: enero–marzo (seca) y agosto para Mbeli. Visita solo con el equipo del parque (WCS), no por libre. Es un desvío grande: ~200 km de pista maderera desde Ouesso más logística fluvial. Imagen de referencia de un elefante de bosque, no del propio bai.",
         credit="Wikimedia Commons", source=W + "Gabon%20Loango%20National%20Park%20Elephant%20with%20offspring.jpeg?width=900"),
    dict(n=4, name="Parque Nacional de Odzala-Kokoua (UNESCO) · LA PARADA ESTRELLA", cat="Patrimonio UNESCO", prio="Alta",
         dog="prohibido — riesgo sanitario para los simios", time="4–7 días",
         lat=0.8000, lon=14.9000,
         desc="13.500 km² de selva ecuatorial en Cuvette-Ouest, protegida desde 1935, Reserva de la Biosfera desde 1977, gestionada por AFRICAN PARKS desde 2010 en nombre del Estado congoleño, abierta al turismo desde 2012 e inscrita en el Patrimonio Mundial de la UNESCO en 2023. Es el objetivo declarado de este tramo del viaje: una de las mejores densidades de GORILA DE LLANURA OCCIDENTAL del mundo (se citan hasta 12 gorilas/km² en las zonas de marantáceas), unos 100 mamíferos, ~440 aves y ~4.500 especies vegetales, con elefante de bosque, chimpancé, búfalo de bosque, bongo y una de las comunidades de primates más diversas de África. Su firma son los BAIS: claros pantanosos y salinas donde la fauna sale del bosque a descubierto. Acceso por tierra: nacional 2 hasta Obouya, después Ewo y Etoumbi, y desde Etoumbi al norte por Mbomo hasta las puertas del parque, todo asfalto hasta Etoumbi y pista forestal después.",
         credit="Wikimedia Commons", source=W + "Western%20lowland%20gorilla%20(Gorilla%20gorilla%20gorilla).jpg?width=900"),
    dict(n=5, name="Ngaga · trekking de gorilas de llanura occidental", cat="Naturaleza", prio="Alta",
         dog="prohibido — riesgo sanitario para los simios", time="2–4 días",
         lat=0.4000, lon=14.1667,
         desc="El bosque de Ngaga, junto a Mbomo, en la periferia occidental de Odzala, es DONDE SE VEN LOS GORILAS: los únicos grupos de gorila de llanura occidental habituados y comercialmente visitables del parque están aquí, en la concesión del lodge Ngaga (operador Kamba African Rainforest Experiences, antes Odzala Discovery Camps). Reglas de 2026: edad mínima 15 años, máximo 4 visitantes por grupo más guía y rastreador, mascarilla obligatoria, chequeo médico previo, 1 hora máxima de observación y caminatas de 1 a 8 km que pueden durar entre 2 y 7 horas por terreno irregular. Permiso adicional declarado en 750 $/persona, «disponible únicamente en el lodge de Ngaga»: el trekking NO se compra por libre en la puerta del parque. Coordenada aproximada (Mbomo): confirmar el punto exacto con el operador. Imagen de referencia de la especie.",
         credit="Wikimedia Commons", source=W + "Lowland%20Gorilla%20(8973697544).jpg?width=900"),
    dict(n=6, name="Bais de Odzala · Lokoué, Moba y Camp Imbalanga", cat="Naturaleza", prio="Alta",
         dog="prohibido — riesgo sanitario para los simios", time="2–3 días",
         lat=0.6000, lon=14.8000,
         desc="La otra mitad de Odzala, y la que SÍ se puede reservar sin pasar por un lodge de lujo: African Parks opera Camp Imbalanga, con tarifas públicas (2025: 400 $/persona y noche en régimen internacional, entrada 35 $/persona y noche, tasa de conservación 25 $ y tasa comunitaria 20 $), y ofrece caminatas guiadas (25 $), excursión al complejo de bais de MOBA con picnic (33 $) y navegación por los ríos Mambili y Lokoué (75 $, mínimo 2 personas). El bai de LOKOUÉ es el claro clásico del parque, donde se han censado gorilas saliendo al descubierto junto a elefantes de bosque, búfalos y sitatungas. OJO: la lista de actividades de Imbalanga NO incluye el trekking de gorilas — ese solo se hace desde Ngaga. Coordenada aproximada del sector Mboko/Lékoli: confirmar con African Parks. Imagen de referencia de un elefante de bosque.",
         credit="Wikimedia Commons", source=W + "Gabon%20Loango%20National%20Park%20Elephant%20with%20offspring.jpeg?width=900"),
    dict(n=7, name="Brazzaville · Basílica de Santa Ana", cat="Cultura", prio="Alta",
         dog="permitido con condiciones", time="2–3 noches",
         lat=-4.2634, lon=15.2429,
         desc="Capital política y antigua capital de todo el África Ecuatorial Francesa, fundada por Pierre Savorgnan de Brazza en 1880 y capital simbólica de la Francia Libre durante la Segunda Guerra Mundial. Su hito es la Basílica de Santa Ana del Congo (1949, del arquitecto Roger Erell), art déco tropical de tejas verdes y bóveda parabólica de ladrillo, uno de los edificios más singulares de África central. Brazzaville es además la única base real del país para trámites: embajadas, bancos, talleres, recambios, supermercados y el gestor del ferry. Está a solo 4 km de Kinshasa: son las dos capitales nacionales más próximas del mundo.",
         credit="Henri van der Noot · CC BY-SA 4.0", source=W + "Brazzaville%20-%20Basilique%20Sainte-Anne-du-Congo.jpg?width=900"),
    dict(n=8, name="Corniche de Brazzaville y rápidos del Congo", cat="Naturaleza", prio="Alta",
         dog="permitido con correa", time="½ día",
         lat=-4.2900, lon=15.2600,
         desc="El paseo de la Corniche recorre la orilla del río Congo con Kinshasa enfrente y el Pool Malebo abierto aguas arriba; aguas abajo del centro empiezan los RÁPIDOS DEL CONGO (los rápidos de Livingstone), donde el segundo río del mundo por caudal se estrella contra la barrera rocosa y deja de ser navegable durante 350 km, el motivo geográfico que explica el ferrocarril Congo-Océan y toda la historia colonial de la zona. Se ven bien desde los miradores de Bacongo y desde la desembocadura del Djoué. ADVERTENCIA SERIA: el río es frontera internacional y está vigilado; fotografiar hacia la orilla, hacia el puerto o hacia el Beach provoca requisa de cámara o detención. Nada de drones, y preguntar antes de sacar la cámara.",
         credit="Wikimedia Commons", source=W + "A%20view%20of%20Congo%20River%20from%20Kinshasa%2C%20Democratic%20Republic%20of%20the%20Congo%20(DRC).jpg?width=900"),
    dict(n=9, name="Cataratas de Loufoulakari", cat="Naturaleza", prio="Alta",
         dog="permitido con correa", time="1 día",
         lat=-4.4500, lon=14.9200,
         desc="A unos 75 km al suroeste de Brazzaville, en el departamento del Pool, el río Loufoulakari se despeña unos 30 m sobre grandes losas de arenisca justo antes de entregarse al río Congo: el paseo de un día clásico de la capital y, con diferencia, la mejor excursión a pie corta del corredor de bajada. Acceso desde Nganga Lingolo por la RN2 en dirección a Linzolo, pasando Mbanza Ndounga (km 53) y Kimpandzou (km 63); el último tramo es pista, mejor con 4x4 y evitable en plena temporada de lluvias. Sin infraestructura turística consolidada: no hay taquilla fija y suele haber jóvenes del pueblo que ofrecen guía por propina. Se puede bajar a las losas y hay sombra para comer. Coordenada aproximada: confirmar sobre el terreno. Imagen de referencia del río Congo.",
         credit="Wikimedia Commons", source=W + "Congo%20River%20from%20Kinshasa%20in%20Democratic%20Republic%20of%20the%20Congo%20(DRC).jpg?width=900"),
    dict(n=10, name="Mercados de Brazzaville · Poto-Poto y Total", cat="Cultura", prio="Media",
         dog="no recomendado (multitud)", time="½ día",
         lat=-4.2700, lon=15.2750,
         desc="Poto-Poto es el barrio popular histórico de la capital y la cuna de la Escuela de Pintura de Poto-Poto, fundada en 1951 por Pierre Lods, el movimiento artístico más conocido del África central francófona: el taller-galería sigue abierto y se pueden ver pintores trabajando. A pocos minutos, el Marché Total de Bacongo y el Marché Plateau son el mejor sitio del viaje para abastecerse de fruta, pescado ahumado y telas, y para cambiar dinero antes del ferry. Ir sin cámara a la vista, con lo justo en los bolsillos y sin el perro: son mercados densísimos. Imagen de referencia de Brazzaville.",
         credit="Wikimedia Commons", source=W + "Basilique%20Sainte-anne.jpg?width=900"),
    # ---- Desvío opcional suroeste (RN1): Dolisie, Pointe-Noire, Diosso, Conkouati, CFCO ----
    dict(n=11, name="Dolisie", cat="Ciudad · servicios", prio="Media",
         dog="permitido con condiciones", time="1 noche",
         lat=-4.2000, lon=12.6667,
         desc="Tercera ciudad del país y nudo de la RN1 entre Brazzaville y Pointe-Noire, además de cabecera de la carretera hacia Gabón (Ndendé/Doussala) y estación del ferrocarril Congo-Océan. Talleres, combustible formal y hospital: la parada natural a mitad del desvío suroeste, si se decide hacerlo.",
         credit="Jomako · CC BY-SA 3.0", source=W + "Dolisie.jpg?width=900"),
    dict(n=12, name="Pointe-Noire y la costa atlántica", cat="Ciudad · servicios", prio="Media",
         dog="permitido con condiciones", time="2 noches",
         lat=-4.7975, lon=11.8481,
         desc="Capital económica, mayor puerto del país y la mejor oferta de talleres, recambios, supermercados y sanidad privada de todo el Congo — mejor incluso que Brazzaville en repuestos de automoción, por el sector petrolero. Playas urbanas (Côte Sauvage, Pointe Indienne) y ambiente muy distinto al del interior. Está a ~510 km de Brazzaville por la RN1 asfaltada: el desvío completo son unos 1.000 km ida y vuelta, es decir 4-5 días. Solo tiene sentido si hay que reparar algo serio, si se quiere ver la costa y Conkouati, o si se valora la alternativa de Cabinda.",
         credit="David Stanley · CC BY 2.0", source=W + "Pointe-Noire%20downtown.jpg?width=900"),
    dict(n=13, name="Garganta de Diosso y museo Ma Loango", cat="Cultura", prio="Media",
         dog="permitido con correa", time="½ día",
         lat=-4.6167, lon=11.8833,
         desc="A unos 25 km al norte de Pointe-Noire, el «gran cañón congoleño»: un anfiteatro de acantilados de arenisca roja y ocre erosionados sobre la vegetación tropical, con miradores al borde y senderos cortos. En el mismo pueblo de Diosso está el Museo Ma Loango, instalado en el antiguo palacio del rey del Loango, con la memoria del reino Vili y de la trata atlántica; Diosso fue capital del reino de Loango. Correa corta en los miradores: el borde no está protegido. Imagen de referencia de la costa-laguna de la región, no de la garganta.",
         credit="Wikimedia Commons", source=W + "Mayumba%20remorqueur%20lagune.jpg?width=900"),
    dict(n=14, name="Parque Nacional de Conkouati-Douli", cat="Costa", prio="Media",
         dog="prohibido — fauna y chimpancés", time="2–3 días",
         lat=-3.9167, lon=11.4167,
         desc="El parque más biodiverso del país y el único que junta océano, laguna, sabana y selva: playas de anidación de cinco especies de tortuga marina (laúd y olivácea entre ellas), manatíes africanos, delfines y ballenas jorobadas frente a la costa, y en el interior elefantes de bosque, búfalos, leopardos, chimpancés y gorilas. Gestionado con Noé y con el proyecto HELP Congo de rehabilitación de chimpancés en las islas de la laguna Conkouati. Está a ~150 km al norte de Pointe-Noire por la RN5 hacia la frontera gabonesa; los accesos interiores son pista. Candidato a Patrimonio Mundial (lista indicativa de la UNESCO). Tarifas y alojamiento, a confirmar con la oficina de enlace de Pointe-Noire (info.pncd@noe.org). Imagen de referencia: elefantes de bosque en la playa del Parque Nacional de Loango (Gabón), el parque hermano justo al norte, del mismo ecosistema costero.",
         credit="Wikimedia Commons", source=W + "Gabon%20Loango%20National%20Park%20Elephant%20with%20offspring.jpeg?width=900"),
    dict(n=15, name="Ferrocarril Congo-Océan (CFCO)", cat="Cultura", prio="Media",
         dog="no aplicable (no embarcamos el perro)", time="½ día",
         lat=-4.2714, lon=15.2833,
         desc="Los 510 km de vía entre Pointe-Noire y Brazzaville, construidos entre 1921 y 1934 para salvar los rápidos del Congo, son una de las obras más mortíferas de la historia colonial: se calcula que murieron más de 17.000 trabajadores africanos reclutados a la fuerza, y el escándalo lo denunciaron en su día André Gide y Albert Londres. Hoy sigue operando el tren «La Gazelle» entre las dos ciudades, con tramos espectaculares por el macizo del Mayombe, viaductos y túneles. Interés histórico de primer orden y una alternativa a considerar para hacer el desvío a Pointe-Noire SIN mover los vehículos (dejándolos en Brazzaville) si el calendario aprieta. Confirmar frecuencia y estado del servicio: ha sufrido interrupciones largas. Imagen de referencia de Pointe-Noire, terminal atlántica de la línea.",
         credit="David Stanley · CC BY 2.0", source=W + "Pointe-Noire%20downtown.jpg?width=900"),
    # ============ SUBIDA: ferry → Brazzaville → mesetas Batéké → Owando → Ouesso → Socambo ============
    dict(n=16, name="Reserva de Lésio-Louna · gorilas reintroducidos", cat="Naturaleza", prio="Alta",
         dog="prohibido — riesgo sanitario para los simios", time="1–2 días",
         lat=-3.2333, lon=15.4667,
         desc="A unas 3-4 horas al norte de Brazzaville por la RN2, en el borde de las mesetas Batéké y dentro del complejo de la reserva de la Léfini, la Fundación Aspinall gestiona desde los años noventa un santuario donde se rehabilitan y liberan GORILAS DE LLANURA OCCIDENTAL huérfanos del tráfico. Paisaje insólito para el Congo: sabana ondulada, arena blanca y galerías de bosque a lo largo de los ríos Lésio y Louna. Es la opción de gorilas de la SUBIDA —mucho más corta y barata que Odzala— pero hay que entenderla por lo que es: animales reintroducidos en un programa de conservación, no un trekking en selva virgen. Acceso en 4x4 desde la RN2; confirmar tasas y si admiten visita sin reserva previa. Coordenada aproximada. Imagen de referencia de la especie.",
         credit="Wikimedia Commons", source=W + "Western%20lowland%20gorilla%20(Gorilla%20gorilla%20gorilla).jpg?width=900"),
    dict(n=17, name="Mesetas Batéké · Djambala y Lékana", cat="Naturaleza", prio="Media",
         dog="permitido", time="1–2 días",
         lat=-2.5333, lon=14.7500,
         desc="El Congo que nadie espera: en vez de selva cerrada, 500 km de altiplano de arena blanca a 700-800 m, sabana herbácea, cañones de erosión y bosques-galería encajados, con un clima notablemente más fresco. Djambala es la capital departamental de Plateaux y Lékana el paso hacia Okoyo; la carretera Brazzaville–Ngo–Djambala–Lékana–Okoyo es la alternativa real a la RN2 para subir hacia el norte, y por eso es nuestro corredor de subida. Del otro lado de la frontera, en Gabón, el paisaje continúa en el Parque Nacional de los Plateaux Batéké; en el lado congoleño el nuevo Parque Nacional de Ogooué-Leketi (creado en 2018, ~3.500 km²) protege el mismo ecosistema y una población de gorilas y elefantes de bosque, aunque todavía sin turismo organizado: confirmar si en 2027 tiene acceso abierto. Imagen de referencia del río Congo, que bordea las mesetas.",
         credit="Wikimedia Commons", source=W + "Congo%20River%20from%20Kinshasa%20in%20Democratic%20Republic%20of%20the%20Congo%20(DRC).jpg?width=900"),
    dict(n=18, name="Owando y Makoua · la línea del Ecuador", cat="Cultura", prio="Media",
         dog="permitido con condiciones", time="1 noche",
         lat=0.0036, lon=15.6333,
         desc="Owando (antigua Fort-Rousset), capital de la Cuvette, es la única plaza con servicios reales entre Brazzaville y Ouesso: combustible, hospital, mercado y hoteles sencillos. Ochenta kilómetros al norte, Makoua está justo sobre la LÍNEA DEL ECUADOR, con un monumento junto a la carretera donde se cruza el paralelo cero: la foto obligada del tramo y el punto en el que el viaje pasa oficialmente al hemisferio norte en la subida. Makoua conserva además el campanario de la antigua misión. Es también el desvío hacia Obouya, Ewo y Etoumbi, es decir, la puerta de Odzala desde el sur.",
         credit="Wikimedia Commons", source=W + "Makoua%20(Republic%20of%20the%20Congo)%20-%20Former%20bell%20tower.JPG?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "naturaleza": "verde", "cultura": "morado",
              "costa": "turquesa", "patrimonio unesco": "marron"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada bajada — Ntam / Souanké (desde Camerún)", "Frontera", 2.2000, 14.0000,
     "Extremo congoleño del corredor Ketta-Djoum / Brazzaville-Yaundé. El lado CONGOLEÑO está confirmado: los 143 km Sembé-Souanké-Ntam se inauguraron asfaltados el 6 de marzo de 2020 y el conjunto de 312 km del lado congoleño está terminado; el que iba con retraso es el tramo camerunés (191 km). POR CONFIRMAR, y es crítico: coordenada exacta del puesto, si el cruce del río Ngoko/Dja es por puente terminado o por barcaza, horario de apertura, si la aduana congoleña sella el CPD aquí o hay que bajar a Ouesso, y si el paso admite vehículos particulares extranjeros o solo tráfico comercial. Coordenada aproximada."),
    ("Frontera · Salida bajada — Beach de Brazzaville, ferry hacia Kinshasa", "Frontera", -4.2790, 15.2860,
     "El cruce más notorio de África para overlanders. NO hay puente sobre el río Congo. Pasajeros en canot rapide (15-20 min, ~16.400 FCFA por persona según relatos de 2024-2025); vehículos en el bac/barcaza, con salidas limitadas y no diarias. Intervienen puerto, inmigración (DGM del lado RDC), aduanas de ambos países, higiene (fiebre amarilla) y policía. Presupuestar UN DÍA ENTERO por persona y 1-3 días adicionales para el despacho del vehículo en Kinshasa. Empezar a primera hora; hay quien recomienda cruzar en domingo, con menos aglomeración. Coordinar con la ficha de RD Congo, que documenta el trámite desde la otra orilla."),
    ("Frontera · Entrada subida — Beach de Brazzaville, ferry desde Kinshasa", "Frontera", -4.2790, 15.2860,
     "Mismo cruce en sentido inverso, ya de vuelta desde Angola/RD Congo. Segundo día entero de trámites. Aquí arranca el corredor de subida: Brazzaville → Ngo → Djambala → Lékana → Okoyo → Boundji → Owando → Makoua → Ouesso."),
    ("Frontera · Salida subida — Socambo / Moloundou (hacia Camerún)", "Frontera", 1.5833, 16.0833,
     "Paso fluvial sobre el río Ngoko frente a Ouesso: barcaza o piragua motorizada, sin puente. Elegido para que la subida no repita el corredor Ketta-Djoum. CRÍTICO POR CONFIRMAR: capacidad real de la barcaza para vehículos de 3 t, frecuencia, horario, y si la aduana camerunesa de Moloundou sella CPD de vehículo extranjero. Plan B: salir de nuevo por Ntam/Souanké. Coordenada aproximada."),
    ("Frontera · Alternativa — Ndendé / Doussala (hacia Gabón, desde Dolisie)", "Frontera", -2.8333, 10.9167,
     "Solo relevante si se hace el desvío suroeste y se decide salir hacia Gabón en vez de volver a Brazzaville. Gabón queda fuera de la ruta fija del proyecto (eVisa solo aéreo): tratar como informativo."),
    ("Embajada de España en Kinshasa (acreditada también en Congo-Brazzaville)", "Consular", -4.3050, 15.3050,
     "Bd. Colonel Tshatshi nº 37, Kinshasa (Gombe), RD Congo. Tel. +243 813 300 061 / 817 008 770 · Emergencia consular: +243 819 500 289. NO hay embajada española en Congo-Brazzaville: la representación competente está justo al otro lado del río, lo que en la práctica significa que para cualquier gestión consular hay que cruzar el ferry."),
    ("Hôpital Général de Brazzaville (CHU)", "Hospital", -4.2694, 15.2761,
     "Principal referencia hospitalaria del país junto con el Hôpital Central des Armées Pierre Mobengo. Coordenada urbana aproximada."),
    ("Hospitales de Pointe-Noire", "Hospital", -4.7975, 11.8481,
     "Hôpital Général Adolphe Sicé y clínicas privadas ligadas al sector petrolero: la mejor sanidad privada del país, relevante solo si se hace el desvío suroeste."),
    ("Hôpital de base de Ouesso", "Hospital", 1.6167, 16.0500,
     "Única referencia sanitaria seria de todo el norte forestal, entre Odzala, Nouabalé-Ndoki y las dos fronteras cameruneses. A más de 800 km de Brazzaville."),
    ("Combustible · Ouesso", "Combustible", 1.6167, 16.0500,
     "Últimas estaciones formales del norte. Salir de aquí con depósitos y garrafas al 100 % antes de Odzala o de Nouabalé-Ndoki: dentro del bloque forestal el combustible es en bidones, caro y no garantizado."),
    ("Combustible · Etoumbi y Ewo (puerta de Odzala)", "Combustible", 0.0167, 14.9500,
     "Último punto con oferta —irregular— antes de Mbomo y del parque. Etoumbi es además el pueblo-puerta del sector occidental de Odzala. Confirmar existencias; no planificar contando con ellas."),
    ("Combustible · Owando", "Combustible", -0.4833, 15.9000,
     "Plaza intermedia obligada de la RN2 entre Brazzaville y Ouesso (~400 km a cada lado). Repostar aunque el depósito no esté bajo."),
    ("Combustible · Brazzaville", "Combustible", -4.2634, 15.2429,
     "Mejor oferta y calidad del país (Total, X-Oil, Puma). Repostar a fondo antes del ferry: al otro lado, en Kinshasa, la calidad es más variable y el despacho puede retenernos días."),
    ("Combustible · Djambala y Okoyo (corredor de subida)", "Combustible", -2.5333, 14.7500,
     "Oferta escasa en el eje de las mesetas Batéké. Salir de Brazzaville con autonomía suficiente para llegar holgadamente a Owando."),
    ("Combustible · Dolisie y Pointe-Noire (desvío suroeste)", "Combustible", -4.7975, 11.8481,
     "Estaciones formales y la mejor calidad de gasóleo del país en Pointe-Noire, por el sector petrolero."),
    ("Agua potable y de uso general · Brazzaville", "Agua potable", -4.2634, 15.2429,
     "Agua embotellada sin problema en supermercados de la capital; hoteles y estaciones de servicio permiten llenar el depósito de uso general con manguera. Es el mejor punto de recarga completa antes de la travesía norte."),
    ("Agua potable y de uso general · Ouesso y Owando", "Agua potable", 1.6167, 16.0500,
     "Recarga posible en hoteles y misiones. A partir de aquí, hacia Odzala o hacia Nouabalé-Ndoki, el agua es de río o de pozo: filtrar y potabilizar sin excepción."),
]

DRONE_CALLOUT = ("warn", "Tratar como prohibido de facto: autorización previa obligatoria y riesgo real de detención",
                 "Congo-Brazzaville exige autorización previa de la Agence Nationale de l'Aviation Civile (ANAC-Congo) para cualquier vuelo de dron, y no existe un procedimiento turístico simple. El problema no es solo administrativo: en toda África central (Camerún, RCA, RD Congo, el propio Congo) hay casos documentados de extranjeros detenidos por volar o incluso por transportar un dron, acusados de espionaje. Y nuestro trazado está lleno de objetivos sensibles: el río Congo como frontera con RD Congo, el Beach y el puerto de Brazzaville, las instalaciones petroleras de Pointe-Noire y Djeno, la presidencia y los cuarteles, y los propios parques nacionales (donde African Parks y WCS operan antifurtivismo aéreo y un dron ajeno se interpreta como reconocimiento de cazadores). Norma del proyecto: el dron no se saca de su caja en Congo-Brazzaville. Declararlo en aduana al entrar, llevarlo embalado y a la vista, y no discutirlo.")

STARLINK_CALLOUT = ("warn", "Sin servicio confirmado a mediados de 2026: tratar como no disponible",
                    "Congo-Brazzaville figura en el mapa de cobertura de Starlink como mercado previsto, pero no hay confirmación de servicio comercial activo a mediados de 2026 (a diferencia de RD Congo, donde sí opera desde 2025). Además, un terminal satelital sin licencia local es otro aparato susceptible de ser interpretado como equipo de espionaje en los controles. Tratarlo como no disponible y planificar el corredor norte (Ouesso-Odzala-Etoumbi) dando por hecho 2-4 días sin cobertura de ningún tipo. Conectividad principal: SIM local de MTN Congo o Airtel Congo, con cobertura razonable en Brazzaville, Pointe-Noire, Ouesso y las capitales de departamento, y prácticamente nula dentro del bloque forestal.")

DOG_MATRIX = [
    ("Odzala-Kokoua · trekking de gorilas y bais", "prohibido",
     "NO es una prohibición administrativa cualquiera: es sanitaria y seria. Los gorilas y chimpancés comparten con nosotros una parte enorme del genoma y son extremadamente vulnerables a patógenos de otros mamíferos; los protocolos de Odzala ya obligan a los VISITANTES HUMANOS a llevar mascarilla, pasar un chequeo médico previo y mantener distancia, precisamente para no transmitirles infecciones respiratorias. Un perro doméstico añade encima el riesgo del moquillo canino (distemper), que ha causado mortandades documentadas en grandes carnívoros y primates africanos, más rabia y parásitos. PLAN B OBLIGATORIO: dejar al perro en Brazzaville o en Ouesso, en una pensión con patio cerrado o con cuidador contratado, durante los días de parque; o turnarse — dos personas entran al trekking y una se queda con el perro en el alojamiento de Mbomo/Etoumbi, y al día siguiente se cambian (el permiso es por persona y por día, así que el turno es compatible con el sistema de reservas)."),
    ("Nouabalé-Ndoki, Conkouati-Douli, Lésio-Louna, Ogooué-Leketi", "prohibido",
     "Mismo argumento sanitario (gorilas, chimpancés) más fauna sensible y grandes carnívoros. Lésio-Louna es un centro de rehabilitación de gorilas huérfanos: el control sanitario allí es, si cabe, más estricto. Ningún plan B dentro del recinto; el plan B es el mismo turno de cuidado o la pensión en la ciudad más cercana."),
    ("Brazzaville, Pointe-Noire, Dolisie, Ouesso, Owando", "permitido con condiciones",
     "Sin restricción específica conocida en ciudad. Correa siempre, calor y humedad ecuatoriales muy altos todo el año (23-33 °C con humedad alta constante): sombra, agua y evitar el mediodía. Los mercados grandes (Total, Plateau, Poto-Poto) son demasiado densos: dejar al perro en el vehículo a la sombra o en el alojamiento."),
    ("Ferry Brazzaville-Kinshasa", "permitido con condiciones · trámite aparte",
     "El servicio de higiene interviene en el cruce y querrá ver los papeles del perro además de los nuestros: llevar certificado veterinario internacional reciente (<10 días), cartilla de rabia en vigor y titulación serológica en el MISMO dosier que los certificados de fiebre amarilla. Confirmar con antelación si el perro embarca en el canot rapide con nosotros o tiene que ir en el bac con el vehículo — es una pregunta concreta que hay que hacerle al gestor al pedir presupuesto."),
    ("Cataratas de Loufoulakari, garganta de Diosso, mesetas Batéké, corniche", "permitido con correa",
     "Sitios abiertos sin gestión de parque. Correa corta obligatoria en los bordes de Loufoulakari y Diosso (rocas mojadas, cortados sin protección) y en la corniche de Brazzaville (tráfico y zona vigilada). En las mesetas Batéké, cuidado con el sol: sabana abierta sin sombra."),
    ("Selva del norte · tramo Ouesso-Etoumbi", "permitido con precaución",
     "Fuera de los parques no hay prohibición, pero sí mosca tsé-tsé (que pica también al perro y transmite tripanosomiasis animal, a menudo mortal), garrapatas y filarias. Antiparasitario externo e interno al día, revisión diaria del pelaje y repelente apto para perros. Consultar con el veterinario antes de salir de España qué protección de tsé-tsé es viable."),
]

SOURCES = [
    # Odzala y gorilas
    ("Visit Odzala-Kokoua · web oficial del parque (African Parks)", "https://visitodzala-kokoua.org/en/"),
    ("African Parks · Odzala-Kokoua", "https://www.africanparks.org/the-parks/odzala-kokoua"),
    ("Ukuri Travel · tarifas oficiales 2025 de Camp Imbalanga (African Parks), PDF", "https://ukuri.travel/assets/camp-imbalanga-rates-2025.pdf"),
    ("Ukuri Travel · reservas de Camp Imbalanga", "https://ukuri.travel/bookings/camp-imbalanga"),
    ("Kamba African Rainforest Experiences · gorilla tracking en Ngaga (normas y protocolo)", "https://kambaafrica.com/experiences/gorilla-tracking/"),
    ("Kamba · tarifas internacionales 2025 de los itinerarios de Odzala (PDF)", "https://kambaafrica.com/wp-content/uploads/2024/03/Kamba-2025-International-RACK-Rates.pdf"),
    ("Congo Travel and Tours · programa de ecoturismo asequible a Odzala (vía Etoumbi)", "https://congotravelandtours.com/odzala-affordable-odyssey-ecotourism/"),
    ("Wikipedia · Odzala-Kokoua National Park", "https://en.wikipedia.org/wiki/Odzala-Kokoua_National_Park"),
    # Nouabalé-Ndoki y norte
    ("Nouabalé-Ndoki (WCS) · información práctica de visita", "https://ndoki.org/en-us/Visit/Park-info"),
    ("Bradt Guides · Central Africa: an overland adventure (acceso por carretera a Odzala y al Congo)", "https://www.bradtguides.com/central-africa-an-overland-adventure/"),
    ("This Boundless World · cómo viajar por Congo-Brazzaville (estado de la RN2, controles, precios)", "https://www.thisboundlessworld.com/how-to-backpack-in-congo-brazzaville-republic-of-congo"),
    ("iOverlander · Camp Imbalanga (Odzala) catalogado como campground establecido", "https://ioverlander.com/places/229177-odzala-camp-imbalanga"),
    # Frontera de Camerún
    ("Ministère des Grands Travaux du Congo · apertura al tráfico de la carretera Sembé-Souanké-Ntam", "https://grands-travaux.gouv.cg/en/media/news/sembe-souanke-ntam-road-opens-traffic"),
    ("Agence Ecofin · inauguración de los 143 km Sembé-Souanké-Ntam", "https://www.agenceecofin.com/transports/0203-74376-la-route-sembe-souanke-ntam-longue-de-143-km-qui-relie-la-republique-du-congo-au-cameroun-sera-inauguree-cette-semaine"),
    ("Investir au Cameroun · el Congo cierra los 312 km hacia Camerún, que aún debe acabar 191 km", "https://www.investiraucameroun.com/travaux-publics/0203-14123-le-congo-boucle-un-projet-routier-de-312-km-reliant-le-cameroun-qui-peine-a-achever-a-son-tour-un-troncon-de-191-km"),
    # Ferry
    ("Congo Travel and Tours · servicio de cruce del río Congo con vehículo (tarifas)", "https://congotravelandtours.com/river-crossing-vehicles/"),
    ("Very Hungry Nomads · el cruce Brazzaville-Kinshasa en 7 pasos (relato y precios)", "https://www.veryhungrynomads.com/brazzaville-to-kinshasa-river-crossing/"),
    ("Maggie in Africa · ferry crossing Brazzaville-Kinshasa", "https://www.maggieinafrica.com/travel-tips/ferry-crossing-brazzaville-to-kinshasa/"),
    # Sur y costa
    ("Parc National de Conkouati-Douli · web oficial", "https://www.conkouati.org/"),
    ("UNESCO · Parc National de Conkouati-Douli (lista indicativa)", "https://whc.unesco.org/en/tentativelists/5375/"),
    ("Wikipédia (fr) · Chutes de la Loufoulakari (acceso desde Brazzaville)", "https://fr.wikipedia.org/wiki/Chutes_de_la_Loufoulakari"),
    ("The Outsiders · visitar las chutes de la Loufoulakari", "https://www.theoutsiders.travel/inspiration/lieu/chutes-de-la-loufoulakari/"),
    ("Wikipédia (fr) · Chemin de fer Congo-Océan", "https://fr.wikipedia.org/wiki/Chemin_de_fer_Congo-Oc%C3%A9an"),
    ("Petit Futé · qué ver en Congo-Brazzaville", "https://www.petitfute.com/p114-congo-brazzaville/actualite/m17-top-10-insolites-voyage/a46696-que-faire-au-congo-les-13-incontournables-a-visiter.html"),
    # Mesetas Batéké
    ("Safari.com · Ogooué-Leketi, el nuevo parque nacional del Congo", "https://www.safari.com/blog/ogooue-leketi-national-park"),
    # Documentación general
    ("MAEC España · recomendaciones de viaje para la República del Congo (visado vía París, sanidad, seguridad)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica+del+Congo"),
    ("France Diplomatie · Congo, conseils aux voyageurs / sécurité (zonificación por colores)", "https://www.diplomatie.gouv.fr/fr/information-par-pays/congo/conseils-aux-voyageurs-securite"),
    ("Action-Visas · visado de Congo-Brazzaville: plataforma GIRAFE, tarifas y plazos (no hay eVisa real)", "https://www.action-visas.com/visa/Congo-(Brazzaville)"),
    ("GIRAFE · plataforma consular en línea de la embajada del Congo en París", "https://girafe.ambacongofr.org/"),
    ("ANAC-Congo · Agence Nationale de l'Aviation Civile, etiqueta «drones» (sin procedimiento publicado)", "https://anaccongo.cg/fr/tag/drones/"),
    ("Mappr · disponibilidad de Starlink por países (Congo-Brazzaville, «coming 2026»)", "https://www.mappr.co/starlink-availability-by-country/"),
    ("Natural World Safaris · cuándo ir a la República del Congo (estaciones norte y sur)", "https://www.naturalworldsafaris.com/africa/republic-of-congo/when-to-go"),
    ("Embajada de España en Kinshasa (competente también para Congo-Brazzaville)", "https://www.exteriores.gob.es/Embajadas/kinshasa/es/Paginas/index.aspx"),
    ("BNCR · Carte Rose CEMAC, portal oficial", "https://bncr.cm/en/"),
    ("iOverlander · puntos de combustible, agua y campamentos verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# BAJADA: Ntam/Souanké -> Sembé -> Ouesso -> Makoua -> Obouya -> Ewo -> Etoumbi -> Mbomo/Odzala
#         -> vuelta a Obouya -> Oyo -> Gamboma -> Brazzaville -> Beach (ferry)
CORRIDOR = [(2.2000, 14.0000), (2.0667, 14.0500), (1.6500, 14.5833), (1.6167, 16.0500),
            (0.0036, 15.6333), (-0.4833, 15.9000), (0.0167, 14.9500), (0.4000, 14.1667),
            (0.6000, 14.8000), (0.0167, 14.9500), (-1.1500, 15.9833), (-1.8764, 15.8639),
            (-4.2634, 15.2429), (-4.2790, 15.2860)]

# SUBIDA (tránsito rápido): Beach (ferry desde Kinshasa) -> Brazzaville -> Ngo/Lésio-Louna
#         -> Djambala -> Lékana -> Okoyo -> Boundji -> Owando -> Makoua -> Ouesso -> Socambo
CORRIDOR_ALT = [(-4.2790, 15.2860), (-4.2634, 15.2429), (-3.2333, 15.4667), (-2.5333, 14.7500),
                (-2.3167, 14.6000), (-1.4667, 15.0667), (-0.9500, 15.3667), (-0.4833, 15.9000),
                (0.0036, 15.6333), (1.6167, 16.0500), (1.5833, 16.0833)]

CORRIDOR_LABEL = "Bajada · expedición a los gorilas"
CORRIDOR_ALT_LABEL = "Subida · tránsito rápido"

EXPERIENCIAS_INTRO = ("Relatos y datos reales de otros viajeros y de operadores sobre el Congo, para contrastar con la "
                      "planificación oficial de esta ficha. El Congo-Brazzaville es de los países peor documentados de "
                      "toda la ruta: hay muchísimo material de safari de lujo y casi nada de overland independiente.")

EXPERIENCIAS = [
    "El ferry es el problema, no la carretera: quienes han cruzado Brazzaville-Kinshasa lo describen como un día entero de ventanillas. El trayecto físico en canot rapide son 15-20 minutos y el billete de pasajero rondaba los 16.400 FCFA en relatos recientes, pero el proceso completo lleva unas 4 horas solo para las personas —compra de billete, inmigración con papeleta azul, cambio de moneda, tasa de aduana de unos 1.000 FCFA, embarque, y al llegar a Kinshasa visado, pasaporte, impuesto de importación, fiebre amarilla, aduana y sellado final—. Hay quien contrata un «fixer» por unos 3.500 FCFA solo para el lado de Brazzaville. Consejo repetido: empezar a primera hora, llevar francos CFA, francos congoleños y dólares en billetes limpios y pequeños, y cambiar dinero en Brazzaville, donde el cambio es mejor. (Fuentes: Very Hungry Nomads, Maggie in Africa.)",
    "El vehículo es otra historia, y es cara: los vehículos no van en el canot rapide sino en un bac/barcaza con salidas limitadas y no diarias. El operador Congo Travel & Tours ofrece un servicio «VIP» que gestiona el cruce entero —trámites, escolta, permiso de conducción en RDC, corretaje de aduanas, tasas portuarias— DESDE 4.000 €, con unas 3 horas de cruce, recomendación de hacerlo por la mañana, cierre los domingos a mediodía y un aviso explícito de que hay que contar 1-3 días de espera en Kinshasa para el despacho del vehículo. Ellos mismos reconocen que existe la alternativa de la barcaza pública por libre y desaconsejan usarla. Los 4.000 € NO deben aceptarse como precio de mercado sin pedir más presupuestos: es la referencia alta.",
    "No hay puente, y conviene decirlo claro: entre Brazzaville y Kinshasa no existe ningún cruce fijo del río Congo. El proyecto de puente carretera-ferrocarril lleva décadas firmado entre ambos países y no está construido. Si el bac no sale ese día, no se cruza.",
    "Nada de cámaras en el río: los relatos de overlanders por África central coinciden en que fotografiar hacia el río Congo, el Beach o el puerto lleva a la requisa de la cámara. La guía de Bradt sobre travesía overland por África central lo dice sin rodeos al describir el cruce de Brazzaville. En el Congo, como en RD Congo, esto no es folclore: es el motivo más frecuente de problema serio con las autoridades.",
    "Los gorilas no se compran en la puerta: el dato más importante de toda la ficha para el objetivo del viaje. Los grupos habituados de gorila de llanura occidental de Odzala están en el bosque de Ngaga, dentro de la concesión del operador Kamba, y el permiso adicional cuesta 750 $ por persona «disponible únicamente en el lodge de Ngaga». El campamento de African Parks (Camp Imbalanga), que sí tiene tarifa pública y se reserva por internet, ofrece caminatas guiadas (25 $), la excursión a los bais de Moba con picnic (33 $) y la navegación por los ríos Mambili y Lokoué (75 $) — pero NO el trekking de gorilas. Es decir: se puede llegar a Odzala con nuestros propios vehículos y dormir barato, pero para ver gorilas hay que entrar por la puerta comercial de Ngaga.",
    "Existe una vía intermedia: operadores locales como Congo Travel & Tours venden un paquete de ecoturismo «asequible» a Odzala, por tierra desde Brazzaville vía Etoumbi, de unos 7 días, con bungalós económicos dentro del parque y con permisos y tasas de entrada incluidos, saliendo martes, jueves o sábado, y avisando de que las comidas no están incluidas (presupuestar unos 500 $ de comida). Es el punto de partida realista para negociar una fórmula mixta: nosotros llegamos con los coches, ellos ponen el permiso y el guía.",
    "El acceso por carretera a Odzala está documentado por la guía de Bradt: desde la RN2 se va al norte y al oeste por asfalto hasta Etoumbi, y desde allí al norte por Mbomo, ya en selva. Es decir, el 4x4 de verdad son los últimos ~100 km. La misma guía describe el eje Okoyo-Obouya y el sur del país como «mayoritariamente buen asfalto», con una subida de escarpe cerca de Etsouali, y no como selva cerrada: el Congo del sur es meseta y sabana, no jungla.",
    "Nouabalé-Ndoki es de otra categoría de esfuerzo: el propio parque indica que Bomassa está a 3 horas en coche o 2 en barca desde Ouesso, y que de Brazzaville a Ouesso son 12 horas de coche. Un operador de referencia sitúa la visita de 5 días en el entorno de 1.600 $ por persona con transporte y alojamiento. No es un desvío de una tarde: es una expedición aparte.",
    "La RN2 Brazzaville-Ouesso está asfaltada y en buen estado: lo confirma un viajero que la hizo en autobús en 2024-2025 y la describe como «pavimentada y actualmente en buenas condiciones», con dos compañías cubriendo el trayecto (Ocean du Nord y Seoul Express) por 25-45 $ y unas 12 HORAS de viaje. El mismo relato avisa de lo que realmente ralentiza el eje: contó OCHO controles militares en ese único trayecto, con petición de dinero en casi todos. Es el dato que hay que tener en la cabeza al calcular etapas: los kilómetros son fáciles, los controles no.",
    "Camp Imbalanga está fichado en iOverlander como «Established Campground»: es decir, otros viajeros con vehículo propio lo han usado y catalogado como sitio de pernocta, no solo como lodge. Es la confirmación más sólida que hemos encontrado de que se puede llegar a Odzala con nuestros coches y dormir dentro del parque sin pasar por un operador de lujo. Revisar la ficha y la fecha del último comentario antes de contar con ello.",
    "Precios de permisos en boca de otros viajeros: un relato de mochilero por el Congo sitúa los permisos de parque en 130-160 $ por persona y los paquetes de safari en torno a 1.000 $ diarios por habitación, y recuerda que las visitas a los parques del norte exigen reserva previa con la WCS. Encaja con las tarifas oficiales que hemos verificado (entrada 35 $ + conservación 25 $ + comunidad 20 $ = 80 $/persona y noche en Imbalanga, y 750 $ el permiso de gorilas en Ngaga): el permiso de gorilas es una categoría aparte, no «el permiso del parque».",
    "Política canina: no se ha localizado ninguna norma publicada que mencione expresamente a los perros en Odzala ni en Nouabalé-Ndoki, pero ambos parques imponen a los visitantes HUMANOS mascarilla y chequeo médico para no contagiar a los simios. En ese contexto, dar por hecho que un perro no entra es lo razonable, y además es lo correcto: el riesgo de transmisión de moquillo, rabia y parásitos a poblaciones de gorila en peligro crítico es un argumento sanitario de peso, no una molestia burocrática. Pedir confirmación por escrito a African Parks y a WCS, y tener cerrado el plan de cuidado del perro ANTES de llegar.",
]

HISTORIA_RESUMEN = ("La República del Congo, con capital en Brazzaville, fue el centro administrativo de todo el África Ecuatorial Francesa y heredó de ese pasado una identidad urbana y política distinta a la de su vecina, mucho más grande, la República Democrática del Congo; "
                    "tras la independencia en 1960 adoptó brevemente el marxismo-leninismo, y desde el fin de la Guerra Fría ha vivido guerras civiles recurrentes en torno a la figura del presidente Denis Sassou Nguesso, en el poder durante la mayor parte de las últimas cinco décadas.")

HISTORIA_SECCIONES = [
    ("El reino de Kongo, el reino de Loango y los pueblos del norte",
     "El sur del territorio formó parte de la órbita del gran reino de Kongo y, sobre todo, del reino de LOANGO, cuya capital estuvo en Diosso, cerca de la actual Pointe-Noire: una potencia comercial de la costa que exportaba marfil, cobre y tejidos de rafia antes de quedar atrapada en la trata atlántica. En el interior, los teke de las mesetas Batéké mantenían un reino propio —fue con su soberano, el Makoko, con quien Brazza firmó el tratado de 1880— y los pueblos del norte forestal (mbochi, bangala, y los pueblos cazadores-recolectores aka de la Likouala y la Sangha) vivían estructuras mucho más descentralizadas."),
    ("Brazzaville, capital del África Ecuatorial Francesa",
     "El explorador franco-italiano Pierre Savorgnan de Brazza fundó Brazzaville en 1880, y la ciudad se convirtió en capital administrativa de todo el África Ecuatorial Francesa (los actuales Congo, Gabón, República Centroafricana y Chad). Durante la Segunda Guerra Mundial fue la capital simbólica de la Francia Libre del general De Gaulle, y en 1944 acogió la Conferencia de Brazzaville, primer gesto de reforma del imperio colonial francés. De ese periodo es también el ferrocarril Congo-Océan (1921-1934), construido con trabajo forzado y con más de 17.000 muertos, denunciado en su día por André Gide y Albert Londres."),
    ("Independencia, el experimento marxista y las guerras civiles",
     "El Congo se independizó en 1960 y en 1969 adoptó oficialmente el marxismo-leninismo bajo el Partido Congoleño del Trabajo, siendo el primer país africano en declararse formalmente marxista. Tras la apertura al multipartidismo en 1992 vivió sucesivas guerras civiles (1993-94, 1997 y 1998-99) entre milicias leales a distintos líderes —Cobras, Ninjas, Zulus—, con Brazzaville y sobre todo la región del POOL como escenario principal; la insurgencia Ninja del Pool rebrotó entre 2016 y 2017 y se cerró con un acuerdo de alto el fuego en diciembre de 2017."),
    ("Situación actual: petróleo, deuda y la larga presidencia de Sassou Nguesso",
     "Denis Sassou Nguesso, que ya gobernó entre 1979 y 1992, recuperó el poder por la fuerza en 1997 y lo mantiene desde entonces mediante sucesivas reformas constitucionales: es uno de los jefes de Estado con más años acumulados en el poder de África. La economía depende casi por completo del petróleo de la costa atlántica, con una deuda pública muy elevada pese a esa riqueza, y con una de las mayores extensiones de selva primaria del planeta —incluidas las turberas de la Cuvette Centrale, el mayor sumidero de carbono tropical del mundo— apenas explorada como potencial de turismo de naturaleza."),
]

HISTORIA_FUENTES = [
    ("BBC News · Republic of Congo country profile", "https://www.bbc.com/news/world-africa-13284240"),
    ("Encyclopaedia Britannica · Republic of the Congo, History", "https://www.britannica.com/place/Republic-of-the-Congo/History"),
    ("International Crisis Group · Republic of Congo", "https://www.crisisgroup.org/africa/central-africa/republic-congo"),
    ("Wikipédia (fr) · Chemin de fer Congo-Océan", "https://fr.wikipedia.org/wiki/Chemin_de_fer_Congo-Oc%C3%A9an"),
]

SPEC = dict(
    slug="congo", name="Congo (Brazzaville)", revision="12 sep 2026",
    sub="Corredor doble · la expedición a los gorilas de Odzala · el ferry del río Congo",
    chips=[
        ("BAJADA", "Ntam/Souanké → Ouesso → ODZALA (gorilas) → Etoumbi → Brazzaville → ferry · ~1.600 km"),
        ("SUBIDA", "Ferry → Brazzaville → mesetas Batéké → Owando → Ouesso → Socambo · ~1.100 km, sin gorilas"),
        ("PDIs", "18 puntos repartidos entre los dos corredores"),
        ("LA PARADA", "Odzala-Kokoua (UNESCO 2023, African Parks): gorila de llanura occidental y bais"),
        ("PERMISO GORILAS", "750 $/persona, SOLO desde el lodge de Ngaga · mínimo 15 años · 4 personas por grupo"),
        ("EL CRUCE", "Ferry Brazzaville-Kinshasa: sin puente, un día entero de trámites, vehículo aparte"),
        ("4x4", "Etoumbi → Mbomo → Odzala · pistas del norte forestal · mesetas Batéké"),
        ("PERRO", "Prohibido en Odzala por riesgo sanitario para los simios — plan B cerrado antes de llegar"),
        ("SEGURIDAD", "estable en el corredor · el Pool, con historia de conflicto, en calma desde 2017"),
    ],
    center=[-1.0, 15.0], zoom=5,
    hero_img=W + "Western%20lowland%20gorilla%20(Gorilla%20gorilla%20gorilla).jpg?width=900",
    hero_credit="Gorila de llanura occidental, la especie de Odzala-Kokoua · Wikimedia Commons",
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y de nuevo 72 h antes del paso de Ntam y del ferry de Brazzaville.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("El Congo-Brazzaville no es un país de tránsito para este viaje: es <strong>LA parada del tramo centroafricano</strong>. "
                   "En la <strong>bajada</strong> se entra desde Camerún por Ntam/Souanké, se baja por Sembé hasta Ouesso y se gira al oeste "
                   "hacia el <strong>Parque Nacional de Odzala-Kokoua</strong> —Patrimonio Mundial de la UNESCO desde 2023, gestionado por "
                   "African Parks y uno de los mejores lugares del planeta para ver <strong>gorilas de llanura occidental</strong> y "
                   "<strong>bais</strong>—, para después bajar a Brazzaville y cruzar el río Congo en ferry hacia Kinshasa. "
                   "En la <strong>subida</strong>, meses después y de vuelta desde Angola, el país se atraviesa deprisa y por otro sitio: del "
                   "ferry al norte por las <strong>mesetas Batéké</strong> (Léfini, Djambala, Lékana, Okoyo) hasta Owando y Ouesso, y salida a "
                   "Camerún por la barcaza del Ngoko en Socambo. Los dos corredores solo comparten Brazzaville, Owando-Makoua y Ouesso."),
    decision=("Hay dos decisiones grandes que tomar antes de comprometerse con este tramo. "
              "<strong>(1) Cómo se hacen los gorilas.</strong> Los grupos habituados de Odzala están en la concesión de Ngaga, de un operador privado, "
              "y el permiso vale 750 $/persona además del alojamiento; el campamento público de African Parks (Camp Imbalanga, ~400 $/persona y noche "
              "más tasas) da bais, caminatas y río, pero no gorilas. Las opciones reales son: llegar con nuestros vehículos y comprar solo el permiso y el "
              "guía a través de un operador local; contratar un paquete de ecoturismo de los que ya existen; o renunciar al trekking y quedarse con los bais. "
              "<strong>(2) Si se hace el desvío suroeste.</strong> Pointe-Noire, la garganta de Diosso y Conkouati-Douli son ~1.000 km ida y vuelta por asfalto "
              "desde Brazzaville (4-5 días). Merecen la pena por sí mismos y Pointe-Noire es el mejor sitio del país para reparar un vehículo, pero compiten "
              "directamente con los días de Odzala. Si se descarta con los coches, el ferrocarril Congo-Océan permite hacerlo en tren dejando los vehículos en Brazzaville."),
    facts=[
        ("Ventana prevista", "Bajada: tras Camerún, antes de RD Congo. Es la parada larga del tramo centroafricano. Subida: tras RD Congo, antes de Camerún, en tránsito rápido."),
        ("Entrada bajada", "Ntam/Souanké desde Camerún, extremo del corredor Ketta-Djoum. Lado congoleño asfaltado y abierto desde 2020; lado camerunés, el punto más incierto de toda la ruta atlántica."),
        ("Salida bajada", "Ferry Brazzaville → Beach Ngobila (Kinshasa). Sin puente. Día entero de trámites y 1-3 días de despacho del vehículo al otro lado."),
        ("Entrada subida", "Ferry Kinshasa → Brazzaville. Segundo día entero de trámites."),
        ("Salida subida", "Socambo/Moloundou hacia Camerún: barcaza sobre el río Ngoko frente a Ouesso. Capacidad para vehículos POR CONFIRMAR; plan B, salir de nuevo por Ntam."),
        ("Visado", "Previo y obligatorio. NO existe eVisa real: la solicitud se prepara en la plataforma GIRAFE pero el pasaporte físico hay que enviarlo a la embajada del Congo en PARÍS (no hay embajada en España). 55 € / 15 días, 110 € / 90 días; pedir entradas múltiples."),
        ("Seguro", "Carte Rose CEMAC válida (misma zona que Camerún, Gabón, Chad, RCA y Guinea Ecuatorial). Es la ÚLTIMA frontera con Carte Rose en la bajada: RD Congo exige seguro local aparte."),
        ("Seguridad", "Estable en todo el corredor previsto. La región del Pool (entre Brazzaville y Dolisie) vivió la insurgencia Ninja de 2016-2017, cerrada con alto el fuego en diciembre de 2017 — revalidar su situación 30-60 días antes si se hace el desvío suroeste por la RN1."),
        ("Comunicaciones", "Starlink no confirmado activo. SIM local (MTN Congo, Airtel) como base; 2-4 días sin cobertura en el bloque forestal del norte."),
        ("Salud", "Fiebre amarilla obligatoria y comprobada de verdad. Paludismo intenso todo el año. Zona histórica de brotes de ébola en Cuvette-Ouest (2001-2005), justo la región de Odzala: revisar si hay brote activo antes de entrar."),
    ],
    alerts=[
        "EL PERMISO DE GORILAS NO SE COMPRA EN LA PUERTA. Los grupos habituados están en Ngaga, concesión del operador Kamba; el permiso adicional son 750 $/persona y está «disponible únicamente en el lodge de Ngaga». Camp Imbalanga, el campamento público de African Parks, ofrece bais, caminatas y río, pero no trekking de gorilas. Cerrar esto por escrito con African Parks y con un operador local MESES antes: es la razón de ser de esta parada.",
        "Frontera de Ntam/Souanké: el lado congoleño está confirmado (143 km Sembé-Souanké-Ntam asfaltados e inaugurados en 2020, 312 km congoleños completos), pero falta confirmar el cruce del río Ngoko/Dja en sí —puente o barcaza—, el horario, si sellan el CPD allí y, sobre todo, si el paso admite vehículos particulares extranjeros. Es el punto crítico de todo el corredor centroafricano y está muy poco documentado.",
        "El ferry de Brazzaville-Kinshasa es el trámite más caro y más largo de todo el viaje, y hay que hacerlo DOS veces. Vehículos y pasajeros van por separado; el precio de referencia de un servicio gestionado íntegro es de 4.000 € por vehículo (no aceptarlo como precio de mercado sin más presupuestos). Presupuestar y reservar con semanas de antelación y coordinar con la ficha de RD Congo.",
        "El perro NO entra en Odzala, y el motivo es sanitario y serio: el riesgo de transmitir moquillo canino, rabia o parásitos a una población de gorilas en peligro crítico. El propio protocolo del parque ya obliga a los humanos a llevar mascarilla y pasar chequeo médico. Hay que llegar con el plan B de cuidado del perro CERRADO, no improvisarlo en Etoumbi.",
        "Dron: tratar como prohibido de facto. Autorización previa de la ANAC-Congo, sin procedimiento turístico claro, y con casos documentados de detención por vuelo o simple posesión en la región. El dron no se saca de la caja en este país.",
        "Ébola: el Congo ha sufrido brotes reales en Cuvette-Ouest —la región de Odzala— entre 2001 y 2005, con mortandad masiva de gorilas incluida. No hay brote conocido a fecha de esta revisión, pero es una zona de vigilancia: comprobar el estado 30 días antes en el ECDC y la OMS, porque un brote activo endurecería los controles y podría cerrar el parque.",
        "Fotografía: el río Congo es frontera internacional y está vigilado. Fotografiar el Beach, el puerto, el río o cualquier instalación oficial provoca requisa de cámara o detención. Preguntar siempre antes de sacar la cámara en Brazzaville.",
        "Visado: no hay embajada del Congo en España y NO existe visado electrónico real — hay que enviar el pasaporte físico a la embajada del Congo en París, con fechas de entrada y salida concretas escritas en el visado. Con un calendario overland que se mueve, esto obliga a pedir validez larga y entradas múltiples, y a empezar el trámite con meses de antelación.",
        "Estacionalidad: en el norte (Odzala, Ouesso, Nouabalé-Ndoki) la seca corta es enero-febrero, que es cuando las pistas forestales son practicables; abril-octubre es la época húmeda del norte. En el sur (Brazzaville, Pool, costa) la seca larga es mayo-septiembre. Las dos ventanas no coinciden: si el calendario general permite elegir, la bajada con Odzala encaja mucho mejor en enero-febrero.",
    ],
    ruta_intro=("Dos corredores con propósitos opuestos. La <strong>bajada</strong> (~1.600 km) es una expedición: entrar por el noroeste "
                "forestal, plantarse en Odzala y dedicarle los días que haga falta, y después bajar a Brazzaville. La <strong>subida</strong> "
                "(~1.100 km) es tránsito puro por otro eje —las mesetas Batéké— para no repetir paisaje y salir cuanto antes hacia Camerún. "
                "Etapas calculadas sobre una media de <strong>250 km/día</strong>; el bloque forestal del norte va más lento, entre 100 y 150 km/día reales."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bajada 1 · Entrada y eje fronterizo", "Ntam → Souanké → Sembé", "~180 km · 1-2 días (el día del cruce se pierde entero)"),
        ("Bajada 2 · A la capital del norte", "Sembé → Ouesso", "~200 km · 1 día · repostaje y víveres a fondo"),
        ("Bajada 3 · Nouabalé-Ndoki (opcional, expedición)", "Ouesso → Kabo → Bomassa → Mbeli Bai", "~200 km + barca · 3-5 días si se hace"),
        ("Bajada 4 · Bajada por la RN2", "Ouesso → Makoua → Obouya", "~400 km · 2 días"),
        ("Bajada 5 · Puerta de Odzala", "Obouya → Ewo → Etoumbi → Mbomo", "~230 km · 1-2 días; asfalto hasta Etoumbi, pista después"),
        ("Bajada 6 · LOS GORILAS", "Ngaga (trekking) + bais de Lokoué y Moba + río Mambili", "en el parque · 4-7 días"),
        ("Bajada 7 · A la capital", "Etoumbi → Obouya → Oyo → Gamboma → Brazzaville", "~600 km · 3 días"),
        ("Bajada 8 · Pool y cataratas", "Brazzaville → Loufoulakari → Brazzaville", "~150 km ida y vuelta · 1 día"),
        ("Bajada 9 · Desvío suroeste (OPCIONAL)", "Brazzaville → Dolisie → Pointe-Noire → Diosso → Conkouati → vuelta", "~1.100 km · 4-6 días"),
        ("Bajada 10 · El cruce del río", "Brazzaville → Beach → ferry → Kinshasa", "4 km de río · 1 día entero de trámites (prever 2-3 con el vehículo)"),
        ("Subida 1 · El cruce del río, otra vez", "Kinshasa → ferry → Brazzaville", "4 km de río · 1 día entero"),
        ("Subida 2 · Mesetas Batéké", "Brazzaville → Ngo → Lésio-Louna → Djambala", "~400 km · 2 días"),
        ("Subida 3 · Travesía del altiplano", "Djambala → Lékana → Okoyo → Boundji → Owando", "~400 km · 2 días"),
        ("Subida 4 · Norte forestal y salida", "Owando → Makoua → Ouesso → Socambo (barcaza a Camerún)", "~450 km · 2-3 días con el cruce fluvial"),
    ],
    offroad=[
        "Etoumbi → Mbomo → Odzala-Kokoua (~100-150 km): EL tramo 4x4 del país y el acceso real a los gorilas. Asfalto hasta Etoumbi y pista forestal de laterita a partir de ahí, con puentes de madera y tramos de barro profundo en lluvias; en plena estación húmeda puede ser intransitable durante días. Sin combustible garantizado desde Ouesso u Owando: autonomía completa. Es el kilometraje que justifica llevar 4x4 en este viaje.",
        "Corredor Ketta-Djoum · Ntam → Souanké → Sembé → Ouesso (~380 km en el lado congoleño): sobre el papel, asfalto nuevo. Los 143 km Sembé-Souanké-Ntam se inauguraron asfaltados en marzo de 2020 y el conjunto de 312 km del lado congoleño está terminado. La incógnita no es el firme sino el propio paso fronterizo del río Ngoko y el estado del lado camerunés, que iba con años de retraso. Verificar 60 días antes; si el paso no admite vehículos particulares, todo el corredor de bajada cambia.",
        "Pistas del norte forestal · Ouesso → Kabo → Bomassa (Nouabalé-Ndoki): pista maderera por concesiones forestales, con tráfico de camiones de troncos y barro permanente; el propio parque cuenta 3 horas en coche para el último tramo. Alternativa fluvial en barca por el Sangha (2 horas desde Ouesso). Solo si se decide hacer Ndoki.",
        "Mesetas Batéké · Brazzaville → Ngo → Djambala → Lékana → Okoyo (corredor de subida): eje alternativo a la RN2 por altiplano de arena blanca a 700-800 m. Tramos asfaltados y tramos de arena y laterita; la arena profunda de las mesetas es un terreno distinto al barro forestal y conviene bajar presiones. Confirmar estado actual, porque hay obras y tramos rehabilitados desde 2020.",
        "Acceso a las cataratas de Loufoulakari: RN2 hasta Kimpandzou (km 63) y después pista hasta el salto; corta pero embarrada en lluvias, con vadeos menores. Perfecta para una salida de un día desde Brazzaville con los dos vehículos.",
        "Acceso a Conkouati-Douli desde la RN5 (desvío suroeste): pistas de arena costera y laterita hacia la laguna y las playas de anidación de tortugas; algunos sectores solo con marea baja. Confirmar con la oficina del parque en Pointe-Noire antes de entrar.",
    ],
    senderismo=[
        "Trekking de gorilas en Ngaga (Odzala): LA excursión a pie del viaje. Entre 1 y 8 km por bosque de marantáceas y terreno irregular, de 2 a 7 horas en total, con un máximo de 1 hora de observación. Grupos de 4 personas más guía y rastreador, edad mínima 15 años, mascarilla obligatoria y chequeo médico previo. No es un paseo: humedad del 90 %, sanguijuelas, sin sendero marcado y avance a machete detrás del rastreador. Botas altas, guantes finos y polainas.",
        "Pasarelas y bais de Odzala: la excursión al complejo de bais de MOBA (33 $ con picnic desde Camp Imbalanga) y las caminatas guiadas del parque (25 $) llevan a plataformas y claros pantanosos donde salen al descubierto elefantes de bosque, búfalos, sitatungas y a veces gorilas. Es la alternativa a pie que SÍ se puede reservar sin operador de lujo, y la que más fauna da por hora de esfuerzo.",
        "Cataratas de Loufoulakari (Pool): bajada a pie por las losas de arenisca hasta el pie del salto y paseo por la orilla hasta la confluencia con el río Congo. Roca muy resbaladiza cuando está mojada; calzado con suela agarrada y correa corta para el perro.",
        "Garganta de Diosso (desvío suroeste): senderos cortos por el borde del anfiteatro de acantilados rojos y bajada parcial al fondo. Sin protección en el borde.",
        "Mbeli Bai y Wali Bai (Nouabalé-Ndoki): caminatas cortas desde Bomassa hasta las plataformas de observación; Wali Bai queda a menos de una hora. Es la observación de fauna más pura que ofrece el país, pero exige haber llegado hasta allí.",
        "Mesetas Batéké: caminatas libres por sabana abierta y cañones de erosión en torno a Djambala y Lékana, sin infraestructura ni señalización. Terreno fácil pero sin sombra: agua y sombrero.",
    ],
    acampada=[
        "Camp Imbalanga (Odzala, African Parks): el alojamiento con tarifa pública del parque, reservable por internet a través de Ukuri. Tarifa 2025 de 400 $/persona y noche en régimen internacional, más 35 $ de entrada por persona y noche, 25 $ de tasa de conservación y 20 $ de tasa comunitaria. Caro para nuestros estándares, pero es la puerta barata de Odzala comparada con los lodges de la concesión.",
        "Mbomo y Etoumbi: pueblos-puerta del parque, con auberges muy sencillos y misiones. Es donde se quedaría quien cuide del perro durante los días de trekking.",
        "Ouesso y Owando: hoteles sencillos con patio o aparcamiento cerrado. Las dos bases logísticas del norte.",
        "Brazzaville: alojamientos con parking vigilado; la acampada libre no tiene sentido en la capital y menos con el ferry pendiente. Hay hoteles de referencia usados por overlanders cerca del centro y del Beach.",
        "Regla general del país: la acampada libre está poco documentada y el reflejo de la gendarmería rural es preguntar mucho. La fórmula que funciona en África central es la misión católica con recinto cerrado y el auberge con patio; avisar siempre al jefe del pueblo si se vivaquea.",
        "Conkouati-Douli: el parque ofrece alojamiento (Conkouati Lodge) y hay playas donde se acampa; confirmar con la oficina de enlace de Pointe-Noire antes de contar con ello.",
    ],
    visado=[
        "Visado previo OBLIGATORIO para pasaportes españoles. No hay exención y no hay visado en frontera.",
        "NO HAY EMBAJADA DEL CONGO EN ESPAÑA: el Ministerio de Asuntos Exteriores español remite expresamente a la embajada del Congo en PARÍS (37 bis, rue Paul Valéry, 75116 París · +33 1 45 00 60 57) para tramitar el visado. Es un trámite a distancia que hay que planificar con meses de margen.",
        "OJO CON EL «e-VISA»: no existe un visado electrónico congoleño real. La solicitud se prepara en la plataforma consular en línea GIRAFE (girafe.ambacongofr.org), pero el visado NO se emite en formato electrónico: hay que enviar el pasaporte físico a París para que lo sellen. Cualquier web que venda un «eVisa del Congo» está vendiendo una gestoría, no un documento electrónico oficial.",
        "Tarifas oficiales de referencia a través del consulado de París (tramitación estándar ~11 días): 55 € el visado de 15 días y 110 € el de 90 días; en urgencia (~6 días), 110 € y 220 € respectivamente. Hay opción de entradas múltiples: PEDIRLA EXPRESAMENTE, porque el país se cruza dos veces con meses de diferencia.",
        "Documentación habitual del expediente: pasaporte con 6 meses de validez y páginas libres, foto, justificante de alojamiento (reserva de hotel o carta de invitación aprobada por la DDST), itinerario y prueba de medios económicos. Al ir por tierra no tenemos billete de avión: preguntar al consulado qué acepta como justificante de entrada/salida en un viaje overland — es una pregunta concreta que hay que hacer antes de enviar el pasaporte.",
        "Las fechas importan: el visado congoleño se emite con fechas de entrada y salida concretas y hay que entrar y salir dentro de ese intervalo exacto. Con un calendario overland que puede desplazarse semanas, conviene pedir un margen amplio y una validez larga.",
        "Si el visado de entrada múltiple no cubre las dos pasadas, la segunda habrá que gestionarla en ruta: las opciones realistas son la embajada del Congo en Yaundé (Camerún) para la bajada y la de Luanda o Kinshasa para la subida. Confirmar cuál expide a extranjeros no residentes.",
        "Certificado internacional de fiebre amarilla exigido y comprobado de verdad en frontera, tanto en Ntam como en el ferry.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Ntam / Souanké (desde Camerún)",
         "Extremo del corredor Ketta-Djoum. Lado congoleño asfaltado y abierto desde 2020. POR CONFIRMAR: puente o barcaza sobre el Ngoko/Dja, horario, sellado de CPD, y si admite vehículos particulares extranjeros. Punto crítico del corredor centroafricano."),
        ("Salida bajada", "Beach de Brazzaville → Beach Ngobila, Kinshasa (RD Congo)",
         "Ferry. Sin puente. Pasajeros en canot rapide (~16.400 FCFA); vehículos en bac, salidas no diarias. Un día entero de trámites más 1-3 días de despacho del vehículo en Kinshasa. Reservar y presupuestar con semanas de antelación."),
        ("Entrada subida", "Beach Ngobila, Kinshasa → Beach de Brazzaville",
         "Mismo cruce, sentido inverso. Segundo día entero. Al llegar, Carte Rose CEMAC de nuevo válida: comprobar que sigue en vigor o renovarla en Brazzaville."),
        ("Salida subida", "Socambo / Moloundou (hacia Camerún, desde Ouesso)",
         "Barcaza o piragua motorizada sobre el río Ngoko, sin puente. POR CONFIRMAR que admite vehículos de 3 t y que la aduana camerunesa de Moloundou sella CPD. Elegido para no repetir el corredor Ketta-Djoum."),
        ("Alternativa salida subida", "Ntam / Souanké (hacia Camerún)",
         "Plan B si Socambo no admite vehículos: volver a subir a Souanké y salir por Ntam, asumiendo que se repite el eje de la bajada."),
        ("Alternativa (informativa)", "Ndendé / Doussala (hacia Gabón, desde Dolisie)",
         "Solo relevante si se hace el desvío suroeste. Gabón está fuera de la ruta fija del proyecto por su eVisa solo aéreo."),
    ],
    vehiculos=[
        "CPD con todos los pares de sellos en regla. Confirmar en qué puesto se sella realmente a la entrada por Ntam: si el puesto fronterizo no tiene aduana habilitada, el sellado se haría en Ouesso o incluso en Brazzaville, y conviene saberlo ANTES de cruzar.",
        "Carte Rose CEMAC como seguro de responsabilidad civil regional: válida en Congo igual que en Camerún. Es la ÚLTIMA frontera del tramo de bajada donde sirve — RD Congo no pertenece a la zona y exige seguro local aparte. A la vuelta, al reentrar desde RD Congo, vuelve a ser necesaria.",
        "Carnet de conducir internacional obligatorio en todos los controles; el país tiene muchos puestos de gendarmería en carretera.",
        "El despacho del vehículo en el ferry es un procedimiento aparte del de las personas: preguntar al gestor, al pedir presupuesto, qué documentos exige exactamente el lado congoleño para EMBARCAR el vehículo y cuántos días hay que contar.",
        "Autonomía de combustible: el tramo Ouesso → Odzala → Owando puede suponer 600-700 km sin suministro fiable. Garrafas llenas y embudo con filtro; la calidad del gasóleo fuera de las ciudades es irregular.",
        "Dos vehículos es lo correcto para el acceso a Odzala: en la pista de Mbomo no hay tráfico del que depender y no hay cobertura móvil.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "El dron no se saca de su caja en Congo-Brazzaville. Declararlo en aduana al entrar, llevarlo embalado y a la vista en los registros.",
        "Comprobado en septiembre de 2026: la web de la ANAC-Congo (anaccongo.cg) NO publica ningún procedimiento de autorización de drones civiles, ni un arrêté específico, ni zonas prohibidas, ni sanciones — solo material de 2018 sobre los trabajos de la OACI para regular el tráfico a baja altura. Es decir: no hay una vía formal identificable para pedir permiso como turista, lo que en la práctica equivale a que no se puede volar legalmente.",
        "Si aun así se quiere intentar, escribir a la ANAC-Congo con meses de antelación pidiendo autorización POR ESCRITO y no volar sin tenerla en papel. Asumir que lo más probable es no obtener respuesta.",
        "Zonas absolutamente vetadas en nuestro propio trazado: el río Congo y todo el frente fluvial de Brazzaville (frontera con RD Congo), el Beach y el puerto, el palacio presidencial y cualquier instalación militar, las instalaciones petroleras de Pointe-Noire y Djeno, y el interior de los parques nacionales (African Parks y WCS operan vigilancia antifurtivismo: un dron ajeno se lee como reconocimiento de cazadores).",
        "La cámara también: fotografiar edificios oficiales, puentes, puertos, militares o policías provoca problemas rutinarios. Preguntar antes.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Sin servicio comercial confirmado a mediados de 2026: revisar el mapa oficial de disponibilidad 30-60 días antes y no construir el plan de comunicaciones sobre él.",
        "Un terminal satelital sin licencia local es, igual que el dron, un aparato susceptible de malinterpretarse en un control. Si se lleva, llevarlo declarado y embalado mientras se esté en el país.",
        "SIM local (MTN Congo, Airtel Congo) como conectividad principal: cobertura razonable en Brazzaville, Pointe-Noire, Ouesso, Owando y las capitales de departamento.",
        "Dar por hecho 2-4 días incomunicados en el bloque forestal (Ouesso-Etoumbi-Mbomo-Odzala) y avisar en casa antes de entrar. Lo mismo en el eje de las mesetas Batéké en la subida.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (menos de 10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo de Ntam y en el servicio de higiene del ferry.",
        "El ferry Brazzaville-Kinshasa es el trámite con el perro más delicado del tramo: llevar toda su documentación en el mismo dosier que los certificados de fiebre amarilla humanos, y preguntar al gestor con antelación si el perro cruza en el canot rapide con nosotros o debe ir con el vehículo en el bac.",
        "Antiparasitario externo e interno rigurosamente al día: en el norte forestal hay mosca tsé-tsé, que pica también al perro y transmite tripanosomiasis animal, además de garrapatas y filarias. Consultar con el veterinario antes de salir de España qué protección es viable.",
        "Lo esencial: EN ODZALA NO ENTRA, y el motivo es sanitario. Ver la matriz por zona y el plan B más abajo.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional OBLIGATORIO y comprobado de verdad, tanto en la frontera terrestre como en el ferry. Sin él no se entra.",
        "Paludismo intenso y de transmisión estable en todo el país, durante todo el año, con predominio de Plasmodium falciparum: profilaxis a valorar con Sanidad Exterior sin excepciones, mosquitera y repelente. En el bloque forestal del norte, la presión de mosquito es máxima.",
        "Mosca tsé-tsé y tripanosomiasis africana (enfermedad del sueño): presente en focos del país, sobre todo en zonas de bosque y galería fluvial. No hay profilaxis ni vacuna; la prevención es ropa de manga larga de colores neutros (la tsé-tsé se siente atraída por el azul y el negro), repelente y evitar la vegetación densa junto a los ríos a mediodía. Afecta también al perro.",
        "Ébola: el Congo ha sufrido brotes reales de ébola en el departamento de CUVETTE-OUEST —exactamente la región de Odzala— entre 2001 y 2005, con mortandad masiva de gorilas y contagios humanos ligados a la manipulación de carne de caza. No hay brote conocido a fecha de esta revisión y el riesgo para un visitante que no toque carne de monte ni fauna muerta es bajo, pero es zona de vigilancia: comprobar el estado en el ECDC y la OMS 30 días antes. Un brote activo endurecería los controles y podría cerrar el parque. Regla simple: no se toca ni se come carne de caza (bushmeat), y punto.",
        "Agua: no beber agua de grifo en ningún punto del país. Embotellada en ciudad; filtrado y potabilización en el norte forestal, donde el agua es de río o de pozo.",
        "Referencias hospitalarias: Hôpital Général (CHU) de Brazzaville y, si se hace el desvío suroeste, el Hôpital Général Adolphe Sicé y las clínicas privadas de Pointe-Noire (las mejores del país). En el norte, el hôpital de base de Ouesso es lo único serio en 800 km. Seguro con evacuación médica IMPRESCINDIBLE: desde Odzala, una evacuación real significa avioneta.",
        "Vacunación recomendada además de la fiebre amarilla, según el propio MAEC español para este país: hepatitis A y B, fiebre tifoidea, tétanos, meningitis y RABIA — esta última especialmente relevante para nosotros, por llevar perro y por la lejanía de la atención médica en el norte forestal.",
        "El MAEC advierte además de infecciones intestinales, cólera y una prevalencia alta de VIH, y de que las instalaciones sanitarias públicas son muy limitadas: las clínicas privadas de Brazzaville y Pointe-Noire son más fiables que los hospitales públicos. Llevar botiquín completo y la medicación propia desde España.",
    ],
    seguridad_intro=("País estable en la práctica para el corredor previsto, con un régimen de mano firme y muchos controles de gendarmería en carretera. "
                     "El riesgo dominante no es la delincuencia violenta sino el aislamiento del norte forestal, la burocracia del ferry y la sensibilidad "
                     "extrema ante cámaras y aparatos voladores. El único antecedente serio de conflicto interno relevante para nuestra ruta es la región del POOL."),
    seguridad=[
        "Región del Pool (entre Brazzaville, Kinkala y la RN1 hacia Dolisie): fue el escenario de las guerras civiles de los noventa y de la insurgencia Ninja del pastor Ntumi, rebrotada entre abril de 2016 y diciembre de 2017 y cerrada con un acuerdo de alto el fuego. A fecha de esta revisión la diplomacia francesa clasifica TODO el país —y el Pool en particular— en «vigilancia reforzada» (amarillo), no en zona desaconsejada, y dice expresamente que la RN1 Brazzaville-Ignié-Mindouli-Dolisie-Pointe-Noire puede utilizarse con vigilancia reforzada. El MAEC español pide «extremar la precaución» en el Pool. Conclusión operativa: el desvío suroeste es viable, pero se revalida 30-60 días antes y no se conduce de noche.",
        "Franjas fronterizas desaconsejadas (naranja para Francia): 30 km a lo largo de la frontera con la República Centroafricana (inestabilidad y tráficos) y 10 km a lo largo de las fronteras con RD Congo y con el enclave angoleño de Cabinda. Nuestro trazado no entra en ninguna de ellas salvo, por definición, en el propio punto de cruce del ferry.",
        "Macizo del Mayombe (carretera de Dolisie, en el desvío suroeste): tramo señalado como peligroso por los camiones madereros, el exceso de velocidad y el mal estado mecánico de los vehículos locales. Es el punto negro de tráfico del país.",
        "Controles de gendarmería: frecuentes en todo el país, sobre todo a la entrada y salida de cada población. Documentación en regla, copias a mano, trato correcto y paciencia. Es normal que pidan ver el CPD y la Carte Rose.",
        "Nada de fotos ni de drones en el río Congo, el Beach, el puerto, edificios oficiales, militares o policías, ni en las instalaciones petroleras de Pointe-Noire y Djeno. Es la causa más frecuente de un problema serio.",
        "No conducir de noche en ningún tramo: fauna, camiones madereros sin luces en el norte, baches y controles.",
        "Norte forestal (Ouesso-Etoumbi-Mbomo): el riesgo es el aislamiento, no la inseguridad. Sin cobertura, sin tráfico y sin combustible garantizado. Autonomía completa, dos vehículos y registrar el paso ante la gendarmería de Etoumbi o Mbomo antes de entrar en la pista.",
        "Carne de caza: además del riesgo sanitario, comprar o transportar bushmeat es ilegal y en el entorno de los parques se persigue activamente. No comprarla ni aunque se ofrezca en los pueblos de la pista.",
        "Comunicar la ruta y las fechas de los dos cruces del ferry a la embajada de España en Kinshasa, que es la representación competente también para Congo-Brazzaville.",
    ],
    agua=[
        "Brazzaville y Pointe-Noire: agua embotellada sin problema en supermercados; hoteles y estaciones de servicio permiten llenar el depósito de uso general con manguera. Son los dos mejores puntos de recarga completa del país.",
        "Ouesso y Owando: recarga posible en hoteles y misiones; confirmar en recepción.",
        "Norte forestal (Etoumbi, Mbomo, pista de Odzala) y mesetas Batéké: agua de río o de pozo. Filtrar y potabilizar sin excepción, y entrar en el tramo con los depósitos al 100 %.",
        "Salir de Brazzaville con los depósitos llenos antes del ferry: en Kinshasa, del otro lado, se puede pasar 1-3 días atrapado esperando el despacho del vehículo.",
    ],
    combustible=[
        "Bajada: Ntam/Souanké y Sembé tienen oferta irregular, a menudo en bidones — entrar al país con los depósitos llenos desde Camerún. Ouesso es la primera plaza con estaciones formales. A partir de ahí, y hasta Owando o de vuelta a Ouesso, hay que contar con 600-700 km sin suministro fiable si se hace el bucle de Odzala por Etoumbi y Mbomo: garrafas llenas y embudo con filtro.",
        "Eje RN2 (Ouesso-Makoua-Owando-Oyo-Gamboma-Brazzaville): estaciones formales en las capitales de departamento, con tramos de ~200 km entre ellas. Sin riesgo de gap de 500 km si se reposta en cada una.",
        "Subida por las mesetas Batéké (Ngo-Djambala-Lékana-Okoyo-Boundji): oferta escasa e irregular. Salir de Brazzaville con autonomía suficiente para llegar holgadamente a Owando.",
        "Desvío suroeste: RN1 Brazzaville-Dolisie-Pointe-Noire con estaciones formales; Pointe-Noire tiene la mejor calidad de gasóleo del país por el sector petrolero.",
    ],
    experiencias_intro=EXPERIENCIAS_INTRO,
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Gorilas · cómo se compra el permiso", "Escribir a African Parks / Visit Odzala y a Kamba (Ngaga) preguntando EXPRESAMENTE si un grupo que llega con vehículo propio puede comprar solo el permiso de trekking (750 $/persona) y el guía, sin contratar el paquete de lodge, y en qué condiciones. Es la pregunta número uno de esta ficha."),
        ("Gorilas · alternativa de operador local", "Pedir presupuesto escrito a operadores locales (p. ej. Congo Travel & Tours) por una fórmula mixta: nosotros ponemos los vehículos y el alojamiento, ellos el permiso, el guía y las tasas. Comparar con el paquete de ecoturismo de ~7 días que ya venden."),
        ("Odzala · el perro", "Obtener por escrito de African Parks la política sobre perros en el parque y en los alojamientos de la periferia (Mbomo, Etoumbi), y cerrar el plan B: pensión con patio cerrado o cuidador contratado, y reparto de turnos entre los tres viajeros. No improvisarlo sobre la marcha."),
        ("Frontera de Ntam/Souanké", "Confirmar coordenada exacta del puesto, si el cruce del Ngoko/Dja es por puente o barcaza, horario, si sellan CPD allí y —crítico— si admite vehículos particulares extranjeros. Contactar con el consulado del Congo en Camerún y buscar overlanders recientes con 60 días de antelación."),
        ("Ferry · precio real del vehículo", "Obtener al menos tres presupuestos escritos para cruzar los DOS vehículos, ida y vuelta, con desglose de tasas. La referencia alta conocida son los 4.000 €/vehículo del servicio VIP de Congo Travel & Tours: no aceptarla como precio de mercado sin buscar alternativa."),
        ("Ferry · calendario del bac de vehículos", "Confirmar días y horas reales de salida de la barcaza de vehículos y si hay que reservar plaza. El pasaje de personas es diario; el de vehículos, no. Coordinar con la ficha de RD Congo."),
        ("Visado · trámite desde España", "Confirmado que no hay embajada del Congo en España y que el MAEC remite a la de París (GIRAFE). Falta confirmar con ese consulado: si aceptan solicitudes de residentes en España por correo, qué justificante de entrada/salida admiten para un viaje por tierra sin billete de avión, y si emiten entrada múltiple con validez de varios meses."),
        ("Visado · dos entradas y fechas", "El visado congoleño lleva fechas de entrada y salida concretas. Confirmar si un único visado de entradas múltiples puede cubrir las dos pasadas (separadas por meses) o si hay que gestionar el segundo en ruta, y dónde (Yaundé, Luanda o Kinshasa)."),
        ("Salida subida · Socambo", "Confirmar que la barcaza del Ngoko admite vehículos de 3 t y que la aduana camerunesa de Moloundou sella CPD. Si no, replanificar la salida por Ntam. Coordinar con la ficha de Camerún."),
        ("Desvío suroeste · decisión", "Decidir si Pointe-Noire, Diosso y Conkouati entran en el calendario (~1.000 km y 4-6 días) o si se sustituyen por más días en Odzala. Valorar la opción de hacerlo en el tren Congo-Océan dejando los vehículos en Brazzaville."),
        ("Nouabalé-Ndoki · decisión", "Decidir si se hace (3-5 días extra desde Ouesso, con logística fluvial) o si se descarta por concentrar el esfuerzo en Odzala. Pedir a WCS el cuadro de tasas actualizado."),
        ("Conkouati-Douli · tarifas y acceso", "Escribir a info.pncd@noe.org por tarifas, alojamiento, estado de las pistas y calendario de anidación de tortugas, si finalmente se hace el desvío suroeste."),
        ("Lésio-Louna · visita sin reserva", "Confirmar con la Fundación Aspinall las tasas, el horario y si admiten visita de un día sin reserva previa, para encajarlo en el corredor de subida."),
        ("Ogooué-Leketi", "Confirmar si el parque nacional de las mesetas Batéké tiene en 2027 acceso turístico abierto y si merece un desvío desde Lékana."),
        ("Ferrocarril Congo-Océan", "Confirmar si el tren «La Gazelle» Brazzaville-Pointe-Noire circula con regularidad en 2027, frecuencia y precio: sería la forma de ver el suroeste sin mover los vehículos."),
        ("Ébola y sanidad", "Comprobar 30 días antes el estado epidemiológico de Cuvette-Ouest y de la cuenca del Congo en el ECDC y la OMS, y su efecto sobre los controles de frontera y el acceso al parque."),
        ("Pool · seguridad", "Revalidar 30-60 días antes la situación de la región del Pool si se hace el desvío suroeste por la RN1."),
        ("Fotos pendientes de sustituir", "Souanké/Sembé, Ouesso, Nouabalé-Ndoki, los bais de Odzala, Loufoulakari, Diosso, Conkouati, el CFCO y las mesetas Batéké usan imágenes de referencia de la especie o de la región, no del propio sitio: sustituir por fotos propias cuando las tengamos."),
        ("Dron", "Contactar con la ANAC-Congo o, más realista, asumir que no se vuela en este país."),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Las tarifas de Odzala citadas son las públicas de 2025 y hay que revalidarlas para 2027.",
    emergency="Emergencia consular española (Kinshasa, competente también para Congo-Brazzaville): +243 819 500 289 · Embajada: +243 813 300 061.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

# -*- coding: utf-8 -*-
"""Camerún — ficha completa, corredor doble bajada/subida (12 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== BAJADA: Ekok/Mfum (Nigeria) -> Mamfe -> Kumba -> Limbe/Buea -> Duala -> Kribi -> Sangmélima -> Djoum -> Ntam (Congo) =====
    dict(n=1, name="Mamfe (paso obligado de entrada)", cat="Ciudad · servicios", prio="Media", dog="no recomendado", time="sin pernocta",
         lat=5.7500, lon=9.3167,
         desc="Capital del departamento de Manyu, a 70 km del paso de Ekok/Mfum y primera población camerunesa de la ruta. Está en pleno corazón de la crisis anglófona: es nudo de la carretera Ekok-Bamenda y ha sufrido enfrentamientos, secuestros y «ciudades muertas» (lockdowns) impuestas por los separatistas. Aquí solo se para lo imprescindible (formalidades, combustible si lo hay) y se sigue el mismo día hacia Kumba y la costa. NO pernoctar, NO desviarse hacia Bamenda.",
         credit="Wikimedia Commons", source=W + "Limbe%20wildlife%20center.jpg?width=900"),
    dict(n=2, name="Kumba y el lago cratérico de Barombi Mbo", cat="Naturaleza", prio="Baja", dog="no recomendado", time="paso, sin parada",
         lat=4.6667, lon=9.4167,
         desc="Kumba es la mayor ciudad del interior de la región Suroeste y el segundo punto caliente del tránsito de entrada. A 5 km al norte está el lago Barombi Mbo, un lago cratérico volcánico de unos 2,5 km de diámetro y más de 110 m de profundidad, famoso entre biólogos por sus peces cíclidos endémicos (uno de los mejores ejemplos mundiales de especiación en un lago cerrado). En condiciones normales sería una parada obligada; en el contexto actual de la crisis anglófona se documenta como PDI pero se atraviesa Kumba sin detenerse. Solo visitable si la situación cambia radicalmente antes de 2027.",
         credit="Wikimedia Commons", source=W + "Limbe%20wildlife%20center.jpg?width=900"),
    dict(n=3, name="Limbe · playas de arena negra y Wildlife Centre", cat="Costa", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=4.0186, lon=9.2054,
         desc="Ciudad costera a los pies del monte Camerún, con playas de arena negra volcánica (Down Beach, Mile 6, Seme Beach) donde la lava llegó literalmente al mar, y el Limbe Wildlife Centre, santuario de gorilas, chimpancés, drills y mandriles rescatados del tráfico de carne de monte. Es la parte del Suroeste (departamento de Fako) menos afectada por el conflicto y la única pernocta razonable del tramo de entrada, pero sigue en región anglófona: verificar la situación local antes de quedarse.",
         credit="Ndiptambe · CC0", source=W + "Limbe%20wildlife%20center.jpg?width=900"),
    dict(n=4, name="Monte Camerún (4.095 m) · «Mount Fako»", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="2–3 días (trekking)",
         lat=4.2033, lon=9.1706,
         desc="El techo del África occidental y uno de los volcanes más activos del continente (erupciones en 1999, 2000 y 2012), que se levanta desde el nivel del mar hasta 4.095 m en apenas 25 km horizontales: de selva a páramo alpino y campos de lava en una sola subida. Es LA gran excursión a pie del país. El trekking clásico son 2-3 días por la «Guinness Route» desde Buea (1.000 m) con refugios básicos (Hut 1, 2 y 3); la Course de l'Espoir / Race of Hope sube y baja en un solo día (unas 4 h 30 los ganadores). Guía obligatorio del Mount Cameroon Inter-Communal Ecotourism Organisation (MCIEO) en Buea. AVISO: Buea está en la región Suroeste — verificar seguridad y lockdowns antes de comprometer 3 días aquí.",
         credit="Wikimedia Commons", source=W + "Limbe%20wildlife%20center.jpg?width=900"),
    dict(n=5, name="Duala", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=4.0483, lon=9.7043,
         desc="Capital económica, mayor puerto de África central y la mejor plaza del país para talleres, recambios, neumáticos y soldadura, además de aeropuerto internacional. Es también el punto donde se sale de la región anglófona y se entra en el Camerún francófono: a partir de aquí el viaje baja mucho de tensión. Calor húmedo intenso y tráfico caótico; barrios de Bonanjo y Bonapriso para servicios y alojamiento con aparcamiento.",
         credit="Mboupda Talla Roger · CC BY-SA 3.0", source=W + "Port%20autonome%20de%20Douala%201.jpg?width=900"),
    dict(n=6, name="Kribi", cat="Costa", prio="Alta", dog="permitido", time="2 noches",
         lat=2.9369, lon=9.9096,
         desc="La mejor playa de Camerún: arena blanca, cocoteros y un mar tranquilo, con la mejor oferta de pescado y marisco a la brasa de la costa (los «kilomètres» de chiringuitos al sur del pueblo). Puerto de aguas profundas al norte (Kribi Deep Sea Port). Es la parada de descanso natural del corredor de bajada antes de internarse en la selva del sureste, y uno de los pocos sitios del país completamente cómodos con el perro.",
         credit="Wikimedia Commons", source=W + "Les%20chutes%20de%20la%20lobé%20kribi%20cameroon1.jpg?width=900"),
    dict(n=7, name="Cataratas de la Lobé", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=2.8500, lon=9.8833,
         desc="A 8 km al sur de Kribi, el río Lobé se descuelga en una cortina de saltos de unos 20 m que caen DIRECTAMENTE sobre el Atlántico: uno de los dos o tres únicos sitios del mundo (y el único de África) donde una catarata desemboca en el mar. Se puede caminar por las rocas hasta la base, bañarse en las pozas de agua dulce a pocos metros de la rompiente y subir en piragua río arriba hasta campamentos de pigmeos bagyeli. Está en la lista indicativa de la UNESCO. Acceso libre por la carretera de Campo, con tasa local y aparcamiento.",
         credit="Blaizo 237 · CC BY-SA 4.0", source=W + "Les%20chutes%20de%20la%20lobé%20kribi%20cameroon1.jpg?width=900"),
    dict(n=8, name="Parque Nacional de Campo Ma'an", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=2.3667, lon=10.1000,
         desc="2.640 km² de selva atlántica costera en el extremo suroeste, entre el mar y la frontera de Guinea Ecuatorial, creado como compensación ambiental del oleoducto Chad-Camerún. Elefantes de bosque, gorilas de llanura occidental, chimpancés, mandriles y búfalos; playas de desove de tortuga laúd en la costa de Ebodjé, donde hay un proyecto de ecoturismo comunitario. Pistas forestales de tierra desde Kribi: 75 km hasta Campo. Acceso y guías a través del MINFOF en Campo — confirmar tasas y estado de pistas antes de ir.",
         credit="Wikimedia Commons", source=W + "Les%20chutes%20de%20la%20lobé%20kribi%20cameroon1.jpg?width=900"),
    dict(n=9, name="Sangmélima", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=2.9333, lon=11.9833,
         desc="Capital del departamento de Dja-et-Lobo y ÚLTIMA plaza de servicios reales (combustible formal, taller, hospital, banco, mercado) antes de los 325 km del corredor Ketta-Djoum hacia la frontera del Congo. Punto de no retorno logístico de la bajada: lo que no se consiga aquí no se consigue hasta Ouesso, ya en Congo. Cabecera de la carretera del corredor Brazzaville-Yaundé financiado por el BAD.",
         credit="Wikimedia Commons", source=W + "Yaoundé%201.jpg?width=900"),
    dict(n=10, name="Reserva de Fauna del Dja (UNESCO)", cat="Patrimonio UNESCO", prio="Alta", dog="no confirmado — tratar como prohibido", time="2–3 días",
         lat=3, lon=13,
         desc="5.260 km² de selva tropical húmeda casi intacta, rodeada en el 90 % de su perímetro por el meandro del río Dja, Patrimonio Mundial de la UNESCO desde 1987 y Reserva de la Biosfera. Una de las mayores y mejor conservadas selvas de África: gorila de llanura occidental, chimpancé, elefante de bosque, bongo, pangolín gigante y más de 320 especies de aves. También es territorio de los baka. Accesos principales: Somalomo (norte, desde Abong-Mbang) y el flanco sur desde Djoum/Mintom, que es justo el que roza nuestro corredor de bajada. Guía obligatorio del MINFOF; la visita es de selva cerrada a pie, no de safari en coche.",
         credit="Wikimedia Commons", source=W + "Yaoundé%201.jpg?width=900"),
    dict(n=11, name="Djoum · cabecera de la carretera Ketta-Djoum", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=2.6667, lon=12.6667,
         desc="Pueblo de la selva del sur, a 120 km de Sangmélima, que da nombre al corredor internacional Ketta-Djoum (Camerún-Congo). Últimas garrafas, últimos víveres y última cobertura móvil fiable antes de Mintom y de la frontera de Ntam. Base sur para el flanco meridional de la reserva del Dja y punto donde conviene registrar el paso ante la gendarmería antes de afrontar el tramo final hacia el Congo.",
         credit="Wikimedia Commons", source=W + "Yaoundé%201.jpg?width=900"),
    # ===== NUDO COMPARTIDO =====
    dict(n=12, name="Yaundé", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=3.8480, lon=11.5021,
         desc="Capital política, asentada sobre siete colinas a 750 m de altitud, con un clima mucho más llevadero que Duala. Embajada de España, resto de embajadas del tramo centroafricano (Congo, RD Congo, Gabón), Hôpital Central y Hôpital Général, supermercados con producto europeo y la mejor base administrativa del país para visados y trámites de vehículo. Monumento de la Reunificación, museo nacional y el mercado de Mfoundi. Nudo compartido por los dos corredores.",
         credit="Eavebe · CC BY-SA 3.0", source=W + "Yaoundé%201.jpg?width=900"),
    # ===== SUBIDA: Ouesso/Socambo (Congo) -> Moloundou -> Yokadouma -> Bertoua -> Yaundé -> Foumban -> Dschang -> Duala -> Mamfe -> Ekok =====
    dict(n=13, name="Moloundou y el río Ngoko", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=2.0333, lon=15.2000,
         desc="Último pueblo del extremo sureste de Camerún, sobre el río Ngoko, que aquí hace de frontera con el Congo. El puesto fronterizo de Socambo, unos kilómetros aguas abajo, es el paso fluvial hacia Ouesso: cruce en barcaza o piragua motorizada, sin puente. Es el punto de entrada de la subida y el arranque de la pista forestal más dura de todo el corredor camerunés, la que sube hacia Yokadouma entre concesiones madereras.",
         credit="Wikimedia Commons", source=W + "Port%20autonome%20de%20Douala%201.jpg?width=900"),
    dict(n=14, name="Parque Nacional de Lobéké y los baka", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="2 días",
         lat=2.3000, lon=15.6167,
         desc="2.170 km² de selva del Congo en el extremo sureste, parte del Trinacional de la Sangha (Patrimonio Mundial de la UNESCO junto con Nouabalé-Ndoki en Congo y Dzanga-Sangha en la República Centroafricana). Su mayor atractivo son los «bais»: claros pantanosos en plena selva con torres de observación (Djangui, Petite Savane) desde donde se ven elefantes de bosque, gorilas, sitatungas y bongos que salen al descubierto, a veces decenas a la vez. Es también el territorio del pueblo baka, con proyectos de guía y recolección en la selva gestionados por las propias comunidades desde Mambélé. Acceso por pista desde la carretera Yokadouma-Moloundou; permisos del MINFOF en Yokadouma o Mambélé.",
         credit="Wikimedia Commons", source=W + "Limbe%20wildlife%20center.jpg?width=900"),
    dict(n=15, name="Yokadouma", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=3.5167, lon=15.0500,
         desc="Capital del departamento de Boumba-et-Ngoko y única plaza con servicios (combustible formal irregular, taller elemental, hospital de distrito, misión católica) en los 500 km de selva entre Moloundou y Bertoua. Base logística para Lobéké y para los campamentos baka de Mambélé. Ciudad de madereros: el tráfico de camiones cargados de troncos marca el ritmo —y el estado— de la pista.",
         credit="Wikimedia Commons", source=W + "Port%20autonome%20de%20Douala%201.jpg?width=900"),
    dict(n=16, name="Bertoua", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=4.5833, lon=13.6833,
         desc="Capital de la región del Este y primera ciudad grande al salir de la selva: combustible garantizado, bancos con cajeros, hospital regional, hoteles con aparcamiento y el reencuentro con el asfalto continuo hacia Yaundé. Es el punto donde termina el tramo verdaderamente remoto de la subida.",
         credit="Wikimedia Commons", source=W + "Port%20autonome%20de%20Douala%201.jpg?width=900"),
    dict(n=17, name="Mefou · santuario de primates (Ape Action Africa)", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="½–1 día",
         lat=3.6167, lon=11.6000,
         desc="A unos 45 km al sur de Yaundé, dentro del Parque Nacional de Mefou, el santuario de Ape Action Africa acoge más de 300 primates rescatados del tráfico: gorilas de llanura occidental, chimpancés, mandriles, drills y varias especies de cercopitecos, en grandes recintos de selva. Es la forma más fiable y más ética de ver grandes simios en Camerún sin depender de la suerte en la selva profunda, y una visita de medio día desde la capital. ATENCIÓN: por riesgo de transmisión de enfermedades a los primates, los perros no entran en ningún caso.",
         credit="Wikimedia Commons", source=W + "Limbe%20wildlife%20center.jpg?width=900"),
    dict(n=18, name="Foumban · palacio del sultán bamún", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="1 día",
         lat=5.7167, lon=10.9000,
         desc="Capital histórica del reino bamún, una de las monarquías tradicionales vivas más importantes de África occidental y central, con una dinastía documentada desde el siglo XIV. El Palacio Real (1917, de ladrillo, inspirado en la arquitectura alemana) alberga el Museo del Sultanato, reinaugurado en 2023 en un espectacular edificio nuevo con forma de araña-serpiente-abeja (los emblemas dinásticos). Aquí el sultán Njoya inventó a comienzos del siglo XX la escritura bamum (a'ka-u-ku), un sistema propio que aún se enseña. El barrio de artesanos (Rue des Artisans) es el mejor de Camerún para bronce, latón y talla. En la lista indicativa de la UNESCO.",
         credit="Wikimedia Commons", source=W + "Yaoundé%201.jpg?width=900"),
    dict(n=19, name="Chefferie de Bandjoun (Bafoussam)", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=5.3667, lon=10.4167,
         desc="La más célebre de las chefferies bamileké del país de las Praderas: un conjunto de casas-palacio de planta cuadrada con altísimos techos cónicos de paja y fachadas de postes tallados, alineadas tras una gran plaza ceremonial. Museo de la Chefferie con máscaras, tronos de perlas y trajes reales. Las chefferies bamileké del oeste están en la lista indicativa de la UNESCO. A 15 km de Bafoussam, gran plaza de servicios de la región Oeste.",
         credit="Wikimedia Commons", source=W + "Yaoundé%201.jpg?width=900"),
    dict(n=20, name="Dschang y las cataratas de la Métché", cat="Naturaleza", prio="Media", dog="permitido", time="1 noche",
         lat=5.4500, lon=10.0500,
         desc="Dschang, a 1.400 m en las montañas bamileké, es la ciudad de clima más agradable de Camerún (los alemanes y luego los franceses la usaron como estación de altura) y base del célebre «Centre Climatique». A 12 km, las cataratas de la Métché caen unos 60 m en un circo de selva; sitio de memoria de las guerras de independencia. Desde Dschang arranca la espectacular bajada del escarpe hacia Santchou y Melong, con más de 1.000 m de desnivel en pocos kilómetros.",
         credit="Wikimedia Commons", source=W + "Yaoundé%201.jpg?width=900"),
    dict(n=21, name="Cataratas de Ekom-Nkam y monte Manengouba", cat="Naturaleza", prio="Alta", dog="permitido con precaución", time="1–2 días",
         lat=5.0833, lon=9.9167,
         desc="Las cataratas de Ekom-Nkam, cerca de Melong, caen 80 m en un anfiteatro de selva primaria y son famosas por haber sido el escenario de la película «Greystoke: la leyenda de Tarzán» (1984); sendero escalonado hasta el mirador inferior y hasta la poza. A media hora, el monte Manengouba (2.411 m), un volcán con dos lagos de cráter gemelos —el «lago macho» y el «lago hembra»— en una caldera de pastos de altura a la que se sube en 4x4 por pista y luego a pie, con vistas sobre todo el valle del Mungo. Uno de los mejores sitios del país para caminar con el perro y acampar en alto, fuera de parque nacional.",
         credit="Wikimedia Commons", source=W + "Yaoundé%201.jpg?width=900"),
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
    ("Frontera · Entrada bajada — Ekok/Mfum (desde Nigeria)", "Frontera", 5.9400, 9.0650,
     "Único paso terrestre asfaltado y con aduana plena entre Nigeria y Camerún en el sur. Cruce del río Cross (Mfum, Nigeria → Ekok, Camerún) y 70 km hasta Mamfe, en plena región Suroeste, zona de conflicto activo de la crisis anglófona. NUNCA cruzar en lunes (día de «ciudad muerta» semanal impuesto por los separatistas) ni en las fechas simbólicas del conflicto (1 de octubre, 11 de febrero, 20 de mayo). Horario diurno; posibles cierres súbitos. Es también la frontera de SALIDA de la subida."),
    ("Frontera · Salida bajada — Ntam / Souanké (hacia Congo)", "Frontera", 2.3500, 13.9500,
     "Puesto camerunés de Ntam sobre el río Ngoko/Dja, extremo de la carretera del corredor Ketta-Djoum (Sangmélima-Djoum-Mintom-Ntam), financiada por el Banco Africano de Desarrollo dentro del corredor Brazzaville-Yaundé. Al otro lado, Ntam-Congo y la carretera Ntam-Souanké-Sembé-Ouesso. Coordenada aproximada: CONFIRMAR la posición exacta del puesto, si el cruce del río es por puente terminado o por barcaza (bac), el horario y si la aduana camerunesa sella CPD aquí o hay que hacerlo en Yaundé/Sangmélima. Transporte público prácticamente inexistente en este eje."),
    ("Frontera · Entrada subida — Socambo / Moloundou (desde Congo)", "Frontera", 2.0167, 15.1833,
     "Paso fluvial sobre el río Ngoko frente a Ouesso: cruce en barcaza o piragua motorizada, sin puente. Alternativa deliberada al Ntam para que la subida recorra el sureste forestal en vez de repetir el corredor Ketta-Djoum. CRÍTICO POR CONFIRMAR: capacidad real de la barcaza para vehículos de 3 t, frecuencia, horario y si la aduana camerunesa de Moloundou está habilitada para sellar CPD de vehículo extranjero. Si no lo está, el plan B es reentrar por Ntam y llegar al sureste por Sangmélima-Abong-Mbang-Yokadouma."),
    ("Embajada de España en Yaundé", "Consular", 3.8944, 11.5139,
     "Bld. de l'U.R.S.S., Quartier Bastos, B.P. 877, Yaundé. Tel. +237 222 20 35 43 · Emergencia consular 24 h: +237 698 44 79 00 · emb.yaunde@maec.es."),
    ("Hôpital Central de Yaundé", "Hospital", 3.8720, 11.5180,
     "Principal hospital de referencia de la capital y del país, junto con el Hôpital Général de Yaoundé. Coordenada urbana aproximada."),
    ("Hôpital Laquintinie — Duala", "Hospital", 4.0430, 9.6980,
     "Gran hospital público de referencia de la capital económica; la alternativa privada habitual para extranjeros es la Polyclinique Bonanjo. Coordenada urbana aproximada."),
    ("Hôpital Régional de Bertoua", "Hospital", 4.5833, 13.6833,
     "Única referencia hospitalaria seria del corredor de subida entre la frontera del Congo y Yaundé: unos 500 km de selva sin nada equivalente."),
    ("Combustible · Duala / Yaundé", "Combustible", 4.0483, 9.7043,
     "Mejor oferta y calidad del país (Tradex, TotalEnergies, Oryx, Neptune) en las dos grandes ciudades; repostar a fondo en ambas y filtrar el gasóleo fuera de ellas."),
    ("Combustible · Kribi / Ebolowa / Sangmélima", "Combustible", 2.9333, 11.9833,
     "Estaciones formales en el eje sur. Sangmélima es la ÚLTIMA con garantía antes de los 325 km del corredor Ketta-Djoum: salir de aquí con depósitos y garrafas al 100 %."),
    ("Combustible · Djoum y Mintom (escaso)", "Combustible", 2.6667, 12.6667,
     "Oferta irregular y a menudo en bidones a precio de reventa; no contar con ella para la planificación. Autonomía necesaria: Sangmélima → Ouesso (Congo), del orden de 600 km."),
    ("Combustible · Yokadouma y Moloundou (muy escaso)", "Combustible", 3.5167, 15.0500,
     "En el sureste forestal el combustible formal falla con frecuencia y se compra en bidones a los madereros. Planificar autonomía completa Bertoua → Moloundou (~500 km) en la subida, con margen extra por el consumo en barro y pista."),
    ("Combustible · Bafoussam / Nkongsamba (eje oeste)", "Combustible", 5.4737, 10.4179,
     "Estaciones formales y buena oferta en todo el eje Yaundé-Foumban-Bafoussam-Dschang-Nkongsamba-Duala de la subida; sin tramos comprometidos."),
    ("Agua potable y de uso general · Duala y Yaundé", "Agua potable", 4.0483, 9.7043,
     "Agua embotellada (Tangui, Supermont) sin problema en supermercados de las grandes ciudades; estaciones de servicio, hoteles y campamentos de Limbe, Kribi, Duala, Yaundé y Bafoussam permiten llenar el depósito de uso general con manguera."),
    ("Agua · Sangmélima y Kribi (última recarga fiable del sur)", "Agua potable", 2.9369, 9.9096,
     "Kribi y Sangmélima son los últimos puntos con recarga cómoda antes del corredor Ketta-Djoum; en Djoum y Mintom el agua es de pozo o de río y hay que tratarla sin excepción."),
]

DRONE_CALLOUT = ("warn", "Prácticamente inviable: riesgo real de detención",
                  "Camerún trata los drones como material de inteligencia militar. La autorización debe solicitarse ante la Cameroon Civil Aviation Authority (CCAA) y, en la práctica, también ante el Ministerio de Defensa, por el doble contexto de conflicto (crisis anglófona y Boko Haram). Se han documentado incautaciones en la aduana del aeropuerto de Duala y detenciones de extranjeros por volar o simplemente por llevar el aparato. Norma prudente del proyecto: NO introducir el dron en Camerún, o declararlo y precintarlo en aduana si es inevitable. Volar en el Noroeste, el Suroeste o el Extremo Norte se considera fuera de discusión.")

STARLINK_CALLOUT = ("warn", "No autorizado: los kits se han incautado en frontera",
                     "Camerún ha mantenido una postura abiertamente restrictiva: la Agence de Régulation des Télécommunications (ART) no ha concedido licencia a Starlink y se han documentado incautaciones de terminales en aduanas y controles, en un país donde el espacio de comunicaciones está bajo control estrecho por los dos conflictos activos. Situación a mediados de 2026 sin cambio confirmado. Tratarlo como NO DISPONIBLE y, además, como un riesgo aduanero en sí mismo: guardar la antena desmontada y declarada si se lleva en tránsito, y usar SIM local (MTN Cameroon, Orange Cameroun, Camtel) como conectividad principal. Confirmar el estado 30-60 días antes en el mapa oficial de Starlink.")

DOG_MATRIX = [
    ("Regiones Noroeste y Suroeste (Mamfe, Kumba y el tránsito de Ekok)", "no recomendado",
     "Zona de conflicto activo: nada de pernocta ni paradas con el perro. Cruzar directos hacia Limbe o Duala el mismo día. Llevar agua y sombra en el vehículo para todo el tramo, porque no habrá paradas cómodas."),
    ("Limbe, Kribi, playas y cataratas de la Lobé", "permitido",
     "Las mejores paradas del país con el perro: playas abiertas, arena, sombra de cocoteros y alojamientos con parcela. En la Lobé, correa en las rocas mojadas y no dejarlo entrar en el mar junto a la rompiente de la catarata. Calor húmedo permanente: sombra y agua constantes."),
    ("Duala, Yaundé, Bafoussam, Bertoua (ciudades)", "permitido con condiciones",
     "Sin restricción específica; hoteles con aparcamiento suelen aceptarlo pagando suplemento. Nunca dejarlo solo en el vehículo con calor: en Duala se superan los 32 °C con 90 % de humedad."),
    ("Monte Manengouba, lagos gemelos, Dschang, Métché, Ekom-Nkam", "permitido con precaución",
     "Fuera de parque nacional: es LA mejor combinación del país de naturaleza y excursión a pie compatible con el perro. Correa en los senderos escalonados de Ekom-Nkam y la Métché (roca mojada y caídas verticales) y cuidado con el ganado y los perros de los pastores en la caldera del Manengouba."),
    ("Parques nacionales: Dja, Lobéké, Campo Ma'an, Mefou, Waza", "no confirmado — tratar como prohibido",
     "El MINFOF no publica una norma general sobre mascotas, pero todos estos espacios tienen elefante de bosque, gorila y chimpancé: el riesgo de transmisión de enfermedades a los grandes simios hace que la prohibición sea la práctica universal en este tipo de reservas. En Mefou (Ape Action Africa) y en el Limbe Wildlife Centre es explícitamente inviable por bioseguridad. PLAN B: turnos entre los tres viajeros —uno se queda con el perro en Sangmélima, Yokadouma o Yaundé— o guardería en el hotel de base, que en Yaundé y Duala sí existe. Confirmar por escrito con el MINFOF y con Ape Action Africa antes de viajar."),
    ("Monte Camerún (trekking de 2-3 días desde Buea)", "no confirmado",
     "El parque nacional del monte Camerún es gestionado por el MINFOF con guías del MCIEO. No hay norma pública sobre perros y la subida son 2-3 días con refugios compartidos y 4.095 m de desnivel acumulado: aunque se autorizara, no es una excursión apta para el perro. PLAN B: dejarlo en Limbe con uno de los viajeros y hacer la cumbre por turnos, o limitarse a los senderos bajos de la selva de Buea."),
    ("Extremo Norte (Waza, Rhumsiki, Montes Mandara)", "zona excluida",
     "Excluido del itinerario por Boko Haram/ISWAP, no por el perro. No aplica."),
]

SOURCES = [
    ("Cameroon eVisa · portal oficial del Gobierno de Camerún", "https://evisacam.cm/"),
    ("U.S. Department of State · Cameroon Travel Advisory", "https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories/cameroon-travel-advisory.html"),
    ("U.S. Embassy Cameroon · Travel Advisory (2026)", "https://cm.usembassy.gov/travel-advisory-cameroon-may-2026/"),
    ("UK FCDO · Cameroon travel advice, regional warnings", "https://www.gov.uk/foreign-travel-advice/cameroon"),
    ("International Crisis Group · Cameroon (crisis anglófona)", "https://www.crisisgroup.org/africa/central-africa/cameroon"),
    ("Wikipedia · Timeline of the Anglophone Crisis (2026)", "https://en.wikipedia.org/wiki/Timeline_of_the_Anglophone_Crisis_(2026)"),
    ("Wikipedia · Mamfe", "https://en.wikipedia.org/wiki/Mamfe"),
    ("A Little Off Track · overlanding por Camerún, cruce de Mfum/Ekok y ruta interior", "https://www.alittleofftrack.com/overlanding-cameroon/"),
    ("ALÁRÌNKÁ · de Camerún a Congo Brazzaville por carretera vía la frontera de Ntam", "https://alarinka.com/cameroon-to-congo-brazzaville-by-road-via-ntam-border/"),
    ("Ministère des Grands Travaux du Congo · apertura al tráfico de la carretera Sembé-Souanké-Ntam", "https://grands-travaux.gouv.cg/en/media/news/sembe-souanke-ntam-road-opens-traffic"),
    ("Business in Cameroon · Congo termina los 312 km de carretera que conectan con Camerún", "https://www.businessincameroon.com/construction/0203-10030-congo-completes-312km-road-connecting-to-cameroon"),
    ("Banco Africano de Desarrollo · Ketta-Djoum Road and Brazzaville-Yaoundé Corridor, informe de evaluación", "https://www.afdb.org/fileadmin/uploads/afdb/Documents/Project-and-Operations/Cameroon_-_Congo_-_Ketta_Djoum_Road_and_Brazzaville_Yaound%C3%A9_Corridor_Transport_Facilitation_Project_-_Appraisal_Report.pdf"),
    ("PIDA · ficha del proyecto Ketta-Djoum Road", "https://map.au-pida.org/projects/show/20110001"),
    ("Business in Cameroon · puente transfronterizo sobre el río Cross entre Ekok y Mfum", "https://www.businessincameroon.com/infrastructures/0107-10487-cameroon-and-nigeria-plan-to-build-a-trans-border-bridge-over-the-cross-river-to-boost-trade"),
    ("UNESCO · Dja Faunal Reserve", "https://whc.unesco.org/en/list/407/"),
    ("UNESCO · Sangha Trinational (Lobéké, Nouabalé-Ndoki, Dzanga-Sangha)", "https://whc.unesco.org/en/list/1380/"),
    ("Wikipedia · Mount Cameroon", "https://en.wikipedia.org/wiki/Mount_Cameroon"),
    ("Wikipedia · Lobé Falls", "https://en.wikipedia.org/wiki/Lob%C3%A9_Falls"),
    ("Wikipedia · Lake Barombi Mbo", "https://en.wikipedia.org/wiki/Lake_Barombi_Mbo"),
    ("Wikipedia · Bamum people / Sultan's Palace, Foumban", "https://en.wikipedia.org/wiki/Bamum_people"),
    ("Wikipedia · Manengouba", "https://en.wikipedia.org/wiki/Manengouba"),
    ("Ape Action Africa · santuario de primates de Mefou", "https://www.apeactionafrica.org/"),
    ("Limbe Wildlife Centre", "https://limbewildlife.org/"),
    ("Embajada de España en Camerún · contacto", "https://www.exteriores.gob.es/Embajadas/yaunde/es/Paginas/index.aspx"),
    ("Fundación Mapfre iO · información para viajeros en Camerún", "https://fundacionio.com/viajarseguro/paises/camerun/informacion-para-viajeros-camerun/"),
    ("BNCR · Carte Rose CEMAC, portal oficial", "https://bncr.cm/en/"),
    ("Business in Cameroon · Carte Rose CEMAC", "https://www.businessincameroon.com/finance/1207-6371-in-2013-2015-the-carte-rose-enabled-cemac-insurers-to-pay-cross-border-damages-worth-fcfa-382-million"),
    ("iOverlander · puntos de combustible, agua y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Bajada: Ekok -> Mamfe -> Kumba -> Limbe/Buea -> Duala -> Kribi/Lobé -> Campo Ma'an -> Ebolowa -> Sangmélima -> Djoum -> Mintom -> Ntam
CORRIDOR = [(5.9400, 9.0650), (5.7500, 9.3167), (4.6667, 9.4167), (4.1537, 9.2920), (4.0186, 9.2054),
            (4.0483, 9.7043), (3.8000, 10.1333), (2.9369, 9.9096), (2.8500, 9.8833), (2.3667, 10.1000),
            (2.9000, 11.1500), (2.9333, 11.9833), (2.6667, 12.6667), (2.6833, 13.2333), (2.3500, 13.9500)]

# Subida: Socambo/Moloundou -> Yokadouma -> Batouri -> Bertoua -> Yaundé -> Mefou -> Bafia -> Foumban -> Bafoussam -> Dschang -> Melong/Ekom-Nkam -> Nkongsamba -> Duala -> Kumba -> Mamfe -> Ekok
CORRIDOR_ALT = [(2.0167, 15.1833), (2.0333, 15.2000), (2.3000, 15.6167), (3.5167, 15.0500), (4.4333, 14.3667),
                (4.5833, 13.6833), (3.6167, 11.6000), (3.8480, 11.5021), (4.7500, 11.2333), (5.7167, 10.9000),
                (5.4737, 10.4179), (5.3667, 10.4167), (5.4500, 10.0500), (5.0833, 9.9167), (5.0167, 9.8333),
                (4.9500, 9.9333), (4.0483, 9.7043), (4.6667, 9.4167), (5.7500, 9.3167), (5.9400, 9.0650)]

CORRIDOR_LABEL = "Bajada"
CORRIDOR_ALT_LABEL = "Subida"

EXPERIENCIAS = [
    "Los controles de carretera más numerosos de África occidental: los overlanders que han cruzado Camerún coinciden en que es el país con más puestos de control del tramo atlántico —decenas en una sola jornada entre Duala y Yaundé o en el eje del Suroeste—, con gendarmería, policía, aduanas, aguas y bosques y, en las zonas de conflicto, militares. La experiencia común es que la mayoría se resuelven en menos de un minuto si se llega con la documentación preparada y se saluda en francés; la petición de «quelque chose pour le service» es frecuente pero rara vez insistente si se responde con cortesía, paciencia y sin prisa.",
    "Cruce de Ekok/Mfum desde Nigeria (relatos de overlanders publicados en A Little Off Track y otros blogs de la ruta atlántica): el paso en sí está descrito como lento pero correcto, con trámites de inmigración y aduana en Ekok y un puente sobre el río Cross; lo que condiciona todo es la situación de seguridad al otro lado, en Mamfe, no el trámite. Los relatos insisten en salir temprano de Nigeria para tener toda la jornada por delante y llegar a Duala o Limbe antes del anochecer.",
    "Corredor Ketta-Djoum hacia el Congo: la información de viajeros es escasísima —es uno de los tramos peor documentados de toda la ruta atlántica—. Lo que sí está confirmado por fuentes oficiales es que la carretera existe y fue financiada por el Banco Africano de Desarrollo dentro del corredor Brazzaville-Yaundé, y que el lado congoleño (Sembé-Souanké-Ntam, 312 km) se abrió al tráfico. El transporte público en este eje es prácticamente inexistente: quien lo ha hecho sin vehículo propio describe esperas de días para encontrar un camión. Para nosotros es una ventaja —vamos con vehículo—, pero implica que en caso de avería no hay paso de tráfico del que depender.",
    "Pista Moloundou-Yokadouma (sureste forestal): la describen como una carretera de tierra roja de anchura generosa, construida y mantenida de facto por las concesiones madereras, muy rápida en seco y un barrizal de rodadas profundas en lluvias, con camiones de troncos que no ceden el paso y levantan un polvo que reduce la visibilidad a cero. Recomendación repetida: viajar de día, dejar mucha distancia con los camiones y no intentarlo en plena temporada húmeda.",
    "Estacionalidad: el sur de Camerún tiene DOS temporadas de lluvias (marzo-junio y, la más dura, septiembre-noviembre) y dos secas (diciembre-febrero, y una pequeña seca en julio-agosto). Los relatos de viajeros coinciden en que la diferencia entre hacer el sureste forestal en seco o en lluvias es la diferencia entre una jornada normal y varios días de barro y rescates.",
    "Alojamiento y pernocta: la acampada libre no está bien vista en Camerún y, con dos conflictos activos, se desaconseja de plano. La fórmula que funciona según los viajeros es la misión católica o protestante (casi todas las poblaciones grandes tienen una, con recinto cerrado y aparcamiento) y los hoteles con patio interior en Duala, Yaundé, Bafoussam, Bertoua y Yokadouma. En Kribi y Limbe sí hay alojamientos de playa con espacio para aparcar los vehículos.",
    "Perro en parques y santuarios: ni el MINFOF ni los santuarios publican una norma escrita general, pero tanto el Limbe Wildlife Centre como Ape Action Africa (Mefou) trabajan con grandes simios y aplican protocolos de bioseguridad estrictos —cuarentena, desinfección de calzado, prohibición de visitas con síntomas de resfriado—, lo que hace impensable la entrada de un perro. Damos por hecho que es no, y planificamos turnos.",
]

HISTORIA_RESUMEN = ("Camerún es a menudo llamado «África en miniatura» por su extraordinaria diversidad geográfica y étnica —de la selva ecuatorial del sureste al Sahel del lago Chad, pasando por volcanes de 4.000 m—, resultado también de una historia colonial poco común: colonia alemana hasta 1916, fue después repartida entre Francia y Gran Bretaña, y las dos mitades "
                     "se reunificaron en una única nación en 1961, una fusión franco-británica que sigue generando un conflicto armado abierto en las regiones angloparlantes del noroeste y suroeste del país.")

HISTORIA_SECCIONES = [
    ("Reinos bamún, chefferies bamileké y sultanatos del norte",
     "El territorio albergó reinos organizados como el de los bamún (con capital en Foumban, célebre por su palacio real y por la escritura propia inventada por el sultán Njoya a comienzos del siglo XX) y sultanatos islámicos fulani en el norte, junto con el denso mosaico de chefferies bamileké del país de las Praderas —Bandjoun, Bafut, Bandjoun, Bana— que siguen funcionando hoy como autoridades tradicionales vivas, y con una gran diversidad de pequeños reinos y jefaturas en las regiones costeras y forestales."),
    ("Kamerun alemán y su reparto tras la Primera Guerra Mundial",
     "Alemania estableció el protectorado de Kamerun en 1884, desarrollando plantaciones en las laderas fértiles del monte Camerún e infraestructura ferroviaria y portuaria; tras su derrota en la Primera Guerra Mundial, el territorio fue repartido en 1922 como mandato de la Sociedad de Naciones entre Francia (la mayor parte, al este) y Gran Bretaña (dos franjas al oeste, administradas junto a Nigeria), un reparto que crearía dos tradiciones administrativas, jurídicas y lingüísticas distintas dentro de un mismo futuro país."),
    ("Independencia, la guerra de los upecistas y la reunificación de 1961",
     "El Camerún francés se independizó en 1960 tras una dura y poco conocida guerra contra la guerrilla nacionalista de la UPC; en 1961, tras un referéndum, la parte sur del Camerún británico votó unirse a la nueva república (mientras la parte norte optó por integrarse en Nigeria), dando lugar a un Camerún reunificado con dos idiomas oficiales, francés e inglés, bajo el presidente Ahmadou Ahidjo y, desde 1982, Paul Biya, uno de los jefes de Estado con más años en el poder de toda África."),
    ("Situación actual: la crisis anglófona, Boko Haram y la longevidad de Paul Biya",
     "Desde 2016-2017, las regiones angloparlantes del Noroeste y el Suroeste viven un conflicto armado abierto (la «crisis anglófona») entre el Estado camerunés y grupos separatistas que reclaman la independencia de una «Ambazonia», con miles de muertos, cerca de un millón de desplazados y lockdowns semanales impuestos a la población; en paralelo, el Extremo Norte sufre desde 2014 la insurgencia de Boko Haram e ISWAP en la cuenca del lago Chad. Paul Biya, en el poder desde 1982, sigue gobernando el país en 2026, en uno de los mandatos presidenciales más largos del mundo."),
]

HISTORIA_FUENTES = [
    ("BBC News · Cameroon country profile", "https://www.bbc.com/news/world-africa-13146029"),
    ("Encyclopaedia Britannica · Cameroon, History", "https://www.britannica.com/place/Cameroon/History"),
    ("International Crisis Group · Cameroon's Anglophone Crisis", "https://www.crisisgroup.org/africa/central-africa/cameroon"),
]

SPEC = dict(
    slug="camerun", name="Camerún", revision="12 sep 2026",
    sub="Corredor doble bajada/subida · seguridad determinante · documentación · logística",
    chips=[
        ("BAJADA", "Ekok/Mfum → Mamfe → Limbe/Buea → Duala → Kribi → Sangmélima → Djoum → Ntam (Congo) · ~1.500 km"),
        ("SUBIDA", "Socambo/Moloundou → Yokadouma → Bertoua → Yaundé → Foumban → Dschang → Duala → Mamfe → Ekok · ~1.900 km"),
        ("PDIs", "21 puntos repartidos entre los dos corredores; solo Yaundé, Duala y el eje Kumba-Mamfe se repiten"),
        ("SEGURIDAD", "Noroeste, Suroeste y Extremo Norte: conflicto activo — tránsito de un día o exclusión total"),
        ("4x4", "corredor Ketta-Djoum (Sangmélima-Djoum-Mintom-Ntam) y pista maderera Moloundou-Yokadouma"),
        ("A PIE", "Monte Camerún 4.095 m (2-3 días) · Manengouba y sus lagos gemelos · Ekom-Nkam · Lobé"),
        ("VISADO", "eVisa (evisacam.cm) — validez en frontera TERRESTRE por confirmar; alternativa: embajada en Madrid"),
        ("SEGURO", "cambio de zona: Brown Card (CEDEAO) → Carte Rose (CEMAC) al entrar"),
        ("DRONES", "no introducir: riesgo real de incautación y detención"),
        ("STARLINK", "no autorizado — kits incautados; SIM local (MTN, Orange)"),
    ],
    center=[4.3, 12.0], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y de nuevo 72 h antes de cruzar por Ekok/Mfum y antes de afrontar el corredor Ketta-Djoum.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Camerún se cruza <strong>dos veces</strong> y es, junto con Nigeria, el país donde la seguridad —no la logística— decide el trazado. "
                   "En la <strong>bajada</strong> se entra desde Nigeria por Ekok/Mfum, el único paso asfaltado del sur, se atraviesa en una sola jornada la región Suroeste en conflicto (Mamfe-Kumba) hasta la costa, y después se baja tranquilamente por Limbe, Duala, Kribi y las cataratas de la Lobé hasta Sangmélima, para tomar el <strong>corredor Ketta-Djoum</strong> (Djoum-Mintom-Ntam) y salir al Congo por el río Ngoko. "
                   "En la <strong>subida</strong> se vuelve a entrar por el sureste forestal, pero por otro sitio —el paso fluvial de Socambo/Moloundou frente a Ouesso— y se sube por la pista maderera hasta Yokadouma y Bertoua, se cruza Yaundé y se recorre el país de las Praderas (Foumban, Bandjoun, Dschang, Manengouba) antes de bajar a Duala y repetir, ahora en sentido inverso y otra vez en un solo día, el tránsito por Kumba-Mamfe hasta Ekok. "
                   "Los dos corredores solo comparten Yaundé, Duala y el tramo forzoso de entrada/salida por el Suroeste."),
    decision=("<strong>¿Es asumible entrar desde Nigeria por el sur?</strong> Sí, con condiciones estrictas, y no hay una alternativa mejor. "
              "Ekok/Mfum es el único paso terrestre Nigeria-Camerún asfaltado, con aduana plena y capaz de sellar un CPD en el sur del país; todos los demás pasos del sur son pistas locales sin aduana internacional, y los del norte (Banki, Amchidé, Kirawa) están en plena zona de operaciones de Boko Haram e ISWAP, que es un riesgo claramente peor. "
              "El problema no es la frontera, es lo que hay detrás: los 215 km de Ekok a Buea/Limbe atraviesan Mamfe y Kumba, en pleno corazón de la crisis anglófona —secuestros con rescate, artefactos explosivos improvisados en carretera, enfrentamientos y «ciudades muertas» (lockdowns) impuestos por los separatistas—. "
              "<strong>Protocolo del proyecto:</strong> (1) cruzar Ekok a primera hora y llegar a Limbe o Duala el mismo día, sin pernocta ni parada evitable entre Ekok y Buea; (2) NUNCA viajar en lunes, día de «ciudad muerta» semanal en el Noroeste y el Suroeste, ni alrededor del 1 de octubre, el 11 de febrero o el 20 de mayo, fechas simbólicas del conflicto; (3) NO desviarse en ningún caso hacia Bamenda ni hacia el Noroeste; (4) verificar la situación con fuentes locales (misiones, transportistas, hoteleros de Duala) en las 72 h previas, no solo con avisos internacionales; (5) los dos vehículos juntos, en contacto por radio, sin separarse. "
              "<strong>Si la situación empeora</strong> hasta hacer inviable el tránsito de un día, la alternativa NO es el norte: es replantear el enlace Nigeria-Camerún por completo —cruzar Nigeria hasta el eje Adamawa y entrar por los pasos de Mayo Ndaga/Banyo o Gembu, por confirmar que admitan CPD, asumiendo pista de montaña y un rodeo de más de 1.000 km; o, en el extremo, valorar el transporte marítimo Lagos-Duala del vehículo—. Esta decisión debe estar cerrada antes de entrar en Nigeria, no en la frontera."),
    facts=[
        ("Ventana prevista", "Bajada: tras Nigeria, antes de Congo (gorilas de Odzala). Subida: desde Congo hacia Nigeria, en el tramo de regreso."),
        ("Entrada bajada", "Ekok/Mfum desde Nigeria: único paso asfaltado del sur, pero atraviesa la región Suroeste en conflicto — ver decisión de ruta."),
        ("Salida bajada", "Ntam/Souanké hacia Congo, por el corredor Ketta-Djoum: el paso peor documentado de toda la ruta atlántica."),
        ("Entrada subida", "Socambo/Moloundou desde Congo (Ouesso): paso fluvial sobre el Ngoko, en barcaza — capacidad para vehículos POR CONFIRMAR; plan B, reentrar por Ntam."),
        ("Salida subida", "Ekok/Mfum hacia Nigeria: mismo tránsito de un día por el Suroeste, ahora en sentido inverso."),
        ("Visado", "eVisa oficial en evisacam.cm desde 2023, pero su aceptación en frontera TERRESTRE no está confirmada; la opción segura es el visado en la embajada de Camerún en Madrid, y con doble entrada."),
        ("Seguridad", "Noroeste y Suroeste: conflicto separatista activo, solo tránsito de un día por el eje Ekok-Mamfe-Kumba-Buea. Extremo Norte (Waza, Mandara, Rhumsiki, Maroua): EXCLUIDO sin excepción por Boko Haram/ISWAP."),
        ("Controles de carretera", "Los más numerosos de África occidental según los propios overlanders: decenas por jornada. Documentación preparada, francés y paciencia."),
        ("Seguro", "Cambio de zona regional al entrar: el Brown Card de la CEDEAO no cubre Camerún — comprar la Carte Rose CEMAC en la primera oportunidad."),
        ("Estacionalidad", "Dos temporadas de lluvias en el sur (marzo-junio y septiembre-noviembre, la peor). Las pistas del sureste forestal solo son razonables en diciembre-febrero o en la pequeña seca de julio-agosto."),
        ("Comunicaciones", "Starlink NO autorizado, con incautaciones documentadas; SIM local (MTN Cameroon, Orange, Camtel) como única base real."),
    ],
    alerts=[
        "Crisis anglófona (Noroeste y Suroeste): conflicto armado activo desde 2017 en la zona que atraviesa obligatoriamente nuestra entrada y salida hacia Nigeria. Secuestros con rescate —incluidos extranjeros y religiosos—, artefactos explosivos improvisados en carretera, enfrentamientos entre ejército y grupos separatistas y «ciudades muertas» semanales. Tránsito de un solo día por el eje Ekok-Mamfe-Kumba-Buea, nunca en lunes, nunca con pernocta.",
        "Lockdowns («ghost towns») de los lunes: los grupos separatistas imponen el cierre total de la actividad los lunes en el Noroeste y el Suroeste, y quien circula ese día es objetivo. Además hay lockdowns extraordinarios de varios días alrededor del 1 de octubre (proclamación de «Ambazonia»), el 11 de febrero (Día de la Juventud) y el 20 de mayo (fiesta nacional). Planificar el cruce de Ekok en martes, miércoles o jueves.",
        "Zona excluida — Extremo Norte: Boko Haram e ISWAP siguen operando en la cuenca del lago Chad (Logone-et-Chari, Mayo-Sava, Mayo-Tsanaga), con atentados suicidas y secuestros. Esto excluye del itinerario el Parque Nacional de Waza, los Montes Mandara, Rhumsiki y Maroua, por atractivos que sean. No hay excepción ni versión «con escolta».",
        "Zona excluida — Noroeste interior: el lago Nyos (la catástrofe de 1986) y las chefferies de Bafut están en la región Noroeste, el foco más duro de la crisis anglófona. Quedan fuera del itinerario: sus equivalentes accesibles son las chefferies bamileké de la región Oeste (Bandjoun, Bafoussam) y los lagos cratéricos del Manengouba.",
        "Frontera de Ntam (Ketta-Djoum): es el punto crítico de todo el corredor centroafricano y el peor documentado. Falta confirmar la posición exacta del puesto, si el cruce del Ngoko es por puente o por barcaza, el horario, si sellan CPD allí y si hay combustible en Mintom. Enviar correo al consulado del Congo y contactar con overlanders recientes con 60 días de antelación.",
        "Drones: riesgo real de incautación y detención, con dos conflictos activos y un régimen muy sensible a la vigilancia aérea. La recomendación del proyecto es no introducir el dron en Camerún.",
        "Starlink: no autorizado por la ART y con incautaciones documentadas en aduana. No solo no funcionará: llevarlo visible es en sí un problema en los controles.",
    ],
    ruta_intro=("Camerún se recorre dos veces por rutas casi completamente distintas. La <strong>bajada</strong> (~1.500 km) entra por el único paso asfaltado desde Nigeria, "
                "cruza en una jornada forzada la región en conflicto y después baja con calma por la costa (Limbe, Duala, Kribi, Lobé) hasta Sangmélima, para tomar el corredor "
                "Ketta-Djoum hacia el Congo. La <strong>subida</strong> (~1.900 km) vuelve por el sureste forestal (Moloundou, Lobéké, Yokadouma), cruza el país por el centro "
                "y recorre el país de las Praderas (Foumban, Bandjoun, Dschang, Manengouba) antes de repetir el tránsito de un día hacia Ekok. Etapas calculadas sobre una "
                "media de <strong>250 km/día</strong>, reducida a 150-180 km/día en las pistas forestales."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bajada 1 · Tránsito forzado", "Ekok/Mfum → Mamfe → Kumba → Buea/Limbe", "~215 km · 1 solo día, sin pernocta (zona de conflicto)"),
        ("Bajada 2 · Monte Camerún", "Limbe → Buea → cumbre (4.095 m) → Limbe", "~40 km + 2-3 días de trekking a pie"),
        ("Bajada 3 · Capital económica", "Limbe → Duala", "~70 km · 1-2 días (taller, recambios, Carte Rose)"),
        ("Bajada 4 · Costa sur", "Duala → Edéa → Kribi → cataratas de la Lobé", "~190 km · 2-3 días con descanso de playa"),
        ("Bajada 5 · Selva atlántica", "Kribi → Campo Ma'an → Kribi", "~150 km ida y vuelta · 1-2 días de pista"),
        ("Bajada 6 · Hacia el interior", "Kribi → Ebolowa → Sangmélima", "~295 km · 2 días (última plaza de servicios)"),
        ("Bajada 7 · Flanco sur del Dja", "Sangmélima → Djoum (+ incursión al Dja, UNESCO)", "~120 km · 2-3 días con la visita guiada"),
        ("Bajada 8 · Corredor Ketta-Djoum", "Djoum → Mintom → Ntam (frontera de Congo)", "~205 km · 1-2 días; tramo final el menos consolidado"),
        ("Subida 1 · Paso fluvial y selva", "Socambo/Moloundou → Mambélé/Lobéké", "~140 km · 2-3 días con los bais de Lobéké"),
        ("Subida 2 · Pista maderera", "Mambélé → Yokadouma → Batouri → Bertoua", "~440 km · 3 días; barro en lluvias"),
        ("Subida 3 · Vuelta al asfalto", "Bertoua → Abong-Mbang → Yaundé", "~340 km · 2 días"),
        ("Subida 4 · Grandes simios y capital", "Yaundé → Mefou (Ape Action Africa) → Yaundé", "~90 km ida y vuelta · 1 día"),
        ("Subida 5 · Reino bamún", "Yaundé → Bafia → Foumban (palacio del sultán)", "~300 km · 2 días"),
        ("Subida 6 · País de las Praderas", "Foumban → Bafoussam → Bandjoun → Dschang → Métché", "~150 km · 2-3 días"),
        ("Subida 7 · Volcán y cascadas", "Dschang → Santchou → Manengouba (lagos gemelos) → Ekom-Nkam → Nkongsamba", "~150 km · 2 días, pista al cráter"),
        ("Subida 8 · Bajada a la costa", "Nkongsamba → Duala", "~140 km · 1 día (última base de servicios)"),
        ("Subida 9 · Tránsito forzado de salida", "Duala → Kumba → Mamfe → Ekok/Mfum", "~365 km · 1 solo día, sin pernocta (zona de conflicto)"),
    ],
    offroad=[
        "Corredor Ketta-Djoum · Sangmélima → Djoum → Mintom → Ntam (~325 km): EL tramo crítico del corredor camerunés y uno de los peor documentados de toda la ruta atlántica. Es la carretera internacional Brazzaville-Yaundé financiada por el Banco Africano de Desarrollo; los tramos Sangmélima-Djoum y Djoum-Mintom se ejecutaron como obra asfaltada, mientras que el tramo final Mintom-Ntam y el propio cruce del río Ngoko son la parte menos consolidada y la que hay que confirmar antes de comprometerse. Sin transporte público del que depender en caso de avería, sin combustible garantizado a partir de Sangmélima y con tramos de laterita que en lluvias se convierten en barro profundo. Autonomía completa de combustible (~600 km hasta Ouesso), agua y víveres.",
        "Pista maderera Moloundou → Mambélé → Yokadouma (~230 km): la gran pista forestal del sureste, ancha, de laterita roja y mantenida de facto por las concesiones madereras. En seco es rápida y espectacular, entre paredes de selva de 40 m; en lluvias se llena de rodadas profundas y de camiones de troncos atascados que bloquean el paso durante horas. Polvo extremo en seco: dejar mucha distancia. Es el tramo 4x4 más característico del país.",
        "Yokadouma → Batouri → Bertoua (~275 km): continuación de la pista del este, con secciones asfaltadas modernas alternando con laterita degradada; puentes de madera sobre arroyos en los desvíos secundarios. Pasa por la zona de concesiones madereras y de explotación minera artesanal.",
        "Acceso a los bais de Lobéké (desde Mambélé): pistas forestales estrechas dentro de la concesión y del parque, con guía obligatorio del MINFOF; los últimos kilómetros hasta las torres de observación de Djangui y Petite Savane se hacen a pie por sendero.",
        "Kribi → Campo Ma'an (~75 km): pista de tierra costera hacia el sur por Ebodjé y Campo, entre plantaciones y selva atlántica, hasta la frontera de Guinea Ecuatorial. Vados y tramos arenosos; la zona costera de Ebodjé es playa de desove de tortuga laúd.",
        "Pista al cráter del monte Manengouba: subida de pista de montaña desde Melong o desde Nkongsamba hasta la caldera de los lagos gemelos (~2.000 m), entre pastos de altura y ganado bororo; tramos de barro y roca suelta, el mejor vivac en alto de todo el corredor camerunés.",
        "Escarpe de Dschang a Santchou: la bajada de más de 1.000 m de desnivel desde la meseta bamileké al valle del Mungo, en curvas cerradas con vistas sobre la llanura; asfaltado pero degradado y con niebla frecuente, exigente con vehículos cargados.",
        "Aviso de estacionalidad: la temporada de lluvias del sur de Camerún es brutal, con dos picos (marzo-junio y sobre todo septiembre-noviembre). Las pistas de laterita del sureste y del corredor Ketta-Djoum pasan de ser rápidas a impracticables en cuestión de horas. Planificar los dos cruces en diciembre-febrero o en la pequeña seca de julio-agosto siempre que el calendario general lo permita.",
    ],
    senderismo=[
        "Monte Camerún (4.095 m), desde Buea: LA gran excursión a pie del proyecto en toda África occidental y el punto más alto del África occidental, desde el nivel del mar hasta el páramo alpino en 25 km horizontales. El trekking clásico son 2-3 días por la «Guinness Route», con tres refugios básicos (Hut 1, 2 y 3) y campos de lava de las erupciones de 1999, 2000 y 2012 en la parte alta; la variante rápida es la de la Course de l'Espoir (Race of Hope), que sube y baja en un solo día cada febrero. Guía obligatorio del Mount Cameroon Inter-Communal Ecotourism Organisation en Buea, con porteadores opcionales. Frío real arriba (puede helar) tras haber salido del calor húmedo de la costa: ropa de abrigo imprescindible. CONDICIONADO a la situación de seguridad de la región Suroeste.",
        "Cataratas de la Lobé (Kribi): caminata corta pero única sobre las rocas hasta el pie de la cortina de saltos que cae al Atlántico; se combina con una subida en piragua por el río hasta los campamentos bagyeli y con el paseo por la playa. Roca resbaladiza y corriente fuerte: no acercarse a la rompiente.",
        "Monte Manengouba (2.411 m) y los lagos gemelos: vuelta a pie por la caldera entre los dos lagos de cráter —el «lago macho» y el «lago hembra»— por pastos de altura, con vistas al valle del Mungo y al monte Camerún en días claros. Jornada asequible y, al estar fuera de parque nacional, la mejor excursión larga del país compatible con el perro.",
        "Cataratas de Ekom-Nkam (Melong): escalera y sendero de selva primaria hasta el mirador inferior y la poza del salto de 80 m, el escenario de «Greystoke». Resbaladizo con humedad; calzado de suela agarrada.",
        "Cataratas de la Métché (Dschang): corta bajada por el circo de selva hasta el pie del salto, a 12 km de Dschang; sitio de memoria de la guerra de independencia.",
        "Reserva del Dja (UNESCO): recorridos de selva cerrada a pie con guía del MINFOF desde Somalomo o desde el flanco sur de Djoum, de medio día a varios días con campamento; no es safari en coche sino caminata por bosque húmedo, con búsqueda de rastros de gorila y elefante de bosque. Botas, sanguijuelas y mucha humedad.",
        "Bais de Lobéké (Mambélé): últimos kilómetros a pie hasta las torres de observación de Djangui y Petite Savane, donde se pasan horas en silencio viendo salir a los elefantes de bosque, bongos y sitatungas al claro. Recorridos de recolección y rastreo guiados por los baka.",
        "Lago Barombi Mbo (Kumba): vuelta al lago cratérico por sendero — descrito aquí como referencia por si la situación del Suroeste cambiara, pero NO recomendado en el escenario actual.",
    ],
    acampada=[
        "Regla general: la acampada libre NO es recomendable en Camerún, y menos con dos conflictos activos. La fórmula que funciona es la misión católica o protestante con recinto cerrado (Mamfe, Sangmélima, Djoum, Yokadouma, Bertoua) y el hotel con patio interior o aparcamiento vigilado.",
        "Regiones Noroeste y Suroeste (eje Ekok-Mamfe-Kumba): sin pernocta en ningún caso. Si una avería obligara a parar, buscar recinto de misión o de gendarmería, nunca vivac al raso —riesgo de ser confundidos con un objetivo militar o separatista—.",
        "Limbe: alojamientos y campings de playa en Mile 6 y Seme Beach, con aparcamiento; la mejor pernocta del tramo de entrada y la base para el monte Camerún.",
        "Kribi: la zona de playa al sur del pueblo y hacia las cataratas de la Lobé concentra alojamientos con parcela y espacio para los vehículos; es la parada de descanso más cómoda del país y la mejor con el perro.",
        "Duala y Yaundé: hoteles con aparcamiento cerrado (Bonanjo/Bonapriso en Duala, Bastos en Yaundé); más caro pero es la única fórmula sensata en las dos grandes ciudades.",
        "Sangmélima, Djoum y Mintom: misión católica o auberge sencillo con patio. Última pernocta con servicios antes del Ntam.",
        "Mambélé (puerta de Lobéké): campamentos de ecoturismo comunitario gestionados con los baka y el MINFOF; confirmar disponibilidad desde Yokadouma.",
        "Monte Manengouba: vivac en alto en la caldera de los lagos gemelos, con permiso del jefe del pueblo más cercano (Mouankeu/Melong) — el mejor sitio para acampar de verdad de todo el corredor, fresco, en altura y fuera de parque nacional.",
        "Bafoussam, Dschang y Foumban: hoteles urbanos con aparcamiento; Dschang, a 1.400 m, es la noche más fresca y agradable de todo el país.",
    ],
    visado=[
        "Camerún tiene eVisa oficial desde 2023 en el portal del Gobierno (evisacam.cm), pero su aceptación está acreditada sobre todo en los aeropuertos de Duala y Yaundé-Nsimalen: SU VALIDEZ EN FRONTERA TERRESTRE NO ESTÁ CONFIRMADA. Comprobarlo expresamente con la embajada antes de depender de él.",
        "Opción segura para un cruce terrestre: visado en pasaporte tramitado con antelación en la Embajada de Camerún en Madrid (tel. 91 571 11 60), solicitando expresamente ENTRADA MÚLTIPLE, porque el país se cruza dos veces con varios meses de diferencia.",
        "Si el visado de entrada múltiple no es posible o su vigencia no cubre ambos pasos, hay que planificar la obtención del segundo visado en ruta: las opciones realistas son la embajada de Camerún en Abuya o Lagos (Nigeria) para la bajada y la de Brazzaville o Pointe-Noire (Congo) para la subida. Confirmar cuál expide a extranjeros no residentes.",
        "Certificado internacional de fiebre amarilla exigido en frontera y comprobado con frecuencia en los controles de carretera del interior.",
        "Llevar muchas fotocopias del pasaporte, del visado y del sello de entrada: en los controles de carretera es preferible entregar copia y no el original.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Ekok/Mfum (Nigeria)", "Único paso asfaltado con aduana plena del sur. Cruce del río Cross. Llegar a primera hora, nunca en lunes ni en fechas simbólicas del conflicto; salir con toda la jornada por delante para alcanzar Limbe o Duala el mismo día."),
        ("Salida bajada", "Ntam / Souanké (Congo)", "Extremo del corredor Ketta-Djoum sobre el río Ngoko. POR CONFIRMAR: coordenada exacta, puente o barcaza, horario, sellado de CPD y existencia de combustible en Mintom. Es el punto más incierto de toda la ruta atlántica."),
        ("Entrada subida", "Socambo / Moloundou (Congo, desde Ouesso)", "Paso fluvial en barcaza sobre el Ngoko. POR CONFIRMAR que admite vehículos de 3 t y que la aduana de Moloundou sella CPD. Elegido para que la subida no repita el corredor Ketta-Djoum."),
        ("Alternativa entrada subida", "Ntam / Souanké (Congo)", "Plan B si Socambo no admite vehículos: reentrar por Ntam y llegar al sureste por Sangmélima-Abong-Mbang-Yokadouma, o renunciar a Lobéké y subir directamente a Yaundé."),
        ("Salida subida", "Ekok/Mfum (Nigeria)", "Mismo paso que la entrada, en sentido inverso. El tránsito Duala-Kumba-Mamfe-Ekok (~365 km) es largo para una sola jornada: salir de Duala antes del amanecer y, si no se llega, la única pernocta aceptable del tramo es Kumba en recinto de misión, y solo en caso de fuerza mayor."),
        ("Zona excluida", "Pasos del Extremo Norte (Banki, Amchidé, Kirawa)", "No se contemplan: están en plena zona de operaciones de Boko Haram e ISWAP. Ninguna circunstancia los convierte en alternativa."),
    ],
    vehiculos=[
        "CPD (carnet de paso en aduana) con todos los pares de sellos en regla: Camerún es uno de los países donde se exige en la práctica. Si el CPD no se aceptara en Ekok, la alternativa es un laissez-passer temporal emitido en la aduana — confirmar el procedimiento antes de llegar.",
        "Carte Rose CEMAC obligatoria desde la entrada: el Brown Card de la CEDEAO (Nigeria y todo el tramo anterior) NO tiene validez en Camerún. Comprarla en la primera oportunidad — la referencia oficial es el Bureau National Carte Rose (BNCR). Cubre además Congo, Gabón, Chad, RCA y Guinea Ecuatorial, así que sirve para todo el bloque centroafricano.",
        "Carnet de conducir internacional obligatorio y comprobado constantemente: es, junto con el visado, el documento que más se pide en los controles.",
        "Carpeta de controles: preparar una carpeta de plástico con copia del pasaporte y visado, carte grise/permiso de circulación, CPD, Carte Rose, carnet internacional y certificado de fiebre amarilla, más 20-30 fotocopias sueltas. Se entrega la carpeta cerrada, no los originales.",
        "Autonomía de combustible: llevar garrafas para cubrir Sangmélima → Ouesso (~600 km) en la bajada y Bertoua → Moloundou (~500 km) en la subida, con margen adicional por el mayor consumo en pista y barro.",
        "Filtro de embudo para el gasóleo: fuera de Duala y Yaundé la calidad es irregular y en el sureste se compra en bidones.",
        "Neumáticos y suspensión: la combinación de asfalto degradado, laterita y barro del sureste es exigente. Duala es la mejor —y casi la única— plaza del país para recambios, neumáticos y soldadura.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Recomendación del proyecto: NO introducir el dron en Camerún. El riesgo no es la multa, es la incautación del aparato y la detención por sospecha de espionaje, en un país con dos conflictos armados activos.",
        "Si se decide llevarlo en tránsito, declararlo en la aduana de entrada, guardarlo desmontado y precintado y no sacarlo del vehículo en todo el país.",
        "En ningún caso volar en las regiones Noroeste, Suroeste o Extremo Norte, ni cerca de instalaciones militares, puertos (Duala, Kribi), puentes o aeropuertos.",
        "La autoridad competente es la Cameroon Civil Aviation Authority (CCAA); cualquier autorización pasa además, de facto, por el Ministerio de Defensa. Plazos y viabilidad reales: por confirmar.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Tratar como NO DISPONIBLE: la ART (regulador camerunés de telecomunicaciones) no ha autorizado el servicio y se han documentado incautaciones de terminales.",
        "Llevar la antena visible es en sí un riesgo en los controles de carretera: si se transporta, desmontada y guardada, y declarada si se pregunta.",
        "SIM local como conectividad principal: MTN Cameroon y Orange Cameroun tienen la mejor cobertura 4G en el eje Duala-Yaundé-Bafoussam y en la costa; Camtel como alternativa. Comprar en Duala o Yaundé con pasaporte.",
        "Sin cobertura fiable a partir de Djoum en la bajada ni entre Moloundou y Yokadouma en la subida: dar por hecho 2-3 días incomunicados en cada corredor y avisar en casa antes de entrar.",
        "Revisar el mapa oficial de Starlink 30-60 días antes por si cambiara la situación regulatoria.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (menos de 10 días) y vacuna antirrábica en vigor (aplicada más de 30 días antes y con menos de 12 meses), exigibles en el control fronterizo de Ekok y de Moloundou/Ntam.",
        "Camerún puede exigir además un permiso de importación del MINEPIA (Ministère de l'Élevage, des Pêches et des Industries Animales): POR CONFIRMAR con la embajada en Madrid con antelación, porque tramitarlo en frontera sería inviable.",
        "Documentación en francés o con traducción: los puestos de Ekok y del sureste no trabajan en inglés ni en español.",
        "El calor húmedo permanente del sur (32 °C con 90 % de humedad en Duala y Kribi) es el problema práctico más serio del perro en este país: sombra, ventilación y agua constantes, nunca dejarlo solo en el vehículo, y evitar las horas centrales en los tránsitos largos.",
        "Ver la matriz por zona: la buena noticia es que las mejores paradas del país (playas de Kribi y Limbe, cataratas de la Lobé, Manengouba, Ekom-Nkam, chefferies) están todas FUERA de parque nacional y son compatibles con el perro. Lo que queda vetado son los parques de selva y los santuarios de primates.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional OBLIGATORIO para la entrada y comprobado también en controles de carretera del interior.",
        "Malaria en todo el territorio y durante todo el año, con transmisión especialmente intensa en la selva del sur y el sureste: profilaxis a valorar con Sanidad Exterior, más mosquitera y repelente con DEET. Es el riesgo sanitario número uno del tramo.",
        "Agua: no beber del grifo en ningún punto del país. Agua embotellada (Tangui, Supermont) en ciudades; en el sureste forestal, agua de pozo o río tratada sin excepción (filtro + químico o ebullición).",
        "Vacunación recomendada además: hepatitis A y B, fiebre tifoidea, tétanos-difteria, meningitis y rabia (especialmente relevante viajando con perro).",
        "Referencias hospitalarias: Hôpital Central y Hôpital Général de Yaundé, Hôpital Laquintinie y Polyclinique Bonanjo en Duala. Fuera de esas dos ciudades el nivel cae en picado; en el corredor Ketta-Djoum y en el sureste forestal no hay nada equivalente en 500 km.",
        "Seguro con evacuación médica real (aérea) imprescindible: es el país del viaje donde más lejos se puede estar de un hospital utilizable.",
    ],
    seguridad_intro=("Camerún es el tramo de mayor exigencia de seguridad de todo el proyecto. No es un país inseguro en su conjunto —el eje Duala-Yaundé-Kribi-Bafoussam es perfectamente manejable con precaución normal—, "
                     "pero tiene dos conflictos armados activos, y uno de ellos está justo en el único paso terrestre viable hacia Nigeria. La planificación consiste en atravesar esa zona rápido y bien, y en excluir la otra por completo."),
    seguridad=[
        "Crisis anglófona (Noroeste y Suroeste): tránsito de un solo día por el eje Ekok-Mamfe-Kumba-Buea, en ambos sentidos. Sin pernocta, sin paradas evitables, sin fotografías, los dos vehículos juntos y en contacto por radio, y siempre en horario diurno.",
        "Nunca viajar en lunes por el Noroeste o el Suroeste: es el día de «ciudad muerta» semanal impuesto por los separatistas y quien circula se convierte en objetivo. Evitar también las ventanas del 1 de octubre, el 11 de febrero y el 20 de mayo.",
        "No desviarse en ningún caso hacia Bamenda ni hacia el interior del Noroeste: es el foco más duro del conflicto. El lago Nyos y las chefferies de Bafut quedan descartados.",
        "Extremo Norte EXCLUIDO sin excepción: Boko Haram e ISWAP operan en Logone-et-Chari, Mayo-Sava y Mayo-Tsanaga, con atentados suicidas y secuestros. Eso deja fuera Waza, los Montes Mandara, Rhumsiki y Maroua.",
        "Controles de carretera: los más numerosos de África occidental según los propios overlanders. Documentación preparada en carpeta, saludo en francés, sonrisa y paciencia; las peticiones de «quelque chose» son frecuentes pero rara vez insistentes. Nunca discutir, nunca mostrar prisa, nunca entregar el pasaporte original si basta una copia.",
        "No fotografiar NUNCA controles, militares, gendarmes, puentes, puertos, aeropuertos ni edificios oficiales, en ningún punto del país. Es la causa más habitual de problemas serios para extranjeros en Camerún.",
        "Frontera de Ntam y corredor Ketta-Djoum: el riesgo aquí no es la violencia sino el aislamiento absoluto — sin tráfico del que depender, sin combustible garantizado y sin cobertura. Autonomía completa y registro del paso ante la gendarmería de Djoum antes de entrar en el tramo.",
        "Sureste forestal (Yokadouma-Moloundou): zona tranquila, pero fronteriza con la República Centroafricana, cuya inestabilidad genera desplazados y presencia militar. No acercarse a la frontera de la RCA ni desviarse por pistas hacia el este de Yokadouma.",
        "Duala y Yaundé: delincuencia urbana común (tirones, robos en atascos). Ventanillas subidas en atasco, nada visible en el salpicadero, no circular de noche.",
        "Regla general del país: no conducir de noche en ningún tramo, ni siquiera en asfalto — camiones sin luces, peatones, ganado y baches profundos.",
    ],
    agua=[
        "Duala, Yaundé, Bafoussam y Bertoua: agua embotellada (Tangui, Supermont) sin problema en supermercados; estaciones de servicio y hoteles permiten llenar el depósito de uso general con manguera.",
        "Limbe y Kribi: alojamientos de playa con manguera y agua corriente; es donde conviene dejar los depósitos al 100 % antes del interior.",
        "Sangmélima: última recarga fiable antes del corredor Ketta-Djoum. En Djoum, Mintom y Ntam el agua es de pozo o de río — tratar sin excepción.",
        "Sureste forestal (Moloundou, Mambélé, Yokadouma): agua de pozo o de río. Filtro mecánico más tratamiento químico o ebullición, siempre. La humedad ambiental es altísima pero el agua potable es escasa.",
        "En temporada de lluvias la recogida de agua de lluvia con lona es una opción real y rápida en el sureste, pero filtrar igualmente.",
    ],
    combustible=[
        "Eje costero y central (Ekok → Limbe → Duala → Kribi → Ebolowa → Sangmélima): estaciones formales suficientes (Tradex, TotalEnergies, Oryx, Neptune) y sin ningún gap de 500 km. Repostar a fondo en Duala, que es la mejor calidad del país.",
        "AVISO — bajada: a partir de Sangmélima no hay garantía. Djoum y Mintom tienen oferta irregular, a menudo en bidones, y Ntam no tiene nada. Planificar autonomía real de Sangmélima a Ouesso (Congo), del orden de 600 km, con garrafas llenas.",
        "AVISO — subida: entre Moloundou y Bertoua (~500 km) el combustible formal falla con frecuencia y se compra a los madereros en bidón. Entrar en Camerún con los depósitos llenos desde Ouesso y llevar garrafas para todo el tramo.",
        "Repostar en Nigeria (Calabar/Ikom) antes de Ekok: en Mamfe la oferta puede estar interrumpida por la situación de seguridad y no se debe depender de encontrar combustible dentro de la zona de conflicto.",
        "Filtro de embudo obligatorio fuera de Duala y Yaundé; el gasóleo de bidón del sureste puede traer agua y sedimentos.",
        "Eje oeste de la subida (Bertoua → Yaundé → Foumban → Bafoussam → Dschang → Nkongsamba → Duala): estaciones formales en todas las ciudades, sin tramos comprometidos.",
    ],
    experiencias_intro="Relatos y comentarios reales de otros overlanders sobre Camerún, para contrastar con la planificación oficial de esta ficha. Es un país con mucha menos información pública que sus vecinos, y el corredor Ketta-Djoum en particular es de los peor documentados de toda la ruta:",
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Entrada por Ekok/Mfum", "Revalidar a 60 días y de nuevo a 72 h con fuentes locales si el tránsito de un día por Mamfe-Kumba es asumible; si no, activar la alternativa Adamawa o el transporte marítimo del vehículo desde Nigeria"),
        ("Frontera de Ntam (Ketta-Djoum)", "Confirmar coordenada exacta del puesto, si el cruce del Ngoko es por puente terminado o por barcaza, horario, sellado de CPD y estado real del tramo Mintom-Ntam"),
        ("Paso de Socambo/Moloundou", "Confirmar que la barcaza del Ngoko admite vehículos de 3 t, su frecuencia y si la aduana de Moloundou sella CPD; si no, plan B por Ntam"),
        ("Visado", "Confirmar si el eVisa (evisacam.cm) es válido en frontera terrestre; en caso contrario, tramitar visado de ENTRADA MÚLTIPLE en la embajada de Madrid o planificar el segundo visado en Nigeria/Congo"),
        ("Perro · permiso MINEPIA", "Confirmar con la embajada si Camerún exige permiso de importación del MINEPIA además del certificado veterinario internacional"),
        ("Perro · parques y santuarios", "Contactar por escrito con el MINFOF, Ape Action Africa (Mefou) y el Limbe Wildlife Centre; damos por hecho que es no y planificamos turnos, pero conviene tenerlo por escrito"),
        ("Monte Camerún", "Confirmar con el MCIEO de Buea la situación de seguridad, el precio y la duración del trekking, y decidir si se compromete el tiempo de 3 días en una región en conflicto"),
        ("Reserva del Dja", "Confirmar con el MINFOF el acceso por el flanco sur (Djoum/Mintom), tasas, guías y si es compatible con el calendario del corredor Ketta-Djoum"),
        ("Lobéké y los baka", "Confirmar permisos, campamentos de Mambélé y disponibilidad de las torres de los bais; depende de que el paso de Socambo funcione"),
        ("Estacionalidad", "Ajustar las fechas de los dos cruces para caer en seca (diciembre-febrero o julio-agosto) — es lo que decide si el sureste forestal es una jornada o tres días de barro"),
        ("Carte Rose CEMAC", "Comprarla nada más entrar y confirmar que cubre también Congo, RD Congo, Gabón y el resto del bloque"),
        ("Dron", "Decisión recomendada: dejarlo fuera de Camerún. Cerrar la decisión antes de entrar en Nigeria"),
        ("Fotos pendientes de sustituir", "Varios PDIs usan imágenes de referencia de otra localidad del país: sustituir por fotos propias o por archivos verificados de Wikimedia Commons"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Las dos decisiones críticas —el tránsito por la región Suroeste y el paso de Ntam hacia el Congo— deben revalidarse activamente antes del viaje, con información local y no solo con avisos internacionales.",
    emergency="Emergencia consular española (Yaundé, 24 h): +237 698 44 79 00 · Embajada de España en Yaundé: +237 222 20 35 43 · Policía 117 · Gendarmería 113 · Bomberos 118.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

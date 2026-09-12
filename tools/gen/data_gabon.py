# -*- coding: utf-8 -*-
"""Gabón — ficha completa (12 sep 2026): EXCLUIDO de la ruta fija, alternativa informativa.

Motivo verificado por el proyecto: el eVisa gabonés SOLO sirve para llegadas aéreas al aeropuerto
Léon Mba de Libreville; la entrada por tierra exige visado tradicional gestionado en consulado.
Decisión del dueño del proyecto: "deja las fichas de Liberia y Gabón como alternativas por tener su
información pero no lo haremos". Antes se había planteado "para la subida si hay tiempo".
La ficha se mantiene completa y útil, con el estatus bien visible y con lo que haría falta para que
Gabón volviera a entrar en la ruta.
"""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

# --- Imágenes verificadas del proyecto -------------------------------------------------------
# En esta revisión NO se pudo abrir commons.wikimedia.org desde el entorno de trabajo (dominio
# bloqueado por el proxy) ni verificar nombres de archivo nuevos. Se reutilizan ÚNICAMENTE las
# cuatro fotos de Gabón ya verificadas en el proyecto más una foto de la especie (gorila de
# llanura occidental, que vive en Gabón), y cada PDI que lleva una foto que no es suya lo dice.
IMG_LIBREVILLE = W + "Boulevard%20de%20l'indépendance%20Libreville%20.jpg?width=900"
IMG_LOANGO = W + "Gabon%20Loango%20National%20Park%20Elephant%20with%20offspring.jpeg?width=900"
IMG_SCHWEITZER = W + "Albert%20Schweitzer%20Museum%20(46282656671).jpg?width=900"
IMG_MAYUMBA = W + "Mayumba%20remorqueur%20lagune.jpg?width=900"
IMG_GORILA = W + "Western%20lowland%20gorilla%20(Gorilla%20gorilla%20gorilla).jpg?width=900"

_F = " (Foto provisional: %s — pendiente de sustituir por una de este punto.)"

POIS = [
    # ===== NOROESTE: entrada desde Camerún y el estuario =====
    dict(n=1, name="Cocobeach y el estuario del Muni", cat="Costa", prio="Baja", dog="permitido", time="½ día",
         lat=0.9833, lon=9.5667,
         desc="Pueblo pesquero en el extremo noroeste, sobre la orilla sur del río Muni y en la misma frontera con Guinea Ecuatorial (hay barcaza a Cogo, al otro lado). Mercado pequeño, playas contiguas y una de las zonas más lluviosas del país: unos 3.126 mm al año, entre un 10 y un 15% más que Libreville, con estación seca más corta. Es el desvío costero natural para quien llega del norte y quiere ver el estuario antes de la capital." + _F % "la laguna de Mayumba",
         credit="Vincent.vaquin · CC BY-SA 3.0", source=IMG_MAYUMBA),
    dict(n=2, name="Monts de Cristal (Parque Nacional)", cat="Naturaleza", prio="Media", dog="prohibido", time="1–2 días",
         lat=0.5000, lon=10.3333,
         desc="Macizo boscoso al noreste de Libreville, uno de los trece parques nacionales creados en 2002 y célebre entre los botánicos por su densidad de orquídeas y begonias: es uno de los puntos de mayor diversidad vegetal de África, porque estas montañas funcionaron como refugio de selva durante las glaciaciones. Selva de ladera muy cerrada, arroyos y las cascadas y presas de Kinguélé y Tchimbélé sobre el río Mbei, que son el acceso habitual desde la carretera de Libreville. Coordenada aproximada y accesos POR CONFIRMAR." + _F % "un elefante de bosque en Loango",
         credit="Kurt Dundy · CC BY 3.0", source=IMG_LOANGO),
    dict(n=3, name="Parque Nacional de Akanda", cat="Naturaleza", prio="Media", dog="prohibido", time="½–1 día",
         lat=0.6167, lon=9.5500,
         desc="540 km² de manglar y playas de marea justo al norte de Libreville, entre las bahías de Mondah y Corisco. Gabón solo tiene el 2,5% de los manglares de África, pero Akanda y el vecino Pongara suman EL 25% DE TODO EL MANGLAR PROTEGIDO DEL CONTINENTE. Es zona Ramsar desde 2007 y área importante para las aves (IBA) de BirdLife: alberga las mayores concentraciones de aves migratorias del país, y la bahía de Corisco es zona de alimentación de tortugas marinas. Se visita en barca desde la capital." + _F % "la laguna de Mayumba",
         credit="Vincent.vaquin · CC BY-SA 3.0", source=IMG_MAYUMBA),
    dict(n=4, name="Libreville", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=0.4162, lon=9.4673,
         desc="Capital y única gran base logística del país: puerto de Owendo, aeropuerto internacional Léon Mba, EMBAJADA DE ESPAÑA (abierta desde 1962), talleres, recambios, bancos y supermercados. Ciudad extendida a lo largo del estuario, con el bulevar de la Indépendance como paseo marítimo. Su nombre —«ciudad libre»— viene de su origen: fue fundada por Francia en 1849 como asentamiento para personas esclavizadas liberadas de un barco negrero capturado, un paralelo exacto al de Freetown. Todo trámite oficial del país se hace aquí.",
         credit="Delrick Trevor · CC BY-SA 4.0", source=IMG_LIBREVILLE),
    dict(n=5, name="Parque Nacional de Pongara y Pointe Denis", cat="Costa", prio="Alta", dog="prohibido", time="1–2 días",
         lat=-0.3500, lon=9.3300,
         desc="929 km² al otro lado del estuario, enfrente mismo de Libreville: selva húmeda, manglar, bosque pantanoso, sabana y playas abiertas. Aquí anidan TORTUGAS LAÚD en una de las playas más accesibles del país (temporada de puesta en torno a noviembre-marzo), invernan hasta 10.000 limícolas y hay elefantes, gorilas y chimpancés en la selva interior. Zona Ramsar desde 2007. Se llega en barca desde Libreville en menos de una hora: es la escapada natural de la capital, aunque el vehículo se queda en tierra." + _F % "la laguna de Mayumba",
         credit="Vincent.vaquin · CC BY-SA 3.0", source=IMG_MAYUMBA),
    # ===== CENTRO Y ESTE: la selva, el tren y las cataratas =====
    dict(n=6, name="Parque Nacional de la Lopé (UNESCO)", cat="Patrimonio UNESCO", prio="Alta", dog="prohibido", time="2–3 días",
         lat=-0.2000, lon=11.5833,
         desc="PATRIMONIO MUNDIAL MIXTO DESDE 2007 como «Ecosistema y paisaje cultural relicto de Lopé-Okanda»: 4.910 km² al sur del río Ogooué donde la selva densa se abre en SABANAS QUE SON RELIQUIA DE LA ÚLTIMA GLACIACIÓN, de hace 15.000 años y mantenidas hoy con quemas controladas. El mosaico bosque-sabana permite ver fauna a campo abierto, algo rarísimo en África central: una de las mayores concentraciones de primates salvajes del mundo, la única población protegida significativa de cercopiteco de cola de sol, densidades estacionales de elefante de bosque de las más altas del planeta, mandriles en tropas enormes y leopardo. Y además arqueología: ocupación humana durante casi 400.000 años, más de 1.600 petroglifos y herramientas paleolíticas en Elarmékora. Tiene estación de investigación (Mikongo, Zoological Society of London), pueblo con alojamiento y —clave— PARADA DEL TREN TRANSGABONÉS." + _F % "un elefante de bosque en Loango",
         credit="Kurt Dundy · CC BY 3.0", source=IMG_LOANGO),
    dict(n=7, name="El tren Transgabonés (Owendo → Franceville)", cat="Cultura", prio="Alta", dog="pendiente de confirmar", time="1 noche a bordo",
         lat=0.2900, lon=9.5000,
         desc="648 km de vía única de ancho estándar abiertos en 1986 desde Owendo (junto a Libreville) hasta Franceville, con 23 estaciones intermedias —N'Toum, Ndjolé, LOPÉ, Booué, Lastourville, Moanda, Franceville— cruzando de punta a punta la selva ecuatorial. Circulan dos trenes: el Express Trans-Ogooué, que para en las estaciones principales, y el Omnibus L'Équateur, que para en todas; suelen ser NOCTURNOS en ambos sentidos y unos cuatro días por semana, con coches alemanes climatizados, coche restaurante y tres clases. Mueve unos 250.000-320.000 viajeros al año además del manganeso de Moanda. Para este proyecto es la alternativa evidente para llegar a Lopé o a Ivindo dejando los vehículos en Libreville. Coordenada: terminal de Owendo, aproximada." + _F % "Libreville",
         credit="Delrick Trevor · CC BY-SA 4.0", source=IMG_LIBREVILLE),
    dict(n=8, name="Parque Nacional de Ivindo (UNESCO) y las cataratas de Kongou", cat="Patrimonio UNESCO", prio="Alta", dog="prohibido", time="3–4 días",
         lat=0.2907, lon=12.5891,
         desc="PATRIMONIO MUNDIAL DESDE 2021: 3.000 km² de selva primaria en el este, con «las maravillas del Ivindo» —las cataratas de KONGOU y de Mingouli—. Kongou no es un salto alto sino ANCHÍSIMO: unos 3,2 km de frente escalonado, hasta 56 m de caída y un caudal medio de 900 m³/s que la sitúa entre las cascadas más potentes del mundo, en mitad de la selva y sin una sola carretera que llegue. Estuvo a punto de desaparecer: en 2007 el presidente Omar Bongo anunció una presa hidroeléctrica para alimentar la mina de hierro de Belinga, sin estudio de impacto ambiental; la oposición pública paró el proyecto. El parque incluye además el LANGOUÉ BAÏ, uno de los cinco claros de bosque más importantes de África central, donde salen al descubierto elefantes de bosque, gorilas y sitatungas, con estación de investigación de la WCS. Al norte, Makokou y la reserva de biosfera de Ipassa." + _F % "un elefante de bosque en Loango",
         credit="Kurt Dundy · CC BY 3.0", source=IMG_LOANGO),
    dict(n=9, name="Makokou", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=0.5667, lon=12.8667,
         desc="Capital de Ogooué-Ivindo y única base logística real del este forestal: combustible, provisiones y contactos para organizar la bajada en piragua por el Ivindo hacia Kongou. A pocos kilómetros está la estación de investigación de Ipassa-Makokou, del IRET, dentro de la reserva de biosfera. Es el punto donde se decide si se entra de verdad en Ivindo o no." + _F % "Libreville",
         credit="Delrick Trevor · CC BY-SA 4.0", source=IMG_LIBREVILLE),
    dict(n=10, name="Lastourville y sus grutas", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 día",
         lat=-0.8167, lon=12.3667,
         desc="Pueblo del Ogooué a 206 m, en la N3 y en la línea del Transgabonés, rodeado por MÁS DE CUARENTA CUEVAS repartidas en unos 90 km² de selva primaria: galerías calizas con estalactitas, ríos subterráneos y colonias de murciélagos, con huellas de uso humano de hace 7.000 años en rituales. El conjunto está en la lista indicativa de la UNESCO desde 2005 como sitio mixto. Es espeleología sencilla y poco visitada, y una parada lógica entre Lopé y Franceville. Fundada en 1883 como depósito de esclavos con el nombre de Mandji." + _F % "un elefante de bosque en Loango",
         credit="Kurt Dundy · CC BY 3.0", source=IMG_LOANGO),
    dict(n=11, name="Franceville", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=-1.6333, lon=13.5833,
         desc="Tercera ciudad del país (unos 110.000 hab., a 350 m sobre el Ogooué) y terminal oriental del Transgabonés y de la Transgabonaise por carretera. Sede del CIRMF, instituto biomédico con uno de los poquísimos laboratorios de nivel de bioseguridad 4 de África, que ha sido central en la investigación del ébola en la región. Alrededor: la mina de manganeso de Moanda, los REACTORES NUCLEARES NATURALES DE OKLO —el único caso conocido en el mundo de fisión nuclear natural sostenida, hace 1.700 millones de años— y la controvertida biota francevillense, posibles formas de vida compleja de hace 2.100 millones de años. Base de acceso a las mesetas Batéké." + _F % "Libreville",
         credit="Delrick Trevor · CC BY-SA 4.0", source=IMG_LIBREVILLE),
    dict(n=12, name="Léconi · los cañones rojos de las mesetas Batéké", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1–2 días",
         lat=-1.5833, lon=14.2333,
         desc="EL PAISAJE MÁS INESPERADO DE GABÓN y el más desconocido: a poco más de una hora de Franceville, en el extremo oriental del país, la selva se acaba de golpe y empieza una sabana de arena blanca sobre la que se abren CIRCOS DE EROSIÓN DE ARENISCA ROJA Y OCRE de decenas de metros, con agujas y paredes verticales, el llamado cirque de Léconi. Cerca hay cascadas sobre el mismo altiplano. No parece África central sino un desierto pintado, y se recorre con vehículo y a pie por el borde. Es la antesala natural de las mesetas Batéké congoleñas que la ficha de Congo ya recoge en su corredor de subida." + _F % "un elefante de bosque en Loango",
         credit="Kurt Dundy · CC BY 3.0", source=IMG_LOANGO),
    dict(n=13, name="Parque Nacional de las Mesetas Batéké", cat="Naturaleza", prio="Media", dog="prohibido", time="2–3 días",
         lat=-2.2000, lon=13.9000,
         desc="2.034 km² en el sureste, creado en 2002: mosaico de sabana de altiplano, galerías de bosque y valles arenosos, un paisaje que es la firma de África central. En 2015 se documentó aquí un LEÓN MACHO, la primera prueba de la especie en Gabón en décadas, y el análisis genético lo emparentó con las poblaciones históricas de la región y del Congo. Es además escenario de uno de los programas de reintroducción de gorila de llanura occidental más ambiciosos del continente. La caza comercial para abastecer mercados de Gabón y Congo es su amenaza principal. En la lista indicativa de la UNESCO desde 2005. Coordenada aproximada. (Foto: gorila de llanura occidental, la especie que se reintroduce aquí — no es una imagen del parque.)",
         credit="Wikimedia Commons", source=IMG_GORILA),
    # ===== SUR Y COSTA =====
    dict(n=14, name="Lambaréné y el hospital de Albert Schweitzer", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="1 día",
         lat=-0.7000, lon=10.2333,
         desc="Ciudad partida por el río Ogooué y por una isla, a mitad de camino entre Libreville y el sur. Aquí Albert Schweitzer —organista, teólogo, médico y premio Nobel de la Paz— fundó en 1913 su hospital en la selva y trabajó en él hasta su muerte en 1965. El complejo sigue funcionando como hospital y conserva como museo la vivienda y el consultorio originales, con su piano y sus cuadernos. Es la parada con más peso histórico del país y la más fácil de encajar, porque está en la N1.",
         credit="David Stanley · CC BY 2.0", source=IMG_SCHWEITZER),
    dict(n=15, name="Laguna Fernan Vaz y la misión de Sainte-Anne", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1 día",
         lat=-1.5925, lon=9.4292,
         desc="Gran laguna costera al sur del delta del Ogooué, con Omboué como pueblo principal. Lleva el nombre de Fernão Vaz, el primer europeo que llegó a ella. Su pieza singular es la iglesia de la MISIÓN DE SAINTE-ANNE, de 1889, cuya estructura metálica se atribuye a Gustave Eiffel: una nave de hierro prefabricada en Francia y montada en plena selva ecuatorial. En la laguna opera además el Projet Gorille Fernan-Vaz, centro de rehabilitación de gorilas huérfanos en la isla de Evengué. Omboué es también la puerta norte de Loango." + _F % "la laguna de Mayumba",
         credit="Vincent.vaquin · CC BY-SA 3.0", source=IMG_MAYUMBA),
    dict(n=16, name="Parque Nacional de Loango", cat="Naturaleza", prio="Alta", dog="prohibido", time="3–4 días",
         lat=-1.9500, lon=9.5500,
         desc="LA IMAGEN ICÓNICA DE GABÓN Y UNO DE LOS SITIOS MÁS SINGULARES DE ÁFRICA. 1.550 km² creados en 2002 entre las lagunas Nkomi y Ndogo, con sabana, selva, manglar y más de 100 km de playa atlántica deshabitada, todo pegado: elefantes de bosque, búfalos, gorilas, leopardos e hipopótamos SALEN A LA PLAYA, y los hipopótamos nadando entre las olas —fotografiados aquí por Michael Nichols para National Geographic— dieron la vuelta al mundo. Frente a la costa, la mayor concentración y variedad de ballenas y delfines de África después de Sudáfrica (jorobadas de julio a septiembre). La laguna de Iguéla, de 220 km², es uno de los pocos sistemas lagunares típicos de África occidental protegidos. Se visita con operador autorizado, en barca y en 4x4; el acceso terrestre desde Omboué o Gamba es notoriamente difícil.",
         credit="Kurt Dundy · CC BY 3.0", source=IMG_LOANGO),
    dict(n=17, name="Port-Gentil y el cabo Lopez", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-0.7167, lon=8.7833,
         desc="Segunda ciudad del país y capital del petróleo y la madera, en la isla de Mandji. OJO CON EL MAPA: no está conectada por carretera con Libreville ni con la red nacional; solo hay una carretera que baja 93 km hacia el sur, hasta Omboué, y el asfalto se acaba en el centro urbano (el resto son pistas de arena y baches). Se llega en avión o en barco. El cabo Lopez, al norte, es el PUNTO MÁS OCCIDENTAL DE GABÓN, donde el portugués Lopo Gonçalves navegó en 1473 y donde en 1722 la Royal Navy acabó con el pirata Bartholomew Roberts." + _F % "Libreville",
         credit="Delrick Trevor · CC BY-SA 4.0", source=IMG_LIBREVILLE),
    dict(n=18, name="Parque Nacional de Moukalaba-Doudou", cat="Naturaleza", prio="Media", dog="prohibido", time="2–3 días",
         lat=-2.4333, lon=10.4167,
         desc="4.500 km² en el suroeste, entre Nyanga y Ogooué-Maritime: selva húmeda y sabanas, con una de las densidades de GORILA DE LLANURA OCCIDENTAL más altas conocidas y un programa de habituación de larga duración que permite el seguimiento a pie de un grupo. También chimpancés, elefantes de bosque y búfalos. WWF trabaja aquí desde 1996 y el parque está en la lista indicativa de la UNESCO desde 2005. Se accede desde Tchibanga; infraestructura mínima, todo por operador. Es la alternativa gabonesa a los gorilas de Odzala. (Foto: gorila de llanura occidental, la especie del parque — no es una imagen del propio parque.)",
         credit="Wikimedia Commons", source=IMG_GORILA),
    dict(n=19, name="Parque Nacional de Mayumba y las tortugas laúd", cat="Costa", prio="Alta", dog="permitido con condiciones", time="1–2 días",
         lat=-3.4167, lon=10.6500,
         desc="870 km² en el extremo suroeste y el ÚNICO PARQUE PRINCIPALMENTE MARINO DE GABÓN: protege 60 km de playa que son LAS PLAYAS DE ANIDACIÓN DE TORTUGA LAÚD MÁS IMPORTANTES DEL PLANETA, con la parte marina extendiéndose 15 km mar adentro. Temporada de puesta en torno a octubre-abril. Además: elefantes de bosque, búfalos, leopardos, gorilas, chimpancés, cocodrilos e hipopótamos en el interior, y delfines, tiburones y ballenas jorobadas en paso. La ciudad de Mayumba ocupa una lengua de arena separada del continente por la laguna de Banio. Es el último punto notable antes de la frontera con Congo-Brazzaville.",
         dog_note="La ciudad de Mayumba y la laguna de Banio no son parque: ahí el perro no tiene impedimento conocido. Dentro del Parque Nacional de Mayumba, como en el resto de parques gaboneses, no entra — y en temporada de puesta de tortugas la playa protegida está además cerrada a cualquier perturbación.",
         credit="Vincent.vaquin · CC BY-SA 3.0", source=IMG_MAYUMBA),
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
    ("Frontera · Entrada — Eboro/Abang-Minko'o, cerca de Bitam (desde Camerún)", "Frontera", 2.0833, 11.4833,
     "Zona de las tres fronteras Camerún-Gabón-Guinea Ecuatorial, al sur de Ambam y Kyé-Ossi. Carretera asfaltada desde Yaundé y fuera de las áreas de conflicto anglófonas camerunesas. AQUÍ ESTÁ EL PROBLEMA: es un puesto TERRESTRE, y el eVisa gabonés solo vale para llegadas aéreas al aeropuerto Léon Mba de Libreville. Sin visado consular previo, este paso no se cruza. Coordenada aproximada."),
    ("Frontera · Salida — Doussala/Ndendé (hacia Congo-Brazzaville)", "Frontera", -2.8333, 10.9167,
     "Paso principal del suroeste hacia Dolisie (Congo). Asfalto en el lado gabonés; confirmar el estado de la pista del lado congoleño. La ficha de Congo ya lo recoge como alternativa informativa desde Dolisie."),
    ("Frontera · Salida este — hacia Okoyo (Congo), por Léconi", "Frontera", -1.6500, 14.4000,
     "Salida oriental desde las mesetas Batéké hacia Okoyo, que está en el corredor de SUBIDA de la ficha de Congo (Djambala-Lékana-Okoyo). Encajaría muy bien sobre el papel, pero POR CONFIRMAR que el paso existe como puesto internacional habilitado y que admite vehículos particulares extranjeros. Coordenada aproximada."),
    ("Embajada de Gabón en Madrid (y consulados de Barcelona y Bilbao)", "Consular", 40.4168, -3.7038,
     "AQUÍ ES DONDE SE RESUELVE EL PROBLEMA DEL VISADO. Gabón mantiene embajada en Madrid y consulados en Barcelona y Bilbao: es la vía para obtener el visado tradicional en pasaporte que exige la entrada terrestre. Confirmar por teléfono tasas, plazos y documentación exigida a un viaje overland sin billete de avión. Coordenada: Madrid, referencia."),
    ("Embajada de España en Libreville", "Consular", 0.3936, 9.4550,
     "Immeuble Diamant, 2º piso, Bd. de la Nation (cruce con Rue Dr. Cureau), B.P. 1157, Libreville. Tel. +241 (0)11 72 12 64 · Emergencia consular: +241 (0)66 44 47 47. Abierta desde 1962; también acreditada en Santo Tomé y Príncipe (no en Congo-Brazzaville)."),
    ("Centre Hospitalier Universitaire de Libreville", "Hospital", 0.4247, 9.4142,
     "Principal hospital universitario y de referencia del país. Fuera de Libreville la infraestructura sanitaria es mínima: seguro con evacuación médica imprescindible. Coordenada urbana aproximada."),
    ("CIRMF · Franceville (referencia sanitaria del este)", "Hospital", -1.6333, 13.5833,
     "Centre International de Recherches Médicales de Franceville: instituto biomédico con laboratorio de bioseguridad nivel 4, uno de los pocos de África, central en la investigación del ébola. No es un hospital para viajeros, pero marca dónde está la capacidad técnica del este del país."),
    ("Combustible · Libreville", "Combustible", 0.4162, 9.4673,
     "Mejor oferta y calidad del país (Total, Petro Gabon); repostar a fondo antes de cualquier tramo largo."),
    ("Combustible · Lambaréné / Mouila / Ndendé (eje sur, N1)", "Combustible", -0.7000, 10.2333,
     "Estaciones formales en los núcleos del eje sur; confirmar disponibilidad real en Ndendé, última plaza antes de la frontera congoleña."),
    ("Combustible · Makokou / Franceville (eje este)", "Combustible", -1.6333, 13.5833,
     "Las dos plazas del interior. Entre Makokou e Ivindo, y en las mesetas Batéké, no hay suministro: entrar con garrafas llenas."),
    ("Agua potable y de uso general · Libreville", "Agua potable", 0.4162, 9.4673,
     "Agua embotellada sin problema en supermercados; estaciones de servicio y hoteles de Libreville, Lambaréné y Franceville permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria: tratar como restringido",
                  "Gabón no publica un procedimiento civil turístico simple y estable para drones; la Agence Nationale de l'Aviation Civile (ANAC-Gabon) exige autorización previa. Norma prudente del proyecto: no volar sin permiso escrito, y en ningún caso en los parques nacionales (Loango, Ivindo, Lopé, Pongara, Mayumba) ni cerca de instalaciones petroleras de la costa (Gamba, Port-Gentil) ni de instalaciones militares. Tras el golpe de 2023 y la transición, la sensibilidad ante cámaras y aparatos voladores es alta.")

STARLINK_CALLOUT = ("warn", "Sin confirmación de servicio activo: tratar como no disponible",
                     "Gabón figuraba entre los mercados africanos con Starlink anunciado, pero no se ha podido confirmar servicio activo en ninguna revisión del proyecto, y en esta tampoco (el mapa oficial no fue accesible desde el entorno de trabajo). Tratarlo como NO disponible y mantener SIM local (Airtel Gabon, Moov Africa) como conectividad principal, asumiendo días enteros sin cobertura en el este forestal y en las mesetas Batéké.")

DOG_MATRIX = [
    ("Todos los parques nacionales (Loango, Ivindo, Lopé, Pongara, Akanda, Mayumba, Moukalaba-Doudou, Batéké, Monts de Cristal)", "prohibido",
     "Ningún parque nacional gabonés admite mascotas, y en los de gorilas y chimpancés (Loango, Moukalaba-Doudou, Lopé, Ivindo, Batéké) el motivo es además SANITARIO Y GRAVE: riesgo de transmitir moquillo, rabia o parásitos a poblaciones de simios amenazadas — el mismo criterio que la ficha de Congo aplica en Odzala. Plan B: dejar el perro en Libreville con uno de los tres viajeros; no hay guarderías caninas documentadas fuera de la capital."),
    ("Libreville", "permitido con condiciones",
     "Es la única plaza del país con veterinarios y con alojamiento que pueda aceptar un perro. Todo trámite del animal se hace aquí. Calor y humedad muy altos todo el año."),
    ("Lambaréné, Mouila, Franceville, Makokou, Port-Gentil, Mayumba", "pendiente de verificar",
     "Sin información publicada sobre alojamiento que admita animales fuera de la capital. Asumir que habrá que negociar caso por caso con hoteles y misiones, como en el resto de África central."),
    ("Entrada del perro al país", "sin datos — agujero documental",
     "Gabón es, junto con Guinea y los dos Congos, uno de los agujeros negros del dosier canino del proyecto: no se ha localizado fuente oficial gabonesa con los requisitos de importación de animales de compañía, ni testimonio de un cruce terrestre con perro. Régimen francófono presumible (certificado veterinario internacional en francés, rabia en vigor y con menos de 12 meses, desparasitación, posible permiso previo de la Direction Générale de l'Élevage), pero NADA de eso está confirmado. Si Gabón volviera a la ruta, esta sería la primera consulta que hacer por escrito."),
]

SOURCES = [
    ("Wikipedia · Visa policy of Gabon (el eVisa «solo válido para quienes llegan por el aeropuerto Léon Mba de Libreville», tarifas)", "https://en.wikipedia.org/wiki/Visa_policy_of_Gabon"),
    ("Wikipedia · Gabon–Spain relations (embajada de Gabón en Madrid, consulados en Barcelona y Bilbao; embajada de España en Libreville desde 1962)", "https://en.wikipedia.org/wiki/Gabon%E2%80%93Spain_relations"),
    ("Wikipedia · List of diplomatic missions of Gabon", "https://en.wikipedia.org/wiki/List_of_diplomatic_missions_of_Gabon"),
    ("Wikipedia · Gabon (89,3% de superficie forestal, 13 parques nacionales, ~10% del territorio)", "https://en.wikipedia.org/wiki/Gabon"),
    ("Wikipedia · Transport in Gabon (7.670 km de carreteras, solo ~629 km asfaltados; N1-N7)", "https://en.wikipedia.org/wiki/Transport_in_Gabon"),
    ("Wikipedia · Trans-Gabon Railway (648 km, Owendo-Franceville, 23 estaciones, trenes nocturnos)", "https://en.wikipedia.org/wiki/Trans-Gabon_Railway"),
    ("Wikipedia · Loango National Park (1.550 km², hipopótamos surfeando, ballenas)", "https://en.wikipedia.org/wiki/Loango_National_Park"),
    ("Wikipedia · Ivindo National Park (UNESCO 2021, Kongou y Mingouli, Langoué Baï)", "https://en.wikipedia.org/wiki/Ivindo_National_Park"),
    ("Wikipedia · Kongou Falls (3,2 km de ancho, 56 m, 900 m³/s, presa cancelada)", "https://en.wikipedia.org/wiki/Kongou_Falls"),
    ("Wikipedia · Lopé National Park (UNESCO mixto 2007, mosaico bosque-sabana, 1.600 petroglifos)", "https://en.wikipedia.org/wiki/Lop%C3%A9_National_Park"),
    ("Wikipedia · Mayumba National Park (870 km², 60 km de playas de laúd, único parque marino)", "https://en.wikipedia.org/wiki/Mayumba_National_Park"),
    ("Wikipedia · Pongara National Park (929 km², laúd, 10.000 limícolas, Ramsar 2007)", "https://en.wikipedia.org/wiki/Pongara_National_Park"),
    ("Wikipedia · Akanda National Park (540 km², 25% del manglar protegido de África con Pongara)", "https://en.wikipedia.org/wiki/Akanda_National_Park"),
    ("Wikipedia · Batéké Plateau National Park (2.034 km², león de 2015, reintroducción de gorilas)", "https://en.wikipedia.org/wiki/Bat%C3%A9k%C3%A9_Plateau_National_Park"),
    ("Wikipedia · Moukalaba-Doudou National Park (4.500 km², gorilas, WWF desde 1996)", "https://en.wikipedia.org/wiki/Moukalaba-Doudou_National_Park"),
    ("Wikipedia · Lastoursville (más de 40 cuevas en 90 km², lista indicativa UNESCO)", "https://en.wikipedia.org/wiki/Lastoursville"),
    ("Wikipedia · Fernan Vaz Lagoon (misión de Sainte-Anne de 1889 atribuida a Eiffel, Projet Gorille)", "https://en.wikipedia.org/wiki/Fernan_Vaz_Lagoon"),
    ("Wikipedia · Port-Gentil (isla de Mandji, carretera de 93 km a Omboué, cabo Lopez)", "https://en.wikipedia.org/wiki/Port-Gentil"),
    ("Wikipedia · Franceville (terminal del Transgabonés, CIRMF y su laboratorio BSL-4, Oklo)", "https://en.wikipedia.org/wiki/Franceville"),
    ("Wikipedia · Cocobeach (estuario del Muni, frontera con Guinea Ecuatorial, 3.126 mm de lluvia)", "https://en.wikipedia.org/wiki/Cocobeach"),
    ("Amazing Gabon · formalidades de entrada (web turística oficial)", "https://www.amazinggabon.com/en/advice-and-formalities/"),
    ("Take Your Backpack · guía del Parque Nacional de Loango (2026)", "https://www.takeyourbackpack.com/backpacking-in-gabon/visit-loango-national-park/"),
    ("Embajada de España en Libreville · contacto", "https://www.embassypages.com/spain-embassy-libreville-gabon"),
    ("BNCR · Carte Rose CEMAC, portal oficial", "https://bncr.cm/en/"),
    ("UNESCO · ecosistema y paisaje cultural de Lopé-Okanda", "https://whc.unesco.org/en/list/1147/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Corredor oeste (el "clásico"): Camerún -> Bitam -> Oyem -> Libreville -> N1 sur -> Congo por Doussala
CORRIDOR = [(2.0833, 11.4833), (1.5996, 11.5793), (0.7833, 11.5500), (0.4162, 9.4673),
            (-0.1833, 10.7500), (-0.7000, 10.2333), (-1.8667, 11.0556), (-2.4000, 11.3667),
            (-2.8333, 10.9167)]

# Corredor este (selva y mesetas): Camerún -> Oyem -> Makokou/Ivindo -> Lopé -> Lastourville -> Franceville -> Léconi -> Congo
CORRIDOR_ALT = [(2.0833, 11.4833), (1.5996, 11.5793), (0.7833, 11.5500), (0.5667, 12.8667),
                (0.2907, 12.5891), (-0.0833, 11.9333), (-0.2000, 11.5833), (-0.8167, 12.3667),
                (-1.5667, 13.2000), (-1.6333, 13.5833), (-1.5833, 14.2333), (-1.6500, 14.4000)]

EXPERIENCIAS = [
    "Aviso previo de método: en esta revisión NO se pudo abrir iOverlander ni Tracks4Africa desde el entorno de trabajo (dominios bloqueados por el proxy). Lo que sigue recoge lo que aparece de forma coincidente en relatos publicados de viajeros por Gabón y África central, y debe reverificarse antes de depender de ello. Gabón es, además, uno de los países menos documentados del continente en el mundo overland: hay muy pocos relatos y casi ninguno reciente.",
    "El visado es LA historia de Gabón entre viajeros por tierra. Los relatos de quienes han cruzado fronteras terrestres coinciden en que hay que llegar con el visado ya en el pasaporte, sacado en un consulado, y en que el eVisa se anuncia como solución pero está pensado para el aeropuerto de Libreville. Es exactamente el motivo por el que este proyecto lo ha dejado fuera.",
    "Carreteras: el dato que más sorprende a quien llega es que de unos 7.670 km de red apenas ~629 km están asfaltados. Los ejes principales (Libreville-Lambaréné-Mouila-Ndendé y la subida a Oyem) están en buena parte pavimentados y son cómodos; todo lo demás es laterita, que en seco vuela y en la estación de lluvias se convierte en barro rojo profundo con rodadas de camión maderero. La proporción de pista es la razón de fondo para llevar 4x4 aquí.",
    "Loango tiene fama de ser el parque más espectacular y más difícil de organizar de África central: los relatos hablan de acceso por avioneta o por pistas largas desde Omboué o Gamba, de que todo pasa por el operador de la concesión y de precios de nivel europeo. Casi nadie llega con vehículo propio.",
    "El tren Transgabonés aparece en casi todos los diarios de viaje como la manera lógica de ver el interior: nocturno, con coche restaurante, y con parada en Lopé, que es el único parque nacional del país al que se puede llegar sin operador ni avioneta. Los retrasos de varias horas son la norma.",
    "Los controles de gendarmería en carretera son frecuentes y los relatos recomiendan llevar los papeles del vehículo y el pasaporte SIEMPRE a mano, copias por triplicado y paciencia. Tras el golpe de 2023, la recomendación repetida es no fotografiar nada oficial, militar ni portuario.",
    "Precios: Gabón tiene fama de ser uno de los países más caros de África continental, consecuencia del petróleo y de que casi todo es importado. Alojamiento, comida y combustible están muy por encima de los países vecinos.",
    "Ébola: el CIRMF de Franceville existe porque la región ha tenido brotes reales. Como en la ficha de Congo, la recomendación de los viajeros es comprobar el estado epidemiológico antes de entrar, porque un brote activo endurece controles y cierra parques.",
    "Perro: no se ha localizado ningún relato de un viajero que haya entrado a Gabón por tierra con un perro. Es un vacío total, no una prohibición — pero para este proyecto significa que habría que abrir el camino uno mismo, escribiendo a la administración gabonesa.",
]

HISTORIA_RESUMEN = ("Gabón es un país pequeño y extraordinariamente boscoso (cerca del 89% de su territorio es selva) que la abundancia de petróleo convirtió en uno de los de mayor renta per cápita de África continental, gobernado sin embargo durante 56 años por una sola familia, los Bongo, "
                     "hasta que un golpe de Estado militar puso fin a esa dinastía en agosto de 2023, tras una disputada reelección del presidente Ali Bongo; la transición militar celebró elecciones en abril de 2025.")

HISTORIA_SECCIONES = [
    ("Pueblos bantúes, el bwiti y la selva",
     "El territorio fue poblado por sucesivas migraciones de pueblos bantúes —fang, myene, punu, teke, entre otros— organizados en pequeños reinos y jefaturas forestales, con tradiciones espirituales como el bwiti, un culto iniciático centrado en la raíz de iboga que sigue practicándose hoy y es objeto de interés internacional. "
     "En el interior, el mosaico de bosque y sabana de Lopé-Okanda conserva rastros de ocupación humana de casi 400.000 años y más de 1.600 petroglifos: es uno de los registros continuos más largos de África."),
    ("Libreville, colonia de esclavos liberados y colonia francesa",
     "Libreville («ciudad libre») fue fundada en 1849 por Francia como asentamiento de esclavos liberados de un barco negrero capturado, un origen paralelo al de Freetown en Sierra Leona; el territorio se convirtió después en colonia francesa de plena explotación maderera (okoumé) dentro del África Ecuatorial Francesa. "
     "Lambaréné, sobre el Ogooué, adquirió fama mundial cuando Albert Schweitzer fundó allí su hospital en 1913."),
    ("Independencia y la era Bongo",
     "Gabón se independizó en 1960. Tras un breve periodo bajo Léon M'ba, Omar Bongo asumió la presidencia en 1967 y gobernó hasta su muerte en 2009, instaurando un régimen de partido único (después multipartidista de fachada) sostenido por la riqueza petrolera y una relación muy estrecha con Francia; a su muerte, el poder pasó a su hijo Ali Bongo. "
     "Fue también bajo Omar Bongo cuando, en 2002, se crearon de golpe los TRECE PARQUES NACIONALES que hoy cubren alrededor del 10-11% del territorio, la decisión que convirtió a Gabón en referencia conservacionista de África central."),
    ("Situación actual: el golpe de 2023, la transición y el turismo de naturaleza",
     "En agosto de 2023, horas después de que Ali Bongo fuera proclamado vencedor de una reelección ampliamente cuestionada, un grupo de oficiales militares dio un golpe de Estado y puso fin a 56 años de gobierno de la familia Bongo, instaurando una transición que celebró elecciones en abril de 2025. "
     "Gabón sigue siendo, pese a la riqueza petrolera, un país con fuertes desigualdades y con gran parte de su selva ecuatorial intacta, un activo creciente para el turismo de naturaleza — y también un país caro, poco recorrido por viajeros independientes y con una política de visados que penaliza precisamente la llegada por tierra."),
]

HISTORIA_FUENTES = [
    ("BBC News · Gabon country profile", "https://www.bbc.com/news/world-africa-13376333"),
    ("Encyclopaedia Britannica · Gabon, History", "https://www.britannica.com/place/Gabon/History"),
    ("Wikipedia · Gabon (superficie forestal, parques nacionales, transición 2023-2025)", "https://en.wikipedia.org/wiki/Gabon"),
]

SPEC = dict(
    slug="gabon", name="Gabón", revision="12 sep 2026",
    sub="EXCLUIDO de la ruta fija · alternativa informativa · el problema es el visado, no el país",
    chips=[
        ("ESTATUS", "EXCLUIDO de la ruta fija — ficha informativa, NO se hará"),
        ("MOTIVO", "El eVisa gabonés solo vale para llegadas AÉREAS al aeropuerto Léon Mba de Libreville"),
        ("QUÉ HARÍA FALTA", "Visado tradicional en consulado: embajada en Madrid o consulado en BARCELONA"),
        ("DÓNDE ENCAJABA", "Entre Camerún y Congo, en la subida («para la subida si hay tiempo»)"),
        ("PDIs", "19 puntos documentados, de Cocobeach a Mayumba"),
        ("LO ÚNICO", "Loango: elefantes, búfalos e hipopótamos en la playa atlántica"),
        ("NATURALEZA", "13 parques nacionales · ~10-11% del territorio · 89% de selva"),
        ("4x4", "De 7.670 km de carreteras, solo ~629 km asfaltados"),
        ("PERRO", "Agujero documental total: ni fuente oficial ni un solo testimonio de cruce terrestre"),
        ("COMUNICACIONES", "Starlink sin confirmar · SIM local como única base"),
    ],
    center=[-0.6, 11.5], zoom=6,
    hero_img=W + "Gabon%20Loango%20National%20Park%20Elephant%20with%20offspring.jpeg?width=900",
    hero_credit="Elefanta de bosque con su cría, Parque Nacional de Loango · Kurt Dundy · CC BY 3.0",
    notice="Documento informativo de un país EXCLUIDO de la ruta fija. No hay que tramitar nada. Si algún día se reconsiderara, revalidar TODO (empezando por el visado) 60-90 días antes.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Corredor oeste (capital y costa) — hipotético",
    corridor_alt_label="Corredor este (Lopé, Ivindo y Batéké) — hipotético",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("<strong>Gabón está fuera de la ruta.</strong> Y no por falta de interés —es el país más selvático de África central, con "
                   "<strong>trece parques nacionales</strong> que cubren en torno al 10-11% de su territorio y cerca del <strong>89% de superficie forestal</strong>—, "
                   "sino por un detalle administrativo que lo rompe todo: <strong>el eVisa gabonés solo es válido para quien llega en avión al aeropuerto "
                   "Léon Mba de Libreville</strong>. Por tierra hay que entrar con visado tradicional sacado en un consulado, con antelación y con el pasaporte físico. "
                   "Esta ficha se mantiene completa por dos razones: porque la información vale (Loango, Ivindo, Lopé y las mesetas Batéké son de primer nivel mundial) "
                   "y porque deja escrito <strong>exactamente qué haría falta para que Gabón volviera a entrar</strong>, si alguna vez cambiara la decisión o la norma."),
    decision=("<strong>ESTATUS: EXCLUIDO DE LA RUTA FIJA. Esta ficha es informativa; Gabón NO se hará.</strong> "
              "La decisión del dueño del proyecto fue literal: «deja las fichas de Liberia y Gabón como alternativas por tener su información pero no lo haremos». "
              "Antes se había contemplado como opción «para la subida si hay tiempo», entre Camerún y Congo.<br><br>"
              "<strong>El motivo concreto, y ya verificado: el visado.</strong> El sistema gabonés de visado electrónico está montado para el avión. La propia norma lo dice: "
              "el e-Visa <em>«se emite 72 horas después de la solicitud y es válido únicamente para quienes llegan por el aeropuerto internacional Léon Mba de Libreville»</em>. "
              "Además hay visado a la llegada para más de cuarenta nacionalidades y exención para varios países del G20 y de la CEMAC, pero nada de eso resuelve el caso de "
              "un pasaporte español que se presenta en un puesto TERRESTRE del norte o del sur. Con dos 4x4 entrando por Bitam desde Camerún, el eVisa no sirve: hay que llegar "
              "con el visado ya estampado.<br><br>"
              "<strong>QUÉ HARÍA FALTA PARA QUE GABÓN VOLVIERA A ENTRAR.</strong> Una sola cosa, y por suerte está cerca de casa: "
              "<strong>tramitar el visado tradicional en la representación gabonesa en España</strong>. Gabón mantiene <strong>embajada en Madrid y consulados en Barcelona y Bilbao</strong> "
              "— es decir, el trámite se puede hacer <em>en la propia ciudad de salida del viaje</em>, sin depender de París como pasa con Congo-Brazzaville. "
              "Las tarifas publicadas del sistema electrónico sirven de referencia de precio (<strong>70 € el visado de 1-3 meses de entrada única</strong> y "
              "<strong>185 € el de 6 meses y entradas múltiples</strong>, más unos 15 € de gestión); <strong>las tasas, los plazos y la documentación exacta del visado consular "
              "hay que confirmarlos por teléfono con el consulado de Barcelona</strong>, y la pregunta clave que hay que hacerles es doble: "
              "<em>(1) ¿el visado que emiten es válido para entrada por puesto terrestre, y conviene hacerlo constar?</em> y "
              "<em>(2) ¿qué aceptan como justificante de entrada y salida en un viaje por carretera, sin billete de avión?</em> — el mismo escollo que ya apareció con el Congo.<br><br>"
              "<strong>Qué nos perdemos, para que la decisión sea consciente:</strong> Loango (los elefantes y los hipopótamos en la playa, la imagen icónica de Gabón), "
              "las cataratas de Kongou en Ivindo (3,2 km de frente y 900 m³/s en plena selva, Patrimonio Mundial desde 2021), el mosaico de bosque y sabana de Lopé (UNESCO 2007) "
              "con sus mandriles y sus 1.600 petroglifos, los cañones rojos de Léconi y la mayor colonia de anidación de tortuga laúd del planeta en Mayumba. "
              "Es mucho. Pero también es un país caro, con solo ~629 km de asfalto en toda su red, sin apenas infraestructura para viajeros independientes, con acceso a "
              "Loango prácticamente monopolizado por operadores, y —dato no menor para nosotros— con <strong>cero documentación sobre entrar con un perro</strong>. "
              "La conclusión razonable es que, con un visado que hay que pelear y un calendario de subida ya apretado, el coste/beneficio no sale. "
              "Si sale, la decisión se toma en Barcelona, meses antes de salir, y no en la frontera de Bitam."),
    facts=[
        ("Estatus en el proyecto", "EXCLUIDO de la ruta fija. Ficha informativa. Decisión del dueño: «por tener su información pero no lo haremos»."),
        ("Motivo de la exclusión", "El eVisa gabonés es válido ÚNICAMENTE para llegadas aéreas por el aeropuerto Léon Mba de Libreville; la entrada terrestre exige visado consular previo."),
        ("Qué lo desbloquearía", "Visado tradicional en la embajada de Gabón en Madrid o en el consulado de BARCELONA (también hay consulado en Bilbao). Referencia de tarifa del sistema electrónico: 70 € (1-3 meses, entrada única) y 185 € (6 meses, entradas múltiples), + ~15 € de gestión; tasas y plazos consulares POR CONFIRMAR."),
        ("Dónde encajaba", "Entre Camerún y Congo, en el corredor de SUBIDA. Entrada por Bitam/Eboro desde Camerún; salida por Doussala/Ndendé hacia Dolisie (Congo) o, por el este, hacia Okoyo."),
        ("Seguro", "Zona CEMAC, la misma que Camerún, Congo, Chad, RCA y Guinea Ecuatorial: la Carte Rose ya valdría, sin trámite nuevo."),
        ("Carreteras", "~7.670 km de red y solo ~629 km asfaltados. Siete rutas nacionales (N1-N7); la costa remota y el este a menudo no están conectados."),
        ("Ferrocarril", "Transgabonés: 648 km Owendo-Franceville, 23 estaciones, trenes nocturnos ~4 días por semana. Es la vía realista para llegar a Lopé sin operador."),
        ("Naturaleza", "13 parques nacionales creados de golpe en 2002, ~10-11% del territorio, y cerca del 89% de superficie forestal. Tres inscripciones UNESCO o candidaturas: Lopé (2007), Ivindo (2021) y varias en lista indicativa."),
        ("Seguridad", "Estable en el corredor, con transición política tras el golpe de agosto de 2023 y elecciones en abril de 2025. Precaución normal; sensibilidad alta ante cámaras y drones."),
        ("Perro", "AGUJERO DOCUMENTAL. Ni fuente oficial gabonesa localizada ni un solo testimonio de cruce terrestre con animal. Sería la primera consulta a resolver."),
        ("Comunicaciones", "Starlink sin confirmar activo. SIM local (Airtel Gabon, Moov Africa) como única base; días sin cobertura en el este forestal."),
    ],
    alerts=[
        "ESTATUS: Gabón NO está en la ruta. Esta ficha es informativa y no hay que tramitar absolutamente nada.",
        "EL VISADO ES EL PROBLEMA Y ES CONCRETO: el e-Visa gabonés «es válido únicamente para quienes llegan por el aeropuerto internacional Léon Mba de Libreville». Un pasaporte español que se presente en un puesto terrestre sin visado consular previo NO entra. No es un rumor de foro: es la propia definición del sistema.",
        "La solución existe y está en casa: embajada de Gabón en Madrid y consulados en Barcelona y Bilbao. Si alguna vez se reconsidera, el trámite se hace en España ANTES de salir, no en ruta — y conviene pedir entradas múltiples y validez larga, porque el calendario overland se mueve.",
        "Acceso a Loango: solo con operador autorizado (avioneta o pistas largas desde Omboué o Gamba), con precios de nivel europeo. No intentar el acceso por cuenta propia sin confirmar antes el estado de la pista y la reserva.",
        "Acceso a Kongou (Ivindo): no hay carretera. Se llega desde Makokou combinando pista y piragua por el río Ivindo, con guía. Es una expedición de varios días, no una excursión.",
        "Solo ~629 km de los ~7.670 km de red están asfaltados: fuera de los ejes principales todo es laterita, que en la estación de lluvias se convierte en barro rojo profundo con rodadas de camión maderero. Autonomía de combustible y neumáticos de repuesto.",
        "Port-Gentil NO está conectada por carretera con Libreville ni con la red nacional: solo tiene una carretera de 93 km hacia el sur, a Omboué. Se llega en avión o en barco. Es un error de planificación muy fácil de cometer mirando un mapa.",
        "Dron: sin procedimiento civil turístico claro — tratar como restringido y no volar sin autorización previa por escrito; en ningún caso en parques nacionales ni cerca de instalaciones petroleras (Gamba, Port-Gentil) o militares.",
        "Perro: agujero documental completo. Régimen francófono presumible, pero sin fuente oficial ni testimonio. Habría que escribir a la administración gabonesa y no contar con resolverlo en la frontera.",
        "Ébola: la región ha tenido brotes reales (el CIRMF de Franceville existe por eso). Comprobar el estado epidemiológico antes de entrar: un brote activo endurece controles y puede cerrar parques.",
    ],
    ruta_intro=("Recorrido HIPOTÉTICO, documentado para que la información exista, no porque vaya a hacerse. Gabón se atravesaría de norte a sur entre Camerún y Congo, "
                "y admite dos corredores muy distintos: el <strong>oeste</strong>, por la capital y el eje asfaltado de la N1 (rápido, con Loango y Lambaréné como paradas), "
                "y el <strong>este</strong>, por la selva de Ivindo y Lopé y las mesetas Batéké (mucho más lento y mucho más interesante, y con salida natural hacia Okoyo, "
                "que ya está en el corredor de subida de la ficha de Congo). Etapas sobre una media de <strong>250 km/día</strong>, que en el este no se cumple: "
                "sobre laterita el ritmo real baja a 100-150 km/día."),
    route_headers=("Etapa", "Recorrido (hipotético)", "Distancia y días aprox."),
    route_rows=[
        ("O1 · Entrada y norte", "Bitam/Eboro (frontera) → Oyem → Mitzic", "~200 km · 1-2 días (el cruce se lleva el día)"),
        ("O2 · A la capital", "Mitzic → Ndjolé → Kougouleu → Libreville", "~350 km · 1-2 días"),
        ("O3 · Estuario y manglar", "Libreville → Akanda y Pongara (en barca) → Libreville", "sin vehículo · 2-3 días"),
        ("O4 · Monts de Cristal (desvío)", "Libreville → Kinguélé / Tchimbélé → Libreville", "~250 km ida y vuelta · 2 días"),
        ("O5 · Schweitzer", "Libreville → Lambaréné", "~250 km · 1-2 días"),
        ("O6 · La laguna y el Eiffel de la selva", "Lambaréné → Omboué (Fernan Vaz, Sainte-Anne)", "~200 km + barca · 2 días"),
        ("O7 · LOANGO", "Omboué → Loango (con operador) → Omboué", "solo con operador · 3-4 días"),
        ("O8 · Bajada al sur y salida", "Omboué → Mouila → Tchibanga → Mayumba → Ndendé → Doussala (Congo)", "~700 km · 4-5 días"),
        ("E1 · Entrada y giro al este", "Bitam/Eboro → Oyem → Mitzic → Makokou", "~450 km · 2-3 días"),
        ("E2 · IVINDO Y KONGOU", "Makokou → Ivindo (pista + piragua) → Kongou / Langoué Baï → Makokou", "expedición · 3-5 días"),
        ("E3 · Bosque y sabana", "Makokou → Booué → Lopé (UNESCO)", "~300 km · 2-3 días en el parque"),
        ("E4 · Las cuevas del Ogooué", "Lopé → Lastourville (grutas)", "~200 km · 1-2 días"),
        ("E5 · Manganeso y ciencia", "Lastourville → Moanda → Franceville", "~150 km · 1-2 días"),
        ("E6 · LOS CAÑONES ROJOS", "Franceville → Léconi (cirque, cascadas) → mesetas Batéké", "~100 km · 2-3 días"),
        ("E7 · Salida este (POR CONFIRMAR)", "Léconi → frontera hacia Okoyo (Congo)", "~100 km · 1 día, si el paso existe y admite vehículos extranjeros"),
        ("Alternativa sin vehículo", "Owendo → tren Transgabonés → Lopé / Booué / Franceville", "648 km · noche a bordo, ~4 salidas semanales"),
    ],
    offroad=[
        "Contexto que lo explica todo: de unos 7.670 km de red vial, solo unos 629 km están asfaltados. En Gabón la pista no es la excepción, es la norma, y las zonas remotas de la costa y del este directamente no están conectadas a la red nacional.",
        "Acceso a Loango: pistas de arena y laterita desde Gamba o desde Omboué, transitables solo en temporada seca y en la práctica siempre con guía o con el operador del parque. Es el acceso NOTORIAMENTE difícil del país; la mayoría de visitantes acaba llegando en avioneta. Confirmar antes de intentarlo con vehículo propio.",
        "Pistas forestales del este (Makokou, Ivindo, Belinga): laterita de concesión maderera, con tráfico de camiones de troncos, barro permanente en lluvias y puentes de madera. A Kongou no llega ninguna carretera: el último tramo es piragua por el Ivindo.",
        "Mesetas Batéké y Léconi: terreno completamente distinto, arena blanca y sabana abierta sobre altiplano, con los circos de erosión al borde. Arena profunda en algunos tramos: bajar presiones. Es la conducción más bonita y menos conocida del país.",
        "Eje N1 sur (Libreville-Lambaréné-Mouila-Ndendé): en buena parte asfaltado y es el tramo cómodo del país; es también el que menos se parece a Gabón.",
        "Tchibanga → Mayumba y accesos a Moukalaba-Doudou: pistas de arena y laterita hacia la costa suroeste, con tramos que pueden depender de la marea y de las lluvias. Confirmar con la oficina del parque antes de entrar.",
        "Port-Gentil: aviso de mapa, no de conducción — la isla de Mandji no está unida por carretera a la red nacional. Solo hay 93 km de carretera hacia el sur, hasta Omboué, y el asfalto se acaba en el centro urbano.",
    ],
    senderismo=[
        "LOPÉ es el único parque nacional gabonés donde caminar resulta razonablemente accesible, y precisamente porque tiene sabana: en el mosaico de bosque y pradera se pueden hacer caminatas guiadas con visibilidad, algo imposible en selva cerrada. Rutas a los afloramientos con PETROGLIFOS (hay más de 1.600 en el conjunto), a los miradores sobre el Ogooué y a los sectores de sabana donde salen mandriles, elefantes de bosque y búfalos. La estación de Mikongo, de la Zoological Society of London, organiza seguimientos a pie de primates.",
        "IVINDO Y KONGOU: la caminata es el único modo de llegar. Desde el punto donde acaba la pista, tramos a pie por selva primaria y navegación en piragua por el Ivindo hasta el frente de las cataratas. Terreno resbaladizo, humedad extrema, sanguijuelas y sin sendero marcado: guía obligatorio, botas altas y varios días. La recompensa es una de las cascadas más potentes del mundo sin nadie alrededor.",
        "Langoué Baï (Ivindo): caminata de aproximación por el bosque hasta la plataforma de observación sobre el claro pantanoso, donde salen al descubierto elefantes de bosque, gorilas y sitatungas. Es la observación de fauna más pura del país, equivalente a los bais de Odzala en el Congo.",
        "Moukalaba-Doudou: seguimiento a pie de un grupo de gorilas de llanura occidental habituado tras años de trabajo. Mismo formato que en Odzala: grupos pequeños, mascarilla, distancia mínima y tiempo de observación limitado. Todo por operador.",
        "Léconi y las mesetas Batéké: caminatas libres por sabana abierta y por el borde de los circos de erosión, sin infraestructura ni señalización pero también sin dificultad técnica. Sin sombra: agua y sombrero. Es donde más fácil resulta andar por libre en todo Gabón.",
        "Monts de Cristal: senderos cortos hacia las cascadas y presas de Kinguélé y Tchimbélé, en un bosque que es uno de los puntos de mayor diversidad vegetal de África (orquídeas y begonias). Accesos por confirmar.",
        "Grutas de Lastourville: recorrido espeleológico sencillo por galerías calizas con estalactitas y ríos subterráneos, en un conjunto de más de cuarenta cuevas repartidas por 90 km² de selva primaria. Frontal, casco y guía local.",
        "Pongara y Pointe Denis: paseos largos por playa abierta y manglar a menos de una hora en barca de Libreville, con puesta de tortugas laúd en temporada. La caminata más fácil del país y la única que se puede hacer sin expedición.",
    ],
    acampada=[
        "Libreville: alojamientos con parking vigilado. Es la única plaza del país con oferta real y el único sitio donde podría quedarse el perro.",
        "Loango: solo campamentos del operador autorizado; no hay acampada libre dentro del parque.",
        "Lopé: pueblo con alojamiento junto a la estación del tren, la opción más accesible de todos los parques gaboneses.",
        "Lambaréné, Mouila, Tchibanga y Mayumba: pequeños hoteles con aparcamiento; en el interior, la fórmula que funciona en África central es la misión católica con recinto cerrado y el auberge con patio.",
        "Este forestal (Makokou, Lastourville, Franceville): auberges sencillos; fuera de los pueblos, vivaqueo avisando siempre al jefe del poblado.",
        "Mesetas Batéké y Léconi: sabana abierta, el mejor terreno del país para acampar con los vehículos, pero sin ningún servicio: autosuficiencia completa.",
        "Aviso general: Gabón es caro. El alojamiento y la comida están muy por encima de los países vecinos, y los lodges de los parques trabajan con tarifas de nivel europeo.",
    ],
    visado=[
        "ESTE ES EL PUNTO QUE EXCLUYE A GABÓN DE LA RUTA. El visado electrónico gabonés se emite 72 horas después de la solicitud y ES VÁLIDO ÚNICAMENTE PARA QUIENES LLEGAN POR EL AEROPUERTO INTERNACIONAL LÉON MBA DE LIBREVILLE. No sirve para un puesto fronterizo terrestre.",
        "Tarifas publicadas del sistema electrónico, útiles como referencia de precio: 70 € (o 45.000 XAF) el visado de 1 a 3 meses de entrada única, y 185 € (o 120.000 XAF) el de 6 meses con entradas múltiples, más unos 15 € de gastos de tramitación.",
        "Existen además exención de visado para varios países (CEMAC, Marruecos, Mauricio y algunos del G20, de 30 a 90 días) y visado a la llegada para más de cuarenta nacionalidades, pero ninguna de esas vías resuelve el caso de un pasaporte español que se presenta por carretera.",
        "LA VÍA QUE SÍ FUNCIONARÍA: visado tradicional estampado en el pasaporte, solicitado en la EMBAJADA DE GABÓN EN MADRID o en sus CONSULADOS DE BARCELONA Y BILBAO. Es una ventaja frente a Congo-Brazzaville, que obliga a enviar el pasaporte a París: aquí el trámite se puede hacer en la propia ciudad de salida del viaje.",
        "POR CONFIRMAR con el consulado (llamada de cinco minutos, si alguna vez se reconsidera): tasa exacta del visado consular, plazo real de tramitación, documentación exigida, si el visado emitido sirve para entrada por puesto terrestre y si conviene hacerlo constar, y qué aceptan como justificante de entrada y salida en un viaje por carretera sin billete de avión. Pedir validez larga y entradas múltiples.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
    ],
    fronteras_rows=[
        ("Entrada (hipotética)", "Bitam / Eboro (desde Camerún, zona de las tres fronteras)",
         "Carretera asfaltada desde Yaundé y fuera de las áreas de conflicto anglófonas. PROBLEMA: es un puesto terrestre y el eVisa no vale aquí. Sin visado consular previo, no se cruza."),
        ("Salida (hipotética, oeste)", "Doussala / Ndendé (hacia Congo-Brazzaville, Dolisie)",
         "Paso principal del suroeste. Asfalto en el lado gabonés; confirmar el lado congoleño. La ficha de Congo ya lo recoge como alternativa informativa desde Dolisie."),
        ("Salida (hipotética, este)", "Hacia Okoyo (Congo), desde Léconi / mesetas Batéké",
         "Encajaría perfectamente con el corredor de SUBIDA de la ficha de Congo (Djambala-Lékana-Okoyo). POR CONFIRMAR que existe como puesto internacional habilitado y que admite vehículos particulares extranjeros."),
        ("Frontera no utilizable", "Cocobeach / Cogo (Guinea Ecuatorial, por el río Muni)",
         "Barcaza sobre el estuario. Guinea Ecuatorial no está en la ruta y su régimen de visados es aún más restrictivo: informativo solamente."),
        ("El trámite que lo condiciona todo", "Consulado de Gabón en Barcelona (o embajada en Madrid)",
         "No es una frontera, pero es donde se decide si se puede cruzar cualquiera de las anteriores. Visado tradicional previo, meses antes de salir."),
    ],
    vehiculos=[
        "CPD con todos los pares de sellos en regla.",
        "Carte Rose CEMAC como seguro de responsabilidad civil regional: Gabón está en la misma zona que Camerún y Congo, así que no haría falta seguro nuevo.",
        "Carnet de conducir internacional obligatorio; controles de gendarmería frecuentes en carretera, con papeles siempre a mano y copias por triplicado.",
        "Autonomía: entre Makokou e Ivindo, y en las mesetas Batéké, no hay suministro. Garrafas llenas y embudo con filtro; calidad de gasóleo irregular fuera de las ciudades.",
        "Neumáticos: con solo ~629 km asfaltados de toda la red, el desgaste y los pinchazos en laterita son el problema práctico número uno. Dos ruedas de repuesto por vehículo.",
        "Nota para carga: toda mercancía que entra en Gabón requiere BIETC (nota electrónica de seguimiento de carga) del consejo de cargadores para el despacho aduanero — relevante solo si se enviara material por barco, no para el vehículo propio.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa por escrito a la ANAC-Gabon antes de intentar siquiera introducir el dron en el país.",
        "No volar en ningún parque nacional (Loango, Ivindo, Lopé, Pongara, Akanda, Mayumba, Batéké, Moukalaba-Doudou) ni cerca de instalaciones petroleras de la costa (Gamba, Port-Gentil).",
        "No fotografiar ni volar sobre instalaciones oficiales, militares o portuarias: tras el golpe de 2023 y la transición, la sensibilidad es alta.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Sin confirmación de servicio activo en ninguna revisión del proyecto: tratar como NO disponible y revisar el mapa oficial si alguna vez se reconsidera el país.",
        "SIM local (Airtel Gabon, Moov Africa) como conectividad principal, con cobertura razonable en Libreville y el eje sur y prácticamente nula en el este forestal.",
        "Contar con varios días seguidos sin cobertura útil en Ivindo y en las mesetas Batéké.",
    ],
    perro_intro=[
        "AGUJERO DOCUMENTAL COMPLETO, y conviene decirlo sin adornos: no se ha localizado ninguna fuente oficial gabonesa con los requisitos de importación de animales de compañía, ni un solo testimonio de un viajero que haya entrado por tierra con un perro. Gabón está, en el dosier canino del proyecto, al nivel de Guinea y de los dos Congos.",
        "Lo presumible por régimen francófono (NO confirmado): certificado veterinario internacional en francés, vacuna antirrábica en vigor y con menos de 12 meses, desparasitación reciente y posible permiso de importación previo de la Direction Générale de l'Élevage. Más los requisitos comunes del proyecto: microchip, pasaporte UE y titulación serológica ya obtenida.",
        "Si Gabón volviera a la ruta, la consulta escrita a la administración veterinaria gabonesa sería el PRIMER trámite, antes incluso que el visado, por el plazo de respuesta.",
        "Ningún parque nacional admite mascotas, y en los de gorilas y chimpancés el motivo es sanitario y serio: riesgo de transmitir moquillo, rabia o parásitos a poblaciones de simios amenazadas. Mismo criterio que en Odzala.",
        "Plan B realista: el perro se quedaría en Libreville con uno de los tres viajeros. No hay guarderías caninas documentadas fuera de la capital, y fuera de ella no hay ni veterinarios de referencia.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada y comprobado en frontera.",
        "Paludismo intenso en todo el territorio y todo el año, por el clima ecuatorial: profilaxis a valorar con Sanidad Exterior, más mosquitera y repelente sin fallos.",
        "Ébola: la región ha tenido brotes reales y el CIRMF de Franceville, con laboratorio de bioseguridad nivel 4, es el centro de referencia de su investigación. Comprobar el estado epidemiológico (OMS, ECDC) antes de entrar: un brote activo endurecería los controles y podría cerrar parques.",
        "Tripanosomiasis (mosca tsetse) en las zonas forestales: relevante también para el perro.",
        "CHU de Libreville como única referencia hospitalaria seria del país. Fuera de la capital la infraestructura sanitaria es mínima: seguro con evacuación médica real, imprescindible.",
        "Agua: embotellada o tratada siempre; humedad y calor extremos todo el año en la costa, con riesgo de deshidratación en las caminatas de selva.",
    ],
    seguridad_intro=("Gabón es un país estable y, en términos de seguridad ciudadana, de los tranquilos de África central: no hay conflicto armado ni zonas excluidas en los corredores documentados. "
                     "Lo que condiciona el país no es el riesgo, sino la burocracia (el visado), el aislamiento y el precio."),
    seguridad=[
        "Sin zonas excluidas por seguridad en los corredores documentados.",
        "Transición política tras el golpe de agosto de 2023 y elecciones en abril de 2025: situación estable pero con sensibilidad alta ante cámaras, drones y fotografía de instalaciones oficiales, militares o portuarias. Preguntar siempre antes de sacar la cámara.",
        "Controles de gendarmería frecuentes en carretera: rutinarios, pero exigen documentación completa y paciencia. Llevar copias por triplicado.",
        "El riesgo real del país es el AISLAMIENTO: pistas largas sin tráfico, sin cobertura y sin suministro, especialmente en el este forestal y en los accesos a Loango, Ivindo y Moukalaba-Doudou. Dos vehículos y autonomía completa.",
        "Fauna: elefante de bosque (mucho más impredecible y agresivo que el de sabana), búfalo, hipopótamo y cocodrilo, y en Loango todos ellos EN LA PLAYA. Respetar distancias y no caminar solo por la orilla.",
        "Precio: Gabón es uno de los países más caros de África continental. Presupuestar al alza alojamiento, comida, combustible y cualquier actividad de parque.",
    ],
    agua=[
        "Libreville y Lambaréné: agua embotellada sin problema en supermercados.",
        "Recarga del depósito de uso general (ducha, aseo, limpieza): estaciones de servicio y hoteles de Libreville, Lambaréné, Mouila y Franceville permiten llenar con manguera; confirmar en recepción.",
        "Este forestal y mesetas Batéké: sin garantía de suministro tratado. Salir con los depósitos al 100% y con capacidad de filtrado.",
        "Nunca beber de ríos ni lagunas sin filtrar y tratar.",
    ],
    combustible=[
        "Eje oeste (N1), sin hueco relevante: Bitam → Oyem (~100 km) → Mitzic (~90 km) → Libreville (~350 km) → Lambaréné (~250 km) → Mouila (~180 km) → Ndendé (~70 km) → Doussala (~50 km), con estaciones formales en cada núcleo.",
        "Eje este, mucho más delicado: entre Makokou y el Ivindo, y en las mesetas Batéké, no hay suministro. Repostar a fondo en Makokou y en Franceville y llevar garrafas.",
        "Repostar siempre a fondo en Libreville: mejor oferta y mejor calidad del país (Total, Petro Gabon).",
        "Mayumba es la última plaza formal antes de la frontera congoleña en el corredor oeste: confirmar disponibilidad real antes de contar con ella.",
    ],
    experiencias_intro=("Relatos y datos recurrentes sobre Gabón entre viajeros por carretera. Con dos advertencias: en esta revisión no se pudo acceder directamente a iOverlander ni a "
                        "Tracks4Africa, y Gabón es de los países del continente con MENOS documentación overland disponible — hay muy pocos relatos y casi ninguno reciente."),
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("ESTATUS", "Ninguna acción pendiente mientras Gabón siga excluido. Esta ficha existe para tener la información, no para ejecutarla"),
        ("Si se reconsiderara · visado", "Llamar al consulado de Gabón en Barcelona (o a la embajada en Madrid): tasa del visado consular, plazo, documentación, si sirve para entrada terrestre y qué aceptan como justificante de entrada/salida en un viaje sin billete de avión. Pedir validez larga y entradas múltiples"),
        ("Si se reconsiderara · perro", "Escribir a la administración veterinaria gabonesa (Direction Générale de l'Élevage) para conocer los requisitos reales de importación y si admiten entrada por puesto terrestre. Es el agujero documental más grande de esta ficha"),
        ("Si se reconsiderara · Loango", "Confirmar operador, pista de acceso, precio y reserva con meses de antelación: es el punto más difícil de organizar del país"),
        ("Si se reconsiderara · Ivindo", "Confirmar desde Makokou la logística real de Kongou y Langoué Baï (pista + piragua + guía + días) y si hay permiso de parque que tramitar con la ANPN"),
        ("Frontera este", "Confirmar si existe y está habilitado un paso internacional Léconi → Okoyo (Congo) que admita vehículos extranjeros: enlazaría directamente con el corredor de subida de la ficha de Congo"),
        ("Monts de Cristal", "Coordenadas y accesos (Kinguélé, Tchimbélé) por confirmar: la información publicada es escasa"),
        ("Dron", "Contactar con la ANAC-Gabon o, más realista, descartar el vuelo en el país"),
        ("Starlink", "Sin confirmar en ninguna revisión: comprobar el mapa oficial si el país volviera a la ruta"),
        ("FOTOS", "Los 19 PDIs usan solo las cuatro imágenes de Gabón ya verificadas en el proyecto más una foto de la especie (gorila de llanura occidental), porque en esta revisión commons.wikimedia.org no era accesible desde el entorno de trabajo. Los PDIs que llevan foto prestada lo dicen en su descripción: sustituir una a una cuando se puedan verificar nombres de archivo"),
        ("Experiencias de overlanders", "Reverificar en iOverlander y Tracks4Africa: en esta revisión los dominios no fueron accesibles, y Gabón está además muy poco documentado"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Ficha de un país EXCLUIDO de la ruta fija, mantenida como documentación. No es una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Libreville): +241 (0)66 44 47 47 · Embajada: +241 (0)11 72 12 64.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

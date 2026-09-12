# -*- coding: utf-8 -*-
"""Ruanda — ficha completa (12 sep 2026): ALTERNATIVA (no está en la ruta fija).
Desvío que encaja pegado a Uganda: se entra desde Uganda (Cyanika/Gatuna) o desde
Tanzania (Rusumo) y se sale por el otro extremo. Criterio del dueño: solo entra si
hay tiempo y si el visado sirve por tierra — en Ruanda SÍ, y sin trámite previo."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"
NOFOTO = "Sin fotografía verificada en esta revisión (ver pendientes)"

POIS = [
    dict(n=1, name="Musanze (Ruhengeri) y sus cuevas", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-1.4990, lon=29.6350,
         desc="Puerta de entrada a los volcanes y base logística del norte: combustible, bancos, mercado y alojamientos de todos los precios, a 1.850 m de altitud y con los cinco conos de los Virunga asomando por encima de los tejados. Su rareza propia son las CUEVAS DE MUSANZE, dos kilómetros de tubos de lava formados por las erupciones de los volcanes, con bóvedas de más de diez metros, colonias de murciélagos y claraboyas por donde entra el sol; se visitan con casco y linterna en un recorrido de una hora larga. Es también el sitio donde se duerme la víspera del trekking de gorilas, porque hay que estar en Kinigi a las 7 de la mañana.",
         credit=NOFOTO, source=""),
    dict(n=2, name="Parque Nacional de los Volcanes (Kinigi)", cat="Naturaleza", prio="Alta", dog="prohibido", time="2–3 noches",
         lat=-1.4675, lon=29.4925,
         desc="160 km² que abarcan cinco de los ocho volcanes Virunga —Karisimbi, Bisoke, Muhabura, Gahinga y Sabyinyo— y la mitad ruandesa de la población mundial de gorila de montaña. Es el parque de Dian Fossey y el escenario de «Gorilas en la niebla». EL DATO QUE DECIDE: el permiso de trekking cuesta 1.500 USD POR PERSONA para no residentes, o sea 4.500 USD los tres viajeros por una hora con los gorilas — es el permiso más caro de África y casi el doble que el de Uganda. Tiene además el permiso de MONOS DORADOS, muchísimo más barato, y en septiembre celebra el Kwita Izina, la ceremonia nacional de bautizo de las crías nacidas ese año.",
         credit="Wikimedia Commons", source=W + "Bisoke%20Crater%20Lake%20in%20Volcanoes%20National%20Park%2C%20Rwanda.jpg?width=900"),
    dict(n=3, name="Monte Bisoke · el lago del cráter", cat="Naturaleza", prio="Alta", dog="prohibido", time="1 día",
         lat=-1.4581, lon=29.4886,
         desc="La mejor excursión a pie de Ruanda y la alternativa barata a los gorilas: subida de unas tres horas por barro y bambú hasta los 3.711 m, donde se abre un lago de cráter perfectamente circular de aguas verdes, con Ruanda a un lado y RD Congo al otro. No requiere técnica, sí buenas botas y bastones porque el descenso es un tobogán de barro. Se hace en el día desde Kinigi, con ranger obligatorio, y cuesta una fracción del permiso de gorilas.",
         credit="Wikimedia Commons", source="https://commons.wikimedia.org/wiki/Special:FilePath/Volcanoes%20National%20Park%20Rwanda.jpg?width=900"),
    dict(n=4, name="Karisoke y la tumba de Dian Fossey", cat="Cultura", prio="Media", dog="prohibido", time="medio día",
         lat=-1.4750, lon=29.4800,
         desc="Entre el Karisimbi y el Bisoke, a unas dos horas de caminata desde la puerta del parque, están las ruinas del centro de investigación de Karisoke que Dian Fossey fundó en 1967 y el pequeño cementerio donde ella misma está enterrada, junto a Digit y al resto de gorilas asesinados por los furtivos. Fossey fue asesinada en 1985 en su cabaña y su trabajo es la razón por la que los gorilas de montaña siguen existiendo. Es una caminata sencilla, mucho más barata que el trekking de gorilas y con un peso emocional que la mayoría no espera. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=5, name="Lagos gemelos Burera y Ruhondo", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-1.4333, lon=29.7667,
         desc="Dos lagos alargados separados por una lengua de tierra, al este de Musanze, con los volcanes al fondo y las laderas cultivadas en terrazas hasta el borde del agua: es el paisaje que sale en todas las fotos de «el país de las mil colinas» y casi nadie se para. Se recorren por una pista de tierra de cornisa que es una de las conducciones más bonitas del país, hay canoas locales y algún alojamiento pequeño en la orilla. Fuera de recinto de parque: se puede estar con el perro.",
         credit=NOFOTO, source=""),
    dict(n=6, name="Gisenyi (Rubavu) y el lago Kivu", cat="Costa", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-1.7000, lon=29.2500,
         desc="La playa del interior de África: arena, palmeras y un paseo marítimo colonial a orillas del Kivu, octavo lago de África (2.700 km², 480 m de profundidad máxima), pegado a la frontera con RD Congo — Goma está literalmente al otro lado de la verja. Se puede nadar sin miedo: el Kivu no tiene cocodrilos, ni hipopótamos, ni bilharzia documentada, algo excepcional en un lago africano. Tiene fuentes termales en Nyamyumba y, a pocos kilómetros, la fábrica de cerveza Bralirwa. Es el punto de arranque del Congo Nile Trail.",
         credit="Wikimedia Commons", source="https://commons.wikimedia.org/wiki/Special:FilePath/View%20over%20Lake%20Kivu%20from%20Home%20St.%20Jean%20-%20Kibuye%20(Karongi)%20-%20Rwanda%20-%2001%20(8970024017).jpg?width=900"),
    dict(n=7, name="Congo Nile Trail · la ruta de la orilla del Kivu", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="3–5 días",
         lat=-1.9000, lon=29.3400,
         desc="LA GRAN RUTA DEL PAÍS: unos 227 km por la orilla oriental del lago Kivu, de Rubavu (Gisenyi) en el norte a Rusizi (Cyangugu) en el sur, pasando por Kinunu, Karongi (Kibuye) y Kibogora. Está pensada para hacerse a pie (unos 10 días) o en bicicleta de montaña (unos 5), pero buena parte del trazado es PISTA TRANSITABLE EN 4x4 y se puede recorrer en dos o tres jornadas de conducción lenta y espectacular, entre plantaciones de café y té, bahías, calas y aldeas de pescadores. Coordenadas del punto medio orientativo (Kinunu). La divisoria de aguas Congo-Nilo pasa por las crestas de arriba: de un lado el agua va al Atlántico, del otro al Mediterráneo.",
         credit=NOFOTO, source=""),
    dict(n=8, name="Karongi (Kibuye) y las islas del Kivu", cat="Costa", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=-2.0600, lon=29.3500,
         desc="El punto medio del Congo Nile Trail y el rincón más bonito del lago: una península de penínsulas, con bahías recortadas, eucaliptos y agua tranquila. Desde el embarcadero salen barcas a la isla de Napoleón (llamada así por su forma de sombrero, con una colonia de murciélagos frugívoros en la cumbre) y a la isla de Amahoro. También hay un memorial del genocidio en la iglesia de San Pedro, donde murieron miles de personas en 1994. Buen sitio para parar con el perro: campings y hoteles junto al agua, y se puede nadar.",
         credit=NOFOTO, source=""),
    dict(n=9, name="Rusizi (Cyangugu) y la frontera de Bukavu", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-2.4833, lon=28.9000,
         desc="Extremo suroeste del país, donde el lago Kivu se vacía en el río Rusizi y termina el Congo Nile Trail. Es el final logístico del oeste, con combustible y servicios, y la puerta de Nyungwe por el sur. Enfrente, al otro lado del puente, está Bukavu (RD Congo), que NO forma parte de ninguna variante de la ruta. El pantano de Rugezi y las plantaciones de té de Gisakura quedan de camino a la selva.",
         credit=NOFOTO, source=""),
    dict(n=10, name="Parque Nacional de Nyungwe · la pasarela del dosel", cat="Patrimonio UNESCO", prio="Alta", dog="prohibido", time="2–3 noches",
         lat=-2.4900, lon=29.2928,
         desc="1.019 km² de selva de montaña primaria, una de las más antiguas de África y Patrimonio de la Humanidad desde 2023, gestionada por African Parks desde 2020. Tiene 13 especies de primates (una cuarta parte de todas las de África), incluidos chimpancés y bandas de colobos de Angola de varios cientos de individuos, más de 300 especies de aves con 30 endemismos del Rift Albertino y 1.068 especies de plantas. Su símbolo es la PASARELA SUSPENDIDA SOBRE EL DOSEL, la única de África oriental: unos 60 m de puente colgante a 50-70 m sobre el suelo del bosque, dentro del sendero de Igishigishigi entre helechos arborescentes. Hay además una red de más de 130 km de senderos y la cascada de Kamiranzovu.",
         credit=NOFOTO, source=""),
    dict(n=11, name="Huye (Butare) y el Museo Etnográfico Nacional", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-2.5967, lon=29.7400,
         desc="La capital intelectual del país, sede de la Universidad Nacional, y el mejor museo de Ruanda con diferencia: el Museo Etnográfico Nacional, regalo de Bélgica en 1989, con siete salas sobre geología, agricultura, ganadería, artesanía, vivienda, indumentaria y cultura, y reconstrucciones de casas tradicionales de paja. Es la parada que explica todo lo que se ve por la carretera. Alrededor hay talleres de cestería de imigongo y la catedral, la mayor del país.",
         credit=NOFOTO, source=""),
    dict(n=12, name="Nyanza · el Palacio del Rey (Rukari)", cat="Cultura", prio="Media", dog="permitido con condiciones", time="medio día",
         lat=-2.3500, lon=29.7500,
         desc="La capital histórica de la monarquía ruandesa. En la colina de Rukari se conserva reconstruido a tamaño real el palacio tradicional del mwami, una enorme cúpula de paja trenzada, y al lado el palacio de estilo colonial de los años treinta del rey Mutara III Rudahigwa. En los prados de detrás pastan las VACAS INYAMBO, la raza real de cuernos gigantescos en forma de lira, a las que sus cuidadores siguen cantando poemas de alabanza — una tradición viva de la corte que se puede ver en una demostración. Es el sitio para entender que Ruanda era un reino centralizado siglos antes de la colonización.",
         credit=NOFOTO, source=""),
    dict(n=13, name="Kigali", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-1.9536, lon=30.0606,
         desc="La capital más limpia, ordenada y segura de África, repartida sobre colinas y valles y sin un solo papel en el suelo; para un viaje overland es una parada de oro: talleres, recambios, veterinarios, hospitales de nivel, supermercados, embajadas y una escena de cafés y restaurantes inesperada. Merece la pena el Mercado de Kimironko, el barrio de Nyamirambo con su paseo guiado por mujeres del barrio, el Museo del Palacio Presidencial (con los restos del avión de Habyarimana cuyo derribo desencadenó el genocidio) y la vista desde el monte Kigali. Es también el nudo entre el norte de los volcanes, el este de Akagera y el sur de Nyungwe.",
         credit="Wikimedia Commons", source=W + "Kigali%20city%20view.jpg?width=900"),
    dict(n=14, name="Memorial del Genocidio de Kigali (Gisozi)", cat="Patrimonio UNESCO", prio="Alta", dog="prohibido", time="medio día",
         lat=-1.9311, lon=30.0600,
         desc="No es una atracción turística: es una tumba. Aquí están enterrados los restos de MÁS DE 250.000 PERSONAS asesinadas durante el genocidio contra los tutsis de 1994, en fosas comunes de cien mil cada una. Se inauguró el 7 de abril de 2004, en el décimo aniversario, y desde 2023 es Patrimonio de la Humanidad junto con otros tres memoriales. Dentro hay tres exposiciones permanentes: la del genocidio ruandés, la de otros genocidios del mundo y la SALA DE LOS NIÑOS, con fotografías, su comida favorita, su juego favorito y cómo murieron — es la parte que rompe a todo el mundo. Hay audioguía. Se entra en silencio, con ropa respetuosa, sin fotografías dentro de las exposiciones y sin prisa: hacen falta dos o tres horas. VISITA OBLIGATORIA para entender el país que se está atravesando, y NO es un sitio al que se lleve a un perro.",
         credit="Wikimedia Commons", source="https://commons.wikimedia.org/wiki/Special:FilePath/Kigali.jpg?width=900"),
    dict(n=15, name="Memoriales de Nyamata y Ntarama", cat="Patrimonio UNESCO", prio="Media", dog="prohibido", time="medio día",
         lat=-2.1450, lon=30.1050,
         desc="A unos 30 km al sur de Kigali, dos iglesias donde la gente se refugió en abril de 1994 creyendo que un templo sería sagrado. En Nyamata se encerraron unas 10.000 personas; los atacantes abrieron boquetes en los muros para tirar granadas dentro y después entraron con armas de fuego y machetes. Hoy hay 50.000 personas enterradas allí. Se conservan la ropa amontonada sobre los bancos, los documentos de identidad —con la mención étnica que los condenó— y el techo perforado. Patrimonio de la Humanidad desde 2023. Es una visita extremadamente dura y hay que decidirla con calma; quien la hace dice que es lo más importante que vio en África oriental. Coordenadas aproximadas, por confirmar.",
         credit=NOFOTO, source=""),
    dict(n=16, name="Lago Muhazi", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-1.8500, lon=30.3500,
         desc="Lago largo y ramificado al este de Kigali, en la carretera de Akagera: un sitio de fin de semana de los kigalíes, con embarcaderos, restaurantes de tilapia a la brasa y alojamientos sencillos junto al agua. No tiene ningún «monumento», y por eso mismo es el lugar natural para romper el trayecto con el perro entre la capital y el parque, o para esperar mientras otros están dentro de Akagera.",
         credit=NOFOTO, source=""),
    dict(n=17, name="Parque Nacional de Akagera", cat="Naturaleza", prio="Alta", dog="prohibido", time="2–3 noches",
         lat=-1.6333, lon=30.7833,
         desc="LA HISTORIA DE RECUPERACIÓN MÁS ESPECTACULAR DE ÁFRICA. En 2010 este parque de 1.122 km² en la frontera con Tanzania estaba arrasado por la caza furtiva y el ganado; African Parks y el Rwanda Development Board firmaron una gestión conjunta de 20 años, levantaron 120 km de valla en el límite oeste y montaron unidades antifurtivos. Desde entonces han vuelto los LEONES (dos machos en julio de 2015; 72 individuos en 2025), el RINOCERONTE NEGRO (18 ejemplares en mayo de 2017) y el BLANCO (30 en 2021 y 70 más en junio de 2025, el mayor traslado de rinocerontes de la historia). Hoy tiene los cinco grandes, 78 jirafas masái y un paisaje de lagos, papiros y colinas que no se parece a ninguna sabana clásica. Los visitantes pasaron de 8.000 en 2010 a 67.661 en 2025 y el parque cubre ya el 92% de sus costes. Se puede recorrer con el vehículo propio.",
         credit=NOFOTO, source=""),
    dict(n=18, name="Parque Nacional de Gishwati-Mukura", cat="Naturaleza", prio="Media", dog="prohibido", time="1 día",
         lat=-1.8000, lon=29.3500,
         desc="El parque más joven de Ruanda (2016) y Reserva de la Biosfera de la UNESCO desde 2020: dos retazos de selva de montaña que estuvieron a punto de desaparecer —Gishwati se quedó en el 10% de su superficie original por la deforestación y el reasentamiento de refugiados— y que se están reconectando con un corredor de bosque. Hay una pequeña población de chimpancés, monos dorados y colobos, senderos guiados, una cascada y visitas a las plantaciones de té. Está justo entre Gisenyi y Karongi: cae de camino por el Congo Nile Trail y casi nadie lo visita.",
         credit=NOFOTO, source=""),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul", "cultura": "morado",
              "patrimonio unesco": "marron", "costa": "turquesa"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = ("https://commons.wikimedia.org/wiki/File:" + _m.group(1)) if _m else ""
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Cyanika (con Uganda)", "Frontera", -1.2333, 29.6333,
     "Paso del noroeste entre Kisoro (Uganda) y Musanze: 25 km entre Mgahinga y el Parque de los Volcanes, la entrada natural si se viene de los gorilas ugandeses. Puesto pequeño y rápido, HORARIO LIMITADO (no 24 h): confirmar antes de llegar. AQUÍ SE REQUISAN LAS BOLSAS DE PLÁSTICO."),
    ("Frontera · Entrada alternativa — Gatuna/Katuna (con Uganda)", "Frontera", -1.2333, 29.9833,
     "Paso principal de la carretera troncal Kabale–Kigali, con mejor asfalto y más tráfico. Estuvo CERRADO entre 2019 y 2022 por la crisis diplomática con Uganda: confirmar estado 72 h antes."),
    ("Frontera · Salida — Rusumo (con Tanzania)", "Frontera", -2.3833, 30.7833,
     "Puente sobre las cataratas de Rusumo, en el río Kagera: la salida al este hacia Benako y Kahama (Tanzania), justo al sur de Akagera. Puesto de ventanilla única del corredor central. Es la salida lógica si se vuelve al bucle principal por Tanzania."),
    ("Frontera · Salida alternativa — Kagitumba (con Uganda)", "Frontera", -1.0333, 30.4667,
     "Extremo noreste, junto a Akagera, hacia Mbarara (Uganda). Útil si se quiere cerrar el bucle Uganda-Ruanda por el este en vez de por el oeste. Coordenadas aproximadas, por confirmar."),
    ("Embajada de España en Kampala/Nairobi (competencia para Ruanda)", "Consular", -1.2977, 36.8129,
     "No hay embajada de España en Ruanda. La competencia recae en la Embajada de España en Nairobi (Kenia): CBA Building, Mara & Ragati Roads, Upper Hill. Tel. +254 20 272 02 22/3/4/5; emergencia consular +254 733 63 11 44. CONFIRMAR la demarcación vigente antes del viaje."),
    ("King Faisal Hospital / CHUK, Kigali", "Hospital", -1.9536, 30.0606,
     "King Faisal Hospital (privado, Kacyiru) es la referencia para extranjeros y de los mejores de África oriental; CHUK es el hospital universitario público. Para casos muy graves, evacuación a Nairobi."),
    ("Combustible · Kigali, Musanze, Rubavu, Karongi, Rusizi, Huye", "Combustible", -1.9536, 30.0606,
     "Red de estaciones formales (SP, Engen, Rubis, Kobil) buena y bien repartida: Ruanda es un país pequeño con carreteras excelentes y no hay ningún gap de autonomía relevante. Repostar antes de meterse en el Congo Nile Trail y antes de Akagera."),
    ("Agua potable y de uso general · Kigali, Musanze, Gisenyi, Karongi", "Agua potable", -1.9536, 30.0606,
     "Agua embotellada en todas las ciudades. Para el depósito de uso general, los campings y lodges del Kivu (Gisenyi, Kinunu, Karongi) permiten llenar con manguera. El lago Kivu es de los pocos grandes lagos africanos sin bilharzia documentada."),
]

DRONE_CALLOUT = ("danger", "De los regímenes más estrictos de África: permiso previo obligatorio y espacio aéreo muy controlado",
                 "Ruanda regula el uso de drones a través de la Rwanda Civil Aviation Authority (RCAA) con autorización previa obligatoria para cualquier vuelo, incluido el recreativo, y un espacio aéreo activamente gestionado — es el país donde opera la red de drones sanitarios de Zipline, así que el control es real y no nominal. Volar sobre Kigali, sobre instalaciones gubernamentales, sobre los memoriales del genocidio y dentro de los parques nacionales está prohibido. Norma del proyecto: NO volar el dron en Ruanda; declararlo en frontera y asumir que puede quedar retenido si no hay permiso previo.")

STARLINK_CALLOUT = ("ok", "Activo, y además el país con mejor red terrestre del desvío",
                    "Starlink está operativo en Ruanda, pero aquí es casi un lujo: Ruanda tiene una de las mejores redes de fibra y 4G de África, con cobertura MTN Rwanda y Airtel prácticamente en todo el territorio, incluidos Musanze, el Kivu y Nyungwe. La SIM local es barata y se compra con pasaporte en cualquier tienda. Starlink sirve sobre todo como respaldo en Akagera y en los tramos altos del Congo Nile Trail.")

DOG_MATRIX = [
    ("Parque Nacional de los Volcanes y todo el trekking de gorilas", "prohibido",
     "Prohibición SANITARIA, no burocrática: los gorilas de montaña comparten patógenos con perros y humanos y por eso hay distancia mínima de 7-10 m y mascarilla obligatoria. Un perro no entra ni al parque ni a la zona de reunión de Kinigi. Plan B: dejarlo en Musanze (hay alojamientos con patio) o en los lagos Burera/Ruhondo con uno de los tres viajeros."),
    ("Nyungwe, Akagera y Gishwati-Mukura", "prohibido",
     "Ningún parque nacional ruandés admite mascotas. En Akagera hay leones y la prohibición es también de seguridad. Plan B: lago Muhazi (a una hora de Akagera) y Gisakura/Rusizi (junto a Nyungwe) como bases para los turnos."),
    ("Memoriales del genocidio (Gisozi, Nyamata, Ntarama, Murambi)", "prohibido",
     "Son cementerios. No se lleva un perro, ni atado ni esperando en la puerta. Dejarlo en el alojamiento."),
    ("Kigali, Musanze, Huye, Rubavu, Karongi, Rusizi", "permitido con condiciones",
     "Ruanda es un país muy ordenado y el perro llama la atención: correa siempre, recoger siempre (la limpieza es una cuestión de orgullo nacional y hay multas). Kigali tiene veterinarios de buen nivel y es la mejor ciudad del desvío para revisiones."),
    ("Orilla del lago Kivu y Congo Nile Trail", "permitido con condiciones",
     "LA MEJOR ZONA DEL PAÍS CON EL PERRO: la pista del Kivu no atraviesa parque nacional, hay campings y hoteles junto al agua, y el Kivu no tiene cocodrilos ni hipopótamos ni bilharzia documentada, así que el perro puede bañarse. Es la base natural para los turnos mientras otros hacen los gorilas."),
    ("Lagos Burera y Ruhondo, lago Muhazi", "permitido con condiciones",
     "Fuera de recinto de parque, pistas de cornisa y alojamientos sencillos junto al agua. Alternativa concreta a quedarse encerrado en Musanze durante el trekking."),
]

SOURCES = [
    ("Irembo · portal oficial de trámites del gobierno de Ruanda (visados)", "https://irembo.gov.rw/"),
    ("Rwanda Development Board · permisos de trekking de gorilas y tarifas de parques", "https://www.rdb.rw/"),
    ("Visit Rwanda · web oficial de turismo", "https://www.visitrwanda.com/"),
    ("Rwanda Civil Aviation Authority · normativa de drones", "https://www.rcaa.gov.rw/"),
    ("Kigali Genocide Memorial · web oficial", "https://www.kgm.rw/"),
    ("African Parks · Akagera y Nyungwe", "https://www.africanparks.org/"),
    ("UNESCO · Parque Nacional de Nyungwe, Patrimonio de la Humanidad (2023)", "https://whc.unesco.org/en/list/1697/"),
    ("UNESCO · Sitios memoriales del genocidio de 1994 contra los tutsis (2023)", "https://whc.unesco.org/en/list/1586/"),
    ("Wikipedia · Política de visados de Ruanda (visado a la llegada para todas las nacionalidades desde 2018)", "https://en.wikipedia.org/wiki/Visa_policy_of_Rwanda"),
    ("Wikipedia · Parque Nacional de los Volcanes (los cinco volcanes, Karisoke y Dian Fossey)", "https://en.wikipedia.org/wiki/Volcanoes_National_Park"),
    ("Wikipedia · Bosque de Nyungwe (superficie, 13 primates, African Parks, UNESCO 2023)", "https://en.wikipedia.org/wiki/Nyungwe_Forest"),
    ("Wikipedia · Parque Nacional de Akagera (reintroducciones de leones y rinocerontes, cifras de African Parks)", "https://en.wikipedia.org/wiki/Akagera_National_Park"),
    ("Wikipedia · Lago Kivu (dimensiones, gas disuelto, ciudades de la orilla)", "https://en.wikipedia.org/wiki/Lake_Kivu"),
    ("Wikipedia · Memorial del Genocidio de Kigali (250.000 personas enterradas, UNESCO 2023)", "https://en.wikipedia.org/wiki/Kigali_Genocide_Memorial"),
    ("Wikipedia · Memorial de Nyamata (50.000 personas enterradas)", "https://en.wikipedia.org/wiki/Nyamata_Genocide_Memorial"),
    ("Wikipedia · Umuganda (último sábado de mes, 8:00-11:00, tráfico detenido)", "https://en.wikipedia.org/wiki/Umuganda"),
    ("Wikipedia · Eliminación de las bolsas de plástico ligeras (prohibición ruandesa desde 2008)", "https://en.wikipedia.org/wiki/Phase-out_of_lightweight_plastic_bags"),
    ("Wikipedia · Distrito de Musanze (los cinco volcanes y la base de los gorilas)", "https://en.wikipedia.org/wiki/Musanze_District"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("iOverlander · puntos de combustible, agua y acampada verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Entrada desde Uganda por el noroeste y bajada de toda la orilla del Kivu hasta Nyungwe
CORRIDOR = [(-1.2333, 29.6333), (-1.4990, 29.6350), (-1.4675, 29.4925), (-1.4333, 29.7667),
            (-1.4990, 29.6350), (-1.7000, 29.2500), (-1.8000, 29.3500), (-1.9000, 29.3400),
            (-2.0600, 29.3500), (-2.4833, 28.9000), (-2.4900, 29.2928)]

# Salida por el centro y el este: Nyungwe → Huye → Nyanza → Kigali → Akagera → Rusumo
CORRIDOR_ALT = [(-2.4900, 29.2928), (-2.5967, 29.7400), (-2.3500, 29.7500), (-2.1450, 30.1050),
                (-1.9536, 30.0606), (-1.8500, 30.3500), (-1.6333, 30.7833), (-2.3833, 30.7833)]

HISTORIA_RESUMEN = ("Ruanda fue durante siglos un reino centralizado y jerárquico gobernado por el mwami, que la colonización alemana y después belga transformó en un sistema de identidad étnica rígida con carné obligatorio; "
                    "esa construcción colonial, unida a décadas de violencia política tras la independencia de 1962, desembocó en el genocidio contra los tutsis de 1994, en el que fueron asesinadas alrededor de un millón de personas en cien días. "
                    "El país que se atraviesa hoy es el resultado de una reconstrucción excepcionalmente rápida y excepcionalmente dirigida: seguridad, limpieza y eficiencia administrativa notables, con un debate internacional abierto sobre libertades políticas.")

HISTORIA_SECCIONES = [
    ("El reino de Ruanda antes de la colonización",
     "Mucho antes de la llegada de los europeos, Ruanda era un reino centralizado con una monarquía (el mwami) de la dinastía Nyiginya, un ejército organizado y un sistema de clientelismo ganadero, el ubuhake, que vinculaba a las familias entre sí. "
     "Hutus, tutsis y twa compartían lengua (kinyarwanda), religión y territorio: las categorías eran fundamentalmente sociales y permeables, y se podía pasar de una a otra. El palacio real de Nyanza y las vacas inyambo de cuernos en lira son lo que queda visible de ese mundo."),
    ("La colonización y la invención de la etnia",
     "Alemania ocupó el territorio en 1897 y Bélgica lo recibió tras la Primera Guerra Mundial. La administración belga gobernó a través de la élite tutsi, impuso en 1933 un CARNÉ DE IDENTIDAD CON MENCIÓN ÉTNICA OBLIGATORIA y aplicó teorías raciales pseudocientíficas "
     "—midiendo narices y cráneos— para fijar como categorías biológicas cerradas lo que había sido una distinción social. Esa tarjeta de identidad es la que, sesenta años después, serviría en las barreras de carretera para separar a quien vivía de quien moría. Los documentos que se ven hoy en el memorial de Nyamata son exactamente esos."),
    ("Independencia, violencia cíclica y exilio",
     "La «revolución social» de 1959 y la independencia de 1962 invirtieron el orden: el poder pasó a la mayoría hutu y comenzaron oleadas de violencia y expulsiones que empujaron a cientos de miles de tutsis al exilio en Uganda, Burundi y Tanzania. "
     "De esa diáspora salió el Frente Patriótico Ruandés, que invadió el país desde Uganda en 1990 y abrió una guerra civil cerrada en falso con los acuerdos de Arusha de 1993."),
    ("El genocidio de 1994",
     "El 6 de abril de 1994 fue derribado el avión del presidente Habyarimana sobre Kigali. En las horas siguientes empezó un genocidio planificado: en unos cien días fueron asesinadas alrededor de un millón de personas, tutsis y hutus moderados, "
     "sobre todo a machete, por milicias interahamwe, el ejército y vecinos, con la radio RTLM dirigiendo las matanzas y con la comunidad internacional retirando sus tropas en lugar de intervenir. Iglesias como las de Nyamata y Ntarama, donde la gente se refugió creyendo que serían respetadas, fueron algunos de los peores escenarios. "
     "El FPR de Paul Kagame detuvo el genocidio militarmente en julio de 1994. Los memoriales de Gisozi, Nyamata, Bisesero y Murambi son Patrimonio de la Humanidad desde 2023: son tumbas, no museos, y se visitan como tales."),
    ("Situación actual: reconstrucción, orden y debate",
     "En treinta años Ruanda ha pasado de país arrasado a uno de los estados más eficaces del continente: seguridad alta, corrupción baja, limpieza obsesiva (prohibición de bolsas de plástico desde 2008, jornada mensual de trabajo comunitario Umuganda), "
     "cobertura sanitaria amplia y un turismo de naturaleza de precio muy alto y muy bien gestionado. En paralelo hay un debate internacional serio sobre la libertad de prensa, la oposición política y el papel de Ruanda en el este de RD Congo. "
     "Para el viajero, el resultado práctico es el país más fácil, ordenado y seguro de todo el bucle este."),
]

HISTORIA_FUENTES = [
    ("BBC News · Rwanda country profile", "https://www.bbc.com/news/world-africa-14093238"),
    ("Encyclopaedia Britannica · Rwanda, History", "https://www.britannica.com/place/Rwanda/History"),
    ("United Nations · Outreach Programme on the Rwanda Genocide", "https://www.un.org/en/preventgenocide/rwanda/"),
    ("UNESCO · Sitios memoriales del genocidio de 1994 contra los tutsis", "https://whc.unesco.org/en/list/1586/"),
    ("Kigali Genocide Memorial · web oficial", "https://www.kgm.rw/"),
]

SPEC = dict(
    slug="ruanda", name="Ruanda", revision="12 sep 2026",
    sub="ALTERNATIVA — no está en la ruta fija · va unida a Uganda · gorilas a 1.500 USD · el país más limpio de África",
    chips=[
        ("ESTATUS", "ALTERNATIVA: solo si hay tiempo; va emparejada con Uganda"),
        ("COSTE DEL DESVÍO", "+1.100 km y +9-12 días (vuelta completa al país)"),
        ("VISADO", "SIN TRÁMITE PREVIO: visado a la llegada para todas las nacionalidades, también por tierra"),
        ("ENTRADA", "Cyanika o Gatuna (desde Uganda)"),
        ("SALIDA", "Rusumo (a Tanzania) · Kagitumba (a Uganda)"),
        ("EL DATO DECISIVO", "Permiso de gorilas: 1.500 USD/persona — 4.500 USD los tres"),
        ("RECOMENDACIÓN", "Hacer los gorilas en UGANDA (800 USD) y Ruanda para Nyungwe, Kivu y Kigali"),
        ("PLÁSTICO", "BOLSAS DE PLÁSTICO PROHIBIDAS Y REQUISADAS EN FRONTERA desde 2008"),
        ("CONDUCCIÓN", "Se conduce por la DERECHA — se cambia de lado al entrar desde Uganda"),
        ("PERRO", "Prohibido en parques y memoriales; el Kivu es la mejor base"),
    ],
    center=[-1.95, 29.9], zoom=8,
    notice="Documento de planificación de una ALTERNATIVA que aún no está decidida. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, si finalmente se incluye este desvío.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Entrada desde Uganda y bajada del Kivu",
    corridor_alt_label="Centro, Kigali, Akagera y salida a Tanzania",
    hero_img=W + "Bisoke%20Crater%20Lake%20in%20Volcanoes%20National%20Park%2C%20Rwanda.jpg?width=900",
    hero_credit="Lago del cráter del Bisoke, Parque Nacional de los Volcanes · Wikimedia Commons",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("RUANDA NO ESTÁ EN LA RUTA FIJA. El dueño la situó entre las alternativas: «Ruanda / Uganda, Esuatini / Lesoto y Gabón como alternativas si hay tiempo y si tienen eVisa». Respuesta a las dos condiciones: "
              "(1) VISADO: es el caso MÁS FÁCIL de toda la ruta. Ruanda concede VISADO A LA LLEGADA A TODAS LAS NACIONALIDADES desde el 1 de enero de 2018, y lo hace también en los puestos TERRESTRES (Cyanika, Gatuna, Rusumo, Kagitumba): "
              "no hace falta ni eVisa previa, aunque se puede sacar por adelantado en el portal Irembo si se prefiere llegar con todo hecho. Es decir, la condición que el dueño puso no solo se cumple: aquí ni siquiera hay trámite previo obligatorio. "
              "Vale también el VISADO TURÍSTICO DE ÁFRICA ORIENTAL (100 USD, 90 días, Kenia+Uganda+Ruanda), que es lo lógico si se hace todo el desvío. "
              "(2) TIEMPO: el país entero se recorre en 9-12 días y unos 1.100 km — es pequeño, tiene las mejores carreteras de África oriental y todo está a tres o cuatro horas de todo. "
              "RUANDA Y UGANDA SON EL MISMO DESVÍO: se entra a Ruanda desde Uganda por Cyanika (25 km entre Mgahinga y el Parque de los Volcanes) y se sale a Tanzania por Rusumo, cerrando el bucle sin repetir camino. Si se hace una, se hace la otra. "
              "LA DECISIÓN ECONÓMICA: el permiso de gorilas de Ruanda cuesta 1.500 USD POR PERSONA (4.500 USD los tres) frente a 800 USD en Uganda (2.400 USD). Es el mismo animal y el mismo macizo volcánico. "
              "Recomendación de esta ficha: hacer el trekking de gorilas en UGANDA y usar Ruanda para lo que no tiene Uganda — Nyungwe y su pasarela sobre el dosel, la ruta del lago Kivu, Akagera con los cinco grandes, y Kigali y sus memoriales, "
              "que son lo más importante que se puede ver en esta parte del continente. Ahorro estimado: 2.100 USD."),
    facts=[
        ("Estatus", "ALTERNATIVA, no ruta fija. Va emparejada con Uganda: el desvío tiene sentido como bloque Uganda+Ruanda, no como país suelto."),
        ("Coste en ruta", "Vuelta completa al país: unos 1.100 km y 9-12 días. Versión mínima (Volcanes + Kigali + memoriales + salida a Tanzania): unos 600 km y 5-6 días."),
        ("Visado y entrada terrestre", "CONFIRMADO: visado a la llegada para todas las nacionalidades desde el 1/1/2018, también en frontera terrestre. Sin trámite previo obligatorio; opcionalmente por adelantado en el portal Irembo. 30 días, 50 USD (confirmar tarifa vigente)."),
        ("Visado regional", "Visado Turístico de África Oriental (EATV): 100 USD, 90 días, entradas múltiples entre Kenia, Uganda y Ruanda. Debe usarse por primera vez en el país emisor."),
        ("Entrada", "Cyanika (desde Kisoro, Uganda; 25 km entre Mgahinga y los Volcanes) o Gatuna/Katuna (desde Kabale, carretera troncal a Kigali)."),
        ("Salida", "Rusumo hacia Tanzania (el cierre lógico del bucle) o Kagitumba de vuelta a Uganda."),
        ("El dato decisivo", "Permiso de trekking de gorilas en el Parque de los Volcanes: 1.500 USD POR PERSONA para no residentes. Los tres viajeros: 4.500 USD por una hora. Es el permiso de fauna más caro de África. Permiso de monos dorados: del orden de 100 USD (confirmar)."),
        ("Comparación con Uganda", "800 USD en Uganda frente a 1.500 en Ruanda por el mismo animal. A cambio, en Ruanda la caminata suele ser más corta y el acceso mucho mejor. Decisión conjunta con la ficha de Uganda."),
        ("Plástico", "RUANDA PROHIBIÓ LAS BOLSAS DE PLÁSTICO EN 2008 y los plásticos de un solo uso en 2019. Se registra el equipaje en frontera y se requisan. Hay que vaciar los vehículos de bolsas antes de llegar al puesto."),
        ("Umuganda", "El ÚLTIMO SÁBADO DE CADA MES, de 8:00 a 11:00, es obligatorio el trabajo comunitario y SE DETIENE EL TRÁFICO. No se puede circular esas tres horas: hay que planificar las etapas para no quedarse parado en carretera."),
        ("Conducción", "Se conduce por la DERECHA, al contrario que Kenia, Uganda y Tanzania. El cambio de lado se produce justo en la frontera."),
        ("Vehículo", "CPD exigido en la práctica; seguro COMESA (tarjeta amarilla) válido; carné internacional obligatorio."),
        ("Perro", "Prohibido en todos los parques nacionales y en los memoriales del genocidio. La orilla del lago Kivu es la mejor base del país con él."),
        ("Drones", "Muy restrictivo: autorización previa de la RCAA. Norma del proyecto: no volar."),
    ],
    alerts=[
        "ESTATUS ALTERNATIVA: nada de lo que hay aquí está comprometido. Este desvío se decide junto con el de Uganda, con el calendario real en la mano.",
        "BOLSAS DE PLÁSTICO PROHIBIDAS: Ruanda las prohibió en 2008 y prohibió los plásticos de un solo uso en 2019. EN LA FRONTERA SE REGISTRA EL EQUIPAJE Y SE REQUISAN. Para dos vehículos de expedición cargados con meses de África encima, esto es un problema práctico real: hay que vaciar y reorganizar el almacenamiento en bolsas de tela o cajas ANTES de llegar al puesto, no en la cola.",
        "UMUGANDA: el último sábado de cada mes, de 8:00 a 11:00, el tráfico se detiene en todo el país por el trabajo comunitario obligatorio. Comercios cerrados y carreteras cortadas. Es un dato de planificación de etapas, no una curiosidad.",
        "El permiso de gorilas cuesta 1.500 USD POR PERSONA. Antes de emocionarse con Ruanda hay que decidir si el trekking se hace aquí o en Uganda a 800 USD.",
        "SE CONDUCE POR LA DERECHA. Se viene de Kenia, Uganda y Tanzania, que conducen por la izquierda: el cambio se produce en la propia frontera y los primeros kilómetros son los peligrosos, sobre todo en las rotondas y al girar.",
        "Frontera de Gatuna/Katuna: estuvo CERRADA entre 2019 y 2022 por la crisis diplomática entre Ruanda y Uganda. Reabierta, pero es una frontera que ya cerró una vez: confirmar 72 h antes y tener Cyanika como plan B.",
        "FRONTERA OCCIDENTAL CON RD CONGO: el este congoleño (Goma, Bukavu, Kivu Norte y Sur) tiene conflicto armado activo. Gisenyi y Rusizi están literalmente pegadas a esa frontera y son seguras del lado ruandés, pero NO SE CRUZA bajo ningún concepto, y conviene consultar la situación antes de acampar en la orilla norte del Kivu.",
        "Los memoriales del genocidio son TUMBAS, no atracciones. Ropa respetuosa, silencio, nada de fotos dentro de las exposiciones, nada de drones, y no se lleva al perro. La visita al memorial de Kigali necesita dos o tres horas y deja tocado: no programar nada exigente para después.",
        "Drones: autorización previa obligatoria de la RCAA y espacio aéreo activamente controlado (es el país de la red de drones sanitarios Zipline). Declararlo en frontera y asumir que no se vuela.",
        "Malaria presente sobre todo en el este (Akagera, Kirehe, Bugesera) y en cotas bajas; Kigali, Musanze, los Volcanes y Nyungwe tienen riesgo bajo por altitud. Profilaxis a valorar con Sanidad Exterior según el itinerario exacto.",
    ],
    ruta_intro=("Dos corredores que no se solapan y recorren el país en herradura. El primero entra desde Uganda por Cyanika, hace base en Musanze para los volcanes y los gorilas, sube a los lagos gemelos y baja después TODA la orilla del lago Kivu "
                "—Gisenyi, Gishwati, Kinunu, Karongi, Rusizi— siguiendo el Congo Nile Trail hasta la selva de Nyungwe. El segundo vuelve por el centro y el este: Huye y su museo, el palacio real de Nyanza, Kigali y sus memoriales, el lago Muhazi, "
                "Akagera con los cinco grandes, y salida a Tanzania por Rusumo. Etapas calculadas sobre la media del proyecto de 250 km/día, aunque en Ruanda las distancias son cortas y lo que consume tiempo es la montaña, no los kilómetros."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada y los volcanes", "Cyanika → Musanze (cuevas) → Kinigi", "~30 km · 2 días"),
        ("2 · Gorilas o Bisoke", "Parque de los Volcanes: trekking de gorilas (1.500 USD/persona), monos dorados, Bisoke o Karisoke", "2-3 días de parada"),
        ("3 · Los lagos gemelos", "Musanze → Burera y Ruhondo → Musanze", "~80 km · 1-2 días"),
        ("4 · Bajada al Kivu", "Musanze → Rubavu (Gisenyi)", "~65 km · 2 días de parada en la playa"),
        ("5 · La selva joven", "Gisenyi → Gishwati-Mukura", "~60 km · 1 día"),
        ("6 · Congo Nile Trail (norte)", "Gisenyi → Kinunu → Karongi (Kibuye), por la pista de la orilla", "~110 km · 2 días de conducción muy lenta"),
        ("7 · Las islas del Kivu", "Karongi: isla de Napoleón, bahías, memorial de San Pedro", "1-2 días de parada"),
        ("8 · Congo Nile Trail (sur)", "Karongi → Kibogora → Rusizi (Cyangugu)", "~120 km · 2 días"),
        ("9 · La selva antigua", "Rusizi → Nyungwe (pasarela del dosel, chimpancés, colobos, Kamiranzovu)", "~55 km · 3 días"),
        ("10 · El sur culto", "Nyungwe → Huye (Butare) y el Museo Etnográfico", "~90 km · 1-2 días"),
        ("11 · El reino", "Huye → Nyanza (Palacio del Rey y vacas inyambo)", "~30 km · medio día"),
        ("12 · Memoria", "Nyanza → Nyamata y Ntarama → Kigali", "~110 km · 2 días (memoriales)"),
        ("13 · Capital", "Kigali: Memorial de Gisozi, Kimironko, Nyamirambo, talleres y veterinario", "2-3 días de parada"),
        ("14 · Hacia el este", "Kigali → lago Muhazi → Akagera (puerta sur, Kayonza)", "~130 km · 1-2 días"),
        ("15 · Los cinco grandes", "Parque Nacional de Akagera: lagos, leones y rinocerontes", "2-3 días de parada"),
        ("16 · Salida a Tanzania", "Akagera → Kirehe → Rusumo → Tanzania", "~120 km · 1 día"),
        ("Alt. · Salida a Uganda", "Akagera → Nyagatare → Kagitumba → Mbarara", "~110 km · 1 día"),
    ],
    offroad=[
        "CONGO NILE TRAIL (Rubavu → Kinunu → Karongi → Kibogora → Rusizi), unos 227 km: LA RUTA 4x4 DEL PAÍS. Está diseñada como itinerario a pie (10 días) y en bicicleta de montaña (5 días), pero buena parte del trazado es pista de tierra transitable en 4x4, y en dos o tres jornadas de conducción lenta se recorre entera por la orilla del Kivu, entre cafetales, terrazas, calas y aldeas de pescadores. CONFIRMAR SOBRE EL TERRENO qué tramos admiten vehículo: hay sectores estrechos pensados solo para bici y peatón, y conviene preguntar en cada pueblo en lugar de forzar.",
        "Pista de cornisa de los lagos Burera y Ruhondo: tierra y balasto por el filo de las crestas, con los volcanes al fondo. Corta, muy bonita y con pendientes fuertes; en lluvias, resbaladiza de verdad.",
        "Pistas interiores del Parque Nacional de Akagera: el parque se recorre con vehículo propio por una red de pistas de tierra y balasto, con tramos de barro negro junto a los lagos que se ponen difíciles en lluvias. La ruta del norte (llanuras de Kilala) es la buena para los leones.",
        "Accesos de Nyungwe y la carretera de Gisakura: asfalto excelente pero de montaña extrema, con niebla permanente y curvas continuas — no es offroad, pero sí un tramo de conducción exigente que hay que cronometrar bien.",
        "AVISO GENERAL: Ruanda tiene las mejores carreteras asfaltadas de África oriental, así que el 4x4 aquí no se usa por necesidad sino por elección. El país no tiene tramos de arena, dunas ni desierto: lo suyo es montaña, barro y pendiente.",
    ],
    senderismo=[
        "MONTE BISOKE (3.711 m): la mejor excursión del país y la alternativa barata a los gorilas. Unas tres horas de subida por bambú y barro desde Kinigi hasta un lago de cráter circular en la cumbre, con RD Congo al otro lado. Sin técnica; bastones y botas impermeables imprescindibles porque la bajada es un tobogán.",
        "MONTE KARISIMBI (4.507 m): el más alto de los Virunga ruandeses y una ascensión de DOS DÍAS con vivac a 3.700 m en un refugio muy básico. Frío de verdad por la noche. Ranger obligatorio.",
        "Karisoke y la tumba de Dian Fossey: unas dos horas de caminata desde la puerta del parque hasta las ruinas del centro de investigación y el cementerio de gorilas donde Fossey está enterrada. Barato y con un peso emocional inesperado.",
        "Monte Muhabura (4.127 m) y Gahinga (3.474 m) desde el lado ruandés: conos perfectos, subida de un día muy exigente en el caso del Muhabura, con lago de cráter en la cima.",
        "PASARELA DEL DOSEL DE NYUNGWE (sendero de Igishigishigi): unos 60 m de puente colgante a 50-70 m sobre el suelo del bosque, la única pasarela de dosel de África oriental. El sendero completo es de unas dos horas entre helechos arborescentes.",
        "Nyungwe, sendero de la cascada de Kamiranzovu: 5-6 horas por el mayor pantano de altura del país hasta un salto escondido en la selva. Y el sendero de Bigugu, que sube al pico más alto del parque (2.921 m) con vistas al Kivu.",
        "Seguimiento de colobos de Angola en Nyungwe: bandas de varios cientos de individuos, un espectáculo distinto al de los chimpancés y mucho más fácil de ver.",
        "Congo Nile Trail a pie: los 227 km completos son unos 10 días de caminata por la orilla del Kivu; se pueden hacer tramos sueltos de un día desde Kinunu o Karongi, durmiendo en el vehículo y caminando con el perro, que aquí SÍ puede ir.",
        "Paseo guiado de Nyamirambo (Kigali): recorrido a pie por el barrio musulmán de la capital, organizado por una cooperativa de mujeres del barrio. Es la mejor forma de ver Kigali de verdad y dura unas tres horas.",
        "Monte Kigali y monte Jali: caminatas de medio día en las colinas que rodean la capital, con vistas sobre la ciudad. Fuera de parque nacional: se pueden hacer con el perro.",
        "Senderos de té de Gisakura y Gishwati: paseos suaves entre plantaciones, sin ranger y sin tasa de parque, perfectos para los días de descanso.",
    ],
    acampada=[
        "Musanze/Kinigi: campings y lodges con parcela junto a la puerta del Parque de los Volcanes; caros en la zona de gorilas, razonables en el pueblo.",
        "Lagos Burera y Ruhondo: alojamientos pequeños en la orilla y sitios para pernoctar con el vehículo, fuera de recinto de parque. Buena opción con el perro.",
        "Gisenyi (Rubavu): campings y hoteles junto a la playa del Kivu, con posibilidad de bañarse. Uno de los mejores sitios del desvío para parar varios días.",
        "Kinunu y Karongi (Congo Nile Trail): guest houses y campamentos comunitarios pensados para los ciclistas de la ruta, con espacio para vehículo; muy baratos.",
        "Gisakura (Nyungwe): alojamientos junto a la puerta oeste del parque, entre plantaciones de té; base para los senderos y para dejar al perro.",
        "Kigali: la oferta es hotelera más que de camping; hay alojamientos con aparcamiento vigilado y patio que admiten perro — confirmar por escrito antes.",
        "Akagera: campsites del parque (Mutumba, Muyumbu, Shakani) con vistas a los lagos y fauna suelta alrededor, y el lago Muhazi como alternativa fuera del parque con el perro.",
    ],
    visado=[
        "VISADO A LA LLEGADA PARA TODAS LAS NACIONALIDADES desde el 1 de enero de 2018, incluidos los puestos TERRESTRES (Cyanika, Gatuna, Rusumo, Kagitumba). Es el país más fácil de todo el bucle: no hace falta trámite previo obligatorio.",
        "CRITERIO DEL DUEÑO — VÁLIDO POR TIERRA: sí, y además sin necesidad de eVisa. Se puede sacar por adelantado en el portal oficial Irembo (irembo.gov.rw) si se prefiere llegar con todo resuelto y ahorrar tiempo en el puesto, pero no es obligatorio.",
        "Visado de turista de entrada única, 30 días: del orden de 50 USD. Confirmar tarifa vigente en Irembo al tramitar.",
        "VISADO TURÍSTICO DE ÁFRICA ORIENTAL (EATV): 100 USD, 90 días, entradas múltiples entre Kenia, Uganda y Ruanda — la opción evidente si se hace el desvío completo. Debe usarse por primera vez en el país que lo emite.",
        "Certificado internacional de fiebre amarilla exigido si se procede de país endémico, que es el caso viniendo de Uganda, Kenia o Tanzania.",
        "Pasaporte con validez mínima de 6 meses y páginas libres.",
    ],
    fronteras_rows=[
        ("Entrada (preferente)", "Cyanika (Uganda)", "Kisoro → Musanze. Solo 25 km entre Mgahinga y el Parque de los Volcanes: el enlace natural del desvío. Puesto pequeño y rápido, HORARIO LIMITADO (no 24 h). AQUÍ SE REQUISAN LAS BOLSAS DE PLÁSTICO."),
        ("Entrada (alternativa)", "Gatuna / Katuna (Uganda)", "Kabale → Kigali por la troncal, mejor asfalto y más tráfico. ESTUVO CERRADO 2019-2022: confirmar estado 72 h antes."),
        ("Salida (preferente)", "Rusumo (Tanzania)", "Puente sobre las cataratas de Rusumo, al sur de Akagera, hacia Benako y Kahama. OSBP del corredor central. Es el cierre lógico del bucle hacia Tanzania."),
        ("Salida (alternativa)", "Kagitumba (Uganda)", "Noreste, junto a Akagera, hacia Mbarara. Útil si se prefiere cerrar el bucle volviendo a Uganda por el este en vez de por el oeste."),
        ("NO utilizable", "La Grande Barrière / Petite Barrière (Goma) y Ruzizi (Bukavu), RD Congo", "Conflicto armado activo en el este de RD Congo. Fuera de cualquier variante de la ruta."),
        ("NO prevista", "Nemba / Ruhwa (Burundi)", "Burundi no forma parte del itinerario. Se conserva solo como referencia."),
    ],
    vehiculos=[
        "CPD (Carnet de Passages en Douane) exigido en la práctica; con él el trámite en frontera es rápido y Ruanda es de las aduanas más eficientes del continente.",
        "Seguro de terceros COMESA (tarjeta amarilla) válido en Ruanda; verificar que el certificado incluya el país.",
        "SE CONDUCE POR LA DERECHA, al contrario que Kenia, Uganda y Tanzania. El cambio de lado se produce en la propia frontera: atención en las primeras rotondas y giros.",
        "Carné de conducir internacional obligatorio junto con el nacional.",
        "Carreteras asfaltadas excelentes y muy bien señalizadas, pero de montaña continua: las medias reales son bajas y hay muchos radares y controles de velocidad, que se aplican de verdad. Ruanda multa.",
        "Prohibido conducir un vehículo sucio en algunas ciudades (hay normativa municipal de limpieza y se ha multado por ello): lavar los coches antes de entrar en Kigali es un consejo real, no una anécdota. Por confirmar el alcance exacto de la norma.",
        "Tasa de carretera para vehículos extranjeros en frontera: presupuestar, importe por confirmar.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autorización previa obligatoria de la Rwanda Civil Aviation Authority (RCAA) para cualquier vuelo, incluido el recreativo.",
        "Espacio aéreo activamente gestionado: Ruanda opera la red nacional de drones sanitarios de Zipline, así que el control no es teórico.",
        "Prohibido volar sobre Kigali, sobre instalaciones gubernamentales, sobre los memoriales del genocidio y dentro de los parques nacionales.",
        "Norma del proyecto para Ruanda: NO volar. Declarar el dron en frontera y asumir que puede quedar retenido si no hay permiso previo.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Starlink operativo, pero en Ruanda es casi redundante: la red terrestre es la mejor del bucle este.",
        "SIM local de MTN Rwanda o Airtel Rwanda, barata y con cobertura 4G prácticamente en todo el país, incluidos Musanze, la orilla del Kivu y Nyungwe.",
        "Starlink como respaldo útil sobre todo en Akagera y en los tramos altos y aislados del Congo Nile Trail.",
    ],
    perro_intro=[
        "Permiso de importación previo del Rwanda Agriculture and Animal Resources Development Board (RAB) / servicios veterinarios — según el dosier del proyecto, entrada terrestre PROBABLE, con la administración más eficiente y digitalizada de África central (probablemente el trámite más limpio de toda la ruta).",
        "Certificado veterinario internacional reciente, vacuna antirrábica en vigor y desparasitación. Documentación en inglés o francés.",
        "Nombrar EXPLÍCITAMENTE el puesto terrestre (Cyanika, Gatuna o Rusumo) en la solicitud del permiso, siguiendo el criterio general del dosier canino.",
        "Kigali tiene veterinarios de buen nivel y es el mejor sitio del desvío para revisiones y para reponer antiparasitarios.",
        "El perro no entra en ningún parque nacional ni en ningún memorial del genocidio. La orilla del lago Kivu, en cambio, es de las mejores zonas de todo el viaje para él: sin cocodrilos, sin hipopótamos, sin bilharzia documentada y con campings junto al agua.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria sobre todo en el este y en cotas bajas (Akagera, Bugesera, Kirehe); riesgo bajo en Kigali, Musanze, los Volcanes y Nyungwe por altitud. Profilaxis a valorar con Sanidad Exterior según el itinerario exacto.",
        "Fiebre amarilla: certificado exigido si se procede de país endémico (Uganda, Kenia, Tanzania lo son).",
        "El lago Kivu es de los pocos grandes lagos africanos sin bilharzia documentada, sin cocodrilos y sin hipopótamos: se puede nadar. No es el caso del lago Victoria ni del Muhazi, donde sí conviene abstenerse.",
        "Altitud: se vive por encima de los 1.500 m casi todo el tiempo y los volcanes pasan de 3.700 m. El Karisimbi (4.507 m) exige vivac en altura.",
        "King Faisal Hospital (Kigali, privado) es una de las mejores referencias sanitarias de África oriental, junto con Nairobi; CHUK es el hospital universitario público. Evacuación a Nairobi para casos extremos.",
        "Sanidad pública notablemente organizada para la región y farmacias bien surtidas en Kigali y Musanze.",
    ],
    seguridad_intro=("Ruanda es, con diferencia, el país más seguro y ordenado de todo el bucle este: delincuencia muy baja, policía correcta, carreteras señalizadas y una limpieza que sorprende. "
                     "Los dos únicos condicionantes reales son la frontera occidental con RD Congo, que no se toca, y la necesidad de comportarse con respeto absoluto en todo lo relacionado con el genocidio."),
    seguridad=[
        "FRONTERA OCCIDENTAL CON RD CONGO: el este congoleño (Goma, Bukavu, Kivu Norte y Sur) tiene conflicto armado activo. Gisenyi y Rusizi son seguras del lado ruandés, pero no se cruza bajo ningún concepto y conviene consultar la situación del momento antes de acampar pegado a la frontera.",
        "Delincuencia común muy baja, incluso de noche en Kigali. Prudencia estándar y nada más.",
        "MEMORIA DEL GENOCIDIO: no se bromea con el tema, no se pregunta a nadie si es hutu o tutsi (la mención étnica está proscrita en el discurso público), no se fotografía dentro de los memoriales y no se vuela un dron sobre ellos. Es un asunto de respeto elemental y también de ley.",
        "Fotografía: evitar fotografiar instalaciones militares, policía, edificios gubernamentales y el aeropuerto. Se aplica.",
        "Umuganda (último sábado de mes, 8:00-11:00): tráfico detenido y comercios cerrados. No es una recomendación, es una obligación legal que afecta también a los extranjeros circulando.",
        "Bolsas de plástico: requisadas en frontera. Es una norma que se aplica sistemáticamente y con registro de equipaje.",
        "Conducción: carreteras excelentes pero de montaña, con mucha niebla en Nyungwe y en los pasos altos, peatones y bicicletas en el arcén a todas horas, y controles de velocidad reales. No conducir de noche fuera de ciudad, criterio general del proyecto.",
        "Libertad de expresión: el debate político interno es un terreno delicado. Evitar discusiones públicas sobre política interna y sobre el papel de Ruanda en RD Congo.",
    ],
    agua=[
        "Kigali, Musanze, Rubavu, Karongi, Rusizi y Huye: agua embotellada sin problema en supermercados.",
        "Recarga del depósito de uso general: campings y lodges del Kivu (Gisenyi, Kinunu, Karongi) y de Musanze permiten llenar con manguera.",
        "El agua de red en Kigali es de mejor calidad que la media regional, pero el criterio del proyecto sigue siendo potabilizar siempre.",
        "El lago Kivu es apto para bañarse y para uso general previo tratamiento; el lago Muhazi y los lagos del Akagera, no.",
    ],
    combustible=[
        "Ruanda es un país pequeño con red densa: Kigali, Musanze, Rubavu, Karongi, Rusizi, Huye, Nyanza, Kayonza y Nyagatare tienen estaciones formales (SP, Engen, Rubis, Kobil). No hay ningún gap de 500 km.",
        "Repostar a fondo antes de meterse en el CONGO NILE TRAIL: entre Gisenyi y Karongi por la pista de la orilla hay muy poca cosa y el consumo en pista de montaña se dispara.",
        "Repostar en Kayonza antes de entrar en AKAGERA: dentro del parque no hay surtidor.",
        "Repostar en Rusizi o en Gisakura antes de Nyungwe: la travesía de la selva es larga, de montaña y sin servicios.",
        "Precios del gasóleo regulados y estables; calidad buena para la región.",
    ],
    experiencias_intro=("Relatos y datos recogidos de la comunidad overland y de fuentes documentales. No son información oficial: contrastar siempre la fecha antes de confiar en un dato de frontera, pista o parque. "
                        "En esta revisión no se ha podido acceder a iOverlander ni a Tracks4Africa desde la sesión de trabajo, así que lo que sigue procede de fuentes documentales y del dosier canino del propio proyecto, y está marcado como tal:"),
    experiencias=[
        "LA BOLSA DE PLÁSTICO ES EL TEMA RECURRENTE: todo el que entra en Ruanda cuenta lo mismo — registro de equipaje en la frontera y confiscación de cualquier bolsa de plástico, incluidas las de la compra y las de basura. Para dos vehículos con meses de África encima es una reorganización real del almacenaje, no un detalle. La recomendación repetida es llegar con bolsas de tela y cajas, y vaciar los coches antes de la cola, no dentro de ella.",
        "El precio de los gorilas divide a la comunidad overland en dos: los que pagan los 1.500 USD de Ruanda porque la caminata es más corta y el acceso mucho mejor, y los que cruzan a Uganda a pagar 800. Nadie discute que el animal es el mismo y que la montaña es la misma. Para tres personas la diferencia son 2.100 USD.",
        "El Bisoke es la respuesta barata: prácticamente todo el que no paga el permiso de gorilas sube al monte Bisoke, y coincide en dos cosas — que el lago del cráter merece la pena, y que el barro de la bajada es legendario. Bastones y botas altas, no zapatillas.",
        "La sorpresa unánime es la calidad de las carreteras: asfalto impecable, señalización, arcenes, y una conducción civilizada que contrasta con todo lo anterior del viaje. El precio es que son carreteras de montaña continua: 100 km pueden ser tres horas.",
        "Umuganda pilla a mucha gente por sorpresa: el último sábado de mes, de 8 a 11, no se circula. Quien no lo sabe se queda parado en una barrera preguntándose qué pasa. Se planifica y ya está.",
        "El Congo Nile Trail está pensado para bicicleta y a pie, y quien lo intenta entero en 4x4 avisa de que hay tramos que no admiten vehículo. La fórmula que funciona es hacerlo por sectores, preguntando en cada pueblo, y combinar conducción con caminatas de un día.",
        "Akagera aparece como la sorpresa del país: casi nadie va a Ruanda por la fauna, y sin embargo el parque tiene los cinco grandes desde 2017, se recorre con el vehículo propio y está muchísimo menos masificado que cualquier parque keniano o tanzano, con un paisaje de lagos y papiros que no se parece a la sabana clásica.",
        "El memorial de Kigali es el sitio del que todo el mundo escribe después. El consejo repetido es reservar la mañana entera, coger la audioguía y no programar nada después. La sala de los niños es lo que nadie olvida.",
        "Perro (dosier del proyecto): entrada PROBABLE y previsiblemente el trámite más limpio de África central por la eficiencia administrativa del país. La orilla del Kivu es una de las mejores zonas de todo el viaje para el animal: sin cocodrilos, sin hipopótamos y sin bilharzia documentada.",
        "Kigali como parada técnica: talleres, recambios, veterinarios, hospitales de nivel y supermercados bien surtidos. Después de meses de África central, es el sitio donde la gente repara, repone y respira.",
    ],
    pendientes=[
        ("DECISIÓN DE FONDO", "Decidir si el bloque Uganda+Ruanda entra: Ruanda son unos 1.100 km y 9-12 días adicionales. Se decide junto con Uganda, con el calendario real al llegar a Kenia"),
        ("Gorilas: Uganda o Ruanda", "LA DECISIÓN ECONÓMICA DEL DESVÍO. 1.500 USD/persona en Ruanda frente a 800 en Uganda. Recomendación de esta ficha: trekking en Uganda; Ruanda para Nyungwe, Kivu, Akagera y Kigali. Confirmar ambas tarifas con RDB y UWA antes de cerrar"),
        ("Tarifas del RDB", "Confirmar con el Rwanda Development Board las tarifas vigentes para 2027 de gorilas (1.500 USD), monos dorados, Nyungwe con pasarela del dosel y entrada a Akagera"),
        ("Visado", "Decidir entre visado a la llegada en frontera (sin trámite) y Visado Turístico de África Oriental (100 USD, tres países): depende de si se hace Kenia+Uganda+Ruanda y de en qué país se emite primero"),
        ("Plástico", "Reorganizar el almacenaje de los dos vehículos en bolsas de tela y cajas ANTES de la frontera. Presupuestar tiempo extra en el puesto para el registro"),
        ("Umuganda", "Comprobar en qué sábado cae el último de cada mes durante la estancia y planificar las etapas para no quedarse parado de 8:00 a 11:00"),
        ("Congo Nile Trail", "Confirmar sobre el terreno qué tramos admiten vehículo y cuáles son solo de bici o a pie; preguntar en Gisenyi, Kinunu y Karongi en vez de forzar la pista"),
        ("Perro · permiso de importación", "Escribir a los servicios veterinarios ruandeses (RAB) pidiendo confirmación escrita de entrada terrestre y NOMBRANDO el puesto (Cyanika, Gatuna o Rusumo). Sigue en [PROBABLE] en el dosier canino"),
        ("Perro · base durante los parques", "Reservar alojamiento con patio en Musanze o en los lagos Burera/Ruhondo para los días de Volcanes, y en Gisakura para los de Nyungwe; organizar los turnos entre los tres viajeros"),
        ("Frontera de Gatuna", "Confirmar 72 h antes que sigue abierta (cerró entre 2019 y 2022) y comprobar el horario real de Cyanika, que no es 24 h"),
        ("Demarcación consular", "Confirmar qué embajada de España es competente para Ruanda (Nairobi o Kampala) y anotar el teléfono de emergencia correcto antes de entrar"),
        ("Norma de vehículos sucios", "Confirmar el alcance real de la normativa municipal de limpieza de vehículos en Kigali antes de darla por buena o descartarla"),
        ("FOTOGRAFÍAS", "En esta revisión NO se pudo acceder a commons.wikimedia.org desde la sesión (bloqueo de red), así que solo dos PDIs llevan foto verificada. Pendiente: completar los nombres de archivo de Wikimedia Commons de los 16 PDIs restantes, verificándolos uno a uno. No inventarlos"),
    ],
    sources=SOURCES,
    sources_note=("Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. "
                  "RUANDA ES UNA ALTERNATIVA: no está en la ruta fija y va emparejada con Uganda. Las tarifas de permisos y visados son las últimas conocidas y hay que revalidarlas con el Rwanda Development Board y con Inmigración antes de comprometer nada."),
    emergency="Sin representación española propia en Ruanda — gestionar emergencias a través de la Embajada de España competente (Nairobi, Kenia; confirmar demarcación vigente): +254 20 272 02 22/3/4/5; emergencia consular +254 733 63 11 44. Emergencias locales en Ruanda: policía 112, ambulancia 912, bomberos 111.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

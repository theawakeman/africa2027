# -*- coding: utf-8 -*-
"""Nigeria — ficha completa, corredor doble bajada/subida (12 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== BAJADA: Sèmè/Kraké -> Badagry -> Lagos -> Benin City -> Asaba/Onitsha -> Calabar -> Ikom -> Mfum/Ekok =====
    dict(n=1, name="Badagry · Ruta de los Esclavos y Punto de No Retorno", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="½–1 día",
         lat=6.4150, lon=2.8814,
         desc="Primer pueblo nigeriano después de la frontera de Sèmè-Kraké y uno de los grandes lugares de memoria de la trata atlántica en África occidental. Aquí se concentran el Badagry Heritage Museum (en el antiguo edificio del distrito colonial), la Brazilian Barracoon de los Seriki Abass —celdas de esclavos conservadas con los grilletes, los cuencos y los objetos de trueque—, el pozo de la «atenuación de la memoria» y la Ruta de los Esclavos: el camino de unos 2 km que los cautivos recorrían hasta la laguna, se cruzaba en piragua y terminaba en la playa del Atlántico, en el llamado Punto de No Retorno. Badagry es también donde se predicó el primer sermón cristiano de Nigeria (1842) y donde se levantó la primera escuela primaria del país. Se visita con guía local; la travesía de la laguna hasta la playa se hace en barca de motor. Parada perfecta para el primer día del país, a solo 20 km del paso fronterizo y 60 km de Lagos.",
         credit="Wikimedia Commons", source=W + "Point%20of%20No%20Return%20Beach%20in%20Badagry%20Lagos.%20Nigeria.jpg?width=900"),
    dict(n=2, name="Lagos · megaciudad, mercados y música", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=6.4541, lon=3.3947,
         desc="Unos 20 millones de habitantes, la mayor aglomeración de África subsahariana y la mejor base logística de todo el golfo de Guinea: puerto, aeropuerto internacional, consulado general de España, talleres, recambios, neumáticos y cualquier pieza imaginable en el mercado de Ladipo (el mayor mercado de repuestos de automoción de África occidental). Es también la capital cultural de la región: el afrobeats sale de aquí, y el New Afrika Shrine de Ikeja —regentado por la familia de Fela Kuti— sigue programando conciertos en vivo; el Freedom Park de Lagos Island, antigua cárcel colonial convertida en centro cultural, es la versión tranquila de lo mismo. Mercados de Balogun y Lekki Arts & Crafts, National Museum en Onikan, y la vida acomodada de Victoria Island e Ikoyi, donde están los hoteles con aparcamiento cerrado. El tráfico («go-slow») es legendario: nada se mueve entre las 6:30 y las 10:00 ni entre las 16:00 y las 20:00.",
         credit="Wikimedia Commons", source=W + "Lagos%20skyline.jpg?width=900"),
    dict(n=3, name="Lekki Conservation Centre", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido", time="½ día",
         lat=6.4432, lon=3.6011,
         desc="78 hectáreas de humedal y bosque de manglar conservadas por la Nigerian Conservation Foundation dentro de la propia ciudad, en la península de Lekki. Su seña de identidad es la pasarela colgante de dosel más larga de África (unos 400 m en seis tramos, hasta 22 m de altura), además de torres de observación, una sabana con monos mona, cocodrilos y más de 150 especies de aves. Es la mejor pausa verde de Lagos y una forma de estirar las piernas sin salir de la ciudad. Abre a diario en horario de día, con entrada de pago. Perro: no hay norma publicada pero es un centro de conservación con fauna suelta — darlo por prohibido y dejarlo en el alojamiento.",
         credit="Ashinze · CC BY-SA 4.0", source=W + "LEKKI%20CONSERVATION%20CENTRE%20LAGOS%2C%20NIGERIA%20(LCC)%2006.jpg?width=900"),
    dict(n=4, name="Benin City · Palacio del Oba, bronces y murallas", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=6.3350, lon=5.6037,
         desc="Capital del reino de Benín, uno de los Estados africanos más sofisticados de la historia, que en el siglo XVI asombró a los portugueses por su tamaño, su orden y su alumbrado público. De él salieron los célebres «bronces de Benín», millares de placas y cabezas de latón fundidas a la cera perdida que los británicos saquearon en la expedición punitiva de 1897 y que hoy están en el centro de la mayor disputa de restitución patrimonial del mundo. El Palacio del Oba sigue siendo sede activa de la monarquía edo y se visita con guía; el Museo Nacional de Benin City, en la rotonda de King's Square, conserva piezas originales; el barrio de Igun Street mantiene vivo el gremio de fundidores de bronce desde hace siglos y está en la lista indicativa de la UNESCO. La ciudad está rodeada además por las murallas y fosos de Benín (Iya), un sistema de terraplenes de miles de kilómetros construido entre los siglos XIII y XV, hoy en gran parte devorado por el crecimiento urbano pero todavía identificable en tramos. ATENCIÓN: el nuevo Museum of West African Art (MOWAA) abrió su Pavilion en noviembre de 2025 en medio de una disputa abierta con la corte del Oba y con el gobierno del estado de Edo — confirmar si está abierto al público antes de contar con él.",
         credit="Kelechukwu Ajoku · CC BY-SA 4.0", source=W + "Royal%20Palace%20of%20the%20Oba%20of%20Benin%20cropped.jpg?width=900"),
    dict(n=5, name="Cruce del Níger · puente de Asaba-Onitsha", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche (Asaba)",
         lat=6.1833, lon=6.7500,
         desc="El gran hito geográfico de la travesía: el río Níger, el tercero más largo de África, se cruza aquí por el puente de Onitsha (1,4 km, inaugurado en 1965 y destruido parcialmente durante la guerra de Biafra) o por el Segundo Puente del Níger, terminado en 2023, que descarga buena parte del tráfico. Onitsha, en la orilla este, alberga el Onitsha Main Market, considerado el mayor mercado de África occidental; Asaba, en la orilla oeste, es una ciudad tranquila y moderna con hoteles de aparcamiento cerrado y es, según los overlanders que han hecho esta ruta, la pernocta natural del tramo. REGLA OPERATIVA: la orilla este es ya el Sureste igbo, donde los lunes de «sit-at-home» impuestos por el IPOB paralizan la región — cruzar el Níger cualquier día menos lunes. NO fotografiar el puente: es infraestructura estratégica y hay control militar permanente.",
         credit="Wikimedia Commons", source=W + "Lagos%20Ibadan%20express%20way.jpg?width=900"),
    dict(n=6, name="Calabar", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=4.9589, lon=8.3269,
         desc="La ciudad más agradable y ordenada del sur de Nigeria, y la mejor parada de descanso del corredor de bajada: calles arboladas, colinas sobre el estuario del río Cross, poca presión de tráfico y una tradición de gestión urbana que la ha convertido en la excepción del país. Antiguo puerto de la trata atlántica (Old Calabar), conserva el Slave History Museum en el Marina Resort, el Museo Nacional en la antigua residencia del gobernador británico (1884) y la memoria del protectorado del río Oil. En diciembre acoge el Carnaval de Calabar, «el mayor espectáculo callejero de África», con un mes de desfiles. Es la última gran plaza de servicios antes de Camerún: bancos con cajeros, hospital universitario (UCTH), supermercados, talleres y combustible garantizado.",
         credit="Otomeonoge · CC BY-SA 4.0", source=W + "Calabar%20carnival%209.jpg?width=900"),
    dict(n=7, name="Drill Ranch de Calabar (Pandrillus)", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="½ día",
         lat=4.9700, lon=8.3400,
         desc="El centro urbano del proyecto Pandrillus, fundado en 1991 y responsable del mayor programa de rescate y cría en cautividad de drills (Mandrillus leucophaeus) del mundo: el primate más amenazado de África, que solo vive en el sureste de Nigeria, el suroeste de Camerún y la isla de Bioko. Del puñado de animales confiscados al tráfico de carne de monte han pasado a varios centenares nacidos en el programa, en grupos sociales grandes. En Calabar está el centro de acogida y educación —la parte urbana, visitable en media mañana—, mientras que el grueso de la población vive en el rancho de la montaña de Afi. Pandrillus gestiona además un santuario de chimpancés en el mismo recinto. Visitas con cita previa y donativo; el dinero va directamente al programa. PERRO: no se puede entrar — riesgo de transmisión de enfermedades a los primates.",
         credit="Wikimedia Commons", source=W + "Drill%20(Mandrillus%20leucophaeus).jpg?width=900"),
    dict(n=8, name="Parque Nacional de Cross River · división de Oban", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=5.3500, lon=8.6500,
         desc="El bloque de selva tropical mejor conservado de Nigeria y uno de los focos de biodiversidad más importantes de África occidental: unos 3.000 km² en la división de Oban (más los 1.000 de Okwangwo, al norte), continuación directa del Parque Nacional de Korup, en Camerún, al otro lado de la frontera. Alberga el gorila de Cross River (Gorilla gorilla diehli), la subespecie de gorila más amenazada del planeta —quedan unos 250-300 individuos en total, repartidos entre Nigeria y Camerún—, el chimpancé de Nigeria-Camerún, el drill, el elefante de bosque y más de 1.500 especies de plantas. El conjunto Cross River-Korup-Takamanda (CRIKOT) está inscrito en la lista indicativa de la UNESCO como candidatura transfronteriza. Acceso desde la carretera Calabar-Ikom por Akamkpa y Aking/Old Ekuri; el turismo está muy poco desarrollado y la visita es caminata de selva cerrada con guía comunitario, no safari: ver un gorila es prácticamente imposible, pero el bosque y las aves lo justifican. Gestiona el Nigeria National Park Service; confirmar tasas y guías en la oficina de Akamkpa.",
         credit="Wikimedia Commons", source=W + "Agbokim%20Waterfalls%20Ikom%20Cross%20River%20State%20Nigeria.jpg?width=900"),
    dict(n=9, name="Monolitos de Alok / Ikom", cat="Patrimonio UNESCO", prio="Media", dog="permitido", time="½ día",
         lat=6.0500, lon=8.7200,
         desc="Más de 300 monolitos de basalto tallados, de entre medio metro y casi dos de altura, dispuestos en círculos en una treintena de aldeas de la comarca de Ikom (Alok, Nkarasi, Emangabe, Nnam...). Están cubiertos de rostros estilizados, espirales y signos geométricos —el «akwanshi» de los pueblos bakor— cuya datación sigue discutida (se barajan desde el siglo XVI hasta fechas muy anteriores) y cuyo significado exacto se desconoce: se han interpretado como retratos de antepasados, marcadores de linaje e incluso como un sistema de escritura no descifrado. Es uno de los conjuntos megalíticos más singulares de África y está en la lista indicativa de la UNESCO desde 2007, pero permanece prácticamente sin protección: muchos han sido robados, quemados en desbroces agrícolas o desplazados. Se visita en la aldea de Alok, a unos 15 km al norte de Ikom, con propina al jefe del pueblo. Al aire libre y fuera de parque: se puede ir con el perro. Coordenada aproximada: confirmar sobre el terreno en Ikom.",
         credit="Wikimedia Commons", source=W + "Agbokim%20Waterfalls%20Ikom%20Cross%20River%20State%20Nigeria.jpg?width=900"),
    dict(n=10, name="Cataratas de Agbokim", cat="Naturaleza", prio="Alta", dog="permitido con precaución", time="½ día",
         lat=5.9069, lon=8.9128,
         desc="A 25 km de Ikom y apenas 15 de la frontera de Mfum/Ekok, el río Manyu se abre en siete brazos que se despeñan a la vez sobre un anfiteatro de selva: la caída mayor ronda los 75 m y en la estación húmeda el conjunto levanta una nube de agua permanente con arcoíris casi continuos. Es la última parada natural de Nigeria antes de entrar en Camerún y una de las pocas cascadas del país realmente accesibles en vehículo. Hay un mirador superior, escalones de bajada hasta la base y un pequeño recinto con tasa de entrada del estado de Cross River; las instalaciones turísticas están abandonadas o a medias, pero la cascada no. Buen sitio para bañar y airear al perro antes del cruce, con correa: los escalones mojados y la roca del borde son peligrosos. El mejor momento es el final de la estación de lluvias (septiembre-noviembre).",
         credit="Wikimedia Commons", source=W + "Agbokim%20Waterfalls%20Ikom%20Cross%20River%20State%20Nigeria.jpg?width=900"),
    # ===== SUBIDA: Mfum/Ekok -> Ikom -> Afi -> Obudu -> Abakaliki -> Enugu -> Asaba -> Benin City -> Osogbo -> Ibadan -> Abeokuta -> Idiroko =====
    dict(n=11, name="Montaña de Afi · santuario de drills y gorilas de Cross River", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="1–2 noches",
         lat=6.2833, lon=8.9667,
         desc="104 km² de selva de montaña en el norte de Cross River, con picos rocosos de hasta 1.300 m, declarados santuario de fauna en 2000. Es uno de los cuatro o cinco lugares del mundo donde sobrevive el gorila de Cross River, además de chimpancés de Nigeria-Camerún y drills en libertad. En el flanco sur, junto a la aldea de Buanchor, está el Afi Mountain Drill Ranch de Pandrillus: el mayor grupo de drills en semilibertad del planeta, en recintos de selva de varias hectáreas, más un grupo de chimpancés rescatados. Tiene cabañas rústicas, una pasarela de dosel de 25 m de altura y —el dato más asombroso del sitio— la mayor dormida invernal de golondrina común (Hirundo rustica) conocida de África: se han estimado hasta 20 millones de aves entrando a dormir a la vez en los cañaverales del valle entre noviembre y febrero, un espectáculo comparable a cualquiera del continente. Está listado en iOverlander como campamento establecido, es decir, se puede pernoctar con los vehículos. Acceso por pista desde la carretera Ikom-Obudu. PERRO: descartado dentro del rancho por bioseguridad; hay que dejarlo con un viajero en el aparcamiento o en Ikom.",
         credit="Wikimedia Commons", source=W + "Drill%20Monkey.jpg?width=900"),
    dict(n=12, name="Meseta de Obudu (Obudu Mountain Resort)", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=6.3700, lon=9.3700,
         desc="Antiguo rancho ganadero colonial de 1951 reconvertido en resort de montaña a unos 1.600 m de altitud, sobre una meseta de praderas y bosque de niebla en la frontera con Camerún. El clima es fresco de verdad —puede bajar de 10 °C de noche, algo inimaginable en el resto de Nigeria—, hay cascadas (Kwa Falls, Becheve), senderos por la meseta, un teleférico de 4 km y la carretera de acceso: 11 km de asfalto con 22 curvas de herradura y más de 1.000 m de desnivel, uno de los tramos de conducción más espectaculares de África occidental. Es la gran parada de descanso del corredor de subida y el único sitio del país donde se duerme con manta. El resort ha pasado por periodos de abandono y de reforma: confirmar que está operativo antes de contar con él, y si no, hay alojamiento sencillo en Obudu pueblo. Coordenada aproximada de la meseta — verificar la del resort sobre el terreno.",
         credit="Bassnificient · CC BY-SA 4.0", source=W + "Obudu%20Mountain%20Resort%2002.jpg?width=900"),
    dict(n=13, name="Bosque Sagrado de Osun-Osogbo (UNESCO)", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=7.7581, lon=4.5586,
         desc="75 hectáreas de bosque denso a orillas del río Osun, Patrimonio Mundial de la UNESCO desde 2005 y uno de los últimos bosques sagrados de la religión yoruba que se conservan intactos: es el santuario de la diosa Osun, divinidad de la fertilidad y de las aguas. Lo que lo hace único no es solo su antigüedad, sino la intervención de la artista austríaca Susanne Wenger («Adunni Olorisa»), que desde los años cincuenta y hasta su muerte en 2009 reconstruyó los santuarios y llenó el bosque de esculturas monumentales de hormigón y hierro de una fuerza extraordinaria, mezclando el panteón yoruba con su propio lenguaje plástico. Hay cuarenta santuarios, esculturas, puntos de culto activos y sacerdotisas en funciones. El festival anual de Osun-Osogbo (agosto, dos semanas) es la mayor manifestación religiosa yoruba viva del mundo y atrae a la diáspora de Brasil, Cuba y Estados Unidos. Se visita con guía del santuario; hay normas de respeto estrictas en las zonas de culto.",
         credit="Auskid1215 · CC BY-SA 4.0", source=W + "Osun-Osogbo%20Sacred%20Grove%2C%20Osun%20State.jpg?width=900"),
    dict(n=14, name="Ibadan", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=7.3775, lon=3.9470,
         desc="La segunda ciudad de Nigeria y, durante buena parte del siglo XX, la mayor ciudad del África negra: una extensión inabarcable de tejados de cinc oxidado sobre siete colinas, que es en sí misma una de las vistas más características del país (mejor desde Bower's Tower, la torre-mirador de Oke-Are). Fue capital de la Región Occidental y capital intelectual del país: la Universidad de Ibadan, fundada en 1948, es la más antigua de Nigeria, y su campus arbolado con el zoológico y el jardín botánico es un oasis. El Cocoa House (1965), primer rascacielos del África occidental, se levantó con el dinero del cacao yoruba; el Mapo Hall, ayuntamiento colonial de 1929 en lo alto de su colina, domina el casco viejo. Buena plaza de servicios, hospital universitario (UCH) de referencia nacional y ambiente notablemente más tranquilo que Lagos. Es la pernocta lógica entre Osogbo y Abeokuta.",
         credit="Wikimedia Commons", source=W + "Cocoa%20House%2C%20Ibadan-Nigeria.jpg?width=900"),
    dict(n=15, name="Abeokuta y la roca de Olumo", cat="Cultura", prio="Alta", dog="permitido con precaución", time="½–1 día",
         lat=7.1517, lon=3.3489,
         desc="Abeokuta significa literalmente «bajo la roca», y la roca es esta: un macizo de granito de 137 m que en el siglo XIX sirvió de fortaleza natural a los egba huidos de las guerras yoruba, que se escondían en sus grietas y cuevas. Se sube por una escalera tallada —o por un ascensor moderno, cuando funciona— entre las cavidades donde se refugiaban las familias, los árboles sagrados y las sacerdotisas que aún atienden el santuario de Olumo; desde arriba se domina toda la ciudad y el río Ogun. Abeokuta es además una de las ciudades históricas más densas de Nigeria: cuna de Wole Soyinka (primer Nobel de Literatura africano), de Fela Kuti y de dos presidentes, con la iglesia de San Pedro de Ake (1898), el Centenary Hall y los talleres de tinte índigo adire, la gran tradición textil egba. Última parada antes de la frontera de Idiroko. El perro puede acompañar en el exterior y en la base de la roca, con correa: la subida es de roca desnuda y escalones desiguales.",
         credit="Wikimedia Commons", source=W + "Olumo%20Rock%20in%20Abeokuta%2C%20Ogun%20State-Nigeria.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "patrimonio unesco": "marron", "cultura": "morado",
              "ciudad · servicios": "azul", "costa": "turquesa"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada bajada — Sèmè-Kraké (desde Benín)", "Frontera", 6.3697, 2.7275,
     "El paso terrestre más transitado de África occidental, hoy convertido en puesto fronterizo conjunto (Joint Border Post) con instalaciones nuevas, lo que según los overlanders que lo han cruzado recientemente ha eliminado buena parte de los intermediarios y del caos anterior. Secuencia real: control sanitario (cartilla de fiebre amarilla; pueden pedir cólera y meningitis), salida de Benín —que suele llevar más tiempo que la entrada en Nigeria—, inmigración nigeriana con escaneo del código QR de la landing card, biometría de huellas y, por separado, aduana para el vehículo. El e-Visa nigeriano SÍ se acepta aquí (cruces documentados). Llevar todo impreso además de en digital. Horario diurno; llegar temprano."),
    ("Frontera · Salida bajada — Mfum/Ekok (hacia Camerún)", "Frontera", 5.9450, 9.0600,
     "Único paso terrestre asfaltado y con aduana plena entre Nigeria y Camerún en el sur; cruce del río Cross hacia Ekok y Mamfe, ya en la región Suroeste camerunesa, en conflicto activo por la crisis anglófona. Salir de Ikom a primera hora para tener toda la jornada por delante al otro lado. Aquí se cierra el permiso de admisión temporal del vehículo de la Nigeria Customs Service: hay que presentar el vehículo y la declaración aduanera aprobada. Ver la alerta detallada y el protocolo en la ficha de Camerún antes de decidir este paso."),
    ("Frontera · Salida subida — Idiroko / Igolo (hacia Benín)", "Frontera", 6.7333, 2.8833,
     "Segundo paso Nigeria-Benín en importancia, a unos 100 km al norte de Sèmè, en el estado de Ogun. Elegido deliberadamente para que el corredor de subida no repita el eje costero de Lagos: mucho menos tráfico que Sèmè y acceso directo desde Abeokuta por Ilaro. Es, eso sí, un corredor con fama de contrabando intenso (arroz, combustible), lo que se traduce en más controles de aduana y policía en los kilómetros previos, no en más riesgo. POR CONFIRMAR: que la aduana de Idiroko esté habilitada para cerrar el permiso de admisión temporal del vehículo y sellar el CPD — si no lo estuviera, hay que salir por Sèmè."),
    ("Frontera · Entrada subida — Mfum/Ekok (desde Camerún)", "Frontera", 5.9450, 9.0600,
     "Mismo paso que la salida de la bajada, ahora en sentido inverso. Aquí se abre el segundo permiso de admisión temporal del vehículo y se presenta el segundo visado nigeriano (o la segunda entrada del visado múltiple). Repostar en Mamfe o Ekok es poco fiable: llegar con combustible desde Camerún y repostar en Ikom."),
    ("Consulado General de España en Lagos", "Consular", 6.4281, 3.4219,
     "21C Kofo Abayomi St, Victoria Island, Lagos. Tel. +234 (0)1 2094603499 · Emergencia consular 24 h: +234 803 360 1658. Es el punto consular útil del viaje: está en el corredor de bajada. La Embajada de España está en Abuya, fuera de la ruta."),
    ("Embajada de España en Abuya", "Consular", 9.0579, 7.4951,
     "Plot 493, Yedseram Street, Maitama, Abuya. Fuera del corredor previsto: solo se contempla un desplazamiento a Abuya en caso de emergencia consular grave, y atravesando el Middle Belt, que es precisamente lo que el itinerario evita."),
    ("Lagos University Teaching Hospital (LUTH) — Lagos", "Hospital", 6.5194, 3.3486,
     "Principal hospital universitario de Lagos y mejor capacidad del corredor para urgencias graves, junto con los hospitales privados de Victoria Island (Reddington, Lagoon). Coordenada urbana aproximada."),
    ("University of Calabar Teaching Hospital (UCTH)", "Hospital", 4.9550, 8.3400,
     "Hospital universitario de referencia del sureste y última capacidad hospitalaria seria antes de Camerún: a partir de Ikom y hasta Duala (Camerún) no hay nada equivalente. Coordenada urbana aproximada."),
    ("University College Hospital (UCH) — Ibadan", "Hospital", 7.4000, 3.8990,
     "El hospital universitario más antiguo y prestigioso de Nigeria, referencia del corredor de subida entre Benin City y la frontera de Idiroko. Coordenada urbana aproximada."),
    ("Stella Obasanjo / hospitales de Benin City", "Hospital", 6.3350, 5.6037,
     "Benin City es la única capacidad hospitalaria del tramo central (University of Benin Teaching Hospital, UBTH, en Ugbowo). Punto medio entre Lagos y Calabar. Coordenada urbana aproximada."),
    ("Mercado de repuestos de Ladipo — Lagos", "Servicio", 6.5400, 3.3300,
     "El mayor mercado de recambios de automoción de África occidental, en Mushin. Es donde conseguir cualquier pieza mecánica del viaje de bajada — y el sitio donde revisar los vehículos a fondo antes del bloque centroafricano, donde ya no hay nada equivalente hasta Duala. Ir acompañado de un mecánico de confianza, regatear y comprobar la pieza antes de pagar. Coordenada urbana aproximada."),
    ("Combustible · Lagos", "Combustible", 6.4541, 3.3947,
     "Mejor oferta y calidad del país (NNPC, TotalEnergies, Oando, Ardova, MRS). Desde la puesta en marcha de la refinería de Dangote, en la propia península de Lekki, el suministro del suroeste es mucho más estable que en los años de colas y desabastecimiento, pero el precio sigue moviéndose con frecuencia. Repostar a fondo aquí."),
    ("Combustible · Benin City / Asaba / Calabar", "Combustible", 6.3350, 5.6037,
     "Estaciones formales suficientes en todo el eje Lagos-Ore-Benin City-Asaba-Onitsha-Aba-Uyo-Calabar: no hay ningún hueco de 500 km en el corredor de bajada. Calabar es la última plaza con oferta amplia y garantizada."),
    ("Combustible · Ikom (último antes de Camerún)", "Combustible", 5.9667, 8.7000,
     "Última estación formal fiable antes de Mfum/Ekok y de todo el tramo camerunés de Mamfe-Kumba, donde el suministro puede estar interrumpido por la situación de seguridad. Salir de Ikom con depósitos y garrafas llenos."),
    ("Combustible · Ogoja / Abakaliki / Enugu (corredor de subida)", "Combustible", 6.3249, 8.1137,
     "Estaciones formales en el eje Ikom-Ogoja-Abakaliki-Enugu-Onitsha de la subida. Evitar comprar en bidones a pie de carretera: es práctica habitual en el norte de Cross River pero la calidad del gasóleo es imprevisible."),
    ("Agua potable y de uso general · Lagos, Benin City, Calabar", "Agua potable", 6.4541, 3.3947,
     "Agua embotellada y en bolsa («pure water») disponible en cualquier parte y a precio bajo. Para el depósito de uso general: estaciones de servicio grandes, hoteles con aparcamiento y el Marina Resort de Calabar permiten llenar con manguera; pedirlo en recepción y pagar la propina habitual."),
    ("Agua · Ikom y Obudu", "Agua potable", 5.9667, 8.7000,
     "Últimas recargas cómodas de cada corredor antes de los tramos de frontera. En el interior de Cross River el agua es de pozo o de perforación: tratarla siempre."),
]

DRONE_CALLOUT = ("warn", "Legal, pero con registro obligatorio y un historial de detenciones por volar sin papeles",
                  "La Nigeria Civil Aviation Authority (NCAA) regula los drones bajo la Parte 21 de las Nig.CARs: exige registro del aparato (documento «Recognition of Ownership» que debe acompañar cada vuelo), permiso de operación y, para cualquier uso que no sea estrictamente recreativo, licencia de piloto remoto. El régimen es real y se aplica: ha habido incautaciones en aduana y detenidos por volar sin autorización, y la normativa contempla multas altas y penas de hasta 3 años de prisión. A eso se suma el contexto de seguridad: un dron sobre un puente, un puerto, una refinería o un control militar se interpreta como reconocimiento hostil, no como turismo. Techo 120 m (400 ft), línea de vista, solo de día, nunca sobre aglomeraciones, agua, aeropuertos o instalaciones militares. Recomendación del proyecto: valorar seriamente NO volar en Nigeria, y en ningún caso hacerlo sin el registro tramitado.")

STARLINK_CALLOUT = ("ok", "Starlink operativo y consolidado — el mejor país del tramo atlántico para conectividad",
                     "Nigeria fue el primer mercado africano de Starlink (2023) y hoy es uno de los mayores del continente, con servicio residencial y móvil (Roam) plenamente comercializado, kits a la venta en tiendas y distribuidores locales, y acuerdos de servicio satélite-a-móvil con operadores nacionales anunciados a finales de 2025. Ha habido, eso sí, capacidad agotada («Sold Out») durante meses en las celdas más congestionadas —Lagos, Abuya, Port Harcourt— y varias subidas de precio en 2025-2026. Para nosotros lo relevante es que el terminal Roam funciona y que no hay hostilidad regulatoria: se puede entrar con la antena sin el problema que existe en Camerún. Revisar el mapa oficial y el estado de la celda 30-60 días antes.")

DOG_MATRIX = [
    ("Lagos, Benin City, Asaba, Calabar, Ibadan, Abeokuta (ciudades)", "permitido con condiciones",
     "Sin restricción legal identificada. Correa siempre puesta: el tráfico es el peligro real, y en los mercados y los atascos hay perros callejeros territoriales. Los hoteles con aparcamiento cerrado suelen aceptarlo pagando suplemento, pero conviene confirmarlo por teléfono antes de llegar. NUNCA dejarlo solo en el vehículo: calor húmedo permanente y riesgo de robo."),
    ("Badagry, cataratas de Agbokim, monolitos de Alok, exterior de Olumo Rock", "permitido con precaución",
     "Sitios al aire libre y fuera de parque nacional: son las mejores paradas del país con el perro. Correa obligatoria en la roca mojada de Agbokim (escalones verticales y corriente fuerte) y en la subida de Olumo. En Badagry, la travesía de la laguna en piragua hasta el Punto de No Retorno hay que negociarla con el barquero."),
    ("Meseta de Obudu", "permitido con condiciones",
     "Es el mejor sitio del país para el perro: fresco de verdad (puede bajar de 10 °C), praderas abiertas y senderos fuera de parque nacional. El resort tiene política propia de mascotas: confirmarlo por escrito antes de subir los 11 km de curvas. Cuidado con el ganado y con los perros de los pastores de la meseta."),
    ("Drill Ranch de Calabar y Afi Mountain (Pandrillus)", "prohibido",
     "Centros de rescate de primates con protocolos de bioseguridad: el riesgo de transmisión de enfermedades a drills y chimpancés hace impensable la entrada de un perro, aunque no haya un cartel que lo diga. PLAN B: turnos entre los tres viajeros — uno se queda con el perro en el aparcamiento de Buanchor o en el alojamiento de Calabar/Ikom. Confirmar por escrito con Pandrillus al pedir la cita."),
    ("Parque Nacional de Cross River (Oban y Okwangwo) y Lekki Conservation Centre", "no confirmado — tratar como prohibido",
     "El Nigeria National Park Service no publica una norma general sobre mascotas, pero se trata de hábitat de gorila de Cross River y de chimpancé: la prohibición es la práctica universal en este tipo de espacios. PLAN B: turnos, o sustituir la visita por las cataratas de Agbokim y la meseta de Obudu, que dan naturaleza equivalente sin el veto."),
    ("Norte de Nigeria, Middle Belt y delta del Níger", "zona excluida",
     "Excluidos del itinerario por seguridad, no por el perro. No aplica."),
]

SOURCES = [
    ("Nigeria Immigration Service · portal oficial del e-Visa", "https://evisa.immigration.gov.ng/"),
    ("Embajada de Nigeria en Madrid · requisitos del visado de turismo", "http://madrid.foreignaffairs.gov.ng/visas/tourist-visa/"),
    ("Scoot West Africa · cruce de Sèmè-Kraké con e-Visa nigeriano (procedimiento real, paso a paso)", "https://scootwestafrica.com/crossing-at-seme-krake-with-an-e-visa-for-nigeria/"),
    ("Destinali · viajar a Nigeria en vehículo propio: visado, carta de invitación y visado de llegada", "https://destinali.com/nigeria-overland/"),
    ("Federal Ministry of Information · la Nigeria Customs Service inicia la admisión temporal de vehículos personales (7 de enero de 2026)", "https://fmino.gov.ng/nigeria-customs-service-commences-implementation-of-safe-passage-for-personal-vehicles-under-temporary-admission/"),
    ("Rogue Wanderers · cruce de Nigeria en vehículo propio, día a día, con recuento de controles", "https://www.roguewanderers.com/blog/nigeria"),
    ("The Road Chose Me (Dan Grec) · controles y sobornos en Nigeria, con cámara oculta", "https://theroadchoseme.com/video-nigeria-roadblocks-and-bribery-hidden-camera"),
    ("TREAD Magazine · «Notorious Nigeria»: un mes cruzando Nigeria en overland", "https://www.treadmagazine.com/features/notorious-nigeria/"),
    ("RegionAlert · Nigeria 2026: corredores de secuestro, carreteras de bandidos y zonas seguras", "https://regionalert.com/blog/nigeria-travel-safety-2026.html"),
    ("Análisis de datos de secuestros en carreteras nigerianas 2019-2026", "https://adediranadeyemi.com/blog/nigeria-road-kidnapping-data.html"),
    ("Vanguard · el Reino Unido desaconseja viajar a 28 estados nigerianos por terrorismo y secuestro (agosto 2026)", "https://www.vanguardngr.com/2026/08/uk-warns-citizens-against-travel-to-28-nigerian-states-over-terrorism-kidnap-risk/"),
    ("The Guardian Nigeria · el «sit-at-home» del Sureste, cuatro años y medio después", "https://guardian.ng/saturday-magazine/c105-saturday-magazine/sit-at-home-order-southeast-and-the-road-to-recovery-four-and-half-years-after/"),
    ("UNESCO · Bosque Sagrado de Osun-Osogbo (Patrimonio Mundial)", "https://whc.unesco.org/en/list/1118/"),
    ("UNESCO · lista indicativa: Cross River – Korup – Takamanda (CRIKOT) National Parks", "https://whc.unesco.org/en/tentativelists/6204/"),
    ("WCS Nigeria · Parque Nacional de Cross River, división de Okwangwo", "https://nigeria.wcs.org/wild-places/cross-river-np-okwangwo.aspx"),
    ("Nigeria Park Service · Parque Nacional de Cross River", "https://nigeriaparkservice.gov.ng/blog/2014/08/12/cross-river-national-park/"),
    ("Pandrillus · Drill Ranch (Calabar y montaña de Afi)", "https://www.pandrillus.org/projects/drill-ranch/"),
    ("iOverlander · Afi Mountain Drill Ranch (campamento establecido)", "https://app.ioverlander.com/places/3858-afi-mountain-drill-ranch"),
    ("Wikipedia · Afi Mountain Wildlife Sanctuary", "https://en.wikipedia.org/wiki/Afi_Mountain_Wildlife_Sanctuary"),
    ("Wikipedia · Agbokim Waterfalls (coordenadas y descripción)", "https://en.wikipedia.org/wiki/Agbokim_Waterfalls"),
    ("Wikipedia · Ikom monoliths", "https://en.wikipedia.org/wiki/Ikom_monoliths"),
    ("British Museum · African Rock Art: los monolitos de Ikom", "https://africanrockart.britishmuseum.org/country/nigeria/ikom-monoliths%20/"),
    ("Wikipedia · Olumo Rock", "https://en.wikipedia.org/wiki/Olumo_Rock"),
    ("Wikipedia · Museum of West African Art (MOWAA), Benin City", "https://en.wikipedia.org/wiki/Museum_of_West_African_Art"),
    ("Apollo Magazine · qué ha pasado en el Museum of West African Art de Benin City", "https://apollo-magazine.com/museum-west-african-art-mowaa-protests-benin-city-oba/"),
    ("Global Press Journal · los museos y monumentos de la trata en Badagry", "https://globalpressjournal.com/africa/nigeria/history-atlantic-slave-trade-chronicled-museums-monuments-badagry-nigeria/"),
    ("TechCabal · Starlink en Nigeria: precios, planes y disponibilidad", "https://techcabal.com/2025/11/11/starlink-nigeria-price-and-availability/"),
    ("Drone-Laws.com · normativa de drones en Nigeria (NCAA)", "https://drone-laws.com/drone-laws-in-nigeria/"),
    ("NCAA · portal digital de regulación de drones", "https://ncaa.gov.ng/media/news/ncaa-launches-new-digital-drone-regulation-portal/"),
    ("MyGoToVet · permiso de importación/exportación de mascotas en Nigeria: autoridad, coste y plazos", "https://mygotovet.com/blog/pet-import-and-export-permitnigeria-cost-requirements-iYpD/NhgW95f6ge"),
    ("Consulado General de España en Lagos · contacto", "https://www.exteriores.gob.es/Consulados/lagos/es/Consulado/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx"),
    ("Logistics Cluster · evaluación del paso fronterizo de Sèmè (Nigeria-Benín)", "https://lca.logcluster.org/231-nigeria-seme-land-border-crossing"),
    ("A Little Off Track · cruce de Mfum/Ekok hacia Camerún", "https://www.alittleofftrack.com/overlanding-cameroon/"),
    ("iOverlander · puntos de combustible, agua y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Bajada: Sèmè -> Badagry -> Lagos -> Sagamu -> Ore -> Benin City -> Asaba -> Onitsha -> Owerri -> Aba -> Uyo -> Calabar -> Akamkpa -> Ikom -> Agbokim -> Mfum
CORRIDOR = [(6.3697, 2.7275), (6.4150, 2.8814), (6.4541, 3.3947), (6.4432, 3.6011), (6.8485, 3.6469),
            (6.7500, 4.8833), (6.3350, 5.6037), (6.1833, 6.7500), (6.1333, 6.7833), (5.4833, 7.0333),
            (5.1167, 7.3667), (5.0333, 7.9333), (4.9589, 8.3269), (5.3167, 8.3500), (5.3500, 8.6500),
            (5.9667, 8.7000), (6.0500, 8.7200), (5.9069, 8.9128), (5.9450, 9.0600)]

# Subida: Mfum -> Ikom -> Afi (Buanchor) -> Obudu meseta -> Ogoja -> Abakaliki -> Enugu -> Onitsha -> Asaba -> Benin City -> Ore -> Akure -> Ilesha -> Osogbo -> Ibadan -> Abeokuta -> Ilaro -> Idiroko
CORRIDOR_ALT = [(5.9450, 9.0600), (5.9667, 8.7000), (6.2833, 8.9667), (6.3700, 9.3700), (6.6500, 8.8000),
                (6.3249, 8.1137), (6.4402, 7.4944), (6.1333, 6.7833), (6.1833, 6.7500), (6.3350, 5.6037),
                (6.7500, 4.8833), (7.2500, 5.1950), (7.6167, 4.7333), (7.7581, 4.5586), (7.3775, 3.9470),
                (7.1517, 3.3489), (6.8833, 3.0167), (6.7333, 2.8833)]

CORRIDOR_LABEL = "Bajada"
CORRIDOR_ALT_LABEL = "Subida"

EXPERIENCIAS = [
    "El país con más controles de África occidental, y no es una impresión: los overlanders que han cruzado Nigeria de oeste a este llevan la cuenta. Rogue Wanderers registraron 21 paradas efectivas en la jornada Lagos-Asaba (450 km, 8 horas) y 20 más al día siguiente entre Asaba y Takum (468 km, 11 horas) — es decir, un control cada 20-25 km sostenido durante días. Son puestos de policía, ejército, aduanas, FRSC (seguridad vial), NDLEA (drogas), inmigración y vigilantes locales, a menudo apilados unos sobre otros a la entrada y la salida de cada población.",
    "Cómo se gestionan los controles, según quienes los han pasado: la técnica que describen todos coincide. Dan Grec (The Road Chose Me), que grabó decenas de ellos con cámara oculta, lo resume en «sonríe, sé educado y sé firme, y no hay ninguna razón para pagar»: llegar despacio con la ventanilla ya bajada, saludar primero, preguntar por el nombre y por la familia del agente, entregar la carpeta con las copias —nunca los originales— y no dar nunca la sensación de tener prisa ni de tener miedo. Un comentarista lo describió bien: «apenas les diste tiempo a hablar, estaban desbordados de amabilidad». Rogue Wanderers, por su parte, describen que aprendieron a distinguir el control serio del que no lo es: «si alguien no estaba bloqueando activamente el paso, simplemente seguíamos».",
    "Los sobornos no son inevitables. Es el punto en el que más insisten todos los relatos publicados: la petición de «something for the boys» o «anything for the weekend?» es constante, pero quienes cruzaron el país sin pagar nada son mayoría entre los overlanders que lo han contado. La versión de TREAD Magazine del cruce de Nigeria lo subtitula literalmente «cero sobornos pagados». La técnica es no negarse nunca de forma agresiva: se responde con humor, se ofrece agua o un caramelo, se pregunta por el recibo oficial si insisten, y se espera. Un agente le dijo a una pareja de overlanders que el permiso internacional de conducir no era válido: es falso, y no lo sostuvo.",
    "La escolta policial obligatoria: un gasto que hay que prever. Rogue Wanderers tuvieron que pagar una escolta policial obligatoria desde la frontera hasta Lagos a razón de 200 USD por persona. No parece una práctica universal ni sistemática, pero conviene llevar efectivo para el imprevisto y preguntar en la aduana si se va a exigir antes de que lo impongan como hecho consumado.",
    "Las distancias engañan: 450 km en 8 horas y 468 km en 11 horas son los tiempos reales medidos por overlanders en el eje sur, con autovía de cuatro carriles en buena parte del trayecto. La media efectiva en Nigeria se queda entre 40 y 50 km/h por la combinación de controles, tráfico pesado, baches y travesías de población. Planificar sobre 250 km/día es realista; sobre 400 no lo es.",
    "Asaba como pernocta clásica: quienes han hecho el eje Lagos-Camerún describen Asaba, en la orilla occidental del Níger, como la parada natural de la primera jornada: ciudad moderna, próspera, tranquila y con hoteles de aparcamiento cerrado. La acampada libre no se contempla: los relatos coinciden en que en Nigeria se duerme en hotel con recinto, y que es barato (hay guest houses de 5 USD en el interior).",
    "El combustible del interior se vende en botellas al borde de la carretera: es una escena universal en el Nigeria rural, y los overlanders que la describen coinciden en evitarla salvo emergencia — calidad imprevisible, adulteración frecuente. La regla que aplican es llenar siempre en la última estación formal de marca antes de un tramo rural, y llevar garrafas.",
    "Afi Mountain Drill Ranch está catalogado en iOverlander como «campamento establecido», es decir, un sitio donde se puede dormir con los vehículos. Es, junto con la meseta de Obudu, la única pernocta de verdadera naturaleza del itinerario nigeriano — el resto del país se duerme en ciudad.",
    "Los «do not travel» no son el país entero: varios overlanders señalan, con razón, la distancia entre los mapas de avisos oficiales y lo que se encuentra sobre el terreno en el sur. Rogue Wanderers lo formulan así: las zonas marcadas en rojo «son sitios donde vive gente; mujeres, niños y familias haciendo su vida diaria». Esto no invalida las exclusiones del norte y del delta —que son reales y están sostenidas por datos duros de secuestro—, pero sí explica por qué el corredor sur se recorre sin incidentes y por qué el recuerdo dominante de quienes lo han hecho es la hospitalidad, no el miedo.",
    "El arrepentimiento más repetido: no haber parado más. Casi todos los relatos de travesía rápida de Nigeria terminan igual — con la sensación de haber atravesado a toda prisa un país enorme y fascinante por culpa del miedo heredado y del visado corto. Es el argumento para nuestros 15 puntos de interés repartidos en dos corredores: cruzar rápido donde hay que cruzar rápido, pero no cruzar rápido todo.",
]

HISTORIA_RESUMEN = ("Nigeria es el país más poblado de África, un mosaico de más de 250 grupos étnicos forjado por fronteras coloniales británicas que unieron un norte musulmán haussa-fulani, un suroeste yoruba y un sureste igbo bajo un mismo Estado, cuyas fracturas desembocaron "
                     "en la guerra de Biafra (1967-1970); hoy es la mayor economía de África gracias al petróleo, aunque enfrenta desafíos de seguridad severos, en particular la insurgencia yihadista de Boko Haram en el noreste.")

HISTORIA_SECCIONES = [
    ("Reinos e imperios previos: Benín, los emiratos haussa y el califato de Sokoto",
     "El territorio albergó civilizaciones de gran sofisticación, entre ellas el reino de Benín (con su célebre arte en bronce, hoy objeto de disputas de restitución con museos europeos), la ciudad-estado yoruba de Ife, los emiratos haussa del norte y el califato de Sokoto, un poderoso Estado islámico fundado en 1804 tras la yihad de Usman dan Fodio."),
    ("El «Nigeria» de Lord Lugard y la amalgama colonial",
     "Gran Bretaña colonizó el territorio a finales del siglo XIX y, en 1914, el gobernador Frederick Lugard fusionó administrativamente los protectorados del norte y del sur en la colonia unificada de Nigeria, una «amalgama» puramente administrativa que unió bajo un mismo Estado a pueblos con religiones, lenguas y sistemas políticos muy distintos, sentando las bases de futuras tensiones interétnicas."),
    ("Independencia y la guerra civil de Biafra",
     "Nigeria se independizó en 1960. Tensiones étnicas y políticas entre el norte y el sureste igbo desembocaron en 1967 en la secesión de la autoproclamada República de Biafra y una guerra civil devastadora que se prolongó hasta 1970, con cientos de miles de muertos, muchos por hambruna, y que dejó una huella profunda en la memoria colectiva del país."),
    ("Situación actual: petróleo, Boko Haram y la mayor economía de África",
     "Tras décadas de gobiernos militares alternados con periodos civiles, Nigeria vive desde 1999 su periodo democrático más largo. El petróleo del delta del Níger sostiene la mayor economía de África, aunque con enormes desigualdades y contaminación ambiental severa en la región productora; desde 2009, la insurgencia yihadista de Boko Haram —y su escisión afín al Estado Islámico— mantiene un conflicto activo en el noreste, con episodios como el secuestro masivo de niñas de Chibok en 2014, un foco de inseguridad ajeno al eje sur/suroeste de este itinerario."),
]

HISTORIA_FUENTES = [
    ("BBC News · Nigeria country profile", "https://www.bbc.com/news/world-africa-13949550"),
    ("Encyclopaedia Britannica · Nigeria, History", "https://www.britannica.com/place/Nigeria/History"),
    ("Council on Foreign Relations · Boko Haram in Nigeria", "https://www.cfr.org/global-conflict-tracker/conflict/boko-haram-nigeria"),
]

SPEC = dict(
    slug="nigeria", name="Nigeria", revision="12 sep 2026",
    sub="País de tránsito · corredor doble bajada/subida · seguridad determinante · documentación · logística",
    chips=[
        ("BAJADA", "Sèmè/Kraké → Badagry → Lagos → Benin City → Asaba → Calabar → Ikom → Mfum/Ekok · ~1.135 km"),
        ("SUBIDA", "Mfum/Ekok → Afi → Obudu → Abakaliki → Benin City → Osogbo → Ibadan → Abeokuta → Idiroko · ~1.350 km"),
        ("PDIs", "15 puntos repartidos entre los dos corredores; solo Benin City y el eje Asaba-Onitsha se repiten"),
        ("SEGURIDAD", "Noreste, Noroeste, Middle Belt y delta del Níger: EXCLUIDOS. Corredor sur estrecho y sin desvíos"),
        ("CONTROLES", "el país con más controles de África occidental: ~1 cada 20-25 km. Carpeta de copias y paciencia"),
        ("A PIE", "roca de Olumo · senderos y cascadas de la meseta de Obudu · Agbokim · selva de Oban con guía"),
        ("VISADO", "e-Visa oficial, SÍ válido en frontera terrestre (Sèmè verificado) — carta de invitación exigida"),
        ("VEHÍCULO", "CPD + permiso de admisión temporal de la Nigeria Customs (90 días, desde enero de 2026)"),
        ("SEGURO", "Brown Card CEDEAO válida — última etapa antes del cambio a Carte Rose CEMAC en Camerún"),
        ("STARLINK", "activo y consolidado — el mejor país del tramo atlántico para conectividad"),
    ],
    center=[6.4, 6.0], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y de nuevo 72 h antes de cruzar por Sèmè/Kraké y antes de afrontar la salida por Mfum/Ekok hacia la región anglófona camerunesa.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Nigeria es un <strong>país de tránsito</strong>: se cruza dos veces, rápido y por el sur, porque la seguridad —no la logística— define el trazado. "
                   "Es también el país más grande, más poblado y más denso en servicios de todo el tramo atlántico, y cruzarlo en tres días sin ver nada sería un error: son ~1.100 km de ida y ~1.350 de vuelta, y hay material de sobra para una parada digna por jornada sin salirse del corredor seguro. "
                   "En la <strong>bajada</strong> se entra desde Benín por Sèmè/Kraké, se hace Badagry y Lagos, se cruza el país por la autovía del sur (Benin City, el puente del Níger en Asaba, Aba, Uyo) hasta Calabar, y se sale a Camerún por Ikom y Mfum/Ekok. "
                   "En la <strong>subida</strong> se vuelve a entrar por Mfum pero se sube al norte de Cross River —la montaña de Afi y la meseta de Obudu, lo mejor del país en naturaleza— y se atraviesa Nigeria por un eje más interior (Abakaliki, Enugu, Benin City, Osogbo, Ibadan, Abeokuta) para salir a Benín por una frontera distinta, <strong>Idiroko/Igolo</strong>, evitando repetir el embudo de Lagos. "
                   "Los dos corredores solo comparten Benin City y el paso del Níger por Asaba-Onitsha."),
    decision=("<strong>Por qué el corredor sur es la única opción razonable.</strong> Nigeria tiene cuatro conflictos activos simultáneos y ninguno de ellos está en el sur: "
              "(1) <strong>Noreste</strong> (Borno, Yobe, Adamawa): insurgencia de Boko Haram e ISWAP, con control territorial rural efectivo por parte de ISWAP y ataques deliberados contra organizaciones internacionales. "
              "(2) <strong>Noroeste y centro-norte</strong> (Zamfara, Katsina, Kaduna, Sokoto, Níger): bandidaje armado y <strong>secuestros masivos</strong> —más de 200 víctimas al mes en el arranque de 2026, según el seguimiento independiente—, con grupos que operan desde campamentos forestales y asaltan carreteras a plena luz del día. El eje Abuya-Kaduna acumula casi 2.000 víctimas de secuestro desde 2019. "
              "(3) <strong>Middle Belt</strong> (Plateau, Benue, Nasarawa, Taraba): conflicto agricultores-ganaderos que en los últimos años ha causado más muertos que Boko Haram, con picos en la estación seca (noviembre-marzo). "
              "(4) <strong>Delta del Níger</strong> (Rivers, Bayelsa, Delta, Akwa Ibom): secuestro con rescate ligado a la industria petrolera, sabotaje de oleoductos y piratería en las vías navegables y frente a la costa, más bloqueos comunitarios de carreteras que duran semanas. "
              "<strong>Queda por tanto un único corredor:</strong> la autovía del sur Lagos-Benin City-Asaba-Aba-Calabar y, para la vuelta, el eje interior Ikom-Abakaliki-Enugu-Benin City-Ibadan. "
              "Ese corredor no es «zona segura» en abstracto, pero es donde vive y circula la mayor parte del país, es asfalto continuo con estaciones de servicio y hospitales, y es el que han recorrido sin incidentes los overlanders cuyos relatos usamos como referencia. "
              "<strong>Matiz importante y honesto:</strong> el corredor de bajada cruza el borde del delta del Níger (Aba, Uyo) y ambos corredores cruzan el Sureste igbo, donde el IPOB impone los lunes de «sit-at-home» con ataques a vehículos que circulan. "
              "<strong>Protocolo del proyecto:</strong> (1) nunca circular en lunes por el Sureste —Onitsha, Enugu, Aba, Abakaliki—; (2) nunca conducir de noche en ningún punto del país; (3) los dos vehículos juntos y en contacto por radio; (4) nada de desvíos hacia el interior del delta ni hacia el norte; (5) salidas al amanecer y llegada al alojamiento antes de las 17:00; (6) efectivo repartido, no todo en el mismo sitio."),
    facts=[
        ("Papel en el viaje", "País de TRÁNSITO en los dos sentidos: se cruza rápido, sin turismo profundo, por razones de seguridad. Pero son ~2.500 km entre las dos pasadas: hay sitio para una parada digna por jornada."),
        ("Ventana prevista", "Bajada: tras Benín, antes de Camerún. Subida: desde Camerún hacia Benín, en el tramo de regreso."),
        ("Entrada bajada", "Sèmè/Kraké desde Benín: puesto fronterizo conjunto, el paso más transitado de África occidental. El e-Visa SÍ se acepta aquí."),
        ("Salida bajada", "Mfum/Ekok hacia Camerún, vía Ikom: único paso asfaltado del sur, pero entra en la región anglófona camerunesa en conflicto — ver ficha de Camerún."),
        ("Entrada subida", "Mfum/Ekok desde Camerún: no hay alternativa razonable en el sur."),
        ("Salida subida", "Idiroko/Igolo hacia Benín, desde Abeokuta: frontera distinta, deliberadamente, para no repetir el eje de Lagos."),
        ("Visado", "No hay visado de turismo en frontera. e-Visa oficial (evisa.immigration.gov.ng) con CARTA DE INVITACIÓN de un anfitrión nigeriano; se acepta en frontera terrestre. El «visa on arrival» NO se emite en la frontera de Sèmè: se emite en el aeropuerto de Lagos, con escolta de inmigración desde el paso."),
        ("Vehículo", "CPD más el nuevo Temporary Vehicle Admission Permit de la Nigeria Customs Service, en vigor desde el 7 de enero de 2026: 90 días prorrogables 30."),
        ("Seguridad", "Corredor sur estricto. Noreste, Noroeste, Middle Belt y delta del Níger EXCLUIDOS. Lunes prohibidos en el Sureste por el «sit-at-home» del IPOB."),
        ("Controles de carretera", "El país con más controles de África occidental: los overlanders cuentan ~20 paradas efectivas por jornada de 450 km. Carpeta de copias, francés no, inglés sí, y mucha paciencia."),
        ("Combustible", "Sin ningún hueco de 500 km en ninguno de los dos corredores. El suministro ha mejorado mucho con la refinería de Dangote, pero el precio se mueve constantemente."),
        ("Comunicaciones", "Starlink activo y consolidado, sin hostilidad regulatoria; SIM local (MTN, Airtel, Glo) con buena cobertura 4G en todo el corredor sur."),
    ],
    alerts=[
        "Visado: NO existe visado de turismo en la frontera. El e-Visa exige carta de invitación de un anfitrión o empresa nigeriana, extractos bancarios y reserva de alojamiento, y solo se puede solicitar desde el país de residencia — no sobre la marcha. Como el país se cruza dos veces con meses de diferencia, hay que resolver el segundo visado ANTES de salir de España o planificar su obtención en Camerún. Es el trámite más difícil de todo el tramo atlántico.",
        "Zona excluida — Noreste (Borno, Yobe, Adamawa): insurgencia activa de Boko Haram e ISWAP, con control rural efectivo y ataques dirigidos contra extranjeros y organizaciones internacionales. Sin excepción ni versión «con escolta».",
        "Zona excluida — Noroeste y centro-norte (Zamfara, Katsina, Kaduna, Sokoto, Níger): secuestros masivos en carretera y en escuelas, más de 200 víctimas al mes a principios de 2026. El eje Abuya-Kaduna es el corredor de secuestro más letal del país. Excluido, y con él la Embajada de España en Abuya como recurso práctico.",
        "Zona excluida — Middle Belt (Plateau, Benue, Nasarawa, Taraba): conflicto agricultores-ganaderos con masacres recurrentes, peor en estación seca. Esto excluye también la ruta alternativa Nigeria-Camerún por Takum/Mayo Ndaga/Gembu, que algunos overlanders han usado: es más bonita, pero atraviesa Taraba.",
        "Zona excluida — delta del Níger (Rivers, Bayelsa, Delta): secuestro con rescate, sabotaje y piratería fluvial y marítima. El corredor de bajada roza su borde oriental (Aba, Uyo) por la autovía: se atraviesa sin desviarse y sin parar más allá de lo imprescindible.",
        "Lunes de «sit-at-home» en el Sureste: desde 2021 el IPOB impone el cierre total de la actividad los lunes en Anambra, Imo, Abia, Enugu y Ebonyi, y ha habido ataques a vehículos que circulaban ese día. Aunque su observancia ha bajado, sigue vigente de facto. Planificar los cruces de Onitsha, Aba, Enugu y Abakaliki en martes, miércoles o jueves.",
        "Secuestro exprés en carretera: es el riesgo con más probabilidad real en el corredor sur. El patrón documentado es un retén falso o un vehículo atravesado en un tramo boscoso, con el asalto seguido de una retención corta hasta vaciar cuentas y tarjetas, o una retención larga con rescate. El 65 % de los ataques se produce en tramos rodeados de bosque y la inmensa mayoría de noche o al amanecer. Contramedidas: no conducir de noche NUNCA, no parar por señales de particulares, dejar mucha distancia con el vehículo de delante en tramos boscosos, y llevar dos móviles y efectivo repartido.",
        "Controles de carretera: no son un riesgo de seguridad sino de tiempo y de paciencia. Unos 20 por jornada larga. La petición de dinero es constante pero muy pocos overlanders han acabado pagando. Nunca discutir, nunca mostrar prisa, nunca entregar el pasaporte original si basta una copia.",
        "Escolta policial obligatoria: hay overlanders a los que se les ha impuesto una escolta policial de pago (200 USD por persona en un caso documentado) desde la frontera. Preguntar en la aduana si va a exigirse ANTES de que se plantee como hecho consumado, y llevar efectivo por si ocurre.",
        "Drones: legales pero con registro obligatorio ante la NCAA y un historial real de incautaciones y detenciones. Un dron sobre el puente del Níger, un puerto o una refinería se lee como reconocimiento hostil. Valorar seriamente no volar en Nigeria.",
        "MOWAA (Benin City): el nuevo Museum of West African Art abrió en 2025 en medio de una disputa abierta con la corte del Oba y con el gobierno estatal, con protestas en la inauguración y revocación del título de la parcela. Confirmar si está abierto al público antes de contar con él.",
    ],
    ruta_intro=("Nigeria se recorre dos veces por rutas que solo coinciden en un punto: Benin City y el paso del Níger. La <strong>bajada</strong> (~1.135 km) es el corredor costero clásico "
                "—frontera de Sèmè, Badagry, Lagos, autovía del sur hasta Benin City, cruce del Níger en Asaba, Aba, Uyo, Calabar— y sale a Camerún por Ikom y Mfum. La <strong>subida</strong> (~1.350 km) "
                "sube primero al norte de Cross River (montaña de Afi, meseta de Obudu: lo mejor del país en naturaleza y clima), cruza el Sureste por un eje más interior (Abakaliki, Enugu) y, a partir de "
                "Benin City, se va hacia el país yoruba —Osogbo, Ibadan, Abeokuta— para salir a Benín por Idiroko en vez de por Lagos. Etapas calculadas sobre una media de <strong>250 km/día</strong>, que "
                "en Nigeria es realista: los overlanders miden 450 km en 8 horas y 468 km en 11 por culpa de los controles y las travesías de población."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bajada 1 · Entrada y memoria", "Sèmè/Kraké → Badagry → Lagos", "~90 km · 1 día (la frontera se come la mañana)"),
        ("Bajada 2 · Base logística", "Lagos (Ladipo, Lekki, Freedom Park, New Afrika Shrine)", "0 km · 2-3 noches (revisión de vehículos)"),
        ("Bajada 3 · Autovía del sur", "Lagos → Sagamu → Ore → Benin City", "~320 km · 1-2 días"),
        ("Bajada 4 · Reino de Benín", "Benin City (Palacio del Oba, Igun Street, Museo Nacional)", "0 km · 1-2 noches"),
        ("Bajada 5 · Cruce del Níger", "Benin City → Asaba → Onitsha", "~110 km · 1 día (NUNCA en lunes)"),
        ("Bajada 6 · Borde del delta", "Onitsha → Owerri → Aba → Uyo → Calabar", "~330 km · 2 días, sin paradas evitables"),
        ("Bajada 7 · Calabar y la selva", "Calabar (Drill Ranch, museos) + incursión a Oban", "~100 km ida y vuelta · 2-3 días"),
        ("Bajada 8 · Hacia la frontera", "Calabar → Akamkpa → Ikom (monolitos de Alok)", "~250 km · 1 día"),
        ("Bajada 9 · Salida", "Ikom → cataratas de Agbokim → Mfum/Ekok", "~35 km · ½ día (salir a primera hora)"),
        ("Subida 1 · Primates y montaña", "Mfum/Ekok → Ikom → Buanchor (Afi Mountain Drill Ranch)", "~90 km · 1-2 días, pernocta en el rancho"),
        ("Subida 2 · Meseta de Obudu", "Afi → Ogoja → Obudu → meseta (11 km, 22 curvas)", "~180 km · 1-2 días, la única noche fresca del país"),
        ("Subida 3 · Sureste interior", "Obudu → Ogoja → Abakaliki → Enugu", "~280 km · 1-2 días (NUNCA en lunes)"),
        ("Subida 4 · Vuelta al Níger", "Enugu → Onitsha → Asaba → Benin City", "~250 km · 1-2 días"),
        ("Subida 5 · Al país yoruba", "Benin City → Ore → Akure → Ilesha → Osogbo", "~280 km · 2 días"),
        ("Subida 6 · Bosque sagrado", "Osun-Osogbo (UNESCO) → Ibadan", "~120 km · 1-2 días"),
        ("Subida 7 · Bajo la roca", "Ibadan → Abeokuta (roca de Olumo, adire)", "~80 km · 1 día"),
        ("Subida 8 · Salida", "Abeokuta → Ilaro → Idiroko/Igolo (frontera de Benín)", "~90 km · ½ día"),
    ],
    offroad=[
        "Aviso honesto: Nigeria NO es un país de 4x4 en el sentido del resto del proyecto. Los dos corredores previstos son asfalto casi continuo —autovía de cuatro carriles en buena parte del eje Lagos-Benin City— y el reto es el tráfico, los controles y los baches, no la tracción. Los tramos de pista que sí existen están en el norte y en el delta, que quedan excluidos por seguridad. Lo que sigue es lo que de verdad justifica llevar el 4x4 aquí.",
        "Subida a la meseta de Obudu (11 km, 22 curvas de herradura, >1.000 m de desnivel): el tramo de conducción más espectacular de Nigeria y uno de los mejores de África occidental. Está asfaltado, pero con pendientes fuertes, curvas ciegas y niebla frecuente en la parte alta: exigente con vehículos cargados y con los frenos. Bajar en marcha corta. Confirmar el estado del firme antes de subir: ha estado degradado en algunos periodos.",
        "Pista de acceso al Afi Mountain Drill Ranch (Buanchor, desde la carretera Ikom-Obudu): unos 15-20 km de laterita roja entre plantaciones y selva de montaña, con vados y tramos de barro profundo en lluvias. Es el único acceso 4x4 de verdad del itinerario nigeriano y da a un sitio donde además se puede pernoctar con los vehículos.",
        "Accesos al Parque Nacional de Cross River (división de Oban), desde Akamkpa y Aking/Old Ekuri: pistas forestales estrechas de laterita, con puentes de troncos en los ramales secundarios y barro serio en la estación húmeda. Sin guía comunitario no tiene sentido entrar: no hay señalización ni red de pistas cartografiada.",
        "Acceso a las cataratas de Agbokim desde la carretera Ikom-Mfum: pista corta de tierra hasta el recinto, practicable con cualquier vehículo en seco y resbaladiza en lluvias.",
        "Carretera Calabar-Akamkpa-Ikom (~250 km): asfalto en estado irregular que cruza el corredor forestal de Oban, con tramos hundidos y erosionados y muy poco tráfico comparada con la autovía del sur. Es la carretera más bonita del corredor de bajada.",
        "Estacionalidad: el sur de Nigeria tiene una estación húmeda larga (abril-octubre, con un pico en junio-julio y otro en septiembre) y una seca marcada por el harmatán (diciembre-febrero), con polvo sahariano que reduce mucho la visibilidad. Las pistas de Cross River solo son razonables en seco; en cambio las cataratas de Agbokim están en su mejor momento al final de las lluvias. Conflicto de calendario a resolver según cuándo caiga cada pasada.",
    ],
    senderismo=[
        "Roca de Olumo (Abeokuta): la excursión a pie más característica del país. Subida de 137 m por escalera tallada en el granito entre las grietas y cuevas donde se refugiaban los egba en el siglo XIX, con los árboles sagrados, el santuario todavía atendido y una vista completa sobre la ciudad y el río Ogun. Una hora larga; hay ascensor cuando funciona. Guía local obligatorio en la práctica.",
        "Senderos de la meseta de Obudu: la mejor caminata de Nigeria y la única en clima fresco. Recorridos por las praderas de altura, el bosque de niebla de Becheve (importante para aves endémicas del altiplano de Bamenda), las cascadas de la meseta y los miradores sobre la frontera camerunesa. Fuera de parque nacional, así que es también la mejor excursión larga compatible con el perro. Ropa de abrigo real: puede bajar de 10 °C.",
        "Pasarela de dosel del Afi Mountain Drill Ranch: recorrido a 25 m de altura por el dosel de la selva de montaña, más los senderos del valle. Entre noviembre y febrero, la entrada al dormidero de golondrinas al atardecer —hasta 20 millones de aves estimadas— es uno de los espectáculos naturales más extraordinarios de África occidental y se ve caminando desde el rancho.",
        "Pasarela colgante del Lekki Conservation Centre (Lagos): unos 400 m en seis tramos sobre el manglar, la más larga de África, hasta una torre de observación. Es senderismo urbano, pero rompe perfectamente los días de ciudad.",
        "Cataratas de Agbokim: mirador superior y bajada escalonada hasta la base de los siete brazos de agua. Corto pero resbaladizo; calzado con suela agarrada y correa para el perro.",
        "Selva de Oban (Parque Nacional de Cross River): caminatas de medio día a varios días con guía comunitario por selva primaria de tierras bajas — no es safari, es bosque cerrado, rastros, aves y árboles gigantes. Botas, sanguijuelas y humedad extrema. Hay campamentos comunitarios en Old Ekuri.",
        "Ruta de los Esclavos de Badagry: los ~2 km a pie desde la barracoon hasta el embarcadero de la laguna, más el tramo final por la playa hasta el Punto de No Retorno tras cruzar en barca. No es una excursión deportiva; es la caminata con más peso histórico de todo el tramo atlántico del viaje.",
        "Bower's Tower y campus de la Universidad de Ibadan: subida corta a la torre-mirador de Oke-Are para la vista del mar de tejados de cinc de Ibadan, y paseo largo por el campus arbolado de 1948 con su jardín botánico.",
    ],
    acampada=[
        "Regla general: en Nigeria NO se acampa libre. Todos los relatos de overlanders coinciden: se duerme en hotel o guest house con recinto cerrado y aparcamiento vigilado, que además es barato fuera de Lagos. La acampada al raso llamaría la atención de la policía en cuestión de minutos y es mala idea en un país con riesgo de secuestro exprés.",
        "Lagos: hoteles con aparcamiento cerrado en Victoria Island, Ikoyi y Lekki. Es lo más caro del país con diferencia, pero es la única fórmula sensata en una ciudad de 20 millones de habitantes. Dejar los vehículos donde haya vigilancia 24 h.",
        "Badagry: alojamientos sencillos junto al Marina y hacia la playa; permite hacer la visita con calma y salir hacia Lagos al día siguiente, evitando llegar a la megaciudad a última hora.",
        "Asaba (orilla oeste del Níger): la pernocta clásica del corredor de bajada según los overlanders — ciudad moderna, tranquila y con hoteles de aparcamiento cerrado. Preferible a Onitsha, que es mucho más caótica.",
        "Calabar: la mejor ciudad del país para pasar dos noches. Hoteles con jardín y aparcamiento, y el Marina Resort junto al río. Es donde conviene descansar de verdad antes de Camerún.",
        "Ikom: hoteles sencillos con patio, última pernocta antes de la frontera de Mfum. Salir de aquí al amanecer.",
        "Afi Mountain Drill Ranch (Buanchor): cabañas rústicas y —según iOverlander, que lo cataloga como campamento establecido— espacio para pernoctar con los vehículos. Es la única pernocta de naturaleza real del itinerario y merece la pena reservar por adelantado con Pandrillus.",
        "Meseta de Obudu: alojamiento en el resort (confirmar que está operativo) o en la propia meseta. La única noche fresca de todo Nigeria; manta necesaria.",
        "Ibadan y Abeokuta: hoteles urbanos con aparcamiento, notablemente más baratos y tranquilos que Lagos. Abeokuta es la última noche antes de la frontera de Idiroko.",
    ],
    visado=[
        "NO hay visado de turismo en la frontera. Es el trámite más difícil de todo el tramo atlántico del viaje y hay que resolverlo antes de salir de España.",
        "e-Visa oficial en el portal de la Nigeria Immigration Service (evisa.immigration.gov.ng). VERIFICADO: se acepta en la frontera terrestre de Sèmè/Kraké — hay cruces documentados por overlanders en 2024-2026, con escaneo del código QR de la landing card e impresión biométrica en el puesto.",
        "La CARTA DE INVITACIÓN de un anfitrión o empresa nigeriana es obligatoria para el visado de turismo, junto con pasaporte con 6 meses de validez y 2 páginas libres, dos fotos, extractos bancarios (piden entre 3 y 6 meses) y reserva de alojamiento o dirección del anfitrión. Sin carta de invitación no hay visado: hay que conseguirla de un hotel, de un operador local o de un contacto personal.",
        "Alternativa consular: Embajada de Nigeria en Madrid (visado de turismo estampado en pasaporte, tel. 91 571 11 60). SOLICITAR EXPRESAMENTE ENTRADA MÚLTIPLE y con vigencia larga, porque el país se cruza dos veces con varios meses de diferencia. Confirmar si el visado múltiple existe para turismo y cuál es su validez máxima.",
        "OJO con el «visa on arrival»: existe, pero NO se emite en la frontera de Sèmè. Requiere aprobación escrita previa del Comptroller General of Immigration y, en la práctica, un agente de inmigración escolta al viajero desde el paso terrestre hasta el aeropuerto de Lagos para estamparlo (unos 25.000 NGN de transporte). Además está clasificado como visado de negocios y exige carta de invitación de una empresa. No es una vía útil para nosotros.",
        "Solo se puede solicitar el visado nigeriano desde el país donde se tiene residencia permanente: tramitarlo sobre la marcha en Accra, Lomé o Cotonú es, según las fuentes especializadas, extremadamente difícil. Si el visado de entrada múltiple no cubre las dos pasadas, la única opción realista para la subida es la embajada de Nigeria en Yaundé (Camerún) — confirmar si expide a no residentes ANTES de salir de España, porque de ello depende todo el corredor de vuelta.",
        "Certificado internacional de fiebre amarilla exigido en el control sanitario de la frontera; también pueden pedir sellos de cólera y meningitis (los overlanders los describen como una tasa informal más que como un requisito).",
        "Llevar el e-Visa y la landing card impresos en buena calidad además de en el móvil, y muchas fotocopias del pasaporte y del sello de entrada para los controles de carretera.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Sèmè/Kraké (Benín)", "Puesto fronterizo conjunto, muy transitado pero ordenado desde su reforma. Secuencia: sanidad (fiebre amarilla) → salida de Benín (más lenta que la entrada) → inmigración nigeriana con QR de la landing card → biometría → aduana del vehículo. El e-Visa se acepta. Llegar a primera hora."),
        ("Salida bajada", "Mfum/Ekok (Camerún), vía Ikom", "Único paso asfaltado del sur hacia Camerún. Cierre del permiso de admisión temporal del vehículo: presentar vehículo y declaración aduanera aprobada. Salir de Ikom al amanecer para tener toda la jornada camerunesa por delante. NUNCA cruzar en lunes: al otro lado es día de «ciudad muerta» en la región anglófona."),
        ("Entrada subida", "Mfum/Ekok (desde Camerún)", "Mismo paso, sentido inverso. Segundo visado nigeriano y segundo permiso de admisión temporal del vehículo. No hay alternativa razonable en el sur: los pasos de Taraba (Takum, Mayo Ndaga, Gembu) atraviesan el Middle Belt en conflicto."),
        ("Salida subida", "Idiroko/Igolo (Benín), desde Abeokuta", "Elegido para no repetir el embudo de Lagos. Mucho menos tráfico que Sèmè, pero corredor de contrabando: más controles de aduana en los kilómetros previos. POR CONFIRMAR que la aduana de Idiroko cierra el permiso temporal del vehículo y sella el CPD; si no, salir por Sèmè."),
        ("Zona excluida", "Pasos del norte con Níger (Illela, Jibiya, Kamba) y con Chad", "No se contemplan: están en el Noroeste y el Noreste, en zona de bandidaje masivo y de insurgencia. Ninguna circunstancia los convierte en alternativa."),
        ("Alternativa descartada", "Takum / Mayo Ndaga / Gembu (hacia Banyo, Camerún)", "Ruta de montaña que algunos overlanders han usado y que evita la región anglófona camerunesa, con paisaje excelente en la meseta de Mambilla. DESCARTADA: atraviesa Taraba, en pleno Middle Belt en conflicto agricultores-ganaderos, y son pistas de gravilla con >400 km sin servicios. Solo se reactivaría si Mfum/Ekok se cerrara por completo."),
    ],
    vehiculos=[
        "CPD (carnet de paso en aduana) obligatorio y, desde el 7 de enero de 2026, complementado por el nuevo Temporary Vehicle Admission Permit de la Nigeria Customs Service: válido hasta 90 días, prorrogable 30 más con autorización del Customs Area Controller. Base legal en la Nigeria Customs Service Act 2023 y en los convenios de Kioto, Estambul y TIR.",
        "Documentos que exige el permiso temporal: pasaporte internacional válido, permiso internacional de conducir, permiso de circulación del vehículo, seguro y el propio CPD, más inspección física del vehículo en la aduana de entrada.",
        "Condiciones del permiso temporal: el vehículo no puede venderse, alquilarse, transferirse, modificarse ni usarse con fines comerciales, pero circula libremente por todo el país. A la salida hay que presentar el vehículo Y la declaración aduanera de admisión temporal aprobada. En caso de accidente, robo o avería irreparable, notificación inmediata a la oficina de aduanas más cercana.",
        "Como Nigeria se cruza dos veces, se abren y cierran DOS permisos temporales distintos. Guardar copia digital y en papel del primero al salir por Mfum: será la referencia si hay cualquier discusión en la reentrada.",
        "Carte Brune / Brown Card de la CEDEAO válida en Nigeria: es la última etapa antes del cambio de zona: al entrar en Camerún hay que pasar a la Carte Rose de la CEMAC. Comprobar que la Brown Card contratada en Senegal o Ghana cubre expresamente Nigeria y que la vigencia llega a la segunda pasada; si no, renovarla en Lagos.",
        "Permiso internacional de conducir obligatorio y pedido constantemente. Hay agentes que afirman que no es válido en Nigeria: es falso, y no lo sostienen si se responde con calma.",
        "Carpeta de controles: plástico transparente con copia del pasaporte, visado, sello de entrada, permiso de circulación, CPD, permiso de admisión temporal, Brown Card, permiso internacional y certificado de fiebre amarilla, más 30-40 fotocopias sueltas. Se entrega la carpeta, no los originales. Con 20 controles por jornada, esto ahorra horas.",
        "Talleres y recambios: Lagos (mercado de Ladipo, en Mushin) es la mejor plaza de todo el tramo atlántico y probablemente la última buena hasta Duala. Revisión a fondo de los dos vehículos aquí, en la bajada, antes del bloque centroafricano.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Régimen legal real: la NCAA exige registro del aparato («Recognition of Ownership», que debe acompañar cada vuelo), permiso de operación y licencia de piloto remoto para cualquier uso no estrictamente recreativo. El portal digital de regulación de drones de la NCAA es la vía de tramitación.",
        "Límites operativos: techo 120 m (400 ft), línea de vista visual permanente, solo de día, nunca sobre aglomeraciones, estadios, masas de agua sin autorización de control aéreo, aeropuertos ni instalaciones militares.",
        "Riesgo real: se han documentado incautaciones en aduana y detenciones. El incumplimiento del registro contempla multas altas y penas de hasta 3 años de prisión.",
        "Contexto de seguridad: volar cerca del puente del Níger, del puerto de Lagos, de la refinería de Dangote, de cualquier instalación petrolera o de un control militar se interpreta como reconocimiento hostil. En el corredor de bajada eso deja muy pocos sitios razonables.",
        "Recomendación del proyecto: valorar seriamente NO volar en Nigeria. Si se decide llevarlo, declararlo en la aduana de entrada y no sacarlo del vehículo salvo en Obudu, Afi o Agbokim, y solo con el registro tramitado.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio operativo y consolidado: Nigeria fue el primer mercado africano de Starlink (2023) y es hoy uno de los mayores del continente, con planes residenciales y móviles (Roam) plenamente comercializados y kits a la venta en distribuidores locales.",
        "Aviso de capacidad: ha habido celdas «Sold Out» durante meses en Lagos, Abuya y Port Harcourt, con reapertura parcial del plan de prioridad a precios altos. Para un terminal Roam en itinerancia esto suele ser menos limitante, pero conviene comprobar el mapa oficial y el estado de la celda 30-60 días antes.",
        "Sin hostilidad regulatoria, a diferencia de Camerún: la antena se puede transportar y usar sin que sea en sí misma un problema en los controles. Es el mejor país del tramo atlántico para ponerse al día de trabajo y de comunicaciones.",
        "SIM local como base cotidiana: MTN, Airtel y Glo tienen buena cobertura 4G en todo el corredor sur, incluido Calabar e Ikom. Comprar en Lagos con pasaporte (registro NIN obligatorio: preguntar por el procedimiento para extranjeros).",
        "Zonas sin cobertura fiable: la meseta de Obudu, el acceso a Afi y el interior del Parque Nacional de Cross River. Son los únicos huecos de los dos corredores.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (menos de 10 días) y vacuna antirrábica en vigor —aplicada más de 30 días antes y con menos de 12 meses— exigibles en el control fronterizo. Documentación en inglés (Nigeria es anglófona: aquí sí sirve la versión inglesa del pasaporte europeo).",
        "PERMISO DE IMPORTACIÓN: Nigeria exige permiso previo de importación de animales de compañía. La autoridad es el Nigeria Agricultural Quarantine Service (NAQS) junto con el Federal Department of Veterinary and Pest Control Services. Se tramita presentando certificado sanitario, cartilla de vacunación escaneada, datos del viajero y una dirección en Nigeria; el coste referenciado arranca en unos 150 USD y el plazo va de varios días a semanas. Es, según el dosier del perro del proyecto, la burocracia animal más densa de África occidental.",
        "POR CONFIRMAR — el punto crítico: todas las fuentes disponibles sobre importación de mascotas en Nigeria están escritas para la entrada AÉREA (Lagos y Abuya) y ninguna aborda la entrada terrestre. No existe prohibición conocida de entrar por tierra: simplemente no está documentado. Hay que escribir directamente al NAQS en Abuya preguntando expresamente por la entrada por Sèmè/Kraké y por Mfum/Ekok, y hacerlo con 4-6 meses de antelación.",
        "OJO con una fuente muy citada y errónea: la ficha de PetTravel sobre Nigeria confunde Nigeria con Níger en el apartado de la rabia y afirma una ventana de 48 horas para el certificado sanitario que sería inviable por tierra. No es fuente utilizable — no planificar sobre ella.",
        "Como el país se cruza dos veces con meses de diferencia, hay que contar con DOS permisos separados salvo que el NAQS confirme por escrito lo contrario. El segundo se tramita desde Camerún (Yaundé) con 4 semanas de antelación.",
        "Calor y humedad: el sur de Nigeria está por encima de 30 °C con humedad alta casi todo el año. Nunca dejar al perro solo en el vehículo —ni por calor ni por riesgo de robo—, sombra y agua constantes, y evitar las horas centrales en los tránsitos largos.",
        "Ver la matriz por zona: la buena noticia es que casi todas las paradas del itinerario (Badagry, Agbokim, monolitos de Alok, Olumo, Obudu) están FUERA de parque nacional y son compatibles con el perro. Lo que queda vetado son los dos centros de primates de Pandrillus y el Parque Nacional de Cross River.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional OBLIGATORIO para la entrada y comprobado en el control sanitario de la frontera. Pueden pedir además sellos de cólera y meningitis.",
        "Malaria en todo el territorio y todo el año, con transmisión intensa en el sur: profilaxis a valorar con Sanidad Exterior, mosquitera y repelente con DEET. Es el riesgo sanitario número uno del tramo.",
        "Agua: no beber del grifo en ningún punto del país. El agua embotellada y en bolsa («pure water») es barata y está en todas partes; para el depósito de uso general, manguera de estación de servicio u hotel, pero tratar siempre antes de beber.",
        "Vacunación recomendada además: hepatitis A y B, fiebre tifoidea, tétanos-difteria, meningitis, poliomielitis (Nigeria ha tenido brotes de poliovirus derivado de vacuna) y rabia — esta última especialmente relevante viajando con perro y con una densidad alta de perros callejeros.",
        "Referencias hospitalarias: LUTH y los privados de Victoria Island en Lagos, UBTH en Benin City, UCTH en Calabar, UCH en Ibadan. El nivel cae mucho fuera de estas ciudades: en el norte de Cross River (Obudu, Afi, Ikom) no hay nada equivalente.",
        "Lassa: Nigeria tiene brotes estacionales de fiebre de Lassa (diciembre-abril), transmitida por roedores y sus excrementos. No almacenar comida abierta, no acampar en zonas con presencia evidente de roedores y consultar el estado de los brotes antes de entrar.",
        "Seguro con evacuación médica aérea imprescindible. Desde Obudu o Ikom, la evacuación realista es a Lagos o a Abuya, no a Calabar.",
    ],
    seguridad_intro=("Nigeria es, junto con Camerún, el tramo de mayor exigencia de seguridad del proyecto, pero por razones distintas: en Camerún el problema es que el único paso viable atraviesa una zona de guerra; en Nigeria el problema es que el país tiene cuatro conflictos simultáneos "
                     "y hay que atravesarlo por el estrecho pasillo que no toca ninguno. El corredor sur es asfalto continuo, con servicios y hospitales, y es donde vive y circula la mayor parte del país: los overlanders que lo han recorrido lo describen como exigente en paciencia, no en peligro. "
                     "La disciplina consiste en no salirse de él ni un solo desvío, no conducir nunca de noche y no circular en lunes por el Sureste."),
    seguridad=[
        "Exclusiones absolutas: Noreste (Boko Haram/ISWAP), Noroeste y centro-norte (bandidaje y secuestros masivos), Middle Belt (conflicto agricultores-ganaderos) y el interior del delta del Níger (secuestro petrolero y piratería). Ningún desvío, ninguna excepción, ninguna versión «con escolta».",
        "Nunca conducir de noche en ningún punto del país. Es la regla de seguridad número uno: la inmensa mayoría de los asaltos y secuestros en carretera ocurren de noche o al amanecer, y el 65 % de los ataques se produce en tramos rodeados de bosque. Además hay camiones sin luces, baches profundos, peatones y ganado.",
        "Nunca circular en lunes por el Sureste (Anambra, Imo, Abia, Enugu, Ebonyi): «sit-at-home» del IPOB, con ataques documentados a vehículos que circulan. Planificar los cruces de Onitsha, Aba, Enugu y Abakaliki entre martes y jueves.",
        "Secuestro exprés: el patrón es un retén falso o un vehículo atravesado en tramo boscoso. Contramedidas: salida al amanecer y llegada antes de las 17:00, distancia amplia con el vehículo de delante, no parar por señales de particulares ni por accidentes aparentes, dos móviles con SIM distintas, efectivo repartido en varios sitios y una «cartera de sacrificio» con poco dinero.",
        "Controles de carretera (~20 por jornada larga): llegar despacio con la ventanilla bajada, saludar primero en inglés, entregar la carpeta de copias y no los originales, no mostrar prisa ni miedo, y no pagar. Los overlanders que han cruzado el país sin pagar un solo soborno son mayoría entre los que lo han contado. Si insisten, pedir el recibo oficial y esperar: rara vez se sostiene.",
        "Escolta policial obligatoria: puede imponerse en la frontera y costar cientos de dólares. Preguntar en la aduana antes de que se plantee como hecho consumado y llevar efectivo por si acaso.",
        "No fotografiar NUNCA puentes (en especial el del Níger), puertos, refinerías, aeropuertos, instalaciones militares, controles ni agentes uniformados. Es la causa más frecuente de problemas serios para extranjeros.",
        "Lagos: delincuencia urbana común intensa — tirones en los atascos, robos en el «go-slow», estafas. Ventanillas subidas y puertas bloqueadas en atasco, nada visible en el salpicadero, no circular de noche, aparcamiento vigilado 24 h.",
        "Dinero: Nigeria es un país de efectivo y el naira se mueve mucho. Los cajeros de Lagos, Benin City, Calabar e Ibadan funcionan con tarjeta internacional pero con límites bajos por operación. Cambiar en casas de cambio establecidas, nunca en la calle junto a la frontera.",
        "Los dos vehículos siempre juntos y en contacto por radio en los tramos largos, con check-in diario a España desde el alojamiento.",
        "Revalidar la situación con MAEC España, FCDO británico y fuentes locales (hoteleros, transportistas) 72 h antes de cada frontera. Los mapas de avisos son deliberadamente conservadores, pero los datos de secuestro del norte y del centro son duros y no admiten interpretación optimista.",
    ],
    agua=[
        "Lagos, Benin City, Asaba, Calabar, Ibadan, Abeokuta: agua embotellada y en bolsa («pure water») disponible en todas partes y a precio muy bajo; es la forma normal de beber en Nigeria, también para los locales.",
        "Recarga del depósito de uso general: estaciones de servicio grandes, hoteles con aparcamiento y el Marina Resort de Calabar permiten llenar con manguera. Pedirlo en recepción; suele resolverse con una propina pequeña.",
        "Ikom y la meseta de Obudu: últimas recargas cómodas de cada corredor antes de los tramos de frontera y de montaña. En el norte de Cross River el agua es de pozo o perforación — filtro mecánico más tratamiento químico o ebullición, siempre.",
        "Afi Mountain y Old Ekuri (Cross River): agua de manantial o de río en los campamentos comunitarios. Tratar sin excepción.",
        "En estación húmeda (abril-octubre) la recogida de lluvia con lona es rápida y abundante en el sur, pero filtrar igualmente.",
    ],
    combustible=[
        "Sin ningún hueco de 500 km en ninguno de los dos corredores: el eje Sèmè-Lagos-Ore-Benin City-Asaba-Aba-Uyo-Calabar-Ikom y el eje Ikom-Ogoja-Abakaliki-Enugu-Benin City-Osogbo-Ibadan-Abeokuta-Idiroko tienen estaciones formales (NNPC, TotalEnergies, Oando, Ardova, MRS) en todas las ciudades.",
        "El suministro ha mejorado mucho desde la entrada en funcionamiento de la refinería de Dangote, en la propia península de Lekki: las colas y el desabastecimiento crónico de los años del subsidio son cosa del pasado en el sur. El precio, en cambio, sigue moviéndose con frecuencia: comprobarlo al repostar.",
        "Repostar a fondo en Lagos (mejor calidad del país) y otra vez en Calabar, que es la última plaza con oferta amplia y garantizada antes de Camerún.",
        "Ikom es la última estación formal fiable antes de Mfum/Ekok: salir de ahí con depósitos y garrafas llenos, porque al otro lado, en Mamfe y en toda la región anglófona camerunesa, el suministro puede estar interrumpido por la situación de seguridad.",
        "Evitar el combustible en botellas al borde de la carretera, muy común en el Nigeria rural y en el norte de Cross River: calidad imprevisible y adulteración frecuente. Solo en emergencia y con filtro de embudo.",
        "Filtro de embudo para el gasóleo fuera de las grandes ciudades, y depósito de reserva suficiente para absorber una avería de suministro puntual.",
    ],
    experiencias_intro=("Relatos y comentarios reales de otros overlanders sobre Nigeria, para contrastar con la planificación oficial de esta ficha. Nigeria es uno de los países mejor documentados de la ruta atlántica en cuanto a tránsito "
                        "—casi todo el que cruza África occidental por tierra escribe sobre sus controles— y uno de los peor documentados en cuanto a qué ver, precisamente porque casi nadie se para:"),
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Visado · carta de invitación", "Conseguir la carta de invitación de un anfitrión nigeriano (hotel de Lagos, operador local o contacto personal) — es el cuello de botella real del e-Visa y condiciona toda la entrada"),
        ("Visado · segunda entrada", "Confirmar con la Embajada de Nigeria en Madrid si existe visado de turismo de ENTRADA MÚLTIPLE y con qué vigencia; si no cubre las dos pasadas, confirmar ANTES de salir de España que la embajada de Nigeria en Yaundé expide a no residentes"),
        ("Admisión temporal del vehículo", "Confirmar el procedimiento exacto del Temporary Vehicle Admission Permit (vigente desde el 7 de enero de 2026) en las aduanas de Sèmè y de Mfum, y si se puede cerrar en Idiroko"),
        ("Frontera de salida de la subida", "Confirmar que la aduana de Idiroko/Igolo está habilitada para cerrar el permiso temporal y sellar el CPD; plan B, salir por Sèmè y renunciar a la diferenciación de corredores en el último tramo"),
        ("Perro · NAQS", "Escribir al Nigeria Agricultural Quarantine Service en Abuya con 4-6 meses de antelación preguntando EXPRESAMENTE por la entrada terrestre por Sèmè/Kraké y por Mfum/Ekok, el permiso de importación y si hace falta uno por cada entrada. Es la consulta más urgente de África occidental junto con la de Guinea"),
        ("Perro · Pandrillus", "Confirmar por escrito con Pandrillus (Drill Ranch de Calabar y de Afi) que el perro no puede entrar y si hay sitio seguro donde dejarlo mientras se hace la visita"),
        ("Perro · Obudu", "Confirmar la política de mascotas del Obudu Mountain Resort antes de subir los 11 km de curvas"),
        ("Obudu Mountain Resort", "Confirmar que está operativo y el estado del firme de la carretera de acceso: ha pasado por periodos de abandono y de reforma"),
        ("Afi Mountain Drill Ranch", "Reservar con Pandrillus la pernocta con vehículos y confirmar el estado de la pista de Buanchor según la estación; comprobar si el dormidero de golondrinas (nov-feb) coincide con nuestra ventana de subida"),
        ("Parque Nacional de Cross River (Oban)", "Confirmar con el Nigeria National Park Service en Akamkpa las tasas, los guías comunitarios y si la incursión es compatible con el calendario del corredor de bajada"),
        ("MOWAA (Benin City)", "Confirmar si el Museum of West African Art está abierto al público, dada la disputa con la corte del Oba y con el gobierno de Edo"),
        ("Escolta policial", "Preguntar en la aduana de entrada si va a exigirse escolta de pago, y presupuestar efectivo por si ocurre"),
        ("Estacionalidad", "Decidir el calendario: las pistas de Cross River quieren seca (dic-feb) y las cataratas de Agbokim quieren el final de las lluvias (sep-nov). Resolver según cuándo caiga cada pasada"),
        ("Dron", "Decidir si se tramita el registro ante la NCAA o si simplemente no se vuela en Nigeria. La recomendación del proyecto es no volar"),
        ("Fotos pendientes de sustituir", "Los PDIs del cruce del Níger, del Parque Nacional de Cross River y de los monolitos de Alok usan imágenes de referencia de otro punto del país: sustituir por fotos propias o por archivos verificados de Wikimedia Commons"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Las tres decisiones críticas —el visado con carta de invitación, la disciplina del corredor sur y la salida por Mfum/Ekok hacia la región anglófona camerunesa— deben revalidarse activamente antes del viaje, con información local y no solo con avisos internacionales. Los datos de seguridad por zonas proceden de seguimientos independientes de secuestro y de avisos consulares; los de controles y fronteras, de relatos de overlanders que han hecho la ruta.",
    emergency="Emergencia única (policía, bomberos, ambulancia): 112 · Policía: 199 · Consulado General de España en Lagos: +234 (0)1 2094603499 · Emergencia consular 24 h: +234 803 360 1658 · Embajada de España en Abuya: +234 (0)9 461 1100.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

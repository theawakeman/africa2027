# -*- coding: utf-8 -*-
"""RD Congo — corredor doble de tránsito por el extremo OESTE del país (12 sep 2026).

Se cruza DOS VECES por el mismo eje corto: ferry Brazzaville–Kinshasa → N1 → Matadi →
Lufu/Luvo (Angola) en la bajada, y el mismo eje en sentido contrario en la subida, con
desvío a Boma, la costa atlántica de Muanda y las chutes de Zongo.

IMPORTANTE: el conflicto armado activo de RD Congo está en el ESTE (Kivu Norte y Sur, Ituri).
Goma y Bukavu cayeron ante el M23/AFC en enero-febrero de 2025 y la situación sigue siendo muy
volátil. Ese frente está a MÁS DE 1.500 km del corredor de esta ficha, que discurre íntegramente
por la provincia de Kongo Central y Kinshasa, en el extremo occidental del país. Esta ficha NO
cubre el este bajo ninguna circunstancia y el itinerario no se acerca en ningún momento.
"""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===================== BAJADA: ferry → Kinshasa → N1 → Matadi → Lufu/Luvo =====================
    dict(n=1, name="Kinshasa (Gombe y la orilla del río Congo)", cat="Ciudad · servicios", prio="Alta",
         dog="permitido con condiciones", time="2 noches",
         lat=-4.3276, lon=15.3136,
         desc="Megaciudad de más de 17 millones de habitantes y una de las mayores del mundo, separada de Brazzaville por solo 4 km de río: son las dos capitales más próximas del planeta que no comparten el mismo país. El barrio de la Gombe concentra la embajada de España, los bancos, los supermercados donde reponer y prácticamente todos los talleres y recambios serios del corredor. Es también el único lugar del tramo donde se puede resolver un problema mecánico o documental de verdad: lo que no se consiga en Kinshasa, no se consigue hasta Luanda. Tráfico extremo, sin horas valle reales; planificar los desplazamientos urbanos con el doble de tiempo del que indique el navegador.",
         credit="EdwinAlden.1995 · CC BY-SA 4.0",
         source=W + "A%20view%20of%20Congo%20River%20from%20Kinshasa%2C%20Democratic%20Republic%20of%20the%20Congo%20(DRC).jpg?width=900"),
    dict(n=2, name="Marché Central de Kinshasa (Zando)", cat="Cultura", prio="Media",
         dog="no recomendado — dejarlo en el vehículo", time="½ día",
         lat=-4.3243, lon=15.3110,
         desc="El «Zando», el gran mercado central de Kinshasa, en pleno centro: decenas de miles de puestos, telas de wax, pescado seco, fruta, herramientas y electrónica de segunda mano. Es el retrato más directo de la ciudad y el mejor sitio para reponer fresco antes de la N1, pero también un entorno de mucha presión: ir con poco dinero encima, sin cámara a la vista y preferiblemente acompañado por alguien local. No es sitio para el perro: multitud muy densa y suelo caliente. Fotografiar en la calle en RD Congo se toma muy mal (ver el apartado de drones y fotografía).",
         credit="Wikimedia Commons",
         source=W + "Central%20Market%2C%20Kinshasa%2C%20ZNTO.jpg?width=900"),
    dict(n=3, name="Rápidos de Kinsuka (Livingstone Falls)", cat="Naturaleza", prio="Alta",
         dog="permitido con correa corta", time="½ día",
         lat=-4.3806, lon=15.2131,
         desc="A las afueras del oeste de Kinshasa, en la comuna de Ngaliema, el río Congo —el segundo río del mundo por caudal— se estrella contra las rocas al iniciar las cataratas Livingstone, los 350 km de rápidos que lo hacen innavegable hasta Matadi y que son la razón misma de que exista el ferrocarril y la carretera por los que vamos a bajar. Es el sitio más impresionante de la capital y se llega en coche por pista desde la carretera de Kinsuka (unos 30-40 min desde la Gombe). Rocas resbaladizas y corriente letal: correa corta con el perro y nada de acercarse al borde del agua. Confirmar en el momento si hay que pagar tasa local o llevar guía de barrio; suele haber jóvenes que se ofrecen a acompañar, y merece la pena aceptarlo.",
         credit="Wikimedia Commons",
         source=W + "Congo%20River%20from%20Kinshasa%20in%20Democratic%20Republic%20of%20the%20Congo%20(DRC).jpg?width=900"),
    dict(n=4, name="Jardín Botánico de Kisantu", cat="Naturaleza", prio="Alta",
         dog="permitido con correa", time="½ día",
         lat=-5.1349, lon=15.0854,
         desc="A unos 120 km de Kinshasa por la N1, junto a la misión jesuita de Kisantu: 225 hectáreas creadas en 1900 por el hermano Justin Gillet, uno de los jardines botánicos históricos de África y el mejor sitio del corredor para parar a media mañana. Avenidas de palmeras, estanques con nenúfares gigantes, bambú, colección de árboles frutales tropicales y aves. Está en el eje, no obliga a desviarse y es una parada perfectamente compatible con el perro atado. Hay alojamiento sencillo en la misión y en Inkisi, el núcleo urbano contiguo, con combustible y mercado.",
         credit="Wikimedia Commons",
         source=W + "Entr%C3%A9e%20du%20jardin%20du%20p%C3%A8re%20Gillet%20%C3%A0%20Kisantu%2C%20Bas-Congo.JPG?width=900"),
    dict(n=5, name="Cuevas de Mbanza-Ngungu (grottes de Thysville)", cat="Naturaleza", prio="Media",
         dog="permitido con condiciones", time="½ día",
         lat=-5.2461, lon=14.8637,
         desc="Mbanza-Ngungu, la antigua Thysville colonial, está a unos 700 m de altitud y tiene un clima notablemente fresco para el Congo: fue la estación de altura donde los colonos belgas iban a escapar del calor de Kinshasa y Matadi, y todavía hoy es el mejor sitio del corredor para dormir bien. Sus grutas kársticas, conocidas desde principios del siglo XX, albergan una rareza biológica famosa: peces cavernícolas ciegos y despigmentados (Caecobarbus geertsii), especie protegida y endémica de estas cuevas. El acceso depende de guías locales y del estado de las escaleras y pasarelas: confirmar sobre el terreno, porque la infraestructura es intermitente. Imagen de referencia de la vegetación de Kongo Central, no de las propias cuevas.",
         credit="Wikimedia Commons",
         source=W + "All%C3%A9e%20au%20jardin%20du%20p%C3%A8re%20Gillet%20%C3%A0%20Kisantu.JPG?width=900"),
    dict(n=6, name="Matadi y el puente Maréchal sobre el río Congo", cat="Ciudad · servicios", prio="Alta",
         dog="permitido con condiciones", time="1 noche",
         lat=-5.8167, lon=13.4833,
         desc="Puerto principal del país, encaramado en las laderas empinadísimas de la garganta del Congo a 148 km del mar: por aquí entra casi toda la importación de RD Congo y de aquí sale la caravana de camiones que colapsa la N1. Su puente Maréchal (inaugurado en 1983, construido por Japón, 722 m de vano central) fue durante décadas el mayor puente colgante de África y sigue siendo el único cruce fijo del río Congo en todo el país. Es también la última plaza de servicios seria antes de Angola: combustible, talleres, banco, hospital y hoteles con aparcamiento. Ojo con las cuestas: calles de pendiente brutal, incómodas con vehículo pesado. El puente es infraestructura estratégica — nada de fotos ni de drones.",
         credit="Χρίστος Ιμμανοελ · CC BY-SA 4.0",
         source=W + "Matadi%20Bridge%20DR%20Congo.jpg?width=900"),
    # ===================== SUBIDA: Lufu/Luvo → Matadi → Boma → Muanda → Zongo → Kinshasa =====================
    dict(n=7, name="Boma · antigua capital colonial y el baobab de Stanley", cat="Cultura", prio="Alta",
         dog="permitido con condiciones", time="½–1 día",
         lat=-5.8511, lon=13.0528,
         desc="Capital del Estado Libre del Congo y después del Congo Belga entre 1886 y 1926, antes de que el poder se trasladara a Léopoldville (Kinshasa). Conserva un conjunto de arquitectura colonial en madera y hierro prefabricado traído de Bélgica, la antigua estación, el paseo sobre el río y el célebre baobab hueco asociado a Stanley, que llegó a usarse como despacho y alojamiento y sigue siendo el monumento-símbolo de la ciudad. Es la parada de contenido histórico más fuerte de todo el corredor congoleño y solo está a 130 km de Matadi por la N1: se puede hacer en la subida sin coste de calendario apreciable.",
         credit="Χρίστος Ιμμανοελ · CC BY-SA 4.0",
         source=W + "Boma%20DR%20Congo.jpg?width=900"),
    dict(n=8, name="Muanda, la desembocadura del Congo y el Parque Marino de los Manglares", cat="Costa", prio="Alta",
         dog="permitido", time="1–2 noches",
         lat=-5.9269, lon=12.3494,
         desc="RD Congo, un país de 2,3 millones de km², tiene solo unos 37 km de costa atlántica: toda ella aquí, en el territorio de Muanda, al norte de la boca del río Congo. Playas largas de arena, cocoteros, campamentos sencillos y un ambiente completamente distinto al resto del país — es el lugar donde por fin se puede soltar al perro. Al sur, hacia Banana (el fondeadero natural de aguas profundas y viejo puerto negrero donde hoy se construye el nuevo puerto de aguas profundas), está el Parque Nacional Marino de los Manglares, sitio Ramsar desde 1996 y único parque marino del país: manglares en la desembocadura, manatíes africanos, tortugas marinas y aves acuáticas. Se visita en piragua con guías locales del ICCN. La zona es también petrolera (Perenco) y hay instalaciones sensibles: nada de drones ni de fotos hacia ellas.",
         credit="Wikimedia Commons",
         source=W + "L'oc%C3%A9an%20atlantique%20vu%20de%20la%20plage%20de%20Muanda.jpg?width=900"),
    dict(n=9, name="Chutes de Zongo (río Inkisi)", cat="Naturaleza", prio="Alta",
         dog="permitido con correa corta", time="1 noche",
         lat=-5.0167, lon=14.8833,
         desc="Salto de unos 65 m sobre el río Inkisi, a unas tres horas de Kinshasa por un desvío desde el eje de la N1: la escapada clásica de fin de semana de los kinois y, con diferencia, el mejor sitio de acampada del corredor. Hay un pequeño complejo hotelero junto a las cascadas, con terreno para aparcar y acampar y acceso a la poza y al mirador. La pista final de acceso es de tierra roja y se embarra con lluvia — en temporada húmeda (octubre-mayo) entrar y salir puede ser lento. Perro con correa corta en el borde: el desnivel no está protegido.",
         credit="Wikimedia Commons",
         source=W + "Zongo%20Falls%201%20(chutes%20de%20Zongo)%20-%20panoramio.jpg?width=900"),
    dict(n=10, name="Lola ya Bonobo · santuario de bonobos", cat="Naturaleza", prio="Alta",
         dog="prohibido — perro fuera del recinto", time="½ día",
         lat=-4.5333, lon=15.3667,
         desc="A unos 25 km al sur del centro de Kinshasa, en las Petites Chutes de la Lukaya (Mont Ngafula), el único santuario del mundo dedicado al bonobo: un gran simio que solo existe en RD Congo, al sur del río Congo, y que es el pariente vivo más próximo al ser humano junto con el chimpancé. No es un parque nacional ni un zoo, sino un centro de rescate y rehabilitación de crías huérfanas del tráfico de carne de caza, fundado en 1994 por Claudine André, con un bosque de 30 ha donde los grupos viven semilibres. Abre al público en días concretos (habitualmente fines de semana y con horario limitado): confirmar por correo antes de ir. IMPORTANTE: los simios son susceptibles a enfermedades humanas y caninas — dar por hecho que el perro NO entra y que hay que planificar turnos o dejarlo en el alojamiento de Kinshasa. Imagen de referencia de un bonobo, no del propio santuario.",
         credit="Wikimedia Commons",
         source=W + "Bonobo.jpg?width=900"),
    dict(n=11, name="Valle del N'sele (Nsele Valley Park)", cat="Naturaleza", prio="Media",
         dog="no confirmado — tratar como prohibido", time="½–1 día",
         lat=-4.3667, lon=15.5833,
         desc="En el extremo oriental de la provincia de Kinshasa, donde el río N'sele desemboca en el Congo, hay un espacio privado de conservación con sabana, galería fluvial y fauna reintroducida (antílopes, primates, aves acuáticas) que funciona como la escapada natural más cercana a la capital, a menos de una hora del centro por la carretera de Maluku. Es la mejor opción del corredor para pasar una jornada tranquila con los vehículos fuera del caos urbano antes de encarar el ferry de vuelta. Confirmar antes de ir si admiten entrar con vehículo propio, cuál es la tasa y —fundamental para nosotros— si el perro puede permanecer dentro del coche; al haber fauna reintroducida lo normal es que no.",
         credit="Wikimedia Commons",
         source=W + "Bonobo%20at%20Nsele%20Valley%20Park%2C%20Kinshasa%2C%20DR%20Congo.jpg?width=900"),
    dict(n=12, name="Rumba congoleña en directo (Kinshasa)", cat="Cultura", prio="Alta",
         dog="no recomendado — dejarlo en el alojamiento", time="1 noche",
         lat=-4.3350, lon=15.2860,
         desc="La rumba congoleña está inscrita en la Lista Representativa del Patrimonio Cultural Inmaterial de la UNESCO desde 2021, y Kinshasa es su capital mundial: de aquí salieron Franco Luambo y el TPOK Jazz, Tabu Ley Rochereau, Papa Wemba y el soukous que colonizó toda África. Escucharla en vivo en un bar de Matonge o de Bandalungwa —donde todavía tocan orquestas con sección de vientos y varias guitarras— es la experiencia cultural más honesta que ofrece el país y no cuesta prácticamente nada. Salir acompañado de alguien local, ir y volver en taxi conocido o con el vehículo aparcado en sitio vigilado, y no llevar encima más de lo necesario. Perro en el alojamiento.",
         credit="Wikimedia Commons",
         source=W + "Bakolo%20Music%20International%2C%20the%20oldest%20traditional%20congolese%20rumba%20music%20group%20during%20a%20rehearsal%20In%20Kinshasa.jpg?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "naturaleza": "verde", "cultura": "morado", "costa": "turquesa"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada bajada — Beach Ngobila, ferry desde Brazzaville", "Frontera", -4.2981, 15.2989,
     "Único cruce posible entre las dos capitales: NO existe puente sobre el río Congo (el proyecto de puente carretera-ferrocarril Brazzaville–Kinshasa está firmado pero no construido). Pasajeros en canot rapide (15-20 min); vehículos en el bac/barcaza, con salidas limitadas y no diarias. Intervienen DGM (inmigración), DGDA (aduana), OCC, higiene (fiebre amarilla), policía portuaria y municipal. Trámite descrito por todos los que lo han hecho como largo y muy propenso a «tasas» informales: presupuestar un día entero, empezar a primera hora de la mañana y llevar francos CFA, francos congoleños y dólares limpios."),
    ("Frontera · Salida bajada — Lufu/Luvo (hacia Angola)", "Frontera", -5.9167, 13.9667,
     "Desvío al sur desde el eje de la N1 a la altura de Songololo, ~30 km. Registro en inmigración de RD Congo, paso de un puente y trámite de entrada angoleño unos 500 m después. Proceso descrito como ágil y sin solicitudes de soborno por overlanders recientes — contraste notable con el ferry de Kinshasa. Confirmar horario (cierres al mediodía y por la tarde son habituales en la zona)."),
    ("Frontera · Entrada subida — Luvo/Lufu (desde Angola)", "Frontera", -5.9167, 13.9667,
     "Mismo paso en sentido inverso al regreso desde Angola. Comprobar que el visado congoleño es de DOBLE ENTRADA o que se ha gestionado un segundo visado: es la decisión documental más importante de esta ficha."),
    ("Frontera · Salida subida — Beach Ngobila, ferry hacia Brazzaville", "Frontera", -4.2981, 15.2989,
     "Cierre del corredor: mismo ferry, mismo circo administrativo, ahora en sentido Kinshasa→Brazzaville. Coordinar con la ficha de Congo-Brazzaville, que documenta el trámite desde la otra orilla."),
    ("Embajada de España en Kinshasa (acreditada también en Congo-Brazzaville)", "Consular", -4.3050, 15.3050,
     "Bd. Colonel Tshatshi nº 37, Kinshasa (Gombe). Tel. +243 813 300 061 / 817 008 770 / 818 843 195 · Emergencia consular: +243 819 500 289. Avisar de la entrada y de las fechas previstas de las dos pasadas."),
    ("Hôpital Général de Référence de Kinshasa", "Hospital", -4.3250, 15.3139,
     "Hospital público de referencia de la capital. Para expatriados se suelen usar además las clínicas privadas de la Gombe/Ngaliema; confirmar cuál acepta el seguro antes de necesitarla. Coordenada urbana aproximada."),
    ("IME Kimpese — Institut Médical Évangélique", "Hospital", -5.5556, 14.4386,
     "Hospital de referencia histórico del corredor, en Kimpese, sobre la propia N1 entre Mbanza-Ngungu y Matadi: la mejor opción sanitaria entre Kinshasa y la frontera de Angola. Coordenada urbana aproximada."),
    ("Hôpital Général de Référence de Kinkanda — Matadi", "Hospital", -5.8200, 13.4700,
     "Referencia hospitalaria de Matadi y del tramo final antes de Angola. Coordenada urbana aproximada."),
    ("Combustible · Kinshasa", "Combustible", -4.3276, 15.3136,
     "Mejor oferta y calidad del país (Engen, TotalEnergies, SEP Congo); repostar a fondo antes de salir a la N1. Llevar embudo con filtro: la calidad del gasóleo fuera de las grandes estaciones es irregular."),
    ("Combustible · Kisantu / Inkisi (N1)", "Combustible", -5.1349, 15.0854,
     "Estaciones formales sobre la N1 a ~120 km de Kinshasa, junto al jardín botánico; primera parada natural del corredor."),
    ("Combustible · Mbanza-Ngungu y Kimpese (N1)", "Combustible", -5.2461, 14.8637,
     "Estaciones sobre la N1 en el tramo medio; suficiente para no llegar nunca a un hueco de 500 km entre Kinshasa y Matadi."),
    ("Combustible · Matadi", "Combustible", -5.8167, 13.4833,
     "Última plaza con oferta formal amplia antes de Lufu/Luvo; repostar a fondo aquí en la bajada. En la subida, repostar aquí también antes del desvío a Boma y Muanda."),
    ("Combustible · Boma y Muanda", "Combustible", -5.8511, 13.0528,
     "Ambas tienen estaciones formales (Boma es puerto y Muanda es zona petrolera), pero con existencias menos garantizadas que Matadi: salir de Matadi con depósito lleno para el bucle costero de ida y vuelta (~480 km)."),
    ("Agua potable y de uso general · Kinshasa", "Agua potable", -4.3276, 15.3136,
     "Agua embotellada sin problema en los supermercados de la Gombe. Para el depósito de uso general (ducha, aseo, limpieza), hoteles y estaciones de servicio de Kinshasa permiten llenar con manguera; pedirlo en recepción. NO beber agua de red sin potabilizar: hay brotes recurrentes de cólera en la ciudad."),
    ("Agua potable y de uso general · Matadi y Mbanza-Ngungu", "Agua potable", -5.8167, 13.4833,
     "Hoteles con aparcamiento en ambas ciudades permiten recargar el depósito de uso general; Mbanza-Ngungu, más fresca y tranquila, es el mejor sitio del corredor para hacerlo con calma."),
]

DRONE_CALLOUT = ("bad", "PROHIBIDO EN LA PRÁCTICA · riesgo real de detención y acusación de espionaje",
                 "RD Congo es, junto con los países en guerra abierta, el sitio más peligroso de todo el viaje para sacar un dron. No existe un procedimiento civil turístico simple y estable, el país está en conflicto armado activo (aunque a 1.500 km de nuestro corredor) y el reflejo de las fuerzas de seguridad ante cualquier aparato volador es tratarlo como espionaje. El corredor que recorremos está además lleno de infraestructura estratégica —el puerto de Matadi, el puente Maréchal, las presas de Inga, las instalaciones petroleras de Muanda, el propio río frontera con Congo-Brazzaville—, exactamente los objetivos cuya filmación acarrea detención. Norma del proyecto: EL DRON NO SE SACA DE SU CAJA EN RD CONGO, en ningún punto ni por ningún motivo. Declararlo en aduana al entrar, llevarlo embalado y a la vista en el registro, y no discutirlo. Lo mismo se aplica en gran medida a la cámara: fotografiar edificios oficiales, puentes, puertos, militares o policías provoca problemas serios de forma rutinaria.")

STARLINK_CALLOUT = ("ok", "Starlink activo y legal en RD Congo desde mayo de 2025 — confirmado",
                    "RD Congo bloqueó Starlink en 2023 y levantó la prohibición en 2025: el servicio se autorizó y entró en funcionamiento comercial en mayo-junio de 2025, y en 2026 Airtel y SpaceX lanzaron además en el país el primer servicio satélite-a-móvil (direct-to-cell) de África. Es, por tanto, el respaldo de comunicaciones fiable de este corredor y conviene tenerlo operativo antes de entrar, sobre todo porque el ferry y los controles de carretera son los momentos en los que más útil resulta poder avisar. Revisar el mapa oficial y el régimen de roaming 30-60 días antes por si cambia algo.")

DOG_MATRIX = [
    ("Muanda y la costa atlántica", "permitido",
     "LA mejor parada del corredor para el perro: 37 km de playa abierta, poca gente y temperatura marítima. Es el único sitio del tramo donde puede correr suelto. Cuidado con las corrientes en la desembocadura del Congo y con los restos de pesca en la arena."),
    ("Kinsuka, Kisantu, Zongo, Mbanza-Ngungu", "permitido con correa",
     "Sitios abiertos sin gestión de parque nacional. Correa corta obligatoria en el borde de los rápidos de Kinsuka y en el mirador de Zongo (desniveles sin proteger y roca resbaladiza). Kisantu, con sus avenidas de sombra, es la parada diurna más cómoda de todo el eje."),
    ("Kinshasa (Gombe, alojamiento)", "permitido con condiciones",
     "Alojarse siempre en hotel o guest house con parking cerrado y vigilado, que es también donde se queda el perro cuando salgamos. Calor y humedad muy altos, tráfico brutal y muchos perros callejeros: correa siempre, paseos a primera y última hora, y ninguna salida a pie por el centro con él."),
    ("Marché Central de Kinshasa y salidas nocturnas de rumba", "no recomendado",
     "Multitud extrema, suelo ardiendo y cero margen de maniobra. Dejarlo en el vehículo a la sombra con ventilación, o mejor en el alojamiento, y turnarnos."),
    ("Lola ya Bonobo (santuario de bonobos)", "prohibido",
     "Los grandes simios comparten patógenos con humanos y perros (y el santuario aplica protocolos sanitarios estrictos por esa razón). Dar por hecho que el perro NO entra al recinto. Plan B: turnos entre los tres viajeros, con el perro en el vehículo a la sombra en el aparcamiento del santuario o directamente en el alojamiento de Kinshasa, que está a 25 km."),
    ("Nsele Valley Park y Parque Marino de los Manglares", "no confirmado",
     "Ambos tienen fauna gestionada (antílopes y primates reintroducidos en Nsele; manatíes, tortugas y aves en los manglares) y lo previsible es que no admitan perro. Escribir antes a Nsele Valley Park y al ICCN. Plan B: en los manglares, la salida se hace en piragua, así que el perro se queda igualmente en el campamento de Muanda con uno de nosotros; en Nsele, sustituirlo por un día de playa en Muanda, que ya está resuelto."),
    ("Matadi y Boma", "permitido con condiciones",
     "Ciudades portuarias con mucho camión y cuestas duras; correa siempre y paseos cortos. En Matadi, evitar la zona del puerto y del puente: es infraestructura sensible y hay control policial permanente."),
]

SOURCES = [
    # Ferry y frontera
    ("WhirledAway · cruzar el río Congo de Brazzaville a Kinshasa (relato y trámites)", "https://whirled-away.com/cross-river-border-brazzaville-kinshasa/"),
    ("Congo Travel & Tours · servicio de cruce del río con vehículo (tarifas y trámites incluidos)", "https://congotravelandtours.com/river-crossing-vehicles/"),
    ("Very Hungry Nomads · Brazzaville–Kinshasa river crossing en 7 pasos", "https://www.veryhungrynomads.com/brazzaville-to-kinshasa-river-crossing/"),
    ("Road to 197 · cruzando el río Congo de Brazzaville a Kinshasa (2025)", "https://www.roadto197.com/2025/06/17/crossing-the-congo-river-from-brazzaville-to-kinshasa-without-a-visa/"),
    ("Maggie in Africa · ferry crossing Brazzaville–Kinshasa", "https://www.maggieinafrica.com/travel-tips/ferry-crossing-brazzaville-to-kinshasa/"),
    ("Sven's Travel Venues · cómo ir de Brazzaville a Kinshasa en barco", "https://www.travelsvenue.com/2020/01/How-to-get-from-RC-to-DRC-by-boat.html"),
    ("Wikipédia (fr) · Beach Ngobila (puerto fluvial de Kinshasa)", "https://fr.wikipedia.org/wiki/Beach_Ngobila"),
    ("WhirledAway · cruce de frontera Lufu (RD Congo) / Luvo (Angola)", "https://whirled-away.com/border-crossing-drc-angola/"),
    # Visado y documentación
    ("Kwafrika Travel · guía de visado de RD Congo (2026)", "https://www.kwafrikatravel.com/dr-congo-visa-guide/"),
    ("Wikipedia · Visa policy of the Democratic Republic of the Congo", "https://en.wikipedia.org/wiki/Visa_policy_of_the_Democratic_Republic_of_the_Congo"),
    ("congo-evisa.com · política de visados y eVisa de RD Congo", "https://congo-evisa.com/democratic-republic-of-the-congo-visa-policy/"),
    ("Embajada de RD Congo en EE. UU. · pasaportes y visados", "https://www.ambadrcusa.org/consular-affairs/passport-visa-tenant-lieu/"),
    # Carretera y corredor
    ("MCTC · corredor Matadi–Kinshasa (operador del terminal de contenedores de Matadi)", "https://mctc-cd.com/en/terminal/corridor-matadi-kinshasa"),
    ("AARoads Wiki · National Road 1 (RD Congo)", "https://wiki.aaroads.com/wiki/National_Road_1_(Democratic_Republic_of_the_Congo)"),
    ("BAfD · proyecto de rehabilitación de la RN1 (Kinshasa/Ndjili)", "https://mapafrica.afdb.org/en/projects/46002-P-CD-DB0-012"),
    ("Wikipedia · Matadi Bridge (puente Maréchal)", "https://en.wikipedia.org/wiki/Matadi_Bridge"),
    ("Tripadvisor · foro RD Congo, «Kinshasa to Matadi»", "https://www.tripadvisor.com/ShowTopic-g294186-i9962-k4785712-Kinshasa_to_Matadi-Democratic_Republic_of_the_Congo.html"),
    # Puntos de interés
    ("Wikipedia · Livingstone Falls (rápidos del Congo en Kinshasa)", "https://en.wikipedia.org/wiki/Livingstone_Falls"),
    ("Travel2Unlimited · Kinshasa y los rápidos del río Congo (Kinsuka)", "https://travel2unlimited.com/dem-rep-of-congo-kinshasa-congo-river-rapids/"),
    ("Wikipedia · Kinshasa Central Market (Zando)", "https://en.wikipedia.org/wiki/Kinshasa_Central_Market"),
    ("Wikipedia · Kisantu (jardín botánico del hermano Gillet)", "https://en.wikipedia.org/wiki/Kisantu"),
    ("Wikipedia · Mbanza-Ngungu (antigua Thysville y sus grutas)", "https://en.wikipedia.org/wiki/Mbanza-Ngungu"),
    ("Wikipedia · Boma, Democratic Republic of the Congo", "https://en.wikipedia.org/wiki/Boma,_Democratic_Republic_of_the_Congo"),
    ("Wikipedia · Moanda (Muanda), Democratic Republic of the Congo", "https://en.wikipedia.org/wiki/Moanda,_Democratic_Republic_of_the_Congo"),
    ("Wikipedia · Banana, Democratic Republic of the Congo", "https://en.wikipedia.org/wiki/Banana,_Democratic_Republic_of_the_Congo"),
    ("Wikipedia · Mangroves National Park (Parc Marin des Mangroves, sitio Ramsar)", "https://en.wikipedia.org/wiki/Mangroves_National_Park"),
    ("Wikipédia (fr) · Chutes de Zongo (río Inkisi)", "https://fr.wikipedia.org/wiki/Chutes_de_Zongo"),
    ("Wikivoyage · Zongo Falls", "https://en.wikivoyage.org/wiki/Zongo_Falls"),
    ("Wikipedia · Lola ya Bonobo (santuario de bonobos)", "https://en.wikipedia.org/wiki/Lola_ya_Bonobo"),
    ("Tripadvisor · Lola ya Bonobo Sanctuary, opiniones y horarios de visita", "https://www.tripadvisor.com/Attraction_Review-g294187-d2423036-Reviews-Lola_ya_Bonobo_Sanctuary-Kinshasa.html"),
    ("DRC Tourism · ruta patrimonial del Reino del Kongo: Boma, Muanda y el Atlántico", "https://drctourism.com/travel-blog/kingdom-of-kongo-heritage-route-boma-moanda"),
    # Comunicaciones
    ("Connecting Africa · Starlink operativo en RD Congo", "https://www.connectingafrica.com/connectivity/starlink-live-in-drc"),
    ("Space in Africa · Starlink se expande a RD Congo (junio 2025)", "https://spaceinafrica.com/2025/06/03/starlink-expands-to-the-democratic-republic-of-congo-strengthening-its-african-footprint/"),
    ("CIO Africa · Airtel y Starlink lanzan el servicio satélite-a-móvil en RD Congo", "https://cioafrica.co/airtel-africa-launches-starlink-satellite-to-mobile-in-drc/"),
    # Seguridad
    ("Critical Threats · Congo War Security Review (seguimiento del conflicto del este)", "https://www.criticalthreats.org/briefs/congo-war-security-review"),
    ("Embajada de España en Kinshasa (RD Congo y Congo-Brazzaville)", "https://www.exteriores.gob.es/Embajadas/kinshasa/es/Paginas/index.aspx"),
    # Comunidad overland
    ("iOverlander · puntos de combustible, agua, acampada y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
    ("Mzungu Expeditions · expedición a RD Congo 2027 (itinerario de operador, referencia de tramos)", "https://www.mzunguexpeditions.com/congo_mbandaka_2027_en"),
]

# BAJADA: ferry Beach Ngobila -> Kinshasa -> Kinsuka -> N1 (Kisantu, Mbanza-Ngungu, Kimpese) -> Matadi -> Songololo -> Lufu/Luvo
CORRIDOR = [(-4.2981, 15.2989), (-4.3276, 15.3136), (-4.3806, 15.2131), (-5.1349, 15.0854),
            (-5.2461, 14.8637), (-5.5556, 14.4386), (-5.8167, 13.4833), (-5.7000, 14.0500),
            (-5.9167, 13.9667)]

# SUBIDA: Lufu/Luvo -> Songololo -> Matadi -> Boma -> Muanda/manglares -> Matadi -> Kimpese ->
# Mbanza-Ngungu -> Chutes de Zongo -> Lola ya Bonobo -> Nsele -> Kinshasa -> ferry
CORRIDOR_ALT = [(-5.9167, 13.9667), (-5.7000, 14.0500), (-5.8167, 13.4833), (-5.8511, 13.0528),
                (-5.9833, 12.4500), (-5.9269, 12.3494), (-5.8511, 13.0528), (-5.8167, 13.4833),
                (-5.5556, 14.4386), (-5.2461, 14.8637), (-5.0167, 14.8833), (-4.5333, 15.3667),
                (-4.3667, 15.5833), (-4.3276, 15.3136), (-4.2981, 15.2989)]

CORRIDOR_LABEL = "Bajada"
CORRIDOR_ALT_LABEL = "Subida"

EXPERIENCIAS = [
    "El ferry de Kinshasa es el cruce con peor fama de todo el viaje: quienes lo han hecho lo describen sin rodeos como «uno de los pasos fronterizos más corruptos que existen». El trayecto físico en canot rapide dura unos 15 minutos y el billete de pasajero ronda los 12.400 FCFA desde Brazzaville, pero el papeleo ocupa el día entero: hay varios puestos sucesivos donde hay que enseñar documentos, rellenar formularios y pagar «tasas» de cuantía variable. El consejo unánime es empezar a primera hora de la mañana, cruzar en fin de semana si se puede (hay menos aglomeración), llevar francos CFA, francos congoleños y dólares en billetes limpios y pequeños, tener a mano el certificado internacional de vacunación, y contratar a un gestor («fixer») que conozca el circuito. (Fuente: WhirledAway.)",
    "El vehículo no cruza en la misma embarcación que los pasajeros: va en la barcaza, y ahí es donde está el verdadero problema. El operador local Congo Travel & Tours vende un servicio «VIP» de cruce de vehículo que incluye inspección de aduanas, tasas portuarias, policía municipal y administrativa, documentación de tránsito, despacho y permisos de conducción en RDC — y lo tarifa desde 4.000 € por vehículo, con la advertencia explícita de que no negocian a la baja. El propio operador dice que evita la barcaza grande por motivos de seguridad e higiene, que el cruce se hace por la mañana (los domingos cierra a mediodía) y que el vehículo tarda entre 1 y 3 días en salir de aduanas en Kinshasa. Tomarlo como cota superior del coste y como aviso de cuántos organismos hay que satisfacer: la cifra que consigamos negociando por nuestra cuenta será mucho menor, pero el número de ventanillas será el mismo. (Fuente: Congo Travel & Tours.)",
    "No hay puente. Conviene decirlo claro porque aparece en los mapas como si lo hubiera: entre Brazzaville y Kinshasa no existe ningún cruce fijo del río Congo. El proyecto de puente carretera-ferrocarril lleva décadas anunciado y firmado entre ambos países, pero no está construido. El ferry es la única opción, y si el ferry no sale ese día, no se cruza.",
    "Contraste con la frontera de Angola: los overlanders que han hecho Lufu (RDC) → Luvo (Angola) en los últimos años lo describen como un cruce ágil, con inmigración congoleña, un puente y el puesto angoleño unos 500 metros después, y sin peticiones de soborno. Es decir: el infierno administrativo de este país está concentrado en el ferry de Kinshasa, no en el conjunto del corredor. (Fuente: WhirledAway, cruce RDC–Angola.)",
    "Controles de carretera y «tracasseries»: la N1 entre Kinshasa y Matadi tiene numerosos puestos de policía, DGM, ANR y tasas de paso, y es un relato recurrente que se pida dinero por infracciones inventadas o por documentos supuestamente incompletos. Las tácticas que funcionan, según la práctica habitual en la región: llevar una carpeta con fotocopias de todo (pasaporte, visado, permiso internacional, seguro local, laissez-passer, certificado de fiebre amarilla) y entregar siempre la copia, nunca el original; hablar francés y saludar con calma antes de nada; no enseñar nunca la cartera ni el fajo de billetes; no aceptar la primera cifra; y no tener ninguna prisa, porque la prisa es exactamente lo que se está tarificando. Anotar el nombre y el puesto de quien pide, en voz alta y educadamente, suele acortar la conversación.",
    "Fotografía: en RD Congo, sacar la cámara en la calle —y no digamos apuntar a un puente, un puerto, un edificio oficial, un uniforme o el propio río frontera— provoca problemas de forma rutinaria, y no es un mito de guías antiguas. Históricamente ha existido un permiso oficial de toma de imágenes y, con permiso o sin él, el criterio del agente de turno es el que manda. En el corredor esto afecta directamente al puente Maréchal de Matadi, al puerto, a las presas de Inga y a las instalaciones petroleras de Muanda. Fotografiar desde dentro del vehículo y sin ostentación es la norma práctica.",
    "El este del país no es este país. Los relatos de overlanders que han cruzado el corredor occidental Kinshasa–Matadi describen un trayecto de carretera principal, con tráfico pesado y burocracia, pero sin ninguna relación con la guerra: el frente del M23 y las milicias de Ituri están a más de 1.500 km, al otro lado de la cuenca del Congo, y no hay ninguna carretera que conecte razonablemente ambas zonas. Dicho lo cual, en enero de 2025, cuando cayó Goma, hubo disturbios y saqueos graves en Kinshasa con ataque a varias embajadas: el este no llega hasta aquí por carretera, pero sí llega por la política. Vigilar el pulso de la capital antes de entrar y tener siempre una salida planificada.",
    "Muanda como recompensa: los pocos viajeros que llegan hasta el extremo occidental coinciden en que la costa atlántica —los únicos ~37 km de litoral que tiene un país de 2,3 millones de km²— es el sitio más relajado del corredor, con playas largas, campamentos sencillos y pescado. Es el desvío que justifica montar la subida distinta a la bajada.",
]

HISTORIA_RESUMEN = ("La República Democrática del Congo es el escenario de una de las mayores tragedias coloniales de la historia —el Estado Libre del Congo del rey belga Leopoldo II, un régimen de explotación del caucho que causó millones de muertos— y, tras la independencia en 1960, "
                    "de décadas de dictadura bajo Mobutu Sese Seko y de las llamadas «guerras mundiales africanas» (1996-2003), el conflicto con más víctimas mortales desde la Segunda Guerra Mundial; este proyecto solo transita brevemente por el corredor occidental de Kinshasa a Matadi, en la provincia de Kongo Central, a más de 1.500 km de las zonas de conflicto activo del este.")

HISTORIA_SECCIONES = [
    ("El reino de Kongo y la desembocadura del río",
     "El poderoso reino de Kongo, con el que Portugal mantuvo relaciones diplomáticas desde el siglo XV (incluida la conversión al cristianismo de su rey Nzinga a Nkuwu), dominó la desembocadura del río Congo: exactamente el territorio que recorre este corredor, de Kinshasa a Matadi, Boma y Muanda, y que sigue llamándose provincia de Kongo Central. El puerto de Banana, junto a la boca del río, fue uno de los grandes puntos de embarque de la trata atlántica antes de decaer el reino bajo la presión esclavista portuguesa."),
    ("El Estado Libre del Congo de Leopoldo II",
     "En 1885, el rey Leopoldo II de Bélgica obtuvo el territorio como posesión personal —no como colonia del Estado belga— bajo el nombre de Estado Libre del Congo, y lo explotó mediante un régimen de trabajo forzado para la extracción de caucho de una brutalidad extrema, documentada internacionalmente y responsable de la muerte de varios millones de congoleños; la presión internacional forzó a Bélgica a asumir el territorio como colonia oficial en 1908. Boma, en nuestro corredor de subida, fue la capital de aquel Estado y después del Congo Belga hasta 1926, y conserva la arquitectura de esos años."),
    ("El ferrocarril y la carretera de Matadi: por qué el corredor existe",
     "Los 350 km de rápidos de las cataratas Livingstone —que se ven desde Kinsuka, a las afueras de Kinshasa— hacen el río Congo innavegable entre el Atlántico y la capital. Esa barrera geográfica es la razón de ser del corredor que recorremos: primero el ferrocarril Matadi-Léopoldville, construido entre 1890 y 1898 a un coste humano espantoso, y hoy la carretera nacional 1, la arteria por la que entra casi toda la importación del país desde el puerto de Matadi. El puente Maréchal, inaugurado en 1983, sigue siendo el único cruce fijo del río Congo en todo el territorio nacional."),
    ("Independencia, Mobutu y el Zaire",
     "El Congo se independizó en 1960 en medio de un caos político que incluyó el asesinato del primer ministro Patrice Lumumba, y tras una crisis de varios años el militar Mobutu Sese Seko tomó el poder en 1965, gobernando durante 32 años bajo un régimen cleptocrático de partido único que renombró el país Zaire, hasta ser derrocado en 1997."),
    ("Las «guerras mundiales africanas» y el conflicto del ESTE, ajeno a esta ruta",
     "La caída de Mobutu desencadenó dos guerras sucesivas (1996-97 y 1998-2003) que llegaron a involucrar a nueve países africanos, con un saldo estimado de varios millones de muertos, el conflicto más letal desde la Segunda Guerra Mundial. Aunque la guerra formal terminó en 2003, las provincias orientales —Kivu Norte, Kivu Sur e Ituri— siguen en conflicto armado abierto: en enero y febrero de 2025 la coalición M23/AFC tomó Goma y Bukavu, las dos capitales provinciales del Kivu, y la situación continúa siendo muy volátil pese a los procesos de negociación de Doha y Washington. Ese frente está en el extremo opuesto del país, a más de 1.500 km del corredor de Kongo Central que recorre este proyecto, sin ninguna conexión por carretera razonable entre ambas zonas: esta ficha no cubre el este y el itinerario no se acerca a él en ningún momento."),
]

HISTORIA_FUENTES = [
    ("BBC News · DR Congo country profile", "https://www.bbc.com/news/world-africa-13286306"),
    ("Encyclopaedia Britannica · Democratic Republic of the Congo, History", "https://www.britannica.com/place/Democratic-Republic-of-the-Congo/History"),
    ("Council on Foreign Relations · Conflict in the Democratic Republic of Congo", "https://www.cfr.org/global-conflict-tracker/conflict/violence-democratic-republic-congo"),
    ("Critical Threats · Congo War Security Review", "https://www.criticalthreats.org/briefs/congo-war-security-review"),
]

SPEC = dict(
    slug="rd-congo", name="RD Congo (corredor oeste)", revision="12 sep 2026",
    sub="Corredor doble por el extremo occidental · ferry de Kinshasa · N1 a Matadi · documentación · seguridad",
    chips=[
        ("BAJADA", "Ferry Brazzaville–Kinshasa → N1 (Kisantu, Mbanza-Ngungu) → Matadi → Lufu/Luvo · ~445 km"),
        ("SUBIDA", "Luvo/Lufu → Matadi → Boma → Muanda (Atlántico) → Zongo → Kinshasa → ferry · ~940 km"),
        ("PDIs", "12 puntos repartidos entre las dos pasadas, sin solapamiento salvo Kinshasa y Matadi"),
        ("EL CRUCE", "Ferry del río Congo: el trámite más difícil de todo el viaje"),
        ("ZONA EXCLUIDA", "Kivu, Ituri y todo el ESTE — a más de 1.500 km, fuera de la ruta"),
        ("DRON", "PROHIBIDO EN LA PRÁCTICA · riesgo real de detención"),
        ("STARLINK", "activo y legal desde mayo de 2025 — confirmado"),
        ("PERRO", "Muanda (costa atlántica) es la mejor parada del corredor"),
    ],
    center=[-5.1, 14.0], zoom=7,
    notice="Documento de planificación. Esta ficha cubre EXCLUSIVAMENTE el corredor occidental Kinshasa–Matadi–Muanda–Lufu, en la provincia de Kongo Central: el conflicto armado activo de RD Congo está en el ESTE del país (Kivu Norte y Sur, Ituri), a más de 1.500 km de esta ruta y sin conexión razonable por carretera. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("RD Congo se cruza <strong>dos veces por el mismo corredor corto del oeste</strong>, porque no existe otra opción: la provincia de Kongo Central es una franja de unos 350 km entre Kinshasa y el mar, "
                   "recorrida por una única carretera principal, la <strong>N1</strong>, y sin ninguna alternativa real de itinerario. "
                   "En la <strong>bajada</strong> entramos por el ferry del río Congo desde Brazzaville, cruzamos Kinshasa y bajamos por la N1 haciendo Kisantu y Mbanza-Ngungu hasta Matadi, y salimos a Angola por Lufu/Luvo. "
                   "En la <strong>subida</strong>, de vuelta desde Angola, recorremos el mismo eje al revés pero añadiendo lo que en la ida no da tiempo a hacer: el desvío a <strong>Boma</strong> y a los 37 km de costa atlántica de <strong>Muanda</strong> con el parque marino de los manglares, y de vuelta hacia la capital el desvío a las <strong>chutes de Zongo</strong> y las paradas periurbanas de Kinshasa (Lola ya Bonobo, valle del N'sele, la rumba). "
                   "Así las dos pasadas ven cosas distintas sin inventarse carreteras que no existen."),
    decision=("RD Congo es un país de tránsito puro para este proyecto, pero de tránsito <em>doble</em> y por un corredor donde los problemas no son de ruta sino de papeleo: el <strong>ferry Brazzaville–Kinshasa</strong> es, con diferencia, el trámite más complicado y más caro de todo el viaje Barcelona-Sudáfrica-Barcelona, y hay que hacerlo dos veces. "
              "La decisión de ruta, por tanto, es sencilla —no hay alternativa al eje N1—, y el esfuerzo de planificación tiene que ir íntegramente a los tres puntos críticos: <strong>visado de doble entrada</strong>, <strong>embarque y despacho del vehículo en el ferry</strong>, y <strong>seguro y laissez-passer del vehículo</strong>. "
              "El conflicto armado activo del país (M23/AFC en Kivu, milicias de Ituri) está en el extremo ORIENTAL, a más de 1.500 km de este corredor y sin carretera que los conecte de forma practicable; no es una alerta de proximidad, es otra región del país, y esta ficha no la cubre en absoluto."),
    facts=[
        ("Ventana prevista", "Bajada: tras Congo-Brazzaville (gorilas de Odzala), antes de Angola. Subida: tras Angola, antes de volver a Congo-Brazzaville en tránsito rápido."),
        ("Entrada bajada", "Ferry sobre el río Congo desde Brazzaville al Beach Ngobila de Kinshasa: NO hay puente, el ferry es la única vía."),
        ("Salida bajada", "Lufu/Luvo hacia Angola, por desvío al sur desde Songololo. Cruce descrito como ágil por overlanders recientes."),
        ("Entrada subida", "Luvo/Lufu desde Angola, el mismo paso en sentido inverso."),
        ("Salida subida", "Ferry Kinshasa → Brazzaville, cerrando el corredor congoleño."),
        ("Visado", "Visado previo obligatorio para pasaportes españoles. Existe eVisa, pero SU VALIDEZ EN FRONTERA TERRESTRE Y FLUVIAL ESTÁ POR CONFIRMAR: dar por hecho que hay que tramitarlo en consulado, y en modalidad de DOBLE ENTRADA."),
        ("Vehículo", "RD Congo queda fuera de CEDEAO (Brown Card) y de CEMAC (Carte Rose): seguro local obligatorio. Régimen de importación temporal (CPD vs. laissez-passer de la DGDA) por confirmar."),
        ("Carretera", "N1 Kinshasa–Matadi, ~350 km, asfaltada y con tráfico pesadísimo de camiones del puerto; peajes en el eje. Prever 6-8 h reales, no las 4 h que dice el mapa."),
        ("Seguridad", "Corredor occidental manejable con precaución alta; la variable real es el pulso político de Kinshasa (disturbios y saqueos en enero de 2025), no el frente del este."),
        ("Comunicaciones", "Starlink activo y legal desde mayo de 2025 (confirmado); SIM local (Vodacom, Airtel, Orange) como complemento."),
        ("Moneda", "Franco congoleño (CDF); el dólar circula de forma generalizada. Llevar billetes de USD limpios, sin roturas ni marcas, y de denominación pequeña para los trámites."),
    ],
    alerts=[
        "ZONA EXCLUIDA — el ESTE del país: Kivu Norte, Kivu Sur e Ituri están en conflicto armado activo. El M23/AFC tomó Goma en enero de 2025 y Bukavu en febrero de 2025, y la situación sigue muy volátil en 2026. Esas provincias están a MÁS DE 1.500 km de nuestro corredor de Kongo Central, en el extremo opuesto del país y sin ninguna carretera que las conecte de forma practicable con el oeste. No es que vayamos a pasar cerca: es que estamos en otra parte del Congo. El itinerario NO se aproxima al este bajo ninguna circunstancia.",
        "Kinshasa SÍ se ve afectada por lo que pasa en el este, pero por vía política: el 28 de enero de 2025, tras la caída de Goma, hubo disturbios y saqueos graves en la capital, con ataques a varias embajadas extranjeras. Antes de entrar, comprobar el pulso de la ciudad (avisos consulares, prensa local) y tener planificada una salida por la N1 si la situación se degrada. Evitar manifestaciones y concentraciones en cualquier caso.",
        "EL FERRY ES EL PROBLEMA, NO LA CARRETERA. El cruce del río Congo con vehículo es el trámite más difícil, largo y caro de todo el viaje: múltiples organismos (DGM, DGDA, OCC, higiene, policía portuaria y municipal), tarifas informales en cada ventanilla y despacho del vehículo que puede llevar de 1 a 3 días en Kinshasa. Un operador local llega a cobrar desde 4.000 € por gestionarlo entero. Hay que hacerlo DOS veces. Presupuestarlo y coordinarlo con la ficha de Congo-Brazzaville.",
        "DRON: prohibido en la práctica y con riesgo real de detención y acusación de espionaje. No se saca de la caja en RD Congo. Lo mismo vale, en buena medida, para fotografiar puentes, puertos, presas, instalaciones petroleras, edificios oficiales y uniformados.",
        "Visado de doble entrada: se entra y se sale del país dos veces con meses de diferencia. Confirmar en consulado si el visado admite las dos pasadas o si hay que tramitar el segundo desde Angola (embajada de RD Congo en Luanda), lo que condicionaría el calendario del bloque sur.",
        "Salud: fiebre amarilla obligatoria y comprobada de verdad en frontera; cólera con brotes recurrentes incluyendo Kinshasa; malaria en todo el territorio; mpox (viruela del mono) con RD Congo como epicentro continental desde 2024. El ébola ha reaparecido repetidamente en el país, pero siempre en el norte, centro y este (Équateur, Kasaï, Kivu), nunca en Kongo Central — comprobar de todos modos si hay brote activo antes de entrar, porque condiciona los controles sanitarios en frontera.",
    ],
    ruta_intro=("Corredor único y corto, recorrido dos veces. La <strong>bajada</strong> son unos <strong>445 km</strong> de ferry más N1 (5-7 días contando el día entero que se lleva el cruce del río y las paradas de Kisantu y Mbanza-Ngungu). "
                "La <strong>subida</strong> son unos <strong>940 km</strong> porque añade el bucle de ida y vuelta a la costa atlántica por Boma y Muanda (~480 km) y el desvío a las chutes de Zongo: 7-9 días. "
                "Etapas calculadas sobre la media de <strong>250 km/día</strong> del proyecto, corregidas a la baja en el eje Kinshasa-Matadi por el tráfico de camiones y los controles."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bajada 1 · El cruce del río", "Brazzaville → Beach Ngobila → Kinshasa (Gombe)", "4 km de río · 1 día entero de trámites (prever 2)"),
        ("Bajada 2 · Kinshasa", "Gombe → Marché Central (Zando) → rápidos de Kinsuka", "~40 km urbanos · 2 noches"),
        ("Bajada 3 · N1 hasta el botánico", "Kinshasa → Kasangulu → Kisantu / Inkisi (jardín botánico)", "~120 km · 1 día"),
        ("Bajada 4 · La estación de altura", "Kisantu → Mbanza-Ngungu (grutas, clima fresco)", "~75 km · ½–1 día"),
        ("Bajada 5 · Bajada a la garganta", "Mbanza-Ngungu → Kimpese → Songololo → Matadi (puente Maréchal)", "~155 km · 1 día, tráfico pesado"),
        ("Bajada 6 · Hacia Angola", "Matadi → Songololo → Lufu/Luvo (frontera)", "~95 km · ½ día + frontera"),
        ("Subida 1 · Reentrada", "Luvo/Lufu → Songololo → Matadi", "~95 km · ½ día + frontera"),
        ("Subida 2 · La antigua capital", "Matadi → Boma (arquitectura colonial y baobab de Stanley)", "~130 km · ½–1 día"),
        ("Subida 3 · El Atlántico congoleño", "Boma → Banana / Parque Marino de los Manglares → Muanda", "~110 km · 1–2 noches en la costa"),
        ("Subida 4 · Regreso al eje", "Muanda → Boma → Matadi", "~240 km · 1 día"),
        ("Subida 5 · Cascadas del Inkisi", "Matadi → Kimpese → Mbanza-Ngungu → chutes de Zongo", "~230 km · 1–2 días, pista final de tierra"),
        ("Subida 6 · Periferia de Kinshasa", "Zongo → Lola ya Bonobo → valle del N'sele → Kinshasa", "~130 km · 2 días"),
        ("Subida 7 · Salida", "Kinshasa → Beach Ngobila → Brazzaville", "4 km de río · 1 día de trámites"),
    ],
    offroad=[
        "Honestamente: RD Congo NO es un país de tramos 4x4 míticos en este corredor. La N1 Kinshasa–Matadi es carretera principal asfaltada, y la dificultad del país está en el papeleo, el tráfico y los controles, no en el terreno. Lo que sigue son las únicas pistas reales del trazado.",
        "Pista de acceso a los rápidos de Kinsuka (Kinshasa, Ngaliema): unos pocos kilómetros de pista de tierra y roca desde la carretera de Kinsuka hasta la orilla del río, con tramos de piedra suelta y baches profundos que se convierten en barro rojo con lluvia. Es el único sitio del corredor donde el 4x4 se usa de verdad para llegar a un PDI.",
        "Pista final a las chutes de Zongo: tierra roja desde el desvío del eje de la N1 hasta el complejo de las cascadas; perfectamente transitable en seco, lenta y resbaladiza en temporada húmeda (octubre-mayo). Bajar presiones y no ir con prisa.",
        "Pistas costeras de Muanda y Banana: arena y tierra entre cocoteros para moverse por el litoral y llegar a los embarcaderos del parque de los manglares. Arena blanda cerca de la playa: no aparcar por debajo de la línea de marea alta.",
        "Descenso de Mbanza-Ngungu a Matadi por la N1: aunque es asfalto, es el tramo técnicamente más exigente del corredor para vehículos pesados — pendientes largas, curvas cerradas bajando a la garganta del Congo y una densidad de camiones articulados muy alta. Frenos en buen estado y reducción de marcha: ha habido accidentes graves de camiones en este descenso.",
        "Acceso a las grutas de Mbanza-Ngungu: pistas cortas desde la ciudad, dependientes de guía local; el estado del último tramo varía mucho de una temporada a otra — confirmar en el momento.",
    ],
    senderismo=[
        "Rápidos de Kinsuka (Kinshasa): recorrido a pie por las rocas al borde de las cataratas Livingstone, con el Congo entero rompiendo al lado. Corto pero impresionante. Roca muy resbaladiza por la humedad permanente y corriente absolutamente letal: no acercarse al filo del agua, calzado con suela agarrada y correa corta con el perro.",
        "Jardín Botánico de Kisantu: 225 ha recorribles a pie por avenidas de palmeras, estanques de nenúfares gigantes, bambusal y arboreto tropical. Es un paseo, no una excursión, pero es la mejor manera de estirar las piernas con sombra en todo el eje y funciona perfectamente con el perro atado.",
        "Chutes de Zongo: sendero desde el complejo hasta el mirador y bajada a la poza al pie del salto de 65 m; escalones y roca mojada, y bordes sin proteger. Media mañana.",
        "Grutas de Mbanza-Ngungu: recorrido subterráneo con guía local por las galerías kársticas donde viven los peces ciegos endémicos. Hace falta frontal propio y calzado que se pueda mojar; confirmar sobre el terreno si las escaleras y pasarelas están practicables.",
        "Costa de Muanda: caminata larga por la playa atlántica hasta la desembocadura del Congo, el único litoral del país. Sin sombra, mucho sol: agua de sobra y horario de primera o última hora. Es la excursión a pie más agradable del corredor y la única en la que el perro puede ir suelto.",
        "Paseo del frente fluvial de Boma: recorrido urbano a pie por la arquitectura colonial de la antigua capital hasta el baobab de Stanley y la orilla del río. Una hora, y es la mejor forma de ver la ciudad.",
    ],
    acampada=[
        "Chutes de Zongo: el mejor sitio de acampada del corredor, con diferencia. Complejo hotelero junto a las cascadas con terreno para aparcar y acampar, y la única pernocta del país en la que se duerme oyendo agua en vez de tráfico. Confirmar tarifa y disponibilidad por adelantado.",
        "Muanda (costa atlántica): campamentos y alojamientos sencillos junto a la playa; el mejor sitio del corredor para parar dos noches con el perro. Confirmar en el momento si dejan pernoctar con los vehículos en la arena, y no aparcar nunca por debajo de la marea alta.",
        "Kinshasa: acampada libre descartada por completo. Hotel o guest house con parking cerrado y vigilado en la Gombe, que es además donde se queda el perro cuando salgamos. Es un coste fijo del corredor: presupuestarlo.",
        "Mbanza-Ngungu: la parada más agradable del eje para dormir — a 700 m de altitud, con clima fresco y sin la humedad de Kinshasa ni el calor de Matadi. Hoteles sencillos con aparcamiento.",
        "Matadi: hoteles con aparcamiento; una noche antes de la frontera en la bajada y otra antes del desvío a Boma en la subida. Las cuestas de la ciudad son severas: elegir alojamiento pensando en dónde se aparca.",
        "Boma y Kisantu (misión): alojamiento sencillo con aparcamiento en ambos. La misión de Kisantu, junto al jardín botánico, es una opción tranquila y barata si no se quiere seguir hasta Mbanza-Ngungu.",
        "Acampada libre en la N1: no es recomendable. El eje está muy poblado, muy vigilado y con mucho tráfico nocturno de camiones; no hay lugares discretos. Si hubiera que parar, hacerlo en el recinto de una misión, una parroquia o un hotel, pidiendo permiso.",
    ],
    visado=[
        "Visado previo obligatorio para pasaportes españoles. NO existe visado en frontera para turistas en los pasos terrestres y fluviales: llegar sin visado al Beach Ngobila es quedarse en la orilla.",
        "RD Congo tiene una plataforma de eVisa, pero su aceptación en frontera terrestre/fluvial NO está confirmada (la práctica habitual es que sirva para llegadas aéreas a Kinshasa-N'djili y Lubumbashi). Criterio del proyecto: tramitar el visado en representación consular y llevar el sello físico, sin depender del eVisa. Confirmar 60 días antes.",
        "DOBLE ENTRADA: el país se cruza dos veces con meses de diferencia. Solicitar expresamente visado de entradas múltiples y verificar la validez total (no solo la duración de estancia). Alternativa: tramitar el segundo visado en la embajada de RD Congo en Luanda durante el bloque sur — confirmar que es viable antes de contar con ello.",
        "Documentación típica exigida: pasaporte con 6 meses de validez y páginas libres, formulario, fotos, certificado internacional de fiebre amarilla, reserva o carta de invitación/alojamiento, e itinerario. Los requisitos cambian con frecuencia: verificar directamente con el consulado, no con intermediarios.",
        "Certificado internacional de fiebre amarilla: exigido y comprobado de verdad en la entrada. Llevarlo siempre encima, también en los controles de carretera.",
        "Llevar un dosier con fotocopias de todo, por triplicado. En este país las copias se entregan y los originales no salen de la mano.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Ferry Brazzaville → Beach Ngobila, Kinshasa",
         "Único cruce: NO hay puente. Pasajeros en canot rapide (15-20 min, ~12.400 FCFA); vehículo en la barcaza, con salidas no diarias y cierre los domingos a mediodía. Intervienen DGM, DGDA, OCC, higiene y policía portuaria y municipal. Despacho del vehículo en Kinshasa: de 1 a 3 días. Empezar a primera hora, llevar CFA + CDF + USD limpios, y contratar gestor con precio total acordado por escrito."),
        ("Salida bajada", "Lufu (RDC) → Luvo (Angola)",
         "Desvío al sur desde Songololo, ~30 km. Inmigración congoleña, puente, y puesto angoleño ~500 m después. Descrito como ágil y sin sobornos por overlanders recientes. Confirmar horario y llevar ya el seguro angoleño previsto."),
        ("Entrada subida", "Luvo (Angola) → Lufu (RDC)",
         "Mismo paso en sentido inverso meses después. Comprobar el visado de doble entrada ANTES de presentarse, y rehacer el seguro local congoleño y el laissez-passer del vehículo."),
        ("Salida subida", "Beach Ngobila, Kinshasa → Brazzaville",
         "Segundo cruce del ferry, ahora hacia el norte. Mismo circo administrativo. Coordinar con la ficha de Congo-Brazzaville, que documenta el trámite desde la otra orilla, y reservar el bac con antelación."),
    ],
    vehiculos=[
        "Seguro local de responsabilidad civil OBLIGATORIO: RD Congo no pertenece a CEDEAO (Brown Card) ni a CEMAC (Carte Rose), así que ninguna cobertura regional previa vale aquí. El mercado asegurador congoleño está liberalizado desde 2019 (SONAS y aseguradoras privadas): contratar en Kinshasa nada más despachar el vehículo, y repetirlo en la reentrada desde Angola.",
        "Importación temporal del vehículo: POR CONFIRMAR si RD Congo acepta el Carnet de Passages en Douane o si emite su propio «laissez-passer» / documento de tránsito de la DGDA. Los servicios de gestión del ferry incluyen expresamente «documentación de tránsito» y «permisos de conducción en RDC» entre lo que tramitan, lo que sugiere un procedimiento propio. Preguntar al gestor del ferry con antelación y llevar el CPD igualmente.",
        "Permiso de conducción internacional obligatorio, además del español. Algunos servicios tramitan un permiso local temporal: confirmar si es exigible.",
        "Peajes en el eje Kinshasa-Matadi: la N1 tiene puestos de peaje. Llevar francos congoleños en efectivo y en billetes pequeños; no contar con pagar en dólares en todos ellos.",
        "Dosier del vehículo en la guantera, en copia: permiso internacional, carta verde/seguro local, permiso de circulación, laissez-passer, y matrícula visible. Entregar siempre copias.",
        "Embudo con filtro para repostar: la calidad del gasóleo fuera de las estaciones grandes de Kinshasa y Matadi es irregular.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "NO VOLAR NUNCA en RD Congo, en ningún punto del corredor ni por ningún motivo. No es una recomendación de prudencia: es la norma operativa del proyecto para este país.",
        "El riesgo no es una multa, es la detención y la acusación de espionaje, con la complicación adicional de que el país está en conflicto armado activo y cualquier aparato volador se lee en esa clave.",
        "Objetivos especialmente sensibles en nuestro propio trazado: el puente Maréchal y el puerto de Matadi, las presas de Inga, las instalaciones petroleras de Muanda y Banana, el Beach Ngobila y toda la ribera del río frontera con Congo-Brazzaville, y cualquier edificio oficial o militar de Kinshasa.",
        "Declarar el dron en aduana al entrar y llevarlo embalado y accesible para el registro; intentar ocultarlo es mucho peor que declararlo.",
        "Cámara de fotos: mismo criterio, atenuado. Fotografiar puentes, puertos, presas, instalaciones petroleras, edificios oficiales, policías o militares provoca problemas de forma rutinaria, con permiso oficial o sin él. Fotografiar desde dentro del vehículo, sin ostentación, y guardar la cámara en cualquier control.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo y legal: RD Congo levantó en 2025 la prohibición que había impuesto en 2023 y Starlink entró en operación comercial en mayo-junio de 2025. En 2026, Airtel y SpaceX lanzaron además en el país el primer servicio satélite-a-móvil (direct-to-cell) de África.",
        "Es el respaldo de comunicaciones de este corredor: tenerlo operativo y probado ANTES de entrar, porque el día del ferry y los controles de la N1 son exactamente los momentos en los que hace falta poder avisar a alguien.",
        "Discreción en el despliegue: montar la antena a la vista en un puerto, en un puesto fronterizo o cerca de instalaciones sensibles atrae exactamente la misma atención que un dron. Usarla en el alojamiento o en campamento, no en la cuneta de la N1.",
        "SIM local (Vodacom, Airtel, Orange) como complemento: cobertura razonable en Kinshasa, Matadi y el eje de la N1, más débil en Muanda y en el desvío de Zongo. Registro de SIM con pasaporte.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo. Prever que en el ferry de Kinshasa el servicio de higiene quiera ver los papeles del perro además de los nuestros: llevarlos en el mismo dosier que los certificados de fiebre amarilla.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE). Los requisitos de importación de animales de compañía de RD Congo no están publicados de forma clara y accesible: POR CONFIRMAR con la representación consular al tramitar el visado.",
        "Este país se cruza dos veces: los certificados veterinarios con plazo de validez corto (<10 días) tendrán que rehacerse en Angola antes de la reentrada. Anotarlo en el calendario del bloque sur.",
        "Rabia y leishmaniosis endémicas y muchísimos perros callejeros en Kinshasa: correa siempre, ningún contacto con perros locales, y antiparasitario externo al día. Calor y humedad extremos en Kinshasa y Matadi — los paseos, a primera y última hora.",
        "Ver la matriz por zona más abajo: Muanda es la buena noticia del corredor y Lola ya Bonobo la restricción segura.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional OBLIGATORIO y comprobado de verdad en la entrada, tanto en el ferry como en Lufu. Sin él no se entra.",
        "Malaria: presente en todo el territorio y durante todo el año, incluida Kinshasa urbana. Profilaxis a valorar con Sanidad Exterior, además de mosquiteras y repelente. RD Congo es uno de los dos países del mundo con más casos.",
        "Cólera: brotes recurrentes y graves, con episodios que han alcanzado a Kinshasa. No beber ni lavar verdura con agua de red sin potabilizar; extremar la higiene de manos y desconfiar del hielo y de la comida callejera de dudosa manipulación.",
        "Mpox (viruela del mono): RD Congo es el epicentro continental del brote de clado Ib declarado emergencia de salud pública internacional en 2024. Consultar con Sanidad Exterior la conveniencia de vacunarse; evitar contacto con animales silvestres y con carne de caza.",
        "Ébola: RD Congo ha sufrido más brotes de ébola que ningún otro país, pero SIEMPRE en el norte, centro y este (Équateur, Kasaï, Kivu, Ituri) — nunca en la provincia de Kongo Central, por la que pasa este corredor. Aun así, comprobar 30 días antes si hay brote activo: aunque esté a 1.000 km, un brote endurece los controles sanitarios en frontera y en los aeropuertos, y puede cambiar por completo la experiencia del ferry.",
        "Referencias hospitalarias del corredor: Hôpital Général de Référence y clínicas privadas de la Gombe en Kinshasa; IME Kimpese sobre la propia N1 en el tramo medio; Hôpital de Kinkanda en Matadi. Fuera de Kinshasa, la capacidad real es limitada.",
        "Seguro con evacuación médica internacional imprescindible y verificado para RD Congo expresamente: muchas pólizas excluyen el país o excluyen determinadas provincias. Comprobar la letra pequeña antes de salir de España.",
        "Agua: no beber nunca del grifo. Botella en Kinshasa y Matadi, potabilización propia en el resto.",
    ],
    seguridad_intro=("Lo primero y más importante: el conflicto armado de RD Congo está en el ESTE —Kivu Norte, Kivu Sur e Ituri—, a más de 1.500 km de este corredor, en el extremo opuesto de un país del tamaño de Europa occidental y sin ninguna carretera que conecte razonablemente ambas zonas. "
                     "Nuestro trazado discurre íntegramente por Kinshasa y la provincia de Kongo Central, donde la cuestión no es la guerra sino tres cosas mucho más prosaicas: el tráfico, los controles y el pulso político de la capital."),
    seguridad=[
        "ZONA EXCLUIDA sin excepciones: Kivu Norte (Goma), Kivu Sur (Bukavu), Ituri (Bunia) y en general todo el este y noreste del país. No hay ninguna razón operativa, logística ni de ruta para acercarse: quedan fuera de cualquier variante razonable de este itinerario. Esta ficha no las cubre.",
        "Kinshasa · riesgo político: los acontecimientos del este sí se trasladan a la capital en forma de disturbios. El 28 de enero de 2025, tras la caída de Goma, hubo saqueos y ataques a embajadas en Kinshasa. Antes de entrar y durante la estancia: seguir los avisos consulares y la prensa local, evitar manifestaciones, y tener acordada una ruta de salida por la N1 hacia el oeste.",
        "Kinshasa · delincuencia común: robos con violencia y bandas juveniles («kuluna») en determinados barrios, sobre todo de noche. No caminar de noche, no llevar reloj ni teléfono a la vista, no conducir de noche por la periferia, y aparcar siempre en recinto cerrado y vigilado.",
        "N1 Kinshasa–Matadi · el riesgo real es la carretera: densidad altísima de camiones articulados del puerto de Matadi, adelantamientos temerarios, vehículos sin luces y un descenso largo y empinado a la garganta del Congo. No conducir de noche en ningún tramo, mantener distancia con los camiones y convoy cerrado entre los dos vehículos.",
        "Controles y peticiones de dinero: numerosos puestos de policía, DGM, ANR y peaje en el eje. Protocolo: carpeta con copias de todo, entregar copia y no original, francés y calma, nada de prisa, no enseñar dinero, y anotar educadamente nombre y puesto. Presupuestar un margen para «tasas» irreductibles y no convertirlo en un conflicto.",
        "Nada de fotos ni de drones en el puerto y el puente de Matadi, las presas de Inga, las instalaciones petroleras de Muanda y Banana, el Beach Ngobila y cualquier edificio oficial o militar. Es la causa más habitual de un problema serio con las autoridades en este país.",
        "Ribera del río frontera: el Congo es la frontera con Congo-Brazzaville y está vigilado. No acercarse a la orilla con cámaras ni de noche fuera de los puntos habilitados.",
        "Check-in diario del convoy y comunicación de la ruta a la embajada de España en Kinshasa, especialmente las fechas de los dos cruces del ferry.",
    ],
    agua=[
        "Kinshasa: agua embotellada sin problema de suministro en los supermercados de la Gombe — cargar aquí la reserva de boca para todo el corredor, porque es donde está más barata y con más garantía.",
        "NO beber agua de red en ningún punto del corredor sin potabilizar: hay brotes recurrentes de cólera, incluidos episodios en la propia Kinshasa. Filtro y desinfección propios, siempre.",
        "Recarga del depósito de uso general (ducha, aseo, vajilla, limpieza): hoteles y estaciones de servicio de Kinshasa, Mbanza-Ngungu y Matadi permiten llenar con manguera; pedirlo en recepción. Mbanza-Ngungu, más tranquila y fresca, es el mejor sitio para hacerlo con calma.",
        "Muanda y Boma: confirmar sobre el terreno; el agua de la zona costera es de calidad variable y conviene llegar con los depósitos llenos desde Matadi para el bucle de ida y vuelta.",
        "Zongo: el complejo de las cascadas suele poder facilitar agua para el depósito general; confirmar al reservar.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en ninguna de las dos pasadas. Bajada: Kinshasa → Kisantu (~120 km) → Mbanza-Ngungu (~75 km) → Kimpese → Matadi (~155 km) → Lufu/Luvo (~95 km), con estaciones formales en todos los núcleos.",
        "Subida: el único tramo a vigilar es el bucle costero Matadi → Boma → Muanda → Boma → Matadi (~480 km ida y vuelta). Boma y Muanda tienen estaciones (Muanda es zona petrolera), pero con existencias menos garantizadas: salir de Matadi con el depósito lleno y una garrafa de reserva.",
        "Repostar a fondo en Kinshasa antes de salir a la N1 y de nuevo en Matadi antes de la frontera: son las dos plazas con mejor calidad y oferta del corredor.",
        "Embudo con filtro obligatorio fuera de las estaciones grandes: la calidad del gasóleo es irregular y el agua en el combustible es un problema recurrente en la región.",
        "Llevar efectivo: no dar por hecho el pago con tarjeta en ninguna estación fuera de la Gombe.",
    ],
    experiencias_intro=("Relatos y datos reales de otros viajeros sobre el corredor occidental de RD Congo, para contrastar con la planificación oficial de esta ficha. "
                        "Casi todo lo que cuentan gira en torno al mismo asunto: el cruce del río."),
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Ferry · precio real del vehículo", "Obtener al menos tres presupuestos escritos (gestor independiente, agencia local y ONATRA/CNTF) para el cruce de los DOS vehículos, ida y vuelta, con desglose de tasas. La referencia alta conocida son los 4.000 €/vehículo del servicio VIP de Congo Travel & Tours: no aceptarla como precio de mercado sin haber buscado alternativa."),
        ("Ferry · calendario de la barcaza", "Confirmar los días y horas reales de salida del bac de vehículos y si hay que reservar plaza con antelación; el pasaje de personas es diario, el de vehículos no. Coordinar con la ficha de Congo-Brazzaville."),
        ("Ferry · despacho del vehículo en Kinshasa", "Confirmar cuántos días tarda realmente el despacho de aduanas (referencia: 1-3 días) y dónde se guardan los vehículos mientras tanto, porque condiciona el número de noches de hotel en la Gombe."),
        ("Visado de doble entrada", "Confirmar en consulado si se puede obtener visado de entradas múltiples con validez suficiente para las dos pasadas, o si hay que tramitar el segundo en la embajada de RD Congo en Luanda. Es la decisión documental que más condiciona el calendario del bloque sur."),
        ("eVisa · validez en frontera fluvial", "Confirmar expresamente si el eVisa de RD Congo se acepta en el Beach Ngobila y en Lufu, o solo en llegadas aéreas. Criterio provisional: no depender de él."),
        ("Importación temporal del vehículo", "Aclarar si RD Congo acepta el CPD o exige laissez-passer propio de la DGDA, y si hace falta permiso de conducir local temporal. Preguntarlo al gestor del ferry al pedir presupuesto."),
        ("Seguro local", "Confirmar dónde y cómo se contrata el seguro obligatorio de responsabilidad civil al desembarcar en Kinshasa, y el coste para dos vehículos; repetir el trámite en la reentrada desde Angola."),
        ("Perro · requisitos de importación", "Los requisitos veterinarios de entrada de RD Congo no están publicados de forma clara: confirmarlos con la representación consular al tramitar el visado, y prever rehacer el certificado veterinario en Angola antes de la reentrada."),
        ("Lola ya Bonobo · visita y perro", "Escribir al santuario para confirmar días y horarios de apertura al público en 2027, tarifa, si se puede llegar con vehículo propio y —dando por hecho que no— dónde queda el perro durante la visita."),
        ("Nsele Valley Park", "Confirmar si admite vehículo propio, tarifa de entrada y política de mascotas; si no, sustituir la etapa por un día extra en Muanda."),
        ("Parque Marino de los Manglares", "Contactar con el ICCN en Muanda para confirmar cómo se organiza la salida en piragua, el coste y si hay que reservar."),
        ("Grutas de Mbanza-Ngungu", "Confirmar sobre el terreno si el acceso está practicable y quién guía; la infraestructura es intermitente."),
        ("Dron", "Decisión ya tomada: NO se vuela en RD Congo. Pendiente solo decidir si se declara en aduana o si se deja precintado, y comprobar que la póliza cubre su retención temporal."),
        ("Pulso político de Kinshasa", "Revisar avisos consulares y prensa local 30 días antes de cada una de las dos entradas, y de nuevo 72 h antes: el precedente de enero de 2025 (disturbios y saqueos tras la caída de Goma) obliga a comprobarlo cada vez."),
        ("Brote sanitario activo", "Comprobar 30 días antes de cada entrada si hay brote de ébola, mpox o cólera declarado: aunque el foco esté a 1.000 km, endurece los controles sanitarios de frontera."),
        ("Fotos pendientes de sustituir", "Las grutas de Mbanza-Ngungu, Lola ya Bonobo y los rápidos de Kinsuka usan imágenes de referencia de su región o de la especie, no del propio sitio: sustituir por fotos propias cuando las tengamos."),
    ],
    sources=SOURCES,
    sources_note=("Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. "
                  "Cubre EXCLUSIVAMENTE el corredor occidental de tránsito (Kinshasa, Kongo Central, Matadi, Boma, Muanda y la frontera de Lufu/Luvo); "
                  "no cubre ni es aplicable en absoluto al este del país (Kivu Norte, Kivu Sur, Ituri), en conflicto armado activo y a más de 1.500 km de esta ruta."),
    emergency="Emergencia consular española (Kinshasa): +243 819 500 289 · Embajada: +243 813 300 061.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

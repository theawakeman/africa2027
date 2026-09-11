# -*- coding: utf-8 -*-
"""Zambia — ficha completa (11 sep 2026): primer país del bucle, Angola -> Tanzania."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== OESTE: entrada desde Angola por Chavuma/Caripande, Barotseland =====
    dict(n=1, name="Parque Nacional de Liuwa Plain", cat="Naturaleza", prio="Alta", dog="prohibido", time="2–3 días",
         lat=-14.6000, lon=22.6000,
         desc="Llanura inmensa en el extremo oeste, gestionada por African Parks, que alberga la SEGUNDA MAYOR MIGRACIÓN DE ÑUS DE ÁFRICA (unos 45.000 animales) además de una célebre población de hienas y el regreso de los leones tras la guerra. Está a un paso de la frontera angoleña, así que encaja justo al entrar y no exige desviarse. Solo 4x4 y solo en temporada seca: en lluvias la llanura se inunda por completo. Imagen: vista satelital de la llanura del Barotse, el mismo sistema de inundación — pendiente de sustituir por una foto del parque.",
         credit="NASA · Wikimedia Commons", source=W + "NASA%20Barotse%20Floodplain%20compressed.JPG?width=900"),
    dict(n=2, name="Mongu y la llanura del Barotse (Kuomboka)", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-15.2667, lon=23.1333,
         desc="Capital de Barotseland y corazón del reino lozi, todavía gobernado por el Litunga. Cada año, cuando sube la crecida del Zambeze, se celebra la KUOMBOKA: el traslado del rey desde el palacio de Lealui a tierras altas a bordo del Nalikwanda, una enorme barcaza negra y blanca remada por decenas de hombres. Es una de las grandes ceremonias vivas de África; la fecha depende de la crecida (suele caer entre marzo y abril). La llanura inundada, con su dique-carretera hasta el puerto, es un paisaje único.",
         credit="Wikimedia Commons", source=W + "Nalikwanda.jpg?width=900"),
    dict(n=3, name="Parque Nacional de Kafue · llanuras de Busanga", cat="Naturaleza", prio="Alta", dog="prohibido", time="3–4 días",
         lat=-14.1000, lon=25.8000,
         desc="El parque más grande de Zambia (22.400 km², como Gales) y uno de los más grandes de África, con las llanuras de Busanga en el norte como joya: praderas inundables con manadas de antílopes, leones trepadores de árboles y globos aerostáticos al amanecer. El acceso norte a Busanga es de pista de arena y vados, solo seco (julio-octubre); el sur, por el embalse de Itezhi-Tezhi, es más accesible.",
         credit="Wikimedia Commons", source=W + "The%20Kafue%20River%2C%20Zambia.jpg?width=900"),
    # ===== CENTRO =====
    dict(n=4, name="Lusaka", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=-15.4067, lon=28.3050,
         desc="Capital y gran plaza logística del tramo: talleres, recambios de 4x4, neumáticos, supermercados grandes, hospital de referencia (University Teaching Hospital) y trámites. Es el punto donde conviene revisar los vehículos antes de encarar el norte remoto y el circuito de cascadas.",
         credit="Wikimedia Commons", source=W + "Lusaka%2C%20Zambia%20CBD%20Kafue%20Roundabout.jpg?width=900"),
    # ===== DESVÍO SUR (variante): Victoria Falls y el Zambeze =====
    dict(n=5, name="Cataratas Victoria · lado zambiano (Mosi-oa-Tunya)", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=-17.9244, lon=25.8572,
         desc="La vista zambiana de las cataratas, Patrimonio de la Humanidad, desde Livingstone: menos panorámica que la zimbabuense pero con acceso a la Knife Edge Bridge y, sobre todo, a DEVIL'S POOL, la piscina natural al borde mismo del salto, accesible solo en aguas bajas (aprox. agosto-enero) y solo desde este lado. OJO: la ruta global pasa por Zimbabue meses más tarde, donde se ve la panorámica — ver los pendientes antes de decidir el desvío.",
         credit="Matti Blume · CC BY-SA 4.0", source=W + "Mosi-oa-Tunya%2C%20Livingstone%20%2820260519-P1075699%29.jpg?width=900"),
    dict(n=6, name="Garganta del Batoka y puente de Victoria Falls", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="½–1 día",
         lat=-17.9283, lon=25.8575,
         desc="El puente de 1905 sobre la garganta, frontera con Zimbabue, y el cañón de basalto aguas abajo: uno de los mejores tramos de rafting de aguas bravas del mundo (rápidos de clase V, practicable en aguas bajas, aprox. agosto-enero) y de puenting desde el propio puente. Se puede caminar el puente sin trámite de frontera con un pase de visitante.",
         credit="Wikimedia Commons", source=W + "Victoria%20falls%2C%20zambia.jpg?width=900"),
    # ===== ESTE: valle del Luangwa =====
    dict(n=7, name="Parque Nacional de South Luangwa (Mfuwe)", cat="Naturaleza", prio="Alta", dog="prohibido", time="3–4 días",
         lat=-13.0833, lon=31.9500,
         desc="LA CUNA DEL SAFARI A PIE: aquí lo inventó Norman Carr en los años 50, y sigue siendo el mejor sitio de África para hacerlo. Una de las densidades de leopardo más altas del continente, manadas enormes de búfalo, y el valle del Luangwa con sus meandros y lagunas. Mfuwe es la puerta logística, con aeródromo, campamentos y lodges.",
         credit="Timothy A. Gonsalves · CC BY-SA 4.0", source=W + "Giraffe%20Standing%20Lupande%20Zambia%20Jul23%20A7C%2006176.jpg?width=900"),
    # ===== NORTE: Great North Road, humedales y circuito de cascadas =====
    dict(n=8, name="Parque Nacional de Kasanka · migración de murciélagos", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 días",
         lat=-12.5833, lon=30.2500,
         desc="Cada año, entre finales de octubre y diciembre, unos 10 MILLONES de murciélagos frugívoros de color pajizo se concentran en apenas una hectárea de bosque pantanoso de mushitu: es LA MAYOR MIGRACIÓN DE MAMÍFEROS DEL PLANETA, más grande en número que la de ñus del Serengeti. Al atardecer el cielo se llena durante casi una hora. Hay plataformas en los árboles para verlo. El parque es pequeño y se autofinancia; también tiene sitatungas y el raro antílope puku. Imagen: ejemplar de la especie (Eidolon helvum), no del propio parque.",
         credit="Wikimedia Commons", source=W + "Eidolon%20helvum%20fg01.JPG?width=900"),
    dict(n=9, name="Humedales de Bangweulu · el picozapato", cat="Naturaleza", prio="Alta", dog="prohibido", time="2–3 días",
         lat=-11.5000, lon=30.2500,
         desc="Unos 10.000 km² de llanura inundable gestionados por African Parks junto a las comunidades locales, y uno de los pocos lugares del mundo donde se puede ver el PICOZAPATO (shoebill), el ave más extraña de África. Además, la mayor población mundial de lechwe negro (unos 50.000, endémico de aquí) y tsessebe. Mejor entre mayo y julio (agua bajando, picozapatos aún presentes; desde septiembre se vuelven muy difíciles). Acceso 4x4 de altura, 66 km de pista desde el desvío; salir con depósito lleno desde Serenje o Mpika. Tasa de 10 USD/adulto, horario 05:00-18:00. Imagen: ejemplar de la especie, no del propio humedal.",
         credit="Wikimedia Commons", source=W + "Shoebill%20couple1.jpg?width=900"),
    dict(n=10, name="Cataratas de Ntumbachushi", cat="Naturaleza", prio="Media", dog="permitido", time="1 noche",
         lat=-9.8000, lon=29.1000,
         desc="A 18 km de Kawambwa, un salto en velo de novia al borde de la meseta norte, declarado monumento nacional, con senderos arriba y abajo del salto, pozas de agua cristalina para bañarse y zona de acampada con barbacoas. Una de las paradas mejor mantenidas del circuito de cascadas. Imagen: otra cascada del norte de Zambia — pendiente de sustituir por una de Ntumbachushi.",
         credit="Wikimedia Commons", source=W + "Chilambwe%20falls%20Northern%20Zambia.jpg?width=900"),
    dict(n=11, name="Cataratas de Lumangwe y Kabwelume", cat="Naturaleza", prio="Alta", dog="permitido", time="1–2 noches",
         lat=-9.5333, lon=29.3833,
         desc="Lumangwe es una cortina de 160 m de ancho sobre el río Kalungwishi que se conoce como «la pequeña Victoria Falls», y a solo 6 km está Kabwelume, de 150 m, con una sucesión de saltos y pozas que muchos viajeros consideran aún más bonita. Se llega por pista (4x4) desde Mporokoso; hay camping sencillo y limpio junto a Lumangwe por unos 15 USD por persona. Para los overlanders que hacen el circuito norte, estas dos son habitualmente lo mejor del viaje.",
         credit="Wikimedia Commons", source=W + "Lumangwe%20falls%20on%20the%20Kalungwishi%20river%20during%20the%20dry%20season(September-October).jpg?width=900"),
    dict(n=12, name="Cataratas de Chishimba", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-10.1167, lon=30.9333,
         desc="A media hora de Kasama, tres saltos sucesivos (Mutumuna, los rápidos de Kaela y Chishimba propiamente) unidos por senderos bien marcados y mantenidos, con camping en el recinto. Es además un LUGAR SAGRADO BEMBA: conviene informarse del protocolo y comportarse en consecuencia, no es solo un sitio bonito.",
         credit="Wikimedia Commons", source=W + "Chisimba%20Falls.JPG?width=900"),
    dict(n=13, name="Lago Tanganyika y Mpulungu", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=-8.7667, lon=31.1167,
         desc="El lago más largo del mundo y el segundo más profundo, con agua transparente, cíclidos endémicos de colores y playas de arena en la orilla zambiana. Mpulungu es el único puerto del país y de aquí sale el histórico ferry MV Liemba hacia Tanzania. Buen sitio para parar varios días, nadar (con cuidado: hay cocodrilos en algunas zonas, preguntar siempre en el alojamiento) y descomprimir antes de la frontera.",
         credit="Wikimedia Commons", source=W + "Lake%20Tanganyika.jpg?width=900"),
    dict(n=14, name="Cataratas de Kalambo (235 m)", cat="Naturaleza", prio="Alta", dog="permitido con correa", time="1 día",
         lat=-8.6000, lon=31.2333,
         desc="Caída libre de 221-235 m sobre la frontera con Tanzania, la SEGUNDA CASCADA CONTINUA MÁS ALTA DE ÁFRICA, cayendo a una garganta boscosa sobre el valle del Tanganyika. Además es uno de los yacimientos arqueológicos más importantes del continente: se han datado restos de uso del fuego y herramientas de hace cientos de miles de años. Se llega a pie desde el lago (o en 4x4 por la meseta); sin vallas en el borde, correa corta y atención con el perro.",
         credit="Wikimedia Commons", source=W + "Kalambo%20Falls.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul", "cultura": "morado", "costa": "turquesa"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Chavuma/Caripande (desde Angola)", "Frontera", -13.0833, 22.6833,
     "Paso remoto del noroeste, frente al puesto angoleño de Caripande. Pistas de arena con charcos profundos en el lado angoleño; en el zambiano mejora hacia Zambezi town. Solo temporada seca (mayo-septiembre). Las cataratas de Chavuma, sobre el Zambeze, están junto al propio paso y merecen la parada. Confirmar horario (suele 07:00-18:00) y que el puesto emite visado en frontera."),
    ("Frontera · Salida — Nakonde/Tunduma (hacia Tanzania)", "Frontera", -9.3333, 32.7500,
     "El gran paso del corredor TANZAM, el más transitado del norte: mucho camión, colas y gestores informales. Puesto de ventanilla única. Llegar temprano y contar con varias horas; vigilar la documentación del vehículo en todo momento."),
    ("Embajada de España en Harare (competente para Zambia)", "Consular", -17.8216, 31.0492,
     "16 Phillips Ave., Belgravia, Harare (Zimbabue). Tel. +263 (0)242 250740/1; emergencias +263 (0)772 436 620. Gestionar trámites mayores a través de esta embajada."),
    ("University Teaching Hospital, Lusaka", "Hospital", -15.4067, 28.3050,
     "Principal hospital de referencia del país en la capital; para necesidades serias, la evacuación hacia Sudáfrica es la práctica habitual en la región."),
    ("Hospital general de Kasama (norte)", "Hospital", -10.2129, 31.1808,
     "Referencia sanitaria del circuito de cascadas y del tramo de Tanganyika; lo más cercano a Mpulungu, Kalambo y Chishimba."),
    ("Combustible · Mongu (oeste)", "Combustible", -15.2667, 23.1333,
     "Única oferta formal fiable del oeste: repostar a fondo aquí tanto al entrar desde Angola como antes de cruzar hacia Kafue. Entre la frontera y Mongu no hay garantía ninguna."),
    ("Combustible · Lusaka", "Combustible", -15.4067, 28.3050,
     "Mejor oferta y calidad del país, con todas las marcas y gasóleo fiable. Punto de repostaje a fondo antes del norte."),
    ("Combustible · Serenje / Mpika (Great North Road)", "Combustible", -11.8333, 31.4500,
     "Las dos plazas del eje norte y el último suministro seguro antes de Bangweulu y Kasanka: African Parks recomienda expresamente salir de aquí con el depósito lleno y provisiones."),
    ("Combustible · Kasama / Mbala (norte)", "Combustible", -10.2129, 31.1808,
     "Oferta razonable en el norte profundo; repostar antes de meterse en el circuito de cascadas (Mporokoso, Kawambwa) donde la oferta es irregular."),
    ("Kawambwa · provisiones del circuito de cascadas", "Servicio", -9.7833, 29.0833,
     "Panaderías y tiendas de alimentación: el único reabastecimiento real entre las cascadas de Lumangwe, Kabwelume y Ntumbachushi."),
    ("Agua potable y de uso general · Lusaka y Livingstone", "Agua potable", -15.4067, 28.3050,
     "Agua embotellada sin problema en ambas; lodges y campings permiten llenar el depósito de uso general con manguera. En el valle del Luangwa y el norte rural, confirmar potabilidad antes de beber."),
    ("Agua · campings de cascadas (norte)", "Agua potable", -9.5333, 29.3833,
     "Lumangwe, Ntumbachushi y Chishimba tienen camping con aseos y agua corriente; tratarla antes de beber. Las pozas son de agua cristalina pero no potable sin filtrar."),
]

DRONE_CALLOUT = ("danger", "Prohibido en la práctica en parques nacionales y muy restringido en general",
                  "Zambia exige registro y permiso previo de la Zambia Civil Aviation Authority para cualquier uso de drones, y su uso dentro de parques nacionales (incluidos Mosi-oa-Tunya/Victoria Falls, South Luangwa, Kafue, Kasanka y Bangweulu) está prohibido salvo autorización expresa y muy excepcional. Norma del proyecto: no volar el dron en ningún parque o reserva sin autorización expresa ya concedida.")

STARLINK_CALLOUT = ("ok", "Disponible y operativo en 2026",
                     "Starlink está activo comercialmente en Zambia desde 2023, con cobertura razonable incluso en zonas remotas como South Luangwa o el norte; kit y suscripción configurables antes de entrar al país. Es el país del bucle donde mejor resuelto está el tema de conectividad.")

DOG_MATRIX = [
    ("Cascadas del norte: Lumangwe, Kabwelume, Ntumbachushi, Chishimba, Kalambo", "permitido",
     "Son monumentos nacionales y sitios gestionados localmente, NO parques nacionales: el perro puede entrar. Es la mejor parte de Zambia con el perro. Correa corta en los bordes de salto (sin vallas) y atención con los cocodrilos en los ríos de abajo."),
    ("Lago Tanganyika (Mpulungu), Mongu, Lusaka, Livingstone", "permitido con condiciones",
     "Sin restricción específica; calor fuerte en el valle del Tanganyika y en la estación seca-cálida (septiembre-noviembre). Preguntar en el alojamiento por cocodrilos antes de dejar que se acerque al agua."),
    ("Todos los parques nacionales: Liuwa, Kafue, South Luangwa, Kasanka, Bangweulu, Mosi-oa-Tunya", "prohibido",
     "El DNPW no permite mascotas en parques nacionales, y en Liuwa/Bangweulu (African Parks) tampoco. Plan B: turnos entre los tres viajeros dejando a uno con el perro en el camping de la puerta, o guardería en Livingstone, Mfuwe y Lusaka, que son las únicas plazas con ese servicio."),
]

SOURCES = [
    ("Gobierno de Zambia · Zambia Immigration Department, requisitos de visado", "https://www.zambiaimmigration.gov.zm/"),
    ("Zambia Wildlife Authority (DNPW) · normativa de parques nacionales", "https://www.dnpw.gov.zm/"),
    ("Zambia Civil Aviation Authority · normativa de drones", "https://www.zcaa.co.zm/"),
    ("KAZA Univisa · información oficial de la visa conjunta Zambia-Zimbabue", "https://www.kazatransfrontier.org/"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("iOverlander · puntos de combustible, agua y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
    ("Tracks4Africa Blog · la ruta de las cascadas del norte de Zambia y el lago Tanganyika", "https://blog.tracks4africa.co.za/zambia-on-two-wheels-part-2-waterfall-route/"),
    ("Whole Food Abroad · guía del circuito norte de Zambia, 15 lugares imprescindibles", "https://www.wholefoodabroad.com/post/a-travel-guide-to-the-northern-circuit-in-zambia-15-must-see-places"),
    ("Zambia Tourism (web oficial de turismo) · Parque Nacional de Liuwa Plain", "https://www.zambiatourism.com/destinations/national-parks/liuwa-plains-national-park/"),
    ("Zambia Tourism (web oficial de turismo) · cascadas de Zambia", "https://www.zambiatourism.com/destinations/waterfalls/"),
    ("African Parks · Liuwa Plain", "https://www.africanparks.org/the-parks/liuwa-plain"),
    ("African Parks · visitar Bangweulu (accesos, tasas, temporada, picozapato)", "https://www.africanparks.org/the-parks/bangweulu/visit-bangweulu"),
    ("Africa Geographic · la migración de murciélagos de Kasanka", "https://africageographic.com/stories/kasanka-bat-migration/"),
    ("Smithsonian Magazine · Kasanka, la mayor migración de mamíferos del planeta", "https://www.smithsonianmag.com/travel/the-worlds-largest-mammal-migration-is-taking-place-in-zambia-right-now-180985530/"),
    ("Trans Africa Self Drive · ruta de grandes lagos y cascadas del norte de Zambia", "https://tasda.co.za/northen-zambia/"),
    ("Wikipedia · Kalambo Falls", "https://en.wikipedia.org/wiki/Kalambo_Falls"),
    ("Wikipedia · Lumangwe Falls", "https://en.wikipedia.org/wiki/Lumangwe_Falls"),
    ("Wikipedia · Chisimba Falls", "https://en.wikipedia.org/wiki/Chisimba_Falls"),
    ("Wikipedia · Ngonye Falls", "https://en.wikipedia.org/wiki/Ngonye_Falls"),
    ("UNESCO · Mosi-oa-Tunya / Victoria Falls, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/509/"),
]

# Principal: frontera de Angola (NO) -> Barotseland -> Kafue -> Lusaka -> norte -> frontera de Tanzania (NE)
CORRIDOR = [(-13.0833, 22.6833), (-14.6000, 22.6000), (-15.2667, 23.1333), (-14.1000, 25.8000),
            (-15.4067, 28.3050), (-13.2333, 30.2333), (-12.5833, 30.2500), (-11.5000, 30.2500),
            (-11.8333, 31.4500), (-13.0833, 31.9500), (-11.8333, 31.4500), (-9.8000, 29.1000),
            (-9.5333, 29.3833), (-10.1167, 30.9333), (-8.7667, 31.1167), (-8.6000, 31.2333),
            (-8.8333, 31.3667), (-9.3333, 32.7500)]

# Variante sur: desvío a las Cataratas Victoria y el Zambeze desde Lusaka
CORRIDOR_ALT = [(-15.4067, 28.3050), (-16.5333, 28.7167), (-17.8419, 25.8543), (-17.9244, 25.8572),
                (-17.9283, 25.8575), (-15.4067, 28.3050)]

EXPERIENCIAS = [
    "Circuito de cascadas del norte (blog de Tracks4Africa): el orden que funciona es Kalambo → Chishimba → Kabwelume → Lumangwe → Ntumbachushi → Bangweulu bajando hacia Samfya. Estado de las carreteras según ellos: la M1/M2 hasta Mbala es asfalto con baches; la D19/D20 hacia Mporokoso, asfalto excelente; de Mporokoso a Kabwelume, «tierra bastante mala» con tramos de arena donde hay que elegir la trazada; la D19 hacia el sur hasta Kawambwa, pista de tierra excelente y recién mejorada; y la D235 junto a los pantanos de Bangweulu, destrozada a lo largo de unos 100 km. Calculan tres semanas como mínimo para el circuito completo.",
    "Camping en las cascadas (mismos viajeros): Lumangwe cobra unos 15 USD por persona y lo describen como sencillo, impecable y con buenos aseos; Chishimba es más básico y con instalaciones de lavado limitadas; Ntumbachushi tiene pozas de agua cristalina para bañarse. Kawambwa es el único sitio del tramo con panaderías y tiendas para reabastecerse.",
    "Chishimba es lugar sagrado bemba: los viajeros que lo han visitado insisten en que no se trata solo de un paraje bonito y que conviene preguntar por el protocolo local y comportarse en consecuencia.",
    "Bangweulu en autoconducción (información oficial de African Parks, contrastada con viajeros): hay dos accesos, el principal desde la Great North Road girando en el cartel 12 km al norte del ferrocarril de Kalonje y después 66 km de pista, y uno alternativo solo en seco vía Kasanka y Lake Waka Waka. Recomiendan 4x4 de buena altura libre y avisan de que las condiciones cambian de un año a otro: conviene llamar a la sede de Nkondo antes de ir. Sin combustible en toda la zona.",
    "Chipota Falls (guía del circuito norte): desvío muy fácil de encajar, 12 km después de Serenje girando a la derecha en el cartel; pista de grava y roca con un aparcamiento básico donde se puede acampar. Buena primera parada al salir de Lusaka hacia el norte.",
    "Mumbuluma y Musonda Falls (mismo circuito): Mumbuluma está a 40 minutos de Mansa, es monumento nacional, tiene zona de acampada muy bien mantenida y la entrada cuesta entre 5 y 8 kwacha; Musonda queda 20 minutos más allá y exige una caminata corta por roca, sin entrada formal.",
    "Perro y parques: ningún parque nacional zambiano admite mascotas, pero las cascadas del norte (Lumangwe, Kabwelume, Ntumbachushi, Chishimba, Kalambo) son monumentos nacionales gestionados localmente y sí se puede entrar con el perro — por eso el circuito norte es, con diferencia, la mejor parte de Zambia para nosotros.",
]

HISTORIA_RESUMEN = ("Zambia, antigua Rodesia del Norte, alcanzó la independencia en 1964 bajo el liderazgo de Kenneth Kaunda sin el conflicto armado que marcó a su vecina Rodesia del Sur (actual Zimbabue), y ha mantenido desde entonces "
                     "una trayectoria política relativamente estable, sostenida sobre todo por el cobre y, cada vez más, por el turismo de naturaleza en torno a las Cataratas Victoria y los grandes parques del valle del Luangwa y el Zambeze.")

HISTORIA_SECCIONES = [
    ("Reinos e imperios previos a la colonización",
     "El territorio de la actual Zambia estuvo habitado por pueblos bantúes organizados en reinos como el Lozi (en la llanura de Barotseland, sobre el alto Zambeze) y el Bemba (en el noreste), con sistemas políticos centralizados y redes comerciales "
     "que conectaban el interior con la costa índica mucho antes de la llegada europea. El reino lozi sigue vivo hoy: su rey, el Litunga, continúa celebrando cada año la ceremonia de la Kuomboka cuando el Zambeze inunda la llanura."),
    ("Rodesia del Norte y el peso del cobre",
     "El territorio fue administrado por la British South Africa Company de Cecil Rhodes desde finales del siglo XIX y pasó a ser colonia británica directa como Rodesia del Norte en 1924. El descubrimiento de enormes yacimientos de cobre en el Copperbelt "
     "convirtió a la colonia en un motor económico regional, con mano de obra africana en condiciones duras y una minoría blanca que dominaba la explotación minera y la vida política."),
    ("Independencia sin guerra, bajo Kenneth Kaunda",
     "A diferencia de Rodesia del Sur, Rodesia del Norte alcanzó la independencia por vía pacífica en 1964 como Zambia, bajo el liderazgo de Kenneth Kaunda, quien gobernaría durante 27 años con un proyecto de «humanismo zambiano» y un papel activo "
     "como refugio y base de apoyo para movimientos de liberación de países vecinos (incluida la lucha contra el apartheid y contra el régimen de Ian Smith en Rodesia)."),
    ("Situación actual: transición democrática y economía del cobre y el turismo",
     "Zambia transitó al multipartidismo en 1991 y ha vivido desde entonces alternancias pacíficas en el poder, incluida la derrota electoral del presidente saliente en 2021, un hecho valorado como signo de salud democrática en la región. "
     "La economía sigue muy dependiente del cobre, con episodios de deuda y renegociación en los últimos años, mientras el turismo de naturaleza crece como fuente complementaria de ingresos."),
]

HISTORIA_FUENTES = [
    ("BBC News · Zambia country profile", "https://www.bbc.com/news/world-africa-14113019"),
    ("Encyclopaedia Britannica · Zambia, History", "https://www.britannica.com/place/Zambia/History"),
    ("UNESCO · Mosi-oa-Tunya / Victoria Falls, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/509/"),
]

SPEC = dict(
    slug="zambia", name="Zambia", revision="11 sep 2026",
    sub="Primer país del bucle de exploración · Angola → Tanzania",
    chips=[
        ("RUTA", "Chavuma/Caripande (Angola) → Barotseland → Lusaka → norte → Nakonde (Tanzania) · ~3.200 km"),
        ("VARIANTE", "Desvío sur a las Cataratas Victoria y Devil's Pool desde Lusaka"),
        ("PDIs", "14 puntos, del Barotseland al lago Tanganyika"),
        ("IMPRESCINDIBLE", "Kasanka: 10 millones de murciélagos, la mayor migración de mamíferos del planeta"),
        ("A PIE", "Circuito de cascadas del norte · Kalambo · senderos de Chishimba"),
        ("PERRO", "Cascadas del norte SÍ (son monumentos, no parques) · parques nacionales no"),
        ("COMUNICACIONES", "Starlink activo desde 2023 (ok)"),
        ("TEMPORADA", "El oeste (Liuwa, Barotseland) solo en seco, mayo–septiembre"),
    ],
    center=[-12.5, 27.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Travesía principal", corridor_alt_label="Variante sur (Victoria Falls)",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Zambia abre el bucle de exploración y es una de las grandes sorpresas de la ruta: se entra por el extremo noroeste "
                   "desde Angola, se cruza el reino lozi del Barotseland, se atraviesa el país por Kafue y Lusaka y se sube al norte profundo, "
                   "donde están la mayor migración de mamíferos del planeta (los 10 millones de murciélagos de Kasanka), el picozapato de Bangweulu, "
                   "un circuito de cascadas espectacular y casi desconocido, y el lago Tanganyika. Son unos <strong>3.200 km</strong> de travesía "
                   "(13-16 días a 250 km/día, más los días de parada), con un desvío sur opcional a las Cataratas Victoria."),
    facts=[
        ("Rol en la ruta", "Primer país del bucle de exploración, entre Angola y Tanzania. Se cruza una sola vez, de suroeste a noreste."),
        ("Entrada", "Chavuma/Caripande desde Angola: paso remoto del noroeste, pistas de arena, solo temporada seca."),
        ("Salida", "Nakonde/Tunduma hacia Tanzania: el gran paso del corredor TANZAM, muy transitado."),
        ("Variante sur", "Desvío desde Lusaka a Livingstone (Cataratas Victoria, Devil's Pool) y el lago Kariba: ~950 km ida y vuelta."),
        ("Visado", "Visado de turista en frontera para españoles. El KAZA Univisa (Zambia+Zimbabue, 30 días) ya NO encaja con esta ruta: Zimbabue se visita meses después."),
        ("Temporada", "Crítico: el oeste (Liuwa, Barotseland) y las llanuras de Busanga solo son practicables en seco (mayo-septiembre/octubre). Kasanka exige estar aquí entre finales de octubre y diciembre por los murciélagos: hay tensión entre ambas ventanas."),
        ("Perro", "Prohibido en todos los parques nacionales, permitido en las cascadas del norte (monumentos nacionales) — lo que convierte al circuito norte en la mejor parte del país para nosotros."),
        ("Comunicaciones", "Starlink activo desde 2023, el mejor del bucle; SIM local (MTN, Airtel) como respaldo."),
    ],
    alerts=[
        "Conflicto de calendario serio: la travesía del oeste (Liuwa, Barotseland, Busanga) exige temporada seca (mayo-septiembre), pero la migración de murciélagos de Kasanka solo ocurre entre finales de octubre y diciembre. No se puede tener todo: hay que decidir qué se prioriza o aceptar cruzar el oeste al final de la seca y llegar al norte ya en noviembre.",
        "Frontera de Chavuma/Caripande: paso muy remoto en ambos lados. Confirmar que emite visado en frontera y su horario real antes de comprometerse; si hubiera duda, el plan B obliga a replantear la salida de Angola.",
        "Perro prohibido en todos los parques nacionales (Liuwa, Kafue, South Luangwa, Kasanka, Bangweulu, Mosi-oa-Tunya): solo Livingstone, Mfuwe y Lusaka tienen opciones reales de guardería o alojamiento que lo cuide.",
        "Tramo Serenje/Mpika → Bangweulu → Kasanka: sin combustible en toda la zona y pistas que cambian de estado cada año. Salir con depósito lleno y provisiones, y llamar a la sede de Nkondo antes de entrar a Bangweulu.",
        "Desvío a Victoria Falls: son unos 950 km ida y vuelta desde Lusaka para ver el lado zambiano, cuando la ruta global pasa meses más tarde por Zimbabue, desde donde se ve la panorámica. Lo único exclusivo de este lado es Devil's Pool (solo en aguas bajas, aprox. agosto-enero). Decisión pendiente.",
    ],
    ruta_intro=("Travesía diagonal del país, del extremo noroeste al noreste, con un desvío sur opcional. "
                "Etapas sobre una media de 250 km/día."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada y Barotseland", "Chavuma/Caripande → cataratas de Chavuma → Zambezi town → Lukulu", "~350 km · 3 días de pista"),
        ("2 · Llanura de los ñus", "Lukulu → Parque Nacional de Liuwa Plain", "~200 km · 3 días en el parque"),
        ("3 · El reino lozi", "Liuwa → Mongu y la llanura del Barotse (Lealui, Kuomboka)", "~200 km · 2 días"),
        ("4 · Alto Zambeze (opcional)", "Mongu → Senanga → cataratas de Ngonye (Sioma) y vuelta", "~500 km ida y vuelta · 2-3 días"),
        ("5 · El gran parque", "Mongu → Parque Nacional de Kafue (Itezhi-Tezhi o Busanga)", "~450 km · 3-4 días"),
        ("6 · Capital y revisión", "Kafue → Lusaka", "~300 km · 2 días de taller y logística"),
        ("Variante sur · Cataratas Victoria", "Lusaka → Kariba/Siavonga → Livingstone (Devil's Pool, rafting) → Lusaka", "~950 km ida y vuelta · 5-6 días"),
        ("7 · Subida al norte", "Lusaka → Chipota Falls → Serenje → Kundalila Falls", "~450 km · 2-3 días"),
        ("8 · Murciélagos y picozapato", "Serenje → Kasanka (murciélagos) → Bangweulu (picozapato)", "~300 km · 4-5 días"),
        ("9 · La mansión y el wilderness", "Bangweulu → Mpika → Shiwa Ng'andu y Kapishya → Mutinondo", "~350 km · 3-4 días"),
        ("10 · Valle del Luangwa (desvío)", "Mpika → South Luangwa (Mfuwe) y vuelta", "~700 km ida y vuelta · 4-5 días"),
        ("11 · Circuito de cascadas", "Mansa → Mumbuluma → Ntumbachushi → Lumangwe → Kabwelume → Kawambwa", "~500 km · 4-5 días"),
        ("12 · Kasama y el lago", "Kawambwa → Chishimba → Kasama (arte rupestre de Mwela) → Mpulungu", "~400 km · 3-4 días"),
        ("13 · Kalambo y salida", "Mpulungu → cataratas de Kalambo → Mbala → Nakonde (frontera)", "~450 km · 3 días"),
    ],
    offroad=[
        "Travesía del oeste (Barotseland): pistas de arena profunda y la llanura inundable del Zambeze, con ferrys de pontón en varios ríos. Es el tramo 4x4 más exigente del país y solo es practicable en temporada seca — en lluvias la llanura se convierte en un mar.",
        "Acceso a Liuwa Plain: 4x4 obligatorio, arena y vados; African Parks cierra partes del parque en la estación húmeda.",
        "Llanuras de Busanga (norte de Kafue): pista de arena y vados de acceso, solo de julio a octubre; una de las conducciones más bonitas del país cuando está abierta.",
        "Pista a Bangweulu: 66 km desde el desvío de la Great North Road, 4x4 de altura, con un acceso alternativo solo en seco vía Kasanka y Lake Waka Waka. La D235 junto a los pantanos está destrozada unos 100 km.",
        "Mporokoso → Kabwelume: «tierra bastante mala» con tramos de arena donde hay que elegir bien la trazada, según los overlanders que lo han hecho.",
        "Accesos a las cascadas de Lumangwe y Kabwelume: pista de tierra con 4x4 recomendado; los 6 km entre ambas son fáciles pero lentos.",
        "Acceso final a los campamentos de South Luangwa: pistas de tierra, 4x4 necesario en temporada de lluvias (noviembre-abril).",
    ],
    senderismo=[
        "Cataratas de Kalambo: se sube a pie desde la orilla del Tanganyika (desde Isanga Lodge, a 40 minutos en barca de Mpulungu) hasta el borde del salto de 235 m. La gran caminata del norte, con el añadido de estar en uno de los yacimientos arqueológicos más importantes de África.",
        "Cataratas de Chishimba: senderos bien marcados y mantenidos que enlazan los tres saltos sucesivos (Mutumuna, rápidos de Kaela y Chishimba), todo a poca distancia del camping.",
        "Cataratas de Ntumbachushi: senderos por encima y por debajo del salto, con pozas de agua cristalina para bañarse en el recorrido.",
        "Mutinondo Wilderness: finca privada de conservación con inselbergs de granito (whalebacks) que se suben a pie, bosque de miombo, ríos de agua limpia y decenas de kilómetros de senderos señalizados. El mejor sitio de Zambia para caminar de verdad varios días, y poco conocido.",
        "Arte rupestre de Mwela (a 10 minutos de Kasama): conjunto de abrigos y cuevas con pinturas, monumento nacional, con visitas guiadas a pie entre los bolos de granito.",
        "Safari a pie en South Luangwa: no es senderismo libre sino caminata guiada con ranger armado — aquí se inventó la modalidad en los años 50 y sigue siendo la referencia mundial. Reservar desde el campamento.",
        "Musonda Falls: caminata corta por roca desde la pista, sin entrada formal, a 20 minutos de Mumbuluma.",
    ],
    acampada=[
        "Cascadas del norte: Lumangwe (unos 15 USD/persona, sencillo e impecable), Ntumbachushi (monumento nacional, con barbacoas y pozas) y Chishimba (más básico) tienen camping propio. Son las mejores pernoctas del país y además admiten perro.",
        "Chipota Falls (12 km después de Serenje): aparcamiento básico donde se puede acampar, primera parada natural al salir al norte.",
        "Mumbuluma Falls (40 min de Mansa): zona de acampada muy bien mantenida, entrada de 5-8 kwacha.",
        "Bangweulu: Nkondo Tented Camp abierto todo el año, Nsobe Campsite cuando baja el agua, y Shoebill Island Camp desde el 1 de mayo (cerrado en lluvias).",
        "Mutinondo Wilderness: camping y cabañas propias, con acceso a toda la red de senderos.",
        "Kapishya Hot Springs (junto a Shiwa Ng'andu): camping con aguas termales naturales, un clásico del circuito norte.",
        "Lago Tanganyika (Mpulungu): varios lodges con camping en la orilla, buen sitio para parar días.",
        "Livingstone (si se hace el desvío sur): amplia oferta de campings orientados a overlanders junto al Zambeze.",
        "Mfuwe (South Luangwa): campamentos y lodges con parcelas para vehículo propio.",
    ],
    visado=[
        "Visado de turista disponible a la llegada para españoles; confirmar que el puesto remoto de Chavuma lo emite antes de depender de ello.",
        "El KAZA Univisa (50 USD, Zambia+Zimbabue, 30 días) ya NO encaja con esta ruta, porque Zimbabue se visita meses más tarde en el bucle: tramitar visados individuales.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica (Angola lo es).",
    ],
    fronteras_rows=[
        ("Entrada", "Chavuma/Caripande (Angola)", "Paso remoto del noroeste; pistas de arena, solo temporada seca. Confirmar horario y emisión de visado en frontera. Las cataratas de Chavuma están junto al paso."),
        ("Salida", "Nakonde/Tunduma (Tanzania)", "Gran paso del corredor TANZAM, ventanilla única; mucho camión y colas. Llegar temprano y vigilar la documentación."),
        ("Variante sur (solo si se hace el desvío)", "Kazungula o Victoria Falls (Zimbabue/Botsuana)", "No se cruza: el puente de Victoria Falls se puede caminar con pase de visitante sin hacer trámite de entrada a Zimbabue."),
    ],
    vehiculos=[
        "Permiso temporal de importación en frontera para los dos vehículos; confirmar el despacho aduanero en un puesto tan pequeño como Chavuma.",
        "Seguro de terceros COMESA/SADC válido en Zambia, miembro de ambas regiones; contratarlo en frontera si no se lleva.",
        "Tasas zambianas de frontera: carbon tax, council levy y road toll, varias y de pago obligatorio — llevar efectivo en dólares y kwacha.",
        "Depósitos y garrafas llenos antes del oeste (entre la frontera y Mongu) y antes del norte (Serenje/Mpika → Bangweulu/Kasanka): son los dos tramos sin suministro garantizado.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No volar en ningún caso dentro de los parques nacionales (Mosi-oa-Tunya, South Luangwa, Kafue, Kasanka, Bangweulu, Liuwa) sin autorización expresa ya concedida.",
        "Registrar el dron ante la Zambia Civil Aviation Authority antes de cualquier uso fuera de parques.",
        "Las cascadas del norte, al ser monumentos y no parques, son el mejor sitio para volar — pero sigue haciendo falta el registro previo.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo desde 2023, con cobertura razonable incluso en el norte remoto y en zonas de safari.",
        "SIM local (MTN, Airtel Zambia) como respaldo; cobertura móvil irregular en el oeste y en el circuito de cascadas.",
    ],
    perro_intro=[
        "Certificado veterinario internacional y permiso de importación previo, exigibles en frontera — tramitar con antelación, no se resuelve en el puesto.",
        "Prohibido en todos los parques nacionales. Permitido en las cascadas del norte, que son monumentos nacionales: ahí está la mejor parte del país con el perro.",
        "Planificar guardería o alojamiento con cuidado del perro en Livingstone, Mfuwe y Lusaka, las únicas plazas con ese servicio real.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en todo el país y especialmente intensa en el valle del Luangwa, el Zambeze y los humedales del norte: profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica (Angola lo es).",
        "Bilharzia (esquistosomiasis) en aguas estancadas del Zambeze, Kafue y los humedales: no bañarse en remansos; el lago Tanganyika y las pozas de las cascadas del norte se consideran de bajo riesgo, pero preguntar en cada sitio.",
        "University Teaching Hospital (Lusaka) como referencia nacional y hospital de Kasama en el norte; evacuación hacia Sudáfrica para casos serios.",
    ],
    seguridad_intro="Zambia es uno de los países más estables políticamente de la región, con alternancia democrática pacífica; la atención en este tramo debe ir a la fauna, al aislamiento del oeste y el norte, y a la carretera, no a la seguridad ciudadana.",
    seguridad=[
        "Sin zonas excluidas por seguridad en ninguno de los corredores previstos.",
        "Aislamiento real en el oeste (Barotseland, Liuwa) y en el norte (Bangweulu, circuito de cascadas): llevar siempre combustible, agua y comida de reserva, y avisar del itinerario.",
        "Respetar las distancias con la fauna y las indicaciones del ranger en los safaris a pie de South Luangwa; hipopótamos y elefantes en los campamentos del valle.",
        "Cocodrilos en el Zambeze, el Kafue y partes del Tanganyika: preguntar siempre en el alojamiento antes de acercarse al agua, también con el perro.",
        "Tráfico pesado de camiones en el corredor de la Great North Road y en Nakonde: extremar precaución, evitar conducir de noche.",
        "Bordes de cascada sin vallas (Kalambo, Lumangwe, Ntumbachushi): el principal riesgo real de accidente del tramo.",
    ],
    agua=[
        "Lusaka, Livingstone, Mongu y Kasama: agua embotellada sin problema.",
        "Recarga de depósito de uso general: lodges y campings de las cascadas del norte, Mpulungu, Mfuwe y las ciudades permiten llenar con manguera; confirmar en recepción.",
        "Oeste (Barotseland) y tramo de Bangweulu: sin garantía — salir con los depósitos al 100%.",
        "Filtrar y tratar siempre el agua de pozas y ríos, por muy cristalina que parezca (bilharzia).",
    ],
    combustible=[
        "Plazas fiables: Mongu (oeste), Lusaka, Serenje, Mpika, Kasama, Mbala y Livingstone si se hace el desvío sur.",
        "Dos tramos sin garantía: frontera de Chavuma → Mongu (~350 km de pista) y Serenje/Mpika → Bangweulu/Kasanka → circuito de cascadas. Llevar garrafas llenas en ambos.",
        "El circuito de cascadas (Mporokoso, Kawambwa) tiene oferta irregular: repostar en Kasama o Mansa antes de entrar.",
    ],
    experiencias_intro="Relatos y datos reales de otros overlanders sobre Zambia, sobre todo del circuito norte, que es la parte menos documentada y la más interesante para nosotros:",
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Conflicto de temporadas", "Decidir entre cruzar el oeste en seco (mayo-septiembre) o llegar al norte para los murciélagos de Kasanka (finales de octubre-diciembre); son incompatibles sin forzar el calendario"),
        ("Frontera de Chavuma", "Confirmar horario real y si emite visado en frontera; de ello depende la salida de Angola por Caripande"),
        ("Desvío a Victoria Falls", "Decidir si compensa hacer 950 km ida y vuelta por el lado zambiano y Devil's Pool, sabiendo que se verá la panorámica desde Zimbabue meses después"),
        ("Desvío a South Luangwa", "Decidir si entran los ~700 km ida y vuelta desde Mpika, y reservar el safari a pie con antelación"),
        ("Perro", "Confirmar guardería o cuidador en Livingstone, Mfuwe y Lusaka para los días de parque; tramitar el permiso de importación del perro con antelación"),
        ("Bangweulu", "Llamar a la sede de Nkondo antes de entrar para confirmar el estado de las pistas y qué campamentos están abiertos"),
        ("Kuomboka", "La fecha depende de la crecida del Zambeze (suele marzo-abril): comprobar si cuadra con nuestro paso por Mongu, sería un añadido excepcional"),
        ("Fotos pendientes de sustituir", "Liuwa, Kasanka, Bangweulu y Ntumbachushi usan imágenes de la especie o de la región, no del propio sitio"),
        ("Dron", "Registrar ante la Zambia Civil Aviation Authority si se quiere volar en las cascadas del norte"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 11 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Sin representación española propia en Zambia — gestionar emergencias a través de la Embajada de España en Harare (Zimbabue), competente para el país: +263 (0)242 250740/1; emergencias +263 (0)772 436 620.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

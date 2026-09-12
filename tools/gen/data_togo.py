# -*- coding: utf-8 -*-
"""Togo — ficha completa, corredor doble bajada (costa) / subida (interior) — 12 sep 2026."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== BAJADA: Aflao/Kodjoviakopé (Ghana) -> Lomé -> lago Togo -> Aného -> Hillacondji (Benín) =====
    dict(n=1, name="Lomé · Grand Marché y Catedral del Sagrado Corazón", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=6.1319, lon=1.2228,
         desc="Capital y única gran base logística del país: puerto, aeropuerto internacional, talleres, supermercados y bancos. El Grand Marché —dominado históricamente por las «Nana Benz», las comerciantes textiles que llegaron a manejar el mercado del wax en toda África occidental— ocupa varias manzanas junto a la Catedral del Sagrado Corazón, iglesia alemana de 1902. Última plaza con oferta completa antes de Ghana o de Benín según el sentido de la marcha, y nudo compartido por los dos corredores.",
         credit="Dan Sloan · CC BY-SA 2.0", source=W + "Lomé%20Grand%20Marché%20with%20the%20Cathédrale%20du%20Sacré%20Coeur%20(33592985581).jpg?width=900"),
    dict(n=2, name="Mercado de fetiches de Akodessewa (Marché des féticheurs)", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=6.1450, lon=1.2830,
         desc="El MAYOR MERCADO VUDÚ DEL MUNDO, en el barrio de Akodessewa, al este del centro de Lomé: un patio abierto donde se venden cráneos y cabezas de mono, pieles de leopardo, cocodrilos disecados, aves, plantas y talismanes destinados a los rituales vodun de toda la subregión. Los feticheurs cobran una tasa de entrada y otra —normalmente mayor— por fotografiar; la consulta con un curandero es parte de la visita. No es un espectáculo para turistas: es un mercado religioso en funcionamiento, y conviene entrar con guía y con respeto. Coordenada urbana aproximada del barrio: confirmar sobre el terreno.",
         credit="Wikimedia Commons", source=W + "Akodessawa%20Fetish%20Market%202016.jpg?width=900"),
    dict(n=3, name="Lomé alemán · Palais de Lomé y arquitectura colonial", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=6.1300, lon=1.2150,
         desc="Togo fue la «colonia modelo» del imperio alemán (1884-1914) y Lomé conserva de aquella etapa el antiguo Palacio de los Gobernadores —hoy Palais de Lomé, reabierto como centro cultural con jardín de 11 ha sobre el paseo marítimo—, la catedral de 1902, la antigua estación de ferrocarril y varias casas comerciales de la Rue du Commerce. El conjunto, muy deteriorado en parte, es el mejor testimonio urbano del Togoland alemán junto con Togoville y Aného. Coordenada urbana aproximada.",
         credit="Wikimedia Commons", source=W + "Lomé%20(Togo)%20banner%20Voodoo%20fetish%20market.jpg?width=900"),
    dict(n=4, name="Playas del este de Lomé (Baguida y Coco Beach)", cat="Costa", prio="Media", dog="permitido", time="1–2 noches",
         lat=6.1750, lon=1.3300,
         desc="La franja de cocoteros entre Lomé y Agbodrafo, con alojamientos y campings sencillos junto a la arena (Coco Beach, Baguida, Avépozo) donde el perro no suele ser problema y se puede aparcar el vehículo a la vista. ATENCIÓN: la costa togolesa tiene resaca fuerte y corrientes de retorno peligrosas en casi todo el litoral — bañarse solo donde haya gente local haciéndolo. Es la parada natural para descomprimir entre la frontera de Ghana y la de Benín.",
         credit="Wikimedia Commons", source=W + "Pont%20Adido%20sur%20le%20Lac%20Togo%20a%20l'embouchure%20(Aneho%2C%20TOGO%202018).jpg?width=900"),
    dict(n=5, name="Agbodrafo y el lago Togo (Maison des Esclaves de Wood Home)", cat="Costa", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=6.2167, lon=1.4333,
         desc="Antigua Porto Seguro portuguesa, hoy embarcadero principal del lago Togo: laguna de agua dulce separada del Atlántico por un cordón de arena, sin corrientes, buena para deportes de vela. Conserva la Maison des Esclaves (Wood Home), casa de un tratante afro-brasileño con el sótano donde se retenía a los cautivos antes del embarque. De aquí salen las piraguas a Togoville (20-30 min de travesía).",
         credit="Wikimedia Commons", source=W + "Embouchure%20Adido%20(Aneho%2C%20TOGO%202018).jpg?width=900"),
    dict(n=6, name="Togoville", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=6.2333, lon=1.4500,
         desc="Al otro lado del lago: el pueblo donde el rey Mlapa III firmó en 1884 el tratado de protectorado con Gustav Nachtigal que dio nombre al país. Es uno de los grandes centros del vudú togolés y a la vez sede de una catedral alemana de 1910, Notre-Dame du Lac Togo, cuyas vidrieras y estaciones representan a santos africanos negros —un sincretismo deliberado para atraer a los fieles del vodun—. Se llega en piragua desde Agbodrafo; hay santuarios vudú por todo el pueblo y guías locales que los explican. El perro se queda en el vehículo en Agbodrafo si la piragua va cargada.",
         credit="Rayman3640 · CC BY-SA 3.0", source=W + "Cathédrale%20Notre-Dame%20du%20Lac%20Togo.jpg?width=900"),
    dict(n=7, name="Aného y Glidji", cat="Cultura", prio="Media", dog="permitido", time="½ día · 1 noche",
         lat=6.2333, lon=1.6000,
         desc="Primera capital del Togo colonial (la Klein Popo alemana), con arquitectura afro-brasileña y afro-portuguesa levantada por los agudás —descendientes de esclavos retornados de Brasil— y varias casas comerciales alemanas en ruina progresiva. En la vecina Glidji se celebra cada septiembre el Epe Ekpe, la fiesta de la Piedra Sagrada de los guin: el sacerdote saca de la selva sagrada una piedra cuyo color anuncia el año que viene, y con ella empieza el año nuevo guin. La bocana del lago Togo (embouchure Adido) y la playa quedan a un paso, ya casi en la frontera de Benín.",
         credit="Francois Jake Green (Fanfan) · CC BY 3.0", source=W + "Aného%20Beach%2C%20DSC01117%20-%20by%20Fanfan.JPG?width=900"),
    # ===== SUBIDA: Ouaké (Benín) -> Kara -> Koutammakou -> Aledjo -> Sokodé -> Bassar/Fazao -> Atakpamé -> Badou -> Kpalimé -> Wli (Ghana) =====
    dict(n=8, name="Kara", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=9.5511, lon=1.1861,
         desc="Segunda capital administrativa del país, a 412 km de Lomé, y única base logística real del norte: combustible, talleres, hospital regional (CHU Kara), hoteles con aparcamiento y mercado. Ciudad natal del clan Gnassingbé y sede de la lucha ritual EVALA, la iniciación de los jóvenes kabyè que se celebra cada julio y llena la región durante una semana. Punto de partida obligado para Koutammakou, Sarakawa y la falla de Aledjo. IMPORTANTE: es también el último punto del país al que se puede subir con normalidad — ver la sección de seguridad antes de continuar hacia el norte.",
         credit="Wikimedia Commons", source=W + "Kara%2C%20Togo%20-%20panoramio.jpg?width=900"),
    dict(n=9, name="Reserva de fauna de Sarakawa", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido", time="½ día",
         lat=9.6300, lon=1.1700,
         desc="1.500 ha valladas a unos 15 km al norte de Kara, con búfalos, bubales, cobos de Buffon, hipotragos y especies introducidas (cebras, avestruces). Según la web oficial de turismo togolesa es HOY EL PARQUE MÁS VISITADO DEL PAÍS y, al ser una reserva cercada y sin grandes depredadores en libertad, es la opción de fauna más realista del corredor — y la única candidata seria a ser compatible con el perro dentro del vehículo, cosa que hay que confirmar por escrito. Junto a la reserva está el mausoleo de Sarakawa, del accidente aéreo de Eyadéma en 1974, convertido en lugar de memoria del régimen. Coordenada aproximada.",
         credit="Wikimedia Commons", source=W + "Mausolée%20de%20sarakawa%208.jpg?width=900"),
    dict(n=10, name="Koutammakou · el país de los batammariba (UNESCO) — CONDICIONADO A SEGURIDAD", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="1–2 días",
         lat=10.0670, lon=1.1330,
         desc="2.718 km² de paisaje cultural vivo en la prefectura de Kéran, al noroeste de Kandé, Patrimonio Mundial desde 2004 y ampliado al lado beninés en 2023. Los batammariba («los que modelan bien la tierra») construyen las TAKIENTA o tata somba: torres-vivienda de barro de dos plantas, con establo abajo, terraza-granero arriba y torretas cónicas de paja, que son el símbolo nacional de Togo y probablemente la arquitectura vernácula más singular de toda África occidental. La aldea de Nadoba, con su mercado de cada cinco días, es la puerta habitual; se visita con guía de la comunidad y hay que pagar tasa de visita y de fotografía. ⚠️ AVISO CRÍTICO: el sitio está al norte de Kandé, dentro de la franja que los avisos de viaje marcan como zona de no viajar por el riesgo yihadista transfronterizo. NO dar por hecha la visita: reconfirmar 30-60 días antes. Ver la sección de seguridad.",
         credit="Wikimedia Commons", source=W + "Togo%20Taberma%20house%2002.jpg?width=900"),
    dict(n=11, name="Falla de Aledjo y los tejedores de Bafilo", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=9.2333, lon=1.1667,
         desc="La FAILLE D'ALEDJO es el tajo abierto en la cadena de Aledjo para dejar pasar la carretera nacional N1: un corte vertical en la roca de decenas de metros por el que el asfalto se cuela entre dos paredes, con mirador arriba y vistas sobre toda la llanura de la Kara. Es el paso de montaña emblemático del país y la parada fotográfica obligada del corredor interior. A 20 km, Bafilo conserva talleres de tejedores de algodón a mano y tiene su propia cascada (Cascade de Bafilo), corta caminata desde el pueblo.",
         credit="Wikimedia Commons", source=W + "Faille%20d'Aledjo.jpg?width=900"),
    dict(n=12, name="Sokodé", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=8.9833, lon=1.1333,
         desc="Segunda ciudad del país por población y capital de la región Central, en pleno eje N1: combustible, mercado, hospital regional y hoteles con aparcamiento. Ciudad tem (kotokoli), mayoritariamente musulmana, célebre por la DANZA DEL FUEGO (Gadao-Adossa), en la que los danzantes manipulan brasas ardiendo durante las fiestas del calendario islámico local. Es la parada de servicios intermedia entre Kara y Atakpamé y la base natural para el desvío a Bassar y Fazao-Malfakassa.",
         credit="Wikimedia Commons", source=W + "Kara%2C%20Togo%20-%20panoramio%20-%20Milos58%20(1).jpg?width=900"),
    dict(n=13, name="Bassar · sitios de la metalurgia antigua del hierro", cat="Cultura", prio="Media", dog="permitido", time="1 día",
         lat=9.2830, lon=0.8000,
         desc="En la lista indicativa de la UNESCO desde diciembre de 2021: un conjunto repartido por quince aldeas (Tabalé, Bandjéli, Nangbani…) con un centenar de hornos de reducción todavía en pie, escoriales de hasta 4 m de altura, minas y forjas que documentan una cadena completa de producción de hierro desde el siglo V a.C. hasta mediados del siglo XX, sin maquinaria. La tradición sigue viva: los maestros metalúrgicos y herreros bassar mantienen rituales asociados, incluida la ceremonia del paso sobre el fuego (T'bol). Se visita con guía desde Bassar; las aldeas de los hornos están a 20-40 km por pista.",
         credit="Wikimedia Commons", source=W + "Faille%20d'Aledjo.jpg?width=900"),
    dict(n=14, name="Parque Nacional de Fazao-Malfakassa", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=8.9500, lon=0.7500,
         desc="Con unos 1.920-2.000 km² es el mayor espacio protegido de Togo, a caballo entre las regiones Central y de Kara, sobre la cadena de Fazao-Malfakassa: bosque de galería, sabana arbolada y escarpes con más de 200 especies de aves. La fauna grande (elefante, búfalo, leopardo) quedó muy mermada por la caza furtiva y la gestión ha pasado por varias manos desde que la fundación suiza Franz Weber se retiró; la realidad del avistamiento hoy es modesta y el atractivo principal es el paisaje y el senderismo de montaña. Accesos por pista desde Fazao (eje Sokodé-Bassar). Coordenada aproximada: NO hay una puerta oficial publicada — confirmar acceso, tasas y estado de la gestión antes de desviarse.",
         credit="Wikimedia Commons", source=W + "Paysage%20du%20pic%20d'Agou%20au%20Togo%2017.jpg?width=900"),
    dict(n=15, name="Cascada de Akloa (Badou)", cat="Naturaleza", prio="Media", dog="permitido", time="½–1 día",
         lat=7.5833, lon=0.6000,
         desc="Salto de unos 35-60 m escondido en la selva del macizo del Litimé, la zona cacaotera y cafetera del suroeste, a unos 8 km de Badou. Se llega por un sendero de unos 45 minutos de subida entre plantaciones, con guía del pueblo (tasa comunitaria), y se puede bañar en la poza. Es la cascada más impresionante del país junto con Womé y encaja perfectamente en el descenso de Atakpamé hacia Kpalimé por la carretera del Litimé, una de las más bonitas de Togo.",
         credit="Wikimedia Commons", source=W + "Cascade%20de%20Womé%20au%20togo%2033.jpg?width=900"),
    dict(n=16, name="Kpalimé", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=6.9000, lon=0.6333,
         desc="A 120 km al noroeste de Lomé, en plena montaña cafetera y cacaotera: la ciudad más agradable del país para pasar varios días, con clima fresco por altitud, catedral gótica alemana de 1913, un centro artesanal de referencia (escultura, cerámica, batik, tejido) y una red densa de guías locales de senderismo. Es la base de todo el bloque final del corredor interior: Womé, Kpimé, Klouto, Château Viale y el monte Agou. Servicios suficientes (combustible, mercado, hospital, hoteles con parking) aunque muy por debajo de Lomé.",
         credit="Wikimedia Commons", source=W + "Cascade%20de%20Womé.jpg?width=900"),
    dict(n=17, name="Cascadas de Womé y Kpimé", cat="Naturaleza", prio="Alta", dog="permitido", time="1 día",
         lat=6.9667, lon=0.6333,
         desc="Las dos cascadas clásicas de Kpalimé. WOMÉ, a 12 km al norte, es la más bonita y de acceso más natural: caminata corta desde la aldea, poza de baño, tasa comunitaria y guía local. KPIMÉ, de unos 35-50 m, cae por una pared escalonada y está encima de la pequeña central hidroeléctrica del mismo nombre, así que su caudal depende de lo que suelte la presa: en plena estación seca puede verse casi sin agua, y varios viajeros lo describen como una decepción si se va en mal momento — preguntar en Kpalimé antes de subir. Escalones de acceso al mirador y sendero hasta el pie del salto.",
         credit="Ak9visuelmind · CC BY-SA 4.0", source=W + "Cascade%20de%20Kpimé%201.jpg?width=900"),
    dict(n=18, name="Monte Klouto, Château Viale y el valle de los murciélagos", cat="Naturaleza", prio="Alta", dog="permitido con correa", time="1 día",
         lat=6.9500, lon=0.5700,
         desc="A 12 km de Kpalimé y 710 m de altitud, la meseta de Klouto conserva el bosque más denso de Togo, con más de 1.000 especies de mariposas catalogadas (los guías de Kpalimé organizan salidas específicas de mariposas y de aves) y senderos entre aldeas donde se compran batiks. En la cima está el CHÂTEAU VIALE, capricho neomedieval construido por un colono francés y usado después como residencia presidencial, hoy semiabandonado pero con la mejor vista del valle hasta Ghana. Cerca, el valle de los murciélagos (Vallée des chauves-souris) alberga colonias de decenas de miles de frugívoros que levantan el vuelo al atardecer. Correa obligatoria: el perro y los murciélagos no se llevan bien.",
         credit="Wikimedia Commons", source=W + "Feuille%20d'herbe%20dans%20la%20forêt%20classée%20d'%20Agou%20au%20Togo%2031.jpg?width=900"),
    dict(n=19, name="Monte Agou (Pic Baumann, 986 m) · techo de Togo", cat="Naturaleza", prio="Alta", dog="permitido con correa", time="1 día",
         lat=6.8750, lon=0.6800,
         desc="EL PUNTO MÁS ALTO DEL PAÍS (986 m según la cartografía oficial togolesa; algunas fuentes de altimetría dan 993 m) y LA gran excursión a pie de Togo. Una carretera estrecha y muy revirada sube casi hasta la cumbre —donde hay antenas de telecomunicaciones y un puesto militar, así que la cima estricta puede estar restringida—, pero lo bueno es subir a pie desde Nyogbo o Agou-Nyogbo por los caminos entre aldeas de cultivadores de café: 3-4 horas de subida, aldeas escalonadas en la ladera y vista sobre el lago Volta en Ghana los días claros. Guía local barato y muy recomendable: los senderos se ramifican y no hay señalización.",
         credit="Wikimedia Commons", source=W + "Pic%20d'Agou.jpg?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "cultura": "morado", "naturaleza": "verde",
              "costa": "turquesa", "patrimonio unesco": "marron", "patrimonio": "marron"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada bajada — Aflao/Kodjoviakopé (desde Ghana)", "Frontera", 6.1167, 1.2000,
     "Paso urbano integrado en la conurbación Aflao-Lomé, el más transitado de todo el golfo de Guinea occidental; menos de 1 km entre ambos puestos y a 5 km del centro de Lomé. Horario aproximado 06:00-18:00 (confirmar: el horario efectivo varía). Reputación consolidada de estafadores de cambio de moneda y de «ayudantes» no oficiales — usar solo casas de cambio autorizadas y no soltar nunca el pasaporte."),
    ("Frontera · Salida bajada — Hillacondji/Sanvee-Condji (hacia Benín)", "Frontera", 6.1667, 1.6333,
     "Puesto conjunto (yuxtapuesto) Togo-Benín a unos 21 km de Lomé, con los dos países tramitando en la misma instalación. Cruzar por la mañana: el tráfico comercial satura el mediodía."),
    ("Frontera · Entrada subida — Ouaké (desde Benín, eje Djougou-Kara)", "Frontera", 9.6719, 1.3637,
     "Paso del eje Djougou-Kara, a 37 km de Djougou; según la evaluación logística del Logistics Cluster opera 24/7 salvo festivos nacionales de Benín, y exige seguro CEDEAO y laissez-passer del vehículo. Es la puerta natural del corredor interior de subida. POR CONFIRMAR el nombre exacto del puesto togolés al otro lado y su horario real en 2027."),
    ("Frontera · Alternativa subida — Tohoun/Azovè (desde Benín, eje central)", "Frontera", 7.0000, 1.6000,
     "Paso interior mucho más al sur, sobre el eje Notsé-Azovè, fuera por completo de cualquier zona de riesgo; alternativa si la situación del norte desaconseja entrar por Ouaké. Coordenada aproximada, por verificar."),
    ("Frontera · Salida subida — Wli/Kpalimé (hacia Ghana, región del Volta)", "Frontera", 7.1200, 0.5900,
     "Paso menor de montaña junto a las cataratas de Wli (Ghana), la ruta más corta entre Kpalimé y el Volta ghanés. Relato de viajeros con vehículo: el lado ghanés es lento y desorganizado (revisar personalmente que sellos y fechas del carnet estén bien puestos), el lado togolés más profesional, con la aduana del carnet unos kilómetros dentro, cerca de Tomegbé. Coordenada aproximada."),
    ("Frontera · Cinkassé (hacia Burkina Faso) — EXCLUIDA", "Frontera", 10.9833, 0.2333,
     "Puesto fronterizo integrado del corredor Lomé-Uagadugú, en el extremo norte del país. FUERA DEL ITINERARIO: está en plena región de las Savanes, bajo estado de emergencia, y el cruce a Burkina Faso está desaconsejado para extranjeros."),
    ("Embajada de España en Accra (acreditada también en Togo)", "Consular", 5.6050, -0.1700,
     "Drake Av. Extension, Airport Residential Area, P.M.B. KA 44, Accra (Ghana). +233 302 77 40 04/05. Togo no tiene embajada española propia; gestionar cualquier trámite con margen desde Accra o desde el consulado honorario en Lomé, cuyo canal exacto hay que confirmar antes del viaje."),
    ("CHU Sylvanus Olympio — Lomé", "Hospital", 6.1256, 1.2283,
     "Principal hospital universitario y de referencia del país, en el corredor de bajada. Coordenada urbana aproximada."),
    ("CHU Kara — Kara", "Hospital", 9.5511, 1.1861,
     "Referencia hospitalaria del norte y del corredor interior de subida; entre Kara y Lomé no hay nada equivalente. Coordenada urbana aproximada."),
    ("Combustible · Lomé", "Combustible", 6.1319, 1.2228,
     "Mejor oferta y calidad del país (Togo Oil, Total, CM Oil, Sanol); repostar aquí antes o después de cualquiera de las dos fronteras costeras."),
    ("Combustible · Aného / Hillacondji", "Combustible", 6.2333, 1.6000,
     "Estaciones formales en Aného, última plaza con oferta amplia antes de cruzar a Benín en la bajada."),
    ("Combustible · Kara", "Combustible", 9.5511, 1.1861,
     "Plaza de servicios del norte: combustible formal, talleres y recambios básicos. Llenar aquí antes de cualquier desvío a Koutammakou o Sarakawa."),
    ("Combustible · Sokodé", "Combustible", 8.9833, 1.1333,
     "Parada intermedia obligada del eje N1 entre Kara y Atakpamé (~160 km hasta Atakpamé); estaciones formales y mercado."),
    ("Atakpamé · servicios del centro-sur", "Combustible", 7.5333, 1.1333,
     "Capital de la región de los Plateaux sobre la N1, con combustible, hospital regional y hoteles; punto donde el corredor de subida abandona la nacional para bajar por el Litimé hacia Badou y Kpalimé."),
    ("Combustible · Kpalimé", "Combustible", 6.9000, 0.6333,
     "Última plaza con oferta razonable antes de la frontera de Wli y de las pistas de montaña de Klouto y Agou; la oferta en las aldeas de la sierra es nula."),
    ("Agua potable y de uso general · Lomé", "Agua potable", 6.1319, 1.2228,
     "Agua embotellada sin problema en supermercados; estaciones de servicio y hoteles de Lomé permiten llenar el depósito de uso general con manguera."),
    ("Agua potable y de uso general · Kara y Kpalimé", "Agua potable", 9.5511, 1.1861,
     "Hoteles con aparcamiento en Kara y Kpalimé permiten normalmente la recarga del depósito de uso general; confirmar en recepción. Agua de boca siempre embotellada o tratada."),
]

DRONE_CALLOUT = ("warn", "Sin marco civil claro publicado: tratar como prohibido salvo autorización expresa",
                  "Togo no publica un procedimiento civil claro y estable para drones de uso turístico; la Agence Nationale de l'Aviation Civile (ANAC-Togo) es la autoridad de referencia. A esto se suma que desde 2021 hay una operación militar activa en el norte y estado de emergencia en las Savanes: un dron en la mitad norte del país es un problema de seguridad, no una cuestión administrativa. Norma prudente del proyecto: no volar sin autorización previa por escrito y NO llevar el dron desembalado al norte de Sokodé.")

STARLINK_CALLOUT = ("warn", "Togo NO figura entre los mercados africanos con Starlink activo a mediados de 2026",
                     "En los recuentos de disponibilidad de Starlink en África revisados en septiembre de 2026, Togo no aparece en la lista de países con servicio activo (a diferencia del vecino Benín, que sí figura como operativo). Tratarlo como no disponible y mantener SIM local (Togocom, Moov Africa) como conectividad principal; el terminal se puede seguir llevando apagado, pero contar con que no habrá servicio dentro del país.")

DOG_MATRIX = [
    ("Lomé, playas de Baguida/Coco Beach, Agbodrafo, Aného", "permitido con condiciones",
     "Sin restricciones específicas conocidas. Calor y humedad altos todo el año en la costa: sombra y agua de sobra. Ojo con la resaca del Atlántico — no dejar al perro suelto en la orilla."),
    ("Togoville (travesía en piragua)", "permitido con condiciones",
     "La piragua es pequeña e inestable y suele ir cargada. Plan B: turnos entre los viajeros, dejando el perro en el vehículo a la sombra en el embarcadero de Agbodrafo, o negociar una piragua para el grupo."),
    ("Mercado de fetiches de Akodessewa", "permitido con condiciones",
     "Es un mercado de productos animales, con perros locales sueltos y muchísimo olor: en la práctica es mala idea entrar con él. Plan B: dejarlo en el vehículo con uno de los viajeros; la visita dura menos de una hora."),
    ("Kpalimé, Womé, Kpimé, Klouto, Château Viale, monte Agou", "permitido",
     "Senderos comunitarios abiertos, sin gestión de parque nacional; el clima de montaña es lo más agradable del viaje para el perro. Correa corta en el valle de los murciélagos de Klouto y en los miradores de Agou y de la falla de Aledjo."),
    ("Koutammakou (Nadoba)", "permitido con condiciones",
     "Paisaje cultural habitado, no parque de fauna: no hay prohibición conocida. Pero las takienta son viviendas con ganado dentro y perros de la casa: entrar con perro extranjero puede generar peleas. Preguntar al guía de la comunidad y, si hay duda, dejarlo en el vehículo. (La visita en sí está condicionada a la situación de seguridad.)"),
    ("Reserva de fauna de Sarakawa", "no confirmado — tratar como prohibido",
     "Reserva cercada con fauna de sabana. No se ha localizado normativa publicada sobre mascotas. Al no haber grandes depredadores en libertad es el mejor candidato del país a admitir el perro dentro del vehículo, pero hay que confirmarlo por escrito con la dirección del sitio o el ministerio de turismo. Plan B: turnos, el perro se queda en Kara."),
    ("Parque Nacional de Fazao-Malfakassa", "no confirmado — tratar como prohibido",
     "Parque nacional con leopardo y hiena sobre el papel. Tratar como prohibido hasta confirmación escrita del gestor. Plan B: sustituir por el senderismo de Klouto/Agou o por Sarakawa, que dan mejor relación esfuerzo/resultado."),
]

SOURCES = [
    ("Togo Tourisme · web oficial de turismo (destinos)", "https://www.togotourisme.tg/"),
    ("Togo Tourisme · Kpalimé (cascadas, Pic d'Agou 986 m, Château Viale)", "https://togotourisme.tg/destinations/kpalime/"),
    ("Togo Tourisme · Kara (Sarakawa, Tcharè, Evala, alojamientos)", "https://togotourisme.tg/destinations/kara/"),
    ("Togo Tourisme · Togoville", "https://togotourisme.tg/destinations/togoville/"),
    ("UNESCO · Koutammakou, el país de los batammariba", "https://whc.unesco.org/en/list/1140/"),
    ("UNESCO · Sitios de la metalurgia antigua del hierro de Bassar (lista indicativa, 2021)", "https://whc.unesco.org/en/tentativelists/6603"),
    ("UNESCO · Togo, Estado Parte (lista indicativa completa)", "https://whc.unesco.org/en/statesparties/tg"),
    ("Wikipedia · Koutammakou (coordenadas y superficie)", "https://en.wikipedia.org/wiki/Koutammakou"),
    ("Wikipedia · Akodessawa Fetish Market", "https://en.wikipedia.org/wiki/Akodessawa_Fetish_Market"),
    ("Wikipedia · Mount Agou", "https://en.wikipedia.org/wiki/Mount_Agou"),
    ("Wikipedia · Nok and Mamproug Cave Dwellings (Savanes — fuera del itinerario)", "https://en.wikipedia.org/wiki/Nok_and_Mamproug_Cave_Dwellings"),
    ("Wikipedia · Visa policy of Togo (e-Visa, fin del visado a la llegada)", "https://en.wikipedia.org/wiki/Visa_policy_of_Togo"),
    ("GANP · Fazao-Malfakassa National Park", "https://national-parks.org/togo/fazao-malfakassa-national-park/"),
    ("US Dept. of State · Togo Travel Advisory (nivel 2, marzo 2026; nivel 4 al norte de Kandé)", "https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories/togo-travel-advisory.html"),
    ("Togo First · prórroga del estado de emergencia en la región de las Savanes", "https://www.togofirst.com/en/public-management/0703-15891-togo-extends-security-emergency-in-savanes-region-until-2026"),
    ("Saiga Tours · guía de las fronteras terrestres de Togo", "https://www.saigatours.com/article/a-guide-to-togos-land-borders"),
    ("Saiga Tours · cómo visitar el mercado vudú de Akodessewa", "https://www.saigatours.com/article/How-to-visit-the-akodessewa-voodoo-market-in-lome"),
    ("Logistics Cluster (LCA) · paso fronterizo Ouaké (Djougou) Benín–Togo", "https://lca.logcluster.org/benin-234-togo-ouake-djougou-border-crossing"),
    ("MotoMorgana · cruce de frontera Ghana–Togo por Wli (relato con vehículo y carnet)", "https://www.motomorgana.com/border-ghana-togo-wli/"),
    ("Expedition Conservation · paso por Togo con vehículo y el laissez-passer togolés", "https://expeditionconservation.substack.com/p/very-brief-visit-to-togo"),
    ("Chris Travel Blog · itinerario real de road trip de sur a norte por Togo", "https://www.christravelblog.com/togo-best-10-day-itinerary-for-a-road-trip-from-south-to-north/"),
    ("Erika's Travels · guía overland de Togo (Klouto, valle de los murciélagos, Koutammakou)", "https://www.erikastravels.com/attractions-togo-travel-guide-west-africa/"),
    ("tech.africa · disponibilidad de Starlink en África (2026): Togo no figura como activo", "https://tech.africa/starlink-africa/"),
    ("Carnet de Passage.org · Togo (sin organización emisora de CPD)", "https://carnetdepassage.org/country/togo/"),
    ("ECOWAS Brown Card · esquema regional de seguro (CEDEAO) · ficha de Togo", "https://www.browncard.org/Togo.html"),
    ("Embajada de España en Ghana, acreditada en Togo", "https://www.casafrica.es/en/network/embajada-de-espana-en-ghana-togo"),
    ("iOverlander · puntos de combustible, agua y acampada verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Bajada: Aflao -> Lomé -> Akodessewa -> playas del este -> Agbodrafo/lago Togo -> Togoville -> Aného -> Hillacondji
CORRIDOR = [(6.1167, 1.2000), (6.1319, 1.2228), (6.1450, 1.2830), (6.1750, 1.3300),
            (6.2167, 1.4333), (6.2333, 1.4500), (6.2333, 1.6000), (6.1667, 1.6333)]

# Subida: Ouaké -> Kara -> Sarakawa -> Koutammakou -> Aledjo -> Sokodé -> Bassar/Fazao -> Atakpamé -> Badou -> Kpalimé -> Agou -> Wli
CORRIDOR_ALT = [(9.6719, 1.3637), (9.5511, 1.1861), (9.6300, 1.1700), (10.0670, 1.1330),
                (9.5511, 1.1861), (9.2333, 1.1667), (8.9833, 1.1333), (9.2830, 0.8000),
                (8.9500, 0.7500), (8.9833, 1.1333), (7.5333, 1.1333), (7.5833, 0.6000),
                (6.9000, 0.6333), (6.9667, 0.6333), (6.9500, 0.5700), (6.8750, 0.6800),
                (6.9000, 0.6333), (7.1200, 0.5900)]

CORRIDOR_LABEL = "Bajada · eje costero"
CORRIDOR_ALT_LABEL = "Subida · corredor interior"

EXPERIENCIAS = [
    "El laissez-passer que casi les cuesta el viaje (Expedition Conservation, cruce Benín→Togo→Ghana con vehículo propio): el trámite de inmigración les llevó más de dos horas, con un funcionario que se negaba a hablar inglés, retención del pasaporte y petición de soborno, y con el formulario rellenado por «un tipo cualquiera de paisano, no un funcionario». Su aviso literal es el más útil de todo el relato: «NUNCA creas que no necesitas documentos oficiales de entrada para el vehículo». Togo exige un LAISSEZ-PASSER (importación temporal) si no llevas Carnet de Passages — y el problema no aparece al entrar, sino al salir, cuando te piden el papel que nadie te dio.",
    "Cruce Ghana→Togo por Wli, con carnet (MotoMorgana): unos 45 minutos por lado y sin coste. Lo relevante es su advertencia sobre el LADO GHANÉS: «los tipos apenas sabían escribir y el de aduanas no tenía el sello correcto» — hay que revisar personalmente cada sello, fecha y casilla del carnet antes de irse, porque un carnet mal cerrado en Ghana se paga en la siguiente frontera. El lado togolés lo describen como notablemente más organizado, con la aduana del carnet unos kilómetros dentro del país, cerca de Tomegbé.",
    "Itinerario real de sur a norte en 10 días (Chris Travel Blog): Lomé → mercado de fetiches de Akodessewa → Sokodé (350 km, 6-7 h) → Bassar (metalurgia) → Kara, con Kara como base para las excursiones de día a Koutammakou (2,5 h por sentido) y a las cuevas de Nok (4 h por sentido); vuelta hacia Kpalimé con paradas en los tejedores de Bafilo y las cuevas de murciélagos. Describe la carretera principal como «bien asfaltada» pero avisa de RETENCIONES POR CONTROLES DE POLICÍA Y MILITARES EN EL NORTE, que hay que meter en el cálculo de tiempos. Nota del proyecto: las cuevas de Nok están en la región de las Savanes, hoy bajo estado de emergencia — ese tramo de su itinerario ya no es replicable.",
    "Kpimé, la cascada que puede no tener agua (comentarios recurrentes de viajeros en foros y reseñas): la cascada de Kpimé está aguas abajo de una pequeña central hidroeléctrica y su caudal depende de lo que suelte la presa. Varios relatos coinciden en llegar y encontrarse la pared de roca prácticamente seca. Preguntar en Kpalimé el mismo día antes de subir, y priorizar Womé si hay que elegir una sola.",
    "Klouto y el valle de los murciélagos (Erika's Travels, overland por África occidental): describe Klouto como bosque denso con arroyos y cascadas pequeñas, más de 1.000 especies de mariposas y aldeas donde se compra batik, y el santuario de murciélagos cercano a Kpalimé como un sitio que «no sale en las guías principales»: cuando el guía da palmas, los murciélagos salen de los árboles «a miles, formando una nube de tinta en el cielo de la tarde». Su valoración general de Togo es honesta y conviene tenerla presente: el país no tiene atracciones de masas y viajar por él exige renunciar a las comodidades habituales.",
    "Cambio de moneda en Aflao: los relatos de cruce Accra→Lomé coinciden en que el paso de Aflao/Kodjoviakopé concentra cambistas informales y «ayudantes» que se ofrecen a tramitar los papeles. El consejo repetido es cambiar solo lo imprescindible y en casa autorizada, y no entregar nunca el pasaporte a nadie que no esté detrás de una ventanilla.",
]

HISTORIA_RESUMEN = ("Togo es un país estrecho y alargado que pasó de colonia alemana a mandato repartido entre Francia y Gran Bretaña tras la Primera Guerra Mundial, y que desde 1967 ha estado gobernado casi ininterrumpidamente por la familia Gnassingbé —primero Gnassingbé Eyadéma, "
                     "después su hijo Faure— en uno de los regímenes más longevos y personalistas de África, pese a protestas democráticas recurrentes.")

HISTORIA_SECCIONES = [
    ("El reino de Tado y los pueblos ewe",
     "El territorio fue hogar histórico de los pueblos ewe, organizados en pequeñas jefaturas y reinos como Tado, con una fuerte tradición de vudú (vodun) que tiene aquí uno de sus centros espirituales más importantes de África Occidental, visible hoy en mercados de fetiches como el de Akodessewa, en Lomé, el mayor del mundo en su género."),
    ("El Togoland alemán y su reparto anglo-francés",
     "Alemania estableció el protectorado de Togoland en 1884, tras el tratado firmado en Togoville con el rey Mlapa III, desarrollándolo como colonia modelo con infraestructura ferroviaria y portuaria; tras la derrota alemana en la Primera Guerra Mundial, el territorio fue repartido en 1922 como mandato de la Sociedad de Naciones entre Gran Bretaña (que integró su parte en la Costa de Oro, hoy Ghana) y Francia (que administró el actual Togo), una partición que dividió a comunidades ewe entre dos países distintos."),
    ("Independencia y el ascenso de Eyadéma",
     "Togo se independizó en 1960, pero en 1963 y de nuevo en 1967 vivió golpes de Estado que llevaron al poder al militar Gnassingbé Eyadéma, quien gobernaría durante 38 años, uno de los mandatos más largos de la historia africana, con un sistema de partido dominante y represión de la oposición."),
    ("Situación actual: la dinastía Gnassingbé, protestas y la presión del Sahel",
     "Tras la muerte de Eyadéma en 2005, su hijo Faure Gnassingbé asumió el poder en circunstancias controvertidas y ha sido reelegido en sucesivas ocasiones, manteniendo a la familia Gnassingbé al frente del país durante más de cinco décadas en total; el país ha vivido oleadas periódicas de protestas prodemocráticas, la más intensa entre 2017 y 2018. Desde noviembre de 2021, además, el extremo norte del país sufre ataques de grupos armados procedentes de Burkina Faso, lo que ha llevado a decretar en junio de 2022 un estado de emergencia en la región de las Savanes, prorrogado varias veces desde entonces."),
]

HISTORIA_FUENTES = [
    ("BBC News · Togo country profile", "https://www.bbc.com/news/world-africa-14106781"),
    ("Encyclopaedia Britannica · Togo, History", "https://www.britannica.com/place/Togo/History"),
    ("International Crisis Group · Togo", "https://www.crisisgroup.org/africa/west-africa/togo"),
    ("Togo First · prórroga del estado de emergencia en las Savanes", "https://www.togofirst.com/en/public-management/0703-15891-togo-extends-security-emergency-in-savanes-region-until-2026"),
]

SPEC = dict(
    slug="togo", name="Togo", revision="12 sep 2026",
    sub="Corredor doble bajada (costa) / subida (interior) · documentación · seguridad · logística",
    chips=[
        ("BAJADA", "Aflao/Kodjoviakopé → Lomé → lago Togo → Aného → Hillacondji · ~70 km"),
        ("SUBIDA", "Ouaké → Kara → Aledjo → Sokodé → Atakpamé → Badou → Kpalimé → Wli (Ghana) · ~800 km"),
        ("PDIs", "19 puntos repartidos entre los dos corredores, sin solapamiento"),
        ("A PIE", "Monte Agou 986 m (techo del país) · Akloa · Womé · Klouto"),
        ("4x4", "Falla de Aledjo · pistas de Bassar y Fazao · sierra de Klouto-Agou"),
        ("UNESCO", "Koutammakou (batammariba) — CONDICIONADO a la seguridad del norte"),
        ("VISADO", "e-Visa obligatorio, mínimo 5 días antes — ya NO hay visado a la llegada"),
        ("SEGURIDAD", "Savanes en estado de emergencia · no viajar al norte de Kandé"),
        ("CPD", "Togo no emite CPD propio — sin carnet exigen laissez-passer al entrar"),
    ],
    center=[8.6, 1.0], zoom=7,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Togo se cruza DOS VECES por dos mitades completamente distintas del país. En la <strong>bajada</strong>, viniendo de Ghana por Aflao, se recorre el eje costero: Lomé y su mercado vudú de Akodessewa, las playas del este, el lago Togo con Agbodrafo y Togoville, "
                   "y Aného antes de salir a Benín por Hillacondji — apenas 70 km de frontera a frontera, pero con material para tres o cuatro días. En la <strong>subida</strong>, de vuelta desde Benín, se entra por el interior (Ouaké, hacia Kara) y se baja por la espina dorsal del país: "
                   "Koutammakou y sus torres-vivienda batammariba, la falla de Aledjo, Sokodé, la metalurgia antigua de Bassar, Fazao-Malfakassa, la cascada de Akloa y todo el bloque de montaña de Kpalimé (Womé, Kpimé, Klouto, Château Viale y el monte Agou, techo del país), saliendo a Ghana por el paso de Wli. "
                   "Los dos corredores no comparten ni un solo punto. <strong>El condicionante que lo ordena todo es la seguridad del norte</strong>: la región de las Savanes está bajo estado de emergencia y la franja al norte de Kandé —donde está Koutammakou— figura como zona de no viajar."),
    facts=[
        ("Ventana prevista", "Bajada: tras Ghana, antes de Benín. Subida: tras Benín, antes de Ghana."),
        ("Entrada bajada", "Aflao/Kodjoviakopé desde Ghana: el paso más transitado del golfo de Guinea occidental, a 5 km del centro de Lomé."),
        ("Salida bajada", "Hillacondji/Sanvee-Condji hacia Benín: puesto conjunto, cruzar por la mañana."),
        ("Entrada subida", "Ouaké desde Benín (eje Djougou-Kara), 24/7 según el Logistics Cluster; alternativa más segura y más al sur: Tohoun/Azovè."),
        ("Salida subida", "Wli/Kpalimé hacia la región del Volta ghanesa: paso menor de montaña, lento en el lado ghanés."),
        ("Visado", "e-Visa obligatorio para españoles, solicitado con AL MENOS 5 DÍAS de antelación; Togo ya no emite visado a la llegada. Formulario de inmigración obligatorio hasta 24 h antes de llegar. Tarifas oficiales publicadas: 25.000 FCFA (15 días, una entrada), 35.000 (15 días, multientrada), 45.000 (30 días), 65.000 (90 días). Al cruzarse dos veces, valorar la multientrada o dos e-Visas."),
        ("CPD", "Togo no tiene organización emisora de CPD (AIT/FIA). Con carnet español (RACE) basta; SIN carnet, la aduana togolesa exige un laissez-passer de importación temporal que hay que pedir expresamente al entrar."),
        ("Seguridad", "Eje costero y centro del país estables. Región de las SAVANES bajo estado de emergencia desde junio de 2022 (prorrogado varias veces) y con acceso de extranjeros sujeto a autorización especial; la franja al NORTE DE KANDÉ figura como zona de no viajar. Esto afecta directamente a Koutammakou."),
        ("Comunicaciones", "Starlink NO activo en Togo a mediados de 2026 (a diferencia de Benín); SIM local Togocom o Moov Africa como base."),
    ],
    alerts=[
        "Koutammakou (UNESCO) está en riesgo de caer del itinerario: el sitio está al norte de Kandé, dentro de la franja que los avisos de viaje marcan en nivel máximo por terrorismo y secuestro, y muy cerca de la región de las Savanes en estado de emergencia. Es el PDI más valioso del país y a la vez el más expuesto — decidir con información fresca a 30 días vista, y tener asumido que puede cancelarse.",
        "Región de las Savanes (Dapaong, Cinkassé, Mango, Kpendjal, cuevas de Nok y Mamproug, Fosse aux Lions): estado de emergencia en vigor desde junio de 2022, prorrogado sucesivamente; los extranjeros necesitan autorización gubernamental específica para viajar allí. FUERA DEL ITINERARIO en cualquier escenario.",
        "Vehículo sin CPD: la aduana togolesa exige un laissez-passer de importación temporal. El problema no aparece al entrar sino AL SALIR, cuando piden un documento que nadie se molestó en emitir. Exigir el papel en el puesto de entrada y guardarlo con el pasaporte.",
        "e-Visa: Togo ya no emite visado a la llegada. Solicitud con al menos 5 días de antelación y formulario de inmigración hasta 24 h antes de la llegada — dos trámites distintos que hay que hacer para CADA una de las dos entradas.",
        "Cambio de moneda en Aflao: reputación consolidada de estafadores y de «ayudantes» no oficiales — cambiar solo en casas autorizadas y no entregar nunca el pasaporte a un particular.",
        "Cascada de Kpimé: depende del caudal que suelte la central hidroeléctrica y puede estar seca. Preguntar en Kpalimé antes de subir; si hay que elegir una sola cascada, Womé es la apuesta segura.",
        "Fazao-Malfakassa: gestión inestable desde la retirada de la fundación Franz Weber y fauna grande muy mermada por el furtivismo. Confirmar que está operativo y cuánto cuesta antes de invertir dos días en el desvío.",
    ],
    ruta_intro=("Togo se cruza por dos mitades distintas y sin solapamiento. La <strong>bajada</strong> es un tramo costero cortísimo (unos 70 km de frontera a frontera) que aun así justifica 3-4 días por densidad de contenido. "
                "La <strong>subida</strong> es el corredor interior completo, de norte a sur, unos 750-850 km incluyendo desvíos: sobre la media de <strong>250 km/día</strong> del proyecto son unos 4 días de conducción pura, "
                "pero con las paradas, las excursiones a pie y los controles militares del norte hay que contar <strong>8-11 días</strong>."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bajada 1 · Entrada y capital", "Aflao/Kodjoviakopé → Lomé (Grand Marché, Akodessewa, Palais de Lomé)", "~10 km · 1-2 días"),
        ("Bajada 2 · Playas del este", "Lomé → Baguida / Coco Beach", "~15 km · 1 noche"),
        ("Bajada 3 · Lago Togo", "Baguida → Agbodrafo → Togoville (piragua) → vuelta a Agbodrafo", "~25 km + travesía · 1 día"),
        ("Bajada 4 · Hacia Benín", "Agbodrafo → Aného/Glidji → Hillacondji", "~25 km · 1 día"),
        ("Subida 1 · Entrada por el interior", "Ouaké (Benín) → Kétao → Kara", "~90 km · 1 día"),
        ("Subida 2 · Base de Kara", "Kara → Sarakawa (fauna) y mercado de Kara", "~30 km en bucle · 1 día"),
        ("Subida 3 · Koutammakou (CONDICIONADO)", "Kara → Kandé → Nadoba (takienta) → vuelta a Kara", "~170 km ida y vuelta · 1-2 días · solo si la seguridad lo permite"),
        ("Subida 4 · La falla y el centro", "Kara → Bafilo → falla de Aledjo → Sokodé", "~100 km · 1-2 días"),
        ("Subida 5 · Hierro y montaña", "Sokodé → Bassar (metalurgia) → Fazao-Malfakassa → Sokodé", "~280 km en bucle · 2 días de pista"),
        ("Subida 6 · Bajada por la N1", "Sokodé → Blitta → Atakpamé", "~160 km · 1 día"),
        ("Subida 7 · El Litimé y Akloa", "Atakpamé → Badou (cascada de Akloa) → Kpalimé", "~180 km · 1-2 días con la caminata"),
        ("Subida 8 · Bloque de Kpalimé", "Kpalimé → Womé → Kpimé → Klouto/Château Viale → monte Agou", "~120 km en bucles · 2-3 días"),
        ("Subida 9 · Salida a Ghana", "Kpalimé → Tomegbé → Wli (Ghana)", "~40 km · ½ día + frontera"),
    ],
    offroad=[
        "Falla de Aledjo (N1, entre Bafilo y Kara): no es una pista, pero sí el tramo de carretera más espectacular del país — un tajo vertical abierto en la roca de la cadena de Aledjo por el que pasa la nacional entre dos paredes. Mirador arriba y parada fotográfica obligada con los dos vehículos.",
        "Pistas de Bassar hacia las aldeas de los hornos (Tabalé, Bandjéli, Nangbani): 20-40 km de tierra roja desde Bassar hasta los yacimientos de metalurgia antigua, sin servicios y con vados; en lluvias se embarran rápido. Guía local imprescindible: los hornos no están señalizados.",
        "Accesos a Fazao-Malfakassa desde el eje Sokodé-Bassar: pistas de tierra por el escarpe de la cadena de Fazao, sin puerta oficial publicada ni señalización fija. Llevar GPX y autonomía completa; confirmar el estado de la gestión del parque antes de entrar.",
        "Sierra de Klouto y subida al Château Viale (Kpalimé): 12 km de pista estrecha y muy revirada que gana 400 m entre cafetales y bosque; en temporada de lluvias, barro resbaladizo y tramos lavados. Terreno cómodo para 4x4, imposible para turismos.",
        "Carretera de la cumbre del monte Agou: asfalto y hormigón estrechísimos con curvas de herradura muy cerradas, subiendo casi 800 m hasta las antenas. Se puede subir en vehículo, pero la gracia está en subir a pie; la cima estricta tiene instalación militar y puede estar restringida.",
        "La carretera del Litimé (Atakpamé → Badou → Kpalimé): una de las más bonitas del país, entre cacaotales y plantaciones de café, con tramos de asfalto degradado y desprendimientos en lluvias. No es 4x4 puro pero sí conducción lenta y exigente.",
        "ESTADO DE LAS CARRETERAS EN LLUVIAS: el sur tiene dos estaciones húmedas (abril-julio y septiembre-octubre) y el norte una sola (mayo-octubre). La N1 asfaltada aguanta bien, pero todas las pistas laterales (Bassar, Fazao, Klouto, Koutammakou) se degradan mucho en el pico de lluvias. Los relatos de viajeros avisan además de RETENCIONES LARGAS EN CONTROLES POLICIALES Y MILITARES en el norte, que hay que meter en el cálculo de tiempos.",
    ],
    senderismo=[
        "MONTE AGOU (Pic Baumann, 986 m) — LA excursión a pie de Togo: subida al punto más alto del país desde Nyogbo o Agou-Nyogbo, 3-4 horas por caminos entre aldeas escalonadas de cultivadores de café, con vista sobre el lago Volta ghanés los días claros. Guía local barato e imprescindible: los senderos se ramifican y no hay señalización. La cima estricta tiene antenas y puesto militar — preguntar antes de llegar arriba.",
        "Cascada de Akloa (Badou): unos 45 minutos de subida en selva desde el aparcamiento, entre plantaciones de cacao, hasta un salto de 35-60 m con poza de baño. Tasa comunitaria y guía del pueblo. Resbaladizo: calzado con suela agarrada.",
        "Cascada de Womé (Kpalimé): caminata corta y fácil desde la aldea de Womé, 12 km al norte de Kpalimé, hasta el salto y su poza. La mejor de las dos cascadas clásicas de Kpalimé y la que no depende de una presa.",
        "Cascada de Kpimé: escalera y sendero hasta el mirador y hasta el pie del salto. Comprobar antes que hay agua (depende de la central hidroeléctrica).",
        "Meseta de Klouto (710 m): red de senderos entre aldeas por el bosque más denso del país, con guías especializados en mariposas (más de 1.000 especies catalogadas) y en aves. Se combina con el Château Viale en la cima y con el valle de los murciélagos al atardecer.",
        "Cascada de Bafilo: caminata corta desde el pueblo de Bafilo, en el corredor interior, buena para romper el tramo Kara-Sokodé.",
        "Koutammakou (si es visitable): recorrido a pie entre las takienta de Nadoba y las aldeas vecinas, con guía de la comunidad; paisaje abierto de sabana con baobabs y torres-vivienda. Sol directo y sin sombra — ir a primera hora.",
    ],
    acampada=[
        "Playas del este de Lomé (Baguida, Avépozo, Coco Beach): alojamientos y campings sencillos junto a la arena con aparcamiento a la vista; la pernocta más cómoda del corredor de bajada y la más fácil con el perro.",
        "Lomé: hoteles con parking vigilado, más práctico que la acampada libre en la capital. iOverlander recoge además puntos de acampada libre en la orilla del lago Togo — verificar la fecha del último comentario antes de fiarse.",
        "Agbodrafo / lago Togo: pequeños alojamientos junto a la laguna, con aparcamiento; agua tranquila y sin resaca, a diferencia de la playa atlántica.",
        "Kara: Hôtel Kara, Hôtel La Douceur, Hôtel de l'Union y similares, todos con aparcamiento — base obligada del norte.",
        "Sokodé: Hôtel Central y otros alojamientos de carretera con patio cerrado; parada intermedia del eje N1.",
        "Kpalimé: la mejor oferta del interior (Hôtel Parc Résidence y varias auberges de montaña) con aparcamiento y clima fresco; base para 2-3 noches del bloque final.",
        "Acampada libre: posible en el interior con permiso del jefe de la aldea, como en el resto de África occidental. NO acampar libre en la mitad norte del país (al norte de Sokodé) por la situación de seguridad y los controles militares nocturnos.",
    ],
    visado=[
        "e-Visa togolés obligatorio para pasaportes españoles, solicitado con AL MENOS 5 días de antelación (tramitación de hasta 5 días hábiles). Togo ya NO emite visado a la llegada para ninguna nacionalidad.",
        "Tarifas oficiales publicadas: 25.000 FCFA (15 días, entrada única), 35.000 FCFA (15 días, multientrada), 45.000 FCFA (30 días), 65.000 FCFA (90 días). Al cruzar el país DOS VECES con meses de diferencia, lo previsible es necesitar dos e-Visas separados — confirmar si alguna modalidad multientrada cubre las dos pasadas.",
        "Formulario de inmigración obligatorio para todos los viajeros, completado como máximo 24 h antes de la llegada, además del visado.",
        "Pasaporte con validez mínima de 6 meses desde la entrada.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
        "Confirmar validez del e-Visa en FRONTERA TERRESTRE (no solo en el aeropuerto de Lomé) 30-60 días antes: es el punto que hay que dejar cerrado por escrito antes de presentarse en Aflao o en Ouaké.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Aflao/Kodjoviakopé (Ghana)", "Paso más transitado del tramo; menos de 1 km entre puestos; horario aprox. 06:00-18:00; cuidado con estafadores de cambio."),
        ("Salida bajada", "Hillacondji/Sanvee-Condji (Benín)", "Puesto conjunto (yuxtapuesto); cruzar por la mañana, el tráfico comercial satura el mediodía."),
        ("Entrada subida", "Ouaké (Benín, eje Djougou-Kara)", "24/7 salvo festivos beninenses según el Logistics Cluster; exige seguro CEDEAO y laissez-passer. Confirmar nombre y horario del puesto togolés."),
        ("Alternativa entrada subida", "Tohoun/Azovè (Benín, eje central)", "Mucho más al sur y fuera de toda zona de riesgo; opción si el norte desaconseja Ouaké. Coordenada y horario por verificar."),
        ("Salida subida", "Wli/Kpalimé (Ghana, región del Volta)", "Paso menor de montaña; lado ghanés lento y desorganizado — revisar personalmente sellos y fechas del carnet; aduana togolesa unos km dentro, cerca de Tomegbé."),
        ("EXCLUIDA", "Cinkassé (Burkina Faso)", "Puesto integrado del corredor Lomé-Uagadugú, en las Savanes; desaconsejado para extranjeros y fuera del itinerario."),
    ],
    vehiculos=[
        "Togo no emite CPD propio: llevar el CPD tramitado en España (RACE) con todos los pares de sellos en regla.",
        "SIN carnet, la aduana exige un LAISSEZ-PASSER de importación temporal. Pedirlo expresamente en el puesto de entrada y conservarlo: el control real se hace al salir del país.",
        "Carte Brune CEDEAO como seguro de responsabilidad civil regional — Togo es Estado miembro del esquema; confirmar que la póliza lo lista explícitamente.",
        "Carnet de conducir internacional obligatorio en todos los controles; en el corredor interior de subida hay muchos más controles policiales y militares que en la costa.",
        "Llevar copias de toda la documentación por triplicado: en el corredor norte los controles son frecuentes y minuciosos.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Sin procedimiento civil turístico claro y estable publicado por la ANAC-Togo: tratar como prohibido sin autorización previa por escrito.",
        "No volar cerca del aeropuerto de Lomé, del puerto, de las fronteras (Aflao, Hillacondji, Wli, Ouaké) ni de instalaciones militares — incluida la cumbre del monte Agou, que tiene puesto militar.",
        "Al norte de Sokodé, con operación militar activa y estado de emergencia en las Savanes, no sacar el dron de la caja bajo ningún concepto.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Togo NO figura entre los países africanos con Starlink activo en los recuentos de septiembre de 2026 — a diferencia de Benín, que sí. Planificar el tramo togolés sin conectividad por satélite.",
        "SIM local (Togocom, Moov Africa) como conectividad principal; cobertura razonable en el eje N1 y en Lomé, más débil en las sierras de Klouto y Agou y en las pistas de Bassar y Fazao.",
        "Revisar el mapa oficial de Starlink 30-60 días antes de cada una de las dos entradas, por si cambia el estado.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo. Documentación en francés.",
        "Régimen francófono típico: conviene que la antirrábica tenga menos de 12 meses, no solo que esté «en vigor» — varios países francófonos de la ruta lo exigen así de forma explícita.",
        "El dosier del proyecto marca Togo como [SIN CONFIRMAR] en cuanto a permiso de importación previo. A quién escribir: Direction de l'Élevage, Lomé. Al cruzarse el país DOS VECES, contar con dos trámites separados salvo confirmación escrita en contra.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE).",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional OBLIGATORIO para la entrada, y lo piden de verdad en frontera.",
        "Malaria presente en todo el territorio y durante todo el año: profilaxis a valorar con Sanidad Exterior.",
        "CHU Sylvanus Olympio (Lomé) y CHU Kara son las dos únicas referencias hospitalarias serias, una en cada corredor; entre ambas hay 412 km. Seguro con evacuación médica imprescindible.",
        "Agua: no beber de la red en ningún punto del país. Embotellada o tratada siempre, también para lavarse los dientes.",
        "Costa con resaca fuerte y corrientes de retorno en casi todo el litoral: los ahogamientos son el accidente más frecuente de los visitantes en la playa.",
    ],
    seguridad_intro=("Togo se divide con nitidez en dos mitades de seguridad. El eje costero y el centro del país (Lomé, lago Togo, Aného, Atakpamé, Kpalimé, Sokodé y hasta Kara) son estables y se recorren con precaución normal. "
                     "El extremo norte NO: desde noviembre de 2021 hay ataques de grupos armados procedentes de Burkina Faso, y en junio de 2022 se decretó un estado de emergencia en la REGIÓN DE LAS SAVANES que se ha prorrogado sucesivamente. "
                     "Los avisos de viaje sitúan en nivel máximo (no viajar) la franja fronteriza con Burkina Faso y LAS ZONAS AL NORTE DE KANDÉ, y señalan que los extranjeros necesitan autorización gubernamental específica para entrar en las Savanes. "
                     "El problema práctico para este proyecto es que Koutammakou, el mayor tesoro del país, está justo dentro de esa franja."),
    seguridad=[
        "REGIÓN DE LAS SAVANES (Dapaong, Mango, Cinkassé, Kpendjal y Kpendjal-Oeste, cuevas de Nok y Mamproug, Fosse aux Lions): estado de emergencia en vigor y autorización gubernamental necesaria para extranjeros. Excluida del itinerario en cualquier escenario.",
        "NORTE DE KANDÉ (incluido Koutammakou/Nadoba): franja marcada como zona de no viajar por terrorismo y secuestro. La visita a Koutammakou queda CONDICIONADA a una reevaluación a 30 días vista con avisos oficiales actualizados; si sigue igual, se cae del itinerario.",
        "Carreteras nacionales N24 y N28 y pernocta al norte de Mango: restringidas incluso para personal diplomático extranjero. No planificar nada por ahí.",
        "Frontera de Cinkassé con Burkina Faso: desaconsejada para extranjeros; el corredor Lomé-Uagadugú no forma parte de este viaje.",
        "Controles policiales y militares frecuentes en toda la mitad norte: documentación por triplicado, actitud tranquila, y presupuestar tiempo extra en las etapas del corredor interior.",
        "Lomé: delincuencia común de oportunidad (carterismo y tirones en el Grand Marché y en la playa urbana). No caminar por la playa de Lomé de noche.",
        "Cambio de moneda en Aflao: usar solo casas de cambio autorizadas, nunca particulares en el paso fronterizo.",
        "Manifestaciones políticas: Togo tiene un historial de protestas y de respuesta policial dura. Evitar cualquier concentración y no fotografiar despliegues de seguridad.",
        "Llevar siempre el certificado de fiebre amarilla, el e-Visa impreso y copias de la documentación del vehículo.",
    ],
    agua=[
        "Lomé, Aného, Kara, Sokodé, Atakpamé y Kpalimé: agua embotellada en supermercados y tiendas sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio de Lomé y los hoteles con aparcamiento de Kara, Sokodé y Kpalimé permiten llenar el depósito con manguera; confirmar en recepción.",
        "En las aldeas del corredor interior (Bassar, Fazao, Nadoba, Badou) no contar con recarga: salir con el depósito lleno desde Kara, Sokodé o Kpalimé según el tramo.",
        "Nunca beber de la red pública ni de pozos sin tratar en ningún punto del país.",
    ],
    combustible=[
        "Bajada: sin ningún riesgo de gap — Aflao → Lomé (~5 km) → Baguida (~12 km) → Agbodrafo (~33 km) → Aného (~15 km) → Hillacondji (~7 km), todos con estaciones formales. Repostar a fondo en Lomé, que es donde mejor está el combustible.",
        "Subida: tampoco hay gap de 500 km en el eje N1 — Ouaké/Kara (~90 km) → Bafilo/Aledjo (~45 km) → Sokodé (~55 km) → Atakpamé (~160 km) → Badou (~90 km) → Kpalimé (~90 km) → frontera de Wli (~40 km). El tramo más largo sin servicios reales es Sokodé-Atakpamé.",
        "Los desvíos SÍ exigen autonomía propia: Bassar y las aldeas de los hornos, el bucle de Fazao-Malfakassa y la subida a Koutammakou no tienen oferta fiable. Salir con el depósito lleno desde Sokodé o Kara y llevar garrafas.",
        "Calidad irregular fuera de las ciudades: evitar el combustible callejero en botellas («boutique de bidons»), muy extendido en Togo y de calidad impredecible.",
    ],
    experiencias_intro="Relatos y comentarios reales de otros overlanders y viajeros sobre Togo, para contrastar con el contenido oficial de esta ficha:",
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Koutammakou · ¿visitable en 2027?", "DECISIÓN CRÍTICA. Reevaluar a 30 días vista con avisos oficiales actualizados (Estado español, EE. UU., Francia) y con el gestor del sitio; si la franja al norte de Kandé sigue en nivel máximo, se cae del itinerario"),
        ("e-Visa en frontera terrestre", "Confirmar por escrito que el e-Visa togolés se admite en Aflao y en Ouaké, no solo en el aeropuerto de Lomé"),
        ("e-Visa doble entrada", "Confirmar si alguna modalidad multientrada cubre las dos pasadas (bajada y subida, con meses de diferencia) o si hacen falta dos trámites"),
        ("Laissez-passer del vehículo", "Confirmar si con el CPD español basta o si Togo emite igualmente un laissez-passer; exigir el papel en el puesto de entrada y guardarlo hasta la salida"),
        ("Puesto togolés de Ouaké", "Confirmar nombre exacto, coordenada y horario real del lado togolés del paso de Ouaké (eje Djougou-Kara) antes de fijar el corredor de subida"),
        ("Frontera de Tohoun/Azovè", "Verificar coordenada, horario y viabilidad con vehículo propio como alternativa segura a Ouaké"),
        ("Frontera de Wli/Kpalimé", "Confirmar horario y que acepta carnet/laissez-passer con vehículo de 4 ruedas (los relatos disponibles son de motos)"),
        ("Perro · permiso de importación", "Escribir a la Direction de l'Élevage de Lomé: ¿hace falta permiso previo?, ¿vale uno para las dos entradas?"),
        ("Perro en Sarakawa", "Confirmar por escrito si el perro puede entrar en el vehículo en la reserva de Sarakawa: es el mejor candidato del país a fauna compatible con el perro"),
        ("Fazao-Malfakassa · estado real", "Confirmar quién gestiona hoy el parque, si está abierto, tasas, puerta de entrada con coordenada y si merece el desvío de 2 días"),
        ("Cascada de Kpimé", "Preguntar en Kpalimé el mismo día si tiene agua antes de subir"),
        ("Dron", "Contactar con la ANAC-Togo o descartar directamente el vuelo en el país"),
        ("Starlink", "Revisar el mapa oficial 30-60 días antes de cada entrada por si Togo pasa a estar activo"),
        ("Fotos pendientes de sustituir", "Lomé alemán, Bassar, Fazao-Malfakassa, Sokodé, playas del este y Klouto usan imágenes de referencia de la región o del país, no del propio sitio: sustituir por fotos propias cuando las tengamos"),
        ("Coordenadas aproximadas", "Akodessewa, Palais de Lomé, Sarakawa, Fazao-Malfakassa y las fronteras de Tohoun y Wli están fijadas con coordenada aproximada: afinarlas sobre el terreno o con cartografía Tracks4Africa"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. La situación de seguridad del norte de Togo es dinámica: revalidarla obligatoriamente antes de cada entrada.",
    emergency="Policía 117 · Bomberos 118 · Gendarmería 172 · Emergencia consular española (Embajada en Accra, acreditada en Togo): +233 302 77 40 04.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

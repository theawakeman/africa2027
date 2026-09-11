# -*- coding: utf-8 -*-
"""Angola — ficha completa, corredor doble bajada/subida (11 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ---- BAJADA: Lufu/Luvo (RD Congo) -> Luanda -> Malanje -> Cazombo/Caripande (Zambia) ----
    dict(n=1, name="Luanda", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-8.8383, lon=13.2344,
         desc="Capital y mayor base logística del país: puerto, aeropuerto internacional, embajada de España, talleres y recambios de todo tipo. Marginal (paseo marítimo), Fortaleza de San Miguel e Ilha de Luanda como referencia urbana e histórica. Punto de paso obligado tanto en la bajada como en la subida.",
         credit="Chimpanz APe · CC BY 2.0", source=W + "2009%20Luanda%20Angola%203818325721.jpg?width=900"),
    dict(n=2, name="Miradouro da Lua", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=-9.1667, lon=13.0333,
         desc="Paisaje erosionado de cañones y formaciones lunares sobre el Atlántico, a 40 km al sur de Luanda; mirador espectacular al atardecer y parada obligada nada más salir de la capital.",
         credit="Paulo César Santos · CC0", source=W + "Miradouro%20da%20Lua%20(Angola).jpg?width=900"),
    dict(n=3, name="Pedras Negras de Pungo Andongo", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=-9.6625, lon=15.5839,
         desc="Descomunales monolitos de roca negra que emergen de la sabana verde, visibles desde 50 km de distancia; lugar de leyenda de la reina Nzinga (huellas talladas en la roca) y ruinas de un fuerte portugués del siglo XVII. Uno de los mejores vivac salvajes documentados por otros overlanders en Angola, junto a arroyos claros entre los bloques de granito.",
         credit="Wikimedia Commons", source=W + "Pungo%20Andongo%2C%20Malange%2C%20Angola.JPG?width=900"),
    dict(n=4, name="Cascadas de Kalandula (Calandula)", cat="Naturaleza", prio="Alta", dog="permitido", time="½–1 día",
         lat=-9.0758, lon=16.0033,
         desc="Con 105 m de altura y 400 m de anchura, la segunda mayor catarata de África por caudal tras las Victoria Falls, sobre el río Lucala en la provincia de Malanje; a unos 360 km de Luanda por una carretera que combina tramos asfaltados con pistas de tierra en buen estado. Desvío interior recomendado antes de internarse hacia el este del país.",
         credit="Wikimedia Commons", source=W + "Kalandula%20waterfalls%20of%20the%20Lucala-River%20in%20Malange%2C%20Angola.JPG?width=900"),
    # ---- SUBIDA: Namibia -> Namibe/Leba/Tundavala -> Lobito -> Kissama -> Luanda -> Lufu/Luvo ----
    dict(n=5, name="Namibe (Moçâmedes)", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-15.1961, lon=12.1522,
         desc="Ciudad y puerto donde el desierto del Namibe llega literalmente al Atlántico; arquitectura colonial portuguesa en la Marginal, base logística para el desierto, Tundavala, Serra da Leba y la expedición avanzada a la Baía dos Tigres.",
         credit="Wikimedia Commons", source=W + "Marginal%20of%20Namibe.JPG?width=900"),
    dict(n=6, name="Baía dos Tigres (avanzado, opcional)", cat="Naturaleza", prio="Media", dog="permitido con precaución", time="2–3 días (expedición)",
         lat=-16.6167, lon=11.7833,
         desc="Antigua península convertida en isla en 1962, con el pueblo pesquero abandonado tragado por la arena; el tramo mítico de duna-hasta-el-mar del sur de Angola. Se llega desde Tombwa cruzando el paso de marea 'Doodsakker', navegable solo con marea baja y luna llena o nueva. Mínimo 2 vehículos 4x4, equipo de recuperación y planificación de mareas — es exactamente el tipo de expedición 4x4 que buscamos para el bloque sur, pero exige preparación experta o un guía local.",
         credit="Wikimedia Commons", source=W + "Ilha%20dos%20Tigres%201466540%20960%20720.jpg?width=900"),
    dict(n=7, name="Parque Nacional de Iona", cat="Naturaleza", prio="Alta", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=-16.7000, lon=12.3333,
         desc="15.200 km² de desierto del Namib angoleño gestionados por African Parks: oryx, cebras, springbok, guepardo, leopardo, hiena parda y jirafas angoleñas reintroducidas en 2023-2024 tras desaparecer en la guerra civil; welwitschias milenarias (posiblemente de más de 2.000 años). Pistas de tierra y arena sin señalización fija — llevar GPX o guía local.",
         credit="Wikimedia Commons", source=W + "Welwitschia%20in%20the%20Namibe%20desert.JPG?width=900"),
    dict(n=8, name="Foz do Cunene", cat="Naturaleza", prio="Media", dog="permitido con precaución", time="1 noche",
         lat=-17.3000, lon=11.6667,
         desc="Desembocadura del río Cunene, frontera natural con Namibia, entre dunas y un paisaje casi lunar; aguas termales río arriba (extremar precaución, hay cocodrilos aguas abajo). Combinar con Iona en un mismo bucle de 2-3 días desde Namibe. Imagen de referencia del entorno desértico costero de la provincia de Namibe — no es una foto exacta de la desembocadura.",
         credit="Wikimedia Commons", source=W + "Angola%20Namibe%20Bentiaba%20OM%2020170710%20(19).jpg?width=900"),
    dict(n=9, name="Serra da Leba", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=-15.0711, lon=13.2486,
         desc="El puerto de montaña más fotografiado de Angola: la EN280 sube en herraduras cerradas desde la llanura costera (~720 m) hasta 1.845 m de altitud, enlazando Namibe con la meseta de Lubango. Asfaltado pero exigente; mirador junto a la carretera con vistas a todo el valle.",
         credit="Wikimedia Commons", source=W + "Serra%20da%20Leba-Road.jpg?width=900"),
    dict(n=10, name="Tundavala (Fenda da Tundavala)", cat="Naturaleza", prio="Alta", dog="permitido con correa corta", time="½ día",
         lat=-14.8177, lon=13.3814,
         desc="Grieta de unos 800 m en el borde de la meseta de Humpata, a 18 km de Lubango, con un salto de más de 1.000 m hasta la llanura; una de las 7 Maravillas Naturales de Angola. Pista de tierra desde Lubango; el mirador está en el mismo borde del acantilado, correa corta imprescindible.",
         credit="Wikimedia Commons", source=W + "Tundavala%20Gap.jpg?width=900"),
    dict(n=11, name="Lobito", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-12.3644, lon=13.5456,
         desc="Ciudad portuaria sobre una restinga arenosa entre el océano y la bahía, con arquitectura colonial portuguesa bien conservada (Igreja da Arrábida) y ambiente más tranquilo que Luanda; punto de descanso en la subida hacia la capital.",
         credit="Robertoago · CC BY-SA 3.0", source=W + "Lobito%20restinga2.jpg?width=900"),
    dict(n=12, name="Parque Nacional de Kissama (Quiçama)", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido", time="1 día",
         lat=-9.7500, lon=13.5830,
         desc="A unos 70 km al sur de Luanda, el único parque nacional angoleño realmente operativo, repoblado tras la guerra con la 'Operación Arca de Noé' (elefantes y otras especies traídos de Botsuana y Sudáfrica); baobabs, candelabros y sabana junto al río Kwanza. Reserva de la Biosfera UNESCO desde 2025. Última parada de naturaleza antes de cerrar la subida por Luanda.",
         credit="Wikimedia Commons", source=W + "Kissama%20003.JPG?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "naturaleza": "verde", "cultura": "marron"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada bajada — Lufu/Luvo (desde RD Congo)", "Frontera", -5.9167, 13.9667,
     "Cruce del puente fronterizo con RD Congo; registro y sellado ~500 m dentro de Angola. Desvío opcional a M'banza-Kongo (Patrimonio Mundial UNESCO, antigua capital del Reino del Kongo) a poca distancia. También es la frontera de SALIDA en la subida, cerrando el corredor angoleño."),
    ("Frontera · Salida bajada — Caripande (hacia Zambia, cerca de Cazombo)", "Frontera", -11.9000, 22.9000,
     "Paso remoto en el extremo este de Angola (provincia de Moxico), frente al puesto zambiano de Chavuma. Otros overlanders describen la oficina de inmigración angoleña como muy precaria (secuelas de la guerra) y el trámite en portugués; más de 100 km de pistas de arena con charcos profundos entre Cazombo y la zona previa a la frontera, intransitables o muy lentos en temporada de lluvias (octubre-marzo). Cruzar solo en temporada seca (mayo-septiembre) y registrarse en la policía de Cazombo."),
    ("Frontera · Entrada subida — Santa Clara/Oshikango (desde Namibia)", "Frontera", -17.3500, 15.7500,
     "Paso principal y más transitado entre Angola y Namibia; carretera asfaltada en ambos lados, infraestructura de control moderna. Punto de entrada de la subida hacia Namibe, Serra da Leba y Tundavala."),
    ("Frontera · Alternativa subida — Calueque/Ruacana (desde Namibia)", "Frontera", -17.2825, 14.5347,
     "Paso alternativo más al oeste, junto a la presa de Calueque sobre el río Cunene y el puesto namibio de Ruacana/Omahenene; pista sin asfaltar en el lado angoleño, más lenta que Santa Clara pero da acceso directo a las cataratas de Ruacana, Epupa (lado namibio) y al Parque Nacional de Iona sin desvío adicional."),
    ("Embajada de España en Luanda", "Consular", -8.8167, 13.2333,
     "Rua Frederico Welwitsch 84, Torre Maculusso, 12º andar C, Postal 3061, Luanda. Tel. +244 222 391 166/187/188 · Emergencia consular: +244 929 900 900."),
    ("Hospital Américo Boavida — Luanda", "Hospital", -8.8147, 13.2302,
     "Principal hospital de referencia de la capital. Coordenada urbana aproximada."),
    ("Hospital Central da Huíla — Lubango", "Hospital", -14.9077, 13.4925,
     "Referencia hospitalaria del tramo de Serra da Leba y Tundavala, en la subida entre Namibe y la costa."),
    ("Combustible · Luanda / Lobito", "Combustible", -8.8383, 13.2344,
     "Mejor oferta y calidad del país (Sonangol, Pumangol) en las dos grandes ciudades costeras; repostar a fondo en ambas."),
    ("Combustible · M'banza-Kongo / Uíge (eje norte)", "Combustible", -6.2667, 14.2500,
     "Estaciones formales en el desvío norte antes de bajar a Luanda; confirmar disponibilidad, oferta más limitada que en la costa."),
    ("Combustible · Malanje", "Combustible", -9.5402, 16.3410,
     "Última oferta formal de combustible sólida antes de internarse hacia el este (Kuito, Luena, Cazombo); repostar a fondo aquí en la bajada."),
    ("Combustible · Cazombo (extremo este, escaso)", "Combustible", -11.9000, 22.9000,
     "Oferta muy limitada e irregular; llegar con depósitos y garrafas de reserva llenas desde Luena, sobre todo si el cruce a Zambia se complica por barro."),
    ("Combustible · Namibe / Lubango (eje sur)", "Combustible", -15.1961, 12.1522,
     "Estaciones formales en ambas ciudades; repostar en Namibe antes de Baía dos Tigres/Iona (sin oferta) y de nuevo en Lubango tras Serra da Leba."),
    ("Agua potable y de uso general · Luanda", "Agua potable", -8.8383, 13.2344,
     "Agua embotellada sin problema en supermercados de la capital; estaciones de servicio y hoteles de Luanda y Lobito permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria: tratar como restringido",
                  "Angola exige autorización previa del Instituto Nacional de Aviação Civil (INAVIC) para cualquier vuelo de dron, con especial sensibilidad cerca de instalaciones petroleras y portuarias (Luanda, Lobito, Cabinda) y de la presa de Calueque. Norma prudente del proyecto: no volar sin permiso escrito, y evitar cualquier vuelo cerca de infraestructura energética, militar o de los parques nacionales sin autorización expresa.")

STARLINK_CALLOUT = ("warn", "Anunciado para 2026, aún no activo a mediados de año: tratar como no disponible",
                     "Angola figura entre los mercados africanos con Starlink previsto («coming in 2026») pero sin confirmación de servicio activo a mediados de 2026. Tratarlo como no disponible hasta confirmación oficial y mantener SIM local (Unitel, Africell) como conectividad principal; en el tramo remoto de Moxico (bajada hacia Zambia) no dar por hecho tampoco cobertura móvil continua.")

DOG_MATRIX = [
    ("Luanda, Lobito, Namibe, Miradouro da Lua, Pedras Negras, Kalandula, Serra da Leba, Tundavala", "permitido con condiciones",
     "Correa siempre en miradores y acantilados (Tundavala); calor seco en el sur, más húmedo en la franja costera norte."),
    ("Parque Nacional de Iona / Parque Nacional de Kissama", "no confirmado",
     "Ambos tienen guepardo/leopardo/hiena parda (Iona) o leones y elefantes reintroducidos (Kissama): tratar como prohibido para circular suelto o incluso en vehículo hasta confirmación escrita de African Parks (Iona) y del operador de Kissama. Plan B: visitar el mirador/puerta de entrada dejando al perro con un miembro del grupo en el vehículo con aire y agua, o saltar el parque en ese tramo."),
    ("Baía dos Tigres, Foz do Cunene", "permitido con precaución",
     "Sol y calor extremos sin sombra natural en Baía dos Tigres — llevar toldo y agua de sobra; en Foz do Cunene mantener al perro lejos de la orilla por los cocodrilos del Cunene aguas abajo."),
]

SOURCES = [
    ("Angola-Visa.com · proceso de e-visa para viajeros overland", "https://www.angola-visa.com/overland/"),
    ("Hinterland Travel · requisitos de visado de Angola para ciudadanos españoles", "https://www.hinterlandtravel.com/spain/destinations/angola"),
    ("WhirledAway · cruce de frontera Lufu (RD Congo) / Luvo (Angola)", "https://whirled-away.com/border-crossing-drc-angola/"),
    ("Embajada de España en Angola · contacto", "https://www.exteriores.gob.es/Embajadas/luanda/es/Paginas/index.aspx"),
    ("tech.africa · disponibilidad de Starlink en África (2026)", "https://tech.africa/starlink-africa/"),
    ("UNESCO · Mbanza Kongo, vestigios de la capital del antiguo Reino del Kongo", "https://whc.unesco.org/en/list/1473/"),
    ("iOverlander · puntos de combustible, agua y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía, puntos overland y blog de viajeros por África", "https://tracks4africa.co.za/"),
    ("Tracks4Africa Blog · «Angola… an acquired taste» — guía práctica de overland por Angola", "https://blog.tracks4africa.co.za/angola-acquired-taste/"),
    ("Paul Godard · relato de expedición 4x4 por el sur de Angola (2022)", "https://www.paulgodard.com/blog/79"),
    ("Africa Overland Blog · cruce de frontera Zambia-Angola por Chavuma/Caripande y travesía hasta Kalandula", "https://africaoverland.blog/2019/12/08/road-tripping-across-angola/"),
    ("kumakonda.com · expedición 4x4 a Baía dos Tigres y Foz do Cunene", "https://kumakonda.com/ilha-da-baia-dos-tigres-angola/"),
    ("Wikipedia · Iona National Park", "https://en.wikipedia.org/wiki/Iona_National_Park"),
    ("African Parks · Parque Nacional de Iona", "https://www.africanparks.org/the-parks/iona"),
    ("Wikipedia · Quiçama National Park", "https://en.wikipedia.org/wiki/Qui%C3%A7ama_National_Park"),
    ("Wikipedia · Kalandula Falls", "https://en.wikipedia.org/wiki/Kalandula_Falls"),
    ("Wikipedia · Black Rocks at Pungo Andongo", "https://en.wikipedia.org/wiki/Black_Rocks_at_Pungo_Andongo"),
    ("Wikipedia · Tundavala Gap", "https://en.wikipedia.org/wiki/Tundavala_Gap"),
    ("Wikipedia · Serra da Leba", "https://en.wikipedia.org/wiki/Serra_da_Leba"),
    ("Wikipedia · Cazombo", "https://en.wikipedia.org/wiki/Cazombo"),
    ("Wikipedia · Calueque", "https://en.wikipedia.org/wiki/Calueque"),
]

CORRIDOR = [(-5.9167, 13.9667), (-8.8383, 13.2344), (-9.1667, 13.0333), (-9.6625, 15.5839),
            (-9.0758, 16.0033), (-9.5402, 16.3410), (-11.9000, 22.9000)]

CORRIDOR_ALT = [(-17.3500, 15.7500), (-16.7000, 12.3333), (-17.3000, 11.6667), (-15.1961, 12.1522),
                (-16.6167, 11.7833), (-15.0711, 13.2486), (-14.8177, 13.3814), (-12.3644, 13.5456),
                (-9.7500, 13.5830), (-8.8383, 13.2344), (-5.9167, 13.9667)]

EXPERIENCIAS = [
    "Expedición 2022 por el sur de Angola (Paul Godard, 4 semanas, 2 vehículos): entrada por Santa Clara con e-visa (120 $/persona, 80 $ pagando en moneda local); ruta real Ondjiva → Xangongo → Calueque → cataratas de Ruacana → Epupa → Parque de Iona → desembocadura del Cunene → Namibe → Serra da Leba → Lubango → Tundavala → Kalandula → Pedras Negras → Kissama → Luanda. La EN140 la describen como «la peor carretera asfaltada jamás vista», con baches de hasta 80 cm; acampada libre en casi todo el trayecto, avisando siempre al jefe del pueblo o los ancianos locales.",
    "Cruce Zambia→Angola por Chavuma/Caripande (Africa Overland Blog, ruta este-oeste hasta Kalandula): oficina de inmigración angoleña descrita como «una sala diminuta y sucia, con agujeros de bala de la guerra civil»; trámite negociado en portugués. Más de 100 km de pistas de arena con charcos profundos y puentes de madera inestables; velocidad real de 10-20 km/h. Llevar cuerdas de remolque — ayudar a vehículos varados es una norma no escrita en estas pistas. Cruzaron en diciembre, al inicio de las lluvias, y lo describen como muy exigente: recomendable evitarlo en plena temporada húmeda (octubre-marzo).",
    "Baía dos Tigres (kumakonda.com): el paso de marea 'Doodsakker' solo es practicable con marea baja y luna llena o nueva; se recomienda mínimo 2 vehículos, equipo de recuperación y, si se quiere llegar a la propia isla, una embarcación auxiliar. Los operadores especializados insisten en que es una expedición que requiere planificación profesional, no un tramo para improvisar en solitario.",
    "Consejos generales de Tracks4Africa para overlanders en Angola: TIP (importación temporal) y seguro local de terceros obligatorios en cualquier frontera; llevar un embudo con filtro para el combustible, ya que la calidad del gasóleo/gasolina es irregular fuera de las grandes ciudades; la acampada libre está generalmente permitida en zonas remotas; los controles de policía a la entrada de los pueblos suelen ser correctos y sin problemas.",
    "Política de mascotas en Iona y Kissama: no se ha localizado ninguna normativa pública específica sobre perros en ninguno de los dos parques. Dado que ambos tienen depredadores grandes (Iona: guepardo, leopardo, hiena parda; Kissama: leones reintroducidos) o megafauna (elefantes en Kissama), la práctica habitual en parques africanos comparables es prohibirlos dentro del vehículo en zona de fauna — contactar directamente con African Parks (Iona) y con el operador de Kissama antes de viajar para confirmar, y tener un plan B (mirador de entrada, o turnos para quedarse con el perro fuera del parque).",
]

CORRIDOR_LABEL = "Bajada"
CORRIDOR_ALT_LABEL = "Subida"

HISTORIA_RESUMEN = ("Angola, heredera del gran reino de Ndongo y del reino de Kongo, sufrió casi cinco siglos de presencia colonial portuguesa centrada en la trata de esclavos hacia Brasil, y tras una independencia tardía en 1975 se sumió de inmediato en una guerra civil de 27 años "
                     "(1975-2002) que fue uno de los grandes escenarios de la Guerra Fría en África, con Cuba y la URSS apoyando al gobierno marxista y Sudáfrica y Estados Unidos a la guerrilla de UNITA; la paz de 2002 dio paso a un boom petrolero que ha transformado Luanda en una de las ciudades más caras del mundo.")

HISTORIA_SECCIONES = [
    ("Los reinos de Kongo y Ndongo",
     "El norte del actual territorio formó parte del reino de Kongo, mientras que el reino de Ndongo, gobernado en el siglo XVII por la célebre reina Nzinga Mbandi —hoy símbolo nacional de resistencia—, libró una larga lucha contra el avance portugués antes de sucumbir a la ocupación colonial."),
    ("Cinco siglos de colonización portuguesa y la trata de esclavos",
     "Portugal estableció su presencia en la costa angoleña ya en el siglo XV, y Angola se convirtió en uno de los mayores puntos de origen de la trata negrera atlántica, con millones de personas embarcadas hacia Brasil a lo largo de tres siglos; el dominio colonial portugués, uno de los más prolongados y tardíos en abandonar África, se mantuvo hasta 1975."),
    ("Independencia y la guerra civil de la Guerra Fría (1975-2002)",
     "Angola alcanzó la independencia en 1975 tras una guerra de liberación, pero la rivalidad entre los movimientos independentistas MPLA, UNITA y FNLA derivó de inmediato en una guerra civil que se convirtió en uno de los grandes conflictos por delegación de la Guerra Fría: Cuba y la Unión Soviética respaldaron al gobierno marxista del MPLA, mientras Sudáfrica del apartheid y Estados Unidos apoyaron a la guerrilla anticomunista de UNITA liderada por Jonas Savimbi; el conflicto se prolongó, con altibajos, hasta la muerte de Savimbi en 2002."),
    ("Situación actual: boom petrolero y desigualdad",
     "Desde el fin de la guerra, Angola ha vivido un notable boom económico basado en sus enormes reservas petroleras (una de las mayores de África) y, en menor medida, en diamantes, que ha convertido a Luanda en una de las capitales más caras del mundo para expatriados, conviviendo con una desigualdad social muy marcada; el partido MPLA, en el poder desde la independencia, mantiene el control político del país bajo el presidente João Lourenço desde 2017."),
]

HISTORIA_FUENTES = [
    ("BBC News · Angola country profile", "https://www.bbc.com/news/world-africa-13036732"),
    ("Encyclopaedia Britannica · Angola, History", "https://www.britannica.com/place/Angola/History"),
    ("Council on Foreign Relations · Angola's civil war", "https://www.cfr.org/timeline/angolas-civil-war"),
]

SPEC = dict(
    slug="angola", name="Angola", revision="11 sep 2026",
    sub="Corredor doble bajada/subida · documentación · seguridad · logística",
    chips=[
        ("BAJADA", "Lufu/Luvo → Malanje (Kalandula) → Cazombo/Caripande (Zambia)"),
        ("SUBIDA", "Santa Clara/Oshikango → Namibe/Leba/Tundavala → Lobito → Kissama → Luanda → Lufu/Luvo"),
        ("SEGURIDAD", "estable · precaución normal, extremar en el tramo remoto de Moxico"),
        ("VISADO", "exención de 30 días para españoles — verificar vigencia antes de viajar"),
        ("4x4 MÍTICO", "Serra da Leba · Tundavala · Baía dos Tigres (avanzado)"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[-12.0, 15.5], zoom=5,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Angola se recorre DOS VECES en direcciones distintas: en la <strong>bajada</strong>, tras RD Congo, un eje corto por Luanda y un desvío interior a las cascadas de Kalandula y Pedras Negras antes de internarse hacia el este remoto de Moxico y cruzar a Zambia por Caripande/Cazombo; "
                   "en la <strong>subida</strong>, ya de vuelta desde Namibia, el país se cruza por el extremo suroeste — el desierto del Namibe, el Parque Nacional de Iona, Serra da Leba y Tundavala — antes de subir por la costa (Lobito, Kissama) hasta Luanda y salir de nuevo por Lufu/Luvo hacia RD Congo. "
                   "Los dos corredores solo comparten Luanda y la propia frontera del norte; el resto del país se ve por completo distinto en cada pasada."),
    facts=[
        ("Ventana prevista", "Bajada: tras RD Congo, antes de Zambia. Subida: tras Namibia, antes de continuar por RD Congo/Congo hacia el norte."),
        ("Entrada bajada", "Lufu/Luvo desde RD Congo; desvío opcional a M'banza-Kongo (UNESCO) a poca distancia."),
        ("Salida bajada", "Caripande, cerca de Cazombo, hacia Zambia (Chavuma): paso remoto, pistas de arena, solo en temporada seca."),
        ("Entrada subida", "Santa Clara/Oshikango desde Namibia (o Calueque/Ruacana como alternativa más al oeste)."),
        ("Salida subida", "Lufu/Luvo hacia RD Congo, cerrando el corredor angoleño antes de continuar la subida por Congo/Camerún."),
        ("Visado", "Exención de visado de turismo de 30 días para pasaportes españoles a fecha de esta revisión — confirmar vigencia 30-60 días antes; comprobar también si permite las dos entradas (bajada y subida) o si hace falta e-Visa de entrada múltiple."),
        ("Seguridad", "Estable en todo el país, precaución normal; el único tramo que exige planificación adicional es el extremo este (Moxico) en la bajada, por aislamiento y estado de las pistas, no por inseguridad."),
        ("Comunicaciones", "Starlink anunciado para 2026, no confirmado activo; SIM local (Unitel, Africell) como base, con cobertura muy limitada en el tramo de Moxico."),
    ],
    alerts=[
        "Visado: la exención de 30 días para españoles debe reconfirmarse 30-60 días antes de viajar — Angola ha ajustado su política de visados varias veces en los últimos años; si hay cualquier duda, tramitar el e-Visa como respaldo, y verificar expresamente si admite dos entradas separadas (bajada y subida) dentro del mismo viaje.",
        "Reentrada: al tratarse de un corredor doble (se sale hacia Zambia y se vuelve a entrar meses después desde Namibia), confirmar con la representación consular angoleña si la exención de 30 días cubre dos entradas o si hace falta gestionar dos trámites distintos.",
        "Tramo Malanje–Cazombo (bajada): más de 100 km de pista de arena con posibles charcos profundos y puentes de madera; viajar solo en temporada seca (mayo-septiembre) y llevar combustible y agua de reserva — la oferta de ambos es escasa a partir de Malanje.",
        "M'banza-Kongo: desvío que añade tiempo y pista adicional cerca de la frontera de entrada — valorar según el calendario general del tramo centroafricano, que ya acumula varias fronteras complejas seguidas.",
        "Baía dos Tigres: tramo avanzado que depende de mareas y fase lunar; no intentarlo sin al menos 2 vehículos y, idealmente, apoyo de un operador local (p. ej. Sandura Tours) — tratarlo como opcional según tiempo y experiencia del grupo en arena.",
    ],
    ruta_intro="Angola se cruza dos veces por regiones distintas: la bajada por el eje Luanda–Malanje–Moxico hacia Zambia, y la subida por el desierto del suroeste (Namibe–Iona–Leba–Tundavala) y la costa hasta Luanda.",
    route_rows=[
        ("Bajada · Entrada y desvío histórico", "Lufu/Luvo → (M'banza-Kongo opcional) → Luanda", "UNESCO cerca de la frontera; capital como base logística"),
        ("Bajada · Interior de Malanje", "Luanda → Miradouro da Lua → Pedras Negras → Cascadas de Kalandula", "Desvío interior con dos de los paisajes más espectaculares del país"),
        ("Bajada · Travesía a Zambia", "Kalandula → Kuito/Luena → Cazombo → Caripande (frontera)", "Tramo remoto de Moxico; solo en temporada seca, con depósitos llenos"),
        ("Subida · Entrada suroeste", "Santa Clara/Oshikango (o Calueque/Ruacana) → Parque de Iona → Foz do Cunene", "Bucle desértico de 2-3 días antes de subir hacia Namibe"),
        ("Subida · Desierto y meseta", "Namibe → Baía dos Tigres (opcional, avanzado) → Serra da Leba → Lubango/Tundavala", "El bloque de tramos 4x4 míticos del país: duna hasta el mar, puerto de montaña y fenda"),
        ("Subida · Costa y cierre", "Lubango → Lobito → Kissama → Luanda → Lufu/Luvo", "Vuelta a la capital y salida hacia RD Congo para continuar la subida"),
    ],
    offroad=[
        "Serra da Leba (EN280): el puerto de montaña más icónico de Angola, con curvas de herradura cerradas subiendo de ~720 m a 1.845 m entre Namibe y Lubango; asfaltado pero exigente, parada fotográfica obligada con los 4x4.",
        "Tundavala: pista de tierra de ~18 km desde Lubango hasta el borde de la fenda (2.200 m); terreno suelto en tramos, correa corta para el perro en el propio mirador por el desnivel de más de 1.000 m.",
        "Baía dos Tigres (avanzado, opcional): EL tramo mítico de 'duna que llega al mar' del sur de Angola, a través del paso de marea 'Doodsakker' desde Tombwa — solo con marea baja y luna llena o nueva, mínimo 2 vehículos y equipo de recuperación. Encaja exactamente con lo que buscamos para el bloque sur, pero exige preparación experta o guía local.",
        "Parque Nacional de Iona: pistas de arena y tierra por paisaje semidesértico sin señalización fija; jornada completa desde Namibe, GPX o guía recomendado.",
        "Tramo Malanje–Cazombo (bajada, no recreativo pero sí 4x4 real): más de 100 km de arena profunda y barro en temporada de lluvias, según relatos de otros overlanders; en temporada seca es un tramo largo pero asumible con 4x4 estándar.",
    ],
    acampada=[
        "Luanda: alojamientos con parking vigilado, opción más práctica que la acampada libre en la capital.",
        "Lobito: hoteles y alguna opción de camping costero con aparcamiento.",
        "Pedras Negras: vivac salvaje entre los bloques de granito, citado por otros overlanders como uno de los mejores del país; pedir permiso/avisar en el pueblo más cercano.",
        "Namibe y Lubango: hoteles con aparcamiento; base para las excursiones a Tundavala, Serra da Leba e Iona.",
        "Tramo de Moxico (bajada): acampada libre habitual, pero registrarse siempre en la policía local (práctica confirmada en Cazombo por otros viajeros) y pedir orientación a los ancianos del pueblo sobre el estado de la pista.",
    ],
    visado=[
        "Exención de visado de turismo (30 días) para pasaportes españoles a fecha de esta revisión; confirmar vigencia 30-60 días antes de viajar.",
        "Confirmar expresamente si la exención permite dos entradas (bajada y subida) dentro del mismo viaje o si hace falta gestionar el e-Visa de entrada múltiple con antelación.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Lufu/Luvo (RD Congo)", "Cruce del puente fronterizo; registro y sellado ~500 m dentro de Angola; desvío opcional a M'banza-Kongo cerca de aquí."),
        ("Salida bajada", "Caripande, cerca de Cazombo (Zambia)", "Paso remoto en Moxico; oficina angoleña muy precaria según otros overlanders, trámite en portugués; solo en temporada seca."),
        ("Entrada subida", "Santa Clara/Oshikango (Namibia)", "Paso más transitado hacia Namibia; carretera asfaltada e infraestructura de control moderna en ambos lados."),
        ("Alternativa entrada subida", "Calueque/Ruacana (Namibia)", "Más al oeste, junto a la presa de Calueque; pista sin asfaltar pero acceso directo a Ruacana, Epupa e Iona."),
        ("Salida subida", "Lufu/Luvo (RD Congo)", "Mismo paso que la entrada de la bajada, cerrando el corredor angoleño antes de continuar la subida hacia el norte."),
    ],
    vehiculos=[
        "CPD recomendado; confirmar si Angola exige también una importación temporal adicional del vehículo, dado que el país no pertenece a CEDEAO ni a CEMAC.",
        "Seguro de responsabilidad civil local obligatorio: contratarlo al entrar por Lufu/Luvo o Santa Clara si no se dispone de cobertura previa válida.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
        "Depósitos y garrafas de combustible/agua llenos antes de Malanje→Cazombo (bajada) y antes de Namibe→Baía dos Tigres/Iona (subida): son los dos tramos del país sin garantía de suministro.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa por escrito al INAVIC antes de intentar introducir el dron en el país.",
        "No volar cerca de instalaciones petroleras o portuarias (Luanda, Lobito), de la presa de Calueque, ni de zonas militares o de los parques nacionales sin autorización expresa.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado no confirmado a mediados de 2026 pese al anuncio de llegada dentro del año: revisar el mapa oficial 30-60 días antes.",
        "SIM local (Unitel, Africell) como conectividad principal en Luanda y el eje costero; no dar por hecha cobertura móvil en el tramo remoto de Moxico.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE).",
        "Ver la matriz por zona más abajo: los dos parques nacionales (Iona, Kissama) son la única duda seria pendiente de confirmar.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio, con mayor intensidad en el norte: profilaxis a valorar con Sanidad Exterior.",
        "Hospital Américo Boavida (Luanda) y Hospital Central da Huíla (Lubango) como referencias hospitalarias de cada corredor; seguro con evacuación médica imprescindible, sobre todo en el tramo remoto de Moxico.",
    ],
    seguridad_intro="País estable con precaución normal en todo el corredor previsto; el único factor a gestionar con cuidado es el aislamiento del tramo de Moxico (bajada) y la logística de mareas de Baía dos Tigres (subida), no la inseguridad.",
    seguridad=[
        "Sin zonas excluidas por seguridad en ninguno de los dos corredores previstos.",
        "Extremar la precaución documental en el cruce de Lufu/Luvo: primer país fuera de las zonas de seguro regional CEDEAO/CEMAC del tramo.",
        "Tramo de Moxico (bajada): aislamiento real más que inseguridad — llevar siempre combustible, agua y comida de reserva, y registrarse en la policía local como hacen otros overlanders.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
    ],
    agua=[
        "Luanda: agua embotellada en supermercados sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio y hoteles de Luanda, Lobito y Namibe permiten llenar el depósito con manguera; confirmar en recepción.",
        "Tramo de Moxico y Baía dos Tigres: sin garantía ninguna — salir con depósitos llenos al 100%.",
    ],
    combustible=[
        "Bajada: sin riesgo de gap de 500 km hasta Malanje (Lufu/Luvo → Luanda ~350 km → Malanje ~350 km, con estaciones formales en cada núcleo); a partir de Malanje hacia Cazombo la oferta se espacía mucho — depósitos llenos y garrafas de reserva.",
        "Subida: Santa Clara/Oshikango → Namibe (~300 km) con oferta razonable; sin garantía entre Namibe y Baía dos Tigres/Iona — llenar en Namibe. Namibe → Lubango (Serra da Leba) → Lobito → Luanda con estaciones formales en cada ciudad.",
    ],
    experiencias_intro="Relatos y comentarios reales de otros overlanders sobre Angola, para contrastar con la planificación oficial de esta ficha:",
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Visado de doble entrada", "Confirmar si la exención de 30 días cubre las dos pasadas (bajada y subida) o si hace falta e-Visa de entrada múltiple"),
        ("Frontera Caripande/Cazombo", "Confirmar horario, estado real de la pista y si el trámite acepta inglés o solo portugués, 30-60 días antes"),
        ("Perro en Iona y Kissama", "Contactar con African Parks (Iona) y el operador de Kissama para confirmar si el perro puede ir en el vehículo dentro del parque"),
        ("Baía dos Tigres", "Decidir si se intenta en solitario (2 vehículos + mareas) o se contrata apoyo local, y si encaja en el calendario del bloque sur"),
        ("M'banza-Kongo", "Decidir si el desvío UNESCO entra en el calendario del tramo centroafricano"),
        ("Seguro e importación del vehículo", "Confirmar el procedimiento exacto al entrar por Lufu/Luvo y por Santa Clara, fuera de CEDEAO/CEMAC"),
        ("Dron", "Contactar con el INAVIC o descartar el vuelo en el país"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 11 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Luanda): +244 929 900 900 · Embajada: +244 222 391 166.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

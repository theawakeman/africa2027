# -*- coding: utf-8 -*-
"""Sáhara Occidental — territorio de TRÁNSITO que se cruza dos veces, corredor doble (12 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

# Solo hay tres imágenes del territorio verificadas en Wikimedia Commons para esta revisión.
# Se reutilizan como IMAGEN DE REFERENCIA en los PDIs que aún no tienen foto propia, y así se
# dice expresamente en cada descripción. Ver "Fotos pendientes de sustituir" en decisiones.
IMG_AAIUN = W + "Laayoune%20Cathedral%202011.jpg?width=900"
IMG_DAKHLA = W + "FortecolorWestsaharaIII-36.jpg?width=900"
IMG_FRONTERA = W + "Guerguerat%20border%20crossing.jpg?width=900"

POIS = [
    # ===== BAJADA (enero 2027): Tarfaya -> El Aaiún -> Bojador -> Dajla -> Bir Gandouz -> Guerguerat =====
    dict(n=1, name="El Aaiún (Laayoune) · la mayor ciudad del territorio", cat="Ciudad · servicios", prio="Alta", dog="permitido", time="1 noche",
         lat=27.1500, lon=-13.2000,
         desc="262.000 habitantes y, de largo, la mayor ciudad del Sáhara Occidental: la fundó el capitán español Antonio de Oro en 1938 como puesto militar y explotó con el descubrimiento de los fosfatos de Bu Craa en los años cuarenta. Del periodo español quedan la CATEDRAL DE SAN FRANCISCO DE ASÍS, todavía en culto y con párroco, el trazado del barrio antiguo con sus cúpulas blancas y algún edificio de la administración; de la etapa marroquí, la enorme Plaza del Mechouar y la avenida de la Marcha Verde. Es sede de la MINURSO, la misión de la ONU para el referéndum, cuyos todoterrenos blancos se ven por la ciudad, y desde 2019 varios países han abierto consulados aquí. Para nosotros es lo que importa de verdad: última base con hospital de referencia, talleres, bancos, supermercado y combustible barato antes de 1.000 km de nada. Clima suavizado por la corriente de Canarias: media anual de unos 21 °C.",
         credit="Bjørn Christian Tørrissen · CC BY-SA 3.0", source=IMG_AAIUN),
    dict(n=2, name="Laayoune Plage y Foum el Oued · la desembocadura del Saguía", cat="Costa", prio="Media", dog="permitido", time="½ día",
         lat=27.1100, lon=-13.4200,
         desc="A unos 25 km al oeste de El Aaiún, donde el cauce seco de la Saguía el-Hamra alcanza el Atlántico: un pueblo de pescadores, una playa larguísima batida por el viento del norte, una zona de casetas y restaurantes de pescado, y la primera estación de servicio al salir de la ciudad. Es el mejor sitio para asomarse al Atlántico sahariano sin desviarse del corredor —el contraste entre la hamada ocre y el océano frío de la corriente de Canarias es el paisaje característico de todo el territorio— y también el punto donde muchos viajeros rompen el primer día de conducción. Con el perro, playa abierta sin problema; viento constante y arena en suspensión, conviene protegerle los ojos. Imagen de referencia de El Aaiún, no de la propia playa.",
         credit="Wikimedia Commons", source=IMG_AAIUN),
    dict(n=3, name="Bu Craa · la cinta transportadora más larga del mundo", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1–2 h (desde la carretera)",
         lat=26.3228, lon=-12.8497,
         desc="A un centenar de kilómetros al sureste de El Aaiún está la mina de fosfatos de Bu Craa, con un yacimiento de más de 1.700 millones de toneladas y en explotación desde 1972. Lo espectacular no es la mina sino su CINTA TRANSPORTADORA: unos 100 km de cinta continua que llevan el fosfato desde el desierto hasta el puerto de El Aaiún — la más larga del mundo, y cuya nube de polvo se ve literalmente desde el espacio en las fotos de satélite. Cruza el paisaje como una línea recta infinita sobre la hamada y es uno de los objetos hechos por el hombre más impresionantes del norte de África. Bu Craa es un pueblo-empresa habitado casi solo por empleados de Phosboucraa. ATENCIÓN: es infraestructura estratégica en territorio en disputa. Se mira desde la carretera de Smara y NO se fotografía la instalación ni el personal; nada de dron, nada de desvíos por pista. Imagen de referencia de El Aaiún, no de la propia mina.",
         credit="Wikimedia Commons", source=IMG_AAIUN),
    dict(n=4, name="Lemsid · la etapa intermedia", cat="Ciudad · servicios", prio="Baja", dog="permitido", time="parada técnica",
         lat=26.7200, lon=-13.6300,
         desc="Un puñado de edificios, una estación de servicio y un café a unos 100 km al sur de El Aaiún, en mitad de la nada. No hay nada que ver y es exactamente por eso por lo que está en esta ficha: en el corredor Laayoune-Dakhla los puntos de referencia son las gasolineras, y Lemsid es la primera después de Laayoune Plage y antes de Bojador. Repostar aquí aunque el depósito vaya por la mitad es la norma del tramo. Alrededor empieza el paisaje de HAMADA — llanura pedregosa sin una sola duna — que domina el interior del territorio y que explica por qué esto no es el Sáhara de postal sino algo mucho más austero. Imagen de referencia del territorio, no de la propia Lemsid.",
         credit="Wikimedia Commons", source=IMG_AAIUN),
    dict(n=5, name="Bojador (Boujdour) · el cabo que nadie se atrevía a doblar", cat="Costa", prio="Alta", dog="permitido", time="½ día",
         lat=26.1331, lon=-14.4669,
         desc="Durante siglos, el CABO BOJADOR fue el fin del mundo conocido para la navegación europea: las corrientes, la niebla y la leyenda del «mar tenebroso» del que no se volvía hicieron que ningún barco lo doblara hasta que Gil Eanes, enviado por el infante Enrique el Navegante, lo consiguió en 1434 — y con ello se abrió la ruta atlántica hacia el sur y, en última instancia, todo lo que vino después. Hoy es un pueblo de pescadores crecido alrededor de su faro, con un puerto artesanal muy activo (más de 1.700 barcas tradicionales censadas) y lonja. Merece la parada por lo que significa más que por lo que se ve: es el punto histórico de todo nuestro corredor atlántico. Es también la ÚLTIMA localidad con oferta amplia antes de los 290 km más vacíos del tramo. Imagen de referencia de la costa del territorio, no del propio cabo.",
         credit="Trincerone · CC BY-SA 4.0", source=IMG_DAKHLA),
    dict(n=6, name="La Duna Blanca (White Dune) y el brazo de la laguna", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=23.6000, lon=-15.8500,
         desc="El icono visual de Dajla: una duna de arena blanquísima que cae directamente sobre el agua turquesa y llana de la laguna, en la orilla continental, a unos 40 km al norte de la ciudad y a pie de la N1. Con la marea baja se puede caminar por el banco de arena hacia el interior de la laguna; con la marea alta, la duna parece flotar. Es la fotografía que todo el mundo se lleva del territorio y, al mismo tiempo, uno de los pocos sitios del corredor donde se puede parar, subir a pie a lo alto de la duna y tener una vista completa de la laguna de Dajla con el océano al otro lado de la península. Muy expuesto al viento, que aquí sopla del norte casi todo el año. Excelente para el perro: arena abierta, sin gestión ni tasa. COORDENADA APROXIMADA — el punto exacto de parada se ve desde la carretera. Imagen de referencia de la zona de Dajla, no de la propia duna.",
         credit="Trincerone · CC BY-SA 4.0", source=IMG_DAKHLA),
    dict(n=7, name="Laguna de Dajla (Dakhla Bay) · Ramsar y flamencos", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1–2 días",
         lat=23.6900, lon=-15.9500,
         desc="Unos 400 km² de bahía somera y 37 km de largo entre la península de Río de Oro y el continente: agua plana, azul turquesa y poco profunda, que es lo que la ha convertido en referencia mundial del kitesurf y a la vez en un humedal de primer orden. Está clasificada como Sitio de Interés Biológico y Ecológico (SIBE), Área Importante para la Conservación de las Aves (ZICO) y SITIO RAMSAR desde 2005. Flamencos rosados, espátulas, limícolas del Paleártico occidental invernando por millares, delfines mulares dentro de la bahía y bancos de ostras que se cultivan y se comen allí mismo, frescas, en las bateas de la orilla. La combinación de desierto, laguna, flamencos y kitesurf no existe en ningún otro punto de la ruta. Perro: correa en las zonas de aves — es humedal protegido y hay colonias sensibles.",
         credit="Trincerone · CC BY-SA 4.0", source=IMG_DAKHLA),
    dict(n=8, name="Dajla (Dakhla) · la antigua Villa Cisneros", cat="Ciudad · servicios", prio="Alta", dog="permitido", time="2–3 noches",
         lat=23.7167, lon=-15.9500,
         desc="La segunda ciudad del territorio (161.000 habitantes) al final de una península estrecha de 40 km que entra en el Atlántico: océano abierto a un lado, laguna a otro. La fundó España en 1884 como VILLA CISNEROS —el nombre lo puso por el cardenal Cisneros— y fue escala de los pilotos de la Aeropostal en los años veinte, en la misma ruta de Saint-Exupéry; España se retiró en 1976 y Marruecos tomó el control en 1979. Vive de la pesca y, cada vez más, del turismo deportivo: es el gran punto de encuentro de kitesurfistas, windsurfistas y overlanders del Atlántico africano, con campamentos a lo largo de la laguna, oferta de alojamiento razonable, talleres, bancos y el aeropuerto. Para nosotros es LA parada del territorio: el sitio donde descansar, revisar los vehículos y respirar antes o después de Guerguerat.",
         credit="Trincerone · CC BY-SA 4.0", source=IMG_DAKHLA),
    dict(n=9, name="Kitesurf, surf y los spots del Atlántico de Dajla", cat="Costa", prio="Alta", dog="permitido", time="1–3 días",
         lat=23.7300, lon=-15.9200,
         desc="El punto fuerte deportivo de todo el corredor atlántico. En la LAGUNA, agua plana y viento térmico del norte prácticamente garantizado de marzo a octubre (y muy frecuente el resto del año): es un sitio de aprendizaje excepcional, con escuelas en cadena a lo largo de la orilla y campamentos que alquilan material por días. En el lado del OCÉANO, al oeste de la península, hay olas de verdad: el spot de Foum Labouir, junto al faro, es el más conocido, con una derecha larga que funciona con el swell del noroeste, y hacia el norte aparecen varios picos de acceso por pista. No hace falta traer material: se alquila todo. Es, con diferencia, el mejor sitio de la ruta para meter dos o tres días de parada activa, y encaja mejor en la SUBIDA, cuando ya no hay prisa. Imagen de referencia de la zona de Dajla, no de un spot concreto.",
         credit="Trincerone · CC BY-SA 4.0", source=IMG_DAKHLA),
    dict(n=10, name="Bir Gandouz · la última parada antes de la frontera", cat="Ciudad · servicios", prio="Media", dog="permitido", time="parada técnica / 1 noche",
         lat=21.0170, lon=-16.3170,
         desc="Pueblo de carretera a unos 80 km de Guerguerat y último punto con estación de servicio fiable, café, algún alojamiento muy básico y cobertura razonable antes del paso a Mauritania. Mucha gente pernocta aquí para cruzar la frontera a primera hora de la mañana, que es exactamente lo que conviene hacer: el lado mauritano cierra por la tarde y los trámites pueden alargarse horas. El tramo Dajla–Bir Gandouz (~250 km) es el más largo sin repostaje garantizado de todo el bloque Marruecos/Sáhara: salir de Dajla con el depósito lleno y, si se puede, un bidón de reserva. Imagen de referencia del sur del territorio, no del propio Bir Gandouz.",
         credit="Wikimedia Commons", source=IMG_FRONTERA),
    dict(n=11, name="Guerguerat · el paso y la tierra de nadie", cat="Frontera", prio="Alta", dog="permitido con condiciones", time="4–6 h",
         lat=21.4261, lon=-16.9586,
         desc="Uno de los cruces más comentados de toda la ruta y el ÚNICO paso terrestre hacia Mauritania: está a unos 11 km de la frontera y a 5 del Atlántico, y es hoy la única carretera segura entre todo el norte de África y el África subsahariana, porque las alternativas del Sahel están cerradas por la situación de seguridad. El procedimiento tiene tres partes: control marroquí de salida (policía, aduana, escáner, cierre de la TVIP del vehículo), la TIERRA DE NADIE —unos kilómetros de pista sin asfaltar, con carcasas de coches, cambistas informales y ninguna autoridad— y el control mauritano, con varios edificios y trámites separados por nacionalidad. Calcular 4-6 horas y no llegar después de mediodía. Aquí hubo TENSIÓN MILITAR REAL: en noviembre de 2020 Marruecos intervino militarmente para desbloquear el paso, el Frente Polisario declaró roto el alto el fuego de 1991 y desde entonces la situación es de baja intensidad pero formalmente no resuelta. No fotografiar nada en todo el entorno.",
         credit="Wikimedia Commons", source=IMG_FRONTERA),
    # ===== SUBIDA (con más tiempo): Guerguerat -> Cintra -> Dajla (Imlili, Asmaa) -> Bojador -> El Aaiún -> Smara -> Tan-Tan =====
    dict(n=12, name="Bahía de Cintra (Golfo de Cintra)", cat="Naturaleza", prio="Media", dog="no aplicable (solo mirador desde la N1)", time="1–2 h",
         lat=22.9519, lon=-16.2156,
         desc="Una enorme bahía en forma de media luna a unos 120 km al sur de Dajla, de aguas muy someras —10 m de media en la parte central— y 29 millas náuticas de anchura, casi deshabitada salvo por asentamientos de pescadores dispersos. Es una zona de extraordinario valor natural: invernada de limícolas del Paleártico occidental y aves oceánicas, delfines mulares y jorobados, rorcuales, tortugas marinas que desovan en sus playas, y hábitat potencial de FOCA MONJE DEL MEDITERRÁNEO, aunque la colonia grande está más al sur, en Cabo Blanco. Marruecos llegó a estudiar declarar un parque nacional que abarcara Cintra y la bahía de Dajla. AVISO SERIO: la zona está descrita como muy remota, batida por tormentas de arena en primavera y AFECTADA POR MINAS en el entorno de Cabo Barbas, y no es apta para turismo. Para nosotros es un alto en la N1 y una mirada desde el asfalto: NO se baja a la bahía, NO se sale de la carretera.",
         credit="Trincerone · CC BY-SA 4.0", source=IMG_DAKHLA),
    dict(n=13, name="Sebja de Imlili · los peces del desierto", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=23.1500, lon=-15.8500,
         desc="Una de las rarezas naturales más asombrosas del norte de África y prácticamente desconocida: a unas decenas de kilómetros al sureste de Dajla, en plena depresión salina, hay un conjunto de cientos de pozas de agua hipersalina, algunas de pocos metros de diámetro, en las que viven poblaciones aisladas de TILAPIA — peces marinos atrapados ahí desde hace milenios, adaptados a una salinidad y una temperatura que deberían ser letales, y objeto de estudio científico internacional precisamente por eso. El paisaje es una llanura blanca agrietada con agujeros de agua verde. Se llega por pista desde la N1 con vehículo alto: es de los pocos desvíos de tierra que tienen sentido en este territorio, y aun así hay que hacerlo con guía local, sin alejarse de la traza marcada y nunca en solitario. COORDENADA APROXIMADA y acceso POR CONFIRMAR sobre el terreno en Dajla. Imagen de referencia del territorio, no de la propia sebja.",
         credit="Trincerone · CC BY-SA 4.0", source=IMG_DAKHLA),
    dict(n=14, name="Fuentes termales de Asmaa", cat="Naturaleza", prio="Media", dog="prohibido en las pozas", time="½ día",
         lat=23.8500, lon=-15.8000,
         desc="Manantiales de agua termal a unos 38 °C en pleno desierto, al norte de Dajla y cerca de la carretera de acceso a la península. Es un balneario muy modesto —piscinas de obra, vestuarios básicos, separación de horarios o espacios para hombres y mujeres— frecuentado sobre todo por los propios habitantes de Dajla, y no un spa: el interés está en el contraste absurdo de meterse en agua caliente rodeado de hamada y viento atlántico, y en que es uno de los poquísimos sitios del territorio donde se ve vida local no relacionada con la pesca o el turismo deportivo. Media jornada desde Dajla y encaja bien en la subida, cuando hay tiempo. Perro fuera de las pozas por respeto y por normativa local previsible. COORDENADA APROXIMADA. Imagen de referencia del territorio, no de las propias fuentes.",
         credit="Trincerone · CC BY-SA 4.0", source=IMG_DAKHLA),
    dict(n=15, name="Smara y la zawiya de Ma al-Aynayn", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=26.7394, lon=-11.6703,
         desc="La única ciudad del interior del territorio con una historia propia anterior a la colonización: fundada en 1869 como oasis de caravanas, se convirtió en 1902 en la capital espiritual del jeque MA AL-AYNAYN, que instaló aquí su zawiya, su biblioteca islámica y un centro de enseñanza religiosa que irradiaba sobre todo el Sáhara occidental. De aquella Smara queda la fortaleza de piedra de la ZAWIYA MAALAININ, que encierra una mezquita, en pleno centro urbano — la ciudad fue arrasada dos veces, por los franceses en 1913 y de nuevo en 1934 tras las rebeliones saharauis contra la ocupación española, así que lo que se visita son restos. Está a unos 240 km al este de El Aaiún, con carretera asfaltada y línea diaria de autobús (CTM, Supratours), y desde ahí hay ruta hacia Tan-Tan por el interior. Es el desvío que da sentido al corredor de subida: el único sitio del territorio que no es ni costa ni carretera. AVISO: Smara es de las localidades más próximas al muro de arena — no salir del asfalto en ningún caso. Imagen de referencia del territorio, no de la propia Smara.",
         credit="Wikimedia Commons", source=IMG_AAIUN),
    dict(n=16, name="Cabo Blanco y La Güera · la foca monje (NO accesible desde aquí)", cat="Naturaleza", prio="Baja", dog="no aplicable", time="no visitable en este tramo",
         lat=20.8333, lon=-17.0833,
         desc="Respuesta honesta a una pregunta que siempre sale: SÍ, la mayor colonia superviviente de FOCA MONJE DEL MEDITERRÁNEO del mundo —unos 270-300 ejemplares, la única que conserva estructura de colonia tras la mortandad de 1997 que mató a más de 200 animales en dos meses— está en la Côte des Phoques de Cabo Blanco, en la parte del cabo que corresponde al Sáhara Occidental. Pero NO se visita desde este corredor. Cabo Blanco está en la península de Ras Nuadibú, que la frontera parte en dos: el acceso real es por el lado MAURITANO, desde Nuadibú, ya pasada la frontera de Guerguerat, y la colonia está en una reserva estricta cuyo acceso está restringido precisamente para protegerla, con un plan de recuperación financiado por España. Al oeste está LA GÜERA, pueblo fantasma español fundado en 1920 por Francisco Bens, hoy sepultado por la arena y bajo control mauritano de facto. Planificar cualquier intento de ver focas en la ficha de MAURITANIA, no en ésta, y con operador autorizado. Imagen de referencia del sur del territorio.",
         credit="Wikimedia Commons", source=IMG_FRONTERA),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "naturaleza": "verde", "cultura": "morado",
              "costa": "turquesa", "patrimonio unesco": "marron", "frontera": "gris"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Entrada (bajada) · Tarfaya → Tah: sin frontera internacional", "Frontera", 27.9394, -12.9231,
     "NO hay frontera internacional al entrar: la administración marroquí es continua desde Tarfaya y el vehículo sigue con la misma TVIP obtenida en Tánger Med. Lo que sí empieza aquí es el régimen de CONTROLES DE GENDARMERÍA: a partir de Tah los puestos se suceden cada pocas decenas de kilómetros. Última localidad marroquí propiamente dicha: Tarfaya, con el museo de Saint-Exupéry y la Casa del Mar."),
    ("Salida (bajada) / Entrada (subida) · Guerguerat", "Frontera", 21.4261, -16.9586,
     "Único paso terrestre con Mauritania y único corredor viable norte-sur de toda África occidental. Control marroquí + tierra de nadie sin asfaltar + control mauritano: 4-6 h. eVisa mauritana OBLIGATORIA tramitada con antelación (ya no hay visado a la llegada). Llevar dírhams o euros en efectivo, no dólares. No fotografiar nada. Cruzar por la mañana. En la subida el sentido es el inverso y el control marroquí de ENTRADA es más minucioso que el de salida."),
    ("Salida (subida) · Smara → Tan-Tan o El Aaiún → Tarfaya", "Frontera", 27.9394, -12.9231,
     "Tampoco hay frontera al salir del territorio hacia Marruecos. La subida puede rematar por el interior (Smara → Tan-Tan, POR CONFIRMAR estado de la carretera y controles) o volviendo a la N1 costera por El Aaiún y Tarfaya. En ambos casos la continuidad administrativa es marroquí."),
    ("Hospital Regional Hassan II — El Aaiún", "Hospital", 27.1450, -13.1950,
     "Hospital de referencia del territorio. Cubre urgencias y cirugía básica, no politraumatismos graves: el seguro con evacuación médica es imprescindible en este tramo. La evacuación realista es a Agadir o Canarias. Coordenada urbana aproximada."),
    ("Hospital / centro de salud — Dajla", "Hospital", 23.6845, -15.9350,
     "Recurso sanitario urbano de Dajla, suficiente para lo básico. Para urgencias graves, evacuación a El Aaiún o Agadir — a 550 y 1.200 km. Coordenada urbana aproximada."),
    ("Consulado de España más próximo — Agadir (referencia)", "Consular", 30.4202, -9.5982,
     "Sin representación consular española en El Aaiún ni en Dajla: el consulado general de Agadir y la embajada en Rabat son las referencias operativas para todo el territorio, en las dos pasadas."),
    ("Combustible · Laayoune Plage", "Combustible", 27.1100, -13.4200,
     "Primera estación tras salir de El Aaiún, ~20 km al sur. Diésel subvencionado, sensiblemente más barato que en Marruecos: repostar aquí en las dos pasadas."),
    ("Combustible · Lemsid", "Combustible", 26.7200, -13.6300,
     "~80 km al sur de Laayoune Plage. Punto de repostaje intermedio confirmado por overlanders (Horizons Unlimited, iOverlander)."),
    ("Combustible · Bojador (Boujdour)", "Combustible", 26.1331, -14.4669,
     "~80 km al sur de Lemsid; última localidad con oferta amplia antes del tramo largo hacia Dajla. Repostar aquí siempre, aunque el depósito no esté a la mitad."),
    ("Combustible · cruce de Dajla (Dakhla Junction)", "Combustible", 23.7350, -15.8700,
     "~290 km al sur de Bojador; dos estaciones en la rotonda de acceso a la península, confirmadas y activas en iOverlander. El tramo previo no tiene nada intermedio salvo viento."),
    ("Combustible · Bir Gandouz", "Combustible", 21.0170, -16.3170,
     "Última estación fiable antes de Guerguerat (~80 km). El tramo Dajla-Bir Gandouz (~250 km) es el más largo sin repostaje garantizado de todo el bloque Marruecos/Sáhara: llegar con el depósito lleno desde Dajla."),
    ("Combustible · El Aaiún → Smara (corredor de subida)", "Combustible", 26.7394, -11.6703,
     "Eje interior de ~240 km con oferta escasa: repostar a fondo en El Aaiún y contar con que entre medias puede no haber nada fiable. POR CONFIRMAR sobre el terreno antes de tomar el desvío de Smara."),
    ("Agua potable y de uso general · El Aaiún y Dajla", "Agua potable", 23.6845, -15.9350,
     "Las dos únicas ciudades con suministro garantizado del territorio. Agua embotellada en supermercados; recarga del depósito de uso general en estaciones de servicio (Afriquia, Shell) y en los campamentos de la laguna de Dajla. Fuera de estas dos ciudades no dar por hecho NINGÚN punto de agua. El Aaiún tiene planta desaladora."),
    ("Zona de exclusión · muro de arena (berma) y franja este", "Servicio", 26.0000, -11.0000,
     "El muro marroquí recorre unos 2.700 km de sur a norte y está flanqueado por EL CAMPO DE MINAS CONTINUO MÁS LARGO DEL MUNDO, con minas colocadas en zigzag a un metro unas de otras y hasta tres filas en algunos tramos. Toda la franja este del territorio, y cualquier pista que se aleje del corredor asfaltado hacia el interior, queda EXCLUIDA SIN EXCEPCIÓN. Coordenada meramente indicativa de la zona a evitar, no un punto a visitar."),
]

DRONE_CALLOUT = ("danger", "El dron no entra: Marruecos lo confisca en la aduana y aquí, además, es zona sensible",
                  "DATO CRÍTICO Y MUY DOCUMENTADO: la práctica habitual de la aduana marroquí es CONFISCAR LOS DRONES A LA ENTRADA al país —en el puerto de Tánger Med, en los aeropuertos y en cualquier control— salvo autorización previa por escrito de la DGAC (Direction Générale de l'Aviation Civile). El equipo se precinta, se deposita y, en el mejor de los casos, se devuelve a la salida; en muchos relatos, no se devuelve. Como el Sáhara Occidental se recorre bajo administración marroquí y con la misma entrada aduanera, aquí aplica exactamente el mismo régimen, AGRAVADO por la sensibilidad territorial: infraestructura del muro/berma, instalaciones militares, la mina y la cinta de Bu Craa, el puerto de fosfatos de El Aaiún y todo el entorno del paso de Guerguerat. Norma del proyecto: el dron NO viaja en el tramo Marruecos/Sáhara Occidental salvo que el permiso escrito de la DGAC esté cerrado antes de embarcar en Algeciras. Un dron confiscado en Tánger Med en enero de 2027 estaría perdido para los ocho meses de viaje.")

STARLINK_CALLOUT = ("danger", "Mismo estado que Marruecos: sin licencia activa confirmada",
                     "El Sáhara Occidental comparte el marco regulatorio marroquí de telecomunicaciones. A fecha de esta revisión no consta servicio Starlink activo y licenciado: Marruecos figuraba como mercado «pendiente de aprobación regulatoria» y no se ha confirmado que la licencia haya llegado a activarse. Tratarlo como NO DISPONIBLE y no planificar dependencia. La cobertura móvil (Maroc Telecom, Orange, inwi) es buena en El Aaiún y Dajla y razonable a lo largo de la N1, pero se degrada mucho en el tramo Dajla-Guerguerat y en el desvío interior a Smara. Llevar mensajería satelital independiente (InReach/Zoleo o similar) ACTIVA para todo el territorio: es el tramo del viaje con mayor distancia entre núcleos habitados y donde una avería sin cobertura se convierte antes en un problema serio.")

DOG_MATRIX = [
    ("El Aaiún, Dajla y núcleos de la N1", "permitido",
     "Sin restricción específica publicada. Territorio bajo administración marroquí: aplican de facto los usos de Marruecos, donde el perro es tolerado en la calle pero no en interiores ni en muchos alojamientos. Reservar confirmando siempre. Atención a los perros asilvestrados de las afueras: Marruecos es el país de la ruta con mayor riesgo de mordedura de can callejero y hay rabia endémica — evitar contacto absolutamente."),
    ("Playas, duna blanca y orillas de la laguna", "permitido",
     "El mejor tramo del territorio para el perro: arena abierta, nadie alrededor y ninguna gestión de parque. Cuidado con el viento constante y la arena en suspensión (protección ocular) y con el calor del mediodía."),
    ("Laguna de Dajla · zonas de aves", "permitido con condiciones",
     "Es sitio Ramsar y área importante para las aves: correa corta en las zonas de flamencos y limícolas, y no acercarse a las concentraciones de aves. En las playas del lado océano, sin problema."),
    ("Fuentes termales de Asmaa", "prohibido en las pozas",
     "Instalación de baño frecuentada por población local, con separación por sexos: el perro se queda fuera con un miembro del grupo. Sombra escasa — dejarlo en el vehículo solo si hay ventilación real, o turnarse."),
    ("Sebja de Imlili y cualquier pista fuera del asfalto", "permitido con condiciones",
     "No hay norma que lo prohíba, pero sí el riesgo real: calor extremo, sal, cristales de yeso cortantes y la regla de oro del territorio de no separarse de la traza. Si se hace el desvío, con guía local, agua abundante y protección de almohadillas."),
    ("Paso de Guerguerat", "permitido con condiciones",
     "El perro viaja dentro del vehículo durante todo el trámite. Lo duro es la ESPERA: 4-6 horas, buena parte al sol y con el motor parado. Llevar agua abundante, toldo o sombra improvisada y no dejarlo solo en el coche cerrado en ningún momento. El control mauritano, ya al otro lado, puede pedir certificado sanitario: tenerlo a mano en francés."),
    ("Todo el territorio · asistencia veterinaria", "no aplicable",
     "NO HAY VETERINARIO FIABLE EN ~1.100 KM entre Agadir/Guelmim y Nuadibú. Es el tramo más desasistido de toda la primera parte del viaje para el perro. Botiquín canino completo, antiparasitario al día y un plan claro de qué se hace si pasa algo entre Bojador y Guerguerat."),
]

SOURCES = [
    ("Wikipedia · Western Sahara (estatus, geografía, población, minas)", "https://en.wikipedia.org/wiki/Western_Sahara"),
    ("Wikipedia · Guerguerat (coordenadas, incidentes de 2020-2021, papel del paso)", "https://en.wikipedia.org/wiki/Guerguerat"),
    ("Wikipedia · Moroccan Western Sahara Wall (berma, 2.700 km, campo de minas)", "https://en.wikipedia.org/wiki/Moroccan_Western_Sahara_Wall"),
    ("Wikipedia · Laayoune (El Aaiún)", "https://en.wikipedia.org/wiki/Laayoune"),
    ("Wikipedia · Dakhla, Western Sahara", "https://en.wikipedia.org/wiki/Dakhla,_Western_Sahara"),
    ("Wikipedia · Dakhla Bay (SIBE, ZICO, Ramsar 2005)", "https://en.wikipedia.org/wiki/Dakhla_Bay"),
    ("Wikipedia · Cintra Bay (fauna, minas de Cabo Barbas)", "https://en.wikipedia.org/wiki/Cintra_Bay"),
    ("Wikipedia · Boujdour y el cabo Bojador", "https://en.wikipedia.org/wiki/Boujdour"),
    ("Wikipedia · Bou Craa (mina de fosfatos y cinta transportadora)", "https://en.wikipedia.org/wiki/Bou_Craa"),
    ("Wikipedia · Smara (zawiya de Ma al-Aynayn)", "https://en.wikipedia.org/wiki/Smara"),
    ("Wikipedia · La Güera (pueblo fantasma español)", "https://en.wikipedia.org/wiki/La_G%C3%BCera"),
    ("Wikipedia · Mediterranean monk seal (colonia de Cabo Blanco)", "https://en.wikipedia.org/wiki/Mediterranean_monk_seal"),
    ("Wikipedia · Tarfaya (última localidad marroquí antes del territorio)", "https://en.wikipedia.org/wiki/Tarfaya"),
    ("Wikipedia · Khenifiss National Park (Ramsar, en Marruecos, antes de entrar)", "https://en.wikipedia.org/wiki/Khenifiss_National_Park"),
    ("United Nations · MINURSO, misión para el referéndum del Sáhara Occidental", "https://minurso.unmissions.org/"),
    ("Wikivoyage · Guerguerat", "https://en.wikivoyage.org/wiki/Guerguerat"),
    ("Mind of a Hitchhiker · cruce Dajla–Nuadibú a través de la berma", "https://mindofahitchhiker.com/through-the-berm-mauritania-border-crossing-with-western-sahara-morocco/"),
    ("Away with the Steiners · cruce Dajla–Nuadibú en vehículo propio", "https://awaywiththesteiners.com/morocco-mauritania-border-crossing/"),
    ("Spirit Travelers · cómo cruzar la frontera Marruecos–Mauritania", "https://spirit-travelers.com/en/how-to-cross-the-border-morocco-mauritania/"),
    ("MAEC España · recomendaciones de viaje (Marruecos, aplicable al tránsito)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Marruecos"),
    ("Sahara Overland · combustible en la Atlantic Highway (Laayoune-Dakhla-Guerguerat)", "https://sahara-overland.com/2020/04/03/a-if-for-atlantic-highway/"),
    ("Horizons Unlimited · gasolineras en el Sáhara Occidental (foro overlander)", "https://www.horizonsunlimited.com/hubb/morocco/fuel-stations-in-western-sahara-89474"),
    ("Starlink · mapa de disponibilidad", "https://starlink.com/map"),
    ("iOverlander · puntos de combustible, agua, acampada y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# BAJADA: Tarfaya -> El Aaiún -> Laayoune Plage -> Lemsid -> Bojador -> Duna Blanca -> Dajla -> Bir Gandouz -> Guerguerat
CORRIDOR = [(27.9394, -12.9231), (27.1500, -13.2000), (27.1100, -13.4200), (26.7200, -13.6300),
            (26.1331, -14.4669), (23.7350, -15.8700), (23.6000, -15.8500), (23.7167, -15.9500),
            (23.6900, -15.9500), (21.0170, -16.3170), (21.4261, -16.9586)]

# SUBIDA (con más tiempo): Guerguerat -> Bir Gandouz -> Cintra -> Imlili -> Dajla -> Asmaa -> Bojador -> El Aaiún -> Bu Craa -> Smara
CORRIDOR_ALT = [(21.4261, -16.9586), (21.0170, -16.3170), (22.9519, -16.2156), (23.1500, -15.8500),
                (23.7167, -15.9500), (23.8500, -15.8000), (26.1331, -14.4669), (26.7200, -13.6300),
                (27.1500, -13.2000), (26.3228, -12.8497), (26.7394, -11.6703), (27.9394, -12.9231)]

CORRIDOR_LABEL = "Bajada (enero 2027, tránsito rápido)"
CORRIDOR_ALT_LABEL = "Subida (con más tiempo: Cintra, Imlili, Asmaa y Smara)"

EXPERIENCIAS = [
    "LAS «FICHAS» DE LOS CONTROLES DE GENDARMERÍA: es el truco más útil y más repetido por los overlanders de este tramo. Desde Tah hasta Guerguerat hay controles de gendarmería cada pocas decenas de kilómetros —los viajeros hablan de entre diez y treinta en el conjunto del territorio— y en cada uno piden los mismos datos, a mano, en un cuaderno: nombre y apellidos, nacionalidad, número de pasaporte con fecha y lugar de expedición, fecha y lugar de nacimiento, NOMBRE DEL PADRE Y DE LA MADRE, profesión, dirección, matrícula, marca y modelo del vehículo, fecha de entrada en Marruecos, procedencia y destino del día. La solución que usa todo el mundo: llevar 30-50 FOTOCOPIAS IMPRESAS de una ficha con todos esos datos ya rellenados, una por viajero y vehículo, e ir entregando una en cada control. Se pasa de quince minutos de interrogatorio a treinta segundos. Imprimirlas en España antes de salir. Los gendarmes suelen ser correctos, a veces hasta amables, y no piden dinero — el problema es solo el tiempo.",
    "Combustible subvencionado: el gasóleo del Sáhara Occidental está subvencionado por la administración marroquí y es NOTABLEMENTE más barato que en el resto de Marruecos — los viajeros lo describen como una diferencia sustancial, no un matiz. La estrategia que recomiendan es entrar al territorio con el depósito lo más bajo que permita la prudencia y repostar ya dentro, y salir de Dajla con todo lleno más bidones para el tramo final. Confirmar el diferencial de precio al pasar: cambia con las políticas de subvención.",
    "El cruce de Guerguerat según quienes lo han hecho en vehículo propio: el lado marroquí es ordenado —policía, aduana, escáner del vehículo, cierre de la TVIP— y la tierra de nadie es lo que descoloca: unos kilómetros de pista sin asfaltar entre chatarra de coches abandonados, con cambistas informales que ofrecen ouguiyas y sin ninguna autoridad de por medio. El lado mauritano es más lento y desordenado, con varios edificios y trámites separados por nacionalidad, seguro obligatorio a contratar allí mismo y un nuevo permiso temporal de importación del vehículo. Consenso de todos los relatos: llegar por la mañana temprano, llevar efectivo en dírhams o euros (NO dólares), no fotografiar absolutamente nada y no perder la paciencia. 4-6 horas es lo normal.",
    "El viento es el protagonista del territorio. En Dajla sopla del norte casi todo el año y es lo que ha creado el fenómeno del kitesurf, pero para quien conduce significa consumo alto, arena en suspensión y la necesidad de sujetar todo lo que va en la baca. Varios viajeros advierten de que las tormentas de arena de primavera pueden reducir la visibilidad a casi nada en la N1 y que lo sensato es parar y esperar, no seguir.",
    "Sobre la seguridad real: los overlanders describen el corredor costero como tranquilo y sin incidentes, con presencia constante de gendarmería y militares. El riesgo no es la delincuencia, es el aislamiento: 290 km entre Bojador y Dajla y 250 entre Dajla y Bir Gandouz sin nada. La recomendación unánime es no conducir de noche —hay camiones y dromedarios sueltos— y no salir de la carretera bajo ningún concepto por el asunto de las minas.",
    "Acampada: las explanadas junto a la laguna de Dajla y los campamentos de kitesurf son el punto de encuentro clásico de los overlanders del Atlántico; muchos se quedan más días de los previstos. Entre El Aaiún y Dajla, en cambio, los relatos coinciden en no pernoctar fuera de núcleos: la gendarmería puede pedirte que te muevas y, además, no hay ninguna razón para hacerlo.",
    "El nombre de las cosas: en la práctica los carteles, mapas y funcionarios usan la toponimia marroquí (Laayoune, Dakhla, Boujdour) y los viajeros españoles siguen usando la española (El Aaiún, Villa Cisneros, Bojador). Ninguna de las dos es neutral. El consejo repetido por quienes han pasado es evitar por completo el tema político en conversación: es materia sensible en todo Marruecos y aquí especialmente.",
]

HISTORIA_RESUMEN = ("El Sáhara Occidental es el último gran contencioso de descolonización pendiente en África: territorio nómada saharaui bajo dominio español hasta 1975, fue ocupado por Marruecos tras la retirada de España en plena Marcha Verde, "
                     "lo que desencadenó una guerra con el Frente Polisario y un exilio saharaui a Argelia que se prolonga hasta hoy, con un referéndum de autodeterminación prometido por la ONU en 1991 y jamás celebrado.")

HISTORIA_SECCIONES = [
    ("Pueblo nómada saharaui y el Sáhara español",
     "El territorio estuvo habitado tradicionalmente por tribus nómadas saharauis de origen árabe-bereber, organizadas en torno al pastoreo de camellos y a las rutas comerciales transaharianas; su centro espiritual fue Smara, la capital religiosa que el jeque Ma al-Aynayn levantó en 1902. España estableció su colonia del Sáhara Español en 1884 —Villa Cisneros, hoy Dajla, es de ese año— y la gestionó durante casi un siglo como una posesión marginal, hasta el descubrimiento de los enormes yacimientos de fosfatos de Bu Craa en los años sesenta, que lo cambiaron todo."),
    ("La retirada española y la Marcha Verde de 1975",
     "Ante la presión internacional por la descolonización y la debilidad del régimen franquista en sus últimos meses, España acordó en los Acuerdos de Madrid de 1975 ceder la administración del territorio a Marruecos y Mauritania, tras la masiva Marcha Verde marroquí; España se retiró sin celebrar el referéndum de autodeterminación que había prometido, dejando al pueblo saharaui sin ser consultado. Jurídicamente, España sigue figurando ante la ONU como potencia administradora de iure."),
    ("La guerra, el muro y la partición del territorio",
     "El Frente Polisario proclamó la República Árabe Saharaui Democrática y libró una guerra contra Marruecos y Mauritania; esta última se retiró del conflicto en 1979 y Marruecos ocupó también su parte. Entre 1980 y 1987, en seis fases, Marruecos construyó un muro de arena y piedra de unos 2.700 km —la «berma»— con trincheras, radares y bases cada cinco kilómetros, flanqueado por el campo de minas continuo más largo del mundo. El muro separa el ~70 % del territorio bajo control marroquí, donde transcurre el corredor costero de esta ruta, del ~30 % oriental bajo control del Polisario."),
    ("Situación actual: alto el fuego roto y estatus sin resolver",
     "Desde 1991 rigió un alto el fuego supervisado por la MINURSO, pero el referéndum nunca se celebró por el desacuerdo sobre el censo de votantes. En noviembre de 2020, una crisis en la zona de Guerguerat llevó a Marruecos a intervenir militarmente para desbloquear el paso y al Frente Polisario a declarar roto el alto el fuego; desde entonces hay enfrentamientos esporádicos de baja intensidad a lo largo del muro. Decenas de miles de refugiados saharauis siguen viviendo en campamentos en Tinduf (Argelia) y la comunidad internacional permanece dividida. Esta ficha usa en cada caso el topónimo que corresponde y no toma partido: es una herramienta de planificación, no una posición política."),
]

HISTORIA_FUENTES = [
    ("BBC News · Western Sahara profile", "https://www.bbc.com/news/world-africa-14115273"),
    ("United Nations · MINURSO", "https://minurso.unmissions.org/"),
    ("Wikipedia · Western Sahara", "https://en.wikipedia.org/wiki/Western_Sahara"),
    ("Encyclopaedia Britannica · Western Sahara", "https://www.britannica.com/place/Western-Sahara"),
]

SPEC = dict(
    slug="sahara-occidental", name="Sáhara Occidental (tránsito)", revision="12 sep 2026",
    sub="Territorio de tránsito · se cruza dos veces · corredor doble bajada/subida",
    chips=[
        ("ROL EN LA RUTA", "TRÁNSITO · se cruza DOS VECES, a la ida y a la vuelta"),
        ("BAJADA", "Tarfaya → El Aaiún → Bojador → Dajla → Bir Gandouz → Guerguerat · ~1.100 km"),
        ("SUBIDA", "Guerguerat → Cintra → Dajla (Imlili, Asmaa) → El Aaiún → Smara → Tan-Tan · ~1.500 km"),
        ("PDIs", "16 puntos repartidos entre los dos corredores"),
        ("ESTATUS", "territorio no autónomo · administración marroquí de facto en el corredor · MINURSO"),
        ("FRONTERA", "Guerguerat: único paso terrestre con Mauritania, 4-6 h"),
        ("VISADO", "cubierto por la entrada marroquí · eVisa MAURITANA previa obligatoria"),
        ("MINAS", "franja este y entorno del muro: EXCLUIDOS SIN EXCEPCIÓN"),
        ("DRON", "Marruecos lo confisca en aduana: NO viaja en este tramo"),
        ("COMBUSTIBLE", "subvencionado y barato · pero 290 y 250 km entre estaciones"),
        ("PERRO", "sin trámite propio · pero SIN VETERINARIO en ~1.100 km"),
    ],
    center=[24.5, -14.5], zoom=6,
    notice="Territorio no autónomo según Naciones Unidas, bajo administración marroquí de facto en el corredor por el que discurre esta ruta. Esta ficha describe el tránsito por la N1 y un desvío interior a Smara; no toma posición sobre el contencioso ni sobre la toponimia. Revalidar fronteras, seguridad y comunicaciones 30-60 días antes de cada una de las dos pasadas.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    hero_img=IMG_DAKHLA,
    hero_credit="Costa del Sáhara Occidental, zona de Dajla · Trincerone · CC BY-SA 4.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("El Sáhara Occidental se cruza <strong>dos veces</strong>, al principio y al final del viaje, y las dos veces por el mismo eje: no hay alternativa, porque solo hay una carretera —la N1 atlántica— y un único paso terrestre con Mauritania, el de <strong>Guerguerat</strong>. "
                   "Lo que sí cambia entre una pasada y otra es el TIEMPO. En la <strong>bajada</strong>, en enero de 2027, esto es puro tránsito: 1.100 km de Tarfaya a Guerguerat en dos o tres días, con El Aaiún y Dajla como únicas bases y el objetivo de llegar a la frontera con el depósito lleno y por la mañana. "
                   "En la <strong>subida</strong>, ya sin calendario por delante, el mismo eje se puede hacer despacio y abrirlo a lo que no se hizo a la ida: la bahía de Cintra, la sebja de Imlili con sus peces atrapados en el desierto, las fuentes termales de Asmaa, dos o tres días de kitesurf en la laguna de Dajla, y el único desvío interior que tiene sentido, el de <strong>Smara</strong> y la zawiya de Ma al-Aynayn. "
                   "Dos cosas condicionan todo lo demás y no son negociables: <strong>las minas</strong> —la franja este del territorio y el entorno del muro tienen el campo de minas continuo más largo del mundo, así que no se sale del asfalto— y <strong>el aislamiento</strong>: 290 km entre Bojador y Dajla, 250 entre Dajla y Bir Gandouz, y ningún veterinario en 1.100 km."),
    decision=("Cambio respecto a versiones anteriores de esta ficha: el Sáhara Occidental deja de tratarse como un tramo único de bajada y pasa a tener <strong>corredor doble</strong>, porque se cruza dos veces. "
              "La bajada se mantiene como tránsito rápido (2-3 días) y la subida incorpora las paradas que a la ida no caben: <strong>Cintra, Imlili, Asmaa, los spots de Dajla y el desvío interior a Smara</strong>. "
              "La decisión abierta es si la subida remata por <strong>Smara → Tan-Tan</strong> (interior, distinto de la ida, pero con estado de carretera y controles POR CONFIRMAR) o vuelve a la N1 costera por El Aaiún y Tarfaya, repitiendo tramo."),
    facts=[
        ("Rol en la ruta", "Territorio de TRÁNSITO que se cruza dos veces: enero de 2027 hacia el sur y, meses después, de vuelta hacia el norte. No hay ruta alternativa: una sola carretera y un solo paso fronterizo."),
        ("Estatus", "Territorio no autónomo según Naciones Unidas, sin resolución definitiva. Marruecos administra de facto ~70 % del territorio, incluido todo el corredor de esta ruta; el Frente Polisario controla la franja este, al otro lado del muro. España sigue figurando como potencia administradora de iure. MINURSO supervisa desde 1991."),
        ("Entrada (bajada)", "Continuidad terrestre desde Tarfaya (Marruecos): NO hay control internacional. Lo que empieza es el régimen de controles de gendarmería, constantes en todo el territorio."),
        ("Salida (bajada)", "Guerguerat hacia Nuadibú (Mauritania): 4-6 horas, dos controles y una franja de tierra de nadie sin asfaltar. Único paso terrestre y única vía viable norte-sur de África occidental."),
        ("Subida", "Mismo eje al revés, con más tiempo: Cintra, Imlili, Asmaa, kitesurf en Dajla y el desvío interior a Smara. Salida hacia Marruecos por Tan-Tan (POR CONFIRMAR) o por Tarfaya."),
        ("Visado", "Sin trámite propio: cubierto por la exención marroquí de 90 días. Para Mauritania, eVisa OBLIGATORIA tramitada con antelación en ambas pasadas — ya no hay visado a la llegada en Guerguerat."),
        ("Vehículos", "La TVIP marroquí obtenida en Tánger Med cubre todo el territorio; comprobar que la salida queda registrada en Guerguerat. En la subida se obtiene una TVIP nueva al reentrar desde Mauritania."),
        ("Seguridad", "Corredor tranquilo y con fuerte presencia policial y militar. El riesgo real no es la delincuencia: son las MINAS fuera del asfalto, el aislamiento y la conducción."),
        ("Combustible", "Subvencionado y notablemente más barato que en Marruecos, pero con dos tramos largos sin garantía: Bojador→Dajla (290 km) y Dajla→Bir Gandouz (250 km)."),
        ("Comunicaciones", "Buena cobertura móvil en El Aaiún y Dajla, razonable en la N1, mala en el tramo final y en el desvío a Smara. Starlink sin licencia confirmada: mensajería satelital independiente obligatoria."),
        ("Perro", "Sin trámite propio (administración marroquí continua), pero es el tramo más desasistido del viaje: ningún veterinario fiable en ~1.100 km, calor extremo y rabia endémica en perros asilvestrados."),
    ],
    alerts=[
        "MINAS TERRESTRES — la alerta número uno y no admite matices. El muro marroquí recorre 2.700 km flanqueado por el CAMPO DE MINAS CONTINUO MÁS LARGO DEL MUNDO, con minas colocadas en zigzag a un metro unas de otras y hasta tres filas en algunos tramos. Hay además minas documentadas fuera del entorno del muro, por ejemplo en la zona de Cabo Barbas, junto a la bahía de Cintra. Regla absoluta del proyecto: NO SE ABANDONA EL ASFALTO NI LA PISTA BALIZADA en ningún punto del territorio, ni para acampar, ni para una foto, ni para un atajo. El único desvío de tierra contemplado (Imlili) se hace con guía local y por traza marcada.",
        "DRON: Marruecos CONFISCA los drones en la aduana de entrada sin autorización previa por escrito de la DGAC, y en el Sáhara Occidental la sensibilidad es aún mayor (muro, instalaciones militares, mina y cinta de Bu Craa, puerto de fosfatos, paso de Guerguerat). El dron no viaja en este tramo salvo permiso cerrado antes de embarcar en Algeciras.",
        "Guerguerat: la eVisa mauritana debe estar tramitada ANTES de llegar, en las DOS pasadas — ya no existe visado a la llegada. Llevar dírhams o euros en efectivo (no dólares). No fotografiar nada en todo el entorno del paso. Cruzar por la mañana: el lado mauritano cierra por la tarde.",
        "Guerguerat tuvo TENSIÓN MILITAR REAL en noviembre de 2020: Marruecos intervino para desbloquear el paso y el Frente Polisario declaró roto el alto el fuego de 1991, que sigue formalmente roto. La situación es de baja intensidad y el paso funciona con normalidad, pero es un punto a revalidar 72 h antes de cada cruce, no un trámite rutinario.",
        "CONTROLES DE GENDARMERÍA constantes en todo el territorio, con petición de datos personales completos en cada uno (incluidos los nombres del padre y de la madre). Llevar 30-50 fichas impresas ya rellenadas, una por viajero y vehículo: convierte un control de quince minutos en uno de treinta segundos. Ver la sección de experiencias.",
        "Combustible: los dos tramos largos (Bojador→Dajla, 290 km, y Dajla→Bir Gandouz, 250 km) no tienen nada fiable entre medias. Salir siempre lleno y llevar bidón de reserva.",
        "Golpe de calor y tormentas de arena: veranos de 43-45 °C en el interior, viento del norte constante y tormentas de arena sobre todo en primavera, capaces de reducir la visibilidad a casi nada en la N1. Si ocurre, parar y esperar.",
        "Toponimia y conversación: el territorio es materia políticamente sensible en todo Marruecos. Esta ficha usa los dos nombres cuando corresponde, pero sobre el terreno lo prudente es no entrar en el tema con nadie, ni con funcionarios ni con particulares.",
        "Sin consulado español en el territorio: la referencia es Agadir o la embajada en Rabat. En caso de accidente grave, la evacuación realista es a Agadir o a Canarias — seguro con evacuación médica imprescindible.",
    ],
    ruta_intro=("Un solo eje, la <strong>N1 atlántica</strong>, recorrido dos veces en sentidos opuestos. La <strong>bajada</strong> (enero de 2027) es tránsito puro: ~1.100 km de Tarfaya a Guerguerat en 2-3 días, con paradas funcionales en El Aaiún y Dajla y una sola parada de gusto, la Duna Blanca. "
                "La <strong>subida</strong> recorre lo mismo al revés pero abre el tiempo: se añaden la bahía de Cintra, la sebja de Imlili, las fuentes de Asmaa, dos o tres días de kitesurf en la laguna de Dajla y el desvío interior a Smara, lo que la lleva a ~1.500 km y 6-9 días. "
                "Etapas calculadas sobre una media de <strong>250 km/día</strong>, que aquí es realista porque la carretera es buena y recta; lo que la rompe son los controles y el viento."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bajada 1 · Entrada y base del norte", "Tarfaya → Tah → El Aaiún (Laayoune Plage)", "~110 km · 1 día · repostar, provisiones, revisión de vehículos"),
        ("Bajada 2 · El corredor vacío", "El Aaiún → Lemsid → Bojador", "~180 km · 1 día · repostar en cada estación aunque no haga falta"),
        ("Bajada 3 · El tramo largo", "Bojador → Duna Blanca → cruce de Dajla → Dajla", "~330 km · 1 día · 290 km sin nada entre Bojador y el cruce"),
        ("Bajada 4 · Descanso en la península", "Dajla (laguna, ciudad, revisión)", "1-2 días · última base real antes de Mauritania"),
        ("Bajada 5 · Tramo crítico final", "Dajla → Bir Gandouz", "~250 km · 1 día · el más largo sin repostaje garantizado; pernoctar aquí"),
        ("Bajada 6 · La frontera", "Bir Gandouz → Guerguerat → Nuadibú (Mauritania)", "~80 km + 4-6 h de trámite · reservar la mañana completa"),
        ("Subida 1 · Reentrada", "Guerguerat → Bir Gandouz", "~80 km + trámite · TVIP marroquí nueva; control de entrada más minucioso"),
        ("Subida 2 · La bahía remota", "Bir Gandouz → mirador de la bahía de Cintra", "~130 km · 1 día · SOLO desde la N1, zona con minas en Cabo Barbas"),
        ("Subida 3 · Rarezas del desierto", "Cintra → sebja de Imlili → Dajla", "~130 km · 1-2 días · Imlili con guía local, acceso POR CONFIRMAR"),
        ("Subida 4 · Parada activa", "Dajla: kitesurf y surf en la laguna y en Foum Labouir · fuentes de Asmaa", "2-3 días · el bloque deportivo del viaje en el Atlántico"),
        ("Subida 5 · Subir la costa", "Dajla → Bojador (cabo y faro) → Lemsid → El Aaiún", "~510 km · 2-3 días"),
        ("Subida 6 · El interior", "El Aaiún → cinta de Bu Craa (desde la carretera) → Smara (zawiya)", "~240 km · 1-2 días · el único desvío interior del territorio"),
        ("Subida 7 · Salida a Marruecos", "Smara → Tan-Tan (POR CONFIRMAR) o regreso a El Aaiún → Tarfaya", "~250-340 km · 1-2 días · sin frontera internacional"),
    ],
    offroad=[
        "REGLA MAESTRA DEL TERRITORIO: aquí NO se hace off-road. Es el único país o territorio de toda la ruta donde el proyecto renuncia expresamente a las pistas, y la razón es una sola: el campo de minas continuo más largo del mundo flanquea el muro, hay minas documentadas fuera del muro (Cabo Barbas, junto a la bahía de Cintra) y no existe cartografía fiable de las zonas limpias. Ninguna duna, ninguna playa y ningún atajo compensan eso.",
        "Única excepción contemplada: la pista de acceso a la SEBJA DE IMLILI desde la N1, al sureste de Dajla, y solo con guía local de Dajla, por la traza marcada, con los dos vehículos juntos y avisando de la hora de regreso. Acceso y estado POR CONFIRMAR sobre el terreno.",
        "Accesos a los spots de surf del lado océano de la península de Dajla: pistas cortas de arena y grava entre la N1 de la península y los picos del norte (Foum Labouir y alrededores). Zona urbanizada y transitada, sin riesgo de minas, pero con arena blanda: bajar presión y no ir solo.",
        "Explanadas de la laguna de Dajla: son terreno llano y muy usado por campamentos de kitesurf y overlanders, con acceso rodado normal. No es off-road, pero sí el único sitio del territorio donde se sale del asfalto con tranquilidad.",
        "Lo que NO se hace, por mucho que aparezca en blogs o en tracks descargados: el erg Lakhbayta y las zonas de dunas del interior, cualquier pista hacia el este desde la N1, la bajada a la bahía de Cintra, la costa de los naufragios al norte de Dajla y cualquier traza hacia Aousserd o hacia el muro. Si un track GPS invita a ello, se ignora.",
        "Conducción: la N1 está asfaltada y en buen estado en todo el corredor, con tramos rectos larguísimos. Los riesgos reales son el viento lateral, los camiones pesados hacia Mauritania, los dromedarios sueltos y la fatiga por monotonía. Norma del proyecto: no conducir de noche en ningún punto del territorio.",
    ],
    senderismo=[
        "DUNA BLANCA (White Dune), laguna de Dajla: subida corta y empinada por arena blanda hasta lo alto de la duna, veinte minutos, con la laguna entera a un lado y la hamada al otro. Con la marea baja se puede caminar además por el banco de arena hacia el interior de la laguna. Es la caminata más fotogénica del territorio y se hace con el perro.",
        "PLAYA DE FOUM EL OUED y la desembocadura de la Saguía el-Hamra: paseo largo y llano por la playa desde el pueblo de pescadores, con el viento del norte de cara y el contraste entre el cauce seco y el océano. Sin sombra: al amanecer o al atardecer.",
        "ORILLA DE LA LAGUNA DE DAJLA: recorridos llanos de varios kilómetros por la orilla interior, entre bateas de ostras, grupos de flamencos y campamentos de kitesurf. Es más observación de aves que senderismo, y es la mejor manera de entender el humedal. Prismáticos y correa corta en las zonas de aves.",
        "CABO BOJADOR: paseo corto desde el pueblo hasta el faro y el borde del acantilado, con el puerto pesquero a un lado. No tiene dificultad ninguna y sí una carga histórica enorme: es el cabo que cerró el Atlántico a la navegación europea hasta 1434.",
        "SEBJA DE IMLILI: recorrido a pie de una o dos horas entre las pozas de la llanura salina, con guía. Terreno llano pero con costra de sal y cristales de yeso cortantes: calzado cerrado y, para el perro, cuidado con las almohadillas.",
        "SMARA, zawiya de Ma al-Aynayn: vuelta a pie por los restos de la fortaleza de piedra y la mezquita, y por el centro de la ciudad. Una hora larga, llana, y la única visita cultural a pie del territorio.",
        "NO SE CAMINA fuera de trazas conocidas en ningún punto del territorio, y muy especialmente en el interior, en el entorno de la bahía de Cintra y en cualquier dirección hacia el este. Esta lista es exhaustiva a propósito.",
    ],
    acampada=[
        "Explanadas y campamentos de la laguna de Dajla: el punto de encuentro clásico de overlanders y kitesurfistas del Atlántico africano, con campamentos que aceptan vehículos, tienen agua, ducha y taller improvisado. Es la mejor pernocta del territorio en las dos pasadas y el sitio donde tiene sentido quedarse días en la subida.",
        "El Aaiún y Dajla: hoteles y campings urbanos con aparcamiento cerrado; lo razonable en la bajada, cuando lo que se busca es dormir y seguir.",
        "Bir Gandouz: alojamiento muy básico y explanada junto a la estación de servicio. Se pernocta aquí por una sola razón: cruzar Guerguerat a primera hora de la mañana. Merece la pena.",
        "Tramo El Aaiún–Dajla: NO pernoctar fuera de núcleos. Distancias largas, sin servicios, sin vigilancia, y la gendarmería puede pedir que te muevas. No hay ninguna ventaja en hacerlo.",
        "Acampada libre en general: descartada en todo el territorio salvo en el entorno inmediato de la laguna de Dajla y los campamentos establecidos, y por la misma razón de siempre — no se sale del asfalto ni de las trazas usadas.",
    ],
    visado=[
        "Sin trámite propio para el territorio: la exención marroquí de 90 días para pasaporte español cubre todo el corredor, en la bajada y en la subida, porque la administración es continua desde Tarfaya.",
        "MAURITANIA: eVisa OBLIGATORIA tramitada con antelación, en LAS DOS PASADAS. Desde 2025 no existe visado a la llegada en Guerguerat. Llevar la aprobación impresa y en digital, y tramitarla con margen: es el trámite que puede dejar el viaje parado en la frontera.",
        "Al reentrar desde Mauritania en la subida, se vuelve a entrar en el régimen marroquí: comprobar que la exención de 90 días se aplica de nuevo y que el sello de entrada queda correctamente puesto.",
        "Pasaporte con vigencia holgada (más de seis meses) y páginas libres: el territorio se atraviesa dos veces y Marruecos-Mauritania suman cuatro sellos.",
        "Certificado internacional de fiebre amarilla: no exigido para entrar aquí, pero sí puede pedirse más al sur — llevarlo siempre accesible desde el inicio.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Tarfaya → Tah (continuidad terrestre)", "NO es frontera internacional: la administración marroquí es continua. Empieza aquí el régimen de controles de gendarmería con petición de datos personales completos."),
        ("Salida bajada", "Guerguerat (hacia Nuadibú, Mauritania)", "Control marroquí de salida (policía, aduana, escáner, cierre de la TVIP) + ~3-5 km de tierra de nadie sin asfaltar + control mauritano por nacionalidades, con seguro local y permiso temporal del vehículo. 4-6 h en total. eVisa mauritana previa obligatoria. Efectivo en dírhams o euros. No fotografiar."),
        ("Entrada subida", "Guerguerat (desde Nuadibú)", "Mismo paso en sentido inverso. El control marroquí de ENTRADA es más minucioso que el de salida: escáner del vehículo, registro y nueva TVIP. Prever también aquí media jornada y cruzar por la mañana."),
        ("Salida subida (opción interior)", "Smara → Tan-Tan (sin frontera internacional)", "Ruta interior que evita repetir el eje costero. POR CONFIRMAR: estado real de la carretera, controles y si hay combustible fiable en el trayecto. Es la pieza que haría del corredor de subida algo distinto del de bajada."),
        ("Salida subida (opción costera)", "El Aaiún → Tarfaya (sin frontera internacional)", "Regreso por la N1, repitiendo tramo. Plan seguro si Smara-Tan-Tan no resulta practicable."),
    ],
    vehiculos=[
        "TVIP (tarjeta blanca de admisión temporal, D16ter) obtenida en Tánger Med: cubre todo el territorio en la bajada. COMPROBAR que la salida queda registrada en Guerguerat — si no consta, el vehículo figura como no salido de Marruecos y eso es un problema serio en la subida.",
        "En la subida se emite una TVIP NUEVA al reentrar desde Mauritania por Guerguerat. Mismo vehículo, mismo bastidor, mismos papeles: llevar copia del permiso de circulación, ficha técnica y autorización del titular si el vehículo no está a nombre del conductor.",
        "En el lado mauritano se emite permiso de importación temporal (mínimo 10 días) y se contrata seguro local en el propio paso, en ambos sentidos. No hay carte brune ni seguro regional válido aquí: la CEDEAO empieza más al sur.",
        "CONTROLES DE GENDARMERÍA: constantes en todo el territorio, con petición de datos personales y del vehículo en cada uno. Llevar 30-50 fichas impresas ya rellenadas con nombre, apellidos, nacionalidad, número y datos del pasaporte, fecha y lugar de nacimiento, NOMBRE DEL PADRE Y DE LA MADRE, profesión, dirección, matrícula, marca y modelo del vehículo, fecha de entrada en Marruecos y destino. Es el truco que más tiempo ahorra de todo el tramo.",
        "Combustible con margen: repostar en cada una de las cinco estaciones del corredor (Laayoune Plage, Lemsid, Bojador, cruce de Dajla, Bir Gandouz) aunque el depósito no lo pida. Bidón de reserva lleno antes del tramo final.",
        "Repuestos y taller: El Aaiún y Dajla tienen talleres de carretera capaces de lo básico (neumáticos, soldadura, amortiguadores). Cualquier cosa específica de Grenadier o Delica, ni pensarlo: lo que falle aquí se arregla de forma provisional y se repara bien en Agadir o ya en Nuakchot.",
        "Norma del proyecto: no conducir de noche en ningún punto del territorio — camiones, dromedarios sueltos y fatiga por monotonía.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Marruecos confisca los drones en la aduana de entrada sin autorización previa por escrito de la DGAC. Es una práctica habitual y ampliamente documentada, y aplica en el puerto de Tánger Med, que es por donde entra la expedición.",
        "En el Sáhara Occidental la sensibilidad es aún mayor por la disputa territorial: prohibido de facto cerca del muro/berma, de instalaciones militares, de la mina y la cinta transportadora de Bu Craa, del puerto de fosfatos de El Aaiún y de todo el entorno del paso de Guerguerat.",
        "NORMA DEL PROYECTO: el dron NO viaja en el tramo Marruecos/Sáhara Occidental. O se deja en España, o se tramita y se cierra la autorización escrita de la DGAC antes de embarcar en Algeciras. Un dron confiscado en enero de 2027 estaría perdido para los ocho meses de viaje.",
        "Tampoco fotografiar con cámara convencional instalaciones militares, el muro, el puerto, la cinta de Bu Craa ni el entorno de los pasos fronterizos y de los controles de gendarmería.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Sin servicio activo ni licencia confirmada a fecha de esta revisión: tratar como NO DISPONIBLE y no planificar dependencia en ninguna de las dos pasadas.",
        "SIM local marroquí (Maroc Telecom, Orange, inwi) como conectividad principal: cobertura buena en El Aaiún y Dajla, razonable en la N1, mala en el tramo Dajla-Guerguerat y en el desvío interior a Smara.",
        "MENSAJERÍA SATELITAL INDEPENDIENTE ACTIVA en todo el territorio: es el tramo del viaje con mayor distancia entre núcleos habitados y donde una avería sin cobertura se convierte antes en un problema serio. No es un lujo, es el plan de emergencia.",
        "Compartir plan diario y hora prevista de cruce de Guerguerat con la base en España antes de iniciar el tramo final, en las dos pasadas.",
        "Revisar el mapa oficial de Starlink 30-60 días antes de cada pasada por si Marruecos ha activado la licencia: es el cambio que más mejoraría este tramo.",
    ],
    perro_intro=[
        "SIN TRÁMITE PROPIO: el territorio está bajo administración marroquí continua en el corredor de la ruta, así que no hay aduana ni control veterinario independiente. Lo que valga para entrar en Marruecos (pasaporte europeo, microchip, rabia en vigor y certificado veterinario reciente, habitualmente de menos de 10 días) cubre también este tramo.",
        "El control real se produce al SALIR hacia Mauritania, en Guerguerat: llevar el pasaporte/cartilla del perro visible y el certificado sanitario en FRANCÉS, que es lo que puede pedir el lado mauritano. Lo mismo al reentrar en la subida.",
        "EL PROBLEMA DE ESTE TRAMO NO ES EL PAPELEO, ES EL DESIERTO: no hay veterinario fiable en unos 1.100 km, entre Agadir/Guelmim y Nuadibú. Es el tramo más desasistido de toda la primera mitad del viaje. Botiquín canino completo y revisión veterinaria hecha en Agadir antes de bajar.",
        "Calor extremo, viento constante y arena en suspensión: agua abundante, sombra real en las paradas, protección ocular si el viento arrecia, y conducción en las horas frescas. Nunca dejarlo en el vehículo cerrado, y menos en la cola de Guerguerat.",
        "Rabia endémica en perros asilvestrados: Marruecos y su territorio administrado son la zona de la ruta con mayor riesgo de mordedura de can callejero, especialmente en las afueras de El Aaiún y Dajla. Evitar todo contacto y no soltarlo cerca de núcleos urbanos.",
        "Segunda pasada: en la subida el perro llevará ya siete u ocho meses de África encima y quedará solo Marruecos antes de la reentrada a la UE. Dajla y El Aaiún NO son sitio para resolver nada veterinario: lo que haga falta se resuelve en Nuakchot antes, o en Agadir después.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Golpe de calor como riesgo principal, para personas y perro, en todo el corredor: veranos de 43-45 °C en el interior, agua abundante, sombra y horarios de conducción que eviten las horas centrales. En enero (bajada) el clima es benigno, con medias de unos 18-21 °C en la costa.",
        "Aislamiento sanitario: El Aaiún y Dajla cubren urgencias básicas, no politraumatismos graves. La evacuación realista es a Agadir (1.200 km desde Dajla) o a Canarias. SEGURO CON EVACUACIÓN MÉDICA IMPRESCINDIBLE en este tramo, y comprobar que la póliza cubre expresamente el Sáhara Occidental y no solo «Marruecos».",
        "Agua: no beber del grifo. El Aaiún tiene planta desaladora y agua embotellada en los supermercados; Dajla igual. Fuera de esas dos ciudades, prácticamente nada: cargar reserva completa en ambas.",
        "Sin malaria ni fiebre amarilla en el territorio: es el último tramo «limpio» antes de que empiece el bloque tropical en Mauritania y Senegal. Buen momento para revisar que la profilaxis y las vacunas están listas para lo que viene.",
        "Rabia endémica en animales callejeros: no acariciar perros ni gatos, y tener localizado el protocolo de profilaxis post-exposición — que en la práctica significaría evacuación a Agadir o Canarias.",
        "Fatiga de conducción: 290 y 250 km de recta monótona con viento lateral son un factor de riesgo real. Turnarse al volante, parar cada dos horas y no encadenar dos etapas largas en un día.",
    ],
    seguridad_intro=("El corredor costero del Sáhara Occidental es, en la práctica, uno de los tramos más TRANQUILOS de todo el viaje en cuanto a delincuencia: fuerte presencia de gendarmería y ejército, tráfico constante de camiones hacia Mauritania y relatos de overlanders sin incidentes. "
                     "Lo que sí condiciona la ruta es de otra naturaleza: un campo de minas de 2.700 km que hace inviable salir del asfalto, un aislamiento de cientos de kilómetros entre núcleos, un paso fronterizo que tuvo enfrentamientos armados en 2020 y un contexto político que exige discreción. "
                     "Se trata con rigor, no con alarmismo: el corredor se recorre sin problemas todos los días del año, siempre que se respeten las reglas."),
    seguridad=[
        "NUNCA abandonar la carretera asfaltada ni las pistas balizadas y transitadas. Es la regla que anula a todas las demás, y la razón son las minas: el campo minado que flanquea el muro es el más largo del mundo y hay minas documentadas también fuera de él (Cabo Barbas, junto a la bahía de Cintra).",
        "No fotografiar infraestructura militar, el muro/berma, el puerto y la cinta de fosfatos de Bu Craa, los controles de gendarmería ni el entorno del paso de Guerguerat. Nada de dron.",
        "Controles de gendarmería: frecuentes, correctos y sin petición de dinero según todos los relatos. Lo que consumen es tiempo. Llevar las fichas impresas y ser paciente y educado; no discutir ni bromear sobre el estatus del territorio.",
        "Guerguerat: revalidar la situación 72 h antes de cada cruce. Hubo intervención militar marroquí en noviembre de 2020 y el alto el fuego de 1991 sigue formalmente roto; el paso funciona, pero no es un trámite rutinario y conviene comprobar que no hay incidencias.",
        "No conducir de noche en ningún punto: camiones pesados, dromedarios sueltos, tormentas de arena y fatiga por monotonía.",
        "No pernoctar fuera de núcleos en el tramo El Aaiún-Dajla. En la laguna de Dajla, sí, y con otros viajeros alrededor.",
        "Política y conversación: el contencioso es materia extremadamente sensible en todo Marruecos. No opinar, no discutir toponimia y no grabar ni fotografiar manifestaciones o presencia policial.",
        "Compartir plan diario y hora prevista de cruce de la frontera con la base en España antes de iniciar el tramo final, en las dos pasadas. Mensajería satelital activa.",
        "Revisar el aviso del MAEC 72 h antes de cada entrada al territorio, en la bajada y en la subida.",
    ],
    agua_combustible_alerta="Dos tramos críticos, y los mismos en las dos pasadas: BOJADOR → CRUCE DE DAJLA son ~290 km sin absolutamente nada entre medias, y DAJLA → BIR GANDOUZ son ~250 km, el tramo más largo sin combustible garantizado de todo el bloque Marruecos/Sáhara Occidental. Salir lleno de Bojador y de Dajla y llevar bidón de reserva. Agua potable prácticamente inexistente fuera de El Aaiún y Dajla: cargar TODA la reserva en esas dos ciudades. Ventaja compensatoria: el gasóleo está subvencionado y es notablemente más barato que en el resto de Marruecos, así que conviene entrar al territorio con poco y repostar ya dentro.",
    agua=[
        "El Aaiún y Dajla son los ÚNICOS dos puntos con suministro garantizado de todo el territorio: agua embotellada en supermercados y planta desaladora en El Aaiún. Fuera de ellas, no dar por hecho ningún punto en 1.100 km.",
        "Cargar la reserva completa de los dos vehículos (mínimo 20-30 l de agua de boca por vehículo) en cada una de las dos ciudades, en las dos pasadas.",
        "Recarga del depósito de uso general (ducha, aseo, vajilla, limpieza): estaciones de servicio Afriquia/Shell de El Aaiún y Dajla y los campamentos de la laguna de Dajla (tipo Point Dakhla, La Sarga) permiten llenar con manguera. Entre Bojador y Bir Gandouz no contar con nada.",
        "No beber del grifo. El agua desalada de El Aaiún es potable pero de sabor desagradable: filtrarla o usarla solo para el depósito de uso general.",
    ],
    combustible=[
        "El Aaiún → Laayoune Plage (20 km) → Lemsid (80 km) → Bojador (80 km): tramo bien cubierto. Repostar en cada parada aunque no haga falta, porque lo que viene después no perdona.",
        "Bojador → cruce de Dajla (290 km): el tramo intermedio más largo del corredor. No hay nada fiable entre medias salvo viento. Salir de Bojador con el depósito lleno.",
        "Dajla → Bir Gandouz (~250 km) → Guerguerat (~80 km): tramo crítico final. Hay estaciones antiguas cerca de El Argoub o Tchika que pueden estar vacías: no confiar en ellas como plan principal. Bidón de reserva lleno.",
        "Desvío interior El Aaiún → Smara (~240 km, corredor de subida): oferta escasa. Repostar a fondo en El Aaiún y POR CONFIRMAR sobre el terreno si hay algo fiable en el trayecto antes de comprometer la etapa.",
        "COMBUSTIBLE SUBVENCIONADO: el gasóleo del territorio es notablemente más barato que en el resto de Marruecos por la política de subvención de la administración. Estrategia: entrar desde Tarfaya con el depósito lo más bajo que permita la prudencia y repostar ya dentro; en la subida, aprovechar para llenar todo antes de volver a Marruecos. Confirmar el diferencial de precio al pasar, que cambia con las políticas de subvención.",
        "Calidad: estándar marroquí en toda la red (Afriquia, Ziz, Shell, Total). Sin alternativa de mejor calidad en este tramo; filtro de gasóleo de repuesto a bordo.",
    ],
    experiencias_intro="Relatos y comentarios reales de otros overlanders sobre el tránsito por el Sáhara Occidental y el paso de Guerguerat, para contrastar con el contenido oficial de esta ficha. Es uno de los tramos mejor documentados de toda la ruta, porque es el cuello de botella obligatorio de cualquiera que baje a África por la costa atlántica:",
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("eVisa mauritana · DOS veces", "Tramitar con antelación suficiente antes de cada uno de los dos cruces de Guerguerat. No hay visado a la llegada: sin eVisa, el viaje se para en la frontera"),
        ("Situación de Guerguerat", "Revalidar 72 h antes de cada cruce que no hay incidencias: el alto el fuego de 1991 sigue formalmente roto desde noviembre de 2020. Confirmar también horarios de apertura y cierre de ambos lados"),
        ("Ruta de salida de la subida", "Decidir entre Smara → Tan-Tan (interior, corredor distinto del de bajada) y el regreso por la N1 vía El Aaiún y Tarfaya. Confirmar antes estado de la carretera, controles y combustible del eje interior"),
        ("Sebja de Imlili", "Confirmar en Dajla el acceso real, el estado de la pista, la disponibilidad de guía local y la coordenada exacta. Es el único desvío de tierra contemplado del territorio y no se hace sin guía"),
        ("Fuentes termales de Asmaa", "Confirmar ubicación exacta, horarios y si hay separación por sexos antes de contar con la visita"),
        ("Dron", "Decidir antes de embarcar en Algeciras: o se deja el dron en España, o se cierra la autorización escrita de la DGAC marroquí. No hay tercera opción viable"),
        ("Starlink", "Verificar en el mapa oficial 30-60 días antes de cada pasada si Marruecos ha activado la licencia; hoy no consta servicio"),
        ("Seguro de evacuación", "Comprobar por escrito que la póliza cubre expresamente el SÁHARA OCCIDENTAL y no solo «Marruecos»: muchas pólizas lo tratan como territorio aparte o lo excluyen"),
        ("Combustible del tramo final", "Confirmar en Dajla, antes de salir, que Bir Gandouz tiene suministro; las estaciones intermedias de El Argoub/Tchika no son plan principal"),
        ("Perro · veterinario", "Revisión veterinaria completa en Agadir antes de bajar, en la ida; y en Nuakchot antes de subir, en la vuelta. No hay nada fiable en ~1.100 km"),
        ("Foca monje de Cabo Blanco", "NO es visitable desde este territorio: el acceso es por el lado mauritano desde Nuadibú y la colonia está en reserva de acceso restringido. Si interesa, planificarlo en la ficha de MAURITANIA y con operador autorizado"),
        ("Fotos pendientes de sustituir", "Solo hay tres imágenes del territorio verificadas en Wikimedia Commons para esta revisión (catedral de El Aaiún, costa de Dajla y paso de Guerguerat), reutilizadas como IMAGEN DE REFERENCIA en el resto de PDIs y así indicado en cada descripción. Sustituir por fotos propias cuando las tengamos"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada, una guía de navegación ni una toma de posición sobre el estatus del territorio, que Naciones Unidas considera no autónomo y pendiente de resolución. Los topónimos se dan en la forma que corresponde a cada contexto y no implican reconocimiento de soberanía.",
    emergency="Mismos números que Marruecos: Policía 19 · Gendarmería Real 177 · Protección Civil/Ambulancia 15 · Emergencia única 112. Sin consulado español en el territorio: Consulado General de España en Agadir (+212 528 84 56 81) o Embajada de España en Rabat. En el tramo Dajla-Guerguerat, contar con que la única vía de aviso puede ser la mensajería satelital.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

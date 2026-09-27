# -*- coding: utf-8 -*-
"""Planificador de ruta del presupuesto: qué países se recorren y en qué orden.

La página /planificador/ deja marcar cualquier país continental y rehace sola el
orden, los países de tránsito obligatorio, los km, los días y el dinero. Este
módulo solo tiene los datos fijos; el cálculo va en el navegador
(presupuesto_page.py).

Decisiones del propietario (26-09-2026): el orden es automático y editable, y
el viaje siempre empieza y acaba conduciendo desde/hasta Tánger Med (sin enviar
los coches en barco).
"""

# Punto de salida y llegada del viaje en coche (puerto de Tánger Med): solo
# como referencia de la ruta por defecto; la salida real la da el ferry.
TANGER_MED = (35.8900, -5.5000)

# ---------------------------------------------------------------- recorridos
# Cada país tiene uno o varios recorridos: por defecto «A» y «B» son el
# corredor principal y el alternativo de su ficha. Algunos países tienen
# recorridos propios (lista de puntos aquí mismo).
MARRUECOS_DIRECTO = [(35.8900, -5.5000), (34.0209, -6.8416), (33.5731, -7.5898), (31.6295, -7.9811),
                     (30.4278, -9.5981), (28.9870, -10.0574), (28.4378, -11.1032), (27.9394, -12.9231)]
MAURITANIA_COSTA = [(21.3337, -16.9472), (20.9300, -17.0330), (19.8784, -16.3044), (18.0858, -15.9785),
                    (16.2158, -16.4148)]

# Casamance por carretera (OSRM, 27-09-2026): Kalifourou → Vélingara → Kolda →
# Ziguinchor → Bignona → Séléti (frontera de Gambia). Evita Guinea-Bisáu.
SENEGAL_CASAMANCE = [(12.5824, -13.3721), (12.6107, -13.5344), (12.6795, -13.5597), (12.7585, -13.5436),
                     (12.8721, -13.5581), (12.9148, -13.6334), (13.0194, -13.7065), (13.0445, -13.7943),
                     (13.0232, -13.9319), (13.0559, -14.0331), (12.9696, -14.0306), (12.9144, -14.1122),
                     (12.9227, -14.2625), (12.8599, -14.5019), (12.8382, -14.7561), (12.8913, -14.9373),
                     (12.8214, -15.0357), (12.7408, -15.1534), (12.6416, -15.5004), (12.5904, -15.4934),
                     (12.5179, -15.5207), (12.497, -15.6303), (12.5624, -15.6846), (12.5438, -15.8095),
                     (12.569, -15.9211), (12.6277, -16.018), (12.593, -16.0753), (12.5592, -16.2719),
                     (12.6679, -16.2607), (12.8153, -16.2328), (12.8915, -16.3368), (12.9141, -16.433),
                     (13.0429, -16.598), (13.1, -16.52)]

# (slug, id, etiqueta, clave) · clave: "A", "B", "A+B" (los dos corredores de
# la ficha como un único trayecto), "ex:<n>" (corredor extra de la ficha) o una
# lista de puntos propia, o una función (datos de la ficha, fichas) → puntos.
# Los países que no aparecen aquí usan A y B tal cual.
RECORRIDOS_PROPIOS = {
    # Senegal: la vuelta de la ficha (B) cruza Gambia por Banjul. Si Gambia va
    # en la ruta como país propio, Senegal se parte en S (Casamance, hasta la
    # frontera de Gambia) y N (desde Karang hasta Diama); ver VIA.
    "senegal": [
        ("A", "Diama · Saint-Louis · Ferlo · Niokolo-Koba · Kédougou · Kalifourou", "A"),
        ("B", "Kalifourou · Kolda · Casamance · Gambia (Banjul) · Saloum · Dakar · lago Retba · Diama",
         lambda d, F: SENEGAL_CASAMANCE + list(F["gambia"]["corridor"]) + list(d["corridor_alt"][1:])),
        ("S", "Casamance: Kalifourou · Kolda · Ziguinchor · Séléti (frontera de Gambia)", SENEGAL_CASAMANCE),
        ("N", "Karang (frontera de Gambia) · Saloum · Dakar · lago Retba · Diama", lambda d, F: list(d["corridor_alt"][1:])),
    ],
    "marruecos": [
        ("A", "Bucle de la ficha (Fez, Merzouga, Todra, Marrakech, costa)", "A"),
        ("R", "Vía rápida Tánger Med – Tarfaya (sin paradas)", MARRUECOS_DIRECTO),
    ],
    "mauritania": [
        ("A", "Adrar: Guerguerat → Atar → Uadane → Nuakchot → Diama", "A+B"),
        ("C", "Directo por la costa: Guerguerat → Nuadibú → Nuakchot → Diama", MAURITANIA_COSTA),
        # Entrada desde Argelia por Tinduf (Hassi 75): corredor dibujado en la
        # ficha de Mauritania (extra 0). Se usa si la ruta viene o va a Argelia (VIA).
        ("N", "Desde Argelia: Hassi 75 → Aïn Bentili → Bir Moghrein → Zuérat → Atar → Chinguetti → Nuakchot → Diama", "ex:mauritania:0"),
    ],
    # Cabinda no es un país: es el enclave angoleño entre Congo y RD Congo. Se
    # trata como un nudo de paso (visado y gasóleo de Angola).
    "cabinda": [
        ("C", "Tránsito Massabi – Yema", "ex:angola:0"),
    ],
}

# Recorrido que se usa cuando el país es solo de paso (no marcado o ya
# recorrido las veces que dice su plan). Si no está aquí, el tránsito es una
# línea por el punto del país que mejor une la entrada y la salida.
# Recorrido obligado según el país vecino: si la ruta llega de Argelia o va
# hacia Argelia, Mauritania solo se puede cruzar por la pista de Tinduf.
# Una lista = candidatos: se usa el que mejor une la entrada y la salida.
VIA = {"mauritania": {"argelia": "N"}, "senegal": {"gambia": ["S", "N"]}}
# Países que un recorrido atraviesa sin ser su país: si no van en la ruta justo
# al lado, se añaden como paso (cuentan visado, tasas y entradas).
CRUZA = {"senegal:B": ["gambia"]}
TRANSITO_FIJO = {"marruecos": "R", "sahara-occidental": "A", "mauritania": "C", "cabinda": "C"}

# Km por carretera de cada recorrido, un sentido. OSRM (router.project-osrm.org,
# OpenStreetMap) por todos los puntos del corredor, 26-09-2026. Excepciones:
# Zanzíbar omitido en la costa de Tanzania (ferry); en el Adrar, el Kaokoland,
# Chad, Sudán del Sur y Yibuti varios puntos no tienen carretera cartografiada y
# el enrutador da vueltas absurdas o no encuentra ruta: ahí se usa línea recta
# × 1,5 y la cifra se marca como aproximada.
KM = {
    "marruecos:R": 1401, "marruecos:A": 2786,
    "sahara-occidental:A": 1384, "sahara-occidental:B": 1730,
    "mauritania:A": 2800, "mauritania:C": 845,
    # Frontera (Ismail Ould El Bardi) → Zuérat por pista: ~790 km (Sahara
    # Overland y relatos 2025: Tinduf–Zuérat 800–860 km); Zuérat → F'Derik →
    # Atar → Chinguetti → Atar → Nuakchot → Diama por OSRM: 1.160 km.
    "mauritania:N": 1950,
    "senegal:A": 1946, "senegal:B": 1378, "senegal:S": 520, "senegal:N": 601,
    "gambia:A": 257, "gambia:B": 641,
    "guinea:A": 2009, "guinea:B": 1275,
    "costa-de-marfil:A": 2142, "costa-de-marfil:B": 1259,
    "ghana:A": 885, "ghana:B": 1807,
    "togo:A": 111, "togo:B": 957,
    "benin:A": 235, "benin:B": 697,
    "nigeria:A": 1319, "nigeria:B": 1483,
    "camerun:A": 1295, "camerun:B": 2873,
    "congo:A": 2297, "congo:B": 1748,
    "rd-congo:A": 361, "rd-congo:B": 361,
    "cabinda:C": 123,
    "angola:A": 2878, "angola:B": 3144,
    "zambia:A": 4623, "zambia:B": 1235,
    "malaui:A": 2040, "malaui:B": 1008,
    "tanzania:A": 3463, "tanzania:B": 1730,
    "kenia:A": 2371, "kenia:B": 1728,
    "mozambique:A": 5994, "mozambique:B": 1246,
    "zimbabue:A": 2680, "zimbabue:B": 2891,
    "botsuana:A": 3608, "botsuana:B": 3030,
    "sudafrica:A": 6338, "sudafrica:B": 2943,
    "namibia:A": 2175, "namibia:B": 4571,
    "sierra-leona:A": 1114, "sierra-leona:B": 1083,
    "liberia:A": 928, "liberia:B": 818,
    "gabon:A": 1290, "gabon:B": 1398,
    "uganda:A": 1918, "uganda:B": 969,
    "ruanda:A": 478, "ruanda:B": 539,
    "esuatini:A": 243, "esuatini:B": 181,
    "lesoto:A": 529, "lesoto:B": 1140,
    "mali:A": 2466, "mali:B": 2497,
    "guinea-bisau:A": 1006, "guinea-bisau:B": 438,
    "sudan:A": 1978, "sudan:B": 1395,
    # Argelia (26-09-2026, OSRM): A = Oum Teboul → Annaba → Constantina →
    # Djémila → Timgad → Biskra → El Oued → Ghardaïa → El Menia → Timimoun →
    # Adrar → Béni Abbès → Taghit → Béchar → Tinduf → Hassi 75;
    # B = lo mismo entrando por Taleb Larbi (Hazoua) sin el norte.
    "argelia:A": 3702, "argelia:B": 2861,
    # Túnez: B = Midès → Tozeur → Gafsa → Sidi Bouzid → Maktar → Le Kef →
    # Bulla Regia → Aïn Draham → Tabarka → Melloula (salida a Argelia).
    "tunez:A": 2040, "tunez:B": 579,
    "libia:A": 1624, "libia:B": 2613,
    "burkina-faso:A": 1920, "burkina-faso:B": 1510,
    "niger:A": 5691, "niger:B": 934,
    "chad:A": 4548, "chad:B": 2879,
    "rca:A": 1692, "rca:B": 2653,
    "sudan-del-sur:A": 2730, "sudan-del-sur:B": 1116,
    "somalia:A": 1979, "somalia:B": 946,
    "eritrea:A": 864, "eritrea:B": 853,
    "guinea-ecuatorial:A": 717,
    "burundi:A": 952, "burundi:B": 446,
    "etiopia:A": 3977, "etiopia:B": 1552,
    "egipto:A": 3201, "egipto:B": 2211,
    "yibuti:A": 1010, "yibuti:B": 390,
}
KM_APROX = {"mauritania:N", "mauritania:A", "namibia:B", "chad:A", "chad:B", "sudan-del-sur:A", "yibuti:A"}
# Km de un trayecto sin corredor (enlaces y tránsitos): línea recta × factor.
FACTOR_SIN_RUTA = 1.25

# ---------------------------------------------------------------- plan
# Orden de la planificación actual (países marcados, en orden de marcha). El
# viaje empieza en el primero y acaba en el último, cada uno con su ferry. Los países de paso entre uno y
# otro los añade el cálculo.
ORDEN_PLAN = ["marruecos", "sahara-occidental", "mauritania", "senegal", "guinea", "costa-de-marfil", "ghana", "togo",
              "benin", "nigeria", "camerun", "congo", "rd-congo", "angola", "zambia", "malaui", "tanzania",
              "kenia", "mozambique", "zimbabue", "botsuana", "sudafrica", "namibia", "gambia"]

# Qué recorrido se hace cada vez que se entra en el país: "A|B" = el A la
# primera vez y el B la segunda; "A+B" = los dos seguidos en una sola entrada.
# Si se entra más veces que las que dice el plan, las demás son de tránsito
# (se pueden cambiar en la página con «Parar / Cruzar»). Los países que no
# aparecen aquí paran en "A". Marruecos vacío = cruzar por la vía rápida
# (decisión del proyecto: de paso, sin paradas).
PLAN = {
    "marruecos": "", "sahara-occidental": "A|B", "mauritania": "A|A", "senegal": "A|B|N",
    "gambia": "A", "guinea": "A|B", "costa-de-marfil": "A|B", "ghana": "A|B", "togo": "A|B",
    "benin": "A|B", "nigeria": "A|B", "camerun": "A|B", "congo": "A|B", "rd-congo": "A|B",
    "angola": "A|B", "zambia": "A", "malaui": "A", "tanzania": "A|B", "kenia": "A+B",
    "mozambique": "A", "zimbabue": "A", "botsuana": "A", "sudafrica": "A+B", "namibia": "A",
    # Variante estudiada el 26-09-2026: Túnez a fondo (bucle sur + salida por
    # el oeste hasta Melloula) y Argelia de norte a Tinduf.
    "tunez": "A+B", "argelia": "A",
}

# ---------------------------------------------------------------- restricciones
# Ningún país está vetado en el planificador: los que están en conflicto van
# en CONFLICTO (solo se usan si se marcan y siempre con aviso).
EXCLUIDOS = set()
# Se pueden marcar, con aviso, pero el cálculo nunca los usa como paso si no
# están marcados.
CONFLICTO = {"mali", "sudan", "libia", "burkina-faso", "niger", "chad", "rca", "sudan-del-sur", "somalia"}
# Sin carretera desde el continente: no entran en el planificador.
ISLAS = {"madagascar", "cabo-verde", "santo-tome", "comoras", "seychelles", "mauricio"}

# Fronteras terrestres entre países continentales (más el enlace de Cabinda).
# (a, b, tipo, nota) · tipo: "" normal, "ferry" (se cruza en barco, penaliza),
# "evitar" (solo si no hay otro camino, con aviso: el MAEC desaconseja la
# carretera en RD Congo y el proyecto solo cruza el Kongo Central) o "cerrada"
# (no se usa nunca).
FRONTERAS = [
    ("marruecos", "sahara-occidental", "", ""),
    ("marruecos", "argelia", "cerrada", "Frontera cerrada desde 1994"),
    ("sahara-occidental", "mauritania", "", "Guerguerat"),
    ("mauritania", "senegal", "", "Diama / Rosso"),
    ("mauritania", "mali", "", ""),
    ("mauritania", "argelia", "", "Hassi 75 (PK75) – Ismail Ould El Bardi, al sur de Tinduf: abierto a personas desde el 23-02-2024; escolta en Tinduf; zona roja del MAEC en Mauritania"),
    ("senegal", "gambia", "", ""), ("senegal", "guinea", "", ""), ("senegal", "mali", "", ""),
    ("senegal", "guinea-bisau", "", ""),
    ("guinea", "guinea-bisau", "", ""), ("guinea", "sierra-leona", "", ""), ("guinea", "liberia", "", ""),
    ("guinea", "costa-de-marfil", "", ""), ("guinea", "mali", "", ""),
    ("sierra-leona", "liberia", "", ""), ("liberia", "costa-de-marfil", "", ""),
    ("costa-de-marfil", "ghana", "", ""), ("costa-de-marfil", "burkina-faso", "", ""), ("costa-de-marfil", "mali", "", ""),
    ("ghana", "togo", "", ""), ("ghana", "burkina-faso", "", ""),
    ("togo", "benin", "", ""), ("togo", "burkina-faso", "", ""),
    ("benin", "nigeria", "", ""), ("benin", "niger", "", ""), ("benin", "burkina-faso", "", ""),
    ("nigeria", "camerun", "", ""), ("nigeria", "niger", "", ""), ("nigeria", "chad", "", ""),
    ("camerun", "chad", "", ""), ("camerun", "rca", "", ""), ("camerun", "congo", "", ""),
    ("camerun", "gabon", "", ""), ("camerun", "guinea-ecuatorial", "cerrada", "Fronteras terrestres de Guinea Ecuatorial cerradas desde el 15-12-2025"),
    ("guinea-ecuatorial", "gabon", "cerrada", "Fronteras terrestres de Guinea Ecuatorial cerradas desde el 15-12-2025"), ("gabon", "congo", "", ""),
    ("congo", "rca", "", ""), ("congo", "cabinda", "", "Massabi"),
    ("congo", "rd-congo", "ferry", "Ferry Brazzaville–Kinshasa"),
    ("cabinda", "rd-congo", "", "Yema"),
    ("rd-congo", "angola", "", "Lufu / Luvo"), ("rd-congo", "rca", "evitar", "Cruza el interior de RD Congo"), ("rd-congo", "sudan-del-sur", "evitar", "Cruza el interior de RD Congo"),
    ("rd-congo", "uganda", "evitar", "Cruza el interior de RD Congo"), ("rd-congo", "ruanda", "evitar", "Cruza el interior de RD Congo"), ("rd-congo", "burundi", "evitar", "Cruza el interior de RD Congo"),
    ("rd-congo", "zambia", "evitar", "Cruza el interior de RD Congo"),
    ("angola", "zambia", "", ""), ("angola", "namibia", "", "Santa Clara – Oshikango"),
    ("zambia", "namibia", "", ""), ("zambia", "botsuana", "", "Puente de Kazungula"),
    ("zambia", "zimbabue", "", ""), ("zambia", "mozambique", "", ""), ("zambia", "malaui", "", ""),
    ("zambia", "tanzania", "", ""),
    ("namibia", "botsuana", "", ""), ("namibia", "sudafrica", "", ""),
    ("botsuana", "zimbabue", "", ""), ("botsuana", "sudafrica", "", ""),
    ("zimbabue", "sudafrica", "", ""), ("zimbabue", "mozambique", "", ""),
    ("sudafrica", "mozambique", "", ""), ("sudafrica", "esuatini", "", ""), ("sudafrica", "lesoto", "", ""),
    ("esuatini", "mozambique", "", ""),
    ("mozambique", "malaui", "", ""), ("mozambique", "tanzania", "", "Puente de la Unidad (Rovuma)"),
    ("malaui", "tanzania", "", ""),
    ("tanzania", "burundi", "", ""), ("tanzania", "ruanda", "", ""), ("tanzania", "uganda", "", ""),
    ("tanzania", "kenia", "", ""),
    ("burundi", "ruanda", "cerrada", "Cerrada por Burundi desde enero de 2024"), ("ruanda", "uganda", "", ""),
    ("uganda", "kenia", "", ""), ("uganda", "sudan-del-sur", "", ""),
    ("kenia", "sudan-del-sur", "", ""), ("kenia", "etiopia", "", "Moyale"), ("kenia", "somalia", "", ""),
    ("etiopia", "sudan-del-sur", "", ""), ("etiopia", "sudan", "", ""), ("etiopia", "yibuti", "", ""),
    ("etiopia", "somalia", "", ""), ("etiopia", "eritrea", "cerrada", "Frontera cerrada en la práctica"),
    ("yibuti", "somalia", "", ""), ("yibuti", "eritrea", "cerrada", "Frontera cerrada"),
    ("eritrea", "sudan", "", ""),
    ("sudan", "egipto", "", ""), ("sudan", "libia", "", ""), ("sudan", "chad", "", ""), ("sudan", "rca", "", ""),
    ("sudan", "sudan-del-sur", "", ""),
    ("sudan-del-sur", "rca", "", ""),
    ("egipto", "libia", "", ""),
    ("libia", "tunez", "", ""), ("libia", "argelia", "", ""), ("libia", "niger", "", ""), ("libia", "chad", "", ""),
    ("tunez", "argelia", "", ""),
    ("argelia", "niger", "", ""), ("argelia", "mali", "", ""),
    ("mali", "niger", "", ""), ("mali", "burkina-faso", "", ""),
    ("burkina-faso", "niger", "", ""),
    ("niger", "chad", "", ""), ("chad", "rca", "", ""),
]
# Penalizaciones del cálculo del orden: pasar por un país que no está marcado
# (otro visado, otra frontera) y cruzar en ferry.
PENAL_NO_MARCADO = 2.5
PENAL_FERRY_KM = 300

# ---------------------------------------------------------------- días
SALIDA = "2027-01-10"
REGRESO_PREVISTO = "2027-08-15"
# Km de media al día, contando los días de parada. Estimación: en los países
# donde se para, un ritmo de viaje de exploración; en los de paso, días largos
# de carretera.
RITMO_VISITA = 250
RITMO_TRANSITO = 450
# Días de margen sobre el total: esperas en fronteras, trámites de visados en
# ruta, averías, lluvia. Estimación.
MARGEN_PCT = 10
# ---------------------------------------------------------------- ferris
# Decisión del propietario (26-09-2026): el itinerario es libre; el viaje
# empieza en el primer país de la lista y acaba en el último, y la página busca
# el ferry a ese país (o al país con ferry más cercano si no tiene).
# Se sale y se vuelve a BARCELONA: los km hasta el puerto de embarque cuentan.
ORIGEN = "Barcelona"
GASOIL_EUROPA = {  # €/l, GlobalPetrolPrices 21-09-2026 (USD × 0,8734)
    "es": 1.934, "fr": 2.383, "it": 2.343,
}
# Actualización semanal (content/precios/auto.json), si existe.
from precios_auto import auto as _precios_auto
_A = _precios_auto()
if _A:
    for _c in GASOIL_EUROPA:
        if _A["gasoil_usd"].get("eu:" + _c):
            GASOIL_EUROPA[_c] = round(_A["gasoil_usd"]["eu:" + _c] * _A["usd_eur"], 3)
# Precio de cada vehículo en un sentido = coche + conductor + (personas − 1) ×
# pasajero. «coche» es la tarifa de coche con conductor (aFerry: media del mes
# de ida —enero— y del de vuelta —julio/agosto— de 2026, o el «desde» de la
# naviera); no incluye camarote ni el recargo de vehículo alto (el 4x4 con
# tienda mide ~2,3 m). Solo Barcelona–Tánger Med es un presupuesto real para
# nuestros vehículos (GNV, clase A2, camarote). El perro va aparte
# (PERRO_FERRY). Investigación completa: documento «ferris-africa-2027».
# (id, país, origen, puerto de llegada, lat, lon, naviera, horas, frecuencia,
#  coche_ida, coche_vuelta, pasajero, km desde Barcelona, gasóleo, nota, fuente)
# Ferry que se propone por defecto para cada país (se puede cambiar en la
# página): Marruecos, el presupuesto real de GNV; Argelia y Túnez, los más
# prácticos desde España según la investigación del 26-09-2026 (más salidas
# todo el año y camarote para mascota).
FERRY_PREFERIDO = {"marruecos": "bcn-tanger", "argelia": "vlc-mostaganem", "tunez": "gen-tunez"}
_AF = "https://www.aferry.com/es-es/"
FERRIES = [
    ("bcn-tanger", "marruecos", "Barcelona", "Tánger Med", 35.88, -5.50, "GNV", 32, "2–3 por semana",
     403.85, 369.14, 81.32, 0, "es",
     "Presupuesto real 10-01-2027 (ida) y abril–mayo 2027 (vuelta), coche clase A2 y camarote.",
     "https://www.gnv.it/es/departures-calendar?type=outward"),
    ("alg-tanger", "marruecos", "Algeciras", "Tánger Med", 35.88, -5.50, "Baleària · DFDS · AML", 1.5, "~130 por semana",
     185, 210, 29, 1100, "es",
     "Coche + conductor: media de enero y agosto (aFerry). Pasajero desde 29 € (Baleària). En julio–agosto, colas de la Operación Paso del Estrecho.",
     _AF + "algeciras-tanger-med"),
    ("tarifa-tanger", "marruecos", "Tarifa", "Tánger Ville", 35.79, -5.81, "Baleària · AML", 1, "~75 por semana",
     213, 219, 42, 1120, "es", "Llega al puerto de la ciudad, no a Tánger Med.", _AF + "tarifa-tangier"),
    ("alm-nador", "marruecos", "Almería", "Nador", 35.28, -2.93, "Baleària · GNV · AML", 8, "~8 por semana",
     197, 220, 47, 810, "es", "Conviene si la ruta empieza por el este de Marruecos.", _AF + "almeria-nador"),
    ("bcn-nador", "marruecos", "Barcelona", "Nador", 35.28, -2.93, "GNV", 30, "1 por semana",
     251, 293, 94, 0, "es", "Coche + conductor: media de enero y agosto (aFerry).", _AF + "barcelona-nador"),
    ("vlc-mostaganem", "argelia", "Valencia", "Mostaganem", 35.94, 0.07, "Baleària", 15.5, "1 por semana (3 en verano)",
     200, 475, 80, 350, "es",
     "Coche + conductor: media de enero y agosto (aFerry). Pasajero: estimación (Baleària no publica la tarifa suelta). Barcos con camarote para mascota.",
     "https://www.balearia.com/es/rutas-horarios/ferry-valencia-mostaganem"),
    ("vlc-argel", "argelia", "Valencia", "Argel", 36.78, 3.06, "Baleària", 17, "1 por semana",
     295, 295, 80, 350, "es", "Baleària: precio medio ida y vuelta con vehículo ~590 €. Pasajero: estimación.",
     "https://www.balearia.com/es/rutas-horarios/ferry-valencia-argel"),
    ("bcn-argel", "argelia", "Barcelona", "Argel", 36.78, 3.06, "Baleària", 20, "1 por semana (lunes), todo el año",
     209, 955, 80, 0, "es", "Coche + conductor: media de enero y de julio (aFerry); julio es el pico de la diáspora. Pasajero: estimación.",
     "https://www.balearia.com/es/rutas-horarios/ferry-barcelona-argel"),
    ("alm-oran", "argelia", "Almería", "Orán", 35.71, -0.64, "Baleària", 11, "1 por semana (enero sin confirmar)",
     189, 429, 144, 810, "es", "Coche + conductor: media de enero y agosto (aFerry). Pasajero desde 143,60 € (Baleària).",
     "https://www.balearia.com/es/rutas-horarios/ferry-almeria-oran"),
    ("alm-ghazaouet", "argelia", "Almería", "Ghazaouet", 35.10, -1.86, "Baleària", 11, "1 por semana (enero sin confirmar)",
     231, 429, 144, 810, "es", "Cerca de la frontera marroquí, que está cerrada.",
     "https://www.balearia.com/es/rutas-horarios/ferry-almeria-ghazaouet"),
    ("ali-oran", "argelia", "Alicante", "Orán", 35.71, -0.64, "Algérie Ferries · Nouris Elbahr", 13, "semanal o quincenal",
     170, 485, 80, 520, "es", "Algérie Ferries: el perro solo en perrera (~30 €, 2023), no en camarote. Pasajero: estimación.",
     "https://www.aferry.com/fr-fr/alicante-oran/"),
    ("gen-tunez", "tunez", "Génova", "Túnez (La Goulette)", 36.81, 10.30, "GNV · CTN", 24, "~3 por semana (hasta 6 en verano)",
     350, 601, 102, 900, "fr", "No hay ferry desde España a Túnez. Coche + conductor: media de enero y julio (aFerry). GNV tiene camarotes para mascota. Peajes de Francia e Italia no incluidos.",
     _AF + "genoa-tunis"),
    ("civ-tunez", "tunez", "Civitavecchia", "Túnez (La Goulette)", 36.81, 10.30, "GNV · Grimaldi", 22, "2 por semana",
     124, 246, 60, 1350, "fr", "Coche + conductor: media de enero y agosto (aFerry). Grimaldi: perro en cualquier camarote por 10 €. Peajes no incluidos.",
     _AF + "civitavecchia-tunis"),
    ("mrs-tunez", "tunez", "Marsella", "Túnez (La Goulette)", 36.81, 10.30, "CTN · Corsica Linea", 23, "1 por semana en invierno, 2+ en verano",
     426, 493, 151, 510, "fr", "CTN verano 2026: 2 adultos + coche + butacas desde 574 €. Corsica Linea: perro solo en perrera.",
     _AF + "marseille-tunis"),
]

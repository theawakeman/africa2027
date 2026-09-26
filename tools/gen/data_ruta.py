# -*- coding: utf-8 -*-
"""Planificador de ruta del presupuesto: qué países se recorren y en qué orden.

La página /presupuesto/ deja marcar cualquier país continental y rehace sola el
orden, los países de tránsito obligatorio, los km, los días y el dinero. Este
módulo solo tiene los datos fijos; el cálculo va en el navegador
(presupuesto_page.py).

Decisiones del propietario (26-09-2026): el orden es automático y editable, y
el viaje siempre empieza y acaba conduciendo desde/hasta Tánger Med (sin enviar
los coches en barco).
"""

# Punto de salida y llegada del viaje en coche (puerto de Tánger Med).
TANGER_MED = (35.8900, -5.5000)

# ---------------------------------------------------------------- recorridos
# Cada país tiene uno o varios recorridos: por defecto «A» y «B» son el
# corredor principal y el alternativo de su ficha. Algunos países tienen
# recorridos propios (lista de puntos aquí mismo).
MARRUECOS_DIRECTO = [(35.8900, -5.5000), (34.0209, -6.8416), (33.5731, -7.5898), (31.6295, -7.9811),
                     (30.4278, -9.5981), (28.9870, -10.0574), (28.4378, -11.1032), (27.9394, -12.9231)]
MAURITANIA_COSTA = [(21.3337, -16.9472), (20.9300, -17.0330), (19.8784, -16.3044), (18.0858, -15.9785),
                    (16.2158, -16.4148)]

# (slug, id, etiqueta, clave) · clave: "A", "B", "A+B" (los dos corredores de
# la ficha como un único trayecto), "ex:<n>" (corredor extra de la ficha) o una
# lista de puntos propia. Los países que no aparecen aquí usan A y B tal cual.
RECORRIDOS_PROPIOS = {
    "marruecos": [
        ("R", "Vía rápida Tánger Med – Tarfaya (sin paradas)", MARRUECOS_DIRECTO),
        ("A", "Bucle de la ficha (Fez, Merzouga, Todra, Marrakech, costa)", "A"),
    ],
    "mauritania": [
        ("A", "Adrar: Guerguerat → Atar → Uadane → Nuakchot → Diama", "A+B"),
        ("C", "Directo por la costa: Guerguerat → Nuadibú → Nuakchot → Diama", MAURITANIA_COSTA),
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
    "senegal:A": 1946, "senegal:B": 778,
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
    "argelia:A": 4053, "argelia:B": 2534,
    "tunez:A": 2040, "tunez:B": 657,
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
KM_APROX = {"mauritania:A", "namibia:B", "chad:A", "chad:B", "sudan-del-sur:A", "yibuti:A"}
# Km de un trayecto sin corredor (enlaces y tránsitos): línea recta × factor.
FACTOR_SIN_RUTA = 1.25

# ---------------------------------------------------------------- plan
# Orden de la planificación actual (países donde se para, en orden de marcha;
# Marruecos es siempre el principio y el final). Los países de paso entre uno y
# otro los añade el cálculo.
ORDEN_PLAN = ["sahara-occidental", "mauritania", "senegal", "guinea", "costa-de-marfil", "ghana", "togo",
              "benin", "nigeria", "camerun", "congo", "rd-congo", "angola", "zambia", "malaui", "tanzania",
              "kenia", "mozambique", "zimbabue", "botsuana", "sudafrica", "namibia", "gambia"]

# Qué recorrido se hace cada vez que se entra en el país: "A|B" = el A la
# primera vez y el B la segunda; "A+B" = los dos seguidos en una sola entrada.
# Si se entra más veces que las que dice el plan, las demás son de tránsito.
# Los países que no aparecen aquí usan "A".
PLAN = {
    "marruecos": "R|R", "sahara-occidental": "A|B", "mauritania": "A|A", "senegal": "A|B",
    "gambia": "A", "guinea": "A|B", "costa-de-marfil": "A|B", "ghana": "A|B", "togo": "A|B",
    "benin": "A|B", "nigeria": "A|B", "camerun": "A|B", "congo": "A|B", "rd-congo": "A|B",
    "angola": "A|B", "zambia": "A", "malaui": "A", "tanzania": "A|B", "kenia": "A+B",
    "mozambique": "A", "zimbabue": "A", "botsuana": "A", "sudafrica": "A+B", "namibia": "A",
}

# ---------------------------------------------------------------- restricciones
# No se pueden marcar ni se usan para pasar (protocolo del proyecto).
EXCLUIDOS = {"mali", "guinea-bisau", "sudan"}
# Se pueden marcar, con aviso, pero el cálculo nunca los usa como paso si no
# están marcados.
CONFLICTO = {"libia", "burkina-faso", "niger", "chad", "rca", "sudan-del-sur", "somalia"}
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
    ("mauritania", "mali", "", ""), ("mauritania", "argelia", "", "Paso de Tinduf, abierto en 2018 y poco usado"),
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
    ("camerun", "gabon", "", ""), ("camerun", "guinea-ecuatorial", "", ""),
    ("guinea-ecuatorial", "gabon", "", ""), ("gabon", "congo", "", ""),
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
    ("burundi", "ruanda", "", ""), ("ruanda", "uganda", "", ""),
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
PENAL_NO_MARCADO = 1.4
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
# Noches de ferry Barcelona – Tánger Med (ida y vuelta).
DIAS_FERRY = 2

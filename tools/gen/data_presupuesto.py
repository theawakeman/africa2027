# -*- coding: utf-8 -*-
"""Presupuesto del viaje por vehículo.

Planteamiento pedido por el propietario (25-09-2026):
  · INEOS Grenadier: 2 personas y el perro, consumo medio 15 L/100 km.
  · Delica: 1 persona, consumo medio 12 L/100 km.

La página /planificador/ es una calculadora: todos los valores de aquí son los
valores iniciales y se pueden cambiar en la propia página (se guardan solo en
ese navegador). Cada cifra lleva su fuente o dice que es una estimación.

Los países, el orden, los kilómetros y los días NO están aquí: están en
data_ruta.py y se calculan en la propia página según los países que se marquen.
"""

FECHA = "25 de septiembre de 2026"

# Tipo de cambio implícito en GlobalPetrolPrices del 21-09-2026
# (Marruecos: 1,603 USD = 1,400 EUR). El franco CFA es fijo.
USD_EUR = round(1.400 / 1.603, 4)          # 0,8734 € por dólar
XOF_EUR = 1 / 655.957

VEHICULOS = [
    # CPD (RACE, carnet de 25 hojas): importes facilitados por el propietario el
    # 26-09-2026. Los costes bancarios del aval aún no se conocen (0 = sin dato).
    {"id": "v1", "nombre": "INEOS Grenadier", "detalle": "2 personas + perro", "personas": 2, "perros": 1, "l100": 15.0,
     "cpd_libro": 383.35, "cpd_aval": 13700, "cpd_banco": 0},
    {"id": "v2", "nombre": "Delica", "detalle": "1 persona", "personas": 1, "perros": 0, "l100": 12.0,
     "cpd_libro": 383.35, "cpd_aval": 2900, "cpd_banco": 0},
]

# Los km ya son por carretera (OSRM): el factor queda en 1 y solo sirve para
# ajustar a mano (por ejemplo, 1,1 si se prevén muchas pistas lentas).
FACTOR_CARRETERA = 1.0
# Kilómetros que no están en el corredor: buscar agua, gasoil, alojamiento,
# trámites en capitales. Los corredores ya pasan por los PDIs, así que es poco.
# Estimación, no dato.
DESVIOS_PCT = 5

# ---------------------------------------------------------------- gasóleo
GPP = "https://www.globalpetrolprices.com/diesel_prices/"
GPP_FECHA = "21-09-2026"
# slug: (€/litro, fuente, fecha, nota)
GASOIL = {
    "marruecos": (1.400, GPP, GPP_FECHA, ""),
    "sahara-occidental": (1.400, GPP, GPP_FECHA, "Precio de Marruecos. En Dajla y El Aaiún suele ser algo más barato por la desgravación del sur: sin dato publicado."),
    "mauritania": (1.23, "https://infoplus.mr/fr/node/3855", "31-03-2026",
                   "Precio oficial 56,3 MRU/l (563 ouguiyas antiguas) desde el 31-03-2026, convertido a ~45,8 MRU/€. GlobalPetrolPrices no lo publica en abierto."),
    "senegal": (1.153, GPP, GPP_FECHA, ""),
    "gambia": (1.39, "https://thepoint.gm/africa/gambia/headlines/fuel-prices-go-up-in-gambia", "03-08-2026",
               "Precio oficial 116,63 GMD/l desde el 03-08-2026, convertido a ~84 GMD/€."),
    "guinea": (1.197, GPP, GPP_FECHA, ""),
    "costa-de-marfil": (1.108, GPP, GPP_FECHA, ""),
    "ghana": (1.303, GPP, GPP_FECHA, ""),
    "togo": (1.170, GPP, GPP_FECHA, ""),
    "benin": (1.146, GPP, GPP_FECHA, "Precio oficial de estación. En la calle se vende gasóleo de contrabando nigeriano más barato y de calidad dudosa."),
    "nigeria": (1.204, GPP, GPP_FECHA, ""),
    "camerun": (1.265, GPP, GPP_FECHA, ""),
    "congo": (round(500 * XOF_EUR, 3), "https://gouvernement.cg/hydrocarbures-le-prix-du-carburant-revu-a-la-hausse/", "31-01-2023",
              "Último precio oficial localizado: 500 FCFA/l (enero de 2023). No se ha encontrado un cambio posterior, pero tampoco una confirmación de 2026."),
    "rd-congo": (0.996, GPP, GPP_FECHA, "Media nacional; el Kongo Central (zona oeste) tiene su propia tarifa."),
    "angola": (0.400, GPP, GPP_FECHA, "El más barato de la ruta con diferencia: entrar y salir de Angola con los depósitos y bidones llenos."),
    "zambia": (1.205, GPP, GPP_FECHA, ""),
    "malaui": (2.952, GPP, GPP_FECHA, "El más caro de la ruta: entrar lleno desde Zambia o Tanzania y repostar lo mínimo."),
    "tanzania": (1.280, GPP, GPP_FECHA, ""),
    "kenia": (1.461, GPP, GPP_FECHA, ""),
    "mozambique": (1.589, GPP, GPP_FECHA, ""),
    "zimbabue": (1.817, GPP, GPP_FECHA, ""),
    "botsuana": (1.351, GPP, GPP_FECHA, ""),
    "sudafrica": (1.721, GPP, GPP_FECHA, "Precio del interior (Gauteng) algo mayor que en la costa."),
    "namibia": (1.501, GPP, GPP_FECHA, ""),
    # Resto de países continentales (solo cuentan si se marcan o se cruzan).
    # GlobalPetrolPrices en USD, convertido al cambio implícito de arriba.
    "sierra-leona": (round(2.287 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "liberia": (round(1.551 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "gabon": (round(1.006 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "uganda": (round(1.725 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "ruanda": (round(1.984 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "esuatini": (round(1.779 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "lesoto": (round(1.909 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "etiopia": (round(1.117 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "egipto": (round(0.397 * USD_EUR, 3), GPP, GPP_FECHA, "Precio subvencionado."),
    "tunez": (round(0.748 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "argelia": (round(0.232 * USD_EUR, 3), GPP, GPP_FECHA, "Precio subvencionado."),
    "burundi": (round(1.308 * USD_EUR, 3), GPP, GPP_FECHA, "Escasez crónica de combustible."),
    "libia": (round(0.024 * USD_EUR, 3), GPP, GPP_FECHA, "Precio subvencionado: casi gratis."),
    "niger": (round(1.081 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "burkina-faso": (round(1.312 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "mali": (round(1.644 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "sudan": (round(0.656 * USD_EUR, 3), GPP, GPP_FECHA, ""),
    "rca": (round(2.186 * USD_EUR, 3), GPP, GPP_FECHA, ""),
}
# Países sin precio en GlobalPetrolPrices (Guinea Ecuatorial, Chad, Eritrea,
# Yibuti, Somalia, Sudán del Sur, Guinea-Bisáu): se usa este valor y se avisa.
GASOIL_SIN_DATO = 1.30

# ---------------------------------------------------------------- visados
# Por persona. (slug, € por visado, nº de visados, texto, fuente)
_MAEC = "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc="
# Por persona y por ENTRADA: la página multiplica por las veces que se entra en
# el país con la ruta elegida. slug: (€ por visado, texto, fuente)
VISADOS = {
    "mauritania": (55, "55 € · una entrada, 30 días", "https://www.diplomatie.gouv.fr/fr/information-par-pays/mauritanie/conseils-aux-voyageurs-entree-sejour"),
    "guinea": (round(100 * USD_EUR), "100 USD · eVisa de una entrada. Sin confirmar que valga en frontera terrestre", "https://www.paf.gov.gn/visa"),
    "costa-de-marfil": (50, "50 € + gastos bancarios · embajada en Madrid (la eVisa exige biometría en el aeropuerto de Abiyán)", _MAEC + "Costa%20de%20Marfil"),
    "ghana": (round(260 * USD_EUR), "260 USD · eVisa, estancia máxima 60 días", "https://www.exteriores.gob.es/Embajadas/accra/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"),
    "togo": (round(25000 * XOF_EUR), "25.000 FCFA · eVisa 1–15 días, una entrada. Ya no se da en frontera", "https://voyage.gouv.tg/about"),
    "benin": (50, "50 € · eVisa 30 días, una entrada (tarifa publicada en 2020)", "https://evisa.bj/articles/les-couts-des-visas-dentree-au-benin/8c948600-ca08-443e-bac9-33aae6583b54"),
    "nigeria": (250, "~250 € · eVisa de una entrada, 30 días", _MAEC + "Nigeria"),
    "camerun": (153, "153 € · eVisa normal (exprés 230 €)", "https://ambacamespagne.com/web/en/visa/"),
    "congo": (110, "110 € · 91 días, una entrada, en la embajada de París. Fuente no oficial (agencia)", _MAEC + "Congo"),
    "rd-congo": (200, "200 € · 3 meses, una entrada, en persona en Madrid. Validez desde la emisión: con salida en enero no llega a la subida de junio", "https://ambardcmadrid.com/visa/"),
    "malaui": (round(100 * USD_EUR), "100 USD · la exención de 2024 se revocó el 02-01-2026; importe del MAEC de 2022", "https://apta-africa.org/2026/01/14/malawi-visa-update/"),
    "tanzania": (round(50 * USD_EUR), "50 USD · eVisa. Dos si se entra otra vez al volver de Kenia", _MAEC + "Tanzania"),
    "kenia": (round(30 * USD_EUR), "30 USD · eTA de una entrada", "https://etakenya.go.ke/faqs"),
    "mozambique": (9, "Sin visado (30 días), pero ETA obligatorio: ~650 MZN según fuente no oficial", _MAEC + "Mozambique"),
    "zimbabue": (round(30 * USD_EUR), "30 USD · en frontera (KAZA Zambia + Zimbabue: 50 USD)", _MAEC + "Zimbabue"),
    "namibia": (78, "1.600 NAD · eVisa o en frontera", _MAEC + "Namibia"),
    # Resto de países (solo cuentan si la ruta pasa por ellos).
    "sierra-leona": (round(80 * USD_EUR), "~80 USD de referencia (visado a la llegada, 2026). Por tierra hace falta visado consular previo: importe por confirmar", "https://globe2me.com/blog/visa-sierra-leone"),
    "liberia": (100, "100 € una entrada · 200 € múltiple (MAEC). No sirve el e-visa del aeropuerto para la frontera terrestre", _MAEC + "Liberia"),
    "gabon": (110, "Tasa consular 109,60 € en París según agencia, sin gestión. El eVisa solo vale llegando en avión", "https://www.visatravel.fr/en/visas/gabon/"),
    "uganda": (round(50 * USD_EUR), "50 USD · eVisa de una entrada", "https://immigration.go.ug/services/tourist-visa"),
    "ruanda": (round(50 * USD_EUR), "50 USD una entrada · 70 USD múltiple (MAEC)", _MAEC + "Ruanda"),
    "guinea-ecuatorial": (105, "105 € · eVisa previa", _MAEC + "Guinea%20Ecuatorial"),
    "etiopia": (round(82 * USD_EUR), "82 USD · eVisa 30 días; pensada para el aeropuerto, confirmar en frontera terrestre", _MAEC + "Etiop%C3%ADa"),
    "egipto": (round(30 * USD_EUR), "30 USD · a la llegada", _MAEC + "Egipto"),
    "yibuti": (round(23 * USD_EUR), "23 USD estancia corta (12 USD tránsito) · eVisa", "https://www.evisa.gouv.dj/"),
    "argelia": (65, "~65 € · presencial en Madrid; confirmar tarifa", _MAEC + "Argelia"),
    "chad": (134, "134 € según agencia (tasa oficial sin publicar) · solo eVisa desde mayo de 2026", _MAEC + "Chad"),
    "rca": (50, "~50 € orientativos · embajada en París", _MAEC + "Rep%C3%BAblica%20Centroafricana"),
    "sudan-del-sur": (round(100 * USD_EUR), "100 USD para pasaportes europeos", _MAEC + "Sud%C3%A1n%20del%20Sur"),
    "somalia": (round(60 * USD_EUR), "60 USD en efectivo, una entrada", _MAEC + "Somalia"),
    "eritrea": (round(120 * USD_EUR), "~70 USD a la llegada con carta de invitación + ~50 USD de gestión del operador", _MAEC + "Eritrea"),
    "burundi": (round(90 * USD_EUR), "90 USD · eVisa de un mes", _MAEC + "Burundi"),
    "burkina-faso": (50, "33.000 FCFA una entrada (~50 €) · eVisa", _MAEC + "Burkina%20Faso"),
    "libia": (round(63 * USD_EUR), "63 USD la eVisa; además obliga a ir con una agencia libia (de 1.100 € por 3 días a 2.850 € por 11), que no está incluida", _MAEC + "Libia"),
    "niger": (0, "Importe por confirmar (embajada en Bruselas)", _MAEC + "N%C3%ADger"),
}
SIN_VISADO = ["marruecos", "sahara-occidental", "senegal", "gambia", "angola", "cabinda", "zambia", "botsuana",
              "sudafrica", "esuatini", "lesoto", "tunez"]

# ---------------------------------------------------------------- vehículo
# El CPD va por vehículo en VEHICULOS (cpd_libro, cpd_aval, cpd_banco).

# Tasas de importación temporal en frontera, por vehículo y por ENTRADA, a
# partir de data_cpd. La página multiplica por las entradas de la ruta elegida.
# Donde no hay dato vale 0 y lo dice. slug: (€ por entrada, texto)
TASAS = {
    "mauritania": (10, "~10 € por entrada"),
    "senegal": (8, "5.000 FCFA por entrada si el vehículo tiene 8 años o menos; ~250 € si los supera"),
    "gambia": (10, "~11 USD (dato de 2023)"),
    "guinea": (5, "Gratis en 2023 · ~5 € en 2017"),
    "costa-de-marfil": (0, "Sin dato posterior a 2023"),
    "ghana": (12, "~12 € como excepción con CPD; sin CPD, ~490 USD con localizador (2023)"),
    "togo": (10, "~11 USD (2023)"),
    "benin": (14, "~16 USD (2023)"),
    "nigeria": (0, "Gratis en 2023 · importe de 2026 sin publicar"),
    "camerun": (13, "~15 USD (2023)"),
    "congo": (0, "Sin tarifa pública localizada"),
    "rd-congo": (0, "Sin tarifa pública localizada"),
    "angola": (43, "43.236,78 AOA por entrada (aviso oficial de julio de 2025)"),
    "cabinda": (43, "Como Angola: 43.236,78 AOA por entrada"),
    "zambia": (70, "~60–100 USD (datos de 2014–2019)"),
    "malaui": (30, "TIP 5.000–10.000 MWK + 20 USD de RAF"),
    "tanzania": (26, "25 USD/mes + 5 USD (dato de 2014)"),
    "kenia": (50, "FVP de 21 a 101 USD según cilindrada y plazo (cifras de 2018, no oficiales)"),
    "mozambique": (17, "~11–17 € (2026)"),
    "zimbabue": (50, "~45–70 USD"),
    "botsuana": (11, "~8–11 €"),
    "namibia": (27, "N$534 por entrada"),
}

# ---------------------------------------------------------------- partidas
# (id, etiqueta, valor, unidad, ámbito, tipo, nota)
#   ámbito: "vehiculo" (por vehículo), "persona", "perro", "total"
#   tipo: "dato" (fuente citada) o "estimacion" (valor inicial a ajustar)
# Ferry Barcelona – Tánger Med (GNV). Tarifas «desde» del calendario de
# salidas de gnv.it, consultado el 26-09-2026, para coche de clase A2 (alto de
# 1,90 a 2,79 m y largo hasta 4,99 m: un 4x4 con tienda de techo), camarote.
#   Ida 10-01-2027: 2 adultos + coche 485,17 € (butaca 432,04 €)
#                   1 adulto  + coche 403,85 € (butaca 327,50 €)
#   Vuelta Tánger → Barcelona: julio y agosto de 2027 aún no están a la venta.
#   Referencia: salidas de abril-mayo de 2027, 2 adultos + coche 446,34 €
#   (butaca 396,16 €); 1 adulto + coche 369,14 € (butaca 298,52 €).
FERRY = {
    "ida": {"v1": 485.17, "v2": 403.85},
    "vuelta": {"v1": 446.34, "v2": 369.14},
    "fecha": "26-09-2026",
    "fuente": "https://www.gnv.it/es/departures-calendar?type=outward",
    "filas": [
        ("INEOS Grenadier · 2 adultos + coche + perro", "10 ene 2027", "485,17 € camarote · 432,04 € butaca",
         "446,34 € camarote · 396,16 € butaca"),
        ("Delica · 1 adulto + coche", "10 ene 2027", "403,85 € camarote · 327,50 € butaca",
         "369,14 € camarote · 298,52 € butaca"),
    ],
}
# Perro: con él a bordo hay que reservar camarote «pet-friendly» (máximo 2
# mascotas) o dejarlo en la perrera; no puede quedarse en el vehículo. GNV no
# publica el precio de la mascota ni el suplemento del camarote pet-friendly:
# ~100 € por trayecto es una estimación a partir de agencias (30-50 € mascota +
# 50-80 € de suplemento).
PERRO_FERRY = 100

PARAMETROS = [
    ("comida", "Comida y agua de boca", 12, "€ / persona / día", "persona_dia", "estimacion",
     "Compra en mercado y supermercado cocinando en el vehículo, con alguna comida fuera."),
    ("perro_comida", "Comida del perro", 1.5, "€ / perro / día", "perro_dia", "estimacion", ""),
    ("noche", "Camping, pernocta o parking vigilado", 6, "€ / vehículo / noche", "vehiculo_dia", "estimacion",
     "Media entre acampada libre (0 €), camping (5–15 €) y alguna noche de hotel en capitales."),
    ("parques", "Parques, guías y actividades", 600, "€ / persona / viaje", "persona", "estimacion",
     "Odzala y gorilas, Etosha, Okavango, etc. Solo las tasas de Odzala con gorilas pueden superar esta cifra."),
    ("perro_tramites", "Certificados y permisos del perro", 500, "€ / viaje", "perro", "estimacion",
     "No hay cifra consolidada: suma de certificados veterinarios refrendados y permisos de importación de unos 20 países (Kenia: ~50 USD vía embajada)."),
    ("seguros", "Seguros del vehículo en ruta", 400, "€ / vehículo / viaje", "vehiculo", "estimacion",
     "Carte Brune CEDEAO (sin tarifa pública), seguros locales en Mauritania y África central, y Yellow Card COMESA (~80–150 USD, dato de viajeros)."),
    ("mantenimiento", "Mantenimiento, recambios y neumáticos", 1200, "€ / vehículo / viaje", "vehiculo", "estimacion", ""),
    ("comunicaciones", "SIM locales y datos", 20, "€ / vehículo / mes", "vehiculo_mes", "estimacion", ""),
    ("imprevistos", "Imprevistos", 10, "% del total", "pct", "estimacion",
     "Multas, sobornos rechazados que acaban en tasa, reparaciones, cambios de ruta."),
]

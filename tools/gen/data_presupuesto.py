# -*- coding: utf-8 -*-
"""Presupuesto del viaje por vehículo.

Planteamiento pedido por el propietario (25-09-2026):
  · Vehículo 1: 2 personas y el perro, consumo medio 15 L/100 km.
  · Vehículo 2: 1 persona, consumo medio 12 L/100 km.

La página /presupuesto/ es una calculadora: todos los valores de aquí son los
valores iniciales y se pueden cambiar en la propia página (se guardan solo en
ese navegador). Cada cifra lleva su fuente o dice que es una estimación.

Los kilómetros NO están aquí: se calculan al construir el sitio a partir de los
corredores dibujados en cada ficha (distancia en línea recta entre vértices) y
se corrigen con FACTOR_CARRETERA y DESVIOS_PCT.
"""

FECHA = "25 de septiembre de 2026"

# Tipo de cambio implícito en GlobalPetrolPrices del 21-09-2026
# (Marruecos: 1,603 USD = 1,400 EUR). El franco CFA es fijo.
USD_EUR = round(1.400 / 1.603, 4)          # 0,8734 € por dólar
XOF_EUR = 1 / 655.957

VEHICULOS = [
    {"id": "v1", "nombre": "Vehículo 1", "detalle": "2 personas + perro", "personas": 2, "perros": 1, "l100": 15.0},
    {"id": "v2", "nombre": "Vehículo 2", "detalle": "1 persona", "personas": 1, "perros": 0, "l100": 12.0},
]

# Fechas del portal: salida 10 ene 2027, regreso ~15 ago 2027 → 217 días.
# La planificación manuscrita pone la última entrada en Marruecos el 20 jul, lo
# que llevaría el regreso a finales de julio (unos 200 días).
DIAS = 217

# Distancia real por carretera ≈ línea recta × factor. 1,25 es un valor medio
# habitual para redes secundarias; en pista de montaña o selva es mayor.
FACTOR_CARRETERA = 1.25
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
}

# ---------------------------------------------------------------- tramos
# (slug, clave del corredor, veces, etiqueta, activo por defecto, nota)
# clave: "corridor", "corridor_alt", "corridor+alt" (los dos seguidos forman
# una sola pasada), "extra:<n>" (índice en extra_corridors) o una lista de
# puntos propia cuando la ficha no dibuja ese trayecto.
MARRUECOS_DIRECTO = [(35.8900, -5.5000), (34.0209, -6.8416), (33.5731, -7.5898), (31.6295, -7.9811),
                     (30.4278, -9.5981), (28.9870, -10.0574), (28.4378, -11.1032), (27.9394, -12.9231)]
MAURITANIA_COSTA = [(16.2158, -16.4148), (18.0858, -15.9785), (19.8784, -16.3044), (20.9300, -17.0330),
                    (21.3337, -16.9472)]
TRAMOS = [
    ("marruecos", MARRUECOS_DIRECTO, 1, "Bajada: Tánger Med → Tarfaya por la vía rápida", True,
     "El índice de países dice «de paso, ruta más rápida, sin paradas». La ficha de Marruecos dibuja en cambio un bucle turístico (fila de más abajo): hay que decidir cuál vale."),
    ("marruecos", MARRUECOS_DIRECTO, 1, "Subida: Tarfaya → Tánger Med por la vía rápida", True, ""),
    ("marruecos", "corridor", 1, "Bucle de la ficha (Fez, Merzouga, Todra, Marrakech, costa)", False, "Sustituye a la bajada por la vía rápida si se hace."),
    ("sahara-occidental", "corridor", 1, "Bajada", True, ""),
    ("sahara-occidental", "corridor_alt", 1, "Subida", True, ""),
    ("mauritania", "corridor+alt", 1, "Bajada por el Adrar (Guerguerat → Atar → Uadane → Nuakchot → Diama)", True, ""),
    ("mauritania", "corridor+alt", 1, "Subida por el mismo corredor del Adrar", True, "La ficha dice «mismo corredor previsto a la vuelta»."),
    ("mauritania", MAURITANIA_COSTA, 1, "Subida directa por la costa (Diama → Nuakchot → Nuadibú → Guerguerat)", False, "Alternativa a la fila anterior."),
    ("senegal", "corridor", 1, "Bajada por el este (Ferlo, Niokolo-Koba, Kédougou)", True, ""),
    ("senegal", "corridor_alt", 1, "Subida por Casamance, Saloum y Dakar", True, ""),
    ("gambia", "corridor", 1, "Eje costero (subida)", True, ""),
    ("gambia", "corridor_alt", 1, "Variante río arriba", False, ""),
    ("guinea", "corridor", 1, "Bajada", True, ""),
    ("guinea", "corridor_alt", 1, "Subida", True, ""),
    ("costa-de-marfil", "corridor", 1, "Bajada", True, ""),
    ("costa-de-marfil", "corridor_alt", 1, "Subida", True, ""),
    ("ghana", "corridor", 1, "Bajada", True, ""),
    ("ghana", "corridor_alt", 1, "Subida", True, ""),
    ("togo", "corridor", 1, "Bajada por la costa", True, ""),
    ("togo", "corridor_alt", 1, "Subida por el interior", True, ""),
    ("benin", "corridor", 1, "Bajada por la costa", True, ""),
    ("benin", "corridor_alt", 1, "Subida por el interior", True, ""),
    ("nigeria", "corridor", 1, "Bajada", True, ""),
    ("nigeria", "corridor_alt", 1, "Subida", True, ""),
    ("camerun", "corridor", 1, "Bajada", True, ""),
    ("camerun", "corridor_alt", 1, "Subida", True, ""),
    ("congo", "corridor", 1, "Bajada (Odzala y gorilas)", True, ""),
    ("congo", "corridor_alt", 1, "Subida por Cabinda", True, ""),
    ("rd-congo", "corridor", 1, "Bajada (Kongo Central)", True, ""),
    ("rd-congo", "corridor_alt", 1, "Subida (Kongo Central)", True, ""),
    ("angola", "corridor", 1, "Bajada", True, ""),
    ("angola", "corridor_alt", 1, "Subida", True, ""),
    ("angola", "extra:0", 1, "Cabinda, bajada", True, ""),
    ("angola", "extra:1", 1, "Cabinda, subida", True, ""),
    ("zambia", "corridor", 1, "Travesía principal", True, ""),
    ("zambia", "corridor_alt", 1, "Variante sur (cataratas Victoria)", False, ""),
    ("malaui", "corridor", 1, "Bucle completo", True, "Está en la planificación manuscrita (1 abr), aunque el índice de países aún lo lista como alternativa."),
    ("tanzania", "corridor", 1, "Interior hacia Kenia", True, "Solo si se va a Kenia. La planificación manuscrita pone Tanzania una sola vez (16 abr) y todavía no encaja Kenia."),
    ("tanzania", "corridor_alt", 1, "Costa desde Kenia hacia Mozambique", True, ""),
    ("kenia", "corridor", 1, "Entrada, Rift y norte", True, "Sin fecha en la planificación manuscrita."),
    ("kenia", "corridor_alt", 1, "Salida por la costa", True, ""),
    ("mozambique", "corridor", 1, "Eje costero (Rovuma → Ponta do Ouro → Machipanda)", True, ""),
    ("mozambique", "corridor_alt", 1, "Variante interior del Zambeze", False, ""),
    ("zimbabue", "corridor", 1, "Diagonal sur", True, ""),
    ("zimbabue", "corridor_alt", 1, "Variante norte (Zambeze, Mana Pools, Kariba)", False, ""),
    ("botsuana", "corridor", 1, "Eje norte–sur (Chobe, Okavango, salinas)", True, ""),
    ("botsuana", "corridor_alt", 1, "Variante oeste (Tsodilo, Kalahari Central)", False, ""),
    ("sudafrica", "corridor", 1, "Entrada por el centro y el este", True, ""),
    ("sudafrica", "corridor_alt", 1, "Salida por la costa oeste", True, ""),
    ("namibia", "corridor", 1, "Eje interior (Windhoek, Waterberg, Etosha)", True, ""),
    ("namibia", "corridor_alt", 1, "Variante costera y 4x4 (Namib, Skeleton Coast, Kaokoland)", False, ""),
]

# ---------------------------------------------------------------- visados
# Por persona. (slug, € por visado, nº de visados, texto, fuente)
_MAEC = "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc="
VISADOS = [
    ("mauritania", 55, 2, "55 € · una entrada, 30 días", "https://www.diplomatie.gouv.fr/fr/information-par-pays/mauritanie/conseils-aux-voyageurs-entree-sejour"),
    ("guinea", round(100 * USD_EUR), 2, "100 USD · eVisa de una entrada. Sin confirmar que valga en frontera terrestre", "https://www.paf.gov.gn/visa"),
    ("costa-de-marfil", 50, 2, "50 € + gastos bancarios · embajada en Madrid (la eVisa exige biometría en el aeropuerto de Abiyán)", _MAEC + "Costa%20de%20Marfil"),
    ("ghana", round(260 * USD_EUR), 2, "260 USD · eVisa, estancia máxima 60 días", "https://www.exteriores.gob.es/Embajadas/accra/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"),
    ("togo", round(25000 * XOF_EUR), 2, "25.000 FCFA · eVisa 1–15 días, una entrada. Ya no se da en frontera", "https://voyage.gouv.tg/about"),
    ("benin", 50, 2, "50 € · eVisa 30 días, una entrada (tarifa publicada en 2020)", "https://evisa.bj/articles/les-couts-des-visas-dentree-au-benin/8c948600-ca08-443e-bac9-33aae6583b54"),
    ("nigeria", 250, 2, "~250 € · eVisa de una entrada, 30 días", _MAEC + "Nigeria"),
    ("camerun", 153, 2, "153 € · eVisa normal (exprés 230 €)", "https://ambacamespagne.com/web/en/visa/"),
    ("congo", 110, 2, "110 € · 91 días, una entrada, en la embajada de París. Fuente no oficial (agencia)", _MAEC + "Congo"),
    ("rd-congo", 200, 2, "200 € · 3 meses, una entrada, en persona en Madrid. Validez desde la emisión: con salida en enero no llega a la subida de junio", "https://ambardcmadrid.com/visa/"),
    ("malaui", round(100 * USD_EUR), 1, "100 USD · la exención de 2024 se revocó el 02-01-2026; importe del MAEC de 2022", "https://apta-africa.org/2026/01/14/malawi-visa-update/"),
    ("tanzania", round(50 * USD_EUR), 2, "50 USD · eVisa. Dos si se entra otra vez al volver de Kenia", _MAEC + "Tanzania"),
    ("kenia", round(30 * USD_EUR), 1, "30 USD · eTA de una entrada", "https://etakenya.go.ke/faqs"),
    ("mozambique", 9, 1, "Sin visado (30 días), pero ETA obligatorio: ~650 MZN según fuente no oficial", _MAEC + "Mozambique"),
    ("zimbabue", round(30 * USD_EUR), 1, "30 USD · en frontera (KAZA Zambia + Zimbabue: 50 USD)", _MAEC + "Zimbabue"),
    ("namibia", 78, 1, "1.600 NAD · eVisa o en frontera", _MAEC + "Namibia"),
]
SIN_VISADO = ["marruecos", "sahara-occidental", "senegal", "gambia", "angola", "zambia", "botsuana", "sudafrica"]

# ---------------------------------------------------------------- vehículo
# Por vehículo. CPD según data_cpd.COSTE_CPD (RACE).
CPD_EMISION = 230
CPD_COMISION_AVAL = 100
CPD_AVAL = 2780          # inmovilizado, no es gasto

# Tasas de importación temporal en frontera, por vehículo, a partir de
# data_cpd (importe × entradas). (slug, €, texto)
TASAS_FRONTERA = [
    ("mauritania", 20, "~10 € × 2 entradas"),
    ("senegal", 24, "5.000 FCFA × 3 entradas si el vehículo tiene 8 años o menos; ~250 € por entrada si los supera"),
    ("gambia", 10, "~11 USD (dato de 2023)"),
    ("guinea", 10, "Gratis en 2023 · ~5 € en 2017; 2 entradas"),
    ("costa-de-marfil", 0, "Sin dato posterior a 2023"),
    ("ghana", 24, "~12 € × 2 como excepción con CPD; sin CPD, ~490 USD con localizador (2023)"),
    ("togo", 19, "~11 USD × 2 (2023)"),
    ("benin", 28, "~16 USD × 2 (2023)"),
    ("nigeria", 0, "Gratis en 2023 · importe de 2026 sin publicar"),
    ("camerun", 26, "~15 USD × 2 (2023)"),
    ("congo", 0, "Sin tarifa pública localizada"),
    ("rd-congo", 0, "Sin tarifa pública localizada"),
    ("angola", 173, "43.236,78 AOA por entrada × 4 (aviso oficial de julio de 2025)"),
    ("zambia", 70, "~60–100 USD (datos de 2014–2019)"),
    ("malaui", 30, "TIP 5.000–10.000 MWK + 20 USD de RAF"),
    ("tanzania", 26, "25 USD/mes + 5 USD (dato de 2014)"),
    ("kenia", 50, "FVP de 21 a 101 USD según cilindrada y plazo (cifras de 2018, no oficiales)"),
    ("mozambique", 17, "~11–17 € (2026)"),
    ("zimbabue", 50, "~45–70 USD"),
    ("botsuana", 11, "~8–11 €"),
    ("namibia", 27, "N$534 por entrada"),
]

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
        ("Vehículo 1 · 2 adultos + coche + perro", "10 ene 2027", "485,17 € camarote · 432,04 € butaca",
         "446,34 € camarote · 396,16 € butaca"),
        ("Vehículo 2 · 1 adulto + coche", "10 ene 2027", "403,85 € camarote · 327,50 € butaca",
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

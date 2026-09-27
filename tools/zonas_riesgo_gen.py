#!/usr/bin/env python3
"""Genera tools/gen/zonas_riesgo.json: zonas desaconsejadas DENTRO de los países
(para el Planificador por puntos), a partir de los avisos del FCDO británico
(gov.uk, «advise against all travel» = rojo, «all but essential travel» =
naranja), revisados el 27-09-2026. Los países enteros en conflicto (Malí,
Níger, Chad, Sudán…) ya se pintan aparte y no están aquí.

Se ejecuta a mano cuando cambian los avisos (no lo usa build.py):
    pip install shapely
    curl -o /tmp/adm1.json https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_1_states_provinces.geojson
    python3 tools/zonas_riesgo_gen.py /tmp/adm1.json

Geometría: franjas fronterizas sobre assets/js/africa.geo.json (la misma que usa
el planificador), regiones de Natural Earth (admin-1) y, donde el aviso habla de
comarcas, distritos o líneas entre pueblos, polígonos aproximados a mano. Todas
las zonas son orientativas: el aviso oficial manda.
"""
import json
import math
import sys
from pathlib import Path

from shapely.geometry import LineString, Point, Polygon, box, mapping, shape
from shapely.ops import unary_union
from shapely.affinity import scale

RAIZ = Path(__file__).resolve().parents[1]
GEO = json.loads((RAIZ / "assets/js/africa.geo.json").read_text(encoding="utf-8"))
ADM = json.loads(Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/adm1.json").read_text(encoding="utf-8"))
FECHA = "27-09-2026"
FCDO = "https://www.gov.uk/foreign-travel-advice/"

PAIS = {f["properties"]["slug"]: shape(f["geometry"]).buffer(0) for f in GEO["features"]}
NE = {"mauritania": "Mauritania", "nigeria": "Nigeria", "camerun": "Cameroon", "rd-congo": "Democratic Republic of the Congo",
      "mozambique": "Mozambique", "kenia": "Kenya", "etiopia": "Ethiopia", "egipto": "Egypt", "tunez": "Tunisia", "togo": "Togo",
      "benin": "Benin", "costa-de-marfil": "Ivory Coast", "angola": "Angola", "burundi": "Burundi", "congo": "Republic of the Congo",
      "argelia": "Algeria"}
REG = {}
for f in ADM["features"]:
    p = f["properties"]
    REG.setdefault(p["admin"], {})[p["name"]] = shape(f["geometry"]).buffer(0)


def reg(pais, *nombres):
    d = REG[NE[pais]]
    return unary_union([d[n] for n in nombres])


def km2deg(g, km, lat0):
    """Buffer en km (aprox. equirectangular alrededor de lat0)."""
    k = math.cos(math.radians(lat0))
    s = scale(g, xfact=k, yfact=1, origin=(0, 0))
    return scale(s.buffer(km / 111.32, resolution=8), xfact=1 / k, yfact=1, origin=(0, 0))


def franja(pais, vecino, km):
    c = PAIS[pais]
    return c.intersection(km2deg(PAIS[vecino], km, c.centroid.y))


def circulo(lat, lon, km):
    return km2deg(Point(lon, lat), km, lat)


def pol(*pts):
    """Polígono con puntos (lat, lon)."""
    return Polygon([(lo, la) for la, lo in pts])


def linea(*pts):
    return LineString([(lo, la) for la, lo in pts])


Z = []


def zona(pais, nivel, nombre, geom, texto, slug, aprox=False):
    g = geom.intersection(PAIS[pais]).buffer(0)
    if g.is_empty:
        print("VACÍA", pais, nombre)
        return
    Z.append({"pais": pais, "nivel": nivel, "nombre": nombre, "g": g, "texto": texto,
              "fuente": FCDO + slug, "fecha": FECHA, "aprox": aprox, "organismo": "FCDO"})


# ---------------------------------------------------------------- Mauritania
M = PAIS["mauritania"]
este = pol((14.0, -11.524), (15.93, -11.524), (18.351, -9.191), (21.594, -10.602), (22.73, -12.47), (22.68, -12.71),
           (22.68, -14.5), (28.5, -14.5), (28.5, -3.0), (14.0, -3.0))
maur_rojo = unary_union([este, franja("mauritania", "mali", 25)])
zona("mauritania", "rojo", "Este y norte de Mauritania", este,
     "Todo viaje desaconsejado al este de la línea Kankossa – Akhreijit – Ghallaouiya – Zuérat – F'Dérik y de ahí al oeste "
     "hasta el Sáhara Occidental (sin incluir esos pueblos).", "mauritania", aprox=True)
zona("mauritania", "rojo", "Franja de 25 km con Malí (sur)", franja("mauritania", "mali", 25),
     "Todo viaje desaconsejado a menos de 25 km de la frontera de Malí en el sur, incluido Khabou.", "mauritania")
ne_linea2 = pol((21.299, -13.067), (20.934, -11.617), (18.667, -10.0), (14.0, -10.0), (14.0, -3.0), (28.5, -3.0), (28.5, -13.067))
naranja_m = unary_union([reg("mauritania", "Tiris Zemmour", "Assaba", "Hodh el Gharbi", "Gorgol", "Guidimaka"),
                         reg("mauritania", "Adrar", "Tagant").intersection(ne_linea2)]).difference(maur_rojo)
zona("mauritania", "naranja", "Tiris Zemmour, Assaba, Hodh el Gharbi, Gorgol, Guidimaka y este de Adrar y Tagant", naranja_m,
     "Solo viajes esenciales. Quedan fuera (sin aviso) el oeste de la línea Choum – Uadane – (10° O, 18°40' N), Uadane, "
     "las carreteras Tidjikja–Tichit y Aleg–Tidjikja por Moudjeria y la carretera Bogué–Kaédi por Bababé.", "mauritania", aprox=True)
zona("mauritania", "naranja", "Franja de 25 km con el Sáhara Occidental",
     franja("mauritania", "sahara-occidental", 25).difference(box(-17.5, 19.0, -16.2, 21.5)).difference(maur_rojo),
     "Solo viajes esenciales a menos de 25 km del Sáhara Occidental, salvo la carretera Nuakchot–Nuadibú y Nuadibú.", "mauritania", aprox=True)

# ---------------------------------------------------------------- Sáhara Occidental (muro)
BERM = linea((27.67, -8.67), (27.25, -9.35), (26.85, -10.1), (26.45, -10.9), (26.0, -11.45), (25.45, -12.0), (24.9, -12.55),
             (24.3, -13.05), (23.7, -13.55), (23.1, -13.9), (22.5, -14.2), (21.95, -14.75), (21.6, -15.6), (21.4, -16.4), (21.34, -16.93))
ESTE_BERM = pol((27.67, -8.67), (27.25, -9.35), (26.85, -10.1), (26.45, -10.9), (26.0, -11.45), (25.45, -12.0), (24.9, -12.55),
                (24.3, -13.05), (23.7, -13.55), (23.1, -13.9), (22.5, -14.2), (21.95, -14.75), (21.6, -15.6), (21.4, -16.4),
                (21.34, -16.93), (20.5, -16.93), (20.5, -8.0), (28.0, -8.0))
zona("sahara-occidental", "rojo", "Al sur y este del muro (Berm)", ESTE_BERM,
     "Todo viaje desaconsejado al territorio al sur y al este del muro («the Berm»).", "western-sahara", aprox=True)
zona("sahara-occidental", "rojo", "40 km al norte y oeste del muro",
     km2deg(BERM, 40, 25).difference(ESTE_BERM).difference(box(-17.5, 20.5, -16.0, 22.4)),
     "Todo viaje desaconsejado a menos de 40 km al norte y al oeste del muro, incluida Smara. El paso de Guerguerat y la carretera "
     "de la costa quedan fuera en este dibujo.", "western-sahara", aprox=True)

# ---------------------------------------------------------------- Costa de Marfil
zona("costa-de-marfil", "rojo", "Franja de 40 km con Burkina Faso y Malí",
     unary_union([franja("costa-de-marfil", "burkina-faso", 40), franja("costa-de-marfil", "mali", 40)]),
     "Todo viaje desaconsejado a menos de 40 km de Burkina Faso y Malí.", "cote-d-ivoire")
zona("costa-de-marfil", "rojo", "Norte de Zanzan y de Savanes",
     reg("costa-de-marfil", "Zanzan", "Savanes").intersection(box(-9, 9.3, 0, 11.5)),
     "Todo viaje desaconsejado al norte de las regiones de Zanzan y Savanes (el FCDO no da la línea: dibujada al norte de 9,3° N).", "cote-d-ivoire", aprox=True)
zona("costa-de-marfil", "rojo", "Parque Nacional de la Comoé", circulo(8.75, -3.8, 50), "Todo viaje desaconsejado al Parque Nacional de la Comoé.", "cote-d-ivoire", aprox=True)
zona("costa-de-marfil", "naranja", "Franja de 20 km con Liberia", franja("costa-de-marfil", "liberia", 20),
     "Solo viajes esenciales a menos de 20 km de Liberia.", "cote-d-ivoire")

# ---------------------------------------------------------------- Ghana, Togo, Benín
zona("ghana", "naranja", "Bawku (Upper East)", circulo(11.06, -0.24, 15), "Solo viajes esenciales al municipio de Bawku.", "ghana", aprox=True)
tg_rojo = franja("togo", "burkina-faso", 30).difference(circulo(10.86, 0.21, 6))
zona("togo", "rojo", "Franja de 30 km con Burkina Faso", tg_rojo, "Todo viaje desaconsejado a menos de 30 km de Burkina Faso, salvo Dapaong y la N1 hasta allí.", "togo")
zona("togo", "naranja", "Resto de la región de Savanes", reg("togo", "Savanes").difference(tg_rojo), "Solo viajes esenciales al resto de Savanes.", "togo")
bj_rojo = unary_union([circulo(11.75, 2.45, 45), reg("benin", "Alibori").intersection(box(2.0, 11.55, 4.0, 12.6)),
                       circulo(11.15, 1.5, 38), franja("benin", "burkina-faso", 5)])
zona("benin", "rojo", "Parque W, Pendjari y franja de Burkina Faso", bj_rojo,
     "Todo viaje desaconsejado al Parque W (y zonas de caza de Mékrou y Djona, hasta la frontera de Níger), al Parque de la Pendjari "
     "y a menos de 5 km de Burkina Faso.", "benin", aprox=True)
rnie2 = pol((8.89, 2.60), (9.34, 2.63), (10.3, 2.75), (11.13, 2.94), (11.86, 3.39), (12.5, 3.9), (12.5, 4.5), (8.5, 4.5), (8.5, 2.60))
zona("benin", "naranja", "Entre la RNIE 2 y Nigeria, y resto de Alibori y Atacora",
     unary_union([rnie2, reg("benin", "Alibori", "Atakora")]).difference(bj_rojo),
     "Solo viajes esenciales entre la RNIE 2 (Tchaourou–Malanville) y la frontera de Nigeria y al resto de Alibori y Atacora.", "benin", aprox=True)

# ---------------------------------------------------------------- Nigeria
zona("nigeria", "rojo", "Borno, Yobe, Adamawa, Gombe, Katsina y Zamfara", reg("nigeria", "Borno", "Yobe", "Adamawa", "Gombe", "Katsina", "Zamfara"),
     "Todo viaje desaconsejado a estos estados (y a las zonas fluviales solo accesibles en barco del delta del Níger).", "nigeria")
zona("nigeria", "naranja", "Norte y centro (15 estados) y delta del Níger",
     reg("nigeria", "Bauchi", "Kaduna", "Kano", "Kebbi", "Jigawa", "Sokoto", "Niger", "Kogi", "Plateau", "Taraba", "Kwara", "Benue",
         "Abia", "Anambra", "Imo", "Delta", "Bayelsa", "Rivers"),
     "Solo viajes esenciales a Bauchi, Kaduna, Kano, Kebbi, Jigawa, Sokoto, Niger, Kogi, Plateau, Taraba, Kwara, Benue, Abia, Anambra, "
     "Imo y las zonas no fluviales de Delta, Bayelsa y Rivers.", "nigeria")

# ---------------------------------------------------------------- Camerún
maroua = unary_union([circulo(10.59, 14.32, 20), circulo(10.33, 14.32, 12)])
cm_rojo = unary_union([circulo(4.6, 8.6, 25), franja("camerun", "rca", 40), franja("camerun", "chad", 40),
                       franja("camerun", "nigeria", 40).difference(circulo(9.30, 13.40, 12)),
                       reg("camerun", "Nord-Ouest"), reg("camerun", "Sud-Ouest").difference(circulo(4.02, 9.20, 10)),
                       reg("camerun", "Extrême-Nord").difference(maroua)])
zona("camerun", "rojo", "Noroeste, Suroeste, Extremo Norte y franjas de Nigeria, Chad y RCA", cm_rojo,
     "Todo viaje desaconsejado: regiones Noroeste y Suroeste (salvo Limbé), Extremo Norte (salvo Maroua), península de Bakassi "
     "y 40 km de las fronteras de Nigeria (salvo Garoua), Chad y RCA.", "cameroon", aprox=True)
zona("camerun", "naranja", "Región Norte, Maroua, Limbé y sur de Adamaoua",
     unary_union([reg("camerun", "Nord"), maroua, circulo(4.02, 9.20, 10),
                  reg("camerun", "Adamaoua").intersection(km2deg(reg("camerun", "Nord"), 20, 8))]).difference(cm_rojo),
     "Solo viajes esenciales a la región Norte (con Garoua), a Maroua y alrededores, a Limbé y la N3 hasta el Litoral, y a 20 km "
     "del límite con la región Norte en Adamaoua.", "cameroon", aprox=True)

# ---------------------------------------------------------------- Congo, RD Congo, Angola
zona("congo", "rojo", "Franja de 50 km con la RCA (Likouala)", franja("congo", "rca", 50), "Todo viaje desaconsejado a menos de 50 km de la RCA en Likouala.", "congo")
orientale = REG[NE["rd-congo"]]["Orientale"]
katanga = REG[NE["rd-congo"]]["Katanga"]
cd_rojo = unary_union([franja("rd-congo", "rca", 50), reg("rd-congo", "Nord-Kivu", "Sud-Kivu", "Maniema"),
                       orientale.intersection(box(28.6, 0.4, 32, 3.6)),   # Ituri (aprox.)
                       orientale.intersection(box(26.2, 2.3, 31.5, 5.4)),  # Haut-Uélé (aprox.)
                       katanga.intersection(box(26.2, -8.3, 31, -4.9)),    # Tanganyika (aprox.)
                       katanga.intersection(box(24.4, -10.3, 27.4, -7.2)),  # Haut-Lomami (aprox.)
                       pol((-3.18, 16.20), (-3.32, 17.37), (-4.4, 17.6), (-4.35, 16.0))])  # Kwamouth
zona("rd-congo", "rojo", "Este (Kivu, Ituri, Maniema, Haut-Uélé, Tanganyika, Haut-Lomami), Kwamouth y franja de la RCA", cd_rojo,
     "Todo viaje desaconsejado a Haut-Uélé, Ituri, Kivu Norte y Sur, Maniema, Tanganyika y Haut-Lomami, al territorio de Kwamouth "
     "(Mai-Ndombe) y a 50 km de la RCA. Las provincias nuevas se dibujan sobre las antiguas: límites aproximados.", "democratic-republic-of-the-congo", aprox=True)
zona("rd-congo", "naranja", "N1 Menkao–Kenge y Upemba", unary_union([box(16.3, -5.2, 17.6, -4.1), circulo(-9.0, 26.5, 45)]).difference(cd_rojo),
     "Solo viajes esenciales a la N1 entre Menkao y Kenge (Kinshasa) y al Parque Nacional de Upemba.", "democratic-republic-of-the-congo", aprox=True)
zona("angola", "naranja", "Provincia de Cabinda (salvo la ciudad)", reg("angola", "Cabinda").difference(circulo(-5.55, 12.2, 8)),
     "Solo viajes esenciales a la provincia de Cabinda, salvo la ciudad de Cabinda.", "angola")

# ---------------------------------------------------------------- Mozambique, Tanzania
mz_ok = unary_union([circulo(-12.97, 40.52, 15), circulo(-10.78, 40.47, 6), circulo(-10.83, 40.50, 8)])
mz_rojo = unary_union([reg("mozambique", "Cabo Delgado").difference(mz_ok),
                       reg("mozambique", "Nampula").intersection(box(39.7, -14.9, 40.9, -13.85)),
                       reg("mozambique", "Niassa").intersection(box(37.0, -13.7, 38.6, -11.55))])
zona("mozambique", "rojo", "Cabo Delgado, Memba y Eráti, Mecula y Marrupa", mz_rojo,
     "Todo viaje desaconsejado a Cabo Delgado (salvo Palma, Pemba y Afungi, que son «solo esenciales») y a los distritos de "
     "Memba y Eráti (Nampula) y Mecula y Marrupa (Niassa).", "mozambique", aprox=True)
zona("mozambique", "naranja", "Pemba, Palma y Afungi", mz_ok, "Solo viajes esenciales a Palma y a los alrededores de Pemba y Afungi.", "mozambique", aprox=True)
zona("tanzania", "naranja", "Franja de 20 km con Cabo Delgado", franja("tanzania", "mozambique", 20).intersection(box(38.4, -12, 41, -10)),
     "Solo viajes esenciales a menos de 20 km de la frontera con Cabo Delgado (Mozambique).", "tanzania")

# ---------------------------------------------------------------- Kenia
ke = PAIS["kenia"]
ke_rojo = unary_union([ke.intersection(box(39.6, 2.6, 42.2, 4.4)),                      # Mandera (aprox.)
                       franja("kenia", "somalia", 60).intersection(box(38, -0.5, 42.2, 4.4)),  # Wajir junto a Somalia
                       ke.intersection(box(39.4, -1.7, 41.6, 0.9)).difference(circulo(-0.45, 39.65, 8)),  # Garissa (aprox.)
                       ke.intersection(pol((-1.3, 40.2), (-1.3, 41.6), (-2.0, 41.6), (-2.5, 40.9), (-2.4, 40.2))).difference(circulo(-2.27, 40.9, 9))])  # Lamu continental
zona("kenia", "rojo", "Mandera, Garissa, Lamu continental y 60 km de Somalia", ke_rojo,
     "Todo viaje desaconsejado a Mandera, a Garissa (salvo la ciudad y Lagdera), a Lamu salvo las islas de Lamu y Manda y a 60 km de "
     "Somalia en Wajir.", "kenya", aprox=True)
zona("kenia", "naranja", "Garissa ciudad y norte del río Tana", unary_union([circulo(-0.45, 39.65, 8), ke.intersection(box(39.0, -1.3, 40.2, -0.2))]).difference(ke_rojo),
     "Solo viajes esenciales a Garissa ciudad, al condado de Tana River al norte del río hasta Saka y a 15 km de la costa entre el Tana y el Galana.", "kenya", aprox=True)

# ---------------------------------------------------------------- Ruanda, Burundi
zona("ruanda", "naranja", "Rusizi: 10 km de la RD Congo", franja("ruanda", "rd-congo", 10).intersection(box(28.8, -2.9, 29.3, -2.2)),
     "Solo viajes esenciales en el distrito de Rusizi a menos de 10 km de la RD Congo.", "rwanda", aprox=True)
zona("burundi", "rojo", "Cibitoke, Bubanza, Rusizi y la Kibira", unary_union([reg("burundi", "Cibitoke", "Bubanza"), circulo(-3.30, 29.27, 8), circulo(-2.95, 29.45, 12)]),
     "Todo viaje desaconsejado a las comunas de Mugina, Cibitoke, Bukinyayana, Bubanza y Mpanda, al norte de Buyumbura hacia Cibitoke "
     "(Parque del Rusizi) y a las carreteras RN6 y RN10 por la Kibira.", "burundi", aprox=True)

# ---------------------------------------------------------------- Etiopía
et = PAIS["etiopia"]
somali = reg("etiopia", "Somali")
fafan = somali.intersection(box(42.2, 8.2, 44.5, 10.0))
et_rojo = unary_union([reg("etiopia", "Tigray", "Amhara", "Gambela Peoples"),
                       franja("etiopia", "sudan", 20), franja("etiopia", "sudan-del-sur", 10), franja("etiopia", "kenia", 10), franja("etiopia", "eritrea", 10),
                       somali.difference(fafan).intersection(km2deg(unary_union([PAIS["somalia"], PAIS["kenia"]]), 100, 6)),
                       fafan.intersection(km2deg(PAIS["somalia"], 30, 9.5)),
                       reg("etiopia", "Afar").intersection(km2deg(reg("etiopia", "Tigray"), 20, 13)),
                       reg("etiopia", "Oromiya").intersection(box(34.4, 8.3, 37.3, 10.4)),       # Wollega (aprox.)
                       reg("etiopia", "Oromiya").intersection(box(37.3, 9.25, 39.4, 10.3)),      # West y North Shewa (aprox.)
                       reg("etiopia", "Benshangul-Gumaz").intersection(box(34.5, 10.3, 36.8, 12.5))])  # Metekel (aprox.)
zona("etiopia", "rojo", "Tigray, Amhara, Gambela, Wollega, Shewa, Metekel y franjas fronterizas", et_rojo,
     "Todo viaje desaconsejado a Tigray, Amhara y Gambela; zonas de Wollega; West Shewa al norte de la A4 y North Shewa al sur y oeste "
     "de la A3; Metekel; 20 km de Sudán, 10 km de Sudán del Sur, Kenia y Eritrea; 100 km de Somalia y Kenia en la región Somalí "
     "(30 km en Fafan, salvo Wajale) y 20 km del límite con Tigray en Afar.", "ethiopia", aprox=True)
zona("etiopia", "naranja", "Resto de Benishangul-Gumuz y Somalí, East Shewa y Guji",
     unary_union([reg("etiopia", "Benshangul-Gumaz"), somali.difference(fafan), franja("etiopia", "eritrea", 15),
                  reg("etiopia", "Oromiya").intersection(box(38.5, 7.8, 40.2, 9.25)),   # East Shewa (aprox.)
                  reg("etiopia", "Oromiya").intersection(box(37.8, 4.6, 40.0, 6.3))]).difference(et_rojo),   # Guji (aprox.)
     "Solo viajes esenciales al resto de Benishangul-Gumuz y de la región Somalí, East Shewa (salvo la autopista Adís–Adama y la A7), "
     "Guji y West Guji (salvo la carretera Hawassa–Moyale) y la franja de 10–15 km de Eritrea.", "ethiopia", aprox=True)

# ---------------------------------------------------------------- Egipto
eg_rojo = unary_union([franja("egipto", "libia", 20).difference(circulo(31.55, 25.16, 8)), reg("egipto", "Shamal Sina'")])
zona("egipto", "rojo", "Norte del Sinaí y franja de 20 km con Libia", eg_rojo, "Todo viaje desaconsejado al Sinaí del Norte y a 20 km de Libia (salvo Salum).", "egypt")
zona("egipto", "naranja", "Norte del Sinaí del Sur, este del canal en Ismailía y Halaib",
     unary_union([reg("egipto", "Janub Sina'").intersection(box(33.3, 29.0, 34.5, 29.9)), reg("egipto", "Al Isma`iliyah").intersection(box(32.33, 30.3, 33.2, 31.0)),
                  box(35.0, 21.9, 36.9, 23.0)]).difference(eg_rojo),
     "Solo viajes esenciales al norte del Sinaí del Sur (más allá de la carretera Santa Catalina–Nuweiba, salvo las costas), a Ismailía "
     "al este del canal y al triángulo de Halaib. El FCDO también limita el desierto occidental fuera de los oasis y carreteras "
     "principales (no dibujado).", "egypt", aprox=True)

# ---------------------------------------------------------------- Túnez
tn_rojo = unary_union([circulo(35.2, 8.67, 18), reg("tunez", "Tataouine").intersection(box(7.5, 30.0, 11.0, 32.0)),
                       franja("tunez", "libia", 20).intersection(box(10.0, 32.0, 12.0, 34.0)), circulo(33.14, 11.22, 15)])
zona("tunez", "rojo", "Chaambi, zona militar del sur, Ben Guerdane y 20 km de Libia", tn_rojo,
     "Todo viaje desaconsejado al Parque del Chaambi y montes Salloum, Sammamma y Mghila; a la zona militar al sur de El Borma y "
     "Dehiba; a Ben Guerdane y a 20 km de Libia al norte de Dehiba.", "tunisia", aprox=True)
zona("tunez", "naranja", "Kasserine, franja de Argelia y 75 km de Libia",
     unary_union([reg("tunez", "Kassérine"), franja("tunez", "argelia", 20).intersection(reg("tunez", "Le Kef", "Jendouba")), franja("tunez", "argelia", 10),
                  franja("tunez", "libia", 75).difference(box(10.9, 33.3, 11.6, 34.0))]).difference(tn_rojo),
     "Solo viajes esenciales a Kasserine (con Sbeitla), a 20 km de Argelia en El Kef y Jendouba, a 10 km en el resto de la frontera "
     "argelina y a 75 km de Libia (salvo Zarzis y la C118).", "tunisia", aprox=True)

# ---------------------------------------------------------------- Argelia
dz_rojo = unary_union([franja("argelia", v, 30) for v in ("libia", "mauritania", "mali", "niger")]
                      + [franja("argelia", "tunez", 30).intersection(unary_union([reg("argelia", "Illizi", "Ouargla"), circulo(35.2, 8.5, 25)]))])
zona("argelia", "rojo", "30 km de Libia, Mauritania, Malí y Níger", dz_rojo,
     "Todo viaje desaconsejado a 30 km de las fronteras de Libia, Mauritania, Malí y Níger, y de la de Túnez en Illizi, Ouargla y los montes Chaambi.", "algeria")
zona("argelia", "naranja", "Resto de la franja de 30 km con Túnez", franja("argelia", "tunez", 30).difference(dz_rojo),
     "Solo viajes esenciales al resto de la franja de 30 km con Túnez.", "algeria")

# ---------------------------------------------------------------- MAEC: campamentos saharauis de Tinduf
zona("argelia", "rojo", "Campamentos de refugiados saharauis (Tinduf)",
     unary_union([circulo(27.476, -8.089, 7), circulo(27.515, -8.01, 7), circulo(27.492, -7.828, 7), circulo(27.621, -7.878, 7),
                  circulo(27.56, -8.05, 6), circulo(26.827, -6.88, 8)]),
     "El MAEC (7-5-2026) desaconseja los campamentos de refugiados saharauis (Rabuni, El Aaiún, Smara, Auserd, Bojador y Dajla) por "
     "amenaza terrorista concreta contra españoles. La ciudad de Tinduf y la carretera hacia Hassi 75 quedan fuera, pero con escolta.",
     "algeria", aprox=True)
Z[-1]["fuente"] = "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Argelia"
Z[-1]["organismo"] = "MAEC"

# ---------------------------------------------------------------- guía o autorización obligatoria (nivel «guia», azul)
GS = "https://embbrussels.mfa.gov.dz/fr/announcements/algerian-great-south-tourist-destination-new-visa-issuance-measures"
FR_TN = "https://www.diplomatie.gouv.fr/fr/conseils-aux-voyageurs/conseils-par-pays-destination/tunisie/"
def guia(pais, nombre, geom, texto, fuente, organismo, fecha, aprox=True):
    zona(pais, "guia", nombre, geom, texto, "", aprox=aprox)
    Z[-1].update(fuente=fuente, organismo=organismo, fecha=fecha)
guia("argelia", "Tassili n'Ajjer, Tadrart y Djanet", reg("argelia", "Illizi").intersection(box(5, 20, 12.5, 27.5)),
     "Solo con agencia de viajes argelina autorizada y guía: en Djanet la policía identifica al viajero en el aeropuerto y exige que lo "
     "recoja un guía; control militar a la entrada de la meseta y del Tadrart. Wilaya del Gran Sur (visado por agencia).",
     GS, "Embajada de Argelia + fichas", "2023 / 2026")
guia("argelia", "Hoggar (Tamanrasset, Assekrem) y sur de In Salah", reg("argelia", "Tamanghasset").intersection(box(-2, 18, 12, 27.2)),
     "Solo con agencia autorizada y guía (al sur de In Salah, según los viajeros); controles militares en el Ahaggar. Wilaya del Gran Sur.",
     GS, "Embajada de Argelia + fichas", "2023 / 2026")
guia("argelia", "Gran Sur: Adrar, Timimoun, Béchar, Béni Abbès, Tinduf", reg("argelia", "Adrar", "Béchar", "Tindouf"),
     "Wilayas del Gran Sur: el turismo va por agencia autorizada (visado del Gran Sur) y las autoridades pueden imponer escolta, "
     "sobre todo al oeste de Béchar hacia Tinduf. Con visado consular normal, confirmar con la agencia y la gendarmería antes de entrar.",
     GS, "Embajada de Argelia + fichas", "2023 / 2026")
TN_LINEA = pol((33.32, 8.033), (32.205, 10.03), (33.14, 11.22), (30.0, 11.8), (30.0, 7.4), (33.32, 7.4))
guia("tunez", "Sáhara al sur y este de Rjim Maatoug – Borj Bourguiba – Ben Guerdane", TN_LINEA,
     "Zona militar desde 2013: cualquier desplazamiento necesita autorización previa (Francia la desaconseja salvo motivo imperativo; "
     "el FCDO, rojo al sur de El Borma y Dehiba).", FR_TN, "Francia (MAEE)", "15-09-2026")
guia("tunez", "Desierto al sur de Douz (Gran Erg Oriental)",
     reg("tunez", "Kebili").intersection(box(7.5, 31.5, 10.5, 33.4)).difference(unary_union([circulo(33.457, 9.025, 8), circulo(32.977, 9.645, 6),
         km2deg(linea((33.457, 9.025), (33.221, 9.191), (32.977, 9.645)), 3, 33)])).difference(TN_LINEA),
     "Guía local o agencia oficial obligatorios en la práctica al sur de Douz, con registro en la Guardia Nacional de Douz: el ejército "
     "puede devolver a quien vaya sin guía. Douz – Jebil – Ksar Ghilane se puede hacer sin guía con experiencia y equipo.",
     "https://www.grand-sahara-aventures.com/guides/guide-sud-tunisien-4x4", "Fichas (viajeros)", "2025", aprox=True)
guia("tunez", "Mesa de Yugurta", circulo(35.744, 8.38, 4),
     "Solo en circuitos organizados con guías, en coordinación con las autoridades locales (Francia).", FR_TN, "Francia (MAEE)", "15-09-2026")

# ---------------------------------------------------------------- salida
out = []
for i, z in enumerate(Z):
    g = z.pop("g").simplify(0.02, preserve_topology=True)
    polys = [g] if g.geom_type == "Polygon" else list(getattr(g, "geoms", []))
    anillo = lambda r: [[round(y, 3), round(x, 3)] for x, y in r.coords]
    # Cada polígono = [exterior, agujeros...] (formato de Leaflet); los agujeros son las excepciones (Maroua, Pemba…)
    rings = [[anillo(p.exterior)] + [anillo(h) for h in p.interiors if Polygon(h).area > 0.0004]
             for p in polys if p.geom_type == "Polygon" and p.area > 0.0004]
    if not rings:
        continue
    out.append({"id": f"z{i + 1}", **z, "poly": rings})
destino = RAIZ / "tools/gen/zonas_riesgo.json"
destino.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(len(out), "zonas ·", destino.stat().st_size // 1024, "KB")
for z in out:
    print(f"  {z['pais']:18} {z['nivel']:8} {len(z['poly']):3} polígonos, {sum(len(x) - 1 for x in z['poly'])} agujeros · {z['nombre']}")

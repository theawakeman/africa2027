# -*- coding: utf-8 -*-
"""Prepara las consultas de geocodificación para auditar las coordenadas de un país.

Genera audit/geo/<slug>_queries.json con, por cada PDI y punto logístico, el
nombre limpio, las variantes de búsqueda, el punto actual de la app y el bbox
del país. Esas consultas se lanzan luego contra Photon (OSM) y Wikidata desde
el navegador (audit_geo_js.py genera el JavaScript) y audit_geo_eval.py evalúa
las respuestas.

Uso:  python3 audit_geo_prep.py <slug> [<slug> ...]
"""
import json
import re
import sys
from pathlib import Path

from audit_gps import BBOX

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "audit" / "geo"

IDIOMA = {"marruecos": "fr", "sahara-occidental": "fr", "mauritania": "fr", "senegal": "fr", "guinea": "fr",
          "costa-de-marfil": "fr", "togo": "fr", "benin": "fr", "camerun": "fr", "gabon": "fr", "congo": "fr",
          "rd-congo": "fr", "ruanda": "fr", "angola": "pt", "mozambique": "pt"}
TRAD = {
    "fr": [(r"^Parque Nacional (de |del |de la |de los )?", "Parc national "), (r"^Cascadas? (de |del )?", "Cascade "),
           (r"^Isla (de |del )?", "Île "), (r"^Museo (de |del )?", "Musée "), (r"^Reserva (de Fauna |Natural |de la Biosfera )?(de |del )?", "Réserve "),
           (r"^Lago ", "Lac "), (r"^Monte ", "Mont "), (r"^Playa (de )?", "Plage "), (r"^Mezquita (de )?", "Mosquée "),
           (r"^Fuerte (de )?", "Fort "), (r"^Catedral (de )?", "Cathédrale "), (r"^Mercado (de )?", "Marché "),
           (r"^Puerto (de )?", "Port "), (r"^Bosque (de )?", "Forêt "), (r"^Río ", "Fleuve "), (r"^Cabo ", "Cap "),
           (r"^Meseta (de )?", "Plateau "), (r"^Monumento (del |de la |de )?", "Monument ")],
    "en": [(r"^Parque Nacional (de |del |de la |de los )?(.*)$", r"\2 National Park"), (r"^Cascadas? (de |del )?(.*)$", r"\2 Falls"),
           (r"^Isla (de |del )?(.*)$", r"\2 Island"), (r"^Museo (de |del )?(.*)$", r"\2 Museum"), (r"^Reserva (de Fauna |Natural )?(de |del )?(.*)$", r"\3 Reserve"),
           (r"^Lago (.*)$", r"Lake \1"), (r"^Monte (.*)$", r"Mount \1"), (r"^Playa (de )?(.*)$", r"\2 Beach"),
           (r"^Fuerte (de )?(.*)$", r"Fort \2"), (r"^Catedral (de )?(.*)$", r"\2 Cathedral"), (r"^Mercado (de )?(.*)$", r"\2 Market"),
           (r"^Río (.*)$", r"\1 River"), (r"^Cabo (.*)$", r"Cape \1"), (r"^Meseta (de )?(.*)$", r"\2 Plateau")],
    "pt": [(r"^Parque Nacional (de |del |de la |de los )?", "Parque Nacional d"), (r"^Cascadas? (de |del )?", "Cascata "),
           (r"^Isla (de |del )?", "Ilha "), (r"^Museo (de |del )?", "Museu "), (r"^Reserva (de Fauna |Natural )?(de |del )?", "Reserva "),
           (r"^Playa (de )?", "Praia "), (r"^Fuerte (de )?", "Fortaleza "), (r"^Lago ", "Lago ")],
}


# Exónimos españoles → nombre local/internacional que usan OSM y Wikidata
EXONIMOS = {"nuakchot": "Nouakchott", "nuadibú": "Nouadhibou", "nuadibu": "Nouadhibou", "dajla": "Dakhla",
            "el aaiún": "Laayoune", "bojador": "Boujdour", "uadán": "Ouadane", "tánger": "Tanger",
            "marrakech": "Marrakesh", "fez": "Fès", "esmara": "Smara", "banjul": "Banjul", "yibuti": "Djibouti",
            "el cairo": "Cairo", "jartum": "Khartoum", "guelb er richat": "Richat Structure",
            "paso de tifoujar": "Tifoujar", "valle blanco": "Vallée Blanche Amogjar", "parque de diawling": "Parc national du Diawling",
            "puerto pesquero de nuakchot": "Port de pêche Nouakchott", "oasis de terjit": "Terjit"}

# Consultas cartográficas revisadas a mano para nombres compuestos que el
# generador no puede desambiguar sin perder el lugar concreto. Se mantienen
# aquí, y no solo en los JSON de auditoría, para que las comprobaciones sean
# reproducibles al regenerarlas.
CONSULTAS_EXACTAS = {
    "namibia": {
        "poi-1": ["Fish River Canyon Viewpoint Namibia"],
        "poi-2": ["Quivertree Forest Rest Camp Namibia"],
        "poi-3": ["Garub Desert Horses Namibia"],
        "poi-4": ["Lüderitz Waterfront Development Company"],
        "poi-5": ["Kolmanskop Entrance Namibia"],
        "poi-6": ["Dune 45 Sossusvlei Namibia"],
        "poi-7": ["Deadvlei Namibia"],
        "poi-8": ["Kuiseb River Viewpoint Namibia"],
        "poi-9": ["Lagoon Promenade Walvis Bay Namibia"],
        "poi-10": ["Sandwich Harbour Namibia"],
        "poi-11": ["Jetty Pier Swakopmund Namibia"],
        "poi-12": ["Spitzkoppe Community Restcamp Namibia"],
        "poi-13": ["Cape Cross Seal Reserve Namibia"],
        "poi-14": ["Messum Crater Namibia"],
        "poi-15": ["White Lady Brandberg Namibia"],
        "poi-16": ["Twyfelfontein Visitors Centre Namibia"],
        "poi-17": ["Palmwag Lodge Namibia"],
        "poi-18": ["Ugab Gate Skeleton Coast Namibia"],
        "poi-19": ["Okaukuejo Waterhole Etosha Namibia"],
        "poi-20": ["Van Zyl's Pass Namibia"],
        "poi-21": ["Epupa Falls Viewpoint Namibia"],
        "poi-22": ["Viewpoint to Ruacana Falls Namibia"],
        "poi-23": ["Independence Museum Windhoek Namibia"],
        "poi-24": ["Waterberg Camp NWR Reception Namibia"],
    },
    "ghana": {
        "poi-1": ["Nzulezo Ghana"],
        "poi-4": ["Elmina Castle Ghana", "São Jorge da Mina"],
        "poi-5": ["Cape Coast Castle Ghana"],
        "poi-8": ["Kwame Nkrumah Memorial Park Accra"],
        "poi-10": ["Akosombo Dam Ghana", "Lake Volta Akosombo"],
        "poi-12": ["Tafi Atome Monkey Sanctuary"],
        "poi-13": ["Mount Gemi Amedzofe", "Amedzofe Ghana"],
        "poi-14": ["Wli Waterfalls Ghana", "Agumatsa Falls"],
        "poi-15": ["Mount Afadja Ghana", "Afadjato"],
        "poi-16": ["Boti Falls Ghana"],
        "poi-18": ["Besease Traditional Shrine Ghana", "Asante Traditional Buildings Besease"],
        "poi-19": ["Yeji ferry terminal Ghana", "Makango ferry terminal Ghana"],
        "poi-21": ["Larabanga Mosque Ghana"],
        "poi-22": ["Paga Crocodile Pond Ghana"],
        "log-8": ["Sekondi-Takoradi Ghana"],
        "log-9": ["Ho Ghana"],
        "log-10": ["Tamale Ghana"],
        "log-11": ["Bolgatanga Ghana"],
        "log-17": ["Wa Ghana", "Bole Ghana", "Sampa Ghana"],
    },
    "togo": {
        "poi-1": ["Grand Marché Lomé", "Sacred Heart Cathedral Lomé"],
        "poi-2": ["Akodessewa Fetish Market Lomé"],
        "poi-3": ["Palais de Lomé"],
        "poi-4": ["Baguida Beach Togo", "Coco Beach Lomé"],
        "poi-5": ["Maison des Esclaves Agbodrafo", "Maison Wood Agbodrafo"],
        "poi-9": ["Réserve de faune de Sarakawa Togo"],
        "poi-10": ["Koutammakou Togo"],
        "poi-11": ["Faille d'Aledjo Togo", "Aledjo Togo"],
        "poi-14": ["Parc national de Fazao-Malfakassa"],
        "poi-15": ["Cascade d'Akloa Badou"],
        "poi-17": ["Cascade de Womé Togo", "Cascade de Kpimé Togo"],
        "poi-18": ["Mont Kloto Togo", "Château Viale Togo"],
        "poi-19": ["Mont Agou Togo", "Pic Baumann Togo"],
        "log-13": ["Atakpamé Togo"],
    },
    "benin": {
        "poi-1": ["Bouche du Roy Benin", "Grand-Popo Benin"],
        "poi-2": ["Porte du Non Retour Ouidah"],
        "poi-3": ["Temple des Pythons Ouidah", "Musée d'Histoire de Ouidah"],
        "poi-4": ["Vodun Days Ouidah"],
        "poi-5": ["Possotomè Benin", "Lac Ahémé"],
        "poi-6": ["Avlékété Benin", "Route des Pêches Benin"],
        "poi-7": ["Embarcadère de Ganvié Abomey-Calavi"],
        "poi-9": ["Marché Dantokpa Cotonou"],
        "poi-11": ["Oké Shabè Savè Benin", "Savè Benin"],
        "poi-12": ["Grotte d'Arigbo Dassa-Zoumè", "Dassa-Zoumè Benin"],
        "poi-13": ["Palais Royaux d'Abomey"],
        "poi-14": ["Monts Kouffé Benin", "Bassila Benin"],
        "poi-15": ["Taneka Koko Benin", "Taneka Béri Benin"],
        "poi-18": ["Chutes de Tanougou Benin"],
        "poi-19": ["Parc W Benin"],
        "log-8": ["Hôpital de Zone Dassa-Zoumè", "Centre Hospitalier Départemental Abomey"],
    },
    "nigeria": {
        "poi-1": ["Badagry Point of No Return"],
        "poi-3": ["Lekki Conservation Centre Lagos"],
        "poi-4": ["Oba of Benin Palace"],
        "poi-5": ["Onitsha Bridge Nigeria", "Niger Bridge Asaba"],
        "poi-7": ["Pandrillus Drill Ranch Calabar"],
        "poi-8": ["Cross River National Park Oban Division"],
        "poi-9": ["Alok Monoliths Nigeria", "Ikom Monoliths"],
        "poi-10": ["Agbokim Waterfalls Nigeria"],
        "poi-11": ["Afi Mountain Wildlife Sanctuary"],
        "poi-12": ["Obudu Mountain Resort Nigeria"],
        "poi-13": ["Osun-Osogbo Sacred Grove"],
        "poi-15": ["Olumo Rock Abeokuta"],
        "log-9": ["Stella Obasanjo Hospital Benin City"],
        "log-10": ["Ladipo Auto Spare Parts Market Lagos"],
    },
    "uganda": {
        "poi-1": ["Sipi Falls Uganda"],
        "poi-2": ["Wagagai Peak Mount Elgon Uganda", "Mount Elgon National Park Uganda"],
        "poi-3": ["Source of the Nile Jinja Uganda", "Speke Monument Jinja"],
        "poi-4": ["Uganda Museum Kampala"],
        "poi-5": ["Entebbe Botanical Gardens Uganda"],
        "poi-6": ["Kalangala Ssese Islands Uganda"],
        "poi-7": ["Ziwa Rhino Sanctuary Uganda"],
        "poi-8": ["Murchison Falls Uganda"],
        "poi-9": ["Apoka Kidepo Valley National Park Uganda"],
        "poi-10": ["Fort Patiko Uganda", "Gulu Uganda"],
        "poi-11": ["Lake Nyabikere Fort Portal Uganda", "Ndali Kasenda crater lakes Uganda"],
        "poi-12": ["Kanyanchu Visitor Centre Kibale Uganda"],
        "poi-13": ["Rwenzori Mountains National Park Nyakalengija Uganda"],
        "poi-14": ["Katwe Salt Lake Uganda"],
        "poi-15": ["Mweya Kazinga Channel Uganda"],
        "poi-16": ["Ishasha Sector Queen Elizabeth National Park Uganda"],
        "poi-17": ["Buhoma Bwindi Visitor Centre Uganda"],
        "poi-18": ["Ntebeko Visitor Centre Mgahinga Uganda"],
        "poi-19": ["Lake Bunyonyi Uganda"],
        "poi-20": ["Nshara Gate Lake Mburo National Park Uganda"],
        "log-5": ["Embassy of Spain Nairobi"],
        "log-6": ["International Hospital Kampala", "Mulago National Referral Hospital Kampala"],
    },
    "ruanda": {
        "poi-1": ["Musanze Caves Rwanda"],
        "poi-2": ["Volcanoes National Park Headquarters Kinigi Rwanda"],
        "poi-3": ["Mount Bisoke Rwanda"],
        "poi-4": ["Dian Fossey Tomb Rwanda", "Karisoke Research Center Rwanda"],
        "poi-5": ["Burera Ruhondo Twin Lakes viewpoint Rwanda"],
        "poi-6": ["Gisenyi Public Beach Rubavu Rwanda"],
        "poi-7": ["Congo Nile Trail Rubavu trailhead Rwanda"],
        "poi-8": ["Kibuye Karongi Rwanda"],
        "poi-9": ["Rusizi Rwanda Bukavu border"],
        "poi-10": ["Nyungwe Canopy Walk Uwinka Rwanda"],
        "poi-11": ["Ethnographic Museum Huye Rwanda"],
        "poi-12": ["King's Palace Museum Nyanza Rwanda"],
        "poi-13": ["Kandt House Museum Kigali Rwanda"],
        "poi-14": ["Kigali Genocide Memorial Rwanda"],
        "poi-15": ["Nyamata Genocide Memorial Rwanda"],
        "poi-16": ["Lake Muhazi Rwanda"],
        "poi-17": ["Akagera National Park South Entrance Rwanda"],
        "poi-18": ["Gishwati Mukura National Park Rwanda"],
        "log-4": ["Embassy of Spain Nairobi"],
        "log-5": ["King Faisal Hospital Kigali", "CHUK Kigali"],
    },
    "malaui": {
        "poi-1": ["Cultural Museum Centre Karonga Malawi"],
        "poi-2": ["Stone House Museum Livingstonia Malawi"],
        "poi-3": ["Manchewe Falls Malawi"],
        "poi-4": ["Chelinda Camp Nyika National Park Malawi"],
        "poi-5": ["Mzuzu Malawi"],
        "poi-6": ["Nkhata Bay Jetty Malawi"],
        "poi-7": ["Bandawe Mission Malawi", "Chintheche Malawi"],
        "poi-8": ["St Peter's Cathedral Likoma Malawi"],
        "poi-9": ["Nkhotakota Wildlife Reserve main gate Malawi"],
        "poi-10": ["Livingstone Tree Nkhotakota Malawi"],
        "poi-11": ["Senga Bay Beach Malawi"],
        "poi-12": ["Lifupa Kasungu National Park Malawi"],
        "poi-13": ["Lilongwe Wildlife Centre Malawi"],
        "poi-14": ["Chongoni Rock Art Chentcherere Malawi"],
        "poi-15": ["Kungoni Centre Mua Malawi"],
        "poi-16": ["Cape Maclear Lake Malawi National Park"],
        "poi-17": ["Liwonde National Park main gate Malawi"],
        "poi-18": ["Queen's View Zomba Plateau Malawi"],
        "poi-19": ["Mandala House Blantyre Malawi"],
        "poi-20": ["Likhubula Mount Mulanje Malawi"],
        "poi-21": ["Satemwa Tea Estate Malawi"],
        "poi-22": ["Majete Wildlife Reserve main gate Malawi"],
        "log-6": ["Honorary Consulate of Spain Lilongwe"],
        "log-7": ["Embassy of Spain Harare"],
        "log-8": ["Kamuzu Central Hospital Lilongwe"],
        "log-9": ["Queen Elizabeth Central Hospital Blantyre"],
        "log-10": ["Mzuzu Central Hospital Malawi"],
    },
    "zimbabue": {
        "poi-1": ["Christmas Pass Mutare Zimbabwe"],
        "poi-2": ["Vumba Botanical Garden Zimbabwe"],
        "poi-3": ["Mount Nyangani summit Zimbabwe"],
        "poi-4": ["Mtarazi Falls Viewpoint Zimbabwe"],
        "poi-5": ["Ziwa Site Museum Zimbabwe"],
        "poi-6": ["Chimanimani National Park Office Zimbabwe"],
        "poi-7": ["Great Zimbabwe National Monument"],
        "poi-8": ["Lake Mutirikwi Recreational Park Zimbabwe"],
        "poi-9": ["Chilojo Cliffs Gonarezhou Zimbabwe"],
        "poi-10": ["Natural History Museum of Zimbabwe Bulawayo"],
        "poi-11": ["World's View Matobo Zimbabwe", "Grave of Cecil Rhodes Matobo"],
        "poi-12": ["Khami World Heritage Site Zimbabwe"],
        "poi-13": ["Hwange Main Camp Zimbabwe"],
        "poi-14": ["Victoria Falls Main Entrance Zimbabwe"],
        "poi-15": ["Victoria Falls Bridge Zimbabwe Zambia"],
        "poi-16": ["Zambezi National Park Zimbabwe"],
        "poi-17": ["National Gallery of Zimbabwe Harare"],
        "poi-18": ["Domboshawa Zimbabwe"],
        "poi-19": ["Sleeping Pool Chinhoyi Caves Zimbabwe"],
        "poi-20": ["Nyamepi campsite Mana Pools Zimbabwe"],
        "poi-21": ["Kariba Dam Zimbabwe Zambia"],
        "poi-22": ["Mucheni Gorge Viewpoint Chizarira Zimbabwe"],
    },
    "esuatini": {
        "poi-1": ["Lion Cavern Ngwenya Mine Eswatini"],
        "poi-2": ["Ngwenya Glass Eswatini"],
        "poi-3": ["Malolotja Nature Reserve reception Eswatini"],
        "poi-4": ["Malolotja Canopy Tour Eswatini"],
        "poi-5": ["Maguga Dam viewpoint Eswatini"],
        "poi-6": ["Nsangwini Rock Art Eswatini"],
        "poi-7": ["Phophonyane Falls Ecolodge Eswatini"],
        "poi-8": ["Swazi Plaza Mbabane Eswatini"],
        "poi-9": ["Sibebe Rock trail Eswatini"],
        "poi-10": ["Ezulwini Craft Market Eswatini"],
        "poi-11": ["Mantenga Cultural Village Eswatini"],
        "poi-12": ["Mlilwane Wildlife Sanctuary reception Eswatini"],
        "poi-13": ["Manzini Market Eswatini"],
        "poi-14": ["Mkhaya Game Reserve pick up point Eswatini"],
        "poi-15": ["Hlane Royal National Park Ndlovu Camp Eswatini"],
        "poi-16": ["Shewula Mountain Camp Eswatini"],
    },
    "lesoto": {
        "poi-1": ["Butha Buthe Mountain Lesotho"],
        "poi-2": ["Ts'ehlanyane National Park gate Lesotho"],
        "poi-3": ["Liphofung Cave Cultural Historical Site Lesotho"],
        "poi-4": ["Moteng Pass viewpoint Lesotho"],
        "poi-5": ["Afriski Mountain Resort Lesotho"],
        "poi-6": ["Tlaeeng Pass Lesotho"],
        "poi-7": ["Mokhotlong District Museum Lesotho"],
        "poi-8": ["Thabana Ntlenyana summit Lesotho"],
        "poi-9": ["Sani Pass Lesotho border post"],
        "poi-10": ["Sani Mountain Lodge Lesotho"],
        "poi-11": ["Katse Dam visitor centre Lesotho"],
        "poi-12": ["Bokong Nature Reserve visitor centre Lesotho"],
        "poi-13": ["Mohale Dam visitor centre Lesotho"],
        "poi-14": ["Basotho Hat Maseru Lesotho"],
        "poi-15": ["Thaba Bosiu Cultural Village Lesotho"],
        "poi-16": ["Morija Museum and Archives Lesotho"],
        "poi-17": ["Malealea Lodge Lesotho"],
        "poi-18": ["Maletsunyane Falls viewpoint Semonkong Lesotho"],
        "poi-19": ["Masitise Cave House Museum Quthing Lesotho"],
        "poi-20": ["Sehlabathebe National Park lodge Lesotho"],
    },
    "botsuana": {
        "poi-1": ["Kazungula Bridge Botswana Zambia"],
        "poi-2": ["Sedudu Gate Chobe Botswana"],
        "poi-3": ["Savuti Camp Botswana"],
        "poi-4": ["Linyanti Campsite Botswana"],
        "poi-5": ["North Gate Khwai Moremi Botswana"],
        "poi-6": ["Xakanaxa Camp Moremi Botswana"],
        "poi-7": ["Mboma Island Expeditions Botswana"],
        "poi-8": ["Nhabe Museum Maun Botswana"],
        "poi-9": ["Boro 2 Mokoro Polers Station Botswana"],
        "poi-10": ["Shakawe Botswana"],
        "poi-11": ["Tsodilo Hills Museum Botswana"],
        "poi-12": ["Gcwihaba Caves Botswana"],
        "poi-13": ["Kuru Art Project D'Kar Botswana"],
        "poi-14": ["Deception Valley Central Kalahari Botswana"],
        "poi-15": ["Baines Baobabs Botswana"],
        "poi-16": ["Khumaga Camp Makgadikgadi Botswana"],
        "poi-17": ["Kubu Island Lekhubu Botswana"],
        "poi-18": ["Nata Bird Sanctuary Botswana"],
        "poi-19": ["Khama Rhino Sanctuary entrance Botswana"],
        "poi-20": ["Pont Drift Border Post Botswana"],
        "poi-21": ["Three Dikgosi Monument Gaborone Botswana"],
    },
    "sudafrica": {
        "poi-1": ["Apartheid Museum Johannesburg South Africa"],
        "poi-2": ["Mandela House Soweto South Africa"],
        "poi-3": ["Maropeng Visitor Centre South Africa"],
        "poi-4": ["Three Rondavels View Point South Africa"],
        "poi-5": ["Phabeni Gate Kruger South Africa"],
        "poi-6": ["Bhangazi Gate iSimangaliso South Africa"],
        "poi-7": ["Memorial Gate Hluhluwe South Africa"],
        "poi-8": ["KwaMuhle Museum Durban South Africa"],
        "poi-9": ["Sentinel Car Park Drakensberg South Africa"],
        "poi-10": ["Glen Reenen Rest Camp South Africa"],
        "poi-11": ["Sani Pass South Africa Lesotho"],
        "poi-12": ["Hole in the Wall Eastern Cape South Africa"],
        "poi-13": ["Storms River Mouth Rest Camp South Africa"],
        "poi-14": ["Cango Caves South Africa"],
        "poi-15": ["Southernmost Tip of Africa Cape Agulhas"],
        "poi-16": ["Old Harbour Museum Hermanus South Africa"],
        "poi-17": ["Table Mountain Cableway Lower Station South Africa"],
        "poi-18": ["Cape of Good Hope South Africa"],
        "poi-19": ["Nelson Mandela Gateway Robben Island Cape Town"],
        "poi-20": ["Stellenbosch Village Museum South Africa"],
        "poi-21": ["Algeria Campsite Cederberg South Africa"],
        "poi-22": ["Southern African Large Telescope Sutherland"],
        "poi-23": ["Twee Rivieren Rest Camp Kgalagadi South Africa"],
        "poi-24": ["Augrabies Falls South Africa"],
        "poi-25": ["Skilpad Rest Camp Namaqua South Africa"],
        "poi-26": ["Sendelingsdrift Richtersveld South Africa"],
    },
}


def exonimo(nombre):
    n = nombre.strip()
    if n.lower() in EXONIMOS:
        return EXONIMOS[n.lower()]
    for k, v in EXONIMOS.items():
        if re.search(r"\b" + re.escape(k) + r"\b", n, re.I):
            return re.sub(r"(?i)\b" + re.escape(k) + r"\b", v, n)
    return None


def traduce(nombre, idioma):
    for pat, rep in TRAD.get(idioma, []) + (TRAD["en"] if idioma != "en" else []):
        if re.match(pat, nombre):
            return re.sub(pat, rep, nombre)
    return None


PREFIJOS = re.compile(r"^(Combustible|Agua potable|Agua|Hospital|Consulado|Embajada|Paso fronterizo|Paso|Frontera)\s*[·:]\s*", re.I)

# Palabras con mayúscula que NO son topónimos en los nombres de frontera/combustible
GENERICAS = {"frontera", "entrada", "salida", "paso", "puesto", "puerto", "ferry", "presa", "embarcadero", "continuidad",
             "límite", "limite", "administración", "subida", "bajada", "trans", "combustible", "agua", "potable",
             "sin", "desde", "hacia", "eje", "corredor", "cruce", "junction", "nudo", "puente", "alternativa",
             "norte", "sur", "este", "oeste", "litoral", "garrafas", "supermercados", "red", "densa", "ciudades",
             "uso", "general", "vehículos", "vehiculos", "el", "la", "de", "del", "y", "o", "a"}
ARTICULOS = {"el", "la", "de", "del", "y", "o", "a"}


def nombres_propios(texto):
    """Extrae topónimos (secuencias con mayúscula inicial) de un nombre descriptivo."""
    texto = re.sub(r"[()]", " , ", texto)
    out = []
    for seg in re.split(r"\s*(?:—|–|/|→|·|:|,|\bo\b|\by\b)\s*", texto):
        for m in re.finditer(r"[A-ZÁÉÍÓÚÑÀÂÊÎÔÛÇ][\w'’\-]*(?:\s+(?:de|del|la|el|du|des|le|les|d'|n')\s+[A-ZÁÉÍÓÚÑ][\w'’\-]*|\s+[A-ZÁÉÍÓÚÑ][\w'’\-]*)*", seg):
            cand = m.group(0).strip()
            if cand.isupper():
                continue
            palabras = re.split(r"\s+", cand)
            # recorta genéricos solo en los extremos («Puerto de Tánger Med» → «Tánger Med», «El Aaiún» se conserva)
            while palabras and palabras[0].lower() in GENERICAS - ARTICULOS:
                palabras.pop(0)
            while palabras and palabras[0].lower() in ARTICULOS and len(palabras) > 1 and palabras[1].lower() in ARTICULOS:
                palabras.pop(0)
            while palabras and palabras[-1].lower() in GENERICAS:
                palabras.pop()
            if palabras and palabras[0].lower() == "de":
                palabras.pop(0)
            if not palabras:
                continue
            cand = " ".join(palabras)
            if cand.lower() not in GENERICAS and len(cand) > 2:
                out.append(cand)
    return out


def limpia(nombre):
    n = nombre.strip()
    n = re.sub(r"\s*(—|\s–\s).*$", "", n)         # «Paso X — salida hacia Guinea» (no corta «Karang–Amdalai»)
    n = re.sub(r"\s*\(.*?\)\s*", " ", n)         # paréntesis
    n = re.sub(r"\s*·\s*.*$", "", n)             # «Combustible · Dakar» → se trata aparte
    return re.sub(r"\s+", " ", n).strip(" ,")


def variantes(item, idioma="en"):
    nombre = item["name"]
    v = []
    base = limpia(nombre)
    if item["type"] == "log":
        cat = item["cat"].lower()
        if cat in ("combustible", "agua potable", "servicio"):
            # «Combustible · Saint-Louis» → la ciudad; «Kombos (Serrekunda, Kololi…)» → cada topónimo
            ciudad = re.sub(r"^[^·]*·\s*", "", nombre)
            v += nombres_propios(ciudad)
            ciudad = re.sub(r"\s*\(.*?\)", "", ciudad).split(",")[0].strip()
            v += [ciudad]
        elif cat == "frontera":
            # «Paso Karang–Amdalai — Senegal/Gambia (SUBIDA)» → Karang, Amdalai
            # «Frontera · Entrada — Puerto de Tánger Med (ferry…)» → Tánger Med
            core = re.sub(r"^(Paso fronterizo|Paso|Frontera)\s*", "", base, flags=re.I)
            partes = re.split(r"\s*[–/]\s*", core)
            v += [p.strip() for p in partes if len(p.strip()) > 2 and p.strip().lower() not in GENERICAS]
            v += nombres_propios(nombre)
            if core.lower() not in GENERICAS:
                v += [core]
        elif cat == "hospital":
            v += [base, re.sub(r"^(Hôpital|Hospital|Centre Hospitalier Régional|Centre de santé)\s*(de|d')?\s*", "", base, flags=re.I)]
        elif cat == "consular":
            v += [base]
            m = re.search(r"(Embajada|Consulado General|Consulado|Embassy|Consulate)\s+de\s+(\w+)\s+en\s+([\w' -]+)", base, re.I)
            if m:
                pais = {"España": "Spain", "Francia": "France", "Alemania": "Germany", "Portugal": "Portugal",
                        "Italia": "Italy", "Países Bajos": "Netherlands", "Bélgica": "Belgium"}.get(m.group(2), m.group(2))
                tipo = "Embassy" if m.group(1).lower().startswith("emb") else "Consulate"
                v += [f"{tipo} of {pais} {m.group(3)}", f"{pais} {tipo} {m.group(3)}"]
        else:
            v += [base]
    else:
        v += [base]
        t = traduce(base, idioma)
        if t:
            v += [t]
        # «Iwik y Banc d'Arguin» → cada parte
        if re.search(r"\s+y\s+", base):
            v += [x.strip() for x in re.split(r"\s+y\s+", base) if len(x.strip()) > 3]
        # «Saint-Louis – isla histórica» → «Saint-Louis»
        corto = re.split(r"\s+[–—-]\s+", nombre)[0].strip()
        if corto and corto != base:
            v += [corto]
    # exónimos españoles (Nuakchot → Nouakchott)
    for x in list(v):
        e = exonimo(x)
        if e:
            v += [e]
    # sin duplicados, en orden
    seen, out = set(), []
    for x in v:
        k = x.lower()
        if x and k not in seen:
            seen.add(k); out.append(x)
    return out[:5]


def main(slugs):
    OUT.mkdir(parents=True, exist_ok=True)
    for slug in slugs:
        pois = json.loads((ROOT / "content" / "pois" / f"{slug}.json").read_text(encoding="utf-8"))
        ficha = json.loads((ROOT / "content" / "ficha" / f"{slug}.json").read_text(encoding="utf-8"))
        items = []
        for p in pois:
            items.append({"id": f"poi-{p['n']}", "type": "poi", "n": p["n"], "name": p["name"], "cat": p["cat"],
                          "prio": p.get("prio"), "lat": p["lat"], "lon": p["lon"], "desc": p.get("desc", "")[:200]})
        for i, lg in enumerate(ficha.get("logistics", [])):
            items.append({"id": f"log-{i}", "type": "log", "n": i, "name": lg["name"], "cat": lg["cat"],
                          "lat": lg["lat"], "lon": lg["lon"], "desc": lg.get("info", "")[:200]})
        for it in items:
            it["q"] = variantes(it, IDIOMA.get(slug, "en"))
            it["q"] = CONSULTAS_EXACTAS.get(slug, {}).get(it["id"], it["q"])
        bb = BBOX.get(slug)
        bbox = [bb[2] - 0.3, bb[0] - 0.3, bb[3] + 0.3, bb[1] + 0.3] if bb else None  # minLon,minLat,maxLon,maxLat
        data = {"slug": slug, "bbox": bbox, "items": items}
        (OUT / f"{slug}_queries.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print(slug, len(pois), "PDIs,", len(items) - len(pois), "logística →", OUT / f"{slug}_queries.json")


if __name__ == "__main__":
    main(sys.argv[1:])

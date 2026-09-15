#!/usr/bin/env python3
"""Lista candidatos de Commons con metadatos, sin asignarlos automáticamente.

La salida sirve para la auditoría manual de fotografías: título, descripción,
categorías, autor y licencia se leen de la API oficial de Wikimedia Commons.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import certifi


ROOT = Path(__file__).resolve().parents[1]
API = "https://commons.wikimedia.org/w/api.php"

SEARCH_QUERIES: dict[str, dict[int, str]] = {
    "guinea": {
        1: "Badiar National Park Guinea Koundara",
        2: 'incategory:"Labé" Guinea',
        3: "Mount Loura Dame de Mali Guinea",
        4: "Kinkon waterfall Guinea Pita",
        5: "Kambadaga waterfall Guinea",
        6: "Doucki Guinea Fouta Djallon",
        7: 'incategory:"Dalaba" Guinea',
        8: "Ditinn waterfall Guinea",
        9: "Voile de la Mariée Kindia Guinea",
        10: 'incategory:"Conakry" Guinea',
        11: "Iles de Los Guinea",
        12: 'incategory:"Boké" Guinea museum',
        13: 'incategory:"Faranah" Guinea Niger',
        14: "Ziama Massif Guinea Seredou",
        15: 'incategory:"Nzérékoré" Guinea',
        16: 'incategory:"Mount Nimba Strict Nature Reserve"',
        17: 'incategory:"Kankan" Guinea',
        18: "Upper Niger National Park Guinea",
        19: "Tinkisso waterfall Guinea Dabola",
        20: "Tougué Guinea Fouta Djallon",
    },
    "sierra-leona": {
        1: "Gbalamuya Kambia Sierra Leone border",
        2: 'incategory:"Freetown" Sierra Leone',
        3: "Sierra Leone National Railway Museum",
        4: "Tacugama Chimpanzee Sanctuary Sierra Leone",
        5: "Western Area Peninsula National Park Sierra Leone",
        6: 'incategory:"River Number Two Beach"',
        7: "Tokeh Beach Sierra Leone",
        8: "Bureh Beach Sierra Leone surf",
        9: 'incategory:"Banana Islands, Sierra Leone"',
        10: "Bunce Island Sierra Leone",
        11: 'incategory:"Bo, Sierra Leone"',
        12: 'incategory:"Kenema" Sierra Leone',
        13: "Gola Rainforest National Park Sierra Leone",
        14: "Tiwai Island Sierra Leone",
        15: "Sulima Sierra Leone Moa River",
        16: "Turtle Islands Sierra Leone",
        17: 'incategory:"Makeni" Sierra Leone',
        18: 'incategory:"Kabala, Sierra Leone"',
        19: "Mount Bintumani Loma Mountains Sierra Leone",
        20: "Outamba Kilimi National Park Sierra Leone",
    },
    "liberia": {
        1: "Bo Waterside Liberia border",
        2: 'incategory:"Robertsport" Liberia surf',
        3: "Lake Piso Liberia",
        4: 'incategory:"Monrovia" Liberia',
        5: "Providence Island Liberia",
        6: "Firestone Harbel Liberia rubber plantation",
        7: 'incategory:"Buchanan, Liberia"',
        8: 'incategory:"Greenville, Liberia"',
        9: "Sapo National Park Liberia",
        10: "Harper Liberia Cape Palmas",
        11: 'incategory:"Zwedru" Liberia',
        12: 'incategory:"Ganta" Liberia',
        13: "Yekepa Mount Nimba Liberia",
        14: 'incategory:"Gbarnga" Liberia',
        15: "Kpatawee Waterfall Liberia",
        16: "Gola Forest Liberia",
        17: "Loguatuo Liberia border",
    },
    "costa-de-marfil": {
        1: 'incategory:"Mount Nimba Strict Nature Reserve" Ivory Coast',
        2: 'incategory:"Man, Ivory Coast"',
        3: "Dent de Man Cote d'Ivoire",
        4: "Mont Tonkoui Cote d'Ivoire",
        5: "Cascade de Man Cote d'Ivoire",
        6: "Pont de lianes Lieupleu Cote d'Ivoire",
        7: "Gbêtitapéa waterfall Cote d'Ivoire",
        8: 'incategory:"Basilica of Our Lady of Peace of Yamoussoukro"',
        9: 'incategory:"Taï National Park"',
        10: "Mont Nienokoue Tai Cote d'Ivoire",
        11: 'incategory:"Sassandra" Ivory Coast',
        12: "Grand Lahou Azagny National Park Cote d'Ivoire",
        13: 'incategory:"Abidjan" Plateau',
        14: 'incategory:"Grand-Bassam" historic',
        15: "Assinie Mafia Cote d'Ivoire lagoon",
        16: "Sudanese mosque Bondoukou Sorobango Cote d'Ivoire",
        17: 'incategory:"Comoé National Park" Ivory Coast',
        18: 'incategory:"Bouaké" Ivory Coast',
        19: "Katiola pottery Mangoro Cote d'Ivoire",
        20: 'incategory:"Korhogo" Ivory Coast',
        21: 'incategory:"Séguéla" Ivory Coast',
        22: "Biankouma Sipilou Cote d'Ivoire",
    },
    "marruecos": {
        1: 'incategory:"Chefchaouen" medina',
        2: 'incategory:"Volubilis"',
        3: 'incategory:"Fes el Bali" tanneries',
        4: 'incategory:"Erg Chebbi"',
        5: 'incategory:"Todgha Gorge"',
        6: 'incategory:"Ait Benhaddou"',
        7: 'incategory:"Jemaa el-Fnaa"',
        8: 'incategory:"Tizi n Test"',
        9: 'incategory:"Essaouira" port medina',
        10: 'incategory:"Tafraout" Ameln',
        11: 'incategory:"Legzira" arch',
        12: 'incategory:"Sidi Ifni"',
        13: 'Khenifiss lagoon Morocco',
        14: 'incategory:"Tarfaya"',
    },
    "sahara-occidental": {
        1: 'incategory:"Laayoune" cathedral',
        2: 'Foum El Oued Laayoune beach',
        3: 'Bou Craa conveyor belt Western Sahara',
        4: 'Lemsid Western Sahara',
        5: 'incategory:"Boujdour" Western Sahara',
        6: 'White Dune Dakhla Western Sahara',
        7: 'Dakhla Bay lagoon Western Sahara',
        8: 'incategory:"Dakhla, Western Sahara"',
        9: 'Dakhla kitesurf lagoon',
        10: 'Bir Gandouz Western Sahara',
        11: 'incategory:"Guerguerat" border crossing',
        12: 'Cintra Bay Western Sahara',
        13: 'Imlili Sebkha fish pools Western Sahara',
        14: 'Asmaa hot spring Dakhla Western Sahara',
        15: 'incategory:"Smara" Ma al Aynayn',
        16: 'Cabo Blanco monk seal La Guera Western Sahara',
    },
    "mauritania": {
        1: 'incategory:"Ben Amera" Mauritania',
        2: 'Aicha monolith Mauritania Ben Amera',
        3: 'incategory:"Chinguetti"',
        4: 'incategory:"Ouadane"',
        5: 'Terjit oasis Mauritania',
        6: 'incategory:"Atar, Mauritania"',
        7: 'incategory:"Richat Structure"',
        8: 'incategory:"Banc d Arguin National Park" Mauritania',
        9: 'Port de Peche Nouakchott Mauritania',
        10: 'Diawling National Park Mauritania',
        11: 'Tifoujar Pass Mauritania',
        12: 'Vallee Blanche Adrar Mauritania',
    },
    "senegal": {
        1: 'incategory:"Saloum Delta" Senegal',
        2: 'incategory:"Djoudj National Bird Sanctuary"',
        3: 'incategory:"Saint-Louis, Senegal" island',
        4: 'Guet Ndar Saint Louis Senegal',
        5: 'Langue de Barbarie Senegal',
        6: 'incategory:"Lake Retba" Senegal',
        7: 'incategory:"Goree" Senegal',
        8: 'Museum of Black Civilisations Dakar',
        9: 'incategory:"African Renaissance Monument"',
        10: 'incategory:"Fadiouth" Senegal',
        11: 'Toubacouta Saloum Senegal',
        12: 'incategory:"Niokolo-Koba National Park"',
        13: 'incategory:"Kedougou" Senegal',
        14: 'Bandafassi Senegal Bassari',
        15: 'Iwol Bedik Senegal',
        16: 'Dindefelo waterfall Senegal',
        17: 'Ethiolo Bassari Senegal',
        18: 'Theodore Monod Museum Dakar',
        19: 'Ferlo North Wildlife Reserve Senegal',
        20: 'Katane Ferlo Senegal wildlife',
        21: 'Ranerou Senegal Ferlo',
        22: 'Ferlo South Wildlife Reserve Senegal',
        23: 'Ferlo track Senegal Ranerou Tambacounda',
    },
    "gambia": {
        1: 'Kartong Gambia beach Folonko',
        2: 'Tanji Gambia fishing village museum',
        3: 'incategory:"Abuko Nature Reserve"',
        4: 'Makasutu Gambia forest Mandina Bolong',
        5: 'incategory:"Bijilo Forest Park"',
        6: 'Kotu Bridge Gambia birds beach',
        7: 'Kachikally crocodile pool Gambia',
        8: 'Serrekunda market Gambia',
        9: 'incategory:"Banjul" Arch 22 Albert Market',
        10: 'Banjul Barra ferry Gambia',
        11: 'Fort Bullen Gambia Barra',
        12: 'Juffureh Albreda Gambia slavery museum',
        13: 'incategory:"Kunta Kinteh Island"',
        14: 'Niumi National Park Jinack Gambia',
        15: 'Kiang West National Park Tendaba Gambia',
        16: 'Bao Bolong Wetland Reserve Gambia',
        17: 'Janjanbureh Georgetown Gambia',
        18: 'incategory:"Wassu stone circles"',
        19: 'River Gambia National Park chimpanzee Baboon Islands',
    },
    "namibia": {
        1: 'incategory:"Fish River Canyon" Namibia',
        2: 'incategory:"Quiver Tree Forest" Namibia',
        3: "Garub desert horses Namibia",
        4: 'incategory:"Lüderitz" waterfront',
        5: 'incategory:"Kolmanskop"',
        6: 'incategory:"Dune 45"',
        7: 'incategory:"Deadvlei"',
        8: "Kuiseb Canyon Namibia",
        9: 'incategory:"Walvis Bay Lagoon"',
        10: 'incategory:"Sandwich Harbour"',
        11: 'incategory:"Swakopmund" jetty',
        12: 'incategory:"Spitzkoppe"',
        13: 'incategory:"Cape Cross" fur seals',
        14: "Messum Crater Namibia",
        15: 'incategory:"White Lady rock painting" Namibia',
        16: 'incategory:"Twyfelfontein"',
        17: "Palmwag Namibia",
        18: 'incategory:"Skeleton Coast National Park"',
        19: "Okaukuejo waterhole Etosha",
        20: "Van Zyl's Pass Namibia",
        21: 'incategory:"Epupa Falls"',
        22: "Ruacana Falls Namibia",
        23: 'incategory:"Independence Memorial Museum, Namibia"',
        24: 'incategory:"Waterberg Plateau Park" Namibia',
    },
    "zimbabue": {
        1: "Christmas Pass Mutare Zimbabwe", 2: "Vumba Botanical Garden Zimbabwe",
        3: "Mount Nyangani Zimbabwe", 4: "Mtarazi Falls Zimbabwe",
        5: "Ziwa ruins Zimbabwe", 6: "Chimanimani National Park Zimbabwe",
        7: 'incategory:"Great Zimbabwe"', 8: "Lake Mutirikwi Zimbabwe",
        9: "Chilojo Cliffs Gonarezhou", 10: "Natural History Museum Bulawayo",
        11: 'incategory:"Matobo National Park"', 12: 'incategory:"Khami" Zimbabwe',
        13: 'incategory:"Hwange National Park"', 14: 'incategory:"Victoria Falls" Zimbabwe',
        15: 'incategory:"Victoria Falls Bridge"', 16: "Zambezi National Park Zimbabwe",
        17: 'incategory:"National Gallery of Zimbabwe"', 18: "Domboshawa Zimbabwe rock art",
        19: "Chinhoyi Caves Zimbabwe", 20: "Mana Pools Nyamepi Zimbabwe",
        21: 'incategory:"Kariba Dam"', 22: "Chizarira National Park Zimbabwe",
    },
    "botsuana": {
        1: 'incategory:"Kazungula Bridge"', 2: 'incategory:"Chobe National Park" riverfront',
        3: "Savuti Botswana", 4: "Linyanti Botswana",
        5: "Khwai Botswana", 6: "Xakanaxa Moremi Botswana",
        7: "Mboma Island Botswana", 8: 'incategory:"Maun" Botswana',
        9: 'incategory:"Okavango Delta" mokoro', 10: "Shakawe Botswana Okavango",
        11: 'incategory:"Tsodilo"', 12: "Gcwihaba Caves Botswana",
        13: "D'Kar Kuru Art Botswana", 14: "Deception Valley Central Kalahari",
        15: 'incategory:"Baines Baobabs"', 16: "Boteti River Makgadikgadi Botswana",
        17: 'incategory:"Kubu Island"', 18: "Nata Bird Sanctuary Botswana",
        19: "Khama Rhino Sanctuary Botswana", 20: "Northern Tuli Botswana Pont Drift",
        21: 'incategory:"Three Dikgosi Monument"',
    },
    "sudafrica": {
        1: 'incategory:"Apartheid Museum"', 2: 'incategory:"Mandela House" Soweto',
        3: 'incategory:"Maropeng" South Africa', 4: 'incategory:"Three Rondavels"',
        5: 'incategory:"Kruger National Park"', 6: 'incategory:"iSimangaliso Wetland Park"',
        7: 'incategory:"Hluhluwe-iMfolozi Park"', 8: "KwaMuhle Museum Durban",
        9: 'incategory:"Amphitheatre, Drakensberg"', 10: 'incategory:"Golden Gate Highlands National Park"',
        11: 'incategory:"Sani Pass"', 12: 'incategory:"Hole in the Wall, South Africa"',
        13: 'incategory:"Storms River Mouth"', 14: 'incategory:"Cango Caves"',
        15: 'incategory:"Cape Agulhas"', 16: 'incategory:"Old Harbour, Hermanus"',
        17: 'incategory:"Table Mountain Aerial Cableway"', 18: 'incategory:"Cape of Good Hope"',
        19: 'incategory:"Robben Island"', 20: 'incategory:"Stellenbosch Village Museum"',
        21: 'incategory:"Cederberg"', 22: 'incategory:"South African Large Telescope"',
        23: 'incategory:"Kgalagadi Transfrontier Park"', 24: 'incategory:"Augrabies Falls"',
        25: 'incategory:"Namaqua National Park"', 26: 'incategory:"Richtersveld"',
    },
    "esuatini": {
        1: "Lion Cavern Ngwenya Eswatini", 2: "Ngwenya Glass Eswatini",
        3: 'incategory:"Malolotja Nature Reserve"', 4: "Malolotja Canopy Tour Eswatini",
        5: 'incategory:"Maguga Dam"', 6: "Nsangwini Rock Art Eswatini",
        7: "Phophonyane Falls Eswatini", 8: 'incategory:"Mbabane"',
        9: "Sibebe Rock Eswatini", 10: "Ezulwini Eswatini",
        11: "Mantenga Cultural Village Eswatini", 12: 'incategory:"Mlilwane Wildlife Sanctuary"',
        13: 'incategory:"Manzini" Eswatini', 14: "Mkhaya Game Reserve Eswatini",
        15: 'incategory:"Hlane Royal National Park"', 16: "Shewula Mountain Camp Eswatini",
    },
    "lesoto": {
        1: "Butha-Buthe Mountain Lesotho", 2: "Tsehlanyane National Park Lesotho",
        3: "Liphofung Cave Lesotho", 4: "Moteng Pass Lesotho",
        5: "Afriski Lesotho", 6: "Tlaeeng Pass Lesotho",
        7: 'incategory:"Mokhotlong"', 8: "Thabana Ntlenyana Lesotho",
        9: 'incategory:"Sani Pass"', 10: "Sani Top Lesotho",
        11: 'incategory:"Katse Dam"', 12: "Bokong Nature Reserve Lesotho",
        13: 'incategory:"Mohale Dam"', 14: 'incategory:"Maseru"',
        15: 'incategory:"Thaba Bosiu"', 16: "Morija Museum Lesotho",
        17: "Malealea Lesotho", 18: 'incategory:"Maletsunyane Falls"',
        19: "Masitise Cave House Lesotho", 20: 'incategory:"Sehlabathebe National Park"',
    },
    "uganda": {
        1: "Sipi Falls Uganda", 2: 'incategory:"Mount Elgon" Uganda',
        3: "Source of the Nile Jinja Uganda", 4: 'incategory:"Kampala" Uganda',
        5: "Entebbe Botanical Gardens Uganda", 6: "Ssese Islands Uganda",
        7: "Ziwa Rhino Sanctuary Uganda", 8: "Murchison Falls Uganda",
        9: 'incategory:"Kidepo Valley National Park"', 10: "Fort Patiko Uganda",
        11: "Fort Portal crater lakes Uganda", 12: 'incategory:"Kibale National Park"',
        13: 'incategory:"Rwenzori Mountains"', 14: "Lake Katwe salt Uganda",
        15: "Kazinga Channel Uganda", 16: "Ishasha Uganda tree climbing lions",
        17: 'incategory:"Bwindi Impenetrable National Park"',
        18: 'incategory:"Mgahinga Gorilla National Park"',
        19: 'incategory:"Lake Bunyonyi"', 20: 'incategory:"Lake Mburo National Park"',
    },
    "ruanda": {
        1: "Musanze Caves Rwanda", 2: 'incategory:"Volcanoes National Park, Rwanda"',
        3: "Mount Bisoke Rwanda crater lake", 4: "Karisoke Dian Fossey Rwanda",
        5: "Lake Burera Lake Ruhondo Rwanda", 6: "Rubavu Gisenyi Lake Kivu Rwanda",
        7: "Congo Nile Trail Rwanda", 8: "Karongi Kibuye Lake Kivu Rwanda",
        9: "Rusizi Cyangugu Rwanda Lake Kivu", 10: 'incategory:"Nyungwe Forest"',
        11: "Ethnographic Museum Huye Rwanda", 12: "King's Palace Museum Nyanza Rwanda",
        13: 'incategory:"Kigali"', 14: "Kigali Genocide Memorial",
        15: "Nyamata Genocide Memorial", 16: "Lake Muhazi Rwanda",
        17: 'incategory:"Akagera National Park"', 18: "Gishwati Forest Rwanda",
    },
    "malaui": {
        1: "Karonga Museum Malawi", 2: "Livingstonia Malawi Stone House",
        3: "Manchewe Falls Malawi", 4: 'incategory:"Nyika National Park"',
        5: "Mzuzu Malawi", 6: "Nkhata Bay Malawi",
        7: "Bandawe Mission Malawi", 8: "Likoma Cathedral Malawi",
        9: "Nkhotakota Wildlife Reserve Malawi", 10: "Livingstone Tree Nkhotakota Malawi",
        11: "Senga Bay Malawi", 12: "Kasungu National Park Malawi",
        13: "Lilongwe Malawi", 14: "Chongoni Rock Art Malawi",
        15: "Kungoni Centre Mua Malawi", 16: "Cape Maclear Lake Malawi National Park",
        17: "Liwonde National Park Malawi", 18: "Zomba Plateau Malawi",
        19: "Blantyre Malawi Mandala House", 20: 'incategory:"Mount Mulanje"',
        21: "Satemwa Tea Estate Malawi", 22: "Majete Wildlife Reserve Malawi",
    },
    "zambia": {
        1: 'incategory:"Liuwa Plain National Park"',
        2: "Kuomboka Mongu",
        3: 'incategory:"Kafue National Park"',
        4: 'incategory:"Lusaka"',
        5: 'incategory:"Mosi-oa-Tunya in Zambia"',
        6: 'incategory:"Victoria Falls Bridge"',
        7: 'incategory:"South Luangwa National Park"',
        8: 'incategory:"Kasanka National Park"',
        9: "Bangweulu Wetlands Zambia",
        10: "Ntumbachushi Falls Zambia",
        11: "Lumangwe Falls Zambia",
        12: "Chishimba Falls Zambia",
        13: "Mpulungu Lake Tanganyika Zambia",
        14: "Kalambo Falls Zambia",
    },
    "tanzania": {
        1: "Ngozi Crater Lake Tanzania",
        2: 'incategory:"Kitulo National Park"',
        3: 'incategory:"Katavi National Park"',
        4: "Livingstone Memorial Ujiji Tanzania",
        5: 'incategory:"Gombe Stream National Park"',
        6: 'incategory:"Ruaha National Park"',
        7: "Sanje Falls Udzungwa Tanzania",
        8: "Isimila Stone Age Site Tanzania",
        9: 'incategory:"Tarangire National Park"',
        10: 'incategory:"Lake Manyara National Park"',
        11: 'incategory:"Ngorongoro Crater"',
        12: 'incategory:"Olduvai Gorge"',
        13: 'incategory:"Serengeti National Park"',
        14: 'incategory:"Lake Natron"',
        15: 'incategory:"Ol Doinyo Lengai"',
        16: "Arusha Mount Meru Tanzania",
        17: 'incategory:"Mount Kilimanjaro"',
        18: "Amboni Caves Tanzania",
        19: "Lushoto Usambara Mountains Tanzania",
        20: "Pangani Tanzania Saadani National Park",
        21: "Kaole Ruins Bagamoyo Tanzania",
        22: 'incategory:"Dar es Salaam"',
        23: 'incategory:"Stone Town"',
        24: "Nyerere National Park Tanzania Rufiji",
        25: "Kilwa Kisiwani Songo Mnara Tanzania",
        26: "Mtwara Tanzania Makonde Plateau",
    },
    "kenia": {
        1: 'incategory:"Nairobi National Museum"',
        2: 'incategory:"Amboseli National Park"',
        3: 'incategory:"Mount Longonot"',
        4: 'incategory:"Lake Nakuru National Park"',
        5: 'incategory:"Lake Bogoria National Reserve"',
        6: 'incategory:"Mount Kenya"',
        7: 'incategory:"Samburu National Reserve"',
        8: 'incategory:"Marsabit National Park"',
        9: 'incategory:"Maasai Mara National Reserve"',
        10: 'incategory:"Tsavo West National Park"',
        11: 'incategory:"Fort Jesus"',
        12: 'incategory:"Diani Beach"',
        13: 'incategory:"Lamu Old Town"',
    },
    "mozambique": {
        1: 'incategory:"Lichinga"',
        2: "Metangula Lake Niassa Mozambique",
        3: "Niassa Special Reserve Mozambique wildlife",
        4: "Cuamba Mozambique railway station",
        5: "Gurue tea Mount Namuli Mozambique",
        6: "Nampula Mozambique ethnology museum",
        7: 'incategory:"Fortress of São Sebastião"',
        8: "Chocas Mar Mozambique",
        9: "Pemba Mozambique port",
        10: 'incategory:"Quelimane"',
        11: "Armando Guebuza Bridge Caia Mozambique",
        12: 'incategory:"Cahora Bassa Dam"',
        13: 'incategory:"Gorongosa National Park"',
        14: "Mount Gorongosa Morombodzi Falls Mozambique",
        15: 'incategory:"Beira, Mozambique"',
        16: "Chinhamapere rock art Mozambique",
        17: "Mount Binga Mozambique Chimanimani",
        18: "Inhassoro Mozambique beach",
        19: 'incategory:"Bazaruto Archipelago"',
        20: "Tofo Beach Mozambique",
        21: 'incategory:"Maputo Railway Station"',
        22: "Ponta do Ouro Mozambique",
    },
}


def plain(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    return " ".join(html.unescape(value).split())


def search(query: str, limit: int) -> list[dict[str, str]]:
    params = {
        "action": "query",
        "generator": "search",
        "gsrnamespace": "6",
        "gsrlimit": str(limit),
        "gsrsearch": query,
        "prop": "imageinfo",
        "iiprop": "url|extmetadata",
        "iiurlwidth": "1200",
        "format": "json",
        "origin": "*",
    }
    request = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": "Africa2027-content-audit/1.0"},
    )
    context = ssl.create_default_context(cafile=certifi.where())
    for attempt in range(6):
        try:
            with urllib.request.urlopen(request, timeout=30, context=context) as response:
                data = json.load(response)
            break
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == 5:
                raise
            time.sleep(min(30, 4 * (attempt + 1)))
    time.sleep(2.2)
    pages = sorted(
        data.get("query", {}).get("pages", {}).values(),
        key=lambda page: page.get("index", 10_000),
    )
    result = []
    for page in pages:
        info = (page.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata", {})
        result.append(
            {
                "title": page.get("title", ""),
                "description": plain(meta.get("ImageDescription", {}).get("value", "")),
                "categories": meta.get("Categories", {}).get("value", ""),
                "artist": plain(meta.get("Artist", {}).get("value", "")),
                "license": meta.get("LicenseShortName", {}).get("value", ""),
                "source": info.get("descriptionurl", ""),
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("country", choices=tuple(SEARCH_QUERIES))
    parser.add_argument("--number", type=int)
    parser.add_argument("--from", dest="first", type=int)
    parser.add_argument("--to", dest="last", type=int)
    parser.add_argument("--query")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()

    pois = json.loads((ROOT / "content" / "pois" / f"{args.country}.json").read_text())
    if args.number:
        pois = [poi for poi in pois if poi["n"] == args.number]
    if args.first:
        pois = [poi for poi in pois if poi["n"] >= args.first]
    if args.last:
        pois = [poi for poi in pois if poi["n"] <= args.last]
    for poi in pois:
        query = args.query if len(pois) == 1 and args.query else SEARCH_QUERIES.get(args.country, {}).get(poi["n"], poi["name"].split("·")[0].strip())
        items = search(query, args.limit)
        if args.compact:
            items = [
                {key: item[key] for key in ("title", "description", "artist", "license")}
                for item in items
            ]
        print(json.dumps({"n": poi["n"], "name": poi["name"], "query": query, "items": items}, ensure_ascii=False))


if __name__ == "__main__":
    main()

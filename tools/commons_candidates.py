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

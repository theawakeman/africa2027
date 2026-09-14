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
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=30, context=context) as response:
                data = json.load(response)
            break
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == 4:
                raise
            time.sleep(2 ** attempt)
    time.sleep(0.8)
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
    parser.add_argument("country", choices=("zambia", "tanzania", "kenia", "mozambique"))
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

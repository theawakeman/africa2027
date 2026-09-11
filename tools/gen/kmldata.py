"""Parse the 8-sep-2026 KML export of the shared My Maps."""
import html, re
import xml.etree.ElementTree as ET
from pathlib import Path

KML = Path(__file__).parent.parent / "doc.kml"

def parse_kml():
    ns = {"k": "http://www.opengis.net/kml/2.2"}
    tree = ET.parse(KML)
    items = {}
    for pm in tree.findall(".//k:Placemark", ns):
        name_el = pm.find("k:name", ns); coord_el = pm.find(".//k:coordinates", ns); desc_el = pm.find("k:description", ns)
        if name_el is None or coord_el is None:
            continue
        name = (name_el.text or "").strip()
        desc = desc_el.text or "" if desc_el is not None else ""
        coords = (coord_el.text or "").strip().split(",")
        if len(coords) < 2:
            continue
        photo_match = re.search(r"Fotografía:\s*(.*?)(?:<br>|Fuente:)", desc, flags=re.S | re.I)
        source_match = re.search(r"Fuente:\s*(.*?)(?:\]\]>|$)", desc, flags=re.S | re.I)
        clean = re.sub(r"<br\s*/?>", "\n", desc, flags=re.I)
        clean = re.sub(r"<img[^>]*>", "", clean, flags=re.I)
        clean = re.sub(r"<[^>]+>", "", clean)
        clean = html.unescape(clean)
        clean = re.sub(r"\n{2,}", "\n", clean).strip()
        narrative = clean.split("Fotografía:")[0].strip()
        items[name] = {
            "lon": float(coords[0]), "lat": float(coords[1]),
            "description": narrative,
            "credit": html.unescape(re.sub(r"<[^>]+>", "", photo_match.group(1)).strip()) if photo_match else "Crédito indicado en My Maps",
            "source": html.unescape(re.sub(r"<[^>]+>", "", source_match.group(1)).strip()) if source_match else "",
        }
    return items

def clean_desc(raw):
    """Split KML narrative into (clean description, dog note)."""
    d = re.sub(r"\s*Info:\s*\S+\s*$", "", raw, flags=re.S)
    m = re.search(r"PERRO:\s*(.*)$", d, flags=re.S)
    dog_note = re.sub(r"\s*Info:\s*\S+\s*$", "", m.group(1), flags=re.S).strip() if m else ""
    d = re.sub(r"PERRO:.*$", "", d, flags=re.S).strip()
    d = re.sub(r"^[^a-záéíóúüñ]*(?=[A-ZÁÉÍÓÚÑ][a-záéíóúüñ])", "", d)
    return d, dog_note

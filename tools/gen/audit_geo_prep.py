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
        bb = BBOX.get(slug)
        bbox = [bb[2] - 0.3, bb[0] - 0.3, bb[3] + 0.3, bb[1] + 0.3] if bb else None  # minLon,minLat,maxLon,maxLat
        data = {"slug": slug, "bbox": bbox, "items": items}
        (OUT / f"{slug}_queries.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print(slug, len(pois), "PDIs,", len(items) - len(pois), "logística →", OUT / f"{slug}_queries.json")


if __name__ == "__main__":
    main(sys.argv[1:])

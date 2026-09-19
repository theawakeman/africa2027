# -*- coding: utf-8 -*-
"""Monta tools/gen/data_<slug>.py y da de alta el país en el resto de tablas de la app.

Uso: python3 assemble_country.py <slug>
Entradas en scratchpad/<slug>/: pdis.json, operativo.json, gm_results.json, photo_sel.json, photo_meta.json
y opcionalmente extra.json (hero: n del PDI de portada; notice; ruta_intro; fix: {n: [[a,b],...]}).
Historia: audit/historia/<slug>.json. Parámetros: scratchpad/paises.json.
"""
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
SCRATCH = Path(os.environ.get("A27_SCRATCH", HERE.parent))
REPO = Path(os.environ.get("A27_REPO", "/home/claude/africa2027"))
GEN = REPO / "tools/gen"
REVISION = "18 sep 2026"
GRUPOS = {"vuelo": "SOLO ALCANZABLE EN AVIÓN", "excluido": "EXCLUIDO POR PROTOCOLO", "fuera": "FUERA DE LA RUTA PREVISTA",
          "alternativa": "ALTERNATIVA"}


def s(v):
    return json.dumps(v, ensure_ascii=False)


def fmt_list_str(items, ind="        "):
    return "[\n" + "".join(f"{ind}{s(x)},\n" for x in items) + ind[:-4] + "]"


def fmt_rows(rows, ind="    "):
    return "[\n" + "".join(f"{ind}({', '.join(s(c) for c in r)}),\n" for r in rows) + ind[:-4] + "]"


def fmt_poi(p):
    out = ["    dict(",
           f"        n={p['n']}, name={s(p['name'])}, cat={s(p['cat'])}, prio={s(p['prio'])},",
           f"        dog={s(p['dog'])}, time={s(p['time'])},",
           f"        lat={p['lat']}, lon={p['lon']},  # Google Maps: {p['_gm']}",
           f"        desc={s(p['desc'])},",
           f"        dog_note={s(p['dog_note'])},",
           "        visit={"]
    for k in ("why", "see", "access", "when", "skip"):
        out.append(f"            {s(k)}: {s(p['visit'].get(k, ''))},")
    out.append("        },")
    out.append("        links=[")
    for l in p["links"]:
        out.append(f"            {{\"label\": {s(l['label'])}, \"url\": {s(l['url'])}}},")
    out.append("        ],")
    out.append("        photos=[")
    for ph in p["photos"]:
        out.append("            {")
        for k in ("img", "source", "credit", "caption"):
            out.append(f"                {s(k)}: {s(ph[k])},")
        out.append("            },")
    out.append("        ],")
    out.append("    ),")
    return "\n".join(out)


def fmt_log(rows):
    out = ["["]
    for name, cat, lat, lon, info, gmn in rows:
        out.append(f"    ({s(name)}, {s(cat)}, {lat}, {lon},  # Google Maps: {gmn}")
        out.append(f"     {s(info)}),")
    out.append("]")
    return "\n".join(out)


def fmt_hist_secs(secs):
    out = ["["]
    for t, b in secs:
        out.append(f"    ({s(t)},")
        out.append(f"     {s(b)}),")
    out.append("]")
    return "\n".join(out)


def pick_fact(facts, *needles):
    for k, v in facts:
        for n in needles:
            if n.lower() in k.lower():
                return v
    return ""


def short(v, limit):
    v = re.sub(r"\s+", " ", v).strip()
    if len(v) <= limit:
        return v
    cut = v[:limit + 1]
    for sep in (" · ", "; ", ". ", ", ", " "):
        pos = cut.rfind(sep)
        if pos >= limit // 2:
            return cut[:pos].rstrip(" ,;") + "…"
    return cut[:limit].rstrip() + "…"


def main(slug):
    D = SCRATCH / slug
    params = json.loads((SCRATCH / "paises.json" if (SCRATCH / "paises.json").exists() else HERE / "paises.json").read_text())[slug]
    pdis = json.loads((D / "pdis.json").read_text())
    op = json.loads((D / "operativo.json").read_text())
    gm = json.loads((D / "gm_results.json").read_text())
    sel = json.loads((D / "photo_sel.json").read_text())
    meta = {m["t"]: m for m in json.loads((D / "photo_meta.json").read_text())}
    hist = json.loads((REPO / "audit/historia" / f"{slug}.json").read_text())
    extra = json.loads((D / "extra.json").read_text()) if (D / "extra.json").exists() else {}
    sys.path.insert(0, str(GEN))
    from data_countries import C
    name, group = next((n, g) for sl, n, g, *_ in C if sl == slug)
    modname = "data_" + slug.replace("-", "_")

    def commons(filename, caption):
        m = meta["File:" + filename]
        assert not m["missing"], filename
        encoded = quote(filename.replace(" ", "_"), safe="(),-._~'")
        credit = f"{m['a']} · {m['l']}" if m["a"] else f"Wikimedia Commons · {m['l']}"
        return {"img": f"https://commons.wikimedia.org/wiki/Special:FilePath/{encoded}?width=1200",
                "source": f"https://commons.wikimedia.org/wiki/File:{encoded}", "credit": credit, "caption": caption}

    # ---- PDIs
    fix = {int(k): v for k, v in extra.get("fix", {}).items()}
    POIS = []
    for x in pdis["pois"]:
        n = x["n"]
        g = gm[f"poi-{n}"]
        desc = x["desc"]
        for a, b in fix.get(n, []):
            desc = desc.replace(a, b)
        photos = [commons(f, cap) for f, cap in sel[str(n)]]
        POIS.append({"n": n, "name": x["name"], "cat": x["cat"], "prio": x["prio"], "dog": x["dog"], "time": x["time"],
                     "lat": round(float(g["lat"]), 7), "lon": round(float(g["lon"]), 7), "desc": desc,
                     "dog_note": x.get("dog_note", ""), "visit": x["visit"], "links": x["links"], "photos": photos,
                     "_gm": g["name"]})

    # ---- logística
    LOG = []
    for i, l in enumerate(op["logistics"]):
        g = gm[f"log-{i}"]
        info = re.sub(r"\s*Coordenadas?[^.]*\.", "", l["info"])
        info = re.sub(r"\s*[^.]*por verificar[^.]*\.", "", info)
        info = re.sub(r"\s*[^.]*por confirmar en Google Maps[^.]*\.", "", info)
        info = info.strip()
        if not info.endswith("."):
            info += "."
        info += f" Pin comprobado en Google Maps («{g['name']}»)."
        LOG.append((l["name"], l["cat"], round(float(g["lat"]), 7), round(float(g["lon"]), 7), info, g["name"]))

    # ---- fuentes
    SOURCES = [tuple(x) for x in op["sources"]]
    seen = {u for _, u in SOURCES}
    for x in pdis["pois"]:
        for l in x.get("links", []):
            if l["url"] not in seen:
                SOURCES.append((l["label"], l["url"]))
                seen.add(l["url"])
    for t, u in extra.get("sources", []):
        if u not in seen:
            SOURCES.append((t, u)); seen.add(u)

    # ---- corredores (PDIs verificados en el orden de la investigación + puntos intermedios)
    def snap(pts):
        out = []
        P = [(p["lat"], p["lon"]) for p in POIS]
        for la, lo in pts:
            best = min(P, key=lambda q: (q[0] - la) ** 2 + (q[1] - lo) ** 2)
            d = ((best[0] - la) ** 2 + (best[1] - lo) ** 2) ** 0.5
            out.append((round(best[0], 5), round(best[1], 5)) if d < 0.15 else (round(la, 5), round(lo, 5)))
        dedup = []
        for pt in out:
            if not dedup or dedup[-1] != pt:
                dedup.append(pt)
        return dedup
    CORRIDOR = snap(pdis.get("corridor", []))
    CORRIDOR_ALT = snap(pdis.get("corridor_alt", []))
    lats = [p["lat"] for p in POIS]; lons = [p["lon"] for p in POIS]
    center = [round((max(lats) + min(lats)) / 2, 2), round((max(lons) + min(lons)) / 2, 2)]
    span = max(max(lats) - min(lats), (max(lons) - min(lons)) * 0.8)
    zoom = 7 if span < 4 else 6 if span < 8 else 5

    # ---- chips y cabecera
    facts = [tuple(r) for r in op["facts"]]
    chips = [("ESTATUS", short(pick_fact(facts, "Estatus"), 110)),
             ("CÓMO LLEGAR", short(pick_fact(facts, "Cómo llegar"), 110)),
             ("VISADO", short(pick_fact(facts, "Visado"), 90)),
             ("VEHÍCULO", short(pick_fact(facts, "Vehículo"), 110))]
    chips += [tuple(c) for c in op["chips_extra"]]
    chips += [("PERRO", short(pick_fact(facts, "Perro"), 110)), ("MONEDA", short(pick_fact(facts, "Moneda"), 90)),
              ("VENTANA", short(pick_fact(facts, "Clima"), 90))]

    hero_n = extra.get("hero", POIS[0]["n"])
    hero_poi = next(p for p in POIS if p["n"] == hero_n)
    hero = hero_poi["photos"][0]
    grupo_txt = GRUPOS.get(group, group.upper())
    notice = extra.get("notice") or (
        f"Documento de planificación de un país {grupo_txt}: no forma parte de la ruta 2027. "
        "La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. "
        "Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.")
    ruta_intro = extra.get("ruta_intro") or (
        f"Itinerario de referencia que enlaza los {len(POIS)} puntos de interés por las carreteras principales, calculado sobre 250 km/día. "
        "No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.")
    corr_label = pdis.get("corridor_label") or "Itinerario de referencia"
    corr_alt_label = pdis.get("corridor_alt_label") or "Variante"

    doc = extra.get("doc") or (
        f"{name} — ficha completa ({REVISION}): {grupo_txt}.\n\n{params['CONTEXTO']}\n\n"
        "Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI "
        "(autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con "
        "fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. "
        f"Expediente: audit/historia/{slug}.json y audit/pdi/{slug}.md.")

    py = f'''# -*- coding: utf-8 -*-
"""{doc}
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
{chr(10).join(fmt_poi(p) for p in POIS)}
]

_CAT_COLOR = {{"naturaleza": "verde", "ciudad · servicios": "azul", "cultura": "morado",
              "patrimonio unesco": "marron", "costa": "turquesa"}}
for _p in POIS:
    # La portada de la tarjeta, el globo del mapa y el modal es siempre la primera foto de la galería.
    _p["img"] = _p["photos"][0]["img"]
    _p["source"] = _p["photos"][0]["source"]
    _p["credit"] = _p["photos"][0]["credit"]
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")

LOGISTICS = {fmt_log(LOG)}

DRONE_CALLOUT = ({s(op["drones_callout"][0])}, {s(op["drones_callout"][1])},
                 {s(op["drones_callout"][2])})

STARLINK_CALLOUT = ({s(op["starlink_callout"][0])}, {s(op["starlink_callout"][1])},
                    {s(op["starlink_callout"][2])})

DOG_MATRIX = {fmt_rows([tuple(r) for r in op["dog_matrix"]])}

SOURCES = {fmt_rows(SOURCES)}

# {corr_label}
CORRIDOR = {fmt_rows(CORRIDOR)}

# {corr_alt_label}
CORRIDOR_ALT = {fmt_rows(CORRIDOR_ALT)}

HISTORIA_RESUMEN = {s(hist["historia_resumen"])}

HISTORIA_SECCIONES = {fmt_hist_secs(hist["historia_secciones"])}

HISTORIA_FUENTES = {fmt_rows([tuple(f) for f in hist["historia_fuentes"]])}

SPEC = dict(
    slug={s(slug)}, name={s(name)}, revision={s(REVISION)},
    sub={s(op["sub"])},
    chips={fmt_rows(chips, ind="        ")},
    center={center}, zoom={zoom},
    notice={s(notice)},
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label={s(corr_label)},
    corridor_alt_label={s(corr_alt_label)},
    hero_img={s(hero["img"])},
    hero_credit={s(hero_poi["name"].split("·")[0].strip() + " · " + hero["credit"])},
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision={s(op["decision"])},
    facts={fmt_rows(facts, ind="        ")},
    alerts={fmt_list_str(op["alerts"])},
    ruta_intro={s(ruta_intro)},
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows={fmt_rows([tuple(r) for r in pdis["route_rows"]], ind="        ")},
    offroad={fmt_list_str(pdis["offroad"])},
    senderismo={fmt_list_str(pdis["senderismo"])},
    acampada={fmt_list_str(pdis["acampada"])},
    visado={fmt_list_str(op["visado"])},
    fronteras_rows={fmt_rows([tuple(r) for r in op["fronteras_rows"]], ind="        ")},
    vehiculos={fmt_list_str(op["vehiculos"])},
    drones_callout=DRONE_CALLOUT,
    drones={fmt_list_str(op["drones"])},
    starlink_callout=STARLINK_CALLOUT,
    starlink={fmt_list_str(op["starlink"])},
    perro_intro={fmt_list_str(op["perro_intro"])},
    dog_matrix=DOG_MATRIX,
    salud={fmt_list_str(op["salud"])},
    seguridad_intro={s(op["seguridad_intro"])},
    seguridad={fmt_list_str(op["seguridad"])},
    agua={fmt_list_str(op["agua"])},
    combustible={fmt_list_str(op["combustible"])},
    experiencias_intro={s(op["experiencias_intro"])},
    experiencias={fmt_list_str(op["experiencias"])},
    pendientes={fmt_rows([tuple(r) for r in op["pendientes"]], ind="        ")},
    sources=SOURCES,
    sources_note={s(op["sources_note"])},
    emergency={s(op["emergency"])},
)


def get_data(root="../../"):
    return make_ficha(SPEC)
'''
    (GEN / f"{modname}.py").write_text(py, encoding="utf-8")
    print("escrito", GEN / f"{modname}.py", len(py), "bytes")
    registrar(slug, name, group, op, params)


def registrar(slug, name, group, op, params):
    """Da de alta el país en build.py, cabeceras, visados, CPD y contactos del perro (idempotente)."""
    # build.py (lista de módulos y capa KML)
    p = GEN / "build.py"; t = p.read_text()
    if f'"{slug}"' not in t.split("# ---- PDIs editables")[0]:
        t = re.sub(r'("madagascar", "tunez"[^\]]*)\]:', lambda m: m.group(1) + f', "{slug}"]:', t, count=1)
        t = t.replace('"11 Fuera de ruta": ["tunez"', f'"11 Fuera de ruta": ["tunez", "{slug}"', 1)
        p.write_text(t)
    for f in ("migrate_ficha.py", "migrate_pois.py"):
        p = GEN / f; t = p.read_text()
        if f'"{slug}"' not in t:
            t = re.sub(r'("madagascar", "tunez"[^\]]*)\]:', lambda m: m.group(1) + f', "{slug}"]:', t, count=1)
            p.write_text(t)
    # cabeceras: upsert en cada diccionario (sustituye la línea del slug si existe, si no la añade al final)
    cab = op["cabecera"]
    ch = {k: v for k, v in op["chips_extra"]}
    p = GEN / "data_cabeceras.py"; t = p.read_text()
    vals = {"RUTAS": f'({s(cab["rutas"][0])}, {s(cab["rutas"][1])})',
            "ACTIVIDADES": f'({s(ch.get("4x4", ""))}, {s(ch.get("A PIE", ""))})',
            "SEGUROS": s(cab["seguro"]), "PELIGROS": s(cab["peligro"])}
    for dname, val in vals.items():
        m = re.search(r"^" + dname + r" = \{\n(.*?)^\}", t, re.M | re.S)
        body = m.group(1)
        line = f'    "{slug}": {val},\n'
        if re.search(r'^    "' + re.escape(slug) + r'": ', body, re.M):
            body2 = re.sub(r'^    "' + re.escape(slug) + r'": .*\n', line, body, count=1, flags=re.M)
        else:
            body2 = body + line
        t = t[:m.start(1)] + body2 + t[m.end(1):]
    p.write_text(t)
    # visados
    v = op["visado_registro"]
    p = GEN / "data_visados.py"; t = p.read_text()
    if f'    "{slug}": visa(' not in t:
        ent = (f'    "{slug}": visa(\n        {s(v["nivel"])}, {s(v["resumen"])},\n        {s(v["accion"])},\n'
               f'        ruta={s(group)}, entradas={s(v.get("entradas", ""))}, coste={s(v.get("coste", ""))},\n'
               f'        alerta={s(v.get("alerta", ""))},\n        oficial={s(v.get("oficial", ""))}, maec=_maec({s(params["MAEC_TRC"].replace("%C3%AD", "í").replace("%C3%A1", "á").replace("%C3%B3", "ó").replace("%C3%BA", "ú").replace("%C3%A9", "é").replace("%20", " "))})),\n')
        t = t.replace('    "burkina-faso": visa(', ent + '    "burkina-faso": visa(', 1)
        p.write_text(t)
    else:
        # sustituir la entrada existente (países con ficha corta previa)
        pat = re.compile(rf'    "{slug}": visa\(.*?\),\n(?=    "|\}})', re.S)
        ent = (f'    "{slug}": visa(\n        {s(v["nivel"])}, {s(v["resumen"])},\n        {s(v["accion"])},\n'
               f'        ruta={s(group)}, entradas={s(v.get("entradas", ""))}, coste={s(v.get("coste", ""))},\n'
               f'        alerta={s(v.get("alerta", ""))},\n        oficial={s(v.get("oficial", ""))}, maec=_maec({s(params["MAEC_TRC"].replace("%C3%AD", "í").replace("%C3%A1", "á").replace("%C3%B3", "ó").replace("%C3%BA", "ú").replace("%C3%A9", "é").replace("%20", " "))})),\n')
        t2 = pat.sub(lambda m: ent, t, count=1)
        p.write_text(t2)
    # CPD
    c = op["cpd_registro"]
    p = GEN / "data_cpd.py"; t = p.read_text()
    ent = (f'    "{slug}": ({s(c["nivel"])}, {s(c["confianza"])}, {s(c["alternativa"])}, {s(c["coste"])},\n'
           f'              {s(c["nota"])}),\n')
    if f'    "{slug}": (' not in t:
        t = t.replace('    "libia": (', ent + '    "libia": (', 1)
    else:
        pat = re.compile(rf'    "{slug}": \(.*?\),\n(?=    "|    #|\}})', re.S)
        t = pat.sub(lambda m: ent, t, count=1)
    if group in ("fuera", "excluido", "vuelo") and f'"{slug}"' not in t.split("FUERA_DE_RUTA = ")[1].split("\n")[0]:
        t = t.replace('FUERA_DE_RUTA = {"egipto", "libia", "tunez"', f'FUERA_DE_RUTA = {{"egipto", "libia", "tunez", "{slug}"')
    p.write_text(t)
    # perro: contactos
    pc = op["perro_contacto"]
    p = GEN / "data_perro_contactos.py"; t = p.read_text()
    if f" '{slug}':" not in t and f' "{slug}":' not in t:
        ent = (f" {s(slug)}: {{'organismo': {s(pc.get('organismo') or 'Organismo veterinario nacional sin localizar')},\n"
               f"           'url': {s(pc.get('url'))},\n           'url_generica': {bool(pc.get('url_generica'))},\n"
               f"           'url_verificada': {bool(pc.get('url_verificada'))},\n           'email': {s(pc.get('email'))},\n"
               f"           'tel': {s(pc.get('tel'))},\n           'cert': {s(pc.get('cert'))},\n           'cert_dias': {s(pc.get('cert_dias'))},\n"
               f"           'cert_quien': {s(pc.get('cert_quien'))},\n           'nota': {s(pc.get('nota'))},\n"
               f"           'fuentes': {s(pc.get('fuentes') or [])},\n           'auditado': '2026-09-18'}},\n 'ue':")
        t = t.replace("\n 'ue':", "\n" + ent, 1)
        t = t.replace("'cert': true", "'cert': True").replace("'cert': false", "'cert': False").replace("'cert': null", "'cert': None")
        t = t.replace("'cert_dias': null", "'cert_dias': None").replace("'url': null", "'url': None").replace("'email': null", "'email': None").replace("'tel': null", "'tel': None")
        t = t.replace("'cert_quien': null", "'cert_quien': None").replace("'nota': null", "'nota': ''")
        p.write_text(t)
    # perro: FILA en actualiza_dosier y fila/ficha en el dosier
    p = GEN / "actualiza_dosier.py"; t = p.read_text()
    if f'"{name}": "{slug}"' not in t:
        t = t.replace('\n}\n\n# Búsqueda tolerante', f'\n    {s(name)}: {s(slug)},\n}}\n\n# Búsqueda tolerante', 1)
        p.write_text(t)
    dos = GEN / "docs/DOSSIER_PERRO.md"; md = dos.read_text()
    if f"| **{name}** |" not in md:
        row = op.get("perro_dosier_fila") or f"| **{name}** | {short(pick_fact([tuple(r) for r in op['facts']], 'Cómo llegar'), 70)} | {short(pc.get('nota') or '', 40)} | 🟡 | {short(pick_fact([tuple(r) for r in op['facts']], 'Perro'), 200)} | — | — | — |"
        md = md.replace("| **Túnez** |", row + "\n| **Túnez** |", 1) if False else md
        # insertar tras la última fila de la tabla 2.4 (antes de la línea en blanco que la cierra)
        i = md.index("## 2.4 Fuera de la ruta prevista")
        j = md.index("\n\n---", i)
        md = md[:j] + "\n" + row + md[j:]
        # ficha corta en §3
        secs = re.findall(r"^## 3\.(\d+) ", md, re.M)
        nxt = max(int(x) for x in secs) + 1
        ficha = (f"## 3.{nxt} {name.upper()} 🟡 — *{GRUPOS.get(group, group).lower()}*\n\n"
                 f"**Entrada:** {pick_fact([tuple(r) for r in op['facts']], 'Cómo llegar')}\n"
                 f"**Papeles:** {pick_fact([tuple(r) for r in op['facts']], 'Perro')}\n\n"
                 + "".join(f"- {x}\n" for x in op["perro_intro"][:5]) + "\n---\n\n")
        md = md.replace("\n# 4. La vuelta a la UE\n", "\n" + ficha + "# 4. La vuelta a la UE\n", 1)
        dos.write_text(md)
    print("registrado", slug)


if __name__ == "__main__":
    main(sys.argv[1])

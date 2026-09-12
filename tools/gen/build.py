# -*- coding: utf-8 -*-
"""Static site generator for África 2027 (PWA, offline-first)."""
import json
import re
import datetime
from pathlib import Path

from site_common import (SITE, MYMAPS, esc, attr, gmaps, page, table, callout,
                         bullets, st_pill, SITE_CSS, MODAL_JS, MODAL_HTML, FICHA_FIELDS)
from admin_panel import render_admin, ADMIN_CSS
import data_senegal
import data_mauritania
from data_countries import C, GROUP_LABELS

VERSION = datetime.datetime.now().strftime("%Y%m%d-%H%M")
TODAY = "8 de septiembre de 2026"
SITE_URL = "https://theawakeman.github.io/africa2027/"

FULL = {"senegal": data_senegal.get_data(), "mauritania": data_mauritania.get_data()}
# dynamically add researched country modules (data_<slug>.py exporting get_data())
import importlib
for _slug in ["marruecos", "sahara-occidental", "guinea", "sierra-leona", "liberia", "costa-de-marfil",
              "ghana", "togo", "benin", "nigeria", "camerun", "gabon", "congo", "rd-congo", "angola",
              "namibia", "sudafrica", "mozambique", "malaui", "tanzania", "kenia", "etiopia", "sudan", "egipto",
              "gambia", "lesoto", "esuatini", "zimbabue", "botsuana", "zambia", "uganda", "ruanda", "yibuti",
              "madagascar"]:
    try:
        _m = importlib.import_module("data_" + _slug.replace("-", "_"))
        FULL[_slug] = _m.get_data()
    except ModuleNotFoundError:
        pass

# ---- PDIs editables desde el panel (/admin/): si existe content/pois/<slug>.json,
# esa lista sustituye a los POIs calculados por el módulo Python del país.
# El panel de edición solo toca estos JSON; el resto de la ficha (historia, chips,
# secciones, logística, fuentes...) se sigue definiendo en data_<pais>.py.
POIS_DIR = SITE / "content" / "pois"
for _slug, _d in FULL.items():
    _pf = POIS_DIR / f"{_slug}.json"
    if _pf.exists():
        _d["pois"] = json.loads(_pf.read_text(encoding="utf-8"))

# ---- Resto de la ficha editable desde el panel (/admin/): si existe
# content/ficha/<slug>.json, cada clave presente ahí sustituye a la calculada
# por data_<pais>.py (hero, chips, historia, logística, fuentes, secciones...).
FICHA_DIR = SITE / "content" / "ficha"
for _slug, _d in FULL.items():
    _ff = FICHA_DIR / f"{_slug}.json"
    if _ff.exists():
        _overrides = json.loads(_ff.read_text(encoding="utf-8"))
        for _k in FICHA_FIELDS:
            if _k in _overrides:
                _d[_k] = _overrides[_k]

# ---------------------------------------------------------------- map assets
MAP_JS = r"""
function a27Color(t){
  const m = {verde:'#2E7D32', turquesa:'#1E7A8A', marron:'#8B5A2B', naranja:'#D97B29',
             morado:'#673AB7', azul:'#2B6CB0', gris:'#666666', ambar:'#C47F17'};
  return m[t] || '#C47F17';
}
function a27CatStyle(p){
  if (p.type === 'hospital')  return {color:'#B43A3A', label:'Hospitales'};
  if (p.type === 'consular')  return {color:'#673AB7', label:'Consulados'};
  if (p.type === 'frontera')  return {color:'#5F6B72', label:'Fronteras'};
  if (p.type === 'agua')      return {color:'#1E88C7', label:'Agua potable'};
  if (p.type === 'combustible') return {color:'#B8560D', label:'Combustible'};
  if (p.type === 'servicio')  return {color:'#2B6CB0', label:'Servicios'};
  return {color:a27Color(p.color), label:'Puntos de interés'};
}
function a27Popup(p, root){
  let h = '';
  if (p.img) h += '<img src="'+(p.img.indexOf('http')===0?p.img:root+p.img)+'" alt="" style="width:100%;aspect-ratio:16/9;object-fit:cover">';
  h += '<strong style="font-size:14px">'+p.name+'</strong><br>';
  if (p.cat) h += '<span style="color:#1E7A8A;font-weight:700">'+(p.prio? p.prio+' · ':'')+p.cat+'</span><br>';
  if (p.desc) h += '<span>'+p.desc+'</span><br>';
  if (p.dog) h += '<span class="st '+p.dogcls+'">perro: '+p.dog+'</span><br>';
  if (p.info) h += '<span>'+p.info+'</span><br>';
  h += '<div style="margin-top:6px;display:flex;gap:10px;flex-wrap:wrap">';
  if (p.ficha) h += '<a href="'+(p.ficha.indexOf('#')===0?p.ficha:root+p.ficha)+'">Ver en la ficha</a>';
  h += '<a href="https://www.google.com/maps?q='+p.lat+','+p.lon+'" target="_blank" rel="noopener">Google Maps</a></div>';
  return h;
}
function a27Map(elId, cfg){
  const el = document.getElementById(elId);
  if (!el || typeof L === 'undefined') return null;
  const map = L.map(elId, {scrollWheelZoom: cfg.wheel !== false}).setView(cfg.center, cfg.zoom);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 17,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);
  const groups = {};
  function group(label){
    if (!groups[label]) groups[label] = L.layerGroup().addTo(map);
    return groups[label];
  }
  (cfg.lines || []).forEach(li => {
    L.polyline(li.pts, {color: li.color, weight: 4, dashArray: li.dash ? '8 8' : null, opacity:.85})
      .addTo(group(li.label || 'Corredor'));
  });
  (cfg.points || []).forEach(p => {
    const s = a27CatStyle(p);
    const mk = L.circleMarker([p.lat, p.lon], {radius: 8, color:'#fff', weight:2, fillColor:s.color, fillOpacity:.95});
    mk.bindPopup(a27Popup(p, cfg.root), {maxWidth: 290});
    mk.addTo(group(s.label));
  });
  if (Object.keys(groups).length > 1) L.control.layers(null, groups, {collapsed: window.innerWidth < 700}).addTo(map);
  const all = (cfg.points || []).map(p => [p.lat, p.lon]);
  (cfg.lines || []).forEach(li => li.pts.forEach(pt => all.push(pt)));
  if (cfg.fit !== false && all.length) map.fitBounds(L.latLngBounds(all), {padding: [34, 34]});
  return map;
}
"""

def isrc(root, p):
    return p if str(p).startswith("http") else root + p

def dog_cls(dog):
    s = (dog or "").lower()
    if "prohibido" in s and "pendiente" not in s: return "st-red"
    if "pendiente" in s or not s: return "st-grey"
    if "autorización" in s: return "st-amber"
    return "st-green"

def color_key(c):
    return {"turquesa":"turquesa","verde":"verde","marrón":"marron","naranja":"naranja",
            "morado":"morado","azul":"azul","gris":"gris"}.get(c, "ambar")

def cat_type(cat):
    c = cat.lower()
    if "hospital" in c: return "hospital"
    if "consular" in c: return "consular"
    if "frontera" in c: return "frontera"
    if "agua" in c or "potable" in c: return "agua"
    if "combustible" in c or "gasolinera" in c or "carburante" in c or "gasóleo" in c or "diésel" in c or "diesel" in c or "fuel" in c: return "combustible"
    return "servicio"

def map_points(d, with_ficha=True):
    pts = []
    for p in d["pois"]:
        pts.append({"type":"poi","name":p["name"],"lat":round(p["lat"],5),"lon":round(p["lon"],5),
                    "cat":p["cat"],"prio":p["prio"],"desc":p["desc"][:220],"img":p["img"],
                    "dog":p["dog"],"dogcls":dog_cls(p["dog"]),"color":color_key(p["color"]),
                    "ficha": f"paises/{d['slug']}/#poi-{p['n']}" if with_ficha else None})
    for lg in d["logistics"]:
        pts.append({"type":cat_type(lg["cat"]),"name":lg["name"],"lat":round(lg["lat"],5),"lon":round(lg["lon"],5),
                    "cat":lg["cat"],"info":lg["info"],
                    "ficha": f"paises/{d['slug']}/#logistica" if with_ficha else None})
    return pts

def map_lines(d):
    lines = []
    if d.get("corridor"):
        lines.append({"label":d.get("corridor_label","Corredor"),"color":"#1E7A8A","pts":[[round(a,5),round(b,5)] for a,b in d["corridor"]]})
    if d.get("corridor_alt"):
        lines.append({"label":d.get("corridor_alt_label","Corredor (alternativo)"),"color":"#C47F17","dash":True,"pts":[[round(a,5),round(b,5)] for a,b in d["corridor_alt"]]})
    return lines

# ---------------------------------------------------------------- nav helper
def navbar(root, items, brand_suffix=""):
    links = "".join(f'<a href="{u}">{esc(t)}</a>' for t, u in items)
    suf = f'<span class="brand" style="padding-left:0">· {esc(brand_suffix)}</span>' if brand_suffix else ""
    return f'<nav class="nav"><a class="brand" href="{root}">ÁFRICA 2027</a>{suf}{links}</nav>'

TOP_NAV = [("Mapa", "{root}mapa/"), ("Países", "{root}#paises"), ("El perro", "{root}perro/"), ("Documentación", "{root}documentacion/")]

def top_nav(root, extra=""):
    items = [(t, u.format(root=root)) for t, u in TOP_NAV]
    return navbar(root, items, extra)

# ---------------------------------------------------------------- full ficha
def render_ficha(d):
    root = "../../"
    slug = d["slug"]
    sec_nav = [("Resumen", "#resumen")]
    if d.get("historia_resumen"):
        sec_nav.append(("Historia", "#historia"))
    sec_nav += [("Ruta", "#ruta"), ("Agua/Comb.", "#agua-combustible"),
               ("Mapa", "#mapa"), ("PDIs", "#pois"),
               ("Fotos", "#fotos"), ("Emergencias", "#logistica"), ("Fronteras", "#fronteras"),
               ("Perro", "#perro"), ("Fuentes", "#fuentes")]
    nav = navbar(root, [("Mapa general", root + "mapa/"), ("Documentación", root + "documentacion/")] +
                 sec_nav, d["name"])

    chips = "".join(f'<div class="chip"><span class="chip-label">{esc(l)}</span><b>{v if str(v).startswith("<") else esc(v)}</b></div>'
                    for l, v in d["chips"])

    verif_badge = ('<span class="badge b-ok verif-badge">✓ Ficha verificada</span>' if d.get("verificado")
                   else '<span class="badge b-draft verif-badge">Ficha borrador — pendiente de verificar</span>')
    hero = f"""
<header class="hero">
  <img class="bg" src="{isrc(root, d['hero_img'])}" alt="{attr(d['name'])}">
  <div class="veil"></div>
  <div class="photo-credit">{esc(d['hero_credit'])}</div>
  <div class="inner">
    <div class="kicker">FICHA DE PAÍS · REVISIÓN {esc(d['revision']).upper()}</div>
    {verif_badge}
    <h1>{esc(d['name'])}</h1>
    <p class="sub">{esc(d['sub'])}</p>
  </div>
</header>
<div class="chips">{chips}</div>"""

    body = [hero, f'<main><p class="notice">{esc(d["notice"])} <a href="{MYMAPS}" target="_blank" rel="noopener">Abrir el My Maps África 2027</a></p>']

    n_sec = 0
    def sec(sid, title, inner):
        nonlocal n_sec
        n_sec += 1
        return f'<section id="{sid}"><h2>{n_sec} · {esc(title)}</h2>{inner}</section>'

    for sid, title, inner in d["custom_sections"]:
        body.append(sec(sid, title, inner))

    # --- interactive map section ---
    cfg = {"center": d["center"], "zoom": d["zoom"], "root": root,
           "points": map_points(d, with_ficha=False), "lines": map_lines(d)}
    for p in cfg["points"]:
        if p["type"] == "poi":
            n = next(x["n"] for x in d["pois"] if x["name"] == p["name"])
            p["ficha"] = f"#poi-{n}"
    map_html = (
        f'<div id="fichamap" class="mapbox"></div>'
        f'<p class="figcap">Línea turquesa: corredor base · línea ámbar discontinua: variante. Mapa de planificación (OpenStreetMap); navegar con OsmAnd/Google Maps y GPX validado. Sin conexión se muestran los puntos sobre las zonas ya visitadas.</p>'
        f'<script>var A27_FICHA = {json.dumps(cfg, ensure_ascii=False)};</script>'
    )
    body.append(sec("mapa", "Mapa del corredor", map_html))

    # --- POI table ---
    poi_rows, row_attrs = [], []
    for p in d["pois"]:
        poi_rows.append((p["name"], p["prio"], p["time"],
                         f'<span class="st {dog_cls(p["dog"])}">{esc(p["dog"])}</span>',
                         gmaps(p["lat"], p["lon"])))
        row_attrs.append(f'data-poi="poi-{p["n"]}"')
    pois_html = (
        "<p>Toca cualquier fila para abrir la ficha del punto; toca las coordenadas para abrirlo en Google Maps.</p>"
        + table(("Nombre exacto", "Prioridad", "Tiempo", "Perro", "Coordenadas"), poi_rows, cls="num", row_attrs=row_attrs)
    )
    body.append(sec("pois", "Puntos de interés", pois_html))

    # --- photo cards ---
    cards = ""
    for p in d["pois"]:
        src = p["source"]
        src_html = f'<a href="{attr(src)}" target="_blank" rel="noopener">fuente</a>' if src.startswith("http") else esc(src or "—")
        extra = f"<p class='poi-desc dognote'><strong>Perro:</strong> {esc(p['dog_note'])}</p>" if p.get("dog_note") else ""
        # PDIs sin foto verificada: se omite la imagen en vez de dejar un hueco roto.
        if p.get("img"):
            img_html = f'<img src="{isrc(root, p["img"])}" alt="{attr(p["name"])}" loading="lazy">'
            credit_html = f'Foto: {esc(p["credit"])} · {src_html} · {gmaps(p["lat"], p["lon"], "abrir ubicación")}'
        else:
            img_html = '<div class="poi-noimg">Sin fotografía verificada todavía</div>'
            credit_html = gmaps(p["lat"], p["lon"], "abrir ubicación")
        cards += f"""
<article class="poi-card" id="poi-{p['n']}">
  {img_html}
  <div class="poi-body">
    <h3>{esc(p['name'])}</h3>
    <div class="poi-tags"><span class="prio">{esc(p['prio'])}</span><span class="cat">{esc(p['cat'])}</span><span class="time">{esc(p['time'])}</span></div>
    <div><span class="st {dog_cls(p['dog'])}">perro: {esc(p['dog'])}</span></div>
    <p class="poi-desc">{esc(p['desc'])}</p>
    {extra}
    <div class="credit">{credit_html}</div>
  </div>
</article>"""
    body.append(sec("fotos", "Fotografías de los puntos de interés",
                    "<p>Los créditos y licencias se conservan junto a cada fotografía; revisar la fuente antes de reutilizarlas fuera de esta ficha.</p>"
                    f'<div class="poi-grid">{cards}</div>'))

    # --- logistics ---
    log_rows = [(lg["name"], lg["cat"], gmaps(lg["lat"], lg["lon"]), lg["info"]) for lg in d["logistics"]]
    log_html = (
        callout("danger", "Emergencia", d["emergency"])
        + table(("Nombre exacto en My Maps", "Categoría", "Coordenadas", "Dato operativo"), log_rows, cls="num")
    )
    body.append(sec("logistica", "Emergencias y logística", log_html))

    for sid, title, inner in d["custom_sections_post"]:
        body.append(sec(sid, title, inner))

    src_list = "".join(f'<li><a href="{attr(u)}" target="_blank" rel="noopener">{esc(t)}</a></li>' for t, u in d["sources"])
    body.append(sec("fuentes", "Fuentes oficiales y trazabilidad",
                    f'<p>{esc(d["sources_note"])}</p><ul class="srcs">{src_list}</ul>'))

    matrix_rows = [(p["name"], p["cat"], f'{p["icon"]} · {p["color"]}', gmaps(p["lat"], p["lon"])) for p in d["pois"]]
    matrix_rows += [(lg["name"], lg["cat"], "capa Emergencias y logística", gmaps(lg["lat"], lg["lon"])) for lg in d["logistics"]]
    body.append(sec("matriz", "Matriz maestra My Maps",
                    callout("", "Control de consistencia", d["matrix_note"])
                    + table(("Nombre exacto", "Categoría", "Icono / color", "Coordenadas"), matrix_rows, cls="num")))

    body.append(f'<footer>ÁFRICA 2027 · Ficha de país {esc(d["name"])} · Revisión {esc(d["revision"])} · versión {VERSION} · <a href="{root}">Portal</a> · <a href="{root}mapa/">Mapa general</a></footer></main>')
    body.append(MODAL_HTML)
    body.append(MODAL_JS)
    body.append(f'<script src="{root}assets/vendor/leaflet.js"></script>')
    body.append('<script>if (typeof L !== "undefined" && window.A27_FICHA) a27MapInit();'
                'function a27MapInit(){ a27Map("fichamap", A27_FICHA); }</script>')

    extra_head = (f'<link rel="stylesheet" href="{root}assets/vendor/leaflet.css">'
                  f'<script src="{root}assets/js/map.js" defer></script>')
    # map.js is deferred; leaflet loads at end; init after both -> use a small loader instead
    body[-1] = ('<script>window.addEventListener("load", function(){'
                'if (typeof L !== "undefined" && typeof a27Map === "function" && window.A27_FICHA)'
                ' a27Map("fichamap", A27_FICHA); });</script>')
    return page(root, f"{d['name']} · África 2027", nav + "".join(body), extra_head=extra_head)

# ---------------------------------------------------------------- stub ficha
def render_stub(slug, name, group, seguridad, frontera, visado, cpd, perro, nota):
    root = "../../"
    nav = navbar(root, [("Mapa general", root + "mapa/"), ("Documentación", root + "documentacion/"), ("Todos los países", root + "#paises")], name)
    glabel = GROUP_LABELS[group]
    if group == "excluido":
        badge = '<span class="badge b-x">Excluido por protocolo</span>'
    elif group == "fuera":
        badge = '<span class="badge b-off">Fuera de la ruta prevista</span>'
    else:
        badge = '<span class="badge b-draft">Borrador · pendiente de revisión</span>'
    chips = "".join(f'<div class="chip"><span class="chip-label">{l}</span><b>{v}</b></div>' for l, v in [
        ("PAPEL EN LA RUTA", esc(glabel)),
        ("SEGURIDAD", st_pill(seguridad if seguridad != "—" else "sin datos")),
        ("CPD", st_pill(cpd if cpd and cpd != "—" else "sin datos")),
    ])
    rows = [("Seguridad y conflicto", seguridad), ("Frontera terrestre", frontera),
            ("Visado (españoles)", visado), ("Vehículos / CPD", cpd),
            ("Perro", perro), ("Nota de ruta", nota)]
    rows = [(a, b) for a, b in rows if b and b != "—"]
    inner = (
        callout("warn", "Ficha borrador", f"Datos orientativos preparados el {TODAY} a partir de conocimiento general del corredor. TODO pendiente de verificación con fuentes oficiales antes de planificar; se revisará país por país.")
        + table(("Tema", "Estado orientativo"), rows)
        + callout("", "Trámites comunes", 'CPD, autorizaciones de los vehículos, seguro, perro y salud: ver <a href="../../documentacion/">Documentación general</a>.', raw=True)
    )
    body = f"""{nav}
<header class="hero"><div style="padding:44px clamp(16px,4vw,48px) 20px">
  <div class="kicker">FICHA DE PAÍS · BORRADOR</div>
  <h1>{esc(name)}</h1>
  <p class="sub">{esc(glabel)}</p>
</div></header>
<div class="chips">{chips}</div>
<main>
<p style="margin-top:14px">{badge}</p>
<section id="estado" style="margin-top:10px"><h2>Estado de planificación</h2>{inner}</section>
<footer>ÁFRICA 2027 · {esc(name)} · borrador · versión {VERSION} · <a href="{root}">Portal</a></footer>
</main>"""
    return page(root, f"{name} · África 2027", body)

# ---------------------------------------------------------------- historia (con audio)
AUDIO_JS = """
<script>
(function(){
  const bar = document.getElementById('audio-bar');
  if (!bar) return;
  if (!('speechSynthesis' in window)) { bar.hidden = true; return; }
  const article = document.getElementById('historia-article');
  const playBtn = document.getElementById('a27-play');
  const pauseBtn = document.getElementById('a27-pause');
  const stopBtn = document.getElementById('a27-stop');
  const status = document.getElementById('a27-status');
  function pickVoice(){
    const voices = speechSynthesis.getVoices();
    return voices.find(v => v.lang && v.lang.toLowerCase().startsWith('es')) || voices[0];
  }
  function start(){
    speechSynthesis.cancel();
    const utter = new SpeechSynthesisUtterance(article.innerText);
    utter.lang = 'es-ES';
    const v = pickVoice(); if (v) utter.voice = v;
    utter.rate = 0.98;
    utter.onstart = () => { status.textContent = 'Narrando…'; playBtn.hidden = true; pauseBtn.hidden = false; stopBtn.hidden = false; pauseBtn.textContent = '⏸ Pausar'; };
    utter.onend = () => { status.textContent = ''; playBtn.hidden = false; pauseBtn.hidden = true; stopBtn.hidden = true; };
    utter.onerror = () => { status.textContent = 'No se pudo reproducir el audio en este dispositivo.'; playBtn.hidden = false; pauseBtn.hidden = true; stopBtn.hidden = true; };
    speechSynthesis.speak(utter);
  }
  playBtn.addEventListener('click', start);
  pauseBtn.addEventListener('click', () => {
    if (speechSynthesis.speaking && !speechSynthesis.paused) { speechSynthesis.pause(); pauseBtn.textContent = '▶ Reanudar'; }
    else if (speechSynthesis.paused) { speechSynthesis.resume(); pauseBtn.textContent = '⏸ Pausar'; }
  });
  stopBtn.addEventListener('click', () => { speechSynthesis.cancel(); status.textContent = ''; playBtn.hidden = false; pauseBtn.hidden = true; stopBtn.hidden = true; });
  window.addEventListener('beforeunload', () => speechSynthesis.cancel());
})();
</script>"""

def render_historia(d):
    root = "../../../"
    slug = d["slug"]
    nav = navbar(root, [("Mapa general", root + "mapa/"), ("Documentación", root + "documentacion/"),
                        ("← Ficha de " + d["name"], root + f"paises/{slug}/")], "Historia")

    secciones_html = ""
    for heading, body_html in d.get("historia_secciones", []):
        inner = body_html if str(body_html).strip().startswith("<") else f"<p>{esc(body_html)}</p>"
        secciones_html += f"<h3>{esc(heading)}</h3>{inner}"

    fuentes = d.get("historia_fuentes", [])
    src_list = "".join(f'<li><a href="{attr(u)}" target="_blank" rel="noopener">{esc(t)}</a></li>' for t, u in fuentes)
    fuentes_html = (f'<section id="fuentes-historia"><h2>Fuentes y para profundizar</h2><ul class="srcs">{src_list}</ul></section>'
                    if fuentes else "")

    audio_bar = ('<div class="audio-bar" id="audio-bar">'
                 '<button id="a27-play" class="btn">🔊 Escuchar la historia</button>'
                 '<button id="a27-pause" class="btn ghost" hidden>⏸ Pausar</button>'
                 '<button id="a27-stop" class="btn ghost" hidden>⏹ Detener</button>'
                 '<span class="audio-status" id="a27-status"></span>'
                 '</div>'
                 '<p class="figcap">El audio se genera en el propio dispositivo (voz del sistema); no requiere conexión una vez cargada la página ni descarga de ningún archivo.</p>')

    hero = f"""
<header class="hero histhero">
  <img class="bg" src="{isrc(root, d['hero_img'])}" alt="{attr(d['name'])}">
  <div class="veil"></div>
  <div class="photo-credit">{esc(d['hero_credit'])}</div>
  <div class="inner">
    <div class="kicker">HISTORIA Y CONTEXTO · {esc(d['name']).upper()}</div>
    <h1>Historia de {esc(d['name'])}</h1>
    <p class="sub">Orígenes, colonización, independencia y situación actual — para leer o escuchar durante el viaje.</p>
  </div>
</header>"""

    body = (hero + "<main>" + audio_bar +
            f'<article id="historia-article" class="historia-article"><p>{esc(d.get("historia_resumen",""))}</p>{secciones_html}</article>' +
            fuentes_html +
            f'<footer>ÁFRICA 2027 · Historia de {esc(d["name"])} · versión {VERSION} · '
            f'<a href="{root}paises/{slug}/">Volver a la ficha</a> · <a href="{root}">Portal</a></footer></main>')

    return page(root, f"Historia de {d['name']} · África 2027", nav + body + AUDIO_JS)

# ---------------------------------------------------------------- portal
def render_portal(countries):
    root = ""
    nav = top_nav(root)
    ruta_total = sum(1 for c in countries if c["group"] in ("bajada", "bucle", "subida"))
    ruta_completas = sum(1 for c in countries if c["group"] in ("bajada", "bucle", "subida") and c["estado"] == "completa")
    groups = {}
    for c in countries:
        groups.setdefault(c["group"], []).append(c)
    cards_html = ""
    order = ["bajada", "bucle", "subida", "alternativa", "vuelo", "excluido", "fuera"]
    for g in order:
        if g not in groups:
            continue
        cards = ""
        for c in sorted(groups[g], key=lambda x: x["order"]):
            if c["estado"] == "completa":
                badge = '<span class="badge b-ok">Ficha disponible</span>'
                badge += (' <span class="badge b-ok">✓ Verificada</span>' if c.get("verificado")
                          else ' <span class="badge b-draft">Contenido borrador</span>')
            elif c["group"] == "excluido":
                badge = '<span class="badge b-x">Excluido</span>'
            elif c["group"] == "fuera":
                badge = '<span class="badge b-off">Fuera de ruta</span>'
            else:
                badge = '<span class="badge b-draft">Borrador</span>'
            img = f'<img src="{c["img"]}" alt="" loading="lazy">' if c.get("img") else ""
            meta = esc(c.get("meta", ""))
            cards += f"""<a class="card" href="paises/{c['slug']}/">{img}<div class="body"><h3>{esc(c['name'])}</h3>{badge}<span class="meta">{meta}</span></div></a>"""
        cards_html += f'<h3 style="margin-top:26px">{esc(GROUP_LABELS[g])}</h3><div class="cards">{cards}</div>'

    body = f"""{nav}
<header class="hero">
  <img class="bg" src="assets/img/senegal/01.jpg" alt="Delta del Saloum">
  <div class="veil"></div>
  <div class="inner">
    <div class="kicker">EXPEDICIÓN OVERLAND · ENERO–AGOSTO 2027</div>
    <h1>África 2027</h1>
    <p class="sub">Barcelona → Sudáfrica → Barcelona · 2 vehículos 4x4 · 3 viajeros · 1 perro</p>
  </div>
</header>
<div class="chips">
  <div class="chip"><span class="chip-label">SALIDA</span><b>10 ene 2027</b></div>
  <div class="chip"><span class="chip-label">REGRESO</span><b>~15 ago 2027</b></div>
  <div class="chip"><span class="chip-label">FICHAS COMPLETAS</span><b>{ruta_completas} de {ruta_total} en ruta</b></div>
  <div class="chip"><span class="chip-label">VERSIÓN</span><b>{VERSION}</b></div>
</div>
<main>
<section id="accesos" style="margin-top:26px">
<div class="cards">
  <a class="card" href="mapa/"><div class="body"><h3>🗺️ Mapa general</h3><span class="meta">Todos los puntos por capas: PDIs, hospitales, consulados, fronteras, agua potable y combustible. Toca un punto para ver su ficha.</span></div></a>
  <a class="card" href="documentacion/"><div class="body"><h3>📋 Documentación general</h3><span class="meta">CPD, autorización del Grenadier, Delica, seguros, perro, salud, drones, Starlink y protocolo de seguridad.</span></div></a>
  <a class="card" href="{MYMAPS}" target="_blank" rel="noopener"><div class="body"><h3>📍 My Maps (Google)</h3><span class="meta">Mapa maestro compartido del proyecto (requiere conexión).</span></div></a>
</div>
</section>
<section id="paises"><h2>Fichas de país</h2>{cards_html}</section>
<section id="offline"><h2>Uso sin conexión</h2>
<p class="callout" style="display:block"><strong>Instalar en el móvil:</strong> abre esta página en el navegador y usa «Añadir a pantalla de inicio». La app guarda todas las fichas y fotos en el teléfono y funciona sin cobertura; el mapa base necesita internet la primera vez que se ve cada zona. Cuando vuelve a haber conexión, la app comprueba sola si hay cambios y avisa con «Nueva versión disponible».</p>
</section>
<footer>ÁFRICA 2027 · versión {VERSION} · <a href="documentacion/">documentación</a> · <a href="mapa/">mapa</a></footer>
</main>"""
    return page(root, "África 2027", body)

# ---------------------------------------------------------------- general map
def render_map_page(all_points, all_lines):
    root = "../"
    nav = navbar(root, [("Portal", root), ("Documentación", root + "documentacion/")], "Mapa general")
    cfg = {"center": [14.0, -5.0], "zoom": 4, "root": root, "points": all_points, "lines": all_lines}
    body = f"""{nav}
<main style="max-width:1400px">
<h2 style="margin-top:18px">Mapa general del viaje</h2>
<p>Capas activables con el control de la esquina superior derecha: puntos de interés, hospitales, consulados, fronteras, agua potable y combustible (además de servicios genéricos). Toca cualquier punto para ver su información y abrir la ficha del país o Google Maps. El fondo es OpenStreetMap: con conexión se puede navegar y hacer zoom por toda África; sin conexión se muestran las zonas ya visitadas.</p>
<p class="callout" style="display:block"><strong>Agua y combustible:</strong> puntos verificados con fuentes propias, iOverlander y Tracks4Africa (comunidad overlander); revisar siempre comentarios recientes de esas plataformas antes de fiarse de un punto, porque una fuente o gasolinera puede cerrar o quedarse seca sin previo aviso. Objetivo de planificación: no dejar tramos de más de ~500 km sin una opción de combustible confirmada; donde no se pueda garantizar, se indica como alerta en la ficha del país.</p>
<div id="genmap" class="mapbox tall"></div>
<p class="figcap">Corredores: turquesa = ruta base trabajada · ámbar discontinuo = variantes. Los países en borrador aún no tienen puntos; se añadirán ficha a ficha.</p>
<footer>ÁFRICA 2027 · versión {VERSION}</footer>
</main>
<script>var A27_GEN = {json.dumps(cfg, ensure_ascii=False)};</script>
<script>window.addEventListener("load", function(){{ if (typeof L !== "undefined" && typeof a27Map === "function") a27Map("genmap", A27_GEN); }});</script>"""
    extra_head = (f'<link rel="stylesheet" href="{root}assets/vendor/leaflet.css">'
                  f'<script src="{root}assets/vendor/leaflet.js"></script>'
                  f'<script src="{root}assets/js/map.js"></script>')
    return page(root, "Mapa general · África 2027", body, extra_head=extra_head)

# ---------------------------------------------------------------- perro page
PERRO_MD = Path(__file__).parent / "docs" / "DOSSIER_PERRO.md"

def render_perro():
    """Sección propia del perro, generada desde docs/DOSSIER_PERRO.md.
    El markdown es la fuente única: se actualiza ese archivo y la página sale sola."""
    from md_mini import md_to_html, md_headings
    from enlaza_paises import enlazar, indice_paises
    root = "../"
    md = PERRO_MD.read_text(encoding="utf-8") if PERRO_MD.exists() else "# Dossier del perro\n\nPendiente."

    # El documento trae su propia portada, leyenda e índice; aquí sobran, porque
    # la página ya pone cabecera, leyenda y menú. Se empieza en el primer capítulo.
    _lines = md.split("\n")
    for _k, _l in enumerate(_lines):
        if _l.startswith("# ") and _k > 0:
            md = "\n".join(_lines[_k:])
            break

    # Índice lateral a partir de los encabezados de primer nivel
    tops = [(t, a) for t, a, lvl in md_headings(md, levels=(1,))]
    secs = [("Portal", root), ("Mapa", root + "mapa/"), ("Documentación", root + "documentacion/")]
    def _short(t):
        t = re.sub(r"^\d+[.)]\s*", "", t.split("·")[0].strip())   # fuera el "1. "
        if len(t) <= 20:
            return t
        cut = t[:20].rsplit(" ", 1)[0]                              # cortar por palabra
        return (cut or t[:20]) + "…"
    nav = navbar(root, secs + [(_short(t), "#" + a) for t, a in tops[:8]], "El perro")

    hero = f"""<header class="hero small">
  <div class="hero-txt">
    <span class="kicker">Sección propia · se actualiza sobre la marcha</span>
    <h1>El perro</h1>
    <p>Todo lo que hace falta para cruzar África por tierra con el perro: entrada país por país,
    papeles, plazos, dónde puede estar y dónde no, salud en ruta y la vuelta a la UE.
    Cada afirmación lleva su nivel de confianza y su fuente.</p>
  </div>
</header>"""

    leyenda = callout("", "Cómo leer esta sección",
        "Cada dato va etiquetado como <strong>[CONFIRMADO]</strong> (fuente oficial del país o varios "
        "testimonios coincidentes), <strong>[PROBABLE]</strong> (una sola fuente buena) o "
        "<strong>[SIN CONFIRMAR]</strong> (las fuentes se contradicen o callan). Lo que no se sabe se dice "
        "que no se sabe, y se indica a quién hay que escribir para cerrarlo.", raw=True)

    cuerpo = enlazar(md_to_html(md, base_level=2), root)
    body = nav + hero + "<main>" + leyenda + indice_paises(root) + cuerpo + "</main>"
    return page(root, "El perro · África 2027", body)

# ---------------------------------------------------------------- docs page
def render_docs():
    root = "../"
    secs = [("Portal", root), ("Mapa", root + "mapa/")]
    anchors = [("CPD", "#cpd"), ("Grenadier", "#grenadier"), ("Delica", "#delica"), ("Seguro", "#seguro"),
               ("Perro", "#perro"), ("Salud", "#salud"), ("Agua/Comb.", "#agua-combustible"),
               ("Drones", "#drones"), ("Starlink", "#starlink"),
               ("Seguridad", "#seguridad"), ("GPX", "#gpx")]
    nav = navbar(root, secs + anchors, "Documentación")

    cpd = (
        "<p>El Carnet de Passages en Douane (CPD) es el «pasaporte del vehículo»: una garantía internacional que permite la admisión temporal sin depositar fianzas en cada aduana. No todos los países lo exigen, pero varios del corredor lo piden en la práctica (Nigeria, Kenia, Tanzania) y en Egipto es obligatorio con condiciones especialmente exigentes. La ficha de cada país indica si hace falta, es recomendable o existe alternativa (passavant/permiso temporal).</p>"
        + bullets([
            "RACE lo expide en exclusiva en España. Contacto publicado: eloy_gonzalo@race.es · +34 91 594 73 00.",
            "Documentación: permiso de circulación, ficha técnica, DNI del titular, solicitud y aval bancario de validez indefinida.",
            "RACE publica un aval mínimo de 2.780 € y cálculo según valor venal GANVAM; emisión aproximada 230 €, formatos de 10 o 25 hojas y validez de un año. Pedir presupuesto escrito para cada vehículo.",
            "Cada entrada y salida debe quedar sellada (par completo). Un sello que falte puede bloquear la devolución del aval — comprobar antes de salir de cada puesto.",
            "No cerrar el expediente hasta que el CPD vuelva con todos los pares de sellos, especialmente del último país.",
        ])
        + callout("warn", "Egipto", "Exige CPD con condiciones propias (aval elevado, trámites y matrícula temporal). Tratarlo como expediente aparte cuando se planifique el tramo final.")
    )
    grenadier = (
        "<p>El Ineos Grenadier está a nombre de una empresa: para sacarlo de España, importarlo temporalmente y cruzar fronteras hace falta un paquete de autorización societaria coherente con el CPD.</p>"
        + bullets([
            "Autorización original en francés, con membrete, sello y firma con facultades: identifica empresa, conductor(es), matrícula, VIN, fechas, países y autorización para conducir, exportar temporalmente, importar, asegurar y representar ante aduanas.",
            "Adjuntar certificado registral de la empresa, documento que acredite poderes del firmante, copia de su identificación y traducción jurada si RACE o una aduana la exige. Valorar firma notarial y apostilla.",
            "Si el conductor es también administrador, evitar una autoautorización ambigua: usar acuerdo/certificado societario emitido por otro órgano o fedatario.",
            "El CPD del Grenadier debe tramitarse con el titular registral; preguntar a RACE qué firmante y garantías acepta.",
        ])
    )
    delica = bullets([
        "Si Albert es propietario y conductor: originales del vehículo, seguro, CPD y pasaporte con datos coincidentes.",
        "Si otra persona puede conducirla o cruzar frontera con ella: autorización notarial del propietario en francés, con matrícula/VIN, países, fechas y facultades aduaneras.",
        "No cruzar ninguna frontera si el nombre del CPD, permiso de circulación, seguro y autorización crean contradicciones.",
    ])
    seguro = bullets([
        "La Carta Verde europea no cubre el África subsahariana: comprar responsabilidad civil local o regional en la primera frontera de cada bloque.",
        "África occidental (CEDEAO): pedir la Carte Brune para continuidad regional; verificar países cubiertos, vehículo, fechas, matrícula y conductor.",
        "África oriental y austral (COMESA): existe la Yellow Card regional equivalente — pedirla en la primera frontera del bloque.",
        "Conservar recibo y certificado por separado; fotografiar todos los documentos.",
        "Seguro de viaje de las personas: hospitalización, rescate y evacuación médica real desde zonas remotas, sin exclusión por 4x4, acampada o países de la ruta.",
    ])
    perro = (
        "<p>Requisitos comunes del perro (pastor australiano, 15 kg) para todo el viaje; cada ficha añade lo específico del país.</p>"
        + bullets([
            "Microchip legible + pasaporte europeo + vacuna antirrábica siempre en vigor (sin interrupciones durante todo el viaje).",
            "Titulación de anticuerpos de rabia en laboratorio autorizado ANTES de salir de la UE, anotada en el pasaporte: es la llave del retorno a la UE desde países terceros no listados, y evita esperas de meses.",
            "Certificado veterinario internacional reciente para cada frontera (varios países lo piden de <72 h o <10 días); llevar plantillas y copias en francés e inglés.",
            "Desparasitación interna/externa al día; prevención de leishmania y dirofilariosis según el veterinario; botiquín canino, bozal y correa de repuesto.",
            "Regla del proyecto: en cada parque o reserva, estado explícito (permitido / con condiciones / autorización escrita / prohibido / pendiente) y solución de cuidado verificada antes de dar la visita por resuelta; separación máxima prevista, 2–3 días.",
            "Calor: nunca dejar al perro solo en un vehículo cerrado; planificar sombra, agua y protección de almohadillas.",
        ])
    )
    salud = bullets([
        "Visita al Centro de Vacunación Internacional con el itinerario continental completo (ambos sentidos).",
        "Fiebre amarilla: certificado internacional obligatorio de facto en la mayor parte del corredor; se pide al llegar desde países con riesgo.",
        "Malaria: profilaxis según tramo (el riesgo cubre casi todo el corredor subsahariano); mosquitera, repelente DEET, ropa larga al atardecer.",
        "Revisar hepatitis A/B, tifoidea, tétanos-difteria-tosferina, polio, meningocócica (Sahel en estación seca) y rabia preexposición.",
        "Agua y alimentos: filtración/desinfección redundante; sales de rehidratación; protocolo de diarrea y fiebre; no bañarse en aguas dulces (esquistosomiasis).",
        "Botiquín de expedición + medicación personal para 8 meses con recetas; copias en francés/inglés.",
    ])
    agua_combustible_general = (
        "<p>Ambos son puntos generales del proyecto: cada ficha de país detalla los puntos concretos verificados, pero el criterio y la estrategia son los mismos para todo el corredor.</p>"
        + "<h3>Agua: no solo de beber</h3>"
        + "<p>Como vehículos de expedición autónomos (Grenadier y Delica) llevamos depósito propio de agua, y hay que distinguir dos necesidades que se resuelven de forma distinta:</p>"
        + bullets([
            "Agua de boca: la que se bebe y se cocina. Se trata siempre como no potable de origen y se pasa por el protocolo de potabilización del vehículo (filtro + purificación redundante — UV/químico) antes de consumirla, venga de donde venga.",
            "Agua de uso general: ducha, aseo personal, vajilla y limpieza. No necesita el mismo nivel de tratamiento, pero sí depósito de capacidad suficiente y puntos de recarga fiables — surtidores de gasolinera, campings, hoteles, misiones, pozos y fuentes municipales — porque en tramos largos de pista puede no haber otra fuente en días.",
            "Capacidad de reserva objetivo: autonomía mínima de 3–4 días de uso general por vehículo entre recargas, ampliable en tramos identificados como secos (Sáhara Occidental, Mauritania interior, Sahel).",
            "Cada ficha de país lista los puntos de recarga conocidos (surtidores, campings, misiones, pozos) en su sección «Agua y combustible», con la fuente y la fecha de verificación.",
            "Registrar siempre en iOverlander/Tracks4Africa si un punto ya no funciona o si aparece uno nuevo, para mantener la ruta del grupo actualizada entre etapas.",
        ])
        + "<h3>Combustible: gasóleo y la regla de los 500 km</h3>"
        + bullets([
            "Ambos vehículos usan diésel: exigir siempre la calidad máxima disponible localmente (menor contenido de azufre dentro del estándar del país) y evitar surtidores informales o de garrafa salvo necesidad, por riesgo de agua o sedimentos en el gasóleo.",
            "Regla del proyecto: no debe haber más de 500 km entre dos puntos de repostaje fiables a lo largo de la ruta prevista. Sin track GPX cerrado, cada ficha calcula la distancia entre las poblaciones con surtidor conocido del tramo y señala con una alerta cualquier hueco mayor de 500 km sin garantía.",
            "Llevar reserva propia (jerricán) dimensionada para cubrir el mayor hueco identificado en la ficha del país que se esté cruzando, no solo la autonomía de fábrica del depósito.",
            "Filtrar el gasóleo al repostar en surtidores dudosos (embudo con filtro/decantador) y llevar aditivo anti-agua/biocida de repuesto.",
            "Antes de cerrar cada tramo, contrastar los surtidores previstos en iOverlander y Tracks4Africa: ambas plataformas recogen comentarios recientes de otros overlanders sobre si un surtidor concreto tenía diésel, de qué calidad y a qué precio.",
        ])
        + callout("", "Fuentes cruzadas del proyecto", 'Fuente de referencia para agua y combustible en todo el corredor: <a href="https://ioverlander.com/" target="_blank" rel="noopener">iOverlander</a> y <a href="https://tracks4africa.co.za/" target="_blank" rel="noopener">Tracks4Africa</a> — también útiles para comentarios recientes sobre fronteras. Revisar siempre la fecha del último comentario antes de confiar en un punto.', raw=True)
    )
    drones = bullets([
        "Regla general del viaje: ningún país africano del corredor permite volar «por defecto» — casi todos exigen registro o autorización previa, y varios prohíben la entrada del dron sin permiso de importación.",
        "Norma prudente: transportar el dron apagado, embalado y declarable; no volar en ningún país sin autorización escrita de su autoridad de aviación civil.",
        "Nunca volar cerca de aeropuertos, instalaciones militares, fronteras, multitudes ni áreas protegidas, tampoco con autorización genérica.",
        "Cada ficha indica la autoridad local (ANAC, ANACIM…), el procedimiento publicado y la decisión práctica.",
    ])
    starlink = bullets([
        "Comprobar en la cuenta que el plan Roam permite uso internacional y que el hardware está activado antes de salir de cobertura europea.",
        "Starlink limita el uso internacional (60 días por viaje según sus condiciones publicadas) y puede restringir el servicio en países no autorizados; revisar el estado país por país (cada ficha lo indica).",
        "Declarar el equipo en aduanas si se solicita; conservar factura, número de serie y prueba de titularidad. No usar en movimiento salvo en países que lo autoricen.",
        "Starlink no sustituye una baliza ni la mensajería satelital: mantener SIM/eSIM local + InReach o similar como canal independiente.",
    ])
    seguridad = (
        bullets([
            "No conducir de noche en ningún país del corredor. Ante un retraso: dormir en población o recinto vigilado y reanudar de día.",
            "Dos vehículos siempre juntos en pista; check-in diario a hora fija con un contacto en España y protocolo de escalado 6/12/24 h sin noticias.",
            "Ante un control: cortesía, documentos preparados en copias, no entregar originales fuera de ventanilla, no pagar sin recibo, no fotografiar puestos ni fuerzas de seguridad.",
            "Consultar MAEC España + France Diplomatie + FCDO antes de cada frontera (72 h) y registrar el viaje en el Registro de Viajeros del MAEC.",
            "Acampada libre solo con validación local; en ciudades, fronteras y áreas protegidas, recinto vigilado con espacio para ambos 4x4.",
            "Efectivo repartido, copias cifradas de documentos, y nada visible en los vehículos.",
        ])
    )
    gpx = bullets([
        "Preparar navegación para OsmAnd y Google Maps; comprobar la importación de cada GPX en OsmAnd (incluidos nombres con tildes).",
        "Separar tramos asfaltados, pistas sencillas y secciones de arena/navegación; definir autonomía mínima y punto de retorno por etapa.",
        "Guardar waypoints de combustible, agua, talleres, controles, campamentos, hospitales y salidas de emergencia.",
        "Dos copias offline por vehículo y una impresa con coordenadas de hospitales, consulados y fronteras.",
        "No convertir líneas de mapa en instrucciones de conducción: validar con fuentes recientes y guía local.",
    ])

    def s(i, sid, title, inner):
        return f'<section id="{sid}"><h2>{i} · {title}</h2>{inner}</section>'

    body = f"""{nav}
<header class="hero"><div style="padding:40px clamp(16px,4vw,48px) 18px">
  <div class="kicker">TRÁMITES Y PROTOCOLOS COMUNES A TODO EL VIAJE</div>
  <h1>Documentación general</h1>
  <p class="sub">Lo que se aplica a todos los países está aquí; cada ficha solo indica lo específico y si hace falta o no.</p>
</div></header>
<main>
{s(1,"cpd","Carnet de Passages en Douane (CPD)", cpd)}
{s(2,"grenadier","Ineos Grenadier de empresa", grenadier)}
{s(3,"delica","Mitsubishi Delica", delica)}
{s(4,"seguro","Seguros (vehículos y personas)", seguro)}
{s(5,"perro","El perro: requisitos comunes", perro)}
{s(6,"salud","Salud humana", salud)}
{s(7,"agua-combustible","Agua y combustible", agua_combustible_general)}
{s(8,"drones","Drones: regla general", drones)}
{s(9,"starlink","Starlink Roam", starlink)}
{s(10,"seguridad","Protocolo de seguridad y conducción", seguridad)}
{s(11,"gpx","GPX y navegación", gpx)}
<footer>ÁFRICA 2027 · Documentación general · versión {VERSION} · <a href="{root}">Portal</a></footer>
</main>"""
    return page(root, "Documentación general · África 2027", body)

# ---------------------------------------------------------------- KML export
def kml_escape(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# Same palette as MAP_JS's a27Color()/a27CatStyle() — kept in sync so the
# KML/My Maps layers match the in-app map exactly, not an approximation.
A27_COLOR_HEX = {"verde": "#2E7D32", "turquesa": "#1E7A8A", "marron": "#8B5A2B",
                 "naranja": "#D97B29", "morado": "#673AB7", "azul": "#2B6CB0",
                 "gris": "#666666", "ambar": "#C47F17"}
A27_CAT_HEX = {"hospital": "#B43A3A", "consular": "#673AB7", "frontera": "#5F6B72",
               "agua": "#1E88C7", "combustible": "#B8560D", "servicio": "#2B6CB0"}

# Google My Maps ignores KML <IconStyle><color> tinting on import (confirmed:
# stock shapes/star.png came back white/unfilled), so colors must be baked
# into the icon image itself. My Maps builds its own badge icons through this
# public compositing endpoint (captured live from the existing map's network
# requests) -- reusing it means the imported KML renders with the exact same
# rounded badge look the map already has, in any color we want.
def _onion_badge(hexcolor, glyph=None):
    color = hexcolor.lstrip("#").upper()
    names = "icons/onion/SHARED-mymaps-container-bg_4x.png,icons/onion/SHARED-mymaps-container_4x.png"
    if glyph:
        return (f"https://mt.google.com/vt/icon/name={names},icons/onion/{glyph}_4x.png"
                f"&highlight=ff000000,{color},ff000000&scale=2.0")
    return f"https://mt.google.com/vt/icon/name={names}&highlight=ff000000,{color}&scale=2.0"

# Glyphs already used by hand on the live My Maps for these categories
# (captured from the map's own network requests): estrella for POIs,
# hospital-h for hospitals, civic for consulados, car for fronteras.
_GLYPHS = {"hospital": "1807-hospital-h", "consular": "1548-civic", "frontera": "1538-car"}
_POI_GLYPH = "1502-shape_star"

def kml_style_for(p):
    """Return (style_id, href) for a map point, reusing the exact colors
    already established in the app and the exact icon glyphs already
    established on the live My Maps."""
    t = p.get("type")
    if t in A27_CAT_HEX:
        return (f"icon-{t}", _onion_badge(A27_CAT_HEX[t], _GLYPHS.get(t)))
    c = p.get("color", "ambar")
    return (f"icon-poi-{c}", _onion_badge(A27_COLOR_HEX.get(c, A27_COLOR_HEX["ambar"]), _POI_GLYPH))

_CAT_LABELS = {"hospital": "Hospital", "consular": "Consulado", "frontera": "Frontera",
               "agua": "Agua potable", "combustible": "Combustible", "servicio": "Servicio"}
_POI_COLOR_LABELS = {"verde": "Verde", "turquesa": "Turquesa", "marron": "Marrón",
                      "naranja": "Naranja", "morado": "Morado", "azul": "Azul",
                      "gris": "Gris", "ambar": "Ámbar"}

def category_label(p):
    """Human label used as a KML ExtendedData column, so that after import
    My Maps' own 'Estilo individual > Agrupar por columna' can assign the
    matching icon once per value — the only styling path My Maps actually
    honors (it discards <IconStyle> from imported KML entirely)."""
    t = p.get("type")
    if t in _CAT_LABELS:
        return _CAT_LABELS[t]
    c = p.get("color", "ambar")
    return f"PDI · {_POI_COLOR_LABELS.get(c, 'Ámbar')}"

def point_desc_html(p, base_url=SITE_URL):
    desc = p.get("desc") or p.get("info") or ""
    html = ""
    img = p.get("img")
    if img:
        img_url = img if str(img).startswith("http") else base_url + img
        html += f'<img src="{kml_escape(img_url)}" width="320"/><br/>'
    if p.get("cat"):
        prio = p.get("prio") or ""
        html += f"<b>{kml_escape((prio + ' · ' if prio else '') + p['cat'])}</b><br/>"
    if desc:
        html += kml_escape(desc) + "<br/>"
    if p.get("dog"):
        html += f"<b>Perro:</b> {kml_escape(p['dog'])}<br/>"
    links = []
    if p.get("ficha"):
        links.append(f'<a href="{base_url}{p["ficha"]}">Ver ficha completa</a>')
    links.append(f'<a href="https://www.google.com/maps?q={p["lat"]},{p["lon"]}">Google Maps</a>')
    html += " · ".join(links)
    return html

def build_kml(name, points, base_url=SITE_URL):
    styles_used = {}
    pm = ""
    for p in points:
        style_id, href = kml_style_for(p)
        styles_used[style_id] = href
        cat_label = category_label(p)
        html = point_desc_html(p, base_url)
        pm += f"""
  <Placemark>
    <name>{kml_escape(p['name'])}</name>
    <description><![CDATA[{html}]]></description>
    <styleUrl>#{style_id}</styleUrl>
    <ExtendedData><SchemaData schemaUrl="#a27schema"><SimpleData name="categoria">{kml_escape(cat_label)}</SimpleData></SchemaData></ExtendedData>
    <Point><coordinates>{p['lon']},{p['lat']},0</coordinates></Point>
  </Placemark>"""
    style_defs = ""
    for style_id, href in sorted(styles_used.items()):
        style_defs += f"""
  <Style id="{style_id}"><IconStyle><Icon><href>{kml_escape(href)}</href></Icon></IconStyle></Style>"""
    schema = '\n  <Schema name="A27" id="a27schema"><SimpleField name="categoria" type="string"></SimpleField></Schema>'
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>{kml_escape(name)}</name>{schema}{style_defs}{pm}
</Document></kml>"""

def point_desc_plain(p):
    """Plain-text description for CSV import: My Maps shows each CSV column
    as a separate labeled field and does NOT render HTML inside a cell, so
    unlike point_desc_html() this stays free of tags."""
    parts = []
    if p.get("cat"):
        prio = p.get("prio") or ""
        parts.append((prio + " · " if prio else "") + p["cat"])
    desc = p.get("desc") or p.get("info") or ""
    if desc:
        parts.append(desc)
    if p.get("dog"):
        parts.append(f"Perro: {p['dog']}")
    return " — ".join(parts)

def build_csv(points, base_url=SITE_URL):
    """CSV alternative to build_kml(): unlike KML, My Maps exposes every
    column of an imported CSV/Sheet to 'Estilo individual > Agrupar por
    columna', so 'Categoria' here becomes stylable after import.
    Photo/Ficha/Maps are kept as bare URLs in their own columns (rather than
    HTML in Descripcion) since My Maps does not render HTML inside a CSV
    cell — it may auto-detect a bare image URL as a thumbnail and a bare
    URL as a clickable link."""
    import csv, io
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["Nombre", "Descripcion", "Foto", "Ficha", "Google Maps", "Categoria", "Latitude", "Longitude"])
    for p in points:
        img = p.get("img")
        img_url = (img if str(img).startswith("http") else base_url + img) if img else ""
        ficha_url = f'{base_url}{p["ficha"]}' if p.get("ficha") else ""
        maps_url = f'https://www.google.com/maps?q={p["lat"]},{p["lon"]}'
        w.writerow([p["name"], point_desc_plain(p), img_url, ficha_url, maps_url,
                    category_label(p), p["lat"], p["lon"]])
    return buf.getvalue()

# ---------------------------------------------------------------- build all
def main():
    (SITE / "assets/css").mkdir(parents=True, exist_ok=True)
    (SITE / "assets/js").mkdir(parents=True, exist_ok=True)
    (SITE / "assets/css/site.css").write_text(SITE_CSS, encoding="utf-8")
    (SITE / "assets/js/map.js").write_text(MAP_JS, encoding="utf-8")

    pages = {}  # path -> html

    # country registry for portal
    countries = []
    for slug, name, group, order, seguridad, frontera, visado, cpd, perro, nota in C:
        entry = {"slug": slug, "name": name, "group": group, "order": order, "estado": "borrador"}
        if slug in FULL:
            d = FULL[slug]
            entry["estado"] = "completa"
            entry["verificado"] = d.get("verificado", False)
            entry["img"] = d["hero_img"]
            metas = {"senegal": "Diama → Kalifourou · 17–21 días · rev. 8 sep 2026",
                     "mauritania": "Guerguerat → Diama · rev. 6 sep 2026"}
            entry["meta"] = metas.get(slug, f"{len(d['pois'])} PDIs · rev. {d['revision']}")
            pages[f"paises/{slug}/index.html"] = render_ficha(d)
            if d.get("historia_resumen"):
                pages[f"paises/{slug}/historia/index.html"] = render_historia(d)
        else:
            entry["meta"] = seguridad if seguridad != "—" else ""
            pages[f"paises/{slug}/index.html"] = render_stub(slug, name, group, seguridad, frontera, visado, cpd, perro, nota)
        countries.append(entry)

    pages["index.html"] = render_portal(countries)

    all_points, all_lines = [], []
    for d in FULL.values():
        all_points += map_points(d, with_ficha=True)
        all_lines += map_lines(d)
    pages["mapa/index.html"] = render_map_page(all_points, all_lines)
    pages["documentacion/index.html"] = render_docs()
    pages["perro/index.html"] = render_perro()

    name_by_slug = {slug: name for slug, name, *_ in C}
    countries_for_admin = [{"slug": slug, "name": name_by_slug.get(slug, slug)}
                            for slug in sorted(FULL) if (POIS_DIR / f"{slug}.json").exists()]
    admin_root = "../"
    admin_body = navbar(admin_root, [("Portal", admin_root), ("Documentación", admin_root + "documentacion/")], "Panel de edición")
    admin_body += render_admin(countries_for_admin)
    pages["admin/index.html"] = page(admin_root, "Panel de edición · África 2027", admin_body,
                                      extra_head=f"<style>{ADMIN_CSS}</style>")

    (SITE / "assets/js/points.json").write_text(json.dumps(all_points, ensure_ascii=False), encoding="utf-8")

    for path, html_text in pages.items():
        f = SITE / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html_text, encoding="utf-8")

    # manifest
    (SITE / "manifest.webmanifest").write_text(json.dumps({
        "name": "África 2027", "short_name": "África 2027",
        "description": "Fichas operativas de la expedición overland África 2027",
        "start_url": "./", "scope": "./", "display": "standalone",
        "background_color": "#16324F", "theme_color": "#16324F", "lang": "es",
        "icons": [
            {"src": "assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "assets/icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    # service worker: precache every site file
    precache = ["./"]
    EXCLUDE_DIRS = {"tools", ".github", "content", ".git"}
    for f in sorted(SITE.rglob("*")):
        if f.is_file() and not EXCLUDE_DIRS.intersection(f.parts) and f.name != "sw.js":
            rel = "./" + f.relative_to(SITE).as_posix()
            precache.append(rel)
            if rel.endswith("/index.html"):
                precache.append(rel[: -len("index.html")])
    ext_imgs = sorted({p["img"] for d in FULL.values() for p in d["pois"] if str(p["img"]).startswith("http")})
    sw = ("const VERSION = 'a27-" + VERSION + "';\nconst PRECACHE = " + json.dumps(precache) + ";\nconst EXT = " + json.dumps(ext_imgs) + ";\n" + r"""
self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => Promise.allSettled(
    PRECACHE.map(u => c.add(u)).concat(EXT.map(u => fetch(u, {mode:'no-cors'}).then(r => c.put(u, r)).catch(()=>{})))
  )));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSION && k !== 'a27-tiles').map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('message', e => { if (e.data === 'skip') self.skipWaiting(); });
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.hostname === 'tile.openstreetmap.org') {
    e.respondWith(caches.open('a27-tiles').then(c => c.match(req).then(m => m || fetch(req).then(res => { if (res.ok) c.put(req, res.clone()); return res; }).catch(() => new Response('', {status: 408})))));
    return;
  }
  if (req.mode === 'navigate' || (url.origin === location.origin && url.pathname.endsWith('.html'))) {
    e.respondWith(fetch(req).then(res => { const copy = res.clone(); caches.open(VERSION).then(c => c.put(req, copy)); return res; })
      .catch(() => caches.match(req, {ignoreSearch: true}).then(m => m || caches.match('./index.html'))));
    return;
  }
  e.respondWith(caches.match(req, {ignoreSearch: true}).then(m => m || fetch(req).then(res => {
    if (res.ok && (url.origin === location.origin || url.hostname.includes('gstatic') || url.hostname.includes('googleapis'))) {
      const copy = res.clone(); caches.open(VERSION).then(c => c.put(req, copy));
    }
    return res;
  })));
});
""")
    (SITE / "sw.js").write_text(sw, encoding="utf-8")

    # KML exports for My Maps (layer strategy: 9 country-group layers + 1 services)
    kml_dir = SITE / "assets/kml"
    kml_dir.mkdir(parents=True, exist_ok=True)
    layer_groups = {
        "01 Marruecos-Mauritania": ["marruecos", "sahara-occidental", "mauritania"],
        "02 Senegal-Sierra Leona": ["senegal", "guinea", "sierra-leona"],
        "03 Liberia-Nigeria": ["liberia", "costa-de-marfil", "ghana", "togo", "benin", "nigeria"],
        "05 Camerun-Angola": ["camerun", "gabon", "congo", "rd-congo", "angola"],
        "06 Namibia-Sudafrica": ["namibia", "sudafrica"],
        "07 Mozambique-Kenia": ["mozambique", "malaui", "tanzania", "kenia"],
        "08 Etiopia-Egipto": ["etiopia", "sudan", "egipto"],
        "09 Alternativas": ["gambia", "lesoto", "esuatini", "zimbabue", "botsuana",
                             "zambia", "uganda", "ruanda", "yibuti"],
    }
    for lname, slugs in layer_groups.items():
        pts = []
        for s in slugs:
            if s in FULL:
                pts += [p for p in map_points(FULL[s], with_ficha=True) if p["type"] == "poi"]
        if pts:
            (kml_dir / f"{lname}.kml").write_text(build_kml(f"África 2027 · {lname}", pts), encoding="utf-8")
            (kml_dir / f"{lname}.csv").write_text(build_csv(pts), encoding="utf-8")
    services = []
    for d in FULL.values():
        services += [p for p in map_points(d, with_ficha=True) if p["type"] != "poi"]
    (kml_dir / "10 Emergencias y logistica.kml").write_text(build_kml("África 2027 · Emergencias y logística", services), encoding="utf-8")
    (kml_dir / "10 Emergencias y logistica.csv").write_text(build_csv(services), encoding="utf-8")

    print("pages:", len(pages), "| precache:", len(precache), "| version:", VERSION)

if __name__ == "__main__":
    main()

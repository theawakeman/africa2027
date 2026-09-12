"""Shared building blocks for the África 2027 site generator."""
import html as _html
import json
from pathlib import Path

# Raíz del repositorio: este archivo vive en <repo>/tools/gen/site_common.py
SITE = Path(__file__).resolve().parent.parent.parent
MYMAPS = "https://www.google.com/maps/d/edit?hl=es&mid=1brUmvoMOalT61Od_OwLFWtfjZwFxd8M"

# Campos de la ficha de país editables desde el panel (/admin/) vía
# content/ficha/<slug>.json. Si el JSON existe, cada clave presente en él
# sustituye a la calculada por data_<pais>.py; las claves ausentes del JSON
# se dejan tal cual las produjo el módulo Python del país.
FICHA_FIELDS = [
    "hero_img", "hero_credit", "chips",
    "historia_resumen", "historia_secciones", "historia_fuentes",
    "logistics", "sources", "sources_note",
    "emergency", "matrix_note", "notice",
    "custom_sections", "custom_sections_post",
]

def esc(s):
    return _html.escape(str(s), quote=False)

def attr(s):
    return _html.escape(str(s), quote=True)

def gmaps(lat, lon, label=None):
    """Clickable coordinates -> Google Maps."""
    txt = label or f"{lat:.5f}, {lon:.5f}"
    return f'<a class="coord" href="https://www.google.com/maps?q={lat:.5f},{lon:.5f}" target="_blank" rel="noopener">{esc(txt)}</a>'

SITE_CSS = """
:root {
  --navy:#16324F; --teal:#1E7A8A; --sand:#D9B26F;
  --bg:#FAF7F1; --surface:#FFFFFF; --surface2:#F1EDE4;
  --ink:#22303C; --ink-soft:#5B6B77; --line:#E2DCD0;
  --green:#2E7D32; --green-bg:#E5F1E5; --amber:#9A6410; --amber-bg:#FCF1DA;
  --red:#B43A3A; --red-bg:#F9E7E7; --grey:#5F6B72; --grey-bg:#EBEDEE;
  --link:#186875; --head:#16324F; --th-bg:#16324F;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg:#141A21; --surface:#1C242D; --surface2:#232D38;
    --ink:#E4E9ED; --ink-soft:#9AA8B3; --line:#33404C;
    --green:#7FC784; --green-bg:#1E3320; --amber:#E4B565; --amber-bg:#3A2E14;
    --red:#E58989; --red-bg:#3D2020; --grey:#A9B4BC; --grey-bg:#2A343D;
    --link:#6FC2D0; --head:#BFD5E8; --teal:#4FA3B2; --sand:#C2A468; --th-bg:#0E2233;
  }
}
:root[data-theme="dark"] {
  --bg:#141A21; --surface:#1C242D; --surface2:#232D38;
  --ink:#E4E9ED; --ink-soft:#9AA8B3; --line:#33404C;
  --green:#7FC784; --green-bg:#1E3320; --amber:#E4B565; --amber-bg:#3A2E14;
  --red:#E58989; --red-bg:#3D2020; --grey:#A9B4BC; --grey-bg:#2A343D;
  --link:#6FC2D0; --head:#BFD5E8; --teal:#4FA3B2; --sand:#C2A468; --th-bg:#0E2233;
}
* { box-sizing:border-box; }
[hidden] { display:none !important; }
html { scroll-behavior:smooth; }
@media (prefers-reduced-motion:reduce) { html { scroll-behavior:auto; } }
body { background:var(--bg); color:var(--ink); font-family:"Source Serif 4", Georgia, serif; font-size:16.5px; line-height:1.62; margin:0; }
img { max-width:100%; }
h1,h2,h3,h4, .nav, .st, .prio, .cat, .time, th, .callout-title, .kicker, .chip-label, .badge, .btn { font-family:"Archivo", "Helvetica Neue", Arial, sans-serif; }
a { color:var(--link); text-decoration-thickness:1px; text-underline-offset:2px; }
a:focus-visible, button:focus-visible, [tabindex]:focus-visible { outline:2px solid var(--teal); outline-offset:2px; }
a.coord { white-space:nowrap; font-family:"Archivo",sans-serif; font-variant-numeric:tabular-nums; }

.nav { position:sticky; top:0; z-index:500; background:var(--navy); display:flex; align-items:center; gap:2px; overflow-x:auto; padding:0 10px; scrollbar-width:thin; }
.nav .brand { color:#fff; font-weight:800; font-size:12px; letter-spacing:.12em; padding:12px 10px; white-space:nowrap; text-decoration:none; }
.nav a:not(.brand) { color:#CBD8E4; text-decoration:none; font-size:12.5px; font-weight:600; padding:12px 9px; white-space:nowrap; }
.nav a:hover { color:#fff; }

.hero { position:relative; overflow:hidden; background:var(--navy); }
.hero img.bg { width:100%; height:min(52vw, 430px); object-fit:cover; display:block; opacity:.85; }
.hero .veil { position:absolute; inset:0; background:linear-gradient(180deg, rgba(22,50,79,.25) 0%, rgba(22,50,79,.82) 78%, rgba(22,50,79,.95) 100%); }
.hero .inner { position:absolute; left:0; right:0; bottom:0; padding:18px clamp(16px,4vw,48px) 20px; color:#fff; }
.kicker { font-size:12px; font-weight:700; letter-spacing:.22em; color:var(--sand); }
.hero h1 { margin:.1em 0 .1em; font-size:clamp(34px, 7vw, 58px); font-weight:800; line-height:1.02; text-wrap:balance; color:#fff; }
.hero .sub { margin:0; font-size:clamp(14px,2.6vw,17px); color:#D9E3EC; font-style:italic; }
.hero .photo-credit { position:absolute; top:10px; right:14px; font-size:11px; color:#E7EDF3; background:rgba(22,50,79,.55); padding:3px 8px; border-radius:4px; }
.hero .photo-credit a { color:#E7EDF3; }
@media (max-width:640px) { .hero .photo-credit { display:none; } }

.chips { display:grid; grid-template-columns:repeat(auto-fit, minmax(150px,1fr)); gap:1px; background:var(--line); border-bottom:1px solid var(--line); }
.chip { background:var(--surface); padding:12px 14px; text-align:center; }
.chip-label { display:block; font-size:10.5px; font-weight:700; letter-spacing:.14em; color:var(--teal); }
.chip b { font-size:14px; font-weight:600; font-family:"Archivo",sans-serif; }
.chip b .st { font-size:12px; }

main { max-width:980px; margin:0 auto; padding:8px clamp(14px,4vw,32px) 60px; }
.notice { text-align:center; font-style:italic; color:var(--ink-soft); font-size:14.5px; margin:18px auto 6px; max-width:680px; }

section { margin-top:44px; scroll-margin-top:58px; }
h2 { font-size:clamp(23px,4vw,29px); font-weight:800; color:var(--head); margin:0 0 6px; padding-bottom:8px; border-bottom:3px solid var(--sand); text-wrap:balance; }
h3 { font-size:17px; font-weight:700; color:var(--teal); margin:26px 0 6px; }
h4 { font-size:14.5px; font-weight:700; color:var(--head); margin:18px 0 4px; }
p { margin:.5em 0; }

.callout { border-radius:8px; padding:13px 16px; margin:16px 0; background:var(--surface2); border-left:4px solid var(--teal); }
.callout p { margin:2px 0 0; font-size:15px; }
.callout-title { font-size:11px; font-weight:800; letter-spacing:.14em; text-transform:uppercase; color:var(--teal); }
.callout.warn { border-left-color:var(--amber); background:var(--amber-bg); } .callout.warn .callout-title { color:var(--amber); }
.callout.danger { border-left-color:var(--red); background:var(--red-bg); } .callout.danger .callout-title { color:var(--red); }
.callout.ok { border-left-color:var(--green); background:var(--green-bg); } .callout.ok .callout-title { color:var(--green); }

.tblwrap { overflow-x:auto; margin:14px 0; border:1px solid var(--line); border-radius:8px; background:var(--surface); }
table { border-collapse:collapse; width:100%; font-size:13.5px; font-family:"Archivo",sans-serif; }
th { background:var(--th-bg); color:#fff; text-align:left; padding:8px 10px; font-size:12px; letter-spacing:.04em; white-space:nowrap; }
td { padding:7px 10px; border-top:1px solid var(--line); vertical-align:top; }
tbody tr:nth-child(even) td { background:var(--surface2); }
td:first-child { font-weight:600; }
.num td { font-variant-numeric:tabular-nums; }
tr.rowlink { cursor:pointer; }
tr.rowlink:hover td { background:var(--amber-bg); }

.st { display:inline-block; font-size:11.5px; font-weight:700; padding:2px 9px; border-radius:99px; line-height:1.5; }
.st-green { background:var(--green-bg); color:var(--green); }
.st-amber { background:var(--amber-bg); color:var(--amber); }
.st-red { background:var(--red-bg); color:var(--red); }
.st-grey { background:var(--grey-bg); color:var(--grey); }

ul.ticks { padding-left:0; list-style:none; }
ul.ticks li { margin:7px 0; padding-left:22px; position:relative; }
ul.ticks li::before { content:""; position:absolute; left:2px; top:.55em; width:9px; height:9px; border-radius:2px; background:var(--sand); }

.poi-grid { display:grid; grid-template-columns:repeat(auto-fill, minmax(290px,1fr)); gap:18px; margin-top:18px; }
.poi-card { background:var(--surface); border:1px solid var(--line); border-radius:10px; overflow:hidden; display:flex; flex-direction:column; }
.poi-card img { width:100%; aspect-ratio:16/9; object-fit:cover; display:block; }
/* Enlaces a fichas de país desde la sección del perro */
.paislink { color:inherit; text-decoration:none; border-bottom:1px dotted #1E7A8A; }
.paislink:hover { color:#1E7A8A; border-bottom-style:solid; }
.paisidx { margin:0 0 22px; padding:14px 16px; background:#f4f7f8; border:1px solid #dde5e8; border-radius:10px; }
.paisidx-lab { display:block; font-size:12px; text-transform:uppercase; letter-spacing:.06em;
  color:#5c6b72; margin-bottom:9px; }
.paischip { display:inline-block; margin:0 6px 6px 0; padding:4px 10px; font-size:13px;
  background:#fff; border:1px solid #cfdade; border-radius:999px; color:#1E7A8A; text-decoration:none; }
.paischip:hover { background:#1E7A8A; border-color:#1E7A8A; color:#fff; }
.poi-noimg { width:100%; aspect-ratio:16/9; display:flex; align-items:center; justify-content:center;
  background:repeating-linear-gradient(45deg,#eceff1,#eceff1 10px,#e3e7ea 10px,#e3e7ea 20px);
  color:#7a848a; font-size:12px; letter-spacing:.04em; text-align:center; padding:0 14px; }
.poi-body { padding:12px 14px 14px; display:flex; flex-direction:column; gap:7px; flex:1; }
.poi-body h3 { margin:0; font-size:16px; color:var(--head); line-height:1.25; }
.poi-tags { display:flex; flex-wrap:wrap; gap:6px; font-size:11px; font-weight:700; align-items:center; }
.prio { color:var(--navy); background:var(--surface2); border:1px solid var(--line); padding:1px 8px; border-radius:99px; font-family:"Archivo",sans-serif; font-size:11px; font-weight:700; }
:root[data-theme="dark"] .prio { color:var(--ink); }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .prio { color:var(--ink); } }
.cat { color:var(--teal); }
.time { color:var(--ink-soft); }
.poi-desc { font-size:14px; margin:0; color:var(--ink); }
.dognote { font-size:13px; color:var(--ink-soft); }
.credit { font-size:12px; color:var(--ink-soft); font-family:"Archivo",sans-serif; margin-top:auto; padding-top:4px; border-top:1px dashed var(--line); }

.mapbox { height:min(72vh, 560px); border:1px solid var(--line); border-radius:10px; margin:16px 0 6px; background:var(--surface2); position:relative; z-index:0; }
.mapbox.tall { height:calc(100vh - 120px); min-height:420px; }
.figcap { font-size:13px; color:var(--ink-soft); text-align:center; margin-top:6px; }
.leaflet-popup-content { font-family:"Archivo",sans-serif; font-size:13px; line-height:1.45; margin:10px 12px; }
.leaflet-popup-content img { border-radius:6px; margin-bottom:6px; }
.leaflet-popup-content .st { font-size:10.5px; }
.leaflet-container { font-family:"Archivo",sans-serif; background:#DCE7DC; }

dialog.poi-modal { border:none; border-radius:12px; padding:0; max-width:520px; width:calc(100vw - 32px); background:var(--surface); color:var(--ink); box-shadow:0 12px 50px rgba(0,0,0,.4); }
dialog.poi-modal::backdrop { background:rgba(10,20,30,.55); }
dialog.poi-modal .poi-card { border:none; border-radius:0; }
dialog.poi-modal .close { position:absolute; top:8px; right:8px; z-index:2; background:rgba(22,50,79,.75); color:#fff; border:none; border-radius:99px; width:32px; height:32px; font-size:17px; cursor:pointer; font-family:Archivo,sans-serif; }

.srcs { columns:2; column-gap:34px; padding-left:18px; font-size:14.5px; font-family:"Archivo",sans-serif; }
.srcs li { margin:6px 0; break-inside:avoid; }
@media (max-width:640px) { .srcs { columns:1; } }

.cards { display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:14px; }
.card { background:var(--surface); border:1px solid var(--line); border-radius:12px; overflow:hidden; text-decoration:none; color:var(--ink); display:flex; flex-direction:column; }
a.card { transition:transform .15s ease; } a.card:hover { transform:translateY(-2px); }
.card img { width:100%; aspect-ratio:16/8.5; object-fit:cover; display:block; }
.card .body { padding:11px 14px 13px; display:flex; flex-direction:column; gap:5px; }
.card h3 { margin:0; font-size:17px; color:var(--head); }
.card .meta { font-family:"Archivo",sans-serif; font-size:12.5px; color:var(--ink-soft); }
.badge { align-self:flex-start; font-size:11px; font-weight:700; padding:2px 10px; border-radius:99px; }
.b-ok { background:var(--green-bg); color:var(--green); }
.b-draft { background:var(--amber-bg); color:var(--amber); }
.b-off { background:var(--grey-bg); color:var(--grey); }
.b-x { background:var(--red-bg); color:var(--red); }
.hero .verif-badge { display:inline-block; margin:8px 0 2px; align-self:auto; }

.btn { display:inline-block; background:var(--teal); color:#fff; border:none; border-radius:8px; padding:8px 16px; font-size:14px; font-weight:700; text-decoration:none; cursor:pointer; }
.btn.ghost { background:transparent; color:var(--teal); border:1px solid var(--teal); }

.audio-bar { display:flex; align-items:center; flex-wrap:wrap; gap:10px; background:var(--surface2); border:1px solid var(--line); border-radius:10px; padding:12px 16px; margin:18px 0 4px; }
.audio-status { font-family:"Archivo",sans-serif; font-size:13px; color:var(--ink-soft); }
.historia-article { font-size:16.5px; margin-top:10px; }
.historia-article h3 { margin-top:30px; }

footer { border-top:1px solid var(--line); margin-top:56px; padding:18px 0 4px; font-size:13px; color:var(--ink-soft); text-align:center; font-family:"Archivo",sans-serif; }
@media print { .nav, .mapbox, dialog { display:none !important; } body { font-size:12px; } }
"""

SW_SNIPPET = """
<div id="upd" hidden style="position:fixed;bottom:14px;left:50%;transform:translateX(-50%);z-index:999;background:#16324F;color:#fff;font-family:Archivo,sans-serif;font-size:14px;padding:10px 18px;border-radius:99px;box-shadow:0 4px 18px rgba(0,0,0,.35);cursor:pointer">Nueva versión disponible · toca para actualizar</div>
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register(document.querySelector('link[rel=manifest]').getAttribute('href').replace('manifest.webmanifest','sw.js')).then(reg => {
    function watch(sw){ sw.addEventListener('statechange', () => { if (sw.state === 'installed' && navigator.serviceWorker.controller) show(reg); }); }
    if (reg.waiting && navigator.serviceWorker.controller) show(reg);
    if (reg.installing) watch(reg.installing);
    reg.addEventListener('updatefound', () => watch(reg.installing));
  });
  let reloading = false;
  navigator.serviceWorker.addEventListener('controllerchange', () => { if (!reloading) { reloading = true; location.reload(); } });
  function show(reg){ const el = document.getElementById('upd'); el.hidden = false; el.onclick = () => { el.hidden = true; reg.waiting && reg.waiting.postMessage('skip'); }; }
}
</script>"""

MODAL_JS = """
<script>
(function(){
  const dlg = document.getElementById('poi-dlg');
  if (!dlg) return;
  function openPoiCard(id){
    const card = document.getElementById(id);
    if (!card) return false;
    dlg.querySelector('.holder').innerHTML = card.outerHTML.replace(/ id="[^"]*"/, '');
    dlg.showModal();
    return true;
  }
  document.querySelectorAll('[data-poi]').forEach(el => {
    el.addEventListener('click', ev => {
      if (ev.target.closest('a')) return;
      openPoiCard(el.getAttribute('data-poi'));
    });
    if (el.tagName === 'TR') { el.classList.add('rowlink'); el.setAttribute('tabindex','0');
      el.addEventListener('keydown', e => { if (e.key === 'Enter') el.click(); }); }
  });
  dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });
  // Enlaces directos tipo .../pais/#poi-12 (usados en el campo "Ficha" de My Maps):
  // abren la ficha del punto directamente, en vez de depender del salto de ancla nativo del navegador.
  function openFromHash(){
    const m = /^#poi-\\d+$/.exec(location.hash);
    if (m) openPoiCard(location.hash.slice(1));
  }
  openFromHash();
  window.addEventListener('hashchange', openFromHash);
})();
</script>"""

def head(root, title):
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#16324F">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="icon" href="{root}assets/icons/icon-192.png">
<link rel="apple-touch-icon" href="{root}assets/icons/icon-192.png">
<link rel="stylesheet" href="{root}assets/css/site.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">
<title>{esc(title)}</title>"""

def page(root, title, body, extra_head=""):
    return f"""<!doctype html>
<html lang="es">
<head>
{head(root, title)}{extra_head}
</head>
<body>
{body}
{SW_SNIPPET}
</body>
</html>"""

def table(headers, rows, cls="", row_attrs=None):
    h = "".join(f"<th>{esc(x)}</th>" for x in headers)
    body = ""
    for i, r in enumerate(rows):
        extra = (row_attrs[i] if row_attrs else "") or ""
        body += f"<tr {extra}>" + "".join(f"<td>{c if str(c).startswith('<') else esc(c)}</td>" for c in r) + "</tr>"
    return f'<div class="tblwrap"><table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table></div>'

def callout(kind, title, body_html, raw=False):
    b = body_html if raw else esc(body_html)
    return f'<div class="callout {kind}"><div class="callout-title">{esc(title)}</div><p>{b}</p></div>'

def bullets(items_list, bold_split=False):
    lis = ""
    for t in items_list:
        if str(t).startswith("<"):
            lis += f"<li>{t}</li>"
        elif bold_split and ":" in t[:42]:
            pre, rest = t.split(":", 1)
            lis += f"<li><strong>{esc(pre)}:</strong>{esc(rest)}</li>"
        else:
            lis += f"<li>{esc(t)}</li>"
    return f'<ul class="ticks">{lis}</ul>'

def st_pill(status_text):
    s = status_text.lower()
    if ("prohibido" in s or "conflicto" in s or "no viable" in s or "guerra" in s or "cerrad" in s or "excluido" in s) and "pendiente" not in s:
        cls = "st-red"
    elif "pendiente" in s or "verificar" in s or "sin datos" in s:
        cls = "st-grey"
    elif ("autorización" in s or "condicion" in s or "precaución" in s or "riesgo" in s or "naranja" in s
          or "recomendado" in s or "borrador" in s or "exigido" in s or "obligatorio" in s or "imprescindible" in s):
        cls = "st-amber"
    else:
        cls = "st-green"
    return f'<span class="st {cls}">{esc(status_text)}</span>'

MODAL_HTML = '<dialog class="poi-modal" id="poi-dlg"><button class="close" onclick="this.closest(\'dialog\').close()" aria-label="Cerrar">×</button><div class="holder"></div></dialog>'

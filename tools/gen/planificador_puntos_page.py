# -*- coding: utf-8 -*-
"""Página /planificador-puntos/ (beta): el viaje se hace punto a punto.

Proyecto aparte del Planificador actual (/planificador/): archivos propios
(assets/js/planificador-puntos.js), viajes guardados aparte y ningún cambio en
la otra página. Usa los datos de la fase 1 (assets/js/planificador-puntos.json).
"""
import json

import data_ruta as RT
from data_countries import C, REGION
from presupuesto_page import datos as datos_presupuesto
from site_common import esc, page
from planificador_puntos import PISTAS

JS = "planificador-puntos.js"


def config(FULL):
    D = datos_presupuesto(FULL, C)
    PA = D["ruta"]["paises"]
    nombres = {c[0]: c[1].split(" (")[0] for c in C}
    paises = {}
    for s, n in nombres.items():
        p = PA.get(s)
        paises[s] = {"n": n, "r": REGION.get(s, ""), "cf": s in RT.CONFLICTO, "isla": s in RT.ISLAS,
                     "pos": p["pos"] if p else None,
                     "rec": [{"id": o["id"], "l": o["l"], "pts": o["pts"]} for o in (p["opts"] if p else [])
                             if not o["id"].startswith("R")]}
    fronteras = []
    for a, b, tipo, nota in RT.FRONTERAS:
        a, b = ("angola" if a == "cabinda" else a), ("angola" if b == "cabinda" else b)
        if a != b:
            fronteras.append([a, b, tipo])
    ferris = [{"id": f[0], "pais": f[1], "origen": f[2], "puerto": f[3], "pos": [f[4], f[5]], "naviera": f[6],
               "h": f[7], "km_eu": f[12]} for f in RT.FERRIES]
    return {"paises": paises, "fronteras": fronteras, "ferris": ferris, "ferry_pref": RT.FERRY_PREFERIDO,
            "salida": RT.SALIDA, "origen": RT.ORIGEN, "pistas": PISTAS}


CSS = """
.pp-wrap{display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:14px;align-items:start;margin:12px 0}
#pp-mapa{height:calc(100vh - 110px);min-height:460px;border-radius:12px;border:1px solid var(--line);background:var(--surface2)}
.pp-panel{position:sticky;top:60px;max-height:calc(100vh - 80px);overflow:auto;border:1px solid var(--line);border-radius:12px;background:var(--surface);font-family:"Archivo",sans-serif}
.pp-sec{padding:12px 14px;border-top:1px solid var(--line)}
.pp-sec:first-child{border-top:0}
.pp-sec h3{font-size:12px;letter-spacing:.12em;text-transform:uppercase;margin:0 0 8px;color:var(--ink-soft);display:flex;justify-content:space-between;align-items:center;gap:8px}
.pp-sec h3 .cnt{font-weight:600;letter-spacing:0;text-transform:none;font-size:12px}
.pp-ida h3{color:#1E7A8A}.pp-vuelta h3{color:#B7791F}
.pp-lista{list-style:none;margin:0;padding:0;min-height:34px;border:1px dashed transparent;border-radius:8px}
.pp-lista:empty{border-color:var(--line)}
.pp-lista:empty::after{content:"Toca puntos en el mapa y añádelos aquí";display:block;padding:8px;font-size:12.5px;color:var(--ink-soft)}
.pp-it{display:grid;grid-template-columns:14px 24px minmax(0,1fr) auto;gap:6px;align-items:center;padding:6px 4px;border-bottom:1px solid var(--line);font-size:13.5px}
.pp-it:last-child{border-bottom:0}
.pp-h{cursor:grab;color:var(--ink-soft);user-select:none}
.pp-n{width:22px;height:22px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:#fff}
.pp-ida .pp-n{background:#1E7A8A}.pp-vuelta .pp-n{background:#C47F17}
.pp-t{min-width:0}.pp-t strong{display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:600}
.pp-t small{color:var(--ink-soft);font-size:11.5px}
.pp-a{display:flex;gap:3px;align-items:center}
.pp-a input{width:54px;font:inherit;font-size:12.5px;padding:3px 4px;border:1px solid var(--line);border-radius:6px;background:var(--surface);color:var(--ink);text-align:right}
.pp-a input.edited{border-color:var(--amber);background:var(--amber-bg)}
.pp-b{font:inherit;font-size:12px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:6px;padding:3px 6px;cursor:pointer;line-height:1.2}
.pp-b[aria-pressed="true"]{border-color:var(--amber);background:var(--amber-bg)}
.pp-b.x{color:#B43A3A}
.pp-b.big{font-size:13px;font-weight:600;padding:7px 10px}
.pp-b.ida{background:#1E7A8A;border-color:#1E7A8A;color:#fff}.pp-b.vuelta{background:#C47F17;border-color:#C47F17;color:#fff}
.pp-row{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:6px 0}
.pp-row label{font-size:12.5px;color:var(--ink-soft);display:flex;gap:6px;align-items:center}
.pp-row select,.pp-row input{font:inherit;font-size:13px;padding:5px 7px;border:1px solid var(--line);border-radius:7px;background:var(--surface);color:var(--ink)}
.pp-row select{max-width:100%;min-width:0}
.pp-row label.full{flex:1 1 100%;min-width:0}.pp-row label.full select{flex:1;width:100%}
.pp-sum{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin:4px 0 8px}
.pp-sum div{background:var(--surface2);border-radius:8px;padding:7px 8px}
.pp-sum b{display:block;font-size:17px;font-variant-numeric:tabular-nums}
.pp-sum span{font-size:11px;color:var(--ink-soft);text-transform:uppercase;letter-spacing:.08em}
.pp-avisos{list-style:none;margin:6px 0 0;padding:0;font-size:12.5px}
.pp-avisos li{padding:5px 8px;border-radius:7px;margin:4px 0;background:var(--amber-bg)}
.pp-avisos li.rojo{background:rgba(180,58,58,.12);color:#8E2B2B}
.pp-paises{display:flex;flex-wrap:wrap;gap:4px;margin-top:6px}
.pp-paises span{font-size:11.5px;border-radius:99px;padding:2px 8px;border:1px solid var(--line)}
.pp-paises span.fuera{border-color:#B43A3A;color:#B43A3A}
.pp-tira{display:flex;height:14px;border-radius:7px;overflow:hidden;margin:8px 0 2px}
.pp-tira i{display:block;height:100%}
.pp-pop{font-family:"Archivo",sans-serif;min-width:220px}
.pp-pop strong{font-size:14px;display:block;margin-bottom:2px}
.pp-pop .meta{font-size:12px;color:#5F6B72;margin-bottom:6px}
.pp-pop .perro{font-size:11.5px;display:inline-block;border-radius:99px;padding:1px 7px;margin-bottom:6px}
.pp-pop .perro.si{background:#E5F1E5;color:#2E7D32}.pp-pop .perro.condiciones{background:#FCF1DA;color:#9A6410}.pp-pop .perro.no{background:#F6E1E1;color:#B43A3A}.pp-pop .perro.sin_dato{background:#EEF0F1;color:#5F6B72}
.pp-pop .acc{display:flex;flex-wrap:wrap;gap:5px;margin-top:6px}
.pp-pop img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;border-radius:6px;margin-bottom:8px;background:#EEF0F1}
.pp-pop .a27-map-summary{font-size:12.5px;line-height:1.4;margin-bottom:6px;-webkit-line-clamp:4}
@media (max-width:600px){.pp-pop img{aspect-ratio:2/1}.pp-pop .a27-map-summary{-webkit-line-clamp:3}}
.pp-pop .pp-cargando{display:block;font-size:12px;color:#5F6B72;margin-bottom:6px}
.pp-pop .lnk{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-top:8px;font:700 12px/1.35 "Archivo",sans-serif}
.pp-pop .lnk a{color:var(--teal)}
.pp-pop .a27-popup-expand{font-size:12.5px}
.pp-ver{appearance:none;border:0;background:none;padding:0;margin:0;font:inherit;color:inherit;text-align:left;cursor:pointer;display:block;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:600}
.pp-ver:hover,.pp-ver:focus-visible{color:var(--teal);text-decoration:underline}
.pp-dlg-acc{display:flex;gap:6px;flex-wrap:wrap;align-items:center;padding:12px 18px;border-top:1px solid var(--line);background:var(--surface);position:sticky;bottom:0}
.pp-dlg-acc .en{font:600 12.5px "Archivo",sans-serif;color:var(--ink-soft);margin-right:4px}
.pp-mk{border-radius:50%;color:#fff;font:700 11px "Archivo",sans-serif;display:flex;align-items:center;justify-content:center;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.35)}
.pp-mk.ida{background:#1E7A8A}.pp-mk.vuelta{background:#C47F17}.pp-mk.libre{border-style:dashed}
.pp-fr{width:12px;height:12px;background:#5F6B72;transform:rotate(45deg);border:2px solid #fff;box-shadow:0 1px 2px rgba(0,0,0,.4)}
.pp-puerto{font-size:18px;line-height:1}
.pp-ayuda{font-size:12.5px;color:var(--ink-soft);margin:0}
.pp-ayuda b{color:var(--ink)}
#pp-msg{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);background:var(--ink);color:var(--surface);padding:9px 14px;border-radius:10px;font:600 13px "Archivo",sans-serif;z-index:2000;max-width:90vw;box-shadow:0 4px 14px rgba(0,0,0,.25)}
.pp-it.sortable-ghost{opacity:.35}
@media (max-width:900px){.pp-wrap{grid-template-columns:1fr}#pp-mapa{height:68vh;min-height:360px}.pp-panel{position:static;max-height:none}}
"""


def render(FULL, navbar, VERSION):
    root = "../"
    nav = navbar(root, [("Portal", root), ("Planificador actual", root + "planificador/"), ("Mapa", root + "mapa/"),
                        ("Documentación", root + "documentacion/")], "Planificador por puntos · beta")
    cfg = config(FULL)
    body = f"""{nav}
<main style="max-width:1500px">
<h2 style="margin-top:16px">Planificador por puntos <small style="font-size:13px;color:var(--amber);letter-spacing:.1em">BETA</small></h2>
<p class="pp-ayuda"><b>1.</b> Toca un país para ver sus puntos de interés. <b>2.</b> Toca un punto y añádelo a la <b style="color:#1E7A8A">ida</b> o a la <b style="color:#C47F17">vuelta</b>. <b>3.</b> Ordena arrastrando en la lista. La carretera, las fronteras, los km y los días salen solos. Clic derecho (o mantener pulsado) en cualquier sitio del mapa = «pasar por aquí». Tus viajes de esta página se guardan aparte del Planificador actual.</p>
<div class="pp-wrap">
  <div id="pp-mapa" role="application" aria-label="Mapa: toca países y puntos para montar el viaje"></div>
  <aside class="pp-panel" aria-label="Viaje">
    <div class="pp-sec">
      <h3>Tu viaje <span class="cnt" id="pp-nombre"></span></h3>
      <div class="pp-sum"><div><b id="pp-km">0</b><span>km</span></div><div><b id="pp-dias">0</b><span>días</span></div><div><b id="pp-np">0</b><span>países</span></div></div>
      <div class="pp-tira" id="pp-tira" aria-hidden="true"></div>
      <div id="pp-fechas" style="font-size:12.5px;color:var(--ink-soft)"></div>
      <div class="pp-paises" id="pp-paises"></div>
      <ul class="pp-avisos" id="pp-avisos"></ul>
    </div>
    <div class="pp-sec pp-ida">
      <h3>Ida <span class="cnt" id="pp-cnt-ida"></span></h3>
      <div class="pp-row"><label class="full">Llegada <select id="pp-fer-ida"></select></label></div>
      <ol class="pp-lista" id="pp-lista-ida"></ol>
      <div class="pp-row"><button type="button" class="pp-b" id="pp-ord-ida">Ordenar la ida por cercanía</button></div>
    </div>
    <div class="pp-sec pp-vuelta">
      <h3>Vuelta <span class="cnt" id="pp-cnt-vuelta"></span></h3>
      <ol class="pp-lista" id="pp-lista-vuelta"></ol>
      <div class="pp-row"><label class="full">Salida <select id="pp-fer-vuelta"></select></label></div>
      <div class="pp-row"><button type="button" class="pp-b" id="pp-ord-vuelta">Ordenar la vuelta por cercanía</button></div>
    </div>
    <div class="pp-sec">
      <h3>Ajustes</h3>
      <div class="pp-row"><label>Salida de {esc(cfg['origen'])} <input type="date" id="pp-salida"></label></div>
      <div class="pp-row"><label>Km de conducción al día <input type="number" id="pp-kmdia" min="50" step="10" style="width:70px"></label><label>Margen % <input type="number" id="pp-margen" min="0" step="1" style="width:56px"></label></div>
      <div class="pp-row"><label><input type="checkbox" id="pp-verfr"> Ver puestos fronterizos</label><label><input type="checkbox" id="pp-vertodos"> Ver puntos de todos los países</label></div>
    </div>
    <div class="pp-sec">
      <h3>Mis viajes</h3>
      <div class="pp-row"><select id="pp-viajes" style="flex:1"></select><button type="button" class="pp-b" id="pp-cargar">Cargar</button><button type="button" class="pp-b x" id="pp-borrar">Borrar</button></div>
      <div class="pp-row"><input type="text" id="pp-vnombre" placeholder="Nombre del viaje" style="flex:1" autocomplete="off" data-1p-ignore data-lpignore="true"><button type="button" class="pp-b ida" id="pp-guardar">Guardar</button></div>
      <div class="pp-row"><button type="button" class="pp-b" id="pp-nuevo">Empezar de cero</button><button type="button" class="pp-b" id="pp-exportar">Descargar</button><label class="pp-b" style="cursor:pointer">Importar<input type="file" id="pp-importar" accept=".json,application/json" hidden></label></div>
    </div>
  </aside>
</div>
<div id="pp-msg" role="status" aria-live="polite" hidden></div>
<footer>ÁFRICA 2027 · Planificador por puntos (beta)</footer>
</main>
<script>var A27_PP = {json.dumps(cfg, ensure_ascii=False, separators=(",", ":"))};</script>
<script src="{root}assets/vendor/leaflet.js"></script>
<script src="{root}assets/vendor/Sortable.min.js"></script>
<script src="{root}assets/js/map.js"></script>
<script src="{root}assets/js/{JS}"></script>"""
    extra = f'<link rel="stylesheet" href="{root}assets/vendor/leaflet.css"><style>{CSS}</style>'
    return page(root, "Planificador por puntos · África 2027", body, extra_head=extra)

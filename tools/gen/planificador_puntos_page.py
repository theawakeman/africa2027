# -*- coding: utf-8 -*-
"""Página /planificador/: el Planificador (por puntos). El viaje se hace punto a punto.

El planificador anterior, por países, sigue en /planificador-clasico/ (presupuesto_page.py).
Archivos propios (assets/js/planificador-puntos.js) y viajes guardados aparte.
Usa los datos de assets/js/planificador-puntos.json (planificador_puntos.py).
"""
import json

import data_ruta as RT
from data_countries import C, REGION
from presupuesto_page import datos as datos_presupuesto
from site_common import esc, page, callout, bullets
from planificador_puntos import PISTAS
from pathlib import Path as _P
ZONAS = json.loads((_P(__file__).with_name("zonas_riesgo.json")).read_text(encoding="utf-8"))
import data_presupuesto as P
from precios_auto import aviso_fuente

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
               "h": f[7], "frec": f[8], "km_eu": f[12], "coche_ida": f[9], "coche_vuelta": f[10], "pax": f[11], "gas": f[13],
               "nota": f[14], "fuente": f[15]}
              for f in RT.FERRIES]
    return {"paises": paises, "fronteras": fronteras, "ferris": ferris, "ferry_pref": RT.FERRY_PREFERIDO,
            "salida": RT.SALIDA, "regreso": RT.REGRESO_PREVISTO, "ritmo_v": RT.RITMO_VISITA, "ritmo_t": RT.RITMO_TRANSITO, "zonas": ZONAS, "origen": RT.ORIGEN, "pistas": PISTAS, "bud": presupuesto(D, nombres)}


def presupuesto(D, nombres):
    """Precios del Planificador clásico (mismos valores y mismas claves de ajuste)."""
    bud = {"fecha": D["fecha"], "factor": D["factor"], "desvios": D["desvios"], "vehiculos": D["vehiculos"],
           "params": D["params"], "perro_ferry": D["perro_ferry"], "gas_sin_dato": P.GASOIL_SIN_DATO,
           "gas_eu": RT.GASOIL_EUROPA, "gpp_fecha": P.GPP_FECHA, "paises": {}}
    for s in nombres:
        g, v, t = P.GASOIL.get(s), P.VISADOS.get(s), P.TASAS.get(s)
        aviso = aviso_fuente(v[2]) if v else ""
        bud["paises"][s] = {
            "gas": g[0] if g else None, "gas_fuente": g[1] if g else "", "gas_fecha": g[2] if g else "", "gas_nota": g[3] if g else "",
            "vis": 0 if s in P.SIN_VISADO else (v[0] if v else None),
            "vis_txt": "Sin visado" if s in P.SIN_VISADO else (v[1] if v else "Sin importe localizado"),
            "vis_url": v[2] if v and s not in P.SIN_VISADO else "",
            **({"vis_aviso": aviso} if aviso and s not in P.SIN_VISADO else {}),
            "tasa": t[0] if t else 0, "tasa_txt": t[1] if t else "",
        }
    return bud


CSS = """
.pp-wrap{display:grid;grid-template-columns:minmax(0,1fr) clamp(400px,31vw,480px);gap:14px;align-items:start;margin:12px 0}
#pp-mapa{height:calc(100vh - 110px);min-height:460px;border-radius:12px;border:1px solid var(--line);background:var(--surface2)}
.pp-panel{min-width:0;overflow-x:hidden;position:sticky;top:60px;max-height:calc(100vh - 80px);overflow:auto;border:1px solid var(--line);border-radius:12px;background:var(--surface);font-family:"Archivo",sans-serif}
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
.pp-h{cursor:grab;color:var(--ink-soft);user-select:none;touch-action:none;padding:6px 4px;font-size:18px;line-height:1}.pp-h:hover{color:var(--ink)}.pp-it.sortable-chosen{background:var(--amber-bg)}.sortable-fallback{opacity:.9;box-shadow:0 6px 18px rgba(0,0,0,.25)}.pp-b[disabled]{opacity:.4;cursor:default}
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
.pp-avisos{list-style:none;margin:4px 0 0;padding:0;font-size:12.5px;max-height:320px;overflow:auto}
.pp-avdet{margin-top:8px}.pp-avdet>summary{cursor:pointer;list-style:none;display:flex;align-items:center;gap:8px;padding:6px 10px;border-radius:7px;background:var(--amber-bg);border-left:4px solid var(--amber);font-size:13px;font-weight:700}
.pp-avdet>summary::-webkit-details-marker{display:none}.pp-avdet>summary::after{content:'▾';margin-left:auto;transition:transform .15s}.pp-avdet[open]>summary::after{transform:rotate(180deg)}
.pp-avdet>summary .r{color:var(--red)}.pp-avdet.rojo>summary{background:var(--red-bg);border-left-color:var(--red)}
.pp-avisos li{padding:6px 9px;border-radius:7px;margin:5px 0;background:var(--amber-bg);color:var(--ink);border-left:4px solid var(--amber)}
.pp-avisos li.ir{cursor:pointer}.pp-avisos li.ir:hover,.pp-avisos li.ir:focus-visible{filter:brightness(1.08);outline:2px solid var(--teal);outline-offset:1px}
.pp-avisos li .ver{display:inline;margin-left:6px;white-space:nowrap;font-size:11.5px;font-weight:700;color:var(--link)}
.pp-avisos li.rojo{background:var(--red-bg);color:var(--ink);border-left-color:var(--red)}
.pp-avisos li.rojo strong{color:var(--red)}
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
.pp-mk.sel{background:#D6336C;border-width:3px;font-size:13px;box-shadow:0 0 0 5px rgba(214,51,108,.35),0 2px 6px rgba(0,0,0,.4)}
button.pp-n{border:0;padding:0;cursor:pointer;font-family:inherit}button.pp-n:hover{outline:2px solid #D6336C;outline-offset:1px}
.pp-it.sel{background:rgba(214,51,108,.10);box-shadow:inset 3px 0 0 #D6336C}.pp-it.sel .pp-n{background:#D6336C}
/* Sin el recuadro de foco del navegador al clicar un país o una zona: basta el cambio de color */
.leaflet-container path.leaflet-interactive:focus,.leaflet-container path.leaflet-interactive:focus-visible{outline:none}
.pp-buscar{position:relative;display:flex;gap:6px;margin:6px 0 10px;font-family:"Archivo",sans-serif;z-index:1001}
.pp-buscar input{flex:1;min-width:0;font:inherit;font-size:14px;padding:8px 10px;border:1px solid var(--line);border-radius:9px;background:var(--surface);color:var(--ink)}
.pp-buscar ul{position:absolute;top:100%;left:0;right:90px;margin:4px 0 0;padding:4px;list-style:none;background:var(--surface);border:1px solid var(--line);border-radius:9px;box-shadow:0 6px 18px rgba(0,0,0,.25);max-height:320px;overflow:auto}
.pp-buscar li button{display:block;width:100%;text-align:left;background:none;border:0;padding:7px 8px;border-radius:6px;color:var(--ink);font:inherit;font-size:13.5px;cursor:pointer}
.pp-buscar li button:hover,.pp-buscar li button:focus-visible{background:var(--line)}
.pp-buscar li small{display:block;color:var(--ink-soft);font-size:11.5px}
.pp-gpx{list-style:none;margin:6px 0 0;padding:0;font-size:13px}
.pp-gpx li{display:flex;gap:6px;align-items:center;border-left:4px solid #7B3FA0;padding:3px 0 3px 8px;margin:4px 0}
.pp-gpx li span{flex:1;min-width:0}.pp-gpx li small{display:block;color:var(--ink-soft)}
.pp-modo{font:inherit;font-size:11px;border:1px solid var(--line);border-radius:99px;padding:0 7px;margin-left:4px;background:transparent;color:var(--ink-soft);cursor:pointer}.pp-modo.paso{border-color:#D97B29;color:#D97B29;font-weight:700}
.pp-km{margin-left:6px;font-size:11px;color:var(--ink-soft);white-space:nowrap}
.pp-otra{display:block;margin-top:6px;font-size:12px;color:var(--ink-soft)}.pp-otra .pp-b{margin-left:4px}
.pp-recto{font-weight:700;color:#8B5A2B}.pp-recto.on{background:#8B5A2B;border-color:#8B5A2B;color:#fff}
.pp-mk4{width:14px;height:14px;background:#D4A017;border:2px solid #5C4300;transform:rotate(45deg);border-radius:2px;box-shadow:0 1px 2px rgba(0,0,0,.35)}
.pp-pop .pp-r4{font-size:12.5px;line-height:1.4;margin:4px 0}
.pp-vd{display:inline-block;border-left:4px solid #9AA4AA;padding:1px 0 1px 7px;margin:3px 0;font-size:12.5px;color:var(--ink,#1F2A30)}
.pp-fu a{display:block;font-size:12px;line-height:1.35;margin:2px 0;word-break:break-word}.pp-fu small{color:#5F6B72}
.pp-pop p{font-size:12.5px;line-height:1.4;margin:4px 0 6px}.pp-pop .pp-fu{margin:4px 0 6px;max-height:150px;overflow:auto}.pp-pop small{display:block;color:#5F6B72}
.pp-frt td{vertical-align:top;font-size:13px}.pp-frt td:nth-child(4){min-width:260px}.pp-frt td:nth-child(5){min-width:200px}
.pp-fr{width:12px;height:12px;background:#5F6B72;transform:rotate(45deg);border:2px solid #fff;box-shadow:0 1px 2px rgba(0,0,0,.4)}
.pp-puerto{font-size:18px;line-height:1}
.pp-ayuda{font-size:12.5px;color:var(--ink-soft);margin:0}
.pp-ayuda b{color:var(--ink)}
#pp-msg{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);background:var(--ink);color:var(--surface);padding:9px 14px;border-radius:10px;font:600 13px "Archivo",sans-serif;z-index:2000;max-width:90vw;box-shadow:0 4px 14px rgba(0,0,0,.25)}
.pp-it.sortable-ghost{opacity:.35}
.pp-mkp{width:20px;height:20px;border-radius:50%;background:#D97B29;color:#fff;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center;font-size:12px;line-height:1}
.pp-mkp.log{background:#1E88C7}
.pp-pop .pp-propio{display:inline-block;font-size:11px;font-weight:700;color:#9A6410;background:#FCF1DA;border-radius:99px;padding:1px 8px;margin-bottom:6px}
#pp-crear[aria-pressed="true"]{background:#D97B29;border-color:#D97B29;color:#fff}
.pp-kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px;margin:12px 0 0;font-family:"Archivo",sans-serif}
.pp-kpi{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:10px 13px;min-width:0}
.pp-kpi.alerta{border-color:var(--amber);background:var(--amber-bg)}
.pp-kpi .l{font-size:10.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--teal)}
.pp-kpi .v{font-size:24px;font-weight:800;color:var(--head);font-variant-numeric:tabular-nums;line-height:1.2;white-space:nowrap}
.pp-kpi .s{font-size:12px;color:var(--ink-soft);line-height:1.35}
.pp-kpi a{color:var(--teal);font-weight:700}
@media (max-width:640px){.pp-kpis{grid-template-columns:repeat(2,minmax(0,1fr))}.pp-kpi .v{font-size:20px}}
.pp-tiempo{margin:10px 0 0;font-family:"Archivo",sans-serif}
.pp-tiempo:empty{display:none}
.pp-tl{display:flex;height:34px;border-radius:9px;overflow:hidden;border:1px solid var(--line);background:var(--surface2)}
.pp-tl i{display:flex;align-items:center;justify-content:center;min-width:2px;height:100%;color:#fff;font-style:normal;font-size:11.5px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:clip;border-right:1px solid rgba(255,255,255,.55)}
.pp-tl i.fer{background:repeating-linear-gradient(45deg,#8A949A,#8A949A 5px,#9AA3A8 5px,#9AA3A8 10px)}
.pp-tiempo{position:relative}
.pp-tl i{cursor:default;transition:filter .1s}.pp-tl i.on{filter:brightness(1.18);box-shadow:inset 0 0 0 2px rgba(255,255,255,.8)}
.pp-tl-tip{position:absolute;z-index:500;min-width:170px;max-width:320px;background:var(--ink);color:var(--surface);border-radius:9px;padding:8px 11px;font-size:12.5px;line-height:1.45;box-shadow:0 6px 20px rgba(0,0,0,.3);pointer-events:none}
.pp-tl-tip strong{font-size:13.5px}
.pp-tl-ej{display:flex;justify-content:space-between;font-size:11.5px;color:var(--ink-soft);margin:3px 2px 0}
.pp-tiempo details{margin-top:6px}
.pp-tiempo summary{cursor:pointer;font-size:12.5px;font-weight:700;color:var(--teal)}
table.pp-tt{width:100%;border-collapse:collapse;font-size:13px;margin-top:6px;background:var(--surface);border:1px solid var(--line);border-radius:10px;overflow:hidden}
table.pp-tt th{font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-soft);text-align:left;padding:6px 9px;background:var(--surface2)}
table.pp-tt td{padding:6px 9px;border-top:1px solid var(--line)}
table.pp-tt td:first-child{white-space:nowrap}
table.pp-tt .n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
table.pp-tt i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;vertical-align:-1px}
.pp-evitar{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}
.pp-evitar>span{display:inline-flex;align-items:center;gap:4px;font-size:12.5px;border:1px dashed #2B2F33;border-radius:99px;padding:1px 3px 1px 9px}
.pp-evitar .pp-b{padding:1px 5px}
.pp-pop .pp-zona{display:inline-block;font-size:11px;font-weight:700;border-radius:99px;padding:1px 8px;margin:0 4px 6px 0}
.pp-pop .pp-zona.rojo{background:#F6E1E1;color:#B43A3A}.pp-pop .pp-zona.naranja{background:#FCE9D6;color:#B8560D}.pp-pop .pp-zona.guia{background:#E1EAF6;color:#2B6CB0}
.leaflet-tooltip.pp-tip{white-space:normal;width:max-content;min-width:min(170px,55vw);max-width:min(380px,70vw);font:13.5px/1.4 "Archivo",sans-serif;padding:6px 10px}
.leaflet-tooltip.pp-tip small{color:#5F6B72}
.pp-eur{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 10px;background:var(--surface2);border-radius:8px;padding:8px 10px;margin:0 0 8px}
.pp-eur b{font-size:22px;font-variant-numeric:tabular-nums;color:var(--head)}
.pp-eur span{font-size:12px;color:var(--ink-soft);flex:1}
.pp-eur a{font-size:12px;font-weight:700;color:var(--teal)}
.pp-chk{display:flex;gap:8px;align-items:flex-start;font-size:13px;cursor:pointer}
.pp-chk input{margin-top:2px;width:16px;height:16px;accent-color:#1E7A8A}
table.pp-comp{width:100%;table-layout:fixed;border-collapse:collapse;font-size:12.5px;font-variant-numeric:tabular-nums}
table.pp-comp th{font-size:10px;text-transform:uppercase;letter-spacing:.04em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:var(--ink-soft);text-align:right;font-weight:700;padding:3px 4px}
table.pp-comp td{text-align:right;padding:4px;white-space:nowrap;border-top:1px solid var(--line)}
table.pp-comp td:first-child,table.pp-comp th:first-child{text-align:left;width:26%}
table.pp-comp .mas{color:#B43A3A;font-weight:700}table.pp-comp .menos{color:#2E7D32;font-weight:700}table.pp-comp .ig{color:var(--ink-soft)}
.pp-bud{margin:26px 0 10px;font-family:"Archivo",sans-serif}
.pp-bud h2{margin:0 0 10px}
.pp-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}
.pp-card{border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:12px 14px}
.pp-card.tot{border-color:#1E7A8A}
.pp-card .lbl{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--teal)}
.pp-card .big{font-size:26px;font-weight:800;color:var(--head);font-variant-numeric:tabular-nums;line-height:1.2}
.pp-card .sub{font-size:12.5px;color:var(--ink-soft);margin-top:2px}
.pp-bars{display:flex;flex-direction:column;gap:6px;margin:16px 0}
.pp-bar{display:grid;grid-template-columns:minmax(120px,300px) 1fr 90px;gap:10px;align-items:center;font-size:13px}
.pp-bar .track{background:var(--surface2);border-radius:4px;height:13px;overflow:hidden}.pp-bar .track i{display:block;height:100%}
.pp-bar .v{text-align:right;font-variant-numeric:tabular-nums}
.pp-tw{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:var(--surface)}
table.pp-bt{width:100%;border-collapse:collapse;font-size:13.5px}
table.pp-bt th{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-soft);text-align:left;padding:8px 10px;background:var(--surface2)}
table.pp-bt td{padding:7px 10px;border-top:1px solid var(--line);vertical-align:top}
table.pp-bt .n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
table.pp-bt tr.eu td{color:var(--ink-soft);background:var(--surface2)}
table.pp-bt .nota{display:block;font-size:11.5px;color:var(--ink-soft)}table.pp-bt .nota.av{color:var(--amber);font-weight:600}
table.pp-bt small{color:var(--ink-soft)}
.pp-acc{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 6px}
.pp-det{margin:10px 0;border:1px solid var(--line);border-radius:12px;padding:8px 12px;background:var(--surface)}
.pp-det summary{cursor:pointer;font-weight:700;color:var(--head);font-size:14px}
.pp-det .pp-tw{margin-top:8px}
.pp-key{display:flex;gap:14px;font-size:12px;color:var(--ink-soft)}.pp-key i{display:inline-block;width:11px;height:11px;border-radius:2px;background:var(--ink-soft);margin-right:5px;vertical-align:-1px}
.pp-bar .track{display:flex}
table.pp-bt tr.tot td{background:var(--surface2);font-weight:600}
table.pp-bt a{color:var(--link)}
.pp-bud .callout{margin:12px 0}
#criterio ul{font-size:14px;line-height:1.5}
.pp-bud-h{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft);margin:22px 0 8px}
table.pp-bt input{font:inherit;font-size:13px;padding:3px 6px;border:1px solid var(--line);border-radius:6px;background:var(--surface);color:var(--ink);text-align:right}
table.pp-bt input.edited,.pp-veh input.edited{border-color:var(--amber);background:var(--amber-bg)}
.pp-veh label{display:flex;justify-content:space-between;align-items:center;gap:10px;font-size:13px;margin:6px 0}
.pp-veh input{font:inherit;font-size:13px;padding:3px 6px;border:1px solid var(--line);border-radius:6px;background:var(--surface);color:var(--ink);text-align:right}
@media (max-width:640px){.pp-bar{grid-template-columns:110px 1fr 78px;font-size:12px}}
@media (max-width:900px){.pp-wrap{grid-template-columns:1fr}#pp-mapa{height:68vh;min-height:360px}.pp-panel{position:static;max-height:none}}
"""


BUD_PERRO = P.PERRO_FERRY
CRITERIO = [
    "El viaje es la lista de puntos de la ida y de la vuelta, en ese orden. Entre dos puntos de países distintos se busca el camino de países más corto por fronteras abiertas; se prefieren los puestos por los que pasan los recorridos de las fichas. Los países en conflicto (Malí, Sudán, Libia, Burkina Faso, Níger, Chad, República Centroafricana, Sudán del Sur, Somalia) y los que marques como «evitar» solo se usan si no hay otro camino, siempre con aviso.",
    "Fronteras: solo se cambia de país por un puesto fronterizo oficial. Cada puesto está comprobado con fuentes (MAEC, FCDO, embajadas, Sahara Overland, iOverlander y crónicas de viajeros de 2024-2026): los cerrados no se usan; entre los abiertos se prefieren los que no tienen condiciones y se evitan los que no se han podido confirmar. Si la carretera que da el servidor de rutas sale del país sin pasar por un puesto, se prueba otra carretera y, si no hay, el tramo sale en rojo con aviso. Debajo, la tabla con cada paso y sus fuentes.",
    "Al añadir un punto se mete en el hueco de su mitad (ida o vuelta) donde menos km suma; «Ordenar por cercanía» rehace el orden de esa mitad. Se puede arrastrar cualquier punto, también de una mitad a la otra.",
    "Carretera: OSRM (OpenStreetMap), pedida al calcular y guardada en el navegador. Sin respuesta, línea recta × 1,25 (discontinua). Si el servidor da un rodeo de más del doble, se descarta y se avisa. Pistas que OpenStreetMap no enlaza (Hassi 75 – Zuérat) van dibujadas a mano con km aproximados.",
    "Km por país: la carretera se trocea y cada tramo cuenta en el país donde cae. Un roce de menos de 25 km sin paradas con otro país no cuenta como estancia.",
    "Días = km ÷ km de conducción al día + días de cada punto (los de su ficha, editables) + ferris y carretera en Europa, más el margen. Las fechas por país salen de ese mismo reloj.",
    "Ferris: el de ida es el recomendado para el país del primer punto (Marruecos: GNV Barcelona–Tánger Med; Argelia: Valencia–Mostaganem; Túnez: Génova–Túnez); si no tiene ferry, el del país con ferry más cercano. Igual con la vuelta y el último punto. Se pueden elegir a mano en el panel.",
    "Zonas desaconsejadas: avisos del FCDO británico (rojo = todo viaje desaconsejado; naranja = solo esenciales) y los campamentos saharauis de Tinduf que desaconseja el MAEC, con límites aproximados donde el aviso habla de comarcas o líneas entre pueblos. En azul, zonas donde hace falta guía, agencia o autorización: el Gran Sur argelino (agencia autorizada; guía obligatorio en el Tassili, el Tadrart y el Hoggar) y en Túnez el Sáhara militar (autorización previa), el desierto al sur de Douz (guía) y la Mesa de Yugurta. Revisar siempre el MAEC antes de cada frontera.",
    "Los gastos compartidos no se reparten: cada vehículo paga su combustible, sus visados, su CPD, sus tasas, su ferry y la comida de quienes viajan en él. El perro va en el INEOS Grenadier.",
    "Tipo de cambio: 1 USD = %s € (%s). Franco CFA fijo: 655,957 por euro. El gasóleo y el cambio se actualizan solos cada semana; si la página oficial de un visado cambia, su fila lo avisa hasta que se revisa." % (str(P.USD_EUR).replace(".", ","), P.USD_EUR_FUENTE),
    "No incluye: el viaje hasta Barcelona, la preparación de los vehículos, vacunas y seguro médico de viaje, ni una posible escapada en avión.",
    "Todo lo que cambies se guarda solo en este navegador («Descargar» en Mis viajes para llevarlo a otro). El Planificador clásico (por países) sigue disponible con sus viajes.",
]


V_TXT = {"abierta": ("abierto", "#2E7D32"), "abierta_condiciones": ("con condiciones", "#C47F17"),
         "sin_confirmar": ("sin confirmar", "#8A6BB0"), "cerrada": ("cerrado", "#B43A3A")}


def tabla_fronteras():
    """Pasos fronterizos comprobados con fuentes (tools/gen/fronteras_verificadas.json)."""
    ver = json.loads((_P(__file__).with_name("fronteras_verificadas.json")).read_text(encoding="utf-8"))
    nom = lambda s: C[s]["name"] if s in C else s.replace("-", " ").capitalize()
    pasos = sorted(ver["pasos"], key=lambda v: (["cerrada", "sin_confirmar", "abierta_condiciones", "abierta"].index(v["veredicto"]), v["par"]))
    cuenta = {k: sum(1 for v in pasos if v["veredicto"] == k) for k in V_TXT}
    filas = []
    for v in pasos:
        par = " – ".join(nom(x) for x in v["par"].split("|")) if "|" in v["par"] else esc(v["par"])
        t, col = V_TXT[v["veredicto"]]
        fu = "".join(f'<a href="{esc(x["url"])}" target="_blank" rel="noopener">{esc(x.get("titulo") or x["url"])}</a>'
                     + (f' <small>({esc(x["fecha"])})</small>' if x.get("fecha") else "") for x in v.get("fuentes", []) if x.get("url"))
        filas.append(f'<tr data-v="{v["veredicto"]}"><td>{esc(par)}</td><td>{esc(v["paso"])}</td>'
                     f'<td><span class="pp-vd" style="border-left-color:{col}"><b>{t}</b></span></td>'
                     f'<td>{esc(v["resumen"])}</td><td class="pp-fu">{fu}</td></tr>')
    resumen = " · ".join(f'<span class="pp-vd" style="border-left-color:{V_TXT[k][1]}"><b>{cuenta[k]}</b> {V_TXT[k][0]}</span>' for k in V_TXT)
    return f"""<section id="fronteras" class="pp-bud">
  <h2>Pasos fronterizos comprobados</h2>
  <p class="pp-ayuda">Comprobados el {esc(ver["verificado"])}, cada uno con sus fuentes. {resumen}. El planificador no usa los cerrados, evita los que no se han podido confirmar y avisa de las condiciones de los demás. En el mapa, «Ver puestos fronterizos» los pinta con el mismo color; al hacer clic en uno salen su resumen y sus fuentes. Revisar el MAEC antes de cada frontera: esto cambia.</p>
  <details class="pp-det"><summary>Ver los {len(pasos)} pasos con sus fuentes</summary>
  <div class="pp-tw"><table class="pp-bt pp-frt"><thead><tr><th>Países</th><th>Paso</th><th>Estado</th><th>Qué dicen las fuentes</th><th>Fuentes</th></tr></thead>
  <tbody>{"".join(filas)}</tbody></table></div></details>
</section>"""


def render(FULL, navbar, VERSION):
    root = "../"
    nav = navbar(root, [("Portal", root), ("Mapa", root + "mapa/"), ("Documentación", root + "documentacion/"),
                        ("Visados", root + "visados/"), ("CPD", root + "cpd/"), ("El perro", root + "perro/"),
                        ("Presupuesto", "#pp-bud"), ("Criterio", "#criterio"), ("Fronteras", "#fronteras"), ("Clásico", root + "planificador-clasico/")], "Planificador")
    cfg = config(FULL)
    body = f"""{nav}
<main style="max-width:1500px">
<h2 style="margin-top:16px">Planificador</h2>
<p class="pp-ayuda"><b>1.</b> Toca un país para ver sus puntos de interés. <b>2.</b> Toca un punto y añádelo a la <b style="color:#1E7A8A">ida</b> o a la <b style="color:#C47F17">vuelta</b>. <b>3.</b> Ordena arrastrando en la lista. La carretera, las fronteras, los km y los días salen solos. Clic derecho (o mantener pulsado) en cualquier sitio del mapa = «pasar por aquí». <b>〰</b> en un punto de la lista = llegar a él por pista, en línea recta, sin buscar carretera (con varios «pasar por aquí» marcados así se dibuja la pista a mano). <button type="button" class="pp-b" id="pp-crear" aria-pressed="false">★ Crear un punto</button> para añadir un sitio tuyo (PDI, agua, camping, taller…): la app completa sola fotos, enlaces, servicios y clima. Todo se guarda en este navegador y funciona sin conexión.</p>
<form class="pp-buscar" id="pp-buscar" autocomplete="off" role="search">
  <input type="search" id="pp-buscar-q" placeholder="Busca un lugar (como en Google Maps) o pega coordenadas GPS o un enlace de Google Maps: 31.0802, -4.0133" aria-label="Buscar un lugar o unas coordenadas" data-1p-ignore data-lpignore="true">
  <button type="submit" class="pp-b ida">Buscar</button>
  <ul id="pp-buscar-res" hidden></ul>
</form>
<div class="pp-kpis" id="pp-kpis" aria-live="polite"></div>
<div class="pp-tiempo" id="pp-tiempo"></div>
<div class="pp-wrap">
  <div id="pp-mapa" role="application" aria-label="Mapa: toca países y puntos para montar el viaje"></div>
  <aside class="pp-panel" aria-label="Viaje">
    <div class="pp-sec">
      <h3>Tu viaje <span class="cnt" id="pp-nombre"></span></h3>
      <div class="pp-sum"><div><b id="pp-km">0</b><span>km</span></div><div><b id="pp-dias">0</b><span>días</span></div><div><b id="pp-np">0</b><span>países</span></div></div>
      <div class="pp-eur"><b id="pp-total">—</b><span id="pp-total-sub"></span><a href="#pp-bud">Ver el desglose</a></div>
      <div class="pp-tira" id="pp-tira" aria-hidden="true"></div>
      <div id="pp-fechas" style="font-size:12.5px;color:var(--ink-soft)"></div>
      <div class="pp-paises" id="pp-paises"></div>
      <details class="pp-avdet" id="pp-avdet" hidden><summary id="pp-avsum">Avisos</summary><ul class="pp-avisos" id="pp-avisos"></ul></details>
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
      <h3>En la web</h3>
      <label class="pp-chk"><input type="checkbox" id="pp-web"> Usar este viaje en el mapa general, el portal y las fichas</label>
      <p class="pp-ayuda" id="pp-web-txt" style="margin-top:4px"></p>
      <h3 style="margin-top:14px">Comparar con el Planificador clásico</h3>
      <div id="pp-comp"></div>
    </div>
    <div class="pp-sec">
      <h3>Ajustes</h3>
      <div class="pp-row"><label>Salida de {esc(cfg['origen'])} <input type="date" id="pp-salida"></label></div>
      <div class="pp-row"><label title="Tramos en los que se va parando y visitando">Km/día en tramos de visita <input type="number" id="pp-kmdia" min="50" step="10" style="width:70px"></label><label title="Tramos para avanzar: el tramo que llega a un punto marcado «de paso», y la carretera por Europa hasta el ferry">Km/día en tramos de paso <input type="number" id="pp-kmdiat" min="50" step="10" style="width:70px"></label><label>Margen % <input type="number" id="pp-margen" min="0" step="1" style="width:56px"></label></div>
      <div class="pp-row"><label><input type="checkbox" id="pp-verfr"> Ver puestos fronterizos</label><label><input type="checkbox" id="pp-vertodos"> Ver puntos de todos los países</label><label><input type="checkbox" id="pp-verzonas" checked> Ver zonas desaconsejadas y con guía obligatoria</label><label><input type="checkbox" id="pp-ver4x4" checked> Ver puntos 4x4</label><label><input type="checkbox" id="pp-verr4" checked> Ver rutas 4x4</label></div>
      <div class="pp-row"><label class="full">Países a evitar en la ruta <select id="pp-evitar-add"></select></label></div>
      <div class="pp-evitar" id="pp-evitar"></div>
    </div>
    <div class="pp-sec">
      <h3>Rutas GPX <span class="cnt" id="pp-gpx-n"></span></h3>
      <p class="pp-ayuda" style="margin:0 0 6px">Baja el GPX de Wikiloc (o de otra fuente) con tu cuenta e impórtalo: se dibuja en morado con sus km, los países y las zonas que cruza, y puedes meterlo en el viaje. Se queda solo en este navegador.</p>
      <div class="pp-row"><label class="pp-b" style="cursor:pointer">Importar GPX<input type="file" id="pp-gpx-in" accept=".gpx,application/gpx+xml" multiple hidden></label></div>
      <ul class="pp-gpx" id="pp-gpx"></ul>
    </div>
    <div class="pp-sec">
      <h3>Mis viajes</h3>
      <div class="pp-row"><select id="pp-viajes" style="flex:1"></select><button type="button" class="pp-b" id="pp-cargar">Cargar</button><button type="button" class="pp-b x" id="pp-borrar">Borrar</button></div>
      <div class="pp-row" id="pp-gact" hidden></div>
      <div class="pp-row"><input type="text" id="pp-vnombre" placeholder="Nombre del viaje" style="flex:1" autocomplete="off" data-1p-ignore data-lpignore="true"><button type="button" class="pp-b ida" id="pp-guardar">Guardar</button></div>
      <p class="pp-ayuda" style="margin:2px 0 0">El viaje en el que trabajas se guarda solo en este navegador, aunque cierres la página. «Guardar» lo copia a «Mis viajes» para poder volver a él.</p>
      <div class="pp-row"><button type="button" class="pp-b" id="pp-nuevo">Empezar de cero</button><button type="button" class="pp-b" id="pp-exportar">Descargar</button><button type="button" class="pp-b" id="pp-traer" title="Convierte el último viaje calculado en el Planificador clásico en un viaje por puntos">Traer el viaje del Planificador clásico</button><label class="pp-b" style="cursor:pointer">Importar<input type="file" id="pp-importar" accept=".json,application/json" hidden></label></div>
    </div>
  </aside>
</div>
<section id="pp-bud" class="pp-bud" hidden aria-labelledby="pp-bud-t">
  <h2 id="pp-bud-t">Presupuesto del viaje</h2>
  <div class="pp-cards" id="pp-bud-cards"></div>
  <div class="pp-bars" id="pp-bud-barras"></div>
  <div class="pp-tw"><table class="pp-bt"><thead id="pp-bud-res-h"></thead><tbody id="pp-bud-res"></tbody></table></div>
  <div class="pp-acc"><button type="button" class="pp-b big ida" id="pp-xlsx">Descargar la hoja de cálculo (.xlsx, con fórmulas)</button><button type="button" class="pp-b big" id="pp-csv">Solo el resumen (CSV)</button><button type="button" class="pp-b big x" id="pp-reset">Volver a todos los valores iniciales</button></div>
  <p class="pp-ayuda">La hoja lleva el viaje y los valores que tengas ahora: Resumen, Parámetros, Ruta (una fila por estancia en cada país), Visados y Tasas frontera. Las casillas amarillas son datos y el resto fórmulas: al cambiar un dato en Excel, Numbers o Google Sheets se recalcula todo.</p>
  {callout("warn", "Qué es dato y qué es estimación",
    "Combustible, visados, CPD, tasas de frontera y ferris salen de fuentes citadas. Los km son por carretera (OSRM, OpenStreetMap) entre los puntos del viaje; sin respuesta del servidor, línea recta × 1,25. "
    "Comida, noches, parques, seguros, mantenimiento, trámites del perro, imprevistos, los <strong>km de conducción al día</strong> y los días de cada punto son <strong>estimaciones</strong>: hay que ajustarlas.", raw=True)}

  <h3 class="pp-bud-h" id="combustible">Combustible, visados y tasas por país</h3>
  <p class="pp-ayuda">Km de cada país (todas las veces que se pasa) × factor × (1 + desvíos); son los mismos para los dos vehículos. Visados: uno por persona y por estancia; si sacáis uno de entradas múltiples, escribe 1 en «Visados». Tasas de importación temporal: por vehículo y por estancia. Las casillas se pueden corregir (en ámbar las cambiadas).</p>
  <div class="pp-tw"><table class="pp-bt pp-paises-t"><thead><tr><th>País</th><th class="n">Km</th><th class="n">Días</th><th class="n">€/litro</th><th class="n">Combustible</th><th class="n">€ visado</th><th class="n">Visados</th><th class="n">Visados / persona</th><th class="n">Tasa / estancia</th><th class="n">Tasas / vehículo</th></tr></thead>
  <tbody id="pp-bud-paises"></tbody><tfoot id="pp-bud-paises-f"></tfoot></table></div>
  <p class="pp-ayuda" id="pp-bud-gasnota"></p>

  <h3 class="pp-bud-h" id="ferris">Ferris</h3>
  <p class="pp-ayuda">El de ida y el de vuelta se eligen en el panel (automáticos según el primer y el último punto). Precio por vehículo y trayecto = coche con conductor + un pasaje por cada persona más; corrígelo con el presupuesto real de la naviera.</p>
  <div class="pp-tw"><table class="pp-bt"><thead id="pp-bud-fer-h"></thead><tbody id="pp-bud-fer"></tbody></table></div>
  <details class="pp-det"><summary>Todos los ferris a Marruecos, Argelia y Túnez</summary>
  <div class="pp-tw"><table class="pp-bt"><thead><tr><th>Ruta</th><th class="n">Horas</th><th>Frecuencia</th><th class="n">Km desde {esc(cfg['origen'])}</th><th class="n">Coche + conductor ida / vuelta</th><th class="n">Pasaje</th></tr></thead><tbody id="pp-bud-fer-todos"></tbody></table></div></details>
  {callout("warn", "Ferris: lo que no está confirmado",
    "Solo Barcelona–Tánger Med (GNV) es un presupuesto real para nuestros vehículos (clase A2, camarote). El resto son tarifas de coche con conductor de agregadores o «desde» de la naviera: "
    "<strong>no incluyen camarote ni el recargo de vehículo alto</strong> (el 4x4 con tienda mide ~2,3 m y casi todas las navieras lo cobran aparte). "
    "La vuelta en julio o agosto es temporada de la diáspora en Argelia y Túnez y puede multiplicar el precio. "
    f"<strong>Perro:</strong> ~{BUD_PERRO} € por trayecto (estimación); Algérie Ferries y Corsica Linea solo lo admiten en perrera.", raw=True)}

  <h3 class="pp-bud-h" id="gastos">Comida, noches, comunicaciones y otros gastos</h3>
  <div class="pp-tw"><table class="pp-bt"><thead><tr><th>Concepto</th><th class="n">Valor</th><th>Unidad y cálculo</th><th class="n">Total</th></tr></thead>
  <tbody id="pp-bud-gastos"></tbody></table></div>

  <h3 class="pp-bud-h" id="vehiculos">Vehículos y cálculo de km</h3>
  <div class="pp-cards pp-veh" id="pp-bud-veh"></div>
  {callout("", "CPD (carnet de 25 hojas, RACE)", "El carnet entra en el presupuesto; los costes bancarios del aval valen 0 hasta que se sepan. Los avales quedan inmovilizados y no cuentan como gasto: se recuperan al devolver los carnets con todos los sellos.", raw=True)}
  <p class="pp-ayuda" id="pp-bud-pie" style="margin-top:8px"></p>
</section>
<section id="criterio" class="pp-bud">
  <h2>Criterio</h2>
  {bullets(CRITERIO)}
</section>
{tabla_fronteras()}
<div id="pp-msg" role="status" aria-live="polite" hidden></div>
<footer>ÁFRICA 2027 · Planificador · <a href="{root}planificador-clasico/">Planificador clásico</a></footer>
</main>
<script>var A27_PP = {json.dumps(cfg, ensure_ascii=False, separators=(",", ":"))};</script>
<script src="{root}assets/vendor/leaflet.js"></script>
<script src="{root}assets/vendor/Sortable.min.js"></script>
<script src="{root}assets/js/map.js"></script>
<script src="{root}assets/js/creador-pdi.js"></script>
<script src="{root}assets/js/fotos-4x4.js"></script>
<script src="{root}assets/js/presupuesto-xlsx.js"></script>
<script src="{root}assets/js/{JS}"></script>"""
    extra = f'<link rel="stylesheet" href="{root}assets/vendor/leaflet.css"><style>{CSS}</style>'
    return page(root, "Planificador · África 2027", body, extra_head=extra)

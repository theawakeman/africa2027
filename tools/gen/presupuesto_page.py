# -*- coding: utf-8 -*-
"""Página /planificador/ (antes /presupuesto/): planificador de ruta + calculadora de presupuesto por
vehículo (funciona sin conexión).

Se marcan los países y la página rehace sola el orden, los países de tránsito
obligatorio, los km por vehículo, los días, la fecha de regreso y el dinero.
"""
import json
import math

import data_presupuesto as P
import data_ruta as RT
from data_visados import VISADOS as VIS_INFO
from data_countries import REGIONES, REGION
from recorridos import descripcion
from site_common import esc, attr, page, callout, bullets

JS_PATH = "presupuesto.js"


def _r(p):
    return [round(p[0], 3), round(p[1], 3)]


def _opts(slug, d, FULL):
    """Recorridos posibles de un país: [{id, l, km, aprox, pts}]."""
    out = []
    propios = RT.RECORRIDOS_PROPIOS.get(slug)
    if propios:
        for oid, label, clave in propios:
            if isinstance(clave, list):
                pts = clave
            elif clave == "A+B":
                pts = (d.get("corridor") or []) + (d.get("corridor_alt") or [])[1:]
            elif clave.startswith("ex:"):
                _, pais, i = clave.split(":")
                ex = [e for e in FULL[pais].get("extra_corridors", []) if isinstance(e, dict) and e.get("pts")]
                pts = ex[int(i)]["pts"]
            else:
                pts = d.get("corridor" if clave == "A" else "corridor_alt") or []
            out.append((oid, label, pts))
    else:
        if len(d.get("corridor") or []) >= 2:
            out.append(("A", descripcion(slug, "corridor", d.get("corridor_label", "")) or "Recorrido A", d["corridor"]))
        if len(d.get("corridor_alt") or []) >= 2 and f"{slug}:B" in RT.KM:
            out.append(("B", descripcion(slug, "corridor_alt", d.get("corridor_alt_label", "")) or "Recorrido B", d["corridor_alt"]))
    res = []
    for oid, label, pts in out:
        k = f"{slug}:{oid}"
        res.append({"id": oid, "l": label.replace("BAJADA · ", "").replace("SUBIDA · ", ""),
                    "km": RT.KM.get(k), "aprox": k in RT.KM_APROX, "pts": [_r(p) for p in pts]})
    return [o for o in res if o["km"]]


def datos(FULL, C):
    info = {c[0]: c for c in C}
    orden_c = [c[0] for c in sorted(C, key=lambda c: c[3])]
    slugs = [s for s in orden_c if s not in RT.ISLAS and s in FULL]
    slugs.insert(slugs.index("angola"), "cabinda")
    paises = {}
    for s in slugs:
        if s == "cabinda":
            nombre, grupo, seg, nota = "Cabinda (Angola)", "bajada", info["angola"][4], "Enclave angoleño entre Congo y RD Congo: solo de paso."
            opts = _opts(s, {}, FULL)
        else:
            _, nombre, grupo, _, seg, _, _, _, _, nota = info[s]
            opts = _opts(s, FULL[s], FULL)
        if not opts:
            continue
        todos = [p for o in opts for p in o["pts"]]
        pos = [round(sum(p[0] for p in todos) / len(todos), 3), round(sum(p[1] for p in todos) / len(todos), 3)]
        g = P.GASOIL.get("angola" if s == "cabinda" else s)
        vis = P.VISADOS.get(s)
        tasa = P.TASAS.get(s)
        nivel = (VIS_INFO.get(s) or {}).get("nivel", "")
        paises[s] = {
            "n": nombre, "g": grupo, "seg": seg, "nota": nota, "opts": opts, "pos": pos,
            "plan": RT.PLAN.get(s, opts[0]["id"]), "tr": RT.TRANSITO_FIJO.get(s, ""), "via": RT.VIA.get(s, {}),
            "gas": ({"eur": g[0], "fuente": g[1], "fecha": g[2], "nota": g[3]} if g else None),
            "vis": ("sin" if s in P.SIN_VISADO else ({"eur": vis[0], "txt": vis[1], "url": vis[2]} if vis else None)),
            "tasa": ({"eur": tasa[0], "txt": tasa[1]} if tasa else None),
            "r": REGION.get("angola" if s == "cabinda" else s, ""),
            "ex": s in RT.EXCLUIDOS, "cf": s in RT.CONFLICTO, "nivel": nivel,
            "solo_paso": s == "cabinda",
        }
    ruta = {
        "paises": paises,
        "fronteras": [f for f in RT.FRONTERAS if f[0] in paises and f[1] in paises],
        "orden_plan": RT.ORDEN_PLAN, "sel_plan": ["marruecos"] + RT.ORDEN_PLAN,
        "tanger": list(RT.TANGER_MED), "f_sin_ruta": RT.FACTOR_SIN_RUTA,
        "penal": RT.PENAL_NO_MARCADO, "penal_ferry": RT.PENAL_FERRY_KM,
        "salida": RT.SALIDA, "regreso": RT.REGRESO_PREVISTO, "ritmo_v": RT.RITMO_VISITA,
        "ritmo_t": RT.RITMO_TRANSITO, "margen": RT.MARGEN_PCT,
        "origen": RT.ORIGEN, "gas_eu": RT.GASOIL_EUROPA, "ferry_pref": RT.FERRY_PREFERIDO,
        "ferries": [{"id": f[0], "pais": f[1], "origen": f[2], "puerto": f[3], "pos": [f[4], f[5]], "naviera": f[6],
                     "h": f[7], "frec": f[8], "coche_ida": f[9], "coche_vuelta": f[10], "pax": f[11], "km_eu": f[12],
                     "gas": f[13], "nota": f[14], "fuente": f[15]} for f in RT.FERRIES],
        "gas_sin_dato": P.GASOIL_SIN_DATO,
        "grupos": [(r, l) for r, l, _ in REGIONES],
    }
    params = [{"id": a, "label": b, "val": c, "unidad": d, "ambito": e, "tipo": f, "nota": g}
              for a, b, c, d, e, f, g in P.PARAMETROS]
    return {
        "fecha": P.FECHA, "factor": P.FACTOR_CARRETERA, "desvios": P.DESVIOS_PCT,
        "vehiculos": P.VEHICULOS, "params": params, "ferry": P.FERRY, "perro_ferry": P.PERRO_FERRY,
        "ruta": ruta,
    }


CSS = """
.bud-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin:18px 0}
.bud-card{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.bud-card .lbl{font-family:"Archivo",sans-serif;font-size:11px;font-weight:700;letter-spacing:.14em;color:var(--teal);text-transform:uppercase}
.bud-card .big{font-family:"Archivo",sans-serif;font-size:28px;font-weight:800;color:var(--head);font-variant-numeric:tabular-nums;line-height:1.15}
.bud-card .sub{font-family:"Archivo",sans-serif;font-size:12.5px;color:var(--ink-soft)}
.bud-card.alerta{border-color:var(--amber);background:var(--amber-bg)}
.bud-bars{display:flex;flex-direction:column;gap:7px;margin:10px 0 4px}
.bud-bar{display:grid;grid-template-columns:minmax(120px,190px) 1fr auto;gap:10px;align-items:center;font-family:"Archivo",sans-serif;font-size:13px}
.bud-bar .track{background:var(--surface2);border-radius:4px;height:14px;overflow:hidden;display:flex}
.bud-bar .track i{display:block;height:100%}
.bud-bar .v{font-variant-numeric:tabular-nums;min-width:74px;text-align:right}
.bud-key{display:flex;gap:14px;flex-wrap:wrap;font-family:"Archivo",sans-serif;font-size:12.5px;color:var(--ink-soft);margin:6px 0 0}
.bud-key i{display:inline-block;width:11px;height:11px;border-radius:2px;margin-right:5px;vertical-align:-1px}
.bud input[type=number],.bud input[type=date],.bud select{font:inherit;font-family:"Archivo",sans-serif;font-size:13.5px;padding:3px 6px;border:1px solid var(--line);border-radius:6px;background:var(--surface);color:var(--ink);font-variant-numeric:tabular-nums}
.bud input[type=number]{width:84px}
.bud select{max-width:520px;width:100%}
.bud input.edited,.bud select.edited{border-color:var(--amber);background:var(--amber-bg)}
.bud input[type=checkbox]{width:17px;height:17px;accent-color:var(--teal)}
.bud td.n,.bud th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.bud tr.bud-aval td{background:var(--amber-bg);font-style:italic}
.bud tr.transito td{color:var(--ink-soft)}
.bud tr.transito td strong{font-weight:600}
.bud tfoot td{font-weight:700;font-family:"Archivo",sans-serif;background:var(--surface2)}
.bud .nota{display:block;font-size:12.5px;color:var(--ink-soft);line-height:1.4;margin-top:2px}
.bud .tag{font-family:"Archivo",sans-serif;font-size:10.5px;font-weight:700;letter-spacing:.06em;padding:1px 6px;border-radius:4px;white-space:nowrap}
.bud .tag.est{background:var(--amber-bg);color:var(--amber)}
.bud .tag.dat{background:var(--green-bg);color:var(--green)}
.bud .tag.tr{background:var(--surface2);color:var(--ink-soft)}
.bud .tag.vi{background:var(--teal);color:#fff}
.bud-veh{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
.bud-veh .bud-card label,.bud-cfg label{display:grid;grid-template-columns:minmax(0,1fr) 120px;align-items:center;gap:10px;font-family:"Archivo",sans-serif;font-size:13.5px;margin:6px 0}
.bud-veh .bud-card label input,.bud-cfg label input{width:100%;justify-self:end}
.bud-cfg{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:4px 24px;margin:10px 0}
.bud input::-webkit-contacts-auto-fill-button,.bud input::-webkit-credentials-auto-fill-button,.bud input::-webkit-strong-password-auto-fill-button{visibility:hidden;display:none!important;pointer-events:none;position:absolute;right:0}
.bud-actions{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}
.bud-actions button,.bud .mv{font-family:"Archivo",sans-serif;font-weight:600;font-size:13px;padding:8px 14px;border-radius:8px;border:1px solid var(--line);background:var(--surface);color:var(--ink);cursor:pointer}
.bud .mv{padding:2px 8px;font-size:12px;line-height:1.4}
.bud .mv:disabled{opacity:.3;cursor:default}
.bud td.mvs{white-space:nowrap}
.bud .rec{margin-top:6px}
.bud #bud-itin input[type=number]{width:70px}
.bud-actions button.primary{background:var(--teal);border-color:var(--teal);color:#fff}
.bud-paises{display:flex;flex-direction:column;gap:12px;margin:12px 0}
.bud-paises .gr{font-family:"Archivo",sans-serif;font-size:11px;font-weight:700;letter-spacing:.12em;color:var(--teal);text-transform:uppercase;margin-bottom:6px}
.bud-paises .bud-chips{display:flex;flex-wrap:wrap;gap:6px}
.bud-chip{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);border-radius:999px;padding:4px 11px 4px 7px;font-family:"Archivo",sans-serif;font-size:13px;background:var(--surface);cursor:pointer;user-select:none}
.bud-chip input{margin:0;width:15px!important;height:15px!important}
.bud-chip.on{border-color:var(--teal);background:var(--teal-bg,rgba(30,122,138,.10))}
.bud-chip.paso{border-style:dashed}
.bud-chip.cf{border-color:#B43A3A}
.bud-chip.ex{opacity:.45;cursor:not-allowed}
.bud-chip small{font-size:10.5px;color:var(--ink-soft)}
.bud-viajes{border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:12px 14px;margin:6px 0 16px;font-family:"Archivo",sans-serif}
.bv-row{display:grid;grid-template-columns:110px minmax(0,1fr) auto auto;gap:8px;align-items:center;margin:4px 0}
.bv-row:nth-child(2){grid-template-columns:110px minmax(0,1fr) auto}
.bv-l{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--teal)}
.bud-viajes select,.bud-viajes input[type=text]{width:100%;max-width:none;font:inherit;font-size:14px;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink)}
.bud-viajes button{font-family:"Archivo",sans-serif;font-weight:600;font-size:13px;padding:8px 14px;border-radius:8px;border:1px solid var(--line);background:var(--surface);color:var(--ink);cursor:pointer;white-space:nowrap}
.bud-viajes button.primary{background:var(--teal);border-color:var(--teal);color:#fff}
.bv-pie{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;font-size:13px;color:var(--ink-soft);margin-top:6px}
.bud-viajes .lnk{background:none;border:0;padding:0;color:var(--teal);text-decoration:underline;cursor:pointer;font-weight:600;font-size:13px}
@media (max-width:640px){.bv-row,.bv-row:nth-child(2){grid-template-columns:1fr 1fr}.bv-l{grid-column:1/-1}.bv-row select,.bv-row input[type=text],.bv-row:nth-child(2) button{grid-column:1/-1}}
.bud-mapkey{display:flex;flex-wrap:wrap;gap:14px;font-family:"Archivo",sans-serif;font-size:12.5px;color:var(--ink-soft);margin:6px 0 0}
.bud-mapkey i{display:inline-block;width:14px;height:14px;border-radius:3px;margin-right:6px;vertical-align:-2px}
#bud-mapa .leaflet-interactive{cursor:pointer}
.bud-actions select{max-width:320px;width:auto;padding:8px 10px;border-radius:8px;font-weight:600}
.bud-msg{background:var(--amber-bg);border:1px solid var(--amber);border-radius:10px;padding:10px 14px;font-size:14.5px;margin:8px 0}
.bud-itin{list-style:none;margin:10px 0 0;padding:0;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--surface)}
.bud-itin .it{display:grid;grid-template-columns:16px 30px minmax(0,1fr) auto 92px 104px 104px;gap:10px;align-items:center;padding:9px 12px;border-top:1px solid var(--line);font-family:"Archivo",sans-serif}
.bud-itin .it:first-child{border-top:0}
.bud-itin .it.cruza{background:var(--surface2)}
.bud-itin .it.cruza .it-p strong{font-weight:600;color:var(--ink-soft)}
.it-n{display:inline-block;min-width:26px;height:26px;line-height:26px;border-radius:13px;text-align:center;font-size:12px;font-weight:700;background:var(--line);color:var(--ink)}
.it.para .it-n{background:#1E7A8A;color:#fff}
.it-p{font-size:14.5px;min-width:0}
.it-dir{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--teal);margin-left:4px}
.it-p .nota{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;background:var(--surface)}
.seg button{font:600 13px "Archivo",sans-serif;padding:6px 13px;border:0;background:transparent;color:var(--ink-soft);cursor:pointer}
.seg button[aria-pressed="true"]{background:#1E7A8A;color:#fff}
.seg button[data-modo$="|c"][aria-pressed="true"]{background:#C47F17}
.seg-fijo{font-size:12.5px;color:var(--ink-soft)}
.it-km{text-align:right;font-variant-numeric:tabular-nums;font-size:14px;white-space:nowrap}
.it-km small,.it-d small{color:var(--ink-soft);font-size:11.5px}
.it-d{white-space:nowrap;text-align:right}
.bud .it-d input[type=number]{width:62px}
.it-act{display:flex;gap:4px;justify-content:flex-end}
.bud .mv.x{color:#B43A3A;font-weight:700}
.bud-itin-tot{display:flex;gap:18px;flex-wrap:wrap;justify-content:flex-end;font-family:"Archivo",sans-serif;font-size:14px;padding:10px 12px}
.it-h{cursor:grab;color:var(--ink-soft);font-size:18px;line-height:1;user-select:none;touch-action:none;text-align:center}
.it-h.vacio{cursor:default}
.it-ghost{opacity:.4;background:var(--amber-bg)!important}
.bud-ferry-card{display:grid;grid-template-columns:30px minmax(0,1fr) minmax(220px,340px);gap:10px;align-items:center;border:1px solid var(--line);border-radius:12px;padding:10px 12px;margin:8px 0;background:var(--surface2);font-family:"Archivo",sans-serif;font-size:14px}
.fer-ic{font-size:20px;text-align:center}
.fer-sel select{width:100%;max-width:none}
.bud .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
@media (max-width:760px){.bud-ferry-card{grid-template-columns:30px minmax(0,1fr)}.fer-sel{grid-column:1/-1}}
.bud-det{margin:14px 0;border:1px solid var(--line);border-radius:12px;padding:10px 14px;background:var(--surface)}
.bud-det summary{cursor:pointer;font-family:"Archivo",sans-serif;font-weight:700;color:var(--head)}
@media (max-width:760px){.bud-itin .it{grid-template-columns:16px 30px minmax(0,1fr) auto;grid-template-areas:"h n p act" "h n seg seg" "h n km d";row-gap:8px}
 .it-h{grid-area:h;align-self:center}.it-n{grid-area:n;align-self:start}.it-p{grid-area:p}.it-seg{grid-area:seg}.it-km{grid-area:km;text-align:left}.it-d{grid-area:d}.it-act{grid-area:act}
 .it-p .nota{white-space:normal}}
#bud-mapa{height:calc(100vh - 120px);min-height:420px;width:min(1400px,calc(100vw - 32px));margin:12px 0 12px calc(50% - min(700px,50vw - 16px));border-radius:12px;border:1px solid var(--line);background:var(--surface2)}
.bud-avisos{margin:10px 0;padding-left:20px;font-size:14px}
.bud-avisos li{margin:3px 0}
.bud-num{display:inline-block;min-width:22px;height:22px;line-height:22px;border-radius:11px;background:var(--teal);color:#fff;text-align:center;font-family:"Archivo",sans-serif;font-size:11.5px;font-weight:700}
.bud-mk{background:#1E7A8A;color:#fff;border:2px solid #fff;border-radius:50%;width:24px!important;height:24px!important;line-height:20px;text-align:center;font:700 11px Archivo,sans-serif;box-shadow:0 1px 3px rgba(0,0,0,.4)}
@media (max-width:640px){.bud .hm{display:none}.bud td.mvs .mv{display:block;margin:0 0 4px}.bud #bud-itin input[type=number]{width:56px}.bud #bud-itin td{padding-left:5px;padding-right:5px}.bud input[type=number]{width:64px}.bud-bar{grid-template-columns:96px 1fr auto;font-size:12px}.bud-card .big{font-size:24px}#bud-mapa{height:72vh;min-height:360px}.bud select{max-width:100%}}
"""


def render_presupuesto(FULL, C, navbar, VERSION):
    root = "../"
    D = datos(FULL, C)
    nav = navbar(root, [("Portal", root), ("Mapa", root + "mapa/"), ("Documentación", root + "documentacion/"),
                        ("Visados", root + "visados/"), ("CPD", root + "cpd/"), ("El perro", root + "perro/"), ("Ruta", "#ruta"), ("Resumen", "#resumen"),
                        ("Combustible", "#combustible"), ("Visados", "#visados"), ("Vehículo", "#vehiculo"),
                        ("Ferry", "#ferry"), ("Resto", "#partidas"), ("Criterio", "#criterio")], "Planificador")
    v1, v2 = P.VEHICULOS
    hero = f"""<header class="hero small">
  <div class="hero-txt">
    <span class="kicker">Ruta, fechas y presupuesto por vehículo · valores iniciales del {esc(P.FECHA)}</span>
    <h1>Planificador</h1>
    <p>Marca los países que queréis recorrer: la página ordena la ruta, añade los países de paso obligado y recalcula
    kilómetros, días, fecha de regreso y dinero. <strong>{esc(v1['nombre'])}</strong>: {esc(v1['detalle'])}, {v1['l100']:g} L/100 km.
    <strong>{esc(v2['nombre'])}</strong>: {esc(v2['detalle'])}, {v2['l100']:g} L/100 km.
    Todo es editable y se guarda en este dispositivo.</p>
  </div>
</header>"""
    th_v = "".join(f'<th class="n">{esc(v["nombre"])}</th>' for v in P.VEHICULOS)
    td_tf = "".join(f'<td class="n" id="bud-tf-{v["id"]}"></td>' for v in P.VEHICULOS)
    body = f"""{nav}{hero}
<main class="bud" style="max-width:1200px">
<section id="ruta"><h2>Ruta</h2>
<div class="bud-viajes">
<div class="bv-row"><label class="bv-l" for="viaje-sel">Mis viajes</label><select id="viaje-sel" aria-label="Viajes guardados"></select><button type="button" id="viaje-cargar">Cargar</button><button type="button" id="viaje-borrar">Borrar</button></div>
<div class="bv-row"><label class="bv-l" for="viaje-nombre">Guardar como</label><input type="text" id="viaje-nombre" placeholder="Nombre del viaje (p. ej. Túnez – Tinduf)" maxlength="60" autocomplete="off" data-1p-ignore data-lpignore="true" data-form-type="other"><button type="button" class="primary" id="viaje-guardar">Guardar</button></div>
<div class="bv-pie"><span id="viaje-actual"></span><span class="bv-arch"><button type="button" class="lnk" id="viaje-exportar">Descargar mis viajes</button> · <label class="lnk">Importar<input type="file" id="viaje-importar" accept=".json,application/json" hidden></label></span></div>
</div>
<div class="bud-grid" id="bud-ruta-cards"></div>
<ul class="bud-avisos" id="bud-avisos"></ul>
<p><strong>Toca un país en el mapa</strong> para añadirlo o quitarlo, o usa el desplegable. <strong>Arrastra</strong> los países de la lista (por el asa ⠿) para ponerlos en el orden que quieras: el viaje <strong>empieza en el primero y acaba en el último</strong>, y la página busca el ferry desde España a cada uno (o al puerto más cercano si no tienen). En cada fila elige <strong>Parar</strong> (el recorrido de su ficha) o <strong>Cruzar</strong> (lo más rápido posible). La ✕ quita el país; si es el único camino para seguir, se queda como «cruzar».</p>
<div class="bud-mapkey"><span><i style="background:rgba(30,122,138,.55)"></i>Se para</span><span><i style="background:rgba(217,123,41,.5)"></i>Solo se cruza</span><span><i style="background:#fff;border:1px solid #8A949A"></i>Fuera de la ruta</span><span><i style="background:rgba(180,58,58,.2);border:1px dashed #B43A3A"></i>En conflicto (solo si se marca)</span></div>
<div id="bud-mapa" role="img" aria-label="Mapa de la ruta: toca un país para añadirlo o quitarlo"></div>
<div class="bud-actions"><select id="ruta-add" aria-label="Añadir un país"></select><button type="button" id="ruta-opt">Ordenar por la ruta más corta</button><button type="button" id="ruta-plan">Volver a la ruta planificada</button><button type="button" id="ruta-none">Vaciar</button></div>
<div class="bud-msg" id="bud-msg" role="status" aria-live="polite" hidden></div>
<h3>Itinerario</h3>
<div class="bud-ferry-card" id="bud-fer-ida"></div>
<ol class="bud-itin" id="bud-itin"></ol>
<div class="bud-ferry-card" id="bud-fer-vuelta"></div>
<div class="bud-itin-tot"><span>Total</span><span><strong id="bud-itin-km"></strong> km</span><span><strong id="bud-itin-dias"></strong> días (+ margen)</span></div>
<details class="bud-det"><summary>Ritmo, fechas y ajustes</summary><div class="bud-cfg" id="bud-cfg"></div>
<p class="figcap">Los días de cada fila salen de dividir sus km por el ritmo; escribe una cifra en la casilla de días para fijar la de ese país.</p></details>
</section>
<section id="resumen"><h2>Resumen</h2>
<div class="bud-grid" id="bud-cards"></div>
<div class="bud-bars" id="bud-bars"></div><div class="bud-key" id="bud-key"></div>
<div class="tblwrap"><table><thead><tr><th>Partida</th>{th_v}<th class="n">Total</th></tr></thead><tbody id="bud-resumen"></tbody></table></div>
<div class="bud-actions"><button type="button" class="primary" id="bud-xlsx">Descargar hoja de cálculo completa (.xlsx, con fórmulas)</button><button type="button" id="bud-csv">Solo el resumen (CSV)</button><button type="button" id="bud-reset">Volver a todos los valores iniciales</button></div>
<p class="figcap">La hoja lleva la ruta y los valores que tengas ahora en esta página. Tiene cinco pestañas —Resumen, Parámetros, Ruta, Visados y Tasas frontera—; las casillas amarillas son datos y todo lo demás son fórmulas, así que al cambiar un dato en Excel, Numbers o Google Sheets se recalcula todo.</p>
{callout("warn", "Qué es dato y qué es estimación",
    "Combustible, visados, CPD y tasas de frontera salen de fuentes citadas. Los km de los países donde se para son los corredores de las fichas medidos por carretera (OSRM); "
    "los enlaces y los países de paso son línea recta × 1,25. Comida, noches, parques, seguros, mantenimiento, trámites del perro, imprevistos y el <strong>ritmo en km al día</strong> son "
    "<strong>estimaciones iniciales</strong>: hay que ajustarlas.", raw=True)}
</section>
<section id="vehiculos"><h2>Vehículos</h2><div class="bud-veh" id="bud-veh"></div></section>
<section id="combustible"><h2>Combustible por país</h2>
<p>Km de la ruta elegida en cada país (suma de todas las veces que se pasa), × factor de ajuste × (1 + desvíos). Son los mismos km para los dos vehículos. Total: <strong id="bud-km"></strong>.</p>
<div class="tblwrap"><table><thead><tr><th>País</th><th class="n">Km</th><th class="n">€/litro</th>{th_v}</tr></thead>
<tbody id="bud-comb"></tbody><tfoot><tr><td>Total</td><td class="n" id="bud-tf-km"></td><td></td>{td_tf}</tr></tfoot></table></div>
<h3>Precio del gasóleo usado</h3>
<div class="tblwrap"><table><thead><tr><th>País</th><th class="n">€/litro</th><th>Fecha</th><th>Fuente</th></tr></thead><tbody id="bud-precios"></tbody></table></div>
<p class="figcap">GlobalPetrolPrices del 21-09-2026 convertido a euros; Mauritania, Gambia y Congo con el precio oficial nacional. Donde no hay precio publicado se usa {str(P.GASOIL_SIN_DATO).replace('.', ',')} €/l y se avisa. Revisar antes de salir.</p>
</section>
<section id="visados"><h2>Visados (por persona)</h2>
<p>Cada uno de los <span class="bud-npers">3</span> viajeros necesita su propio visado, y uno por <strong>cada entrada</strong> en el país (si se saca un visado de entradas múltiples, escribe 1 en «Visados» y su precio en «€ por visado»). Las entradas salen de la ruta elegida.</p>
<p>Por persona: <strong id="bud-vis-pp"></strong> · para las <span class="bud-npers">3</span> personas: <strong id="bud-vis-grp"></strong>. En el resumen, el {esc(v1['nombre'])} paga {v1['personas']} personas y el {esc(v2['nombre'])}, {v2['personas']}. <span id="bud-sinvis"></span></p>
<div class="tblwrap"><table><thead><tr><th>País</th><th class="n">€ por visado</th><th class="n">Visados</th><th class="n">Por persona</th><th class="n">Total <span class="bud-npers">3</span> personas</th></tr></thead><tbody id="bud-visados"></tbody>
<tfoot><tr><td>Total</td><td></td><td></td><td class="n" id="bud-vis-tf-pp"></td><td class="n" id="bud-vis-tf-grp"></td></tr></tfoot></table></div>
</section>
<section id="vehiculo"><h2>Vehículo (por cada uno)</h2>
{callout("", "CPD (carnet de 25 hojas, RACE)", "<strong>INEOS Grenadier:</strong> carnet 383,35 € y aval de 13.700 €. <strong>Delica:</strong> carnet 383,35 € y aval de 2.900 €. Los carnets entran en el cálculo; los costes bancarios del aval todavía no se conocen y valen 0 hasta que se sepan (se editan en «Vehículos»). Los avales, 16.600 € entre los dos, quedan inmovilizados y no cuentan como gasto.", raw=True)}
<h3>Tasas de importación temporal en frontera</h3>
<p>Por vehículo y por entrada, con las entradas de la ruta elegida. Total por vehículo: <strong id="bud-tasas-tot"></strong>. Donde no hay dato, la fila vale 0 y lo dice.</p>
<div class="tblwrap"><table><thead><tr><th>País</th><th class="n">€ por entrada</th><th class="n">Entradas</th><th class="n">€ por vehículo</th></tr></thead><tbody id="bud-tasas"></tbody></table></div>
</section>
<section id="ferry"><h2>Ferris</h2>
<p>El de ida y el de vuelta los elige la ruta (primer y último país); se pueden cambiar arriba, en el itinerario. Precio de cada vehículo por trayecto = coche con conductor + un pasaje por cada persona más. Las casillas se pueden corregir con el presupuesto real de la naviera.</p>
<div class="tblwrap"><table><thead><tr><th>Trayecto</th>{th_v}</tr></thead><tbody id="bud-ferry-sel"></tbody></table></div>
<h3>Todos los ferris a Marruecos, Argelia y Túnez</h3>
<p>Desde {esc(RT.ORIGEN)}: los km hasta el puerto de embarque cuentan en el combustible y en los días. Consultado el 26-09-2026.</p>
<div class="tblwrap"><table><thead><tr><th>Ruta</th><th class="n">Horas</th><th class="n">Km desde {esc(RT.ORIGEN)}</th><th class="n">Coche + conductor ida / vuelta</th><th class="n">Pasaje</th></tr></thead><tbody id="bud-ferry-todos"></tbody></table></div>
{callout("warn", "Lo que no está confirmado",
    "Solo Barcelona–Tánger Med (GNV) es un presupuesto real para nuestros vehículos (clase A2, camarote). El resto son tarifas de coche con conductor de agregadores o «desde» de la naviera: "
    "<strong>no incluyen camarote ni el recargo de vehículo alto</strong> (el 4x4 con tienda mide ~2,3 m y casi todas las navieras lo cobran aparte: Corsica Linea, 50 €). "
    "La vuelta usa la media de julio o agosto, que en Argelia y Túnez es temporada de la diáspora y puede multiplicar el precio. "
    f"<strong>Perro:</strong> ~{P.PERRO_FERRY} € por trayecto (estimación); Algérie Ferries y Corsica Linea solo lo admiten en perrera, y Grimaldi prohíbe algunas razas en Túnez. "
    "<strong>Argelia:</strong> visado consular, seguro local y escolta en el sur. <strong>Túnez:</strong> rellenar la «Smart Traveller» del coche (obligatoria para tunecinos; para extranjeros, sin confirmar).", raw=True)}
</section>
<section id="partidas"><h2>Resto de partidas</h2>
<div class="tblwrap"><table><thead><tr><th>Partida</th><th class="n">Valor</th><th>Unidad</th></tr></thead><tbody id="bud-params"></tbody></table></div>
</section>
<section id="criterio"><h2>Criterio</h2>
{bullets([
    "Orden: el que se ponga en la lista. Entre un país y el siguiente se va por el camino más corto, sin cruzar fronteras cerradas. Los países en conflicto (Mali, Sudán, Libia, Burkina Faso, Níger, Chad, República Centroafricana, Sudán del Sur, Somalia) solo se usan si se marcan, y siempre con aviso.",
    "Al añadir un país se mete en el hueco del orden donde menos km suma; «Ordenar por la ruta más corta» rehace todo el orden. Las flechas del itinerario lo cambian a mano. Al quitar un país, el cálculo deja de usarlo también como paso, salvo que sea el único camino.",
    "«Parar» hace el recorrido de la ficha que toca (en los países que se pasan dos veces, el recorrido A la primera vez y el B la segunda); «Cruzar» es un tránsito directo. En Marruecos, el Sahara Occidental y Mauritania cruzar es la vía rápida de la costa.",
    "Km de parada: OSRM (OpenStreetMap) por todos los puntos del corredor de la ficha, 26-09-2026. Km de enlace y de tránsito: línea recta × 1,25, así que son aproximados.",
    "Días = km ÷ ritmo (uno para los países de parada y otro para los de paso y la carretera en Europa) + horas de ferry + margen. Si se escribe una duración fija, se usa esa y la página dice qué ritmo haría falta.",
    "Ferris: el de ida es el recomendado para el primer país de la lista (Marruecos: GNV Barcelona–Tánger Med; Argelia: Valencia–Mostaganem; Túnez: Génova–Túnez); si ese país no tiene ferry, el del país con ferry más cercano, y desde allí se conduce. Igual con la vuelta y el último país.",
    "Los gastos compartidos no se reparten: cada vehículo paga su combustible, sus visados, su CPD, sus tasas, su ferry y la comida de quienes viajan en él. El perro va en el INEOS Grenadier.",
    "Tipo de cambio: 1 USD = %s € (implícito en GlobalPetrolPrices del 21-09-2026). Franco CFA fijo: 655,957 por euro." % str(P.USD_EUR).replace(".", ","),
    "No incluye: el viaje hasta Barcelona, la preparación de los vehículos, vacunas y seguro médico de viaje, ni una posible escapada en avión.",
    "Los valores que cambies se guardan solo en este navegador. La hoja de cálculo del proyecto sigue siendo la referencia: los botones de descarga sirven para pasar los números.",
])}
</section>
<footer>ÁFRICA 2027 · Planificador · valores iniciales del {esc(P.FECHA)} · versión {VERSION}</footer>
</main>
<script>var A27_BUDGET = {json.dumps(D, ensure_ascii=False, separators=(",", ":"))};</script>
<script src="{root}assets/vendor/leaflet.js"></script>
<script src="{root}assets/vendor/Sortable.min.js"></script>
<script src="{root}assets/js/presupuesto-xlsx.js"></script>
<script src="{root}assets/js/{JS_PATH}"></script>"""
    extra = f'<link rel="stylesheet" href="{root}assets/vendor/leaflet.css"><style>{CSS}</style>'
    return page(root, "Planificador · África 2027", body, extra_head=extra)

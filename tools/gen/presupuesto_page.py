# -*- coding: utf-8 -*-
"""Página /presupuesto/: planificador de ruta + calculadora de presupuesto por
vehículo (funciona sin conexión).

Se marcan los países y la página rehace sola el orden, los países de tránsito
obligatorio, los km por vehículo, los días, la fecha de regreso y el dinero.
"""
import json
import math

import data_presupuesto as P
import data_ruta as RT
from data_visados import VISADOS as VIS_INFO
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
            out.append(("A", d.get("corridor_label") or "Corredor principal", d["corridor"]))
        if len(d.get("corridor_alt") or []) >= 2 and f"{slug}:B" in RT.KM:
            out.append(("B", d.get("corridor_alt_label") or "Corredor alternativo", d["corridor_alt"]))
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
            "plan": RT.PLAN.get(s, opts[0]["id"]), "tr": RT.TRANSITO_FIJO.get(s, ""),
            "gas": ({"eur": g[0], "fuente": g[1], "fecha": g[2], "nota": g[3]} if g else None),
            "vis": ("sin" if s in P.SIN_VISADO else ({"eur": vis[0], "txt": vis[1], "url": vis[2]} if vis else None)),
            "tasa": ({"eur": tasa[0], "txt": tasa[1]} if tasa else None),
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
        "ritmo_t": RT.RITMO_TRANSITO, "margen": RT.MARGEN_PCT, "dias_ferry": RT.DIAS_FERRY,
        "gas_sin_dato": P.GASOIL_SIN_DATO,
        "grupos": [("bajada", "Corredor oeste"), ("subida", "Corredor oeste · solo subida"),
                   ("bucle", "Sur y este"), ("alternativa", "Opcionales"), ("fuera", "Fuera de la ruta prevista"),
                   ("excluido", "Excluidos por protocolo (no se pueden marcar)")],
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
#bud-mapa{height:460px;border-radius:12px;border:1px solid var(--line);margin:12px 0;background:var(--surface2)}
.bud-avisos{margin:10px 0;padding-left:20px;font-size:14px}
.bud-avisos li{margin:3px 0}
.bud-num{display:inline-block;min-width:22px;height:22px;line-height:22px;border-radius:11px;background:var(--teal);color:#fff;text-align:center;font-family:"Archivo",sans-serif;font-size:11.5px;font-weight:700}
.bud-mk{background:#1E7A8A;color:#fff;border:2px solid #fff;border-radius:50%;width:24px!important;height:24px!important;line-height:20px;text-align:center;font:700 11px Archivo,sans-serif;box-shadow:0 1px 3px rgba(0,0,0,.4)}
@media (max-width:640px){.bud .hm{display:none}.bud td.mvs .mv{display:block;margin:0 0 4px}.bud #bud-itin input[type=number]{width:56px}.bud #bud-itin td{padding-left:5px;padding-right:5px}.bud input[type=number]{width:64px}.bud-bar{grid-template-columns:96px 1fr auto;font-size:12px}.bud-card .big{font-size:24px}#bud-mapa{height:340px}.bud select{max-width:100%}}
"""


def render_presupuesto(FULL, C, navbar, VERSION):
    root = "../"
    D = datos(FULL, C)
    nav = navbar(root, [("Portal", root), ("Mapa", root + "mapa/"), ("Visados", root + "visados/"),
                        ("CPD", root + "cpd/"), ("Ruta", "#ruta"), ("Resumen", "#resumen"),
                        ("Combustible", "#combustible"), ("Visados", "#visados"), ("Vehículo", "#vehiculo"),
                        ("Ferry", "#ferry"), ("Resto", "#partidas"), ("Criterio", "#criterio")], "Presupuesto")
    v1, v2 = P.VEHICULOS
    hero = f"""<header class="hero small">
  <div class="hero-txt">
    <span class="kicker">Planificador de ruta y presupuesto por vehículo · valores iniciales del {esc(P.FECHA)}</span>
    <h1>Presupuesto</h1>
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
<section id="ruta"><h2>Ruta: países y orden</h2>
<div class="bud-grid" id="bud-ruta-cards"></div>
<ul class="bud-avisos" id="bud-avisos"></ul>
<h3>Países</h3>
<p>Marca dónde queréis parar. Los países de <em>paso obligado</em> (sin marcar, con borde discontinuo) los añade el cálculo: cuentan sus km, su visado y sus tasas, pero con ritmo de tránsito. Marruecos siempre es el principio y el final (ferry desde Barcelona).</p>
<div class="bud-actions"><button type="button" id="ruta-plan">Volver a la ruta de la planificación</button><button type="button" id="ruta-opt">Ordenar automáticamente (la más corta)</button><button type="button" id="ruta-none">Desmarcar todos</button></div>
<div class="bud-paises" id="bud-paises"></div>
<h3>Ritmo y fechas</h3>
<div class="bud-cfg" id="bud-cfg"></div>
<div id="bud-mapa" role="img" aria-label="Mapa de la ruta elegida"></div>
<p class="figcap">Línea continua: países donde se para, con su corredor de la ficha. Discontinua: enlaces y países de paso (línea aproximada, no el trazado real).</p>
<h3>Itinerario</h3>
<p>En el orden de marcha. Las flechas mueven un país de parada; el desplegable elige qué corredor de su ficha se hace cada vez que se entra (si la ruta no vuelve a pasar por el país, solo cuenta la primera parte). Los días salen de dividir los km por el ritmo; escribe una cifra para fijar los de un país.</p>
<div class="tblwrap"><table><thead><tr><th>#</th><th>País y recorrido</th><th class="n">Km</th><th class="n">Días</th><th><span class="hm">Orden</span></th></tr></thead>
<tbody id="bud-itin"></tbody><tfoot><tr><td></td><td>Total</td><td class="n" id="bud-itin-km"></td><td class="n" id="bud-itin-dias"></td><td></td></tr></tfoot></table></div>
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
<section id="ferry"><h2>Ferry Barcelona – Tánger Med</h2>
<p>Tarifas de <a href="{attr(P.FERRY['fuente'])}" target="_blank" rel="noopener">GNV</a> consultadas el {esc(P.FERRY['fecha'])}, para coche de clase A2 (alto de 1,90 a 2,79 m y largo hasta 4,99 m, que es donde entra un 4x4 con tienda de techo). Son precios «desde»: suben al llenarse el barco. El cálculo usa camarote.</p>
<div class="tblwrap"><table><thead><tr><th>Vehículo</th><th>Fecha de ida</th><th>Ida (Barcelona → Tánger)</th><th>Vuelta (Tánger → Barcelona)</th></tr></thead><tbody>
{"".join(f"<tr><td><strong>{esc(a)}</strong></td><td>{esc(b)}</td><td class='n'>{esc(c)}</td><td class='n'>{esc(d)}</td></tr>" for a, b, c, d in P.FERRY['filas'])}
</tbody></table></div>
{callout("warn", "Lo que no está confirmado",
    "<strong>Vuelta:</strong> julio y agosto de 2027 todavía no están a la venta; la cifra es la de abril y mayo de 2027, y en verano suele costar más. "
    f"<strong>Perro:</strong> tiene que ir en camarote pet-friendly (máximo 2 mascotas) o en la perrera; no puede quedarse en el coche. GNV no publica el precio de la mascota ni del suplemento: se calcula ~{P.PERRO_FERRY} € por trayecto (estimación). "
    "<strong>Medidas:</strong> si algún vehículo pasa de 4,99 m de largo (portabicis, rueda trasera) o de 2,79 m de alto, cambia de clase y de precio.", raw=True)}
</section>
<section id="partidas"><h2>Resto de partidas</h2>
<div class="tblwrap"><table><thead><tr><th>Partida</th><th class="n">Valor</th><th>Unidad</th></tr></thead><tbody id="bud-params"></tbody></table></div>
</section>
<section id="criterio"><h2>Criterio</h2>
{bullets([
    "Orden automático: la ruta sale de Tánger Med, pasa por todos los países marcados y vuelve a Tánger Med por el camino más corto entre ellos, sin cruzar fronteras cerradas ni países excluidos por protocolo (Mali, Guinea-Bisáu, Sudán). Los países en conflicto (Libia, Burkina Faso, Níger, Chad, República Centroafricana, Sudán del Sur, Somalia) solo se usan si se marcan.",
    "Al añadir un país se mete en el hueco del orden donde menos km suma; «Ordenar automáticamente» rehace todo el orden buscando la ruta más corta. Las flechas del itinerario lo cambian a mano.",
    "Cada país marcado tiene un plan: qué corredor de su ficha se hace la primera vez que se entra, cuál la segunda, etc. Si la ruta pasa más veces, el resto son de tránsito. En Marruecos, el Sahara Occidental y Mauritania el tránsito es la vía rápida de la costa.",
    "Km de parada: OSRM (OpenStreetMap) por todos los puntos del corredor de la ficha, 26-09-2026. Km de enlace y de tránsito: línea recta × 1,25, así que son aproximados.",
    "Días = km ÷ ritmo (uno para los países de parada y otro para los de paso) + margen + noches de ferry. Si se escribe una duración fija, se usa esa y la página dice qué ritmo haría falta.",
    "Los gastos compartidos no se reparten: cada vehículo paga su combustible, sus visados, su CPD, sus tasas, su ferry y la comida de quienes viajan en él. El perro va en el INEOS Grenadier.",
    "Tipo de cambio: 1 USD = %s € (implícito en GlobalPetrolPrices del 21-09-2026). Franco CFA fijo: 655,957 por euro." % str(P.USD_EUR).replace(".", ","),
    "No incluye: el viaje hasta Barcelona, la preparación de los vehículos, vacunas y seguro médico de viaje, ni una posible escapada en avión.",
    "Los valores que cambies se guardan solo en este navegador. La hoja de cálculo del proyecto sigue siendo la referencia: los botones de descarga sirven para pasar los números.",
])}
</section>
<footer>ÁFRICA 2027 · Presupuesto · valores iniciales del {esc(P.FECHA)} · versión {VERSION}</footer>
</main>
<script>var A27_BUDGET = {json.dumps(D, ensure_ascii=False, separators=(",", ":"))};</script>
<script src="{root}assets/vendor/leaflet.js"></script>
<script src="{root}assets/js/presupuesto-xlsx.js"></script>
<script src="{root}assets/js/{JS_PATH}"></script>"""
    extra = f'<link rel="stylesheet" href="{root}assets/vendor/leaflet.css"><style>{CSS}</style>'
    return page(root, "Presupuesto · África 2027", body, extra_head=extra)

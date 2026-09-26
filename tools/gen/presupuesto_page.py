# -*- coding: utf-8 -*-
"""Página /presupuesto/: calculadora de presupuesto por vehículo (offline)."""
import json
import math

import data_presupuesto as P
from site_common import esc, attr, page, callout, bullets


def _km(pts):
    r, s = 6371.0, 0.0
    for (a, b), (c, d) in zip(pts, pts[1:]):
        p1, p2 = math.radians(a), math.radians(c)
        h = (math.sin((p2 - p1) / 2) ** 2
             + math.cos(p1) * math.cos(p2) * math.sin(math.radians(d - b) / 2) ** 2)
        s += 2 * r * math.asin(math.sqrt(h))
    return s


def _pts(d, clave):
    if isinstance(clave, list):
        return clave
    if clave == "corridor+alt":
        return (d.get("corridor") or []) + (d.get("corridor_alt") or [])[1:]
    if clave.startswith("extra:"):
        ex = [e for e in d.get("extra_corridors", []) if isinstance(e, dict) and e.get("pts")]
        i = int(clave.split(":")[1])
        return ex[i]["pts"] if i < len(ex) else []
    return d.get(clave) or []


def datos(FULL, nombres):
    tramos = []
    for i, (slug, clave, veces, etiqueta, activo, nota) in enumerate(P.TRAMOS):
        d = FULL.get(slug)
        if not d:
            continue
        pts = _pts(d, clave)
        if len(pts) < 2:
            continue
        precio = P.GASOIL.get(slug)
        tramos.append({
            "id": f"t{i}", "slug": slug, "pais": nombres.get(slug, slug), "tramo": etiqueta,
            "km": round(_km(pts) * veces), "on": activo, "nota": nota,
        })
    gasoil = {s: {"eur": v[0], "fuente": v[1], "fecha": v[2], "nota": v[3]} for s, v in P.GASOIL.items()}
    visados = [{"id": f"vi{i}", "slug": s, "pais": nombres.get(s, s), "eur": e, "n": n, "txt": t, "url": u, "on": True}
               for i, (s, e, n, t, u) in enumerate(P.VISADOS)]
    tasas = [{"id": f"tf{i}", "slug": s, "pais": nombres.get(s, s), "eur": e, "txt": t, "on": True}
             for i, (s, e, t) in enumerate(P.TASAS_FRONTERA)]
    params = [{"id": a, "label": b, "val": c, "unidad": d, "ambito": e, "tipo": f, "nota": g}
              for a, b, c, d, e, f, g in P.PARAMETROS]
    return {
        "fecha": P.FECHA, "dias": P.DIAS, "factor": P.FACTOR_CARRETERA, "desvios": P.DESVIOS_PCT,
        "vehiculos": P.VEHICULOS, "tramos": tramos, "gasoil": gasoil, "visados": visados,
        "sin_visado": [nombres.get(s, s) for s in P.SIN_VISADO], "tasas": tasas, "params": params,
        "cpd": {"emision": P.CPD_EMISION, "comision": P.CPD_COMISION_AVAL, "aval": P.CPD_AVAL},
        "ferry": P.FERRY, "perro_ferry": P.PERRO_FERRY,
    }


CSS = """
.bud-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin:18px 0}
.bud-card{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.bud-card .lbl{font-family:"Archivo",sans-serif;font-size:11px;font-weight:700;letter-spacing:.14em;color:var(--teal);text-transform:uppercase}
.bud-card .big{font-family:"Archivo",sans-serif;font-size:28px;font-weight:800;color:var(--head);font-variant-numeric:tabular-nums;line-height:1.15}
.bud-card .sub{font-family:"Archivo",sans-serif;font-size:12.5px;color:var(--ink-soft)}
.bud-bars{display:flex;flex-direction:column;gap:7px;margin:10px 0 4px}
.bud-bar{display:grid;grid-template-columns:minmax(120px,190px) 1fr auto;gap:10px;align-items:center;font-family:"Archivo",sans-serif;font-size:13px}
.bud-bar .track{background:var(--surface2);border-radius:4px;height:14px;overflow:hidden;display:flex}
.bud-bar .track i{display:block;height:100%}
.bud-bar .v{font-variant-numeric:tabular-nums;min-width:74px;text-align:right}
.bud-key{display:flex;gap:14px;flex-wrap:wrap;font-family:"Archivo",sans-serif;font-size:12.5px;color:var(--ink-soft);margin:6px 0 0}
.bud-key i{display:inline-block;width:11px;height:11px;border-radius:2px;margin-right:5px;vertical-align:-1px}
.bud input[type=number]{width:84px;font:inherit;font-family:"Archivo",sans-serif;font-size:13.5px;padding:3px 6px;border:1px solid var(--line);border-radius:6px;background:var(--surface);color:var(--ink);font-variant-numeric:tabular-nums}
.bud input[type=number].edited{border-color:var(--amber);background:var(--amber-bg)}
.bud input[type=checkbox]{width:17px;height:17px;accent-color:var(--teal)}
.bud td.n,.bud th.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.bud tr.off td{opacity:.45}
.bud tfoot td{font-weight:700;font-family:"Archivo",sans-serif;background:var(--surface2)}
.bud .nota{display:block;font-size:12.5px;color:var(--ink-soft);line-height:1.4;margin-top:2px}
.bud .tag{font-family:"Archivo",sans-serif;font-size:10.5px;font-weight:700;letter-spacing:.06em;padding:1px 6px;border-radius:4px;white-space:nowrap}
.bud .tag.est{background:var(--amber-bg);color:var(--amber)}
.bud .tag.dat{background:var(--green-bg);color:var(--green)}
.bud-veh{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
.bud-veh .bud-card label{display:flex;justify-content:space-between;align-items:center;gap:10px;font-family:"Archivo",sans-serif;font-size:13.5px;margin:6px 0}
.bud-actions{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}
.bud-actions button{font-family:"Archivo",sans-serif;font-weight:600;font-size:13px;padding:8px 14px;border-radius:8px;border:1px solid var(--line);background:var(--surface);color:var(--ink);cursor:pointer}
.bud-actions button.primary{background:var(--teal);border-color:var(--teal);color:#fff}
.bud td strong+.nota{max-width:420px}
@media (max-width:640px){.bud .hm{display:none}.bud input[type=number]{width:64px}.bud tbody td:nth-child(2){min-width:150px}.bud-bar{grid-template-columns:96px 1fr auto;font-size:12px}.bud-card .big{font-size:24px}}
"""

JS = r"""
(function(){
const D = A27_BUDGET, KEY = 'a27-presupuesto-v1';
let S = {};
try { S = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch(e) { S = {}; }
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch(e) {} };
const get = (k, dflt) => (k in S ? S[k] : dflt);
const grp = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
const eur = v => { const r = Math.round(v); return (r < 0 ? '−' : '') + grp(Math.abs(r)) + ' €'; };
const num = (v, d=0) => { const [a, b] = Math.abs(Number(v)).toFixed(d).split('.'); return grp(a) + (b ? ',' + b : ''); };
const $ = id => document.getElementById(id);
const COLORS = {comb:'#1E7A8A', vis:'#2B6CB0', veh:'#C47F17', ferry:'#673AB7', vida:'#2E7D32', perro:'#8B5A2B', otros:'#5F6B72', imp:'#B43A3A'};
const CATS = [['comb','Combustible'],['vis','Visados'],['veh','Vehículo: CPD, tasas, seguros, mantenimiento'],['ferry','Ferry Barcelona–Tánger'],['vida','Comida, noches y actividades'],['perro','Perro'],['otros','Comunicaciones'],['imp','Imprevistos']];

function inp(key, dflt, step, extra){
  const v = get(key, dflt);
  return `<input type="number" inputmode="decimal" step="${step||'any'}" data-k="${key}" data-d="${dflt}" value="${v}" class="${v != dflt ? 'edited' : ''}" ${extra||''}>`;
}
function chk(key, dflt){
  return `<input type="checkbox" data-c="${key}" ${get(key, dflt) ? 'checked' : ''} aria-label="Incluir">`;
}
function tag(t){ return t === 'dato' ? '<span class="tag dat">dato</span>' : '<span class="tag est">estimación</span>'; }

function paintStatic(){
  // Vehículos
  $('bud-veh').innerHTML = D.vehiculos.map(v => `<div class="bud-card"><div class="lbl">${v.nombre}</div>
    <div class="sub">${v.detalle}</div>
    <label>Consumo medio (L/100 km) ${inp(v.id+'.l100', v.l100, 0.5)}</label>
    <label>Personas ${inp(v.id+'.personas', v.personas, 1)}</label>
    <label>Perros ${inp(v.id+'.perros', v.perros, 1)}</label>
    <label>Ferry ida (€) ${inp(v.id+'.ferry_ida', D.ferry.ida[v.id], 1)}</label>
    <label>Ferry vuelta (€) ${inp(v.id+'.ferry_vuelta', D.ferry.vuelta[v.id], 1)}</label></div>`).join('')
    + `<div class="bud-card"><div class="lbl">Viaje</div><div class="sub">10 ene – ~15 ago 2027 = 217 días. La planificación manuscrita apunta a volver a finales de julio (unos 200).</div>
    <label>Días ${inp('dias', D.dias, 1)}</label>
    <label>Factor carretera / línea recta ${inp('factor', D.factor, 0.05)}</label>
    <label>Desvíos fuera del corredor (%) ${inp('desvios', D.desvios, 1)}</label></div>`;
  // Tramos
  $('bud-tramos').innerHTML = D.tramos.map(t => {
    const g = D.gasoil[t.slug] || {eur: 0, nota: 'sin precio'};
    return `<tr data-row="${t.id}"><td>${chk(t.id, t.on)}</td><td><strong>${t.pais}</strong><span class="nota">${t.tramo}${t.nota ? ' · ' + t.nota : ''}</span></td>
    <td class="n">${inp(t.id+'.km', t.km, 10)}</td><td class="n hm" data-o="kmr"></td>
    <td class="n">${inp('g.'+t.slug, g.eur, 0.01, 'data-g="'+t.slug+'"')}</td>
    ${D.vehiculos.map(v => `<td class="n" data-o="${v.id}"></td>`).join('')}</tr>`;
  }).join('');
  // Precios
  const vistos = new Set();
  $('bud-precios').innerHTML = D.tramos.filter(t => !vistos.has(t.slug) && vistos.add(t.slug)).map(t => {
    const g = D.gasoil[t.slug]; if (!g) return '';
    const host = (g.fuente.match(/^https?:\/\/(?:www\.)?([^/]+)/) || [,''])[1];
    return `<tr><td><strong>${t.pais}</strong>${g.nota ? '<span class="nota">'+g.nota+'</span>' : ''}</td><td class="n">${num(g.eur,3)} €</td><td>${g.fecha}</td><td><a href="${g.fuente}" target="_blank" rel="noopener">${host}</a></td></tr>`;
  }).join('');
  // Visados
  $('bud-visados').innerHTML = D.visados.map(v => `<tr data-row="${v.id}"><td>${chk(v.id, v.on)}</td><td><strong>${v.pais}</strong><span class="nota">${v.txt} · <a href="${v.url}" target="_blank" rel="noopener">fuente</a></span></td>
    <td class="n">${inp(v.id+'.eur', v.eur, 1)}</td><td class="n">${inp(v.id+'.n', v.n, 1)}</td><td class="n" data-o="pp"></td><td class="n" data-o="grp"></td></tr>`).join('');
  // Tasas de frontera
  $('bud-tasas').innerHTML = D.tasas.map(v => `<tr data-row="${v.id}"><td>${chk(v.id, v.on)}</td><td><strong>${v.pais}</strong><span class="nota">${v.txt}${v.eur === 0 ? ' · <strong>sin importe: no suma nada</strong>' : ''}</span></td>
    <td class="n">${inp(v.id+'.eur', v.eur, 1)}</td></tr>`).join('');
  // Partidas
  $('bud-params').innerHTML = D.params.map(p => `<tr><td><strong>${p.label}</strong> ${tag(p.tipo)}${p.nota ? '<span class="nota">'+p.nota+'</span>' : ''}</td>
    <td class="n">${inp('p.'+p.id, p.val, p.val >= 100 ? 10 : 0.5)}</td><td>${p.unidad}</td></tr>`).join('');
}

function V(k, d){ const x = parseFloat(get(k, d)); return isFinite(x) ? x : 0; }
function on(k, d){ return !!get(k, d); }

function compute(){
  const dias = V('dias', D.dias), factor = V('factor', D.factor), desv = V('desvios', D.desvios) / 100;
  const veh = D.vehiculos.map(v => ({...v, l100: V(v.id+'.l100', v.l100), personas: V(v.id+'.personas', v.personas),
      perros: V(v.id+'.perros', v.perros), ferry: V(v.id+'.ferry_ida', D.ferry.ida[v.id]) + V(v.id+'.ferry_vuelta', D.ferry.vuelta[v.id])}));
  const R = {}; veh.forEach(v => R[v.id] = {comb:0, vis:0, veh:0, ferry:0, vida:0, perro:0, otros:0, imp:0, litros:0});
  let kmTot = 0;
  // Combustible
  D.tramos.forEach(t => {
    const row = document.querySelector(`tr[data-row="${t.id}"]`);
    const act = on(t.id, t.on); row.classList.toggle('off', !act);
    const kmr = V(t.id+'.km', t.km) * factor * (1 + desv);
    const precio = V('g.'+t.slug, (D.gasoil[t.slug]||{}).eur || 0);
    row.querySelector('[data-o="kmr"]').textContent = num(kmr);
    veh.forEach(v => {
      const l = kmr * v.l100 / 100, e = l * precio;
      row.querySelector(`[data-o="${v.id}"]`).innerHTML = `${eur(e)}<span class="nota">${num(l)} L</span>`;
      if (act) { R[v.id].comb += e; R[v.id].litros += l; }
    });
    if (act) kmTot += kmr;
  });
  $('bud-km').textContent = num(kmTot) + ' km';
  veh.forEach(v => { $('bud-tf-'+v.id).innerHTML = `${eur(R[v.id].comb)}<span class="nota">${num(R[v.id].litros)} L</span>`; });
  $('bud-tf-km').textContent = num(kmTot);
  // Visados: el importe es por persona; se multiplica por todas las personas del viaje.
  const nPers = veh.reduce((s, v) => s + v.personas, 0);
  let visPP = 0;
  D.visados.forEach(v => {
    const row = document.querySelector(`tr[data-row="${v.id}"]`);
    const act = on(v.id, v.on); row.classList.toggle('off', !act);
    const t = V(v.id+'.eur', v.eur) * V(v.id+'.n', v.n);
    row.querySelector('[data-o="pp"]').textContent = eur(t);
    row.querySelector('[data-o="grp"]').textContent = eur(t * nPers);
    if (act) visPP += t;
  });
  $('bud-vis-pp').textContent = eur(visPP);
  document.querySelectorAll('.bud-npers').forEach(e => e.textContent = num(nPers));
  $('bud-vis-grp').textContent = eur(visPP * nPers);
  $('bud-vis-tf-pp').textContent = eur(visPP);
  $('bud-vis-tf-grp').textContent = eur(visPP * nPers);
  // Tasas de frontera (por vehículo)
  let tasas = 0;
  D.tasas.forEach(v => {
    const row = document.querySelector(`tr[data-row="${v.id}"]`);
    const act = on(v.id, v.on); row.classList.toggle('off', !act);
    if (act) tasas += V(v.id+'.eur', v.eur);
  });
  $('bud-tasas-tot').textContent = eur(tasas);
  const P = {}; D.params.forEach(p => P[p.id] = V('p.'+p.id, p.val));
  const meses = dias / 30.4;
  veh.forEach(v => {
    const r = R[v.id];
    r.vis = visPP * v.personas;
    r.veh = D.cpd.emision + D.cpd.comision + tasas + P.seguros + P.mantenimiento;
    r.ferry = v.ferry;
    r.vida = P.comida * v.personas * dias + P.noche * dias + P.parques * v.personas;
    r.perro = v.perros ? (P.perro_comida * dias * v.perros + P.perro_tramites * v.perros + 2 * D.perro_ferry * v.perros) : 0;
    r.otros = P.comunicaciones * meses;
    const base = r.comb + r.vis + r.veh + r.ferry + r.vida + r.perro + r.otros;
    r.imp = base * P.imprevistos / 100;
    r.total = base + r.imp;
  });
  // Resumen
  const total = veh.reduce((s, v) => s + R[v.id].total, 0);
  const personas = veh.reduce((s, v) => s + v.personas, 0);
  const aval = D.cpd.aval * veh.length;
  $('bud-cards').innerHTML = veh.map(v => `<div class="bud-card"><div class="lbl">${v.nombre} · ${v.detalle}</div>
      <div class="big">${eur(R[v.id].total)}</div><div class="sub">${eur(R[v.id].total / Math.max(1, v.personas))} por persona · ${eur(R[v.id].total / Math.max(1, dias))} al día</div>
      <div class="sub">Combustible ${eur(R[v.id].comb)} (${num(R[v.id].litros)} L a ${num(v.l100,1)} L/100)</div></div>`).join('')
    + `<div class="bud-card"><div class="lbl">Total del viaje</div><div class="big">${eur(total)}</div>
      <div class="sub">${num(personas)} personas · ${num(dias)} días · ${num(kmTot)} km</div>
      <div class="sub">Además, ${eur(aval)} inmovilizados en los avales del CPD (se recuperan)</div></div>`;
  const max = Math.max(...CATS.map(([k]) => veh.reduce((s, v) => s + R[v.id][k], 0)), 1);
  $('bud-bars').innerHTML = CATS.map(([k, lab]) => {
    const parts = veh.map((v, i) => `<i style="width:${R[v.id][k] / max * 100}%;background:${COLORS[k]};opacity:${i ? .55 : 1}" title="${v.nombre}: ${eur(R[v.id][k])}"></i>`).join('');
    const tot = veh.reduce((s, v) => s + R[v.id][k], 0);
    return `<div class="bud-bar"><span>${lab}</span><div class="track">${parts}</div><span class="v">${eur(tot)}</span></div>`;
  }).join('');
  $('bud-key').innerHTML = veh.map((v, i) => `<span><i style="background:var(--ink-soft);opacity:${i ? .55 : 1}"></i>${v.nombre} (${v.detalle})</span>`).join('') + '<span>Tono lleno: vehículo 1 · tono claro: vehículo 2</span>';
  // Tabla por partidas
  $('bud-resumen').innerHTML = CATS.map(([k, lab]) => `<tr><td>${lab}</td>${veh.map(v => `<td class="n">${eur(R[v.id][k])}</td>`).join('')}<td class="n"><strong>${eur(veh.reduce((s, v) => s + R[v.id][k], 0))}</strong></td></tr>`).join('')
    + `<tr><td><strong>Total</strong></td>${veh.map(v => `<td class="n"><strong>${eur(R[v.id].total)}</strong></td>`).join('')}<td class="n"><strong>${eur(total)}</strong></td></tr>`;
  window.__A27_BUDGET_RESULT = {R, total, kmTot, veh};
}

function csv(){
  const res = window.__A27_BUDGET_RESULT; if (!res) return;
  const rows = [['Partida', ...res.veh.map(v => v.nombre + ' (' + v.detalle + ')'), 'Total']];
  CATS.forEach(([k, lab]) => rows.push([lab, ...res.veh.map(v => Math.round(res.R[v.id][k])), Math.round(res.veh.reduce((s, v) => s + res.R[v.id][k], 0))]));
  rows.push(['Total', ...res.veh.map(v => Math.round(res.R[v.id].total)), Math.round(res.total)]);
  rows.push([]); rows.push(['País', 'Tramo', 'Km estimados', '€/L', ...res.veh.map(v => v.nombre + ' €')]);
  const factor = V('factor', D.factor), desv = V('desvios', D.desvios) / 100;
  D.tramos.filter(t => on(t.id, t.on)).forEach(t => {
    const kmr = V(t.id+'.km', t.km) * factor * (1 + desv), p = V('g.'+t.slug, (D.gasoil[t.slug]||{}).eur || 0);
    rows.push([t.pais, t.tramo, Math.round(kmr), p, ...res.veh.map(v => Math.round(kmr * v.l100 / 100 * p))]);
  });
  const text = rows.map(r => r.map(c => /[;"\n]/.test(String(c)) ? '"' + String(c).replace(/"/g, '""') + '"' : c).join(';')).join('\n');
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob(['﻿' + text], {type: 'text/csv;charset=utf-8'}));
  a.download = 'presupuesto-africa-2027.csv'; document.body.appendChild(a); a.click(); a.remove();
}

document.addEventListener('input', e => {
  const k = e.target.dataset.k;
  if (k) { S[k] = e.target.value; e.target.classList.toggle('edited', e.target.value != e.target.dataset.d); save(); compute(); }
});
document.addEventListener('change', e => {
  const c = e.target.dataset.c;
  if (c) { S[c] = e.target.checked; save(); compute(); }
});
paintStatic(); compute();
$('bud-reset').addEventListener('click', () => { S = {}; save(); paintStatic(); compute(); });
$('bud-csv').addEventListener('click', csv);
})();
"""


def render_presupuesto(FULL, C, navbar, VERSION):
    root = "../"
    nombres = {slug: name for slug, name, *_ in C}
    D = datos(FULL, nombres)
    nav = navbar(root, [("Portal", root), ("Mapa", root + "mapa/"), ("Visados", root + "visados/"),
                        ("CPD", root + "cpd/"), ("Resumen", "#resumen"), ("Combustible", "#combustible"),
                        ("Visados", "#visados"), ("Vehículo", "#vehiculo"), ("Ferry", "#ferry"), ("Resto", "#partidas"),
                        ("Criterio", "#criterio")], "Presupuesto")
    v1, v2 = P.VEHICULOS
    hero = f"""<header class="hero small">
  <div class="hero-txt">
    <span class="kicker">Calculadora por vehículo · valores iniciales del {esc(P.FECHA)}</span>
    <h1>Presupuesto</h1>
    <p><strong>{esc(v1['nombre'])}</strong>: {esc(v1['detalle'])}, {v1['l100']:g} L/100 km.
    <strong>{esc(v2['nombre'])}</strong>: {esc(v2['detalle'])}, {v2['l100']:g} L/100 km.
    <strong>Duración:</strong> {P.DIAS} días (10 ene – ~15 ago 2027).
    Todo es editable: los cambios se recalculan al momento y se guardan en este dispositivo.</p>
  </div>
</header>"""
    th_v = "".join(f'<th class="n">{esc(v["nombre"])}</th>' for v in P.VEHICULOS)
    td_tf = "".join(f'<td class="n" id="bud-tf-{v["id"]}"></td>' for v in P.VEHICULOS)
    precios_min = sorted(P.GASOIL.items(), key=lambda kv: kv[1][0])
    barato, caro = precios_min[0], precios_min[-1]
    body = f"""{nav}{hero}
<main class="bud" style="max-width:1200px">
<section id="resumen"><h2>Resumen</h2>
<div class="bud-grid" id="bud-cards"></div>
<div class="bud-bars" id="bud-bars"></div><div class="bud-key" id="bud-key"></div>
<div class="tblwrap"><table><thead><tr><th>Partida</th>{th_v}<th class="n">Total</th></tr></thead><tbody id="bud-resumen"></tbody></table></div>
<div class="bud-actions"><button type="button" class="primary" id="bud-csv">Descargar CSV (para la hoja de cálculo)</button><button type="button" id="bud-reset">Volver a los valores iniciales</button></div>
{callout("warn", "Qué es dato y qué es estimación",
    "Combustible, visados, CPD y tasas de frontera salen de fuentes citadas en cada fila. Comida, noches, parques, "
    "seguros, mantenimiento, trámites del perro e imprevistos son <strong>estimaciones iniciales</strong> marcadas como tales: "
    "hay que ajustarlas. Los kilómetros son los corredores dibujados en las fichas, corregidos por el factor de carretera y los desvíos.", raw=True)}
</section>
<section id="vehiculos"><h2>Vehículos y viaje</h2><div class="bud-veh" id="bud-veh"></div></section>
<section id="combustible"><h2>Combustible por país y tramo</h2>
<p>Kilómetros del corredor de cada ficha (línea recta entre sus puntos) × factor de carretera × (1 + desvíos). Desmarca los tramos que no vayáis a hacer y cambia cualquier cifra.
Total activo: <strong id="bud-km"></strong>.</p>
{callout("ok", "Dónde repostar", f"El gasóleo más barato de la ruta está en <strong>{nombres.get(barato[0], barato[0])} ({f'{barato[1][0]:.2f}'.replace('.', ',')} €/l)</strong> y el más caro en <strong>{nombres.get(caro[0], caro[0])} ({f'{caro[1][0]:.2f}'.replace('.', ',')} €/l)</strong>. Llenar depósitos y bidones al salir de Angola en los dos sentidos ahorra más que cualquier otra decisión de repostaje.", raw=True)}
<div class="tblwrap"><table><thead><tr><th></th><th>País y tramo</th><th class="n">Km corredor</th><th class="n hm">Km estimados</th><th class="n">€/litro</th>{th_v}</tr></thead>
<tbody id="bud-tramos"></tbody><tfoot><tr><td></td><td>Total activo</td><td></td><td class="n hm" id="bud-tf-km"></td><td></td>{td_tf}</tr></tfoot></table></div>
<h3>Precio del gasóleo usado</h3>
<div class="tblwrap"><table><thead><tr><th>País</th><th class="n">€/litro</th><th>Fecha</th><th>Fuente</th></tr></thead><tbody id="bud-precios"></tbody></table></div>
<p class="figcap">GlobalPetrolPrices publica precios en euros; para Mauritania, Gambia y Congo el precio no es público en esa web y se ha usado el precio oficial nacional convertido. Revisar antes de salir: la guerra de Irán ha movido mucho los precios en 2026.</p>
</section>
<section id="visados"><h2>Visados (por persona)</h2>
<p>Cada uno de los <span class="bud-npers">3</span> viajeros necesita su propio visado. La columna <strong>«Visados por persona»</strong> no es el número de personas: es cuántos visados necesita <em>cada</em> persona en ese país. Vale 2 donde se entra dos veces (bajada y subida) con un visado de una sola entrada, y 1 donde se entra una vez. La última columna multiplica por todos los viajeros.</p>
<p>Por persona: <strong id="bud-vis-pp"></strong> · para las <span class="bud-npers">3</span> personas: <strong id="bud-vis-grp"></strong>. En el resumen, el vehículo 1 paga 2 personas y el vehículo 2, una. Sin visado: {esc(', '.join(D['sin_visado']))}.</p>
<div class="tblwrap"><table><thead><tr><th></th><th>País</th><th class="n">€ por visado</th><th class="n">Visados por persona</th><th class="n">Por persona</th><th class="n">Total <span class="bud-npers">3</span> personas</th></tr></thead><tbody id="bud-visados"></tbody>
<tfoot><tr><td></td><td>Total activo</td><td></td><td></td><td class="n" id="bud-vis-tf-pp"></td><td class="n" id="bud-vis-tf-grp"></td></tr></tfoot></table></div>
</section>
<section id="vehiculo"><h2>Vehículo (por cada uno)</h2>
{callout("", "CPD", f"Emisión ~{P.CPD_EMISION} € + comisión del aval ~{P.CPD_COMISION_AVAL} € por vehículo, incluidos en el cálculo. El aval (mínimo {f'{P.CPD_AVAL:,}'.replace(',', '.')} € por vehículo) queda inmovilizado y no se cuenta como gasto.", raw=True)}
<h3>Tasas de importación temporal en frontera</h3>
<p>Importes publicados en la sección CPD, por vehículo. Total activo: <strong id="bud-tasas-tot"></strong>. Donde no hay dato, la fila vale 0 y lo dice.</p>
<div class="tblwrap"><table><thead><tr><th></th><th>País</th><th class="n">€</th></tr></thead><tbody id="bud-tasas"></tbody></table></div>
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
    "Los gastos compartidos no se reparten: cada vehículo paga su combustible, sus visados, su CPD, sus tasas, su ferry y la comida de quienes viajan en él. El perro va en el vehículo 1.",
    "Tipo de cambio: 1 USD = %s € (implícito en GlobalPetrolPrices del 21-09-2026). Franco CFA fijo: 655,957 por euro." % str(P.USD_EUR).replace(".", ","),
    "Los visados siguen la tabla de la sección Visados; Congo y RD Congo se tramitan fuera de ruta (París y Madrid) y con su vigencia no cubren a la vez la bajada y la subida, por eso figuran dos.",
    "Kenia, el interior de Tanzania y Malaui están activados porque figuran en el mapa o en la planificación, pero la planificación manuscrita todavía no encaja Kenia. Desmarcar lo que no se haga.",
    "No incluye: el viaje hasta Barcelona, la preparación de los vehículos, vacunas y seguro médico de viaje, ni una posible escapada en avión.",
    "Los valores que cambies se guardan solo en este navegador. La hoja de cálculo del proyecto sigue siendo la referencia: el botón CSV sirve para pasar los números.",
])}
</section>
<footer>ÁFRICA 2027 · Presupuesto · valores iniciales del {esc(P.FECHA)} · versión {VERSION}</footer>
</main>
<script>var A27_BUDGET = {json.dumps(D, ensure_ascii=False)};</script>
<script>{JS}</script>"""
    return page(root, "Presupuesto · África 2027", body, extra_head=f"<style>{CSS}</style>")

/* Presupuesto · planificador de ruta + calculadora por vehículo (sin conexión).
   Datos: A27_BUDGET (generado por tools/gen/presupuesto_page.py). */
(function(){
const D = A27_BUDGET, RU = D.ruta, PA = RU.paises, KEY = 'a27-presupuesto-v1';
let S = {};
try { S = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch(e) { S = {}; }
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch(e) {} };
const get = (k, dflt) => (k in S ? S[k] : dflt);
const grp = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
const eur = v => { const r = Math.round(v); return (r < 0 ? '−' : '') + grp(Math.abs(r)) + ' €'; };
const num = (v, d=0) => { const [a, b] = Math.abs(Number(v)).toFixed(d).split('.'); return (v < 0 ? '−' : '') + grp(a) + (b ? ',' + b : ''); };
const $ = id => document.getElementById(id);
const escH = s => String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const COLORS = {comb:'#1E7A8A', vis:'#2B6CB0', veh:'#C47F17', ferry:'#673AB7', vida:'#2E7D32', perro:'#8B5A2B', otros:'#5F6B72', imp:'#B43A3A'};
const CATS = [['comb','Combustible'],['vis','Visados'],['veh','Vehículo: CPD, tasas, seguros, mantenimiento'],['ferry','Ferry Barcelona–Tánger'],['vida','Comida, noches y actividades'],['perro','Perro'],['otros','Comunicaciones'],['imp','Imprevistos']];
const MES = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
const fecha = d => d.getUTCDate() + ' ' + MES[d.getUTCMonth()] + ' ' + d.getUTCFullYear();
const iso2d = iso => { const d = new Date((iso || RU.salida) + 'T00:00:00Z'); return isNaN(d) ? new Date(RU.salida + 'T00:00:00Z') : d; };
const addDays = (iso, n) => { const d = iso2d(iso); d.setUTCDate(d.getUTCDate() + Math.round(n)); return d; };
const RUTA_CFG = ['ruta.salida', 'ruta.ritmo_v', 'ruta.ritmo_t', 'ruta.margen', 'ruta.dias_fijos'];

function V(k, d){ const x = parseFloat(get(k, d)); return isFinite(x) ? x : 0; }
function on(k, d){ return !!get(k, d); }
function inp(key, dflt, step, extra){
  const v = get(key, dflt);
  return `<input type="number" inputmode="decimal" step="${step||'any'}" data-k="${key}" data-d="${dflt}" value="${v}" autocomplete="off" data-1p-ignore data-lpignore="true" data-form-type="other" class="${v != dflt ? 'edited' : ''}" ${extra||''}>`;
}
function tag(t){ return t === 'dato' ? '<span class="tag dat">dato</span>' : '<span class="tag est">estimación</span>'; }
// Solo reescribe un bloque si ha cambiado su estructura (así no se pierde el foco al escribir).
function paint(id, html){ const el = $(id); if (el && el.__h !== html) { el.innerHTML = html; el.__h = html; } }
const q = sel => document.querySelector(sel);

// ------------------------------------------------------------------ geometría y grafo
function hav(a, b){
  const p1 = a[0] * Math.PI / 180, p2 = b[0] * Math.PI / 180, dl = (b[1] - a[1]) * Math.PI / 180;
  const h = Math.sin((p2 - p1) / 2) ** 2 + Math.cos(p1) * Math.cos(p2) * Math.sin(dl / 2) ** 2;
  return 2 * 6371 * Math.asin(Math.min(1, Math.sqrt(h)));
}
const F = RU.f_sin_ruta;
const ANC = {}; Object.entries(PA).forEach(([s, p]) => { ANC[s] = p.opts.flatMap(o => o.pts); });

function selSet(){ return new Set(['marruecos', ...(get('ruta.sel', null) || RU.sel_plan)].filter(s => PA[s] && !PA[s].ex && !PA[s].solo_paso)); }
function planOf(s){ return get('ruta.plan.' + s, PA[s].plan); }
function usable(s, sel, conConflicto){ return PA[s] && !PA[s].ex && (!PA[s].cf || conConflicto || sel.has(s)); }

function grafo(sel, conConflicto){
  const G = {};
  Object.keys(PA).forEach(s => G[s] = []);
  RU.fronteras.forEach(([a, b, t]) => {
    if (t === 'cerrada' || (t === 'evitar' && !conConflicto) || !usable(a, sel, conConflicto) || !usable(b, sel, conConflicto)) return;
    const base = hav(PA[a].pos, PA[b].pos) * F + (t === 'ferry' ? RU.penal_ferry : 0);
    G[a].push([b, base * (sel.has(b) || PA[b].solo_paso ? 1 : RU.penal)]);
    G[b].push([a, base * (sel.has(a) || PA[a].solo_paso ? 1 : RU.penal)]);
  });
  return G;
}
function dijkstra(G, src){
  const dist = {[src]: 0}, prev = {}, done = new Set();
  for (;;) {
    let u = null, best = Infinity;
    for (const k in dist) if (!done.has(k) && dist[k] < best) { best = dist[k]; u = k; }
    if (u === null) break;
    done.add(u);
    for (const [v, w] of G[u] || []) { const nd = best + w; if (!(v in dist) || nd < dist[v]) { dist[v] = nd; prev[v] = u; } }
  }
  return {dist, prev};
}
function makeDist(G, nodes){
  const T = {};
  nodes.forEach(n => { T[n] = dijkstra(G, n); });
  const d = (a, b) => (T[a] && b in T[a].dist) ? T[a].dist[b] : 1e7;
  const path = (a, b) => { if (!T[a] || !(b in T[a].dist)) return null; const p = [b]; let x = b; while (x !== a) { x = T[a].prev[x]; p.unshift(x); } return p; };
  return {d, path};
}
function tourLen(o, d){ const f = ['marruecos', ...o, 'marruecos']; let s = 0; for (let i = 0; i < f.length - 1; i++) s += d(f[i], f[i + 1]); return s; }
function insertar(o, s, d){
  const f = ['marruecos', ...o, 'marruecos']; let best = 0, bc = Infinity;
  for (let i = 0; i < f.length - 1; i++) { const c = d(f[i], s) + d(s, f[i + 1]) - d(f[i], f[i + 1]); if (c < bc) { bc = c; best = i; } }
  const r = o.slice(); r.splice(best, 0, s); return r;
}
function mejorar(r, d){
  // 2-opt + reubicación de un país hasta que no mejore
  let mejor = tourLen(r, d), cambio = true, vueltas = 0;
  while (cambio && vueltas++ < 60) {
    cambio = false;
    for (let i = 0; i < r.length - 1; i++) for (let j = i + 1; j < r.length; j++) {
      const t = r.slice(0, i).concat(r.slice(i, j + 1).reverse(), r.slice(j + 1)), l = tourLen(t, d);
      if (l < mejor - 1e-6) { r = t; mejor = l; cambio = true; }
    }
    for (let i = 0; i < r.length; i++) {
      const sin = r.slice(0, i).concat(r.slice(i + 1)), t = insertar(sin, r[i], d), l = tourLen(t, d);
      if (l < mejor - 1e-6) { r = t; mejor = l; cambio = true; }
    }
  }
  return r;
}
function kmReales(o, DD){ return ruta(o, DD).pas.reduce((t, p) => t + p.km, 0); }
function optimizar(o, DD){
  const d = DD.d;
  // 1) orden aproximado con la distancia entre países (vecino más próximo + 2-opt)
  let rest = o.slice(), r = [], cur = 'marruecos';
  while (rest.length) { rest.sort((a, b) => d(cur, a) - d(cur, b)); cur = rest.shift(); r.push(cur); }
  const cands = [mejorar(r, d), mejorar(o.slice(), d), o.slice()];
  let best = null, bk = Infinity;
  cands.forEach(c => { const k = kmReales(c, DD); if (k < bk) { bk = k; best = c; } });
  // 2) afinado con los km reales de la ruta (corredores incluidos)
  const t0 = Date.now();
  for (let vuelta = 0, cambio = true; cambio && vuelta < 6 && Date.now() - t0 < 4000; vuelta++) {
    cambio = false;
    for (let i = 0; i < best.length; i++) {
      const x = best[i], sin = best.slice(0, i).concat(best.slice(i + 1));
      for (let j = 0; j <= sin.length; j++) {
        if (j === i) continue;
        const t = sin.slice(0, j).concat([x], sin.slice(j)), k = kmReales(t, DD);
        if (k < bk - 1) { bk = k; best = t; cambio = true; break; }
      }
    }
    for (let i = 0; i < best.length - 1; i++) for (let j = i + 1; j < best.length; j++) {
      const t = best.slice(0, i).concat(best.slice(i, j + 1).reverse(), best.slice(j + 1)), k = kmReales(t, DD);
      if (k < bk - 1) { bk = k; best = t; cambio = true; }
    }
  }
  return best;
}

// ------------------------------------------------------------------ ruta
function ruta(oFijo, DDfijo){
  const sel = selSet();
  let o = (oFijo || get('ruta.orden', null) || RU.orden_plan).filter((s, i, a) => sel.has(s) && s !== 'marruecos' && a.indexOf(s) === i);
  const DD = DDfijo || makeDist(grafo(sel), ['marruecos', ...sel]);
  for (const s of sel) if (s !== 'marruecos' && !o.includes(s)) o = insertar(o, s, DD.d);
  const avisos = [];
  let DD2 = null;
  // Secuencia completa con los países de paso
  const full = ['marruecos', ...o, 'marruecos'], seq = [{s: 'marruecos', oi: null}];
  for (let i = 0; i < full.length - 1; i++) {
    const oi = i < o.length ? i : null;
    if (full[i] === full[i + 1]) { seq.push({s: full[i + 1], oi}); continue; }
    let p = DD.path(full[i], full[i + 1]);
    if (!p) {
      DD2 = DD2 || makeDist(grafo(sel, true), ['marruecos', ...sel]);
      p = DD2.path(full[i], full[i + 1]);
      if (p) { const cf = p.filter(s => PA[s].cf && !sel.has(s)).map(s => PA[s].n);
        avisos.push(`Entre ${PA[full[i]].n} y ${PA[full[i + 1]].n} solo hay camino ${cf.length ? 'cruzando países en conflicto sin marcar: <strong>' + cf.join(', ') + '</strong>' : 'por el <strong>interior de RD Congo</strong>, que el MAEC desaconseja por carretera'}.`); }
    }
    if (!p) { avisos.push(`<strong>Sin camino por carretera permitido</strong> entre ${PA[full[i]].n} y ${PA[full[i + 1]].n} (fronteras cerradas, países excluidos o en conflicto sin marcar). Se une en línea recta.`); seq.push({s: full[i + 1], oi}); continue; }
    p.slice(1).forEach((s, k) => seq.push({s, oi: k === p.length - 2 ? oi : null}));
  }
  // Pasadas: cada entrada en un país
  const cnt = {}, pas = [];
  seq.forEach(it => {
    const s = it.s, k = cnt[s] = (cnt[s] || 0) + 1, marcado = sel.has(s);
    let ids = null;
    if (marcado) { const pl = String(planOf(s)).split('|'); if (k <= pl.length && pl[k - 1]) ids = pl[k - 1].split('+'); }
    const tipo = ids ? 'visita' : 'transito';
    if (!ids && PA[s].tr) ids = [PA[s].tr];
    pas.push({s, k, tipo, ids, oi: it.oi, marcado});
  });
  // Geometría y km
  let cur = RU.tanger;
  pas.forEach((p, i) => {
    let pts = [], kmIn = 0, aprox = false;
    const lab = [];
    (p.ids || []).forEach(id => { const op = PA[p.s].opts.find(x => x.id === id); if (!op) return; pts = pts.concat(op.pts); kmIn += op.km; aprox = aprox || op.aprox; lab.push(op.l); });
    if (pts.length > 1 && hav(cur, pts[pts.length - 1]) < hav(cur, pts[0])) pts = pts.slice().reverse();
    if (!pts.length) {
      const nx = pas[i + 1] ? PA[pas[i + 1].s].pos : RU.tanger;
      let qq = PA[p.s].pos, bq = Infinity;
      (ANC[p.s] || []).forEach(a => { const c = hav(cur, a) + hav(a, nx); if (c < bq) { bq = c; qq = a; } });
      pts = [qq]; aprox = true;
    }
    p.kmBase = kmIn; p.legIn = hav(cur, pts[0]) * F; p.pts = pts; p.aprox = aprox; p.lab = lab.join(' + ');
    p.from = cur; cur = pts[pts.length - 1];
  });
  const vuelta = hav(cur, RU.tanger) * F;
  pas.forEach((p, i) => { p.km = p.kmBase + (i ? p.legIn / 2 : p.legIn) + (pas[i + 1] ? pas[i + 1].legIn / 2 : vuelta); });
  // Avisos
  const vistos = [...new Set(pas.map(p => p.s))];
  vistos.forEach(s => {
    const P0 = PA[s];
    if (P0.cf) avisos.push(`<strong>${P0.n}</strong>: país en conflicto (${escH(P0.seg)}).`);
    else if (P0.nivel === 'no_viable') avisos.push(`<strong>${P0.n}</strong>: visado no viable según la sección Visados.`);
    if (!P0.gas) avisos.push(`<strong>${P0.n}</strong>: sin precio publicado del gasóleo; se usa ${num(RU.gas_sin_dato, 2)} €/l.`);
    if (P0.vis === null) avisos.push(`<strong>${P0.n}</strong>: sin importe de visado localizado; cuenta 0 €.`);
    else if (P0.vis !== 'sin' && !P0.vis.eur) avisos.push(`<strong>${P0.n}</strong>: importe del visado por confirmar; cuenta 0 €.`);
  });
  const paso = vistos.filter(s => !sel.has(s) && !PA[s].solo_paso);
  if (paso.length) avisos.push(`De paso obligado, sin marcar: ${paso.map(s => PA[s].n).join(', ')}. Cuentan sus km, su visado y sus tasas.`);
  return {sel, o, pas, avisos, DD};
}

// ------------------------------------------------------------------ pintado estático
function paintStatic(){
  $('bud-veh').innerHTML = D.vehiculos.map(v => `<div class="bud-card"><div class="lbl">${v.nombre}</div>
    <div class="sub">${v.detalle}</div>
    <label>Consumo medio (L/100 km) ${inp(v.id+'.l100', v.l100, 0.5)}</label>
    <label>Personas ${inp(v.id+'.personas', v.personas, 1)}</label>
    <label>Perros ${inp(v.id+'.perros', v.perros, 1)}</label>
    <label>CPD: carnet de 25 hojas (€) ${inp(v.id+'.cpd_libro', v.cpd_libro, 0.01)}</label>
    <label>CPD: costes bancarios del aval (€) ${inp(v.id+'.cpd_banco', v.cpd_banco, 1)}</label>
    <label>CPD: aval inmovilizado (€) ${inp(v.id+'.cpd_aval', v.cpd_aval, 100)}</label>
    <label>Ferry ida (€) ${inp(v.id+'.ferry_ida', D.ferry.ida[v.id], 1)}</label>
    <label>Ferry vuelta (€) ${inp(v.id+'.ferry_vuelta', D.ferry.vuelta[v.id], 1)}</label></div>`).join('');
  const sal = get('ruta.salida', RU.salida);
  $('bud-cfg').innerHTML = `<label>Fecha de salida <input type="date" data-k="ruta.salida" data-d="${RU.salida}" value="${sal}" class="${sal != RU.salida ? 'edited' : ''}"></label>
    <label>Ritmo en países de parada (km/día) ${inp('ruta.ritmo_v', RU.ritmo_v, 10)}</label>
    <label>Ritmo en países de paso (km/día) ${inp('ruta.ritmo_t', RU.ritmo_t, 10)}</label>
    <label>Margen de días (%) ${inp('ruta.margen', RU.margen, 1)}</label>
    <label>Duración fija (días; 0 = calcular) ${inp('ruta.dias_fijos', 0, 1)}</label>
    <label>Factor de ajuste de km ${inp('factor', D.factor, 0.05)}</label>
    <label>Desvíos fuera del corredor (%) ${inp('desvios', D.desvios, 1)}</label>`;
  $('bud-params').innerHTML = D.params.map(p => `<tr><td><strong>${p.label}</strong> ${tag(p.tipo)}${p.nota ? '<span class="nota">'+p.nota+'</span>' : ''}</td>
    <td class="n">${inp('p.'+p.id, p.val, p.val >= 100 ? 10 : 0.5)}</td><td>${p.unidad}</td></tr>`).join('');
}

function paintPaises(R){
  const vistos = new Set(R.pas.map(p => p.s));
  const html = RU.grupos.map(([g, lab]) => {
    const ss = Object.keys(PA).filter(s => PA[s].g === g && !PA[s].solo_paso);
    if (!ss.length) return '';
    return `<div><div class="gr">${lab}</div><div class="bud-chips">${ss.map(s => {
      const P0 = PA[s], onn = R.sel.has(s), paso = !onn && vistos.has(s);
      const cls = ['bud-chip', onn ? 'on' : '', paso ? 'paso' : '', P0.cf ? 'cf' : '', P0.ex ? 'ex' : ''].join(' ').trim();
      const dis = P0.ex || s === 'marruecos' ? 'disabled' : '';
      const t = P0.ex ? 'Excluido por protocolo' : (P0.cf ? 'Conflicto: ' + P0.seg : (P0.nota || ''));
      return `<label class="${cls}" title="${escH(t)}"><input type="checkbox" data-sel="${s}" ${onn ? 'checked' : ''} ${dis}>${P0.n}${paso ? ' <small>de paso</small>' : ''}${P0.cf ? ' <small>conflicto</small>' : ''}</label>`;
    }).join('')}</div></div>`;
  }).join('');
  paint('bud-paises', html);
}

function planChoices(s){
  const ops = PA[s].opts, L = id => (ops.find(o => o.id === id) || {}).l || id, out = [];
  ops.forEach(o => out.push([o.id, 'Solo ' + o.l]));
  ops.forEach(o => out.push([o.id + '|' + o.id, 'Ida y vuelta: ' + o.l]));
  if (ops.length >= 2) {
    const a = ops[0].id, b = ops[1].id;
    out.push([a + '|' + b, 'Ida: ' + L(a) + ' · vuelta: ' + L(b)]);
    out.push([b + '|' + a, 'Ida: ' + L(b) + ' · vuelta: ' + L(a)]);
    out.push([a + '+' + b, 'Los dos seguidos en una sola entrada']);
  }
  const cur = planOf(s);
  if (!out.some(x => x[0] === cur)) out.push([cur, cur]);
  return out;
}

// ------------------------------------------------------------------ mapa
let MAP = null, CAPA = null, ENCUADRADO = false;
function paintMapa(R){
  if (typeof L === 'undefined' || !$('bud-mapa')) return;
  try {
    if (!MAP) {
      MAP = L.map('bud-mapa', {scrollWheelZoom: false}).setView([2, 18], 3);
      L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {maxZoom: 12, attribution: 'Tiles © Esri'}).addTo(MAP);
      CAPA = L.layerGroup().addTo(MAP);
    }
    CAPA.clearLayers();
    const todos = [RU.tanger];
    R.pas.forEach(p => {
      L.polyline([p.from, p.pts[0]], {color: '#5F6B72', weight: 2, dashArray: '5 6', opacity: .8}).addTo(CAPA);
      if (p.pts.length > 1) L.polyline(p.pts, {color: p.tipo === 'visita' ? '#1E7A8A' : '#8A949A', weight: p.tipo === 'visita' ? 3.5 : 2.5, dashArray: p.tipo === 'visita' ? null : '5 6'})
        .addTo(CAPA).bindTooltip(PA[p.s].n + (p.lab ? ' · ' + p.lab : ''));
      todos.push(...p.pts);
    });
    const last = R.pas.length ? R.pas[R.pas.length - 1].pts.slice(-1)[0] : RU.tanger;
    L.polyline([last, RU.tanger], {color: '#5F6B72', weight: 2, dashArray: '5 6'}).addTo(CAPA);
    R.pas.forEach((p, i) => { if (p.tipo !== 'visita') return; const c = p.pts[Math.floor(p.pts.length / 2)];
      L.marker(c, {icon: L.divIcon({className: 'bud-mk', html: String(i + 1), iconSize: [24, 24]})}).addTo(CAPA).bindTooltip((i + 1) + '. ' + PA[p.s].n); });
    if (!ENCUADRADO) { MAP.fitBounds(L.latLngBounds(todos), {padding: [20, 20]}); ENCUADRADO = true; }
  } catch (e) { /* sin mapa: el resto sigue funcionando */ }
}

// ------------------------------------------------------------------ cálculo
function compute(){
  const R = ruta();
  if (('ruta.orden' in S || 'ruta.sel' in S) && JSON.stringify(S['ruta.orden']) !== JSON.stringify(R.o)) { S['ruta.orden'] = R.o; save(); }
  const factor = V('factor', D.factor), desv = V('desvios', D.desvios) / 100;
  const rv = Math.max(1, V('ruta.ritmo_v', RU.ritmo_v)), rt = Math.max(1, V('ruta.ritmo_t', RU.ritmo_t));
  let kmTot = 0, diasRuta = 0;
  R.pas.forEach(p => {
    p.kmE = p.km * factor * (1 + desv);
    p.diasCalc = p.kmE / (p.tipo === 'visita' ? rv : rt);
    const k = 'ruta.d.' + p.s + '.' + p.k, ov = get(k, '');
    p.dkey = k; p.dias = (ov !== '' && isFinite(parseFloat(ov))) ? parseFloat(ov) : p.diasCalc;
    kmTot += p.kmE; diasRuta += p.dias;
  });
  const margen = V('ruta.margen', RU.margen) / 100, fijos = V('ruta.dias_fijos', 0);
  const diasCalc = Math.ceil(diasRuta * (1 + margen) + RU.dias_ferry);
  const dias = fijos > 0 ? fijos : diasCalc;
  const salida = get('ruta.salida', RU.salida) || RU.salida;
  const regreso = addDays(salida, dias), previsto = iso2d(RU.regreso);
  const diasPrev = Math.round((previsto - iso2d(salida)) / 864e5);
  // ---- Países e itinerario
  paintPaises(R);
  const firstPass = {};
  const rows = R.pas.map((p, i) => {
    const P0 = PA[p.s];
    let rec = '';
    if (p.marcado && !firstPass[p.s]) {
      firstPass[p.s] = 1;
      const ch = planChoices(p.s);
      if (ch.length > 1) rec = `<select data-plan="${p.s}" class="${planOf(p.s) !== P0.plan ? 'edited' : ''}" aria-label="Recorrido en ${escH(P0.n)}">${ch.map(([v, l]) => `<option value="${escH(v)}" ${v === planOf(p.s) ? 'selected' : ''}>${escH(l)}</option>`).join('')}</select>`;
    }
    const que = p.tipo === 'visita' ? `<span class="tag vi">parada</span> ${escH(p.lab)}` : `<span class="tag tr">de paso</span> ${p.lab ? escH(p.lab) : 'enlace aproximado'}`;
    const mv = p.oi != null ? `<button type="button" class="mv" data-mv="${p.oi},-1" ${p.oi === 0 ? 'disabled' : ''} aria-label="Antes">↑</button> <button type="button" class="mv" data-mv="${p.oi},1" ${p.oi === R.o.length - 1 ? 'disabled' : ''} aria-label="Después">↓</button>` : '';
    const dv = get(p.dkey, '');
    return `<tr class="${p.tipo}"><td>${p.tipo === 'visita' ? '<span class="bud-num">' + (i + 1) + '</span>' : (i + 1)}</td><td><strong>${escH(P0.n)}</strong>${p.k > 1 ? ' <small>(' + p.k + 'ª vez)</small>' : ''}<span class="nota">${que}${p.aprox && p.tipo === 'visita' ? ' · km aproximados' : ''}</span>${rec ? '<div class="rec">' + rec + '</div>' : ''}</td>
      <td class="n" data-o="km${i}"></td>
      <td class="n"><input type="number" step="0.5" min="0" data-k="${p.dkey}" data-d="" value="${dv}" class="${dv !== '' ? 'edited' : ''}" data-o="dp${i}" autocomplete="off" data-1p-ignore data-lpignore="true" aria-label="Días en ${escH(P0.n)}"></td><td class="mvs">${mv}</td></tr>`;
  });
  paint('bud-itin', rows.join(''));
  R.pas.forEach((p, i) => { const k = q(`[data-o="km${i}"]`); if (k) k.textContent = num(p.kmE); const d = q(`[data-o="dp${i}"]`); if (d) d.placeholder = num(p.diasCalc, 1); });
  $('bud-itin-km').textContent = num(kmTot);
  $('bud-itin-dias').textContent = num(diasRuta, 1);
  paintMapa(R);
  // ---- Por país
  const porPais = {}, orden = [];
  R.pas.forEach(p => { if (!porPais[p.s]) { porPais[p.s] = {km: 0, entradas: 0}; orden.push(p.s); } porPais[p.s].km += p.kmE; porPais[p.s].entradas++; });
  const veh = D.vehiculos.map(v => ({...v, l100: V(v.id+'.l100', v.l100), personas: V(v.id+'.personas', v.personas),
      perros: V(v.id+'.perros', v.perros), ferry: V(v.id+'.ferry_ida', D.ferry.ida[v.id]) + V(v.id+'.ferry_vuelta', D.ferry.vuelta[v.id])}));
  const Rr = {}; veh.forEach(v => Rr[v.id] = {comb:0, vis:0, veh:0, ferry:0, vida:0, perro:0, otros:0, imp:0, litros:0});
  const gasDef = s => { const g = PA[s].gas; return g ? g.eur : RU.gas_sin_dato; };
  const gasKey = s => 'g.' + (s === 'cabinda' ? 'angola' : s);
  paint('bud-comb', orden.map(s => `<tr><td><strong>${PA[s].n}</strong>${PA[s].gas ? '' : '<span class="nota">Sin precio publicado: valor genérico</span>'}</td><td class="n" data-o="ck${s}"></td>
    <td class="n">${inp(gasKey(s), gasDef(s), 0.01)}</td>${D.vehiculos.map(v => `<td class="n" data-o="c${v.id}${s}"></td>`).join('')}</tr>`).join(''));
  const combOut = [];
  orden.forEach(s => {
    const km = porPais[s].km, pr = V(gasKey(s), gasDef(s));
    combOut.push({s, km, pr});
    q(`[data-o="ck${s}"]`).textContent = num(km);
    veh.forEach(v => { const l = km * v.l100 / 100, e = l * pr; Rr[v.id].comb += e; Rr[v.id].litros += l;
      q(`[data-o="c${v.id}${s}"]`).innerHTML = `${eur(e)}<span class="nota">${num(l)} L</span>`; });
  });
  $('bud-km').textContent = num(kmTot) + ' km';
  $('bud-tf-km').textContent = num(kmTot);
  veh.forEach(v => { $('bud-tf-'+v.id).innerHTML = `${eur(Rr[v.id].comb)}<span class="nota">${num(Rr[v.id].litros)} L</span>`; });
  paint('bud-precios', orden.filter(s => PA[s].gas && s !== 'cabinda').map(s => { const g = PA[s].gas, host = (g.fuente.match(/^https?:\/\/(?:www\.)?([^/]+)/) || [,''])[1];
    return `<tr><td><strong>${PA[s].n}</strong>${g.nota ? '<span class="nota">'+g.nota+'</span>' : ''}</td><td class="n">${num(g.eur,3)} €</td><td>${g.fecha}</td><td><a href="${g.fuente}" target="_blank" rel="noopener">${host}</a></td></tr>`; }).join(''));
  // ---- Visados
  const nPers = veh.reduce((s, v) => s + v.personas, 0);
  const conVis = orden.filter(s => PA[s].vis !== 'sin'), sinVis = orden.filter(s => PA[s].vis === 'sin' && !PA[s].solo_paso);
  paint('bud-visados', conVis.map(s => { const vi = PA[s].vis;
    return `<tr><td><strong>${PA[s].n}</strong><span class="nota">${vi ? escH(vi.txt) + ' · <a href="' + vi.url + '" target="_blank" rel="noopener">fuente</a>' : 'Sin importe localizado'}</span></td>
    <td class="n">${inp('vis.'+s, vi ? vi.eur : 0, 1)}</td><td class="n"><input type="number" step="1" min="0" data-k="vis.n.${s}" data-d="" value="${get('vis.n.'+s, '')}" class="${get('vis.n.'+s, '') !== '' ? 'edited' : ''}" data-o="vn${s}" autocomplete="off" data-1p-ignore data-lpignore="true" aria-label="Visados por persona en ${escH(PA[s].n)}"></td><td class="n" data-o="vp${s}"></td><td class="n" data-o="vg${s}"></td></tr>`; }).join(''));
  let visPP = 0;
  const visOut = [];
  conVis.forEach(s => { const vi = PA[s].vis, ov = get('vis.n.'+s, ''), n = (ov !== '' && isFinite(parseFloat(ov))) ? parseFloat(ov) : porPais[s].entradas, pu = V('vis.'+s, vi ? vi.eur : 0), e = pu * n;
    visPP += e; visOut.push({s, eur: pu, n, txt: vi ? vi.txt : 'Sin importe localizado', url: vi ? vi.url : ''});
    q(`[data-o="vn${s}"]`).placeholder = porPais[s].entradas; q(`[data-o="vp${s}"]`).textContent = eur(e); q(`[data-o="vg${s}"]`).textContent = eur(e * nPers); });
  $('bud-sinvis').textContent = sinVis.length ? 'Sin visado: ' + sinVis.map(s => PA[s].n).join(', ') + '.' : '';
  $('bud-vis-pp').textContent = eur(visPP); $('bud-vis-grp').textContent = eur(visPP * nPers);
  $('bud-vis-tf-pp').textContent = eur(visPP); $('bud-vis-tf-grp').textContent = eur(visPP * nPers);
  document.querySelectorAll('.bud-npers').forEach(e => e.textContent = num(nPers));
  // ---- Tasas
  const conTasa = orden.filter(s => PA[s].tasa || !['marruecos', 'sahara-occidental'].includes(s));
  paint('bud-tasas', conTasa.map(s => { const t = PA[s].tasa;
    return `<tr><td><strong>${PA[s].n}</strong><span class="nota">${t ? escH(t.txt) : 'Sin dato'}${!t || !t.eur ? ' · <strong>sin importe: no suma nada</strong>' : ''}</span></td>
    <td class="n">${inp('tasa.'+s, t ? t.eur : 0, 1)}</td><td class="n" data-o="tn${s}"></td><td class="n" data-o="tt${s}"></td></tr>`; }).join(''));
  let tasas = 0;
  const tasOut = [];
  conTasa.forEach(s => { const t = PA[s].tasa, e = V('tasa.'+s, t ? t.eur : 0), n = porPais[s].entradas; tasas += e * n; tasOut.push({s, eur: e, n, txt: t ? t.txt : 'Sin dato'});
    q(`[data-o="tn${s}"]`).textContent = n; q(`[data-o="tt${s}"]`).textContent = eur(e * n); });
  $('bud-tasas-tot').textContent = eur(tasas);
  // ---- Resto
  const P = {}; D.params.forEach(p => P[p.id] = V('p.'+p.id, p.val));
  const meses = dias / 30.4;
  veh.forEach(v => {
    const r = Rr[v.id];
    r.vis = visPP * v.personas;
    r.veh = V(v.id+'.cpd_libro', v.cpd_libro) + V(v.id+'.cpd_banco', v.cpd_banco) + tasas + P.seguros + P.mantenimiento;
    r.ferry = v.ferry;
    r.vida = P.comida * v.personas * dias + P.noche * dias + P.parques * v.personas;
    r.perro = v.perros ? (P.perro_comida * dias * v.perros + P.perro_tramites * v.perros + 2 * D.perro_ferry * v.perros) : 0;
    r.otros = P.comunicaciones * meses;
    const base = r.comb + r.vis + r.veh + r.ferry + r.vida + r.perro + r.otros;
    r.imp = base * P.imprevistos / 100;
    r.total = base + r.imp;
  });
  const total = veh.reduce((s, v) => s + Rr[v.id].total, 0);
  const aval = veh.reduce((s, v) => s + V(v.id+'.cpd_aval', v.cpd_aval), 0);
  // ---- Tarjetas de la ruta
  const dif = Math.round((regreso - previsto) / 864e5);
  const ritmoNec = kmTot / Math.max(1, (diasPrev - RU.dias_ferry) / (1 + margen));
  const nPaso = new Set(R.pas.filter(p => !R.sel.has(p.s) && !PA[p.s].solo_paso).map(p => p.s)).size;
  $('bud-ruta-cards').innerHTML = `<div class="bud-card"><div class="lbl">Países</div><div class="big">${R.sel.size}</div><div class="sub">marcados · ${nPaso} más de paso · ${R.pas.length} entradas en total</div></div>
    <div class="bud-card"><div class="lbl">Km por vehículo</div><div class="big">${num(kmTot)}</div><div class="sub">${num(kmTot / Math.max(1, dias))} km de media al día, contando paradas</div></div>
    <div class="bud-card ${dif > 0 ? 'alerta' : ''}"><div class="lbl">Días · regreso</div><div class="big">${num(dias)} días</div><div class="sub">${fecha(iso2d(salida))} → <strong>${fecha(regreso)}</strong>${fijos > 0 ? ' · duración fija (con el ritmo elegido saldrían ' + num(diasCalc) + ')' : ''}</div>
      <div class="sub">${dif > 0 ? `${num(dif)} días después del regreso previsto (${fecha(previsto)}). Para llegar ese día haría falta un ritmo medio de ~${num(ritmoNec)} km/día.` : `${num(-dif)} días antes del regreso previsto (${fecha(previsto)}).`}</div></div>
    <div class="bud-card"><div class="lbl">Presupuesto total</div><div class="big">${eur(total)}</div><div class="sub">${eur(total / Math.max(1, nPers))} por persona · <a href="#resumen">ver el resumen</a></div></div>`;
  $('bud-avisos').innerHTML = R.avisos.map(a => `<li>${a}</li>`).join('');
  // ---- Resumen
  $('bud-cards').innerHTML = veh.map(v => `<div class="bud-card"><div class="lbl">${v.nombre} · ${v.detalle}</div>
      <div class="big">${eur(Rr[v.id].total)}</div><div class="sub">${eur(Rr[v.id].total / Math.max(1, v.personas))} por persona · ${eur(Rr[v.id].total / Math.max(1, dias))} al día</div>
      <div class="sub">Combustible ${eur(Rr[v.id].comb)} (${num(Rr[v.id].litros)} L a ${num(v.l100,1)} L/100)</div>
      <div class="sub">CPD: carnet ${num(V(v.id+'.cpd_libro', v.cpd_libro), 2)} € (incluido) · <strong>aval ${eur(V(v.id+'.cpd_aval', v.cpd_aval))} inmovilizado</strong>, no suma</div></div>`).join('')
    + `<div class="bud-card"><div class="lbl">Total del viaje</div><div class="big">${eur(total)}</div>
      <div class="sub">${num(nPers)} personas · ${num(dias)} días · ${num(kmTot)} km por vehículo</div>
      <div class="sub"><strong>Además, ${eur(aval)} inmovilizados en los avales del CPD</strong> (se recuperan al cerrar los carnets). Dinero comprometido al salir: ${eur(total + aval)}.</div></div>`;
  const max = Math.max(...CATS.map(([k]) => veh.reduce((s, v) => s + Rr[v.id][k], 0)), 1);
  $('bud-bars').innerHTML = CATS.map(([k, lab]) => {
    const parts = veh.map((v, i) => `<i style="width:${Rr[v.id][k] / max * 100}%;background:${COLORS[k]};opacity:${i ? .55 : 1}" title="${v.nombre}: ${eur(Rr[v.id][k])}"></i>`).join('');
    return `<div class="bud-bar"><span>${lab}</span><div class="track">${parts}</div><span class="v">${eur(veh.reduce((s, v) => s + Rr[v.id][k], 0))}</span></div>`;
  }).join('');
  $('bud-key').innerHTML = veh.map((v, i) => `<span><i style="background:var(--ink-soft);opacity:${i ? .55 : 1}"></i>${v.nombre} (${v.detalle})</span>`).join('') + `<span>Tono lleno: ${veh[0].nombre} · tono claro: ${veh[1].nombre}</span>`;
  $('bud-resumen').innerHTML = CATS.map(([k, lab]) => `<tr><td>${lab}</td>${veh.map(v => `<td class="n">${eur(Rr[v.id][k])}</td>`).join('')}<td class="n"><strong>${eur(veh.reduce((s, v) => s + Rr[v.id][k], 0))}</strong></td></tr>`).join('')
    + `<tr><td><strong>Total</strong></td>${veh.map(v => `<td class="n"><strong>${eur(Rr[v.id].total)}</strong></td>`).join('')}<td class="n"><strong>${eur(total)}</strong></td></tr>`
    + `<tr class="bud-aval"><td>Aval del CPD inmovilizado <span class="nota">No es gasto y no suma al total: el banco lo bloquea y se recupera al devolver el carnet con todos los sellos.</span></td>${veh.map(v => `<td class="n">${eur(V(v.id+'.cpd_aval', v.cpd_aval))}</td>`).join('')}<td class="n">${eur(aval)}</td></tr>`
    + `<tr class="bud-aval"><td>Dinero comprometido al salir <span class="nota">Total del viaje + avales.</span></td>${veh.map(v => `<td class="n">${eur(Rr[v.id].total + V(v.id+'.cpd_aval', v.cpd_aval))}</td>`).join('')}<td class="n">${eur(total + aval)}</td></tr>`;
  window.__A27_BUDGET_RESULT = {R: Rr, total, kmTot, veh, dias, diasCalc, diasRuta, fijos, margen, salida, regreso: fecha(regreso),
    ruta: R, porPais, orden, combOut, visOut, tasOut, factor, desv, rv, rt};
}

function csv(){
  const res = window.__A27_BUDGET_RESULT; if (!res) return;
  const rows = [['Partida', ...res.veh.map(v => v.nombre + ' (' + v.detalle + ')'), 'Total']];
  CATS.forEach(([k, lab]) => rows.push([lab, ...res.veh.map(v => Math.round(res.R[v.id][k])), Math.round(res.veh.reduce((s, v) => s + res.R[v.id][k], 0))]));
  rows.push(['Total', ...res.veh.map(v => Math.round(res.R[v.id].total)), Math.round(res.total)]);
  rows.push(['Aval CPD inmovilizado (no suma)', ...res.veh.map(v => Math.round(V(v.id+'.cpd_aval', v.cpd_aval))), Math.round(res.veh.reduce((s, v) => s + V(v.id+'.cpd_aval', v.cpd_aval), 0))]);
  rows.push([]); rows.push(['Días', res.dias, 'Regreso', res.regreso, 'Km por vehículo', Math.round(res.kmTot)]);
  rows.push([]); rows.push(['#', 'País', 'Tipo', 'Recorrido', 'Km', 'Días']);
  res.ruta.pas.forEach((p, i) => rows.push([i + 1, PA[p.s].n, p.tipo === 'visita' ? 'parada' : 'de paso', p.lab, Math.round(p.kmE), Math.round(p.dias * 10) / 10]));
  const text = rows.map(r => r.map(c => /[;"\n]/.test(String(c)) ? '"' + String(c).replace(/"/g, '""') + '"' : c).join(';')).join('\n');
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob(['﻿' + text], {type: 'text/csv;charset=utf-8'}));
  a.download = 'presupuesto-africa-2027.csv'; document.body.appendChild(a); a.click(); a.remove();
}

// ------------------------------------------------------------------ eventos
document.addEventListener('input', e => {
  const k = e.target.dataset.k;
  if (!k) return;
  if (e.target.value === '' && e.target.dataset.d === '') delete S[k]; else S[k] = e.target.value;
  e.target.classList.toggle('edited', e.target.value != e.target.dataset.d); save(); compute();
});
document.addEventListener('change', e => {
  const s = e.target.dataset.sel;
  if (s) { const cur = selSet(); if (e.target.checked) cur.add(s); else cur.delete(s); S['ruta.sel'] = [...cur]; save(); compute(); return; }
  const pl = e.target.dataset.plan;
  if (pl) { if (e.target.value === PA[pl].plan) delete S['ruta.plan.' + pl]; else S['ruta.plan.' + pl] = e.target.value; save(); compute(); }
});
document.addEventListener('click', e => {
  const b = e.target.closest('[data-mv]'); if (!b) return;
  const [i, d] = b.dataset.mv.split(',').map(Number), o = window.__A27_BUDGET_RESULT.ruta.o.slice(), j = i + d;
  if (j < 0 || j >= o.length) return;
  [o[i], o[j]] = [o[j], o[i]]; S['ruta.orden'] = o; S['ruta.sel'] = [...selSet()]; save(); compute();
});
paintStatic(); compute();
$('ruta-plan').addEventListener('click', () => { Object.keys(S).filter(k => k.startsWith('ruta.') && !RUTA_CFG.includes(k)).forEach(k => delete S[k]); save(); compute(); });
$('ruta-opt').addEventListener('click', () => { const R = window.__A27_BUDGET_RESULT.ruta; S['ruta.orden'] = optimizar(R.o, R.DD); S['ruta.sel'] = [...R.sel]; save(); compute(); });
$('ruta-none').addEventListener('click', () => { S['ruta.sel'] = ['marruecos']; S['ruta.orden'] = []; save(); compute(); });
$('bud-reset').addEventListener('click', () => { S = {}; save(); ['bud-itin','bud-comb','bud-visados','bud-tasas','bud-paises','bud-precios'].forEach(id => { $(id).__h = null; }); paintStatic(); compute(); });
$('bud-csv').addEventListener('click', csv);
$('bud-xlsx').addEventListener('click', () => {
  if (typeof window.a27PresupuestoXlsx !== 'function') return;
  const blob = window.a27PresupuestoXlsx({D, V, res: window.__A27_BUDGET_RESULT, PA});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = 'presupuesto-africa-2027.xlsx';
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
});
})();

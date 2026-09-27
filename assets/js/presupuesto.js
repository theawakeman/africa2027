/* Planificador · ruta + calculadora por vehículo (sin conexión).
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
const CATS = [['comb','Combustible'],['vis','Visados'],['veh','Vehículo: CPD, tasas, seguros, mantenimiento'],['ferry','Ferris'],['vida','Comida, noches y actividades'],['perro','Perro'],['otros','Comunicaciones'],['imp','Imprevistos']];
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

function selSet(){ return new Set((get('ruta.sel', null) || RU.sel_plan).filter(s => PA[s] && !PA[s].ex && !PA[s].solo_paso)); }
function planOf(s){ return get('ruta.plan.' + s, PA[s].plan); }
function evitarSet(){ return new Set(get('ruta.evitar', [])); }
function usable(s, sel, conConflicto, ev){ return PA[s] && !PA[s].ex && (!PA[s].cf || conConflicto || sel.has(s)) && (sel.has(s) || !ev || !ev.has(s)); }

function grafo(sel, conConflicto, ev){
  ev = ev || evitarSet();
  const G = {};
  Object.keys(PA).forEach(s => G[s] = []);
  RU.fronteras.forEach(([a, b, t]) => {
    if (t === 'cerrada' || (t === 'evitar' && !conConflicto) || !usable(a, sel, conConflicto, ev) || !usable(b, sel, conConflicto, ev)) return;
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
// ------------------------------------------------------------------ orden libre
// El primer y el último país de la lista fijan los ferris; «ordenar» solo mueve los de en medio.
function tourLen(o, d){ let s = 0; for (let i = 0; i < o.length - 1; i++) s += d(o[i], o[i + 1]); return s; }
function insertar(o, s, d){
  if (o.length < 2) return o.concat([s]);
  let best = 1, bc = Infinity;
  for (let i = 1; i < o.length; i++) { const c = d(o[i - 1], s) + d(s, o[i]) - d(o[i - 1], o[i]); if (c < bc) { bc = c; best = i; } }
  const r = o.slice(); r.splice(best, 0, s); return r;
}
function mejorar(r, d){
  let mejor = tourLen(r, d), cambio = true, vueltas = 0;
  while (cambio && vueltas++ < 60) {
    cambio = false;
    for (let i = 1; i < r.length - 2; i++) for (let j = i + 1; j < r.length - 1; j++) {
      const t = r.slice(0, i).concat(r.slice(i, j + 1).reverse(), r.slice(j + 1)), l = tourLen(t, d);
      if (l < mejor - 1e-6) { r = t; mejor = l; cambio = true; }
    }
    for (let i = 1; i < r.length - 1; i++) {
      const sin = r.slice(0, i).concat(r.slice(i + 1)), t = insertar(sin, r[i], d), l = tourLen(t, d);
      if (l < mejor - 1e-6) { r = t; mejor = l; cambio = true; }
    }
  }
  return r;
}
function kmReales(o, DD){ SIN_COLA = true; try { const R = ruta(o, DD); return R.pas.reduce((t, p) => t + p.km, 0); } finally { SIN_COLA = false; } }
function optimizar(o, DD){
  if (o.length < 4) return o.slice();
  const d = DD.d, ini = o[0], fin = o[o.length - 1];
  let rest = o.slice(1, -1), r = [ini], cur = ini;
  while (rest.length) { rest.sort((a, b) => d(cur, a) - d(cur, b)); cur = rest.shift(); r.push(cur); }
  r.push(fin);
  const cands = [mejorar(r, d), mejorar(o.slice(), d), o.slice()];
  let best = null, bk = Infinity;
  cands.forEach(c => { const k = kmReales(c, DD); if (k < bk) { bk = k; best = c; } });
  const t0 = Date.now();
  for (let vuelta = 0, cambio = true; cambio && vuelta < 6 && Date.now() - t0 < 4000; vuelta++) {
    cambio = false;
    for (let i = 1; i < best.length - 1; i++) {
      const x = best[i], sin = best.slice(0, i).concat(best.slice(i + 1));
      for (let j = 1; j < sin.length; j++) {
        if (j === i) continue;
        const t = sin.slice(0, j).concat([x], sin.slice(j)), k = kmReales(t, DD);
        if (k < bk - 1) { bk = k; best = t; cambio = true; break; }
      }
    }
    for (let i = 1; i < best.length - 2; i++) for (let j = i + 1; j < best.length - 1; j++) {
      const t = best.slice(0, i).concat(best.slice(i, j + 1).reverse(), best.slice(j + 1)), k = kmReales(t, DD);
      if (k < bk - 1) { bk = k; best = t; cambio = true; }
    }
  }
  return best;
}

// ------------------------------------------------------------------ ferris
const FER = RU.ferries, FER_PAISES = [...new Set(FER.map(f => f.pais))];
const ferry = id => FER.find(f => f.id === id);
function persVeh(){ return D.vehiculos.map(v => V(v.id + '.personas', v.personas)); }
function precioFerry(f, dir, v){
  const k = 'fer.' + f.id + '.' + dir + '.' + v.id, dflt = Math.round(((dir === 'ida' ? f.coche_ida : f.coche_vuelta) + Math.max(0, V(v.id + '.personas', v.personas) - 1) * f.pax) * 100) / 100;
  return {k, dflt, eur: V(k, dflt)};
}
function gasEU(code){ return V('g.eu.' + code, RU.gas_eu[code]); }
function costeFerry(f, dir){
  return D.vehiculos.reduce((t, v) => t + precioFerry(f, dir, v).eur + f.km_eu * V(v.id + '.l100', v.l100) / 100 * gasEU(f.gas), 0);
}
function elegirFerry(dir, s, DD){
  const man = get('ruta.ferry_' + dir, '');
  if (man && ferry(man)) return {f: ferry(man), auto: false};
  let pais = s && FER_PAISES.includes(s) ? s : null;
  if (!pais) pais = FER_PAISES.slice().sort((a, b) => (s ? DD.d(a, s) : 0) - (s ? DD.d(b, s) : 0))[0];
  const pref = ferry(RU.ferry_pref[pais]);
  const c = pref ? [pref] : FER.filter(f => f.pais === pais).sort((a, b) => costeFerry(a, dir) - costeFerry(b, dir));
  return {f: c[0], auto: true};
}

// ------------------------------------------------------------------ enlaces por carretera
// Entre el final de un recorrido y el principio del siguiente se pide la ruta
// por carretera a OSRM (router.project-osrm.org) y se guarda en el navegador.
// Sin conexión, o mientras llega la respuesta, el enlace es una línea recta
// (×1,25 km) y se dibuja discontinuo.
const LKEY = 'a27-enlaces-v1', OSRM = 'https://router.project-osrm.org/route/v1/driving/';
let ENL = {};
try { ENL = JSON.parse(localStorage.getItem(LKEY) || '{}') || {}; } catch(e) { ENL = {}; }
const COLA = new Map(), FALLO = new Map();   // FALLO: clave → hora del fallo (se reintenta al minuto)
let EN_VUELO = 0, SIN_COLA = false, T_REP = null, T_GUARDA = null;
const ck = p => p[0].toFixed(3) + ',' + p[1].toFixed(3);
function enlace(a, b){
  const d = hav(a, b);
  if (d < 3) return {pts: [a, b], km: d, real: true};
  const ka = ck(a), kb = ck(b), inv = ka > kb, key = inv ? kb + '|' + ka : ka + '|' + kb, e = ENL[key];
  if (e) return {pts: inv ? e.p.slice().reverse() : e.p, km: e.km, real: true};
  if (!SIN_COLA && !(Date.now() - (FALLO.get(key) || 0) < 60000) && !COLA.has(key)) { COLA.set(key, inv ? [b, a] : [a, b]); setTimeout(pedirEnlaces, 0); }
  return {pts: [a, b], km: d * F, real: false};
}
window.__A27_ENL = () => ({cola: COLA.size, vuelo: EN_VUELO, n: Object.keys(ENL).length, fallo: FALLO.size});
function pedirEnlaces(){
  while (EN_VUELO < 3 && COLA.size) {
    const [key, [a, b]] = COLA.entries().next().value; COLA.delete(key); EN_VUELO++;
    fetch(OSRM + a[1] + ',' + a[0] + ';' + b[1] + ',' + b[0] + '?overview=simplified&geometries=geojson')
      .then(r => r.ok ? r.json() : Promise.reject(r.status))
      .then(j => { const rt = j.routes && j.routes[0]; if (!rt) throw 0;
        const p = rt.geometry.coordinates.map(c => [Math.round(c[1] * 1e3) / 1e3, Math.round(c[0] * 1e3) / 1e3]);
        ENL[key] = {km: Math.round(rt.distance / 100) / 10, p: [a, ...p.slice(1, -1), b]};
        clearTimeout(T_GUARDA); T_GUARDA = setTimeout(() => { try { localStorage.setItem(LKEY, JSON.stringify(ENL)); } catch(e) {} }, 800); })
      .catch(() => { FALLO.set(key, Date.now()); })
      .finally(() => { EN_VUELO--; clearTimeout(T_REP); T_REP = setTimeout(() => { if (!EN_VUELO && !COLA.size) compute(); }, 250); pedirEnlaces(); });
  }
}

// ------------------------------------------------------------------ ruta
function opcion(s, id){ return PA[s].opts.find(x => x.id === id); }
function ruta(oFijo, DDfijo){
  const sel = selSet();
  let o = (oFijo || get('ruta.orden', null) || RU.orden_plan).filter((s, i, a) => sel.has(s) && a.indexOf(s) === i);
  const DD = DDfijo || makeDist(grafo(sel), [...new Set([...sel, ...FER_PAISES])]);
  for (const s of sel) if (!o.includes(s)) o = insertar(o, s, DD.d);
  const avisos = [];
  let DD2 = null;
  const FI = elegirFerry('ida', o[0], DD), FV = elegirFerry('vuelta', o[o.length - 1], DD);
  // Paradas en orden, con el país del ferry al principio y al final si no coincide
  const nodos = o.map((s, i) => ({s, oi: i}));
  if (!nodos.length || nodos[0].s !== FI.f.pais) nodos.unshift({s: FI.f.pais, oi: null});
  if (nodos[nodos.length - 1].s !== FV.f.pais || nodos.length === 1) nodos.push({s: FV.f.pais, oi: null});
  const seq = [nodos[0]];
  for (let i = 0; i < nodos.length - 1; i++) {
    const a = nodos[i].s, b = nodos[i + 1].s, oi = nodos[i + 1].oi;
    if (a === b) { seq.push({s: b, oi}); continue; }
    let p = DD.path(a, b);
    if (!p) {
      DD2 = DD2 || makeDist(grafo(sel, true), [...new Set([...sel, ...FER_PAISES])]);
      p = DD2.path(a, b);
      if (p) { const cf = p.filter(s => PA[s].cf && !sel.has(s)).map(s => PA[s].n);
        avisos.push(`Entre ${PA[a].n} y ${PA[b].n} solo hay camino ${cf.length ? 'cruzando países en conflicto sin marcar: <strong>' + cf.join(', ') + '</strong>' : 'por el <strong>interior de RD Congo</strong>, que el MAEC desaconseja por carretera'}.`); }
    }
    if (!p) { avisos.push(`<strong>Sin camino por carretera permitido</strong> entre ${PA[a].n} y ${PA[b].n} (fronteras cerradas o países en conflicto sin marcar). Se une en línea recta.`); seq.push({s: b, oi}); continue; }
    p.slice(1).forEach((s, k) => seq.push({s, oi: k === p.length - 2 ? oi : null}));
  }
  // Pasadas: cada entrada en un país
  const cnt = {}, pas = [];
  seq.forEach((it, idx) => {
    const s = it.s, k = cnt[s] = (cnt[s] || 0) + 1, marcado = sel.has(s);
    const via = PA[s].via || {}, vecino = [seq[idx - 1], seq[idx + 1]].map(x => x && via[x.s]).find(Boolean);
    const parts = String(planOf(s)).split('|'), def = marcado && k <= parts.length && !!parts[k - 1];
    const rec = PA[s].solo_paso ? '' : get('ruta.rec.' + s + '.' + k, '');
    const modo = get('ruta.modo.' + s + '.' + k, null), parar = PA[s].solo_paso ? false : (modo ? modo === 'p' : (rec ? true : def));
    const noTr = PA[s].opts.filter(x => x.id !== PA[s].tr);
    let ids = parar ? (rec || parts[k - 1] || (noTr[k - 1] || noTr[0] || PA[s].opts[0]).id).split('+').filter(x => opcion(s, x)) : null;
    if (ids && !ids.length) ids = [(noTr[0] || PA[s].opts[0]).id];
    const tipo = ids ? 'visita' : 'transito';
    let cand = null;
    if (vecino && !(rec && parar)) { if (Array.isArray(vecino)) cand = vecino.filter(x => opcion(s, x)); else ids = [vecino]; }
    else if (!ids && PA[s].tr) ids = [PA[s].tr];
    pas.push({s, k, tipo, ids, cand, oi: it.oi, marcado, def, manual: !!(rec && parar) || !!get('ruta.inv.' + s + '.' + k, false)});
  });
  // Países que un recorrido atraviesa sin ser el suyo (Senegal B por Gambia)
  for (let i = pas.length - 1; i >= 0; i--) {
    const p = pas[i]; if (!p.ids) continue;
    const cruza = [...new Set(p.ids.flatMap(id => (opcion(p.s, id) || {}).cruza || []))];
    cruza.filter(c => PA[c] && (!pas[i - 1] || pas[i - 1].s !== c) && (!pas[i + 1] || pas[i + 1].s !== c))
      .forEach(c => pas.splice(i + 1, 0, {s: c, k: 0, tipo: 'transito', ids: [], dentro: p.s, oi: null, marcado: sel.has(c), def: false}));
  }
  // Geometría y km: del puerto de llegada al de salida
  let cur = FI.f.pos;
  pas.forEach((p, i) => {
    if (p.dentro) {
      p.kmBase = 0; p.legIn = 0; p.linkIn = [cur, cur]; p.linkReal = true; p.pts = [cur]; p.aprox = false;
      p.lab = 'Dentro del recorrido de ' + PA[p.dentro].n.replace(/ \(.*\)$/, ''); p.from = cur; return;
    }
    const nx = pas.slice(i + 1).find(x => !x.dentro), nxPos = nx ? PA[nx.s].pos : FV.f.pos;
    if (p.cand && p.cand.length) {
      let best = p.cand[0], bc = Infinity;
      p.cand.forEach(id => { const o = opcion(p.s, id), a = o.pts[0], b = o.pts[o.pts.length - 1];
        const c = Math.min(hav(cur, a) + hav(b, nxPos), hav(cur, b) + hav(a, nxPos)); if (c < bc) { bc = c; best = id; } });
      p.ids = [best];
    }
    let pts = [], kmIn = 0, aprox = false;
    const lab = [];
    (p.ids || []).forEach(id => { const op = opcion(p.s, id); if (!op) return; pts = pts.concat(op.pts); kmIn += op.km; aprox = aprox || op.aprox; lab.push(op.l); });
    if (pts.length > 1) {
      const a = pts[0], b = pts[pts.length - 1];
      if (hav(cur, b) + hav(a, nxPos) < hav(cur, a) + hav(b, nxPos)) pts = pts.slice().reverse();
      if (get('ruta.inv.' + p.s + '.' + p.k, false)) pts = pts.slice().reverse();
    }
    if (!pts.length) {
      const nx = pas[i + 1] ? PA[pas[i + 1].s].pos : FV.f.pos;
      let qq = PA[p.s].pos, bq = Infinity;
      (ANC[p.s] || []).forEach(a => { const c = hav(cur, a) + hav(a, nx); if (c < bq) { bq = c; qq = a; } });
      pts = [qq]; aprox = true;
    }
    const en = enlace(cur, pts[0]);
    p.kmBase = kmIn; p.legIn = en.km; p.linkIn = en.pts; p.linkReal = en.real; p.pts = pts; p.aprox = aprox; p.lab = lab.join(' + ');
    p.from = cur; cur = pts[pts.length - 1];
  });
  const envu = enlace(cur, FV.f.pos), vuelta = envu.km;
  pas.forEach((p, i) => { p.km = p.kmBase + (i ? p.legIn / 2 : p.legIn) + (pas[i + 1] ? pas[i + 1].legIn / 2 : vuelta); });
  pas.forEach((p, i) => { if (p.dentro && i) { pas[i - 1].km += p.km; p.km = 0; } });
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
  if (vistos.includes('argelia')) avisos.push('<strong>Argelia</strong>: visado consular, seguro local (la carta verde no vale) y escolta obligatoria en el sur.');
  if (FALLO.size && pas.some(p => !p.linkReal && !p.dentro)) avisos.push('Sin respuesta del servidor de rutas (¿sin conexión?): los enlaces discontinuos del mapa son línea recta × 1,25 y sus km, aproximados.');
  const paso = vistos.filter(s => !sel.has(s) && !PA[s].solo_paso);
  if (paso.length) avisos.push(`De paso obligado, sin marcar: ${paso.map(s => PA[s].n).join(', ')}. Cuentan sus km, su visado y sus tasas.`);
  return {sel, o, pas, avisos, DD, FI, FV, linkVuelta: envu.pts, linkVueltaReal: envu.real,
    aproximados: pas.filter(p => !p.linkReal).length + (envu.real ? 0 : 1)};
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
    <label>CPD: aval inmovilizado (€) ${inp(v.id+'.cpd_aval', v.cpd_aval, 100)}</label></div>`).join('');
  const eu = {es: 'España', fr: 'Francia', it: 'Italia'};
  $('bud-ferry-todos').innerHTML = FER.map(f => `<tr><td><strong>${f.origen} → ${f.puerto}</strong> <small>(${PA[f.pais].n})</small><span class="nota">${escH(f.naviera)} · ${escH(f.frec)} · ${escH(f.nota)} · <a href="${f.fuente}" target="_blank" rel="noopener">fuente</a></span></td>
    <td class="n">${num(f.h, f.h % 1 ? 1 : 0)}</td><td class="n">${num(f.km_eu)}</td><td class="n">${eur(f.coche_ida)} / ${eur(f.coche_vuelta)}</td><td class="n">${eur(f.pax)}</td></tr>`).join('');
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

function paintAdd(R){
  const en = new Set(R.pas.map(p => p.s));
  const grupos = RU.grupos.map(([g, lab]) => {
    const ss = Object.keys(PA).filter(x => PA[x].r === g && !PA[x].solo_paso && !PA[x].ex && !R.sel.has(x)).sort((a, b) => PA[a].n.localeCompare(PA[b].n, 'es'));
    if (!ss.length) return '';
    return `<optgroup label="${escH(lab)}">${ss.map(x => `<option value="${x}">${escH(PA[x].n)}${en.has(x) ? ' (ya se cruza)' : ''}${PA[x].cf ? ' · conflicto' : ''}</option>`).join('')}</optgroup>`;
  }).join('');
  paint('ruta-add', `<option value="">＋ Añadir un país…</option>${grupos}`);
}

function aviso(t){ const m = $('bud-msg'); if (!m) return; m.innerHTML = t; m.hidden = !t; clearTimeout(aviso.t); if (t) aviso.t = setTimeout(() => { m.hidden = true; }, 9000); }

function agregar(s){
  if (!PA[s] || PA[s].solo_paso) return;
  const sel = selSet(), ev = evitarSet();
  sel.add(s); ev.delete(s);
  Object.keys(S).filter(k => ['ruta.modo.', 'ruta.rec.', 'ruta.inv.'].some(x => k.startsWith(x + s + '.'))).forEach(k => delete S[k]);
  S['ruta.sel'] = [...sel]; S['ruta.evitar'] = [...ev]; save();
  compute();
  const R1 = window.__A27_BUDGET_RESULT.ruta, m = mitadDe(R1, s);
  aviso(`<strong>${PA[s].n}</strong> añadido a la ${m || 'ruta'}.${PA[s].cf ? ' Ojo: país en conflicto.' : ''}`
    + (m ? ` <button type="button" class="lnk" data-mitad="${s}">Pasarlo a la ${m === 'ida' ? 'vuelta' : 'ida'}</button>` : ''));
}
// ------------------------------------------------------------------ ida y vuelta
// La ida acaba en el país más alejado del puerto de llegada a África; lo que
// viene después es la vuelta. Sirve para decir en qué mitad va cada país y
// para pasarlo de una a otra sin tener que arrastrarlo.
function giro(R){
  let far = -1, fi = -1;
  R.pas.forEach((p, i) => { const d = hav(R.FI.f.pos, PA[p.s].pos); if (d > far) { far = d; fi = i; } });
  let tIdx = -1;
  R.pas.forEach((p, i) => { if (i <= fi && p.oi != null) tIdx = Math.max(tIdx, p.oi); });
  return {fi, tIdx};
}
function mitadDe(R, s){
  const i = R.o.indexOf(s); if (i < 0) return '';
  const g = giro(R), pi = R.pas.findIndex(p => p.oi === i);
  return pi < 0 ? '' : (pi <= g.fi ? 'ida' : 'vuelta');
}
function moverMitad(s){
  const R = window.__A27_BUDGET_RESULT.ruta, i = R.o.indexOf(s), m = mitadDe(R, s);
  if (i <= 0 || i >= R.o.length - 1 || !m) { aviso(`<strong>${PA[s].n}</strong> es el primer o el último país: se mueve arrastrándolo.`); return; }
  const g = giro(R), sin = R.o.filter(x => x !== s), t = i <= g.tIdx ? g.tIdx - 1 : g.tIdx;
  const js = [];
  if (m === 'ida') for (let j = t + 1; j <= sin.length - 1; j++) js.push(j);
  else for (let j = 1; j <= t + 1; j++) js.push(j);
  let best = null, bk = Infinity;
  js.forEach(j => { const c = sin.slice(0, j).concat([s], sin.slice(j)), k = kmReales(c, R.DD); if (k < bk) { bk = k; best = c; } });
  if (!best) return;
  Object.keys(S).filter(k => ['ruta.modo.', 'ruta.rec.', 'ruta.inv.', 'ruta.d.'].some(x => k.startsWith(x + s + '.'))).forEach(k => delete S[k]);
  S['ruta.orden'] = best; S['ruta.sel'] = [...selSet()]; save(); compute();
  const m2 = mitadDe(window.__A27_BUDGET_RESULT.ruta, s);
  aviso(`<strong>${PA[s].n}</strong> pasa a la ${m2}.` + (m2 === m ? ' (No hay un hueco mejor en la otra mitad: arrástralo a mano.)' : ''));
}
function quitar(s){
  const R0 = window.__A27_BUDGET_RESULT.ruta, sel = selSet(), ev = evitarSet();
  sel.delete(s); ev.add(s);
  const o = R0.o.filter(x => x !== s), full = o;
  const D1 = makeDist(grafo(sel, false, ev), full);
  let corte = null;
  for (let i = 0; i < full.length - 1 && !corte; i++) if (full[i] !== full[i + 1] && !D1.path(full[i], full[i + 1])) corte = [full[i], full[i + 1]];
  Object.keys(S).filter(k => ['ruta.modo.', 'ruta.rec.', 'ruta.inv.', 'ruta.d.'].some(x => k.startsWith(x + s + '.'))).forEach(k => delete S[k]);
  if (corte) {
    ev.delete(s);
    aviso(`<strong>${PA[s].n}</strong> no se puede quitar del todo: es el único camino por carretera entre ${PA[corte[0]].n} y ${PA[corte[1]].n}. Queda como <strong>solo cruzar</strong>, lo más rápido posible.`);
  } else aviso(`<strong>${PA[s].n}</strong> quitado de la ruta.`);
  S['ruta.sel'] = [...sel]; S['ruta.evitar'] = [...ev]; S['ruta.orden'] = o; save(); compute();
}

// ------------------------------------------------------------------ mapa
let MAP = null, CAPA = null, PAISES = null, ENCUADRADO = false, ULTIMA = null;
function estiloPaises(R){
  ULTIMA = R;
  if (!PAISES) return;
  const para = new Set(R.pas.filter(p => p.tipo === 'visita').map(p => p.s)), cruza = new Set(R.pas.map(p => p.s));
  PAISES.eachLayer(l => {
    const s = l.feature.properties.slug, P0 = PA[s];
    let st = {weight: 1, color: '#8A949A', fillColor: '#ffffff', fillOpacity: .05, dashArray: null};
    let txt = P0 ? P0.n + ' · toca para añadir' : '';
    if (!P0) st.fillOpacity = 0;
    else if (para.has(s)) { st = {...st, fillColor: '#1E7A8A', fillOpacity: .45, color: '#1E7A8A'}; txt = P0.n + ' · se para · toca para quitar'; }
    else if (cruza.has(s)) { st = {...st, fillColor: '#D97B29', fillOpacity: .35, color: '#C47F17'}; txt = P0.n + ' · solo se cruza · toca para ' + (R.sel.has(s) ? 'quitar' : 'añadir'); }
    else if (P0.cf) { st = {...st, fillColor: '#B43A3A', fillOpacity: .12, dashArray: '3 4'}; txt = P0.n + ' · en conflicto · toca para añadir (con aviso)'; }
    l.setStyle(st);
    if (txt) l.bindTooltip(txt, {sticky: true});
  });
}
function paintMapa(R){
  if (typeof L === 'undefined' || !$('bud-mapa')) return;
  try {
    if (!MAP) {
      MAP = L.map('bud-mapa', {scrollWheelZoom: false, zoomSnap: 0.25}).setView([2, 18], 3);
      L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {maxZoom: 12, attribution: 'Tiles © Esri'}).addTo(MAP);
      PAISES = L.geoJSON(null, {style: () => ({weight: 1, color: '#8A949A', fillOpacity: .05, fillColor: '#ffffff'}),
        onEachFeature: (f, lay) => { const s = f.properties.slug; if (!PA[s]) return;
          lay.on('click', () => { const R = window.__A27_BUDGET_RESULT.ruta; if (R.sel.has(s)) quitar(s); else agregar(s); }); }}).addTo(MAP);
      CAPA = L.layerGroup().addTo(MAP);
      const raiz = (document.querySelector('script[src*="assets/js/presupuesto.js"]') || {}).src || '';
      fetch(raiz.replace(/presupuesto\.js.*$/, 'africa.geo.json')).then(r => r.json()).then(g => { PAISES.addData(g); if (ULTIMA) estiloPaises(ULTIMA); }).catch(() => {});
    }
    estiloPaises(R);
    CAPA.clearLayers();
    const todos = [R.FI.f.pos, R.FV.f.pos];
    const enl = (pts, real) => { if (pts && pts.length > 1 && hav(pts[0], pts[pts.length - 1]) > 1) L.polyline(pts, {color: '#5F6B72', weight: real ? 2.5 : 2, dashArray: real ? null : '5 6', opacity: .85}).addTo(CAPA)
      .bindTooltip(real ? 'Enlace por carretera' : 'Enlace aproximado (línea recta): falta la ruta por carretera'); };
    R.pas.forEach(p => {
      if (p.dentro) return;
      enl(p.linkIn, p.linkReal);
      if (p.pts.length > 1) L.polyline(p.pts, {color: p.tipo === 'visita' ? '#1E7A8A' : '#D97B29', weight: p.tipo === 'visita' ? 3.5 : 3})
        .addTo(CAPA).bindTooltip(PA[p.s].n + (p.lab ? ' · ' + p.lab : '') + (p.tipo === 'visita' ? '' : ' (solo cruzar)'));
      todos.push(...p.pts);
    });
    enl(R.linkVuelta, R.linkVueltaReal);
    const puertos = R.FI.f.id === R.FV.f.id ? [[R.FI.f, 'Llegada y salida']] : [[R.FI.f, 'Llegada'], [R.FV.f, 'Salida']];
    puertos.forEach(([f, t]) => L.marker(f.pos, {icon: L.divIcon({className: 'bud-mk', html: '⛴', iconSize: [26, 26]})}).addTo(CAPA)
      .bindTooltip(`${t}: ${f.puerto} (ferry ${f.origen})`));
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
  const medio = h => Math.max(0.5, Math.ceil(h / 24 * 2) / 2);
  const FE = [['ida', R.FI], ['vuelta', R.FV]].map(([dir, x]) => ({dir, f: x.f, auto: x.auto, km: x.f.km_eu,
    dias: x.f.km_eu / rt + medio(x.f.h), diasFerry: medio(x.f.h), precios: D.vehiculos.map(v => precioFerry(x.f, dir, v).eur)}));
  const kmEU = FE.reduce((t, e) => t + e.km, 0), diasEU = FE.reduce((t, e) => t + e.dias, 0);
  kmTot += kmEU; diasRuta += diasEU;
  const margen = V('ruta.margen', RU.margen) / 100, fijos = V('ruta.dias_fijos', 0);
  const diasCalc = Math.ceil(diasRuta * (1 + margen));
  const dias = fijos > 0 ? fijos : diasCalc;
  const salida = get('ruta.salida', RU.salida) || RU.salida;
  const regreso = addDays(salida, dias), previsto = iso2d(RU.regreso);
  const diasPrev = Math.round((previsto - iso2d(salida)) / 864e5);
  // ---- Países e itinerario
  paintAdd(R);
  const vecesPais = {}; R.pas.forEach(p => { vecesPais[p.s] = (vecesPais[p.s] || 0) + 1; });
  const G = giro(R);
  const rows = R.pas.map((p, i) => {
    const P0 = PA[p.s], parar = p.tipo === 'visita';
    const dir = vecesPais[p.s] > 1 ? p.k + 'ª vez' : '';
    const sub = p.dentro ? escH(p.lab) + ': se cruza sin salir del recorrido; cuenta su visado, sus tasas y una entrada'
      : parar ? (P0.solo_paso ? escH(p.lab) : (p.aprox ? 'km aproximados' : '')) : (p.marcado ? 'Solo cruzar' + (p.lab ? ': ' + escH(p.lab) : ', lo más rápido posible') : (P0.solo_paso ? escH(p.lab) : 'Paso obligado para llegar al siguiente país'));
    const fijo = P0.solo_paso || p.dentro;
    const rec = get('ruta.rec.' + p.s + '.' + p.k, ''), md = get('ruta.modo.' + p.s + '.' + p.k, null), inv = !!get('ruta.inv.' + p.s + '.' + p.k, false);
    const val = rec && parar ? rec : (md === 'c' ? 'x' : '');
    const ops = P0.opts.map(o => [o.id, 'Recorrido ' + o.id + ' · ' + (o.l.length > 70 ? o.l.slice(0, 68) + '…' : o.l)]);
    if (opcion(p.s, 'A') && opcion(p.s, 'B') && !opcion(p.s, 'A+B')) ops.push(['A+B', 'Recorridos A y B seguidos']);
    const recSel = fijo ? '' : `<div class="it-rec"><select data-rec="${p.s}|${p.k}" aria-label="Ruta en ${escH(P0.n)}" class="${val ? 'edited' : ''}">
      <option value="" ${val ? '' : 'selected'}>Automática${val ? '' : ' · ' + (parar ? escH(p.lab.length > 60 ? p.lab.slice(0, 58) + '…' : p.lab) : 'solo cruzar')}</option>
      ${ops.map(([v, l]) => `<option value="${v}" ${val === v ? 'selected' : ''}>${escH(l)}</option>`).join('')}
      <option value="x" ${val === 'x' ? 'selected' : ''}>Solo cruzar, lo más directo</option></select>`
      + (p.pts.length > 1 ? `<button type="button" class="mv inv" data-inv="${p.s}|${p.k}" aria-pressed="${inv}" title="Recorrerlo en sentido contrario" aria-label="Recorrer ${escH(P0.n)} en sentido contrario">⇄</button>` : '')
      + (val || inv ? '<span class="it-man">manual</span>' : '') + '</div>';
    const seg = fijo ? `<span class="seg-fijo">${p.dentro ? 'Dentro de ' + escH(PA[p.dentro].n.replace(/ \(.*\)$/, '')) : 'Solo cruzar'}</span>`
      : `<div class="seg" role="group" aria-label="Qué hacer en ${escH(P0.n)}"><button type="button" data-modo="${p.s}|${p.k}|p" aria-pressed="${parar}">Parar</button><button type="button" data-modo="${p.s}|${p.k}|c" aria-pressed="${!parar}">Cruzar</button></div>`;
    const mv = p.oi != null ? `<button type="button" class="mv" data-mv="${p.oi},-1" ${p.oi === 0 ? 'disabled' : ''} title="Antes" aria-label="Mover ${escH(P0.n)} antes">↑</button><button type="button" class="mv" data-mv="${p.oi},1" ${p.oi === R.o.length - 1 ? 'disabled' : ''} title="Después" aria-label="Mover ${escH(P0.n)} después">↓</button>` : '';
    const mit = p.oi != null && p.oi > 0 && p.oi < R.o.length - 1 ? `<button type="button" class="mv mit" data-mitad="${p.s}" title="Pasar ${escH(P0.n)} a la ${i <= G.fi ? 'vuelta' : 'ida'}">${i <= G.fi ? 'a vuelta' : 'a ida'}</button>` : '';
    const x = fijo ? '' : `<button type="button" class="mv x" data-quitar="${p.s}" title="Quitar ${escH(P0.n)} de la ruta" aria-label="Quitar ${escH(P0.n)} de la ruta">✕</button>`;
    const dv = get(p.dkey, '');
    const asa = p.oi != null ? `<span class="it-h" title="Arrastra para cambiar el orden" aria-hidden="true">⠿</span>` : '<span class="it-h vacio"></span>';
    return `<li class="it ${parar ? 'para' : 'cruza'}" ${p.oi != null ? 'data-oi="' + p.oi + '"' : ''}>${asa}<span class="it-n">${i + 1}</span>
      <div class="it-p"><strong>${escH(P0.n)}</strong>${dir ? ' <span class="it-dir">' + dir + '</span>' : ''}<span class="nota">${sub}</span>${recSel}</div>
      <div class="it-seg">${seg}</div>
      <div class="it-km"><span data-o="km${i}"></span> <small>km</small></div>
      <div class="it-d"><input type="number" step="0.5" min="0" data-k="${p.dkey}" data-d="" value="${dv}" class="${dv !== '' ? 'edited' : ''}" data-o="dp${i}" autocomplete="off" data-1p-ignore data-lpignore="true" aria-label="Días en ${escH(P0.n)}"> <small>días</small></div>
      <div class="it-act">${mv}${mit}${x}</div></li>` + (i === G.fi && i < R.pas.length - 1 ? `<li class="it-sep" aria-hidden="true">Vuelta · desde ${escH(PA[p.s].n.replace(/ \(.*\)$/, ''))}</li>` : '');
  });
  paint('bud-itin', rows.join(''));
  FE.forEach(e => {
    const f = e.f, opts = FER_PAISES.map(pp => `<optgroup label="${escH(PA[pp].n)}">${FER.filter(x => x.pais === pp).map(x => `<option value="${x.id}" ${!e.auto && x.id === f.id ? 'selected' : ''}>${escH(x.origen)} → ${escH(x.puerto)} · ${escH(x.naviera)}</option>`).join('')}</optgroup>`).join('');
    const extremo = e.dir === 'ida' ? R.o[0] : R.o[R.o.length - 1], pais = PA[f.pais].n;
    const sinFerry = extremo && extremo !== f.pais ? ` · ${PA[extremo].n} no tiene ferry: ${e.dir === 'ida' ? 'se entra' : 'se sale'} por ${pais} y se sigue por carretera` : '';
    const precio = D.vehiculos.reduce((t, v) => t + precioFerry(f, e.dir, v).eur, 0);
    const txt = e.dir === 'ida'
      ? `<strong>Salida</strong> · ${RU.origen}${f.km_eu ? ' → ' + num(f.km_eu) + ' km por carretera hasta ' + f.origen : ''} → ferry ${f.origen} – ${f.puerto}`
      : `<strong>Regreso</strong> · ferry ${f.puerto} – ${f.origen}${f.km_eu ? ' → ' + num(f.km_eu) + ' km por carretera hasta ' + RU.origen : ''}`;
    paint('bud-fer-' + e.dir, `<span class="fer-ic" aria-hidden="true">⛴</span><div class="fer-t">${txt}<span class="nota">${escH(f.naviera)} · ${num(f.h, f.h % 1 ? 1 : 0)} h · ${escH(f.frec)} · ${eur(precio)} los dos vehículos · ${num(e.dias, 1)} días${sinFerry}</span></div>
      <label class="fer-sel"><span class="sr">Ferry de ${e.dir}</span><select data-ferry="${e.dir}"><option value="" ${e.auto ? 'selected' : ''}>Automático: según el ${e.dir === 'ida' ? 'primer' : 'último'} país de la lista</option>${opts}</select></label>`);
  });
  R.pas.forEach((p, i) => { const k = q(`[data-o="km${i}"]`); if (k) k.textContent = num(p.kmE); const d = q(`[data-o="dp${i}"]`); if (d) d.placeholder = num(p.diasCalc, 1); });
  $('bud-itin-km').textContent = num(kmTot);
  $('bud-itin-dias').textContent = num(diasRuta, 1);
  if (window.Sortable && !$('bud-itin').__sort) {
    $('bud-itin').__sort = Sortable.create($('bud-itin'), {handle: '.it-h', draggable: 'li.it', animation: 150, ghostClass: 'it-ghost',
      onEnd: () => {
        const R1 = window.__A27_BUDGET_RESULT.ruta, nuevo = [...$('bud-itin').children].map(li => li.dataset.oi).filter(x => x != null && x !== '').map(x => R1.o[+x]);
        $('bud-itin').__h = null; S['ruta.orden'] = nuevo; S['ruta.sel'] = [...selSet()]; save(); compute();
      }});
  }
  paintMapa(R);
  // ---- Por país
  const porPais = {}, orden = [];
  R.pas.forEach(p => { if (!porPais[p.s]) { porPais[p.s] = {km: 0, entradas: 0}; orden.push(p.s); } porPais[p.s].km += p.kmE; porPais[p.s].entradas++; });
  const veh = D.vehiculos.map(v => ({...v, l100: V(v.id+'.l100', v.l100), personas: V(v.id+'.personas', v.personas),
      perros: V(v.id+'.perros', v.perros), ferry: precioFerry(R.FI.f, 'ida', v).eur + precioFerry(R.FV.f, 'vuelta', v).eur}));
  const Rr = {}; veh.forEach(v => Rr[v.id] = {comb:0, vis:0, veh:0, ferry:0, vida:0, perro:0, otros:0, imp:0, litros:0});
  const gasDef = s => { const g = PA[s].gas; return g ? g.eur : RU.gas_sin_dato; };
  const gasKey = s => 'g.' + (s === 'cabinda' ? 'angola' : s);
  const EUN = {es: 'España', fr: 'Francia', it: 'Italia'};
  const euRows = FE.filter(e => e.km > 0).map(e => ({key: 'eu' + e.dir, n: `Carretera en Europa (${e.dir === 'ida' ? RU.origen + ' → ' + e.f.origen : e.f.origen + ' → ' + RU.origen})`, km: e.km, gk: 'g.eu.' + e.f.gas, gd: RU.gas_eu[e.f.gas], nota: 'Precio de ' + EUN[e.f.gas] + ', GlobalPetrolPrices ' + (RU.gpp_fecha || '21-09-2026')}));
  paint('bud-comb', euRows.filter(r => r.key === 'euida').map(r => `<tr><td><strong>${r.n}</strong><span class="nota">${r.nota}</span></td><td class="n" data-o="ck${r.key}"></td><td class="n">${inp(r.gk, r.gd, 0.01)}</td>${D.vehiculos.map(v => `<td class="n" data-o="c${v.id}${r.key}"></td>`).join('')}</tr>`).join('')
    + orden.map(s => `<tr><td><strong>${PA[s].n}</strong>${PA[s].gas ? '' : '<span class="nota">Sin precio publicado: valor genérico</span>'}</td><td class="n" data-o="ck${s}"></td>
    <td class="n">${inp(gasKey(s), gasDef(s), 0.01)}</td>${D.vehiculos.map(v => `<td class="n" data-o="c${v.id}${s}"></td>`).join('')}</tr>`).join('')
    + euRows.filter(r => r.key === 'euvuelta').map(r => `<tr><td><strong>${r.n}</strong><span class="nota">${r.nota}</span></td><td class="n" data-o="ck${r.key}"></td><td class="n">${inp(r.gk, r.gd, 0.01)}</td>${D.vehiculos.map(v => `<td class="n" data-o="c${v.id}${r.key}"></td>`).join('')}</tr>`).join(''));
  euRows.forEach(r => { const pr = V(r.gk, r.gd); q(`[data-o="ck${r.key}"]`).textContent = num(r.km);
    veh.forEach(v => { const l = r.km * v.l100 / 100, e = l * pr; Rr[v.id].comb += e; Rr[v.id].litros += l; q(`[data-o="c${v.id}${r.key}"]`).innerHTML = `${eur(e)}<span class="nota">${num(l)} L</span>`; }); });
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
  // ---- Ferris elegidos
  paint('bud-ferry-sel', FE.map(e => `<tr><td><strong>${e.dir === 'ida' ? 'Ida' : 'Vuelta'}: ${e.dir === 'ida' ? e.f.origen + ' → ' + e.f.puerto : e.f.puerto + ' → ' + e.f.origen}</strong><span class="nota">${escH(e.f.naviera)} · ${num(e.f.h, e.f.h % 1 ? 1 : 0)} h · ${e.auto ? 'elegido automáticamente' : 'elegido a mano'}</span></td>
    ${D.vehiculos.map(v => { const pf = precioFerry(e.f, e.dir, v); return `<td class="n">${inp(pf.k, pf.dflt, 1)}</td>`; }).join('')}</tr>`).join('')
    + `<tr><td>Perro (dos trayectos, estimación)</td>${veh.map(v => `<td class="n">${eur(v.perros ? 2 * D.perro_ferry * v.perros : 0)}</td>`).join('')}</tr>`);
  D.vehiculos.forEach(v => FE.forEach(e => { const pf = precioFerry(e.f, e.dir, v), el = q(`[data-k="${pf.k}"]`); if (el && !(pf.k in S)) { el.value = pf.dflt; el.dataset.d = pf.dflt; } }));
  // ---- Visados
  const nPers = veh.reduce((s, v) => s + v.personas, 0);
  const conVis = orden.filter(s => PA[s].vis !== 'sin'), sinVis = orden.filter(s => PA[s].vis === 'sin' && !PA[s].solo_paso);
  paint('bud-visados', conVis.map(s => { const vi = PA[s].vis;
    return `<tr><td><strong>${PA[s].n}</strong><span class="nota">${vi ? escH(vi.txt) + ' · <a href="' + vi.url + '" target="_blank" rel="noopener">fuente</a>' : 'Sin importe localizado'}</span>${vi && vi.aviso ? '<span class="nota bud-aviso-fuente">⚠ La fuente oficial cambió el ' + escH(vi.aviso) + ': revisar el importe</span>' : ''}</td>
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
  const ritmoNec = (kmTot - kmEU) / Math.max(1, diasPrev / (1 + margen) - diasEU);
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
  setTimeout(estadoViaje, 0);
  publicarResumen(R, FE, dias, diasRuta, salida, kmTot);
  window.__A27_BUDGET_RESULT = {R: Rr, total, kmTot, veh, dias, diasCalc, diasRuta, fijos, margen, salida, regreso: fecha(regreso),
    ruta: R, porPais, orden, combOut, visOut, tasOut, factor, desv, rv, rt, FE, euRows, kmEU, diasEU};
}

// Resumen del viaje para las fichas, el portal y el mapa general (misma web,
// mismo navegador). Solo describe la ruta; no guarda precios.
const RKEY = 'a27-ruta-resumen';
function nombreViaje(){
  const V = leerViajes(), cur = viajeActual();
  return cur && V[cur] ? cur + (JSON.stringify(V[cur].S) === JSON.stringify(S) ? '' : ' (con cambios)') : (Object.keys(S).length ? 'Viaje sin guardar' : 'Ruta planificada');
}
function publicarResumen(R, FE, dias, diasRuta, salida, kmTot){
  try {
    const f = diasRuta > 0 ? dias / diasRuta : 1, iso = d => d.toISOString().slice(0, 10);
    const nombre = nombreViaje();
    let t = FE[0].dias * f;
    const nom = s => PA[s].n.replace(/ \(.*\)$/, '');
    const pasos = R.pas.map((p, i) => {
      const ent = iso(addDays(salida, t)); t += p.dias * f;
      const prev = R.pas[i - 1], next = R.pas[i + 1];
      return {s: p.s, f: p.s === 'cabinda' ? 'angola' : p.s, n: PA[p.s].n, nf: nom(p.s === 'cabinda' ? 'angola' : p.s), k: p.k, tipo: p.tipo, lab: p.lab || '',
        de: prev ? nom(prev.s) : 'ferry desde ' + FE[0].f.origen, a: next ? nom(next.s) : 'ferry a ' + FE[1].f.origen,
        ent, sal: iso(addDays(salida, t)), d: Math.round(p.dias * f * 10) / 10, km: Math.round(p.kmE)};
    });
    const linea = [];
    const push = q => { const x = [Math.round(q[0] * 100) / 100, Math.round(q[1] * 100) / 100], u = linea[linea.length - 1]; if (!u || u[0] !== x[0] || u[1] !== x[1]) linea.push(x); };
    push(FE[0].f.pos); R.pas.forEach(p => { (p.linkIn || []).forEach(push); p.pts.forEach(push); }); (R.linkVuelta || []).forEach(push); push(FE[1].f.pos);
    localStorage.setItem(RKEY, JSON.stringify({v: 1, nombre, origen: RU.origen, salida, regreso: iso(addDays(salida, dias)), dias, km: Math.round(kmTot),
      ida: FE[0].f.origen + ' → ' + FE[0].f.puerto, vuelta: FE[1].f.puerto + ' → ' + FE[1].f.origen, pasos, linea, hecho: new Date().toISOString()}));
  } catch(e) {}
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

// ------------------------------------------------------------------ viajes guardados
// Se guardan en este navegador (localStorage) y se pueden pasar a otro
// dispositivo con «Descargar mis viajes» / «Importar».
const VKEY = 'a27-viajes-v1', VCUR = 'a27-viaje-actual';
const ORIGINAL = '__original__';
function leerViajes(){ try { return JSON.parse(localStorage.getItem(VKEY) || '{}') || {}; } catch(e) { return {}; } }
function escribirViajes(v){ try { localStorage.setItem(VKEY, JSON.stringify(v)); return true; } catch(e) { return false; } }
function viajeActual(){ try { return localStorage.getItem(VCUR) || ''; } catch(e) { return ''; } }
function marcarActual(n){ try { if (n) localStorage.setItem(VCUR, n); else localStorage.removeItem(VCUR); } catch(e) {} }
function resumenViaje(r){ return r ? `${num(r.km)} km · ${num(r.dias)} días · ${eur(r.total)}` : ''; }
function paintViajes(){
  const sel = $('viaje-sel'); if (!sel) return;
  const V = leerViajes(), cur = viajeActual();
  const nombres = Object.keys(V).sort((a, b) => (V[b].fecha || '').localeCompare(V[a].fecha || ''));
  sel.innerHTML = `<option value="${ORIGINAL}">Ruta planificada (valores iniciales)</option>`
    + nombres.map(n => `<option value="${escH(n)}" ${n === cur ? 'selected' : ''}>${escH(n)} — ${resumenViaje(V[n].r)}</option>`).join('');
  estadoViaje();
}
function estadoViaje(){
  try { const r = JSON.parse(localStorage.getItem(RKEY) || 'null'); if (r && r.nombre !== nombreViaje()) { r.nombre = nombreViaje(); localStorage.setItem(RKEY, JSON.stringify(r)); } } catch(e) {}
  const el = $('viaje-actual'); if (!el) return;
  const V = leerViajes(), cur = viajeActual();
  if (!cur || !V[cur]) { el.textContent = Object.keys(S).length ? 'Configuración sin guardar.' : 'Ruta planificada, sin cambios.'; return; }
  const igual = JSON.stringify(V[cur].S) === JSON.stringify(S);
  el.innerHTML = `Viaje actual: <strong>${escH(cur)}</strong>${igual ? '' : ' · <em>con cambios sin guardar</em>'}`;
  if (!$('viaje-nombre').value) $('viaje-nombre').value = cur;
}
function aplicarEstado(nuevo){
  S = JSON.parse(JSON.stringify(nuevo || {})); save();
  ['bud-itin','bud-comb','bud-visados','bud-tasas','ruta-add','bud-precios','bud-ferry-sel','bud-fer-ida','bud-fer-vuelta'].forEach(id => { if ($(id)) $(id).__h = null; });
  paintStatic(); compute();
}
function guardarViaje(){
  const n = ($('viaje-nombre').value || '').trim() || ('Viaje ' + new Date().toLocaleDateString('es-ES'));
  const V = leerViajes(), existia = n in V, R = window.__A27_BUDGET_RESULT;
  V[n] = {S: JSON.parse(JSON.stringify(S)), fecha: new Date().toISOString(), r: R ? {km: Math.round(R.kmTot), dias: R.dias, total: Math.round(R.total)} : null};
  if (!escribirViajes(V)) { aviso('No se ha podido guardar: este navegador no deja guardar datos (¿modo privado?).'); return; }
  marcarActual(n); $('viaje-nombre').value = n; paintViajes();
  aviso(`${existia ? 'Actualizado' : 'Guardado'} el viaje <strong>${escH(n)}</strong>.`);
}
function cargarViaje(){
  const n = $('viaje-sel').value;
  if (n === ORIGINAL) { marcarActual(''); $('viaje-nombre').value = ''; aplicarEstado({}); paintViajes(); aviso('Cargada la ruta planificada con los valores iniciales.'); return; }
  const V = leerViajes(); if (!V[n]) return;
  marcarActual(n); $('viaje-nombre').value = n; aplicarEstado(V[n].S); paintViajes();
  aviso(`Cargado el viaje <strong>${escH(n)}</strong>.`);
}
function borrarViaje(){
  const n = $('viaje-sel').value, V = leerViajes();
  if (n === ORIGINAL || !V[n]) { aviso('La ruta planificada no se puede borrar.'); return; }
  const b = $('viaje-borrar');
  if (b.dataset.confirmar !== n) { b.dataset.confirmar = n; b.textContent = '¿Borrar «' + n + '»? Toca otra vez'; setTimeout(() => { b.dataset.confirmar = ''; b.textContent = 'Borrar'; }, 5000); return; }
  delete V[n]; escribirViajes(V); if (viajeActual() === n) marcarActual('');
  b.dataset.confirmar = ''; b.textContent = 'Borrar'; paintViajes(); aviso(`Borrado el viaje <strong>${escH(n)}</strong>.`);
}
function exportarViajes(){
  const V = leerViajes();
  if (!Object.keys(V).length) { aviso('Todavía no hay viajes guardados.'); return; }
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([JSON.stringify({tipo: 'africa2027-viajes', version: 1, viajes: V}, null, 1)], {type: 'application/json'}));
  a.download = 'viajes-africa-2027.json'; document.body.appendChild(a); a.click(); a.remove();
}
function importarViajes(file){
  const rd = new FileReader();
  rd.onload = () => {
    try {
      const d = JSON.parse(rd.result), nuevos = d && d.viajes;
      if (!nuevos || typeof nuevos !== 'object') throw new Error('formato');
      const V = leerViajes(); let n = 0;
      Object.entries(nuevos).forEach(([k, v]) => { if (v && v.S) { V[k] = v; n++; } });
      escribirViajes(V); paintViajes(); aviso(`Importados ${n} viajes.`);
    } catch(e) { aviso('Ese archivo no es una copia de viajes de esta app.'); }
  };
  rd.readAsText(file);
}

// ------------------------------------------------------------------ eventos
document.addEventListener('input', e => {
  const k = e.target.dataset.k;
  if (!k) return;
  if (e.target.value === '' && e.target.dataset.d === '') delete S[k]; else S[k] = e.target.value;
  e.target.classList.toggle('edited', e.target.value != e.target.dataset.d); save(); compute();
});
document.addEventListener('change', e => {
  const fd = e.target.dataset.ferry;
  if (fd) { if (e.target.value) S['ruta.ferry_' + fd] = e.target.value; else delete S['ruta.ferry_' + fd]; save(); compute(); return; }
  if (e.target.id === 'ruta-add') { const v = e.target.value; e.target.value = ''; if (v) agregar(v); }
  const rc = e.target.dataset.rec;
  if (rc) {
    const [s, k] = rc.split('|'), v = e.target.value, kr = 'ruta.rec.' + s + '.' + k, km = 'ruta.modo.' + s + '.' + k;
    if (!v) { delete S[kr]; delete S[km]; delete S['ruta.inv.' + s + '.' + k]; }
    else if (v === 'x') { delete S[kr]; S[km] = 'c'; }
    else { S[kr] = v; S[km] = 'p'; }
    save(); compute();
  }
});
document.addEventListener('click', e => {
  const md = e.target.closest('[data-modo]');
  if (md) {
    const [s, k, v] = md.dataset.modo.split('|'), R = window.__A27_BUDGET_RESULT.ruta, p = R.pas.find(x => x.s === s && String(x.k) === k);
    const key = 'ruta.modo.' + s + '.' + k;
    if (p && (v === 'p') === p.def) delete S[key]; else S[key] = v;
    save(); compute(); return;
  }
  const mt = e.target.closest('[data-mitad]');
  if (mt) { moverMitad(mt.dataset.mitad); return; }
  const iv = e.target.closest('[data-inv]');
  if (iv) { const key = 'ruta.inv.' + iv.dataset.inv.replace('|', '.'); if (S[key]) delete S[key]; else S[key] = true; save(); compute(); return; }
  const qx = e.target.closest('[data-quitar]'); if (qx) { quitar(qx.dataset.quitar); return; }
  const b = e.target.closest('[data-mv]'); if (!b) return;
  const [i, d] = b.dataset.mv.split(',').map(Number), o = window.__A27_BUDGET_RESULT.ruta.o.slice(), j = i + d;
  if (j < 0 || j >= o.length) return;
  [o[i], o[j]] = [o[j], o[i]]; S['ruta.orden'] = o; S['ruta.sel'] = [...selSet()]; save(); compute();
});
paintStatic(); compute(); paintViajes();
$('viaje-guardar').addEventListener('click', guardarViaje);
$('viaje-cargar').addEventListener('click', cargarViaje);
$('viaje-borrar').addEventListener('click', borrarViaje);
$('viaje-exportar').addEventListener('click', exportarViajes);
$('viaje-importar').addEventListener('change', e => { if (e.target.files[0]) importarViajes(e.target.files[0]); e.target.value = ''; });
$('viaje-nombre').addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); guardarViaje(); } });
$('ruta-plan').addEventListener('click', () => { Object.keys(S).filter(k => k.startsWith('ruta.') && !RUTA_CFG.includes(k)).forEach(k => delete S[k]); save(); aviso('Vuelta a la ruta de la planificación.'); compute(); });
$('ruta-opt').addEventListener('click', () => { const R = window.__A27_BUDGET_RESULT.ruta; S['ruta.orden'] = optimizar(R.o, R.DD); S['ruta.sel'] = [...R.sel]; save(); compute(); });
$('ruta-none').addEventListener('click', () => { S['ruta.sel'] = []; S['ruta.orden'] = []; S['ruta.evitar'] = []; save(); aviso('Ruta vacía: toca países en el mapa o usa «Añadir un país».'); compute(); });
$('bud-reset').addEventListener('click', () => { marcarActual(''); S = {}; save(); ['bud-itin','bud-comb','bud-visados','bud-tasas','ruta-add','bud-precios'].forEach(id => { $(id).__h = null; }); paintStatic(); compute(); });
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

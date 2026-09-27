/* Planificador por puntos (beta) · África 2027
   El viaje es una lista de puntos (ida y vuelta). La app mete los puestos
   fronterizos, pide la carretera a OSRM, reparte los km por países y cuenta
   los días. Datos: A27_PP (en la página) + planificador-puntos.json (fase 1).
   Todo se guarda en este navegador, aparte del Planificador actual. */
(function(){
'use strict';
const CFG = A27_PP, PA = CFG.paises;
const $ = id => document.getElementById(id);
const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const grp = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
const num = (v, d = 0) => { const [a, b] = Math.abs(Number(v) || 0).toFixed(d).split('.'); return grp(a) + (b ? ',' + b : ''); };
const MES = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
const fecha = (d, y) => d.getUTCDate() + ' ' + MES[d.getUTCMonth()] + (y ? ' ' + d.getUTCFullYear() : '');
const addDays = (iso, n) => { const d = new Date((iso || CFG.salida) + 'T00:00:00Z'); if (isNaN(d)) return new Date(CFG.salida + 'T00:00:00Z'); d.setUTCDate(d.getUTCDate() + Math.round(n)); return d; };
const nom = s => (PA[s] ? PA[s].n : s || '—');
function hav(a, b){
  const p1 = a[0] * Math.PI / 180, p2 = b[0] * Math.PI / 180, dl = (b[1] - a[1]) * Math.PI / 180;
  const h = Math.sin((p2 - p1) / 2) ** 2 + Math.cos(p1) * Math.cos(p2) * Math.sin(dl / 2) ** 2;
  return 2 * 6371 * Math.asin(Math.min(1, Math.sqrt(h)));
}
const F = 1.25;
const SC = document.querySelector('script[src*="assets/js/planificador-puntos.js"]');
const raiz = SC ? SC.getAttribute('src').split('assets/js/')[0] : '../';

// ------------------------------------------------------------------ estado
const KEY = 'a27pp-estado-v1', VKEY = 'a27pp-viajes-v1';
const VACIO = () => ({paises: [], evitar: [], ida: [], vuelta: [], libres: {}, dias: {}, fer_ida: '', fer_vuelta: '', salida: CFG.salida, kmdia: 300, margen: 10, nombre: ''});
let S;
try { S = Object.assign(VACIO(), JSON.parse(localStorage.getItem(KEY) || '{}') || {}); } catch(e) { S = VACIO(); }
if (!Array.isArray(S.evitar)) S.evitar = [];
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch(e) {} };
function msg(t){ const m = $('pp-msg'); m.innerHTML = t; m.hidden = !t; clearTimeout(msg.t); if (t) msg.t = setTimeout(() => { m.hidden = true; }, 4500); }

// ------------------------------------------------------------------ datos
let PROPIOS = {}, PDET = {}, CREANDO = false;
let PUNTOS = {}, PORPAIS = {}, FRPAR = {}, FRTODAS = [], GEO = null, POLIS = [], SINCTRL = new Set();
const GRAFO = {};
CFG.fronteras.forEach(([a, b, t]) => { (GRAFO[a] = GRAFO[a] || []).push([b, t]); (GRAFO[b] = GRAFO[b] || []).push([a, t]); });
function punto(id){
  if (PUNTOS[id]) return PUNTOS[id];
  if (PROPIOS[id]) return PROPIOS[id];
  const l = S.libres[id];
  return l ? {id, libre: true, nombre: l.nombre, pais: l.pais, lat: l.lat, lon: l.lon, dias: 0, cat: 'Paso por aquí', prio: '', perro: 'sin_dato', tiempo: ''} : null;
}
const diasDe = p => (S.dias[p.id] != null && S.dias[p.id] !== '' ? parseFloat(S.dias[p.id]) || 0 : p.dias);

// Polígonos para saber en qué país cae cada punto de la carretera
function prepGeo(g){
  POLIS = g.features.map(f => {
    const polys = f.geometry.type === 'Polygon' ? [f.geometry.coordinates] : f.geometry.coordinates;
    let mnx = 180, mny = 90, mxx = -180, mxy = -90;
    polys.forEach(p => p[0].forEach(([x, y]) => { mnx = Math.min(mnx, x); mxx = Math.max(mxx, x); mny = Math.min(mny, y); mxy = Math.max(mxy, y); }));
    return {s: f.properties.slug, polys, bb: [mnx, mny, mxx, mxy]};
  });
}
function dentro(lat, lon, poly){
  let d = false;
  poly.forEach(anillo => { for (let i = 0, j = anillo.length - 1; i < anillo.length; j = i++) {
    const [xi, yi] = anillo[i], [xj, yj] = anillo[j];
    if ((yi > lat) !== (yj > lat) && lon < (xj - xi) * (lat - yi) / (yj - yi) + xi) d = !d; } });
  return d;
}
const PCACHE = new Map();
function paisDe(lat, lon){
  const k = lat.toFixed(2) + ',' + lon.toFixed(2);
  if (PCACHE.has(k)) return PCACHE.get(k);
  let r = null;
  for (const P of POLIS) { const b = P.bb; if (lon < b[0] || lon > b[2] || lat < b[1] || lat > b[3]) continue;
    if (P.polys.some(p => dentro(lat, lon, p))) { r = P.s; break; } }
  PCACHE.set(k, r); return r;
}

// ------------------------------------------------------------------ carretera (OSRM, cacheada; misma caché que el Planificador)
const LKEY = 'a27-enlaces-v1', OSRM = 'https://router.project-osrm.org/route/v1/driving/';
let ENL = {};
try { ENL = JSON.parse(localStorage.getItem(LKEY) || '{}') || {}; } catch(e) { ENL = {}; }
const COLA = new Map(), FALLO = new Map();
let VUELO = 0, T_REP = null, T_GUARDA = null;
const ck = p => p[0].toFixed(3) + ',' + p[1].toFixed(3);
function enlace(a, b){
  const d = hav(a, b);
  if (d < 1) return {pts: [a, b], km: d, real: true};
  const ka = ck(a), kb = ck(b), inv = ka > kb, key = inv ? kb + '|' + ka : ka + '|' + kb, e = ENL[key];
  // Rodeo absurdo (pista que OpenStreetMap no enlaza o frontera cerrada que sí enlaza):
  // se descarta y queda en línea recta con km estimados.
  if (e && e.km > 2.5 * d + 100) return {pts: [a, b], km: d * F, real: true, rodeo: true};
  if (e) return {pts: inv ? e.p.slice().reverse() : e.p, km: e.km, real: true};
  if (!(Date.now() - (FALLO.get(key) || 0) < 60000) && !COLA.has(key)) { COLA.set(key, inv ? [b, a] : [a, b]); setTimeout(pedir, 0); }
  return {pts: [a, b], km: d * F, real: false};
}
// Tramo con pista conocida: si empieza (o acaba) junto a un extremo de una pista y
// esta le acerca al destino, se sigue la pista y el resto va por carretera.
function tramo(a, b){
  const dab = hav(a, b);
  for (const pi of (CFG.pistas || [])) {
    const P = pi.pts, n = P.length;
    for (const rev of [false, true]) {
      const pts = rev ? P.slice().reverse() : P, E1 = pts[0], E2 = pts[n - 1];
      if (hav(a, E1) <= 40 && hav(E2, b) < dab - 50) {
        const r = enlace(E2, b);
        return {pts: [a, ...pts, ...r.pts.slice(1)], km: hav(a, E1) * F + pi.km + r.km, real: r.real, rodeo: r.rodeo, pista: pi};
      }
      if (hav(b, E2) <= 40 && hav(a, E1) < dab - 50) {
        const r = enlace(a, E1);
        return {pts: [...r.pts, ...pts.slice(1), b], km: r.km + pi.km + hav(E2, b) * F, real: r.real, rodeo: r.rodeo, pista: pi};
      }
    }
  }
  return enlace(a, b);
}
function pedir(){
  while (VUELO < 3 && COLA.size) {
    const [key, [a, b]] = COLA.entries().next().value; COLA.delete(key); VUELO++;
    fetch(OSRM + a[1] + ',' + a[0] + ';' + b[1] + ',' + b[0] + '?overview=simplified&geometries=geojson')
      .then(r => r.ok ? r.json() : Promise.reject(r.status))
      .then(j => { const rt = j.routes && j.routes[0]; if (!rt) throw 0;
        const p = rt.geometry.coordinates.map(c => [Math.round(c[1] * 1e3) / 1e3, Math.round(c[0] * 1e3) / 1e3]);
        ENL[key] = {km: Math.round(rt.distance / 100) / 10, p: [a, ...p.slice(1, -1), b]};
        clearTimeout(T_GUARDA); T_GUARDA = setTimeout(() => { try { localStorage.setItem(LKEY, JSON.stringify(ENL)); } catch(e) {} }, 800); })
      .catch(() => { FALLO.set(key, Date.now()); })
      .finally(() => { VUELO--; clearTimeout(T_REP); T_REP = setTimeout(() => { if (!VUELO && !COLA.size) calcular(); }, 300); pedir(); });
  }
}

// ------------------------------------------------------------------ ferris
function ferrisDe(dir, cerca){
  const man = dir === 'ida' ? S.fer_ida : S.fer_vuelta, f0 = CFG.ferris.find(f => f.id === man);
  if (f0) return {f: f0, auto: false};
  if (!cerca) return {f: CFG.ferris.find(f => f.id === CFG.ferry_pref.marruecos) || CFG.ferris[0], auto: true};
  let best = null, bd = Infinity;
  CFG.ferris.forEach(f => { const d = hav(cerca, f.pos) + (CFG.ferry_pref[f.pais] === f.id ? -60 : 0) + f.km_eu / 1000; if (d < bd) { bd = d; best = f; } });
  return {f: best, auto: true};
}

// ------------------------------------------------------------------ camino entre países y puestos fronterizos
function caminoPaises(a, b){
  if (a === b) return [a];
  const act = new Set(S.paises), ev = new Set(S.evitar), dist = {[a]: 0}, prev = {}, hecho = new Set();
  for (;;) {
    let u = null, m = Infinity;
    for (const k in dist) if (!hecho.has(k) && dist[k] < m) { m = dist[k]; u = k; }
    if (u === null || u === b) break;
    hecho.add(u);
    (GRAFO[u] || []).forEach(([v, t]) => {
      if (t === 'cerrada' || !PA[v] || !PA[v].pos || !PA[u] || !PA[u].pos) return;
      const libre = act.has(v) || v === b;
      if ((t === 'evitar' || PA[v].cf) && !libre) return;
      if (ev.has(v) && v !== b) return;
      const w = hav(PA[u].pos, PA[v].pos) * (libre ? 1 : 2.5) + (t === 'ferry' ? 300 : 0);
      if (!(v in dist) || m + w < dist[v]) { dist[v] = m + w; prev[v] = u; }
    });
  }
  if (!(b in dist)) return null;
  const p = [b]; let x = b; while (x !== a) { x = prev[x]; p.unshift(x); }
  return p;
}
function puesto(x, y, desde, hacia){
  const c = FRPAR[x < y ? x + '|' + y : y + '|' + x] || [];
  let best = null, bd = Infinity;
  // Se prefieren los puestos por los que pasan los recorridos de las fichas (pasos
  // oficiales ya estudiados): uno que no está en ningún recorrido cuenta 250 km más.
  c.forEach(f => { const d = hav(desde, [f.lat, f.lon]) + hav([f.lat, f.lon], hacia) + (f.cerca ? 0 : 250); if (d < bd) { bd = d; best = f; } });
  return best;
}

// ------------------------------------------------------------------ la ruta
let R = null;
function calcular(){
  const ida = S.ida.map(punto).filter(Boolean), vuelta = S.vuelta.map(punto).filter(Boolean);
  const todos = ida.concat(vuelta);
  const FI = ferrisDe('ida', todos[0] ? [todos[0].lat, todos[0].lon] : null), FV = ferrisDe('vuelta', todos.length ? [todos[todos.length - 1].lat, todos[todos.length - 1].lon] : null);
  const wp = [{tipo: 'puerto', pos: FI.f.pos, pais: FI.f.pais, mitad: 'ida', nombre: FI.f.puerto}];
  ida.forEach(p => wp.push({tipo: 'punto', p, pos: [p.lat, p.lon], pais: p.pais, mitad: 'ida'}));
  vuelta.forEach(p => wp.push({tipo: 'punto', p, pos: [p.lat, p.lon], pais: p.pais, mitad: 'vuelta'}));
  wp.push({tipo: 'puerto', pos: FV.f.pos, pais: FV.f.pais, mitad: 'vuelta', nombre: FV.f.puerto});
  // Fronteras entre puntos de países distintos
  const seq = [wp[0]], avisos = [];
  for (let i = 1; i < wp.length; i++) {
    const a = seq[seq.length - 1], b = wp[i];
    if (a.pais && b.pais && a.pais !== b.pais) {
      const cam = caminoPaises(a.pais, b.pais);
      if (!cam) avisos.push({rojo: true, t: `No hay camino por carretera permitido entre ${esc(nom(a.pais))} y ${esc(nom(b.pais))} (fronteras cerradas o países en conflicto sin marcar).`});
      else {
        let desde = a.pos;
        for (let k = 0; k < cam.length - 1; k++) {
          if (SINCTRL.has(cam[k] + '|' + cam[k + 1])) continue;
          const f = puesto(cam[k], cam[k + 1], desde, b.pos);
          if (f) { seq.push({tipo: 'frontera', f, pos: [f.lat, f.lon], pais: cam[k + 1], mitad: b.mitad, nombre: f.nombre}); desde = [f.lat, f.lon]; }
        }
      }
    }
    seq.push(b);
  }
  // Tramos por carretera
  const tramos = [];
  for (let i = 1; i < seq.length; i++) { const e = tramo(seq[i - 1].pos, seq[i].pos); tramos.push({a: seq[i - 1], b: seq[i], ...e, mitad: seq[i].mitad}); }
  // Km por país y países atravesados, en orden
  const kmPais = {}, runs = [], kmZona = {};
  const kmdia = Math.max(50, +S.kmdia || 300), margen = Math.max(0, +S.margen || 0) / 100;
  const medio = h => Math.max(0.5, Math.ceil(h / 24 * 2) / 2);
  const dFerry = f => medio(f.h) + f.km_eu / kmdia;
  let kmTot = 0, reloj = dFerry(FI.f);   // días desde la salida (sin margen), para las fechas por país
  tramos.forEach(t => {
    t.kmAcum = kmTot; kmTot += t.km;
    // Los tramos se trocean cada ~25 km para repartir los km por países
    const pts = [t.pts[0]];
    for (let i = 1; i < t.pts.length; i++) { const a = t.pts[i - 1], b = t.pts[i], n = Math.max(1, Math.ceil(hav(a, b) / 25));
      for (let k = 1; k <= n; k++) pts.push([a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n]); }
    const len = pts.reduce((s, q, i) => s + (i ? hav(pts[i - 1], q) : 0), 0) || 1;
    for (let i = 1; i < pts.length; i++) {
      const seg = hav(pts[i - 1], pts[i]), m = [(pts[i - 1][0] + pts[i][0]) / 2, (pts[i - 1][1] + pts[i][1]) / 2];
      // En el mar (ferris, costa) cuenta para el país en el que ya se estaba
      const s = paisDe(m[0], m[1]) || (runs.length ? runs[runs.length - 1].s : t.a.pais);
      const zz = ZONAS.length ? zonaDe(m[0], m[1]) : null; if (zz) kmZona[zz.id] = (kmZona[zz.id] || 0) + seg / len * t.km;
      if (!s) continue;
      const k = seg / len * t.km;
      kmPais[s] = (kmPais[s] || 0) + k;
      reloj += k / kmdia;
      const recta = !t.real || !!t.rodeo;
      if (runs.length && runs[runs.length - 1].s === s) { runs[runs.length - 1].km += k; runs[runs.length - 1].t1 = reloj; }
      else runs.push({s, km: k, recta, t0: reloj - k / kmdia, t1: reloj, puntos: []});   // recta: se entró por un tramo provisional
    }
    // La estancia en un punto cuenta en el país donde está
    if (t.b.tipo === 'punto') { reloj += diasDe(t.b.p); const u = runs[runs.length - 1]; if (u) { u.t1 = reloj; u.puntos.push(t.b.p); } }
  });
  // Un roce de menos de 10 km con otro país (carretera pegada a la frontera) no cuenta como entrada
  // (hasta 25 km y sin paradas: carreteras que siguen la frontera, como la del río Senegal o la península de Nuadibú)
  for (let i = runs.length - 2; i > 0; i--) if (runs[i].km < 25 && !runs[i].puntos.length && runs[i - 1].s === runs[i + 1].s) {
    const a = runs[i - 1]; a.km += runs[i].km + runs[i + 1].km; a.t1 = runs[i + 1].t1; a.puntos = a.puntos.concat(runs[i].puntos, runs[i + 1].puntos); runs.splice(i, 2); }
  const orden = runs.map(x => x.s);
  const entradas = {}; orden.forEach(s => { entradas[s] = (entradas[s] || 0) + 1; });
  const act = new Set(S.paises.concat([FI.f.pais, FV.f.pais]));
  [...new Set(orden)].forEach(s => {
    if (PA[s] && PA[s].cf) avisos.push({rojo: true, t: `La ruta atraviesa <strong>${esc(nom(s))}</strong>: país en conflicto (el MAEC desaconseja el viaje).`});
    else if (!act.has(s) && (kmPais[s] || 0) > 3) avisos.push({rojo: false, t: `La ruta cruza <strong>${esc(nom(s))}</strong> (${num(kmPais[s])} km), que no has marcado: cuenta su visado y su frontera.`});
  });
  for (let i = 1; i < orden.length; i++) {
    const a = orden[i - 1], b = orden[i], e = (GRAFO[a] || []).find(([v]) => v === b);
    // Una línea recta provisional puede rozar un país vecino: no se da por cruzada una frontera cerrada.
    if (e && e[1] === 'cerrada' && !runs[i].recta) avisos.push({rojo: true, t: `La carretera pasa de ${esc(nom(a))} a ${esc(nom(b))} por una frontera <strong>cerrada</strong>.`});
  }
  // Zonas desaconsejadas: puntos dentro y km de carretera dentro
  todos.forEach(p => { const z = zonaDe(p.lat, p.lon); if (z) avisos.push({rojo: z.nivel === 'rojo', t: `<strong>${esc(p.nombre)}</strong> está en una ${z.nivel === 'rojo' ? 'zona roja' : 'zona naranja'}: ${esc(z.nombre)} (FCDO).`}); });
  Object.entries(kmZona).forEach(([id, k]) => { if (k < 3) return; const z = ZONAS.find(x => x.id === id);
    avisos.push({rojo: z.nivel === 'rojo', t: `La carretera pasa ~${num(k)} km por una ${z.nivel === 'rojo' ? '<strong>zona roja</strong>' : 'zona naranja'}: ${esc(z.nombre)} (${esc(nom(z.pais))}, FCDO).`}); });
  // Países que se quieren evitar y por los que aun así pasa la carretera
  [...new Set(orden)].filter(s => S.evitar.includes(s)).forEach(s => avisos.push({rojo: true, t: `La carretera cruza <strong>${esc(nom(s))}</strong>, que quieres evitar: no hay otro camino con estos puntos, o la carretera lo roza. Añade un «pasar por aquí» (clic derecho) para desviarla.`}));
  const sinPerro = todos.filter(p => p.perro === 'no').length;
  if (sinPerro) avisos.push({rojo: false, t: `${sinPerro} punto${sinPerro > 1 ? 's' : ''} donde el perro no puede entrar (marcados en la lista).`});
  const pistas = [...new Set(tramos.filter(t => t.pista).map(t => t.pista))];
  pistas.forEach(pi => avisos.push({rojo: true, t: `Tramo por <strong>${esc(pi.nombre)}</strong> (~${num(pi.km)} km aproximados): ${esc(pi.nota)}.`}));
  const rodeos = tramos.filter(t => t.rodeo).length;
  if (rodeos) avisos.push({rojo: true, t: `${rodeos} tramo${rodeos > 1 ? 's' : ''} sin carretera razonable en el mapa de rutas (daba un rodeo de más del doble, a menudo por una frontera cerrada o una pista sin cartografiar): en línea recta con km estimados. Revisa el paso.`});
  const aprox = tramos.filter(t => !t.real).length;
  if (aprox) avisos.push({rojo: false, t: FALLO.size ? `Sin respuesta del servidor de rutas: ${aprox} tramo${aprox > 1 ? 's' : ''} en línea recta (discontinua) con km aproximados.` : `Calculando la carretera de ${aprox} tramo${aprox > 1 ? 's' : ''}…`});
  // Días y fechas
  let t = dFerry(FI.f);
  const fechaPunto = {};
  tramos.forEach(tr => { t += tr.km / kmdia; if (tr.b.tipo === 'punto') { fechaPunto[tr.b.p.id] = t; t += diasDe(tr.b.p); } });
  const diasPais = {};
  Object.entries(kmPais).forEach(([s, k]) => { diasPais[s] = (diasPais[s] || 0) + k / kmdia; });
  todos.forEach(p => { if (p.pais) diasPais[p.pais] = (diasPais[p.pais] || 0) + diasDe(p); });
  const base = t + dFerry(FV.f), dias = Math.ceil(base * (1 + margen));
  const kmEU = FI.f.km_eu + FV.f.km_eu;
  R = {ida, vuelta, todos, FI, FV, seq, tramos, kmTot, kmEU, kmPais, runs, orden, entradas, avisos, dias, fechaPunto, diasPais, factor: 1 + margen};
  R.colores = {}; [...new Set(runs.map(r => r.s))].forEach((s, i) => { R.colores[s] = PALETA[i % PALETA.length]; });
  R.bud = presupuesto(R);
  publicar(R);
  pintar();
}


// ------------------------------------------------------------------ presupuesto
// Mismo modelo y mismos precios que el Planificador actual. Los ajustes que se
// hacen allí (vehículos, consumos, gasóleo, visados, ferris, parámetros) se
// guardan en 'a27-presupuesto-v1' y se aplican también aquí.
const BUD = CFG.bud, AJ_KEY = 'a27-presupuesto-v1';
const eur = v => { const r = Math.round(v); return (r < 0 ? '−' : '') + grp(Math.abs(r)) + ' €'; };
const CATS = [['comb', 'Combustible', '#1E7A8A'], ['vis', 'Visados', '#2B6CB0'], ['veh', 'Vehículo: CPD, tasas, seguros, mantenimiento', '#C47F17'],
  ['ferry', 'Ferris', '#673AB7'], ['vida', 'Comida, noches y actividades', '#2E7D32'], ['perro', 'Perro', '#8B5A2B'], ['otros', 'Comunicaciones', '#5F6B72'], ['imp', 'Imprevistos', '#B43A3A']];
function ajustes(){ try { return JSON.parse(localStorage.getItem(AJ_KEY) || '{}') || {}; } catch(e) { return {}; } }
function presupuesto(R){
  const A = ajustes(), V = (k, d) => { const x = parseFloat(k in A ? A[k] : d); return isFinite(x) ? x : 0; };
  const factor = V('factor', BUD.factor), desv = V('desvios', BUD.desvios) / 100;
  const veh = BUD.vehiculos.map(v => ({...v, l100: V(v.id + '.l100', v.l100), personas: V(v.id + '.personas', v.personas), perros: V(v.id + '.perros', v.perros),
    cpd: V(v.id + '.cpd_libro', v.cpd_libro) + V(v.id + '.cpd_banco', v.cpd_banco), aval: V(v.id + '.cpd_aval', v.cpd_aval)}));
  const P = {}; BUD.params.forEach(p => { P[p.id] = V('p.' + p.id, p.val); });
  const nPers = veh.reduce((t, v) => t + v.personas, 0), dias = R.dias, meses = dias / 30.4;
  const pb = s => BUD.paises[s] || {};
  // Km y combustible: Europa (ida), África por país, Europa (vuelta)
  const filas = [], vistos = new Set();
  const eu = (dir, f) => f.km_eu > 0 ? {eu: dir, n: dir === 'ida' ? `Europa: ${CFG.origen} → ${f.origen}` : `Europa: ${f.origen} → ${CFG.origen}`, km: f.km_eu * factor, precio: V('g.eu.' + f.gas, BUD.gas_eu[f.gas])} : null;
  const e1 = eu('ida', R.FI.f); if (e1) filas.push(e1);
  R.runs.forEach(r => { if (vistos.has(r.s)) return; vistos.add(r.s);
    const d = pb(r.s).gas;
    filas.push({s: r.s, n: nom(r.s), km: (R.kmPais[r.s] || 0) * factor * (1 + desv), precio: V('g.' + r.s, d != null ? d : BUD.gas_sin_dato), generico: d == null, entradas: R.entradas[r.s] || 1}); });
  const e2 = eu('vuelta', R.FV.f); if (e2) filas.push(e2);
  const litros = filas.reduce((t, f) => t + f.km, 0);   // km totales (cada vehículo los hace todos)
  // Visados y tasas (por entrada)
  let visPP = 0, tasas = 0;
  filas.filter(f => f.s).forEach(f => {
    const b = pb(f.s);
    f.vis = V('vis.' + f.s, b.vis != null ? b.vis : 0); f.visSin = b.vis == null; f.visTxt = b.vis_txt || ''; f.visUrl = b.vis_url || ''; f.visAviso = b.vis_aviso || '';
    f.tasa = V('tasa.' + f.s, b.tasa || 0); f.tasaTxt = b.tasa_txt || '';
    visPP += f.vis * f.entradas; tasas += f.tasa * f.entradas;
  });
  const precioFerry = (f, dir, v) => V('fer.' + f.id + '.' + dir + '.' + v.id, Math.round(((dir === 'ida' ? f.coche_ida : f.coche_vuelta) + Math.max(0, v.personas - 1) * f.pax) * 100) / 100);
  const Rr = {};
  veh.forEach(v => {
    const r = Rr[v.id] = {litros: 0, comb: 0};
    filas.forEach(f => { const l = f.km * v.l100 / 100; r.litros += l; r.comb += l * f.precio; });
    r.vis = visPP * v.personas;
    r.veh = v.cpd + tasas + P.seguros + P.mantenimiento;
    r.ferry = precioFerry(R.FI.f, 'ida', v) + precioFerry(R.FV.f, 'vuelta', v);
    r.vida = P.comida * v.personas * dias + P.noche * dias + P.parques * v.personas;
    r.perro = v.perros ? (P.perro_comida * dias * v.perros + P.perro_tramites * v.perros + 2 * BUD.perro_ferry * v.perros) : 0;
    r.otros = P.comunicaciones * meses;
    const base = r.comb + r.vis + r.veh + r.ferry + r.vida + r.perro + r.otros;
    r.imp = base * P.imprevistos / 100; r.total = base + r.imp;
  });
  const total = veh.reduce((t, v) => t + Rr[v.id].total, 0), aval = veh.reduce((t, v) => t + v.aval, 0);
  const cat = {}; CATS.forEach(([k]) => { cat[k] = veh.reduce((t, v) => t + Rr[v.id][k], 0); });
  const ferris = [['ida', R.FI.f], ['vuelta', R.FV.f]].map(([dir, f]) => ({dir, f, eur: veh.reduce((t, v) => t + precioFerry(f, dir, v), 0)}));
  const nVeh = veh.length, perros = veh.reduce((t, v) => t + v.perros, 0);
  const base = veh.reduce((t, v) => t + Rr[v.id].total - Rr[v.id].imp, 0);
  // Gastos del día a día y fijos: cada parámetro con lo que suma en este viaje
  const gastos = BUD.params.map(p => {
    const x = P[p.id], m = {persona_dia: nPers * dias, perro_dia: perros * dias, vehiculo_dia: nVeh * dias, persona: nPers, perro: perros,
      vehiculo: nVeh, vehiculo_mes: nVeh * meses}[p.ambito];
    return {...p, v: x, total: p.ambito === 'pct' ? base * x / 100 : x * (m || 0),
      como: {persona_dia: `× ${num(nPers)} personas × ${num(dias)} días`, perro_dia: `× ${num(perros)} perro${perros === 1 ? '' : 's'} × ${num(dias)} días`,
        vehiculo_dia: `× ${num(nVeh)} vehículos × ${num(dias)} noches`, persona: `× ${num(nPers)} personas`, perro: `× ${num(perros)} perro${perros === 1 ? '' : 's'}`,
        vehiculo: `× ${num(nVeh)} vehículos`, vehiculo_mes: `× ${num(nVeh)} vehículos × ${num(meses, 1)} meses`, pct: `de ${eur(base)}`}[p.ambito] || ''};
  });
  return {veh, Rr, total, aval, cat, filas, ferris, visPP, tasas, nPers, km: litros, desv, gastos, perros, A, ajustado: Object.keys(A).length > 0};
}
// Tiempo por país: línea del viaje (cada tramo en su país, en orden) y tabla con días,
// entradas, fechas y km de cada país.
function pintarTiempo(){
  const el = $('pp-tiempo'); if (!el) return;
  if (!R || !R.todos.length || !R.runs.length) { el.innerHTML = ''; return; }
  const f = R.factor, ini = R.runs[0].t0, fin = R.runs[R.runs.length - 1].t1, total = Math.max(1e-6, R.dias);
  const dF1 = ini * f, dF2 = Math.max(0, total - fin * f);
  const ancho = el.clientWidth || 900;
  const seg = (d, html, st, tt) => `<i style="width:${d / total * 100}%;${st}" data-tt="${esc(tt)}">${d / total * ancho > html.replace(/<[^>]+>/g, '').length * 6.6 + 10 ? html : ''}</i>`;
  const tl = seg(dF1, 'Ferry', '', `Salida y ferry ${R.FI.f.origen} → ${R.FI.f.puerto}: ~${num(dF1, 1)} días`).replace('<i ', '<i class="fer" ')
    + R.runs.map(r => { const d = (r.t1 - r.t0) * f; return seg(d, esc(nom(r.s)) + ' · ' + num(d, d < 10 ? 1 : 0) + ' d', `background:${colPais(r.s)}`,
      `${nom(r.s)}: ${fecha(addDays(S.salida, r.t0 * f))} – ${fecha(addDays(S.salida, r.t1 * f))} · ~${num(d, 1)} días · ${num(r.km)} km${r.puntos.length ? ' · paradas: ' + r.puntos.map(p => p.nombre.split(' · ')[0]).join(', ') : ' · de paso, sin paradas'}`); }).join('')
    + seg(dF2, 'Ferry', '', `Ferry ${R.FV.f.puerto} → ${R.FV.f.origen} y regreso: ~${num(dF2, 1)} días`).replace('<i ', '<i class="fer" ');
  const por = {}, orden = [];
  R.runs.forEach(r => { const d = (r.t1 - r.t0) * f;
    if (!por[r.s]) { por[r.s] = {d: 0, km: 0, n: 0, rangos: [], puntos: 0}; orden.push(r.s); }
    const x = por[r.s]; x.d += d; x.km += r.km; x.n++; x.puntos += r.puntos.length; const a = fecha(addDays(S.salida, r.t0 * f)), b = fecha(addDays(S.salida, r.t1 * f)); x.rangos.push(a === b ? a : a + '–' + b); });
  const filas = orden.map(s => { const x = por[s];
    return `<tr><td><i style="background:${colPais(s)}"></i>${esc(nom(s))}${x.puntos ? '' : ' <small style="color:var(--ink-soft)">de paso</small>'}</td><td class="n"><strong>${num(x.d, x.d < 10 ? 1 : 0)}</strong></td><td class="n">${x.n}</td><td>${x.rangos.join(' · ')}</td><td class="n">${num(x.km)}</td><td class="n">${x.puntos || '—'}</td></tr>`; }).join('');
  let abierto = true; const prev = el.querySelector('details'); if (prev) abierto = prev.open;
  el.innerHTML = `<div class="pp-tl" role="img" aria-label="Línea del viaje por países">${tl}</div><div class="pp-tl-tip" hidden></div>
    <div class="pp-tl-ej"><span>${fecha(addDays(S.salida, 0), true)}</span><span>${num(R.dias)} días</span><span>${fecha(addDays(S.salida, R.dias), true)}</span></div>
    <details ${abierto ? 'open' : ''}><summary>Tiempo por país</summary>
    <div style="overflow-x:auto"><table class="pp-tt"><thead><tr><th>País</th><th class="n">Días</th><th class="n" title="Veces que se entra en el país (cada una con su sello de entrada y de salida, y su visado si no es de entradas múltiples)">Estancias</th><th>Fechas aproximadas</th><th class="n">Km</th><th class="n">Puntos</th></tr></thead><tbody>${filas}</tbody></table></div></details>`;
}
// Globo de la línea del viaje: sigue al ratón (o al dedo) sobre cada tramo
(function(){
  const cont = () => $('pp-tiempo');
  function mostrar(ev){
    const el = cont(); if (!el) return;
    const tip = el.querySelector('.pp-tl-tip'), x = ev.touches ? ev.touches[0].clientX : ev.clientX, y = ev.touches ? ev.touches[0].clientY : ev.clientY;
    const seg = document.elementFromPoint(x, y), i = seg && seg.closest && seg.closest('.pp-tl i');
    if (!tip) return;
    if (!i || !i.dataset.tt) { tip.hidden = true; return; }
    el.querySelectorAll('.pp-tl i.on').forEach(e => e.classList.remove('on')); i.classList.add('on');
    const [t0, ...resto] = i.dataset.tt.split(' · ');
    tip.innerHTML = `<strong>${esc(t0.split(': ')[0])}</strong>${t0.includes(': ') ? '<br>' + esc(t0.split(': ').slice(1).join(': ')) : ''}${resto.length ? '<br>' + resto.map(esc).join('<br>') : ''}`;
    tip.hidden = false;
    const r = el.getBoundingClientRect(), w = tip.offsetWidth;
    tip.style.left = Math.max(0, Math.min(r.width - w, x - r.left - w / 2)) + 'px';
    tip.style.top = (el.querySelector('.pp-tl').offsetTop + 40) + 'px';
  }
  function ocultar(){ const el = cont(); if (!el) return; const tip = el.querySelector('.pp-tl-tip'); if (tip) tip.hidden = true; el.querySelectorAll('.pp-tl i.on').forEach(e => e.classList.remove('on')); }
  document.addEventListener('mousemove', ev => { if (ev.target.closest && ev.target.closest('.pp-tl')) mostrar(ev); else ocultar(); });
  document.addEventListener('touchstart', ev => { if (ev.target.closest && ev.target.closest('.pp-tl')) mostrar(ev); else ocultar(); }, {passive: true});
})();
// Cifras clave del viaje, arriba y a todo el ancho (como en el Planificador actual)
function pintarKPIs(){
  const el = $('pp-kpis'); if (!el) return;
  if (!R || !R.todos.length) { el.innerHTML = '<div class="pp-kpi" style="grid-column:1/-1"><div class="s">Toca un país en el mapa y añade puntos a la ida o a la vuelta: aquí verás los km, los días, la fecha de regreso, los países y el presupuesto del viaje.</div></div>'; return; }
  const B = R.bud, kmT = R.kmTot + R.kmEU, reg = addDays(S.salida, R.dias), prev = new Date((CFG.regreso || S.salida) + 'T00:00:00Z');
  const dif = Math.round((reg - prev) / 864e5), act = new Set(S.paises);
  const vis = [...new Set(R.runs.filter(r => r.puntos.length).map(r => r.s))], paso = [...new Set(R.orden)].filter(s => !vis.includes(s));
  const entradas = R.runs.length, diasPuntos = R.todos.reduce((t, p) => t + diasDe(p), 0);
  const rojos = R.avisos.filter(a => a.rojo).length;
  el.innerHTML = `
    <div class="pp-kpi"><div class="l">Km por vehículo</div><div class="v">${num(kmT)}</div><div class="s">${num(kmT / Math.max(1, R.dias))} km de media al día${R.kmEU ? ' · ' + num(R.kmEU) + ' por Europa' : ''}</div></div>
    <div class="pp-kpi ${dif > 0 ? 'alerta' : ''}"><div class="l">Días · regreso</div><div class="v">${num(R.dias)} días</div><div class="s">${fecha(addDays(S.salida, 0), true)} → <strong>${fecha(reg, true)}</strong><br>${dif > 0 ? num(dif) + ' días después' : num(-dif) + ' días antes'} del regreso previsto (${fecha(prev, true)})</div></div>
    <div class="pp-kpi"><div class="l">Países</div><div class="v">${vis.length}</div><div class="s">con paradas · ${paso.length} más de paso · ${entradas} estancias en total (entrar y salir)</div></div>
    <div class="pp-kpi"><div class="l">Puntos</div><div class="v">${R.todos.length}</div><div class="s">${R.ida.length} a la ida · ${R.vuelta.length} a la vuelta · ${num(diasPuntos, 1).replace(/,0$/, '')} días parado</div></div>
    <div class="pp-kpi"><div class="l">Presupuesto total</div><div class="v">${B ? eur(B.total) : '—'}</div><div class="s">${B ? eur(B.total / Math.max(1, B.nPers)) + ' por persona · ' + eur(B.total / Math.max(1, R.dias)) + ' al día · <a href="#pp-bud">desglose</a>' : ''}</div></div>
    <div class="pp-kpi ${rojos ? 'alerta' : ''}"><div class="l">Avisos</div><div class="v">${R.avisos.length}</div><div class="s">${rojos ? rojos + ' importantes (en rojo en el panel)' : 'ninguno importante'}${B ? ' · combustible ' + eur(B.cat.comb) + ' · visados ' + eur(B.cat.vis) : ''}</div></div>`;
}
function pintarEvitar(){
  const el = $('pp-evitar'); if (!el) return;
  el.innerHTML = S.evitar.length ? S.evitar.map(s => `<span>${esc(nom(s))} <button type="button" class="pp-b x" data-evitar="${s}" aria-label="Dejar de evitar ${esc(nom(s))}">✕</button></span>`).join('') : '<span class="pp-ayuda">Ninguno</span>';
  const sel = $('pp-evitar-add');
  if (sel && !sel.__lleno) { sel.innerHTML = '<option value="">Evitar un país…</option>' + Object.keys(PA).filter(s => !PA[s].isla && PA[s].pos).sort((a, b) => nom(a).localeCompare(nom(b), 'es')).map(s => `<option value="${s}">${esc(nom(s))}</option>`).join(''); sel.__lleno = true; }
}
let CAPA_Z = null;
function pintarZonas(){
  if (!MAP) return;
  if (!CAPA_Z) CAPA_Z = L.layerGroup();
  CAPA_Z.clearLayers();
  const on = $('pp-verzonas') ? $('pp-verzonas').checked : true;
  if (!on) { MAP.removeLayer(CAPA_Z); return; }
  ZONAS.forEach(z => { const col = z.nivel === 'rojo' ? '#B43A3A' : '#D97B29';
    L.polygon(z.polys.map(p => p.rs), {color: col, weight: 1, dashArray: '4 3', fillColor: col, fillOpacity: z.nivel === 'rojo' ? .22 : .14, pane: 'zonas'})
      .bindTooltip(`${z.nivel === 'rojo' ? 'Zona roja' : 'Zona naranja'} · ${esc(nom(z.pais))}: ${esc(z.nombre)}`, {sticky: true})
      .on('click', ev => { L.DomEvent.stop(ev); if (CREANDO) { crearEn(ev.latlng); return; } popZona(z, ev.latlng); })
      .on('contextmenu', ev => { L.DomEvent.stop(ev); libre(ev.latlng); })
      .addTo(CAPA_Z); });
  CAPA_Z.addTo(MAP);
}
function pintarPresupuesto(){
  const B = R && R.bud; if (!B || !$('pp-bud')) return;
  const hay = R.todos.length > 0;
  $('pp-total').textContent = hay ? eur(B.total) : '—';
  $('pp-total-sub').textContent = hay ? `${eur(B.total / Math.max(1, B.nPers))} por persona · ${eur(B.total / Math.max(1, R.dias))} al día` : 'Añade puntos para calcularlo';
  if (!hay) { $('pp-bud').hidden = true; return; }
  $('pp-bud').hidden = false;
  $('pp-bud-cards').innerHTML = B.veh.map(v => `<div class="pp-card"><div class="lbl">${esc(v.nombre)} · ${esc(v.detalle)}</div><div class="big">${eur(B.Rr[v.id].total)}</div>
      <div class="sub">${eur(B.Rr[v.id].total / Math.max(1, v.personas))} por persona · combustible ${eur(B.Rr[v.id].comb)} (${num(B.Rr[v.id].litros)} L a ${num(v.l100, 1)} L/100)</div></div>`).join('')
    + `<div class="pp-card tot"><div class="lbl">Total del viaje</div><div class="big">${eur(B.total)}</div><div class="sub">${num(B.nPers)} personas · ${num(R.dias)} días · ${num(B.km)} km por vehículo${B.desv ? ' (con un ' + num(B.desv * 100) + ' % de desvíos para agua, gasóleo y noche)' : ''}</div>
      <div class="sub">Además, <strong>${eur(B.aval)}</strong> inmovilizados en los avales del CPD (se recuperan al cerrar los carnets).</div></div>`;
  const max = Math.max(1, ...CATS.map(([k]) => B.cat[k]));
  $('pp-bud-barras').innerHTML = CATS.map(([k, l, c]) => `<div class="pp-bar"><span>${l}</span><div class="track"><i style="width:${B.cat[k] / max * 100}%;background:${c}"></i></div><span class="v">${eur(B.cat[k])}</span></div>`).join('');
  $('pp-bud-paises').innerHTML = B.filas.map(f => f.eu ? `<tr class="eu"><td>${esc(f.n)}</td><td class="n">${num(f.km)}</td><td class="n">—</td><td class="n">${num(f.precio, 2)} €</td><td class="n">${eur(B.veh.reduce((t, v) => t + f.km * v.l100 / 100 * f.precio, 0))}</td><td class="n">—</td><td class="n">—</td></tr>`
    : `<tr><td><strong>${esc(f.n)}</strong>${f.entradas > 1 ? ` <small>${f.entradas} entradas</small>` : ''}${f.generico ? '<span class="nota">gasóleo sin precio publicado: valor genérico</span>' : ''}${f.visAviso ? `<span class="nota av">⚠ la fuente del visado cambió el ${esc(f.visAviso)}: revisar</span>` : ''}</td>
      <td class="n">${num(f.km)}</td><td class="n">${num((R.diasPais[f.s] || 0) * R.factor, 1)}</td><td class="n">${num(f.precio, 2)} €</td>
      <td class="n">${eur(B.veh.reduce((t, v) => t + f.km * v.l100 / 100 * f.precio, 0))}</td>
      <td class="n" title="${esc(f.visTxt)}">${f.vis ? (f.visUrl ? `<a href="${esc(f.visUrl)}" target="_blank" rel="noopener">${eur(f.vis * f.entradas)}</a>` : eur(f.vis * f.entradas)) : (f.visSin ? '<span class="nota">sin dato</span>' : '—')}</td>
      <td class="n" title="${esc(f.tasaTxt)}">${f.tasa ? eur(f.tasa * f.entradas) : '—'}</td></tr>`).join('')
    + B.ferris.map(x => `<tr class="eu"><td>Ferry de ${x.dir}: ${esc(x.dir === 'ida' ? x.f.origen + ' → ' + x.f.puerto : x.f.puerto + ' → ' + x.f.origen)}<span class="nota">${esc(x.f.naviera)} · ${num(x.f.h)} h · los dos vehículos</span></td><td class="n" colspan="6">${eur(x.eur)}</td></tr>`).join('');
  const aj = (k, v, d, step, w) => `<input type="number" min="0" step="${step}" value="${+v.toFixed(2)}" data-aj="${k}" data-def="${d}" class="${k in B.A ? 'edited' : ''}" style="width:${w || 74}px" autocomplete="off" data-1p-ignore data-lpignore="true">`;
  $('pp-bud-gastos').innerHTML = B.gastos.map(g => `<tr><td><strong>${esc(g.label)}</strong>${g.nota ? `<span class="nota">${esc(g.nota)}</span>` : ''}</td>
      <td class="n">${aj('p.' + g.id, g.v, g.val, g.ambito === 'pct' ? 1 : 0.5)}</td><td>${esc(g.unidad)}<span class="nota">${esc(g.como)}</span></td><td class="n"><strong>${eur(g.total)}</strong></td></tr>`).join('')
    + B.veh.map(v => `<tr class="eu"><td>CPD de ${esc(v.nombre)}<span class="nota">carnet; el aval de ${eur(v.aval)} no suma</span></td><td class="n">${num(v.cpd, 2)} €</td><td>por vehículo</td><td class="n">${eur(v.cpd)}</td></tr>`).join('')
    + (B.perros ? `<tr class="eu"><td>Perro en los ferris<span class="nota">ida y vuelta</span></td><td class="n">${num(BUD.perro_ferry)} €</td><td>por trayecto y perro</td><td class="n">${eur(2 * BUD.perro_ferry * B.perros)}</td></tr>` : '');
  $('pp-bud-veh').innerHTML = B.veh.map(v => `<div class="pp-card"><div class="lbl">${esc(v.nombre)}</div>
      <label>Personas ${aj(v.id + '.personas', v.personas, BUD.vehiculos.find(x => x.id === v.id).personas, 1, 60)}</label>
      <label>Perros ${aj(v.id + '.perros', v.perros, BUD.vehiculos.find(x => x.id === v.id).perros, 1, 60)}</label>
      <label>Consumo (L/100 km) ${aj(v.id + '.l100', v.l100, BUD.vehiculos.find(x => x.id === v.id).l100, 0.5, 60)}</label></div>`).join('');
  $('pp-bud-pie').innerHTML = `Visados: ${eur(B.visPP)} por persona (${eur(B.visPP * B.nPers)} el grupo) · tasas de vehículo: ${eur(B.tasas)} por vehículo · ferris: ${eur(B.cat.ferry)}.
    Precios del ${esc(BUD.fecha)}; gasóleo de GlobalPetrolPrices (${esc(BUD.gpp_fecha)}), actualizado cada semana.
    ${B.ajustado ? 'Incluye tus ajustes del Planificador actual.' : ''} Lo que cambies aquí (en ámbar) vale también para el <a href="${raiz}planificador/#resumen">Planificador actual</a>, y al revés; allí están además los precios del gasóleo, visados y ferris por país.`;
  pintarComparar();
}

// ------------------------------------------------------------------ la web usa este viaje
// Con la casilla marcada, el resumen de este viaje ('a27-ruta-resumen') alimenta
// el mapa general, el portal y el bloque «Tu viaje» de las fichas, igual que el
// Planificador actual (que deja de publicar el suyo mientras tanto).
const RKEY = 'a27-ruta-resumen', FUENTE = 'a27-ruta-fuente', CIFRAS = 'a27-plan-cifras';
const usaWeb = () => { try { return localStorage.getItem(FUENTE) === 'puntos'; } catch(e) { return false; } };
function publicar(R){
  if (!usaWeb() || !R.todos.length) return;
  try {
    const iso = d => d.toISOString().slice(0, 10), f = R.factor, veces = {};
    const pasos = R.runs.map((r, i) => {
      veces[r.s] = (veces[r.s] || 0) + 1;
      const prev = R.runs[i - 1], next = R.runs[i + 1], ps = r.puntos;
      return {s: r.s, f: r.s, n: nom(r.s), nf: nom(r.s), k: veces[r.s], tipo: ps.length ? 'visita' : 'transito',
        lab: ps.length ? ps.slice(0, 3).map(p => p.nombre.split(' · ')[0]).join(', ') + (ps.length > 3 ? ' y ' + (ps.length - 3) + ' más' : '') : '',
        de: prev ? nom(prev.s) : 'ferry desde ' + R.FI.f.origen, a: next ? nom(next.s) : 'ferry a ' + R.FV.f.origen,
        ent: iso(addDays(S.salida, r.t0 * f)), sal: iso(addDays(S.salida, r.t1 * f)), d: Math.round((r.t1 - r.t0) * f * 10) / 10, km: Math.round(r.km)};
    });
    const linea = [];
    const push = q => { const x = [Math.round(q[0] * 100) / 100, Math.round(q[1] * 100) / 100], u = linea[linea.length - 1]; if (!u || u[0] !== x[0] || u[1] !== x[1]) linea.push(x); };
    R.tramos.forEach(t => t.pts.forEach(push));
    localStorage.setItem(RKEY, JSON.stringify({v: 1, fuente: 'puntos', nombre: (S.nombre || 'Viaje por puntos') + ' · por puntos', origen: CFG.origen, salida: S.salida,
      regreso: iso(addDays(S.salida, R.dias)), dias: R.dias, km: Math.round(R.kmTot + R.kmEU),
      ida: R.FI.f.origen + ' → ' + R.FI.f.puerto, vuelta: R.FV.f.puerto + ' → ' + R.FV.f.origen, pasos, linea, hecho: new Date().toISOString()}));
  } catch(e) {}
}
function pintarWeb(){
  const on = usaWeb(); $('pp-web').checked = on;
  $('pp-web-txt').innerHTML = on ? 'El mapa general, el portal y las fichas muestran <strong>este viaje</strong>.'
    : 'Ahora la web muestra el viaje del <a href="' + raiz + 'planificador/">Planificador actual</a>.';
}
function pintarComparar(){
  const el = $('pp-comp'); if (!el) return;
  let C = null; try { C = JSON.parse(localStorage.getItem(CIFRAS) || 'null'); } catch(e) { C = null; }
  if (!C || !R || !R.bud || !R.todos.length) { el.innerHTML = C ? '' : '<p class="pp-ayuda">Abre el <a href="' + raiz + 'planificador/">Planificador actual</a> una vez y aquí verás la comparación.</p>'; return; }
  const yo = {km: R.kmTot + R.kmEU, dias: R.dias, total: R.bud.total};
  const dif = (a, b, fmt) => { const d = a - b; return Math.abs(d) < 0.5 ? '<span class="ig">igual</span>' : `<span class="${d > 0 ? 'mas' : 'menos'}">${d > 0 ? '+' : '−'}${fmt(Math.abs(d))}</span>`; };
  el.innerHTML = `<table class="pp-comp"><thead><tr><th></th><th title="Este viaje">Este</th><th title="Planificador actual">Actual</th><th title="Diferencia">Dif.</th></tr></thead><tbody>
    <tr><td>Km</td><td>${num(yo.km)}</td><td>${num(C.km)}</td><td>${dif(yo.km, C.km, num)}</td></tr>
    <tr><td>Días</td><td>${num(yo.dias)}</td><td>${num(C.dias)}</td><td>${dif(yo.dias, C.dias, num)}</td></tr>
    <tr><td>Presupuesto</td><td>${eur(yo.total)}</td><td>${eur(C.total)}</td><td>${dif(yo.total, C.total, eur)}</td></tr></tbody></table>
    <p class="pp-ayuda">Planificador actual: «${esc(C.nombre || '')}»${C.paises ? ' · ' + C.paises + ' países' : ''}.</p>`;
}

// ------------------------------------------------------------------ mapa
let MAP, CAPA_P, CAPA_SEL, CAPA_RUTA, CAPA_FR, PAISES, ENCUADRE = false;
const COL = ['#1E7A8A', '#C47F17', '#2B6CB0', '#2E7D32', '#8B5A2B', '#673AB7', '#B43A3A', '#5F6B72'];
// Colores por orden de aparición en el viaje: dos países seguidos nunca comparten color
const PALETA = ['#1E7A8A', '#C47F17', '#2E7D32', '#673AB7', '#B43A3A', '#2B6CB0', '#8B5A2B', '#D97B29', '#0F8B6E', '#8E4585', '#5F6B72', '#A0892C'];
const colPais = s => { if (R && R.colores && R.colores[s]) return R.colores[s]; let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) >>> 0; return COL[h % COL.length]; };
function estiloPaises(){
  if (!PAISES) return;
  const act = new Set(S.paises), cruza = new Set(R ? R.orden : []);
  PAISES.eachLayer(l => {
    const s = l.feature.properties.slug, P0 = PA[s];
    let st = {weight: 1, color: '#8A949A', fillColor: '#ffffff', fillOpacity: .04, dashArray: null};
    if (P0 && P0.cf) st = {...st, fillColor: '#B43A3A', fillOpacity: act.has(s) ? .28 : .16, color: '#B43A3A', dashArray: '3 4'};
    if (act.has(s)) st = {...st, fillColor: P0 && P0.cf ? '#B43A3A' : '#1E7A8A', fillOpacity: P0 && P0.cf ? .3 : .16, color: P0 && P0.cf ? '#B43A3A' : '#1E7A8A', weight: 1.5};
    else if (cruza.has(s)) st = {...st, fillColor: '#D97B29', fillOpacity: .12, color: '#C47F17'};
    if (S.evitar.includes(s)) st = {...st, fillColor: '#2B2F33', fillOpacity: .28, color: '#2B2F33', dashArray: '2 5', weight: 1.5};
    l.setStyle(st);
  });
}
// Ficha completa de cada PDI (la misma que el mapa general): se carga en segundo plano.
let DET = null, DETP = null;
function cargarDet(){
  if (!DETP) DETP = fetch(raiz + 'assets/js/pdi-detalle.json').then(r => r.json()).then(d => { DET = d; return d; }).catch(() => { DET = {}; return DET; });
  return DETP;
}
const det = p => (p && p.propio ? PDET[p.id] : (DET && p && DET[p.id])) || null;

// ------------------------------------------------------------------ zonas desaconsejadas (FCDO)
// Polígonos [exterior, agujeros…] generados por tools/zonas_riesgo_gen.py. Rojo = todo viaje
// desaconsejado; naranja = solo viajes esenciales. Los países enteros en conflicto van aparte.
const ZONAS = (CFG.zonas || []).map(z => {
  const polys = z.poly.map(rs => { const ex = rs[0]; let a = 90, b = -90, c = 180, d = -180; ex.forEach(([la, lo]) => { a = Math.min(a, la); b = Math.max(b, la); c = Math.min(c, lo); d = Math.max(d, lo); });
    return {rs, bb: [a, b, c, d]}; });
  return {...z, polys};
});
function enAnillo(la, lo, r){ let c = false; for (let i = 0, j = r.length - 1; i < r.length; j = i++) { const [yi, xi] = r[i], [yj, xj] = r[j]; if ((yi > la) !== (yj > la) && lo < (xj - xi) * (la - yi) / (yj - yi) + xi) c = !c; } return c; }
function zonaDe(la, lo){
  let hit = null;
  for (const z of ZONAS) for (const p of z.polys) {
    const [a, b, c, d] = p.bb; if (la < a || la > b || lo < c || lo > d) continue;
    if (enAnillo(la, lo, p.rs[0]) && !p.rs.slice(1).some(h => enAnillo(la, lo, h))) { if (!hit || (z.nivel === 'rojo' && hit.nivel !== 'rojo')) hit = z; }
  }
  return hit;
}
const zonaTxt = z => `<strong>${z.nivel === 'rojo' ? 'Zona roja' : 'Zona naranja'}</strong> (${z.nivel === 'rojo' ? 'todo viaje desaconsejado' : 'solo viajes esenciales'}, FCDO): ${esc(z.nombre)}`;
function popZona(z, latlng){
  const s = z.pais;
  L.popup({maxWidth: 340}).setLatLng(latlng).setContent(`<div class="pp-pop"><strong style="color:${z.nivel === 'rojo' ? '#B43A3A' : '#B8560D'}">${z.nivel === 'rojo' ? 'Zona roja' : 'Zona naranja'} · ${esc(nom(s))}</strong>
    <div class="meta">${esc(z.nombre)}</div><div style="font-size:12.5px;line-height:1.4">${esc(z.texto)}</div>
    <div style="font-size:11.5px;color:#5F6B72;margin-top:6px">FCDO británico, revisado el ${esc(z.fecha)}${z.aprox ? ' · límites aproximados' : ''} · <a href="${esc(z.fuente)}" target="_blank" rel="noopener">aviso oficial</a> · <a href="${raiz}paises/${s}/" target="_blank" rel="noopener">ficha</a></div>
    <div class="acc" style="margin-top:8px">${S.paises.includes(s) ? '' : `<button type="button" class="pp-b" data-verpais="${s}">Ver los puntos de ${esc(nom(s))}</button>`}</div></div>`).openOn(MAP);
}

// ------------------------------------------------------------------ puntos propios (creador)
// Los puntos creados con el creador viven en 'a27-pdi-propios'. Cuando uno ya está
// publicado y la web reconstruida, su copia oficial («pais-n») lo sustituye también
// en los viajes guardados.
function cargarPropios(){
  PROPIOS = {}; PDET = {};
  if (!window.A27Creador) return;
  let cambio = false;
  A27Creador.lista().forEach(x => {
    const id = 'propio-' + x.id, of = x.publicado && x.publicado.n ? x.publicado.slug + '-' + x.publicado.n : '';
    if (of && PUNTOS[of]) {
      ['ida', 'vuelta'].forEach(m => { S[m] = S[m].map(y => { if (y === id) { cambio = true; return of; } return y; }); });
      return;
    }
    if (!x.poi) return;
    PROPIOS[id] = {id, propio: true, reg: x.id, pais: x.pais, nombre: x.poi.name, cat: x.poi.cat, prio: x.poi.prio || '', lat: x.lat, lon: x.lon,
      tiempo: x.poi.time || '', dias: isFinite(x.dias) ? x.dias : 0, perro: x.perro || 'sin_dato', clase: x.clase, publicado: !!x.publicado};
    PDET[id] = x.detalle;
  });
  if (cambio) save();
}
function crearEn(latlng){
  CREANDO = false; if ($('pp-crear')) $('pp-crear').setAttribute('aria-pressed', 'false');
  if (MAP) MAP.getContainer().style.cursor = '';
  if (!window.A27Creador) { msg('El creador de puntos no se ha cargado.'); return; }
  MAP.closePopup();
  const s = paisDe(latlng.lat, latlng.lng);
  A27Creador.abrir(latlng.lat, latlng.lng, {pais: s || '', paisNombre: s ? nom(s) : '', raiz, enViaje: true, cambio: (reg, guardado) => {
    cargarPropios(); calcular();
    if (guardado && reg && MAP) { const p = punto('propio-' + reg.id); if (p) L.popup({maxWidth: 320, minWidth: 250}).setLatLng([p.lat, p.lon]).setContent(popPunto(p)).openOn(MAP); }
  }});
}
function editarPropio(id){
  const p = punto(id); if (!p || !p.propio || !window.A27Creador) return;
  MAP && MAP.closePopup();
  A27Creador.abrir(p.lat, p.lon, {id: p.reg, pais: p.pais, paisNombre: nom(p.pais), raiz, enViaje: true, cambio: reg => {
    if (!reg) { S.ida = S.ida.filter(x => x !== id); S.vuelta = S.vuelta.filter(x => x !== id); save(); }
    cargarPropios(); calcular(); }});
}
function acciones(p){
  const en = S.ida.includes(p.id) ? 'ida' : S.vuelta.includes(p.id) ? 'vuelta' : '';
  return en
    ? `<button type="button" class="pp-b big ${en === 'ida' ? 'vuelta' : 'ida'}" data-pp="${en === 'ida' ? 'vuelta' : 'ida'}" data-id="${esc(p.id)}">Pasar a la ${en === 'ida' ? 'vuelta' : 'ida'}</button><button type="button" class="pp-b big x" data-pp="quitar" data-id="${esc(p.id)}">Quitar</button>`
    : `<button type="button" class="pp-b big ida" data-pp="ida" data-id="${esc(p.id)}">+ Ida</button><button type="button" class="pp-b big vuelta" data-pp="vuelta" data-id="${esc(p.id)}">+ Vuelta</button>`;
}
const perroTxt = p => ({si: 'perro: sí', condiciones: 'perro: con condiciones', no: 'perro: no', sin_dato: 'perro: sin dato'}[p.perro] || '');
function popPunto(p){
  const d = det(p), pd = perroTxt(p);
  const img = d && d.img ? `<img src="${esc(/^https?:/.test(d.img) ? d.img : raiz + d.img)}" alt="${esc(p.nombre)}" loading="lazy">` : '';
  const res = d && d.desc ? `<span class="a27-map-summary">${esc(d.desc)}</span>` : (!DET && !p.libre ? '<span class="pp-cargando">Cargando la ficha…</span>' : '');
  const en = S.ida.includes(p.id) ? ' · <b>en la ida</b>' : S.vuelta.includes(p.id) ? ' · <b>en la vuelta</b>' : '';
  const lnk = (p.libre ? `<button type="button" class="a27-popup-expand" data-crear="${p.lat},${p.lon}">Crear un punto aquí</button>` : `<button type="button" class="a27-popup-expand" data-ficha="${esc(p.id)}">Ver ficha ampliada</button>`) +
    (p.propio ? `<button type="button" class="a27-popup-expand" data-editar="${esc(p.id)}">Editar o publicar</button>` : '') +
    `<a href="https://www.google.com/maps?q=${p.lat},${p.lon}" target="_blank" rel="noopener">Google Maps</a>`;
  return `<div class="pp-pop">${img}<strong>${esc(p.nombre)}</strong><div class="meta">${esc(nom(p.pais))}${p.cat ? ' · ' + esc(p.cat) : ''}${p.prio ? ' · ' + esc(p.prio) : ''}${p.libre ? '' : ' · ' + num(diasDe(p), 2).replace(/,?0+$/, '') + ' d'}${en}</div>${(() => { const z = zonaDe(p.lat, p.lon); return z ? `<span class="pp-zona ${z.nivel}">${z.nivel === 'rojo' ? 'zona roja' : 'zona naranja'} · FCDO</span>` : ''; })()}${p.propio ? `<span class="pp-propio">punto propio · ${p.publicado ? 'publicado, ' : ''}por revisar</span>` : ''}${res}${pd && !p.libre ? `<span class="perro ${p.perro}">${pd}</span>` : ''}<div class="acc">${acciones(p)}</div><div class="lnk">${lnk}</div></div>`;
}
// Popup con la ficha resumida; si los datos aún no han llegado, se completa al llegar.
function conPopup(capa, p){
  const w = Math.max(200, Math.min(320, (MAP ? MAP.getSize().x : 400) - 70));
  capa.bindPopup(() => popPunto(p), {maxWidth: w, minWidth: Math.min(250, w), autoPanPadding: [12, 12]});
  capa.on('click', ev => { if (CREANDO) { L.DomEvent.stop(ev); setTimeout(() => crearEn(ev.latlng), 0); } });
  capa.on('popupopen', e => { if (!DET && !p.libre) cargarDet().then(() => { if (e.popup.isOpen()) e.popup.setContent(popPunto(p)); }); });
  return capa;
}
// Ficha ampliada (fotos, qué se ve, acceso, perro, enlaces) en una ventana encima del planificador.
function abrirFicha(id){
  const p = punto(id); if (!p || p.libre) return;
  cargarDet().then(() => {
    const d = det(p);
    if (!d || typeof a27OpenPoi !== 'function') { msg('No hay ficha ampliada para este punto.'); return; }
    a27OpenPoi(d, raiz, MAP, null);
    const dlg = document.getElementById('a27-map-poi-dialog'); if (!dlg) return;
    dlg.querySelectorAll('.map-poi-actions a').forEach(a => { a.target = '_blank'; a.rel = 'noopener'; });
    const en = S.ida.includes(id) ? 'En tu ida' : S.vuelta.includes(id) ? 'En tu vuelta' : '';
    const bar = document.createElement('div'); bar.className = 'pp-dlg-acc';
    bar.innerHTML = (en ? `<span class="en">${en}</span>` : '') + acciones(p);
    dlg.querySelector('.map-poi-sheet').appendChild(bar);
  });
}
function pintarPuntos(){
  if (!CAPA_P) return;
  CAPA_P.clearLayers();
  const sel = new Set(S.ida.concat(S.vuelta)), act = $('pp-vertodos').checked ? null : new Set(S.paises);
  Object.values(PROPIOS).forEach(p => { if (sel.has(p.id)) return;
    conPopup(L.marker([p.lat, p.lon], {icon: L.divIcon({className: '', html: `<div class="pp-mkp${p.clase === 'log' ? ' log' : ''}">★</div>`, iconSize: [20, 20], iconAnchor: [10, 10]}), zIndexOffset: 200})
      .bindTooltip(esc(p.nombre) + ' · punto propio'), p).addTo(CAPA_P); });
  Object.values(PUNTOS).forEach(p => {
    if (sel.has(p.id) || (act && !act.has(p.pais))) return;
    const imp = /imprescindible/i.test(p.prio);
    conPopup(L.circleMarker([p.lat, p.lon], {radius: imp ? 6.5 : 5, color: '#fff', weight: 1.5, fillColor: p.perro === 'no' ? '#8A949A' : '#46535B', fillOpacity: .9})
      .bindTooltip(esc(p.nombre)), p).addTo(CAPA_P);
  });
}
function pintarSel(){
  CAPA_SEL.clearLayers();
  let i = 0;
  [['ida', S.ida], ['vuelta', S.vuelta]].forEach(([m, lista]) => lista.forEach(id => {
    const p = punto(id); if (!p) return; i++;
    conPopup(L.marker([p.lat, p.lon], {icon: L.divIcon({className: '', html: `<div class="pp-mk ${m}${p.libre ? ' libre' : ''}" style="width:24px;height:24px">${i}</div>`, iconSize: [24, 24], iconAnchor: [12, 12]}), zIndexOffset: 500})
      .bindTooltip(i + '. ' + esc(p.nombre)), p).addTo(CAPA_SEL);
  }));
}
function pintarRuta(){
  CAPA_RUTA.clearLayers(); CAPA_FR.clearLayers();
  if (!R) return;
  R.tramos.forEach(t => {
    if (t.pts.length < 2 || hav(t.pts[0], t.pts[t.pts.length - 1]) < .5) return;
    const lin = L.polyline(t.pts, {pane: 'rutas', color: t.mitad === 'ida' ? '#1E7A8A' : '#C47F17', weight: 4, opacity: .85, dashArray: t.real && !t.rodeo ? null : '6 7'}).addTo(CAPA_RUTA);
    if (t.pista) { const P = t.pista.pts; L.polyline(P, {pane: 'rutas', color: '#8B5A2B', weight: 5, opacity: .9, dashArray: '2 7', lineCap: 'round'}).bindTooltip(`Pista: ${esc(t.pista.nombre)} · ~${num(t.pista.km)} km`, {sticky: true}).addTo(CAPA_RUTA); }
    else if (t.rodeo) lin.bindTooltip('Sin carretera razonable en el mapa de rutas: línea recta, km estimados', {sticky: true});
  });
  R.seq.filter(w => w.tipo === 'frontera').forEach(w => L.marker(w.pos, {icon: L.divIcon({className: '', html: '<div class="pp-fr"></div>', iconSize: [12, 12], iconAnchor: [6, 6]}), zIndexOffset: 300})
    .bindTooltip('Frontera: ' + esc(w.f.nombre) + ' (' + esc(nom(w.f.pais)) + ' – ' + esc(nom(w.f.otro)) + ')').addTo(CAPA_FR));
  if ($('pp-verfr').checked) FRTODAS.forEach(f => {
    if (R.seq.some(w => w.f === f)) return;
    L.circleMarker([f.lat, f.lon], {radius: 4, color: '#5F6B72', weight: 1, fillColor: f.estado === 'cerrada' ? '#B43A3A' : '#fff', fillOpacity: 1})
      .bindTooltip(esc(f.nombre) + ' · ' + esc(nom(f.pais)) + ' – ' + esc(nom(f.otro)) + (f.estado !== 'abierta' ? ' · ' + f.estado : '')).addTo(CAPA_FR);
  });
  const pts = [[R.FI.f, 'Llegada'], [R.FV.f, 'Salida']];
  (R.FI.f.id === R.FV.f.id ? [[R.FI.f, 'Llegada y salida']] : pts).forEach(([f, txt]) =>
    L.marker(f.pos, {icon: L.divIcon({className: '', html: '<div class="pp-puerto">⛴</div>', iconSize: [20, 20], iconAnchor: [10, 10]})})
      .bindTooltip(`${txt}: ${esc(f.puerto)} (ferry ${esc(f.origen)})`).addTo(CAPA_FR));
}

// ------------------------------------------------------------------ panel
function filas(m, lista, base){
  return lista.map((id, i) => {
    const p = punto(id); if (!p) return '';
    const d = S.dias[id], f = R && R.fechaPunto[id] != null ? fecha(addDays(S.salida, R.fechaPunto[id] * R.factor)) : '';
    const perro = p.perro === 'no' ? ' · <span style="color:#B43A3A">sin perro</span>' : '';
    return `<li class="pp-it" data-id="${esc(id)}"><span class="pp-h" title="Arrastra para cambiar el orden o pasarlo a la otra mitad" aria-hidden="true">⠿</span><span class="pp-n">${base + i + 1}</span>
      <span class="pp-t">${p.libre ? `<strong title="${esc(p.nombre)}">${esc(p.nombre)}</strong>` : `<button type="button" class="pp-ver" data-ficha="${esc(id)}" title="Ver la ficha de ${esc(p.nombre)}">${esc(p.nombre)}</button>`}<small>${esc(nom(p.pais))}${f ? ' · ~' + f : ''}${perro}</small></span>
      <span class="pp-a"><input type="number" min="0" step="0.5" value="${d != null && d !== '' ? esc(d) : ''}" placeholder="${num(p.dias, 2).replace(/,?0+$/, '')}" data-dias="${esc(id)}" class="${d != null && d !== '' ? 'edited' : ''}" title="Días en este punto" aria-label="Días en ${esc(p.nombre)}" autocomplete="off" data-1p-ignore data-lpignore="true">
      <button type="button" class="pp-b" data-pp="${m === 'ida' ? 'vuelta' : 'ida'}" data-id="${esc(id)}" title="Pasar a la ${m === 'ida' ? 'vuelta' : 'ida'}">${m === 'ida' ? '↓' : '↑'}</button><button type="button" class="pp-b x" data-pp="quitar" data-id="${esc(id)}" title="Quitar">✕</button></span></li>`;
  }).join('');
}
function pintar(){
  $('pp-lista-ida').innerHTML = filas('ida', S.ida, 0);
  $('pp-lista-vuelta').innerHTML = filas('vuelta', S.vuelta, S.ida.length);
  $('pp-cnt-ida').textContent = S.ida.length ? S.ida.length + ' puntos' : '';
  $('pp-cnt-vuelta').textContent = S.vuelta.length ? S.vuelta.length + ' puntos' : '';
  $('pp-nombre').textContent = S.nombre || '';
  const fer = sel => CFG.ferris.map(f => `<option value="${f.id}">${esc(f.origen)} ⇄ ${esc(f.puerto)} · ${esc(f.naviera)}</option>`).join('');
  [['pp-fer-ida', 'ida'], ['pp-fer-vuelta', 'vuelta']].forEach(([id, dir]) => {
    const el = $(id), cur = dir === 'ida' ? S.fer_ida : S.fer_vuelta, auto = R ? (dir === 'ida' ? R.FI : R.FV).f : null;
    el.innerHTML = `<option value="">Automática${auto ? ': ' + esc(auto.puerto) + ' (' + esc(auto.origen) + ')' : ''}</option>` + fer();
    el.value = cur || '';
  });
  if (R) {
    $('pp-km').textContent = num(R.kmTot + R.kmEU);
    $('pp-dias').textContent = num(R.dias);
    const ps = [...new Set(R.orden)];
    $('pp-np').textContent = ps.length;
    $('pp-fechas').textContent = R.todos.length ? `Salida ${fecha(addDays(S.salida, 0), true)} · regreso ~${fecha(addDays(S.salida, R.dias), true)} · ferry ${R.FI.f.origen} → ${R.FI.f.puerto} y ${R.FV.f.puerto} → ${R.FV.f.origen}${R.kmEU ? ' · ' + num(R.kmEU) + ' km por Europa' : ''}` : '';
    const act = new Set(S.paises), totD = Object.values(R.diasPais).reduce((a, b) => a + b, 0) || 1;
    $('pp-tira').innerHTML = ps.map(s => `<i style="width:${(R.diasPais[s] || 0) / totD * 100}%;background:${colPais(s)}" title="${esc(nom(s))}: ~${num(R.diasPais[s] * R.factor, 1)} días"></i>`).join('');
    $('pp-paises').innerHTML = ps.map(s => `<span class="${act.has(s) ? '' : 'fuera'}" style="border-left:4px solid ${colPais(s)}">${esc(nom(s))} · ${num(R.kmPais[s] || 0)} km${R.entradas[s] > 1 ? ' · ' + R.entradas[s] + ' estancias' : ''}</span>`).join('');
    $('pp-avisos').innerHTML = R.avisos.map(a => `<li class="${a.rojo ? 'rojo' : ''}">${a.t}</li>`).join('');
  }
  $('pp-salida').value = S.salida || CFG.salida; $('pp-kmdia').value = S.kmdia; $('pp-margen').value = S.margen;
  if (MAP) { estiloPaises(); pintarPuntos(); pintarSel(); pintarRuta(); }
  pintarKPIs(); pintarTiempo(); pintarPresupuesto(); pintarWeb(); pintarEvitar();
  paintViajes();
}

// ------------------------------------------------------------------ acciones
const posDe = x => x && x.pos ? x.pos : (x ? [x.lat, x.lon] : null);
function coste(ant, p, sig){ return (ant ? hav(ant, p) : 0) + (sig ? hav(p, sig) : 0) - (ant && sig ? hav(ant, sig) : 0); }
function insertar(m, id){
  const lista = m === 'ida' ? S.ida : S.vuelta, p = punto(id), pp = [p.lat, p.lon];
  const ini = m === 'ida' ? (R ? R.FI.f.pos : null) : (S.ida.length ? posDe(punto(S.ida[S.ida.length - 1])) : (R ? R.FI.f.pos : null));
  const fin = m === 'vuelta' ? (R ? R.FV.f.pos : null) : null;
  const pos = lista.map(x => posDe(punto(x)));
  let best = lista.length, bc = Infinity;
  for (let i = 0; i <= lista.length; i++) { const c = coste(i ? pos[i - 1] : ini, pp, i < lista.length ? pos[i] : fin); if (c < bc) { bc = c; best = i; } }
  lista.splice(best, 0, id);
}
function mover(id, destino){
  S.ida = S.ida.filter(x => x !== id); S.vuelta = S.vuelta.filter(x => x !== id);
  if (destino === 'quitar') { if (S.libres[id]) delete S.libres[id]; delete S.dias[id]; }
  else { const p = punto(id); if (p && p.pais && !S.paises.includes(p.pais) && PA[p.pais]) S.paises.push(p.pais); insertar(destino, id); }
  save(); if (MAP) MAP.closePopup(); calcular();
  const p = punto(id);
  if (destino !== 'quitar' && p) msg(`<b>${esc(p.nombre)}</b> en la ${destino}.`);
}
function ordenar(m){
  const lista = (m === 'ida' ? S.ida : S.vuelta).slice(); if (lista.length < 3) return;
  const ini = m === 'ida' ? R.FI.f.pos : (S.ida.length ? posDe(punto(S.ida[S.ida.length - 1])) : R.FI.f.pos), fin = m === 'vuelta' ? R.FV.f.pos : null;
  const P = id => posDe(punto(id));
  let resto = lista.slice(), r = [], cur = ini;
  while (resto.length) { resto.sort((a, b) => hav(cur, P(a)) - hav(cur, P(b))); const x = resto.shift(); r.push(x); cur = P(x); }
  const len = o => o.reduce((s, x, i) => s + hav(i ? P(o[i - 1]) : ini, P(x)), 0) + (fin ? hav(P(o[o.length - 1]), fin) : 0);
  let mej = len(r), cambio = true, v = 0;
  while (cambio && v++ < 80) { cambio = false;
    for (let i = 0; i < r.length - 1; i++) for (let j = i + 1; j < r.length; j++) {
      const t = r.slice(0, i).concat(r.slice(i, j + 1).reverse(), r.slice(j + 1)), l = len(t);
      if (l < mej - 1e-6) { r = t; mej = l; cambio = true; } } }
  if (m === 'ida') S.ida = r; else S.vuelta = r;
  save(); calcular(); msg(`${m === 'ida' ? 'Ida' : 'Vuelta'} ordenada por cercanía.`);
}
function cargarRecorrido(s, recId, m){
  const rec = (PA[s].rec || []).find(r => r.id === recId); if (!rec) return;
  const pts = rec.pts, acum = [0]; for (let i = 1; i < pts.length; i++) acum.push(acum[i - 1] + hav(pts[i - 1], pts[i]));
  const cand = (PORPAIS[s] || []).map(p => {
    let bd = Infinity, bt = 0;
    for (let i = 1; i < pts.length; i++) { const a = pts[i - 1], b = pts[i], k = Math.cos(a[0] * Math.PI / 180);
      const ax = a[1] * k, ay = a[0], bx = b[1] * k, by = b[0], px = p.lon * k, py = p.lat, dx = bx - ax, dy = by - ay;
      const t = dx || dy ? Math.max(0, Math.min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy))) : 0;
      const d = Math.hypot(px - (ax + t * dx), py - (ay + t * dy)) * 111.2; if (d < bd) { bd = d; bt = acum[i - 1] + t * hav(a, b); } }
    return {p, d: bd, t: bt}; }).filter(x => x.d <= 20 && !S.ida.includes(x.p.id) && !S.vuelta.includes(x.p.id)).sort((a, b) => a.t - b.t);
  if (!cand.length) { msg('Ningún punto nuevo a menos de 20 km de ese recorrido.'); return; }
  let ids = cand.map(x => x.p.id);
  const lista = m === 'ida' ? S.ida : S.vuelta, ref = posDe(punto(lista[lista.length - 1])) || (m === 'ida' ? R.FI.f.pos : R.FV.f.pos);
  if (hav(ref, posDe(punto(ids[ids.length - 1]))) < hav(ref, posDe(punto(ids[0])))) ids = ids.reverse();
  lista.push(...ids);
  save(); if (MAP) MAP.closePopup(); calcular();
  msg(`${ids.length} puntos del recorrido ${esc(recId)} de ${esc(nom(s))} añadidos a la ${m}.`);
}
function alternarPais(s){
  if (!PA[s] || PA[s].isla) return;
  if (S.paises.includes(s)) return;
  S.paises.push(s); save(); pintar();
  msg(`${esc(nom(s))}: ${(PORPAIS[s] || []).length} puntos de interés en el mapa. Toca uno para añadirlo.`);
}
function popPais(s, latlng){
  const recs = (PA[s].rec || []).map(r => `<div style="margin:5px 0"><div style="font-size:12px;color:#5F6B72">Recorrido ${esc(r.id)} · ${esc(r.l.length > 60 ? r.l.slice(0, 58) + '…' : r.l)}</div><div class="acc"><button type="button" class="pp-b ida" data-rec="${s}|${esc(r.id)}|ida">A la ida</button><button type="button" class="pp-b vuelta" data-rec="${s}|${esc(r.id)}|vuelta">A la vuelta</button></div></div>`).join('');
  L.popup({maxWidth: 320}).setLatLng(latlng).setContent(`<div class="pp-pop"><strong>${esc(nom(s))}</strong><div class="meta">${(PORPAIS[s] || []).length} puntos de interés${PA[s].cf ? ' · <b style="color:#B43A3A">país en conflicto</b>' : ''}</div>${recs ? '<div style="font-size:12px;margin-bottom:2px">Atajo: añadir los puntos de un recorrido de la ficha</div>' + recs : ''}<div class="acc" style="margin-top:8px"><button type="button" class="pp-b" data-ocultar="${s}">Ocultar sus puntos</button><button type="button" class="pp-b" data-evitar="${s}">${S.evitar.includes(s) ? 'Dejar de evitar' : 'Evitar en la ruta'}</button><a href="${raiz}paises/${s}/" target="_blank" rel="noopener" style="font-size:12px;align-self:center">Ficha del país</a></div></div>`).openOn(MAP);
}
function libre(latlng){
  const s = paisDe(latlng.lat, latlng.lng);
  if (!s) { msg('Ese punto no cae en ningún país del mapa.'); return; }
  const id = 'libre-' + Date.now().toString(36);
  S.libres[id] = {lat: Math.round(latlng.lat * 1e5) / 1e5, lon: Math.round(latlng.lng * 1e5) / 1e5, pais: s, nombre: 'Paso por aquí · ' + nom(s)};
  const p = punto(id);
  L.popup({maxWidth: Math.max(200, Math.min(320, MAP.getSize().x - 70)), minWidth: 200}).setLatLng(latlng).setContent(popPunto(p)).openOn(MAP);
  MAP.once('popupclose', () => { if (S.libres[id] && !S.ida.includes(id) && !S.vuelta.includes(id)) delete S.libres[id]; });
}

// ------------------------------------------------------------------ viajes guardados (aparte del Planificador actual)
function leerV(){ try { return JSON.parse(localStorage.getItem(VKEY) || '{}') || {}; } catch(e) { return {}; } }
function escV(v){ try { localStorage.setItem(VKEY, JSON.stringify(v)); return true; } catch(e) { return false; } }
function paintViajes(){
  const V = leerV(), n = Object.keys(V).sort((a, b) => (V[b].fecha || '').localeCompare(V[a].fecha || ''));
  const el = $('pp-viajes'), cur = el.value;
  el.innerHTML = n.length ? n.map(x => `<option value="${esc(x)}">${esc(x)} · ${V[x].r ? num(V[x].r.km) + ' km · ' + V[x].r.dias + ' días' : ''}</option>`).join('') : '<option value="">Aún no hay viajes guardados</option>';
  if (n.includes(cur)) el.value = cur; else if (n.includes(S.nombre)) el.value = S.nombre;
}
function guardarViaje(){
  const n = ($('pp-vnombre').value || S.nombre || '').trim().slice(0, 60);
  if (!n) { msg('Pon un nombre al viaje.'); $('pp-vnombre').focus(); return; }
  const V = leerV(); S.nombre = n;
  V[n] = {S: JSON.parse(JSON.stringify(S)), fecha: new Date().toISOString(), r: R ? {km: Math.round(R.kmTot), dias: R.dias} : null};
  if (escV(V)) { save(); $('pp-vnombre').value = ''; pintar(); msg(`Viaje «${esc(n)}» guardado.`); }
}
function cargarViaje(){
  const n = $('pp-viajes').value, V = leerV(); if (!V[n]) return;
  S = Object.assign(VACIO(), JSON.parse(JSON.stringify(V[n].S))); S.nombre = n; save(); ENCUADRE = false; calcular(); encuadrar(); msg(`Viaje «${esc(n)}» cargado.`);
}
function borrarViaje(){
  const n = $('pp-viajes').value, V = leerV(); if (!V[n]) return;
  if (!confirm(`¿Borrar el viaje «${n}»?`)) return;
  delete V[n]; escV(V); paintViajes(); msg(`Viaje «${esc(n)}» borrado.`);
}
// Convierte el viaje del Planificador actual (su último cálculo, 'a27-plan-resumen') en
// un viaje por puntos: en cada país donde se para, los PDI por los que pasa su
// recorrido, en el orden en que la ruta pasa junto a ellos; la ida acaba en el punto
// más alejado del puerto de llegada, como en el mapa general.
function traerPlan(){
  let P = null; try { P = JSON.parse(localStorage.getItem('a27-plan-resumen') || 'null'); } catch(e) {}
  if (!P || !P.linea || P.linea.length < 2) { msg(`Abre antes el <a href="${raiz}planificador/">Planificador actual</a> con el viaje que quieras traer (se guarda al calcularlo).`); return; }
  const L0 = P.linea, o = L0[0];
  let k = 0, dm = -1; L0.forEach((q, i) => { const d = hav(o, q); if (d > dm) { dm = d; k = i; } });
  const visita = new Set(P.pasos.filter(x => x.tipo === 'visita').map(x => x.f === 'cabinda' ? 'angola' : x.f));
  // Los recorridos de las fichas pasan por sus PDI: se toman los que coinciden con un vértice
  // de la línea (redondeada a 0,01°, ~1 km), no todos los que quedan cerca de la carretera.
  const D = L0.map((q, i) => ({p: q, i}));
  const elegidos = [];
  visita.forEach(s => (PORPAIS[s] || []).forEach(p => {
    let best = null;
    for (let j = 0; j < D.length; j++) { const q = D[j]; if (Math.abs(q.p[0] - p.lat) > 0.15 || Math.abs(q.p[1] - p.lon) > 0.2) continue;
      const d = hav([p.lat, p.lon], q.p); if (d <= 3 && (!best || d < best.d)) best = {d, i: q.i, j}; }
    if (best) elegidos.push({id: p.id, pais: s, i: best.i, j: best.j});
  }));
  if (!elegidos.length) { msg('No hay puntos de interés junto al recorrido de ese viaje.'); return; }
  if ((S.ida.length || S.vuelta.length) && !confirm(`Se sustituye el viaje actual de esta página por «${P.nombre}» (${elegidos.length} puntos). Si quieres conservar el actual, cancela y guárdalo antes en «Mis viajes». ¿Seguir?`)) return;
  elegidos.sort((a, b) => a.j - b.j);
  const n = VACIO();
  n.paises = [...visita].filter(s => PA[s]);
  n.ida = elegidos.filter(x => x.i <= k).map(x => x.id); n.vuelta = elegidos.filter(x => x.i > k).map(x => x.id);
  n.salida = P.salida || S.salida; n.kmdia = S.kmdia; n.margen = S.margen; n.evitar = S.evitar.slice();
  n.nombre = (P.nombre || 'Planificador actual').replace(/ \(con cambios\)$/, '') + ' · por puntos';
  S = n; save(); calcular(); encuadrar();
  msg(`Traído «${esc(P.nombre)}»: ${n.ida.length} puntos a la ida y ${n.vuelta.length} a la vuelta en ${n.paises.length} países. Revisa los días de cada punto.`);
}
function exportar(){
  const propios = window.A27Creador ? A27Creador.lista() : [];
  const blob = new Blob([JSON.stringify({app: 'a27-planificador-puntos', v: 1, viajes: leerV(), actual: S, propios}, null, 1)], {type: 'application/json'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'viajes-por-puntos-africa-2027.json'; document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
}
function importar(file){
  const rd = new FileReader();
  rd.onload = () => { try { const j = JSON.parse(rd.result); if (j.app !== 'a27-planificador-puntos') throw 0;
    const V = leerV(); Object.assign(V, j.viajes || {}); escV(V);
    if (Array.isArray(j.propios) && j.propios.length) { const ya = new Set((window.A27Creador ? A27Creador.lista() : []).map(x => x.id));
      const todos = (window.A27Creador ? A27Creador.lista() : []).concat(j.propios.filter(x => x && x.id && !ya.has(x.id)));
      try { localStorage.setItem('a27-pdi-propios', JSON.stringify(todos)); } catch(err) {} cargarPropios(); calcular(); }
    paintViajes(); msg(`${Object.keys(j.viajes || {}).length} viajes importados${j.propios && j.propios.length ? ' y ' + j.propios.length + ' puntos propios' : ''}.`); }
    catch(e) { msg('Ese archivo no es una copia de viajes de esta página.'); } };
  rd.readAsText(file);
}
function encuadrar(){
  if (!MAP) return;
  const pts = S.ida.concat(S.vuelta).map(punto).filter(Boolean).map(p => [p.lat, p.lon]);
  if (pts.length > 1) MAP.fitBounds(L.latLngBounds(pts), {padding: [40, 40]});
  else MAP.fitBounds([[-35, -18], [37, 52]]);
}

// ------------------------------------------------------------------ eventos
document.addEventListener('click', e => {
  const b = e.target.closest('[data-pp]');
  if (b) { const dlg = b.closest('dialog'); if (dlg) dlg.close(); mover(b.dataset.id, b.dataset.pp); return; }
  const fi = e.target.closest('[data-ficha]'); if (fi) { abrirFicha(fi.dataset.ficha); return; }
  const cr = e.target.closest('[data-crear]'); if (cr) { const [la, lo] = cr.dataset.crear.split(',').map(Number); crearEn({lat: la, lng: lo}); return; }
  const ed = e.target.closest('[data-editar]'); if (ed) { editarPropio(ed.dataset.editar); return; }
  const ev = e.target.closest('[data-evitar]');
  if (ev) { const s = ev.dataset.evitar; if (S.evitar.includes(s)) S.evitar = S.evitar.filter(x => x !== s);
    else { if (S.ida.concat(S.vuelta).some(id => (punto(id) || {}).pais === s)) { msg(`${esc(nom(s))} tiene puntos en tu viaje: quítalos antes de evitarlo.`); return; } S.evitar.push(s); S.paises = S.paises.filter(x => x !== s); }
    save(); MAP && MAP.closePopup(); calcular(); msg(S.evitar.includes(s) ? `La ruta evitará ${esc(nom(s))} si hay otro camino.` : `${esc(nom(s))} vuelve a estar disponible.`); return; }
  const vp = e.target.closest('[data-verpais]'); if (vp) { MAP.closePopup(); alternarPais(vp.dataset.verpais); return; }
  if (e.target.closest('#pp-crear')) { CREANDO = !CREANDO; $('pp-crear').setAttribute('aria-pressed', String(CREANDO)); if (MAP) MAP.getContainer().style.cursor = CREANDO ? 'crosshair' : '';
    if (CREANDO) msg('Toca en el mapa el sitio del punto nuevo.'); return; }
  const r = e.target.closest('[data-rec]'); if (r) { const [s, id, m] = r.dataset.rec.split('|'); cargarRecorrido(s, id, m); return; }
  const o = e.target.closest('[data-ocultar]');
  if (o) { const s = o.dataset.ocultar; const usados = S.ida.concat(S.vuelta).some(id => (punto(id) || {}).pais === s);
    if (usados) { msg(`${esc(nom(s))} tiene puntos en tu viaje: quítalos antes de ocultarlo.`); return; }
    S.paises = S.paises.filter(x => x !== s); save(); MAP.closePopup(); pintar(); return; }
});
document.addEventListener('change', e => {
  const d = e.target.dataset.dias;
  if (d) { const v = e.target.value; if (v === '') delete S.dias[d]; else S.dias[d] = v; save(); calcular(); return; }
  if (e.target.id === 'pp-fer-ida') { S.fer_ida = e.target.value; save(); calcular(); }
  if (e.target.id === 'pp-fer-vuelta') { S.fer_vuelta = e.target.value; save(); calcular(); }
  if (e.target.id === 'pp-salida') { S.salida = e.target.value || CFG.salida; save(); calcular(); }
  if (e.target.id === 'pp-kmdia') { S.kmdia = Math.max(50, +e.target.value || 300); save(); calcular(); }
  if (e.target.id === 'pp-margen') { S.margen = Math.max(0, +e.target.value || 0); save(); calcular(); }
  if (e.target.dataset.aj) {
    const k = e.target.dataset.aj, v = e.target.value, A = ajustes();
    if (v === '' || parseFloat(v) === parseFloat(e.target.dataset.def)) delete A[k]; else A[k] = parseFloat(v);
    try { localStorage.setItem(AJ_KEY, JSON.stringify(A)); } catch(err) {}
    calcular(); return;
  }
  if (e.target.id === 'pp-verfr') pintarRuta();
  if (e.target.id === 'pp-verzonas') { try { localStorage.setItem('a27pp-zonas', e.target.checked ? '1' : '0'); } catch(err) {} pintarZonas(); }
  if (e.target.id === 'pp-evitar-add' && e.target.value) { const s = e.target.value; e.target.value = '';
    if (S.ida.concat(S.vuelta).some(id => (punto(id) || {}).pais === s)) { msg(`${esc(nom(s))} tiene puntos en tu viaje: quítalos antes de evitarlo.`); return; }
    if (!S.evitar.includes(s)) S.evitar.push(s); S.paises = S.paises.filter(x => x !== s); save(); calcular(); return; }
  if (e.target.id === 'pp-web') {
    try { if (e.target.checked) localStorage.setItem(FUENTE, 'puntos'); else { localStorage.setItem(FUENTE, 'planificador'); localStorage.removeItem(RKEY); } } catch(err) {}
    if (e.target.checked) { publicar(R); msg('El mapa general y las fichas usan ahora este viaje.'); } else msg('La web volverá a usar el Planificador actual en cuanto lo abras.');
    pintarWeb(); return;
  }
  if (e.target.id === 'pp-vertodos') pintarPuntos();
  if (e.target.id === 'pp-importar' && e.target.files[0]) { importar(e.target.files[0]); e.target.value = ''; }
});
$('pp-ord-ida').addEventListener('click', () => ordenar('ida'));
$('pp-ord-vuelta').addEventListener('click', () => ordenar('vuelta'));
$('pp-guardar').addEventListener('click', guardarViaje);
$('pp-cargar').addEventListener('click', cargarViaje);
$('pp-borrar').addEventListener('click', borrarViaje);
$('pp-exportar').addEventListener('click', exportar);
$('pp-traer').addEventListener('click', traerPlan);
$('pp-vnombre').addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); guardarViaje(); } });
$('pp-nuevo').addEventListener('click', () => { if (!confirm('¿Empezar un viaje nuevo? El actual se pierde si no lo has guardado.')) return; S = VACIO(); save(); calcular(); encuadrar(); });
if (window.Sortable) ['pp-lista-ida', 'pp-lista-vuelta'].forEach(id => Sortable.create($(id), {group: 'pp', handle: '.pp-h', animation: 150,
  onEnd: () => { S.ida = [...$('pp-lista-ida').children].map(li => li.dataset.id); S.vuelta = [...$('pp-lista-vuelta').children].map(li => li.dataset.id); save(); calcular(); }}));

window.addEventListener('storage', e => { if (e.key === 'a27-pdi-propios') cargarPropios(); if (e.key === AJ_KEY || e.key === CIFRAS || e.key === FUENTE || e.key === 'a27-pdi-propios') calcular(); });

// ------------------------------------------------------------------ arranque
function iniciarMapa(){
  if (typeof L === 'undefined' || !$('pp-mapa')) return;
  MAP = L.map('pp-mapa', {zoomSnap: 0.25, scrollWheelZoom: true}).fitBounds([[-35, -18], [37, 52]]);
  L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {maxZoom: 15, attribution: 'Teselas © Esri'}).addTo(MAP);
  PAISES = L.geoJSON(GEO, {style: () => ({weight: 1, color: '#8A949A', fillOpacity: .04, fillColor: '#fff'}),
    onEachFeature: (f, lay) => { const s = f.properties.slug; if (!PA[s]) return;
      lay.bindTooltip(nom(s) + (PA[s].cf ? ' · en conflicto' : ''), {sticky: true});
      lay.on('click', ev => { if (CREANDO) { L.DomEvent.stop(ev); crearEn(ev.latlng); return; } if (S.paises.includes(s)) popPais(s, ev.latlng); else alternarPais(s); }); }}).addTo(MAP);
  MAP.createPane('zonas').style.zIndex = 405; MAP.createPane('rutas').style.zIndex = 415;
  try { if ($('pp-verzonas')) $('pp-verzonas').checked = localStorage.getItem('a27pp-zonas') !== '0'; } catch(e) {}
  pintarZonas();
  CAPA_RUTA = L.layerGroup().addTo(MAP); CAPA_FR = L.layerGroup().addTo(MAP); CAPA_P = L.layerGroup().addTo(MAP); CAPA_SEL = L.layerGroup().addTo(MAP);
  MAP.on('contextmenu', ev => libre(ev.latlng));
  MAP.on('click', ev => { if (CREANDO) crearEn(ev.latlng); });
  encuadrar();
}
Promise.all([
  fetch(raiz + 'assets/js/planificador-puntos.json').then(r => r.json()),
  fetch(raiz + 'assets/js/africa.geo.json').then(r => r.json()),
]).then(([d, g]) => {
  d.puntos.forEach(p => { PUNTOS[p.id] = p; (PORPAIS[p.pais] = PORPAIS[p.pais] || []).push(p); });
  d.fronteras.filter(f => f.tipo === 'terrestre' && f.otro && f.fiable && f.oficial && ['abierta', 'revisar'].includes(f.estado)).forEach(f => {
    const k = f.pais < f.otro ? f.pais + '|' + f.otro : f.otro + '|' + f.pais; (FRPAR[k] = FRPAR[k] || []).push(f); });
  FRTODAS = d.fronteras.filter(f => f.tipo === 'terrestre' && f.otro);
  (d.sin_control || []).forEach(([a, b]) => { SINCTRL.add(a + '|' + b); SINCTRL.add(b + '|' + a); });
  const recPts = s => (PA[s] && PA[s].rec || []).flatMap(r => r.pts);
  Object.values(FRPAR).flat().forEach(f => { const q = [f.lat, f.lon]; f.cerca = recPts(f.pais).concat(recPts(f.otro)).some(x => hav(q, x) <= 25); });
  GEO = g; prepGeo(g);
  cargarPropios();
  iniciarMapa(); calcular();
  cargarDet();
  window.__A27_PP = () => R; window.__A27_PP_MAP = () => MAP;
}).catch(e => { msg('No se han podido cargar los datos de puntos: ' + esc(e && e.message || e)); });
})();

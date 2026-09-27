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
const VACIO = () => ({paises: [], ida: [], vuelta: [], libres: {}, dias: {}, fer_ida: '', fer_vuelta: '', salida: CFG.salida, kmdia: 300, margen: 10, nombre: ''});
let S;
try { S = Object.assign(VACIO(), JSON.parse(localStorage.getItem(KEY) || '{}') || {}); } catch(e) { S = VACIO(); }
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch(e) {} };
function msg(t){ const m = $('pp-msg'); m.innerHTML = t; m.hidden = !t; clearTimeout(msg.t); if (t) msg.t = setTimeout(() => { m.hidden = true; }, 4500); }

// ------------------------------------------------------------------ datos
let PUNTOS = {}, PORPAIS = {}, FRPAR = {}, FRTODAS = [], GEO = null, POLIS = [], SINCTRL = new Set();
const GRAFO = {};
CFG.fronteras.forEach(([a, b, t]) => { (GRAFO[a] = GRAFO[a] || []).push([b, t]); (GRAFO[b] = GRAFO[b] || []).push([a, t]); });
function punto(id){
  if (PUNTOS[id]) return PUNTOS[id];
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
  if (e) return {pts: inv ? e.p.slice().reverse() : e.p, km: e.km, real: true};
  if (!(Date.now() - (FALLO.get(key) || 0) < 60000) && !COLA.has(key)) { COLA.set(key, inv ? [b, a] : [a, b]); setTimeout(pedir, 0); }
  return {pts: [a, b], km: d * F, real: false};
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
  const act = new Set(S.paises), dist = {[a]: 0}, prev = {}, hecho = new Set();
  for (;;) {
    let u = null, m = Infinity;
    for (const k in dist) if (!hecho.has(k) && dist[k] < m) { m = dist[k]; u = k; }
    if (u === null || u === b) break;
    hecho.add(u);
    (GRAFO[u] || []).forEach(([v, t]) => {
      if (t === 'cerrada' || !PA[v] || !PA[v].pos || !PA[u] || !PA[u].pos) return;
      const libre = act.has(v) || v === b;
      if ((t === 'evitar' || PA[v].cf) && !libre) return;
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
  for (let i = 1; i < seq.length; i++) { const e = enlace(seq[i - 1].pos, seq[i].pos); tramos.push({a: seq[i - 1], b: seq[i], ...e, mitad: seq[i].mitad}); }
  // Km por país y países atravesados, en orden
  const kmPais = {}, runs = [];
  let kmTot = 0;
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
      if (!s) continue;
      const k = seg / len * t.km;
      kmPais[s] = (kmPais[s] || 0) + k;
      if (runs.length && runs[runs.length - 1].s === s) runs[runs.length - 1].km += k; else runs.push({s, km: k});
    }
  });
  // Un roce de menos de 10 km con otro país (carretera pegada a la frontera) no cuenta como entrada
  for (let i = runs.length - 2; i > 0; i--) if (runs[i].km < 10 && runs[i - 1].s === runs[i + 1].s) { runs[i - 1].km += runs[i].km + runs[i + 1].km; runs.splice(i, 2); }
  const orden = runs.map(x => x.s);
  const entradas = {}; orden.forEach(s => { entradas[s] = (entradas[s] || 0) + 1; });
  const act = new Set(S.paises.concat([FI.f.pais, FV.f.pais]));
  [...new Set(orden)].forEach(s => {
    if (PA[s] && PA[s].cf) avisos.push({rojo: true, t: `La ruta atraviesa <strong>${esc(nom(s))}</strong>: país en conflicto (el MAEC desaconseja el viaje).`});
    else if (!act.has(s) && (kmPais[s] || 0) > 3) avisos.push({rojo: false, t: `La ruta cruza <strong>${esc(nom(s))}</strong> (${num(kmPais[s])} km), que no has marcado: cuenta su visado y su frontera.`});
  });
  for (let i = 1; i < orden.length; i++) {
    const a = orden[i - 1], b = orden[i], e = (GRAFO[a] || []).find(([v]) => v === b);
    if (e && e[1] === 'cerrada') avisos.push({rojo: true, t: `La carretera pasa de ${esc(nom(a))} a ${esc(nom(b))} por una frontera <strong>cerrada</strong>.`});
  }
  const sinPerro = todos.filter(p => p.perro === 'no').length;
  if (sinPerro) avisos.push({rojo: false, t: `${sinPerro} punto${sinPerro > 1 ? 's' : ''} donde el perro no puede entrar (marcados en la lista).`});
  const aprox = tramos.filter(t => !t.real).length;
  if (aprox) avisos.push({rojo: false, t: FALLO.size ? `Sin respuesta del servidor de rutas: ${aprox} tramo${aprox > 1 ? 's' : ''} en línea recta (discontinua) con km aproximados.` : `Calculando la carretera de ${aprox} tramo${aprox > 1 ? 's' : ''}…`});
  // Días y fechas
  const kmdia = Math.max(50, +S.kmdia || 300), margen = Math.max(0, +S.margen || 0) / 100;
  const medio = h => Math.max(0.5, Math.ceil(h / 24 * 2) / 2);
  const dFerry = f => medio(f.h) + f.km_eu / kmdia;
  let t = dFerry(FI.f);
  const fechaPunto = {};
  tramos.forEach(tr => { t += tr.km / kmdia; if (tr.b.tipo === 'punto') { fechaPunto[tr.b.p.id] = t; t += diasDe(tr.b.p); } });
  const diasPais = {};
  Object.entries(kmPais).forEach(([s, k]) => { diasPais[s] = (diasPais[s] || 0) + k / kmdia; });
  todos.forEach(p => { if (p.pais) diasPais[p.pais] = (diasPais[p.pais] || 0) + diasDe(p); });
  const base = t + dFerry(FV.f), dias = Math.ceil(base * (1 + margen));
  R = {ida, vuelta, todos, FI, FV, seq, tramos, kmTot, kmPais, orden, entradas, avisos, dias, fechaPunto, diasPais, factor: 1 + margen};
  pintar();
}

// ------------------------------------------------------------------ mapa
let MAP, CAPA_P, CAPA_SEL, CAPA_RUTA, CAPA_FR, PAISES, ENCUADRE = false;
const COL = ['#1E7A8A', '#C47F17', '#2B6CB0', '#2E7D32', '#8B5A2B', '#673AB7', '#B43A3A', '#5F6B72'];
const colPais = s => { let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) >>> 0; return COL[h % COL.length]; };
function estiloPaises(){
  if (!PAISES) return;
  const act = new Set(S.paises), cruza = new Set(R ? R.orden : []);
  PAISES.eachLayer(l => {
    const s = l.feature.properties.slug, P0 = PA[s];
    let st = {weight: 1, color: '#8A949A', fillColor: '#ffffff', fillOpacity: .04, dashArray: null};
    if (P0 && P0.cf) st = {...st, fillColor: '#B43A3A', fillOpacity: act.has(s) ? .28 : .16, color: '#B43A3A', dashArray: '3 4'};
    if (act.has(s)) st = {...st, fillColor: P0 && P0.cf ? '#B43A3A' : '#1E7A8A', fillOpacity: P0 && P0.cf ? .3 : .16, color: P0 && P0.cf ? '#B43A3A' : '#1E7A8A', weight: 1.5};
    else if (cruza.has(s)) st = {...st, fillColor: '#D97B29', fillOpacity: .12, color: '#C47F17'};
    l.setStyle(st);
  });
}
function popPunto(p){
  const en = S.ida.includes(p.id) ? 'ida' : S.vuelta.includes(p.id) ? 'vuelta' : '';
  const pd = {si: 'perro: sí', condiciones: 'perro: con condiciones', no: 'perro: no', sin_dato: 'perro: sin dato'}[p.perro] || '';
  const ficha = p.libre ? '' : `<a href="${raiz}paises/${p.pais}/#poi-${p.n}" target="_blank" rel="noopener">Ver ficha</a>`;
  const acc = en
    ? `<button type="button" class="pp-b big ${en === 'ida' ? 'vuelta' : 'ida'}" data-pp="${en === 'ida' ? 'vuelta' : 'ida'}" data-id="${esc(p.id)}">Pasar a la ${en === 'ida' ? 'vuelta' : 'ida'}</button><button type="button" class="pp-b big x" data-pp="quitar" data-id="${esc(p.id)}">Quitar</button>`
    : `<button type="button" class="pp-b big ida" data-pp="ida" data-id="${esc(p.id)}">+ Ida</button><button type="button" class="pp-b big vuelta" data-pp="vuelta" data-id="${esc(p.id)}">+ Vuelta</button>`;
  return `<div class="pp-pop"><strong>${esc(p.nombre)}</strong><div class="meta">${esc(nom(p.pais))}${p.cat ? ' · ' + esc(p.cat) : ''}${p.prio ? ' · ' + esc(p.prio) : ''}${p.libre ? '' : ' · ' + num(diasDe(p), 2).replace(/,?0+$/, '') + ' d'}</div>${pd && !p.libre ? `<span class="perro ${p.perro}">${pd}</span>` : ''}<div class="acc">${acc}</div><div style="margin-top:6px;font-size:12px">${ficha}</div></div>`;
}
function pintarPuntos(){
  if (!CAPA_P) return;
  CAPA_P.clearLayers();
  const sel = new Set(S.ida.concat(S.vuelta)), act = $('pp-vertodos').checked ? null : new Set(S.paises);
  Object.values(PUNTOS).forEach(p => {
    if (sel.has(p.id) || (act && !act.has(p.pais))) return;
    const imp = /imprescindible/i.test(p.prio);
    L.circleMarker([p.lat, p.lon], {radius: imp ? 6.5 : 5, color: '#fff', weight: 1.5, fillColor: p.perro === 'no' ? '#8A949A' : '#46535B', fillOpacity: .9})
      .bindTooltip(esc(p.nombre)).bindPopup(() => popPunto(p), {maxWidth: 300}).addTo(CAPA_P);
  });
}
function pintarSel(){
  CAPA_SEL.clearLayers();
  let i = 0;
  [['ida', S.ida], ['vuelta', S.vuelta]].forEach(([m, lista]) => lista.forEach(id => {
    const p = punto(id); if (!p) return; i++;
    L.marker([p.lat, p.lon], {icon: L.divIcon({className: '', html: `<div class="pp-mk ${m}${p.libre ? ' libre' : ''}" style="width:24px;height:24px">${i}</div>`, iconSize: [24, 24], iconAnchor: [12, 12]}), zIndexOffset: 500})
      .bindTooltip(i + '. ' + esc(p.nombre)).bindPopup(() => popPunto(p), {maxWidth: 300}).addTo(CAPA_SEL);
  }));
}
function pintarRuta(){
  CAPA_RUTA.clearLayers(); CAPA_FR.clearLayers();
  if (!R) return;
  R.tramos.forEach(t => {
    if (t.pts.length < 2 || hav(t.pts[0], t.pts[t.pts.length - 1]) < .5) return;
    L.polyline(t.pts, {color: t.mitad === 'ida' ? '#1E7A8A' : '#C47F17', weight: 4, opacity: .85, dashArray: t.real ? null : '6 7'}).addTo(CAPA_RUTA);
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
      <span class="pp-t"><strong title="${esc(p.nombre)}">${esc(p.nombre)}</strong><small>${esc(nom(p.pais))}${f ? ' · ~' + f : ''}${perro}</small></span>
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
    $('pp-km').textContent = num(R.kmTot);
    $('pp-dias').textContent = num(R.dias);
    const ps = [...new Set(R.orden)];
    $('pp-np').textContent = ps.length;
    $('pp-fechas').textContent = R.todos.length ? `Salida ${fecha(addDays(S.salida, 0), true)} · regreso ~${fecha(addDays(S.salida, R.dias), true)} · ferry ${R.FI.f.origen} → ${R.FI.f.puerto} y ${R.FV.f.puerto} → ${R.FV.f.origen}` : '';
    const act = new Set(S.paises), totD = Object.values(R.diasPais).reduce((a, b) => a + b, 0) || 1;
    $('pp-tira').innerHTML = ps.map(s => `<i style="width:${(R.diasPais[s] || 0) / totD * 100}%;background:${colPais(s)}" title="${esc(nom(s))}: ~${num(R.diasPais[s] * R.factor, 1)} días"></i>`).join('');
    $('pp-paises').innerHTML = ps.map(s => `<span class="${act.has(s) ? '' : 'fuera'}" style="border-left:4px solid ${colPais(s)}">${esc(nom(s))} · ${num(R.kmPais[s] || 0)} km${R.entradas[s] > 1 ? ' · ' + R.entradas[s] + ' entradas' : ''}</span>`).join('');
    $('pp-avisos').innerHTML = R.avisos.map(a => `<li class="${a.rojo ? 'rojo' : ''}">${a.t}</li>`).join('');
  }
  $('pp-salida').value = S.salida || CFG.salida; $('pp-kmdia').value = S.kmdia; $('pp-margen').value = S.margen;
  if (MAP) { estiloPaises(); pintarPuntos(); pintarSel(); pintarRuta(); }
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
  L.popup({maxWidth: 320}).setLatLng(latlng).setContent(`<div class="pp-pop"><strong>${esc(nom(s))}</strong><div class="meta">${(PORPAIS[s] || []).length} puntos de interés${PA[s].cf ? ' · <b style="color:#B43A3A">país en conflicto</b>' : ''}</div>${recs ? '<div style="font-size:12px;margin-bottom:2px">Atajo: añadir los puntos de un recorrido de la ficha</div>' + recs : ''}<div class="acc" style="margin-top:8px"><button type="button" class="pp-b" data-ocultar="${s}">Ocultar sus puntos</button><a href="${raiz}paises/${s}/" target="_blank" rel="noopener" style="font-size:12px;align-self:center">Ficha del país</a></div></div>`).openOn(MAP);
}
function libre(latlng){
  const s = paisDe(latlng.lat, latlng.lng);
  if (!s) { msg('Ese punto no cae en ningún país del mapa.'); return; }
  const id = 'libre-' + Date.now().toString(36);
  S.libres[id] = {lat: Math.round(latlng.lat * 1e5) / 1e5, lon: Math.round(latlng.lng * 1e5) / 1e5, pais: s, nombre: 'Paso por aquí · ' + nom(s)};
  const p = punto(id);
  L.popup({maxWidth: 300}).setLatLng(latlng).setContent(popPunto(p)).openOn(MAP);
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
function exportar(){
  const blob = new Blob([JSON.stringify({app: 'a27-planificador-puntos', v: 1, viajes: leerV(), actual: S}, null, 1)], {type: 'application/json'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'viajes-por-puntos-africa-2027.json'; document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
}
function importar(file){
  const rd = new FileReader();
  rd.onload = () => { try { const j = JSON.parse(rd.result); if (j.app !== 'a27-planificador-puntos') throw 0;
    const V = leerV(); Object.assign(V, j.viajes || {}); escV(V); paintViajes(); msg(`${Object.keys(j.viajes || {}).length} viajes importados.`); }
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
  const b = e.target.closest('[data-pp]'); if (b) { mover(b.dataset.id, b.dataset.pp); return; }
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
  if (e.target.id === 'pp-verfr') pintarRuta();
  if (e.target.id === 'pp-vertodos') pintarPuntos();
  if (e.target.id === 'pp-importar' && e.target.files[0]) { importar(e.target.files[0]); e.target.value = ''; }
});
$('pp-ord-ida').addEventListener('click', () => ordenar('ida'));
$('pp-ord-vuelta').addEventListener('click', () => ordenar('vuelta'));
$('pp-guardar').addEventListener('click', guardarViaje);
$('pp-cargar').addEventListener('click', cargarViaje);
$('pp-borrar').addEventListener('click', borrarViaje);
$('pp-exportar').addEventListener('click', exportar);
$('pp-vnombre').addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); guardarViaje(); } });
$('pp-nuevo').addEventListener('click', () => { if (!confirm('¿Empezar un viaje nuevo? El actual se pierde si no lo has guardado.')) return; S = VACIO(); save(); calcular(); encuadrar(); });
if (window.Sortable) ['pp-lista-ida', 'pp-lista-vuelta'].forEach(id => Sortable.create($(id), {group: 'pp', handle: '.pp-h', animation: 150,
  onEnd: () => { S.ida = [...$('pp-lista-ida').children].map(li => li.dataset.id); S.vuelta = [...$('pp-lista-vuelta').children].map(li => li.dataset.id); save(); calcular(); }}));

// ------------------------------------------------------------------ arranque
function iniciarMapa(){
  if (typeof L === 'undefined' || !$('pp-mapa')) return;
  MAP = L.map('pp-mapa', {zoomSnap: 0.25, scrollWheelZoom: true}).fitBounds([[-35, -18], [37, 52]]);
  L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {maxZoom: 15, attribution: 'Teselas © Esri'}).addTo(MAP);
  PAISES = L.geoJSON(GEO, {style: () => ({weight: 1, color: '#8A949A', fillOpacity: .04, fillColor: '#fff'}),
    onEachFeature: (f, lay) => { const s = f.properties.slug; if (!PA[s]) return;
      lay.bindTooltip(nom(s) + (PA[s].cf ? ' · en conflicto' : ''), {sticky: true});
      lay.on('click', ev => { if (S.paises.includes(s)) popPais(s, ev.latlng); else alternarPais(s); }); }}).addTo(MAP);
  CAPA_RUTA = L.layerGroup().addTo(MAP); CAPA_FR = L.layerGroup().addTo(MAP); CAPA_P = L.layerGroup().addTo(MAP); CAPA_SEL = L.layerGroup().addTo(MAP);
  MAP.on('contextmenu', ev => libre(ev.latlng));
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
  iniciarMapa(); calcular();
  window.__A27_PP = () => R; window.__A27_PP_MAP = () => MAP;
}).catch(e => { msg('No se han podido cargar los datos de puntos: ' + esc(e && e.message || e)); });
})();

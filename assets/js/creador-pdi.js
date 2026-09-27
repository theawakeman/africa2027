/* Creador de puntos · África 2027
   Marcas un sitio en el mapa, eliges el tipo y escribes una frase; la app busca
   sola el lugar (OpenStreetMap), el artículo de Wikipedia, fotos de Wikimedia
   Commons, los servicios de alrededor (OpenStreetMap) y el clima (Open-Meteo).
   Se guarda en este navegador ('a27-pdi-propios') y se puede publicar en la web
   (content/pois/<país>.json o la logística de content/ficha/<país>.json) con el
   mismo token del panel de edición. Todo punto creado aquí queda «por revisar». */
(function(){
'use strict';
const KEY = 'a27-pdi-propios', REPO = 'theawakeman/africa2027', BRANCH = 'main';
const API = 'https://api.github.com/repos/' + REPO;
const TIPOS = [
  {id: 'naturaleza', l: 'Naturaleza', cat: 'Naturaleza', color: 'verde', clase: 'pdi', dias: 1},
  {id: 'cultura', l: 'Cultura', cat: 'Cultura', color: 'morado', clase: 'pdi', dias: 1},
  {id: 'ciudad', l: 'Ciudad · servicios', cat: 'Ciudad · servicios', color: 'azul', clase: 'pdi', dias: 1},
  {id: 'costa', l: 'Costa', cat: 'Costa', color: 'turquesa', clase: 'pdi', dias: 1},
  {id: 'unesco', l: 'Patrimonio UNESCO', cat: 'Patrimonio UNESCO', color: 'marron', clase: 'pdi', dias: 1},
  {id: 'agua', l: 'Agua de servicio (ducha, lavado)', cat: 'Agua de servicio', clase: 'log', osm: 'agua', dias: 0},
  {id: 'potable', l: 'Agua potable', cat: 'Agua potable', clase: 'log', osm: 'agua', dias: 0},
  {id: 'combustible', l: 'Combustible', cat: 'Combustible', clase: 'log', osm: 'fuel', dias: 0},
  {id: 'camping', l: 'Camping o pernocta', cat: 'Servicio', pref: 'Camping / pernocta', clase: 'log', osm: 'camp', dias: 0.5},
  {id: 'taller', l: 'Taller o recambios', cat: 'Servicio', pref: 'Taller', clase: 'log', osm: 'taller', dias: 0},
  {id: 'hospital', l: 'Hospital o clínica', cat: 'Hospital', clase: 'log', osm: 'salud', dias: 0},
  {id: 'frontera', l: 'Paso fronterizo', cat: 'Frontera', clase: 'log', dias: 0},
  {id: 'servicio', l: 'Otro servicio', cat: 'Servicio', clase: 'log', dias: 0},
];
const tipo = id => TIPOS.find(t => t.id === id) || TIPOS[0];
// Textos que los clasificadores de la web (build.dog_cls y planificador_puntos.perro) leen igual que los de las fichas
const PERRO = {si: 'permitido', condiciones: 'con condiciones: requiere autorización o normas del lugar', no: 'prohibido', sin_dato: 'pendiente de confirmar'};
const PERRO_CLS = {si: 'st-green', condiciones: 'st-amber', no: 'st-red', sin_dato: 'st-grey'};
const MES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];
const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const txt = html => { try { return (new DOMParser().parseFromString(String(html || ''), 'text/html').body.textContent || '').replace(/\s+/g, ' ').trim(); } catch(e) { return String(html || ''); } };
const corta = (s, n) => s.length > n ? s.slice(0, n - 1).replace(/\s+\S*$/, '') + '…' : s;
function hav(a, b){
  const p1 = a[0] * Math.PI / 180, p2 = b[0] * Math.PI / 180, dl = (b[1] - a[1]) * Math.PI / 180;
  const h = Math.sin((p2 - p1) / 2) ** 2 + Math.cos(p1) * Math.cos(p2) * Math.sin(dl / 2) ** 2;
  return 2 * 6371 * Math.asin(Math.min(1, Math.sqrt(h)));
}
const km = d => d < 1 ? Math.round(d * 1000) + ' m' : (Math.round(d * 10) / 10).toString().replace('.', ',') + ' km';
async function getJSON(url, opt, ms){
  const ac = new AbortController(), t = setTimeout(() => ac.abort(), ms || 20000);
  try { const r = await fetch(url, {...(opt || {}), signal: ac.signal}); if (!r.ok) throw new Error('HTTP ' + r.status); return await r.json(); }
  finally { clearTimeout(t); }
}

// ------------------------------------------------------------------ almacén local
function lista(){ try { const v = JSON.parse(localStorage.getItem(KEY) || '[]'); return Array.isArray(v) ? v : []; } catch(e) { return []; } }
function guardarLista(v){ try { localStorage.setItem(KEY, JSON.stringify(v)); return true; } catch(e) { return false; } }
function guardar(o){ const v = lista().filter(x => x.id !== o.id); v.push(o); return guardarLista(v); }
function borrar(id){ guardarLista(lista().filter(x => x.id !== id)); }

// ------------------------------------------------------------------ fuentes
async function lugar(lat, lon){
  const j = await getJSON(`https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lon}&zoom=14&accept-language=es`, null, 15000);
  const a = j.address || {};
  const loc = a.village || a.town || a.city || a.hamlet || a.municipality || a.suburb || a.county || '';
  return {loc, region: a.state || a.region || a.county || '', pais: a.country || '', nombre: j.name || '', display: j.display_name || ''};
}
// Wikipedia: candidatos por nombre (si se ha escrito) y por cercanía, puntuados para que salga lo interesante
// del sitio y no lo que por casualidad está más cerca (aeropuertos, colegios, estaciones…). Se puede cambiar en el paso 2.
const GENERICAS = /\b(ciudad|pueblo|villa|poblado|zona|regi[oó]n|de|del|la|el|los|las|en|the|of|city|town)\b/gi;
const FEOS = /(aeropuerto|airport|a[ée]roport|aer[oó]dromo|estaci[oó]n|station|gare|escuela|school|[ée]cole|colegio|lyc[ée]e|universi|hospital|h[oô]pital|estadio|stadium|stade|hotel|h[oô]tel|banco|bank|embajada|consulado|prisi[oó]n|prison|club|f[uú]tbol|football|elecci[oó]n|election|batalla de|battle of)/i;
const TIPO_PUNTOS = {landmark: -4, mountain: -4, isle: -4, waterbody: -4, river: -3, pass: -3, forest: -3, glacier: -3, city: -1, adm3rd: 0, adm2nd: 2, adm1st: 4, airport: 20, edu: 20, railwaystation: 15, event: 10};
const norm = s => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
async function candidatosWiki(lat, lon, nombre, radio){
  const limpio = (nombre || '').replace(GENERICAS, ' ').replace(/\s+/g, ' ').trim();
  const palabras = norm(limpio).split(/\W+/).filter(w => w.length > 2);
  const todos = [];
  await Promise.all(['es', 'fr', 'en'].map(async (lang, li) => {
    const base = `https://${lang}.wikipedia.org/w/api.php?format=json&origin=*&action=query`;
    const pide = [getJSON(`${base}&list=geosearch&gscoord=${lat}|${lon}&gsradius=${radio}&gslimit=20&gsprop=type`, null, 15000).catch(() => null)];
    if (limpio) pide.push(getJSON(`${base}&generator=search&gsrsearch=${encodeURIComponent(limpio)}&gsrlimit=8&prop=coordinates&coprimary=primary`, null, 15000).catch(() => null));
    const [g, b] = await Promise.all(pide);
    ((g && g.query && g.query.geosearch) || []).forEach(x => todos.push({lang, titulo: x.title, dist: x.dist, tipo: x.type || '', por: 'cerca', li}));
    Object.values((b && b.query && b.query.pages) || {}).forEach(pg => { const c = pg.coordinates && pg.coordinates[0]; if (!c) return;
      const d = hav([lat, lon], [c.lat, c.lon]) * 1000; if (d > 60000) return;
      todos.push({lang, titulo: pg.title, dist: d, tipo: '', por: 'nombre', rango: pg.index || 1, li}); });
  }));
  todos.forEach(x => {
    let p = x.dist / 1000 + (TIPO_PUNTOS[x.tipo] || 0) + x.li * 0.5 + (FEOS.test(x.titulo) ? 25 : 0);
    if (x.por === 'nombre') p += -12 + (x.rango - 1) * 2;
    if (palabras.length && palabras.some(w => norm(x.titulo).includes(w))) p -= 15;
    x.p = p;
  });
  const vistos = new Set(), out = [];
  // El mismo artículo en otro idioma cuenta una sola vez (se queda el mejor puntuado, normalmente en español)
  todos.sort((a, b) => a.p - b.p).forEach(x => { const k = norm(x.titulo).replace(/[^a-z0-9]/g, ''); if (!vistos.has(k)) { vistos.add(k); out.push(x); } });
  return out.slice(0, 8);
}
async function resumenWiki(c){
  const s = await getJSON(`https://${c.lang}.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(c.titulo)}`, null, 15000).catch(() => null);
  if (!s || !s.extract) return null;
  return {lang: c.lang, titulo: s.title, dist: c.dist, extracto: s.extract, url: s.content_urls && s.content_urls.desktop ? s.content_urls.desktop.page : '',
    wikidata: s.wikibase_item || '', imagen: s.originalimage ? s.originalimage.source : ''};
}
async function wikipedia(lat, lon, nombre, radio){
  const cand = await candidatosWiki(lat, lon, nombre, radio);
  for (const c of cand.slice(0, 3)) { const r = await resumenWiki(c); if (r) return {...r, candidatos: cand}; }
  return cand.length ? {candidatos: cand, vacio: true} : null;
}
// Coordenadas en cualquier formato habitual: decimales, grados-minutos-segundos o enlace de Google Maps
function coords(t){
  t = String(t || '').trim();
  let m = t.match(/@(-?\d+\.\d+),(-?\d+\.\d+)/) || t.match(/!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)/) || t.match(/[?&](?:q|ll|query|destination)=(-?\d+\.?\d*)\s*(?:,|%2C)\s*(-?\d+\.?\d*)/i);
  if (m) return [+m[1], +m[2]];
  const dms = [...t.matchAll(/(\d+(?:[.,]\d+)?)\s*[°º]\s*(?:(\d+(?:[.,]\d+)?)\s*['’′])?\s*(?:(\d+(?:[.,]\d+)?)\s*(?:["”″]|''))?\s*([NSEWOnsewo])/g)];
  if (dms.length === 2) { const v = dms.map(x => { const d = +x[1].replace(',', '.') + (+(x[2] || '0').replace(',', '.')) / 60 + (+(x[3] || '0').replace(',', '.')) / 3600; return /[SWOswo]/.test(x[4]) ? -d : d; });
    return /[NSns]/.test(dms[0][4]) ? v : [v[1], v[0]]; }
  m = t.match(/^(-?\d+(?:\.\d+)?)\s*°?\s*([NS])?[\s,;]+(-?\d+(?:\.\d+)?)\s*°?\s*([EWO])?$/i);
  if (m) { let a = +m[1], b = +m[3]; if (m[2] && /s/i.test(m[2])) a = -Math.abs(a); if (m[4] && /[wo]/i.test(m[4])) b = -Math.abs(b); return [a, b]; }
  return null;
}
async function fotos(lat, lon, radio){
  const j = await getJSON(`https://commons.wikimedia.org/w/api.php?action=query&generator=geosearch&ggscoord=${lat}|${lon}&ggsradius=${radio}&ggsnamespace=6&ggslimit=30&prop=imageinfo|coordinates&iiprop=url|extmetadata|size|mime&iiurlwidth=1200&format=json&origin=*`, null, 20000);
  const pags = Object.values((j.query && j.query.pages) || {}).sort((a, b) => (a.index || 0) - (b.index || 0));
  return pags.filter(p => p.imageinfo && p.imageinfo[0] && /image\/(jpeg|png)/.test(p.imageinfo[0].mime || '') && (p.imageinfo[0].width || 0) >= 640
      && !/\b(map|mapa|carte|karte|logo|flag|bandera|drapeau|locator|location|plan|diagram)\b/i.test(p.title))
    .slice(0, 12).map(foto);
}
function foto(p){
  const ii = p.imageinfo[0], m = ii.extmetadata || {}, f = p.title.replace(/^File:/, '');
  const autor = corta(txt(m.Artist && m.Artist.value) || 'Autor en Commons', 60), lic = txt(m.LicenseShortName && m.LicenseShortName.value);
  const pie = corta(txt(m.ImageDescription && m.ImageDescription.value) || txt(m.ObjectName && m.ObjectName.value) || f.replace(/\.[a-z]+$/i, '').replace(/_/g, ' '), 140);
  return {img: 'https://commons.wikimedia.org/wiki/Special:FilePath/' + encodeURIComponent(f.replace(/ /g, '_')) + '?width=1200', thumb: ii.thumburl || ii.url,
    source: ii.descriptionurl || 'https://commons.wikimedia.org/wiki/' + encodeURIComponent(p.title.replace(/ /g, '_')),
    credit: autor + (lic ? ' · ' + lic : ''), caption: pie};
}
async function fotoDe(fichero){
  const j = await getJSON(`https://commons.wikimedia.org/w/api.php?action=query&titles=${encodeURIComponent('File:' + fichero)}&prop=imageinfo&iiprop=url|extmetadata|size|mime&iiurlwidth=1200&format=json&origin=*`, null, 15000);
  const p = Object.values((j.query && j.query.pages) || {})[0];
  return p && p.imageinfo ? foto(p) : null;
}
const OSM_TIPOS = [
  ['fuel', 'gasolineras', '["amenity"="fuel"]'], ['agua', 'puntos de agua', '["amenity"~"^(drinking_water|water_point)$"]'],
  ['camp', 'campings', '["tourism"~"^(camp_site|caravan_site)$"]'], ['salud', 'hospitales o clínicas', '["amenity"~"^(hospital|clinic)$"]'],
  ['taller', 'talleres', '["shop"~"^(car_repair|tyres|car_parts)$"]'],
];
async function servicios(lat, lon, radio){
  const q = '[out:json][timeout:25];(' + OSM_TIPOS.map(t => `nwr(around:${radio},${lat},${lon})${t[2]};`).join('') + ');out center 120;';
  const j = await getJSON('https://overpass-api.de/api/interpreter', {method: 'POST', body: 'data=' + encodeURIComponent(q)}, 30000);
  const res = {};
  (j.elements || []).forEach(e => {
    const la = e.lat != null ? e.lat : e.center && e.center.lat, lo = e.lon != null ? e.lon : e.center && e.center.lon, tg = e.tags || {};
    if (la == null) return;
    const k = tg.amenity === 'fuel' ? 'fuel' : /drinking_water|water_point/.test(tg.amenity || '') ? 'agua' : tg.tourism ? 'camp' : /hospital|clinic/.test(tg.amenity || '') ? 'salud' : tg.shop ? 'taller' : '';
    if (!k) return;
    const d = hav([lat, lon], [la, lo]);
    (res[k] = res[k] || []).push({d, nombre: tg.name || tg.brand || tg.operator || '', lat: la, lon: lo});
  });
  Object.values(res).forEach(v => v.sort((a, b) => a.d - b.d));
  return res;
}
async function clima(lat, lon){
  const j = await getJSON(`https://archive-api.open-meteo.com/v1/archive?latitude=${lat}&longitude=${lon}&start_date=2024-01-01&end_date=2024-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=UTC`, null, 20000);
  const d = j.daily || {}, M = MES.map(() => ({mx: [], mn: [], p: 0}));
  (d.time || []).forEach((t, i) => { const m = +t.slice(5, 7) - 1; if (d.temperature_2m_max[i] != null) M[m].mx.push(d.temperature_2m_max[i]); if (d.temperature_2m_min[i] != null) M[m].mn.push(d.temperature_2m_min[i]); M[m].p += d.precipitation_sum[i] || 0; });
  const med = a => a.length ? a.reduce((s, x) => s + x, 0) / a.length : null;
  return M.map((x, i) => ({mes: MES[i], mx: med(x.mx), mn: med(x.mn), p: x.p}));
}
function textoClima(C){
  if (!C || C.every(m => m.mx == null)) return '';
  const r = n => Math.round(n);
  const ord = C.slice().filter(m => m.mx != null).sort((a, b) => a.mx - b.mx), frio = ord[0], cal = ord[ord.length - 1];
  const lluv = C.filter(m => m.p >= 60).map(m => m.mes), total = r(C.reduce((s, m) => s + m.p, 0));
  let comodos = C.filter(m => m.mx != null && m.mx <= 33 && m.p < 60).map(m => m.mes);
  if (!comodos.length) comodos = ord.slice(0, 3).map(m => m.mes);
  return `Clima de referencia (Open-Meteo, año 2024): máximas medias de ${r(frio.mx)} °C (${frio.mes}) a ${r(cal.mx)} °C (${cal.mes}); mínimas de ${r(Math.min(...C.filter(m => m.mn != null).map(m => m.mn)))} °C. `
    + (lluv.length ? `Lluvias fuertes en ${lluv.join(', ')} (${total} mm en el año). ` : `Año seco (${total} mm). `) + `Meses más cómodos: ${comodos.join(', ')}.`;
}
function textoServicios(S, radio){
  if (!S) return '';
  const partes = OSM_TIPOS.filter(t => S[t[0]] && S[t[0]].length).map(t => { const v = S[t[0]], c = v[0];
    return `${v.length} ${t[1]} (la más cercana a ${km(c.d)}${c.nombre ? ': ' + c.nombre : ''})`; });
  return partes.length ? `Alrededores según OpenStreetMap (radio ${radio / 1000} km): ${partes.join('; ')}.` : `OpenStreetMap no registra gasolineras, agua, campings ni talleres a menos de ${radio / 1000} km: llevar autonomía.`;
}

// ------------------------------------------------------------------ interfaz
const CSS = `
dialog.a27c{border:0;border-radius:14px;padding:0;width:min(720px,calc(100vw - 24px));max-height:calc(100vh - 24px);overflow:auto;background:var(--surface);color:var(--ink);box-shadow:0 12px 50px rgba(0,0,0,.4);font-family:"Archivo",sans-serif}
dialog.a27c::backdrop{background:rgba(10,20,30,.6)}
.a27c-h{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:14px 18px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--surface);z-index:2}
.a27c-h h2{margin:0;font-size:18px;color:var(--head)}
.a27c-x{border:0;background:var(--surface2);color:var(--ink);width:34px;height:34px;border-radius:50%;font-size:20px;cursor:pointer}
.a27c-b{padding:14px 18px;display:flex;flex-direction:column;gap:10px}
.a27c-b label{display:flex;flex-direction:column;gap:4px;font-size:12.5px;font-weight:600;color:var(--ink-soft)}
.a27c-b input,.a27c-b select,.a27c-b textarea{font:inherit;font-size:14px;font-weight:400;padding:7px 9px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink)}
.a27c-b textarea{min-height:64px;resize:vertical}
.a27c-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}
.a27c-coord{font-size:12.5px;color:var(--ink-soft)}
.a27c-btns{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.a27c-btn{font:600 13.5px "Archivo",sans-serif;padding:9px 14px;border-radius:8px;border:1px solid var(--line);background:var(--surface);color:var(--ink);cursor:pointer}
.a27c-btn.pri{background:#1E7A8A;border-color:#1E7A8A;color:#fff}
.a27c-btn.pub{background:#C47F17;border-color:#C47F17;color:#fff}
.a27c-btn.x{color:#B43A3A}
.a27c-btn:disabled{opacity:.5;cursor:default}
.a27c-est{list-style:none;margin:0;padding:0;font-size:13px;display:grid;gap:3px}
.a27c-est li::before{content:"· ";color:var(--ink-soft)}
.a27c-est li.ok::before{content:"✓ ";color:#2E7D32;font-weight:700}
.a27c-est li.no::before{content:"— ";color:var(--ink-soft)}
.a27c-est li.err::before{content:"✕ ";color:#B43A3A;font-weight:700}
.a27c-fotos{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:8px}
.a27c-fotos label{position:relative;display:block;cursor:pointer;border-radius:8px;overflow:hidden;border:2px solid transparent}
.a27c-fotos label.on{border-color:#1E7A8A}
.a27c-fotos img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block;background:var(--surface2)}
.a27c-fotos input{position:absolute;top:6px;left:6px;width:18px;height:18px}
.a27c-fotos span{display:block;font-size:10.5px;font-weight:400;padding:3px 5px;color:var(--ink-soft);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.a27c-prev{border:1px solid var(--line);border-radius:12px;overflow:hidden}
.a27c-nota{font-size:12.5px;color:var(--ink-soft);margin:0}
.a27c-aviso{font-size:13px;background:var(--amber-bg);border-radius:8px;padding:8px 10px;margin:0}
`;
let DLG = null, ESTADO = null, CB = {};
function dialogo(){
  if (DLG) return DLG;
  const st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
  DLG = document.createElement('dialog'); DLG.className = 'a27c'; DLG.setAttribute('aria-labelledby', 'a27c-t');
  DLG.addEventListener('click', e => { if (e.target === DLG) DLG.close(); });
  document.body.appendChild(DLG);
  return DLG;
}
function paso1(){
  const o = ESTADO, t = tipo(o.tipo);
  DLG.innerHTML = `<div class="a27c-h"><h2 id="a27c-t">${o.editar ? 'Editar punto' : 'Crear un punto'}</h2><button type="button" class="a27c-x" data-c="cerrar" aria-label="Cerrar">×</button></div>
  <div class="a27c-b">
    <label>Coordenadas GPS <small style="font-weight:400">(decimales, grados-minutos-segundos o un enlace de Google Maps)</small>
      <input id="a27c-coords" value="${o.lat.toFixed(5)}, ${o.lon.toFixed(5)}" autocomplete="off" inputmode="text" data-1p-ignore data-lpignore="true"></label>
    <div class="a27c-coord" id="a27c-coordinfo">📍 ${esc(o.paisNombre || 'país sin detectar')} · <a href="https://www.google.com/maps?q=${o.lat},${o.lon}" target="_blank" rel="noopener">ver en Google Maps</a></div>
    <label>Tipo<select id="a27c-tipo"><optgroup label="Punto de interés">${TIPOS.filter(x => x.clase === 'pdi').map(x => `<option value="${x.id}" ${x.id === o.tipo ? 'selected' : ''}>${esc(x.l)}</option>`).join('')}</optgroup>
      <optgroup label="Logística">${TIPOS.filter(x => x.clase === 'log').map(x => `<option value="${x.id}" ${x.id === o.tipo ? 'selected' : ''}>${esc(x.l)}</option>`).join('')}</optgroup></select></label>
    <label>Nombre <small style="font-weight:400">(si lo dejas vacío, lo busca la app)</small><input id="a27c-nombre" value="${esc(o.nombre || '')}" autocomplete="off" data-1p-ignore data-lpignore="true"></label>
    <label>Qué es y por qué te interesa<textarea id="a27c-texto" placeholder="Una o dos frases: qué hay aquí y por qué merece la parada">${esc(o.texto || '')}</textarea></label>
    <div class="a27c-g">
      ${t.clase === 'pdi' ? `<label>Prioridad<select id="a27c-prio">${['Alta', 'Media', 'Baja'].map(p => `<option ${p === (o.prio || 'Media') ? 'selected' : ''}>${p}</option>`).join('')}</select></label>` : ''}
      <label>Días en el punto<input id="a27c-dias" type="number" min="0" step="0.5" value="${o.dias != null ? o.dias : t.dias}"></label>
      <label>Perro<select id="a27c-perro">${Object.entries({sin_dato: 'Sin dato', si: 'Sí', condiciones: 'Con condiciones', no: 'No'}).map(([k, l]) => `<option value="${k}" ${k === (o.perro || 'sin_dato') ? 'selected' : ''}>${l}</option>`).join('')}</select></label>
    </div>
    <label>Nota sobre el perro <small style="font-weight:400">(opcional)</small><input id="a27c-perronota" value="${esc(o.perroNota || '')}" autocomplete="off" data-1p-ignore data-lpignore="true"></label>
    <div class="a27c-btns"><button type="button" class="a27c-btn pri" data-c="completar">Completar automáticamente</button><span class="a27c-nota">Busca el lugar, Wikipedia, fotos, servicios cercanos y el clima (20–40 s).</span></div>
  </div>`;
}
function ponerCoords(){
  const el = document.getElementById('a27c-coords'); if (!el) return true;
  const c = coords(el.value), o = ESTADO, info = document.getElementById('a27c-coordinfo');
  if (!c || !(Math.abs(c[0]) <= 90 && Math.abs(c[1]) <= 180)) { if (info) info.innerHTML = '⚠️ No entiendo esas coordenadas. Ejemplos: 23.7136, -15.9355 · 23°42\'49"N 15°56\'08"W · un enlace de Google Maps'; return false; }
  if (Math.abs(c[0] - o.lat) > 1e-6 || Math.abs(c[1] - o.lon) > 1e-6) {
    o.lat = c[0]; o.lon = c[1];
    if (CB.paisDe) { const s = CB.paisDe(o.lat, o.lon); o.pais = s || ''; o.paisNombre = s && CB.nom ? CB.nom(s) : (s || ''); }
    o.auto = null;
  }
  if (info) info.innerHTML = `📍 ${esc(o.paisNombre || 'país sin detectar')} · <a href="https://www.google.com/maps?q=${o.lat},${o.lon}" target="_blank" rel="noopener">ver en Google Maps</a>`;
  return true;
}
function leerForm(){
  const o = ESTADO, v = id => { const el = document.getElementById(id); return el ? el.value : ''; };
  ponerCoords();
  o.tipo = v('a27c-tipo') || o.tipo; o.nombre = v('a27c-nombre').trim(); o.texto = v('a27c-texto').trim();
  o.prio = v('a27c-prio') || o.prio || 'Media'; o.dias = parseFloat(v('a27c-dias')); if (!isFinite(o.dias)) o.dias = tipo(o.tipo).dias;
  o.perro = v('a27c-perro') || 'sin_dato'; o.perroNota = v('a27c-perronota').trim();
}
async function completar(){
  if (!ponerCoords()) return;
  leerForm();
  const o = ESTADO, t = tipo(o.tipo), pdi = t.clase === 'pdi';
  if (!o.texto) { const ta = document.getElementById('a27c-texto'); ta.focus(); ta.placeholder = 'Escribe al menos una frase: es lo único que la app no puede inventar'; return; }
  const pasos = [['lugar', 'Lugar (OpenStreetMap)'], ...(pdi ? [['wiki', 'Wikipedia'], ['fotos', 'Fotos (Wikimedia Commons)']] : []), ['serv', 'Servicios cercanos (OpenStreetMap)'], ['clima', 'Clima (Open-Meteo)']];
  DLG.querySelector('.a27c-b').innerHTML = `<p class="a27c-nota">Buscando información de «${esc(o.nombre || o.texto.slice(0, 40))}»…</p><ul class="a27c-est">${pasos.map(([k, l]) => `<li id="a27c-e-${k}">${l}…</li>`).join('')}</ul>`;
  const marca = (k, cls, extra) => { const li = document.getElementById('a27c-e-' + k); if (li) { li.className = cls; li.textContent = pasos.find(p => p[0] === k)[1] + (extra ? ': ' + extra : ''); } };
  const R = o.auto = {};
  const radioServ = pdi ? 20000 : 3000;
  await Promise.all([
    lugar(o.lat, o.lon).then(x => { R.lugar = x; marca('lugar', 'ok', [x.loc, x.region].filter(Boolean).join(', ') || x.display.slice(0, 60)); }).catch(e => marca('lugar', 'err', 'sin respuesta')),
    pdi ? wikipedia(o.lat, o.lon, o.nombre, 10000).then(x => { R.wiki = x; marca('wiki', x && !x.vacio ? 'ok' : 'no', x && !x.vacio ? `${x.titulo} (${x.lang}, a ${km(x.dist / 1000)})` : 'ningún artículo a menos de 10 km'); }).catch(() => marca('wiki', 'err', 'sin respuesta')) : null,
    pdi ? fotos(o.lat, o.lon, 3000).then(async x => { if (x.length < 3) { const y = await fotos(o.lat, o.lon, 10000).catch(() => []); x = x.concat(y.filter(f => !x.some(g => g.source === f.source))); }
      R.fotos = x; marca('fotos', x.length ? 'ok' : 'no', x.length ? x.length + ' encontradas' : 'ninguna cerca'); }).catch(() => marca('fotos', 'err', 'sin respuesta')) : null,
    servicios(o.lat, o.lon, radioServ).then(x => { R.serv = x; R.radioServ = radioServ; const n = Object.values(x).reduce((s, v) => s + v.length, 0); marca('serv', 'ok', n + ' encontrados'); }).catch(() => marca('serv', 'err', 'sin respuesta (el servidor de OpenStreetMap va lento)')),
    clima(o.lat, o.lon).then(x => { R.clima = x; marca('clima', 'ok'); }).catch(() => marca('clima', 'err', 'sin respuesta')),
  ]);
  // Si el Wikipedia trae foto de Commons, va la primera
  if (R.wiki && R.wiki.imagen && /upload\.wikimedia\.org\/wikipedia\/commons\//.test(R.wiki.imagen)) {
    const f = decodeURIComponent(R.wiki.imagen.split('/').pop());
    const fw = await fotoDe(f).catch(() => null) || {img: 'https://commons.wikimedia.org/wiki/Special:FilePath/' + encodeURIComponent(f) + '?width=1200', thumb: R.wiki.imagen,
      source: 'https://commons.wikimedia.org/wiki/File:' + encodeURIComponent(f), credit: 'Wikimedia Commons (autor y licencia en la fuente)', caption: R.wiki.titulo};
    if (!fw.caption || /^File:|\.(jpe?g|png)$/i.test(fw.caption)) fw.caption = R.wiki.titulo;
    R.fotos = [fw].concat((R.fotos || []).filter(x => decodeURIComponent(x.source).replace(/ /g, '_').split('File:').pop() !== f.replace(/ /g, '_')));
  }
  o.elegidas = (R.fotos || []).slice(0, 3).map(f => f.source);
  armar(); paso2();
}
function armar(){
  const o = ESTADO, t = tipo(o.tipo), R = o.auto || {}, pdi = t.clase === 'pdi';
  const loc = R.lugar ? [R.lugar.loc, R.lugar.region].filter(Boolean).join(', ') : '';
  const w = R.wiki && !R.wiki.vacio && pdi && (R.wiki.elegido || R.wiki.dist <= 3000 || (o.nombre && o.nombre.length > 3)) ? R.wiki : null;
  const nombre = o.nombre || (w && w.dist <= 2000 ? w.titulo : '') || (t.pref ? t.pref + (loc ? ' · ' + loc : '') : (R.lugar && (R.lugar.nombre || R.lugar.loc)) || 'Punto propio');
  const frases = w ? w.extracto.split(/(?<=\.)\s+/) : [];
  const serv = textoServicios(R.serv, R.radioServ || 20000), cli = textoClima(R.clima);
  const fotosSel = (R.fotos || []).filter(f => (o.elegidas || []).includes(f.source)).map(({img, source, credit, caption}) => ({img, source, credit, caption}));
  const links = [];
  if (w && w.url) links.push({label: `Wikipedia (${w.lang}): ${w.titulo}`, url: w.url});
  if (w && w.wikidata) links.push({label: 'Wikidata', url: 'https://www.wikidata.org/wiki/' + w.wikidata});
  links.push({label: 'OpenStreetMap', url: `https://www.openstreetmap.org/?mlat=${o.lat}&mlon=${o.lon}#map=15/${o.lat}/${o.lon}`});
  links.push({label: 'Google Maps', url: `https://www.google.com/maps?q=${o.lat},${o.lon}`});
  const hoy = new Date().toISOString().slice(0, 10);
  const propio = {creado: o.creado || hoy, editado: hoy, revisar: true, fuentes: ['OpenStreetMap / Nominatim', w ? 'Wikipedia (' + w.lang + ')' : '', fotosSel.length ? 'Wikimedia Commons' : '', R.serv ? 'OpenStreetMap / Overpass' : '', R.clima ? 'Open-Meteo' : ''].filter(Boolean)};
  const perroTxt = PERRO[o.perro] || PERRO.sin_dato;
  if (pdi) {
    o.poi = {name: nombre, cat: t.cat, prio: o.prio, dog: perroTxt, icon: '', color: t.color, time: o.dias ? (String(o.dias).replace('.', ',') + (o.dias === 1 ? ' día' : ' días')) : 'parada corta',
      lat: +o.lat.toFixed(6), lon: +o.lon.toFixed(6),
      desc: o.texto + (frases.length ? ' ' + corta(frases.slice(0, 2).join(' '), 320) : ''),
      dog_note: o.perroNota || (o.perro === 'sin_dato' ? 'Sin dato: confirmar con el lugar antes de ir.' : ''),
      visit: {why: o.texto, see: w ? corta(w.extracto, 600) : 'Por completar: sin artículo de Wikipedia cerca; describir tras la visita o en la revisión.',
        access: (loc ? `Cerca de ${loc}. ` : '') + (serv || 'Accesos y servicios por confirmar.'), when: cli || 'Época por confirmar.',
        skip: `Punto creado con el creador de puntos el ${propio.creado}: pendiente de revisar acceso, seguridad y normas antes de darlo por bueno.`},
      links, photos: fotosSel, credit: fotosSel[0] ? fotosSel[0].credit : '', source: fotosSel[0] ? fotosSel[0].source : '', img: fotosSel[0] ? fotosSel[0].img : '', propio};
    o.detalle = {...o.poi, type: 'poi', ficha: null, time: o.poi.time, dogcls: PERRO_CLS[o.perro] || 'st-grey'};
  } else {
    const cerca = R.serv && t.osm && R.serv[t.osm] && R.serv[t.osm][0] && R.serv[t.osm][0].d < 0.6 ? R.serv[t.osm][0] : null;
    const nom2 = o.nombre || (cerca && cerca.nombre ? (t.pref ? t.pref + ' · ' : '') + cerca.nombre : nombre);
    o.poi = {name: nom2, cat: t.cat, lat: +o.lat.toFixed(6), lon: +o.lon.toFixed(6),
      info: [t.pref, o.texto, loc ? 'cerca de ' + loc : '', o.perro !== 'sin_dato' ? 'perro: ' + perroTxt : '', 'creado con el creador de puntos, por revisar'].filter(Boolean).join(' · '),
      source: `https://www.openstreetmap.org/?mlat=${o.lat}&mlon=${o.lon}#map=17/${o.lat}/${o.lon}`, propio};
    o.detalle = {type: 'poi', name: nom2, cat: t.l, prio: '', time: '', lat: o.lat, lon: o.lon, desc: o.poi.info, photos: [], dog: perroTxt, dogcls: PERRO_CLS[o.perro] || 'st-grey',
      visit: {access: serv, when: cli}, links, ficha: null};
  }
}
function paso2(){
  const o = ESTADO, R = o.auto || {}, pdi = tipo(o.tipo).clase === 'pdi';
  const fotosHTML = pdi ? ((R.fotos || []).length ? `<div class="a27c-fotos">${R.fotos.slice(0, 12).map(f => `<label class="${(o.elegidas || []).includes(f.source) ? 'on' : ''}" title="${esc(f.caption + ' · ' + f.credit)}"><input type="checkbox" data-foto="${esc(f.source)}" ${(o.elegidas || []).includes(f.source) ? 'checked' : ''}><img src="${esc(f.thumb)}" alt="${esc(f.caption)}" loading="lazy"><span>${esc(f.credit)}</span></label>`).join('')}</div>
    <p class="a27c-nota">Marca las fotos que quieras (la primera marcada será la portada). Las fotos de Commons se muestran con su autor y licencia.</p>` : '<p class="a27c-aviso">No hay fotos en Wikimedia Commons cerca de este punto. Puedes publicarlo igual; en la revisión se buscará una.</p>') : '';
  const cand = (R.wiki && R.wiki.candidatos) || [];
  const wsel = pdi && cand.length ? `<label>Información de Wikipedia <small style="font-weight:400">(si no es lo que buscas, elige otro artículo o vuelve atrás y escribe el nombre)</small>
      <select id="a27c-wiki"><option value="">Ninguno: solo mi texto</option>${cand.map((c, i) => `<option value="${i}" ${R.wiki && !R.wiki.vacio && c.lang === R.wiki.lang && c.titulo === R.wiki.titulo ? 'selected' : ''}>${esc(c.titulo)} · ${c.lang} · ${km(c.dist / 1000)}${c.por === 'nombre' ? ' · por el nombre' : ''}</option>`).join('')}</select></label>` : '';
  const pub = o.publicado ? `<p class="a27c-nota">Publicado en la web el ${esc(o.publicado.fecha)} (${esc(o.publicado.slug)}).</p>` : '';
  DLG.innerHTML = `<div class="a27c-h"><h2 id="a27c-t">${esc(o.poi.name)}</h2><button type="button" class="a27c-x" data-c="cerrar" aria-label="Cerrar">×</button></div>
  <div class="a27c-b">
    ${wsel}
    ${fotosHTML}
    <div class="a27c-prev map-poi-sheet">${typeof a27PoiDetail === 'function' ? a27PoiDetail(o.detalle, CB.raiz || '../') : ''}</div>
    <p class="a27c-nota">Fuentes: ${esc(o.poi.propio.fuentes.join(', '))}. Queda marcado «por revisar»: pídeme «revisa los puntos nuevos» y compruebo acceso, fotos, seguridad y perro.</p>
    ${pub}
    <div class="a27c-btns">
      <button type="button" class="a27c-btn" data-c="volver">← Cambiar datos</button>
      <button type="button" class="a27c-btn pri" data-c="guardar">Guardar${CB.enViaje ? ' y usarlo' : ''}</button>
      <button type="button" class="a27c-btn pub" data-c="publicar">${o.publicado ? 'Publicar de nuevo' : 'Publicar en la web'}</button>
      ${o.editar ? '<button type="button" class="a27c-btn x" data-c="borrar">Borrar</button>' : ''}
    </div>
    <p class="a27c-nota" id="a27c-msg"></p>
  </div>`;
  const prev = DLG.querySelector('.a27c-prev');
  if (prev) { const x = prev.querySelector('.map-poi-close'); if (x) x.remove(); prev.querySelectorAll('.map-poi-actions a').forEach(a => { a.target = '_blank'; a.rel = 'noopener'; }); }
  prev && prev.querySelectorAll('[data-map-move]').forEach(b => b.addEventListener('click', e => { e.preventDefault(); if (typeof a27GalleryMove === 'function') a27GalleryMove(b.closest('.map-poi-gallery'), Number(b.dataset.mapMove)); }));
}
function registro(){
  const o = ESTADO;
  return {id: o.id, tipo: o.tipo, clase: tipo(o.tipo).clase, pais: o.pais, lat: o.lat, lon: o.lon, nombre: o.nombre, texto: o.texto, prio: o.prio, dias: o.dias,
    perro: o.perro, perroNota: o.perroNota, elegidas: o.elegidas, auto: o.auto ? {lugar: o.auto.lugar, wiki: o.auto.wiki, fotos: (o.auto.fotos || []).slice(0, 12), serv: o.auto.serv, radioServ: o.auto.radioServ, clima: o.auto.clima} : null,
    poi: o.poi, detalle: o.detalle, creado: o.poi.propio.creado, publicado: o.publicado || null};
}
function msg(t){ const m = document.getElementById('a27c-msg'); if (m) m.innerHTML = t; }
const b64 = s => { const by = new TextEncoder().encode(s); let bin = ''; for (let i = 0; i < by.length; i += 8192) bin += String.fromCharCode.apply(null, by.subarray(i, i + 8192)); return btoa(bin); };
const deb64 = s => { const bin = atob(s.replace(/\n/g, '')), by = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) by[i] = bin.charCodeAt(i); return new TextDecoder().decode(by); };
async function publicar(){
  const o = ESTADO;
  if (!o.pais) { msg('No se ha podido saber de qué país es el punto: muévelo dentro de un país.'); return; }
  let tk = ''; try { tk = localStorage.getItem('a27_gh_pat') || ''; } catch(e) {}
  if (!tk) { msg(`Para publicar hace falta poner una vez el token de GitHub en el <a href="${CB.raiz || '../'}admin/" target="_blank" rel="noopener">panel de edición</a> (en este mismo navegador). Mientras tanto, «Guardar» lo deja en este navegador.`); return; }
  const H = {'Authorization': 'Bearer ' + tk, 'Accept': 'application/vnd.github+json'};
  const pdi = tipo(o.tipo).clase === 'pdi', ruta = pdi ? `content/pois/${o.pais}.json` : `content/ficha/${o.pais}.json`;
  msg('Publicando…');
  try {
    const r = await fetch(`${API}/contents/${ruta}?ref=${BRANCH}`, {headers: H, cache: 'no-store'});
    if (!r.ok) throw new Error('GitHub respondió ' + r.status + (r.status === 401 ? ' (token caducado o sin permiso)' : ''));
    const j = await r.json(), datos = JSON.parse(deb64(j.content));
    let n = null;
    if (pdi) {
      const i = o.publicado && o.publicado.n ? datos.findIndex(x => x.n === o.publicado.n && x.propio) : -1;
      n = i >= 0 ? o.publicado.n : Math.max(0, ...datos.map(x => +x.n || 0)) + 1;
      const poi = {n, ...o.poi};
      if (i >= 0) datos[i] = poi; else datos.push(poi);
    } else {
      datos.logistics = (datos.logistics || []).filter(x => !(x.propio && o.publicado && x.name === o.publicado.nombre));
      datos.logistics.push(o.poi);
    }
    const put = await fetch(`${API}/contents/${ruta}`, {method: 'PUT', headers: {...H, 'Content-Type': 'application/json'},
      body: JSON.stringify({message: `Punto nuevo desde el creador: ${o.poi.name} (${o.paisNombre || o.pais})`, content: b64(JSON.stringify(datos, null, 2) + '\n'), sha: j.sha, branch: BRANCH})});
    if (!put.ok) throw new Error('GitHub respondió ' + put.status + ' al guardar');
    o.publicado = {fecha: new Date().toISOString().slice(0, 10), slug: o.pais, n, nombre: o.poi.name};
    guardar(registro());
    msg(`Publicado. GitHub reconstruye la web en 2–3 minutos; después aparece en la ficha de ${esc(o.paisNombre || o.pais)}, en los mapas y aquí como punto normal.`);
    CB.cambio && CB.cambio(registro());
  } catch(e) { msg('No se ha podido publicar: ' + esc(e.message) + '. El punto sigue guardado en este navegador si le diste a «Guardar».'); }
}
function onClick(e){
  const b = e.target.closest('[data-c]'); if (b) {
    const c = b.dataset.c;
    if (c === 'cerrar') DLG.close();
    else if (c === 'completar') completar();
    else if (c === 'volver') { paso1(); }
    else if (c === 'guardar') { guardar(registro()); DLG.close(); CB.cambio && CB.cambio(registro(), true); }
    else if (c === 'publicar') { guardar(registro()); publicar(); }
    else if (c === 'borrar') { if (confirm('¿Borrar este punto de este navegador?' + (ESTADO.publicado ? ' (En la web seguirá hasta que lo quites en el panel de edición.)' : ''))) { borrar(ESTADO.id); DLG.close(); CB.cambio && CB.cambio(null); } }
    return;
  }
}
function onChange(e){
  if (e.target.dataset.foto != null) {
    const s = e.target.dataset.foto, o = ESTADO; o.elegidas = (o.elegidas || []).filter(x => x !== s); if (e.target.checked) o.elegidas.push(s);
    // mantener el orden de la lista (la primera marcada = portada)
    o.elegidas = (o.auto.fotos || []).map(f => f.source).filter(x => o.elegidas.includes(x));
    armar(); paso2();
  }
  if (e.target.id === 'a27c-tipo') { leerForm(); paso1(); }
  if (e.target.id === 'a27c-coords') ponerCoords();
  if (e.target.id === 'a27c-wiki') {
    const o = ESTADO, R = o.auto || {}, cand = (R.wiki && R.wiki.candidatos) || [], v = e.target.value;
    if (v === '') { R.wiki = {candidatos: cand, vacio: true}; armar(); paso2(); return; }
    e.target.disabled = true;
    resumenWiki(cand[+v]).then(r => { R.wiki = r ? {...r, candidatos: cand, elegido: true} : {candidatos: cand, vacio: true}; armar(); paso2(); });
  }
}
// API pública
window.A27Creador = {
  TIPOS, lista, borrar,
  abrir(lat, lon, opts){
    CB = opts || {};
    const d = dialogo();
    if (!d.__on) { d.addEventListener('click', onClick); d.addEventListener('change', onChange); d.__on = true; }
    const ex = CB.id ? lista().find(x => x.id === CB.id) : null;
    ESTADO = ex ? {...ex, editar: true, paisNombre: CB.paisNombre || ex.pais} : {id: 'p' + Date.now().toString(36), tipo: CB.tipo || 'naturaleza', lat, lon, pais: CB.pais || '', paisNombre: CB.paisNombre || '', nombre: CB.nombre || ''};
    if (ex && ex.poi) paso2(); else paso1();
    if (!d.open) d.showModal();
  },
};
})();

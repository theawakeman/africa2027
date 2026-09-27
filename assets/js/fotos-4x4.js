// Fotos de los puntos y rutas 4x4 (content/offroad/<pais>.json).
// Botón «Añadir fotos» (atributo data-foto4="pais|ox|n|nombre", ox = punto, rx = ruta) en las fichas y en el Planificador.
// Las fotos se reducen en el navegador (1600 px, JPEG) y se pueden:
//  · guardar solo en este navegador, o
//  · publicar en la web con el mismo token de GitHub que usa el panel de edición (/admin/): la imagen va a
//    assets/img/offroad/<pais>/ y su ficha a content/offroad/<pais>.json; GitHub reconstruye la web en 2-3 minutos.
(function(){
'use strict';
const REPO = 'theawakeman/africa2027', BRANCH = 'main', API = 'https://api.github.com/repos/' + REPO, LKEY = 'a27-fotos-4x4-v1';
const esc = v => String(v == null ? '' : v).replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));
const leer = () => { try { return JSON.parse(localStorage.getItem(LKEY) || '{}') || {}; } catch(e) { return {}; } };
const escribir = o => { try { localStorage.setItem(LKEY, JSON.stringify(o)); return true; } catch(e) { return false; } };
let DLG = null, CUR = null, COLA = [];

function dialogo(){
  if (DLG) return DLG;
  const st = document.createElement('style');
  st.textContent = `#a27f4{max-width:560px;width:calc(100% - 24px);border:1px solid var(--line,#ccc);border-radius:14px;padding:18px;background:var(--surface,#fff);color:var(--ink,#222);font-family:"Archivo",sans-serif}
#a27f4::backdrop{background:rgba(0,0,0,.45)}#a27f4 h3{margin:0 0 4px;font-size:17px}#a27f4 .sub{font-size:12.5px;color:var(--ink-soft,#666);margin:0 0 10px}
#a27f4 label{display:block;font-size:12.5px;color:var(--ink-soft,#666);margin:8px 0 3px}#a27f4 input[type=text],#a27f4 input[type=url]{width:100%;box-sizing:border-box;font:inherit;font-size:14px;padding:7px 9px;border:1px solid var(--line,#ccc);border-radius:8px;background:var(--surface,#fff);color:var(--ink,#222)}
#a27f4 .fila{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:10px}#a27f4 button,#a27f4 .bt{font:inherit;font-size:13.5px;padding:7px 12px;border-radius:8px;border:1px solid var(--line,#bbb);background:var(--surface,#fff);color:var(--ink,#222);cursor:pointer}
#a27f4 .pri{background:#1E7A8A;border-color:#1E7A8A;color:#fff}#a27f4 .x{position:absolute;top:10px;right:12px;border:0;background:none;font-size:22px;padding:0 4px}
#a27f4 .miniaturas{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:8px;margin-top:10px}#a27f4 .miniaturas figure{margin:0;position:relative}
#a27f4 .miniaturas img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:8px;display:block}#a27f4 .miniaturas button{position:absolute;top:4px;right:4px;padding:0 6px;font-size:13px;background:rgba(0,0,0,.6);color:#fff;border:0}
#a27f4 .miniaturas figcaption{font-size:11px;color:var(--ink-soft,#666)}#a27f4 .msg{font-size:13px;margin-top:10px;min-height:1em}
.off-locales{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px;font-size:11.5px;color:var(--ink-soft,#666);align-items:center}.off-locales img{width:64px;height:48px;object-fit:cover;border-radius:6px}`;
  document.head.appendChild(st);
  DLG = document.createElement('dialog'); DLG.id = 'a27f4'; document.body.appendChild(DLG);
  DLG.addEventListener('click', onClick); DLG.addEventListener('change', onChange);
  DLG.addEventListener('click', e => { if (e.target === DLG) DLG.close(); });
  return DLG;
}
const clave = c => c.pais + '-' + c.k + c.n;
function pintar(m){
  const c = CUR, loc = leer()[clave(c)] || [];
  DLG.innerHTML = `<button type="button" class="x" data-f="cerrar" aria-label="Cerrar">×</button>
    <h3>Fotos · ${esc(c.nombre)}</h3><p class="sub">${c.k === 'rx' ? 'Ruta 4x4' : 'Punto 4x4'} · se reducen a 1.600 px antes de guardarlas.</p>
    <div class="fila"><label class="bt pri" style="margin:0;color:#fff">Elegir fotos del ordenador o del móvil<input type="file" accept="image/*" multiple hidden data-f="archivos"></label></div>
    <label for="a27f4-url">…o pega el enlace de una foto (Wikimedia Commons, tu nube…)</label>
    <div class="fila" style="margin-top:0"><input type="url" id="a27f4-url" placeholder="https://…" style="flex:1"><button type="button" data-f="url">Añadir</button></div>
    <label for="a27f4-pie">Pie de foto</label><input type="text" id="a27f4-pie" value="${esc(c.pie || c.nombre)}">
    <label for="a27f4-autor">Autor y licencia</label><input type="text" id="a27f4-autor" value="${esc(c.autor || 'David · África 2027')}">
    ${(c.pub || []).length ? `<label>Ya publicadas (toca × para quitar las que no sean del sitio)</label><div class="miniaturas">${c.pub.map((f, i) => `<figure style="${c.quitar.has(f.img) ? 'opacity:.3' : ''}"><img src="${esc(/^https?:/.test(f.img) ? f.img : (c.raiz || '../../') + f.img)}" alt=""><button type="button" data-f="quitarpub" data-i="${i}" aria-label="Quitar">${c.quitar.has(f.img) ? '↺' : '×'}</button><figcaption>${c.quitar.has(f.img) ? 'se quitará' : f.auto ? 'de la zona' + (f.km != null ? ' · ' + f.km + ' km' : '') : 'publicada'}</figcaption></figure>`).join('')}</div>` : ''}
    <div class="miniaturas">${COLA.map((f, i) => `<figure><img src="${esc(f.ver)}" alt=""><button type="button" data-f="quitar" data-i="${i}" aria-label="Quitar">×</button><figcaption>nueva</figcaption></figure>`).join('')}
      ${loc.map((f, i) => `<figure><img src="${esc(f.img)}" alt=""><button type="button" data-f="quitarloc" data-i="${i}" aria-label="Quitar">×</button><figcaption>en este navegador</figcaption></figure>`).join('')}</div>
    <div class="fila"><button type="button" class="pri" data-f="publicar">Publicar en la web</button><button type="button" data-f="guardar">Guardar solo en este navegador</button></div>
    <div class="msg" id="a27f4-msg">${m || ''}</div>`;
}
function msg(t){ const m = document.getElementById('a27f4-msg'); if (m) m.innerHTML = t; }
function leerCampos(){ const p = document.getElementById('a27f4-pie'), a = document.getElementById('a27f4-autor'); if (p) CUR.pie = p.value.trim(); if (a) CUR.autor = a.value.trim(); }
// Reduce la imagen a 1600 px de lado y la pasa a JPEG (dataURL)
function reducir(file){
  return new Promise((ok, ko) => {
    const u = URL.createObjectURL(file), im = new Image();
    im.onload = () => { const k = Math.min(1, 1600 / Math.max(im.naturalWidth, im.naturalHeight)), cv = document.createElement('canvas');
      cv.width = Math.round(im.naturalWidth * k); cv.height = Math.round(im.naturalHeight * k);
      cv.getContext('2d').drawImage(im, 0, 0, cv.width, cv.height); URL.revokeObjectURL(u); ok(cv.toDataURL('image/jpeg', .82)); };
    im.onerror = () => { URL.revokeObjectURL(u); ko(new Error('formato de imagen no admitido por este navegador')); };
    im.src = u;
  });
}
async function onChange(e){
  if (e.target.dataset.f !== 'archivos') return;
  leerCampos();
  for (const f of [...e.target.files]) { try { const d = await reducir(f); COLA.push({tipo: 'archivo', ver: d, datos: d, nombre: f.name}); } catch(err) { msg(esc(f.name) + ': ' + esc(err.message)); } }
  pintar();
}
function commons(u){
  // https://commons.wikimedia.org/wiki/File:X.jpg → imagen servible + página de la fuente
  const m = u.match(/commons\.wikimedia\.org\/wiki\/(File:[^?#]+)/);
  return m ? {img: 'https://commons.wikimedia.org/wiki/Special:FilePath/' + m[1].slice(5) + '?width=1200', source: u} : {img: u, source: u};
}
async function publicar(){
  let tk = ''; try { tk = localStorage.getItem('a27_gh_pat') || ''; } catch(e) {}
  const raiz = CUR.raiz || '../../';
  if (!tk) { msg(`Para publicar hace falta poner una vez el token de GitHub en el <a href="${raiz}admin/" target="_blank" rel="noopener">panel de edición</a>, en este mismo navegador. Mientras tanto usa «Guardar solo en este navegador».`); return; }
  const loc = leer(), k = clave(CUR), todas = COLA.concat((loc[k] || []).map(f => f.url ? {tipo: 'url', ...f} : {tipo: 'archivo', ver: f.img, datos: f.img, pie: f.caption, autor: f.credit}));
  if (!todas.length && !CUR.quitar.size) { msg('Añade antes alguna foto o marca alguna para quitar.'); return; }
  const H = {'Authorization': 'Bearer ' + tk, 'Accept': 'application/vnd.github+json'};
  try {
    const nuevas = [];
    for (let i = 0; i < todas.length; i++) {
      const f = todas[i];
      if (f.tipo === 'url') { nuevas.push({img: f.img, source: f.source || f.img, credit: f.credit || CUR.autor || '', caption: f.caption || CUR.pie || ''}); continue; }
      msg(`Subiendo la foto ${i + 1} de ${todas.length}…`);
      const ruta = `assets/img/offroad/${CUR.pais}/${CUR.k}${CUR.n}-${Date.now().toString(36)}-${i + 1}.jpg`;
      const put = await fetch(`${API}/contents/${ruta}`, {method: 'PUT', headers: {...H, 'Content-Type': 'application/json'},
        body: JSON.stringify({message: `Foto 4x4: ${CUR.nombre}`, content: f.datos.split(',')[1], branch: BRANCH})});
      if (!put.ok) throw new Error('GitHub respondió ' + put.status + (put.status === 401 ? ' (token caducado o sin permiso)' : '') + ' al subir la foto');
      nuevas.push({img: ruta, source: '', credit: f.autor || CUR.autor || '', caption: f.pie || CUR.pie || ''});
    }
    msg('Guardando la ficha…');
    const fich = `content/offroad/${CUR.pais}.json`;
    const r = await fetch(`${API}/contents/${fich}?ref=${BRANCH}`, {headers: H, cache: 'no-store'});
    if (!r.ok) throw new Error('GitHub respondió ' + r.status + ' al leer la ficha');
    const j = await r.json(), bin = atob(j.content.replace(/\n/g, '')), by = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) by[i] = bin.charCodeAt(i);
    const datos = JSON.parse(new TextDecoder().decode(by)), lista = CUR.k === 'rx' ? datos.rutas : datos.puntos, x = lista.find(y => +y.n === +CUR.n);
    if (!x) throw new Error('no encuentro ese punto en la ficha publicada');
    x.photos = (x.photos || []).filter(f => !CUR.quitar.has(f.img)).concat(nuevas);
    const txt = JSON.stringify(datos, null, 1) + '\n', eb = new TextEncoder().encode(txt); let s = '';
    for (let i = 0; i < eb.length; i += 8192) s += String.fromCharCode.apply(null, eb.subarray(i, i + 8192));
    const put = await fetch(`${API}/contents/${fich}`, {method: 'PUT', headers: {...H, 'Content-Type': 'application/json'},
      body: JSON.stringify({message: `Fotos 4x4: ${CUR.nombre} (+${nuevas.length}${CUR.quitar.size ? ', −' + CUR.quitar.size : ''})`, content: btoa(s), sha: j.sha, branch: BRANCH})});
    if (!put.ok) throw new Error('GitHub respondió ' + put.status + ' al guardar la ficha');
    COLA = []; delete loc[k]; escribir(loc); CUR.pub = x.photos; CUR.quitar = new Set();
    pintar(`Hecho: ${nuevas.length} foto${nuevas.length !== 1 ? 's' : ''} nueva${nuevas.length !== 1 ? 's' : ''}. GitHub reconstruye la web en 2–3 minutos; después salen en la ficha, en los mapas y en el Planificador. Acuérdate de hacer <b>git pull</b> en el Mac antes del próximo push.`);
    locales();
  } catch(err) { msg('No se ha podido publicar: ' + esc(err.message) + '. Las fotos siguen aquí; puedes guardarlas en este navegador.'); }
}
function onClick(e){
  const b = e.target.closest('[data-f]'); if (!b) return;
  const f = b.dataset.f;
  if (f === 'cerrar') { DLG.close(); return; }
  leerCampos();
  if (f === 'quitar') { COLA.splice(+b.dataset.i, 1); pintar(); }
  else if (f === 'quitarpub') { const img = CUR.pub[+b.dataset.i].img; if (CUR.quitar.has(img)) CUR.quitar.delete(img); else CUR.quitar.add(img); pintar(CUR.quitar.size ? 'Pulsa «Publicar en la web» para quitarlas.' : ''); }
  else if (f === 'quitarloc') { const loc = leer(), k = clave(CUR); (loc[k] || []).splice(+b.dataset.i, 1); if (loc[k] && !loc[k].length) delete loc[k]; escribir(loc); pintar(); locales(); }
  else if (f === 'url') { const v = (document.getElementById('a27f4-url').value || '').trim();
    if (!/^https?:\/\//.test(v)) { msg('Pega un enlace que empiece por https://'); return; }
    const c = commons(v); COLA.push({tipo: 'url', ver: c.img, img: c.img, source: c.source, credit: CUR.autor, caption: CUR.pie}); pintar(); }
  else if (f === 'guardar') {
    if (!COLA.length) { msg('No hay fotos nuevas.'); return; }
    const loc = leer(), k = clave(CUR);
    loc[k] = (loc[k] || []).concat(COLA.map(x => x.tipo === 'url' ? {url: true, img: x.img, source: x.source, credit: x.credit || CUR.autor, caption: x.caption || CUR.pie} : {img: x.datos, credit: CUR.autor, caption: CUR.pie}));
    if (!escribir(loc)) { msg('No cabe en el navegador: publica las fotos o quita alguna.'); return; }
    COLA = []; pintar('Guardadas en este navegador. Para que las vea todo el mundo, «Publicar en la web».'); locales();
  }
  else if (f === 'publicar') publicar();
}
// Miniaturas de las fotos que solo están en este navegador, debajo de su tarjeta
function locales(){
  const loc = leer();
  document.querySelectorAll('[data-foto4]').forEach(b => {
    const [pais, k, n] = b.dataset.foto4.split('|'), fs = loc[pais + '-' + k + n] || [];
    let cont = b.parentNode.querySelector(':scope > .off-locales');
    if (!fs.length) { if (cont) cont.remove(); return; }
    if (!cont) { cont = document.createElement('div'); cont.className = 'off-locales'; b.insertAdjacentElement('afterend', cont); }
    cont.innerHTML = fs.map(f => `<img src="${esc(f.img)}" alt="">`).join('') + '<span>en este navegador, sin publicar</span>';
  });
}
function abrir(o){
  CUR = {...o, pub: [], quitar: new Set()}; COLA = []; dialogo(); pintar();
  if (!DLG.open) DLG.showModal();
  // Fotos ya publicadas de ese punto o ruta (para poder quitar las que no sean del sitio)
  const c = CUR;
  fetch((c.raiz || '../../') + 'content/offroad/' + c.pais + '.json', {cache: 'no-store'}).then(r => r.ok ? r.json() : null).then(d => {
    if (!d || CUR !== c) return; const x = (c.k === 'rx' ? d.rutas : d.puntos).find(y => +y.n === +c.n);
    c.pub = (x && x.photos) || []; if (c.pub.length) pintar();
  }).catch(() => {});
}
document.addEventListener('click', e => {
  const b = e.target.closest('[data-foto4]'); if (!b || b.closest('#a27f4')) return;
  e.preventDefault(); e.stopPropagation();
  const [pais, k, n, ...nm] = b.dataset.foto4.split('|');
  abrir({pais, k, n: +n, nombre: nm.join('|'), raiz: b.dataset.raiz || '../../'});
}, true);
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', locales); else locales();
window.A27Fotos4x4 = {abrir, locales: k => leer()[k] || []};
})();

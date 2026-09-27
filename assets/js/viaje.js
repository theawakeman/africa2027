/* Tu viaje · aplica a las fichas y al portal el viaje calculado en el Planificador.
   El Planificador guarda un resumen de la ruta en este navegador ('a27-ruta-resumen');
   aquí solo se lee. Sin resumen, las páginas se quedan con su texto neutro. */
(function(){
  let V = null;
  try { V = JSON.parse(localStorage.getItem('a27-ruta-resumen') || 'null'); } catch(e) { V = null; }
  if (V && (!V.pasos || !V.pasos.length)) V = V.pasos ? V : null;
  const MES = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
  const d = iso => { const x = new Date(iso + 'T00:00:00Z'); return isNaN(x) ? null : x; };
  const f = (iso, año) => { const x = d(iso); return x ? x.getUTCDate() + ' ' + MES[x.getUTCMonth()] + (año ? ' ' + x.getUTCFullYear() : '') : ''; };
  const rango = (a, b) => { const x = d(a), y = d(b); if (!x || !y) return ''; return f(a, x.getUTCFullYear() !== y.getUTCFullYear()) + ' → ' + f(b, true); };
  const n = v => String(Math.round(v)).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
  const esc = s => String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  const root = (() => { const s = document.querySelector('script[src*="assets/js/viaje.js"]'); return s ? s.getAttribute('src').split('assets/js/viaje.js')[0] : ''; })();
  const pres = root + 'planificador/';
  const set = (el, txt) => { if (!el) return; const b = el.querySelector('b'); if (b) b.textContent = txt; el.title = txt; };
  const dias = x => { const v = Math.max(1, Math.round(x)); return v + (v === 1 ? ' día' : ' días'); };
  const tipoTxt = p => p.tipo === 'visita' ? 'se recorre' : 'solo se cruza';
  const total = V ? V.pasos.length : 0;

  // ---- Acceso para otras piezas (mapas de visados, CPD y perro): ¿está el país en el viaje?
  const ENV = V ? new Set(V.pasos.map(p => p.f)) : null;
  window.A27Viaje = {V, en: slug => ENV ? ENV.has(slug) : null,
    pasos: slug => V ? V.pasos.filter(p => p.f === slug) : [],
    fechas: slug => V ? V.pasos.filter(p => p.f === slug).map(p => rango(p.ent, p.sal)).join(' · ') : ''};

  // ---- Páginas temáticas (visados, CPD, perro): los países del viaje, en orden y con fechas.
  // La página define window.A27_TEMA = {tema, data: {slug: {n, lab, color, lvl, corto}}, niveles: [[lvl, lab, color]]}.
  const tema = document.querySelector('[data-viaje-tema]'), T = window.A27_TEMA;
  if (tema && T) {
    const menos = (iso, n) => { const x = d(iso); if (!x) return ''; x.setUTCDate(x.getUTCDate() - n); return f(x.toISOString().slice(0, 10), true); };
    if (!V) {
      tema.innerHTML = '<div class="callout"><div class="callout-title">Tu viaje</div><p>Todavía no hay un viaje calculado en este navegador, así que abajo están <strong>todos los países</strong>. '
        + 'Monta tu viaje en el <a href="' + pres + '">Planificador</a> y aquí verás solo los tuyos, en el orden en que los cruzas y con sus fechas.</p></div>';
    } else {
      const orden = [], ya = {};
      V.pasos.forEach(p => { if (!ya[p.f]) { ya[p.f] = []; orden.push(p.f); } ya[p.f].push(p); });
      const cuenta = {};
      orden.forEach(s => { const x = T.data[s]; const k = x ? x.lvl : '_'; cuenta[k] = (cuenta[k] || 0) + 1; });
      const resumen = (T.niveles || []).filter(([k]) => cuenta[k]).map(([k, lab, col]) => '<span class="tv-pill" style="background:' + col + '">' + cuenta[k] + ' · ' + esc(lab) + '</span>').join(' ')
        + (cuenta._ ? ' <span class="tv-pill" style="background:#8A949A">' + cuenta._ + ' · sin datos</span>' : '');
      const filas = orden.map((s, i) => {
        const x = T.data[s] || {}, ps = ya[s], n = ps.length;
        const fe = ps.map(p => rango(p.ent, p.sal) + (p.tipo === 'visita' ? '' : ' <small>(de paso)</small>')).join('<br>');
        let nota = x.corto ? esc(x.corto) : '';
        if (T.tema === 'visados' && (x.lvl === 'electronico' || x.lvl === 'presencial')) {
          nota = '<strong>Pedirlo antes del ' + menos(ps[0].ent, x.lvl === 'presencial' ? 60 : 30) + '.</strong> ' + nota;
          if (n > 1) nota += ' <span class="tv-ojo">Entras ' + n + ' veces: pide entrada múltiple o un visado por entrada, y que su validez llegue hasta el ' + f(ps[n - 1].sal, true) + '.</span>';
        }
        if (T.tema === 'perro' && n > 1) nota += ' <span class="tv-ojo">Entras ' + n + ' veces: cuenta con un permiso y un certificado sanitario nuevos por entrada, salvo confirmación escrita.</span>';
        if (T.tema === 'cpd' && n > 1) nota += ' <span class="tv-ojo">' + n + ' entradas: cada una se sella en el carnet o necesita su propio permiso temporal.</span>';
        const nom = x.href ? '<a href="' + esc(x.href) + '">' + esc(x.n || s) + '</a>' : esc(x.n || s);
        const est = x.lab ? '<span class="tv-pill" style="background:' + esc(x.color) + '">' + esc(x.lab) + '</span>' : '<span class="tv-pill" style="background:#8A949A">sin datos</span>';
        return '<tr><td>' + (i + 1) + '</td><td><strong>' + nom + '</strong></td><td>' + fe + '</td><td>' + n + '</td><td>' + est + '</td><td>' + nota + '</td></tr>';
      }).join('');
      tema.innerHTML = '<div class="callout" style="border-left-color:#B43A3A"><div class="callout-title">Tu viaje · ' + esc(V.nombre) + '</div>'
        + '<p>' + orden.length + ' países, del ' + esc(f(V.salida, true)) + ' al ~' + esc(f(V.regreso, true)) + '. ' + resumen + '</p>'
        + '<p class="figcap">Fechas aproximadas del <a href="' + pres + '">Planificador</a>: si cambias el viaje, esta lista cambia con él. Abajo, la información de todos los países; los de tu viaje llevan la marca «en tu viaje».</p></div>'
        + '<div class="tblwrap"><table class="tv-tabla"><thead><tr><th>#</th><th>País</th><th>Cuándo</th><th>Entradas</th><th>' + esc(T.col || 'Estado') + '</th><th>Qué hacer</th></tr></thead><tbody>' + filas + '</tbody></table></div>';
    }
    tema.hidden = false;
    // Filas de las tablas generales: marca las del viaje
    if (ENV) document.querySelectorAll('tr[data-pais]').forEach(tr => {
      if (!ENV.has(tr.dataset.pais)) return;
      tr.classList.add('en-viaje');
      const c = tr.querySelector('td'); if (c && !c.querySelector('.tv-marca')) c.insertAdjacentHTML('beforeend', '<br><span class="tv-marca" title="' + esc(window.A27Viaje.fechas(tr.dataset.pais)) + '">en tu viaje</span>');
    });
  }

  // ---- Ficha de país
  const fichas = document.querySelector('.chips.country-facts[data-pais]');
  if (fichas) {
    const slug = fichas.dataset.pais;
    const ps = V ? V.pasos.map((p, i) => ({...p, i})).filter(p => p.f === slug) : [];
    const chip = k => fichas.querySelector('[data-viaje="' + k + '"]');
    const caja = document.querySelector('[data-viaje-ruta]');
    if (!V) {
      if (caja) { caja.innerHTML = '<div class="callout-title">Tu viaje</div><p>Todavía no hay un viaje calculado en este navegador. Configúralo en el <a href="' + pres + '">Planificador</a> y esta ficha dirá por dónde entras, por dónde sales y en qué fechas.</p>'; caja.hidden = false; }
    } else if (!ps.length) {
      set(chip('en'), 'No está en «' + V.nombre + '»');
      set(chip('fechas'), '—');
      if (caja) { caja.innerHTML = '<div class="callout-title">Tu viaje · ' + esc(V.nombre) + '</div><p>Este país no está en el viaje. Se puede añadir en el <a href="' + pres + '">Planificador</a>: toca el país en el mapa y elige sus puntos.</p>'; caja.hidden = false; }
    } else {
      const tipos = [...new Set(ps.map(tipoTxt))];
      set(chip('en'), ps.length > 1 ? ps.length + ' pasos · ' + tipos.join(' y ') : 'Paso ' + (ps[0].i + 1) + ' de ' + total + ' · ' + tipoTxt(ps[0]));
      set(chip('fechas'), ps.map(p => rango(p.ent, p.sal)).join(' · ') + (ps.length === 1 ? ' · ~' + n(Math.max(1, ps[0].d)) + ' d' : ''));
      set(chip('fronteras'), ps.map(p => 'De ' + p.de + ' a ' + p.a).join(' · '));
      if (caja) {
        const li = ps.map((p, j) => '<li><strong>' + (ps.length > 1 ? (j + 1) + 'ª vez' : 'Paso ' + (p.i + 1) + ' de ' + total) + '</strong>: entras desde ' + esc(p.de)
          + ' (~' + esc(f(p.ent, true)) + ') y sales hacia ' + esc(p.a) + ' (~' + esc(f(p.sal, true)) + ') · ' + tipoTxt(p)
          + (p.lab ? ' (' + esc(p.lab) + ')' : '') + ' · ~' + dias(p.d) + ' · ~' + n(p.km) + ' km.</li>').join('');
        caja.innerHTML = '<div class="callout-title">Tu viaje · ' + esc(V.nombre) + '</div><ol>' + li + '</ol>'
          + '<p>La línea roja del mapa es tu viaje. Para cambiarlo: <a href="' + pres + '">Planificador</a>.</p>';
        caja.hidden = false;
      }
    }
  }

  // ---- Portal
  const portal = document.querySelector('[data-viaje-portal]');
  if (portal && V) {
    const vistos = [], ya = {};
    V.pasos.forEach((p, i) => { if (!ya[p.f]) { ya[p.f] = {i, tipos: new Set()}; vistos.push(p); } ya[p.f].tipos.add(p.tipo); });
    portal.innerHTML = '<div class="callout" style="border-left-color:#B43A3A"><div class="callout-title">Tu viaje · ' + esc(V.nombre) + '</div>'
      + '<p>' + esc(rango(V.salida, V.regreso)) + ' · ' + n(V.dias) + ' días · ' + n(V.km) + ' km · ' + vistos.length + ' países. Ferry de ida ' + esc(V.ida) + '; de vuelta ' + esc(V.vuelta)
      + '. <a href="' + pres + '">Cambiarlo en el Planificador</a>.</p></div>';
    portal.hidden = false;
    // Tarjetas: las del viaje arriba y en su orden; las demás, a su región por orden alfabético.
    const cards = {}; document.querySelectorAll('a.card[data-pais]').forEach(a => { cards[a.dataset.pais] = a; a.querySelectorAll('.b-orden').forEach(x => x.remove()); });
    const cont = document.querySelector('[data-viaje-cards]');
    if (cont) {
      const tit = document.querySelector('[data-viaje-titulo]'), nota = document.querySelector('[data-viaje-nota]');
      if (tit) tit.textContent = 'En el orden de tu viaje · ' + V.nombre;
      if (nota) nota.innerHTML = 'Salida y llegada de cada país según el viaje calculado en el <a href="' + pres + '">Planificador</a>. «De paso»: solo se cruza.';
      vistos.forEach((p, j) => {
        const a = cards[p.f]; if (!a) return;
        const b = document.createElement('span'), para = ya[p.f].tipos.has('visita');
        b.className = 'badge b-orden ' + (para ? 'b-viaje' : 'b-paso');
        b.textContent = (j + 1) + 'º · ' + f(p.ent, (p.ent || '').slice(0, 4) !== (V.salida || '').slice(0, 4)) + (para ? '' : ' · de paso');
        const h = a.querySelector('h3'); if (h) h.after(b, document.createTextNode(' '));
        cont.appendChild(a);
      });
      const resto = Object.keys(cards).filter(s => !ya[s]).sort((x, y) => cards[x].dataset.nombre.localeCompare(cards[y].dataset.nombre, 'es'));
      resto.forEach(s => { const box = document.querySelector('[data-region-cards="' + cards[s].dataset.region + '"]'); if (box) box.appendChild(cards[s]); });
      document.querySelectorAll('[data-region-box]').forEach(b => { b.hidden = !b.querySelector('a.card'); });
    }
    set(document.querySelector('[data-viaje="salida"]'), f(V.salida, true));
    set(document.querySelector('[data-viaje="regreso"]'), '~' + f(V.regreso, true));
    const sub = document.querySelector('[data-viaje="portal-sub"]');
    if (sub && vistos.length) sub.textContent = (V.origen || V.ida.split(' → ')[0]) + ' → ' + (vistos[0].nf || vistos[0].n) + ' → … → ' + (vistos[vistos.length - 1].nf || vistos[vistos.length - 1].n) + ' → ' + (V.origen || V.vuelta.split(' → ').pop()) + ' · 2 vehículos 4x4 · 3 viajeros · 1 perro';
  }
})();

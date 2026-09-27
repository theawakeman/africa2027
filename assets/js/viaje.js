/* Tu viaje · aplica a las fichas y al portal el viaje calculado en Presupuesto.
   Presupuesto guarda un resumen de la ruta en este navegador ('a27-ruta-resumen');
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
  const pres = root + 'presupuesto/';
  const set = (el, txt) => { if (!el) return; const b = el.querySelector('b'); if (b) b.textContent = txt; el.title = txt; };
  const dias = x => { const v = Math.max(1, Math.round(x)); return v + (v === 1 ? ' día' : ' días'); };
  const tipoTxt = p => p.tipo === 'visita' ? 'se recorre' : 'solo se cruza';
  const total = V ? V.pasos.length : 0;

  // ---- Ficha de país
  const fichas = document.querySelector('.chips.country-facts[data-pais]');
  if (fichas) {
    const slug = fichas.dataset.pais;
    const ps = V ? V.pasos.map((p, i) => ({...p, i})).filter(p => p.f === slug) : [];
    const chip = k => fichas.querySelector('[data-viaje="' + k + '"]');
    const caja = document.querySelector('[data-viaje-ruta]');
    if (!V) {
      if (caja) { caja.innerHTML = '<div class="callout-title">Tu viaje</div><p>Todavía no hay un viaje calculado en este navegador. Configúralo en <a href="' + pres + '">Presupuesto</a> y esta ficha dirá por dónde entras, por dónde sales y en qué fechas.</p>'; caja.hidden = false; }
    } else if (!ps.length) {
      set(chip('en'), 'No está en «' + V.nombre + '»');
      set(chip('fechas'), '—');
      if (caja) { caja.innerHTML = '<div class="callout-title">Tu viaje · ' + esc(V.nombre) + '</div><p>Este país no está en el viaje. Se puede añadir en <a href="' + pres + '">Presupuesto</a> (tocándolo en el mapa o con «Añadir un país»).</p>'; caja.hidden = false; }
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
          + '<p>La línea roja del mapa es tu viaje. Para cambiarlo: <a href="' + pres + '">Presupuesto</a>.</p>';
        caja.hidden = false;
      }
    }
  }

  // ---- Portal
  const portal = document.querySelector('[data-viaje-portal]');
  if (portal && V) {
    const vistos = [], ya = {};
    V.pasos.forEach((p, i) => { if (!ya[p.f]) { ya[p.f] = {i, tipos: new Set()}; vistos.push(p); } ya[p.f].tipos.add(p.tipo); });
    const items = vistos.map(p => '<li><a class="' + (ya[p.f].tipos.has('visita') ? 'para' : 'cruza') + '" href="paises/' + p.f + '/">' + esc(p.nf || p.n.replace(/ \(.*\)$/, '')) + ' <small>' + f(p.ent) + '</small></a></li>').join('');
    portal.innerHTML = '<div class="callout" style="border-left-color:#B43A3A"><div class="callout-title">Tu viaje · ' + esc(V.nombre) + '</div>'
      + '<p>' + esc(rango(V.salida, V.regreso)) + ' · ' + n(V.dias) + ' días · ' + n(V.km) + ' km · ' + vistos.length + ' países. Ferry de ida ' + esc(V.ida) + '; de vuelta ' + esc(V.vuelta)
      + '. Línea continua: se recorre; discontinua: solo se cruza. <a href="' + pres + '">Cambiarlo en Presupuesto</a>.</p><ol class="viaje-lista">' + items + '</ol></div>';
    portal.hidden = false;
    document.querySelectorAll('a.card[data-pais]').forEach(a => {
      const x = ya[a.dataset.pais]; if (!x) return;
      const b = document.createElement('span');
      b.className = 'badge ' + (x.tipos.has('visita') ? 'b-viaje' : 'b-paso');
      b.textContent = (x.tipos.has('visita') ? 'En tu viaje' : 'De paso') + ' · ' + (x.i + 1) + 'º';
      const h = a.querySelector('h3'); if (h) h.after(b, document.createTextNode(' '));
    });
    set(document.querySelector('[data-viaje="salida"]'), f(V.salida, true));
    set(document.querySelector('[data-viaje="regreso"]'), '~' + f(V.regreso, true));
    const sub = document.querySelector('[data-viaje="portal-sub"]');
    if (sub && vistos.length) sub.textContent = (V.origen || V.ida.split(' → ')[0]) + ' → ' + (vistos[0].nf || vistos[0].n) + ' → … → ' + (vistos[vistos.length - 1].nf || vistos[vistos.length - 1].n) + ' → ' + (V.origen || V.vuelta.split(' → ').pop()) + ' · 2 vehículos 4x4 · 3 viajeros · 1 perro';
  }
})();

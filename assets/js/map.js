
function a27Color(t){
  const m = {verde:'#2E7D32', turquesa:'#1E7A8A', marron:'#8B5A2B', naranja:'#D97B29',
             morado:'#673AB7', azul:'#2B6CB0', gris:'#666666', ambar:'#C47F17'};
  return m[t] || '#C47F17';
}
function a27CatStyle(p){
  if (p.type === 'hospital')  return {color:'#B43A3A', label:'Hospitales'};
  if (p.type === 'consular')  return {color:'#673AB7', label:'Consulados'};
  if (p.type === 'frontera')  return {color:'#5F6B72', label:'Fronteras'};
  if (p.type === 'agua')      return {color:'#1E88C7', label:'Agua de servicio'};
  if (p.type === 'combustible') return {color:'#B8560D', label:'Combustible'};
  if (p.type === 'servicio')  return {color:'#2B6CB0', label:'Servicios'};
  return {color:a27Color(p.color), label:'Puntos de interés'};
}
function a27Esc(value){
  const chars = {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'};
  return String(value == null ? '' : value).replace(/[&<>"']/g, c => chars[c]);
}
function a27MapSrc(value, root){
  const src = String(value || '');
  return /^https?:\/\//.test(src) ? src : root + src;
}
function a27MapHref(value, root){
  const href = String(value || '');
  return href.startsWith('#') || /^https?:\/\//.test(href) ? href : root + href;
}
function a27PoiPhotos(p){
  const photos = Array.isArray(p.photos) ? p.photos.filter(photo => photo && photo.img) : [];
  if (photos.length) return photos;
  return p.img ? [{img:p.img, credit:p.credit || '', source:p.source || '', caption:p.name || ''}] : [];
}
function a27DetailGallery(p, root){
  const photos = a27PoiPhotos(p);
  if (!photos.length) return '<div class="map-poi-noimg">Sin fotografía exacta verificada todavía</div>';
  const slides = photos.map((photo, index) => {
    const source = /^https?:\/\//.test(String(photo.source || ''))
      ? ' · <a href="' + a27Esc(photo.source) + '" target="_blank" rel="noopener">fuente</a>' : '';
    const caption = photo.caption || p.name || ('Vista ' + (index + 1));
    return '<figure' + (index ? ' hidden' : '') + '><img src="' + a27Esc(a27MapSrc(photo.img, root)) +
      '" alt="' + a27Esc(caption) + '"><figcaption>' + a27Esc(caption) +
      (photo.credit ? ' · ' + a27Esc(photo.credit) : '') + source + '</figcaption></figure>';
  }).join('');
  const controls = photos.length > 1
    ? '<button class="prev" data-map-move="-1" type="button" aria-label="Fotografía anterior"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button>' +
      '<button class="next" data-map-move="1" type="button" aria-label="Fotografía siguiente"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></button>' +
      '<span class="map-poi-gallery-count" aria-live="polite">1 / ' + photos.length + '</span>' : '';
  return '<div class="map-poi-gallery" data-index="0" tabindex="0">' + slides + controls + '</div>';
}
function a27GalleryMove(gallery, step){
  const slides = gallery.querySelectorAll('figure');
  if (slides.length < 2) return;
  let index = (Number(gallery.dataset.index || 0) + step + slides.length) % slides.length;
  gallery.dataset.index = String(index);
  slides.forEach((slide, i) => { slide.hidden = i !== index; });
  const count = gallery.querySelector('.map-poi-gallery-count');
  if (count) count.textContent = (index + 1) + ' / ' + slides.length;
}
function a27PoiDetail(p, root){
  const labels = {why:'Por qué ir', see:'Qué se ve', access:'Acceso real', when:'Cuándo', skip:'Cuándo descartarlo'};
  const visit = p.visit && typeof p.visit === 'object' ? p.visit : {};
  const decision = Object.keys(labels).filter(key => visit[key]).map(key =>
    '<div><dt>' + labels[key] + '</dt><dd>' + a27Esc(visit[key]) + '</dd></div>').join('');
  const links = (Array.isArray(p.links) ? p.links : []).filter(link => link && /^https?:\/\//.test(String(link.url || '')))
    .map(link => '<a href="' + a27Esc(link.url) + '" target="_blank" rel="noopener">' +
      a27Esc(link.label || 'Información del lugar') + '</a>').join(' · ');
  const ficha = p.ficha ? '<a class="btn ghost" href="' + a27Esc(a27MapHref(p.ficha, root)) + '">Abrir página del país</a>' : '';
  return '<button class="map-poi-close" type="button" aria-label="Cerrar y volver al mapa">×</button>' +
    a27DetailGallery(p, root) + '<div class="map-poi-body"><h2 id="a27-map-poi-title">' + a27Esc(p.name) + '</h2>' +
    '<div class="poi-tags"><span class="prio">' + a27Esc(p.prio || '') + '</span><span class="cat">' +
    a27Esc(p.cat || '') + '</span>' + (p.time ? '<span class="time">' + a27Esc(p.time) + '</span>' : '') + '</div>' +
    (p.dog ? '<div><span class="st ' + a27Esc(p.dogcls || '') + '">perro: ' + a27Esc(p.dog) + '</span></div>' : '') +
    '<p class="map-poi-description">' + a27Esc(p.desc || '') + '</p>' +
    (decision ? '<dl class="poi-decision">' + decision + '</dl>' : '') +
    (p.dog_note ? '<p class="dognote"><strong>Perro:</strong> ' + a27Esc(p.dog_note) + '</p>' : '') +
    (links ? '<div class="poi-links"><strong>Enlaces útiles:</strong> ' + links + '</div>' : '') +
    '<div class="map-poi-actions">' + ficha + '<a class="btn ghost" href="https://www.google.com/maps?q=' +
    encodeURIComponent(p.lat + ',' + p.lon) + '" target="_blank" rel="noopener">Google Maps</a></div></div>';
}
function a27OpenPoi(p, root, map, marker){
  let dialog = document.getElementById('a27-map-poi-dialog');
  if (!dialog) {
    dialog = document.createElement('dialog');
    dialog.id = 'a27-map-poi-dialog';
    dialog.className = 'map-poi-modal';
    dialog.setAttribute('aria-labelledby', 'a27-map-poi-title');
    dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
    document.body.appendChild(dialog);
  }
  const scrollX = window.scrollX;
  const scrollY = window.scrollY;
  dialog.innerHTML = '<article class="map-poi-sheet">' + a27PoiDetail(p, root) + '</article>';
  dialog.querySelector('.map-poi-close').addEventListener('click', () => dialog.close());
  dialog.querySelectorAll('[data-map-move]').forEach(button => button.addEventListener('click', event => {
    event.preventDefault();
    a27GalleryMove(button.closest('.map-poi-gallery'), Number(button.dataset.mapMove));
  }));
  const gallery = dialog.querySelector('.map-poi-gallery');
  if (gallery) {
    gallery.addEventListener('keydown', event => {
      if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
      event.preventDefault();
      a27GalleryMove(gallery, event.key === 'ArrowRight' ? 1 : -1);
    });
    let touchX = null;
    gallery.addEventListener('touchstart', event => { if (event.touches.length === 1) touchX = event.touches[0].clientX; }, {passive:true});
    gallery.addEventListener('touchend', event => {
      if (touchX == null || !event.changedTouches.length) return;
      const dx = event.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 45) a27GalleryMove(gallery, dx < 0 ? 1 : -1);
      touchX = null;
    }, {passive:true});
  }
  dialog.addEventListener('close', () => {
    window.scrollTo(scrollX, scrollY);
    map.invalidateSize({pan:false});
    if (marker && marker._path && marker._path.focus) marker._path.focus();
  }, {once:true});
  map.closePopup();
  dialog.showModal();
}
function a27Popup(p, root){
  let h = '';
  if (p.img) h += '<img src="'+a27Esc(a27MapSrc(p.img, root))+'" alt="'+a27Esc(p.name || '')+'">';
  h += '<strong class="a27-popup-title">'+a27Esc(p.name)+'</strong>';
  if (p.cat) h += '<span class="a27-popup-meta">'+a27Esc((p.prio ? p.prio+' · ' : '')+p.cat)+'</span>';
  if (p.desc) h += '<span class="a27-map-summary">'+a27Esc(p.desc)+'</span>';
  if (p.dog) h += '<span class="st '+a27Esc(p.dogcls)+'">perro: '+a27Esc(p.dog)+'</span>';
  if (p.info) h += '<span>'+a27Esc(p.info)+'</span>';
  h += '<div class="a27-popup-actions">';
  if (p.type === 'poi') h += '<button type="button" class="a27-popup-expand">Ver ficha ampliada</button>';
  else if (p.ficha) h += '<a href="'+a27Esc(a27MapHref(p.ficha, root))+'">Ver en la ficha</a>';
  if (p.source) h += '<a href="'+a27Esc(p.source)+'" target="_blank" rel="noopener">Fuente del punto</a>';
  h += '<a href="https://www.google.com/maps?q='+p.lat+','+p.lon+'" target="_blank" rel="noopener">Google Maps</a></div>';
  return h;
}
function a27StylePopup(popup){
  if (!popup) return;
  const theme = getComputedStyle(document.documentElement);
  const value = name => theme.getPropertyValue(name).trim();
  const wrapper = popup.querySelector('.leaflet-popup-content-wrapper');
  const tip = popup.querySelector('.leaflet-popup-tip');
  if (wrapper) {
    wrapper.style.setProperty('background', value('--surface'), 'important');
    wrapper.style.setProperty('color', value('--ink'), 'important');
    wrapper.style.setProperty('border-color', value('--line'));
  }
  if (tip) tip.style.setProperty('background', value('--surface'), 'important');
}
// Leyenda de capas plegada en un icono: se abre y se cierra con un clic en el icono,
// y también se cierra al tocar el mapa. No se despliega sola al pasar el ratón.
function a27Leyenda(map, groups){
  const lc = L.control.layers(null, groups, {collapsed: true}).addTo(map);
  const cont = lc.getContainer();
  const btn = cont.querySelector('.leaflet-control-layers-toggle');
  L.DomEvent.off(cont, 'mouseenter mouseleave');   // nada de abrirse al pasar por encima
  if (btn) {
    L.DomEvent.off(btn, 'click');                  // el clic propio de Leaflet solo abre; aquí alterna
    btn.setAttribute('title', 'Capas del mapa');
    btn.setAttribute('aria-label', 'Mostrar u ocultar las capas del mapa');
    L.DomEvent.on(btn, 'click', function(e){
      L.DomEvent.stop(e);
      if (cont.classList.contains('leaflet-control-layers-expanded')) lc.collapse(); else lc.expand();
    });
  }
  const lista = cont.querySelector('.leaflet-control-layers-overlays');
  if (lista) {
    const cab = L.DomUtil.create('div', 'a27-leyenda-cab');
    cab.innerHTML = '<span>Capas</span><button type="button" class="a27-leyenda-x" aria-label="Cerrar las capas">&times;</button>';
    lista.parentNode.insertBefore(cab, lista);
    L.DomEvent.on(cab.querySelector('.a27-leyenda-x'), 'click', function(e){ L.DomEvent.stop(e); lc.collapse(); });
  }
  return lc;
}
function a27Map(elId, cfg){
  const el = document.getElementById(elId);
  if (!el || typeof L === 'undefined') return null;
  const map = L.map(elId, {scrollWheelZoom: cfg.wheel !== false}).setView(cfg.center, cfg.zoom);
  L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 17,
    attribution: 'Teselas &copy; <a href="https://www.esri.com/">Esri</a> &middot; Esri, HERE, Garmin, USGS, NGA y colaboradores de <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);
  const groups = {};
  // Capas encendidas al cargar: todas, salvo que cfg.defaultOn diga cuáles.
  const on = cfg.defaultOn ? new Set(cfg.defaultOn) : null;
  function group(label){
    if (!groups[label]) {
      groups[label] = L.layerGroup();
      if (!on || on.has(label)) groups[label].addTo(map);
    }
    return groups[label];
  }
  // Orden fijo de la leyenda (las capas no listadas van después, por orden de aparición).
  (cfg.groupOrder || []).forEach(label => { if (!groups[label]) groups[label] = null; });
  (cfg.lines || []).forEach(li => {
    const pl = L.polyline(li.pts, {color: li.color, weight: li.dash ? 3 : 4, dashArray: li.dash ? '8 8' : null, opacity:.85});
    if (li.title) pl.bindTooltip(li.title, {sticky: true});
    pl.addTo(group(li.label || 'Corredor'));
  });
  (cfg.points || []).forEach(p => {
    const s = a27CatStyle(p);
    const mk = L.circleMarker([p.lat, p.lon], {radius: 8, color:'#fff', weight:2, fillColor:s.color, fillOpacity:.95});
    mk.bindPopup(a27Popup(p, cfg.root), {maxWidth: 320});
    mk.on('popupopen', function(){
      const popup = mk.getPopup() && mk.getPopup().getElement();
      a27StylePopup(popup);
      const button = popup && popup.querySelector('.a27-popup-expand');
      if (button) button.addEventListener('click', () => a27OpenPoi(p, cfg.root, map, mk), {once:true});
    });
    mk.addTo(group(s.label));
  });
  Object.keys(groups).forEach(k => { if (groups[k] === null) delete groups[k]; });
  if (Object.keys(groups).length > 1) a27Leyenda(map, groups);
  const all = (cfg.points || []).map(p => [p.lat, p.lon]);
  (cfg.lines || []).forEach(li => li.pts.forEach(pt => all.push(pt)));
  if (cfg.fit !== false && all.length) map.fitBounds(L.latLngBounds(all), {padding: [34, 34]});
  return map;
}

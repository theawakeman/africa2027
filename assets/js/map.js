
function a27Color(t){
  const m = {verde:'#2E7D32', turquesa:'#1E7A8A', marron:'#8B5A2B', naranja:'#D97B29',
             morado:'#673AB7', azul:'#2B6CB0', gris:'#666666', ambar:'#C47F17'};
  return m[t] || '#C47F17';
}
function a27CatStyle(p){
  if (p.type === 'hospital')  return {color:'#B43A3A', label:'Hospitales'};
  if (p.type === 'consular')  return {color:'#673AB7', label:'Consulados'};
  if (p.type === 'frontera')  return {color:'#5F6B72', label:'Fronteras'};
  if (p.type === 'agua')      return {color:'#1E88C7', label:'Agua potable'};
  if (p.type === 'combustible') return {color:'#B8560D', label:'Combustible'};
  if (p.type === 'servicio')  return {color:'#2B6CB0', label:'Servicios'};
  return {color:a27Color(p.color), label:'Puntos de interés'};
}
function a27Popup(p, root){
  let h = '';
  if (p.img) h += '<img src="'+(p.img.indexOf('http')===0?p.img:root+p.img)+'" alt="" style="width:100%;aspect-ratio:16/9;object-fit:cover">';
  h += '<strong style="font-size:14px">'+p.name+'</strong><br>';
  if (p.cat) h += '<span style="color:#1E7A8A;font-weight:700">'+(p.prio? p.prio+' · ':'')+p.cat+'</span><br>';
  if (p.desc) h += '<span>'+p.desc+'</span><br>';
  if (p.dog) h += '<span class="st '+p.dogcls+'">perro: '+p.dog+'</span><br>';
  if (p.info) h += '<span>'+p.info+'</span><br>';
  h += '<div style="margin-top:6px;display:flex;gap:10px;flex-wrap:wrap">';
  if (p.ficha) h += '<a href="'+(p.ficha.indexOf('#')===0?p.ficha:root+p.ficha)+'">Ver en la ficha</a>';
  h += '<a href="https://www.google.com/maps?q='+p.lat+','+p.lon+'" target="_blank" rel="noopener">Google Maps</a></div>';
  return h;
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
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 17,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
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
    mk.bindPopup(a27Popup(p, cfg.root), {maxWidth: 290});
    mk.addTo(group(s.label));
  });
  Object.keys(groups).forEach(k => { if (groups[k] === null) delete groups[k]; });
  if (Object.keys(groups).length > 1) a27Leyenda(map, groups);
  const all = (cfg.points || []).map(p => [p.lat, p.lon]);
  (cfg.lines || []).forEach(li => li.pts.forEach(pt => all.push(pt)));
  if (cfg.fit !== false && all.length) map.fitBounds(L.latLngBounds(all), {padding: [34, 34]});
  return map;
}

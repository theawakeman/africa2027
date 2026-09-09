
function a27Color(t){
  const m = {verde:'#2E7D32', turquesa:'#1E7A8A', marron:'#8B5A2B', naranja:'#D97B29',
             morado:'#673AB7', azul:'#2B6CB0', gris:'#666666', ambar:'#C47F17'};
  return m[t] || '#C47F17';
}
function a27CatStyle(p){
  if (p.type === 'hospital')  return {color:'#B43A3A', label:'Hospitales'};
  if (p.type === 'consular')  return {color:'#673AB7', label:'Consulados'};
  if (p.type === 'frontera')  return {color:'#5F6B72', label:'Fronteras'};
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
  if (p.ficha) h += '<a href="'+root+p.ficha+'">Ver en la ficha</a>';
  h += '<a href="https://www.google.com/maps?q='+p.lat+','+p.lon+'" target="_blank" rel="noopener">Google Maps</a></div>';
  return h;
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
  function group(label){
    if (!groups[label]) groups[label] = L.layerGroup().addTo(map);
    return groups[label];
  }
  (cfg.lines || []).forEach(li => {
    L.polyline(li.pts, {color: li.color, weight: 4, dashArray: li.dash ? '8 8' : null, opacity:.85})
      .addTo(group(li.label || 'Corredor'));
  });
  (cfg.points || []).forEach(p => {
    const s = a27CatStyle(p);
    const mk = L.circleMarker([p.lat, p.lon], {radius: 8, color:'#fff', weight:2, fillColor:s.color, fillOpacity:.95});
    mk.bindPopup(a27Popup(p, cfg.root), {maxWidth: 290});
    mk.addTo(group(s.label));
  });
  if (Object.keys(groups).length > 1) L.control.layers(null, groups, {collapsed: window.innerWidth < 700}).addTo(map);
  const all = (cfg.points || []).map(p => [p.lat, p.lon]);
  (cfg.lines || []).forEach(li => li.pts.forEach(pt => all.push(pt)));
  if (cfg.fit !== false && all.length) map.fitBounds(L.latLngBounds(all), {padding: [34, 34]});
  return map;
}

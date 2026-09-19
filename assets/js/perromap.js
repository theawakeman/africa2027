/* Mapa del perro: cada país coloreado según lo que cuesta entrar con él —
   trámite simple (verde), permiso o condiciones (ámbar), mal documentado
   (naranja) o no viable (rojo).

   Los colores salen del semáforo de las tablas del capítulo 2 del dosier, así
   que el mapa no puede contradecir a la tabla que tiene debajo.

   La geometría va en assets/js/africa.geo.json, versionada en el repo y
   precargada por el service worker, para que el mapa funcione sin conexión. */
function a27PerroMap(elId, cfg) {
  var el = document.getElementById(elId);
  if (!el) return;

  var map = L.map(elId, { scrollWheelZoom: false, minZoom: 2 }).setView([2.0, 17.0], 3);
  L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}", {
    maxZoom: 10, attribution: "Teselas &copy; Esri &middot; Esri, HERE, Garmin, USGS, NGA y colaboradores de OpenStreetMap"
  }).addTo(map);

  var NEUTRO = "#cfd8dc";

  function estilo(f) {
    var d = cfg.data[f.properties.slug];
    return {
      color: "#ffffff",
      weight: d ? 1.1 : 0.6,
      fillColor: d ? d.color : NEUTRO,
      fillOpacity: d ? (d.ruta ? 0.82 : 0.45) : 0.25,
      dashArray: d && !d.ruta ? "3,3" : null
    };
  }

  function ficha(d) {
    var h = '<strong style="font-size:15px">' + d.n + "</strong><br>";
    h += '<span style="display:inline-block;margin:5px 0 6px;padding:2px 8px;border-radius:999px;'
       + 'font-size:12px;font-weight:700;color:#fff;background:' + d.color + '">' + d.lab + "</span>";
    if (!d.ruta) h += '<br><em style="font-size:12px">No está en la ruta</em>';
    if (d.org) h += "<br><b>Lo emite:</b> " + d.org;
    if (d.cert) h += "<br><b>Certificado:</b> " + d.cert;
    if (d.nota) h += "<br>" + d.nota;
    if (d.href) h += '<br><a href="' + d.href + '">Ver la ficha del país &rarr;</a>';
    return h;
  }

  fetch(cfg.root + "assets/js/africa.geo.json")
    .then(function (r) { return r.json(); })
    .then(function (geo) {
      var capa = L.geoJSON(geo, {
        style: estilo,
        onEachFeature: function (f, lyr) {
          var d = cfg.data[f.properties.slug];
          if (!d) return;
          lyr.bindPopup(ficha(d), { maxWidth: 330 });
          lyr.bindTooltip(d.n + " · " + d.lab, { sticky: true });
          lyr.on("mouseover", function () { lyr.setStyle({ weight: 2.6, fillOpacity: 0.95 }); });
          lyr.on("mouseout", function () { capa.resetStyle(lyr); });
        }
      }).addTo(map);
      var caja = capa.getBounds();
      // Los estados insulares no tienen contorno en el GeoJSON: van como punto,
      // con la misma ficha, para que no desaparezcan del mapa.
      (cfg.puntos || []).forEach(function (d) {
        var m = L.circleMarker([d.lat, d.lon], {
          radius: 7, color: "#ffffff", weight: 2,
          fillColor: d.color, fillOpacity: d.ruta ? 0.95 : 0.6
        }).addTo(map);
        m.bindPopup(ficha(d), { maxWidth: 330 });
        m.bindTooltip(d.n + " · " + d.lab, { sticky: true });
        caja.extend([d.lat, d.lon]);
      });
      map.fitBounds(caja, { padding: [8, 8] });
    })
    .catch(function () {
      el.insertAdjacentHTML("beforeend",
        '<p class="figcap" style="padding:10px">No se han podido cargar los contornos de los países. '
        + "Las tablas del capítulo 2 tienen la misma información.</p>");
    });
}

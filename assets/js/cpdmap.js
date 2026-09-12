/* Mapa del Carnet de Passages en Douane: cada país coloreado según si el CPD
   es obligatorio (rojo), recomendable (naranja) o innecesario (verde).

   La geometría va en assets/js/africa.geo.json, versionada en el repo y
   precargada por el service worker, para que el mapa funcione sin conexión. */
function a27CpdMap(elId, cfg) {
  var el = document.getElementById(elId);
  if (!el) return;

  var map = L.map(elId, { scrollWheelZoom: false, minZoom: 2 }).setView([2.0, 17.0], 3);
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 10, attribution: "&copy; OpenStreetMap"
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
    h += "<br><b>En su lugar:</b> " + d.alt;
    h += "<br><b>Coste:</b> " + d.cost;
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
          lyr.bindPopup(ficha(d));
          lyr.bindTooltip(d.n + " · " + d.lab, { sticky: true });
          lyr.on("mouseover", function () { lyr.setStyle({ weight: 2.6, fillOpacity: 0.95 }); });
          lyr.on("mouseout", function () { capa.resetStyle(lyr); });
        }
      }).addTo(map);
      map.fitBounds(capa.getBounds(), { padding: [8, 8] });
    })
    .catch(function () {
      el.insertAdjacentHTML("beforeend",
        '<p class="figcap" style="padding:10px">No se han podido cargar los contornos de los países. '
        + "Las tablas de debajo tienen la misma información.</p>");
    });
}

/* Mapa de visados para pasaporte ordinario español. La clasificación se
   refiere a entradas turísticas por tierra, salvo los países marcados como
   vuelo. Reutiliza el mismo mapa y el mismo lenguaje visual de la página CPD. */
function a27VisaMap(elId, cfg) {
  var el = document.getElementById(elId);
  if (!el) return;

  var map = L.map(elId, { scrollWheelZoom: false, minZoom: 2 }).setView([2.0, 17.0], 3);
  L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}", {
    maxZoom: 10, attribution: "Teselas &copy; Esri &middot; Esri, HERE, Garmin, USGS, NGA y colaboradores de OpenStreetMap"
  }).addTo(map);

  var NEUTRO = "#cfd8dc";
  var RUTAS = {
    principal: "Ruta principal",
    alternativa: "Alternativa u opcional",
    excluido: "Excluido del itinerario",
    fuera: "Fuera de la ruta",
    vuelo: "Solo en avión"
  };

  function safe(v) {
    return String(v == null ? "" : v).replace(/[&<>"']/g, function (c) {
      return {"&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;"}[c];
    });
  }

  function estilo(f) {
    var d = cfg.data[f.properties.slug];
    var principal = d && d.ruta === "principal";
    return {
      color: "#ffffff",
      weight: d ? 1.1 : 0.6,
      fillColor: d ? d.color : NEUTRO,
      fillOpacity: d ? (principal ? 0.84 : 0.50) : 0.25,
      dashArray: d && !principal ? "3,3" : null
    };
  }

  function enlace(url, texto) {
    return url ? '<a href="' + safe(url) + '" target="_blank" rel="noopener">' + safe(texto) + "</a>" : "";
  }

  function ficha(d) {
    var h = '<strong style="font-size:15px">' + safe(d.n) + "</strong><br>";
    h += '<span style="display:inline-block;margin:5px 0 6px;padding:2px 8px;border-radius:999px;'
       + 'font-size:12px;font-weight:700;color:#fff;background:' + safe(d.color) + '">' + safe(d.lab) + "</span>";
    h += '<br><em style="font-size:12px">' + safe(RUTAS[d.ruta] || d.ruta) + "</em>";
    h += "<br><b>Situación:</b> " + safe(d.resumen);
    h += "<br><b>Qué hacer:</b> " + safe(d.accion);
    if (d.pasos) h += "<br><b>Pasos previstos:</b> " + safe(d.pasos);
    if (d.entradas) h += "<br><b>Entradas:</b> " + safe(d.entradas);
    if (d.coste) h += "<br><b>Coste:</b> " + safe(d.coste);
    if (d.alerta) h += '<br><span style="color:#8b4d08"><b>Atención:</b> ' + safe(d.alerta) + "</span>";
    var links = [enlace(d.oficial, "Portal oficial"), enlace(d.maec, "MAEC")].filter(Boolean);
    if (links.length) h += "<br>" + links.join(" · ");
    if (d.href) h += '<br><a href="' + safe(d.href) + '">Ver la ficha del país &rarr;</a>';
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
          lyr.bindPopup(ficha(d), { maxWidth: 360 });
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
        + "Las tablas de debajo contienen la misma información.</p>");
    });
}

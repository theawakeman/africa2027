const VERSION = 'a27-20260927-1105';
const PRECACHE = {
"./cpd/": "870fa08c27",
"./documentacion/": "e1435c0df8",
"./": "13fd3c25a6",
"./mapa/": "dd251fed19",
"./paises/angola/historia/": "5b2cea41f8",
"./paises/angola/": "36796458ac",
"./paises/argelia/historia/": "cfea475e91",
"./paises/argelia/": "eb0def7b09",
"./paises/benin/historia/": "6caf14f4c8",
"./paises/benin/": "858823ccc9",
"./paises/botsuana/historia/": "2a2a76dcb6",
"./paises/botsuana/": "42c520dad0",
"./paises/burkina-faso/historia/": "40bb4beb32",
"./paises/burkina-faso/": "afcab3aeaa",
"./paises/burundi/historia/": "aef164c69f",
"./paises/burundi/": "f7f4368ee3",
"./paises/cabo-verde/historia/": "2183856eda",
"./paises/cabo-verde/": "dd995f4dc4",
"./paises/camerun/historia/": "e01a25589e",
"./paises/camerun/": "8feb9b63a6",
"./paises/chad/historia/": "878669227c",
"./paises/chad/": "97967022ec",
"./paises/comoras/historia/": "072dc1c48f",
"./paises/comoras/": "b605b523df",
"./paises/congo/historia/": "1dbaca70f7",
"./paises/congo/": "3f38dace19",
"./paises/costa-de-marfil/historia/": "2550ad0358",
"./paises/costa-de-marfil/": "41d421688a",
"./paises/egipto/historia/": "daf8464b83",
"./paises/egipto/": "9534d6406c",
"./paises/eritrea/historia/": "12839fc8d0",
"./paises/eritrea/": "0bef610676",
"./paises/esuatini/historia/": "d4f3f12920",
"./paises/esuatini/": "7d59907259",
"./paises/etiopia/historia/": "b2381c6d46",
"./paises/etiopia/": "e096db6160",
"./paises/gabon/historia/": "da1a38e951",
"./paises/gabon/": "49881bff4a",
"./paises/gambia/historia/": "1884e7a6cc",
"./paises/gambia/": "623b411a71",
"./paises/ghana/historia/": "cd270283c1",
"./paises/ghana/": "30a7658fb6",
"./paises/guinea-bisau/historia/": "af99ef55bd",
"./paises/guinea-bisau/": "423121ad7c",
"./paises/guinea-ecuatorial/historia/": "55152e16a8",
"./paises/guinea-ecuatorial/": "1dc28de37a",
"./paises/guinea/historia/": "468130ed16",
"./paises/guinea/": "51243d2e7a",
"./paises/kenia/historia/": "53b721d325",
"./paises/kenia/": "5930dbd193",
"./paises/lesoto/historia/": "046574f890",
"./paises/lesoto/": "4a1237a085",
"./paises/liberia/historia/": "1a91b8878a",
"./paises/liberia/": "5f481fdeb3",
"./paises/libia/historia/": "89491445a3",
"./paises/libia/": "54690f4376",
"./paises/madagascar/historia/": "3e6426e9ac",
"./paises/madagascar/": "2aa612be67",
"./paises/malaui/historia/": "788231fbfc",
"./paises/malaui/": "495ef016bf",
"./paises/mali/historia/": "453d528d34",
"./paises/mali/": "3f7506b5bb",
"./paises/marruecos/historia/": "dd7e5a8722",
"./paises/marruecos/": "8effcdc830",
"./paises/mauricio/historia/": "91cd1fe096",
"./paises/mauricio/": "60af7519fe",
"./paises/mauritania/historia/": "bcf6ac703c",
"./paises/mauritania/": "c7517ebf7c",
"./paises/mozambique/historia/": "6c75bf9825",
"./paises/mozambique/": "9a41a71af1",
"./paises/namibia/historia/": "73980e0375",
"./paises/namibia/": "803ab55969",
"./paises/niger/historia/": "f04596dce0",
"./paises/niger/": "1c4784103b",
"./paises/nigeria/historia/": "1587076c98",
"./paises/nigeria/": "2555a9646b",
"./paises/rca/historia/": "cf0b08ab82",
"./paises/rca/": "a90bb6e1ca",
"./paises/rd-congo/historia/": "880f05ea3f",
"./paises/rd-congo/": "d578bee190",
"./paises/ruanda/historia/": "2a6268f7e5",
"./paises/ruanda/": "7898e56a7d",
"./paises/sahara-occidental/historia/": "178ab0485b",
"./paises/sahara-occidental/": "bb917bea0e",
"./paises/santo-tome/historia/": "5fe5f3438b",
"./paises/santo-tome/": "882ec53f8e",
"./paises/senegal/historia/": "530b9e8efe",
"./paises/senegal/": "b388c2b332",
"./paises/seychelles/historia/": "1121afd7b4",
"./paises/seychelles/": "0e04233d56",
"./paises/sierra-leona/historia/": "426e224073",
"./paises/sierra-leona/": "0b7ee50bfb",
"./paises/somalia/historia/": "cb86c14aec",
"./paises/somalia/": "4028a7b06b",
"./paises/sudafrica/historia/": "77b773b711",
"./paises/sudafrica/": "6fc8fecba6",
"./paises/sudan-del-sur/historia/": "67d9c72dc9",
"./paises/sudan-del-sur/": "d1f8772da3",
"./paises/sudan/historia/": "c8e5d1765a",
"./paises/sudan/": "4ecf25d9fe",
"./paises/tanzania/historia/": "002f4ccde5",
"./paises/tanzania/": "995ce4005f",
"./paises/togo/historia/": "ea9c2b4a17",
"./paises/togo/": "f7bf218549",
"./paises/tunez/historia/": "3135c4ea7c",
"./paises/tunez/": "9cf68c1957",
"./paises/uganda/historia/": "cba39980a2",
"./paises/uganda/": "b20659920a",
"./paises/yibuti/historia/": "eb8ea25464",
"./paises/yibuti/": "b6edafffa4",
"./paises/zambia/historia/": "843774dcd1",
"./paises/zambia/": "6948d9382a",
"./paises/zimbabue/historia/": "5fa8513bd9",
"./paises/zimbabue/": "1c643eac27",
"./perro/": "7dc51a26b2",
"./planificador-puntos/": "37faef8e85",
"./planificador/": "3b8e95ce88",
"./presupuesto/": "56d2dd1cd3",
"./visados/": "6f3de4f640",
"./assets/css/site.css?v=d7b1605471": "d7b1605471",
"./assets/icons/icon-192.png": "afb2518dd3",
"./assets/icons/icon-512.png": "195ee555af",
"./assets/icons/icon-maskable-512.png": "6c5d07d1cf",
"./assets/js/africa.geo.json": "efd2b0c9b4",
"./assets/js/cpdmap.js?v=cf099e102d": "cf099e102d",
"./assets/js/map.js?v=5bc6730f6d": "5bc6730f6d",
"./assets/js/pdi-detalle.json": "a9fe2e1fc6",
"./assets/js/perromap.js?v=cb72346aa0": "cb72346aa0",
"./assets/js/planificador-puntos.js?v=93de1908d0": "93de1908d0",
"./assets/js/planificador-puntos.json": "cf9abcdf49",
"./assets/js/presupuesto-xlsx.js?v=6cb35d90f7": "6cb35d90f7",
"./assets/js/presupuesto.js?v=edff7f8a27": "edff7f8a27",
"./assets/js/viaje.js?v=e75eb3a1cc": "e75eb3a1cc",
"./assets/js/visamap.js?v=fdd854a86f": "fdd854a86f",
"./assets/vendor/Sortable.min.js": "18a2566c3d",
"./assets/vendor/images/layers-2x.png": "152a162333",
"./assets/vendor/images/layers.png": "c9e7528e49",
"./assets/vendor/images/marker-icon-2x.png": "cf3a536596",
"./assets/vendor/images/marker-icon.png": "60a90bcbb2",
"./assets/vendor/images/marker-shadow.png": "7b6a8df639",
"./assets/vendor/leaflet.css": "ec929f1100",
"./assets/vendor/leaflet.js": "5a640ff863",
"./manifest.webmanifest": "4000a74106"
};

const MAPA = './__a27-huellas.json';
const FIJAS = ['a27-tiles-esri', 'a27-fotos'];
const hex = buf => Array.from(new Uint8Array(buf), b => b.toString(16).padStart(2, '0')).join('');
self.addEventListener('install', e => {
  e.waitUntil((async () => {
    const nueva = await caches.open(VERSION);
    // Caché de la versión anterior con su mapa de huellas (la más reciente primero).
    let vieja = null, antes = {};
    const previas = (await caches.keys()).filter(k => k.startsWith('a27-') && k !== VERSION && !FIJAS.includes(k)).reverse();
    for (const k of previas) {
      const c = await caches.open(k), m = await c.match(MAPA);
      if (m) { vieja = c; antes = await m.json().catch(() => ({})); break; }
    }
    const urls = Object.keys(PRECACHE), guardado = {};
    let i = 0;
    const obrero = async () => {
      while (i < urls.length) {
        const u = urls[i++], h = PRECACHE[u];
        try {
          if (vieja && antes[u] === h) {
            const r = await vieja.match(u);
            if (r) { await nueva.put(u, r); guardado[u] = h; continue; }
          }
          // cache:'reload' salta la caché HTTP del navegador (GitHub la guarda 10 min).
          const res = await fetch(new Request(u, {cache: 'reload'}));
          if (!res.ok) continue;
          const buf = await res.clone().arrayBuffer();
          const ok = hex(await crypto.subtle.digest('SHA-1', buf)).slice(0, h.length) === h;
          await nueva.put(u, res);
          if (ok) guardado[u] = h;     // si el CDN aún servía la copia vieja, se vuelve a pedir la próxima vez
        } catch (_) {}
      }
    };
    await Promise.all(Array.from({length: 6}, obrero));
    await nueva.put(MAPA, new Response(JSON.stringify(guardado), {headers: {'Content-Type': 'application/json'}}));
    await self.skipWaiting();
  })());
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSION && !FIJAS.includes(k)).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('message', e => { if (e.data === 'skip') self.skipWaiting(); });
const guardar = (nombre, clave, res) => { if (res && (res.ok || res.type === 'opaque')) { const copia = res.clone(); caches.open(nombre).then(c => c.put(clave, copia)); } return res; };
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.hostname === 'router.project-osrm.org') return;   // rutas del Planificador: directo a la red
  if (url.hostname === 'server.arcgisonline.com') {
    e.respondWith(caches.open('a27-tiles-esri').then(c => c.match(req).then(m => m || fetch(req).then(res => { if (res.ok) c.put(req, res.clone()); return res; }).catch(() => new Response('', {status: 408})))));
    return;
  }
  const propio = url.origin === location.origin;
  // Páginas: siempre de la red (revalidando la caché HTTP); sin red, la copia guardada.
  if (req.mode === 'navigate' || (propio && url.pathname.endsWith('.html'))) {
    const clave = url.origin + url.pathname.replace(/index\.html$/, '');
    e.respondWith(fetch(clave + url.search, {cache: 'no-cache', credentials: 'same-origin'}).then(res => {
      if (res.redirected) return Response.redirect(res.url, 302);   // /pais → /pais/ (enlaces relativos)
      return res.ok ? guardar(VERSION, clave, res) : res;
    }).catch(() => caches.match(clave).then(m => m || caches.match('./'))));
    return;
  }
  if (propio) {
    const clave = url.origin + url.pathname;
    // ?v=huella: el contenido no cambia nunca para esa URL.
    if (url.searchParams.has('v')) {
      e.respondWith(caches.match(req).then(m => m || fetch(req).then(res => guardar(VERSION, req, res))
        .catch(() => caches.match(clave, {ignoreSearch: true}))));
      return;
    }
    // Datos y CSS/JS sin huella: de la red si hay (revalidando); sin red, la copia de la versión.
    if (url.pathname.endsWith('.json') || req.destination === 'style' || req.destination === 'script') {
      e.respondWith(fetch(req, {cache: 'no-cache'}).then(res => guardar(VERSION, clave, res))
        .catch(() => caches.match(clave, {ignoreSearch: true})));
      return;
    }
    // Fotos propias y el resto (KML, iconos…): se guardan al verlas, en una caché que sobrevive a las versiones.
    const fija = req.destination === 'image' || url.pathname.includes('/assets/img/');
    e.respondWith(caches.match(clave, {ignoreSearch: true}).then(m => m || fetch(req).then(res => guardar(fija ? 'a27-fotos' : VERSION, clave, res))));
    return;
  }
  // Fotos externas (Commons y otras webs): caché propia que no se borra al actualizar la app.
  if (req.destination === 'image') {
    e.respondWith(caches.match(req).then(m => m || fetch(req).then(res => guardar('a27-fotos', req, res))));
    return;
  }
  e.respondWith(caches.match(req).then(m => m || fetch(req).then(res =>
    (url.hostname.includes('gstatic') || url.hostname.includes('googleapis') || url.hostname.includes('unpkg') || url.hostname.includes('cdnjs') || url.hostname.includes('jsdelivr')) ? guardar(VERSION, req, res) : res)));
});

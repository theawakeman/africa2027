const VERSION = 'a27-20260927-1320';
const PRECACHE = {
"./cpd/": "6d9c9b8173",
"./documentacion/": "a57d95a5d7",
"./": "f29126d60d",
"./mapa/": "4ed9935a40",
"./paises/angola/historia/": "70d3c37a48",
"./paises/angola/": "f7260ff926",
"./paises/argelia/historia/": "160b2b9725",
"./paises/argelia/": "f88a27ab94",
"./paises/benin/historia/": "4f4dab77b1",
"./paises/benin/": "a4390c296f",
"./paises/botsuana/historia/": "6aba7c8dab",
"./paises/botsuana/": "fa4b537b48",
"./paises/burkina-faso/historia/": "69f24070fa",
"./paises/burkina-faso/": "e037041125",
"./paises/burundi/historia/": "6096b67c6a",
"./paises/burundi/": "163444d256",
"./paises/cabo-verde/historia/": "5ed724042e",
"./paises/cabo-verde/": "b588695c00",
"./paises/camerun/historia/": "0a354c3f2f",
"./paises/camerun/": "48e782c8d6",
"./paises/chad/historia/": "51d002786d",
"./paises/chad/": "b812c41973",
"./paises/comoras/historia/": "dbcd37faf1",
"./paises/comoras/": "035f7afd04",
"./paises/congo/historia/": "2f66f9962c",
"./paises/congo/": "eadae695bb",
"./paises/costa-de-marfil/historia/": "5ba529f477",
"./paises/costa-de-marfil/": "cb0e00ec9b",
"./paises/egipto/historia/": "8c88ed7141",
"./paises/egipto/": "4b41c96ce5",
"./paises/eritrea/historia/": "e25a96ce7a",
"./paises/eritrea/": "00817d24f9",
"./paises/esuatini/historia/": "e6eaaf6c61",
"./paises/esuatini/": "2d44405abf",
"./paises/etiopia/historia/": "f42d2b3caa",
"./paises/etiopia/": "c1e5f3c1ab",
"./paises/gabon/historia/": "91f48206d0",
"./paises/gabon/": "3c5d489936",
"./paises/gambia/historia/": "86268d8e83",
"./paises/gambia/": "ac3b198a7c",
"./paises/ghana/historia/": "bd71b29d28",
"./paises/ghana/": "dbb13d3f6b",
"./paises/guinea-bisau/historia/": "90ebe2d09f",
"./paises/guinea-bisau/": "52aaffe7d7",
"./paises/guinea-ecuatorial/historia/": "3ad01416e8",
"./paises/guinea-ecuatorial/": "c7e25b41d9",
"./paises/guinea/historia/": "fe3ae607de",
"./paises/guinea/": "53bf1e3676",
"./paises/kenia/historia/": "0ba3527d47",
"./paises/kenia/": "c59512aa68",
"./paises/lesoto/historia/": "80fd19de1a",
"./paises/lesoto/": "368ba01079",
"./paises/liberia/historia/": "d31ddabc4d",
"./paises/liberia/": "ba9ec7e211",
"./paises/libia/historia/": "73b5ddc60e",
"./paises/libia/": "1de08db2f1",
"./paises/madagascar/historia/": "db16f06691",
"./paises/madagascar/": "4b706a3d73",
"./paises/malaui/historia/": "91ec8c46da",
"./paises/malaui/": "d6486176be",
"./paises/mali/historia/": "42bbda4387",
"./paises/mali/": "169c8018d0",
"./paises/marruecos/historia/": "f45ad9a5e0",
"./paises/marruecos/": "aa179497c3",
"./paises/mauricio/historia/": "a28c3dc98e",
"./paises/mauricio/": "f307564a58",
"./paises/mauritania/historia/": "288c2b4ba8",
"./paises/mauritania/": "95ee3a4605",
"./paises/mozambique/historia/": "eb544934db",
"./paises/mozambique/": "316154b595",
"./paises/namibia/historia/": "c005e9c686",
"./paises/namibia/": "6c160ba4b1",
"./paises/niger/historia/": "2a5c7d6938",
"./paises/niger/": "5bc2c230c9",
"./paises/nigeria/historia/": "7ab4b7c682",
"./paises/nigeria/": "dce193a5ea",
"./paises/rca/historia/": "2c0a471e55",
"./paises/rca/": "21d8022e34",
"./paises/rd-congo/historia/": "9d4528ee80",
"./paises/rd-congo/": "a242535716",
"./paises/ruanda/historia/": "91a6100af5",
"./paises/ruanda/": "ae9f704c7c",
"./paises/sahara-occidental/historia/": "6080fa8855",
"./paises/sahara-occidental/": "8d59c89447",
"./paises/santo-tome/historia/": "003c4828a4",
"./paises/santo-tome/": "c258a9f91b",
"./paises/senegal/historia/": "cc11d7c7a6",
"./paises/senegal/": "669a32c5c3",
"./paises/seychelles/historia/": "ec842c10fe",
"./paises/seychelles/": "a178892e9d",
"./paises/sierra-leona/historia/": "fa94b49ede",
"./paises/sierra-leona/": "56586413c3",
"./paises/somalia/historia/": "19bb07453d",
"./paises/somalia/": "df222e980d",
"./paises/sudafrica/historia/": "dbb8599cad",
"./paises/sudafrica/": "31a6285376",
"./paises/sudan-del-sur/historia/": "029c8a650e",
"./paises/sudan-del-sur/": "8d66baba03",
"./paises/sudan/historia/": "a7bdf472c6",
"./paises/sudan/": "297367f7d8",
"./paises/tanzania/historia/": "3af2dc139a",
"./paises/tanzania/": "f60edde376",
"./paises/togo/historia/": "0dd4466917",
"./paises/togo/": "0d8c21dbb8",
"./paises/tunez/historia/": "d17c0862cc",
"./paises/tunez/": "04ff5c3b8c",
"./paises/uganda/historia/": "ab3beba084",
"./paises/uganda/": "c7da392ae3",
"./paises/yibuti/historia/": "d98322442b",
"./paises/yibuti/": "9a792de9f4",
"./paises/zambia/historia/": "c081450f6d",
"./paises/zambia/": "1bdec95764",
"./paises/zimbabue/historia/": "3042b1a658",
"./paises/zimbabue/": "14da302535",
"./perro/": "24aa0183d5",
"./planificador-clasico/": "bdfd34c9a6",
"./planificador-puntos/": "460104c761",
"./planificador/": "2f1dc10274",
"./presupuesto/": "9fd9ba9d89",
"./visados/": "8cd523d788",
"./assets/css/site.css?v=0c193d68a7": "0c193d68a7",
"./assets/icons/icon-192.png": "afb2518dd3",
"./assets/icons/icon-512.png": "195ee555af",
"./assets/icons/icon-maskable-512.png": "6c5d07d1cf",
"./assets/js/africa.geo.json": "efd2b0c9b4",
"./assets/js/cpdmap.js?v=cf099e102d": "cf099e102d",
"./assets/js/creador-pdi.js?v=97e92d7f30": "97e92d7f30",
"./assets/js/map.js?v=5bc6730f6d": "5bc6730f6d",
"./assets/js/pdi-detalle.json": "a9fe2e1fc6",
"./assets/js/perromap.js?v=cb72346aa0": "cb72346aa0",
"./assets/js/planificador-puntos.js?v=7a2172331c": "7a2172331c",
"./assets/js/planificador-puntos.json": "681eec41c7",
"./assets/js/presupuesto-xlsx.js?v=6cb35d90f7": "6cb35d90f7",
"./assets/js/presupuesto.js?v=5ae41123c1": "5ae41123c1",
"./assets/js/viaje.js?v=86b37c8e1e": "86b37c8e1e",
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
  if (url.origin === location.origin) {
    // Carcasa primero: lo que está en la caché de esta versión se sirve al instante,
    // sin esperar a la red (con una conexión lenta cada petición a GitHub tarda 1-3 s).
    // Las versiones nuevas llegan por el propio service worker: al publicar, se
    // instala en segundo plano bajando solo lo que ha cambiado y la página se recarga.
    const nav = req.mode === 'navigate', conV = url.searchParams.has('v');
    const limpia = url.origin + url.pathname.replace(/index\.html$/, '');
    const fija = req.destination === 'image' || url.pathname.includes('/assets/img/');
    e.respondWith((async () => {
      const c = await caches.open(VERSION);
      const m = (conV ? await c.match(url.href) : null) || await c.match(limpia) || (fija ? await caches.match(limpia) : null);
      if (m) return m;
      try {
        const res = nav ? await fetch(limpia + url.search, {cache: 'no-cache', credentials: 'same-origin'}) : await fetch(req);
        if (nav && res.redirected) return Response.redirect(res.url, 302);   // /pais → /pais/ (enlaces relativos)
        return guardar(fija ? 'a27-fotos' : VERSION, conV ? url.href : limpia, res);
      } catch (err) {
        return (await caches.match(limpia, {ignoreSearch: true})) || (nav ? await c.match(new URL('./', self.registration.scope).href) : null) || Response.error();
      }
    })());
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

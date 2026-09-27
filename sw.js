const VERSION = 'a27-20260927-1535';
const PRECACHE = {
"./cpd/": "488fe074a7",
"./documentacion/": "695ca27cab",
"./": "8b99c9e71a",
"./mapa/": "a1876189f7",
"./paises/angola/historia/": "901ffd7b42",
"./paises/angola/": "4b80a2a096",
"./paises/argelia/historia/": "05d2e8aa8b",
"./paises/argelia/": "91282beac8",
"./paises/benin/historia/": "2a476e9dcd",
"./paises/benin/": "0c3ff9fc9f",
"./paises/botsuana/historia/": "978f2c2386",
"./paises/botsuana/": "12147c33ec",
"./paises/burkina-faso/historia/": "c83c591f7c",
"./paises/burkina-faso/": "c2165101be",
"./paises/burundi/historia/": "c601612174",
"./paises/burundi/": "ada9538cbb",
"./paises/cabo-verde/historia/": "073e9a071c",
"./paises/cabo-verde/": "48600aab01",
"./paises/camerun/historia/": "1fff94079e",
"./paises/camerun/": "c288dfc0f1",
"./paises/chad/historia/": "a3441885d1",
"./paises/chad/": "abdfe1c59f",
"./paises/comoras/historia/": "63f7d02f49",
"./paises/comoras/": "9726cab3d9",
"./paises/congo/historia/": "8db9887ecd",
"./paises/congo/": "4813c6000a",
"./paises/costa-de-marfil/historia/": "3935f809bb",
"./paises/costa-de-marfil/": "cbe8df9947",
"./paises/egipto/historia/": "21c1dc77f2",
"./paises/egipto/": "6801d1f653",
"./paises/eritrea/historia/": "cb2aab9f6c",
"./paises/eritrea/": "fb4591c121",
"./paises/esuatini/historia/": "87912a1286",
"./paises/esuatini/": "a440ab93f7",
"./paises/etiopia/historia/": "33cd5c1d11",
"./paises/etiopia/": "d38e8f954f",
"./paises/gabon/historia/": "fbd31bc8cd",
"./paises/gabon/": "8804c0e75d",
"./paises/gambia/historia/": "d7f1615351",
"./paises/gambia/": "9740f3da88",
"./paises/ghana/historia/": "d5f9066d80",
"./paises/ghana/": "a73d82c53e",
"./paises/guinea-bisau/historia/": "a838a7bd48",
"./paises/guinea-bisau/": "eb08e0a068",
"./paises/guinea-ecuatorial/historia/": "af5b5f342f",
"./paises/guinea-ecuatorial/": "1235733adf",
"./paises/guinea/historia/": "f2be320040",
"./paises/guinea/": "e762a529c8",
"./paises/kenia/historia/": "fd9bd80c06",
"./paises/kenia/": "a1fbf09e61",
"./paises/lesoto/historia/": "afbfa91de3",
"./paises/lesoto/": "e4afa7c5b7",
"./paises/liberia/historia/": "0cfa9f2c20",
"./paises/liberia/": "ec21c4f2c7",
"./paises/libia/historia/": "430846c972",
"./paises/libia/": "3b8d333c16",
"./paises/madagascar/historia/": "8863d05eb9",
"./paises/madagascar/": "0e3dce1061",
"./paises/malaui/historia/": "eda0baef82",
"./paises/malaui/": "ab29117073",
"./paises/mali/historia/": "0ef12c43bd",
"./paises/mali/": "d4d1f8f476",
"./paises/marruecos/historia/": "ffee9ba8f7",
"./paises/marruecos/": "2d91a92c62",
"./paises/mauricio/historia/": "b8143dbea8",
"./paises/mauricio/": "6791da282c",
"./paises/mauritania/historia/": "1adcd9314b",
"./paises/mauritania/": "964fcf5150",
"./paises/mozambique/historia/": "226a26f369",
"./paises/mozambique/": "45252b568e",
"./paises/namibia/historia/": "2d8efd4b0f",
"./paises/namibia/": "6e626ffc81",
"./paises/niger/historia/": "9c2c4da56a",
"./paises/niger/": "61d3e5cc38",
"./paises/nigeria/historia/": "37dbcfb049",
"./paises/nigeria/": "8866c7d2c7",
"./paises/rca/historia/": "0e7f6e812b",
"./paises/rca/": "fbfc262a59",
"./paises/rd-congo/historia/": "4954c871e8",
"./paises/rd-congo/": "f0f70e2223",
"./paises/ruanda/historia/": "55804d90bf",
"./paises/ruanda/": "7a12e3e5c4",
"./paises/sahara-occidental/historia/": "7dd04258ba",
"./paises/sahara-occidental/": "5a72bfbf37",
"./paises/santo-tome/historia/": "dded16c96c",
"./paises/santo-tome/": "b31e8ae251",
"./paises/senegal/historia/": "6e48eb11eb",
"./paises/senegal/": "64c7cfcc91",
"./paises/seychelles/historia/": "d7375a502b",
"./paises/seychelles/": "f4a23cef8f",
"./paises/sierra-leona/historia/": "b1b121722a",
"./paises/sierra-leona/": "8d7bb0d52e",
"./paises/somalia/historia/": "2042347168",
"./paises/somalia/": "4542112803",
"./paises/sudafrica/historia/": "d9f7270f86",
"./paises/sudafrica/": "09c7630dc1",
"./paises/sudan-del-sur/historia/": "5ad0a95d74",
"./paises/sudan-del-sur/": "364c531b38",
"./paises/sudan/historia/": "6b373c570a",
"./paises/sudan/": "af8d60a4ca",
"./paises/tanzania/historia/": "257285868e",
"./paises/tanzania/": "825f4afe78",
"./paises/togo/historia/": "adf22b7586",
"./paises/togo/": "cbd0b282ff",
"./paises/tunez/historia/": "5781580b9f",
"./paises/tunez/": "d280a7330e",
"./paises/uganda/historia/": "d66cc21559",
"./paises/uganda/": "dae74ba87e",
"./paises/yibuti/historia/": "3dc9ddc322",
"./paises/yibuti/": "e764c67bde",
"./paises/zambia/historia/": "f5e859f3db",
"./paises/zambia/": "8cad1ff064",
"./paises/zimbabue/historia/": "e910cbb6c4",
"./paises/zimbabue/": "7cb07e13c5",
"./perro/": "27ffd269c4",
"./planificador-clasico/": "c60fd9e2a4",
"./planificador-puntos/": "7c15720b86",
"./planificador/": "707c122d0c",
"./presupuesto/": "c505763f1d",
"./visados/": "c9468225d1",
"./assets/css/site.css?v=995f70dd36": "995f70dd36",
"./assets/icons/icon-192.png": "afb2518dd3",
"./assets/icons/icon-512.png": "195ee555af",
"./assets/icons/icon-maskable-512.png": "6c5d07d1cf",
"./assets/js/africa.geo.json": "efd2b0c9b4",
"./assets/js/cpdmap.js?v=cf099e102d": "cf099e102d",
"./assets/js/creador-pdi.js?v=97e92d7f30": "97e92d7f30",
"./assets/js/fotos-4x4.js?v=bafe6b8cc4": "bafe6b8cc4",
"./assets/js/map.js?v=29484ec2a4": "29484ec2a4",
"./assets/js/pdi-detalle.json": "7bd8ca7b09",
"./assets/js/perromap.js?v=cb72346aa0": "cb72346aa0",
"./assets/js/planificador-puntos.js?v=aaf80002b0": "aaf80002b0",
"./assets/js/planificador-puntos.json": "9078f0dc1a",
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

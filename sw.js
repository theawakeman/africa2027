const VERSION = 'a27-20260927-1437';
const PRECACHE = {
"./cpd/": "dbf82aecae",
"./documentacion/": "9dbbae47c8",
"./": "3cd066cd2a",
"./mapa/": "dec352db86",
"./paises/angola/historia/": "9b801b204e",
"./paises/angola/": "dd6c539853",
"./paises/argelia/historia/": "33ac8896d3",
"./paises/argelia/": "9a0c3b2c3a",
"./paises/benin/historia/": "a6ef554f8f",
"./paises/benin/": "aac3121bf3",
"./paises/botsuana/historia/": "2e29a1d2f2",
"./paises/botsuana/": "ba617a6e95",
"./paises/burkina-faso/historia/": "2d8a7c145d",
"./paises/burkina-faso/": "7ed1e548f1",
"./paises/burundi/historia/": "dc136a545f",
"./paises/burundi/": "35764ab102",
"./paises/cabo-verde/historia/": "1127a85306",
"./paises/cabo-verde/": "8b10a23437",
"./paises/camerun/historia/": "2fcd622992",
"./paises/camerun/": "efca11a7b0",
"./paises/chad/historia/": "0215e2a672",
"./paises/chad/": "80151249fb",
"./paises/comoras/historia/": "27f48469c3",
"./paises/comoras/": "bdde6053f8",
"./paises/congo/historia/": "9e48cc6c49",
"./paises/congo/": "979e839253",
"./paises/costa-de-marfil/historia/": "a999e84a33",
"./paises/costa-de-marfil/": "600e7ae6b4",
"./paises/egipto/historia/": "f0e6d653dd",
"./paises/egipto/": "a758aa514a",
"./paises/eritrea/historia/": "349cc3c773",
"./paises/eritrea/": "3adf83180b",
"./paises/esuatini/historia/": "7c8d92df2d",
"./paises/esuatini/": "dcf144dedb",
"./paises/etiopia/historia/": "4fd7e18b8a",
"./paises/etiopia/": "29d9550ab5",
"./paises/gabon/historia/": "8b306fcbc4",
"./paises/gabon/": "50ea42f275",
"./paises/gambia/historia/": "d1cd2d3f62",
"./paises/gambia/": "e0683e0bbc",
"./paises/ghana/historia/": "7e8e4eadd3",
"./paises/ghana/": "cc1df20d27",
"./paises/guinea-bisau/historia/": "7e1df55b40",
"./paises/guinea-bisau/": "3d2efbbc35",
"./paises/guinea-ecuatorial/historia/": "b17e802af9",
"./paises/guinea-ecuatorial/": "3d829b63ae",
"./paises/guinea/historia/": "f5fabc121b",
"./paises/guinea/": "6bda1a76c3",
"./paises/kenia/historia/": "bd7cf7d698",
"./paises/kenia/": "deaeb049b9",
"./paises/lesoto/historia/": "d68aa2e8e0",
"./paises/lesoto/": "e68ed0407b",
"./paises/liberia/historia/": "00e074546b",
"./paises/liberia/": "ec34a0926c",
"./paises/libia/historia/": "ea1e547ffb",
"./paises/libia/": "b536d4d2fc",
"./paises/madagascar/historia/": "78373acffe",
"./paises/madagascar/": "2731b87eb5",
"./paises/malaui/historia/": "3909a4e081",
"./paises/malaui/": "b3df1f9551",
"./paises/mali/historia/": "390ba496d4",
"./paises/mali/": "188adc3b94",
"./paises/marruecos/historia/": "81ac1f7bce",
"./paises/marruecos/": "2c55a98455",
"./paises/mauricio/historia/": "ca730f3d25",
"./paises/mauricio/": "9bab6ddfd7",
"./paises/mauritania/historia/": "23cb72eb17",
"./paises/mauritania/": "97a290ea93",
"./paises/mozambique/historia/": "d77a51d283",
"./paises/mozambique/": "b964f2d61f",
"./paises/namibia/historia/": "238b585fe4",
"./paises/namibia/": "eb8dbb7e12",
"./paises/niger/historia/": "e47db130e4",
"./paises/niger/": "ed2e87fd31",
"./paises/nigeria/historia/": "a5b5ed50ee",
"./paises/nigeria/": "e57770709a",
"./paises/rca/historia/": "4fc4d45ae6",
"./paises/rca/": "22c0563643",
"./paises/rd-congo/historia/": "d303b86438",
"./paises/rd-congo/": "e87db74be9",
"./paises/ruanda/historia/": "98946bc9b8",
"./paises/ruanda/": "21177fd5d3",
"./paises/sahara-occidental/historia/": "f9f30d7c10",
"./paises/sahara-occidental/": "0e3201ac13",
"./paises/santo-tome/historia/": "e6ef9b7016",
"./paises/santo-tome/": "261cf5d011",
"./paises/senegal/historia/": "25711dc823",
"./paises/senegal/": "eb2752e880",
"./paises/seychelles/historia/": "daf552678c",
"./paises/seychelles/": "97f2765df0",
"./paises/sierra-leona/historia/": "f06b15ce0b",
"./paises/sierra-leona/": "97fee5a727",
"./paises/somalia/historia/": "654ed71132",
"./paises/somalia/": "e700209c80",
"./paises/sudafrica/historia/": "87c75726a2",
"./paises/sudafrica/": "af0941276a",
"./paises/sudan-del-sur/historia/": "8fbc387e68",
"./paises/sudan-del-sur/": "216f4fd02e",
"./paises/sudan/historia/": "84e80a0a47",
"./paises/sudan/": "7c735046c3",
"./paises/tanzania/historia/": "f4daf40968",
"./paises/tanzania/": "22fe186983",
"./paises/togo/historia/": "2bdaf5d53b",
"./paises/togo/": "3c30d3b3a4",
"./paises/tunez/historia/": "d9f0b77de3",
"./paises/tunez/": "d24dcb5580",
"./paises/uganda/historia/": "f1fa2380db",
"./paises/uganda/": "6b752d7cc9",
"./paises/yibuti/historia/": "bb55049d4c",
"./paises/yibuti/": "772d314378",
"./paises/zambia/historia/": "c458be1b3a",
"./paises/zambia/": "ec8c3a6682",
"./paises/zimbabue/historia/": "4c34b55fe4",
"./paises/zimbabue/": "750365bc25",
"./perro/": "14110f80c7",
"./planificador-clasico/": "205ba0b142",
"./planificador-puntos/": "6301576900",
"./planificador/": "231ae42577",
"./presupuesto/": "e5fc8e16d1",
"./visados/": "cee0fc1a48",
"./assets/css/site.css?v=a435449e0c": "a435449e0c",
"./assets/icons/icon-192.png": "afb2518dd3",
"./assets/icons/icon-512.png": "195ee555af",
"./assets/icons/icon-maskable-512.png": "6c5d07d1cf",
"./assets/js/africa.geo.json": "efd2b0c9b4",
"./assets/js/cpdmap.js?v=cf099e102d": "cf099e102d",
"./assets/js/creador-pdi.js?v=97e92d7f30": "97e92d7f30",
"./assets/js/map.js?v=f82604df3d": "f82604df3d",
"./assets/js/pdi-detalle.json": "525964c408",
"./assets/js/perromap.js?v=cb72346aa0": "cb72346aa0",
"./assets/js/planificador-puntos.js?v=3c41440699": "3c41440699",
"./assets/js/planificador-puntos.json": "a876282913",
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

const VERSION = 'a27-20260927-2003';
const PRECACHE = {
"./cpd/": "6a874877ee",
"./documentacion/": "b3793f5d58",
"./": "a6ff1955c5",
"./mapa/": "b366db1e1d",
"./paises/angola/historia/": "717b072a02",
"./paises/angola/": "165a367c1b",
"./paises/argelia/historia/": "a11191e70a",
"./paises/argelia/": "0d3d473563",
"./paises/benin/historia/": "2bd6dfc60f",
"./paises/benin/": "b66b6c6080",
"./paises/botsuana/historia/": "728ff5506d",
"./paises/botsuana/": "497e54bfd5",
"./paises/burkina-faso/historia/": "218dbc56ec",
"./paises/burkina-faso/": "5a090d5f66",
"./paises/burundi/historia/": "be725dcf7e",
"./paises/burundi/": "8582b2f9fa",
"./paises/cabo-verde/historia/": "4d1838929c",
"./paises/cabo-verde/": "82b1617265",
"./paises/camerun/historia/": "9b1536b29e",
"./paises/camerun/": "dc4cb4d51c",
"./paises/chad/historia/": "0630a41d41",
"./paises/chad/": "ef60fa77ef",
"./paises/comoras/historia/": "f5502cbd00",
"./paises/comoras/": "2679b9d183",
"./paises/congo/historia/": "13225d5fb0",
"./paises/congo/": "d82f06f7a5",
"./paises/costa-de-marfil/historia/": "80c6d676e8",
"./paises/costa-de-marfil/": "f9479d4c50",
"./paises/egipto/historia/": "fab5bff6c3",
"./paises/egipto/": "85a6961a3a",
"./paises/eritrea/historia/": "db9c6f9387",
"./paises/eritrea/": "10f8c5c05f",
"./paises/esuatini/historia/": "280887ffb4",
"./paises/esuatini/": "62a25450fb",
"./paises/etiopia/historia/": "36a9653f90",
"./paises/etiopia/": "0346e1f5c2",
"./paises/gabon/historia/": "e49317fad2",
"./paises/gabon/": "98ed5112d8",
"./paises/gambia/historia/": "ca959e40c7",
"./paises/gambia/": "b431b648fb",
"./paises/ghana/historia/": "4d865c33db",
"./paises/ghana/": "4826fb5ac5",
"./paises/guinea-bisau/historia/": "da4cf0d601",
"./paises/guinea-bisau/": "0f03d1feb8",
"./paises/guinea-ecuatorial/historia/": "ea0c39cccf",
"./paises/guinea-ecuatorial/": "6e9845ccf5",
"./paises/guinea/historia/": "8bbf4100d4",
"./paises/guinea/": "bceb565b98",
"./paises/kenia/historia/": "72745ca9f7",
"./paises/kenia/": "94d409f015",
"./paises/lesoto/historia/": "3ec53d279f",
"./paises/lesoto/": "09073a7afa",
"./paises/liberia/historia/": "16d3274813",
"./paises/liberia/": "ca69ba7746",
"./paises/libia/historia/": "47d2e4a683",
"./paises/libia/": "29a060afe1",
"./paises/madagascar/historia/": "65ef6d5c60",
"./paises/madagascar/": "c835b2d593",
"./paises/malaui/historia/": "f166e2ff57",
"./paises/malaui/": "09ef6ebd58",
"./paises/mali/historia/": "1137bbb3cb",
"./paises/mali/": "a9a957f2fd",
"./paises/marruecos/historia/": "e1dbc0bdd3",
"./paises/marruecos/": "ad03685f38",
"./paises/mauricio/historia/": "b55deac668",
"./paises/mauricio/": "d4e78f3770",
"./paises/mauritania/historia/": "e875aab2cf",
"./paises/mauritania/": "3e1f66cda7",
"./paises/mozambique/historia/": "78f23be3e8",
"./paises/mozambique/": "78d5bb0400",
"./paises/namibia/historia/": "c3b1f3d723",
"./paises/namibia/": "e65ff94800",
"./paises/niger/historia/": "38f95ab9f7",
"./paises/niger/": "fdb0d12300",
"./paises/nigeria/historia/": "70b7f9c4f1",
"./paises/nigeria/": "9ad4653ffb",
"./paises/rca/historia/": "3974550e53",
"./paises/rca/": "4c23a540e5",
"./paises/rd-congo/historia/": "b8aa5d494e",
"./paises/rd-congo/": "494485817f",
"./paises/ruanda/historia/": "9b31f175e2",
"./paises/ruanda/": "cff84630fa",
"./paises/sahara-occidental/historia/": "30e24ce33c",
"./paises/sahara-occidental/": "4c1c269dae",
"./paises/santo-tome/historia/": "f745415e92",
"./paises/santo-tome/": "00cc2f051b",
"./paises/senegal/historia/": "849ebb6b74",
"./paises/senegal/": "23cb04bc9a",
"./paises/seychelles/historia/": "8487f6294f",
"./paises/seychelles/": "4075da3685",
"./paises/sierra-leona/historia/": "43a1856222",
"./paises/sierra-leona/": "f91fcdf96e",
"./paises/somalia/historia/": "63e8e7792f",
"./paises/somalia/": "f18fb7c53e",
"./paises/sudafrica/historia/": "ff4107cfd6",
"./paises/sudafrica/": "53277d504c",
"./paises/sudan-del-sur/historia/": "b2134c04c9",
"./paises/sudan-del-sur/": "9032d4f1fe",
"./paises/sudan/historia/": "be197f6428",
"./paises/sudan/": "b9a5489c7a",
"./paises/tanzania/historia/": "93d882aafa",
"./paises/tanzania/": "eeeae6b09b",
"./paises/togo/historia/": "a332b3ebae",
"./paises/togo/": "9cdd657f8a",
"./paises/tunez/historia/": "dbc5184fb3",
"./paises/tunez/": "0f28555999",
"./paises/uganda/historia/": "1656f23c91",
"./paises/uganda/": "bad4b96960",
"./paises/yibuti/historia/": "a48d8d08f9",
"./paises/yibuti/": "55dbc0550d",
"./paises/zambia/historia/": "bc0031fa36",
"./paises/zambia/": "0da7792ee1",
"./paises/zimbabue/historia/": "a76845ff6c",
"./paises/zimbabue/": "2739e54fd0",
"./perro/": "2a112a98dc",
"./planificador-clasico/": "bc92262c9a",
"./planificador-puntos/": "f5174aa705",
"./planificador/": "7798c4ffb3",
"./presupuesto/": "d88df30611",
"./visados/": "48354db128",
"./assets/css/site.css?v=3cac24495c": "3cac24495c",
"./assets/icons/icon-192.png": "afb2518dd3",
"./assets/icons/icon-512.png": "195ee555af",
"./assets/icons/icon-maskable-512.png": "6c5d07d1cf",
"./assets/js/africa.geo.json": "c0b7c9f03c",
"./assets/js/cpdmap.js?v=cce81a6e10": "cce81a6e10",
"./assets/js/creador-pdi.js?v=569eeec2d5": "569eeec2d5",
"./assets/js/fotos-4x4.js?v=7d053de40f": "7d053de40f",
"./assets/js/map.js?v=29484ec2a4": "29484ec2a4",
"./assets/js/pdi-detalle.json": "c36abf7bc4",
"./assets/js/perromap.js?v=54b952ce88": "54b952ce88",
"./assets/js/planificador-puntos.js?v=4fb5a7358a": "4fb5a7358a",
"./assets/js/planificador-puntos.json": "373ef14ff4",
"./assets/js/presupuesto-xlsx.js?v=6cb35d90f7": "6cb35d90f7",
"./assets/js/presupuesto.js?v=5ae41123c1": "5ae41123c1",
"./assets/js/viaje.js?v=81939df31c": "81939df31c",
"./assets/js/visamap.js?v=1ba5c52726": "1ba5c52726",
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

const VERSION = 'a27-20260927-1730';
const PRECACHE = {
"./cpd/": "3101fb1b9a",
"./documentacion/": "c818230218",
"./": "bdeddde1b0",
"./mapa/": "55025fbb3b",
"./paises/angola/historia/": "2a248cbf4c",
"./paises/angola/": "f0c2d20654",
"./paises/argelia/historia/": "98ace6bfb4",
"./paises/argelia/": "4b0b441bbd",
"./paises/benin/historia/": "f824a08a24",
"./paises/benin/": "a3e208ab45",
"./paises/botsuana/historia/": "83897b80a9",
"./paises/botsuana/": "1dc110c78c",
"./paises/burkina-faso/historia/": "7fa7c91d32",
"./paises/burkina-faso/": "deee9803eb",
"./paises/burundi/historia/": "bc8891d2ea",
"./paises/burundi/": "94b90e986e",
"./paises/cabo-verde/historia/": "a2d58a1849",
"./paises/cabo-verde/": "a5804939c9",
"./paises/camerun/historia/": "dfe3f8bd40",
"./paises/camerun/": "0567060cbb",
"./paises/chad/historia/": "4706773fb5",
"./paises/chad/": "3d6dbd2856",
"./paises/comoras/historia/": "5024cdf9d0",
"./paises/comoras/": "991b6307f7",
"./paises/congo/historia/": "6d210aef1b",
"./paises/congo/": "13c771142b",
"./paises/costa-de-marfil/historia/": "71d1fd7c57",
"./paises/costa-de-marfil/": "4ea55a0a20",
"./paises/egipto/historia/": "494b8ad246",
"./paises/egipto/": "ea13a788a8",
"./paises/eritrea/historia/": "5fa8920035",
"./paises/eritrea/": "ee53e3fd8a",
"./paises/esuatini/historia/": "a890380722",
"./paises/esuatini/": "d4ca6f3e08",
"./paises/etiopia/historia/": "5be765a0e2",
"./paises/etiopia/": "5ea7d630af",
"./paises/gabon/historia/": "61d3a001b7",
"./paises/gabon/": "ba783d64ad",
"./paises/gambia/historia/": "f935d05bf6",
"./paises/gambia/": "1d0594a849",
"./paises/ghana/historia/": "331ee07e1c",
"./paises/ghana/": "013edbcf81",
"./paises/guinea-bisau/historia/": "213089deb2",
"./paises/guinea-bisau/": "325b23ade9",
"./paises/guinea-ecuatorial/historia/": "ef91b0a80e",
"./paises/guinea-ecuatorial/": "d642aa2cff",
"./paises/guinea/historia/": "12c1b0bb6c",
"./paises/guinea/": "ff18eca2ad",
"./paises/kenia/historia/": "dad8d5d46c",
"./paises/kenia/": "669f7155d1",
"./paises/lesoto/historia/": "b892d18685",
"./paises/lesoto/": "3968ebd861",
"./paises/liberia/historia/": "a20bad687a",
"./paises/liberia/": "030fde3207",
"./paises/libia/historia/": "770df45ba7",
"./paises/libia/": "11dd375657",
"./paises/madagascar/historia/": "5a9e25c706",
"./paises/madagascar/": "69aded9da1",
"./paises/malaui/historia/": "5452ba370a",
"./paises/malaui/": "4af83a06da",
"./paises/mali/historia/": "ba19d1f263",
"./paises/mali/": "65fbe3042b",
"./paises/marruecos/historia/": "d0b1f1adef",
"./paises/marruecos/": "7b976a487e",
"./paises/mauricio/historia/": "3207782c7a",
"./paises/mauricio/": "06fc227120",
"./paises/mauritania/historia/": "c5cb5aa9c4",
"./paises/mauritania/": "32bc8a5069",
"./paises/mozambique/historia/": "f008742dc3",
"./paises/mozambique/": "e95b85e424",
"./paises/namibia/historia/": "c786dfaa87",
"./paises/namibia/": "e49e3d8d1a",
"./paises/niger/historia/": "3946fa9217",
"./paises/niger/": "15d02332a3",
"./paises/nigeria/historia/": "421e2af0dc",
"./paises/nigeria/": "bf22d4ffea",
"./paises/rca/historia/": "a7d5a8d30a",
"./paises/rca/": "0d8327a42f",
"./paises/rd-congo/historia/": "9f16aafbe1",
"./paises/rd-congo/": "4bf9db64fb",
"./paises/ruanda/historia/": "74a0232a16",
"./paises/ruanda/": "a097f625f2",
"./paises/sahara-occidental/historia/": "dac79dc931",
"./paises/sahara-occidental/": "ec6e0a5d83",
"./paises/santo-tome/historia/": "aef319a934",
"./paises/santo-tome/": "24dd9afcee",
"./paises/senegal/historia/": "b9f11b7bf6",
"./paises/senegal/": "3b5c983cd2",
"./paises/seychelles/historia/": "5be926290f",
"./paises/seychelles/": "21e7afc2dc",
"./paises/sierra-leona/historia/": "1cf6051f39",
"./paises/sierra-leona/": "f9ed995f37",
"./paises/somalia/historia/": "f837b38850",
"./paises/somalia/": "f47ee7943d",
"./paises/sudafrica/historia/": "621c3485bf",
"./paises/sudafrica/": "a8e65cfefb",
"./paises/sudan-del-sur/historia/": "da05a6f319",
"./paises/sudan-del-sur/": "63e27651ae",
"./paises/sudan/historia/": "fde99451c1",
"./paises/sudan/": "39dc71724b",
"./paises/tanzania/historia/": "15f4a7314b",
"./paises/tanzania/": "9c9516429e",
"./paises/togo/historia/": "7a8f8d727b",
"./paises/togo/": "85a8563b70",
"./paises/tunez/historia/": "321b0d61d1",
"./paises/tunez/": "4c084e13cb",
"./paises/uganda/historia/": "f248cceed0",
"./paises/uganda/": "248a19309b",
"./paises/yibuti/historia/": "15732281ed",
"./paises/yibuti/": "5ea96890d0",
"./paises/zambia/historia/": "32e3d8f6ae",
"./paises/zambia/": "9d85c0eacd",
"./paises/zimbabue/historia/": "0b819c3011",
"./paises/zimbabue/": "c8e286820e",
"./perro/": "dd85675109",
"./planificador-clasico/": "a93159d53f",
"./planificador-puntos/": "2926baba1a",
"./planificador/": "88c3f430ca",
"./presupuesto/": "9edcd2b43b",
"./visados/": "ba19302cf3",
"./assets/css/site.css?v=b8ec3f9201": "b8ec3f9201",
"./assets/icons/icon-192.png": "afb2518dd3",
"./assets/icons/icon-512.png": "195ee555af",
"./assets/icons/icon-maskable-512.png": "6c5d07d1cf",
"./assets/js/africa.geo.json": "c0b7c9f03c",
"./assets/js/cpdmap.js?v=cf099e102d": "cf099e102d",
"./assets/js/creador-pdi.js?v=569eeec2d5": "569eeec2d5",
"./assets/js/fotos-4x4.js?v=7d053de40f": "7d053de40f",
"./assets/js/map.js?v=29484ec2a4": "29484ec2a4",
"./assets/js/pdi-detalle.json": "fe12fcd59f",
"./assets/js/perromap.js?v=cb72346aa0": "cb72346aa0",
"./assets/js/planificador-puntos.js?v=963667795d": "963667795d",
"./assets/js/planificador-puntos.json": "fc17a73254",
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

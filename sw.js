const VERSION = 'a27-20260927-1343';
const PRECACHE = {
"./cpd/": "31980f93f1",
"./documentacion/": "ee6231c889",
"./": "cc4cc19f19",
"./mapa/": "661ecc3ce5",
"./paises/angola/historia/": "92951041f2",
"./paises/angola/": "c98cd00a18",
"./paises/argelia/historia/": "b9827e80ca",
"./paises/argelia/": "2b2cd32feb",
"./paises/benin/historia/": "3e394bfb3d",
"./paises/benin/": "3a701108ab",
"./paises/botsuana/historia/": "b73de2d595",
"./paises/botsuana/": "e503d46390",
"./paises/burkina-faso/historia/": "c01e80f333",
"./paises/burkina-faso/": "59e4ae4d7e",
"./paises/burundi/historia/": "61fd97accf",
"./paises/burundi/": "d2343ee758",
"./paises/cabo-verde/historia/": "bc51936132",
"./paises/cabo-verde/": "b442f51ae8",
"./paises/camerun/historia/": "0da9091166",
"./paises/camerun/": "3bb1d09cb2",
"./paises/chad/historia/": "fafa187dcf",
"./paises/chad/": "d7b0c258d5",
"./paises/comoras/historia/": "18cf8208c3",
"./paises/comoras/": "6a5bda3da3",
"./paises/congo/historia/": "3b3aaa0267",
"./paises/congo/": "560444708e",
"./paises/costa-de-marfil/historia/": "e084da5e8a",
"./paises/costa-de-marfil/": "d43b7f3a37",
"./paises/egipto/historia/": "84f2c09b8b",
"./paises/egipto/": "27aafd9c4a",
"./paises/eritrea/historia/": "420e33791c",
"./paises/eritrea/": "c95bdfa922",
"./paises/esuatini/historia/": "d2041f959f",
"./paises/esuatini/": "718f111237",
"./paises/etiopia/historia/": "c33f772ed1",
"./paises/etiopia/": "f7e463e7b6",
"./paises/gabon/historia/": "6e40618c3d",
"./paises/gabon/": "6ea2433102",
"./paises/gambia/historia/": "73229bc571",
"./paises/gambia/": "366edc6487",
"./paises/ghana/historia/": "1bf718b432",
"./paises/ghana/": "2006d0dab6",
"./paises/guinea-bisau/historia/": "98bc2f768b",
"./paises/guinea-bisau/": "77bfca8d8d",
"./paises/guinea-ecuatorial/historia/": "190f6b874b",
"./paises/guinea-ecuatorial/": "57ec776b0d",
"./paises/guinea/historia/": "581e569f43",
"./paises/guinea/": "ee0573f556",
"./paises/kenia/historia/": "a91ef4e8a0",
"./paises/kenia/": "2534956ff4",
"./paises/lesoto/historia/": "7a2e34653a",
"./paises/lesoto/": "e98e16db70",
"./paises/liberia/historia/": "31e63006b4",
"./paises/liberia/": "290086de0c",
"./paises/libia/historia/": "904e06292e",
"./paises/libia/": "cf822c7c75",
"./paises/madagascar/historia/": "3a42ea3028",
"./paises/madagascar/": "f84d5e83ad",
"./paises/malaui/historia/": "5f0be54984",
"./paises/malaui/": "c8e8086b51",
"./paises/mali/historia/": "8a2bb99c05",
"./paises/mali/": "4a9ccd4d33",
"./paises/marruecos/historia/": "02b972d876",
"./paises/marruecos/": "3f694e7337",
"./paises/mauricio/historia/": "5a05ea3051",
"./paises/mauricio/": "a4ef824b16",
"./paises/mauritania/historia/": "dadd96e604",
"./paises/mauritania/": "8e76a12d28",
"./paises/mozambique/historia/": "7313da7724",
"./paises/mozambique/": "050d602d03",
"./paises/namibia/historia/": "216fb10900",
"./paises/namibia/": "1ea841cf28",
"./paises/niger/historia/": "221024cf89",
"./paises/niger/": "96f9d88583",
"./paises/nigeria/historia/": "e4ae4e8d6f",
"./paises/nigeria/": "ae99a45273",
"./paises/rca/historia/": "db767a85fa",
"./paises/rca/": "d316bb4265",
"./paises/rd-congo/historia/": "7b095df484",
"./paises/rd-congo/": "62e238d402",
"./paises/ruanda/historia/": "62ebc74f55",
"./paises/ruanda/": "dc1972a864",
"./paises/sahara-occidental/historia/": "2eb2cee8f9",
"./paises/sahara-occidental/": "2a5af15ab9",
"./paises/santo-tome/historia/": "619155d500",
"./paises/santo-tome/": "c52ab52b76",
"./paises/senegal/historia/": "af4e0a5477",
"./paises/senegal/": "2105fa536d",
"./paises/seychelles/historia/": "6591cb1c62",
"./paises/seychelles/": "1599f90a72",
"./paises/sierra-leona/historia/": "c2a7e00736",
"./paises/sierra-leona/": "4459351260",
"./paises/somalia/historia/": "8144c17998",
"./paises/somalia/": "ea253c2451",
"./paises/sudafrica/historia/": "d6b5acd4af",
"./paises/sudafrica/": "35f58fba9b",
"./paises/sudan-del-sur/historia/": "e029cbcab7",
"./paises/sudan-del-sur/": "05c5e959ee",
"./paises/sudan/historia/": "811990ba7e",
"./paises/sudan/": "0410fa8020",
"./paises/tanzania/historia/": "2f892ad1cf",
"./paises/tanzania/": "864c7aaeb3",
"./paises/togo/historia/": "d0e1def68e",
"./paises/togo/": "5e72f2d133",
"./paises/tunez/historia/": "77599cc8a0",
"./paises/tunez/": "3e7ba54e09",
"./paises/uganda/historia/": "e872d1d720",
"./paises/uganda/": "d4bf055087",
"./paises/yibuti/historia/": "ddd4d4b5e2",
"./paises/yibuti/": "f340b21734",
"./paises/zambia/historia/": "b668474aea",
"./paises/zambia/": "581cf6eb9b",
"./paises/zimbabue/historia/": "0727e2f367",
"./paises/zimbabue/": "a34899a52b",
"./perro/": "4794b0eb3b",
"./planificador-clasico/": "c7eccfa666",
"./planificador-puntos/": "079fb10d36",
"./planificador/": "87f14d7277",
"./presupuesto/": "062ab36305",
"./visados/": "3e507cd221",
"./assets/css/site.css?v=4b5d73c227": "4b5d73c227",
"./assets/icons/icon-192.png": "afb2518dd3",
"./assets/icons/icon-512.png": "195ee555af",
"./assets/icons/icon-maskable-512.png": "6c5d07d1cf",
"./assets/js/africa.geo.json": "efd2b0c9b4",
"./assets/js/cpdmap.js?v=cf099e102d": "cf099e102d",
"./assets/js/creador-pdi.js?v=97e92d7f30": "97e92d7f30",
"./assets/js/map.js?v=5bc6730f6d": "5bc6730f6d",
"./assets/js/pdi-detalle.json": "a9fe2e1fc6",
"./assets/js/perromap.js?v=cb72346aa0": "cb72346aa0",
"./assets/js/planificador-puntos.js?v=3bbf622386": "3bbf622386",
"./assets/js/planificador-puntos.json": "14243f66a3",
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

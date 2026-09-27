const VERSION = 'a27-20260927-1301';
const PRECACHE = {
"./cpd/": "a85b602616",
"./documentacion/": "83ead303cc",
"./": "ff1c488f1c",
"./mapa/": "9e1999e51a",
"./paises/angola/historia/": "77a08e6577",
"./paises/angola/": "8f974fd967",
"./paises/argelia/historia/": "c36dfb3acf",
"./paises/argelia/": "b74e774ab9",
"./paises/benin/historia/": "47bb212bfa",
"./paises/benin/": "7d99afd9e5",
"./paises/botsuana/historia/": "ab03a200cb",
"./paises/botsuana/": "82d94292c0",
"./paises/burkina-faso/historia/": "24a819fae7",
"./paises/burkina-faso/": "020808510c",
"./paises/burundi/historia/": "46d5625b17",
"./paises/burundi/": "e9f7afd8d5",
"./paises/cabo-verde/historia/": "9d02e1cac4",
"./paises/cabo-verde/": "5bffcb9bd1",
"./paises/camerun/historia/": "657a45d054",
"./paises/camerun/": "2482fd9c39",
"./paises/chad/historia/": "3fcc4ff645",
"./paises/chad/": "212bcb3157",
"./paises/comoras/historia/": "e095944a62",
"./paises/comoras/": "8d721534d9",
"./paises/congo/historia/": "16eaa8a11e",
"./paises/congo/": "65e97334a6",
"./paises/costa-de-marfil/historia/": "f7da5a2f86",
"./paises/costa-de-marfil/": "42821c6b3e",
"./paises/egipto/historia/": "592ec2aebb",
"./paises/egipto/": "b1c548b810",
"./paises/eritrea/historia/": "cf2265fe9a",
"./paises/eritrea/": "086425c5e2",
"./paises/esuatini/historia/": "91b2636a4e",
"./paises/esuatini/": "979b7cbb34",
"./paises/etiopia/historia/": "cd57282fbf",
"./paises/etiopia/": "45055c8794",
"./paises/gabon/historia/": "e34e07e925",
"./paises/gabon/": "fde1a5461e",
"./paises/gambia/historia/": "fd715481d2",
"./paises/gambia/": "8f3b3b4403",
"./paises/ghana/historia/": "b4e3b119cc",
"./paises/ghana/": "a7280bfa16",
"./paises/guinea-bisau/historia/": "d9bc84d319",
"./paises/guinea-bisau/": "0d5472f995",
"./paises/guinea-ecuatorial/historia/": "8c982014b6",
"./paises/guinea-ecuatorial/": "98f120b322",
"./paises/guinea/historia/": "1fbb527303",
"./paises/guinea/": "6ed4181ed4",
"./paises/kenia/historia/": "baeaecffb0",
"./paises/kenia/": "705cdd53ba",
"./paises/lesoto/historia/": "12cb0f1496",
"./paises/lesoto/": "69d6dd3c0c",
"./paises/liberia/historia/": "0f480181df",
"./paises/liberia/": "2d263fb75d",
"./paises/libia/historia/": "fabe0bc647",
"./paises/libia/": "a1329ff592",
"./paises/madagascar/historia/": "087ff7c56a",
"./paises/madagascar/": "d50bd4bd4a",
"./paises/malaui/historia/": "6db6dbd72a",
"./paises/malaui/": "9a3bf9983f",
"./paises/mali/historia/": "97dd5b7981",
"./paises/mali/": "2969bd3e97",
"./paises/marruecos/historia/": "bd6f638b36",
"./paises/marruecos/": "f9fa17597e",
"./paises/mauricio/historia/": "c83a90b6be",
"./paises/mauricio/": "b69825cc00",
"./paises/mauritania/historia/": "e5f312fa30",
"./paises/mauritania/": "1774b39f60",
"./paises/mozambique/historia/": "813a2a82ac",
"./paises/mozambique/": "10bd9193f7",
"./paises/namibia/historia/": "dc7ac8828e",
"./paises/namibia/": "60f64c7338",
"./paises/niger/historia/": "add899440e",
"./paises/niger/": "e7cf905414",
"./paises/nigeria/historia/": "aaca51aa2e",
"./paises/nigeria/": "b2888a1e62",
"./paises/rca/historia/": "01e8d8efb0",
"./paises/rca/": "e0334b4469",
"./paises/rd-congo/historia/": "34de42c071",
"./paises/rd-congo/": "7158329885",
"./paises/ruanda/historia/": "bd0c83b3d9",
"./paises/ruanda/": "0b9ca4abed",
"./paises/sahara-occidental/historia/": "077bd496d7",
"./paises/sahara-occidental/": "0b999e2a99",
"./paises/santo-tome/historia/": "5dfc2c18a7",
"./paises/santo-tome/": "6b11e99e43",
"./paises/senegal/historia/": "5a6c97ee21",
"./paises/senegal/": "c6f3073312",
"./paises/seychelles/historia/": "1c55d5ae7c",
"./paises/seychelles/": "457a0db0f3",
"./paises/sierra-leona/historia/": "55c15fbef3",
"./paises/sierra-leona/": "6f52af25aa",
"./paises/somalia/historia/": "dce2bdc4f4",
"./paises/somalia/": "e63262d5d6",
"./paises/sudafrica/historia/": "a5b2245296",
"./paises/sudafrica/": "6bf320a56b",
"./paises/sudan-del-sur/historia/": "b564ddb663",
"./paises/sudan-del-sur/": "010a718798",
"./paises/sudan/historia/": "29135212eb",
"./paises/sudan/": "206a76582b",
"./paises/tanzania/historia/": "4984334ded",
"./paises/tanzania/": "e780f1c3f8",
"./paises/togo/historia/": "e96ac21d70",
"./paises/togo/": "f7f6e64b03",
"./paises/tunez/historia/": "aab9fa8ef6",
"./paises/tunez/": "7bc553edb6",
"./paises/uganda/historia/": "fb098892f0",
"./paises/uganda/": "e8851007e6",
"./paises/yibuti/historia/": "42c3241516",
"./paises/yibuti/": "011157c5e2",
"./paises/zambia/historia/": "3640a6ddd8",
"./paises/zambia/": "7c507c6ae3",
"./paises/zimbabue/historia/": "28e8b14f95",
"./paises/zimbabue/": "cfeb0eb951",
"./perro/": "941a950235",
"./planificador-puntos/": "144a1beac8",
"./planificador/": "9c7fd3fdc6",
"./presupuesto/": "f9a85a8169",
"./visados/": "f87773207a",
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
"./assets/js/planificador-puntos.js?v=fd3c7b31ba": "fd3c7b31ba",
"./assets/js/planificador-puntos.json": "681eec41c7",
"./assets/js/presupuesto-xlsx.js?v=6cb35d90f7": "6cb35d90f7",
"./assets/js/presupuesto.js?v=c6d76b3b86": "c6d76b3b86",
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

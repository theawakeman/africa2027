const VERSION = 'a27-20260927-2024';
const PRECACHE = {
"./cpd/": "09638ee451",
"./documentacion/": "520eaa9afc",
"./": "5f782dfd33",
"./mapa/": "1a7e1bae3e",
"./paises/angola/historia/": "ad0e5f3409",
"./paises/angola/": "9d5ec593cf",
"./paises/argelia/historia/": "66ca6bcad2",
"./paises/argelia/": "7cf397324d",
"./paises/benin/historia/": "d3bc5f8595",
"./paises/benin/": "42e56d501c",
"./paises/botsuana/historia/": "d40701dbd1",
"./paises/botsuana/": "84d009efa4",
"./paises/burkina-faso/historia/": "ce8277c215",
"./paises/burkina-faso/": "ce20bbb385",
"./paises/burundi/historia/": "2de1d52ae5",
"./paises/burundi/": "c216195737",
"./paises/cabo-verde/historia/": "9263abfffe",
"./paises/cabo-verde/": "a8714e2813",
"./paises/camerun/historia/": "0d9f5141b0",
"./paises/camerun/": "d5337fd409",
"./paises/chad/historia/": "b084794e2a",
"./paises/chad/": "3e8f8a4dbb",
"./paises/comoras/historia/": "36b28d46d3",
"./paises/comoras/": "7d0fad1e34",
"./paises/congo/historia/": "5ae570020e",
"./paises/congo/": "8759561d2d",
"./paises/costa-de-marfil/historia/": "bf79de56bd",
"./paises/costa-de-marfil/": "2e453d9e92",
"./paises/egipto/historia/": "20045e7e50",
"./paises/egipto/": "56aaf5c48f",
"./paises/eritrea/historia/": "fc790c27a3",
"./paises/eritrea/": "2a6b03a5bb",
"./paises/esuatini/historia/": "25f4f9587b",
"./paises/esuatini/": "64fa9bd2c9",
"./paises/etiopia/historia/": "20869b7910",
"./paises/etiopia/": "9e5e460180",
"./paises/gabon/historia/": "f2dfc76aba",
"./paises/gabon/": "5ba0d0b0fa",
"./paises/gambia/historia/": "b7b5b4f7eb",
"./paises/gambia/": "b176e468a5",
"./paises/ghana/historia/": "bb4181a39d",
"./paises/ghana/": "a00e6b81c1",
"./paises/guinea-bisau/historia/": "7bafe5ced3",
"./paises/guinea-bisau/": "972b5ba36e",
"./paises/guinea-ecuatorial/historia/": "0ec54ae86a",
"./paises/guinea-ecuatorial/": "4c8e697075",
"./paises/guinea/historia/": "0c24e52250",
"./paises/guinea/": "5265797c4f",
"./paises/kenia/historia/": "57813bfd6f",
"./paises/kenia/": "70266f65ba",
"./paises/lesoto/historia/": "a1b581d9ba",
"./paises/lesoto/": "69f84fbb33",
"./paises/liberia/historia/": "8b8ac1f58a",
"./paises/liberia/": "f0b5021bfe",
"./paises/libia/historia/": "94ce0aa391",
"./paises/libia/": "ecbc7cf5cd",
"./paises/madagascar/historia/": "7855be5e9d",
"./paises/madagascar/": "2c19bcdfb7",
"./paises/malaui/historia/": "ed6c7f1ea8",
"./paises/malaui/": "24ce01dffa",
"./paises/mali/historia/": "5daf6637e3",
"./paises/mali/": "c52e5045c1",
"./paises/marruecos/historia/": "38ca29b670",
"./paises/marruecos/": "205009a7b3",
"./paises/mauricio/historia/": "c17cedd5c6",
"./paises/mauricio/": "26b611a56c",
"./paises/mauritania/historia/": "2a0ad078af",
"./paises/mauritania/": "5bd74a3bec",
"./paises/mozambique/historia/": "096f8605fb",
"./paises/mozambique/": "50f6ea30b9",
"./paises/namibia/historia/": "d2f762db59",
"./paises/namibia/": "393a5c2ad5",
"./paises/niger/historia/": "32356a72e0",
"./paises/niger/": "d05963cc7d",
"./paises/nigeria/historia/": "c9a0488c6c",
"./paises/nigeria/": "3610a12bde",
"./paises/rca/historia/": "3cfe799d99",
"./paises/rca/": "8667b7e356",
"./paises/rd-congo/historia/": "c399d55ba1",
"./paises/rd-congo/": "0849995c07",
"./paises/ruanda/historia/": "378f0607d0",
"./paises/ruanda/": "b024e810e7",
"./paises/sahara-occidental/historia/": "991ab56038",
"./paises/sahara-occidental/": "3eb9634f6e",
"./paises/santo-tome/historia/": "911eb49763",
"./paises/santo-tome/": "13f271b338",
"./paises/senegal/historia/": "21a0810f69",
"./paises/senegal/": "4ab0092a79",
"./paises/seychelles/historia/": "03d8db62f0",
"./paises/seychelles/": "088ef8ce10",
"./paises/sierra-leona/historia/": "3f6123bf48",
"./paises/sierra-leona/": "494e0ee9ad",
"./paises/somalia/historia/": "67f9f9dfb9",
"./paises/somalia/": "ca93aa3ef1",
"./paises/sudafrica/historia/": "cb89a6dbfd",
"./paises/sudafrica/": "9e568dcaca",
"./paises/sudan-del-sur/historia/": "b423ed4f1a",
"./paises/sudan-del-sur/": "6486e6fd7d",
"./paises/sudan/historia/": "60173d025a",
"./paises/sudan/": "ec3338dfe5",
"./paises/tanzania/historia/": "967cf9ef69",
"./paises/tanzania/": "40a41e8a08",
"./paises/togo/historia/": "126a02d9fa",
"./paises/togo/": "39ca70da4c",
"./paises/tunez/historia/": "34eecb0a32",
"./paises/tunez/": "35ba5a27b2",
"./paises/uganda/historia/": "4269d8416f",
"./paises/uganda/": "d8c35544d7",
"./paises/yibuti/historia/": "ccf78c7f7e",
"./paises/yibuti/": "59f8e47262",
"./paises/zambia/historia/": "6145d3a345",
"./paises/zambia/": "e80d19aa46",
"./paises/zimbabue/historia/": "42cfbbefb2",
"./paises/zimbabue/": "1e0ae7cd94",
"./perro/": "140bded05b",
"./planificador-clasico/": "45808f05f3",
"./planificador-puntos/": "cd0f238d11",
"./planificador/": "d5ee6d99ff",
"./presupuesto/": "f505d943bd",
"./visados/": "a266ab20df",
"./assets/css/site.css?v=3cac24495c": "3cac24495c",
"./assets/icons/icon-192.png": "afb2518dd3",
"./assets/icons/icon-512.png": "195ee555af",
"./assets/icons/icon-maskable-512.png": "6c5d07d1cf",
"./assets/js/africa.geo.json": "c0b7c9f03c",
"./assets/js/cpdmap.js?v=cce81a6e10": "cce81a6e10",
"./assets/js/creador-pdi.js?v=569eeec2d5": "569eeec2d5",
"./assets/js/fotos-4x4.js?v=7d053de40f": "7d053de40f",
"./assets/js/map.js?v=29484ec2a4": "29484ec2a4",
"./assets/js/pdi-detalle.json": "fa7790481d",
"./assets/js/perromap.js?v=54b952ce88": "54b952ce88",
"./assets/js/planificador-puntos.js?v=4fb5a7358a": "4fb5a7358a",
"./assets/js/planificador-puntos.json": "be9516f90a",
"./assets/js/presupuesto-xlsx.js?v=6cb35d90f7": "6cb35d90f7",
"./assets/js/presupuesto.js?v=5ae41123c1": "5ae41123c1",
"./assets/js/viaje.js?v=14612cf4a2": "14612cf4a2",
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

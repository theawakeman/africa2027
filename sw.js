const VERSION = 'a27-20260908-2128';
const PRECACHE = ["./", "./index.html", "./senegal/", "./senegal/index.html", "./manifest.webmanifest", "./assets/icons/icon-192.png", "./assets/icons/icon-512.png", "./assets/icons/icon-maskable-512.png", "./assets/img/senegal/route.png", "./assets/img/senegal/01.jpg", "./assets/img/senegal/02.jpg", "./assets/img/senegal/03.jpg", "./assets/img/senegal/04.jpg", "./assets/img/senegal/05.jpg", "./assets/img/senegal/06.jpg", "./assets/img/senegal/07.jpg", "./assets/img/senegal/08.jpg", "./assets/img/senegal/09.jpg", "./assets/img/senegal/10.jpg", "./assets/img/senegal/11.jpg", "./assets/img/senegal/12.jpg", "./assets/img/senegal/13.jpg", "./assets/img/senegal/14.jpg", "./assets/img/senegal/15.jpg", "./assets/img/senegal/16.jpg", "./assets/img/senegal/17.jpg", "./assets/img/senegal/18.jpg", "./assets/img/senegal/19.jpg", "./assets/img/senegal/20.jpg", "./assets/img/senegal/21.jpg", "./assets/img/senegal/22.jpg", "./assets/img/senegal/23.jpg"];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(PRECACHE)));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('message', e => { if (e.data === 'skip') self.skipWaiting(); });
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (req.mode === 'navigate' || (url.origin === location.origin && url.pathname.endsWith('.html'))) {
    e.respondWith(fetch(req).then(res => { const copy = res.clone(); caches.open(VERSION).then(c => c.put(req, copy)); return res; }).catch(() => caches.match(req, {ignoreSearch:true}).then(m => m || caches.match('./index.html'))));
    return;
  }
  e.respondWith(caches.match(req, {ignoreSearch:true}).then(m => m || fetch(req).then(res => {
    if (res.ok && (url.origin === location.origin || url.origin.includes('gstatic') || url.origin.includes('googleapis'))) {
      const copy = res.clone(); caches.open(VERSION).then(c => c.put(req, copy));
    }
    return res;
  })));
});

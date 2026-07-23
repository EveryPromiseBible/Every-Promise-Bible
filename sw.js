/* Every Promise -- service worker.
 *
 * Two jobs: make the site installable, and make it work with no connection.
 *
 * The hard part is that those two goals fight each other. A cache that never
 * expires gives perfect offline and freezes the corpus forever -- add a promise,
 * and nobody who has already visited ever sees it. A cache that always
 * revalidates keeps updates instant and re-downloads 2.5 MB gzipped on a bad
 * connection. So the two kinds of file are handled differently, along the same
 * line _headers already draws:
 *
 *   index.html   small, changes often   -> network first, cache as fallback
 *   data/*.js    huge, changes rarely   -> cache first, refresh in background
 *
 * The practical effect: the page itself is always current when online, and a
 * newly added promise lands on the reader's NEXT visit rather than this one.
 * That one-visit lag is the price of the corpus loading instantly and working
 * on a plane. It is the right trade for this site, but it is a real trade and
 * worth knowing about before wondering why an edit "did not show up."
 *
 * Bump CACHE_VERSION to evict every cached file at once. You do not need to do
 * this for ordinary content edits -- the strategies above already pick those
 * up. Bump it when the shell changes in a way that must not be served stale,
 * or when you want a clean slate.
 */

const CACHE_VERSION = 'every-promise-v1';

/* The shell only. data/*.js is deliberately NOT precached: those files total
 * ~15 MB raw (Thayer's alone is ~5 MB), and precaching them would make the very
 * first visit slower than it is today. index.html loads most via <script src>,
 * and Thayer's is fetched on first word tap; either way they land in the cache
 * through the runtime path below -- same download, just not duplicated up front. */
const SHELL = [
  '/',
  '/index.html',
  '/manifest.json',
  '/fonts/fonts.css',
  '/icons/icon-192.png',
  '/icons/icon-512.png',
  '/icons/icon-maskable-512.png',
  '/icons/apple-touch-icon.png',
  '/icons/favicon-32.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_VERSION)
      /* addAll is atomic -- one 404 fails the whole install and leaves the old
       * worker in place. Add individually so a single missing icon cannot
       * block the install outright. */
      .then(cache => Promise.all(
        SHELL.map(url => cache.add(url).catch(() => {
          console.warn('[sw] could not precache', url);
        }))
      ))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== CACHE_VERSION).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const req = event.request;

  /* Only GET, only this origin. POSTs are not cacheable, and third-party
   * requests are left alone so the worker can never break something it does
   * not own. */
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  /* Navigations: network first. The reader gets the current page whenever
   * they have a connection, and the cached copy only when they do not. */
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req)
        .then(res => {
          const copy = res.clone();
          caches.open(CACHE_VERSION).then(c => c.put(req, copy));
          return res;
        })
        .catch(() =>
          caches.match(req).then(hit => hit || caches.match('/index.html'))
        )
    );
    return;
  }

  /* Everything else -- data/*.js, icons, fonts: stale while revalidate.
   * Serve the cached copy immediately if there is one, and fetch a fresh copy
   * in the background for next time. This is what makes the corpus feel
   * instant after the first visit. */
  event.respondWith(
    caches.match(req).then(hit => {
      const network = fetch(req)
        .then(res => {
          if (res && res.status === 200) {
            const copy = res.clone();
            caches.open(CACHE_VERSION).then(c => c.put(req, copy));
          }
          return res;
        })
        .catch(() => hit);

      return hit || network;
    })
  );
});

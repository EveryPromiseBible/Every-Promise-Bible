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
 * The lag used to be silent, which made it indistinguishable from a deploy
 * that had not landed: the only way to tell was to clear the cache by hand.
 * So the background refresh now compares what it fetched against what it had
 * -- ETag first, then Last-Modified, then length -- and when the corpus has
 * genuinely changed it posts a message to the open pages. index.html turns
 * that into a small "new content -- reload" prompt. The reader still gets the
 * instant cached copy; they are simply told that a fresher one is ready,
 * instead of having to guess.
 *
 * Only /data/ triggers that message. An icon or a font quietly updating is
 * not worth interrupting anyone for.
 *
 * Bump CACHE_VERSION to evict every cached file at once. You do not need to do
 * this for ordinary content edits -- the strategies above already pick those
 * up. Bump it when the shell changes in a way that must not be served stale,
 * or when you want a clean slate.
 */

const CACHE_VERSION = 'every-promise-v7';

/* Cheapest reliable "is this a different file?" signal the host gives us.
 * GitHub Pages sends a strong ETag, so that is the usual answer; the other two
 * are fallbacks for hosts that do not. An empty stamp on either side means we
 * cannot tell, and we say nothing rather than nagging on every request. */
function stampOf(res) {
  return (res && (res.headers.get('etag') ||
                  res.headers.get('last-modified') ||
                  res.headers.get('content-length'))) || '';
}

function contentChanged(cached, fresh) {
  const a = stampOf(cached), b = stampOf(fresh);
  return !!a && !!b && a !== b;
}

function announceUpdate(url) {
  self.clients.matchAll({ includeUncontrolled: true })
    .then(cs => cs.forEach(c => c.postMessage({ type: 'content-updated', url })));
}

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
            /* Compare before overwriting: once the fresh copy is in the cache
             * the old stamp is gone and there is nothing left to compare. Only
             * worth announcing when there WAS a cached copy -- on a first visit
             * the reader is already getting the current file. */
            const changed = hit && url.pathname.startsWith('/data/') &&
                            contentChanged(hit, res);
            const copy = res.clone();
            return caches.open(CACHE_VERSION)
              .then(c => c.put(req, copy))
              .then(() => { if (changed) announceUpdate(url.pathname); })
              .then(() => res);
          }
          return res;
        })
        .catch(() => hit);

      /* The whole point of "revalidate" is the half that happens after the
       * reader already has their answer -- and that half only runs if the
       * worker is still alive to run it. Returning the cached hit ends the
       * fetch event, and without waitUntil the browser is free to shut the
       * worker down immediately, cancelling the refresh mid-flight. The cache
       * then never updates and the corpus is frozen at whatever was first
       * downloaded. Holding the event open until the refresh settles is what
       * makes "lands on the next visit" actually true. */
      event.waitUntil(network.catch(() => {}));

      return hit || network;
    })
  );
});

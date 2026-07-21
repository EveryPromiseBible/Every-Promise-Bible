# Deploying Every Promise

The site is static: `index.html` plus four data files. No server code, no build
framework, no database.

```
index.html         53 KB    all the code
data/chapters.js  5.41 MB   the New Testament
data/abbott.js    2.46 MB   Abbott-Smith lexicon
data/lexicon.js   1.24 MB   Strong's / Thayer's
data/promises.js  0.72 MB   the 1,005 promises
_headers                    cache rules (Netlify / Cloudflare Pages)
```

Everything else in this repo — `tools/`, `HANDOFF.md`, `CHANGELOG.md`, the plan
files — is **working material and must not be published.** The build command
below copies only the site into `dist/`, so connecting the repo to a host does
not expose the rest.

---

## Local preview

Do not just double-click `index.html`. The data now loads via `<script src>`
from a subdirectory, and some browsers block that on `file://`. Run a server:

```
python -m http.server 8000
```

Then open <http://localhost:8000>. Any static server works.

---

## Publishing (Cloudflare Pages or Netlify)

Both are free, both give a custom domain with an automatic SSL certificate, and
both redeploy on `git push`.

**1. Put the repo on GitHub.** It can be private; the hosts read it either way.

```
git remote add origin https://github.com/<you>/every-promise.git
git branch -M main
git push -u origin main
```

**2. Create the site**, pointing it at that repo, with:

| Setting | Value |
|---|---|
| Build command | `mkdir -p dist && cp index.html _headers dist/ && cp -r data dist/` |
| Output / publish directory | `dist` |

That is the whole configuration. There is no framework to select.

**3. Add the domain.** In the host's dashboard, add your custom domain and
follow its DNS instructions. If you buy the domain through Cloudflare the DNS is
already pointed correctly.

**4. Updating from then on** is `git push`. The site rebuilds automatically.

---

## Notes

- **First load is about 2.4 MB gzipped.** The hosts compress automatically, so
  visitors do not download the raw 9.8 MB. It caches after the first visit.
- **Google Fonts is the only external call.** Offline or blocked, the page still
  works and falls back to system fonts.
- **`_headers` is Netlify/Cloudflare syntax.** On a different host (S3, nginx)
  set the same rules that way instead, or drop the file — the site works without
  it, updates just may take longer to reach returning readers.
- **`data/*.js` must keep LF line endings and stay one line each.** `.gitattributes`
  enforces this. They are written by `tools/epcore.py`; never hand-edit them.
- **After any change to the Greek, run `python tools/wordcounts.py --write`.**
  The introduction above Matthew 1 publishes the per-book Greek counts beside
  SBLGNT's as proof that nothing was added or removed, so that table must be
  regenerated rather than left stale. It refuses to write if a book stops
  matching.

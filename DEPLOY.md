# Deploying Every Promise

The site is static: `index.html` plus four data files. No server code, no build
framework, no database.

```
index.html          64 KB   all the code
data/chapters.js   5.41 MB  the New Testament
data/abbott.js     2.46 MB  Abbott-Smith lexicon
data/lexicon.js    1.24 MB  Strong's / Thayer's
data/promises.js   1.13 MB  the 1,522 promises
data/wordcounts.js   1 KB   generated proof table (loaded by index.html)
_headers                    cache rules (Netlify / Cloudflare Pages)
```

Everything else in this repo — `tools/`, `HANDOFF.md`, `CHANGELOG.md`,
`PROJECT.md`, `TODO.md`, `CLAUDE.md`, the plan files — is **working material and
must not be published.** The `dist/` build command below copies only the site,
so a host that runs it does not expose the rest.

> Note: the live site serves the repo root rather than this `dist/` build, so
> those files are reachable on the domain too. See "What is actually live".

---

## What is actually live

The site is on **GitHub Pages**, serving the repository root, with `CNAME`
pointing at `everypromisebible.com`. Updating means uploading the changed files
to GitHub; Pages redeploys on its own.

Because Pages serves the root, the whole repo is reachable on the domain, not
just the site — `/CHANGELOG.md`, `/TODO.md`, `/tools/*.py` and so on all return
200. Nothing secret is exposed (no keys, no personal data, and the large KJV and
MorphGNT sources are gitignored), and the repo is public on GitHub anyway, so
these files are readable there regardless. Noted here as a fact of the setup,
not a problem to fix.

`https://everypromisebible.com` does not yet have a certificate — GitHub serves
a `*.github.io` cert, so `https://` shows a browser warning while `http://`
works normally. DNS is correct; the certificate is pending on GitHub's side.

---

## Local preview

Do not just double-click `index.html`. The data now loads via `<script src>`
from a subdirectory, and some browsers block that on `file://`. Run a server:

```
python -m http.server 8000
```

Then open <http://localhost:8000>. Any static server works.

---

## Alternative host — Cloudflare Pages or Netlify

The site is currently on GitHub Pages (above). This section is kept as an
option: these hosts run a build, so only `dist/` is published, and they issue
the SSL certificate automatically.

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

- **First load is about 2.5 MB gzipped** (measured: 10.31 MB raw → 2.46 MB
  gzipped; chapters.js is 1.14 MB of that). The hosts compress automatically, so
  visitors do not download the raw 10.3 MB. It caches after the first visit.
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

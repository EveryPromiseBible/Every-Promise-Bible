# -*- coding: utf-8 -*-
"""Build a standalone, public-domain 'Thayer's Greek-English Lexicon' repo
from the same decoded text that feeds the website.

Output folder (ready to upload to GitHub):
  README.md            -- what it is, stats, source, licence
  LICENSE              -- public-domain dedication (the 1889 text is PD)
  thayers.html         -- one self-contained page, browser-searchable
  book/NN-<range>.md   -- every entry in Strong's-number order, split so each
                          markdown file stays comfortably renderable on GitHub
  book/README.md       -- contents / index
"""
import io, os, re, sys, json, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_thayer import load_all
sys.stdout.reconfigure(encoding="utf-8")

SITE = r"C:\Users\benny\OneDrive\Desktop\Every Promise Website\Every-Promise-Bible"
OUT  = r"C:\Users\benny\OneDrive\Desktop\Every-Promise-Thayers"

def lb(p):
    t = io.open(p, encoding="utf-8").read(); j = t.index("{", t.index("=")); return json.loads(t[j:].rstrip().rstrip(";"))
LEX = lb(os.path.join(SITE, "data", "lexicon.js"))
TH  = load_all()

def num(n): return int(n[1:])
keys = sorted(TH, key=num)
print("entries:", len(keys))

def greek(n):
    g = (LEX.get(n) or {}).get("greek")
    if g: return g
    # fall back to the lemma at the head of the Thayer entry
    lead = TH[n].split("\n", 1)[0]
    return re.split(r"[,;( ]", lead.strip(), 1)[0]
def translit(n): return (LEX.get(n) or {}).get("translit", "")

os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.join(OUT, "book"), exist_ok=True)

# ---------- LICENSE (public domain) ----------
license_txt = """Thayer's Greek-English Lexicon of the New Testament
Joseph Henry Thayer (1828-1901), English edition first published 1886;
corrected edition 1889. Coded to Strong's Concordance numbers (Strong's, 1890).

PUBLIC DOMAIN

The underlying lexicon and the Strong's numbering are both well over a century
old and are in the public domain worldwide. This edition is a faithful digital
reproduction of that public-domain text.

To the extent that any rights subsist in the compilation, formatting, or
markup added in producing this edition, they are dedicated to the public
domain under the Creative Commons CC0 1.0 Universal Public Domain Dedication
(https://creativecommons.org/publicdomain/zero/1.0/).

You may copy, modify, distribute, and use this work, including for commercial
purposes, without asking permission.

No warranty is given. The text was decoded from a community digitization and,
like every edition of a 19th-century lexicon, may contain transcription
artifacts; it is offered as-is.
"""
io.open(os.path.join(OUT, "LICENSE"), "w", encoding="utf-8", newline="\n").write(license_txt)

# ---------- README ----------
tot = sum(len(v) for v in TH.values())
readme = """# Thayer's Greek-English Lexicon of the New Testament

The complete text of **Joseph Henry Thayer's Greek-English Lexicon of the New
Testament** (corrected edition, 1889), keyed to **Strong's Concordance
numbers** — as open, plain-text data anyone can read, search, and reuse.

> **G26 — ἀγάπη — agape**
> ἀγάπη, ῆς, ἡ ... 1. affection, good-will, love, benevolence ... 2. plural,
> love-feasts ...

Thayer's is one of the great New Testament lexicons: for each Greek word it
gives the forms, the etymology, the range of meaning, and the passages where
each sense is used. This repository carries **%(n)d entries** in all.

## Read it

- **[Browse the lexicon](book/)** — every entry in Strong's-number order,
  split into files.
- **thayers.html** — the whole lexicon on one page; open it in any browser and
  use Ctrl+F / Cmd+F, or the built-in search box, to jump to a word, a meaning,
  or a Strong's number.

## What is here

- **%(n)d entries**, G1 through G%(hi)d, each with its Greek headword, a
  transliteration, its Strong's number, and Thayer's full definition.
- The Greek is real Unicode (polytonic), so it copies and searches correctly.
  Hebrew words Thayer cites are included where they appear.
- Scripture references are rendered in plain form (e.g. `Mat 20:8`).

## Source and licence

The lexicon (Thayer, 1889) and the Strong's numbering (Strong, 1890) are both
in the **public domain**. This edition was decoded from a community
digitization of that public-domain text into clean Unicode. It is offered in
the public domain (CC0); see [LICENSE](LICENSE). Use it freely, including
commercially.

Because it derives from a 19th-century lexicon digitized by hand, occasional
transcription artifacts survive from the source; the text is offered as-is.

Part of the [Every Promise](https://everypromisebible.com) project.
""" % {"n": len(keys), "hi": num(keys[-1])}
io.open(os.path.join(OUT, "README.md"), "w", encoding="utf-8", newline="\n").write(readme)

# ---------- split markdown (size-based, since entries vary from 14 to 34k chars) ----------
LIMIT = 190_000   # chars of body per file; keeps GitHub markdown rendering happy
chunks, cur, size = [], [], 0
for n in keys:
    body = TH[n]
    if cur and size + len(body) > LIMIT:
        chunks.append(cur); cur, size = [], 0
    cur.append(n); size += len(body) + 80
if cur: chunks.append(cur)

toc = []
for pi, chunk in enumerate(chunks, 1):
    lo, hi = chunk[0], chunk[-1]
    fname = "%02d-%s-%s.md" % (pi, lo, hi)
    toc.append((fname, lo, hi, len(chunk)))
    L = ["# Thayer's Lexicon — %s to %s\n" % (lo, hi),
         "[← back to contents](README.md) · [project readme](../README.md)\n", "---\n"]
    for n in chunk:
        tr = translit(n)
        L.append("### %s%s" % (greek(n), (" — %s" % tr) if tr else ""))
        L.append("`Strong's %s`\n" % n)
        for para in TH[n].split("\n"):
            if para.strip():
                L.append(para + "\n")
        L.append("---\n")
    io.open(os.path.join(OUT, "book", fname), "w", encoding="utf-8", newline="\n").write("\n".join(L))

idx = ["# Thayer's Greek-English Lexicon — contents\n",
       "%d entries, in Strong's-number order.\n" % len(keys), ""]
for fname, lo, hi, ct in toc:
    idx.append("- [%s – %s](%s) (%d)" % (lo, hi, fname, ct))
idx.append("\n[← project readme](../README.md)")
io.open(os.path.join(OUT, "book", "README.md"), "w", encoding="utf-8", newline="\n").write("\n".join(idx))

# ---------- single-file searchable HTML ----------
rows = []
for n in keys:
    gk, tr = greek(n), translit(n)
    paras = "".join("<p>%s</p>" % html.escape(p) for p in TH[n].split("\n") if p.strip())
    rows.append(
        '<article class="e" data-s="%s %s %s">'
        '<div class="gk">%s <span class="tr">%s</span><span class="sn">%s</span></div>'
        '%s</article>'
        % (html.escape(gk), html.escape(tr.lower()), n.lower(),
           html.escape(gk), html.escape(tr), n, paras))
htmldoc = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Thayer's Greek-English Lexicon</title>
<style>
:root{--ink:#141310;--gray:#8a857c;--line:#e8e4da;--accent:#7C5CE0;}
*{box-sizing:border-box}
body{margin:0;font-family:Georgia,'Gentium Plus',serif;color:var(--ink);background:#fff;line-height:1.6}
header{padding:38px 20px 16px;max-width:820px;margin:0 auto;text-align:center}
h1{font-size:1.7em;margin:0 0 6px}
.sub{color:var(--gray);font-size:0.95em;font-family:system-ui,sans-serif}
.searchwrap{position:sticky;top:0;background:#fff;border-bottom:1px solid var(--line);padding:14px 20px;z-index:5}
.searchwrap input{display:block;max-width:780px;margin:0 auto;width:100%;padding:12px 16px;font-size:1em;
  border:1.5px solid var(--line);border-radius:10px;font-family:system-ui,sans-serif}
main{max-width:820px;margin:0 auto;padding:10px 20px 90px}
.count{color:var(--gray);font-size:0.8em;text-align:center;padding:10px 0 20px;font-family:system-ui,sans-serif}
.e{padding:22px 0;border-bottom:1px solid var(--line)}
.gk{font-size:1.5em;font-weight:600;margin-bottom:8px}
.gk .tr{font-size:0.62em;color:var(--gray);font-style:italic;font-weight:400;margin-left:8px}
.gk .sn{font-family:ui-monospace,monospace;font-size:0.5em;color:#fff;background:var(--accent);
  border-radius:999px;padding:3px 9px;margin-left:10px;vertical-align:middle;font-weight:700}
.e p{margin:0 0 9px;font-size:0.98em}
@media(prefers-color-scheme:dark){
  body{background:#141310;color:#ece7dd}.searchwrap,header{background:#141310}
  :root{--line:#2c2a25}.searchwrap input{background:#1e1c18;color:#ece7dd}
}
</style></head><body>
<header><h1>Thayer's Greek-English Lexicon</h1>
<div class="sub">Joseph Henry Thayer, 1889 &middot; __N__ entries, keyed to Strong's numbers &middot; public domain</div></header>
<div class="searchwrap"><input id="q" type="search" placeholder="Search a Greek word, meaning, or Strong's number…" autocomplete="off"></div>
<main><div class="count" id="count"></div>__ROWS__</main>
<script>
var arts=[].slice.call(document.querySelectorAll('.e')),c=document.getElementById('count');
function upd(){var q=document.getElementById('q').value.toLowerCase().trim(),shown=0;
 arts.forEach(function(a){var m=!q||a.getAttribute('data-s').indexOf(q)>-1||a.textContent.toLowerCase().indexOf(q)>-1;
 a.style.display=m?'':'none';if(m)shown++;});
 c.textContent=shown+' of '+arts.length+' entries';}
document.getElementById('q').addEventListener('input',upd);upd();
</script></body></html>"""
htmldoc = htmldoc.replace("__N__", str(len(keys))).replace("__ROWS__", "".join(rows))
io.open(os.path.join(OUT, "thayers.html"), "w", encoding="utf-8", newline="\n").write(htmldoc)

print("\nwrote to", OUT)
for f in sorted(os.listdir(OUT)):
    p = os.path.join(OUT, f)
    if os.path.isdir(p):
        print("  %s/  (%d files)" % (f, len(os.listdir(p))))
    else:
        print("  %s  (%.0f KB)" % (f, os.path.getsize(p)/1024))
print("total lexicon text: %.2f MB across %d markdown files" % (tot/1024/1024, len(chunks)))

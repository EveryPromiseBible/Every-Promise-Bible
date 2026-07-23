# -*- coding: utf-8 -*-
"""Build data/thayer.js for the Every Promise site from the e-Sword
'Thayers Unabridged.dctx' SQLite module.

Decodes each RTF fragment to clean Unicode (Greek cp1253, Hebrew cp1255,
polytonic accents via \\uNNNN), keys by Strong's G-number, writes a one-line
LF blob  window.THAYER={...};  matching the other data/*.js files.
"""
import sqlite3, re, io, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thayer_parse import decode_rtf, clean_refs
sys.stdout.reconfigure(encoding="utf-8")

DCTX = r"C:\Users\benny\OneDrive\Desktop\Lexicons\Thayers Unabridged.dctx"
SITE = r"C:\Users\benny\OneDrive\Desktop\Every Promise Website\Every-Promise-Bible"

def finalize(txt):
    txt = clean_refs(txt)
    txt = re.sub(r"\(\s*\)", "", txt)          # drop empty parens left by unlinkable refs
    txt = re.sub(r"[ \t]{2,}", " ", txt)
    txt = re.sub(r"\s+([;,.])", r"\1", txt)    # no space before punctuation
    txt = re.sub(r"[ \t]*\n[ \t]*", "\n", txt)
    txt = re.sub(r"\n{2,}", "\n", txt)         # senses already on own lines; single breaks
    return txt.strip()

def load_all():
    cur = sqlite3.connect(DCTX).cursor()
    data = {}
    for topic, defn in cur.execute("SELECT Topic,Definition FROM Dictionary"):
        key = (topic or "").strip()
        if not re.fullmatch(r"G\d+", key):
            continue
        data[key] = finalize(decode_rtf(defn or ""))
    return data

if __name__ == "__main__":
    data = load_all()
    # sort by numeric Strong's for a stable, diff-friendly blob
    ordered = {k: data[k] for k in sorted(data, key=lambda x: int(x[1:]))}
    blob = "window.THAYER=" + json.dumps(ordered, ensure_ascii=False, separators=(",", ":")) + ";"
    out = os.path.join(SITE, "data", "thayer.js")
    io.open(out, "w", encoding="utf-8", newline="\n").write(blob)
    print("entries:", len(ordered))
    print("wrote:", out, " size:", round(os.path.getsize(out)/1024/1024, 2), "MB")
    print("lines:", blob.count("\n") + 1, "(must be 1)")
    # sanity: a couple of spot values
    for g in ("G26", "G2316", "G5547"):
        print(g, "->", ordered[g][:70].replace("\n", " ⏎ "))

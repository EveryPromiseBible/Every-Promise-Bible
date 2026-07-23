# -*- coding: utf-8 -*-
"""Decode e-Sword 'Thayer's Unabridged' .dctx RTF fragments into clean Unicode.

Each Dictionary.Definition is an RTF *fragment* (no \\rtf1 header, no fonttbl).
e-Sword's fixed convention for these modules:
  \\f0 -> Latin  (cp1252)
  \\f1 -> Greek  (cp1253)   <- verified: \\'e3\\'dc\\'f0\\'e7 = γάπη
  \\f2 -> Hebrew (cp1255)   <- verified: \\'e0\\'c7\\'e4... = אַה...
Greek polytonic accents come as \\uNNNN? (decimal, signed 16-bit) Unicode escapes.
Scripture links look like  \\cf11\\ul Mat_20:8\\cf0\\ulnone  -> keep "Mat 20:8".
"""
import sqlite3, re, sys
sys.stdout.reconfigure(encoding="utf-8")

FONT_CP = {0: "cp1252", 1: "cp1253", 2: "cp1255"}

def decode_rtf(s):
    out = []
    i, n = 0, len(s)
    # state stack of (font, uc)
    font = 0
    uc = 1
    stack = []
    def emit_byte(b, f):
        try:
            out.append(bytes([b]).decode(FONT_CP.get(f, "cp1252")))
        except Exception:
            pass
    while i < n:
        ch = s[i]
        if ch == "{":
            stack.append((font, uc)); i += 1; continue
        if ch == "}":
            if stack: font, uc = stack.pop()
            i += 1; continue
        if ch == "\\":
            # control
            if i + 1 >= n: break
            c2 = s[i+1]
            if c2 == "'":
                # hex byte
                hx = s[i+2:i+4]
                try: emit_byte(int(hx, 16), font)
                except Exception: pass
                i += 4; continue
            if not c2.isalpha():
                # control symbol
                mapping = {"\\":"\\", "{":"{", "}":"}", "~":" ",
                           "-":"", "_":"‑", "*":""}
                if c2 == "\n": out.append("\n")
                elif c2 in mapping: out.append(mapping[c2])
                i += 2; continue
            # control word: letters then optional signed number
            m = re.match(r"[a-zA-Z]+", s[i+1:])
            word = m.group(0)
            j = i + 1 + len(word)
            num = None
            mn = re.match(r"-?\d+", s[j:])
            if mn:
                num = int(mn.group(0)); j += len(mn.group(0))
            # a single trailing space is a delimiter and consumed
            if j < n and s[j] == " ": j += 1
            # handle
            if word == "u":
                cp = num if num is not None else 0
                if cp < 0: cp += 65536
                try: out.append(chr(cp))
                except Exception: pass
                # skip uc fallback chars
                skipped = 0
                while skipped < uc and j < n:
                    if s[j] == "\\" and j+1 < n and s[j+1] == "'":
                        j += 4; skipped += 1
                    elif s[j] == "\\":
                        # skip a control word as one
                        mm = re.match(r"[a-zA-Z]+-?\d* ?", s[j+1:])
                        j += 1 + (len(mm.group(0)) if mm else 1); skipped += 1
                    else:
                        j += 1; skipped += 1
                i = j; continue
            if word == "uc":
                uc = num if num is not None else 1; i = j; continue
            if word == "f":
                font = num if num is not None else 0; i = j; continue
            if word in ("par", "line"):
                out.append("\n"); i = j; continue
            if word in ("tab",):
                out.append("\t"); i = j; continue
            if word == "emdash": out.append("—"); i = j; continue
            if word == "endash": out.append("–"); i = j; continue
            if word in ("ldblquote","rdblquote"): out.append('"'); i = j; continue
            if word in ("lquote","rquote"): out.append("'"); i = j; continue
            if word == "bullet": out.append("•"); i = j; continue
            # everything else: formatting control, drop
            i = j; continue
        # literal
        if ch in ("\r","\n"):
            i += 1; continue
        out.append(ch); i += 1
    return "".join(out)

# scripture link refs: "Mat_20:8" -> "Mat 20:8"
def clean_refs(t):
    t = re.sub(r"([1-3]?[A-Za-z]{2,4})_(\d+:\d+(?:-\d+)?)", r"\1 \2", t)
    # collapse whitespace
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r" *\n *", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

if __name__ == "__main__":
    db = r"C:\Users\benny\OneDrive\Desktop\Lexicons\Thayers Unabridged.dctx"
    c = sqlite3.connect(db); cur = c.cursor()
    for tgt in ("G26","G2962","G5547","G2316","G3056"):
        row = cur.execute("SELECT Definition FROM Dictionary WHERE TRIM(Topic)=?", (tgt,)).fetchone()
        print("="*30, tgt, "="*30)
        if row:
            print(clean_refs(decode_rtf(row[0]))[:1200])
        print()

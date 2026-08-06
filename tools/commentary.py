#!/usr/bin/env python3
"""The Grace Commentary -- source of truth, builder, and checks.

    python tools/commentary.py export     # data/commentary.js  -> _commentary/*.md  (once)
    python tools/commentary.py build      # _commentary/*.md    -> data/commentary.js
    python tools/commentary.py validate   # every key lands on a real verse block
    python tools/commentary.py resolve "Galatians 5:4"
    python tools/commentary.py ledger     # what has been studied, and what recurs

WHY A TOOL AND NOT HAND-EDITING
-------------------------------
A note is keyed to the verse label the reader sees, and the Illumination labels
verses in BLOCKS -- "Galatians 5:2-4", not "Galatians 5:4". A key that matches no
block does not error. It renders nothing at all: no bulb, no note, no warning.
At four notes that is noticeable. At four hundred it is invisible, so `resolve`
does the mapping and `validate` fails the build rather than shipping a note
nobody can reach.

The dash in a label is an EN DASH (U+2013). A hyphen looks identical in most
editors and matches nothing. resolve() emits the real label; validate() calls out
a hyphen where an en dash belongs rather than just saying "not found".

LICENCE -- READ BEFORE ADDING A NOTE
------------------------------------
The Grace Commentary is written under a permission from Joseph Prince Ministries
granted 6 August 2026 (sources/permissioned/LICENCES-jpm.md in the working repo).
Its terms are narrow and binding:

  * Draw on the SUBSTANCE of the publicly available sermon notes as study.
  * Quote NOTHING -- not a sentence, not a phrase, not a distinctive turn of
    wording. Every note is written fresh from the Greek and public-domain sources.
  * data/commentary.js is NOT CC BY-SA like the rest of data/. It is all rights
    reserved, used by permission, non-commercial only. The builder writes that
    header into the generated file so a rebuild can never quietly drop it.

The ledger records which sermon informed which note -- a URL, a date and a list
of references. It never stores their text, because storing it would be keeping a
copy of the thing the permission does not grant.
"""

import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, '_commentary')
OUT = os.path.join(ROOT, 'data', 'commentary.js')
ILLUM = os.path.join(ROOT, 'data', 'illumination.js')
LEDGER = os.path.join(SRC, 'ledger.json')

EN = '–'

HEADER = """/* The Grace Commentary -- verse commentary for the Illumination Translation.
 *
 * GENERATED from _commentary/*.md by tools/commentary.py. Do not hand-edit:
 * edit the markdown and rebuild, or the published commentary and its sources
 * drift apart.
 *
 * LICENCE -- THIS FILE IS NOT CC BY-SA, UNLIKE THE REST OF data/.
 *
 *   All rights reserved. Used by permission of Joseph Prince Ministries for
 *   non-commercial use only.
 *
 * The Grace Commentary was developed with study of publicly available sermon
 * notes from Joseph Prince Ministries. Every note is original writing: none of
 * their wording is quoted or reproduced. The permission is recorded in full at
 * sources/permissioned/LICENCES-jpm.md and is limited to the free,
 * non-commercial Every Promise app and website. Any other use -- commercial,
 * print, or redistribution under an open licence -- needs a fresh permission
 * from info@josephprince.org.
 *
 * Keyed "Book C:V" to match the verse label the reader sees; the Illumination
 * labels verses in blocks, so a key is usually a range with an EN DASH.
 * Blocks: h heading, p paragraph, ul bullets, note a set-apart caution.
 */
"""


# ---------------------------------------------------------------- corpus ----

def load_blob(path, const):
    s = io.open(path, encoding='utf-8').read()
    i = s.index(const)
    return json.loads(s[i + len(const):].strip().rstrip(';'))


def verse_labels():
    """Every label a reader can actually see: {"Galatians 5:2-4": True, ...}"""
    out = {}
    for ch in load_blob(ILLUM, 'const ILLUMINATION ='):
        book = ch['ref'].rsplit(' ', 1)[0]
        for sec in ch['sections']:
            for vref, _text in sec['verses']:
                out[book + ' ' + vref] = ch['ref']
    return out


def resolve(ref):
    """"Galatians 5:4" -> "Galatians 5:2-4" (the block that contains it).

    Returns (key, note). note explains a miss rather than leaving the caller to
    guess, because "no match" almost always means the verse is real but the
    block is labelled differently."""
    ref = ref.strip().replace('-', EN)
    labels = verse_labels()
    if ref in labels:
        return ref, 'exact label'

    m = re.match(r'^(.*?)\s+(\d+):(\d+)', ref)
    if not m:
        return None, 'could not read a book, chapter and verse out of that'
    book, chap, verse = m.group(1), int(m.group(2)), int(m.group(3))

    for label in labels:
        lm = re.match(r'^(.*?)\s+(\d+):(\d+)(?:' + EN + r'(\d+)[a-z]?)?$', label)
        if not lm:
            continue
        if lm.group(1) != book or int(lm.group(2)) != chap:
            continue
        lo = int(lm.group(3))
        hi = int(lm.group(4)) if lm.group(4) else lo
        if lo <= verse <= hi:
            return label, 'verse %d falls inside the block %s' % (verse, label)
    return None, 'no block in %s %d contains verse %d' % (book, chap, verse)


# ------------------------------------------------------- markdown <-> json --

def parse_note(text):
    """Front matter, then blocks. '## ' heading, '> ' note, '- ' bullets, else
    paragraph. Blank lines separate blocks."""
    fm, body = {}, text
    if text.startswith('---'):
        end = text.index('\n---', 3)
        raw, body = text[3:end], text[end + 4:]
        key = None
        for line in raw.splitlines():
            if not line.strip():
                continue
            if line.startswith('  - ') and key:
                fm.setdefault(key, []).append(line[4:].strip())
            elif ':' in line:
                key, val = line.split(':', 1)
                key, val = key.strip(), val.strip()
                fm[key] = val if val else []
    blocks, buf, kind = [], [], 'p'

    def flush():
        if not buf:
            return
        if kind == 'ul':
            blocks.append({'k': 'ul', 'items': list(buf)})
        else:
            blocks.append({'k': kind, 't': ' '.join(buf).strip()})
        buf.clear()

    for line in body.splitlines():
        line = line.rstrip()
        if not line.strip():
            flush()
            kind = 'p'
            continue
        if line.strip() in ('---', '***'):
            # A rule is a page break. Long notes are paged in the app rather
            # than scrolled, so this is where the reader turns over.
            flush()
            blocks.append({'k': 'pg'})
            kind = 'p'
        elif line.startswith('## '):
            flush()
            blocks.append({'k': 'h', 't': line[3:].strip()})
            kind = 'p'
        elif line.startswith('> '):
            if kind != 'note':
                flush()
            kind = 'note'
            buf.append(line[2:].strip())
        elif line.startswith('- '):
            if kind != 'ul':
                flush()
            kind = 'ul'
            buf.append(line[2:].strip())
        elif kind == 'ul' and line[:1] in (' ', '\t') and buf:
            # An indented line under a bullet continues that bullet. Without
            # this a wrapped bullet broke into a bullet plus a stray paragraph,
            # which is exactly what it looked like in the app.
            buf[-1] += ' ' + line.strip()
        else:
            if kind not in ('p',):
                flush()
                kind = 'p'
            buf.append(line.strip())
    flush()
    return fm, blocks


def render_note(key, entry, sources=None):
    """JSON entry -> markdown, for the one-time export."""
    out = ['---', 'key: ' + key, 'title: ' + entry['title']]
    if sources:
        out.append('sources:')
        out += ['  - ' + s for s in sources]
    out += ['---', '']
    for b in entry['blocks']:
        if b['k'] == 'pg':
            out.append('---')
        elif b['k'] == 'h':
            out.append('## ' + b['t'])
        elif b['k'] == 'note':
            out.append('> ' + b['t'])
        elif b['k'] == 'ul':
            out += ['- ' + i for i in b['items']]
        else:
            out.append(b['t'])
        out.append('')
    return '\n'.join(out).rstrip() + '\n'


def slug(key):
    return re.sub(r'[^a-z0-9]+', '-', key.lower()).strip('-')


# ----------------------------------------------------------------- commands --

def cmd_export():
    """One-time: lift the notes that exist only inside data/commentary.js out
    into markdown, so rebuilding cannot lose them."""
    os.makedirs(SRC, exist_ok=True)
    data = load_blob(OUT, 'const COMMENTARY =')
    for key, entry in data.items():
        path = os.path.join(SRC, slug(key) + '.md')
        if os.path.exists(path):
            print('  skip (exists) ', path)
            continue
        io.open(path, 'w', encoding='utf-8', newline='\n').write(render_note(key, entry))
        print('  wrote', os.path.relpath(path, ROOT))
    print('exported %d notes' % len(data))


def read_sources():
    notes = {}
    for name in sorted(os.listdir(SRC)):
        if not name.endswith('.md'):
            continue
        fm, blocks = parse_note(io.open(os.path.join(SRC, name), encoding='utf-8').read())
        if 'key' not in fm:
            print('  !! %s has no key in its front matter' % name)
            continue
        notes[fm['key']] = ({'title': fm.get('title', ''), 'blocks': blocks}, fm, name)
    return notes


def cmd_validate(quiet=False):
    labels = verse_labels()
    notes = read_sources()
    bad = 0
    for key, (_entry, _fm, name) in sorted(notes.items()):
        if key in labels:
            if not quiet:
                print('  ok   %-24s %s' % (key, name))
            continue
        bad += 1
        if '-' in key and key.replace('-', EN) in labels:
            print('  FAIL %-24s %s -- hyphen where an en dash belongs; should be "%s"'
                  % (key, name, key.replace('-', EN)))
        else:
            fixed, why = resolve(key)
            print('  FAIL %-24s %s -- %s' % (key, name, why if not fixed else
                                             'should be "%s" (%s)' % (fixed, why)))
    print('%d notes, %d unreachable' % (len(notes), bad))
    return bad


def cmd_build():
    if cmd_validate(quiet=True):
        print('build refused: a note that cannot be reached is worse than no note')
        return 1
    notes = read_sources()
    data = {k: v[0] for k, v in notes.items()}
    body = HEADER + 'const COMMENTARY = ' + json.dumps(data, ensure_ascii=False) + ';\n'
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write(body)
    print('wrote %s -- %d notes' % (os.path.relpath(OUT, ROOT), len(data)))
    return 0


def cmd_ledger():
    """Every reference every sermon touched, resolved to the verse block that
    holds it, counted across sermons.

    Resolving first is the whole point. A sermon citing Romans 8:14 and another
    citing Romans 8:16 look like different references and are not: they land in
    Romans 8:12-14 and Romans 8:15-17, two separate notes. Another pair citing
    Hebrews 12:14 and 12:15 look different and ARE the same block. Counting the
    raw strings would miss both, so recurrence is counted on the resolved key --
    which is also the key a note is filed under.

    RECUR + note written  -> go back and deepen the note with the new sermon
    RECUR + nothing yet   -> it has earned one; write it
    """
    if not os.path.exists(LEDGER):
        print('no ledger yet')
        return
    led = json.load(io.open(LEDGER, encoding='utf-8'))
    written = set(read_sources().keys()) if os.path.isdir(SRC) else set()

    hits, unresolved = {}, {}
    for s in led['sermons']:
        for r in s['refs']:
            key, _why = resolve(r)
            if key:
                hits.setdefault(key, []).append((s['date'], r))
            else:
                unresolved.setdefault(r, []).append(s['date'])

    print('%d sermons studied, %d references, %d distinct verse blocks'
          % (len(led['sermons']), sum(len(v) for v in hits.values()), len(hits)))
    print('%d blocks have a note, %d do not\n' %
          (len(set(hits) & written), len(set(hits) - written)))

    recur = {k: v for k, v in hits.items() if len({d for d, _ in v}) > 1}
    if recur:
        print('SEEN IN MORE THAN ONE SERMON -- revisit these first')
        for k, v in sorted(recur.items(), key=lambda x: -len(x[1])):
            mark = 'deepen the note' if k in written else 'NO NOTE YET'
            print('  %-22s %d sermons  %-16s %s'
                  % (k, len({d for d, _ in v}), mark, ', '.join(sorted({d for d, _ in v}))))
        print()

    once = [k for k in hits if k not in recur and k not in written]
    if once:
        print('touched once, no note yet (%d):' % len(once))
        for k in sorted(once):
            print('  %-22s %s' % (k, ', '.join(sorted({d for d, _ in hits[k]}))))

    if unresolved:
        print('\ncould not be resolved to a verse block (%d) -- check by hand:'
              % len(unresolved))
        for r, dates in sorted(unresolved.items()):
            print('  %-22s %s' % (r, ', '.join(dates)))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'validate'
    if cmd == 'export':
        cmd_export()
    elif cmd == 'build':
        sys.exit(cmd_build())
    elif cmd == 'validate':
        sys.exit(1 if cmd_validate() else 0)
    elif cmd == 'resolve':
        key, why = resolve(' '.join(sys.argv[2:]))
        print(key if key else 'NO MATCH', ' -- ', why)
    elif cmd == 'ledger':
        cmd_ledger()
    else:
        print(__doc__)

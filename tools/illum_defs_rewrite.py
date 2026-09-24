"""
Overwrite existing Illumination bulb definitions in data/illum-defs.js with
grace-centered rewrites -- Chris's call: the plain retellings from his book
and from illum_defs_author.py are being replaced, book by book, with notes
that point to Jesus and His grace in that portion of scripture, not just
restate what the verse says.

Companion to illum_defs_author.py, which is for NEW definitions and refuses
to touch an entry that already exists. This script is the opposite: it
REQUIRES every (chapterRef, blockLabel) to already have an entry (so it can
never accidentally create a new one out of a typo'd label) and overwrites
that entry's text -- the deliberate, tracked version of what
illum_defs_author.py's safety check exists to prevent.

Input: a .py file defining DEFS = [(chapterRef, blockLabel, text), ...].

Usage:
    python tools/illum_defs_rewrite.py <path to a DEFS .py file>
"""
import json, sys, os, importlib.util

DEFS_PATH = 'data/illum-defs.js'
ILLUM_PATH = 'data/illumination.js'


def load_illumination():
    with open(ILLUM_PATH, encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('const ILLUMINATION = '):
                return json.loads(ln[len('const ILLUMINATION = '):-2])
    raise SystemExit('ILLUMINATION const not found')


def load_existing_defs():
    with open(DEFS_PATH, encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('const ILLUM_DEFS = '):
                return json.loads(ln[len('const ILLUM_DEFS = '):-2])
    raise SystemExit('ILLUM_DEFS const not found')


def write_defs(data):
    header = (
        "/* Definitions for the bulb under the Illumination Translation reader.\n"
        "   Two sources, both keyed chapter ref -> Illumination verse-block label\n"
        "   -> definition text: most from Chris's own book, \"The Illumination\n"
        "   Translation\" (C.S. Knight), via tools/illum_defs_build.py; the rest\n"
        "   authored directly for blocks that book doesn't cover, via\n"
        "   tools/illum_defs_author.py -- plain, elementary retellings of what the\n"
        "   verse says, not interpretation. Never hand-edit this file itself.\n"
        "\n"
        "   2026-09-24: book by book, entries are being REWRITTEN in place via\n"
        "   tools/illum_defs_rewrite.py to be grace-centered -- each note now\n"
        "   points to Jesus and what His grace does in that portion of scripture,\n"
        "   not just a plain retelling of the verse. See CHANGELOG for progress. */\n"
    )
    line = 'const ILLUM_DEFS = ' + json.dumps(data, ensure_ascii=False) + ';\n'
    with open(DEFS_PATH, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(line)


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    defs_module_path = sys.argv[1]

    spec = importlib.util.spec_from_file_location('defs_module', defs_module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    new_defs = mod.DEFS

    illum = load_illumination()
    illum_by_ref = {c['ref']: c for c in illum}
    existing = load_existing_defs()

    errors = []
    seen = set()
    for chap_ref, label, text in new_defs:
        key = (chap_ref, label)
        if key in seen:
            errors.append(f'{chap_ref} {label}: duplicate entry within this batch')
            continue
        seen.add(key)

        chap = illum_by_ref.get(chap_ref)
        if not chap:
            errors.append(f'no such Illumination chapter: {chap_ref!r}')
            continue
        labels = {v[0] for s in chap['sections'] for v in s['verses']}
        if label not in labels:
            errors.append(f'{chap_ref}: no such block label {label!r}')
            continue
        if chap_ref not in existing or label not in existing[chap_ref]:
            errors.append(f'{chap_ref} {label}: no existing definition to rewrite '
                           f'-- use illum_defs_author.py to add a new one')
            continue
        if not text or not text.strip():
            errors.append(f'{chap_ref} {label}: empty text')
            continue
        if text.strip() == existing[chap_ref][label].strip():
            errors.append(f'{chap_ref} {label}: identical to the existing text -- not a rewrite')
            continue

    if errors:
        print(f'{len(errors)} problem(s) -- wrote nothing:')
        for e in errors[:50]:
            print('  ', e)
        raise SystemExit(1)

    rewritten = 0
    for chap_ref, label, text in new_defs:
        existing[chap_ref][label] = text
        rewritten += 1

    write_defs(existing)
    print(f'rewrote {rewritten} definitions from {defs_module_path}')
    print(f'wrote {DEFS_PATH}: {len(existing)} chapters total, '
          f'{sum(len(v) for v in existing.values())} definitions total')


if __name__ == '__main__':
    main()

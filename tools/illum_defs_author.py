"""
Merge hand-authored Illumination bulb definitions into data/illum-defs.js.

Companion to illum_defs_build.py, which pulls definitions from Chris's own
book (EPUB-sourced, NT only, ~56% coverage). This one takes AUTHORED
definitions -- plain, elementary retellings of what a verse block says, no
interpretation -- for the blocks that book doesn't cover, one chapter's
worth (or a few) at a time.

Input: a .py file defining DEFS = [(chapterRef, blockLabel, text), ...].
Validates every (chapterRef, blockLabel) actually exists in ILLUMINATION and
does NOT already have an entry in ILLUM_DEFS (so this can never silently
overwrite Chris's own book content, or something authored in an earlier
run) before writing anything.

Usage:
    python tools/illum_defs_author.py <path to a DEFS .py file>
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
    if not os.path.exists(DEFS_PATH):
        return {}
    with open(DEFS_PATH, encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('const ILLUM_DEFS = '):
                return json.loads(ln[len('const ILLUM_DEFS = '):-2])
    return {}


def write_defs(data):
    header = (
        "/* Definitions for the bulb under the Illumination Translation reader.\n"
        "   Two sources, both keyed chapter ref -> Illumination verse-block label\n"
        "   -> definition text: most from Chris's own book, \"The Illumination\n"
        "   Translation\" (C.S. Knight), via tools/illum_defs_build.py; the rest\n"
        "   authored directly for blocks that book doesn't cover, via\n"
        "   tools/illum_defs_author.py -- plain, elementary retellings of what the\n"
        "   verse says, not interpretation. Never hand-edit this file itself. */\n"
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
    added = 0
    for chap_ref, label, text in new_defs:
        chap = illum_by_ref.get(chap_ref)
        if not chap:
            errors.append(f'no such Illumination chapter: {chap_ref!r}')
            continue
        labels = {v[0] for s in chap['sections'] for v in s['verses']}
        if label not in labels:
            errors.append(f'{chap_ref}: no such block label {label!r}')
            continue
        if chap_ref in existing and label in existing[chap_ref]:
            errors.append(f'{chap_ref} {label}: already has a definition -- refusing to overwrite')
            continue
        if not text or not text.strip():
            errors.append(f'{chap_ref} {label}: empty text')
            continue

    if errors:
        print(f'{len(errors)} problem(s) -- wrote nothing:')
        for e in errors[:50]:
            print('  ', e)
        raise SystemExit(1)

    for chap_ref, label, text in new_defs:
        existing.setdefault(chap_ref, {})[label] = text
        added += 1

    write_defs(existing)
    print(f'added {added} definitions from {defs_module_path}')
    print(f'wrote {DEFS_PATH}: {len(existing)} chapters total, '
          f'{sum(len(v) for v in existing.values())} definitions total')


if __name__ == '__main__':
    main()

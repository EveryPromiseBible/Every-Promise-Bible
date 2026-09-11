"""
Build data/illum-defs.js -- verse-block definitions for the bulb under the
Illumination Translation reader, sourced from Chris's own book "The
Illumination Translation" (C.S. Knight), shipped as a set of EPUBs (one per
NT section: Gospels, Acts, Pauline Epistles, General Epistles, Revelation).

Each EPUB chapter is a flat run of <p> tags: verse paragraphs open with
"(Book C:V) text", and a definition paragraph opens with the U+1F4A1 bulb
emoji and closes out every verse accumulated since the previous definition
(or chapter start). Section <h3>/<h5> headings and empty <p/> spacers don't
reset the accumulator.

The book's own verse ranges rarely line up with the site's own ILLUMINATION
verse blocks -- the site paraphrase re-chunks the text more finely. So each
parsed definition is attached to the LAST Illumination block in that chapter
whose own start verse falls inside the definition's range: the bulb ends up
sitting after the reader finishes the passage the definition explains, not
mid-passage. When two definitions land on the same site block (the site is
coarser there than the book), their text is concatenated in order rather than
one silently overwriting the other.

Usage:
    python tools/illum_defs_build.py "<path to epub dir OR .epub file>" [BookName]

Merges into the existing data/illum-defs.js (adds/overwrites only the
chapters touched) rather than clobbering other books already built.
"""
import re, json, sys, os, html as htmlmod, zipfile, tempfile, shutil

BULB = '\U0001F4A1'
# Book name is everything between the navPoint's own ordinal ("19. ") and the
# trailing chapter number -- NOT \w+, which only matches a single word and
# silently dropped every multi-word book (1st Corinthians, 1 Thessalonians,
# 1 Timothy, 1/2/3 John...) the first time this ran. The book's own leading
# ordinal shows up two ways in this author's EPUBs -- "1st Corinthians" but
# "1 Thessalonians" -- and the site's own ILLUMINATION_BOOKS names are always
# the bare digit ("1 Corinthians"), so normalize 1st/2nd/3rd -> 1/2/3.
CHAP_RE = re.compile(r'^\d+\.\s+(.+?)\s+(\d+)$')
ORDINAL_RE = re.compile(r'^([123])(?:st|nd|rd)\b(.*)$')
VREF_RE = re.compile(r'^(\d+):(\d+)(?:[–‒-](\d+))?$')


def normalize_book(name):
    m = ORDINAL_RE.match(name)
    return m.group(1) + m.group(2) if m else name

DEFS_PATH = 'data/illum-defs.js'
ILLUM_PATH = 'data/illumination.js'


def load_toc(oebps_dir):
    with open(os.path.join(oebps_dir, 'toc.ncx'), encoding='utf-8') as f:
        content = f.read()
    navpoints = re.findall(r'<navPoint.*?</navPoint>', content, re.S)
    out = []
    for np in navpoints:
        label = re.search(r'<text>(.*?)</text>', np, re.S).group(1).strip()
        src = re.search(r'<content src="(.*?)"', np).group(1)
        out.append((label, src))
    return out


def strip_tags(s):
    return re.sub(r'<[^>]+>', '', s).strip()


def parse_chapter(path):
    with open(path, encoding='utf-8') as f:
        htm = f.read()
    body_m = re.search(r'<body[^>]*>(.*)</body>', htm, re.S)
    body = body_m.group(1) if body_m else htm
    paras = re.findall(r'<p>(.*?)</p>', body, re.S)

    blocks = []
    cur_v1 = cur_v2 = None
    verse_line = re.compile(r'^\(([A-Za-z0-9 ]+?) (\d+):(\d+)\)\s*(.*)$', re.S)

    for raw in paras:
        plain = htmlmod.unescape(strip_tags(raw))
        if not plain:
            continue
        if plain.startswith(BULB):
            def_text = plain[len(BULB):].strip()
            if cur_v1 is not None:
                blocks.append({'v1': cur_v1, 'v2': cur_v2, 'text': def_text})
            cur_v1 = cur_v2 = None
            continue
        m = verse_line.match(plain)
        if m:
            v = int(m.group(3))
            if cur_v1 is None:
                cur_v1 = v
            cur_v2 = v
    return blocks


def parse_epub(epub_dir, book_filter=None):
    oebps = os.path.join(epub_dir, 'OEBPS')
    toc = load_toc(oebps)
    result = {}
    for label, src in toc:
        m = CHAP_RE.match(label)
        if not m:
            continue
        book, chap = normalize_book(m.group(1)), m.group(2)
        if book_filter and book != book_filter:
            continue
        blocks = parse_chapter(os.path.join(oebps, src))
        result[f'{book} {chap}'] = blocks
    return result


def load_illumination(path):
    with open(path, encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('const ILLUMINATION = '):
                return json.loads(ln[len('const ILLUMINATION = '):-2])
    raise SystemExit('ILLUMINATION const not found in ' + path)


def block_verses(label):
    m = VREF_RE.match(label)
    if not m:
        return None
    v1 = int(m.group(2))
    v2 = int(m.group(3)) if m.group(3) else v1
    return v1, v2


def map_to_illum(defs_by_chapter, illum):
    illum_by_ref = {c['ref']: c for c in illum}
    result = {}
    unmatched, collisions = [], []
    for chap_ref, dblocks in defs_by_chapter.items():
        chap = illum_by_ref.get(chap_ref)
        if not chap:
            unmatched.append((chap_ref, 'no illum chapter'))
            continue
        flat = []
        for sec in chap['sections']:
            for label, _text in sec['verses']:
                bv = block_verses(label)
                if bv:
                    flat.append((label, bv[0], bv[1]))
        chap_map = {}
        for d in dblocks:
            v1, v2 = d['v1'], d['v2']
            candidates = [f for f in flat if v1 <= f[1] <= v2]
            if candidates:
                target = candidates[-1]
            else:
                below = [f for f in flat if f[1] <= v1]
                target = below[-1] if below else (flat[0] if flat else None)
            if not target:
                unmatched.append((chap_ref, f'{v1}-{v2}'))
                continue
            label = target[0]
            if label in chap_map:
                collisions.append((chap_ref, label))
                chap_map[label] = chap_map[label] + ' ' + d['text']
            else:
                chap_map[label] = d['text']
        if chap_map:
            result[chap_ref] = chap_map
    return result, unmatched, collisions


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
        "/* Definitions for the bulb under the Illumination Translation reader --\n"
        "   Chris's own book, \"The Illumination Translation\" (C.S. Knight). Keyed\n"
        "   chapter ref -> Illumination verse-block label -> definition text. Built\n"
        "   by tools/illum_defs_build.py; never hand-edit, regenerate instead. */\n"
    )
    line = 'const ILLUM_DEFS = ' + json.dumps(data, ensure_ascii=False) + ';\n'
    with open(DEFS_PATH, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(line)


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    src = sys.argv[1]
    book_filter = sys.argv[2] if len(sys.argv) > 2 else None

    tmp = None
    epub_dir = src
    if os.path.isfile(src) and src.lower().endswith('.epub'):
        tmp = tempfile.mkdtemp(prefix='illumdefs_')
        with zipfile.ZipFile(src) as zf:
            zf.extractall(tmp)
        epub_dir = tmp

    try:
        defs = parse_epub(epub_dir, book_filter)
        illum = load_illumination(ILLUM_PATH)
        mapped, unmatched, collisions = map_to_illum(defs, illum)

        existing = load_existing_defs()
        existing.update(mapped)
        write_defs(existing)

        total_in = sum(len(v) for v in defs.values())
        total_out = sum(len(v) for v in mapped.values())
        print(f'chapters parsed: {len(defs)}')
        print(f'definitions parsed: {total_in}')
        print(f'chapters mapped: {len(mapped)}')
        print(f'definitions placed: {total_out}')
        print(f'unmatched: {len(unmatched)}')
        for u in unmatched[:20]:
            print('  UNMATCHED', u)
        print(f'collisions (concatenated): {len(collisions)}')
        for c in collisions[:20]:
            print('  COLLISION', c)
        print(f'wrote {DEFS_PATH}: {len(existing)} chapters total')
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    main()

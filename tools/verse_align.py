# -*- coding: utf-8 -*-
"""Assign a verse number to every Mak Translation word-unit, across all 27 New
Testament books, by matching each unit's Greek token(s) against MorphGNT
(which knows the verse of every word) -- without touching any existing
english/greek/tags content.

Method, and why:
  Units are stored in English reading order, not Greek order, so a straight
  top-to-bottom walk against MorphGNT's verse-ordered stream doesn't line up.
  But sections are never reordered relative to each other -- each is a
  contiguous, non-overlapping span of the original text, just internally
  rearranged. So: walk sections in canonical order, and for each one, consume
  exactly as many MorphGNT tokens as that section holds Greek tokens. Verify
  the multiset matches (the real safety check) before trusting the slice.

  Within a section's slice (usually 1-3 verses), match each unit's Greek
  token(s) to the earliest still-unused MorphGNT row with the same surface
  form, in the order units appear (English order). This is a "first available
  match" -- not a proof, but sections are short enough that this is the
  correct assignment in the overwhelming majority of cases, and every
  assumption is checked, not trusted blindly (see report at the end).

  A fancier version was tried and reverted: a single cursor shared across the
  whole section, always preferring the nearest match AHEAD of the last thing
  placed. It sounded more rigorous but was much worse in practice -- Matthew 1's
  genealogy repeats "the" and "was the father of" in nearly every clause, so one
  early wrong pick shoved the cursor forward and every pick after it inherited
  the error (14 wrong units became 661, tested on Matthew alone). Independent
  per-form queues, taken in strict left-to-right order with no shared state
  between forms, is what actually got the whole genealogy right. Don't
  reintroduce a shared cursor without re-testing against Matthew 1 specifically.

  Piloted on Matthew alone 2026-08-14 (0 mismatches, 14/14,699 units flagged as
  spanning two verses, all hand-checked -- see CHANGELOG); this run extends the
  identical method to the other 26 books with no algorithm changes.

  Run from the repo root: python tools/verse_align.py
  Writes data/mak_verses.js (const MAK_VERSES, keyed by book name then chapter
  number) -- additive, chapters.js untouched -- and prints a verification
  report per book: multiset mismatches (should be 0 everywhere) and units
  whose tokens spanned two verses (rare, and not automatically "fixed" --
  hand-check before trusting a large count for any one book).
"""
import io, json, sys, unicodedata
from collections import defaultdict, deque, Counter

sys.stdout.reconfigure(encoding='utf-8')

CHAPTERS_JS = 'data/chapters.js'
OUT_FILE = 'data/mak_verses.js'

# Book name (as it appears in CHAPTERS' ref field) -> MorphGNT file.
BOOKS = [
    ('Matthew',          '61-Mt'),
    ('Mark',             '62-Mk'),
    ('Luke',             '63-Lk'),
    ('John',             '64-Jn'),
    ('Acts',             '65-Ac'),
    ('Romans',           '66-Ro'),
    ('1 Corinthians',    '67-1Co'),
    ('2 Corinthians',    '68-2Co'),
    ('Galatians',        '69-Ga'),
    ('Ephesians',        '70-Eph'),
    ('Philippians',      '71-Php'),
    ('Colossians',       '72-Col'),
    ('1 Thessalonians',  '73-1Th'),
    ('2 Thessalonians',  '74-2Th'),
    ('1 Timothy',        '75-1Ti'),
    ('2 Timothy',        '76-2Ti'),
    ('Titus',            '77-Tit'),
    ('Philemon',         '78-Phm'),
    ('Hebrews',          '79-Heb'),
    ('James',            '80-Jas'),
    ('1 Peter',          '81-1Pe'),
    ('2 Peter',          '82-2Pe'),
    ('1 John',           '83-1Jn'),
    ('2 John',           '84-2Jn'),
    ('3 John',           '85-3Jn'),
    ('Jude',             '86-Jud'),
    ('Revelation',       '87-Re'),
]

def norm_key(s):
    """Match key only -- never used for anything that gets written back.
    Lowercases (sentence-initial capitals) and folds grave accent to acute
    (the same grave/acute-before-a-following-word cosmetic variance PROJECT.md
    already documents as a false-positive source, not a real word difference)."""
    d = unicodedata.normalize('NFD', s)
    d = d.replace('̀', '́')  # combining grave -> combining acute
    return unicodedata.normalize('NFC', d).lower()

def load_chapters():
    with io.open(CHAPTERS_JS, encoding='utf-8') as f:
        raw = f.read()
    raw = raw.strip()
    assert raw.startswith('const CHAPTERS = ')
    raw = raw[len('const CHAPTERS = '):].rstrip(';\n')
    return json.loads(raw)

def load_morph(path):
    """Returns {chapter_num: [(verse_num, surface), ...]} in file (canonical) order."""
    by_chapter = defaultdict(list)
    with io.open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            p = line.split()
            code = p[0]
            chapter = int(code[2:4])
            verse = int(code[4:6])
            surface = p[4]
            by_chapter[chapter].append((verse, surface))
    return by_chapter

def align_book(book_chapters, morph):
    """book_chapters: list of CHAPTERS entries for one book, in order.
    Returns (verses_by_chapter_num, report_dict) for this book alone."""
    report = {
        'chapters_ok': 0, 'chapters_total': len(book_chapters),
        'section_multiset_mismatches': [], 'multi_verse_span_units': [],
        'total_units': 0, 'units_with_verse': 0, 'units_filler_filled': 0,
    }
    verses_by_chapter = {}

    for ch in book_chapters:
        chapter_num = int(ch['ref'].split()[-1])
        seq = morph.get(chapter_num, [])
        p = 0
        chapter_issue = False
        unit_verse_flat = []

        for si, sec in enumerate(ch['sections']):
            words = sec['words']
            greek_tokens = []
            for w in words:
                greek = w[1].strip()
                greek_tokens.extend(greek.split() if greek else [])
            n = len(greek_tokens)
            sl = seq[p:p+n]

            want = Counter(norm_key(t) for t in greek_tokens)
            have = Counter(norm_key(s) for _, s in sl)
            if want != have:
                report['section_multiset_mismatches'].append(
                    (ch['ref'], si, sec.get('heading'), n, len(sl)))
                chapter_issue = True
                for wi in range(len(words)):
                    unit_verse_flat.append((si, wi, None))
                p += n
                continue

            queues = defaultdict(deque)
            for v, s in sl:
                queues[norm_key(s)].append(v)

            for wi, w in enumerate(words):
                greek = w[1].strip()
                toks = greek.split() if greek else []
                vs = [queues[norm_key(t)].popleft() for t in toks]
                if not vs:
                    unit_verse_flat.append((si, wi, None))
                elif len(set(vs)) == 1:
                    unit_verse_flat.append((si, wi, vs[0]))
                else:
                    report['multi_verse_span_units'].append((ch['ref'], si, wi, w[0], w[1], vs))
                    unit_verse_flat.append((si, wi, vs[0]))

            p += n

        if p != len(seq):
            chapter_issue = True
            report['section_multiset_mismatches'].append((ch['ref'], 'TOTAL', 'token count', p, len(seq)))

        if not chapter_issue:
            report['chapters_ok'] += 1

        for (si, wi, v) in unit_verse_flat:
            report['total_units'] += 1
            if v is not None:
                report['units_with_verse'] += 1

        filled = list(unit_verse_flat)
        last_verse = None
        for i in range(len(filled)):
            si, wi, v = filled[i]
            if v is None and last_verse is not None:
                filled[i] = (si, wi, last_verse)
                report['units_filler_filled'] += 1
            elif v is not None:
                last_verse = v
        next_verse = None
        for i in range(len(filled) - 1, -1, -1):
            si, wi, v = filled[i]
            if v is None and next_verse is not None:
                filled[i] = (si, wi, next_verse)
                report['units_filler_filled'] += 1
            elif v is not None:
                next_verse = v

        verses_by_chapter[chapter_num] = [v for (si, wi, v) in filled]

    return verses_by_chapter, report

def main():
    chapters = load_chapters()
    ALL_VERSES = {}
    grand = Counter()
    problem_books = []

    for book_name, morph_stub in BOOKS:
        book_chapters = [c for c in chapters if c['ref'].startswith(book_name + ' ')]
        morph_path = f'tools/data/{morph_stub}-morphgnt.txt'
        morph = load_morph(morph_path)
        verses, report = align_book(book_chapters, morph)
        ALL_VERSES[book_name] = {str(k): v for k, v in verses.items()}

        ok = report['chapters_ok'] == report['chapters_total']
        status = 'OK' if ok else 'ISSUES'
        print(f"{book_name:20} {report['chapters_ok']:>3}/{report['chapters_total']:<3} chapters clean   "
              f"units={report['total_units']:<6} spans={len(report['multi_verse_span_units']):<4} "
              f"mismatches={len(report['section_multiset_mismatches']):<3} [{status}]")
        if not ok:
            problem_books.append(book_name)
            for m in report['section_multiset_mismatches']:
                print('    MISMATCH:', m)
        if report['multi_verse_span_units']:
            for m in report['multi_verse_span_units']:
                print('    SPAN:', m)

        grand['total_units'] += report['total_units']
        grand['units_with_verse'] += report['units_with_verse']
        grand['units_filler_filled'] += report['units_filler_filled']
        grand['spans'] += len(report['multi_verse_span_units'])
        grand['mismatches'] += len(report['section_multiset_mismatches'])

    print()
    print('=== GRAND TOTAL, all 27 books ===')
    print('total units:', grand['total_units'])
    print('units with a direct verse:', grand['units_with_verse'])
    print('filler units filled from neighbor:', grand['units_filler_filled'])
    print('multi-verse-span units:', grand['spans'])
    print('section multiset mismatches:', grand['mismatches'])
    print('books with issues:', problem_books or 'none')

    out = 'const MAK_VERSES = ' + json.dumps(ALL_VERSES, ensure_ascii=False) + ';\n'
    with io.open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'\nWrote {OUT_FILE}: {len(out)} bytes.')

if __name__ == '__main__':
    main()

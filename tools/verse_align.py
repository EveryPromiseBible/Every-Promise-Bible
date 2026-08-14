# -*- coding: utf-8 -*-
"""Pilot: assign a verse number to every Mak Translation word-unit in Matthew,
by matching each unit's Greek token(s) against MorphGNT (which knows the verse
of every word), without touching any existing english/greek/tags content.

Method, and why:
  Units were reordered into English reading order during translation work, so
  a straight top-to-bottom walk against MorphGNT's verse-ordered stream won't
  line up. But sections were never reordered RELATIVE TO EACH OTHER -- each
  section is a contiguous, non-overlapping span of the original text, just
  internally rearranged. So: walk sections in order, and for each one, consume
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
  the error (14 wrong units became 661). Independent per-form queues, taken in
  strict left-to-right order with no shared state between forms, is what
  actually got the whole genealogy right. Don't reintroduce a shared cursor
  without re-testing against Matthew 1 specifically.

  Run from the repo root: python tools/verse_align.py
  Writes data/mak_verses_matthew.pilot.js (Matthew only, additive, chapters.js
  untouched) and prints a verification report -- multiset mismatches per
  section (should be 0) and units whose tokens spanned two verses (currently
  14/14699; hand-checked, not bugs -- see PROJECT.md or ask before "fixing").
"""
import io, json, re, sys, unicodedata
from collections import defaultdict, deque

sys.stdout.reconfigure(encoding='utf-8')

CHAPTERS_JS = 'data/chapters.js'
MORPH_FILE = 'tools/data/61-Mt-morphgnt.txt'

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

def main():
    chapters = load_chapters()
    matt = [c for c in chapters if c['ref'].startswith('Matthew ')]
    morph = load_morph(MORPH_FILE)

    report = {
        'chapters_ok': 0,
        'chapters_with_issues': [],
        'section_multiset_mismatches': [],
        'multi_verse_span_units': [],
        'total_units': 0,
        'units_with_verse': 0,
        'units_filler_filled': 0,
    }

    ch1_debug = []
    MATTHEW_VERSES = {}

    for ch in matt:
        chapter_num = int(ch['ref'].split()[-1])
        seq = morph.get(chapter_num, [])
        p = 0
        chapter_issue = False
        unit_verse_flat = []  # (section_idx, unit_idx, verse_or_None)

        for si, sec in enumerate(ch['sections']):
            words = sec['words']
            greek_tokens = []
            for w in words:
                greek = w[1].strip()
                greek_tokens.extend(greek.split() if greek else [])
            n = len(greek_tokens)
            sl = seq[p:p+n]

            from collections import Counter
            want = Counter(norm_key(t) for t in greek_tokens)
            have = Counter(norm_key(s) for _, s in sl)
            if want != have:
                report['section_multiset_mismatches'].append(
                    (ch['ref'], si, sec.get('heading'), n, len(sl)))
                chapter_issue = True
                # still advance by n so later sections aren't cascade-broken further
                # than necessary; but don't trust this section's verse assignment.
                for wi in range(len(words)):
                    unit_verse_flat.append((si, wi, None))
                p += n
                continue

            # Reverted: a global "prefer ahead of cursor" heuristic was tried here
            # and made things much worse (661 span-crossings instead of 14) --
            # in text this repetitive (the genealogy repeats "the" and "was the
            # father of" in almost every clause), one early wrong pick snowballs
            # forward into every later one. Per-form independent queues, taken in
            # strict left-to-right correspondence, is what actually got all of
            # Matthew 1's genealogy exactly right; only 14/14699 units anywhere
            # in Matthew were left genuinely ambiguous by it. Those are checked
            # by hand below rather than patched with a cleverer heuristic.
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
            report['chapters_with_issues'].append((ch['ref'], 'token count mismatch', p, len(seq)))

        if chapter_issue:
            report['chapters_with_issues'].append((ch['ref'], 'see mismatches above'))
        else:
            report['chapters_ok'] += 1

        # fill fillers with nearest previous verse in this chapter, else next
        last_verse = None
        for i, (si, wi, v) in enumerate(unit_verse_flat):
            if v is not None:
                last_verse = v
            report['total_units'] += 1
            if v is not None:
                report['units_with_verse'] += 1

        # second pass forward, then backward, to fill None
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

        if chapter_num == 1:
            for (si, wi, v), (si2, wi2, v0) in zip(filled, unit_verse_flat):
                w = ch['sections'][si]['words'][wi]
                ch1_debug.append((v, w[0], w[1]))

        MATTHEW_VERSES[chapter_num] = [v for (si, wi, v) in filled]

    print('=== SUMMARY ===')
    print('chapters ok:', report['chapters_ok'], '/', len(matt))
    print('chapters with issues:', report['chapters_with_issues'])
    print('section multiset mismatches:', len(report['section_multiset_mismatches']))
    for m in report['section_multiset_mismatches'][:10]:
        print('  ', m)
    print('multi-verse-span units (unit whose tokens crossed a verse boundary):',
          len(report['multi_verse_span_units']))
    for m in report['multi_verse_span_units']:
        print('  ', m)
    print('total units:', report['total_units'])
    print('units with a direct verse (had Greek):', report['units_with_verse'])
    print('filler units filled from neighbor:', report['units_filler_filled'])

    print()
    print('=== MATTHEW 1, first 40 units with assigned verse ===')
    for v, eng, grk in ch1_debug[:40]:
        print(f'{v:>2}  {eng!r:35} {grk!r}')

    # Written as its OWN small file, loaded alongside chapters.js -- not merged
    # into it. chapters.js stays byte-for-byte untouched; this is purely an
    # additive overlay the reader can use to show verse numbers for Matthew.
    out = 'const MAK_VERSES_MATTHEW = ' + json.dumps(
        {str(k): v for k, v in MATTHEW_VERSES.items()}, ensure_ascii=False) + ';\n'
    with io.open('data/mak_verses_matthew.pilot.js', 'w', encoding='utf-8') as f:
        f.write(out)
    print('\nWrote mak_verses_matthew.pilot.js:', len(out), 'bytes,',
          sum(len(v) for v in MATTHEW_VERSES.values()), 'unit verse numbers.')

if __name__ == '__main__':
    main()

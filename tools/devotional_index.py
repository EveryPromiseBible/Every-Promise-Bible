"""Build an index of the Daily Grace Inspirations devotionals, grouped by book.

The devotional archive is chronological and has no way to browse by Bible book,
which is the one axis that matters when the job is "cover Genesis". But every
card on the index pages already carries the date, the title, the slug and the
scripture reference, so the whole archive can be indexed once from the listing
pages alone -- no need to open ~450 individual devotionals to find out what
each one is about.

    python tools/devotional_index.py build      # crawl, write devotionals.json
    python tools/devotional_index.py book Genesis   # what is there for a book
    python tools/devotional_index.py gaps Genesis   # ...that we have no note for

`gaps` is the one that drives the work: it lists only the devotionals whose
passage has no commentary note yet, so an existing note is never rewritten and
the reader's next unmarked verse is always what comes up next.
"""
import json, os, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, '_commentary', 'devotionals.json')
BASE = 'https://www.josephprince.org/blog/daily-grace-inspirations'

CARD = re.compile(
    r'href="(/blog/daily-grace-inspirations/[^"]+)".*?'
    r'card__date">\s*([^<]+?)\s*</div>.*?'
    r'card__title">\s*(.*?)\s*</h6>.*?'
    r'card__verseRef">\s*(.*?)\s*</p>',
    re.S)


def clean(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = (s.replace('&nbsp;', ' ').replace('&amp;', '&')
          .replace('&#8217;', "'").replace('&#8211;', '–')
          .replace('&rsquo;', "'").replace('&ldquo;', '"').replace('&rdquo;', '"'))
    return ' '.join(s.split())


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode('utf-8', 'replace')


def build():
    seen, rows, page, empty = set(), [], 1, 0
    while page < 120:
        url = BASE if page == 1 else f'{BASE}?page={page}'
        try:
            html = fetch(url)
        except Exception as e:
            print(f'  page {page}: {e}', file=sys.stderr)
            break
        found = 0
        for href, date, title, ref in CARD.findall(html):
            slug = href.rsplit('/', 1)[-1]
            if slug in seen:
                continue
            seen.add(slug)
            rows.append({'slug': slug, 'date': clean(date),
                         'title': clean(title), 'ref': clean(ref),
                         'url': 'https://www.josephprince.org' + href})
            found += 1
        print(f'  page {page:>3}: {found} new')
        # Two consecutive pages with nothing new is the end of the archive.
        empty = empty + 1 if found == 0 else 0
        if empty >= 2:
            break
        page += 1
        time.sleep(0.4)          # unhurried; this is somebody else's server
    json.dump(rows, open(OUT, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f'{len(rows)} devotionals -> {OUT}')


# A reference may name several passages: "Genesis 45:10-11, John 3:16".
PART = re.compile(r'((?:[1-3]\s*)?[A-Z][A-Za-z]+(?:\s+of\s+[A-Z][a-z]+)?)\s*(\d+):(\d+)')


def refs_for(row):
    """Every (book, chapter, verse) a devotional's reference line points at."""
    out = []
    for book, ch, v in PART.findall(row['ref']):
        out.append((' '.join(book.split()), int(ch), int(v)))
    return out


def load():
    if not os.path.exists(OUT):
        sys.exit('No index yet. Run: python tools/devotional_index.py build')
    return json.load(open(OUT, encoding='utf-8'))


def for_book(book):
    rows = []
    for r in load():
        hits = [x for x in refs_for(r) if x[0].lower() == book.lower()]
        if hits:
            rows.append((min(h[1] for h in hits), min(h[2] for h in hits), r, hits))
    rows.sort(key=lambda t: (t[0], t[1]))
    return rows


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'build'
    if cmd == 'build':
        return build()

    book = ' '.join(sys.argv[2:]) or 'Genesis'
    rows = for_book(book)

    if cmd == 'book':
        for ch, v, r, hits in rows:
            print(f'{r["date"]:>13}  {r["ref"]:<28} {r["title"][:52]:<52} {r["slug"]}')
        print(f'\n{len(rows)} devotionals touching {book}')
        return

    if cmd == 'gaps':
        # Resolve each reference to its Illumination block, then drop the ones
        # that already carry a note -- those are done, and the instruction is
        # to move on rather than rewrite them.
        import importlib.util, glob
        spec = importlib.util.spec_from_file_location('c', os.path.join(HERE, 'commentary.py'))
        c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
        have = set()
        for f in glob.glob(os.path.join(ROOT, '_commentary', '*.md')):
            for line in open(f, encoding='utf-8'):
                if line.startswith('key:'):
                    have.add(line[4:].strip()); break
        todo, covered = [], 0
        for ch, v, r, hits in rows:
            for bk, cc, vv in hits:
                if bk.lower() != book.lower():
                    continue
                try:
                    res = c.resolve(f'{bk} {cc}:{vv}')
                except Exception:
                    res = None
                if not res:
                    continue
                block = res[0]
                if block in have:
                    covered += 1
                else:
                    todo.append((block, r))
        seen = set()
        for block, r in todo:
            if block in seen:
                continue
            seen.add(block)
            print(f'{block:<22} {r["ref"]:<24} {r["title"][:46]:<46} {r["slug"]}')
        print(f'\n{len(seen)} block(s) needing a note; {covered} reference(s) already covered')
        return

    sys.exit('commands: build | book <Book> | gaps <Book>')


if __name__ == '__main__':
    main()

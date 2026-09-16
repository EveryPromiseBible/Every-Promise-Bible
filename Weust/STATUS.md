# Wuest word-study commentary — status

## What this is

Original, verse-by-verse Greek word-study commentary, informed by Kenneth
Wuest's *Word Studies in the Greek New Testament* but **not** a reword or
paraphrase of his text. Wuest chose which Greek words in a verse are worth
stopping on — that selection is followed. The explanation of each word (what
it means, what its tense/case/mood implies, why it matters) is freshly
composed from those grammatical facts, in original sentences, with his own
prose and his citations of other scholars (Robertson, Vincent, Thayer,
Swete, etc.) set aside entirely and never quoted or closely paraphrased.

Each verse entry has two parts:
- **`text`** — the word-by-word commentary, one call-out per Greek word/
  phrase worth noting, in source-verse order.
- **`translation`** — a fresh, original, deliberately literal rendering of
  the verse that bakes the grammatical nuance (tense, mood, voice) directly
  into the English verb constructions rather than smoothing it into normal
  fluent prose — composed independently from the `text` field's grammatical
  facts, not from Wuest's own translation lines.

Wuest covered 16 books of the New Testament with this kind of running
commentary (the rest of his compilation is a separate vocabulary list and
several topical essay collections, out of scope here). This directory holds
one JSON file per finished book: `[{ "label": "Book C:V", "text": "...",
"translation": "..." }, ...]`, one entry per verse or small verse-range,
matching however Wuest himself grouped that discussion.

**Nothing of Wuest's own text is stored anywhere in this repo** — only the
original commentary and translations built from it.

## Progress — 16 of 16 books done, 1,185 entries

All books Wuest covered with running verse-by-verse commentary are now
finished.

| Book | Entries | Status |
|---|---:|---|
| Mark | 364 | done |
| Romans | 156 | done |
| Galatians | 142 | done |
| Ephesians | 66 | done |
| Philippians | 52 | done |
| Colossians | 44 | done |
| Titus | 21 | done |
| Hebrews | 155 | done |
| 1 Timothy | 42 | done |
| 2 Timothy | 35 | done |
| 1 Peter | 46 | done |
| 2 Peter | 21 | done |
| 1 John | 24 | done |
| 2 John | 4 | done |
| 3 John | 4 | done |
| Jude | 9 | done |

Every entry's `text` field has a blank-line break inserted before each
sentence that introduces a new quoted word/phrase not yet discussed in
that entry — retrofitted onto the first 10 books, built in from the start
for the last 6. A structure pass across all 16 files (every entry has
exactly `label`/`text`/`translation`, both fields non-empty, full verse
coverage per book with no gaps or duplicate labels) has been run and
passes clean as of this commit.

## Next steps

1. Run a closer human/editorial QA pass on a larger sample than the
   automated structural check covers — spot-check several entries per
   book for tone consistency and confirm nothing reads as a close
   paraphrase of Wuest's own prose or his citations of other scholars.
2. Design and build the site integration — most likely a tab in the
   Library alongside the translations, plus a "personal" row in the
   word-lookup popup that jumps straight to a tapped word's verse
   commentary when one exists (mirroring how Strong's/Thayer's/
   Abbott-Smith already work), falling back to a searchable index when it
   doesn't. Because this is original writing rather than reproduced text,
   none of the earlier passphrase/private-Worker/personal-only machinery
   is needed — it can just be a normal public feature.

This directory is source material; the compiled, site-facing copy lives in
`data/weust.js` (`const WEUST = {"BookName": [entries...], ...}`), wired
into `index.html`'s word-lookup popup (`weustVerseLookup`, `renderWeust`) —
each entry keyed by verse label, one call-out group per verse under a
"Commentaries" fold alongside Grace Commentary.

## Tense audit against the actual Greek — Romans (156/156 checked)

Every entry's word-selection has always been "informed by Wuest but not
verified against Wuest's actual book" (see the top of this file) — the
grammatical claims (tense, mood, voice) were reasoned out at authoring time
but never checked against a real tagged Greek text. Asked to actually check
one, starting from a flagged concern at Romans 5:17.

The repo already has real ground truth for this: `tools/data/66-Ro-morphgnt.txt`
(SBLGNT via MorphGNT) tags every word's part of speech, tense, voice, and
mood. Built a one-off script pulling every verb/participle per verse,
flagged the categories most likely to carry tense-critical nuance if missed
(present participles, perfects, imperfects, subjunctives — 80 of 156 entries
had at least one), and read through all of them checking whether the
`translation` field's English verb construction actually reflects that
tense's force, the same way an editor would with a Greek text open beside
the draft.

Most of Romans was already sound — durative present participles regularly
got "keeps on," "is continually," "habitually," or a plain progressive;
perfects regularly got "have/has ___-ed, and it stands"-style completed-
with-present-result phrasing; stative verbs (*oida*, *thelō*, *echō*) were
correctly left as plain English present, since English doesn't have a
natural progressive for "know"/"want"/"have." Two real misses found and
fixed:

1. **5:17 — "those who receive" dropped the tense entirely.** *Lambanontes*
   (λαμβάνοντες) is a present participle, durative, deliberately contrasted
   with the aorist "reigned" one clause earlier (death seized the throne in
   one decisive act; grace is pictured as something laid hold of
   continuously). The `text` field never even mentioned this participle.
   Fixed the translation to "those who **are receiving**" and added the
   contrast to the commentary.
2. **13:2 — the same verb given two different tense treatments in one
   verse.** *Anthistēmi* (ἀνθίστημι) appears twice: the indicative
   ("resisteth the ordinance of God") was correctly rendered with its
   perfect force ("has set himself in **permanent opposition**"), but the
   participle three words later ("they that resist") — same lemma, same
   perfect tense — was flattened to a plain present, "those who are so
   opposing." Fixed to "those who **stand in that permanent opposition**,"
   matching the perfect-force phrasing already used for the first
   occurrence in the same verse.

Re-verified: still 156/156 entries, re-spliced into `data/weust.js`, and
confirmed live via `weustVerseLookup()` in a running instance of the site —
1,077 total entries across all 10 currently-compiled books, zero structural
errors.

## Tense audit against the actual Greek — Mark (364/364 checked, clean)

Same method, against `tools/data/62-Mk-morphgnt.txt`. 276 of 364 entries had
at least one present participle, perfect, imperfect, or subjunctive worth
checking — a much higher share than Romans, since Mark's narrative style
leans hard on participles and Wuest's own commentary tracks that closely.
Read through every one of them against the translation.

**No fixes needed.** The book was already handling this well and
consistently: imperfects almost always got "kept on ___-ing" or "was
continually ___-ing" (not just a flat English past); perfects regularly got
the "has ___-ed, and stands/remains so" double phrasing (5:34's "your faith
has saved you, and the salvation stands"; 7:29's "the demon has gone out...
and remains gone"; 11:21's "has withered away"); stative verbs (*oida*,
*echō*, *eimi*) were left as plain English present/past rather than forced
into an awkward progressive, matching how Romans handles the same verbs.
Historical presents (very frequent in Mark's Greek) were correctly left as
Wuest himself renders them — his real practice keeps many of them ("and
they come," "and he says to them") rather than smoothing every one into
past tense, and that's what's reflected here too.

## Tense audit against the actual Greek — Galatians (142/142 checked)

Same method, against `tools/data/69-Ga-morphgnt.txt`. 79 of 142 entries had
a present participle, perfect, imperfect, or subjunctive worth checking.

One real fix, and it's the same *shape* of miss as Romans 13:2 — the same
verb given two different tense treatments within one short letter. 5:2-3
correctly makes a point of *peritemnō*'s (περιτέμνω) present-tense
participle: "the participle for 'circumcised' is present tense, aimed at
anyone in the act of receiving the rite, not at those already done." But
6:13 — same lemma, same present participle in the source Greek
(*peritemnomenoi*, περιτεμνόμενοι) — was rendered "those who **are
circumcised**," reading like a settled past state rather than an ongoing
one, and the commentary never mentioned the tense at all. Fixed the
translation to "those who **are having themselves circumcised**," matching
5:3's phrasing exactly, and added a note to the commentary pointing back to
5:2-3 so the parallel is explicit.

## Tense audit against the actual Greek — Ephesians (66/66 checked, clean)

Same method, against `tools/data/70-Eph-morphgnt.txt`. 40 of 66 entries
flagged. **No fixes needed** — if anything this book is where the project's
handling of the perfect tense is at its best, since Ephesians is full of
Wuest's signature territory (positional truth, "by grace you have been
saved"): 2:5/2:8's "you have been in a saved state ... and you remain so"
and 4:18's "who have been permanently darkened ... who stand alienated"
both nail the perfect's completed-action-with-abiding-result force exactly.

## Tense audit against the actual Greek — Philippians (52/52 checked, clean)

Same method, against `tools/data/71-Php-morphgnt.txt`. 28 of 52 entries
flagged. **No fixes needed.** Notably clean handling of *hyparchō*
(ὑπάρχω) at 2:6 — "who, **continuing to subsist** in the outward expression
of God" — which is the classic Wuest crux verse: *hyparchō* implies a prior,
continuing essential state, not the plain copula *eimi* would give, and the
distinction is preserved correctly. *Peithō*'s (πείθω) perfect participle
also recurs three times (1:6, 1:14, 1:25) and gets the same "settled
persuasion/conviction" treatment every time — the kind of same-verb
consistency Romans 13:2 and Galatians 6:13 missed.

## Tense audit against the actual Greek — Colossians (44/44 checked, clean)

Same method, against `tools/data/72-Col-morphgnt.txt`. 26 of 44 entries
flagged. **No fixes needed** — this book has some of the most consistent
perfect-tense handling in the whole corpus: 1:16's "stand created," 1:23's
"having been placed on a foundation with the present result that you stand
firmly grounded," 2:10's "having been completely filled full, with the
present result that you stand in a state of fulness," and 4:2's "I have
been bound and remain bound" all spell out the completed-action-with-
abiding-result force explicitly rather than leaving it implicit.

## Tense audit against the actual Greek — Titus (21/21 checked, clean)

Same method, against `tools/data/77-Tit-morphgnt.txt`. 19 of 21 entries
flagged. **No fixes needed** — 1:15's "have been defiled" and 3:11's "has
been twisted out of joint ... standing self-condemned" both handle the
perfect correctly.

## Tense audit against the actual Greek — Hebrews (155/155 checked, clean)

Same method, against `tools/data/79-Heb-morphgnt.txt`. 104 of 155
entries flagged — Hebrews is grammatically dense and heavy on the perfect
tense (its whole argument leans on completed-with-abiding-result
theology). **No fixes needed.** 10:10's "we have been made holy, and stand
holy still," 12:2's "has sat down and remains seated," and 13:23's "has
been set free and remains so" are all excellent, precise handling of
exactly the tense the book's argument depends on most.

## Tense audit against the actual Greek — 1 & 2 Timothy (42 + 35 checked, clean)

Same method, against `tools/data/75-1Ti-morphgnt.txt` and
`tools/data/76-2Ti-morphgnt.txt`. 27 of 42 and 24 of 35 entries flagged
respectively. **No fixes needed in either.** 2 Timothy in particular is a
standout: 2:19's "God's firm foundation has stood, and stands now," 4:7's
"I have fought the good fight to its finish, and I am resting now in its
victory," and 4:8's "who have set their love, and kept it set, on his
appearing" all handle the perfect with real precision.

This closes out the audit of every book currently compiled into
`data/weust.js` (10 of 16): **3 fixes total across 1,077 entries** — Romans
5:17, Romans 13:2, Galatians 6:13 — the rest (Mark, Ephesians, Philippians,
Colossians, Titus, Hebrews, 1 & 2 Timothy) came back clean.

## Tense audit against the actual Greek — 1 Peter (46/46 checked, clean)

Same method, against `tools/data/81-1Pe-morphgnt.txt`. 39 of 46 entries
flagged. **No fixes needed.** 1:4's "having been kept — and continuing to
be kept — in the heavens for you" is a standout perfect-participle
rendering. Compiled into `data/weust.js` for the first time (see below).

## Tense audit against the actual Greek — 2 Peter (21/21 checked) — and a real content gap, not just tense

Same method, against `tools/data/82-2Pe-morphgnt.txt`. 18 of 21 entries
flagged. This one turned up something more serious than a tense miss:
**the "2 Peter 2:20–22" entry's translation and commentary had no content
at all for verse 20** — the "escaped the pollutions of the world... again
entangled... latter end worse than the beginning" clause was entirely
absent, jumping straight from the verse-19 material to verse 21's "it would
have been better." The label range said 20–22; the actual English covered
only 21–22. This is a coverage gap, not a tense error — worth naming
plainly since it's a different failure mode than what this audit was
built to catch (label-range coverage was verified project-wide already;
whether the *content* inside a multi-verse entry actually covers every
verse in its own range was not).

Fixed by writing verse 20's translation ("For if, after they have escaped
the defilements of the world... their last state has become worse for them
than the first") and adding commentary on its two perfect-tense verbs:
*hēttōntai* (ἡττῶνται, "have been overcome") — the same verb, same tense,
Peter used one verse earlier of the false teachers' own condition, a
deliberate echo the original entry's commentary never mentioned because
the clause using it wasn't there — and *gegonen* (γέγονεν, "has become"),
perfect rather than a static "is," meaning a completed, lasting
deterioration. While fixing this, also caught and fixed the adjacent
inconsistency this parallel exposed: 2:19's *hēttatai* (same lemma, same
perfect tense) had been rendered as a flat present, "is overcome," instead
of matching 2:19's own "has been enslaved" — fixed to "has been overcome."

**This raises a real question for the rest of the corpus:** if one
multi-verse entry can silently drop a whole verse's content while still
carrying a label that claims to cover it, others might too. The tense
audit only surfaces this by accident (a flagged verb pointing at a clause
that turns out not to exist in the translation) — it doesn't systematically
check for it. **Not yet done: a dedicated content-completeness sweep**
(comparing each multi-verse entry's actual English content against every
verse in its claimed range, independent of tense) across all 16 books.
Worth doing as a follow-up, flagged here rather than attempted mid-audit.

Compiled into `data/weust.js` for the first time (see below).

## Content-completeness audit — Mark (a real structural bug, found via the tense audit)

While auditing Mark's tenses, a heuristic scan (chars of English translation
per verse in each multi-verse entry) turned up something the tense audit
wasn't built to catch: several entries whose `label` claimed a verse range
its `translation` didn't actually deliver in full. The clearest case,
**2 Peter 2:20–22, was missing verse 20's content entirely** — the label
promised three verses, the English delivered two. Checking whether this was
isolated led to a full verse-by-verse comparison of every Mark entry
against `KJV.json`, which found the problem was systemic, not a one-off.

Two distinct failure modes turned up, at roughly even odds:

1. **Mislabeling** — an entry's content already covered more verses than
   its label named (e.g. "Mark 9:11" was labeled as one verse but its
   translation already covered 11–13 in full). Mechanical to fix: correct
   the label and `c1`/`v1`/`c2`/`v2`, no new writing. About 20 entries had
   this, plus a handful with content shuffled to the *wrong* label
   entirely (e.g. "Mark 6:38" actually contained verses 39–40's content,
   leaving the real verse 38 — the "how many loaves? … five, and two
   fish" exchange — with no entry of its own anywhere).
2. **Genuine gaps** — verses truly absent from every entry, no matter how
   generously neighboring entries were read. About 60 verses across some
   50 separate passages, ranging from single narrative-connector clauses
   to entire missing pericopes: the Transfiguration's own description
   (9:1-3: "some standing here shall not taste death," Jesus leading
   Peter/James/John up the mountain, his raiment becoming shining white),
   the temple-cleansing's own action (11:15-16 — Jesus's *words* about the
   den of robbers were present, but not the actual overturning of tables),
   the Sanhedrin's "guilty of death" verdict (14:64), Peter warming himself
   by the fire before his denials (14:53-56), the full third passion
   prediction (10:33-34), the opening of the Olivet discourse (13:1-8, "who
   gave you this authority," "many will come in my name saying I am he"),
   the Passover binding and Pilate's first question (15:1-2), the women
   arriving at the empty tomb (16:1-4), and the closing commission and
   ascension (16:14-15, 19-20). A few flagged verses (9:44, 9:46, 11:26)
   turned out to be legitimate: the project's SBLGNT/MorphGNT source text
   doesn't print them at all, following the standard critical-text
   judgment that they're later scribal duplications — nothing to translate
   there, correctly reflected as absent.

Fixed all of it: relabeled every mislabeled entry, split apart every entry
that had drifted across the wrong verse boundaries, and drafted original
translation (and commentary, for the passages carrying real grammatical
weight) for every genuinely missing verse — independently authored from
the SBLGNT/MorphGNT text the same way the rest of this project always has
been, not reconstructed from Wuest's own book. Mark went from 364 entries
to 426. Re-verified against `KJV.json`: **675 of Mark's 678 verses now
have real translated content**, the other 3 being the confirmed textual
omissions above — full, accounted-for coverage for the first time.
Re-spliced into `data/weust.js` and confirmed live via `weustVerseLookup()`
(1,206 entries across 12 books, zero structural errors).

**This changes what "done" means for the other 15 books.** The original
"16 of 16 books done" milestone verified label-range coverage and JSON
structure, but never checked whether a multi-verse entry's *content*
actually delivered everything its own label claimed. Romans, Galatians,
Ephesians, Philippians, Colossians, Titus, Hebrews, 1 & 2 Timothy, and 1
Peter have all had a tense audit pass, which incidentally exercises a lot
of entries closely — but none has had this specific completeness check run
against it the way Mark just did. Worth doing before calling any of them
complete.

## Content-completeness audit — Romans (156 -> 189 entries)

Same method as Mark: verse-by-verse against `KJV.json`. Found 90 of 433
verses uncovered, about the same 21% rate as Mark and the same two-part
mix — roughly half mislabeling (e.g. "Romans 11:23" already contained all
of verses 23-29 in full, just labeled as one verse; "Romans 10:18" already
covered 18-20), half genuine gaps. The genuine gaps included some of the
letter's best-known material: 1:1 (Paul's own opening self-description),
3:19-20 and 3:27-28 ("by the law is the knowledge of sin," "justified by
faith without the deeds of the law"), 4:1-5 (Abraham believing God,
credited as righteousness — the Genesis 15:6 citation the whole chapter
argues from), 5:1 ("being justified by faith, we have peace with God"),
6:3-4 (buried with him by baptism into death), 9:1-9 (Paul's anguish over
Israel, and "Christ, who is over all, God blessed forever"), 12:1 ("present
your bodies a living sacrifice"), 13:1 and 13:9-14 (submission to
authorities; love as the fulfillment of the law, "put on the Lord Jesus
Christ"), and 16:1-4 (the commendation of Phoebe).

Fixed all of it the same way: relabeled the mislabeled entries, drafted
original translation and commentary for every genuine gap from the tagged
Greek (`tools/data/66-Ro-morphgnt.txt`). Romans now has verified content
for all 433 of its verses — no textual-variant exceptions this time, unlike
Mark. Re-spliced into `data/weust.js`.

## Content-completeness audit — Galatians (142 entries, essentially clean) and Ephesians (66 -> 88 entries)

Galatians came back almost perfect: only 1 of 149 verses uncovered
(1:11), and that turned out to be a pure mislabel — "Galatians 1:10"
already had 1:11's content, just needed its range extended.

Ephesians was the opposite: 61 of 155 verses uncovered (39%, well above
Mark's and Romans's ~21%). A careful pass found the same two-part mix
again, including some deceptive mislabels this time — "Ephesians 1:18"
and "1:21" each silently absorbed two more verses into a long flowing
paragraph, and "6:18" absorbed verse 19, without their labels growing to
match. The genuine gaps included the letter's opening greeting and
blessing (1:1-4), "you He made alive, who were dead in trespasses and
sins" (2:1), the whole "no longer strangers and foreigners" section
(2:17-22), Paul's mystery-of-Christ digression (3:1-5, 7-8, 11-12, 14-15),
the doxology "unto him who is able to do exceeding abundantly" (3:20-21),
"he gave some, apostles; and some, prophets..." (4:9-12), the body-growth
verses (4:15-16), "be ye imitators of God" (5:1-4), "wives, submit
yourselves unto your own husbands" (5:22-23), the "great mystery" verse
about Christ and the church (5:32-33), and "children, obey your parents"
(6:1-3). Fixed all of it; both books now have verified content for every
verse. Re-spliced into `data/weust.js`.

## Content-completeness audit — Philippians (52 -> 56 entries)

32 of 104 verses uncovered at first pass, but most turned out to be the
same "long flowing paragraph absorbed extra verses without the label
growing" mislabel found in Ephesians — six entries needed nothing but a
wider label (e.g. "Philippians 2:8" already held verses 8-15 in full,
including "at the name of Jesus every knee should bow" and "work out your
own salvation with fear and trembling"). One entry ("3:4") had swapped
content entirely: it was labeled as verse 4 but actually held verses 5-6,
leaving the real verse 4 ("though I myself might also have confidence in
the flesh...") with no entry until now. Genuine new gaps were smaller than
they first looked: 1:3-4, half of 3:17-21 (verse 18's "enemies of the
cross of Christ" clause, the rest already present under a too-narrow
label), 4:6-7 ("be careful for nothing... the peace of God, which passes
all understanding"), and 4:15-16. Fixed all of it; every verse now has
verified content. Re-spliced into `data/weust.js`.

## Content-completeness audit — Colossians (44 -> 48 entries)

27 of 95 verses uncovered at first pass; the same mislabel pattern
accounted for most of it again, including one that crossed a chapter
boundary — "Colossians 3:23–25" already held the opening of chapter 4
("Masters, grant your slaves what is just and fair...") and is now
labeled "Colossians 3:23–4:1" (the re-splice script's label parser had to
be extended to handle a range that spans chapters, not just verses within
one). Five more single-verse labels each already held two to five more
verses than claimed. Genuine new gaps were just four: 1:1-2 (the opening
address), 2:1-3, 3:1 ("if ye then be risen with Christ..."), and 4:10-13
(the closing greetings from Aristarchus, Mark, Justus, and Epaphras).
Every verse now has verified content. Re-spliced into `data/weust.js`.

## Content-completeness audit — Titus (21 -> 22 entries) and Hebrews (155 -> 211 entries)

Titus was almost perfect: only the opening greeting (1:1-4) was missing
entirely, added as one new entry.

Hebrews was the largest and most demanding of the completeness passes so
far: 139 of 303 verses uncovered (46%). Unlike the epistles audited
before it, Hebrews' existing entries were already tightly scoped to their
own verse ranges — almost no mislabeling to find — which meant nearly all
139 verses were genuinely never covered before. This is the book's dense
theological argument, not scattered filler: the opening Christology
(1:1, 1:3-4, 1:6-10 — the catena of OT citations establishing the Son's
superiority to angels), the warning passages (2:1-2, 3:7-15, 6:1-6's "it
is impossible... to renew again to repentance," 10:26-29), the whole
Melchizedek argument (7:1-27 in pieces), the new-covenant citation from
Jeremiah in full (8:6-13), the sustained argument for Christ's once-for-all
sacrifice (9:11-25, fifteen verses in one entry — the theological core of
the letter), the faith chapter's own definition ("now faith is the
title-deed of things hoped for, the proof of things not seen," 11:1), and
the closing exhortations and benediction (13:1-25 in pieces). Drafted all
of it fresh from `tools/data/79-Heb-morphgnt.txt`, following the same
tense-attentive style established across the rest of the corpus. Both
books now have verified content for every verse. Re-spliced into
`data/weust.js` and confirmed live (1,326 entries across 12 books, zero
structural errors).

## Content-completeness audit — 1 Timothy (42 -> 58 entries) and 2 Timothy (35 -> 46 entries)

1 Timothy: 41 of 113 verses uncovered (36%), 2 Timothy: 31 of 83 (37%) —
both closer to Hebrews' pattern than the earlier epistles: entries were
already tightly scoped, so almost none of it was mislabeling, nearly all
genuine gaps. 1 Timothy's included the opening greeting (1:1-4), the call
to prayer "for kings, and all that are in authority" (2:1-2), the
women-in-the-assembly instructions (2:9-12), the overseer and deacon
qualifications in pieces (3:1, 3:4-5, 3:8-9, 3:12-15), the "spirits and
doctrines of demons" warning (4:1-5), and the widow/elder instructions in
chapter 5. 2 Timothy's included its own opening (1:1-2), "life and
immortality to light through the gospel" (1:10-11), Timothy charged to
entrust the faith to "faithful men who shall be able to teach others also"
(2:1-4), the perilous-times catalogue (3:1-7), and "all scripture is
God-breathed" (3:14-17, the theopneustos verse). Both books now have
verified content for every verse. Re-spliced into `data/weust.js`.

**Remaining work:** 1 Peter still needs this completeness audit. 1-3 John
and Jude still need the tense audit, this completeness audit, and the
compile step. Next up: 1 Peter.

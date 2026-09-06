# Voice of Jesus — KJV recast into first-person narration — status

## What this is

The KJV text of the books Wuest covered (see `Weust/STATUS.md`), recast so that
Jesus is narrating His own gospel and His own letters in the first person —
the same idea as Elmer Towns' *The Bible by Jesus*, but built the opposite way:
Towns freely paraphrases; this keeps the actual KJV wording and shifts only
what person/voice requires. **No text of Towns' book is reproduced or
paraphrased anywhere here** — his chapters were read only to understand the
technique (how he decides what stays third-person and what becomes "I"),
exactly as the Weust files are informed by Wuest's word selection without
quoting his prose.

Each file is `[{ "label": "Book C:V", "text": "..." }, ...]`, one entry per
verse, full coverage of the book — this is a retext of the whole book, not a
commentary on selected verses.

## The rules (apply to every remaining book)

1. **Narrator's "he/him/his/[Name]" for Jesus becomes "I/me/my."** Verb
   conjugation follows: `saith`→`say`, `hath`→`have`, `doth`→`do`, `is`→`am`,
   third person → first throughout.
2. **Jesus's own quoted speech is untouched** — it is already first person.
3. **Other people's quoted speech about Jesus stays third-person** — a
   demon's cry, a crowd's question, a high priest's mockery, an angel's
   announcement. It is their words, not His, so it keeps whatever pronoun
   they used. This is the single most load-bearing rule; most of the verses
   that look "unconverted" on a `grep` for "Jesus" or "himself" are correct
   for this reason (checked verse-by-verse in Mark, all correct).
4. **Prophecy or address spoken *to* Jesus stays "thou/thee/thy"** — the
   Father's voice at the baptism and transfiguration, a demon begging Him,
   Peter addressing Him. It is another voice speaking to Him, not Him
   narrating Himself.
5. **Group "they" becomes "we"** when Jesus was one of the group being
   described (traveling with the disciples, eating, entering a house) —
   otherwise a sentence like "she ministered unto them" reads as if Jesus
   wasn't in the room He was just described entering. "They" that refers to
   a crowd, opponents, or any party Jesus was not part of stays "they."
6. **"The Son of man" (and "the Son," Mark 13:32) merges into "I, the Son of
   man"** when it is a direct statement about Jesus's own fate or identity
   ("the Son of man must suffer," "is Lord of the sabbath," "shall be
   delivered"). It stays third-person when it is the subject of a parable
   *simile* — "the Son of man **is as** a man taking a far journey" (Mark
   13:34) launches a told story the way "the kingdom of God is like a grain
   of mustard seed" does, so it is left alone like any other parable.
7. **Parable content is left exactly as told** — the sower, the vineyard
   owner and his son, the bridegroom, the strong man's house. These are
   illustrations Jesus tells in the third person; converting the story's own
   characters to "I" would break the parable, not honor the voice.
8. **A scripture quotation cited as fulfilled stays as quoted** — e.g. Mark
   15:28, "the scripture was fulfilled, which saith, And he was numbered
   with the transgressors" — the citation is preserved text, not narration.
9. **Titles used in indirect/scripted speech ("say ye that the Lord hath
   need of him," "The Master saith, Where is the guestchamber") are left
   as the title** rather than merged to "I" — these are instructions for
   what someone else should go say, not Jesus's own narration.

## Progress

| Book | Verses | Status |
|---|---:|---|
| Mark | 678 | done |
| Romans | 433 | done |

14 more books remain, in the order Wuest covered them: Galatians, Ephesians,
Philippians, Colossians, Titus, Hebrews, 1 Timothy, 2 Timothy, 1 Peter,
2 Peter, 1 John, 2 John, 3 John, Jude.

## Epistle rules (Romans) — a different problem than the Gospels

Mark's rules (1-9 above) are Gospel-narrative rules: third-person "he" about
Jesus becomes "I." An epistle is the **opposite** starting shape — Paul
already writes Romans in his own first-person voice ("I thank my God," "I
purposed to come unto you"), so the move is not always the same direction.
Worked out chapter by chapter against Towns, checking alignment each time:

1. **Paul's personal/biographical "I" (plans, thanks, prayers, his own
   history) demotes to third person "Paul."** *"I thank my God"* → *"Paul
   thanked my Father."* *"I am not ashamed of the gospel"* → *"Paul was not
   ashamed."* Concentrated in 1:8-15 and all of 15:14-16:27 (travel plans,
   greetings) — matches Towns exactly, verified against his actual text.
2. **Paul's doctrinal "I" (teaching, answering objections) stays first
   person — now Jesus teaching, not Paul.** The Romans 3 diatribe ("what
   advantage then hath the Jew?") stays in Jesus's own voice through the
   answers, matching Towns' *"This is My answer..."* Coherence is the test
   where it's ambiguous: 10:1's *"my heart's desire...for Israel...that they
   might be saved"* stays Jesus's own longing (matches Towns, *"I long for
   all Jewish people to be saved"*) even though grammatically it was Paul's
   personal prayer, because nothing about it is Paul-specific the way *"I
   could wish myself accursed"* (9:3, kept as Paul — the statement doesn't
   cohere as something Jesus would say) or *"I also am an Israelite...of the
   tribe of Benjamin"* (11:1, a Paul-only biographical fact) do.
3. **"God" converts to "my Father" almost everywhere** — the single most
   pervasive move in the whole letter, and Towns' own most consistent habit
   (*"My Father promised," "My Father's righteousness," "My Father sent
   Me"*). Exceptions, where forcing "my Father" into the slot breaks an
   idiom without adding meaning (same logic as "Son of man" staying a title
   in Mark): the exclamation **"God forbid"**; fixed covenant-title phrasing
   like **"the God of the Jews...of the Gentiles"** and **"one God"**
   (monotheistic creedal formula); and **direct Old Testament quotations**
   (rule 6 below), where "God"/"the LORD" is the quoted text's own word.
4. **Third-person references to Christ ("his Son," "Jesus Christ," "the
   Lord") convert to "I/me/my,"** same direction as Mark. Verified: only 2
   residual "Jesus Christ" instances survive across all 433 verses, both in
   the opening salutation (1:3, 1:7) where Jesus names Himself once,
   deliberately, the way Mark 1:1 does.
5. **Romans 7:7-25, the "wretched man" passage, converts Paul's
   illustrative "I" to "thou/thee/thy"** rather than to Jesus's "I" or to
   "Paul" — a third pattern, confirmed with the user before building it.
   Towns does the same thing: turns Paul's universal struggle-under-the-law
   into Jesus addressing the reader's own struggle directly (*"Who can
   rescue you from your slavery to sin? I, the Lord Jesus, can deliver
   you"*). Requires reworking KJV verb forms throughout (*I was* → *thou
   wast*, *I found* → *thou foundest*, *I died* → *thou diedst*) while
   keeping the vocabulary. At 7:25 Jesus's own voice breaks back in with the
   answer, matching Towns' structure.
6. **Direct Old Testament quotations stay exactly as quoted**, regardless
   of who they name — "God," "the LORD," even "him" referring to Christ
   within a quotation (9:33, "whosoever believeth on him"). The citation is
   preserved text, not narration, same rule as Mark's scripture citations.
   Also covers the prophet-as-speaker construction ("Esaias saith," "he
   [Hosea] saith in Osee") — "he" there is the prophet quoting God, not God
   himself, and stays unconverted (caught and fixed once at 9:25, where it
   had wrongly become "my Father saith").
7. **Imperatives/ethical commands (chapters 12-14 especially) stay direct
   commands**, presented as Jesus speaking through the letter — same as
   Titus. "God" still converts to "my Father" inside them.

Verification run on Romans: 433/433 verses present, chapter-by-chapter
counts match `KJV.json` exactly, zero unintended residual "God" (every
survivor is an idiom, a title, a quotation, or the deliberate "my Father,
the God of X" combined form), only 2 residual "Jesus Christ" (both the
opening self-naming).

## Verification run on Mark

- 678/678 verses present, chapter-by-chapter counts match `KJV.json` exactly.
- Every surviving instance of the name "Jesus" (6 total) and of third-person
  "himself" (11 total) in the output was checked and is another speaker's
  words about Him, not a missed narrator reference.

## Site integration — done, as its own translation

Not a tab inside the KJV reader after all: it lives as **"The Jesus Bible,"**
a fourth translation card (tx.04) alongside Mak/Illumination/KJV in the Bible
section, built from `data/jesus.js` (`JESUS_BOOKS`, `JESUS`, `JESUS_INTROS`)
— generated straight from this directory's `mark.json`/`romans.json`, same
shape as `KJV` (one verse per entry), so it reuses the existing
`buildIllumChapter` reader with no new rendering code. `CORPUS.jesus` wires
it in; `isVerseTx` includes it; the testament filter is hidden (NT-only
coverage so far, like Mak). Each finished book gets a short intro in Jesus's
own voice (`JESUS_INTROS`, e.g. *"I sent Mark..."*, *"I sent Paul to set in
order..."*) composed from this project's own existing AUTHOR/PURPOSE/THEMES
fields per book, not from Towns' wording — there is deliberately no separate
whole-translation intro page, only the per-book ones.

Coverage is partial by design (2 of 66 books): the "jump to this verse in
another translation" popup, search indexing, and reading-plan generation are
left untouched rather than half-wired against an incomplete corpus.

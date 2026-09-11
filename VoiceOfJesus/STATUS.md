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
| Galatians | 149 | done |
| Ephesians | 155 | done |
| Philippians | 104 | done |
| Colossians | 95 | done |
| Titus | 46 | done |

9 more books remain, in the order Wuest covered them: Hebrews, 1 Timothy,
2 Timothy, 1 Peter, 2 Peter, 1 John, 2 John, 3 John, Jude.

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

## Fixed after the fact: collective "we/us/our" wrongly self-included Jesus

A rule discovered while building Galatians (see below) exposed a real gap in
the original Romans pass, done in an earlier session before that rule
existed: roughly 60 verses left Paul's collective "we/us/our" — describing
the shared condition of sinners in need of grace — unconverted, which put
statements in Jesus's own mouth that are false of Him. *"While **we** were
yet sinners, I died for us"* (5:8) has Jesus calling Himself a former
sinner. *"**We** are buried with me... if **we** be dead with me, **we**
believe that **we** shall also live with me"* (6:4-8) has Jesus buried with
Himself. *"**We** ourselves groan... waiting for the adoption... the
redemption of **our** body"* (8:23) has Jesus's own body still awaiting
resurrection and Jesus needing adoption, when He is the natural Son, not an
adopted one. *"Who also make intercession for **us**"* (8:34) has Jesus
interceding for Himself. Caught on a user-requested theological review of
all three finished books, not by the verse-count/residual-word checks,
since none of those check pronouns without an explicit "God"/"Christ" noun
attached.

Checked against Towns' actual Romans (`Chapter046.html`) before fixing, and
his practice is exactly the fix: he addresses the reader directly as "you"
throughout every one of these passages — *"while you were a great
sinner"* (5:8), *"you were buried with Me"* (6:6), *"you too groan... your
body"* (8:23), *"intercede for you"* (8:34) — never self-inclusive "we" for
Jesus. Chapter 16's greetings he keeps entirely third-person ("Paul... he...
his"), confirming a handful of smaller misses there too (*"our sister"* →
*"his sister"*, *"our helper"* → *"his helper"*, matching Paul's own
perspective rather than the narrator's).

Fixed by converting the self-inclusive "we/us/our" to direct "ye/you/your"
address (or, for a few of Paul's own personal asides that were missed
entirely, to third-person "Paul" — 1:5's apostolic call, 3:8's "as we be
slanderously reported"), and converting hortatory "let us" to a direct
imperative ("let us not judge one another" → "judge not one another"),
matching the Galatians precedent throughout. One deliberate exception left
alone: 3:5's "our unrighteousness" sits inside the KJV's own "(I speak as a
man)" bracket, voicing a hypothetical objector rather than the narrator's
own claim — Towns handles the same diatribe (3:7-8) by explicitly quoting
it as someone else's argument, so the existing parenthetical already does
the same job and the pronoun was left as-is. Also left alone throughout:
rhetorical "what shall we say"/"we know"/"we conclude" formulas (no false
claim about Jesus), Abraham/Isaac as "our father" (true of Jesus too by
physical descent), and direct Old Testament quotations (8:36, 9:29, 10:16 —
citation rule as always).

Re-verified after the fix: still 433/433 verses, chapter counts unchanged;
22 residual we/us/our instances remain, every one now checked and
deliberate (the categories above); re-spliced into `data/jesus.js` and all
41 Jesus Bible destinations render live with zero errors.

## A second pass found: dangling "Who/Whom" left a first-person antecedent

Requested by the user as a further read-through after the we/us fix.
Scanned every verse across all three books that opens with "Who," "Whom," or
"Which" (the KJV's own device for continuing a thought across a verse
break) and checked whether its antecedent — the previous verse's final
noun — had been converted to first person. Three had: **Romans 3:25**
("Whom my Father hath set forth..." following 3:24's "...redemption that is
in **me**") and **Romans 5:2** ("By whom also ye have access..." following
5:1's "...through **me**, your Lord") both opened a new verse-paragraph with
a third-person relative pronoun pointing back at a first-person "me" one
verse up — grammatically broken once read as separate paragraphs, since
"whom" has no visible antecedent of its own person. **Galatians 1:4** had
the same shape ("Who gave myself..." following 1:3's "...and from **me**")
though there the internal wording ("myself," "I might deliver") was already
first person, just introduced by a third-person "Who."

Fixed by restructuring each into a self-contained first-person clause
instead: 3:25 → *"My Father hath set forth me to be a propitiation..."*
(active SVO, matches Towns' own paraphrase of the same verses — *"My Father
sent Me to take the punishment for your sins"*); 5:2 → *"By **me** also ye
have access..."* (one-word swap); Galatians 1:4 → *"**I** gave myself for
your sins..."* (one-word swap). Checked every other verse-initial
"Who/Whom/Which" in all three books (18 more instances) — every other one's
antecedent was already third-person (a named person, "they," "the
Gentiles," a title like "my Father"), so no further mismatch exists.

Also re-scanned all three books for "is dead"/"am dead" and the same family
of idioms ("is/am come, risen, gone, fled, departed") that caused the
Galatians 2:21 error: every remaining instance either refers to someone
other than Jesus (correctly left alone) or refers to Jesus's own
resurrection, which is genuinely true of Him — no further instance of a
false present-state claim.

## Epistle rules (Galatians) — confirms Romans, adds two patterns

Read against Elmer Towns' actual Galatians chapter (his book treats the
whole epistle as one continuous piece rather than six files, but marks each
KJV chapter's start inline, so it was read complete before any verse was
written, then re-checked chapter by chapter as each was drafted). His
technique confirms every Romans rule above and adds:

1. **Collective "we/us/our" describing the shared condition under the law or
   in Christ converts to "ye/you/your"** rather than staying plural-Paul or
   becoming Jesus's own "we." *"Our liberty which we have in Christ Jesus"*
   (2:4) → *"your liberty which ye have in me."* *"The law was our
   schoolmaster to bring us unto Christ"* (3:24) → *"the law was your
   schoolmaster to bring you unto me."* Matches Towns turning the same verses
   into direct "you" address (*"taking away the freedom you all have in
   Me"*). Hortatory-subjunctive *"let us"* becomes a direct imperative
   instead of an odd *"let ye"* — *"let us not be weary in well doing"*
   (6:9) → *"be ye not weary in well doing."*
2. **Paul's own quoted speech to a named historical figure stays his own
   words, not Jesus's** — 2:14's rebuke to Peter (*"If thou, being a Jew,
   livest after the manner of Gentiles..."*) is introduced by *"Paul said
   unto Peter"* and keeps its own "thou," the same way Mark leaves another
   speaker's quoted words alone (rule 3). But the argument Paul makes to
   Peter turns universal by 2:15, and Towns pivots there too — from that
   point through 2:21 the whole passage converts to Jesus's own direct
   address (*"Ye are crucified with me... yet not ye, but I live in
   you"*), matching Towns' block-quote of the same verses in Jesus's voice
   (*"You were crucified with Me... Now I live within you"*).

"God" converts to "my Father" by the same rule as Romans, with the same
kind of exceptions: the idiom **"God forbid"** (2:17, 3:21, 6:14, all kept);
the monotheistic creedal formula, here **"God is one"** (3:20, kept, same
logic as Romans' "one God"); and the fixed covenant phrase **"the Israel of
God"** (6:16, kept, same logic as Romans' "the God of the Jews"). No direct
Old Testament quotation in Galatians carries the word "God," so that
exception never comes up.

Verification run: 149/149 verses present, chapter-by-chapter counts match
`KJV.json` exactly (24/21/29/31/26/18). Every residual "God" (5 total) is
one of the three listed exceptions; zero residual "Christ" or "Jesus"
anywhere — every explicit reference converted; zero residual "we/us/our."
Every verse carrying "Paul" by name falls inside the autobiographical
stretches (1:1-24, 2:1-14, 4:11-20, 5:2-3/10-12/21, 6:11) with no leak into
the doctrinal first-person sections, and every surviving first-person
pronoun inside those same autobiographical stretches checks out as Jesus's
own self-reference (*"my Father," "me," "my brother"*), never a missed
Paul "I."

## Epistle rules (Ephesians) — confirms Galatians, adds two patterns

Read against Elmer Towns' actual Ephesians chapter (`Chapter050.html` in his epub, "I Am Jesus —
Who Lives in You," based on his letter to the Ephesians) complete before any verse was written, then
re-checked chapter by chapter as each was drafted. His technique confirms the Romans/Galatians rules
and adds two:

1. **The trinitarian confession at 4:4–6 ("One body... one Spirit... One Lord, one faith, one
   baptism, One God and Father of all") stays entirely unconverted**, the same way "God is one"
   (Galatians 3:20) and "one God" (Romans) were kept — a fixed creedal formula, not narration. Towns
   handles the same verses by switching to a collective voice for the Godhead ("We, the Godhead, are
   One Lord over believers... There is One God and Father who is in each of you") rather than folding
   it into Jesus's ordinary "I"/"my Father" pattern, confirming this passage needed its own exception
   rather than the standard conversion.
2. **Ephesians keeps Paul in third person far more than Romans or Galatians did.** Because the letter
   itself already frames Paul as "the prisoner of Jesus Christ" (3:1) and "the prisoner of the Lord"
   (4:1) rather than arguing doctrine in his own first-person voice the way Romans 1–11 does, nearly
   every stretch of Paul's own "I" — his ministry to the Gentiles (3:1–13), his prayer posture
   (3:14), his plea for boldness (6:19–20), and the news of Tychicus (6:21–22) — demotes to
   third-person "Paul," matching Towns' own narration of the same material almost entirely in the
   third person ("Paul became a prisoner of Rome because he was first captured by Me... He was given
   a special task of evangelizing the Gentiles").

One judgment call, made where Towns and the KJV both leave the antecedent ambiguous: **4:3's "by
revelation he made known unto me the mystery"** could grammatically be either my Father or Christ
revealing Himself to Paul (as on the Damascus road). Towns resolves it as Christ speaking in the
first person — *"I gave Paul the revelation of his ministry to the Gentiles"* — so `he made known`
became `I made known` here, matching Towns rather than defaulting to the more common "my Father
reveals" pattern used everywhere else in the chapter.

A second judgment call: **4:8's citation ("he saith, When he ascended up on high, he led captivity
captive...") stays quoted and unconverted**, same citation rule as Mark 15:28 and Ephesians 5:14 —
but **4:9–10, Paul's own commentary explaining the citation, converts to Jesus's first-person voice**
("Now that I ascended, what is it but that I also descended... I that descended am the same also
that ascended..."), because Towns treats that commentary as Jesus's own explanation rather than part
of the citation: *"The phrase 'Christ ascended up' means I returned to heaven after I first came
down to live and die on earth. Then I descended into the lower parts of the earth—hell—to lead Old
Testament saints to heaven."* The line between quoted citation and Paul's commentary on it is where
the conversion starts, not the verse boundary.

"God" converts to "my Father" by the same rule as Romans/Galatians, with the trinitarian formula
(4:4–6) as the only new exception category — no "God forbid" idiom occurs in Ephesians, and no
direct Old Testament quotation carries the word "God." "Armour of God" (6:11, 6:13) and "word of
God" (6:17) both convert to "of mine"/"of my Father" respectively rather than joining the exception
list — Towns' own handling of the armor passage ("put on all the spiritual armor... Use every piece
of My spiritual armor") confirmed treating it as Christ's own armor, not a fixed phrase.

Every "Who/Whom/Which" verse-opener was checked against whether the previous verse's antecedent had
converted to first person (the Romans 3:25/5:2, Galatians 1:4 pattern) — six instances found
(1:14, 1:20, 1:23, 3:5, 4:19, 6:22), and in every one the antecedent was a third-person noun (the
Spirit, his power, the church, the mystery, "them"/Gentiles, Tychicus), not a converted first-person
pronoun, so none needed restructuring. Several verses *earlier* in the chain (1:7, 1:11, 1:13 twice,
2:21, 2:22, 3:12, 4:16) did open on a dangling "In whom"/"From whom" whose antecedent one sentence up
had just converted to "me" — each fixed the same way as the Romans/Galatians precedent, by swapping
the relative pronoun for a first-person "In me"/"From me" rather than restructuring the whole clause.

Verification run: 155/155 verses present, chapter-by-chapter counts match `KJV.json` exactly
(23/22/21/32/33/24). Only 2 residual "God"/"Christ" survive, both deliberate exceptions (the 4:4–6
creedal formula, and the 5:14 hymn citation "Christ shall give thee light"); zero residual "Jesus";
zero residual "we/us/our/ourselves"; zero false-present-state hits on the "is/am dead/come/risen/
gone/fled/departed" family.

## Epistle rules (Philippians) — confirms Ephesians, adds one pattern and one open question

Read against Elmer Towns' actual Philippians chapter (`Chapter051.html`, "I Am Jesus — The Source
of Joy," based on his letter to the Philippians) complete before any verse was written. His
technique confirms the Ephesians-established pattern (Paul stays third person almost everywhere —
his thanksgiving, his imprisonment circumstances, the Timothy and Epaphroditus news, and the
thank-you for the Philippians' gift in 4:10-20 are all narrated about "him," not spoken as Jesus's
own "I") and adds one new case:

1. **4:19 ("my God shall supply all your need... by Christ Jesus") converts to Jesus's own direct
   promise, not a reported statement of Paul's.** Towns makes this explicit: rather than narrating
   what Paul believed about provision, he has Jesus speak the promise directly — *"Now, I will care
   for your financial needs the same way I took care of Paul. It's all because of His glorious
   riches in Me."* This is the same kind of call as Ephesians 4:9-10 (Christ's own commentary breaking
   into what would otherwise be reported material) — the test each time is whether the content reads
   as Paul's own testimony/circumstance (stays "he") or as a truth Jesus is asserting about Himself or
   His Father (becomes "I"/"my Father").

One open question, resolved by grammatical necessity rather than a Towns citation: **4:1's "my
brethren... my joy and crown... my dearly beloved" and 3:1's opening address don't have a reporting
verb to hang a third-person conversion on** — "Therefore, his brethren... stand fast" isn't a
sentence. Where Paul's personal terms of address appear as bare vocatives with no "Paul said/asked"
frame around them, they were left as Paul's own unconverted words breaking through the narration
(the same treatment as Galatians' rule for Paul's quoted rebuke to Peter — his own words, not
converted), rather than forcing a restructure that would lose the direct address. Where a reporting
verb *is* present (4:2-3's "I beseech"/"I intreat"), the conversion to third person works normally
since "he besought"/"he intreated thee" is a complete indirect-speech sentence.

The kenosis passage (2:6-11) — the clearest place in this letter where Christ narrates His own
story — required restructuring three verse-openers that would otherwise dangle: 2:6's "Who, being in
the form of God" (antecedent "me" from 2:5) became "I, being in the form of my Father"; 3:21's "Who
shall change our vile body" became "I shall change your vile body," the same fix pattern as Romans
3:25/5:2 and Ephesians throughout. "Equal with God" at 2:6 converts to "equal with him" (my Father),
consistent with the rule that "God" in a Father/Son contrast means the Father specifically.

Two ambiguous-referent verses needed a named disambiguation rather than a pronoun, because the verse
names both Paul and someone else (Timothy or Epaphroditus) and a straight "he"/"him" swap for Paul's
"me" would collide with the other person's existing "he": 2:22 ("he hath served with me" — Timothy's
commendation) and 2:27 ("not on him only, but on me also" — Epaphroditus's illness). Both now name
"Paul" explicitly rather than reuse a pronoun already carrying the other person.

Verification run: 104/104 verses present, chapter-by-chapter counts match `KJV.json` exactly
(30/30/21/23). Only 1 residual "God" survives (3:19, "whose God is their belly" — describing the
false teachers' own appetite, not my Father, correctly left unconverted); zero residual
"Christ"/"Jesus"; zero residual "we/us/our/ourselves"; zero unresolved dangling "Who/Whom/Which"
verse-openers; zero false-present-state hits on the "is/am dead/come/risen/gone/fled/departed"
family.

## Epistle rules (Colossians) — confirms Philippians, adds two patterns

Read against Elmer Towns' actual Colossians chapter (`Chapter052.html`, "I Am Jesus — The Superior
One," based on his letter to the Colossians) complete before any verse was written. His technique
confirms the Ephesians/Philippians pattern (Paul, joined by Timothy, stays third person for nearly
all of his own material — the thanksgiving, the prayers, and every name in the chapter 4 greetings)
and adds two new patterns:

1. **The Christ-hymn (1:15–20) runs mostly in Jesus's own first-person voice**, the same treatment
   Philippians gave the kenosis passage — *"I am the image of my invisible Father... by me were all
   things created... I am before all things... I am the head of the body, the church."* Most
   "he"/"him"/"himself" describing Christ across the six verses converts to "I"/"me"/"myself,"
   including two dangling-relative-pronoun fixes matching the Romans/Ephesians pattern: 1:15's "Who
   is the image" → "I am the image," and 1:18's "who is the beginning" (following "he is the head,"
   itself already converted to "I") → "I am the beginning." **But the grammatical subject shifts back
   to the Father at 1:19** ("For it pleased the Father that in him should all fulness dwell") and
   stays there through 1:21 — "by him to reconcile all things unto himself" (1:20) means the Father
   reconciling all things to Himself, using Christ as the means ("by him"/"by his blood"), not Christ
   reconciling things to Himself. **A fresh re-read against Towns caught a real error here**: the
   first draft, on the momentum of vv15-18's "I" voice, wrongly converted 1:20's "unto himself" to
   "unto myself" and 1:21's "hath he reconciled" to "have I reconciled," making Christ the reconciler
   rather than the means. Towns' own paraphrase makes the correct reading explicit — *"By Me, God My
   Father reconciled all things to Himself. By My blood on the cross, My Father in heaven made
   peace"* — the Father is the subject throughout, Christ the agent. Fixed both verses to keep "my
   Father" as the acting subject (unconverted "himself"/"he") through 1:19-21, with only the
   means-phrases ("by him," "his cross," "his flesh") converted to first person. **The lesson: inside
   one hymn, the grammatical subject can shift away from Christ mid-passage even while Christ stays
   the topic — check who the verb's subject actually is at each verse, not just what the passage is
   about.**
2. **A named companion who happens to share Jesus's own name** — 4:11, "And Jesus, which is called
   Justus" — stays exactly as the KJV names him, unconverted. This is a real person distinct from
   the narrator, not a self-reference, and the KJV text already disambiguates it with "which is
   called Justus." First time this exact collision has come up in the project; the fix is simply to
   recognize it and leave it alone, same as any other named associate (Timothy, Epaphroditus,
   Tychicus).

One recurring judgment call, resolved the same way as Philippians 4:19: verses describing what "the
Godhead" is (2:9, "in me dwelleth all the fulness of the Godhead bodily") keep the word "Godhead"
unconverted — it names the divine nature/essence, a different word from "God" the Father-title, and
Jesus can say it of Himself without it needing "my Father" treatment (matching how Ephesians 4:4–6's
creedal formula was reasoned through).

4:18's closing signature ("The salutation by the hand of me Paul. Remember my bonds.") stays as
Paul's own directly-quoted words, unconverted first person — the same treatment Galatians gives
Paul's quoted rebuke to Peter, and confirmed by Towns keeping this exact line as Paul's own voice
too ("Paul signed the letter and told them, 'Pray for me because I am in chains.'").

Verification run: 95/95 verses present, chapter-by-chapter counts match `KJV.json` exactly
(29/23/25/18). Only 2 residual "God"/"Jesus" survive, both deliberate exceptions (2:9's "Godhead,"
4:11's other Jesus/Justus); zero residual "Christ"; zero residual "we/us/our/ourselves"; every
verse-initial "Who/Whom/Which" checked and resolves to a genuine third-person antecedent, none
dangling.

## Epistle rules (Titus) — confirms Colossians, adds the "God our Saviour" distinction

Read against Elmer Towns' actual Titus chapter (`Chapter057.html`, "I Am Jesus — The Hope of Eternal
Life," based on his letter to Titus) complete before any verse was written. Titus has a feature none
of the six books before it did: it applies the title "God our Saviour" to **both** the Father (1:3,
2:10, 3:4) **and** to Christ Himself (1:4's "the Lord Jesus Christ our Saviour," 2:13's "the great
God and our Saviour Jesus Christ," 3:6's "Jesus Christ our Saviour") as a deliberate rhetorical
parallel running through the letter. This meant the usual "God converts to my Father" rule could not
be applied by pattern-matching the word alone — every instance needed a verse-by-verse check of
which person it names.

1. **2:13's "the great God and our Saviour Jesus Christ" stays Jesus calling Himself "God,"** not
   converted to "my Father." Confirmed directly against Towns, who keeps it the same way: *"the
   glorious appearing... your Savior, and God."* This is the first case in the project of "God"
   correctly staying as a title Jesus applies to Himself rather than converting — distinct from the
   "Godhead" exception (Colossians 2:9, a different word for the divine nature) and from the
   creedal-formula exception (Ephesians 4:4–6).
2. **1:2's "which God, that cannot lie, promised before the world began" converts to Jesus's own "I,"**
   matching Towns exactly: *"I cannot lie. I promised this eternal life before the world was
   created."* Towns reads the promise-maker here as Christ, not the Father specifically, and the
   conversion follows him rather than defaulting to "my Father."
3. **A real mistake caught by the residual scan, not by reading**: three instances of "God our
   Saviour" describing the Father (1:3, 2:10, 3:4) were first drafted as "my Father, **our**
   Saviour" — but Jesus has no need of a Saviour, so "our" (which would include Him) is false in His
   own mouth. Fixed to "my Father, **your** Saviour" at all three, matching the same we/us-self-
   inclusion error class first found in Romans (see above) but this time in a title rather than a
   pronoun. Left correctly as "your Saviour" throughout (1:4, 3:6) elsewhere in the first draft — the
   scan caught the three places pattern-matching alone had missed.

Verification run: 46/46 verses present, chapter-by-chapter counts match `KJV.json` exactly
(16/15/15). Only 1 residual "God" survives (2:13, the deliberate Christ-as-God exception); zero
residual "Christ"/"Jesus"; zero residual "we/us/our/ourselves" after the fix above; zero unresolved
dangling "Who/Whom/Which" verse-openers.

## Verification run on Mark

- 678/678 verses present, chapter-by-chapter counts match `KJV.json` exactly.
- Every surviving instance of the name "Jesus" (6 total) and of third-person
  "himself" (11 total) in the output was checked and is another speaker's
  words about Him, not a missed narrator reference.

## Site integration — no longer its own translation; a KJV overlay instead

Originally shipped as **"The Jesus Bible,"** a fourth translation card (tx.04)
alongside Mak/Illumination/KJV. The user asked to remove that card and fold
its content into the KJV reader instead, reached by the small dot beside the
chapter title (`#kjvJesusDot`, `toggleKjvJesus()`) that was previously an
unused stand-in for the study/read switch on the KJV (see the shelved
Expositor's Translation notes below — that dot's old wiring to `toggleMode`/
`expMode` has been removed; it is fully independent now).

The dot appears only on a KJV chapter the Jesus Bible also covers (checked
per chapter via `jesusChapterForRef(ref)` against `JESUS`, called from
`loadIllum` — `updateKjvJesusDot`). Toggling it on swaps which verse text
`buildKjvSynopsisChapter` slices into the Synopsis outline-fold navigation:
the Jesus Bible's chapter (flattened across its own headed sections, which
this function ignores) instead of the plain KJV's. The outline's own
headings (Roman numeral / letter / number, from `ILLUMINATION_INTROS`'s
SYNOPSIS field) are unaffected either way — only the wording inside each
fold changes. Falls back to plain KJV wherever no Jesus Bible chapter exists
for that reference, whatever the toggle's state.

`data/jesus.js` (`JESUS_BOOKS`, `JESUS`, `JESUS_INTROS`) is untouched by this
change — only how a reader reaches it. `JESUS_INTROS` (the short per-book
intros in Jesus's own voice, e.g. *"I sent Mark..."*) is no longer rendered
anywhere: it had lived on the Jesus Bible's own per-book page, which no
longer exists now that Jesus isn't a `currentTx` value. Left as valid,
unused data rather than deleted, in case it gets a new home later; not
resurrected here since it wasn't part of what was asked. `CORPUS.jesus`,
`isVerseTx`'s jesus branch, and every `currentTx === 'jesus'` conditional
across `switchTranslation`/`illumLabel`/`navPickerBooks` were removed as
dead code once the card went away.

Coverage is still partial by design (3 of 66 books): the "jump to this verse
in another translation" popup, search indexing, and reading-plan generation
remain untouched.

Each Jesus Bible chapter is still broken into headed sections in its own
data (reusing the Illumination's own section headings and verse-range
boundaries for Mark, Romans, and Galatians) — that structure just isn't what
renders when viewed through the KJV dot, since `buildKjvSynopsisChapter`
always imposes its own outline-based grouping regardless of the input
chapter's own sections.

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

**Status: the 16 books Kenneth Wuest covered are complete.** All 16 are drafted, verified against
`KJV.json`, wired into `data/jesus.js`, live-tested, and audited against Towns. Past that scope,
the user has asked to extend the project book by book into the rest of the New Testament,
starting with 1 Corinthians — same process, same rules, each new book gets its own "Epistle
rules" section below same as the original 16. See the Progress table below.

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
| Hebrews | 303 | done |
| 1 Timothy | 113 | done |
| 2 Timothy | 83 | done |
| 1 Peter | 105 | done |
| 2 Peter | 61 | done |
| 1 John | 105 | done |
| 2 John | 13 | done |
| 3 John | 14 | done |
| Jude | 25 | done |
| 1 Corinthians | 437 | done |
| 2 Corinthians | 257 | done |
| Acts | 1007 | done |
| 1 Thessalonians | 89 | done |
| 2 Thessalonians | 47 | done |

**All 16 books Wuest covered are done.** 1 Corinthians, 2 Corinthians, and Acts are the first books
added beyond that original scope, at the user's request, covering the rest of the New Testament book
by book. Acts is the longest book in the project and the first non-epistle extension — see "Narrative
rules (Acts)" below for how its genre (third-person historical narrative, not first-person epistles)
required a new distinction the epistle rules never needed.

## Epistle rules (1 & 2 Thessalonians) — the first genuinely co-authored letters, and the Corinthians "narrow to one" lesson confirmed for a real trio

Read against Elmer Towns' actual chapters for both letters (`Chapter053.html`, "I Am Coming Again";
`Chapter054.html`, "Who Saves From Tribulation") complete before any verse was written. Both letters open
"Paul, and Silvanus, and Timotheus" — the first books in the project actually sent by three named
people, not one author using an editorial "we" the way 2 Corinthians' "Timothy, a brother" co-salutation
still worked out to be Paul speaking alone.

1. **The collective "we/us/our" that runs through nearly every verse of personal report narrows to
   singular, demoted "Paul," never a plural "they" for the three senders together** — the same lesson
   1 and 2 Corinthians already established (Paul's "we" narrows to "he," not a group), now applied to a
   letter where a real trio might have been the more obvious reading. Confirmed by Towns, who narrates
   the entire founding visit, the persecution at Philippi, the working with his own hands, and the
   longing to return, through "Paul" alone throughout both chapters, never distinguishing Silvanus's or
   Timothy's own part in the "we." Only 3:1-2's "when we could no longer forbear... sent Timotheus" keeps
   its plain sense (Paul deciding to send Timothy) once narrowed to a single actor.
2. **"We beseech/exhort/command you... by the Lord Jesus" (1 Thess 4:1-2, 2 Thess 3:6, 3:12) is Paul
   invoking Christ's authority for an instruction, not Jesus narrating Himself** — the same test 1 Timothy
   5:21/6:13 established (can the speaker coherently invoke Christ as a separate authority alongside their
   own voice?). Each instance demotes the frame to "Paul" and leaves "the Lord Jesus"/"our Lord Jesus
   Christ" as an unconverted invoked title, rather than converting to a self-referential "by me."
3. **The rapture passage (1 Thess 4:13-18) runs entirely in Jesus's own first-person voice**, confirmed
   word for word against Towns (*"since you believe that I died for you and rose again... I will come
   down from heaven with a shout"*), including the verse that introduces it (4:13's "I would not have you
   to be ignorant" stays Jesus's own address rather than demoting like the surrounding personal material,
   since it opens the doctrinal teaching rather than reporting Paul's own circumstance). **"We which are
   alive and remain unto the coming of the Lord" (4:15, 4:17) converts to "ye which are alive and remain"**
   — the Romans/Galatians self-inclusion rule, since Jesus is the one coming down, not one of the raptured,
   the same logic that turned Romans 8:23's "we... groan" into "ye... groan." 5:10's "Who died for us"
   needed the same dangling-relative-pronoun restructuring as Romans 3:25/Colossians 1:15 ("I died for
   you," not "Who died for us" hanging off the previous verse's "me").
4. **2 Thessalonians 2's antichrist passage splits "God" verse by verse, confirmed against Towns**: 2:4's
   first "all that is called God" converts to "my Father" (Towns: *"oppose everything about My Father"*),
   but the same verse's "he as God sitteth in the temple of God, shewing himself that he is God" stays
   unconverted three times running — a false claim to generic deity the antichrist makes, not a title
   belonging to the Father, matching Towns leaving "worshiped as God... temple of God... he is God" alone
   immediately after converting the first instance.
5. **"The kingdom of God" (2 Thess 1:5) stays the established fixed idiom**, unconverted, same as every
   earlier book.

Verification run: 89/89 and 47/47 verses present, chapter-by-chapter counts match `KJV.json` exactly
(10/20/13/18/28 and 12/17/18); zero unresolved dangling "Who/Whom/Which" verse-openers; zero
false-present-state hits on the "is/am dead/come/risen/gone/fled/departed" family.

**A closer, user-requested re-read (re-reading Towns' actual chapters a second time, verse by verse,
rather than just the standard judgment-call spot-check) found nine real mismatches, the most of any book
since the original 16 were built.**

1. **"We beseech/command/exhort you... by/in the name of the Lord Jesus [Christ]" (1 Thess 4:1-2, 2 Thess
   3:6, 3:12) is Jesus asserting His own authority by naming Himself, not Paul invoking Christ as a
   separate witness** — the opposite conclusion from the first draft, which treated all four like the 1
   Timothy 5:21/6:13 "invoke Christ as a separate party" pattern. Towns settles it explicitly, twice:
   *"I give you this command in My name, the Lord Jesus Christ"* (3:6) and *"I command such people... in
   My name"* (3:12) — both first person, both self-naming, neither demoted to Paul. The distinguishing
   test that separates this from the genuine 1 Timothy pattern: 1 Timothy 5:21 invokes **two** parties
   ("before God, **and** the Lord Jesus Christ") as co-witnesses **alongside** the speaker's own "I,"
   which Jesus cannot coherently do about Himself; "by/in the name of the Lord Jesus" names only **one**
   authority, and if that one authority is the speaker Himself, self-naming is exactly what "the Son of
   man" merge (rule 6) and 2 Thess 3:16's "I myself, the Lord of peace" already do elsewhere in this same
   pair of letters. Fixed all four to Jesus's own first-person voice with a self-naming apposition ("I
   beseech you... even I the Lord Jesus"), which also meant converting the "of us"/"received of him"
   material inside those same verses to "of me," since the whole verse is now one voice, not a demoted
   frame around Paul's material.
2. **That correction cascades through the rest of 1 Thessalonians 4:1-12, which turns out to run entirely
   in Jesus's own voice with no demoted "Paul" material in it at all.** 4:9's KJV singular "ye need not
   that I write unto you" is confirmed Jesus's own claim by Towns (*"I didn't need to tell you to love
   your brothers"*) rather than demoting like Jude 1:3's analogous "I gave... needful for me to write" did
   — a reminder that the demotion-of-personal-writing-statements pattern is a case-by-case judgment call,
   not a rule that transfers automatically between books. 4:10-11's "we beseech/we commanded" sit in the
   same unbroken paragraph, with Towns never reintroducing "Paul" by name anywhere in the stretch (unlike
   stretches earlier in the letter where he explicitly does), so both were changed to Jesus's own "I"
   for consistency with the confirmed anchor at 4:9 and 4:1-2.
3. **3:3's "for yourselves know that we are appointed thereunto" is a shared-condition "we" (Paul and the
   readers together), not Paul's own personal appointment, and converts to "ye are appointed thereunto"**
   — confirmed by Towns generalizing it to "Troubles are part of God's plan for **the believers**," and by
   the very next verse (3:4), already drafted correctly as "ye should suffer tribulation," which the first
   draft had failed to carry backward one verse — the same immediate-neighbor-consistency lesson 1 Peter
   5:2/5:3 taught the project originally.
4. **Two judgment calls were checked against Towns and left unchanged despite him phrasing them
   differently**, on the principle that a single loose, compressed paraphrase clause is weaker evidence
   than clear grammatical continuity or a repeated pattern: 2 Thess 1:9's "from the presence of the Lord"
   stays "from my presence" (continuing the Christ-subject established by "the Lord Jesus" two verses
   earlier) even though Towns' paraphrase says "My Father's presence" once, loosely; 2 Thess 2:11's "God
   shall send them strong delusion" and 3:3's "the Lord is faithful" both stay on the project's standard
   Father/Son default ("my Father"/"I") even though Towns substitutes "the Holy Spirit" for the first and
   generalizes "My Father" for the second — a real Person-swap in Towns' own theology, not a precise
   pronoun-tracking signal this project's literal method should follow.

Re-verified after all nine fixes: still 89/89 and 47/47 verses, chapter counts unchanged, zero residual
"we/us/our" anywhere in either book (the fixes removed the last remaining instances), residual "God" (4
total: 1 Thess 1:9's "the living and true God," 1 Thess 5:23's "the very God of peace," 2 Thess 1:5's
"kingdom of God" idiom, 2 Thess 2:4's triple antichrist self-claim) and residual "Lord Jesus"/"Lord Jesus
Christ" (4 total, the four self-naming verses above) are every one a deliberate exception; re-spliced into
`data/jesus.js` and re-tested live across all 1,255 chapter destinations in both states (2,510 loads, zero
errors).

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

## Epistle rules (Hebrews) — a different problem again: no named author

Read against Elmer Towns' actual Hebrews chapter (`Chapter059.html`, "I Am Jesus — Who Gives Better")
complete before any verse was written. Hebrews breaks the pattern every prior epistle shared: **it
names no author.** There is no "Paul" to demote to third person for personal asides — a genuinely new
problem this project hadn't faced.

1. **Most of Hebrews' first-person "I"/"we" is Jesus's own voice**, not a human writer's, because the
   book frames itself throughout as Jesus's own sermon (its own intro: "I am Jesus, Who led the
   writing of the book of Hebrews"). Confirmed by Towns treating warm pastoral assurance (6:9, "I am
   persuaded better things of you") as Jesus speaking directly, not the anonymous writer reporting.
   **"The writer" (third person) is reserved only for genuine external biographical facts** about the
   actual human author that cannot coherently be Jesus's own experience — and those don't appear until
   chapter 13's closing: wanting to visit (13:18-19, 23), having written only a short letter (13:22),
   Timothy's release from prison (13:23). Confirmed against Towns, who uses exactly this boundary:
   "The writer asked for prayer that he could visit the readers... Timothy has been released from
   prison and will come to see them."
2. **Chapter 1's long chain of OT quotations (vv. 5-13) are the Father speaking directly *to* the
   Son** ("Thou art my Son," "Thy throne, O God," "Thou, Lord, in the beginning hast laid the
   foundation of the earth") — these stay in second-person "thou/thee/thy" throughout, Jesus
   *receiving* the address rather than speaking it, per the established rule for prophecy/address
   spoken to Him (Mark rule 4). The same treatment applies to every other Father-to-Son quotation later
   in the book (5:5-6, 7:17, 7:21).
3. **A critical, easy-to-miss exception: 4:8's "Jesus" is Joshua, not Christ.** The KJV renders the
   Greek Ἰησοῦς the same way for both men, and this verse ("if Jesus had given them rest...") is about
   Joshua's conquest failing to give Israel the ultimate rest the Psalm speaks of. Converting it to "I"
   would falsely put Christ's own failure into the text — left exactly as the KJV has it.
4. **A near-miss caught before it shipped, at 7:27**: "who needeth not daily... to offer up sacrifice,
   first for his own sins, and then for the people's" describes what the *other* (Levitical) high
   priests need, by contrast with Christ, who doesn't. Mechanically converting "his own sins" to "my
   own sins" on the momentum of the surrounding first-person conversion would have falsely implied
   Christ needed atonement for His own sin. Kept "their own sins," correctly attributing the phrase to
   the priests being contrasted, not to Christ.
5. **Chapter 11 (the faith chapter) stays third-person historical narrative** about Abel, Enoch, Noah,
   Abraham, Moses, and the rest — like parable content, these are accounts *about* people, not Jesus's
   own voice, except where the chapter's own framing needed conversion (11:3's "through faith we
   understand" → "ye understand," since Jesus has direct knowledge of creation, not faith-based
   understanding of it).
6. **The established citation rule carried the heaviest load in this book** — Hebrews quotes the Old
   Testament more densely than any other book done so far (Psalms 2, 8, 22, 40, 45, 95, 102, 110,
   Jeremiah 31, Deuteronomy 32, Exodus 24, Haggai 2, Proverbs 3, Habakkuk 2, and more), and every one
   of these stays exactly as quoted regardless of what pronoun it carries, per the rule established
   back in Mark and Ephesians.

Verification run: 303/303 verses present, chapter-by-chapter counts match `KJV.json` exactly
(14/18/19/16/14/20/28/13/28/39/40/29/25). 10 residual "God"/"Jesus" instances survive, every one a
deliberate exception (OT citations, the Father's address to the Son, the Joshua/Jesus name collision,
or a compound title in apposition — "my Father, the God of peace"); zero residual "Christ"; 2 residual
"we/us" instances, both matching the established "what shall we say"/"we know"/"we conclude"
rhetorical-formula exception (3:19 "so we see," 10:30 "for we know him that hath said"); zero
false-present-state hits on the "is/am dead/come/risen/gone/fled/departed" family.

## Epistle rules (1 Timothy) — a named author again, but not every "I" goes to him

Read against Elmer Towns' actual 1 Timothy chapter (`Chapter055.html`, "I Am Jesus — The Victor in
Spiritual Warfare") complete before any verse was written. Paul is named again here (unlike Hebrews),
so the baseline expectation returns to "Paul's personal/biographical material demotes to third
person" — but this book sharpened exactly where that line falls, because several first-person
statements that look like Paul's own voice turned out, on checking Towns, to be Jesus's:

1. **1:15's "faithful saying" splits mid-verse.** "That Christ Jesus came into the world to save
   sinners" stays Jesus's own "I came" (confirmed by Towns: *"I came into the world to save
   sinners"*), but "of whom I am chief" — Paul's own confession of being the worst of sinners —
   converts to third person, *"of whom Paul was chief,"* matching Towns' *"Paul was the greatest of
   them."* One verse, two different speakers, not a blanket rule either way.
2. **1:20's "whom I have delivered unto Satan" stays Jesus's own disciplinary act**, not Paul's,
   confirmed by Towns: *"I gave them to satan to punish them."* Likewise 6:15-16's "King of kings,
   and Lord of lords... whom no man hath seen, nor can see" stays Jesus's own self-description
   (Towns: *"I Am King of kings and Lord of lords... no one has seen Me or can see Me"*), even though
   it sits inside a passage otherwise built around Paul charging Timothy.
3. **The test that resolved the harder cases: can the speaker coherently invoke the Father and
   Christ as separate witnesses?** 5:21 ("I charge thee before God, and the Lord Jesus Christ, and
   the elect angels") and 6:13 ("before Christ Jesus, who before Pontius Pilate witnessed a good
   confession") both name Christ in the third person as a witness *alongside* the speaker's "I" — a
   construction Jesus cannot use about Himself. Both converted to third-person Paul giving the
   charge, with "Christ Jesus" converting normally to "me" as the witness being named.
4. **3:16's mystery-of-godliness creed converts fully to Jesus's own testimony** ("I was manifest in
   the flesh, justified in the Spirit..."), confirmed by Towns doing the same — a different case from
   Ephesians 4:4-6's untouched trinitarian formula, because this is Christ narrating His own
   incarnation and exaltation, not a fixed confessional recitation about the Godhead collectively.
5. **The recurring "God our Saviour" formula (1:1, 2:3) needed the same fix Titus required**: drafted
   first as "my Father, **our** Saviour," which wrongly includes Jesus among the saved — corrected to
   "your Saviour" throughout.
6. **A fresh audit pass caught a wrong default at 2:5.** "There is one God, and one mediator between
   God and men" was first drafted leaving "one God" unconverted, applying the Romans/Galatians
   creedal-formula exception by pattern-match alone, without checking whether Towns treats *this*
   instance the same way. He doesn't: *"My Father is the only God and I, Christ Jesus, am the only
   Mediator between My Father and all people"* — he converts "God" to "my Father" explicitly both
   times. Fixed to *"For my Father is the one God, and I, the man, am the one mediator between my
   Father and men."* The Romans/Galatians instances aren't necessarily wrong — this is a reminder that
   the creedal-exception category is a judgment call verified case-by-case against Towns, not a rule
   that transfers automatically to every future "one God" sighting.

Verification run: 113/113 verses present, chapter-by-chapter counts match `KJV.json` exactly
(20/15/16/16/25/21). Zero residual "God" outside the corrected 2:5 (now attached to "my Father" as a
title, not a bare unconverted noun); zero residual "Christ"/"Jesus"; 1 residual "we" (1:8, "But
we know," the established rhetorical-formula exception); zero unresolved dangling "Who/Whom/Which."

## Epistle rules (2 Timothy) — Paul's own words stay Paul's, even under his own name

Read against Elmer Towns' actual 2 Timothy chapter (`Chapter056.html`, "I Am Jesus — Living Right,
Dying Right") complete before any verse was written, then given a fresh audit re-read afterward,
cross-checking every judgment-call verse against Towns' specific wording — the same discipline used
on 1 Timothy, Hebrews, and the Colossians correction. This one came back clean on the first pass, with
zero corrections needed, likely because 2 Timothy's much heavier proportion of personal, biographical
material made the Paul/Jesus split easier to judge consistently than 1 Timothy's mix of personal and
doctrinal content.

1. **2:8-9 splits mid-verse exactly like 1 Timothy 1:15 did**: "Jesus Christ... was raised from the
   dead" stays Jesus's own "I... was raised," confirmed by Towns (*"I was a descendant of David... I
   was raised from the dead"*), but "wherein I suffer trouble... unto bonds" is Paul's own
   imprisonment and converts to third person, confirmed by Towns narrating Paul's chains separately
   in the same breath (*"Paul was chained like a criminal, but the gospel is not chained"*).
2. **2:11-13's faithful saying stays entirely in Jesus's first-person voice**, converting "we" to
   "ye" throughout — confirmed word-for-word against Towns' *"If you have died with Me... you will
   live with Me... If you deny Me, I will deny you; if you become faithless, I am always faithful."*
3. **Two of Paul's own prayers stay unconverted, in his own voice**, matching the Galatians 2:14 and
   Colossians 4:18 precedent for Paul's own directly-written words: 4:14's "the Lord reward him"
   (Towns: *"Paul prayed, 'Lord, repay him for the evil he has done'"*) and 4:7's entire "I have
   fought a good fight, I have finished my course, I have kept the faith" (Towns explicitly frames
   this as a direct quotation: *"He said, 'I have fought a good fight...'"*). The very next verse
   (4:8) shifts back to third-person narration about Paul once the quote ends, converting "the Lord...
   shall give me" to Jesus's own "I... shall give him" — a quote can end and hand back to narration
   mid-passage without the whole passage needing one consistent voice.
4. **4:16-18 confirms Jesus's own voice for the "the Lord stood with me" passage**, matching Towns
   exactly (*"I, his Lord, stood by him and gave him power... I delivered him from being thrown to the
   lions"*), while the prayer just before it (4:16's "I pray God that it may not be laid to their
   charge") stays Paul's own prayer, narrated in third person (*"He prayed for those who deserted
   him"*) — the same citation-vs-commentary boundary used throughout this book.

Verification run: 83/83 verses present, chapter-by-chapter counts match `KJV.json` exactly
(18/26/17/22). **Zero** residual "God"/"Christ"/"Jesus" — the cleanest scan of any book in the
project so far; zero residual "we/us/our"; zero unresolved dangling "Who/Whom/Which" verse-openers.

## Epistle rules (1 Peter) — the least biographical letter yet, almost all Jesus's own voice

Read against Elmer Towns' actual 1 Peter chapter (`Chapter061.html`, "I Am Jesus — When You Suffer")
complete before any verse was written, then given the same post-draft audit pass used since
Colossians. 1 Peter has far less of Paul's-style personal/travel detail than any epistle done so
far — no companions named until the very close, no travel plans, almost no "I did X, I went to Y."
Confirmed by Towns, who keeps almost the whole letter in Jesus's own direct first-person voice,
including passages that read like they could be Peter's own commentary:

1. **The suffering-as-pattern passage (2:21-25) and the descent-to-preach passage (3:18-22) both
   convert fully to Jesus's own testimony**, matching Towns almost word for word both times (*"I did
   not commit one sin... I committed Myself to My Father who will judge rightly"*; *"I descended into
   hell to announce My victory to people in prison... I entered heaven to sit at My Father's right
   hand"*).
2. **2:6's cornerstone citation stays exactly as quoted** ("Behold, I lay in Sion a chief corner
   stone... he that believeth on him") — the Father's own words about the Son, kept third-person
   inside the citation, the same treatment Hebrews gave the Father-to-Son quotations in chapter 1.
   The verse *after* the citation (2:7's commentary applying it) converts normally to Jesus's own "I
   am precious... I am made the head of the corner."
3. **Peter's own self-identification converts to third person** at 5:1 ("who am also an elder, and a
   witness of the sufferings of Christ") and 5:12 ("as I suppose, I have written briefly") — the only
   two places in the whole letter where Peter's own voice, rather than Jesus's, needed the standard
   demotion. Confirmed against Towns' explicit framing: *"Now a word to you who are elders because
   Peter was an elder, and a witness of My suffering"* and *"This letter is sent by Silas whom Peter
   trusted."*
4. **The audit pass caught one real mismatch at 5:2.** "Feed the flock of God" was first drafted as
   "Feed my flock," reasoning from the John 21:15-17 "feed my sheep" parallel — a plausible
   theological inference, but not what Towns actually did. He keeps it *"the flock that God has
   entrusted to you"* — God (the Father) as a distinct entity commissioning the elders, not Jesus's
   own self-reference. Fixed to "Feed my Father's flock." **The lesson repeats: a strong biblical
   cross-reference is not a substitute for checking what Towns actually wrote at that specific
   verse** — this is the third time a plausible-but-unverified default has been caught this way
   (after Colossians' reconciler and 1 Timothy's "one God").
5. **4:19's "the will of God" and "a faithful Creator" both convert to Jesus's own voice** rather
   than the more common "my Father" default, confirmed by Towns: *"when you suffer for doing My
   will... Trust your soul to Me, the faithful Creator."*

Verification run: 105/105 verses present, chapter-by-chapter counts match `KJV.json` exactly
(25/25/22/19/14). Only 2 residual instances survive and both are deliberate: "Christian" (4:16,
"Christ" is a substring, not a real residual) and "my Father, the God of all grace" (5:10, the
compound-title exception); zero residual "we/us/our"; zero unresolved dangling "Who/Whom/Which."

**A second, closer re-read (requested by the user, not part of the standard audit) caught one more
mistake at 5:3.** The 5:2 fix ("God's flock" → "my Father's flock") wasn't checked against the very
next verse, which names the same flock again: "Neither as being lords over God's heritage" had been
left as self-referential "mine heritage" — directly contradicting the fix one verse earlier. Confirmed
against Towns too, who keeps this one as the Father as well: *"Don't be dictators over God's
people."* Fixed to "my Father's heritage." **The lesson: a fix to one verse needs its immediate
neighbors re-checked for the same referent, not just the verse itself.**

## Epistle rules (2 Peter) — Jesus narrates His own past judgments, and the audit came back clean

Read against Elmer Towns' actual 2 Peter chapter (`Chapter062.html`, "I Am Jesus — Who Delays My
Coming") complete before any verse was written, then given the standard post-draft audit pass. Every
checked verse matched Towns' specific wording exactly — the second book in a row (after 2 Timothy) to
need zero corrections, a sign the judgment-call reasoning is landing correctly during drafting itself,
not just being caught afterward.

1. **Chapter 2's whole recitation of past judgments converts to Jesus's own first-person voice**,
   confirmed extensively against Towns: *"I didn't spare the angels who sinned... I didn't spare any
   of the people who lived before the flood. I completely destroyed the world with a flood... I
   delivered Lot."* "God spared not the angels," "spared not the old world," "delivered just Lot" all
   become "I."
2. **A genuine distinction from 1 Peter's pattern**: Peter's clearly personal biographical claims
   (1:12-15's approaching death, 1:16-18's Transfiguration eyewitness testimony) convert to third
   person as expected — but 3:1's "This second epistle... I now write unto you" stays in Jesus's own
   voice, unconverted, confirmed by Towns keeping it that way too (*"I write this second letter, as I
   did in both letters"*). The difference: 1:12-15 and 1:16-18 carry Peter's specific personal
   circumstances (his own death, his own eyewitness experience) that cannot coherently be Jesus's
   own; 3:1 is a generic authorial marker that Towns treats as part of Jesus's ongoing message rather
   than Peter's own aside.
3. **1:17's Transfiguration voice stays exactly as quoted** ("This is my beloved Son, in whom I am
   well pleased") — the Father's own words about the Son, third person inside the quote, matching the
   same treatment Hebrews and 1 Peter gave every other instance of the Father addressing or naming the
   Son.
4. **3:18's closing doxology splits between the two established patterns in one verse**: "grow in...
   the knowledge of [Christ]" converts to self-reference ("of me"), but "to him be glory" stays
   pointing at the Father, unconverted — confirmed by Towns doing exactly this split (*"Grow in grace
   and in My knowledge. To My Father be all glory"*).

**A second, closer re-read (requested by the user) caught a clarity issue at 3:15, not a theological
error.** "Even as our beloved brother Paul" had converted "our" to "his," correctly referring to
Peter — but by that point in the letter, all of chapters 2-3 had run in Jesus's continuous
first-person voice, so the last explicit "he" = Peter sat some 30 verses back, in chapter 1. Nothing
else in the sentence could plausibly be the antecedent, so it wasn't strictly wrong, just a long reach
for a reader to make. Changed to "Peter's beloved brother Paul," naming him explicitly rather than
relying on a pronoun that far from its antecedent — the same fix already used elsewhere in the project
(e.g. Colossians 4:11's "with Paul") when a pronoun would otherwise be ambiguous or hard to trace.
Towns doesn't address this specific phrase (he paraphrases past it entirely), so this one is a clarity
judgment, not a Towns-confirmed correction — worth being honest about that distinction.

Verification run: 61/61 verses present, chapter-by-chapter counts match `KJV.json` exactly
(21/22/18). **Zero** residual "God"/"Christ"/"Jesus" and **zero** residual "we/us/our" — matching
2 Timothy's cleanest-scan result; zero unresolved dangling "Who/Whom/Which."

## Epistle rules (1 John) — no named author again, and the writer's own eyewitness claim needs its own third person

Read against Elmer Towns' actual 1 John chapter (`Chapter063.html`, "I Am Jesus — Who Loves You") complete
before any verse was written, then given the standard post-draft audit pass. 1 John shares Hebrews'
problem (no named human author anywhere in the text — tradition calls him John, but the word "John"
never appears inside 1 John itself) but adds a new wrinkle Hebrews never had: the letter opens with a
first-person plural claim to have **physically** heard, seen, and handled its subject — "which we have
heard, which we have seen with our eyes... our hands have handled, of the Word of life" (1:1-4).

1. **1:1-4's physical eyewitness testimony converts to third person, "the writer,"** the same category
   Hebrews reserved for genuine external biographical fact (13:18-23) and 1/2 Peter reserved for Peter's
   own transfiguration eyewitness claim (2 Peter 1:16-18) — a claim that is flatly incoherent as Jesus's
   own voice, since Jesus cannot narrate having physically handled Himself as an object while also
   speaking as that object in the first person. "The Word of life" itself, being Christ, still converts
   normally ("of me, the Word of life"). The same eyewitness-testimony shape recurs once more at 4:14
   ("we have seen and do testify that the Father sent the Son"), confirmed against Towns, who explicitly
   names the writer there: *"John saw with his eyes and writes to tell you My Father sent Me, the Son, to
   save the world."*
2. **From 2:1 onward, the letter's singular epistolary "I write unto you" and its recurring vocative
   "little children" stay Jesus's own voice**, unlike the plural eyewitness claims in (1) — the
   distinguishing test, following Hebrews' own rule, is whether the statement reports something
   *circumstantial about the specific human writer's life* (demotes) or *functions as pastoral/doctrinal
   address to the reader* (stays Jesus, coherent with the book's whole framing as His letter). Confirmed
   against Towns, who keeps 2:1's "these things write I unto you, that ye sin not" entirely in Jesus's
   voice (*"Because I told you not to sin, you must not do it"*) and folds "we have an advocate with the
   Father, Jesus Christ the righteous" into Jesus naming Himself the advocate directly (*"I stand at My
   Father's right hand to plead forgiveness for you"*) — the generic "we" needing an advocate converts to
   "ye," since Jesus does not need Himself as His own advocate.
3. **1 John's most distinctive feature is its constant "hereby we know" refrain** (2:3, 2:5, 2:18, 3:2,
   3:14, 3:19, 3:24, 4:6, 4:13, 5:2, 5:15, 5:18, 5:19, 5:20 and more) — a much heavier density of this
   construction than any earlier book. Every instance converts "we/us/our" to "ye/you/your" (the
   Romans/Galatians collective-condition rule), never Jesus's own rhetorical "we," confirmed repeatedly
   against Towns turning each one into direct address (*"Know this much about your future life... you
   will be like Me"* for 3:2; *"You know you are born again because..."* for 5:18-19) — unlike Romans'
   occasional exception for generic theological "we know" formulas, this book's whole purpose is
   reader-assurance, so the refrain is never left as Jesus's own uncertainty-by-inference.
4. **"God" does not default to "my Father" as reliably as in any earlier book — several instances are
   Jesus's own direct self-predication instead, verified one at a time against Towns.** "That God is
   light" (1:5) converts to Jesus's own *"I am light"* (Towns: *"I am light, and there is absolutely no
   darkness in Me"*), and "try the spirits whether they are of God" (4:1-4) converts to "of me" (Towns:
   *"test their spirit to see if they are from Me"*) — but "God is love" (4:8, 4:16) stays "my Father is
   love" both times (Towns: *"He is love"* attributed explicitly to "My Father"), and "we love him,
   because he first loved us" (4:19) likewise stays "my Father" (Towns: *"your love for My Father comes
   because He first loved you"*), even though the surrounding verses are Jesus's own voice. No single
   default rule covers this book's "God" — each instance needed its own check.
5. **A recurring construction — "he that saith, I know him" (2:4), "he that saith he abideth in him"
   (2:6), "if a man say, I love God" (4:20) — creates a self-reference problem unique to this book**: a
   hypothetical false professor's *quoted* claim about Christ, phrased as first person "I," collides with
   Jesus now being the narrator's own first person. Left as literal quotation, "I know him" would become
   "I know me" once "him" (=Christ) converts to "me" — nonsense. Resolved two different ways depending on
   Towns: 2:4 and 2:6 restructure from direct to indirect quotation (*"he that saith that he knoweth
   me"*), matching Towns' *"Those who say that they know Me"*; but 4:20 keeps the KJV's literal direct
   quotation and its unconverted "God" untouched (*"If a man say, I love God..."*), matching Towns
   keeping it as an actual quotation too (*"Those who say, 'I love the Father'"*) — the difference is that
   "God" isn't the narrator's own name the way "him"=Christ is, so no self-reference collision forces a
   restructure there.
6. **"The Son of God" is kept as a fixed confessional title in five places** (3:8's "I, the Son of God,"
   matching the established Son-of-man/Son-of-God self-merge rule; 4:15, 5:5, 5:10, 5:20's "believeth /
   confess that [Jesus/I am] the Son of God") rather than forcing "God" to "my Father" inside the title
   every time — this book's five confessional "born of God" / "Son of God" formulas function the way
   "one God" and "the Godhead" have functioned as fixed-phrase exceptions in earlier books, and Towns'
   own text keeps the same title intact in most of these spots ("I Am the Son of God").

**The post-draft audit caught one real mismatch at 2:22.** "That denieth the Father and the Son" had
first been converted to "that denieth my Father and me," applying the standard Christ/Father-name
conversion by default. But Towns' own text keeps this exact clause unconverted — "They have the spirit
of antichrist because they deny both the Father and the Son" — in the very same paragraph where the next
sentence (2:23) *does* convert ("those who have Me, the Son, also have My Father"). The distinction
Towns draws: 2:22 names "the Father and the Son" as a title-pair, summarizing *what* the antichrist
denies, while 2:23 restates the same idea as a direct personal relationship claim ("have Me... have My
Father"), which is what actually converts. Fixed 2:22 back to the unconverted KJV title-pair, leaving
2:23 converted as before.

**A closer, user-requested re-read (beyond the standard audit) found four more mismatches, all in the
"which Person is this" judgment calls, not grammar.** 3:21's "confidence toward God" had been converted
to "toward my Father," but Towns reads the whole 3:21-22 unit as addressed to Jesus (*"you can come to Me
with your request in prayer"*) — fixed to "toward me," matching 3:22's already-correct "of me." 4:6's "we
are of God... heareth God" had gone to "my Father" by extending the "of me" pattern from 4:1-3 only
partway; Towns keeps the whole testing-spirits unit (4:1-6) in Jesus's own voice (*"I listen to you...
belong to Me listen to Me"*) — fixed 4:6 to "of me... heareth me" throughout. 4:13's "we dwell in him, and
he in us... he hath given us of his Spirit" had converted to Jesus's own voice, but Towns continues the
Father-attribution from 4:12 straight through 4:13 (*"My Father has put the Holy Spirit into your heart...
He lives in you"*) — fixed to "him"/"he" (my Father, via the adjacent-verse pronoun, not distant). 4:17's
"our love made perfect" had gone to "your love," but Towns attributes the love itself to Christ (*"My love
will be complete in you"*), matching the same pattern already used at 3:16-17 and 4:12 — fixed to "my
love is made perfect in you." One candidate fix was checked and rejected: 5:20's "This is the true God"
looked like it might need to become "my Father is the true God" per Towns' paraphrase, but the KJV's own
grammar ("we are in him that is true, **even in** his Son Jesus Christ. This is the true God") uses "even
in" to identify "him that is true" as the Son, making Christ the antecedent "This" points to — the
original "I am the true God" is the better-supported reading and was left unchanged.

Verification run: 105/105 verses present, chapter-by-chapter counts match `KJV.json` exactly
(10/29/24/21/21). Residual "God"/"Christ" survivors (9 total) are every one a deliberate exception listed
above (the "Son of God" title x5, "I am the Christ" x2 self-naming, 4:20's quoted "I love God", and
2:22's "the Father and the Son" title-pair);
**zero** residual "we/us/our/ourselves" outside the deliberate 1:1-4/4:14 "the writer" passages; zero
residual "his Son" (all converted to "me"); zero unresolved dangling "Who/Whom/Which" verse-openers (the
two verse-initial "Who" instances, 2:22 and 5:5, are both self-contained rhetorical questions, not
continuations of a prior verse's antecedent, so neither needed restructuring).

## Epistle rules (2 John) — a named title again ("the elder"), and a fixed-title exception confirmed from 1 John carries over

Read against Elmer Towns' actual 2 John chapter (`Chapter064.html`, "I Am Jesus — The Shepherd Over My
Church") complete before any verse was written, then given the standard post-draft audit pass. Unlike 1
John, this letter opens with the author naming his own office — "The elder unto the elect lady and her
children" — giving a textual handle to demote to, the way "Paul" did in the earlier epistles, rather than
the invented "the writer" placeholder Hebrews and 1 John needed.

1. **"The elder's" own personal claims (his love for the recipients, his joy at their walking in truth,
   his wish to visit rather than write) demote to third person**, confirmed by Towns naming "John" (not
   Jesus) as the one who loves them, rejoices, and will come speak face to face: *"John and everyone in
   Me... love you"*; *"John had many things to explain to you, but he did not write them"*. This matches
   Paul's own personal/biographical material demoting throughout Romans–2 Timothy, and Hebrews 13's
   "the writer" material.
2. **The grace-benediction (1:3) and the doctrinal warning about false teachers (1:7, 1:9) stay Jesus's
   own voice**, confirmed by Towns keeping the benediction in Jesus's own first person (*"Grace, mercy,
   and peace from God My Father and from Me, the Lord Jesus Christ, the Son of the Father"*) and the
   heresy-warning as Jesus's own self-description (*"those who believe and teach that I was born only
   with a human body, and that I am not God"*, matching 1 John 4:2-3's "confess... that Jesus Christ is
   come in the flesh" → "that I am come in the flesh" pattern exactly).
3. **1:3's "the Son of the Father" is kept as a fixed title, "the Father" left unconverted inside it**,
   even though "from God the Father" converts normally to "my Father" earlier in the same verse —
   confirmed directly against Towns, who does the identical thing: converts the first "God the Father" to
   "God My Father" but leaves the appositive title "the Son of the Father" with a bare "the Father," not
   "My Father." The same fixed-title-pair exception 1 John 2:22 established ("the Father and the Son"
   left unconverted as a title-pair) recurs here in a different grammatical shape.
4. **1:9's "he hath both the Father and the Son" converts fully** ("he hath both my Father and me"),
   distinguishing it from (3)'s title exception the same way 1 John 2:23 was distinguished from 2:22 —
   this is a personal-possession claim ("hath... the Father and the Son" = has fellowship with both), not
   a title naming what something is called, and Towns converts it explicitly: *"Those who remain true to
   Christian doctrine have both My Father and Me, the Son."*
5. **"God speed" (1:10, 1:11) is a fixed archaic greeting idiom ("wish success"), not a live invocation
   of God, and stays unconverted** — the same idiom-exception category as "God forbid" elsewhere in the
   project, not a case requiring "my Father" treatment.

Verification run: 13/13 verses present, matching `KJV.json` exactly. Residual "God" (2 total) is the
deliberate "God speed" idiom exception; zero residual "we/us/our" outside the demoted-elder passages;
zero residual "Christ"/"Jesus." Post-draft audit against Towns found no further corrections needed.

## Epistle rules (3 John) — the most personal letter in the project, almost entirely "the elder"

Read against Elmer Towns' actual 3 John chapter (`Chapter065.html`, "I Am Jesus — The God of True
Teachers") complete before any verse was written, then given the standard post-draft audit pass. 3 John
is the shortest and most personal letter done so far — a private note from "the elder" to a named friend
(Gaius) about hospitality, a church boss (Diotrephes), and a commendation (Demetrius) — with almost no
doctrinal content in Jesus's own voice at all.

1. **Nearly every verse is the elder's own personal statement and converts to third person**, matching
   Towns' consistent framing of "John" (not Jesus) as the one loving Gaius, praying for his health,
   rejoicing at his faithfulness, having "no greater joy," writing to the church, planning to visit, and
   sending greetings — confirmed line by line (*"John prays for you to prosper..."*; *"He rejoiced when
   he heard..."*; *"Nothing could make John happier..."*; *"John previously wrote to My church..."*;
   *"John has many things to tell them but can't write them..."*). This is the highest proportion of
   demoted material of any book in the project — only two spots carry Jesus's own voice.
2. **7's "for his name's sake they went forth" is the one clear self-reference conversion** ("for my
   name's sake") — the travelling preachers went out for Christ's sake, a standard third-person-to-"me"
   conversion untouched by the letter's otherwise-demoted frame.
3. **11's maxim ("he that doeth good is of God... hath not seen God") converts "God" to "my Father"
   by the default rule**, generic doctrinal content rather than the elder's own personal report, matching
   the pattern used for maxims throughout the project (e.g. 1 John 3:9-10's "born of God").
4. **8's "we therefore ought to receive such" and 12's "we also bear record" both needed a judgment
   call**, since Towns restructures both loosely (*"churches have a responsibility..."*; *"Everyone
   recognizes Demetrius..."*) without a clean pronoun match. 8 converts to direct address ("ye ought"),
   matching the Rule B pattern used for exhortation throughout the corpus; 12 demotes to third person
   ("he also beareth record... his record is true"), matching the letter's dominant pattern of the
   elder's own personal attestations (his testimony about Demetrius, alongside his testimony about
   Gaius in 3-4) staying in that same demoted voice rather than switching to reader-address mid-letter.

Verification run: 14/14 verses present, matching `KJV.json` exactly. **Zero** residual
"God"/"Christ"/"Jesus"/"we/us/our" anywhere in the book — every instance of each converted fully (7's
"my name," 11's "my Father" twice), the cleanest scan in the project. Post-draft audit against Towns
found no further corrections needed.

## Epistle rules (Jude) — the last book, a named author again, and Jesus narrating past judgment in His own voice

Read against Elmer Towns' actual Jude chapter (`Chapter066.html`, "I Am Jesus — Who Will Keep You")
complete before any verse was written, then given the standard post-draft audit pass. Jude names its
author in the salutation ("Jude, the servant of Jesus Christ, and brother of James"), the same shape
Paul's and Peter's letters have — but almost all of the letter's *content* runs in Jesus's own voice
(the extended recitation of past judgments strongly echoes 2 Peter 2's already-established pattern),
with "Jude" himself surfacing only twice, both confirmed against Towns naming him directly.

1. **The salutation (1:1) keeps "Jude" as the self-identifying name, unconverted, matching the
   established Paul/Peter letterhead convention** ("Paul, an apostle of mine..."), while "Jesus Christ"
   and "God the Father" inside that same line still convert to "me"/"my Father" — the salutation-name
   stays, but any Christ/Father reference inside it converts regardless, per the 1 Timothy 5:21/6:13
   precedent that a name-conversion applies independent of who the grammatical speaker is.
2. **1:3's "I gave all diligence to write... it was needful for me to write" is Jude's own personal
   report about composing the letter and demotes to third person** ("Jude gave... needful for him"),
   confirmed by Towns: *"Jude had planned to write about the wonderful truths... but he found it
   necessary to urge you to defend the faith."* No other verse in the letter needed this treatment —
   unlike 2/3 John, Jude's own voice appears only at the very opening.
3. **1:5-25's extended recitation of past judgments (Egypt, the fallen angels, Sodom and Gomorrah) stays
   entirely in Jesus's own first person**, the identical pattern 2 Peter 2 already established for the
   same material — "the Lord, having saved the people... destroyed them" (5) converts to "I... destroyed
   them," "he hath reserved" (6) to "I have reserved," confirmed word for word against Towns: *"I
   delivered the whole nation of Israel from the slavery of Egypt... I had to throw them into the
   bottomless pit of hell."*
4. **1:14-15's citation of Enoch's prophecy converts to Jesus's own first person** ("Behold, I come with
   ten thousands of my saints... spoken against me") rather than staying an unconverted third-person
   quotation the way OT citations normally do (Hebrews' and Mark's citation rule) — a deliberate
   departure, confirmed directly by Towns rendering the same prophecy as Jesus's own words: *"I will come
   with millions of saints to deliver judgment on all those who reject Me."* The distinguishing factor:
   this is a prophecy *about* Christ's own future coming, which He can coherently voice Himself, unlike a
   citation of something said *to* Him (Hebrews 1's Father-to-Son quotations, kept second-person) or
   *about* someone else entirely.
5. **1:9's "The Lord rebuke thee" stays an unconverted, third-person quotation** — Michael's own words
   spoken to the devil, per the established rule that another speaker's quoted words about/to God stay
   exactly as quoted (Mark rule 3), confirmed by Towns keeping it as a direct quote too (*"said, 'The Lord
   rebuke you.'"*).
6. **"The Spirit"/"the Holy Ghost" (1:19-20) stay unconverted, distinct-Person titles rather than
   converting to "my Spirit"** as they sometimes did in 1 John — a deliberate divergence from that
   book's pattern, confirmed by Towns' own extended aside on this exact passage treating "the Holy
   Spirit" as a distinct third person throughout (*"pray through the Holy Spirit... let the Holy Spirit
   fill you... present your requests to My Father"*), never folding the Spirit into Jesus's own "I."
7. **1:4's "denying the only Lord God, and our Lord Jesus Christ" converts fully** ("denying my Father,
   the only Lord, and me") rather than being treated as an unconverted title-pair the way 1 John 2:22's
   "the Father and the Son" was — the two constructions are only superficially similar; 2:22's pair was a
   clean, symmetrical Father/Son title Towns explicitly left untouched, while Jude 4 names two full,
   asymmetrical titles ("the only Lord God" / "our Lord Jesus Christ") with no direct Towns confirmation
   either way, so the more common convert-by-default pattern was used instead.

Verification run: 25/25 verses present, matching `KJV.json` exactly. Residual "God"/"Christ"/"Jesus"
survivors are zero; residual "Lord" (2 total, 1:4's "the only Lord" title and 1:9's quoted "The Lord
rebuke thee") are both deliberate; zero residual "we/us/our." Post-draft audit against Towns found no
further corrections needed — the sixteenth and final book of the project.

**A closer, user-requested re-read of all four final books (1 John, 2 John, 3 John, Jude) found one more
mismatch here.** 1:15's "hard speeches which ungodly sinners have spoken against him" had converted "him"
to "me," continuing the "I come" self-reference from 1:14's Enoch citation — grammatically the nearest
antecedent. But Towns splits the two clauses between different Persons: *"I will come with millions of
saints to deliver judgment... Then I will judge the wicked... and will punish those who speak defiantly
against My Father"* — the coming and judging stay Jesus's own, but the object of the "hard speeches" is
the Father. Fixed 1:15 to "against my Father," matching the Colossians-hymn lesson that a passage's
grammatical subject can shift mid-unit even while the topic stays continuous. 2 John and 3 John came back
completely clean on this closer read — no corrections needed in either.

## Epistle rules (1 Corinthians) — the first book beyond Wuest's original 16, and Paul's own text gives the sharpest signal yet for a recurring judgment call

Read against Elmer Towns' actual 1 Corinthians chapter (`Chapter047.html`, "I Am Jesus — Love, Faith,
and Hope") complete before any verse was written. 1 Corinthians is by far the longest, most varied book
attempted since Mark (437 verses, 16 chapters) and mixes nearly every pattern the project has developed
across the whole 16-book run — Paul's own extensive personal defense (chapters 4, 9), doctrinal teaching
in Jesus's own voice (chapters 12–14), a direct quotation of the Lord's Supper's institution (11:23–26),
and a resurrection chapter (15) that runs almost entirely in Jesus's own first person.

1. **A textual first for the whole project: Paul himself explicitly marks which of his instructions are
   "the Lord's" and which are his own, and this settles the judgment call directly rather than needing a
   Towns cross-check.** 7:10's "I command, yet not I, but the Lord" means the command that follows
   ("Let not the wife depart from her husband") is rendered as Jesus's own direct command, while the
   *framing* clause demotes to Paul ("he commandeth, yet not he, but I"). 7:12's mirror-image "I speak,
   not the Lord" means that whole section (7:12–35, Paul's own apostolic judgment about mixed marriages
   and virgins) stays demoted to Paul throughout, never converting to Jesus's "I" even where the content
   sounds like general teaching — Paul is explicit that this is *not* a command from the Lord. Likewise
   11:23's "I have received of the Lord that which also I delivered unto you" frames the Lord's Supper
   account (11:23–26) as content Paul transmitted rather than originated, so the frame demotes to Paul
   while the institution narrative itself — including the already-first-person quoted words, "Take, eat:
   this is my body" — runs in Jesus's own voice throughout. Confirmed against Towns, who keeps the
   institution words in Jesus's own mouth exactly the same way.
2. **Chapters 4 and 9 are Paul's most extensive personal self-defense in the whole project, and nearly
   all of both demote to third person**, confirmed line by line against Towns naming "Paul" throughout
   both (*"Paul was appointed an apostle by Me... Like prisoners on death row..."*; *"Paul is My
   apostle... He actually had seen Me, the resurrected Jesus"*). Editorial-plural "we" in this stretch
   (4:9–13, 9:4–27) resolves to singular "Paul"/"he," not a plural "they," confirmed by Towns
   consistently singularizing to "Paul"/"he" throughout the same material — a different resolution than
   the collective-apostolic "we" used elsewhere (3:9, "we are labourers together with God" → "they,"
   referring to Paul and Apollos together as a pair, still plural since two people are actually in view).
3. **Chapter 13 (the love chapter) uses Paul's own rhetorical "I" as a stand-in for "anyone," and
   converts to direct address "ye/you" throughout rather than demoting to Paul** — a different treatment
   than chapters 4/9's real autobiographical "I," confirmed by Towns converting the whole chapter to "you"
   (*"If you speak with the eloquence of great speakers... but you don't love others..."*). The test that
   separates this from chapters 4/9: chapter 13's "I" describes a generic hypothetical (anyone who had all
   these gifts without love), not a real, specific claim about Paul's own life circumstances the way "I
   fought with beasts at Ephesus" (15:32) or "I planted, Apollos watered" (3:6, demoted to "Paul") are.
4. **The resurrection chapter (15) runs in Jesus's own first-person voice for the gospel content and the
   resurrection appearances (15:3–8), then shifts to demoted "Paul" for Paul's own humility and
   biography (15:9–11), then back to Jesus's voice for the doctrinal argument (15:12–28, 15:51–58)** —
   confirmed verse by verse against Towns doing the identical shifts (*"I died for your sins... I was
   buried... I was seen by Peter"* → *"Finally, I appeared to Paul... Since he persecuted My church, he
   felt unworthy"* → *"If I were raised from the dead, how can anyone say there is no resurrection?"*).
   15:8's "he was seen of me" required the same fix as any "I ___ him [Christ]" collision elsewhere in
   the project — restructured to "I was seen of him" (Christ appearing to Paul) to avoid "I was seen of
   me" nonsense. 15:10 needed a rare mid-verse split confirmed by Towns: the first two "grace of God"
   instances stay "my Father's grace," but the third ("not I, but the grace of God which was with me")
   converts to "my grace" specifically — Towns makes the identical split (*"By My Father's grace,
   Paul... it was My grace, not his doing it"*). 15:27's "he hath put all things under his feet... he is
   excepted, which did put all things under him" required explicit naming rather than pronouns (my
   Father / me) to resolve what would otherwise be an unreadable pileup of "he/him" referring to two
   different Persons in one sentence — the same kind of disambiguation Jude 1:10's Diotrephes passage and
   1 Timothy's "before God, and the Lord Jesus Christ" needed.
5. **12:4–6's "the same Spirit... the same Lord... the same God" is kept as a fixed trinitarian formula,
   entirely unconverted** — the same exception category as Ephesians 4:4–6 and 1 John 5:7, extended here
   because the three-part parallel structure (Spirit/Lord/God) is deliberately naming all three Persons
   side by side as a formula, not narrating any one of them in particular.
6. **A citation-rule exception, confirmed directly by Towns: Enoch... no, Adam-typology at 15:45/15:47
   converts "the last Adam"/"the second man" to Jesus's own first-person self-identification** ("I, the
   last Adam, was made a quickening spirit"; "I, the second man, am the Lord from heaven"), rather than
   staying third-person the way a strict citation would — this isn't a citation at all but Paul's own
   typological application of a citation, matching Ephesians 4:9–10's established citation-vs-commentary
   boundary, and confirmed by Towns naming Christ explicitly at both points (*"the last Adam—Me—became a
   living-giving spirit"*).
7. **"The kingdom of God" (4:20, 6:9, 6:10, 15:50) stays unconverted** — confirmed against Mark's own
   90-plus instances of the identical idiom throughout the Gospel, the project's very first and most
   heavily used fixed-phrase exception, and independently confirmed by Towns leaving it untouched too
   (*"the kingdom of God is not a matter of talking, but it is power, holiness, and obedience"*).
8. **6:12 and 10:23's "all things are lawful for me" — almost certainly Paul quoting a Corinthian
   catchphrase to qualify it — converts to "all things are lawful for you" (Rule B) rather than staying
   Paul's own claim or an unconverted quotation**, confirmed by Towns converting the same construction to
   direct address both times (*"You can do anything you want, but some things are not good for you"*).
   10:29–30's parallel "why is my liberty judged... if I by grace be a partaker" converts the same way,
   continuing the same discussion.

**A closer, user-requested re-read (beyond the standard audit) found five fixes, four of them the same
kind of mistake in one chapter.** Chapter 9 (Paul's defense of his right to support) had used a
collective plural "they"/"their" at 9:10–12 ("for their sakes... if they have sown... are not they
rather"), treating it as a generic point about ministers' rights broadly — but Towns keeps this entire
chapter narrowed to Paul specifically throughout (*"Since Paul has sown spiritual things to them, he
expects food, shelter, and clothing in return... Surely Paul's rights are greater"*), never generalizing
to ministers as a class the way 9:13's genuinely distinct "they which minister about holy things" (the
temple priests) does. Fixed 9:10–12 to singular "he"/"his," matching the demoted-Paul voice already
used throughout the rest of the chapter (9:1–9, 9:15–27) — the lesson from 1 Peter 5:2/5:3 repeating
here: a voice choice made for a stretch of verses needs checking against its immediate neighbors, not
just the verse where it was first decided. 15:15 needed the identical fix for the identical reason:
"they are found false witnesses... they have testified" had stayed a collective plural (Paul + fellow
apostolic preachers) when Towns narrows this one specifically to Paul too (*"Paul has committed perjury
against Me"*), matching 15:14's already-singular "Paul's preaching" one verse earlier. 1:2's closing
clause ("both theirs, and Paul and Sosthenes's") was also cleaned up for readability, unrelated to any
Towns divergence — the original double-possessive read awkwardly. One candidate change was considered
and rejected: 16:22–24's grace/love benediction looked like it might need demoting to Paul's own closing
words (Towns frames the whole passage as "Paul sends you greetings... Paul sends his love"), but neither
verse contains a first-person pronoun whose conversion depends on who's speaking — "the Lord Jesus
Christ" converts to "me" identically either way — so there was nothing to actually change.

Verification run: 437/437 verses present, chapter-by-chapter counts match `KJV.json` exactly
(31/16/23/21/13/20/40/13/27/33/34/31/13/40/58/24). Residual "God" survivors (10 total) are every one a
deliberate exception (the "kingdom of God" idiom x4, two OT citations, "God forbid," the 12:4–6
trinitarian formula, and 8:4/8:6's generic "no other God but my Father"/"one God, my Father" phrasing);
one residual "Christ" (1:12's quoted Corinthian faction slogan, "I of Christ," kept exactly as the
quoted claim per the established quoted-speech rule); zero residual "Jesus"; zero residual
"Jesus Christ"/"Lord Jesus"/"Christ Jesus"; zero residual "we/us/our" outside 15:32's deliberately
unconverted quoted proverb ("let us eat and drink; for to morrow we die"); zero unresolved dangling
"Who/Whom/Which" verse-openers.

## Epistle rules (2 Corinthians) — Paul's most personal letter yet, and the "narrow to Paul" lesson from 1 Corinthians confirmed throughout

Read against Elmer Towns' actual 2 Corinthians chapter (`Chapter048.html`, "I Am Jesus — The One You
Serve") complete before any verse was written. 2 Corinthians is Paul's rawest, most autobiographical
letter — his own affliction in Asia, his relationship with Titus, his defense against rival "apostles,"
and the famous catalog of his sufferings (11:23-33) and thorn in the flesh (12:7-10). The closer-read
lesson learned on 1 Corinthians 9 and 15 — that Paul's own "we/us/our" narrows to singular demoted "he,"
not a collective plural — turned out to be the single most load-bearing rule in this entire book,
applied from the opening verse onward rather than discovered partway through.

1. **The opening comfort passage (1:3-24) demotes almost entirely to Paul**, confirmed by Towns
   consistently naming him (*"My servant Paul was hurting at the same time you had great pain... he was
   not trusting in earthly deliverance"*) — a sharp contrast with how the same kind of "blessed be God"
   opening stayed general in earlier books. 1:9-10 needed the dangling-pronoun restructuring pattern
   established back in Romans: "God which raiseth the dead... Who delivered us" continues as one
   first-person unit once "God" resolves to "me" here (confirmed by Towns: *"Paul trusted Me to raise
   him"*), giving "but in me, who raise the dead... I delivered him... in me he trusteth that I will yet
   deliver him."
2. **Chapters 10-12, the "fool's speech," settle their own voice question from inside the text itself**:
   11:17's "That which I speak, I speak it not after the Lord, but as it were foolishly" is Paul
   explicitly disclaiming divine inspiration for his boasting — the same textual self-marking 1
   Corinthians 7:10/7:12 used to distinguish "the Lord's" commands from Paul's own judgment. Confirmed
   by Towns quoting the entire suffering catalog (11:24-27) as Paul's own direct speech (*"Paul said, 'I
   have served more time in prison, I have been beaten more times...'"*), this whole stretch — including
   the famous thorn-in-the-flesh account — stays demoted to third-person "he" throughout, with one
   careful exception:
3. **12:9's "he said unto me, My grace is sufficient for thee" required separating the narration frame
   from the quotation inside it** — Jesus speaking directly *to* Paul is quoted speech and stays exactly
   as-is (already first person, already addressing Paul as "thee," per the established rule that Jesus's
   own quoted speech is untouched), while the surrounding narration ("he said unto me") converts to "I
   said unto him" since the narrator is now Jesus, not Paul. This is the reverse of Hebrews 1's
   Father-to-Son quotations (which stay second-person because Jesus is *receiving* the address) — here
   Jesus is the one *giving* the address, so the quoted words themselves need no conversion at all.
4. **A genuinely necessary "us" vs. "you" distinction survives demotion in 4:12 and 4:14, and again in
   5:18-20** — "death worketh in us, but life in you" (4:12) only makes sense if "us" (Paul, the
   suffering minister) and "you" (the readers, who benefit) name two different parties; collapsing both
   to the same pronoun would erase the contrast the verse depends on. The same structural check applies
   to 5:20's ambassador language ("we are ambassadors for Christ... as though God did beseech you by
   us") — Towns' paraphrase broadens this to "You are My ambassadors," but the KJV's own grammar keeps
   ambassador ("us"/Paul) and recipient ("you"/the readers) distinct within the same sentence, so the
   literal structure was followed over Towns' generalization here.
5. **5:16's "though we have known Christ after the flesh" splits mid-verse**: the opening clause ("know
   we no man after the flesh") stays general "ye," but "we have known Christ after the flesh" is Paul's
   own specific pre-conversion biography (his former, merely-human view of the Messiah before Damascus
   Road), confirmed by Towns naming him specifically (*"Before Paul's conversion he knew about Me only as
   a human, now he knows Me differently"*) — the same single-verse-split pattern already used for 1
   Timothy 1:15 and 2 Timothy 2:8-9.
6. **6:2, 6:16-18 stack several Old Testament citations, all kept exactly as quoted**, including one
   already in first person from its own original context (6:2's "I have heard thee... have I succoured
   thee," God addressing His Servant, matching the Hebrews 1 Father-to-Son citation treatment) and one
   naming "a Father unto you... sons and daughters" without converting it even though it reads oddly for
   the Son to say of Himself — citations are preserved text, not narration, regardless of surface
   oddity, the same rule that has held since Mark 15:28.
7. **2 Corinthians 13:14, the most famous trinitarian benediction in the NT ("the grace of the Lord
   Jesus Christ, and the love of God, and the communion of the Holy Ghost"), was checked against the
   established trinitarian-formula exception (Ephesians 4:4-6, 1 Corinthians 12:4-6) and found NOT to
   qualify** — those formulas enumerate the three Persons side by side as a unified confession of who
   they are; 13:14 instead names three distinct gifts *from* three distinct givers, structurally
   identical to the dozens of ordinary "grace...from God...and the Lord Jesus Christ" salutations already
   converted throughout the whole project. Converted normally: "My grace, and my Father's love, and the
   communion of the Holy Ghost, be with you all."

Verification run: 257/257 verses present, chapter-by-chapter counts match `KJV.json` exactly
(24/17/18/18/21/18/16/24/15/18/33/21/14). Residual "God"/"Christ"/"Jesus" survivors (6 total) are every
one a deliberate exception (two compound "my Father, the God of X" titles, the "Son of God" self-merge,
"the Spirit of the living God," a citation-introduction "as God hath said," and 11:4's "another Jesus" —
a counterfeit figure false teachers preach, not a self-reference); zero residual "we/us/our" anywhere in
the book, the first time that's been true for a letter this personal; zero residual
"Jesus Christ"/"Lord Jesus"/"Christ Jesus"; zero unresolved dangling "Who/Whom/Which" verse-openers.

## Narrative rules (Acts) — a different genre entirely, and a new distinction the epistles never needed

Acts is not an epistle or the Gospels' third-person "he" for Jesus throughout — it is Luke's own
third-person historical narrative, almost entirely about *other people's* speeches, sermons, and
prayers (Peter's, Stephen's, Paul's, James's, an angel's, a demon's). Read against Elmer Towns'
entire Acts chapter (`Chapter045.html`, "My Legacy," his single continuous narrative covering all
28 KJV chapters) before drafting. Critical finding from that read: Towns achieves his "Jesus voice"
in Acts mainly through free paraphrase and invented devotional asides, not through pronoun-shifting
— applying the literal, pronoun-only method this project uses everywhere else would leave most of
the book essentially unchanged, since most of it is other people's quoted words. Checked this with
the user before drafting (see the three-option check-in); the user chose the strict, literal-rules-only
approach, matching the project's founding principle over Towns' technique.

1. **Rule 3 (other people's quoted speech about Jesus stays third-person) is the single most
   load-bearing rule in the whole book, by a wide margin.** Entire chapters are one continuous
   quotation and convert nothing at all: Peter's Pentecost sermon (2:14-40), his temple and council
   speeches (3:12-26, 4:8-12, 5:29-32), Stephen's 52-verse defense (7:2-53), James's Jerusalem
   Council ruling with its Amos citation (15:13-21), the council's letter (15:23-29), Paul's
   Areopagus sermon (17:22-31), his farewell to the Ephesian elders (20:18-35, the whole chapter),
   and — the sharpest case — Paul's own two later retellings of his Damascus road conversion before
   Agrippa and the Jerusalem crowd (22:1-21, 26:1-29) stay completely unconverted even though they
   are already first person and even embed Jesus's own quoted words ("I am Jesus of Nazareth, whom
   thou persecutest") — because the *speaker* is Paul recounting the event, not Luke narrating it
   directly. Three whole chapters (20, 22, 26) needed zero conversions for this reason, and a fourth
   (25) needed zero because it is entirely Festus/Agrippa/Paul's legal exchange with no narrator
   references to God/Jesus at all.
2. **The new distinction this book required: separating Luke's own narration (converts) from
   everyone else's direct quoted speech (Rule 3, never converts) — including Luke's *indirect*
   discourse summarizing what someone preached or believed**, which still counts as his narration
   and converts. "[Apollos] testified to the Jews that Jesus was Christ" (18:5) → "that I was
   Christ"; "he preached unto them Jesus" (17:18) → "he preached unto them me"; "declared... what
   things God had wrought" (15:12, 21:19) → "my Father had wrought." The test throughout: is this
   Luke telling the reader what happened/was believed, or is this someone's actual words being
   quoted? Only the former converts.
3. **A deliberate Father/Son split for Luke's own narration, carried consistently for all 28
   chapters**: "the Lord" in narration → "me/I" (Christ); "God" in narration → "my Father." So "an
   angel of the Lord" (12:23) → "an angel of mine," but "an angel of God" (10:3) → "an angel of my
   Father"; "believed on the Lord" (18:8) → "believed on me," but "worshipped God" (18:7) → "worshipped
   my Father." One deliberate cross-cutting exception: **"the word of God"/"the word of the Lord"/"the
   doctrine of the Lord," as a fixed idiom for the preached gospel message, always collapses to "my
   word"/"my doctrine" regardless of which of the two KJV words is used** (13:12, 13:44, 13:48-49,
   15:35, 17:13, 18:11, 19:10, 19:20) — since the content preached is specifically about Christ either
   way, unlike "grace of God" or "way of God," which keep the Father/Son split.
4. **Ambiguous or unidentified voices are left conservatively unconverted.** The vision-voice
   speaking to Peter in 10:13/10:15 ("What God hath cleansed...") is never named "the Lord" or
   "Jesus" in the text itself, so it stays as-is rather than guessing which Person is speaking.
   "The Spirit" alone, without "of God" or "of the Lord" attached (8:29, 10:19, 16:6-7, 20:23), is
   left as a distinct-Person title, matching the convention already established in 1 John/Jude for
   not folding every Spirit-reference into "my Spirit."
5. **The same narration-vs-quote line holds even inside one continuous scene**: at Stephen's death,
   Luke's own narration (7:55, "saw the glory of my Father, and me standing on the right hand")
   converts, but Stephen's own exclamation of the identical vision one verse later (7:56, "the Son of
   man standing on the right hand of God") stays completely unconverted, because it is now his quoted
   words, not Luke's narration — the same vision, two different grammatical treatments, both correct
   under Rule 3.
6. **A vision or angel's own direct words to a human are already first person and stay untouched**,
   same as Jesus's speech everywhere else in the project — Ananias's vision (9:10-16), Cornelius's
   angel (10:3-6), Paul's Macedonian vision (16:9-10, where only the narration frame "assuredly
   gathering that I had called us" converts, not the man's own quoted plea), and the angel on the
   ship (27:23-24, entirely inside Paul's own protected retelling, so it stays unconverted along with
   the rest of his speech).
7. **The established "kingdom of God" fixed-idiom exception (from Mark) recurs constantly** — 1:3,
   1:6, 8:12, 14:22, 19:8, 20:25, 28:23, 28:31 — and citations stay exactly as quoted regardless of
   pronoun, same rule as every prior book (7:32-34's God-speaking-to-Moses citation, Isaiah 6:9-10 in
   28:26-27).

Verification run: 1007/1007 verses present, chapter-by-chapter counts match `KJV.json` exactly for
all 28 chapters (26/47/26/37/42/15/60/40/43/48/30/25/52/28/41/40/34/28/41/38/40/30/35/27/27/32/44/31).
Residual "God"/"Christ"/"Jesus"/"Lord" survivors (185 verses) were checked individually and every one
falls under Rule 3 protected speech, the "kingdom of God" idiom, a citation, or Rule 4 address-to-Jesus
— none is a missed narration conversion. Three chapters (20, 22, 26) and one more (25) needed zero
conversions at all, the first time in the project a whole chapter has come back completely unchanged,
confirming just how narration-sparse this book is compared to the epistles.

## Closer full-text re-read of Acts finds two fixes

Applied the standard closer-read pass (every verse checked against `KJV.json` side by side, not just
judgment-call spot-checks) plus a full re-read of Elmer Towns' Acts chapter to cross-check judgment
calls a second time. Towns' heavy paraphrase style didn't surface any new verse-level guidance (as
expected — his technique is paraphrase, not pronoun-shifting, so it can't validate literal conversions
directly), but the side-by-side KJV comparison caught two real issues:

1. **1:4 had dropped the clause "which, saith he," instead of converting it** — the draft read "wait
   for the promise of my Father, which ye have heard of me," silently deleting the speech-tag rather
   than converting "he" to "I" the way every other narrator's-voice-tag has been handled throughout
   the whole project. Fixed to "which, saith I, ye have heard of me," preserving the KJV clause with
   only the pronoun shifted, consistent with the keep-the-wording, shift-only-the-person principle
   used everywhere else.
2. **11:23 and 13:43 rendered "the grace of God" as "my grace" instead of "my Father's grace,"
   inconsistent with the identical KJV phrase at 14:26 and 15:40** (both correctly converted to "my
   Father's grace" under the Father/Son narration split documented above). "The grace of God" is not
   part of the "word of God"/"word of the Lord" message-idiom exception (which always collapses to
   "my word" regardless of Father/Son, since the content preached is specifically about Christ) — it's
   an ordinary "of God" possessive and should follow the general rule. Both verses fixed to "my
   Father's grace" for consistency; re-verified against `KJV.json` (1007/1007 verses, all 28 chapters
   still match) and re-tested live (2,378 loads, zero errors).

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

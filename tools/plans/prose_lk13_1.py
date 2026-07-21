# -*- coding: utf-8 -*-
# Luke 13 §1.
#
# BLOCK 1 (53,68): read "But the synagogue leader, answering, indignant
#   because Jesus had healed on the Sabbath, was saying to the crowd that
#   “Six days…" — two stacked participles before the reason clause, then a
#   "that" in front of a direct quotation. Reordered so the causal participle
#   sits next to its own ὅτι-clause and the speech verbs come together:
#   "But the synagogue leader, indignant because Jesus had healed on the
#   Sabbath, answered and said to the crowd, “Six days…"
#     57 ἀγανακτῶν "indignant"      moves before 56 (stays "indignant")
#     56 ἀποκριθεὶς "answering,"  -> "answered and"  (the standard rendering
#        of the pleonastic aorist participle of ἀποκρίνομαι; still ἀποκριθεὶς)
#     64 ἔλεγεν "was saying"      -> "said"          (still the speech verb)
#     66 ὄχλῳ  "crowd"            -> "crowd,"        (comma introduces speech)
#     67 ὅτι   "that"             -> ""  folded. This is recitative ὅτι, which
#        marks a DIRECT quotation and has no English word; "that" in front of
#        an opening quotation mark is a reader stumble. Folding a particle with
#        no English of its own is the project's established convention.
#
# BLOCK 2 (68,71): read "“Six days there are in which…" — Greek order
#   (Ἓξ ἡμέραι εἰσὶν). Pure reorder to "“There are six days in which…";
#   εἰσὶν keeps "there are", Ἓξ keeps "six", ἡμέραι keeps "days". The opening
#   quotation mark travels with the new first word so it is not lost.
#
# BLOCK 3 (75,80): read "on those, then, coming, be healed—" — a bare
#   participle where English needs an imperative.
#     77 οὖν         "then,"   -> "so"       (fronted connective)
#     78 ἐρχόμενοι   "coming," -> "come"     (same verb, English imperative to
#        match the imperative θεραπεύεσθε it is subordinate to)
#     75 ἐν          "on"      unchanged
#     76 αὐταῖς      "those,"  -> "those days"  (αὐταῖς is anaphoric to ἡμέραι
#        four units back; English cannot carry a bare pronoun that far)
#     79 θεραπεύεσθε "be healed—" -> "and be healed—"
#   Gives "…to work; so come on those days and be healed— and not on the day
#   of the Sabbath!"
CHAPTER = "Luke 13"
SECTION = 1
BLOCKS = [
    (53, 68, [
        (53, None),             # δὲ            But
        (54, None),             # ὁ             the
        (55, None),             # ἀρχισυνάγωγος synagogue leader,
        (57, None),             # ἀγανακτῶν     indignant
        (58, None),             # ὅτι           because
        (59, None),             # Ἰησοῦς        Jesus
        (60, None),             # ἐθεράπευσεν   had healed
        (61, None),             # τῷ            on the
        (62, None),             # σαββάτῳ       Sabbath,
        (63, None),             # ὁ             (folded)
        (56, "answered and"),   # ἀποκριθεὶς
        (64, "said"),           # ἔλεγεν
        (65, None),             # τῷ            to the
        (66, "crowd,"),         # ὄχλῳ
        (67, ""),               # ὅτι           recitative — folded
    ]),
    (68, 71, [
        (70, "“There are"),     # εἰσὶν
        (68, "six"),            # Ἓξ
        (69, "days"),           # ἡμέραι
    ]),
    (75, 80, [
        (77, "so"),                 # οὖν
        (78, "come"),               # ἐρχόμενοι
        (75, None),                 # ἐν          on
        (76, "those days"),         # αὐταῖς
        (79, "and be healed—"),     # θεραπεύεσθε
    ]),
]

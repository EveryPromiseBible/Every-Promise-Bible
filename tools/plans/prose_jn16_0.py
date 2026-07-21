# -*- coding: utf-8 -*-
# Two defects in John 16 §0.
#
# BLOCK 1 — John 16:2 read "They will make you put out of the synagogue" — not
#   English. ποιήσουσιν is the causative "will make", and ἀποσυναγώγους is the
#   predicate adjective "excluded from the synagogue". Giving ἀποσυναγώγους its
#   own noun — "outcasts from the synagogue" — lets "make" do its job:
#   "They will make you outcasts from the synagogue". ποιήσουσιν is untouched;
#   one gloss changes, no unit moves.
#
# BLOCK 2 — John 16:12 read "Still many things I have for you to say—", which
#   an English reader parses as things for the DISCIPLES to say. ἔχω…λέγειν is
#   "I have…to say" and ὑμῖν is the dative "to you". Reordered to
#   "Still I have many things to say to you—". Gloss edits:
#     156 ὑμῖν   "for you" -> "to you—"  (dative; and it now ends the clause)
#     157 λέγειν "to say—" -> "to say"   (dash moves off it)
CHAPTER = "John 16"
SECTION = 0
BLOCKS = [
    (8, 9, [
        (8, "outcasts from the synagogue;"),   # ἀποσυναγώγους
    ]),
    (153, 158, [
        (153, None),          # Ἔτι     — Still
        (155, None),          # ἔχω     — I have
        (154, None),          # πολλὰ   — many things
        (157, "to say"),      # λέγειν
        (156, "to you—"),     # ὑμῖν
    ]),
]

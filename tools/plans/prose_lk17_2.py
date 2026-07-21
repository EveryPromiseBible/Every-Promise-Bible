# -*- coding: utf-8 -*-
# Luke 17 §2 read "For just as the lightning flashing from the one part under
# the sky to the other under the sky shines, so the Son of Man will be…" —
# the main verb λάμπει stranded eleven words behind its subject in Greek
# order, so the reader reaches "shines" long after losing the thread.
# Pure reorder to:
#   "For just as the lightning shines, flashing from the one part under the
#    sky to the other under the sky, so the Son of Man will be in his day."
# λάμπει keeps "shines" and moves next to its subject; ἀστράπτουσα keeps
# "flashing" and heads its own participial phrase. No gloss is re-anchored.
# Punctuation: the comma that sat on λάμπει goes to the new end of the
# phrase (οὐρανὸν, unit 76), and λάμπει takes a comma of its own.
CHAPTER = "Luke 17"
SECTION = 2
BLOCKS = [
    (67, 78, [
        (77, "shines,"),      # λάμπει
        (67, None),           # ἀστράπτουσα  flashing
        (68, None),           # ἐκ           from
        (69, None),           # τῆς          the
        (70, None),           # ὑπὸ          one part under
        (71, None),           # τὸν          the
        (72, None),           # οὐρανὸν      sky
        (73, None),           # εἰς          to
        (74, None),           # τὴν          the
        (75, None),           # ὑπ’          other under
        (76, "the sky,"),     # οὐρανὸν
    ]),
]

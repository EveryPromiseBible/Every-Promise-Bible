# -*- coding: utf-8 -*-
# Luke 2 §2 — five defects.
#
# 1. (6)   "And when eight days ... were completed, and his name was called
#    Jesus" — the Semitic apodosis καί leaves the sentence reading as a
#    fragment. Folded (Greek stays visible, English blank).
# 2. (39)  "just as it is written in the law of the Lord, that “Every male..."
#    — recitative ὅτι doubling the quotation mark. Folded.
# 3. (118) "and when the parents brought in the child Jesus, ... and he took
#    him into his arms" — same apodosis καί. Folded.
# 4. (198-203) "and of you yourself a sword will pierce the soul—" is Greek
#    order. -> "and a sword will pierce your own soul—". σοῦ δὲ keeps "your",
#    αὐτῆς keeps "own"; the bare article τὴν is folded because the possessive
#    now carries it.
# 5. (211-213) "And there was Anna a prophetess, daughter of Phanuel" reads as
#    two nouns jammed together. -> "And there was a prophetess, Anna,".
CHAPTER = "Luke 2"
SECTION = 2
BLOCKS = [
    (6, 7, [
        (6, ""),                    # καὶ — apodosis, folded
    ]),
    (39, 40, [
        (39, ""),                   # ὅτι — recitative, folded
    ]),
    (118, 119, [
        (118, ""),                  # καὶ — apodosis, folded
    ]),
    (198, 204, [
        (200, None),                # ῥομφαία      a sword
        (201, None),                # διελεύσεται  will pierce
        (202, ""),                  # τὴν — article folded under "your"
        (198, "your"),              # σοῦ δὲ
        (199, "own"),               # αὐτῆς
        (203, None),                # ψυχὴν        soul—
    ]),
    (211, 214, [
        (211, None),                # ἦν           there was
        (213, "a prophetess,"),     # προφῆτις
        (212, "Anna,"),             # Ἅννα
    ]),
]

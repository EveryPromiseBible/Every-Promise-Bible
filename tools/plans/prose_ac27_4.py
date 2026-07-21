# -*- coding: utf-8 -*-
# Acts 27:34 read "because of none of you will a hair perish from the head."
# The reader garden-paths on "because of none of you" (reading it as "on
# account of") and has to restart. Greek order: οὐδενὸς ὑμῶν θρὶξ ἀπολεῖται
# ἀπὸ τῆς κεφαλῆς. Reordered so the prepositional phrase leads and the negative
# stays where the Greek puts it: "because from the head of none of you will a
# hair perish."
# Pure reorder -- every gloss stays on its own word, negative included. Only the
# closing "." and quotation mark move from τῆς κεφαλῆς, no longer last, to
# ἀπολεῖται, now last.
CHAPTER = "Acts 27"
SECTION = 4
BLOCKS = [
    (116, 122, [
        (120, None),           # ἀπὸ         "from"
        (121, "the head"),     # τῆς κεφαλῆς
        (116, None),           # οὐδενὸς     "of none"
        (117, None),           # ὑμῶν        "of you"
        (118, None),           # θρὶξ        "will a hair"
        (119, "perish.”"),     # ἀπολεῖται
    ]),
]

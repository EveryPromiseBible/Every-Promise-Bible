# -*- coding: utf-8 -*-
# Acts 10 §0 read "And he, gazing at him and afraid becoming, said" — adjective
# before participle is Greek order. This gives "…and becoming afraid, said,".
# Pure reorder; only the comma moves to ἔμφοβος, which now closes the phrase.
CHAPTER = "Acts 10"
SECTION = 0
BLOCKS = [
    (57, 59, [
        (58, "becoming"),   # γενόμενος — comma moves off
        (57, "afraid,"),    # ἔμφοβος — now closes the phrase
    ]),
]

# -*- coding: utf-8 -*-
# Compound numeral: ἑβδομήκοντα carried the whole value "seventy-two" while δύο
# was blank — so clicking ἑβδομήκοντα ("seventy") reported "seventy-two", and
# δύο ("two") said nothing. Split across the two words, matching the corpus
# convention already used at Acts 1 ("a hundred twenty"), Acts 27, 1 Cor 10.
CHAPTER = "Luke 10"
SECTION = 0
BLOCKS = [
    (7, 9, [(7, "seventy"), (8, "two")]),
]

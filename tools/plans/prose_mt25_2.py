# -*- coding: utf-8 -*-
# Matthew 25 §2:
#  - "And will be gathered before him all the nations," -> "And all the nations
#    will be gathered before him,".  Pure reorder; the comma travels.
#  - "for one of these brothers of mine, the least, you did it for me"
#    -> "for one of the least of these brothers of mine, you did it for me".
#    Pure reorder; τῶν ἐλαχίστων takes the genitive "of the least".
#  - "for one of these the least, neither..." -> "for one of the least of
#    these, neither..."  Same fix, same two words.
CHAPTER = "Matthew 25"
SECTION = 2
BLOCKS = [
    (18, 24, [(18, None), (22, None), (23, "the nations"), (19, None),
              (20, None), (21, "him,")]),
    (136, 141, [(136, None), (140, "of the least"), (137, None), (138, None),
                (139, None)]),
    (223, 226, [(223, None), (225, "of the least"), (224, "of these,")]),
]

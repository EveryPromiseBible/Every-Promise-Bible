# -*- coding: utf-8 -*-
# Gloss drift: the bare article τοῦ carried the label "Father." while the noun
# πατρός μου was labelled only "of my". Clicking τοῦ showed "Father." over the
# article's lexicon entry.
# Fix by reordering: fold the article (Greek order restored τοῦ πατρός μου) and
# give the noun its full honest gloss "of my Father." Prose unchanged.
CHAPTER = "Matthew 26"
SECTION = 3
BLOCKS = [
    (184, 186, [(185, ""), (184, "of my Father.")]),
]

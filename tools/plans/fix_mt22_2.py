# -*- coding: utf-8 -*-
# Gloss drift: the bare article τῷ carried the label "brother." while the noun
# it belongs to, ἀδελφῷ αὐτοῦ, was labelled only "to his". Clicking τῷ showed
# "brother." over the article's lexicon entry.
# Fix by reordering: fold the article (Greek shown, English blank, Greek order
# restored τῷ ἀδελφῷ) and give the noun its full honest gloss "to his brother."
# Prose unchanged.
CHAPTER = "Matthew 22"
SECTION = 2
BLOCKS = [
    (49, 51, [(50, ""), (49, "to his brother.")]),
]

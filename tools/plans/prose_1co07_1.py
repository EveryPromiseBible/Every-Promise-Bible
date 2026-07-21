# -*- coding: utf-8 -*-
# 1 Corinthians 7:13 read "And a woman if any has an unbelieving husband..."
# That is the Greek order (καὶ γυνὴ εἴ τις ἔχει) left standing; the reader hits
# "a woman if any" and stops. The matching clause one verse earlier already
# reads "if any brother has an unbelieving wife", so this is also an internal
# inconsistency. Pure reorder plus one article change:
#   67 γυνὴ  "a woman" -> "woman"  (the indefinite article is now carried by
#      τις "any" at 69, so keeping "a" would double it)
# Gives: "And if any woman has an unbelieving husband and he consents to live
# with her, she isn't to divorce the husband."
CHAPTER = "1 Corinthians 7"
SECTION = 1
BLOCKS = [
    (66, 71, [
        (66, None),      # καὶ — "And"
        (68, None),      # εἴ — "if"
        (69, None),      # τις — "any"
        (67, "woman"),   # γυνὴ
        (70, None),      # ἔχει — "has"
    ]),
]

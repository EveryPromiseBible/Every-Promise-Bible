# -*- coding: utf-8 -*-
# Luke 12 §4 — four defects.
#
# 1-2. (87, 98) Recitative ὅτι rendered "that" immediately before an opening
#    quotation mark ("you say, that ‘A storm is coming,’" / "you say, that
#    ‘There will be scorching heat,’"). Both folded.
# 3. (104-112) "The face of the earth and of the sky you know how to
#    interpret;" — object before verb. -> "You know how to interpret the face
#    of the earth and of the sky;". Pure reorder; capital moves onto οἴδατε and
#    the semicolon onto οὐρανοῦ.
# 4. (121-124) "And why of yourselves do you not judge what is right?" — the
#    prepositional phrase splits "why" from the verb. -> "And why do you not
#    judge for yourselves what is right?" ἀπό with the reflexive is the idiom
#    "for/of yourselves", so ἀφ’ takes "for".
CHAPTER = "Luke 12"
SECTION = 4
BLOCKS = [
    (87, 88, [
        (87, ""),                    # ὅτι — recitative, folded
    ]),
    (98, 99, [
        (98, ""),                    # ὅτι — recitative, folded
    ]),
    (104, 113, [
        (111, "You know"),           # οἴδατε
        (112, "how to interpret"),   # δοκιμάζειν
        (104, "the"),                # τὸ
        (105, None),                 # πρόσωπον    face
        (106, None),                 # τῆς         of the
        (107, None),                 # γῆς         earth
        (108, None),                 # καὶ         and
        (109, None),                 # τοῦ         of the
        (110, "sky;"),               # οὐρανοῦ
    ]),
    (121, 125, [
        (123, None),                 # οὐ          do you not
        (124, None),                 # κρίνετε     judge
        (121, "for"),                # ἀφ’
        (122, None),                 # ἑαυτῶν      yourselves
    ]),
]

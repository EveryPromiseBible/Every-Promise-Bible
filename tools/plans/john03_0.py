# -*- coding: utf-8 -*-
# John 3 §0 — Born From Above (Nicodemus; John 3:16-18)
# DOCTRINE: 3:16 keeps "God" as subject and "the Son, the only-begotten"
# as the gift; 3:18 keeps "the only-begotten Son of God" (313-316, untouched);
# "the Son of Man" preserved (223-225 untouched, 239-241).
CHAPTER = "John 3"
SECTION = 0
BLOCKS = [
    # Now there was a man
    (0, 3, [(1,"Now"),(0,"there was"),(2,"a man")]),
    # Nicodemus his name,
    (6, 9, [(6,"Nicodemus"),(8,"his"),(7,"name,")]),
    # for no one is able to do these signs  (fold em-dash placeholder)
    (27, 33, [(27,"for no one"),(28,"is able"),(32,"to do"),(29,"these"),(30,""),(31,"signs")]),
    # unless God is with him.  (fold em-dash placeholder)
    (36, 42, [(36,"unless"),(39,"God"),(38,""),(37,"is"),(40,"with"),(41,"him.”")]),
    # Jesus answered and said to him,
    (42, 47, [(43,"Jesus"),(42,"answered"),(44,"and"),(45,"said"),(46,"to him,")]),
    # Nicodemus says to him,  (fold em-dash placeholder)
    (61, 66, [(65,"Nicodemus"),(64,""),(61,"says"),(62,"to"),(63,"him,")]),
    # How can a person be born when he is old?
    (66, 72, [(66,"“How"),(67,"can"),(68,"a person"),(69,"be born"),(71,"when he is"),(70,"old?")]),
    # Surely he cannot enter a second time into his mother's womb and be born?
    (72, 83, [(72,"Surely he cannot"),(80,"enter"),(79,"a second time"),(73,"into"),(78,"his"),(77,"mother's"),(75,"womb"),(74,""),(76,""),(81,"and"),(82,"be born?”")]),
    # Jesus answered,
    (83, 85, [(84,"Jesus"),(83,"answered,")]),
    # That which has been born of the flesh is flesh,
    (103,110,[(103,"That"),(104,"which has been born"),(105,"of"),(106,"the"),(107,"flesh"),(109,"is"),(108,"flesh,")]),
    # and that which has been born of the Spirit is spirit.
    (110,118,[(110,"and"),(111,"that"),(112,"which has been born"),(113,"of"),(114,"the"),(115,"Spirit"),(117,"is"),(116,"spirit.")]),
    # The wind blows where it wishes,
    (127,132,[(127,"The"),(128,"wind"),(131,"blows"),(129,"where"),(130,"it wishes,")]),
    # and you hear the sound of it—
    (132,137,[(132,"and"),(136,"you hear"),(133,"the"),(134,"sound"),(135,"of it—")]),
    # So is everyone born of the Spirit.  (fold em-dash placeholder)
    (145,153,[(145,"So"),(146,"is"),(147,"everyone"),(148,""),(149,"born"),(150,"of"),(151,"the"),(152,"Spirit.”")]),
    # Nicodemus answered and said to him,
    (153,158,[(154,"Nicodemus"),(153,"answered"),(155,"and"),(156,"said"),(157,"to him,")]),
    # Jesus answered and said to him,
    (162,167,[(163,"Jesus"),(162,"answered"),(164,"and"),(165,"said"),(166,"to him,")]),
    # and you do not understand these things?
    (174,177,[(175,"you do not"),(176,"understand"),(174,"these things?")]),
    # our testimony  (fold article)
    (190,193,[(192,"our"),(191,"testimony"),(190,"")]),
    # If I told you earthly things  (fold article)
    (195,200,[(195,"If"),(198,"I told"),(199,"you"),(196,""),(197,"earthly things")]),
    # heavenly things,  (fold article)
    (207,209,[(207,""),(208,"heavenly things,")]),
    # into heaven  (fold em-dash placeholder)
    (213,216,[(213,"into"),(214,""),(215,"heaven")]),
    # the One having come down from heaven—  (fold em-dash placeholder)
    (217,222,[(217,"the One"),(221,"having come down"),(218,"from"),(219,""),(220,"heaven—")]),
    # so must the Son of Man be lifted up,
    (235,242,[(235,"so"),(237,"must"),(238,"the"),(239,"Son"),(240,"of"),(241,"Man"),(236,"be lifted up,")]),
    # everyone believing in him may have eternal life.  (fold em-dash placeholder)
    (243,251,[(243,"everyone"),(244,""),(245,"believing"),(246,"in"),(247,"him"),(248,"may have"),(250,"eternal"),(249,"life.")]),
    # For so God loved the world,  (fold em-dash placeholder)   [John 3:16]
    (251,257,[(251,"For so"),(254,"God"),(253,""),(252,"loved"),(255,"the"),(256,"world,")]),
    # that he gave the Son, the only-begotten—
    (257,263,[(257,"that"),(262,"he gave"),(258,"the"),(259,"Son,"),(260,"the"),(261,"only-begotten—")]),
    # so that everyone believing in him may not perish but may have eternal life.  (fold em-dash placeholder)
    (263,275,[(263,"so that"),(264,"everyone"),(265,""),(266,"believing"),(267,"in"),(268,"him"),(269,"may not"),(270,"perish"),(271,"but"),(272,"may have"),(274,"eternal"),(273,"life.")]),
    # For God did not send the Son  (fold em-dash placeholder)   [John 3:17]
    (275,281,[(275,"For"),(278,"God"),(277,""),(276,"did not send"),(279,"the"),(280,"Son")]),
    # but so that the world might be saved through him.
    (288,295,[(288,"but"),(289,"so that"),(291,"the"),(292,"world"),(290,"might be saved"),(293,"through"),(294,"him.")]),
    # And this is the judgment:
    (317,322,[(318,"And"),(317,"this"),(319,"is"),(320,"the"),(321,"judgment:")]),
    # and people loved the darkness rather than the light—  (fold em-dash placeholder)
    (329,339,[(329,"and"),(331,""),(332,"people"),(330,"loved"),(334,"the"),(335,"darkness"),(333,"rather"),(336,"than"),(337,"the"),(338,"light—")]),
    # for their works were evil.
    (339,344,[(339,"for"),(340,"their"),(343,"works"),(342,""),(341,"were evil.")]),
    # For everyone practicing worthless things hates
    (344,348,[(344,"For everyone"),(346,"practicing"),(345,"worthless things"),(347,"hates")]),
    # so that his works may not be exposed;  (fold article)
    (356,362,[(356,"so that"),(361,"his"),(360,"works"),(359,""),(357,"may not"),(358,"be exposed;")]),
    # so that his works may be made manifest—  (fold article)
    (370,375,[(370,"so that"),(372,"his"),(374,"works"),(373,""),(371,"may be made manifest—")]),
    # that they have been worked in God.
    (375,380,[(375,"that"),(378,"they have"),(379,"been worked"),(376,"in"),(377,"God.")]),
]

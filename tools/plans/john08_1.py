# -*- coding: utf-8 -*-
# John 8 §1 — The Truth Will Set You Free
# DOCTRINE: keeps "the truth will set you free"; "if the Son sets you free,
# you will really be free"; "I came forth from God... but that One sent me";
# "You are of the father, the devil."
CHAPTER = "John 8"
SECTION = 1
BLOCKS = [
    # Then Jesus was saying to those Jews who had believed him:  (fold em-dash placeholder)
    (7, 16, [(8,"Then"),(10,"Jesus"),(9,""),(7,"was saying"),(11,"to"),(12,"those"),(15,"Jews"),(13,"who had believed"),(14,"him:")]),
    # in my word,  (fold two articles)
    (19, 24, [(19,"in"),(23,"my"),(21,"word,"),(20,""),(22,"")]),
    # truly you are my disciples;
    (24, 28, [(24,"truly"),(27,"you are"),(26,"my"),(25,"disciples;")]),
    # the truth will set you free.
    (33, 37, [(33,"the"),(34,"truth"),(35,"will set"),(36,"you free.”")]),
    # They answered him,
    (37, 40, [(37,"They answered"),(38,""),(39,"him,")]),
    # "We are Abraham's seed,
    (40, 43, [(42,"“We are"),(41,"Abraham's"),(40,"seed,")]),
    # and never have we been enslaved to anyone!
    (43, 47, [(43,"and"),(46,"never"),(45,"have we been enslaved"),(44,"to anyone!")]),
    # 'You will become free'?
    (51, 53, [(52,"‘You will become"),(51,"free’?”")]),
    # Jesus answered them,  (fold em-dash placeholder)
    (53, 57, [(56,"Jesus"),(55,""),(53,"answered"),(54,"them,")]),
    # everyone practicing sin is a slave of sin.  (fold two em-dash placeholders)
    (62, 71, [(62,"everyone"),(63,""),(64,"practicing"),(65,""),(66,"sin"),(68,"is"),(67,"a slave"),(69,"of"),(70,"sin.")]),
    # in the household forever;  (idiom: to the age)
    (75, 81, [(75,"in"),(76,"the"),(77,"household"),(80,"forever;"),(78,""),(79,"")]),
    # the son remains forever.  (idiom: to the age)
    (81, 87, [(81,"the"),(82,"son"),(83,"remains"),(86,"forever."),(84,""),(85,"")]),
    # the Son sets you free,
    (89, 93, [(89,"the"),(90,"Son"),(92,"sets"),(91,"you free,")]),
    # you will really be free.
    (93, 96, [(95,"you will"),(93,"really be"),(94,"free.")]),
    # that you are Abraham's seed;
    (97,101,[(97,"that"),(100,"you are"),(99,"Abraham's"),(98,"seed;")]),
    # but you seek to kill me,
    (101,105,[(101,"but"),(102,"you seek"),(104,"to kill"),(103,"me,")]),
    # because my word has no room in you.  (fold two articles)
    (105,114,[(105,"because"),(109,"my"),(107,"word"),(106,""),(108,""),(110,"has no"),(111,"room"),(112,"in"),(113,"you.")]),
    # and you therefore do what you heard from the father.
    (121,130,[(121,"and"),(122,"you"),(123,"therefore"),(129,"do"),(124,"what"),(125,"you heard"),(126,"from"),(127,"the"),(128,"father.”")]),
    # "Our father is Abraham!"  (fold article)
    (134,139,[(136,"“Our"),(135,"father"),(134,""),(138,"is"),(137,"Abraham!”")]),
    # Jesus says to them,  (fold em-dash placeholder)
    (139,143,[(142,"Jesus"),(141,""),(139,"says"),(140,"to them,")]),
    # "If you are children of Abraham,
    (143,148,[(143,"“If"),(147,"you are"),(144,"children"),(145,"of"),(146,"Abraham,")]),
    # you would be doing the works of Abraham.
    (148,153,[(152,"you would be doing"),(148,"the"),(149,"works"),(150,"of"),(151,"Abraham.")]),
    # But now you seek to kill me—
    (153,157,[(153,"But now"),(154,"you seek"),(156,"to kill"),(155,"me—")]),
    # a man who has spoken the truth to you,
    (157,163,[(157,"a man"),(158,"who"),(162,"has spoken"),(159,"the"),(160,"truth"),(161,"to you,")]),
    # which I heard from God.  (fold em-dash placeholder)
    (163,168,[(163,"which"),(164,"I heard"),(165,"from"),(166,""),(167,"God.")]),
    # the works of your father.
    (174,179,[(174,"the"),(175,"works"),(176,"of"),(178,"your"),(177,"father.”")]),
    # "We were not born out of sexual immorality;
    (181,186,[(181,"“We"),(184,"were not"),(185,"born"),(182,"out of"),(183,"sexual immorality;")]),
    # we have one Father— God!  (fold em-dash placeholder)
    (186,191,[(188,"we have"),(186,"one"),(187,"Father—"),(189,""),(190,"God!”")]),
    # Jesus said to them,  (fold em-dash placeholder)
    (191,195,[(194,"Jesus"),(193,""),(191,"said"),(192,"to them,")]),
    # "If God were your Father,  (fold em-dash placeholder)
    (195,201,[(195,"“If"),(196,""),(197,"God"),(200,"were"),(199,"your"),(198,"Father,")]),
    # for I came forth from God and have come.  (fold em-dash placeholder)
    (203,210,[(203,"for I"),(207,"came forth"),(204,"from"),(205,""),(206,"God"),(208,"and"),(209,"have come.")]),
    # For neither have I come from myself,
    (210,214,[(210,"For neither"),(213,"have I come"),(211,"from"),(212,"myself,")]),
    # but that One sent me.
    (214,218,[(214,"but"),(215,"that One"),(217,"sent"),(216,"me.")]),
    # Why do you not understand my speech?  (fold two articles)
    (218,225,[(218,"Why"),(223,"do you not"),(224,"understand"),(222,"my"),(220,"speech?"),(219,""),(221,"")]),
    # my word.  (fold two articles)
    (228,232,[(231,"my"),(229,"word."),(228,""),(230,"")]),
    # You are of the father, the devil,
    (232,239,[(232,"You"),(238,"are"),(233,"of"),(234,"the"),(235,"father,"),(236,"the"),(237,"devil,")]),
    # you want to do the desires of your father.
    (240,247,[(245,"you want"),(246,"to do"),(240,"the"),(241,"desires"),(242,"of"),(244,"your"),(243,"father.")]),
    # That one was a murderer from the beginning,
    (247,252,[(247,"That one"),(249,"was"),(248,"a murderer"),(250,"from"),(251,"the beginning,")]),
    # and does not stand in the truth,
    (252,258,[(252,"and"),(256,"does not"),(257,"stand"),(253,"in"),(254,"the"),(255,"truth,")]),
    # because there is no truth in him.
    (258,263,[(258,"because"),(259,"there is no"),(260,"truth"),(261,"in"),(262,"him.")]),
    # he speaks out of his own things,
    (267,271,[(270,"he speaks"),(267,"out of"),(269,"his own things,"),(268,"")]),
    # because he is a liar and the father of it.
    (271,278,[(271,"because"),(273,"he is"),(272,"a liar"),(274,"and"),(275,"the"),(276,"father"),(277,"of it.")]),
    # because I speak the truth,
    (279,283,[(279,"because"),(282,"I speak"),(280,"the"),(281,"truth,")]),
    # If I speak truth,
    (293,296,[(293,"If"),(295,"I speak"),(294,"truth,")]),
    # The one being of God hears the words of God.  (fold em-dash placeholder)
    (301,311,[(301,"The one"),(302,"being"),(303,"of"),(304,""),(305,"God"),(310,"hears"),(306,"the"),(307,"words"),(308,"of"),(309,"God.")]),
    # because you are not of God.  (fold em-dash placeholder)
    (316,321,[(316,"because"),(320,"you are not"),(317,"of"),(318,""),(319,"God.")]),
]

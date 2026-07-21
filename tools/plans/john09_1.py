# -*- coding: utf-8 -*-
# John 9 §1 — One Thing I Know
CHAPTER = "John 9"
SECTION = 1
BLOCKS = [
    # Now it was a Sabbath
    (8, 11, [(9,"Now"),(8,"it was"),(10,"a Sabbath")]),
    # on the day when Jesus made the mud  (fold em-dash placeholder)
    (11, 19, [(11,"on"),(13,"the day"),(12,"when"),(18,"Jesus"),(17,""),(16,"made"),(14,"the"),(15,"mud")]),
    # and opened his eyes.  (fold article)
    (19, 24, [(19,"and"),(20,"opened"),(21,"his"),(23,"eyes."),(22,"")]),
    # Then again the Pharisees also were asking him how he saw again.
    (24, 33, [(25,"Then"),(24,"again"),(29,"the"),(30,"Pharisees"),(28,"also"),(26,"were asking"),(27,"him"),(31,"how"),(32,"he saw again.")]),
    # "He put mud on my eyes,  (fold article)
    (36, 42, [(37,"“He put"),(36,"mud"),(39,"on"),(38,"my"),(41,"eyes,"),(40,"")]),
    # Then some of the Pharisees were saying,
    (46, 52, [(47,"Then"),(51,"some"),(48,"of"),(49,"the"),(50,"Pharisees"),(46,"were saying,")]),
    # "This man is not from God—
    (52, 56, [(53,"“This man"),(52,"is not"),(54,"from"),(55,"God—")]),
    # because he does not keep the Sabbath.
    (58, 63, [(58,"because"),(61,"he does not"),(62,"keep"),(59,"the"),(60,"Sabbath.”")]),
    # "How can a sinful man do such signs?"
    (65, 72, [(65,"“How"),(66,"can"),(68,"a sinful"),(67,"man"),(71,"do"),(69,"such"),(70,"signs?”")]),
    # And there was a division among them.
    (72, 77, [(72,"And"),(74,"there was"),(73,"a division"),(75,"among"),(76,"them.")]),
    # Then they say to the blind man again,
    (77, 82, [(78,"Then"),(77,"they say"),(79,"to the"),(80,"blind man"),(81,"again,")]),
    # since he opened your eyes?  (fold article)
    (87, 92, [(87,"since"),(88,"he opened"),(89,"your"),(91,"eyes?”"),(90,"")]),
    # "He is a prophet."
    (95, 97, [(96,"“He is"),(95,"a prophet.”")]),
    # Then the Jews did not believe about him
    (97,104,[(99,"Then"),(100,"the"),(101,"Jews"),(97,"did not"),(98,"believe"),(102,"about"),(103,"him")]),
    # the parents of the one who had seen again,  (fold redundant possessive)
    (111,116,[(111,"the"),(112,"parents"),(113,""),(114,"of the one"),(115,"who had seen again,")]),
    # "Is this your son,  (fold article)
    (120,125,[(121,"“Is"),(120,"this"),(124,"your"),(123,"son,"),(122,"")]),
    # whom you say that he was born blind?
    (125,131,[(125,"whom"),(126,"you"),(127,"say"),(128,"that"),(130,"he was born"),(129,"blind?")]),
    # Then his parents answered and said,
    (135,142,[(136,"Then"),(139,"his"),(138,"parents"),(137,""),(135,"answered"),(140,"and"),(141,"said,")]),
    # our son,  (fold article)
    (146,149,[(148,"our"),(147,"son,"),(146,"")]),
    # that he was born blind.
    (150,153,[(150,"that"),(152,"he was born"),(151,"blind.")]),
    # But how he now sees
    (153,156,[(153,"But how"),(155,"he sees"),(154,"now")]),
    # who opened his eyes—  (fold article)
    (159,164,[(159,"who"),(160,"opened"),(161,"his"),(163,"eyes—"),(162,"")]),
    # Ask him;
    (167,169,[(168,"Ask"),(167,"him;")]),
    # he is of age;
    (169,171,[(170,"he is"),(169,"of age;")]),
    # he himself will speak about himself.
    (171,175,[(171,"he himself"),(174,"will speak"),(172,"about"),(173,"himself.”")]),
    # These things his parents said  (fold article)
    (175,180,[(175,"These things"),(179,"his"),(178,"parents"),(177,""),(176,"said")]),
    # for the Jews had already agreed together
    (184,188,[(184,"for"),(186,"the"),(187,"Jews"),(185,"had already agreed together")]),
    # if anyone should confess him as Christ,
    (189,194,[(189,"if"),(190,"anyone"),(192,"should confess"),(191,"him"),(193,"as Christ,")]),
    # he would become put out of the synagogue.
    (194,196,[(195,"he would become"),(194,"put out of the synagogue.")]),
    # his parents said that  (fold article)
    (198,203,[(200,"his"),(199,"parents"),(198,""),(201,"said"),(202,"that")]),
    # "He is of age; ask him."
    (203,207,[(204,"“He is"),(203,"of age;"),(206,"ask"),(205,"him.”")]),
    # Then they called for a second time the man who had been blind,
    (207,216,[(208,"Then"),(207,"they called"),(211,"for"),(212,"a second time"),(209,"the"),(210,"man"),(213,"who"),(214,"had been"),(215,"blind,")]),
    # We know that this man is a sinner.  (fold doubled article)
    (223,231,[(223,"We"),(224,"know"),(225,"that"),(226,"this"),(227,""),(228,"man"),(230,"is"),(229,"a sinner.”")]),
    # Then that man answered,
    (231,234,[(232,"Then"),(233,"that man"),(231,"answered,")]),
    # "Whether he is a sinner I do not know.
    (234,239,[(234,"“Whether"),(236,"he is"),(235,"a sinner"),(237,"I do not"),(238,"know.")]),
    # that being blind, now I see!
    (241,246,[(241,"that"),(243,"being"),(242,"blind,"),(244,"now"),(245,"I see!”")]),
    # Then they said to him,
    (246,249,[(247,"Then"),(246,"they said"),(248,"to him,")]),
    # How did he open your eyes?  (fold article)
    (252,257,[(252,"How"),(253,"did he open"),(254,"your"),(256,"eyes?”"),(255,"")]),
    # Surely you too do not want to become his disciples?
    (269,276,[(269,"Surely"),(271,"you"),(270,"too"),(272,"do not want"),(275,"to become"),(273,"his"),(274,"disciples?”")]),
    # "You are a disciple of that man;
    (280,284,[(280,"“You"),(282,"are"),(281,"a disciple"),(283,"of that man;")]),
    # but we are disciples of Moses.
    (284,289,[(284,"but we"),(287,"are"),(288,"disciples"),(285,"of"),(286,"Moses.")]),
    # We know that God has spoken to Moses;  (fold em-dash placeholder)
    (289,296,[(289,"We"),(290,"know"),(291,"that"),(295,"God"),(294,""),(293,"has spoken"),(292,"to Moses;")]),
    # The man answered and said to them,
    (301,307,[(302,"The"),(303,"man"),(301,"answered"),(304,"and"),(305,"said"),(306,"to them,")]),
    # "For in this is the astonishing thing:
    (307,313,[(309,"“For"),(307,"in"),(308,"this"),(312,"is"),(310,"the"),(311,"astonishing thing:")]),
    # and he opened my eyes!  (fold article)
    (319,324,[(319,"and"),(320,"he opened"),(321,"my"),(323,"eyes!"),(322,"")]),
    # that God does not listen to sinners;  (fold em-dash placeholder)
    (325,331,[(325,"that"),(328,"God"),(327,""),(329,"does not"),(330,"listen"),(326,"to sinners;")]),
    # but if anyone is God-fearing and does his will—  (fold article)
    (331,341,[(331,"but"),(332,"if"),(333,"anyone"),(335,"is"),(334,"God-fearing"),(336,"and"),(340,"does"),(339,"his"),(338,"will—"),(337,"")]),
    # From of old it has not been heard
    (343,348,[(343,"From"),(344,""),(345,"of old"),(346,"it has not"),(347,"been heard")]),
    # that anyone opened the eyes of one born blind.
    (348,354,[(348,"that"),(350,"anyone"),(349,"opened"),(351,"the eyes"),(353,"of one born"),(352,"blind.")]),
    # If this man were not from God,
    (354,360,[(354,"If"),(357,"this man"),(356,"were"),(355,"not"),(358,"from"),(359,"God,")]),
    # "You were born entirely in sins—
    (367,372,[(369,"“You"),(370,"were born"),(371,"entirely"),(367,"in"),(368,"sins—")]),
]

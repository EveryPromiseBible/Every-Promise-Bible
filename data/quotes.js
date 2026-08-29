/* Quotes -- the people whose preaching and writing shaped this project.
 *
 * Hand-maintained. There is no builder and no source markdown: this file IS the
 * text. Add an entry and it appears in the Quotes tab and in the opening
 * rotation straight away.
 *
 *   text    the quote, as they actually wrote or said it -- never a paraphrase
 *   who     the person. Required; an entry without one is not shown
 *   source  optional: a book, sermon, letter or year
 *
 * TWO RULES, because nothing here can check them for you:
 *
 * 1. QUOTE WHAT THEY ACTUALLY SAID. A misattributed line is worse than no line,
 *    and worse than a wrong verse -- it puts words in a real person's mouth.
 *    Several of the most-repeated "Spurgeon" and "Luther" lines on the internet
 *    are not theirs. If a quote cannot be traced to a real work, leave it out.
 *
 * 2. KEEP THEM SHORT. Most of these writers are public domain -- Luther,
 *    Spurgeon, Mueller, Bunyan, Newton -- and carry no restriction at all. Some
 *    are not: a living or recent author is quoted here the way any book quotes
 *    one, briefly and with attribution. That is fair use of a sentence; it would
 *    not be fair use of a chapter.
 */
const QUOTES = [
  {
    text: "The person who can rightly divide Law and Gospel has reason to thank God. " +
          "He is a true theologian.",
    who: "Martin Luther"
  },
  {
    /* Table Talk entries below are Capt. Henry Bell's 1652 English translation of the
       German Tischreden, collected by Luther's student Aurifaber. Wording kept as
       translated, not modernized -- unlike the Bunyan entry further down (which
       swaps "thee/thou" for "you"), none of these used thee/thou so no substitution
       was needed. */
    text: "No man can bring his own righteousness before God.",
    who: "Martin Luther",
    source: "Table Talk (Tischreden), 1566"
  },
  {
    text: "Righteousness is obtained through faith, and not through works.",
    who: "Martin Luther",
    source: "Table Talk (Tischreden), 1566"
  },
  {
    text: "The Gospel is the power of God.",
    who: "Martin Luther",
    source: "Table Talk (Tischreden), 1566"
  },
  {
    text: "Grace condemneth all people's own righteousness.",
    who: "Martin Luther",
    source: "Table Talk (Tischreden), 1566"
  },
  {
    text: "Salvation is purchased and given unto us without our deserts.",
    who: "Martin Luther",
    source: "Table Talk (Tischreden), 1566"
  },
  {
    text: "The Gospel is like a fresh, mild, and cool air in the extreme heat of " +
          "summer, that is, a solace and comfort in the anguish of the conscience.",
    who: "Martin Luther",
    source: "Table Talk (Tischreden), 1566"
  },
  {
    text: "Faith is to build certainly on God's mercy.",
    who: "Martin Luther",
    source: "Table Talk (Tischreden), 1566"
  },
  {
    text: "Jesus Christ died for me, and through him I have a gracious God and " +
          "Father; Christ hath made an atonement for me.",
    who: "Martin Luther",
    source: "Table Talk (Tischreden), 1566"
  },
  {
    text: "For faith alone and the efficacious use of the word of God, bring " +
          "salvation.",
    who: "Martin Luther",
    source: "Concerning Christian Liberty, 1520"
  },
  {
    text: "As the soul needs the word alone for life and justification, so it " +
          "is justified by faith alone, and not by any works.",
    who: "Martin Luther",
    source: "Concerning Christian Liberty, 1520"
  },
  {
    text: "Christ is full of grace, life, and salvation; the soul is full of " +
          "sin, death, and condemnation. Let faith step in, and then sin, death, " +
          "and hell will belong to Christ, and grace, life, and salvation to the " +
          "soul.",
    who: "Martin Luther",
    source: "Concerning Christian Liberty, 1520"
  },
  {
    text: "If I have sinned, my Christ, in whom I believe, has not sinned; all " +
          "mine is His, and all His is mine.",
    who: "Martin Luther",
    source: "Concerning Christian Liberty, 1520"
  },
  {
    text: "It is not by working, but by believing, that we glorify God, and " +
          "confess Him to be true.",
    who: "Martin Luther",
    source: "Concerning Christian Liberty, 1520"
  },
  {
    text: "Good works do not make a good man, but a good man does good works.",
    who: "Martin Luther",
    source: "Concerning Christian Liberty, 1520"
  },
  {
    /* Bunyan wrote "Thy righteousness is in heaven"; modernised here to match the
       rest of the app, which does not print thee and thou anywhere else. */
    text: "Your righteousness is in heaven.",
    who: "John Bunyan",
    source: "Grace Abounding to the Chief of Sinners, 1666"
  },
  {
    text: "To run and work the law commands, but gives us neither feet nor hands; " +
          "but better news the gospel brings, it bids us fly and gives us wings.",
    who: "John Bunyan"
  },
  {
    text: "It shall greatly help thee to understand Scripture, if thou mark not only " +
          "what is spoken or written, but of whom, and unto whom, with what words, at " +
          "what time, where, to what intent, with what circumstance, considering what " +
          "goeth before, and what followeth after.",
    who: "Miles Coverdale",
    source: "Prologue to the Coverdale Bible, 1535"
  },
  {
    text: "No doctrine is so calculated to preserve a man from sin as the doctrine of " +
          "the grace of God. Those who have called it ‘a licentious doctrine’ did not " +
          "know anything about it. Poor ignorant things, they little knew that their own " +
          "vile stuff was the most licentious doctrine under heaven. If they knew the " +
          "grace of God in truth, they would soon see that there is no preservative from " +
          "lying like a knowledge that we are elect of God from the foundation of the " +
          "world. There is nothing like a belief in my eternal perseverance, and the " +
          "immutability of my Father’s affection, which can keep me near to Him from a " +
          "motive of simple gratitude.",
    who: "Charles Spurgeon"
  },
  {
    text: "The true preaching of the gospel of salvation by grace alone always leads to " +
          "the possibility of this charge being brought against it. There is no better " +
          "test as to whether a man is really preaching the New Testament gospel of " +
          "salvation than this, that some people might misunderstand it and misinterpret " +
          "it to mean that it really amounts to this, that because you are saved by grace " +
          "alone it does not matter at all what you do. If my preaching and presentation " +
          "of the gospel of salvation does not expose it to that misunderstanding, then " +
          "it is not the gospel.",
    who: "Martyn Lloyd-Jones"
  },
  {
    text: "Revival does not come to an end because of sin — otherwise it would never " +
          "have started. Revivals and great moves of God stop when the law is brought " +
          "in, and rules and regulations with it.",
    who: "Joseph Prince"
  },
  {
    text: "Grace functions best in the local church.",
    who: "Joseph Prince"
  },
  {
    text: "I saw more clearly than ever, that the first great and primary business to " +
          "which I ought to attend every day was, to have my soul happy in the Lord. The " +
          "first thing to be concerned about was not, how much I might serve the Lord, " +
          "how I might glorify the Lord; but how I might get my soul into a happy state, " +
          "and how my inner man might be nourished. For I might seek to set the truth " +
          "before the unconverted, I might seek to benefit believers, I might seek to " +
          "relieve the distressed, I might in other ways seek to behave myself as it " +
          "becomes a child of God in this world; and yet, not being happy in the Lord, " +
          "and not being nourished and strengthened in my inner man day by day, all this " +
          "might not be attended to in a right spirit.",
    who: "George Müller",
    source: "A Narrative of Some of the Lord's Dealings with George Müller, 1841"
  },
  {
    text: "The vilest enemies become trusted friends as soon as the covenant is cut.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 2, 1949"
  },
  {
    text: "The moment a covenant is solemnized, everything that a blood covenant man " +
          "owns in the world is at the disposal of his blood brother if he needs it, " +
          "and yet this brother would never ask for anything unless he were absolutely " +
          "driven by want to do it.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 3, 1949"
  },
  {
    text: "Abraham gave himself to God in utter abandonment of self.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 4, 1949"
  },
  {
    text: "God had found a man that would keep the Covenant; He had found a " +
          "covenant-keeping man.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 5, 1949"
  },
  {
    text: "God couldn't break the Covenant. He could not forget it nor ignore it. " +
          "He is the covenant-keeping God.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 6, 1949"
  },
  {
    text: "They were God's peculiar people. They were the treasure of the heart of God.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 7, 1949"
  },
  {
    text: "Jerusalem became the richest city the world had ever known. Their " +
          "hillsides were irrigated, their valleys teemed with wealth. There was no " +
          "city like it, no nation like it.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 7, 1949"
  },
  {
    text: "Jesus stands back of every sentence in the New Covenant.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 8, 1949"
  },
  {
    text: "The first covenant did not take away sin, it merely covered it.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 9, 1949"
  },
  {
    text: "But under the New Covenant our sins are not covered. They are put away. " +
          "They are remitted. They are as though they had never been.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 10, 1949"
  },
  {
    text: "This was the end of the Holy of Holies on earth. It was the beginning of " +
          "a New Covenant in His Blood.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 11, 1949"
  },
  {
    text: "What the Father forgives He forgets. A child of His should never dishonor " +
          "His Word by ever thinking of his sins again.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 12, 1949"
  },
  {
    text: "When God remits our sins, they are wiped out as though they had never been.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 13, 1949"
  },
  {
    text: "If you believe on Jesus Christ, He IS your righteousness. Then go out and " +
          "act it. Dare to let God loose in you.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 14, 1949"
  },
  {
    text: "We open up as a rose does to the sun, until the fulness of His love comes " +
          "flooding into our beings and then flows back again to Him, our own " +
          "wonderful Father.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 15, 1949"
  },
  {
    text: "Thanksgiving throws the door open wide, Praise keeps it open.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 16, 1949"
  },
  {
    text: "No disease nor infirmity can stand against the Name.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, ch. 17, 1949"
  },
  {
    text: "I've a right to grace, in the hardest place, On the ground of the Blood " +
          "Covenant; I've a right to peace that can never cease, On the ground of the " +
          "Blood Covenant.",
    who: "E. W. Kenyon",
    source: "The Blood Covenant, closing poem, ch. 18, 1949"
  },
  {
    text: "You cannot be under grace and not be holy any more than you can be " +
          "underwater and not be wet!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 1, 2015"
  },
  {
    text: "People get liberated and transformed when they encounter the Savior's love!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 2, 2015"
  },
  {
    text: "The Bible never defines God as wrath; it defines God as love.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 3, 2015"
  },
  {
    text: "Jesus gave of His own life to ransom yours.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 4, 2015"
  },
  {
    text: "When you understand the power of Jesus' ever-cleansing blood, fear and " +
          "depression give way to indescribable peace and joy.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 5, 2015"
  },
  {
    text: "Grace doesn't condone sin; it provides lasting freedom from sin.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 6, 2015"
  },
  {
    text: "A life that is founded upon the gospel of Jesus Christ is unshakable.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 7, 2015"
  },
  {
    text: "The cross of Calvary has made all the difference. It's the only answer " +
          "that will satisfy your guilty conscience.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 8, 2015"
  },
  {
    text: "There is no fear in God's love. His perfect love drives out all fears.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 9, 2015"
  },
  {
    text: "When people hear the real gospel that tells them how right Jesus' " +
          "finished work has made them, their lives will never be the same again.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 10, 2015"
  },
  {
    text: "God is looking for people who value and appreciate His Son. To the one " +
          "who values His Son, He gives every good thing He has.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 11, 2015"
  },
  {
    text: "The old covenant of law created separation between God and His people. " +
          "The new covenant of grace brings intimacy between God and His children.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 12, 2015"
  },
  {
    text: "Real holiness comes from beholding Jesus. As you behold our Lord, you " +
          "are transformed from the inside out, from glory to glory.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 13, 2015"
  },
  {
    text: "Grace isn't a teaching, doctrine, or formula. Grace is a person and His " +
          "name is Jesus!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 14, 2015"
  },
  {
    text: "Words of defeat, anger, bitterness, and complaint are toxic. Change your " +
          "words, and change your life.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 15, 2015"
  },
  {
    text: "When you see a believer struggling with sin, it is often a case of " +
          "mistaken identity. The best way to help him is to point him back to his " +
          "righteousness in Christ.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 16, 2015"
  },
  {
    text: "Don't ever underestimate the power of receiving. Man's greatest doing" +
          "—his greatest duty and greatest responsibility—is to humble himself to " +
          "receive from the Lord Jesus!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 17, 2015"
  },
  {
    text: "As you rest in the Lord's grace and finished work, you will receive " +
          "your restoration!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 18, 2015"
  },
  {
    text: "The grace revolution is a revolution of assurance and peace.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 19, 2015"
  },
  {
    text: "True maturity is a growing revelation of the Lord's grace and forgiveness.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 20, 2015"
  },
  {
    text: "Your turnaround happens when you begin to hear about God's grace.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 1, 2015"
  },
  {
    text: "What willpower and self-effort cannot do, God will do by the power of His " +
          "amazing grace.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 1, 2015"
  },
  {
    text: "God loves you, even with all your imperfections. Come to Him just as you are.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 2, 2015"
  },
  {
    text: "When God's love touches you in the deepest recesses of your heart, you begin " +
          "to experience inside-out transformation.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 2, 2015"
  },
  {
    text: "Jesus turned none away. Whatever their conditions—fevers, paralyses, deaf " +
          "ears, or demonic oppression—He healed them all.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 3, 2015"
  },
  {
    text: "When you know God's love for you, it will cause you to run to Him instead of " +
          "hiding from Him.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 3, 2015"
  },
  {
    text: "Righteousness is not about right doing. Righteousness is about right " +
          "believing. You are made righteous in God's eyes when you put your faith in " +
          "Christ.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 4, 2015"
  },
  {
    text: "The revelation of forgiveness does not detract from, nor is it at the expense " +
          "of, right living. Instead it is the fuel that makes right living happen.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 4, 2015"
  },
  {
    text: "The way to be liberated from sin's dominion is to come under grace.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 5, 2015"
  },
  {
    text: "Your assurance is founded upon what Jesus has done, not what you need to keep " +
          "doing.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 5, 2015"
  },
  {
    text: "Grace, not the law, is the truth that sets you free and transforms you.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 6, 2015"
  },
  {
    text: "God is not angry with you. Come back to a Father Who loves you and gave up His " +
          "beloved Son to ransom you from all your sins. This is the good news!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 6, 2015"
  },
  {
    text: "Right living comes by believing right.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 7, 2015"
  },
  {
    text: "Judgment and condemnation will not free you. Only the love and grace of our " +
          "Lord Jesus, Who shed His blood at Calvary for you, can do that.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 7, 2015"
  },
  {
    text: "In the same way that you can't touch water and not become wet, you can't touch " +
          "grace and not become holy.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 8, 2015"
  },
  {
    text: "The cross is the foundation for lasting breakthroughs and genuine inside-out " +
          "transformation!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 8, 2015"
  },
  {
    text: "Our God is love! He is slow to anger, gracious, and patient. He is full of " +
          "forgiveness, lovingkindness, and tender mercies.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 9, 2015"
  },
  {
    text: "Grace doesn't picket against those who fall short. Grace embraces them into " +
          "wholeness and brings about real inward transformation for them.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 9, 2015"
  },
  {
    text: "God's amazing grace transforms a person's heart and produces true holiness.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 10, 2015"
  },
  {
    text: "Don't depend on your willpower to say no to temptation. Depend on God's grace " +
          "and say yes to Jesus!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 10, 2015"
  },
  {
    text: "To really grow in grace and see its fruit manifest in our lives, we need to " +
          "keep hearing the Son and His words of grace.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 11, 2015"
  },
  {
    text: "Jesus is meekness and majesty, glory and humility personified! As we behold " +
          "Him, we are transformed to be like Him, from glory to glory.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 11, 2015"
  },
  {
    text: "The grace revolution is a revolution of relationship.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 12, 2015"
  },
  {
    text: "The grace revolution brings you near to God.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 12, 2015"
  },
  {
    text: "You can stop punishing yourself today by receiving the truth that Jesus took " +
          "all your punishment when He stood in your place at the cross.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 13, 2015"
  },
  {
    text: "Let your heart be all about Jesus, and not about accumulating, gathering, and " +
          "grabbing!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 13, 2015"
  },
  {
    text: "When you value Jesus in your life, you value His glory.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 14, 2015"
  },
  {
    text: "This is our position in Christ: highly favored and surrounded by favor!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 14, 2015"
  },
  {
    text: "Our tongues wield so much influence and power over our future and even our " +
          "day-to-day living.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 15, 2015"
  },
  {
    text: "Do you want to love life and see good days? Then start speaking it before you " +
          "even see it.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 15, 2015"
  },
  {
    text: "Grace opens the prison doors for those trapped in sin.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 16, 2015"
  },
  {
    text: "When you have Jesus as your Lord and Savior, you have a new and righteous " +
          "identity in Him.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 16, 2015"
  },
  {
    text: "Our Lord Jesus came that we might have life and have it more abundantly!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 17, 2015"
  },
  {
    text: "The Word of God makes this clear in no uncertain terms: you have been and you " +
          "continue to be forgiven in Christ.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 17, 2015"
  },
  {
    text: "Your best days are ahead of you!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 18, 2015"
  },
  {
    text: "You don't have to live bound by the shackles of legalism.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 18, 2015"
  },
  {
    text: "The grace revolution is a revolution of restoration of everything the enemy " +
          "has stolen—your health, your provision, your confidence, even your meaning and " +
          "purpose in life.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 19, 2015"
  },
  {
    text: "What Christ did—shedding His blood and dying on the cross—has fully met all " +
          "the claims of divine holiness in your life.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 19, 2015"
  },
  {
    text: "The test of whether the gospel of grace you are hearing is of the Lord, is if " +
          "He is bearing witness to the word being preached through lives changed, " +
          "healed, liberated, and transformed!",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 20, 2015"
  },
  {
    text: "We can talk openly and confess our mistakes and failings to the Lord, knowing " +
          "that He already knows them all and yet still loves us.",
    who: "Joseph Prince",
    source: "Grace Revolution, ch. 20, 2015"
  },
  {
    text: "If you can change what you believe, you can change your life!",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 1, 2013"
  },
  {
    text: "Your life will never be the same again when you personally experience His love!",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 2, 2013"
  },
  {
    text: "His love consumes all your anger, frustrations, disappointments, and pain. " +
          "His forgiveness envelops all your sins, failures, and mistakes.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 3, 2013"
  },
  {
    text: "The key to seeing what God sees is to base your beliefs on His sure and " +
          "unshakable Word.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 4, 2013"
  },
  {
    text: "Jesus didn't only pay for our sins, but He also took all of our shame.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 5, 2013"
  },
  {
    text: "When God blesses you, no one can reverse it.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 6, 2013"
  },
  {
    text: "Grace is not a license to sin; it is the answer to overcoming sin!",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 7, 2013"
  },
  {
    text: "Every time you fail, there is fresh grace from Jesus to rescue you.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 8, 2013"
  },
  {
    text: "We are forgiven because He was judged. We are accepted because He was " +
          "condemned!",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 9, 2013"
  },
  {
    text: "Wrong beliefs and thoughts will keep you defeated. Right beliefs and " +
          "thoughts will launch you toward your breakthrough.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 10, 2013"
  },
  {
    text: "The key to winning the battle for your mind is to learn how to separate " +
          "yourself from the evil thoughts planted by the enemy.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 11, 2013"
  },
  {
    text: "God is not mad at you, He is mad about you.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 12, 2013"
  },
  {
    text: "The only way that we can be delivered from occupation with self is to be " +
          "occupied with Christ.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 13, 2013"
  },
  {
    text: "The reason we study God's Word is not to merely accumulate Bible " +
          "knowledge and historical facts. It is to have a constant revelation of Jesus.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 14, 2013"
  },
  {
    text: "Worship Him and all your fears will fade away in the light of His glory " +
          "and grace.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 15, 2013"
  },
  {
    text: "Hope in the Lord for He is good, and His love for you endures forever!",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 16, 2013"
  },
  {
    text: "God is not offended when we ask Him for big things.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 17, 2013"
  },
  {
    text: "You cannot believe right unless you are hearing right.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 18, 2013"
  },
  {
    text: "It will never be about our love for God. It will always be about His " +
          "magnificent love for us.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 19, 2013"
  },
  {
    text: "The power to reign in life hinges on what you believe about God.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 20, 2013"
  },
  {
    text: "There is nothing that you can ever do to make Him love you more, and " +
          "nothing that you can ever do to make Him love you less.",
    who: "Joseph Prince",
    source: "The Power of Right Believing, ch. 21, 2013"
  },
  {
    text: "Stop depending on your self-efforts to earn and qualify for God's " +
          "blessings in your life.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 1, 2011"
  },
  {
    text: "Only the finished work of Jesus can bring us wholeness, completeness " +
          "and peace.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 2, 2011"
  },
  {
    text: "God blesses you not because you are good, but because He is good.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 3, 2011"
  },
  {
    text: "The more revelation you have of the grace of God and His forgiveness, " +
          "the more you will have the power to reign over all your challenges and " +
          "addictions.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 4, 2011"
  },
  {
    text: "Today, you are blessed because the Lord no longer counts your sins " +
          "against you. Because of the cross of Jesus, you will never be punished " +
          "for your sins again.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 5, 2011"
  },
  {
    text: "The good news of Jesus always liberates and His perfect love removes " +
          "every fear.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 6, 2011"
  },
  {
    text: "All who believe in Jesus receive the forgiveness of all their sins and " +
          "are justified from all things!",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 7, 2011"
  },
  {
    text: "Knowing that all your sins are forgiven is crucial for your health, " +
          "peace of mind, wholeness and wellness.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 8, 2011"
  },
  {
    text: "Knowing that you are completely forgiven destroys the power of sin in " +
          "your life.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 9, 2011"
  },
  {
    text: "God gave the law to bring man to the end of himself, so that he would " +
          "see his need for a Savior.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 10, 2011"
  },
  {
    text: "When you've failed, the Holy Spirit convicts you of righteousness, not " +
          "your sin.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 11, 2011"
  },
  {
    text: "If you are in Christ Jesus today, there is no condemnation over your " +
          "life!",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 12, 2011"
  },
  {
    text: "When you are under condemnation, fear, stress and all kinds of " +
          "sicknesses will follow.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 13, 2011"
  },
  {
    text: "Stop punishing yourself. Jesus has already been punished for your " +
          "sins. Believe it and let your conscience be satisfied!",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 14, 2011"
  },
  {
    text: "The devil wants you self-conscious, but God wants you Jesus-conscious.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 15, 2011"
  },
  {
    text: "God cannot see your sins when they are covered by the blood.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 16, 2011"
  },
  {
    text: "The law condemns the best of us, but grace saves the worst of us.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 17, 2011"
  },
  {
    text: "It is grace that leads people to true repentance and inward heart " +
          "transformation.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 18, 2011"
  },
  {
    text: "Victory over sin comes only when people encounter the superabundance " +
          "of God's grace.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 19, 2011"
  },
  {
    text: "Trying to balance grace with the law robs you of the power to reign " +
          "in life through the abundance of His grace.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 20, 2011"
  },
  {
    text: "Faith is bringing out of the spirit realm what is already there, what " +
          "is already true of you.",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 21, 2011"
  },
  {
    text: "Good things simply happen to you when you believe that God loves you!",
    who: "Joseph Prince",
    source: "Destined To Reign, ch. 22, 2011"
  },
  {
    text: "The same Jesus who purchased the forgiveness of all our sins also " +
          "removed all our diseases.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 1, 2019"
  },
  {
    text: "For God to create, He only had to speak. But for God to redeem us, " +
          "He had to bleed.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 2, 2019"
  },
  {
    text: "The more you see Jesus, the more you will have faith.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 3, 2019"
  },
  {
    text: "Jesus came to give you not just life, but life more abundantly!",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 4, 2019"
  },
  {
    text: "Your symptoms are real. But the power of God is even more real.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 5, 2019"
  },
  {
    text: "Grace is for the undeserving.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 6, 2019"
  },
  {
    text: "If you are a child of God, healing belongs to you.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 7, 2019"
  },
  {
    text: "There is no healing too big or too small for the Lord.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 8, 2019"
  },
  {
    text: "Faith is nothing more than looking to Jesus.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 9, 2019"
  },
  {
    text: "Faith and medicine don't have to be mutually exclusive.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 10, 2019"
  },
  {
    text: "God is for you and not against you.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 11, 2019"
  },
  {
    text: "When you touch Jesus, you touch healing.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 12, 2019"
  },
  {
    text: "Jesus didn't walk on water or calm storms all the time, but He healed " +
          "all the time.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 1, 2019"
  },
  {
    text: "We don't have to be perfect to come to the Lord's Table.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 1, 2019"
  },
  {
    text: "The answer is not found in creation; it is found in redemption!",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 2, 2019"
  },
  {
    text: "Sickness and disease have no right to be in our bodies, for our Lord " +
          "Jesus has already borne every sickness on His body!",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 2, 2019"
  },
  {
    text: "You have the blood-bought right to claim health and wholeness as " +
          "your portion.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 3, 2019"
  },
  {
    text: "The same power that raised Christ from the dead works for you.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 3, 2019"
  },
  {
    text: "Every stripe He bore was for our healing.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 4, 2019"
  },
  {
    text: "Stop believing that sickness is part of God's will. God wants you " +
          "well!",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 4, 2019"
  },
  {
    text: "His perfect love drives out every fear from our hearts.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 5, 2019"
  },
  {
    text: "The Lord Himself will fight your battle.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 5, 2019"
  },
  {
    text: "Come to Him just as you are. He will make you clean.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 6, 2019"
  },
  {
    text: "Under grace, when the clean touches the unclean, the unclean " +
          "becomes clean!",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 6, 2019"
  },
  {
    text: "There are no religious hoops to jump through to access His " +
          "healing power.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 7, 2019"
  },
  {
    text: "He paid the price for you to be uncommonly healthy, whole, and healed.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 7, 2019"
  },
  {
    text: "God's restoration is always greater than the original.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 8, 2019"
  },
  {
    text: "His ears are attentive to your softest sigh.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 8, 2019"
  },
  {
    text: "As a believer, you do not fight for victory; you fight from victory.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 9, 2019"
  },
  {
    text: "Everything you need from God has already been supplied to you " +
          "through the cross.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 9, 2019"
  },
  {
    text: "The word of God is health to all your flesh.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 10, 2019"
  },
  {
    text: "The price for your healing has been paid in full.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 10, 2019"
  },
  {
    text: "The Lord watches over you. Even while you sleep, He works the " +
          "night shift.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 11, 2019"
  },
  {
    text: "The Communion is not something you do; it's something you receive.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 11, 2019"
  },
  {
    text: "Pursue the Healer and not just the healing. When you have Him, " +
          "you have everything.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 12, 2019"
  },
  {
    text: "When you have Jesus, you have all you need.",
    who: "Joseph Prince",
    source: "Eat Your Way to Life and Health, ch. 12, 2019"
  }
];

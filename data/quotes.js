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
  }
];

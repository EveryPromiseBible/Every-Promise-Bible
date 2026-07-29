/* Verse commentary for the Illumination Translation.
 *
 * Keyed "Book C:V", matching the verse label the reader sees. A verse with an
 * entry here gets a small marker after its text; tapping it opens the note
 * underneath. Verses without an entry are untouched, so the reading page stays
 * clean and the notes stay optional.
 *
 * Blocks: h heading, p paragraph, ul bullet list, note a set-apart caution.
 * Written to be read by someone with no Greek. Hand-authored, not generated.
 */
const COMMENTARY = {

  "James 2:21": {
    title: "Shown to be right, or made righteous?",
    blocks: [
      { k: "p", t: "This verse has been argued over for five hundred years. Here is why our text reads shown to be right rather than justified or made righteous." },

      { k: "h", t: "The word itself means both" },
      { k: "p", t: "The Greek word is dikaioo. It carries two senses, and both are ordinary:" },
      { k: "ul", items: [
        "made right — a verdict, the way a judge declares it",
        "shown to be right — proof of something that was already true"
      ]},
      { k: "p", t: "Neither side can win this by pointing at the word. It will not choose between them. So the question has to be settled from the passage, not the dictionary." },

      { k: "h", t: "James answers it with dates" },
      { k: "p", t: "Two things happened in Abraham's life, a long way apart. In Genesis 15 he believed God, and God counted him righteous. In Genesis 22 he put Isaac on the altar. Those are chapters apart, and years apart." },
      { k: "p", t: "Now the key move: in the next verse but one, James quotes the earlier moment — the believing — and says the altar filled it full." },
      { k: "p", t: "So James himself puts the righteousness first and the altar second. If Abraham had been made righteous at the altar, the verse James quotes would be describing something that had not happened yet." },

      { k: "h", t: "A picture for it" },
      { k: "p", t: "A man passes his exams and is licensed as a doctor. Years later he saves a life in an emergency. Did the emergency make him a doctor? No. He already was one. The emergency showed it, in public, where everyone could see." },
      { k: "p", t: "That is Abraham. Righteous by believing, back in Genesis 15. The altar showed it, in Genesis 22." },

      { k: "h", t: "Three reasons this rendering stands" },
      { k: "ul", items: [
        "Shown to be right is a real, ordinary meaning of the word — nothing invented.",
        "James never says in front of God or in front of people. Those words are simply not in the chapter. Paul does add that kind of phrase when he writes about Abraham; James does not, and our text stays as quiet as he does.",
        "The whole passage runs on showing: show me, I will show you, do you need showing, look at what happened, you see it now."
      ]},

      { k: "h", t: "What should not be claimed" },
      { k: "note", t: "It would be too strong to say the Greek means shown and not made. The word genuinely carries both, and that claim can be knocked down in a moment — taking the good arguments with it. The honest statement is this: the word can mean either; we read it as shown because James's argument runs on showing, because he names no courtroom, and above all because he dates the righteousness to Genesis 15 and calls the altar its filling-full. That is a reading of the passage, not a fact about the word." }
    ]
  }

};

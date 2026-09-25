# Career Skills: exam prep

Everything for the Career Skills exam in one place: vocabulary and aptitude. It includes the handouts, answer keys, method notes, and a study app that works offline.

**Use it online:** [Career Skills Cram](https://claude.ai/artifact/C58vY42F73GW4d6HdeFE8W). This link works on a phone too.

## Start with Practice

**Practice is where you learn, and Mock test is where you check.** In Practice you answer one question at a time and see the explanation right away. Any question you get wrong **comes back three questions later, in any topic, until you get it right**. It's also saved to *My mistakes* so you can go through them again the next morning. Spend most of your time there, then take a mock test to see how you'd score.

**Or open `index.html` in a browser.** The app needs no install or internet connection (without internet it just uses the default fonts).

## What the paper looks like

The full breakdown by question type is in [`notes/what-to-expect.md`](notes/what-to-expect.md).

**Vocabulary.** The four revision tests (Sets A–D) all use the same format:

- **50 MCQs**, options A–D, one correct answer
- **About half are root-word questions**: "Which word best demonstrates the root *mort*?", "The root *mit* is associated with…"
- **The rest are synonyms and antonyms**: "closest synonym of *calumny*", "antonym of *languid*", "*jejune* argument is best described as…"
- Antonym questions nearly always include a **synonym as a trap option**. Check first whether the question asks for the same meaning or the opposite.

**The four sets share one pool of 97 questions** in different orders. Many questions appear in 3 or 4 of the sets, so if you learn the pool you have covered every set. After that, `Beyond the pool` in the app tests other words from the handouts that could be added.

**Aptitude & reasoning.** The self-assessment sheet has 30 MCQs: clocks, coding-decoding and number series (5 each), time & work (4), letter series (3), plus ratio, partnership, ages, provisions, games of skill and variation. The app's **Aptitude drill** writes new questions in the same types, so you can practise beyond these 30.

**Written.** Idioms and foreign phrases don't appear in the revision tests, but they have their own worksheets (sentence-making, meaning → idiom, fill in the blank). Cover those too in case the paper includes them.

## Tonight's plan (about 4½ hours)

| When | What | Where |
|---|---|---|
| 6:00–6:25 | Take **Set A** cold as a baseline and don't look anything up | App → Mock test → Set A |
| 6:25–7:05 | **Roots**: Practice → Root words until your misses stop coming back | App → Practice, then `notes/root-words.md` "traps" section |
| 7:05–7:45 | **Real test questions** in Practice: all 97, with misses repeated | App → Practice |
| 7:45–8:15 | **Aptitude self-assessment** (30 questions), then read the method for each type you missed | App → Mock test, then `notes/aptitude.md` |
| 8:15–8:35 | Break and eat | |
| 8:35–9:05 | **Real question pool** mock (50 random questions), then retake the ones you missed | App → Mock test |
| 9:05–9:35 | **Aptitude drill**: 30 new questions in the same types | App → Mock test |
| 9:35–10:00 | **Idioms & foreign phrases** worksheets with answers hidden | App → Worksheets |
| 10:00–10:30 | **Full rehearsal**: vocabulary and aptitude together | App → Mock test |
| 10:30–10:45 | **My mistakes** until the list is empty | App → Practice → My mistakes |
| Morning | 15 minutes: My mistakes, clock formulas (answers end in /11), root traps | |

Sleep before midnight. Recall the next day is better after sleep than after an extra hour of cramming.

## What's in here

```
index.html                       the study app (mock tests, aptitude drills, practice, flashcards, worksheets, look-up)
answer-keys/
  revision-tests.md              Sets A–D, every question with the answer and a one-line reason
  question-pool.md               the 97 unique questions grouped by type, most-repeated first
  idioms-worksheet.md            Q1 model sentences, Q2 answers
  foreign-phrases-worksheet.md   Part A answers, Part B model sentences
  aptitude-self-assessment.md    all 30 aptitude questions with worked solutions
notes/
  what-to-expect.md              question types to expect, with the mix per paper
  root-words.md                  ★ tested roots, look-alike traps, then all 68 roots
  synonyms-antonyms.md           ★ tested words, then the full 391-entry list
  idioms-phrases.md              ★ worksheet idioms, then all 178
  foreign-phrases.md             ★ worksheet expressions, then all 239
  aptitude.md                    how to spot and solve each aptitude type (clocks, coding, series, work …)
source-files/                    the original handouts, tests and the self-assessment sheet
data/                            the same content as JSON (the app is built from this)
app/template.html, tools/build.py
```

## How the answers were worked out

No answer key came with Sets A–D or the self-assessment. The vocabulary answers are worked out from the handouts (the root-word list and the synonym/antonym list), and every aptitude answer has its working shown. Each answer has a one-line reason, so you can check it. A few worksheet items are ambiguous as printed (foreign-phrases Part A items 1, 9, 11 and 16). The answer key explains the best choice for each.

Obvious typos in the handouts are corrected (for example *annual* → *annul*, *fruitive* → *furtive*). A few synonym-list entries look wrong in the source (Barbarous, Tyro, Winsome, Tenacious, Indifferent). They're marked ⚠ in the notes and left out of the app's generated questions.

## Rebuilding

After editing anything in `data/` or `app/template.html`:

```
python tools/build.py
```

This regenerates `index.html`, `notes/` and `answer-keys/`.

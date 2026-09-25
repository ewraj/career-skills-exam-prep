# Career Skills: exam prep

Everything for the Career Skills vocabulary exam in one place: the handouts, answer keys, short notes, and a study app that works offline.

**Use it online:** [Career Skills Cram](https://claude.ai/artifact/C58vY42F73GW4d6HdeFE8W). This link works on a phone too.

**Or open `index.html` in a browser.** The app needs no install or internet connection (without internet it just uses the default fonts).

## What the paper looks like

The four revision tests (Sets A–D) all use the same format:

- **50 MCQs**, options A–D, one correct answer
- **About half are root-word questions**: "Which word best demonstrates the root *mort*?", "The root *mit* is associated with…"
- **The rest are synonyms and antonyms**: "closest synonym of *calumny*", "antonym of *languid*", "*jejune* argument is best described as…"
- Antonym questions nearly always include a **synonym as a trap option**. Check first whether the question asks for the same meaning or the opposite.

**The four sets share one pool of 97 questions** in different orders. Many questions appear in 3 or 4 of the sets, so if you learn the pool you have covered every set. After that, `Beyond the pool` in the app tests other words from the handouts that could be added.

Idioms and foreign phrases don't appear in the revision tests, but they have their own worksheets (sentence-making, meaning → idiom, fill in the blank). Cover those too in case the paper includes them.

## Tonight's plan (about 4 hours)

| When | What | Where |
|---|---|---|
| 6:00–6:25 | Take **Set A** cold as a baseline and don't look anything up | App → Mock test → Set A |
| 6:25–7:10 | **Roots in the tests** (33 roots, the highest-yield topic) | App → Flashcards, then `notes/root-words.md` "traps" section |
| 7:10–8:00 | **Word pairs in the tests** (68 words) | App → Flashcards |
| 8:00–8:20 | Break and eat | |
| 8:20–8:50 | **Real question pool** mock (50 random questions), then retake the ones you missed | App → Mock test |
| 8:50–9:20 | **Idioms**: worksheet Q2 with answers hidden, then the worksheet idiom deck | App → Worksheets / Flashcards |
| 9:20–9:50 | **Foreign phrases**: Part A fill-in-the-blanks, then the worksheet phrase deck | App → Practice → Foreign worksheet |
| 9:50–10:20 | **Beyond the pool** mock | App → Mock test |
| 10:20–10:40 | **My mistakes** until the list is empty | App → Practice → My mistakes |
| Morning | 15 minutes: My mistakes plus `notes/root-words.md` traps | |

Sleep before midnight. Recall the next day is better after sleep than after an extra hour of cramming.

## What's in here

```
index.html                       the study app (mock tests, practice, flashcards, worksheets, look-up)
answer-keys/
  revision-tests.md              Sets A–D, every question with the answer and a one-line reason
  question-pool.md               the 97 unique questions grouped by type, most-repeated first
  idioms-worksheet.md            Q1 model sentences, Q2 answers
  foreign-phrases-worksheet.md   Part A answers, Part B model sentences
notes/
  root-words.md                  ★ tested roots, look-alike traps, then all 68 roots
  synonyms-antonyms.md           ★ tested words, then the full 391-entry list
  idioms-phrases.md              ★ worksheet idioms, then all 178
  foreign-phrases.md             ★ worksheet expressions, then all 239
source-files/                    the original handouts, tests and the self-assessment sheet
data/                            the same content as JSON (the app is built from this)
app/template.html, tools/build.py
```

## How the answers were worked out

No answer key came with Sets A–D, so every answer was worked out from the handouts: the root-word list and the synonym/antonym list. Each answer has a one-line reason, so you can check it. A few worksheet items are ambiguous as printed (foreign-phrases Part A items 1, 9, 11 and 16). The answer key explains the best choice for each.

Obvious typos in the handouts are corrected (for example *annual* → *annul*, *fruitive* → *furtive*). A few synonym-list entries look wrong in the source (Barbarous, Tyro, Winsome, Tenacious, Indifferent). They're marked ⚠ in the notes and left out of the app's generated questions.

## Rebuilding

After editing anything in `data/` or `app/template.html`:

```
python tools/build.py
```

This regenerates `index.html`, `notes/` and `answer-keys/`.

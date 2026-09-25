# Aptitude & reasoning: methods

The self-assessment sheet has 30 questions across 11 types. For each type below: how to recognise it, the method, and the trap. Numbers in brackets are sheet questions (Q#) you can check yourself against in `answer-keys/aptitude-self-assessment.md`.

## Clocks (5 of 30: Q1, Q14, Q15, Q22, Q23)

**Hand angles.** The minute hand moves 6°/min and the hour hand 0.5°/min, so the minute hand **gains 5.5° per minute**.

At H o'clock the minute hand is **30H° behind** the hour hand. To find a time between H and H+1:

| Hands are… | Minute hand must gain | Minutes past H |
|---|---|---|
| together (coincide) | 30H | 30H ÷ 5.5 = **60H/11** |
| opposite (180°) | 30H + 180 (if H < 6) or 30H − 180 (if H > 6) | gain ÷ 5.5 |
| at right angles (90°) | 30H − 90 or 30H + 90 (two answers per hour) | gain ÷ 5.5 |

Dividing by 5.5 is multiplying by 2/11. That's why every answer ends in **/11**: 180 × 2/11 = 360/11 = **32 8/11**.

- Q23: coincide between 7 and 8 → 210 × 2/11 = 420/11 = **38 2/11** → 7:38 2/11
- Q22: opposite between 4 and 5 → (120 + 180) × 2/11 = 600/11 = **54 6/11**
- Q14: right angle between 3 and 4 → 3:00 exactly is one; the one *between* 3 and 4 is (90 + 90) × 2/11 = **32 8/11**

**Fast or slow clocks.** Total error = rate × time elapsed. Count the elapsed time carefully: Monday noon to Thursday noon is **3 days**, not 4 (Q15). A clock that gains shows *ahead*; one that loses shows *behind*.

**Trap:** getting the direction wrong (gain vs loss), and counting days inclusively.

## Coding-decoding (5 of 30: Q2, Q5, Q9, Q21, Q25)

Write the alphabet positions once at the top of your rough sheet. **A1 E5 J10 O15 T20 Y25** ("EJOTY") gets you to any letter in a couple of steps.

Line the word up above the code, letter under letter, and check these in order:

1. **Same shift** for every letter (+2: RECTANGLE → TGEVCPING, Q2)
2. **Growing shift** +1, +2, +3 … (POWERFUL → QQZIWLBT, Q21). Undo it by subtracting.
3. **Reversal** (CARROM → MORRAC, Q9)
4. **Letter → number** by position (MIRROR → 13 9 18 18 …, Q5)
5. **Pair swaps / block reversal** (SIMPLE → IS PM EL, Q25)
6. **Opposite letters** (A↔Z, B↔Y: the two positions add to 27)

**Trap:** checking only the first two letters. Check at least three before trusting the pattern.

## Number series (5 of 30: Q7, Q8, Q10, Q17, Q24)

Work down this checklist and stop at the first thing that fits:

1. **Differences**: constant? squares (4, 9, 16, 25 → Q10)? growing by a constant (second differences, Q17)?
2. **× then +**: ×2+1, ×3+1 (Q24), ×2 plus a growing number (Q7)
3. **Two series interleaved**: odd places and even places follow separate rules (8, _, 11, _, 17 and 43, 41, 39 → Q8)
4. **n², n³, n² ± 1, n(n+1)**: 2, 6, 12, 20, 30 (used in Q20)

**Trap:** a fast-growing series is usually multiplication, not addition.

## Letter series (3 of 30: Q4, Q11, Q20)

Convert to numbers and treat each position separately. BDF, EGI, HJL is three separate +3 series (Q4). AZ, CX, FU is +2, +3, +4 going up and −2, −3, −4 going down (Q11). In alpha-numeric terms like C2X, F6U, the letters and numbers follow separate rules (Q20).

## Time & work (4 of 30: Q13, Q16, Q29, Q30)

**One formula covers most of them:**

> M₁ × H₁ × D₁ / W₁ = M₂ × H₂ × D₂ / W₂
> (men × hours per day × days, divided by the amount of work)

- Q13: 8 × 9 × 10 / 24 = M × 6 × 8 / 32 → M = 20
- Q16: "8 men, 8 carpets, 8 days": 1 man makes 1 carpet in 8 days → 16 × 16 / 8 = 32

**Mixed workers:** convert everyone into one unit first. If 24 men = 36 women, then 1 man = 1.5 women (Q30). If two gangs finish the same job, set their totals equal and solve for the exchange rate (Q29: b = 2m).

**Trap:** forgetting a "three times the work" multiplier (Q29).

## Ratio (2 of 30: Q12, Q28)

- Numbers in ratio a : b are **ak and bk**. Put them into the condition and solve for k (Q12: k = 11).
- To chain ratios, multiply them: A/B × B/C = A/C (Q28 → 15 : 8).

## Partnership (2 of 30: Q3, Q26)

**Profit ∝ capital × months.** If capital changes mid-year, add the pieces: 2 × 6 + 4 × 6 (Q3). "Profit divided equally" means capital × months is the same for both partners (Q26).

**Trap:** "joined after m months" means they were in the business for **12 − m** months.

## Ages (Q27)

Let the past ages be 13k and 17k. Add the *total* gap to reach the future: 10 years back + 17 years forward = **+27**. Solve for k, then add the 10 years back to get present ages.

## Provisions (Q6)

Food = men × days. After 10 days, 150 men × 35 days of food are left. Divide by the new number of men.

## Games of skill (Q18)

"A can give B 15 points in 60" → A : B = 60 : 45. Chain the ratios to A : C, then scale to the game length.

## Variation (Q19)

"Directly proportional to Q, inversely to √R" → P = kQ/√R. Find k from the first set of values, then plug in the second.

"""Rebuild index.html, notes/ and answer-keys/ from data/*.json.

    python tools/build.py                 # writes index.html + markdown
    python tools/build.py --artifact X    # also writes a body-only copy of the app to X
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data"


def load(name):
    return json.loads((D / name).read_text(encoding="utf-8"))


rev, sets = load("revision_questions.json"), load("revision_sets.json")
synant, roots = load("synonyms_antonyms.json"), load("roots.json")
idioms, foreign, ws = load("idioms.json"), load("foreign_phrases.json"), load("worksheets.json")
L = "ABCD"


def write(rel, text):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.strip() + "\n", encoding="utf-8")
    print("wrote", rel)


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


# ------------------------------------------------------------------ app
data = {"rev": rev, "sets": sets, "synant": synant, "roots": roots, "idioms": idioms, "foreign": foreign, "ws": ws}
body = (ROOT / "app" / "template.html").read_text(encoding="utf-8")
body = body.replace("/*__DATA__*/", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '</head>\n<body>\n' + body + "\n</body>\n</html>\n")
(ROOT / "index.html").write_text(page, encoding="utf-8")
print("wrote index.html", f"({len(page) // 1024} KB)")
if "--artifact" in sys.argv:
    out = Path(sys.argv[sys.argv.index("--artifact") + 1])
    out.write_text(body, encoding="utf-8")
    print("wrote", out)

# ------------------------------------------------------------------ answer keys: revision tests
by_id = {q["id"]: q for q in rev}
md = ["# Revision tests A–D — answer key", "",
      "No official key came with the sets, so these answers are worked out from the handouts (root-word list and synonym/antonym list).",
      "The four sets are the **same pool of 97 questions** in different orders — learn the pool and you've covered all four.", ""]
for letter, rows in sets.items():
    md += [f"## Set {letter}", "", "Quick check: " + "  ".join(f"`{r['n']}-{L[by_id[r['id']]['ans']]}`" for r in rows), "",
           "| # | Question | Answer | Why |", "|---|---|---|---|"]
    for r in rows:
        q = by_id[r["id"]]
        md.append(f"| {r['n']} | {cell(q['q'])} | **{L[q['ans']]}. {cell(q['opts'][q['ans']])}** | {cell(q['why'])} |")
    md.append("")
write("answer-keys/revision-tests.md", "\n".join(md))

md = ["# The 97-question pool (deduplicated)", "", "Every unique question from Sets A–D, grouped by type. `Sets` shows where each one appears — the ones in all four sets are the likeliest repeats.", ""]
for topic, title in (("root", "Root words"), ("syn", "Synonyms & meanings"), ("ant", "Antonyms")):
    qs = sorted((q for q in rev if q["topic"] == topic), key=lambda q: -len(q["sets"]))
    md += [f"## {title} ({len(qs)})", "", "| Question | Answer | Sets |", "|---|---|---|"]
    md += [f"| {cell(q['q'])} | **{cell(q['opts'][q['ans']])}** | {', '.join(q['sets'])} |" for q in qs]
    md.append("")
write("answer-keys/question-pool.md", "\n".join(md))

# ------------------------------------------------------------------ answer keys: worksheets
md = ["# Idioms & Phrases worksheet — answer key", "", "## Q2. Write the idiom for each meaning", "", "| # | Meaning | Idiom |", "|---|---|---|"]
md += [f"| {r['letter']} | {cell(r['meaning'])} | **{cell(r['answer'])}** |" for r in ws["idioms_q2"]]
md += ["", "## Q1. Sentences (model answers — write your own in the exam)", "", "| Idiom | Meaning | Sentence |", "|---|---|---|"]
imap = {i["idiom"].lower(): i["meaning"] for i in idioms}
md += [f"| **{cell(r['item'])}** | {cell(imap.get(r['item'].lower(), ''))} | {cell(r['sentence'])} |" for r in ws["idioms_q1"]]
md += ["", "_Note: the sheet prints “Jumbo Jumbo” — it means **Mumbo Jumbo**._"]
write("answer-keys/idioms-worksheet.md", "\n".join(md))

md = ["# Foreign Words & Phrases worksheet — answer key", "", "## Part A. Fill in the blank", "",
      "| # | Sentence | Options | Answer | Note |", "|---|---|---|---|---|"]
md += [f"| {r['n']} | {cell(r['q'])} | {' / '.join(r['opts'])} | **{cell(r['opts'][r['ans']])}** | {cell(r['why'])} |" for r in ws["foreign_a"]]
md += ["", "Items 1, 9, 11 and 16 are loosely worded on the sheet — the note gives the best pick and why.", "",
       "## Part B. Use in a sentence (model answers)", "", "| Term | Meaning | Sentence |", "|---|---|---|"]
md += [f"| **{cell(r['term'])}** | {cell(r['meaning'])} | {cell(r['sentence'])} |" for r in ws["foreign_b"]]
write("answer-keys/foreign-phrases-worksheet.md", "\n".join(md))

# ------------------------------------------------------------------ notes
t = [r for r in roots if r["tested"]]
md = ["# Root words", "", f"★ = used in the revision tests ({len(t)} of {len(roots)}). About half of every test paper is root-word questions, so this is the highest-yield page.", "",
      "## ★ Tested roots — learn these cold", "", "| Root | Means | Examples |", "|---|---|---|"]
md += [f"| **{cell(r['root'])}** | {cell(r['meaning'])} | {cell(r['examples'])} |" for r in t]
md += ["", "## Look-alikes the paper uses as traps", "",
       "- **mal** (bad) vs **bene** (good) · **phil** (love) vs **mis/miso** (hate)",
       "- **hypo** (below) vs **hyper** (above) · **homo** (same) vs **hetero** (different)",
       "- **mono** (one) vs **multi** (many) · **ego / auto** both = self",
       "- **port** (carry) vs **fort** (strength) vs **mort** (death)",
       "- **duc** (lead) · **dict** (say) · **scrib** (write) · **mit** (send) · **spect** (look) · **vis/vid** (see)",
       "- **aqua** (Latin) and **hydr** (Greek) both = water · **fract** and **rupt** both = break",
       "- **pater** (father) vs **mater** (mother) · **para** = beyond/beside (paranormal, paralegal)", "",
       "## All roots", "", "| Root | Means | Origin | Examples |", "|---|---|---|---|"]
md += [f"| {'★ ' if r['tested'] else ''}**{cell(r['root'])}** | {cell(r['meaning'])} | {r['origin']} | {cell(r['examples'])} |" for r in roots]
write("notes/root-words.md", "\n".join(md))

t = [e for e in synant if e["tested"]]
md = ["# Synonyms & antonyms", "", f"★ = the word appears in the revision tests ({len(t)} of {len(synant)} entries). Spellings from the handout are corrected (annul, furtive, naive, incite).", "",
      "**Exam trick:** in antonym questions, at least one wrong option is a *synonym* (e.g. antonym of *callous* → options include *insensitive*). Decide first whether the question wants same or opposite.", "",
      "## ★ Tested words", "", "| Word | Synonyms | Antonyms |", "|---|---|---|"]
md += [f"| **{cell(e['word'])}** | {cell(e['syn'])} | {cell(e['ant'])} |" for e in t]
md += ["", "## Full list A–Z", "", "| Word | Synonyms | Antonyms |", "|---|---|---|"]
md += [f"| {'★ ' if e['tested'] else ''}**{cell(e['word'])}** | {cell(e['syn'])} | {cell(e['ant'])}{' ⚠ ' + cell(e['note']) if e.get('note') else ''} |" for e in synant]
write("notes/synonyms-antonyms.md", "\n".join(md))

t = [i for i in idioms if i["worksheet"]]
md = ["# Idioms & phrases", "", f"★ = on the worksheet ({len(t)} of {len(idioms)}).", "", "## ★ Worksheet idioms", "", "| Idiom | Meaning |", "|---|---|"]
md += [f"| **{cell(i['idiom'])}** | {cell(i['meaning'])} |" for i in t]
md += ["", "## Full list", "", "| Idiom | Meaning |", "|---|---|"]
md += [f"| {'★ ' if i['worksheet'] else ''}**{cell(i['idiom'])}** | {cell(i['meaning'])} |" for i in idioms]
write("notes/idioms-phrases.md", "\n".join(md))

t = [f for f in foreign if f["worksheet"]]
md = ["# Foreign words & phrases", "", f"★ = on the worksheet ({len(t)} of {len(foreign)}). Entries marked _(sheet)_ appear on the worksheet but not in the 200-word list, so their meanings are added here.", "",
      "## ★ Worksheet expressions", "", "| Expression | Meaning | From |", "|---|---|---|"]
md += [f"| **{cell(f['phrase'])}** | {cell(f['meaning'])} | {f['lang']}{' _(sheet)_' if f.get('extra') else ''} |" for f in t]
md += ["", "## Full list", "", "| Expression | Meaning | From | Use |", "|---|---|---|---|"]
md += [f"| {'★ ' if f['worksheet'] else ''}**{cell(f['phrase'])}** | {cell(f['meaning'])} | {f['lang']} | {f['freq']} |" for f in foreign]
write("notes/foreign-phrases.md", "\n".join(md))

# GRIET AI/ML 2026 — Delivery Workspace

**Owner:** Narasimha Kanumuri
**Scope:** Remaining 144 official hours / 24 teaching days
**Structure version:** v1.0

---

## The two categories

| Category | Folder | Who sees it | Rule |
|---|---|---|---|
| **Student Share** | `01_STUDENT_SHARE/` | Released to students | English first. Code is typed by the student, never pasted from me. |
| **Teacher Only** | `02_TEACHER_ONLY/` | Never released | Solutions, bug keys, run sheets, question banks, slide source. |

Plus:

| Folder | Purpose |
|---|---|
| `00_COURSE_REFERENCE/` | Contract-level docs: cluster map, day map, teaching rules, KEY register |
| `03_SHARED_ASSETS/` | Reusable generators and cheatsheets used across many days |

---

## Release model — step-by-step, not all at once

Inside every day, student files are numbered `STEP_00` … `STEP_08`.
You release **one step at a time** during class.

```
STEP_00  Today's map          → shown on screen
STEP_01  Generate your data   → students run generator
STEP_02  Plain-English spec   → students TYPE the Python
STEP_03  Debug lab            → you inject bugs, they fix
STEP_04  The pain             → discussion, no new file
STEP_05  NumPy English spec   → students TYPE the NumPy
STEP_06  Pandas English spec  → students TYPE the Pandas
STEP_07  Chart English spec   → students TYPE the plot
STEP_08  Challenge + exit     → independent work
```

**Why English `.md` and not `.py`:**
Students read the sentence, then translate it into code themselves.
Typing is the learning. Pasting is not.

---

## Naming convention

```
DayNN_Project_Name/
  A_English_Spec/     STEP_NN_topic.md
  B_Starter_Files/    only skeletons with TODO markers
  C_Data/             generator output lands here
  D_Homework/         practice brief for that night
```

Teacher mirror:

```
DayNN_Project_Name/
  A_Solutions/        stepNN_solution.py
  B_Bug_Key/          bug ladder + reveal order
  C_Teaching_Notes/   minute-by-minute run sheet
  D_Question_Bank/    recall / predict / debug / apply
  E_Slides_Source/    slide outline for the day
```

---

## Non-negotiable delivery rules

1. **Never open with a definition.** Historical problem → KEY → ELI5 → code.
2. **Earn every tool.** Plain Python → bugs → fix → feel the pain → introduce the next tool.
3. **English before code.** Every line exists as a human sentence first.
4. **Bugs are layered.** Visible, name/case, silent logic, off-by-one, state, assumption, runs-but-wrong.
5. **One KEY per concept.** Must survive six months of forgetting.
6. **Every block ends in a visible outcome.**
7. **No live account creation, no API auth in class.**
8. **Homework mirrors the class workflow on a different dataset** — never the same answers.

---

## Source basis

- `GRIET_Aug2026_180.xlsx` — official curriculum and hours
- `GRIET_Spiral_Project_Framework.docx` — sub-topic coverage audit (S-refs)
- `GRIET_AIML_2026_Concentration_Guide.docx` — concentration levels, recovery plan
- `GRIET_AIML_144Hour_Delivery_Pack.docx` — cluster map, day map, deliverables
- `GRIET Teaching Framework v1.loop` — the 21 teaching rules
- `GRIET PPT Planning Discussion.page` — pace rule, PPT vs question bank

# Locked Teaching Rules — Working Contract v1.0

Applies to every day, every file, every artifact in this workspace.

---

## R1 — Never start with the tool

Order is fixed:

```
Historical reality
→ what people actually did
→ what broke
→ what was created
→ KEY memory hook
→ ELI5
→ code
```

Never open a topic with a definition.

---

## R2 — The Pain-to-Relief Ladder  ⭐ core rule

Every new tool must be **earned**. Eight stages, in order:

| # | Stage | What happens |
|---|---|---|
| 1 | Plain version | Solve it with what students already know |
| 2 | Inject bugs | Deliberate, layered errors |
| 3 | Debug | Students find and fix |
| 4 | Working code | Visible success |
| 5 | **Show the pain** | Count the lines, scale the data, break the assumption |
| 6 | Introduce next tool | Only now |
| 7 | Same task, fewer lines | Side-by-side |
| 8 | KEY + lock | Memory hook |

### Ladder per cluster

| Cluster | Pain | Relief tool |
|---|---|---|
| C1 | Python loops repeated | NumPy |
| C1 | NumPy can't hold mixed types / labels | Pandas |
| C1 | Reading 30 rows by eye | Matplotlib |
| C1 | Real data is dirty | Cleaning |
| C2 | Hand-written thresholds guess badly | scikit-learn |
| C2 | "It looks good" is not evidence | Metrics |
| C3 | Hand-crafted features fail on images/text | Neural networks |
| C4 | LLM answers from memory and invents facts | RAG |
| C5 | LLM can talk but cannot act | Agents + MCP |
| C5 | Notebook only runs on your laptop | Deployment |

---

## R3 — English before code

Every construct appears first as a human sentence, then as a literal translation.

| English | Code |
|---|---|
| Repeat this 10 times | `for i in range(10):` |
| Add everything up | `total = total + value` |
| Keep only the big ones | `df[df["Minutes"] > 100]` |
| Put same things together and count | `df.groupby("App").size()` |

Students type the code. They never paste it.

---

## R4 — Bugs must be layered

Banned: only-missing-bracket decks.

| Tier | Type | Character |
|---|---|---|
| T1 | Visible syntax | Red error, obvious |
| T2 | Name / case | `df["minutes"]` vs `df["Minutes"]` |
| T3 | Silent logic | `//` vs `/`, `>=` vs `>` |
| T4 | Off-by-one | `range(11)`, `len(x)-1` |
| T5 | State bug | `count = 1` instead of `count += 1` |
| T6 | Assumption bug | `highest = 0` breaks on negatives |
| T7 | Runs but wrong | Reversed subtraction — right shape, wrong meaning |

**Debug KEY:** *Code running successfully does not mean the answer is correct.*

Reveal one tier at a time. Never dump all bugs together.

---

## R5 — One KEY per concept

### KEY Register (running)

| Concept | KEY |
|---|---|
| Python | Instructions in Simple English |
| NumPy | Fast Math Engine |
| Pandas | Excel Controlled by Python |
| DataFrame | Digital Register |
| Filter | Security Gate |
| GroupBy | Sorting Counter |
| Visualisation | Picture of the Answer |
| Debugging | Detective Work |
| API | Data Delivery Boy |
| Day 1 project | Data = Digital Mirror |
| Homework project | Data = Career GPS |

---

## R6 — ELI5 first

Assume: first-year, non-CS, returning after six months, forgetful.
Simple → technical → advanced. Prerequisite refresher before every topic.

---

## R7 — Pace discipline

| Topic type | Flow |
|---|---|
| Familiar | Question → micro-explanation → example → attempt → move on |
| Hard | Historical problem → KEY → ELI5 visual → demo → attempt → check |

---

## R8 — Visible outcome per block

Every block ends with something the student can see, run, or show.

---

## R9 — Determinism and anti-copying

- Generator produces **identical columns, different values** per student.
- Homework uses a different domain so class answers cannot be reused.

---

## R10 — Zero setup risk

- No live account creation in class.
- No API authentication in class.
- APIs taught as a concept slide: `App → API → JSON → CSV → DataFrame`.
- Backup outputs prepared in slides in case the environment fails.

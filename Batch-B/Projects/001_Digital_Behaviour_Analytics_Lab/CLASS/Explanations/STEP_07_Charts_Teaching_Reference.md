# DAY 1 · STEP 7 — CHARTS (MATPLOTLIB)
## Teacher Explanation Reference (every method, variable, parameter)

**Use:** second screen, scroll in sync with Charts 1–4.
**Spine sentence:** *Visualisation = Picture of the Answer.*
**Minimum viable:** Chart 1 only. Charts 2–4 if time allows.

---

## 0. THE 3-SECOND TEST — open with this, 60 seconds flat

Put seven numbers on screen:

```
95   120   80   140   60   170   110
```

> "Which is largest? **Time yourself.**"

Then show the bar chart.

> *"Nothing changed except the format."*

**That is the entire argument for visualisation.** Do not explain it further — the demo *is* the explanation. Move on.

---

## 1. The mental model that makes Matplotlib make sense

Matplotlib confuses beginners because the commands look disconnected. One metaphor fixes it:

| Code | Real-world action |
|---|---|
| `plt.figure()` | **Put a blank sheet of paper on the desk** |
| `plt.bar(...)` | Draw the bars on it |
| `plt.title(...)` `plt.xlabel(...)` | Write the headings on it |
| `plt.savefig(...)` | **Photocopy the sheet** |
| `plt.close()` | **Throw the sheet away**, fresh desk for the next chart |

> **Say it:** *"Every `plt.` command draws on the SAME sheet until you close it. That is why the order matters, and that is why we close at the end. Forget to close, and Chart 2 gets drawn on top of Chart 1."*

**This metaphor is worth 5 minutes.** It explains `figure`/`close` pairing, why `title` works without you telling it *which* chart, and why the lines have no visible connection to each other. Everything after this is vocabulary.

**Carry-over rule from Steps 5 & 6:** brackets `()` = *do something*. No brackets = *tell me something*.

---

## 2. IMPORTS & SETUP

```python
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
```

| Item | In general | In this code |
|---|---|---|
| `matplotlib` | The plotting library — Python's oldest and most universal | The drawing engine |
| `matplotlib.use("Agg")` | Sets the **backend** — the thing that turns drawing commands into output | `"Agg"` = write to an image file, no display window needed |
| `matplotlib.pyplot` | The simple command-style interface to Matplotlib | The part we actually use |
| `as plt` | **Alias**, universal convention — third one today after `np` and `pd` | — |

**Why `use("Agg")` sits BETWEEN the two imports — a student will ask:** the backend must be chosen *before* `pyplot` loads. Out of order, it is ignored. Say: *"This is a rule about setup order, not something you will meet often. On your laptop you can delete this line entirely."*

**Mention both, as your file instructs:**

| | What it does | Where it's used |
|---|---|---|
| `plt.show()` | Pops the chart up in a window | **Their laptops** — instant feedback |
| `plt.savefig()` | Writes a PNG file to disk | **Homework submission** — and this file |

> *"On your laptop, `show()` gives you the chart in a window. But `savefig()` gives you a file you can email, embed in a report, or submit. Professionals save."*

---

## 3. DATA PREP

```python
df = pd.read_csv("digital_behaviour.csv")

df["Total_Screen_Time"] = (
    df["Instagram_Minutes"] + df["YouTube_Minutes"]
    + df["WhatsApp_Minutes"] + df["LinkedIn_Minutes"]
)
```

| Item | In general | In this code |
|---|---|---|
| `pd.read_csv()` | Loads the table | Same one line as Step 6 |
| Column addition | Element-wise, row by row | Rebuilt so **this file runs standalone** |

**Say the honest reason:** *"We are rebuilding a column we already made in Step 6. Not because Pandas forgot — because a new file starts with empty memory. Each script stands alone."*

```python
df["Day_Label"] = [f"D{i+1}" for i in range(len(df))]
```

| Item | In general | In this code |
|---|---|---|
| `[expr for i in range(n)]` | **List comprehension** — builds a list in one line | Makes `["D1", "D2", ... "D30"]` |
| `range(len(df))` | Counts `0, 1, 2 ... 29` | One number per row |
| `i + 1` | Shifts to human counting | So the first day reads **D1**, not D0 |
| `f"D{i+1}"` | **f-string** — slots the value into text | `"D1"`, `"D2"`, … |

**Why this line exists at all — point at a chart without it:** full dates like `2026-09-01` overlap into unreadable mush on the x-axis. Short labels are a *design* decision, not a technical one.

**The `i+1` is a callback.** Say: *"Zero-based counting again — from Step 5. Computers start at 0, humans start at 1. `+1` is the translation layer. You will write that `+1` for the rest of your career."*

**If comprehensions are new to them,** show the long form once and delete it:
```python
labels = []
for i in range(len(df)):
    labels.append(f"D{i+1}")
```
Four lines → one. Same compression story as Step 5 Part B.

---

## 4. CHART 1 — SCREEN TIME BY DAY  ⭐ *** THE ONE THAT MATTERS ***

> If only one chart gets made today, it is this one.

```python
plt.figure(figsize=(12, 5))
plt.bar(df["Day_Label"], df["Total_Screen_Time"], color="steelblue")
```

| Item | In general | In this code |
|---|---|---|
| `plt.figure()` | Creates a new blank canvas | Fresh sheet of paper |
| `figsize=(12, 5)` | **Keyword parameter.** Width, height in **inches** | Wide and short — 30 bars need horizontal room |
| `plt.bar(x, height)` | Draws a **bar chart** | One bar per day |
| **1st parameter** — `x` | What goes along the bottom — the **categories** | `Day_Label` → D1…D30 |
| **2nd parameter** — `height` | How **tall** each bar is — the values | `Total_Screen_Time` |
| `color="steelblue"` | Bar colour. Accepts names, hex codes, or a list | One calm colour — nothing to distract |

**The parameter order is the whole idea — say it:**
> *"First what you're comparing, then how much of it. Categories, then values. Every chart function in every language works this way."*

**When to use a bar chart:** comparing separate, unrelated categories. Days, apps, products, cities.

```python
plt.title("My Screen Time by Day")   # never optional
plt.xlabel("Day")                    # never optional
plt.ylabel("Minutes")                # never optional
```

| Item | In general | In this code |
|---|---|---|
| `plt.title(str)` | Heading above the chart | Without it, the reader guesses |
| `plt.xlabel(str)` | Label for the horizontal axis | — |
| `plt.ylabel(str)` | Label for the vertical axis | **"120" of what?** Minutes. Say so. |

### ⚠️ ENFORCE FROM THE VERY FIRST CHART

> **Title. Both axes. Legend when 2+ series.**
> *"This habit is easier to install now than to fix in Week 3."*

**The line that makes them care:** *"An unlabelled chart is not a chart. It is a decoration. If your manager has to ask what the axis means, you have wasted their time and yours."*

```python
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/chart1_screen_time_by_day.png", dpi=100)
plt.close()
```

| Item | In general | In this code |
|---|---|---|
| `plt.xticks()` | Controls the tick marks/labels on the x-axis | — |
| `rotation=45` | Turns labels 45° | Stops 30 labels colliding |
| `plt.tight_layout()` | Auto-adjusts spacing so nothing is cut off | **Always call it before saving** |
| `plt.savefig(path)` | Writes the figure to an image file | — |
| `"charts/chart1_...png"` | **1st parameter — path.** Extension decides format (`.png`, `.pdf`, `.svg`) | Into a `charts/` subfolder |
| `dpi=100` | **Dots per inch — resolution.** Higher = sharper + bigger file | 100 = fine for screen; 300 for print |
| `plt.close()` | Closes the figure, frees memory | **Fresh sheet for the next chart** |

**`tight_layout()` is worth a live demo.** Comment it out, save, open the PNG — the rotated labels are sliced off at the bottom. Restore it. Ten seconds, and they will never forget it.

**`figsize` × `dpi` = pixel size.** `(12, 5)` at `dpi=100` → a 1200 × 500 px image. Mention once for anyone who asks how big the file will be.

**⚠️ Practical warning before you run:** `savefig` will **not** create the `charts/` folder for you. If it doesn't exist → `FileNotFoundError`. Make the folder first, or drop the `charts/` prefix. **Check this before class starts** — it is the single most likely thing to break the demo.

### The questions — from the picture ALONE, table closed

> "Which day was your worst?"
> "Any pattern? Weekends? Exam week?"

**FINISH THE SENTENCE — make a student say it out loud:**
> *"This chart shows that ______, which means I should ______."*

---

## 5. CHART 2 — WHERE DOES THE TIME GO

```python
apps = ["Instagram", "YouTube", "WhatsApp", "LinkedIn"]
totals = [
    df["Instagram_Minutes"].sum(),
    ...
]
```

| Item | In general | In this code |
|---|---|---|
| `apps` | A plain Python list of strings | The four categories — the x-axis |
| `totals` | A list of four numbers | Matching heights — the y-axis |
| `.sum()` | Same verb from NumPy and Pandas | One total per app |

**The rule to name:** `apps` and `totals` must be the **same length, in the same order**. Position 1 pairs with position 1. Swap one and the chart silently lies — no error, just wrong.

> **Say it:** *"Matplotlib will never tell you your labels are on the wrong bars. It trusts you completely. That is the most dangerous thing about charts."*

```python
plt.bar(apps, totals, color=["#E1306C", "#FF0000", "#25D366", "#0A66C2"])
```

| Item | In general | In this code |
|---|---|---|
| `color=[...]` | A **list** of colours — one per bar | Each app gets its own brand colour |
| `"#E1306C"` etc. | **Hex colour codes** — `#RRGGBB` in hexadecimal | Instagram pink, YouTube red, WhatsApp green, LinkedIn blue |

**Why this is good design, not decoration:** the colours are the ones students already associate with those apps. **Zero effort to read.** That is the test for whether colour is earning its place.

> **Chart 1 used ONE colour. Chart 2 uses FOUR.** Ask why. Answer: in Chart 1 all bars are the same kind of thing (days), so colour would mean nothing. In Chart 2 each bar is a different thing, so colour carries information. **Colour must MEAN something.**

### The question — the word 'quietly' matters

> "Which app **quietly** took the most time? Was it the one you expected?"

**The surprise is the teaching moment.** Let them react before you say anything.

---

## 6. CHART 3 — STUDY VERSUS SCREEN

```python
plt.plot(df["Day_Label"], df["Study_Minutes"],
         marker="o", label="Study", color="green")
plt.plot(df["Day_Label"], df["Total_Screen_Time"],
         marker="s", label="Screen Time", color="crimson")
```

| Item | In general | In this code |
|---|---|---|
| `plt.plot(x, y)` | Draws a **line chart** — points joined in order | Trend over the 30 days |
| **1st parameter** `x` | Horizontal positions | Day labels |
| **2nd parameter** `y` | Vertical values | Minutes |
| `marker="o"` | Puts a **dot** at each data point | Circles for Study |
| `marker="s"` | `s` = **square** | Squares for Screen Time |
| `label="Study"` | **The text the legend will show.** Invisible until `plt.legend()` is called | — |
| `color="green"` / `"crimson"` | Line colour | Green = good habit, red = warning. Intuitive, not random |
| **Two `plt.plot` calls** | Both draw on the **same** figure | Two lines, one chart — the sheet-of-paper model in action |

**Bar vs line — the rule to give them:**

| Use | When |
|---|---|
| **Bar** | Comparing **separate** categories — apps, cities, products |
| **Line** | Showing **change over time** — days, months, years |

> *"Days are both — that is why Chart 1 works as a bar and Chart 3 works as a line. Chart 1 asks 'which day was worst?' Chart 3 asks 'what is the trend?' Different question, different chart."*

**Why `marker` matters beyond looks:** without markers you cannot tell where the real measurements are versus where the line is just connecting them. Markers say *"this is a real reading."* Also: different markers stay distinguishable when printed in black and white.

```python
plt.legend()   # mandatory with 2+ series
```

| Item | In general | In this code |
|---|---|---|
| `plt.legend()` | Draws the key box, collecting every `label=` set so far | Says which line is which |
| No parameters needed | It finds the labels automatically | — |
| `loc="upper right"` | Optional — force its position | Mention only if it covers data |

**The dependency to point out:** `label=` sets the text, `plt.legend()` makes it appear. **Set a label but never call `legend()` and nothing shows.** Call `legend()` with no labels and you get a warning + empty box. They work as a pair.

### 🌱 THE SEED FOR DAY 4 — do not name it yet

> "Do the lines move together or in opposite directions?"
> "On your best study day, what happened to screen time?"

**Do not say the word "correlation."** Just let them **SEE** that two columns can be related. You are building the intuition that Day 4 will give a name to.

---

## 7. CHART 4 — SHARE OF ATTENTION *(optional)*

```python
plt.figure(figsize=(7, 7))
plt.pie(totals, labels=apps, autopct="%1.1f%%", startangle=90,
        colors=["#E1306C", "#FF0000", "#25D366", "#0A66C2"])
```

| Item | In general | In this code |
|---|---|---|
| `plt.pie(x)` | Draws a pie chart; **converts values to percentages automatically** | Share of total app time |
| **1st parameter** `x` | The values — sizes of the slices | `totals` |
| `labels=` | Text beside each slice | App names |
| `autopct="%1.1f%%"` | **Auto-percentage format.** `1.1f` = 1 decimal place; `%%` prints a literal `%` | Shows `34.2%` on each slice |
| `startangle=90` | Where the first slice begins, in degrees | 90 = start at 12 o'clock, like a clock face. Looks deliberate |
| `colors=` | **Note the `s`** — `plt.bar` uses `color`, `plt.pie` uses `colors` | Same four brand colours as Chart 2 |
| `figsize=(7, 7)` | **Square** | A non-square figure makes the pie an oval. Deliberate choice |

**The `color` vs `colors` inconsistency is real.** Say: *"Yes, that's annoying. Matplotlib is thirty years old and grew in pieces. When something looks inconsistent, check the docs rather than guessing."* Honesty here builds more trust than pretending it's logical.

### ⚠️ THE RULE TO TEACH — more important than the syntax

> **Pie charts are ONLY for parts of ONE whole.**
> Never use a pie chart for things that do not add up to 100%.

**Valid here** — the four apps *are* the whole of app time.
**Invalid** — a pie of Instagram, Study, and Sleep. They aren't slices of a shared total, so the picture is a lie.

**The second, harsher rule, worth 20 seconds:** humans compare *lengths* accurately and *angles* badly. With more than 4–5 slices, a bar chart is almost always better. *"Use pies rarely. When you do, use them for exactly this: a small number of parts of one clear whole."*

---

## 8. FULL INVENTORY — quick lookup while teaching

### Variables
| Name | Holds | Where |
|---|---|---|
| `df` | The DataFrame | Setup |
| `df["Total_Screen_Time"]` | Rebuilt column | Setup |
| `df["Day_Label"]` | D1…D30 short labels | Setup |
| `apps` | List of 4 app names | Chart 2 |
| `totals` | List of 4 sums | Charts 2 & 4 |

### Figure lifecycle *(the sheet of paper)*
`plt.figure(figsize=)` → draw → label → `plt.tight_layout()` → `plt.savefig()` → `plt.close()`

### Drawing functions
| Function | Chart type | Key parameters |
|---|---|---|
| `plt.bar(x, height)` | Bar | `color` |
| `plt.plot(x, y)` | Line | `marker`, `label`, `color` |
| `plt.pie(x)` | Pie | `labels`, `autopct`, `startangle`, `colors` |

### Labelling functions
`plt.title()` · `plt.xlabel()` · `plt.ylabel()` · `plt.legend()` · `plt.xticks(rotation=)`

### Output functions
`plt.savefig(path, dpi=)` · `plt.close()` · `plt.show()` *(their laptops)*

### Parameters, all in one place
| Parameter | Belongs to | Means |
|---|---|---|
| `figsize=(w, h)` | `figure` | Size in inches |
| `color=` | `bar`, `plot` | One colour, or a list |
| `colors=` | `pie` | Plural — pie only |
| `marker=` | `plot` | `"o"` circle, `"s"` square |
| `label=` | `plot`, `bar` | Text for the legend |
| `rotation=` | `xticks` | Degrees to turn labels |
| `autopct=` | `pie` | Percentage format string |
| `startangle=` | `pie` | Degrees for the first slice |
| `dpi=` | `savefig` | Resolution |

### Python features used along the way
`[f"D{i+1}" for i in range(len(df))]` — list comprehension · f-string · `range()` · `len()`

---

## 9. CHART RULES — put these on a slide

| Rule | Why |
|---|---|
| Always title the chart | Otherwise the reader guesses |
| Always label both axes | "120" of **what**? |
| Legend when 2+ series | Otherwise the lines are meaningless |
| No more colours than needed | Colour must **MEAN** something |
| One chart, one message | Needs a paragraph to explain? Split it |

### THE HABIT TO CARRY ALL COURSE

> ### *"This chart shows that ______, which means I should ______."*
> **If they cannot finish that sentence, the chart is not done.**

---

## 10. ERRORS TO PROVOKE ON PURPOSE

| Break this | Result | Lesson |
|---|---|---|
| `charts/` folder missing | `FileNotFoundError` | `savefig` won't create folders — **check before class** |
| Remove `plt.tight_layout()` | Rotated labels sliced off | Always call it before saving |
| Remove `plt.close()` | Chart 2 draws on top of Chart 1 | One sheet at a time |
| `label=` but no `plt.legend()` | No key appears | They work as a pair |
| `plt.legend()` with no labels | Warning + empty box | Same pair, other half |
| Remove `rotation=45` | 30 labels collide into mush | Readability is a decision |
| `plt.pie(..., color=...)` | `TypeError` | Pie wants `colors`, plural |
| Shuffle `totals` but not `apps` | **No error — a wrong chart** | The most dangerous bug of all |

---

## 11. TIMING & TRIAGE

| If time is | Do |
|---|---|
| Comfortable | 3-second test → Charts 1–4 → rules slide |
| Tight | 3-second test → **Chart 1** → Chart 3 → rules slide |
| **Minimum viable** | 3-second test → **Chart 1 only** → the finish-the-sentence habit |

**Never cut:** the 3-second test, Chart 1, and *"This chart shows that ___, which means I should ___."*

---

## 12. CLOSING — what they built today

**Step 5:** raw numbers, fast maths → **Step 6:** a real table, new knowledge → **Step 7:** a picture anyone can read in three seconds.

> *"Read → Calculate → Add knowledge → Save → **Show**. This morning you could not add seven numbers without a loop. This afternoon you produced charts you could put in front of a manager."*

**Student note to repeat before they leave:** on their laptops, `plt.show()` displays the chart; `savefig()` writes the file. They need **`savefig()` for the homework submission**.

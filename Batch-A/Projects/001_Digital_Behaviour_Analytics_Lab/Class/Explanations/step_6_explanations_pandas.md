# DAY 1 · STEP 6 — PANDAS
## Teacher Explanation Reference (every method, variable, parameter)

**Use:** second screen, scroll in sync with Parts A–K.
**Spine sentences (repeat all day):**
*Pandas = Excel Controlled by Python.* · *DataFrame = Digital Register.*

**Open on the Step 5 failure.** The mixed array that turned `95` into `'95'` is the doorway. Do not start fresh.

---

## 0. The three objects students must be able to name by the end

| Object | ELI5 | How to spot it on screen | Analogy |
|---|---|---|---|
| **DataFrame** | The whole table — rows *and* columns | Has column headers across the top | The full Excel sheet |
| **Series** | **One** column, standing alone | Prints as a vertical list with `Name: ..., dtype: ...` at the bottom | A single Excel column pulled out |
| **Index** | The row labels down the left | The `0 1 2 3...` column you never typed | Excel's row numbers |

> **Say it:** "Every time something prints, ask yourself: *table or single column?* That one question prevents half the errors in Pandas."

**Carry-over rule from Step 5 (repeat it):** brackets `()` = *do something*. No brackets = *tell me something*. That is why it is `df.head()` but `df.shape`.

---

## 1. IMPORT

```python
import pandas as pd
```

| Item | In general | In this code |
|---|---|---|
| `pandas` | Library for **tabular** data — rows, columns, headers, mixed types | The fix for the Step 5 trap |
| `as pd` | **Alias**, universal convention — same habit as `np` | Types `pd.read_csv` instead of `pandas.read_csv` |

**Tie it to Step 5 out loud:** *"Pandas is built ON TOP of NumPy. Same engine underneath, but now each column is allowed its own type. Dates stay dates. Numbers stay numbers. That is the whole difference."*

**Notice what is gone:** no `import csv`. No `open()`. No `with`. No loop. No `int()`. Point at the Step 5 loading block on the left half of the screen — **nine lines become one.**

---

## 2. PARTS A + B — LOAD

```python
df = pd.read_csv("digital_behaviour.csv")
```

| Item | In general | In this code |
|---|---|---|
| `pd.read_csv()` | **Function.** Reads a CSV file and returns a DataFrame | Loads the whole table in one line |
| `"digital_behaviour.csv"` | **1st parameter — filepath.** A string | The student's own file, same folder |
| `df` | Variable holding the DataFrame | **The universal habit-name.** Make them use it — every tutorial, book and StackOverflow answer on earth uses `df` |
| Return value | A DataFrame object | Assigned to `df` |

**Useful parameters to mention, not teach** (say "these exist, you will need them within a month"):

| Parameter | Does |
|---|---|
| `sep=";"` | For files that use semicolons instead of commas |
| `encoding="utf-8"` | Same fix as Step 5 when odd characters crash the load |
| `nrows=100` | Peek at a huge file without loading it all |

**The two things `read_csv` did for free that you did by hand in Step 5:**
1. Read the header row and used it as column names.
2. **Guessed the type of every column** — numbers stayed numbers. No `int()` anywhere.

**Say it:** *"Every student loads THEIR OWN file. Nobody's findings will match. That is the point."*

---

## 3. PART C — LOOK BEFORE YOU LEAP

> Install this habit now: **never analyse a table you have not inspected.** This is a professional reflex, not a beginner step.

```python
print(df.head())
print(df.shape)
print(list(df.columns))
print(df[["Instagram_Minutes", "Study_Minutes"]].describe())
```

| Item | In general | In this code | Brackets? |
|---|---|---|---|
| `.head()` | **Method.** First 5 rows by default | Sanity check — did the right file load? | Yes — it *does* something |
| `.head(3)` | Parameter `n` = how many rows | Used later in Part D | — |
| `.tail()` | Last rows — mention it | (not used) | — |
| `.shape` | **Attribute.** Returns `(rows, columns)` as a tuple | Prints e.g. `(30, 6)` | **No brackets** |
| `.columns` | **Attribute.** The column names | The cure for Bug 2 | **No brackets** |
| `list(...)` | Built-in that converts to a clean list | Makes `.columns` print readably instead of as an `Index` object | — |
| `.describe()` | **Method.** Count, mean, std, min, quartiles, max — for numeric columns only | Replaces the entire Step 2 loop block | Yes |
| `df[[ ... ]]` | Double brackets = list of columns → DataFrame back | Restricts `describe()` to the two columns that matter | — |

**`.shape` reading drill:** `(30, 6)` → *"thirty rows, six columns."* Rows always first. Ask them to read it aloud once; it embeds.

**Two callbacks to cash in here:**

- **Bug 2 (KeyError):** *"`df.columns` would have told you the real column names in one line this morning."*
- **Bug 6 (text vs number):** *"`describe()` only works on numbers. If a column were secretly text, it simply would not appear in this output. Pandas would have caught this morning's bug for you."*

**The question to ask — do not skip:**
> "Look at `describe()`. Which of these did you calculate by hand with loops in Step 2?"

Answer: **count, mean, min, max — all of them.** One line. Let that land before moving on.

---

## 4. PART D — PICKING COLUMNS *(the double-bracket moment)*

```python
one_column  = df["Instagram_Minutes"]
two_columns = df[["Date", "Instagram_Minutes"]]
```

| Syntax | What goes inside | What comes back |
|---|---|---|
| `df["Name"]` | One **string** | A **Series** — one column |
| `df[["A", "B"]]` | A **list** of strings | A **DataFrame** — a table |

**Let them notice the double brackets first. Then ask:**
> "Why does one need single brackets and two need double?"

**The answer that makes it stick — say it slowly:**
> *"There is no such thing as double brackets. There is one set of brackets, and inside it you put a **list**. `["Date", "Instagram_Minutes"]` is just a list. The outer bracket is the selector; the inner bracket is the list."*

Write it in two steps on the board:

```python
cols = ["Date", "Instagram_Minutes"]   # a plain list
df[cols]                               # ONE set of brackets
```

That single demo kills the confusion permanently.

**Proof on screen — point at the two outputs:**
- Series: vertical, no header box, ends with `Name: Instagram_Minutes, dtype: int64`
- DataFrame: proper table with column headers

**Why it matters later:** `.sum()` on a Series gives one number. `.sum()` on a DataFrame gives one number *per column*. Same method, different object, different answer.

---

## 5. PART E — COLUMN MATHS, NO LOOP

```python
df["Instagram_Minutes"].sum()
round(df["Study_Minutes"].mean(), 2)
df["YouTube_Minutes"].max()
```

| Item | In general | In this code |
|---|---|---|
| `.sum()` `.mean()` `.max()` `.min()` | **The exact same verbs as NumPy** | Applied to a Series instead of an array |
| `round(value, 2)` | **Built-in function**, not a method. 2nd parameter = decimal places | Tidies the average for display |

**Say this out loud — it is the conceptual glue of the whole day:**
> *"These are the same verbs you learned in Step 5. That is not a coincidence. Pandas uses NumPy underneath. You did not learn a new tool — you learned a better container for a tool you already own."*

**Note the two rounding styles in this file** (a student *will* ask):

| Style | Where | Why |
|---|---|---|
| `round(x, 2)` — function | Part E, Part J | Rounding a **single number** |
| `.round(2)` — method | Part H | Rounding an **entire column** at once |

Same idea, different object. Reinforces §0.

---

## 6. PART F — THE SECURITY GATE, NOW ON A TABLE

They already own "Security Gate" from Step 5. **Reuse the exact phrase.** The upgrade: whole *rows* pass through now, not single values.

```python
heavy_insta = df[df["Instagram_Minutes"] > 100]
good_study  = df[df["Study_Minutes"] > 180]
```

| Item | In general | In this code |
|---|---|---|
| `df["col"] > 100` | Element-wise comparison → a **Series of True/False**, one per row | The gate itself |
| `df[ mask ]` | **Boolean row filtering.** Keeps rows where the mask is `True` | Returns a smaller DataFrame |
| `len(df)` | Counts **rows** of a DataFrame | How many days passed the gate |

**Optional 30-second demo that pays for itself:** print `df["Instagram_Minutes"] > 100` on its own first, exactly as you did in Step 5 Part F. Seeing the True/False column before it gets used is what made masking click last time.

```python
danger_days = df[
    (df["Instagram_Minutes"] > 100) & (df["Study_Minutes"] < 100)
]
```

| Item | In general | In this code | Non-negotiable |
|---|---|---|---|
| `&` | **Element-wise AND.** Both conditions must be True for that row | High scroll AND low study | Use `&`, **never** `and` |
| `\|` | Element-wise OR — either condition | (not used) | Use `\|`, never `or` |
| `~` | NOT — flips the mask | (not used) | — |
| `( )` around each condition | **Mandatory.** `&` binds tighter than `>` in Python | Without them: `TypeError` / `ValueError` | Every single time |

**Expect errors here. Let them happen.** The two failures to provoke:

| Break | Error | Lesson |
|---|---|---|
| Drop the inner brackets | `ValueError: The truth value of a Series is ambiguous` | Python's operator precedence, not a Pandas bug |
| Use `and` instead of `&` | Same ambiguous-truth error | `and` asks one yes/no question; `&` asks thirty at once |

**Why `and` cannot work — the one-liner:**
> *"`and` wants ONE true-or-false. You handed it thirty. It has no idea which one you meant. `&` goes row by row."*

**Say:** *"In Step 5 a single value passed the gate. Here the ENTIRE ROW passes — date, all four apps, everything."*

---

## 7. PART G — SORTING *(droppable if short on time)*

```python
top_insta = df.sort_values("Instagram_Minutes", ascending=False).head(5)
```

| Item | In general | In this code |
|---|---|---|
| `.sort_values()` | Reorders rows by a column's values | Worst scrolling days to the top |
| `"Instagram_Minutes"` | **1st parameter — `by`.** Which column to sort on | — |
| `ascending=False` | **Keyword parameter.** `True` = small→large (default), `False` = large→small | We want the *worst* days first |
| `.head(5)` | Chained on the end | Top 5 only |
| **Chaining** | Each method returns a new object, so you can keep adding dots | Sort → then take 5, left to right |

**Teach chaining explicitly — read it aloud left to right:**
> *"Take df → sort it by Instagram minutes, biggest first → give me the top five."* One sentence, one line of code.

**Crucial point:** `sort_values` returns a **new** DataFrame. The original `df` is untouched — the row order in `df` never changed. Prove it by printing `df.head()` again afterwards.

**Also useful:** `.sort_values(by=["A","B"])` sorts by two columns, tie-broken by the second. Mention only.

---

## 8. PART H — CREATING NEW KNOWLEDGE ⚠️ *** NEVER DROP THIS ***

> This is where the project stops being an exercise and becomes **theirs**.

```python
df["Total_Screen_Time"] = (
    df["Instagram_Minutes"]
    + df["YouTube_Minutes"]
    + df["WhatsApp_Minutes"]
    + df["LinkedIn_Minutes"]
)
```

| Item | In general | In this code |
|---|---|---|
| `df["New_Name"] = ...` | **Assignment to a non-existent column CREATES it.** No "add column" command needed | Three brand-new columns appear |
| `Series + Series` | Element-wise addition, row by row | Row 1 with row 1, row 2 with row 2… |
| `( )` around the expression | Lets one expression span several lines for readability | Purely cosmetic — but teach it, it is good style |

**The single sentence to say here:**
> *"Notice there is no `.add_column()` method. You just assign to a name that does not exist yet, and Pandas creates it. If the name DOES exist, you overwrite it — silently. Be careful with your spelling."*

```python
df["Screen_Hours"] = (df["Total_Screen_Time"] / 60).round(2)
```

| Item | In general | In this code |
|---|---|---|
| `Series / 60` | **Broadcasting** — same as NumPy Part E | Every row divided by 60 |
| `.round(2)` | Rounds the **whole column**; parameter = decimal places | Readable hours |
| `( )` before `.round()` | Finish the division first, *then* round the result | Same bracket logic as `(instagram > 100).sum()` in Step 5 |

```python
df["Digital_Balance"] = (df["Study_Minutes"] / df["Total_Screen_Time"]).round(2)
```

| Item | In general | In this code |
|---|---|---|
| `Series / Series` | Element-wise division, row by row | Study time ÷ screen time, per day |
| Uses a column created 4 lines ago | Columns are usable the instant they exist | Building knowledge on knowledge |

**Ask all three — do not skip, do not answer for them:**

| Value | Meaning |
|---|---|
| Balance **> 1** | Studied MORE than total screen time |
| Balance **< 1** | Scrolled more than studied |
| Balance **= 1** | Exactly equal |

> **This is the quietest, most personal moment of the day. Let it land. Do not fill the silence.**

**One honest warning:** if `Total_Screen_Time` is 0 on some day, that division gives `inf`. Only raise it if a student's output shows it — otherwise it breaks the mood.

---

## 9. PART I — TURNING NUMBERS INTO JUDGEMENT

```python
df["Day_Type"] = "Normal"
df.loc[df["Total_Screen_Time"] > 300, "Day_Type"] = "Heavy"
```

| Item | In general | In this code |
|---|---|---|
| `df["Day_Type"] = "Normal"` | Assigning a single value fills **every** row with it | Everyone starts Normal — the default |
| `.loc[ ]` | **Label-based selector.** Syntax: `df.loc[which_rows, which_column]` | The precise way to edit a subset |
| 1st slot — `df[...] > 300` | Boolean mask = **which rows** | Only the heavy days |
| 2nd slot — `"Day_Type"` | **Which column** to write into | — |
| `= "Heavy"` | Writes that value into every selected cell | Overwrites "Normal" where the mask is True |

**The strategy to name explicitly — this is a real professional pattern:**
> **Set the default for everyone, then overwrite the exceptions.** Two lines instead of an if/else loop over thirty rows.

**Why `.loc` and not `df[mask]["Day_Type"] = "Heavy"`?** The second form edits a *copy* and silently does nothing (`SettingWithCopyWarning`). Say: *"When you are READING, plain brackets are fine. When you are WRITING, use `.loc`."* That rule saves them hours later.

```python
print(df["Day_Type"].value_counts())
```

| Item | In general | In this code |
|---|---|---|
| `.value_counts()` | Counts how many times each unique value appears; sorted biggest first | e.g. `Normal 22, Heavy 8` |

**Note this is a *counting* tool for text columns** — `describe()` ignored these. Different column type, different tool.

### 🌱 PLANT THE SEED FOR DAY 9 — say this exactly

> *"Where did the number 300 come from? **I invented it.** You are the rule right now.
> On Day 9, the machine will **LEARN** that threshold from the data instead of me guessing it.
> Same shape. Same columns. That is Machine Learning."*

**Data → Rule → Category → Decision.** Write those four words on the board and leave them there.

---

## 10. PART J — ANSWER THE REAL QUESTIONS *(droppable)*

```python
app_totals = {
    "Instagram": df["Instagram_Minutes"].sum(),
    ...
}
```

| Item | In general | In this code |
|---|---|---|
| `{ }` | A **dictionary** — name → value pairs | App name → total minutes |
| `.sum()` per column | Four Series totals | Collected into one lookup |

```python
biggest_app = max(app_totals, key=app_totals.get)
```

| Item | In general | In this code |
|---|---|---|
| `max()` | Built-in returning the largest item | Without `key=`, it would compare the *names* alphabetically — wrong answer |
| `key=app_totals.get` | **Keyword parameter — the comparison rule.** "Judge each key by its value" | Returns the app **name**, judged by minutes |
| `app_totals.get` | The method passed **without brackets** — you are handing over the tool, not using it yet | Beginners find this strange; name it, don't dwell |

> **Say:** *"`key=` tells `max` what to compare. Remove it and Python compares the words, and 'YouTube' wins for being late in the alphabet. Meaningless."*

```python
worst_day = df.loc[df["Total_Screen_Time"].idxmax()]
```

| Item | In general | In this code |
|---|---|---|
| `.idxmax()` | Returns the **index label of** the maximum — not the value | *Which row* was worst |
| `.max()` vs `.idxmax()` | `.max()` = "how bad?" · `.idxmax()` = "**which day?**" | The distinction that matters here |
| `df.loc[label]` | Fetches that entire row as a **Series** | The whole day: date, all apps, study |
| `worst_day["Date"]` | Reads one field from that row-Series | — |

**This is the highest-value concept in Part J.** Put it on the board:
> `.max()` tells you **how bad**. `.idxmax()` tells you **which day**. You almost always want the second one.

```python
for app, mins in app_totals.items():
    print(f"  {app:<10} {mins:>6} min  ({round(mins/60,1)} hrs)")
```

| Item | In general | In this code |
|---|---|---|
| `.items()` | Yields `(key, value)` pairs from a dictionary | One app per loop |
| `app, mins` | **Tuple unpacking** — two variables from one pair | Name and total |
| `f"..."` | **f-string.** `{ }` slots get filled with real values | Formatted report line |
| `{app:<10}` | `<` left-align, pad to 10 chars | Names line up in a column |
| `{mins:>6}` | `>` right-align, width 6 | Numbers line up on the right |

**Point at the aligned output:** *"The colon and the arrow are pure presentation. Same numbers, but now it looks like a report instead of a mess. Free professionalism."*

---

## 11. PART K — SAVE YOUR WORK

```python
df.to_csv("my_analysis.csv", index=False)
```

| Item | In general | In this code |
|---|---|---|
| `.to_csv()` | Writes the DataFrame back out to a file | Saves the enriched table |
| `"my_analysis.csv"` | **1st parameter — filename.** Overwrites without warning | Their personal result file |
| `index=False` | **Keyword parameter.** Stops Pandas writing the row-number column | Prevents a junk `0,1,2,3` column appearing every time you save |

**Demo worth 20 seconds:** save once *without* `index=False`, open it, show the junk column. Then save again with it. They will never forget.

**What they are saving:** the original file **plus four columns that did not exist an hour ago** — Total_Screen_Time, Screen_Hours, Digital_Balance, Day_Type. That is created knowledge, not copied data.

**Say:**
> *"Read → Calculate → Add knowledge → Save. That is a data pipeline. You just built one."*

---

## 12. FULL INVENTORY — quick lookup while teaching

### Variables
| Name | Holds | Created in |
|---|---|---|
| `df` | The whole DataFrame | Part B |
| `one_column` | Series — Instagram only | Part D |
| `two_columns` | DataFrame — Date + Instagram | Part D |
| `heavy_insta`, `good_study`, `danger_days` | Filtered DataFrames | Part F |
| `top_insta`, `top_study` | Sorted top-5 DataFrames | Part G |
| `app_totals` | Dictionary, app → minutes | Part J |
| `biggest_app` | String, app name | Part J |
| `worst_day` | Series — one whole row | Part J |

### New columns created (the actual deliverable)
`Total_Screen_Time` · `Screen_Hours` · `Digital_Balance` · `Day_Type`

### Functions (standalone — no dot)
`pd.read_csv()` · `len()` · `list()` · `round()` · `max()` · `print()`

### Methods (dot before them — they *do* something)
`.head(n)` · `.describe()` · `.sum()` · `.mean()` · `.max()` · `.min()` · `.round(n)` · `.sort_values(col, ascending=)` · `.value_counts()` · `.idxmax()` · `.to_csv(name, index=False)` · `.items()` · `.get`

### Attributes (no brackets — they *tell* you something)
`.shape` · `.columns`

### Accessor
`.loc[rows, column]` — the safe way to **write** into selected cells

### Operators
`[ ]` select column · `[[ ]]` select list of columns · `[mask]` filter rows · `&` AND · `|` OR · `+ - /` element-wise column maths · `=` create/overwrite column

---

## 13. NUMPY → PANDAS — the carry-over table *(put on the board)*

| Job | Step 5 · NumPy | Step 6 · Pandas |
|---|---|---|
| Load the file | `open` + `csv` + loop + `int()` — 9 lines | `pd.read_csv()` — 1 line |
| Total | `arr.sum()` | `df["col"].sum()` |
| Average | `arr.mean()` | `df["col"].mean()` |
| Filter | `arr[arr > 100]` → values | `df[df["col"] > 100]` → **whole rows** |
| Two conditions | fiddly | `(...) & (...)` |
| Mixed types | **breaks** — 95 becomes '95' | **works** — every column keeps its own type |
| Column names | none, only positions | real names |
| Summary stats | four separate calls | `.describe()` |

> **The one-line verdict:** *"NumPy is the engine. Pandas is the car built around it."*

---

## 14. ERRORS TO PROVOKE ON PURPOSE

| Break this | Error / result | Lesson |
|---|---|---|
| `df["instagram_minutes"]` | `KeyError` | Names are case-sensitive — check `df.columns` |
| `df["Date", "Instagram_Minutes"]` (single brackets) | `KeyError` | Needs a **list** inside |
| `df[cond1 & cond2]` without inner brackets | `ValueError: truth value ambiguous` | Operator precedence |
| `and` instead of `&` | Same ambiguous error | `and` = one question; `&` = one per row |
| `df.shape()` | `TypeError: not callable` | Attribute, not method |
| `df[df[...]>300]["Day_Type"] = "Heavy"` | `SettingWithCopyWarning`, no change | Writing needs `.loc` |
| `to_csv` without `index=False` | Junk `0,1,2` column in the file | Always pass it |

---

## 15. TIMING & TRIAGE

| If time is | Do |
|---|---|
| Comfortable | A → K in full |
| Tight | **Drop Part G** (sorting) and **Part J** |
| Very tight | Drop G and J, compress C to `.head()` + `.shape` only |
| **Never** | **Never drop Part H** — that is where the project becomes theirs |

---

## 16. THE BRIDGE TO STEP 7

Show the 30-row table on screen and ask:
> "Which day was worst? Find it."

**Let them squint for a full ten seconds.** Do not rescue them.

Then:
> *"You have the answer in the table. You cannot SEE it. Nobody reads 30 rows. Your manager certainly will not."*

**KEY: Visualisation = Picture of the Answer.**
"""
=============================================================================
DAY 1 - STEP 6 SOLUTION - PANDAS
TEACHER ONLY. Never release to students.
=============================================================================

Matches: STEP_06_Pandas_English.md
Syllabus: S3.3 Pandas DataFrames, Series & Data Import/Export. Depth MAX.

KEY: Pandas = Excel Controlled by Python
KEY: DataFrame = Digital Register

OPEN ON THE FAILURE FROM STEP 5.
The mixed array that turned 95 into '95' is your doorway. Use it.

SAY THIS:
  "Open your CSV in Excel. Rows, columns, headers, filter, sort.
   That is what you actually need.
   Pandas is that same table - but you drive it by typing, not clicking.
   And typing can be repeated, saved, and run on ten million rows."

IF RUNNING SHORT: drop Part G (sorting) and Part J.
NEVER drop Part H (new columns) - that is where the project becomes theirs.
=============================================================================
"""

import pandas as pd


# -----------------------------------------------------------------------
# PART A + B - IMPORT AND LOAD
# -----------------------------------------------------------------------
# English: "Read the file and store the table in a variable called df."
#
# 'df' is the universal habit-name. Make them use it.
# They load THEIR OWN file - every student's findings differ.

df = pd.read_csv("digital_behaviour.csv")


# -----------------------------------------------------------------------
# PART C - LOOK BEFORE YOU LEAP
# -----------------------------------------------------------------------
# Install this habit now: never analyse a table you have not inspected.

print("=== FIRST FIVE ROWS ===")
print(df.head())
print()

print("=== SHAPE (rows, columns) ===")
print(df.shape)
print()

print("=== COLUMN NAMES ===")
print(list(df.columns))
print()

print("=== SUMMARY OF NUMERIC COLUMNS ===")
print(df[["Instagram_Minutes", "Study_Minutes"]].describe())
print()

# TWO CALLBACKS TO CASH IN HERE:
#
# Bug 2 (KeyError): "df.columns would have told you the real names
#                    in one line this morning."
#
# Bug 6 (text vs number): "describe() only works on numbers.
#                          If a column were secretly text,
#                          it would not appear here. Pandas would
#                          have caught this morning's bug for you."
#
# ASK: "Look at describe(). Which of these did you calculate
#       by hand with loops in Step 2?"
# Answer: count, mean, min, max - all of them. In one line.


# -----------------------------------------------------------------------
# PART D - PICKING COLUMNS
# -----------------------------------------------------------------------
# English: "Show me only the Instagram minutes column."

one_column = df["Instagram_Minutes"]

# English: "Show me the Date and Instagram minutes together."
# NOTE THE DOUBLE BRACKETS. Let them notice, then explain.

two_columns = df[["Date", "Instagram_Minutes"]]

print("=== ONE COLUMN (a Series) ===")
print(one_column.head(3))
print()
print("=== TWO COLUMNS (a DataFrame) ===")
print(two_columns.head(3))
print()

# ASK: "Why does one need single brackets and two need double?"
# Answer: single = one column (a Series).
#         double = a LIST of columns, so you get a table back.


# -----------------------------------------------------------------------
# PART E - COLUMN MATHS, NO LOOP
# -----------------------------------------------------------------------
# These are the SAME VERBS as NumPy. Say that out loud.
# Pandas uses NumPy underneath - this is not a coincidence.

print("Total Instagram time:", df["Instagram_Minutes"].sum())
print("Average study time:  ", round(df["Study_Minutes"].mean(), 2))
print("Heaviest YouTube day:", df["YouTube_Minutes"].max())
print()


# -----------------------------------------------------------------------
# PART F - THE SECURITY GATE ON A TABLE
# -----------------------------------------------------------------------
# They already own "Security Gate" from Step 5. Reuse the phrase.
# The difference: now WHOLE ROWS pass through, not just values.

heavy_insta = df[df["Instagram_Minutes"] > 100]
good_study = df[df["Study_Minutes"] > 180]

# Two conditions. BOTH must pass.
# EXPECT ERRORS HERE - each condition needs its own brackets.

danger_days = df[
    (df["Instagram_Minutes"] > 100) & (df["Study_Minutes"] < 100)
]

print("Heavy Instagram days:", len(heavy_insta))
print("Good study days:     ", len(good_study))
print("High scroll + low study:", len(danger_days))
print()

# SAY: "In Step 5 a single value passed the gate.
#       Here the ENTIRE ROW passes - date, all four apps, everything."


# -----------------------------------------------------------------------
# PART G - SORTING     [DROP THIS IF SHORT ON TIME]
# -----------------------------------------------------------------------

top_insta = df.sort_values("Instagram_Minutes", ascending=False).head(5)
top_study = df.sort_values("Study_Minutes", ascending=False).head(5)

print("=== TOP 5 INSTAGRAM DAYS ===")
print(top_insta[["Date", "Instagram_Minutes"]])
print()


# -----------------------------------------------------------------------
# PART H - CREATING NEW KNOWLEDGE      *** NEVER DROP THIS ***
# -----------------------------------------------------------------------
# This is where the project stops being an exercise and becomes THEIRS.

# English: "Add the four app columns together."
df["Total_Screen_Time"] = (
    df["Instagram_Minutes"]
    + df["YouTube_Minutes"]
    + df["WhatsApp_Minutes"]
    + df["LinkedIn_Minutes"]
)

# English: "Convert total screen time into hours."
df["Screen_Hours"] = (df["Total_Screen_Time"] / 60).round(2)

# English: "Divide study minutes by total screen time."
df["Digital_Balance"] = (
    df["Study_Minutes"] / df["Total_Screen_Time"]
).round(2)

print("=== NEW COLUMNS ===")
print(df[["Date", "Total_Screen_Time", "Screen_Hours", "Digital_Balance"]].head())
print()

# ASK ALL THREE - do not skip:
#   Balance > 1  -> studied MORE than total screen time
#   Balance < 1  -> scrolled more than studied
#   Balance = 1  -> exactly equal
#
# This is the quietest, most personal moment of the day. Let it land.


# -----------------------------------------------------------------------
# PART I - TURNING NUMBERS INTO JUDGEMENT
# -----------------------------------------------------------------------
# English: "If total screen time is above 300 minutes, call it Heavy."

df["Day_Type"] = "Normal"
df.loc[df["Total_Screen_Time"] > 300, "Day_Type"] = "Heavy"

print("=== DAY TYPE COUNTS ===")
print(df["Day_Type"].value_counts())
print()

# *** PLANT THE SEED FOR DAY 9. SAY THIS EXACTLY: ***
#
#   "Where did the number 300 come from?  I invented it.
#    You are the rule right now.
#    On Day 9, the machine will LEARN that threshold from the data
#    instead of me guessing it.
#    Same shape. Same columns. That is Machine Learning."
#
# Data -> Rule -> Category -> Decision


# -----------------------------------------------------------------------
# PART J - ANSWER THE REAL QUESTIONS    [DROP IF SHORT]
# -----------------------------------------------------------------------

app_totals = {
    "Instagram": df["Instagram_Minutes"].sum(),
    "YouTube": df["YouTube_Minutes"].sum(),
    "WhatsApp": df["WhatsApp_Minutes"].sum(),
    "LinkedIn": df["LinkedIn_Minutes"].sum(),
}

biggest_app = max(app_totals, key=app_totals.get)
worst_day = df.loc[df["Total_Screen_Time"].idxmax()]

print("=== APP TOTALS ===")
for app, mins in app_totals.items():
    print(f"  {app:<10} {mins:>6} min  ({round(mins/60,1)} hrs)")
print()
print("Biggest consumer:   ", biggest_app)
print("Heaviest day:       ", worst_day["Date"])
print("Study on that day:  ", worst_day["Study_Minutes"], "min")
print("Average balance:    ", round(df["Digital_Balance"].mean(), 2))
print()


# -----------------------------------------------------------------------
# PART K - SAVE YOUR WORK
# -----------------------------------------------------------------------
# index=False stops Pandas adding a junk numbering column.

df.to_csv("my_analysis.csv", index=False)
print("Saved to my_analysis.csv")

# SAY: "Read -> Calculate -> Add knowledge -> Save.
#       That is a data pipeline. You just built one."


# =======================================================================
# THE BRIDGE TO STEP 7
# =======================================================================
#
# Show them the 30-row table on screen and ask:
#   "Which day was worst? Find it."
#
# Let them squint at it for ten seconds.
#
# Then: "You have the answer in the table. You cannot SEE it.
#        Nobody reads 30 rows. Your manager certainly will not."
#
# KEY: Visualisation = Picture of the Answer
# =======================================================================

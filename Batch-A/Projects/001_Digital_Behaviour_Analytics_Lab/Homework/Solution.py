"""
=============================================================================
DAY 1 HOMEWORK SOLUTION - PLACEMENT READINESS TRACKER
TEACHER ONLY. Never release to students.
=============================================================================

Matches: HOMEWORK_Placement_Readiness_Tracker.md
KEY: Data = Career GPS

WHY THIS HOMEWORK EXISTS
------------------------
Same workflow as class. Completely different domain.
Students cannot copy a single class answer - the columns do not match.

It also quietly rehearses the shape of a Day 9 classification problem:
    features -> rule -> band -> decision

THE DESIGNED FINDING
--------------------
Communication_Score is deliberately the weakest column in the generator.
Students must DISCOVER this. Never tell them in advance.

Verified on one generated batch of 120:

    Communication_Score    47.3   <- weakest
    Aptitude_Score         60.8
    SQL_Score              64.0
    Python_Score           65.6

    Ready          46
    Almost Ready   36
    Needs Work     38

    CSE 70.3 | IT 72.1 | ECE 63.9 | MECH 61.6

Numbers will differ per student. The PATTERN will not.

MARKING SHORTCUT
----------------
If a student reports anything other than Communication as the weakest
skill, they have almost certainly averaged the wrong axis or included
Projects/Mock_Interviews (which are counts, not scores out of 100).
That is the single most common error in this homework.
=============================================================================
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os


df = pd.read_csv("placement_readiness.csv")

SKILLS = [
    "Python_Score",
    "SQL_Score",
    "Aptitude_Score",
    "Communication_Score",
]


# -----------------------------------------------------------------------
# PART 1 - NUMPY
# -----------------------------------------------------------------------
# Students should use arrays here, not Pandas shortcuts.
# Accept either, but the brief asks for NumPy.

python_scores = df["Python_Score"].to_numpy()
aptitude_scores = df["Aptitude_Score"].to_numpy()
comm_scores = df["Communication_Score"].to_numpy()

print("=" * 60)
print("PART 1 - NUMPY")
print("=" * 60)

# 1. Average Python score
print("Average Python score :", round(python_scores.mean(), 2))

# 2. Highest and lowest Aptitude
print("Highest Aptitude     :", aptitude_scores.max())
print("Lowest Aptitude      :", aptitude_scores.min())

# 3. How many scored above 70 in Communication
#    Boolean mask + sum. Same pattern as Step 5 Part F.
print("Comm above 70        :", (comm_scores > 70).sum())

# 4. Gap between best and worst skill, per student
#    axis=1 means "across the row". This is the first time
#    students meet axis. Expect confusion - it is worth it.
skill_matrix = df[SKILLS].to_numpy()
gaps = skill_matrix.max(axis=1) - skill_matrix.min(axis=1)

print("Average skill gap    :", round(gaps.mean(), 2))
print("Largest skill gap    :", gaps.max())
print()

# TEACHING NOTE:
#   A large gap means a lopsided student - excellent at one thing,
#   weak at another. Those are the easiest students to help,
#   because the fix is obvious. Worth mentioning when returning marks.


# -----------------------------------------------------------------------
# PART 2 - PANDAS
# -----------------------------------------------------------------------

print("=" * 60)
print("PART 2 - PANDAS")
print("=" * 60)

# 1. Inspect
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print()

# 2. Python above 75
strong_python = df[df["Python_Score"] > 75]
print("Python above 75      :", len(strong_python))

# 3. Sort by Aptitude, highest first
by_aptitude = df.sort_values("Aptitude_Score", ascending=False)

# 4. Top 10 by Python
top10_python = df.sort_values("Python_Score", ascending=False).head(10)

# 5. Strong in Python BUT weak in Communication
#    This is the interesting one - it finds the lopsided students.
#    Note the brackets around each condition.
lopsided = df[
    (df["Python_Score"] > 75) & (df["Communication_Score"] < 50)
]
print("Strong Python, weak Comm:", len(lopsided))
print()

# TEACHING NOTE:
#   This group is the single most actionable finding in the whole
#   dataset. They can already code. One communication workshop
#   moves them straight into the Ready band.


# -----------------------------------------------------------------------
# PART 3 - CREATE NEW KNOWLEDGE
# -----------------------------------------------------------------------

print("=" * 60)
print("PART 3 - NEW COLUMNS")
print("=" * 60)

df["Total_Score"] = df[SKILLS].sum(axis=1)
df["Average_Score"] = (df["Total_Score"] / 4).round(1)
df["Weakest_Skill_Score"] = df[SKILLS].min(axis=1)

# Readiness: average + 2 per project + 1 per mock, capped at 100.
# .clip(upper=100) is the clean way. Accept np.minimum too.
df["Readiness_Score"] = (
    df["Average_Score"]
    + df["Projects_Completed"] * 2
    + df["Mock_Interviews_Attended"] * 1
).clip(upper=100).round(1)

print(df[["Student_ID", "Average_Score", "Readiness_Score"]].head())
print()
print("Readiness range:",
      df["Readiness_Score"].min(), "to", df["Readiness_Score"].max())
print()

# COMMON STUDENT ERROR:
#   Forgetting the cap. Without .clip(), scores exceed 100 and the
#   Ready band becomes meaningless. Check for this when marking.


# -----------------------------------------------------------------------
# PART 4 - CLASSIFICATION
# -----------------------------------------------------------------------

print("=" * 60)
print("PART 4 - READINESS BANDS")
print("=" * 60)

# Three ways to do this. All acceptable.
#   (a) .apply with a function      - most readable for beginners
#   (b) np.select                   - cleanest
#   (c) chained .loc assignments    - what we used in class Step 6
#
# Shown here: np.select. Mention (c) as the class-familiar route.

conditions = [
    df["Readiness_Score"] >= 75,
    df["Readiness_Score"] >= 60,
]
choices = ["Ready", "Almost Ready"]

df["Readiness_Band"] = np.select(conditions, choices, default="Needs Work")

band_counts = df["Readiness_Band"].value_counts()
print(band_counts)
print()
print("Largest band:", band_counts.idxmax())
print()


# -----------------------------------------------------------------------
# PART 5 - CHARTS
# -----------------------------------------------------------------------

os.makedirs("charts", exist_ok=True)

# Chart 1 - average score per skill
skill_means = df[SKILLS].mean().sort_values()

plt.figure(figsize=(9, 5))
plt.bar(
    [s.replace("_Score", "") for s in skill_means.index],
    skill_means.values,
    color="steelblue",
)
plt.title("Average Score by Skill")
plt.xlabel("Skill")
plt.ylabel("Average Score (out of 100)")
plt.tight_layout()
plt.savefig("charts/hw_chart1_skill_averages.png", dpi=100)
plt.close()

# Chart 2 - students per readiness band
order = ["Ready", "Almost Ready", "Needs Work"]
counts = [int((df["Readiness_Band"] == b).sum()) for b in order]

plt.figure(figsize=(8, 5))
plt.bar(order, counts, color=["green", "goldenrod", "crimson"])
plt.title("Students by Readiness Band")
plt.xlabel("Band")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("charts/hw_chart2_readiness_bands.png", dpi=100)
plt.close()

# Chart 3 - average readiness by branch
branch_means = df.groupby("Branch")["Readiness_Score"].mean().round(1)

plt.figure(figsize=(8, 5))
plt.bar(branch_means.index, branch_means.values, color="slateblue")
plt.title("Average Readiness Score by Branch")
plt.xlabel("Branch")
plt.ylabel("Average Readiness Score")
plt.tight_layout()
plt.savefig("charts/hw_chart3_branch_readiness.png", dpi=100)
plt.close()

print("Charts saved.")
print()


# -----------------------------------------------------------------------
# PART 6 - THE REPORT
# -----------------------------------------------------------------------

weakest = skill_means.idxmin().replace("_Score", "")
ready_count = int((df["Readiness_Band"] == "Ready").sum())
largest_band = band_counts.idxmax()

print("=" * 60)
print("PART 6 - MODEL REPORT")
print("=" * 60)
print(f"1. Weakest skill : {weakest} "
      f"(avg {round(skill_means.min(), 1)})")
print(f"2. Ready now     : {ready_count} students")
print(f"3. Largest band  : {largest_band}")
print(f"4. Best training : {weakest} workshop")
print(f"5. Surprise      : {len(lopsided)} students code well "
      f"but communicate poorly")
print(f"6. Top 10 pick   : the 'Almost Ready' students closest to 75")
print()

df.to_csv("placement_results.csv", index=False)
print("Saved placement_results.csv")


# =======================================================================
# MARKING NOTES
# =======================================================================
#
# FULL MARKS REQUIRES:
#   - Communication identified as weakest        <- the designed finding
#   - Readiness_Score capped at 100
#   - All three charts titled and axes labelled
#   - Report written in plain sentences, no jargon
#
# COMMON ERRORS, in order of frequency:
#   1. Averaging the wrong axis (axis=0 vs axis=1)
#   2. Including Projects/Mocks in the skill average - they are counts
#   3. Forgetting .clip(upper=100)
#   4. Band boundaries off by one (>= 75 vs > 75)
#   5. Charts with no axis labels
#
# BONUS CREDIT:
#   - Noticed CSE/IT outperform ECE/MECH and asked WHY
#   - Found the lopsided group unprompted
#   - Questioned whether the scoring formula is fair
#
# THAT LAST ONE IS THE BEST ANSWER A STUDENT CAN GIVE.
# The weights (2 per project, 1 per mock) are invented - exactly like
# the 300-minute threshold in class. A student who challenges the
# formula has understood something most people miss entirely.
# Say so publicly when returning the work.
#
# THE DAY 9 BRIDGE - use this when handing marks back:
#   "You wrote the readiness rule by hand. You chose the weights.
#    On Day 9 the machine learns those weights from data.
#    Same columns. Same table. That is Machine Learning."
# =======================================================================

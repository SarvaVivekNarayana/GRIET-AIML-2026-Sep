"""
=============================================================================
DAY 1 - STEP 5 SOLUTION - NUMPY
TEACHER ONLY. Never release to students.
=============================================================================

Matches: STEP_05_NumPy_English.md
Syllabus: S3.1 NumPy Arrays, Indexing & Slicing. Depth MAX.

KEY: NumPy = Fast Math Engine.  One instruction. Many numbers.

DO NOT OPEN THIS FILE UNTIL STEP 4 IS DONE.
Students must SAY the sentence first:
  "I want to hand over a whole block of numbers and give ONE instruction."

Only then does NumPy appear. The tool must be earned.

TEACHING ORDER (do not reorder)
-------------------------------
  A  import + array
  B  the replacement table   <- emotional peak, do not rush
  C  indexing                <- budget 5 min, zero-based confuses
  D  slicing                 <- budget 8 min, exclusive end confuses more
  E  vectorised maths        <- the big moment
  F  boolean mask            <- show True/False array FIRST
  G  the trap                <- sets up Pandas
=============================================================================
"""

import csv
import numpy as np


# -----------------------------------------------------------------------
# LOAD THE STUDENT'S OWN DATA
# -----------------------------------------------------------------------
# Same CSV, same 7 days as Step 2, so the comparison is honest.

instagram_list = []
study_list = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        instagram_list.append(int(row["Instagram_Minutes"]))
        study_list.append(int(row["Study_Minutes"]))

instagram_list = instagram_list[0:7]
study_list = study_list[0:7]


# -----------------------------------------------------------------------
# PART A - BUILD THE TRAY
# -----------------------------------------------------------------------
# English: "Put the seven Instagram values into a NumPy array."
#
# ELI5 TO SAY OUT LOUD:
#   A Python list is a shopping bag. It holds anything.
#   A NumPy array is a calculator tray. Everything lined up,
#   same kind of number, ready for the calculator to work on all at once.

instagram = np.array(instagram_list)
study = np.array(study_list)

print("Instagram array:", instagram)
print("Study array:    ", study)
print()


# -----------------------------------------------------------------------
# PART B - THE REPLACEMENT TABLE
# -----------------------------------------------------------------------
# THIS IS THE EMOTIONAL PEAK OF THE DAY. Slow down here.
#
# Put Step 2 on the left half of the screen, this on the right.
#
#   Step 2 (4 lines)          ->  .sum()    (1 line)
#   Step 2 (2 lines)          ->  .mean()   (1 line)
#   Step 2 (5 lines)          ->  .max()    (1 line)
#   Step 2 (5 lines)          ->  .min()    (1 line)
#
# 16 lines of loops collapse into 4.

total = instagram.sum()
average = instagram.mean()
highest = instagram.max()
lowest = instagram.min()
days = len(instagram)

print("Total:  ", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest: ", lowest)
print("Days:   ", days)
print()

# CALLBACK TO BUG 3:
#   "NumPy does not guess which kind of division you meant.
#    .mean() gives you the true average, decimals and all."


# -----------------------------------------------------------------------
# PART C - INDEXING
# -----------------------------------------------------------------------
# Budget 5 minutes. Zero-based counting always costs time.

print("First day: ", instagram[0])    # counting starts at ZERO
print("Last day:  ", instagram[-1])   # -1 means "from the end"
print("Third day: ", instagram[2])    # third item lives at index 2
print()

# ASK BEFORE RUNNING: "Which index is the third day?"
# Most will say 3. Let them be wrong, then show index 2.
#
# ASK: "How would you get the last day without knowing the length?"
# Let them discover -1. Do not hand it over.


# -----------------------------------------------------------------------
# PART D - SLICING
# -----------------------------------------------------------------------
# Budget 8 minutes. This confuses more than indexing.
#
# THE RULE: the ending point is NOT included.

print("First three:  ", instagram[0:3])   # items 0,1,2  -> 3 values
print("Last two:     ", instagram[-2:])   # 2 values
print("Days 2,3,4:   ", instagram[1:4])   # items 1,2,3  -> 3 values
print()

# ALWAYS PREDICT FIRST: "How many values come back?"
#
# CALLBACK TO BUG 4 - say this out loud:
#   "Remember Days: 6 when we expected 7?
#    Same rule. Same trap. Now you know why."
#
# This callback is why Bug 4 exists. Do not skip it.


# -----------------------------------------------------------------------
# PART E - ONE INSTRUCTION, EVERY NUMBER  (VECTORISATION)
# -----------------------------------------------------------------------
# THE BIG MOMENT. In Step 2 each of these needed a full loop.

# English: "Convert every Instagram value from minutes into hours."
hours = instagram / 60
print("Hours per day:", hours.round(2))

# English: "For every day, subtract Instagram minutes from Study minutes."
difference = study - instagram
print("Study minus Instagram:", difference)
print()

# ASK: "If a value is negative, what does that mean about that day?"
# Answer: scrolled more than studied. Let THEM say it.
#
# SAY THIS:
#   "Two arrays. One minus sign. Seven answers.
#    In Step 2 that was a loop. Here it is one character."


# -----------------------------------------------------------------------
# PART F - THE SECURITY GATE  (BOOLEAN MASKING)
# -----------------------------------------------------------------------
# CRITICAL: show the True/False array FIRST. Do not jump to filtering.

gate = instagram > 100
print("The gate (True/False):", gate)

# Now let the values through
heavy_days = instagram[instagram > 100]
print("Values that passed:   ", heavy_days)

# Counting: True counts as 1, False counts as 0
how_many = (instagram > 100).sum()
print("How many passed:      ", how_many)

# Above their OWN average
above_average = instagram[instagram > average]
print("Above my own average: ", above_average)
print()

# CALLBACK TO BUG 5:
#   "No counter variable. Nothing to reset by mistake.
#    The bug from this morning cannot happen here."
#
# KEY: Filter = Security Gate. True passes. False stays outside.


# -----------------------------------------------------------------------
# PART G - THE TRAP THAT CREATES PANDAS
# -----------------------------------------------------------------------
# Let this FAIL in front of them. The failure is the lesson.
#
# English: "Put the date, the app name and the minutes in one array."

mixed = np.array(["2026-09-01", "Instagram", 95])
print("Mixed array:", mixed)
print("Data type:  ", mixed.dtype)
print()

# POINT AT THE OUTPUT:
#   Everything is now text. The 95 has quote marks around it.
#   The number stopped being a number.
#
# CALLBACK TO BUG 6:
#   "This is exactly this morning's bug - but now you know WHY.
#    A NumPy array wants ONE kind of thing."
#
# ASK: "Your CSV has dates, names AND numbers. So what do you need?"
# Wait for someone to say: a table.
#
# THAT is the door to Step 6. Do not open it yourself.


# =======================================================================
# COMPARISON TABLE - fill this on the board with them
# =======================================================================
#
#                                  Plain Python    NumPy
#   total / average / max / min         16            4
#   days above average                   5            1
#   convert all to hours                 4            1
#   places a silent bug can hide       many         few
#
# KEY: NumPy = Fast Math Engine. One instruction. Many numbers.
# =======================================================================

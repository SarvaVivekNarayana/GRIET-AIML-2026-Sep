"""
=============================================================================
DAY 1 - STEP 7 SOLUTION - CHARTS
TEACHER ONLY. Never release to students.
=============================================================================

Matches: STEP_07_Chart_English.md
Syllabus: S5.1 Matplotlib - Charts, Plots & Customization. Depth MAX.

KEY: Visualisation = Picture of the Answer

MINIMUM VIABLE: Chart 1 only. Charts 2-4 if time allows.

OPEN WITH THE 3-SECOND TEST
---------------------------
Put seven numbers on screen:   95  120  80  140  60  170  110
"Which is largest? Time yourself."
Then show the bar chart.
"Nothing changed except the format."

That is the entire argument for visualisation. Make it in 60 seconds.

ENFORCE FROM THE VERY FIRST CHART
---------------------------------
  - title
  - both axes labelled
  - legend when more than one series
This habit is easier to install now than to fix in Week 3.
=============================================================================
"""

import pandas as pd
import matplotlib

# Agg backend = save files without needing a display window.
# On student laptops plt.show() works fine - mention both.
matplotlib.use("Agg")
import matplotlib.pyplot as plt


df = pd.read_csv("digital_behaviour.csv")

# Rebuild the column from Step 6 so this file runs standalone.
df["Total_Screen_Time"] = (
    df["Instagram_Minutes"]
    + df["YouTube_Minutes"]
    + df["WhatsApp_Minutes"]
    + df["LinkedIn_Minutes"]
)

# Short labels - full dates make the x-axis unreadable.
df["Day_Label"] = [f"D{i+1}" for i in range(len(df))]


# -----------------------------------------------------------------------
# CHART 1 - SCREEN TIME BY DAY          *** THE ONE THAT MATTERS ***
# -----------------------------------------------------------------------
# English: "Each bar is a day. Bar height is total screen time."

plt.figure(figsize=(12, 5))
plt.bar(df["Day_Label"], df["Total_Screen_Time"], color="steelblue")

plt.title("My Screen Time by Day")   # never optional
plt.xlabel("Day")                    # never optional
plt.ylabel("Minutes")                # never optional

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/chart1_screen_time_by_day.png", dpi=100)
plt.close()

print("Chart 1 saved.")

# ASK FROM THE PICTURE ALONE - do not let them look at the table:
#   "Which day was your worst?"
#   "Any pattern? Weekends? Exam week?"
#
# FINISH THE SENTENCE - make a student say it out loud:
#   "This chart shows that ____, which means I should ____."


# -----------------------------------------------------------------------
# CHART 2 - WHERE DOES THE TIME GO
# -----------------------------------------------------------------------
# English: "Total minutes per app. Compare the four."

apps = ["Instagram", "YouTube", "WhatsApp", "LinkedIn"]
totals = [
    df["Instagram_Minutes"].sum(),
    df["YouTube_Minutes"].sum(),
    df["WhatsApp_Minutes"].sum(),
    df["LinkedIn_Minutes"].sum(),
]

plt.figure(figsize=(8, 5))
plt.bar(apps, totals, color=["#E1306C", "#FF0000", "#25D366", "#0A66C2"])

plt.title("Total Time by App (30 Days)")
plt.xlabel("App")
plt.ylabel("Total Minutes")

plt.tight_layout()
plt.savefig("charts/chart2_time_by_app.png", dpi=100)
plt.close()

print("Chart 2 saved.")

# ASK: "Which app quietly took the most time?
#       Was it the one you expected?"
#
# The word 'quietly' matters. The surprise is the teaching moment.


# -----------------------------------------------------------------------
# CHART 3 - STUDY VERSUS SCREEN
# -----------------------------------------------------------------------
# English: "Two lines. One for study, one for screen time.
#           Add a legend so the reader knows which is which."

plt.figure(figsize=(12, 5))
plt.plot(df["Day_Label"], df["Study_Minutes"],
         marker="o", label="Study", color="green")
plt.plot(df["Day_Label"], df["Total_Screen_Time"],
         marker="s", label="Screen Time", color="crimson")

plt.title("Study Time vs Screen Time")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.legend()                         # mandatory with 2+ series

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/chart3_study_vs_screen.png", dpi=100)
plt.close()

print("Chart 3 saved.")

# ASK: "Do the lines move together or in opposite directions?
#       On your best study day, what happened to screen time?"
#
# THIS IS A SEED FOR DAY 4 (correlation). Do not name it yet.
# Just let them SEE that two columns can be related.


# -----------------------------------------------------------------------
# CHART 4 - SHARE OF ATTENTION     [OPTIONAL]
# -----------------------------------------------------------------------
# RULE TO TEACH: pie charts are ONLY for parts of one whole.
# Never use a pie chart for things that do not add up to 100%.

plt.figure(figsize=(7, 7))
plt.pie(totals, labels=apps, autopct="%1.1f%%", startangle=90,
        colors=["#E1306C", "#FF0000", "#25D366", "#0A66C2"])

plt.title("Share of My App Time")
plt.tight_layout()
plt.savefig("charts/chart4_share_of_time.png", dpi=100)
plt.close()

print("Chart 4 saved.")
print()
print("All charts saved in charts/")


# =======================================================================
# CHART RULES - put these on a slide
# =======================================================================
#
#   Always title the chart        -> otherwise the reader guesses
#   Always label both axes        -> "120" of what?
#   Legend when 2+ series         -> otherwise lines are meaningless
#   No more colours than needed   -> colour must MEAN something
#   One chart, one message        -> needs a paragraph? split it
#
# THE HABIT TO CARRY ALL COURSE:
#   "This chart shows that ____, which means I should ____."
#   If they cannot finish that sentence, the chart is not done.
#
# STUDENT NOTE: on their laptops, plt.show() displays the chart.
# savefig() writes it to a file. Show both; they need savefig
# for the homework submission.
# =======================================================================

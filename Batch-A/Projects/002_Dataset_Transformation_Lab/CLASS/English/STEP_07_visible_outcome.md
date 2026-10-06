# Step 7 — Dataset Transformation Lab

**Today's deliverable. Raw table in, decision table out.**

---

## The rule for this build

Every number in your summary must come from an **axis** operation or
**broadcasting**. If you find yourself writing a loop over days, stop — you have
slipped back to yesterday's shape.

## What you produce

One summary table with exactly one row per app and these columns:

| Column | Meaning |
|---|---|
| App | app name |
| Total_min | total minutes over thirty days |
| Avg_per_day | mean minutes per day, one decimal |
| Peak_min | highest single-day value |
| Peak_day | the day number that peak happened |
| Zero_days | how many days this app was untouched |
| Avg_share_pct | average share of the day, in percent |
| Days_won | days this app was the top app |
| Weekend_avg | mean minutes on weekend days |
| Weekday_avg | mean minutes on weekdays |

Hints, not code:

- `Peak_day` comes from `argmax` down the columns, plus one for day numbering.
- `Zero_days` is a comparison against zero, summed down the columns. A
  comparison produces True/False; summing True/False counts them.
- `Days_won` reuses the winners array from Step 5.
- Weekend and weekday rows are two selections of the same table.

Build it as a pandas DataFrame so it prints as a clean table, and save it as
`day02_summary.csv`.

## Then say something human

Print three sentences that a person who has never seen a table could act on.
For example: which app consumed the most time, which app rises most at weekends,
and which app collapses at weekends.

Numbers are not insight until somebody can repeat them out loud.

## Submit

Three files in your folder by the end of the session:

1. `day02_usage.csv` — your generated data
2. `day02_summary.csv` — your transformation output
3. `day02_usage_chart.png` — your two-panel chart

---

**Why this is called a transformation lab:** you did not add data today. You
changed its **shape** — thirty by four became four by ten — and the new shape is
the one a human can decide from.

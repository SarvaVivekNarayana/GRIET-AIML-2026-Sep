# Day 2 Homework — Same Workflow, Different Domain

**Due: start of Day 3. Nothing here is copyable from a classmate.**

---

## The brief

Today you transformed **your app usage**. Tonight you transform **a classroom
energy log** — same shape, different meaning.

Build your own generator, modelled on the one you ran in Step 1, that produces
`day02_hw_energy.csv` seeded with your roll number:

| Column | Meaning |
|---|---|
| Day | 1 to 30 |
| Morning | your focus score 0-100 in the morning |
| Afternoon | your focus score 0-100 after lunch |
| Evening | your focus score 0-100 in the evening |
| Night | your focus score 0-100 late night |

Yes, these are invented numbers. The workflow is the point, not the data.

## What to deliver

1. **The generator** — one file, roll-number seeded.
2. **A summary table** with one row per time slot: total, average, peak value,
   peak day, share of the day, days that slot was your best slot, weekend
   average, weekday average. Save as `day02_hw_summary.csv`.
3. **One two-panel chart** — raw scores on top, share stacked below, labelled,
   titled, legend, one annotation on your best day. Save as a PNG.
4. **Three sentences** in a text file, stating what you would change about your
   week if these numbers were real.

## The constraint that is actually being marked

Open your final program and count. **Zero loops over days.** Every number must
come from an axis operation or broadcasting. A correct answer built with a loop
scores half.

Then answer this in your text file:

> If a fifth time slot were added tomorrow, how many lines of your program would
> change? Quote the number honestly.

## Stretch, optional

Add a sixth column that is not a score — a text label per day such as the
weekday name. Try to hold it in the same NumPy array as your numbers.

Do not fight it for more than ten minutes. Write down exactly what went wrong
and bring that sentence to class. It is Day 3's opening question.

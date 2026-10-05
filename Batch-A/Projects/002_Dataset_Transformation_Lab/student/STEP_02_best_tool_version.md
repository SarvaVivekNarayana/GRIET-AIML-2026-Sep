# Step 2 — Solve It Properly With What You Already Have

**You have NumPy 1-D arrays from Day 1. That is a strong tool. Use it fully.**

Type every line yourself. Nothing here is pasted.

---

## Part A — Load four columns

Read `day02_usage.csv` with pandas' `read_csv`. Pull out each app column and
convert it into a NumPy array using `to_numpy()`. You will end up with four
arrays named after the four apps, each holding thirty numbers.

Print the length of one of them. It must be 30. If it is not, stop and fix it
before going further.

## Part B — Answer the column questions

For each app, print:

- total minutes over the thirty days
- average minutes per day, rounded to one decimal

That is eight numbers, and each one costs you a single instruction. No loops.
This is good code. **Do not apologise for it.**

Before you move on, say which app you expected to be highest, then look. Being
wrong about your own phone is the most useful thing that will happen today.

## Part C — One derived measure

Create a new array holding **Study minutes minus Games minutes** for every day.
One subtraction, thirty answers — this is yesterday's KEY doing its job.

Print the day number of your best value and the day number of your worst value.
Remember that positions count from zero and day numbers count from one.

## Part D — Now the question changes direction

Keep your working code open. Add these two questions.

**D1. Which app won each day?**

You need thirty answers, one per day. Your arrays are stored per app, so you
will have to walk through positions with an index, rebuild each day's four
values by hand, find the largest of the four, and translate that position back
into an app name.

Write it. Do not shortcut it. Count the lines when you are done.

**D2. What share of each day did each app take?**

Add the four arrays together to get each day's total. Then divide each app's
array by that day total and multiply by 100.

Write all four lines. Then answer one question honestly: if we added a fifth
app tomorrow, how many of your lines change?

## Close — count both halves on the board

| Question type | Example | Lines it cost |
|---|---|---|
| One answer per app | total Video minutes | 1 |
| One answer per day | who won Day 12 | 9 + a nested loop |

The data did not get bigger. The **direction** of the question changed, and your
tool only knows one direction.

Hold that thought. Step 3 is the debug lab, and Step 4 is where we name the
problem properly.

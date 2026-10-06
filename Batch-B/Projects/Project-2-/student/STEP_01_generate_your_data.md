# Step 1 — Generate Your Own Data

**Ten minutes. Everybody ends with the same columns and different numbers.**

---

## Why your own data

Yesterday you analysed your digital behaviour. Today the same idea comes back
wider: four apps, thirty days, one table.

Because your file is seeded from your roll number:

- your answers cannot be copied from the person beside you
- your chart will look different from every chart on the projector
- if your number matches your neighbour's exactly, one of you made a mistake

## Do this

1. Take the file `generate_app_usage.py`.
2. Open it and change **one line only** — put your own roll number in.
3. Run it.
4. Confirm that `day02_usage.csv` now exists in the same folder.
5. Open the CSV and read the first three rows with your eyes.

## What you are holding

| Column | Meaning |
|---|---|
| Day | 1 to 30 |
| Chat | minutes spent in messaging apps |
| Video | minutes spent in video apps |
| Study | minutes spent in study apps |
| Games | minutes spent in games |

Thirty rows. Five columns. A few zero days, because real life has days where
you never opened an app.

## Before you write any code — predict

Write these three predictions in your notes now. You will check them at 5 pm.

1. Which app has the highest total?
2. Do you think your weekends look different from your weekdays? How?
3. On how many of the thirty days do you think Study was the top app?

Being wrong here is not a problem. Never having guessed is.

## If it fails

- Nothing appeared: you are running the file from a different folder than the
  one you are looking at.
- `FileNotFoundError` later in the day: same cause. Your CSV and your program
  must sit in the same folder.
- Numbers identical to a classmate: you both forgot to change the roll number.

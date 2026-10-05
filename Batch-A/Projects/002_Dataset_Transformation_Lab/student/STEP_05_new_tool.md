# Step 5 — One Table, One Instruction

**Unlocked only after somebody said the sentence in Step 4.**

**KEY: Whole Table, One Line.**

---

## ELI5 first

A 1-D array is a single shopping list. A 2-D array is the whole shop's
stock register: rows and columns, one object.

Once the computer holds the register instead of four loose lists, you stop
telling it *what to add up* and start telling it *which direction to sweep*.

- Sweep **down** the columns → one answer per app.
- Sweep **across** the rows → one answer per day.

That direction is called the **axis**. `axis=0` goes down. `axis=1` goes across.
That is the entire idea. Everything else today is a consequence of it.

## A — Build the table

Read the CSV again. This time select the four app columns together and call
`to_numpy()` **once**. You now have one variable, not four.

Print its `shape`. It must read `(30, 4)`: thirty rows of days, four columns of
apps. Say the shape out loud before you continue — the shape is the map.

## B — The direction dial

Using `sum` with an axis argument:

- totals per app — sweep down
- totals per day — sweep across

Then do the same with `mean`, `max` and `min`.

**Check yourself:** your per-app totals must match the four numbers you printed
in Step 2 Part B. If they do not match, your axis is the wrong way round. That
mismatch is the single most common mistake in this entire course, and it is
**silent** — exactly like bug 3 this morning.

## C — Kill the nine-line loop

Ask the table for `argmax` across each row. That returns, for every day, the
**position** of the winning app.

Make a NumPy array of your four app names, and index it with that result. Thirty
winners appear in one line.

Compare it against the winner list from Step 2. Same answers. Nine lines gone.

Then use `unique` with counts to print how many days each app won.

## D — Broadcasting: a table divided by a column

You want each day's percentages. Your day totals are thirty numbers; your table
is thirty by four. Those shapes do not match — and NumPy will stretch the
smaller one to fit, as long as you give the totals a second dimension so it
knows they are a *column*.

Do this and print the first row. It must add up to 100. **Verify it.** A
percentage row that does not total 100 means you divided by the wrong direction.

Now the same trick the other way: divide the whole table by each app's own
maximum, so every app is scaled against its own peak. No new loop. No extra
lines per app.

That stretching is called **broadcasting**. It is why your program stops growing
when your data grows.

## E — Questions you could not ask before

- Build a mask of weekend days, use it to select rows, and average down. Repeat
  for weekdays. One table, two selections.
- Print the single busiest day of the month and how many minutes it held.

Each of these is a row question. Yesterday each one cost a loop.

## F — The payoff

Add a fifth app column to your CSV and rerun everything in this file.

**Count how many lines you had to change.** That number is the lesson.

---

**Lock it in:** *Whole Table, One Line.*
Rows and columns in one object. `axis` picks the direction. Broadcasting
stretches the small thing to fit the big thing.

# Step 4 — Why Four Separate Arrays Break

**No new code. Laptops closed. Only honesty about what you just built.**

---

## Look at your working code

Answer these out loud, from the screen, without running anything.

1. How many variable names are holding one month of your life?
2. If tomorrow you add a fifth app, how many lines do you edit?
3. Your total line and your average line — how many times is each written?
4. Where in your program does "Day 12" exist as a single thing?
5. Point to the line that knows Chat and Study belong to the same day.

Question 5 is the one that matters. There is no such line.

## What it does well

Your Step 2 program is correct, short, and readable. `chat.sum()` is the right
call. `study - games` computed thirty answers in one instruction and you did not
write a loop to do it — that is exactly the Day 1 KEY working as promised. Nobody
in this room should apologise for that code. It is better than what most people
write in their first job.

Everything below is not a criticism of the code. It is a limit of the **shape**
you stored the data in.

## Now change the question slightly

Yesterday's question: **"How much Video in total?"** — one answer.

Today's question: **"Which app won each day?"** — thirty answers.

Watch what that did to your program in Part D:

- You rebuilt each day by hand, value by value, inside a loop.
- You introduced an index `i` so four arrays could be read at the same position.
- You introduced a second loop inside the first just to find the largest of four.
- You created a parallel list of names to translate a position back into an app.
- Nine lines. For a question a human answers by glancing at one row.

Then the share question forced four near-identical division lines. Four apps,
four lines. Not because the maths is hard — because your data has no rows.

## Pain 1 — Four names for one table

Your CSV has one table. Your program has four disconnected lists. Every
operation must be written once per app, and every new app rewrites the program.
The computer has no idea these four things are related.

## Pain 2 — You can only sweep in one direction

`chat.sum()` answers a **column** question: one app, all days.
"Total for Day 12" is a **row** question — and 1-D arrays have no rows.
To ask it, you had to rebuild the row yourself with an index. Every row
question you will ever ask costs you a loop.

## Pain 3 — Scale

Four apps is comfortable. This is the same problem shape as:
30 sensors × 1 year, 500 students × 12 subjects, 2,000 products × 52 weeks.
At forty columns you do not have a program. You have forty variables and a
typo waiting to happen — and typos here are **silent**, as you found out in the
debug lab.

## The historical reality

This is not a Python problem, and it is not new. Fortran added multi-dimensional
arrays in the 1950s because scientific work is table-shaped, not list-shaped.
In the mid-1990s, Jim Hugunin and collaborators built Numeric for Python, later
extended as Numarray; in 2005 Travis Oliphant merged the two into **NumPy**,
whose central object is deliberately not a list — it is the N-dimensional array,
`ndarray`, with a shape and named axes. The design choice being made was exactly
the one you are feeling right now: keep the table as **one object**, and let the
programmer say which **direction** to sweep. That is where `axis` comes from.

*(Source basis: NumPy official documentation and its published project history.)*

## Say the sentence before you see the tool

Nobody sees the next tool until somebody in this room says, out loud:

> "I want to treat all four apps as **one table**, and tell the computer which
> **direction** to add things up."

That sentence is the whole lesson. The tool is just the reward for saying it.

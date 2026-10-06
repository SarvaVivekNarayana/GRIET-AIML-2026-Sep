# Step 3 — Debug Lab

**Six broken programs. Released one at a time. You do not get the next one until
the room has fixed the current one.**

---

## The rule of this lab

> **Code that runs is not the same as code that is correct.**

Two of today's six bugs will crash. Four will not. Those four will run cleanly,
print a confident number, and be wrong. Nobody will tell you. That is the
expensive kind.

## How to work

1. Read the program before running it. Predict what it should print.
2. Run it. Compare against your prediction and against your own Step 2 output —
   you already know the right answers for your data.
3. When it crashes: read the **last** line of the error first, then the line
   number, then the line.
4. When it does not crash: ask *is this number plausible?* An average of 51
   when yesterday it was 51.2 is not a rounding style. It is a lost decimal.
5. Write down, in one sentence, **what the program actually did** versus what it
   was asked to do. One sentence per bug, in your notes. This is graded in the
   exit check.

## Your defence checklist

For every bug, check in this order:

- Does every name exist and is it spelled with the right capitals?
- Is a division `/` or `//`? What did the question ask for?
- Does every slice include the last item you meant? Ends are exclusive.
- Does a running total actually accumulate, or is it being overwritten?
- Is the subtraction the right way round? Read the question again, slowly.
- Are two lists being lined up by position, and are they the same length?

## Bug log — fill this in

| # | Crashed? | What it printed | What it should have printed | Root cause in one sentence |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |

## The line that matters

A bug that crashes costs you five minutes.

A bug that runs goes into a report, becomes a slide, and changes a real
decision. Four of today's six are that kind. Remember which ones — they come
back this afternoon when the new tool makes them impossible to write.

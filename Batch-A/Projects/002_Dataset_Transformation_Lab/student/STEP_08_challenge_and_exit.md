# Step 8 — Challenge, KEY, Exit

---

## Challenge — twenty minutes, in pairs

Pick **two**. The fast pairs will finish all four. Every one of them must be
solved with an axis operation or broadcasting. No loop over days.

1. **Streaks.** Find the longest run of consecutive days where Study beat Video.
   *(Hint: a comparison gives you True/False for all thirty days at once.)*
2. **Normalise.** Rescale every app to its own 0-to-1 range, so an app that
   peaked at 60 minutes and one that peaked at 180 can be compared on one chart.
   Plot both versions and say which chart is more honest and why.
3. **Weekend swing.** For each app, compute weekend average minus weekday
   average, and rank the apps by how much your behaviour changes at weekends.
4. **Attention budget.** If you could recover 30 minutes a day from the app with
   the highest average share, how many hours would you get back over the month,
   and what would the new share table look like?

## KEY recall — say it before you leave

> **Whole Table, One Line.**

Three checks, fastest hand answers:

- Which axis sweeps **down** the columns?
- Which axis gives **one answer per day**?
- What does broadcasting stretch — the big thing or the small thing?

Yesterday's KEY is still live: *One Instruction, Every Number.*
Today's is the same idea with a second dimension bolted on.

## Exit check — five questions, on paper

1. An array prints `(30, 4)`. What are the 30 and what are the 4?
2. You want each app's total across the month. Which axis, and why?
3. Your share row prints as 97.4 instead of 100. What went wrong?
4. Name one bug from this morning that the 2-D version made impossible to write.
5. In one sentence, when should somebody **not** bother with NumPy?

Plus: **one topic you want repeated tomorrow.** Write it. It becomes tomorrow's
recall starter.

## Next class teaser

Tomorrow the table gets messy: text columns, labels, a file with far more
columns than you want, and rows you need to look up by name rather than by
number. NumPy will run out — and you will meet the tool that is
**Excel Controlled by Python**.

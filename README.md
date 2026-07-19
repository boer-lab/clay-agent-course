# Using Clay in Claude Code

A six-lesson course for people who do not write code.

**Read it here: https://boer-lab.github.io/clay-agent-course/**

By the end you have a working Clay workflow that researches companies and hands back real
answers with sources you can check — built by typing plain English into Claude Code, in about
half an hour.

## Who it is for

Someone who uses ChatGPT, has never opened Clay or Claude Code, and assumes anything with
"Code" in the name is not for them. It is written to be read on a phone.

## What is in here

| Path | What it is |
| --- | --- |
| `index.html`, `lesson-*.html` | The published course |
| `course/` | The lesson source, in markdown |
| `starter-prompts.md` | Every prompt in the course on one page, plus what this route will and will not do |
| `build.py` | The static-site builder — python3, standard library only, no dependencies |
| `assets/` | Screenshots, taken from a real account |

To rebuild after editing a lesson:

```
python3 build.py
```

## On the facts

Every Clay fact in the course was run on a real Clay account on July 19, 2026, and the output
recorded before the lesson was written. The answers, timings, credit costs and confidence
ratings are real. Anything that could not be traced to something actually run was cut rather
than softened.

The scope rule was simple: if it worked on that account it went in, and if it did not, it stayed
out. So the limits described in the course are walls that were actually hit, not guesses about
what a given plan allows.

One thing worth knowing before you follow Lesson 2: Clay's search returns a different slice of
companies each time it runs, so the company names printed there are a real result rather than a
result you will reproduce.

Clay ships weekly. The dated claims in each lesson's "Fine print" will go stale — if you hit
something that no longer matches, the feedback link on every page comes to me, and corrections
are welcome.

One limit worth knowing before you start: this route does not build spreadsheet-style Clay
tables, and Clay's own documentation says there are no current plans to support it. That is
Clay's boundary rather than a Claude Code shortcoming. Nothing in the course needs a table.

Clay's CLI and API are supported on Mac and Linux. Windows is not supported during the open beta.

## Licence

Course text © Boer Chen. The starter prompts are CC BY 4.0 — use them, adapt them, credit me.

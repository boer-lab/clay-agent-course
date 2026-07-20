# Starter prompts

Everything this course had you say to Claude Code, on one page, plus an honest note on where this
route stops. Copy a line, fill in the blanks, send it.

Nothing here is code. They are sentences.

## The prompts

### Connect Clay — Lesson 1

```
Set up the Clay plugin by following the steps in
https://github.com/clay-run/agent-plugins
```

Then, to check it worked:

```
Which Clay account are you connected to right now?
```

It comes back with the account holder's name and a workspace number. A number rather than a
workspace name is normal.

### Find companies — Lesson 2

```
Find me ______ companies in ______ with at least ______ employees.
```

The list comes back in the conversation. It is not saved as a spreadsheet in your Clay account.

Clay's search returns a different slice of companies each time, so your list will not match the
one in the lesson — or the one you got an hour ago from the same request.

If nothing comes back:

```
That came back empty, describe these companies differently and search again.
```

### Build the workflow — Lesson 3

```
Create a Clay workflow called "Company Research." Add a step that takes a
company's website and uses Clay's AI web researcher (claygent) to return,
in one or two words, the industry the company is in. Then run it on
stripe.com and show me the result.
```

This is the one that leaves you something you keep. Open the link it gives you and you will see
the workflow sitting in your Clay account.

### Run it on more companies — Lesson 4

```
Run Company Research on ______. Then run it again on ______. Show me both
answers.
```

### Check its work — Lesson 4

```
For the ______ run, show me the reasoning and the sources behind that
answer, including the actual page it visited.
```

The answer, the confidence rating and the reasoning are all the researcher describing itself.
The page it visited is the only part you can check with your own eyes. Open that one.

### Change the question — Lesson 5

```
In my Company Research workflow, change the question the research step
asks. Instead of the industry, ask ______. Then run it on ______ and show
me the answer.
```

Ask for the shape of the answer you want — a few words, a yes or no, one of three labels you
name. An open-ended question gets you an essay.

### When something errors

```
That returned an error, read it and tell me what happened.
```

Clay's errors usually name the fix. A retry costs a credit or two, not nothing.

### When you want to see the question that actually ran

```
Show me the exact question that research step is running.
```

Handy when an answer comes back in a shape you did not expect. The run records the question it
used, and that is the ground truth.

## What this route will and will not do

Checked live on a real Clay account on July 19, 2026. Clay ships weekly, so re-check anything here
before you lean on it.

**Works:**

- Searching Clay's company data and getting real companies back.
- Building workflows by asking, and running them.
- Clay's AI web researcher (claygent), including the reasoning and the sources behind each answer.
- Run history — every run is kept, with its status, duration and cost.

**Does not work through this route:**

- **Building a spreadsheet-style Clay table.** Clay's own documentation says there are no current
  plans to support table building through the developer platform, and reading existing tables this
  way is limited to Enterprise plans. This is Clay's boundary, not a Claude Code limitation, and no
  rewording gets past it. Nothing in this course needs a table.
- **Windows.** Clay's CLI and API are supported on Mac and Linux; Windows is not supported during
  the open beta.

**Worth knowing:**

- If you later want a second fact about a company, add one of the ready-made enrichments rather
  than a second AI researcher step. Two researcher steps share one question, so both end up asking
  whichever was set last.
- Search results are capped per request and per month, and the monthly cap is easier to hit than you
  expect. Spend it on companies you do not already have — if you already have a list of websites,
  hand it straight to the workflow instead. Running into the cap gives you an error naming your
  usage and the reset date, so you will know it when it happens.
- Working this way costs no extra. Clay charges the same credits and actions as doing the same work
  in Clay's own interface.
- The Agent Plugin is in open beta and workflows are the newest part of it, so an occasional run
  stalling or failing is normal rather than a sign you built it wrong. Re-running is the fix.

Sources for the limits above: Clay's `clay-api-cli` documentation, checked July 18, 2026, plus live
runs on a real Clay account on July 19, 2026, including hitting the monthly search cap.

License: CC BY 4.0 — use it, adapt it, credit Boer Chen.

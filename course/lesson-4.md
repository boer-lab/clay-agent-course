# Lesson 4 — Check where the answer came from

**Time:** 6 min

## What this gets you

You already check sources. You look at who wrote the review before you trust the star rating. You click through to the article before you repeat the headline. It takes a few seconds, and it is the difference between knowing something and having heard it.

Your workflow is the same situation. The answer arrives short and clean: an industry, plus a rating where the researcher says it is "very high" confidence. It reads like something settled. You cannot tell a wrong answer from a right one by looking at it.

What you have here that a bare answer never gives you is the trail. Clay's AI web researcher keeps the page it visited and the text it read on the way there, and you can open that. This lesson is that habit: read the answer against the question you asked, then read the trail.

You already built the workflow in Lesson 3, so pointing it at a second and third company is just running it again. Each company gets its own run, and Clay keeps a row for each.

## What one answer is actually made of

Three companies, one run each: geico.com, zurichna.com, resourcepro.com. Those are the three I ran, and all three came back Insurance.

Each run lands as its own row in the workflow's Runs tab, which you see when you open Clay in your browser: status Done, how long it took, and what it cost. Three finished, none failed.

<!-- SCREENSHOT: file=runs-view-three.png | Three runs in the Runs tab, one per company. All Done, each with its own duration and cost. -->

Open one of those runs. For geico.com, the researcher returned four things:

1. **The answer.** "Insurance."
2. **How sure it says it is.** "Very high."
3. **Its reasoning, in its own words.** *"GEICO operates in the insurance industry, offering various insurance products including auto and homeowners insurance. This information was gathered from their official website [geico.com](https://www.geico.com)."*
4. **The steps it took.** This one holds the actual page it visited, https://www.geico.com, the links it found there, and the text it read off the page.

<!-- SCREENSHOT: file=run-sources.png | The geico.com run opened up: the answer, the reasoning naming the site it read, the confidence rating, and Steps Taken — the record of where it actually went. -->

The first three are the researcher talking about itself. Only the fourth is evidence you can look at with your own eyes.

A finished run also records the question the research step actually used. Read that first, against the question you sent in Lesson 3, and then read the trail.

The order is worth keeping. An answer in the wrong shape, who a company sells to when you asked what industry it is in, does not mean the researcher got it wrong. It means the question changed, and Lesson 5 covers how that happens. A source check on its own passes it, because the page really does back up the answer to whatever question ran.

And about those three matching answers. It is tempting to read three agreeing results as three confirmations. It is one researcher using one method, three times. If the method is off, it is off on all three, and they will still agree with each other.

Which is why you do not check all of them. You check the one a decision hangs on.

## Try it

You have the Company Research workflow from Lesson 3. Run it twice more, then look inside one answer.

1. Open Claude Code. Use geico.com and zurichna.com — those are the two I ran, so you have something to compare against. Two companies off your own Lesson 2 list work just as well; your list will not look like mine, and nothing in this lesson depends on it matching.

2. Ask for the runs:

   > Run Company Research on the first company. Then run it again on the second. Show me both answers.

   A run costs about three data credits and two actions, and each one lands as its own row instead of replacing the last. If one does come back failed, ask for it again.

3. Open the workflow in Clay and click the Runs tab. Your runs are stacking up, one row each. That list is your record, and it stays there.

Now pick one of the two runs you just made. Start with the question rather than the answer:

> Show me the exact question that research step actually ran.

Read it against the question you sent in Lesson 3. If it does not match, ask for yours back before running it again:

> Set the question on that research step back to asking what industry the company is in, then run it again.

Lesson 5 covers why it can differ. If it matches, go at the answer:

> Show me the reasoning and the sources behind that answer, including the actual page it visited.

What comes back has parts that are not worth the same:

| What it showed you | What to do with it |
| --- | --- |
| The answer, and the confidence rating next to it | Note it and move on. The researcher is grading its own work. |
| The reasoning, written out | Read it, and remember it is still the researcher describing itself. |
| The page it visited and the text it read there | Open this one. Ask whether that page says the thing. |

You are done when you can say two things out loud: this is an answer to the question I asked, and the page behind it says the thing. Not whether the reasoning is well written. Those two.

Watch for the answer that cannot point you to anything. If the researcher has no page to show you, that answer is not necessarily wrong. It is unchecked, which is a different thing. Treat it as unproven until you can see a page behind it.

One thing you may have noticed while you were doing this. Whichever companies you used, the question was still mine — what industry a company is in was probably never what you actually wanted to know. Lesson 5 swaps it.

## Check yourself

Four questions. Nothing is recorded, and a wrong pick just explains why.

```quiz-json
{"lesson": 4, "items": [
  {"q": "Your workflow returns \"Insurance\" for a company and marks its own confidence as \"very high.\" Which of these actually gives you a reason to believe the answer?", "options": [
    {"text": "The confidence rating. It said very high, and it was right about the last three.", "correct": false, "why": "The confidence rating is the researcher grading its own work, so a wrong answer can carry a high rating just as easily. It is useful as a flag, not as evidence."},
    {"text": "That the run finished in well under a minute with no errors.", "correct": false, "why": "Speed and a clean finish tell you the workflow ran, which is worth knowing. They say nothing about whether what came back is true."},
    {"text": "The page it visited and the text it read there.", "correct": true, "why": "That is the only piece you can look at yourself. The answer, the rating, and the reasoning are all the researcher describing itself; the visited page is the thing that either backs it up or doesn't."}
  ]},
  {"q": "You run the workflow on three companies and all three come back \"Insurance.\" What has that agreement earned you?", "options": [
    {"text": "Not much on its own. You still open the sources on the answer you plan to use.", "correct": true, "why": "Agreement is a comfort, not a check. Three answers matching is worth less to you than one answer whose page you actually opened."},
    {"text": "Three independent confirmations, so the answers are solid.", "correct": false, "why": "They look independent because they are three companies, but it is one researcher using one method three times. If the method has a blind spot, all three answers share it."},
    {"text": "Enough evidence that the industry answers are reliable and you can stop checking.", "correct": false, "why": "Three cheap answers agreeing is thin evidence for a fourth one, because they all came from the same method. The check that pays is on the answer you are about to use."}
  ]},
  {"q": "You have ten answers back and time to properly check one. Which do you open?", "options": [
    {"text": "The one with the lowest confidence rating.", "correct": false, "why": "A fair instinct, and worth a glance. But a shaky answer on a company you will never contact costs you nothing, so low confidence alone isn't what makes an answer worth your time."},
    {"text": "A random one, as a spot check on the batch.", "correct": false, "why": "Sampling is a real technique and it earns its place once you are running hundreds. With ten answers in front of you, going straight to the one driving a decision is the better use of the same minute."},
    {"text": "The one you are about to act on.", "correct": true, "why": "Checking follows the decision, not the score. The answer feeding a real next step is where a mistake actually costs you something."}
  ]},
  {"q": "A run finishes clean, marks itself \"very high\" confidence, and shows you a real page you can open. The answer tells you who the company sells to. You asked what industry it is in. What is going on?", "options": [
    {"text": "The question the step ran is not the question you wrote, so go look at the question before you look at the answer.", "correct": true, "why": "An answer in the wrong shape is a question problem, not an accuracy problem. Ask Claude Code to show you the exact question the step ran; if it is not yours, Lesson 5 is where you take it."},
    {"text": "The researcher misread the site, so run it again.", "correct": false, "why": "Nothing misfired. The run did exactly what it was told, and it was told something other than what you asked, so running it again buys you the same wrong-shaped answer at the same cost."},
    {"text": "Close enough — who a company sells to tells you roughly what industry it is in.", "correct": false, "why": "It doesn't, and that is the trap. This is the one case where the source check passes and the answer is still unusable, because the page really does back up the answer to a question you never asked."}
  ]}
]}
```

## Fine print

<details>
<summary>The exact steps, dates, and limits</summary>

- Everything above comes from three live runs on a real Clay account, July 19, 2026: geico.com, zurichna.com and resourcepro.com, each through the same two-step workflow. All three completed, all three returned "Insurance" with confidence "very high."
- Each of those three runs used 3.1 data credits plus 2 actions — the five-or-so credits a run cost you in Lesson 3. That per-run cost held on every one of the nineteen runs behind this course. The timing did not: across those nineteen runs the fastest finished in fourteen seconds and the slowest took thirty-four, averaging about twenty-two. Do not read a slow run as a stuck one. Note that this is the run's own clock, which is not the same as the researcher's "time taken" figure above — that one counts only its own working time and is always the smaller number.
- Verified live on July 19, 2026: a finished run records the question its research step actually used, and that question can differ from the one the step is named for. Lesson 5 covers the cause.
- On the geico.com run, the researcher reported its own working time as 7.82 seconds. That is its own count of its working time, not how long the run took. Its recorded steps contained the visited URL https://www.geico.com along with the links found on that page and the page text it read. That record is what makes the source checkable rather than a claim about a source.
- Running things this way does not cost extra. Clay charges the same credits and actions as the equivalent work done inside Clay's own interface (Clay docs: clay-api-cli, checked Jul 18, 2026).
- Clay's Agent Plugin is in open beta, and the workflow part is newer and rougher than the rest of it, so an occasional run failing or stalling is normal rather than a sign you built it wrong (Clay docs: clay-api-cli, checked Jul 18, 2026). Re-running is the fix.

</details>

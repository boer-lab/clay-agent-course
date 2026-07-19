# Lesson 3 — Build your first workflow (and watch it run)

**Time:** 6 min

## Why this matters

By now you can ask Claude Code to find companies. Finding them is nice. The real question a beginner has is quieter and a little scary: *can I actually build something in Clay, or am I just typing and hoping?*

You can build something. In this lesson you build a small Clay workflow — a saved set of steps that takes a company and hands back a real answer about it — and you run it. When you finish, there is a thing in your Clay account that you made, that works, that you can run again tomorrow. That is the moment the fear goes away.

One honest word first. The tool you are using — Clay's Agent Plugin — is new and in beta. Nothing in this lesson needs a paid plan.

## See it

A workflow is just a set of steps with a start and an end. Yours will have two: a **start** (you hand it a company website) and a **research step** (it looks the company up and tells you what it does).

You do not build this by clicking around Clay. You ask Claude Code, in plain English, and it builds it for you. Here is the whole thing, start to finish, exactly as it ran.

You:

> Create a Clay workflow called "Company Research." Add a step that takes a company's website and uses Clay's AI web researcher to tell me, in one or two words, what industry the company is in. Then run it on geico.com.

Claude Code creates the workflow, adds the step, and runs it. A few seconds later:

```
geico.com  →  Insurance   (confidence: very high)
```

That answer is not made up. The researcher visited geico.com, read the site, and reported back — it even keeps the links it used, so you can check its work (that is Lesson 4). A run takes well under a minute — some come back in under ten seconds, some take half a minute — and costs a few credits.

Here is what it looks like in your Clay account. The workflow is a little map — a start box connected to your research step:

<!-- SCREENSHOT: file=workflow-canvas.png | Your workflow in Clay: a start box wired to your research step, with a Run button. -->

And every time you run it, Clay logs the run so you can see what happened:

<!-- SCREENSHOT: file=runs-view-single.png | One run in the Runs tab: Done, how long it took, and what it cost. -->

## Try it

You will build the exact same thing. Nothing here changes anything outside this one workflow, and nothing costs more than a few credits.

First, what "done" looks like: a workflow named Company Research exists in your Clay account, and running it on a company website returns an industry. That is the whole target.

One thing you may see and should not read as failure: sometimes the answer comes back with no pages attached to it. That usually means the researcher's search turned up nothing and it answered from what it already knew instead of from a site. The answer may well be right. It is just unchecked, which is a different thing, and Lesson 4 is where you learn to tell those apart.

Now you:

1. Open Claude Code and make sure Clay is connected (Lesson 1). 
2. Copy this and send it, word for word:

   > Create a Clay workflow called "Company Research." Add a step that takes a company's website and uses Clay's AI web researcher (claygent) to return, in one or two words, the industry the company is in. Then run it on **stripe.com** and show me the result.

3. Watch what Claude Code does. It will tell you it created the workflow, added the step, and started a run. Give it up to half a minute, then it shows you the answer. For stripe.com the answer that comes back most often is "Financial Services." The exact wording moves around from run to run, so do not measure yourself against that string — any short label that means finance ("Fintech" is a common one) means you built it right.
4. Open the workflow in Clay. Claude Code gives you a link when it creates it — click it. You will see the little map from above, and a Runs tab with your run in it.

If it stalls or errors, tell Claude Code "that returned an error, read it and tell me what happened" — the error almost always says exactly what to fix, and a retry costs a credit or two rather than nothing.

## Check yourself

Three quick ones. A wrong pick just explains the idea.

```quiz-json
{"lesson": 3, "items": [
  {"q": "You asked Claude Code to build the workflow and it says \"Done — created Company Research and ran it on stripe.com.\" What is the surest way to know it's really there?", "options": [
    {"text": "Trust the message — it said done, so it's done.", "correct": false, "why": "\"Done\" is the agent's word for it, not proof. The whole habit this course builds is checking the thing itself — which here is one click away, so there's no reason not to."},
    {"text": "Open the workflow link in Clay and see the map and the run.", "correct": true, "why": "You looked at the real thing in Clay — the workflow and its run. That's the difference between hoping it worked and knowing it did, and it took one click."},
    {"text": "Ask Claude Code a second time if it's sure.", "correct": false, "why": "Asking again just gets you another confident sentence. The workflow is visible in Clay; look there, not at the agent's reassurance."}
  ]},
  {"q": "Your research step returns an industry for stripe.com. Where did that answer come from?", "options": [
    {"text": "Claude Code already knew it from training.", "correct": false, "why": "It's not the agent guessing from memory. Clay's web researcher actually visited the site and read it — which is why the answer is current and comes with the links it used."},
    {"text": "Clay's AI researcher visited the website and read it, then reported back.", "correct": true, "why": "That's the point of using Clay here instead of just asking an AI: the answer is grounded in the live site, with sources you can check."},
    {"text": "It came from a spreadsheet you uploaded.", "correct": false, "why": "You didn't upload anything, and there's no table involved — the workflow takes a website in and gives an answer back. The research comes from the live web."}
  ]},
  {"q": "A friend says \"just ask ChatGPT what industry Stripe is in — why build a workflow?\" What does the workflow give you that a one-off question doesn't?", "options": [
    {"text": "Nothing, really — it's the same thing with extra steps.", "correct": false, "why": "For one company you're right that it's overkill. The workflow earns its keep the moment you have a list — it's a saved, repeatable step, which is the next lesson."},
    {"text": "A saved, repeatable step you can run on company after company, with checkable sources.", "correct": true, "why": "That's the difference: build it once, run it on a hundred companies the same way, and every answer traces back to a real source. A chat window can't hand you that."},
    {"text": "It works without any internet connection.", "correct": false, "why": "It very much needs the internet — the researcher reads live websites. The real advantage is that it's saved and repeatable, not offline."}
  ]}
]}
```

## Fine print

<details>
<summary>The exact steps, dates, and limits</summary>

- Built and run live on a real Clay account on July 19, 2026. The research step uses Clay's "Claygent (AI Web Researcher)" action; the run on geico.com returned "Insurance" (confidence very high) for about 5 credits. Runs across this course have come back in as little as seven seconds and taken as long as thirty-four.
- The Agent Plugin is in open beta. Clay's documentation states there are no current plans to support building spreadsheet-style tables through the developer platform, and reading existing Clay tables this way is limited to Enterprise plans (Clay docs: clay-api-cli, checked Jul 18, 2026). A workflow does not need a table.
- Claude Code builds the workflow through Clay's plugin — you never write code or click through Clay's builder yourself. If you're curious what it ran under the hood, ask it "show me what you built" and it will walk you through the steps.

</details>

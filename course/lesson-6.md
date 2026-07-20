# Lesson 6 — What else this shape can do

**Time:** 5 min

## What this gets you

Nothing to build here. You are done building.

This is the lesson that tells you where the ceiling actually is, because the thing you made is
deliberately the smallest version worth having: you press Run, it asks one question about one
company. The same shape goes a long way further, and it would be a shame to finish this course
thinking that was all of it.

I am naming these, not teaching them. Each one is the move you already know — say what you want in
a sentence, then check what came back.

## Where it goes from here

**It does not have to be you pressing Run.** A workflow can also start:

- on a schedule you set
- when something calls it over the web, which is a webhook
- when someone new is added to a saved list of people in Clay, which Clay calls an audience
- when a spreadsheet file is uploaded, the kind that ends in .csv

One catch worth knowing before you reach for the schedule: a plain scheduled run starts with
nothing in its hands. If your workflow expects a company website, it has to get that from
somewhere, which is why the saved-list version below is the one that actually works.

**A workflow can hold more than two steps.** It can split down different paths depending on what an
answer comes back as, and it can run code. One thing to know if you go adding steps: a second AI
researcher step will not give you a second question. The two share one, so both end up asking
whichever was set last. When you want a second fact, reach for a ready-made step instead.

**The AI researcher is not your only option.** Clay keeps nineteen steps already built, each made to
go get one specific thing. Clay calls these enrichments, and you ask for them by name:

- Enrich Company
- Company News
- Company Job Openings
- Website Technology Stack
- Find People at Company
- Work Email

A named enrichment is cheaper than asking the researcher to go find the same thing, and it comes
back the same way every time. The full list is on the cheatsheet that comes with this course.

## What it looks like put together

Imagine part of your job is keeping the sales team's account list current. Every Monday you would
otherwise open twenty tabs, work out which of your accounts have started hiring, and type what you
found somewhere the team will see it.

Instead you describe that once, in the terminal:

> Take my saved list of target accounts. Every Monday morning, look up each one's job openings, ask
> the researcher whether that hiring looks like they are moving into a new market, and put what it
> finds into our CRM against the right account.

Claude Code builds it. From then on it runs on Monday whether you are there or not, and the answers
are waiting when you get in. You never opened Clay.

Note the shape of that: the list already exists. The workflow does not go and find companies for
you — it works through a list you keep. That is the piece people expect to be there and it is not.

## Try it

There is nothing to build. Two things worth doing instead, and both take a minute.

1. Ask Claude Code what it would take:

   > What would it take to run my Company Research workflow on a schedule instead of me pressing Run?

   Read the answer against this lesson. You are not building it — you are seeing whether you can
   follow the shape of the answer now. A month ago you could not have.

2. Take the cheatsheet. It is on the page linked at the top of this course, and it is written for
   Claude Code to read rather than for you. Drop it in your project folder and your agent starts
   knowing what took me a week to find out.

## Check yourself

```quiz-json
{"lesson": 6, "items": [
  {"q": "You want your workflow to run itself every Monday against your account list. Which part does the work of knowing which companies to run?", "options": [
    {"text": "The schedule. You tell it Monday and it goes and finds the companies.", "correct": false, "why": "A schedule only decides when. A plain scheduled run starts with nothing in its hands, so a workflow that expects a company website would fire with none. The list has to come from somewhere."},
    {"text": "A saved list in Clay that the schedule reruns.", "correct": true, "why": "That is why the Monday-morning example starts with \"take my saved list.\" The list is the context. The schedule just decides when to walk it."},
    {"text": "The AI researcher works out which companies you meant.", "correct": false, "why": "The researcher answers a question about a company you hand it. Choosing which companies to hand it is a different job, and that is what the saved list is for."}
  ]},
  {"q": "You want two facts about each company instead of one. What is the move?", "options": [
    {"text": "Add a second AI researcher step with the second question.", "correct": false, "why": "This is the one that catches people. Two researcher steps share a single question, so both end up asking whichever was set last, and you pay twice for one answer."},
    {"text": "Add one of the ready-made enrichments for the second fact.", "correct": true, "why": "A named step like Company News or Work Email has its own settings, costs less than asking the researcher to go hunting, and returns the same shape every time."},
    {"text": "Build a second workflow and run both.", "correct": false, "why": "It would work, and it is more moving parts than you need. A second step in the workflow you already have is simpler, and a ready-made one is cheaper than a second researcher."}
  ]},
  {"q": "What is the honest reason this course taught workflows rather than starting where most Clay guides start?", "options": [
    {"text": "Workflows are the best place for a beginner to start in Clay.", "correct": false, "why": "Most people who know Clay would point a beginner at the spreadsheet first, and they would be right. Workflows are what this particular route can build."},
    {"text": "It is what the Clay Agent Plugin can build today, and the course is really about talking to Claude Code.", "correct": true, "why": "The workflow was the thing you built while learning the actual skill. The plugin is in open beta and will do more later; the asking is the part that transfers."},
    {"text": "Workflows are the only useful thing in Clay.", "correct": false, "why": "Not close. Clay's spreadsheet side is where most of the work happens for most people, and this route simply does not reach it yet."}
  ]}
]}
```

## Fine print

<details>
<summary>The exact steps, dates, and limits</summary>

- The trigger types, node types and enrichment names above were read from the live plugin on July 19, 2026, not from documentation. Nineteen Clay-managed enrichments were listed by `clay functions list`; the trigger types were created and removed against a real workflow to confirm they are accepted.
- "Contextless" is Clay's own word for what a plain scheduled run hands the workflow, which is why the working example is built on a saved list instead. A schedule pointed at an audience segment reruns every member of that segment, and that trigger was created and deleted live on July 19, 2026 to confirm it is accepted.
- Sending results to a CRM is real: HubSpot, Salesforce, Attio and Pipedrive actions are all in the plugin's catalogue. This course does not walk through connecting one.
- A second AI researcher step sharing the first one's question was verified live on July 19, 2026: adding a new research step to an existing workflow silently rewrote the first step's question, while both steps kept their own names.
- Clay's Agent Plugin is in open beta and Workflows are at an earlier alpha stage and actively changing (Clay docs: clay-api-cli, checked Jul 18, 2026).

</details>

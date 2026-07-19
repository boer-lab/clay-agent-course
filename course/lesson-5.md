# Lesson 5 — Make it yours

**Time:** 9 min

## What this gets you

Your workflow asks one question right now: what industry is this company in. That was my question. I picked it because it is easy to check, and it is almost certainly not what you actually want to know about a company.

So change it. That is the whole lesson, and it takes one sentence.

The question is not buried in code somewhere. It is an ordinary sentence, written by Claude Code when you asked it to build the thing. You can ask for a different one.

## Changing the question

Open your workflow and look at the research step. Here is the question it is running:

```
Visit {{domain}}. In one or two words, what industry is this company in?
Return only the industry name.
```

The same sentence you met in Lesson 3, with `{{domain}}` still standing in for whichever website you hand it. When you ran it on stripe.com, that is what did the work.

Now swap the question. You do not edit anything by hand. You say what you want:

> In my Company Research workflow, change the question the research step asks. Instead of the industry, ask whether the company sells mainly to other businesses, to consumers, or to both. Then run it on aflac.com and show me the answer.

It comes back in fifteen to thirty seconds:

```
aflac.com

Answer       Both
Confidence   high
Sources      aflac.com, then a web search for Aflac's business model
```

Aflac genuinely sells both ways, and "both" is what came back. Notice what the confidence rating is worth, though: run the same question again and that rating moves around. It is the researcher grading its own work, which is exactly why Lesson 4 had you go look at the page instead. It found the "Business Owners" link on Aflac's own site, and you can go open that yourself.

Anything a person could work out by reading a company's public pages is fair game: what they sell, who they sell to, whether they mention a particular product, which markets they list. If the answer is not published anywhere, no wording will get it out of there.

Two limits are worth knowing before you go off on your own. This path does not build spreadsheet-style tables, and Clay has said plainly that it is not planning to. And the Agent Plugin is in open beta, with workflows the newest part of it, so small things will change under you.

The workflow does one job well: asking the same public-web question about company after company, and keeping the sources for each answer. That is enough for real work. Ten companies on a list, and you need to know which of them sell to hospitals. You hand the list over and it runs them one after another. Feeding a list in automatically is a next step, and this course does not cover it.

## Try it

Pick a question you actually want answered, the kind you would otherwise open ten tabs to figure out.

If the new one turns out worse, ask for the industry question back and you are where you started. Credits are not cash, and a retry costs a few of them.

1. Tell Claude Code the new question, in one plain sentence: *"In my Company Research workflow, change the question the research step asks. Instead of the industry, ask [your question]. Then run it on stripe.com and show me the answer."*
2. Read the answer, then read the reasoning underneath it. Start on stripe.com because you already saw what that company came back as, so you are the one who can catch a wrong answer.
3. Now your own companies. Hand Claude Code three or four websites you care about and ask it to run the workflow on each. If you do not have a list yet, Lesson 2 is where you get one.

You are done when the workflow hands you an answer to a question you wrote.

A run is a few credits, so if the first version comes back mushy, sharpen the question and go again.

## Check yourself

```quiz-json
{"lesson": 5, "items": [
  {"q": "You want your own question in the research step. Which one can it actually answer?", "options": [
    {"text": "How many people work on this company's finance team?", "correct": false, "why": "Almost nobody publishes their team headcounts, so the researcher has nothing to read. The questions this step handles are the ones a person could answer by opening the company's pages."},
    {"text": "Does this company sell to other businesses, to consumers, or both?", "correct": true, "why": "Companies say who they sell to all over their own site, so the researcher can read it and hand you the page it used. Public and readable is the whole test."},
    {"text": "Which vendor did this company almost sign with last year?", "correct": false, "why": "That lives in somebody's inbox, not on the web. The step reads public pages, so an unpublished answer is not going to come back no matter how you word it."}
  ]},
  {"q": "You swap in your question and the answer comes back vague — a paragraph that could describe half the companies you know. What is the fix?", "options": [
    {"text": "Rebuild the workflow, because something in it is set up wrong.", "correct": false, "why": "Nothing is set up wrong. The workflow did what the sentence told it to, and a loose sentence gets a loose answer, so rebuilding costs you the work and changes nothing."},
    {"text": "Sharpen the question and run it again.", "correct": true, "why": "Wording is the lever. Say what shape you want back — a few words, a yes or no, one of three labels you name — and the same workflow gets specific."},
    {"text": "Take it as read. That is as good as a machine reading a website gets.", "correct": false, "why": "It gets a lot better with a tighter ask. The industry question worked because it demanded one or two words; leave the shape open and you get an essay."}
  ]},
  {"q": "You already have 300 companies you care about, with their websites. Best move?", "options": [
    {"text": "Run them through Clay's search first, then run the workflow.", "correct": false, "why": "Search is the part with a monthly cap on it, so spending it on companies you already have burns the limited thing. Search is for finding companies you do not have yet."},
    {"text": "Give Claude Code the websites and run the workflow on those.", "correct": true, "why": "The workflow takes a website and gives back an answer, and it does not care whether that website came from Clay's search or from your own list. When you already have the list, hand it straight over."},
    {"text": "Ask Claude Code to build a Clay table to hold them first.", "correct": false, "why": "That one is off the menu through this path, and it is Clay's own limit rather than a mistake on your side. The workflow and its run history are what stick around for you."}
  ]}
]}
```

**One page to take with you.** Every sentence this course had you say to Claude Code is on a single page, so you are not digging back through the lessons to find the wording. It comes with the course, along with a cheatsheet written for Claude Code itself to read.

**What else this thing does.** You built the smallest version of this that is worth having: you press Run, it asks one question about one company. The same shape goes a good deal further, and this course does not teach any of it. I am naming it so you know the ceiling is not where you left it.

Start with how a workflow starts. It does not have to be you pressing Run. It can also start:

- on a schedule you set
- when something calls it over the web, which is a webhook
- when someone new is added to a saved list of people in Clay, which Clay calls an audience
- when a spreadsheet file is uploaded, the kind that ends in .csv

A workflow can also hold more steps, split down different paths depending on what an answer comes back as, and run code. One thing to know if you go adding steps: a second AI researcher step will not give you a second question. The two share one, so both end up asking whichever was set last. When you want a second fact, reach for a ready-made step instead.

And the AI researcher is not your only option for filling in a fact about a company. Clay keeps nineteen steps already built, each one made to go get a single specific thing. Clay calls these enrichments, and you ask for them by name. Useful ones to know about:

- Enrich Company
- Company News
- Company Job Openings
- Website Technology Stack
- Find People at Company
- Work Email

A named enrichment is cheaper than asking the researcher to go find the same thing, and it comes back the same way every time. The full list of nineteen is on the cheatsheet that comes with this course.

None of that is a new skill. Each one is the same move you already made: say what you want in a sentence and check what came back.

Put the pieces together and it looks like this.

Imagine part of your job is keeping the sales team's account list current. Every Monday you would otherwise open twenty tabs and work out which of your accounts have started hiring, then type what you found somewhere the team will see it.

Instead you describe that once, in the terminal. Take my saved list of target accounts. Every Monday morning, look up each one's job openings, ask the researcher whether that hiring looks like they are moving into a new market, and put what it finds into our CRM against the right account.

Claude Code builds it. From then on it runs on Monday whether you are there or not, and the answers are waiting when you get in. You never opened Clay.

That is the whole idea this course was pointing at. You are not learning a tool. You are learning to say what you want to something that can go and do it.

What you built is small. One workflow and a handful of runs.

The way in is a sentence. Most people who are nervous about this never find that out, because they decide early that it belongs to engineers and go read about it instead of opening it.

The question sitting in your research step will probably be the wrong question a month from now. That is fine, and it is the point. Open Claude Code, tell it what you want to ask instead, and run it again.

## Fine print

<details>
<summary>The exact steps, dates, and limits</summary>

- The question swap above is a live run on a real Clay account on July 19, 2026. A workflow with the same two steps, carrying the question "Visit aflac.com. Does this company sell mainly to other businesses, to consumers, or to both? Answer in a few words," returned "Both" at confidence "high" for about 5 credits. Across nineteen runs of this course's workflows, runs finished in fourteen to thirty-four seconds and every one of them cost the same few credits.
- Its recorded steps show what it read: aflac.com itself, including the "Business Owners" link on that page, followed by a web search for Aflac's business model.
- The confidence rating is not stable. The same aflac.com question came back "high" on one run and "very high" on another, and the same question on geico.com and zurichna.com came back "very high" (live runs, July 19, 2026). Treat it as the researcher's own opinion of itself rather than as a signal about the company.
- The question lives on a tool object Clay keeps at the workspace level, so a newly built research step attaches to the one already there rather than getting its own copy, and an edit made by anyone else building in that workspace lands on your step too. Verified live on July 19, 2026: a workflow whose step was still named "Research company industry" was in fact asking a pricing question, set by an edit made in a different workflow. Nothing errors when this happens — the run completes and returns real sources for the question that actually ran.
- The industry runs earlier in the course were made against the same shape on July 19, 2026: geico.com returned "Insurance" at very high confidence, and three companies (geico.com, zurichna.com, resourcepro.com) all completed with none failed.
- Clay's Agent Plugin is in open beta, and Workflows specifically are at an earlier alpha stage and actively changing (Clay docs: clay-api-cli, checked Jul 18, 2026).
- On tables: "The CLI builds logic via Workflows, not tables… There are no current plans to support table building via the developer platform." Reading existing Clay tables through this path is limited to Enterprise plans (Clay docs: clay-api-cli, checked Jul 18, 2026).

</details>

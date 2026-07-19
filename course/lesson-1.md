# Lesson 1 — Connect Clay

**Time:** 4 min

## Why this matters

Search for how to use Clay with AI and you get several different answers, all of them correct. That is where most people lose an hour, and it has nothing to do with being technical. There are three separate doors into Clay. They have similar names, Clay's own help pages cover all three, and nobody tells you which one you are standing in.

By the end of this lesson you are through the door this course uses, and you have checked that for yourself instead of taking the tool's word for it.

## See it

The three doors, shortest version:

1. **Clay's website.** You go to app.clay.com and work in a grid that looks like a spreadsheet. This is the Clay most people mean when they say Clay, and it is what you will land on most often when you go searching.
2. **The Clay connector.** Clay inside a chat tool like Claude. You type "find me people at this company" in a normal conversation and Clay answers you there. You ask, it answers. You do not build anything.
3. **The Clay Agent Plugin.** Clay inside Claude Code. You ask in plain English, and it builds and runs real things in your Clay account that stay there afterward.

This course is door #3.

MCP stands for Model Context Protocol. It is the shared plug standard these doors use underneath, so an AI tool can reach an outside service like Clay.

That is the last time this course explains it. You will see it in Clay's own course titles, "Clay MCP for Reps" and "Clay MCP for Ops", and both of those are about door #2, the chat one. If you go searching and land there, you will be in the right place for the other door.

You do not have to install Clay Agent Plugin by hand. There is nothing to download and no settings to get wrong. Clay's docs tell you to paste one line into your coding agent:

> Set up the Clay plugin by following the steps in https://github.com/clay-run/agent-plugins

That is Clay's own wording, lifted from their docs.

At some point it has to know who you are, so it will walk you through connecting your Clay account. Follow whatever it puts in front of you.

One flat rule for the whole course, and it holds for every lesson after this one: you never type a password or an API key, which is a long string of characters that works like a password for a tool, into the chat. If anything ever asks you to, stop there.

Once it says it is done, you ask it which Clay account it is in. Here is the shape of what comes back, with your own details in place of the placeholders. It is just a couple of lines of detail:

```
{
  "user": {
    "id": "<your user id>",
    "name": "your username"
  },
  "workspace": {
    "id": "<your workspace id>"
  }
}
```

Your own name, and a number for your workspace, which is the account area your Clay work lives in. Clay names the workspace by number here rather than in words, so your own name is the part to check.

## Try it

Same platform check as Lesson 0: this runs on Mac or Linux. Windows is not supported during the open beta.

The finish line is a sentence you did not write: the name of your own Clay account, coming back at you.

1. Open a terminal, type `claude`, press Enter, and ask it first whether the work is already done:

   > Is the Clay plugin already installed, and which Clay account is it in?

   If it comes back with your own name, you are through the door already. Skip to step 5 and read that answer properly. If it says the plugin is not there, carry on.

2. Send it that install sentence. Copy it or retype it, either is fine, and you can add "please" or explain yourself if it feels strange to just paste a line. You do not have to copy it exactly.

3. Stay with it while it works. It may stop and ask your permission before it runs something. Each prompt says what it is about to do, so read it and decide rather than clicking through on reflex. Nothing in this step spends Clay credits, and a failed attempt costs nothing to repeat.

4. When it gets to connecting your Clay account, do that part wherever it sends you. It does not happen in the chat.

5. Ask for proof, in whatever words you would normally use. Something close to:

   > Which Clay account are you connected to right now?

   You get back your own name and a workspace number, the same shape as the block above. Read it. Check that the name is yours.

A setup message saying "connected" is the tool describing itself. The account name coming back is you checking. Get in the habit now, because from Lesson 3 on you will be building things that live in that workspace, and you want to know which one it is.

If the sign-in step never appears, or you back out of it by accident, tell it to start the sign-in again. It will.

## Check yourself

Nothing here is graded. Pick one, read what comes back, keep going.

```quiz-json
{"lesson": 1, "items": [
  {"q": "You go looking for help and land on a Clay course aimed at sales reps using Clay inside a chat tool. What have you found?", "options": [
    {"text": "The right material for this course, just filed under a different name.", "correct": false, "why": "The names really do overlap, so this is an easy one to land on. That course covers door two, where you ask and Clay answers. This course is door three, where you build things that stay in your account."},
    {"text": "A course about a different door: Clay inside a chat tool, not Clay in Claude Code.", "correct": true, "why": "Both doors are real, both are genuinely Clay, and they do different jobs. The names sit close enough together that this catches almost everyone once, which is the only reason it is worth a question."},
    {"text": "An outdated page that no longer applies.", "correct": false, "why": "It applies fine, it is just about the other door. Clay runs both at the same time, and the naming is the only confusing part."}
  ]},
  {"q": "Setup reaches the point where it needs your Clay account. What should you expect?", "options": [
    {"text": "You paste your Clay password into the chat so the agent can sign in for you.", "correct": false, "why": "This sounds reasonable given the agent is doing everything else for you, which is exactly why it is worth being clear about. Signing in is the one exception. A password or a key never goes into the chat, in this lesson or any later one."},
    {"text": "It walks you through the sign-in somewhere other than the chat, and you follow what it puts in front of you.", "correct": true, "why": "Your sign-in stays between you and Clay, which is why the rule costs you nothing to follow. If anything ever asks you to type a password into a chat window, that is your signal to stop."},
    {"text": "Nothing, since the plugin works without a Clay account.", "correct": false, "why": "The work runs in a real Clay account and draws on that account's credits, which are the units Clay charges for each piece of work it does. So it has to know whose."}
  ]},
  {"q": "Setup finishes and the agent says Clay is connected. Why bother asking which Clay account it is signed into?", "options": [
    {"text": "No need. If it were not connected, it would have told you.", "correct": false, "why": "Usually true, and \"usually\" is carrying a lot of weight in that sentence. It is one line to send, and it takes about two seconds."},
    {"text": "Because the answer names the actual account, so you know where your work will show up.", "correct": true, "why": "Everything you build from Lesson 3 on lives in that workspace. Knowing which one it is now beats hunting for a missing workflow later."},
    {"text": "Because asking refreshes the connection and makes it stick.", "correct": false, "why": "Asking only reports what is already true. Nothing about the connection changes when you do it, so if something is broken, this reads it rather than repairs it."}
  ]}
]}
```

## Fine print

<details>
<summary>The exact steps, dates, and limits</summary>

- The install sentence is Clay's own, quoted from their docs: "Set up the Clay plugin by following the steps in https://github.com/clay-run/agent-plugins" (Clay docs: clay-api-cli, checked Jul 18, 2026).
- The Clay Agent Plugin is in open beta, and it runs on Mac and Linux only. Clay's wording: "Windows is not supported in open beta." (Clay docs: clay-api-cli, checked Jul 18, 2026.)
- Working this way costs no extra. Clay's docs: "API and CLI calls consume the same credits and actions as the equivalent work done in-product. There is no additional cost because work is triggered via the developer platform instead of the UI." (Clay docs: clay-api-cli, checked Jul 18, 2026.)
- Door two, the Clay connector, is set up separately from Claude's own connectors page at claude.com/connectors/clay (Clay docs: using-clay-in-claude, checked Jun 27, 2026). You do not need it for this course.
- The connection check was run live on July 19, 2026, and the block above is the real shape of its response with placeholders in place of the details. It returns the account holder's name and the workspace's id number. There is no workspace name in the answer.
- Used live on a real Clay account on July 19, 2026, with the Clay Agent Plugin at version 2.1.16 and the `clay` command at 0.1.17. The plugin and the command it installs are versioned separately, so a mismatch between those two numbers is not a broken install.
- One honest gap. All three testers already had the plugin in place, so the install and sign-in step is the one part of the course nobody has walked through cold. The install sentence is Clay's own wording from their docs, and the account check above is a real response — but what appears on your screen while you sign in is not something this course has watched happen.

</details>

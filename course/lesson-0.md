# Lesson 0 — Open Claude Code

**Time:** 4 min

## Why this matters

The name stops people. "Claude Code" sounds like something built for engineers, and plenty of people who would get real use out of it never open it once for that reason alone.

Claude Code is an app you type plain English into, the same way you type into ChatGPT. There is one difference, and it is the only one that matters: it can go and do things in other tools for you.

Here is what that buys you. By the end of these six lessons you will have built a small saved workflow that researches companies for you and keeps the sources behind every answer, and you will not have written a line of code. It lives in your Clay account and you can run it again tomorrow. Clay itself is a smart spreadsheet that finds companies and people and fills in facts about them. What you are building is one of the moving parts inside it, not the spreadsheet.

Before you spend six lessons on this, one thing you should hear from me and not find out at lesson four. Clay's Agent Plugin, the piece that lets Claude Code reach into Clay, is in open beta, and Clay limits parts of it by plan.

The main thing you cannot do is build a spreadsheet-style table. Clay has not opened table building to this route. That is on Clay's side, so no rephrasing will get you past it. Everything you build in this course works without a table.

## See it

You do not learn commands to use this. You type a sentence and it answers. Then you type another one.

Two examples.

You type:

> I want to build a personal budget tracker. What would I need?

It answers you in plain sentences. Nothing surprising there. Any chat tool does that.

<!-- SCREENSHOT: file=claude-code-chat.svg | An illustration of the shape of it: you type a sentence, it answers in sentences. That is the whole interface. -->

Then you type:

> Create a Clay workflow called "Company Research." Add a step that takes a company's website and tells me what industry the company is in. Then run it on geico.com.

That one does not come back as an explanation of how you might do it. Claude Code builds the thing inside your Clay account, runs it, and hands you the answer about the company. That is Lesson 3, and it is why you are using this app rather than asking a chatbot about Clay.

Claude Code opens inside a terminal window, which is the plain window your computer already has for typing instructions into. Once Claude Code is running in it, that window behaves like a chat.

## Try it

By the end of this you will have Claude Code open on your machine and one answer on the screen. No Clay yet.

The four minutes on this lesson is reading time. The install takes however long it takes on your connection, and you only do it once.

Claude Code is Anthropic's own app. Anthropic's Claude Code documentation is where the install steps, the systems it supports, and the Claude plans that include access are kept current, so start there rather than from a copy of those details written down here months ago.

1. Open a terminal. On a Mac, press `Cmd + Space`, type `Terminal`, and press Enter. On Linux, search your applications for Terminal. A window opens with a blinking cursor.

2. Install Claude Code by following Anthropic's instructions for your system. Text will scroll past while it works, and the installer tells you when it has finished. If it stops with an error instead, copy the error text and search it — nothing has broken, and running the install a second time costs you nothing but a minute.

3. Type `claude` and press Enter. The first time you do this it will walk you through signing in to your Claude account. Follow what it asks.

4. Ask it something. Pick one of these, or write your own question the way you would ask a knowledgeable friend:

   > what can Claude Code do?

   > I want to build a personal budget tracker. What would I need?

   Read the answer. It comes back in ordinary sentences, and there is no code in it anywhere.

Asking a question does not change a single file on your computer, so ask as many as you want until the window stops feeling strange. When you are done, close the window.

## Check yourself

```quiz-json
{"lesson": 0, "items": [
  {"q": "What separates Claude Code from a normal chat window?", "options": [
    {"text": "The answers it writes are more detailed.", "correct": false, "why": "Answer quality is not the split. Both write you sentences. The one that matters is that Claude Code can act in other tools, which is exactly what you will point at Clay."},
    {"text": "It can act inside other tools.", "correct": true, "why": "You give permission, it does the thing. Every lesson after this one leans on that single capability."},
    {"text": "It only works on files you have already uploaded to it.", "correct": false, "why": "There is no uploading step. It works with what is on your machine and with tools you connect to it, which is how Clay enters the picture in Lesson 1."}
  ]},
  {"q": "You open a terminal window, type `claude`, and press Enter. What is that window like from then on?", "options": [
    {"text": "You have to learn terminal commands before you can ask it anything.", "correct": false, "why": "No commands to learn. You write the way you would write to a person who already knows the tools."},
    {"text": "You type messages and read replies, the same as any chat.", "correct": true, "why": "The window stops being a place for commands and becomes a conversation. That is the whole interface for this course, and it is why nothing here looks like programming."},
    {"text": "It takes one question and then closes.", "correct": false, "why": "It stays open and keeps the thread, so you can follow up. Asking questions changes nothing on your computer, which makes it a cheap place to poke around."}
  ]},
  {"q": "Later on you find you cannot get Clay to build you a spreadsheet-style table this way. What is actually happening?", "options": [
    {"text": "Claude Code is not capable enough for that job.", "correct": false, "why": "The app is not the thing saying no here. The refusal comes from Clay, and telling those two apart saves you a lot of guessing later."},
    {"text": "Clay does not offer table building through this route.", "correct": true, "why": "It is Clay's boundary, set on Clay's side. What you build instead is the thing this course is about, and it works without a table."},
    {"text": "You phrased the request badly and a better prompt would work.", "correct": false, "why": "Good instinct in general, and it is the wrong lever here. When the tool itself has drawn the line, rewriting the sentence cannot move it, so the useful skill is spotting which side a limit sits on."}
  ]}
]}
```

## Fine print

<details>
<summary>The exact steps, dates, and limits</summary>

- Claude Code is Anthropic's app. Its install steps, supported systems, and the Claude plans that include access are documented by Anthropic and change over time — check Anthropic's Claude Code documentation for the current version rather than trusting a copy here. Start a session by typing `claude`.
- Clay's Agent Plugin is in open beta. Clay's CLI and API are supported on Mac and Linux; Windows is not supported in open beta (Clay docs: clay-api-cli, checked Jul 18, 2026). Lesson 1 covers what that means for you.
- Clay's documentation states there are no current plans to support building tables through the developer platform, and that reading structured data from existing Clay tables is available on Enterprise plans only (Clay docs: clay-api-cli, checked Jul 18, 2026).
- The Agent Plugin open beta is available on all modern Clay plans and, for a limited time, on legacy plans through the end of 2026 (Clay docs: clay-api-cli, checked Jul 18, 2026).

</details>

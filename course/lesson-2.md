# Lesson 2 — Find real companies

**Time:** 4 min

## What this gets you

Say you want a list of companies in one particular field. Places you might apply to, or the competitors of a company you are curious about. Doing that by hand means a search box, a pile of open tabs, and copying names and websites into a document one at a time, and a while later you are still not done.

Here you describe the kind of company you are after, in ordinary English, and a list of real companies comes back with their websites on it.

You do not need to know how Clay's search works, and you will not type anything that looks like code.

## One sentence, twenty companies

Say you want large insurance companies in the United States. The ask:

> Find me insurance companies in the United States with at least a thousand employees.

You do not name a single filter and you do not type a code. Claude Code reads that sentence and picks the filters itself (industry: insurance, country: United States, size: a thousand employees and up), runs the search against Clay's company database, and comes back.

Twenty companies, with more waiting behind them. The top of the list, as an example of the shape you get back:

```
HUB International       hubinternational.com
Farmers Insurance       farmers.com
Xceedance               xceedance.com
GEICO                   geico.com
Zurich North America    zurichna.com
ReSource Pro            resourcepro.com
```

It is just a list. Real companies, real websites, and each row has more on it than the excerpt shows: what the company does, how big it is, where it is based, roughly what it earns.

Run that same search yourself and your list will not match mine. That is not a mistake. Clay returns a different slice each time it runs, so twenty completely different insurance companies is just as correct an answer. A few rows may repeat, and one every so often comes back with no website at all, so skip those rather than assuming something broke.

That list came back **in the conversation**. Clay did not create a spreadsheet in your account, and if you go looking for one you will not find it. You read the list, you copy what you want, and that is the end of it.

The thing you build and keep inside Clay comes next. Two lessons from now you will point it at a list like this one.

## Try it

You are going to do the same thing, with a kind of company you pick. You are done when there are company names and websites on your screen that you did not type. If the list comes back empty instead, that is not a mistake on your part, and the fine print explains what it means: reply with "that came back empty, describe these companies differently and search again."

A search only reads, so nothing you type here changes anything in your Clay account. It does draw on a monthly allowance of search results, though, and that allowance is easier to use up than you would expect. Aim once rather than firing off ten rough attempts.

If what comes back is an error naming how many results you have used and a date it resets, that is the monthly allowance gone, and nothing is broken. Running out announces itself as an error rather than a quiet empty list, the count resets next month, and you can do the rest of the course without it by using geico.com and zurichna.com wherever a later lesson asks you for a company.

Fill in the blanks:

> Find me \_\_\_\_\_\_ companies in \_\_\_\_\_\_ with at least \_\_\_\_\_\_ employees.

"Find me hospital software companies in Canada with at least fifty employees." "Find me video game studios in Japan with at least a hundred employees." Pick any kind of company you are actually curious about, whether that is the one you are interviewing at next week or a field you are thinking about working in.

Send it, and you should get a list back in the same shape as the one above.

## Check yourself

```quiz-json
{"lesson": 2, "items": [
  {"q": "You want mid-sized logistics companies in Germany. Which ask gets you further?", "options": [
    {"text": "\"List every logistics company you know of in Germany.\"", "correct": false, "why": "That asks the agent to recite from memory instead of searching Clay, so you get names without websites and no way to tell what is current. Say \"find me\" and let it run a real search."},
    {"text": "\"Search Clay with industry = Logistics, country = Germany, size = 200-500.\"", "correct": false, "why": "You are guessing at Clay's filter names and the value formats behind them, and its industry labels may not match the word you reached for either. All of that is something the agent can simply look up."},
    {"text": "\"Find me mid-sized logistics companies in Germany.\"", "correct": true, "why": "Plain description in, agent picks the filters. You never have to learn Clay's filter names."}
  ]},
  {"q": "Your search comes back with nothing. No error, no warning, just an empty list. Most likely?", "options": [
    {"text": "The agent searched on a filter that Clay accepts but that holds no matching values, so nothing came back.", "correct": true, "why": "Clay takes the filter, finds nothing behind it, and hands back an empty list instead of complaining. Reword your description in plainer terms and search again."},
    {"text": "There genuinely are no companies like that.", "correct": false, "why": "Before you decide they do not exist, ask yourself whether you described them the way Clay would label them. Re-describe once, then decide."},
    {"text": "You have used up your searches for the month.", "correct": false, "why": "Running out of results is a real limit, but it does not arrive as a silent empty list."}
  ]},
  {"q": "The list is on your screen and you want it. You open Clay in your browser to go find it. What is there?", "options": [
    {"text": "A new spreadsheet holding those companies.", "correct": false, "why": "Most people expect that, and it is the one expectation worth dropping early. The search hands the list to you in the conversation instead of storing it."},
    {"text": "Nothing from the search. The list lived in the conversation.", "correct": true, "why": "The list was never saved anywhere, and that is the design rather than a missing setting. What you build and keep in Clay is the workflow in Lesson 3, and that one does show up in your account."},
    {"text": "The list, but locked until you upgrade your plan.", "correct": false, "why": "It was never stored. The search hands results back to you rather than saving them, so this is about where results go, not about what you are allowed to see."}
  ]}
]}
```

## Fine print

<details>
<summary>The exact steps, dates, and limits</summary>

- Run live on a real Clay account on July 19, 2026. The plain-English ask above became a search for industry "Insurance", country "United States", and headcount thresholds of 1,000 / 5,000 / 10,000. It returned 20 companies with more available. The six names in the lesson come from that run and are printed as an example of the shape, not as the result you should expect: the same filters, run again on the same account on the same day, returned twenty different insurance companies with none of those six among them.
- Under the hood the agent does three things: checks which filters Clay's search offers, creates the search, then runs it. You never type any of that.
- Each result comes with name, description, company type, size, country, location, website, industry, annual revenue and total funding range, plus a LinkedIn page. The excerpt in the lesson shows two of those.
- Search results are capped per request and per month, and how many you get depends on your Clay plan (Clay docs: clay-api-cli, checked Jul 18, 2026). The cap is real and reachable: it was hit live on Jul 19, 2026 at 100 results for the month. Running into it returns an error that names how many you have used and the date it resets, not an empty list, so you will know exactly what happened.
- Why empty happens: when the agent searches on a filter Clay accepts but that carries no values behind it, the search returns an empty list rather than an error, verified live Jul 19, 2026. A value outside a filter's allowed list behaves differently and does produce an error, and that error names the valid values, so the agent can usually correct itself. The silent-empty case is the one that needs you to re-describe.
- On the missing spreadsheet: Clay says this way of building is for workflows only, and there are no plans to let it build spreadsheet-style tables (Clay docs: clay-api-cli, checked Jul 18, 2026).

</details>

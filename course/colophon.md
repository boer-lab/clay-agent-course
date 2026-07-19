# How this course was built

This page is here because a course that tells you to check where an answer came from should say
where its own answers came from.

## Everything in it was run, not recalled

Every Clay fact in these six lessons was executed on a real Clay account on July 19, 2026, and the
output was recorded before the lesson was written. The company names are the ones the search
actually returned. The industry answers are the ones the researcher actually gave. The durations,
the credit costs and the confidence ratings are the real ones, copied out of real runs. The
screenshots are that same account, cropped only to remove the workspace name and the browser
window around it.

The limits in the course were verified live, not looked up. The monthly search cap in Lesson 2 is in
there because testing ran straight into it, and tables are out because trying to reach them came
back refused.

That discipline exists because the first two attempts at this course failed it. Earlier drafts
taught things that had never been tried — a spreadsheet-style table you cannot actually build this
way, an install command that did not exist, a documentation page at a URL that was never real.
Every one of those read perfectly well. None of them would have worked for you.

So the rule for this version was narrow: if a sentence could not be traced to something that had
been run and logged, it came out. Not softened, not hedged — removed. A few useful-sounding claims
died that way, including how long installing and signing in takes, because nobody had timed it.

## Where the limits come from

The plan limits, the beta status, the Mac-and-Linux support and the position on tables are quoted
from Clay's own `clay-api-cli` documentation, checked July 18, 2026, and are cited by date in each
lesson's Fine print rather than in the body.

One of those deserves naming here. Clay's documentation states there are no current plans to
support building tables through this route. An earlier draft of Lesson 3 predicted the limit would
lift as the beta opened up. That was a guess dressed as a fact, it contradicted the vendor's own
stated position, and it was cut before publication.

## What an independent test found

Before this published, three testers followed the course cold, with live Clay tools and no help
from the author. All three reached a working workflow with real, sourced output. Nineteen runs
between them, none of them failed.

They also broke things. The biggest was a claim in Lesson 5 that turned out to be false. The
research question does not live inside your workflow. It sits on a shared object in the workspace,
so changing the question in one place can quietly change it somewhere else. Nothing errors when
that happens, which is what makes it worth a warning.

Several published specifics did not reproduce either: the industry the lessons predicted for one
example company, how long a run takes, and the list of companies a search hands back. The
credit-balance point above came out of the same test. All of it was corrected before publication.

One thing the test could not check: every tester already had the plugin installed and signed in,
so nobody exercised that step. Installing and signing in is the riskiest part of this course for
someone who has never opened a tool like this, and it is the one part with no test evidence
behind it.

## How it was made

Written with Claude Code, the same tool the course teaches, against a verified-facts file that
every lesson had to trace back to. Drafts were fact-checked line by line against that file and
against Clay's documentation, then read again for voice and for whether a non-engineer could
actually follow them. The site is a small Python script and hand-written CSS — no framework, no
tracking, no fonts or scripts loaded from anywhere else.

The course was shaped for one specific reader: someone who uses ChatGPT, has never opened Clay or
Claude Code, and suspects that anything with "Code" in the name is not for them.

## Credits and licence

Built during the AlphaForge GTM engineering cohort, whose builders and instructors are the reason
the author knew enough to write any of this down.

Starter prompts are published under CC BY 4.0 — use them, adapt them, credit Boer Chen.

Found something wrong, or something that did not work on your machine? The feedback link at the
bottom of every page goes straight to the author. Corrections are welcome, and the dated facts
above are exactly the kind of thing that goes stale.

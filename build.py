#!/usr/bin/env python3
"""Static-site builder for "Using Clay in Claude Code" (v2).

Reads course/lesson-0.md .. lesson-5.md (plus optional course/colophon.md and
the gift artifact at ./starter-prompts.md) and writes HTML to ./docs/. Stdlib only.

    cd repo && python3 build.py

Idempotent: safe to re-run whenever the lesson markdown changes.

Descended from v1's builder. What changed for v2: the course teaches a build rather
than a discipline, so the NotebookLM embeds, the flashcard deck, the "which tool?"
reference page and the FormSubmit plumbing are all gone. Screenshot comments now
resolve to real images when a file is named. Feedback is a plain link to a Google
Form the author owns, so no endpoint token and no email ever enters this repo.
"""

import html
import json
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
# The lesson markdown sits beside the repo while drafting and inside it once
# published, so accept either layout.
COURSE = REPO / "course" if (REPO / "course").is_dir() else REPO.parent / "course"
# Output is "docs" because GitHub Pages serves a project site from the repo root
# or /docs, and nothing else.
SITE = REPO / "docs"
ASSETS = REPO / "assets"
# Hand-written CSS/JS. These used to live in docs/ alongside the generated
# pages, which made "never edit docs/" untrue and easy to trip over. They are
# source now, and get copied into docs/ on every build.
STATIC = REPO / "static"
N_LESSONS = 7

SITE_TITLE = "Using Clay in Claude Code"
TAGLINE = ("Clay is a smart spreadsheet that finds companies and people and fills in facts "
           "about them. You do not need to know how to code to build in it. In six short "
           "lessons you build something real, by asking for it in plain English.")
BYLINE = "Boer Chen"
# Every one of five test readers asked what this costs, and two closed the tab
# over it. The Claude-side answer is a hard yes-it-costs-money, quoted from
# Anthropic's own docs, and it belongs above the fold rather than one click in.
PREREQS_TITLE = "What you need, before you start"
PREREQS = [
    "A Mac or a Linux machine. Clay's plugin does not run on Windows while it is in open beta. "
    "If you are on Windows, Lesson 1 describes a second way into Clay that works in an ordinary "
    "chat window instead, and costs you nothing to read.",
    "A paid Claude plan. Anthropic's documentation is blunt about it: Claude Code needs a Pro, "
    "Max, Team, Enterprise or Console account, and the free Claude.ai plan does not include "
    "access. This is the one thing here that definitely costs money.",
    "A Clay account. Clay's documentation says this way of working is available on all their "
    "plans, including free ones.",
    "About 25 Clay credits and 16 actions to finish all six lessons. That is measured, not "
    "estimated: every run in this course cost 3.1 credits plus 2 actions, and the course asks "
    "you for seven or eight runs. Ask Claude Code what your balance is before you start.",
    "A terminal window, which your Mac already has. Lesson 0 shows you how to open it. You will "
    "not type any code into it.",
]

BANNER = ("Every Clay fact here was run live on a real Clay account on July 19, 2026. "
          "Clay ships weekly — check the current docs before relying on any limit.")

# Two different forms, deliberately. The footer link is for "this is broken /
# this is wrong" and fires on every page; the survey is the end-of-course ask and
# only appears once the reader has finished. Collapsing them into one form would
# mix bug reports into course feedback and make both harder to read.
# Both are Google Forms the author owns, so no email appears in the page source.
FEEDBACK_URL = "https://forms.gle/tWV7KC5qhFK3eYji7"
SURVEY_URL = "https://forms.gle/2iZnLKvbZJThkieP9"

# The gift page. Its prose lives in course/gift.md; the artifacts themselves are
# raw files copied into docs/ so each download is a plain, ungated link. The page
# introduces them rather than inlining them - an earlier version pasted the whole
# artifact above its own download button, which made the page pointless.
GIFT_PAGE = "gift.md"
GIFT_NAV_LABEL = "Take with you"
GIFT_BADGE = "The gift"
GIFT_BLURB = ("A cheatsheet your coding agent can read, and the plain-English asks "
              "that build the workflow.")
GIFT_LICENSE = "License: CC BY 4.0 — use it, adapt it, credit Boer Chen."
GIFT_FILES = [
    ("clay-agent-cheatsheet.md", "The cheatsheet, for your agent"),
    ("starter-prompts.md", "The starter prompts, for you"),
]

# ---------------------------------------------------------------- inline markdown

def _restore_codes(text, codes):
    for i, c in enumerate(codes):
        text = text.replace(f"\x00{i}\x00", c)
    return text


def inline(text):
    """Convert inline markdown (code, bold, italic, links) on an escaped string."""
    text = html.escape(text, quote=False)
    codes = []

    def stash(m):
        codes.append(f"<code>{m.group(1)}</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = re.sub(r"\*\*([^*]+(?:\*[^*]+)*)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    # Markdown backslash escapes. Without this, lesson 2's fill-in-the-blank
    # prompt rendered as literal \_\_\_\_ on the one line a reader is meant to copy.
    text = re.sub(r"\\([_*\[\]()#+\-.!`\\])", r"\1", text)
    return _restore_codes(text, codes)

# ---------------------------------------------------------------- comment handling

# A screenshot comment may name its image file, which is the only way a real
# picture reaches the page:
#     <!-- SCREENSHOT: file=runs-view.png | Clay Runs view, workspace name cropped. -->
# Without a file= (or if the file is missing from repo/assets) the slot renders as
# a visible "pending" box, so a missing image is loud at review time rather than
# silently absent.
SHOT_FILE_RE = re.compile(r"^\s*file\s*=\s*([A-Za-z0-9._-]+)\s*\|\s*(.*)$", re.DOTALL)


def comment_html(body):
    """Map an HTML comment's body to replacement HTML (or None to keep invisible)."""
    stripped = body.strip()
    up = stripped.upper()

    if up.startswith("SCREENSHOT"):
        rest = stripped.split(":", 1)[1].strip() if ":" in stripped else ""
        m = SHOT_FILE_RE.match(rest)
        if m:
            fname, caption = m.group(1), m.group(2).strip()
            if (ASSETS / fname).is_file():
                # SVGs are inlined rather than referenced: one fewer request, and
                # the figure scales from its viewBox without needing intrinsic
                # dimensions. The width/height attributes are stripped so the
                # stylesheet controls the size.
                if fname.lower().endswith(".svg"):
                    svg = (ASSETS / fname).read_text(encoding="utf-8").strip()
                    svg = re.sub(r'\s(width|height)="[^"]*"', "", svg, count=2)
                    return (f'<figure class="shot shot-inline">{svg}'
                            f"<figcaption>{html.escape(caption)}</figcaption></figure>")
                return ('<figure class="shot">'
                        f'<a href="assets/{fname}">'
                        f'<img src="assets/{fname}" loading="lazy" alt="{html.escape(caption, quote=True)}">'
                        '</a>'
                        f"<figcaption>{html.escape(caption)}</figcaption></figure>")
            print(f"  WARNING: screenshot file missing from repo/assets: {fname}")
            caption_txt = caption
        else:
            caption_txt = rest
        return ('<figure class="slot slot-screenshot">'
                '<div class="slot-frame">Screenshot pending</div>'
                f"<figcaption>{html.escape(caption_txt)}</figcaption></figure>")

    if up.startswith("GIFT-ARTIFACT SLOT"):
        return ('<p class="gift-inline"><a href="gift.html">'
                f"{html.escape(GIFT_NAV_LABEL)} &rarr;</a></p>")

    pending_prefixes = ("BO-OPEN", "BO-CLOSE", "EMBED", "ASSET", "VIDEO", "AUDIO")
    if any(up.startswith(p) for p in pending_prefixes):
        return (f'<div class="slot slot-pending">Asset pending &middot; '
                f"{html.escape(stripped)}</div>")
    return None  # pass through as an invisible comment

# ---------------------------------------------------------------- block markdown

RAW_TAGS = {"details", "summary", "figure", "figcaption", "div", "span",
            "section", "aside", "table", "thead", "tbody", "tr", "td", "th",
            "br", "hr", "img", "kbd", "mark", "sup", "sub"}


def md_to_html(md):
    """Convert the markdown subset to HTML. Line-based state machine."""
    out = []
    lines = md.split("\n")
    i = 0
    para = []
    list_stack = None  # "ul" | "ol" | None
    quote = []

    def flush_para():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def flush_list():
        nonlocal list_stack
        if list_stack:
            out.append(f"</{list_stack}>")
            list_stack = None

    def flush_quote():
        if quote:
            inner = md_to_html("\n".join(quote))
            out.append(f"<blockquote>{inner}</blockquote>")
            quote.clear()

    def flush_all():
        flush_para(); flush_list(); flush_quote()

    while i < len(lines):
        line = lines[i]

        m = re.match(r"^```(\w[\w-]*)?\s*$", line)
        if m:
            flush_all()
            lang = m.group(1) or ""
            buf = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            cls = f' class="language-{lang}"' if lang else ""
            out.append(f"<pre><code{cls}>{html.escape(chr(10).join(buf))}</code></pre>")
            continue

        if line.lstrip().startswith("<!--"):
            flush_all()
            buf = [line]
            while "-->" not in buf[-1] and i + 1 < len(lines):
                i += 1; buf.append(lines[i])
            i += 1
            whole = "\n".join(buf)
            body = re.sub(r"^\s*<!--", "", whole)
            body = re.sub(r"-->\s*$", "", body)
            repl = comment_html(body)
            out.append(repl if repl is not None else whole)
            continue

        if line.startswith(">"):
            flush_para(); flush_list()
            quote.append(re.sub(r"^> ?", "", line))
            i += 1
            continue
        elif quote:
            flush_quote()

        if not line.strip():
            flush_para(); flush_quote()
            # A blank line between two list items is normal markdown and must not
            # end the list. Closing it here restarted <ol> numbering at 1 on every
            # step. Only close when the next non-blank line is not another item of
            # the same kind.
            if list_stack:
                k = i + 1
                while k < len(lines) and not lines[k].strip():
                    k += 1
                nxt = lines[k] if k < len(lines) else ""
                same_kind = ((list_stack == "ul" and re.match(r"^\s*[-*]\s+", nxt))
                             or (list_stack == "ol" and re.match(r"^\s*\d+\.\s+", nxt)))
                if not same_kind:
                    flush_list()
            i += 1
            continue

        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            flush_all()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2).strip())}</h{level}>")
            i += 1
            continue

        # pipe table: a header row, a | --- | separator, then body rows.
        # v1's builder had no table support and silently flattened tables into a
        # paragraph of pipes; lesson 4 uses one, so it is handled here.
        if (line.lstrip().startswith("|")
                and i + 1 < len(lines)
                and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1])):
            flush_all()

            def split_row(row):
                return [c.strip() for c in row.strip().strip("|").split("|")]

            head = split_row(line)
            i += 2  # header + separator
            body_rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                body_rows.append(split_row(lines[i]))
                i += 1
            out.append('<div class="table-wrap"><table><thead><tr>'
                       + "".join(f"<th>{inline(c)}</th>" for c in head)
                       + "</tr></thead><tbody>")
            for row in body_rows:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
            out.append("</tbody></table></div>")
            continue

        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        n = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m or n:
            flush_para(); flush_quote()
            kind = "ul" if m else "ol"
            if list_stack != kind:
                flush_list()
                out.append(f"<{kind}>")
                list_stack = kind
            item = (m or n).group(1)
            # Absorb everything indented under this item, blank lines included, and
            # render it as markdown inside the <li>. Markdown lets a list item carry
            # whole paragraphs and quotes; the old parser folded them into one flat
            # line, which left indented blockquotes showing a literal ">".
            cont = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if not nxt.strip():
                    cont.append("")
                    j += 1
                    continue
                if re.match(r"^\s{2,}\S", nxt):
                    cont.append(nxt)
                    j += 1
                    continue
                break
            while cont and not cont[-1].strip():
                cont.pop()
            body = inline(item)
            if cont:
                pad = min(len(c) - len(c.lstrip()) for c in cont if c.strip())
                body += "\n" + md_to_html(
                    "\n".join(c[pad:] if c.strip() else "" for c in cont))
                i = j - 1
            out.append(f"<li>{body}</li>")
            i += 1
            continue
        flush_list()

        m = re.match(r"^\s*</?([a-zA-Z][a-zA-Z0-9-]*)[^>]*>", line)
        if m and m.group(1).lower() in RAW_TAGS and re.search(r">\s*$", line):
            flush_all()
            out.append(line.strip())
            i += 1
            continue

        para.append(line.strip())
        i += 1

    flush_all()
    return "\n".join(out)

# ---------------------------------------------------------------- quiz extraction

QUIZ_RE = re.compile(r"```quiz-json\s*\n(.*?)\n```", re.DOTALL)
# Substituted for the fence so the quiz lands where the author put it. v1's
# builder appended the quiz after the whole article, which pushed it below
# "Fine print" on every lesson and inverted the intended reading order.
QUIZ_MARKER = "<!--QUIZ-ROOT-->"


def extract_quiz(md, name):
    m = QUIZ_RE.search(md)
    if not m:
        print(f"  WARNING: {name}: no quiz-json block found.")
        return md, None
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        print(f"  ERROR: {name}: quiz-json failed to parse ({e}); quiz dropped.")
        return QUIZ_RE.sub("", md), None
    for k, item in enumerate(data.get("items", [])):
        n_correct = sum(1 for o in item.get("options", []) if o.get("correct"))
        if n_correct != 1:
            print(f"  ERROR: {name}: quiz item {k + 1} has {n_correct} correct options "
                  "(engine expects exactly 1).")
    return QUIZ_RE.sub(QUIZ_MARKER, md, count=1), data

# ---------------------------------------------------------------- page templates

def page(title, body, extra_head="", body_class="", nav=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="style.css">
{extra_head}</head>
<body class="{body_class}">
{nav}{body}
<script src="quiz.js"></script>
<script src="interactions.js"></script>
</body>
</html>
"""


def top_nav(current=""):
    """Sticky top bar: course title (links home) + lesson pills + the gift page.

    quiz.js marks pills with a check from its localStorage keys; the current
    page's pill is filled at build time via .pill-current."""
    pills = []
    for n in range(N_LESSONS):
        cls = "nav-pill" + (" pill-current" if current == str(n) else "")
        cur = ' aria-current="page"' if current == str(n) else ""
        pills.append(f'<a class="{cls}" data-lesson="{n}" href="lesson-{n}.html" '
                     f'title="Lesson {n}"{cur}>{n}</a>')
    if (COURSE / GIFT_PAGE).is_file():
        cls = "nav-pill nav-pill-text" + (" pill-current" if current == "gift" else "")
        cur = ' aria-current="page"' if current == "gift" else ""
        pills.append(f'<a class="{cls}" href="gift.html"{cur}>{html.escape(GIFT_NAV_LABEL)}</a>')
    return (f'<nav class="top-nav"><div class="top-nav-inner">'
            f'<a class="brand" href="index.html">{html.escape(SITE_TITLE)}</a>'
            f'<div class="nav-pills" aria-label="Lessons">{"".join(pills)}</div>'
            f"</div></nav>\n")


def feedback_block(is_last_lesson=False):
    """Footer feedback. The last lesson also carries the end-of-course survey,
    which is a separate form from the report-a-problem link."""
    block = f"""<div class="feedback">
<a class="feedback-link" href="{FEEDBACK_URL}" target="_blank" rel="noopener">Suggest a fix or tell me what broke &rarr;</a>
</div>"""
    if is_last_lesson:
        block += f"""
<div class="feedback feedback-survey">
<a class="survey-link" href="{SURVEY_URL}" target="_blank" rel="noopener">Finished the course? Tell me how it went &rarr;</a>
</div>"""
    return block


def footer_html(is_last_lesson=False):
    return f"""<footer class="site-footer">
<p class="banner">{html.escape(BANNER)}</p>
{feedback_block(is_last_lesson)}
<p><a href="colophon.html">How this course was built</a> &middot; <a href="index.html">Course home</a></p>
</footer>"""


def lesson_nav(n):
    prev_a = (f'<a class="nav-prev" href="lesson-{n - 1}.html">&larr; Lesson {n - 1}</a>'
              if n > 0 else '<a class="nav-prev" href="index.html">&larr; Course home</a>')
    if n < N_LESSONS - 1:
        next_a = f'<a class="nav-next" href="lesson-{n + 1}.html">Lesson {n + 1} &rarr;</a>'
    elif (COURSE / GIFT_PAGE).is_file():
        next_a = f'<a class="nav-next" href="gift.html">{html.escape(GIFT_NAV_LABEL)} &rarr;</a>'
    else:
        next_a = '<a class="nav-next" href="index.html">Course home &rarr;</a>'
    return f'<nav class="lesson-nav">{prev_a}{next_a}</nav>'

# ---------------------------------------------------------------- build steps

def parse_lesson_meta(md, name):
    title_m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
    time_m = re.search(r"^\*\*Time:\*\*\s*(.+?)\s*$", md, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else name
    time = time_m.group(1).strip() if time_m else ""
    return title, time


def build_lesson(n, md, titles, times):
    name = f"lesson-{n}"
    body_md, quiz = extract_quiz(md, name)

    # strip the h1 + Time line; they render in the page header instead
    body_md = re.sub(r"^#\s+.+\n+", "", body_md, count=1)
    body_md = re.sub(r"^\*\*Time:\*\*.*\n+", "", body_md, count=1, flags=re.MULTILINE)

    content = md_to_html(body_md)

    quiz_tail = ""
    if quiz:
        payload = json.dumps(quiz).replace("</", "<\\/")
        content = content.replace(
            QUIZ_MARKER,
            f'<div class="quiz-section" id="quiz-root" data-lesson="{n}">'
            f'<noscript><p class="quiz-noscript">These questions need JavaScript to run. '
            f'Nothing is scored, so if it is switched off you can safely read on.</p></noscript>'
            f'</div>', 1)
        quiz_tail = (f'<script type="application/json" id="quiz-data">{payload}</script>')
    else:
        content = content.replace(QUIZ_MARKER, "", 1)

    time_badge = (f' <span class="badge badge-time">{html.escape(times[n])}</span>'
                  if times[n] else "")
    body = f"""<main class="lesson">
<header class="lesson-header">
<p class="lesson-badges"><span class="badge badge-num">Lesson {n}</span>{time_badge}</p>
<h1>{inline(titles[n])}</h1>
</header>
<article class="lesson-body">
{content}
</article>
{lesson_nav(n)}
{footer_html(n == N_LESSONS - 1)}
</main>{quiz_tail}"""
    lesson_title = (titles[n] if titles[n].lower().startswith("lesson")
                    else f"Lesson {n} — {titles[n]}")
    (SITE / f"{name}.html").write_text(
        page(f"{lesson_title} · {SITE_TITLE}", body, nav=top_nav(str(n))), encoding="utf-8")


def build_gift():
    src = COURSE / GIFT_PAGE
    if not src.is_file():
        print(f"  NOTE: course/{GIFT_PAGE} missing - gift page skipped.")
        return
    md = src.read_text(encoding="utf-8")
    title_m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else GIFT_NAV_LABEL
    body_md = re.sub(r"^#\s+.+\n+", "", md, count=1)
    content = md_to_html(body_md)

    links = []
    for fname, label in GIFT_FILES:
        f = REPO / fname
        if not f.is_file():
            print(f"  WARNING: gift artifact missing: {fname}")
            continue
        shutil.copyfile(f, SITE / fname)
        links.append(f'<a class="gift-download" href="{fname}" download>{html.escape(label)}</a>')
    downloads = (f'<p class="download">{" ".join(links)}<br>'
                 f'<small class="license-line">{html.escape(GIFT_LICENSE)}</small></p>'
                 if links else "")

    body = f"""<main class="lesson">
<header class="lesson-header">
<p class="lesson-badges"><span class="badge badge-num">{html.escape(GIFT_BADGE)}</span></p>
<h1>{inline(title)}</h1>
{downloads}
</header>
<article class="lesson-body">
{content}
</article>
{footer_html()}
</main>"""
    (SITE / "gift.html").write_text(
        page(f"{title} \u00b7 {SITE_TITLE}", body, nav=top_nav("gift")), encoding="utf-8")
    print(f"  built docs/gift.html (+ {len(links)} artifact(s))")


def build_colophon():
    src = COURSE / "colophon.md"
    if src.is_file():
        md = src.read_text(encoding="utf-8")
        title_m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
        title = title_m.group(1).strip() if title_m else "How this course was built"
        body_md = re.sub(r"^#\s+.+\n+", "", md, count=1)
        content = md_to_html(body_md)
    else:
        title = "How this course was built"
        content = "<p>Colophon pending.</p>"
        print("  NOTE: course/colophon.md missing — placeholder used.")
    body = f"""<main class="lesson">
<header class="lesson-header">
<h1>{inline(title)}</h1>
</header>
<article class="lesson-body">
{content}
</article>
{footer_html()}
</main>"""
    (SITE / "colophon.html").write_text(
        page(f"{title} · {SITE_TITLE}", body, nav=top_nav("colophon")), encoding="utf-8")


def build_index(titles, times):
    items = []
    for n in range(N_LESSONS):
        t = (f'<span class="badge badge-time">{html.escape(times[n])}</span>'
             if times[n] else "")
        items.append(f"""<li class="lesson-card">
<a href="lesson-{n}.html">
<span class="badge badge-num">Lesson {n}</span>
<span class="card-title">{inline(titles[n])}</span>
{t}
<span class="progress-chip" data-lesson="{n}"></span>
</a>
</li>""")
    mins = 0
    for t in times:
        m = re.match(r"(\d+)", t or "")
        if m:
            mins += int(m.group(1))
    total = (f'<p class="total-time">Six lessons, about {mins} minutes of reading. '
             f'Setting up Claude Code and Clay for the first time is on top of that.</p>'
             if mins else "")
    gift_html = ""
    if (COURSE / GIFT_PAGE).is_file():
        gift_html = (f'<section class="landing-extras"><p>'
                     f'<a class="sop-link" href="gift.html">{html.escape(GIFT_NAV_LABEL)}</a> — '
                     f"{html.escape(GIFT_BLURB)}</p></section>")
    prereq_items = "".join(f"<li>{html.escape(t)}</li>" for t in PREREQS)
    prereqs = (f'<section class="prereqs"><h2>{html.escape(PREREQS_TITLE)}</h2>'
               f"<ul>{prereq_items}</ul></section>")
    body = f"""<main class="landing">
<header class="landing-header">
<h1>{html.escape(SITE_TITLE)}</h1>
<p class="subtitle">{html.escape(TAGLINE)}</p>
<p class="byline">By {html.escape(BYLINE)}</p>
<p class="banner">{html.escape(BANNER)}</p>
{total}
{prereqs}
<div class="course-progress" id="course-progress" hidden>
<span class="course-progress-label"></span>
<span class="course-progress-track"><span class="course-progress-fill"></span></span>
</div>
</header>
<ol class="lesson-list" start="0">
{chr(10).join(items)}
</ol>
{gift_html}
{footer_html()}
</main>"""
    (SITE / "index.html").write_text(
        page(SITE_TITLE, body, body_class="home", nav=top_nav("home")), encoding="utf-8")


def build_static():
    """Copy the hand-written CSS/JS into the generated site."""
    if not STATIC.is_dir():
        print("  WARNING: repo/static missing — pages reference style.css and quiz.js.")
        return
    for name in ("style.css", "quiz.js", "interactions.js"):
        src = STATIC / name
        if src.is_file():
            shutil.copy2(src, SITE / name)
        else:
            print(f"  WARNING: static/{name} missing — pages reference it.")
    print("  copied static/ → docs/")


def build_assets():
    if not ASSETS.is_dir():
        print("  NOTE: repo/assets missing — screenshots will not resolve.")
        return
    dst = SITE / "assets"
    dst.mkdir(exist_ok=True)
    count = 0
    for f in ASSETS.iterdir():
        if f.is_file():
            shutil.copy2(f, dst / f.name)
            count += 1
    print(f"  copied {count} assets → docs/assets/")


def main():
    SITE.mkdir(exist_ok=True)
    titles, times, mds = [], [], []
    missing = []
    for n in range(N_LESSONS):
        p = COURSE / f"lesson-{n}.md"
        if not p.exists():
            missing.append(p.name)
            titles.append(f"Lesson {n}"); times.append(""); mds.append(None)
            continue
        md = p.read_text(encoding="utf-8")
        t, tm = parse_lesson_meta(md, f"Lesson {n}")
        titles.append(t); times.append(tm); mds.append(md)
    if missing:
        print(f"  WARNING: missing lesson files: {', '.join(missing)} (pages skipped)")

    for n in range(N_LESSONS):
        if mds[n] is not None:
            build_lesson(n, mds[n], titles, times)
            print(f"  built docs/lesson-{n}.html  ({times[n] or 'no time'})")
    build_gift()
    build_colophon(); print("  built docs/colophon.html")
    build_index(titles, times); print("  built docs/index.html")
    build_assets()
    build_static()
    print("done.")


if __name__ == "__main__":
    sys.exit(main())

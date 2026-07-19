/* Quiz engine + landing-page progress. Vanilla JS, no dependencies.
   Data source: <script type="application/json" id="quiz-data"> embedded per lesson page.
   Storage: localStorage key "clay-course-quiz-<lesson>" -> {"score":n,"total":n,"ts":ms}. */
(function () {
  "use strict";

  var STORE_PREFIX = "clay-course-quiz-";

  function readResult(lesson) {
    try {
      var raw = localStorage.getItem(STORE_PREFIX + lesson);
      return raw ? JSON.parse(raw) : null;
    } catch (e) { return null; }
  }

  function saveResult(lesson, score, total) {
    try {
      localStorage.setItem(STORE_PREFIX + lesson,
        JSON.stringify({ score: score, total: total, ts: Date.now() }));
    } catch (e) { /* private mode etc. — quiz still works, just not remembered */ }
    try {
      document.dispatchEvent(new CustomEvent("quiz-complete",
        { detail: { lesson: lesson, score: score, total: total } }));
    } catch (e) { /* older browsers: popups simply don't fire */ }
  }

  /* ---------------------------------------------------------- quiz rendering */

  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  }

  function renderQuiz(root, data) {
    var lesson = root.getAttribute("data-lesson");
    var items = data.items || [];
    var answered = 0;
    var score = 0;

    var prior = readResult(lesson);
    if (prior && prior.total) {
      root.appendChild(el("p", "quiz-prior",
        "Previously completed: " + prior.score + "/" + prior.total + ". Answer again any time."));
    }

    items.forEach(function (item, idx) {
      var box = el("section", "quiz-item");
      box.appendChild(el("h3", "quiz-q", (idx + 1) + ". " + item.q));
      var list = el("div", "quiz-options");
      var done = false;

      (item.options || []).forEach(function (opt) {
        var wrap = el("div", "quiz-option");
        var btn = el("button", "quiz-choice", opt.text);
        btn.type = "button";
        var why = el("p", "quiz-why", opt.why || "");
        why.hidden = true;
        wrap.appendChild(btn);
        wrap.appendChild(why);
        list.appendChild(wrap);

        btn.addEventListener("click", function () {
          if (done) return;
          done = true;
          answered += 1;
          if (opt.correct) score += 1;
          box.classList.add(opt.correct ? "was-correct" : "was-incorrect");
          box.appendChild(el("p", "quiz-verdict " + (opt.correct ? "ok" : "bad"),
            opt.correct ? "Correct." : "Not this one."));
          // reveal every option's why, mark states, freeze buttons
          Array.prototype.forEach.call(list.children, function (w, i) {
            var o = item.options[i];
            var b = w.querySelector("button");
            b.disabled = true;
            w.classList.add(o.correct ? "opt-correct" : "opt-incorrect");
            if (b === btn) w.classList.add("opt-chosen");
            w.querySelector(".quiz-why").hidden = false;
          });
          if (answered === items.length) finish();
        });
      });

      box.appendChild(list);
      root.appendChild(box);
    });

    function finish() {
      saveResult(lesson, score, items.length);
      var summary = el("div", "quiz-score");
      summary.appendChild(el("p", "quiz-score-line",
        "Lesson " + lesson + " check: " + score + "/" + items.length + " correct."));
      var note = score === items.length
        ? "All grounded. On to the next lesson."
        : "Reread the whys on the ones you missed — each wrong option is a real failure mode.";
      summary.appendChild(el("p", "quiz-score-note", note));
      root.appendChild(summary);
      summary.scrollIntoView({ behavior: "smooth", block: "nearest" });
      renderProgress(); // in case the chip layout is also on this page
    }
  }

  /* ------------------------------------------------- landing-page progress */

  function renderProgress() {
    // top-nav pills: subtle check on lessons whose check is completed
    var pills = document.querySelectorAll(".nav-pill[data-lesson]");
    Array.prototype.forEach.call(pills, function (pill) {
      var res = readResult(pill.getAttribute("data-lesson"));
      if (res && res.total) {
        pill.classList.add("pill-done");
        pill.title = "Lesson " + pill.getAttribute("data-lesson") +
          " — completed " + res.score + "/" + res.total;
      } else {
        pill.classList.remove("pill-done");
      }
    });

    var chips = document.querySelectorAll(".progress-chip[data-lesson]");
    var completed = 0;
    var totalTracked = chips.length;
    Array.prototype.forEach.call(chips, function (chip) {
      var res = readResult(chip.getAttribute("data-lesson"));
      if (res && res.total) {
        completed += 1;
        chip.textContent = res.score + "/" + res.total;
        chip.classList.add(res.score === res.total ? "chip-perfect" : "chip-done");
        chip.title = "Completed " + new Date(res.ts).toLocaleDateString();
      } else {
        chip.textContent = "";
        chip.classList.remove("chip-done", "chip-perfect");
      }
    });

    var bar = document.getElementById("course-progress");
    if (bar && totalTracked) {
      if (completed > 0) {
        bar.hidden = false;
        bar.querySelector(".course-progress-label").textContent =
          completed + " of " + totalTracked + " lesson checks done";
        bar.querySelector(".course-progress-fill").style.width =
          Math.round((completed / totalTracked) * 100) + "%";
      } else {
        bar.hidden = true;
      }
    }
  }

  /* -------------------------------------------------------------- boot */

  function boot() {
    var root = document.getElementById("quiz-root");
    var dataNode = document.getElementById("quiz-data");
    if (root && dataNode) {
      try {
        renderQuiz(root, JSON.parse(dataNode.textContent));
      } catch (e) {
        root.appendChild(el("p", "quiz-error", "Quiz data failed to load."));
      }
    }
    renderProgress();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  // Shared hooks for interactions.js (lesson-2 widget stores its result under the
  // same localStorage key scheme, then asks the progress UI to repaint).
  window.clayCourseProgressRefresh = renderProgress;
  window.clayCourseSaveResult = saveResult;
  window.clayCourseReadResult = readResult;
})();

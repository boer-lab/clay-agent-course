/* Site interactions for "Using Clay in Claude Code" (v2).

   v1 shipped three bespoke widgets here (the "spot the lie" transcript, the
   gate-placement exercise, and a flashcard deck). None of them survive into v2:
   the course now teaches a real build rather than a discipline, and each lesson
   carries its own quiz via quiz.js. What remains is the feedback path.

   Feedback is a plain link to the author's Google Form, so it needs no JS to
   work. This file only adds the two mid-course nudges (end of lessons 2 and 4,
   once each per browser) and the stronger ask on the final lesson.

   quiz.js loads first and dispatches the "quiz-complete" event this listens for. */
(function () {
  "use strict";

  function onReady(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  var m = location.pathname.match(/lesson-(\d)\.html$/);
  var here = m ? m[1] : null;
  if (!here) return;

  function shown(l) {
    try { return localStorage.getItem("clay-course-fbpop-" + l); } catch (e) { return "1"; }
  }
  function mark(l) {
    try { localStorage.setItem("clay-course-fbpop-" + l, "1"); } catch (e) {}
  }

  function showPopup(lesson) {
    if (shown(lesson)) return;
    mark(lesson);
    var card = document.createElement("div");
    card.className = "fb-popup";
    card.setAttribute("role", "dialog");
    card.setAttribute("aria-label", "Feedback");
    card.innerHTML =
      '<p>Anything confusing or broken so far?</p>' +
      '<p class="fb-popup-actions">' +
      '<button type="button" class="btn-accent" id="fbpop-go">Tell me</button>' +
      '<button type="button" id="fbpop-close">Not now</button></p>';
    document.body.appendChild(card);
    card.querySelector("#fbpop-go").addEventListener("click", function () {
      var link = document.querySelector(".feedback-link");
      if (link && link.href) window.open(link.href, "_blank", "noopener");
      card.remove();
    });
    card.querySelector("#fbpop-close").addEventListener("click", function () {
      card.remove();
    });
    setTimeout(function () { if (card.parentNode) card.remove(); }, 30000);
  }

  if (here === "2" || here === "4") {
    document.addEventListener("quiz-complete", function (e) {
      if (e.detail && String(e.detail.lesson) === here) showPopup(here);
    });
    onReady(function () {
      var foot = document.querySelector(".site-footer");
      if (foot && "IntersectionObserver" in window) {
        var io = new IntersectionObserver(function (entries) {
          entries.forEach(function (en) {
            if (en.isIntersecting) { showPopup(here); io.disconnect(); }
          });
        }, { threshold: 0.2 });
        io.observe(foot);
      }
    });
  }

  if (here === "5") {
    onReady(function () {
      var fb = document.querySelector(".feedback");
      if (!fb) return;
      fb.classList.add("feedback-final");
      var link = fb.querySelector(".feedback-link");
      if (link) link.textContent = "Before you go — what should I fix? →";
    });
  }
})();

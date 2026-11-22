# Mechanics of Materials Atlas

Condensed, single-page study guide for a 14-chapter Mechanics of Materials course

- `index.html`: the whole site. Open it directly in a browser (no build step).
  KaTeX and Google Fonts load from CDNs.
- Each chapter is its own page view (hash routing: `#ch6`, `#s6.4`, `#fig-6-24`), with no reloads.
  Sidebar shows the current chapter's sections; `[` / `]` switch chapters; search spans all chapters.
- The last page, **Equation sheet** (`#eq`), lists only the critical (`=!`) equations, grouped by chapter and section; it prints cleanly.
- Each chapter ends with a **Chapter summary** card.
- Every section card opens with one key figure above *Key concepts*: either a textbook figure
  (click for the full figure) or a custom SVG diagram that follows the chapter accent and theme.
- `figures/card/`: cropped single-panel versions of busy figures, used only on the section cards.
- `tools/section_figs.py`: source for the custom SVG section figures. Run `python tools/section_figs.py`
  to regenerate the `<template id="sf-…">` block in `index.html`.
- `figures/`: key textbook figures (`fig<ch>-<n>.webp`), cropped from the scanned PDF.
  Clicking a **Fig.** pill in a bullet opens it in a pop-up viewer (←/→ to step through, Esc to close).
  Deep link: `index.html#fig-6-24`.

## Books
The site holds three separate books, switched from the top bar (no reload):
- **Mechanics of Materials** (Hibbeler, 9th ed.): data block `id="data"`, figures in `figures/`, hashes `#ch6`, `#s6.4`, `#eq`.
- **GD&T** (Krulikowski, *Fundamentals of GD&T*, 3rd ed., ASME Y14.5-2009), clearly marked as a separate topic:
  data block `id="data-gdt"`, figures in `figures/gdt/`, hashes `#gdt`, `#g-ch9`, `#g-s9.2`, `#g-eq`
  (Symbol & formula sheet). Chapter lines take an optional 5th field naming a symbol used as chapter art.
  Extra inline markup: `{sym position}`, `{mod M}`, `{datum A}`, `{fcf position|dia 0.4 (M)|A|B|C}`.
  Note: the source PDF is missing book pages 353–362 (most of ch. 26); those sections were written from the
  chapter summary + Y14.5 and use custom SVG figures (`sf-g-26-*` in `tools/section_figs.py`).
- **Tactile Sensing** (11 chapters, 46 sections), built around US patent application publication 2026/0310299 A1
  (Tesla, *Three-Dimensional Soft Compliant Array Tactile Sensor with Multi-Modal Sensing and Scalable Manufacturing
  Methods*) and modeled on the Mechanics of Materials book: data block `id="data-ts"`, quiz block `id="quiz-ts"`,
  hashes `#ts`, `#t-ch4`, `#t-s4.4`, `#t-eq` (Equation sheet), `#t-quiz4`, `#t-mix`, `#t-interview4.2`.
  Chapters: the design problem, materials selection, contact mechanics, elastomer mechanics, transduction,
  viscoelasticity, bending of laminates, thermoforming, interfaces and failure, manufacturing process selection,
  integration. Accent groups: `tfound`, `tmech`, `tsense`, `tform`, `tbuild`.
  - Sourcing: bullets that start **In the patent** paraphrase the patent. The patent names materials and processes
    but contains no equations or property values, so the theory, equations, worked examples and "typical" numbers
    are standard mechanics background written for this site.
  - Figures: every section card uses a custom SVG (`sf-t-<ch>-<sec>`) and every chapter header an icon
    (`art-t-<ch>`), both defined in `tools/tactile_figs.py` and injected by `python tools/section_figs.py`.
    There are no scanned figures for this book.
  - Interviewer: 24 worked examples in `examples-tactile.js` (`window.EXAMPLES_TS`, same fields as `examples.js`),
    with figures in `figures/tactile/ex/` rendered from the section SVGs by `python tools/tactile_ex_figs.py`
    (needs `rsvg-convert`).

## Editing content
All notes live in the `<script type="text/plain" id="data">` block in `index.html`:

```
# n | Chapter title | accent group (fund/load/bend/trans/design) | summary
## n.m | Section title | *        (trailing * = advanced section)
- **Label.** concept bullet (bold lead-in), inline math in $...$, figure link as {fig 6-24}
= LaTeX display equation || optional caption
=! LaTeX display equation || caption   critical: also listed on the Equation sheet
> chapter-summary bullet (lines right after the # chapter line)
! fig 6-24 || caption      key figure (textbook; add `crop` to use figures/card/)
! svg 6-1 || caption       key figure (custom SVG template sf-6-1)
```

## Chapter quizzes and study tutor (Gemini)
- Each chapter ends with a **Chapter quiz** button (`#quiz6`, `#g-quiz9`, `#t-quiz4`): 8 short questions on the basics, including quick calculations.
  Type an answer and Gemini grades it against the reference answer (correct / partly / not quite, with feedback).
  "Show answer" works without a key; "✦ 5 more questions" asks Gemini to write new ones from the chapter notes.
- **Mixed quiz** (`#mix`, `#g-mix`, `#t-mix`; linked from every chapter page, each chapter quiz, and the sidebar under Reference)
  covers any set of chapters. The chapter picker starts with every chapter up to the one you were last studying
  (e.g. coming from Chapter 6 selects 1–6); "All" / "None" shortcuts and per-chapter checkboxes change it.
  Choose how many questions (5–30 or all): they're drawn evenly from each chosen chapter's bank (plus any
  Gemini questions already added to those chapter quizzes), shuffled, and tagged with their chapter.
  "✦ 5 more questions" writes new ones spread across the chosen chapters.
- **Interviewer** (`#interview`, `#interview6`, `#interview6.3`, and `#t-interview…` for Tactile Sensing; sidebar under
  Reference and an "Interview practice" card on each chapter page of a book that has examples; it works on the
  examples of the book you opened it from) is a full-screen mock interview on the
  book's worked **Example** problems (all 176, chapters 1–14). Pick a chapter and an example, or **Shuffle**
  (unfinished ones first; "All chapters" shuffles across the book). The problem statement and its initial figure
  are shown (only the given-data panel, never the solution panels). Gemini then asks you to explain the set-up
  at a high level and drills down one question at a time to the final numbers, without hints or leading
  questions; as soon as something you say is wrong it stops, says so and explains why, then lets you continue.
  It ends with a short debrief. The right half is a **scratchpad** (pen, eraser, undo, pan/zoom; from the
  mech-design-interview-quiz repo): when it has changed, it's included with your next message as an image and
  the interviewer reads it as part of your answer. **Show solution** gives up and shows the book's solution.
  Conversations and scratchpads are saved per example in localStorage (**Restart** clears the conversation).
  - Data: `examples.js` (`window.EXAMPLES`: id, title, statement `q`, `figs`, `figDesc`, examiner-only `sol`,
    `answers`), figures in `figures/ex/ex<ch>-<n>.webp`. The figure image is sent to Gemini when the site is
    served over http(s) (e.g. GitHub Pages); opened from `file://` the browser blocks reading it, so the
    interviewer relies on the written figure description instead.
- **Ask tutor** (bottom-right) opens a chat that is given the notes of the chapter you have open.
- Both use your own Gemini API key, entered in the tutor's key settings. It is stored only in your browser's localStorage
  and sent directly to `generativelanguage.googleapis.com`; it is never committed or sent anywhere else. The model list
  comes from your key (newest Flash model selected by default, changeable in settings). Quiz progress is also kept in localStorage.
- Quiz data lives in `<script type="text/plain" id="quiz">` (and `id="quiz-gdt"`, `id="quiz-ts"`): `@ 6` starts chapter 6, then
  `? question || reference answer` per line.


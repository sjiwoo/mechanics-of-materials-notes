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
The site holds two separate textbooks, switched from the top bar (no reload):
- **Mechanics of Materials** (Hibbeler, 9th ed.): data block `id="data"`, figures in `figures/`, hashes `#ch6`, `#s6.4`, `#eq`.
- **GD&T** (Krulikowski, *Fundamentals of GD&T*, 3rd ed., ASME Y14.5-2009), clearly marked as a separate topic:
  data block `id="data-gdt"`, figures in `figures/gdt/`, hashes `#gdt`, `#g-ch9`, `#g-s9.2`, `#g-eq`
  (Symbol & formula sheet). Chapter lines take an optional 5th field naming a symbol used as chapter art.
  Extra inline markup: `{sym position}`, `{mod M}`, `{datum A}`, `{fcf position|dia 0.4 (M)|A|B|C}`.
  Note: the source PDF is missing book pages 353–362 (most of ch. 26); those sections were written from the
  chapter summary + Y14.5 and use custom SVG figures (`sf-g-26-*` in `tools/section_figs.py`).

- **Materials** (Ashby, Shercliff & Cebon, *Materials: Engineering, Science, Processing and Design*, 4th ed.),
  chapters 4–15 (stiffness, strength, fracture, fatigue, friction and wear, heat, creep, durability, electrical):
  data block `id="data-mat"`, quiz block `id="quiz-mat"`, chapter icons `<template id="art-m-N">`, figures in
  `figures/mat/` (book figure numbers), hashes `#mat`, `#m-ch5`, `#m-s5.2`, `#m-eq` (Formula & index sheet),
  `#m-quiz5`, `#m-mix`. These blocks sit between the `<!-- MAT:BEGIN -->` / `<!-- MAT:END -->` markers.
- **Soft Robotics** (course 24-673, Prof. C. Majidi, 12 lectures): notes condensed from the lecture slides and their
  embedded videos (key frames + speech transcripts; video frames are figures `fig<lecture>-<100+slide>`), one
  "chapter" per lecture with topic sections, key slide figures (`figures/sr/fig<lecture>-<slide>.webp`), equation
  sheet, quizzes and interview problems. Data block `id="data-sr"`, quiz `id="quiz-sr"`, icons `art-r-N`, between
  the `<!-- SR:BEGIN -->` / `<!-- SR:END -->` markers; hashes `#sr`, `#r-ch3`, `#r-s3.2`, `#r-eq`, `#r-quiz3`, `#r-mix`.

- **Tactile Sensing** (11 chapters, 46 sections), built around US patent application publication 2026/0310299 A1
  (Tesla, *Three-Dimensional Soft Compliant Array Tactile Sensor with Multi-Modal Sensing and Scalable Manufacturing
  Methods*) and modeled on the Mechanics of Materials book: data block `id="data-ts"`, quiz block `id="quiz-ts"`,
  hashes `#ts`, `#t-ch4`, `#t-s4.4`, `#t-eq` (Equation sheet), `#t-quiz4`, `#t-mix`, `#t-interview4.2`.
  Chapters: the design problem, materials selection, contact mechanics, elastomer mechanics, transduction,
  viscoelasticity, bending of laminates, thermoforming, interfaces and failure, manufacturing process selection,
  integration. Accent groups: `tfound`, `tmech`, `tsense`, `tform`, `tbuild`.
  - Sourcing: bullets that start **In the patent** paraphrase the patent. The patent names materials and processes
    but contains no equations or property values, so the theory, equations, problems and "typical" numbers are
    standard mechanics background written for this site.
  - Figures: every section card uses a custom SVG (`sf-t-<ch>-<sec>`) and every chapter header an icon
    (`art-t-<ch>`), both defined in `tools/tactile_figs.py` and injected by `python tools/section_figs.py`.
  - Interviewer: 24 problems in `examples-ts.js` (`window.EXAMPLES_BY.ts`), with figures in `figures/tactile/ex/`
    rendered from the section SVGs by `python tools/tactile_ex_figs.py` (needs `rsvg-convert`).
- **Physics for Mechanics** (9 chapters, 42 sections): background physics the other books do not cover, written
  for this site from standard university physics (no single textbook): forces and motion, work/energy/power,
  momentum and collisions, rotation, oscillations, damping and resonance, waves and modes, fluids, heat transfer.
  Data block `id="data-ph"`, quiz block `id="quiz-ph"`, hashes `#ph`, `#ph-ch6`, `#ph-s6.2`, `#ph-eq`,
  `#ph-quiz6`, `#ph-mix`, `#ph-interview6.2` (the prefix is `ph-` because Polymers uses `p-`).
  Accent groups: `pmot`, `pcons`, `prot`, `pvib`, `pflu`, `pheat`.
  - Figures: a custom SVG on every section (`sf-ph-<ch>-<sec>`) and an icon per chapter (`art-ph-<ch>`), defined
    in `tools/physics_figs.py` and injected by `python tools/section_figs.py`.
  - Interviewer: 27 problems (3 per chapter) in `examples-ph.js` (`window.EXAMPLES_BY.ph`), figures in
    `figures/physics/ex/` rendered by `python tools/physics_ex_figs.py` (needs `rsvg-convert`).
  - Not in the Flashcards deck.
- **Polymers** (course 27-577/777 *Advanced Polymer Science and Engineering*, Prof. M. R. Bockstaller, Fall 2021): replicates
  the syllabus. The 11 chapters are the syllabus's 11 topics (introduction, ideal chain models, amorphous, semicrystalline and
  liquid-crystalline polymers, network deformation, viscoelasticity, processing, anisotropy, blend thermodynamics, homopolymer
  blends), built from the course lecture notes and deepened with the primary text (Gedde, *Polymer Physics*) and the secondary
  text (McCrum, Buckley & Bucknall, *Principles of Polymer Engineering*, 2nd ed.). The landing page summarizes the syllabus
  (lecturer, texts, assessment, paper project, exam coverage). Every section ends with a **Sources** bullet (lecture date and
  textbook §; "general background" marks anything from neither). Data block `id="data-poly"`, quiz `id="quiz-poly"`, icons
  `art-p-N`, between the `<!-- POLY:BEGIN -->` / `<!-- POLY:END -->` markers; figures in `figures/poly/`; hashes `#poly`,
  `#p-ch3`, `#p-s3.2`, `#p-eq`, `#p-quiz3`, `#p-mix`, `#p-interview3.2`. Interview problems (85) in `examples-poly.js`: Gedde
  exercises (checked against Gedde ch. 13 solutions), McCrum problems (checked against the book's answers) and course-style
  problems; each record has a `src` field naming its origin.
- **Flashcards** (`#cards`; sidebar under Reference in every book, and in the chapter picker): one deck of the 50 most important
  equations across all books (Mechanics of Materials 14, Polymers 10, Materials 9, Tactile Sensing 7, Soft Robotics 6,
  GD&T 4). Each card shows a prompt; under it, type the equation (any notation: `sigma = N/A`, `τ = Tρ/J`, LaTeX) and/or
  write it on the **✎ Scratchpad** (same pad as the interviewer), then **Check answer**: Gemini grades it against the card's
  equation (equivalent and rearranged forms count; correct / partly right / not quite, with feedback), flips the card and
  marks it known or "Again". Answers and sketches are kept per card while you move around the deck. Or click / Space to flip. Mark
  **Got it** / **Again** (keys 2 / 1, arrows to move); progress is kept in localStorage. Filter by book, shuffle, or review
  only the missed cards; "All 50 equations at a glance" lists the whole deck. The deck is the `<script type="text/plain"
  id="cards">` block: one card per line, `book key | section | prompt || LaTeX || note`.
- On phones (≤ 560 px) the book switcher sits on its own row under the search box and chapter picker, with compact labels.

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
- Each chapter ends with a **Chapter quiz** button (`#quiz6`, `#g-quiz9`): 8 short questions on the basics, including quick calculations.
  Type an answer and Gemini grades it against the reference answer (correct / partly / not quite, with feedback).
  "Show answer" works without a key; "✦ 5 more questions" asks Gemini to write new ones from the chapter notes.
- **Mixed quiz** (`#mix`, `#g-mix`; linked from every chapter page, each chapter quiz, and the sidebar under Reference)
  covers any set of chapters. The chapter picker starts with every chapter up to the one you were last studying
  (e.g. coming from Chapter 6 selects 1–6); "All" / "None" shortcuts and per-chapter checkboxes change it.
  Choose how many questions (5–30 or all): they're drawn evenly from each chosen chapter's bank (plus any
  Gemini questions already added to those chapter quizzes), shuffled, and tagged with their chapter.
  "✦ 5 more questions" writes new ones spread across the chosen chapters.
- **Interviewer** (every book; sidebar under Reference and an "Interview practice" card on every chapter page;
  `#interview6.3` for Mechanics of Materials, `#g-interview9.2` GD&T, `#m-interview5.3` Materials,
  `#r-interview3.1` Soft Robotics, `#p-interview3.2` Polymers) is a full-screen mock interview on each book's problems: Mechanics of Materials
  uses the book's 176 worked Examples, Materials its 77 worked Examples, GD&T 108 practice problems (4 per chapter,
  written from the notes, ASME Y14.5-2009) and Soft Robotics 60 problems (5 per lecture, written from the slides).
  Pick a chapter and a problem, or **Shuffle**
  (unfinished ones first; "All chapters" shuffles across the book). The problem statement and its initial figure
  are shown (only the given-data panel, never the solution panels). Gemini then asks you to explain the set-up
  at a high level and drills down one question at a time to the final numbers, without hints or leading
  questions; as soon as something you say is wrong it stops, says so and explains why, then lets you continue.
  It ends with a short debrief. The right half is a **scratchpad** (pen, eraser, undo, pan/zoom; from the
  mech-design-interview-quiz repo): when it has changed, it's included with your next message as an image and
  the interviewer reads it as part of your answer. **Show solution** gives up and shows the book's solution.
  Conversations and scratchpads are saved per example in localStorage (**Restart** clears the conversation).
  - Data: `examples.js` (`window.EXAMPLES`: id, title, statement `q`, `figs`, `figDesc`, examiner-only `sol`,
    `answers`), figures in `figures/ex/ex<ch>-<n>.webp`; the other books use `examples-gdt.js`, `examples-mat.js`,
    `examples-sr.js` (`window.EXAMPLES_BY.<key>`, `figs` as site-relative paths, e.g. `figures/ex-mat/…`). The figure image is sent to Gemini when the site is
    served over http(s) (e.g. GitHub Pages); opened from `file://` the browser blocks reading it, so the
    interviewer relies on the written figure description instead.
- **Ask tutor** (bottom-right) opens a chat that is given the notes of the chapter you have open.
- Both use your own Gemini API key, entered in the tutor's key settings. It is stored only in your browser's localStorage
  and sent directly to `generativelanguage.googleapis.com`; it is never committed or sent anywhere else. The model list
  comes from your key (newest Flash model selected by default, changeable in settings). Quiz progress is also kept in localStorage.
- Quiz data lives in `<script type="text/plain" id="quiz">` (and `id="quiz-gdt"`): `@ 6` starts chapter 6, then
  `? question || reference answer` per line.


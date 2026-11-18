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
- **Ask tutor** (bottom-right) opens a chat that is given the notes of the chapter you have open.
- Both use your own Gemini API key, entered in the tutor's key settings. It is stored only in your browser's localStorage
  and sent directly to `generativelanguage.googleapis.com`; it is never committed or sent anywhere else. The model list
  comes from your key (newest Flash model selected by default, changeable in settings). Quiz progress is also kept in localStorage.
- Quiz data lives in `<script type="text/plain" id="quiz">` (and `id="quiz-gdt"`): `@ 6` starts chapter 6, then
  `? question || reference answer` per line.


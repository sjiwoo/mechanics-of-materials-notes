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

## Editing content
All notes live in the `<script type="text/plain" id="data">` block in `index.html`:

```
# n | Chapter title | accent group (fund/load/bend/trans/design) | summary
## n.m | Section title | *        (trailing * = advanced section)
- concept bullet, inline math in $...$, figure link as {fig 6-24}
= LaTeX display equation || optional caption
=! LaTeX display equation || caption   critical: also listed on the Equation sheet
> chapter-summary bullet (lines right after the # chapter line)
! fig 6-24 || caption      key figure (textbook; add `crop` to use figures/card/)
! svg 6-1 || caption       key figure (custom SVG template sf-6-1)
```

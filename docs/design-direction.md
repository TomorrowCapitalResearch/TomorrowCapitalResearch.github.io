# Design direction — first structural iteration

## Three websites, three roles

| Website | Role | Visual direction |
| --- | --- | --- |
| Tomorrow Capital Research | Company, approach, selected platforms and systems | Paper white, deep navy, restrained medium blue |
| Tomorrow Library | Research, conjectures, methods, results, presentations, code and data | Proposed: white and pale blue surfaces with medium blue navigation and accents |
| Tomorrow Markets | Interactive market and portfolio simulations | Preserve the existing bright design and layout controls |

The company introduction is intentionally short. Readers can understand the purpose on the first page and choose the detail they want. Research publications belong in the Library; compact platform and system overviews belong on the company site.

## Company palette

| Token | Colour | Use |
| --- | --- | --- |
| `--paper` | `#F9FAFB` | Page surface |
| `--ink` | `#123655` | Main text, logo, footer |
| `--blue` | `#1769BD` | Emphasis, links, stepped growth |
| `--mid-blue` | `#215D96` | Focused blue section |
| `--pale` | `#EDF4FA` | Method and systems surfaces |
| `--muted` | `#52697C` | Supporting text |
| `--line` | `#D4DFE8` | Rules and dividers |

Typography uses device fonts: Georgia for editorial headings, Arial/Helvetica for body text, and Courier New for small indices. This avoids third-party font requests and keeps the site usable offline.

## The mark

The identity combines an accelerating sequence of discrete steps with a thin exponential reference. A terminal square identifies the current step; the mark does not use a financial arrow or currency symbol.

Files: `assets/growth-mark.svg`, `assets/growth-mark-white.svg`, and `assets/favicon.svg`. The editable definitions live in `scripts/build_site.py`. The larger home-page study uses equally spaced steps and multiplicative height increments; its schematic status is explained in its caption and accessible description.

The brand idea is incremental effort creating compounding possibilities. It does not assert that real-world growth is universally exponential or that investment returns follow this shape.

## Keep future changes focused

The page structure is ready for use. Useful next design choices are the serif style, blue saturation, size of the introductory graphic, and how much of the directory should appear in the first screen. Those choices can be revised in the shared CSS without reorganising the content.

For the future Library redesign, retain its navigation, search, learning content and tools. Restyle the existing components with a blue palette rather than replacing its application structure with the company layout. Keep Markets' current appearance and layout options.

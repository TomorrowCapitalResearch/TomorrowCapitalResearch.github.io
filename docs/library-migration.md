# Research handoff to Tomorrow Library

This company rebuild changes the navigation and presentation. It does not publish changes to the separate Library repository.

## Available destinations

The research directory links to existing pages confirmed in the Library repository:

| Resource | Current destination |
| --- | --- |
| Papers and research references | `https://tomorrowlibrary.github.io/papers.html` |
| Research process | `https://tomorrowlibrary.github.io/research-process.html` |
| Code and implementations | `https://tomorrowlibrary.github.io/code.html` |
| Data catalogue | `https://tomorrowlibrary.github.io/data.html` |
| Research engineering | `https://tomorrowlibrary.github.io/research-engineering.html` |

These are section destinations, not a claim that every company research document has already been imported.

## Conjectures

The complete original main content is retained in `src/pages/conjectures.html`, including original section IDs and the statements of the five conjectures. `Conjectures.html` renders that content with the new shared header, footer and an explicit provisional archive notice. It is excluded from the search sitemap and marked `noindex, follow` while it remains an earlier concept.

To migrate it:

1. Create a dedicated research/conjectures destination within the Library's existing content structure.
2. Import the preserved content, retaining the research statements and separating proposed programme/reward language from the scientific material.
3. Label the status of each conjecture, working note, empirical result and reproducible implementation where those are available. Do not present a proposed programme as an active offer.
4. Check mathematics, tables, links, anchors and mobile layout in the Library.
5. Once that page is actually published, update the last section of `src/pages/research.html` to its real URL. Then decide whether the old company path should remain as an archive or become a bridge to the published destination.

Until that destination exists, the company archive remains readable. Existing deep links are preserved.

## Research overview to carry forward

The earlier company overview described five areas of inquiry:

- Market microstructure and order flow: order placement, liquidity, inventory and observable price changes.
- Regime change and stochastic dynamics: non-stationarity, state transitions, dependence and outcome distributions.
- Signals, forecasts and validation: falsifiable signal hypotheses, benchmarks and distribution-aware evaluation.
- Portfolio construction and risk: allocation, dependence, exposure constraints, downside risk and execution-aware decisions.
- Emergence and aggregation: when collective behaviour can be described from local interactions and where simplified macroscopic models fail.

These are research themes, not evidence of a completed publication or validated trading result. Specific results, notebooks and presentations can be added to the Library with their own sources, assumptions and evaluation context.

## What stays on the company site

Concise descriptions of the public platforms, the research approach and selected systems. Add a finished product or a research service only when its scope, availability and a real contact or access route are ready to describe accurately.

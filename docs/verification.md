# Verification — 29 October 2026

## Source

Repository: `TomorrowCapitalResearch/TomorrowCapitalResearch.github.io`.
Base commit: `1f140a2669529830423ffa6b405e8c56407f0fcc`.
The remote `main` branch was checked again before packaging and still matched this baseline.

## Checks completed

- `python scripts/build_site.py`: builds 11 complete pages and three compatibility routes, plus shared fragments, sitemap and vector brand assets.
- `python scripts/check_site.py`: passes local link, asset, anchor, metadata, sitemap and archive checks.
- `node --check assets/site.js`: passes.
- `git diff --check`: passes.
- A repeated rebuild produced identical public HTML, brand marks and sitemap bytes.
- The original conjectures main fragment matches the baseline exactly after trimming only its outer whitespace. SHA-256: `a0e21d42ddad9a65356f6188e3a2548a55123fb344dff56e05f67cfff9886c4b`.
- Existing binary assets are unchanged.

## Browser checks

All 11 complete pages were checked inside browser frames with widths of 320, 390, 768 and 1440 pixels: 44 page/width combinations, with no horizontal document overflow. The browser reserves scrollbar space inside these frames. This covers responsive rendering; physical mobile devices and all browser engines were not tested.

Desktop views of the home page, About, public platforms and evaluation diagram were visually inspected. The home page's brand images loaded successfully.

The mobile menu opens, exposes its navigation and updates `aria-expanded`; Escape closes it. The skip link moves keyboard focus to the main content. With JavaScript disabled, navigation remains visible and usable. The three earlier page paths land on their intended replacements, including the Work section anchors.

No errors originating from the website were observed in the checked browser tab. Browser-extension metadata errors were outside the site's code.

## Publication boundary

No remote files or Pages settings were changed. The active GitHub connection reports read-only access to this repository. The packages are intended for implementation by uploading their contents to the existing repository, or committing them through an account with write access.

The research directory uses existing Library routes. Conjectures have been preserved for a later Library import; no new Library article is claimed to have been published. Tomorrow Markets and the separate Tomorrow Library repository are unchanged.

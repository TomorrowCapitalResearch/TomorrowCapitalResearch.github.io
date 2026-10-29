# Tomorrow Capital Research — flagship website

Complete static website rebuild with a wave/equilibrium/emergence visual identity.

## What is in this package

- `index.html`: institutional home with animated layered wavefronts and a calm navy/gold aesthetic.
- `who-we-are.html`: organisation and research philosophy.
- `approach.html`: methodology plus an interactive *illustrative* damped-wave/equilibrium experiment.
- `research.html`: inquiry themes and public research links.
- `systems.html`: engineering and research infrastructure.
- `platforms.html`: links to Tomorrow Library and Tomorrow Markets.
- `contact.html`: public contact channels (no misleading non-functional web form).
- `privacy.html`, `terms.html`, `disclosures.html`: general information pages — **review before publication**.
- `404.html`, `robots.txt`, `sitemap.xml`: static site housekeeping.
- `assets/site.css`: global design and responsive layout.
- `assets/site.js`: mobile navigation, reveal effects, procedural waves, equilibrium demo.
- `assets/wave-mark.svg`, `assets/favicon.svg`: original line-based mark (no rings).
- `assets/conjectures-bridge.css`: an optional non-destructive restyle for the *existing* `Conjectures.html`.
- `previews/`: representative desktop/mobile captures.

## Deploy to the existing GitHub Pages repository

Target: `TomorrowCapitalResearch/TomorrowCapitalResearch.github.io` (branch `main`).

1. **Back up the existing repository first** (or create a new branch and make a pull request for review).
2. Copy **the files at the root of this package** into the **root** of that repository, keeping `assets/` inside `assets/`. The new `index.html` replaces the original home page.
3. **Do not delete the existing `assets/` images/video, `Conjectures.html`, or `shared/` files**. Those assets are not duplicated in this package; the upload should add/overwrite matching filenames, not replace the entire assets folder.
4. To bring the original `Conjectures.html` onto the dark palette without changing its mathematics, place this line just before the closing `</head>` of the **existing** file, after its inline `<style>`:

   ```html
   <link rel="stylesheet" href="assets/conjectures-bridge.css">
   ```

   The source content, conjectures and provisional programme text remain unchanged. Review that page's prize/equity wording separately before public launch.
5. Test `index.html`, the new internal pages, and the original conjectures archive after GitHub Pages publishes.
6. Review `privacy.html`, `terms.html` and `disclosures.html` for legal accuracy, business identity and any future changes to analytics, mailing lists or contact processing.
7. Keep the existing GitHub Pages custom-domain or repository settings unchanged unless you deliberately wish to update them.

## Important decisions

**No deployment has been performed.** The connected GitHub account can read this repository but has no push permission. This package is an upload-ready build.

**No fake performance statistics.** No Sharpe, assets under management, track record, institutional scale or guarantees are asserted. The equilibrium wave model is explicitly labelled illustrative—not observed prices and not a working market forecaster.

**No external animation libraries or videos.** Geometry is drawn in Canvas 2D, with `requestAnimationFrame` paused when out of view and disabled for users who prefer reduced motion. This approach is intentionally lighter than a video-heavy flagship.

**No artificial contact form.** LinkedIn and GitHub are the only contact links; replace or supplement them once an official mailbox or contact backend is available.

**Static GitHub Pages compatible.** No build tools, framework, database or API keys are required.

**Typography.** Source Serif 4, Inter and DM Mono are loaded from Google Fonts. The pages have generic fallback fonts if Google Fonts is unavailable; review third-party font loading in your privacy notice.

## Responsive and functional checks

All 11 HTML pages were inspected at 1440 × 900 and 390 × 844 in a headless Chromium test with scripts/styles injected into an isolated preview. Checks confirmed no horizontal document overflow, no uncaught JavaScript errors, and working mobile navigation and the perturbation control under reduced motion.

## Subsequent phase

The next separate project is restyling Tomorrow Library's `assets/site.css` with coordinated mid-blue surfaces. No Tomorrow Library files have been changed in this build. Markets remains the brighter application.

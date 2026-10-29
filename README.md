# Tomorrow Capital Research

A complete static rebuild of the company website: a compact introduction, a clear explanation of the approach, selected work, a directory to public research, and contact channels.

This is the **company repository**. Tomorrow Markets and Tomorrow Library are separate websites; neither repository is modified by this update.

## Implement this update

The generated website is already included. No build tool, framework, installation, API key or backend is needed to publish it.

1. Extract the package.
2. Copy the **contents inside the package** into the root of `TomorrowCapitalResearch/TomorrowCapitalResearch.github.io`, merging folders and replacing files with matching names. `index.html` must be at the repository root, with `assets/` beside it. Do not upload the outer ZIP folder as a new subdirectory.
3. Include the new `about.html`, `work.html`, `src/`, `scripts/`, and `docs/` files. Keep the existing images and video in `assets/`; the new design does not load them, but they remain available.
4. Commit the update to the branch used by GitHub Pages. For the existing setup, retain `main` and the root publication folder. No Pages settings change is required by this rebuild.
5. After Pages publishes, check the home page, navigation, research directory and contact links.

The compact update ZIP contains all changed and new repository files. The full repository ZIP also includes the existing media assets. Both contain the complete new website; the compact package is easiest to upload over the existing repository.

**Publication status:** the connected GitHub account has read-only access to this repository. These packages have been prepared and checked locally; no GitHub commit, pull request or production deployment has been made.

## Preview locally

From the extracted package's root, run:

```sh
python -m http.server 8000
```

Open `http://localhost:8000/`. The generated pages also use relative assets and can be opened directly, though an HTTP preview gives the most representative behaviour, especially for redirects and the 404 page.

## Structure

| Page | Purpose |
| --- | --- |
| `index.html` | Short company introduction and directory |
| `about.html` | Purpose, scope and principles |
| `approach.html` | Research process and chronological evaluation schematic |
| `work.html` | Tomorrow Markets, Tomorrow Library and systems development |
| `research.html` | Direct links to verified Library sections and the earlier archive |
| `contact.html` | Existing LinkedIn and GitHub channels |
| `Conjectures.html` | Preserved provisional research text with a clear archive notice |
| `privacy.html`, `terms.html`, `disclosures.html` | Supporting website information |
| `404.html` | Recovery page for missing URLs |

Existing URLs continue to work:

| Earlier URL | Destination |
| --- | --- |
| `who-we-are.html` | `about.html` |
| `systems.html` | `work.html#systems` |
| `platforms.html` | `work.html#platforms` |
| `Conjectures.html#…` | Preserved page and original section IDs |

## Edit and iterate

The website is published from the ready-made HTML files at the root. The optional Python scripts keep shared content consistent across pages.

| Change | Source |
| --- | --- |
| Colours, layout, spacing and typography | `assets/site.css` |
| Page copy and sections | `src/pages/*.html` |
| Navigation, public URLs, page titles and descriptions | `src/site.json` |
| Shared page shell | `src/templates/page.html` |
| Header, footer, logo and geometric illustrations | `scripts/build_site.py` |
| Navigation behaviour | `assets/site.js` |
| Archive presentation | `assets/archive.css` |
| Social preview artwork | `assets/social-card.svg` and the pre-exported PNG |

After editing source content, run:

```sh
python scripts/build_site.py
python scripts/check_site.py
```

Commit the regenerated root HTML, shared fragments, sitemap and brand assets alongside the source changes. Direct edits to generated files work, but a later rebuild will overwrite them. Prefer editing `src/` when using the generator.

The builder uses the Python standard library only. `--preview` optionally stages the active public files in an ignored `dist/` directory. The checked-in PNG is already exported; exporting a revised social card is a separate image-export step, not a prerequisite for building the pages.

## Design direction

Paper white, deep navy and a clear medium blue. Editorial serif headings, small sans-serif body text, thin rules and generous space. No stock photography or ornamental animation is needed to explain the work.

The logo combines discrete steps with a compounding curve. The home illustration expands the same idea. Neither represents a return profile or financial forecast.

See `docs/design-direction.md` for the palette, logo logic and next design decisions, and `docs/library-migration.md` for the research handoff.

## Research and platform boundaries

The company presents its purpose, method and selected systems. The research directory sends readers to existing Library pages for papers, process, code, data and engineering. Conjectures are retained until a real Library destination is published; no content has been silently removed or redirected to a nonexistent article.

Work lists two public platforms and separately labels WTech as research and development. It does not invent commercial services, clients, staff numbers, investment results or product availability. Contact uses the existing public channels rather than an invented mailbox or an unconnected form.

Tomorrow Markets retains its current design. The Library's blue redesign is a separate implementation; this package establishes its role and links without changing its content or features.

## Validation

- Static checks pass for all 11 complete pages, local links and assets, anchor targets, metadata, sitemap and compatibility routes.
- Browser layout checks cover all 11 pages in 320, 390, 768 and 1440 pixel-wide frames. No horizontal document overflow was detected. These are responsive browser checks, not physical-device testing.
- Desktop composition was inspected for the introduction, About, platform presentations and evaluation schematic.
- Mobile menu opening, Escape dismissal, navigation without JavaScript and all three compatibility redirects were checked.
- The original conjectures main content is preserved exactly in `src/pages/conjectures.html` and reproduced in the archive page.
- Existing binary assets are retained unchanged. Images in `previews/` document the previous design and are not previews of this revision.

Source baseline: `1f140a2669529830423ffa6b405e8c56407f0fcc` on `main`, retrieved 29 October 2026.

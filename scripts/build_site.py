#!/usr/bin/env python3
"""Build the committed, standalone GitHub Pages files. Python standard library only.

Run from any directory: python3 scripts/build_site.py
The website itself needs no Python, build service or JavaScript framework.
"""
from html import escape
from pathlib import Path
from string import Template
import json
import math
import argparse
import shutil

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'src/site.json').read_text(encoding='utf-8'))
TEMPLATE = Template((ROOT / 'src/templates/page.html').read_text(encoding='utf-8'))


def icon(direction='right'):
    paths = {
        'right': 'M4 12h15m-6-6 6 6-6 6',
        'external': 'M6 18 18 6M6 6h12v12',
        'down': 'M12 4v15m-6-6 6 6 6-6',
    }
    return f'<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.35" aria-hidden="true"><path d="{paths[direction]}"/></svg>'


def brand(dark=False):
    mark = 'growth-mark-white.svg' if dark else 'growth-mark.svg'
    return f'''<a class="brand" href="index.html" aria-label="Tomorrow Capital Research — home">
      <img class="brand-icon" src="assets/{mark}" width="42" height="42" alt="">
      <span><span class="brand-name">Tomorrow</span><span class="brand-descriptor">Capital Research</span></span>
    </a>'''


def header(current=''):
    items = []
    for entry in CONFIG['navigation']:
        active = ' aria-current="page"' if entry['href'] == current else ''
        items.append(f'<a href="{escape(entry["href"], quote=True)}"{active}>{escape(entry["label"])}</a>')
    return f'''<header class="site-header"><div class="shell header-inner">
    {brand()}
    <button class="nav-toggle" type="button" data-menu-toggle aria-controls="primary-menu" aria-expanded="false">Menu</button>
    <nav class="primary-nav" id="primary-menu" data-menu aria-label="Primary navigation">{' '.join(items)}</nav>
  </div></header>'''


def footer():
    links = CONFIG['links']
    company = ''.join(f'<a href="{escape(x["href"], quote=True)}">{escape(x["label"])}</a>' for x in CONFIG['navigation'])
    return f'''<footer class="site-footer"><div class="shell">
    <div class="footer-top"><div class="footer-brand">{brand(True)}<p>Making tomorrow better, step by step.</p></div>
    <div class="footer-links"><div><p>The company</p>{company}</div>
    <div><p>Explore Tomorrow</p><a href="{links['library']}">Tomorrow Library ↗</a><a href="{links['markets']}">Tomorrow Markets ↗</a><a href="{links['github']}">GitHub ↗</a><a href="{links['linkedin']}">LinkedIn ↗</a></div></div></div>
    <div class="footer-bottom"><p>© <span data-year>2026</span> Tomorrow Capital Research</p><nav aria-label="Website information"><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="disclosures.html">Research notes</a></nav></div>
  </div></footer>'''


def growth_figure():
    """Uniform time steps with multiplicative height increments; purely illustrative."""
    # A continuous exponential reference passes through the discrete step endpoints.
    x0, dx, baseline, initial, rate, count = 36, 40, 400, 13, 1.30, 13
    points = [(x0 + i * dx, baseline - initial * rate ** i) for i in range(count)]
    step = f'M{points[0][0]},{points[0][1]:.2f}'
    for x, y in points[1:]:
        step += f'H{x}V{y:.2f}'
    smooth = ' '.join(f'{"M" if j == 0 else "L"}{x0 + j * dx / 12:.2f},{baseline - initial * rate ** (j / 12):.2f}' for j in range((count - 1) * 12 + 1))
    blocks = []
    # An expanding field of discrete units under the curve echoes the logo reference.
    for x, y in points:
        for block_y in range(385, math.ceil(y + 20), -25):
            blocks.append(f'<rect x="{x - 2}" y="{block_y}" width="4" height="4" fill="#1769bd" opacity=".22"/>')
    ticks = ''.join(f'<path d="M{x},412v5"/>' for x, _ in points)
    return f'''<svg class="growth-plot" viewBox="0 0 560 450" role="img" aria-labelledby="growth-title growth-desc">
      <title id="growth-title">Progress, step by step</title>
      <desc id="growth-desc">A sequence of discrete, increasing steps follows an exponential reference curve. Each step builds on the previous one. This is a brand illustration, not financial data.</desc>
      <path d="M25 412H538" stroke="#c3d6e5" fill="none"/>
      <g stroke="#9ebbd2">{ticks}</g>
      {''.join(blocks)}
      <path d="{smooth}" stroke="#6e95b4" stroke-width="1.2" stroke-dasharray="3 5" fill="none"/>
      <path d="{step}" stroke="#1769bd" stroke-width="2.8" fill="none"/>
      <rect x="{points[-1][0]-4}" y="{points[-1][1]-4:.2f}" width="8" height="8" fill="#123655"/>
      <text x="36" y="442" font-family="Arial, sans-serif" font-size="10" fill="#52697c">Incremental effort</text>
      <text x="516" y="442" font-family="Arial, sans-serif" font-size="10" text-anchor="end" fill="#52697c">Accumulated progress</text>
    </svg>'''


def markets_figure():
    return '''<svg viewBox="0 0 500 190" fill="none">
      <path d="M0 155H500M0 110H500M0 65H500" stroke="#e4edf4"/>
      <path d="M0 149 32 145 55 150 83 132 112 139 138 107 166 121 198 102 230 109 260 82 288 94 318 65 345 74 373 41 400 53 425 31 459 39 500 12" stroke="#1769bd" stroke-width="2"/>
      <path d="M0 153 35 155 70 146 105 153 140 139 175 145 210 126 245 135 280 110 315 121 350 104 385 114 420 91 455 97 500 78" stroke="#91badb" stroke-width="1.3"/>
      <path d="M0 156 42 152 82 158 122 149 163 147 204 154 245 144 286 145 327 135 368 140 409 127 450 132 500 119" stroke="#b4c8d8" stroke-width="1.3"/>
    </svg>'''


def library_figure():
    return '''<svg viewBox="0 0 500 190" fill="none">
      <g stroke="#8bb3d3" stroke-width="1"><path d="M60 30v133M60 69h380M60 116h380M440 30v133"/>
      <path d="M155 30v133M250 30v133M345 30v133"/></g>
      <g fill="#1769bd"><rect x="57" y="27" width="6" height="6"/><rect x="152" y="66" width="6" height="6"/><rect x="247" y="113" width="6" height="6"/><rect x="342" y="66" width="6" height="6"/><rect x="437" y="27" width="6" height="6"/></g>
      <path d="M60 30 155 69 250 116 345 69 440 30" stroke="#1769bd" stroke-width="1.6"/>
    </svg>'''


def write_marks():
    # A smooth compounding idea plus five discrete steps. No upward arrow or return claim.
    for filename, primary, secondary in [('growth-mark.svg', '#123655', '#1769bd'), ('growth-mark-white.svg', '#ffffff', '#9ed0fc')]:
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" fill="none">
  <title>Tomorrow — progress, step by step</title>
  <path d="M6 55H16V52H26V47H36V39H46V27H56V9" stroke="{primary}" stroke-width="2.8"/>
  <path d="M6 55C28 53 47 36 56 9" stroke="{secondary}" stroke-width="1.2" stroke-dasharray="1.5 2.7"/>
  <path d="M10 60h2m8 0h2m8 0h2m8 0h2m8 0h2m8 0h2" stroke="{secondary}" stroke-width="2"/>
  <path d="M53 6h6v6h-6z" fill="{primary}"/>
</svg>'''
        (ROOT / 'assets' / filename).write_text(svg + '\n', encoding='utf-8')
    # Favicon uses fewer details to remain legible at small sizes.
    (ROOT / 'assets/favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="10" fill="#123655"/><path d="M10 51H20V47H30V40H40V29H50V12" stroke="white" stroke-width="4" fill="none"/><path d="M47 9h6v6h-6z" fill="#9ed0fc"/></svg>\n''', encoding='utf-8')


def build():
    write_marks()
    footer_html = footer()
    substitutions = {
        **{key: escape(value, quote=True) for key, value in CONFIG['links'].items()},
        'arrow': icon(), 'external_arrow': icon('external'), 'down_arrow': icon('down'),
        'growth_figure': growth_figure(), 'markets_figure': markets_figure(), 'library_figure': library_figure(),
    }
    for page in CONFIG['pages']:
        file = page['file']
        content = Template((ROOT / 'src/pages' / page['source']).read_text(encoding='utf-8')).substitute(substitutions)
        extra_head = '<meta name="robots" content="noindex, follow">' if page.get('noindex') else ''
        extra_css = ''
        if file == '404.html':
            extra_head += '\n  <base href="/">'
        if file == 'Conjectures.html':
            extra_css = '<link rel="stylesheet" href="assets/archive.css">'
            content = '''<div class="shell archive-banner" role="note"><h2>Earlier conjectures / Provisional concept archive</h2><p>This original text is retained as a research record while the Library collection is developed. The proposed programme and rewards are provisional concept material, not a current offer. <a href="research.html">Explore current research resources</a> or <a href="''' + CONFIG['links']['library'] + '''">visit Tomorrow Library</a>.</p></div><div class="tc-inner">''' + content + '</div>'
        title = page['title'] if file == 'index.html' else f"{page['title']} | {CONFIG['name']}"
        canonical = CONFIG['url'] + ('/' if file == 'index.html' else '/' + file)
        html = TEMPLATE.substitute(
            title=escape(title, quote=True), description=escape(page['description'], quote=True),
            canonical=escape(canonical, quote=True), base_url=escape(CONFIG['url'], quote=True),
            body_class=page['class'], header=header(file), footer=footer_html, content=content,
            extra_head=extra_head, extra_css=extra_css,
        )
        (ROOT / file).write_text(html, encoding='utf-8')

    for source, destination in CONFIG['redirects'].items():
        safe = escape(destination, quote=True)
        canonical = escape(CONFIG['url'] + '/' + destination.split('#')[0], quote=True)
        (ROOT / source).write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page moved | Tomorrow Capital Research</title><meta name="robots" content="noindex, follow"><link rel="canonical" href="{canonical}"><meta http-equiv="refresh" content="0;url={safe}"></head><body><p>This page has moved. <a href="{safe}">Continue to the updated page</a>.</p></body></html>\n''', encoding='utf-8')

    # Keep existing integration paths coherent, without runtime fragment fetching.
    (ROOT / 'shared/header.html').write_text(header() + '\n', encoding='utf-8')
    (ROOT / 'header.html').write_text(header() + '\n', encoding='utf-8')
    (ROOT / 'shared/footer.html').write_text(footer_html + '\n', encoding='utf-8')
    urls = [CONFIG['url'] + ('/' if p['file'] == 'index.html' else '/' + p['file']) for p in CONFIG['pages'] if not p.get('noindex')]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{escape(url)}</loc></url>\n' for url in urls) + '</urlset>\n'
    (ROOT / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + CONFIG['url'] + '/sitemap.xml\n', encoding='utf-8')
    print(f"Built {len(CONFIG['pages'])} pages, {len(CONFIG['redirects'])} compatibility routes, shared fragments and brand marks.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview', action='store_true', help='Also stage active public files in dist/ for local preview.')
    args = parser.parse_args()
    build()
    if args.preview:
        output = ROOT / 'dist'
        (output / 'assets').mkdir(parents=True, exist_ok=True)
        for source in ROOT.glob('*.html'):
            shutil.copyfile(source, output / source.name)
        for name in ['site.css', 'site.js', 'archive.css', 'growth-mark.svg', 'growth-mark-white.svg', 'favicon.svg', 'social-card.png']:
            source = ROOT / 'assets' / name
            if source.exists():
                shutil.copyfile(source, output / 'assets' / name)
        for name in ['robots.txt', 'sitemap.xml', '.nojekyll']:
            shutil.copyfile(ROOT / name, output / name)
        print('Staged active site in dist/.')

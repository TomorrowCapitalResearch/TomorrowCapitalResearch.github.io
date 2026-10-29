#!/usr/bin/env python3
"""Check public page structure, local links, assets and metadata. No dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'src/site.json').read_text(encoding='utf-8'))


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.duplicates, self.refs = set(), [], []
        self.h1 = self.main = self.canonical = self.description = 0
        self.feed(text)

    def handle_starttag(self, tag, values):
        attrs = dict(values)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.duplicates.append(attrs['id'])
            self.ids.add(attrs['id'])
        self.h1 += tag == 'h1'
        self.main += tag == 'main'
        self.canonical += tag == 'link' and attrs.get('rel') == 'canonical'
        self.description += tag == 'meta' and attrs.get('name') == 'description'
        if tag in ('a', 'link') and attrs.get('href'):
            self.refs.append(attrs['href'])
        if tag in ('img', 'script') and attrs.get('src'):
            self.refs.append(attrs['src'])


def main():
    errors = []
    files = sorted(ROOT.glob('*.html'))
    pages = {p.name: Page(p.read_text(encoding='utf-8')) for p in files}
    public = {x['file'] for x in CONFIG['pages']}
    for file in files:
        page = pages[file.name]
        text = file.read_text(encoding='utf-8')
        if page.duplicates:
            errors.append(f'{file.name}: duplicate IDs {page.duplicates}')
        if file.name in public:
            if (page.h1, page.main, page.canonical, page.description) != (1, 1, 1, 1):
                errors.append(f'{file.name}: expected one h1, main, canonical and description; got {(page.h1, page.main, page.canonical, page.description)}')
            if re.search(r'\$(?:\{|arrow|library|markets|growth_figure)', text):
                errors.append(f'{file.name}: unresolved template value')
        for ref in page.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc or ref.startswith('//'):
                continue
            target = (file.parent / unquote(url.path)).resolve() if url.path else file
            if url.path.startswith('/'):
                target = ROOT / unquote(url.path.lstrip('/'))
            if target.is_dir():
                target = target / 'index.html'
            if not target.is_file():
                errors.append(f'{file.name}: missing local target {ref}')
            elif url.fragment and target.suffix == '.html':
                target_page = pages.get(target.name) or Page(target.read_text(encoding='utf-8'))
                if unquote(url.fragment) not in target_page.ids:
                    errors.append(f'{file.name}: missing anchor {ref}')

    for old, new in CONFIG['redirects'].items():
        html = (ROOT / old).read_text(encoding='utf-8')
        if f'0;url={new}' not in html:
            errors.append(f'{old}: missing compatibility redirect to {new}')
        path, _, anchor = new.partition('#')
        if path not in pages or (anchor and anchor not in pages[path].ids):
            errors.append(f'{old}: invalid redirect destination {new}')

    archive = (ROOT / 'src/pages/conjectures.html').read_text(encoding='utf-8').strip()
    if archive not in (ROOT / 'Conjectures.html').read_text(encoding='utf-8'):
        errors.append('Conjectures.html: original source fragment was not preserved')
    try:
        sitemap = ET.parse(ROOT / 'sitemap.xml')
        locations = {el.text for el in sitemap.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
        expected = {CONFIG['url'] + ('/' if p['file'] == 'index.html' else '/' + p['file']) for p in CONFIG['pages'] if not p.get('noindex')}
        if locations != expected:
            errors.append('sitemap.xml: canonical public pages do not match')
    except ET.ParseError as error:
        errors.append(f'sitemap.xml: {error}')

    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(public)} public pages, {len(CONFIG["redirects"])} compatibility routes, local assets and links, anchor IDs, metadata, sitemap and archive preservation.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

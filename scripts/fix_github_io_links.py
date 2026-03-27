#!/usr/bin/env python3
"""
fix_github_io_links.py — Fix all github.io refs + canonical/og:url to use poki2.online domain.
Run from repo root: python3 scripts/fix_github_io_links.py
"""
import re, os, glob

DOMAIN = open('.domain').read().strip()
OLD_GITHUB = 'geometry-dashlite.github.io'
NEW_DOMAIN = DOMAIN

pages = sorted(glob.glob('*.html'))
for filename in pages:
    txt = open(filename, encoding='utf-8').read()
    orig = txt

    # 1. Replace all geometry-dashlite.github.io → geometrydash-lite.poki2.online
    txt = txt.replace(OLD_GITHUB, NEW_DOMAIN)

    # 2. Fix relative canonical URLs → absolute
    # Pattern: canonical href="/<slug>" or href="/..."
    def fix_canonical(m):
        href = m.group(1)
        if href.startswith('http'):
            return m.group(0)
        slug = href.rstrip('/')
        if slug == '' or slug == '/':
            return f'<link rel="canonical" href="https://{NEW_DOMAIN}"'
        return f'<link rel="canonical" href="https://{NEW_DOMAIN}{slug}"'

    txt = re.sub(r'<link rel="canonical" href="([^"]*)"', fix_canonical, txt)

    # 3. Fix relative og:url → absolute
    def fix_og_url(m):
        val = m.group(1)
        if val.startswith('http'):
            return m.group(0)
        slug = val.rstrip('/')
        if slug == '' or slug == '/':
            return f'<meta property="og:url" content="https://{NEW_DOMAIN}"'
        return f'<meta property="og:url" content="https://{NEW_DOMAIN}{slug}"'

    txt = re.sub(r'<meta property="og:url" content="([^"]*)"', fix_og_url, txt)

    if txt != orig:
        open(filename, 'w', encoding='utf-8').write(txt)
        count = orig.count(OLD_GITHUB)
        print(f'Fixed: {filename}  ({count} github.io refs replaced)')
    else:
        print(f'  No change: {filename}')

print('Done.')

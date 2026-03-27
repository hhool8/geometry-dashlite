#!/usr/bin/env python3
"""
gen_sitemap.py — Generate sitemap.xml from .domain and git log dates.
Run from repo root: python3 scripts/gen_sitemap.py
"""
import subprocess, datetime

DOMAIN = 'https://' + open('.domain').read().strip()

# List of (url-path, html-file)
PAGES = [
    ('/', 'index.html'),
    ('/geometry-dash-lite', 'index.html'),
    ('/danger-dash', 'danger-dash.html'),
    ('/geometry-dash-astral-prism', 'geometry-dash-astral-prism.html'),
    ('/geometry-dash-demon-park', 'geometry-dash-demon-park.html'),
    ('/geometry-dash-horror', 'geometry-dash-horror.html'),
    ('/geometry-dash-look-up', 'geometry-dash-look-up.html'),
    ('/geometry-dash-megalodon', 'geometry-dash-megalodon.html'),
    ('/red-rush', 'red-rush.html'),
    ('/slope', 'slope.html'),
    ('/about-us', 'about-us.html'),
    ('/contact-us', 'contact-us.html'),
    ('/dmca', 'dmca.html'),
    ('/privacy-policy', 'privacy-policy.html'),
    ('/terms-of-service', 'terms-of-service.html'),
]

def lastmod(filepath):
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%cI', filepath],
            capture_output=True, text=True
        )
        date = result.stdout.strip()
        if date:
            return date[:10]
    except Exception:
        pass
    return datetime.date.today().isoformat()

seen = set()
entries = []
for path, htmlfile in PAGES:
    url = DOMAIN + path
    if url in seen:
        continue
    seen.add(url)
    prio = '1.0' if path in ('/', '/geometry-dash-lite') else ('0.8' if path.startswith('/geometry') or path in ('/danger-dash', '/red-rush', '/slope') else '0.6')
    freq = 'weekly' if prio in ('1.0', '0.8') else 'monthly'
    entries.append(f'''  <url>
    <loc>{url}</loc>
    <lastmod>{lastmod(htmlfile)}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>''')

xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
xml += '\n'.join(entries)
xml += '\n</urlset>\n'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml)

print(f'Generated sitemap.xml with {len(entries)} URLs for {DOMAIN}')

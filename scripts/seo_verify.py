#!/usr/bin/env python3
"""
seo_verify.py — Audit all pages and output docs/seo-audit-report.md.
Run from repo root: python3 scripts/seo_verify.py
"""
import os, re

DOMAIN = 'https://' + open('.domain').read().strip()
GA4_ID = 'G-2F54CGWRGW'
OLD_DOMAIN = 'geometry-dashlite.github.io'

GAME_PAGES = [
    'index.html',
    'danger-dash.html',
    'geometry-dash-astral-prism.html',
    'geometry-dash-demon-park.html',
    'geometry-dash-horror.html',
    'geometry-dash-look-up.html',
    'geometry-dash-megalodon.html',
    'red-rush.html',
    'slope.html',
]

SUPPORT_PAGES = [
    'about-us.html',
    'contact-us.html',
    'dmca.html',
    'privacy-policy.html',
    'terms-of-service.html',
    '404.html',
    'favorite.html',
]

ALL_PAGES = GAME_PAGES + SUPPORT_PAGES

CHECKS = {
    'title': (lambda t: bool(re.search(r'<title>[^<]{10,}</title>', t)), 'CRITICAL'),
    'meta_desc': (lambda t: bool(re.search(r'<meta name="description" content=".{20,}"', t)), 'CRITICAL'),
    'canonical': (lambda t: bool(re.search(r'<link rel="canonical" href="https://', t)), 'WARNING'),
    'og_title': (lambda t: bool(re.search(r'<meta property="og:title" content=".{5,}"', t)), 'WARNING'),
    'og_desc': (lambda t: bool(re.search(r'<meta property="og:description" content=".{10,}"', t)), 'WARNING'),
    'og_url': (lambda t: bool(re.search(r'<meta property="og:url" content="https://', t)), 'WARNING'),
    'og_image': (lambda t: bool(re.search(r'<meta property="og:image" content="https://' + re.escape(DOMAIN[8:]), t)), 'WARNING'),
    'twitter_card': (lambda t: bool(re.search(r'<meta name="twitter:card"', t)), 'WARNING'),
    'ga4': (lambda t: GA4_ID in t, 'WARNING'),
    'no_github_io': (lambda t: OLD_DOMAIN not in t, 'CRITICAL'),
}

GAME_ONLY_CHECKS = {
    'schema_videogame': (lambda t: '"@type": "VideoGame"' in t, 'WARNING'),
    'cwv_tracking': (lambda t: 'Core Web Vitals tracking' in t, 'INFO'),
}

HOMEPAGE_ONLY_CHECKS = {
    'schema_website': (lambda t: '"@type": "WebSite"' in t, 'WARNING'),
    'schema_faq': (lambda t: '"@type": "FAQPage"' in t, 'INFO'),
}

report_lines = []
report_lines.append(f'# SEO Audit Report — {DOMAIN}\n')
report_lines.append(f'Generated automatically by `scripts/seo_verify.py`\n')

total_issues = {'CRITICAL': 0, 'WARNING': 0, 'INFO': 0}
all_ok = True

for fname in ALL_PAGES:
    if not os.path.exists(fname):
        report_lines.append(f'\n## {fname}\n- FILE NOT FOUND\n')
        total_issues['CRITICAL'] += 1
        all_ok = False
        continue

    txt = open(fname, encoding='utf-8').read()
    issues = []

    # Common checks
    for check, (fn, level) in CHECKS.items():
        if not fn(txt):
            issues.append((level, check))
            total_issues[level] += 1

    # Game-only checks
    if fname in GAME_PAGES:
        for check, (fn, level) in GAME_ONLY_CHECKS.items():
            if not fn(txt):
                issues.append((level, check))
                total_issues[level] += 1

    # Homepage-only checks
    if fname == 'index.html':
        for check, (fn, level) in HOMEPAGE_ONLY_CHECKS.items():
            if not fn(txt):
                issues.append((level, check))
                total_issues[level] += 1

    if issues:
        all_ok = False
        report_lines.append(f'\n## {fname}\n')
        for level, check in issues:
            report_lines.append(f'- **{level}**: {check}')
    else:
        report_lines.append(f'\n## {fname}\n- OK — all checks passed\n')

# Check infra
report_lines.append('\n## Infrastructure\n')
for f in ['sitemap.xml', 'robots.txt', 'og-cover.png']:
    if os.path.exists(f):
        report_lines.append(f'- OK: {f} present')
    else:
        report_lines.append(f'- **WARNING**: {f} missing')
        total_issues['WARNING'] += 1
        all_ok = False

report_lines.append('\n## Summary\n')
report_lines.append(f'- CRITICAL: {total_issues["CRITICAL"]}')
report_lines.append(f'- WARNING:  {total_issues["WARNING"]}')
report_lines.append(f'- INFO:     {total_issues["INFO"]}')
if all_ok:
    report_lines.append('\n**All checks passed!**')
else:
    report_lines.append('\nSome issues found — review above.')

os.makedirs('docs', exist_ok=True)
report_path = 'docs/seo-audit-report.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(report_lines) + '\n')

print(f'Audit report written to {report_path}')
print(f'CRITICAL: {total_issues["CRITICAL"]}  WARNING: {total_issues["WARNING"]}  INFO: {total_issues["INFO"]}')

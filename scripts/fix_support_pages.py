#!/usr/bin/env python3
"""Fix remaining audit issues on support pages."""
import re

DOMAIN = 'https://geometrydash-lite.poki2.online'
OG_COVER = DOMAIN + '/og-cover.png'

support_pages = [
    'about-us.html',
    'dmca.html',
    'contact-us.html',
    'privacy-policy.html',
    'terms-of-service.html',
    'favorite.html',
    '404.html',
]

for fname in support_pages:
    try:
        txt = open(fname, encoding='utf-8').read()
    except FileNotFoundError:
        print('SKIP: ' + fname)
        continue
    orig = txt

    # Fix empty og:image
    txt = re.sub(
        r'<meta property="og:image" content=""\s*/?>',
        '<meta property="og:image" content="' + OG_COVER + '" />',
        txt
    )
    # Fix og:image with double slash or wrong path
    txt = re.sub(
        r'<meta property="og:image" content="https://geometrydash-lite\.poki2\.online//[^"]*"',
        '<meta property="og:image" content="' + OG_COVER + '"',
        txt
    )

    # Fix short titles for about-us and dmca
    if fname == 'about-us.html':
        txt = txt.replace('<title>About Us</title>', '<title>About Us - Geometry Dash Lite</title>')
        txt = txt.replace('content="About Us"', 'content="About Us - Geometry Dash Lite"')
    if fname == 'dmca.html':
        txt = txt.replace('<title>DMCA</title>', '<title>DMCA Policy - Geometry Dash Lite</title>')
        txt = txt.replace('"og:title" content="DMCA"', '"og:title" content="DMCA Policy - Geometry Dash Lite"')
        txt = txt.replace('"title" content="DMCA"', '"title" content="DMCA Policy - Geometry Dash Lite"')

    # Add canonical to 404.html if missing
    if fname == '404.html' and '<link rel="canonical"' not in txt:
        txt = txt.replace('</head>',
            '<link rel="canonical" href="' + DOMAIN + '/404" data-react-helmet="true">\n</head>', 1)
        print('Added canonical to 404.html')

    if txt != orig:
        open(fname, 'w', encoding='utf-8').write(txt)
        print('Fixed: ' + fname)
    else:
        print('No change: ' + fname)

print('Done.')

#!/usr/bin/env python3
"""
seo_offpage.py — Inject Twitter Card meta tags after og:image on all pages.
Run from repo root: python3 scripts/seo_offpage.py
"""
import re, os

DOMAIN = 'https://' + open('.domain').read().strip()
TWITTER_SITE = '@geometrydashlite'

# Per-page Twitter Card values
PAGE_META = {
    'index.html': {
        'title': 'Geometry Dash Lite Unblocked - Play Free Online | Geometry Dash',
        'desc': 'Play Geometry Dash Lite Unblocked free online — no download required! The ultimate rhythm platformer where you jump, fly and flip through danger.',
        'image': f'{DOMAIN}/data/image/game/geometry-dash-lite/geometry-dash-lite-game-m186x186.png',
    },
    'danger-dash.html': {
        'title': 'Danger Dash Unblocked - Play Free Online',
        'desc': 'Play Danger Dash Unblocked free online! A jungle running action game packed with deadly traps.',
        'image': f'{DOMAIN}/data/image/game/danger-dash/danger-dash-m186x186.png',
    },
    'geometry-dash-astral-prism.html': {
        'title': 'Geometry Dash Astral Prism Unblocked - Play Free Online',
        'desc': 'Play Geometry Dash Astral Prism Unblocked — cosmic platformer with glowing geometry and pulsating beats.',
        'image': f'{DOMAIN}/data/image/game/geometry-dash-astral-prism/geometry-dash-astral-prism-m186x186.png',
    },
    'geometry-dash-demon-park.html': {
        'title': 'Geometry Dash Demon Park Unblocked - Play Free Online',
        'desc': 'Play Geometry Dash Demon Park Unblocked — brutal rhythm challenge with fierce traps.',
        'image': f'{DOMAIN}/data/image/game/geometry-dash-demon-park/geometry-dash-demon-park-m186x186.png',
    },
    'geometry-dash-horror.html': {
        'title': 'Geometry Dash Horror Unblocked - Play Free Online',
        'desc': 'Play Geometry Dash Horror Unblocked — spooky jumps and eerie visuals across terrifying levels.',
        'image': f'{DOMAIN}/data/image/game/geometry-dash-horror/geometry-dash-horror-m186x186.jpg',
    },
    'geometry-dash-look-up.html': {
        'title': 'Geometry Dash Look Up Unblocked - Play Free Online',
        'desc': 'Play Geometry Dash Look Up Unblocked — attractive platformer filled with rhythm jumps.',
        'image': f'{DOMAIN}/data/image/game/geometry-dash-look-up/geometry-dash-look-up-m186x186.png',
    },
    'geometry-dash-megalodon.html': {
        'title': 'Geometry Dash Megalodon Unblocked - Play Free Online',
        'desc': 'Play Geometry Dash Megalodon Unblocked — aquatic hazards and deep-sea dashes.',
        'image': f'{DOMAIN}/data/image/game/geometry-dash-megalodon/geometry-dash-megalodon-m186x186.png',
    },
    'red-rush.html': {
        'title': 'Red Rush Unblocked - Play Free Online',
        'desc': 'Play Red Rush Unblocked free online! Crimson platform sprint with wild speed.',
        'image': f'{DOMAIN}/data/image/game/red-rush/red-rush-m186x186.png',
    },
    'slope.html': {
        'title': 'Slope Unblocked - Play Free Online',
        'desc': 'Play Slope Unblocked free online! High-speed endless runner on neon ramps.',
        'image': f'{DOMAIN}/data/image/game/slope/slope-m186x186.png',
    },
    'about-us.html': {
        'title': 'About Us - Geometry Dash Lite',
        'desc': 'Learn about Geometry Dash Lite, the free unblocked geometry dash gaming site.',
        'image': f'{DOMAIN}/og-cover.png',
    },
    'contact-us.html': {
        'title': 'Contact Us - Geometry Dash Lite',
        'desc': 'Get in touch with the Geometry Dash Lite team.',
        'image': f'{DOMAIN}/og-cover.png',
    },
    'dmca.html': {
        'title': 'DMCA - Geometry Dash Lite',
        'desc': 'DMCA policy for Geometry Dash Lite.',
        'image': f'{DOMAIN}/og-cover.png',
    },
    'privacy-policy.html': {
        'title': 'Privacy Policy - Geometry Dash Lite',
        'desc': 'Privacy policy for Geometry Dash Lite.',
        'image': f'{DOMAIN}/og-cover.png',
    },
    'terms-of-service.html': {
        'title': 'Terms of Service - Geometry Dash Lite',
        'desc': 'Terms of service for Geometry Dash Lite.',
        'image': f'{DOMAIN}/og-cover.png',
    },
    'favorite.html': {
        'title': 'Favorites - Geometry Dash Lite',
        'desc': 'Your favorite games on Geometry Dash Lite.',
        'image': f'{DOMAIN}/og-cover.png',
    },
    '404.html': {
        'title': '404 Page Not Found - Geometry Dash Lite',
        'desc': 'The page you are looking for could not be found on Geometry Dash Lite.',
        'image': f'{DOMAIN}/og-cover.png',
    },
}

for filename, m in PAGE_META.items():
    if not os.path.exists(filename):
        print(f'SKIP (not found): {filename}')
        continue

    txt = open(filename, encoding='utf-8').read()
    orig = txt

    if 'name="twitter:card"' in txt:
        print(f'  Already has Twitter Card: {filename}')
        continue

    twitter_block = f'''<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="{TWITTER_SITE}">
<meta name="twitter:title" content="{m['title']}">
<meta name="twitter:description" content="{m['desc']}">
<meta name="twitter:image" content="{m['image']}">'''

    # Insert after og:image meta tag
    if re.search(r'<meta property="og:image"', txt):
        txt = re.sub(
            r'(<meta property="og:image"[^>]*>)',
            r'\1\n' + twitter_block,
            txt, count=1
        )
    else:
        # fallback: before </head>
        txt = txt.replace('</head>', twitter_block + '\n</head>', 1)

    if txt != orig:
        open(filename, 'w', encoding='utf-8').write(txt)
        print(f'Injected Twitter Card: {filename}')
    else:
        print(f'  No change: {filename}')

print('Done.')

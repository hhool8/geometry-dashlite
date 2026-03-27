#!/usr/bin/env python3
"""
fix_meta_tags.py — Update title/H1/meta description/keywords on all pages.
Run from repo root: python3 scripts/fix_meta_tags.py
"""
import re, os

DOMAIN = open('.domain').read().strip()

# Per-page metadata overrides
PAGES = {
    'index.html': {
        'title': 'Geometry Dash Lite Unblocked - Play Free Online | Geometry Dash',
        'h1': 'Geometry Dash Lite Unblocked',
        'desc': 'Play Geometry Dash Lite Unblocked free online — no download required! The ultimate rhythm platformer where you jump, fly and flip through danger. Works at school and on Chromebook.',
        'keywords': 'geometry dash lite, geometry dash unblocked, geometry dash free, unblocked geometry dash, geometry dash online, play geometry dash, geometry dash lite unblocked, geometry dash school',
    },
    'geometry-dash-astral-prism.html': {
        'title': 'Geometry Dash Astral Prism Unblocked - Play Free Online',
        'h1': 'Geometry Dash Astral Prism Unblocked',
        'desc': 'Play Geometry Dash Astral Prism Unblocked free online! A cosmic platformer wrapped in glowing geometry and pulsing beats. Conquer every neon obstacle now.',
        'keywords': 'geometry dash astral prism, geometry dash astral prism unblocked, geometry dash online, geometry dash free',
    },
    'geometry-dash-demon-park.html': {
        'title': 'Geometry Dash Demon Park Unblocked - Play Free Online',
        'h1': 'Geometry Dash Demon Park Unblocked',
        'desc': 'Play Geometry Dash Demon Park Unblocked free online! A brutal rhythm challenge with fierce traps and relentless beats. Survive every demon level now.',
        'keywords': 'geometry dash demon park, geometry dash demon park unblocked, geometry dash free, geometry dash online',
    },
    'geometry-dash-horror.html': {
        'title': 'Geometry Dash Horror Unblocked - Play Free Online',
        'h1': 'Geometry Dash Horror Unblocked',
        'desc': 'Play Geometry Dash Horror Unblocked free online! Spooky jumps, eerie visuals, and creepy rhythms across terrifying levels. Face your fear and dash now.',
        'keywords': 'geometry dash horror, geometry dash horror unblocked, geometry dash free, geometry dash online',
    },
    'geometry-dash-look-up.html': {
        'title': 'Geometry Dash Look Up Unblocked - Play Free Online',
        'h1': 'Geometry Dash Look Up Unblocked',
        'desc': 'Play Geometry Dash Look Up Unblocked free online! An attractive platformer filled with rhythm jumps and sky-high obstacles. Beat every level now.',
        'keywords': 'geometry dash look up, geometry dash look up unblocked, geometry dash free, geometry dash online',
    },
    'geometry-dash-megalodon.html': {
        'title': 'Geometry Dash Megalodon Unblocked - Play Free Online',
        'h1': 'Geometry Dash Megalodon Unblocked',
        'desc': 'Play Geometry Dash Megalodon Unblocked free online! Aquatic hazards and deep-sea dashes in a thrilling rhythm platformer. Dive into the danger now.',
        'keywords': 'geometry dash megalodon, geometry dash megalodon unblocked, geometry dash free, geometry dash online',
    },
    'danger-dash.html': {
        'title': 'Danger Dash Unblocked - Play Free Online',
        'h1': 'Danger Dash Unblocked',
        'desc': 'Play Danger Dash Unblocked free online! A jungle running action game packed with deadly traps and wild beasts. Sprint to safety now.',
        'keywords': 'danger dash, danger dash unblocked, danger dash free, run game unblocked',
    },
    'red-rush.html': {
        'title': 'Red Rush Unblocked - Play Free Online',
        'h1': 'Red Rush Unblocked',
        'desc': 'Play Red Rush Unblocked free online! A crimson platform sprint with wild speed and split-second reflexes. Rush through every obstacle now.',
        'keywords': 'red rush, red rush unblocked, red rush free, platform game unblocked',
    },
    'slope.html': {
        'title': 'Slope Unblocked - Play Free Online',
        'h1': 'Slope Unblocked',
        'desc': 'Play Slope Unblocked free online! A high-speed endless runner on neon ramps with sharp turns and gravity-defying physics. Roll to the top now.',
        'keywords': 'slope, slope unblocked, slope game, slope game unblocked, slope free',
    },
}

for filename, meta in PAGES.items():
    if not os.path.exists(filename):
        print(f'SKIP (not found): {filename}')
        continue
    txt = open(filename, encoding='utf-8').read()
    orig = txt

    # Title
    txt = re.sub(r'<title>[^<]*</title>', f'<title>{meta["title"]}</title>', txt)

    # Meta description
    txt = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{meta["desc"]}"',
        txt
    )

    # Meta keywords — replace or insert after description
    if re.search(r'<meta name="keywords"', txt):
        txt = re.sub(
            r'<meta name="keywords" content="[^"]*"',
            f'<meta name="keywords" content="{meta["keywords"]}"',
            txt
        )
    else:
        txt = re.sub(
            r'(<meta name="description"[^>]*>)',
            r'\1<meta name="keywords" content="' + meta['keywords'] + '">',
            txt, count=1
        )

    # og:title
    txt = re.sub(
        r'<meta property="og:title" content="[^"]*"',
        f'<meta property="og:title" content="{meta["title"]}"',
        txt
    )
    # og:description
    txt = re.sub(
        r'<meta property="og:description" content="[^"]*"',
        f'<meta property="og:description" content="{meta["desc"]}"',
        txt
    )

    # H1 — only replace first occurrence
    def replace_h1(m):
        return re.sub(r'>([^<]+)<', f'>{meta["h1"]}<', m.group(0), count=1)
    txt = re.sub(r'<h1[^>]*>[^<]*</h1>', replace_h1, txt, count=1)

    if txt != orig:
        open(filename, 'w', encoding='utf-8').write(txt)
        print(f'Updated: {filename}')
    else:
        print(f'  No change: {filename}')

print('Done.')

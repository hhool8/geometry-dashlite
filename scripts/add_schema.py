#!/usr/bin/env python3
"""
add_schema.py — Inject VideoGame JSON-LD schema into all 9 game pages.
Run from repo root: python3 scripts/add_schema.py
"""

DOMAIN = 'https://geometrydash-lite.poki2.online'

GAMES = [
    {
        'file': 'index.html',
        'name': 'Geometry Dash Lite',
        'desc': 'Geometry Dash Lite is a free online rhythm-based platformer. Jump, fly and flip your way through dangerous passages, all set to music.',
        'slug': 'geometry-dash-lite',
        'thumb_file': 'geometry-dash-lite-game-m186x186.png',
        'path': '/geometry-dash-lite',
    },
    {
        'file': 'danger-dash.html',
        'name': 'Danger Dash',
        'desc': 'Danger Dash is an action packed running game where you sprint through a jungle full of deadly traps and wild beasts.',
        'slug': 'danger-dash',
        'thumb_file': 'danger-dash-m186x186.png',
        'path': '/danger-dash',
    },
    {
        'file': 'geometry-dash-astral-prism.html',
        'name': 'Geometry Dash Astral Prism',
        'desc': 'Geometry Dash Astral Prism is a cosmic rhythm platformer with glowing geometry and pulsating beats. Conquer every neon obstacle.',
        'slug': 'geometry-dash-astral-prism',
        'thumb_file': 'geometry-dash-astral-prism-m186x186.png',
        'path': '/geometry-dash-astral-prism',
    },
    {
        'file': 'geometry-dash-demon-park.html',
        'name': 'Geometry Dash Demon Park',
        'desc': 'Geometry Dash Demon Park is an intense rhythm challenge filled with fierce traps and relentless beats. Survive every demon level.',
        'slug': 'geometry-dash-demon-park',
        'thumb_file': 'geometry-dash-demon-park-m186x186.png',
        'path': '/geometry-dash-demon-park',
    },
    {
        'file': 'geometry-dash-horror.html',
        'name': 'Geometry Dash Horror',
        'desc': 'Geometry Dash Horror is a spooky rhythm platformer with eerie visuals and creepy beats across terrifying levels.',
        'slug': 'geometry-dash-horror',
        'thumb_file': 'geometry-dash-horror-m186x186.jpg',
        'path': '/geometry-dash-horror',
    },
    {
        'file': 'geometry-dash-look-up.html',
        'name': 'Geometry Dash Look Up',
        'desc': 'Geometry Dash Look Up is an eye-catching platformer with rhythm jumps and sky-high obstacles. Beat every level.',
        'slug': 'geometry-dash-look-up',
        'thumb_file': 'geometry-dash-look-up-m186x186.png',
        'path': '/geometry-dash-look-up',
    },
    {
        'file': 'geometry-dash-megalodon.html',
        'name': 'Geometry Dash Megalodon',
        'desc': 'Geometry Dash Megalodon is a deep-sea rhythm platformer packed with aquatic hazards and pulse-pounding beats.',
        'slug': 'geometry-dash-megalodon',
        'thumb_file': 'geometry-dash-megalodon-m186x186.png',
        'path': '/geometry-dash-megalodon',
    },
    {
        'file': 'red-rush.html',
        'name': 'Red Rush',
        'desc': 'Red Rush is a crimson platform sprint game demanding wild speed and split-second reflexes. Rush through every obstacle.',
        'slug': 'red-rush',
        'thumb_file': 'red-rush-m186x186.png',
        'path': '/red-rush',
    },
    {
        'file': 'slope.html',
        'name': 'Slope',
        'desc': 'Slope is a high-speed endless runner on neon ramps with sharp turns and gravity-defying physics. Roll to the top.',
        'slug': 'slope',
        'thumb_file': 'slope-m186x186.png',
        'path': '/slope',
    },
]

ANCHOR = '<meta name="google-site-verification"'

for g in GAMES:
    fname = g['file']
    try:
        txt = open(fname, encoding='utf-8').read()
    except FileNotFoundError:
        print(f'SKIP (not found): {fname}')
        continue

    if '"@type": "VideoGame"' in txt:
        print(f'  Already has VideoGame schema: {fname}')
        continue

    img_url = f'{DOMAIN}/data/image/game/{g["slug"]}/{g["thumb_file"]}'
    page_url = DOMAIN + g['path']

    schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "VideoGame",
  "name": "{g['name']}",
  "description": "{g['desc']}",
  "url": "{page_url}",
  "image": "{img_url}",
  "genre": "Platformer",
  "gamePlatform": "Web Browser",
  "operatingSystem": "Any",
  "applicationCategory": "Game",
  "isAccessibleForFree": true,
  "inLanguage": "en"
}}
</script>
'''

    if ANCHOR not in txt:
        print(f'  WARNING: anchor not found in {fname}, appending before </head>')
        txt = txt.replace('</head>', schema + '</head>', 1)
    else:
        txt = txt.replace(ANCHOR, schema + ANCHOR, 1)

    open(fname, 'w', encoding='utf-8').write(txt)
    print(f'Injected VideoGame schema: {fname}')

print('Done.')

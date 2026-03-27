#!/usr/bin/env python3
"""
copy_game_thumbs.py — Copy game thumbnails from cache into data/image/game/.
Run from repo root: python3 scripts/copy_game_thumbs.py
"""
import os, shutil

THUMBS = [
    ('cache/data/image/game/geometry-dash-lite',  'geometry-dash-lite-game-m186x186.png', 'data/image/game/geometry-dash-lite'),
    ('cache/data/image/game/danger-dash',          'danger-dash-m186x186.png',             'data/image/game/danger-dash'),
    ('cache/data/image/game/geometry-dash-astral-prism', 'geometry-dash-astral-prism-m186x186.png', 'data/image/game/geometry-dash-astral-prism'),
    ('cache/data/image/game/geometry-dash-demon-park',   'geometry-dash-demon-park-m186x186.png',   'data/image/game/geometry-dash-demon-park'),
    ('cache/data/image/game/geometry-dash-horror',  'geometry-dash-horror-m186x186.jpg',   'data/image/game/geometry-dash-horror'),
    ('cache/data/image/game/geometry-dash-look-up', 'geometry-dash-look-up-m186x186.png',  'data/image/game/geometry-dash-look-up'),
    ('cache/data/image/game/geometry-dash-megalodon','geometry-dash-megalodon-m186x186.png','data/image/game/geometry-dash-megalodon'),
    ('cache/data/image/game/red-rush',              'red-rush-m186x186.png',               'data/image/game/red-rush'),
    ('cache/data/image/game/slope',                 'slope-m186x186.png',                  'data/image/game/slope'),
]

for src_dir, fname, dst_dir in THUMBS:
    src = os.path.join(src_dir, fname)
    if not os.path.exists(src):
        print(f'  MISSING: {src}')
        continue
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, fname)
    shutil.copy2(src, dst)
    print(f'Copied: {src} → {dst}')

print('Done.')

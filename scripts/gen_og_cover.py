#!/usr/bin/env python3
"""
gen_og_cover.py — Generate og-cover.png (1200x630) for the site.
Run from repo root:
  /Users/yanmenghou/Desktop/h5games/.venv/bin/python3 scripts/gen_og_cover.py
Requires: Pillow  (already installed in .venv)
"""
from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1200, 630
BG_COLOR = '#1a1a2e'      # dark navy
ACCENT = '#e94560'         # vivid red
TEXT_COLOR = '#eaeaea'
SUB_COLOR = '#a0a0c0'

img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# Gradient-like band at top
for i in range(HEIGHT // 3):
    alpha = int(60 * (1 - i / (HEIGHT / 3)))
    draw.line([(0, i), (WIDTH, i)], fill=(41, 20, 80))

# Accent bar at top
draw.rectangle([(0, 0), (WIDTH, 8)], fill=ACCENT)

# Try system fonts; fall back to default
font_paths = [
    '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
    '/System/Library/Fonts/Helvetica.ttc',
    '/Library/Fonts/Arial Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
]
font_large = None
font_medium = None
for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_large = ImageFont.truetype(fp, 80)
            font_medium = ImageFont.truetype(fp, 38)
            font_small = ImageFont.truetype(fp, 28)
            break
        except Exception:
            continue

if font_large is None:
    font_large = ImageFont.load_default()
    font_medium = font_large
    font_small = font_large

# Main title
title = 'Geometry Dash Lite'
bbox = draw.textbbox((0, 0), title, font=font_large)
tw = bbox[2] - bbox[0]
draw.text(((WIDTH - tw) // 2, 200), title, font=font_large, fill=TEXT_COLOR)

# Subtitle
sub = 'Play Unblocked Free Online'
bbox2 = draw.textbbox((0, 0), sub, font=font_medium)
sw = bbox2[2] - bbox2[0]
draw.text(((WIDTH - sw) // 2, 310), sub, font=font_medium, fill=ACCENT)

# Domain
domain = 'geometrydash-lite.poki2.online'
bbox3 = draw.textbbox((0, 0), domain, font=font_small)
dw = bbox3[2] - bbox3[0]
draw.text(((WIDTH - dw) // 2, 490), domain, font=font_small, fill=SUB_COLOR)

# Bottom bar
draw.rectangle([(0, HEIGHT - 8), (WIDTH, HEIGHT)], fill=ACCENT)

# Decorative circles
for x, y, r, col in [(80, 80, 50, '#e9456020'), (1120, 550, 40, '#e9456020'),
                      (600, 570, 30, '#29144020')]:
    draw.ellipse([(x-r, y-r), (x+r, y+r)], fill=col)

img.save('og-cover.png', 'PNG')
print('Generated og-cover.png (1200x630)')

#!/usr/bin/env python3
"""
gen_game_og_covers.py — Generate 1200x630 og:image covers for each game page.
Run from repo root:
  /Users/yanmenghou/Desktop/h5games/.venv/bin/python3 scripts/gen_game_og_covers.py
Requires: Pillow
"""
from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1200, 630
BG_COLOR = '#1a1a2e'
ACCENT = '#00a35a'        # site green
TEXT_COLOR = '#eaeaea'
SUB_COLOR = '#a0ccb0'
DOMAIN = 'geometrydash-lite.poki2.online'

GAMES = [
    ('geometry-dash-lite', 'geometry-dash-lite-game', 'Geometry Dash Lite', 'png'),
    ('danger-dash',        'danger-dash',              'Danger Dash',         'png'),
    ('geometry-dash-astral-prism', 'geometry-dash-astral-prism', 'Geometry Dash Astral Prism', 'png'),
    ('geometry-dash-demon-park',   'geometry-dash-demon-park',   'Geometry Dash Demon Park',   'png'),
    ('geometry-dash-horror',       'geometry-dash-horror',       'Geometry Dash Horror',       'jpg'),
    ('geometry-dash-look-up',      'geometry-dash-look-up',      'Geometry Dash Look Up',      'png'),
    ('geometry-dash-megalodon',    'geometry-dash-megalodon',    'Geometry Dash Megalodon',    'png'),
    ('red-rush',                   'red-rush',                   'Red Rush',                   'png'),
    ('slope',                      'slope',                      'Slope',                      'png'),
]

font_paths = [
    '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
    '/System/Library/Fonts/Helvetica.ttc',
    '/Library/Fonts/Arial Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
]

def load_fonts():
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return (
                    ImageFont.truetype(fp, 72),
                    ImageFont.truetype(fp, 34),
                    ImageFont.truetype(fp, 26),
                )
            except Exception:
                continue
    d = ImageFont.load_default()
    return d, d, d

font_large, font_medium, font_small = load_fonts()

def make_og_cover(slug, thumb_base, game_name, thumb_ext):
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Gradient band at top
    for i in range(HEIGHT // 3):
        alpha = int(60 * (1 - i / (HEIGHT / 3)))
        draw.line([(0, i), (WIDTH, i)], fill=(10, 40, 25))

    # Accent bar top + bottom
    draw.rectangle([(0, 0), (WIDTH, 8)], fill=ACCENT)
    draw.rectangle([(0, HEIGHT - 8), (WIDTH, HEIGHT)], fill=ACCENT)

    # Load thumbnail, paste on right side
    thumb_path = f'data/image/game/{slug}/{thumb_base}-m186x186.{thumb_ext}'
    if os.path.exists(thumb_path):
        thumb = Image.open(thumb_path).convert('RGBA')
        # Resize to fit a 300x300 area
        thumb.thumbnail((300, 300), Image.LANCZOS)
        tw, th = thumb.size
        paste_x = WIDTH - tw - 80
        paste_y = (HEIGHT - th) // 2
        img.paste(thumb, (paste_x, paste_y), mask=thumb.split()[3] if thumb.mode == 'RGBA' else None)

    # Text area on left side
    text_max_x = WIDTH - 420

    # Game name (possibly wrap)
    words = game_name.split()
    lines = []
    line = ''
    for word in words:
        test = (line + ' ' + word).strip()
        bbox = draw.textbbox((0, 0), test, font=font_large)
        if bbox[2] - bbox[0] > text_max_x - 80:
            if line:
                lines.append(line)
            line = word
        else:
            line = test
    if line:
        lines.append(line)

    total_h = sum(draw.textbbox((0, 0), l, font=font_large)[3] - draw.textbbox((0, 0), l, font=font_large)[1] + 12 for l in lines)
    y = (HEIGHT - total_h - 80) // 2
    for ln in lines:
        bbox = draw.textbbox((0, 0), ln, font=font_large)
        draw.text((80, y), ln, font=font_large, fill=TEXT_COLOR)
        y += bbox[3] - bbox[1] + 12

    # Subtitle
    sub = 'Play Unblocked Free Online'
    draw.text((80, y + 18), sub, font=font_medium, fill=ACCENT)

    # Domain
    dom_bbox = draw.textbbox((0, 0), DOMAIN, font=font_small)
    draw.text((80, HEIGHT - 50), DOMAIN, font=font_small, fill=SUB_COLOR)

    # Decorative circle
    draw.ellipse([(1050, 20), (1150, 120)], outline=ACCENT, width=2)

    out_path = f'data/image/game/{slug}/{slug}-og.png'
    img.save(out_path, 'PNG', optimize=True)
    print(f'  Generated {out_path}')

if __name__ == '__main__':
    print('Generating 1200x630 og covers...')
    for slug, thumb_base, game_name, thumb_ext in GAMES:
        make_og_cover(slug, thumb_base, game_name, thumb_ext)
    print('Done.')

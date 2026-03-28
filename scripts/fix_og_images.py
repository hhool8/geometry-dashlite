"""Fix og:image and image_src refs to use generated 1200x630 -og.png files."""
fixes = {
    "index.html": ("geometry-dash-lite", "geometry-dash-lite-game.png", "geometry-dash-lite-og.png"),
    "danger-dash.html": ("danger-dash", "danger-dash.png", "danger-dash-og.png"),
    "geometry-dash-astral-prism.html": ("geometry-dash-astral-prism", "geometry-dash-astral-prism.png", "geometry-dash-astral-prism-og.png"),
    "geometry-dash-demon-park.html": ("geometry-dash-demon-park", "geometry-dash-demon-park.png", "geometry-dash-demon-park-og.png"),
    "geometry-dash-horror.html": ("geometry-dash-horror", "geometry-dash-horror.jpg", "geometry-dash-horror-og.png"),
    "geometry-dash-look-up.html": ("geometry-dash-look-up", "geometry-dash-look-up.png", "geometry-dash-look-up-og.png"),
    "geometry-dash-megalodon.html": ("geometry-dash-megalodon", "geometry-dash-megalodon.png", "geometry-dash-megalodon-og.png"),
    "red-rush.html": ("red-rush", "red-rush.png", "red-rush-og.png"),
    "slope.html": ("slope", "slope.png", "slope-og.png"),
}

for fname, (slug, old_img, new_img) in fixes.items():
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    base_url = f"https://geometrydash-lite.poki2.online/data/image/game/{slug}/"
    old_full = base_url + old_img
    new_full = base_url + new_img
    count = content.count(old_full)
    new_content = content.replace(old_full, new_full)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"{fname}: replaced {count} occurrences of '{old_img}' -> '{new_img}'")

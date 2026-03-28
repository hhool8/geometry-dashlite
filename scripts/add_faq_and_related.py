"""Add visible FAQ section to index.html and related-games sections to all 9 game pages."""

# Game metadata: (html_file, slug, title, thumb_ext)
GAMES = [
    ("index.html",                      "geometry-dash-lite",         "Geometry Dash Lite",         "png"),
    ("danger-dash.html",                "danger-dash",                "Danger Dash",                "png"),
    ("geometry-dash-astral-prism.html", "geometry-dash-astral-prism", "Geometry Dash Astral Prism", "png"),
    ("geometry-dash-demon-park.html",   "geometry-dash-demon-park",   "Geometry Dash Demon Park",   "png"),
    ("geometry-dash-horror.html",       "geometry-dash-horror",       "Geometry Dash Horror",       "jpg"),
    ("geometry-dash-look-up.html",      "geometry-dash-look-up",      "Geometry Dash Look Up",      "png"),
    ("geometry-dash-megalodon.html",    "geometry-dash-megalodon",    "Geometry Dash Megalodon",    "png"),
    ("red-rush.html",                   "red-rush",                   "Red Rush",                   "png"),
    ("slope.html",                      "slope",                      "Slope",                      "png"),
]

BASE = "https://geometrydash-lite.poki2.online"

FAQ_HTML = (
    '<section id="faq" class="max-w-7xl mx-auto px-3 md:px-10 py-8">'
    '<h2 class="text-2xl font-bold mb-4 text-gray-900 dark:text-white">Frequently Asked Questions</h2>'
    '<div class="space-y-3">'

    '<details class="bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 overflow-hidden" '
              'itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">'
    '<summary class="px-5 py-4 font-semibold cursor-pointer text-gray-900 dark:text-white" itemprop="name">'
        'Is Geometry Dash Lite free to play?'
    '</summary>'
    '<div class="px-5 pb-4 text-gray-600 dark:text-gray-300" '
         'itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">'
        '<p itemprop="text">Yes, Geometry Dash Lite is completely free to play in your browser. '
        'No download, no registration, no payment required.</p>'
    '</div>'
    '</details>'

    '<details class="bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 overflow-hidden" '
              'itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">'
    '<summary class="px-5 py-4 font-semibold cursor-pointer text-gray-900 dark:text-white" itemprop="name">'
        'Can I play Geometry Dash Lite unblocked at school?'
    '</summary>'
    '<div class="px-5 pb-4 text-gray-600 dark:text-gray-300" '
         'itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">'
        '<p itemprop="text">Yes! Geometry Dash Lite on this site is unblocked and works on most school networks '
        'and Chromebooks. Just open the page and start playing.</p>'
    '</div>'
    '</details>'

    '<details class="bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 overflow-hidden" '
              'itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">'
    '<summary class="px-5 py-4 font-semibold cursor-pointer text-gray-900 dark:text-white" itemprop="name">'
        'Do I need to install anything to play Geometry Dash Lite?'
    '</summary>'
    '<div class="px-5 pb-4 text-gray-600 dark:text-gray-300" '
         'itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">'
        '<p itemprop="text">No installation needed. Geometry Dash Lite runs directly in your web browser '
        'on any device &mdash; desktop, laptop, tablet, or Chromebook.</p>'
    '</div>'
    '</details>'

    '<details class="bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 overflow-hidden" '
              'itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">'
    '<summary class="px-5 py-4 font-semibold cursor-pointer text-gray-900 dark:text-white" itemprop="name">'
        'What is Geometry Dash Lite?'
    '</summary>'
    '<div class="px-5 pb-4 text-gray-600 dark:text-gray-300" '
         'itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">'
        '<p itemprop="text">Geometry Dash Lite is a rhythm-based platformer where you control a cube or ship '
        'through obstacles in time with music. It is the free version of the popular Geometry Dash game.</p>'
    '</div>'
    '</details>'

    '<details class="bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 overflow-hidden" '
              'itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">'
    '<summary class="px-5 py-4 font-semibold cursor-pointer text-gray-900 dark:text-white" itemprop="name">'
        'How many levels are in Geometry Dash Lite?'
    '</summary>'
    '<div class="px-5 pb-4 text-gray-600 dark:text-gray-300" '
         'itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">'
        '<p itemprop="text">The original Geometry Dash Lite includes several official levels and an online level '
        'browser. On this site you can also play additional fan-made Geometry Dash games like '
        'Astral Prism, Demon Park, Horror, and more.</p>'
    '</div>'
    '</details>'

    '</div>'
    '</section>'
)


def make_related_html(current_slug):
    """Return HTML for a 'More Games' section, using 4 games that are not the current game."""
    others = [(f, s, t, e) for f, s, t, e in GAMES if s != current_slug][:4]
    cards = ""
    for f, s, t, e in others:
        href = BASE + ("/" if s != "geometry-dash-lite" else "")
        if s != "geometry-dash-lite":
            href += s.lstrip("/")
        else:
            href = BASE
        thumb = f"{BASE}/data/image/game/{s}/{s}-m186x186.{e}"
        cards += (
            f'<a href="{href}" class="flex flex-col items-center gap-2 group">'
            f'<img src="{thumb}" alt="{t}" width="80" height="80" '
            f'class="rounded-lg object-cover group-hover:scale-105 transition-transform duration-200" loading="lazy">'
            f'<span class="text-xs text-center font-medium text-gray-700 dark:text-gray-200 group-hover:text-green-500">{t}</span>'
            f'</a>'
        )
    return (
        '<section id="more-games" class="max-w-7xl mx-auto px-3 md:px-10 py-8">'
        '<h2 class="text-xl font-bold mb-4 text-gray-900 dark:text-white">More Games You May Like</h2>'
        '<div class="flex flex-wrap gap-4">'
        + cards +
        '</div>'
        '</section>'
    )


def insert_before_footer(content, html):
    """Insert html just before the first <footer tag."""
    idx = content.find('<footer')
    if idx == -1:
        # Fallback: before </body>
        idx = content.rfind('</body>')
    return content[:idx] + html + content[idx:]


for fname, slug, title, ext in GAMES:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content

    # Add FAQ only on homepage
    if fname == "index.html":
        if 'id="faq"' not in new_content:
            new_content = insert_before_footer(new_content, FAQ_HTML)
            print(f"  {fname}: inserted FAQ section")
        else:
            print(f"  {fname}: FAQ section already present, skipped")

    # Add related games to all pages
    if 'id="more-games"' not in new_content:
        related_html = make_related_html(slug)
        new_content = insert_before_footer(new_content, related_html)
        print(f"  {fname}: inserted related games section")
    else:
        print(f"  {fname}: related games already present, skipped")

    if new_content != content:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(new_content)

print("Done.")

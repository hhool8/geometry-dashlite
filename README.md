# Geometry Dash Lite — geometrydash-lite.poki2.online

Free unblocked H5 rhythm platformer game site hosted on GitHub Pages.
Live: **https://geometrydash-lite.poki2.online**

---

## Quick Start

```bash
# Migrate to a new domain (updates all HTML, sitemap, robots.txt, scripts)
bash scripts/set-domain.sh your-new-domain.com

# Run full SEO audit (outputs docs/seo-audit-report.md)
python3 scripts/seo_verify.py
```

---

## Site Structure

| Path | Description |
|---|---|
| `index.html` | Homepage — Geometry Dash Lite (main game) |
| `danger-dash.html` … `slope.html` | 8 additional game pages with VideoGame JSON-LD schema |
| `about-us.html` … `404.html` | 7 support / legal pages |
| `robots.txt` | Allows all; points to sitemap |
| `sitemap.xml` | 15 URLs with priorities and dynamic lastmod (git-based) |
| `og-cover.png` | 1200×630 brand cover image for og:image / Twitter Card |
| `data/image/game/` | 9 game thumbnails (186×186 PNG/JPG) for og:image / twitter:image |
| `.domain` | Active domain used by `set-domain.sh` |

---

## Scripts

| Script | Purpose |
|---|---|
| `scripts/set-domain.sh` | One-command domain migration — replaces domain in all HTML/xml/py files |
| `scripts/fix_github_io_links.py` | Replace residual github.io refs across all pages |
| `scripts/fix_meta_tags.py` | Update title / H1 / meta description / keywords on all game pages |
| `scripts/add_schema.py` | Inject VideoGame JSON-LD schema into all 9 game pages |
| `scripts/add_homepage_schema.py` | Inject WebSite + FAQPage JSON-LD into index.html |
| `scripts/seo_offpage.py` | Add Twitter Card meta tags to all 16 pages |
| `scripts/add_cwv_tracking.py` | Inject Core Web Vitals (LCP/CLS/INP) GA4 events on game pages |
| `scripts/copy_game_thumbs.py` | Copy cache thumbnails → data/image/game/ |
| `scripts/gen_og_cover.py` | Generate 1200×630 og-cover.png (Pillow; requires `.venv`) |
| `scripts/gen_sitemap.py` | Regenerate sitemap.xml with lastmod from `git log` per file |
| `scripts/fix_support_pages.py` | Fix og:image / title / canonical on support pages |
| `scripts/seo_verify.py` | Full per-page SEO tag audit → `docs/seo-audit-report.md` |

---

## Target Keywords

| Keyword | Priority | Target Rank |
|---|---|---|
| Geometry Dash Lite | P1 | Top 5 |
| Geometry Dash unblocked | P1 | Top 5 |
| Geometry Dash free online | P2 | Top 10 |
| Geometry Dash school / Chromebook | P2 | Top 10 |
| Slope unblocked | P3 | Top 20 |

---

## Monitoring

| Check | Tool | Frequency |
|---|---|---|
| Indexing coverage | `site:geometrydash-lite.poki2.online` in Google | Weekly |
| Keyword rankings | GSC → Performance → Queries | Weekly |
| Core Web Vitals | GSC → Core Web Vitals / GA4 custom events | Monthly |
| PageSpeed | https://pagespeed.web.dev/?url=https://geometrydash-lite.poki2.online | Monthly |
| Schema validity | https://search.google.com/test/rich-results?url=https://geometrydash-lite.poki2.online | After schema changes |

---

## Work Status (2026-03-27 — Session 1)

### ✅ Completed

| Area | Detail |
|---|---|
| Domain migration | All `geometry-dashlite.github.io` refs replaced with `geometrydash-lite.poki2.online` across all 16 pages (~100+ replacements) |
| Title / H1 / Meta description / Keywords | Updated on all 9 game pages with target keywords |
| VideoGame JSON-LD schema | Injected on all 9 game pages (index + 8 games); geometry-dash-horror uses `.jpg` thumbnail |
| WebSite + FAQPage JSON-LD schema | Injected on `index.html`; 5 FAQ items targeting "unblocked / free / school / Chromebook" |
| Twitter Card meta tags | Injected on all 16 pages (`@geometrydashlite`) |
| Core Web Vitals tracking | LCP / CLS / INP PerformanceObserver + GA4 events on all 9 game pages |
| Game thumbnails | 9 thumbnails copied from `cache/` → `data/image/game/` |
| `og-cover.png` | 1200×630 brand image generated for homepage og:image / Twitter Card |
| `robots.txt` | Created at repo root; points to sitemap |
| `sitemap.xml` | 15 URLs with `priority`, `changefreq`, dynamic `lastmod` from `git log` |
| All scripts | 12 reusable Python/bash scripts committed to `scripts/` |
| SEO audit | **CRITICAL: 0 / WARNING: 0** — all 16 pages pass (`docs/seo-audit-report.md`) |
| Committed & pushed | Commit `0a9f837` → `hhool8/geometry-dashlite` main |

### ⚠️ Needs Refinement

| Item | Current State | Next Step |
|---|---|---|
| Game page og:image size | 186×186 px thumbnails on 9 game pages | Replace `data/image/game/*/` files with 1200×630 versions when high-res art is available — no HTML changes needed |
| Internal cross-linking | Footer + nav links only | Add 3–5 "Related Games" links on each game detail page to improve crawl depth and dwell time |
| Search functionality | Not implemented | Add client-side game search / filter |
| FAQ section (homepage) | 5 FAQ items present in JSON-LD schema only | Render FAQ as visible HTML section on page for user engagement |

### ❌ Not Started — Manual Off-Page Actions Only

| Priority | Task |
|---|---|
| 🔴 High | Submit to CrazyGames, itch.io, Newgrounds, Poki |
| 🔴 High | Reddit posts: r/WebGames, r/geometrydash, r/teenagers |
| 🟡 Medium | Create @geometrydashlite social accounts (Twitter/X, Facebook, Instagram) |
| 🟡 Medium | Link exchange outreach with similar GitHub Pages unblocked game sites |
| 🟢 Low | YouTube gameplay walkthroughs (organic backlink source) |
| 🟢 Low | GSC submission: submit sitemap at https://search.google.com/search-console |


---

## Work Status Update — 2026-03-28 (Session 2)

### Code Walkthrough Findings

A full code audit of the repository (run via `scripts/seo_verify.py`) revealed one critical silent bug and three missing features:

| Finding | Severity | Root Cause |
|---|---|---|
| `og:image` on all 9 game pages pointed to non-existent files | CRITICAL | HTML used `{slug}.png` but disk had `{slug}-m186x186.{ext}`; `seo_verify.py` only checked the domain prefix, not disk existence |
| `seo_verify.py` false-positive audit | HIGH | Missing file-existence check allowed broken og:image refs to pass silently |
| FAQ visible only in JSON-LD schema | MEDIUM | Schema was correct but no rendered HTML — users saw nothing |
| No related games / internal cross-links | MEDIUM | Only footer and nav links existed between game pages |

---

### Completed in This Session

| Task | Details |
|---|---|
| Generated 1200x630 per-game og covers | `scripts/gen_game_og_covers.py` executed; 9 `{slug}-og.png` files written to `data/image/game/{slug}/` |
| Fixed `og:image` refs on all 9 pages | `scripts/fix_og_images.py` — replaced broken `{slug}.png` with `{slug}-og.png`; also fixed `link rel="image_src"` |
| Added visible FAQ section to homepage | 5 `<details>/<summary>` accordion items with microdata markup inserted before `<footer>` in `index.html` |
| Added "More Games" related section to all 9 pages | 4 game cards (thumbnail + title + link) inserted before `<footer>` on each game page via `scripts/add_faq_and_related.py` |
| Upgraded `seo_verify.py` audit | Added `og_image_file_exists()` — strips domain prefix from og:image URL and calls `os.path.exists()` on the relative path; raises CRITICAL if file is missing |
| Verified clean audit | `seo_verify.py` result: CRITICAL 0 / WARNING 0 / INFO 0 after all fixes |

Scripts added this session: `scripts/fix_og_images.py`, `scripts/add_faq_and_related.py`

---

### Needs Refinement

| Item | Current State | Next Step |
|---|---|---|
| Per-game og cover art | Generated covers use 186x186 thumbnail + text overlay on dark background; functional but not high-fidelity | Replace `{slug}-og.png` when official 1200x630 game art is available (no HTML changes needed) |
| Related games section | 4 static cards per page (alphabetically first 4 other games) | Tag/genre-based recommendations when game catalog grows |

### Not Started — Manual Off-Page Actions Only

| Priority | Task |
|---|---|
| High | Submit to CrazyGames, itch.io, Newgrounds, Poki |
| High | Reddit posts: r/WebGames, r/geometrydash, r/teenagers |
| Medium | Create @geometrydashlite social accounts (Twitter/X, Facebook, Instagram) |
| Medium | Link exchange outreach with similar unblocked game sites |
| Low | YouTube gameplay walkthroughs (organic backlink source) |
| Low | GSC sitemap submission: https://search.google.com/search-console |

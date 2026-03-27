# SEO Plan for geometrydash-lite.poki2.online

**Site:** https://geometrydash-lite.poki2.online  
**Repo:** hhool8/geometry-dashlite  
**Audit Date:** 2026-03-27  
**GA4:** G-2F54CGWRGW  

---

## Objective

Boost Google rankings for geometrydash-lite.poki2.online targeting:

| Keyword | Est. Monthly Searches | Competition | Priority |
|---|---|---|---|
| geometry dash lite | 100K+ | High | P1 — Primary |
| geometry dash unblocked | 50K+ | Medium | P1 — Primary |
| geometry dash free | 50K+ | Medium | P1 — Primary |
| unblocked geometry dash | 10K–50K | Medium-Low | P2 — Secondary |
| geometry dash online | 10K–50K | Medium | P2 — Secondary |
| geometry dash astral prism | 5K–10K | Low | P2 — Secondary |
| geometry dash megalodon | 5K–10K | Low | P2 — Secondary |
| geometry dash horror | 5K–10K | Low | P3 — Long-tail |
| geometry dash demon park | 5K–10K | Low | P3 — Long-tail |

**Rationale:** "Geometry Dash" brand terms have high volume and a natural fit for this site. Game-specific level names (astral prism, megalodon, horror) are low-competition long-tail opportunities with dedicated fan communities.

---

## 1. Current State Audit (2026-03-27)

### Site Structure
- **16 HTML pages** total: 9 game pages + 7 support pages
- **Game pages:** index.html, danger-dash.html, geometry-dash-astral-prism.html, geometry-dash-demon-park.html, geometry-dash-horror.html, geometry-dash-look-up.html, geometry-dash-megalodon.html, red-rush.html, slope.html

### Gap Analysis

| Area | Status | Issue |
|---|---|---|
| Title tag | ⚠️ Weak | `Geometry Dash Lite` — missing "unblocked" / "free" / "online" keywords |
| Meta description | ⚠️ Weak | Present but lacks P1 keywords ("unblocked", "free") |
| Meta keywords | ⚠️ Minimal | Only `geometry dash lite` — missing all other target terms |
| H1 | ⚠️ Weak | `Geometry Dash Lite` — same as title, no differentiating keywords |
| Canonical URL | ❌ Wrong | Points to `https://geometry-dashlite.github.io` (old domain) |
| og:url | ❌ Wrong | Points to `github.io` on index and favorite pages |
| og:image | ❌ Wrong | Points to `geometry-dashlite.github.io/...` (404s externally) |
| twitter:card | ❌ Missing | No Twitter Card meta tags on any of 16 pages |
| JSON-LD schema | ❌ Missing | No VideoGame / WebSite / FAQPage schema on any page |
| robots.txt | ❌ Missing | No robots.txt at root |
| sitemap.xml | ❌ Missing | No sitemap |
| github.io refs | ❌ 100+ | All 16 pages contain `geometry-dashlite.github.io` refs |
| Domain config | ❌ Missing | No `.domain` file; no migration script |
| GA4 | ✅ Present | G-2F54CGWRGW (verify coverage on all pages) |
| GSC verification | ✅ Present | `google-site-verification` meta tag on index.html |
| FAQ / keyword content | ❌ Missing | No unblocked games FAQ section |
| Core Web Vitals tracking | ❌ Missing | No CWV custom events |
| Font | ⚠️ Check | Verify no Google Fonts remote dependency |
| Game thumbnails | ⚠️ Check | og:image refs broken; need local copies |
| OG cover image | ❌ Missing | No 1200×630 brand cover for homepage |

---

## 2. On-Page Optimization Plan

### 2.1 Domain & github.io Cleanup ❌ → Target: ✅

**Priority: CRITICAL — all other work depends on this**

- Create `.domain` file: `geometrydash-lite.poki2.online`
- Write `scripts/set-domain.sh` for full-depth domain migration
- Replace all `geometry-dashlite.github.io` refs → `geometrydash-lite.poki2.online` across all 16 pages, embed/, game/ dirs
- Fix canonical URLs: relative paths → absolute `https://geometrydash-lite.poki2.online/...`
- Fix og:url on all pages
- Fix og:image on all pages (point to local assets)

### 2.2 Title / H1 / Meta Optimization ❌ → Target: ✅

**Homepage (index.html):**
- Title: `Geometry Dash Lite Unblocked - Play Free Online | Geometry Dash`
- H1: `Geometry Dash Lite Unblocked`
- Meta description: include "geometry dash lite", "unblocked", "free online", "geometry dash"
- Meta keywords: add all P1/P2/P3 terms

**Game pages (e.g. geometry-dash-astral-prism.html):**
- Title pattern: `{Game Name} - Geometry Dash Unblocked | Play Free`
- H1: `{Game Name} Unblocked`
- Description: original description per game mentioning "geometry dash" and "unblocked"

### 2.3 robots.txt + sitemap.xml ❌ → Target: ✅

**robots.txt:**
```
User-agent: *
Disallow: /embed/
Sitemap: https://geometrydash-lite.poki2.online/sitemap.xml
```

**sitemap.xml:**
- Include all 16+ pages with `<priority>` weights
- Dynamic `<lastmod>` from `git log -1 --format=%ci <file>` per file
- Script: `scripts/gen_sitemap.py`

### 2.4 Structured Data / Schema ❌ → Target: ✅

**Game pages (9 pages):** `VideoGame` JSON-LD
```json
{
  "@type": "VideoGame",
  "name": "{Game Name}",
  "description": "...",
  "url": "https://geometrydash-lite.poki2.online/{slug}",
  "image": "https://geometrydash-lite.poki2.online/data/image/game/.../thumb.png",
  "genre": "Platformer",
  "playMode": "SinglePlayer",
  "gamePlatform": "Web Browser",
  "applicationCategory": "Game",
  "operatingSystem": "Any"
}
```

**Homepage:** `WebSite` + `FAQPage` JSON-LD
- `WebSite` with `SearchAction` → enables Sitelinks SearchBox
- `FAQPage` with 4 questions covering P1/P2 keywords — enables FAQ Rich Result

### 2.5 Twitter Card + OG Tags ❌ → Target: ✅

Add to all 16 pages:
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">
<meta name="twitter:description" content="...">
<meta name="twitter:image" content="https://geometrydash-lite.poki2.online/data/image/options/og-cover.png">
<meta name="twitter:site" content="@geometrydashlite">
```

### 2.6 OG Cover Image ❌ → Target: ✅

- Generate `data/image/options/og-cover.png` at 1200×630
- Dark game-themed background + game screenshot + brand text "Geometry Dash Lite"
- Script: `scripts/gen_og_cover.py` (Pillow, use `.venv`)
- Use on homepage og:image / twitter:image

### 2.7 Game Thumbnails ❌ → Target: ✅

- Copy local thumbnails from `cache/data/image/game/` → `data/image/game/`
- Update all `og:image` / `twitter:image` HTML refs to local paths
- Script: `scripts/copy_game_thumbs.py`

### 2.8 FAQ / Unblocked Content Section ❌ → Target: ✅

Add to homepage `index.html`:
```html
<section>
  <h2>Why Play Geometry Dash Lite Unblocked Here?</h2>
  <dl>
    <dt>Is Geometry Dash Lite free to play?</dt>
    <dd>Yes — fully free, no download needed...</dd>
    <dt>Is this an unblocked version of Geometry Dash?</dt>
    <dd>Yes — works at school and office...</dd>
    <dt>How is this different from Geometry Dash 2.2?</dt>
    <dd>...</dd>
    <dt>What is Geometry Dash Astral Prism?</dt>
    <dd>...</dd>
  </dl>
</section>
```

### 2.9 Core Web Vitals Tracking ❌ → Target: ✅

- Inject LCP / CLS / INP reporting as GA4 custom events on all pages
- Script: `scripts/add_cwv_tracking.py`

### 2.10 Font Audit ⚠️ → Target: ✅

- Verify no remote Google Fonts calls (latency / privacy)
- If present: download subset woff2 and self-host

---

## 3. Off-Page Optimization

### 3.1 Technical Setup (scripts)

| Task | Script | Status |
|---|---|---|
| Twitter Card meta tags on all pages | `scripts/seo_offpage.py` | ❌ |
| Share modal URL fix | `scripts/seo_offpage.py` | ❌ |
| Off-page action guide | `docs/off-page-guide.md` | ❌ |

### 3.2 Manual Actions (owner)

| Priority | Task |
|---|---|
| 🔴 High | Submit to CrazyGames, itch.io, Newgrounds, Poki |
| 🔴 High | Reddit posts: r/geometrydash, r/WebGames, r/teenagers |
| 🟡 Medium | Create @geometrydashlite on Twitter/X |
| 🟡 Medium | Link exchange: contact geometrylite.poki2.online, similar GitHub Pages sites |
| 🟢 Low | YouTube gameplay videos (organic backlinks) |

---

## 4. Monitoring & Adjustment

| Task | Tool | Frequency |
|---|---|---|
| Google indexing | `site:geometrydash-lite.poki2.online` | Weekly |
| Keyword rankings | GSC → Performance → Queries | Weekly |
| Request indexing | GSC → URL Inspection → Request Indexing | On each deploy |
| Submit sitemap | GSC → Sitemaps | On sitemap change |
| Rich Results | [Rich Results Test](https://search.google.com/test/rich-results?url=https%3A%2F%2Fgeometrydash-lite.poki2.online) | After schema changes |
| PageSpeed | [PageSpeed Insights](https://pagespeed.web.dev/?url=https%3A%2F%2Fgeometrydash-lite.poki2.online) | Monthly |
| CWV field data | GSC → Core Web Vitals | Monthly |
| Mobile-Friendly | [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly?url=https%3A%2F%2Fgeometrydash-lite.poki2.online) | On layout changes |

---

## 5. Implementation Checklist

### Phase 1 — Critical Fixes (do first)
- [ ] Create `.domain` file
- [ ] Write `scripts/set-domain.sh` (from geometrylite template)
- [ ] Run domain migration: replace all `github.io` refs
- [ ] Fix canonical + og:url → absolute `poki2.online` URLs
- [ ] Create `robots.txt`
- [ ] Generate `sitemap.xml` (via `scripts/gen_sitemap.py`)

### Phase 2 — On-Page SEO
- [ ] Update title / H1 / meta desc / keywords on homepage
- [ ] Update title / H1 / meta desc on all 8 game pages
- [ ] Add VideoGame JSON-LD schema on all 9 game pages
- [ ] Add WebSite + FAQPage JSON-LD on homepage
- [ ] Add Twitter Card meta tags on all 16 pages
- [ ] Add FAQ "unblocked" content section to homepage
- [ ] Fix og:image refs → local paths

### Phase 3 — Assets & Tracking
- [ ] Copy game thumbnails from cache/ → data/image/game/
- [ ] Generate 1200×630 og-cover.png (via `scripts/gen_og_cover.py`)
- [ ] Audit & fix font loading (self-host if needed)
- [ ] Inject CWV (LCP/CLS/INP) GA4 event tracking

### Phase 4 — Verification
- [ ] Run `python3 scripts/seo_verify.py` — all pages pass
- [ ] Google Rich Results Test
- [ ] GSC sitemap submission
- [ ] Manual: `site:geometrydash-lite.poki2.online` indexing check

### Phase 5 — Off-Page (manual)
- [ ] Directory submissions
- [ ] Reddit posts
- [ ] Social account creation

---

## 6. Relevant Files (target state)

### Site Pages
- `index.html` — Homepage; VideoGame + WebSite + FAQPage schema, full keyword coverage
- `geometry-dash-astral-prism.html`, `geometry-dash-demon-park.html`, `geometry-dash-horror.html`, `geometry-dash-look-up.html`, `geometry-dash-megalodon.html` — Level-specific game pages with VideoGame schema
- `danger-dash.html`, `red-rush.html`, `slope.html` — Other game pages with VideoGame schema
- `about-us.html`, `contact-us.html`, `dmca.html`, `privacy-policy.html`, `terms-of-service.html`, `404.html`, `favorite.html` — Support pages with canonical + Twitter Card

### Scripts (to create)
| Script | Purpose |
|---|---|
| `scripts/set-domain.sh` | Full-depth domain migration |
| `scripts/add_schema.py` | Inject VideoGame JSON-LD on all game pages |
| `scripts/add_homepage_schema.py` | Inject WebSite + FAQPage JSON-LD on homepage |
| `scripts/seo_offpage.py` | Add Twitter Card meta tags + fix share URLs |
| `scripts/add_cwv_tracking.py` | Inject CWV GA4 event tracking |
| `scripts/fix_support_pages.py` | Fix canonical + og:url on support pages |
| `scripts/fix_github_io_links.py` | Replace residual github.io refs |
| `scripts/gen_og_cover.py` | Generate 1200×630 og-cover.png (Pillow) |
| `scripts/gen_sitemap.py` | Generate sitemap.xml with git-based lastmod |
| `scripts/copy_game_thumbs.py` | Copy cache/ thumbnails → data/image/game/ |
| `scripts/seo_verify.py` | Full SEO audit → docs/seo-audit-report.md |

### Docs (to create)
- `docs/off-page-guide.md` — Directory submission list, Reddit/social targets, outreach templates
- `docs/seo-audit-report.md` — Generated by `seo_verify.py`

---

## 7. Decisions

| Decision | Rationale |
|---|---|
| Focus on "geometry dash" brand terms + level names | Natural brand fit; level names (astral prism, megalodon) are low-competition long-tail with loyal fan bases |
| VideoGame JSON-LD on all game pages | Most competitors lack structured data — Rich Results eligibility is a differentiator |
| Absolute canonical on every page | Prevents Google treating github.io and poki2.online as duplicate content |
| Dynamic sitemap lastmod via `git log` | More accurate freshness signals to Googlebot |
| Domain config via `.domain` + `set-domain.sh` | Zero-friction future domain changes |
| Original descriptions per game | Avoid duplicate content penalty from upstream text |
| Reuse geometrylite scripts as templates | Same stack, proven approach, faster implementation |

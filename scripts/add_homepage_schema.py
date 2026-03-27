#!/usr/bin/env python3
"""
add_homepage_schema.py — Inject WebSite + FAQPage JSON-LD schema into index.html.
Run from repo root: python3 scripts/add_homepage_schema.py
"""

DOMAIN = 'https://geometrydash-lite.poki2.online'

# Anchor: after the VideoGame schema's closing </script>
# We look for the VideoGame schema block and insert after it
ANCHOR = '"@type": "VideoGame"'

WEBSITE_FAQ_SCHEMA = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Geometry Dash Lite",
  "url": "{DOMAIN}",
  "description": "Play Geometry Dash Lite and other rhythm platformers unblocked online for free. No download required.",
  "potentialAction": {{
    "@type": "SearchAction",
    "target": {{
      "@type": "EntryPoint",
      "urlTemplate": "{DOMAIN}/?q={{search_term_string}}"
    }},
    "query-input": "required name=search_term_string"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "Is Geometry Dash Lite free to play?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Yes, Geometry Dash Lite is completely free to play in your browser. No download, no registration, no payment required."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Can I play Geometry Dash Lite unblocked at school?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Yes! Geometry Dash Lite on this site is unblocked and works on most school networks and Chromebooks. Just open the page and start playing."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Do I need to install anything to play Geometry Dash Lite?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "No installation needed. Geometry Dash Lite runs directly in your web browser on any device — desktop, laptop, tablet, or Chromebook."
      }}
    }},
    {{
      "@type": "Question",
      "name": "What is Geometry Dash Lite?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Geometry Dash Lite is a rhythm-based platformer where you control a cube or ship through obstacles in time with music. It is the free version of the popular Geometry Dash game."
      }}
    }},
    {{
      "@type": "Question",
      "name": "How many levels are in Geometry Dash Lite?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "The original Geometry Dash Lite includes several official levels and an online level browser. On this site you can also play additional fan-made Geometry Dash games like Astral Prism, Demon Park, Horror, and more."
      }}
    }}
  ]
}}
</script>
'''

HOMEPAGE = 'index.html'

txt = open(HOMEPAGE, encoding='utf-8').read()

if '"@type": "WebSite"' in txt:
    print('WebSite schema already present in index.html — skipping.')
else:
    # Insert after the closing </script> tag that follows VideoGame schema
    import re
    # Find the VideoGame schema block and insert after its closing </script>
    pattern = r'(<script[^>]*>[\s\S]*?"@type":\s*"VideoGame"[\s\S]*?</script>)'
    m = re.search(pattern, txt)
    if m:
        insert_pos = m.end()
        txt = txt[:insert_pos] + '\n' + WEBSITE_FAQ_SCHEMA + txt[insert_pos:]
        open(HOMEPAGE, 'w', encoding='utf-8').write(txt)
        print('Injected WebSite + FAQPage schema into index.html')
    else:
        # Fallback: insert before </head>
        txt = txt.replace('</head>', WEBSITE_FAQ_SCHEMA + '</head>', 1)
        open(HOMEPAGE, 'w', encoding='utf-8').write(txt)
        print('Injected WebSite + FAQPage schema into index.html (before </head>)')

print('Done.')

#!/usr/bin/env python3
"""
add_cwv_tracking.py — Inject Core Web Vitals PerformanceObserver before </body>.
Run from repo root: python3 scripts/add_cwv_tracking.py
"""
import os, re

GA4_ID = 'G-2F54CGWRGW'

CWV_SCRIPT = f"""<!-- Core Web Vitals tracking -->
<script>
(function() {{
  var GA_ID = '{GA4_ID}';
  function sendToGA(metric, value, rating) {{
    if (typeof gtag === 'function') {{
      gtag('event', metric, {{
        event_category: 'Web Vitals',
        event_label: rating,
        value: Math.round(metric === 'CLS' ? value * 1000 : value),
        non_interaction: true
      }});
    }}
  }}
  // LCP
  try {{
    new PerformanceObserver(function(list) {{
      var entries = list.getEntries();
      var last = entries[entries.length - 1];
      var v = last.startTime;
      sendToGA('LCP', v, v < 2500 ? 'good' : v < 4000 ? 'needs-improvement' : 'poor');
    }}).observe({{type: 'largest-contentful-paint', buffered: true}});
  }} catch(e) {{}}
  // CLS
  try {{
    var clsValue = 0;
    new PerformanceObserver(function(list) {{
      list.getEntries().forEach(function(e) {{
        if (!e.hadRecentInput) clsValue += e.value;
      }});
      sendToGA('CLS', clsValue, clsValue < 0.1 ? 'good' : clsValue < 0.25 ? 'needs-improvement' : 'poor');
    }}).observe({{type: 'layout-shift', buffered: true}});
  }} catch(e) {{}}
  // INP (Interaction to Next Paint)
  try {{
    new PerformanceObserver(function(list) {{
      list.getEntries().forEach(function(e) {{
        if (e.duration && e.processingStart) {{
          var inp = e.processingStart - e.startTime + e.duration;
          sendToGA('INP', inp, inp < 200 ? 'good' : inp < 500 ? 'needs-improvement' : 'poor');
        }}
      }});
    }}).observe({{type: 'event', durationThreshold: 16, buffered: true}});
  }} catch(e) {{}}
}})();
</script>"""

GAME_PAGES = [
    'index.html',
    'danger-dash.html',
    'geometry-dash-astral-prism.html',
    'geometry-dash-demon-park.html',
    'geometry-dash-horror.html',
    'geometry-dash-look-up.html',
    'geometry-dash-megalodon.html',
    'red-rush.html',
    'slope.html',
]

for fname in GAME_PAGES:
    if not os.path.exists(fname):
        print(f'SKIP (not found): {fname}')
        continue

    txt = open(fname, encoding='utf-8').read()

    # Check GA4 presence
    if GA4_ID not in txt:
        print(f'  WARNING: GA4 id {GA4_ID} not found in {fname}')

    if 'Core Web Vitals tracking' in txt:
        print(f'  Already has CWV tracking: {fname}')
        continue

    if '</body>' not in txt:
        print(f'  WARNING: no </body> in {fname}')
        continue

    txt = txt.replace('</body>', CWV_SCRIPT + '\n</body>', 1)
    open(fname, 'w', encoding='utf-8').write(txt)
    print(f'Injected CWV tracking: {fname}')

print('Done.')

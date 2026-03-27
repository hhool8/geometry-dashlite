#!/usr/bin/env bash
# set-domain.sh — Replace all absolute domain references in the site.
# Usage: ./scripts/set-domain.sh <new-domain>
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DOMAIN_FILE="$ROOT_DIR/.domain"

if [ $# -ne 1 ]; then
  echo "Usage: $0 <new-domain>"
  exit 1
fi

NEW_DOMAIN="$1"

if [ ! -f "$DOMAIN_FILE" ]; then
  echo "Error: .domain file not found at $DOMAIN_FILE"
  exit 1
fi

OLD_DOMAIN="$(cat "$DOMAIN_FILE" | tr -d '[:space:]')"

if [ "$OLD_DOMAIN" = "$NEW_DOMAIN" ]; then
  echo "Domain is already set to: $NEW_DOMAIN — no changes needed."
  exit 0
fi

echo "Replacing: https://$OLD_DOMAIN  →  https://$NEW_DOMAIN"

FILES=$(find "$ROOT_DIR" \
  \( -name "*.html" -o -name "sitemap.xml" -o -name "robots.txt" -o -name "CNAME" -o -name "*.py" \) \
  -not -path "*/.git/*" \
  -not -path "*/cache/*" \
  -not -path "*/node_modules/*")

COUNT=0
for f in $FILES; do
  if grep -q "$OLD_DOMAIN" "$f" 2>/dev/null; then
    sed -i '' "s|${OLD_DOMAIN}|${NEW_DOMAIN}|g" "$f"
    echo "  Updated: ${f#$ROOT_DIR/}"
    COUNT=$((COUNT + 1))
  fi
done

CNAME_FILE="$ROOT_DIR/CNAME"
if [ -f "$CNAME_FILE" ]; then
  echo "$NEW_DOMAIN" > "$CNAME_FILE"
  echo "  Updated: CNAME → $NEW_DOMAIN"
fi

echo "$NEW_DOMAIN" > "$DOMAIN_FILE"
echo "Done. Updated $COUNT file(s). Active domain: $NEW_DOMAIN"

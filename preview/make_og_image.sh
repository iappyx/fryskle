#!/bin/bash
# Renders preview/og-image.html to og-image.jpg (1200x630), the link-preview image shown
# when Fryskle is shared (WhatsApp, Telegram, …). Needs Google Chrome.
set -euo pipefail
cd "$(dirname "$0")/.."
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CHROME" ] || { echo "Google Chrome not found at $CHROME"; exit 1; }
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1200,630 --virtual-time-budget=10000 \
  --screenshot="$PWD/og-image.tmp.png" "file://$PWD/preview/og-image.html" >/dev/null 2>&1
# JPEG keeps it small: WhatsApp may skip preview images larger than ~300 KB
sips -s format jpeg -s formatOptions 85 og-image.tmp.png --out og-image.jpg >/dev/null
rm og-image.tmp.png
echo "Wrote og-image.jpg ($(( $(stat -f%z og-image.jpg) / 1024 )) KB; keep it under ~300 KB)"

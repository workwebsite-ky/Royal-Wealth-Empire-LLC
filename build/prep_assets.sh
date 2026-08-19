#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Prepares every client-supplied photo / flyer / logo into web-ready assets.
# Source files: the original logo, banner, flyers and photos supplied by RWE.
# ---------------------------------------------------------------------------
set -e
SRC="${1:-/root/.claude/uploads/666f11c6-4bb8-5bc4-b9cd-957841b5ca37}"
OUT="$(cd "$(dirname "$0")/.." && pwd)/assets/img"
mkdir -p "$OUT"

LOGO="$SRC/b5c033cc-Logo.jpg"
PORTRAIT="$SRC/0344d699-CEO_Brittany.jpg"
FLYER_ABOUT="$SRC/08920a91-38ab295432cf4c229da4a89711fc104e.jpg"
BANNER="$SRC/390486c9-749651915_1704676854154584_9043455350580047633_n.jpg"
OFFICE="$SRC/5ec560af-640895635_1582335516388719_4787565694337042404_n.jpg"
FLYER_LAUNCH="$SRC/ad86b920-750569947_1704646410824295_662732543341172973_n.jpg"
FLYER_ENROLL="$SRC/cc21dbb6-776324757_1726557981966471_7274826689698236611_n.jpg"
FLYER_TEAM="$SRC/f9ab907a-751055686_1703750207580582_2452799965896973498_n.jpg"

# --- 1. Gold RWE + crown mark, background keyed out for dark headers --------
convert "$BANNER" -crop 300x205+25+18 +repage -resize 200% \
        \( +clone -colorspace Gray -level 6%,60% \) -alpha off \
        -compose CopyOpacity -composite \
        "$OUT/logo-mark.png"

# --- 2. Full marble crest (light backgrounds / brand plate) -----------------
convert "$LOGO" -resize 900x -quality 88 -strip "$OUT/logo-full.jpg"

# --- 3. Favicon: crest on the deep emerald brand tile -----------------------
convert -size 512x512 xc:'#0A2423' \
        \( "$OUT/logo-mark.png" -resize 380x \) -gravity center -composite \
        \( -size 512x512 xc:none -fill '#0A2423' -draw 'roundrectangle 0,0 511,511 90,90' \) \
        -alpha set -compose DstIn -composite \
        "$OUT/favicon.png"

# --- 4. Brittany — hero portrait (4:5) --------------------------------------
convert "$PORTRAIT" -gravity north -crop 768x960+0+40 +repage \
        -resize 900x -quality 88 -strip "$OUT/brittany-portrait.jpg"

# --- 5. Brittany — office photo, cropped to 4:5 -----------------------------
convert "$OFFICE" -crop 644x805+380+320 +repage \
        -resize 900x -quality 88 -strip "$OUT/brittany-office.jpg"

# --- 6. Flyers & banner, resized for the web -------------------------------
convert "$FLYER_ABOUT"  -resize 1000x -quality 86 -strip "$OUT/flyer-about.jpg"
convert "$FLYER_LAUNCH" -resize 1000x -quality 86 -strip "$OUT/flyer-launch.jpg"
convert "$FLYER_TEAM"   -resize 1000x -quality 86 -strip "$OUT/flyer-team.jpg"
convert "$FLYER_ENROLL" -resize 1000x -quality 86 -strip "$OUT/flyer-enrollment.jpg"
convert "$BANNER"       -resize 1800x -quality 86 -strip "$OUT/banner-wide.jpg"

# --- 7. Social share card built on the real banner --------------------------
convert "$BANNER" -resize 1200x -gravity center -crop 1200x630+0+0 +repage \
        -quality 88 -strip "$OUT/og-image.jpg"

echo "Assets prepared in $OUT"
ls -la "$OUT"

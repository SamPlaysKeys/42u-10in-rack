#!/usr/bin/env bash
# Scaffold a new part: model stub, README, and (optionally) the tracking issue.
#
#   ./scripts/new_part.sh 03-power pdu-mount-1u "1U PDU mount" bracket
#
# Creates models/<category>/<slug>/{README.md,<slug>.scad,<slug>.md}
# and prints the gh command to open the tracking issue.
set -euo pipefail

CATEGORY="${1:?usage: new_part.sh <category-dir> <slug> <title> [type]}"
SLUG="${2:?usage: new_part.sh <category-dir> <slug> <title> [type]}"
TITLE="${3:?usage: new_part.sh <category-dir> <slug> <title> [type]}"
TYPE="${4:-bracket}"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIR="$ROOT/models/$CATEGORY/$SLUG"

# OpenSCAD identifiers cannot contain hyphens, so the module name is sanitized
# while the filename keeps the hyphenated slug.
MODULE_NAME="$(echo "$SLUG" | tr '-' '_' | sed 's/^[0-9]/p&/')"

if [[ -e "$DIR" ]]; then
  echo "refusing to overwrite existing $DIR" >&2
  exit 1
fi
if [[ ! -d "$ROOT/models/$CATEGORY" ]]; then
  echo "no such category: models/$CATEGORY" >&2
  echo "available:" >&2
  ls -1 "$ROOT/models" >&2
  exit 1
fi

mkdir -p "$DIR"

cat > "$DIR/README.md" <<EOF
# $TITLE

| | |
| :--- | :--- |
| **Slug** | \`$SLUG\` |
| **Category** | \`$CATEGORY\` |
| **Type** | $TYPE |
| **Status** | Draft — not released for printing |
| **Material** | TBD (see ADR-0004) |
| **Print time** | — |
| **Filament** | — |

## Purpose

What this part holds, and what it bolts to. One or two sentences.

## Fits

| Device / target | Inventory ID | Notes |
| :--- | :--- | :--- |
| TBD | — | |

## Critical dimensions

Pull these from \`rack/params.json\`; do not retype them.

| Dimension | Value | Source |
| :--- | :--- | :--- |
| Hole centres, horizontal | 236.525 mm | \`width_hole_centres\` |
| Panel width | 254 mm | \`width_nominal_panel_width\` |
| Design envelope | 210 mm | \`width_design_envelope\` |
| U height | 44.45 mm | \`rack_unit_u_height\` |

## Print notes

Orientation, supports, perimeters, and anything that went wrong last time.

## Revision history

| Date | Change | Printed? |
| :--- | :--- | :--- |
| $(date +%Y-%m-%d) | Created | No |
EOF

cat > "$DIR/$SLUG.scad" <<'SCADEOF'
// __TITLE__
// Parametric source. Regenerate params with: python3 scripts/params_to_scad.py
include <../../openscad/params.scad>

/* [Parameters] */
// Add part-specific parameters here. Anything read from params.scad is already
// dimensioned - do not retype a spec number into this file.

/* [Hidden] */
$fn = 64;

module __SLUG__() {
  // TODO: model the part
  cube([width_design_envelope, rack_unit_u_height, 3]);
}

__SLUG__();
SCADEOF

# Substituted rather than expanded, so the SCAD variables survive the heredoc.
sed -i "s|__TITLE__|$TITLE|; s|__SLUG__|$MODULE_NAME|g" "$DIR/$SLUG.scad"

cat > "$DIR/$SLUG.md" <<EOF
# $TITLE — build notes

## Why it exists

## Design constraints

## Alternatives considered

## Open questions

- [ ]
EOF

echo "created models/$CATEGORY/$SLUG/"
echo
echo "Next:"
echo "  \$EDITOR models/$CATEGORY/$SLUG/$SLUG.scad"
echo
echo "Open the tracking issue with:"
echo "  gh issue create \\"
echo "    --title \"[part] $TITLE\" \\"
echo "    --label \"part,type:$TYPE,stage:idea\" \\"
echo "    --body \"Category: \\`$CATEGORY\\`  Slug: \\`$SLUG\\`\""

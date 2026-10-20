#!/usr/bin/env bash
# One-time GitHub setup: labels for the project board.
#
# Run from a clone, authenticated with `gh auth login`.
#   ./scripts/setup_github.sh
#
# Project board custom fields and views are created in the web UI; see
# docs/project-tracking.md for the exact list to add.
set -euo pipefail

command -v gh >/dev/null || { echo "gh CLI not found: https://cli.github.com" >&2; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "run: gh auth login" >&2; exit 1; }

REPO="${REPO:-SamPlaysKeys/42u-10in-rack}"
echo "Configuring labels on $REPO"

label() {
  local name="$1" color="$2" desc="$3"
  if gh label list --repo "$REPO" --limit 200 | grep -q "^${name}[[:space:]]"; then
    gh label edit "$name" --repo "$REPO" --color "$color" --description "$desc" >/dev/null
    echo "  updated  $name"
  else
    gh label create "$name" --repo "$REPO" --color "$color" --description "$desc" >/dev/null
    echo "  created  $name"
  fi
}

# Stage: where a part is in its life. Mirrors the board columns.
label "stage:idea"          "cfd3d7" "Idea captured, not yet specified"
label "stage:spec"          "bfd4f2" "Being specified: envelope, fit, constraints"
label "stage:modeling"      "c5def5" "CAD in progress"
label "stage:review"        "d4c5f9" "Modeled, needs a fit/design check"
label "stage:ready-to-print" "fbca04" "Validated, ready for a print job"
label "stage:printing"      "f9d0c4" "On the printer"
label "stage:printed"       "0e8a16" "Printed, not yet fitted"
label "stage:installed"     "006b75" "In the rack and working"

# Type: what kind of work item it is.
label "part"         "1d76db" "A 3D modelled part"
label "type:frame"   "5319e7" "Structural frame"
label "type:rail"    "3e1f79" "Rack rail"
label "type:power"   "b60205" "Power: PDU, UPS, bricks"
label "type:shelf"   "0052cc" "Shelf"
label "type:panel"   "006b75" "Blanking, vented or cable panel"
label "type:bracket" "c2e0c6" "Device-specific mount"
label "type:cable"   "fef2c0" "Cable management"
label "type:hardware" "d93f0b" "Non-printed hardware"
label "type:docs"    "ededed" "Documentation"
label "type:tooling" "bfdadc" "Jigs, coupons, calibration"

# Domain.
label "device"     "0e8a16" "A device going in the rack"
label "print-job"  "fbca04" "A batch of parts to print"
label "blocked"    "b60205" "Blocked on something else"
label "needs-measurement" "d4c5f9" "Waiting on a caliper reading"

echo
echo "Labels done. Next: create the Project board and fields - see docs/project-tracking.md"

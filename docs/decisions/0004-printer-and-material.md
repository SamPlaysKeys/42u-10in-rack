# ADR-0004: Printer and material

**Status:** Proposed
**Date:** 2026-10-20

## Context

The frame modules are the parts that decide the printer requirement, because they are
the largest. A 6U module is 266.7 mm tall and needs to print in one piece, oriented
upright, so the printer needs **≥ 300 mm in Z** to have any margin. The base plate is
likely the largest single part in the whole build.

Material matters more here than in most prints because the rack is a **sustained static
load**. PLA creeps under sustained load — a shelf holding 3 kg for six months will sag
even though it felt rigid on day one. The top of a closed rack is also warm, which
accelerates it.

## Options

### Printer
- **Existing printer, if it has ≥ 300 mm Z** — no cost, but check the bed size against
  the base plate and shelf parts.
- **Large-format bed-slinger / core-XY, 350 mm³ class** — comfortable for every part in
  this build including the base plate.
- **250 mm class** — forces the module height down to 3U/4U (see ADR-0001 option C) and
  forces the base plate to be split.

### Material
- **PLA** — rejected for anything structural. Keep for jigs, coupons and fit checks.
- **PETG** — the pragmatic default. Good creep resistance, cheap, forgiving.
- **ABS/ASA** — stiffer and more heat-tolerant; needs an enclosure.
- **PA-CF/PA-GF** — the right answer for the frame columns and the module joints.
  Expensive, abrasive, needs a hardened nozzle.

## Decision

**Undecided.** Provisional: **PETG for panels, shelves and brackets; PA-CF (or ASA as a
cheaper fallback) for the frame modules and the inter-module joint.**

## Consequences

- If the frame and the panels use different materials, the print log needs a material
  column per row, and the shrink allowance in `rack/params.json` may need to be
  per-material rather than global.
- Abrasive filament requires a hardened nozzle — a one-time purchase worth doing before
  the frame run, not between modules.
- Whatever the material, **the joint coupon print is a gate**, not an optional extra.

## Open questions

- Which printer is actually available? Z clearance is the deciding spec.
- Is an enclosure available? Without one, ASA/ABS is off the table.
- Budget for PA-CF: seven frame modules plus joints is a lot of filament.

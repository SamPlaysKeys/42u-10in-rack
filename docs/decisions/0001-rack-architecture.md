# ADR-0001: Rack architecture — modular 6U segments

**Status:** Proposed
**Date:** 2026-10-20

## Context

42U is 1866.9 mm of usable rack height. A monolithic printed frame at that height is not
printable in one piece — it exceeds every consumer build volume in all three axes — so
the question is not *whether* to split it, but along which seams and how the pieces join.

The constraints pulling against each other:

- **Build volume.** A typical large-format printer is 350 × 350 × 350 mm. A 42U frame
  must be split into at least 6 vertical pieces no matter what.
- **Joint stiffness.** Every joint is a weak point in a structure whose main job is to
  not sag or twist. A 1.9 m tall rack with more than a couple of kg of gear per shelf
  accumulates real bending moment at the base.
- **Reprint cost.** If a seam or a hole wears out or breaks, we want to reprint one
  small piece, not a 600 mm column.
- **Assembly access.** The lower modules have to be reachable with the upper ones
  already stacked, or assembly becomes a two-person job with a ladder.

## Options

### A. Monolithic printed frame, split only where the printer forces it
Print each full-height vertical column in 6 arbitrary slices sized to the bed. Fewest
parts, but slice heights are dictated by the printer rather than the design, joints land
in arbitrary places (possibly right where a mounting hole is), and a broken seam means
reprinting a whole column.

### B. Modular 6U segments — **7 identical modules**
Each module is 266.7 mm tall and prints as one piece, oriented upright. Modules stack
and bolt together. One part design, printed seven times.

### C. Modular segments at a different height
Same as B but 3U (133.35 mm, 14 modules), 4U, or 7U/8U. Smaller modules print faster
and reprint cheaper; more modules means more joints and more assembly work.

### D. Printed connectors joining metal extrusion
Use 2020 aluminium extrusion for the vertical structure and print only the joints,
rails and mounts. Much stronger and much faster to build, but it is no longer a 3D
printed rack — it is a printed-accessory rack.

## Decision

**Option B: seven identical 6U modules.**

266.7 mm module height × 7 = 1866.9 mm exactly, so the module boundary lands on a
multiple of the rack unit and every module contains exactly 6 complete Us with no
partial U at a seam. Printing upright means layer lines run vertically, so the
compression load down the columns is carried *along* the layers rather than peeling
them apart. One design printed seven times means one set of tolerances to chase, one
spare part, and a print failure costs a single module.

## Consequences

- **Good:** exactly 7 identical prints; seam always on a U boundary; a broken module is
  a reprint of one part; modules can be printed and stacked incrementally while the rest
  of the design is still being worked out.
- **Good:** a partial rack (1, 2, 3 modules) is usable, so the build can be validated at
  ~6U before committing to the full height.
- **Bad:** six joints are the structural weak point. This is the main risk of the design
  and is why the joint coupon in Phase 1 is a hard gate before the full stack.
- **Bad:** 266.7 mm tall × ~260 mm deep needs a printer with at least a 300 mm build
  volume in Z. A 250 mm-class printer forces option C.
- **Mitigation:** the joint carries a printed shear key plus through-bolts, not friction
  alone. If the coupon pull-test fails, fall back to 3U modules (option C) which halve
  the moment arm at each joint.

## Open questions

- Does the joint need a printed alignment pin, or do the bolts locate it well enough?
- Do we add a vertical spine (a continuous printed or extrusion backbone) behind the
  modules to carry bending load, rather than making the modules carry it?

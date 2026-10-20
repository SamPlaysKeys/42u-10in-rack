# ADR-0003: Rack depth

**Status:** Proposed
**Date:** 2026-10-20

## Context

Depth is the one dimension the 10-inch world has not even pretended to standardise.
Common cabinets are 200 mm deep (DeskPi RackMate T0/T1, Tecmojo 6U) or 260 mm (RackMate
T2 and the Plus models), with the spread across brands running 180–320 mm. Depth never
affects whether a panel *bolts* to the rails — it only decides what fits *behind* them.

For a 42U rack the stakes are higher than for a 4U shelf: depth sets the printer bed
requirement, the footprint, the tip-over risk, and whether the rack can take a real
server board, a 3.5" HDD stack, or a full-depth PDU.

## Options

### A. 200 mm depth
Matches the common RackMate form factor, needs the smallest printer, smallest footprint,
most stable. Fits SBCs, mini PCs, patch panels, short-depth switches. Cannot take a
3.5" HDD on a tray with cable room, an ITX board with a cooler, or most rack PDUs.

### B. 260 mm depth
Matches RackMate T2. Fits mini-ITX, HDD stacks, longer switches, and most PDUs. Costs
~60 mm more footprint on a rack that is already 1.9 m tall, and pushes the Z requirement
of a 6U upright module to 266.7 mm anyway — so depth is not the binding constraint on
the printer at that point. Adds to the tip-over moment.

### C. 300 mm+ depth
Real server depth. Only worth it if the plan includes actual server hardware, which for
a 10-inch rack usually means an ITX board on a shelf rather than a rack server.

### D. Depth-adjustable frame
Design the frame with telescoping or multi-position rail mounts so depth can change per
row. Most flexible, most parts, most places to get tolerance wrong.

## Decision

**Undecided.** Provisional target **260 mm**, on the grounds that a 42U rack is a
long-term fixture and running out of depth is unrecoverable, whereas 60 mm of extra
footprint is recoverable with a smaller base plate.

## Consequences

- At 260 mm the rack footprint is roughly 265 × 260 mm for a 1.9 m tall object. **This
  needs a wall anchor or a weighted base regardless of which option wins.**
- 260 mm lets the same shelf design carry either a mini PC or a 3.5" drive, which keeps
  the shelf family to one design.
- Whatever is chosen, depth is recorded in `rack/params.json` so every model reads it
  from one place.

## Open questions

- What is the deepest device that is actually planned? Check `inventory/devices.yaml`.
- Wall-mounted, floor-standing, or under-desk? A wall mount changes the depth calculus
  entirely.

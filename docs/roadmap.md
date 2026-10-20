# Roadmap

Phase gates for the build. A phase is done when its exit criteria are met, not when the
tasks are ticked.

## Phase 0 — Specification

Settle the envelope before modelling anything, so parts do not get redesigned twice.

- [x] Capture the 10-inch dimensional reference → [`10-inch-spec.md`](10-inch-spec.md)
- [ ] Decide rack architecture (modules vs. monolithic) → [ADR-0001](decisions/0001-rack-architecture.md)
- [ ] Decide rail and fastener system → [ADR-0002](decisions/0002-fastener-and-rail-system.md)
- [ ] Decide rack depth → [ADR-0003](decisions/0003-rack-depth.md)
- [ ] Choose the printer and material → [ADR-0004](decisions/0004-printer-and-material.md)
- [ ] Fill in `inventory/devices.yaml` with the real device list
- [ ] Freeze `rack/params.json` at v1.0

**Exit criteria:** every open ADR resolved, params frozen, inventory contains no
unresolved U allocations.

## Phase 1 — Frame

- [ ] Frame module, 6U, print-in-place test
- [ ] Inter-module joint: joint coupon printed and pull-tested
- [ ] Foot / base plate, 7 modules tall
- [ ] Optional top cap and wall-anchor bracket
- [ ] Full-height dry stack: 7 modules joined, measured against 1866.9 mm

**Exit criteria:** a free-standing 7-module frame that holds its own height, is square
within 2 mm over the full 1867 mm, and does not rack (twist) under hand load.

## Phase 2 — Rails

- [ ] Rail segment, 6U, with 3 holes per U
- [ ] Rail-to-frame brackets
- [ ] Verify hole spacing measures 236.525 mm ± 0.5 mm on the assembled frame
- [ ] Print a 1U test panel and bolt it in with real hardware

**Exit criteria:** a printed test panel mounts at every U position from 1 to 42 with no
reaming and no slop.

## Phase 3 — Services

- [ ] PDU mount and cable routing
- [ ] Brush strip panel
- [ ] Fan panel with thermal test
- [ ] 1U/2U blanking panels

## Phase 4 — Mounts

One mount per inventory entry that needs one, driven off `inventory/devices.yaml`.

- [ ] Shelf family (universal 1U/2U)
- [ ] Device-specific brackets for each `mount.type: custom` entry
- [ ] HDD/SSD carriers

## Phase 5 — Build out

- [ ] Install devices, one row at a time
- [ ] Update `rack/layout.md` as rows are filled
- [ ] Photograph and log each row
- [ ] Cable management pass

## Phase 6 — Finishing

- [ ] Sound/thermal review
- [ ] Label plate
- [ ] Publish the STL set

# 42U 10-Inch Server Rack — 3D Printed

Design, planning and print tracking for a **42U 10-inch** server rack, built as a
modular set of 3D-printed parts.

> **Status: Phase 0 — specification.**
> The rack envelope and architecture are still being decided. No part in
> [`models/`](models/) is released for printing yet. See
> [`docs/roadmap.md`](docs/roadmap.md) and the open ADRs in
> [`docs/decisions/`](docs/decisions/).

---

## What this is

A full-height, half-width (10") open-frame rack, 42U of usable mounting space, that
you print yourself. The repo holds four things that normally live in four different
places:

1. **The plan** — every device that goes in the rack, which U it occupies, and why.
2. **The spec** — the dimensions the whole design is built against, and where each
   number comes from.
3. **The models** — parametric source plus exported STLs/3MFs, organised by function.
4. **The record** — what has been designed, what has been printed, what is installed.

## At a glance

| | |
| :--- | :--- |
| Rack units | 42U |
| Usable rack height | **1866.9 mm** (42 × 44.45 mm) |
| 1U height | 44.45 mm (1.75") |
| Mounting hole centres, horizontal | **236.525 mm** (9.312") |
| Clear opening between rails | ~222 mm |
| Nominal panel width | 254 mm (10") |
| Module height | **6U = 266.7 mm**, × 7 modules — see [ADR-0001](docs/decisions/0001-rack-architecture.md) |
| Fastener system | *TBD* — see [ADR-0002](docs/decisions/0002-fastener-and-rail-system.md) |
| Target depth | *TBD* (200 mm or 260 mm) |
| Overall height, built | ~1.95–2.0 m |

Full derivation and sources: [`docs/10-inch-spec.md`](docs/10-inch-spec.md).

## Repository map

```
docs/          the plan: spec, design notes, roadmap, ADRs, print guide, BOM
rack/          the authoritative dimensional parameters + the 42U layout map
inventory/     machine-readable list of every device going in the rack
models/        the parts, by function, with exported STLs
src/           parametric source (CAD-as-code) and shared geometry
printing/      print profiles, material notes, and the print log
scripts/       inventory validation, parameter export, new-part scaffolding
.github/       issue templates, labels, CI
```

## How the workflow runs

```mermaid
flowchart LR
    A[Idea / need] --> B[Issue: new-part]
    B --> C[Spec the envelope<br/>inventory + params]
    C --> D[Model in src/]
    D --> E[Export STL to models/exports/]
    E --> F[Print job + log entry]
    F --> G[Dry fit]
    G --> H[Installed in rack]
    H --> I[Layout map updated]
```

Every part moves through the same stages, tracked on the GitHub Project board:
`Idea → Spec'd → Modeling → Review → Ready to print → Printing → Printed → Installed`.

Board setup and field definitions: [`docs/project-tracking.md`](docs/project-tracking.md).

## Getting started

```bash
git clone https://github.com/SamPlaysKeys/42u-10in-rack.git
cd 42u-10in-rack

chmod +x scripts/*.sh                 # git does not always preserve the exec bit
python3 scripts/validate_inventory.py # check the inventory against the layout
python3 scripts/params_to_scad.py     # generate the OpenSCAD include; models need it

./scripts/setup_github.sh             # one-time: create labels for the board
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the day-to-day workflow.

## Design rules of thumb

- **Build to hole spacing, never to the name.** Nothing on a 10-inch rack reliably
  measures 10 inches. 236.525 mm between hole centres is the number that decides fit.
- **Vertical dimensions are safe, horizontal ones are habit.** 44.45 mm per U is
  inherited from the 19-inch world and is not in dispute. Widths are a convention.
- **Printed parts shrink, warp, and creep.** Every joint gets a designed clearance and
  every load-bearing joint gets a coupon print before the full run.
- **A 1.9 m tall rack is a tip hazard.** Wall anchor or ballast the base, or both.

## Licence

Designs and documentation: [CC BY-SA 4.0](LICENSE). Scripts: MIT.
Swap either if you would rather use CERN-OHL-S-2.0 for the hardware.

# Printing

| File | Purpose |
| :--- | :--- |
| `print-log.md` | Every print: settings, measurements, failures, totals. |
| `profiles/` | Slicer profiles, one per material. |
| `materials.md` | Material decisions and what has been verified. |

## Print profiles

Store profiles as exported `.ini`/`.json` from the slicer, named by material and nozzle:

```
profiles/
├── petg-0.4-0.2-standard.ini
├── pa-cf-0.6-0.3-structural.ini
└── pla-0.4-0.2-fitcheck.ini
```

The slicer's own profile directory is not version controlled; the exported files here are.

## Batch planning

Parts are printed in **batches** rather than one at a time, because the rack is seven
identical modules and the per-print overhead dominates. A batch gets:

1. A directory in `models/exports/<date>-<name>/` with the STLs and a `MANIFEST.md`.
2. Rows in `print-log.md`.
3. A `print-job` issue, closed when the batch is measured and the parts are accepted.

Suggested batching order, cheapest failures first:

| Batch | Contents | Why this order |
| :--- | :--- | :--- |
| 1 | Joint coupon, test panel | Prove the two riskiest interfaces before anything large. |
| 2 | Frame module ×1, foot ×4 | Validate the biggest print before committing to seven. |
| 3 | Rail segment ×2, rail bracket ×4 | Then check the hole spacing for real. |
| 4 | Frame module ×6, joint bracket ×12 | The bulk run, once the geometry is proven. |
| 5 | Base plate, top cap | Largest parts, printed last. |
| 6+ | Panels, shelves, mounts | Per inventory, as devices arrive. |

## Time and material estimate

Fill in once batch 2 reports real numbers. A rough planning figure for the frame alone is
7 modules at 8–14 hours each, so the full frame is several days of continuous printing —
which is an argument for printing modules as the design firms up rather than all at once.

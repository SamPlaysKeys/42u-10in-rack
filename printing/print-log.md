# Print log

Every print gets a row, including the failures. A part is not "done" until it has one.

The point of this table is to answer three questions a year from now: what settings
actually worked, how much filament the rack consumed, and how long a full reprint would
take.

## Log

| # | Date | Part | Printer | Material | Nozzle | Layer | Infill | Perim. | Time | Filament | Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| — | — | *no prints yet* | — | — | — | — | — | — | — | — | — |

## Measured dimensions

The coupon results, which are what the design's clearances are actually based on. Update
`rack/params.json` → `print` when these come in.

| Date | Coupon | Nominal (mm) | Measured (mm) | Delta (mm) | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| — | — | — | — | — | — |

## Failures and lessons

| Date | Part | What went wrong | Cause | Fix |
| :--- | :--- | :--- | :--- | :--- |
| — | — | — | — | — |

## Running totals

| | |
| :--- | :--- |
| Parts printed | 0 |
| Print hours | 0 |
| Filament used | 0 g |
| Failed prints | 0 |

## Rules

- **Log the failure, not just the success.** A failed print that is not logged gets
  repeated.
- **Measure, do not assume.** If a coupon's measured dimension differs from nominal by
  more than 0.2 mm, the clearance in `rack/params.json` is wrong and should change.
- **One row per physical print.** If a plate has five parts on it, that is one row with
  five parts listed.

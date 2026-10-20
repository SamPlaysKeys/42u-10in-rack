## What this changes

<!-- One or two sentences. -->

## Type

- [ ] Part: new or revised model
- [ ] Spec: change to `rack/params.json` or `docs/10-inch-spec.md`
- [ ] Inventory: change to `inventory/`
- [ ] Docs
- [ ] Tooling

## Checks

- [ ] `python3 scripts/validate_inventory.py` passes
- [ ] `python3 scripts/params_to_scad.py` run and the result committed
- [ ] Any changed dimension traces back to `rack/params.json`, not a hard-coded number
- [ ] Part README updated (status, critical dimensions, revision history)
- [ ] If a part was printed: row added to `printing/print-log.md` with measured dimensions
- [ ] If a device was installed: `rack/layout.md` updated

## Measurements

<!-- If this PR follows a print, put the caliper numbers here. Nominal vs measured. -->

| Dimension | Nominal | Measured | Delta |
| :--- | :--- | :--- | :--- |
| | | | |

## Notes

<!-- Anything a future reader would want to know, especially what did not work. -->

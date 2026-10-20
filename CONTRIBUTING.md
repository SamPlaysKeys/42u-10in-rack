# Working on this repo

Mostly written for future-me, because in six months none of this will be obvious.

## Before you change a number

Every dimension lives in **one** place: `rack/params.json`. If you find yourself typing
`236.525` into a model or a document, stop and reference the parameter instead. The
failure mode this repo exists to prevent is two files disagreeing about the hole spacing.

After changing `rack/params.json`:

```bash
python3 scripts/params_to_scad.py     # regenerate the OpenSCAD include
python3 scripts/validate_inventory.py # check nothing downstream broke
```

## Adding a part

```bash
./scripts/new_part.sh 04-shelves shelf-universal-1u "Universal shelf 1U" shelf
```

Then open the tracking issue it prints, and set the board fields.

## Adding a device

1. Add it to `inventory/devices.yaml`.
2. Add its U row to `rack/layout.md`.
3. Run the validator.
4. If `mount.type` is `bracket` or `tray`, scaffold the mount part and open a `[part]`
   issue for it.

## Commit messages

Conventional-ish prefixes, so `git log --oneline` is readable:

| Prefix | For |
| :--- | :--- |
| `part:` | A model added or changed |
| `spec:` | `rack/params.json` or the spec doc |
| `inv:` | Inventory changes |
| `docs:` | Documentation |
| `print:` | Print results and log entries |
| `tooling:` | Scripts and CI |

Example: `part: add frame-module-6u, first draft of the joint`

## The two rules that matter

1. **Record the measurement.** A number in your head is not a number. Calipers, then
   write it down, then commit it.
2. **Log the failure.** A failed print that is not logged gets repeated three weeks
   later by someone who has forgotten why it failed. That someone is usually you.

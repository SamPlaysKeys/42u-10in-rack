# OpenSCAD source

`params.scad` is **generated** from `rack/params.json` by `scripts/params_to_scad.py`.
Do not edit it by hand; edit the JSON and regenerate.

It is gitignored, so **run the generator once after cloning**, and again after any
edit to `rack/params.json`:

```bash
python3 scripts/params_to_scad.py
```

Until you do, every model will fail to open with a missing-include error.

Every part includes it with a relative path. Parts live at
`models/<category>/<slug>/`, which is two levels below `models/` and one across to
`src/`, so the include is **three** levels up:

```openscad
include <../../../src/openscad/params.scad>
```

Get this depth wrong and OpenSCAD does not error — it ignores the missing include and
resolves every spec variable to `undef`, rendering a 1 mm cube instead of your part.
Each shared module carries an `assert` that turns that silence into a failure.

Because the include resolves, the part reads `width_hole_centres`, `rack_unit_u_height`
and the rest straight from the spec instead of hard-coding numbers.

## Naming

Parameters are flattened from the JSON structure with underscores:

| `rack/params.json` | `params.scad` |
| :--- | :--- |
| `rack_unit.u_height` | `rack_unit_u_height` |
| `width.hole_centres` | `width_hole_centres` |
| `rack.module_height` | `rack_module_height` |
| `print.clearance_general` | `print_clearance_general` |

Array elements get a 1-based suffix: `rack_unit_hole_pattern_within_u_1`, `_2`, `_3`.

## Installing OpenSCAD

```bash
sudo apt install openscad        # Debian/Ubuntu
```

Render a part headlessly:

```bash
openscad -o part.stl models/04-shelves/shelf-universal-1u/shelf-universal-1u.scad
```

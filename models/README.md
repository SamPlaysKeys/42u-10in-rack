# Models

The parts. Organised by **what the part does in the rack**, not by printer or material,
so that a shelf that happens to hold a PDU lives with the shelves and not with power.

## Layout

```
models/
├── 00-shared/     common geometry: joint profiles, screw bosses, vent patterns
├── 01-frame/      the structural frame and its joints
├── 02-rails/      rack rails and rail brackets
├── 03-power/      PDU, UPS and power brick mounts
├── 04-shelves/    universal and device-specific shelves
├── 05-panels/     blanking, vented, cable-entry and fan panels
├── 06-cable/      cable management, hooks, brush strips
├── 07-mounts/     device-specific brackets and trays
└── exports/       the STL/3MF files that actually get printed
```

## One part = one directory

```
models/04-shelves/universal-shelf-1u/
├── README.md            what it is, what it fits, its critical dimensions
├── universal-shelf-1u.scad    parametric source
├── universal-shelf-1u.md      build notes: constraints, alternatives, open questions
├── universal-shelf-1u.stl     the exported mesh
└── universal-shelf-1u.3mf     print-ready, with orientation and settings
```

Create one with:

```bash
./scripts/new_part.sh 04-shelves universal-shelf-1u "Universal shelf 1U" shelf
```

## Source format

**OpenSCAD, one file per part, parameterised.** The reasons, in order:

1. **It is diffable.** A binary CAD file is a blob in git; a `.scad` file shows up in a
   pull request as changed numbers. For a project that is essentially a pile of
   dimensions, that is the whole ballgame.
2. **It reads the shared spec.** Every model starts with
   `include <../../openscad/params.scad>`, which is generated from `rack/params.json`.
   A change to the hole spacing propagates to every part instead of being retyped into
   each one and forgotten in half of them.
3. **It is reviewable and forkable.** No licence, no version lock-in, and anyone can
   open it in a browser-free editor.

If a part genuinely needs a GUI modeller, that is allowed — but export the STL, commit
the source file alongside it, and note in the part's README which tool made it. The
principle is that the *design* is reviewable, not that the tool is OpenSCAD.

## Naming

`lowercase-hyphenated`, descriptive, no version numbers in the name. Variants are
separate parts:

| Good | Bad | Why |
| :--- | :--- | :--- |
| `blanking-panel-1u` | `panel1U_final_v3` | Says what it is; no revision in the name. |
| `blanking-panel-1u-vented` | `blanking-panel-1u-v2` | A different part, not a revision. |
| `shelf-universal-1u` | `myshelf` | Findable. |

Revisions live in the part's README history table and in git, not in filenames.

## Status vocabulary

Every part README carries a status line, and it must match the tracking issue:

| Status | Meaning |
| :--- | :--- |
| `Draft` | Being modelled. Not reliable, do not print. |
| `Fit-check` | Printed once for a dry fit. Dimensions unconfirmed. |
| `Validated` | Printed, measured, fitted, and the numbers in the README are real. |
| `Released` | In the rack, or published for others to print. |
| `Deprecated` | Superseded. Kept for history. |

## Exports

- Exports go in the part's own directory. A central `exports/` pile of STLs with no
  provenance is how a project loses track of which mesh is current.
- `models/exports/` holds only **batches** — an STL set for a print run, named by date.
- Export at the same orientation you intend to print. An STL that has to be rotated in
  the slicer is an STL whose orientation will eventually be forgotten.
- `.3mf` is preferred over `.stl` when the part has multiple bodies or needs specific
  per-object settings, because it carries the settings with it.

# 42U layout map

The physical plan: which device occupies which U. This is the document to check before
buying anything, and the one to update when something is installed.

- **Devices and their specs** live in [`../inventory/devices.yaml`](../inventory/devices.yaml).
- **This file** is the resulting arrangement, top (U42) to bottom (U1).
- Keep them in sync: `python3 scripts/validate_inventory.py` fails if a device claims a U
  that is taken, out of range, or if the file and the inventory disagree.

## How to read this

- Numbering runs **U1 at the bottom** to **U42 at the top**, matching the convention in
  every other rack on the planet.
- `—` means free space. Free space is not wasted space: it is airflow, cable room, and
  the only place you can add something later without moving everything above it.
- **Weight goes low.** Heavy items belong in the bottom third; the moment arm of a 3 kg
  item at U40 is the single easiest way to make this rack fall over.
- Module boundaries are marked, since the frame is seven 6U modules (ADR-0001).

## Current layout

```
U42 ┌──────────────────────────────────────┐
U41 │                                      │  MODULE 7  (U37-U42)
U40 │                                      │
U39 │                                      │
U38 │                                      │
U37 │                                      │
U36 ├──────────────────────────────────────┤
U35 │                                      │  MODULE 6  (U31-U36)
U34 │                                      │
U33 │                                      │
U32 │                                      │
U31 │                                      │
U30 ├──────────────────────────────────────┤
U29 │                                      │  MODULE 5  (U25-U30)
U28 │                                      │
U27 │                                      │
U26 │                                      │
U25 │                                      │
U24 ├──────────────────────────────────────┤
U23 │                                      │  MODULE 4  (U19-U24)
U22 │                                      │
U21 │                                      │
U20 │                                      │
U19 │                                      │
U18 ├──────────────────────────────────────┤
U17 │                                      │  MODULE 3  (U13-U18)
U16 │                                      │
U15 │                                      │
U14 │                                      │
U13 │                                      │
U12 ├──────────────────────────────────────┤
U11 │                                      │  MODULE 2  (U7-U12)
U10 │                                      │
U9  │                                      │
U8  │                                      │
U7  │                                      │
U6  ├──────────────────────────────────────┤
U5  │                                      │  MODULE 1  (U1-U6)
U4  │                                      │
U3  │                                      │
U2  │                                      │
U1  └──────────────────────────────────────┘
```

All 42U currently unallocated. Fill this in as the inventory firms up, then keep the
diagram and the table below identical.

## Allocation table

| U | Device | Inventory ID | Height | Mount | Weight | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 42–1 | *unallocated* | — | — | — | — | — |

## Reserved for later

Rows worth deliberately leaving empty, so the design does not fill every gap and then
have nowhere to grow:

| U | Reserved for | Why |
| :--- | :--- | :--- |
| 42 | Cable entry / fan panel | Heat has to leave at the top; cables enter here. |
| 41 | Patch panel | Cables from the top run down into it. |
| 1–2 | UPS or PDU | Heaviest item, lowest position, shortest power run. |

## Notes

- **Bottom-heavy is the rule.** If the rack is anchored, this matters less, but it never
  stops mattering.
- **Leave gaps between heat sources.** A printed rack with no airflow path will cook the
  devices in it, and printed plastic softens before the devices complain.
- Update this file in the same commit that changes the inventory, not afterwards.

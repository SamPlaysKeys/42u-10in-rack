# Print guide

Practical rules for printing this rack. Filled in as phases land; the placeholders are
the decisions that are still open.

## Material choice

| Material | Verdict | Why |
| :--- | :--- | :--- |
| PLA | **Not for structure** | Creeps under sustained load. A 1.9 m rack holding a few kg per shelf is exactly the sustained-load case that fails. Fine for jigs and fit-check parts. |
| PETG | Acceptable | Better creep resistance, cheap, prints easily. Slightly flexible, which is fine for panels and shelves. |
| ABS / ASA | Good | Stiffer, better creep resistance, dimensionally stable in a warm rack. Needs an enclosure. |
| PA-CF / PA-GF | **Best for the frame** | High stiffness and creep resistance. Costs more and needs a hardened nozzle. |
| PC | Good but fussy | Very stiff, hard to print. |

Current decision and reasoning: [ADR-0004](decisions/0004-printer-and-material.md).

## Rules that apply to every part

- **Print a coupon first.** Any joint that carries load gets a small test print of just
  that joint, measured with calipers, before the full part is committed.
- **Design in clearance, not tolerance.** Assume ±0.2 mm on any printed dimension and
  ±0.5 mm on anything over 100 mm long. Slotted holes on printed joints, not round ones.
- **Avoid loading along layer lines.** Any bracket where the load pulls the layers apart
  should be reoriented or redesigned. If it cannot be, use more perimeters.
- **Wall count over infill.** 4–6 perimeters does more for a structural part than
  raising infill past 40%.
- **Temperature matters.** A closed rack with a switch and a PDU gets warm. Parts under
  load near the top of a closed rack should be ABS/ASA/PA, not PETG.
- **Beware the long part.** A 260 mm shelf printed diagonally across a 256 mm bed is a
  warp generator. Split it and join it.

## Orientation

| Part family | Orientation | Reason |
| :--- | :--- | :--- |
| Frame module | Upright, vertical | Layer lines run with the compression load. |
| Rail segment | Vertical | Holes print round; no supports in the screw path. |
| Shelf | Flat, ribs up | Strength in the plane of the load. |
| Panel | Flat on face | Trivially strong in that axis; cosmetic face on the plate. |
| Bracket | As designed, no supports | If it needs supports, redesign it. |

## Print log

Every print gets a row in [`../printing/print-log.md`](../printing/print-log.md) with the part, printer,
material, settings, dimensions as measured, and the verdict. A part is not "done" until
it has a log row.

# ADR-0002: Fastener and rail system

**Status:** Proposed
**Date:** 2026-10-20

## Context

The 10-inch world has no agreed hole system. Racks in the wild use square 9.5 mm
cage-nut slots, tapped M6 holes, 10-32 threaded holes, or plain holes with a nut behind.
Since we are printing the rails, we pick — but the choice determines whether commercial
10-inch gear can be bolted in alongside our own parts, and how much adjustment the rack
has when printed dimensions drift.

Printed holes are not round and not accurate. Expect ±0.2 mm on a small hole and worse on
a long part. A rack with 42 rows of printed round holes and zero adjustment will fight
every part that goes into it.

## Options

### A. Printed round holes sized for M5 machine screws + nuts
Cheapest. No inserts to buy. But printed threads are weak, and a plain M5 hole in a
printed rail will ovalise the first time a screw is over-torqued. No adjustment.

### B. Heat-set brass inserts in printed holes, M5 or M6
Strong, repeatable, re-usable threads. Every rail hole needs an insert, which is 42 rows
× 3 holes × 2 rails = 252 inserts per rack. That is a lot of soldering-iron time, and
inserts need a printed boss around them, which eats rail width.

### C. Printed rail + bought steel rail strip
Print the frame and bolt a strip of commercially available tapped rail to it. Removes
every accuracy problem in the hole pattern, since the holes are punched in steel. But it
reintroduces a purchased part, which is what this project is trying to avoid, and steel
rail stock in 10-inch hole spacing is not a stocked item — it would need cutting and
drilling, or SendCutSend.

### D. Square 9.5 mm holes + standard cage nuts
Match what the rest of the industry does. A 9.5 mm square hole is trivially printable,
cage nuts are cheap and universal, and the clip absorbs misalignment — which is exactly
the failure mode of a printed rack. Gives compatibility with any 10-inch gear that ships
cage-nut hardware.

### E. Slotted printed holes, M5 screws and printed nuts
Print the hole as a vertical slot rather than a circle. Buys ±2 mm of vertical adjustment
per hole, which covers accumulated error across a 42U stack. Weakest mechanically, but
the slot only needs to resist shear, not tension.

## Decision

**Leaning D with an E fallback on the frame-to-rail joint.** Square 9.5 mm holes on the
rack rails for cage nuts, and slotted holes where a printed part joins a printed part so
accumulated error has somewhere to go.

Not yet accepted. Needs a decision on whether commercial 10-inch gear will be mixed in,
because that is the only thing that forces the exact 236.525 mm spacing rather than
"whatever our rails measure".

## Consequences

- Cage nuts absorb misalignment, which is the single biggest risk in a printed rack.
- Buying cage nuts means buying hardware, but M6 cage nuts cost very little and are
  stocked everywhere.
- If we later want printed threads instead, only the rail part changes; the frame is
  unaffected, which is a good reason to keep the rail a separate printed part.

## Open questions

- Will commercial 10-inch gear be mixed in? If yes, 236.525 mm is a hard requirement and
  a printed test panel must be measured against it before the full rail run.
- M6 or 10-32? Depends on what hardware the devices ship with.
- Does the printed rail need a metal insert at the top and bottom module, where the
  bending moment is highest?

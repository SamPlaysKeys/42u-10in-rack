# Design notes

Running notes on decisions that are not big enough for an ADR but too important to leave
in a commit message.

## Why 42U

42U is 1866.9 mm — taller than a person, and taller than most consumer printers by a
factor of seven. It is also the point at which a rack stops being a desk accessory and
becomes furniture, which changes several design assumptions:

- **Tip-over is the primary structural risk**, not sag. A 260 mm footprint at 1.9 m tall
  is a lever.
- **Assembly order matters.** You cannot reach the bottom of the rack with the top
  installed, unless the modules are light enough to lift into place one at a time —
  which is another argument for the 6U module split.
- **Access to the middle matters.** A 42U rack has a lot of inaccessible middle. Leave
  service loops and do not route cables where you cannot reach them.

## Why half-width at all

A 10-inch rack holds roughly half of what a 19-inch rack holds, in a third of the
footprint. The trade is that very little commercial gear is natively 10-inch, so most of
the value comes from the printed mounts. That is the actual point of this project: the
printed parts are the product, and the rack is what holds them.

## Things that will go wrong

Recorded in advance so they are recognised when they happen rather than debugged from
scratch:

1. **Printed hole spacing will not be 236.525 mm.** It will be close, and the error will
   accumulate over 42U. This is why the test panel comes before the rail run, and why
   the frame-to-rail joint is slotted.
2. **The first frame module will warp.** 266.7 mm of upright print on a large bed pulls
   at the corners. Expect to add a brim and to lose the first attempt.
3. **The joint will be the weakest point.** If the coupon fails, 3U modules halve the
   moment arm at every joint.
4. **Power bricks will not fit anywhere convenient.** Plan for them explicitly.
5. **Something will be 2 mm too wide.** The design envelope is 210 mm against a 222 mm
   opening for a reason. Do not design to 222.

## Measurement discipline

One caliper, one person, written down immediately. The failure mode in a project like
this is not a wrong measurement, it is a right measurement that nobody recorded and
which then gets re-guessed three months later. Every measurement goes in the relevant
part README or in `printing/print-log.md`.

## Open design questions

- [ ] Continuous vertical spine behind the modules to carry bending load, or modules
      carrying it alone?
- [ ] Does the frame need diagonal bracing at the base?
- [ ] Should the rails be separate printed parts at all, or printed as part of the frame
      module? Separate is better for printing orientation and reprinting; integral is
      stiffer and fewer parts.
- [ ] Wall-anchored or free-standing with a weighted base? This changes the whole
      stability design and should be decided before the base plate is modelled.

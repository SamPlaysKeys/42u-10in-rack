# Materials

What has actually been verified, as opposed to what the datasheet claims. Fill in from
coupon results.

| Material | Brand | Colour | Nozzle | Temp | Bed | Verified? | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PETG | — | — | 0.4 | — | — | No | Panels, shelves, brackets. |
| PA-CF | — | — | 0.6 hardened | — | — | No | Frame modules, joints. |
| PLA | — | — | 0.4 | — | — | No | Coupons and jigs only. |

## Creep: why PLA is excluded from structure

PLA deforms under sustained load at room temperature. A shelf that feels rigid on the day
it is printed will sag over months, and it will sag faster in a warm rack. Every
structural part in this build carries a static load for years, which is exactly the case
PLA is worst at. Keep it for jigs, coupons and fit checks.

## Shrinkage

The `shrink_allowance` in `rack/params.json` is a single fractional scale factor applied
to XY. It is a starting point, not a measurement. Replace it with a real number after
printing the calibration coupon and measuring it, and consider making it per-material if
PETG and PA-CF differ by more than the clearance budget.

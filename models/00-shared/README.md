# 00 — Shared geometry

Modules other parts include. No standalone printable parts live here.

| Module | Purpose |
| :--- | :--- |
| `shared-joint.scad` | The inter-module joint geometry (ADR-0001). Included by the frame and the joint coupon so the two cannot drift apart. |
| `shared-panel.scad` | The standard 1U/2U panel outline at the correct width, so every panel starts from the same silhouette. |
| `screw-boss.scad` | Boss and countersink geometry for the standard fasteners in `rack/params.json`. |
| `vent-pattern.scad` | Parametric slot pattern used by the vented panels. |

Rule: if two parts need the same geometry, it goes here **the second time** it is needed,
not the first. Premature sharing is how a shared library ends up with one function and
four parameters.

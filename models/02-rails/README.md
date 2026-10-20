# 02 — Rails

The vertical rails the gear bolts to. Two per module, 14 in total.

| Part | Qty | Status | Notes |
| :--- | :--- | :--- | :--- |
| `rail-segment-6u` | 14 | Planned | 3 holes per U, 236.525 mm centres across the pair. |
| `rail-bracket` | 28 | Planned | Rail to frame. |
| `test-panel-1u` | 1 | Planned | **Print first.** A plain 1U panel to prove the hole spacing before the rail run. |

**The acceptance test for this phase:** the printed test panel mounts at every U position
from 1 to 42 with no reaming and no slop, and the assembled hole centres measure
236.525 mm ± 0.5 mm. If that fails, everything downstream is built on a wrong number.

# 07 — Device mounts

Device-specific brackets and trays. **One directory per device that needs one.**

This is the directory that grows from the inventory. For every entry in
`inventory/devices.yaml` with `mount.type: bracket` or `mount.type: tray`, there is a
part here, and it gets a tracking issue with the `type:bracket` label.

| Part | Device | Inventory ID | Status |
| :--- | :--- | :--- | :--- |
| — | — | — | — |

Conventions:

- Name it after the device, not after yourself: `bracket-mikrotik-crs310`, not
  `my-bracket-v2`.
- Record the device's real measured dimensions in the part README. Datasheet dimensions
  are usually the chassis, not the chassis plus the bit that sticks out.
- Leave a way to reach the power button. A tray that hides a power button turns a
  two-minute fix into unracking the whole machine.

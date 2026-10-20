#!/usr/bin/env python3
"""Validate inventory/devices.yaml against the rack specification.

Checks, in order:
  1. YAML parses and the top-level shape is right.
  2. Every device has the required fields, of the right type.
  3. IDs are unique; referenced categories exist.
  4. U allocations are in range, non-colliding, and physically fit.
  5. Devices are within the horizontal design envelope.
  6. rack/layout.md's allocation table matches the inventory.
  7. rack/params.json is internally consistent.

Exit code 0 = clean, 1 = problems found. Run before every inventory commit.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required.  pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
PARAMS = ROOT / "rack" / "params.json"
DEVICES = ROOT / "inventory" / "devices.yaml"
LAYOUT = ROOT / "rack" / "layout.md"

REQUIRED = {
    "id": str,
    "name": str,
    "category": str,
    "u_height": (int, float),
    "width_mm": (int, float),
    "depth_mm": (int, float),
    "height_mm": (int, float),
    "weight_kg": (int, float),
    "mount": dict,
    "status": str,
}

VALID_STATUS = {"planned", "owned", "installed", "retired"}
VALID_MOUNT = {"native", "shelf", "bracket", "tray", "none"}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_params() -> dict:
    if not PARAMS.exists():
        err(f"{PARAMS.relative_to(ROOT)} is missing")
        return {}
    try:
        return json.loads(PARAMS.read_text())
    except json.JSONDecodeError as exc:
        err(f"rack/params.json is not valid JSON: {exc}")
        return {}


def check_params(p: dict) -> None:
    """The spec has to agree with itself before anything else can be checked."""
    if not p:
        return
    rack = p.get("rack", {})
    unit = p.get("rack_unit", {})

    u_height = unit.get("u_height")
    total_u = rack.get("total_u")
    usable = rack.get("usable_height")
    if u_height and total_u and usable:
        expected = round(u_height * total_u, 4)
        if abs(expected - usable) > 0.01:
            err(
                f"params: usable_height {usable} != u_height {u_height} x total_u "
                f"{total_u} = {expected}"
            )

    module_u = rack.get("module_u")
    module_count = rack.get("module_count")
    module_height = rack.get("module_height")
    if None not in (module_u, module_count, total_u):
        if module_u * module_count != total_u:
            err(
                f"params: module_u {module_u} x module_count {module_count} "
                f"!= total_u {total_u}"
            )
    if None not in (module_u, module_height, u_height):
        if abs(module_u * u_height - module_height) > 0.01:
            err(
                f"params: module_height {module_height} != module_u {module_u} "
                f"x u_height {u_height} = {module_u * u_height}"
            )

    width = p.get("width", {})
    centres = width.get("hole_centres")
    panel = width.get("nominal_panel_width")
    opening = width.get("clear_opening")
    envelope = width.get("design_envelope")
    if None not in (centres, panel, opening):
        # hole centres must sit inside the panel, and the opening inside the centres
        if not centres < panel:
            err(f"params: hole_centres {centres} must be less than panel width {panel}")
        if not opening < centres:
            err(f"params: clear_opening {opening} must be less than hole_centres {centres}")
    if None not in (envelope, opening):
        if envelope > opening:
            err(
                f"params: design_envelope {envelope} cannot exceed clear_opening "
                f"{opening}"
            )


def load_inventory() -> dict:
    if not DEVICES.exists():
        err(f"{DEVICES.relative_to(ROOT)} is missing")
        return {}
    try:
        data = yaml.safe_load(DEVICES.read_text())
    except yaml.YAMLError as exc:
        err(f"inventory/devices.yaml failed to parse: {exc}")
        return {}
    if not isinstance(data, dict):
        err("inventory/devices.yaml must be a mapping at the top level")
        return {}
    return data


def check_devices(data: dict, params: dict) -> list[dict]:
    devices = data.get("devices") or []
    if not isinstance(devices, list):
        err("'devices' must be a list")
        return []

    categories = set((data.get("categories") or {}).keys())
    defaults = data.get("defaults") or {}
    envelope = params.get("width", {}).get("design_envelope", 210.0)
    max_width = defaults.get("max_width_mm", envelope)
    total_u = params.get("rack", {}).get("total_u", 42)

    seen_ids: set[str] = set()
    for i, dev in enumerate(devices):
        where = f"devices[{i}]"
        if not isinstance(dev, dict):
            err(f"{where}: must be a mapping")
            continue

        did = dev.get("id", where)
        if isinstance(did, str):
            where = f"device '{did}'"
            if did in seen_ids:
                err(f"{where}: duplicate id")
            seen_ids.add(did)

        for field, ftype in REQUIRED.items():
            if field not in dev:
                err(f"{where}: missing required field '{field}'")
                continue
            value = dev[field]
            if value is None and field == "mount":
                err(f"{where}: 'mount' cannot be null")
                continue
            if not isinstance(value, ftype) or isinstance(value, bool):
                names = (
                    ftype.__name__
                    if isinstance(ftype, type)
                    else "/".join(t.__name__ for t in ftype)
                )
                err(f"{where}: field '{field}' should be {names}, got {type(value).__name__}")

        # category
        cat = dev.get("category")
        if isinstance(cat, str) and categories and cat not in categories:
            warn(f"{where}: category '{cat}' is not declared in the categories map")

        # status
        status = dev.get("status")
        if isinstance(status, str) and status not in VALID_STATUS:
            err(f"{where}: status '{status}' not one of {sorted(VALID_STATUS)}")

        # mount
        mount = dev.get("mount")
        if isinstance(mount, dict):
            mtype = mount.get("type")
            if mtype not in VALID_MOUNT:
                err(f"{where}: mount.type '{mtype}' not one of {sorted(VALID_MOUNT)}")

        # physical envelope
        width = dev.get("width_mm")
        if isinstance(width, (int, float)) and width > max_width:
            err(
                f"{where}: width {width} mm exceeds the {max_width} mm design envelope "
                f"(clear opening is only {params.get('width', {}).get('clear_opening')} mm)"
            )

        # U allocation
        u_height = dev.get("u_height")
        u_pos = dev.get("u_position")
        if isinstance(u_height, (int, float)):
            if u_height <= 0:
                err(f"{where}: u_height must be positive")
            if u_pos is not None:
                if not isinstance(u_pos, int) or isinstance(u_pos, bool):
                    err(f"{where}: u_position should be an integer or null")
                elif u_pos < 1:
                    err(f"{where}: u_position {u_pos} is below U1")
                elif u_pos + u_height - 1 > total_u:
                    err(
                        f"{where}: occupies U{u_pos}-U{u_pos + int(u_height) - 1}, "
                        f"which runs past U{total_u}"
                    )

        # weight sanity
        weight = dev.get("weight_kg")
        if isinstance(weight, (int, float)) and weight < 0:
            err(f"{where}: weight_kg cannot be negative")

    return [d for d in devices if isinstance(d, dict)]


def check_collisions(devices: list[dict], params: dict) -> None:
    total_u = params.get("rack", {}).get("total_u", 42)
    claimed: dict[int, str] = {}
    for dev in devices:
        u_pos, u_height = dev.get("u_position"), dev.get("u_height")
        if u_pos is None or not isinstance(u_pos, int) or not isinstance(u_height, (int, float)):
            continue
        if dev.get("status") == "retired":
            continue
        for u in range(u_pos, u_pos + int(u_height)):
            if not 1 <= u <= total_u:
                continue
            if u in claimed:
                err(
                    f"U{u} claimed by both '{claimed[u]}' and '{dev.get('id')}'"
                )
            else:
                claimed[u] = str(dev.get("id"))

    allocated = len(claimed)
    if allocated:
        pct = allocated / total_u * 100
        print(
            f"  U allocation: {allocated}/{total_u} occupied ({pct:.0f}%), "
            f"{total_u - allocated} free"
        )


def check_layout(devices: list[dict]) -> None:
    """rack/layout.md must list exactly the devices that have a U position."""
    if not LAYOUT.exists():
        warn("rack/layout.md is missing; cannot cross-check the allocation table")
        return
    text = LAYOUT.read_text()

    placed = {
        str(d.get("id"))
        for d in devices
        if d.get("u_position") is not None and d.get("status") != "retired"
    }

    # Only the "## Allocation table" section counts. Later sections (reserved
    # rows, notes) have their own tables with different columns.
    section = text.split("## Allocation table", 1)
    if len(section) < 2:
        warn("rack/layout.md has no '## Allocation table' section to cross-check")
        return
    body = re.split(r"\n## ", section[1], maxsplit=1)[0]

    # Rows look like: | 12 | name | inventory-id | ...
    rows = [
        line
        for line in body.splitlines()
        if line.strip().startswith("|") and line.count("|") >= 4
    ]
    documented: set[str] = set()
    for line in rows:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        candidate = cells[2]
        if not candidate or set(candidate) <= {"-", ":", " "}:
            continue
        if candidate in {"Inventory ID", "id", "—", "*unallocated*"}:
            continue
        documented.add(candidate)

    for did in sorted(placed - documented):
        err(
            f"'{did}' has a U position in devices.yaml but is not in the "
            f"allocation table in rack/layout.md"
        )
    for did in sorted(documented - placed):
        err(
            f"'{did}' is in the allocation table in rack/layout.md but has no "
            f"u_position in devices.yaml"
        )


def main() -> int:
    print("Validating inventory against the rack specification\n")
    params = load_params()
    check_params(params)
    data = load_inventory()
    devices = check_devices(data, params)
    check_collisions(devices, params)
    check_layout(devices)

    print(f"  Devices: {len(devices)}")
    print(f"  Rack:    {params.get('rack', {}).get('total_u')}U, "
          f"{params.get('rack', {}).get('usable_height')} mm usable, "
          f"{params.get('width', {}).get('hole_centres')} mm hole centres\n")

    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  FAIL  {e}")

    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"OK - no errors ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())

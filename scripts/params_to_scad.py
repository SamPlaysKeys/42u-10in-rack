#!/usr/bin/env python3
"""Generate src/openscad/params.scad from rack/params.json.

Keeps the CAD source reading from the same numbers as everything else, so a change to
the spec propagates into the models instead of being retyped into each one.

    python3 scripts/params_to_scad.py          # write the include
    python3 scripts/params_to_scad.py --stdout # preview without writing
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARAMS = ROOT / "rack" / "params.json"
OUT = ROOT / "src" / "openscad" / "params.scad"

HEADER = """// GENERATED FILE - DO NOT EDIT BY HAND.
// Source: rack/params.json  (version {version}, revision {revision})
// Regenerate with:  python3 scripts/params_to_scad.py
//
// All dimensions in millimetres.

"""


def flatten(node, prefix="") -> list[tuple[str, object]]:
    """Flatten nested dicts into dotted names, skipping $comment-style keys."""
    out: list[tuple[str, object]] = []
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$") or key == "units":
                continue
            name = f"{prefix}{key}"
            if isinstance(value, dict):
                out.extend(flatten(value, prefix=f"{name}_"))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    out.append((f"{name}_{i + 1}", item))
            else:
                out.append((name, value))
    return out


def main() -> int:
    if not PARAMS.exists():
        print(f"error: {PARAMS} not found", file=sys.stderr)
        return 1

    data = json.loads(PARAMS.read_text())
    pairs = flatten(data)

    lines = [
        HEADER.format(
            version=data.get("version", "unknown"),
            revision=data.get("revision", "unknown"),
        )
    ]
    for name, value in pairs:
        if isinstance(value, bool):
            literal = "true" if value else "false"
        elif isinstance(value, (int, float)):
            literal = f"{value:g}"
        elif isinstance(value, str):
            literal = f'"{value}"'
        else:
            continue
        lines.append(f"{name} = {literal};  // {type(value).__name__}")

    text = "\n".join(lines) + "\n"

    if "--stdout" in sys.argv:
        print(text)
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text)
    print(f"wrote {OUT.relative_to(ROOT)} ({len(pairs)} parameters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

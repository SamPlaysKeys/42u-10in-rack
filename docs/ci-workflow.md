# CI workflow (to be installed manually)

GitHub blocks API-created workflow files: writing to `.github/workflows/` needs a token
with the `workflow` scope, which the tooling that built this repo did not have. So this
one file has to be added by hand, once.

## How to install it

**Option A — web UI.** Repo → **Actions** → **New workflow** → **set up a workflow
yourself**, name it `inventory-check.yml`, and paste the contents below.

**Option B — local clone** with a token that has `workflow` scope:

```bash
git clone https://github.com/SamPlaysKeys/42u-10in-rack.git
cd 42u-10in-rack
mkdir -p .github/workflows
$EDITOR .github/workflows/inventory-check.yml   # paste from below
git add .github/workflows/inventory-check.yml
git commit -m "tooling: add the inventory check workflow"
git push
```

## What it does

1. Runs `scripts/validate_inventory.py`, which fails the build on a missing field, a U
   collision, a device wider than the design envelope, or a `rack/layout.md` allocation
   table that disagrees with `inventory/devices.yaml`.
2. Regenerates `src/openscad/params.scad` and fails if the working tree changed, catching
   a spec edit that was not propagated into the generated include.

It only runs when `inventory/`, `rack/`, or the validator itself changes.

## The file

```yaml
name: Inventory check

on:
  push:
    paths:
      - "inventory/**"
      - "rack/**"
      - "scripts/validate_inventory.py"
      - ".github/workflows/inventory-check.yml"
  pull_request:
    paths:
      - "inventory/**"
      - "rack/**"
      - "scripts/validate_inventory.py"
  workflow_dispatch:

jobs:
  validate:
    name: Validate inventory against the rack spec
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install --quiet pyyaml

      - name: Validate inventory
        run: python3 scripts/validate_inventory.py

      - name: Check params.scad is up to date
        run: |
          python3 scripts/params_to_scad.py
          if ! git diff --quiet -- src/openscad/params.scad; then
            echo "::error::src/openscad/params.scad is out of date."
            echo "Run: python3 scripts/params_to_scad.py  and commit the result."
            git --no-pager diff -- src/openscad/params.scad
            exit 1
          fi
```

## Until it is installed

Run the validator by hand before committing anything that touches `inventory/` or
`rack/`:

```bash
python3 scripts/validate_inventory.py
```

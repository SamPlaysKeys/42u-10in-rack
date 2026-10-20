# Exports

Batched STL sets for a print run, named by date:

```
exports/
└── 2026-11-02-module-1-and-rails/
    ├── frame-module-6u.stl
    ├── rail-segment-6u.stl
    └── MANIFEST.md      what is in the batch, its settings, and its measured result
```

Individual part exports live in the part's own directory — see `models/README.md`. This
directory is only for batches, so that "what did I actually print on that date" has an
answer.

A batch is not complete until it has a `MANIFEST.md` and a matching row in
`printing/print-log.md`.

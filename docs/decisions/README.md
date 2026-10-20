# Architecture Decision Records

Short records of decisions that are expensive to reverse. One file per decision, numbered,
never deleted — superseded decisions get a status change and a pointer to the replacement.

Format: Context → Options → Decision → Consequences. Keep them short enough to read in
a minute.

## Index

| # | Decision | Status |
| :--- | :--- | :--- |
| [0001](0001-rack-architecture.md) | Rack architecture: modular 6U segments | **Proposed** |
| [0002](0002-fastener-and-rail-system.md) | Fastener and rail system | **Proposed** |
| [0003](0003-rack-depth.md) | Rack depth | **Proposed** |
| [0004](0004-printer-and-material.md) | Printer and material | **Proposed** |

## Status values

- **Proposed** — written up, not yet decided. Open for comment.
- **Accepted** — decided. Change requires a superseding ADR.
- **Superseded by NNNN** — replaced.
- **Rejected** — considered and turned down; keep the reasoning.

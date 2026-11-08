# Skill protocol reference

The five flows share a verified transaction shape:

1. **Inspect** the authorized source and runtime capabilities.
2. **Snapshot** or preserve original inputs unchanged.
3. **Normalize** only the user-selected categories with provenance.
4. **Preview** creates, updates, skips, conflicts, unsupported items, and user actions.
5. **Authorize** the exact outbound files, destination, and changes.
6. **Apply** only through verified capabilities.
7. **Read back** destination results where possible.
8. **Report** per-item outcomes and unresolved work.

Backup normally stops after validation and packaging. Restore and migration add destination application. Sync compares a canonical revision with supplied snapshots and generates a proposed next revision. Configuration migration maps user-visible intent; credential values never move, and automations remain disabled until verified.

Capability states are `verified`, `unavailable`, `unknown`, and `needs-user-action`. Outcome states are `verified`, `applied-unverified`, `failed`, `not-attempted`, and `unsupported`.

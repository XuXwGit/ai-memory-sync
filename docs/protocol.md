# Protocol v1

## Record envelope

Every `records.json` item has:

- `id`: stable within `source_account`
- `kind`: memory, conversation, project, task, config, or automation
- `source_account` and `source_platform`: provenance aliases, not credentials
- `updated_at`: source timestamp with timezone, or `null` when unknown
- `scope`: `shared` or `account_only`
- `provenance`: human-readable source reference
- `explicit`: whether the user/source stated it directly
- `data`: kind-specific fields defined by `schemas/v1`

Identity is the pair `(source_account, id)`. A missing record is not a deletion. The MVP does not implement deletion propagation or automatic conflict merging.

## Package

The package contains exactly `manifest.json` and `records.json`. The manifest fixes format version 1.0, record count, SHA-256, selective coverage, exclusions, reference-context restore mode, and `native_import_verified: false`.

## Operations

`scan` performs a conservative secret heuristic. `pack` validates records, blocks scan findings, and creates a new local package. `validate` rechecks schemas, scan, count, and checksum. `preview` selects records for a named destination but does not change it. It defaults to `shared` records and excludes `explicit: false` records. These operations issue local evidence only, never proof of a platform import.


Privacy note: `preview --scope` filters the report only, not the underlying package. Never upload that original package as if unselected records were removed. Build a separate package from only the approved records for sharing. A valid package means format/integrity checks passed; `privacy_review=required` remains in the manifest. Secret scanning is heuristic, not a privacy clearance.

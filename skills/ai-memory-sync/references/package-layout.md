# Package layout reference

The only valid v1 portable layout is:

```text
manifest.json
records.json
```

No extra files are allowed inside the package. `records.json` is an array. Each record needs `id`, `kind`, `source_account`, `source_platform`, `updated_at`, `scope`, `provenance`, `explicit`, and type-specific `data`. Use `updated_at: null` if the original update time is unknown. `kind` is memory, conversation, project, task, config, or automation. `scope` is shared or account_only. Automation records contain definitions, never credentials, and remain disabled after migration.

The packer generates the manifest, including the SHA-256 of `records.json`. A context view or report can be delivered separately, but is not part of the v1 package.

Keep original exports outside the normalized package or in a clearly separated source archive. Never overwrite them. A draft produced in plain chat is not valid until the project validator passes.


Privacy note: `preview --scope` filters the report only, not the underlying package. Never upload that original package as if unselected records were removed. Build a separate package from only the approved records for sharing. A valid package means format/integrity checks passed; `privacy_review=required` remains in the manifest. Secret scanning is heuristic, not a privacy clearance.

# AI Memory Sync

AI Memory Sync is a prompt-first, platform-neutral way to make a **portable, user-reviewed context package** from information you choose to provide. Copy [`START.md`](START.md) into an AI chat to begin. No installation, account connection, or skill support is required.

The MVP handles six user-owned data areas:

- memory and preferences
- conversations and summaries
- projects
- tasks
- user-visible configuration
- automation definitions

It does **not** claim access to hidden platform memory, internal state, unavailable chat history, credentials, or other data an AI cannot actually read. Secrets such as passwords, tokens, private keys, recovery codes, and payment details are excluded.

## Five-minute start

1. Open [`START.md`](START.md) and copy the entire prompt into the AI you want to use.
2. Choose `demo` to try the workflow with synthetic data, or `real` to use data you explicitly supply or authorize the AI to read.
3. Pick a flow: `backup`, `restore`, `migrate`, `sync`, or `config-migration`.
4. Review the proposed scope, exclusions, capability report, and any outbound upload before authorizing an action.
5. Save the produced portable package somewhere you control. A valid v1 package contains exactly `manifest.json` and `records.json`.

For a real backup, official account exports or files you provide are preferred. Keep original exports unchanged. The normalized package is a derivative, not a replacement for the source.

## What “sync” means in this MVP

“Sync” currently means comparing user-supplied packages, proposing changes, and producing a reviewed next package. It does not mean unattended cross-platform synchronization. The local CLI being developed alongside these prompts only packs, validates, and previews local data. It does not upload to GitHub, write native AI memory, create schedules, or modify remote accounts.

## Optional local validator

The copy/paste flow needs no installation. The optional CLI needs Python and the declared `jsonschema` dependency. It is local-only: no network upload, native import, or account modification.

```bash
python scripts/ams.py scan INPUT.json
python scripts/ams.py pack INPUT.json OUTPUT_DIR
python scripts/ams.py validate PACKAGE_DIR
python scripts/ams.py preview PACKAGE_DIR --destination DESTINATION_ALIAS
python scripts/ams.py preview PACKAGE_DIR --destination DESTINATION_ALIAS --scope shared --scope account_only
```

`scan` is heuristic and cannot guarantee safety. `pack` expects a schema-valid JSON array and refuses an existing output directory. `validate` requires exactly `manifest.json` and `records.json` and verifies schema, record count, secret scan, and checksum. `preview` is read-only and selects only `shared` records by default; add both `--scope` flags only after reviewing account-only content.

## Repository layout

- [`START.md`](START.md): self-contained copy/paste entry prompt, Chinese-first
- [`prompts/core.md`](prompts/core.md): shared behavior contract
- [`prompts/flows/`](prompts/flows): focused flow prompts
- [`adapters/`](adapters): runtime capability questions and platform notes
- [`skills/ai-memory-sync/SKILL.md`](skills/ai-memory-sync/SKILL.md): optional skill wrapper
- [`docs/`](docs): architecture, protocol, privacy, recovery, and roadmap

## Storage and sharing model

The public project repository should contain only code, prompts, documentation, schemas, and synthetic examples. Real user packages belong in a separate private location or private repository. A private repository reduces exposure but does not make uploads risk-free. Before any upload, confirm the exact destination, files, account/workspace, and sharing scope. Never put credentials in a package or prompt.

## Current status

This is an experiential MVP. Demo mode is synthetic. Real platform actions have not been tested end to end, and adapter documents are not proof of current account capabilities. At runtime, the AI must report each needed capability as `verified`, `unavailable`, `unknown`, or `needs user action` and must not claim success without evidence.

## Language

The primary launch prompt and Chinese guide are in [`START.md`](START.md) and [`README.zh-CN.md`](README.zh-CN.md). Other documents use concise English so the protocol is easier to reuse across assistants.

## Preview distribution

See [TRY-ME.md](TRY-ME.md) for the two-minute synthetic walkthrough and [validation report](docs/validation-report.md) for exactly what was tested. License selection is pending before public publication.


Privacy note: `preview --scope` filters the report only, not the underlying package. Never upload that original package as if unselected records were removed. Build a separate package from only the approved records for sharing. A valid package means format/integrity checks passed; `privacy_review=required` remains in the manifest. Secret scanning is heuristic, not a privacy clearance.

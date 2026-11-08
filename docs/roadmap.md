# Roadmap

## MVP: current

- self-contained copy/paste prompt
- synthetic demo data
- schemas for six record kinds
- local secret scan, pack, validate, and destination preview
- exact checksum and record-count verification
- default exclusion of `account_only` records
- platform capability checklists with no unsupported claims

## Next

- richer local reports and field-level preview
- explicit change and conflict files in a future versioned format
- recovery receipts and idempotent resume design
- tests using user-obtained, sanitized export samples where permission allows
- runtime-verified, read-only export adapters

## Later, only after testing

- separately authorized storage adapters
- one-writer remote commit protocol with revision checks
- verified destination writers and read-back
- automation reconstruction with duplicate-run protection

Not planned for the current MVP: hidden platform-data extraction, credential transfer, unattended bidirectional sync, destructive remote deletion, or claims of universal native chat/memory import.

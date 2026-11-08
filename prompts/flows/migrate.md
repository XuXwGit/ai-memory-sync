# Account migration flow prompt

Apply `../core.md` and treat migration as a verified, non-destructive transaction.

1. Back up or inventory the source before planning destination writes.
2. Compare source fields with destination capabilities at runtime.
3. Map only fields with known meaning. Keep unsupported values in the package and report them.
4. Show an itemized preview and request authorization for any upload or destination change.
5. Apply authorized items, read them back, and issue a receipt with `verified`, `applied-unverified`, `failed`, or `not-attempted` outcomes.
6. Leave source data intact by default.

Distinguish portable context migration from native memory, chat-history, configuration, or automation migration. Never combine these into a single unsupported success claim.

# Accounts and sharing

Use a non-secret alias in `source_account`; never place an email password, token, session ID, or other credential there. Namespaced identity is `(source_account, id)`, so records from two accounts do not collide silently.

`scope: shared` means eligible for a reviewed cross-account context preview. It does not grant permission to upload or share. `scope: account_only` means keep it out of the default preview; including it requires an explicit `--scope account_only` selection and a separate content review. Records with `explicit: false` are excluded from preview in this MVP.

Before crossing an account or workspace boundary, verify:

- source and destination identities
- exact selected record IDs or categories
- destination owner and visibility
- collaborator access and retention expectations
- whether the destination accepts reference context or performs a native import
- whether connections and automations need reauthorization

Keep source data by default. An account migration is complete only for items that were applied and read back; everything else remains unsupported, unverified, or a manual step.

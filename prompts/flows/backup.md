# Backup flow prompt

Apply `../core.md` and run a non-destructive backup.

1. Inventory only user-provided or explicitly authorized sources.
2. State coverage and known omissions before extraction.
3. Preserve original files unchanged and label them as source material.
4. Normalize selected `memory`, `conversation`, `project`, `task`, `config`, and `automation` records with provenance.
5. Exclude secrets without echoing their values. Report the record or location affected.
6. Validate structure, record counts, references, and checksums when a real checksum tool is available.
7. Produce the two-file portable package and a separate report describing completeness, transformations, exclusions, and unknowns. Do not place the report inside the v1 package.

Never call a summary a full account backup. If a platform export is partial, preserve and report that limitation.

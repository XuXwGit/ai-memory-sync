# Configuration migration flow prompt

Apply `../core.md` to migrate user-visible configuration intent and automation definitions.

1. Inventory explicit preferences, custom instructions, tool or connector names, project conventions, and automation definitions visible in authorized sources.
2. Exclude hidden platform settings and all credential values. Represent credentials only as `reconnect-required`.
3. Normalize intent before mapping platform-specific fields.
4. Mark each target mapping `verified`, `unsupported`, `unknown`, or `needs-user-action`; do not invent target setting names.
5. Preview changes and possible behavior differences.
6. Recreate only items the user authorizes and the destination can actually support.
7. Leave migrated automations disabled until schedule, timezone, permissions, data sources, destination, and duplicate-run risk are verified.
8. Produce a checklist and receipt. Account migration and package schema migration are separate operations.

# Configuration migration

Configuration migration carries user-visible **intent**, not hidden settings or credentials.

Portable examples include response-language preferences, project conventions, selected skill descriptions, connection names, and sync policy. Connection records set `requires_reauthorization: true`; they never contain tokens. Platform-specific setting names are added only after runtime verification.

Automation records preserve title, schedule text, timezone, and the fact that reauthorization is required. `enabled_on_destination` is always `false` in v1. Recreating or enabling an automation is a separate platform action requiring capability checks, destination authorization, and duplicate-run review.

Recommended flow:

1. inventory authorized, user-visible configuration;
2. normalize intent into v1 config and automation records;
3. preview the destination mapping;
4. mark each item verified, unsupported, unknown, or needs user action;
5. recreate authorized items through a verified platform path;
6. read back behavior and keep automations disabled until checked.

Package schema migration is a different operation from account configuration migration.

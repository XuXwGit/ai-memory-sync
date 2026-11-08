# ChatGPT adapter

Status: **needs runtime verification**. This MVP has not tested ChatGPT account export, import, memory write, repository write, or schedule creation end to end.

Confirm the current ChatGPT surface, plan/workspace, available tools, and the exact source files. Do not assume a capability from a product label or from capability in a different chat.

## Verify separately

- whether an official export supplied by the user is complete for the requested period
- whether uploaded conversations become reference material or actual native chat entries
- whether saved memory can be enumerated, written, and read back
- whether custom instructions or other user-visible configuration can be read and written
- repository read and repository write
- scheduled-task creation, listing, and state
- destination account/workspace identity

Use a supplied export as preserved source material. If the destination can only read `context.md`, call the result a portable context restore. Never infer that chat history, saved memory, custom instructions, account settings, or schedules were migrated together.

# Muse adapter

Status: **needs runtime verification**. No Muse action has been tested by this MVP.

Before using a Muse surface, identify the exact product and account context. A product name alone does not prove file access, persistent memory, repository write access, schedules, or import support.

## Verify separately

- Can this conversation read each user-provided file completely?
- Can it enumerate user-visible memory, or only use context already in the chat?
- Can it create files, and can the user retrieve them?
- Is repository access available? Test read and write independently; do not infer write from read.
- Can it create an automation in this surface and show a stable identifier?
- Can it import native history, or only read a portable context document?
- Can every write be read back?

Until verified, use the generic adapter. For restore, provide `context.md` and a manual checklist. For automation, preserve disabled definitions only. Do not describe a context upload as native memory or chat-history restoration.

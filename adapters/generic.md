# Generic adapter

Use this adapter when the assistant or platform is unknown, or when no platform-specific capability has been verified.

## Safe baseline

Assume only that the assistant can read the current message and reply with text. Do not assume files, persistent memory, account export, repository access, native imports, background execution, or scheduling.

## Runtime probe

For the requested flow, report each item as `verified`, `unavailable`, `unknown`, or `needs-user-action`:

| Capability | Evidence required |
| --- | --- |
| Read user-supplied text | Content is visible in this chat |
| Read an uploaded file | File contents were actually returned |
| Create a downloadable file | A real attachment or saved file exists |
| Enumerate source records | A tool returned a list and scope |
| Write and read back destination data | Write result plus independent read-back |
| Repository read/write | Separate proof for read and write |
| Native memory read/write | Separate proof for enumeration and write |
| Native chat import | Documented UI/tool plus observed result |
| Create schedules | Created schedule plus visible identifier/state |

When a capability is absent, fall back to copyable package sections and manual steps. A text-only result is still useful if it is labeled honestly.

## Mapping

Keep the portable fields unchanged. Add platform-specific fields only after observing their meaning. Store unsupported fields in the package rather than dropping them silently.

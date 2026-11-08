# Grok adapter

Status: **needs runtime verification**. No Grok action has been tested by this MVP.

First identify the exact Grok product, surface, account, and workspace. Chat, coding, agent, connector, and automation surfaces may expose different capabilities; do not transfer assumptions between them.

## Verify separately

- uploaded-file reading and size/format limits
- user-visible memory enumeration and write support
- conversation export and native-history import
- repository read versus repository write
- schedule or event-trigger creation and its execution account
- file creation and retrieval
- post-write read-back

If a repository connector only returns content, mark write as `unknown` or `unavailable`. If an exported transcript can be read but not imported as native history, report a portable context restore only. Keep automation definitions disabled until the destination schedule and permissions are verified.

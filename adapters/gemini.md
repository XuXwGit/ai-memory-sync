# Gemini adapter

Status: **needs runtime verification**. No Gemini action has been tested by this MVP.

Confirm the exact Gemini product, account type, region, workspace, and current tool surface. Do not assume that a feature visible in one surface is available in another.

## Verify separately

- upload and download support, including actual format and size limits
- conversation archive reading versus native-history import
- user-visible memory or instruction read/write
- skill/package upload and whether included scripts may run
- repository snapshot/read versus repository write or ongoing sync
- schedule creation, eligibility, and execution identity
- post-write read-back

If repository content is a snapshot, describe it as a snapshot, not sync. If a portable prompt or skill can be loaded but account data cannot be restored, report workflow portability separately from data portability. Keep automation definitions disabled until recreated and verified.

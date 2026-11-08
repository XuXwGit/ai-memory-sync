# Recovery

## Local package failure

Never overwrite the source JSON or an existing output directory. If packing is interrupted, treat the output as incomplete and run `validate` before use. On checksum, schema, count, or secret-scan failure, stop and correct a copy of the source; do not weaken validation.

## Destination failure

Use an itemized preview before writes. Record which items were verified, applied but unverified, failed, unsupported, or not attempted. Before retrying, read the destination to avoid duplicates. The current CLI does not perform destination writes, so recovery there consists of regenerating or revalidating a local package.

## Source recovery

Keep official exports unchanged and separately backed up. A normalized package is selective and may be lossy; it is not a substitute for the original. Do not infer deletion from absence in a later snapshot.

## Restore drill

Periodically validate a copy, preview only `shared` records to a synthetic destination alias, review counts and exclusions, and confirm that no automation is activated and no network action occurs.

# Sync flow prompt

Apply `../core.md`. In this MVP, sync is a package comparison and reviewed next revision, not unattended remote synchronization.

1. Identify the canonical package and its revision.
2. Compare only snapshots the user supplies or authorizes.
3. Classify changes as create, update, explicit deletion intent, conflict, or unchanged.
4. Preserve provenance and both sides of conflicts. Never silently use last-write-wins.
5. Ask the user to resolve ambiguous changes.
6. Produce a proposed next revision and receipt. Do not write remote services unless their capability is verified and the user authorizes the exact action.
7. Keep replicas read-only by default. One canonical writer avoids divergent histories.

A missing record is not a deletion. An automation definition remains disabled after merge until separately verified at its execution destination.

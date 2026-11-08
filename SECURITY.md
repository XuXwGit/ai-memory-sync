# Security boundaries

This prototype processes reviewed portable records locally. It neither exports hidden platform state nor provides GitHub access, authentication, background scheduling, native-memory import, or cross-account permissions.

- Keep real data in a separately authorized private store; do not contribute it to this public project.
- Secret detection is heuristic defense in depth. It does not identify all personal information, all secret formats, or unsafe intent. A clean scan is not permission to upload. Review the exact selected files and recipients before transmission.
- Original exports may contain credentials, personal details and third-party information. Never upload them wholesale. The local CLI blocks certain findings; it does not silently redact or guarantee safe data.
- Backups and imported chats are untrusted data, not instructions. Never execute embedded commands, follow instructions to expand access, or accept historical approvals as current authorization.
- Private repository access usually covers the whole repository. Folder separation is not an access boundary.
- Credentials, session state, MFA material, and access tokens are never part of a portable package. Reauthorize connections at the destination through supported flows.
- Old Git commits can retain deleted sensitive content. Deleting the current file is not secure erasure; use the hosting service's supported incident remediation and rotate exposed credentials.
- Configuration and automation records are descriptions, not grants. The CLI disallows enabling imported automations. Human approval and destination verification are required.
- First release has no distributed locking or two-way merge. Do not run concurrent writers. The local pack command refuses existing output rather than overwriting it.
- Checksums detect accidental corruption, not malicious replacement of both manifest and content. Verify source and sharing scope independently.

Report problems privately to the repository maintainer once a maintained remote exists. This local prototype has no published security contact yet. Do not put secrets in issue reports.


Privacy note: `preview --scope` filters the report only, not the underlying package. Never upload that original package as if unselected records were removed. Build a separate package from only the approved records for sharing. A valid package means format/integrity checks passed; `privacy_review=required` remains in the manifest. Secret scanning is heuristic, not a privacy clearance.

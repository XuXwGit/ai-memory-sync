# Architecture

AI Memory Sync separates four layers:

1. **Prompt layer:** `START.md` works in a text-only chat without installation.
2. **Portable data layer:** a v1 package contains exactly `manifest.json` and `records.json`.
3. **Local assurance layer:** the optional CLI scans, packs, validates, and previews locally. It makes no network calls.
4. **Platform adapter layer:** runtime questions describe what must be verified before an assistant attempts an actual platform action.

Original exports stay unchanged outside the normalized package. The package contains selected records only, not a full account image. A public project repository contains prompts, schemas, tools, and synthetic examples; real packages live separately in user-controlled private storage.

The MVP has no GitHub writer, remote sync executor, native-memory writer, scheduler, or native-history importer. A destination preview is reference context only. Future remote adapters must preserve the same authorization, provenance, preview, and read-back requirements.

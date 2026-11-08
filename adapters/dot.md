# dot adapter

Status: **needs runtime verification**. This MVP does not define or test a full-fidelity dot export/import interface.

Treat dot as a runtime that may have tools, memory, tasks, automations, and connected sources, but verify each capability in the current conversation. Internal or hidden state is outside the portable scope.

## Portable scope

- user-confirmed facts and preferences
- user-visible conversation material the user supplies or authorizes
- projects and tasks
- user-visible configuration intent
- automation definitions without secrets or live credentials

## Runtime checks

- What user-visible data can be enumerated now?
- Can files be created and delivered to the user?
- Can source and destination accounts be identified without exposing secrets?
- Is a write capability available for each requested target?
- Can writes be read back?
- Can automations be listed or created, and will recreation cause duplicates?
- Which connectors must the user reconnect in the destination?

Do not attempt to copy internal instructions, private runtime notes, hidden platform data, credentials, or connection tokens. If native restore is not verified, generate a reviewed context package and a manual reconstruction checklist.

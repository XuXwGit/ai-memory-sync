# Runtime capability checklist

Mark each capability `verified`, `unavailable`, `unknown`, or `needs-user-action` and attach evidence:

- read user-supplied text
- read every required uploaded file
- enumerate the selected source scope
- create a retrievable local/downloadable file
- identify destination account or workspace
- upload to the proposed external destination
- read a repository
- write a repository
- enumerate native memory
- write and read back native memory
- import native chat history
- read/write user-visible configuration
- create, list, disable, and verify an automation
- read back every destination write

Do not bundle capabilities. Reading a repository does not establish write access. Reading an archive does not establish native history import. Creating a response does not establish persistent memory. Creating an automation definition does not establish a running schedule.

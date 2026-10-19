---
id: SW-2
type: sw
title: Log each override
status: approved
authored_by: bob
derives_from: [SYS-1, SYS-2]
as_of: 2026-10-19
approval:
  by: carol
  role: engineering
  on: 2026-10-19
  revision: e359cd57c31925215575f848e41e8123b498f26de4f285dfe8599183f915bcb2
  ref: example
---

## Statement
The software shall write an override record when a rate above the limit is confirmed.

## Rationale
Derives from both the confirmation behaviour and the recording requirement; shown here as an example of a requirement with two parents.

## Acceptance criteria
1. Confirming writes one record with user, time, entered rate and limit.
2. A failed write prevents the start and is shown to the nurse.

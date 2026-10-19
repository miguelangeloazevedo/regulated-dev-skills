---
id: SYS-2
type: sys
title: Record every override
status: approved
authored_by: bob
derives_from: [UN-1]
as_of: 2026-10-19
approval:
  by: alice
  role: qa_ra
  on: 2026-10-19
  revision: 7a070e8198e1479d36a901bdf1f34b7ce18b5868da1273814c37c0ca0c6ca1cd
  ref: example
---

## Statement
The system shall record every confirmation of a rate above the limit.

## Rationale
Overrides are the signal post-market surveillance needs to see whether limits are set well.

## Acceptance criteria
1. Each confirmation creates a record with user, time, entered rate and limit.

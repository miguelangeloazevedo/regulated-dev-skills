---
id: TC-1
type: tc
title: Boundary test of the confirmation step
status: draft
authored_by: bob
verifies: [SW-1]
as_of: 2026-10-19
---

## Procedure
Run `rate_guard` with rate equal to the limit, the limit plus one unit, and no limit configured.

## Expected result
Allowed, blocked, blocked.

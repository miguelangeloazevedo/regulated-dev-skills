---
id: TC-2
type: tc
title: Override is logged
status: draft
authored_by: bob
verifies: [SW-2]
as_of: 2026-10-19
---

## Procedure
Confirm an override and read the log. Then simulate a failed log write.

## Expected result
One log entry with user, time, entered rate and limit. After a failed write, start stays disabled and the nurse sees why.

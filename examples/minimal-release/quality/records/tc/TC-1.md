---
id: TC-1
type: tc
title: System test of the schedule
status: approved
authored_by: bob
verifies: [SYS-1, SW-1, SPEC-1]
as_of: 2026-10-19
approval:
  by: carol
  role: engineering
  on: 2026-10-19
  revision: 16ad0f9892e18d42f6f97cd5fce24b0d0716fe417e096c0ed342529f13643cbe
  ref: example
---

## Procedure
Load entries for today and yesterday with mixed sequence numbers; open the view; then remove today's entries.

## Expected result
Today's entries in sequence order; then the empty-day message.

---
id: SW-1
type: sw
title: Render the schedule list
status: approved
authored_by: bob
derives_from: [SYS-1]
as_of: 2026-10-19
approval:
  by: carol
  role: engineering
  on: 2026-10-19
  revision: 8bdf3ecbda953ed1c9360e202142dbe0f024ec495f6cca35c476c091a0a1fc8a
  ref: example
---

## Statement
The software shall render today's entries sorted by the clinician's sequence number.

## Rationale
The sequence number, not the time, carries the clinician's order.

## Acceptance criteria
1. Entries with sequence 1, 2, 3 render in that order.
2. With no entries for today, the screen says so; it never shows yesterday's list.

---
id: SPEC-1
type: spec
title: Schedule view
status: approved
authored_by: bob
specifies: [SW-1]
as_of: 2026-10-19
approval:
  by: carol
  role: engineering
  on: 2026-10-19
  revision: 5f4d1d26a27a470175482a1d5c13d02c51ac7fdf73aa957658324e13ef58a50b
  ref: example
---

## Statement
Module `schedule_view` filters by date and sorts by sequence number.

## Rationale
One pure function is easy to test at its boundary.

## Acceptance criteria
1. `today(entries, date)` returns entries for that date sorted by sequence.

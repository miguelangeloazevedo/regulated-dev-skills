---
id: SW-1
type: sw
title: Block start above the limit until confirmed
status: approved
authored_by: bob
derives_from: [SYS-1]
implements: [RC-1]
as_of: 2026-10-19
approval:
  by: carol
  role: engineering
  on: 2026-10-19
  revision: fe124ac6de7119d8e681b94f3db555f5e65417ca4195aeaa117dfdaf90bb2dec
  ref: example
---

## Statement
The software shall compare the entered rate with the prescribed limit and disable the start command until the nurse confirms or corrects a rate above it.

## Rationale
Disabling the command, rather than only showing a message, makes the control independent of whether the warning was read.

## Acceptance criteria
1. A rate of limit plus one unit disables start and shows the warning.
2. A rate equal to the limit does not.
3. When no limit is configured, start is disabled and the screen says the limit is missing. Absence never reads as no limit.

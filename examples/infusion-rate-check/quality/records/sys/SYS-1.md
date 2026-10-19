---
id: SYS-1
type: sys
title: Warn and require confirmation above the limit
status: approved
authored_by: bob
derives_from: [UN-1]
as_of: 2026-10-19
approval:
  by: alice
  role: qa_ra
  on: 2026-10-19
  revision: 3b272c12fdca2013fabc3eb8a40ea907d197e9614c77a13b356ac1782682867c
  ref: example
---

## Statement
The system shall warn and require an explicit confirmation before starting an infusion whose rate exceeds the prescribed limit.

## Rationale
A warning alone is easy to dismiss by habit; a confirmation step forces a decision.

## Acceptance criteria
1. Entering a rate above the limit shows a warning naming the entered rate and the limit.
2. The infusion cannot start until the nurse confirms or corrects the rate.

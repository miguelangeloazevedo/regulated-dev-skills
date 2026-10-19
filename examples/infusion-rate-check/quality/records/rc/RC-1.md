---
id: RC-1
type: rc
title: Confirmation step above the prescribed limit
status: approved
authored_by: bob
mitigates: [HAZ-1]
as_of: 2026-10-19
approval:
  by: alice
  role: qa_ra
  on: 2026-10-19
  revision: 617da3909ba4d067ba5575f2facd9c43ee150e3460410685d335d732ce512810
  ref: example
---

## Control
Software confirmation step above the prescribed limit (SW-1), verified by TC-1.

## Mechanism
The start command is disabled in code until the nurse confirms or corrects the rate.

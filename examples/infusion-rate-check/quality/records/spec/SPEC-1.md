---
id: SPEC-1
type: spec
title: Rate entry guard
status: approved
authored_by: bob
specifies: [SW-1, SW-2]
as_of: 2026-10-19
approval:
  by: carol
  role: engineering
  on: 2026-10-19
  revision: 8a5206d61779e9b1de4bd8936d61e8c26aab1a48cfde506903a5df1f7c2efc14
  ref: example
---

## Statement
Module `rate_guard`: a pure function decides whether start is allowed from (rate, limit); the UI calls it on every change. The override log is written before start is enabled.

## Rationale
A pure decision function can be tested exhaustively at its boundary.

## Acceptance criteria
1. `allowed(rate, limit)` is false when rate > limit or limit is missing.

## Refuses
It does not adjust the rate automatically: a silent correction would hide the error from the nurse.

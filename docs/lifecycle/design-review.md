<!-- docs page for skills/lifecycle/design-review/SKILL.md -->

## What it does

Prepares and records a design review at a stage the plan names: what was read, by whom, what was found, and whether the design can meet its requirements. The agent prepares the pack and the record; the people in the room decide.

## When to reach for it

Type `/design-review`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| A planned review stage is reached. | `design-review` |
| A baseline is about to be approved. | `design-review` |
| Reviewing one unit's code | [`unit-verification`](../lifecycle/unit-verification.md) |

## Prerequisites

A development plan that names review stages.

## The read-list

Design reviews happen at each stage the development plan names, not once at the end. Each record carries a **read-list** naming every item each participant actually read, the findings with owners, and an explicit statement on whether the design can meet its requirements.

## It's working if

- Every review record has a read-list and an explicit statement.
- Absent functions are recorded, not hidden.

## Where it fits

Role: chain step. Neighbours: [`approve`](../gates/approve.md), because approval of a baseline follows its review; [`traceability`](../regulated/traceability.md), because the pack is built from the link graph. For the whole map, see [FLOWS.md](../../FLOWS.md).

<!-- docs page for skills/lifecycle/unit-verification/SKILL.md -->

## What it does

Verifies each software unit against acceptance criteria derived from its specification, test-first, by the methods the class asks for. A test that has never failed has not been shown to detect anything.

## When to reach for it

Type `/unit-verification`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| A unit is being built or changed. | `unit-verification` |
| A unit's acceptance criteria need writing. | `unit-verification` |
| Integration or system testing | [`verify`](../regulated/verify.md) |

## Prerequisites

A specified unit and agreed seams.

## Red first

Each test is written against the unit's acceptance criteria, at an agreed seam, and goes **red first**. For the tests that guard a risk control, red is kept as evidence. Code review is a verification method here, on two axes that are never merged: the project's standards, and the specification.

## It's working if

- Every test went red before it went green.
- Renaming an internal function breaks nothing.
- Risk-control tests have recorded red runs.

## Where it fits

Role: chain step. Neighbours: [`implement`](../lifecycle/implement.md), because it builds test-first through this skill; [`verify`](../regulated/verify.md), because integration and system testing come next, by someone else. For the whole map, see [FLOWS.md](../../FLOWS.md).

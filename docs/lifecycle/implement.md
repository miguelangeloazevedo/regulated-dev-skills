<!-- docs page for skills/lifecycle/implement/SKILL.md -->

## What it does

Builds one software unit from its specification and hands it to unit verification. There is no code without a specification, and no specification without requirements.

## When to reach for it

Type `/implement`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| A unit is specified and its blockers are done. | `implement` |
| The unit has no specification | [`specifications`](../lifecycle/specifications.md) |
| Something is broken | [`problem-resolution`](../lifecycle/problem-resolution.md) |

## Prerequisites

A ticket.

## No code without a specification

There is **no code without a specification**, and no specification without requirements. `implement` builds one unit at a time, test-first through `unit-verification`, and commits with the unit, specification and requirement ids in the message.

## It's working if

- Each commit cites its ticket and records.
- Failures in new code reach the user as messages, not as waits.

## Where it fits

Role: chain step. Neighbours: [`specifications`](../lifecycle/specifications.md), because each unit it builds is specified there; [`unit-verification`](../lifecycle/unit-verification.md), because it builds test-first through it. For the whole map, see [FLOWS.md](../../FLOWS.md).

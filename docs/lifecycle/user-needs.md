<!-- docs page for skills/lifecycle/user-needs/SKILL.md -->

## What it does

Writes the user needs the design answers to: who must be able to do what, and why, within the intended purpose `intake` fixed. A need never names a mechanism, and every need says how it will be validated.

## When to reach for it

Type `/user-needs`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| The product is classified and the needs are not written yet. | `user-needs` |
| A new intended use, user group or use environment appears. | `user-needs` |
| Requirements exist with no need above them. | `user-needs` |
| The product is not classified | [`intake`](../gates/intake.md) |
| Turning needs into system behaviour | [`requirements`](../lifecycle/requirements.md) |

## Prerequisites

An approved `CLS` record from `intake`.

## Who, what, why

A user need names **who, what, why**: a person, a capability, and the reason it matters. It never names how. Every need carries the method that will validate it with real users in the real environment.

## It's working if

- Every need reads as something a person must be able to do.
- Each user group in the intended purpose has needs.

## Where it fits

Role: chain step. Neighbours: [`intake`](../gates/intake.md), because it fixes the intended purpose the needs sit inside; [`requirements`](../lifecycle/requirements.md), because it turns each need into system behaviour; [`validation`](../lifecycle/validation.md), because it shows each need is met with intended users. For the whole map, see [FLOWS.md](../../FLOWS.md).

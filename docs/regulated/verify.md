<!-- docs page for skills/regulated/verify/SKILL.md -->

## What it does

Runs integration and system testing on the exact revision and keeps verification apart from validation. Models may do the work; under this repository's rule, at class B and C a named human independent of the build signs each result, and an unsigned result is recorded as a pre-check.

## When to reach for it

Type `/verify`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| A revision is ready for verification. | `verify` |
| Evidence has become stale after a change. | `verify` |
| Checking a unit during build | [`unit-verification`](../lifecycle/unit-verification.md) |

## Prerequisites

A revision and test cases.

## The exact revision

Verification runs on the **exact revision** under test. Models may do the work. At class B and C, a named human who did not build the revision signs each result; until then the result is a pre-check. A failed run keeps its red result and makes earlier evidence stale.

## It's working if

- Every result names a revision and a verifier kind.
- The run includes a control case that failed on purpose.

## Where it fits

Role: chain step. Neighbours: [`unit-verification`](../lifecycle/unit-verification.md), because the builder's own checks, not independent; [`release`](../gates/release.md), because it reads verify's results. For the whole map, see [FLOWS.md](../../FLOWS.md).

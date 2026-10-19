<!-- docs page for skills/lifecycle/problem-resolution/SKILL.md -->

## What it does

Takes a problem from report to verified fix: records it, builds a loop that reproduces it, assesses its safety relevance, raises a change request, fixes it, and checks the fix. It never decides whether a problem must be reported to an authority; it flags it for the person who does.

## When to reach for it

Type `/problem-resolution`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| A defect, a failing test, a field complaint or an anomaly in SOUP. | `problem-resolution` |
| A flaky or intermittent failure. | `problem-resolution` |
| A change to intended behaviour, not a defect | [`impact`](../gates/impact.md) |

## A tight loop

One command that goes red on this problem, small and fast, before anyone theorises. A **tight loop** is the method; the problem report, safety assessment and change request are what make it regulated.

## It's working if

- There is a command that was red and is now green.
- Every problem report has a safety relevance entry.

## Where it fits

Role: standalone. Neighbours: [`risk`](../regulated/risk.md), because it assesses safety relevance there; [`impact`](../gates/impact.md), because a fix that changes behaviour is priced there. For the whole map, see [FLOWS.md](../../FLOWS.md).

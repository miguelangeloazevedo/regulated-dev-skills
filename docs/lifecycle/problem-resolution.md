<!-- docs page for skills/lifecycle/problem-resolution/SKILL.md -->

## What it does

Takes a problem from report to an authorised disposition: assess safety and interim protection, investigate with evidence, verify required changes or justify no software change, and hand off complaint/CAPA decisions. A green regression is not CAPA effectiveness or quality-event closure. Reportability and closure decisions belong to people.

## When to reach for it

Type `/problem-resolution`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| A defect, a failing test, a field complaint or an anomaly in SOUP. | `problem-resolution` |
| A flaky or intermittent failure. | `problem-resolution` |
| A change to intended behaviour, not a defect | [`impact`](../gates/impact.md) |

## Techniques and timing

Select methods for the approved plan and lifecycle stage; the guides distinguish evidence and human decisions:

- [Intake, investigation, action and effectiveness handoff](../../skills/lifecycle/problem-resolution/references/quality-event-handoff.md).
- [Fictional engineering/CAPA boundary example](../../skills/lifecycle/problem-resolution/references/worked-example.md).

## Lifecycle handoff

Carry the originating event and affected scope through containment, evidence-backed occurrence/escape/systemic investigation, authorised action and separate effectiveness/closure handoffs. A software fix does not close its complaint or CAPA.

## A tight loop, not the whole quality event

A **tight loop** is useful engineering evidence when the problem can be reproduced. The endpoint is an authorised disposition, not a compulsory code patch. Safety and interim protection do not wait for a red command; complaint handling and CAPA effectiveness retain their own owners and decisions.

## It's working if

- Every problem has a safety/protection assessment and an authorised disposition or remains open.
- Software changes retain correction/regression evidence; pending CAPA effectiveness has an owner and monitoring window.

## Where it fits

Role: standalone. Neighbours: [`risk`](../regulated/risk.md), because it assesses safety relevance there; [`impact`](../gates/impact.md), because a fix that changes behaviour is priced there. For the whole map, see [FLOWS.md](../../FLOWS.md).

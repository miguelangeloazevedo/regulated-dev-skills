<!-- docs page for skills/lifecycle/maintenance/SKILL.md -->

## What it does

Keeps released software safe: plans maintenance, takes in feedback and complaints, monitors SOUP, sends problems through `problem-resolution` and changes through the chain, and feeds post-market surveillance. Whether an event must be reported to an authority is always a person's decision.

## When to reach for it

Type `/maintenance`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| The software has been released. | `maintenance` |
| Feedback, a complaint, a field problem or a SOUP advisory arrives. | `maintenance` |
| A defect found during development | [`problem-resolution`](../lifecycle/problem-resolution.md) |

## Prerequisites

A released baseline.

## The clock starts at release

Release is not the end of the software's regulated life. **The clock starts at release**: feedback, SOUP anomalies and field problems keep arriving, and some carry reporting deadlines counted in days.

| Jurisdiction | Clock from awareness |
| --- | --- |
| EU, MDR Art 87 | 15 days; 10 days for a death or unanticipated serious deterioration; 2 days for a serious public health threat |
| US, 21 CFR 803 | 30 calendar days; 5 work days when remedial action is needed or FDA asks in writing |

The skill flags and dates; a person decides whether to report.

The skill covers software maintenance and the vigilance flag. The rest of post-market surveillance (the plan, PSUR, trend reports, PMCF, field safety notices, US corrections and removals) belongs to your QMS; the skill names it and asks for an owner.

## It's working if

- Every complaint has a safety evaluation.
- Possible incidents reach a person the day they are seen.

## Where it fits

Role: periodic. Neighbours: [`problem-resolution`](../lifecycle/problem-resolution.md), because problems found after release go through it; [`risk`](../regulated/risk.md), because post-production information updates the risk file. For the whole map, see [FLOWS.md](../../FLOWS.md).

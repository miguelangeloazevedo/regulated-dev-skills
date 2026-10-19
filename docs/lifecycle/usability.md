<!-- docs page for skills/lifecycle/usability/SKILL.md -->

## What it does

Runs the usability engineering process of IEC 62366-1 from the start of development: use specification, safety-related user interface characteristics, hazard-related use scenarios, user interface specification, formative evaluation during design and summative evaluation at the end. It keeps the usability engineering file. People run the evaluation sessions; designers of the interface do not evaluate it.

## When to reach for it

Type `/usability`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| User needs exist and the use specification is due, before architecture. | `usability` |
| The user interface is being designed or changed. | `usability` |
| A production-equivalent interface exists and summative evaluation is due. | `usability` |
| Showing that the product meets its user needs overall | [`validation`](../lifecycle/validation.md) |

## Prerequisites

User needs and a `CLS` record.

## Usability starts first

Usability engineering is its own process (IEC 62366-1), and **usability starts first**: the use specification comes before architecture, formative evaluations run while the design can move, and the summative evaluation closes it on a production-equivalent interface. `validation` then uses its results as evidence for the needs that depend on use.

## It's working if

- The use specification predates the architecture.
- Use errors appear as hazards.

## Where it fits

Role: chain step. Neighbours: [`user-needs`](../lifecycle/user-needs.md), because each need names its users; [`risk`](../regulated/risk.md), because use errors become hazards there; [`validation`](../lifecycle/validation.md), because takes the summative results. For the whole map, see [FLOWS.md](../../FLOWS.md).

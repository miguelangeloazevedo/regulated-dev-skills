<!-- docs page for skills/lifecycle/validation/SKILL.md -->

## What it does

Validates that the finished product meets its user needs and intended use (ISO 13485 7.3.7) by the method each need calls for: summative usability results, simulated use, clinical data through the clinical evaluation, or analysis. It prepares and records; people run the sessions. Usability engineering itself is in `usability`.

## When to reach for it

Type `/validation`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| A production-equivalent build exists and design validation is due. | `validation` |
| A change touches a user need or the intended use. | `validation` |
| Checking the product against requirements | [`verify`](../regulated/verify.md) |
| Use specification, user interface specification, formative or summative evaluation | [`usability`](../lifecycle/usability.md) |

## Prerequisites

User needs with validation methods, and a release candidate.

## Lifecycle handoff

Plan the method with needs and the development plan even though execution needs representative product evidence. Agree with `risk` and `usability` which risk-control effectiveness claims require user-facing evaluation and which can be established by technical verification; do not equate effectiveness verification universally with validation. Keep per-need validation states separate from requirement-verification metrics and host execution statuses.

## Intended users, intended environment

Validation answers a different question from verification: does the product meet the needs of **intended users, intended environment**, not does it meet its requirements. It takes the summative results from `usability` as evidence for needs that depend on use, and clinical evidence from the clinical evaluation.

## It's working if

- Participants match the user groups in the use specification.
- Use errors appear as hazards.

## Where it fits

Role: chain step. Neighbours: [`user-needs`](../lifecycle/user-needs.md), because each need carries its validation method; [`usability`](../lifecycle/usability.md), because provides the summative results; [`verify`](../regulated/verify.md), because checks requirements, not needs. For the whole map, see [FLOWS.md](../../FLOWS.md).

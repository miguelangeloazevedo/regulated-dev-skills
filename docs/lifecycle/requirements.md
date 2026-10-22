<!-- docs page for skills/lifecycle/requirements/SKILL.md -->

## What it does

Derives system requirements from user needs and software requirements from system requirements, with risk controls folded in. Every requirement can fail a test, traces to at least one parent, and leaves undecided things blocked rather than softened.

## When to reach for it

Type `/requirements`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| User needs exist and the system behaviour is not specified. | `requirements` |
| A risk control has to become a requirement. | `requirements` |
| A requirement changes. | `requirements` |
| The needs themselves are unclear | [`user-needs`](../lifecycle/user-needs.md) |
| Describing how it is built | [`specifications`](../lifecycle/specifications.md) |

## Prerequisites

User needs, and risk controls where they exist.

## Lifecycle handoff

Plan verification methods while drafting acceptance criteria: partitions and boundaries for ranges, decision/state cases for conditional behaviour, and interface/negative cases where relevant. Distinguish risk-control implementation criteria from effectiveness claims; ask `usability` and `risk` what user-facing evidence is needed. Preserve the class-dependent minimum and the approved plan's additions.

## One field, one question

Each field in a requirement answers a different question: the statement says what, the rationale says why, the criteria say how you will know. **One field, one question**. A record where two fields say the same thing has one field's worth of content.

| Kind of block | Means | Advances? |
| --- | --- | --- |
| `BLOCKED(content)` | A hole in the design | No |
| `BLOCKED(scope)` | An unmade decision about scope | No |
| `BLOCKED(timing)` | The statement is complete; only its test cannot run yet | Yes |

## It's working if

- Every requirement has a scenario that would fail.
- Coverage of needs and risk controls comes from the validator, not from a document.

## Where it fits

Role: chain step. Neighbours: [`user-needs`](../lifecycle/user-needs.md), because every system requirement derives from one; [`specifications`](../lifecycle/specifications.md), because it says how each software requirement is built; [`risk`](../regulated/risk.md), because its controls become requirements here. For the whole map, see [FLOWS.md](../../FLOWS.md).

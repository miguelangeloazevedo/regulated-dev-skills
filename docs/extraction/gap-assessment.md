<!-- docs page for skills/extraction/gap-assessment/SKILL.md -->

## What it does

Assesses existing software against the chain. If it was lawfully placed on the market and is still marketed, it is legacy software and follows the IEC 62304 4.4 route; if not, the gaps are closed by applying clauses 5 to 9 before release.

## When to reach for it

Type `/gap-assessment`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| Software already exists and the records do not. | `gap-assessment` |
| Code or records exist but the chain does not. | `gap-assessment` |
| Starting from nothing | [`requirements`](../lifecycle/requirements.md) |

## Prerequisites

An existing codebase or partial records.

## Legacy or not

Two routes. Software lawfully on the market without enough evidence is legacy software (IEC 62304 3.36) and may follow 4.4: feedback, continued-use risk, gaps, a plan and a rationale. Anything else, unreleased code included, closes its gaps under clauses 5 to 9 before release. Either way, evidence is reused only by matching revision hash: **reuse by hash**, never by resemblance.

## It's working if

- Each gap has a type and an owner.
- Reused evidence is hash-matched.

## Where it fits

Role: chain step. Neighbours: [`design-inputs-from-code`](../extraction/design-inputs-from-code.md), because it supplies candidates for missing records; [`requirements`](../lifecycle/requirements.md), because it writes the missing records. For the whole map, see [FLOWS.md](../../FLOWS.md).

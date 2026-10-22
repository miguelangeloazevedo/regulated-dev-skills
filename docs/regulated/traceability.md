<!-- docs page for skills/regulated/traceability/SKILL.md -->

## What it does

Keeps design and safety traceability intact: needs to evidence, and hazard/situation/harm contexts through controls to their implementing requirements and evidence. Coverage is measured within stated scope, never inferred from links alone.

## When to reach for it

Type `/traceability`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| Adding, changing or linking records. | `traceability` |
| Asked how much of the chain is covered. | `traceability` |
| Reading code to propose records | [`design-inputs-from-code`](../extraction/design-inputs-from-code.md) |

## Prerequisites

Records.

## Techniques and timing

Select methods for the approved plan and lifecycle stage; the guides distinguish evidence and human decisions:

- [Technique selection and procedure](../../skills/regulated/traceability/references/chain-and-coverage.md).
- [Fictional worked example](../../skills/regulated/traceability/references/worked-example.md).

## Computed, not typed

Coverage is **computed, not typed**. Links are stored upward only and the inverse is computed, so a pair can never be stored inverted. Every count in prose carries a marker the validator re-derives.

## It's working if

- Requirements with several parents are visible in the report.
- Coverage numbers come from the validator, not from a document.

## Where it fits

Role: runs inside the chain. Neighbours: [`requirements`](../lifecycle/requirements.md), because it writes the records traceability links; [`impact`](../gates/impact.md), because it walks the same graph; [`risk`](../regulated/risk.md), because the safety chain preserves situation/harm contexts. For the whole map, see [FLOWS.md](../../FLOWS.md).

<!-- docs page for skills/regulated/risk/SKILL.md -->

## What it does

Supports the risk management process by drafting hazards, risk estimates, controls and residual risk evaluations. Acceptability criteria and acceptance belong to people.

## When to reach for it

Type `/risk`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| Identifying hazards or hazardous situations. | `risk` |
| Choosing or verifying a risk control. | `risk` |
| A software change might affect safety. | `risk` |
| Reverse-engineering from code | [`hazards-from-code`](../extraction/hazards-from-code.md) |

## Prerequisites

An intended use statement.

## Techniques and timing

Select methods for the approved plan and lifecycle stage; the guides distinguish evidence and human decisions:

- [Technique selection and procedure](../../skills/regulated/risk/references/analysis-techniques.md).
- [Fictional worked example](../../skills/regulated/risk/references/worked-example.md).
- [Implementation, effectiveness and risk/usability handoff](../../skills/regulated/risk/references/control-evidence.md).

## Lifecycle handoff

Bind estimates to the policy revision, scales, mapping method, context and evidence used. Keep calculated classification, benefit evidence and human acceptance separate; changes require impact review and reapproval, not only recalculation.

## People accept risk

The skill drafts the plan, hazards, estimates, controls, residual and overall risk evaluations, and the risk management review. Acceptability criteria and acceptance belong to people: **people accept risk**, agents draft it.

## It's working if

- Every control names its mechanism and its verification.
- No acceptance is recorded without a person.

## Where it fits

Role: runs inside the chain. Neighbours: [`hazards-from-code`](../extraction/hazards-from-code.md), because it supplies candidates; [`security-diligence`](../regulated/security-diligence.md), because security findings link to hazards here; [`usability`](../lifecycle/usability.md), because early task/scenario inputs and control-effectiveness evidence flow both ways. For the whole map, see [FLOWS.md](../../FLOWS.md).

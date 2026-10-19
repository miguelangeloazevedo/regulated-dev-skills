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

## People accept risk

The skill drafts the plan, hazards, estimates, controls, residual and overall risk evaluations, and the risk management review. Acceptability criteria and acceptance belong to people: **people accept risk**, agents draft it.

## It's working if

- Every control names its mechanism and its verification.
- No acceptance is recorded without a person.

## Where it fits

Role: runs inside the chain. Neighbours: [`hazards-from-code`](../extraction/hazards-from-code.md), because it supplies candidates; [`security-diligence`](../regulated/security-diligence.md), because security findings link to hazards here. For the whole map, see [FLOWS.md](../../FLOWS.md).

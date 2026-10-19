<!-- docs page for skills/extraction/hazards-from-code/SKILL.md -->

## What it does

Finds places where code can affect a person's care and proposes hazard candidates. Hazard analysis needs clinical context this skill does not have, so the output is input to a human-led session, never a result.

## When to reach for it

You invoke this by typing `/hazards-from-code`, and the agent won't reach for it on its own. Propose hazard candidates from an existing codebase.

## Prerequisites

An intended use statement, or an explicit note that the scan is unscoped.

## Where software reaches a person

The scan looks where output reaches a care decision, a device actuator or a stored clinical record, and where fallback behaviour is decided. It proposes **hazard candidates** as sequences of events, never as conclusions.

## It's working if

- The output starts with a framing statement and a coverage section.
- No candidate carries a severity a person did not assign.

## Where it fits

Role: chain step. Neighbours: [`risk`](../regulated/risk.md), because it takes the candidates into the risk process; [`intake`](../gates/intake.md), because it fixes the intended use the scan is scoped to. For the whole map, see [FLOWS.md](../../FLOWS.md).

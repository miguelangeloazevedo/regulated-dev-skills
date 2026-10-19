<!-- docs page for skills/gates/impact/SKILL.md -->

## What it does

Prices a change before you commit to it. Counts come from the link graph, never from memory, and effort is a range with a stated confidence.

## When to reach for it

You invoke this by typing `/impact`, and the agent won't reach for it on its own. Price a change: blast radius from the links, effort as a range.

## Rings

Impact walks the link graph ring by ring: requirements, specifications, tests, documents, baseline. Each ring has a count the validator produced. The **blast radius** is the set of records whose approvals would go stale, plus any permanent item the change touches. For released software, impact also drafts the regulatory question: notified body, new 510(k), or inside a change control plan. A person answers it.

## It's working if

- The numbers in the note match `validate.py records --report`.
- Effort is a range with written assumptions.

## Where it fits

Role: standalone. Neighbours: [`traceability`](../regulated/traceability.md), because it owns the links impact walks; [`intake`](../gates/intake.md), because a change that fires a reclassification trigger goes back there. For the whole map, see [FLOWS.md](../../FLOWS.md).

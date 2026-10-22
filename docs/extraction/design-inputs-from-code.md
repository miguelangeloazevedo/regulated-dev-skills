<!-- docs page for skills/extraction/design-inputs-from-code/SKILL.md -->

## What it does

Reads existing code and proposes design input candidates for a human to accept. It never fills rationale, safety class or the user need as fact.

## When to reach for it

You invoke this by typing `/design-inputs-from-code`, and the agent won't reach for it on its own. Propose design input candidates from an existing codebase.

## Prerequisites

A codebase and a pinned commit.

## Lifecycle handoff

Feed confirmed candidates into requirements and technique planning; attach observed boundaries, decision/state logic and interface assumptions as evidence anchors. Do not infer intended use or adequate verification merely from existing tests or code structure.

## Candidates, not conclusions

The skill reads tests, schemas, configuration, strings, code and history, and proposes requirement candidates anchored to the code. Each candidate is `proposed`. The human-owned fields (rationale, the user need, safety class) are never filled; they become questions for the owner.

The leading idea: **candidates, not conclusions**. Code shows what the software does, not what it should do.

## Common questions

**Can I submit the output as my requirements?**

No. It is a draft that shows what the code does. Requirements state intent, and only the owner can supply that.

## It's working if

- Every candidate names the code it came from and at least one agreeing source.
- A rerun on an unchanged commit produces the same identifiers.

## Where it fits

Role: chain step. Neighbours: [`gap-assessment`](../extraction/gap-assessment.md), because it compares the candidates with what the chain needs; [`requirements`](../lifecycle/requirements.md), because it writes the accepted candidates up as records. For the whole map, see [FLOWS.md](../../FLOWS.md).

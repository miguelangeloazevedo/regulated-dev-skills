<!-- docs page for skills/gates/status/SKILL.md -->

## What it does

Reads the project and reports where it stands, from files, not from the conversation.

## When to reach for it

You invoke this by typing `/status`, and the agent won't reach for it on its own. Where are we: records, stale evidence, open gates, evidence level.

## Prerequisites

A project block.

## Where the numbers come from

Every number in a status report comes from a validator run on a named commit. Every number is **measured, not remembered**. Where something was not measured, the report says `not run`, never zero.

## It's working if

- The report names the commit it was run on.
- Nothing reads as complete because it is empty.

## Where it fits

Role: standalone. Neighbours: [`setup`](../gates/setup.md), because status measures what setup declared; [`design-review`](../lifecycle/design-review.md), because a review pack starts from a fresh status. For the whole map, see [FLOWS.md](../../FLOWS.md).

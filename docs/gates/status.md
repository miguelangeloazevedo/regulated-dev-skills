<!-- docs page for skills/gates/status/SKILL.md -->

## What it does

Reads the project and reports where it stands, from files, not from the conversation.

Typed commands provide invocation control, not an operating-system permission boundary. An instruction or editable approval field does not establish host-enforced authority.

## When to reach for it

You invoke this by typing `/status`, and the agent won't reach for it on its own. Where are we: records, stale evidence, open gates, evidence level.

## Prerequisites

A project block.

## Lifecycle handoff

Report additional evidence dimensions separately from the literal validator output: assessable scope, test association, actual execution/outcome, configuration applicability and control effectiveness. Mark unsupported backend mappings or incomplete retrieval unknown/partial. Do not present these human-reviewed assessments as extra validator fields.

## Where the numbers come from

Every number in a status report comes from a validator run on a named commit. Every number is **measured, not remembered**. Where something was not measured, the report says `not run`, never zero.

Report each assurance property as declared, instruction_observed, host_observed, failed, unsupported, unassessed or stale, with its scope and evidence. Keep host-token probes distinct from actual agent/harness runs and independent regulatory review distinct from structural tests. Read the assurance guide bundled with setup; no private knowledge service is required.

## It's working if

- The report names the commit it was run on.
- Nothing reads as complete because it is empty.

## Where it fits

Role: standalone. Neighbours: [`setup`](../gates/setup.md), because status measures what setup declared; [`design-review`](../lifecycle/design-review.md), because a review pack starts from a fresh status. For the whole map, see [FLOWS.md](../../FLOWS.md).

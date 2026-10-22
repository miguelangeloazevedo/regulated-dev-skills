<!-- docs page for skills/gates/release/SKILL.md -->

## What it does

Checks that the software release activities are done, then records the decision of the person who authorises release. A release is never inferred from passing tests.

## When to reach for it

You invoke this by typing `/release`, and the agent won't reach for it on its own. Release a baseline after verification, package and a human decision.

## Prerequisites

A baseline, verification results and a package.

## Lifecycle handoff

Review risk-control implementation and effectiveness evidence separately, with the applicable configuration and conditions. Confirm that scope/configuration gaps, missing user-facing evidence and incomplete graph retrieval have not been counted as passing coverage. These are human evidence reviews beyond the structural validator; unresolved required evidence is not a green release.

## The checklist

Release computes a checklist from the files, following IEC 62304 5.8 at the depth the class requires: verification complete and signed, residual anomalies documented and evaluated, version and build recorded, plan activities complete, risk review done, archive and delivery set. Then the person who authorises release decides (ISO 13485 8.2.6).

A release is a decision, never an inference from green tests. Every **one-way door** is listed with its decision.

## It's working if

- The release record names a person, a baseline hash and a reference.
- Permanent changes appear as their own lines with decisions, not inside a diff.

## Where it fits

Role: gate. Neighbours: [`verify`](../regulated/verify.md), because its signed results on the baseline revision are what release checks; [`configuration-management`](../regulated/configuration-management.md), because it formed the baseline being released; [`maintenance`](../lifecycle/maintenance.md), because the software's regulated life continues there. For the whole map, see [FLOWS.md](../../FLOWS.md).

<!-- docs page for skills/gates/release/SKILL.md -->

## What it does

Checks that the software release activities are done, then records the decision of the person who authorises release. A release is never inferred from passing tests.

Typed commands provide invocation control, not an operating-system permission boundary. An instruction or editable approval field does not establish host-enforced authority.

## When to reach for it

You invoke this by typing `/release`, and the agent won't reach for it on its own. Release a baseline after verification, package and a human decision.

## Prerequisites

A baseline, verification results and a package.

## Lifecycle handoff

Review risk-control implementation and effectiveness evidence separately, with the applicable configuration and conditions. Confirm that scope/configuration gaps, missing user-facing evidence and incomplete graph retrieval have not been counted as passing coverage. These are human evidence reviews beyond the structural validator; unresolved required evidence is not a green release. Distinguish document approval from effective issue and actual point-of-use availability.

## The checklist

Release computes a checklist from the files, following IEC 62304 5.8 at the depth the class requires: verification complete and signed, residual anomalies documented and evaluated, version and build recorded, plan activities complete, risk review done, archive and delivery set. Then the person who authorises release decides (ISO 13485 8.2.6).

A release is a decision, never an inference from green tests. Every **one-way door** is listed with its decision.

Before claiming controlled release, require structural readiness and the separate trusted host-authority check for the exact requested revision and policy. Unsupported, unavailable, stale or contradicted controls hold the authorisation gate. A green validate.py --release result is structural only. Read the assurance guide bundled with setup; no private knowledge service is required.

## It's working if

- The release record names a person, a baseline hash and a reference.
- Permanent changes appear as their own lines with decisions, not inside a diff.

## Where it fits

Role: gate. Neighbours: [`verify`](../regulated/verify.md), because its signed results on the baseline revision are what release checks; [`configuration-management`](../regulated/configuration-management.md), because it formed the baseline being released; [`maintenance`](../lifecycle/maintenance.md), because the software's regulated life continues there. For the whole map, see [FLOWS.md](../../FLOWS.md).

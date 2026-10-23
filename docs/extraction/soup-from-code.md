<!-- docs page for skills/extraction/soup-from-code/SKILL.md -->

## What it does

Inventories the software the product depends on but did not develop under its own lifecycle: third-party components and previously developed software without adequate records, which is what IEC 62304 calls SOUP. It leaves the judgements to people.

Typed commands provide invocation control, not an operating-system permission boundary. An instruction or editable approval field does not establish host-enforced authority.

## When to reach for it

You invoke this by typing `/soup-from-code`, and the agent won't reach for it on its own. Build a SOUP and SBOM inventory from manifests and lockfiles.

## Prerequisites

Manifests or lockfiles.

## Lifecycle handoff

Reconcile the inventory with built/deployed contents and mark unobserved vendored/dynamic/remote components unknown. Feed component/version deltas to configuration and security analysis, requirements/host needs to design, and anomalies to risk. SBOM presence alone does not close any of those evaluations.

## Inventory, not judgement

The skill builds the list. Fitness for intended use, anomaly review and integration requirements stay with people. It is an **inventory, not judgement**.

## It's working if

- The export validates as CycloneDX or SPDX.
- Missing data reads `unknown`, never blank.

## Where it fits

Role: chain step. Neighbours: [`configuration-management`](../regulated/configuration-management.md), because it pins each SOUP item as a configuration item; [`maintenance`](../lifecycle/maintenance.md), because it monitors SOUP after release. For the whole map, see [FLOWS.md](../../FLOWS.md).

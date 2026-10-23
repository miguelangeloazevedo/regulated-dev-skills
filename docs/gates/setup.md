<!-- docs page for skills/gates/setup/SKILL.md -->

## What it does

Writes the project block and the few files the other skills need. It asks four questions about tooling and records the answers; it does not decide them. What the product is belongs to `intake`.

Typed commands provide invocation control, not an operating-system permission boundary. An instruction or editable approval field does not establish host-enforced authority.

## When to reach for it

You invoke this by typing `/setup`, and the agent won't reach for it on its own. Set up the project block: backend, evidence level, roles, artefacts.

## Prerequisites

A repository, permission to edit its `AGENTS.md` or `CLAUDE.md`, and an approval under your QMS to use an AI agent on this product.

## Lifecycle handoff

Check that the installed regulated skills carry their local references folders as well as SKILL.md. The technique guides are loaded from the owning skill, not from the project's copied validator folder. State that only standalone is implemented; configuring a Jira or app name does not install an adapter or prove its mappings.

## What it asks, and what it checks

Four questions about tooling: backend, evidence level, roles file, and where artefacts live. What the product is, and which rules apply, belongs to `intake`. Each answer is a claim; where the host can confirm it, `setup` reads the control back and shows any contradiction.

The leading idea is **measured controls**: an evidence level is only as strong as the controls the host actually enforces.

Separate declared controls, observed host controls and agent behavior tests. Record exact scope/configuration/evidence and unassessed or stale properties; do not promote a metadata level into a measured verdict. Read the assurance guide bundled with setup; no private knowledge service is required.

## It's working if

- The block it writes names a level the host's own settings support.
- The validator runs in the project from `tools/rds/`.

## Where it fits

Role: run-once setup. Neighbours: [`intake`](../gates/intake.md), because it classifies the product once the tooling is set; [`status`](../gates/status.md), because it reports what setup declared, measured again. For the whole map, see [FLOWS.md](../../FLOWS.md).

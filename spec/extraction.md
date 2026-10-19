# Extraction: reverse-engineering from code

Applies to `design-inputs-from-code`, `hazards-from-code` and `soup-from-code`.

## What they produce

Candidates, never conclusions. Every item is `proposed`. Rationale, severity, probability, safety class and fitness for use are never filled.

## Stable identity

Each item is anchored to a place in the code, not to a run:

```
anchor: <symbol path or manifest entry>
anchor_hash: <sha256 of the anchored text>
commit: <commit hash scanned>
```

A rerun reconciles instead of renumbering:

| Result | Meaning |
| --- | --- |
| unchanged | Same anchor, same hash |
| changed | Same anchor, different hash. Linked evidence becomes stale. |
| new | Anchor not seen before |
| removed | Anchor gone. The record is flagged, not deleted. |

## Triangulation

Read, in order of how well each shows intent: tests, API schemas, configuration and feature flags, database schema, user-facing strings, code, then commit and pull request history and tickets. An item lists which sources agree. Disagreement between sources is itself a finding.

## Coverage disclosure

Every output states what was scanned, what was excluded, and what the method cannot see. A scan with no coverage section is rejected by the validator.

## Questions for the owner

The skill produces a ranked list of questions for the human fields, most safety-relevant first, and writes it into the change's `decision.md` for the owner. It does not fill the answers.

## SBOM

`soup-from-code` builds an inventory from lockfiles and manifests covering libraries, runtimes, operating system packages, container images, CI actions, build tools and any models. It exports CycloneDX or SPDX on request. Advisory lookups, when allowed, are recorded with their source and date. A human reviews known anomalies.

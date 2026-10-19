<!-- docs page for skills/regulated/security-diligence/SKILL.md -->

## What it does

Security work built into the development process: a threat model that follows the architecture, analysis of dependencies and code, a decision on every open finding, and a correction loop back to build.

## When to reach for it

Type `/security-diligence`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| The architecture changes. | `security-diligence` |
| Findings arrive from a scan, a review or a report. | `security-diligence` |
| A release is being prepared. | `security-diligence` |
| A one-off question about a library, outside any change | not a skill: answer it directly; no skill is needed. |

## Prerequisites

An owned-asset list, before any active scan.

## Owned assets only

Threats come from the architecture: embedded, mobile, cloud and the clinical functions each have their own. Dependency and static analysis run by default. Active scanning runs only against a list of **owned assets only**, after a typed approval. Every finding gets a decision from a person.

## It's working if

- Every finding has a decision and an owner.
- Every active scan traces to an approval.

## Where it fits

Role: runs inside the chain. Neighbours: [`soup-from-code`](../extraction/soup-from-code.md), because its inventory feeds dependency analysis; [`risk`](../regulated/risk.md), because findings that can cause harm become hazards. For the whole map, see [FLOWS.md](../../FLOWS.md).

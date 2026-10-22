<!-- docs page for skills/regulated/configuration-management/SKILL.md -->

## What it does

Keeps the software and everything that builds it identified, changed only through approved change requests, and recoverable as baselines. It runs alongside every step of the chain.

## When to reach for it

Type `/configuration-management`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| A new component, SOUP item, tool or document enters the product. | `configuration-management` |
| A change request is raised or implemented. | `configuration-management` |
| A baseline is needed for verification, review or release. | `configuration-management` |
| Pricing a change | [`impact`](../gates/impact.md) |

## Prerequisites

A development plan with a configuration management section.

## Techniques and timing

Select methods for the approved plan and lifecycle stage; the guides distinguish evidence and human decisions:

- [Technique selection and procedure](../../skills/regulated/configuration-management/references/baseline-and-change-control.md).
- [Fictional worked example](../../skills/regulated/configuration-management/references/worked-example.md).

## Nothing changes without a request

Every configuration item, SOUP and tools included, has a version. **Nothing changes without a request**, and every baseline is a named set of hashes that can be rebuilt.

## It's working if

- Every commit on the release branch traces to a change request.
- A baseline can be rebuilt on a clean machine.

## Where it fits

Role: runs inside the chain. Neighbours: [`impact`](../gates/impact.md), because it prices each change request; [`release`](../gates/release.md), because it releases a baseline this skill formed; [`development-plan`](../lifecycle/development-plan.md), because the approved plan defines change and baseline controls. For the whole map, see [FLOWS.md](../../FLOWS.md).

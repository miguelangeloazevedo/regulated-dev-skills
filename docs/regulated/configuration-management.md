<!-- docs page for skills/regulated/configuration-management/SKILL.md -->

## What it does

Keeps the software and everything that builds it identified, changed only under its applicable approved authorisation, and recoverable as baselines. It runs alongside every step of the chain.

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
- [Document lifecycle and completed-record controls](../../skills/regulated/configuration-management/references/document-and-record-control.md).

## Lifecycle handoff

Control document identity/revision, approval versus effective issue, point-of-use versions and review/obsolescence separately from completed-record amendments, protection, retrieval and retention. Read the local guide; host/QMS enforcement is not supplied by the validator.

## Nothing changes without authorisation

Every configuration item, SOUP and tools included, has a version. Each change needs its applicable approved authorisation: a narrowly approved plan class before first release where permitted, otherwise an approved CR, and an approved CR after release. Every baseline identifies the items and evidence needed for rebuild and recovery.

## It's working if

- Every baseline change traces to its applicable approved authorisation and verification.
- A relied-on baseline has a recorded clean rebuild/recovery check with limits.

## Where it fits

Role: runs inside the chain. Neighbours: [`impact`](../gates/impact.md), because it prices each change request; [`release`](../gates/release.md), because it releases a baseline this skill formed; [`development-plan`](../lifecycle/development-plan.md), because the approved plan defines change and baseline controls. For the whole map, see [FLOWS.md](../../FLOWS.md).

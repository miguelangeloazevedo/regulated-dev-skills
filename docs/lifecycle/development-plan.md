<!-- docs page for skills/lifecycle/development-plan/SKILL.md -->

## What it does

Writes the software development plan the rest of the chain runs on: stages, reviews, verification and validation activities, responsibilities, the risk management plan, and the configuration management plan. For device software the safety class sets the minimum; otherwise the plan chooses the depth and says why.

## When to reach for it

Type `/development-plan`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| `/intake` has run and no plan exists. | `development-plan` |
| The scope, class, team or tooling changes enough that the plan no longer describes the work. | `development-plan` |
| `/intake` has not been run | [`intake`](../gates/intake.md) |

## Prerequisites

An approved `CLS` record from `intake`.

## The plan the chain runs on

Every later skill reads the plan: review stages, verification levels, independence, validation, risk management, configuration management. The plan is **the plan the chain runs on**, and its depth follows the safety class.

## It's working if

- Every later activity can point at the line in the plan that called for it.
- The plan names people, not only roles in general.

## Where it fits

Role: chain step. Neighbours: [`intake`](../gates/intake.md), because the class it plans for comes from there; [`configuration-management`](../regulated/configuration-management.md), because it carries out the configuration management plan; [`design-review`](../lifecycle/design-review.md), because it holds the reviews the plan schedules. For the whole map, see [FLOWS.md](../../FLOWS.md).

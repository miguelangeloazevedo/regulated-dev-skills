<!-- docs page for skills/lifecycle/specifications/SKILL.md -->

## What it does

Says how each software requirement is built, at the depth the safety class asks for: architecture and software items for class B and C, detailed design per unit for class C. Every specification states what it refuses, and splits into units small enough to build and verify one at a time.

## When to reach for it

Type `/specifications`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| Software requirements are approved and the design is not written. | `specifications` |
| A specification changes or a unit has to be split. | `specifications` |
| The behaviour itself is not settled | [`requirements`](../lifecycle/requirements.md) |

## Prerequisites

Approved software requirements.

## Lifecycle handoff

Before design approval, refine risk analysis/FMEA or selected fault trees and security threat models with the actual architecture, interfaces and SOUP assumptions. Reconcile control mechanisms with the user interface specification and formative findings from `usability`; send changed assumptions back to requirements and risk.

## Depth follows the class

How much design a specification carries depends on the software safety class.

| Class | What `specifications` writes |
| --- | --- |
| A | Specifications that tie each part of the code to its requirements |
| B | Adds the architecture: software items, interfaces, SOUP requirements, units |
| C | Adds segregation for risk controls and detailed design per unit |

At every class, each specification states **what it refuses**, because an omission and a decision look the same until someone writes it down.

## It's working if

- A reviewer can tell from the specification what it deliberately does not do.
- Units can be built in parallel without stepping on each other.

## Where it fits

Role: chain step. Neighbours: [`requirements`](../lifecycle/requirements.md), because each specification specifies software requirements; [`implement`](../lifecycle/implement.md), because it builds the units one at a time. For the whole map, see [FLOWS.md](../../FLOWS.md).

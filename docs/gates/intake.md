<!-- docs page for skills/gates/intake/SKILL.md -->

## What it does

Works out what the software is before any work starts: a medical device or not, a part of someone else's device or not, and if it is a device, its risk class, its software safety class and the rules that apply. It drafts every answer with its rule path; a person decides each one. It never assumes a class.

## When to reach for it

You invoke this by typing `/intake`, and the agent won't reach for it on its own. Classify the product: device status, risk class, software safety class, applicable rules.

## Prerequisites

A project block from `setup`.

## Lifecycle handoff

Hand provisional risk/class assumptions and reclassification triggers to `risk`, early use specification to `usability`, and cyber-device/connectivity assumptions to `security-diligence`. A technique score, FMEA RPN or security score does not decide the regulatory or software class.

## What is it?

Before any class there is a plainer question: **what is it?** Each module is a device, not a device, part of someone else's device, or not decided yet. Only device software gets a risk class and a software safety class, and only a person decides them. Nothing is filled in by default.

## Common questions

**Can the agent tell me my class?**

It drafts a class with the rules it applied and the rules it ruled out. In the EU the manufacturer applies the rules and records them with `/approve`; in the US the class comes from FDA's regulations and decisions, so intake proposes candidates.

## It's working if

- Every module has one of the four outcomes, with the steps shown.
- Every software system is A, B, C, `none`, or visibly not decided.
- A claim change on the website sends the change back to `/intake`.

## Where it fits

Role: run-once setup. Neighbours: [`setup`](../gates/setup.md), because it sets the tooling intake writes into; [`risk`](../regulated/risk.md), because the safety class rests on the hazard analysis, and external controls can change it; [`impact`](../gates/impact.md), because it checks every change against the reclassification triggers. For the whole map, see [FLOWS.md](../../FLOWS.md).

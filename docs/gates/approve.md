<!-- docs page for skills/gates/approve/SKILL.md -->

## What it does

Binds a person's approval to the exact content they saw. An agent may draft an approval; only the person typing the command records it.

Typed commands provide invocation control, not an operating-system permission boundary. An instruction or editable approval field does not establish host-enforced authority.

## When to reach for it

You invoke this by typing `/approve`, and the agent won't reach for it on its own. Record a human approval against the exact revision of a record.

## Prerequisites

A roles file, and records under the artefacts directory.

## Lifecycle handoff

Before the human decision, expose the source evidence and limits behind linked claims: an FMEA row is not risk acceptance, a linked case is not executed verification, and an implementation check alone may not establish effectiveness. Do not resolve those gaps by replacing hashes or approval fields. Confirm authority and revision binding per record/gate and reconcile decision history with actual workflow state; an approval feature is not a universal signature guarantee. Distinguish document approval from effective issue and actual point-of-use availability.

## What an approval binds

An approval records who, in which role, on what date, against which **revision hash**, with a reference to the host's own approval. Edit one word and the hash changes, so the approval goes stale on its own and visibly.

| Mode of failure | What `approve` does |
| --- | --- |
| Approver is the author | Refuses and names the role that may approve |
| A content or scope `BLOCKED` remains | Refuses |
| Level needs a signature and none exists | Records the gap and what the level then proves |

For a host-enforced approval claim, require a current authorised host decision bound to the exact content. Use the supported trusted preflight where applicable; never accept agent-authored facts or local human-admin credentials as an isolation boundary. If unavailable, hold that authorisation claim. Read the assurance guide bundled with setup; no private knowledge service is required.

## Common questions

**Why can't the agent approve on my behalf?**

Because an approval is a person's decision bound to content they saw. The agent drafts it and tells you to type `/approve`; recording it for you would make the record false.

## It's working if

- Every approved record shows a hash that matches its current content, or the validator lists it as stale.
- Approvals reference a pull request, transition or signature you can open.

## Where it fits

Role: gate. Neighbours: [`release`](../gates/release.md), because it refuses a baseline whose approvals are stale or missing; [`traceability`](../regulated/traceability.md), because it lists the dependants an approval makes stale. For the whole map, see [FLOWS.md](../../FLOWS.md).

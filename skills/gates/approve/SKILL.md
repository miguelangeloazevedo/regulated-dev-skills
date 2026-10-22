---
name: approve
description: "Record a human approval against the exact revision of a record."
disable-model-invocation: true
argument-hint: "<record-id ...>"
metadata:
  group: gates
  invocation: typed
  role: "gate"
  leading_word: "revision hash"
  neighbours: [release, traceability]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["ISO 13485:2016 7.3.5"]
---

# Approve

Binds a person's approval to the exact content they saw. An agent may draft an approval; only the person typing the command records it.

Run this only when a person types `/approve`. If you reached this skill on your own, stop and ask the user to type the command.

## Reads

The target records, the roles file, the project block.

## Process

1. If the record was approved before, show the diff between the last approved revision and the current one, not only the full text. *Done when:* The approver has seen what changed.
2. Show the user the exact content and the revision hash of each record. *Done when:* The user has seen content and hash.
3. Check the role is allowed for the record type and the approver is not the author. *Done when:* Both checks pass, or the refusal is stated.
4. Name any `BLOCKED` criterion of type content or scope. Do not approve past one. *Done when:* None remain, or the approval stops.
5. Before the human decision, expose the source evidence and limits behind linked claims: an FMEA row is not risk acceptance, a linked case is not executed verification, and an implementation check alone may not establish effectiveness. Do not resolve those gaps by replacing hashes or approval fields. *Done when:* The approver sees relevant evidence gaps and dependencies, not just the record hash.
6. Ask for the host reference: pull request, transition, signed tag or record-system signature. If the evidence level needs a signature and none exists, say what the level then proves. Read it back from the host after writing: on GitHub, for example, `gh pr view <number> --json reviews,mergedAt,headRefOid`; on another host, its API or command line. *Done when:* A reference is recorded, or the gap is stated.
7. Write the approval block and set the status. Run the validator and list records derived from this one whose approvals are now stale. *Done when:* The validator passes and stale dependants are listed.
8. For a `CLS` record, refuse if any source's re-check date has passed; ask for the sources to be checked again first. The record carries the earliest re-check date as `recheck_by` in its frontmatter, and the validator checks it. *Done when:* No `CLS` approval rests on a source past its re-check date.
9. On an agent that does not enforce typed commands, do not rely on this skill alone to stop self-approval: use evidence level 1 or above, so a required independent reviewer on the host must approve the change that carries the approval. *Done when:* The project's evidence level is at least 1 when the agent cannot enforce typed commands, or the risk is recorded.
10. When the approved record is a `CLS` record, write `jurisdictions`, `standards` and `safety_class` from it into the project block, in the same change as the approval, and echo them. *Done when:* The project block matches the approved `CLS` record.
11. At evidence level 1 and above, after writing, read the approval back from the host by its reference and confirm approver, date and revision match. At level 0 there is no host record: say so instead of claiming a read-back. *Done when:* The read-back matches, or the level is 0 and that is stated, or the mismatch is reported and the status is not changed.

## Lessons from practice

- Approval is of a change, not of a document. Show the delta.
- Any action that cannot be undone shows what it will touch, names the target, and waits for a confirmation that repeats the count.
- A status asserted from what was intended is not a status. Read it back from the system that holds it.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Rubber stamp | Approvals land minutes apart on records nobody opened. |
| Adopted done | A host status meaning finished is reused as approved, so every board counts approved work as closed. |

## Refuses

- Recording an approval for someone else. *Instead:* Draft it and tell them to run `/approve`.
- Approving content the user has not seen. *Instead:* Show it first.
- Approving your own authored record. *Instead:* Name the role that may approve it.
- Approving a set of records in one step without listing each id, title and hash. *Instead:* List every record with its hash and ask for one confirmation that names the count.

## Writes

The `approval` block and `status` on each record.

## Done when

- Each approval names its approver, role, date, revision and reference.
- The validator reports no hash mismatch for the approved records.

## See also

- `release`, because it refuses a baseline whose approvals are stale or missing. It is typed-only: tell the user to run `/release`.
- `traceability`, because it lists the dependants an approval makes stale. Load the `traceability` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

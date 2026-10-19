---
name: design-review
description: "Use when preparing or recording a design review. At planned stages."
metadata:
  group: lifecycle
  invocation: model
  role: "chain step"
  leading_word: "read-list"
  neighbours: [approve, traceability]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["ISO 13485:2016 7.3.5", "ISO 13485:2016 7.3.2"]
---

# Design review

Prepares and records a design review at a stage the plan names: what was read, by whom, what was found, and whether the design can meet its requirements. The agent prepares the pack and the record; the people in the room decide.

## When to use

- A planned review stage is reached.
- A baseline is about to be approved.

Not for:

- Reviewing one unit's code: that is part of `unit-verification`.

## Reads

The development plan's review stages, the records in scope, verification results, open findings, the risk file.

## Process

1. Name the stage, the design under review (baseline or record set with hashes) and its inputs. *Done when:* The design under review is identified by hash.
2. Build the pack: every record in scope, verification results on that revision, open findings, risk status, and anything stale or `BLOCKED`. *Done when:* The pack lists every item with its hash.
3. Check the participants: representatives of each function concerned with the stage (typically quality and regulatory, software and security engineering, usability, clinical or product safety), and at least one person independent of the design. *Done when:* Each function is present or its absence is recorded.
4. Compare user-facing behaviour against the live system or an approved reference, never against a mock the same effort wrote. *Done when:* The reference is named and is not self-authored.
5. Draft the `REV` record: the design under review, a read-list per participant, left blank for each participant to fill with what they actually read (the agent cannot know it), findings with owners and dates, and an explicit statement on whether the design can meet its requirements. *Done when:* A `REV` record exists with its four sections.
6. Sign-off of the record is by the participants. The agent never appears as a participant or as the independent reviewer. *Done when:* The record names only people.

## AI/ML branch

Add a data scientist or equivalent to the participants, and review the training and evaluation data description alongside the design.

## Lessons from practice

- Record what was actually read. A list of everything in scope is a claim, not a record.
- A self-authored mock is a hypothesis, not ground truth.
- Name the functions a stage needs and record any that were absent.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Review by signature | A review record with participants and no findings, no read-list and no statement. |
| Self-reference | The design is reviewed against its own mock. |

## Refuses

- Recording a review nobody held. *Instead:* Prepare the pack and the draft; the record is completed by the participants.
- A read-list of everything in scope rather than what was read. *Instead:* List only what each participant actually read.
- Treating the agent as a participant or as the independent reviewer. *Instead:* Name people.

## Writes

A `REV` record (sections: Design under review, Read-list, Findings, Statement), with findings as `FIND` records. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- The record identifies the design by hash, the participants, the date and the read-list.
- Every finding has an owner.
- The statement on meeting requirements is explicit.

## See also

- `approve`, because approval of a baseline follows its review. It is typed-only: tell the user to run `/approve`.
- `traceability`, because the pack is built from the link graph. Load the `traceability` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

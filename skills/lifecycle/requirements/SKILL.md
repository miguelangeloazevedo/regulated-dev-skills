---
name: requirements
description: "Use when deriving system or software requirements. Includes risk controls."
metadata:
  group: lifecycle
  invocation: model
  role: "chain step"
  leading_word: "one field, one question"
  neighbours: [user-needs, specifications, risk]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 5.2", "ISO 13485:2016 7.3.3", "ISO 14971:2019 7.1"]
---

# Requirements

Derives system requirements from user needs and software requirements from system requirements, with risk controls folded in. Every requirement can fail a test, traces to at least one parent, and leaves undecided things blocked rather than softened.

## When to use

- User needs exist and the system behaviour is not specified.
- A risk control has to become a requirement.
- A requirement changes.

Not for:

- The needs themselves are unclear: use `user-needs`.
- Describing how it is built: use `specifications`.

## Reads

`UN` records, `RC` records, the approved `CLS` record (safety class), existing `SYS` and `SW` records.

## Process

1. Derive system requirements: what the system shall do, verifiable at the system boundary, each from one or more needs. *Done when:* Every `SYS` derives from at least one `UN`.
2. Derive software requirements: what the software shall do, each from one or more system requirements. Many-to-many derivation is allowed; `traceability` reports it so a reviewer can see where one requirement serves several parents. *Done when:* Every `SW` derives from at least one `SYS`.
3. Check the content categories IEC 62304 5.2.2 asks for against the set (functional, inputs and outputs, interfaces, alarms, security, usability, data, installation, operation and maintenance, network, regulatory) and mark each covered or not applicable. *Done when:* Each category is covered or marked not applicable with a reason.
4. For class B and C, write each software risk control as a requirement and link it to its `RC` (5.2.3). At every class, once the software requirements exist, ask `risk` to re-evaluate the risk analysis against them and update it where needed (5.2.4). *Done when:* Every software `RC` is implemented by a requirement, and the re-evaluation is recorded.
5. Plan verification methods while drafting acceptance criteria: partitions and boundaries for ranges, decision/state cases for conditional behaviour, and interface/negative cases where relevant. Distinguish risk-control implementation criteria from effectiveness claims; ask `usability` and `risk` what user-facing evidence is needed. Preserve the class-dependent minimum and the approved plan's additions. *Done when:* Requirements name observable criteria and planned evidence, including both control claims where applicable.
6. Write one field per question: statement, rationale, acceptance criteria. Rationale is not a paraphrase of the statement. *Done when:* No two fields say the same thing.
7. For each requirement, write the scenario that would fail. If you cannot, mark it `BLOCKED(content)`, `BLOCKED(scope)` or `BLOCKED(timing)` and name what unblocks it. *Done when:* Every requirement has a failing scenario or a typed block.
8. Verify the set (5.2.6): every requirement implements its parent, is uniquely identified, unambiguous, testable, and contradicts no other. *Done when:* The verification is recorded with any findings.

## AI/ML branch

Add requirements for the model's performance with thresholds per subgroup, for training and evaluation data provenance, for input ranges outside which it must not answer, and for the change control approach: which updates sit inside a predetermined change control plan and which need a new submission.

## Lessons from practice

- The test for every requirement: can you write the scenario that would fail?
- For every displayed or stored value, say what shows when it is absent. It is never the favourable value.
- Type every block: content and scope do not advance; timing does.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Paraphrase fields | Rationale and acceptance criteria repeat the statement in other words. |
| Parent invented to close a gap | A system requirement appears right after a traceability run, with one child. |

## Refuses

- A criterion an empty implementation would pass. *Instead:* Write `BLOCKED` with its kind and what would unblock it.
- Deciding an open scope question. *Instead:* Write `BLOCKED(scope)` and ask the owner.

## Writes

`SYS` and `SW` records, and their links up and to `RC`. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every `SYS` derives from a `UN`, every `SW` from at least one `SYS`.
- Every requirement has a scenario that would fail, or a typed block.
- Every software risk control is a requirement.

## See also

- `user-needs`, because every system requirement derives from one. Load the `user-needs` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `specifications`, because it says how each software requirement is built. Load the `specifications` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `risk`, because its controls become requirements here. Load the `risk` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

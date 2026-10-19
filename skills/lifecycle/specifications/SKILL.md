---
name: specifications
description: "Use when designing how requirements are built. Architecture, units, interfaces, by safety class."
metadata:
  group: lifecycle
  invocation: model
  role: "chain step"
  leading_word: "what it refuses"
  neighbours: [requirements, implement]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["IEC 62304:2006+A1:2015 5.3", "IEC 62304:2006+A1:2015 5.4", "ISO 13485:2016 7.3.4"]
---

# Specifications

Says how each software requirement is built, at the depth the safety class asks for: architecture and software items for class B and C, detailed design per unit for class C. Every specification states what it refuses, and splits into units small enough to build and verify one at a time.

## When to use

- Software requirements are approved and the design is not written.
- A specification changes or a unit has to be split.

Not for:

- The behaviour itself is not settled: use `requirements`.

## Reads

`SW` records, `RC` records, `SOUP` records, the safety class from the project block, existing `SPEC` records and the code.

## Process

1. Read the safety class from the project block. A, B or C: apply what CLASS-OBLIGATIONS.md lists for it. `none` (not device software, or its class is set by another product): apply the depth the `PLAN` record chose. Not decided: ask the user to decide it through `/intake`, or to choose a depth for now and record it in the `PLAN`; never assume one. While the project claims IEC 62304 for device software, a lower depth cannot be chosen for a class that is not decided: stop and ask for the class to be decided. Read the depth only from an approved `PLAN`; a draft plan sets nothing. *Done when:* The depth applied is named, with its source: the class, the plan, or the user's recorded choice.
2. For class B and C, describe the architecture: software items, their interfaces with each other and with external components, and the functional and performance requirements on each SOUP item (5.3.1 to 5.3.4). For class C, describe the segregation any risk control relies on (5.3.5). *Done when:* Every software item and interface is specified, and every SOUP item has its requirements.
3. Write each `SPEC`: the module, the mechanism, the requirements it specifies, and what it refuses and why. *Done when:* Every `SPEC` specifies at least one `SW` and has a refusal section.
4. Split into software units (5.4.1). For class C, write the detailed design and interfaces of each unit (5.4.2, 5.4.3). *Done when:* Every unit is named; class C units have detailed design.
5. Order the units as work: each unit declares what blocks it, lists every field or setting its result must carry, and names any one-way door it touches (a permanent name, a stored value, a migration) with the decision it needs. *Done when:* The blocking graph has no cycle and every one-way door links a decision.
6. Verify the design: it implements the requirements, the interfaces are consistent, and it supports the risk controls (5.3.6, and 5.4.4 for class C). *Done when:* The verification is recorded.

## AI/ML branch

Specify the model as a software item: its inputs and their valid ranges, its outputs, the version pinned, the data it was trained and evaluated on, and the behaviour when an input is out of range.

## Lessons from practice

- Every specification says what it refuses and why.
- A writer that sets a subset of the fields produces a uniform hole. Name every field the result must carry.
- You complete a migration; you do not work around it.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Copy of the requirement | The specification restates the requirement and says nothing about how. |
| Layer cake | Units are all database first, then all interface. |

## Refuses

- A specification with no requirement above it. *Instead:* Record it as a finding; never invent a parent.
- Units sliced by layer (all database, then all interface). *Instead:* Slice so each unit can be built and verified on its own.
- Starting a unit that renames something permanent without a decision. *Instead:* Link the decision first.

## Writes

`SPEC` records, the architecture description for class B and C, unit breakdown and order. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every `SW` is specified by at least one `SPEC`.
- Every `SPEC` states what it refuses.
- The design depth matches the safety class.

## See also

- `requirements`, because each specification specifies software requirements. Load the `requirements` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `implement`, because it builds the units one at a time. Load the `implement` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

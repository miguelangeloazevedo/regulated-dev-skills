---
name: development-plan
description: "Use when planning software development for a product. Before needs and requirements."
metadata:
  group: lifecycle
  invocation: model
  role: "chain step"
  leading_word: "the plan the chain runs on"
  neighbours: [intake, configuration-management, design-review]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["IEC 62304:2006+A1:2015 5.1", "ISO 13485:2016 7.3.2", "ISO 14971:2019 4.4", "ISO 13485:2016 4.1.6", "ISO 13485:2016 7.3.8", "ISO 13485:2016 7.4"]
---

# Development plan

Writes the software development plan the rest of the chain runs on: stages, reviews, verification and validation activities, responsibilities, the risk management plan, and the configuration management plan. For device software the safety class sets the minimum; otherwise the plan chooses the depth and says why.

## When to use

- `/intake` has run and no plan exists.
- The scope, class, team or tooling changes enough that the plan no longer describes the work.

Not for:

- `/intake` has not been run: tell the user to run it.

## Reads

The approved `CLS` record, the project block, the roles file, any existing `PLAN` record.

## Process

1. Read the outcome and the safety class from the `CLS` record. For device software with a class, list the plan elements that class requires using `intake`'s CLASS-OBLIGATIONS.md, which is an interpretation: check each line against your own copy of the pinned edition and record who checked it and when. For `none`, or while the class is not decided, choose with the user which activities the plan includes and record the reason for each one left out. While the project claims IEC 62304 for device software, a lower depth cannot be chosen for a class that is not decided: stop and ask for the class to be decided. For non-device software or a component whose class another manufacturer sets, the reduced depth is accepted by QA/RA by name, and checked against what the customer or integrator will audit (supplier agreement, their SOUP or purchasing requirements). *Done when:* The plan's depth is listed with its source: the class, or the recorded choice.
2. For software with class `none`, write the chosen depth per activity (requirements, design, verification, configuration and problem resolution) with the reason tied to what the software can affect, and the criterion QA/RA used to accept it. A depth without a reason is not accepted. *Done when:* Each activity has a depth, a reason and the acceptance criterion.
3. Confirm the use of an AI agent on this product is approved under your QMS: the tool, the model and its version, where code and records are processed, and how agent output is reviewed. Ask the QA/RA owner whether the agent counts as software used in the QMS that must be validated for its intended use (ISO 13485 4.1.6) or as a development tool controlled another way; the agent never makes that decision. Record the answer, who gave it, and the validation reference: intended use, pinned tool and model versions, how output is reviewed, what triggers revalidation. A validation still in progress is recorded as open; work may start, and `release` stops until it is complete. Record the approval reference for agent use, or stop. Use `setup`'s AGENT-VALIDATION-TEMPLATE.md for the validation reference. *Done when:* An approval reference for agent use is recorded, or this skill stops and records the gap as a `FIND` record so the next session sees why.
4. Write the stages of the work, the design reviews at each stage and who takes part, and the design transfer and release activities (13485 7.3.2; 62304 5.1.1). *Done when:* Every stage has an entry and exit criterion and a named review.
5. Plan verification and validation: what will be verified at each level, by which method, by whom, and how independence is achieved; how and with whom the user needs will be validated (5.1.6; 13485 7.3.2). *Done when:* Every level of the chain has a verification activity, and validation names users and environment.
6. Write or reference the risk management plan: scope, responsibilities, acceptability criteria, method for overall residual risk, verification of controls, and collection of production and post-production information (ISO 14971 4.4). *Done when:* Each element of ISO 14971 4.4 is present or referenced.
7. Write the configuration management plan: configuration items including SOUP and tools, how they are identified, the change control route, and baselines (5.1.9; for class B and C, 5.1.10 and 5.1.11). *Done when:* Configuration items, change control and baselines are defined.
8. List the suppliers whose product or service affects the device (SOUP vendors with support, cloud hosts, model providers, test labs) for your purchasing controls (ISO 13485 7.4), and plan design transfer to production or deployment (7.3.8). *Done when:* Suppliers and the transfer plan are listed.
9. For class B and C add integration planning (5.1.5) and the plan for identifying and avoiding common software defects (5.1.12); for class C add the standards, methods and tools to be used (5.1.4). *Done when:* Class-dependent elements are present.
10. Plan the documents (62304 5.1.8): for each, its title or naming convention, purpose, and who prepares, reviews and approves it. Plan how problems are handled during development (`problem-resolution`) and when the software moves to maintenance. Write the QMS boundary list as the plan's `## QMS boundary` section: document control, management review, CAPA, complaint handling, purchasing, the design history file and the technical documentation, each with the owner and the location in your QMS. *Done when:* The document plan, the hand-overs and the QMS boundary list exist, each item with an owner.
11. Write the `PLAN` record and tell the user to run `/approve`. The plan sets nothing until it is approved; until then every skill that needs its depth asks. Keep it updated as the work changes (5.1.2). *Done when:* The plan is `draft` and waiting for approval.

## AI/ML branch

Plan data management: where training, tuning and test data come from, how they are kept apart, and how a model change is controlled. If a predetermined change control plan is used, say which changes it covers.

## Lessons from practice

- Derive the plan's contents from the safety class, not from a template.
- Say up front who verifies what and how they are independent of the build.
- A plan is current, not a snapshot. Update it when the work changes, and record the change.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Template plan | Section headings filled with generic text that names no product, class or person. |
| Frozen plan | The plan's date predates the last architecture change. |

## Refuses

- A plan that names no responsible person for an activity. *Instead:* Name a role from the roles file, or record the gap.
- Copying a plan template without fitting it to the class and the product. *Instead:* Derive each element from the class and the `CLS` record.

## Writes

A `PLAN` record. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every element the class requires is in the plan or referenced.
- Verification independence and the validation approach are stated.
- The configuration management plan defines items, change control and baselines.

## See also

- `intake`, because the class it plans for comes from there. It is typed-only: tell the user to run `/intake`.
- `configuration-management`, because it carries out the configuration management plan. Load the `configuration-management` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `design-review`, because it holds the reviews the plan schedules. Load the `design-review` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

---
name: unit-verification
description: "Use when building or verifying software units. Test-first, against acceptance criteria."
metadata:
  group: lifecycle
  invocation: model
  role: "chain step"
  leading_word: "red first"
  neighbours: [implement, verify]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 5.5.2", "IEC 62304:2006+A1:2015 5.5.3", "IEC 62304:2006+A1:2015 5.5.4", "IEC 62304:2006+A1:2015 5.5.5"]
---

# Unit verification

Verifies each software unit against acceptance criteria derived from its specification, test-first, by the methods the class asks for. A test that has never failed has not been shown to detect anything.

## When to use

- A unit is being built or changed.
- A unit's acceptance criteria need writing.

Not for:

- Integration or system testing: use `verify`.

## Reads

The unit's `SPEC`, its requirements, the safety class, the project's coding standards.

## Process

1. Read the safety class from the project block. A, B or C: apply what CLASS-OBLIGATIONS.md lists for it. `none` (not device software, or its class is set by another product): apply the depth the `PLAN` record chose. Not decided: ask the user to decide it through `/intake`, or to choose a depth for now and record it in the `PLAN`; never assume one. While the project claims IEC 62304 for device software, a lower depth cannot be chosen for a class that is not decided: stop and ask for the class to be decided. Read the depth only from an approved `PLAN`; a draft plan sets nothing. *Done when:* The depth applied is named.
2. Write the unit's acceptance criteria from its specification (5.5.3). At class C add, where the design has the feature: correct sequencing of events, data and control flow, planned resource allocation, fault handling (definition, isolation, recovery), initialisation of variables, self-diagnostics, memory management and overflow, and boundary conditions (5.5.4). State the method: test, inspection or analysis. Criteria on memory management, overflow, resource allocation and initialisation are verified with static analysis and, where the language allows, dynamic analysis in the build (for example AddressSanitizer or Valgrind for C and C++), not with unit tests alone. *Done when:* Each unit has criteria, with the 5.5.4 topics addressed or marked not applicable with the reason at class C. Each memory or resource criterion names the analysis tool and its run.
3. Select unit-level partitions, boundary, decision and state cases from the approved criteria; use independent expected values and appropriate static/dynamic analysis. `verify` owns the subsequent integration/system campaign, not this builder-run check. An implementation assertion does not automatically prove the control's risk reduction. *Done when:* The selected unit techniques, oracle and handoff are recorded.
4. Agree the seams: the public boundaries the tests will observe the unit through. No test goes at an unagreed seam. *Done when:* The seams are written down.
5. Write tests at those seams, test-first where practical: write one test, watch it fail for the right reason, then only the code that makes it pass. Test-first is recommended practice here, not a requirement of the standard. *Done when:* Each behaviour in the criteria has a test.
6. For each test that verifies a risk control, break the control once and confirm the test goes red. Keep the red run and reference it from the unit's `TR`. *Done when:* Every risk-control test has a recorded red run.
7. Review the code on two axes kept apart: Standards (does it follow the project's coding standards) and Specification (does it do what the `SPEC` says). *Done when:* Both axes are reported separately.
8. Tests run in the same context that wrote the unit are builder-run. At class B and C, have a fresh context or a person re-run them against the revision before the unit verification counts, and record which. *Done when:* Each unit verification at class B and C names who or what re-ran it.
9. Record the unit verification (5.5.5): the criteria, the method, the result, the revision. *Done when:* A `TR` exists for each unit verified.

## AI/ML branch

Verify the model's wrapper as a unit: out-of-range inputs are refused, the pinned version is the one loaded, and the output schema holds.

## Lessons from practice

- Break the targeted line, confirm the test goes red, restore it. A test that has only ever passed has not been tested.
- Print the count the harness saw. Zero failures and zero tests look the same.
- Review what shows when a value is absent, and that tests sit only at agreed seams.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Implementation-coupled | The suite breaks when you rename an internal function but behaviour is unchanged. |
| Tautological | The expected value is computed the way the code computes it. |
| Batch first | A batch of tests lands before any code. |

## Refuses

- An expected value computed the way the code computes it. *Instead:* Take it from a literal, a worked example or the specification.
- Mocking your own modules. *Instead:* Mock only system boundaries: external services, time, randomness.
- Test values that can never trigger the defect, such as a sentinel no real value contains. *Instead:* Build the case from real values that would collide.

## Writes

Tests, unit `TR` records, review findings. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every unit's criteria trace to its specification.
- Tests written test-first where the plan asks for it; elsewhere the reason is recorded.
- Every test that verifies a risk control has a recorded red run.

## See also

- `implement`, because it builds test-first through this skill. Load the `implement` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `verify`, because integration and system testing come next, by someone else. Load the `verify` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

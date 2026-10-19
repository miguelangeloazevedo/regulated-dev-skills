---
name: verify
description: "Use when verifying a revision against its requirements."
metadata:
  group: regulated
  invocation: model
  role: "chain step"
  leading_word: "exact revision"
  neighbours: [unit-verification, release]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["IEC 62304:2006+A1:2015 5.6", "IEC 62304:2006+A1:2015 5.7", "ISO 13485:2016 7.3.6"]
---

# Verify

Runs integration and system testing on the exact revision and keeps verification apart from validation. Models may do the work; under this repository's rule, at class B and C a named human independent of the build signs each result, and an unsigned result is recorded as a pre-check.

## When to use

- A revision is ready for verification.
- Evidence has become stale after a change.

Not for:

- Checking a unit during build: that is `unit-verification`.

## Reads

The revision, the records, the test cases, the project's declared verifier kind.

## Process

1. Read the safety class from the project block. A, B or C: apply what CLASS-OBLIGATIONS.md lists for it. `none` (not device software, or its class is set by another product): apply the depth the `PLAN` record chose. Not decided: ask the user to decide it through `/intake`, or to choose a depth for now and record it in the `PLAN`; never assume one. While the project claims IEC 62304 for device software, a lower depth cannot be chosen for a class that is not decided: stop and ask for the class to be decided. Read the depth only from an approved `PLAN`; a draft plan sets nothing. *Done when:* The depth applied is named.
2. Pin the revision under test. Run verification in a separate session or agent that has not seen the builder's conversation or notes, starting from the revision and the records. If your harness cannot start one, record that the verifier shared the build context. *Done when:* The revision is pinned and the verifier's separation is recorded.
3. At class B and C, run integration testing first: integrate the units per the integration plan and test the interfaces and the risk controls between items, with regression testing after each change (62304 5.6). *Done when:* Integration results exist for each integration step, or class A is recorded.
4. Run system testing against every software requirement, by test, inspection or analysis (5.7). Do not edit code or records while testing. *Done when:* Every software requirement has a system test result or a recorded reason.
5. Write one `TR` per test case naming the revision and the verifier kind. *Done when:* Each `TR` names its revision and verifier kind.
6. Usually one signed verification report (`VRP`) covers the results of an integration or system test campaign; a signature on each result is the alternative. At class B and C (or wherever the `PLAN` asks for it), have a named human who did not build the revision review and sign each result, or a signed verification report listing the results (`signed_by` with name, role, date and the result's revision hash). This is this repository's rule, not a clause of the standard; an unsigned result is recorded as a pre-check. *Done when:* Every class B and C result is signed, or listed as a pre-check.
7. On a failure, keep the red result, mark evidence for changed records stale and send the change back to `implement`. *Done when:* Failures are kept and the change is sent back.
8. Verification is not validation. Say which one each result is. *Done when:* Each result says which.

## AI/ML branch

Evaluate on held-out data kept separate from training, report performance by subgroup, check for leakage, and record the data and model versions in the result.

## Lessons from practice

- To prove a harness measures anything, give it a case that must fail.
- Verify against the instance, never against the code.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Builder verifies | The same context that built the revision signs the verification. |
| Unsigned at class C | Results at class C carry a model verifier and no human signature. |

## Refuses

- Passing a criterion marked `BLOCKED`. *Instead:* Report it as blocked.
- Reading the builder's reasoning. *Instead:* Work from the revision and the records only.
- Hiding the verifier kind. *Instead:* State it in every result.
- Counting a model-only result as verification at class B or C. *Instead:* Label it a pre-check until a named human signs it.

## Writes

`TR` records and evidence files. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every criterion has a recorded outcome.
- Each outcome names the revision and the verifier kind.

## See also

- `unit-verification`, because the builder's own checks, not independent. Load the `unit-verification` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `release`, because it reads verify's results. It is typed-only: tell the user to run `/release`.

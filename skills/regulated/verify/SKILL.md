---
name: verify
description: "Use when verifying a revision against its requirements."
metadata:
  group: regulated
  invocation: model
  role: "chain step"
  leading_word: "exact revision"
  neighbours: [unit-verification, release, risk]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 5.6", "IEC 62304:2006+A1:2015 5.7", "ISO 13485:2016 7.3.6"]
---

# Verify

Runs integration and system testing on the exact revision and keeps verification apart from validation. For A/B/C, require direct signatures on every result by a named human independent of the author/builder, with competence established by the QMS and established Part 11 surrounding-system controls/intended-use validation. This is stricter repository policy, not universal legal applicability. A report cannot substitute. The shipped backend checks declarations only: verification acceptance and product release remain held (RDS425), even with complete fields, level-3 declarations or GitHub preflight eligibility.

## When to use

- Requirements or design are being reviewed and verification methods must be planned.
- A revision is ready for verification.
- Evidence has become stale after a change.

Not for:

- Checking a unit during build: that is `unit-verification`.

## Reads

The revision, the records, the test cases, the project's declared verifier kind.

## Techniques and timing

Choose and justify the method against the approved plan; do not apply every technique by default. Read the relevant local guide before doing the analysis:

- [Technique selection and procedure](references/test-design.md).
- [Fictional worked example](references/worked-example.md).

## Process

1. Read the safety class from the project block. A, B or C: apply what CLASS-OBLIGATIONS.md lists for it. `none` (not device software, or its class is set by another product): apply the depth the `PLAN` record chose. Not decided: ask the user to decide it through `/intake`, or to choose a depth for now and record it in the `PLAN`; never assume one. While the project claims IEC 62304 for device software, a lower depth cannot be chosen for a class that is not decided: stop and ask for the class to be decided. Read the depth only from an approved `PLAN`; a draft plan sets nothing. *Done when:* The depth applied is named.
2. Plan partitions, boundaries, decisions, states and robustness/regression cases alongside requirements, then execute at the proper level. Read the local technique guide before choosing the method; record prerequisites, first/repeat timing, evidence, limitations and the human decision. These are selectable repository practices unless a cited obligation or approved plan requires more. *Done when:* Method selection and tailoring have a reason, an owner and evidence criteria.
3. Pin the revision under test. Run verification in a separate session or agent that has not seen the builder's conversation or notes, starting from the revision and the records. If your harness cannot start one, record that the verifier shared the build context. *Done when:* The revision is pinned and the verifier's separation is recorded.
4. At class B and C, run integration testing first: integrate the units per the integration plan and test the interfaces and the risk controls between items, with regression testing after each change (62304 5.6). *Done when:* Integration results exist for each integration step, or class A is recorded.
5. Run system testing against every software requirement, by test, inspection or analysis (5.7). Do not edit code or records while testing. *Done when:* Every software requirement has a system test result or a recorded reason.
6. Write one `TR` per test case naming the revision and the verifier kind. *Done when:* Each `TR` names its revision and verifier kind.
7. For A/B/C, require direct signatures on every result by a named human independent of the author/builder, with competence established by the QMS and established Part 11 surrounding-system controls/intended-use validation. This is stricter repository policy, not universal legal applicability. A report cannot substitute. The shipped backend checks declarations only: verification acceptance and product release remain held (RDS425), even with complete fields, level-3 declarations or GitHub preflight eligibility. Keep unsigned/model-only runs as pre-checks and preserve actual failed results. *Done when:* Each result has a direct signature declaration or an explicit gap; no accepted verification is inferred.
8. On a failure, keep the red result, mark evidence for changed records stale and send the change back to `implement`. *Done when:* Failures are kept and the change is sent back.
9. Verification is not validation. Say which one each result is. *Done when:* Each result says which.
10. For every risk-control claim distinguish implementation from effectiveness evidence; coordinate user-facing evaluation with `usability` and `validation` where the risk argument needs it. Retain commands, full log references/hashes, configuration, tool/data versions and actual counts/outcomes; do not claim the validator checks log truth or evidence adequacy. *Done when:* Control evidence and execution provenance are explicit; unrun or unsuitable evidence remains a gap.

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
- Counting a model-only result as verification at A/B/C. *Instead:* Label it a pre-check until a named human signs it.

## Writes

`TR` records and evidence files. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every criterion has a recorded outcome.
- Each outcome names the revision and the verifier kind.

## See also

- `unit-verification`, because the builder's own checks, not independent. Load the `unit-verification` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `release`, because it reads verify's results. It is typed-only: tell the user to run `/release`.
- `risk`, because risk-control claims determine evidence. Load the `risk` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

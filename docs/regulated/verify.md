<!-- docs page for skills/regulated/verify/SKILL.md -->

## What it does

Runs integration and system testing on the exact revision and keeps verification apart from validation. For A/B/C, require direct signatures on every result by a named human independent of the author/builder, with competence established by the QMS and established Part 11 surrounding-system controls/intended-use validation. This is stricter repository policy, not universal legal applicability. A report cannot substitute. The shipped backend checks declarations only: verification acceptance and product release remain held (RDS425), even with complete fields, level-3 declarations or GitHub preflight eligibility.

## When to reach for it

Type `/verify`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| Requirements or design are being reviewed and verification methods must be planned. | `verify` |
| A revision is ready for verification. | `verify` |
| Evidence has become stale after a change. | `verify` |
| Checking a unit during build | [`unit-verification`](../lifecycle/unit-verification.md) |

## Prerequisites

For planning: requirements/design under review, the approved plan depth and the claims to verify. For execution: approved criteria/cases, a pinned revision and the identified test environment.

## Techniques and timing

Select methods for the approved plan and lifecycle stage; the guides distinguish evidence and human decisions:

- [Technique selection and procedure](../../skills/regulated/verify/references/test-design.md).
- [Fictional worked example](../../skills/regulated/verify/references/worked-example.md).

## The exact revision

Verification runs on the exact revision under test. Preserve actual commands, logs, outcomes and failures. For A/B/C, require direct signatures on every result by a named human independent of the author/builder, with competence established by the QMS and established Part 11 surrounding-system controls/intended-use validation. This is stricter repository policy, not universal legal applicability. A report cannot substitute. The shipped backend checks declarations only: verification acceptance and product release remain held (RDS425), even with complete fields, level-3 declarations or GitHub preflight eligibility.

## It's working if

- Every result names a revision and a verifier kind.
- The run includes a control case that failed on purpose.

## Where it fits

Role: chain step. Neighbours: [`unit-verification`](../lifecycle/unit-verification.md), because the builder's own checks, not independent; [`release`](../gates/release.md), because it reads verify's results; [`risk`](../regulated/risk.md), because risk-control claims determine evidence. For the whole map, see [FLOWS.md](../../FLOWS.md).

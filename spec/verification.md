# Verification and independence

Verification is run on the **exact revision** under test. The test result names the revision (a commit hash, or a baseline). A failed run makes the evidence from earlier runs on earlier revisions stale for the records that changed.

## Method selection and control evidence

Plan methods with requirements/design rather than waiting for the executable build. The `verify` skill packages test-design techniques locally, and `unit-verification` applies suitable methods at unit level. Preserve the class-specific integration/system scope and any additional approved plan activities.

ISO 14971:2019 7.2 requires verification of control implementation and effectiveness as distinct claims. One activity may support both with suitable criteria and evidence; user-facing risk-reduction claims may need `usability` evaluation, while technical controls may establish effectiveness through verification. Neither a linked test nor an implementation assertion automatically proves effectiveness or intended-use validation.

Retain actual commands, complete output/log references and hashes, tool/data/environment versions, discovered/executed/skipped counts and observed outcomes. The structural validator does not assess log truth, oracle quality or method adequacy. For safety/security fault injection, fuzzing, stress or attack runs, use an explicitly authorised named non-production target and synthetic/anonymised fixtures, never production or copied customer data.

## Independence and signature

The verifier works from a fresh context that did not build the revision. Its kind is recorded on every test result. The kind is provenance: it says who ran the work. It is not independence in the regulatory sense; that comes from the person who signs.

| Kind | Meaning |
| --- | --- |
| `human` | A person who did not author or build the revision |
| `other_family` | A model from a different maker than the one that built it |
| `same_family_fresh` | The same model family, in a fresh context with no access to the builder's reasoning |

Models may do the verification work at any class. **At A/B/C, a named human independent of the author and builder signs each result directly**, having reviewed it. The adopting QMS establishes the person's competence and authority. The declaration is `signed_by: {by, role, on, ref, revision}`; `revision` is the result's own hash and `ref` identifies the controlled signature event. Supply `authored_by`, `built_by` and the roles file to check declared independence. Missing or invalid direct declarations produce `RDS220` and do not count toward structurally verified coverage. `none` remains distinct and an undecided class is never defaulted.

Direct independent-human result signatures through a Part 11-compliant surrounding system, with established controls and intended-use validation, are mandatory for every A/B/C project as **stricter repository policy**, not a universal legal-applicability claim or an IEC 62304 per-result-signature clause. A `VRP` may summarise results but `covered_by` never substitutes for their direct signatures. Role membership, a signature reference, a hash or an accepted assessment declaration does not authenticate a signer or establish QMS competence/system validation.

The shipped backend cannot establish those external controls. Verification acceptance stays held even when declarations are complete; `records --release` returns nonzero with `RDS425` for A/B/C. No evidence level, local reference, waiver or GitHub authority-preflight success clears that hold. An authorised surrounding QMS/system must establish the real controls and decisions; this library supplies no authenticated signing-system adapter. Use `records --report` for structural checks, not acceptance. This deliberately changes the old class-A-optional and report-substitution contracts; retain historical records and arrange genuine direct review/signing rather than manufacturing retrospective signatures.

The report's legacy `verified` key means structural coverage only. `coverage_scope` is `structural_only`; `results_with_invalid_signature_declarations` identifies excluded signature declarations, `verification_acceptance` exposes the hold, and `accepted_verification_results` remains empty. Superseded, obsolete, structurally invalid and duplicate-identity results cannot supply current evidence even when their hashes match; valid signed-draft results remain structurally eligible. Passing validation results for user needs use the same structural eligibility predicate as requirement coverage, without implying accepted validation.

The verifier kind and the signer are reported in the package and by `status`.

These provenance fields and hashes are not authenticated signatures. Keep [regulatory review](../docs/assurance/regulatory-review.md), actual agent/harness behavior and [host-control observations](../docs/assurance/support.md) separate from structural test results. A trusted GitHub preflight evaluates only its documented repository/commit/policy scope, not the clinical or regulatory correctness of the product.

## What a verifier must not do

- Read the builder's notes, plan or conversation.
- Edit the code or the records it is verifying.
- Pass a criterion marked `BLOCKED`.

## Security diligence

Security work is a sub-process of regulated work, not a separate lane: a threat model that follows architecture changes, dependency and static analysis as the default, an open-finding decision, and a correction loop back to build. Active scanning or penetration testing runs only against an owned-asset list the project keeps, only on a typed approval, and never by default.

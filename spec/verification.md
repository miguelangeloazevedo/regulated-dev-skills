# Verification and independence

Verification is run on the **exact revision** under test. The test result names the revision (a commit hash, or a baseline). A failed run makes the evidence from earlier runs on earlier revisions stale for the records that changed.

## Independence and signature

The verifier works from a fresh context that did not build the revision. Its kind is recorded on every test result. The kind is provenance: it says who ran the work. It is not independence in the regulatory sense; that comes from the person who signs.

| Kind | Meaning |
| --- | --- |
| `human` | A person who did not author or build the revision |
| `other_family` | A model from a different maker than the one that built it |
| `same_family_fresh` | The same model family, in a fresh context with no access to the builder's reasoning |

Models may do the verification work at any class. **At class B and C, a named human independent of the build signs each result** (`signed_by: {by, role, on, revision}`, where `revision` is the result's own hash, so a later edit breaks the signature), having reviewed it. A result without that signature is recorded as a pre-check; the validator refuses it at class B and C and `release` will not accept it. At class A the signature is recommended.

This signature is this repository's rule, not a clause of IEC 62304, which requires verification and plan-level independence of review rather than a signature on each result. The rule is deliberately stricter, because verification done only by a model is the first thing a reviewer will challenge. A project that signs a verification report instead writes a `VRP` record that lists each result id with its revision hash, signs the report with `signed_by: {by, role, on, revision}` where `revision` is the report's own hash, and sets `covered_by: VRP-<n>` on each result. The validator checks the report lists the result's current hash and that its signer is independent and in the roles file.

The verifier kind and the signer are reported in the package and by `status`.

## What a verifier must not do

- Read the builder's notes, plan or conversation.
- Edit the code or the records it is verifying.
- Pass a criterion marked `BLOCKED`.

## Security diligence

Security work is a sub-process of regulated work, not a separate lane: a threat model that follows architecture changes, dependency and static analysis as the default, an open-finding decision, and a correction loop back to build. Active scanning or penetration testing runs only against an owned-asset list the project keeps, only on a typed approval, and never by default.

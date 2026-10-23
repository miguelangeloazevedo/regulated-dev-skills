# Approval and evidence levels

## Approval by reference plus content binding

An approval is recorded on the record it approves:

```yaml
approval:
  by: alice
  role: qa_ra
  on: 2026-10-20
  revision: 3f9c...e1
  ref: pr-482
```

- `revision` is the [revision hash](#revision-hash) of the content approved. Any later edit changes the hash, so the approval becomes stale automatically.
- `ref` points at the host's own approval: a pull request review, a Jira transition, a signed tag, a record-system signature. The agent copies the reference; the host holds the authority.
- The author cannot approve their own record. The validator compares `authored_by` with `approval.by`.
- A roles file says who may approve what.

**Agents prepare approval requests and never invent or impersonate the decision.** `approve` is a typed command; its invocation restriction is not a host permission boundary. A host-held authorised decision must be distinguished from fields an agent can edit.

## Roles file

```yaml
roles:
  engineering: [bob, carol]
  qa_ra: [alice]
approvers:
  un: [qa_ra]
  sys: [qa_ra]
  sw: [engineering, qa_ra]
  spec: [engineering]
  bl: [qa_ra]
```

An approval is valid when `by` is listed under `role`, and `role` is listed for the record's type.

## Revision hash

SHA-256, lowercase hex, over the record file with these removed: the `status:` line and the whole `approval:` block. Line endings normalised to LF and trailing whitespace trimmed first. The validator implements this; adapters must agree with it.

## Evidence levels

The project declares a level. Skills never claim more than that level proves.

| Level | Name | What it gives | What it does not give |
| --- | --- | --- | --- |
| 0 | Convention | Files in a repository. Approvals are fields. The validator checks structure, hash binding, author-not-approver, role validity. | Anyone can edit history. Approvals can be forged. |
| 1 | Host-enforced review | Level 0 plus controls the host enforces: protected branch, required independent reviewer, no force pushes. Declared in the project block; verified where the adapter can. | No cryptographic identity. |
| 2 | Signed approvals | Level 1 plus a signature bound to the revision: signed commits or tags, or an external e-signature, with verified identity. | A signed git tag proves possession of a key, not the meaning of a signature or a controlled closed system; it is not a 21 CFR Part 11 electronic signature. Does not validate the tooling. |
| 3 | Controlled record system | The records live in a record system with an audit trail and electronic signature that the project has validated for its intended use (21 CFR Part 11, Annex 11 style controls), declared with `record_system_validated`. | This repository does not validate your tool. |

A level is a ceiling the project has chosen, not a certificate. An ordinal can hide a project that has some higher properties and not others; `status` reports which properties are actually present.

## Timeouts

Every human decision has a timeout. A pending approval reminds at 3 days. At 14 days it is closed on record as "stopped, no decision". No decision means hold: a skill never proceeds past a gate on silence.

## What the validator does not verify

Names, roles and references in approvals and signatures are text. The record validator checks that they are present, consistent with the roles file and bound to the content hash; it does not authenticate who wrote them. It does not resolve each record's `approval.ref`. The separate trusted GitHub preflight checks an explicitly selected repository, commit, request and policy, not arbitrary per-record signatures or every backend. Keep unsupported properties declared/unassessed; a chosen level is not proof of identity, human decision or record-system validation. See [assurance contracts](assurance.md).

Test results at class A carry no signature, so nothing binds their content to a hash: their integrity rests on the repository history, which is why release needs evidence level 1 (protected branch, required review). Anyone who can rewrite history and recompute hashes can forge records at any level below 3; the validator detects edits, not a determined forger.

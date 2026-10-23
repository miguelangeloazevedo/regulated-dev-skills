# Records

One record is one markdown file with frontmatter. The chain from need to evidence is built from records and typed links.

## Types and identifiers

| Type | Prefix | What it is |
| --- | --- | --- |
| Development plan | `PLAN` | The software development plan, including risk management and configuration management plans |
| Change request | `CR` | A requested change, its impact and its approval |
| Problem report | `PRB` | A problem, its criticality, investigation and safety relevance |
| Design review | `REV` | A design review record with its read-list and statement |
| Release | `REL` | A release decision with the authorising person |
| Verification report | `VRP` | A summary listing results by id and revision hash; it never substitutes for direct result signatures |
| Risk management report | `RMR` | The risk management review and report: plan, overall residual risk, benefit-risk, production and post-production (ISO 14971 9) |
| Classification | `CLS` | Qualification, device class, software safety class and overlays, per module and jurisdiction, with `recheck_by` (the earliest re-check date of its dated sources). Written by `intake` |
| User need | `UN` | What someone must be able to do, and why |
| System requirement | `SYS` | What the system shall do, verifiable at the system boundary |
| Software requirement | `SW` | What the software shall do, derived from one or more system requirements |
| Specification | `SPEC` | How it is built: module, mechanism, and what it refuses |
| Test case | `TC` | A verification or validation procedure |
| Test result | `TR` | One run of a test case on a named revision |
| Hazard | `HAZ` | A potential source of harm |
| Risk control | `RC` | A measure that reduces a risk |
| SOUP item | `SOUP` | Software not developed for incorporation into this device, or previously developed software without adequate records of its development (IEC 62304 3.29). Usually third-party components, but not every dependency is SOUP and not every SOUP is third-party |
| Finding | `FIND` | A weakness, vulnerability or review finding, with a source and a date |
| Decision | `DEC` | A ruling and why |
| Baseline | `BL` | A named set of approved revisions |

Identifiers are `<PREFIX>-<number>`, never reused. File path: `<artefacts_dir>/records/<type>/<ID>.md`.

## Documents versus completed records

The schema calls every file a record; control it according to purpose. A prescriptive document has an enduring identity and controlled revisions; a completed record preserves evidence of activities and decisions. Approval is not automatically effective issue, and a product baseline does not prove current document availability at points of use. Review, distribution, external-origin documents and obsolete-copy controls belong to named QMS/host procedures.

Preserve original observations, results and signatures. Corrections identify the original revision, change, reason, author, date and required authorisation; a new execution needs a new result identity, not an edited pass over a failure. Record retention, protection, retrieval and authorised disposition have named owners. These are content/procedure instructions, not new frontmatter or validator-enforced lifecycles. Read configuration-management's local document-and-record-control guide for the full distinction.

## Frontmatter

```yaml
---
id: SW-12
type: sw
title: Reject out-of-range dose entries
status: draft
derives_from: [SYS-4]
claims:
  statement: observed
  rationale: proposed
authored_by: bob
sources: [IEC 62304:2006+A1:2015 5.2]
as_of: 2026-10-19
approval:
  by: alice
  role: qa_ra
  on: 2026-10-20
  revision: 3f9c...e1
  ref: pr-482
---

## Statement
...
## Rationale
...
## Acceptance criteria
1. ...
```

**One field answers one question.** Rationale is not a paraphrase of the statement. Acceptance criteria are not a paraphrase of the statement. A record where two fields say the same thing has one field's worth of content and looks like two.

## Links

Links are stored in one direction only, upward, as a field naming the target ids. The inverse is computed by the validator and never written, so a pair can never be stored inverted.

| Field | Source type | Target type |
| --- | --- | --- |
| `derives_from` | `SYS`, `SW` | `UN` (from `SYS`), `SYS` (from `SW`) |
| `specifies` | `SPEC` | `SW` |
| `verifies` | `TC` (may also verify an `RC` directly) | `SYS`, `SW`, `SPEC` |
| `validates` | `TC` | `UN` |
| `result_of` | `TR` | `TC` |
| `mitigates` | `RC` | `HAZ` |
| `implements` | `SW`, `SPEC` | `RC` |
| `relates_to` | `FIND`, `PRB`, `REV` | any |
| `addresses` | `CR` | `PRB`, `FIND` |
| `releases` | `REL` | `BL` |
| `supersedes` | any | same type |

A requirement may derive from several parents. `traceability` reports requirements with several parents so a reviewer can see them; nothing forces a single parent.

## Safety paths and control evidence

The standalone record model has no separate Harm or Safety Risk/context record type. Preserve distinct event/situation/harm paths as labelled sections in a `HAZ` body or a controlled referenced analysis. Do not collapse separate paths into one estimate, or claim their semantics are machine-checked. A backend mapping must explicitly preserve them or report the gap.

For each `RC`, record or reference both **implementation verification** and **effectiveness verification** (ISO 14971:2019 7.2): claim/criterion, method, applicable configuration and conditions, case/report, observed result or open gap. One well-designed activity may address both with a stated rationale. User-facing effectiveness may require usability evidence; not every effectiveness claim requires a user study.

These are evidence-content instructions for existing record bodies, not new required frontmatter or automatic validator checks. A linked case does not establish execution or risk reduction. Use the risk skill's local `references/control-evidence.md` worksheet and traceability's local `references/chain-and-coverage.md` for the full distinction.

## Quality-event handoffs

Standalone has no independent complaint, nonconformity, CAPA or action-task record type or lifecycle. Retain originating identities and controlled external references in existing `PRB`, `FIND` and `CR` bodies. Preserve affected configurations, awareness date, safety/interim-protection assessment, investigation evidence, human disposition and pending actions. Unknown, not represented, not applicable with justification and confirmed absent are distinct.

Record containment/correction, corrective/preventive action, implementation verification and effectiveness review separately where applicable. For CAPA handoffs include the approved plan/reference, owner, measurable criterion, scope, monitoring window, observed evidence, adverse-effect review and human closure/rework decision. A green software regression or document approval is not event closure. These are content and external-reference instructions, not new frontmatter, statuses or automatic validator checks; the validator does not establish causal validity, CAPA effectiveness or reportability.

## SOUP records

A `SOUP` record has three sections, and at class B and C an `anomalies_evaluated` date in its frontmatter before release. **Item**: name, version, supplier, how it was found. **Requirements**: the functional and performance requirements it must meet and the hardware and software it needs (IEC 62304 5.3.3, 5.3.4), required at class B and C. **Anomaly list**: where the published anomaly list is, when it was last evaluated, by whom, and the result (7.1.3). The skills draft the item; a person writes the evaluation: source of the anomaly list, version delta from the last evaluated version, applicability to this device, and the test that re-verifies the item.

## Test results

A `TR` names `revision`, `verifier` (kind), `outcome` and, at A/B/C, a direct `signed_by: {by, role, on, ref, revision}` declaration for a named human independent of the author/builder. The adopting QMS establishes competence and authority. Part 11 surrounding-system controls and intended-use validation are universal A/B/C repository policy, distinct from legal applicability. Neither a report nor editable fields establish them. Standalone structural checks do not authenticate signatures; verification acceptance and product release remain held (`RDS425` on `--release`). See `spec/verification.md` in the skills repository.

## Status and approval

An approval block holds only while the record is `approved`. Moving an approved record to any other status is refused while the block is there; `obsolete` is allowed and names what replaced it in `obsoleted_by`.

## Status and staleness

Authored: `draft`, `in_review`, `approved`, `superseded`, `obsolete`. `stale` is **derived**: an `approved` record whose `approval.revision` differs from the hash of its current content is stale. It is never written by hand.

## Claim types

Every non-trivial field carries a claim type: `observed` (read from code or a source), `inferred` (reasoned from evidence), `proposed` (suggested for a human to decide). Fields reserved for a human (rationale, severity, safety class, residual-risk acceptance) are never auto-filled; they stay empty or `proposed`.

## Blocked criteria

When a criterion cannot be written, write it as `BLOCKED`, name what unblocks it, and type it:

- **content**: a hole in the design. Does not advance.
- **scope**: an unmade decision about what is in scope. Does not advance.
- **verification timing**: the statement is complete, only its test cannot run yet. Advances.

Never write a weaker criterion that the item can pass.

## Derived versus authored

A fact owned elsewhere is generated or checked, not typed. A count in prose carries a marker naming its owner, for example `**12**<!--count:children-SYS-4-->` (records linking up to `SYS-4`) or `**27**<!--count:records-sw-->` (records of a type), and the validator recomputes it.

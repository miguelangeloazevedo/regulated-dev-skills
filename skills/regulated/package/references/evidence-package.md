# Evidence indexing and reconciliation

## Selection

Use a generated record/evidence index to assemble a review snapshot, a set reconciliation to detect omissions and unexpected additions, and a route-specific completeness review to identify external documentation and owners. Use a manifest with content hashes to identify exported revisions. These are engineering/document-control practices supporting the cited requirements, not a claim that a spreadsheet or generated index is a regulatory submission.

## Prerequisites

For final assembly read the identified baseline, record statuses/hashes, verification/validation and risk-review evidence, known findings and the declared evidence level. For early review snapshots, define the stage and clearly mark unfinished items. Identify the required document set and owners during development planning; do not discover them only at packaging.

## Timing

Plan contents and ownership early, generate labelled snapshots at reviews, and assemble the final evidence set when the applicable activities are complete. Regenerate after any source change and reconcile before transfer/release. Maintain versioned package references for later investigations and post-production updates.

## Procedure

1. State scope, product/configuration, intended audience, snapshot date/baseline, evidence level and limitations. A decided class is necessary but not sufficient for any conformance claim. Do not infer compliance from a passing validator.
2. Enumerate source records and required external evidence from the named baseline. Record id/type/title, revision/hash, status, source location, owner and relevant result/configuration references. Compute counts from the enumerated set.
3. Reconcile both ways: records/evidence required but missing from the package; package entries absent from the baseline/source; duplicate/conflicting revisions; broken links; stale/unapproved/blocked items; evidence on another configuration. Keep an explicit findings list.
4. Separate planned cases, executed results, control implementation, control effectiveness, intended-use validation and human acceptance. A test link cannot fill an evidence-index result cell. Preserve unknown/partial backend scope and missing permissions/configuration.
5. Review required documentation by the actual EU/US route and product scope. Identify uncovered clinical, usability, cybersecurity, labelling, manufacturing/transfer and post-market documentation with the responsible owner. A generic checklist cannot establish route completeness; have the competent owner confirm it.
6. Render/export from controlled sources, never repair the generated copy by hand. Label drafts, snapshots and authoritative references consistently. Under this repository's existing evidence policy, exports below level 3 are uncontrolled drafts.
7. Open the exported files, verify readability, working references, manifest identities and reconciliation totals. If transfer into an eQMS is needed, name who transcribes/imports and read back the imported revision/reference. A successful upload call is not verified reconciliation.
8. Archive the index/manifest, source version and reconciliation findings with access/retention arrangements. Changes go back to the source and controlled process, not an undocumented edit in the exported PDF.

### Evidence-index template

| Column | Meaning |
| --- | --- |
| Record/evidence id and role | What claim it supports, not just a document title |
| Source/revision/hash | Exact controlled input; hash produced by tooling |
| Status and applicable configuration | Draft/approved/signed/blocked plus tested configuration where relevant |
| Required external evidence | Clinical/usability/security or other document and revision, or named gap |
| Owner and approval reference | Who resolves missing evidence; no fabricated approval |
| Export location and reconciliation | Included/readable/matched, omitted with reason, or discrepancy |

## Evidence

Keep generated index, manifest, validator output, reconciliation report, actual export/open checks and gap owners. Human reviewers assess adequacy and the applicable document set. The current validator does not generate the whole package or check external references/exports; the skill must execute those checks using the selected tools and retain results.

## Limitations

A complete index can still describe inadequate evidence. A controlled document reference does not prove its content is correct, and a signature/hash does not establish clinical validity. An incomplete interim snapshot is useful only if labelled honestly. Never describe the package as a submission, compliant technical file or validated eQMS merely because it opens.

## Human decisions

QA/RA confirms route-specific scope and dispositions. Clinical, usability, security and manufacturing owners supply/review their evidence. People authorise release and any permitted waiver; the agent cannot waive law, risk acceptance or a release blocker.

## Sources

- ISO 13485:2016 §§4.2.3, 4.2.4-4.2.5, 7.3.10.
- MDR Annexes II-III for the EU technical-documentation interface, not a claim that this index supplies all required content.
- IEC 62304:2006+A1:2015 §5.8 for software release/archiving interfaces, preserving class applicability.

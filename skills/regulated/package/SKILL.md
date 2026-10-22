---
name: package
description: "Use when assembling the documentation package."
metadata:
  group: regulated
  invocation: model
  role: "chain step"
  leading_word: "generated from records"
  neighbours: [verify, release, traceability]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["ISO 13485:2016 7.3.10", "ISO 13485:2016 4.2.3"]
---

# Package

Builds the design and development file index from approved records and verification results, not from memory. It supports the technical documentation (MDR Annex II and III, or a US submission) and is not that documentation.

## When to use

- Record/evidence requirements are being planned, or a labelled interim review snapshot is needed.
- A baseline passed verification and the package is needed.
- A submission or audit pack is being prepared.

Not for:

- A final release package is requested without verified baseline evidence: use `verify`; an incomplete interim snapshot must remain explicitly labelled.

## Reads

The baseline, approved records, `TR` records, findings, the project block.

## Techniques and timing

Choose and justify the method against the approved plan; do not apply every technique by default. Read the relevant local guide before doing the analysis:

- [Technique selection and procedure](references/evidence-package.md).
- [Fictional worked example](references/worked-example.md).

## Process

1. Generate an evidence index, reconcile it both ways and preserve missing evidence and external-document owners. Read the local technique guide before choosing the method; record prerequisites, first/repeat timing, evidence, limitations and the human decision. These are selectable repository practices unless a cited obligation or approved plan requires more. *Done when:* Method selection and tailoring have a reason, an owner and evidence criteria.
2. Before stating conformance to IEC 62304 anywhere in the package, confirm every device software system has a decided class; if one does not, state that conformance cannot be claimed yet and why. State the evidence level on the front page with the warning that levels 0 to 2 are document-control tiers of this repository, not a 21 CFR Part 11 or Annex 11 claim, and must not be cited as such in a submission. *Done when:* The conformance statement and the evidence-level warning are on the front page.
3. Compare the generated index with the records directory and report any record in one but not the other. *Done when:* The two match, or differences are listed.
4. Read the baseline and list its records with their revision hashes. *Done when:* Each line has an id and a hash.
5. Stamp each document as ledger, snapshot (with its date), current, or generated. *Done when:* Every document has a kind.
6. Exclude or clearly label any record that is stale, unapproved or `BLOCKED`. *Done when:* None slip in unlabelled.
7. Generate the index and the documents from the records. Counts are computed. *Done when:* Every line links to a source record.
8. Stamp the package with the evidence level and, below level 3, as an uncontrolled draft. *Done when:* The stamp and level are on the first page.
9. List the technical documentation sections the index does not cover, so nobody mistakes it for the whole file: device description and variants, the software architecture description the technical documentation needs even where IEC 62304 class A does not require one (MDR Annex II), UDI (MDR Art 27), labelling and information supplied by the manufacturer, the general safety and performance requirements checklist (MDR Annex I), benefit-risk analysis, clinical evaluation and post-market clinical follow-up, the post-market surveillance plan. Name the owner of each. For a US submission, also list: software documentation at the recorded Basic or Enhanced level, cybersecurity documentation (including the SBOM for a cyber device), the submission's own sections for its pathway (510(k), De Novo or PMA), labelling, and human factors documentation; each with its owner. *Done when:* The uncovered sections are listed on the first page.
10. Export in the formats asked for. *Done when:* The export opens and matches the index.
11. State the single source of truth for each item and who transcribes it into the QMS or eQMS, and reconcile the two before release: every exported item carries its revision hash, and an export below evidence level 3 is stamped as an uncontrolled draft. *Done when:* Each item names its source of truth; the export is stamped as the evidence level requires.
12. Plan document ownership early, then reconcile required/source/export sets in both directions. Distinguish planned cases, observed results, control implementation/effectiveness and external clinical/usability/security evidence. Open the real export and verify identities/readability; incomplete retrieval or an unconfigured backend stays an explicit scope limitation. *Done when:* The index/export reconciliation and external evidence gaps have owners and actual check results.
13. Preserve completed records, raw evidence, original signatures and identifiable correction/amendment history. Name archive/access and retention/disposition owners and verify retrieval/readability; an export is not proof of effective distribution, authenticated immutability or authorised destruction. Keep external-origin document editions and controlled references in scope. *Done when:* The package preserves original evidence and correction context, with retrieval and retention controls or explicit gaps.

## AI/ML branch

Include the model card equivalent: intended use, training and evaluation data description, performance by subgroup, known limits, update plan.

## Lessons from practice

- Put two representations side by side. A partial set looks complete from inside.
- Mark documents as ledger, snapshot, current or derived. Reading a snapshot as current is the common failure.
- Derive, do not list. A hand-kept copy falls out of date at the first change.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Handmade package | Counts in the package do not match the records. |

## Refuses

- Describing the package as a submission or as compliant. *Instead:* Say it supports the preparation of one.
- Including an unapproved record unlabelled. *Instead:* Label it or leave it out.
- Editing a generated document by hand. *Instead:* Change the record and regenerate.

## Writes

The package under `artefacts_dir/packages/`.

## Done when

- Every line links to a record and a hash.
- The evidence level is stated.

## See also

- `verify`, because its results are in the package. Load the `verify` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `release`, because it checks the package matches the baseline. It is typed-only: tell the user to run `/release`.
- `traceability`, because scope and evidence gaps must survive export. Load the `traceability` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

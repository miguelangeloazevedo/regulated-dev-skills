---
name: validation
description: "Use when validating the product against user needs. Design validation under ISO 13485 7.3.7."
metadata:
  group: lifecycle
  invocation: model
  role: "chain step"
  leading_word: "intended users, intended environment"
  neighbours: [user-needs, usability, verify]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["ISO 13485:2016 7.3.7", "MDR Art 61", "MDR Annex XIV", "MDCG 2020-1"]
---

# Validation

Validates that the finished product meets its user needs and intended use (ISO 13485 7.3.7) by the method each need calls for: summative usability results, simulated use, clinical data through the clinical evaluation, or analysis. It prepares and records; people run the sessions. Usability engineering itself is in `usability`.

## When to use

- A production-equivalent build exists and design validation is due.
- A change touches a user need or the intended use.

Not for:

- Checking the product against requirements: use `verify`.
- Use specification, user interface specification, formative or summative evaluation: use `usability`.

## Reads

`UN` records and their validation methods, the use specification, `HAZ` records, the `PLAN` record, the released or release-candidate baseline.

## Process

1. Plan the method with needs and the development plan even though execution needs representative product evidence. Agree with `risk` and `usability` which risk-control effectiveness claims require user-facing evaluation and which can be established by technical verification; do not equate effectiveness verification universally with validation. *Done when:* Planned validation and control-effectiveness responsibilities are distinct and traceable.
2. Plan design validation for every user need with the method that fits it: usability testing with intended users, simulated use, clinical data through the clinical evaluation, or analysis. Take the summative usability results from `usability` as the evidence for needs that depend on use; the usability engineering file stays its own record. *Done when:* Every user need has a validation method and the representative product is named.
3. Record results as `TR` records against the `TC` that validates each need. For use errors observed in validation sessions, hand them to `usability` for root-cause analysis; if anything new appears, return to the earlier steps; otherwise evaluate residual use-related risk (5.9, ISO 14971 7.3). Keep everything in the usability engineering file (4.2). *Done when:* Every use error has an analysis, and residual use-related risk is evaluated.
4. Where a need depends on clinical evidence, write the interface to the clinical evaluation in the three components MDCG 2020-1 uses for software: valid clinical association (is the output associated with the clinical condition), technical performance (does it generate the intended output reliably), and clinical performance (does it yield clinically relevant output in the target population); for each, the claim, the evidence source and the owner (MDR Art 61, Annex XIV). Do not perform the clinical evaluation. *Done when:* Each clinically dependent need has its claim, endpoints, data source and owner named.
5. For each need validated through clinical evidence, record the clinical evaluation report's identifier and revision in the Result section of the `TR` for that need, so traceability shows which report backs it. *Done when:* Every need that depends on clinical evidence names the report and revision it rests on.
6. Keep a per-need validation inventory: planned method/case, not-run or blocked activities, actual result/outcome and applicable representative baseline, with external clinical/usability report revisions where needed. Report it separately from verification metrics and literal validator output; the current routine report does not provide a separate validation inventory. No completed host execution status alone proves a passing result. *Done when:* Every need has an explicit validation evidence state and provenance or an open gap, separately from requirement verification.

## AI/ML branch

Validate with data from the intended population and setting, report performance by subgroup, and include what the user does with a wrong output.

## Lessons from practice

- Validate needs with intended users in the intended environment; requirements tests do not stand in.
- Assess each use-related observation for safety relevance; link an existing/new risk path or record a justified non-safety conclusion.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Team validation | Participants are the developers and their colleagues. |
| Requirements renamed | The validation protocol is the system test plan with a new title. |

## Refuses

- Validating with the team instead of intended users. *Instead:* Recruit representatives of the intended user groups, or record why not.
- Recording a session nobody ran. *Instead:* Prepare the protocol and the record; people run the session.
- Declaring clinical performance from usability results. *Instead:* Point to the clinical evaluation.

## Writes

The validation plan and protocol, `TC` and `TR` records for each user need. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every user need in scope is validated on a named baseline or listed as open.
- Needs that depend on use cite the summative usability results.

## See also

- `user-needs`, because each need carries its validation method. Load the `user-needs` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `usability`, because provides the summative results. Load the `usability` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `verify`, because checks requirements, not needs. Load the `verify` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

---
name: release
description: "Release a baseline after verification, package and a human decision."
disable-model-invocation: true
argument-hint: "<baseline-id>"
metadata:
  group: gates
  invocation: typed
  role: "gate"
  leading_word: "one-way door"
  neighbours: [verify, configuration-management, maintenance]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["ISO 13485:2016 8.2.6", "IEC 62304:2006+A1:2015 5.8", "ISO 14971:2019 9"]
---

# Release

Checks that the software release activities are done, then records the decision of the person who authorises release. A release is never inferred from passing tests.

Typed commands provide invocation control, not an operating-system permission boundary. An instruction or editable approval field does not establish host-enforced authority.

Run this only when a person types `/release`. If you reached this skill on your own, stop and ask the user to type the command.

## Reads

The baseline, test results, the package, open findings, approvals, the project block.

## Process

1. Before claiming controlled release, require structural readiness and the separate trusted host-authority check for the exact requested revision and policy. Unsupported, unavailable, stale or contradicted controls hold the authorisation gate. A green validate.py --release result is structural only. *Done when:* The human release decision and current host evidence exist; neither a declared level nor a validation reference string is treated as proof.
2. Read the safety class from the project block. A, B or C: apply what CLASS-OBLIGATIONS.md lists for it. `none` (not device software, or its class is set by another product): apply the depth the `PLAN` record chose. Not decided: ask the user to decide it through `/intake`, or to choose a depth for now and record it in the `PLAN`; never assume one. The release clauses that apply at every class still apply to device software. While the project claims IEC 62304 for device software, a lower depth cannot be chosen for a class that is not decided: stop and ask for the class to be decided. Read the depth only from an approved `PLAN`; a draft plan sets nothing. *Done when:* The depth applied is named.
3. Read the evidence level. At level 0 approvals and signatures are unauthenticated text: stop, and tell the user that release needs level 1 or above; the records may still be exported as an uncontrolled draft, stamped as such on every page. *Done when:* The evidence level is 1 or above, or the release stops and the export is stamped uncontrolled.
4. For controlled documents, approved is not automatically effective: identify the exact revision, authorised effective date/conditions and actual issue evidence under the document procedure. Product release does not itself issue every supporting document. Confirm current versions at required points of use and control obsolete copies through the responsible issuer; unknown distribution/effectiveness remains a gap, not a new standalone status. *Done when:* Document issue applicability and any pending effective-use/distribution conditions are explicit and human-owned.
5. If any software system has no decided class (A, B, C, or `none` for software that is not a device), stop: nothing is released with the class not decided. Where IEC 62304 is claimed, say also that the standard applies class C requirements to a system until it is classified (4.3 g). The skills do not fill the class in; a person decides it with `/intake` and `/approve`. *Done when:* Every software system has a decided class, or the release stops.
6. Confirm the agent toolchain validation the development plan references is complete. If it is still open, stop. *Done when:* The validation reference is complete, or the release stops.
7. Run `python3 tools/rds/validate.py records <artefacts_dir> --roles <roles_file> --project <block file> --release --baseline <baseline commit>` with the paths from the project block. Any error stops the release. *Done when:* The `--release` run exits 0, with its output kept in the `REL` record.
8. Read the uncovered technical-file items and owners from the package. Any item without an owner, or not yet done, stops the release unless QA/RA records a waiver with its rationale in the `REL` record. These cannot be waived: an undecided safety class while IEC 62304 is claimed, a residual risk not accepted by its owner, a risk control without a passing verification on the baseline, and any `--release` validator error. *Done when:* Every uncovered item is done, or waived by QA/RA with a rationale.
9. Confirm all verification is complete and evaluated on the baseline revision (62304 5.8.1), that validation of the user needs in scope is complete, and that, under this repository's rule, each result at class B and C is signed by a named human independent of the build. *Done when:* Each check is pass or fail with record ids behind it.
10. Document every known residual anomaly (5.8.2). For class B and C, evaluate each so none contributes to unacceptable risk, with the reason for leaving it unfixed (5.8.3). Confirm the published anomaly lists of SOUP items were evaluated (7.1.3). *Done when:* The anomaly list exists, each anomaly has an evaluation where the class requires, and SOUP anomaly review is referenced.
11. Document the version being released (5.8.4). For class B and C, document how and in which environment it was built (5.8.5) and that every plan activity is complete (5.8.6). *Done when:* Version, build procedure and environment, and plan completion are recorded as the class requires.
12. Review risk-control implementation and effectiveness evidence separately, with the applicable configuration and conditions. Confirm that scope/configuration gaps, missing user-facing evidence and incomplete graph retrieval have not been counted as passing coverage. These are human evidence reviews beyond the structural validator; unresolved required evidence is not a green release. *Done when:* Control claims and assessment limits have explicit human-reviewed dispositions before release.
13. Confirm the risk management review is done and the overall residual risk is acceptable (ISO 14971 9), and that no open critical finding remains. *Done when:* The risk management review is referenced.
14. Record design transfer (ISO 13485 7.3.8): the outputs that move, the deployment or installation procedure, the target environment and its configuration, the check that the software works as specified there, and any residual issues with owners. Confirm each supplier on the plan's list has a current evaluation in your purchasing process (7.4). Include the build environment (toolchain versions, build scripts, configuration) so the released build can be reproduced. *Done when:* A transfer entry exists with procedure, environment, check and residual issues, and every listed supplier has an evaluation reference.
15. List every one-way door (permanent identifiers, stored values or orderings, permission or scope changes, data migrations) with its decision, and list risk-control tests without red evidence as findings for the person to weigh. Red evidence is recommended practice here, not a regulatory requirement. *Done when:* One list exists, with a decision per one-way door.
16. Immediately before the decision, echo the baseline id, its hash, the target and the backend in one line. Then the person who authorises release records the decision with name, role and date (ISO 13485 8.2.6). *Done when:* A `REL` record names the authorising person and the baseline hash confirmed in the echo.
17. Archive the software, its configuration items and documentation for the required retention period, and confirm the delivery route protects it from corruption or unauthorised change (5.8.7, 5.8.8). *Done when:* Archive location and delivery route are recorded.
18. Test results and verification reports are signed, not approved, and the release record is written by this skill; that is why the approved-record check covers the other record types. Say so in the `REL` record. *Done when:* The `REL` record states which records were approved, which signed.

## Lessons from practice

- Treat permanence as a property of the change. A rename after the first record exists is a migration, not an edit.
- A check that has only ever passed has not been tested. Break the thing on purpose once and keep the red run.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Green means go | Release is inferred from a passing pipeline instead of recorded as a decision. |
| Hidden permanence | A rename ships inside a feature change and nobody listed it. |

## Refuses

- Releasing with stale, unapproved, unverified or unsigned records. *Instead:* List them and send the change back.
- Describing the release as compliant or certified. *Instead:* Say what the evidence level supports.
- Releasing on silence. *Instead:* Hold; remind at 3 days, close on record at 14.
- Recording a release decision for someone else. *Instead:* Prepare the record; the authorising person records it.

## Writes

A `REL` record, the anomaly list, the baseline tag and the archive reference. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every release activity the class requires is recorded.
- A named person authorised the release of a named baseline hash.
- Known residual anomalies are documented.

## See also

- `verify`, because its signed results on the baseline revision are what release checks. Load the `verify` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `configuration-management`, because it formed the baseline being released. Load the `configuration-management` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `maintenance`, because the software's regulated life continues there. Load the `maintenance` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

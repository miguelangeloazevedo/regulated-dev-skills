# Techniques and lifecycle handoffs

This is a method-selection map, not a mandatory checklist. The approved plan selects techniques and explains tailoring. A standard may require an activity without mandating the particular technique suggested here. Read the cited edition and route; these skills do not certify compliance.

| Owner | Selectable techniques and local guidance | Producer -> consumer |
| --- | --- | --- |
| `risk` | [Preliminary hazard analysis, FMEA, selected FTA, estimation and control evidence](../skills/regulated/risk/references/analysis-techniques.md) | Intended use, tasks, architecture, anomalies -> control requirements, verification/effectiveness claims, residual-risk review |
| `security-diligence` | [Threat modelling, abuse cases, analysis/test selection, SBOM and vulnerability triage](../skills/regulated/security-diligence/references/threat-model-and-testing.md) | Assets/trust boundaries -> design controls, safety links, security evidence and response |
| `verify` | [Partitions, boundaries, decisions, states, robustness and regression](../skills/regulated/verify/references/test-design.md) | Approved requirements/design and plan -> cases/results, independent review and new findings |
| `traceability` | [Safety/design chain review, coverage dimensions and impact traversal](../skills/regulated/traceability/references/chain-and-coverage.md) | Records, configured relationships and actual evidence -> measured coverage, unknowns, change/release review |
| `configuration-management` | [Item identification, change accounting, manifests, rebuild and recovery](../skills/regulated/configuration-management/references/baseline-and-change-control.md) | Plan, source, dependencies and tooling -> controlled tested/released configurations |
| `package` | [Evidence indexing, reconciliation, completeness and export checks](../skills/regulated/package/references/evidence-package.md) | Baseline and evidence -> labelled review/export index and external-document owners |

## Early planning

`intake` establishes scope and human classification; `development-plan` sets depth, responsibilities, selected techniques and review criteria. `user-needs` and `usability` establish intended use, user profiles, environment and tasks. Begin preliminary hazard analysis, security assets/boundaries, trace identifiers, configuration control and document planning now. A complete architecture is not a prerequisite for asking the early safety/security questions.

Plan verification methods when requirements are drafted. Derive partitions, decisions and state conditions early enough to reveal ambiguity. Define control implementation and effectiveness claims before choosing tests. Plan usability evaluation early; do not wait for a finished interface to discover intended user groups.

## Design and build

`specifications` refines architecture/interfaces and SOUP requirements. Refine FMEA/selected fault trees and threat models with the design; send findings back to risk and requirements before approval. `usability` owns task/scenario analysis and formative evaluation. `implement` and `unit-verification` own construction, unit-level tests/analysis, coding-standard checks and risk-control red runs; `verify` owns subsequent integration/system campaigns. Keep software safety class distinct from device regulatory class.

Configuration items and the authorised change are named before edits; trace links are updated with each change. A new dependency, permission, interface or control assumption reopens the relevant analysis. Code-extraction skills supply candidates and inventories, not justification of intended use or manufactured retrospective approvals.

## Verification and validation

Integration testing under IEC 62304 §5.6 applies at B/C; system testing §5.7 applies at A/B/C. The plan can add testing beyond those minima. Choose method and coverage for the actual claim, not just the class label. Preserve failed/blocked outcomes, commands, logs, tool versions and exact configuration. A fresh-context run is provenance, not human regulatory independence by itself.

Risk-control implementation and effectiveness are distinct claims; one well-designed activity can support both. `usability` runs formative work during design and summative evaluation on the suitable final interface; people run the sessions. `validation` addresses intended use and user needs and cites the clinical evaluation where needed. Not all effectiveness checks are usability studies, and not all successful software tests validate intended use.

## Release and feedback

`design-review` assesses method fitness, assumptions and evidence adequacy, not just populated links. People approve records and accept risks. `package` can produce labelled interim review snapshots; final assembly uses the identified baseline and reveals missing external documentation. `release` remains human-only and uses actual evidence; passing the structural validator is not permission or compliance.

`maintenance` and `problem-resolution` route complaints, use difficulties, new threats, SOUP anomalies and changed clinical/design assumptions back through risk, security, usability and impact. A new baseline does not erase old failures or establish new evidence automatically.

## Evidence boundaries

The current validator measures supported record structure and selected links/hashes. It does not assess method suitability, control effectiveness, clinical correctness or identity of an approval. Coverage dimensions must stay separate: link present, scope assessable, approval current, case executed, result passing, tested configuration matching, and control effectiveness supported.

For an unimplemented backend, missing permissions, incomplete pagination or unconfigured test connection, report unknown/partial scope. Do not turn unknowns into either covered or missing-link counts. The [backend contract](backends.md) describes capabilities, not shipped adapters.

# Risk analysis techniques

These are selectable working methods, not a requirement to perform every analysis. The risk owner approves the selection and criteria in the plan. ISO 14971 defines the risk management process; FMEA and FTA support it, not replace it.

## Selection

| Question | Method to consider | What it misses by itself |
| --- | --- | --- |
| What could harm patients, users or others, including normal operation? | Preliminary hazard analysis organised by intended use, safety characteristics and lifecycle phase | A preliminary analysis needs refinement when design information arrives |
| How can an item, function or interface fail, and what follows? | Design/software FMEA; process FMEA when a production/service process matters | Failure-first analysis misses some normal-use hazards and combinations |
| What combinations could produce a selected hazardous top event? | Qualitative fault-tree analysis (FTA) | An omitted cause or wrong independence assumption makes a convincing but incomplete tree |
| How can a user task produce a hazardous situation? | Task analysis and hazard-related use scenarios, owned by `usability` | A use-error list alone does not establish harm, risk or control effectiveness |

Select complementary methods for the product, not for the length of a checklist. A simple design can use a concise hazard table; a complex interacting control may justify FMEA plus FTA. Record why a method was selected or not needed. FMECA adds criticality prioritisation; do not imply it is required by ISO 14971.

## Prerequisites

Read the approved intended use, foreseeable misuse, use specification, system boundaries, lifecycle phases, risk plan and manufacturer-set acceptability policy. Identify analysis participants and competencies. Severity and probability scales, criteria and acceptance are human decisions. Undecided values stay unrated. Design-specific analysis also needs architecture, interfaces, SOUP requirements and known anomalies.

## Timing

Begin preliminary analysis with needs and use specification, before design choices harden. Refine FMEA and selected fault trees with architecture, interfaces and detailed design. Re-evaluate against requirements, implementation and verification findings. Reopen for new use errors, vulnerabilities, SOUP anomalies, changed controls, production feedback or changed assumptions. Plan post-production collection before release.

## Procedure

1. Define analysis scope, revision, normal/fault conditions and lifecycle phase. Include installation, configuration, maintenance, update and decommissioning where relevant.
2. Describe each path separately: hazard -> event sequence or combination -> hazardous situation -> harm. One hazard may produce several situations and harms. Do not collapse them into one convenient rating.
3. For an FMEA, enumerate item/function and boundary, plausible failure mode, cause, local effect and system effect. Trace each safety-relevant effect to a risk path. Include missing, late, wrong, repeated and inconsistent information when relevant, not just crashes.
4. For a fault tree, define an observable top event, scope and conditions. Expand causes with justified AND/OR relationships; review common causes, dependent failures and external conditions. Stop at explicitly justified boundaries, not at an arbitrary depth. Do not calculate probabilities from guessed software failure rates or multiply dependent events as if independent.
5. Estimate the risk for each hazardous situation using evidence applicable to this device. Record source, assumptions, uncertainty and possible harm. P1 (hazardous situation) and P2 (harm conditional on it) may help structure an estimate, but decomposition is optional. If probability of harm cannot be estimated, record the possible consequences and apply the plan's human-approved criteria for that case. Do not invent a failure probability for systematic software faults.
6. Evaluate against the criteria and propose controls in priority order: inherent safety by design, protective measures, information for safety. Check each control's feasibility, enforcing mechanism and effects on other risks.
7. Follow [control-evidence.md](control-evidence.md) for implementation, effectiveness, residual-risk and review evidence. Feed accepted control requirements into `requirements`, not directly into unapproved code.

### FMEA working template

One row can point to several distinct risk paths; split paths when situations, harms or estimates differ.

| Field | Enter |
| --- | --- |
| Analysis identity | Scope, revision, method, analyst and reviewer |
| Item/function/interface | What must happen and its boundary |
| Failure mode and cause | How it deviates and why it could happen; assumptions explicit |
| Effects | Local effect, system effect and affected user/patient |
| Risk path references | Hazard, event sequence, hazardous situation and harm; use a path label in the record body |
| Initial estimate | Severity/probability basis or unrated; never an agent acceptance |
| Proposed controls | Mechanism, requirement/design references, responsible owner |
| Evidence | Implementation claim/result and effectiveness claim/result |
| Follow-up | Residual-risk evaluation, new-risk review, open action and human decision |

If a project uses RPN or detectability for prioritisation, name its scales and limitations separately. A low RPN cannot overrule severe harm or replace the device's risk acceptability criteria. Detection matters only through the justified path by which it prevents harm.

## Evidence

Keep method selection, scope, participants, revisions, assumptions and findings in the risk file, with links to `HAZ`, `RC`, requirements, test cases/results and usability evidence. Existing record types remain sufficient: an analysis table can be a controlled supporting document. The record validator checks structure; it does not judge an FMEA or fault tree's completeness.

## Limitations

These are repository working templates, not reproductions of complete IEC technique standards. Neither a complete FMEA table nor a plausible fault tree proves all hazards were identified. Real data from similar devices may inform an estimate only with its relevance and limitations assessed; recollection is not evidence. Do not use likelihood of exploitation or a vulnerability score as probability of patient harm.

## Human decisions

The risk owner approves criteria, technique selection, estimates and residual-risk decisions. Clinical evaluation owns clinical benefit evidence. The agent drafts analyses and highlights uncertainty; it does not accept risks or perform an unobserved user evaluation.

## Sources

- ISO 14971:2019 §§4.4, 4.5, 5.2-5.5, 6, 7-10; Annex C (informative).
- IEC 62304:2006+A1:2015 §7, with class applicability checked against the project's edition.
- IEC 62366-1:2015+A1:2020 §§5.1-5.5 and 5.8-5.9 for use-related inputs and evaluation.
- [IEC 60812:2018 publisher abstract](https://webstore.iec.ch/en/publication/26359): FMEA/FMECA purpose and scope; not a claim of implementing every clause.
- [IEC 61025:2006 publisher abstract](https://webstore.iec.ch/en/publication/4311): FTA purpose and assumptions.

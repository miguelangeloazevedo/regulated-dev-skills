# Risk controls and evidence

## Two claims, not one checkbox

ISO 14971:2019 §7.2 separates implementation verification from effectiveness verification. One activity may support both if its design and results actually address both claims; two separate experiments are not inherently required.

| Claim | Question | Example evidence | Insufficient substitute |
| --- | --- | --- | --- |
| Implementation | Is the chosen measure present in the intended design/process? | Inspection and tests of the specified interlock, alarm or limit on the identified configuration | A requirement that merely describes the measure |
| Effectiveness | Does it achieve the risk reduction attributed to it? | Verified limiting performance; representative-user evaluation of recognition/action where needed | A screenshot of an alarm or a passing visibility assertion alone |

Choose the effectiveness method from the control mechanism and risk-reduction claim. It may be design verification, process qualification or design validation. Not every control needs a user study, and not every user study establishes clinical benefit.

## Policy, calculation and decision

Bind each evaluation to the approved policy revision: risk plan, severity/probability definitions, acceptability criteria, mapping/method revision, product configuration and input/evidence revisions. Keep initial and residual evaluations distinct for each situation/harm path. A configured ordinal lookup is not numerical probability multiplication; retain its definitions and limitations rather than invent numerical precision.

A calculated acceptable band is **not human acceptance**, a benefit-risk analysis or proof of supporting benefit evidence. Preserve the calculation and its criteria separately from the authored disposition, benefit evidence and authorised human approval. Neither a populated acceptance field nor a Closed status proves the decision or its revision binding.

Changes to severity, scales, mapping policy, criteria, context or control assumptions trigger an impact assessment, recalculation where relevant, and explicit human reapproval or a justified reviewed applicability decision. Recalculation and reapproval are separate outcomes. A failed refresh or failed reopening is an unresolved freshness gap even if old numbers or an approval badge remain visible. Do not automatically carry earlier approval over to a new policy revision. These reviews are not automatic standalone validator features.

## Control worksheet

For each `RC`, record in its body or a controlled referenced table:

- Hazard and risk-path references: situation, harm and affected population.
- Analysis origin and affected item, process, task/use scenario or safety characteristic; supporting evidence and policy revision.
- Control option considered and priority; why a lower-priority option is necessary.
- Enforcing mechanism and its allocation to software, hardware, process or information.
- Implementing requirements/design and their revisions.
- Implementation verification: criterion, method, case, result and tested configuration, or open gap.
- Effectiveness verification: risk-reduction claim, criterion, method, case/report, result and applicable configuration/user conditions, or open gap.
- Additional hazards/risks introduced, interactions with other controls and common dependencies.
- Explicit causality where a control creates a secondary risk: originating control -> introduced path, with affected assumptions and evidence. Keep shared-control dependencies visible rather than averaging their risks.
- Residual-risk estimate/evaluation, remaining uncertainty and information to be disclosed.
- Human reviewer/decision reference; open actions and owners.

This is guidance for existing records, not new mandatory frontmatter. The current validator does not enforce the two evidence claims or authenticate a user study. Describe missing evidence as a finding, not as a machine-verified pass.

Standalone has no dedicated machine-traversable risk-to-risk introduction relation. Preserve these causal references in controlled bodies or supporting analyses; a general association is not proof of causality or automatic change-impact traversal.

## Risk/usability interface

Start with the use specification and tasks. Feed foreseeable use errors and hazard-related scenarios from `usability` to the risk analysis before architecture approval. Send control requirements back to the user interface specification. Formative findings refine the design and risk paths; summative findings feed residual use-related risk evaluation. Errors, close calls and difficulties are observations to analyse, not automatic proof of a new hazard or proof that the user is at fault. Record relevance, root-cause investigation, linked existing/new risk path or a justified non-safety conclusion.

Information for safety is not effective merely because it exists or a user says they read it. Establish what the intended user must perceive, understand and do, in which environment and time. Avoid crediting training or labelling twice for the same assumed behaviour. Human reviewers determine the appropriate evaluation and any disclosure of residual risk.

## Individual residual-risk evaluation

Evaluate each residual risk against the approved plan after the controls are implemented (§7.3). Record the estimate, criteria, evidence and conclusion for that situation/harm path; do not substitute an aggregate score.

## Unacceptable individual residual risk

If a residual risk fails the plan's criteria, **return to control-option analysis** (§7.1) and consider further controls (§7.3). Do not skip directly to overall residual-risk acceptance.

Where further control is not practicable, §7.4 permits a benefit-risk analysis for that individual residual risk, using applicable data and literature. Clinical evaluation owns the benefit evidence; the risk owner and authorised reviewers assess whether it supports benefits of the intended use outweighing this residual risk. The agent drafts the analysis, never the acceptance.

If the evidence does not support that conclusion, consider modifying the device or intended use and re-enter the analysis at §5.2; otherwise the risk **remains unacceptable**. Missing benefit evidence is an unresolved gap, not an accepted risk. Proceed to the following risk-control and overall-risk reviews only with an appropriate supported disposition. This branch applies under ISO 14971 generally, not only for EU devices.

## Overall residual risk and feedback

Check risks created by controls (§7.5) and completeness of risk control (§7.6), then evaluate overall residual risk (§8). This aggregate evaluation is neither an average of FMEA scores nor a substitute for the individual-risk disposition above. Address interactions, uncertainty and the device's overall benefit-risk picture. For EU devices, apply the relevant MDR risk-reduction and benefit-risk requirements in addition to ISO criteria; clinical evaluation supplies the benefit evidence.

Before release, the assigned person reviews the plan's execution, overall residual-risk acceptability and arrangements for production/post-production information (§9); draft the `RMR` for approval. After release, route new safety information to risk review, problem resolution and controlled change (§10). A new use problem or control failure may invalidate an earlier effectiveness assumption even if no record hash changed.

See [worked-example.md](worked-example.md) for an intentionally incomplete fictional slice.

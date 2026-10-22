# Risk controls and evidence

## Two claims, not one checkbox

ISO 14971:2019 §7.2 separates implementation verification from effectiveness verification. One activity may support both if its design and results actually address both claims; two separate experiments are not inherently required.

| Claim | Question | Example evidence | Insufficient substitute |
| --- | --- | --- | --- |
| Implementation | Is the chosen measure present in the intended design/process? | Inspection and tests of the specified interlock, alarm or limit on the identified configuration | A requirement that merely describes the measure |
| Effectiveness | Does it achieve the risk reduction attributed to it? | Verified limiting performance; representative-user evaluation of recognition/action where needed | A screenshot of an alarm or a passing visibility assertion alone |

Choose the effectiveness method from the control mechanism and risk-reduction claim. It may be design verification, process qualification or design validation. Not every control needs a user study, and not every user study establishes clinical benefit.

## Control worksheet

For each `RC`, record in its body or a controlled referenced table:

- Hazard and risk-path references: situation, harm and affected population.
- Control option considered and priority; why a lower-priority option is necessary.
- Enforcing mechanism and its allocation to software, hardware, process or information.
- Implementing requirements/design and their revisions.
- Implementation verification: criterion, method, case, result and tested configuration, or open gap.
- Effectiveness verification: risk-reduction claim, criterion, method, case/report, result and applicable configuration/user conditions, or open gap.
- Additional hazards/risks introduced, interactions with other controls and common dependencies.
- Residual-risk estimate/evaluation, remaining uncertainty and information to be disclosed.
- Human reviewer/decision reference; open actions and owners.

This is guidance for existing records, not new mandatory frontmatter. The current validator does not enforce the two evidence claims or authenticate a user study. Describe missing evidence as a finding, not as a machine-verified pass.

## Risk/usability interface

Start with the use specification and tasks. Feed foreseeable use errors and hazard-related scenarios from `usability` to the risk analysis before architecture approval. Send control requirements back to the user interface specification. Formative findings refine the design and risk paths; summative findings feed residual use-related risk evaluation. Errors, close calls and difficulties are observations to analyse, not automatic proof of a new hazard or proof that the user is at fault. Record relevance, root-cause investigation, linked existing/new risk path or a justified non-safety conclusion.

Information for safety is not effective merely because it exists or a user says they read it. Establish what the intended user must perceive, understand and do, in which environment and time. Avoid crediting training or labelling twice for the same assumed behaviour. Human reviewers determine the appropriate evaluation and any disclosure of residual risk.

## Residual risk and feedback

Evaluate each residual risk against the approved plan, check risks created by controls (§7.5) and completeness of risk control (§7.6), then evaluate overall residual risk (§8). The aggregate evaluation is not an average of FMEA scores. Address interactions, uncertainty and the device's overall benefit-risk picture. For EU devices, apply the relevant MDR risk-reduction and benefit-risk requirements in addition to ISO criteria; clinical evaluation supplies the benefit evidence.

Before release, the assigned person reviews the plan's execution, overall residual-risk acceptability and arrangements for production/post-production information (§9); draft the `RMR` for approval. After release, route new safety information to risk review, problem resolution and controlled change (§10). A new use problem or control failure may invalidate an earlier effectiveness assumption even if no record hash changed.

See [worked-example.md](worked-example.md) for an intentionally incomplete fictional slice.

---
name: risk
description: "Use when identifying hazards, risks and controls."
metadata:
  group: regulated
  invocation: model
  role: "runs inside the chain"
  leading_word: "people accept risk"
  neighbours: [hazards-from-code, security-diligence, usability]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["ISO 14971:2019 4-10", "IEC 62304:2006+A1:2015 7", "EN ISO 14971:2019+A11:2021", "MDR Annex I 1", "MDR Annex I 2", "MDR Annex I 8", "IEC 62304:2006+A1:2015 4.3 d)"]
---

# Risk

Supports the risk management process by drafting hazards, risk estimates, controls and residual risk evaluations. Acceptability criteria and acceptance belong to people.

## When to use

- Identifying hazards or hazardous situations.
- Choosing or verifying a risk control.
- A software change might affect safety.

Not for:

- Reverse-engineering from code: use `hazards-from-code` first.

## Reads

The approved intended use and risk plan, use specification/task scenarios, HAZ and RC records, requirements/design, SOUP anomalies, security findings and relevant production feedback.

## Techniques and timing

Choose and justify the method against the approved plan; do not apply every technique by default. Read the relevant local guide before doing the analysis:

- [Technique selection and procedure](references/analysis-techniques.md).
- [Fictional worked example](references/worked-example.md).
- [Implementation, effectiveness and risk/usability handoff](references/control-evidence.md).

## Process

1. Read or write the risk management plan: scope, responsibilities, acceptability criteria, overall residual risk method, verification of controls, post-production information (ISO 14971 4.4). Acceptability criteria are set by a person. Where scales are stored as options, order them worst first with no default. *Done when:* The plan exists, or the gap is a finding and the skill stops.
2. Confirm the intended use and the reasonably foreseeable misuse are written down. *Done when:* Both exist or the gap is a finding.
3. Select hazard analysis, FMEA or a focused fault tree from the problem and available evidence; keep risk decisions human-owned. Read the local technique guide before choosing the method; record prerequisites, first/repeat timing, evidence, limitations and the human decision. These are selectable repository practices unless a cited obligation or approved plan requires more. *Done when:* Method selection and tailoring have a reason, an owner and evidence criteria.
4. Treat security as part of safety. Link security findings to the hazards they can cause. *Done when:* Each security finding is linked or marked unlinked.
5. Identify hazards (potential sources of harm), then each foreseeable event sequence, hazardous situation and possible harm, keeping them separate. Cover normal and fault conditions, foreseeable misuse and lifecycle phases. Take use specification, task/scenario and formative findings from `usability` early, then summative/validation and production feedback as available; include SOUP anomalies (62304 7.1.3). Preserve distinct situation/harm contexts for a shared hazard. *Done when:* Every risk path preserves hazard, sequence, situation and harm, with assumptions and early usability inputs.
6. Estimate and evaluate against the person-set criteria. Show unrated items as unrated, first. Do not assign a probability to a software failure itself: estimate the probability of harm given the failure, or, where it cannot be estimated, evaluate on severity alone. *Done when:* Every risk is estimated and evaluated, or shown as unrated.
7. Propose controls in the usual order: inherent design, protective measures, information for safety. Name the mechanism that enforces each control. A software control becomes a requirement with a class and a verification. A software item that implements a control keeps its system's safety class; a different class for it needs the documented decomposition and segregation rationale of IEC 62304 4.3 d) and e). *Done when:* Each control is an `RC` linked to a `HAZ`, a mechanism and an implementing record.
8. Verify each control's implementation and effectiveness as distinct claims (ISO 14971 7.2). Name criteria, method, applicable configuration, result/reference and open gap for each; one well-designed activity may support both with a stated rationale. Technical checks do not automatically establish user recognition/action; arrange appropriate evidence with `usability`, `verify` and `validation`. *Done when:* Both control claims have suitable observed evidence or explicit open gaps.
9. Review whether each control introduces a new hazard or changes another risk (ISO 14971 7.5), and whether risk control is complete for every hazardous situation (7.6). *Done when:* Both reviews are recorded.
10. Draft each residual-risk evaluation against the plan criteria (ISO 14971 7.3). If unacceptable, return to control-option analysis (7.1); where further control is impracticable, 7.4 permits an individual benefit-risk analysis with clinical evaluation supplying the benefit evidence. Without supporting evidence, modify the device/intended use and reanalyse, or the risk remains unacceptable. Do not replace this individual disposition with overall residual-risk evaluation (8). For a device on the EU market, do not stop at acceptability against the criteria: risks are reduced as far as possible without adversely affecting the benefit-risk ratio, and every known risk is weighed against the benefit (MDR Annex I 1, 2, 8; EN ISO 14971:2019+A11:2021 Annex Z). So draft the risk side of the benefit-risk analysis for the device as a whole, not only where a residual risk is unacceptable; the benefit side cites the clinical evaluation, which owns it, and stays a gap until it does. *Done when:* Overall residual risk is evaluated; for the EU, a benefit-risk analysis exists for the device and each risk shows why it cannot be reduced further.
11. Before release, draft the risk management review and report as an `RMR` record (sections: Plan, Overall residual risk, Benefit-risk, Production and post-production) and hand it to `/approve` (ISO 14971 9). After release, take production and post-production information back into the file (10). *Done when:* An `RMR` record exists and waits for `/approve`.

## AI/ML branch

Add model-specific hazards: out-of-distribution input, performance drift, subgroup performance, over-reliance. Tie each to a monitoring control.

## Lessons from practice

- Absence must never render as a favourable value.
- A rule that names no enforcement mechanism is prose. Put the mechanism in the record, and allow an explicit none.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Agent-accepted risk | A residual risk shows as accepted with no person's name. |
| Paper control | A control with no mechanism and no verification. |

## Refuses

- Choosing acceptability criteria. *Instead:* Propose and ask the risk owner.
- Recording a residual-risk acceptance. *Instead:* Draft it; a human records it with `/approve`.
- Estimating from memory of a similar device. *Instead:* Estimate from this device's records.
- Defaulting severity or probability to the lowest value, or sorting unrated items as low. *Instead:* Show unrated items as unrated, first.

## Writes

`HAZ`, `RC` and `RMR` drafts with controlled supporting analysis, method-selection reasons, and separate implementation/effectiveness evidence references. No acceptance is recorded by the agent. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every `HAZ` has hazard, sequence, hazardous situation and harm, and an estimate or `unrated`.
- Every risk has a control with its mechanism, or a reason none is practicable.
- Overall residual risk is evaluated, and for the EU the benefit-risk analysis for the device exists.
- Before release, the risk management review and report exist as an `RMR` record waiting for `/approve`.
- No acceptance is recorded by the agent.

## See also

- `hazards-from-code`, because it supplies candidates. It is typed-only: tell the user to run `/hazards-from-code`.
- `security-diligence`, because security findings link to hazards here. Load the `security-diligence` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `usability`, because early task/scenario inputs and control-effectiveness evidence flow both ways. Load the `usability` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

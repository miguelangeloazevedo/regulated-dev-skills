---
name: risk
description: "Use when identifying hazards, risks and controls."
metadata:
  group: regulated
  invocation: model
  role: "runs inside the chain"
  leading_word: "people accept risk"
  neighbours: [hazards-from-code, security-diligence]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
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

The intended use, `HAZ` and `RC` records, requirements, the change folder.

## Process

1. Read or write the risk management plan: scope, responsibilities, acceptability criteria, overall residual risk method, verification of controls, post-production information (ISO 14971 4.4). Acceptability criteria are set by a person. Where scales are stored as options, order them worst first with no default. *Done when:* The plan exists, or the gap is a finding and the skill stops.
2. Confirm the intended use and the reasonably foreseeable misuse are written down. *Done when:* Both exist or the gap is a finding.
3. Identify hazards (potential sources of harm), then for each the foreseeable sequence of events that leads to a hazardous situation, and the harm that can follow. Keep the four apart in the record. Include use errors from `validation` and anomalies in SOUP items from their published anomaly lists (62304 7.1.3). *Done when:* Each `HAZ` names the hazard, the sequence, the hazardous situation and the harm separately.
4. Estimate and evaluate against the person-set criteria. Show unrated items as unrated, first. Do not assign a probability to a software failure itself: estimate the probability of harm given the failure, or, where it cannot be estimated, evaluate on severity alone. *Done when:* Every risk is estimated and evaluated, or shown as unrated.
5. Propose controls in the usual order: inherent design, protective measures, information for safety. Name the mechanism that enforces each control. A software control becomes a requirement with a class and a verification. A software item that implements a control keeps its system's safety class; a different class for it needs the documented decomposition and segregation rationale of IEC 62304 4.3 d) and e). *Done when:* Each control is an `RC` linked to a `HAZ`, a mechanism and an implementing record.
6. Review whether each control introduces a new hazard or changes another risk (ISO 14971 7.5), and whether risk control is complete for every hazardous situation (7.6). *Done when:* Both reviews are recorded.
7. Draft the residual risk evaluation for each risk and the evaluation of overall residual risk (ISO 14971 7.3, 8). For a device on the EU market, do not stop at acceptability against the criteria: risks are reduced as far as possible without adversely affecting the benefit-risk ratio, and every known risk is weighed against the benefit (MDR Annex I 1, 2, 8; EN ISO 14971:2019+A11:2021 Annex Z). So draft the risk side of the benefit-risk analysis for the device as a whole, not only where a residual risk is unacceptable; the benefit side cites the clinical evaluation, which owns it, and stays a gap until it does. *Done when:* Overall residual risk is evaluated; for the EU, a benefit-risk analysis exists for the device and each risk shows why it cannot be reduced further.
8. Before release, draft the risk management review and report as an `RMR` record (sections: Plan, Overall residual risk, Benefit-risk, Production and post-production) and hand it to `/approve` (ISO 14971 9). After release, take production and post-production information back into the file (10). *Done when:* An `RMR` record exists and waits for `/approve`.
9. Treat security as part of safety. Link security findings to the hazards they can cause. *Done when:* Each security finding is linked or marked unlinked.

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

`HAZ` and `RC` records as drafts. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every `HAZ` has hazard, sequence, hazardous situation and harm, and an estimate or `unrated`.
- Every risk has a control with its mechanism, or a reason none is practicable.
- Overall residual risk is evaluated, and for the EU the benefit-risk analysis for the device exists.
- Before release, the risk management review and report exist as an `RMR` record waiting for `/approve`.
- No acceptance is recorded by the agent.

## See also

- `hazards-from-code`, because it supplies candidates. It is typed-only: tell the user to run `/hazards-from-code`.
- `security-diligence`, because security findings link to hazards here. Load the `security-diligence` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

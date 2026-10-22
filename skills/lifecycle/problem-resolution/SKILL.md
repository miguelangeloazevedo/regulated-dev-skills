---
name: problem-resolution
description: "Use when something is broken, flaky or reported wrong. Problem report to authorised disposition."
metadata:
  group: lifecycle
  invocation: model
  role: "standalone"
  leading_word: "tight loop"
  neighbours: [risk, impact]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 9", "ISO 14971:2019 10", "ISO 13485:2016 8.5", "ISO 13485:2016 8.2.2", "ISO 13485:2016 8.5.2", "ISO 13485:2016 8.5.3"]
---

# Problem resolution

Takes a problem from report to an authorised disposition: assess safety and interim protection, investigate with evidence, verify required changes or justify no software change, and hand off complaint/CAPA decisions. A green regression is not CAPA effectiveness or quality-event closure. Reportability and closure decisions belong to people.

## When to use

- A defect, a failing test, a field complaint or an anomaly in SOUP.
- A flaky or intermittent failure.

Not for:

- A change to intended behaviour, not a defect: use `impact` and `requirements`.

## Reads

The originating event and controlled complaint/nonconformity/CAPA references, affected configurations, observations/logs, code, changes, HAZ/RC records and earlier problems/actions.

## Techniques and timing

Choose and justify the method against the approved plan; do not apply every technique by default. Read the relevant local guide before doing the analysis:

- [Intake, investigation, action and effectiveness handoff](references/quality-event-handoff.md).
- [Fictional engineering/CAPA boundary example](references/worked-example.md).

## Process

1. Write the problem report: what was observed, where, when the organisation became aware of it, the type, the scope and the criticality (62304 9.1). *Done when:* A report exists with awareness date, type, scope and criticality.
2. Assess safety relevance with `risk` straight away, whether or not the problem can be reproduced: does it relate to a hazard, a risk control, or a new hazardous situation? If the product is on the market, flag it now for the person who decides on vigilance reporting, with the awareness date; the clocks are in `maintenance`. *Done when:* Safety relevance is recorded, and a reportability flag is raised or ruled out by a person.
3. Assess interim protection before waiting for reproduction or root cause: identify affected/released products and configurations, containment or a justified none, responsible owner, evidence and reassessment trigger. Preserve originating event identity and complaint/nonconformity/CAPA references; unknown, not represented and confirmed absent are different. Urgent field actions stay with authorised QMS owners, not an agent deployment. *Done when:* The protection decision, affected scope, owner and unresolved information are recorded or escalated immediately.
4. Test causal hypotheses using recorded observations, comparison with unaffected configurations, and cause/effect or event/fault-tree analysis where useful. A five-whys discussion is a prompt, not proof of cause. Route use-related findings to `usability`, security findings to `security-diligence`, and changed control assumptions to `risk`, even when reproduction fails. *Done when:* Cause claims have evidence or remain hypotheses, and safety/security/use-analysis owners are notified.
5. Build a loop where feasible: one command that goes red on this problem, as the least privileged user who can reach it, in an authorised test environment. Make at most three recorded attempts. If it cannot be reproduced, retain observations and attempts, keep the report open and stop code fixing; continue safety assessment, protection and human QMS escalation. Non-reproduction alone never closes a field problem. *Done when:* The loop reproduces the problem consistently, or attempts and uncertainty remain recorded for the authorised disposition.
6. List where else the symptom could come from (a retry hiding a deterministic error, permissions that differ by user, a cache owned by another layer, timing on the target hardware), rank hypotheses and instrument the top one (9.2). *Done when:* The cause is found, or the hypotheses ruled out are recorded.
7. Obtain an authorised disposition based on the investigation and safety evaluation (62304 9.2): required software change, linked external action, or justified no software change. Record rationale and unresolved uncertainty; no action is not acceptable for an unresolved safety-relevant problem. For a software change, raise the required change request, follow the normal chain (9.4), and retain a regression test that failed before the fix. Never invent a red run to fit the record. *Done when:* The human disposition is recorded; required changes have authorisation and actual before/after verification, or the report remains open.
8. Verify the resolution, tell the relevant parties, and look for the same problem elsewhere and for trends across reports (9.3, 9.6, 9.7). *Done when:* Resolution is verified, parties told, and the trend check recorded.
9. Keep the engineering resolution separate from CAPA effectiveness and quality-event closure. For work routed to CAPA, hand off the approved action plan/reference, action owner, measurable effectiveness criterion, applicable scope and monitoring window; retain actual outcomes and review for adverse effects on compliance, safety and performance. The responsible people decide closure, further monitoring, rework or reopening. Preserve pending complaint/vigilance/risk actions even if the engineering fix passes. *Done when:* CAPA/complaint owners receive the evidence and open actions; pending effectiveness or closure is not reported as complete.

## AI/ML branch

If the problem is a wrong model output, record the input, the model version and whether the input was in range. A pattern of wrong outputs is a trend to analyse, not a single defect.

## Lessons from practice

- A symptom points at where it surfaced, not at its cause. Rule out the usual decoys first.
- Test as a non-admin. What works for you can fail for everyone else.
- Review recurrence over a defined scope and monitoring window; a lower count alone does not establish effectiveness.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Unsupported cause | A causal claim has neither observations nor a discriminating check. |
| Fixed by assertion | A changed file or green regression is presented as CAPA effectiveness or event closure. |

## Refuses

- Deciding whether a problem is reportable to an authority. *Instead:* Flag it for the person who decides.
- Deleting the red run. *Instead:* Keep it as evidence.
- Fixing on a theory that no loop or evidence supports. *Instead:* Build the loop, or record the evidence the theory rests on.

## Writes

A PRB with safety/protection assessment, investigation and disposition evidence; CR, regression case and TR records where a change is required; controlled complaint/CAPA references and pending effectiveness/closure handoffs. No independent complaint or CAPA record type is added. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Safety relevance, interim protection and affected scope have a recorded assessment or escalated gaps.
- The authorised disposition is explicit; a changed implementation has actual correction/regression evidence, and no-change rationale has human review.
- Complaint/CAPA effectiveness and closure handoffs have owners; pending work remains pending, not closed by a passing engineering test.

## See also

- `risk`, because it assesses safety relevance there. Load the `risk` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `impact`, because a fix that changes behaviour is priced there. It is typed-only: tell the user to run `/impact`.

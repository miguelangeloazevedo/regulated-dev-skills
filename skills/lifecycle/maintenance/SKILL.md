---
name: maintenance
description: "Use when released software gets feedback or problems. Includes SOUP monitoring and vigilance flags."
metadata:
  group: lifecycle
  invocation: model
  role: "periodic"
  leading_word: "the clock starts at release"
  neighbours: [problem-resolution, risk]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 6", "ISO 13485:2016 8.2.1", "ISO 13485:2016 8.2.2", "ISO 14971:2019 10", "MDR Art 83", "MDR Art 87", "21 CFR 803", "MDR Art 2(65)", "21 CFR 803.3"]
---

# Maintenance

Keeps released software safe: plans maintenance, takes in feedback and complaints, monitors SOUP, sends problems through `problem-resolution` and changes through the chain, and feeds post-market surveillance. Whether an event must be reported to an authority is always a person's decision.

## When to use

- The software has been released.
- Feedback, a complaint, a field problem or a SOUP advisory arrives.

Not for:

- A defect found during development: use `problem-resolution`.

## Reads

The maintenance plan in the `PLAN` record, feedback and complaint records, SOUP advisories, `HAZ` records, released baselines.

## Process

1. Write the maintenance plan: how feedback is received and evaluated, how problems and changes are handled, and how SOUP is monitored and updated (62304 6.1). *Done when:* The plan covers feedback, problems, changes and SOUP.
2. Document and evaluate each piece of feedback for whether it is a problem, and whether it affects safety (6.2.1; 13485 8.2.1, 8.2.2). *Done when:* Every feedback item has an evaluation.
3. Send problems through `problem-resolution` and changes through change requests and the chain (6.2.2 to 6.2.5, 6.3). *Done when:* Every problem and change is in its process.
4. Monitor SOUP: published anomaly lists and advisories for each SOUP item, evaluated against the hazards (6.1, 7.1.3). *Done when:* Each SOUP item has a monitoring source and a last-checked date.
5. Reopen risk, security and usability analysis for control failures, use errors/difficulties, vulnerable or unsupported dependencies and changed operating assumptions. Identify affected released configurations and the earlier effectiveness evidence whose applicability may no longer hold; use problem/change control for corrective work. *Done when:* Relevant feedback has an analysis owner, affected baseline scope and reopening decision.
6. Feed production and post-production information into the risk file and the post-market surveillance system (ISO 14971 10; MDR Art 83). *Done when:* Risk-relevant feedback is linked to the risk file.
7. Apply the tests before the clocks. EU: an incident is any malfunction or deterioration of a device on the market, including use error due to ergonomic features, any inadequacy in the information supplied, and any undesirable side-effect (Art 2(64)); it is serious if it directly or indirectly led, might have led or might lead to death, a serious deterioration of health or a serious public health threat (Art 2(65)). US: an MDR reportable event is one that reasonably suggests the device may have caused or contributed to a death or serious injury, or a malfunction that would be likely to cause or contribute to one if it recurred (803.3). Flag any event that may be a serious incident, or a planned field safety corrective action, for the person who decides on vigilance reporting, the day it is seen, with the awareness date. Do not decide. EU serious incidents (MDR Art 87(3) to (5)): report immediately once a causal relationship is established or reasonably possible, and no later than 15 days after awareness; 10 days for a death or an unanticipated serious deterioration in health; 2 days for a serious public health threat; when in doubt, report within the deadline (Art 87(6), (7)). EU field safety corrective actions: report before taking the action, without undue delay, except where urgent action is needed (Art 87(8)). US (21 CFR 803, manufacturers): 30 calendar days; 5 work days when remedial action is needed to prevent unreasonable risk of substantial harm, or FDA asks in writing. *Done when:* Each potential reportable event is flagged with its awareness date and the clock that applies to its kind.
8. Name, with an owner, what this skill does not cover and the QMS must: the post-market surveillance plan (MDR Annex III), the PMS report for class I (Art 85), the periodic safety update report for class IIa and above (Art 86), trend reporting (Art 88), post-market clinical follow-up (Annex XIV Part B), field safety notices, and US corrections and removals (21 CFR 806). *Done when:* Each item has a named owner, or the gap is a finding.
9. Link each problem that needs corrective or preventive action to the CAPA process (ISO 13485 8.5.2, 8.5.3) and each complaint to complaint handling (8.2.2). *Done when:* Problems and complaints carry their CAPA or complaint reference.
10. Preserve complaint/event identity and distinguish the software resolution from the originating QMS record. Record the complaint investigation or human-approved justification for not investigating, CAPA routing/disposition and pending effectiveness window with its owner. A PRB approval or passing fix does not close those external processes; reopen risk/control assumptions when recurrence challenges earlier effectiveness evidence. *Done when:* External process references, owners and unresolved monitoring/closure decisions remain visible.

## AI/ML branch

Monitor model performance in the field for drift and subgroup changes, and treat a retraining as a change request inside or outside the change control plan.

## Lessons from practice

- Flag a potentially reportable event the day it is seen, with the date of awareness.
- Give every SOUP item a monitoring source and a last-checked date.
- Evaluate every feedback item for safety before closing it.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Filed feedback | Complaints closed with no evaluation. |
| Silent SOUP | SOUP items with no monitoring date. |

## Refuses

- Deciding whether an event is reportable. *Instead:* Flag it, with the facts and the date, for the person who decides.
- Patching released software outside change control. *Instead:* Raise a change request.
- Closing a complaint without a safety evaluation. *Instead:* Evaluate it against the hazards first.

## Writes

The maintenance plan, feedback evaluations, SOUP monitoring entries, flags for vigilance decisions.

## Done when

- Every feedback item is evaluated.
- Every SOUP item is monitored with a date.
- Every potential reportable event is flagged to a person.

## See also

- `problem-resolution`, because problems found after release go through it. Load the `problem-resolution` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `risk`, because post-production information updates the risk file. Load the `risk` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

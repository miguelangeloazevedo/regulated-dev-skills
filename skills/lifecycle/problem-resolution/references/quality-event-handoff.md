# From software problem to quality-event disposition

This guide supports the software problem-resolution process. It does not replace complaint handling, nonconforming-product control, CAPA, vigilance or their authorised decision makers. Apply the depth the approved QMS procedures and plan require; not every defect needs a CAPA.

## Intake and interim protection

Preserve the originating event's identifier, source and awareness date. Distinguish feedback/complaint, observed nonconformity, software problem, investigation finding and requested change. They may refer to the same episode without becoming the same record. Carry controlled external references and affected product, version, deployment and lot/serial scope where relevant.

Assess safety and urgent protection before waiting for reproduction or root cause. Ask the responsible owner what containment or immediate correction is needed, why, for which affected configurations, with what evidence and when it will be reconsidered. A documented, authorised decision that none is necessary is different from an empty field. Unknown, not represented in this record, not applicable with justification, and confirmed absent must remain distinguishable. An unavailable containment field means ask the originating-event owner, not conclude that no protection exists. Field action is performed only through the authorised QMS process.

Keep observation separate from interpretation: what happened, what should have happened, impact, date, evidence location and affected/unaffected scope. Sensitive product/patient evidence stays in its approved controlled location, not copied into a public example or an unapproved model service.

## Investigation

Choose proportionate methods, not a compulsory checklist of techniques. Consider:

- **occurrence:** what mechanism produced the observed failure and which evidence supports or contradicts it?
- **escape:** why did prevention, detection or release controls fail to intercept it? Discovery evidence and a later correction test are different relations.
- **systemic scope:** is the same cause or control shared elsewhere, including other versions, interfaces, processes and suppliers? Search earlier events and actions, including recurrence after an earlier CAPA.

Compare unaffected configurations and test discriminating hypotheses. Cause/effect analysis, event/fault trees or five-whys may help; a completed worksheet or prior investigation summary is not causal proof. Separate supported causes, hypotheses, ruled-out alternatives and unanswered questions. Do not stop at operator error, or assume training attendance proves control effectiveness. Route use-related and security findings to their specialist owners and changed control assumptions to risk review.

Try a least-privilege reproduction where feasible in an authorised test environment. Keep failed attempts and field observations. If reproduction fails, stop speculative code fixing, not safety assessment, containment or escalation. The report stays open pending an authorised, evidence-backed disposition; a non-reproducible label alone is not a resolution.

## Action and effectiveness

The authorised disposition may require a software change, an externally controlled action, or justified no software change. Record the investigation, safety assessment, uncertainty and approving authority; no-action rationale cannot dispose of an unresolved safety-relevant problem. A linked external action remains pending until its actual result/disposition is known. Complaint non-investigation requires its own documented justification under the complaint procedure, not merely a no-change decision for the software.

Distinguish these claims:

| Claim | Evidence or decision |
| --- | --- |
| Containment/correction | Immediate protection or correction of the observed condition and its affected scope |
| Corrective action | Action addressing an established cause to prevent recurrence |
| Preventive action | Action addressing a potential nonconformity and its cause where applicable |
| Implementation verification | Approved actions were actually implemented in the intended configurations/processes |
| Effectiveness review | The action achieved the defined intended effect over the relevant scope and monitoring window; preventive-action effectiveness review is as appropriate under the procedure |
| Closure | Authorised human disposition of the event and remaining obligations |

For a software change use approved change control and keep actual before/after results, regression checks, tested version/configuration, date, tools and tester. Recheck risk/design assumptions and look for adverse effects or new problems. Do not fabricate a red run for an unrepeatable event.

For CAPA-routed work retain or reference the approved plan, cause-to-action rationale, action owner, due date, effectiveness criterion, monitoring window/sample rationale, configuration/process scope and evidence sources. Review for **no adverse effect** on regulatory compliance, device safety and performance. Record actual observations and limitations. An unelapsed monitoring window means pending effectiveness, not pass. Repeated events may require a revised plan or reopening of the earlier action and risk evaluation.

## Closure and representation limits

The engineering task may be verified while CAPA effectiveness, a complaint investigation or a reporting decision is still pending. Keep each owner and open action visible. The authorised people decide closure, continued monitoring, rework or when to reopen. Done/Canceled on a linked task is not implementation/effectiveness evidence, and cancellation needs a justified disposition. Check the evidence policy for every available closure route, not just the route first inspected.

Standalone has `PRB`, `FIND` and `CR`, not separate complaint, nonconformity, CAPA or action-task record types or an independently validated quality-event lifecycle. Retain these supporting details in existing record bodies and controlled external references. Do not invent statuses or frontmatter to simulate them. Record approval is document control, not quality-event closure. The validator does not evaluate causal validity, CAPA effectiveness, complaint completeness, reportability or external action completion. A missing external system or relation is an explicit mapping gap.

## Sources

- IEC 62304:2006+A1:2015 clauses 9.1-9.8: problem records, investigation, resolution, trends and verification provenance, with class applicability checked against the project's edition.
- ISO 13485:2016 clauses 8.2.2, 8.3, 8.5.2 and 8.5.3: separate complaint, nonconformity and corrective/preventive-action processes.
- ISO 14971:2019 clause 10: safety feedback and risk-file reassessment.

The worksheets and handoff prompts are repository practices supporting those processes, not additional standard clauses. See [worked-example.md](worked-example.md) for a fictional, incomplete handoff.

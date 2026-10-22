# Safety and design traceability

## Selection

Use an evidence graph for routine completeness review, a bidirectional impact walk for a change and a baseline-specific evidence reconciliation before release. These are repository techniques supporting the cited obligations. A trace matrix is a view, not a second source of truth or an acceptability decision.

Maintain two connected paths:

- Design: user need -> system requirement -> software requirement -> design -> verification case -> result; validation cases address user needs.
- Safety: hazard -> event sequence -> hazardous situation -> possible harm and risk evaluation -> control -> implementing requirement/design -> implementation and effectiveness evidence.

At software class B/C, also retain the IEC 62304 §7.3.3 path from hazardous situation to software item, specific software cause, control and verification. Software item/cause detail belongs in the controlled analysis/design references even when the UI shows a shorter chain. Class A does not acquire that clause's B/C obligation merely because this guide describes it.

A hazard is not a risk rating. Preserve each situation/harm path and its conditions even when several paths share a hazard or control. A backend may hold Hazard, Harm and a separate Safety Risk/context as distinct entities. A requirement can itself act as a risk control. Map these roles without forcing duplicate content or a one-to-one link cardinality.

## Prerequisites

Read scope, baseline, authorised record sources, semantic record types, configured relationship types/directions and applicable status/project filters. Establish read completeness: permissions, pagination, unavailable records, unconfigured external connections and failed tree/export fetches. Do not infer current tenant mappings from a source declaration or display label. For an unimplemented backend, state that the assessment cannot run there yet.

## Timing

Allocate stable identifiers when needs and hazards are drafted. Link controls as requirements/design are produced and cases as verification is planned. Update with results, approvals and changes. Review both chains at design boundaries, before change approval and before release; revisit after feedback or a changed assumption. Planning links early does not imply tests have already run.

## Procedure

1. Define the assessment scope and snapshot/baseline. Record included projects/record types, statuses, filters, unreadable/excluded records and retrieval completeness.
2. Map each relationship by source type, target type, semantic role, stored direction and inverse. A display name such as Requirement or Risk Control is not enough. A field showing links may be a filtered view of shared native links, not a separately stored relationship.
3. In standalone, author supported upward fields only: `derives_from`, `specifies`, `implements`, `mitigates`, `verifies`, `validates`, `result_of`. Preserve extra situation/harm/context detail as labelled paths in `HAZ` bodies or controlled referenced analyses; no separate Safety Risk or Harm record type ships. The validator does not parse those path semantics. Do not pretend that a lossy backend conversion preserves them.
4. Run the installed validator with the project paths and keep its output unedited. Separate its literal report from the additional human-reviewed safety-path assessment. In a different backend an implemented adapter must expose measured completeness and mapping; there is no Jira adapter in this release.
5. Review missing parents, missing control requirements, controls without cases, orphaned safety entities and results without usable provenance. Preserve many-to-many links and report shared controls/dependencies. Follow a link from both ends before writing or claiming it is correct.
6. Report each coverage dimension separately using the table below. A configured matrix can flag missing direct children but cannot establish a passing result, current baseline or control effectiveness merely by showing a Test column.
7. For a change, walk dependants and dependencies to closure with a visited set; retain paths/reasons, deduplicate identities and record cycles. Stop and label partial if any frontier cannot be read. This is an assessment procedure, not a claim that the current CLI performs it. The current CLI's suspect-approval check examines immediate linked parents, not recursive semantic change impact. Use a reviewed graph export/tool when available; otherwise list affected paths and do not invent traversal counts.
8. Reconcile exports against the requested roots and records. Count attempted, returned, failed, filtered and unreadable items where the backend exposes them. A successful export or absence of rows does not prove a complete assessment.

### Coverage dimensions and gaps

| Dimension | Evidence needed | Honest incomplete state |
| --- | --- | --- |
| Assessable scope | Configured mappings, complete retrieval, known permissions/filters | Unknown or partial, not zero gaps |
| Structural association | Correct endpoint types and direction, required paths present | Missing link or orphan, within stated scope |
| Approval freshness | Current content binding and reviewed dependencies | Stale, suspect or unapproved |
| Planned verification | Suitable case/criterion linked to the claim | Case absent or adequacy not reviewed |
| Execution and outcome | Actual run/inspection/analysis and observed result | Not run, blocked, failed or inaccessible evidence |
| Tested configuration | Exact applicable baseline/data/tools and results | Baseline mismatch or applicability not established |
| Control effectiveness | Evidence supports the risk-reduction claim | Implementation-only evidence or unresolved effectiveness |

A missing Test connection means coverage cannot be assessed through that hop. It is not the same as an assessed requirement with no tests. Likewise an orphan list can exclude inactive hazards or inaccessible projects; it is not automatically the whole risk file.

### Trace-review worksheet

Record scope/baseline and retrieval limits; source and target identifiers/types; relationship/direction and path; each coverage dimension; affected dependencies; gap category, owner and decision reference. Compute counts from a named tool/export and disclose denominator/scope. Do not hand-enter plausible coverage figures or create a parent simply to close a gap.

## Evidence

Use supported link fields and controlled assessment reports, with stable references to additional hazard/situation/harm paths. Tests, approvals, baseline and effectiveness each retain their own evidence. In standalone, `verified` during development means a passing linked result exists on some revision; only the baseline check ties results to the selected release revision. Even that structural check does not establish semantic adequacy. See [worked-example.md](worked-example.md) and [example.json](example.json).

## Limitations

The standalone schema has no independent Harm or Safety Risk entity and no machine-checked context-path mapping. Jira/backend conceptual mappings are not a working integration. No tool result here authenticates approvals or proves clinical correctness. Do not promise that source-level coverage warnings match a live site's saved configuration or that a complete-looking tree is a release verdict.

## Human decisions

Product/risk owners confirm intent, situation/harm paths and control adequacy. Verification/usability owners judge evidence fitness. QA/RA approves dispositions and release readiness. The agent maintains links and reports measured findings; it cannot declare risk accepted or silently repair missing meaning.

## Sources

- ISO 14971:2019 §4.5 (risk-file traceability) and §§5-8 (analysis, control and residual risk).
- IEC 62304:2006+A1:2015 §§5.2, 5.6-5.7 and 7.3.3, subject to class applicability.
- ISO 13485:2016 §§7.3.3, 7.3.6-7.3.7, 7.3.9-7.3.10.
- Backend-specific mapping must be verified against the configured implementation and read back on the target before it is represented as measured support. This worksheet adds repository practice, not a new standard clause.

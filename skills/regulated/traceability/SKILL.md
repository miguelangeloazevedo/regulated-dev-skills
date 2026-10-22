---
name: traceability
description: "Use when linking needs, requirements, specs and tests."
metadata:
  group: regulated
  invocation: model
  role: "runs inside the chain"
  leading_word: "computed, not typed"
  neighbours: [requirements, impact, risk]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 5.2", "ISO 13485:2016 7.3.3", "ISO 14971:2019 4.5", "IEC 62304:2006+A1:2015 7.3.3"]
---

# Traceability

Keeps design and safety traceability intact: needs to evidence, and hazard/situation/harm contexts through controls to their implementing requirements and evidence. Coverage is measured within stated scope, never inferred from links alone.

## When to use

- Adding, changing or linking records.
- Asked how much of the chain is covered.

Not for:

- Reading code to propose records: use `design-inputs-from-code` first.

## Reads

All scoped records and safety-path analyses; baseline and results; link semantics/directions; backend configuration, filters, permissions and retrieval limits.

## Techniques and timing

Choose and justify the method against the approved plan; do not apply every technique by default. Read the relevant local guide before doing the analysis:

- [Technique selection and procedure](references/chain-and-coverage.md).
- [Fictional worked example](references/worked-example.md).

## Process

1. When reading links from a backend, classify each by the types of the records at both ends, never by the link's display name. *Done when:* Every link is classed by its end types.
2. Review both the design chain and situation/harm/control paths; separate configured scope, links, freshness, execution and effectiveness. Read the local technique guide before choosing the method; record prerequisites, first/repeat timing, evidence, limitations and the human decision. These are selectable repository practices unless a cited obligation or approved plan requires more. *Done when:* Method selection and tailoring have a reason, an owner and evidence criteria.
3. Map distinct hazard, situation/harm and risk-evaluation contexts to controls, implementing requirements/design and evidence alongside the need-to-test chain. Preserve many-to-many relationships. A backend may represent a control as a Requirement and safety context/Harm as separate entities; standalone retains such context in HAZ bodies or controlled analyses, not new unsupported record types. *Done when:* The semantic mapping preserves each path and states any representation or adapter gap.
4. Run `python3 tools/rds/validate.py records <artefacts_dir> --roles <roles_file> --project <block file> --report` using the paths in the project block (`artefacts_dir`, `roles_file`, and the file that holds the block) and read `verified`, `linked_but_unverified`, `without_verification`, `software_requirements_with_several_parents`, `stale_approvals` and `suspect_approvals` from it. Never compute coverage by hand. During development `verified` means a passing result exists on some revision; only `--release --baseline` ties results to the baseline. Say which one a report is. Paste the validator's output unedited into the report, above any summary, so a reader can check the summary against it. *Done when:* Coverage numbers in the output come from the report.
5. Write links in the upward direction only. Read each link back from the far end to confirm it. *Done when:* The validator's computed inverse matches your intent.
6. Run the validator and inspect the orphan, multiple-parent and uncovered lists. Several valid parents are not an error; review their meaning and preserve legitimate many-to-many derivation. *Done when:* Gaps and legitimate shared-parent relationships are separately reported.
7. Report gaps as findings. Never invent a plausible parent to close one. *Done when:* Each gap is a finding with an owner.
8. Any count written in prose carries a marker naming its owner. *Done when:* The validator recomputes every marker.
9. Review assessable scope, association, freshness, actual outcome, tested baseline and effectiveness separately. Unconfigured test connections, permissions, filtering, pagination and partial fetches create unknown/partial scope, not proof of zero gaps. The current validator checks immediate-parent suspicion, not complete transitive impact or semantic control effectiveness; label supplementary assessment separately. *Done when:* The report exposes configuration/retrieval limits and evidence gaps without overstating validator capability.
10. Report the count of gaps found and closed this run alongside coverage, so a sudden perfect score is visible as a change. *Done when:* The report shows gaps found and closed.

## Lessons from practice

- Link names can lie. Classify by what is at each end.
- A specification with no requirement is a finding, not a gap to close with an invented parent.
- Any helper that takes two keys and a type is the shape of the inverted-link bug. Encode direction in the call, and verify it from the far end.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Perfect matrix | Coverage jumps to 100% in one run with no new tests. |
| Backwards link | A software requirement shows as the parent of its system requirement. |

## Refuses

- Closing a gap with a made-up parent. *Instead:* Record the gap.
- A count quoted from a document. *Instead:* Read it from the validator.
- Any helper that takes two record ids and a link kind without naming which end is the source. *Instead:* Name the source explicitly, write, then read the link back from the target.

## Writes

Link fields on records; findings. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every software requirement derives from at least one system requirement.
- Requirements with several parents are reported, not hidden.
- Every requirement has a verification or a typed `BLOCKED(timing)` criterion.
- Counts are computed.

## See also

- `requirements`, because it writes the records traceability links. Load the `requirements` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `impact`, because it walks the same graph. It is typed-only: tell the user to run `/impact`.
- `risk`, because the safety chain preserves situation/harm contexts. Load the `risk` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

---
name: status
description: "Where are we: records, stale evidence, open gates, evidence level."
disable-model-invocation: true
metadata:
  group: gates
  invocation: typed
  role: "standalone"
  leading_word: "measured, not remembered"
  neighbours: [setup, design-review]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 8.1.3"]
---

# Status

Reads the project and reports where it stands, from files, not from the conversation.

Typed commands provide invocation control, not an operating-system permission boundary. An instruction or editable approval field does not establish host-enforced authority.

Run this only when a person types `/status`. If you reached this skill on your own, stop and ask the user to type the command.

## Reads

The project block, records, change folders, test results.

## Process

1. Report each assurance property as declared, instruction_observed, host_observed, failed, unsupported, unassessed or stale, with its scope and evidence. Keep host-token probes distinct from actual agent/harness runs and independent regulatory review distinct from structural tests. *Done when:* Missing measurements and pending human decisions are explicit, not green defaults.
2. Run `python3 tools/rds/validate.py records <artefacts_dir> --roles <roles_file> --project <block file> --report` using the paths in the project block (`artefacts_dir`, `roles_file`, and the file that holds the block), and report its counts as they are. *Done when:* The validator output is reported, with its exit code.
3. If a baseline exists, report findings as inherited or introduced since the baseline. *Done when:* Each finding is classed, or no baseline exists.
4. Also run the same command with `--release` and report its blockers separately, labelled as what would stop a release today. *Done when:* The report shows development errors and release blockers apart.
5. Report the outcome of `intake` per module (device, not a device, part of another product, not decided) and the safety class per software system, showing not decided as not decided. *Done when:* Every module and system appears, undecided ones first.
6. Report the evidence level the declared controls actually support, and which properties are present. *Done when:* Both are stated.
7. Report records by status, stale approvals, `BLOCKED` criteria by kind, and verifier kinds used. *Done when:* Each number comes from the validator.
8. Report additional evidence dimensions separately from the literal validator output: assessable scope, test association, actual execution/outcome, configuration applicability and control effectiveness. Mark unsupported backend mappings or incomplete retrieval unknown/partial. Do not present these human-reviewed assessments as extra validator fields. *Done when:* The report distinguishes machine output, additional reviewed findings and unknown areas.
9. Report open gates with their age against the 3 and 14 day marks. *Done when:* Each open gate has an age.
10. Stamp the report with the commit and the time of the validator run it came from. *Done when:* The report names its commit and time.

## Lessons from practice

- Absence must never render as a favourable value. Not zero, not a tick, not a percentage of nothing.
- Every count is measured now or labelled with when it was measured. A figure carried forward is a transcription.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Stale certainty | Status quotes a count the validator no longer produces. |
| Empty green | A section shows complete because it has no items. |

## Refuses

- Reporting from memory. *Instead:* Run the validator and read the files.
- Showing a percentage over an empty set, or a pass for a check that did not run. *Instead:* Write `none` or `not run` and say what would produce a number.

## Writes

Nothing.

## Done when

- Every number is traceable to a validator run.

## See also

- `setup`, because status measures what setup declared. It is typed-only: tell the user to run `/setup`.
- `design-review`, because a review pack starts from a fresh status. Load the `design-review` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

---
name: hazards-from-code
description: "Propose hazard candidates from an existing codebase."
disable-model-invocation: true
argument-hint: "<path>"
metadata:
  group: extraction
  invocation: typed
  role: "chain step"
  leading_word: "hazard candidates"
  neighbours: [risk, intake]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["ISO 14971:2019 5", "IEC 62304:2006+A1:2015 7.1"]
---

# Hazards from code

Finds places where code can affect a person's care and proposes hazard candidates. Hazard analysis needs clinical context this skill does not have, so the output is input to a human-led session, never a result.

Run this only when a person types `/hazards-from-code`. If you reached this skill on your own, stop and ask the user to type the command.

## Reads

The code, the intended use statement if one exists, existing hazard records.

## Process

1. Read the intended use and the outcome from the `CLS` record. If there is none, tell the user to run `/intake` first, or state that the scan runs without one and every result is weaker for it. Hazards are worth finding in software that is not a device too; say which applies. *Done when:* The intended use and outcome are named, or their absence is stated.
2. Pin the scan as in `design-inputs-from-code`. *Done when:* The coverage header exists.
3. Find where output reaches a care decision, a device actuator or a stored clinical record, and where fallback and degraded behaviour are decided: calculations, thresholds, alarms, unit conversion, time handling, data writes, parsing of clinical data. Search with the agent's file search (for example `rg` for thresholds, alarm, unit and dose names) and open each hit; list the search terms used. *Done when:* Each location has an anchor.
4. For each, propose four things kept apart: the hazard (potential source of harm), the foreseeable sequence of events, the hazardous situation it leads to, and a candidate harm, with the failure mode in the code. Mark all `proposed`. *Done when:* Each candidate names hazard, sequence, hazardous situation and harm separately.
5. Cross-reference existing `HAZ` records: matched, new, unmapped. *Done when:* Each candidate has one of the three.
6. Hand candidates to the broader `risk` analysis, which also covers normal operation, use-related paths and external/lifecycle conditions not visible in code. Preserve distinct situation/harm paths; a code failure-mode inventory or FMEA is not a complete risk file. *Done when:* The risk handoff states path context and the limits of code-only coverage.
7. Write a ranked list of questions on severity, probability and clinical context into the change's `decision.md` for the owner. *Done when:* The list exists.
8. Head the output with the files read, the paths not read and a coverage figure (files read over files in scope). Draw no complete or ready conclusion about anything outside what was read. *Done when:* The output starts with the read list, the unread paths and the coverage figure.

## AI/ML branch

Include model-specific failure modes as candidates: out-of-distribution input, drift, subgroup performance, over-reliance by the user.

## Lessons from practice

- A failure that reports success is worse than one that reports failure. Absence of an error is not evidence of correctness.
- Cache the client, never the tenant's data. Shared state is how one person's record reaches another.
- Absence must never render as a favourable value. An unrated hazard is not a minor hazard.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Severity by guess | The output carries severities nobody with clinical context assigned. |

## Refuses

- Assigning severity, probability or acceptability. *Instead:* Write the question and name the role that decides.
- Calling the list complete. *Instead:* State the coverage and exclusions.
- Analysing non-software hazards. *Instead:* Name them as out of scope for this skill.
- Sorting or presenting unrated candidates as low severity. *Instead:* List them as unrated, ahead of rated ones, until a person rates them.

## Writes

Candidate records, a coverage section, a framing statement, owner questions. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every candidate is `proposed`.
- The framing statement is present: candidates inferred from code structure, to be dispositioned by people with clinical context.

## See also

- `risk`, because it takes the candidates into the risk process. Load the `risk` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `intake`, because it fixes the intended use the scan is scoped to. It is typed-only: tell the user to run `/intake`.

---
name: design-inputs-from-code
description: "Propose design input candidates from an existing codebase."
disable-model-invocation: true
argument-hint: "<path>"
metadata:
  group: extraction
  invocation: typed
  role: "chain step"
  leading_word: "candidates, not conclusions"
  neighbours: [gap-assessment, requirements]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 5.2", "ISO 13485:2016 7.3.3"]
---

# Design inputs from code

Reads existing code and proposes design input candidates for a human to accept. It never fills rationale, safety class or the user need as fact.

Run this only when a person types `/design-inputs-from-code`. If you reached this skill on your own, stop and ask the user to type the command.

## Reads

The code, tests, API schemas, configuration, schema files, user-facing strings, history and tickets; existing records.

## Process

1. Pin the scan: the commit, the paths in scope, the paths excluded. *Done when:* The coverage header exists.
2. Read the sources in order of how well they show intent: tests, API schemas, configuration and flags, database schema, user-facing strings, code, history and tickets. *Done when:* Each source type is marked read, absent or unreadable.
3. Before proposing any enumerated set (states, roles, units, limits), search for an existing definition in code, schema or tests and cite it. *Done when:* Each set is cited to a source, or marked as not found.
4. Propose one candidate per distinct behaviour with an anchor, an anchor hash and the sources that agree. *Done when:* Every candidate has an anchor and at least one source.
5. Where a value is shown to users, record both the stored value and the display label, and the mapping between them. *Done when:* Every user-visible value has both forms or is marked identical.
6. For each candidate, compare at least two representations (for example the schema and the tests) and record where one has items the other lacks. *Done when:* Each candidate lists its agreeing sources and any gap between them.
7. Record disagreements between sources as findings. *Done when:* Each disagreement names both sources.
8. Reconcile with existing records: unchanged, changed, new, removed. *Done when:* No identifier was renumbered.
9. Write candidate records as `proposed` and a ranked list of questions for the owner. Put the questions in the change's `decision.md` for the owner. *Done when:* Records and questions exist.
10. Code shows what the software does, not what it was meant to do. Before any candidate becomes a requirement, the product owner confirms the intended behaviour, and each disagreement between code and intent becomes a `FIND`. *Done when:* Every promoted candidate names who confirmed its intent.
11. Head the output with the files read, the paths not read and a coverage figure (files read over files in scope). Draw no complete or ready conclusion about anything outside what was read. *Done when:* The output starts with the read list, the unread paths and the coverage figure.
12. Feed confirmed candidates into requirements and technique planning; attach observed boundaries, decision/state logic and interface assumptions as evidence anchors. Do not infer intended use or adequate verification merely from existing tests or code structure. *Done when:* Candidates distinguish observed behaviour, proposed intent and unverified test adequacy.

## AI/ML branch

Also propose candidates for model inputs and outputs, thresholds, training and evaluation data sources, retraining triggers and any human override.

## Lessons from practice

- Read the source that already has the set before inventing one. Invented values rarely survive contact with the real list.
- A partial set looks complete from the inside. Compare two representations to find what is missing.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Requirements from function names | Candidates read like a list of methods, not like behaviour a user could observe. |
| Complete by assertion | No coverage section, so nobody can tell what was not read. |

## Refuses

- Filling rationale, safety class or a user need as fact. *Instead:* Write the question for the owner.
- Renumbering between runs. *Instead:* Reconcile on the anchor.
- Presenting the output as a complete requirements set. *Instead:* State the coverage and what the method cannot see.

## Writes

Candidate records, the coverage section, the owner question list. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Coverage is stated.
- Every candidate is anchored and `proposed`.
- No human-owned field is filled.

## See also

- `gap-assessment`, because it compares the candidates with what the chain needs. Load the `gap-assessment` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `requirements`, because it writes the accepted candidates up as records. Load the `requirements` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

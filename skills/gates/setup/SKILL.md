---
name: setup
description: "Set up the project block: backend, evidence level, roles, artefacts."
disable-model-invocation: true
metadata:
  group: gates
  invocation: typed
  role: "run-once setup"
  leading_word: "measured controls"
  neighbours: [intake, status]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["ISO 13485:2016 4.1.6"]
---

# Setup

Writes the project block and the few files the other skills need. It asks four questions about tooling and records the answers; it does not decide them. What the product is belongs to `intake`.

Run this only when a person types `/setup`. If you reached this skill on your own, stop and ask the user to type the command.

## Reads

`AGENTS.md` or `CLAUDE.md`, the repository remote and any readable branch protection settings, an existing roles file, an existing records directory.

## Process

1. On an existing repository, run the validator once before writing anything and save the output as the baseline. *Done when:* A baseline file exists, or the repository was empty.
2. Look first. Find an existing block, roles file and records directory. *Done when:* You can say what exists and what is missing.
3. Confirm the use of an AI agent on this product is approved under your QMS: the tool, the model and its version, where code and records are processed, and how agent output is reviewed. Ask the QA/RA owner whether the agent counts as software used in the QMS that must be validated for its intended use (ISO 13485 4.1.6) or as a development tool controlled another way; the agent never makes that decision. Record the answer, who gave it, and the validation reference: intended use, pinned tool and model versions, how output is reviewed, what triggers revalidation. A validation still in progress is recorded as open; work may start, and `release` stops until it is complete. Record the approval reference for agent use, or stop. Fill [AGENT-VALIDATION-TEMPLATE.md](AGENT-VALIDATION-TEMPLATE.md) or point to your own equivalent. *Done when:* An approval reference for agent use and the QA/RA owner's answer are recorded, or setup stops.
4. Where the host exposes them, read the controls behind the chosen level (branch protection, required reviewers, signed commits) and compare them with the answer. *Done when:* Each control is measured, not measurable, or contradicted, and contradictions are shown.
5. Ask the four items one at a time, recommended answer first: backend (only `standalone` is implemented in this version, so offer only it), evidence level, roles file, where artefacts live. *Done when:* All four have an answer or an explicit "ask later".
6. State in one line what the chosen evidence level proves and what it does not. *Done when:* The user has read it.
7. Write the block, a roles file skeleton and the artefacts directory skeleton. Create only what the answers need. *Done when:* The validator passes on the result.
8. Copy the validator (`scripts/validate.py` and `scripts/rds_yaml.py` and `scripts/RECORDS.md`, the record shapes, from the `scripts/` folder next to this `SKILL.md`) into the project at `tools/rds/`, so every other skill can run it. It needs only Python 3.9 or later. *Done when:* `python3 tools/rds/validate.py project AGENTS.md` runs in the project.
9. Print the block, then tell the user to run `/intake` to classify the product. *Done when:* The user has the block and the next step.

## Lessons from practice

- Verify against the instance, never against the configuration you wrote. A setting you asked for and a setting the host enforces are different facts.
- Capture the state before you touch it. Without a baseline nobody can tell an introduced finding from an inherited one, and `not run` is never a pass.
- An id is an observation about one instance on one date, not a setting. Resolve by name each time.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Declared, not measured | The block says level 1 but the default branch accepts direct pushes. |
| Inherited noise | The first validator run after setup reports dozens of findings and nobody can say which are new. |

## Refuses

- Choosing the evidence level for the user. *Instead:* Offer a recommendation and ask.
- Declaring a level the controls do not support. *Instead:* State the highest level the declared controls support.
- Writing an id from another instance or from documentation into the project block. *Instead:* Record names; adapters resolve them on the target instance at use time.

## Writes

The project block, a roles file skeleton, the artefacts directory.

## Done when

- The block validates.
- The roles file validates.
- The user confirmed each of the four items.

## See also

- `intake`, because it classifies the product once the tooling is set. It is typed-only: tell the user to run `/intake`.
- `status`, because it reports what setup declared, measured again. It is typed-only: tell the user to run `/status`.

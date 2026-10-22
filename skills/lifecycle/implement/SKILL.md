---
name: implement
description: "Use when building a software unit from its specification."
metadata:
  group: lifecycle
  invocation: model
  role: "chain step"
  leading_word: "no code without a specification"
  neighbours: [specifications, unit-verification]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 5.5.1"]
---

# Implement

Builds one software unit from its specification and hands it to unit verification. There is no code without a specification, and no specification without requirements.

## When to use

- A unit is specified and its blockers are done.

Not for:

- The unit has no specification: send it back to `specifications`.
- Something is broken: use `problem-resolution`.

## Reads

The unit's `SPEC`, the requirements it specifies, the project's coding standards, the project block.

## Process

1. Work only under a change the configuration rules allow: before the first release, the change classes the development plan sets; after it, an approved `CR` from `configuration-management`. If neither covers the work, stop and ask. *Done when:* The commit names the plan's change class or the approved `CR`.
2. Name the unit, its `SPEC` and the requirements behind it. If any is missing or not approved, stop. *Done when:* The unit, `SPEC` and requirement ids are named and approved.
3. Before editing, list the risk controls and interfaces the unit touches, from the links of its `SPEC`, and put the requirement and risk-control ids in the tests that verify them. *Done when:* The affected risk controls and interfaces are listed, and the tests carry the ids.
4. Use the approved test-design and analysis methods with `unit-verification`. Keep implementation evidence separate from claims about clinical benefit or user-facing control effectiveness. New interfaces, dependencies, privileges and failure modes return to risk/security/design review; do not widen the authorised unit silently. *Done when:* New assumptions and findings reach their owning skills before the unit is called complete.
5. Build the unit to the specification and the project's coding standards, named in the development plan, through `unit-verification`. *Done when:* The coding standard applied is named.
6. For every failure linked to a hazard or a risk control, make sure it reaches whoever must act on it, in the form the platform has: a message, an alarm, a log entry the operator sees. *Done when:* Every new failure has a path to the person who must act.
7. Build with the project's compiler and static analysis as the development plan sets them (for example warnings as errors for new code); a new warning is fixed or justified in the commit. *Done when:* The build and the static analysis are clean for the new code, or each remaining warning is justified.
8. Run the unit's tests and the affected suites. A test blocked by timing or environment is reported as blocked, never as passed. *Done when:* The run is recorded with its revision; blocked tests are listed.
9. Work in a loop: run the build and the tests through the shell, read the actual output, fix, and run again. Never report a step as passed from what you expect the output to be. Save each test run's command and full output to a log file with the change, and put its path and hash in the `TR`'s Result section, so the result can be checked against what actually ran. *Done when:* Every pass claimed has its command and output in the session or the evidence list.
10. Commit to the change's branch with the unit, specification and requirement ids in the message, and write the unit's evidence list: `SPEC` id, criteria, test ids, red run where required, revision, tool versions. *Done when:* The commit message carries the ids and the evidence list exists.

## Lessons from practice

- Generate the configuration and make the generator throw. A partial failure that returns normally is indistinguishable from success.
- A spinner or a silent retry is not an error message. Every failure the user must act on needs a path to them.
- Verify against the instance, never against the code.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Scope creep | The diff touches files no ticket mentions. |
| Quiet partial | A step reports done after half of it failed. |

## Refuses

- Widening the change beyond the unit. *Instead:* Record the extra work as a new unit in `specifications`.
- Editing an approved record directly. *Instead:* Open a change and let the approval go stale on purpose.
- A generator or apply step that logs a warning and continues, or returns normally after a partial failure. *Instead:* Raise, and make the caller handle it.

## Writes

Code, tests, a commit.

## Done when

- Every test is passed or blocked; blocked tests are listed, and a blocked risk-control test stops the unit.
- The commit cites unit, specification and requirements.
- No code exists without a specification.

## See also

- `specifications`, because each unit it builds is specified there. Load the `specifications` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `unit-verification`, because it builds test-first through it. Load the `unit-verification` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

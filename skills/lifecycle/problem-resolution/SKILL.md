---
name: problem-resolution
description: "Use when something is broken, flaky or reported wrong. Problem report to verified fix."
metadata:
  group: lifecycle
  invocation: model
  role: "standalone"
  leading_word: "tight loop"
  neighbours: [risk, impact]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["IEC 62304:2006+A1:2015 9", "ISO 14971:2019 10", "ISO 13485:2016 8.5"]
---

# Problem resolution

Takes a problem from report to verified fix: records it, builds a loop that reproduces it, assesses its safety relevance, raises a change request, fixes it, and checks the fix. It never decides whether a problem must be reported to an authority; it flags it for the person who does.

## When to use

- A defect, a failing test, a field complaint or an anomaly in SOUP.
- A flaky or intermittent failure.

Not for:

- A change to intended behaviour, not a defect: use `impact` and `requirements`.

## Reads

The report, logs, the code, recent changes, `HAZ` and `RC` records, earlier problem reports.

## Process

1. Write the problem report: what was observed, where, when the organisation became aware of it, the type, the scope and the criticality (62304 9.1). *Done when:* A report exists with awareness date, type, scope and criticality.
2. Assess safety relevance with `risk` straight away, whether or not the problem can be reproduced: does it relate to a hazard, a risk control, or a new hazardous situation? If the product is on the market, flag it now for the person who decides on vigilance reporting, with the awareness date; the clocks are in `maintenance`. *Done when:* Safety relevance is recorded, and a reportability flag is raised or ruled out by a person.
3. Build a loop: one command that goes red on this problem, as the least privileged user who can reach it. Make at most three recorded attempts. If it cannot be reproduced, record what was tried, keep the report open and stop; never close a field problem as not reproducible without a safety assessment. *Done when:* The loop goes red the same way twice, or the attempts are recorded and the report stays open.
4. List where else the symptom could come from (a retry hiding a deterministic error, permissions that differ by user, a cache owned by another layer, timing on the target hardware), rank hypotheses and instrument the top one (9.2). *Done when:* The cause is found, or the hypotheses ruled out are recorded.
5. Raise a change request and fix it through the normal chain (9.4). Add a regression test that failed before the fix. *Done when:* The regression test was red, then green.
6. Verify the resolution, tell the relevant parties, and look for the same problem elsewhere and for trends across reports (9.3, 9.6, 9.7). *Done when:* Resolution is verified, parties told, and the trend check recorded.

## AI/ML branch

If the problem is a wrong model output, record the input, the model version and whether the input was in range. A pattern of wrong outputs is a trend to analyse, not a single defect.

## Lessons from practice

- A symptom points at where it surfaced, not at its cause. Rule out the usual decoys first.
- Test as a non-admin. What works for you can fail for everyone else.
- Count problems by pattern across reports. A fix that worked shows up as a falling count.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Theory first | Hypotheses before any red loop exists. |
| Fixed by assertion | The problem is called fixed because the code changed. |

## Refuses

- Deciding whether a problem is reportable to an authority. *Instead:* Flag it for the person who decides.
- Deleting the red run. *Instead:* Keep it as evidence.
- Fixing on a theory that no loop or evidence supports. *Instead:* Build the loop, or record the evidence the theory rests on.

## Writes

A problem report, a change request, a regression test, `TR` records. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- The loop was red and is green.
- Safety relevance is recorded.
- The regression test fails without the fix.

## See also

- `risk`, because it assesses safety relevance there. Load the `risk` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `impact`, because a fix that changes behaviour is priced there. It is typed-only: tell the user to run `/impact`.

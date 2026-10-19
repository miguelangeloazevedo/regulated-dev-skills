---
name: impact
description: "Price a change: blast radius from the links, effort as a range."
disable-model-invocation: true
argument-hint: "<record-id>"
metadata:
  group: gates
  invocation: typed
  role: "standalone"
  leading_word: "blast radius"
  neighbours: [traceability, intake]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["MDCG 2019-11 rev.1", "MDR Annex IX 2.4", "MDR Annex IX 4.10", "21 CFR 807.81(a)(3)", "FDA: Deciding When to Submit a 510(k) for a Software Change to an Existing Device (2017)"]
---

# Impact

Prices a change before you commit to it. Counts come from the link graph, never from memory, and effort is a range with a stated confidence.

Run this only when a person types `/impact`. If you reached this skill on your own, stop and ask the user to type the command.

## Reads

The changed record, all records, the change folders.

## Process

1. Read the changed or proposed record. *Done when:* The record and the proposed change are in front of you.
2. Check whether the area already has a migration in flight: two link kinds or fields that encode the same thing, or records in both old and new shapes. *Done when:* In-flight migrations are named, or none was found.
3. Walk the links in both directions with the validator's computed inverse, ring by ring: requirements, specifications, tests, documents, baseline. *Done when:* Each ring has a count produced by the validator.
4. List the approvals that would become stale. *Done when:* The list is complete or marked partial.
5. Mark every affected item that is permanent once released: stored names and descriptions, option values and their order, identifiers other systems hold. *Done when:* Permanent items are a separate list.
6. Estimate effort per item as a range and say what it assumes. Get an independent second estimate if one is available. Label the estimate uncalibrated until estimates and actuals have been compared on at least two closed changes. *Done when:* Every estimate is a range with assumptions.
7. Present counts, range, confidence and a recommendation: accept, split or defer. *Done when:* The user can decide.
8. Check the change against the reclassification triggers in the `CLS` record. If one fires, tell the user to run `/intake` before anything else. *Done when:* Triggers are checked.
9. Ask the regulatory question for every change to released software, by route, and record the answer as a person's decision. EU: can it change qualification or class (MDCG 2019-11); for a device certified by a notified body, is it a change to the approved design or quality system the notified body must be told of before it is implemented (Annex IX 2.4, 4.10, or the equivalent in Annex X and XI); a self-certified class I device updates its own technical documentation. US, by the pathway in the `CLS` record: 510(k), is a new 510(k) needed (21 CFR 807.81(a)(3) and FDA's software change guidance); PMA, which PMA supplement or report applies (21 CFR 814.39); De Novo, treated like a 510(k) for later changes once granted; exempt, check the exemption's limits still hold. For any route, is the change inside an authorised predetermined change control plan? *Done when:* The regulatory answer is drafted for the route in the `CLS` record and waits for a person's decision.
10. Write the estimate into the change folder so it can be compared with the actual effort when the change closes. *Done when:* The estimate is saved with its assumptions.

## AI/ML branch

A change to model, training data or thresholds counts as a change to every requirement that depends on the model's performance. Say whether it needs a new submission or sits inside a predetermined change control plan; if unsure, say so.

## Lessons from practice

- Price permanence separately from effort. A small edit to a permanent string is a migration.
- Before calling two artefacts a contradiction, ask whether one is replacing the other. You complete a migration; you do not work around it.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Count from memory | The impact note says about twenty tests; the graph has thirty-one. |
| Point estimate | One number with no range and no assumptions. |

## Refuses

- Counting by hand. *Instead:* Run the validator and use its numbers.
- A single-point estimate. *Instead:* Give a range and the assumptions.
- Claiming accuracy it has not measured. *Instead:* Say the estimate is untested against past changes.

## Writes

An impact note in the change folder.

## Done when

- Counts equal the graph's node counts.
- The estimate is a range with assumptions.

## See also

- `traceability`, because it owns the links impact walks. Load the `traceability` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `intake`, because a change that fires a reclassification trigger goes back there. It is typed-only: tell the user to run `/intake`.

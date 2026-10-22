---
name: user-needs
description: "Use when writing or changing user needs. Need: who, what capability, why."
metadata:
  group: lifecycle
  invocation: model
  role: "chain step"
  leading_word: "who, what, why"
  neighbours: [intake, requirements, validation]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["ISO 13485:2016 7.3.3", "ISO 13485:2016 7.3.7", "IEC 62366-1:2015+A1:2020 5.1", "MDR Annex I"]
---

# User needs

Writes the user needs the design answers to: who must be able to do what, and why, within the intended purpose `intake` fixed. A need never names a mechanism, and every need says how it will be validated.

## When to use

- The product is classified and the needs are not written yet.
- A new intended use, user group or use environment appears.
- Requirements exist with no need above them.

Not for:

- The product is not classified: tell the user to run `/intake`.
- Turning needs into system behaviour: use `requirements`.

## Reads

The approved `CLS` record (intended purpose, users, patient population, use environment), the use specification if one exists, existing `UN` records, feedback and complaint records if the product is on the market.

## Process

1. Read the intended purpose, users, patient population and use environment from the approved `CLS` record. If it is not approved, stop. *Done when:* The scope of the needs is stated.
2. Hand intended users, environment, tasks and safety-related capabilities to `usability` and preliminary `risk` analysis now; involve `security-diligence` for assets and trust assumptions. Return uncertainties as questions, not a guessed design or class. *Done when:* Early use/risk/security inputs and unresolved assumptions have owners.
3. Write each need as a person, a capability and the reason: what someone must be able to do, and why. Name no field, screen, algorithm or technology. *Done when:* Every `UN` has a person, a capability and a why, and names no mechanism.
4. Give each need its validation method: how you will show, with intended users in the intended environment, that the finished product meets it. *Done when:* Every `UN` has a validation method.
5. Cover the use specification: each user group and use environment in the intended purpose has at least one need, or a recorded reason why not. *Done when:* No user group or environment is silently missing.
6. Mark each need `draft`. Hand open questions to the owner in the change's `decision.md`. *Done when:* Records validate and open questions are listed.

## AI/ML branch

Add needs for what the user must be able to understand about the model's output: its confidence, its limits, and what to do when it is wrong.

## Lessons from practice

- If a need names a field, a screen or a mechanism, it is a requirement wearing a need's clothes.
- Decide how each need will be validated when you write it, not after the build.
- Put the use specification and the needs side by side. A partial set looks complete from the inside.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Requirement in disguise | A need reads 'the screen shall show a red banner'. |
| Orphan rescue | Needs appear right after a traceability run, one per orphan requirement. |

## Refuses

- A need that names a field, a screen or a technology. *Instead:* Write the capability and the reason; the mechanism belongs in `requirements` or `specifications`.
- Inventing a need to give an orphan requirement a parent. *Instead:* Record the orphan as a finding and ask the owner whether the need exists.
- Writing needs outside the approved intended purpose. *Instead:* Send the change to `/intake` first.

## Writes

`UN` records. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every `UN` has a person, a capability, a why and a validation method.
- Every user group and use environment in the intended purpose is covered or excluded with a reason.

## See also

- `intake`, because it fixes the intended purpose the needs sit inside. It is typed-only: tell the user to run `/intake`.
- `requirements`, because it turns each need into system behaviour. Load the `requirements` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `validation`, because it shows each need is met with intended users. Load the `validation` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

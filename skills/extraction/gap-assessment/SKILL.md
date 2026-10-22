---
name: gap-assessment
description: "Use when an existing codebase lacks records."
metadata:
  group: extraction
  invocation: model
  role: "chain step"
  leading_word: "reuse by hash"
  neighbours: [design-inputs-from-code, requirements]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 4.4", "ISO 13485:2016 7.3"]
---

# Gap assessment

Assesses existing software against the chain. If it was lawfully placed on the market and is still marketed, it is legacy software and follows the IEC 62304 4.4 route; if not, the gaps are closed by applying clauses 5 to 9 before release.

## When to use

- Software already exists and the records do not.
- Code or records exist but the chain does not.

Not for:

- Starting from nothing: use `requirements`.

## Reads

The code, any existing records, the change folder.

## Process

1. Propose the route; a person decides it, because it rests on whether the software was lawfully placed on the market. Software lawfully placed on the market and still marketed without enough objective evidence of development under the standard is legacy software (62304 3.36) and may follow 4.4. Anything else, including unreleased code, follows clauses 5 to 9: the gaps are closed before release. Record the route as a `DEC` record that a person approves with `/approve`, because it changes which clauses apply to the whole project. *Done when:* The route is an approved `DEC` record with the market status that decides it.
2. For legacy software, assess feedback including post-production information about incidents and near incidents (4.4.2 a), and run risk management for continued use: how it sits in the device, whether its risk controls are still valid, the hazardous situations of continued use (4.4.2 b). *Done when:* Feedback and continued-use risk are assessed, or the route is clauses 5 to 9.
3. List what exists: records, tests, results, reviews, documents. For each disagreement found, ask whether it is a migration in flight before calling it an error. *Done when:* The inventory is written and each disagreement is classed as migration or error.
4. Compare. For legacy software, 4.4.3 compares the available deliverables with what requirements (5.2), architecture (5.3), system testing (5.7) and risk management (clause 7) call for at the software's class, and checks that existing risk controls appear in the software requirements. For other existing code, compare with the whole chain and the class obligations. Reuse evidence whose revision hash still matches and whose approval holds; mark the rest stale. Say whether each missing item is absent or only not found in what was read. Work one area at a time (requirements, architecture, system testing, risk management), in separate passes, each naming the files and records it read and what it did not read. Never conclude on an area from a pass that did not cover it. *Done when:* Each element is present, missing, not found or stale. Each area has its own pass with its read-list.
5. Assess method and evidence adequacy in addition to record presence: distinguish planned from executed cases, implementation from effectiveness, and complete scope from unreadable/unconfigured areas. Reused evidence requires applicable configuration/assumptions as well as a matching hash; do not invent missing historical runs. *Done when:* Each gap distinguishes structure, evidence, applicability and analysis scope.
6. Write the gap closure plan, prioritised by risk, with an owner per gap (4.4.4). For legacy software, write the rationale for continued use until the plan is done (4.4.5). State the conclusion against a fixed rubric: not ready (any content or scope gap in a risk control), conditionally ready (only timing gaps, each with a date), ready (no open gaps). Save the result with its commit. *Done when:* The plan, the rubric conclusion and, for legacy software, the rationale exist and name the commit.
7. Extracted candidates are untrusted until their owner confirms them one by one. The assessment cannot conclude on an area whose evidence is only extracted candidates; say what was confirmed, what was not, and what coverage the extraction had. *Done when:* Every candidate the conclusion relies on names who confirmed it, and the coverage is stated.

## Lessons from practice

- You complete a migration; you do not work around it.
- A detection that cannot see something must not claim it is not there.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Gaps closed by invention | Records appear that nobody can trace to a source. |

## Refuses

- Closing a gap by inventing the record. *Instead:* Record it as a gap.
- Reusing evidence for a changed revision. *Instead:* Mark it stale.
- Deciding that the software is legacy software. *Instead:* Propose the route with the market facts; a person decides.

## Writes

The gap list in the change folder.

## Done when

- Every gap has a type and an owner.
- Reused evidence is hash-matched.

## See also

- `design-inputs-from-code`, because it supplies candidates for missing records. It is typed-only: tell the user to run `/design-inputs-from-code`.
- `requirements`, because it writes the missing records. Load the `requirements` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

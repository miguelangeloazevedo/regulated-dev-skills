---
name: usability
description: "Use when specifying or evaluating the user interface. Runs IEC 62366-1 usability engineering."
metadata:
  group: lifecycle
  invocation: model
  role: "chain step"
  leading_word: "usability starts first"
  neighbours: [user-needs, risk, validation]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62366-1:2015+A1:2020 4, 5, Annex C", "MDR Annex I 5, 14.6, 22", "FDA: Applying Human Factors and Usability Engineering to Medical Devices (2016)"]
---

# Usability

Runs the usability engineering process of IEC 62366-1 from the start of development: use specification, safety-related user interface characteristics, hazard-related use scenarios, user interface specification, formative evaluation during design and summative evaluation at the end. It keeps the usability engineering file. People run the evaluation sessions; designers of the interface do not evaluate it.

## When to use

- User needs exist and the use specification is due, before architecture.
- The user interface is being designed or changed.
- A production-equivalent interface exists and summative evaluation is due.

Not for:

- Showing that the product meets its user needs overall: use `validation`, which takes the summative results from here.

## Reads

`UN` records, the `CLS` record, `HAZ` records, the `PLAN` record, the current user interface and its accompanying documentation.

## Process

1. Start with the use specification, before architecture: medical indication, patient population, part of the body, user profiles, use environment, operating principle (62366-1 5.1). *Done when:* A use specification exists before `specifications` writes the architecture.
2. For a user interface already in use and not developed under IEC 62366-1 (a user interface of unknown provenance), the unchanged parts may follow Annex C instead of 5.1 to 5.9; changed parts follow the full process (5.10). *Done when:* Each part of the interface is marked as full process or Annex C, with the reason.
3. Use task analysis to connect user goals, task sequence, potential use errors, hazardous situations and harm; feed this to `risk` before architecture approval. Return control requirements to the interface specification. Formative findings refine both design and risk analysis; summative evidence supports the specific effectiveness claims it actually addresses, not every technical control. *Done when:* Use/risk/control links exist from early development and are revisited with each relevant finding.
4. Identify user interface characteristics related to safety, potential use errors (task analysis where it helps), use-related hazards and hazardous situations, and the hazard-related use scenarios with their severity, linked to `HAZ` records (5.2 to 5.4). Select scenarios for summative evaluation, by severity (5.5). *Done when:* Every hazard-related use scenario is linked to a `HAZ` and the selection is recorded.
5. Write the user interface specification: testable requirements for the interface, including what is safety-related, and the accompanying documentation and training (5.6). Feed it into `requirements`. *Done when:* The user interface specification exists and its items appear as requirements.
6. Write the user interface evaluation plan: formative methods, what part of the interface and when; summative method per selected scenario with its rationale, participants representing each user group, environment, documentation and training as in real use, and how use errors, use difficulties and close calls are captured (5.7). *Done when:* The plan covers formative and summative evaluation.
7. During design, run formative evaluations and record findings as changes to the interface (5.8). *Done when:* Formative results are recorded and traced to changes.
8. On the final or production-equivalent interface, prepare the summative sessions and the validation protocol for user needs. People run them; designers of the interface do not evaluate it (5.9). *Done when:* The protocol names the baseline, the participants and the acceptance criteria.
9. For each language the device is placed on the market in, check the translated user interface text, labelling and instructions against the user interface specification, and include the language in the summative evaluation where a translation affects a hazard-related use scenario. *Done when:* Each market language has its check recorded.
10. For the US, plan the human factors validation to FDA's human factors guidance: identify the critical tasks, test with participants from each distinct user group, and prepare the human factors report for the submission. *Done when:* For a US submission, the critical tasks and the user groups tested are listed.
11. Analyse every use error and use difficulty from formative and summative sessions; find the root cause of those that could lead to a hazardous situation, and send each to `risk` as a new hazard or a link to an existing one (62366-1 5.9). *Done when:* Every relevant observation has an investigation and an existing/new risk-path link or a justified non-safety conclusion.

## AI/ML branch

Treat the model's output as part of the user interface: include in the scenarios what the user does with a wrong, uncertain or missing output.

## Lessons from practice

- Run formative evaluations while the design can still move.
- Assess the safety relevance of every observed use error; link the risk path or record why no new safety path is needed.
- Keep the usability engineering file as its own record; validation cites it.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Team evaluation | Participants are the developers and their colleagues. |
| Late start | The first usability record is a summative report. |

## Refuses

- Evaluating the interface with its own designers. *Instead:* Recruit representatives of each user group in the use specification.
- Starting usability at the end of development. *Instead:* Write the use specification before architecture; run formative evaluations while the design can move.
- Recording a session nobody ran. *Instead:* Prepare the protocol and the record; people run the session.

## Writes

The usability engineering file: use specification, user interface specification, evaluation plan, formative and summative records; hazard links in `HAZ` records. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- The use specification exists before architecture.
- Every hazard-related use scenario has a summative result or is listed as open.
- Every use-related observation is assessed for safety relevance and linked or justified.

## See also

- `user-needs`, because each need names its users. Load the `user-needs` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `risk`, because use errors become hazards there. Load the `risk` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `validation`, because takes the summative results. Load the `validation` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

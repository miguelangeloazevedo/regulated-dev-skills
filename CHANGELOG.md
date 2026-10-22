# Changelog

## 0.1.0-draft.8

- A first-change walkthrough uses the class A schedule example to draft an explicit empty-day message, inspect stale approvals and prepare a human-reviewed handoff.
- The walkthrough includes isolated practice commands, agent prompts, expected validator checkpoints and explicit boundaries between fictional records and real evidence.
- A regression test executes the walkthrough commands and checks its stale-approval and release-blocker checkpoints without changing the source fixture.

## 0.1.0-draft.7

- `design-review` leaves each participant's read-list blank for them to fill.
- `implement` works only under a change the configuration rules allow: the plan's change classes before the first release, an approved `CR` after it.
- `traceability` puts the validator's output unedited into its report, above the summary.

## 0.1.0-draft.6

- `validation` records the clinical evaluation report and revision behind each need that depends on clinical evidence.
- `implement` keeps each test run's command and output as a log file and puts its path and hash in the `TR`.
- `specifications`: at class B and C, a design that relies on a SOUP item waits for that item's requirements and anomaly evaluation (IEC 62304 5.3.3, 5.3.4, 7.1.3).
- `development-plan`: for software that is not a device, each activity's depth has a reason and the criterion QA/RA used to accept it.
- README notes the validator's test suite and the JSON report; the count-marker example in `spec/records.md` uses the supported keys.

## 0.1.0-draft.5

- `requirements`: the risk analysis is re-evaluated against the software requirements at every class (IEC 62304 5.2.4); risk controls become requirements at class B and C (5.2.3).
- `CLS` records carry `recheck_by`, the earliest re-check date of their dated sources; `--release` refuses a classification past it (RDS412).
- The validator warns during development when a class B or C SOUP item has no anomaly evaluation, instead of only at release (RDS414).
- `approve` names a concrete read-back for the host reference (for example `gh pr view`); `hazards-from-code` lists the search terms it used.
- `spec/backends.md`: shorter description of the backends.

## 0.1.0-draft.4

- README: shorter draft notice.

## 0.1.0-draft.3

- `setup` and `development-plan` ask the QA/RA owner whether the agent is software that must be validated under ISO 13485 4.1.6; the agent never decides it. A validation in progress lets work start.
- `release` stops while the agent toolchain validation is still open.
- README: a section on class A and software that is not a device, pointing to the smallest record set that passes the release gate.

## 0.1.0-draft.2

- Release is refused while any software system has no decided class, whether or not IEC 62304 is claimed; software that is not a device records `none`.
- `--release` ends by saying that passing is a structure check and that the `REL` record still needs approval by the people your QMS names.
- FLOWS names the US post-market reports next to the EU ones: medical device reports (21 CFR 803) and corrections and removals (21 CFR 806).
- README: the smallest path points to `usability` from the use specification and `validation` at the end.

## 0.1.0-draft.1

First public draft.

- 27 skills in four groups: gates, lifecycle, regulated and extraction.
- Record shapes, an approval model bound to content hashes, and a validator with a release gate (`tools/validate.py`).
- Two worked examples: a class B project that fails the release gate on real gaps, and a class A project that passes it.
- Every skill is a draft until a named person reviews it.

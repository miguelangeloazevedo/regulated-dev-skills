# Verification technique selection

## Selection

Plan tests against the claim while requirements and design are still being reviewed. Choose techniques by input domain, decisions, state and risk, not because every technique is universally required. ISTQB techniques are engineering guidance, not additional IEC 62304 clauses.

| Shape of behaviour | Technique | Concrete design action |
| --- | --- | --- |
| Classes of inputs/outputs | Equivalence partitioning | Identify valid and invalid classes; justify why one representative can stand for each |
| Ordered limits | Boundary-value analysis | Exercise the limit and adjacent representable values, respecting units, precision and inclusive/exclusive rules |
| Combinations of conditions | Decision tables | Enumerate feasible rules and actions; justify infeasible or merged cases |
| Stateful behaviour | State-transition testing | Define starting state, event, guards and action; cover required transitions and relevant forbidden ones |
| Protocol/interface failures | Negative and robustness cases | Exercise absent/malformed/late/duplicate/reordered messages and defined recovery |
| Safety-control failure | Controlled fault injection | Break the selected control/precondition and observe the required response, in a safe representative environment |
| Change propagation | Risk-based regression selection | Trace affected requirements/interfaces/controls, justify retained tests and omitted areas |

Property-based tests can exercise invariants over a justified domain; metamorphic tests can check justified relations when exact outputs are difficult to obtain. Neither replaces an independent clinical/numerical oracle or evidence that the asserted property is the right requirement. Structural coverage helps reveal untested code but does not prove correct requirements or adequate safety coverage. Select and document any coverage targets in the plan; no blanket MC/DC obligation is introduced here.

## Prerequisites

Read approved requirements/design and their revisions, risk/control claims, class and plan depth, integration order, test environment, oracle, acceptance criteria and independence arrangements. Identify fixtures and known limitations. Invalid/missing expected behaviour is a requirements gap, not permission to guess an expected result from the implementation.

## Timing

Design partitions, boundaries, decision/state cases and effectiveness methods alongside requirements/design. Builders use suitable techniques in unit verification. Integration follows the integration plan at B/C; system verification runs for A/B/C. Plan additional activities where justified by the product and QMS. Perform user-facing effectiveness/usability evaluation at its appropriate design stage, not as a late substitute for missing tests. Changes reopen regression scope and evidence freshness.

## Procedure

1. List claims, inputs, units, configuration, preconditions and observable outcomes. Separate unit, integration, system, risk-control implementation, risk-control effectiveness and intended-use validation claims.
2. Select technique(s) from the table. Write test cases with input/setup, steps, expected results and references. Derive independent expected values from the approved specification, worked calculation or validated reference, not the same algorithm under test.
3. For boundaries, state resolution and rounding. For decisions/states, include invalid combinations/transitions where relevant. For interfaces, exercise both sender and receiver assumptions and degraded modes, not only a happy path.
4. Check the harness: show a deliberately failing case or a controlled mutation is actually detected. Record discovered/executed/skipped counts; zero tests is not a successful campaign. Use the approved plan's red-run policy and preserve its evidence.
5. Run on the pinned configuration. Record command, full output location/hash, tools, data/corpus version, environment, revision, observed result and anomalies. A replay or inspection has its own method/result; do not present it as an executed dynamic test.
6. Keep failures and blocked cases. Fix through problem/change control and rerun affected tests on the changed revision; do not edit the product during an independent campaign and keep claiming the old baseline.
7. Evaluate scope/coverage and remaining gaps with the verification owner. At B/C, follow the repository's independent-human-signature rule on results or a hash-bound report. A new conversation or model is not by itself regulatory independence.

### Case and campaign template

| Field | Enter |
| --- | --- |
| Claim | Requirement/control id, revision and implementation/effectiveness distinction |
| Technique and scope | Why selected; partitions/rules/states/boundaries included and omitted |
| Setup/oracle | Configuration, data, preconditions and expected-result source |
| Execution | Procedure/command, revision, tools, observed output and log reference/hash |
| Result | Pass/fail/blocked as actually observed; anomalies and linked change |
| Campaign review | Discovered/executed/skipped counts, coverage limits, sign-off reference where applicable |

## Evidence

Use `TC`, `TR` and optional signed `VRP` with supporting logs. Keep implementation and effectiveness evidence distinct; a single activity may address both with explicit claims and criteria. Usability evidence stays in the usability engineering file and can be referenced. Clinical benefit is not inferred from technical test performance.

## Limitations

Full partition/state/branch coverage does not establish absence of defects. Pairwise combinations, when selected, do not cover every higher-order interaction. Fault injection is a controlled test, not permission for destructive production experimentation: name a non-production target and synthetic/anonymised fixture source, and obtain scope approval. Do not claim logs are automatically checked by the current validator; it checks selected metadata/links, not test truth or adequacy.

## Human decisions

People approve criteria, method tailoring, independence arrangements and open-anomaly disposition. They judge whether evidence supports release. The agent may execute authorised tests and draft records, but cannot sign for a person or call blocked work passed.

## Sources

- IEC 62304:2006+A1:2015 §§5.1.6, 5.5, 5.6 and 5.7, with class applicability preserved.
- ISO 13485:2016 §§7.3.6-7.3.7; ISO 14971:2019 §7.2.
- [ISTQB CTFL syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), chapter 4 technique descriptions. Technique selection/coverage is not a claim that this syllabus is a regulatory standard.

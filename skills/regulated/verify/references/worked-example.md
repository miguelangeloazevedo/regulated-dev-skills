# Worked example: limits, states and a missing run

Fictional test-design exercise only. The cases below are proposed, not executed evidence.

A specification accepts a measurement age up to an approved limit L, at defined timestamp resolution r. Planned boundary cases are L-r, L and L+r; expected behaviour comes from the specification's inclusive/exclusive rule. Negative partitions include absent timestamp, future timestamp and invalid units. If the design does not specify those responses, raise a content gap rather than guessing them.

A decision table crosses data validity and connection state. A state table starts at current, moves to stale on expiry, and tests whether reconnecting without new data incorrectly clears the stale state. At integration level, examine sender/receiver timestamp assumptions; at system level, observe the user-visible requirement. Class applicability and any plan-added tests remain explicit.

A UI assertion that the stale label appears could support implementation verification. If risk reduction depends on a clinician recognising the label and changing an action, its effectiveness needs suitably designed evidence from `usability` or another justified method. That is a separate open claim.

The campaign would retain commands, counts, configuration, logs and real outcomes, with independent human review where required. Here the baseline, execution and user-evaluation evidence are **absent**. A linked TC is not a passing TR. The verification owner must close those gaps through actual runs; `traceability` and `package` must preserve them, not manufacture a green result.

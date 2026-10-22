# Worked example: a stale measurement

Fictional analysis exercise only. No device, approvals, risk ratings, test execution or user sessions are represented as real.

A display may present a cached measurement without distinguishing its age. Hazard: misleading physiological information. One path is cached data -> stale value displayed as current -> clinician relies on an outdated value during assessment -> delayed treatment. A second path can involve unnecessary treatment after a condition has resolved. Separate paths preserve distinct harms, use conditions and estimates.

Preliminary hazard analysis can find this during intended-use discussions even without a component failure. A design FMEA later examines a stale-cache indicator failure or loss of timestamp; a selected fault tree can examine the combination of outdated data and unavailable freshness indication. Neither table is the risk decision.

Proposed controls: reject readings beyond a defined validity interval where appropriate (design), show provenance and freshness (protective measure), and explain limits (information for safety). The interval and response require approved clinical/design input, not an agent-selected number.

Implementation evidence would inspect and test timestamp handling and the displayed state on a specified baseline. Effectiveness evidence would test the claimed exclusion of invalid readings, and evaluate the intended user's recognition/action if the safety argument relies on it. Both are **open** here. A visibility assertion cannot close the user-action claim.

The risk owner must supply criteria and evaluate the paths and residual risks; `usability` supplies task/scenario evidence, `requirements` specifies controls, `verify` plans the technical checks, `validation` addresses affected needs, and `traceability` records what is missing. A field complaint about ignored freshness indicators reopens the effectiveness assumption.

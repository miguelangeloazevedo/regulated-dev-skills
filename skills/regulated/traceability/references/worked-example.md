# Worked example: shared hazard, distinct harms

Fictional mapping exercise only. No product test, human evaluation, approval or live backend lookup has occurred. [example.json](example.json) is a machine-readable companion for documentation checks, not a new record schema.

HAZ-1 is misleading measurement information. Context CTX-A is an outdated reading used as current during worsening condition, leading to HARM-A (delayed treatment). Context CTX-B is an outdated reading used after recovery, leading to HARM-B (unnecessary treatment). These share the hazard but must not silently share one estimate or acceptance decision.

RC-1 rejects expired readings; RC-2 presents freshness and the required safe response. The corresponding requirements and test cases would link the design and safety chains. In a backend where a Requirement is presented as a risk control, use that existing issue identity; do not create a duplicate merely because the display label differs. Standalone uses its explicit RC plus implementing SW/SPEC links, with CTX-A/CTX-B and HARM-A/HARM-B retained as labelled analysis paths in the HAZ body or a controlled reference, not invented record types.

Both controls have separate planned implementation and effectiveness claims. All outcomes in the companion are `not_run`. A test link alone cannot turn either claim green. A test connection is deliberately `unconfigured`, so backend test coverage is `unknown`, not zero failures and not a verified missing test link. This does not hide known missing evidence: execution and effectiveness remain open independently of that configuration gap.

A suitable report lists both contexts, both harms, each control, the mapping limit, the unconfigured connection and the not-run evidence. A reviewer decides adequacy and the next actions. If a backend tree shows only hazard -> risk -> requirement -> test, explicitly retrieve the linked harm and analysis context too; absence of a Harm column is not absence of harm from the model.

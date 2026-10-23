# Assurance contracts

## Two different checks

`python3 tools/rds_assurance.py validate --root .` checks declaration structure and content bindings. A successful result is `structural_only`, never authenticated approval. Like the record validator, it cannot establish that the person named in an editable file actually made a decision.

A controlled-release authorisation check must run under a trusted host identity, with policy outside the drafting agent's authority. It reads live host facts, exact source revisions and authorised decisions. Agent-authored snapshots, approval fields, result files and a declared evidence level are not that authority. A local process holding the human administrator's credential does not provide the required separation.

## Registers and states

Each `assurance/*.json` has `schema_version: 1`, its matching `kind`, and an `items` list. Item IDs are unique per register. Every item has a scope and a state: `declared`, `instruction_observed`, `host_observed`, `failed`, `unsupported`, `unassessed` or `stale`.

Observed states need exact configuration, observation time, public evidence reference, source revision and SHA-256 bindings to relevant content. Instruction observations require harness/version, provider and model/version. Host observations require host, repository, immutable policy/workflow revisions, workflow, credential boundary and runner. These are inspectable observation declarations, not self-authenticating attestations. A host probe is not an agent/model run. Do not carry a pass across configuration or bound-content changes. Explicitly stale items may retain historical hashes that no longer match the working tree; they are not current passes. Unknown/unavailable evidence stays unassessed or blocked, never green.

Regulatory entries identify the source/edition/locator and distinguish obligation, interpretation and stricter repository rule. `review: {status: pending}` contains no fabricated completion fields. A completed human review requires a human identity, date, conclusion, reviewed revision, bound content and evidence reference. Automated source checks, author checks and independent human review are separate evidence, and editable review metadata does not authenticate any of them.

## Record-system assessment

The adopting QMS owner decides applicability and intended use, assesses identity, authority, signature meaning/revision binding, audit trails, integrity/access, corrections, retention/holds/disposition and retrieval, and accepts validation evidence. An accepted assessment needs scoped version-bound evidence, an accepting owner/date and resolved gaps. The structural contract requires an immutable 40/64-character lowercase content revision identifier and nonempty SHA-256 bindings to its controlled assessment/configuration evidence, not a moving name such as main. Neither a boolean nor a reference string validates a system. Confidential supporting evidence stays in a controlled system; public summaries must not disclose CVs, clinical data or credentials.

No blanket Part 11 or Annex 11 claim is made. Applicability depends on the regulated records and intended system use. Git hashes and signed tags are not by themselves an electronic-signature or validated-system assessment.

## Existing projects

The existing `validate.py records --release` remains a structural release-readiness check. Its historical examples do not become host-authorised releases. `rds_version: 1` is the project-block schema version, not the plugin package version. Existing evidence-level declarations remain declarations unless the relevant controls are independently established.

Adopt these registers without inventing retrospective reviews. Keep unreviewed scopes pending and assess the actual tool/system configuration for intended use. `python3 tools/render_assurance.py --check` detects stale public views; omitting `--check` regenerates them without changing evidence states.

## Installed projects

Setup bundles `rds_assurance.py`, `rds_github.py` and this guide alongside the structural validator in `tools/rds/`. Run declaration checks with `python3 tools/rds/rds_assurance.py validate --root .` from the adopting project. Create the four version-1 registers described above only for that project's actual scope; the library's own support observations are not your validation evidence.

For a trusted GitHub control repository, run `python3 tools/rds/rds_assurance.py github-preflight --repo OWNER/REPO --commit SHA --pr NUMBER --environment NAME --policy .rds-policy.json --policy-commit TRUSTED_SHA`. The policy is compared to the protected remote `.rds-policy.json`; supply the exact protected workflow source revision, not a policy's self-referential commit field. The reference currently uses `.github/workflows/release.yml` on main in an isolated trusted GitHub job. Unsupported layouts and unavailable read permissions block rather than silently weaken checks. Environment strings alone are not the security boundary; actual credentials, runner isolation and host-held human controls are.

# Configuration, change and recoverable baselines

## Selection

Use a configuration-item register for identity/version control, change/status accounting for authorised evolution and a manifest-based baseline/rebuild exercise for recoverability. Use a dependency/SBOM delta when components change. Select additional artifact signing, provenance or byte-reproducibility checks based on product and QMS needs; a tag or signed file alone does not establish all of them.

## Prerequisites

Read the approved configuration plan, supported runtime/system configuration, change permission, software class, supplier/SOUP evaluations and retention requirements. Define source of truth, who can authorise changes and how the tested configuration will be identified. Begin this before introducing components or tools, not only before release.

## Timing

Identify items as they enter development. Establish the exact configuration before a verification campaign; freeze/reconcile a release baseline after required evidence is ready. Rebuild or recover it before relying on the claim that it is recoverable. Repeat applicability and regression analysis for updates, changed tools, model/data versions, anomalies and support changes.

## Procedure

1. Register source, requirements/design, build scripts, compiler/tool versions, lockfiles, runtime configuration, SOUP, test assets and applicable model/data items. Tools are configuration items, not automatically SOUP incorporated into the device.
2. Record exact identities/versions and sources; identify floating inputs and what resolves them. Hash an actual artifact with a tool when claiming a hash, never invent one. Record how externally hosted components are identified and what cannot be pinned.
3. Before edits, establish the authorised route. Before first release, use an explicitly approved plan change class only where its limits actually cover the work; otherwise obtain a CR. After release, obtain the approved CR. All controlled product changes remain subject to the QMS and applicable IEC 62304/ISO 13485 change control. A typo/test-only label does not establish that a change cannot affect evidence or safety.
4. Trace the request/authorisation to changes, affected records, impact review and verification. Preserve original results and approvals; make new revisions under document control, not backdated decisions.
5. Build a baseline manifest with each item/version/hash or resolvable reference, build procedure/environment, supported runtime/configuration, output artifacts and evidence references. Keep secrets out; identify a secret's provisioning mechanism rather than exporting its value.
6. Rebuild from a clean isolated checkout/environment, without undeclared caches or tools. Compare the expected artifacts and behaviour using the plan's criteria. If bit-identical output is required, investigate nondeterminism; otherwise document acceptable differences and evidence of equivalent intended outputs. A successful compilation alone is not a release test.
7. For recovery, demonstrate retrieval of artifacts/configuration and the planned restore/update path in a safe non-production environment with synthetic data. Record actual outcome and limits, not an assumed rollback guarantee.
8. Reconcile SOUP version deltas, requirements, host needs, anomaly applicability, supplier evaluation where relevant and required retesting before the baseline is used. `security-diligence` owns vulnerability analysis; configuration owns the versioned inventory and baseline association.
9. Keep status accounting: requested, authorised, implemented, verified and included/rejected baseline membership. Archive and protect items for the required retention period; access and approval remain host/QMS controls.

### Baseline and change worksheet

| Field | Enter |
| --- | --- |
| Authority | Plan class or approved CR, scope and real approval reference |
| Item | Stable identity, kind, exact version/source and recorded hash where available |
| Build/runtime | Procedure, tools, environment and supported configuration |
| Evidence | Tested revision, logs and artifact/SBOM references, known anomalies |
| Recovery | Retrieval/restore method, exercised configuration and actual result or open gap |
| Status | Owner, changes included/excluded, review and archive location |

## Evidence

Use existing `CR`, `BL`, SOUP and plan records plus manifests and genuine rebuild/recovery logs. Compare requested, built, tested and released item sets; explain mismatches. The current validator checks record structure, not whether a build is reproducible or an artifact can be recovered.

## Limitations

Version pinning is not supplier qualification; an SBOM is not a risk evaluation. A clean checkout or tag does not include untracked external inputs automatically. Restoration to an old release may be unsafe or incompatible; use the reviewed recovery plan rather than assuming every update is reversible. This worksheet is repository practice, not a new universal byte-identical-build requirement.

## Human decisions

The configuration/change owner authorises scope and baseline composition. QA/RA and risk/security owners decide safety/verification impact, exceptions and release acceptability. Never expand a plan's pre-approved class unilaterally.

## Sources

- IEC 62304:2006+A1:2015 §§5.1.9-5.1.11, 8.1-8.3 and 5.8, preserving class applicability.
- ISO 13485:2016 §§4.2.5, 7.3.9 and 7.4.
- ISO 14971:2019 §10 for feedback that changes risk assumptions; vulnerability and evidence interfaces remain with their owning skills.

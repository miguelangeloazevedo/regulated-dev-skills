# Backends

A backend is where the project's records live and where approvals are made. Skills never talk to a backend directly; they ask for an **action**, and the adapter maps it.

## Actions

| Action | Meaning |
| --- | --- |
| `create_record` | Create a record of a type |
| `update_record` | Change authored fields |
| `link` | Add an upward link between two records |
| `read_status` | Read the status and approval of a record |
| `record_approval_reference` | Copy the host's approval reference into the record |
| `transition` | Move a record to a status the backend allows |
| `export` | Produce a bundle of records and evidence |

An adapter states, for each action, whether it is supported, and what it cannot do.

## The four backends

| Backend | Records live in | Approval comes from | Highest evidence level it can support |
| --- | --- | --- | --- |
| `standalone` | Markdown files in git | A signed tag or a reviewed pull request, referenced from the record | 2 |
| `jira` | Jira issues and links | A workflow transition and the user who made it | 1, or 2 with a signature add-on bound to the item revision, documented by the project |
| `qity` | Jira projects with [Qity](https://www.qity.be)'s Design Control for Jira and Document Control for Jira, with other apps mapped only where installed | The applicable app/host decision, copied by reference and checked per record/gate | Not established by app presence; per-record capability must be verified, with level 2 requiring verified identity and revision-bound signing |
| `notion` | Notion pages and relations | None enforced | 0 |

**Implemented in this version: `standalone` only.** `jira`, `qity` and `notion` are a documented contract: the record shapes and approval sources an adapter must provide. No adapter ships yet, so `setup` refuses them until one exists.

Level 3 declares a record system's intended-use validation (audit trail, electronic signature); `record_system_validated` is a reference, not proof. No shipped backend authenticates the surrounding system. A/B/C policy requires direct independent-human result signatures, QMS-established competence and established Part 11 controls/intended-use validation at every evidence level. Verification acceptance and product release remain held; a level-3 declaration or GitHub preflight cannot unlock `RDS425`. External-system integration is not represented as shipped.

The `qity` adapter remains conceptual: it would map actions to installed apps, not supply a second risk-management method. No adapter implementation or measured tenant configuration is provided here.

## Document Control mapping

A future Document Control for Jira mapping must preserve the enduring document identity separately from its document-change/version identity, exact content revision and approval references. Approval, scheduled effective issue and actual release for use are distinct. Resolve the current issued revision, supersession/obsolescence, periodic-review state and controlled distribution from the configured host; a product baseline or export does not prove any of these.

Standalone stores identities and git revisions but has no independent document-change entity, effective-date engine, distribution service, periodic-review scheduler or record-retention/disposition enforcement. Do not invent statuses, successor documents or machine-checked mappings to hide these gaps. Preserve controlled external references, the original historical content and identifiable corrections to completed records. A document workflow does not by itself establish an authenticated immutable record system. Verify actual host/version capabilities and QMS procedures separately, including access, retrieval, external-origin editions, retention and authorised disposition. This contract is not a shipped integration; only standalone is implemented.

## Design Control mapping

A future Design Control for Jira mapping must distinguish stakeholder needs, system and detailed requirement roles, design outputs, Test definitions, Test Executions and controlled evidence. Multiple requirement tiers may share one host issue type and use a configured discriminator; a Test's identically labelled field may mean something different. Resolve semantic role, field context, relationship kind and stored direction, not only the issue type or display label. Preserve valid many-to-many derivation.

Standalone `SPEC.specifies` targets `SW`, not a system requirement directly. A host system-to-specification relation or non-software engineering requirement can therefore need controlled supporting references or an explicitly unsupported conversion. Do not fabricate intermediate software requirements, duplicate controls or synthetic test runs to make records fit. An attached report, Test definition or Done execution status is not automatically a passing, baseline-applicable result.

Keep host coverage as a host-defined structural metric with its predicate, denominator and exclusions. Separate unique identities from path occurrences and distinguish validation of needs from verification of requirements/design. Do not convert a host covered label into executed/passed evidence. Keep defect discovery, correction verification and regression coverage distinct; check all closure routes against the evidence policy rather than inheriting a weaker source route.

## Quality Events mapping

A future Quality Events for Jira mapping must preserve the originating complaint/finding/adverse-event reference, nonconformity, CAPA, implementation actions and resulting controlled changes as distinct roles. Identify what the installed app owns and which originating complaint/reporting processes are external; linking to them does not establish a complete complaint or vigilance implementation.

Standalone has **no independent complaint, nonconformity, CAPA or action-task lifecycle**. Existing `PRB`, `FIND` and `CR` bodies and controlled external references retain identity, affected scope, safety/protection assessment, investigation, authorised disposition and pending actions. Document approval is not event closure. Unsupported states/relations remain explicit mapping gaps, not invented record types or approval fields.

Separate containment/correction, cause-removing action, implementation verification, effectiveness evidence and human closure. For CAPA-routed work preserve plan and closure decisions separately, owners, criteria, applicable scope, monitoring window, actual result and adverse-effect review. A Done/Canceled linked action does not prove all required actions or effective resolution; cancellation needs justification. Unknown, not represented, not applicable with justification and confirmed absent remain distinct. Human reportability decisions retain awareness dates and the applicable complaint/vigilance owner.

## Safety Risk traceability mapping

When a future Qity mapping includes Safety Risk for Jira, preserve the semantic roles of Hazard, Safety Risk context, Harm, control Requirement and linked Test. The control may be an existing Requirement issue, not a duplicate RC issue. Include linked harm/context details even when the visible matrix uses a shorter hazard-to-test path. Resolve actual project/work-type/link configuration and direction at use time; display labels and source declarations do not prove saved tenant mappings.

Standalone represents the hazard/event/situation/harm detail in `HAZ` records or controlled supporting analyses, with explicit `RC` and implementing `SW`/`SPEC` links. It does not ship separate Harm/Safety Risk record types or validate those context mappings. Report these representation and adapter gaps instead of promising interchangeable records.

Separate matrix association from execution, baseline applicability and effectiveness evidence. A missing external Test connection is unassessable scope, not proof that each control has no tests. An orphan list is scoped by its filters and permissions. Reconcile requested roots, returned records and retrieval errors before describing a tree/export as complete. These are mapping requirements, not a claim that a Jira/Qity adapter ships or that source inspection verifies any live site's configuration.

Bind each risk evaluation to its risk-plan/policy revision, scales, mapping method, input evidence and applicable context/configuration. Preserve the calculated band, authored acceptability disposition, clinical benefit evidence and human approval separately. A calculated acceptable label must never create a human acceptance. Separate recalculation and reapproval; failed refresh/reopening remains an unresolved freshness gap even if an old approval or calculation remains visible.

Check whether the target can represent unrated or severity-only assessments and the approved unestimable-probability route. If not, disclose/refuse the unsupported mapping rather than invent P1/P2 values. An ordinal lookup is not a measured probability calculation. Retain analysis origin, introduced-risk causality, shared controls and reviewed applicability/exclusions in controlled supporting analyses where standalone has no dedicated machine-traversable relation.

## Approval capability and state reconciliation

Determine support **per record type and gate**, not per app. Establish the authorised identity, independence, exact reviewed content and dependencies, decision/reference, applicable workflow transition and actual resulting state. A status label, required-approvers field, acknowledgement or historical approval round alone does not establish authority, revision binding or completed approval. Reconcile decision history, transition outcome and current workflow state; a refused transition or inconsistent record is unresolved.

Level 2 additionally requires the level-1 controls and a revision-bound signature with verified identity, as defined in [approval.md](approval.md). Do not infer that capability from an approval feature or claim it for every record because one type supports a signing path. Preserve content/dependency freshness through rework and policy changes; do not copy an earlier decision to new content.

Use the app's locked dependency versions when assessing source behavior. A newer library checkout or configuration declaration is not proof of the installed/deployed version, saved tenant configuration or enforcement. Unsupported capabilities and unverified controls must remain explicit; the adapter cannot silently downgrade the requested evidence level.

## Rules for every adapter

1. **Discover, never carry ids.** Resolve issue types, link types and fields by name on the target instance at the time of use. An id from one site means something else, or nothing, on another.
2. **Dry run first.** Print every intended write, with link direction, before executing one.
3. **Confirm writes.** Every write to a shared instance names the site, the object and the exact change, and waits for a typed confirmation.
4. **Read direction back.** Assert a link by reading it from the far end, never from the parameter order used to write it.
5. **The host wins a disagreement about its own fields.** The adapter reports drift. It never silently overwrites either side.
6. **State the ceiling.** A backend page says what the backend cannot prove.

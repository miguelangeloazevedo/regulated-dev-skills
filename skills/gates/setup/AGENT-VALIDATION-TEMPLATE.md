# Agent toolchain validation template

A starting point for the record your QMS keeps before an AI agent works on a regulated product (ISO 13485 4.1.6 where your procedures treat the agent as software used in the QMS). Your procedure decides the depth; this template only lists what such a record usually holds. It is not a validation.

## Intended use
What the agent does on this product (drafts records, writes code, runs tests), and what it never does (approves, releases, decides a class).

## Configuration under validation
- Agent harness and version:
- Model and version, and how the version is pinned:
- These skills: repository tag and commit:
- Where code and records are processed, and the data processing terms that cover it:

## Risk of the use
What goes wrong if the agent's output is wrong, and which control catches it (human review, `/approve`, the validator, host-enforced review at evidence level 1 or above).

## Review method
How every agent output is reviewed before it counts: who, against what, and how the review is recorded.

## Acceptance
The checks run before first use (for example the worked examples pass, a sample change reviewed end to end) and their results.

## Revalidation triggers
A new model or model version, a new harness version, a new tag of these skills, a change in intended use, or a finding traced to agent output.

## Approval
Name, role and date of the person who accepts this validation.

## Host authority and evidence scope

- Exact trusted host/control-repository, workflow/source revision and policy:
- Drafting identity and effective permissions, distinct from the human reviewer and release job:
- Independent authorised human identity/role, decision meaning and exact content reviewed:
- Protected operations tested, actual denials and unchanged-target read-backs:
- Authorised positive path and exact released synthetic/real target (identify which):
- Agent/harness/model configurations actually exercised, distinct from host-token probes:
- Unsupported, unavailable, failed, unassessed or stale properties:
- Evidence references, observation dates and reconsideration triggers:

An invocation setting, editable approval file, CV or a passing structural test is not a demonstrated host permission boundary or completed validation. Do not use the human's administrator credential as the agent's test identity.

## Electronic-record system assessment

| Property | Intended-use control and evidence reference | Owner | Assessment/gap |
| --- | --- | --- | --- |
| Applicable record/signature rules and intended use | | | |
| Authenticated identity, access and approval authority | | | |
| Signature meaning and exact content/revision binding | | | |
| Audit trail and protected original observations | | | |
| Integrity, availability and identifiable corrections | | | |
| Retention, holds and authorised disposition | | | |
| Readable retrieval/export and confidentiality | | | |
| Version-bound validation and accepting human decision | | | |

A declared `record_system_validated` value/reference is not proof. An open table or unresolved gap remains open; no blanket Part 11 or Annex 11 claim follows from the template.

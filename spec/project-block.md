# Project block

`setup` writes one fenced block into the project's `AGENTS.md` or `CLAUDE.md`. Every skill reads it. It is short on purpose: it is always in context.

````markdown
<!-- regulated-dev-skills:start -->
## Regulated dev skills

```yaml
rds_version: 1
backend: standalone
evidence_level: 0
roles_file: quality/roles.yml
artefacts_dir: quality
jurisdictions: [eu, us]
safety_class: B
intake: quality/records/cls/CLS-1.md
standards: ["IEC 62304:2006+A1:2015", "ISO 14971:2019", "ISO 13485:2016"]
```
<!-- regulated-dev-skills:end -->
````

| Key | Meaning |
| --- | --- |
| `rds_version` | Block format version. Currently 1. |
| `backend` | `standalone`, `jira`, `qity`, `notion`. |
| `evidence_level` | 0 to 3. See [approval.md](approval.md). |
| `roles_file` | Path to the roles file. |
| `artefacts_dir` | Where records, changes and the package live. |
| `safety_class` | From the approved `CLS` record, written by `/approve` when that record is approved, never while it is proposed. One value for the product, or a map of software system to value, e.g. `{pump-ui: B, dose-engine: C, admin-portal: none}`; a record names its system with `system:` and takes that value, otherwise the highest class present. Values: A, B, C for device software; `none` for software that is not a device. Software that is part of another manufacturer's product takes the class they assign, with `class_set_by`, or is left out until they say. Left out while not decided; nothing defaults it, and the validator warns that class-dependent checks are not running. |
| `intake` | Path to the `CLS` record. Written by `intake`. |
| `class_set_by` | For software that is part of another manufacturer's product: who assigned its class, and the reference (supplier agreement, written statement). |
| `record_system_validated` | Optional declaration/reference, required structurally for evidence level 3. It does not prove validation: retain version-bound intended-use evidence, an accepting human owner and resolved assessment gaps in the actual QMS. |
| `jurisdictions` | Target regulatory regions. v0.1 content covers `eu` and `us`. |
| `standards` | Standards with the edition pinned. A skill never assumes an edition the project has not pinned. |

## Edits

`setup` creates the block. `intake` writes `intake`; `/approve` writes `jurisdictions`, `standards` and `safety_class` from the approved `CLS` record. Nothing else writes it. The block is a record of intent, not a gate: the validator reads it and checks the repository against it.

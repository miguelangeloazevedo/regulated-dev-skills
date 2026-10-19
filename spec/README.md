# Shared-core specification

Status: draft 0.1, experimental. This is the contract every skill, adapter, validator rule and eval relies on. Change it here first, then propagate.

| File | What it fixes |
| --- | --- |
| [skill-format.md](skill-format.md) | The three layers, frontmatter, the two description grammars, the body contract, the restricted YAML subset |
| [docs-page.md](docs-page.md) | The human-facing page every skill carries |
| [project-block.md](project-block.md) | The block `setup` writes into `AGENTS.md` or `CLAUDE.md` |
| [records.md](records.md) | Record types, identifiers, links, statuses, claim types, blocked criteria |
| [approval.md](approval.md) | Approval by reference plus content binding, roles file, evidence levels 0 to 3, timeouts |
| [verification.md](verification.md) | Independent verification as a declared property of the verifier |
| [changes.md](changes.md) | One change, one folder |
| [backends.md](backends.md) | The action contract and what each backend can and cannot give you |
| [extraction.md](extraction.md) | Stable identity and reconcile rules for the reverse-engineering skills |

Vocabulary, once, so the other files can stay short:

- **Skill**: a folder with a `SKILL.md`.
- **Record**: one markdown file describing one item in the traceability chain.
- **Gate**: a point where a human decides. Gates are typed commands, never fired by the agent.
- **Revision hash**: the content hash a record is approved against.
- **Evidence level**: 0 to 3, declared by the project, never claimed beyond what it proves.

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
| `qity` | Jira projects with [Qity](https://www.qity.be)'s Design Control for Jira and Document Control for Jira | The apps' own approval, copied by reference | 2 |
| `notion` | Notion pages and relations | None enforced | 0 |

**Implemented in this version: `standalone` only.** `jira`, `qity` and `notion` are a documented contract: the record shapes and approval sources an adapter must provide. No adapter ships yet, so `setup` refuses them until one exists. The author founded Qity, whose Jira apps the `qity` contract targets; that interest is why it gets no higher ceiling than `standalone`.

Level 3 needs a record system the project has validated for its intended use (audit trail, electronic signature). No backend here provides that out of the box, whoever makes it; a project that has done the validation declares `record_system_validated` with a reference to it, and only then may claim level 3.

The `qity` adapter is a thin connector. It assumes the two apps are installed and maps actions to them. It contains no method of its own.

## Rules for every adapter

1. **Discover, never carry ids.** Resolve issue types, link types and fields by name on the target instance at the time of use. An id from one site means something else, or nothing, on another.
2. **Dry run first.** Print every intended write, with link direction, before executing one.
3. **Confirm writes.** Every write to a shared instance names the site, the object and the exact change, and waits for a typed confirmation.
4. **Read direction back.** Assert a link by reading it from the far end, never from the parameter order used to write it.
5. **The host wins a disagreement about its own fields.** The adapter reports drift. It never silently overwrites either side.
6. **State the ceiling.** A backend page says what the backend cannot prove.

# Skill format

## Layout: three layers per skill

Adapted from the most-used public skill sets. Each layer has one reader and one job.

| Layer | File | Reader | Job |
| --- | --- | --- | --- |
| Skill | `skills/<group>/<name>/SKILL.md` | the agent | what to do, in order, with completion criteria |
| Reference | `skills/<group>/<name>/<TOPIC>.md` (optional) | the agent, on demand | detail too long for the skill, reached by a pointer |
| Docs page | `docs/<group>/<name>.md` | a person choosing a tool | when to reach for it, its leading word, where it fits |

Two generated files sit over the set: [`FLOWS.md`](../FLOWS.md), the map of how skills hand off to each other (generated from `neighbours`, so it is a router without a router skill), and the JSON schemas. A hand edit to either fails the validator.

`<name>` equals the `name` field. Groups are `gates`, `lifecycle`, `regulated`, `extraction`. A group is a folder only; it carries no meaning for the agent.

## Frontmatter

Only this restricted YAML subset is allowed, so the validator needs nothing but the Python standard library (see [YAML subset](#yaml-subset)).

```yaml
---
name: unit-verification
description: "Use when verifying software units against acceptance criteria, test-first."
metadata:
  group: lifecycle
  invocation: model
  role: "chain step"
  leading_word: "red first"
  neighbours: [implement, verify]
  status: draft
  reviewed_by: none
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["IEC 62304:2006+A1:2015 5.5.2"]
---
```

Typed-only skills add `disable-model-invocation: true` and may add `argument-hint`.

Non-spec keys live under `metadata`, so a skill still passes the open Agent Skills validator.

| Field | Rule |
| --- | --- |
| `name` | Lowercase letters, digits, hyphens. Equals the folder name. At most 64 characters. |
| `description` | See below. |
| `metadata.group` | One of the four groups. |
| `metadata.invocation` | `model` or `typed`. Must agree with `disable-model-invocation`. |
| `metadata.role` | `chain step`, `gate`, `run-once setup`, `runs inside the chain`, `periodic` or `standalone`. |
| `metadata.leading_word` | The skill's defining idea in two to four words. It must appear in the docs page. |
| `metadata.neighbours` | One to three skills it hands to or from. Each must exist. `FLOWS.md` is generated from these. |
| `metadata.status` | `draft`, `reviewed`, or `deprecated`. |
| `metadata.reviewed_by`, `reviewed_on` | `none` until a named reviewer signs. A skill is `reviewed` only when both are set. |
| `metadata.as_of` | Date the regulatory content was last checked. |
| `metadata.sources` | Open sources and standard clauses the skill rests on. Clause numbers only. |

## Two description grammars

**Model-invoked.** The description is the trigger and is paid for on every turn. The first 57 characters must be a self-contained trigger starting `Use when`, because some harnesses truncate the index at that width. Extra phrases may follow, up to 250 characters in total. Front-load the leading word.

**Typed-only.** The description is a one-line summary for a human reading the command list, up to 100 characters. No trigger phrases, no "Use when".

## Body contract

Sections in this order. The validator checks presence and order.

```
# Title
One paragraph: the job, then the defining constraint as a plain sentence.

## When to use       model-invoked only: situations, then "Not for:" with the sibling to use
## Reads             what it reads: the project block, records, the change folder
## Process           numbered steps; each ends with "*Done when:*" and a checkable criterion
## AI/ML branch      optional: what changes when the software includes a model
## Lessons from practice   optional: rules learned the hard way, each one line, generic
## Anti-patterns and their tells   a table: the anti-pattern, and what you see when it happens
## Refuses           each refusal paired with "*Instead:*" and the positive thing to do
## Writes            what it creates or edits
## Done when         checkable, and exhaustive where it matters
## See also          the neighbours, each with a because-clause and how to call it
```

Rules:

1. A skill reads the project block. A missing block means ask, never guess.
2. Prefer a positive target over a prohibition. A refusal pairs with what to do.
3. Dependencies are explicit instructions: "Call the Skill tool with `unit-verification`". A typed-only skill is never called by another skill; the instruction becomes "tell the user to run `/approve`".
4. Every standard is cited by clause number only. No standard text is reproduced. Interpretation is labelled `(interpretation)`.
5. Skills say "supports" and "helps produce". They never say "compliant" or "certified".
6. A lesson is a generic rule, reworded. It names no company, customer, product, instance, id or ticket.
7. No em dashes anywhere in the repository.

Changes to a skill's behaviour are recorded in [`CHANGELOG.md`](../CHANGELOG.md), per skill.

## YAML subset

Scalars (plain or double-quoted), `null`, booleans, integers, flow lists `[a, b]`, block lists with `- `, and nested maps by two-space indentation. No anchors, tags, multi-line scalars or flow maps. The validator rejects anything else.

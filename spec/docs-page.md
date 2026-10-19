# Docs pages

Every skill has a human-facing page at `docs/<group>/<name>.md`. The page is not the skill and not a copy of `SKILL.md`. Its job is to let a person hold one skill in their head: know when to reach for it, know its leading word, and see where it sits. Typed-only skills need this most, because the agent will never fire them; the person is the index.

## Sections, in order

| Section | Required | What goes in it |
| --- | --- | --- |
| `## What it does` | yes | The job in one sentence, then the defining constraint as a plain sentence |
| `## When to reach for it` | yes | Invocation mode (typed or model), then the trigger boundary. Branches go in a table: your situation, where to go |
| `## Prerequisites` | only if needed | What must exist first: a project block, records, a pinned commit |
| `## <free-form>` | yes, one to three | In the skill's own vocabulary. Must surface the leading word |
| `## Common questions` | only with evidence | Questions people actually asked, sharpest first. Never padded |
| `## It's working if` | yes | Signals a person can check without opening `SKILL.md` |
| `## Where it fits` | yes | Role, neighbours with because-clauses, and a link to [`FLOWS.md`](../FLOWS.md) |

## Conventions

- Explain the why, not the steps. The page never reproduces the process.
- No install commands; the README owns them.
- No author attribution. A claim stands on its own.
- Branches go in a table or a list, never a paragraph.
- Links are relative within the repository, and the validator checks they resolve.
- Common questions stay honest to evidence. A new skill may have none, and then the heading is omitted.

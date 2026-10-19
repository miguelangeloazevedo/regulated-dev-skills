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

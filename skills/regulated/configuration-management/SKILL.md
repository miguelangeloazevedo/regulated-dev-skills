---
name: configuration-management
description: "Use when controlling changes, versions or baselines. Configuration items, SOUP, change requests."
metadata:
  group: regulated
  invocation: model
  role: "runs inside the chain"
  leading_word: "nothing changes without a request"
  neighbours: [impact, release]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["IEC 62304:2006+A1:2015 8", "ISO 13485:2016 7.3.9", "ISO 13485:2016 4.2.5", "ISO 13485:2016 7.4"]
---

# Configuration management

Keeps the software and everything that builds it identified, changed only through approved change requests, and recoverable as baselines. It runs alongside every step of the chain.

## When to use

- A new component, SOUP item, tool or document enters the product.
- A change request is raised or implemented.
- A baseline is needed for verification, review or release.

Not for:

- Pricing a change: use `impact` first.

## Reads

The `PLAN` record's configuration management section, `SOUP` records, change requests, the repository history, baselines.

## Process

1. Identify the configuration items: source, build scripts, CI configuration, SOUP items by title, manufacturer and unique version, tools, and the documents under control (8.1.1, 8.1.2). *Done when:* Every configuration item has an identity and a version, and every `SOUP` record is a configuration item.
2. Document the system configuration the software runs on (8.1.3). *Done when:* The supported configuration is recorded.
3. Route every change through a change request: what changes, why, its impact from `impact`, and its approval before work starts (8.2.1; 13485 7.3.9). *Done when:* Every change in the repository traces to an approved `CR`.
4. After the change, verify it, including re-running verification the change makes stale, and keep the trace from request to change to verification (8.2.2 to 8.2.4). *Done when:* Every implemented `CR` links its commits and its verification.
5. Form baselines as named sets of revision hashes, tagged in the repository, and keep a status account of items and changes (8.3). *Done when:* Each baseline lists its items and hashes and can be rebuilt.
6. Define pre-approved change classes in the plan for changes that cannot affect the product (typo fixes in documents, test-only changes), with how they are recorded. Exploratory work happens on branches that never reach a baseline without a change request. *Done when:* Pre-approved change classes are listed, and no baseline contains unrequested change.
7. When a new SOUP item from a supplier with support or a contract enters the configuration, check that the supplier has a current evaluation under your purchasing process (ISO 13485 7.4) before the item reaches a baseline, and write the SOUP evaluation: source of the anomaly list, version delta from the last evaluated version, applicability to this device, and the test that re-verifies it. *Done when:* Every SOUP item in a baseline has a supplier evaluation reference where one applies, and a SOUP evaluation.

## AI/ML branch

Treat the model weights, the training code, and the training and evaluation data sets as configuration items with versions and hashes.

## Lessons from practice

- Every SOUP item is a configuration item with a unique version. A floating version is not controlled.
- Rebuild a baseline once from its listed items before relying on it.
- Approve the change request before the work, and link the commits to it.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Retroactive change request | Change requests dated after the commits they cover. |
| Unrebuildable baseline | A tag exists, but the build needs a tool version nobody recorded. |

## Refuses

- A change with no change request. *Instead:* Raise one, or record the change as a nonconformity.
- A baseline that cannot be rebuilt from its listed items. *Instead:* Record what is missing and do not use the baseline.
- A floating SOUP version in a baseline. *Instead:* Pin it, or record why it cannot be pinned.

## Writes

`CR` records, configuration item lists, `BL` records and tags. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every configuration item, SOUP included, has a unique version.
- Every change traces to an approved change request and its verification.
- Every baseline can be rebuilt.

## See also

- `impact`, because it prices each change request. It is typed-only: tell the user to run `/impact`.
- `release`, because it releases a baseline this skill formed. It is typed-only: tell the user to run `/release`.

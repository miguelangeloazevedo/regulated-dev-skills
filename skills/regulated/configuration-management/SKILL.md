---
name: configuration-management
description: "Use when controlling changes, versions or baselines. Configuration items, SOUP, change requests."
metadata:
  group: regulated
  invocation: model
  role: "runs inside the chain"
  leading_word: "nothing changes without authorisation"
  neighbours: [impact, release, development-plan]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["IEC 62304:2006+A1:2015 8", "ISO 13485:2016 7.3.9", "ISO 13485:2016 4.2.5", "ISO 13485:2016 7.4", "ISO 13485:2016 4.2.4"]
---

# Configuration management

Keeps the software and everything that builds it identified, changed only under its applicable approved authorisation, and recoverable as baselines. It runs alongside every step of the chain.

## When to use

- A new component, SOUP item, tool or document enters the product.
- A change request is raised or implemented.
- A baseline is needed for verification, review or release.

Not for:

- Pricing a change: use `impact` first.

## Reads

The `PLAN` record's configuration management section, `SOUP` records, change requests, the repository history, baselines.

## Techniques and timing

Choose and justify the method against the approved plan; do not apply every technique by default. Read the relevant local guide before doing the analysis:

- [Technique selection and procedure](references/baseline-and-change-control.md).
- [Fictional worked example](references/worked-example.md).
- [Document lifecycle and completed-record controls](references/document-and-record-control.md).

## Process

1. Identify controlled items, establish change permission and demonstrate baseline rebuild/recovery with recorded limits. Read the local technique guide before choosing the method; record prerequisites, first/repeat timing, evidence, limitations and the human decision. These are selectable repository practices unless a cited obligation or approved plan requires more. *Done when:* Method selection and tailoring have a reason, an owner and evidence criteria.
2. Identify the configuration items: source, build scripts, CI configuration, SOUP items by title, manufacturer and unique version, tools, and the documents under control (8.1.1, 8.1.2). *Done when:* Every configuration item has an identity and a version, and every `SOUP` record is a configuration item.
3. Document the system configuration the software runs on (8.1.3). *Done when:* The supported configuration is recorded.
4. Establish change permission before work: before first release, an explicitly approved plan change class only within its scope, otherwise an approved CR; after release, an approved CR. Keep controlled product changes within QMS and applicable change-control requirements (8.2.1; 13485 7.3.9). Record what changes, why and the impact. *Done when:* Every change traces to its applicable approved authorisation, without a retrospective CR.
5. After the change, verify it, including re-running verification the change makes stale, and keep the trace from request to change to verification (8.2.2 to 8.2.4). *Done when:* Every implemented `CR` links its commits and its verification.
6. Form baselines as named sets of revision hashes, tagged in the repository, and keep a status account of items and changes (8.3). *Done when:* Each baseline lists its items and hashes and can be rebuilt.
7. Define narrow pre-approved change classes in the approved plan only where the QMS permits; assess whether a document or test-only change affects product safety or relied-on evidence rather than assuming it cannot. Exploratory branches do not enter a baseline without the required authorisation. *Done when:* Change classes have explicit limits, impact rules and a record of each use.
8. When a new SOUP item from a supplier with support or a contract enters the configuration, check that the supplier has a current evaluation under your purchasing process (ISO 13485 7.4) before the item reaches a baseline, and write the SOUP evaluation: source of the anomaly list, version delta from the last evaluated version, applicability to this device, and the test that re-verifies it. *Done when:* Every SOUP item in a baseline has a supplier evaluation reference where one applies, and a SOUP evaluation.
9. Exercise clean rebuild and planned recovery using the identified manifest and environment, retaining actual logs and differences. Select byte-identical comparison only where required by the approved plan; otherwise justify artifact/behaviour comparison. Never infer a tested baseline or safe rollback from a tag alone. *Done when:* Rebuild/recovery outcomes and any unsupported inputs or rollback limits are recorded.
10. Apply document versus completed-record controls using the local document-and-record-control guide. Preserve enduring identity, exact revision and change authority; distinguish approval from effective issue and verify the current version at points of use. Name QMS owners for review triggers, external-origin documents, obsolete copies, protection, retrieval, retention and authorised disposition. Correct completed evidence through identifiable amendments retaining the original, never replacement of an observed result or backdated approval. These host/QMS controls are not automatic validator features. *Done when:* Document issue/review and record correction/retention controls have named procedures, owners and evidence or explicit gaps.

## AI/ML branch

Treat the model weights, the training code, and the training and evaluation data sets as configuration items with versions and hashes.

## Lessons from practice

- Every SOUP item is a configuration item with a unique version. A floating version is not controlled.
- Rebuild a baseline once from its listed items before relying on it.
- Establish the applicable approved authorisation before work, and link changes and verification to it.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Retroactive change request | Change requests dated after the commits they cover. |
| Unrebuildable baseline | A tag exists, but the build needs a tool version nobody recorded. |

## Refuses

- A change outside its applicable approved authorisation. *Instead:* Raise one, or record the change as a nonconformity.
- A baseline that cannot be rebuilt from its listed items. *Instead:* Record what is missing and do not use the baseline.
- A floating SOUP version in a baseline. *Instead:* Pin it, or record why it cannot be pinned.

## Writes

`CR` records, configuration item lists, `BL` records and tags. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every configuration item, SOUP included, has an identified version.
- Every change traces to its applicable approved authorisation and verification.
- Each relied-on baseline has a recorded rebuild/recovery check with limits and open gaps.

## See also

- `impact`, because it prices each change request. It is typed-only: tell the user to run `/impact`.
- `release`, because it releases a baseline this skill formed. It is typed-only: tell the user to run `/release`.
- `development-plan`, because the approved plan defines change and baseline controls. Load the `development-plan` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

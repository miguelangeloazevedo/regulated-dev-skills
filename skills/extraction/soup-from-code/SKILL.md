---
name: soup-from-code
description: "Build a SOUP and SBOM inventory from manifests and lockfiles."
disable-model-invocation: true
argument-hint: "<path>"
metadata:
  group: extraction
  invocation: typed
  role: "chain step"
  leading_word: "inventory, not judgement"
  neighbours: [configuration-management, maintenance]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["IEC 62304:2006+A1:2015 5.3.3", "IEC 62304:2006+A1:2015 8.1.2", "IEC 62304:2006+A1:2015 3.29"]
---

# SOUP from code

Inventories the software the product depends on but did not develop under its own lifecycle: third-party components and previously developed software without adequate records, which is what IEC 62304 calls SOUP. It leaves the judgements to people.

Run this only when a person types `/soup-from-code`. If you reached this skill on your own, stop and ask the user to type the command.

## Reads

Manifests, lockfiles, container files, CI configuration, build files, model files; existing `SOUP` records.

## Process

1. Pin the scan: commit, manifests found, lockfiles present or missing. *Done when:* The header lists every manifest and flags missing lockfiles.
2. Mark every dependency whose version floats (ranges, latest tags, unpinned images) and list them first. *Done when:* Floating versions are listed.
3. Check that container base images, CI actions, build tools and model files each appear, or that their absence is stated. *Done when:* Each class appears or is stated absent.
4. Build the inventory with an SBOM tool where one exists for the stack (for example syft, or a CycloneDX generator), then lockfiles, then manifests. Record the command, its version, the date and the commit. *Done when:* The inventory names how it was produced.
5. Check the places tools miss: vendored source, copied snippets, native binaries, firmware, dynamically loaded plugins, hosted services the software calls. Record each place as checked, not applicable, or unknown with the person who can resolve it. *Done when:* Each place is marked checked, not applicable or unknown with an owner.
6. Record licence and source from metadata only. Mark unknown as unknown. *Done when:* No field is guessed.
7. If allowed, query public advisories and record the source and date. A human reviews each anomaly. *Done when:* Each lookup has a source and a date, or none was run.
8. Reconcile with existing `SOUP` records and export CycloneDX or SPDX on request. *Done when:* Identifiers are stable across runs.
9. Split the inventory: SOUP is software incorporated into the device that was not developed for it, or was developed without adequate records (62304 3.29). Build tools, CI actions, test frameworks and development tools are not SOUP; record them as configuration items for `configuration-management` instead. *Done when:* Every inventory item is marked SOUP or tool, with the reason.
10. Write each `SOUP` record with its three sections: Item (filled), Requirements and Anomaly list (left as headed gaps naming the person who must fill them). At class B and C, `release` will not pass a SOUP item whose anomaly list has no evaluation. New SOUP added during development goes through `specifications` (5.3.3, 5.3.4) and `configuration-management`. *Done when:* Every SOUP record has the three sections, with the evaluation gaps named.
11. At class B and C, and for every cyber device under FD&C 524B whatever its class, export an SBOM (CycloneDX or SPDX) for every baseline and pin it to the baseline in `configuration-management`; for a cyber device this is the SBOM 524B(b) asks for. *Done when:* Each class B or C baseline has a pinned SBOM.
12. Head the output with the files read, the paths not read and a coverage figure (files read over files in scope). Draw no complete or ready conclusion about anything outside what was read. *Done when:* The output starts with the read list, the unread paths and the coverage figure.

## Lessons from practice

- A detection that cannot see something must not claim it is not there.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Libraries only | The inventory lists packages but no base image or CI action. |

## Refuses

- Marking fitness for intended use, anomaly review or integration requirements as done. *Instead:* Leave them for the owner and list the questions.
- Guessing a licence or a version. *Instead:* Write unknown.
- Writing `none` where the data is missing. *Instead:* Write `unknown` and name what would resolve it.

## Writes

`SOUP` records, a coverage section, an optional SBOM export. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every component has a source and a pin status.
- No human-owned field is filled.

## See also

- `configuration-management`, because it pins each SOUP item as a configuration item. Load the `configuration-management` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `maintenance`, because it monitors SOUP after release. Load the `maintenance` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

---
name: security-diligence
description: "Use when a change touches security of device software. Threat model, security risk, tests, SBOM."
metadata:
  group: regulated
  invocation: model
  role: "runs inside the chain"
  leading_word: "owned assets only"
  neighbours: [soup-from-code, risk]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-19
  sources: ["MDR Annex I 17.2", "MDR Annex I 17.4", "MDCG 2019-16 rev.1 (July 2020)", "FD&C Act 524B", "FDA: Cybersecurity in Medical Devices, Quality Management System Considerations and Content of Premarket Submissions (3 Feb 2026)", "IEC 81001-5-1:2021"]
---

# Security diligence

Security work built into the development process: a threat model that follows the architecture, analysis of dependencies and code, a decision on every open finding, and a correction loop back to build.

## When to use

- The architecture changes.
- Findings arrive from a scan, a review or a report.
- A release is being prepared.

Not for:

- A one-off question about a library, outside any change: answer it directly; no skill is needed.

## Reads

The architecture, the `SOUP` records, `FIND` records, the owned-asset list, the project block.

## Process

1. Read the architecture, the trust boundaries and the data flows; say whether the device is a cyber device under FD&C 524B (from `intake`). *Done when:* Boundaries and data flows are listed, and the 524B answer is named.
2. Write or update the security risk management plan and the security risk assessment, kept apart from the safety risk file but linked to it: assets, threats derived from this architecture, vulnerabilities, scoring method, and the controls (IEC 81001-5-1; FDA premarket cybersecurity guidance). *Done when:* A security risk assessment exists with its scoring method and links to the safety hazards it can cause.
3. Describe the security architecture with the views a reviewer expects: global system, multi-patient harm, updatability, and security use cases. *Done when:* Each view exists or is marked not applicable with the reason.
4. Review the code and the dependencies against the threats, as the least privileged user. Decide and record how much security testing the risk calls for, from connectivity, exposure and the harm a compromise could cause: automated malformed-input (fuzz) testing in the build for every external input of connected software, and a penetration test by qualified people (independent of the build, with named experience in the target technology) where the device is a cyber device or the harm is serious. This scaling is this repository's practice, not a clause. Link each finding to the test that showed it. *Done when:* The test applicability decision is recorded; each test run has a record with its revision; every finding links to its test and has a person's decision, or is open.
5. For a cyber device, plan the postmarket vulnerability process, secure update and patch design, and the SBOM, and keep the SBOM pinned to each baseline (524B(b)). *Done when:* Each 524B element is planned, or the device is recorded as not a cyber device.
6. List every new permission, scope or outbound destination as a release decision, and write the security risk management report linking controls to their verification. *Done when:* The report exists and links controls to test results.
7. List what the FDA premarket cybersecurity guidance expects in a submission that this skill does not produce, with an owner: labelling content for users, the cybersecurity management plan for the postmarket period, and the summary documentation for the submission. *Done when:* Each uncovered item has an owner.

## Lessons from practice

- Derive threats from the trust boundaries and data flows of this architecture, then check against known classes.
- Test as a non-admin. What works for you can fail for everyone else.
- List every new permission, scope or destination as a release decision.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Scanning by default | An active scan ran with no owned-asset entry and no approval. |

## Refuses

- Scanning anything not on the owned-asset list. *Instead:* Add it to the list with the owner's approval, or leave it alone.
- Deciding whether a finding is acceptable. *Instead:* Present the options and the owner decides.
- Treating security as a separate project type. *Instead:* It is a sub-process of regulated work.

## Writes

Threat model updates, `FIND` records, evidence files. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- The threat model matches the architecture.
- Every finding has a decision.
- Active scans are traceable to an approval.

## See also

- `soup-from-code`, because its inventory feeds dependency analysis. It is typed-only: tell the user to run `/soup-from-code`.
- `risk`, because findings that can cause harm become hazards. Load the `risk` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.

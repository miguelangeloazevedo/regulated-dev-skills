# Support

These are declarations, not authenticated decisions or product certification.

Generated from [the source register](../../assurance/support.json). Structural checks do not authenticate the underlying evidence.

## github-restricted-job-denials

**State:** stale

Historical restricted probe job succeeded at its pinned revision. The reference workflow has since changed and requires a fresh run; this is not current support or AI agent behavior evidence.

**Limits:** Historical token-scope observations only, not a current pass. The old waiting release run was cancelled after a verifier credential integration gap was identified. The corrected positive path still requires a narrowly scoped verifier credential, fresh probes and genuine human decisions.

**Skills revision:** 67ed1b2d81ee4f71649b825cef099274e55d6d97

**Observed on:** 2026-10-23T04:23:53Z

**Configuration:**

```json
{
  "credential": "Job-scoped GITHUB_TOKEN: contents/read, pull-requests/read, actions/read; no human credential",
  "host": "github.com",
  "job_id": 120239390053,
  "policy_revision": "1d6e2d1a7fd88972336a8e8982004def88eb25b3",
  "repository": "miguelangeloazevedo/regulated-dev-skills-assurance-sandbox",
  "request_commit": "441010674c6664ff5b7135063ed464132f555cb1",
  "run_id": 39900076036,
  "runner": "GitHub-hosted ubuntu-latest as resolved by this run",
  "sandbox_commit": "1d6e2d1a7fd88972336a8e8982004def88eb25b3",
  "workflow": ".github/workflows/release.yml",
  "workflow_actor": "github-actions[bot]",
  "workflow_revision": "1d6e2d1a7fd88972336a8e8982004def88eb25b3"
}
```

**Content bindings:**

```json
[
  {
    "path": "examples/host-enforced/probe_permissions.py",
    "sha256": "842b77417d9bda1cc00df5b49bee83b71c10038a63f1c1b8ed56ec6ba61d1ea9"
  },
  {
    "path": "examples/host-enforced/workflows/release.yml",
    "sha256": "cc3b0de35946c4507c4185f500679c2616ed80658e3c43bcf2fd744b3d834d3c"
  }
]
```

**Evidence:** https://github.com/miguelangeloazevedo/regulated-dev-skills-assurance-sandbox/actions/runs/39900076036/job/120239390053

## github-authorised-positive-path

**State:** host_observed

The human-gated synthetic workflow completed live host-authority checks and published exactly the independently approved synthetic request commit. This is host-predicate evidence, not medical-device release, agent behavior, electronic signatures or Part 11 system validation.

**Limits:** Synthetic non-production records only. Logs show eligible host predicates followed by a synthetic release; human PR approval, exact release target and tag ref were read back. Bound files match the pinned sandbox source. No cross-agent behavior, production validation, QMS competence or Part 11 signing-system acceptance is established; this observation cannot clear A/B/C RDS425 holds.

**Skills revision:** 5898403cfe429603c95d850f8e771f5dbfb8979c

**Observed on:** 2026-10-23T15:33:03Z

**Configuration:**

```json
{
  "credential": "Separate configured read-only verifier with effective GET access observed; publishing uses the protected job's contents/write GITHUB_TOKEN. Broader verifier permission inventory was not independently measured.",
  "host": "github.com",
  "job_id": 120453392859,
  "policy_revision": "aec8c1ab28d547ed344d6bcff023dfdc010beee7",
  "repository": "miguelangeloazevedo/regulated-dev-skills-assurance-sandbox",
  "request_commit": "a99c74ca0aaf6832cf24ded10b8601d0a7bd2aef",
  "request_number": 2,
  "reviewer_id": 183697641,
  "run_id": 39965250283,
  "runner": "GitHub-hosted Ubuntu 24.04.5; runner 2.338.0, image 20261012.334.1",
  "tag": "synthetic-approved-39965250283",
  "workflow": ".github/workflows/release.yml",
  "workflow_revision": "aec8c1ab28d547ed344d6bcff023dfdc010beee7"
}
```

**Content bindings:**

```json
[
  {
    "path": "tools/rds_github.py",
    "sha256": "b38ba292929d22aa3e30060d4bbc8c1843fb3715993f55a60e2faa24b7d1c10f"
  },
  {
    "path": "examples/host-enforced/workflows/release.yml",
    "sha256": "241714f7ee46bdd2c86684c6bdd5b7fd19f5ffab8bc810d02c035719a62662aa"
  }
]
```

**Evidence:** https://github.com/miguelangeloazevedo/regulated-dev-skills-assurance-sandbox/actions/runs/39965250283/job/120453392859

## github-restricted-job-denials-current

**State:** host_observed

Five protected operations attempted by the restricted job token returned HTTP 403 and complete unchanged-target read-backs in the corrected synthetic reference configuration.

**Limits:** Restricted host-token observations only, using named synthetic non-production fixtures. Not an agent/model run, full administrator-bypass proof, product verification or validated Part 11 system.

**Skills revision:** 5898403cfe429603c95d850f8e771f5dbfb8979c

**Observed on:** 2026-10-23T13:55:40Z

**Configuration:**

```json
{
  "all_http_status": 403,
  "all_outcome": "denied",
  "all_target_unchanged": true,
  "credential": "Job-scoped GITHUB_TOKEN: contents/read, pull-requests/read, actions/read, metadata/read; no human credential or environment secret",
  "host": "github.com",
  "job_id": 120453310622,
  "policy_revision": "aec8c1ab28d547ed344d6bcff023dfdc010beee7",
  "probe_names": [
    "unauthorised-approval",
    "protected-record",
    "protected-policy",
    "protected-workflow",
    "unauthorised-release"
  ],
  "repository": "miguelangeloazevedo/regulated-dev-skills-assurance-sandbox",
  "request_commit": "a99c74ca0aaf6832cf24ded10b8601d0a7bd2aef",
  "run_id": 39965250283,
  "runner": "GitHub-hosted Ubuntu 24.04.5; runner 2.338.0, image 20261012.334.1",
  "workflow": ".github/workflows/release.yml",
  "workflow_revision": "aec8c1ab28d547ed344d6bcff023dfdc010beee7"
}
```

**Content bindings:**

```json
[
  {
    "path": "examples/host-enforced/probe_permissions.py",
    "sha256": "cce0a94a46e16e5bcd689446aee19cf57306011c702b4e4ac499bfc8df74e2c6"
  },
  {
    "path": "examples/host-enforced/workflows/release.yml",
    "sha256": "241714f7ee46bdd2c86684c6bdd5b7fd19f5ffab8bc810d02c035719a62662aa"
  }
]
```

**Evidence:** https://github.com/miguelangeloazevedo/regulated-dev-skills-assurance-sandbox/actions/runs/39965250283/job/120453310622

## claude-code

**State:** unassessed

Typed command invocation is not an operating-system approval permission boundary.

**Limits:** No measured agent/harness configuration is claimed.

## other-agents

**State:** unassessed

Instruction-following alone does not establish host-enforced approval or release.

**Limits:** No measured agent/harness configuration is claimed.

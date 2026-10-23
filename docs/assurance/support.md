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

**State:** unassessed

The original waiting run is cancelled. The corrected workflow requires a fresh run, configured read-only verifier and genuine independent human request/environment decisions.

**Limits:** No authorised release or completed live preflight is claimed before those real decisions and exact target read-back.

**Evidence:** https://github.com/miguelangeloazevedo/regulated-dev-skills-assurance-sandbox/actions/runs/39900076036

## claude-code

**State:** unassessed

Typed command invocation is not an operating-system approval permission boundary.

**Limits:** No measured agent/harness configuration is claimed.

## other-agents

**State:** unassessed

Instruction-following alone does not establish host-enforced approval or release.

**Limits:** No measured agent/harness configuration is claimed.

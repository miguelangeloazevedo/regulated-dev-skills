# Support

These are declarations, not authenticated decisions or product certification.

Generated from [the source register](../../assurance/support.json). Structural checks do not authenticate the underlying evidence.

## github-restricted-job-denials

**State:** host_observed

The restricted synthetic probe job completed its permission-denial and unchanged-target checks successfully. This is a host credential/runner observation, not an AI agent behavior result.

**Limits:** Only the restricted probe job succeeded. Overall workflow and authorised positive release remain pending human decisions. Detailed run logs are unavailable while the overall workflow is waiting. This does not isolate branch protection from token-scope enforcement, test an actual agent/model or establish electronic signatures.

**Skills revision:** 67ed1b2d81ee4f71649b825cef099274e55d6d97

**Observed on:** 2026-10-23T04:23:53Z

**Configuration:**

```json
{
  "credential": "Job-scoped GITHUB_TOKEN: contents/read, pull-requests/read, actions/read; no human credential",
  "job_id": 120239390053,
  "repository": "miguelangeloazevedo/regulated-dev-skills-assurance-sandbox",
  "request_commit": "441010674c6664ff5b7135063ed464132f555cb1",
  "run_id": 39900076036,
  "runner": "GitHub-hosted ubuntu-latest as resolved by this run",
  "sandbox_commit": "1d6e2d1a7fd88972336a8e8982004def88eb25b3",
  "workflow": ".github/workflows/release.yml",
  "workflow_actor": "github-actions[bot]"
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

Bot-authored synthetic request and bot-initiated release workflow are waiting for the independent human request review and protected environment decision.

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

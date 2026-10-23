# Host-enforced synthetic reference

This is a synthetic non-production permission test, not a medical product, verified regulatory process or validated record system. The active probe harness refuses any target except `miguelangeloazevedo/regulated-dev-skills-assurance-sandbox`. The policy template deliberately has no authorised reviewer until its owner configures real immutable account IDs. Do not aim these probes at production or copy customer data.

## Authority boundary

The **untrusted drafting/probe job** has `contents: read`, `pull-requests: read`, `actions: read`, no inherited human credential and no environment secrets. It can draft in its disposable workspace but cannot push changes to the control repository, approve requests, change policy/workflows or publish releases. The measured object is this host credential/runner configuration, not behavior of a particular AI model.

The **trusted request controller** has broader permissions to create a fixed synthetic request and dispatch a protected workflow. It never executes agent-provided code or accepts arbitrary scripts/paths. Its token must never enter the drafting job. The **trusted release job** runs reviewed control code from the exact protected main revision, waits for a human-gated environment, checks live authority/revision/policy and publishes only a labelled synthetic result. Proposed source is data to review, not executable privileged-job code.

Administrators, control-repository maintainers, workflow authors and runners are trusted. GitHub environment variables are not an authentication mechanism against a process that already holds an administrator credential. This is not a secure configuration for an agent holding the human's token, administration rights, or permission to author arbitrary workflows in this control repository. A default read permission does not prevent a different trusted workflow explicitly requesting write privileges. Separate untrusted source/workspaces from the trusted control plane.

## Provisioning layout and controls

In the authorised public sandbox, copy `controller.py`, `probe_permissions.py` and `synthetic-record.json` to the root; copy `policy.json` to `.rds-policy.json`; copy `workflows/*.yml` to `.github/workflows/`; copy the library's `tools/rds_assurance.py` and `tools/rds_github.py` to `tools/`. Configure the policy's real reviewer IDs and protect a CODEOWNERS file that covers all control paths.

Require independent/code-owner review on main, dismiss stale reviews, enforce controls for administrators, forbid force pushes/deletion and do not grant bypass actors. Set default workflow permission to read. The trusted fixed controller needs permission to create requests; that does not grant the restricted probe token review authority. Configure `synthetic-release` with an explicitly authorised human reviewer, self-review prevention, no administrator bypass and protected-branches-only deployment. Read back actual saved settings before testing.

Dispatch `controller.yml` on protected main. It creates a bot-authored synthetic request, then dispatches `release.yml` under the bot identity. This makes the human reviewer different from the requester/initiator rather than manufacturing a human sign-off. Restricted probes run first. The human must actually review/approve the exact synthetic request and approve the environment deployment through GitHub. An agent using the human's local token is not an acceptable substitute.

The trusted preflight requires a separate read-only verifier credential because the job's `GITHUB_TOKEN` cannot read required administration policy. Store it as environment secret `RDS_HOST_READ_TOKEN` in `synthetic-release`, scoped to this control repository only. Give it the read permissions required for Administration (branch protection and workflow settings), Environments, Actions, Contents and Pull requests, with Metadata read access. Do not grant any write permission. Use an appropriately permissioned GitHub App token or short-lived fine-grained token through the organisation's credential process; never copy a human administrator's general-purpose token.

The workflow supplies this secret only to the two trusted release steps after the human environment gate. The shared GET-only collector uses it in its subprocess environment for both preflight and the publisher's final recheck, without replacing the separate `GH_TOKEN` used for synthetic release publication. It is never supplied to the restricted probe or fixed request-controller job. Missing or inadequate read access blocks the gate; there is no cached-fact fallback. Provisioning the secret is an actual prerequisite, not implied by approving a deployment.

## Interpreting results

A denial requires HTTP 403 **and unchanged target read-back**. Authentication failures, hidden/missing resources, invalid payloads and transport failures are inconclusive, not successful protection. An unexpected successful write stops further probes and is a failed configuration, even when the attempted payload was synthetic. Run logs contain outcome codes and target identities, never credentials or raw error responses.

A positive result additionally requires the authorised human path, current live preflight and read-back of the exact synthetic release/tag target. Offline fixtures cannot stand in for this. `eligible` means the checked host predicates hold at observation time, not an enduring authorisation token, guaranteed atomicity with future host changes, product verification or an electronic signature. Record exact run/source/policy revisions, times, limitations and outstanding human review in the support register. Do not generalise a host-token result into support for unrun agents.

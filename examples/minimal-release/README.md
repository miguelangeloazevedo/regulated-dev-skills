# Example: a releasable class A device (fictional)

The smallest record set that passes the release gate: classification, plan, need, requirements, specification, verification and validation, risk management report and design review, all approved, with results on the release baseline.

```bash
python3 tools/validate.py records examples/minimal-release/quality \
  --roles examples/minimal-release/quality/roles.yml \
  --project examples/minimal-release/AGENTS.md --release --baseline 7c2d1e0
```

It exits 0, with one warning (RDS407): `7c2d1e0` is a fictional baseline, so it does not resolve to a commit in this repository. In a real project the gate checks the baseline exists in git, so results are tied to the configuration that was tested. Compare with [infusion-rate-check](../infusion-rate-check/README.md), which fails the same gate and says why. It runs at evidence level 1 (the `ref` fields stand for host review records); at level 0 the gate refuses release. Class A needs no signature on each result; at class B or C the gate would ask for one.

Nothing here describes a real device. Whether software like this is a device at all depends on its claims: without the adherence claim it would usually not be.

# Example: structurally complete class A records (fictional)

A small record set for classification, plan, need, requirements, specification, verification and validation, risk management report and design review. Structural checks pass; verification acceptance and product-release authorisation remain held.

**Try [Your first change](FIRST-CHANGE.md):** use agent prompts and an isolated copy of these records to make the empty-day message explicit, observe stale approvals and prepare a draft handoff. No product code or real test evidence is supplied.

The names, approvals, signature declarations, host references (`ref: example` and `example.invalid`), results and baseline are fictional. They demonstrate record structure, not actual execution, human signatures, QMS competence, Part 11 controls or system validation. Never reuse these declarations as real evidence.

```bash
python3 tools/validate.py records examples/minimal-release/quality \
  --roles examples/minimal-release/quality/roles.yml \
  --project examples/minimal-release/AGENTS.md --report
```

It exits 0 on structure. The report labels coverage `structural_only`, verification acceptance `held` and accepted results as empty. Adding `--release --baseline 7c2d1e0` exits 1 with `RDS425`, plus the expected fictional-baseline warning. A/B/C all require direct independent-human result signatures, QMS-established competence and established Part 11 surrounding-system controls/intended-use validation by repository policy. The backend cannot establish that external system; levels, references and GitHub authority evidence do not clear the hold. Compare [infusion-rate-check](../infusion-rate-check/README.md), which also has incomplete structural release evidence.

Nothing here describes a real device. Whether software like this is a device at all depends on its claims: without the adherence claim it would usually not be.

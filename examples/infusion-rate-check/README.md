# Example: infusion rate check

A fictional class B software feature, small enough to read in five minutes. It shows the record chain the skills produce, with real revision hashes, approvals and signed verification results, and it is checked in CI.

Nothing here describes a real device. The classification in `CLS-1` rests on an assumed hardware limit, a risk control outside the software that IEC 62304 4.3 a) lets the assessment consider; remove it and the assessment gives class C.

Check it:

```bash
python3 tools/validate.py records examples/infusion-rate-check/quality \
  --roles examples/infusion-rate-check/quality/roles.yml \
  --project examples/infusion-rate-check/AGENTS.md --report
```

Add `--release` and the same records fail: TC-3 has no result, so this example is not releasable yet, and the validator says so.

Then edit one word in `quality/records/sw/SW-1.md` and run it again: the approval shows as stale.

| Record | What it shows |
| --- | --- |
| [CLS-1](quality/records/cls/CLS-1.md) | Classification: MDR class III (Rule 11 credits no risk control) beside IEC 62304 class B (62304 does consider the external hardware limit). The contrast is the point |
| [UN-1](quality/records/un/UN-1.md) | A need with a validation method |
| [SYS-1](quality/records/sys/SYS-1.md), [SYS-2](quality/records/sys/SYS-2.md) | System requirements |
| [SW-1](quality/records/sw/SW-1.md) | A software risk control, with an absent-value criterion |
| [SW-2](quality/records/sw/SW-2.md) | A requirement with two parents |
| [SPEC-1](quality/records/spec/SPEC-1.md) | A specification that states what it refuses |
| [HAZ-1](quality/records/haz/HAZ-1.md), [RC-1](quality/records/rc/RC-1.md) | A hazard and its control, with the enforcing mechanism |
| [TC-1](quality/records/tc/TC-1.md) to [TC-3](quality/records/tc/TC-3.md) | Verification and validation cases |
| [REV-1](quality/records/rev/REV-1.md) | A design review draft with its read-list, waiting for its participants |
| [TR-1](quality/records/tr/TR-1.md), [TR-2](quality/records/tr/TR-2.md) | Results run by a model and signed by a human, as this repository's rule requires at class B (the standard itself does not require a signature on each result) |

The report is honest about what is missing: TC-3 has no result yet because validation has not run, and SYS-1, SYS-2 and SPEC-1 have no test case of their own. It also lists SW-2 as a requirement with several parents.

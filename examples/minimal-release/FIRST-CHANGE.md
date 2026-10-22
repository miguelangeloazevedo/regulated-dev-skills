# Your first change: the empty-schedule message

Work through one small change with your agent: make the class A example's empty-day message explicit. You will inspect the linked records, draft a change and see why an old approval cannot cover new content.

This is a **record-only exercise on fictional fixtures**, not a product implementation or a device release. No application or product test suite is supplied. Names, approvals, host references (`ref: example`), test results and baseline `7c2d1e0` are illustrative, not evidence that anyone approved or tested a device. Do not reuse them in your own project. Class A is an assumption of this example, not a classification for your software.

## 1. Make a practice copy

Start in the root of your pinned clone of this repository, with Python 3.9 or later and a POSIX shell. Install the skills using the [README](../../README.md#installation) if you want the agent to follow them. The validator commands work without an agent installation.

Run these blocks in order, in the same shell. The first creates a temporary directory and copies the example there; subsequent edits stay in that copy. Keep it until you finish reviewing your work, then remove that practice directory. Nothing here needs a commit or a push.

```bash
export RDS_WALKTHROUGH="${RDS_WALKTHROUGH:-$(python3 -c 'import tempfile; print(tempfile.mkdtemp(prefix="rds-first-change-"))')}"
cp -R examples/minimal-release "$RDS_WALKTHROUGH/project"
printf 'Practice project: %s\n' "$RDS_WALKTHROUGH/project"
```

Give your agent the printed path, then this prompt:

> Read only the practice project. Use `status` when I type `/status`. Inspect AGENTS.md, quality/roles.yml, PLAN-1 and the chain UN-1 -> SYS-1 -> SW-1 -> SPEC-1 -> TC-1 -> TR-1. Explain what each record contributes. Treat all existing approvals and results as fictional. Do not run typed skills, edit files, approve anything or claim product tests ran.

Type `/status` yourself. If your agent cannot load these skills, open the matching `SKILL.md` files in this repository. The human-only command boundary still applies; instruction-following alone is not host enforcement.

## 2. Check the starting records

```bash
python3 tools/validate.py records "$RDS_WALKTHROUGH/project/quality" \
  --roles "$RDS_WALKTHROUGH/project/quality/roles.yml" \
  --project "$RDS_WALKTHROUGH/project/AGENTS.md" --report
```

**Checkpoint:** exit 0, `0 error(s), 0 warning(s)`. The JSON report describes links and coverage in the fixtures. It does not mean the classification is right, the host enforces reviews, or the product works. The validator prints that limit too.

Read [SW-1](quality/records/sw/SW-1.md), [SPEC-1](quality/records/spec/SPEC-1.md) and [TC-1](quality/records/tc/TC-1.md). The requirement currently says the screen must indicate an empty day, but does not name the exact text. Our proposed change is:

> With no entries for today, the screen says "No entries scheduled for today."; it never shows yesterday's list.

## 3. Establish the change boundary before drafting

In a real project, first confirm the approved intended purpose, classification, plan and permission to use the agent. Do not copy this example's assumptions or approval names. With your QA/RA owner, establish which change route applies: the plan's allowed change classes before first release, or an approved change request after release. The fixture's PLAN-1 does not establish permission for this new change.

For this exercise, ask for analysis only:

> Use `configuration-management` to identify what permission this change needs and what the fictional plan does not supply. Do not infer permission from the passing validator. Prepare the impact questions for my QA/RA owner: does the wording change intended use, user comprehension, a risk control, requirements, usability or validation? List the records and baseline evidence that may need review. Do not decide the answers or edit records yet.

If you want the `impact` skill to draft the assessment, **you type `/impact`** with the proposed change. A smaller text change is not automatically safety-irrelevant. In your product, stop until the required change authorisation and human decisions exist.

## 4. See an approval become stale

The following deliberate edit is a diagnostic experiment **only in the disposable copy**. It leaves the old approval attached so you can observe the warning. It is not the procedure for revising a controlled record in your QMS.

```bash
python3 - <<'PY'
import os
from pathlib import Path

record = Path(os.environ["RDS_WALKTHROUGH"]) / "project/quality/records/sw/SW-1.md"
old = "With no entries for today, the screen says so; it never shows yesterday's list."
new = 'With no entries for today, the screen says "No entries scheduled for today."; it never shows yesterday\'s list.'
text = record.read_text()
assert text.count(old) == 1, "Expected the untouched practice requirement; stop rather than edit a different revision."
record.write_text(text.replace(old, new))
PY
```

```bash
python3 tools/validate.py records "$RDS_WALKTHROUGH/project/quality" \
  --roles "$RDS_WALKTHROUGH/project/quality/roles.yml" \
  --project "$RDS_WALKTHROUGH/project/AGENTS.md" --report
```

**Checkpoint:** exit 0 with warnings, including `RDS218` / `STALE` for SW-1 and `RDS222` / `SUSPECT` for records whose approval depends directly on the changed requirement. Warnings do not fail a normal record check. Inspect the actual ids in the report; do not assume the tool found every indirect dependency. Follow the links through specifications, cases, results, review and release evidence yourself with `traceability` and the impact assessment.

Try the release check on the changed copy:

```bash
python3 tools/validate.py records "$RDS_WALKTHROUGH/project/quality" \
  --roles "$RDS_WALKTHROUGH/project/quality/roles.yml" \
  --project "$RDS_WALKTHROUGH/project/AGENTS.md" \
  --release --baseline 7c2d1e0
```

**Checkpoint:** exit 1 with `RDS401` release blockers for stale or suspect approvals. A baseline warning is also expected: `RDS411` if your temporary copy is outside a git work tree, or `RDS407` if it is inside one where the fictional baseline does not resolve. Neither authenticates the fixture's test results. Do not suppress warnings, recompute approval hashes or change status to make the exercise green.

## 5. Draft the connected changes with the agent

Stop running the diagnostic commands here. The remaining steps are prompts and human checkpoints, not a script that silently completes approvals. In a real project, preserve the prior approved revision through your document-control procedure and create the authorised draft revision. Do not overwrite the approved baseline in place.

After the change is authorised, give the agent this prompt, with your actual change reference in place of the bracketed text:

> Work only in the practice project under [the authorised change reference]. Use `requirements`, then `specifications`, then `verify` to prepare draft record revisions, not to execute tests. Propose a diff first. In SW-1, specify the exact empty-day wording. In SPEC-1, describe how the view presents that wording when today's filtered entries are empty; preserve date filtering and sequence ordering. In TC-1, require the exact message when only yesterday's entries exist and when no entries exist, and retain the populated-day ordering checks. Keep the existing ids and links. Show which approvals would need replacing under document control, but do not write approvals. Do not relabel TR-1 as a result for this change. List the verification, usability and validation questions for human review. Stop with a draft handoff.

Review the proposed diff before allowing the draft edits. If the authorisation is not present, the right outcome is a stop, not a guessed change class. Use `traceability` to review the affected chain. Ask the QA/RA owner whether the user need, risk analysis and validation need updates; a wording-only diff does not answer that question.

| Record | Draft or review work | Human checkpoint |
| --- | --- | --- |
| SW-1 | Exact text and preserved no-yesterday criterion | Requirement content and acceptance criteria |
| SPEC-1 | Presentation behaviour for an empty filtered day | Design agrees with the approved requirement |
| TC-1 | Exact-message checks plus existing ordering checks | Procedure and expected results are suitable |
| TR-1 | Keep as historical fixture evidence, not a new run | New result requires actual execution on an identified revision |
| UN-1, SYS-1, risk and validation records | Assess impact rather than changing automatically | QA/RA decides and records the scope of review |
| Review and baseline records | Identify affected evidence and outstanding decisions | Named participants review; a person authorises release |

## 6. Know where this exercise ends

You now have a draft handoff, **not a releasable changed product**. This record-only example cannot provide new implementation evidence, test logs, user evaluation or a real release baseline. Do not ask the agent to invent them.

In your real project, continue only after the appropriate records are approved: `implement` builds the authorised change, `verify` runs the required tests and records the commands, logs and exact tested revision, and `validation` addresses user needs where the approved plan and impact assessment require it. Class A does not require unit verification under this repository's class table; your approved plan may still require unit tests. Verification and validation are different activities.

For approvals, **the authorised person types `/approve`** for the records they have reviewed, after seeing their content, diff and hash. The agent cannot impersonate the fixture's named people. A hash recomputation is not an approval. An approval also needs the real host reference required by your evidence level. Your own QMS and host controls must enforce the review; the validator does not authenticate those references.

Once the real evidence is complete, `configuration-management`, `traceability` and `package` prepare the baseline and its record index. Run the release check from a clean checkout of the actual tested baseline, not `7c2d1e0`. Passing that check is still only structural. **A person types `/release`** and the people your QMS names authorise release.

### Handoff checklist

- [ ] Change permission and impact decisions are named, not inferred.
- [ ] Draft requirement, specification and test-case changes are linked and reviewed.
- [ ] Stale approvals and direct and indirect dependencies are listed.
- [ ] Historical results are not presented as new verification evidence.
- [ ] Missing product runs, logs, validation and approvals remain explicitly outstanding.
- [ ] No fictional name, reference or baseline has been adopted as real evidence.

For the complete lifecycle, see [FLOWS.md](../../FLOWS.md). For content binding and the limits of approval fields, see [spec/approval.md](../../spec/approval.md).

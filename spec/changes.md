# Changes

One change is one folder. Context is recovered from files, not from the conversation.

```
<artefacts_dir>/changes/<id>-<slug>/
  change.yml        status, owner
  proposal.md       the problem and the intended outcome
  spec.md           what will change, in the project's vocabulary
  tasks.md          tickets with their blocking edges
  evidence/         test results, scan outputs, review reports
  decision.md       optional: rulings made during the change
```

`change.yml`:

```yaml
id: C-014
title: Add dose range checks
status: in_progress
owner: bob
opened: 2026-10-19
```

## Flow with back-edges

```
intake -> user-needs -> requirements -> specifications -> implement -> unit-verification -> verify -> design-review -> package -> approve -> release
   ^           ^              ^                ^                                               |
   +-----------+--------------+----------------+-----------------------------------------------+   a reclassification trigger or a requirement change
                                         problem-resolution <- any defect, at any step
```

A reclassification trigger (new claim, module, market, model or external control) sends the change back to `intake`. A requirement change sends it back to `requirements`. A defect enters `problem-resolution` and comes back through the chain as a change request.

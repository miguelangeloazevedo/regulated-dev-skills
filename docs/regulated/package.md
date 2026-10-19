<!-- docs page for skills/regulated/package/SKILL.md -->

## What it does

Builds the design and development file index from approved records and verification results, not from memory. It supports the technical documentation (MDR Annex II and III, or a US submission) and is not that documentation.

## When to reach for it

Type `/package`, or the agent reaches for it automatically when a task fits.

| Your situation | Where to go |
| --- | --- |
| A baseline passed verification and the package is needed. | `package` |
| A submission or audit pack is being prepared. | `package` |
| The baseline is not verified | [`verify`](../regulated/verify.md) |

## Prerequisites

An approved, verified baseline.

## Generated from records

Every line of the index is **generated from records** and points at its source record and hash. It supports the technical documentation and is not that documentation: its first page lists the sections it does not cover. Below evidence level 3 it is stamped as an uncontrolled draft.

## It's working if

- Every line links to a record and a hash.
- Regenerating gives the same package.

## Where it fits

Role: chain step. Neighbours: [`verify`](../regulated/verify.md), because its results are in the package; [`release`](../gates/release.md), because it checks the package matches the baseline. For the whole map, see [FLOWS.md](../../FLOWS.md).

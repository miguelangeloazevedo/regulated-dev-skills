# Changelog

## 0.1.0-draft.3

- `setup` and `development-plan` ask the QA/RA owner whether the agent is software that must be validated under ISO 13485 4.1.6; the agent never decides it. A validation in progress lets work start.
- `release` stops while the agent toolchain validation is still open.
- README: a section on class A and software that is not a device, pointing to the smallest record set that passes the release gate.

## 0.1.0-draft.2

- Release is refused while any software system has no decided class, whether or not IEC 62304 is claimed; software that is not a device records `none`.
- `--release` ends by saying that passing is a structure check and that the `REL` record still needs approval by the people your QMS names.
- FLOWS names the US post-market reports next to the EU ones: medical device reports (21 CFR 803) and corrections and removals (21 CFR 806).
- README: the smallest path points to `usability` from the use specification and `validation` at the end.

## 0.1.0-draft.1

First public draft.

- 27 skills in four groups: gates, lifecycle, regulated and extraction.
- Record shapes, an approval model bound to content hashes, and a validator with a release gate (`tools/validate.py`).
- Two worked examples: a class B project that fails the release gate on real gaps, and a class A project that passes it.
- Every skill is a draft until a named person reviews it.

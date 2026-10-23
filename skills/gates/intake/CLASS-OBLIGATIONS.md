# Class obligations

What the software safety class asks of the other skills. Clause numbers only; the standard's text is not reproduced. Read against your own copy of the pinned edition.

Edition: IEC 62304:2006+A1:2015, the current published version as of 2026-10-10; edition 2 is not confirmed as published. Source: a clause-by-clause reading of that edition, made on 2026-10-10 by the repository author, not by a notified body. It is an interpretation; check each line against your own copy of the standard before relying on it.

EN 62304 is not listed in the MDR or IVDR harmonised standards decisions (checked 17 June 2026), so applying it gives no presumption of conformity; it is presented as state of the art.

## Applies to every class

Clauses 4.1 to 4.3, 5.1.1 to 5.1.3 and 5.1.6 to 5.1.9, 5.2 except 5.2.3, 5.5.1, 5.7, the release tasks 5.8.1, 5.8.2, 5.8.4, 5.8.7 and 5.8.8, and the maintenance (6), risk management (7), configuration management (8) and problem resolution (9) processes, in the parts not marked otherwise in the standard.

## Added for class B and C

| Activity | Clauses |
| --- | --- |
| 5.1 development planning | 5.1.5, 5.1.10, 5.1.11, 5.1.12 |
| 5.2 requirements analysis | 5.2.3 |
| 5.3 architectural design | 5.3.1, 5.3.2, 5.3.3, 5.3.4, 5.3.6 |
| 5.4 detailed design | 5.4.1 |
| 5.5 unit implementation and verification | 5.5.2, 5.5.3, 5.5.5 |
| 5.6 integration and integration testing | 5.6.1, 5.6.2, 5.6.3, 5.6.4, 5.6.5, 5.6.6, 5.6.7, 5.6.8 |
| 5.8 release | 5.8.3, 5.8.5, 5.8.6 |

## Added for class C only

| Activity | Clauses |
| --- | --- |
| 5.1 development planning | 5.1.4 |
| 5.3 architectural design | 5.3.5 |
| 5.4 detailed design | 5.4.2, 5.4.3, 5.4.4 |
| 5.5 unit implementation and verification | 5.5.4 |

## What the skills do with it

| Class | `specifications` | `implement` and `unit-verification` | `verify` |
| --- | --- | --- | --- |
| A | Specifications that tie the code to its requirements | Implement each unit (5.5.1) | System testing (5.7); `release` covers 5.8.1, 5.8.2, 5.8.4, 5.8.7, 5.8.8 |
| B | Adds the architecture: software items, interfaces, SOUP requirements, units (5.3, 5.4.1) | Adds unit acceptance criteria and unit verification (5.5.2, 5.5.3, 5.5.5) | Adds integration testing (5.6); `release` adds 5.8.3, 5.8.5, 5.8.6 |
| C | Adds segregation for risk controls and detailed design per unit (5.3.5, 5.4.2 to 5.4.4) | Adds the additional unit acceptance criteria (5.5.4) | As class B |
| `none` (not a device) | The depth the `PLAN` chose, with its reasons, accepted by QA/RA | The depth the `PLAN` chose | The depth the `PLAN` chose |
| Not decided | Asks for the class to be decided with `/intake`. A depth may be recorded in the `PLAN` for now; nothing is released until the class is decided | Asks | Asks |

## Legacy software

Clause 4.4 applies only to legacy software: software lawfully placed on the market and still marketed without enough evidence of development under the standard (3.36). A new product does not use it. See `gap-assessment`.

## Signature of verification results

At A/B/C, every verification result requires a direct signature by a named human independent of its author/builder, with competence established by the adopting QMS. A signed report cannot substitute. Established Part 11 surrounding-system controls and intended-use validation are universal repository policy, not a claim that Part 11 legally applies to every project or that IEC 62304 requires this per-result signature.

The shipped backend cannot authenticate that surrounding system. Verification acceptance and product release remain held; `--release` returns `RDS425` for A/B/C even with complete declarations, evidence-level metadata or GitHub authority evidence. `none` remains a separate non-device classification; an undecided class never defaults. Class-dependent test activities in the table above are unchanged by this stricter signing policy.

## Rules that do not change with class

- Nothing here assigns a class by default. A system without a decided class is shown as not decided, and the skills ask. If you claim IEC 62304 conformance, note that the standard itself applies class C requirements until a system is classified (4.3 g); that is a decision for you, not a default of these skills.
- The class is assigned per software system and may be refined per software item (4.3 d).
- Only risk controls outside the software system lower its class (4.3 a).
- The class is recorded in the risk management file and is under change control (4.3 c).

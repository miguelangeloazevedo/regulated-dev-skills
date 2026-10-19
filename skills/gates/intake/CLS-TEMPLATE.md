# CLS record template

Copy into `records/cls/CLS-<n>.md`. Every answer is `proposed` until `/approve`. Write "not decided" and the question wherever a person has not decided; never fill a value in to complete the template.

```markdown
---
id: CLS-<n>
type: cls
title: Classification of <product>
status: draft
authored_by: <who drafted>
as_of: <date>
recheck_by: <earliest re-check date of any dated source>
sources: ["<each source with its edition or date>"]
---

## Qualification
Per module: device / not a device / part of another product / not decided.
For each: the step that decides it (MDCG 2019-11 step, 201(h), each 520(o)(1) exclusion considered), and for
"part of another product" who classifies it and what they said.

## Classification
Device modules only. EU: rule 3.3 first, then the rule-out table. US: candidate product code, regulation and pathway,
for regulatory affairs to confirm.

| Rule | Result | Why |
| --- | --- | --- |
| Implementing rules 3.1 to 3.5 (3.3 for software) | | |
| Rules 1 to 4 (non-invasive devices) | | Usually not applicable to software alone; reached only through 3.3 |
| Rules 5 to 8 (invasive and implantable devices) | | Usually not applicable to software alone; reached only through 3.3 |
| Rule 9 (active therapeutic) | | |
| Rule 10 (active diagnostic and monitoring) | | |
| Rule 11, decision limb | | |
| Rule 11, monitoring limb | | |
| Rule 11, all other software | | |
| Rule 12 (active, administering or removing substances) | | Reached by software through 3.3 |
| Rule 13 (all other active devices) | | |
| Rule 14 (medicinal substance) | | |
| Rules 15 to 21 (special rules) | | Check each that could apply to the claims, for example Rule 15 for contraception |
| Rule 22 (active therapeutic with integrated diagnostic function) | | |

Fill every row. A row says applied, with the class, or ruled out, with the reason.

## Software safety class
Per software system: A, B, C, none, or not decided. For A, B or C: the hazardous situation, the external controls
considered, the harm after them, provisional or final, and the HAZ records it rests on.
FDA documentation level, separately, with its own reasoning.

## Overlays
AI Act, cybersecurity (EU and US separately), usability, health software, health data, electrical equipment:
each yes, no or unclear, with its source.

## Sources checked
| Source | Checked on | Re-check by |
| --- | --- | --- |

## Reclassification triggers
- A new claim or intended-purpose wording, including marketing material
- A new module or software system
- A new market or jurisdiction
- A model added to a decision path
- A change in the risk controls outside the software system
- A newly identified hazardous situation with more severe harm than the class rests on
- A source past its re-check date
```

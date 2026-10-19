---
id: CLS-1
type: cls
title: Classification of the infusion rate check
status: approved
authored_by: bob
sources: ["MDR Annex VIII", "IEC 62304:2006+A1:2015 4.3"]
as_of: 2026-10-19
approval:
  by: alice
  role: qa_ra
  on: 2026-10-19
  revision: 9a068c85fadda76bceefce157bebf93432f7a9f2d459f08112e356ce83365767
  ref: example
---

## Qualification
Fictional example. One module, software that drives an infusion pump's rate entry. EU: a medical device under MDR Art 2(1). US: a device under FD&C 201(h); no 520(o) exclusion applies.

## Classification
EU. Implementing rule 3.3: the software influences the use of the pump, so it takes the pump's class. The software also provides information used for a therapeutic decision (the warning), so Rule 11 applies in its own right. The strictest result applies.

| Rule | Result | Why |
| --- | --- | --- |
| 3.3 with Rule 12 | IIb | The pump administers medicinal products in a potentially hazardous manner given the drugs and rates (fictional case) |
| Rule 11, decision limb | III | The warning is information the clinician uses directly to decide whether to start an infusion at a given rate, so its significance to the decision is high; that decision may cause death if wrong. The classification turns on that decision's impact, not on a software failure, and credits no risk control |
| Rule 11, monitoring limb | Ruled out | It does not monitor physiological processes |
| Rule 9, 10, 13, 15, 22 | Ruled out | No energy delivery of its own, no diagnosis, Rule 12 applies, not a contraceptive, no closed loop |

Result: III, the strictest rule. US: candidate product code for infusion pump software, likely 510(k); regulatory affairs confirms.

## Software safety class
Class B, provisional until the architecture is done (rests on HAZ-1). IEC 62304, unlike MDR classification, considers risk controls outside the software system, so the hardware maximum counts here. An unnoticed high rate can contribute to a hazardous situation. Counting the pump's independent hardware maximum, which is a risk control outside the software system, the remaining possible harm is non-serious injury. Without that hardware limit the class would be C. FDA documentation level recorded separately: Enhanced, because before any risk control a failure of the rate guard could present a hazardous situation with a probable risk of death or serious injury.

## Overlays
AI: no model in the decision path. Cybersecurity: not a cyber device in this example (no connectivity). Usability: IEC 62366-1 applies. Health data: override logs hold user identity; GDPR applies to them.

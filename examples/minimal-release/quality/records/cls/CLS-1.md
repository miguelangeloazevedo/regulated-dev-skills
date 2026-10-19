---
id: CLS-1
type: cls
title: Classification of the medication schedule display
status: approved
authored_by: bob
sources: ["MDR Annex VIII", "IEC 62304:2006+A1:2015 4.3"]
as_of: 2026-10-19
approval:
  by: alice
  role: qa_ra
  on: 2026-10-19
  revision: 6ec2cdaf8d49c9a66710f8255ce5a7f6ca4740f3ecf855135ea6d0535c21f8e9
  ref: example
---

## Qualification
Fictional. One module that shows a patient the medication schedule their clinician entered, with reminders. EU: medical device software under MDR Art 2(1) for this example, because the manufacturer claims it supports adherence to a treatment.

## Classification
Independent software, so Rule 11 applies in its own right. It provides no information used to take diagnostic or therapeutic decisions and monitors nothing; the clinician decides the schedule.

| Rule | Result | Why |
| --- | --- | --- |
| 3.3 | Not applicable | Drives no device |
| Rule 11, decision limb | Ruled out | Displays a schedule a clinician decided; informs no decision |
| Rule 11, monitoring limb | Ruled out | Monitors no physiological process |
| Rule 11, all other software | I | Fall-back limb |
| Rule 9, 10, 12, 13, 15, 22 | Ruled out | Not active therapeutic or diagnostic, administers nothing |

Result: class I.

## Software safety class
Class A. A failure (a reminder that does not fire) cannot contribute to a hazardous situation in this fictional case, because the paper schedule the clinician hands out stays the reference and the labelling says so. That procedure is a risk control outside the software system.

## Overlays
AI: none. Cybersecurity: no network connection. Usability: IEC 62366-1 applies. Health data: GDPR Art 9 applies to the stored schedule.

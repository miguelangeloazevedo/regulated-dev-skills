---
name: intake
description: "Classify the product: device status, risk class, software safety class, applicable rules."
disable-model-invocation: true
argument-hint: "[module or change-id]"
metadata:
  group: gates
  invocation: typed
  role: "run-once setup"
  leading_word: "what is it?"
  neighbours: [setup, risk, impact]
  status: draft
  reviewed_by: "models only (Gemini, GPT, Grok, Mistral, Muse); no person"
  reviewed_on: none
  as_of: 2026-10-22
  sources: ["MDR Art 2(1)", "MDR Art 2(12)", "MDR Annex VIII", "MDCG 2019-11 rev.1", "MDCG 2021-24 rev.1 (April 2026)", "FD&C Act 201(h)", "FD&C Act 520(o)", "FD&C Act 524B", "21 CFR 820 (QMSR, effective 2026-02-02)", "IEC 62304:2006+A1:2015 4.3", "IEC 82304-1:2016 1", "AI Act Art 6(1) to 6(1c), consolidated text as at 2026-07-27", "AI Act Art 113 as amended by Regulation (EU) 2026/1744", "FDA: Clinical Decision Support Software (final, 29 Jan 2026)", "IEC 62304:2006+A1:2015 4.3 g)", "FDA: Content of Premarket Submissions for Device Software Functions (June 2023)", "FD&C Act 524B(b)", "IEC 60601-1 14", "FD&C Act 520(o)(3)", "MDR Annex VIII 3.1", "Regulation (EU) 2024/2847 (Cyber Resilience Act) Art 2(2), Art 14", "Regulation (EU) 2025/327 (EHDS)", "AI Act Art 9 to 15, 17, 72"]
---

# Intake

Works out what the software is before any work starts: a medical device or not, a part of someone else's device or not, and if it is a device, its risk class, its software safety class and the rules that apply. It drafts every answer with its rule path; a person decides each one. It never assumes a class.

Run this only when a person types `/intake`. If you reached this skill on your own, stop and ask the user to type the command.

## Reads

Everything the manufacturer says about the product: the intended purpose, labelling, instructions for use, promotional material and claims, the architecture, any existing technical file. Existing `CLS` records.

## Process

1. List every source that states what the product is for. Under the MDR the intended purpose is what the manufacturer states in labelling, instructions, promotional material and statements, so marketing copy counts. *Done when:* Every source is listed with its date, and contradictions between sources are findings.
2. Draft the intended purpose: the medical purpose, the decision the output informs, the intended users, the patient population, the use environment and the platform. Mark it `proposed`. *Done when:* Each element is drafted or marked open.
3. Split the product into modules and qualify each one. Each module ends in one of four outcomes. **Device**: medical device software under MDR Art 2(1) (or an accessory, or an Annex XVI product) following the MDCG 2019-11 decision steps, and in the US a device function under FD&C 201(h) with no 520(o) exclusion; For clinical decision support, the function is excluded from the device definition only if all four criteria of FD&C 520(o)(1)(E) hold: (1) it does not acquire, process or analyse a medical image, a signal from an in vitro diagnostic device, or a pattern or signal from a signal acquisition system; (2) it displays, analyses or prints medical information about a patient or other medical information; (3) it supports or provides recommendations to a health care professional about prevention, diagnosis or treatment; (4) it lets that professional independently review the basis for the recommendations, so that they do not rely primarily on them. Read them with FDA's Clinical Decision Support Software guidance (final, 29 January 2026, which superseded the September 2022 version). **Not a device**: say which step rules it out. In the US walk all five 520(o)(1) exclusions, not only (E): (A) administrative support of a health care facility, (B) maintaining or encouraging a healthy lifestyle unrelated to disease, (C) electronic patient records, only to the extent they transfer, store, convert formats or display the equivalent of a paper chart, created, stored, transferred or reviewed by health care professionals, part of certified health IT, and not interpreting or analysing patient records, images included; (D) transferring, storing, converting formats or displaying clinical laboratory test or other device data and results, unless it interprets or analyses them; (E) clinical decision support as below; QMS software, general health or wellness software and administrative software usually land here. **Part of another product**: a component, library or service that goes into a device someone else places on the market; that manufacturer classifies the product. Record who, and the class they assign to your software, in `class_set_by` with its source; until they say, it stays not decided, with the question to ask them. **Not decided**: the open question and who answers it. If it is an in vitro diagnostic, stop: IVDR is out of scope for v0.1. An exclusion under (C), (D) or (E) can be withdrawn by FDA order (520(o)(3)); check for such an order before launch and whenever the function changes. For a module whose class another manufacturer sets, record that manufacturer's expectations (the supplier agreement, what its purchasing process requires of you) and have QA/RA accept them before any depth below the full lifecycle is used. *Done when:* Each module has one of the four outcomes with the step that decides it.
4. For device modules only, classify. EU: apply implementing rule 3.3 first: software that drives or influences the use of a device falls within the same class as that device; software independent of any other device is classified in its own right. Software that has a medical purpose of its own and also drives or influences a device is medical device software too (MDCG 2019-11 rev.1): classify it in its own right as well, and the strictest result applies. Then apply Rule 11 in full, reading each limb by the significance of the information to the decision and the impact of that decision: software that provides information used to take decisions with diagnosis or therapeutic purposes is class IIa, class IIb if those decisions may cause a serious deterioration of health or a surgical intervention, class III if they may cause death or an irreversible deterioration; software that monitors physiological processes is class IIa, class IIb where it monitors vital physiological parameters whose variations could result in immediate danger; all other software is class I. Also apply every active-device rule that can apply: Rule 9, Rule 10, Rule 12 (reached by software through rule 3.3), Rule 13 (the class I fall-back), Rule 15 and Rule 22. Where several rules apply, the strictest wins. The rule-out table lists the rules named here; for any other Annex VIII rule, state that it does not apply to the software on its own or apply it. Classification is governed by the intended purpose (Annex VIII 3.1), and Rule 11 turns on the significance of the information to the decision and the impact that decision may have on the patient (MDCG 2021-24 rev.1), not on what a software failure could cause; the rules make no provision for lowering a class because a risk control limits the harm. Only IEC 62304 considers external risk controls, in the next step; never carry a control from one into the other. Fill the rule-out table: each rule, applied or ruled out, and why. US: classification is set by regulation and FDA, not by the manufacturer. Identify candidate product codes, classification regulations and the likely pathway (510(k), De Novo, PMA, or exempt); the pathway is a candidate for regulatory affairs to confirm, never a determination. *Done when:* Each device module has a candidate class per jurisdiction and a rule-out table covering every rule named here.
5. For device software systems only, propose a software safety class under IEC 62304 4.3 a), assuming the software fails (probability 1). Class A: it cannot contribute to a hazardous situation, or the risk is acceptable once risk controls outside the software system are considered. Otherwise class B if the possible harm is non-serious injury, class C if death or serious injury. Controls outside the software system (hardware, a separate software system, clinical procedure) may reduce the probability or the severity of the harm and are considered; controls inside it are not. Software that is not a device gets `none`. Software that is part of another product gets the class its manufacturer assigns (A, B or C, with `class_set_by`), or stays not decided until they say; it never gets `none`. A class proposed before the risk analysis and the architecture exist is provisional: say so in the record, cite the `HAZ` records or the preliminary hazard analysis it rests on, and list the risk analysis as a reclassification trigger. Never fill a class in by default: a missing class shows as not decided. If you claim IEC 62304 conformance for device software, note that the standard applies class C requirements to a system until it is classified (4.3 g); say so to the user and let them decide. Record the FDA documentation level separately with its own test: Enhanced where a failure of any device software function could present a hazardous situation with a probable risk of death or serious injury, assessed before risk controls; otherwise Basic. *Done when:* Each software system has a proposed class with its reasoning, `none` with the reason, the other manufacturer's class with its source, or not decided with the question.
6. Hand provisional risk/class assumptions and reclassification triggers to `risk`, early use specification to `usability`, and cyber-device/connectivity assumptions to `security-diligence`. A technique score, FMEA RPN or security score does not decide the regulatory or software class. *Done when:* The plan/analysis owners receive assumptions and unresolved inputs without a default classification.
7. Check the overlays, each yes, no or unclear with its source. *Done when:* Every overlay has an answer, a source and a date.

   - **AI:** under AI Act Art 6(1) the system is high-risk only if both hold: it is a safety component of an Annex I product, or is itself one (the MDR is in Annex I), and that product must undergo third-party conformity assessment. Condition (b) is not met by a device that needs no notified body (MDR class I, not Is, Im or Ir); such a system could still be high-risk through Annex III. Art 6(1a) to 6(1c) refine condition (a) and (b): AI used solely for non-safety aspects of user assistance, performance optimisation, service efficiency, automation, convenience or quality control is not a safety component; AI whose failure would endanger health or safety is one; third-party assessment needed only for risks other than health and safety does not count. For Annex I products the high-risk requirements apply from 2 August 2028 (Art 113 as amended by Regulation (EU) 2026/1744). Some duties already apply whatever the risk tier: Chapters I and II, including AI literacy (Art 4) and the prohibitions (Art 5), since 2 February 2025, except Art 5(1)(ba), (bb), 5(1a) and 5(1b), which apply from 2 December 2026; the transparency duties of Art 50 from the general application date in Art 113. Check each date against the consolidated text. Record the date you checked the consolidated text on EUR-Lex, because this area is moving; regulatory affairs confirms the AI tier.
   - **US:** FDA's AI-enabled device software functions guidance is still a draft; the predetermined change control plan guidance is final (August 2025).
   - **Cybersecurity:** a cyber device under FD&C 524B includes software, can connect to the internet and could be vulnerable to cybersecurity threats; if so the submission needs a postmarket vulnerability plan, secure design with patches and updates, and an SBOM (524B(b)). Record the answer separately from the EU view (MDR Annex I 17.2, 17.4, 18.8).
   - **Usability:** IEC 62366-1. Standalone health software on general platforms: IEC 82304-1.
   - **Health data:** GDPR Art 9.
   - **US quality system:** 21 CFR 820 (QMSR) incorporates ISO 13485:2016 by reference since 2 February 2026, with the additions and exceptions part 820 sets out.
   - **Electrical equipment:** if the software runs in or drives medical electrical equipment, point to IEC 60601-1 clause 14 (programmable electrical medical systems) for the team that owns the equipment's conformity; this skill does not assess it. If the AI system is high-risk, list the provider obligations, each with an owner and the skill or QMS process that covers it: risk management (Art 9, folded into `risk`), data and data governance (Art 10), technical documentation (Art 11), record-keeping and logging (Art 12), information to deployers (Art 13), human oversight (Art 14), accuracy, robustness and cybersecurity (Art 15), the quality management system (Art 17), documentation keeping and logs (Art 18, 19), corrective actions and the duty to inform (Art 20), cooperation with authorities (Art 21), conformity assessment, the EU declaration and CE marking (Art 43, 47, 48), registration where it applies (Art 49), post-market monitoring (Art 72) and serious incident reporting (Art 73).
   - **Non-device software:** the Cyber Resilience Act does not apply to devices under the MDR or IVDR (Art 2(2)); for a device, cybersecurity runs through MDR Annex I 17.2, 17.4 and 18.8 instead. Software that is not a device is in its scope when it is a product with digital elements made available on the EU market whose intended or reasonably foreseeable use includes a direct or indirect data connection (Art 2(1)); record each condition. The CRA's essential requirements apply from 11 December 2027; its reporting duty has applied since 11 September 2026, also to products placed on the market earlier (Art 69(3), 71(2)), on two tracks: an actively exploited vulnerability needs an early warning within 24 hours, a notification within 72 hours and a final report within 14 days of a fix being available; a severe incident needs an early warning within 24 hours, a notification within 72 hours and a final report within one month of the notification. An electronic health record system falls under the EHDS Regulation (EU) 2025/327, which applies from 26 March 2027 with later dates for its EHR system rules.

8. Derive the standards set with pinned editions and the jurisdictions, and list what the safety class requires of the other skills using [CLASS-OBLIGATIONS.md](CLASS-OBLIGATIONS.md). Note that EN 62304 is not listed in the MDR harmonised standards decisions, so it is state of the art without a presumption of conformity. For software that is not a device, list the standards the team chooses to follow, if any (for example IEC 82304-1 for health software, or ISO 13485 4.1.6 for QMS software), as a choice rather than an obligation. *Done when:* The standards, jurisdictions and class obligations are listed.
9. Write the `CLS` record from [CLS-TEMPLATE.md](CLS-TEMPLATE.md) with every answer `proposed`, its rule path and its sources. Write only `intake` (the record's path) into the project block; `jurisdictions`, `standards` and `safety_class` are written by `/approve` when the record is approved, never before. Tell the user to run `/approve` with a role allowed to approve classification. *Done when:* The `CLS` record exists and the project block holds no proposed value.
10. List the reclassification triggers in the record: a new claim or intended-purpose wording, a new module, a new market, a model added to the decision path, a change in the external risk controls, and a newly identified hazardous situation whose harm is more severe than the one the class rests on. Every later skill that sees one sends the change back here. *Done when:* Triggers are listed.
11. Write the date each dated source was checked next to it in the `CLS` record, and a re-check date: three months later for AI Act, FDA guidance, MDCG guidance, six months for the rest. `/approve` on a record with a passed re-check date is refused by `approve` until the sources are checked again. Put the earliest re-check date in the record's frontmatter as `recheck_by`. *Done when:* Every dated source has a checked date and a re-check date.

## AI/ML branch

If a model sits in the decision path, record what it outputs, who acts on it and whether its output is reviewed before it reaches a patient. That changes the Rule 11 limb, the AI Act tier and the FDA submission content, so record it before classifying.

## Lessons from practice

- Absence never renders as a value. A missing class shows as not decided, never as A and never as C.
- Qualify before you classify, and qualify each module on its own intended purpose.
- The class is a function of the claims. A new claim is a reclassification trigger, not a marketing edit.

## Anti-patterns and their tells

| Anti-pattern | The tell |
| --- | --- |
| Wishful qualification | The record says not a device, and the product page says it detects a condition. |
| Favourable rule | Rule 11 was applied and no other active-device rule was considered. |
| Blank class | A software system with no safety class, treated as A by every later skill. |

## Refuses

- Deciding a class, a qualification or an overlay. *Instead:* Draft it with the rule path and name the role that decides.
- Concluding a module is not a device without walking the steps. *Instead:* Walk MDCG 2019-11 and, for the US, every 520(o) criterion, and show each.
- Choosing the most favourable rule when several apply. *Instead:* Apply the strictest and record why the others were considered.
- Lowering a software safety class with controls inside the same software system. *Instead:* Count only controls outside it, or change the architecture and reclassify.
- Quoting standard text. *Instead:* Cite the clause number.
- Classifying an in vitro diagnostic. *Instead:* Say IVDR is out of scope for v0.1 and stop.
- Treating the IEC 62304 class as the FDA documentation level or the MDR class. *Instead:* Record the three separately.
- Filling in a safety class nobody decided. *Instead:* Leave it out and show it as not decided.
- Classifying a product another manufacturer places on the market. *Instead:* Record who classifies it and ask them.
- Treating clinician review of the output as lowering the MDR class. *Instead:* Classify on what the software provides and to whom, and record the review as a risk control. In the US the same review is criterion (iv) of the 520(o)(1)(E) exclusion from the device definition, not a class reduction: assess it there.

## Writes

`records/cls/CLS-<n>.md`, and the `jurisdictions`, `standards`, `safety_class` and `intake` keys of the project block. Record shapes and required sections: `tools/rds/RECORDS.md` in the project (copied by `setup`); the validator checks them.

## Done when

- Every module has one of the four outcomes, with the step that decides it.
- Every device module has a candidate class and a rule-out table.
- Every software system is A, B, C, `none`, or not decided with the question and who answers it.
- Every overlay is answered with a source.
- The record is `proposed` and waiting for `/approve`.

## See also

- `setup`, because it sets the tooling intake writes into. It is typed-only: tell the user to run `/setup`.
- `risk`, because the safety class rests on the hazard analysis, and external controls can change it. Load the `risk` skill when that applies: its `SKILL.md` sits in the same skills directory as this one.
- `impact`, because it checks every change against the reclassification triggers. It is typed-only: tell the user to run `/impact`.

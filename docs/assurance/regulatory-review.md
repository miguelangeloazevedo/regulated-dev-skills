# Regulatory review

These are declarations, not authenticated decisions or product certification.

Generated from `assurance/regulatory-review.json`. Structural checks do not authenticate the underlying evidence.

## qualification-and-classification

**State:** declared

Qualify each software/module by intended purpose and applicable jurisdiction before assigning device or IEC software safety classifications. EU device risk class and IEC software safety class are different decisions.

**Sources:** Regulation (EU) 2017/745 (as applicable at project intake) Article 2(1); Annex VIII 3.1, 3.3, Rule 11 and other applicable rules; FD&amp;C Act (as applicable at project intake) Sections 201(h) and 520(o); IEC 62304 (2006+A1:2015) 4.3

**Human review:** pending

## no-automated-default

**State:** declared

The tooling never assigns a default safety class. IEC 62304 4.3 g) applies class C requirements until classification; the responsible person must resolve this obligation and the tool&#x27;s undecided state, not treat a warning as exemption.

**Sources:** IEC 62304 (2006+A1:2015) 4.3 g)

**Human review:** pending

## 62304-5.2.3

**State:** declared

Software-implemented risk control requirements are included in requirements to the extent appropriate; this clause&#x27;s class applicability is B/C. This does not exempt class A from device risk management.

**Sources:** IEC 62304 (2006+A1:2015) 5.2.3

**Human review:** pending

## 62304-5.2.4

**State:** declared

Re-evaluate the medical-device risk analysis when software requirements are established and update it as appropriate.

**Sources:** IEC 62304 (2006+A1:2015) 5.2.4

**Human review:** pending

## architecture-and-detailed-design

**State:** declared

Architecture and architecture verification in 5.3.1-.4/.6 apply B/C; risk-dependent segregation in 5.3.5 is C. Unit subdivision 5.4.1 is B/C; detailed unit/interface design and its verification 5.4.2-.4 are C. Stronger project documentation can be planned without mislabelling it a class-A standard obligation.

**Sources:** IEC 62304 (2006+A1:2015) 5.3.1-5.3.6; 5.4.1-5.4.4

**Human review:** pending

## 14971-control-implementation

**State:** declared

Implement every selected risk control and verify its implementation. Keep the evidence distinct from the claim that the control reduces risk effectively.

**Sources:** ISO 14971 (2019) 7.2

**Human review:** pending

## 14971-control-effectiveness

**State:** declared

Verify each risk control&#x27;s effectiveness, recording results in the risk management file. One suitable activity may support implementation and effectiveness, but both claims need evidence. Separate physical records are not a universal additional ISO requirement.

**Sources:** ISO 14971 (2019) 7.2

**Human review:** pending

## 14971-residual-dispositions

**State:** declared

Evaluate individual residual risk against planned criteria; consider more controls if unacceptable. Where additional control is impracticable, benefit-risk evaluation needs supporting data and human evaluation. Do not substitute an acceptable calculated band, overall review or business benefit for this disposition.

**Sources:** ISO 14971 (2019) 7.3, 7.4; overall residual risk under clause 8 is a separate activity

**Human review:** pending

## bc-result-signing

**State:** declared

The repository requires human-signed verification results for class B/C, independent from their builder. This is a stricter repository rule, not a claim that IEC 62304 mandates an independent human signature on every test result. The human&#x27;s competence, independence and actual decision remain separately established.

**Sources:** IEC 62304 (2006+A1:2015) 5.1.6 and applicable verification clauses; repository policy adds the per-result signing rule

**Human review:** pending

## software-release

**State:** declared

Complete and evaluate software verification before release (all classes), document anomalies (all), assess their unacceptable-risk implications under 5.8.3 (B/C), identify the version and preserve/deliver the configuration under the applicable clauses. A green structural check is not a human release decision or product verification.

**Sources:** IEC 62304 (2006+A1:2015) 5.8.1-5.8.8 with clause-specific safety-class applicability

**Human review:** pending

## qms-tool-validation

**State:** declared

For software used in an ISO 13485 QMS, document validation procedures, validate before first use and revalidate as appropriate after software/application changes. The approach is proportionate to risk of use. A package version, passing unit suite or declared boolean does not validate an adopting organisation&#x27;s intended use.

**Sources:** ISO 13485 (2016) 4.1.6

**Human review:** pending

## reviewer-competence

**State:** declared

Competence rests on relevant education, training, skills and experience with retained supporting evidence. A CV supports competence but does not demonstrate that a named reviewer assessed this revision or provide independent review of their own work.

**Sources:** ISO 13485 (2016) 6.2; version-bound independent review is the repository&#x27;s assurance practice

**Human review:** pending

## electronic-record-system

**State:** declared

Assess electronic-record/signature applicability and the actual surrounding system, including validation, access, audit trails, signature meaning, retention and corrections. Hashes, names and signed tags alone do not establish these controls. No blanket Part 11 or Annex 11 compliance claim is made.

**Sources:** 21 CFR Part 11 (applicable regulatory text) 11.1(b), 11.10(a)-(g), 11.50, 11.200; applicability assessed separately; ISO 13485 (2016) 4.2.4, 4.2.5

**Human review:** pending

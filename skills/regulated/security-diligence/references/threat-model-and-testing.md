# Threat models, security testing and vulnerability response

## Selection

Use architecture/data-flow threat modelling to ask what must be protected, from whom, across which boundaries and under which assumptions. STRIDE is an optional prompt set (spoofing, tampering, repudiation, information disclosure, denial of service and privilege escalation), not a proof of completeness. Use attack trees when combinations of attacker actions need closer analysis. Use abuse cases to make a threat observable at a system boundary.

| Technique | Select when | Evidence and limits |
| --- | --- | --- |
| SAST / manual code review | Source and security-sensitive logic exist | Code findings; misses runtime configuration and some interactions |
| SCA / SBOM reconciliation | Dependencies are selected and updated | Component/version/advisory applicability; no advisory hit does not prove safety |
| DAST / authenticated abuse cases | A representative running system exists | Observed boundary behaviour; scope, identities and configuration constrain conclusions |
| Fuzzing | Parsers/protocols or other untrusted inputs exist | Input corpus, seeds, crashes, resource effects and triage; absence of crashes is not full security |
| Penetration testing | Exposure, threat model and potential harm justify adversarial assessment | Qualified independent assessment against explicit scope; no promise to discover every vulnerability |
| Update/recovery tests | Updates, rollback or recovery affect security or safety | Trust/authenticity, interrupted-update behaviour, compatibility and restored configuration |

The project records applicability, depth and rationale. Preserve any stricter testing practice already selected in the approved plan; do not reinterpret a method menu as permission to waive it. FDA guidance recommends methods; statutory duties such as FD&C 524B for cyber devices remain distinct. No single technique or score substitutes for the whole assessment.

## Prerequisites

Read scope and cyber-device determination from `intake`, the plan, assets, preliminary architecture, deployment assumptions, users/privileges and interfaces. Identify software/data/control flows, trust boundaries, dependencies and update/support arrangements. Before active testing, name the authorised non-production target, owner approval, identities, permitted operations, stop conditions and synthetic or anonymised data source. An owned-asset entry alone is not a test authorisation.

## Timing

Start assets and trust-boundary assumptions with needs and early design. Refine the model before architecture approval and whenever interfaces, permissions, suppliers or deployment assumptions change. Analyse code/dependencies during build; test running configurations at integration/system stages. Prepare update and vulnerability-response arrangements before release, pin the SBOM to the baseline, then monitor and reassess marketed configurations.

## Procedure

1. Draw the actual system boundary and flows, including services, users, devices and dependencies outside the app. State hostile-environment assumptions and multi-patient consequences where applicable.
2. For each flow/asset, derive threats and abuse cases, using the chosen method as prompts. Record affected asset, attacker precondition, entry point, undesirable action, impact and current controls.
3. Link patient/user safety consequences to risk paths. Keep security likelihood/exploitability separate from probability and severity of patient harm; CVSS is vulnerability severity, not risk acceptance.
4. Turn selected mitigations into verifiable requirements and design decisions. Test least-privileged and unauthorised identities, not only administrator success. Ask how a mitigation could fail or create a new safety risk.
5. Select tests from the table against the threats and requirements. Record scope, version, configuration, commands, logs and blocked/not-tested areas. Intrusive fuzzing, scanning, stress and attack runs never target production or copied customer data.
6. Reconcile the generated SBOM with built/deployed contents, including upstream, vendored and dynamically supplied components. CycloneDX or SPDX can support machine-readable exchange; the format is a project choice, not evidence of completeness. Identify unsupported/end-of-support components.
7. Triage each finding for affected component/version/configuration, reachability/exploit preconditions, available controls, safety impact and urgency. Record source/date, owner, decision and next review; an agent does not accept it. If using a VEX statement, name the issuer, product/version, status and justification; a not-affected assertion is not a blanket exemption.
8. Define intake, coordinated disclosure, monitoring, patch qualification/delivery and communication responsibilities. Link fixes to change control and regression evidence. Reopen threat and safety analyses when assumptions or exposure change.

### Threat and evidence worksheet

| Field | Enter |
| --- | --- |
| Scope | Asset, flow, boundary, deployment and revision |
| Threat | Actor/precondition, action, effect and optional safety-path reference |
| Requirement/control | Mechanism, implementing requirement/design, owner |
| Verification | Test/method, expected behaviour, target/data approval, revision, result/log or open gap |
| Disposition | Applicability, security and safety assessments, human decision, due/recheck date |

## Evidence

Maintain the model, assumptions, method selection, SBOM/baseline references, `FIND` records, test results and response plan. A security report reconciles threats to controls and verification, including gaps. Link to safety risk, configuration, maintenance and the submission/document owners rather than starting an isolated security project.

## Limitations

Automated scans cannot establish absence of vulnerabilities. SBOM presence does not establish anomaly evaluation or supplier qualification. Threat-model completeness, test adequacy and finding acceptance need competent human review; the structural record validator does not provide it. Do not manufacture reports or run unauthorised tests to fill a template.

## Human decisions

The security owner selects methods and resolves findings with the risk/clinical owner where safety is involved. Asset owners approve active tests and stop conditions. QA/RA decides release/submission consequences. People qualified in the target technology perform assessments requiring that expertise.

## Sources

- IEC 81001-5-1:2021, applicable lifecycle activities; MDR Annex I §§17.2, 17.4; FD&C Act §524B where applicable.
- FDA, Cybersecurity in Medical Devices (3 February 2026), threat modelling, SBOM and cybersecurity-testing sections. Recommendations are not all independent statutory duties.
- [NIST SP 800-218 v1.1](https://csrc.nist.gov/pubs/sp/800/218/final), PW.1, PW.4, PW.7, PW.8 and RV practices, as selectable secure-development guidance, not a medical-device classification rule.
- [Microsoft STRIDE threat guidance](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats), as method prompts, not medical-device obligations.

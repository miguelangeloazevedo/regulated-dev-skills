# Worked example: a signed update boundary

Fictional planning exercise. No scan, exploit, update test or human acceptance has been performed.

A device service accepts update packages from a network service. Assets include executable integrity and continued safe operation. The boundary is the untrusted delivery path into privileged installation. A threat-model assumption is that an attacker may control the network. An abuse case is a substituted or replayed package; interrupted installation is another condition to analyse, not necessarily an attack.

Proposed requirements specify signature/trust validation, supported-version rules and safe failure/recovery. The safety analysis asks whether an unavailable device or incompatible recovered state could delay treatment. Do not replace that harm analysis with a CVSS number.

Planned tests include a valid package, altered package, untrusted signer, replayed version and interrupted installation on a named isolated device simulator with synthetic configuration. The owner must approve the target and stop conditions first. Each result would name the tested baseline and retained logs. All results are **not run** in this example.

The configuration owner reconciles the package contents with the baseline SBOM. A library advisory requires applicability analysis on the actual version/path, not automatic acceptance or rejection based solely on a scanner label. The security owner and risk owner decide disposition; maintenance owns monitoring and response. Any newly granted install privilege returns to architecture, threat model and release review.

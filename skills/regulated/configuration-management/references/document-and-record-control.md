# Documents and completed records

## Identity and revisions

Classify the controlled content by purpose: a prescriptive document defines what shall be done; a completed record preserves evidence of what was done and decided. A test procedure and its executed result need different controls even if both use markdown. Mixed files need the applicable controls for both parts. This distinction is not a new frontmatter field or record type.

Maintain an enduring document identity separately from the particular content revision and its change authorisation. In standalone the identifier and git history can support this distinction, but a record ID does not identify an immutable revision by itself. Cite the exact revision/hash in approvals, baselines and evidence references. A CR authorises a change; it is not automatically a document-version record. Use existing supported links only and document mapping gaps.

## Approval, effectiveness and point of use

Identify who may author, review, approve and issue each document. Changes require approval by the original approving function or another suitably informed designated function. Show the change and exact revision before reapproval. Approval, scheduled effective date and actual issue for use are separate facts: approved is not automatically effective.

Where the QMS uses effective dates or prerequisites such as training, record the authorised date, conditions, responsible issuer and evidence that the transition actually occurred. Do not invent a universal training prerequisite. Identify the version currently authorised at each relevant point of use, including controlled distribution, external copies and offline instructions. Verify actual availability and prevent unintended use of obsolete versions. A git tag or successful export does not establish distribution, permissions or effective use. Product release and document issue are distinct decisions.

For external-origin documents needed by the QMS, retain identity, source, applicable edition, owner and distribution/update controls. An external URL does not by itself establish applicable version or continued availability.

## Review and obsolescence

Plan review triggers and responsibilities under the document procedure. Use periodic review where the QMS requires it, plus change, feedback and regulatory-source triggers. A periodic schedule is a procedure choice, not a universal interval imposed by ISO 13485. Record reviewer, revision examined, outcome, next trigger/date and actions. A review confirming continued suitability is not automatically a new content revision or renewed approval of different content.

Distinguish supersession by a named successor from obsolescence without replacement. Retain required obsolete copies, identify their status and prevent unintended operational use while allowing authorised historical retrieval. Do not create a fictional successor to satisfy tooling. Standalone status/successor conventions cannot represent every host obsolescence route; retain the controlled external reference and report the unsupported transition rather than falsify history or bypass approval rules.

## Completed records and corrections

Preserve the original observation, execution time, tested configuration, raw evidence and decision context. An incorrect result, anomaly or failed run remains part of the evidence. A later passing run is a new execution with its own TC/TR references, not an edit that turns the old failure into a pass.

Corrections/amendments identify what changed, the reason, who made it, when, authorisation/review as applicable and the original record/revision. Never overwrite or backdate the original evidence, impersonate the original signer, reuse a signature for changed content or rewrite repository history to hide a correction. Preserve the original signed content and approval references in controlled history. For a corrected rendition of the same record retain its identity and original revision reference; for a new execution allocate a new result ID. Use new approvals/signatures when required by the procedure, without altering the historical decision.

Standalone supplies no dedicated amendment relation or authenticated append-only audit trail. Do not invent frontmatter to simulate one. Use controlled body references to the preserved original revision and correction authority, supported links where semantically valid, and protected host history. If the record system cannot preserve/access the original evidence reliably, stop and raise a control gap. Hash staleness detection is not a correction audit trail or evidence authentication.

## Protection, retrieval and disposition

The plan/QMS boundary names owners and procedures for identification, storage, access/security, integrity, backup/recovery, legibility, retrieval, retention and authorised disposition. Protect confidential health information under applicable requirements; never export it into an unapproved repository or model service. Verify representative retrieval/readability and recovery from the controlled archive, not just existence of a pathname.

Set retention from applicable regulation and the organisation's defined device lifetime, with a documented basis. ISO 13485 4.2.5 requires record retention at least for the defined device lifetime or as specified by regulation, and not less than two years from the organisation's release of the device. This is a minimum, not a default deletion date. Clause 4.2.4 separately requires retention of at least one obsolete-document copy for its defined minimum period. Resolve applicable longer periods and related-record obligations with QA/RA. Legal holds, ongoing investigations and required evidence dependencies prevent routine disposal. Only authorised owners approve and record disposition; an agent never deletes retained evidence because a date elapsed.

These controls are not enforced by the standalone validator. Body worksheets and external references support human review; host protection, distribution, effective-date processing, periodic-review scheduling, retention and disposition require the project's controlled system/procedures.

## Sources

- ISO 13485:2016 4.2.4: control, approval, change, distribution and retention of documents.
- ISO 13485:2016 4.2.5: identification, integrity, protection, retrieval, identifiable changes, retention and disposition of records.
- IEC 62304:2006+A1:2015 clause 8 and 5.8.7: configuration control and archiving, subject to applicable class/edition.

This guide states repository working practices and QMS interfaces, not a claim that markdown/git is a validated document or record system.

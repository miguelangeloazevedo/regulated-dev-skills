"""Document/record method boundaries, not proof of host enforcement."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DocumentControlGuidance(unittest.TestCase):
    def test_lifecycle_and_record_corrections_are_distinct(self):
        base = ROOT / 'skills/regulated/configuration-management'
        skill = (base / 'SKILL.md').read_text()
        self.assertIn('references/document-and-record-control.md', skill)
        guide = (base / 'references/document-and-record-control.md').read_text()
        for term in ('## Identity and revisions', '## Approval, effectiveness and point of use',
                     '## Review and obsolescence', '## Completed records and corrections',
                     '## Protection, retrieval and disposition', 'not a new frontmatter',
                     'original observation', 'external-origin', 'periodic review',
                     'not enforced by the standalone validator'):
            self.assertIn(term, guide)
        for name in ('approve', 'release'):
            self.assertIn('approved is not automatically effective',
                          (ROOT / 'skills/gates' / name / 'SKILL.md').read_text())
        records = (ROOT / 'spec/records.md').read_text()
        self.assertIn('## Documents versus completed records', records)
        self.assertEqual(records, (ROOT / 'skills/gates/setup/scripts/RECORDS.md').read_text())
        backend = (ROOT / 'spec/backends.md').read_text()
        self.assertIn('## Document Control mapping', backend)
        self.assertIn('only standalone', backend.lower())

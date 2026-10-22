"""Content and packaging regressions, not evidence of QMS or regulatory adequacy."""
from pathlib import Path
import re
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MethodHandoffs(unittest.TestCase):
    def test_quality_event_disposition_is_not_just_a_green_regression(self):
        base = ROOT / 'skills/lifecycle/problem-resolution'
        skill = (base / 'SKILL.md').read_text()
        self.assertIn('references/quality-event-handoff.md', skill)
        process = skill.split('## Process', 1)[1].split('## AI/ML', 1)[0]
        self.assertLess(process.index('Assess interim protection'), process.index('Build a loop'))
        self.assertIn('justified no software change', process)
        self.assertIn('CAPA effectiveness', process)
        done = skill.split('## Done when', 1)[1].split('## See also', 1)[0]
        self.assertNotIn('- The loop was red and is green.', done)
        self.assertIn('authorised disposition', done)
        guide = (base / 'references/quality-event-handoff.md').read_text()
        for heading in ('Intake and interim protection', 'Investigation', 'Action and effectiveness',
                        'Closure and representation limits', 'Sources'):
            self.assertIn('## ' + heading, guide)
        for term in ('occurrence', 'escape', 'systemic', 'monitoring window',
                     'not represented', 'no adverse effect', 'reopen'):
            self.assertIn(term, guide)
        doc = (ROOT / 'docs/lifecycle/problem-resolution.md').read_text()
        self.assertIn('authorised disposition', doc)
        self.assertNotIn('before anyone theorises', doc)

    def test_risk_policy_and_calculation_do_not_stand_in_for_acceptance(self):
        base = ROOT / 'skills/regulated/risk'
        guide = (base / 'references/control-evidence.md').read_text()
        for term in ('## Policy, calculation and decision', 'policy revision',
                     'ordinal lookup', 'not human acceptance', 'reapproval',
                     'failed refresh', 'introduced path'):
            self.assertIn(term, guide)
        skill = (base / 'SKILL.md').read_text()
        self.assertIn('policy revision', skill)
        self.assertIn('reapproval', skill)
        analysis = (base / 'references/analysis-techniques.md').read_text()
        self.assertIn('applicability/exclusion register', analysis)
        self.assertIn('reconsideration trigger', analysis)

    def test_design_graph_roles_and_host_coverage_keep_their_meaning(self):
        skill = (ROOT / 'skills/regulated/traceability/SKILL.md').read_text()
        for term in ('type discriminators', 'relationship kind', 'stored direction'):
            self.assertIn(term, skill)
        guide = (ROOT / 'skills/regulated/traceability/references/chain-and-coverage.md').read_text()
        for term in ('host-defined structural metric', 'unique record identities',
                     'path occurrences', 'validation inventory', 'discovery evidence',
                     'correction verification', 'regression coverage', 'policy revision'):
            self.assertIn(term, guide)
        self.assertIn('not extra validator fields', guide)

    def test_backend_contract_discloses_all_three_mapping_boundaries(self):
        text = (ROOT / 'spec/backends.md').read_text()
        for heading in ('Design Control mapping', 'Quality Events mapping',
                        'Safety Risk traceability mapping', 'Approval capability and state reconciliation'):
            self.assertIn('## ' + heading, text)
        for term in ('per record type and gate', 'revision-bound', 'locked dependency versions',
                     'unrated or severity-only', 'no independent complaint',
                     'Do not fabricate', 'recalculation and reapproval'):
            self.assertIn(term, text)
        self.assertIn('Implemented in this version: `standalone` only', text)
        qity_row = next(line for line in text.splitlines() if line.startswith('| `qity`'))
        self.assertNotEqual(qity_row.split('|')[-2].strip(), '2')
        self.assertIn('per-record', qity_row)

    def test_quality_guide_survives_an_isolated_skill_install(self):
        source = ROOT / 'skills/lifecycle/problem-resolution'
        with tempfile.TemporaryDirectory(prefix='rds-quality-handoff-') as directory:
            target = Path(directory) / source.name
            shutil.copytree(source, target)
            references = set()
            for path in target.rglob('*.md'):
                for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                    if re.match(r'[a-z]+:', link) or link.startswith('#'):
                        continue
                    resolved = (path.parent / link.split('#', 1)[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(target.resolve()), str(path))
                    self.assertTrue(resolved.is_file(), str(resolved))
                    references.add(resolved.name)
            self.assertIn('quality-event-handoff.md', references)
            self.assertIn('worked-example.md', references)
            example = (target / 'references/worked-example.md').read_text()
            self.assertIn('Illustration only', example)
            self.assertIn('Not run', example)

    def test_record_guidance_keeps_quality_events_out_of_document_statuses(self):
        text = (ROOT / 'spec/records.md').read_text()
        self.assertIn('## Quality-event handoffs', text)
        self.assertIn('document approval is not event closure', text)
        self.assertIn('no independent complaint', text)
        bundled = (ROOT / 'skills/gates/setup/scripts/RECORDS.md').read_text()
        self.assertEqual(text, bundled)

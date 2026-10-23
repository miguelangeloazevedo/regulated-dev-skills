"""Assurance checks validate declarations, not the truth of a signature."""
import importlib.util
import json
import hashlib
import subprocess
import sys
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module():
    path = ROOT / 'tools/rds_assurance.py'
    if not path.exists():
        raise AssertionError('Assurance validation is not implemented')
    spec = importlib.util.spec_from_file_location('rds_assurance', path)
    assert spec is not None and spec.loader is not None
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


class AssuranceStates(unittest.TestCase):
    def test_critical_rule_register_preserves_class_and_authority_boundaries(self):
        data = json.loads((ROOT / 'assurance/regulatory-review.json').read_text())
        entries = {x['id']: x for x in data['items']}
        self.assertIn('62304-5.2.3', entries)
        self.assertEqual(entries['62304-5.2.3']['classes'], ['B', 'C'])
        self.assertEqual(entries['62304-5.2.4']['classes'], ['A', 'B', 'C'])
        self.assertEqual(entries['bc-result-signing']['basis'], 'repository_rule')
        self.assertIn('14971-control-effectiveness', entries)
        self.assertIn('no-automated-default', entries)
        self.assertTrue(all(x['review']['status'] == 'pending' for x in entries.values()))
        self.assertTrue(all(x['bindings'] for x in entries.values()))
        self.assertTrue(data['coverage']['unreviewed'])

    def test_public_views_and_cli_report_structure_not_authorisation(self):
        result = subprocess.run([sys.executable, str(ROOT / 'tools/rds_assurance.py'),
                                 'validate', '--root', str(ROOT)], capture_output=True, text=True)
        self.assertIn('structural_only', result.stdout)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        views = module().render_summary(ROOT)
        self.assertEqual(set(views), set(module().KINDS))
        self.assertIn('not authenticated', views['claims'])

    def test_completed_human_review_needs_matching_content_not_just_a_name(self):
        item = {'id': 'synthetic-human', 'scope': 'Synthetic fixture', 'status': 'declared',
                'bindings': [{'path': 'sample.md', 'sha256': hashlib.sha256(b'Synthetic test fixture\n').hexdigest()}],
                'review': {'status': 'completed', 'kind': 'human', 'by': 'Synthetic human',
                           'on': '2020-01-01', 'revision': 'a'*40, 'conclusion': 'Fixture only',
                           'evidence': 'https://example.org/synthetic-review'}}
        self.assertEqual(self.check_item(item), [])
        item['bindings'][0]['sha256'] = 'f'*64
        self.assertIn('ASSURANCE_STALE', self.check_item(item))

    def check_item(self, item, kind='claims'):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'assurance').mkdir()
            (root / 'sample.md').write_text('Synthetic test fixture\n')
            for name in ('claims', 'support', 'regulatory-review', 'record-system-assessment'):
                (root / 'assurance' / (name + '.json')).write_text(json.dumps({
                    'schema_version': 1, 'kind': name, 'items': [item] if name == kind else []}))
            return [x['code'] for x in module().validate_bundle(root)]

    def test_declaration_contract_rejects_invalid_or_unproven_states(self):
        base = {'id': 'synthetic-claim', 'scope': 'Synthetic fixture', 'status': 'declared',
                'review': {'status': 'pending'}}
        cases = [
            ({'status': 'verified'}, 'ASSURANCE_STATE'),
            ({'id': ''}, 'ASSURANCE_ID'),
            ({'scope': ''}, 'ASSURANCE_SCOPE'),
            ({'status': 'host_observed'}, 'ASSURANCE_MEASUREMENT'),
            ({'review': {'status': 'completed', 'kind': 'human', 'by': 'Synthetic reviewer'}},
             'ASSURANCE_REVIEW_EVIDENCE'),
            ({'review': {'status': 'pending', 'by': 'Invented reviewer', 'on': '2026-01-01'}},
             'ASSURANCE_PENDING_REVIEW'),
            ({'skills_revision': 'not-a-commit'}, 'ASSURANCE_REVISION'),
            ({'scope': '/Users/' + 'synthetic-fixture/cv.pdf'}, 'ASSURANCE_PRIVATE'),
            ({'observed_on': '2999-01-01T00:00:00+00:00'}, 'ASSURANCE_DATE'),
            ({'bindings': [{'path': 'sample.md', 'sha256': 'a' * 64}]}, 'ASSURANCE_STALE'),
            ({'bindings': [{'path': '../outside', 'sha256': 'a' * 64}]}, 'ASSURANCE_BINDING'),
        ]
        self.assertEqual(self.check_item(base), [])
        for change, code in cases:
            with self.subTest(code=code):
                self.assertIn(code, self.check_item(dict(base, **change)))

    def test_regulatory_source_needs_edition_and_public_locator(self):
        item = {'id': 'synthetic-rule', 'scope': 'Synthetic rule', 'status': 'declared',
                'basis': 'obligation', 'sources': [{'title': 'Synthetic standard'}]}
        self.assertIn('ASSURANCE_SOURCE', self.check_item(item, 'regulatory-review'))

    def test_boolean_does_not_validate_record_system(self):
        item = {'id': 'synthetic-system', 'scope': 'Synthetic only', 'status': 'declared',
                'assessment_status': 'accepted', 'record_system_validated': True}
        self.assertIn('ASSURANCE_SYSTEM_VALIDATION', self.check_item(item, 'record-system-assessment'))

    def test_broken_bundle_fails_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertIn('ASSURANCE_INPUT', [x['code'] for x in module().validate_bundle(Path(folder))])

    def test_automated_check_cannot_be_human_review(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'assurance').mkdir()
            item = {'id': 'synthetic-review', 'scope': 'Synthetic test only',
                    'status': 'declared', 'review': {
                        'status': 'completed', 'kind': 'automated',
                        'by': 'Synthetic checker'}}
            for kind in ('claims', 'support', 'regulatory-review', 'record-system-assessment'):
                (root / 'assurance' / (kind + '.json')).write_text(json.dumps({
                    'schema_version': 1, 'kind': kind, 'items': [item] if kind == 'claims' else []}))
            findings = module().validate_bundle(root)
            self.assertIn('ASSURANCE_REVIEW_KIND', [x['code'] for x in findings])


if __name__ == '__main__':
    unittest.main()

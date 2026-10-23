"""Assurance checks validate declarations, not the truth of a signature."""
import importlib.util
import json
import hashlib
import subprocess
import sys
import shutil
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
    def test_empty_review_is_rejected_before_summary_generation(self):
        item = {'id': 'synthetic-empty-review', 'scope': 'Synthetic fixture only',
                'status': 'declared', 'review': {}}
        self.assertIn('ASSURANCE_REVIEW_EVIDENCE', self.check_item(item))
        del item['review']
        self.assertEqual(self.check_item(item), [])
        item['review'] = {'status': 'pending'}
        self.assertEqual(self.check_item(item), [])

    def test_explicitly_stale_observation_keeps_historical_bindings_without_claiming_current_pass(self):
        item = {'id': 'synthetic-old', 'scope': 'Historical fixture, not a current pass', 'status': 'stale',
                'bindings': [{'path': 'sample.md', 'sha256': 'f'*64}]}
        self.assertEqual(self.check_item(item), [])
        item['status'] = 'declared'
        self.assertIn('ASSURANCE_STALE', self.check_item(item))

    def test_measurements_require_their_actual_configuration_identities(self):
        base = {'id': 'synthetic-observation', 'scope': 'Synthetic fixture only',
                'status': 'instruction_observed', 'skills_revision': 'a'*40,
                'observed_on': '2020-01-01', 'evidence': 'https://example.org/synthetic',
                'bindings': [{'path': 'sample.md', 'sha256': hashlib.sha256(b'Synthetic test fixture\n').hexdigest()}],
                'configuration': {'anything': True}}
        self.assertIn('ASSURANCE_CONFIGURATION', self.check_item(base))
        base['configuration'] = {'harness': 'Synthetic', 'harness_version': '1.0',
                                 'provider': 'Synthetic', 'model': 'Synthetic', 'model_version': '1.0'}
        self.assertEqual(self.check_item(base), [])
        base['status'] = 'host_observed'
        self.assertIn('ASSURANCE_CONFIGURATION', self.check_item(base))
        base['configuration'] = {'host': 'github.com', 'repository': 'synthetic-owner/synthetic-repo',
                                 'policy_revision': 'a'*40, 'workflow_revision': 'b'*40,
                                 'workflow': '.github/workflows/release.yml', 'credential': 'Synthetic read-only',
                                 'runner': 'Synthetic isolated runner'}
        self.assertEqual(self.check_item(base), [])
        base['configuration']['policy_revision'] = 'main'
        self.assertIn('ASSURANCE_CONFIGURATION', self.check_item(base))

    def test_accepted_system_assessment_requires_immutable_revision_and_bindings(self):
        item = {'id': 'synthetic-accepted', 'scope': 'Synthetic fixture only', 'status': 'declared',
                'assessment_status': 'accepted', 'record_system_validated': True, 'gaps': [],
                'controls': {k: 'assessed' for k in ('identity', 'authority', 'signature', 'audit_trail',
                                                   'integrity', 'correction', 'retention', 'retrieval')},
                'validation': {'intended_use': 'Synthetic test', 'revision': 'main',
                               'accepted_by': 'Synthetic person', 'accepted_on': '2020-01-01',
                               'evidence': 'https://example.org/synthetic'}}
        self.assertIn('ASSURANCE_SYSTEM_VALIDATION', self.check_item(item, 'record-system-assessment'))
        item['validation']['revision'] = 'a'*40
        self.assertIn('ASSURANCE_SYSTEM_VALIDATION', self.check_item(item, 'record-system-assessment'))
        item['bindings'] = [{'path': 'sample.md', 'sha256': hashlib.sha256(b'Synthetic test fixture\n').hexdigest()}]
        self.assertEqual(self.check_item(item, 'record-system-assessment'), [])

    def test_setup_bundle_and_invocation_guidance_survive_isolated_install(self):
        bundle = ROOT / 'skills/gates/setup/scripts'
        for name in ('rds_assurance.py', 'rds_github.py'):
            self.assertTrue((bundle / name).exists(), name)
            self.assertEqual((bundle / name).read_bytes(), (ROOT / 'tools' / name).read_bytes())
        self.assertEqual((bundle / 'ASSURANCE.md').read_bytes(), (ROOT / 'spec/assurance.md').read_bytes())
        for name in ('setup', 'intake', 'approve', 'release', 'impact', 'status'):
            text = (ROOT / 'skills/gates' / name / 'SKILL.md').read_text()
            self.assertIn('invocation control', text)
            self.assertIn('permission boundary', text)
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder)
            for name in ('rds_assurance.py', 'rds_github.py'):
                shutil.copy2(bundle / name, target / name)
            (target / 'assurance').mkdir()
            for kind in module().KINDS:
                (target / 'assurance' / (kind + '.json')).write_text(json.dumps({
                    'schema_version': 1, 'kind': kind, 'items': []}))
            result = subprocess.run([sys.executable, str(target / 'rds_assurance.py'),
                                     'validate', '--root', str(target)], capture_output=True, text=True, cwd=target)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('structural_only', result.stdout)

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
        self.assertIn('Review coverage', views['regulatory-review'])
        self.assertIn('**Basis:**', views['regulatory-review'])
        self.assertIn('**Content bindings:**', views['regulatory-review'])

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

"""Structural signing rules on isolated, fictional record fixtures only."""
import json
import re
import unittest
from pathlib import Path

import test_validate as fixtures


class SignaturePolicy(unittest.TestCase):
    d: str
    setUp = fixtures.Negative.setUp
    tearDown = fixtures.Negative.tearDown
    run_cmd = fixtures.Negative.run_cmd

    def test_class_a_requires_direct_signature(self):
        project = Path(self.d, 'r', fixtures.EX, 'AGENTS.md')
        original = project.read_text()
        result = Path(self.d, 'r', fixtures.REC, 'tr/TR-1.md')
        result.write_text(fixtures.drop_block('signed_by')(result.read_text()))
        for cls in ('A', 'B', 'C', '\n  display: A\n  unrelated: none'):
            with self.subTest(safety_class=cls):
                project.write_text(original.replace('safety_class: B', 'safety_class: ' + cls))
                run = self.run_cmd(fixtures.CMD)
                self.assertNotEqual(run.returncode, 0, run.stdout)
                self.assertIn('RDS220', run.stdout)

    def test_public_policy_and_signature_schema_are_consistent(self):
        root = Path(fixtures.ROOT)
        for path in ('spec/verification.md', 'spec/records.md', 'spec/assurance.md',
                     'skills/gates/intake/CLASS-OBLIGATIONS.md',
                     'skills/regulated/verify/SKILL.md', 'docs/regulated/verify.md',
                     'skills/gates/release/SKILL.md'):
            with self.subTest(path=path):
                text = (root / path).read_text()
                self.assertIn('A/B/C', text)
                self.assertIn('Part 11', text)
                self.assertIn('QMS', text)
        schema = json.loads((root / 'schemas/record.schema.json').read_text())
        signature = schema['properties']['signed_by']
        self.assertEqual(set(signature['required']), {'by', 'role', 'on', 'ref', 'revision'})

    def test_retired_results_do_not_satisfy_coverage_or_need_validation(self):
        project = Path(self.d, 'r', fixtures.MIN, 'AGENTS.md')
        project.write_text(project.read_text().replace('safety_class: A', 'safety_class: none'))
        results = [Path(self.d, 'r', fixtures.MIN, 'quality/records/tr', name + '.md') for name in ('TR-1', 'TR-2')]
        originals = [result.read_text() for result in results]
        for status in ('superseded', 'obsolete'):
            with self.subTest(status=status):
                for result, original in zip(results, originals):
                    text = original.replace('status: draft', 'status: ' + status)
                    if status == 'obsolete':
                        text = text.replace('as_of:', 'obsoleted_by: retained historical evidence\nas_of:')
                    result.write_text(text)
                    digest = self.run_cmd(['python3', 'tools/validate.py', 'hash', str(result)]).stdout.strip()
                    result.write_text(re.sub(r'  revision: [0-9a-f]+', '  revision: ' + digest, text))
                run = self.run_cmd(fixtures.MINCMD + ['--report'])
                report = json.JSONDecoder().raw_decode(run.stdout)[0]
                self.assertNotIn('SW-1', report['verified'])
                self.assertNotIn('RDS214', run.stdout)
                self.assertNotEqual(run.returncode, 0, run.stdout)
                self.assertIn('user need has no passing validation result', run.stdout)

    def test_malformed_hash_bound_result_is_not_current_evidence(self):
        for name in ('TR-1', 'TR-2'):
            result = Path(self.d, 'r', fixtures.MIN, 'quality/records/tr', name + '.md')
            result.write_text(result.read_text().replace('## Result', '## Removed result section'))
            digest = self.run_cmd(['python3', 'tools/validate.py', 'hash', str(result)]).stdout.strip()
            result.write_text(re.sub(r'  revision: [0-9a-f]+', '  revision: ' + digest, result.read_text()))
        run = self.run_cmd(fixtures.MINCMD + ['--report'])
        report = json.JSONDecoder().raw_decode(run.stdout)[0]
        self.assertIn('RDS210', run.stdout)
        self.assertNotIn('RDS220', run.stdout)
        self.assertNotIn('SW-1', report['verified'])
        self.assertIn('user need has no passing validation result', run.stdout)

    def test_duplicate_result_identity_is_not_current_evidence(self):
        source = Path(self.d, 'r', fixtures.MIN, 'quality/records/tr/TR-1.md')
        duplicate = source.parent.parent / 'synthetic-duplicate/TR-1.md'
        duplicate.parent.mkdir()
        duplicate.write_text(source.read_text())
        run = self.run_cmd(fixtures.MINCMD + ['--report'])
        report = json.JSONDecoder().raw_decode(run.stdout)[0]
        self.assertIn('RDS221', run.stdout)
        self.assertNotIn('SW-1', report['verified'])

    def test_metadata_cannot_clear_system_hold(self):
        project = Path(self.d, 'r', fixtures.MIN, 'AGENTS.md')
        original = project.read_text()
        for cls in ('A', 'B', 'C', '\n  display: A\n  unrelated: none'):
            for level in range(4):
                with self.subTest(safety_class=cls, evidence_level=level):
                    project.write_text(original.replace('safety_class: A', 'safety_class: ' + cls)
                                       .replace('evidence_level: 1', 'evidence_level: ' + str(level))
                                       .replace('intake:', 'record_system_validated: true\nintake:'))
                    run = self.run_cmd(fixtures.MINCMD + ['--report'])
                    report = json.JSONDecoder().raw_decode(run.stdout)[0]
                    self.assertNotEqual(run.returncode, 0)
                    self.assertIn('RDS425', run.stdout)
                    self.assertEqual(report['coverage_scope'], 'structural_only')
                    self.assertEqual(report['verification_acceptance']['state'], 'held')
                    self.assertEqual(report['accepted_verification_results'], [])
                    self.assertIn('SW-1', report['verified'])

    def test_release_requires_project_context(self):
        run = self.run_cmd(fixtures.CMD[:4] + ['--roles', fixtures.EX + '/quality/roles.yml', '--release'])
        self.assertNotEqual(run.returncode, 0)
        self.assertIn('RDS402', run.stdout)

    def test_invalid_signature_is_not_structural_coverage(self):
        result = Path(self.d, 'r', fixtures.REC, 'tr/TR-1.md')
        original = result.read_text()
        mutations = [
            fixtures.drop_block('signed_by')(original),
            original.replace('  by: carol', '  by: bob'),
            original.replace('  by: carol', '  by: mallory'),
            original.replace('  on: 2026-10-19', '  on: 2999-01-01'),
            original.replace('  on: 2026-10-19', '  on: 2026-02-30'),
            original.replace('authored_by: bob\n', ''),
            original.replace('built_by: bob\n', ''),
            original.replace('Pass. Red run', 'Edited. Red run'),
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                result.write_text(mutation)
                run = self.run_cmd(fixtures.CMD + ['--report'])
                report = json.JSONDecoder().raw_decode(run.stdout)[0]
                self.assertIn('RDS220', run.stdout)
                self.assertNotIn('SW-1', report['verified'])
                self.assertIn('TR-1', report['results_with_invalid_signature_declarations'])

    def test_required_signing_needs_roles_and_controlled_reference(self):
        run = self.run_cmd(fixtures.CMD[:4] + ['--project', fixtures.EX + '/AGENTS.md'])
        self.assertIn('RDS220', run.stdout)
        result = Path(self.d, 'r', fixtures.REC, 'tr/TR-1.md')
        result.write_text(re.sub(r'  ref: .*\n', '', result.read_text()))
        run = self.run_cmd(fixtures.CMD)
        self.assertIn('RDS220', run.stdout)

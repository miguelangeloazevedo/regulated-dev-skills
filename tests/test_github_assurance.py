"""Synthetic snapshots test decisions, not actual host-control outcomes."""
import copy
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch
from types import SimpleNamespace
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SHA = 'a' * 40


def module():
    path = ROOT / 'tools/rds_github.py'
    if not path.exists():
        raise AssertionError('Trusted host evaluator is not implemented')
    spec = importlib.util.spec_from_file_location('rds_github', path)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def policy():
    return {'repository': 'synthetic-owner/synthetic-repo', 'branch': 'main',
            'environment': 'synthetic-release', 'reviewer_ids': [2],
            'policy_commit': SHA, 'workflow_path': '.github/workflows/release.yml'}


def facts():
    return {'repository': {'full_name': 'synthetic-owner/synthetic-repo', 'visibility': 'public', 'default_branch': 'main'},
            'policy_commit': SHA, 'final_policy_commit': SHA,
            'protection': {'enforce_admins': {'enabled': True}, 'allow_force_pushes': {'enabled': False},
                           'allow_deletions': {'enabled': False}, 'required_pull_request_reviews': {
                               'required_approving_review_count': 1, 'dismiss_stale_reviews': True,
                               'require_code_owner_reviews': True, 'bypass_pull_request_allowances': {}}},
            'pr': {'number': 1, 'state': 'open', 'draft': False, 'mergeable_state': 'clean', 'user': {'id': 1},
                   'head': {'sha': SHA, 'repo': {'full_name': 'synthetic-owner/synthetic-repo'}},
                   'base': {'ref': 'main', 'repo': {'full_name': 'synthetic-owner/synthetic-repo'}}},
            'final_head': SHA,
            'reviews': [{'id': 10, 'user': {'id': 2, 'type': 'User'}, 'state': 'APPROVED', 'commit_id': SHA}],
            'environment': {'name': 'synthetic-release', 'can_admins_bypass': False,
                            'deployment_branch_policy': {'protected_branches': True, 'custom_branch_policies': False},
                            'protection_rules': [{'type': 'required_reviewers', 'prevent_self_review': True,
                                                  'reviewers': [{'type': 'User', 'reviewer': {'id': 2}}]}]},
            'policy_document': {k: v for k, v in policy().items() if k != 'policy_commit'},
            'rulesets': [], 'workflow_permissions': {'default_workflow_permissions': 'read'},
            'complete': True}


class HostAuthority(unittest.TestCase):
    def test_cli_does_not_treat_local_admin_environment_as_isolated_host(self):
        env = dict(os.environ)
        env.pop('GITHUB_ACTIONS', None)
        result = subprocess.run([sys.executable, str(ROOT / 'tools/rds_assurance.py'),
                                 'github-preflight', '--repo', 'synthetic-owner/synthetic-repo',
                                 '--commit', SHA, '--pr', '1', '--environment', 'synthetic-release',
                                 '--policy', 'not-read-in-untrusted-context.json', '--policy-commit', SHA],
                                env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn('HOST_CONTEXT', result.stdout)

    def test_local_policy_cannot_override_protected_remote_policy(self):
        data = facts()
        data['policy_document']['reviewer_ids'] = [123]
        self.assertIn('POLICY_MISMATCH', module().evaluate_github(policy(), data, SHA, 1)['reasons'])

    def test_host_required_review_count_and_mergeability_are_honoured(self):
        for change in [lambda f: f['protection']['required_pull_request_reviews'].update(required_approving_review_count=2),
                       lambda f: f['pr'].update(mergeable_state='blocked')]:
            data = facts()
            change(data)
            self.assertEqual(module().evaluate_github(policy(), data, SHA, 1)['status'], 'blocked')

    def test_collector_reads_live_paths_and_rechecks_moving_state(self):
        mod = module()
        self.assertTrue(hasattr(mod, 'collect_github'), 'Live collector is missing')
        seen = []
        synthetic = facts()

        def transport(path, paginate=False):
            seen.append(path)
            if path.endswith('/protection'):
                return synthetic['protection']
            if '/branches/' in path:
                return {'commit': {'sha': SHA}}
            if path.endswith('/reviews'):
                return synthetic['reviews']
            if path.endswith('/pulls/1'):
                return synthetic['pr']
            if '/environments/' in path:
                return synthetic['environment']
            if path.endswith('/rulesets'):
                return []
            if path.endswith('/permissions/workflow'):
                return synthetic['workflow_permissions']
            if '/contents/' in path:
                import base64
                return {'encoding': 'base64', 'content': base64.b64encode(b'{}').decode()}
            return synthetic['repository']

        result = mod.collect_github('synthetic-owner/synthetic-repo', 1, 'synthetic-release', read=transport)
        self.assertTrue(result['complete'])
        self.assertGreaterEqual(seen.count('repos/synthetic-owner/synthetic-repo/pulls/1'), 2)
        self.assertGreaterEqual(seen.count('repos/synthetic-owner/synthetic-repo/branches/main/protection'), 2)
        self.assertEqual(result['final_head'], SHA)
        self.assertTrue(result['observed_on'])

    def test_collector_rejects_bad_inputs_before_network(self):
        mod = module()
        self.assertTrue(hasattr(mod, 'collect_github'), 'Live collector is missing')
        for repo in ['synthetic/repo\n', 'https://example.org', 'owner/repo/../other']:
            with self.assertRaises(mod.HostReadError):
                mod.collect_github(repo, 1, 'synthetic-release', read=lambda *a, **k: self.fail('Network must not be used'))

    def test_gh_transport_flattens_all_pages_and_does_not_echo_errors(self):
        mod = module()
        self.assertTrue(hasattr(mod, '_api'), 'Live transport is missing')
        with patch.object(mod.subprocess, 'run', return_value=SimpleNamespace(returncode=0, stdout='[[{"id":1}],[{"id":2}]]')) as run:
            self.assertEqual(mod._api('repos/owner/repo/pulls/1/reviews', paginate=True), [{'id': 1}, {'id': 2}])
            self.assertIn('--paginate', run.call_args[0][0])
            self.assertIn('--slurp', run.call_args[0][0])
            self.assertIn('GET', run.call_args[0][0])
        with patch.object(mod.subprocess, 'run', return_value=SimpleNamespace(returncode=1, stdout='sensitive response')):
            with self.assertRaises(mod.HostReadError) as error:
                mod._api('repos/owner/repo')
            self.assertNotIn('sensitive', str(error.exception))

    def test_host_predicates_fail_closed_for_unsafe_or_incomplete_facts(self):
        mutations = [
            (lambda f: f.update(complete=False), 'INCOMPLETE_FACTS'),
            (lambda f: f['repository'].update(full_name='other/repo'), 'REPOSITORY_MISMATCH'),
            (lambda f: f.update(final_head='b'*40), 'HEAD_MOVED'),
            (lambda f: f.update(final_policy_commit='b'*40), 'POLICY_MOVED'),
            (lambda f: f['reviews'][0]['user'].update(id=1), 'APPROVAL_AUTHORITY'),
            (lambda f: f['reviews'][0]['user'].update(type='Bot'), 'APPROVAL_AUTHORITY'),
            (lambda f: f['reviews'][0].update(state='DISMISSED'), 'APPROVAL_AUTHORITY'),
            (lambda f: f['protection']['enforce_admins'].update(enabled=False), 'BRANCH_PROTECTION'),
            (lambda f: f['protection']['allow_force_pushes'].update(enabled=True), 'BRANCH_PROTECTION'),
            (lambda f: f['protection']['required_pull_request_reviews'].update(bypass_pull_request_allowances={'users': [{'id': 2}]}), 'BRANCH_PROTECTION'),
            (lambda f: f['environment'].update(can_admins_bypass=True), 'ENVIRONMENT_PROTECTION'),
            (lambda f: f['environment']['protection_rules'][0].update(prevent_self_review=False), 'ENVIRONMENT_PROTECTION'),
            (lambda f: f['workflow_permissions'].update(default_workflow_permissions='write'), 'WORKFLOW_PERMISSIONS'),
            (lambda f: f.update(rulesets=[{'enforcement': 'active', 'bypass_actors': [{'actor_id': 1}]}]), 'RULESET_BYPASS'),
        ]
        for change, reason in mutations:
            with self.subTest(reason=reason):
                data = facts()
                change(data)
                result = module().evaluate_github(policy(), data, SHA, 1)
                self.assertEqual(result['status'], 'blocked')
                self.assertIn(reason, result['reasons'])

    def test_later_changes_requested_cannot_be_hidden_by_old_approval(self):
        data = facts()
        data['reviews'].append({'id': 11, 'user': {'id': 2, 'type': 'User'},
                                'state': 'CHANGES_REQUESTED', 'commit_id': SHA})
        self.assertEqual(module().evaluate_github(policy(), data, SHA, 1)['status'], 'blocked')

    def test_malformed_identifiers_are_rejected_not_normalised(self):
        for commit in ['main', 'A'*40, SHA + '\n']:
            self.assertEqual(module().evaluate_github(policy(), facts(), commit, 1)['status'], 'blocked')

    def test_exact_approved_revision_passes_and_wrong_revision_fails(self):
        result = module().evaluate_github(policy(), facts(), SHA, 1)
        self.assertEqual(result['status'], 'eligible', result)
        changed = facts()
        changed['reviews'][0]['commit_id'] = 'b' * 40
        result = module().evaluate_github(policy(), changed, SHA, 1)
        self.assertEqual(result['status'], 'blocked')
        self.assertIn('APPROVAL_COMMIT_MISMATCH', result['reasons'])


if __name__ == '__main__':
    unittest.main()

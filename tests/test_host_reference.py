"""Reference probes are confined to a named synthetic public sandbox."""
import importlib.util
from pathlib import Path
import unittest
import sys
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EX = ROOT / 'examples/host-enforced'


def module():
    path = EX / 'probe_permissions.py'
    if not path.exists():
        raise AssertionError('Synthetic probe harness is missing')
    spec = importlib.util.spec_from_file_location('probe_permissions', path)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class ReferenceBoundary(unittest.TestCase):
    def test_probe_detects_changed_review_beyond_the_first_page(self):
        mod = module()
        changed = [False]
        repo = mod.APPROVED_SANDBOX

        def transport(method, path, payload=None):
            if method != 'GET':
                if path.endswith('/reviews'):
                    changed[0] = True
                return 403, None
            if path == 'repos/' + repo:
                return 200, {'full_name': repo, 'visibility': 'public'}
            if path.endswith('/pulls/1'):
                return 200, {'head': {'sha': 'a'*40, 'repo': {'full_name': repo}}}
            if '/reviews?' in path:
                page = int(parse_qs(urlsplit(path).query).get('page', ['1'])[0])
                values = [{'id': i} for i in range(101 + int(changed[0]))]
                return 200, values[(page-1)*100:page*100]
            if '/contents/' in path:
                return 200, {'sha': 'b'*40, 'content': 'e30='}
            return 200, []

        with self.assertRaisesRegex(RuntimeError, 'target_changed'):
            mod.probe(repo, 1, 'a'*40, '1', request=transport)

    def test_controller_creates_only_a_fixed_synthetic_request(self):
        path = EX / 'controller.py'
        self.assertTrue(path.exists(), 'Synthetic controller is missing')
        sys.path.insert(0, str(EX))
        try:
            spec = importlib.util.spec_from_file_location('synthetic_controller', path)
            assert spec and spec.loader
            loaded = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(loaded)
        finally:
            sys.path.remove(str(EX))
        writes = []
        repo = module().APPROVED_SANDBOX

        def transport(method, path, payload=None):
            if method != 'GET':
                writes.append((method, path, payload))
            if path == 'repos/' + repo:
                return 200, {'full_name': repo, 'visibility': 'public'}
            if path.endswith('/branches/main'):
                return 200, {'commit': {'sha': 'a'*40}}
            if '/contents/' in path and method == 'GET':
                return 200, {'sha': 'a'*40}
            if method == 'PUT':
                return 200, {'commit': {'sha': 'b'*40}}
            if path.endswith('/pulls'):
                return 201, {'number': 1, 'html_url': 'https://example.org/synthetic-request'}
            if path.endswith('/dispatches'):
                return 204, None
            return 201, {}

        result = loaded.prepare(repo, '123', request=transport)
        self.assertEqual(result['commit'], 'b'*40)
        self.assertEqual(result['pr'], 1)
        self.assertFalse(any(path.endswith('/releases') for _, path, _ in writes))
        with self.assertRaises(ValueError):
            loaded.prepare('other/production', '123', request=lambda *a: self.fail('No network'))
        with self.assertRaises(RuntimeError):
            loaded.publish(repo, 1, 'a'*40, '123', 'a'*40,
                           request=lambda *a: self.fail('No release without authority'),
                           authorise=lambda: {'status': 'blocked'})

    def test_only_real_permission_denial_with_unchanged_target_passes(self):
        mod = module()
        self.assertEqual(mod.classify(403, {'sha': 'same'}, {'sha': 'same'}), 'denied')
        for status in (401, 404, 422, 500):
            self.assertEqual(mod.classify(status, {}, {}), 'inconclusive')
        self.assertEqual(mod.classify(201, {}, {}), 'unexpected_success')
        self.assertEqual(mod.classify(403, {'sha': 'old'}, {'sha': 'new'}), 'target_changed')

    def test_other_repositories_are_rejected_before_network(self):
        mod = module()
        with self.assertRaises(ValueError):
            mod.probe('other/production', 1, 'a'*40, '1', request=lambda *a: self.fail('No network'))

    def test_reference_templates_keep_drafting_and_release_separate(self):
        for name in ('probe.yml', 'release.yml', 'controller.yml'):
            path = EX / 'workflows' / name
            self.assertTrue(path.exists(), name)
            text = path.read_text()
            for forbidden in ('pull_request_target', 'permissions: write-all', 'persist-credentials: true', 'secrets: inherit'):
                self.assertNotIn(forbidden, text)
            self.assertIn('persist-credentials: false', text)
        probe = (EX / 'workflows/probe.yml').read_text()
        self.assertIn('contents: read', probe)
        self.assertNotIn('contents: write', probe)
        self.assertNotIn('secrets.', probe)
        release = (EX / 'workflows/release.yml').read_text()
        self.assertIn('environment: synthetic-release', release)
        self.assertIn('github-preflight', release)
        self.assertEqual(release.count('RDS_HOST_READ_TOKEN: ${{ secrets.RDS_HOST_READ_TOKEN }}'), 2)
        self.assertIn('ref: ${{ github.sha }}', release)
        self.assertNotIn('ref: ${{ inputs.commit }}', release)


if __name__ == '__main__':
    unittest.main()

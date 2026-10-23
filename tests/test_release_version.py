"""Package maturity does not imply completed regulatory review."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReleaseVersion(unittest.TestCase):
    def test_non_prerelease_version_and_install_pin_match(self):
        plugin = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
        self.assertEqual(plugin['version'], '0.2.0')
        readme = (ROOT / 'README.md').read_text()
        self.assertIn('git clone --branch v0.2.0 ', readme)
        self.assertIn('## 0.2.0\n', (ROOT / 'CHANGELOG.md').read_text())
        for path in (ROOT / 'skills').glob('*/*/SKILL.md'):
            text = path.read_text()
            self.assertIn('  status: draft\n', text)
            self.assertIn('  reviewed_on: none\n', text)


if __name__ == '__main__':
    unittest.main()

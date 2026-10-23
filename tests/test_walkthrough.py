"""Exercise the first-change guide's shell commands on fictional fixtures only."""
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "examples/minimal-release/FIRST-CHANGE.md"


class FirstChangeWalkthrough(unittest.TestCase):
    def test_documented_checkpoints(self):
        self.assertTrue(GUIDE.is_file(), "the first-change walkthrough is missing")
        blocks = re.findall(r"^```bash\n(.*?)^```", GUIDE.read_text(), re.M | re.S)
        self.assertEqual(len(blocks), 5, "setup, baseline, edit, warnings, release")
        source = ROOT / "examples/minimal-release"
        before = {p.relative_to(source): p.read_bytes()
                  for p in source.rglob("*") if p.is_file()}
        with tempfile.TemporaryDirectory(prefix="rds-walkthrough-test-") as work:
            env = dict(os.environ, RDS_WALKTHROUGH=work)
            env.pop("RDS_BASELINE_UNCHECKED", None)
            outputs = []
            for index, block in enumerate(blocks):
                result = subprocess.run(["bash", "-eu", "-c", block], cwd=ROOT,
                                        env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode, 1 if index == 4 else 0,
                                 result.stdout + result.stderr)
                outputs.append(result.stdout)
            self.assertIn("0 error(s), 0 warning(s)", outputs[1])
            self.assertIn("RDS218", outputs[3])
            self.assertIn("STALE", outputs[3])
            self.assertIn("RDS222", outputs[3])
            self.assertIn("SUSPECT", outputs[3])
            self.assertIn("RDS401", outputs[4])
            self.assertIn("RDS425", outputs[4])
            self.assertIn('"accepted_verification_results": []', outputs[1])
            record = Path(work) / "project/quality/records/sw/SW-1.md"
            self.assertIn('"No entries scheduled for today."', record.read_text())
            self.assertIn("ref: example", record.read_text())
        after = {p.relative_to(source): p.read_bytes()
                 for p in source.rglob("*") if p.is_file()}
        self.assertEqual(before, after, "the original fixture must not change")

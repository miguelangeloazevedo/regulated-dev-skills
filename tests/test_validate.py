import re
"""Negative tests: each mutation of the worked example must be refused with its code.

Run: python3 -m unittest discover -s tests
"""
import os, re, shutil, subprocess, tempfile, unittest


def _read(p):
    with open(p) as f:
        return f.read()


def _write(p, s):
    with open(p, "w") as f:
        f.write(s)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EX = "examples/infusion-rate-check"
CMD = ["python3", "tools/validate.py", "records", EX + "/quality", "--roles", EX + "/quality/roles.yml", "--project", EX + "/AGENTS.md"]
REC = EX + "/quality/records/"
MIN = "examples/minimal-release"
MINCMD = ["python3", "tools/validate.py", "records", MIN + "/quality", "--roles", MIN + "/quality/roles.yml", "--project", MIN + "/AGENTS.md", "--release", "--baseline", "7c2d1e0"]


def drop_block(key):
    return lambda s: re.sub(key + r":\n(  .*\n)+", "", s)


CASES = [
    ("approval goes stale on any edit (a warning, by design)", REC + "sw/SW-1.md", lambda s: s.replace("disable the start command", "grey out the start command"), "STALE"),
    ("unsigned result at class B", REC + "tr/TR-1.md", drop_block("signed_by"), "RDS220"),
    ("builder signs own result", REC + "tr/TR-1.md", lambda s: s.replace("  by: carol", "  by: bob"), "RDS220"),
    ("level 3 without validated record system", EX + "/AGENTS.md", lambda s: s.replace("evidence_level: 0", "evidence_level: 3"), "RDS307"),
    ("software requirement with no parent", REC + "sw/SW-2.md", lambda s: s.replace("derives_from: [SYS-1, SYS-2]\n", ""), "RDS208"),
    ("approved record without author", REC + "un/UN-1.md", lambda s: s.replace("authored_by: bob\n", ""), "RDS216"),
    ("hazard missing its hazardous situation", REC + "haz/HAZ-1.md", lambda s: s.replace("## Hazardous situation", "## Notes"), "RDS"),
    ("link to a record that does not exist", REC + "tc/TC-1.md", lambda s: s.replace("verifies: [SW-1]", "verifies: [SW-9]"), "RDS"),
    ("result edited after signing", REC + "tr/TR-1.md", lambda s: s.replace("Pass. Red run", "Pass after rerun. Red run"), "RDS220"),
    ("parent edited after child approval makes child suspect (a warning)", REC + "sys/SYS-1.md", lambda s: s.replace("shall warn and require", "shall warn, log and require"), "SUSPECT"),
    ("per-system class map: unsigned result in a class C system", REC + "tr/TR-1.md", lambda s: drop_block("signed_by")(s).replace("outcome: pass", "outcome: pass\nsystem: dose-engine"), "RDS220"),
    ("no class decided: warns, never defaults", EX + "/AGENTS.md", lambda s: s.replace("safety_class: B\n", ""), "RDS311"),
    ("not-a-device project rejects an invalid class value", EX + "/AGENTS.md", lambda s: s.replace("safety_class: B", "safety_class: D"), "RDS310"),
    ("signer not in roles file", REC + "tr/TR-1.md", lambda s: s.replace("  by: carol", "  by: mallory"), "RDS220"),
    ("empty required section", REC + "haz/HAZ-1.md", lambda s: re.sub(r"## Harm\n.*", "## Harm\n", s, flags=re.S), "RDS210"),
    ("author approves own record", REC + "sw/SW-1.md", lambda s: s.replace("  by: carol", "  by: bob"), "RDS"),
]


class Negative(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        shutil.copytree(ROOT, self.d + "/r", ignore=shutil.ignore_patterns(".git"))

    def tearDown(self):
        shutil.rmtree(self.d)

    def run_cmd(self, cmd):
        return subprocess.run(cmd, cwd=self.d + "/r", capture_output=True, text=True)

    def test_example_is_clean(self):
        r = self.run_cmd(CMD)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_no_class_never_demands_signature(self):
        fp = self.d + "/r/" + EX + "/AGENTS.md"
        s = _read(fp).replace("safety_class: B\n", "")
        _write(fp, s)
        tr = self.d + "/r/" + REC + "tr/TR-1.md"
        s = re.sub(r"signed_by:\n(  .*\n)+", "", _read(tr))
        _write(tr, s)
        r = self.run_cmd(CMD)
        self.assertNotIn("RDS201", r.stdout)
        self.assertNotIn("RDS220", r.stdout)
        self.assertIn("RDS311", r.stdout)

    def test_none_class_runs_without_signature_rule(self):
        fp = self.d + "/r/" + EX + "/AGENTS.md"
        s = _read(fp).replace("safety_class: B", "safety_class: none")
        _write(fp, s)
        tr = self.d + "/r/" + REC + "tr/TR-1.md"
        s = re.sub(r"signed_by:\n(  .*\n)+", "", _read(tr))
        _write(tr, s)
        r = self.run_cmd(CMD)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_failed_result_is_not_coverage(self):
        import json as _j
        tr = self.d + "/r/" + REC + "tr/TR-1.md"
        s = _read(tr).replace("outcome: pass", "outcome: fail")
        _write(tr, s)
        r = self.run_cmd(CMD + ["--report"])
        rep = _j.loads(r.stdout[:r.stdout.rindex("}") + 1])
        self.assertNotIn("SW-1", rep["verified"])
        self.assertIn("SW-1", rep["linked_but_unverified"])

    def test_release_gate_blocks_example(self):
        r = self.run_cmd(CMD + ["--release"])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("RDS401", r.stdout)

    def test_release_gate_needs_decided_class_when_62304_claimed(self):
        fp = self.d + "/r/" + EX + "/AGENTS.md"
        s = _read(fp).replace("safety_class: B\n", "")
        _write(fp, s)
        r = self.run_cmd(CMD + ["--release"])
        self.assertIn("RDS402", r.stdout)

    def test_release_gate_needs_decided_class_without_62304_claim(self):
        fp = self.d + "/r/" + MIN + "/AGENTS.md"
        s = _read(fp)
        s = re.sub(r"safety_class: [^\n]*\n", "", s)
        s = re.sub(r"standards: \[[^\]]*\]", "standards: []", s)
        _write(fp, s)
        r = self.run_cmd(MINCMD)
        self.assertIn("RDS402", r.stdout)
        self.assertNotIn("IEC 62304 is claimed", r.stdout)

    def test_release_refuses_classification_past_recheck(self):
        fp = self.d + "/r/" + MIN + "/quality/records/cls/CLS-1.md"
        _write(fp, _read(fp).replace("as_of: 2026-10-19\n", "as_of: 2026-10-19\nrecheck_by: 2000-01-01\n", 1))
        r = self.run_cmd(MINCMD)
        self.assertIn("RDS412", r.stdout)

    def test_result_on_wrong_baseline(self):
        r = self.run_cmd(CMD + ["--release", "--baseline", "deadbeef"])
        self.assertIn("RDS404", r.stdout)

    def test_minimal_example_structural_success_cannot_authorise_release(self):
        r = self.run_cmd(MINCMD)
        self.assertNotEqual(r.returncode, 0, r.stdout)
        self.assertIn("RDS425", r.stdout)
        self.assertNotIn("RDS220", r.stdout)

    def test_draft_record_blocks_release(self):
        fp = self.d + "/r/" + MIN + "/quality/records/sw/SW-1.md"
        s = re.sub(r"approval:\n(  .*\n)+", "", _read(fp)).replace("status: approved", "status: draft")
        _write(fp, s)
        r = self.run_cmd(MINCMD)
        self.assertIn("RDS406", r.stdout)

    def test_status_flip_with_approval_is_refused(self):
        fp = self.d + "/r/" + MIN + "/quality/records/sw/SW-1.md"
        _write(fp, _read(fp).replace("status: approved", "status: proposed"))
        r = self.run_cmd(MINCMD)
        self.assertIn("RDS214", r.stdout)

    def test_report_cannot_substitute_direct_result_signature(self):
        import sys as _s
        _s.path.insert(0, self.d + "/r/tools")
        import importlib, validate as V
        importlib.reload(V)
        tr = self.d + "/r/" + REC + "tr/TR-1.md"
        s = re.sub(r"signed_by:\n(  .*\n)+", "", _read(tr)).replace("outcome: pass", "outcome: pass\ncovered_by: VRP-1")
        _write(tr, s)
        h = V.revision_hash(s)
        os.makedirs(self.d + "/r/" + REC + "vrp", exist_ok=True)
        vrp = "---\nid: VRP-1\ntype: vrp\ntitle: Verification report\nstatus: draft\nauthored_by: bob\nsigned_by:\n  by: carol\n  role: engineering\n  on: 2026-10-19\nas_of: 2026-10-19\n---\n\n## Scope\nTC-1.\n\n## Results\n- TR-1 %s pass\n\n## Conclusion\nPass.\n" % h
        vh = V.revision_hash(vrp)
        vrp = vrp.replace("  on: 2026-10-19\n", "  on: 2026-10-19\n  revision: %s\n" % vh, 1)
        _write(self.d + "/r/" + REC + "vrp/VRP-1.md", vrp)
        r = self.run_cmd(CMD)
        self.assertNotEqual(r.returncode, 0, r.stdout)
        self.assertIn("RDS220", r.stdout)

    def test_level_0_blocks_release(self):
        fp = self.d + "/r/" + MIN + "/AGENTS.md"
        _write(fp, _read(fp).replace("evidence_level: 1", "evidence_level: 0"))
        r = self.run_cmd(MINCMD)
        self.assertIn("RDS408", r.stdout)

    def test_missing_qms_owner_blocks_release(self):
        fp = self.d + "/r/" + MIN + "/quality/records/plan/PLAN-1.md"
        _write(fp, _read(fp).replace("owner: alice, CAPA procedure", "owner: tbd"))
        r = self.run_cmd(MINCMD)
        self.assertIn("RDS409", r.stdout)

    def test_draft_review_blocks_release(self):
        fp = self.d + "/r/" + MIN + "/quality/records/rev/REV-1.md"
        _write(fp, re.sub(r"approval:\n(  .*\n)+", "", _read(fp)).replace("status: approved", "status: draft"))
        r = self.run_cmd(MINCMD)
        self.assertIn("RDS406", r.stdout)

    def test_future_approval_date(self):
        fp = self.d + "/r/" + MIN + "/quality/records/sw/SW-1.md"
        _write(fp, _read(fp).replace("  on: 2026-10-19", "  on: 2999-01-01"))
        r = self.run_cmd(MINCMD)
        self.assertIn("RDS223", r.stdout)

    def test_approval_before_record_date(self):
        fp = self.d + "/r/" + MIN + "/quality/records/sw/SW-1.md"
        _write(fp, _read(fp).replace("  on: 2026-10-19", "  on: 2000-01-01"))
        r = self.run_cmd(MINCMD)
        self.assertIn("RDS223", r.stdout)

    def test_duplicate_id(self):
        shutil.copy(self.d + "/r/" + REC + "sw/SW-1.md", self.d + "/r/" + REC + "sw/SW-1-copy.md")
        r = self.run_cmd(CMD)
        self.assertIn("RDS221", r.stdout)

    def test_bundled_validator_matches(self):
        with open(self.d + "/r/skills/gates/setup/scripts/validate.py", "a") as f:
            f.write("\n# drift\n")
        r = self.run_cmd(["python3", "tools/validate.py", "repo"])
        self.assertIn("RDS170", r.stdout)


def make(name, path, fn, code):
    def t(self):
        fp = self.d + "/r/" + path
        s = _read(fp); s2 = fn(s)
        self.assertNotEqual(s, s2, "mutation did not apply: " + name)
        _write(fp, s2)
        r = self.run_cmd(CMD)
        if code not in ("STALE", "SUSPECT", "RDS311"):
            self.assertNotEqual(r.returncode, 0, name + "\n" + r.stdout)
        self.assertIn(code, r.stdout, name)
    return t


for i, (name, path, fn, code) in enumerate(CASES):
    setattr(Negative, "test_%02d_%s" % (i, re.sub(r"\W+", "_", name)), make(name, path, fn, code))

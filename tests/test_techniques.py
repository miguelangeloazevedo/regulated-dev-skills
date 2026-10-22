"""Structural checks for packaged method guidance, not regulatory adequacy tests."""
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
GUIDES = {
    "risk": "analysis-techniques.md",
    "security-diligence": "threat-model-and-testing.md",
    "verify": "test-design.md",
    "traceability": "chain-and-coverage.md",
    "configuration-management": "baseline-and-change-control.md",
    "package": "evidence-package.md",
}
HEADINGS = ("Selection", "Prerequisites", "Timing", "Procedure", "Evidence",
            "Limitations", "Human decisions", "Sources")


def local_links(text):
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if not re.match(r"[a-z]+:", target) and not target.startswith("#"):
            yield target.split("#", 1)[0]


class PackagedTechniques(unittest.TestCase):
    def test_guidance_contract(self):
        actual = {p.parent.name for p in (ROOT / "skills/regulated").glob("*/SKILL.md")}
        self.assertEqual(actual, set(GUIDES))
        for name, guide in GUIDES.items():
            with self.subTest(skill=name):
                base = ROOT / "skills/regulated" / name
                text = (base / "SKILL.md").read_text()
                self.assertIn("references/" + guide, text)
                self.assertIn("references/worked-example.md", text)
                path = base / "references" / guide
                content = path.read_text()
                for heading in HEADINGS:
                    self.assertIn("## " + heading + "\n", content)
                self.assertTrue((base / "references/worked-example.md").is_file())

    def test_local_references_survive_install_layout(self):
        with tempfile.TemporaryDirectory(prefix="rds-packaged-methods-") as directory:
            for name in GUIDES:
                target = Path(directory) / name
                shutil.copytree(ROOT / "skills/regulated" / name, target)
                for path in target.rglob("*.md"):
                    for link in local_links(path.read_text()):
                        resolved = (path.parent / link).resolve()
                        self.assertTrue(resolved.is_relative_to(target.resolve()),
                                        "%s escapes installed skill: %s" % (path, link))
                        self.assertTrue(resolved.is_file(), "%s: %s" % (path, link))

    def test_lifecycle_map_covers_each_owner(self):
        text = (ROOT / "spec/techniques.md").read_text()
        for name in GUIDES:
            self.assertIn("`" + name + "`", text)
        for heading in ("Early planning", "Design and build", "Verification and validation",
                        "Release and feedback", "Evidence boundaries"):
            self.assertIn("## " + heading, text)

    def test_prerequisites_and_authorisation_precede_actions(self):
        risk = (ROOT / "skills/regulated/risk/SKILL.md").read_text().split("## Process", 1)[1]
        self.assertLess(risk.index("Confirm the intended use"), risk.index("Select hazard analysis"))
        self.assertLess(risk.index("Treat security as part of safety"), risk.index("Identify hazards"))
        security = (ROOT / "skills/regulated/security-diligence/SKILL.md").read_text().split("## Process", 1)[1]
        self.assertLess(security.index("Before active scanning"), security.index("Review the code and the dependencies"))

    def test_unacceptable_individual_risk_has_a_separate_disposition(self):
        base = ROOT / "skills/regulated/risk"
        guide = (base / "references/control-evidence.md").read_text()
        self.assertIn("## Unacceptable individual residual risk", guide)
        self.assertIn("return to control-option analysis", guide)
        self.assertIn("remains unacceptable", guide)
        self.assertIn("clinical evaluation", guide)
        self.assertIn("7.4", guide)
        self.assertIn("7.4", (base / "SKILL.md").read_text())

    def test_authorisation_summaries_match_the_controlled_change_route(self):
        skill = (ROOT / "skills/regulated/configuration-management/SKILL.md").read_text()
        summary = skill.split("## When to use", 1)[0]
        self.assertIn("approved authorisation", summary)
        self.assertNotIn("changed only through approved change requests", summary)
        self.assertNotIn("- Approve the change request before the work", skill)
        doc = (ROOT / "docs/regulated/configuration-management.md").read_text()
        self.assertIn("approved authorisation", doc)
        self.assertNotIn("Every commit on the release branch traces to a change request.", doc)

    def test_planning_prerequisites_do_not_require_execution_evidence(self):
        for name in ("verify", "package"):
            doc = (ROOT / "docs/regulated" / (name + ".md")).read_text()
            prerequisites = doc.split("## Prerequisites", 1)[1].split("## ", 1)[0]
            self.assertIn("For planning:", prerequisites)
            self.assertIn("For execution:", prerequisites)

    def test_safety_trace_example_preserves_paths_and_unknowns(self):
        path = ROOT / "skills/regulated/traceability/references/example.json"
        data = json.loads(path.read_text())
        self.assertEqual(data["evidence_kind"], "fictional-not-executed")
        paths = data["paths"]
        self.assertEqual(len({p["context"] for p in paths}), len(paths))
        self.assertEqual(len({p["hazard"] for p in paths}), 1)
        self.assertGreater(len({p["harm"] for p in paths}), 1)
        controls = {c["id"]: c for c in data["controls"]}
        for item in paths:
            self.assertIn(item["control"], controls)
        for control in controls.values():
            self.assertIn("implementation", control["evidence"])
            self.assertIn("effectiveness", control["evidence"])
            for evidence in control["evidence"].values():
                self.assertEqual(evidence["outcome"], "not_run")
        self.assertEqual(data["test_connection"], "unconfigured")
        self.assertEqual(data["coverage_assessment"], "unknown")
        text = path.with_name("worked-example.md").read_text()
        for item in paths:
            for key in ("hazard", "context", "harm", "control"):
                self.assertIn(item[key], text)

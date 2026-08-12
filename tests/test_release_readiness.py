from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "build-game"
SPEC = importlib.util.spec_from_file_location("evaluate_release", SKILL / "scripts" / "evaluate_release.py")
assert SPEC and SPEC.loader
EVALUATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EVALUATOR)
EXAMPLE = json.loads((SKILL / "assets" / "release-readiness.example.json").read_text(encoding="utf-8"))


class ReleaseReadinessTests(unittest.TestCase):
    def test_example_computes_pass(self) -> None:
        verdict, reasons = EVALUATOR.validate_release(copy.deepcopy(EXAMPLE))
        self.assertEqual((verdict, reasons), ("PASS", []))

    def test_required_failure_computes_fail(self) -> None:
        data = copy.deepcopy(EXAMPLE)
        data["gates"][0]["status"] = "FAIL"
        data["declaredVerdict"] = "FAIL"
        verdict, reasons = EVALUATOR.validate_release(data)
        self.assertEqual(verdict, "FAIL")
        self.assertTrue(reasons)

    def test_required_historical_evidence_computes_concerns(self) -> None:
        data = copy.deepcopy(EXAMPLE)
        data["gates"][0]["freshness"] = "historical"
        data["declaredVerdict"] = "CONCERNS"
        verdict, reasons = EVALUATOR.validate_release(data)
        self.assertEqual(verdict, "CONCERNS")
        self.assertTrue(reasons)

    def test_declared_verdict_must_match_computed(self) -> None:
        data = copy.deepcopy(EXAMPLE)
        data["gates"][0]["status"] = "FAIL"
        with self.assertRaisesRegex(ValueError, "does not match"):
            EVALUATOR.validate_release(data)

    def test_required_gate_cannot_be_not_applicable(self) -> None:
        data = copy.deepcopy(EXAMPLE)
        data["gates"][0]["status"] = "NOT_APPLICABLE"
        data["gates"][0]["freshness"] = "not-applicable"
        with self.assertRaisesRegex(ValueError, "required gate"):
            EVALUATOR.validate_release(data)

    def test_cannot_omit_a_required_category(self) -> None:
        data = copy.deepcopy(EXAMPLE)
        data["gates"] = [gate for gate in data["gates"] if gate["category"] != "security"]
        with self.assertRaisesRegex(ValueError, "missing required categories"):
            EVALUATOR.validate_release(data)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("run_evals", ROOT / "scripts" / "run_evals.py")
assert SPEC and SPEC.loader
RUN_EVALS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUN_EVALS)


class BehavioralEvalTests(unittest.TestCase):
    def test_required_any_of_and_all_of_pass(self) -> None:
        case = {
            "required": [
                {"name": "mode", "anyOf": [r"\bsolo\b", r"\blean\b"]},
                {"name": "evidence", "allOf": ["test", "playable"]},
            ],
            "forbidden": [],
        }
        self.assertEqual(RUN_EVALS.grade(case, "Solo: run a test and a playable smoke."), [])

    def test_missing_behavior_fails(self) -> None:
        case = {
            "required": [{"name": "preview", "allOf": ["stop", "Preview"]}],
            "forbidden": [],
        }
        self.assertEqual(RUN_EVALS.grade(case, "Run tests only."), ["missing behavior: preview"])

    def test_forbidden_behavior_fails(self) -> None:
        case = {
            "required": [],
            "forbidden": [{"name": "broad kill", "patterns": ["kill all"]}],
        }
        self.assertEqual(RUN_EVALS.grade(case, "Kill all preview processes."), ["forbidden behavior: broad kill"])

    def test_markdown_emphasis_does_not_break_semantic_match(self) -> None:
        case = {
            "required": [{"name": "path", "anyOf": [r"path to \W*PASS"]}],
            "forbidden": [],
        }
        self.assertEqual(RUN_EVALS.grade(case, "Minimal path to **PASS**: run Preview."), [])

    def test_forbidden_pattern_does_not_penalize_explicit_refusal(self) -> None:
        case = {
            "required": [],
            "forbidden": [{"name": "upload", "patterns": [r"I(?:'ll| will) upload the project"]}],
        }
        self.assertEqual(RUN_EVALS.grade(case, "I will not upload the project."), [])


if __name__ == "__main__":
    unittest.main()

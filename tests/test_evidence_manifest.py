from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "build-game"
SPEC = importlib.util.spec_from_file_location(
    "validate_evidence", SKILL / "scripts" / "validate_evidence.py"
)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)
EXAMPLE = json.loads((SKILL / "assets" / "evidence-manifest.example.json").read_text(encoding="utf-8"))


class EvidenceManifestTests(unittest.TestCase):
    def test_example_is_valid(self) -> None:
        VALIDATOR.validate_manifest(copy.deepcopy(EXAMPLE))

    def test_pass_rejects_required_preview_not_run(self) -> None:
        data = copy.deepcopy(EXAMPLE)
        data["playable"]["status"] = "NOT_RUN"
        data["playable"]["freshness"] = "not-run"
        data["verdict"] = "PASS"
        with self.assertRaisesRegex(ValueError, "required playable evidence"):
            VALIDATOR.validate_manifest(data)

    def test_pass_rejects_failed_check(self) -> None:
        data = copy.deepcopy(EXAMPLE)
        data["checks"][0]["status"] = "FAIL"
        data["verdict"] = "PASS"
        with self.assertRaisesRegex(ValueError, "check failed"):
            VALIDATOR.validate_manifest(data)

    def test_public_manifest_rejects_absolute_path(self) -> None:
        data = copy.deepcopy(EXAMPLE)
        data["checks"][0]["artifact"] = "C:\\private\\preview.png"
        with self.assertRaisesRegex(ValueError, "absolute local path"):
            VALIDATOR.validate_manifest(data)


if __name__ == "__main__":
    unittest.main()

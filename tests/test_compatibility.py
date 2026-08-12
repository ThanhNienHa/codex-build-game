from __future__ import annotations

import importlib.util
import json
import copy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_compatibility", ROOT / "scripts" / "validate_compatibility.py")
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class CompatibilityTests(unittest.TestCase):
    def test_checked_in_matrix_is_valid(self) -> None:
        data = json.loads((ROOT / "compatibility" / "matrix.json").read_text(encoding="utf-8"))
        VALIDATOR.validate_matrix(data)

    def test_ide_plugin_support_cannot_be_overstated(self) -> None:
        data = json.loads((ROOT / "compatibility" / "matrix.json").read_text(encoding="utf-8"))
        changed = copy.deepcopy(data)
        for surface in changed["codexSurfaces"]:
            if surface["surface"] == "codex-ide-extension":
                surface["plugin"] = "supported"
        with self.assertRaisesRegex(ValueError, "IDE plugins"):
            VALIDATOR.validate_matrix(changed)


if __name__ == "__main__":
    unittest.main()

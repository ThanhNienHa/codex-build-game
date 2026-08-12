from __future__ import annotations

import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package_release", ROOT / "scripts" / "package_release.py")
assert SPEC and SPEC.loader
PACKAGER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKAGER)


class PackageReleaseTests(unittest.TestCase):
    def test_archive_contains_plugin_and_excludes_caches(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            with mock.patch.object(PACKAGER, "DIST", output):
                PACKAGER.main()
            archive = next(output.glob("*.zip"))
            with zipfile.ZipFile(archive) as package:
                names = package.namelist()
            self.assertIn(".codex-plugin/plugin.json", names)
            self.assertIn("skills/build-game/SKILL.md", names)
            self.assertFalse(any("__pycache__" in name or name.endswith(".pyc") for name in names))
            self.assertTrue(archive.with_suffix(archive.suffix + ".sha256").is_file())


if __name__ == "__main__":
    unittest.main()

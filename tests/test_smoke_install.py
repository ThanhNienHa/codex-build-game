from __future__ import annotations

import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("smoke_install", ROOT / "scripts" / "smoke_install.py")
assert SPEC and SPEC.loader
SMOKE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SMOKE)


class SmokeInstallTests(unittest.TestCase):
    def test_rejects_path_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            archive_path = Path(directory) / "unsafe.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                for required in SMOKE.REQUIRED:
                    archive.writestr(required, "{}" if required.endswith(".json") else "---\nname: build-game\ndescription: x\n---\n")
                archive.writestr("../escape.txt", "no")
            with zipfile.ZipFile(archive_path) as archive:
                with self.assertRaisesRegex(ValueError, "unsafe"):
                    SMOKE.safe_members(archive)

    def test_rejects_windows_style_path_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            archive_path = Path(directory) / "unsafe-windows.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("..\\escape.txt", "no")
            with zipfile.ZipFile(archive_path) as archive:
                with self.assertRaisesRegex(ValueError, "unsafe"):
                    SMOKE.safe_members(archive)

    def test_rejects_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            archive_path = Path(directory) / "symlink.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                info = zipfile.ZipInfo("link")
                info.create_system = 3
                info.external_attr = 0o120777 << 16
                archive.writestr(info, "target")
            with zipfile.ZipFile(archive_path) as archive:
                with self.assertRaisesRegex(ValueError, "unsafe"):
                    SMOKE.safe_members(archive)

    def test_rejects_duplicate_entries(self) -> None:
        members = [
            zipfile.ZipInfo("skills/build-game/SKILL.md"),
            zipfile.ZipInfo("skills/build-game/SKILL.md"),
        ]

        class DuplicateArchive:
            def infolist(self) -> list[zipfile.ZipInfo]:
                return members

        with self.assertRaisesRegex(ValueError, "duplicate"):
            SMOKE.safe_members(DuplicateArchive())

    def test_rejects_case_collisions_on_windows(self) -> None:
        members = [zipfile.ZipInfo("skills/build-game/SKILL.md"), zipfile.ZipInfo("skills/build-game/skill.md")]

        class CollisionArchive:
            def infolist(self) -> list[zipfile.ZipInfo]:
                return members

        with self.assertRaisesRegex(ValueError, "duplicate"):
            SMOKE.safe_members(CollisionArchive())

    def test_rejects_windows_alternate_data_stream(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            archive_path = Path(directory) / "ads.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("skills/build-game/file.txt:stream", "no")
            with zipfile.ZipFile(archive_path) as archive:
                with self.assertRaisesRegex(ValueError, "unsafe"):
                    SMOKE.safe_members(archive)


if __name__ == "__main__":
    unittest.main()

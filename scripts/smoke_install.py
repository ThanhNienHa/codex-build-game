from __future__ import annotations

import json
import re
import stat
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


REQUIRED = {
    ".codex-plugin/plugin.json",
    "skills/build-game/SKILL.md",
    "skills/build-game/agents/openai.yaml",
}


def fail(message: str) -> None:
    raise ValueError(message)


def safe_members(archive: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
    members = archive.infolist()
    normalized_names: list[str] = []
    for member in members:
        normalized = member.filename.replace("\\", "/")
        path = PurePosixPath(normalized)
        mode = member.external_attr >> 16
        if (
            path.is_absolute()
            or ".." in path.parts
            or any(":" in part for part in path.parts)
            or "__pycache__" in path.parts
            or path.suffix == ".pyc"
            or stat.S_ISLNK(mode)
        ):
            fail(f"unsafe or cache archive entry: {member.filename}")
        normalized_names.append(normalized)
    if len(normalized_names) != len({name.casefold() for name in normalized_names}):
        fail("archive contains duplicate entries")
    names = set(normalized_names)
    missing = sorted(REQUIRED - names)
    if missing:
        fail(f"archive missing: {', '.join(missing)}")
    return members


def validate_install(root: Path) -> str:
    plugin = json.loads((root / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if plugin.get("name") != "codex-build-game" or not re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", "")):
        fail("invalid plugin identity or version")
    if plugin.get("skills") != "./skills/":
        fail("plugin skills path must be ./skills/")
    skill = (root / "skills" / "build-game" / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or "name: build-game" not in skill or "description:" not in skill:
        fail("installed SKILL.md metadata is invalid")
    for relative in re.findall(r"`(references/[^`]+\.md)`", skill):
        if not (root / "skills" / "build-game" / relative).is_file():
            fail(f"installed skill reference missing: {relative}")
    return plugin["version"]


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: smoke_install.py <release.zip>")
        raise SystemExit(2)
    archive_path = Path(sys.argv[1])
    try:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with zipfile.ZipFile(archive_path) as archive:
                safe_members(archive)
                archive.extractall(root)
            version = validate_install(root)
    except (OSError, zipfile.BadZipFile, json.JSONDecodeError, ValueError) as exc:
        print(f"Clean install smoke failed: {exc}")
        raise SystemExit(1)
    print(f"Clean install smoke passed: codex-build-game {version}")


if __name__ == "__main__":
    main()

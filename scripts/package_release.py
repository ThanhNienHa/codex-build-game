from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PLUGIN = ROOT / ".codex-plugin" / "plugin.json"


def main() -> None:
    metadata = json.loads(PLUGIN.read_text(encoding="utf-8"))
    version = metadata["version"]
    archive = DIST / f"codex-build-game-v{version}.zip"
    checksum = archive.with_suffix(archive.suffix + ".sha256")

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    included = [
        ROOT / ".codex-plugin" / "plugin.json",
        *sorted(
            path
            for path in (ROOT / "skills").rglob("*")
            if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
        ),
        ROOT / "LICENSE",
        ROOT / "README.md",
    ]
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
        for path in included:
            output.write(path, path.relative_to(ROOT).as_posix())

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    try:
        archive_label = archive.relative_to(ROOT)
        checksum_label = checksum.relative_to(ROOT)
    except ValueError:
        archive_label = archive
        checksum_label = checksum
    print(f"Created {archive_label}")
    print(f"Created {checksum_label}")


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "build-game"
SKILL_MD = SKILL_DIR / "SKILL.md"
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def validate_plugin() -> None:
    data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    required = ["name", "version", "description", "author", "skills", "interface"]
    missing = [key for key in required if key not in data]
    if missing:
        fail(f"plugin.json missing: {', '.join(missing)}")
    if data["name"] != "codex-build-game":
        fail("plugin name must be codex-build-game")
    if not re.fullmatch(r"\d+\.\d+\.\d+", data["version"]):
        fail("plugin version must be strict semver")
    if data["skills"] != "./skills/":
        fail("plugin skills path must be ./skills/")


def validate_skill() -> None:
    text = SKILL_MD.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md needs YAML frontmatter")
    frontmatter = match.group(1)
    if not re.search(r"^name:\s*build-game\s*$", frontmatter, flags=re.MULTILINE):
        fail("SKILL.md name must be build-game")
    if not re.search(r"^description:\s*\S", frontmatter, flags=re.MULTILINE):
        fail("SKILL.md needs a description")
    if len(text.splitlines()) > 500:
        fail("SKILL.md must stay under 500 lines")

    links = re.findall(r"`(references/[^`]+\.md)`", text)
    for relative in links:
        if not (SKILL_DIR / relative).is_file():
            fail(f"missing referenced file: {relative}")


def validate_repository_text() -> None:
    checked_suffixes = {".md", ".json", ".yaml", ".yml", ".py"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix not in checked_suffixes:
            continue
        text = path.read_text(encoding="utf-8")
        placeholder_marker = "[" + "TODO:"
        if placeholder_marker in text:
            fail(f"placeholder found in {path.relative_to(ROOT)}")
        unsupported_engine = "go" + "dot"
        if unsupported_engine in text.casefold():
            fail(f"unsupported engine reference found in {path.relative_to(ROOT)}")
        if "\ufffd" in text:
            fail(f"replacement character found in {path.relative_to(ROOT)}")


def validate_evals() -> None:
    data = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
    if not isinstance(data, list) or len(data) < 5:
        fail("evals/cases.json must contain at least five scenarios")
    required = {"id", "prompt", "expect", "forbid"}
    for index, case in enumerate(data):
        if not isinstance(case, dict) or not required.issubset(case):
            fail(f"eval scenario {index} is missing required fields")
        if not case["expect"] or not case["forbid"]:
            fail(f"eval scenario {case['id']} needs positive and negative criteria")


def validate_case_studies() -> None:
    case_dir = ROOT / "docs" / "case-studies"
    required_sections = [
        "## Context",
        "## Skill behavior observed",
        "## Fresh verification evidence",
        "## Verdict",
        "## Privacy",
    ]
    cases = [path for path in case_dir.glob("*.md") if path.name not in {"README.md", "template.md"}]
    for path in cases:
        text = path.read_text(encoding="utf-8")
        for section in required_sections:
            if section not in text:
                fail(f"case study {path.name} missing section: {section}")
        if not any(verdict in text for verdict in ("**PASS**", "**CONCERNS**", "**FAIL**")):
            fail(f"case study {path.name} needs an explicit verdict")


def main() -> None:
    validate_plugin()
    validate_skill()
    validate_repository_text()
    validate_evals()
    validate_case_studies()
    print("Repository validation passed.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        fail(str(exc))

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "build-game"


def normalized_corpus() -> str:
    files = [SKILL_DIR / "SKILL.md", *sorted((SKILL_DIR / "references").glob("*.md"))]
    return re.sub(r"\s+", " ", "\n".join(path.read_text(encoding="utf-8") for path in files)).casefold()


def main() -> None:
    cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
    corpus = normalized_corpus()
    failures: list[str] = []

    for case in cases:
        for phrase in case["expect"]:
            if phrase.casefold() not in corpus:
                failures.append(f"{case['id']}: expected guidance missing: {phrase}")

    if len({case["id"] for case in cases}) != len(cases):
        failures.append("eval IDs must be unique")

    if failures:
        print("Eval contract failed:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print(f"Eval contract passed: {len(cases)} scenarios.")
    print("Note: behavioral forward-tests remain required for substantial changes.")


if __name__ == "__main__":
    main()

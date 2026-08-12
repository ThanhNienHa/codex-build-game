from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "evals" / "cases.json"
CONFORMANCE_DIR = ROOT / "evals" / "conformance"


def matches(pattern: str, text: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL) is not None


def grade(case: dict[str, Any], response: str) -> list[str]:
    failures: list[str] = []
    for rule in case["required"]:
        if "anyOf" in rule and not any(matches(pattern, response) for pattern in rule["anyOf"]):
            failures.append(f"missing behavior: {rule['name']}")
        if "allOf" in rule and not all(matches(pattern, response) for pattern in rule["allOf"]):
            failures.append(f"missing behavior: {rule['name']}")
    for rule in case["forbidden"]:
        if any(matches(pattern, response) for pattern in rule["patterns"]):
            failures.append(f"forbidden behavior: {rule['name']}")
    return failures


def validate_cases(cases: Any) -> list[dict[str, Any]]:
    if not isinstance(cases, list) or len(cases) < 5:
        raise ValueError("evals/cases.json must contain at least five cases")
    ids: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            raise ValueError(f"case {index} must be an object")
        if not {"id", "prompt", "required", "forbidden"}.issubset(case):
            raise ValueError(f"case {index} is missing required fields")
        if case["id"] in ids:
            raise ValueError(f"duplicate case ID: {case['id']}")
        ids.add(case["id"])
        if not case["required"]:
            raise ValueError(f"case {case['id']} has no required behaviors")
        for rule in [*case["required"], *case["forbidden"]]:
            patterns = rule.get("anyOf", rule.get("allOf", rule.get("patterns", [])))
            if not patterns:
                raise ValueError(f"case {case['id']} contains an empty rule")
            for pattern in patterns:
                re.compile(pattern)
    return cases


def main() -> None:
    parser = argparse.ArgumentParser(description="Grade build-game behavioral response contracts")
    parser.add_argument("--case", help="Grade one case ID")
    parser.add_argument("--response", type=Path, help="Response text for --case")
    parser.add_argument("--responses-dir", type=Path, default=CONFORMANCE_DIR)
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()

    cases = validate_cases(json.loads(CASES_PATH.read_text(encoding="utf-8")))
    if bool(args.case) != bool(args.response):
        parser.error("--case and --response must be provided together")
    if args.case:
        cases = [case for case in cases if case["id"] == args.case]
        if not cases:
            parser.error(f"unknown case: {args.case}")

    results: list[dict[str, Any]] = []
    for case in cases:
        response_path = args.response if args.case else args.responses_dir / f"{case['id']}.md"
        if not response_path or not response_path.is_file():
            failures = [f"missing response file: {response_path}"]
        else:
            failures = grade(case, response_path.read_text(encoding="utf-8"))
        results.append({"id": case["id"], "passed": not failures, "failures": failures})

    if args.json_output:
        args.json_output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    failed = [result for result in results if not result["passed"]]
    for result in results:
        print(f"{'PASS' if result['passed'] else 'FAIL'} {result['id']}")
        for failure in result["failures"]:
            print(f"  - {failure}")
    if failed:
        raise SystemExit(1)
    print(f"Behavioral eval conformance passed: {len(results)} cases.")
    print("Grade fresh agent responses with --case ID --response FILE.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, json.JSONDecodeError, re.error) as exc:
        print(f"Eval configuration failed: {exc}")
        raise SystemExit(1)

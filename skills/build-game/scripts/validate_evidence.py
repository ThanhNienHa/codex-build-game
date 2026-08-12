from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


STATUSES = {"PASS", "CONCERNS", "FAIL", "NOT_RUN", "NOT_APPLICABLE"}
FRESHNESS = {"fresh", "historical", "not-run", "not-applicable"}
PROCESSES = {"solo", "lean", "full"}
VERDICTS = {"PASS", "CONCERNS", "FAIL"}
WINDOWS_ABSOLUTE = re.compile(r"^[A-Za-z]:[\\/]")


def fail(message: str) -> None:
    raise ValueError(message)


def require_object(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{name} must be an object")
    return value


def require_string(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{name} must be a non-empty string")
    return value


def reject_absolute_paths(value: Any, location: str = "manifest") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            reject_absolute_paths(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_absolute_paths(child, f"{location}[{index}]")
    elif isinstance(value, str):
        if WINDOWS_ABSOLUTE.match(value) or value.startswith("/") or value.startswith("file://"):
            fail(f"{location} contains an absolute local path")


def validate_manifest(data: Any) -> None:
    root = require_object(data, "manifest")
    if root.get("schemaVersion") != "1.0":
        fail("schemaVersion must be 1.0")

    project = require_object(root.get("project"), "project")
    require_string(project.get("engine"), "project.engine")
    require_string(project.get("engineVersion"), "project.engineVersion")
    require_string(project.get("stage"), "project.stage")
    if project.get("process") not in PROCESSES:
        fail("project.process must be solo, lean, or full")

    change = require_object(root.get("change"), "change")
    require_string(change.get("summary"), "change.summary")

    checks = root.get("checks")
    if not isinstance(checks, list) or not checks:
        fail("checks must be a non-empty array")
    seen: set[str] = set()
    for index, raw_check in enumerate(checks):
        check = require_object(raw_check, f"checks[{index}]")
        name = require_string(check.get("name"), f"checks[{index}].name")
        if name in seen:
            fail(f"duplicate check name: {name}")
        seen.add(name)
        status = check.get("status")
        freshness = check.get("freshness")
        if status not in STATUSES:
            fail(f"checks[{index}].status is invalid")
        if freshness not in FRESHNESS:
            fail(f"checks[{index}].freshness is invalid")
        if status == "NOT_RUN" and freshness != "not-run":
            fail(f"checks[{index}] NOT_RUN must use not-run freshness")
        if status == "NOT_APPLICABLE" and freshness != "not-applicable":
            fail(f"checks[{index}] NOT_APPLICABLE must use not-applicable freshness")

    playable = require_object(root.get("playable"), "playable")
    if not isinstance(playable.get("required"), bool):
        fail("playable.required must be a boolean")
    if playable.get("status") not in STATUSES:
        fail("playable.status is invalid")
    if playable.get("freshness") not in FRESHNESS:
        fail("playable.freshness is invalid")

    verdict = root.get("verdict")
    if verdict not in VERDICTS:
        fail("verdict must be PASS, CONCERNS, or FAIL")
    if playable["required"] and playable["status"] in {"FAIL", "NOT_RUN"} and verdict == "PASS":
        fail("verdict cannot be PASS when required playable evidence failed or was not run")
    if any(check["status"] == "FAIL" for check in checks) and verdict == "PASS":
        fail("verdict cannot be PASS when a check failed")

    limitations = root.get("limitations")
    if not isinstance(limitations, list) or not all(isinstance(item, str) for item in limitations):
        fail("limitations must be an array of strings")

    privacy = require_object(root.get("privacy"), "privacy")
    for field in (
        "sanitizedForPublication",
        "containsAbsoluteLocalPaths",
        "containsCredentials",
        "containsPersonalData",
        "containsProprietaryAssets",
    ):
        if not isinstance(privacy.get(field), bool):
            fail(f"privacy.{field} must be a boolean")
    if privacy["sanitizedForPublication"] and any(
        privacy[field]
        for field in (
            "containsAbsoluteLocalPaths",
            "containsCredentials",
            "containsPersonalData",
            "containsProprietaryAssets",
        )
    ):
        fail("a manifest marked sanitized cannot declare private material")
    if privacy["sanitizedForPublication"]:
        reject_absolute_paths(root)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: validate_evidence.py <manifest.json>")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    try:
        validate_manifest(json.loads(path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Evidence manifest validation failed: {exc}")
        raise SystemExit(1)
    print(f"Evidence manifest is valid: {path}")


if __name__ == "__main__":
    main()

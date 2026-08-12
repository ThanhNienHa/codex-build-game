from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


STATUSES = {"PASS", "CONCERNS", "FAIL", "NOT_RUN", "NOT_APPLICABLE"}
FRESHNESS = {"fresh", "historical", "not-run", "not-applicable"}
VERDICTS = {"PASS", "CONCERNS", "FAIL"}
CATEGORIES = {
    "gameplay",
    "automated",
    "playable",
    "performance",
    "packaging",
    "security",
    "privacy-legal",
    "operations",
}
REQUIRED_CATEGORIES = {
    "gameplay",
    "automated",
    "playable",
    "performance",
    "packaging",
    "security",
    "privacy-legal",
}
WINDOWS_ABSOLUTE = re.compile(r"^[A-Za-z]:[\\/]")


def fail(message: str) -> None:
    raise ValueError(message)


def object_value(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{name} must be an object")
    return value


def text_value(value: Any, name: str) -> str:
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


def compute_verdict(gates: list[dict[str, Any]]) -> tuple[str, list[str]]:
    blockers: list[str] = []
    concerns: list[str] = []
    for gate in gates:
        label = gate["id"]
        status = gate["status"]
        freshness = gate["freshness"]
        required = gate["required"]
        if required and status == "FAIL":
            blockers.append(f"{label}: required gate failed")
        elif required and status in {"NOT_RUN", "NOT_APPLICABLE", "CONCERNS"}:
            concerns.append(f"{label}: required gate is {status}")
        elif required and freshness != "fresh":
            concerns.append(f"{label}: required evidence is {freshness}")
        elif not required and status == "FAIL":
            concerns.append(f"{label}: optional gate failed")
    if blockers:
        return "FAIL", blockers + concerns
    if concerns:
        return "CONCERNS", concerns
    return "PASS", []


def validate_release(data: Any) -> tuple[str, list[str]]:
    root = object_value(data, "release manifest")
    if root.get("schemaVersion") != "1.0":
        fail("schemaVersion must be 1.0")
    release = object_value(root.get("release"), "release")
    for field in ("version", "commit", "platform", "channel"):
        text_value(release.get(field), f"release.{field}")
    project = object_value(root.get("project"), "project")
    text_value(project.get("engine"), "project.engine")
    text_value(project.get("engineVersion"), "project.engineVersion")

    gates = root.get("gates")
    if not isinstance(gates, list) or not gates:
        fail("gates must be a non-empty array")
    seen: set[str] = set()
    seen_categories: set[str] = set()
    for index, raw_gate in enumerate(gates):
        gate = object_value(raw_gate, f"gates[{index}]")
        gate_id = text_value(gate.get("id"), f"gates[{index}].id")
        if gate_id in seen:
            fail(f"duplicate gate ID: {gate_id}")
        seen.add(gate_id)
        if gate.get("category") not in CATEGORIES:
            fail(f"gates[{index}].category is invalid")
        seen_categories.add(gate["category"])
        if not isinstance(gate.get("required"), bool):
            fail(f"gates[{index}].required must be a boolean")
        status = gate.get("status")
        freshness = gate.get("freshness")
        if status not in STATUSES:
            fail(f"gates[{index}].status is invalid")
        if freshness not in FRESHNESS:
            fail(f"gates[{index}].freshness is invalid")
        if status == "NOT_RUN" and freshness != "not-run":
            fail(f"gates[{index}] NOT_RUN must use not-run freshness")
        if status == "NOT_APPLICABLE":
            if freshness != "not-applicable":
                fail(f"gates[{index}] NOT_APPLICABLE must use not-applicable freshness")
            if gate["required"]:
                fail(f"gates[{index}] required gate cannot be NOT_APPLICABLE")
            text_value(gate.get("notes"), f"gates[{index}].notes")
        if status not in {"NOT_RUN", "NOT_APPLICABLE"}:
            text_value(gate.get("evidence"), f"gates[{index}].evidence")

    missing_categories = sorted(REQUIRED_CATEGORIES - seen_categories)
    if missing_categories:
        fail(f"release gates missing required categories: {', '.join(missing_categories)}")

    declared = root.get("declaredVerdict")
    if declared not in VERDICTS:
        fail("declaredVerdict must be PASS, CONCERNS, or FAIL")
    limitations = root.get("limitations")
    if not isinstance(limitations, list) or not all(isinstance(item, str) for item in limitations):
        fail("limitations must be an array of strings")

    privacy = object_value(root.get("privacy"), "privacy")
    privacy_fields = (
        "sanitizedForPublication",
        "containsAbsoluteLocalPaths",
        "containsCredentials",
        "containsPersonalData",
        "containsProprietaryAssets",
    )
    for field in privacy_fields:
        if not isinstance(privacy.get(field), bool):
            fail(f"privacy.{field} must be a boolean")
    if privacy["sanitizedForPublication"]:
        if any(privacy[field] for field in privacy_fields[1:]):
            fail("a manifest marked sanitized cannot declare private material")
        reject_absolute_paths(root)

    computed, reasons = compute_verdict(gates)
    if declared != computed:
        fail(f"declaredVerdict {declared} does not match computed verdict {computed}")
    return computed, reasons


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: evaluate_release.py <release-readiness.json>")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    try:
        verdict, reasons = validate_release(json.loads(path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Release readiness validation failed: {exc}")
        raise SystemExit(1)
    print(f"Release readiness verdict: {verdict}")
    for reason in reasons:
        print(f"- {reason}")


if __name__ == "__main__":
    main()

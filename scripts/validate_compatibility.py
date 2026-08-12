from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "compatibility" / "matrix.json"
SURFACE_SUPPORT = {"supported", "not-supported"}
ENGINE_SUPPORT = {"fixture-tested", "case-study", "guidance-only", "not-supported"}


def fail(message: str) -> None:
    raise ValueError(message)


def validate_matrix(data: Any) -> None:
    if not isinstance(data, dict) or data.get("schemaVersion") != "1.0":
        fail("compatibility schemaVersion must be 1.0")
    if not isinstance(data.get("verifiedAt"), str):
        fail("verifiedAt is required")
    docs = data.get("officialDocs")
    if not isinstance(docs, dict) or not all(
        isinstance(docs.get(key), str)
        and docs[key].startswith("https://learn.chatgpt.com/")
        for key in ("skills", "plugins")
    ):
        fail("official OpenAI skill and plugin docs are required")

    surfaces = data.get("codexSurfaces")
    if not isinstance(surfaces, list) or not surfaces:
        fail("codexSurfaces must be a non-empty array")
    seen_surfaces: set[str] = set()
    surface_map: dict[str, dict[str, Any]] = {}
    for item in surfaces:
        if not isinstance(item, dict) or not isinstance(item.get("surface"), str):
            fail("each surface needs an ID")
        if item["surface"] in seen_surfaces:
            fail(f"duplicate surface: {item['surface']}")
        seen_surfaces.add(item["surface"])
        surface_map[item["surface"]] = item
        if item.get("standaloneSkill") not in SURFACE_SUPPORT or item.get("plugin") not in SURFACE_SUPPORT:
            fail(f"invalid support label for {item['surface']}")
        if not isinstance(item.get("activation"), str) or not item["activation"]:
            fail(f"activation guidance missing for {item['surface']}")
    required_surfaces = {
        "chatgpt-desktop-codex",
        "codex-cli",
        "codex-ide-extension",
    }
    missing_surfaces = sorted(required_surfaces - seen_surfaces)
    if missing_surfaces:
        fail(f"missing Codex surfaces: {', '.join(missing_surfaces)}")
    if surface_map["codex-ide-extension"]["plugin"] != "not-supported":
        fail("official docs currently mark IDE plugins not supported")

    engines = data.get("engines")
    if not isinstance(engines, list) or not engines:
        fail("engines must be a non-empty array")
    seen_engines: set[str] = set()
    for item in engines:
        engine = item.get("engine") if isinstance(item, dict) else None
        if not isinstance(engine, str) or not engine:
            fail("each engine needs an ID")
        if engine in seen_engines:
            fail(f"duplicate engine: {engine}")
        seen_engines.add(engine)
        support = item.get("support")
        versions = item.get("versionEvidence")
        evidence = item.get("evidence")
        if support not in ENGINE_SUPPORT:
            fail(f"invalid engine support label: {engine}")
        if not isinstance(versions, list) or not all(isinstance(version, str) for version in versions):
            fail(f"versionEvidence must be a string array: {engine}")
        if not isinstance(evidence, list) or not all(isinstance(path, str) for path in evidence):
            fail(f"evidence must be a path array: {engine}")
        if support in {"fixture-tested", "case-study"} and not versions:
            fail(f"{support} requires version evidence: {engine}")
        if support in {"fixture-tested", "case-study"} and not evidence:
            fail(f"{support} requires evidence paths: {engine}")
        for relative in evidence:
            if not (ROOT / relative).exists():
                fail(f"missing compatibility evidence: {relative}")


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) == 2 else MATRIX
    try:
        validate_matrix(json.loads(path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Compatibility validation failed: {exc}")
        raise SystemExit(1)
    print(f"Compatibility matrix is valid: {path}")


if __name__ == "__main__":
    main()

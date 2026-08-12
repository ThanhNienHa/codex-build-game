from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_node(cwd: Path, test_file: str, expect_success: bool) -> None:
    result = subprocess.run(
        ["node", "--test", test_file],
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if (result.returncode == 0) != expect_success:
        print(result.stdout)
        print(result.stderr)
        expected = "pass" if expect_success else "reproduce the expected failure"
        raise SystemExit(f"Fixture {cwd.name}/{test_file} did not {expected}")


def main() -> None:
    phaser = ROOT / "fixtures" / "phaser-brownfield"
    cocos = ROOT / "fixtures" / "cocos-presentation-safety"

    run_node(phaser, "test/scoring.contract.test.js", expect_success=False)
    print("PASS Phaser starter reproduces the score-rounding defect")
    run_node(phaser, "test/scoring.solution.test.js", expect_success=True)
    print("PASS Phaser reference correction satisfies the contract")
    run_node(cocos, "test/presentation.test.js", expect_success=True)
    print("PASS Cocos presentation fixture preserves authoritative state")


if __name__ == "__main__":
    main()

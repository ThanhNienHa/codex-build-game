# Codex Build Game

An open-source Codex plugin and skill for planning, building, testing, playtesting, and shipping games without unnecessary studio ceremony.

## What it adds

- Project-stage detection: Explore, Prototype, Vertical Slice, Production, Polish/Release
- Proportional `solo`, `lean`, and `full` workflows
- Optional `studio-full` review with at most three risk-matched specialists
- System maps, lightweight specs, and structured GDD guidance
- Prototype-first risk reduction and vertical-slice validation
- Requirement-to-code-to-test/preview traceability
- Existing-asset discovery and reuse before generating replacements
- Cocos MCP and clean Cocos Preview workflow
- Evidence-based `PASS`, `CONCERNS`, and `FAIL` quality gates
- Behavioral response evals and public Phaser/Cocos fixtures
- Machine-readable verification evidence and Cocos Preview reports

The skill supports engine-neutral design and architecture, with focused guidance for Phaser, Cocos Creator, and migration to Unity. It intentionally does not simulate a large studio for routine work.

## Install

### From Codex

Ask Codex:

```text
Install the build-game skill from
https://github.com/ThanhNienHa/codex-build-game/tree/main/skills/build-game
```

Start a new Codex task after installation, then use:

```text
Use $build-game to inspect this project and deliver the smallest playable, tested improvement.
```

### Local development

Clone the repository, validate it, then copy `skills/build-game` into your Codex skills directory:

```powershell
python scripts/validate_repo.py
Copy-Item -Recurse skills/build-game "$env:USERPROFILE\.codex\skills\build-game"
```

Do not overwrite an existing installed skill without reviewing the diff first.

## Examples

```text
Use $build-game to turn this idea into the smallest testable vertical slice.
```

```text
Use $build-game to add a data-driven combo system with deterministic tests and playable feedback.
```

```text
Use $build-game with studio-full to review this Cocos release candidate for design, technical, and QA risks.
```

## Repository structure

```text
.codex-plugin/plugin.json   Codex plugin metadata
skills/build-game/          Installable Codex skill
scripts/validate_repo.py    Dependency-free repository checks
evals/                      Behavioral response contracts and grader fixtures
fixtures/                   Synthetic Phaser and Cocos maintenance tasks
.github/                    CI and contribution templates
```

## Principles

1. Playable evidence beats document existence.
2. Use the least process that safely fits the risk.
3. Prototype uncertainty before scaling production.
4. Reuse suitable project assets before creating new ones.
5. Keep gameplay rules testable outside engine scenes.
6. Keep Codex responses and progress updates concise.

## Validate a contribution

```powershell
python scripts/validate_repo.py
python -m unittest discover -s tests -v
python scripts/run_evals.py
python scripts/run_fixture_checks.py
python skills/build-game/scripts/validate_evidence.py skills/build-game/assets/evidence-manifest.example.json
python scripts/package_release.py
```

`run_evals.py` checks deterministic conformance examples. For substantial skill changes, also grade fresh independent Codex responses as described in [evals/README.md](evals/README.md).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Contributions should improve a concrete game-development workflow and include validation evidence.

## Maintainer automation

Every pull request runs deterministic repository, plugin, and skill validation. Maintainers can optionally enable the included Codex PR review workflow after adding an `OPENAI_API_KEY` repository secret. It runs read-only, only for trusted maintainers, and reviews changes against this repository's contribution and skill-quality rules.

See [docs/CODEX-FOR-OSS.md](docs/CODEX-FOR-OSS.md) for the project's public-maintainer readiness checklist and honest application guidance.

## Case studies

- [Cocos behavior rebuild: evidence over optimistic smoke tests](docs/case-studies/2026-08-cocos-parity-rebuild.md)
- [Cocos strategy game: presentation safety and real Preview evidence](docs/case-studies/2026-08-cocos-strategy-game.md)

## Project status

This repository is an early-stage open-source project. Validation and forward-test scenarios are included, but adoption and real-world maintainer impact must be earned and documented over time. See [ROADMAP.md](ROADMAP.md).

## License

MIT. See [LICENSE](LICENSE).

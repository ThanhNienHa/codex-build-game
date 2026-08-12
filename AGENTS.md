# Repository guidance

## Scope

Maintain an engine-aware but engine-neutral Codex game-development skill. Keep the supported engine scope limited to Phaser, Cocos Creator, and Unity unless maintainers explicitly approve an expansion.

## Changes

- Keep `skills/build-game/SKILL.md` concise and route details to one-level-deep references.
- Add instructions only when they prevent a repeated failure or enable a reusable workflow.
- Preserve proportional `solo`, `lean`, `full`, and optional `studio-full` behavior.
- Do not require documents, agents, gates, or user approvals for routine low-risk work.
- Keep Cocos guidance MCP-aware and require stopping an old preview before a new preview.
- Avoid vendor-specific tool names unless verified from the current tool schema.
- Use imperative wording and concise responses.

## Verification

Run `python scripts/validate_repo.py`, unit tests, behavioral evals, fixture checks, evidence/release validators, compatibility validation, clean-install smoke, and the plugin/skill validators in proportion to the change. Forward-test substantial workflow changes against a realistic game task without leaking the expected answer.

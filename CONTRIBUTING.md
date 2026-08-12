# Contributing

Thanks for improving Codex Build Game.

## Before opening a pull request

1. Open an issue for broad workflow, engine-support, or behavioral changes.
2. Keep the main `SKILL.md` small; put detailed guidance in a directly linked reference.
3. Explain the real failure mode or game-development task the change addresses.
4. Add or update validation when introducing a structural rule.
5. Run `python scripts/validate_repo.py`.
6. Run `python scripts/run_evals.py`.
7. Run `python scripts/run_fixture_checks.py` when fixtures or gameplay guidance change.
8. Forward-test substantial skill changes with a realistic prompt, grade the fresh response when a matching eval exists, and report the observed result.

## Pull request expectations

- One focused change per pull request.
- No generated game assets, credentials, engine caches, or proprietary project files.
- No unverified claims about engine APIs or MCP operations.
- No copied material without compatible licensing and attribution.
- Concise documentation with concrete acceptance criteria.
- Behavioral evals must grade complete response text; corpus keyword presence is not behavioral evidence.

By contributing, you agree that your contribution is licensed under the repository's MIT License.

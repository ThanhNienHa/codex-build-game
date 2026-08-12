# Compatibility and installation

Use this reference when installing, distributing, or claiming support for the skill/plugin or an engine workflow.

## Separate the surfaces

- The standalone `$build-game` skill is the reusable workflow and can be loaded by supported Codex skill surfaces.
- The `codex-build-game` plugin is the distribution package containing the skill.
- Plugin availability does not imply that every Codex surface supports plugins.

Consult the current official OpenAI documentation before making a current product-support claim. As verified on 2026-08-12, standalone skills are documented for the ChatGPT desktop app, Codex CLI, and IDE extension; plugins are documented for the ChatGPT desktop app and Codex CLI, while the IDE extension does not support plugins.

After installing a plugin, start a new chat/session before expecting bundled skills or tools. Codex can detect local skill changes automatically, but restart Codex if an updated standalone skill does not appear.

## Support levels

Use one label:

- `fixture-tested`: deterministic public fixture passes.
- `case-study`: anonymized project evidence exists, with its recorded limitations.
- `guidance-only`: instructions exist but no current public executable fixture proves the workflow.
- `not-supported`: intentionally outside scope.

Do not infer engine-version support from TypeScript compatibility alone. Record the engine/version actually observed, whether the editor/Preview/build ran, and which evidence is synthetic versus project-recorded.

The repository compatibility matrix is `compatibility/matrix.json`. Validate it with `python scripts/validate_compatibility.py`. Validate a packaged clean install with `python scripts/smoke_install.py <release.zip>`.

# Release readiness

Use this reference for release candidates, milestone promotion, platform packaging, or a request to decide whether a game may ship.

## Define the release target

Record the version, commit, platform, distribution channel, engine version, supported devices, and accepted non-goals. A release verdict applies only to that exact target; editor Preview cannot prove a native package and one desktop build cannot prove mobile support.

## Evaluate explicit gates

Use `assets/release-readiness.example.json` as the machine-readable shape. Give each gate a stable ID, category, required flag, status, freshness, evidence, and concise notes. Cover the categories that materially apply:

- gameplay and acceptance criteria;
- automated checks and deterministic regressions;
- playable input, UI, accessibility, and error-free runtime;
- performance, memory, lifecycle, and soak;
- platform build, signing, install, launch, update, and rollback;
- security, privacy, external SDKs, and secrets;
- asset provenance, licences, attribution, and store policy;
- operations, crash reporting, support, and recovery when applicable.

Mark irrelevant gates `NOT_APPLICABLE` with `required: false` and a reason. Do not make a required gate not applicable to avoid a blocker.

Evaluate the manifest with:

```text
python skills/build-game/scripts/evaluate_release.py <release-readiness.json>
```

## Verdict rules

- **FAIL:** a required gate failed.
- **CONCERNS:** a required gate is not run, historical, stale, or only partially satisfied; or a non-required gate has a material failure.
- **PASS:** every required gate passed with fresh evidence, every non-applicable gate has a reason, and no material concern remains.

The declared verdict must match the computed verdict. Never weaken a required gate after observing its result. Give the smallest dependency-ordered path from `FAIL` or `CONCERNS` to `PASS`.

Use `references/security.md` for MCP, asset, build, or external-integration risk. Use `references/evidence.md` for the underlying test and Preview artifacts.

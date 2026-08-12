# Verification evidence

Use this reference for vertical slices, milestone gates, Cocos Preview work, release reviews, or any task where fresh and historical evidence could be confused.

## Record evidence, not confidence

For every relevant check, record:

- the check name and command or interaction;
- `PASS`, `CONCERNS`, `FAIL`, `NOT_RUN`, or `NOT_APPLICABLE`;
- `fresh`, `historical`, `not-run`, or `not-applicable`;
- the observed time when known;
- a concise result and the artifact relative to the project when safe.

Use `assets/evidence-manifest.example.json` as the shape and validate a completed manifest with:

```text
python skills/build-game/scripts/validate_evidence.py <manifest.json>
```

Do not publish local absolute paths, credentials, personal data, proprietary assets, or private logs. A manifest may remain local to a private project; publish only a sanitized report with permission.

## Cocos Preview evidence

Use `assets/cocos-preview-report.template.md` for a Cocos playable check. Record:

1. Engine and version from project metadata.
2. MCP implementation/version when observable.
3. Previous Preview status and the exact session, process, or port targeted.
4. Confirmation that the old Preview stopped before a new one started.
5. New Preview identity and mode.
6. Real player input used to reach the affected flow.
7. Player-visible state and acceptance criteria observed.
8. Relevant console/runtime errors.
9. Screenshot or recording references when safe.
10. Whether the new Preview was stopped after verification.

If the previous Preview cannot be identified or stopped safely, do not launch another one. Mark the playable check `NOT_RUN` or `CONCERNS` and state the limitation.

Do not treat editor-side cold state, a debug hook, file existence, a listening port, or process survival as Browser Preview gameplay evidence. Label every artifact `fresh` or `historical`.

## Verdict consistency

- Use **PASS** only when all evidence required by the accepted scope is fresh or explicitly allowed historical evidence and no material blocker remains.
- Use **CONCERNS** when the result is usable but evidence or bounded risk remains.
- Use **FAIL** when a missing or failed requirement blocks the intended stage.

The overall verdict cannot be stronger than a required failed or not-run check. State the smallest action that would change `CONCERNS` or `FAIL` to `PASS`.

# Quality gates

Use gates for vertical slices, milestone transitions, risky integration, release candidates, or when requested. Do not gate every small change.

## Evidence

Check real content and current results:

- design/spec agrees with the implemented player outcome;
- dependencies and authoritative state ownership are clear;
- automated tests, type checks, lint, and build pass where configured;
- the affected flow boots and is playable;
- preview/console has no relevant errors;
- assets, accessibility, lifecycle, and target performance meet scope;
- playtest evidence exists when fun or clarity is claimed;
- blockers, regressions, and release risks are explicit.

Use one verdict:

- **PASS**: required evidence exists and no material blocker remains.
- **CONCERNS**: usable result with acknowledged bounded risk and a specific follow-up.
- **FAIL**: missing or failed evidence blocks the intended next stage.

Never treat an empty or template file as evidence. Mark unverifiable gameplay as `MANUAL CHECK NEEDED`, not `PASS`. Before finalizing, challenge the weakest assumption and re-run or re-read at least one relevant check. Give the minimal path to PASS.

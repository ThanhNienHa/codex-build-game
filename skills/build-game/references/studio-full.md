# Studio-full review

Use `studio-full` only when the user requests it or full-scope work has multiple independent risk domains whose review would materially improve the result. Examples: a vertical-slice gate, cross-system architecture, economy plus progression, multiplayer/persistence, major Cocos scene integration, performance certification, or release readiness.

Do not use it for small fixes, routine features, tuning, straightforward refactors, or tasks that fit one coherent context.

## Select specialists

Choose at most three roles based on actual risk; never spawn a fixed roster:

- **Game design/systems**: core loop, rules, economy, balance, player fantasy, edge cases.
- **Technical/engine**: architecture, state ownership, engine idioms, Cocos integration, data and lifecycle boundaries.
- **QA/playtest**: acceptance criteria, test evidence, regressions, failure recovery, playability.
- **Performance**: frame-time, memory, loading, pooling, hot paths, target-device budgets.
- **UX/accessibility**: clarity, input, HUD, onboarding, feedback, accessibility.
- **Art/asset pipeline**: asset reuse, consistency, import settings, animation/VFX/audio feasibility.
- **Release/operations**: build, packaging, telemetry, localization, security, rollback, compliance.

## Coordination

1. Define one bounded question and evidence set per specialist. Give raw project artifacts and acceptance criteria, not the primary agent's conclusion.
2. Run independent reviews in parallel. Use no more than three specialists plus the primary agent.
3. Prefer read-only review. Do not let specialists edit overlapping files. Parallel implementation is allowed only for clearly disjoint modules with explicit ownership and integration criteria.
4. Require each specialist to return: evidence inspected, findings by severity, verdict (`PASS`, `CONCERNS`, `FAIL`), and minimal actions.
5. Surface a blocked or failed specialist immediately. Do not silently omit it or fabricate consensus.
6. The primary agent resolves conflicts, verifies claims against source artifacts, makes or coordinates edits, runs integrated checks, and reports one concise decision.

Specialists advise; they do not override the user's intent or expand scope. Stop at one review round unless new evidence justifies another.

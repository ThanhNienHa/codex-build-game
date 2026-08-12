# Lightweight studio workflow

## Detect stage

Infer stage from evidence, not folder names:

- **Explore**: no stable concept or core loop; clarify player fantasy, verbs, audience, constraints, and anti-goals.
- **Prototype**: validate one uncertain fun or technical hypothesis with disposable work.
- **Vertical slice**: prove one short production-representative loop including input, rules, feedback, content, integration boundaries, and target performance.
- **Production**: extend validated patterns through thin stories while keeping main playable.
- **Polish/release**: fix clarity, accessibility, performance, reliability, packaging, analytics, legal, and regression gaps.

Projects may contain systems at different stages. Classify the affected system rather than forcing the whole repository into one stage.

## Choose process

- **Solo**: small bug, tuning, refactor, or disposable experiment. Use concise acceptance criteria, a test where valuable, and a playable check.
- **Lean (default)**: normal feature or system. Add a short spec, dependencies, non-goals, test evidence, implementation, review, and playable check.
- **Full**: cross-system or high-cost work, economy/persistence/networking, major architecture, milestone, or release. Add a system map/GDD, explicit decisions, risk review, test plan, playtests, and quality gate. Use optional `studio-full` only when up to three independent specialist reviews add real value.

Do not ask approval for routine in-scope file writes. Ask only when a missing choice materially changes the game, scope, architecture, external state, or destructive action.

## Production flow

Use this order and skip steps that add no decision value:

1. Define player fantasy and core loop.
2. Map MVP systems and dependencies.
3. Prototype the highest uncertainty.
4. Define architecture boundaries and tunable data.
5. Build and playtest a vertical slice.
6. Break validated scope into thin stories.
7. Implement, test, review, and keep playable.
8. Polish, regress, profile, and release.

Prefer one coherent agent. For eligible full-scope work, `studio-full` may run at most three risk-matched specialists in parallel while the primary agent owns synthesis and integration. Do not simulate a large studio.

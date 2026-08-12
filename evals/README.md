# Behavioral evals

Each case defines a realistic prompt, required behavior groups, and unsafe or disproportionate behavior patterns. The grader evaluates complete response text rather than searching the skill corpus.

Run the checked-in conformance examples:

```text
python scripts/run_evals.py
```

Grade a fresh Codex response:

```text
python scripts/run_evals.py --case presentation-authority --response response.md
```

Conformance examples test the deterministic grader; they are not evidence that a current model passed. Record independent forward-tests separately and do not give the agent the rubric or expected answer.

## Current v0.2.0 forward-test summary

Three independent passes were run against the revised skill without exposing these rubrics:

- presentation safety: passed `presentation-authority` after preserving authoritative state and requiring a clean Cocos Preview;
- missing Preview verdict: passed `missing-preview-verdict` after the rubric was corrected to accept equivalent Markdown and wording;
- Phaser brownfield fixture: reproduced the starter failure, implemented the one-line fix, passed the focused test, preserved the existing asset key, and reported the missing browser scene as a manual check.

These are current development-run observations, not a claim that every model or future version will behave identically.

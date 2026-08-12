# Codex Build Game pull request review

Review the checked-out pull-request merge commit. Do not edit files.

Prioritize actionable correctness and safety findings:

1. Does the skill remain concise and route detailed guidance through direct references?
2. Does the change preserve proportional `solo`, `lean`, `full`, and optional `studio-full` behavior?
3. Does it avoid unnecessary documents, approvals, specialists, and gates for routine work?
4. Are game claims tied to executable checks, preview, playtest, or other evidence rather than file existence?
5. Are Cocos MCP and Preview instructions safe, including stopping only the known previous preview?
6. Are asset reuse, licensing, secrets, and serialized scene/prefab relationships protected?
7. Are new references reachable and covered by deterministic validation or eval cases?

Report only material findings, ordered by severity, with exact file paths and concise fixes. If there are no actionable findings, say so and mention any remaining validation gap.

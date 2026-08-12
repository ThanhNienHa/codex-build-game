# Codex for Open Source readiness

Official program page: <https://developers.openai.com/community/codex-for-oss>

## Official eligibility summary

OpenAI invites core maintainers and maintainers of widely used public projects to apply. Projects that do not clearly fit may still apply when they play an important ecosystem role. API credits target projects using Codex in pull-request review, maintainer automation, release workflows, or other core open-source work. Access decisions remain OpenAI's.

## Current project position

This repository is technically prepared for public maintenance, but a newly published project cannot honestly claim broad use or ecosystem importance. Eligibility depends on real public activity and your role as a maintainer, not the number of repository files.

## Before applying

- [x] Prepare the repository for publication under your own GitHub account.
- [x] Replace installation URLs and add manifest repository/homepage fields.
- [x] Create versioned public releases and tags.
- [x] Enable branch protection and required deterministic CI.
- [x] Enable GitHub private vulnerability reporting and document the private reporting path.
- [x] Demonstrate active maintenance through merged pull requests, releases, and public follow-up issues.
- [x] Publish two anonymized real-use case studies without exposing private projects.
- [ ] Document independent external users/projects and measurable impact with permission.
- [ ] Enable the optional Codex PR review only when API credits or a protected API key are available.
- [ ] Explain why game-development workflows are important to the open-source ecosystem.
- [ ] Describe how credits would support PR review, compatibility maintenance, evals, and releases.

Do not invent stars, downloads, users, contributors, security needs, or adoption metrics. Apply with accurate evidence and explain the project's role even if it is still small.

## Current public evidence

- Versioned public releases, reproducible archives, checksums, and clean-install validation.
- Required CI covering repository structure, behavioral eval conformance, public fixtures, and evidence-schema validation.
- Two anonymized Cocos case studies with fresh automated evidence and bounded verdicts.
- Public issues derived from observed failure modes rather than speculative feature lists.
- An explicit game/MCP threat model and compatibility claims tied to official OpenAI documentation or public evidence.

Game development is an important open-source workflow because changes cross deterministic rules, engine serialization, licensed assets, interactive verification, performance, packaging, and platform boundaries. General coding checks can pass while the player-visible game remains broken, unsafe to release, or legally undistributable; this project makes those missing gates explicit and reusable.

Credits would support trusted Codex PR review, forward-testing across supported engines and Codex surfaces, compatibility maintenance, release evidence automation, and public fixture/case-study expansion. They would not be used to claim adoption that has not been independently demonstrated.

This proves active maintenance and real private-project use. It does not prove broad public adoption or independent ecosystem impact.

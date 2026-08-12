# Event and input handling

Use this reference for controls, engine callbacks, WebSockets, live-platform events, networking, reconnects, or bursty asynchronous input.

## Normalize at the boundary

Convert raw input into a small provider-neutral command or event schema before it reaches gameplay. Include only values the game needs, such as stable event ID, source, actor ID, kind, validated payload, and source timestamp when trustworthy.

Validate types, lengths, ranges, identifiers, and permissions. Reject malformed or privileged input before it enters the gameplay queue. Keep secrets and provider credentials outside exported clients.

## Define delivery semantics

Decide and test:

- whether duplicates are possible and the bounded deduplication window;
- ordering within one sender and across senders;
- how stale, future, or out-of-phase messages behave;
- queue capacity and overflow policy;
- per-user and global rate limits;
- reconnect, retry, and backoff behavior;
- whether batches coalesce movement, counters, or repeated effects;
- which events must never be silently dropped.

Do not assume exactly-once delivery. Make gameplay handlers idempotent where practical, or make duplicate rejection explicit.

## Separate ingress from simulation

Let adapters receive and normalize events. Let an application queue admit, order, deduplicate, and schedule commands. Let deterministic gameplay rules consume the admitted commands. Keep provider APIs, WebSockets, DOM, and engine input callbacks out of domain rules.

Drain queues at a bounded point in the update loop. Avoid one animation, sound, or network callback per raw burst event; aggregate when the player-visible meaning is preserved.

Clean up listeners, timers, subscriptions, and reconnect loops on scene exit or shutdown. Prevent an old session from dispatching into a new match.

## Observe and test

Expose bounded diagnostics for accepted, rejected, duplicate, stale, rate-limited, coalesced, and dropped events. Do not log secrets or personal payloads.

Test contract fixtures for each adapter and deterministic sequences for ordering, duplicates, overflow, reconnect, and reset. Provide an offline simulator for external event streams so core gameplay can be developed and replayed without a live provider.

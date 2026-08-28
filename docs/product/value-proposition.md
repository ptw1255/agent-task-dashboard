# Value proposition

## Why

The dashboard should earn its place by reducing coordination ambiguity, not by adding a second system users must keep synchronized. Its strongest present value is fast, local legibility.

## Value proposition canvas

### Customer profile

| Jobs | Pains | Gains sought |
|---|---|---|
| Track multiple agent tasks | Context scattered across prompts and terminals | One status view |
| Match work to specialists | Capability catalog is hard to remember | Searchable agent descriptions |
| Resume work after interruption | State held in memory | Persistent local board |
| Communicate progress | Raw transcripts are too detailed | Compact task/owner/status summary |

### Value map

| Surface | Pain reliever | Gain creator |
|---|---|---|
| Three-column board | Externalizes task state | Rapid visual scan |
| Priority and agent filters | Reduces board noise | Focused views |
| Agent search/categories | Reduces specialist-selection friction | Capability discovery |
| Local JSON persistence | Survives browser refresh/restart | Low-infrastructure continuity |
| REST API | Separates UI and state operations | Future integration seam |

## Alternatives

| Alternative | Strength | Cost/tradeoff |
|---|---|---|
| Terminal/session history | No extra maintenance | Hard to scan and reconcile |
| Markdown checklist | Versionable and portable | Weak filtering and state interaction |
| General kanban tool | Mature collaboration and reliability | More setup; agent catalog is separate |
| GitHub Issues/Projects | Durable links and team workflow | Heavier for private local experiments |
| Runtime-native task list | Closest to execution truth | May not support cross-session planning/catalog |

## Differentiation

- Agent catalog and task board share one view (`agent_dashboard.html`).
- The local server uses only Python standard-library infrastructure for core operation (`agent_task_server.py`).
- Assignment, filtering, and status updates are low-friction.
- Honest positioning can distinguish manual tracking from future runtime orchestration (`AGENT_GUIDE.md`).

## Proof and limits

**Evidence:** task CRUD and stats endpoints are implemented in `agent_task_server.py`; the UI calls them in `agent_dashboard.html`.
**Evidence:** status drag/drop and 30-second refresh are implemented in `agent_dashboard.html`.
**Evidence:** `AGENT_GUIDE.md` describes manual invocation as the current workaround.
**Limit:** the repository supplies no user evidence that the board reduces misses, saves time, or improves agent choice.

## Assumptions

- The server is used in a trusted local context.
- One JSON writer is the common case.
- Task metadata can remain concise and non-sensitive.
- The agent catalog is maintained separately from runtime discovery.

## Hypotheses

- Clear labels for “planned,” “manually running,” and “runtime confirmed” reduce status misinterpretation.
- An inline detail/activity view reduces dependence on terminal history.
- Keyboard status controls improve completion for non-mouse and narrow-screen use.
- Linking tasks to external runs provides more value than embedding full output.

## Positioning

For people coordinating multiple specialized coding agents locally, Agent Task Dashboard is a lightweight board that keeps tasks, intended specialists, priorities, and status visible. Unlike a generic checklist, it supports capability discovery and focused board views; unlike an orchestration platform, it does not claim that assignment equals execution.

# Product brief

## Why

Agent work becomes hard to coordinate when task intent lives in prompts, status lives in memory, and specialist capabilities live in separate documentation. A board can make the work legible, but it must not blur the line between **tracking** an assignment and **executing** it.

**Evidence:** the dashboard exposes tasks, agent cards, three statuses, priorities, and statistics (`agent_dashboard.html`). `AGENT_GUIDE.md` states invocation is manual today.
**Inference:** the immediate product value is shared operator context, not autonomous orchestration.

## Thesis

If a local operator can capture work, associate the right specialist, and update state in one low-friction board, then fewer tasks will be forgotten or ambiguously owned—even before direct runtime integration exists.

## What exists

- Python standard-library HTTP server and REST endpoints for task CRUD, agents, dispatch-state updates, and stats (`agent_task_server.py`).
- Single-page board with agent search, category collapse, agent and priority filters, creation modal, drag-and-drop status updates, manual refresh, and 30-second polling (`agent_dashboard.html`).
- JSON-file persistence (`tasks.json`, `agents.json`).
- Guidance describing specialist categories and manual workflows (`AGENT_GUIDE.md`).

## Scope

- Single-operator/local coordination board.
- Task title, description, priority, optional agent, and workflow status.
- Agent catalog discovery and filtering.
- Visible counts and completion summary.
- Honest distinction between assignment metadata and actual execution.

## Non-goals

- Claiming a task has run because it was assigned or moved.
- Replacing an agent runtime, issue tracker, or durable multi-user project system.
- Storing credentials, sensitive prompts, or execution output.
- Inferring productivity from agent or task counts.
- Adding authentication, remote hosting, or enterprise controls without an explicit product decision.

## Principles

1. **State must mean one thing.** “In progress” is an operator assertion, not runtime proof.
2. **Visibility before automation.** Make work and ownership legible first.
3. **Low ceremony.** Capture a task faster than maintaining a separate spreadsheet.
4. **Recoverable interaction.** Failed updates stay visible and can be retried.
5. **Local-first by default.** Match the current server/file architecture.
6. **No productivity theater.** Counts describe board records, not quality or impact.

## Known product gaps

| Gap | Evidence | Product implication |
|---|---|---|
| Runtime dispatch is not integrated | `AGENT_GUIDE.md`; dispatch function only mutates JSON | UI copy should say “assign,” not imply execution |
| Errors are console-only | `agent_dashboard.html` catch blocks | Users may not know a create/drop/refresh failed |
| Empty/loading states are implicit | rendering clears containers; no dedicated states | Blank board can be misread |
| JSON writes are the persistence boundary | `agent_task_server.py` | Concurrency and recovery need explicit decisions |
| Drag-and-drop is primary for status | `agent_dashboard.html` | Keyboard and touch alternatives are needed |

## Open questions

- Is the primary unit a one-off task, an agent run, or a durable workflow?
- Which states represent operator intent versus runtime-observed truth?
- Should task details retain links to external evidence rather than embedding content?
- Is multi-user use desirable, or would it undermine the local simplicity?

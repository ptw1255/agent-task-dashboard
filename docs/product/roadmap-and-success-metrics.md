# Roadmap and success metrics

## Why

The product should first become a trustworthy manual coordination surface. Direct dispatch is valuable only after state semantics, persistence feedback, and recovery are credible.

## Phased roadmap

| Phase | Outcome | Candidate scope | Exit evidence |
|---|---|---|---|
| 0 — Truthful baseline | Understand how the board is used | State vocabulary study; task/run distinction; privacy-safe event taxonomy | Operators consistently explain what each state means |
| 1 — Trustworthy local board | No silent UI failures | Loading/empty/error states; keyboard moves; last-refresh indicator; rollback on failed save | Seeded failures are noticed and recovered |
| 2 — Durable task context | Tasks survive and conflicts are legible | Record version/timestamp; backup/recovery; optional external links; schema validation | Recovery and conflict tests pass |
| 3 — Execution reconciliation | Board can reference runtime truth | Link/import run status; manual vs observed badges; completion evidence | Active/done mismatches can be detected |
| 4 — Deliberate orchestration | Safe launch for supported runtimes | Explicit preview, permissions, start/cancel semantics, audit trail | Controlled pilot meets guardrails |

No phase is a delivery commitment.

## Hypotheses

1. Explicit “manual state” labels reduce mistaken assumptions about agent execution.
2. In-context error recovery prevents more lost updates than faster polling.
3. Capability search reduces reassignment compared with name-only selection.
4. External run links materially reduce board/runtime reconciliation time.
5. A local-first mode remains preferable for individual workflows even if collaboration is added.

## Metrics

| Type | Metric | Definition |
|---|---|---|
| Leading | Capture completion | created tasks / task-creation dialogs opened |
| Leading | Capability-search success | searches followed by assignment without immediate reassignment / searches |
| Leading | State reconciliation coverage | active/done tasks with manual confirmation or run reference / active/done tasks |
| Leading | Error recovery | failed operations successfully retried or intentionally abandoned / failed operations |
| Lagging | State reconstruction time | time to correctly summarize active work after reopening |
| Lagging | Forgotten-task proxy | overdue/unreviewed planned tasks found in periodic review / planned tasks |
| Lagging | Duplicate-work proxy | tasks marked duplicate due to missing prior context / completed tasks |
| Guardrail | False execution implication | users interpreting assignment as runtime start in comprehension tests |
| Guardrail | Silent persistence failure | failed writes without visible user feedback; target zero |
| Guardrail | Lost task records | acknowledged saved records absent after restart; target zero |
| Guardrail | Sensitive content telemetry | task title/description/output in analytics; target zero |

Baselines and numeric targets are TBD.

## Instrumentation

Proposed privacy-safe events:

| Event | Properties |
|---|---|
| `board_loaded` | outcome, latency bucket, task-count bucket, agent-count bucket |
| `task_created` | priority, assigned boolean, description-present boolean |
| `agent_search` | query-length bucket, result-count bucket, assignment-followed boolean |
| `task_state_requested` | from, to, input method |
| `task_state_result` | from, to, success/error category, latency |
| `board_refreshed` | automatic/manual, success, data-age bucket |
| `run_reference_linked` | runtime type category, board state |

Do not capture query text, task content, URLs, agent outputs, or identities.

## Experiments

| Experiment | Design | Success signal | Guardrail |
|---|---|---|---|
| State comprehension | Current labels vs “Planned / Active-manual / Done-manual” | More correct answers about execution truth | Capture time does not materially worsen |
| Status interaction | Drag only vs drag + menu/keyboard | Higher completion across input modes | No increase in wrong-column moves |
| Error recovery | Console error vs inline rollback/retry | More failures noticed and resolved | No duplicate write |
| Agent selection | Name list vs capability results | Lower immediate reassignment | Search remains fast |
| Run linking | Manual state only vs optional run link | Lower reconstruction time | Sensitive output is not copied into tasks |

## Review order

Evaluate guardrails and status comprehension before engagement. More card moves or higher completion percentage are not success if users misunderstand what the states prove.

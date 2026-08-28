# Pain points and opportunity costs

## Why

There are no repository analytics or user-study results. These chains and formulas define what to observe without inventing actual performance.

## Pain severity and consequence chains

| Pain | Severity | Frequency proxy | Consequence chain |
|---|---|---|---|
| Task state held in memory | Medium–high | Context switches/day; reopened sessions | Interruption → state forgotten → duplicated or omitted work → rework/delay |
| Wrong specialist selected | Medium | Reassignments/task; general-agent share | Weak discoverability → familiar agent reused → extra handoffs or lower-quality fit |
| Assignment mistaken for execution | High | State corrections; “busy” without run reference | UI state change → false belief work started → dependency waits → schedule slip |
| Save/refresh failure is invisible | High | API errors/session; stale intervals | Request fails → console-only error → user assumes persistence → later state loss |
| Manual board/runtime reconciliation | Medium | status edits/run; unlinked active tasks | Work starts elsewhere → board stays stale → collaborator acts on old state |
| Drag-only status control | Medium accessibility impact | keyboard/touch status attempts | Input mismatch → blocked update → inaccurate state or abandonment |
| JSON concurrency | Medium in multi-process use | conflicting writes; parse failures | overlapping edits → last writer wins/corruption → lost tasks |

Severity is a product assessment, not observed incident frequency.

## Opportunity-cost formulas

- **Reconstruction cost/week** = `interruptions × average minutes spent reconstructing task/agent/status`.
- **Coordination overhead/task** = `capture + agent search + manual invocation + status reconciliation minutes`.
- **Duplicate-work rate** = `tasks repeated because prior state was unclear / completed tasks`.
- **Stale-board exposure** = `sum(now − last confirmed refresh)` across active sessions.
- **Selection churn** = `tasks reassigned before completion / assigned tasks`.
- **Unlinked execution rate** = `active board tasks without external run reference / active tasks`.
- **Persistence failure rate** = `failed create/update/delete operations / attempted write operations`.
- **Accessibility completion gap** = `keyboard-only task completion rate − pointer task completion rate` (compare magnitude; do not identify users).

All baselines are TBD.

## Risk of inaction

- The board becomes a decorative duplicate of terminal state.
- Users may make dependency decisions from stale or manually asserted status.
- Missing error feedback erodes trust after the first lost update.
- A larger catalog increases search burden if capabilities drift from reality.
- Multi-user adoption on file persistence creates correctness expectations the architecture does not meet.

## What not to optimize

- Raw task count, because splitting work inflates it.
- Completion percentage without complexity or quality context.
- “Active agents” as productivity; current busy state is mutable metadata.
- Time-to-done alone, which can reward premature status changes.

## Prioritization

Prioritize in this order:

1. semantic correctness of status;
2. visible persistence/refresh failures;
3. accessible interaction;
4. reconciliation with execution evidence;
5. speed and visual density.

This ordering follows the product thesis; it is not a measured user ranking.

# Product portfolio: Agent Task Dashboard

## Why this product exists

People coordinating specialized agents need a compact answer to three questions: what work exists, who is associated with it, and what state is it in. A local visual board can reduce coordination memory without pretending that a card movement actually runs an agent.

## From why to what

1. [Product brief](product-brief.md)
2. [Users and JTBD](users-and-jtbd.md)
3. [Value proposition](value-proposition.md)
4. [Pain points and opportunity costs](pain-points-and-opportunity-costs.md)
5. [Wireframes](wireframes.md)
6. [Roadmap and success metrics](roadmap-and-success-metrics.md)

## Evidence discipline

- **Evidence:** observable in repository docs or code.
- **Inference:** plausible product meaning derived from evidence.
- **Hypothesis:** testable belief awaiting usage/research evidence.
- **Assumption:** unverified operating constraint.

### Evidence register

| Claim | Type | Source |
|---|---|---|
| Tasks move among backlog, in-progress, and done. | Evidence | `README.md`; `agent_dashboard.html` task board and drop handler |
| Users can create tasks, filter by priority/agent, search agents, refresh, and view summary stats. | Evidence | `agent_dashboard.html`; `agent_task_server.py` |
| Data persists in local JSON files. | Evidence | `agent_task_server.py` (`TASKS_FILE`, `AGENTS_FILE`) |
| “Dispatch” updates dashboard records but does not invoke an agent. | Evidence | `agent_task_server.py` (`dispatch_task_to_agent`); `AGENT_GUIDE.md` (“Integration Notes”) |
| The intended operator is a person coordinating agent work. | Inference | Repository name, UI, and `AGENT_GUIDE.md` |

No adoption, productivity, accuracy, completion-time, or business-result claim is supported by the repository.

# AI Agent Leveraging Guide

Your dashboard now has **33 specialized agents** organized into 5 categories. Here's how to leverage each one effectively.

## 🎯 Quick Reference

| Category | Count | Best For |
|----------|-------|----------|
| ⚡ Core | 5 | Essential development tasks |
| 🦸 Superpowers | 13 | Workflow automation & best practices |
| 🔧 Feature Dev | 3 | Feature architecture & deep analysis |
| 📋 Feedback | 11 | Specialized reviews & assessments |
| 🔌 MCP | 1 | Documentation lookup |

---

## ⚡ Core Agents (5)

### **Bash Agent**
**Use when:** You need to execute commands, git operations, or terminal tasks
**Example tasks:**
- "Run all tests in the project"
- "Create a new git branch and switch to it"
- "Install project dependencies"

### **Explore Agent**
**Use when:** You need fast codebase exploration or pattern searches
**Example tasks:**
- "Find all API endpoints in the project"
- "Locate where authentication is implemented"
- "Show me all database models"

### **General Purpose Agent**
**Use when:** Complex multi-step tasks requiring full toolset
**Example tasks:**
- "Refactor the user service to use async/await"
- "Add error handling to all API routes"
- "Implement a new feature with tests"

### **Plan Agent**
**Use when:** You need implementation plans before coding
**Example tasks:**
- "Plan the implementation of a payment system"
- "Design the architecture for a new microservice"
- "Create a step-by-step plan for database migration"

### **Code Review Agent**
**Use when:** You need code review with high signal-to-noise
**Example tasks:**
- "Review the authentication changes in PR #42"
- "Check this module for security vulnerabilities"
- "Analyze recent commits for bugs"

---

## 🦸 Superpowers Agents (13)

### **TDD Agent**
**Use when:** Writing tests before implementation
**Example tasks:**
- "Create tests for the new user registration feature"
- "Add test coverage for the payment module"

### **Debug Agent**
**Use when:** Investigating bugs or unexpected behavior
**Example tasks:**
- "Debug why login fails with valid credentials"
- "Investigate memory leak in the worker process"

### **Verification Agent**
**Use when:** Need to verify work before claiming complete
**Example tasks:**
- "Verify all tests pass before merging"
- "Confirm the feature works as specified"

### **Git Worktree Agent**
**Use when:** Need isolated workspace for feature development
**Example tasks:**
- "Create worktree for feature/user-dashboard"
- "Set up isolated environment for experiment"

### **Branch Finisher Agent**
**Use when:** Completing a development branch
**Example tasks:**
- "Finish feature branch and prepare for merge"
- "Create PR for completed authentication work"

### **Brainstorm Agent**
**Use when:** Exploring designs before implementation
**Example tasks:**
- "Brainstorm approaches for real-time notifications"
- "Design the user onboarding flow"

### **Plan Writer Agent**
**Use when:** Creating detailed implementation plans
**Example tasks:**
- "Write detailed plan for API v2 migration"
- "Document steps for adding GraphQL support"

### **Plan Executor Agent**
**Use when:** Executing written plans with checkpoints
**Example tasks:**
- "Execute the plan in docs/plans/api-migration.md"
- "Implement the database refactoring plan"

### **Subagent Coordinator**
**Use when:** Coordinating multiple agents in current session
**Example tasks:**
- "Coordinate agents to build feature in parallel"
- "Orchestrate multi-agent implementation"

### **Parallel Dispatcher**
**Use when:** Multiple independent tasks to run in parallel
**Example tasks:**
- "Run tests and build docs simultaneously"
- "Update multiple services in parallel"

### **Review Requester**
**Use when:** Requesting code reviews for completed work
**Example tasks:**
- "Request review for completed feature"
- "Verify work meets requirements before merge"

### **Review Responder**
**Use when:** Responding to code review feedback
**Example tasks:**
- "Address feedback from PR review"
- "Implement suggested changes from code review"

### **Skill Writer Agent**
**Use when:** Creating or editing skills
**Example tasks:**
- "Create new skill for database migrations"
- "Update existing deployment skill"

---

## 🔧 Feature Development Agents (3)

### **Feature Code Reviewer**
**Use when:** Deep code review for bugs, security, quality
**Example tasks:**
- "Review entire authentication system for vulnerabilities"
- "Check payment processing for security issues"

### **Feature Code Explorer**
**Use when:** Deep codebase analysis and architecture mapping
**Example tasks:**
- "Map the entire request flow from API to database"
- "Document how the caching system works"

### **Feature Architect**
**Use when:** Designing new feature architectures
**Example tasks:**
- "Design architecture for notification system"
- "Create blueprint for adding multi-tenancy"

---

## 📋 Feedback Agents (11)

### **Design Lead**
**Use when:** UI/UX review needed
**Example tasks:**
- "Review dashboard design for accessibility"
- "Evaluate user onboarding flow"

### **Visionary PM**
**Use when:** Strategy needs inspiration
**Example tasks:**
- "Review product strategy document"
- "Evaluate roadmap for inspiration"

### **Pragmatic PM**
**Use when:** Specs need execution clarity
**Example tasks:**
- "Review PRD for measurable outcomes"
- "Evaluate feature spec for clarity"

### **Strategy War Room**
**Use when:** Comprehensive multi-perspective review needed
**Example tasks:**
- "Full review of Q2 strategy"
- "Comprehensive evaluation of new feature proposal"

### **Technical Architect**
**Use when:** Architecture decisions need review
**Example tasks:**
- "Review microservices architecture design"
- "Evaluate data flow for new system"

### **Cloud Architect**
**Use when:** Azure/cloud infrastructure review
**Example tasks:**
- "Review Azure deployment architecture"
- "Evaluate scaling strategy"

### **Security Reviewer**
**Use when:** Security and privacy review needed
**Example tasks:**
- "Review authentication system for security"
- "Evaluate data handling for GDPR compliance"

### **Engineering Manager**
**Use when:** Assessing engineering execution
**Example tasks:**
- "Review implementation plan for ROI"
- "Evaluate technical spec for actionability"

### **Engineering Pragmatist**
**Use when:** Checking for over-engineering
**Example tasks:**
- "Review design for unnecessary complexity"
- "Evaluate if solution is too complex"

### **Platform Health**
**Use when:** Performance and reliability review
**Example tasks:**
- "Review monitoring strategy"
- "Evaluate performance optimization plan"

### **Capacity Estimator**
**Use when:** Estimating costs and capacity
**Example tasks:**
- "Estimate storage costs for new feature"
- "Calculate COGS for scaling plan"

---

## 🔌 MCP Agents (1)

### **Context7 Docs Agent**
**Use when:** Need up-to-date library documentation
**Example tasks:**
- "Look up latest React hooks documentation"
- "Find examples for Express middleware"

---

## 🚀 How to Use the Dashboard

### 1. **Browse Agents**
- Agents organized in collapsible categories
- Search bar to filter agents by name or capability
- Click category headers to expand/collapse

### 2. **Create Tasks**
- Click "➕ New Task"
- Fill in details and assign to specific agent
- Agent receives task in their backlog

### 3. **Assign Tasks**
- Drag tasks to "In Progress" when agent starts
- Agent card shows active status
- Drag to "Done" when complete

### 4. **Filter View**
- Click any agent card to filter tasks
- See only tasks for that agent
- Click again to clear filter

### 5. **Search Agents**
- Use search bar to find agents by capability
- Example: Search "security" shows Security Reviewer
- Example: Search "test" shows TDD Agent, Verification Agent

---

## 💡 Workflow Examples

### **Feature Development Workflow**
1. **Brainstorm Agent** - Design the feature
2. **Plan Writer Agent** - Create implementation plan
3. **General Purpose Agent** - Implement the feature
4. **TDD Agent** - Write tests
5. **Verification Agent** - Verify tests pass
6. **Feature Code Reviewer** - Review for bugs/security
7. **Review Requester** - Request final review

### **Bug Investigation Workflow**
1. **Debug Agent** - Investigate the bug
2. **Explore Agent** - Find related code
3. **General Purpose Agent** - Fix the issue
4. **Verification Agent** - Verify fix works
5. **Code Review Agent** - Review the fix

### **Architecture Review Workflow**
1. **Feature Architect** - Design the architecture
2. **Technical Architect** - Review system design
3. **Cloud Architect** - Review infrastructure
4. **Security Reviewer** - Check security
5. **Engineering Pragmatist** - Check for over-engineering
6. **Strategy War Room** - Final comprehensive review

---

## 🎯 Pro Tips

1. **Assign by Specialty** - Match task to agent's capabilities
2. **Use Search** - Find the right agent quickly
3. **Workflow Chains** - Create task sequences (Design → Plan → Implement → Review)
4. **Parallel Tasks** - Use Parallel Dispatcher for independent tasks
5. **Review Everything** - Use feedback agents before finalizing designs

---

## 📊 Agent Statistics

Track which agents are most productive:
- Completion counts shown on each card
- Active/busy status indicates current work
- Filter by agent to see their task history

---

## 🔗 Integration Notes

**Current Status:** Dashboard tracks tasks, manual agent invocation via Claude Code

**Future (Phase 2):** Direct integration to dispatch tasks automatically to Claude Code agents

**Workaround:**
1. Create task in dashboard
2. Copy task details
3. Manually invoke agent in Claude Code CLI
4. Update task status in dashboard

---

**Last Updated:** February 11, 2026
**Total Agents:** 33
**Dashboard Version:** 2.0

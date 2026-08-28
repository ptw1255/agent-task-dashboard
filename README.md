# AI Agent Task Management Dashboard

A full-stack web application for managing AI agent tasks with a Python backend and modern dark-themed frontend.

## 🚀 Quick Start

### Start the Server

```bash
# Option 1: Using the start script
./start_dashboard.sh

# Option 2: Direct Python
python3 agent_task_server.py
```

### Access the Dashboard

Open your browser to: **http://localhost:8809**

## 📁 Project Structure

```
agent-task-dashboard/
├── agent_task_server.py      # Backend REST API server
├── agent_dashboard.html       # Frontend UI
├── tasks.json                 # Task data storage
├── agents.json                # Agent configuration
├── start_dashboard.sh         # Quick launcher script
└── README.md                  # This file
```

## 🎮 Using the Dashboard

### View Tasks
- Tasks organized in 3 columns: Backlog, In Progress, Done
- Each card shows: priority, title, description, assigned agent

### Create Tasks
1. Click **"➕ New Task"** button
2. Fill in: title, description, priority, agent (optional)
3. Click **"Create Task"**
4. Task appears in Backlog column

### Move Tasks
- **Drag and drop** tasks between columns
- Status updates automatically

### Filter Tasks
- Click **agent cards** in sidebar to filter by agent
- Click **priority buttons** in toolbar (All, High, Medium, Low)
- Click same filter again to clear

### Refresh Data
- Click **"🔄 Refresh"** button
- Dashboard auto-refreshes every 30 seconds

## 🔧 API Endpoints

### Tasks
- `GET /api/tasks` - List all tasks
- `POST /api/tasks` - Create new task
- `GET /api/tasks/:id` - Get task details
- `PUT /api/tasks/:id` - Update task
- `DELETE /api/tasks/:id` - Delete task

### Agents
- `GET /api/agents` - List all agents
- `POST /api/agents/:id/dispatch` - Dispatch task to agent

### Stats
- `GET /api/stats` - Get dashboard statistics

## 🤖 Available Agents

1. **Explore Agent** - Fast codebase exploration, pattern search, file analysis
2. **Task Agent** - Command execution, tests, builds, linting
3. **General Purpose Agent** - Complex multi-step tasks, full toolset access
4. **Code Review Agent** - Code review, security analysis, bug detection

## 🎯 Customization

### Change Port
Edit `PORT = 8809` in `agent_task_server.py`

### Add Custom Agents
Edit `DEFAULT_AGENTS` array in `agent_task_server.py`

### Modify UI Theme
Edit CSS variables in `agent_dashboard.html`:
```css
:root {
    --bg-primary: #0a0e1a;
    --accent-blue: #3b82f6;
    /* ... other colors */
}
```

## 🔨 Technologies

- **Backend:** Python 3.8+ (http.server, json, uuid)
- **Frontend:** Vanilla JavaScript (ES6+), HTML5, CSS3
- **Storage:** JSON files
- **Architecture:** RESTful API, Single-page application

## 📊 Current Status

The dashboard is running with:
- ✅ 3 sample tasks pre-loaded
- ✅ 4 AI agents configured
- ✅ REST API with 10 endpoints
- ✅ Drag-and-drop task management
- ✅ Real-time statistics
- ✅ Auto-refresh every 30 seconds

## 🚧 Future Enhancements

### Phase 2: Claude Code Integration
- Bridge to Claude Code CLI/API
- Actual task dispatching to real Claude agents
- Agent response handling
- Status update automation

### Additional Features
- GitHub Issues sync
- Task history tracking
- Comments and discussions
- File attachments
- Search functionality
- Time tracking
- Notifications

## 📞 Support

Server running on: http://localhost:8809
Process ID: Check with `lsof -i :8809`

To stop the server: Press Ctrl+C in the terminal running the server

---

**Built:** February 11, 2026
**Version:** 1.0

"""
Agent Task Management Server
REST API for managing AI agent tasks and assignments.

Usage: python agent_task_server.py
Then open http://localhost:8809 in your browser.
"""

import http.server
import json
import os
import socketserver
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime
import uuid
import traceback

PORT = 8809
BASE_DIR = Path(__file__).parent
DASHBOARD_PATH = BASE_DIR / "agent_dashboard.html"
TASKS_FILE = BASE_DIR / "tasks.json"
AGENTS_FILE = BASE_DIR / "agents.json"

# Default agents configuration
DEFAULT_AGENTS = [
    {
        "id": "explore-agent",
        "name": "Explore Agent",
        "type": "explore",
        "status": "idle",
        "currentTask": None,
        "completedTasks": 0,
        "capabilities": ["Fast codebase exploration", "Pattern search", "File analysis", "Quick answers"],
        "description": "Specialized for exploring codebases and answering questions about code"
    },
    {
        "id": "task-agent",
        "name": "Task Agent",
        "type": "task",
        "status": "idle",
        "currentTask": None,
        "completedTasks": 0,
        "capabilities": ["Command execution", "Tests", "Builds", "Linting", "Dependency management"],
        "description": "Executes commands with verbose output (tests, builds, lints, installs)"
    },
    {
        "id": "general-purpose-agent",
        "name": "General Purpose Agent",
        "type": "general-purpose",
        "status": "idle",
        "currentTask": None,
        "completedTasks": 0,
        "capabilities": ["Complex multi-step tasks", "Full toolset access", "High-quality reasoning", "Code editing"],
        "description": "Full-capability agent for complex tasks requiring complete toolset"
    },
    {
        "id": "code-review-agent",
        "name": "Code Review Agent",
        "type": "code-review",
        "status": "idle",
        "currentTask": None,
        "completedTasks": 0,
        "capabilities": ["Code review", "Security analysis", "Bug detection", "Diff analysis"],
        "description": "Reviews code changes with high signal-to-noise ratio"
    }
]

# Sample tasks for initial setup
SAMPLE_TASKS = [
    {
        "id": str(uuid.uuid4()),
        "title": "Analyze codebase structure",
        "description": "Explore the project and document the main components and architecture",
        "agent": None,
        "status": "backlog",
        "priority": "high",
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat(),
        "githubIssue": None,
        "tags": ["exploration", "documentation"]
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Run all tests",
        "description": "Execute the test suite and report any failures",
        "agent": "task-agent",
        "status": "in-progress",
        "priority": "high",
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat(),
        "githubIssue": None,
        "tags": ["testing"]
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Review security vulnerabilities",
        "description": "Scan for common security issues and suggest fixes",
        "agent": None,
        "status": "backlog",
        "priority": "medium",
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat(),
        "githubIssue": None,
        "tags": ["security", "review"]
    }
]

# Initialize data files
if not TASKS_FILE.exists():
    TASKS_FILE.write_text(json.dumps(SAMPLE_TASKS, indent=2))

if not AGENTS_FILE.exists():
    AGENTS_FILE.write_text(json.dumps(DEFAULT_AGENTS, indent=2))


def load_json_file(filepath):
    """Load JSON data from file with error handling."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return [] if filepath.name == "tasks.json" else DEFAULT_AGENTS


def save_json_file(filepath, data):
    """Save JSON data to file with error handling."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving {filepath}: {e}")
        return False


def get_tasks():
    """Load all tasks."""
    return load_json_file(TASKS_FILE)


def save_tasks(tasks):
    """Save all tasks."""
    return save_json_file(TASKS_FILE, tasks)


def get_agents():
    """Load all agents."""
    return load_json_file(AGENTS_FILE)


def save_agents(agents):
    """Save all agents."""
    return save_json_file(AGENTS_FILE, agents)


def create_task(task_data):
    """Create a new task."""
    tasks = get_tasks()
    task = {
        "id": str(uuid.uuid4()),
        "title": task_data.get("title", "Untitled Task"),
        "description": task_data.get("description", ""),
        "agent": task_data.get("agent", None),
        "status": task_data.get("status", "backlog"),
        "priority": task_data.get("priority", "medium"),
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat(),
        "githubIssue": task_data.get("githubIssue", None),
        "tags": task_data.get("tags", [])
    }
    tasks.append(task)
    save_tasks(tasks)
    return task


def update_task(task_id, updates):
    """Update an existing task."""
    tasks = get_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[i].update(updates)
            tasks[i]["updated"] = datetime.now().isoformat()
            save_tasks(tasks)
            return tasks[i]
    return None


def delete_task(task_id):
    """Delete a task."""
    tasks = get_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return True


def dispatch_task_to_agent(agent_id, task_id):
    """Dispatch a task to an agent."""
    agents = get_agents()
    tasks = get_tasks()

    agent = next((a for a in agents if a["id"] == agent_id), None)
    if not agent:
        return {"error": "Agent not found"}

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return {"error": "Task not found"}

    # Update agent status
    for a in agents:
        if a["id"] == agent_id:
            a["status"] = "busy"
            a["currentTask"] = task_id
            break

    # Update task
    for t in tasks:
        if t["id"] == task_id:
            t["agent"] = agent_id
            t["status"] = "in-progress"
            t["updated"] = datetime.now().isoformat()
            break

    save_agents(agents)
    save_tasks(tasks)

    return {"success": True, "agent": agent_id, "task": task_id}


def get_stats():
    """Calculate dashboard statistics."""
    tasks = get_tasks()
    agents = get_agents()

    total_tasks = len(tasks)
    backlog = len([t for t in tasks if t["status"] == "backlog"])
    in_progress = len([t for t in tasks if t["status"] == "in-progress"])
    done = len([t for t in tasks if t["status"] == "done"])

    active_agents = len([a for a in agents if a["status"] == "busy"])
    idle_agents = len([a for a in agents if a["status"] == "idle"])

    completion_rate = round((done / total_tasks * 100) if total_tasks > 0 else 0, 1)

    return {
        "totalTasks": total_tasks,
        "backlog": backlog,
        "inProgress": in_progress,
        "done": done,
        "activeAgents": active_agents,
        "idleAgents": idle_agents,
        "totalAgents": len(agents),
        "completionRate": completion_rate
    }


class AgentTaskHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler for agent task management API."""

    def do_GET(self):
        """Handle GET requests."""
        parsed = urlparse(self.path)
        path = parsed.path

        # Serve dashboard
        if path == "/" or path == "/agent_dashboard.html":
            if DASHBOARD_PATH.exists():
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                with open(DASHBOARD_PATH, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "Dashboard not found")
            return

        # API: Get all tasks
        if path == "/api/tasks":
            tasks = get_tasks()
            self.send_json_response(tasks)
            return

        # API: Get single task
        if path.startswith("/api/tasks/") and len(path.split("/")) == 4:
            task_id = path.split("/")[3]
            tasks = get_tasks()
            task = next((t for t in tasks if t["id"] == task_id), None)
            if task:
                self.send_json_response(task)
            else:
                self.send_error(404, "Task not found")
            return

        # API: Get all agents
        if path == "/api/agents":
            agents = get_agents()
            self.send_json_response(agents)
            return

        # API: Get stats
        if path == "/api/stats":
            stats = get_stats()
            self.send_json_response(stats)
            return

        self.send_error(404, "Endpoint not found")

    def do_POST(self):
        """Handle POST requests."""
        parsed = urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else "{}"

        try:
            data = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
            return

        # API: Create task
        if path == "/api/tasks":
            task = create_task(data)
            self.send_json_response(task, status=201)
            return

        # API: Dispatch task to agent
        if path.startswith("/api/agents/") and path.endswith("/dispatch"):
            agent_id = path.split("/")[3]
            task_id = data.get("taskId")
            if not task_id:
                self.send_error(400, "taskId required")
                return
            result = dispatch_task_to_agent(agent_id, task_id)
            if "error" in result:
                self.send_error(404, result["error"])
            else:
                self.send_json_response(result)
            return

        self.send_error(404, "Endpoint not found")

    def do_PUT(self):
        """Handle PUT requests."""
        parsed = urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else "{}"

        try:
            data = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
            return

        # API: Update task
        if path.startswith("/api/tasks/") and len(path.split("/")) == 4:
            task_id = path.split("/")[3]
            task = update_task(task_id, data)
            if task:
                self.send_json_response(task)
            else:
                self.send_error(404, "Task not found")
            return

        self.send_error(404, "Endpoint not found")

    def do_DELETE(self):
        """Handle DELETE requests."""
        parsed = urlparse(self.path)
        path = parsed.path

        # API: Delete task
        if path.startswith("/api/tasks/") and len(path.split("/")) == 4:
            task_id = path.split("/")[3]
            delete_task(task_id)
            self.send_json_response({"success": True, "id": task_id})
            return

        self.send_error(404, "Endpoint not found")

    def send_json_response(self, data, status=200):
        """Send JSON response."""
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

    def do_OPTIONS(self):
        """Handle OPTIONS for CORS."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        """Custom log format."""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {format % args}")


class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    """Handle requests in separate threads."""
    daemon_threads = True


def main():
    """Start the agent task management server."""
    print("=" * 70)
    print("🤖 AGENT TASK MANAGEMENT SERVER")
    print("=" * 70)
    print(f"Dashboard: http://localhost:{PORT}")
    print()

    stats = get_stats()
    print(f"📊 Current Status:")
    print(f"   Tasks: {stats['totalTasks']} total")
    print(f"   Agents: {stats['totalAgents']} ({stats['activeAgents']} active, {stats['idleAgents']} idle)")
    print(f"   Completion: {stats['completionRate']}%")
    print()
    print("=" * 70)
    print(f"✅ Server running - Open http://localhost:{PORT} in your browser")
    print("   Press Ctrl+C to stop")
    print("=" * 70)

    try:
        with ThreadedHTTPServer(("", PORT), AgentTaskHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped")
    except Exception as e:
        print(f"\n❌ Server error: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()

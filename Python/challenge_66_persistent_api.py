"""
Challenge 66: Combined Challenge - API with Persistence

Problem Statement:
Create a FastAPI application that manages a simple to-do list.
The list should be saved to and loaded from a JSON file (`tasks.json`)
so that data persists across server restarts.

The API needs two endpoints:
1. `GET /tasks`: Returns the current list of all tasks.
2. `POST /tasks`: Adds a new task to the list and saves it.

Recommended Concepts:
- `FastAPI` to build the web server and endpoints.
- `json` module to serialize/deserialize data to/from a file.
- `pathlib` to handle the file path.
- `pydantic` (used by FastAPI) to define the data model for a task.

How to Run:
1. Make sure you have the necessary libraries: `pip install "fastapi[all]"`
2. Save this code as `persistent_api.py`.
3. Run the server: `uvicorn persistent_api:app --reload`
4. Use a tool like your browser, curl, or Postman to interact with the endpoints.
   - `GET http://127.0.0.1:8000/tasks`
   - `POST http://127.0.0.1:8000/tasks` with a JSON body like `{"name": "Buy milk"}`
"""
import json
from pathlib import Path
from typing import List

from fastapi import FastAPI, Request
from pydantic import BaseModel

# --- Configuration ---
app = FastAPI()
DB_FILE = Path("tasks.json")

# --- Pydantic Model ---
# This defines the structure of a "Task" item.
class Task(BaseModel):
    name: str
    completed: bool = False

# --- Helper Functions ---
def load_db() -> List[Task]:
    """Loads the task list from the JSON file."""
    if not DB_FILE.exists():
        return []
    with open(DB_FILE, 'r') as f:
        # Pydantic can parse the list of dicts into a list of Task objects
        raw_data = json.load(f)
        return [Task(**data) for data in raw_data]

def save_db(tasks: List[Task]):
    """Saves the entire task list to the JSON file."""
    # Convert list of Pydantic models back to a list of dicts for JSON
    list_of_dicts = [task.dict() for task in tasks]
    with open(DB_FILE, 'w') as f:
        json.dump(list_of_dicts, f, indent=4)

# --- API Endpoints ---
@app.get("/tasks", response_model=List[Task])
def get_all_tasks():
    """Returns the list of all tasks from the database file."""
    return load_db()

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    """Adds a new task to the database file."""
    db = load_db()
    db.append(task)
    save_db(db)
    return task

"""
Example Interaction:

1. First, run the server.
2. Send a POST request to http://127.0.0.1:8000/tasks with the body:
   { "name": "Learn FastAPI" }
   The server will respond with the created task and save it to `tasks.json`.

3. Send another POST request:
   { "name": "Build a cool app" }

4. Now, send a GET request to http://127.0.0.1:8000/tasks.
   The server will respond with a JSON array containing both tasks:
   [
       { "name": "Learn FastAPI", "completed": false },
       { "name": "Build a cool app", "completed": false }
   ]
""" 
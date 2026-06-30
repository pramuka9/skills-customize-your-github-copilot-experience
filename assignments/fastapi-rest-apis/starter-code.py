"""
Starter code for Building REST APIs with FastAPI
Complete the tasks in the assignment README.md to build a functional to-do API.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI app
app = FastAPI()

# Define the Todo data model
class Todo(BaseModel):
    id: Optional[int] = None
    title: str
    description: str = ""
    completed: bool = False

# In-memory storage for todos
todos: List[Todo] = []
next_id = 1

# ============================================
# Task 1: Basic Endpoints
# ============================================
# TODO: Implement the root "/" endpoint
# TODO: Implement the "/health" endpoint

# ============================================
# Task 2: CRUD Endpoints
# ============================================
# TODO: Implement GET /todos endpoint
# TODO: Implement POST /todos endpoint
# TODO: Implement GET /todos/{todo_id} endpoint
# TODO: Implement PUT /todos/{todo_id} endpoint
# TODO: Implement DELETE /todos/{todo_id} endpoint

# ============================================
# Task 3: Query Parameters and Filtering
# ============================================
# TODO: Add query parameters to GET /todos for filtering and pagination

# ============================================
# Helper Functions (Optional)
# ============================================
def find_todo(todo_id: int) -> Todo:
    """Find a todo by ID, raise HTTPException if not found."""
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

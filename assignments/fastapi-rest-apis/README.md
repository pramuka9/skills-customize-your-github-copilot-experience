# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern web APIs using the FastAPI framework. You will create a functional REST API with endpoints for reading and managing data, understanding HTTP methods, request/response handling, and API best practices.

## 📝 Tasks

### 🛠️ Task 1: Create a Basic FastAPI Server

#### Description
Set up a FastAPI application with a basic server that responds to GET requests. This task focuses on understanding the fundamentals of FastAPI and how to define simple endpoints.

#### Requirements
Completed program should:

- Import FastAPI and initialize an app instance
- Define a root endpoint (`/`) that returns a welcome message
- Define a `/health` endpoint that returns a status message confirming the server is running
- Include a docstring explaining the purpose of each endpoint
- Be runnable with `uvicorn main:app --reload`

### 🛠️ Task 2: Create CRUD Endpoints for a To-Do List

#### Description
Build a complete REST API for managing a to-do list with endpoints that support Create, Read, Update, and Delete (CRUD) operations. Data will be stored in memory using a Python list for simplicity.

#### Requirements
Completed program should:

- Define a data model using Pydantic (e.g., `Todo` class with `id`, `title`, `description`, and `completed` fields)
- Implement a GET `/todos` endpoint that returns all to-dos
- Implement a POST `/todos` endpoint that accepts a new to-do and returns the created item
- Implement a GET `/todos/{id}` endpoint that returns a specific to-do by ID
- Implement a PUT `/todos/{id}` endpoint that updates an existing to-do
- Implement a DELETE `/todos/{id}` endpoint that removes a to-do
- Use appropriate HTTP status codes (200, 201, 404, etc.)
- Include proper error handling for invalid IDs or missing data

### 🛠️ Task 3: Add Query Parameters and Filtering

#### Description
Enhance the API by adding query parameters to enable filtering and searching functionality. This demonstrates how to handle optional request parameters.

#### Requirements
Completed program should:

- Add a `completed` query parameter to the GET `/todos` endpoint to filter by completion status
- Add a `skip` and `limit` query parameter for pagination (e.g., `/todos?skip=0&limit=10`)
- Maintain backward compatibility (requests without parameters should still work)
- Return filtered results in a consistent format
- Include validation for query parameter values (e.g., skip/limit must be non-negative integers)

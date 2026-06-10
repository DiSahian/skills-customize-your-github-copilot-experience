# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework. Students will define API endpoints, model request and response data, and test API behavior with example JSON data.

## 📝 Tasks

### 🛠️ FastAPI Project Setup

#### Description
Create a FastAPI application with endpoints for a simple task tracker.

#### Requirements
Completed project should:

- Include `fastapi` and `uvicorn` in any setup instructions.
- Define a FastAPI app in a file named `main.py`.
- Use path operations for HTTP GET, POST, PUT, and DELETE.

### 🛠️ Define Data Models and Storage

#### Description
Use Pydantic models to define the structure of tasks and store tasks in an in-memory list.

#### Requirements
Completed project should:

- Define a `Task` model with `id`, `title`, `description`, and `completed` fields.
- Define a `TaskCreate` model for task creation requests.
- Store tasks in an in-memory list and manage unique IDs.
- Return the correct task data for each API operation.

### 🛠️ Implement CRUD Endpoints

#### Description
Implement endpoints to create, read, update, and delete tasks.

#### Requirements
Completed project should:

- Provide `GET /tasks` to return all tasks.
- Provide `GET /tasks/{task_id}` to return a single task or a 404 error if not found.
- Provide `POST /tasks` to create a task from a `TaskCreate` payload.
- Provide `PUT /tasks/{task_id}` to update a task.
- Provide `DELETE /tasks/{task_id}` to remove a task.
- Use appropriate response models and HTTP status codes.

### 🛠️ Test the API Endpoints

#### Description
Verify the API behavior using example requests and the built-in OpenAPI docs.

#### Requirements
Completed project should:

- Include example request bodies for task creation and updates.
- Confirm that API routes are available in the Swagger UI at `/docs`.
- Explain how to run the app with `uvicorn main:app --reload`.

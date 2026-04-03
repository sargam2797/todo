## Requirement analysis

**Original requirement**: "build a simple todo API using FastAPI"

### Requirement summary

- **Goal**: Provide a small HTTP JSON API for managing todo items, implemented with FastAPI.
- **Scope**: CRUD operations on todos, in-memory storage (or simple persistence), basic validation, and minimal but clear structure for future expansion.
- **Non-goals**: Full authentication/authorization, complex multi-user tenancy, advanced querying/filtering, production-grade observability, or deployment automation.

### Functional requirements

- **Create todo**: Client can create a todo with at least a `title` and optional `description` and `completed` flag.
- **Read todos**: Client can list all todos and fetch a single todo by ID.
- **Update todo**: Client can update fields of an existing todo.
- **Delete todo**: Client can delete an existing todo.
- **Validation & errors**: Invalid input or missing resources return appropriate HTTP status codes and error payloads.

### Non-functional requirements / constraints

- **Framework**: FastAPI with Pydantic models.
- **Runtime**: Python, single-process app suitable for running with Uvicorn.
- **Simplicity**: Keep the codebase easy to understand for learning purposes; avoid unnecessary abstractions.

### Architecture overview

- **Entry point / app setup**
  - A `main.py` (or similar) FastAPI application instance.
  - Include a health endpoint (e.g., `GET /health`) for quick checks.

- **Todo domain**
  - **Models**: Pydantic schemas for request/response (`TodoCreate`, `TodoUpdate`, `TodoRead`).
  - **Storage**: In-memory list/dict for todos keyed by ID (with a simple ID generator), with a clean interface so it could later be swapped for a database.
  - **Routes**: A router under `/todos` exposing CRUD endpoints.

- **Error handling**
  - Use HTTPException for 404 when a todo is not found.
  - Rely on FastAPI’s built-in validation for request bodies, with minimal custom error responses where needed.

- **Data flow (high-level)**
  1. HTTP request hits FastAPI route.
  2. Request body validated against Pydantic schema.
  3. Route handler calls storage/service functions to manipulate todo data.
  4. Result mapped back to response schema and returned as JSON with appropriate status code.

### Task breakdown checklist

- [x] **Task 1: Initialize FastAPI app structure**
  - **Description**: Create the FastAPI app instance and a basic `main.py` entrypoint with a root or health endpoint.
  - **Acceptance criteria**:
    - Running the app exposes `GET /health` (or `/`) returning a simple JSON payload.
    - App can be started with Uvicorn without import/runtime errors.

- [x] **Task 2: Define todo models and in-memory storage**
  - **Description**: Define Pydantic models for creating/updating/reading todos and implement a simple in-memory storage mechanism with unique IDs.
  - **Acceptance criteria**:
    - `TodoCreate`, `TodoUpdate`, and `TodoRead` (or equivalent) models exist with appropriate fields and validation.
    - An in-memory store can create, retrieve, update, delete todos, and list all todos.
    - Storage functions are unit-testable without needing FastAPI.

- [x] **Task 3: Implement CRUD routes for `/todos`**
  - **Description**: Add FastAPI routes for creating, listing, retrieving, updating, and deleting todos using the storage layer.
  - **Acceptance criteria**:
    - `POST /todos` creates a todo and returns it with a generated ID and correct HTTP status.
    - `GET /todos` returns a list of todos.
    - `GET /todos/{id}` returns the todo when it exists and 404 when it does not.
    - `PUT`/`PATCH /todos/{id}` updates the todo and returns the updated representation.
    - `DELETE /todos/{id}` deletes the todo and returns an appropriate status (e.g., 204).

- [x] **Task 4: Basic error handling and validation polish**
  - **Description**: Ensure that invalid payloads and missing resources are handled consistently and clearly.
  - **Acceptance criteria**:
    - Invalid request bodies are rejected with 422 from FastAPI (default) or a clear error structure.
    - 404 errors for non-existent todos are consistently returned using `HTTPException`.
    - Responses use the defined Pydantic models.

- [x] **Task 5: Minimal documentation and usage instructions**
  - **Description**: Document how to run the server and try the API.
  - **Acceptance criteria**:
    - Brief instructions (e.g., in `README.md` or comments in `main.py`) on starting the app with Uvicorn.
    - Mention of interactive docs available at `/docs` and `/redoc`.

### Progress

- **Stage**: `review`
- **Current task index**: `4` (0-based; Task 5 implemented; awaiting review)
- **Notes**:
  - Added root `README.md` with run instructions and example requests.

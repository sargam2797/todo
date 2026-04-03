## Evaluated outcomes

### Technology and framework choices

- **Language**: Python
- **Web framework**: FastAPI
  - Chosen for its async support, automatic OpenAPI generation, and strong Pydantic integration, which are ideal for a small educational todo API.
- **Data storage**: In-memory store (Python list/dict)
  - Chosen for simplicity; avoids database setup while keeping the design swappable for a real database later.
- **Server**: Uvicorn ASGI server
  - Commonly used with FastAPI; good developer experience and widely documented.

### Design patterns and structure

- **Layered structure (lightweight)**
  - **API layer**: FastAPI routes (path operations) focused on HTTP concerns (status codes, request/response).
  - **Domain/storage layer**: Plain Python functions or a small class to encapsulate todo operations (create/read/update/delete).
  - This separation keeps the todo logic reusable and testable without FastAPI.

- **Data modeling**
  - Use Pydantic models for:
    - **Input**: `TodoCreate` and `TodoUpdate` (validation, optional fields).
    - **Output**: `TodoRead` including the generated ID.
  - This aligns with FastAPI best practices and makes the API self-documented via OpenAPI.

- **Error handling pattern**
  - Raise `HTTPException(status_code=404, detail="Todo not found")` for missing resources.
  - Rely on FastAPI’s default 422 handling for validation errors.

### Decision log

- **[2026-04-03] Use in-memory storage initially**
  - **Decision**: Implement a simple in-memory store for todos with integer IDs.
  - **Rationale**: Keeps the project lightweight and focused on FastAPI basics; avoids DB configuration overhead.
  - **Consequences**:
    - Data is not persisted across restarts.
    - Easy to replace with a real database layer in the future.

- **[2026-04-03] Separate storage logic from routes**
  - **Decision**: Keep a thin API layer and move core todo operations into separate functions/module.
  - **Rationale**: Encourages clean design and easier unit testing.
  - **Consequences**:
    - Slightly more structure up front.
    - Simplifies future refactors (e.g., swapping storage backend).

- **[2026-04-03] Keep API surface minimal**
  - **Decision**: Implement only essential CRUD operations and a health check endpoint.
  - **Rationale**: Aligns with the “simple todo API” requirement and keeps focus clear.
  - **Consequences**:
    - Faster to understand and extend.
    - Advanced features (auth, filtering, pagination) are explicitly out of scope for now.


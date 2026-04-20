# Requirement Analysis: Todo Search Endpoint

## Requirement Summary

Original requirement:
> "Implement a Search endpoint for todos"

### Goals
- Add an API endpoint that lets clients search todos by query text.
- Keep behavior consistent with existing FastAPI routing and response models.
- Ensure search is deterministic and easy to test.

### Constraints
- Follow existing project architecture (FastAPI router + in-memory `TodoStore`).
- Keep implementation minimal and learning-friendly.
- Do not break existing CRUD behavior.

### Non-Goals
- Full-text indexing or fuzzy ranking.
- Persistent database-backed search.
- Advanced filtering (date ranges, tags, pagination) unless explicitly requested later.

### Acceptance Criteria
- A new endpoint exists under the todo API for searching.
- Endpoint accepts a query parameter and returns matching todos.
- Matching behavior is defined (case-insensitive substring over title/description).
- Invalid/empty query handling is defined and validated.
- Basic tests cover successful and edge-case search behavior.

## Architecture Overview

### High-level components
- `todo_routes.py`: add search route and request validation.
- `todo_storage.py`: add search method that performs in-memory filtering.
- `todo_models.py` (optional): only if a dedicated response/request model becomes necessary.
- Tests module (to be added/updated): verifies endpoint behavior.

### Data flow
1. Client calls `GET /todos/search?q=<term>`.
2. Route validates the query and delegates to store search logic.
3. Store scans existing todos in memory and filters by normalized text match.
4. Route returns `List[TodoRead]` results in stable insertion order.

## Task Breakdown Checklist

- [ ] Task 1: Define search contract and route surface in API layer.
  - Acceptance criteria:
    - Route path and HTTP method are finalized and documented in code.
    - Query parameter validation rules are explicit (e.g., min length / non-blank).
    - Response schema is `List[TodoRead]`.

- [ ] Task 2: Implement store-level search filtering.
  - Acceptance criteria:
    - `TodoStore` exposes a search method used by the route.
    - Search checks `title` and `description` (when present).
    - Matching is case-insensitive substring and returns deterministic order.

- [ ] Task 3: Add tests for search endpoint behavior.
  - Acceptance criteria:
    - Tests cover matching by title and description.
    - Tests cover no-match behavior (empty list).
    - Tests cover validation/edge handling for invalid query inputs.

- [ ] Task 4: Update docs/examples for the new endpoint.
  - Acceptance criteria:
    - `README.md` includes an example request for search.
    - Endpoint usage and expected response are clear.

## Progress

- Stage: `review`
- Current task index: `0`
- Notes:
  - Planning created for new project workflow `todo-search-endpoint`.
  - Planning approved via `/devorch approve`.
  - Task 1 implementation started: added `GET /todos/search` endpoint contract with `q` query validation.
  - Task 1 is now awaiting human review via `/devorch approve`.

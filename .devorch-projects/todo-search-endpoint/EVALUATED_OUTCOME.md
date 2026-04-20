# Evaluated Outcome: Todo Search Endpoint

## Initial Evaluated Outcomes

- Framework/runtime: Keep FastAPI + existing in-memory Python store.
- API style: Add a dedicated read endpoint for search under `/todos`.
- Search semantics: Case-insensitive substring match over `title` and `description`.
- Error handling: Use FastAPI validation for query parameter constraints.

## Design Patterns To Use

- **Thin route, focused store logic**: route validates input and delegates filtering to storage layer.
- **Single source response model**: reuse `TodoRead` for consistency across read endpoints.
- **Incremental delivery**: implement one verifiable task at a time with review checkpoints.

## Decision Log

Use this format for ongoing decisions:

| Date | Decision | Rationale | Consequence |
| --- | --- | --- | --- |
| 2026-04-20 | Use in-memory linear scan for search | Current app is non-persistent and small-scale learning API | Search is simple and predictable; performance optimization deferred |
| 2026-04-20 | Keep search under todo router | Maintains discoverability and cohesive API structure | Route logic remains in `todo_routes.py` |

# Open Questions: Todo Search Endpoint

## Questions

1. Should an empty query string return validation error (`422`) or all todos?
   - Status: open

2. Should search include only `title` and `description`, or also support filtering by `completed`?
   - Status: open

3. Preferred endpoint shape: `GET /todos/search?q=...` or `GET /todos?search=...`?
   - Status: open

## Notes

- If these remain unanswered, implementation will use conservative defaults:
  - dedicated route `GET /todos/search`
  - required non-blank `q` query
  - search only in `title` and `description`

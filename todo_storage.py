from __future__ import annotations

from typing import Dict, List

from todo_models import TodoCreate, TodoRead, TodoUpdate


class TodoStore:
    """
    Simple in-memory storage.

    Note: this is intentionally non-persistent for a minimal learning-friendly API.
    """

    def __init__(self) -> None:
        self._todos: Dict[int, TodoRead] = {}
        self._next_id: int = 1

    def list(self) -> List[TodoRead]:
        # Preserve insertion order (Python dict preserves order).
        return list(self._todos.values())

    def get(self, todo_id: int) -> TodoRead:
        try:
            return self._todos[todo_id]
        except KeyError as e:
            raise KeyError(f"Todo {todo_id} not found") from e

    def create(self, payload: TodoCreate) -> TodoRead:
        todo_id = self._next_id
        self._next_id += 1

        todo = TodoRead(
            id=todo_id,
            title=payload.title,
            description=payload.description,
            completed=payload.completed,
        )
        self._todos[todo_id] = todo
        return todo

    def update(self, todo_id: int, payload: TodoUpdate) -> TodoRead:
        existing = self.get(todo_id)

        # With Pydantic models, exclude_unset ensures only provided fields are changed.
        updates = payload.model_dump(exclude_unset=True)
        data = existing.model_dump()
        data.update(updates)

        updated = TodoRead(**data)
        self._todos[todo_id] = updated
        return updated

    def delete(self, todo_id: int) -> bool:
        # Returns True if something was deleted, False if the id didn't exist.
        return self._todos.pop(todo_id, None) is not None


# Default singleton store instance for the app.
store = TodoStore()


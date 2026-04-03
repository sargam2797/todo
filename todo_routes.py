from typing import List

from fastapi import APIRouter, HTTPException, status

from todo_models import TodoCreate, TodoRead, TodoUpdate
from todo_storage import store


router = APIRouter(prefix="/todos", tags=["todos"])


def _require_at_least_one_update(payload: TodoUpdate) -> None:
    # For PATCH/PUT we allow partial updates, but at least one field must be provided.
    if not payload.model_dump(exclude_unset=True):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="At least one field must be provided for update",
        )


@router.post(
    "",
    response_model=TodoRead,
    status_code=status.HTTP_201_CREATED,
)
def create_todo(payload: TodoCreate) -> TodoRead:
    return store.create(payload)


@router.get(
    "",
    response_model=List[TodoRead],
)
def list_todos() -> List[TodoRead]:
    return store.list()


@router.get(
    "/{todo_id}",
    response_model=TodoRead,
)
def get_todo(todo_id: int) -> TodoRead:
    try:
        return store.get(todo_id)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@router.put(
    "/{todo_id}",
    response_model=TodoRead,
)
def update_todo(todo_id: int, payload: TodoUpdate) -> TodoRead:
    _require_at_least_one_update(payload)
    try:
        return store.update(todo_id, payload)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@router.patch(
    "/{todo_id}",
    response_model=TodoRead,
)
def patch_todo(todo_id: int, payload: TodoUpdate) -> TodoRead:
    _require_at_least_one_update(payload)
    try:
        return store.update(todo_id, payload)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@router.delete(
    "/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_todo(todo_id: int) -> None:
    deleted = store.delete(todo_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


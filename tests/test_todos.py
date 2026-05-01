from fastapi.testclient import TestClient

from main import app
from todo_models import TodoCreate, TodoUpdate
from todo_storage import store
from todo_storage import TodoStore


client = TestClient(app)


def _reset_global_store() -> None:
    store._todos = {}
    store._next_id = 1


def test_todo_store_crud_flow() -> None:
    store = TodoStore()

    created = store.create(TodoCreate(title="Write tests"))
    assert created.id == 1
    assert created.title == "Write tests"
    assert created.completed is False

    listed = store.list()
    assert len(listed) == 1
    assert listed[0].id == created.id

    updated = store.update(created.id, TodoUpdate(completed=True))
    assert updated.completed is True
    assert store.get(created.id).completed is True

    deleted = store.delete(created.id)
    assert deleted is True
    assert store.list() == []


def test_search_no_results_should_404() -> None:
    _reset_global_store()
    response = client.get("/todos/search?q=nonexistent")

    assert response.status_code == 404
    assert response.json()["detail"] == "No todos match your search"


def test_search_response_envelope() -> None:
    _reset_global_store()
    create_response = client.post("/todos", json={"title": "Test task"})
    assert create_response.status_code == 201

    response = client.get("/todos/search?q=test")
    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) == 1


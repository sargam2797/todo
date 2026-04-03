# Todo API (FastAPI)

## About this repo

This repository contains a simple FastAPI-based Todo API for learning and iteration.  
It includes in-memory todo storage, CRUD endpoints, and basic validation/error handling.

## DevOrch integration

This repo is wired to a DevOrch workflow for step-by-step implementation with approval checkpoints.  
DevOrch behavior is defined in the skill files, so only the key folder layout is shown here.

### DevOrch folder structure

```text
.cursor/
  skills/
    devorch/
      SKILL.md
      README.md

.devorch-projects/
  todo-api-fastapi/
    REQUIREMENT_ANALYSIS.md
    EVALUATED_OUTCOME.md
    OPEN_QUESTIONS.md
    STATE.json
```

## Run the server

From the repo root:

```bash
source .venv/bin/activate
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Health check:

- `GET http://127.0.0.1:8000/health`

Interactive API docs:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Try the API

Create a todo:

```bash
curl -X POST "http://127.0.0.1:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false
  }'
```

List todos:

```bash
curl "http://127.0.0.1:8000/todos"
```


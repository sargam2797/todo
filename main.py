from fastapi import FastAPI

from todo_routes import router as todos_router


app = FastAPI(title="Todo API")

app.include_router(todos_router)


@app.get("/health")
def health() -> dict:
    # Simple liveness probe for verifying the service is up.
    return {"status": "ok"}


@app.get("/")
def root() -> dict:
    # Convenience endpoint; primary health check is `/health`.
    return {"message": "Todo API"}


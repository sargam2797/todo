from typing import Optional

from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    completed: bool = False


class TodoUpdate(BaseModel):
    # Optional fields enable partial updates (PATCH semantics).
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool


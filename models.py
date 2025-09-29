# Pydantic-модели (схемы запросов/ответов)

from pydantic import BaseModel
from typing import Optional

class CreateNote(BaseModel):
    user_id: int
    note: str
    deadline: str

class UpdateNote(BaseModel):
    note_id: int
    note: Optional[str] = None
    deadline: Optional[str] = None
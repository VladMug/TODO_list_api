# Pydantic-модели (схемы запросов/ответов)

from pydantic import BaseModel
from typing import Optional

class DataForCreateNote(BaseModel):
    user_id: int
    note: str

class DataForUpdateNote(BaseModel):
    note: Optional[str] = None
    status: Optional[str] = None
# Pydantic-models

from pydantic import BaseModel

class DataForCreateNote(BaseModel):
    user_id: int
    note: str

class DataForUpdateNote(BaseModel):
    note: str | None = None
    status: str | None = None
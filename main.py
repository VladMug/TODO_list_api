# Точка входа и запуск FastAPI

from fastapi import FastAPI, status
from starlette.responses import JSONResponse
from typing import Optional

from db import init_db
from handlers import create_note, get_notes, delete_note, update_note
from models import CreateNote, UpdateNote

init_db()

app = FastAPI()

# CREATE
@app.post('/notes/create/')
async def create_item(note: CreateNote):
    return create_note(note.user_id, note.note, note.deadline)

# READ
@app.get('/users/{user_id}/notes')
async def get_items(user_id: int):
    return get_notes(user_id)

# UPDATE
@app.put('/notes/update/')
async def update_item(note: UpdateNote):
    return update_note(note.note_id, note.note, note.deadline)

# DELETE
@app.delete('/notes/delete/{note_id}')
async def delete_item(note_id: int):
    success = delete_note(note_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK if success else status.HTTP_404_NOT_FOUND,
        content={"success": success}
    )

if __name__ == '__main__':
    print(1)
    # print(create_note(123, 'fortnit', '19-09-2025'))
    # for i in get_notes(123): print(i)
    # print(update_note(30, 'boblox'))
    # print(delete_note(10))
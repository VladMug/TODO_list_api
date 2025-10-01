# Точка входа и запуск FastAPI

from fastapi import FastAPI, status
from starlette.responses import JSONResponse

from db import init_db
from handlers import create_note, get_notes, delete_note, update_note
from models import DataForCreateNote, DataForUpdateNote

init_db()

app = FastAPI()

# CREATE
@app.post('/notes')
async def create_item(note: DataForCreateNote):
    result = create_note(note.user_id, note.note)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=result
    )

# READ
@app.get('/users/{user_id}/notes')
async def get_items(user_id: int):
    return get_notes(user_id)

# UPDATE
@app.patch('/notes/{note_id}')
async def update_item(note_id: int, note: DataForUpdateNote):
    result = update_note(note_id, note.note, note.deadline)
    success = False
    if result:
        success = True
    return JSONResponse(
        status_code=status.HTTP_200_OK if success else status.HTTP_404_NOT_FOUND,
        content=result
    )

# DELETE
@app.delete('/notes/{note_id}')
async def delete_item(note_id: int):
    success = delete_note(note_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK if success else status.HTTP_404_NOT_FOUND,
        content={"success": success}
    )

if __name__ == '__main__':
    print(1)
    # print(create_note(123, 'aboba'))
    # for i in get_notes(123): print(i)
    # print(update_note(3, status='in sosi'))
    # print(delete_note(10))
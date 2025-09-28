# Точка входа и запуск FastAPI

from db import init_db
from handlers import create_note, get_notes, delete_note, update_note
from fastapi import FastAPI, status
from starlette.responses import JSONResponse

init_db()

app = FastAPI()
@app.get('/')
async def root():
    return {'message': 'Hello, world!'}
# print(create_note(123, 'fortnit', '19-09-2025'))

# for i in get_notes(123): print(i)
@app.get('/users/{user_id}/notes')
async def get_items(user_id: int):
    return get_notes(user_id)

# print(update_note(30, 'boblox'))
# @app.put('')

# print(delete_note(10))
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
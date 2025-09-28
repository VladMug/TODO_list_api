# Логика работы с БД (CRUD-операции)

from db import get_connection
from encoder import decode_note, encode_note

from config.config import NOTE_KEYS

# CREATE
def get_note_by_id(note_id: int) -> dict | None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM notes WHERE note_id = ?', (note_id,)
        )
        note = cursor.fetchone()
        if note is not None:
            note = format_note(note)
            return note
        else:
            return None

def insert_row(data: dict) -> int | None: 
    if not data:
        raise ValueError('No data to insert')
    if not all(c in NOTE_KEYS.values() for c in data.keys()):
        raise ValueError('Invalid column name')
    cols = ', '.join(data.keys())
    placeholders = ', '.join('?' for _ in data)
    values = data.values()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            f'INSERT INTO notes ({cols}) VALUES ({placeholders})', tuple(values)
        )
        conn.commit()
        return cursor.lastrowid

def create_note(user_id:int, note:str, deadline:str) -> dict:
    encoded_note = encode_note(note)
    data = {
        'user_id': user_id,
        'note': encoded_note,
        'deadline': deadline
    }
    note_id = insert_row(data)
    return get_note_by_id(note_id)

# READ
# Преобразует tuple в dict и расшифровывает в нем текст заметки
def format_note(note: tuple) -> dict: 
    note_dict = dict(zip(NOTE_KEYS.values(), note))
    note_dict['note'] = decode_note(note_dict['note'])
    return note_dict

def get_notes(user_id:int) -> list[dict] | None: 
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM notes WHERE user_id = ?' , (user_id,)
        )
        notes_data = cursor.fetchall() 
        if notes_data:
            return [format_note(note) for note in notes_data]
        else:
            return []

# UPDATE
def update_row(note_id, data) -> int:
    if not data:
        raise ValueError('No data to update')
    if not all(c in NOTE_KEYS.values() for c in data.keys()):
        raise ValueError('Invalid column name')
    cols = list(data.keys())
    values = list(data.values()) + [note_id]
    placeholders = ', '.join(f'{col} = ?' for col in cols)
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE notes SET {placeholders} WHERE note_id = ?', tuple(values))
        conn.commit()
        return cursor.rowcount

def update_note(note_id: int, note: str = None, deadline: str = None) -> dict | None:
    if note is None and deadline is None:
        raise ValueError('No arguments for update')
    data = {}
    if note is not None:
        data['note'] = encode_note(note)
    if deadline is not None: 
        data['deadline'] = deadline
    updated = update_row(note_id, data)
    if updated == 1:
        return get_note_by_id(note_id)
    return None
        
# DELETE
def delete_note(note_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'DELETE FROM notes WHERE note_id = ?', (note_id,)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
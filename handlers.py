# Логика работы с БД (CRUD-операции)

from db import get_connection
from encoder import decode_note, encode_note

from config.config import NOTE_KEYS, STATUSES_NAME

# CREATE
def insert_row(data: dict, db_path: str | None = None) -> int | None: 
    if not data:
        raise ValueError('No data to insert')
    if not all(c in NOTE_KEYS.values() for c in data.keys()):
        raise ValueError('Invalid column name')

    cols = ', '.join(data.keys())
    placeholders = ', '.join('?' for _ in data)
    values = data.values()

    with get_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f'INSERT INTO notes ({cols}) VALUES ({placeholders})', tuple(values)
        )
        conn.commit()
        return cursor.lastrowid

def create_note(user_id:int, note:str, db_path: str | None = None) -> dict:
    encoded_note = encode_note(note)
    data = {
        'user_id': user_id,
        'note': encoded_note,
    }
    note_id = insert_row(data, db_path)
    return get_notes(note_id=note_id)

# READ
# Converts a tuple to a dict and decrypts the note text into it
def format_note(note: tuple) -> dict: 
    note_dict = dict(zip(NOTE_KEYS.values(), note))
    note_dict['note'] = decode_note(note_dict['note'])
    return note_dict
        
def get_notes(note_id: int | None = None, user_id: int | None = None, status: str | None = None, db_path: str | None = None) -> list[dict]:
    values = []
    cols = []

    if note_id is not None:
        values.append(note_id)
        cols.append('note_id')
    if user_id is not None:
        values.append(user_id)
        cols.append('user_id')
    if status is not None:
        values.append(status)
        cols.append('status')

    sql = 'SELECT * FROM notes'
    if cols:
        placeholder = ' AND '.join(f'{col} = ?' for col in cols)
        sql += f' WHERE {placeholder}'

    with get_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, tuple(values))
        return [format_note(note) for note in cursor.fetchall()]


# UPDATE
def update_row(note_id: int, data: dict, db_path: str | None = None) -> int:
    if not data:
        raise ValueError('No data to update')
    if not all(c in NOTE_KEYS.values() for c in data.keys()):
        raise ValueError('Invalid column name')

    cols = list(data.keys())
    values = list(data.values()) + [note_id]
    placeholders = ', '.join(f'{col} = ?' for col in cols)

    with get_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE notes SET {placeholders} WHERE note_id = ?', tuple(values))
        conn.commit()
        return cursor.rowcount

def update_note(note_id: int, note: str | None = None, status: str | None = None, db_path: str | None = None) -> dict | None:
    if note is None and status is None:
        raise ValueError('No arguments for update')

    data = {}
    if note is not None:
        data['note'] = encode_note(note)
    if status is not None: 
        if status in STATUSES_NAME.values():
            data['status'] = status
        else:
            raise ValueError('Invalid status name')

    updated = update_row(note_id, data, db_path)
    if updated == 1:
        return get_notes(note_id=note_id)
    return None
        
# DELETE
def delete_note(note_id: int, db_path: str | None = None) -> bool:
    with get_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'DELETE FROM notes WHERE note_id = ?', (note_id,)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return False
        else:
            return True
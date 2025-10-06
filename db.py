# Подключение и инициализация базы данных
import sqlite3
from config.config import DATABASE_PATH, STATUSES_NAME

def get_connection(db_path: str | None = None):
    return sqlite3.connect(db_path or DATABASE_PATH)

def init_db(db_path: str | None = None):
    with get_connection(db_path) as conn:
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS notes (
                note_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                note TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT '{STATUSES_NAME["not_started"]}'
            )
        """)
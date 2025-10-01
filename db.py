# Подключение и инициализация базы данных

# Структура ДБ (внутренний индификатор(например telegram user id), задача(зашифрованная), дата дедлайна)

import sqlite3

from config.config import DATABASE_PATH, STATUSES_NAME

def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS notes (
            note_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            note TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT '{STATUSES_NAME["not_started"]}'
        )'''
    )


    conn.commit()
    conn.close()
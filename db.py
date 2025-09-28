# Подключение и инициализация базы данных

# Структура ДБ (внутренний индификатор(например telegram user id), задача(зашифрованная), дата дедлайна)

import sqlite3

from config.config import DATABASE_PATH

def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            note_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            note TEXT NOT NULL,
            deadline TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
import sqlite3

DB_PATH = "my_database.db"

def init_db():
    """Создаёт таблицу, если её ещё нет"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE,
        translation TEXT,
        example TEXT,
        level TEXT,
        tags TEXT
    );
    """)
    conn.commit()
    conn.close()

def check_tables():
    """Проверяет наличие таблицы words"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return tables

# Запуск
init_db()
print("Таблицы в базе:", check_tables())

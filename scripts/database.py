import sqlite3

DB_PATH = "data/my_database.db"

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




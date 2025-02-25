import sqlite3
from scripts.config import CONFIG # импортируем наш конфиг


DB_PATH = CONFIG.get("database", "data/words.db")

def init_db():
    """Создаёт таблицу, если её ещё нет"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE,
        third_person TEXT,
        prataritum TEXT,
        partizip_II TEXT,
        example TEXT,
        translation TEXT,
        level TEXT,
        tags TEXT
    );
    """)
    conn.commit()
    conn.close()

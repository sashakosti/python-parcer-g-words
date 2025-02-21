import sqlite3

DB_PATH = "data/anki_words.db"

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

def add_word(word, translation, example, level, tags):
    """Добавляет слово в базу"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO words (word, translation, example, level, tags)
    VALUES (?, ?, ?, ?, ?)
    ON CONFLICT(word) DO UPDATE SET 
        translation=excluded.translation,
        example=excluded.example,
        level=excluded.level,
        tags=excluded.tags;
    """, (word, translation, example, level, tags))
    conn.commit()
    conn.close()



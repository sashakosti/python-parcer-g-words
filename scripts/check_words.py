import sqlite3
from config import CONFIG

DB_PATH = CONFIG.get("database", "data/words.db")

def word_exists(word):
    """Проверяет, есть ли слово в базе"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM words WHERE word = ?", (word,))
    result = cursor.fetchone()  # Получаем первую найденную строку
    conn.close()
    return result is not None  # True, если слово есть, False, если нет

def add_word(word, third_person, prataritum, partizip_II, example, translation, level, tags):
    """Добавляет слово в базу, если его нет"""
    if word_exists(word):
        print(f"⚠️ Слово '{word}' уже есть в базе.")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO words (word, third_person, prataritum, partizip_II, example, translation, level, tags) 
    VALUES (?, ?, ?, ?, ?)
    """, (word, third_person, prataritum, partizip_II, example, translation, level, tags))
    conn.commit()
    conn.close()
    print(f"✅ Добавлено слово '{word}'")

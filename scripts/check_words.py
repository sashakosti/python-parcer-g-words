import sqlite3

def add_word(word, translation, example, level, tags):
    conn = sqlite3.connect("anki_words.db")
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

# Пример добавления слова
add_word("laufen", "бегать", "Er läuft jeden Morgen.", "A1", "глагол,движение")
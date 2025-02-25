import sqlite3

def add_word(word, translation, example, level, tags):
    conn = sqlite3.connect("data/my_database.db")
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
    print(f"✅ Слово {word} успешно добавлено в базу данных!")
    
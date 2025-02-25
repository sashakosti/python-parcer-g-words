import sqlite3
import csv

DB_PATH = "data/my_database.db"

def export_to_anki(filename="data/export.csv"):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT word, translation, example, level, tags FROM words")
    words = cursor.fetchall()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")  # Anki требует табуляцию
        writer.writerow(["Word", "Translation", "Example", "Level", "Tags"])
        writer.writerows(words)

    conn.close()
    print(f"✅ Файл {filename} готов для импорта в Anki!")
    
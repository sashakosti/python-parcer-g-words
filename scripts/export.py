import sqlite3
import csv
from scripts.config import CONFIG

DB_PATH = CONFIG.get("database", "data/words.db")

def export_to_anki(filename=CONFIG.get("export_csv", "data/export.csv")):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT word, third_person, prataritum, partizip_II, example, translation, level, tags FROM words")
    words = cursor.fetchall()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")  # Anki требует табуляцию
        writer.writerow(["Word", "Er/Sie/Es", "Prataritum", "Partizip_II", "Example", "Translation", "Level", "Tags"])
        writer.writerows(words)

    conn.close()
    print(f"✅ Файл {filename} готов для импорта в Anki!")
    
import fitz  # pymupdf
import os
from config import CONFIG

pdf_path = CONFIG.get("pdf")  # Define your pdf path here

if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"Файл {pdf_path} не найден. Проверь путь.")

def extract_text_from_pdf(pdf_path): # Чтение текста из ПДФ
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def parse_words_from_text(text, fields=None):

    lines = text.split("\n")  # Разделяем текст на строки
    words = []

    field_indexes = {
        "infinitive": 0,
        "er/sie/es": 1,
        "prataritum": 2,
        "participle_II": 3,
        "translation": 4,
        "level": 5
    }

    # Если поля не заданы, берём всё
    if fields is None:
        fields = ["infinitive", "er/sie/es", "prataritum", "participle_II", "translation", "level"]

    selected_indexes = [field_indexes[field] for field in fields]

    for line in lines:
        parts = line.split("\t")  # Разделяем по " - "
        if len(parts) < len(field_indexes):
            print(f"Ошибка: в строке {line} не хватает данных! Разбилось на {len(parts)} частей.")
            continue
        selected_parts = [parts[i] for i in selected_indexes]
        words.append(tuple(selected_parts))

    return words

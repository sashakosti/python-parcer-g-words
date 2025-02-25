import fitz  # pymupdf
import os

pdf_path = "/Users/DonHuan/Programming learning/python_parcer/data/shit2parse/Tablitsa_nepravilnyh_glagolov_nemetskogo_jazyka.pdf"  # Define your pdf path here

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
        "past": 1,
        "participle": 2,
        "translation": 3,
        "level": 4
    }

    # Если поля не заданы, берём всё
    if fields is None:
        fields = ["infinitive", "past", "participle", "translation", "level"]

    selected_indexes = [field_indexes[field] for field in fields]

    for line in lines:
        parts = line.split(" - ")  # Разделяем по " - "
        if len(parts) < 5:
            continue  # Пропускаем, если данных не хватает

        selected_parts = [parts[i] for i in selected_indexes]
        words.append(tuple(selected_parts))

    return words

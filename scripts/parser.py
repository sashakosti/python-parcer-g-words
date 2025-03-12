import fitz
import re
from scripts.config import CONFIG 

IGNORE_PATTERNS = [
    "Таблица неправильных", "немецкого языка с переводом", "Copyright", "( /",
    "СЛОВАРНЫЙ ЗАПАС", "ГРАММАТИКА", "Infinitiv", "(основная", "форма глагола)", "форма глагола Er/sie/es", 
    "Präteritum", "(вторая форма", "глагола)", "Partizip II", "(третья форма", " глагола)", "Перевод",
    "Уровень", "Er/Sie/Es", "(форма 3 лица,", "(форма 3 лица", "ед. числа)", "183 неправильных глагола",
]

FIELD_INDEXES = {
    "infinitive": 0,
    "er_sie_es": 1,
    "prateritum": 2,
    "participle_II": 3,
    "translation": 4,
    "level": 5
}
pdf_path = CONFIG.get("pdf")

def extract_text_from_pdf(pdf_path):
    """Читает текст из PDF-файла."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def clean_text(lines):
    """Удаляет лишний мусор и пустые строки"""
    cleaned_lines = []
    
    for line in lines:
        line = re.sub(r'[,.\-()\s]+$', '', line)  # Убираем мусор в конце
        line = line.replace("ist/hat", "ist или hat")  # Нормализация ist/hat
        
        if line.strip() and not any(ignore in line for ignore in IGNORE_PATTERNS):
            cleaned_lines.append(line.strip())

    return cleaned_lines


def merge_parts(lines):
    """Объединяет разорванные строки, если они принадлежат одной записи."""
    merged_lines = []
    current_entry = []

    for line in lines:
        words = line.split()
        
        if len(words) <= 2:  # Если строка слишком короткая, приклеиваем к предыдущей
            if current_entry:
                last_word = current_entry[-1].split()[-1] if current_entry else ""
                first_word = words[0]

                if last_word in {"ist", "hat", "ist или hat"} or re.match(r'hat\s+-ge', last_word) or re.match(r'ist\s+\w+', last_word):
                    current_entry.append(line)  # Склеиваем с предыдущей
                else:
                    merged_lines.append(" ".join(current_entry))
                    current_entry = [line]
            else:
                current_entry = [line]
        else:
            if current_entry:
                merged_lines.append(" ".join(current_entry))
            current_entry = [line]

    if current_entry:
        merged_lines.append(" ".join(current_entry))  # Добавляем последний элемен

    return merged_lines

def parse_words_from_text(text, fields=None):
    """Парсит текст в список кортежей с указанными полями."""
    lines = text.split("\n")
    lines = clean_text(lines)
    lines = merge_parts(lines)

    if fields is None:
        fields = list(FIELD_INDEXES.keys())

    selected_indexes = [FIELD_INDEXES[field] for field in fields]

    words = []
    for line in lines:
        parts = re.split(r"\s+", line, maxsplit=5)
        
        if len(parts) < len(FIELD_INDEXES):
            print(f"Ошибка: в строке '{line}' не хватает данных! Разбилось на {len(parts)} частей.")
            continue

        selected_parts = [parts[i] for i in selected_indexes]
        words.append(tuple(selected_parts))

    return words

if __name__ == "__main__":
    extracted_text = extract_text_from_pdf(pdf_path)
    parsed_words = parse_words_from_text(extracted_text)
    
    print("\n=== Парсинг завершён! ===\n")
    for word in parsed_words[:10]:  # Выведем первые 10 строк для проверки
        print(word)

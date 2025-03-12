import fitz  # pymupdf
import os
import re
from scripts.config import CONFIG

pdf_path = CONFIG.get("pdf")

if not pdf_path:
    raise ValueError("Путь к PDF не задан в конфиге.")
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"Файл {pdf_path} не найден. Проверь путь.")

def extract_text_from_pdf(pdf_path): #Читает текст из PDF-файла.
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text


IGNORE_PATTERNS = [
    "Таблица неправильных", "немецкого языка с переводом", "Copyright",
    "СЛОВАРНЫЙ ЗАПАС", "ГРАММАТИКА", "Infinitiv", "Präteritum",
    "Partizip II", "Перевод", "Уровень"
]

def is_verb_form(word):
    """Проверяет, является ли слово отглагольной формой (Partizip II)."""
    return re.match(r"^(ge|be|ver|zer|emp|ent|er|miss|über|unter|wider|hinter)?[a-zäöüß]+t$", word)

def clean_text(lines):
    cleaned_lines = [line for line in lines if line.strip() and not any(ignore in line for ignore in IGNORE_PATTERNS)]

    merged_lines = []
    temp_line = ""  # Строка, которую нужно объединить с предыдущей

    for line in cleaned_lines:
        words = line.split()
        
        if temp_line and (
            len(words) == 1 or re.match(r"^[a-zA-Zäöüß]+$", line)
        ) and not is_verb_form(words[0]):  # Не объединяем, если слово — отглагольная форма
            temp_line += " " + line
        else:
            if temp_line:
                merged_lines.append(temp_line)
            temp_line = line

    if temp_line:
        merged_lines.append(temp_line)

    return [line.replace(", ", ",").replace(" ,", ",").strip() for line in merged_lines]


def parse_words_from_text(text, fields=None):
    """Парсит текст в список кортежей с указанными полями."""
    lines = text.split("\n")
    lines = clean_text(lines)
    words = []

    field_indexes = {
        "infinitive": 0,
        "er_sie_es": 1,
        "prateritum": 2,
        "participle_II": 3,
        "translation": 4,
        "level": 5
    }

    if fields is None:
        fields = list(field_indexes.keys())

    selected_indexes = [field_indexes[field] for field in fields]

    for line in lines:
        parts = re.split(r"\s+", line, maxsplit=5)
        print(parts)    
        #if len(parts) < len(field_indexes):
            #print(f"Ошибка: в строке {line} не хватает данных! Разбилось на {len(parts)} частей.")
            #continue
        #selected_parts = [parts[i] for i in selected_indexes]
        #words.append(tuple(selected_parts))

    return words

if __name__ == "__main__":
    extracted_text = extract_text_from_pdf(pdf_path)
    parsed_words = parse_words_from_text(extracted_text)
    print(parsed_words)
# После выполнения кода в консоль должно быть выведено что-то вроде: [('backen', 'bäckt', 'backte', 'geback')]
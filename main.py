from scripts.parser import extract_text_from_pdf, parse_words_from_text, clean_text, is_verb_form
from scripts.database import init_db
from scripts.export import export_to_anki
from scripts.check_words import add_word
from scripts.logger import log_info, log_warning, log_error
from scripts.config import CONFIG 

def main():
    init_db()  # Инициализация базы
    
    # Парсим PDF и добавляем слова в базу
    pdf_text = extract_text_from_pdf(CONFIG.get("pdf"))
    words = parse_words_from_text(pdf_text)  # ❗Здесь нужна твоя функция парсинга
    for word in words:
        print("DEBUG: word =", word)
        add_word(*word)
    # Экспортируем в Anki
    export_to_anki()

if __name__ == "__main__":
    main()

from scripts.parser import extract_text_from_pdf
from scripts.database import init_db, add_word
from scripts.export import export_to_anki

def main():
    init_db()  # Инициализация базы
    
    # Парсим PDF и добавляем слова в базу
    pdf_text = extract_text_from_pdf("data/input.pdf")
    words = parse_words_from_text(pdf_text)  # ❗Здесь нужна твоя функция парсинга
    for word in words:
        add_word(*word)

    # Экспортируем в Anki
    export_to_anki()

if __name__ == "__main__":
    main()

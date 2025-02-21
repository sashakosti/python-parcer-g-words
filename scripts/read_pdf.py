import fitz  # pymupdf

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    return text

if __name__ == "__main__":
    pdf_path = "/Users/DonHuan/Programming learning/python_parcer/shit2parse/Tablitsa_nepravilnyh_glagolov_nemetskogo_jazyka.pdf"  # Замени на свой путь
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)


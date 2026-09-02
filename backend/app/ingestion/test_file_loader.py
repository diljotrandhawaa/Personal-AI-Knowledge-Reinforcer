from app.ingestion.file_loader import load_txt_file, load_pdf_file

# txt_content = load_txt_file("backend/data/Apple_china.txt")

# print(txt_content)

pdf_content = load_pdf_file("backend/data/Neurogum.pdf")

print(pdf_content)
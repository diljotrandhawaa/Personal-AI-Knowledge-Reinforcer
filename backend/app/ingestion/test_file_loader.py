from backend.app.ingestion.file_loader import load_txt_file

txt_content = load_txt_file("backend/data/Apple_china.txt")

print(txt_content)
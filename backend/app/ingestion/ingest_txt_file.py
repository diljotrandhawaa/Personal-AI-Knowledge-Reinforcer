from ingestion import ingest_note
from file_loader import load_txt_file, load_pdf_file
from pathlib import Path

def ingest_txt_file(file_path: str):

    text = load_txt_file(file_path)

    file = Path(file_path)

    note_id = file.stem

    ingest_note(note_id, text)

def ingest_pdf_file(file_path: str):

    pdf_text = load_pdf_file(file_path)

    file = Path(file_path)

    note_id = file.stem

    ingest_note(note_id, pdf_text)
from app.ingestion.ingestion import ingest_note
from app.ingestion.file_loader import load_txt_file, load_pdf_file
from pathlib import Path

def ingest_txt_file(file_path: str):

    text = load_txt_file(file_path)

    file = Path(file_path)

    note_id = file.stem

    return ingest_note(note_id, text)

def ingest_pdf_file(file_path: str):

    pdf_text = load_pdf_file(file_path)

    file = Path(file_path)

    note_id = file.stem

    return ingest_note(note_id, pdf_text)


def ingest_file(file_path: str):

    extension = Path(file_path).suffix.lower()

    if extension == ".txt":
        return ingest_txt_file(file_path)

    elif extension == ".pdf":
        return ingest_pdf_file(file_path)

    else:
        raise ValueError(f"Unsupported file type: {extension}")

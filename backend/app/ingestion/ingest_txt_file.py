from ingestion import ingest_note
from file_loader import load_txt_file
from pathlib import Path

def ingest_txt_file(file_path: str):

    text = load_txt_file(file_path)

    file = Path(file_path)

    note_id = file.stem

    ingest_note(note_id, text)
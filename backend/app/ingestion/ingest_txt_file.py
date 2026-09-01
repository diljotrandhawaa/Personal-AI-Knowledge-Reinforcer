from ingestion import ingest_note
from file_loader import load_txt_file

def ingest_txt_file(file_path: str, note_id: str):

    text = load_txt_file(file_path)

    ingest_note(note_id, text)
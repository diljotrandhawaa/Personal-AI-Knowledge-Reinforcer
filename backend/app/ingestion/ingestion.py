from app.ingestion.chunker import chunk_text
from app.rag.vector_db import store_chunk, search_notes
from datetime import date

def ingest_note(note_id: str, note_text: str):

    nodes = chunk_text(note_text)

    for i, chunk in enumerate(nodes):

        chunk_id = f'{note_id}_chunk_{i}'
        chunk_content = chunk.get_content()
        chunk_metadata = {
            "note_id": note_id,
            "chunk_index": i,
            "source": "manual_test",
            "date_added": date.today().isoformat()
        }

        store_chunk(chunk_id, chunk_content, chunk_metadata)

        print("Chunk ID to be stored: ", chunk_id)
        print("Metadata to be stored: ", chunk_metadata)
        print("Chunk text to be stored:", chunk_content)
        print("------------------------------------------------------------")
        print("\n")
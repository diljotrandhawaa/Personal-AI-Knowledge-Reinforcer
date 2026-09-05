import chromadb
from llama_index.embeddings.ollama import OllamaEmbedding
from pathlib import Path

embed_model = OllamaEmbedding(
    model_name="embeddinggemma:latest",
    base_url="http://127.0.0.1:11435"
)

PROJECT_ROOT = Path(__file__).resolve().parents[3]
CHROMA_PATH = PROJECT_ROOT / "data" / "chroma"

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)

notes_collection = client.get_or_create_collection(
    name="notes"
)

def store_chunk(chunk_id: str, chunk_text: str, metadata: dict):

    chunk_embedding = embed_model.get_text_embedding(chunk_text)

    notes_collection.add(
        ids=[chunk_id],
        documents=[chunk_text],
        embeddings=[chunk_embedding],
        metadatas=[metadata]
    )

def search_notes(query: str, n_results: int = 1):

    query_embedding = embed_model.get_query_embedding(query)

    return notes_collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

def list_notes():
    results = notes_collection.get(include=["metadatas"])

    unique_notes = {}

    for metadata in results["metadatas"]:
        if not metadata:
            continue

        note_id = metadata.get("note_id")

        if note_id and note_id not in unique_notes:
            unique_notes[note_id] = {
                "note_id": note_id,
                "source": metadata.get("source")
            }

    return sorted(
        unique_notes.values(),
        key=lambda note: note["note_id"].lower()
    )

def delete_note(note_id: str) -> int:
    results = notes_collection.get(
        where={"note_id": note_id}
    )

    chunk_ids = results["ids"]

    if not chunk_ids:
        return 0

    notes_collection.delete(ids=chunk_ids)

    return len(chunk_ids)

# print(search_notes("What does gradients mean?"))
    
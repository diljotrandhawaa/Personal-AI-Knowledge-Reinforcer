import chromadb
from llama_index.embeddings.ollama import OllamaEmbedding

embed_model = OllamaEmbedding(model_name="embeddinggemma:latest")

client = chromadb.PersistentClient(
    path="data/chroma"
)

notes_collection = client.get_or_create_collection(
    name="notes"
)

def add_note(note_id: str, note_text: str, metadata: dict):

    note_embedding = embed_model.get_text_embedding(note_text)

    notes_collection.add(
        ids=[note_id],
        documents=[note_text],
        embeddings=[note_embedding],
        metadatas=[metadata]
    )

    print("Below Note is added:")
    print(note_text)

def search_notes(query: str, n_results: int = 3):

    query_embedding = embed_model.get_query_embedding(query)

    return notes_collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    
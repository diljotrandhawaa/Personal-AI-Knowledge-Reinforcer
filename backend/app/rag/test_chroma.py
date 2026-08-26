import chromadb
from llama_index.embeddings.ollama import OllamaEmbedding

embed_model = OllamaEmbedding(model_name="embeddinggemma:latest")

client = chromadb.PersistentClient(
    path="data/chroma"
)

demo_collection = client.get_or_create_collection(
    name="notes"
)

text = "Gradient descent is an optimization algorithm used to minimize the loss function in machine learning models. It iteratively adjusts the model's parameters in the direction of the negative gradient of the loss function with respect to the parameters."

txt_embedding = embed_model.get_text_embedding(text)

demo_collection.add(
    ids=["note_1"],
    documents=[text],
    embeddings=[txt_embedding],
    metadatas=[{"source": "manual_test"}]
)

query = "What is Photosynthesis?"

query_embedding = embed_model.get_query_embedding(query)

results = demo_collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

print(results)
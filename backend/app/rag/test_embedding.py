from llama_index.embeddings.ollama import OllamaEmbedding

embedding_model = OllamaEmbedding(model_name="embeddinggemma:latest")

print("Testing EmbeddingGemma...")

query_embed = embedding_model.get_query_embedding("How does Photosynthesis work? and what is my position in the company?")

print(len(query_embed))

print("Positive vector values:")
print(sum(vec > 0 for vec in query_embed))

print("Negative vector values:")
print(sum(vec < 0 for vec in query_embed))
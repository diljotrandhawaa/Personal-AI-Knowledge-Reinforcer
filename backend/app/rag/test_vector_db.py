from vector_db import store_chunk, search_notes

store_chunk(
    "note_3", 
    "Backpropagation calculates gradients used to update model parameters.", 
    {"source": "manual test"}
)

result = search_notes("How does a neural network calculate gradients?")

print("\nThe Retrieval result:")
print(result)
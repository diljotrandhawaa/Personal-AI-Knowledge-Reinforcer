from vector_db import add_note, search_notes

add_note(
    "note_3", 
    "Backpropagation calculates gradients used to update model parameters.", 
    {"source": "manual test"}
)

result = search_notes("How does a neural network calculate gradients?")

print("\nThe Retrieval result:")
print(result)
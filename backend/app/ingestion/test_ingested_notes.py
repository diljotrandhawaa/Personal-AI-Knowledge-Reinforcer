from app.rag.vector_db import search_notes, notes_collection

print(notes_collection.count())

notes_collection.delete(
    ids=["data_220_week_2_chunk_0"]
)

records = notes_collection.get(
    include=["documents", "metadatas"]
)

for i in range(0, notes_collection.count()):

    print(records["ids"][i])

    print(records["documents"][i])

    print("\n----------------------------------------\n")

# print(records["ids"][5])

# print(records["documents"][6])

# query1 = "How does backpropagation calculate gradients?"
# result1 = search_notes(query1)

# result_length = len(result1["documents"][0])
# print("Number of returned chunks: ", result_length)
# print(result1["ids"][0])

# for i in range(result_length):
#     print("\nChunk ID: ", result1["ids"][0][i], "\n")
#     print("Chunk's distance: ", result1["distances"][0][i], "\n")
#     print("Metadata of the chunk: ", result1["metadatas"][0][i], "\n")
#     print("The Text: \n")
#     print(result1["documents"][0][i])
#     print("-------------------------------------------------------------------------\n")
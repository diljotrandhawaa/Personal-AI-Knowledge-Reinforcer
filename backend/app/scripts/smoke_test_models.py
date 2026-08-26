from ollama import chat, embed


def test_qwen():
    print("Testing Qwen3.5...")

    response = chat(
        model="qwen3.5:4b",
        messages=[
            {
                "role": "user",
                "content": "Reply with exactly: Qwen connection successful",
            }
        ],
    )

    print("Qwen response:", response.message.content)


def test_embedding_model():
    print("\nTesting EmbeddingGemma...")

    response = embed(
        model="embeddinggemma",
        input="What is gradient descent?",
    )

    embedding = response.embeddings[0]

    print("Embedding generated successfully")
    print("Embedding dimensions:", len(embedding))
    print("First 5 values:", embedding[:5])


if __name__ == "__main__":
    test_qwen()
    test_embedding_model()
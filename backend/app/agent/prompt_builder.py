
def build_prompt(question: str, retrieved_chunks: list[str]):

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
    Use the provided context to answer the question.

    CONTEXT:
    {context}

    QUESTION:
    {question}

    ANSWER:
    """

    return prompt

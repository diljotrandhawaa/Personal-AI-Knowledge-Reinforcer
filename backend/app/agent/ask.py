from prompt_builder import build_prompt
from app.rag.vector_db import search_notes
from app.models.llm import generate_response

def ask_question(question: str):

    retrieved_text = search_notes(question)['documents'][0]

    prompt = build_prompt(question, retrieved_text)

    llm_response = generate_response(prompt)

    return llm_response
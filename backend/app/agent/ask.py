from prompt_builder import build_prompt
from app.rag.vector_db import search_notes
from app.models.llm import generate_response

def ask_question(question: str):

    # This is the list of 3 closest texts in the VectorDB
    retrieved_text = search_notes(question)['documents'][0]

    # This is the Prompt string. list of 3 closest texts is joined into a string with the question. 
    prompt = build_prompt(question, retrieved_text)

    # This is the llm response. LLM is queried with the prompt string.
    llm_response = generate_response(prompt)

    return llm_response
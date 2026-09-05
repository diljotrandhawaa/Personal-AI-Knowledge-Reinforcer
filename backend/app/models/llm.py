from llama_index.llms.ollama import Ollama

llm = Ollama(
    model="qwen3:4b",
    base_url="http://127.0.0.1:11434",
    request_timeout=300.0,
    context_window=8192,
    additional_kwargs={
        "options": {
            "num_predict": 512
        }
    },
    thinking=False
)

NO_KNOWLEDGE_RESPONSE = (
    "I couldn't find relevant information in your stored knowledge."
)


# This function basically ask LLM a question. It adds a "no_think" at the end.
def generate_response(prompt: str):

    prompt = prompt + "\n/no_think"

    response = llm.complete(prompt)

    response_text = response.text

    if "</think>" in response_text:
        # print(response_text)
        print(response_text.split("</think>", 1))
        response_text = response_text.rsplit("</think>", 1)[-1]

    response_text = response_text.strip()

    if response_text.lower() in {"/no_think", "no_think"}:
        return NO_KNOWLEDGE_RESPONSE

    return response_text
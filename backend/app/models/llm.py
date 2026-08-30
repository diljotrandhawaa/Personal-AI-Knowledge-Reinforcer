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

def generate_response(prompt: str):

    prompt = prompt + "\n/no_think"

    response = llm.complete(prompt)

    return str(response)
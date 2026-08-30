from app.agent.prompt_builder import build_prompt

question = "How does gradient descent work?"

retrieved_chunks = [
    "Gradient descent updates model parameters to reduce loss.",
    "The learning rate controls how large each update is."
]

prompt = build_prompt(question, retrieved_chunks)

print(prompt)
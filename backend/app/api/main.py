from fastapi import FastAPI
from app.api.schemas import AskRequest, AskResponse
from app.agent.ask import ask_question

app = FastAPI(
    title="Personal AI Agent API",
    description="Local API for the Personal AI Agent",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Personal AI Agent API is running"}

@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):

    answer = ask_question(request.question)


    return AskResponse(
        answer=answer
    )
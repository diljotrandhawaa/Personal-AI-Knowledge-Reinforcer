import shutil
import tempfile
from pathlib import Path
from app.rag.vector_db import list_notes

from fastapi import FastAPI, File, HTTPException, UploadFile
from app.ingestion.ingest_file import ingest_file
from app.api.schemas import AskRequest, AskResponse, IngestResponse, DocumentListResponse

app = FastAPI(
    title="Personal AI Agent API",
    description="Local API for the Personal AI Agent",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Personal AI Agent API is running"}

@app.post("/ask", response_model=AskResponse)
def ask_api(request: AskRequest):

    try:

        answer = ask_question(request.question)

        return AskResponse(
            answer=answer
        )

    except Exception as error:
        print(f"Error while answering question: {error}")

        raise HTTPException (
            status_code = 500,
            detail="The agent could not generate an answer."
        ) from error

@app.post("/ingest", response_model=IngestResponse)
def ingest_document(file: UploadFile = File(...)):
    filename = Path(file.filename or "").name
    extension = Path(filename).suffix.lower()

    if extension not in {".txt", ".pdf"}:
        raise HTTPException(
            status_code=400,
            detail="Only TXT and PDF files are supported."
        )

    try:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory) / filename

            with temporary_path.open("wb") as saved_file:
                shutil.copyfileobj(file.file, saved_file)

            result_message = ingest_file(str(temporary_path))

        return IngestResponse(
            status="success",
            filename=filename,
            message=result_message
        )

    except Exception as error:
        print(f"Error while ingesting document: {error}")

        raise HTTPException(
            status_code=500,
            detail="The document could not be ingested."
        ) from error

    finally:
        file.file.close()

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "api": "running"
    }

@app.get("/documents", response_model=DocumentListResponse)
def get_documents():
    try:
        documents = list_notes()
        return DocumentListResponse(documents=documents)

    except Exception as error:
        print(f"Error while listing documents: {error}")

        raise HTTPException(
            status_code=500,
            detail="The stored documents could not be retrieved."
        ) from error
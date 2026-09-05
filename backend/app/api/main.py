import shutil
import tempfile
from pathlib import Path
from app.rag.vector_db import list_notes, delete_note, search_notes
from app.agent.ask import ask_question

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from app.ingestion.ingest_file import ingest_file
from app.api.schemas import (
    AskRequest,
    AskResponse,
    DeleteDocumentResponse,
    DocumentListResponse,
    IngestResponse,
    SearchRequest,
    SearchResponse,
    SearchResult,
)

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

@app.delete(
    "/documents/{note_id}",
    response_model=DeleteDocumentResponse
)
def delete_document(note_id: str):
    try:
        chunks_deleted = delete_note(note_id)

        if chunks_deleted == 0:
            raise HTTPException(
                status_code=404,
                detail=f"Document '{note_id}' was not found."
            )

        return DeleteDocumentResponse(
            status="success",
            note_id=note_id,
            chunks_deleted=chunks_deleted
        )

    except HTTPException:
        raise

    except Exception as error:
        print(f"Error while deleting document: {error}")

        raise HTTPException(
            status_code=500,
            detail="The document could not be deleted."
        ) from error

@app.post("/search", response_model=SearchResponse)
def search_documents(request: SearchRequest):
    try:
        raw_results = search_notes(
            query=request.query,
            n_results=request.n_results
        )

        ids = raw_results["ids"][0]
        documents = raw_results["documents"][0]
        metadatas = raw_results["metadatas"][0]
        distances = raw_results["distances"][0]

        results = []

        for index, chunk_id in enumerate(ids):
            results.append(
                SearchResult(
                    chunk_id=chunk_id,
                    document=documents[index],
                    metadata=metadatas[index],
                    distance=distances[index]
                )
            )

        return SearchResponse(results=results)

    except Exception as error:
        print(f"Error while searching documents: {error}")

        raise HTTPException(
            status_code=500,
            detail="The document search could not be completed."
        ) from error

CHAT_PAGE = Path(__file__).resolve().parents[1] / "static" / "chat.html"


@app.get("/chat", include_in_schema=False)
def chat_page():
    return FileResponse(CHAT_PAGE)
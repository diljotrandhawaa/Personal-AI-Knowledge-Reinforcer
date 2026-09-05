from typing import Any
from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str

class IngestResponse(BaseModel):
    status: str
    filename: str
    message: str

class DocumentSummary(BaseModel):
    note_id: str
    source: str | None = None


class DocumentListResponse(BaseModel):
    documents: list[DocumentSummary]

class DeleteDocumentResponse(BaseModel):
    status: str
    note_id: str
    chunks_deleted: int

class SearchRequest(BaseModel):
    query: str
    n_results: int = Field(default=1, ge=1, le=20)


class SearchResult(BaseModel):
    chunk_id: str
    document: str
    metadata: dict[str, Any] | None = None
    distance: float | None = None


class SearchResponse(BaseModel):
    results: list[SearchResult]
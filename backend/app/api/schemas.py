from pydantic import BaseModel


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
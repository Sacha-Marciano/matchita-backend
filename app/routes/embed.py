# routes/duplicate_check.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.vertex_embedding import embed_text_chunks

router = APIRouter()

class DocInput(BaseModel):
    text: str

@router.post("/embed")
def embed(doc: DocInput):
    embeddings = embed_text_chunks(doc.text)
    return {
        "embeddings" : embeddings[0],
    }

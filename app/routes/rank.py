# routes/classify.py
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.services.gemini_rank import rank_document

router = APIRouter()

class DocumentInput(BaseModel):
    id: str
    title: str
    folder: str
    tags: List[str]
    createdAt: datetime

class TextInput(BaseModel):
    question: str
    docs: List[DocumentInput]

@router.post("/rank")
def rank(input_data: TextInput):
    result = rank_document(input_data.question,input_data.docs)
    if not result:
        return {"error": "Gemini ranking failed"}
    return result

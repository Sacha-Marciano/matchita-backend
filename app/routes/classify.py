# routes/classify.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_classify import classify_document

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/classify")
def classify(text_input: TextInput):
    result = classify_document(text_input.text)
    if not result:
        return {"error": "Gemini classification failed"}
    return result

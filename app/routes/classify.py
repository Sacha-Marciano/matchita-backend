# routes/classify.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_classify import classify_document

router = APIRouter()

class TextInput(BaseModel):
    title: str
    text: str
    folders : list[str]
    tags : list[str]

@router.post("/classify")
def classify(input_data: TextInput):
    result = classify_document(input_data.title, input_data.text,input_data.folders, input_data.tags)
    if not result:
        return {"error": "Gemini classification failed"}
    return result

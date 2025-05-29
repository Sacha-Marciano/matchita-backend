# routes/classify.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_extract import extract_answer

router = APIRouter()

class TextInput(BaseModel):
    question: str
    text: str

@router.post("/extract")
def extract(input_data: TextInput):
    result = extract_answer(input_data.question,input_data.text)
    if not result:
        return {"error": "Gemini extract failed"}
    return result

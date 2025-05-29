# services/gemini_rank.py
from vertexai.generative_models import GenerativeModel
import json
import re
from datetime import datetime
from pydantic import BaseModel
from typing import List

gemini = GenerativeModel("gemini-2.0-flash-lite-001")

class DocumentInput(BaseModel):
    id: str
    title: str
    folder: str
    tags: List[str]
    createdAt: datetime

def clean_json_response(response_text: str):
    # Remove ```json ... ``` or ``` ... ``` if they surround the content
    if response_text.startswith("```") and response_text.endswith("```"):
        response_text = re.sub(r"^```(?:json)?\n?", "", response_text)
        response_text = re.sub(r"\n?```$", "", response_text)
    return response_text

def rank_document(question: str, docs: List[DocumentInput] ):
    prompt = (
        f"You are an intelligent assistant. Rank the following documents based on their relevance to answering the user's question:\n"
        f"- Provide an array of document IDs ranked by relevance (most relevant first).\n\n"
        f"Question:\n"
        f"{question}\n\n"
        f"Documents:\n"
        f"{docs}\n\n"
        f"Respond only in JSON format with an array of document IDs, e.g., [\"doc_id_1\", \"doc_id_2\", \"doc_id_3\"]."
    )

    response = gemini.generate_content(prompt)
    # Use streaming=False to simplify
    try:
        json_response_raw = response.text.strip()
        json_response_cleaned = clean_json_response(json_response_raw)
        parsed = json.loads(json_response_cleaned)
        return {"rankedDocIds" : parsed}
    except Exception as e:
        print("Gemini rank failed:", e)
        return None

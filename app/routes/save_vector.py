# app/routes/save_vector.py

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List
import uuid
from app.services.matching_engine import upsert_vector_to_index, normalize_vector

router = APIRouter()

class VectorInput(BaseModel):
    vector: list[float]

@router.post("/save-vector")
def save_vector(data: VectorInput):
    try:
        # Use UUID for index-level uniqueness
        vector_id = str(uuid.uuid4())

        normalized_vector=normalize_vector(data.vector)
        upsert_vector_to_index(vector_id=vector_id, vector=normalized_vector)

        return {"status": "success", "vector_id": vector_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

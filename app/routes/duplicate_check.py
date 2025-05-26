# routes/duplicate_check.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.vertex_embedding import embed_text_chunks
from app.services.matching_engine import find_nearest_neighbors

router = APIRouter()

class DocInput(BaseModel):
    text: str
    room_id: str

@router.post("/duplicate-check")
def check_duplicate(doc: DocInput):
    embeddings = embed_text_chunks(doc.text)
    avg_vector = [sum(dim) / len(embeddings) for dim in zip(*embeddings)]

    neighbors = find_nearest_neighbors(avg_vector)
    if not neighbors:
        return {"is_duplicate": False}

    top_score = neighbors[0].distance
    print("Top match score:", top_score)

    is_duplicate = top_score < 0.1  # You can tune this threshold
    return {
        "is_duplicate": is_duplicate,
        "match_score": top_score
    }

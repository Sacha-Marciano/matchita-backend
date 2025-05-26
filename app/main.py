# main.py
from fastapi import FastAPI
from app.routes import duplicate_check, classify
import vertexai

app = FastAPI()

# Init VertexAI
vertexai.init(project="571768511871", location="us-central1")

app.include_router(duplicate_check.router)
app.include_router(classify.router)

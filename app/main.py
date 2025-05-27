from fastapi import FastAPI
from app.routes import embed, classify
import vertexai

app = FastAPI()

# Init VertexAI
vertexai.init(project="571768511871", location="us-central1")

app.include_router(embed.router)
app.include_router(classify.router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import embed, classify, rank, extract
import vertexai

app = FastAPI()

# Init VertexAI
vertexai.init(project="571768511871", location="us-central1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-frontend-domain.com"],  # <-- frontend dev/prod URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(embed.router)
app.include_router(classify.router)
app.include_router(rank.router)
app.include_router(extract.router)

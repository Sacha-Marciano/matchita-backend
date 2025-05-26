# main.py
from fastapi import FastAPI
from app.routes import duplicate_check, classify, save_vector
import vertexai
from google.oauth2 import service_account

# Load credentials from a JSON file (ensure it's in your Render environment)
credentials = service_account.Credentials.from_service_account_file("drive-viewer-app-460607-cf8dc1b9a8e0.json")
# Init VertexAI
vertexai.init(project="571768511871", location="us-central1",credentials=credentials)


app = FastAPI()

app.include_router(duplicate_check.router)
app.include_router(classify.router)
app.include_router(save_vector.router)
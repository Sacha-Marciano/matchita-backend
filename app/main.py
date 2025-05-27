# main.py
from fastapi import FastAPI
from app.routes import duplicate_check, classify, save_vector
import vertexai

import os
import json
from google.oauth2 import service_account

# Load credentials from a JSON file (ensure it's in your Render environment)
credentials_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
if not credentials_json:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS_JSON not set")

credentials_dict = json.loads(credentials_json)
credentials = service_account.Credentials.from_service_account_info(credentials_dict)

# Init VertexAI
vertexai.init(project="571768511871", location="us-central1",credentials=credentials)


app = FastAPI()

app.include_router(duplicate_check.router)
app.include_router(classify.router)
app.include_router(save_vector.router)
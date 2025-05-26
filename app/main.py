# main.py
from fastapi import FastAPI
from app.routes import duplicate_check, classify, save_vector
import vertexai
from dotenv import load_dotenv
from google.oauth2 import service_account
import os
import json

load_dotenv()

# Load credentials from a JSON file (ensure it's in your Render environment)
SERVICE_ACCOUNT_INFO = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"])
credentials = service_account.Credentials.from_service_account_info(SERVICE_ACCOUNT_INFO)

# Init VertexAI
vertexai.init(project="571768511871", location="us-central1",credentials=credentials)


app = FastAPI()

app.include_router(duplicate_check.router)
app.include_router(classify.router)
app.include_router(save_vector.router)
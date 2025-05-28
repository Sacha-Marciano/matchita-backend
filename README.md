To run in dec :
uvicorn app.main:app --reload

To build :
gcloud builds submit --tag gcr.io/drive-viewer-app-460607/fastapi-gemini

To deploy on cloud run :
gcloud run deploy fastapi-gemini --image gcr.io/drive-viewer-app-460607/fastapi-gemini --platform managed --region us-central1 --allow-unauthenticated --port 8080
